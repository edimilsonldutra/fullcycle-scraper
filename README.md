# fullcycle-scraper

Scraper de aulas da plataforma FullCycle. Extrai resumo e transcrição de cada aula, salva em `.md` e gera um resumo via Gemini.

## Estrutura

```
scraper.py          # extrai as aulas via Playwright
process_lesson.py   # processa os .md com Gemini
scripts/
  cleanup.py        # remove arquivos sem transcrição
  extract_page.js   # script JS de extração do browser
prompts/
  notebooklm.md     # prompt para uso no NotebookLM GUI
output/             # aulas salvas por curso/módulo/aula
```

## Configuração

Copie `.env.example` para `.env` e preencha:

```env
GEMINI_API_KEY=AIzaSy...
GEMINI_MODEL=gemini-2.5-flash     # opcional, padrão: gemini-2.5-flash
FULLCYCLE_EMAIL=seu@email.com
FULLCYCLE_PASSWORD=suasenha
FULLCYCLE_URL=https://plataforma.fullcycle.com.br/...  # deve ser o link de um vídeo do curso, não a página inicial
```

Instale as dependências:

```bash
pip install -r requirements.txt
playwright install chromium
```

## Uso

### 1. Extrair aulas

```bash
python scraper.py
```

Abre o Chrome com o perfil `~/.fullcycle-scraper-profile`, faz login automaticamente (se `FULLCYCLE_EMAIL` e `FULLCYCLE_PASSWORD` estiverem preenchidos) e percorre todas as aulas do curso definido em `FULLCYCLE_URL`.

As aulas são salvas em `output/<curso>/<módulo>/<aula>.md`. Aulas já existentes são puladas.

### 2. Processar com Gemini

Por aula:
```bash
python process_lesson.py "output/Prompt Engineering/05 - Gestão e versionamento de prompt/14 - Criando prompt via interface.md"
```

Por módulo:
```bash
python process_lesson.py "output/Prompt Engineering/05 - Gestão e versionamento de prompt"
```

Por curso inteiro:
```bash
python process_lesson.py "output/Prompt Engineering"
```

Gera três seções no arquivo: **Abreviações**, **Resumo** e **Pontos de atenção**. Aulas já processadas são puladas.

### 3. Gerar infográfico com NotebookLM

1. Abra o [NotebookLM](https://notebooklm.google.com) e crie um novo notebook
2. Adicione o conteúdo do `.md` da aula como fonte
3. Use o prompt em `prompts/notebooklm.md` para gerar o infográfico
4. Salve a imagem gerada como `.png` **na mesma pasta do `.md`**, com o mesmo nome:

```
output/Prompt Engineering/05 - Gestão e versionamento de prompt/
  14 - Criando prompt via interface.md
  14 - Criando prompt via interface.png   ← aqui
```

Para contribuir com infográficos, faça um fork do repositório, adicione os `.png` e abra um Pull Request.

### 4. Limpar arquivos incompletos

```bash
python scripts/cleanup.py
```

Remove arquivos sem transcrição ou com resumo vazio.
