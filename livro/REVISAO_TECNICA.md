# Revisão Técnica — Engenharia de Software na Era da IA

Revisão feita em 23/11/2026 sobre a edição compilada a partir do MBA. A versão anterior completa (capítulos, MD, HTML e PDF) está em [`_versao_anterior/`](_versao_anterior/).

**Critério:** preservar a estrutura, a didática e o conteúdo do curso; corrigir o que estava errado ou desatualizado; acrescentar apenas o que faltava para o leitor tomar decisões corretas em produção. Nenhuma seção foi removida.

**Resultado:** 102 → 116 páginas, ~28,1 mil → ~33,5 mil palavras, 29 → 34 tabelas, 20 diagramas (todos renderizando).

---

## 1. Defeitos estruturais corrigidos

| Problema | Impacto | Correção |
| --- | --- | --- |
| O sumário incluía comentários e títulos de **dentro de blocos de código** (`# .env.local`, `# CLAUDE.md`, `# docker-compose.yml`, `# FDD-04`, `# ADR-014`...) | 13 entradas falsas no sumário | `build_livro.py` gera o sumário ignorando blocos de código |
| Links do sumário usavam slugs com acento (`#capítulo-1-...`), mas o HTML criava os IDs **removendo** acentos (`captulo-1-...`) | Sumário do PDF sem navegação funcional | Slug Unicode idêntico no Python e no JavaScript; o build verifica links quebrados (0 restantes) |
| Cap. 5 dizia que SDD é "aprofundado no Capítulo 7" | Referência cruzada errada | Corrigido para Capítulo 4 |
| Abertura "O problema real e o modelo mental" em 3 formatos diferentes (parágrafo, citação, título H2 nos caps. 9 e 10) | Inconsistência visual e entradas extras no sumário | Padronizada como citação em todos os capítulos |
| Não havia como recompilar o livro | Edições futuras manuais e propensas a erro | `build_livro.py` (MD + HTML + PDF com rodapé e verificação) |

## 2. Correções técnicas (conteúdo errado ou desatualizado)

| Cap. | Antes | Depois |
| --- | --- | --- |
| 1 | Bloco Transformer descrito só como em 2017 (ReLU, encoding senoidal) | Tabela do que mudou: RoPE, RMSNorm/pre-norm, SwiGLU, GQA/FlashAttention, MoE |
| 1 | "Inspecione no *OpenAI Tokenizer*" (vale só para modelos OpenAI) | Cada família tem tokenizador próprio; meça com a ferramenta do provedor usado |
| 1 | Temperatura "0.0 a 1.0+" | Faixa por provedor (Anthropic 0–1; OpenAI/Gemini 0–2) |
| 1 | Código com `temperature` **e** `top_p` juntos, contradizendo o próprio aviso; comentário dizia que `max_tokens` "evita truncamento" | Ajusta só a temperatura; `max_tokens` como teto; checagem de `finish_reason`/`stop_reason` |
| 1 | Temperatura 0 implicitamente tratada como determinística | Aviso explícito: temperatura 0 **não** garante saída idêntica |
| 2 | Prompt caching descrito como "via ID e TTL" (só vale para o cache explícito do Gemini) | Tabela por provedor (automático na OpenAI, `cache_control` na Anthropic, implícito/explícito no Gemini) e ordem ideal do prompt |
| 5 | `ln -s CLAUDE.md AGENTS.md` sem ressalva | Ressalva para Windows e alternativa portátil com `@AGENTS.md` |
| 6 | `allowed-tools` descrito como "lista branca (menor privilégio)" | Na prática **pré-aprova** ferramentas; o bloqueio real vem do token com escopo mínimo e de regras `deny` |
| 7 | Chave de cache **sem tenant** | Chave inclui tenant/escopo de acesso e versão do modelo (evita vazamento de dados entre clientes) |
| 7 | Span OTel com `tenant.tier` fixo em `"enterprise"` e atributos próprios | Convenções semânticas `gen_ai.*` do OpenTelemetry + prefixo `app.*` para negócio |
| 8 | Endpoint FastAPI recebia `user_id` como parâmetro livre e não criava a sessão | `user_id` vem do token autenticado (evita IDOR), sessão buscada/criada explicitamente, teto `max_llm_calls` |
| 9 | Transporte "Streamable HTTP / SSE" | HTTP+SSE foi depreciado (spec 2025-03-26); Streamable HTTP é o transporte remoto |
| 9 | "Quatro primitivos" incluindo Sampling | Três primitivos do servidor + recursos do cliente (Sampling, **Elicitation**, Roots) e anotações de tools |
| 9 | Regra de negócio violada devolvida como erro JSON-RPC `-32602` | Erro de execução volta como resultado `isError: true` (é o que o modelo consegue ler); `-32602` fica para argumentos inválidos |
| 9 | Valores monetários em `float` | `Decimal` com arredondamento explícito |
| 9 | OAuth 2.1 sem papéis definidos | Servidor MCP como *Resource Server* (RFC 9728), audiência (RFC 8707), proibição de *token passthrough* |
| 9 | A2A: `/.well-known/agent.json`, campo `authentication`, método `sendStreamingMessage`, estados incompletos, "Google A2A" | `agent-card.json`, `securitySchemes`/`security`, `message/stream`, estados `auth-required`/`rejected`, projeto na Linux Foundation |
| 9 | `SQLiteSaver`; `inject_headers`/`extract_request` (APIs inexistentes) | `SqliteSaver`/`PostgresSaver`; `opentelemetry.propagate.inject/extract` (W3C Trace Context) |
| 10 | CPU < 80% apresentado como SLI/SLO | SLIs do ponto de vista do usuário; CPU vira sinal de saturação |
| 4 | Atribuição do SDD genérica ("ecossistema Martin Fowler") | Taxonomia de Birgitta Böckeler (spec-first / spec-anchored / spec-as-source) com Spec Kit, Kiro e Tessl |

## 3. Conteúdo acrescentado

- **Prefácio:** nota sobre volatilidade de versões, nomes de modelos e APIs.
- **Cap. 1:** inferência em duas fases (*prefill*/*decode*), KV cache, TTFT; DPO, RLAIF e treino de modelos de raciocínio; restrições de parâmetros em modelos de raciocínio; *lost in the middle* / *context rot*.
- **Cap. 2:** seção **Saída Estruturada** (3 níveis de garantia + validação com Pydantic); vieses do LLM-as-judge (posição, verbosidade, autopreferência) e rigor estatístico em evals.
- **Cap. 3:** validação automática de frontmatter e links de documentos no CI; distinção entre guia sob demanda e contexto sempre carregado.
- **Cap. 4:** `runGate.mjs` reescrito (fail-fast, código de saída, linha final estável para o agente); mitigação de *context anxiety* com reinício limpo de contexto.
- **Cap. 5:** seção **Travas Determinísticas** com `settings.json` (`deny` + hook `PreToolUse`) e *branch protection* como última barreira.
- **Cap. 6:** fixar imagem do MCP por digest; evals com ferramentas só em ambiente descartável; Skills de terceiros tratadas como dependência executável.
- **Cap. 7:** tabela **OWASP LLM Top 10 (2025) × Trust Boundaries**; **tríade letal** e padrão de LLM duplo; recall com filtros em HNSW/pgvector; *contextual retrieval*; métricas de retrieval (Recall@k, MRR, nDCG).
- **Cap. 8:** fixar versão do ADK no `CLAUDE.md` e testes de fumaça contra a versão instalada.
- **Cap. 10:** **alertas por burn rate multi-janela** com regra Prometheus e `promtool`; Secrets do Kubernetes não são criptografados; OIDC e GitOps por *pull*; assinatura de artefatos (Sigstore/cosign); **prompt injection contra o Security Agent** com caso adversarial no Promptfoo.
- **Apêndice:** 8 termos novos no glossário; checklist de go-live de 10 → 12 pontos (isolamento multi-tenant e saídas estruturadas validadas).

## 4. O que não foi alterado (e por quê)

- **APIs específicas do ADK 2.x** (modos `chat`/`single_turn`/`task`, workflows em grafo, `RequestInput`): vêm do material do curso e evoluem rápido; em vez de reescrevê-las sem poder validar contra a versão usada nas aulas, foi acrescentada a orientação de fixar a versão e validar cada exemplo.
- **Nomes de modelos nos exemplos de configuração** (LiteLLM, Promptfoo, ADK): mantidos como exemplos datados; o prefácio agora explica isso.
- **Diagramas Mermaid:** todos mantidos; os rótulos sem acento são intencionais para compatibilidade de renderização.
