Módulo: Arquitetura na Era da IA\
Aula: [Streaming e latência percebida](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18313)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem? No vídeo anterior a gente falou sobre chamadas síncronas.

00:05

A ideia era entender que elas ainda fazem sentido quando a tarefa é pequena,

00:11

objetiva, e a resposta precisa ali voltar na hora.

00:14

Mas também a gente viu que, conforme a resposta começa a ficar mais longa,

00:19

ou a experiência começa a ficar mais travada,

00:21

talvez esse fluxo não seja o melhor caminho.

00:24

Agora a gente entra em um segundo formato que é o streaming.

00:28

Quando a gente fala em streaming com a IA,

00:30

Muita gente associa imediatamente com o chat.

00:33

E realmente o chat é um exemplo bem comum.

00:37

Mas o grande ponto aqui, no final das contas do chat, é que você faz uma pergunta,

00:42

o modelo começa a responder aos poucos e o texto vai aparecendo na tela.

00:46

Só que, arquiteturalmente,

00:48

o ponto mais importante não é o chat nesse caso em si.

00:52

O ponto é que a aplicação não precisa esperar a resposta completa,

00:58

para começar a entregar alguma coisa para o usuário. Isso muda bastante a percepção.

01:03

Imagine que a IA vai gerar uma explicação sobre um ticket de suporte.

01:07

Se a aplicação esperar a IA terminar tudo,

01:09

o usuário fica parado olhando para uma tela carregando.

01:12

Agora, se a resposta começa com algo,

01:15

analisando o problema e logo depois já aparece o

01:18

ticket parece estar relacionado com a cobrança,

01:21

a sensação muda. O usuário entende que alguma coisa já está acontecendo.

01:27

E aqui tem um detalhe importante.

01:29

Streaming não significa necessariamente que o processamento total ficou menor.

01:36

Muitas vezes o tempo total pode ser praticamente o mesmo.

01:40

O que muda é o tempo até o usuário ver a primeira parte da resposta.

01:46

E esse é um conceito importante quando a gente fala em experiência com IA.

01:50

Uma coisa é o tempo total para terminar tudo,

01:57

retorno visível. Em várias features com IA, esse primeiro retorno,

02:02

ele já reduz bastante a sensação de espera.

02:05

Então, no nosso exemplo de tickets, a gente poderia ter um endpoint como um POST,

02:10

sei lá, /tickets, /explain. A aplicação recebe a mensagem do usuário,

02:16

chama IA com o streaming e começa a

02:19

devolver pedaços da explicação conforme eles vão sendo gerados. Na prática,

02:24

isso funciona muito bem. Quando a saída é texto,

02:28

é uma explicação, ou, por exemplo, tem uma recomendação, um resumo,

02:34

ou qualquer tipo de análise que faz sentido ser consumida ali progressivamente.

02:40

O usuário não precisa esperar a frase final para

02:43

começar a entender o caminho da resposta.

02:46

Mas o streaming também não serve para tudo.

02:49

Se a sua aplicação receber, sei lá, um JSON final...

02:53

E para validar aquele JSON e só depois poder tomar uma decisão importante,

02:59

talvez o streaming não vá ajudar tanto.

03:02

Por exemplo, se a IA precisa devolver uma estrutura com categoria,

03:05

prioridade, riscos, campos obrigatórios,

03:08

pode ser que você precise esperar a resposta

03:10

completa antes de confiar naquele resultado. Nesse caso,

03:15

mostrar os pedaços no meio do caminho pode até atrapalhar,

03:19

afinal, um JSON parcial não tem muito valor para o usuário final. E pior,

03:23

Ele pode dar até a impressão que a aplicação já tem uma resposta confiável, quando,

03:28

na verdade, ainda a gente está, vamos dizer assim,

03:32

montando algo que precisa ser validado.

03:35

Então, a decisão aqui não é simplesmente streaming é melhor. A decisão é,

03:40

essa resposta pode ser útil enquanto ela está sendo construída?

03:45

Se a resposta for uma explicação,

03:47

normalmente sim. Se for uma conversa, normalmente sim.

03:50

Se for um relatório textual, o usuário pode acompanhar?

03:54

Talvez sim. Agora, se for uma decisão estruturada,

03:57

que precisa ser validada, principalmente antes, talvez não.

04:01

Um outro ponto é que streaming muda um pouco a

04:04

responsabilidade do back-end e do front-end.

04:07

O back-end precisa conseguir enviar a resposta em partes.

04:11

O front-end precisa exibir essas partes de forma clara.

04:15

E a aplicação precisa lidar... com falhas no meio do caminho,

04:19

porque pode acontecer de a resposta começar e depois quebrar.

04:25

Então, o streaming melhora a percepção,

04:28

mas também exige um cuidado no desenho do fluxo.

04:32

A pergunta prática para esse tipo de decisão é simples.

04:34

O usuário ganha alguma coisa vendo a resposta aos poucos?

04:38

Se sim, o streaming pode melhorar bastante a experiência.

04:40

Se não, talvez seja melhor continuar com uma resposta completa ou...

04:44

a partir de um outro formato.

04:46

E é justamente esse outro formato que a gente vai ver,

04:49

porque tem casos que nem síncrono e nem streaming acabam resolvendo bem.

04:54

Aí a chamada começa a aparecer muito mais num formato de um job,

04:58

algo assíncrono, para que a resposta, de forma geral,

05:02

ela não vai ser imediata e o usuário... vai ter que esperar de alguma outra forma,

05:08

utilizando alguma outra estratégia. Isso já acontece bastante nos dias de hoje,

05:12

mas é uma outra situação que a gente tem que agora trabalhar com IA.

05:17

A IA também entra nesse tipo de categorização,

05:22

vamos dizer assim, nesse tipo de problema.

05:24

Esse problema começa a aparecer. Beleza? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]