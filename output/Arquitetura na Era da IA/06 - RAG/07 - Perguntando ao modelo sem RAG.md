Módulo: Arquitetura na Era da IA\
Aula: [Perguntando ao modelo sem RAG](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18409)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, e agora, indo devagar passo a passo,

00:04

se você olhar aqui, eu tenho agora um arquivo chamado chat,

00:08

e a ideia do chat é bem simples nesse momento.

00:11

O que a gente vai fazer? Eu tenho um model aqui,

00:14

que é init chat model, que eu estou utilizando o LangChain,

00:17

onde eu falo qual é o meu chat model,

00:21

então se você olhar,

00:22

está nas minhas configurações e também vindo das minhas variáveis de ambiente.

00:26

O meu provider aqui está como OpenAI.

00:29

E aqui está a minha key da OpenAI. Então,

00:32

aqui eu tenho a minha variável model. E aí, aqui embaixo eu coloquei print,

00:36

no reg chat started, this chat does not use an internal knowledge base yet,

00:40

e você pode digitar exit para sair.

00:45

E aqui, no final das contas, o que acontece?

00:48

Eu tenho um while True, onde eu faço uma pergunta,

00:52

e toda vez que eu fizer uma pergunta, o que vai acontecer? Ele vai fazer um stream,

00:59

e jogando essa pergunta aqui no nosso modelo utilizando o LangChain.

01:05

E daí ele vai sempre ficar respondendo num loop.

01:09

Se eu digitar exit ou quit, o que vai acontecer? Ele vai sair do programa.

01:14

Então, basicamente, é um programinha muito simples,

01:17

mas aqui a gente já começa a operar num modelo,

01:20

vamos dizer, de chat. Então, se eu colocar um aqui, python -m app .chat, aqui.

01:28

Aqui eu posso perguntar, qual é

01:33

a capital do Brasil?

01:38

E aí ele respondeu, a capital do Brasil é Brasília. Então, basicamente é isso,

01:43

eu consigo ficar perguntando e ele responde em formato de stream,

01:47

inclusive aqui. Se você perceber, ele saiu completando.

01:50

E se eu der um quit aqui para mim,

01:52

ele vai sair aqui do meu programa. Beleza? Então,

01:55

somente para a gente ir bem passo a passo e ir entendendo

01:58

que nesse momento eu não estou mexendo com nada de RAG.

02:01

Eu posso simplesmente fazer uma pergunta comum e o

02:03

modelo vai trazer as respostas que ele tem treinado.

02:08

Não tem nada a ver com a nossa empresa

02:10

fictícia que está no nosso Knowledge Base ainda.

02:14

Tá bom? Então vamos nessa.

## Resumo IA

[RESUMO_IA]