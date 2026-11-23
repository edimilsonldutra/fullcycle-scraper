Módulo: Arquitetura na Era da IA\
Aula: [LiteLLM Proxy na prática](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18325)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, e agora a gente chega numa parte interessante,

00:05

né? Sobre a utilização do LiteLLM,

00:08

mas como proxy, né? Nos exemplos que eu mostrei antes,

00:11

basicamente a gente usava o SDK do LiteLLM para que

00:15

nós não precisássemos usar diretamente um SDK específico de cada provider,

00:21

onde geraria um acoplamento um pouco maior,

00:24

certo? Agora, a nossa ideia aqui, ela já é um pouco diferente.

00:28

Por quê? Porque nós vamos ter a nossa aplicação,

00:31

mas ao mesmo tempo nós vamos

00:33

ter o proxy do LiteLLM configurado, tá? Então,

00:40

eu botei esse comentário aqui pra ficar um pouco melhor pra você entender.

00:44

Então, eu vou ter a minha aplicação Python, tá? Que é esse main.py que eu tô.

00:48

Esse cara vai fazer uma chamada pro LiteLLM proxy,

00:52

tá? E o LiteLLM proxy vai fazer a chamada pra OpenAI.

00:58

Mas tem algumas coisas interessantes.

01:00

Para que a aplicação Python consiga chamar o LiteLLM Proxy,

01:04

esses caras aqui precisam estar autenticados. Então,

01:08

da mesma forma que eu tenho uma chave para a minha aplicação falar com a OpenAI,

01:13

eu tenho que ter uma chave para a minha aplicação Python poder falar com o LiteLLM.

01:18

Porque o LiteLLM Proxy aqui, ele funciona como se ele fosse uma espécie de OpenAI,

01:25

aqui nesse momento, tá? Então, o que eu fiz aqui nesse caso?

01:29

Eu tenho um docker-compose.yaml, tá?

01:32

E a ideia é que esse docker-compose, o que ele vai fazer?

01:36

Ele pega uma variável de ambiente, que é openai-key,

01:39

que a gente precisa, e aqui do liteLLM-master-key,

01:43

que vai ser aqui do proxy que a gente vai precisar utilizar, tá?

01:47

E a gente sobe... esse serviço na porta 4000, que é padrão,

01:52

mas eventualmente você pode escolher uma outra porta caso você precise, tá? Então,

01:57

a ideia principal aqui é, um, injetar qual que vai ser a API aqui da OpenAI,

02:03

porque quem vai saber agora os dados daqui da

02:08

OpenAI não vai ser mais a minha aplicação, vai ser o proxy.

02:11

Então, eu estou passando essa chave para esse proxy.

02:14

E também uma outra chave que o meu proxy tem que ter,

02:17

que é a chave dele mesmo,

02:19

que vai servir como autenticação para a minha aplicação conseguir se autenticar.

02:23

Então, essa que é a ideia principal.

02:25

Somente para você saber, eu já deixei, já dei um app no Docker Compose,

02:29

então ele está rodando já na minha porta 4000,

02:32

e eu só queria mostrar algumas coisinhas aqui interessantes para você.

02:36

Em relação ao proxy... É bem simples você configurar,

02:40

tá? Eu tenho um arquivo aqui chamado config.yml e aqui,

02:44

basicamente, eu tenho uma lista de modelos. Nesse momento,

02:48

eu tenho apenas, nesse caso aqui, uma lista, tá? Então,

02:52

se você olhar que interessante é, eu coloco o model name,

02:57

que eu chamei de developer assistant,

03:00

aí eu passo os parâmetros que eu quero. Por exemplo, o LiteLLM Params,

03:04

eu estou dizendo que ele vai utilizar a OpenAI GPT-4.1 Mini para chamar

03:10

o GPT-4.1 Mini e vou passar a chave da OpenAI aqui nesse caso também.

03:17

E por que eu estou dizendo isso? Porque essa configuração é do meu proxy.

03:21

Mas o mais interessante é que eu criei uma espécie de

03:24

Apelido agora aqui no meu proxy chamado Developer Assistant. Então,

03:29

A partir de agora, a minha aplicação... main.py,

03:32

ela não precisa mais saber que eu estou usando o GPT-4.1 mini.

03:38

O que eu sei é que eu tenho um cara chamado Developer Assistant.

03:43

E é em cima desse cara que eu vou me comunicar.

03:46

Como lá no proxy vai ser configurado,

03:49

aí o problema não é meu. É basicamente isso, tá?

03:51

Agora tem alguns aspectos que eu queria deixar mais claro aqui para você,

03:55

que é o seguinte. Se você olhar,

03:57

eu estou importando, tá? O SDK da OpenAI.

04:01

E aqui que pode gerar um pouco de confusão para você, porque eu falei,

04:05

a ideia é a gente não ficar preso à OpenAI.

04:08

Mas na realidade, isso aqui tem um motivo, não é obrigatório.

04:11

O LiteLLM, ele usa a compatibilidade, toda a base de compatibilidade dele,

04:18

baseado no SDK da OpenAI. Então,

04:21

o que eu posso dizer é que o SDK da OpenAI,

04:24

ele é uma camada bem importante, vamos dizer assim, de compatibilidade,

04:29

para o proxy do LightLM. Então, isso significa que,

04:33

na maioria das vezes que você quiser utilizar o proxy do LightLM,

04:37

você pode sim utilizar o SDK diretamente da OpenAI.

04:41

Ah, Wesley, mas se eu for usar o Gemini? Não tem problema.

04:45

Por quê? Porque quando a gente bater no proxy,

04:48

mesmo usando o SDK da OpenAI,

04:50

o proxy vai fazer toda a conversão que ele precisa para chamar o Gemini na hora que a gente precisar,

04:58

ou para chamar o cloud na hora que a gente precisar.

05:01

Eu vou mostrar isso para vocês daqui a pouco. Por outro lado,

05:04

caso eu não queira utilizar por qualquer motivo,

05:08

por exemplo, o SDK da OpenAI,

05:12

eu posso chamar e utilizar diretamente

05:15

o SDK do próprio LiteLLM.

05:20

E aí eu não estou dependendo de SDK de ninguém.

05:23

O grande ponto aí no meio da história é que...

05:27

Se eu chamo diretamente o SDK do LiteLLM,

05:30

a ideia é que qualquer mudança que eu queira fazer,

05:36

mais específica de um modelo ou do outro,

05:38

eu vou ter que fazer mais mudanças nesse código. Então, normalmente,

05:42

o que o pessoal acaba fazendo é utilizar o OpenAI SDK como base,

05:48

independente do modelo.

05:50

Ou, se você quiser, você pode usar o Light LLM chamando.

05:53

E aquelas diferenças entre um modelo e outro, tá? Elas existem. E aí,

05:58

nesse caso, o que normalmente é feito?

06:00

O Light LLM tem algumas configurações que você pode

06:04

dropar alguns parâmetros ou adicionar alguns parâmetros.

06:08

Adicionar parâmetros adicionais foi uma boa ideia, né?

06:10

Mas adicionar alguns parâmetros na chamada para que

06:15

esses parâmetros sejam passados para o modelo correto.

06:18

Mas perceba. Uma vez que você começa a fazer isso,

06:21

você já está entrando naquele mundo de ficar amarrado especificamente a um modelo.

06:28

Então, se eu estou configurando o LightLLM, utilizando o proxy,

06:31

passando dados específicos, sei lá, do cloud,

06:36

Significa que o meu proxy quase que não é um proxy.

06:39

Porque eu estou tendo que configurar coisas específicas do Cloud.

06:43

Obviamente, tá? Que esse proxy a gente pode fazer de uma forma bem configurada,

06:48

que tenha camadas baseadas realmente em modelos mais intencionais e

06:53

camadas mais abstratas que podem utilizar qualquer tipo de modelo,

06:57

Então tudo tem a sua exceção. Mas o importante é você entender essa ideia principal,

07:02

Tá? No próximo vídeo eu vou terminar de olhar esse programa aqui com você,

07:05

A gente vai fazer a execução e depois a gente vai continuar

07:09

e fazer uma progressão até alguns momentos interessantes da utilização desse proxy. Então vamos nessa.

## Resumo IA

[RESUMO_IA]