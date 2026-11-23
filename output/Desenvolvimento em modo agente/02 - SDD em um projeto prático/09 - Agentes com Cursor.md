Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17787)

## Resumo da aula

A Agents Window do Cursor combina características de IDE com comportamento de execução autônoma semelhante ao de ambientes como Cloud Desktop e Codex App. A diferença prática não está apenas na interface, mas no fato de que o agente pode inspecionar o repositório, interpretar contexto e agir sobre arquivos, dependências e comandos. Isso desloca o papel do desenvolvedor de executor direto para orquestrador da tarefa, escolhendo contexto, modelo e instruções operacionais.

O Cursor permite trabalhar em modo automático, delegando à plataforma a escolha do modelo mais adequado, ou selecionar explicitamente um modelo específico, como uma variante premium. Essa escolha afeta custo, velocidade e estilo de execução do agente, inclusive o grau de iniciativa durante a tarefa. Quando o modo Auto escolhe um modelo mais otimizado para throughput, a execução tende a ser mais rápida, mas isso não garante melhor aderência ao fluxo operacional esperado.

Retomando o uso de @PRD e das features já especificadas, o ganho aqui está em explicitar a ação operacional desejada: verificar critérios de aceitação e executar testes end-to-end. Esse refinamento reduz ambiguidade sobre o que significa “testar”, especialmente quando outra ferramenta havia validado apenas internamente. Em fluxos com agentes, pedir “faça os testes” é insuficiente; nomear o tipo de teste orienta a escolha de ferramentas e limita interpretações excessivamente livres.

A velocidade observada durante a execução pode indicar que o agente está usando um modelo com alto throughput de tokens por segundo, possivelmente diferente de modelos mais lentos e deliberativos. Essa percepção é útil porque o comportamento do agente não depende só do prompt, mas também da família de modelo selecionada pela plataforma. Em prática, isso influencia quanto contexto ele lê, quão rápido propõe mudanças e como decide entre explorar o código ou agir imediatamente.

O agente tende a percorrer muitos arquivos antes de agir para construir uma visão operacional do projeto. Esse comportamento é esperado em tarefas que envolvem critérios de aceitação, porque o agente precisa localizar rotas, configuração, testes existentes e pontos de integração. O custo dessa exploração cresce quando o guidance não define boundaries claros sobre onde procurar e o que modificar.

Lembra da distinção anterior entre Playwright CLI e outras formas de automação? Aqui ela aparece como consequência prática: ao não receber a instrução explícita para usar Playwright CLI, o agente decide instalar Playwright e Chromium localmente para conseguir executar testes end-to-end. O problema não é apenas instalar dependências, mas fazer isso por inferência, alterando o ambiente e potencialmente expandindo o escopo operacional sem autorização explícita.

Quando o agente precisa viabilizar a execução de testes, ele pode modificar arquivos auxiliares como globalsetup.ts para adaptar o projeto ao fluxo que inferiu. Esse tipo de mudança nem sempre corresponde ao objetivo principal da feature; muitas vezes é uma consequência indireta da estratégia escolhida pelo agente para conseguir validar o sistema. Sem harness e sem restrições operacionais, essas alterações colaterais se tornam mais prováveis.

Cada ferramenta e cada modelo apresentam padrões próprios de navegação, edição e execução. Essa variabilidade torna inadequado confiar apenas em “inteligência geral” do agente para obter consistência entre ambientes. A previsibilidade vem do harness: scripts, comandos, convenções e limites explícitos que transformam uma intenção ampla em um fluxo reproduzível.

A possibilidade de manter várias sessões do Cursor executando tarefas em paralelo reforça a ideia de orquestração, não apenas de assistência pontual dentro da IDE. Isso amplia produtividade, mas também multiplica o risco de divergência de comportamento entre agentes se cada sessão interpretar o contexto de forma diferente. Paralelismo com agentes exige ainda mais padronização de entrada, validação e execução.

## Transcrição

00:01

Bom, pessoal, como eu mostrei no Cloud Desktop e no Codex,

00:04

vou dar mais um exemplo aqui em relação ao Cursor,

00:08

por exemplo. O Cursor, eu posso chegar,

00:11

pelo menos é a forma como está nesse momento,

00:14

essas plataformas mudam, a interface muda,

00:16

mas eu acredito que muitos dos conceitos, aos poucos, eles vão ficando,

00:19

onde eu posso pedir para o Cursor fazer o que eu estou querendo.

00:24

Mas o Cursor também tem Agents Window, que é uma forma onde ele é uma ideia...

00:29

Mas ele também funciona como um Cloud Desktop, um Codex App ou algo desse tipo,

00:34

tá? Então o que eu vou fazer? Eu vou maximizar esse cara aqui, tá?

00:39

Aqui ele está olhando o meu

00:42

repositório remoto, porque eu estou dentro ali do projeto,

00:48

mas na real eu quero abrir um workspace que é o MBA Aluno aqui, certo?

00:54

E nesse cara ele já está falando qual é o branch que eu estou.

00:57

E aqui eu posso escolher auto, ou seja,

01:00

se eu quero trabalhar de uma forma balanceada com o modelo que

01:05

ele acha que é o melhor para fazer aquela tarefa,

01:07

ou se eu quiser,

01:08

eu posso escolher qual é o modelo que eu vou utilizar para fazer esse tipo de coisa,

01:14

se eu vou trabalhar de forma premium ou se eu vou trabalhar etc.

01:18

Então eu posso chegar, por exemplo, eu vou trabalhar com o Opus 4.7 High.

01:25

E aqui, nesse momento, o que eu posso chegar e falar?

01:28

Olha, eu vou usar o normal dele aqui,

01:33

o alto, que provavelmente ele vai pegar o Composer 2. Eu vou pedir à Leia,

01:42

o arroba PRD,

01:46

e

01:48

também as features 01, deixa

01:54

eu colocar aqui arroba 01 e

01:59

02.

02:08

Cadê a minha 02 aqui,

02:12

arroba 02, é

02:17

esse cara aqui, que eu quero mesmo, é esse cara aqui,

02:22

02, veja os critérios de

02:27

aceitação e faça os testes,

02:30

eu vou falar testes end-to-end, eu vou escrever mais objetivo,

02:38

pra não dizer que eu não estou sendo justo com o Cursor

02:40

e que eu não fui tão justo com o Codex,

02:42

tá? O Codex falou que ele testou internamente apenas, mas ele não usou o Playwright.

02:46

Vou colocar dessa forma aqui pra ver como é que

02:48

ele acabou colocando com o modelo mais rápido, né?

02:51

O mais otimizado que ele acha.

02:53

Eu acredito que ele vai pro Composer 2 aqui, talvez. Tá?

02:58

E aqui, vendo... É, provavelmente, nessa velocidade aqui que ele está fazendo,

03:02

provavelmente ele vai trabalhar... ele deve estar com outro modelo,

03:08

com certeza ele não está com os modelos da Anthropic,

03:10

ele está com os modelos feitos pela própria Cursor,

03:12

que tem um TPS, muito rápido, tokens por segundo,

03:19

então é muito louco como ele está validando e ele está trabalhando.

03:24

E aqui eu posso ter várias sessões do Cursor fazendo as coisas aqui para mim. Então,

03:30

cada vez mais a gente percebe que a gente tem ferramentas onde a gente orquestra os

03:34

Agentes e a gente tem as ferramentas onde nós

03:37

temos as nossas IDEs e coisas desse tipo.

03:41

Então, isso aí é um ponto importante para a gente entender. Mas, novamente,

03:46

dá para perceber que ele está lendo todos

03:47

os meus arquivos para entender o que existe.

03:53

E agora... ele está ali rodando os testes,

03:57

instalando dependências, e ele está instalando o Playwright com o Chromium,

04:02

para ele poder fazer a abertura do browser, provavelmente, entendeu?

04:06

Como eu nunca falei para ele usar o Playwright CLI,

04:09

ele está ali instalando coisas aqui no meu computador,

04:12

na parada, para rodar o Playwright, para fazer o teste C2E, entendeu?

04:19

E aí as coisas vão escalando.

04:23

O grande ponto que eu quero trazer aqui para vocês, pessoal, é o seguinte.

04:28

Cara, ele saiu mudando os meus arquivos aqui em relação a globalsetup.ts aqui.

04:34

Mas o

04:36

ponto principal que eu acredito é que cada ferramenta vai ter sua peculiaridade,

04:43

cada modelo vai trabalhar de uma forma bem diferente e o que vai fazer

04:47

a diferença é toda a parte de harness e que a gente vai chegar lá. Beleza?

04:52

Então, não quero fazer com que você fique olhando aqui a tela do cursor,

04:56

vamos deixar essa parada rodar,

04:58

e aí a gente vai para a nossa feature número 3,

05:01

e depois a gente vai entrar na parte do desenvolvimento paralelo.

## Resumo IA

**Abreviações**
*   **IDE**: Integrated Development Environment
*   **PRD**: Product Requirements Document (referência a um documento de requisitos)
*   **TPS**: Tokens Por Segundo
*   **CLI**: Command Line Interface
*   **E2E**: End-to-End (fim a fim)

**Resumo**
A aula teve como objetivo demonstrar a Agents Window do Cursor, uma ferramenta que combina características de IDE com a capacidade de execução autônoma de agentes, similar a ambientes como Cloud Desktop e Codex App. O instrutor destacou que a diferença prática do Cursor reside na capacidade do agente de inspecionar o repositório, interpretar o contexto e agir sobre arquivos, dependências e comandos, transformando o desenvolvedor de executor direto para orquestrador de tarefas.

Foram abordados conceitos como a escolha do modelo de IA (modo "Auto" para balanceamento, ou seleção explícita de modelos premium como Opus 4.7 High, ou otimizados para throughput como Composer 2). Essa escolha impacta custo, velocidade e o estilo de execução do agente, incluindo seu grau de iniciativa. Foi enfatizada a importância de prompts claros e objetivos, como "faça os testes end-to-end", em contraste com instruções vagas como "faça os testes", que podem levar a interpretações excessivamente livres.

No fluxo demonstrado, o instrutor abriu o workspace "MBA Aluno" no Cursor e, utilizando o modo "Auto" (que provavelmente selecionou um modelo otimizado para velocidade), instruiu o agente a "verificar critérios de aceitação e fazer os testes end-to-end" com base em @PRD e features 01 e 02. Observou-se que o agente explorou muitos arquivos para construir seu contexto operacional, instalou dependências como Playwright e Chromium, e modificou arquivos auxiliares (ex: `globalsetup.ts`) para viabilizar a execução dos testes E2E, sem que isso fosse explicitamente solicitado. A velocidade da execução indicou o uso de um modelo com alto TPS. A aula concluiu ressaltando que cada ferramenta e modelo possui padrões próprios de navegação e execução, e que a previsibilidade e consistência dependem da implementação de um "harness" robusto. A possibilidade de múltiplas sessões paralelas do Cursor reforça a ideia de orquestração, mas exige maior padronização para evitar divergências.

**Pontos de atenção**
*   **Especificidade dos Prompts:** Instruções genéricas como "faça os testes" são insuficientes. É crucial ser explícito sobre o tipo de teste (ex: "testes end-to-end") e as ferramentas desejadas (ex: "usar Playwright CLI") para orientar o agente e evitar interpretações livres ou ações inesperadas.
*   **Impacto da Escolha do Modelo:** O modo "Auto" pode priorizar modelos com alto throughput (TPS) para velocidade, o que nem sempre garante a melhor aderência ao fluxo operacional esperado ou um comportamento mais deliberativo. A escolha do modelo afeta diretamente custo, velocidade e estilo de execução do agente.
*   **Comportamento de Exploração e Custo:** Agentes tendem a percorrer muitos arquivos para construir uma visão operacional do projeto. Essa exploração pode ser custosa e ineficiente se as instruções (guidance) não definirem limites claros sobre onde procurar e o que modificar.
*   **Modificações Não Autorizadas:** Sem instruções explícitas, agentes podem inferir a necessidade de instalar dependências (ex: Playwright e Chromium) e modificar arquivos auxiliares (ex: `globalsetup.ts`), alterando o ambiente e o escopo operacional sem autorização, o que pode não corresponder ao objetivo principal da tarefa.
*   **Variabilidade e Consistência:** Cada ferramenta e modelo de IA apresenta padrões próprios de navegação, edição e execução. Não se deve confiar apenas na "inteligência geral" do agente para obter consistência entre ambientes.
*   **Necessidade de "Harness":** A previsibilidade e consistência no comportamento do agente vêm do uso de um "harness" – um conjunto de scripts, comandos, convenções e limites explícitos que transformam intenções amplas em um fluxo reproduzível e controlado.
*   **Riscos do Paralelismo:** Embora a execução paralela de múltiplas sessões do Cursor aumente a produtividade, ela multiplica o risco de divergência de comportamento entre agentes se cada sessão interpretar o contexto de forma diferente. O paralelismo com agentes exige uma padronização ainda maior de entradas, validações e execuções.
*   **Mudança de Papel do Desenvolvedor:** O desenvolvedor assume um papel mais de orquestrador, escolhendo contexto, modelo e instruções operacionais, em vez de ser um executor direto das tarefas.