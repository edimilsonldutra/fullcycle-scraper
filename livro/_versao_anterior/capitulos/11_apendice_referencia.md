# Apêndice — Guia Rápido de Referência

Este apêndice consolida, em formato de consulta imediata, a **matriz de decisão técnica**, o **glossário essencial** e os **checklists de produção** cobrindo todo o livro.

---

## A.1 Matriz de Decisão — Qual Técnica ou Ferramenta Usar?

| Problema de Engenharia | Primeira Escolha | Quando Escalar para o Próximo Nível |
| --- | --- | --- |
| **Respostas inconsistentes ou genéricas do LLM** | Prompt estruturado (papel, objetivo, restrições, formato de saída, Few-Shot) | Versionamento + avaliação sistemática (Langfuse) ou otimização programática (DSPy) |
| **Modelo não conhece dados internos ou recentes** | **RAG** (busca híbrida BM25 + vetorial + reranking + citations) | Fine-tuning apenas se o problema for estilo/formato rígido ou domínio muito específico, nunca para "memorizar fatos mutáveis" |
| **Custo ou latência alta em chamadas LLM** | Roteamento por complexidade (AI Gateway) + Prompt Caching + Cache Exato/Semântico | Streaming, chamadas paralelas, modelos menores/destilados em tarefas de classificação/extração |
| **IA gerando código fora do padrão do time** | Design Docs vivos (PRD/TRD/ADR) + `CLAUDE.md`/Rules + workflow **RPI** | **SDD** (Spec-Driven Development) + **Harness Engineering** (lint, typecheck, testes automáticos como gate) |
| **Instruções repetitivas poluindo o contexto do agente** | **Agent Skills** (`SKILL.md` com frontmatter enxuto e *progressive disclosure*) | Scripts determinísticos dentro da Skill + Subagents isolados + testes de trigger com Promptfoo |
| **Conectar agente a APIs, bancos ou ferramentas externas** | **MCP** (Model Context Protocol) com escopo mínimo e autenticação isolada | **A2A** (Agent-to-Agent) quando precisar delegar tarefas entre agentes independentes com Agent Cards |
| **Orquestrar tarefas com múltiplos passos previsíveis** | **Workflows determinísticos** (Sequential, Parallel, Loop) com LLMs em nós específicos | Agente autônomo/multi-agente apenas onde o caminho realmente depende de decisão dinâmica em tempo de execução |
| **Medo de regressão ao alterar prompts, modelos ou RAG** | Dataset versionado + **Evaluations** automatizadas (LLM-as-a-Judge + métricas determinísticas) | Quality Gates obrigatórios no CI/CD bloqueando merge quando métricas caem abaixo do baseline |
| **Risco de Prompt Injection, vazamento ou ações destrutivas** | Trust Boundaries explícitas + validação de entrada/saída + *Human-in-the-Loop* (aprovação em tools críticas) | Provenance de documentos no RAG + baseline reproduzível de ataques (OWASP LLM Top 10) no CI |
| **Incidentes recorrentes e operação sobrecarregada** | Observabilidade correlacionada (logs, métricas, traces + traces de LLM) + Runbooks vivos | Agente SRE operacional em modo **somente leitura / recomendação** primeiro; remediação automatizada apenas com guardrails e rollback seguro |

---

## A.2 Glossário Técnico Essencial

- **A2A (Agent-to-Agent Protocol):** Protocolo aberto (Google) para descoberta (via *Agent Card*), delegação de tarefas assíncronas e comunicação padronizada entre agentes autônomos independentes.
- **ADK (Agent Development Kit):** Framework de desenvolvimento de agentes estruturado em torno de agentes, tools, subagents, sessions, runners e workflows.
- **ADR (Architecture Decision Record):** Documento curto e imutável que registra o contexto, a decisão arquitetural tomada, as alternativas consideradas e suas consequências.
- **AI Gateway:** Camada intermediária entre aplicações e provedores de LLM para roteamento, fallback, rate limiting, controle de custos, cache, observabilidade e políticas de segurança.
- **Cache Semântico:** Cache baseado em similaridade vetorial (embeddings) entre consultas, reutilizando respostas para perguntas diferentes com o mesmo significado (exige threshold rigoroso para evitar falsos positivos).
- **Context Engineering:** Disciplina de projetar, filtrar, estruturar e priorizar o que entra na janela de contexto de um modelo para maximizar precisão e reduzir ruído (*context rot*).
- **CoT (Chain-of-Thought):** Técnica que induz o modelo a explicitar etapas intermediárias de raciocínio antes da resposta final.
- **DSPy:** Framework declarativo que trata prompts como programas otimizáveis a partir de métricas e exemplos, em vez de engenharia manual de strings.
- **Embedding:** Representação numérica vetorial de texto (ou outro dado) que captura significado semântico, permitindo busca por similaridade.
- **Evaluation (Eval):** Processo automatizado de medir qualidade, precisão, fidelidade, seleção de tools e segurança de sistemas com IA contra datasets de referência.
- **Harness Engineering:** Construção da infraestrutura determinística em volta do agente (linters, testes, compiladores, sandboxes, verificadores) que transforma geração probabilística em entrega confiável.
- **HITL (Human-in-the-Loop):** Ponto de controle explícito onde uma ação crítica (escrita em produção, deploy, deleção, aprovação de tool) exige confirmação humana.
- **MCP (Model Context Protocol):** Protocolo padrão aberto que desacopla modelos/clientes de ferramentas, recursos e prompts externos via servidores MCP padronizados.
- **OWASP Top 10 for LLM:** Catálogo de referência dos principais riscos de segurança em aplicações com LLMs (Prompt Injection, Sensitive Information Disclosure, Supply Chain, Excessive Agency, etc.).
- **PRD / TRD:** *Product Requirements Document* (o quê e por quê do ponto de vista de negócio/usuário) e *Technical Requirements Document* (como será construído tecnicamente).
- **Progressive Disclosure:** Princípio de carregar apenas metadados mínimos inicialmente (ex.: frontmatter de uma Skill) e puxar instruções/arquivos completos sob demanda para economizar contexto.
- **RAG (Retrieval-Augmented Generation):** Padrão que recupera trechos relevantes de uma base externa em tempo de consulta e os injeta no contexto do LLM para fundamentar a resposta.
- **ReAct (Reason + Act):** Padrão iterativo no qual o modelo alterna raciocínio (*Thought*), execução de ferramenta (*Action*) e leitura do retorno (*Observation*).
- **RPI (Research, Plan, Implement):** Workflow disciplinado de desenvolvimento com IA que separa pesquisa do código existente, planejamento revisável e execução controlada.
- **SDD (Spec-Driven Development):** Desenvolvimento guiado por especificações estruturadas e verificáveis escritas antes da geração de código por agentes.
- **Skill (Agent Skill):** Pacote modular reutilizável (`SKILL.md` + scripts/referências) que ensina a um agente um procedimento especializado e acionável sob demanda.
- **Trust Boundary:** Fronteira arquitetural entre dados confiáveis (instruções do sistema) e dados não confiáveis (entrada do usuário, retorno de APIs, documentos recuperados no RAG).

---

## A.3 Checklist Mestre de Produção (Go-Live com IA)

Antes de colocar qualquer sistema baseado em IA ou agentes em produção, valide estes 10 pontos:

- [ ] **Desacoplamento de provedor:** Todas as chamadas passam por abstração ou AI Gateway com timeout, retry com backoff e fallback configurados.
- [ ] **Orçamento e limites:** Há teto de tokens, limite de iterações em loops agênticos e alertas de custo por ambiente/feature.
- [ ] **Prompts versionados:** Nenhum prompt crítico está hardcoded sem versão, dono e histórico de alterações.
- [ ] **Dataset de Evaluation no CI:** Existe uma suíte mínima de casos reais (incluindo regressões conhecidas) rodando automaticamente antes do deploy.
- [ ] **RAG auditável (se aplicável):** Chunks têm metadados de origem (*provenance*), busca combina léxico + semântico quando necessário e respostas citam fontes.
- [ ] **Observabilidade ponta a ponta:** Cada requisição gera trace com latência, tokens, custo, versão de prompt, tool calls e erro/fallback.
- [ ] **Princípio do menor privilégio:** Tools e servidores MCP têm permissões mínimas; ações destrutivas exigem aprovação humana (HITL) ou sandbox isolado.
- [ ] **Proteção contra Prompt Injection:** Dados externos (usuário, web, RAG) nunca são misturados sem delimitação clara com instruções de sistema; saídas passam por validação determinística (schema/regras).
- [ ] **Qualidade determinística no código gerado por IA:** Todo código assistido por agentes passa pelos mesmos gates de lint, tipagem, testes automatizados e revisão humana consciente.
- [ ] **Runbook e plano de degradação:** O time sabe exatamente como desativar a feature de IA (feature flag), fazer rollback de prompt/modelo e operar em modo degradado se o provedor cair.

