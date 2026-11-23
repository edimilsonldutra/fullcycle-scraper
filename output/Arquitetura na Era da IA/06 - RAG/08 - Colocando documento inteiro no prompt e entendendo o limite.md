Módulo: Arquitetura na Era da IA\
Aula: [Colocando documento inteiro no prompt e entendendo o limite](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18410)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, e agora a gente vai dar mais um passo, tá?

00:04

E é aqui que a coisa começa a ficar um pouco

00:08

mais chata quando nós não temos RAG ou outros mecanismos para trabalho, tá? Então,

00:14

o que acontece é o seguinte.

00:16

Eu tenho agora aqui um arquivo que eu chamei de Context Chat. Se você olhar,

00:22

eu tenho um prompt de instrução.

00:26

E eu estou falando qual que é o meu documento principal,

00:28

que é o Product Support SLA aqui para mim,

00:31

buscando na minha pasta Knowledge Base, que basicamente é esse aqui,

00:35

Product Support SLA. Então eu tenho esses documentos aqui,

00:39

é um documento pequeno de forma geral,

00:40

depois eu vou pedir para a IA gerar esse documento maior aqui para a gente.

00:44

Mas o grande passo e o grande ponto aqui é que eu tenho as minhas instruções,

00:49

que estão falando aqui para ele responder às perguntas,

00:53

etc., e responder sempre em português.

00:56

Aqui tem load document, ou seja,

00:58

ele vai carregar o documento e aqui ele vai inicializar

01:01

a aplicação que nem a gente já tinha feito.

01:02

Por outro lado, o que acontece?

01:06

Olha só, e aqui que é um ponto importante. No system message,

01:09

eu tenho a minha instrução que eu passei, que são essas instruções,

01:15

e depois eu pulo linha e tenho o

01:19

documento e eu passo os dados do meu documento.

01:23

Ou seja, eu coloco o nome aqui do meu documento. E aí, o que vai acontecer?

01:31

Na hora que eu for conversar aqui e fazer as perguntas,

01:36

nesse momento eu consigo fazer

01:38

perguntas específicas sobre esse documento,

01:43

que nesse caso é o de suporte, de SLA. E aí a gente começa a perguntar,

01:48

que é algo óbvio, porque está no prompt, mas isso aí já vai nos ajudar. Então,

01:53

eu vou colocar aqui um Python -m e aqui

01:57

eu vou dar um context -chat aqui para a gente.

02:02

E agora, ele falou, carreguei o documento Product Support SLA.

02:07

E eu vou perguntar, qual é o SLA de vocês?

02:17

E aqui ele coloca, olha só.

02:20

O SLA de suporte do produto da FCAI Cloud, que é a nossa empresa fictícia,

02:25

é definido de acordo com o plano contratado e a severidade do chamado.

02:29

P1, P2 e P3. Plano Starter, Plano Pro e Plano Enterprise.

02:34

Além disso, o Plano Enterprise, o SLA e etc.

02:37

Mas, como funciona?

02:41

Mas, quais são os planos?

02:47

Vou colocar novamente aqui.

02:49

Está vendo? Então aqui, o documento menciona três planos. Então,

02:52

já dá para perceber que o documento menciona que é um prompt mal feito,

02:57

porque a IA deveria colocar os planos são esses,

03:00

não falar que o documento menciona. Mas se você perceber,

03:04

a coisa aqui é a coisa mais boba do mundo,

03:06

que é pegar as minhas instruções e embedar junto,

03:12

embedar não de banco de dados,

03:13

mas colocar o conteúdo inteiro do documento aqui dentro.

03:18

E, novamente, é um ponto importante para você saber. Muitas vezes,

03:22

Fazer isso dá certo e funciona e é recomendável.

03:26

São documentos longos de contexto que vão ajudar.

03:30

E daí você pode perguntar, Wesley, mas toda hora que chamar vai gastar token?

03:34

Depende, você pode colocar isso num cache.

03:37

E aí você vai ter um desconto gigantesco na hora

03:39

de chamar o provider e coisas desse tipo.

03:42

Então não é porque o seu prompt inicial é

03:44

grande que necessariamente ele vai ser mais caro,

03:47

principalmente se você souber utilizar o cache do provider.

03:51

Agora, o grande ponto de tudo isso é manter esse documento

03:54

atualizado e quando esse documento começa a ficar muito grande,

03:58

aí sim... A gente começa a ter esses problemas de cache,

04:01

a gente tem problemas de atualização,

04:03

e aí a gente começa a entrar num lugar que começa a ficar cada vez mais inviável,

04:08

você pegar um prompt gigante e colocar ali para a IA navegar e ler.

04:14

Vamos imaginar que eu quisesse fazer uma pergunta sobre, sei lá, a Bíblia.

04:18

Imagina eu pegar a Bíblia inteira e colocar num prompt. Não dá para fazer isso.

04:21

Vai estourar a janela de contexto, a gente vai ter todos os problemas do mundo.

04:24

E fora que às vezes a pessoa vai querer saber uma

04:26

coisinha e para isso ela tem que ler tudo,

04:29

então não faz sentido muitas vezes, mas quando às vezes eu tenho um,

04:36

dois documentos mesmo que eles sejam um pouco grandes

04:38

e não vai mudar muito dependendo da situação,

04:41

é mais fácil trabalhar dessa forma,

04:43

do que necessariamente fazer um reg, etc, com um monte de banco de dados,

04:47

então você tem que pensar muito bem,

04:49

porque nem sempre a melhor solução é reg,

04:52

às vezes fazer isso que a gente acabou de fazer,

04:53

funciona tranquilamente. Fechou? Então,

04:57

somente para a gente seguir passo a passo o que a gente acabou de fazer,

05:00

a gente simplesmente colocou no contexto da IA as nossas informações,

05:05

além da informação que ela já é treinada. Então,

05:08

agora ela consegue responder de forma contextual para a gente.

## Resumo IA

[RESUMO_IA]