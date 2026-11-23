Módulo: Arquitetura na Era da IA\
Aula: [Criando gates de qualidade no CI](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18806)

## Resumo da aula



## Transcrição

00:00

Olá, pessoal, tudo bem?

00:02

Agora eu queria mostrar aqui para vocês um pouco da ideia do Quality Gate, tá?

00:06

Somente para você entender a ideia,

00:10

eu tenho um arquivo de configuração aqui chamado de Quality Gate,

00:15

tá? O Quality Gate, basicamente,

00:17

o que ele vai fazer? É um JSON onde eu falo que eu tenho o meus Evolve Components,

00:24

o meu Evolve do Ragas e o Judge Evolve.

00:27

E aqui eu estou colocando os thresholds que eu quero, no mínimo,

00:32

que ele tenha que utilizar para que ele consiga falar que o gate passou.

00:38

E isso é interessante por quê?

00:39

Porque o que você tem que fazer é, você roda os evals que você tem,

00:44

né? Quando você fizer o, sei lá,

00:47

pull request ou qualquer coisa desse tipo, esse Quality Gate vai rodar.

00:51

Vai bater nesses relatórios e daí, finalmente, o que vai acontecer?

00:56

A gente vai saber se está passando ou não,

00:58

se ele vai bloquear o CI ou qualquer coisa do tipo, tá? Então,

01:02

o que acontece é o seguinte.

01:05

Se eu rodar aqui

01:08

um camarada aqui chamado Evolve Gate,

01:12

vou dar um Enter aqui,

01:14

você vai ver que ele vai dar aqui para mim erro.

01:18

E por que ele está dando um erro aqui? Primeira coisa,

01:21

ele está falando que o component eval está missing aqui para mim,

01:25

quer dizer, o component eval não foi encontrado,

01:28

mas o mais interessante é que ele está

01:31

falando que o judge eval também está missing aqui. O que isso significa?

01:37

Que eu não tenho relatório para gerar, eu não tenho relatório.

01:42

que foi gerado para o juiz, no final das contas,

01:45

para ele ter as informações que ele precisa. E está missing por quê?

01:50

Porque o último eval que eu rodei,

01:52

no final das contas, ele foi um eval de um case ID.

01:55

E aí, pelo fato de ser um eval de case ID,

01:58

ele simplesmente não tem todas, necessariamente,

02:03

todas as métricas. Então,

02:05

o que eu posso fazer aqui no meu caso?

02:09

Eu posso simplesmente...

02:14

rodar esses evals para ele gerar o relatório que eu preciso.

02:19

Então, o que eu vou fazer aqui nesse caso?

02:21

Eu vou pegar e rodar o meu eval do Judge, no final das contas.

02:26

Então, eu vou colocar esse cara e eu acho

02:32

que tem que ter um --save-report,

02:34

se eu não me engano. E vamos rodar esse cara aqui.

02:38

ele vai demorar um pouquinho mais, vamos olhar, eu acho que ele não tem --save-report,

02:42

eu acho que o report ele salva automático aqui.

02:47

E agora a gente tem que esperar um pouquinho para ele rodar,

02:52

porque demora um tempinho, então vou dar um pause no vídeo e daí eu volto.

02:57

Bom pessoal, rodou aqui o summary, ele rodou 28 casos,

03:03

um eu acho que ele deu algum bug, alguma coisa desse tipo, e ele gerou...

03:08

aqui um arquivo. Então, agora, o que eu vou fazer?

03:11

Eu vou dar um Evolve Gate aqui para a gente. E agora, o que acontece?

03:16

Todos os meus itens do juiz passaram.

03:20

Eu tenho aqui o Ragas também que passou.

03:22

E o de Component, tá faltando um Missing aqui.

03:26

Então, eu rodei ele aqui também em paralelo, de forma geral,

03:30

pra gente testar e pra adiantar. Mas tem um item que está missing,

03:35

que é o clarification skips retrieval, que está absent. Então, o que eu vou fazer?

03:41

E você percebeu que aqui também, no agent, tem alguns que estão falhando, inclusive.

03:46

Por quê? Porque o valor que ele deu acaba não passando ali no meu,

03:53

quer dizer, no meu threshold, aqui no final das contas.

04:00

E aqui eu vou rodar.

04:02

Então agora o meu EvolveComponent. Então vou rodar aqui EvolveComponents. Components.

04:13

Aqui para mim.

04:15

Para ele fazer a avaliação dos meus componentes.

04:19

Então ele vai pegar todos os caras.

04:21

Vai fazer o Evolve. Aí a gente vai ter, no final das contas,

04:24

o relatório. E aí, o que acontece?

04:27

Ele vai pegar o último relatório e vai rodar o gate pra ver se esse cara passa.

04:33

A gente tem ainda, em paralelo, dois caras falhando aqui,

04:37

né? Esse tá dando fail nesses dois itens.

04:40

Aí a gente vai ter que resolver esses caras aqui.

04:43

Uma forma de a gente resolver, inclusive...

04:46

diminuindo o threshold. O problema é que esse aqui tá com zero.

04:49

Eu vou colocar zero aqui nesse cara somente pra gente fazer

04:52

o nosso quality gate passar no final das contas.

04:56

Mas o mais importante que eu quero que você entenda é

04:59

que imagina que você pra fazer um commit ou

05:02

qualquer coisa desse tipo você tem que rodar esse quality

05:06

gate e aí quando o sistema sobe para uma pipeline,

05:10

esse CI vai ser executado, e na hora que ele é executado, ele pode barrar,

05:15

por exemplo, o pipeline de CI,

05:18

exatamente porque a gente teve uma regressão.

05:23

Então, isso aqui que é um ponto importante.

05:25

A gente tem que, conforme o software vai amadurecendo,

05:28

a gente vai percebendo que a gente tem que tirar, quer dizer, evitar a regressão.

05:34

E isso aí é um ponto importante porque provavelmente esses

05:38

thresholds eles vêm através de uma baseline que foi aprovada em

05:42

algum momento e conforme o software vai amadurecendo a gente sabe

05:46

qual é o threshold que a gente tem que trabalhar.

05:49

Então acho que esse aí que é um ponto importante.

05:51

E aqui está ele rodando aqui tudo isso via component.

05:56

Então, ele demora, eu acho que deve ser um dos mais demorados.

05:59

Na realidade, o Ragas é o mais demorado,

06:02

porque ele faz diversas... Para cada item,

06:06

ele faz três chamadas para tentar descobrir a pergunta que está sendo feita,

06:10

baseado naquela resposta,

06:12

para que a gente consiga verificar se aquilo faz sentido ali no LLM.

06:18

Então, a gente tem que aguardar um pouquinho.

06:20

Eu vou dar um pause novamente para a gente não

06:23

ter que ficar esperando aqui por muito tempo.

06:28

Prontinho. Então, aqui no final das contas, ele acabou gerando.

06:32

E vamos rodar novamente o nosso gate aqui para a gente ver.

06:37

Vamos lá. Então,

06:39

nós temos aqui um item do component eval que

06:42

deu 0.62 e o threshold era 0.65.

06:46

Eu vou fazer esse cara passar na marra aqui para a gente conseguir ver.

06:50

0.65. Aqui é 0.62 que ele deu, né? Vou colocar 0.6.

06:56

Um outro cara que falhou foi o juiz do argument match,

07:01

que deu 0.8, deu 0.6,

07:06

era para ser 0.8, então eu tenho aqui argument match pass,

07:10

eu vou colocar 0.6,

07:13

e aqui tem um que deu horrível, que é o refusal rate, que deu 0 aqui,

07:19

que é o refusal rate, e eu vou colocar 0 aqui também somente para esse gate passar.

07:24

E agora eu vou rodar o Evolgate e olha

07:28

só que interessante todos esses caras agora eles acabaram passando,

07:34

se eu conseguir olhar isso aqui agora,

07:36

certo? Então, Final Result eu tenho aqui como ele

07:39

passou e a coisa mais interessante agora é o seguinte

07:45

E o mais interessante aqui é que quando eu rodo, eu consigo ver esse texto, né?

07:50

Mas no código aqui do nosso Quality Gate aqui, cadê?

07:55

Nosso Evolve Gate aqui, se você olhar, o que que acontece?

08:01

Nesse cara, ele vai pegar os relatórios, ele vai rodar toda aquela parada,

08:07

mas você vai perceber que no final,

08:12

no ano que ele salva o report, tem o print,

08:14

parse args, aqui, olha só que interessante.

08:18

Se o resultado final for que ele passou no final das contas...

08:25

o system exit é 0, se não é 1.

08:28

Então, o que isso significa no final das contas? Quando o system exit é igual a 0,

08:33

significa que ele passou. Quando a CI olhar que o código foi 0,

08:38

ele fala, não deu nenhum erro,

08:39

está tudo de boas. E se retornar 1, na realidade, é porque não está passando. Então,

08:44

é basicamente isso que a sua pipeline vai pegar se o negócio passou,

08:48

independente do texto. Então, aqui...

08:51

eu tenho o meu Quality Gate. Eu sei que se esses caras passarem,

08:54

eu tô feliz e contente, porque simplesmente a...

09:00

Está de boas, está tudo funcionando e etc. Então, isso aqui, galera,

09:04

é algo quase que imprescindível quando você vai trabalhar com seus sistemas,

09:08

porque agora você consegue pegar todos os seus evols e

09:11

ele consegue gerar toda essa informação aí para você.

09:15

Beleza? Espero que você tenha curtido isso,

09:18

porque realmente é importante e é uma das coisas que você vai utilizar no dia

09:23

a dia para garantir mais qualidade na hora de você rodar e subir as suas aplicações. Fechou?

## Resumo IA

[RESUMO_IA]