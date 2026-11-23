Módulo: Arquitetura na Era da IA\
Aula: [Intenção da pergunta antes do retrieval](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18442)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente melhorou o nosso pipeline

00:04

para que os chunks carreguem mais contexto, ou seja,

00:07

ao invés de indexar pedaços soltos do texto,

00:10

a gente começou a enriquecer cada chunk com as informações do título do documento,

00:14

o tipo do produto, o plano, a versão e a sessão.

00:17

Isso ajuda o retrieval porque o embedding passa

00:20

a representar melhor o significado daquele trecho.

00:23

Agora a gente vai dar um passo diferente.

00:25

Até aqui o nosso fluxo está mais ou menos assim. O usuário faz uma pergunta.

00:30

A aplicação manda essa pergunta e faz a busca vetorial,

00:33

recupera os chunks mais parecidos,

00:35

monta o contexto e chama o modelo. Esse fluxo funciona,

00:38

mas ele ainda parte de uma suposição perigosa,

00:42

que a pergunta do usuário está pronta para ser usada na busca.

00:46

E muitas vezes não está.

00:48

O usuário não pergunta pensando em retrieval, o usuário pergunta do jeito dele.

00:53

Às vezes ele usa uma palavra genérica,

00:55

às vezes ele usa uma sigla, às vezes ele mistura duas intenções na mesma frase,

01:00

às vezes ele presume um contexto que só existe na cabeça dele. Por exemplo,

01:04

se a pessoa pergunta, e se der algum problema grave no enterprise?

01:08

Para a gente, olhando a base,

01:11

talvez isso signifique qual é o SLA de incidentes P1 no plano enterprise.

01:16

Só que essa transformação não acontece automaticamente se a gente

01:19

simplesmente mandar a pergunta original para o banco vetorial. Então,

01:23

antes de buscar os chunks, pode existir uma etapa intermediária,

01:27

entender melhor a intenção da pergunta. Essa etapa não precisa ser algo complexo,

01:33

não precisa virar um agente, não precisa criar uma arquitetura enorme.

01:36

A ideia é ter um pequeno planejamento da consulta,

01:39

algo como um query plan. Esse plano pode dizer coisas como,

01:43

qual é a pergunta normalizada? Qual parece ser a intenção?

01:47

Que tipo de documento faz sentido buscar? Se existe algum plano mencionado?

01:52

Se tem algum termo exato importante?

01:54

Se a pergunta é ambígua? Por exemplo, uma pergunta.

01:57

Qual é o tempo de resposta para P1 no Enterprise?

02:00

Poderia gerar um plano simples.

02:04

Pergunta normalizada.

02:05

Qual é o SLA de resposta para incidentes P1 no plano Enterprise?

02:09

Daí ficaria. Tipo de documento? SLA. Plano? Enterprise.

02:14

Termos exatos, P1 e Enterprise.

02:17

Precisa de esclarecimento? Não. Então,

02:20

isso ajuda porque a aplicação passa a buscar melhor.

02:24

Em vez de tratar a pergunta como um texto qualquer,

02:26

ela começa a usar sinais da própria pergunta para configurar o retrieval. Agora,

02:32

cuidado com um ponto mega importante. O modelo pode ajudar a interpretar a pergunta,

02:38

mas ele não deve decidir sozinho o que o usuário pode acessar.

02:43

Essa separação é fundamental.

02:45

Se a aplicação tem regras de tenant,

02:47

produto, status, publicado, visibilidade, permissão,

02:50

isso precisa vir do sistema.

02:52

Não é o modelo que decide se pode buscar um documento interno,

02:55

se é um draft, se é privado ou qualquer coisa desse tipo.

02:58

O modelo pode sugerir que a pergunta... Parece ser sobre SLA ou sobre billing,

03:04

mas a autorização e o escopo de acesso são ainda responsabilidade da aplicação. Então,

03:11

essa camada de intenção não substitui a segurança,

03:14

ela melhora a busca. Um outro ponto importante é a ambiguidade.

03:19

Às vezes, a melhor resposta não é buscar, é perguntar de volta.

03:23

Se o usuário diz, como funciona...

03:25

o suporte no plano da empresa, isso pode significar enterprise,

03:30

pode significar o plano atual da organização,

03:32

pode significar uma condição contratual específica.

03:35

Se a aplicação não tem esse contexto, talvez ela não deveria fingir certeza,

03:40

ela deveria pedir esclarecimentos. E aí, isso muda a qualidade da experiência.

03:45

Ao invés de eu recuperar um chunk e gerar uma resposta confiante,

03:48

o sistema pode dizer,

03:49

Você quer saber sobre o suporte do plano enterprise ou sobre o plano atual da sua...

03:55

organização. E isso é uma mudança muito saudável,

04:00

arquiteturalmente falando.

04:03

Então, o próximo passo do nosso projeto vai ser

04:05

criar uma camada simples de planejamento da pergunta.

04:08

A gente vai fazer uma estruturação do output para

04:12

que o modelo devolva um objeto com campos bem definidos,

04:17

com uma pergunta normalizada, a intenção, o tipo do documento,

04:22

o plano, os termos exatos e a necessidade de esclarecimento.

04:26

Esse plano não vai resolver tudo, mas ele...

04:31

vai preparar o caminho para as próximas melhorias,

04:34

por exemplo, com uma busca híbrida, um re-ranking e também,

04:40

por exemplo, um query rewriting. Então,

04:42

a mensagem principal aqui é que o RAG, a pergunta do usuário,

04:46

não precisa ir crua direto para o retrieval.

04:50

Antes de buscar, a aplicação pode entender melhor a intenção,

04:53

detectar a ambiguidade e preparar uma consulta mais útil.

04:56

Então, vamos nessa para a gente ver esse query

04:59

planner simples que a gente vai fazer.

## Resumo IA

[RESUMO_IA]