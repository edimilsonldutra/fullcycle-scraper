Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17976)

## Resumo da aula

O arquivo PRDProgress.json funciona como um artefato de tracking derivado do PRD. Em vez de recriar o documento inteiro, a skill PRD Writer lê o PRD já existente e produz apenas a estrutura de acompanhamento do projeto com base nas features definidas. Isso evita retrabalho e mantém consistência entre o planejamento original e o controle de execução. A comparação entre projetos também fica mais simples porque o ponto de partida continua sendo o mesmo PRD.

A skill PRD Writer, retomando o PRD já criado anteriormente, passa a ter como alteração principal a geração padrão do arquivo PRDProgress.json. A mudança não está em redefinir o PRD, mas em acrescentar uma saída operacional que organiza o andamento do projeto. Esse comportamento torna a skill útil não só para especificação, mas também para acompanhamento estruturado das entregas. O ganho prático está em transformar o conteúdo do PRD em um formato consumível por outras etapas do fluxo.

A instrução /prd writer acompanhada do PRD e do comando para gerar o arquivo JSON de tracking direciona a skill para uma tarefa específica: extrair as features do documento e montar apenas o artefato de acompanhamento. Esse recorte é importante porque elimina a necessidade de regenerar o PRD completo sempre que o objetivo for apenas atualizar ou produzir o tracking. O comportamento esperado da skill é interpretar o contexto existente e responder com a saída adequada ao pedido. Em fluxos com múltiplos artefatos, essa precisão reduz custo e ruído.

O PRDProgress.json registra as features do projeto, suas dependências, a organização por grupos e o estado inicial de execução. No exemplo, todas as entradas aparecem como pending, o que indica que o arquivo nasce como um mapa de trabalho ainda não iniciado. Além disso, ele preserva elementos organizacionais como waves e categorias de features, incluindo itens como tags, background processing, pipeline e video player. Esse formato permite enxergar o escopo total do projeto em uma estrutura única e objetiva.

As dependências listadas por feature tornam explícita a ordem ou a relação entre partes do sistema. Isso é relevante porque o tracking deixa de ser apenas uma checklist e passa a refletir restrições reais de implementação. Quando o projeto tem 12 features organizadas dessa forma, o arquivo serve como referência para priorização e coordenação do trabalho. O resultado é um acompanhamento mais próximo da estrutura lógica do produto.

Retomando a necessidade de manter o agente focado, o arquivo de tracking também funciona como mecanismo de controle operacional. Ao registrar quais features existem e em que estado estão, ele ajuda a impedir que o agente avance para outra frente fora do escopo desejado. Essa camada adicional de controle se conecta ao uso de harness, porque oferece um artefato objetivo para restringir e orientar a execução. Em vez de depender apenas do prompt corrente, o processo passa a ter um estado explícito do projeto.

## Transcrição

00:01

Bom, pessoal, seguinte, na tela aqui do meu computador, se você olhar,

00:05

eu tenho exatamente o PRD que a gente utilizou da última vez.

00:09

Por que eu estou dizendo isso?

00:10

Para que a gente consiga, inclusive,

00:12

comparar um projeto com outro e também para não sair criando nada do zero,

00:16

porque não faz sentido. Então,

00:19

o que acontece aqui? Eu tenho aquele PRD que a gente criou,

00:22

mas se você olhar agora aqui,

00:24

você vai ver que eu tenho diversas skills e a

00:27

gente vai falar de cada uma delas depois.

00:29

Mas a gente vai focar nessa aqui, que é o PRD Writer,

00:33

que é aquela skill que eu acabei falando para vocês.

00:36

Ela não muda absurdamente, mas você vai perceber que, por padrão,

00:42

ela vai gerar um PRD Progress .json aqui. Então, isso aí é um ponto importante.

00:48

São algumas fases que ela tem. Não mudou muito,

00:52

mas a principal alteração... É para essa mudança.

00:56

Obviamente que eu não vou ficar lendo. Palavra por palavra aqui na skill.

01:00

Mas é importante que você saiba.

01:02

Que a gente tem essa diferença. Então aqui na frente.

01:05

De todo mundo, vamos dizer assim. O que eu vou pedir aqui para ela fazer.

01:10

Eu vou fazer o seguinte. Eu vou colocar /prd writer. E eu vou colocar assim.

01:14

Eu vou colocar o meu PRD. E eu vou colocar assim.

01:18

Baseado no PRD. Gere.

01:22

O arquivo JSON.

01:26

de tracking do projeto baseado nas features. E aqui,

01:34

ele tem que ser esperto o suficiente para ler o meu PRD e gerar somente o arquivo de

01:38

tracking, para que eu não precise gerar o PRD todo

01:41

novamente para ele gerar o arquivo de tracking.

01:43

Então, isso é importante para que a gente consiga trabalhar nesse nosso caso.

01:49

De qualquer forma, esse PRD, ele...

01:53

já gera por padrão, se você for fazer qualquer coisa do zero,

01:56

esse arquivo de tracking é uma forma extremamente simples de

02:00

trackear, e a gente vai ver o porquê,

02:02

inclusive, porque a gente vai ter mais caras

02:04

interagindo com esse arquivo daqui pra frente,

02:06

tá? Então, ele tá gerando aqui, ó, meu PRDProgress .json com

02:12

todas as features e organizações, as waves,

02:15

tudo aquilo que a gente tava querendo, tá?

02:17

Então, se eu olhar agora aqui, eu tenho PRDProgress .json. E agora aqui,

02:23

o que ele acaba fazendo? Olha só. Ele mostra aqui tudo como pending,

02:26

o nome de cada feature, as dependências de cada uma dessas features,

02:32

a organização aqui de tags, background processing, pipeline, video player. Então,

02:37

ele traz todas as features aqui, que são 12 features,

02:39

que elas podem ser desenvolvidas aqui para a gente.

02:43

Então, isso aqui é um aspecto importante.

02:46

O PRD Writer vai ajudar bastante a gente nesse próximo...

02:51

passo que a gente tem em relação à parte de harness.

02:54

É mais uma forma de eu conseguir segurar o agente

02:58

pra que ele não vá pra outra feature,

03:00

pra que a gente consiga manter um pouco mais

03:02

De controle durante todo o nosso processo.

## Resumo IA

**Abreviações**
*   **PRD:** Product Requirements Document
*   **JSON:** JavaScript Object Notation

**Resumo**
A aula abordou a funcionalidade do arquivo `PRDProgress.json` como um artefato de tracking derivado do Product Requirements Document (PRD) original. O objetivo principal é otimizar o acompanhamento de projetos de desenvolvimento de software, eliminando retrabalho e mantendo a consistência entre o planejamento e a execução.

A skill `PRD Writer` é a ferramenta central, tendo sido atualizada para gerar o `PRDProgress.json` por padrão. Em vez de recriar o PRD completo, a skill lê o documento existente e produz apenas a estrutura de acompanhamento do projeto, focando nas features definidas. Isso simplifica a comparação entre projetos, pois o ponto de partida é sempre o mesmo PRD.

O fluxo de trabalho envolve utilizar o comando `/prd writer` acompanhado do PRD e da instrução para "gerar o arquivo JSON de tracking do projeto baseado nas features". Essa diretriz assegura que a skill extraia exclusivamente as features e suas informações para montar o artefato de acompanhamento, sem a necessidade de regenerar o PRD completo.

O `PRDProgress.json` detalha as features do projeto, suas dependências, a organização por grupos (como "waves" e categorias específicas como "tags", "background processing", "pipeline", "video player") e o estado inicial de execução, que é "pending" para todas as entradas. Este formato proporciona uma visão objetiva e estruturada do escopo total, facilitando a priorização e a coordenação do trabalho ao explicitar as restrições reais de implementação.

**Pontos de atenção**
*   **Reaproveitamento do PRD:** A principal vantagem é evitar a regeneração do PRD completo. A skill `PRD Writer` é projetada para ler o PRD existente e extrair apenas as informações necessárias para o tracking, economizando tempo e recursos.
*   **Consistência e Comparabilidade:** Utilizar o PRD original como base garante consistência entre o planejamento inicial e o controle de execução, além de simplificar a comparação de projetos.
*   **Instrução Específica:** É fundamental fornecer à skill `PRD Writer` uma instrução clara para gerar *apenas* o arquivo JSON de tracking (`gerar o arquivo JSON de tracking do projeto baseado nas features`). Isso impede a regeneração desnecessária do PRD completo.
*   **Estrutura e Conteúdo do `PRDProgress.json`:** O arquivo nasce com todas as features em estado "pending", servindo como um mapa de trabalho inicial. A inclusão explícita de dependências entre features é crucial para refletir a lógica do produto e auxiliar na priorização.
*   **Controle do Agente (Harness):** O `PRDProgress.json` atua como um mecanismo de controle operacional, oferecendo um artefato objetivo para restringir e guiar a execução do agente. Ele ajuda a manter o agente focado no escopo e evita desvios, complementando o uso de `harness` ao fornecer um estado explícito do projeto.