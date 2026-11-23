Módulo: IA Labs\
Aula: [Skill N3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18274)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, agora dando continuidade aqui, o que a gente vai fazer é o seguinte,

00:04

a gente vai partir para a criação de uma skill de nível 3,

00:08

tá? E só para relembrar,

00:10

skill de nível 3 é aquela que utiliza referências e scripts,

00:14

um ou outro, ou os dois em conjunto, tá? E para demonstrar isso para vocês,

00:19

a gente vai fazer uma skill com scripts, perfeito?

00:24

E como é que vai ser? Bom, basicamente nós temos aqui...

00:28

Uma nova necessidade, tá? E a necessidade que surgiu foi o seguinte.

00:33

O projeto, ele tem diversos comentários ali de to do,

00:37

fixe, coisas nesse sentido. Então, a gente precisa varrer este projeto,

00:42

entender onde estão localizados esses comentários.

00:47

Baseado nisso, a gente produz ali um pequeno relatório,

00:50

faz uma espécie de mapeamento e coisas nesse sentido, tá?

00:54

Algo relativamente fácil de ser produzido.

00:58

Mas que cabe bastante para uma skill porque

01:01

a gente consegue trazer isso como algo repetitivo,

01:06

dia a dia e totalmente executável. Então,

01:11

para simplificar a nossa ideia aqui,

01:14

o que a gente vai fazer? Vamos fazer um pequeno projeto.

01:19

Eu vou pedir à própria AI para gerar este projeto e

01:22

a partir da geração deste projeto a gente vai dando continuidade.

01:28

Então, vamos lá. Vou pedir aqui para criar um projeto,

01:33

por exemplo, chamado store

01:38

-auth

01:40

com src -auth .js

01:44

e src -report .js.

01:52

Dentro desses arquivos, algumas funções

01:58

referentes.

02:04

rotina de um e

02:08

-commerce padrão.

02:12

Dentro dos arquivos e das funções,

02:18

adicione marcadores de

02:21

tendências espalhados pelo código.

02:27

Utilize, por exemplo, to do para

02:32

itens a fazer, fix para

02:38

necessidade de refactor, por exemplo.

02:44

Gere isso e me dê um relatório no chat.

02:49

Vamos ver aí qual vai ser o resultado.

02:53

Prontinho, pessoal. Então, temos aqui nosso src, temos o package.json,

02:59

vamos dar uma olhada bem rápido aqui. Temos o fixme, temos

03:04

o nosso to do, vamos

03:07

dar uma olhada aqui no nosso report.

03:09

Também temos a presença aqui.

03:12

Claro, projeto fake, só para a gente conseguir trabalhar baseando-se.

03:18

naquilo que nós queremos fazer. Bom, dado isso,

03:22

vou iniciar novamente uma nova sessão. E agora,

03:25

o que eu vou fazer? Criar uma nova skill que

03:31

seja responsável por

03:37

criar um relatório, ou

03:42

melhor, por realizar uma

03:45

Triagem dos marcadores de pendência,

03:51

Por exemplo, do FixMe. De um projeto. Antes de.

04:06

Realizar a criação.

04:09

Confirme o seu entendimento.

04:12

Vamos ver qual que vai ser o resultado.

04:16

De bola. Então, mostrando aqui o.

04:19

Entendimento. Então, eu quero uma nova skill dentro de Cloud Skills.

04:22

Que faça a triagem dos nossos marcadores, que são To Do e Fix. Barreiro projeto.

04:29

Buscando os marcadores.

04:31

Coletar dados de ocorrência.

04:34

Classificar e triagem. Cada um reportar de forma agrupada e acionável. Show de bola.

04:41

Segundo padrão do RAP, eu criaria o meu skill .cmd

04:46

E opcionalmente um script de scan para fazer o graph.

04:49

Beleza. Então, ele está me perguntando aqui o que eu quero criar.

04:53

Quero criar To Do e Fix Me.

04:58

Relatório no chat por enquanto.

05:01

Só catalogar.

05:03

Priorizar e sugerir. E a estrutura, inclusive,

05:07

Ele já até me deu um script para fazer scan ou só skill.

05:12

Como ele já me deu, eu vou já trabalhar junto ao script.

05:18

Mas caso ele não tivesse dado,

05:21

Quero passar aqui uma visão de como e o porquê

05:24

Que a gente está utilizando essa escolha de scripts neste momento.

05:31

Enquanto ele vai fazendo aí, vamos bater um papo sobre isso.

05:34

Galera, o que acontece é o seguinte.

05:36

Existem algumas tarefas, como já falamos anteriormente,

05:39

Que são de cunho determinístico.

05:42

E a gente sabe que inteligência artificial é não determinística. O que isso quer dizer?

05:47

Quer dizer que não determinístico é eu perguntar alguma

05:50

Coisa e vou receber diversas respostas contendo o mesmo contexto.

05:56

Então, um exemplo fácil. Se eu perguntar agora...

06:00

Vamos abrir aqui uma

06:03

Nova seção. Se eu perguntar aqui um oi, temos aqui um resultado.

06:12

Pergunto de novo.

06:14

Olha só, é um outro resultado. Isso é não determinístico. Ou seja,

06:20

Ele segue o mesmo padrão de inferência dentro de um mesmo contexto,

06:24

Porém, a resposta vem de forma diferente.

06:28

Quando eu estou falando de algo determinístico,

06:30

Que é o nosso script, ou...

06:32

Linters, formatadores e outras coisas existentes dentro do mundo da engenharia,

06:38

Eu estou falando de algo que eu tenho a certeza

06:41

Que vai ser executado e sempre vai devolver a mesma resposta.

06:47

E por que isso é importante?

06:48

Pelo simples motivo de que quando eu atrelo a algo determinístico,

06:53

Eu faço algo muito importante para a AI.

06:57

Eu dou o resultado que eu... Então,

07:01

Eu tenho a garantia de que a busca vai acontecer.

07:06

Por quê? Se depender só da AI, ela pode buscar,

07:10

Ela pode falar que buscou, ou ela pode buscar só 20%, 30%,

07:16

50%, porque quem decide é ela. A inferência é dela.

07:21

Quando eu tenho um script, isso não acontece, por quê? Olha só.

07:26

Eu estou pedindo para você executar e o script,

07:29

como é algo determinístico, vai me trazer 100% de tudo.

07:32

Isso, no final das contas, o que a gente ganha?

07:36

A gente ganha maior confiança. É basicamente, de novo,

07:40

o quality gate que nós estamos aqui colocando dentro da nossa

07:45

skill para garantir que ela execute aquilo que tem que ser executado. Beleza?

07:53

Mas voltando aqui, a gente tem então a nossa skill criada junto com o script.

07:58

Vamos dar uma olhadinha aqui.

08:00

Primeiro na nossa skill.

08:03

Então, veja bem que ele fez primeiro tudo em português,

08:06

conforme a gente já vinha trabalhando.

08:12

Agora, nosso foco não vai ser analisar de fato

08:15

o processo que ele está fazendo na skill. E aqui...

08:20

Ele veio e me trouxe o meu script determinístico,

08:23

que é muito simples de ser entendido.

08:24

Basicamente, é um script bash. Ele tem aqui o meu partner a ser analisado,

08:31

excluir alguns diretórios e alguns tipos de arquivo.

08:35

Feito isso, o que ele vai fazer?

08:37

Ele vai simplesmente ler todos os

08:40

meus diretórios em busca deste partner aqui.

08:44

Se ele encontrar alguma coisa...

08:46

ele salva e depois me mostra, tá? Quando eu digo diretórios,

08:50

eu me refiro também aos arquivos que estão inclusos dentro do diretório.

08:53

Se a gente volta aqui na skill, olha só,

08:56

a gente tem o primeiro passo, que é o quê?

08:59

Executar esse meu arquivo, arquivo determinístico.

09:02

Vai ser executado 100%, depois, baseado na resposta dele,

09:07

aí sim eu tenho a classificação ocorrendo.

09:12

E aí, galera, para finalizar, eu tenho aqui um critério de prioridade.

09:17

No qual. O alto. Eu vou corrigir o comportamento. Médio. São melhorias. Relativamente.

09:27

Importantes aqui. De performance. Validação. E coisas. Neste sentido.

09:31

E também. Tenho. Itens de. Baixa.

09:36

Prioridade. Que é. Nice to have. Alguns tipos de polimento. E coisas.

09:39

Neste sentido. Para finalizar. Produzo então. Um pequeno relatório. Fechado? Bom.

09:46

O que eu posso fazer? Agora eu posso executar, então, a minha

09:52

pendence triage. E aí a gente vai dar uma olhada no que vai acontecer.

10:00

Bom, pessoal, já temos aqui o retorno e olha só o resultado.

10:04

A gente tem exatamente aquilo que nós gostaríamos.

10:10

Temos aqui o relatório,

10:11

o médio, o baixo e as minhas recomendações. E note o seguinte,

10:15

vamos aqui no run shell. Olha só o que ele rodou aqui.

10:19

o nosso Bash com userScan. Ou seja,

10:23

agora a gente tem a nossa skill que a gente acabou de criar,

10:26

nível 3, utilizando como exemplo um script.

10:31

Poderia também ser uma referência ou referência e script. Nesse caso,

10:37

eu poderia ter aqui dentro referências para classificar listas de classificação,

10:43

o que realmente é.

10:45

o que realmente é médio, o que realmente é baixo,

10:49

e assim por diante. Fechado? Então, dessa forma aqui, se a gente quiser,

10:55

A gente pode ir evoluindo essa skill, abrir isso aí dentro do GitHub,

11:01

centralizar isso aqui para, de fato,

11:04

ser corrigido posteriormente, coisas nesse sentido, beleza?

11:08

A intenção maior neste momento é, primeiro, a lógica por trás do...

11:15

como e o porquê que a gente está gerando uma skill,

11:19

tá? E principalmente essa questão do determinismo ou não determinismo. Beleza, pessoal?

## Resumo IA

[RESUMO_IA]