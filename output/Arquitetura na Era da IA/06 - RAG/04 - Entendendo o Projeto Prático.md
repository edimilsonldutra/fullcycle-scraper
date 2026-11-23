Módulo: Arquitetura na Era da IA\
Aula: [Entendendo o Projeto Prático](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18406)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente comparou o RAG com outras estratégias como Long Context,

00:07

Cache, SQL, API,

00:09

Tool Calling e Fine Tuning.

00:11

A ideia foi mostrar que RAG não é uma

00:14

resposta automática para qualquer problema com IA.

00:16

Ela faz sentido quando a aplicação precisa recuperar conhecimento externo,

00:20

normalmente textual, e entregar esse contexto para o modelo responder melhor.

00:25

Agora a gente vai apresentar o projeto prático que vai guiar esse capítulo.

00:30

A gente vai construir um Knowledge Chat, ou seja,

00:33

um chat que responde perguntas em uma base inteira de documentos.

00:39

A ideia é simular um cenário bem comum em aplicações reais.

00:42

A empresa tem documentos internos, políticas, regras, fax,

00:46

documentação de produtos, informações de suporte, regras comerciais,

00:50

e quer que o usuário consiga fazer perguntas em linguagem natural. Então,

00:54

o usuário pode perguntar algo como...

00:57

Qual é o prazo de reembolso para os alunos do plano Enterprise?

01:01

Só que a aplicação não vai simplesmente mandar essa pergunta para

01:05

o modelo e esperar ele responder com conhecimento geral.

01:08

Ela vai primeiro buscar nos documentos internos quais

01:10

trechos são relevantes para essa pergunta.

01:12

Depois vai montar o contexto com esses trechos.

01:15

Só então vai gerar uma resposta através do modelo.

01:20

O resultado final que a gente quer é uma resposta mais ou menos assim.

01:25

O prazo de reembolso para o plano Enterprise é de tantos

01:28

dias de acordo com a política interna de reembolso.

01:31

E junto com isso, a aplicação também pode mostrar a fonte usada.

01:35

Por exemplo, o documento,

01:37

a sessão e a versão daquela política.

01:40

Isso é importante porque a gente não quer apenas uma resposta bonita.

01:44

A gente quer uma resposta rastreável. O usuário,

01:47

o desenvolvedor ou o time responsável precisa conseguir

01:50

entender de onde aquela resposta veio.

01:54

A base de dados do nosso projeto vai começar de forma simples.

01:59

A gente vai usar documentos em Markdown.

02:01

Não vamos começar com PDF, Crawler, Google Drive,

02:04

Notion, Confluence ou qualquer integração mais pesada.

02:07

Tudo isso existe no mundo real, mas se a gente começar por aí,

02:11

a aula vai virar muito mais uma aula de

02:14

extração de documentos e integração com ferramentas.

02:17

O nosso foco agora aqui é a arquitetura de RAG.

02:20

Então, vamos trabalhar com uma pasta de documentos internos.

02:24

Por exemplo, uma política de reembolso, um SLA de suporte, acesso ao curso,

02:30

plano Enterprise, certificado, pagamento e fax de produto.

02:34

Cada arquivo vai ter o seu conteúdo textual e também alguns metadados como produto,

02:39

plano, tipo de documento, versão, status e tenant.

02:43

Esses metadados são importantes porque no mundo real o

02:47

RAG não deveria sair buscando em tudo sem nenhum critério.

02:51

Muitas vezes, a pergunta precisa considerar o plano do usuário, o produto,

02:57

a versão do documento, se o documento está publicado ou não.

03:00

Até o tenant daquele cliente.

03:02

Na parte técnica, a gente vai usar Python com Langchain. Postgres e PG Vector.

03:08

O Postgres vai ser o nosso banco de dados

03:09

principal para armazenar os chunks e os embeddings.

03:12

O PG Vector vai permitir fazer as

03:15

buscas por similaridade dentro do próprio Postgres.

03:21

E isso é interessante porque muita gente conhece o Postgres,

03:24

já utiliza o Postgres no dia a dia e já consegue entender

03:28

melhor como essa arquitetura se conecta com algo mais próximo da realidade.

03:33

O projeto vai ter dois fluxos principais.

03:35

O primeiro é o pipeline de ingestão.

03:38

Esse pipeline vai ler os documentos do Markdown,

03:41

extrair os metadados, quebrar o conteúdo em chunks,

03:44

gerar embeddings e salvar tudo no Postgres.

03:47

Essa etapa e essa parte acontecem antes da pergunta do usuário.

03:51

É a preparação da base.

03:53

O segundo é o pipeline de consulta. Esse acontece quando o usuário faz uma pergunta.

04:00

A aplicação pega a pergunta, gera uma representação dela,

04:03

busca os chunks mais relevantes no PG Vector,

04:06

monta o contexto, chama o modelo e devolve a resposta com as fontes.

04:13

A gente vai começar pelo terminal, isso é proposital. Nesse momento,

04:18

eu não quero escolher o GUI atrás de uma interface bonita.

04:21

Eu quero que a gente consiga enxergar o que está acontecendo.

04:25

Eu quero mostrar quais chunks foram encontrados, quais metadados vieram,

04:29

qual fonte foi usada e qual resposta foi gerada.

04:32

Depois, quando o pipeline estiver claro,

04:34

a gente transforma isso ali numa API simples com endpoint de chat.

04:39

Aí fica mais próximo do que a gente trabalharia ali

04:43

no dia a dia com uma aplicação real.

04:45

O ponto principal é que esse projeto não existe

04:48

só para fazer um chat com documentos.

04:50

Ele existe para a gente enxergar as decisões arquiteturais do REG,

04:55

como preparar uma base,

04:57

como buscar contexto, como filtrar, como evitar a resposta sem fonte,

05:01

como lidar quando não existe informação suficiente e

05:04

como debugar quando uma resposta vem errada. Então,

05:08

a partir do próximo vídeo, a gente começa a montar esse projeto do zero.

05:13

Primeiro... Vamos preparar o ambiente,

05:15

subir o Postgres com o PGVector e deixar a estrutura inicial

05:18

pronta para a gente construir o nosso Knowledge Chat.

## Resumo IA

[RESUMO_IA]