Módulo: Arquitetura na Era da IA\
Aula: [Controlando captura de conteúdo por ambiente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18758)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, agora a gente vai fazer algumas experiências aqui. Por quê?

00:06

Porque eu quero trazer aquele assunto sobre a parte de cardinalidade,

00:11

quero falar sobre eventos e também mostrar como que a gente pode,

00:16

com algumas variáveis de ambiente,

00:18

isso aqui é um exemplo simples, obviamente, conseguir escolher o que vai,

00:22

por exemplo, para um back-end ou não vai,

00:24

e qual é o tipo de conteúdo que a gente vai enviar. Então, se você olhar aqui,

00:30

Eu criei aqui um app Envoy chamado Development,

00:33

então a gente está em ambiente de desenvolvimento.

00:35

O Observability Sample Rate está 1.0. O que significa?

00:39

Que ele vai mandar todas as

00:42

informações de tracing para a nossa aplicação. Nesse caso,

00:47

eu vou mostrar com o Jaeger mesmo. E aqui a gente tem Observability Capture Content.

00:53

Então, esse cara aqui serve para realmente conseguir pegar todo o conteúdo.

00:57

Então, o que eu vou fazer? Eu vou fazer o seguinte,

01:00

vamos lá. Eu vou primeiramente, lembrando,

01:02

a gente está em development e a gente está com capture content igual a true. Então,

01:06

eu vou rodar aqui um Python -m

01:10

e eu vou colocar aqui para o nosso camarada.

01:15

Opa, espera um pouquinho, deixa eu só limpar aqui que eu quero trabalhar com o

01:21

Jaeger, que ele é mais fácil de a gente conseguir ver isso aqui,

01:25

mais simples, inclusive.

01:27

Eu vou colocar esse cara aqui.

01:30

E esse cara vai para o Jaeger.

01:33

E esse cara aqui.

01:37

Fecha. Beleza. Então, vamos lá. Então, eu vou rodar agora aqui.

01:41

E eu vou colocar.

01:42

Me fale sobre a SLA do plano Enterprise.

01:54

E vou rodar aqui normal e boas. Então, vamos nessa. Vamos esperar ele processar.

02:02

Ele está fazendo ali tudo o que ele tem que fazer.

02:05

Mas, se você inclusive perceber logo no começo no debugging aqui,

02:08

observabilidade está ativa, o ambiente é desenvolvimento,

02:12

OpenTelemetry como exporter, o sample rate de 1.0,

02:16

capture content de true e ali na realidade está mandando ali para o Jaeger.

02:21

Agora, o que eu vou fazer?

02:22

Eu vou dar aqui find traces e eu vou rodar esse cara agora aqui.

02:27

Então, o que acontece agora?

02:29

Eu tenho aquela minha requisição desde o início.

02:32

Se você olhar aqui o meu regplanning,

02:34

eu tenho aqui as minhas tags e você vai perceber que eu tenho ali o termo exato,

02:38

o enterprise e etc. Eu tenho os dados do meu processo, perfeito, está tudo aqui.

02:45

Agora, eu tenho aqui o meu retrieval.

02:48

E aqui no meu retrieval, eu tenho o tenant, o status, se está publicado,

02:53

o plano e etc. E as informações que a gente já tinha aqui.

02:58

Certo? Agora, eu tenho o meu re-ranking,

03:01

que é as minhas tags, basicamente esse cara aqui.

03:05

E eu tenho aqui o meu answer generation,

03:09

onde eu tenho essas informações aqui que eu precisava ter. Até então, beleza. Mas,

03:15

se eu for agora aqui também no meu pipeline inteiro,

03:19

olha só que interessante agora. Eu tenho... O feature, o resensor,

03:25

Needs clarification, etc. Parecido tudo com o que a gente já tinha feito antes.

03:30

Eu tenho a parte do meu processo.

03:32

Mas, agora, o grande ponto de toda essa história está aqui.

03:37

Você está vendo essa parte aqui chamada de logs?

03:40

Essa parte aqui de logs, no caso do Jaeger, no final das contas,

03:45

é um tipo de evento. Então, se você olhar aqui,

03:49

eu tenho aqui event que é App Debug Question,

03:54

e eu tenho App Debug Question, me fale sobre o plano Enterprise.

04:00

E aqui eu tenho o resultado, e aqui eu tenho o plano Enterprise FSA Cloud,

04:05

e ele traz a resposta aqui para mim.

04:08

Então, o que eu quero mostrar com isso, pessoal? Querendo mostrar,

04:11

são duas coisas importantes. Uma coisa é a relação à cardinalidade.

04:16

O que acontece é o seguinte, com a cardinalidade baixa, que são esses caras aqui,

04:20

isso aqui fica fácil de a gente conseguir trabalhar.

04:23

Por que eu estou dizendo isso? Porque nesse caso,

04:27

eu consigo filtrar na hora que eu vou trabalhar.

04:30

Na minha ferramenta de observabilidade, eu posso chegar e falar,

04:33

eu quero que venha tudo .app .feature, app .total.

04:39

Eu posso conseguir filtrar, eu consigo acessar.

04:42

Por quê? Porque normalmente essas informações aqui...

04:46

Elas são fixas, elas não são instáveis. Agora,

04:50

imagina uma pergunta que cada hora é uma pergunta diferente. Além disso,

04:54

uma pergunta diferente pode ter outra coisa em relação à parte de informação,

05:00

que são as respostas completas, os dados do usuário,

05:03

por exemplo. Então, nesse caso...

05:06

Ao invés de a gente trabalhar com tags ou, na realidade, atributos,

05:10

aqui o Jaeger chama de tags, mas a gente está falando de atributos e eventos.

05:15

O que isso significa? Que o evento é algo que,

05:19

no final das contas, ele nos deixa claro, ali no meio da história,

05:24

o que aconteceu dentro daquele span, por exemplo. Então,

05:30

isso aí que as coisas começam a ficar mais interessantes e aí

05:34

a gente começa a ter os dados um pouco mais sensíveis.

05:36

Então, o evento é aquilo que acontece, tá? E dependendo da situação,

05:42

a gente pode ter um nome fixo para ele, mas...

05:47

Os outros atributos desse cara, normalmente eles são extremamente variáveis. Então,

05:52

fica muito ruim de eu filtrar, de eu buscar e ter todos esses tipos de coisa.

05:56

Então, por isso que a gente acaba tendo essa

05:58

separação forte em relação à parte de eventos.

06:02

Quando a gente está falando sobre observabilidade, inclusive,

06:05

normalmente a gente fala sobre log, trace, eventos.

06:10

Log, trace, eventos e...

06:14

e métricas, certo? E a gente tem diferenças entre logs e eventos.

06:20

O grande ponto aqui é que na ferramenta em si, ela pode, você vê, se você olhar,

06:25

ela está colocando aqui log e está chamando como evento. Parece uma contradição.

06:30

Mas normalmente isso acaba sendo muito de semântica de cada aplicação. Porque log,

06:34

na realidade, é você ter tudo o que aconteceu com todas as informações.

06:40

O evento é...

06:41

quais foram normalmente aqueles gatilhos que fizeram com que aquilo causasse.

06:46

Nesse caso, o Jaeger está trazendo aqui os logs com os eventos dentro,

06:50

ou seja, ele logou quais são os gatilhos e as coisas que acabaram acontecendo.

06:55

Então, ele definiu.

06:56

Mas isso aqui foi escolhido onde a gente definiu dentro da aplicação.

07:01

Ou seja, foi mais uma informação que a gente mandou para o OpenTelemetry.

07:06

Mas o importante que eu quero que você perceba é que ele

07:09

aparece em um local diferente de onde a gente tem esses nossos atributos,

07:14

que aqui o Jäger está chamando de tags. E isso aí é uma das coisas importantes,

07:18

porque... Tag é algo normalmente com uma cardinalidade baixa, que eu consigo filtrar.

07:24

Os eventos normalmente são coisas extremamente variáveis e que normalmente eu uso

07:28

para consultar e não necessariamente para filtrar e qualquer coisa desse tipo, tá?

07:33

Agora, mas se você perceber,

07:36

aqui está constando como ambiente aqui de development, tá?

07:41

Uma coisa interessante é que eu poderia mudar aqui, por exemplo, para production.

07:45

E rodar a minha aplicação aqui, deixa eu até copiar a minha pergunta, aqui

07:52

a minha pergunta, minha resposta, qual foi a minha pergunta,

07:55

e falar sobre o plano Enterprise, né?

07:59

Então o que eu vou fazer aqui? Eu vou sair agora,

08:01

vou entrar de novo na aplicação, e olha só que interessante, se você olhar aqui,

08:08

eu já tenho um filtro, que é Observability Capture Content, e aqui fala,

08:12

isso aqui só pode ser True em Development, por quê?

08:15

Porque se esse cara aqui tiver True, nas regras que estão na aplicação,

08:19

ele vai pegar as informações do usuário,

08:22

que são a pergunta e a resposta que eu não queria ter acesso.

08:26

Agora eu vou colocar isso aqui como falso. Ele vai permitir,

08:29

mas ele sabe que o ambiente está como produção.

08:32

E agora, se eu colocar, me fale sobre o SLA do plano Enterprise,

08:36

o que vai acontecer? Ele vai fazer todo o processo, normalmente.

08:42

E agora, o que acontece aqui? Deixa eu voltar.

08:46

Deixa eu dar um find trace,

08:47

você vai perceber que eu tenho novamente os tracings igualzinho,

08:51

mas se eu for no meu pipeline, eu não tenho mais aqui os meus eventos.

08:55

E isso aí, no final das contas, acontece o porquê?

08:58

Porque eu criei uma regra muito clara que eu não consigo colocar... coisas, por exemplo,

09:06

de debugging ou coisas referentes aos eventos que

09:10

aconteceram ali em ambiente de produção. Então,

09:12

isso aí é uma forma de você conseguir,

09:15

de forma geral, projetar o seu ambiente para que,

09:18

simplesmente com uma troca de variável,

09:20

você consiga ter informações ou não ter essas

09:24

informações ali dentro da sua aplicação,

09:27

enviando para a parte de observabilidade, tá?

09:30

Isso aqui foi feito de uma forma simples.

09:32

Agora tem um ponto importante apenas para constar aqui,

09:35

para não dizer que eu não comentei, tá?

09:37

Que é o seguinte, quando você trabalha com OpenTelemetry,

09:41

você tem algo que você chama de Collector,

09:43

tá? O Collector, ele é um intermediário entre a sua aplicação, tá?

09:50

E aqui ao seu backend, certo?

09:53

Esse Collector, ele pode ser como uma aplicação sidecar,

09:58

ou seja, um proxy que você manda,

10:00

tudo que sai pela sua aplicação passa por esse proxy.

10:02

E esse proxy é o cara que manda a informação para o OpenTelemetry,

10:06

Ou você pode ter um serviço mesmo,

10:09

Realmente um servidor, uma aplicação mesmo, que só fica rodando esse collector,

10:13

E a aplicação manda para o collector, e o collector manda para o backend,

10:18

E quando eu falo backend aqui, eu estou dizendo o Jaeger,

10:20

O Langfuse, o Datadog, o New Relic, etc.

10:24

Então, o que acontece aqui no meio de toda essa história? Esse collector,

10:29

Ele possui formas que nos permitem, por exemplo,

10:34

Em tempo real, fazer esses tipos de restrição.

10:38

Por exemplo, o sampling aqui, eu estou enviando 100% dessas,

10:44

100% das minhas requisições.

10:48

Eu poderia pedir para ele enviar apenas

10:52

Metade de tudo isso. Ou eu posso pedir para ele mandar,

10:56

Sei lá, 10% de tudo que está acontecendo.

10:59

Com o collector do OpenTelemetry,

11:02

Eu posso fazer essa escolha aqui e eu posso fazer algo,

11:05

Por exemplo, para eu quero excluir tudo que é app.debug.

11:09

Então, eu não fico mais tão preocupado com os dados que eu estou sendo enviados. Por quê?

11:14

Porque eu sei que o collector vai barrar. Ou seja,

11:18

Ele vai excluir todas essas informações para na hora de mandar para o backend.

11:25

Então, o meu collector pode fazer diversos desses tipos de filtro,

11:29

Ele pode trabalhar com o meu sample rate e coisas desse tipo.

11:33

Mas mesmo assim,

11:34

Eventualmente vale a pena você pensar e controlar isso na sua aplicação,

11:38

Porque, de forma geral, é um dado que está sendo enviado para alguém e esse dado...

11:43

Não digo que necessariamente ele vai poder vazar,

11:46

Mas ele é um dado a mais que está saindo da sua aplicação.

11:51

Então, muitas vezes é recomendável a gente fazer internamente realmente dados

11:57

Que a gente acha que não devem ser enviados a todo tempo,

12:00

Mesmo para o coletor. Mas isso aí fica muito, muito a decisão de cada...

12:08

Empresa, de governança, de como que isso vai ser tratado e tudo mais.

12:11

O importante que eu quero que você saiba é que esse

12:14

Tipo de coisa é bem comum ali de acontecer.

12:17

Fechou? Então, estamos aqui então, né,

12:20

Queria deixar claro esse exemplo para que você consiga

12:24

Perceber que eu consigo mandar essas informações,

12:27

Somente as que eu quero,

12:28

E eu consigo separar esses eventos que vão ser trabalhados.

12:32

Fechou? Um grande abraço e é isso aí.

## Resumo IA

[RESUMO_IA]