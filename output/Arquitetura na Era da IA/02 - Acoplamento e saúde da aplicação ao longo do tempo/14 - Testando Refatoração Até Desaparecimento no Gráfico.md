Módulo: Arquitetura na Era da IA\
Aula: [Testando Refatoração Até Desaparecimento no Gráfico](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18124)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, ele fez a nossa refatoração aqui no Stripe Gateway.

00:06

O Stripe Gateway, ele não era um cara extremamente perigoso.

00:12

Se eu não me engano, ele estava até na nossa parte azul,

00:14

mas ele faz parte em relação a essa parte de pagamento,

00:18

já que a gente estava trabalhando com essa injeção de dependência.

00:21

Então, a gente consegue ver aqui.

00:24

As mudanças que aconteceram antes aqui.

00:27

Eu acho que o mais importante em relação ao Stripe Gateway aqui

00:31

é que ele está mais próximo agora da nossa linha verde lá.

00:36

Então esse aí eu acho que é um dos pontos importantes.

00:39

Então ele saiu de 0,43 para 0,20.

00:43

Agora, só o Order Service importa o concreto.

00:45

Então, a estabilidade dele subiu. Então, galera,

00:48

vamos tentar olhar para o gráfico que fica muito

00:51

melhor daqui para frente para a gente ver,

00:53

porque a gente tem que tirar os caras da zona de perigo.

00:56

Então, esse é o nosso exercício,

00:57

mas eu estou fazendo bem aos poucos aqui, tá? Mas depois,

01:02

na hora que a gente pegar o jeito e entender,

01:04

eu vou pedir para ele fazer tudo de uma vez seguindo esses padrões, tá?

01:10

Então... Vamos lá, olha como é que ele está nesse momento, certo?

01:15

Então, onde que está o nosso Payment Gateway aqui, o Stripe nosso?

01:19

Cadê? Aqui, olha. O nosso Stripe está aqui,

01:22

olha. Eu não dei um atualizar ainda. Então, agora, olha,

01:25

ele usa o Stripe, aqui, olha, tem o Payment,

01:29

esse cara aqui que a gente criou naquela hora, o Payment Gateway,

01:34

né? E agora o Stripe está dependendo dele,

01:38

o Stripe está dependendo... também dos tipos, né?

01:43

E ele também está dependendo desses caras aqui,

01:46

dessa zona de dor aqui, né? Que é o cara que a gente quer trabalhar.

01:49

Mas primeiro, eu comecei aqui com as interfaces,

01:52

etc. Já que eu estava mexendo com pagamento,

01:55

eu já fiz esse cara. Agora, o que eu vou fazer?

01:58

Eu vou atualizar e, em tese,

01:59

esse meu Stripe tem que ficar mais perto dessa linha agora aqui,

02:03

por conta que a proporção dele deve estar melhor. Então,

02:06

eu vou rodar de novo aqui esse camarada.

02:11

E vou atualizar aqui o nosso gráfico.

02:14

Vamos ver o que vai acontecer agora aqui. Pera aí.

02:19

E agora eu atualizei aqui e ele não está aqui perto.

02:24

E eu já sei por que ele não está aqui perto, galera.

02:27

Isso é um ponto importante.

02:29

Esse meu sistema, da forma como eu coloquei,

02:32

ele não vai trazer todas as classes. Ele traz as mais, vamos dizer...

02:38

As que têm mais prioridade, vamos dizer. Se eu não me engano,

02:41

eu trago as 12 que têm prioridade.

02:44

E como o Stripe saiu, no final das contas,

02:48

como que eu posso dizer, dessa zona de perigo,

02:51

ele nem está sendo plotado no gráfico. Então, não teve graça esse cara aqui.

02:57

Mas a gente já percebeu que a gente

02:58

Consegue trabalhar ajustando essas dependências dessa forma.

03:03

O que eu vou fazer agora vai ser o seguinte,

03:07

Tá? Eu quero fazer agora uma refatoração maior,

03:14

mas trabalhando realmente nessas classes mais complexas para a gente utilizar.

03:21

Tanto de log, quanto na parte de database,

03:24

quanto nessa parte de utils e etc. Que são os caras aqui mais fortes.

03:31

Então, o que eu vou fazer agora aqui?

03:35

Eu vou...

03:38

Fazer o seguinte, eu

03:41

vou primeiro dar um commit aqui, né,

03:43

eu tinha feito uma verificação com eles, com o sistema,

03:47

né, que ele não tava dando, porque que ele não tinha plotado, né,

03:53

então se eu quisesse eu tinha que botar 16

03:56

itens pra aparecer somente pra o nosso camarada do payment,

04:01

do Stripe aparecer, daí eu falei,

04:03

eu não preciso, eu não quero, se o Stripe tá saudável,

04:06

não tem problema dele não aparecer mais no gráfico, tá?

04:08

Estou fazendo um commit. Mas agora, o que eu vou querer fazer?

04:13

Eu vou fazer o seguinte. Eu vou fazer, novamente, um handoff.

04:19

E o que eu quero fazer agora vai ser refatorar o nosso shared.database.

04:26

Então, eu vou colocar aqui. O que eu quero fazer?

04:29

Refatorar o shared.database.ts

04:33

usando o TDD e tirar completamente.

04:41

Completamente da zona de perigo.

04:45

Por que que eu tô fazendo um handoff agora aqui?

04:47

Porque eu vou criar uma nova sessão,

04:48

eu poderia criar uma nova sessão e começar do zero de novo e etc,

04:54

eu até conseguiria, tá? Mas, já que eu tô com isso aqui de handoff,

04:57

eu vou fazer isso sempre pelo menos pra você ter mais uma ideia

05:01

de algo que possa te ajudar no dia a dia aí com o IA,

05:05

Tá? Então ele vai fazer esse handoff e vai fazer a...

05:10

Para aquilo funcionar com a gente.

05:12

Assim que ele terminar esse handoff, o que a gente vai fazer?

05:17

Aí eu já vou fazer algo um pouco mais ousado depois.

05:23

Eu vou primeiro resolver o database e depois,

05:26

uma vez que a gente aprendeu a resolver esse database e funcionar,

05:30

eu consegui tirar ele ali do gráfico,

05:32

eu vou pedir para ele fazer isso em batch, para ele resolver todos.

05:37

Esses caras em perigo e vamos ver se a gente consegue e tudo mais, tá?

05:41

Então vamos aguardar esse handoff gerado aqui e no

05:44

próximo vídeo a gente faz essa refatoração do database.ts

## Resumo IA

[RESUMO_IA]