# Capítulo 1 — Fundamentos de IA Generativa

> **O problema real e o modelo mental:** a maioria das falhas em projetos de IA em produção nasce de tratar Modelos de Linguagem (LLMs) como oráculos determinísticos. Um LLM é um motor probabilístico de predição de tokens baseado na arquitetura Transformer: ele não consulta fatos verificados nem executa lógica formal nativa — ele amostra continuações estatisticamente coerentes a partir de vetores e contexto. Dominar esse mecanismo permite decidir arquitetura, custo, latência e mitigação de risco com critério técnico, acima do hype.

---

## 1.1 IA Tradicional vs. IA Generativa e a Evolução até os Transformers

A mudança entre IA tradicional e IA Generativa (Gen AI) altera diretamente o contrato de engenharia de software:

- **IA Tradicional (preditiva/supervisionada):** aprende um mapeamento de entradas conhecidas para saídas delimitadas (fraude/não fraude, preço, categoria). Funciona como um aluno em prova de múltipla escolha.
- **IA Generativa:** aprende **distribuições de probabilidade** sobre grandes volumes de dados para gerar saídas inéditas — texto, código, imagem, áudio e vídeo.

Essa capacidade resultou da superação progressiva de dois gargalos históricos: **representação semântica** e **dependência de longo prazo em sequências**.

| Era / Arquitetura | Mecanismo Central | Ganho Principal | Limitação Estrutural |
| :--- | :--- | :--- | :--- |
| **Baseada em Regras (anos 1960)** | Lógica `se... então` e árvores de decisão manuais | Previsibilidade total em domínios fechados | Frágil fora do previsto; não escala por exigir codificação manual |
| **N-gramas (ex.: Bigramas)** | Probabilidade da próxima palavra condicionada às `N-1` anteriores | Captura colocações locais ("bom dia", "gato preto") | Coerência local sem coerência global; entra em loops e perde o tópico |
| **Cadeias de Markov / HMMs** | Estados ocultos + probabilidades de transição/emissão (POS tagging, DNA) | Modela sequências curtas com estrutura latente | Depende só do estado anterior; rotulagem cara; falha em texto longo |
| **Feedforward + Embeddings** | Vetores densos (ex.: GloVe) em fluxo unidirecional | Captura similaridade semântica em espaço contínuo | Janela fixa; perde conexões entre parágrafos distantes |
| **RNNs, LSTM e GRU** | Estado recorrente token a token com portas de memória | Processa sequências variáveis e mitiga esquecimento imediato | Execução sequencial impede paralelização; sofre com *vanishing/exploding gradient* |
| **Transformers (2017+)** | *Self-attention* global + *positional encoding* em paralelo | Relaciona todos os tokens simultaneamente em GPUs/TPUs | Custo computacional e de memória cresce com o contexto |

> [!IMPORTANT]
> **Regra de Ouro:** coerência local não implica coerência global nem compreensão real. Um modelo pode gerar frases impecáveis enquanto viola uma restrição definida três parágrafos antes.

No domínio visual, a geração evoluiu por trilhas complementares aos LLMs:
- **GANs (*Generative Adversarial Networks*):** colocam um **gerador** e um **discriminador** em competição para elevar o realismo visual, com o trade-off de treinamento sensível.
- **VAEs (*Variational Autoencoders*):** usam *encoder-decoder* probabilístico sobre um **espaço latente** controlável, permitindo direcionar atributos específicos da saída (como expressão ou estilo).

---

## 1.2 Por Dentro dos LLMs e da Arquitetura Transformer

Quatro engrenagens sustentam qualquer aplicação com LLMs em produção: **tokenização**, **embeddings**, **atenção** e **arquitetura do bloco Transformer**.

### Tokens e Tokenização (BPE)

LLMs operam sobre **tokens** — unidade real de processamento, limite de contexto e cobrança. O algoritmo mais comum é o **BPE (*Byte Pair Encoding*)**, que define agrupamentos frequentes de caracteres durante o treinamento.

Regras práticas para engenharia:
1. Tokens são fixos do treinamento, não criados dinamicamente a cada requisição.
2. **Palavras ≠ Tokens:** código e palavras em português tendem a quebrar em mais subtokens do que o inglês, elevando custo e consumo de janela.
3. **Cada família de modelos tem seu próprio tokenizador:** o mesmo texto gera contagens diferentes em GPT, Claude, Gemini ou Llama. Meça com a ferramenta do provedor que você vai usar (ex.: `tiktoken` para modelos OpenAI, o endpoint de contagem de tokens da API da Anthropic, `count_tokens` do SDK do Gemini) antes de estimar orçamento ou depurar limites — nunca extrapole a contagem de um modelo para outro.

### Embeddings e Similaridade Semântica

Cada token vira um **embedding** (vetor numérico denso). O modelo executa operações matriciais sobre esses vetores: termos de contextos semelhantes ficam próximos no espaço vetorial, permitindo medir afinidade semântica via **similaridade de cosseno** mesmo sem palavras idênticas.

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
frases = [
    "Falha de autenticacao no endpoint de pagamento",
    "Erro 401 ao validar token na API de checkout",
    "Receita de pao de queijo mineiro",
]
emb = model.encode(frases, convert_to_tensor=True)

print("A vs B:", round(util.cos_sim(emb[0], emb[1]).item(), 3))  # Alta similaridade
print("A vs C:", round(util.cos_sim(emb[0], emb[2]).item(), 3))  # Baixa similaridade
```

### Anatomia do Bloco Transformer

Como o Transformer processa tokens em paralelo, ele soma **Positional Encoding** aos embeddings para preservar a ordem da sequência antes de entrar nos blocos internos.

```mermaid
flowchart LR
    T["Texto de Entrada"] --> TOK["Tokenizacao (BPE)"]
    TOK --> EMB["Embeddings + Positional Encoding"]
    EMB --> ATT["Multi-Head Self-Attention (Q, K, V)"]
    ATT --> NORM1["Residual + LayerNorm"]
    NORM1 --> FFN["Position-wise Feedforward (ReLU)"]
    FFN --> NORM2["Residual + LayerNorm"]
    NORM2 --> OUT["Distribuicao do Proximo Token"]
```

- **Self-Attention (Q, K, V):** cada token projeta vetores **Query** (o que busca), **Key** (o que oferece) e **Value** (o conteúdo). A interação `Q x K` define o peso que cada token atribui aos demais ao recompor seu significado a partir de `V`.
- **Multi-Head Attention:** executa múltiplas *heads* em paralelo; de forma emergente no treinamento, cada *head* se especializa em relações distintas (concordância gramatical, referência pronominal, tempo, semântica) e suas saídas são concatenadas.
- **Position-wise Feedforward Layers:** enquanto a atenção **mistura contexto entre tokens**, o bloco *feedforward* (`max(0, xW1 + b1)W2 + b2`) refina **cada posição individualmente**, reorganizando o contexto recebido antes da próxima camada.
- **Conexões Residuais e LayerNorm:** preservam o sinal original, estabilizam ativações numéricas e garantem fluxo saudável de gradientes em redes profundas.

### O que mudou desde o Transformer original (2017)

O diagrama acima descreve o bloco do artigo *Attention Is All You Need*. Os LLMs atuais mantêm a ideia central, mas trocaram várias peças — vale conhecê-las porque explicam limites práticos de contexto, memória e custo:

| Componente | Transformer original | Prática comum nos LLMs atuais | Por que importa na engenharia |
| :--- | :--- | :--- | :--- |
| **Posição** | *Positional encoding* senoidal absoluto | **RoPE** (*Rotary Position Embedding*) e variantes de extensão de contexto | Viabiliza janelas de centenas de milhares de tokens, mas a qualidade nas posições mais distantes varia por modelo |
| **Normalização** | *Post-norm* com LayerNorm | *Pre-norm*, frequentemente com **RMSNorm** | Treino mais estável em redes muito profundas |
| **Feedforward** | ReLU | **SwiGLU** / GELU | Melhor qualidade por parâmetro |
| **Atenção** | *Multi-Head* completa | **GQA/MQA** (*Grouped/Multi-Query Attention*), *FlashAttention* | Reduz memória do KV cache e acelera inferência com contexto longo |
| **Capacidade** | Denso (todos os pesos ativos) | Muitos modelos de fronteira usam **MoE** | Custo por token menor que o tamanho total do modelo sugere |

### Inferência na prática: *prefill*, *decode* e KV cache

Uma chamada a um LLM tem duas fases com perfis de custo diferentes — e entendê-las explica métricas que você vai observar em produção:

1. **Prefill:** todos os tokens de entrada são processados **em paralelo** de uma vez. Domina o **TTFT** (*Time To First Token*) e cresce com o tamanho do prompt.
2. **Decode:** cada token de saída é gerado **sequencialmente**, um por passo, reaproveitando as chaves e valores de atenção já calculados e guardados no **KV cache**. Domina o tempo total e explica por que **tokens de saída são mais caros e mais lentos** que tokens de entrada.

Consequências diretas: prompts longos pioram o TTFT; respostas longas pioram a latência total; *streaming* melhora a latência percebida, mas não o tempo total (Capítulo 7); e o **prompt caching** do provedor (Capítulo 2) funciona justamente reaproveitando o resultado do *prefill* de prefixos idênticos. Monitore **TTFT** e **tokens/segundo** como métricas separadas.

### As Três Famílias Arquiteturais

| Arquitetura | Atenção | Pré-treinamento | Referências | Melhor Caso de Uso |
| :--- | :--- | :--- | :--- | :--- |
| **Encoder-only** | Bidirecional (esquerda e direita) | MLM (*Masked Language Modeling*) | BERT, RoBERTa, DistilBERT, ALBERT | Embeddings, busca semântica, classificação, NER, análise de sentimento |
| **Decoder-only** | Unidirecional com **máscara causal** | CLM (*Causal Language Modeling*) | GPT, LLaMA, Mistral, Phi, Claude | Geração textual, chatbots, código, raciocínio aberto |
| **Encoder-Decoder** | Encoder bidirecional + Decoder causal | *Seq2Seq* | T5, BART | Tradução, sumarização controlada, reescrita |

Entre variantes *encoder-only*, **RoBERTa** prioriza qualidade, **DistilBERT** reduz latência/tamanho por destilação e **ALBERT** compartilha parâmetros para economizar memória.

---

## 1.3 Treinamento, Alinhamento e Otimização em Escala

O ciclo de vida de um LLM passa por três estágios principais:

1. **Pré-treinamento (auto-supervisionado):** aprende padrões linguísticos sem rótulos humanos. No **CLM**, prevê o próximo token usando **Cross-Entropy Loss** + *backpropagation*; no **MLM**, reconstrói tokens mascarados usando contexto bidirecional.
2. **Fine-Tuning Supervisionado (SFT):** adapta o modelo pré-treinado com exemplos rotulados de alta curadoria. Em empresas, o objetivo não é apenas "saber mais fatos", mas **internalizar vocabulário, tom, formato e restrições** — incluindo exemplos de respostas proibidas. Pode ser completo (caro) ou parcial.
3. **Alinhamento (Instruction Tuning e RLHF):** o *Instruction Tuning* melhora a obediência generalista a comandos; o **RLHF (*Reinforcement Learning from Human Feedback*)** combina SFT, modelo de recompensa humano e otimização (ex.: PPO) para gerar respostas úteis, seguras e capazes de admitir limites — com o custo e o viés da avaliação humana. Variantes mais recentes reduzem esse custo: **DPO** (*Direct Preference Optimization*) otimiza diretamente sobre pares de preferência sem treinar um modelo de recompensa separado, e **RLAIF** / *Constitutional AI* usam feedback gerado por modelos guiados por princípios explícitos.
4. **Treino de raciocínio (RL com recompensas verificáveis):** os chamados **modelos de raciocínio** (*reasoning models*) passam por uma etapa adicional de aprendizado por reforço em tarefas cujo resultado pode ser verificado automaticamente (testes de código, respostas matemáticas). Eles aprendem a gerar uma cadeia de raciocínio interna antes da resposta — o que melhora tarefas multi-etapa, mas consome **tokens de raciocínio cobrados como saída** e aumenta a latência. Escolha o nível de esforço de raciocínio (*reasoning effort* / *thinking budget*) pela dificuldade da tarefa, não por padrão.

### Técnicas de Otimização de Grandes Modelos

| Técnica | Gargalo Atacado | Mecanismo | Trade-off |
| :--- | :--- | :--- | :--- |
| **LoRA / PEFT** | Custo de GPU no *fine-tuning* | Congela pesos base e treina matrizes adaptadoras de baixo rank | Menor capacidade de mudança radical de domínio que SFT completo |
| **Quantização (FP32 → FP16 → INT8/INT4)** | Memória (VRAM) e custo de inferência | Reduz precisão numérica dos pesos | Possível perda leve de precisão em tarefas sensíveis (INT4) |
| **MoE (*Mixture of Experts*)** | Custo por inferência em modelos gigantes | Roteador ativa apenas parte dos especialistas por token (ex.: *Switch Transformer*) | Exige memória total alta para hospedar todos os especialistas |
| **P-Tuning / Prefix Tuning** | Adaptação leve sem alterar pesos | Treina vetores contínuos de contexto injetados na entrada | Menor expressividade que alterar pesos em tarefas complexas |

> [!TIP]
> **Esgote opções mais baratas antes de treinar:** na maioria dos cenários práticos, refinar prompts ou adotar RAG entrega mais valor com uma fração do custo e da manutenção de um *fine-tuning*.

---

## 1.4 Controle de Geração: Temperatura, Top-K, Top-P e Max Tokens

A cada token gerado, o modelo produz uma distribuição de probabilidades sobre o vocabulário. Os parâmetros de decodificação controlam essa amostragem:

- **Temperatura (`0.0` a `1.0` na Anthropic; `0.0` a `2.0` na OpenAI e no Gemini):** ajusta a concentração da distribuição. Valores baixos (`0.0`–`0.2`) favorecem os tokens mais prováveis — como um especialista indo direto à referência exata na biblioteca. Valores altos (`0.7`–`1.0`) elevam diversidade e criatividade, aumentando também o risco de deriva e alucinação.
- **Top-K:** limita a escolha aos `K` tokens mais prováveis (quantidade fixa).
- **Top-P (*Nucleus Sampling*):** seleciona o menor conjunto de tokens cuja probabilidade acumulada atinge `P` (quantidade dinâmica conforme a certeza do modelo).
- **Max Tokens:** teto rígido de tokens gerados na resposta.

| Perfil de Tarefa | Temperatura | Top-P | Objetivo |
| :--- | :--- | :--- | :--- |
| **Extração / JSON / SQL / Classificação** | `0.0` – `0.2` | `0.1` – `0.3` | Previsibilidade máxima e estabilidade de schema |
| **Explicação técnica / Suporte / Resumo** | `0.2` – `0.4` | `0.7` – `0.9` | Clareza, naturalidade controlada e fidelidade |
| **Brainstorming / Copywriting** | `0.7` – `0.9` | `0.9` – `0.95` | Diversidade lexical e exploração criativa |

A tabela mostra faixas típicas, mas os provedores recomendam **ajustar `temperature` ou `top_p`, não os dois ao mesmo tempo** — os efeitos se sobrepõem e tornam o comportamento difícil de explicar. Na prática, fixe `top_p` no padrão e calibre apenas a temperatura:

```python
generation_config = {
    "model": "extraction-default",  # Capacidade logica resolvida pelo AI Gateway (Cap. 7)
    "temperature": 0.1,             # Baixa variabilidade para extracao/classificacao
    "max_tokens": 512,              # Teto de saida: dimensione para o maior JSON valido esperado
}

# Verifique sempre o motivo de parada: truncamento nao e erro de rede
# OpenAI: finish_reason == "length" | Anthropic: stop_reason == "max_tokens"
```

> [!WARNING]
> **Armadilha de Depuração:** respostas cortadas no meio em Playgrounds ou APIs quase sempre decorrem de `max_tokens` baixo ou falha do *provider*, não de incapacidade do modelo — inspecione o `finish_reason`/`stop_reason` antes de culpar o prompt. Em testes comparativos, isole uma variável por vez em mensagens novas.

> [!IMPORTANT]
> **Temperatura `0` não é determinismo.** Mesmo com `temperature=0`, provedores podem devolver saídas diferentes para a mesma entrada (agrupamento de requisições em lote, aritmética de ponto flutuante em GPU, roteamento em MoE e atualizações silenciosas do modelo). Nunca projete um fluxo que dependa de saída byte a byte idêntica: valide **schema e regras** de forma determinística e use cache (Capítulo 7) quando precisar de respostas reproduzíveis.

> [!NOTE]
> **Modelos de raciocínio restringem parâmetros de amostragem.** Vários modelos de raciocínio ignoram ou rejeitam `temperature`/`top_p` customizados e expõem, em vez disso, um controle de esforço (*reasoning effort*) ou orçamento de raciocínio (*thinking budget*). Além disso, o `max_tokens` costuma incluir os tokens de raciocínio: um teto baixo pode esgotar o orçamento antes da resposta visível começar.

---

## 1.5 Limitações Estruturais de Produção e Estratégias de Mitigação

Antes de colocar LLMs em fluxos críticos, quatro limitações estruturais exigem mitigação arquitetural:

1. **Alucinação e Factualidade:** ocorre por lacunas de treino, prompts especulativos e ajuste para soar convincente em vez de admitir dúvida. Em áreas jurídica, médica ou financeira, plausibilidade não substitui verificabilidade documental. Mitigue restringindo fontes/datas, usando *few-shot*, exigindo recusa quando faltar evidência e mantendo revisão humana.
2. **Janela de Contexto e Diluição de Atenção:** caber na janela não garante foco. Enviar um PDF de 200 páginas inteiro pedindo uma cláusula da página 13 gera respostas vagas. Estudos de *"lost in the middle"* mostram que informações no meio de contextos longos tendem a ser menos aproveitadas que as do início e do fim, e a qualidade geral cai conforme o contexto cresce (*context rot*) — mesmo em modelos com janelas de centenas de milhares de tokens. Mitigue com **chunking**, recuperação seletiva, posicionamento das instruções críticas no início ou no fim e resumos hierárquicos (ciente da perda de detalhes finos).
3. **Raciocínio Simbólico e Erro Acumulado:** a geração autoregressiva acumula erros em matemática e deduções multi-etapas (como problemas de equações). *Chain of Thought* ajuda a organizar passos, mas **não garante prova formal** — delegue cálculos e validações críticas a código ou ferramentas externas.
4. **Conhecimento Estático vs. Tempo Real (RAG):** pesos do modelo congelam no treinamento e retreinar diariamente é inviável. O padrão **RAG (*Retrieval-Augmented Generation*)** separa o que o modelo guarda nos pesos do contexto fornecido em tempo de execução.

```mermaid
flowchart LR
    U["Query do Usuario"] --> QE["Embedding da Query"]
    QE --> RET["Retriever (Busca Semantica)"]
    KB["Base Vetorial Controlada (Docs, FAQs, S3)"] --> RET
    RET --> CHUNKS["Trechos Relevantes"]
    U --> PROMPT["Prompt Enriquecido"]
    CHUNKS --> PROMPT
    PROMPT --> LLM["LLM (Decoder-only)"]
    LLM --> ANS["Resposta Ancorada nas Fontes"]
```

O fluxo RAG em cinco etapas — **Query → Embedding → Retriever (em fontes corporativas controladas) → Enriquecimento de Contexto → Geração** — reduz ruído e impede que o modelo dependa de memória desatualizada sem precisar alterar seus pesos.

---

## 1.6 Quick Wins de Engenharia: Contexto Estruturado no Fluxo de Trabalho

Os fundamentos de contexto trazem ganhos imediatos no dia a dia de engenharia assistida por IA (IDEs e CLIs como Gemini CLI):

- **Separe entrada, regras e estado do projeto:**
  - `README.md`: visão de entrada e execução.
  - **Rules / Guidelines (`CLAUDE.md`, `GEMINI.md`):** stack autorizada, convenções de código, testes e **onde/por que** usar cada dependência (ex.: "Redis apenas para cache, nunca como fila").
  - **Estado (`state.md`):** bugs conhecidos, limitações e pendências. Mantenha preferências pessoais em arquivos locais (`state.local.md` no `.gitignore`) para não poluir o repositório do time.
- **Documentação viva e MCP:** organize guias de versões atuais por dependência (`docs-libs`) para evitar APIs obsoletas e conecte agentes via **MCP (*Model Context Protocol*)** a fontes reais como Jira, Confluence e documentação oficial.
- **Planeje com PRP (*Product Requirement Prompt*):** transforme requisitos (PRD/ADR) em um plano estruturado com árvore atual vs. futura, *library quirks*, *anti-patterns* e sequência de validação. Execute tarefa por tarefa (`execute prp`) com testes passando, revisão arquivo por arquivo e commits incrementais.
- **Reancore em sessões longas:** regras iniciais perdem peso conforme o chat cresce; faça checkpoints e reforce restrições críticas periodicamente.

---

## 1.7 Checklist de Aplicação Prática

- [ ] **Valide se o caso exige Gen AI:** confirme se geração aberta agrega valor real ou se busca, regras ou ML clássico entregam menor custo e risco.
- [ ] **Alinhe arquitetura à tarefa:** *encoder-only* para embeddings/busca/classificação, *decoder-only* para geração e *encoder-decoder* para tradução/sumarização.
- [ ] **Dimensione tudo em tokens, não em palavras:** teste prompts reais em um tokenizador (especialmente em português) antes de projetar orçamento e janela.
- [ ] **Calibre decodificação por objetivo:** use temperatura baixa (`0.0`–`0.2`) em automações e extrações, ajuste `temperature` *ou* `top_p` (não ambos), verifique `finish_reason`/`max_tokens` e não trate temperatura zero como garantia de determinismo.
- [ ] **Meça latência nas duas fases da inferência:** acompanhe TTFT (*prefill*) e tokens/segundo (*decode*) separadamente e escolha o esforço de raciocínio pela dificuldade real da tarefa.
- [ ] **Separe geração textual de fatos e cálculos:** delegue matemática/lógica formal a código externo e use RAG sobre bases confiáveis para dados recentes.
- [ ] **Esgote prompt e contexto antes de treinar:** recorra a SFT/LoRA apenas quando precisar internalizar comportamento, tom ou vocabulário que não estabiliza via contexto.
- [ ] **Governe o contexto do repositório:** separe rules compartilhadas de estado local (`.gitignore`), planeje features com PRP e mantenha testes e revisão humana obrigatórios.
