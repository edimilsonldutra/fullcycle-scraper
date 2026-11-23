Módulo: Arquitetura na Era da IA\
Aula: [Fallback técnico](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18328)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, e agora a gente vai começando a entrar num ponto onde

00:05

a gente acaba falando um pouco mais sobre resiliência,

00:08

vamos dizer assim, ou vamos dizer assim, fallbacks.

00:11

Então, o que acontece muitas vezes? E é comum,

00:14

e eu acredito que se você for desenvolvedor já deve ter acontecido com você,

00:17

que é o seguinte, quando nós,

00:19

às vezes, chamamos uma API, pode ser que essa API esteja fora do ar.

00:25

O sistema esteja fora do ar e você vai receber um erro no meio dessa história.

00:30

E o mesmo pode acontecer com um modelo. Às vezes eu posso, sei lá,

00:35

chamar o GPT modelo tal naquele momento e aquilo está fora do ar.

00:40

Mas o meu cliente não está nem aí se o

00:42

modelo que eu estou utilizando está fora do ar.

00:45

Então, o que eu posso ter? Eu posso ter algo que a gente chama de fallback técnico.

00:49

O que isso significa? Significa que quando eu chamar um modelo e esse modelo,

00:55

por algumas tentativas, eu não conseguir fazer a chamada dele,

01:00

Ele vai fazer o fallback,

01:01

ou seja, ele vai chamar um outro modelo reserva.

01:03

É como se fosse um modelo de backup. Ou seja,

01:07

não deu certo essa chamada desse cara,

01:09

eu vou chamar um outro modelo de backup

01:11

para substituir esse que eu estou trabalhando.

01:14

Então, nesse caso aqui, o que acontece? Eu tenho o meu config do meu LightLLM,

01:20

mas agora as coisas mudaram um pouco. O que acontece?

01:26

Eu tenho aqui o meu modelo normal,

01:28

que a gente tinha desde o início, o Developer Assistant,

01:31

com GPT-4.1 Mini, e que é a minha chave da OpenAI.

01:35

Agora, eu tenho um outro modelo, que eu chamei de Developer Assistant Backup,

01:41

e esse cara aqui está utilizando o Cloud SoneT 4.6 aqui nesse caso.

01:47

Já é um modelo antigo, mas beleza.

01:49

Usando a chave da Anthropic. Até aqui, não mudou nada.

01:53

Do que a gente fez no vídeo anterior,

01:55

a não ser que antes era Architecture Assistant, alguma coisa desse tipo,

02:00

e agora os nomes estão meio parecidos,

02:02

mas eles fazem sentido, porque esse é o principal,

02:05

e esse aqui é o backup, ou seja, quando der algum problema com esse cara aqui,

02:10

o que vai acontecer, a gente vai chamar esse cara aqui como fallback.

02:14

E daí como que isso funciona? Eu tenho as minhas configurações,

02:17

então significa assim, eu vou...

02:20

chamar o LLMSettings aqui, estou falando de fallbacks,

02:23

e eu estou falando que o Developer Assistant,

02:25

ele vai ter aqui o Developer Assistant Backup,

02:30

no meio dessa história. E aí, quando isso acontecer,

02:34

ao invés de chamar um modelo, ele vai... tá, chamando o outro,

02:39

mas eu como desenvolvedor aqui no meu main.py,

02:42

eu não tenho a menor ideia do que tá acontecendo por trás de toda aquela história,

02:49

tá? Como que eu consigo saber disso aqui?

02:52

Deixa eu rodar de novo o Docker Compose Down,

02:55

poderia dar um restart, mas deixa eu reconstruir esse cara aqui,

02:59

vai, não custa nada, tô gravando, então vamos lá,

03:02

app -d, eu podia dar um restart também, mas beleza.

03:06

Então, o que acontece? Como que eu consigo testar isso em primeira mão? Então,

03:11

a primeira coisa que eu vou fazer é eu vou dar um Python main.py e vou chamar,

03:16

e ele vai chamar o modelo principal.

03:18

E está dando problema porque ele ainda, provavelmente,

03:24

na minha variável de ambiente, está aquele modelo antigo.

03:27

Então, eu preciso do meu Developer Assistant, que é o modelo que eu criei aqui.

03:35

Então, vou colocar meu Developer Assistant como estava antes,

03:38

porque senão não vai funcionar.

03:41

Ele não achou o modelo, ele estava com aquele modelo,

03:43

não existe mais o Architecture Advisor.

03:45

Então, vamos lá, agora vai.

03:48

Vou rodar. E agora, o que vai acontecer é que, em primeira mão,

03:52

provavelmente, nesse momento, ele está chamando o meu GPT 4.1 Win.

03:58

Agora, o que acontece?

03:59

Como que eu consigo saber que tem um fallback aí no meio dessa história?

04:04

Eu posso fazer o seguinte.

04:06

Perceba que o modelo é Developer Assistant. O que eu vou fazer agora aqui é,

04:10

eu vou mudar a variável de ambiente do OpenAI Key,

04:15

ou seja, colocando um A aqui no meio, ou seja, essa aqui é inválida.

04:19

Ou seja, se eu tentar nesse momento chamar a OpenAI diretamente,

04:25

o que vai acontecer no meio dessa história? A gente vai ter um erro,

04:29

óbvio. A minha API Key está errada. Mas, em tese,

04:33

a minha aplicação deveria falhar, porque eu estou com uma key errada,

04:37

mas eu tenho um fallback. Então, o que vai acontecer nesse momento?

04:40

Eu vou chamar o meu proxy e o meu proxy vai ver que a minha

04:47

OpenAI Key está inválida ou que eu não estou conseguindo me comunicar com a OpenAI.

04:51

E nesse caso, o que ele fez por padrão? Chamou por baixo dos panos o Cloud Sonnet,

04:57

que é o que a gente tinha configurado.

05:00

Por que aqui está aparecendo Developer Assistant

05:03

ainda e não Developer Assistant Backup?

05:06

Porque a minha aplicação não sabe que eu tenho um backup e ela nem precisa saber.

05:12

Quem sabe e quem configura o backup é o

05:16

meu próprio proxy aqui no meio dessa história.

05:19

Então, por isso que aqui eu começo a ter um pouco mais de redundância.

05:23

As coisas começam a ficar um pouco melhor aqui para

05:25

mim porque eu tenho mais segurança de dar...

05:30

essas informações.

05:31

E aí a gente começa a entrar em um aspecto que é um pouco complexo,

05:38

tá, galera? Por quê? Porque na prática, isso aqui,

05:42

do jeito que a gente colocou aqui, funciona uma maravilha.

05:45

Mas nós temos um problema e é isso que eu quero que você coloque em mente,

05:49

tá? Não é porque eu tenho um fallback, é que esse fallback,

05:53

ele é aceitável. Como assim?

05:56

Uma vez que agora ele não chamou a OpenAI e ele chamou, por exemplo,

06:01

a Anthropic,

06:02

pode ser que a resposta ou a qualidade da

06:06

resposta ou o comportamento desses caras não sejam iguais.

06:12

Então não adianta ter um fallback apenas e fazer com que esse

06:16

fallback chame um modelo que não vai resolver o problema que está acontecendo.

06:22

E aí a coisa começa a ficar um pouco... pior aqui no meio dessa história.

06:27

Mas vamos avançar com isso,

06:28

Eu acredito que você entendeu a ideia até aqui. Vamos nessa.

## Resumo IA

[RESUMO_IA]