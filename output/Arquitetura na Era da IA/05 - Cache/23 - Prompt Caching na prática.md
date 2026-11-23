Módulo: Arquitetura na Era da IA\
Aula: [Prompt Caching na prática](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18359)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, para que a gente consiga ver um pouquinho melhor como

00:04

isso funciona em relação ao cache do provider,

00:07

basicamente eu tenho a mesma aplicação aqui,

00:09

mas a diferença é que meu prompt inicial,

00:12

o system prompt, ele é bem grande. Ou seja,

00:14

eu vou fazer ele passar de 1024 tokens para esse cara poder ser cacheado.

00:19

E o que acontece aqui? Basicamente,

00:22

eu configurei a LLM aqui, ChatGPT OpenAI,

00:25

temperatura zero. Passei aqui uma prompt cache key.

00:29

A OpenAI não tem isso necessariamente como padrão,

00:31

mas qualquer dado que venha por ali,

00:34

ele pode entrar com um parâmetro adicional. E aqui, de forma geral,

00:38

eu estou querendo receber a mensagem de forma crua,

00:43

para que eu tenha as informações que eu receba ali do provider.

00:48

Agora, qual que é o grande ponto aqui? Ele vai fazer a chamada,

00:51

vai ser basicamente tudo igual ao que a gente estava trabalhando.

00:55

Mas aqui eu vou trazer para que você consiga olhar quais são

01:01

as informações que a gente está conseguindo dar o hit no provider,

01:06

quanto de token a gente conseguiu aproveitar e coisas desse tipo.

01:10

Então eu estou em input tokens, output tokens e o cached tokens e o hit.

01:16

Se teve um cache hit nesse caso ali para a gente.

01:20

Então, como é que vai funcionar no final das contas tudo isso?

01:24

Eu vou executar aqui. Então, eu tenho um provider cache .http.

01:29

E aqui em cima, eu vou dar um send request. Então,

01:33

vamos lá. Mandei o send request. Ele vai mandar. E olha só.

01:38

Tenho dúvidas sobre cobrança e etc.

01:41

Input tokens 1265. Cache read.

01:44

Zero, o prefixo ainda não estava no cache provider.

01:48

Output tokens 40, ou seja, ele teve 40 na saída gerada. Result, o billing,

01:54

confiança de 0.95, ok? E o tempo que ele demorou aqui para trazer o resultado.

02:01

Beleza? Agora, o que eu vou fazer? Eu vou aqui e vou executar uma chamada,

02:08

mas com uma mensagem diferente. Perceba que a mensagem é diferente.

02:11

Uma era, eu tenho dúvidas, outra eu não consigo acessar a minha conta.

02:14

Vou enviar esse request. Olha agora o que acontece aqui para mim.

02:19

Provider cache hit. OpenAI reaproveitou o prefixo. Então,

02:23

não consigo acessar a minha conta.

02:25

Eu tive 1256 input tokens, cache read 1152. Ou seja,

02:31

92% do input eu tive desconto.

02:35

E o output token é 31, account e etc.

02:39

E olha o tempo que ele demorou para retornar aqui para mim.

02:41

822 milissegundos contra... 1 segundo e 421.

02:47

Ou seja, basicamente,

02:49

foi muito mais rápido em relação a tudo isso. E aqui,

02:53

eu posso continuar fazendo. Por que isso, de forma geral,

02:57

faz com que a chamada seja muito mais rápida, de forma geral?

03:02

Porque, simplesmente, ele está reaproveitando aquele system prompt inicial.

03:10

Mesmo que a minha pergunta esteja mudando...

03:13

A parte variável dela é no final. O início, o meu System Prompt,

03:19

ele é igual todas as vezes. Aí nesse momento,

03:21

a OpenAI começa a fazer essa utilização.

03:27

Eu vou dar um exemplo aqui para você. Vou reiniciar aqui a minha aplicação.

03:34

Antes de reiniciar a minha aplicação, eu quero ir aqui no meu System Prompt.

03:41

E no meu System Prompt, eu vou mudar aqui o início dele.

03:44

Vou colocar assim, você traço.

03:47

Ou seja, você concorda comigo que a partir de agora...

03:51

Não sei o que eu abri outra janela aqui sem querer.

03:54

Eu não sei se você concorda comigo, mas a partir de agora...

03:57

Deixa eu fechar esse cara aqui.

04:01

Eu não sei se você concorda comigo, mas a partir de agora,

04:05

Aquele... Eu tenho que dar um VNV de novo aqui. Vamos lá. Vamos lá.

04:13

Então, vamos lá. A partir de agora,

04:15

Se eu executar esse cara novamente, olha só, ele

04:24

deu zero de cache read novamente. Por quê? Porque eu mudei o início do meu prompt.

04:31

Como o meu prompt inicial era diferente,

04:34

ele não conseguiu reaproveitar absolutamente nada ali do meu cache.

04:40

Se eu chegar agora aqui no meu provider cache,

04:42

e eu vou tentar mudar aqui um pouquinho mais para o final,

04:45

nessa parte de confiança, eu vou colocar... e vou colocar um exclamação,

04:50

deixa eu rodar esse cara agora aqui novamente.

04:56

Vamos ver. Vou rodar.

05:00

Ele deu zero aqui de cache read. Ou seja, eu invalidei esse cara novamente.

05:06

Então, eu não sei se você conseguiu perceber,

05:08

mas que a grande sacada aqui é a OpenAI, nesse caso,

05:13

ela faz esse processo automaticamente, tá? Se você for trabalhar...

05:17

com Gemini, tá? Se você for trabalhar com Anthropic,

05:20

cada um trabalha de uma forma diferente, tá?

05:23

O Gemini você consegue falar que esse conteúdo é cacheável,

05:26

depois você consegue pegar o ID daquele cara e atribuir à sua mensagem.

05:31

O da Anthropic, ele trabalha diferente,

05:34

mais com os blocos que você coloca um cache control,

05:37

mas a questão aqui é que eu queria que

05:40

você entendesse que eu consigo combinar o provider cache com o meu cache local,

05:46

com o meu cache semântico e tudo isso trabalhando em conjunto.

05:49

E tudo é cache.

05:51

O grande ponto de tudo isso é como que eu olho para isso.

05:56

Então, eu tenho o cache da aplicação.

05:58

onde eu consigo ter a minha parte de cache e memória,

06:01

o banco de dados na parte semântica, eu posso ter o cache,

06:05

inclusive, no proxy, e eu tenho o cache também no provider,

06:08

e, eventualmente, o meu próprio framework,

06:11

eu consigo também fazer com que ele cacheie algumas coisas para mim,

06:14

para eu não ter que ficar fazendo muita coisa manual.

06:17

Então, tudo é cache, mas com prismas completamente diferentes.

06:22

E eu acho que o grande aprendizado está nesse...

06:26

nesse módulo que a gente falou sobre cache é que a

06:29

gente não pode colocar cache com IA dentro de tudo do mesmo saco, ok? Ou seja,

06:36

a gente tem formas diferentes de trabalhar com objetivos diferentes e

06:40

todos eles podem ser utilizados em conjunto na maioria das vezes.

06:45

O importante é você ter noção do que é possível e do que não é

06:49

possível fazer e principalmente que você entenda

06:53

Quando e como você deve utilizar determinada estratégia.

06:59

Fechou? Era isso aí, galera, que eu queria passar.

07:02

Um grande abraço aí para vocês e até a próxima.

## Resumo IA

[RESUMO_IA]