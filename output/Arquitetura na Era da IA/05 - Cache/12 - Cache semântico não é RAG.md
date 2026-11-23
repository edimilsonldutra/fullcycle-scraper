Módulo: Arquitetura na Era da IA\
Aula: [Cache semântico não é RAG](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18348)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente falou sobre similaridade, distância e threshold.

00:06

A ideia principal foi entender que embedding não

00:09

serve só para gerar um vetor bonito.

00:11

Ele permite comparar textos por proximidade de significado.

00:15

Agora, antes de entrar no PgVector, que é uma extensão do Postgres,

00:19

para trabalhar com um banco de dados vetorial,

00:21

vamos dizer assim, eu quero separar uma coisa que pode gerar bastante confusão.

00:25

Cache semântico... Não é RAG, tá? E se você não sabe o que é RAG,

00:30

RAG significa Retrieval Augmented Generation.

00:34

A gente vai ver isso depois, tá? Essa confusão,

00:38

ela é normal porque os dois assuntos usam algumas peças parecidas.

00:43

Os dois podem usar embeddings, os dois podem usar busca vetorial,

00:47

os dois podem usar bancos de dados como um PG Vector,

00:50

por exemplo, só que a intenção arquitetural é completamente diferente.

00:56

No cache semântico, a pergunta que a aplicação faz é,

00:59

eu já respondi algo parecido antes?

01:02

Já no RAG, a pergunta é,

01:04

quais informações eu preciso buscar para gerar uma nova resposta agora?

01:09

Percebe a diferença? No cache semântico,

01:12

eu estou tentando evitar uma nova chamada para IA,

01:15

eu tenho uma resposta anterior gerada em algum momento e

01:20

eu quero saber se eu posso reaproveitar essa resposta com segurança.

01:24

Então, eu pego uma nova mensagem, gero um embedding,

01:27

procuro mensagens anteriores parecidas e aplico um threshold e

01:31

vejo se aquela resposta cacheada ainda serve. Por exemplo,

01:35

a aplicação já analisou antes a mensagem como que eu cancelo

01:38

a minha assinatura e retornou uma classificação como cancellation.

01:41

Depois chega uma outra mensagem dizendo, quero cancelar meu plano.

01:45

O texto não é igual, então o cache exato não resolveria,

01:49

mas semanticamente pode ser próximo o suficiente para eu reaproveitar a resposta.

01:52

Então esse é o cache semântico.

01:55

Agora o RAG, o motivo é outro. Imagina que um usuário pergunta,

01:59

qual é a política atual de cancelamento? Nesse caso,

02:02

eu não quero simplesmente reutilizar uma resposta antiga.

02:06

Eu quero buscar trechos relevantes numa base de conhecimento,

02:11

talvez documentos internos, páginas de ajuda, contratos, políticas atualizadas,

02:16

e depois montar um contexto para o modelo gerar uma nova resposta.

02:22

Então, o RAG normalmente usa a busca vetorial, na realidade.

02:27

Mas ela não substitui a chamada para o modelo. Ela prepara a chamada.

02:32

No cache semântico, a busca vetorial pode evitar a chamada.

02:36

Então, essa distinção muda tudo. No cache semântico,

02:39

o banco pode guardar entradas como mensagem original,

02:44

embedding da mensagem, resposta gerada, versão do prompt,

02:47

versão das regras e capacidades do modelo.

02:50

A aplicação procura uma resposta parecida para reutilizar. No RAG,

02:54

o banco normalmente guarda chunks de documentos. Embeddings desses chunks,

02:59

metadados, fontes, a versão do documento e talvez até a permissão para acesso.

03:05

E aí a aplicação procura conhecimento para montar o contexto.

03:10

Então mesmo que a tecnologia seja parecida, o objetivo não é o mesmo.

03:14

E isso é importante para a nossa sequência,

03:17

porque na próxima prática a gente vai começar a usar o PG Vector,

03:21

mas a gente ainda não vai entrar em RAG. A gente vai utilizar,

03:26

vamos dizer assim, o PG Vector para uma coisa bem específica.

03:30

Salvar embeddings de mensagens já analisadas

03:32

e buscar respostas anteriores parecidas.

03:35

A gente não vai falar ainda sobre chunking, ingestão de documentos, re-ranking,

03:40

montagem de contexto ou respostas baseadas em fontes externas.

03:44

Isso fica para um capítulo de RAG.

03:46

O foco aqui continua sendo cache. A pergunta desse capítulo é,

03:50

quando eu posso evitar chamar a IA de novo?

03:55

E o cache semântico é uma resposta possível para essa pergunta,

03:58

desde que a gente utilize esse cara com cuidado,

04:01

porque parecido não significa automaticamente reutilizável. Então, na próxima aula,

04:07

a gente vai preparar ali o Postgres com o PG Vector para começar a persistir

04:11

esses embeddings e sair do conceito para uma

04:14

estrutura mais próxima de uma aplicação real.

04:16

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]