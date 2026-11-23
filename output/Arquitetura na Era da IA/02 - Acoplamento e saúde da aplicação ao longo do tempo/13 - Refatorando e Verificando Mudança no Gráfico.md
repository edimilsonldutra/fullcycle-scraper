Módulo: Arquitetura na Era da IA\
Aula: [Refatorando e Verificando Mudança no Gráfico](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18123)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, nossa refatoração foi feita e eu imaginava que ia acontecer o que aconteceu,

00:06

mas na realidade é um bom sinal. Primeira coisa,

00:10

lembra que a gente tem que pensar.

00:13

Ele focou no Dependency Inversion Principle do Payment Gateway no Order Service. O que significa?

00:19

E no Order Service, a gente vai começar a receber ali uma interface.

00:25

Isso não significa que a gente ia ter toda a parte de pagamento

00:28

refatorada e inclusive melhorar aqueles nossos gráficos

00:32

em relação à parte de acoplamento.

00:35

Na realidade, a gente adicionou ainda mais uma interface no Order Service.

00:41

Mas o ponto é que o Order Service utiliza, obviamente, o processo de pagamento.

00:48

E a gente tem uma classe concreta de processo de pagamento,

00:51

que, por exemplo, é o Stripe, que é a parte de pagamento principal.

00:56

Então, se você olhar aqui, olha só.

01:00

Ele coloca antes e depois, ele adicionou mais um teste, o estoque,

01:04

os testes de valores críticos que ele acabou criando,

01:08

NPM Start, cobertura, foi para 94,

01:11

e o Payment Gateway aqui saiu de 1 para 0, ou seja,

01:16

ele ganhou um consumidor de inversão e saiu da zona de inutilidade.

01:22

Como assim? Vamos tentar olhar alguma coisa aqui.

01:26

O que acontecia aqui no meio da história é que

01:29

o nosso Payment Gateway está quase na zona de inutilidade porque,

01:35

basicamente, os caras não estão usando ele.

01:38

Então, no nosso script inicial, na nossa versão inicial,

01:42

a gente tem com ele aqui, se você olhar. Payment Gateway.

01:46

Ele é instável, abstrato. E tem pouca gente utilizando.

01:50

Deixa eu ver se ele gerou de novo esse cara aqui. Deixa eu ver.

01:58

Não atualizou. Deixa eu rodar aqui. Espera aí.

02:02

O script que gera esse main sequence.

02:05

Vamos ver se teve alguma alteração agora.

02:09

Aqui. Olha só que interessante, galera.

02:12

A gente estava com aquele Payment Gateway aqui quase numa zona de inutilidade,

02:17

porque os caras não estavam usando ele. Mas agora, olha só que interessante.

02:22

Eu tenho dois caras utilizando, o Order Service e o Stripe Gateway.

02:28

Então, o Stripe agora está utilizando esse camarada.

02:32

Ou seja, ele teve mais uma dependência chamada,

02:36

mas ele começa a utilizar. Então,

02:40

a gente começa a ver a importância desse nosso gráfico,

02:44

porque a gente começa a verificar como que as coisas

02:47

vão começar a ser resolvidas daqui para frente.

02:50

O que eu vou fazer agora aqui vai ser o seguinte, tá?

02:54

Eu vou dar um commit para

02:57

a gente ter essa parada. E aqui ele está dizendo uma coisa importante,

03:02

tá? Que é o seguinte,

03:04

não é porque eu resolvi uma dependência que eu não

03:07

vou ter mais importação ou qualquer coisa desse tipo.

03:10

Na realidade, ele precisou de uma nova dependência para trabalhar.

03:17

Mas agora, o meu Payment Gateway,

03:19

ele já está... ali numa zona da forma como eu queria. É abstrato,

03:23

não está na zona de utilidade e está trabalhando. O que eu tenho certeza aqui,

03:28

esse cara aqui estava em uma zona de inutilidade. Agora, o Stripe Gateway,

03:33

Aqui para mim, ele está concreto, ele está em nenhuma aqui,

03:39

Stripe Payment Gateway, nenhuma concreta saudável, aqui nenhuma fronteira,

03:44

Em cima do Main Sequence,

03:45

Aqui para a gente. Então, o que está na zona de perigo?

03:49

Então, eu acho que aqui a gente pode fazer, a partir do nosso próximo vídeo,

03:53

Eu acho que dá para a gente iniciar agora,

03:55

É para que ele consiga fazer isso com o Payment e o Stripe agora aqui para a gente,

04:02

Porque aqui pode ser uma boa colocada.

04:04

Então, eu vou colocar aqui para ele assim,

04:07

Eu posso fazer a mesma coisa no Payment Service também,

04:12

Mas eu quero, na realidade, deixa

04:17

Eu só dar uma olhada aqui, espera um pouquinho, galera,

04:19

Onde eu tenho... Cadê o meu camarada do reporting? O database.

04:28

Utils aqui para mim.

04:30

Na realidade, eu vou seguir no Stripe, tá?

04:35

Porque daí ele vai conseguir trabalhar. Eu tenho aqui notification. O sales.

04:42

Tá de boa. Então aqui, ó. Payment Service. Aqui que ele tá colocando,

04:46

Né? Se eu quiser fazer a mesma coisa com o Payment Service.

04:52

Para que ele entre como dependência invertida para a parte de pagamento.

04:58

Eu posso pedir para ele fazer aqui também. Então, eu vou colocar o seguinte.

05:03

Aplique a mesma Dependency Inversion Principal no Payment Service

05:07

e faça a refatoração do

05:13

Stripe aqui para a gente.

05:18

Utilize aqui. TDD.

05:28

E garanta que ele sairá da zona de perigo, tá?

05:36

Ok? Galera,

05:37

Perceba que a gente está sendo o babá de inteligência artificial nesse momento, tá? Ou seja,

05:42

Eu estou interagindo com ela, conversando com ela.

05:45

Eu não estou rodando naqueles modos automáticos com TDD e etc.

05:49

Mas por que eu não estou fazendo isso nesse momento, tá?

05:53

Eu estou fazendo isso porque eu quero mostrar para vocês

05:55

Esses processos que são importantes de a gente entender acoplamento.

06:01

Isso a gente tem que ver, ver arquivo e etc. e tudo mais.

06:06

Software Update pedindo aqui para mim.

06:09

Então, agora, a gente tem que aguardar esse cara rodar e verificar como

06:13

É que vai funcionar todo esse processo que a gente fez até agora.

06:18

Beleza? Então...

06:21

Vamos esperar agora um pouco para ele fazer esse processo.

06:25

E para esse vídeo não ficar muito grande,

06:28

No próximo vídeo eu trago aqui o que ele executou.

## Resumo IA

[RESUMO_IA]