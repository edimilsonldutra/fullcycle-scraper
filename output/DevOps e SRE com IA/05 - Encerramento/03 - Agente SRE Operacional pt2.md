Módulo: DevOps e SRE com IA\
Aula: [Agente SRE Operacional pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18551)

## Resumo da aula



## Transcrição

00:00

Então aqui, uma estratégia de adoção gradual.

00:04

Eu acho que é bacana a gente entender como

00:08

que você pode adotar isso nos seus ambientes.

00:11

Então, o ambiente progressivo aqui. Primeiro você vai fazer tudo em dev,

00:16

deixar o agent agir livremente,

00:18

fazer o reinício que precisar, fazer tudo certinho ali que precisar.

00:24

Depois você vai subir para a stage e você vai agir.

00:27

O agent vai agir com aprovação humana e em

00:31

produção você pode colocar ele agindo também.

00:36

Você também pode colocar,

00:37

se você tiver confiança naquele agent e não for alguma coisa tão,

00:42

como é que eu vou te explicar, tão danosa assim para o seu ambiente,

00:48

para a sua empresa, você pode colocar o agent ali agindo com aprovação,

00:52

porém inicialmente você pode colocar apenas como sugestão e depois ir evoluindo. Ok?

00:58

Então, no segundo aqui, na parte 2 aqui,

01:01

nós temos o Blast Rays pré-aprovado, que basicamente,

01:05

se você falar assim, que você vai fazer um restart no ambiente de dev, ok.

01:10

Fazer um scale no staging, talvez.

01:13

Fazer um drop, database em produção, nunca. Você não pode fazer isso.

01:19

Então, você coloca todo o script para ele,

01:23

o que ele pode e o que ele não pode fazer. Tá bom?

01:27

Então, aqui nesse lado a gente tem o QSuite mais observabilidade,

01:32

que é o QSuite sempre disponível, ou seja,

01:35

a observabilidade completa via LinkFuse e Audit Log estruturado.

01:39

Com o QSuite você vai conseguir parar as ações do agent ali. Então,

01:45

você quer que o agent não faça mais restart dentro do seu ambiente.

01:49

Você pode usar o QSuite para isso. Tá legal?

01:51

Então, basicamente, você vai falar com o agent assim.

01:54

Não faça mais esses tipos de ações. Você ativa com Kill Switch. Ok?

02:01

Governança do agent aqui. Então,

02:03

tem nossas regras de governança que a gente criou

02:06

à medida que a gente foi implementando.

02:09

Então, nós vamos falar um pouco aqui do fluxo que a gente seguiu. Tá bom?

02:13

Basicamente, as ações supervisionadas.

02:16

Registrar pending action com Blast Rays. Ok?

02:21

Aprove. Reject Action Human Decide via o chat OpenAI com linguagem natural.

02:27

O LangFuse Audit Log,

02:29

onde a gente consegue ver tudo o que aconteceu dentro daquele chat.

02:34

A gente consegue ter tudo certinho.

02:38

Tudo de ponta a ponta o que aconteceu. E o Kill Switch,

02:42

que bloqueia ações automaticamente quando ativado. Então, se ele estiver ativado,

02:47

ele vai bloquear qualquer tipo de ação que for ocorrer ali dentro.

02:51

Então a gente implementou essa stack de governança

02:55

para evitar problemas dentro da orquestração do nosso agent.

03:02

Isso é interessante,

03:03

você implementar a governança para evitar que aconteça

03:07

uma catástrofe dentro do seu sistema e

03:09

você pode ter algum problema no seu ambiente ou na sua empresa por causa disso.

03:14

O problema que eu digo é até deixar um sistema, uma aplicação fora do ar.

03:21

Então, alguns casos práticos aqui por indústria, tá?

03:25

Então, a gente tem aqui Fintechs,

03:27

que têm alta criticidade financeira e regulamentação rígida,

03:32

que é feita pelo Banco Central e assim por diante.

03:35

O que é interessante? O agent diagnostica apenas.

03:39

Então, o agent vai apenas diagnosticar para você. Então,

03:42

tome bem cuidado dentro de uma empresa financeira quando

03:47

você for implementar esses tipos de agents, ok?

03:50

Ação corretiva sempre com aprovação humana.

03:53

Sempre coloque aprovação humana se você for fazer alguma ação dentro do seu ambiente.

04:00

E audit logs imutáveis para compliance. Ou seja,

04:04

você tem que garantir que os logs que você está gerando ali de aprovação,

04:10

de restart das coisas,

04:11

sejam bem estruturados e que

04:14

sejam entregues de maneira estruturada,

04:19

e rápida para auditoria e compliance. Ok?

04:24

Health Tech, dados de paciente. Então,

04:28

a gente tem vida e risco nesses tipos de indústria.

04:31

Então, assistido com open code ali que você pode usar.

04:35

Agents autônomos não em produção de paciente. Então, assim,

04:39

se você tiver agents ali que podem arriscar a vida

04:43

de alguém dentro de uma indústria do tipo,

04:45

pode ser um problema. Então, tomem cuidado com essa parte também. Ok?

04:50

Staging ok com supervisão,

04:52

então, quando você for passar por um ambiente de staging para fazer seus testes

04:56

ali para a produção sempre com supervisão e

04:59

rollback instantâneo e obrigatório de qualquer problema,

05:02

pode correr algum risco de vida para alguém, etc. Faça o rollback rapidamente,

05:08

para evitar qualquer tipo de problema, tá?

05:11

Infraestrutura crítica, então sistemas de energia,

05:14

telecom sistemas desse tipo de tema,

05:18

você não pode ter problemas com esses tipos de infraestrutura.

05:22

Imagina se você faz algum agent autônomo que derruba

05:25

a energia de sei lá quantas pessoas.

05:27

Imagina que você faz algum agent autônomo que ele faz o processo todo completo lá,

05:31

que você derruba a internet de muita gente.

05:33

Então, isso pode ser um problema. Então, Blast Heroes muito limitado,

05:37

deixa sempre bem fechadinho. QSuite é obrigatório.

05:40

Você sempre tem que ter a opção de colocar

05:43

um QSuite para ele não fazer coisas automáticas.

05:47

E modo assistido é prioridade,

05:50

tá bom? Então, sempre tente trabalhar no modo assistido. Então,

05:54

alguns casos aí onde a gente pode aplicar Agents,

05:56

mas com bastante cuidado onde a gente vai aplicar e como a gente vai aplicar,

06:02

tá bom? E claro que eles vão ajudar bastante no dia a dia,

06:06

eles vão automatizar bastante coisa, tirar bastante trabalhos manuais,

06:10

mas sempre com governança e olhando onde você pode colocar ou não, ok?

06:17

Então, a gente falou um pouco aqui só do aspecto de autonomia dos nossos agents.

06:21

Igual eu falei, nosso módulo aqui vai ser mais prático.

06:24

Então, a parte teórica aqui vai ser bem rápida.

06:28

Falamos um pouco de governança e falamos um pouco de alguns casos práticos.

06:31

Que a gente deve evitar tanta autonomia para um agente de AI fazer isso,

06:37

fazer qualquer ação.

06:39

E na próxima parte, vamos falar um pouco das demos que a gente vai trabalhar.

06:46

Então a gente vai fazer quatro demos para

06:49

mostrar como está funcionando o nosso ambiente.

06:53

E é isso aí. Daqui a pouco eu volto com a próxima parte. E um abraço a todos.

## Resumo IA

[RESUMO_IA]