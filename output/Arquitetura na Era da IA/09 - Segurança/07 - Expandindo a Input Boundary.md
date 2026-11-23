Módulo: Arquitetura na Era da IA\
Aula: [Expandindo a Input Boundary](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18845)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente criou a nossa primeira baseline

00:05

de segurança contra ataques diretos no Knowledge Chat.

00:09

Foram 33 casos diferentes e o sistema resistiu a 28 deles.

00:13

Nos 5 casos que chamamos de Office Task Generation,

00:17

porém, o comportamento foi diferente.

00:21

Quando pedimos para o sistema traduzir uma política,

00:24

criar um anúncio, produzir uma campanha,

00:27

escrever um poema ou compor uma letra usando assuntos presentes na nossa base,

00:33

o Knowledge Chat executou essas tarefas em vez de recusá -las.

00:37

E isso revelou para a gente uma coisa mega interessante.

00:41

O problema ali não era grounding.

00:44

O sistema encontrava documentos reais,

00:47

usava as informações verdadeiras e até retornava fontes válidas.

00:51

O problema ali era outro.

00:54

Ele não tinha uma política clara dizendo quais

00:57

tarefas aquele produto deveria ou não executar.

01:00

Então, nós encontramos uma falha concreta dentro da nossa input boundary.

01:05

Só que... Olhando novamente para o nosso Thread Model,

01:09

existe uma segunda forma de analisar essa mesma boundary. Até agora,

01:13

nós seguimos a ordem natural em que a

01:16

gente construiu o projeto durante a disciplina. Ou seja,

01:19

primeiro a gente construiu o Knowledge Chat com o

01:22

Reg e depois adicionamos o Support Triage Agent.

01:26

Então, por isso, começamos os ataques pelo Knowledge Chat.

01:31

Mas... A segurança não precisa seguir necessariamente

01:36

a ordem em que os componentes foram implementados.

01:39

Se olharmos pelo ponto de vista da confiança,

01:43

tanto o Knowledge Chat quanto o Support Triage Agent, eles possuem algo em comum.

01:49

Os dois recebem conteúdo diretamente controlado pelo usuário.

01:53

Então, a gente pode enxergar a nossa input boundary dessa forma.

01:58

O usuário envia uma mensagem não confiável. A partir dali, existem dois caminhos.

02:03

E um deles é... A mensagem entra no Knowledge Chat,

02:07

influencia o Query Planner, o Retrieval, o Reranking e, finalmente,

02:12

o modelo que produz uma resposta. No outro,

02:15

a mensagem entra no Support Triage Agent, influencia o raciocínio do modelo,

02:20

a escolha de uma ferramenta e os argumentos enviados para essa ferramenta.

02:25

A origem do conteúdo é da mesma categoria.

02:29

O que muda são as capacidades disponíveis depois dela.

02:34

E essa diferença é muito importante.

02:36

No Knowledge Chat, se a entrada conseguir alterar o comportamento do modelo,

02:40

o impacto mais imediato normalmente aparece na resposta.

02:43

Foi exatamente o que a gente viu com o Off-Task Generation.

02:47

A gente conseguiu fazer um produto de perguntas

02:51

e respostas funcionar como o tradutor,

02:53

Copywriter ou gerador de conteúdo. Agora,

02:56

pense no agente. O Support Triage Agent não possui apenas a capacidade de responder.

03:03

Ele pode pesquisar na base de conhecimento,

03:05

ele pode consultar dados atuais de consumo e

03:08

ele pode também criar tickets de suporte. Então,

03:11

Uma entrada maliciosa que altera o comportamento do

03:14

Agente potencialmente não termina em uma frase errada.

03:19

Ela pode alterar... qual a ferramenta, inclusive, é escolhida.

03:23

Ela pode alterar os argumentos daquela ferramenta,

03:26

pode fazer uma operação acontecer quando nenhuma operação deveria acontecer.

03:30

E é por isso que quando a gente faz um Threat Modeling,

03:33

a gente não basta perguntar quem controla uma entrada.

03:39

Também a gente precisa perguntar quais capacidades aquela entrada consegue alcançar.

03:44

Então, compare dois fluxos.

03:46

No primeiro, a gente tem o usuário, o modelo e a resposta.

03:50

No segundo, a gente tem o usuário, o modelo,

03:52

escolha de ferramenta e o efeito no sistema.

03:56

A input boundary continua existindo nos dois casos,

03:59

mas o blast radius não é o mesmo.

04:04

Também nos ajuda a separar dois conceitos que a

04:06

gente vai se aprofundar mais para frente.

04:08

O Prompt Injection trata da manipulação do comportamento

04:12

do modelo através daquilo que ele recebe.

04:15

Excessive Agency trata do impacto que uma decisão

04:20

errada pode produzir porque o modelo recebeu capacidades,

04:25

permissões ou autonomia demais.

04:28

Imagine que um usuário consiga convencer os nossos

04:30

agentes a chamar o Create Support Ticket.

04:33

Quando ele não deveria?

04:35

Manipulação da decisão pode ter começado com prompt injection,

04:39

mas existe uma segunda pergunta.

04:41

Por que aquela decisão foi suficiente para produzir imediatamente uma ação?

04:47

Essa segunda pergunta já começa a entrar no território de agency,

04:52

autorização, policy enforcement. Nós ainda não vamos corrigir isso. Primeiro,

04:58

eu quero fazer exatamente o mesmo que a gente fez com o Knowledge Chat, que é medir.

05:04

Isso também é importante porque a gente não

05:06

deve assumir que o agente será vulnerável.

05:09

Talvez o System Prompt atual resista a vários ataques.

05:12

Talvez a descrição das tools ajude.

05:15

Talvez o modelo se recuse a executar ações indevidas.

05:18

Mas a gente precisa transformar essas suposições em evidência.

05:22

E é aqui que nós temos uma vantagem. No Knowledge Chat,

05:26

muitas vezes a gente precisa avaliar o conteúdo textual da resposta.

05:30

No Agente, a gente consegue observar algo mais objetivo,

05:34

a trajetória. Qual ferramenta foi chamada?

05:37

Qual ferramenta não deveria ter sido chamada?

05:39

Quais argumentos foram usados? Quantos passos aconteceram?

05:43

Um ticket realmente foi criado?

05:45

Nós já construímos toda essa infraestrutura quando

05:49

a gente estudou sobre avaliação de agentes.

05:53

Agora, a gente vai reutilizar essa infraestrutura como uma pergunta diferente.

05:59

Antes a gente perguntava se o agente escolheu

06:01

corretamente as suas ferramentas em situações normais.

06:05

Agora a gente vai perguntar se ele mantém esse

06:07

comportamento quando a entrada tenta manipulá-lo. Então...

06:12

Nossa input boundary passa a ter dois caminhos avaliados separadamente.

06:19

No Knowledge Chat,

06:20

Nossa baseline terminou com 28 de 33 ataques resistidos e os

06:25

cinco casos de off-task generation evidenciaram uma falha de task scope.

06:31

No Support Triage Agent,

06:33

a gente vai criar uma nova suíte adversarial e descobrir o

06:38

que acontece quando uma entrada direta tenta alterar a seleção de tools,

06:44

argumentos e ações.

06:46

Então, não vamos misturar os dois resultados em um único percentual.

06:51

O objetivo não é dizer que a nossa

06:53

aplicação possui uma determinada porcentagem de segurança.

06:57

A gente quer entender cada Attack Path. Então, na próxima aula,

07:02

a gente vai criar essa baseline para o Support Triage Agent,

07:05

verificar se a mesma input boundary conseguiu alterar a tarefa no Knowledge Chat.

07:12

Também a gente consegue atravessar, inclusive,

07:17

o modelo e chegar até a ferramenta e também ver os efeitos reais ali nesse agente.

07:23

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]