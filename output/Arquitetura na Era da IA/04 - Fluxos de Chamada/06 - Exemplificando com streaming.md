Módulo: Arquitetura na Era da IA\
Aula: [Exemplificando com streaming](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18317)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, no vídeo anterior eu mostrei aqui para vocês como que

00:04

a gente faz para trabalhar de forma síncrona,

00:06

ou seja, o feijão com arroz,

00:08

que é o que a gente sempre fez e não tem segredo nenhum.

00:11

Agora a gente vai para a segunda etapa, que é a parte de streaming,

00:14

e isso aí muda bastante aquilo que eu falei em relação à percepção do usuário,

00:19

e assim, não é nem um pouco difícil de forma geral você implementar,

00:24

é algo que vem como padrão, mas isso muda.

00:27

Inclusive como que o seu back-end responde e como

00:30

que o seu front-end vai responder também.

00:32

Nesse nosso caso aqui,

00:33

eu tenho só a implementação do back-end e a parte do front-end barra client,

00:37

eu vou fazer via curl,

00:38

onde a gente consegue ver essa chamada ali para a gente,

00:42

tá? Então, somente para a gente ficar atualizado.

00:47

Se eu for aqui no meu AI client, deixa eu fechar aqui, né?

00:51

Eu tenho antes aqui, né? Eu tenho aqui o meu analyze ticket.

00:55

Que retorna para a gente aquilo que a gente fez.

00:58

Mas agora eu tenho um outro endpoint que é um explain ticket.

01:03

Ou seja, diferente do fluxo síncrono,

01:06

aqui a gente não espera mais a resposta completa.

01:09

A gente vai trabalhar de forma em streaming,

01:13

onde a gente vai receber os pedaços das mensagens de forma geral.

01:17

E se tiver algum problema,

01:18

a gente vai receber ali um erro 500. Então, de forma geral, o que acontece aqui?

01:24

Eu tenho um stream, ou seja, eu faço uma chamada normal aqui para mim,

01:28

ou seja, faço a chamada e se você olhar,

01:31

eu tenho um parâmetro que eu coloco o stream é igual a true.

01:34

Uma vez que eu coloco o stream é igual a true,

01:36

você vai perceber que eu tenho um loop que eu fico aqui, chunk in stream, ou seja,

01:41

eu vou recebendo os pedaços da informação e vou colocando dentro ali de um delta.

01:47

O que é o delta no final das contas ali para mim?

01:49

É a diferença entre o que eu já mandei... e do que eu estou mandando agora.

01:53

Senão ele vai mandar toda a mensagem inteira,

01:57

toda hora. Então o delta só manda a diferença do conteúdo que eu tenho.

02:01

E o que vai acontecer?

02:03

Ele vai mandar isso aqui para esse nosso delta o tempo inteiro.

02:07

O ponto principal disso é que quando eu estou no

02:10

meu main agora aqui e eu tenho esse meu endpoint explain,

02:15

como é que funciona? Eu recebo esses meus chunks.

02:18

Aqui, Explain Ticket,

02:20

e eu tenho aqueles chunks que vão fazendo atualização para mim.

02:23

E aqui, o que acontece?

02:25

Eu tenho um try, então eu verifico se eu tenho o first chunk,

02:30

basicamente, e daí eu vou para o next.

02:33

E aí ele fica, basicamente, fazendo essa tentativa para ver se eu recebi.

02:40

E no final das contas, eu retorno aqui para ele sempre o primeiro que eu recebi,

02:45

para garantir, e depois ele vai... trazendo o resultado.

02:49

E lembrando que aí nesse caso,

02:51

eu tenho aqui o meu return, que é streaming response.

02:54

Aqui para mim, onde eu tenho o body,

02:57

que é essa função aqui onde eu tenho o first chunk e o resultado deles,

03:02

e eu estou retornando nesse caso aqui como text/plain.

03:06

Então basicamente eu tenho um loop.

03:08

E esse loop vai pegar a primeira chamada e depois vai ficar iterando sobre

03:14

o segundo resultado e os próximos resultados que eu tenho aqui no meio da história,

03:18

tá? Ou seja, é um outro endpoint que eu acabei colocando.

03:21

Então, o que eu vou fazer aqui?

03:23

Basicamente, eu vou chamar a aplicação normalmente, tá?

03:27

Mas agora, ao invés de eu usar aquele HTTP client,

03:30

sabe o que eu vou fazer? Eu tenho, acho que,

03:32

um curl pronto aqui. Abri um outro terminal aqui para mim.

03:35

E eu acho que eu tenho aqui, curl.

03:38

E o que esse cara vai fazer aqui se você olhar?

03:43

Isso. Parece que é uma bobeira, mas isso muda completamente o resultado.

03:48

Então eu estou dando um curl menos N,

03:49

que faz com que ele consiga trazer as respostas,

03:53

inclusive de forma parcial. Aqui tem o fui cobrado e estou fazendo a chamada,

03:59

um POST no /explain.

04:01

Quando eu dou enter aqui,

04:03

o que dá para perceber é que o resultado que eu vou recebendo,

04:07

ele vai funcionando que nem o chat que a gente está acostumado. Então,

04:10

eu dou um enter aqui e ele está retornando o tempo.

04:14

E eu coloquei aqui o tempo total também,

04:16

que ele demorou para retornar. Então,

04:19

eu coloquei um tempo total, time_total,

04:22

aqui no curl para me ajudar, somente para a gente ter uma ideia.

04:26

Mas o ponto importante aqui é que a gente viu que eu não precisei...

04:30

Na realidade, esperar tudo para receber o resultado.

04:33

Eu já fui recebendo o resultado conforme a resposta veio chegando ali para mim,

04:40

que foi um pouco mais devagar. Ou seja,

04:42

ele demorou seis segundos agora para responder,

04:44

aquela hora ele demorou um segundo. Então,

04:46

a gente consegue ver que as informações vão chegando ali de forma diferente.

04:51

Fechou? Então, esse é um exemplo básico de streaming e, obviamente,

04:55

independente do SDK... Se você for trabalhar com uma blockchain,

04:59

qualquer coisa desse tipo,

05:01

é o conceito básico.

05:03

Você recebe chunks e vai retornando o resultado desses chunks ali.

05:07

E aí vai depender muito do protocolo que você está trabalhando. Nesse caso,

05:11

eu coloquei aqui que a gente está trabalhando com

05:13

HTTP mesmo e a gente teve esse resultado. Então,

05:16

aqui é o segundo exemplo quando a gente trabalha com streaming.

05:20

O próximo que a gente vai falar é em relação a jobs,

05:24

ou seja, quando a gente vai trabalhar em background. Então, vamos nessa.

## Resumo IA

[RESUMO_IA]