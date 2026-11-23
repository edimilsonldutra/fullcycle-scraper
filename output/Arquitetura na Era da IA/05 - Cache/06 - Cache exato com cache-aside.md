Módulo: Arquitetura na Era da IA\
Aula: [Cache exato com cache-aside](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18342)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, agora a gente começou a evoluir em relação a isso. No vídeo anterior,

00:06

a gente tinha basicamente porão ali a nossa chamada

00:10

simplesmente para o modelo sem fazer cache algum.

00:12

Agora, basicamente, o que nós temos? É o mesmo programa, porém,

00:19

nós criamos duas coisas importantes aqui. Primeira coisa,

00:23

eu criei uma função chamada normalizeText. O que esse cara faz?

00:27

Ele deixa tudo em letra minúscula e deixa um espaçamento para

00:32

caso você tenha mais de um espaço dentro de uma pergunta,

00:35

dentro de uma mensagem. Ou seja, a ideia é normalizar todo o texto que chega ali.

00:39

E a segunda função que eu tenho aqui é o build cache key.

00:45

Basicamente, o que ele vai fazer?

00:46

Ele vai pegar para a gente esse texto normalizado e vai gerar um hash em cima disso.

00:53

Por quê? Porque sempre que o texto for igual,

00:56

eu garanto que o hash vai ser o mesmo. Ou seja, o hash ali vai ser uma chave. Então,

01:02

quando acontecer isso, no final das contas,

01:05

vai ficar mais fácil para eu conseguir fazer o meu processo simplório,

01:10

simples de cache, tá? Somente para você saber aqui, eu criei um log block aqui,

01:15

é somente para a gente conseguir mostrar os logs de

01:18

uma forma mais agradável aí para todo mundo, tá?

01:21

Então, nesse nosso caso agora, olha. Tem o mesmo esquema,

01:24

fazendo a chamada ali, a cache count,

01:27

mas agora aqui eu tenho o meu cache, tá? E o meu cache em memória,

01:32

ou seja, um dicionário onde entra uma string que vai ser o meu hash,

01:35

certo? E o dicionário,

01:38

no final das contas, que eu vou ter em seguida,

01:40

é o resultado da minha análise ali de ticket,

01:44

tá? Então, qual que é a ideia principal? Eu vou fazer a chamada...

01:49

Eu vou normalizar o texto e eu vou

01:51

construir o meu hash aqui daquela minha pergunta.

01:58

Vou iniciar a minha contagem e vou perguntar o seguinte, olha,

02:02

se aqui que eu tenho agora existe no cache,

02:05

então ele vai falar o seguinte, opa, eu tenho essa versão cacheada,

02:10

então deixa eu pegar o valor do ticket análise que está lá no cache aqui para mim.

02:15

E daí ele inicia a contagem.

02:17

Loga tudo isso para que a gente consiga ver melhor e retorna o resultado.

02:22

Agora, caso isso não aconteça, o que a gente tem?

02:26

Eu vou chamar a IA agora aqui, vou ter o tempo que ela demorou também,

02:32

vou somar um na minha contagem e vou adicionar aquela

02:38

aqui que eu construí lá em cima no meu cache.

02:42

E vou colocar o resultado da minha análise no cache. Então,

02:47

a primeira vez, basicamente, o que eu tenho é,

02:49

se já existe no cache, eu trago do cache. Caso não, eu coloco essa aqui no cache,

02:55

e aqui eu estou logando, de forma geral,

02:58

para a gente ver na tela como é que fica tudo isso aqui.

03:01

E aí, não muda nada em relação ao ticket response. Então, o que eu vou fazer agora?

03:05

Eu vou aqui no meu teste .http,

03:11

e vou fazer aqui a minha chamada. Então, eu vou lá.

03:15

Primeira chamada, tem que chamar a IA,

03:18

porque eu não tenho nada em cache. Então, se você olhar agora,

03:20

cache miss, IA chamada. Então, eu tenho o ticket,

03:24

O texto normal, normalizado, a minha cache key,

03:27

A quantidade de calls para a minha IA,

03:29

A categoria billing e o tempo que ele demorou aqui para executar.

03:33

Agora, se eu chego novamente agora aqui e faço a mesma pergunta, vamos lá.

03:39

Olha só que interessante, eu tenho um cache hit. Ou seja, a resposta bateu no cache,

03:43

A IA não foi chamada, a cache key exatamente a mesma que o anterior,

03:48

Porque a pergunta era exatamente a mesma, a AI calls é 1,

03:52

Porque ele tinha chamado na primeira vez o billing,

03:55

E o tempo praticamente veio 0 milissegundos,

03:57

Porque ele trouxe muito rápido. Beleza? Agora,

04:00

O que acontece? Eu vou chegar agora aqui,

04:02

E eu vou mandar a mesma intenção aqui, tá?

04:07

Mas com espaços aqui em letras maiúsculas e coisas desse tipo. Olha só o que vai acontecer.

04:13

Bati e agora eu tenho ainda o cache hit. Por quê?

04:17

Mesmo que eu tenha tido a pergunta escrita um pouquinho diferente,

04:21

Quando eu normalizei a pergunta,

04:23

Ela acabou vindo igual e eu tenho agora aqui de novo um cache hit.

04:28

Ou seja, eu consegui utilizar o chat.

04:31

Se eu tivesse feito uma mudança, colocasse, por exemplo,

04:34

Um A aqui na frente, o hash,

04:36

Ele muda, né? E aí, ele vai ter que chamar a IA aqui pra gente,

04:41

E daí teve outra chamada aqui pra gente. Então,

04:44

Isso aqui foi a forma mais simples de a gente trabalhar com cache,

04:48

Com IA, mas isso aqui não é nenhuma novidade se você já trabalhou com cache antes,

04:52

Tá? Mas a gente vai avançar e vamos seguindo daqui pra cá.

## Resumo IA

[RESUMO_IA]