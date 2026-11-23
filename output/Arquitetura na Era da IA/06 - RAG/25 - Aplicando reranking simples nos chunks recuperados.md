Módulo: Arquitetura na Era da IA\
Aula: [Aplicando reranking simples nos chunks recuperados](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18446)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente falou sobre re-rank,

00:04

correto? Então, qual que é o nosso objetivo aqui?

00:07

Eu tenho uma implementação que se você for olhar no re-rank.py,

00:10

depois a gente olha com calma, tá?

00:12

Mas o ponto aqui é a gente conseguir simular e

00:16

trazer para vocês o quão importante o re-rank é.

00:20

Lembrando que tem duas vertentes aqui que a gente pode pensar no re-rank.

00:24

Uma, tá? É ele escolher os melhores resultados, tá?

00:29

E a outra coisa é escolher os melhores resultados diminuindo a

00:33

quantidade de dados que a gente vai mandar para o modelo.

00:36

No nosso caso aqui, quando a gente não tem um conteúdo muito grande,

00:40

a gente não vai ver expressivamente a melhora super no resultado.

00:44

Mas claramente a gente vai ver quantos candidatos a

00:49

gente tinha e quantos realmente foram enviados para o modelo.

00:52

Então, o que eu vou fazer aqui?

00:54

Eu vou rodar o nosso... Cat com debug normal, certo?

00:59

E agora eu vou fazer uma pergunta do tipo,

01:03

qual é o e-mail de suporte?

01:08

Certo? Então, quando eu fizer essa pergunta,

01:11

ele vai buscar os chunks ali que ele quer.

01:13

Legal? Então vamos ver o que vai acontecer aqui, somente para você dar uma olhada.

01:18

Bom, se você olhar, vamos entender o que aconteceu aqui.

01:25

Eu fiz a minha pergunta. O que aconteceu?

01:28

Ele fez aquele query plan aqui para a gente. Não precisou de clarification.

01:34

Ele escreveu o search term melhor aqui também, certo? E aqui ele trouxe os chunks.

01:40

Então, ele trouxe oito chunks aqui para a gente, certo?

01:46

E aí, o que acontece?

01:48

Acabaram os chunks. Aqui eu tenho o debug do re-rank result,

01:53

tá? O que acontece? O re-rank,

01:56

ele selecionou... O Chunky, Company Info,

01:59

Product Support SLA e Company Info, o Chunky 20 dele,

02:05

tá? Ou seja, ele escolheu três itens para fazer o re-rank.

02:09

Então, o que acontece aqui?

02:11

Ele trouxe a resposta aqui para a gente, certo?

02:15

Porém, ao invés de ele enviar oito...

02:19

perguntas, oito chunks para fazer uma resposta desse tipo,

02:22

ele acabou enviando apenas três.

02:26

Outra coisa que dá para fazer, por exemplo, sei lá, como funciona o programa de,

02:33

sei lá, um programa de, uma coisa que não sei, indicação.

02:39

Vamos lá. Como funciona o programa de indicação?

02:42

Vou dar um enter aqui e

02:45

olha só o que vai acontecer agora aqui para a gente. Olha só que interessante.

02:51

Eu trouxe aqui, ou seja, ele normalizou a questão,

02:54

como funciona o programa de indicação da FCI,

02:57

não tem plano, os termos exatos são programa e indicação,

03:02

não precisa de clarificação, e aqui tem a pergunta,

03:05

como funciona o programa de indicação da FCI, programa, indicação, indicação,

03:09

ele trouxe aqui. E o tenant aqui tem os filtros,

03:11

isso que a gente viu. Agora sobre chunks, olha o que ele trouxe,

03:15

ele trouxe esse chunk, que é a company info. Segurança e conformidade,

03:19

Perguntas frequentes, company info, ou seja,

03:24

Ele trouxe oito caras aqui para mim,

03:27

Tá? Mas, quando eu vou olhar o meu re-rank, re-rank, na realidade,

03:33

É, ele não selecionou nenhum chunk e ele deu zero resultados trazidos.

03:40

Então... A A que já responde para mim,

03:42

Não encontrei informação suficiente na base de conhecimento. Então,

03:45

Perceba que, apesar de eu receber dados do banco de dados vetorial,

03:49

O que acontece é que, na hora que eu for fazer um re-rank,

03:53

Eu consegui perceber que nenhum daqueles chunks, na realidade,

03:56

Iriam ser úteis o suficiente para eu conseguir re-ranquear.

04:00

Então, se eu quiser depois, inclusive, comparar isso aí com a mesma coisa,

04:06

Eu posso dar um exit e posso fazer o seguinte.

04:10

Deixa eu aqui colocar com o fluxo antigo, eu coloquei um "--no rerank",

04:16

Aqui para mim, certo? E vou dar um enter aqui, beleza?

04:23

E agora eu vou perguntar de novo, como que é a pergunta? Como,

04:28

Deixa eu perguntar igual para garantir que não tem diferença,

04:32

Como funciona o programa de indicação, tá?

04:37

E o que vai acontecer aqui?

04:41

Ele vai trazer que, olha, não encontrei nenhuma informação,

04:45

Mas os quatro chunks de ruídos, eles foram para o modelo.

04:52

Deixa eu colocar um --debug aqui para a gente colocar, --debug. Vamos lá.

05:01

Como funciona o programa de indicação? Vamos lá.

05:12

Perceba que ele não encontrou a resposta.

05:16

Mas o grande ponto é que os chunks que ele encontrou aqui,

05:22

Ele enviou para o modelo. E aí que é o grande ponto. Por quê?

05:28

Porque antes, quando eu fiz o re-rank,

05:30

Ele eliminou os candidatos porque nenhum servia.

05:32

Aqui, como ele não eliminou, ele fez a consulta enviando...

05:38

Esses chunks, ou seja,

05:40

Foram um modelo de ruído que, no final das contas, não resolveu o meu problema.

05:45

Então, imagina que você nem tem informação,

05:47

Você manda oito chunks desses caras e ainda

05:50

Depois disso, você não tem informação suficiente.

05:53

Eu consigo abreviar isso por conta, nesse caso, do re-rank.

05:59

E aqui somente para nível de

06:03

curiosidade, eu posso colocar --menos, --show.

06:12

Prompt aqui para mim. E eu vou colocar aqui, ó.

06:17

Quanto custa o plano pro?

06:22

E aqui, o que acontece? Eu trouxe os prompts,

06:25

Somente para que você consiga ver o que aconteceu aqui que vai ser enviado.

06:30

Tem bastante informação, né? Então, o que acontece? Quanto custa o plano pro?

06:35

Aqui eu tenho o prompt do query planner que a gente precisa.

06:41

Ou seja, aqui tem o System Prompt,

06:43

As regras que foram feitas para gerar os exemplos que

06:47

A gente trouxe para ele conseguir fazer o planner.

06:50

Aqui tem a pergunta do humano, quanto custa o plano pro? Então,

06:54

Acabou o nosso prompt de sistema. Agora aqui... De sistema não, de query.

07:00

Aqui eu tenho o re-ranker prompt, ou seja, você é um sistema de re-rank aqui,

07:06

De um assistente de reg, você nunca vai responder perguntas,

07:10

Analise somente os candidatos de chunks abaixo.

07:13

E selecione somente os que são realmente dignos,

07:19

Realmente que valem a pena enviar para o modelo.

07:23

Regras. Selecione no máximo quatro chunks IDs, os primeiros quatro primeiro. Depois,

07:30

Somente os chunks que têm resposta, ajuda direta para a questão.

07:36

Prefira especificamente os chunks

07:38

Específicos em relação aos genéricos.

07:43

E prefira chunks que tenham palavras e termos exatos quando forem passados.

07:49

Retorne uma lista em branco se nenhum...

07:53

Chunk suportar a resposta. E use somente o chunk ID presente para os candidatos.

07:59

Então, aqui eu tive os candidatos,

08:02

Que é candidatos, chunk ID, pro plan, aqui para mim, o source,

08:05

O content, etc. Está vendo? Então, e aqui o conteúdo desse cara.

08:10

O outro chunk ID que foi enviado ali para o modelo.

08:15

O outro chunk ID que foi enviado para o modelo ali para mim.

08:21

O outro chunk ID. Então, ele trouxe aqui, basicamente,

08:24

Todos os chunks que foram pedidos para o modelo fazer o quê no final das contas?

08:30

Escolher os melhores candidatos dentre desses caras. E depois,

08:34

A gente tem o Final Answer Prompt. Então,

08:38

Você é um cara de suporte, as suas regras são essas.

08:41

O contexto. Você tem esse chunk ID, o conteúdo, o plano,

08:46

A sessão de perguntas e respostas. Esse cara do ProPlan. E acabou.

08:51

Ele trouxe apenas dois itens, basicamente,

08:56

Para responder à pergunta.

08:59

Lembrando que antes nós tínhamos oito caras aqui que seriam candidatos. Então,

09:06

Esses prompts conseguem mostrar para a gente aqui como foi o

09:10

Histórico desde o início até o fim em relação a tudo isso.

09:16

Está aqui um exemplo que eu trouxe de re-rank,

09:19

A gente vai falar sobre código e também eu quero falar sobre alguns outros

09:23

Aspectos também e trade-offs quando a gente está falando de re-rank.

## Resumo IA

[RESUMO_IA]