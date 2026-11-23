Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17975)

## Resumo da aula

O PRD Writer continua sendo o componente que transforma uma ideia inicial de produto em uma definição organizada, como já vinha sendo usado anteriormente. A diferença agora está na ampliação da sua responsabilidade: além de estruturar o PRD, ele também passa a produzir o artefato que acompanha a execução do projeto. Isso fortalece as fronteiras do processo de desenvolvimento, especialmente quando várias tarefas avançam em paralelo.

O acompanhamento do projeto deixa de ser uma anotação solta em texto livre e passa a existir como tracking.json. Esse arquivo registra o progresso em uma estrutura previsível, legível por agentes e por outros processos automatizados. No Harness, essa previsibilidade importa porque reduz ambiguidades operacionais e cria uma base objetiva para continuidade do trabalho.

Texto livre é flexível demais para um fluxo que depende de consistência entre etapas. O modelo pode variar formato, omitir uma feature, duplicar informação ou renomear etapas de forma inconsistente, o que dificulta leitura automatizada e manutenção do estado do projeto. JSON reduz essa fricção ao impor campos mais claros e organização estável, mesmo sem eliminar totalmente a possibilidade de erro.

No VideoMax, o tracking nasce das features definidas no próprio PRD, em vez de ser criado manualmente depois. A sequência é direta: o PRD Writer entende o escopo, define as features do ciclo de desenvolvimento e, a partir dessa definição, gera o tracking inicial. Isso mantém o acompanhamento alinhado ao escopo real do produto e evita divergência entre planejamento e execução.

Se o PRD já estiver pronto, a mesma skill pode ser usada apenas para gerar o tracking.json. Essa possibilidade reaproveita a definição existente sem exigir reconstrução do documento completo. O ganho prático é acelerar a adoção do tracking estruturado mesmo em projetos que já começaram.

Retomando o uso do agente ao longo de sessões extensas, o histórico conversacional nem sempre é uma fonte confiável de estado. Decisões podem ficar escondidas no meio da sessão, o contexto pode se degradar e o volume de features torna esse problema mais severo. O tracking.json funciona como uma fonte objetiva do que já foi feito, sustentando melhor a operação das skills dentro do Harness.

## Transcrição

00:01

Bom pessoal, agora que a gente tem gates,

00:03

a gente conseguiu trabalhar com a parte de UI,

00:05

a gente falou da skill principal para conseguir dar guidance,

00:09

a gente falou de scaffolding,

00:10

a gente vai agora voltar naqueles aspectos que a gente acaba caindo sobre SDD,

00:16

mas agora de uma forma um pouco diferente.

00:18

Então a gente vai voltar a falar sobre o PRD Writer, que é o mesmo cara,

00:24

um pouco adaptado do que a gente utilizou quando a gente falou sobre SDD.

00:29

O PRD Writer vai ser responsável por pegar uma ideia

00:32

de um produto inicial e transformar aquilo em uma definição organizada.

00:36

A gente já tem esse PRD pronto, inclusive do outro projeto.

00:41

Então a gente já entende como é que funciona o PRD,

00:44

como que ele gera e como que ele funciona.

00:47

Porém, nesse nosso caso, a gente vai ter uma peculiaridade.

00:51

Nós vamos ter algo um pouquinho diferente do que aquele PRD inicial.

00:55

Por quê? Porque agora,

00:57

como a gente está querendo organizar melhor as fronteiras e

01:00

organizar melhor o processo de desenvolvimento como um todo,

01:04

a gente precisa amarrar um pouco as pontas,

01:07

principalmente porque muitas vezes a gente vai desenvolver tarefas em paralelo.

01:13

E a gente tem que ter em algum lugar como que a gente mantém o tracking do projeto.

01:18

E por isso que no nosso fluxo,

01:20

o PRD Writer não vai gerar apenas o documento de PRD para ser lido por uma pessoa.

01:26

Ele também vai gerar um arquivo de tracking de progresso.

01:29

Esse tracking vai ser um JSON.

01:31

E isso é bem importante para o funcionamento do Harness. Por que JSON?

01:36

Porque quando a gente deixa esse acompanhamento, vamos dizer assim,

01:40

apenas em texto livre, o modelo pode se perder mais facilmente.

01:45

Ele pode mudar o formato, esquecer uma feature, duplicar informação,

01:49

alterar o nome de uma etapa ou gerar uma estrutura um

01:51

pouco mais difícil de ser lida por outros processos.

01:54

Quando a gente usa JSON ou algum formato que seja mais consolidado,

01:59

vamos dizer, a gente reduz esse tipo de erro, tá?

02:02

Eu não quero dizer que o JSON nunca vai errar,

02:05

que essa estrutura vai ficar mais previsível,

02:07

que o arquivo vai passar a ter campos mais claros,

02:09

dados mais organizados e etc.

02:11

O grande ponto é que a gente tende a reduzir um pouquinho essa fricção.

02:15

Então, no VideoMax,

02:17

o tracking não vai ser apenas uma anotação solta

02:20

dizendo que essa feature está em andamento,

02:22

que essa feature está concluída.

02:25

Ela vai ser uma estrutura mais organizada com base

02:29

nas próprias features que o PRD Writer definiu.

02:32

Durante a geração do PRD. Isso aí é essencial,

02:35

porque o PRD entende primeiro o escopo,

02:38

define quais features vão fazer parte daquele

02:41

produto ou daquele ciclo de desenvolvimento.

02:43

Depois, a partir dessa própria definição,

02:47

ele gera o tracking inicial do projeto. Ou seja,

02:50

O tracking nasce conectado... Com o PRD. Ele não é um arquivo separado,

02:56

criado manualmente depois. Ele é derivado do que o próprio PRD Writer estruturou.

03:00

E, obviamente, a gente pode usar essa skill para,

03:03

caso a gente já tenha o PRD pronto,

03:05

pedir para ele gerar apenas o nosso JSON ali, nesse nosso caso.

03:09

Então, isso vai ajudar bastante ainda durante todo esse processo.

03:14

Beleza? Então, eu acho que, a partir de agora, vai ficar mais fácil,

03:18

porque o agente pode perder contexto, a sessão pode ficar longa demais,

03:23

algumas decisões podem ficar escondidas no meio do histórico,

03:26

e quando a gente tem várias features, isso fica ainda mais complicado. Então,

03:30

o tracking .json vai resolver uma parte desse problema,

03:34

porque já fica uma fonte mais objetiva do que já foi feito.

03:38

Então, isso aí é importante. Então, o PRD evolui.

03:44

E eu vou mostrar para vocês aí como é que funciona.

03:46

Basicamente, são alterações daqui para frente para aquelas

03:50

várias skills que a gente já criou,

03:52

melhoradas para que a gente consiga ter mais sustento, vamos dizer,

03:58

em relação a toda essa parte do Harness. Então, vamos nessa.

## Resumo IA

**Abreviações**

*   **PRD**: Product Requirements Document (Documento de Requisitos de Produto) - Uma definição organizada de uma ideia inicial de produto.
*   **JSON**: JavaScript Object Notation - Um formato estruturado e legível por máquinas para registro e troca de dados, utilizado para manter o tracking do projeto.

**Resumo**

A aula aborda a evolução do componente PRD Writer dentro do processo de desenvolvimento, especificamente no contexto do sistema Harness. O objetivo central é aprimorar o acompanhamento e a gestão de projetos, especialmente quando diversas tarefas avançam em paralelo.

O PRD Writer, que antes se dedicava a transformar uma ideia inicial de produto em um PRD (Product Requirements Document) organizado, agora tem sua responsabilidade ampliada. Além de estruturar o PRD, ele passa a produzir um artefato de acompanhamento da execução do projeto: o `tracking.json`.

Esse arquivo `tracking.json`, baseado no formato JSON, é a principal ferramenta introduzida para substituir anotações soltas em texto livre. A previsibilidade e estrutura do JSON são cruciais para reduzir ambiguidades operacionais no Harness e fornecer uma base objetiva para a continuidade do trabalho. O instrutor enfatiza que o texto livre é excessivamente flexível, propenso a inconsistências (variações de formato, omissão/duplicação de features, renomeação inconsistente de etapas), o que dificulta a leitura automatizada e a manutenção do estado do projeto. O JSON mitiga essa fricção ao impor campos mais claros e uma organização estável.

No fluxo do projeto VideoMax, o `tracking.json` é gerado diretamente das features definidas no PRD, e não criado manualmente após. A sequência é direta: o PRD Writer compreende o escopo, define as features do ciclo de desenvolvimento e, a partir dessa definição, gera o `tracking.json` inicial. Isso assegura que o acompanhamento esteja sempre alinhado ao escopo real do produto e evita divergências entre planejamento e execução. A skill do PRD Writer também pode ser reaproveitada para gerar apenas o `tracking.json` a partir de um PRD já existente, acelerando a adoção do acompanhamento estruturado mesmo em projetos em andamento.

Finalmente, o `tracking.json` serve como uma fonte objetiva e confiável do que já foi feito, solucionando a questão de que o histórico conversacional de agentes, em sessões longas e com muitas features, nem sempre é uma fonte segura de estado, pois decisões podem ficar ocultas e o contexto pode se degradar.

**Pontos de atenção**

*   **Evitar texto livre para acompanhamento de projeto**: A flexibilidade excessiva do texto livre pode levar a inconsistências (alterações de formato, omissões/duplicações de informação, renomeação de etapas), dificultando a leitura automatizada e a manutenção do estado do projeto.
*   **Garantir o alinhamento entre planejamento e execução**: O `tracking.json` deve ser derivado diretamente das features definidas no PRD pelo PRD Writer. Criá-lo manualmente ou de forma desvinculada do PRD pode causar divergências entre o planejado e o executado.
*   **Limitações do histórico conversacional de agentes**: Em sessões extensas, o histórico de conversas de agentes pode não ser uma fonte confiável de estado do projeto, pois decisões importantes podem se perder, o contexto pode se degradar e a complexidade aumenta com o volume de features.
*   **Adotar formatos estruturados (JSON) para o tracking**: O uso de JSON impõe clareza nos campos, organização estável e previsibilidade, o que é essencial para a leitura por agentes e processos automatizados, reduzindo ambiguidades operacionais.
*   **Expandir a responsabilidade do PRD Writer**: Integrar a produção do artefato de acompanhamento (`tracking.json`) à função do PRD Writer fortalece as fronteiras do processo de desenvolvimento e auxilia na gestão de tarefas paralelas.
*   **Reaproveitar a skill do PRD Writer**: É uma boa prática utilizar a mesma skill para gerar o `tracking.json` a partir de um PRD já existente, o que acelera a adoção do modelo de acompanhamento estruturado em projetos em andamento.
*   **Utilizar o `tracking.json` como fonte objetiva de estado**: Este arquivo serve como um registro factual do progresso, fornecendo uma base sólida para a operação das skills dentro do Harness e superando as incertezas do histórico conversacional.