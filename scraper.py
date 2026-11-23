import asyncio
import json
import logging
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from playwright.async_api import async_playwright

load_dotenv()

LOG_FILE = Path("output/errors.log")


def setup_logger() -> logging.Logger:
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("scraper")
    logger.setLevel(logging.ERROR)
    handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
    logger.handlers.clear()
    logger.addHandler(handler)
    return logger


log = setup_logger()

START_URL = os.getenv("FULLCYCLE_URL", "")

import platform

def get_chrome_path() -> str:
    system = platform.system()
    if system == "Windows":
        paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        ]
        for p in paths:
            if os.path.exists(p):
                return p
        return ""
    elif system == "Darwin":  # macOS
        return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    else:  # Linux
        for p in ["/usr/bin/google-chrome", "/usr/bin/chrome"]:
            if os.path.exists(p):
                return p
        return ""

CHROME_PATH = get_chrome_path()
PROFILE_DIR = str(Path.home() / ".fullcycle-scraper-profile")
JS_FILE = Path(__file__).parent / "scripts" / "extract_page.js"


def info(msg: str, indent: int = 0) -> None:
    prefix = "  " * indent
    print(f"{prefix}[+] {msg}")


def step(msg: str, indent: int = 0) -> None:
    prefix = "  " * indent
    print(f"{prefix}>>> {msg}")


def warn(msg: str, indent: int = 0) -> None:
    prefix = "  " * indent
    print(f"{prefix}[!] {msg}")


def load_extract_js() -> str:
    source = JS_FILE.read_text(encoding="utf-8")
    source = re.sub(r"console\.log\(output\);.*", "return output;\n})();", source, flags=re.DOTALL)
    return source


def slugify(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*\n\r]', '', name)
    return name.strip(" .")[:80].rstrip(" .")


GET_METADATA_JS = """
() => {
  // Curso: último link do breadcrumb
  const curso = Array.from(document.querySelectorAll('[data-testid="BREADCRUMB_LINK"]'))
    .pop()?.textContent?.trim() || 'N/A';

  // Aula: item com aria-selected="true"
  const aulaEl = document.querySelector('li[aria-selected="true"]');
  const aula = aulaEl?.querySelector('.css-om3vjz')?.textContent?.trim() || 'N/A';

  // Capítulo: accordion pai do item selecionado
  let capitulo = 'N/A';
  let el = aulaEl?.parentElement;
  while (el && el !== document.body) {
    if (el.id?.startsWith('chapter-')) {
      const h5 = el.querySelector('h5');
      if (h5) {
        // Pega apenas os text nodes diretos, ignorando o <main> filho
        capitulo = Array.from(h5.childNodes)
          .filter(n => n.nodeType === 3)
          .map(n => n.textContent.trim())
          .filter(Boolean)
          .join(' ') || 'N/A';
      }
      break;
    }
    el = el.parentElement;
  }

  return JSON.stringify({ curso, capitulo, aula });
}
"""


def save(output: str, curso: str, capitulo: str, aula: str) -> Path:
    out_dir = Path("output") / slugify(curso) / slugify(capitulo)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slugify(aula)}.md"
    # Preserva Resumo IA já gerado caso o arquivo esteja sendo re-extraído
    if out_path.exists() and "[RESUMO_IA]" in output:
        existing = out_path.read_text(encoding="utf-8")
        marker = "## Resumo IA\n\n"
        if marker in existing and "[RESUMO_IA]" not in existing:
            existing_ia = existing.split(marker, 1)[1]
            output = output.replace("[RESUMO_IA]", existing_ia)
    out_path.write_text(output, encoding="utf-8")
    info(f"Salvo: {out_path}", indent=2)
    return out_path


async def get_metadata(page) -> dict:
    raw = await page.evaluate(GET_METADATA_JS)
    return json.loads(raw) if raw else {"curso": "N/A", "capitulo": "N/A", "aula": "N/A"}


HAS_TRANSCRIPT_JS = """
() => Array.from(document.querySelectorAll('span')).some(s =>
    s.children.length === 0 &&
    /^\\d{2}:\\d{2}(:\\d{2})?$/.test(s.textContent.trim()) &&
    s.parentElement &&
    s.parentElement.textContent.trim().length > s.textContent.trim().length + 2
)
"""


GET_FIRST_TRANSCRIPT_JS = """
() => {
    const s = Array.from(document.querySelectorAll('span')).find(s =>
        s.children.length === 0 &&
        /^\\d{2}:\\d{2}(:\\d{2})?$/.test(s.textContent.trim()) &&
        s.parentElement &&
        s.parentElement.textContent.trim().length > s.textContent.trim().length + 2
    );
    return s ? s.parentElement.textContent.trim().slice(0, 120) : '';
}
"""


async def extract(page, lesson_name: str = "", prev_transcript_head: str = "") -> str | None:
    # Aguarda os controles da aula (Resumo ou botão de Transcrição) renderizarem
    try:
        await page.wait_for_function(
            """() => {
                const btns = Array.from(document.querySelectorAll('button'));
                const hasTransBtn = btns.some(b => /transcri/i.test(b.textContent || ''));
                const hasResumo = !!document.querySelector('h5.css-rymwba');
                return hasTransBtn || hasResumo;
            }""",
            timeout=8000,
        )
    except Exception:
        pass

    # Abre o bloco Resumo da Aula se existir botão de expandir
    try:
        resumo_btn = page.locator('button.MuiButton-root:has-text("Resumo da Aula")').first
        if await resumo_btn.count() > 0:
            await resumo_btn.click(timeout=2000)
            await page.wait_for_timeout(300)
    except Exception:
        pass

    # Clica no botão Mostrar Transcrição (sem exigir role="tab", pois é um <button> comum)
    try:
        show_btn = page.locator('button:has-text("Mostrar Transcrição")').first
        if await show_btn.count() > 0:
            step("Clicando no botão Mostrar Transcrição...", indent=2)
            await show_btn.scroll_into_view_if_needed(timeout=3000)
            await show_btn.click(timeout=4000)
            step("Aguardando segmentos carregarem...", indent=2)
            await page.wait_for_function(HAS_TRANSCRIPT_JS, timeout=5000)
        elif await page.locator('button:has-text("Ocultar Transcrição")').count() > 0:
            # Painel já aberto; aguarda atualizar caso ainda esteja mostrando a aula anterior
            if prev_transcript_head:
                try:
                    await page.wait_for_function(
                        f"""(prev) => {{
                            const s = Array.from(document.querySelectorAll('span')).find(s =>
                                s.children.length === 0 &&
                                /^\\d{{2}}:\\d{{2}}(:\\d{{2}})?$/.test(s.textContent.trim()) &&
                                s.parentElement &&
                                s.parentElement.textContent.trim().length > s.textContent.trim().length + 2
                            );
                            const cur = s ? s.parentElement.textContent.trim().slice(0, 120) : '';
                            return cur !== prev;
                        }}""",
                        arg=prev_transcript_head,
                        timeout=4000,
                    )
                except Exception:
                    pass
            try:
                await page.wait_for_function(HAS_TRANSCRIPT_JS, timeout=3000)
            except Exception:
                pass
        else:
            warn("Botão de transcrição não encontrado nesta aula.", indent=2)
    except Exception:
        warn("Transcrição não carregou nesta aula. Prosseguindo com extração do resumo...", indent=2)

    step("Executando script de extração...", indent=2)
    try:
        js = load_extract_js()
        return await page.evaluate(js)
    except Exception as e:
        msg = f"Erro ao executar JS | aula={lesson_name!r} | url={page.url} | {e}"
        warn(msg, indent=2)
        log.error(msg)
        return None


async def scrape_module(page, module_url: str) -> tuple[int, int, int, int]:
    step(f"Abrindo módulo: {module_url}")
    await page.goto(module_url, wait_until="domcontentloaded", timeout=30000)
    await page.wait_for_timeout(2000)

    step("Aguardando sidebar renderizar...")
    try:
        await page.wait_for_function(
            """() => {
                const count = document.querySelectorAll('[id^="chapter-"]').length;
                if (count === 0) return false;
                window.__chapterCount = count;
                return true;
            }""",
            timeout=60000,
        )
        await page.wait_for_function(
            """() => {
                const count = document.querySelectorAll('[id^="chapter-"]').length;
                return count > 0 && count === window.__chapterCount;
            }""",
            polling=1000,
            timeout=10000,
        )
    except Exception as e:
        msg = f"Sidebar não renderizou | url={page.url} | {e}"
        log.error(msg)
        raise RuntimeError(msg) from e
    info(f"URL após renderização: {page.url}")

    # Coleta estrutura do módulo (apenas <li>, ignora <a> de links externos)
    step("Coletando estrutura do módulo...")
    all_lessons: list[dict] = []

    chapters = await page.query_selector_all('[id^="chapter-"]')
    info(f"{len(chapters)} capítulos encontrados.")

    chapter_idx = 0
    for chapter_el in chapters:
        title_el = await chapter_el.query_selector('h5')
        if not title_el:
            continue

        chapter_name = await page.evaluate(
            """(h5) => Array.from(h5.childNodes)
                .filter(n => n.nodeType === 3)
                .map(n => n.textContent.trim())
                .filter(Boolean)
                .join(' ')""",
            title_el,
        )
        if not chapter_name:
            continue

        collapsed_btn = await chapter_el.query_selector('button[aria-expanded="false"]')
        if collapsed_btn:
            try:
                await collapsed_btn.scroll_into_view_if_needed(timeout=5000)
                await collapsed_btn.click(timeout=8000)
                await page.wait_for_timeout(300)
            except Exception:
                pass

        lesson_els = await chapter_el.query_selector_all('li[id^="list-content-"]')
        if not lesson_els:
            continue

        chapter_idx += 1
        chapter_label = f"{chapter_idx:02d} - {chapter_name}"

        for idx, lesson_el in enumerate(lesson_els, 1):
            content_id = await lesson_el.get_attribute('id')
            name_el = await lesson_el.query_selector('.css-om3vjz')
            if not name_el or not content_id:
                continue
            all_lessons.append({
                'id': content_id,
                'name': (await name_el.inner_text()).strip(),
                'chapter': chapter_label,
                'index': idx,
            })

    info(f"{len(all_lessons)} aulas no total.")

    meta_inicial = await get_metadata(page)
    curso = meta_inicial['curso']
    info(f"Curso/Módulo: {curso}")
    print()

    total = len(all_lessons)
    saved = skipped = errors = 0

    for j, lesson in enumerate(all_lessons, 1):
        lesson_name = lesson['name']
        chapter_label = lesson['chapter']
        content_id = lesson['id']
        lesson_idx = lesson['index']
        lesson_filename = f"{lesson_idx:02d} - {lesson_name}"

        out_path = Path("output") / slugify(curso) / slugify(chapter_label) / f"{slugify(lesson_filename)}.md"
        if out_path.exists() and "[TRANSCRIÇÃO]" not in out_path.read_text(encoding="utf-8"):
            info(f"[{j}/{total}] {lesson_filename} — já existe, pulando.", indent=1)
            skipped += 1
            continue

        step(f"[{j}/{total}] {chapter_label} / {lesson_filename}", indent=1)

        prev_url = page.url
        prev_transcript_head = await page.evaluate(GET_FIRST_TRANSCRIPT_JS)
        selector = f'#{content_id}'
        nav_ok = False
        for attempt in range(1, 3):
            try:
                await page.evaluate(
                    f"""() => {{
                        const el = document.querySelector("{selector}");
                        if (el) el.click();
                    }}"""
                )
                if page.url == prev_url:
                    try:
                        await page.wait_for_function(
                            f"() => window.location.href !== {json.dumps(prev_url)}",
                            timeout=5000,
                        )
                    except Exception:
                        info("Já na aula correta (URL não mudou).", indent=2)
                        prev_transcript_head = ""
                nav_ok = True
                break
            except Exception as e:
                warn(f"Tentativa {attempt} falhou: {e}", indent=2)
                await page.wait_for_timeout(1500)

        if not nav_ok:
            msg = f"Erro ao navegar após 2 tentativas | aula={lesson_name!r}"
            warn(msg, indent=2)
            log.error(msg)
            errors += 1
            continue

        await page.wait_for_function(
            "() => document.readyState === 'complete'",
            timeout=15000,
        )
        # Pequena espera para React atualizar o conteúdo da nova aula antes de extrair
        await page.wait_for_timeout(800)

        meta = await get_metadata(page)

        output = await extract(page, lesson_name, prev_transcript_head=prev_transcript_head)
        if not output:
            warn("Falha na extração, salvando com placeholder.", indent=2)
            log.error(f"Falha na extração | aula={lesson_name!r} | url={page.url}")
            output = "\n".join([
                f"Módulo: {meta['curso']}\\",
                f"Aula: [{lesson_name}]({page.url})",
                "",
                "## Resumo da aula",
                "",
                "",
                "## Transcrição",
                "",
                "[TRANSCRIÇÃO]",
                "",
                "## Resumo IA",
                "",
                "[RESUMO_IA]",
            ])

        save(output, curso, chapter_label, lesson_filename)
        saved += 1
        await page.wait_for_timeout(400)

    print("=" * 50)
    info(f"Módulo '{curso}' concluído! Total: {total} | Salvas: {saved} | Puladas: {skipped} | Erros: {errors}")
    print("=" * 50)
    return total, saved, skipped, errors


async def main():
    urls = sys.argv[1:] if len(sys.argv) > 1 else ([START_URL] if START_URL else [])
    if not urls:
        raise RuntimeError("Nenhuma URL fornecida (passe via CLI ou defina FULLCYCLE_URL no .env)")

    email = os.getenv("FULLCYCLE_EMAIL", "")
    password = os.getenv("FULLCYCLE_PASSWORD", "")

    step("Iniciando navegador Chrome...")
    async with async_playwright() as p:
        launch_args = {
            "user_data_dir": PROFILE_DIR,
            "headless": False,
        }
        if CHROME_PATH and os.path.exists(CHROME_PATH):
            launch_args["executable_path"] = CHROME_PATH
            info(f"Usando Chrome em: {CHROME_PATH}", indent=1)
        else:
            launch_args["channel"] = "chrome"
            info("Usando canal 'chrome' padrão do Playwright", indent=1)

        ctx = await p.chromium.launch_persistent_context(**launch_args)
        page = await ctx.new_page()

        first_url = urls[0]
        step("Abrindo URL inicial para checar autenticação...")
        await page.goto(first_url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(3000)

        info(f"URL atual: {page.url}")

        needs_login = "login" in page.url.lower() or bool(await page.query_selector('input[type="password"]'))

        if needs_login:
            if email and password:
                step("Página de login detectada. Fazendo login automático...")
                try:
                    email_input = page.locator('input[name="email"]:visible').first
                    await email_input.wait_for(state="visible", timeout=10000)
                    step("Preenchendo e-mail...", indent=1)
                    await email_input.fill(email)

                    password_input = page.locator('input[name="password"]:visible').first
                    await password_input.wait_for(state="visible", timeout=10000)
                    step("Preenchendo senha...", indent=1)
                    await password_input.fill(password)

                    step("Clicando em entrar...", indent=1)
                    await page.locator('button[type="submit"]:visible').first.click()

                    step("Aguardando redirecionamento pós-login...", indent=1)
                    await page.wait_for_url(lambda url: "login" not in url, timeout=20000)
                    await page.wait_for_load_state("domcontentloaded", timeout=15000)
                    info("Login realizado com sucesso.")
                except Exception as e:
                    msg = f"Erro no login automático | {e}"
                    warn(msg, indent=1)
                    log.error(msg)
                    warn("Faça o login manualmente no navegador e pressione Enter aqui...")
                    input()
            else:
                warn("Login necessário. Faça o login no navegador e pressione Enter aqui...")
                input()

        grand_total = grand_saved = grand_skipped = grand_errors = 0
        for url in urls:
            t, s, sk, er = await scrape_module(page, url)
            grand_total += t
            grand_saved += s
            grand_skipped += sk
            grand_errors += er

        print("=" * 50)
        info("TUDO CONCLUÍDO!")
        info(f"Total: {grand_total} | Salvas: {grand_saved} | Puladas: {grand_skipped} | Erros: {grand_errors}")
        if grand_errors:
            info(f"Detalhes em: {LOG_FILE}")
        print("=" * 50)

        await ctx.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        log.error(f"Erro fatal | {e}")
        raise
