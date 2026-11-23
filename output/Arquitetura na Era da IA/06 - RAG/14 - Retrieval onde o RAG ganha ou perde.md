Módulo: Arquitetura na Era da IA\
Aula: [Retrieval onde o RAG ganha ou perde](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18416)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente indexou os chunks no Postgres usando o PG Vector. Ou seja,

00:07

agora a nossa base de conhecimento já deixou de ser apenas um conjunto de

00:12

arquivos Markdown e passou a existir também como

00:15

um índice semântico dentro do banco.

00:18

Mas ainda tem um ponto importante,

00:20

indexar não significa que o RAG já está pronto. A partir de agora,

00:26

entra uma das partes mais críticas de qualquer arquitetura RAG,

00:30

que é o retrieval. E retrieval, basicamente,

00:33

é a etapa de recuperação.

00:35

É quando o usuário faz uma pergunta e a aplicação tenta encontrar,

00:39

dentro da base indexada, quais chunks são os mais relevantes para aquela pergunta.

00:45

Só que aqui tem uma armadilha.

00:47

Muita gente trata o retrieval como se fosse uma etapa automática e confiável.

00:51

Tipo assim, gerei um embedding, salvei no banco,

00:54

agora é só buscar o mais parecido e pronto.

00:56

Mas na prática não é tão simples.

00:59

Do retrieval é onde o RAG começa a ganhar ou perder qualidade.

01:03

Se a busca trouxer o contexto certo,

01:06

o modelo tem uma chance muito maior de responder bem.

01:09

Mas se a busca trouxer o contexto errado,

01:13

o modelo pode gerar uma resposta bonita em cima de...

01:16

evidências ruins. E isso é um problema muito perigoso,

01:20

porque a resposta pode parecer muito convincente, inclusive.

01:24

Então, antes de ligar o retrieval com o modelo,

01:27

a gente precisa testar o retrieval sozinho.

01:30

Essa aí é uma prática muito importante.

01:33

Antes de perguntar por que o modelo respondeu errado,

01:36

a gente precisa perguntar, será que a aplicação encontrou o contexto certo?

01:42

É por isso que no próximo passo,

01:44

ainda a gente não vai mostrar a resposta final com o RAG.

01:49

Primeiro, a gente vai criar um script para fazer as perguntas,

01:52

buscar os chunks no PGVector e imprimir o que foi encontrado.

01:57

A gente vai olhar para os documentos retornados,

02:00

as sessões, os metadados e os scores.

02:03

Aqui entram alguns parâmetros que parecem pequenos, mas fazem muita diferença.

02:12

Eu faço uma busca, eu posso pedir os três chunks mais relevantes,

02:16

os cinco mais relevantes, os dez mais relevantes.

02:19

Se eu trago poucos chunks, talvez falte contexto. Se eu trago chunks demais,

02:25

talvez eu comece a colocar ruído na resposta.

02:28

Um outro ponto é o threshold. Nem todo resultado parecido é bom o suficiente.

02:33

Às vezes o banco retorna chunks mais próximos,

02:35

mas isso não quer dizer que eles realmente respondem à pergunta.

02:40

Eles são apenas os melhores dentro do que foi encontrado.

02:43

Se todos forem ruins, ainda assim existe um melhor resultado.

02:47

Por isso, em muitos casos,

02:49

a gente precisa definir um limite mínimo

02:51

de similaridade para aceitar aquele contexto.

02:55

E também tem os filtros por metadados. Esse ponto é arquitetural.

03:00

A busca não deve sair procurando tudo sempre.

03:03

Se a pergunta é sobre produto, FC... AI Cloud, por exemplo,

03:09

não faz sentido recuperar os documentos de outro produto.

03:13

Se o usuário está em um tenant específico,

03:16

não faz sentido buscar documentos de outro tenant. Se o documento está em draft,

03:21

não faz ou não deveria entrar na resposta final. Se existe uma versão publicada,

03:25

a aplicação precisa priorizar a versão correta. Então,

03:29

o retrieval não é só similaridade vetorial.

03:31

O retrieval é similaridade mais filtro, mais contexto de negócio. E aqui,

03:37

a diferença entre um reg de exemplo e um reg mais próximo do mundo real.

03:42

No exemplo simples,

03:43

a gente faz uma pergunta e busca os chunks mais parecidos.

03:46

Em uma arquitetura real, a gente precisa considerar produto, plano, tenant, versão,

03:51

status, visibilidade, permissão e, às vezes, até data de validade daquele documento.

03:56

Uma outra coisa importante é que similaridade não significa verdade.

04:00

Similaridade quer dizer que aquele trecho parece semanticamente próximo da pergunta,

04:05

mas ele pode ser antigo, ele pode estar fora do escopo,

04:08

ele pode ser de outro plano, pode faltar um conceito parecido,

04:12

mas não responder exatamente o que o usuário perguntou. Por isso,

04:17

o retrieval precisa ser... A gente precisa conseguir ver o que foi buscado,

04:23

o que foi retornado,

04:24

quais filtros foram aplicados e quais chunks foram usados depois nas respostas.

04:30

Se essa resposta vira uma caixa preta,

04:33

fica muito difícil melhorar o RAG.

04:37

O time começa a ajustar o prompt, trocar modelo,

04:41

mudar a temperatura, mas o problema real pode estar antes.

04:44

O contexto errado está chegando no modelo. Então, guarda essa ideia. O reg,

04:50

o modelo, gera a resposta. Mas o retrieval escolhe a evidência.

04:54

Se a evidência está errada, a resposta tende a nascer comprometida.

04:59

No próximo vídeo, a gente vai implementar essa inspeção.

05:02

A gente vai criar um script simples para fazer uma pergunta,

05:05

buscar os chunks do Postgres com o pgVector e imprimir os resultados no terminal. Ainda...

05:15

Vamos ainda chamar o modelo para responder. Quer dizer,

05:19

a gente não vai chamar o modelo para responder.

05:22

A ideia é primeiro enxergar se o nosso sistema consegue encontrar o contexto certo.

05:29

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]