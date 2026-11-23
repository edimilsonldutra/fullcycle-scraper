Módulo: Arquitetura na Era da IA\
Aula: [Criando o dataset de evaluation do agente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18803)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, e agora o que acontece? A gente já tem um agente,

00:04

nós já temos as ferramentas que o agente está funcionando,

00:07

mas para a gente trabalhar com evaluation a gente precisa de um dataset.

00:11

E nesse caso o dataset do agente é diferente do dataset

00:15

que a gente fez lá para o nosso reg.

00:17

Ele tem mais campos, ele tem outras informações aqui.

00:22

Esse arquivo é somente para você saber que é Eval Agent Database,

00:26

onde nós temos aqui basicamente os campos que a gente precisa.

00:29

Ou seja, se ele tem que responder, se ele tem que clarificar,

00:34

se ele tem que criar o ticket, se ele tem que refuse.

00:37

E aqui a gente tem ferramentas esperadas,

00:41

ferramentas proibidas, argumentos esperados, trajetória esperada,

00:46

trajetória com match type, o número máximo de steps.

00:51

Os termos esperados e as tags. Então, basicamente,

00:55

essa vai ser a ideia do nosso dataset.

00:57

Para a gente saber trajetória e tudo mais, basicamente, nesse caso,

01:01

é um monte de if para proteger a nossa regra de negócio nesse tipo.

01:07

Ou seja, se ele tem que criar um ticket e o ticket não tiver...

01:15

ali a gente vai ter problema. Por quê?

01:17

Porque isso aqui vai ajudar a gente a validar o nosso

01:19

dataset igual a gente fez com o nosso dataset antes,

01:23

tá? E aqui a ideia é exatamente a mesma do Evolve Components, tá? Do dataset padrão,

01:30

que ele vai sincronizar lá no nosso LangFuse, de forma geral, tá? Então,

01:34

essa aqui é a ideia principal do que foi feito aqui nesse nosso caso.

01:40

Então, se você chegar aqui, ó... Acho que a gente tem 20 caras,

01:44

deixa eu só olhar, eu tinha dado um

01:46

WC aqui, peraí.

01:50

Aqui, ó, eu tenho 20 casos de Evolve Supports, né?

01:54

Aí eu tenho casos onde o Should Refuse é igual a True,

02:00

que são três.

02:02

E eu tenho outro caso também, que é do Should Clarify.

02:07

Quantos caras esse era do Should Clarify? São três caras também.

02:12

E aí a gente vai começando a entrar em outros casos,

02:15

onde a gente tem diversas informações.

02:19

Mas o ponto é que se você for aqui em Evolve e

02:24

olhar aqui, suporte triage agent aqui, você vai conseguir ver...

02:29

todos os 20 casos que vão ter esse dataset. Então, se ele tem que responder,

02:33

se ele tem que clarificar as ferramentas esperadas,

02:36

as ferramentas que são proibidas,

02:38

ou seja, se ele tem que buscar os dados no reg,

02:42

quer dizer, no banco de dados, chamando a pipeline do reg,

02:45

ele não tem que, nesse caso, poder utilizar essas ferramentas que são proibidas.

02:50

Ele está esperando algum argumento. Então,

02:52

a gente tem todas essas informações aqui para a gente.

02:55

E quando a gente roda esse cara,

02:58

que no final das contas é a chamada principal,

03:03

que é o Python -m -evol -agents -dataset,

03:06

ele vai fazer a inserção aqui no Langfuse,

03:08

eu já tinha rodado, então não preciso rodar de novo,

03:10

que é aqui, a triage -agent.

03:14

Então aqui eu tenho todos os casos aqui no Langfuse de todos os meus datasets.

03:19

Se eu clico aqui nesse cara,

03:20

eu consigo ver a mensagem e o expected output. São esses caras aqui.

03:26

Então, aqui é como eu estou fazendo a avaliação específica, inclusive,

03:31

desse agente com esse tipo aí de pergunta. Então,

03:36

essa é a ideia principal. Então, assim,

03:39

foi criar o dataset aqui nessa interação,

03:42

esse vídeo para mostrar que a gente vai precisar do dataset,

03:45

mas o que a gente precisava tanto ter nesse dataset?

03:48

Inclusive, a trajetória esperada. Ou seja,

03:51

ele tem que pegar primeiro a usage e depois ele tem que criar um suporte ticket.

03:55

Então, esses tipos de coisas são importantes para a gente conseguir trabalhar.

04:00

Lembrando que Spected Tools é diferente de Spected Trajectory,

04:05

porque Spected Tools pode trazer diversas ferramentas e o Trajectory

04:09

é a ordem que essas ferramentas vão ser chamadas,

04:12

inclusive. Então, vamos seguindo aí, galera.

## Resumo IA

[RESUMO_IA]