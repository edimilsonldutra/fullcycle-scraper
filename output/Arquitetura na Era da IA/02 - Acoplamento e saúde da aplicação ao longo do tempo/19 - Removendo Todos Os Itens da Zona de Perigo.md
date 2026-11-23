Módulo: Arquitetura na Era da IA\
Aula: [Removendo Todos Os Itens da Zona de Perigo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18129)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, agora que eu terminei essa parte que eu estava trazendo aqui para vocês,

00:07

o que eu vou fazer? Primeira coisa, eu vou dar um commit.

00:10

Vou dar um commit aqui.

00:14

E depois desse meu commit,

00:17

eu acho que eu posso fazer até um handoff para eu ter um pouquinho de contexto,

00:20

mas daí a minha ideia é fazer

00:25

como se a gente tivesse um prompt geral,

00:28

um prompt único.

00:30

que ele vai tentar tirar de uma vez ali todos os caras da zona de perigo, tá?

00:38

Recomendo você fazer isso, depende muito,

00:41

porque é complexo refatorar todas as coisas de uma vez dessa forma.

00:46

Por outro lado, se você tem ali uma cadeia de segurança baseada nos testes,

00:51

você fica mais tranquilo. Basicamente,

00:54

o que eu estou querendo dizer para você é que...

00:57

Não necessariamente vá cegamente pedindo para o seu sistema sair

01:01

refatorando tudo e tirando da zona de perigo.

01:04

Faça isso em iterações, como a gente fez um piloto,

01:07

para a gente sentir se estava indo ok.

01:09

E depois você pode ir aplicando de uma forma um pouquinho mais massiva,

01:13

mas sempre passo a passo para evitar que você faça uma mudança

01:18

muito drástica e eventualmente um detalhe ou outro possa quebrar seu sistema.

01:22

Então aqui eu vou fazer um handoff e o que eu quero fazer agora é fazer uma...

01:27

Refatoração geral,

01:29

tirando todos os componentes da zona de perigo.

01:41

Trabalhar com

01:44

inversão de dependência,

01:50

seguindo inclusive os padrões que utilizamos.

01:58

Na refatoração do

02:04

database.ts e

02:10

aqui eu vou colocar veja o histórico do git, galera, uma dica aqui para você, tá?

02:16

Toda vez que você for fazer algo e que você quer usar algo como base, tá?

02:24

Pede para a IA olhar o histórico do Git,

02:27

ele vai conseguir fazer um antes e depois, tá?

02:29

Aqui nesse caso, eu estou fazendo só o handoff,

02:31

eu estou gerando um arquivo para eu utilizar

02:33

um contexto inicial na minha próxima iteração,

02:36

tá? Mas de forma geral, às vezes eu fiz uma refatoração,

02:40

às vezes eu fiz algo que seguiu um determinado padrão,

02:44

né? E eu quero fazer isso novamente com outro componente,

02:49

com outra classe, em outra situação.

02:51

Como eu já fiz isso no passado e eu tenho

02:54

o histórico do Git mostrando isso ponto a ponto,

02:58

o que eu posso fazer é olhar o histórico do Git e

03:02

entender o que foi feito baseado nesse padrão para você poder replicar.

03:06

Então, o Git é uma forma absurdamente fantástica para que

03:11

você consiga utilizar e conseguir realmente mostrar para a IA,

03:17

através dos diffs dela, como que ela pode...

03:21

seguir e dar os próximos passos do que já foi feito antes, beleza? Bom, galera,

03:28

o Randolph criou aqui o meu arquivo para tirar as coisas da zona de perigo,

03:33

ele deu um resumo do que esse cara cobre, ou seja, olhar os commits,

03:38

Tirar os caras da zona de perigo, que é o snapshot atual,

03:42

incluindo pontos de atenção, ciclos de inverter uma aresta via porta,

03:46

Trio de utilitários.

03:48

Em relação à parte de injeção de dependências,

03:51

comandos, convenções, o repositório e etc.

03:53

Então, eu não estou muito preocupado, como eu disse para vocês,

03:56

com a qualidade do código,

03:58

eu estou mais focado aqui na parte do

04:00

acoplamento com esse bendito gráfico aqui nosso.

04:02

Então, o que eu vou fazer agora? Aqui, no caso do Cloud, eu posso até colocar,

04:07

Na realidade, o Codex tem isso também, um Go, e a minha condição é, baseado nesse

04:15

meu arquivo, e no arroba...

04:19

main sequence.html

04:26

Seu objetivo é fazer

04:31

uma refatoração ao ponto

04:36

de tirar todos os

04:39

arquivos, /classes, /aqui componentes da

04:46

zona de perigo, tá?

04:49

Dessa zona de perigo

04:53

Veja, utilize o histórico

04:58

do Git, utilize o histórico

05:02

do Git no passado para entender o padrão e

05:11

trabalhe com múltiplos agentes e

05:17

no caso da refatoração, trabalhe com

05:24

No final, quero

05:29

garantir que meu software

05:34

esteja devidamente saudável em

05:43

relação ao

05:46

acoplamento e suas proporções. E

05:56

nesse ponto aqui, galera, eu estou colocando o gol, por quê?

06:01

O gol, basicamente,

06:03

ele vai ficar em loop até ele resolver esse tipo de problema. Então,

06:07

acho que esse aí é um grande ponto. E,

06:10

normalmente, no Go você pode também, ele recomenda,

06:13

diante dessa situação, faça isso, ou caso contrário,

06:17

não faça. Então, tem diversas formas de você trabalhar.

06:20

O ponto que eu coloquei aqui, basicamente,

06:22

é para ele realmente focar em todos esses caras.

06:28

Eu posso colocar, ao terminar,

06:32

Aqui, reveja, nesse caso, o nosso projeto é pequeno,

06:37

né? Vou colocar, reveja todos os componentes para

06:42

garantir que o software

06:52

atingiu, quer dizer,

06:57

para garantir que a

06:59

refatoração atingiu o seu objetivo.

07:04

O que eu estou dizendo com isso,

07:06

galera? Pode parecer algo muito bobo, tá? Mas o que eu tô querendo dizer,

07:10

muda muito do que a IA vai fazer.

07:12

Porque ela vai terminar o negócio. Mas depois que ela terminar,

07:15

eu passei mais um comando. Revise tudo o que você tá fazendo, tá?

07:20

Existem workflows prontos para isso, etc. Se você olhar mesmo,

07:24

superpowers, coisa que você aprendeu no SDD,

07:28

na parte de harness, onde você tem implementado, verifique,

07:31

ou trabalham com subagentes e coisas desse tipo, tá? Então,

07:35

existem várias formas.

07:36

Eu não estou querendo utilizar nada dessas skills tão prontas,

07:39

a não ser que o Cloud carregue em relação a isso. Provavelmente,

07:43

eventualmente, ele vai carregar a skill ali de code review.

07:47

De trabalhar com TDD e coisas do tipo, tá?

07:49

Mas perceba que eu não estou forçando a barra aqui.

07:52

Eu estou querendo trabalhar de uma forma mais natural

07:54

para que a gente veja esse gap trabalhando,

07:56

mas que a gente não fique ali com aquela sensação de nossa,

08:01

não fiz tudo automático. A ideia não era fazer tudo automático.

08:05

Por isso que eu estou trabalhando de forma bem crua,

08:08

aqui bem crua nos prompts, nos pedidos,

08:11

mas somente para a gente entender essa ideia. Vou dar um Enter aqui.

08:16

E vou aguardar essa refatoração,

08:18

no próximo vídeo a gente volta e vê o que aconteceu.

## Resumo IA

[RESUMO_IA]