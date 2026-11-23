Módulo: Arquitetura na Era da IA\
Aula: [O mini-projeto Support Triage Agent](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18799)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente começou a falar sobre

00:04

Avaliação de Tool Calling e Agente Simples.

00:06

A gente viu que quando a IA deixa apenas

00:10

de responder e começa a escolher ferramentas, a avaliação muda.

00:13

Agora não basta olhar só para a resposta final,

00:16

a gente precisa olhar também para a ferramenta escolhida e tudo mais.

00:20

Agora eu quero apresentar o mini projeto que a gente vai usar para isso, tá?

00:26

A gente não vai criar uma disciplina inteira de agentes aqui,

00:29

a ideia é bem mais controlada.

00:30

Construir um agente simples de triagem de suporte para o nosso FCAI,

00:35

AI Cloud, né? E ele vai existir dentro do mesmo projeto que a gente já vem usando,

00:43

porque o objetivo é reaproveitar o contexto, as configurações,

00:46

o Langchain, o Langfuse, os datasets e tudo mais.

00:49

Então não vamos criar um repositório do zero. A gente não vai abrir uma stack nova.

00:54

A gente não vai subir um ambiente separado.

00:56

Esse agente vai ter três ferramentas principais.

01:00

A primeira será Search Knowledge Base,

01:03

com underline entre o nome das funções, claramente.

01:07

Ele representa a busca da base de conhecimento.

01:10

Se o usuário perguntar algo como qual é a SLA para P1 no Enterprise,

01:14

o agente deve entender que isso é uma pergunta de

01:17

documentação e vai usar a base de conhecimento.

01:20

A segunda ferramenta será o Get Current Usage.

01:24

Ela representa uma consulta de uso atual do cliente.

01:28

Aqui a diferença é importante.

01:30

Se o usuário pergunta quanto de ingestão eu usei esse mês,

01:35

isso não é conhecimento documental. Isso parece dado vivo do sistema.

01:40

Então, em vez de responder com o reg,

01:42

o agente deve chamar uma ferramenta que simula,

01:45

por exemplo, uma API ou uma consulta de uso atual.

01:49

A terceira ferramenta vai ser o Create Support Ticket.

01:52

Ela representa uma ação. Se o usuário diz, abra um chamado P1,

01:57

porque o painel está fora do ar para todos os usuários,

01:59

o agente deveria criar um ticket de suporte com

02:02

a severidade correta e um resumo ali coerente.

02:06

Com essas três ferramentas,

02:08

a gente consegue demonstrar o que realmente muda na avaliação. No reg,

02:12

a gente avalia se o sistema recuperou os documentos

02:14

certos e respondeu com base no contexto.

02:17

Agora, no agente, a gente também vai avaliar se ele escolheu a ferramenta certa.

02:21

Por exemplo, uma pergunta sobre SLA deveria usar o Search Knowledge Base.

02:25

Uma pergunta sobre consumo atual deveria usar o Get Current Usage.

02:29

Um pedido claro para abrir um chamado deveria usar o Create Support Ticket.

02:34

E um pedido ambíguo sobre 'abra um chamado urgente aí...'

02:39

Talvez não deveria criar nada imediatamente,

02:41

o agente deveria pedir mais informação porque

02:43

o urgente sozinho não define severidade,

02:45

impacto, plano ou escopo.

02:47

Então esse aí é um ponto importante, a ferramenta existe,

02:50

Mas isso não significa que ela deve ser chamada sempre.

02:53

Parte da qualidade do agente está em saber agir e quando pedir esclarecimento.

02:59

O dataset desse mini projeto vai ser diferente do dataset do RAG.

03:04

Ele não vai ter apenas perguntas, termos esperados e a fonte esperada.

03:10

Ele vai ter campos como ferramentas esperadas,

03:12

ferramentas proibidas, argumentos esperados,

03:15

máximo de passos e se o agente deveria pedir esclarecimento.

03:18

Por exemplo, no caso de uma abertura de um P1,

03:21

o dataset pode dizer que a ferramenta esperada é o CreateSupportTicket,

03:26

que o argumento Severity deve ser P1 e que

03:29

o agente não deveria chamar o GetCurrentUsage. Então,

03:33

essa aqui é uma ideia básica para vocês. A trajetória,

03:37

somente para a gente lembrar, isso vai preparar, no final das contas,

03:41

a gente para avaliar a nossa trajetória.

03:45

A trajetória é o caminho que o agente tomou. Quais ferramentas ele chamou,

03:49

em qual ordem, quais passos ele executou, chamou algo desnecessário,

03:53

chamou a ferramenta certa e etc.

03:55

Esse é o tipo de avaliação que não aparece quando

03:58

a gente olha só para o texto final.

04:00

Então, nesse mini projeto, o objetivo não é criar um agente mais poderoso possível.

04:04

O objetivo é criar um agente pequeno, controlado e avaliável. Então, vamos nessa.

## Resumo IA

[RESUMO_IA]