Módulo: Arquitetura na Era da IA\
Aula: [O que é RAG](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18404)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem? Nesse capítulo a gente vai começar a falar sobre RAG.

00:06

E se você nunca ouviu esse termo,

00:08

não tem problema, porque a ideia aqui é construir o raciocínio do zero.

00:12

Antes de falar o nome técnico,

00:14

vamos pensar em um problema bem comum.

00:16

Imagine que você tem uma aplicação com IA... Pode ser um chat de suporte,

00:19

um assistente interno para funcionários, uma ferramenta para responder dúvidas,

00:24

qualquer coisa, uma base de conhecimento de um produto, por exemplo.

00:28

Agora, o grande ponto é o seguinte, imagine que um usuário pergunta,

00:32

qual é o prazo de reembolso para o plano Enterprise?

00:35

A primeira reação pode ser, bom,

00:37

eu mando essa pergunta para o modelo e ele vai responder.

00:39

Só que a gente tem um problema muito claro.

00:42

O modelo não conhece a regra de negócio especificamente da sua empresa.

00:47

Ela sabe o que é um plano, ela sabe o que é Enterprise,

00:49

mas ela não sabe qual é a política específica da sua empresa.

00:53

E talvez essa regra esteja num documento interno, ela pode estar numa página de FAQ,

00:58

num banco de dados, numa política comercial no Notion. Não interessa.

01:02

O grande ponto é que essa informação existe e ela está fora do modelo.

01:06

O modelo não foi treinado com essa informação.

01:09

E esse é o ponto onde o RAG começa a fazer sentido.

01:13

RAG significa Retrieval Augmented Generation.

01:17

Traduzindo de uma forma simples,

01:18

é uma geração aumentada por recuperação de informação.

01:23

Vamos lá, vamos quebrar isso. Retrieval é a parte de recuperação da informação.

01:28

A aplicação recebe uma pergunta e antes de pedir para o modelo responder,

01:33

ela procura em uma base externa quais os documentos,

01:37

trechos ou informações parecem relevantes para aquela pergunta.

01:42

O augmented significa que a resposta do

01:45

modelo vai ser aumentada com esse contexto externo.

01:49

O modelo não vai responder só com o conhecimento geral que ele tem.

01:53

Ele vai receber informações específicas que a aplicação encontrou.

01:58

E o generation é a parte final onde o modelo gera a resposta para o usuário.

02:03

Então, em vez de a gente simplesmente fazer isso,

02:06

o usuário pergunta, o modelo responde, a gente passa a ter algo mais ou menos assim.

02:11

O usuário pergunta, a aplicação busca o contexto relevante,

02:15

a aplicação monta um prompt com esse contexto e

02:18

o modelo responde com base nesse contexto.

02:22

Essa é a ideia central do RAG.

02:24

O modelo não está aprendendo.

02:27

Aqueles documentos de forma permanente estão sendo montados...

02:33

ali em tempo real na hora que a pergunta,

02:36

entre aspas, foi feita. Então,

02:38

a gente não está fazendo ali um fine tuning do modelo.

02:42

A gente apenas está recuperando as informações no momento da

02:48

pergunta e entregando essas informações para o modelo usar na resposta.

02:52

É como se a aplicação dissesse para o modelo,

02:55

olha, antes de responder...

02:57

Considere esses trechos aqui porque eles são os trechos mais

03:00

relevantes que eu encontrei na nossa base interna.

03:04

E isso muda bastante a arquitetura da aplicação,

03:07

porque agora não basta mais chamar o modelo.

03:09

A aplicação precisa ter uma base de conhecimento,

03:12

precisa preparar essa base.

03:16

E a gente precisa também dividir esses documentos,

03:20

a gente precisa criar uma forma de buscar os trechos certos,

03:23

a gente também precisa selecionar o que vai entrar no

03:27

contexto e também decidir como o modelo deve responder.

03:31

Então o RAG não é simplesmente uma feature, RAG é um pipeline.

03:36

Existe uma parte que acontece antes da pergunta do usuário,

03:39

essa parte prepara os documentos, a gente chama isso de ingestão.

03:44

É onde a aplicação lê os arquivos, extrai conteúdo,

03:47

quebra em pedaços menores,

03:49

guarda os metadados e indexa essas informações para a busca.

03:52

E existe uma parte que acontece na hora da pergunta.

03:56

A aplicação recebe a pergunta, busca os trechos relevantes,

04:00

monta o contexto, chama o modelo e devolve a resposta.

04:04

Essa separação é muito importante,

04:06

porque muita gente pensa que RAG é só colocar

04:09

dados num banco vetorial no meio da aplicação.

04:11

Mas o banco vetorial é apenas uma peça.

04:14

O mais importante é entender o fluxo arquitetural. Se a ingestão for ruim...

04:19

a busca tende a ser ruim. Se a busca for ruim,

04:22

o contexto enviado ao modelo também tende a ser ruim.

04:25

E se o contexto também for ruim,

04:26

a resposta final pode sair errada, mesmo usando um modelo excelente.

04:32

Então, a qualidade do RAG não depende só do modelo,

04:35

depende de como a aplicação recupera o contexto.

04:39

E nesse capítulo,

04:41

a gente vai começar a construir um projeto prático para enxergar tudo isso.

04:46

Vai ser uma espécie de um chat com uma base interna. No começo,

04:49

a gente vai perguntar para o modelo sem RAG para ver o problema e depois

04:53

a gente vai colocar um documento inteiro no

04:55

prompt para entender como isso funciona.

04:58

E quando começar a ficar mais limitado,

05:01

a gente vai criar um pipeline de RAG utilizando documentos ali em Markdown.

05:07

Usando o Langchain, Postgres, PG Vector. E, no final das contas,

05:10

o nosso objetivo é ter uma aplicação onde o usuário faz a pergunta,

05:14

o sistema busca os trechos relevantes dos documentos,

05:17

responde com base nesses trechos e mostra ali as fontes usadas.

05:22

Então, nessa primeira aula,

05:23

guarda a ideia principal.

05:25

RAG é uma arquitetura para conectar um modelo de linguagem a conhecimento externo.

05:30

Ele permite que a aplicação recupere informações relevantes e entregue...

05:35

esse contexto para o modelo responder melhor.

05:38

No próximo vídeo,

05:39

a gente vai aprofundar o problema que o RAG resolve e

05:42

por que isso virou uma peça tão importante nas aplicações com IA.

05:46

Então, vamos nessa!

## Resumo IA

[RESUMO_IA]