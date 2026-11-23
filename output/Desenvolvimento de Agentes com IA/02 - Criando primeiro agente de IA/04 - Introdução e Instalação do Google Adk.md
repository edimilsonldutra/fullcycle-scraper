Módulo: Desenvolvimento de Agentes com IA\
Aula: [Introdução e Instalação do Google Adk](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18095)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos fazer a introdução ao Google ADK, ou somente ADK,

00:05

que significa Agent Development Kit,

00:09

ou Kit de Desenvolvimento de Agentes,

00:13

que é o framework mais popular do momento

00:17

para que nós possamos criar os nossos agentes de IA.

00:21

Esse framework foi lançado em 2025.

00:26

E é interessante porque ele não foi criado

00:29

para que fosse disponibilizado exatamente para o mundo inteiro.

00:34

Ele rodou um ano antes na infraestrutura

00:38

internamente da Google até que ele fosse disponibilizado. Então,

00:43

tudo que nós usamos para criar os nossos projetos,

00:47

a Google está utilizando da mesma forma para criar os seus agentes internos.

00:52

Então isso passa uma grande confiabilidade.

00:56

Este site que está em aberto é a documentação oficial da web.

01:03

Nós temos tudo que é necessário para ter as noções básicas.

01:08

Logo aqui de cara nós já vemos que

01:10

existe suporte para várias linguagens de programação, como Python,

01:15

JavaScript, TypeScript, Go, Java e Kotlin.

01:19

Mas a questão é que para Python não tem comparação.

01:25

Sempre esse repositório aqui, que é a base para o Python,

01:29

é o que vai estar mais atualizado,

01:31

que vai ter mais participações, pelo menos no momento.

01:36

Inclusive, a versão que nós vamos utilizar no curso, que é a versão 2,

01:42

ela não está nem documentada para outras stacks ainda.

01:46

Isso está sendo criado. Agora,

01:47

para Python, sim. Então, é exatamente por isso que nós estamos escolhendo Python.

01:53

Então... Esse ponto da versão é relevante

01:56

porque temos o ADK Python versão 1.0,

02:02

ele vai funcionar durante um bom tempo,

02:05

mas o nosso foco é nesta versão 2.

02:09

E aí nós já pensamos em situações que seriam desafios

02:15

para que a gente pudesse desenvolver os nossos agentes utilizando IA.

02:18

É porque se você pega qualquer modelo de inteligência artificial...

02:23

ele não vai ter nenhum treinamento para a versão 2.0 do ADK.

02:28

Eu vou até mostrar isso depois,

02:30

mas o que eu tenho feito é pegar esse

02:35

repositório aqui e acrescentar ele na parte de docs,

02:39

de forma separada, para que a IA pudesse ler.

02:43

E tem também a parte de documentação que está presente aqui.

02:47

É só colocar ADK, vamos

02:52

ter o ADK Docs.

02:57

O que está aqui é a mesma coisa que está aqui no site,

03:01

mas aqui obviamente está para a web.

03:05

Mas no momento nós não temos que nos preocupar,

03:08

que nós não vamos desenvolver utilizando um agente de IA qualquer,

03:12

nós vamos desenvolver tudo do zero,

03:14

mas já são dicas que são muito relevantes.

03:18

No ADK Python temos a versão 2.2.0 como a última versão.

03:25

Então fique ligado no momento que você for fazer alguma instalação,

03:29

porque provavelmente não vai ter ainda uma versão 3 tão cedo.

03:35

Mas uma versão 2.5,

03:39

2.6 pode ter algumas breakchains.

03:42

Nós vamos usar o que há de mais fundamental do ADK,

03:48

mas esses detalhes precisam ser observados.

03:52

Vamos para a IDE.

03:54

Então com o UV eu vou fazer

03:56

um add google-adk com 3 iguais,

04:02

isso aqui é uma anotação para especificar a versão, com 2.2.0.

04:09

Então veja como que é rápido.

04:12

Então agora nós teremos aqui no PyProject a dependência adicionada,

04:17

assim como se fosse em qualquer outro gerenciador de pacotes.

04:21

E ela estará dentro aqui da pasta libs.

04:26

Poderíamos ver aqui o Google ADK

04:31

com todo o código fonte. Já conseguiu acessar tudo,

04:35

inclusive até a IA consegue acessar também, o que é muito bom.

04:38

Dentro da pasta binária,

04:40

toda vez que tiver alguma biblioteca que tenha algum executável a ser adicionado,

04:46

também vai vir para cá.

04:48

Então já temos o executável do ADK e nós

04:51

vamos utilizá-lo bastante durante as aulas.

04:54

Então está tudo certo.

04:56

Podemos até fazer, uma vez que nós estamos com o Virtual Env ativo,

05:03

como esse que está aqui,

05:04

se não estivesse não daria para poder fazer,

05:07

posso editar apenas ADK, vou usar aqui "-help", então

05:13

ele está funcionando corretamente.

05:17

Temos várias opções para poder lidar de forma geral com os agentes,

05:23

nós conseguimos fazer a execução deles, rodar testes.

05:29

Rodar debugs, enfim. Nós vamos construindo, usando isso ao longo do curso. Então,

05:34

está tudo certo. Vamos partir para a criação do nosso agente.

## Resumo IA

[RESUMO_IA]