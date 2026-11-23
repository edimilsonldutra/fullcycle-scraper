Módulo: Arquitetura na Era da IA\
Aula: [Reranking sem chamar o modelo novamente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18448)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, no vídeo anterior,

00:04

o que aconteceu que eu falei para vocês e eu queria deixar mais claro,

00:08

como se fosse um parênteses aqui,

00:10

é falar sobre re-ranking chamando o modelo. O que significa, pessoal?

00:17

Toda vez, nesses exemplos que a gente fez de forma didática,

00:21

a gente está chamando o processo de re-ranking.

00:24

Ou seja, esse processo de re-ranking está chamando o modelo.

00:29

Mas essa, de forma geral, não é a única forma de fazer. Na prática,

00:33

re-ranking significa simplesmente reordenar ou selecionar

00:38

melhor os candidatos depois da primeira busca.

00:41

Isso pode acontecer de várias maneiras.

00:43

A forma mais simples é usar o próprio score da busca vetorial.

00:48

A gente busca, por exemplo, 20 chunks mais parecidos e pega os quatro primeiros.

00:54

Isso é fácil, barato e rápido, mas tem uma limitação.

00:58

Se a busca vetorial já trouxe resultados genéricos no topo,

01:01

a gente só está confiando mesmo no ranking inicial.

01:05

Agora, uma outra alternativa é usar algo chamado de MMR,

01:11

que é Maximal Marginal Relevance.

01:14

A ideia do MMR é equilibrar a relevância e diversidade. Então,

01:21

em vez de eu trazer quatro chunks praticamente iguais sobre o mesmo ponto,

01:27

ele tenta trazer quatro chunks, por exemplo, relevantes,

01:30

mas menos repetidos entre si. Então,

01:34

isso ajuda quando a pergunta precisa de um contexto mais amplo. Por exemplo,

01:38

suporte enterprise envolvendo P1, canais,

01:42

escalonamento e gerente de conta.

01:47

Também dá para a gente fazer o re-ranking utilizando busca lexical. Ou seja,

01:53

nesse caso, a gente usa uma busca... textual tradicional, como um full text search,

01:59

por exemplo, no Postgres, para valorizar os termos exatos. Então,

02:05

isso é muito útil em bases como a nossa,

02:08

que tem termos como P1, P2, P3, SSO, SCIM,

02:14

Open Telemetry, 99%, PRO, Starter, Enterprise.

02:19

Às vezes, o termo literal...

02:22

é mais importante do que a similaridade semântica.

02:25

E uma evolução natural disso é a busca híbrida.

02:31

A aplicação roda uma busca vetorial e uma busca textual.

02:36

Depois combina os rankings.

02:38

E um método comum para isso é chamado de RRF,

02:44

que significa Reciprocal Rank Fusion.

02:49

Onde os documentos bem posicionados em diferentes buscas ganham mais relevância.

02:55

Isso costuma ser muito forte em RAG real,

02:58

porque une o significado com a precisão do termo.

03:03

E outra opção simples também é aplicar boosts por metadados.

03:09

Então, se o query planner,

03:11

por exemplo, identificou que a pergunta é sobre SLA e plano enterprise,

03:18

a aplicação pode aumentar a prioridade de chunks com

03:23

doc type SLA e plan interface ou plan igual a all,

03:28

por exemplo. Isso não usa o outro modelo.

03:31

É uma regra arquitetural em cima dos metadados que a gente já tem.

03:36

E também existe ainda o cross encoder re-ranking.

03:43

Aqui a gente não chama o modelo de chat,

03:45

Mas a gente usa um modelo especializado em relevância.

03:50

Ele recebe a pergunta de cada chunk candidato e devolve uma pontuação.

03:56

Normalmente ele é mais preciso, mas adiciona custo e latência.

04:02

Esse re-ranker pode ser uma API externa ou até um modelo local,

04:06

dependendo da arquitetura. Então, quando eu digo re-ranking,

04:11

eu não quero que você pense apenas em chamar LLM novamente.

04:15

Esse é um caminho possível, mas não é obrigatório.

04:19

A ideia principal é separar duas etapas.

04:22

Primeiro, a busca inicial e encontro dos candidatos.

04:25

Depois, uma segunda estratégia é escolher quais candidatos

04:29

realmente merecem entrar no contexto final.

04:31

No nosso projeto, usar...

04:33

o modelo para re-ranking é didático,

04:36

porque a gente já está trabalhando ali com structured

04:39

output e a gente consegue visualizar a decisão.

04:43

Mas em produção, essa etapa poderia ser substituída por MMR, busca lexical,

04:49

busca híbrida, boosts por metadados ou um re-ranker especializado.

04:55

O ponto arquitetural é esse. O retrieval inicial não precisa ser a última palavra.

05:02

A aplicação pode buscar mais,

05:04

selecionar melhor e mandar menos contexto para o modelo final.

05:08

Isso melhora a qualidade, reduz o ruído e ajuda a controlar o custo.

## Resumo IA

[RESUMO_IA]