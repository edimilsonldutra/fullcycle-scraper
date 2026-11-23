Módulo: Arquitetura na Era da IA\
Aula: [Aprofundando nos Detalhes](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18118)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, vamos dar uma aprofundada agora nisso para você entender que

00:06

esse gráfico apenas não é um gráficozinho bonito,

00:09

mas que você vai usar ele forte no seu dia a dia,

00:12

tá? Então, eu vou dar um exemplo aqui para você, tá?

00:16

Se você olhar aqui, eu tenho o meu main sequence,

00:20

então a ideia é que quanto mais eu esteja perto dessa linha,

00:25

melhor a minha proporção em relação à abstração.

00:30

E instabilidade da minha classe. Então, se eu olhar esse cara aqui,

00:33

você vai perceber que ele tem uma abstração, ou seja,

00:38

ele chama uma abstração, ou seja, é 0.33.

00:42

Ele tem 0.75 de instabilidade.

00:46

E ele tem 0.08 de distância, ou seja,

00:49

perto ali do meu tracejado verde. Então,

00:54

no final das contas, ele depende de três caras.

00:57

E o CA, o aferente dele, um cara depende dele. E um ponto interessante é,

01:04

por que a abstração dele é 0.33? Porque ele depende de uma interface.

01:09

Então ele não é 100% instável.

01:12

Como ele depende de uma interface, a instabilidade dele não é total.

01:16

Então ele está perto de um equilíbrio aqui para a gente.

01:19

Agora, olha só que interessante. Se eu chegar aqui nesse quadrante,

01:24

onde a gente tem a zona de dor,

01:26

Aqui que a coisa pega. Se eu pegar,

01:28

por exemplo, essa classe, olha só que interessante.

01:31

Ela é o database.ts. A abstração dela é zero, ou seja,

01:36

ela não utiliza... Ela trabalha de uma forma extremamente concreta.

01:42

Ela tem a instabilidade de 0.06.

01:46

Por que ela tem essa instabilidade baixa, bem baixa?

01:49

Porque ela depende apenas de uma interface. A distância dela...

01:53

ali da proporção entre a parte de abstração

01:57

e a parte de instabilidade é muito grande,

02:03

é 0.94, ou seja, 17 componentes dependem dela. Então,

02:08

isso significa que se ela mudar e tiver algum problema,

02:10

17 caras têm a chance de quebrar.

02:12

Então, é muito forte isso e...

02:16

tem um alvo muito grande de refatoração no final das contas,

02:19

olha só que interessante, galera, esse gráfico não é um gráfico só bonito,

02:24

pra mim, quando eu olho esse sistema,

02:26

eu vejo que essa classe aqui, ela tá pedindo pra ser refatorada,

02:29

ou ela é um ponto crítico no sistema que eu tenho que ter cuidado, tá?

02:33

Pra não colocar mais gente importando dela. Talvez eu possa criar uma interface e,

02:38

aos poucos, fazer com que quem dependa dela,

02:42

depender dessa interface e ajustar essa dependência.

02:46

Então, todo mundo que está nessa zona de dor é alvo de uma possível refatoração.

02:52

Tem umas bolinhas menores aqui, mas o que acontece?

02:57

Ela não é tão expressiva ali no sistema, porque ela acaba sendo mais estável,

03:03

mais concreta, mas... ela não é um cara ali com uma,

03:07

vamos dizer, com muita gente. Ou seja,

03:10

às vezes você tem algumas classes concretas, acontecem esses acoplamentos fortes,

03:15

mas não é algo muito grande. Se você olhar aqui,

03:18

ela está na zona de dor, mas ela depende de um e dois dependem dela.

03:22

É muito diferente de 17 caras dependerem dele aqui.

03:27

Agora, na prática, o que acontece?

03:29

Você pega esse gráfico,

03:30

mapeia os caras que você quer refatorar ou que você quer ter cuidado,

03:35

Ajusta isso, gera esse gráfico de novo e aí vira um game pra você.

03:39

Quanto mais bolinha você tirar daqui, melhor você vai estar deixando,

03:43

entre aspas, a saúde do sistema,

03:45

e essa saúde eu quero dizer em relação ao acoplamento,

03:47

não estou dizendo em nível de código,

03:49

em nível de qualidade de código, de estabilidade e etc.

03:54

O que eu estou dizendo aqui é tirar caras de um

03:56

nível de dor grande em relação ao acoplamento do sistema.

04:00

Aqui eu tenho o inverso. Eu tenho os caras extremamente instáveis aqui para mim.

04:06

Então se eu clicar nesse cara, olha só.

04:09

Ele é uma classe deus, no final das contas. Por quê?

04:13

Ele tem uma instabilidade alta, porque muita gente depende dele. Mas,

04:17

ao mesmo tempo, ele depende de 15 caras. Então,

04:21

ele é muito instável. Ou seja, ele chama muita gente, tá?

04:27

Somente três caras dependem dele. Então, ele tem ali uma instabilidade muito grande.

04:31

Ele tá no oposto, tá? Enquanto aqui um monte de gente depende dele,

04:35

esse cara aqui, ele depende... de muita gente. Então ele tá no inverso,

04:40

tá? Porém, tá? Apesar dele estar nessa instabilidade grande, né?

04:48

Ele não é algo que pode afetar fortemente o sistema. Como assim?

04:56

Ele é instável porque ele depende de muita gente no final das contas,

05:01

mas se ele mudar, ele não quebra o sistema. Ele meio que se...

05:07

autoquebra, né? Agora, se esse cara da zona de dor quebrar,

05:11

ele afeta o sistema inteiro.

05:13

Então, por isso que essa zona de dor acaba sendo mais forte.

05:16

E aqui, eu tenho um outro cara que ele tá quase na zona de inutilidade.

05:20

Por quê? Ele é uma abstração, tá? Aqui nesse caso, que é o Payment Gateway.

05:27

Ele é 100% uma abstração. A instabilidade dele é média e a distância dele é média.

05:33

Por que que é média? Porque eu tenho uma classe...

05:36

que utiliza ele apenas, e um cara depende dele. Por outro lado,

05:41

tem um outro Payment Gateway que não está utilizando ele. Então,

05:45

por isso que ele acaba caindo meio que nesse meio do caminho.

05:50

E por que ele está perto aqui, já numa zona de inutilidade?

05:54

Eu tenho uma interface que

05:56

é utilizada apenas por uma pessoa,

06:01

por um componente. Então,

06:03

é uma interface para um arquivo. Ou seja, é quase que, entre aspas,

06:08

inútil se eu tiver que criar uma interface que vai funcionar apenas para um arquivo.

06:13

Dependendo, isso pode ser over-engineered. Agora,

06:15

se eu tenho uma interface que vários arquivos utilizam, ele,

06:19

provavelmente, sai dessa zona de inutilidade.

06:22

A zona de inutilidade total é quando você tem uma interface que ninguém utiliza.

06:28

Aí é super inútil no final das contas.

06:31

Nesse caso... tem uma utilidade de um cara só.

06:35

Ele depende de um, um depende dele, e aí a gente tem esse cara.

06:39

Mas se você perceber, a distância dele da proporção está longe aqui. Então, a nossa ideia,

06:44

no final das contas, é tentar manter a proporção aqui dos caras. Então...

06:50

Essa aqui é a ideia desse gráfico, tá? Aqui eu botei que você pode fazer por pasta,

06:54

às vezes seu projeto é muito grande,

06:55

e obviamente você não precisa usar exatamente esse script,

06:58

exatamente esse gráfico, tá? Aqui tem a legenda,

07:01

né? E aqui tem algumas métricas,

07:04

e essas métricas mostram a fórmula que foi

07:05

utilizada apenas aí para que você coloque,

07:08

não quero trazer isso como matemática. Agora, novamente,

07:11

por que eu estou dizendo que isso é importante?

07:14

Porque agora eu vejo o meu sistema, eu vejo a zona de dor,

07:17

e nas próximas aulas, o que vai ser meu objetivo? É gerar novamente esse gráfico,

07:23

mas com muitos desses caras aqui refatorados para a

07:28

gente conseguir ter uma ideia de como que

07:30

mudou a proporção e a gente conseguiu tirar caras da zona de dor da nossa aplicação.

07:36

E aí a gente começa a ver que esse monte de cálculo, esse monte de nome,

07:39

começa a fazer sentido porque eu vou deixando o meu sistema mais saudável.

07:43

Fechou? Então vamos nessa

## Resumo IA

[RESUMO_IA]