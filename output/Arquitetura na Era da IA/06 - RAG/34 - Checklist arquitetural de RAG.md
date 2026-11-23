Módulo: Arquitetura na Era da IA\
Aula: [Checklist arquitetural de RAG](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18455)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente falou sobre soluções prontas de providers e

00:05

sobre decisão entre construir o próprio pipeline ou usar uma solução gerenciada.

00:12

Agora, para fechar esse capítulo,

00:14

eu quero deixar uma checklist arquitetural simples para você

00:17

usar antes de colocar um RAG em produção.

00:21

Então vamos lá, a primeira pergunta é,

00:24

o problema é realmente de recuperação de conhecimento?

00:27

Se a resposta depende de documentos, políticas, manuais, PACs,

00:32

contratos, documentação interna ou base de conhecimento,

00:36

o RAG pode fazer sentido.

00:38

Mas se a resposta depende do estado atual do sistema...

00:43

como o último pagamento, o status da assinatura,

00:47

o uso em tempo real ou dados transacionais,

00:51

provavelmente o caminho é o mais padrão. O famoso SQL,

00:55

fazer chamadas de API, trabalhar com tool calling.

01:01

Segunda pergunta é, qual é a fonte da verdade?

01:04

O modelo não deve ser a fonte de verdade.

01:08

O Vector Store também não deve ser essa fonte.

01:12

A fonte da verdade continua sendo sempre o documento,

01:16

o banco, a API ou o sistema oficial ali da empresa.

01:21

O índice vetorial é uma cópia preparada para busca.

01:25

Se isso não estiver claro, o RAG vira uma caixa preta extremamente perigosa.

01:32

Terceira pergunta. A base cabe no contexto? Se você tem um documento pequeno...

01:38

estável e barato de mandar no prompt, talvez você não precise de RAG.

01:44

Pode ser, vamos dizer assim, que a gente tenha o conceito de long context,

01:51

ele vai resolver. Pode ser que cache vá resolver.

01:55

O RAG começa a fazer mais sentido quando a base cresce, muda,

02:00

precisa de busca muito seletiva, ponte, filtros, versões e permissões.

02:06

Então, esse aí é um outro ponto que você tem que levar em consideração.

02:09

A quarta pergunta é,

02:11

quem pode acessar o quê? Antes de recuperar o contexto,

02:16

a aplicação precisa saber o escopo do usuário,

02:19

o tenant, o produto, o plano, o status,

02:22

a visibilidade e a permissão. Elas não podem,

02:26

vamos dizer assim, deixar para que o modelo decida.

02:30

Então lembre-se, isso é responsabilidade da aplicação.

02:34

Similaridade, ela não é autorização. Tome muito cuidado.

02:39

A gente vê hoje em dia grandes problemas de vazamentos de informação,

02:43

mesmo em empresas gigantes,

02:45

porque provavelmente houve um problema de escopo do que o usuário podia acessar,

02:51

mas na hora de bater nesse banco de dados,

02:53

o modelo trouxe a informação e veio para quem não deveria. Esse é um outro ponto.

02:58

A quinta pergunta é... Como a base muda?

03:02

O documento muda, a política muda, o SLA muda,

03:05

o status vai mudar. Então, se você não tem uma estratégia de reindexação,

03:10

hash, versão ou manifest, uma hora o RAG vai responder com informação antiga. Então,

03:17

o pipeline de ingestão precisa ser parte

03:21

da arquitetura e não um script ali esquecido.

03:25

Sexta pergunta é... Como que eu vou medir se o retrieval está bom?

03:30

Não basta olhar a resposta final.

03:33

Você precisa enxergar a pergunta normalizada, os filtros aplicados,

03:38

os chunks recuperados, os scores, os chunks selecionados,

03:42

as fontes usadas e o prompt final em ambiente de debug. Sem isso,

03:47

você não sabe se o erro veio do documento,

03:51

do chunking, do retrieval, do re -ranking ou do modelo.

03:54

A sétima pergunta.

03:56

O sistema sabe não responder?

04:00

Um RAG confiável não é aquele que responde tudo.

04:04

É aquele que responde quando tem evidência suficiente e recusa quando não tem.

04:09

Uma recusa clara,

04:11

ela sempre vai ser melhor do que uma resposta inventada com confiança.

04:15

A oitava pergunta é, qual é o custo?

04:18

O RAG adiciona custos de embedding, armazenamento, retrieval,

04:24

re -ranking, tokens de contexto e geração.

04:27

Se você recupera contexto demais, pode deixar a aplicação mais cara e mais lenta.

04:31

Então, o pipeline precisa ser pensado também em termos de latência,

04:36

tokens de entrada, tokens de saída e modelo utilizado.

04:41

A nona pergunta. Eu preciso construir ou posso usar uma solução pronta?

04:47

Se o caso é padrão,

04:49

com documentos comuns e pouca customização,

04:52

uma solução gerenciada pode acelerar muito.

04:55

Mas você precisa ter controle fino sobre chunking,

04:59

permissões, metadados, indexação e o prompt final.

05:03

Então, se você precisa disso, talvez construir faça mais sentido.

05:08

Em muitos cenários, o melhor caminho é o híbrido. E a última pergunta é,

05:14

eu consigo explicar por que uma resposta foi dada?

05:18

Se você não consegue rastrear... a resposta até os documentos usados,

05:24

o sistema ainda não está maduro. O RAG em produção precisa de rastreabilidade,

05:30

não necessariamente complexidade enorme, mas ele precisa ter clareza.

05:35

Então, fechando esse capítulo,

05:37

a ideia principal é que o RAG não é um banco vetorial com o LLM.

05:42

RAG é uma arquitetura de recuperação de contexto. Ele envolve fonte da verdade,

05:47

ingestão, metadados, permissões, retrieval, seleção de contexto,

05:52

resposta, fontes, observabilidade e custo.

05:56

Se você sair desse capítulo entendendo isso,

05:59

já muda completamente a forma de você olhar para as aplicações que utilizam IA.

06:05

Porque o objetivo não é... usar o RAG por moda ou porque é comum nos serviços,

06:11

nos providers. O objetivo é entregar o contexto certo para o usuário certo,

06:15

no momento certo, com rastreabilidade suficiente para confiar na resposta.

06:22

Um grande abraço e espero que você tenha curtido.

## Resumo IA

[RESUMO_IA]