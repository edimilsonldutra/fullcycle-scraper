Módulo: IA Labs\
Aula: [O que é uma skill](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18267)

## Resumo da aula



## Transcrição

00:00

Bom, galera, e para começar, então,

00:01

vamos entender aqui o que é uma skill de verdade, tá?

00:05

E a gente vai falar um pouco também sobre o padrão de agent skills que

00:08

vai nos guiar a partir de todas as aulas aqui, daqui para frente e que,

00:14

com base neste padrão,

00:15

a gente vai começar a construir diversas skills ao

00:18

longo do nosso percurso aqui em conjunto,

00:21

tá? Então, para a gente começar, vamos já falar o... que é, de fato, uma skill.

00:27

Primeira coisa que é muito importante da gente entender

00:30

é que a skill não é um código,

00:34

ela é apenas um conhecimento que o Cloud ou

00:37

qualquer outro CLI que você esteja utilizando,

00:40

a gente pode utilizar a nomenclatura CLI ou Harness, vai ler sobre a demanda.

00:47

E o mais importante de entender o que é uma skill é entender o que não é uma skill.

00:54

Isso é super interessante da gente falar,

00:56

porque existem N fatores que fazem, principalmente nós,

01:01

desenvolvedores, criar algumas associações relacionadas ao que de fato é uma skill.

01:08

Mas, entendendo o que não é,

01:11

eu acabo dizendo que fica até mais fácil da gente entender o que ela é.

01:15

Se eu fosse pontuar para vocês o que não é uma skill. A skill não é um código,

01:21

porém, ela pode executar um código. A skill não é uma função,

01:27

mas pode executar algo repetidas vezes, exatamente como uma função faz.

01:33

E a skill não é um endpoint,

01:36

por exemplo, só que ela pode consumir uma via ferramentas bash,

01:40

inclusive ela pode consumir coisas externas.

01:44

No final das contas, pessoal,

01:46

a skill nada mais é que uma pasta com instruções Markdown,

01:51

no qual o seu CLI que você escolheu utilizar vai conseguir

01:56

ler sob demanda e executar aquilo que está nas instruções do Markdown.

02:02

Mais para frente, a gente vai entender também que, baseado neste Markdown,

02:05

a gente consegue trabalhar com níveis diferentes.

02:09

de construções de skill e a gente consegue

02:12

ir cada vez mais agregando habilidades dentro

02:16

dela para que a gente consiga realmente criar algo

02:19

que seja útil a nível de desenvolvimento,

02:22

tá? Mas antes disso, acho que é importante também...

02:25

falarmos a respeito do padrão aberto que foi gerado a partir das criações da skill. Então,

02:32

existe um carinha que se chama agent skills,

02:34

que ele basicamente não é um recurso proprietário,

02:38

é uma convenção de arquivos, conforme eu havia falado para vocês,

02:43

a gente tem ali a nossa instrução,

02:44

o Markdown, e dentro de uma determinada pasta,

02:47

com uma determinada estrutura que a gente deve,

02:50

por obrigação, segui-la. A gente consegue utilizar este padrão aberto. Então,

02:57

podemos dizer que ela é uma convenção de arquivo e ela é totalmente portátil, ou seja,

03:02

a mesma skill pode rodar em vários locais,

03:05

porque todos leem de um mesmo jeito, de um mesmo formato,

03:11

obedecendo aquelas convenções de arquivo que nós havíamos falado.

03:16

E aí você deve se perguntar, ok,

03:18

eu entendi o que é uma skill, porém...

03:21

Eu não entendi o que de fato eu posso fazer com isso.

03:25

E agora eu vou mostrar para vocês o porquê e quando vocês devem utilizar uma skill,

03:31

Perfeito? Então, começando aqui do porquê a gente deve utilizar.

03:35

Vamos pegar alguns cenários sem skill e com skills,

03:39

Só para ficar fácil aqui o nosso exemplo,

03:41

Tá? Imagine então que você tem que

03:44

Ter um determinado padrão dentro do seu time, tá?

03:50

Foi desenvolvido um prompt que vai resolver este problema,

03:55

Aplicando o padrão toda vez que necessário.

03:58

Sem a skill, o que você deveria fazer?

04:01

Você vai reaplicar este padrão a nível de time em

04:04

Todo prompt que você pedir para a LLM resolver.

04:08

Já com a nossa skill, a gente pode criar este padrão, ou seja, criar um wrapper ali,

04:14

A instrução deste padrão, e este arquivo vai ser... lido sozinho na hora certa.

04:20

Um outro ponto que é interessante é que quando você tem

04:24

Um determinado conhecimento que vive na cabeça ali de um desenvolvedor específico,

04:29

De um tech lead específico,

04:31

Ele só vive no momento em que essa pessoa está disponível na empresa.

04:36

Já com a skill, a gente consegue reverter isso,

04:40

Fazendo com que a gente consiga versionar aquele determinado conhecimento,

04:44

Aquela determinada habilidade dentro do Git,

04:47

Ou até mesmo ser revisado em uma determinada PR.

04:51

Outra coisa que veio também para ajudar bastante é aquela

04:55

Questão do cada dev faz do seu jeito.

04:58

Sem a skill, isso aqui acaba sendo bem claro. Porém,

05:02

Quando nós temos uma skill que visa padronizar alguma coisa,

05:06

Nós tendemos a ter resultados consistentes entre os processos,

05:12

Pessoas e sessões.

05:14

Porque a gente bem sabe... que o uso de uma LLM é algo não determinístico. Então,

05:20

Mesmo que eu peça exatamente com o mesmo prompt,

05:24

O meu resultado vai sempre ter um contexto diferente.

05:29

Mesmo que a essência da resposta seja muito parecida,

05:34

Exatamente aquilo que eu quero ver, mas a forma de resposta,

05:37

O contexto da resposta vai ser... Sempre diferente.

05:39

E aí com isso que a gente meio que consegue padronizar isso também, tá?

05:43

Outra coisa que é importante é na parte

05:46

Ali do modelo vai conseguir improvisar em passos determinísticos.

05:51

Existem alguns momentos dentro do processo de desenvolvimento

05:55

Que a gente utiliza diversas ferramentas determinísticas,

05:58

Né? Como formatters, linters, pra gente atestar se determinada...

06:04

Arquivo ou algo nesse sentido está seguindo o padrão ou não.

06:07

Isso acaba sendo uma imposição determinística, porque ele deve,

06:11

Obrigatoriamente, seguir um passo a passo determinístico.

06:15

Já com a skill, o que acontece? O passo exato, ou seja,

06:19

O padrão que você colocou, ele deve virar um script. E aí,

06:25

Quando ele vira um script, a gente tem o quê?

06:27

A gente tem a padronização, de fato, daquilo que está sendo verificado. E aí,

06:33

A gente tem uma saída idêntica que a gente pode colocar dentro de

06:38

Uma skill a partir do nível que nós estamos trabalhando de uma skill.

06:42

A gente vai entender isso em breve. E a gente consegue,

06:44

A partir deste resultado de script, resolver várias...

06:49

Ações a serem tomadas.

06:51

Outra coisa que é muito importante é que quando nós trabalhamos sem skill,

06:56

o onboard acaba sendo uma pergunta para um companheiro de time,

07:00

o que é interessante, porém, a todo momento acaba dificultando o processo.

07:05

Quando a gente está utilizando uma skill,

07:07

a gente pode basicamente fazer com que ela nos ajude neste processo.

07:12

De onboarding. Por quê?

07:14

Porque a gente pode criar diversas skills que vão resolver

07:17

problemas específicos sob demanda e orientar a pessoa que está chegando,

07:22

seja uma pessoa nova na empresa ou uma pessoa nova naquele projeto,

07:25

para utilizar aquelas skills que vão ensinar,

07:29

entre aspas, o Cloud a responder da forma...

07:33

que você deseja. E quando eu digo o Cloud,

07:36

eu estou me referindo ao CLI / Harness que você está utilizando.

07:41

Um outro ponto que é importante também da gente entender é

07:44

o fato de quando nós precisamos utilizar uma skill ou não.

07:49

A primeira coisa que eu diria é a nível de reutilização. Ou seja,

07:53

se você repete isso em vários prompts, dias, projetos,

07:56

é muito provável que você vai precisar...

08:00

trazer esse conhecimento para uma skill. Mas depois, durante as aulas,

08:04

a gente vai fazer alguns modelos mentais para ajudá-los nesse processo de decisão.

08:10

Outra coisa que é bem importante também é em relação a procedimentos não óbvios. Ou seja,

08:15

tem como um objetivo muito específico? E aí a gente tem exemplos aqui como,

08:20

por exemplo, uma ordem, um padrão de time, convenções a serem seguidas. E o Cloud,

08:25

por padrão, está tendendo a não acertar isso sozinho,

08:29

não está reconhecendo este padrão,

08:31

então é bem provável que você precisa criar essa skill para embutir

08:36

este conhecimento dentro do Cloud ou qualquer outro

08:39

CLI / Harness que você está utilizando.

08:42

E uma outra questão que é muito importante é a nível de estabilidade,

08:46

porque se a regra muda diariamente,

08:49

muito provavelmente você não vai precisar de uma skill. Porém,

08:52

se é algo que foi definido ali e já dura semanas, meses e até anos,

08:57

é bem provável que a gente vai precisar

08:59

também padronizar isso dentro de uma skill.

09:02

Coisa importante, tá? Este carinha aqui, que é voltado à segurança,

09:08

sempre que a gente está fazendo o processo de criação de uma skill,

09:12

nós temos que levar em consideração um padrão chave de segurança, que é o quê?

09:18

Credenciais, dados sensíveis e segredos.

09:21

Ou seja, se isso estiver tendo

09:26

a necessidade de virar uma skill, você vai vetar na hora.

09:30

Por quê? Porque a gente não deve, de modo algum,

09:35

criar skills aí que envolvem esse tipo de situação, segredo,

09:41

credenciais ou coisas neste sentido, tá bom? Então,

09:45

já veta aí do seu to-do list coisas que envolvem esse tipo de coisa. Bom,

09:50

outra coisa que é interessante também é a gente fazer uma pequena analogia

09:55

do que pode virar uma skill e do que pode não virar uma skill.

09:59

Porque acaba sendo, como eu disse, um conceito...

10:04

um pouco difícil de abstrair no primeiro momento.

10:06

porque existem já outras ferramentas que podem ser utilizadas,

10:10

mas pelo fato de que skills estão em grande evidência,

10:14

é algo novo,

10:15

existe a tendência da gente sempre querer utilizar a

10:18

skill sempre para resolver determinados problemas e,

10:22

às vezes, não tem necessidade. Então, por exemplo,

10:25

quando eu tenho aqui um procedimento repetitivo e não óbvio,

10:29

é bem provável que eu vá precisar de uma skill para que a gente consiga...

10:33

fazer o wrapper desta habilidade e então se tornar

10:37

um modelo a ser utilizado a todo momento. Agora,

10:40

quando nós temos algo que o fato é sempre verdadeiro do projeto,

10:46

ou seja, eu preciso me assegurar que aquilo ali seja executado sempre,

10:52

é um padrão imposto,

10:53

é bem provável que eu vou utilizar o CloudMD

10:56

ou até mesmo o Agents .MD para garantir...

11:00

que isso acontecerá. Por quê?

11:02

Porque tanto o cloud .md quanto o agents

11:05

.md são garantia de leitura sempre durante a execução.

11:12

Outra coisa que é importante também é acerca de regras mecânicas,

11:16

como, por exemplo, estilo,

11:18

formatação, linters, coisas nesse sentido.

11:22

Você não precisa colocar isso dentro de uma skill.

11:25

Você pode criar um script que está dentro da sua skill e a skill vai utilizar.

11:30

Ou ainda você pode utilizar as ferramentas tradicionais que nós temos hoje,

11:35

como, por exemplo, o ESLint, para quem é do ambiente Node.

11:41

e fazer com que o ESLint seja executado dentro de uma skill,

11:45

através de um bash command.

11:47

Outra questão que é bem importante é em relação

11:50

a acessos de sistema ou a um dado vivo.

11:54

A gente tem já protocolos prontos para isso.

11:57

Nós temos MCP e nós temos tools também, que inclusive,

12:01

assim como os linters, nós podemos fazer com que a skill...

12:06

Chame determinadas tools, chame determinados MCPs.

12:10

Outra coisa acerca de fatos que são voláteis. Exemplo,

12:16

versões de bibliotecas e coisas nesse sentido.

12:18

Prefiro utilizar buscas via tool ou até mesmo a própria web. A gente tem aqui,

12:24

novamente, padrões já estabelecidos. Obviamente,

12:28

a skill pode utilizar tool de web search para que a gente faça um processo de...

12:34

busca acerca de uma documentação e tudo mais,

12:37

e elabore um guia técnico, uma documentação, um plano de implementação.

12:42

Mas tudo isso a skill faz o uso, ela não cria de fato. E por fim,

12:48

ação explícita com efeito colateral. E aí eu dei o exemplo aqui de deploy.

12:53

Aí nós temos a skill como uso principal,

12:57

porém, utilizando aqui uma annotation.

13:01

ou uma propriedade dentro do seu front matter,

13:04

que a gente vai entender o que é isso,

13:06

que é o DisableModelInvocation. Aqui é o ato de fazer deploy, o passo a passo.

13:13

Claro, existem coisas mecânicas aqui dentro que

13:16

a gente pode utilizar outras ferramentas,

13:18

mas a gente tem um passo a passo de

13:20

Instruções que a gente pode automatizar via skill.

13:24

Então, pessoal, até o presente momento,

13:26

a gente falou um pouco sobre o que é uma skill de fato,

13:31

para que a gente deve utilizar e tudo mais. Agora,

13:34

a gente vai entrar em alguns aspectos mais técnicos que envolvem o uso da skill,

13:40

que é um carinha que se chama Front Matter,

13:42

e um outro carinha que se chama Progressive Disclosure.

13:48

Entendendo esses dois caras aqui,

13:50

as coisas passam a fazer sentido. Na hora,

13:54

porque são itens muito importantes para que a

13:57

gente consiga desenvolver uma skill de fato,

14:00

uma skill boa, tá?

14:02

Só que antes da gente começar a falar sobre eles,

14:05

eu gostaria de mostrar para vocês uma pequena skill, bem rápida,

14:09

só para a gente associar a tudo que foi falado aqui a uma prática.

14:13

Vai ser meio que o nosso Hello World ali da skill. Fechado? Então,

14:17

vamos dar uma olhada na nossa próxima aula sobre isso aí.

14:20

E a gente dá continuidade depois no Front Matter e no Progressive Disclosure.

## Resumo IA

[RESUMO_IA]