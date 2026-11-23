Módulo: Arquitetura na Era da IA\
Aula: [Criando o agente simples de triagem](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18801)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, e agora, finalmente, a gente chega para o nosso agente.

00:05

E somente para você saber,

00:07

isso sim é um agente de A, a gente está utilizando o Langchain para fazer isso.

00:11

E nesse caso, somente para você saber, a nossa ideia é o quê?

00:17

Ter um System Prompt, esse cara aí, ele vai nos ajudar muito.

00:22

Para a gente ter o resultado que a gente precisa. Porque no final das contas,

00:26

esse agente é capaz de entender quais as ferramentas que ele tem e baseado

00:31

no System Prompt e no Dockstring de cada ferramenta que ele vai ter acesso,

00:35

ele vai conseguir tomar as ações e trabalhar com a gente. Então aqui está falando,

00:39

você é um agente de suporte de triagem da FCAI Cloud.

00:44

Sempre responde em português,

00:45

use as ferramentas somente quando são precisas e nunca mais,

00:50

e nunca, e também,

00:54

mais questões do que são necessárias, né? E aqui tem...

00:58

Search knowledge agent base, questões sobre documentação,

01:01

planos SLA, billing, suporte ao produto, etc.

01:04

Get current usage. Live usage only. Quota,

01:09

consumo, uso atual, ingestão atual, projeções, excesso, etc.

01:12

E crie um ticket de suporte somente quando tiver claro que ele

01:16

está pedindo para abrir um novo tipo de suporte.

01:19

E aqui nunca escreva a utilização na questão.

01:26

Dá documentação e nunca use perguntas de política nas chamadas de ferramentas.

01:33

Somente retorne os números, tá?

01:35

Em vez de ficar explicando esses tipos de coisa.

01:38

Para abrir o ticket, você precisa de duas coisas.

01:42

A severidade e qual é o problema que está quebrado.

01:45

Quando o usuário fornece para você os dois...

01:48

Abra um chamado P1, o painel está fora do ar. Isso é o suficiente.

01:53

Escreva um sumário sobre o que você acha e etc. e abra.

01:58

Não pergunte por detalhes que o usuário já te deu.

02:03

Pergunte questões de clarificação quando você genuinamente não puder...

02:09

preencher essas duas informações.

02:11

Nunca invente dados de Live Usage Numbers,

02:16

nunca invente dados de Ticket ID,

02:19

todos eles vêm através das ferramentas ou eles não existem.

02:23

Se alguma coisa que for solicitada não tiver nada a ver com o FCAI,

02:28

simplesmente diga que você só pode responder...

02:35

o que você pode. No final das contas, é plainly instead of answers,

02:40

tá? Então basicamente é isso. Se não tiver nada...

02:43

ele só pode responder sobre o que tem sobre o FCAI e a Cloud.

02:47

Basicamente, essa é a ideia desse prompt, galera. Ou seja,

02:50

eu estou falando quais são as ferramentas e falando os detalhes de cada uma,

02:55

né? Então, isso aí é um ponto importante.

02:57

Aqui eu tenho o Support Agent Result, ou seja,

03:00

é aqui a minha classe base que eu vou ter o resultado que o meu agente vai retornar.

03:05

Ou seja, a resposta, se precisa de clarificação sim ou não,

03:09

se um ticket foi criado ou não, o Ticket ID, caso ele tenha sido criado.

03:12

Se a tarefa foi concluída no final das contas e qual é o motivo,

03:16

por que ele fez isso.

03:19

E aqui a gente tem agent to call, o nome, o argumento, agent run debug.

03:23

Porque a gente vai ter debug mode, debug mode que você vai olhar,

03:27

E o agent run aqui é o resultado e o debug aqui para a gente.

03:31

Nós temos aqui a entrada do get agent,

03:34

Ou seja, eu estou criando um novo agente, de forma geral, caso ele já não exista.

03:39

Se você perceber, eu tenho o modelo, o support tools,

03:42

Que são as ferramentas que eu tenho,

03:43

O system prompt e o formato que eu quero,

03:46

Que é exatamente o formato que a gente definiu aqui em cima.

03:51

E agora a gente vai ter extract tool calls,

03:54

Onde a gente vai conseguir pegar do agente,

03:56

Através das chamadas que a gente tem lá do LangChain e tudo mais,

04:01

Quais foram o que foi chamado.

04:03

A gente tem também o Run Support Agent,

04:06

Que na realidade vai fazer a chamada ali no nosso Agent Run.

04:11

E a gente tem a imprimindo,

04:13

Né? Os passos que o agente fez para que a gente consiga entender.

04:17

E normalmente tudo isso vai rodar essa run dentro do nosso debug.

04:21

Uma run, na realidade, no caso aí no LangChain, é algo que pode ser executado.

04:25

Inclusive, nesse caso, uma chamada para um agente. Então,

04:29

A ideia é que quando eu rodar, a gente vai conseguir ver todos esses detalhes.

04:33

Então, no próximo vídeo, a gente continua daí.

## Resumo IA

[RESUMO_IA]