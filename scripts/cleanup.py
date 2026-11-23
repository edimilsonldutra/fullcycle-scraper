import re
import sys
from pathlib import Path

OUTPUT_DIR = Path("output")

EMPTY_RESUMO = re.compile(r'Resumo da aula:\s*\n\n\s*\n={40,}', re.MULTILINE)
EMPTY_TRANSCRICAO = re.compile(r'Transcrição:\s*\n\n\[TRANSCRIÇÃO\]', re.MULTILINE)
BLANK_TRANSCRICAO = re.compile(r'Transcrição:\s*\n\n={40,}', re.MULTILINE)


def check(content: str) -> list[str]:
    reasons = []
    if EMPTY_RESUMO.search(content):
        reasons.append("resumo vazio")
    if EMPTY_TRANSCRICAO.search(content) or BLANK_TRANSCRICAO.search(content):
        reasons.append("transcrição ausente")
    return reasons


def main():
    if not OUTPUT_DIR.exists():
        print("Pasta output/ não encontrada.")
        sys.exit(1)

    deleted: list[tuple[Path, list[str]]] = []

    for f in sorted(OUTPUT_DIR.rglob("*.md")):
        if f.name == "errors.log":
            continue
        content = f.read_text(encoding="utf-8")
        reasons = check(content)
        if reasons:
            rel = f.relative_to(OUTPUT_DIR)
            deleted.append((rel, reasons))
            f.unlink()

    if not deleted:
        print("Nenhum arquivo com problema encontrado.")
        return

    print(f"{'Arquivo':<70} {'Motivo'}")
    print("-" * 90)
    for path, reasons in deleted:
        print(f"{str(path):<70} {', '.join(reasons)}")
    print("-" * 90)
    print(f"Total removido: {len(deleted)}")


if __name__ == "__main__":
    main()
