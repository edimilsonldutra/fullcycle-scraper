Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17978)

## Resumo da aula

Practical

O Spec Writer continua produzindo os artefatos já esperados, como spec.md para a especificação técnica e plan.md para o plano de execução, mas passa a incluir também contracts.md como parte do fluxo. Essa extensão muda o foco da geração de features porque adiciona uma camada explícita de comportamento esperado, legível tanto para implementação quanto para validação. Em vez de depender apenas da descrição técnica, a feature passa a carregar contratos de comportamento derivados do que o produto exige.

O arquivo contracts.md usa o formato GWT: Given, When, Then. Esse formato organiza critérios de comportamento como contexto inicial, ação executada e resultado esperado, o que facilita a leitura e reduz ambiguidade. No exemplo de login, “dado que existe uma tela de login”, “quando o formulário é preenchido e o botão é clicado”, “então o usuário deve estar autenticado”. O valor prático disso é transformar expectativa funcional em uma estrutura que pode orientar implementação, revisão e testes.

Retomando o PRD e o tracking já estabelecidos, o ponto novo aqui é que os critérios de aceitação do PRD.md deixam de ser apenas referência textual e passam a alimentar diretamente o contracts.md. Isso cria continuidade entre definição de produto e especificação executável da feature, sem exigir que os contratos sejam escritos do zero. Quando os critérios de aceitação estão bons, o contrato gerado tende a preservar a intenção funcional com menos perda de contexto.

O fluxo do Spec Writer inclui uma entrevista técnica para refinar a feature antes da geração dos artefatos. Em cenários de demonstração ou aceleração do processo, o comando auto accept instrui o agente a assumir concordância automática com as perguntas feitas, evitando interrupções longas no refinamento. Esse atalho é útil para ganhar velocidade, mas reduz a oportunidade de ajustar decisões de escopo, comportamento ou implementação durante a interação.

A geração pode ser direcionada para uma feature específica, como a feature 01, usando o PRD como fonte de contexto. Isso permite trabalhar incrementalmente sobre partes do produto, em vez de tentar detalhar tudo de uma vez. Na prática, o agente lê o PRD, deriva os contratos e produz os artefatos necessários para aquela feature, mantendo o fluxo alinhado ao planejamento do projeto.

Quando a instrução create issue é incluída no fluxo, o processo pode abrir automaticamente uma issue no GitHub. Essa integração conecta a especificação gerada ao gerenciamento operacional do trabalho, reduzindo tarefas manuais de acompanhamento. O ganho não está na geração do texto em si, mas em transformar a saída da especificação em item rastreável dentro do repositório.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente falou ali sobre o spec writer,

00:05

né? E aqui é a skill de spec writer modificada, né?

00:08

E o ponto principal é a parte do contract.md, tá?

00:12

Obviamente que eu não vou ler esse skill inteiro aqui com você,

00:15

mas é importante que você consiga se ligar aqui. O ponto importante é,

00:21

ele vai continuar gerando aquele spec.md, que é a especificação mais técnica.

00:25

Ele vai continuar gerando aquele plan.md,

00:29

que é o planejamento passo a passo do que ele vai fazer, mas aqui também, tá?

00:34

Ele vai usar o contracts.md ali no formato GWT.

00:40

Eu não sei se você já viu, né?

00:42

Given, When e Then. Então,

00:44

é uma forma fácil de você conseguir pensar de como que alguém vai ler e entender.

00:51

Dado que eu tenho uma tela de login,

00:53

quando eu preencher os dados do formulário e clicar em tal botão...

00:58

então eu devo estar autenticado.

00:59

Coisas desse tipo, tá? Então, essa que é a ideia principal.

01:02

Então, aqui estão os steps que ele deve seguir.

01:07

Basicamente, eu coloquei algumas coisas interessantes que se eu

01:11

colocar create issue no meio da história,

01:13

ele pode criar já uma issue no GitHub pra facilitar a vida. Então,

01:17

tem algumas coisas que são interessantes ali no meio da história, tá?

01:21

Uma outra coisa que tem aqui é,

01:23

ele vai fazer uma entrevista técnica também com a gente.

01:26

E eu sempre vou, pelo menos nessas partes agora, eu sempre vou falar,

01:29

parta do princípio que eu concordo com tudo que você tá me entrevistando,

01:33

senão a gente vai ficar 10 horas aqui gerando as features e tudo mais,

01:38

tá? Mas basicamente, a ideia é a gente conseguir utilizar...

01:43

esse cara pra gerar features. Você vai ter acesso a tudo isso,

01:46

você vai conseguir olhar com calma, tá?

01:48

Mas é importante que você saiba que esse spec writer,

01:52

ele vai funcionar dessa forma aqui, tá?

01:56

Baseado, inclusive, numa coisa. O contract.md,

02:00

ele é gerado e derivado dos critérios

02:03

de aceitação que o próprio PRD.md gerou,

02:08

tá, galera? Então, isso aí é algo importante.

02:11

Todos esses critérios de aceitação aqui do PRD, né?

02:15

São usados como base para o contract.md acabar gerando ali para a gente.

02:20

Então, isso aí é um aspecto ali super importante.

02:24

O que eu vou fazer agora aqui, né?

02:26

Para deixar esse cara gerando aqui para a gente poupar tempo,

02:31

vai ser o seguinte. Eu vou colocar aqui spec writer, tá?

02:35

E eu vou falar agora que eu vou utilizar o PRD.

02:41

E vou querer gerar a feature 01 aqui para mim. E eu vou escrever assim,

02:47

auto accept aqui para mim,

02:51

para ele auto aceitar qualquer coisa. Ou seja,

02:54

parta do princípio que eu estou aceitando tudo que você

02:58

está me falando para gerar aqui essa minha feature.

03:01

Então é basicamente isso que vai acontecer.

03:04

Ele vai ler e vai gerar aqui a minha feature 01 aqui para eu trabalhar.

03:09

E aí ele vai demorar um pouquinho pra gerar tudo isso.

03:12

Mas daí, no próximo vídeo, a gente volta com tudo isso.

03:15

Gerado para que você não tenha que ficar esperando.

## Resumo IA

**Abreviações**

*   **spec.md**: Arquivo de especificação técnica.
*   **plan.md**: Arquivo de plano de execução.
*   **contracts.md**: Arquivo de contratos de comportamento.
*   **GWT**: Given, When, Then (Dado, Quando, Então) – Formato para organizar critérios de comportamento.
*   **PRD**: Product Requirements Document (Documento de Requisitos de Produto).
*   **GitHub**: Plataforma de gerenciamento de repositórios de código e issues.

**Resumo**

A aula aborda as modificações na ferramenta Spec Writer, com o objetivo principal de integrar explicitamente o arquivo `contracts.md` ao fluxo de geração de artefatos. Além dos já existentes `spec.md` (especificação técnica) e `plan.md` (plano de execução), o `contracts.md` é introduzido para adicionar uma camada de comportamento esperado, legível tanto para implementação quanto para validação. Este novo artefato utiliza o formato GWT (Given, When, Then), que organiza os critérios de comportamento em contexto inicial, ação executada e resultado esperado, facilitando a leitura e reduzindo a ambiguidade.

O fluxo de trabalho estabelece uma ligação direta entre os critérios de aceitação definidos no `PRD.md` e a geração do `contracts.md`, garantindo que os contratos derivem diretamente das necessidades do produto sem a necessidade de serem escritos do zero. Antes da geração dos artefatos, o Spec Writer realiza uma entrevista técnica para refinar a feature. Para cenários de demonstração ou aceleração, o comando `auto accept` instrui o agente a concordar automaticamente com as perguntas, agilizando o processo. A ferramenta permite direcionar a geração para uma feature específica (ex: `feature 01`), utilizando o PRD como contexto, o que possibilita um desenvolvimento incremental. Além disso, a instrução `create issue` pode ser incluída no fluxo para que o processo abra automaticamente uma issue no GitHub, integrando a especificação gerada ao gerenciamento operacional do trabalho.

**Pontos de atenção**

*   **Qualidade dos Critérios de Aceitação:** A eficácia do `contracts.md` depende diretamente da qualidade dos critérios de aceitação definidos no `PRD.md`. Critérios bem elaborados garantem que os contratos gerados preservem a intenção funcional com menos perda de contexto.
*   **Benefício do Formato GWT:** O uso do formato GWT (Given, When, Then) para os contratos é uma boa prática que organiza os critérios de comportamento de forma clara, reduz a ambiguidade e transforma expectativas funcionais em uma estrutura útil para orientar implementação, revisão e testes.
*   **Trade-off do `auto accept`:** Embora o comando `auto accept` seja útil para acelerar o processo em demonstrações ou testes, ele elimina a oportunidade de refinamento crítico e ajuste de decisões de escopo, comportamento ou implementação que ocorreria durante a entrevista técnica.
*   **Valor da Integração com GitHub:** A integração com o GitHub através da instrução `create issue` agrega valor significativo ao transformar a saída da especificação em um item de trabalho rastreável, otimizando o gerenciamento operacional do projeto além da simples geração de texto.
*   **Foco na Explicação de Comportamento:** A inclusão do `contracts.md` representa um ponto crítico de mudança no fluxo do Spec Writer, deslocando parte do foco da descrição puramente técnica para uma camada explícita de comportamento esperado do produto.