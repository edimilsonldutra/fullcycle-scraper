Módulo: Arquitetura na Era da IA\
Aula: [Avaliando tool selection argumentos e trajetória](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18804)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem? E aqui a gente entra no Evolve Agent Dataset.

00:07

Da mesma forma como a gente fez lá com o Pipeline para a gente fazer o Agent,

00:12

a parte dos Datasets do Reg, a gente tem agora com o Agente.

00:17

Mas em relação ao nosso Agente, o que acontece?

00:20

Vamos imaginar o seguinte, vamos imaginar a seguinte situação.

00:24

Se eu faço aquela pergunta, quanto usamos de ingestão esse mês?

00:28

E o agente responde, 1320 GB, 88% da cota. É a resposta perfeita,

00:34

mas só que se ele tiver inventado esse número em vez de consultar o sistema,

00:39

você não tem como saber isso só olhando a resposta. Ela é idêntica nos dois casos.

00:44

O que separa os dois é a trajetória. Ou seja, o Get Current Usage,

00:51

ele foi chamado ou não? Então, esse tipo de coisa muda completamente.

00:55

Porque agora a gente tem outros critérios,

00:59

se você for olhar. Que no final das contas,

01:02

se eu pegar aqui meus... Acho que é score labels.

01:08

Evolve agent, né?

01:12

Score labels. Aqui, ó. Então,

01:14

são esses caras que a gente vai usar. Agent tool selection,

01:18

agent forbidden tools, agent argument match, trajectory match.

01:23

Max steps, clarification, refusal, ticket creation, expected terms.

01:26

Esses caras aqui vão ser os caras que eu vou dar, de forma geral,

01:30

o score para que eu consiga fazer aquela medição que eu estava querendo.

01:34

E se você perceber,

01:35

todo esse cara aqui, de forma geral, acaba, muitas vezes, não usando o modelo.

01:44

Porque, nesse caso,

01:45

a gente tem um ponto bem determinístico no

01:49

meio dessa história em relação ao critério.

01:52

que eu vou olhar, eu consigo verificar claramente,

01:55

eu não preciso de um juiz para me

01:58

dizer necessariamente todos esses detalhes e ficar comparando,

02:03

né? Então, esse aí é o ponto importante, tá? Então,

02:06

a nossa ideia é quando a gente consegue determinar

02:10

e entender quando a gente está trabalhando.

02:12

Como que a gente faz isso, no final das contas,

02:15

tá? É o Python -m AppEvolveAgent, tá? Então...

02:20

O que vai fazer, no final das contas, é ele vai rodar esses caras, tá?

02:27

E depois ele vai trazer quais são os casos que ele encontrou como se fosse,

02:32

como que eu posso dizer, com as respostas. Então,

02:37

se eu rodar aqui Python -m AppAgent,

02:40

tá? Ele vai pegar, ele está resetando.

02:43

Os nossos tickets de suporte para a avaliação,

02:45

porque esses tickets eles ficam armazenados ali localmente, né?

02:50

E agora ele está rodando o agente.

02:53

E o interessante é que ele roda o agente, como a gente tem essas informações claras,

02:57

a gente consegue de forma determinística saber o que deu certo, o que não deu certo,

03:02

baseado naquele nosso dataset, tá? Então isso aí é um ponto importante, tá?

03:09

Deixa ele aguardar aqui.

03:15

Vamos lá, mais alguns segundinhos. Ele tem 20 caras para fazer análise, né? Então vamos lá.

03:28

E pronto, agora ele rodou, né? Então vamos analisar os casos aqui,

03:32

ó. Tool Selection, 18 de 20, ok?

03:36

Forbidden Tools, 20 de 20, isso foi muito bom, ou seja,

03:39

Ele nunca tentou chamar uma ferramenta que ele não gostaria de ter chamado.

03:42

Argument Match, 3 de 5, ou seja... duas vezes o cara,

03:47

Ele não conseguiu passar os argumentos certos na nossa ferramenta.

03:52

Trajectory match, 18 de 20, ou seja, ele seguiu, ele não seguiu duas vezes esse cara.

03:57

Max steps, 20, ok, clarification, 18 de 20, refusal, 0 de 3,

04:03

Ticket creation, 18 de 20, expected terms, 8 de 8.

04:06

E aqui ele traz onde que ele falhou, o agent tool selection, agent argument match.

04:12

Ele trouxe quais são os casos que ele não colocou. E se eu chegar aqui e

04:19

abrir o meu Lang Fuse, eu

04:22

vou ter exatamente aquilo que a gente já viu, né? Ou seja, eu tenho as minhas notas.

04:28

Aqui nos termos,

04:29

basicamente a mesma coisa que a gente realmente já teve experiência anterior.

04:34

Mas a diferença agora é que eu tenho trajetória,

04:37

eu tenho os passos, eu tenho clarificação, eu tenho os argumentos,

04:41

se eles foram passados corretamente,

04:43

e eu consigo saber onde eu tive exatamente um determinado problema.

04:48

Então, isso aí acaba fazendo uma baita diferença quando a gente vai trabalhar.

04:53

Então, isso aqui... Vamos dizer, galera, vale ouro,

04:58

porque é a forma de a gente conseguir realmente verificar se

05:01

um agente está trabalhando decentemente aqui para a gente.

05:05

Então, argument match, esse cara aqui não bateu. Então,

05:08

a gente começa a ver e entender onde estão os nossos problemas e tudo mais.

05:13

Galera, eu sei que é bastante coisa, mas, de forma geral,

05:17

eu acho que o mais importante aqui nesse aspecto

05:21

é você entender como que você avalia,

05:23

quais são os pontos que são importantes.

05:26

Esse tipo de informação é valiosa para você conseguir entender...

05:30

como que o agente está trabalhando,

05:32

que é um pouco diferente de quando a gente estava trabalhando com o REG,

05:35

eu não estava preocupado pelas interações,

05:37

pela ordem das coisas, porque eu tinha um pipeline fixo. Porém,

05:40

o REG tem desafios diferentes de agentes e desafios

05:44

diferentes de REG ali no final das contas.

05:47

Mesmo sabendo que um agente acabou consultando e chamando um

05:51

pipeline do REG para ele conseguir pegar informação.

05:54

Então, as coisas estão juntas ali no meio de toda a história,

05:58

de uma forma ou de outra. Fechou? Então é isso aí,

06:01

galera, que eu queria trazer para vocês.

## Resumo IA

[RESUMO_IA]