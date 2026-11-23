Módulo: Arquitetura na Era da IA\
Aula: [Código e Docker Compose](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18756)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? Somente para eu dizer que eu não mostrei o código, né?

00:05

Apesar de você ter acesso a todo esse repositório, eu queria mostrar...

00:11

algumas coisinhas aqui que eu acho que vale a pena simplesmente citar.

00:15

A ideia aqui, de forma geral,

00:17

não é dar uma aula de OpenTelemetry, uma aula de Python e etc.

00:21

Eu acredito que isso aí é o menos importante em relação à parte conceitual,

00:26

em relação à parte de arquitetura.

00:27

Mas é importante eu trazer algumas coisas aqui para você.

00:31

Se você olhar, eu já deixei...

00:33

aqui como padrão, o caminho onde vai ser enviado as informações para o LangFuse,

00:39

o header que ele precisa e a versão que ele pede aqui, que é a versão nesse momento, pelo menos 4.

00:44

O padrão do OpenTelemetry sempre normalmente é um barra V1, barra traces.

00:50

Isso aí já é meio que padrão, se você já trabalhou com OpenTelemetry,

00:54

basicamente é esse o caminho,

00:56

principalmente quando você está trabalhando com algumas outras ferramentas.

01:00

E aqui... que vem a grande questão, né?

01:04

Se você olhar aqui nesse meu caso, deixa eu olhar aqui,

01:08

sete atributos, a gente já tinha tudo isso antes,

01:10

eu tenho o build, a OpenTelemetry exporter, tá? E aqui,

01:15

se você perceber, eu estou pegando os headers, o endpoint,

01:18

e aqui nesse caso, eu fiz basicamente um if em relação.

01:23

Se eu tiver a public key e a secret key, eu estou falando com o meu endpoint,

01:28

ele vai entrar também com o caminho do endpoint do LangFuse e

01:33

eu estou passando um dado de autorização básico com as credenciais e passando,

01:39

adicionando tudo isso aqui no meu header. E daí, acabou.

01:43

E no final das contas, caso ele não passe por esse if e tudo mais...

01:50

eu vou ter essa opção,

01:52

né? Se o header, né, tiver nome somente, né, e ele não vai carregar as credenciais,

01:57

eu boto um none,

01:59

e daí eu sei que no final das contas ele não vai apontar ali para o meu LangFuse,

02:03

e a gente vai trabalhar ali com o nosso Jaeger,

02:07

tá? Então ele manda para uma URL padrão.

02:09

E a parte de credencial aqui do LangFuse,

02:11

basicamente a... É bem simples, no final das contas,

02:15

eu estou dando um encode naquela nossa secret key que a gente tem.

02:19

Então, de forma geral, é isso.

02:21

A Docker Compose, se você acessar aqui,

02:25

o Docker Compose ficou bem grande. O que é o seguinte?

02:29

Nós já temos no Docker Compose, desde o início, o PgVector,

02:32

mas agora eu tenho um Docker Compose extremamente simples,

02:36

nesse caso, que é para o Jaeger. Então, no caso do Jaeger,

02:40

eu tenho a imagem, o nome do container,

02:43

e aqui, só para você saber,

02:45

isso aqui eu gastei um tempinho bobo em cima disso, que...

02:49

Existe um arquivo uiconfig.json no Jaeger. A minha tela, eu uso ela no padrão dark,

02:56

e aí o que acontecia? Aparecia tudo meio bagunçado, é um bug,

02:59

pelo menos nesse momento que existe no Jaeger. Então, no arquivinho de configuração,

03:03

eu coloquei que eu posso configurar para ele fazer um toggle

03:06

de a versão dark e a versão light que tem.

03:10

E é isso a parte do Jaeger.

03:13

Mas o grande ponto aqui é que eu tenho aqui como profiles,

03:15

que é um recurso do Docker Compose,

03:17

que no final das contas... o que ele faz?

03:20

Se eu der um docker compose, --profile jaeger e app -d,

03:26

ele vai subir esse cara sozinho. E por quê?

03:30

Porque eu não quero que quando você teste o sistema,

03:33

obrigatoriamente você tenha que trabalhar com jaeger ou com Langfuse,

03:36

eu não quero que você fique gastando memória no seu container. Aqui já é diferente.

03:41

Nós já temos aqui um profile de observability e

03:44

nesse caso eu tenho aqui o Langfuse Web.

03:47

Se você perceber, esse cara aqui... Ele é grande,

03:50

porque ele tem um monte de variável de ambiente, que são das configurações.

03:54

E aí, o Langfuse, ele já precisa de Redis,

03:57

ele precisa de um local para armazenar as informações.

04:01

Então, eu tenho um Minio aqui,

04:02

que é como se fosse um S3 local aqui na minha máquina.

04:06

Ele precisa do ClickHouse. Então, quando você olha,

04:09

ele precisa de um worker para processar. Então, o Langfuse, ele trabalha...

04:15

de uma forma diferente. Então, se você perceber,

04:17

eu tenho o ClickHouse, eu tenho o Postgres,

04:19

eu tenho o Redis aqui, eu tenho o Menu,

04:23

que é para a parte de Storage dessas informações. Então,

04:27

ele tem um Profile,

04:29

onde você também pode subir nesse formato que eu falei para você. Assim,

04:33

você não precisa necessariamente, toda vez que vai trabalhar com a aplicação,

04:37

ter que subir, na realidade, todas essas stacks.

04:41

Mas, basicamente, a ideia foi essa para trazer como exemplo para você.

04:45

Mas o nosso grande ponto aqui não está no Langfuse,

04:47

não está no LangSmith, não está no Jaeger, no Phoenix, etc. Na realidade,

04:54

a ideia de que nós podemos agora analisar...

04:59

e entender passo a passo o que está acontecendo com a nossa

05:02

aplicação e agora com ferramentas de busca e etc e tudo mais.

05:06

Fechou? Então, vamos seguir, galera.

## Resumo IA

[RESUMO_IA]