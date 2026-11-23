Módulo: Arquitetura na Era da IA\
Aula: [Pipeline de ingestão inicial](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18412)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, agora a gente está numa parte que é importante,

00:07

que é a parte do ingeste que eu falei para vocês.

00:09

Por enquanto a gente não está gravando ali nada

00:11

em banco de dados ou coisa desse tipo.

00:13

Mas aqui eu quero trazer algumas coisas que são muito importantes,

00:19

que mudam o jogo completamente.

00:23

quando você vai trabalhar com reggae.

00:24

E é aí que eu acho que a maioria das

00:26

pessoas acabam errando e simplesmente tendo um resultado muito ruim.

00:32

Muita gente fala que fazer reggae é fácil, mas no final das contas,

00:35

o que normalmente eu digo, fazer um reggae é fácil,

00:37

agora fazer o resultado do reggae sair do jeito que você quer.

00:42

da forma como você quer, com as informações corretas, é muito difícil, tá? De forma geral.

00:47

A gente não pode necessariamente gerar uma simplificação

00:51

disso e falar que tudo é simples. Não é.

00:54

Fazer o resultado sair do jeito que você quer é mais difícil do que parece.

00:58

Uma das coisas que vão ajudar muito,

01:00

muito mesmo você conseguir fazer isso, é organizar os seus metadados. Então,

01:05

se você olhar aqui nesse arquivo, eu tenho aqui Required Metadata.

01:09

O que aqui, no final das contas,

01:11

eu tenho? No meu banco de dados,

01:13

vamos imaginar que tudo isso aqui vão ser colunas do meu banco de dados.

01:16

Ou seja, cada dado, cada metadado, basicamente, o que vai me ajudar?

01:22

Se eu fizer uma pergunta específica sobre tal assunto,

01:26

ao invés de eu buscar o banco de dados inteiro,

01:28

eu posso pedir para ele fazer where, assunto é product,

01:32

tá? Where não sei o que é isso.

01:35

Ou eu quero ver somente documento com status publicado.

01:39

Ou eu só posso mostrar para aquele tipo de chat, para aquele agente,

01:44

documento que a visibilidade esteja para o usuário

01:47

final e não para um usuário admin.

01:49

Ou para determinado tenant, imagina que eu tenho,

01:53

sei lá, um SaaS, uma aplicação multi -tenant, multi -usuário, etc., multi -empresa,

01:57

eu posso ter aqui o tenant ID, por exemplo. Ou seja,

02:01

sempre quando você for fazer qualquer coisa de RAG e nesse estágio de ingestão,

02:07

toma muito cuidado.

02:09

Realmente pense muito, mas muito mesmo quais são os metadados que você vai querer.

02:14

Como que você pode categorizar isso?

02:16

Porque quanto mais você consegue categorizar e organizar,

02:19

melhor é a forma que você tem para filtrar a informação,

02:24

para trazer os documentos e fazer a busca

02:27

somente naqueles documentos que fazem sentido.

02:31

Para você não fazer, vamos dizer, um select asterisco. Então,

02:34

você vai ter vários URs para ajudar você no meio do caminho.

02:39

Então, por isso que eu estou pegando bem forte nessa parte do metadados.

02:43

Eu digo isso porque eu já caí muito nessa pegadinha de não estruturar direito. E quando eu fui ver,

02:48

eu estava fazendo consulta demais, trazendo dados errados,

02:50

dados que não precisavam vir e etc.

02:54

E aqui, basicamente, tem uma função ali de Part Document.

02:58

Por quê? Porque eu estou usando o YAML. Então, basicamente,

03:01

O que ele está fazendo é, ele pega, sei lá, billing aqui.

03:04

Ele tem que processar isso aqui como um YAML. Então, basicamente,

03:07

eu estou pegando os tracinhos do YAML aqui e tratando essa informação para

03:12

ele conseguir parsear o documento e pegar os índices que eu estou precisando.

03:16

Então, aqui ele consegue trazer aqui para mim.

03:19

E aqui eu tenho o caminho, o nome do arquivo, os metadados,

03:23

o conteúdo e o tamanho do conteúdo. E aí,

03:26

finalmente, eu tenho uma função de Load Documents.

03:30

E aí, no final das contas, o que ele vai fazer?

03:32

Ele vai buscar dentro do diretório todos os arquivos Markdown,

03:36

vai fazer um parse e retornar ali para a gente.

03:40

E no final das contas,

03:41

eu tenho o meu print summary que ele vai pegar ali

03:44

e resumir tudo o que aconteceu ali de todos os documentos.

03:48

E depois disso, no meu método, na minha função main,

03:51

é somente a execução que eu vou dar o print summary aqui para a gente.

03:55

Então, se eu chegar agora aqui, vamos sair desse cara e vou entrar no ingest,

04:02

Vamos lá, ingest aqui para mim.

04:05

O que vai acontecer se a gente olhar nesse momento?

04:09

Ele vai mostrar que eu tenho aqui esses documentos carregados.

04:14

Eu tenho o billing policy, que é o título,

04:17

o tenant FCAI, o product FCAI Cloud, o plano são todos.

04:22

O tipo é policy, a versão, se está publicado,

04:26

o tamanho do conteúdo,

04:28

a quantidade de caracteres que eu tenho em cada um desses conteúdos aqui para mim.

04:31

Então, basicamente,

04:32

o que eu fiz agora foi carregar e conseguir separar esses documentos,

04:37

tanto pelo seu conteúdo, mas principalmente aqui com os seus metadados.

04:41

Então, entenda, se você tiver que tirar algo bem importante dessa aula é...

04:47

Tome cuidado com os metadados,

04:49

tá? Os metadados são os pontos super importantes. Somente para você ficar ligado,

04:54

por exemplo, é muito comum, às vezes, nos metadados, ter também um source.

04:58

Por exemplo, ah, esse documento veio do site, esse documento veio do Google Docs,

05:03

esse documento veio de um PDF, esse documento veio dali, esse documento veio dali,

05:07

entendeu? Então, é muito importante também você saber o tipo de documento,

05:11

principalmente se você está trabalhando numa empresa que

05:14

pega os documentos de diversos lugares. Então,

05:17

tente trazer... essas informações. Quando você trabalha, inclusive,

05:22

com Langchain ou Frameworks ou coisas desse tipo,

05:25

às vezes você tem plugins de, sei lá, importar PDF,

05:28

e ele já traz ali os metadados daquele PDF para ajudar a complementar coisas. Mas tome cuidado,

05:34

porque às vezes vem lixo demais que você não precisa,

05:37

e às vezes tem alguma informação que realmente é útil.

05:40

Então, revise todos os metadados, porque um documento, um arquivo, sei lá, doc,

05:47

Tem metadados que podem ser úteis,

05:49

mas não necessariamente ele vai ter todos os metadados que

05:53

um PDF tem ou que um Markdown tem.

05:55

Então, você tem que realmente entender o negócio,

05:58

você tem que entender as regras de negócio,

05:59

você tem que entender realmente o que vai ser buscado para

06:03

Saber o que vai entrar ou não nos metadados.

06:05

Porque nem todos os documentos,

06:07

nem todas as linhas do banco de dados,

06:08

necessariamente vão ter todos os metadados preenchidos.

06:12

Então, toma muito cuidado com isso aí. Vamos seguindo, galera.

## Resumo IA

[RESUMO_IA]