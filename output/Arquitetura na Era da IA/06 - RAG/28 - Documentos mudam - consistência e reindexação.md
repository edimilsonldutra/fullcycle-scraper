Módulo: Arquitetura na Era da IA\
Aula: [Documentos mudam - consistência e reindexação](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18449)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem? Até aqui o nosso RAG já ficou bem mais completo.

00:07

A gente criou a base de documentos,

00:09

gerou os chunks com os metadados,

00:12

indexou no Postgres com o pgVector, testou o retrieval,

00:16

montou a resposta com as fontes,

00:18

adicionou o query planner e depois colocou uma etapa

00:21

de re-ranking para selecionar melhor o contexto final.

00:25

Agora, falta olhar para um problema que aparece em qualquer RAG

00:31

tem, vamos dizer assim, que ele tenta ser mais realista.

00:35

Que é, os documentos mudam. E isso muda bastante a arquitetura.

00:40

Quando a gente indexa os documentos de um banco vetorial,

00:43

aquele índice passa a ser uma representação derivada da base original.

00:48

A fonte da verdade ainda é o documento. Então, o índice existe para... Então,

00:55

se o documento muda e o índice não acompanha,

00:59

a aplicação pode responder com informação antiga.

01:02

Esse é um dos erros mais perigosos quando a gente está falando em RAG,

01:06

porque a resposta pode parecer correta. Ela pode vir com fonte,

01:12

ela pode citar documento certo, pode ter um texto claro,

01:15

mas está baseado em um chunk antigo que não deveria estar sendo mais usado.

01:20

Então, a pergunta não é só... Como que eu gero embeddings? A pergunta é,

01:25

como que eu mantenho o índice consistente com a base de conhecimento?

01:29

Vamos pensar em alguns cenários. Um documento pode ser alterado.

01:33

Por exemplo, o SLA de P1 no Enterprise muda de 1 hora para 30 minutos.

01:39

Se eu não reprocessar esse documento,

01:41

o RAG continua respondendo com a regra antiga.

01:44

Um documento pode sair de Published para Draft. Nesse caso,

01:49

ele não deveria entrar nas respostas, mas se os chunks antigos continuarem no banco,

01:54

talvez a busca ainda encontre aquele conteúdo.

01:58

Um documento pode ser removido. Se o arquivo não existe mais na base,

02:02

mas os chunks continuam indexados,

02:05

a aplicação ainda está utilizando um conhecimento que agora é órfão.

02:10

E também pode surgir uma nova versão. Talvez exista uma nova política de,

02:15

sei lá, 2026-01 para 2028-01. Ou seja,

02:21

a arquitetura precisa deixar claro qual versão está ativa,

02:25

qual está publicada e qual pode ser usada ali na resposta. Por isso, em RAG,

02:32

a indexação não pode ser tratada como um script que roda uma vez e pronto.

02:38

Ela precisa ser pensada como um pipeline idempotente.

02:42

E, de fato, quer dizer que eu posso rodar o

02:46

processo várias vezes e o resultado final continua consistente.

02:50

Se nada mudou, ele não deveria duplicar os chunks. Se algo mudou,

02:55

ele deveria atualizar somente o que precisa.

02:58

Se algo foi removido, ele deveria limpar o índice.

03:02

Uma forma simples de fazer isso é usar um manifest.

03:06

O manifest é um arquivo ou uma tabela

03:09

que registra o estado dos documentos processados.

03:12

Para cada arquivo,

03:14

a gente pode guardar informações como caminho, hash do documento,

03:18

versão, status e quantidade de chunks gerados.

03:22

O hash é importante porque ele permite detectar a mudança.

03:26

Se o conteúdo do documento mudou, o hash muda.

03:31

Se o hash mudou, aquele documento precisa ser reprocessado.

03:35

É como se fosse... a nossa famosa fingerprint.

03:38

O fluxo fica mais ou menos assim.

03:41

A ingestão lê os documentos atuais. Para cada documento,

03:45

calcula um hash. Depois,

03:46

compara esse hash com o que foi registrado no manifesto anterior.

03:51

Se é um documento novo, indexa. Se é um documento alterado,

03:56

remove os chunks antigos e indexa os novos. Se o documento existia no manifesto,

04:02

mas não existe mais na pasta, ele remove os chunks dele do índice.

04:06

Esse processo, ele evita duplicidade e evita respostas com conhecimento antigo.

04:12

Agora, um cuidado.

04:15

Reindexação... Não é só um problema técnico,

04:18

ele também é uma decisão de produto e de operação.

04:21

Em alguns sistemas,

04:22

uma alteração de documento pode atualizar o índice imediatamente.

04:26

Em outros, pode existir um processo de aprovação. Em outros,

04:29

a indexação roda de tempos em tempos por job. Em sistemas maiores,

04:33

isso pode vir através de eventos. Um documento foi publicado,

04:37

uma política mudou, uma página atualizada,

04:39

um arquivo entrou novo no storage, disparou um evento e aí esse pipeline roda.

04:44

No nosso projeto, a gente vai manter isso mais simples.

04:47

A gente vai fazer um pipeline manual,

04:48

executando o comando, mas com um comportamento idempotente.

04:53

A ideia não é montar uma plataforma de ingestão inteira.

04:56

A ideia é que você possa entender o princípio arquitetural que está por trás. Então,

05:02

a mensagem principal dessa aula aqui é que o vector store não é fonte de verdade.

05:09

Ele é um índice derivado. Se a base muda, o índice precisa acompanhar.

05:15

Caso contrário, o REPL pode responder com informação errada,

05:19

mesmo parecendo que está funcionando.

05:21

No próximo vídeo, a gente vai implementar isso.

05:24

A gente vai criar um manifesto simples,

05:26

calcular o hash dos documentos,

05:28

evitar duplicidade e preparar o pipeline para remover

05:32

e indexar chunks quando a base de conhecimento mudar.

05:37

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]