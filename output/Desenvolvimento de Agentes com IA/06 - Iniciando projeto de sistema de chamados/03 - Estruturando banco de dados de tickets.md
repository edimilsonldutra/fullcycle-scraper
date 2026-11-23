Módulo: Desenvolvimento de Agentes com IA\
Aula: [Estruturando banco de dados de tickets](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18558)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos estruturar o banco de dados para trabalhar com os tickets.

00:05

Não vamos usar nada elaborado, vamos continuar trabalhando com o SQLite,

00:09

como já é uma dependência que já está adicionada aqui,

00:12

mas como nós já tínhamos adicionado o Postgres também,

00:16

basta, na verdade, mudar a conexão e levantar o container que está no projeto.

00:23

Isso vai ser apenas a mudança de um arquivo.

00:26

Então, nós já temos o SQLAlchemy adicionado.

00:31

E aqui a pasta do banco de dados. Tem tudo que a gente precisa aqui.

00:37

Tem a parte de definição da

00:40

conexão. Então, aqui nós apontamos o banco de dados para dentro da pasta Agents.

00:47

Como nós vamos ter dois agentes utilizando o banco de dados, eu vou salvar na raiz.

00:53

Não vou salvar dentro do Ticket Receptionist, não. Senão vai ficar ruim.

00:59

Então temos uma função para iniciar o banco de dados, para poder fechar a conexão.

01:04

Esse aqui vai acabar criando as tabelas e que fecha a conexão caso seja necessário.

01:12

Em questão de models, como nós estamos trabalhando com um ORM,

01:17

eu tenho a categoria do ticket que vai ser um enum

01:21

que está sincronizado com o que nós temos lá no prompt.

01:24

Então tem a categoria de billing, bug, feature request, enfim.

01:29

O ticket status, para que nós saibamos qual é o status dele,

01:34

se está pendente, se está esperando uma aprovação,

01:38

se está resolvido, se foi escalado.

01:40

Eu coloquei aqui os status para simbolizar o que nós poderíamos fazer com o ticket.

01:47

Um modelo de classificação que é idêntico

01:51

ao que nós definimos lá no agente,

01:54

mas no agente tem uma diferença.

02:00

Porque, lembrando que nós... Tendemos a trabalhar com

02:06

os dados puros aqui.

02:08

Nós não vamos ficar puxando nenhum objeto complexo

02:11

por conta da questão de serialização.

02:13

As coisas são gravadas no banco e também enviadas para LLM,

02:16

então elas precisam ser serializáveis e deserializáveis facilmente.

02:21

Mas, na verdade, não temos nada demais, a não ser que o ticket categórico é um enum,

02:27

então fica fácil para que a gente depois faça verificações, as tal coisa.

02:34

billing ou qualquer coisa assim.

02:37

Então, esse aqui é o model que vai gerar uma tabela de tickets no banco de dados.

02:44

A tabela vai ser tickets, como essa variável está definida, tem o id,

02:48

que eu coloquei um id personalizado,

02:52

aqui é o tck, mas um id aleatório,

02:57

utilizando como base o UUID4, não vai ser um UUID4,

03:02

mas vai apenas utilizar como base. A gente poderia definir qualquer coisa,

03:07

não é o caso, mas nós vamos ter a relação desse ticket com o usuário,

03:11

a mensagem do ticket que é string,

03:13

o status que tem relação ali com o ticket status também,

03:17

que é o enum. O classification,

03:19

como nós podemos organizar para não ficar muitos campos, ele vira esse embedded,

03:25

nós podemos chamar isso aqui de condensador de campos,

03:30

porque aí eu faço ticket classification quanto qualquer coisa.

03:36

A resposta, que é o resultado final do que nós vamos resolver,

03:41

é gravada aqui. Se tiver algum erro, nós podemos gravar.

03:43

E data de atualização e de criação. Ele pega de forma automática.

03:49

Então, nós temos que preencher esses dados aqui.

03:52

Na verdade, logo de cara, não tem que preencher a resposta,

03:56

porque nós não temos erro também.

03:58

Nós não vamos preencher, vamos mais preencher a classificação e o Customer ID.

04:06

Também nós temos um repositório para que nós possamos,

04:10

nós não lidamos ali com o modo diretamente.

04:14

Então, aqui também eu quero aproveitar o momento

04:17

para poder falar sobre questão de camadas.

04:20

Eu não estou aqui preocupado em usar abordagens como Clean Architecture, Domain Design,

04:28

Application Service.

04:30

Tudo isso cabe junto com os agentes, não tem nenhuma restrição.

04:35

Claro que você precisa saber o que você está fazendo,

04:38

saber escolher o que você vai usar nos momentos adequados.

04:42

A minha ideia aqui de repositório é justamente aquela ideia do repositório da ORM,

04:47

que nós possamos fazer um CRUD com as operações.

04:51

Na verdade, um CRUD com os modos. Então,

04:54

eu posso passar um TicketMode aqui no CreateTicket, ele vai fazer a criação,

05:00

no modo do SQLAlchemy. Update também e um getTicket.

05:06

Toda vez usa esse asyncSession e

05:10

nós temos benefícios de trabalhar com ele.

05:14

Eu não quero entrar em detalhes de questões de outras libs,

05:18

a não ser o nosso desenvolvimento com os agentes.

05:20

Nós vamos ter esse repo e vamos chamar essas operações nos momentos adequados.

05:28

Também temos um reset.py,

05:32

que vai apagar todas as tabelas do banco de

05:35

dados e recriá-las quando for necessário.

05:38

Então, nós podemos chegar aqui

05:41

e fazer um python

05:44

db reset, já

05:47

para poder iniciar, então nós já vamos ter as tabelas criadas aqui.

05:52

Se precisar apagar, só rodar novamente este comando.

05:57

Então, o mínimo que a gente precisa, parte de conexão,

06:01

modelos, repositório e

06:05

o reset. Poderíamos até colocar seeds,

06:07

se for necessário. E nós vamos chamar esse DB, não tem nada aqui,

06:12

complexo, nós vamos chamar esse DB, na verdade dá para chamar o repo diretamente,

06:19

por exemplo, db.repo, aí dá para fazer o create ticket, enfim.

06:23

Agora, com o nosso banco de dados estruturado,

06:25

vamos continuar para que a gente possa criar

06:27

o nosso agente de gerenciamento de tickets,

06:30

de criação de tickets.

## Resumo IA

[RESUMO_IA]