import os
import re
import sys
import time
from pathlib import Path

from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

GEMINI_PROMPT = """\
Você é um assistante especializado em cursos técnicos de desenvolvimento de software e arquitetura.

Com base no resumo e transcrição da aula abaixo, gere em português:

**Abreviações**
Lista de siglas e abreviações mencionadas na aula com sua definição por extenso. Se não houver nenhuma, omita essa seção.

**Resumo**
Texto corrido cobrindo o objetivo da aula, os conceitos e ferramentas abordados e o fluxo explicado pelo instrutor.

**Pontos de atenção**
Lista dos pontos críticos, armadilhas e boas práticas destacados na aula.

Retorne apenas essas seções, sem introdução nem conclusão.

Aula:
```
[CONTENT_FROM_CLASS]
```\
"""



def info(msg: str) -> None:
    print(f"  [+] {msg}")


def warn(msg: str) -> None:
    print(f"  [!] {msg}")


def extract_section(content: str, label: str) -> str:
    pattern = re.compile(
        rf"{re.escape(label)}\s*\n\n(.*?)(?=\n\n##|\Z)",
        re.DOTALL,
    )
    m = pattern.search(content)
    return m.group(1).strip() if m else ""


def parse_file(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")

    def meta(key: str) -> str:
        m = re.search(rf"^{key}: (.+)$", content, re.MULTILINE)
        return m.group(1).strip() if m else ""

    aula_raw = meta("Aula")
    aula_match = re.match(r"\[(.+?)\]", aula_raw)
    aula = aula_match.group(1) if aula_match else aula_raw

    return {
        "content": content,
        "modulo": meta("Módulo"),
        "aula": aula,
        "resumo": extract_section(content, "## Resumo da aula"),
        "transcricao": extract_section(content, "## Transcrição"),
    }


def call_gemini(resumo: str, transcricao: str) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY não definida no .env")

    client = genai.Client(api_key=GEMINI_API_KEY)

    content = f"RESUMO DA AULA:\n{resumo}\n\nTRANSCRIÇÃO:\n{transcricao}"
    prompt = GEMINI_PROMPT.replace("[CONTENT_FROM_CLASS]", content)
    
    max_retries = 5
    for attempt in range(1, max_retries + 1):
        try:
            info(f"Chamando Gemini ({GEMINI_MODEL})...")
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )
            # Sleep a bit to avoid hitting rate limits on the next call (Gemini free tier has 15 RPM limit)
            time.sleep(4.5)
            return response.text.strip()
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                wait_time = 35.0
                match = re.search(r"retry in (\d+\.?\d*)s", err_str)
                if match:
                    wait_time = float(match.group(1)) + 2.0  # add a small buffer
                warn(f"Cota excedida (429). Aguardando {wait_time:.1f}s antes da tentativa {attempt}/{max_retries}...")
                time.sleep(wait_time)
            else:
                raise e
    raise RuntimeError("Número máximo de tentativas excedido devido a erros de cota.")


def update_file(path: Path, content: str, resumo_ia: str) -> str:
    updated = content.replace("[RESUMO_IA]", resumo_ia)
    path.write_text(updated, encoding="utf-8")
    return updated


def process_file(path: Path) -> None:
    print(f"\n>>> {path}")

    info("Lendo arquivo...")
    data = parse_file(path)

    has_resumo = bool(data["resumo"])
    has_transcricao = bool(data["transcricao"]) and data["transcricao"].strip() != "[TRANSCRIÇÃO]"

    if not has_resumo and not has_transcricao:
        warn("Nem resumo nem transcrição encontrados — pulando.")
        return

    if "[RESUMO_IA]" not in data["content"]:
        info("RESUMO IA já preenchido — pulando chamada Gemini.")
        final_content = data["content"]
    else:
        try:
            resumo_ia = call_gemini(
                data["resumo"] if has_resumo else "(Não disponível na plataforma)",
                data["transcricao"] if has_transcricao else "(Não disponível na plataforma)",
            )
            info(f"Resumo IA gerado ({len(resumo_ia)} chars)")
        except Exception as e:
            warn(f"Erro Gemini: {e}")
            return

        info("Atualizando arquivo com RESUMO IA...")
        final_content = update_file(path, data["content"], resumo_ia)
        info(f"Salvo: {path}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Uso: python3 process_lesson.py <caminho/para/aula.md|pasta>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Caminho não encontrado: {path}")
        sys.exit(1)

    if path.is_dir():
        files = sorted(path.rglob("*.md"))
        if not files:
            print(f"Nenhum arquivo .md encontrado em: {path}")
            sys.exit(1)
        print(f"Encontrados {len(files)} arquivo(s) em '{path}'")
        for file in files:
            process_file(file)
    else:
        process_file(path)

    print("\n>>> Concluído!")


if __name__ == "__main__":
    main()
