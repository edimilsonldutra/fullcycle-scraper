"""Compila o livro a partir de capitulos/*.md.

Gera, nesta pasta:
  - LIVRO_ENGENHARIA_DE_SOFTWARE_COM_IA.md   (livro completo com sumario)
  - LIVRO_ENGENHARIA_DE_SOFTWARE_COM_IA.html (Markdown embutido, renderizado no navegador)
  - LIVRO_ENGENHARIA_DE_SOFTWARE_COM_IA.pdf  (A4, via Playwright + Chrome/Edge instalado)

Uso:
  python build_livro.py            # MD + HTML + PDF
  python build_livro.py --no-pdf   # apenas MD + HTML
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHAPTERS_DIR = ROOT / "capitulos"
BASENAME = "LIVRO_ENGENHARIA_DE_SOFTWARE_COM_IA"
MD_OUT = ROOT / f"{BASENAME}.md"
HTML_OUT = ROOT / f"{BASENAME}.html"
PDF_OUT = ROOT / f"{BASENAME}.pdf"

SEP = "\n\n\n---\n\n\n"

# Parte que abre antes do capitulo indicado (prefixo do arquivo)
PARTS = {
    "01": "# Parte I — Fundamentos, Prompts e Contexto Estruturado",
    "04": "# Parte II — Desenvolvimento em Modo Agente e Extensibilidade",
    "07": "# Parte III — Arquitetura, Sistemas Agênticos, Protocolos e Operação",
}

# Mesmo algoritmo do slugify do HTML (mantenha os dois sincronizados)
JS_SLUGIFY = (
    'const slugify = (s) => s.trim().toLowerCase()'
    '.replace(/[^\\p{L}\\p{N}_\\s-]/gu, "").replace(/\\s+/g, "-");'
)


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text)


def plain_heading(md_title: str) -> str:
    """Aproxima o textContent que o navegador vera no heading renderizado."""
    title = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md_title)
    return title.replace("`", "").replace("*", "").replace("_", "_")


def headings_outside_code(md: str):
    in_fence = False
    for line in md.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,2})\s+(.+?)\s*$", line)
        if m:
            yield len(m.group(1)), m.group(2)


def build_toc(chapters: list[str]) -> str:
    lines = ["## Sumário", ""]
    seen: dict[str, int] = {}
    for md in chapters:
        for level, title in headings_outside_code(md):
            slug = slugify(plain_heading(title))
            if slug in seen:
                raise SystemExit(f"Slug duplicado no sumario: {slug!r} ({title!r})")
            seen[slug] = 1
            if level == 1:
                lines.append(f"- **[{title}](#{slug})**")
            else:
                lines.append(f"  - [{title}](#{slug})")
    return "\n".join(lines)


def build_markdown() -> str:
    files = sorted(CHAPTERS_DIR.glob("*.md"))
    if not files or not files[0].name.startswith("00"):
        raise SystemExit("capitulos/00_*.md (prefacio) nao encontrado")
    preface = files[0].read_text(encoding="utf-8").strip()
    chapter_files = files[1:]
    chapters = [f.read_text(encoding="utf-8").strip() for f in chapter_files]

    parts = [preface, build_toc(chapters)]
    for f, md in zip(chapter_files, chapters):
        part = PARTS.get(f.name[:2])
        parts.append(f"{part}\n\n\n{md}" if part else md)
    return SEP.join(parts) + "\n"


def build_html(md: str) -> str:
    html = HTML_OUT.read_text(encoding="utf-8")
    payload = json.dumps(md, ensure_ascii=False).replace("</", "<\\/")
    pattern = re.compile(r'(<script id="raw-markdown" type="application/json">)(.*?)(</script>)', re.S)
    if not pattern.search(html):
        raise SystemExit("Bloco raw-markdown nao encontrado no HTML modelo")
    html = pattern.sub(lambda m: m.group(1) + payload + m.group(3), html, count=1)
    html = re.sub(r"const slugify = \(s\) => [^\n]*", lambda _m: JS_SLUGIFY, html, count=1)
    return html


def build_pdf() -> int:
    from playwright.sync_api import sync_playwright

    footer = (
        '<div style="width:100%;font-size:7.5pt;color:#64748b;padding:0 18mm;'
        'display:flex;justify-content:space-between;font-family:Segoe UI,Arial,sans-serif;">'
        "<span>MBA FullCycle — Síntese Técnica</span>"
        '<span>Página <span class="pageNumber"></span> de <span class="totalPages"></span></span></div>'
    )
    with sync_playwright() as p:
        browser = None
        for channel in ("chrome", "msedge"):
            try:
                browser = p.chromium.launch(channel=channel)
                break
            except Exception:
                continue
        if browser is None:
            browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(HTML_OUT.as_uri(), wait_until="networkidle")
        page.wait_for_function("window.__BOOK_RENDER_STATUS__ && window.__BOOK_RENDER_STATUS__.done", timeout=120_000)
        status = page.evaluate("window.__BOOK_RENDER_STATUS__")
        broken = page.evaluate(
            """() => [...document.querySelectorAll('#book-content a[href^="#"]')]
                .map(a => decodeURIComponent(a.getAttribute('href').slice(1)))
                .filter(id => !document.getElementById(id))"""
        )
        print(f"Mermaid: {status['mermaidOk']}/{status['mermaidTotal']} | tabelas: {status['tableCount']} | H1: {status['h1Count']}")
        if status["mermaidErrors"]:
            print("Erros Mermaid:", json.dumps(status["mermaidErrors"], ensure_ascii=False, indent=2))
        if broken:
            print("Links internos quebrados:", broken)
        page.pdf(
            path=str(PDF_OUT),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=footer,
        )
        browser.close()
        return 1 if (status["mermaidErrors"] or broken) else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-pdf", action="store_true")
    args = parser.parse_args()

    md = build_markdown()
    MD_OUT.write_text(md, encoding="utf-8")
    words = len(re.findall(r"\w+", md))
    print(f"Markdown: {MD_OUT.name} ({words:,} palavras, {md.count('```mermaid')} diagramas)")

    HTML_OUT.write_text(build_html(md), encoding="utf-8")
    print(f"HTML: {HTML_OUT.name}")

    if not args.no_pdf:
        code = build_pdf()
        print(f"PDF: {PDF_OUT.name}")
        sys.exit(code)


if __name__ == "__main__":
    main()
