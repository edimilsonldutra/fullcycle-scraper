Módulo: Arquitetura na Era da IA\
Aula: [Finalizando Refatoração Piloto](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18125)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, o Handoff foi feito e ele escreveu aqui, né? Num arquivo temporário.

00:07

E ele traz um ponto aqui, ó. Armadilha número 1 destacada,

00:10

né? O suporte DB .ts depende das referências atuais.

00:15

Toda rede de segurança quebra se o reset não for escrito junto.

00:20

Sequência TDD verificação e tal. E aqui ele coloca assim,

00:24

Skills sugeridas, brainstorming, writing plans, TDD.

00:28

Verification before completion e commit, tá?

00:31

Ele sugeriu essas skills porque são skills que eu tenho aqui do Cloud

00:36

Code na parte de superpowers e esse

00:39

brainstorming provavelmente ele vai querer fazer perguntas,

00:44

como se fosse uma forma de como que eu trabalho,

00:47

porque é uma operação mais complexa de forma geral para ele fazer tudo isso, tá?

00:53

Eu vou agora, nesse momento, eu vou limpar, tá?

00:59

E eu vou colocar a

01:01

partir do, que é o Handoff,

01:09

faça

01:12

a refatoração do componente.

01:19

Eu vou colocar somente dessa forma aqui,

01:22

era o componente do banco de dados que eu tinha falado? Acho que era, né?

01:27

Era o de Database, do componente conforme o documento. Documento.

01:36

Vamos lá, vou dar um Enter aqui. E vamos ver o que ele vai trazer aqui para a gente.

01:41

Eu poderia ter sido mais específico aqui,

01:43

mas eu fiquei curioso, inclusive, como ele sugeriu skills.

01:48

Vamos ver se ele vai trazer essas skills automaticamente aqui para mim e carregar.

01:55

Então, como é uma refatoração em risco,

01:59

ele está aqui falando em relação às skills que talvez...

02:06

Faça sentido ali para ele.

02:07

E por que é alto risco? Porque tem 17 caras, eu acho,

02:11

que usam ele. Quantos caras? Deixa eu olhar aqui enquanto ele está correndo.

02:15

Database. São 17 caras que dependem dele. Então,

02:18

se tem 17 caras que dependem desse cara diretamente,

02:22

a gente tem que ter a nossa interface e depois mudar

02:27

os 17 caras apontando para a interface e ajustar com ele.

02:30

Ou seja, tem bastante gente.

02:33

Pelo menos 17 arquivos ali que têm que ter uma mudança ali mais forte. Então,

02:38

acho que isso aí é um aspecto mais grave, vamos dizer assim,

02:43

porque é uma operação de realmente alto risco.

02:47

E por isso que ela é alto risco, né?

02:49

Porque tem muita gente dependendo dela e o sistema chegou a ficar assim.

02:54

Eu recomendo que em algum momento, se você for fazer algo parecido,

02:59

gerar um gráfico parecido com esse, né?

03:02

você vai começar a perceber como que é complexo e arriscado,

03:08

muitas vezes, mexer em classes estáveis dessa forma, concretas,

03:11

e por isso que isso dá uma insegurança muito grande. Então,

03:15

por isso que eu comecei ali pelos testes, para eu ter uma rede mínima de segurança,

03:20

para que quando eu faço alterações nessas outras classes,

03:23

eu tenha certeza de que elas vão funcionar. Por outro lado,

03:28

vão ter testes que vão ter que ser alterados por conta disso aí também, tá?

03:33

Então, agora ele está pensando, vamos aguardar aí para ver o que ele faz.

03:38

Bom, pessoal, e agora ele foi fazendo as contas dele aqui,

03:41

Ele entrou num modo brainstorming aqui, e aqui ele tá perguntando, olha...

03:46

A meta do database é ser menor que 0.3,

03:50

do jeito que a métrica é calculada em relação

03:52

ao número de abstrações e interfaces por arquivo.

03:56

Agora eu tenho que escolher, que ele está trabalhando,

03:59

qual é a melhor forma de eu trabalhar com isso.

04:02

Eu posso criar uma única interface com banco de dados,

04:04

meio que gorda, ou seja,

04:06

um arquivo que vai receber uma interface de 17 caras

04:09

e vai virar uma abstração estável num canto bom,

04:12

ou...

04:14

Eu posso criar repositórios por agregado e cada serviço vai depender só dela. Ou seja,

04:20

ou eu vou ter um arquivo único gigante,

04:22

ou eu vou ter vários arquivos com dependências mais colocadas.

04:28

Então, aqui é o ISP, Interface Segregation Principle, em relação ao SOLID. Então,

04:35

eu vou colocar esse cara aqui para ir em repositórios por agregados.

04:38

Aqui ele coloca em relação a funções.

04:41

Vários consumidores não são classes como construtor, sales, etc.

04:45

Para o CA migrar para o concreto, para a abstração, ele tem que importar esse cara.

04:51

Então, eu tenho que converter esses caras para classes injetadas.

04:56

Eu não vou deixar esses caras virarem suas funções.

04:58

Vou dar um enter agora aqui e vamos aguardar

05:01

esse camarada rodar todo esse processo aqui com a gente.

05:06

Pelo jeito...

05:09

Eram perguntas realmente totalmente coerentes, né?

05:12

Porque se você vai mudar 17 caras,

05:14

você tem que ter essas interfaces funcionando.

05:16

Eu mandei ele trabalhar no padrão repositório,

05:19

mas vamos nessa agora pra ver como é que ele vai trabalhar.

05:22

Vamos aguardar e aí vamos

05:26

ver o resultado final.

05:29

Bom, pessoal, ele terminou aqui o processo. Eu não analisei o código,

05:34

mas só pra você saber, basicamente,

05:37

o que ele acabou fazendo foi...

05:40

Como tinha muita dependência e muita coisa, a gente estava falando,

05:46

eu acho que 17 componentes, né? Então, a gente estava falando de algo,

05:50

de uma refatoração que não é trivial,

05:52

mas era um piloto para a gente tentar entender como que aquele gráfico,

05:56

ele acaba mudando ali ao longo do tempo, né? Então, basicamente,

06:01

ele fez até uma pergunta, como que eu queria fazer?

06:04

Criar uma única interface e nessa interface...

06:09

Todo mundo ia acessar esse arquivo com seus contratos,

06:13

o que não é legal. Ou ele falou se eu não queria criar,

06:16

na realidade, interfaces por agregados.

06:21

Eu não estou querendo falar muito, inclusive,

06:25

de Domain-Driven Design ou qualquer coisa desse tipo, mas, basicamente,

06:28

ele cria uma interface onde eu

06:33

posso criar classes concretas que conseguem...

06:37

falar com o mundo externo,

06:38

nesse caso com o banco de dados.

06:39

Então existe um padrão de repositório ou qualquer coisa desse tipo,

06:43

Né, então basicamente ele focou muito no ISP,

06:46

Interface Segregation Principle, do SOLID, tá,

06:49

Lembrando, tá galera, isso aqui não é um curso pra te ensinar SOLID,

06:53

Isso não é um curso pra te ensinar arquitetura no aspecto de como programar, mas aqui

07:00

O nosso foco é entender principalmente aqui sobre acoplamento,

07:04

E, obviamente, quando a gente fala disso,

07:06

A gente invariavelmente tem que falar desses tipos de termos.

07:11

Então, eu não sei o nível de conhecimento que você tem em

07:13

relação a esses aspectos de abstração ou até mesmo padrões de acesso,

07:19

design patterns, etc.

07:20

Mas o importante é que a gente entenda o que aconteceu durante todo esse processo.

07:27

Aqui, no final, no final das contas, ele fez, ele criou uma especificação,

07:34

Um plano ele mesmo, utilizando algumas skills que ele tem, superpoder,

07:39

Aqui que ele chama, mas isso aí é independente. Eu poderia pedir,

07:43

Eu poderia ter as minhas skills, os meus métodos, o meu foco aqui não está...

07:48

Na realidade, no processo de refatoração,

07:51

Na skill que eu vou utilizar para refatorar.

07:53

Meu ponto está aqui, é para a gente entender o quanto a minha refatoração, por exemplo,

07:57

Pode afetar a forma de como eu vejo o nível de acoplamento aqui na minha aplicação, ok?

08:06

Então, no próximo vídeo, a nossa ideia é ver como é que ficou esse nosso...

08:11

Gráfico e o que essa refatoração acabou nos ajudando durante todo esse processo,

08:17

Beleza? Então, vamos nessa!

## Resumo IA

[RESUMO_IA]