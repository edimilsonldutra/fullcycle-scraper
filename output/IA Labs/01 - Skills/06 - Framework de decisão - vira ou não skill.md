Módulo: IA Labs\
Aula: [Framework de decisão - vira ou não skill](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18272)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, então, continuando aqui, vamos falar agora sobre skills,

00:05

mas especificamente sobre como a gente deve tomar

00:09

essa decisão de virar skill ou não virar skill.

00:15

Creio que isso seja o próximo tema aí que pode vir na cabeça de vocês.

00:21

Afinal de contas, a gente entendeu que é uma skill.

00:24

A gente já entendeu como criar uma skill, o que é o tal do front matter.

00:29

Agora que a gente já tem essa base um pouco mais sólida,

00:34

temos que responder uma resposta que é muito chave.

00:39

Quando eu vou criar uma skill?

00:43

Quando eu não vou criar uma skill?

00:46

Inclusive, eu vou mostrar uma forma muito interessante de a gente

00:50

tomar esse tipo de decisão e a gente vai utilizar também.

00:54

O auxílio da IA para nos ajudar. Beleza? Então, vamos lá. Bom, pessoal,

01:01

aqui eu vou demonstrar para vocês um modelo

01:05

mental que acho que faz muito sentido vocês,

01:10

a partir de hoje,

01:11

já começar a estruturar nos projetos que vocês estão trabalhando.

01:17

A primeira coisa é muito importante dizer que, quando a gente fala de skills,

01:22

é bem provável que você vai ou ter uma

01:27

base de uma skill que você pode sempre reutilizar,

01:31

mas é certo que você vai pegar

01:35

essa base e vai fazer as customizações necessárias,

01:39

gerando uma nova skill por projeto. Porque cada projeto tem as suas convenções,

01:45

tem as suas configurações, tem a sua arquitetura, tem, enfim, inúmeras coisas ali.

01:52

Que são específicas ao projeto. Então, é muito provável que,

01:58

mesmo que a gente saiba que uma skill

02:00

seja uma habilidade que seja totalmente reutilizável,

02:04

dado a essa diferença de projetos que nós temos,

02:08

formas de programar e tudo mais,

02:11

a gente vai ter que adequar alguma coisinha ou

02:13

outra para garantir que ela siga as nossas convenções.

02:19

Primeiro ponto já esclarecido. Segunda coisa.

02:22

Se eu pudesse falar para vocês como fazer essa triagem,

02:27

seria através de uma frase.

02:30

Então, a triagem seria igual ao quê?

02:35

Isso é conhecimento procedural

02:41

reutilizável? Se

02:47

isso aqui for respondido, a gente já tem um bom ponto.

02:53

E aí, se você quiser adicionar mais uma questão a ser analisada nessa pequena frase,

02:59

é o seguinte, além

03:02

desses dois pontos aqui, é

03:07

estável ou bastante para

03:11

valer um arquivo

03:15

versionado? Ou seja,

03:18

aqui eu estou falando mais a nível de análise daquilo que você quer executar.

03:26

Aqui eu já estou falando mais a nível de design, de fato.

03:35

Compensa a gente ter mais um arquivo dentro do nosso projeto,

03:40

versionar mais coisas só para ter aquele ganho,

03:45

isso aí é essa triagem que a gente tem que começar a pensar, beleza? Se

03:53

ainda assim, depois dessa reflexão que você fez, as coisas não clarearam ainda,

03:59

Tenta de uma outra forma. Seria assim, o

04:03

Negócio é o seguinte, vale... 3 SIMs. Reutilização.

04:14

Procedimento. Não óbvio. Estabilidade.

04:20

Vou botar aqui. 2 pontinhos.

04:23

Reutilização. É

04:26

repetitivo? Ou

04:29

Seja, faço isso aqui dias,

04:32

diversos prompts iguais, diversos projetos iguais. Se sim, bom ponto.

04:40

Procedimento não óbvio.

04:43

Tem um como específico? Ou seja,

04:46

a ordem de execução, padrão de time, convenções,

04:52

PEPs específicos a serem explorados, que o Cloud Code,

04:57

neste caso, o nosso Harness, não consegue acertar sozinho?

05:03

Ou seja, se o modelo já faz bem,

05:07

sem nenhum tipo de instrução a mais, provavelmente você não precisa de uma skill.

05:13

Agora, se o modelo está pecando nisso aí,

05:16

aí já é mais um sim. Então, o que a gente pode colocar aqui?

05:21

Tem um como específico. Esse como pode ser ordem,

05:27

padrão, uma convenção.

05:31

E, por fim, estabilidade. Ou seja,

05:36

ela é, por exemplo, uma regra que dura semana, dias, semanas,

05:46

meses.

05:49

Se sim, mais um ponto.

05:51

Se não, é bem provável que você não precise de uma skill.

05:57

Depois que você fez essa análise dos três SIMs aqui, pode

06:04

colocar mais uma análise, tá? E essa análise pode ser feita tanto com essa pergunta,

06:08

tanto com a técnica dos três SIMs. Que é o quê?

06:14

Segurança. Isso aqui é válido para

06:18

ambas as formas de pensamento.

06:26

Segurança. Tem algum tipo de segredo?

06:30

Algum credencial?

06:33

Algum token?

06:35

Algo que

06:38

depende de estado em tempo real, por exemplo? Se

06:45

isso aqui for

06:47

um SIM, você não vai fazer skill. Certo?

06:53

Por quê? Porque aqui é procedimento de segurança.

06:56

Então, se...

06:58

esbarra em algo voltado ao que está sendo perguntado,

07:03

já descarta. Mesmo que a gente tenha três SIMs aqui em cima,

07:08

mesmo que o resultado dessa triagem mental sua foi positivo para criar uma skill.

07:15

Afinal de contas, segurança é sempre bem-vinda.

07:20

Fechou? Só que agora a gente tem um outro ponto também a ser analisado. Por quê?

07:27

Quando a gente está fazendo essa triagem mental,

07:30

existem alguns itens que a gente deve ter algumas atenções.

07:34

Por quê? Porque existe uma zona cinzenta, poderia-se dizer,

07:38

entre as nossas skills e alternativas que a gente tem hoje. Como, por exemplo, volta MD,

07:47

algo determinístico, linter, um formatter,

07:50

um MCP tools, alguma busca.

07:56

externa, via tools de web e coisas nesse sentido.

08:00

Enfim, a gente tem algumas alternativas

08:05

quando nós estamos comparando determinado procedimento.

08:10

E é aí que mora uma zona cinzenta que a gente precisa analisar com muito carinho. Por quê?

08:17

Bom, basicamente, a ideia é quando

08:23

o procedimento, aquela

08:26

execução, vou colocar também para ficar fácil.

08:30

É repetível.

08:33

E não, óbvio, é

08:36

Skill 100%. Agora,

08:39

vamos supor que eu preciso ter uma source of truth ali.

08:47

Algo que sempre é verdade para aquele projeto.

08:50

Aí você não vai precisar de uma skill. Neste caso,

08:54

é muito melhor a gente trabalhar com um cloud.md, um agents.md.

09:00

Porque eu tenho a garantia de que o Harness vai sempre lê-lo.

09:05

E é como a gente já percebeu, a skill pode ou não ser lida.

09:11

Quando eu tenho, por exemplo, uma regra mecânica,

09:14

como eu disse, linters, formatters,

09:17

é bem provável que eu não precise também separar isso para dentro de uma skill.

09:22

Eu posso fazer com que a minha skill utilize o linter.

09:28

Isso é bem interessante, inclusive.

09:31

Agora, precisar de fato separar esse procedimento, essa execução,

09:36

criar as instruções para gerar uma skill disso,

09:40

é bem provável que você não precise. Da mesma forma,

09:45

quando eu tenho a necessidade de trabalhar com acesso a dados externos,

09:50

ou acesso a dados vivos,

09:52

poderia fazer isso via tools, via MCP. Então,

09:56

eu não tenho necessidade de criar uma skill para isso.

10:00

Mesmo que uma skill possa utilizar, via linha de comando,

10:04

um MCP Tools, por exemplo. Então,

10:07

perceba que a gente tem essa zona cinzenta, mas mesmo tendo essa zona cinzenta,

10:13

nós temos ali algumas definições bem claras de cada coisa.

10:20

O que cada um tem,

10:23

quais são as diferenças, quando eu posso utilizar ou não. Beleza?

10:30

E agora, para a gente fechar,

10:32

nós temos um outro assunto que é bem importante de debater. Que é o quê?

10:40

Decisão. Qual a minha estrutura de decisão para realmente eu,

10:45

depois que fiz essa triagem,

10:47

vi que não está batendo na zona cinzenta, vamos colocar aqui, o

10:56

que eu tenho que fazer? Tenho que tomar a minha decisão. Beleza. Vira uma skill. Qual nível?

11:03

Será que eu vou... trabalhar mais com nível 1, provavelmente você não vai trabalhar.

11:08

Mas será que eu vou trabalhar mais no nível 2 ou no nível 3?

11:14

Então, vai virar uma skill.

11:18

Se isso for acontecer, qual

11:20

nível? N2 ou N3? A gente sabe que... A partir do N2,

11:27

a gente tem o corpo ali que está sendo lido. A partir do N3,

11:30

a gente tem as nossas referências, a gente tem os nossos arquivos externos,

11:33

scripts e tudo mais. Então, a gente também tem que fazer essa análise,

11:38

essa triagem para ter consciência daquilo que vai ser feito.

11:44

Não é só sobre as instruções que estarão no corpo,

11:47

e sim as referências e tudo mais que compõem.

11:50

No final das contas, uma skill. E aí...

11:53

Para ajudar vocês nessa decisão, eu tenho aqui um pequeno prompt.

12:00

Este prompt vai ser meio que um revisor,

12:05

onde vai te dar uma triagem do que vale a pena ser skill ou não.

12:11

É como se fosse um quality gate.

12:14

Então, estou aqui com a minha sessão do Cloud aberta.

12:19

Vou colar aqui e

12:24

vamos dar uma olhada nesse cara.

12:27

Então, basicamente, tenho

12:30

aqui o meu prompt de triagem,

12:32

onde eu digo que ele é um revisor. Tenho aqui o meu candidato.

12:36

E esse meu candidato vai ser o local no qual eu vou colocar aqui as informações que

12:40

eu quero que faça uma análise para dizer se é viável ou não ele virar uma skill.

12:47

E aí, após isso, o que eu faço?

12:50

Eu pego aquela estrutura de decisão que eu mostrei aqui em cima para vocês e...

12:55

Faço as minhas perguntinhas. Após isso,

12:58

peço para ele formatar aqui uma resposta com um veredicto e tenho

13:06

o meu resultado. Na prática, como

13:10

que usa isso? Muito simples. Eu venho aqui,

13:13

troco essa parte e simplesmente eu posso fazer a minha pergunta.

13:19

Exemplo, candidato aplicar, por exemplo, um checklist.

13:25

Code review no meu time.

13:30

Utilizando, por exemplo, a parte ali de segurança, names,

13:36

convenções, a

13:40

partir de um diff. O que eu vou fazer?

13:46

Copiar esse cara aqui,

13:47

que inclusive pode virar uma skill, e vamos ver qual que é o resultado.

13:53

Ou seja, olha só, preditivo, virar uma skill.

13:58

Da mesma forma, inclusive, ele já até identificou, olha só que legal,

14:03

que a gente já tem aquela skill do Team Code Review.

14:08

Vamos fazer um new aqui. Da mesma forma que, vamos

14:13

pensar numa situação de candidato aqui.

14:19

Por exemplo, qual

14:23

versão de uma biblioteca? Por exemplo, Next.js.

14:31

Venho aqui, colo, e

14:35

aqui eu tenho meu resultado, ou seja, não vira.

14:41

Algo um pouco mais voltado à convenção,

14:44

para não ser algo tão óbvio, vamos dar um new aqui, e

14:48

vamos definir uma convenção, por exemplo, de Python.

14:54

De Python não, de qualquer linguagem de programação, por exemplo,

14:57

ao invés de tab, usar espaço. Usar espaço

15:00

de indentação.

15:05

No projeto. Vamos copiar e colar.

15:13

Vamos ver o que vai acontecer.

15:17

Mais um veredito. Não vira. E por que? Porque a gente tem.

15:22

Algo que já faz isso para a gente. Que é o nosso linter.

15:26

E aí a gente pode também testar aqui. Por exemplo,

15:31

sempre responder em português.

15:35

Do Brasil. Que acaba entrando.

15:38

Naquela linha cinzenta. Porque muitas das vezes.

15:42

a gente deve colocar essas informações, que são sempre verdade,

15:47

no nosso cloud.md. Olha só, não vira. Então,

15:54

destino certo acaba sendo o cloud.md,

15:56

conforme a gente já havia esperado. Então, com este carinha aqui,

16:03

a gente consegue já ter uma ideia do que pode e do que não pode ser uma skill. Fechado?

## Resumo IA

[RESUMO_IA]