Módulo: Arquitetura na Era da IA\
Aula: [Chando OpenIA com SDK](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18286)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, só para a gente ter algo um pouco mais prático aqui, então o que eu fiz é o seguinte,

00:05

eu tenho um prompt que ele é bem simples,

00:06

Criar um exemplo usando o SDK nativo em Python da OpenAI.

00:10

É um projeto para a gente gerar na nossa aula,

00:13

onde eu vou ter três arquivos, o main.py,

00:15

o requirements.txt para instalar as dependências,

00:18

e um .env.example, vale para não usar frameworks,

00:21

dependência no requirements.txt,

00:23

e trabalhar ali com a dependência da OpenAI e o Python.dev,

00:29

simplesmente para ele carregar a variável de ambiente, tá?

00:31

Então, o que eu estou fazendo aqui é,

00:35

a ideia é ele fazer uma chamada diretamente para o modelo e falar,

00:39

você é um arquiteto que vai responder perguntas sobre AI Gateway.

00:43

Basicamente é isso, tá? Então, um programa bem simples.

00:45

Estou pedindo aqui para o Raico executar aqui para a gente,

00:49

porque ele é mais rápido, né?

00:53

E é uma aplicação simples de forma geral. Então,

00:56

eu vou dar um exemplo, esse cara aqui.

00:59

e vamos ver ele desenvolvendo em tese,

01:02

isso aqui tem que ser rápido aí pra gente, tá? Então vamos nessa.

01:07

Ele falou que vai criar o exemplo em Python, de

01:12

acordo com a especificação, criou

01:17

o .env.example, e

01:22

ponto, e fez ali, tá? Então ele falou, pra usar, faça essa instalação,

01:27

então o que eu vou fazer é o seguinte,

01:29

primeiro eu vou duplicar o .env.example aqui, vou deixar apenas ele no .env,

01:36

para eu colocar a minha variável de ambiente.

01:41

Colei a minha variável de ambiente aqui.

01:43

Só para garantir que você não ia ver a minha variável de ambiente.

01:46

E agora eu vou pedir para ele fazer aqui. Try it out.

01:51

Botei aqui para ele rodar.

01:56

Então ele está executando isso aqui para mim.

01:59

E vamos ver se esse cara aqui funciona. Então ele está instalando as dependências.

02:04

Lendo a minha .env.

02:08

Ativando ali o meu virtualenv.

02:13

E vai executar a aplicação.

02:15

Vamos nessa. Eu acho que o ponto que mais demora, na realidade,

02:18

é a latência da resposta, né? Porque eu acho que esse prompt,

02:22

ele faz com que a resposta possa vir meio que grande no meio da história,

02:26

né? Então vamos ver o que que rola.

02:36

Vamos aguardar.

02:39

Prontinho, funcionou. E aqui ele trouxe o resultado.

02:43

Então ele trouxe que funcionou, né?

02:45

E formatou e etc. Mas eu queria ver o resultado daqui. Então deixa eu.

02:50

Colocar aqui, mas eu vou colocar para ele,

02:54

aqui no prompt que ele usou aqui, produção.

03:01

Responda com dois parágrafos, para

03:06

não demorar muito a nossa resposta. Então, em tese,

03:09

isso aqui vai ter que funcionar, né? Deixa eu dar um source, source

03:18

.vnv

03:22

Bin barra activate, né?

03:27

Aqui para mim, e eu vou dar um Python, um main.py, e

03:32

Vamos executar esse cara aqui e ver se ele funciona. Mas, assim,

03:36

Vai funcionar e não tem muito segredo no meio aqui da história. Então,

03:40

O modelo é esse, a pergunta e eu trouxe a resposta,

03:42

E o resumo da história aqui é que, inclusive, tudo aqui é baseado no quê?

03:49

Nesse trecho, onde eu escolho a quantidade de tokens,

03:53

Eu coloco o chat completion.create,

03:56

E eu estou chamando o meu modelo direto. Então,

03:58

Eu acho que a maioria das pessoas que às vezes acabam trabalhando com IA,

04:01

Acabam fazendo uma implementação parecida com essa. Mas, novamente,

04:06

A gente começa a ter aqueles problemas de acoplamento e agora a gente vai

04:10

Avançar um pouco no próximo vídeo como se eu quisesse mudar o meu provider.

04:15

E aí as coisas começam a ficar um pouquinho diferentes.

04:18

Então, vamos nessa no nosso próximo vídeo.

## Resumo IA

[RESUMO_IA]