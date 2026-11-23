Módulo: Arquitetura na Era da IA\
Aula: [Reranking e seleção final do contexto](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18445)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente colocou uma etapa nova antes do retrieval,

00:05

o query planner.

00:07

Agora a pergunta do usuário não vai ser mais crua direto para o banco vetorial.

00:12

Primeiro a aplicação tenta entender a intenção, normaliza a pergunta,

00:16

identifica o tipo de documento, plano,

00:19

termos exatos e também detecta se precisa pedir esclarecimento.

00:24

Isso já melhora bastante o nosso RAG. Mas ainda falta um ponto importante.

00:31

Mesmo com uma pergunta melhor,

00:33

mesmo com filtros melhores e mesmo com chances mais contextualizadas,

00:37

o retrieval ainda devolve candidatos.

00:40

Ele não devolve necessariamente o contexto final perfeito.

00:44

E esse é o tema desse nosso bate-papo agora aqui,

00:48

que é re-ranking e seleção final do contexto.

00:51

No nosso código, a gente aumentou inclusive o top K para 8.

00:56

O motivo foi bem prático. Com cinco resultados,

00:59

às vezes o chunk certo ficava de fora por duas ou mais posições.

01:04

Isso é muito comum em retrieval. Às vezes a resposta está na base,

01:09

o documento foi indexado, o chunk existe,

01:12

mas ele não aparece alto o suficiente no ranking inicial.

01:15

Só que aumentar o top K resolve um problema e cria outro.

01:21

Se eu trago mais chunks, eu aumento a chance de trazer o trecho certo.

01:25

mas eu também aumento a quantidade de ruído.

01:28

Mais chunks significa mais tokens, mais custo,

01:31

mais latência e mais informações competindo dentro do prompt. Então,

01:36

o fluxo começa a ficar mais maduro quando a gente separa duas coisas. Primeiro,

01:42

buscar os candidatos. Segundo,

01:44

escolher quais candidatos realmente vão para o contexto final.

01:49

E essa etapa a gente chama de re-ranking.

01:53

O re-ranking é basicamente reordenar os resultados depois da primeira busca.

01:59

A busca inicial pode trazer, por exemplo, 8, 10 ou 20 chunks candidatos.

02:04

Depois, uma segunda etapa analisa esses chunks com mais cuidado

02:08

e decide quais são os mais relevantes para a pergunta.

02:13

A diferença é sutil, mas é importante. A busca vetorial responde algo como...

02:19

Quais trechos são semanticamente parecidos com essa pergunta?

02:22

O re-ranking tenta responder algo mais direto.

02:26

Quais desses trechos realmente ajudam a responder essa pergunta?

02:30

Essa diferença muda bastante a qualidade do RAG.

02:33

Imagina que um usuário pergunta,

02:35

qual é o tempo de resposta para incidentes P1 no plano Enterprise?

02:39

A busca pode trazer um chunk sobre P1, outro sobre Enterprise,

02:43

outros sobre canais de suporte,

02:45

outros sobre crédito de SLA e outros sobre disponibilidade.

02:49

Todos têm uma relação com o tema,

02:51

mas nem todos respondem diretamente à pergunta.

02:54

O ranking tenta priorizar o chunk que fala exatamente

02:58

sobre o tempo de resposta P1 no Enterprise.

03:02

Existem várias formas de fazer isso. Uma solução é usar um re-ranker próprio,

03:07

normalmente um modelo treinado para comparar perguntas do

03:11

documento e dar uma nota de relevância.

03:13

Alguns providers e engines de busca já oferecem isso.

03:17

Outra opção é usar o próprio modelo para avaliar

03:21

os chunks candidatos e selecionar os melhores.

03:24

Isso é mais simples para a nossa aula e entender melhor essa lógica,

03:28

mas tem custo, latência e precisa de cuidado para não virar mais uma caixa preta.

03:33

Também existem técnicas chamadas de contextual comprehension,

03:38

onde a aplicação tenta reduzir o contexto antes de mandar para o modelo final.

03:45

Em vez de mandar chunks inteiros,

03:46

ela seleciona e comprime apenas as partes que realmente importam.

03:51

Mas o ponto arquitetural é o mesmo.

03:54

A gente não precisa mandar para o modelo final tudo o que o retrieval encontrou.

03:58

A aplicação pode buscar mais candidatos e depois

04:01

ser mais criteriosa na montagem do contexto.

04:04

Isso ajuda em três coisas. Primeiro,

04:06

melhora a qualidade, o modelo recebe menos ruído. Segundo,

04:09

reduz custo, menos contexto no prompt, significa menos input tokens.

04:14

Terceiro... melhora a rastreabilidade.

04:17

As fontes finais ficam mais próximas da resposta real e

04:20

não apenas dos chunks que pareciam estar relacionados.

04:23

Agora, tenha um cuidado importante. O re-ranking não substitui filtro de segurança.

04:29

O re-ranker só deve trabalhar em cima de chunks que a aplicação já pode usar. Ou seja,

04:35

o tenant, o produto, o status, as permissões,

04:37

a visibilidade continuam sendo a responsabilidade da aplicação.

04:41

O modelo pode ajudar...

04:45

ordenar a relevância, mas ele não deve decidir ali a alteração,

04:49

quer dizer, a autorização.

04:53

No nosso projeto, isso se encaixa muito bem com o que a gente já tem.

04:56

O query planner melhora a pergunta,

04:59

o retrieval busca candidatos. Agora, o re-ranking,

05:01

ele pode selecionar os melhores chunks antes do prompt final.

05:05

Então, a partir daqui, no nosso pipeline,

05:07

vai começar a ficar assim. Pergunta do usuário, query planner,

05:11

filtros seguros, retrieval de candidatos, re-ranking,

05:15

montagem do contexto e resposta final com as fontes.

05:18

Esse aí já é um fluxo muito mais próximo do que um RAG real.

05:23

A mensagem principal dessa aula é...

05:26

Retrieval não precisa ser a última decisão antes do modelo.

05:30

Em arquiteturas mais maduras, a primeira busca encontra candidatos,

05:34

mas a aplicação ainda pode reordenar filtros e

05:37

selecionar o contexto final com mais cuidado.

05:39

No próximo vídeo, a gente vai implementar uma versão simples disso,

05:43

vamos buscar mais chunks, mais candidatos, pedir uma etapa de re-ranking,

05:47

escolher os mais relevantes e mandar para o

05:49

modelo final apenas os chunks selecionados.

05:52

Então, vamos nessa!

## Resumo IA

[RESUMO_IA]