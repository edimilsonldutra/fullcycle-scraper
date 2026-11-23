Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17888)

## Resumo da aula

Uma unidade pequena e verificável é um pedaço de trabalho suficientemente delimitado para que um agente consiga executar e, ao final, seja possível decidir com clareza se aquilo foi concluído ou não. O critério principal não é o tamanho absoluto da tarefa, mas a capacidade de validá-la de forma objetiva. Por isso, “pequena” depende do contexto do projeto, da qualidade da especificação e da capacidade do modelo. Em alguns casos, a unidade pode ser criar uma tabela; em outros, pode ser implementar uma feature inteira de login.

O tamanho adequado da unidade não é fixo e emerge da combinação entre escopo, maturidade do projeto e precisão da especificação. À medida que o modelo melhora e o trabalho fica mais bem descrito, a mesma equipe consegue tratar blocos maiores como unidades ainda controláveis. Isso impede uma decomposição artificialmente minúscula, que aumenta overhead sem melhorar previsibilidade. A medida correta é: o agente consegue executar e o sistema consegue verificar.

Uma unidade útil para Harness Engineering precisa ser atômica no sentido operacional: ou está pronta, ou não está. Esse caráter binário evita zonas cinzentas como “quase feito” ou “parcialmente funcionando”, que dificultam coordenação, retomada e avaliação automática. A verificabilidade exige evidência clara de conclusão e funcionamento, não apenas produção de código. Sem esse fechamento objetivo, o estado do projeto deixa de ser confiável para agentes subsequentes.

Retomando as waves do SDD, a decomposição em blocos menores permite que a conclusão de uma parte libere as próximas dependências de execução. O goal maior continua existindo como direção do projeto, mas o avanço real acontece por unidades que destravam outras unidades. Essa estrutura reduz ambiguidade e organiza a ordem de implementação sem exigir que tudo seja resolvido de uma vez. O harness passa a operar sobre marcos verificáveis, e não sobre intenção genérica.

Um prompt curto pode servir apenas como ponto de partida para gerar uma especificação muito mais detalhada, desde que o processo de expansão preserve clareza suficiente para execução. Retomando o uso de skill em spec-driven development, uma instrução pequena pode ser refinada até descrever exatamente o que cada feature deve fazer. Isso transforma uma intenção inicial compacta em unidades acionáveis por agentes de codificação. O valor não está na brevidade do prompt, mas na qualidade da especificação resultante.

Quando o agente implementa uma feature e registra commits ao longo do processo, cada entrega passa a ter um rastro concreto de execução. Esse rastro ajuda a conectar especificação, implementação e verificação dentro da mesma unidade de trabalho. A unidade pequena e verificável não é apenas uma ideia de planejamento; ela precisa aparecer na prática como algo implementado, versionado e passível de checagem. Em Harness Engineering, isso torna o desenvolvimento mais auditável e mais fácil de coordenar.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente falou sobre estado.

00:05

Agora, como que a gente organiza esse estado de forma geral? Como que eu sei,

00:11

como que o agente consegue determinar se aquilo foi feito ou não? Então,

00:17

a grande ideia aqui é você ter uma unidade pequena e verificável.

00:22

O que isso significa?

00:24

Ao invés de eu ter um sistema inteiro para ser desenvolvido,

00:28

eu vou decompor... esse projeto em pedaços menores.

00:32

Hoje em dia, para quem já está trabalhando com IA, isso já começa a ser mais óbvio.

00:37

O grande ponto é o quão grande é

00:40

esse projeto e o que significa uma unidade pequena.

00:45

Isso você vai descobrir dentro do seu próprio projeto e conforme você vai perceber,

00:51

conforme o modelo vai melhorando,

00:54

conforme você vai deixando as coisas mais especificadas,

00:59

Esse trabalho decomposto, essa unidade pequena,

01:03

eventualmente ela não é uma tarefinha de criar uma tabela no banco,

01:07

mas pode ser, desenvolva uma feature de login.

01:10

E dependendo da situação,

01:12

uma feature de login pode ser algo muito simples ou

01:15

dependendo da situação pode ser algo extremamente complexo.

01:18

Agora o grande ponto é que essa tarefa,

01:21

independente do que você considerar pequeno ou não, ela tem que ser verificável.

01:26

Eu tenho que ter certeza clara que ela está feita e que ela está funcionando.

01:30

E por isso que ela tem que ser atômica. Ou seja,

01:33

ou ela está feita ou ela não está feita. Essa parada tem que ser binária,

01:38

basicamente. Então,

01:40

quais são abordagens que normalmente você pode utilizar?

01:46

Você tem um goal maior. Ou seja,

01:49

você tem basicamente o seu projeto de uma forma maior.

01:53

que é o que a gente fez quando a gente estava falando sobre o SDD,

01:56

e blocos menores, que quando você termina esse bloco,

02:02

você consegue ter a possibilidade de desbloquear os outros.

02:05

Então, eu acho que está muito claro aqui que é o que a

02:08

gente fez no SDD quando a gente tinha aquelas nossas waves.

02:11

Quando eu termino aquela parte,

02:12

as outras partes vão sendo desbloqueadas para eu começar a fazer.

02:16

Um outro ponto importante aqui também é o seguinte.

02:21

Muitas vezes, através de um prompt muito curto,

02:24

a gente consegue expandir para uma especificação extremamente detalhada,

02:28

onde um agente de geração desenvolve cada feature realizando os commits.

02:35

Novamente, se você olhar os capítulos anteriores,

02:40

onde a gente falou sobre spec-driven development,

02:44

a gente vê exatamente isso acontecendo. Um projeto menor,

02:47

com blocos menores, onde a gente vai desbloqueando.

02:51

E a partir de, nesse caso, uma skill,

02:54

onde a gente colocou uma especificação até que pequena,

02:58

a gente foi conseguindo expandir para deixar cada vez mais

03:01

claro aquilo que o agente tem que desenvolver.

03:04

E na hora que um agente gerador, um agente que faz a codificação,

03:08

ele vai fazendo a feature e ele vai realizando os commits.

03:12

Então, isso é uma unidade pequena verificável.

03:14

Se você perceber, a gente já começa a fazer relação com o que a gente viu, mas...

03:20

A gente estava falando ali em SDD puro.

03:23

Conforme a gente vai falando em Hines Engineering,

03:25

isso é uma das formas e princípios que a gente tem que pensar

03:28

em torno da hora que você for desenvolver o seu software.

## Resumo IA

**Abreviações**
*   **SDD**: Spec-Driven Development (Desenvolvimento Orientado por Especificação)
*   **IA**: Inteligência Artificial

**Resumo**
A aula abordou a organização do estado de um projeto de desenvolvimento de software através do conceito de "unidade pequena e verificável". O objetivo é permitir que um agente determine, de forma clara e binária, se um pedaço de trabalho foi concluído. O instrutor enfatizou que o critério principal para essa unidade não é seu tamanho absoluto, mas a capacidade de validá-la objetivamente. O tamanho adequado emerge do contexto do projeto, da maturidade do modelo (como IA) e da precisão das especificações, podendo variar desde a criação de uma tabela até a implementação de uma feature de login completa.

Uma unidade útil para Harness Engineering precisa ser atômica e binária (ou está feita, ou não está), evitando estados ambíguos. A verificabilidade exige evidências claras de conclusão e funcionamento, não apenas a produção de código. O fluxo explicado retoma o modelo de "waves" do SDD (Spec-Driven Development), onde um "goal maior" é decomposto em blocos menores; a conclusão de um bloco desbloqueia as próximas dependências, organizando a implementação e reduzindo a ambiguidade. Um prompt curto pode servir como ponto de partida para gerar uma especificação muito mais detalhada, que será utilizada por agentes de codificação. Esses agentes implementam as features e registram commits, criando um rastro concreto de execução que conecta especificação, implementação e verificação, tornando o desenvolvimento mais auditável e coordenável.

**Pontos de atenção**
*   **Verificabilidade como critério principal**: O que define uma "unidade pequena" é a capacidade de validação objetiva e clara de sua conclusão, e não seu tamanho absoluto.
*   **Atomicidade da unidade**: A unidade de trabalho deve ser atômica e binária (feita ou não feita), evitando zonas cinzentas como "quase feito" ou "parcialmente funcionando", que dificultam a coordenação, a retomada e a avaliação automática.
*   **Evidência clara de funcionamento**: A verificabilidade exige prova concreta de conclusão e funcionamento, não apenas a entrega de código. Sem isso, o estado do projeto não é confiável.
*   **Tamanho da unidade é contextual e evolui**: O tamanho adequado não é fixo; ele emerge da combinação entre escopo, maturidade do projeto e precisão da especificação. Decompor tarefas artificialmente em unidades minúsculas pode aumentar o overhead sem melhorar a previsibilidade.
*   **Prompts como gatilhos para especificações detalhadas**: Um prompt inicial pode ser um ponto de partida para gerar uma especificação muito mais rica e detalhada, essencial para a execução por agentes de codificação. O valor está na qualidade da especificação resultante.
*   **Rastreamento e auditabilidade via commits**: O registro de commits durante o processo de implementação cria um rastro concreto de execução, conectando a especificação, a implementação e a verificação dentro da mesma unidade de trabalho, o que é fundamental em Harness Engineering para auditabilidade e coordenação.