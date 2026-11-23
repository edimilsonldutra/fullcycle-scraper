# Capítulo 9 — Protocolos de Comunicação para Sistemas Agênticos (MCP e A2A)

> **O problema real e o modelo mental:** O gargalo de sistemas agênticos em produção não é escolher o melhor LLM, mas evitar que integrações ponto a ponto entre modelos, ferramentas e agentes colapsem em acoplamento combinatório (N x M entre modelos e ferramentas; N x N entre agentes). A solução separa a comunicação em dois eixos ortogonais sobre JSON-RPC 2.0: **MCP** resolve a integração **vertical** (agente ↔ ferramentas e contexto) e **A2A** resolve a integração **horizontal** (agente ↔ agente autônomo).

---

## 9.1 Do Caos das Integrações ao Wire Format (JSON-RPC 2.0)

Sistemas com IA começam simples: um provedor de LLM e poucas funções locais. O problema explode com decisões rotineiras — testar outro provedor, criar fallback, reduzir latência ou compartilhar ferramentas entre assistentes. A matriz de integrações cresce como **N x M**, agravada pelo não-determinismo comportamental dos LLMs, que decidem em runtime qual ferramenta chamar. Assim como o USB padronizou periféricos e o HTTP padronizou a web, protocolos abertos substituem adaptadores artesanais por contratos verificáveis no fio (*wire format*).

### Por que JSON-RPC 2.0

O *wire format* é a mensagem real que trafega entre processos, independente de linguagem ou SDK. Tanto MCP quanto A2A escolhem **JSON-RPC 2.0** porque REST força modelagem de recursos em fluxos orientados a ação e gRPC adiciona atrito binário para inspeção operacional. JSON-RPC 2.0 é leve, legível em logs e independente de transporte, seguindo quatro regras:

1. **Request**: contém `jsonrpc: "2.0"`, `method`, `params` e `id` único para correlação.
2. **Response**: retorna o mesmo `id` e **exatamente um** campo — `result` ou `error`, nunca ambos.
3. **Notification**: mensagem unidirecional **sem `id`**. A ausência do campo sinaliza que não há resposta esperada (usada em inicialização, progresso e cancelamento).
4. **Erros padronizados**: códigos como `-32602` (*Invalid Params*), `-32601` (*Method Not Found*) e `-32603` (*Internal Error*) evitam interpretação frágil de texto livre.

```json
// Request
{"jsonrpc": "2.0", "id": "req-42", "method": "tools/call", "params": {"name": "consultar_clima", "arguments": {"cidade": "Sao Paulo"}}}
// Notification de progresso (sem campo "id")
{"jsonrpc": "2.0", "method": "notifications/progress", "params": {"progressToken": "tok-9", "progress": 50, "total": 100}}
```

### Tool Calling vs. MCP vs. A2A

Em laboratórios comparativos reais — expondo a mesma consulta a uma API externa via Tool Calling da Anthropic, Tool Calling da OpenAI e um servidor FastMCP — as três opções funcionam no dia um. O custo aparece quando o contrato externo muda ou troca-se o provedor: no *tool calling*, schemas e adaptadores precisam ser reescritos em cada cliente; no MCP, a alteração fica concentrada no servidor.

| Critério | Tool Calling Nativo | MCP (Model Context Protocol) | A2A (Agent-to-Agent) |
| :--- | :--- | :--- | :--- |
| **Problema resolvido** | Invocar função local no fluxo do LLM | Padronizar acesso a ferramentas, dados e prompts | Delegar trabalho a agentes autônomos externos |
| **Eixo arquitetural** | Interno ao processo | Vertical (Agente ↔ Ferramenta/Contexto) | Horizontal (Agente ↔ Agente) |
| **Acoplamento ao vendor** | Alto (schema específico do provedor) | Baixo (contrato único para múltiplos hosts) | Baixo (agentes opacos interoperáveis via contrato público) |
| **Descoberta** | Hardcoded na chamada | Handshake + `list` na sessão | Autônoma via Agent Card (`/.well-known/agent-card.json`) |
| **Ciclo de vida** | Síncrono / efêmero | Sessão com progresso e cancelamento | Task persistente, multi-turno e assíncrona |
| **Quando escolher** | Protótipo simples, 1 processo, 1 vendor | Capacidades compartilhadas entre hosts/modelos | Colaboração entre domínios autônomos e opacos |

---

## 9.2 Arquitetura MCP: Papéis, Ciclo de Vida e Primitivos

Misturar prompt, schema de banco, chamadas HTTP e regras de negócio cria o **espaguete agêntico**: uma coluna renomeada quebra toda a aplicação. O MCP quebra esse acoplamento separando três papéis claros:

- **Host**: aplicação principal (IDE, chat, orquestrador) que detém o LLM, a governança, o filtro de contexto e as permissões.
- **Client**: vive no Host com conexão protocolar 1:1 para cada servidor, gerenciando transporte (**STDIO** local ou **Streamable HTTP** remoto — que substituiu o antigo transporte HTTP+SSE, depreciado na revisão de 2025-03-26 da especificação, embora ainda use SSE internamente para respostas em fluxo), timeouts e contenção de falhas (camada anticorrupção).
- **Server**: serviço de domínio independente que expõe capacidades padronizadas (ex.: PostgreSQL MCP, GitHub MCP) sem conhecer o modelo consumidor.

```mermaid
flowchart LR
    subgraph H["Host (Governanca, LLM e Orquestracao)"]
        LLM["LLM / Orquestrador"]
        C1["MCP Client 1"]
        C2["MCP Client 2"]
        A2AC["A2A Client"]
    end

    subgraph V["Eixo Vertical (MCP)"]
        S1["MCP Server: Postgres"]
        S2["MCP Server: GitHub"]
    end

    subgraph HZ["Eixo Horizontal (A2A)"]
        AG1["Agente: Estoque"]
        AG2["Agente: Logistica"]
    end

    LLM --> C1
    LLM --> C2
    LLM --> A2AC
    C1 -->|"JSON-RPC (STDIO / HTTP)"| S1
    C2 -->|"JSON-RPC (HTTP + Gateway)"| S2
    A2AC -->|"A2A (JSON-RPC + SSE / Webhook)"| AG1
    AG1 -->|"Orquestracao Direta (A2A)"| AG2
```

### Ciclo de vida e os quatro primitivos

A sessão MCP percorre três fases: **Handshake (`initialize`)** com negociação explícita de `capabilities` (evitando chamadas não suportadas), **Fase Operacional** (`tools/call`, `resources/read`, `prompts/get`, progresso e cancelamento) e **Shutdown controlado**. As capacidades se dividem entre o que o **servidor** oferece (três primitivos) e o que o **cliente** oferece ao servidor:

| Primitivo | Lado / Direção | Papel arquitetural | Exemplo prático |
| :--- | :--- | :--- | :--- |
| **Resources** | Servidor · `GET` (URI / URI Template) | Leitura de estado e contexto sem efeito colateral, controlada pela aplicação | `orders://{order_id}` ou view JSON de cancelamentos |
| **Tools** | Servidor · ação invocada pelo modelo | Consultas e mutações de estado com schema de entrada (e opcionalmente de saída) | `make_priority_shift` ou `emitir_reembolso` |
| **Prompts** | Servidor · templates escolhidos pelo usuário | Fluxos e comunicações padronizadas do domínio | Template de e-mail de reembolso conforme política |
| **Sampling** | Cliente · inversão (Server → Host) | Server solicita inferência ao LLM do Host | Classificar se um log externo contém prompt injection |
| **Elicitation** | Cliente · inversão (Server → usuário) | Server pede ao usuário, via Host, um dado estruturado que falta | Confirmar o centro de distribuição antes de reprogramar a entrega |
| **Roots** | Cliente → Server | Informa as fronteiras (diretórios/URIs) em que o servidor deve operar | Restringir um servidor de arquivos ao diretório do projeto |

O **Resource** com URI Template transforma leitura de banco em visão segura e navegável (sem expor SQL arbitrário). Já o **Sampling** não é um "tool call reverso": ele injeta capacidade probabilística dentro de um fluxo determinístico do servidor mantendo chaves, custo e escolha de modelo centralizados no Host. A **Elicitation** cumpre papel semelhante para dados humanos: em vez de o servidor falhar por falta de informação, ele pede o dado ao usuário com um schema simples — e o Host decide como (e se) apresentar o pedido.

Tools também podem declarar **anotações** de comportamento — `readOnlyHint`, `destructiveHint`, `idempotentHint` e `openWorldHint` — que ajudam o Host a decidir quando pedir confirmação humana. Trate-as como **dicas fornecidas pelo servidor, não como garantias de segurança**: um Host só deve confiar nelas quando o servidor for confiável, e a autorização real continua no código da tool.

---

## 9.3 Engenharia de Servidores MCP em Produção

Escolher entre **TypeScript SDK (`McpServer`)** e **Python SDK (`FastMCP`)** é uma decisão de aderência à stack do time, não disputa de linguagens. Ambos compartilham a mesma tríade — **Server, Schema e Transport** — e exigem cinco contratos de produção desde o primeiro pull request:

1. **Validação estática e em runtime**: `tsc --noEmit` + Zod no TypeScript; type hints ricos + retornos estruturados (`dict`/modelos tipados) no Python/FastMCP, abandonando texto solto.
2. **Paginação por cursor opaco (`nextCursor`)**: desacopla o cliente de `OFFSET` e da ordenação interna do banco.
3. **Cancelamento cooperativo (`AbortSignal`)**: handlers demorados observam o sinal de cancelamento, liberam recursos e capturam a exceção na borda (retornando resposta controlada, jamais stack trace bruto).
4. **Idempotência baseada em estado**: tools mutáveis verificam o estado atual antes de agir (ex.: confirmar se o frete prioritário já foi aplicado para evitar duplicação).
5. **Erros no nível certo, Logs RFC e Progress**: a especificação distingue **erros de protocolo** (JSON-RPC — tool inexistente ou argumentos que violam o schema, como `-32602 Invalid Params`) de **erros de execução da tool** (regra de negócio violada, API externa indisponível), que devem voltar como **resultado com `isError: true`** e mensagem acionável. É esse segundo formato que chega ao modelo como conteúdo, permitindo que o agente ajuste a próxima ação em vez de assumir queda do servidor. Logs usam as severidades da RFC 5424 (`debug`, `info`, `notice`, `warning`, `error`, `critical`, `alert`, `emergency`) e tarefas longas reportam avanço via `report_progress`.

```python
from decimal import ROUND_HALF_EVEN, Decimal

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.fastmcp.exceptions import ToolError

mcp = FastMCP("orders-retention-server")
TETO_BONUS = Decimal("0.20")
CENTAVOS = Decimal("0.01")


@mcp.resource("orders://cancellations/summary")
def get_cancellations_summary() -> str:
    """Foto controlada dos cancelamentos (sem acesso SQL arbitrario)."""
    return '{"total_cancelados": 4, "perda_estimada_usd": "1840.00"}'


@mcp.tool()
async def emitir_reembolso_bonificado(
    order_id: str, valor_pedido: Decimal, valor_bonus: Decimal, ctx: Context
) -> dict:
    """Concede bonus de retencao respeitando o teto deterministico de 20% do pedido."""
    await ctx.info(f"Validando politica para pedido {order_id}")
    await ctx.report_progress(progress=40, total=100)

    limite = (valor_pedido * TETO_BONUS).quantize(CENTAVOS, rounding=ROUND_HALF_EVEN)
    if valor_bonus <= 0 or valor_bonus > limite:
        # Erro de execucao: retorna ao modelo como resultado com isError=true
        raise ToolError(
            f"Bonus USD {valor_bonus} fora da politica: deve ser > 0 e <= 20% do pedido (USD {limite})."
        )

    await ctx.report_progress(progress=100, total=100)
    return {"order_id": order_id, "status": "aprovado", "bonus_usd": str(valor_bonus)}
```

A política financeira vira código executável e testável, não promessa frágil no prompt. Se o agente tenta conceder 30%, a tool devolve um erro de execução com o teto calculado e o agente tende a convergir para um valor permitido — mas a **garantia está no bloqueio, não na convergência**. Observe também o uso de `Decimal` com arredondamento explícito: valores monetários em `float` acumulam erros de representação binária (`0.1 + 0.2 != 0.3`) que, em escala, viram divergências de conciliação.

> [!TIP]
> **Não depure protocolo antes de validar infraestrutura e testes unitários.** Como a tool é a parte determinística do agente, ela exige a suíte de testes mais rigorosa. Valide o catálogo exposto (schemas, URI templates e respostas) no **MCP Inspector** — cuja arquitetura separa UI e MCP Proxy autenticado por Bearer Token — antes de plugar um agente completo.

---

## 9.4 Segurança em Camadas, OAuth 2.1 e Borda com Docker MCP Gateway

Em sistemas agênticos conectados a ferramentas, o perímetro de defesa deixa de ser apenas rede (VPC, firewall) e passa a incluir a **semântica da conversa**. Um comando malicioso escondido em um e-mail, issue ou registro de banco pode induzir o modelo a executar ações indevidas (**Prompt Injection indireto**). A regra é direta: **em MCP, texto não é só texto — texto pode virar ação**.

A defesa organiza-se em três camadas independentes:

- **Transporte (Quem entra)**: TLS, origem controlada e autenticação forte por escopo.
- **Runtime (Quanto dano pode causar)**: container enxuto, limites de CPU/memória, allowlist de tools e segregação de credenciais.
- **Conteúdo (O que vira instrução)**: validação estrita de schemas, sanitização e barreiras semânticas (inclusive via *Sampling* em dados externos de alto risco).

### OAuth 2.1 + PKCE e Docker MCP Gateway

API keys estáticas autenticam apenas um segredo compartilhado, impedindo distinguir usuário, host e agente. Com **OAuth 2.1**, cada chamada carrega identidade verificável com token curto e escopo restrito; **PKCE** impede que um `authorization code` interceptado seja trocado por `access token`. O servidor MCP nunca valida senhas — apenas tokens e escopos.

A especificação de autorização do MCP (revisão de 2025-06-18 em diante) formaliza papéis que evitam os erros mais comuns:

- **O servidor MCP é um *Resource Server* OAuth**: ele publica seus metadados de recurso protegido (*Protected Resource Metadata*, RFC 9728), indicando qual *Authorization Server* emite tokens aceitos — a autenticação do usuário acontece nesse servidor de autorização, não no MCP.
- **Tokens com audiência explícita**: o cliente pede tokens para aquele recurso específico (*Resource Indicators*, RFC 8707) e o servidor **rejeita tokens emitidos para outra audiência**.
- **Proibido repassar o token recebido** (*token passthrough*): se o servidor MCP chama uma API a jusante, ele obtém credenciais próprias para isso. Encaminhar o token do usuário transforma o servidor num *confused deputy* e apaga a trilha de auditoria.

Para produção, o servidor sai do processo local para trás de um **Docker MCP Gateway**:

- **Dockerfile multi-stage** + rota **`/healthz`** + limites de CPU/memória garantem contenção e reinício automático de processos travados.
- **Segredos na borda**: credenciais de produção ficam no Gateway, nunca no `env` ou `/proc` do runtime do cliente LLM. O Gateway aplica *allowlist* de tools e *rate limit*, injetando o header `Authorization: Bearer` apenas no tráfego autorizado, validado no backend via `AuthMiddleware`.
- **Isolamento de erro vs. visibilidade interna**: ao ocorrer uma exceção interna, o cliente recebe erro limpo sem detalhes sensíveis, enquanto a stack de observabilidade (**OTel Collector → Prometheus + Tempo → Grafana**) registra o span exato com o *stack trace* para a engenharia.

> [!WARNING]
> **Valide o artefato em execução com caos controlado.** Em deploy, falhas banais — como editar uma pasta de referência em vez do `src/` empacotado — simulam bugs de protocolo. Exercite propositalmente token inválido, burst de rate limit e exceção forçada na tool para confirmar simultaneamente bloqueio na borda e visibilidade completa nos traces.

---

## 9.5 A2A: Descoberta, Ciclo de Vida de Task e Orquestração Horizontal

Quando um agente precisa negociar com outro agente autônomo (ex.: Estoque consultando Logística ou Antifraude), o outro lado é opaco, possui raciocínio próprio e duração imprevisível. O protocolo **A2A** (*Agent2Agent*, criado pelo Google e hoje mantido como projeto aberto sob a Linux Foundation) resolve esse acoplamento **N x N** com dois pilares: **Agent Cards** e **Tasks**. A especificação ainda evolui entre versões; os nomes de campos e métodos abaixo seguem a linha 0.3 — confira a versão suportada pelo SDK que você usar.

### Agent Cards e descoberta autônoma

Seguindo a RFC 8615, todo agente A2A publica seu contrato em `/.well-known/agent-card.json` (versões anteriores da especificação usavam `agent.json`), declarando versão do protocolo, endpoint e transporte preferido, esquemas de segurança (no mesmo formato do OpenAPI), suporte a `streaming`/`pushNotifications`, MIME types (`defaultInputModes`/`defaultOutputModes`) e suas **`skills`** (com `tags` e `examples` que orientam roteamento automático). Um *Extended Agent Card* pode expor skills privadas apenas após autenticação.

```json
{
  "protocolVersion": "0.3.0",
  "name": "Agente de Logistica",
  "description": "Rastreia reposicoes, status alfandegario e previsao de entrega.",
  "version": "1.0.0",
  "url": "https://logistica.interno.empresa.com/a2a",
  "preferredTransport": "JSONRPC",
  "capabilities": {"streaming": true, "pushNotifications": true},
  "securitySchemes": {"bearer": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}},
  "security": [{"bearer": []}],
  "defaultInputModes": ["text/plain", "application/json"],
  "defaultOutputModes": ["text/plain", "application/json"],
  "skills": [{
    "id": "rastrear_reposicao",
    "name": "Rastrear Reposicao e Rotas",
    "description": "Consulta status alfandegario e previsao de entrega por fornecedor.",
    "tags": ["logistica", "rastreamento"],
    "examples": ["Verifique a reposicao da LG", "Rastreie o pedido 123"]
  }]
}
```

### Ciclo de vida da Task, `message` vs. `artifact` e Multi-turno

No A2A, uma solicitação cria uma **Task** persistente que transita por estados formais (`submitted` → `working` → `input-required` ou `auth-required` ↔ `working` → estados terminais imutáveis: `completed`, `failed`, `canceled` ou `rejected`). Três regras garantem interoperabilidade sem bugs:

1. **Separe `message` de `artifact`**: `message` sustenta o diálogo operacional; `artifact` entrega o resultado formal estruturado para sistemas consumidores.
2. **Use `input-required` para falta de contexto, não erro de schema**: erro de contrato falha a requisição; campo faltante, ambiguidade ou confirmação de ação destrutiva pausam a Task em `input-required`, acumulando histórico até o `artifact` final.
3. **Prefira SSE e Webhooks a polling agressivo**: o método `message/stream` entrega eventos progressivos via SSE (`TaskStatusUpdateEvent` e `TaskArtifactUpdateEvent`, com chunks do artefato), enquanto *push notifications* por Webhook avisam mudanças de estado em tarefas longas, mesmo com o cliente desconectado. Valide a autenticidade de cada webhook recebido (ele é uma entrada externa como qualquer outra) e, em produção, substitua *in-memory task stores* por persistência externa.

```mermaid
sequenceDiagram
    participant C as "Agente Cliente (Estoque)"
    participant S as "Agente Servidor (Logistica)"
    participant W as "Webhook Receiver"

    C->>S: GET /.well-known/agent-card.json
    S-->>C: Agent Card (skills, streaming, pushNotifications)
    C->>S: message/stream (Verificar reposicao LG)
    S-->>C: TaskStatusUpdate (submitted -> working)
    S-->>C: TaskStatusUpdate (input-required: Qual CD?)
    S-)W: Push Notification (input-required)
    C->>S: message/stream (Mesmo taskId: CD Sao Paulo)
    S-->>C: TaskArtifactUpdate (chunks do relatorio final)
    S-->>C: TaskStatusUpdate (completed)
    S-)W: Push Notification (completed + artifact)
```

### Orquestração direta e Domínios

Na **orquestração direta**, papéis de cliente e servidor são dinâmicos: na topologia **GenUI → Estoque → Logística**, a interface conversa apenas com o Estoque, que atua como **cliente A2A** da Logística e devolve a resposta consolidada. Para o GenUI, a Logística nem existe — encapsulando fronteiras de domínio. Em escala corporativa, agrupar Agent Cards em **Domínios** cria um ponto único de descoberta e governança.

---

## 9.6 Arquiteturas Multiagente: MCP + A2A + LangGraph + OTel

Em sistemas corporativos completos, MCP e A2A compõem padrões de coordenação explícitos: **Delegação direta**, **Hierárquico/Coordenador** (que reconcilia conflitos entre especialistas, como jurídico vs. financeiro em *due diligence*), **Pipeline** sequencial e **Fan-out/Fan-in paralelo** (cuja latência é limitada pela chamada mais lenta, não pela soma delas).

No padrão de um *Resolution Center* (atendimento a pedidos atrasados), o **LangGraph** atua como **maestro local**: define `State`, `Nodes` e `Edges`, materializados com `compile()` e executados via `invoke()` com checkpoints persistidos (`SqliteSaver` em dev; `PostgresSaver` ou outro *checkpointer* transacional em produção) indexados por `thread_id`. O grafo não contém regra de domínio: ele chama dados legados via **MCP** (`ler_pedido_financeiro`), dispara agentes **A2A** em paralelo (Estoque e Logística) e consolida evidências e lacunas em um nó final de `critique`.

Para eliminar a opacidade desse grafo distribuído, o **OpenTelemetry (OTel)** — visualizado em **Arize Phoenix** ou Grafana Tempo — costura todos os processos em uma única cascata de spans: o emissor injeta o contexto W3C Trace Context (headers `traceparent`/`tracestate`) com `opentelemetry.propagate.inject(headers)` e o receptor o recupera com `extract(headers)` antes de abrir seus spans — ou usa a instrumentação automática do cliente/servidor HTTP, que já faz essa propagação. Isso revela instantaneamente causalidade, paralelismo real e gargalos entre grafo, MCP e A2A.

> [!IMPORTANT]
> **Separe coordenação de execução e mantenha testes como documentação viva.** Quando o grafo gerencia apenas transições e cada tool MCP ou agente A2A possui suíte de testes cobrindo payloads e contratos, engenheiros e assistentes de IA evoluem o ecossistema com previsibilidade sem quebrar o fluxo ponta a ponta.

---

## 9.7 Checklist de Aplicação Prática

- [ ] **Escolha a camada certa pelo eixo do problema**: Tool Calling para protótipos locais; **MCP** para acesso vertical a ferramentas/dados compartilhados; **A2A** para delegação horizontal entre agentes autônomos e opacos.
- [ ] **Modele capacidades MCP com semântica estrita**: use **Resources** com URI Templates para leitura segura (sem SQL aberto), **Tools** idempotentes e anotadas para ações, erros de execução (`isError: true`) com mensagem acionável para políticas de negócio (reservando `-32602` para argumentos fora do schema) e `Decimal` para valores monetários.
- [ ] **Garanta contratos operacionais desde o primeiro PR**: valide schemas em runtime, suporte `AbortSignal` com captura de exceção na borda, use cursor opaco (`nextCursor`), logs RFC e `report_progress`.
- [ ] **Blinde a produção em três camadas**: adote **OAuth 2.1 + PKCE** com o servidor MCP como *Resource Server* (validação de audiência, sem *token passthrough*), use **Streamable HTTP** para servidores remotos, empacote servidores em Dockerfile multi-stage com `/healthz` e isole segredos, allowlist e rate limit no **MCP Gateway**.
- [ ] **Implemente A2A aderente ao ciclo de vida**: publique `/.well-known/agent-card.json` com `securitySchemes`, persista Tasks fora da memória, separe `message` de `artifact`, use `input-required` para falta de contexto e prefira SSE/Webhooks a polling.
- [ ] **Desacople orquestração de domínio**: coordene fan-out paralelo, checkpoints (`thread_id`) e reconciliação (`critique`) em um grafo explícito (LangGraph), delegando execução a servidores MCP e agentes A2A.
- [ ] **Correlacione traces entre processos com OTel**: propague o W3C Trace Context (`propagate.inject` / `propagate.extract`) em todas as chamadas remotas e valide a cascata de spans antes de ir para produção.
