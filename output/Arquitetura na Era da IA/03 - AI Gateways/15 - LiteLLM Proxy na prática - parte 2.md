Módulo: Arquitetura na Era da IA\
Aula: [LiteLLM Proxy na prática - parte 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18326)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior,

00:02

a gente estava falando sobre a utilização do proxy com o LiteLLM.

00:08

Então, nesse caso aqui, somente para a gente olhar, o que eu fiz?

00:13

Eu criei uma variável aqui chamada Developer Assistant,

00:16

e se você olhar, o nome dessa variável aqui,

00:20

ela está sendo considerada o nome do meu modelo. Então,

00:23

ao invés de eu passar aqui GPT /...

00:28

OpenAI / GPT 4.1 mini, etc.,

00:31

eu estou passando esse cara, porém, no meu proxy,

00:36

eu estou dizendo que esse cara utiliza esse modelo.

00:40

É basicamente isso que está acontecendo aqui.

00:43

E aí a gente tem um padrão, né?

00:44

O que é uma AI Gateway e por que ela é importante nas aplicações como IA?

00:48

Então, a minha pergunta principal e o System Prompt que eu já tinha.

00:53

E agora, galera, que é a parte que vem interessante no meio da história,

00:57

tá? Porque aqui é onde eu vou fazer a chamada. Então,

01:00

se você perceber, eu estou instanciando diretamente o SDK da OpenAI,

01:04

tá? Mas, se você olhar, eu estou passando a base URL, ou seja,

01:10

fazendo uma substituição da URL padrão da OpenAI e chamando o quê?

01:15

O meu proxy,

01:17

tá? E, ao invés de eu passar aqui, aqui da OpenAI...

01:22

eu estou passando aqui do meu proxy. Se você for olhar o meu .env aqui,

01:26

o que acontece?

01:28

Você vai ter a minha key aqui da OpenAI e

01:31

você vai ter a key do meu Lite LLM Master, tá?

01:37

Então, eu tive uma sorte aqui, inclusive,

01:38

que vocês não conseguiram ver completamente a minha API aqui da OpenAI, mas tudo bem.

01:45

Então, o que acontece? Quando eu estou aqui, eu vou fazer a chamada para o proxy.

01:50

O proxy vai pegar a minha questão aqui,

01:52

juntar com a minha pergunta principal,

01:56

e aí eu vou fazer a própria assinatura comum da OpenAI,

02:01

que é o chat, completions create, system prompt,

02:05

a pergunta, e aí eu tenho o resultado,

02:07

o modelo, a pergunta e a resposta. Então,

02:10

vamos executar esse cara aqui para a gente ver.

02:13

Então, vamos lá, pythonman.py, deixa ele executar, e

02:22

maravilha. Então, se você olhar agora, o model que está aqui para mim é o Assistant.

02:27

E antes, quando a gente olhou a utilização com o OpenAI,

02:32

o model tinha que ser aqui o modelo da OpenAI.

02:35

Então, a gente não precisa mais. Então, eu tenho o model, a pergunta padrão.

02:39

Se eu passasse entre aspas, ele traria a pergunta que eu quisesse.

02:43

E aqui está a resposta que ele acabou trazendo.

02:46

Então, entenda que a minha aplicação não tem

02:48

ideia de qual modelo está sendo chamado.

02:51

O que ela sabe é que o modelo que está disponível para ela é esse Developer

02:56

Assistant e ela confia que esse Developer Assistant vai

02:59

ser o melhor modelo para ela naquele momento.

03:01

Fechou? No próximo vídeo a gente vai avançar e vamos para um próximo passo,

03:06

ele é bem sutil, mas a gente vai começar a ver como essas coisas começam a evoluir.

## Resumo IA

[RESUMO_IA]