Módulo: Arquitetura na Era da IA\
Aula: [Cache com fingerprint](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18344)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, e agora a gente vai começar a trabalhar com um

00:05

conceito que as coisas agora começam a mudar,

00:09

que é o conceito de fingerprint.

00:11

Ou seja, hoje,

00:13

quando a gente estava trabalhando com a parte da chave do nosso cache,

00:18

nós estávamos pegando o quê? O texto normalizado. E nesse texto normalizado,

00:23

a gente usava um hash para ele ali ser a nossa chave do nosso cache. Porém, novamente,

00:28

toda vez que eu estou trabalhando com a IA,

00:31

eu não posso partir do princípio que porque a pergunta é igual,

00:34

porque bateu no meu cache, aquilo realmente é válido,

00:37

porque eventualmente eu estou num contexto diferente.

00:40

Às vezes o prompt mudou, as regras que eu tenho na minha aplicação,

00:44

elas mudaram. O modelo que eu estou trabalhando, ele mudou, por exemplo. Então,

00:48

o que eu fiz aqui? Eu tenho um runtime config, ou seja, por que é runtime?

00:53

Toda hora que a minha aplicação sobe, essas informações vão subir junto. Então,

00:59

eu estou colocando aqui o prompt é v1, as rules são v1, e o nome do meu fast,

01:03

a capacidade do modelo que eu estou usando, é o fastmod, por exemplo. Então,

01:08

eu poderia colocar qualquer nome de modelo,

01:10

ou a versão do modelo, ou qualquer coisa desse tipo.

01:13

E aqui, basicamente, eu continuo na mesma.

01:15

Eu tenho a minha análise de ticket, o ticket request,

01:18

mas olha só agora. Eu tenho mais dois modelos aqui para mim. Eu tenho um,

01:24

que é o fingerprint, e se você perceber,

01:27

o que tem no fingerprint? A versão do meu prompt,

01:30

as regras que eu tenho, as versões das regras da minha aplicação,

01:34

a capability do meu modelo e o texto normalizado.

01:38

Porque vai ser baseado nesse cara aqui que eu vou conseguir gerar o hash.

01:42

E aqui eu tenho a informação do meu cache, que é se teve um hit,

01:47

qual foi a key que bateu, e qual foi o ID ali do fingerprint que a gente tem. Então,

01:54

vamos ali para ficar um pouco mais simples ainda de a gente entender.

01:58

Uma outra coisa que eu tenho aqui no modelo foi um config update,

02:02

porque eu quero poder mudar em tempo de execução a versão...

02:06

do meu prompt, das minhas rules, etc. Para quê?

02:11

Para que eu não tenha que reiniciar o meu servidor para fazer essa alteração,

02:15

porque se eu reiniciar,

02:16

eu vou perder tudo que está na memória,

02:18

porque até agora a gente está trabalhando com cache totalmente em memória.

02:21

Então, antes eu tinha aqui o normalize text e eu tinha o build fingerprint.

02:27

Agora, e o build cache key?

02:30

O que acontece agora nesse momento é que esse

02:32

build cache key que a gente sempre utilizou,

02:35

ele vai fazer uma coisa antes, tá? Ele vai pegar a nossa fingerprint.

02:41

E o que é a fingerprint, no final das contas?

02:43

É o nosso model com todas as versões do prompt com a mensagem do cara.

02:48

E agora, então, eu tenho, na realidade, um hash diferente.

02:52

Ao invés de eu ter o hash que era baseado no nome da pergunta,

02:57

da mensagem que era enviada,

02:58

o meu hash agora é um conjunto... de informações aqui,

03:03

e esse hash eu chamo de fingerprint.

03:05

É um fingerprint porque ele é único e ele existe somente dentro daquele contexto.

03:11

Se uma dessas variáveis acabar mudando,

03:14

Esse hash muda completamente aqui para mim. Eu tenho meu log block e etc.,

03:19

Como eu tinha antes. E agora, o que eu tenho aqui?

03:24

Eu tenho um novo endpoint chamado /barra/config para eu ver as minhas configurações.

03:29

E eu tenho aqui um PUT para eu fazer uma alteração no meu config.

03:33

E aqui, esse PUT é o que eu posso mudar no final das contas.

03:37

Eu posso mudar o prompt version, as rules e o meu model capability.

03:41

Ou seja, eu consigo mudar,

03:43

Vamos imaginar que eu estou na minha aplicação, eu mudo o meu prompt. Opa,

03:46

Então, significa que quando eu for chamar IA,

03:49

Talvez o meu fingerprint agora seja diferente.

03:51

Então agora, o que acontece?

03:54

Quando eu estou dentro da minha aplicação, eu tenho aqui o meu fingerprint. Então,

03:58

Eu peguei a mensagem, gerei meu fingerprint, e agora que eu tenho meu fingerprint,

04:03

Eu gero a minha chave do meu cache baseada nesse fingerprint. E agora, basicamente,

04:09

O que acontece é exatamente o que a gente já fez.

04:11

Se essa aqui estiver no nosso cache, o que vai acontecer?

04:16

Ele vai pegar os dados e vai ser um cache hit.

04:19

Caso ele não encontre, o que ele vai fazer?

04:21

Ele vai chamar o nosso modelo e vai logar

04:27

Aqui como um cache miss e vai retornar as informações.

04:30

A única coisa, nesse caso aqui,

04:31

Que muda no ticket response é que eu estou trazendo as informações do cache,

04:37

Que ele deu um hit false,

04:38

Trouxe aqui e trouxe qual foi o fingerprint que ele foi utilizado.

04:43

Então, nesse caso, o que acontece aqui para a gente?

04:46

Se eu chegar aqui no meu teste .http,

04:49

Eu vou fazer uma chamada aqui, deixa eu só reiniciar meu servidor de qualquer forma,

04:55

Só para garantir que eu não tenho

04:57

Nada enviesado na memória, então eu vou fazer a minha primeira chamada aqui,

05:02

E beleza, então primeira chamada, deu um cache miss, tenho dúvidas sobre cobrança,

05:07

A versão do prompt é versão 1, a rules é versão 1,

05:11

A minha capacidade do modelo é Fast Model, aqui está a minha cache key,

05:16

A quantidade de chamadas, a categoria e o tempo que ele demorou para chamar. Agora,

05:21

O que eu vou fazer? Vou fazer uma segunda chamada aqui e pum,

05:24

Bati nessa chamada e agora eu tive um cache hit.

05:28

Porque é tudo a mesma coisa. Prompt, rules, Fast Model e tudo mais.

05:33

Agora, o que eu vou fazer? Eu vou mudar a versão do meu prompt para a versão 2.

05:39

Então, eu vou dar um send e se você olhar agora aqui, o meu prompt version é 2.

05:44

E agora, o que eu vou fazer? Eu vou agora mandar a mesma mensagem.

05:50

Mas com a versão do prompt como 2. Então, vou enviar agora.

05:55

Quando eu enviei... Opa, espera um pouquinho. Aqui para baixo.

06:00

Quando eu enviei, o que acontece? Ele deu um miss.

06:03

Por quê? Porque agora o meu prompt é o V2. E se o meu prompt é o V2,

06:09

Essa minha cache key não é a mesma. Porque o meu fingerprint mudou.

06:13

Não é porque a minha mensagem é igual que esse cache é válido.

06:20

Porque o prompt dele mudou. Se o prompt dele mudou,

06:23

Pode ter mudado uma monte de regra onde talvez, ao invés de ser billing a categoria,

06:29

Pode ser billing special, por exemplo. Então,

06:33

Eu não posso utilizar um cache onde o fingerprint mudou.

06:37

E essa é a grande sacada que eu acho que muita

06:41

gente acaba deixando passar porque fica tentando cachear apenas as nossas respostas.

06:47

Agora eu vou voltar aqui para o... Para a versão 1 do nosso prompt.

06:50

Ou seja, agora o nosso prompt é a versão 1.

06:53

Mudou aqui para o nosso prompt versão 1. Vou fazer a chamada agora.

06:57

E agora você vai ver que eu tive o cache hit. E aqui na versão 1.

07:01

Por quê? Porque essa versão estava cacheada.

07:04

Mas agora como eu estou na versão 1 do meu prompt.

07:09

Eu não vou ter problema porque isso já estava guardado.

07:12

Beleza? Então, essa é a ideia agora que a gente fez.

07:15

A gente trabalhou com fingerprints,

07:17

onde a gente consolida diversas coisas numa única chave para que,

07:22

se uma delas mudar, o nosso cache vai ter que ser refeito.

07:27

A gente vai ter que ter mais uma chamada aí para a IA.

## Resumo IA

[RESUMO_IA]