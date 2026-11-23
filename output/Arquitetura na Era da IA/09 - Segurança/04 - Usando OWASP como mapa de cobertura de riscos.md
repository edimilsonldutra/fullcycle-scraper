Módulo: Arquitetura na Era da IA\
Aula: [Usando OWASP como mapa de cobertura de riscos](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18842)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente pegou uma arquitetura que a

00:04

gente construiu e a gente criou um Threat Model,

00:06

no final das contas, né?

00:07

Esse Threat Model a gente conseguiu identificar os nossos Trust Boundaries,

00:12

as superfícies de ataque,

00:14

os controles que existem e também uma série de

00:17

riscos que ficaram registrados ali com os ID's,

00:20

né? De SEC 001, 002 e assim por diante, tá?

00:24

Eu já tinha falado, inclusive, um pouco sobre a WASP, nesse caso o GNI Security,

00:30

project deles, tá? Mas o grande ponto aqui é, né?

00:35

Eu acho que vale a pena não digo como que eu posso dizer se aprofundar,

00:42

mas eu acho que vale a pena dar uma reforçada em relação a esse cara aqui,

00:47

tá? Então aqui entra a história do ASP aqui pra gente,

00:51

tá? Então... Quando a gente olha ele,

00:54

ele acaba sendo uma referência que organiza dez grandes categorias

00:58

de risco para uma aplicação que usa um modelo de linguagem.

01:01

A versão, pelo menos atual,

01:03

ela inclui o quê no final das contas? O prompt injection,

01:07

sensitive information disclosure, excessive agency, supply chain,

01:14

data and model poisoning, unbounded consumption, misinformation,

01:20

hidden context. Então, Context Exposure,

01:23

Vector and Embedding Weakness,

01:26

e Improper Output Handling.

01:31

Mas eu não quero usar essa lista como se fosse um checklist,

01:35

onde a gente simplesmente coloca um check em 10 caixinhas ali.

01:39

A ideia é outra. Primeiro, nós olhamos para a nossa arquitetura.

01:44

Depois a gente usou o WASP para verificar se no nosso mapa possui pontos cegos. Por exemplo,

01:50

no nosso track model a gente identificou uma input boundary,

01:53

onde o conteúdo enviado pelo usuário entra na aplicação.

01:56

Quando a gente olha para o WASP,

01:58

a gente encontra prompt injection.

02:00

Então existe uma relação clara entre aquele boundary que

02:04

a gente identificou e uma categoria conhecida de risco.

02:07

Depois a gente tem o data e context boundary. No nosso reg de documentos,

02:13

passam, vários documentos acabam passando pela ingestão. Então,

02:17

eles são transformados em chunks, armazenados no PgVector,

02:20

recuperados, e finalmente a gente coloca ele ali no contexto do modelo.

02:24

Quando a gente olha para essa parte de arquitetura,

02:26

várias categorias do astro começam a aparecer. Por exemplo, a gente tem prompt injection,

02:31

quando uma instrução maliciosa chega indiretamente através de um documento.

02:36

Temos o data and model poisoning,

02:38

quando uma fonte de dados utilizada pelo sistema, ela é...

02:42

A gente tem o vector e

02:45

embedding weakness quando existem problemas de isolamento,

02:50

acesso ou confiança, por exemplo, no conteúdo armazenado e que é também recuperado.

02:56

A gente tem o Sensitive Information Disclosure,

02:59

caso essa cadeia termine expondo informações que eles não deveriam sair dali.

03:05

Então perceba que uma única boundary pode estar relacionada com vários riscos.

03:11

Da mesma forma, um único risco pode aparecer em vários pontos da arquitetura.

03:18

E é por isso que eu não quero,

03:19

Na realidade, organizar o nosso sistema simplesmente em LLM01.

03:25

Depois LLM02, depois LLM03.

03:29

A arquitetura raramente funciona dessa forma.

03:33

O nosso Threat Model continua sendo organizado em torno do sistema real.

03:38

O WASP funciona como uma lente que a gente coloca por cima dele.

03:42

A gente também tem o Model Output Boundary.

03:46

Aqui o modelo produz algo e a aplicação consome essa saída.

03:51

O WASP chama a atenção para... improper output handling. Então,

03:58

A gente tem, nesse caso, a estrutura de output ainda ajuda bastante,

04:02

Porque a gente pode garantir que determinada resposta

04:05

Possui os campos e os tipos esperados.

04:09

Mas isso não significa que os valores dentro desses campos sejam seguros.

04:14

Uma URL pode estar no formato correto e ainda

04:18

Apontar para um destino que não deveria ser permitido.

04:21

Um argumento de ferramenta pode ser uma string perfeitamente válida

04:27

E ainda representar uma operação que aquele usuário não pode realizar.

04:33

Então, novamente, a categoria do WASP não...

04:37

Substitui a análise arquitetural. Ela nos lembra de fazer determinadas perguntas.

04:44

Quando a gente chega, por exemplo, na Action Boundary,

04:47

Isso fica ainda mais evidente.

04:49

O nosso Support Triage Agent pode escolher ferramentas e,

04:55

Por exemplo, gerar efeitos. E aqui aparece o Excessive Agency.

05:00

Que na edição, pelo menos de 2026,

05:04

Está entre os maiores riscos ali que está sendo destacado.

05:08

O próprio Guia separa o cenário em que o modelo é

05:12

Apenas um componente daquele em que passa a atuar utilizando ferramentas,

05:18

Memória e produzindo consequências downstream. Para esses casos,

05:22

O ASP recomenda usar também o Top 10 for...

05:27

Agent Key Applications, tá? Então,

05:30

Isso acaba também se encaixando exatamente no nosso projeto.

05:34

Por quê? Porque para o nosso Knowledge Chat,

05:37

O ASP GNAI LLM Top 10 é a nossa principal referência.

05:42

Quando a gente analisa o Support Triage Agent,

05:46

A gente adiciona também a

05:47

Perspectiva do Agent Key Top 10.

05:53

Porque agora a gente tem a seleção de ferramentas,

05:56

Argumentos, permissões e ações, tá? Então, esse aí é um ponto.

06:01

E que, nesse caso aqui, é esse cara aqui, ó,

06:04

O Top 10 for Argentic Applications,

06:08

Aqui para 2026, tá? Então,

06:13

Que ele tem esse documento, eu vou deixar o link,

06:16

Mas aqui é a mesma pegada onde...

06:20

A gente separa a parte apenas de GNA e LLM e a gente acaba indo para o modo,

06:26

Vamos dizer, agêntico no meio de toda essa história. Então,

06:30

Isso acaba sendo mais um guia de referência.

06:35

Então, é por isso que quando você olha lá no nosso Threat Model,

06:39

A gente acaba vendo códigos diferentes ali no meio da história.

06:44

Por exemplo, deixa eu pegar aqui.

06:47

Deixa eu pegar esse cara aqui.

06:50

Cadê a nossa tabela?

06:54

Aqui, você pode ver o LLM01, LLM02, etc.

07:00

E o LLM09. Mas os outros aparecem como AS...

07:06

Aqui, I01, e a gente tem esses, cara, SI06,

07:10

e a gente acaba tendo esses pontos aí.

07:14

Esses códigos, no final das contas, que a gente acaba tendo,

07:18

não são necessariamente os nossos riscos, tá?

07:21

Eles são referências externas. O nosso risco continua sendo,

07:25

por exemplo, o SEC08, que a gente tem lá embaixo.

07:29

Ele tem ausência de autorização antes da execução de uma ferramenta, né? Então,

07:35

no final das contas, quando a gente navega nesses caras, o código ASI ali,

07:41

ele apenas ajuda a relacionar aquele risco específico

07:45

do nosso projeto com uma categoria mais ampla reconhecida,

07:49

então, pela comunidade. Então, essa diferença é importante.

07:53

Se amanhã a classificação do ASP mudar,

07:55

o nosso thread model não deixa de fazer sentido.

07:58

A arquitetura continua tendo uma decisão do agente chegando em uma ferramenta.

08:03

O risco continua existindo. Nós apenas utilizamos, vamos dizer assim,

08:08

um mapeamento externo. Existe mais um ponto interessante na edição,

08:12

pelo menos de 2026,

08:13

que é a orientação geral ficou muito alinhada com

08:18

o que a gente está fazendo nesse módulo.

08:20

Não projetar o sistema esperando que o modelo nunca seja enganado,

08:24

mas limitar o impacto quando isso pode acontecer no final das contas.

08:30

A própria documentação que a gente tem aqui,

08:32

inclusive, reforça que o prompt injection continua sendo um problema estrutural, porque as instruções...

08:39

Instruções e dados acabam chegando ao modelo dentro do mesmo fluxo de tokens. Então,

08:45

nossa estratégia durante a nossa próxima aula, no final das contas,

08:48

não é tentar construir um prompt perfeito.

08:51

A gente vai tentar atacar determinados limites e

08:54

a gente vai medir o comportamento atual.

08:56

Depois, a gente pode colocar controle fora do

08:59

modelo quando esses controles precisarem ser,

09:02

por exemplo, determinísticos.

09:04

E a gente também vai executar os mesmos cenários novamente.

09:08

A gente volta para o nosso thread model e

09:10

a gente verifica quais riscos foram reduzidos,

09:13

quais continuam em aberto e qual risco residual a gente decidiu aceitar. Então,

09:19

na próxima aula, a gente vai começar pelo primeiro desses riscos.

09:22

A gente vai entender o prompt injection e jailbreak,

09:25

por que eles não são exatamente a mesma coisa e, principalmente,

09:29

por que prompt injection não significa apenas

09:32

alguém escrever ignore a todas as instruções anteriores.

09:37

Fechou? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]