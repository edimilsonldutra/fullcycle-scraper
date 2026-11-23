Módulo: Arquitetura na Era da IA\
Aula: [Arquitetura do RAG - ingestão, índice, retrieval e geração](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18411)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? No vídeo anterior a gente fez um teste importante,

00:04

a gente colocou um documento inteiro do prompt e pedimos

00:07

para o modelo responder com base naquele conteúdo.

00:09

Isso ajuda a gente a entender que bases pequenas, às vezes,

00:13

a gente não precisa começar com uma arquitetura mais complexa,

00:16

só que também deixa claro o limite dessa abordagem.

00:19

Quando começam a existir muitos documentos, versões diferentes,

00:23

filtros, permissões e custos de tokens,

00:26

mandar tudo para o prompt deixa de ser uma boa solução.

00:29

Agora, a gente vai entrar na arquitetura RAG de verdade.

00:32

A primeira coisa que a gente precisa entender é que

00:35

RAG não é uma única chamada ao modelo.

00:38

RAG é um pipeline dividido em partes.

00:40

E na prática, essas partes acontecem em momentos diferentes.

00:44

A primeira parte é em gestão.

00:46

Essa etapa acontece antes da pergunta do usuário.

00:49

É onde a aplicação pega os documentos da base interna,

00:52

lê o conteúdo, extrai os metadados,

00:54

quebra esse conteúdo em pedaços menores e prepara tudo para a busca.

00:58

No nosso caso, a fonte de dados vai ser a pasta Knowledge Base.

01:03

Dentro dela, nós temos os conteúdos em Markdown sobre o produto, SLA de suporte,

01:08

plano enterprise, cobrança política e etc.

01:11

Esses documentos têm conteúdo em português,

01:14

mas a estrutura da aplicação continua ali tudo em inglês. Então,

01:18

a ingestão vai olhar para esses arquivos e transformar

01:22

esses documentos em unidades menores que consigam ser buscadas depois.

01:27

Depois vem o índice.

01:29

O índice é a estrutura que permite encontrar

01:32

rapidamente os trechos mais relevantes para uma pergunta. Então,

01:37

no nosso projeto, esse índice vai ficar no Postgres utilizando o PG Vector.

01:42

Ou seja, a gente vai gerar embeddings dos chunks.

01:46

e salvar esses vetores no banco junto com o conteúdo do chunk e seus metadados. Chunk,

01:53

somente para você saber, são pedaços daquele documento.

01:58

Então somente eu tenho um documento,

02:00

essas partes, esses pedaços são os chunks que a gente acaba fazendo.

02:04

E esse ponto é importante, porque o Postgres não vai guardar só o texto,

02:09

ele também vai guardar informações como o documento de origem.

02:15

O tipo do contato, o plano, o produto, a versão, status, a visibilidade.

02:20

Esses metadados vão ser essenciais mais para frente,

02:24

porque uma busca em RAG não deve sair procurando,

02:28

vamos dizer assim, tudo sem critério. Então, basicamente é essa a pegada.

02:34

Depois disso, a gente vai ter a parte do retrieval.

02:37

O retrieval é o momento que o usuário faz a pergunta e

02:40

a aplicação busca no índice os trechos que parecem mais relevantes.

02:43

Essa busca normalmente usa a similaridade entre o

02:47

embedding da pergunta e os embeddings dos chunks salvos.

02:50

Mas aqui tem uma virada importante.

02:52

Retrieval não é resposta.

02:55

Retrieval só encontra candidatos de contexto.

02:58

Por exemplo, se o usuário pergunta sobre SLA de incidentes P1 no plano enterprise,

03:03

O retrieval deveria trazer trechos do documento de suporte,

03:07

talvez filtrando por produto, plano ou status publicado.

03:13

Se esse trouxe um trecho genérico sobre a empresa ou cobrança,

03:17

provavelmente a resposta final vai ficar ruim.

03:19

Por isso, antes de chamar o modelo,

03:22

a gente precisa inspecionar o retrieval isoladamente.

03:26

Então, nas próximas aulas práticas, a gente vai fazer exatamente isso. Primeiro,

03:31

a gente vai buscar chunks e imprimir no terminal quais foram encontrados,

03:34

com os seus metadados, os seus scores. Só depois disso,

03:38

a gente vai acoplar isso com a chamada ao modelo.

03:42

A próxima parte vai ser a montagem do contexto.

03:45

Depois que a aplicação recupera alguns chunks,

03:48

ela precisa decidir o que vai entrar no prompt final.

03:52

E não é simplesmente pegar tudo e jogar para o modelo.

03:55

A aplicação precisa montar uma mensagem com instruções claras,

04:00

incluir os trechos relevantes.

04:02

Preservar as fontes e pedir para o modelo

04:04

responder somente com base naquele contexto.

04:07

Essa etapa é onde muita coisa pode dar errado.

04:11

Contexto demais aumenta custo e pode confundir.

04:14

Contexto de menos pode deixar a resposta incompleta.

04:17

Contexto errado faz o modelo responder bem em cima de evidências erradas.

04:22

E daí, a gente tem por último, que é a geração.

04:26

A geração é a etapa em que o modelo finalmente responde.

04:30

Repara que o modelo entra no final do fluxo. Antes dele,

04:35

a aplicação já leu documentos, preparou chunks, indexou informações,

04:39

buscou o contexto, montou o prompt e isso...

04:43

é o que diferencia a RAG de uma chamada comum para o LLM.

04:46

Então, quando a gente pensa na arquitetura, temos dois fluxos bem separados.

04:51

O primeiro da ingestão de documentos,

04:53

metadados, chunks, embeddings e índice. E o segundo é o fluxo de consulta,

04:57

que é a pergunta do usuário,

04:58

busca no índice, montagem do contexto,

05:00

chamada ao modelo e resposta com fontes. Essa separação é fundamental.

05:06

A ingestão não deve acontecer toda vez que o usuário perguntar algo.

05:11

Ela é uma... preparação da base.

05:14

Já a consulta acontece em tempo de uso,

05:17

quando o usuário interage ali com o chat, por exemplo. Então, no próximo vídeo,

05:21

a gente vai começar a implementar o pipeline de ingestão inicial.

05:25

Ainda a gente não vai gerar embeddings, nem fazer retrieval. Primeiro,

05:28

a gente vai ler os documentos,

05:30

extrair os metadados e validar que a nossa

05:32

base interna está pronta para ser processada.

05:35

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]