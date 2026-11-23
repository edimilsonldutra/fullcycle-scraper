Módulo: IA Labs\
Aula: [Frontmatter e progressive discloure](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18268)

## Resumo da aula



## Transcrição

00:00

Show de bola, galera! Então, vamos lá!

00:01

Falando agora um pouquinho mais sobre a skill de fato e como é uma skill na prática, tá?

00:09

Conforme eu disse pra vocês,

00:10

a gente apresentou ali o que é uma skill e

00:12

agora eu trouxe pra vocês uma pequena skill,

00:15

tá? De Code Review,

00:17

e aí a gente vai entender na prática como ela funciona. Primeiro ponto,

00:22

nós temos aqui um ponto cloud / skills, são pastas, tá?

00:27

/ o nome da nossa skill, TeamCodeReview. Depois disso,

00:31

eu sempre terei um arquivo que se chama skill.md.

00:34

Aqui é o nosso arquivo de instrução, que é de fato a nossa skill.

00:40

Se vocês repararem bem, ao acessar o nosso skill.md,

00:43

nós temos algo aqui em cima, logo de cara,

00:47

e depois a gente tem o que a gente chama de corpo,

00:50

que é o corpo da nossa skill. O que é este arquivo aqui?

00:54

Este arquivo nada mais é... Que é o nosso front matter,

00:57

que nós vamos entender daqui a pouco o que ele faz, tá?

01:01

Logo depois disso, a gente tem o corpo da nossa skill,

01:05

que são basicamente instruções. E aí,

01:08

eu vou abrir aqui em preview para ficar até

01:12

mais fácil da gente visualizar o conteúdo do nosso Markdown,

01:17

tá? Então, aqui eu tenho o mesmo nome, que é o nome da pasta.

01:21

Temos o mesmo nome aqui em cima nas propriedades.

01:23

Eu tenho que ter esse nome aqui também.

01:26

E seria o meu início do corpo. E após isso,

01:29

a gente tem uma série de instruções. Note que essa skill, inclusive,

01:35

o que ela está fazendo aqui? Ela está utilizando comandos Bash.

01:38

Então, apesar dela não ser um código, uma função,

01:42

eu disse pra vocês que uma skill pode executar comandos.

01:47

E um dos comandos que ela vai executar é o Bash.

01:51

Porém, nada impediria a gente de executar comandos Node, Java,

01:56

qualquer coisa que faça sentido ali no contexto da skill,

02:01

que rode dentro de um terminal, por exemplo.

02:03

A gente conseguiria trabalhar aqui sem nenhum tipo de problema, tá?

02:07

Depois a gente tem os meus steps bem definidos,

02:10

tá? E aí eu tenho aqui basicamente a padronização do que eu espero de saída, certo?

02:16

Repare que nessa skill, a gente tem também a presença de algumas outras pastas,

02:21

né? Isso também a gente vai entender logo mais, porém,

02:25

de forma bem rápida, nós temos aqui a presença de um script,

02:28

a gente tem a presença de um arquivo que se chama reference,

02:30

e a gente tem a presença de um arquivo que se chama eval,

02:33

ok? E galera, para a gente entender o que são essas pastas,

02:37

porque elas fazem parte de uma skill, eu vou voltar aqui no nosso Scale Draw,

02:41

porque agora a gente precisa primeiro entender...

02:44

O que é esse arquivo aqui para depois, como base,

02:47

nós entendermos as pastas? Primeira coisa,

02:50

referente ao front matter. Esse arquivo, basicamente,

02:54

vai ser um bloco que está sempre no topo da sua skill, como a gente percebe aqui.

03:00

E ele é um bloco no estilo YAML, com determinadas propriedades.

03:05

A questão que vocês têm que entender aqui é

03:07

Que grande parte dessas propriedades são opcionais.

03:12

Porém... Existem duas propriedades que são extremamente importantes, tá?

03:17

Porque elas vão nos guiar, inclusive, para a execução ou não dessa skill.

03:22

Que é, primeiro, o name. E logo depois disso, nós temos a description.

03:28

Então, de forma geral, o que é o front matter?

03:31

Front matter nada mais é que este conjunto de propriedades que

03:36

aparecem num bloco YAML e estão sempre no topo da skill,

03:41

tá? E que vai nos servir...

03:42

para a identificação de alguns padrões, como por exemplo,

03:46

padrão de identidade e de disparo,

03:49

que são através do name e da minha description.

03:53

Outras coisas que a gente pode detectar padrão,

03:58

quando ou onde a gente pode invocar.

04:01

Existem algumas propriedades, como por exemplo,

04:04

uma que se chama DisableModelInvocation,

04:08

que vai fazer o quê?

04:09

Vai impedir o seu CLI, no meu caso aqui, o Cloud Code, de carregar a skill sozinha.

04:15

Ela só vai rodar quando você

04:17

digitar o slash command team code reveal.

04:23

Além dos dois padrões que eu falei com vocês,

04:27

que é o padrão de identificação e disparo,

04:31

e depois, quem pode invocar, nós temos também um padrão de ferramenta. Então,

04:37

eu vou colocando aqui algumas informações e... que a gente pode utilizar,

04:42

lembrando que grande parte dessas que eu estou passando para vocês são opcionais.

04:46

Então, quando a gente chega no padrão de ferramenta,

04:49

e aqui o foco é muito mais voltado na segurança,

04:53

nós temos a presença de um cara que se chama Allowed Tools, por exemplo,

04:56

que é uma propriedade que vai dizer quais são as

05:00

tools que o seu CLI pode utilizar sem pedir permissão.

05:04

Da mesma forma que eu tenho o Allowed Tools, eu tenho o Disallowed Tools,

05:20

e aí, a gente segue o mesmo padrão daqui de cima. Então,

05:24

eu poderia colocar quais são as tools presentes ali

05:27

que eu quero habilitar ou desabilitar por padrão.

05:31

Outra coisa importantíssima, que é um outro padrão,

05:34

é a parte de execução. Qual é o modelo e qual é a forma de execução. Então,

05:40

eu posso ter propriedades que se chamam model,

05:42

posso ter o effort, que é a eficiência,

05:46

ou seja, o nível de esforço de raciocínio enquanto a skill vai rodar,

05:52

também posso ter um context, que é o quê?

05:56

Meio que um fork para que a skill consiga rodar ali num

06:01

subagente isolado e o corpo da skill vira o prompt do subagente.

06:07

Mas, novamente, como eu sempre falo,

06:10

todos esses itens aqui vão depender daquilo que você quer fazer. Por padrão,

06:16

e o que vocês têm que ter noção e ter em mente é o name e a description.

06:21

São itens obrigatórios. Aqui, esses caras,

06:24

a gente precisa trabalhar muito bem eles, principalmente a description.

06:28

E por quê? Porque a description é essencial para a produção de qualquer skill.

06:35

Explico o porquê.

06:37

Esse cara, basicamente, vai descrever o que a skill faz.

06:41

Mas não é apenas uma descrição simples. Na verdade,

06:45

vai servir como um classificador. Tudo que a gente escreve aqui,

06:49

eu vou utilizar isso como um classificador. Para quê?

06:53

Para que o Cloud consiga interpretar isso e saber quando executar a skill ou não.

07:00

Para quem não sabe, uma skill pode ser executada de duas formas.

07:03

Já apresento essas formas para vocês neste momento. Vou

07:08

abrir aqui o meu Cloud Code.

07:10

E a primeira forma é através do nosso slash

07:16

command. Então,

07:17

eu tenho aqui o barra e eu tenho a presença

07:19

de várias skills e comandos que eu posso utilizar.

07:21

A outra é através de contexto. Então, por exemplo, eu quero fazer um code review.

07:29

O que vai acontecer aqui? LLM vai tender a interpretar. Code Review,

07:34

vai encontrar uma skill que bata com esse mesmo contexto de Code Review,

07:39

no nosso caso aqui é a Team Code Review, tá? E para que ela consiga encontrar isso,

07:44

a nossa description tem que estar muito bem feita, tá?

07:47

Por quê? Porque ela é o nosso classificador.

07:49

Ela é quem vai editar se o Cloud vai chamar ou não.

07:52

Na verdade, nem é o Cloud, né? O Cloud só vai disparar.

07:55

O modelo vai tomar essa decisão efetivamente,

07:58

independente qual seja o modelo que você esteja utilizando. Então, por isso,

08:02

eu gosto sempre de falar que esses dois carinhas são obrigatórios e a

08:05

gente tem que ter um carinho no momento de escrever esses caras aqui.

08:10

Obviamente, durante o andar das aulas,

08:13

a gente vai ter alguns padrões e tudo mais que...

08:16

a gente consegue implementar aqui para garantir que

08:18

a gente faça aqui da melhor maneira, né?

08:20

Os famosos best practice, ok? Vendida essa parte, então, do front matter,

08:25

a gente tem que voltar aqui para a gente finalizar

08:28

sobre um cara que se chama progressive disclosure,

08:32

tá? Esse cara também é extremamente importante porque, através dele...

08:38

Mas principalmente através dos níveis que a gente consegue

08:41

atingir devido ao uso do Progressive Disclosure,

08:44

a gente vai fazer com que a skill se torne cada

08:47

vez mais capacitada e impactante mesmo a nível de resultado,

08:51

tá? Então, o que é esse cara que se chama Progressive Disclosure?

08:55

Nada mais é que uma estratégia que vai revelar as informações a nível de camadas,

09:00

tá? E o ponto principal é que só carrega -se o necessário a cada momento.

09:05

Se eu pudesse fazer uma analogia bem rápida aqui,

09:08

pensa que você está dentro de uma biblioteca ou de

09:12

uma livraria e você quer comprar um determinado livro.

09:15

O Progressive Disclosure basicamente vai te revelar informações em camadas. Então,

09:21

você pega o seu livro e a primeira coisa que você lê

09:23

num livro quando você está buscando algo é o quê? A capa.

09:27

E logo atrás você vira o livro para ver ali o prefácio,

09:30

para ver um pequeno resumo daquilo que você está buscando.

09:35

Primeiro, analisa. Faz sentido ou não faz sentido? Se fizer, o que você faz?

09:40

Você abre o livro e continua lendo um pouco mais sobre os índices, a introdução,

09:45

para ver se realmente aquilo ali que você está buscando faz sentido ou não. Se fez,

09:51

você vai para um próximo nível, que é o que? Você vai começar a ler o livro,

09:55

vai focar em detalhes específicos que se encontram

09:58

Dentro de capítulos específicos e aí

10:00

Sim, a gente consegue ter as informações completas

10:02

De forma muito detalhada daquele livro.

10:05

A skill vai funcionar exatamente desta forma.

10:08

E por que isso aqui a gente considera o coração de tudo acerca de skill?

10:15

Porque ela vai te dar escala.

10:16

Então, eu consigo ter dezenas de skills instaladas porque o

10:20

meu custo permanente é só o nível 1.

10:23

E a gente vai entender o que é esse nível 1.

10:25

E somente quando eu preciso de mais detalhes,

10:28

fazendo analogia ali com o livro, é que eu vou ter acesso ao nível 2 e 3.

10:32

E aí, esses níveis 2 e 3,

10:35

eles só vão passar a pesar de fato quando a skill for realmente utilizada.

10:40

Então... De forma geral, existe até algumas boas práticas,

10:43

já que a gente já tem a tendência de começar a utilizar,

10:46

que é o quê? Toda boa prática,

10:48

ela vem dos níveis de skill, ou seja, o corpo curto, o que é o corpo?

10:53

Basicamente, é essa parte aqui, logo abaixo do front matter, tá? Depois,

10:59

eu vou empurrar todo o peso para dentro daquela pastinha referência,

11:04

e aí, por isso que existe aquela... a pasta de referência,

11:09

para assim eu começar a utilizar o nível 3.

11:12

E quando eu tenho dados ou análises determinísticas,

11:16

a gente vai imputar essas informações dentro de scripts.

11:20

Por isso que existe aquela pastinha lá chamada scripts.

11:24

Dessa forma, eu consigo garantir uma precisão de disparo. E por que isso?

11:31

Porque a decisão vai acontecer sobre os textos,

11:33

curtos que estão lá dentro do nível 1. Então, uma boa descrição,

11:37

aquilo que a gente já havia conversado,

11:40

é o que vai separar da forma que foi disparado,

11:42

se foi de uma forma correta ou não. E aí, o que é essa questão de níveis?

11:48

Porque até agora a gente entrou ali em dois pontos,

11:51

que é o front matter e o progressive disclosure.

11:54

E aí a gente começou a falar muito sobre esses níveis. Basicamente, pessoal...

11:58

Nós temos três níveis para se trabalhar com uma skill.

12:00

O nível 1, basicamente, é o nome mais a descrição. Então,

12:05

quando a gente gera uma pasta, gera o arquivo skill.md,

12:09

por padrão, eu disse para vocês o quê?

12:11

Que ele deve, obrigatoriamente, inclusive,

12:13

deixa eu até retirar isso aqui, ele deve, obrigatoriamente,

12:18

ter o name e o description muito bem desenvolvidos. Por quê?

12:21

Porque aqui a gente já chega no nível 1.

12:24

E esse nível 1... são os metadados, porque eles são sempre carregados. Aqui,

12:30

que a partir do contexto ali que eu estou passando no prompt,

12:35

é que vai ser tomada a decisão de, opa,

12:38

tenho que chamar essa skill ou, provavelmente, não preciso chamar essa skill, tá?

12:43

Outra coisa importante é quando a gente passa para o nível 2,

12:48

porque aqui, ao ser identificado, que realmente faz sentido,

12:54

usar e executar essa skill, o que vai acontecer? Eu vou ter a presença do meu corpo,

12:59

que nada mais é que as instruções que ele deve executar. Então,

13:03

aqui eu vou ter o passo a passo daquilo que deve ser executado.

13:08

O nível 2 vai ser lido só quando a task casa com a description.

13:12

E aqui tem mais ou menos um cálculo de token que pode ser gasto nesse processo.

13:17

Por fim, dado a leitura... do nosso nível 2, que é o corpo da skill,

13:23

ela vai ter decisões a serem tomadas.

13:25

E essas decisões podem ser download em mais contexto,

13:29

através das minhas pastas de referência, executar um comando, um script,

13:34

através da minha parte de scripts.

13:38

E é aqui que eu vou realmente começar a trabalhar com a

13:41

minha skill para dar bastante contexto e resolver o problema que eu desejo.

13:45

Então, se você reparar bem, tudo acontece... de maneira progressiva mesmo,

13:51

né? A gente começa aqui no nível 1,

13:53

depois vai para o nível 2 e chega até o nível 3. Inclusive,

13:58

a gente pode utilizar essa mesma ideia de design

14:02

para que a gente consiga estruturar as nossas skills. Então,

14:06

a gente começa ali do nível 1, depois... Faz o nível 2,

14:09

que é o corpo, depois chega no nível 3. Óbvio,

14:12

nem toda skill vai ter a necessidade de passar por todos os níveis.

14:16

Algumas vão parar no nível 2, né? O nível 1,

14:19

é certeza que vai ter. Mas algumas podem parar no nível 2 e outras,

14:22

grande maioria, vai chegar com um peso maior no nível 3, tá?

14:26

E também com pesos diferentes, né? A gente pode ter muitas informações no nível 3,

14:30

pode ter poucas informações e assim por diante.

14:32

Então... O Progressive Disclosure basicamente vai conseguir

14:37

fazer esse carregamento por etapa,

14:38

mas também vai nos ajudar, de certa forma,

14:41

a fazer o design da nossa solução se a gente utilizar um pensamento de níveis.

14:48

Primeiro eu faço isso, aí eu subo para o nível 1, depois eu faço isso,

14:51

subo para o nível 2 e assim por diante até chegar ao nível 3. Beleza, pessoal?

## Resumo IA

[RESUMO_IA]