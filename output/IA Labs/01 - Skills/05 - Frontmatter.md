Módulo: IA Labs\
Aula: [Frontmatter](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18271)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, vamos nessa então,

00:02

continuando aqui a nossa aula e agora a gente

00:05

vai falar sobre a parte de front matter,

00:07

que é aquilo que nós havíamos comentado na nossa última aula. Bom,

00:11

a primeira coisa que nós temos que entender é o fato

00:14

de que existem muitos parâmetros no front matter que nós podemos utilizar,

00:21

principalmente quando nós estamos utilizando o Harness Cloud Code, certo?

00:27

Mas... existem alguns dentro do padrão front matter,

00:33

se é que a gente pode chamar isso de padrão, que são de padrão aberto, ou seja,

00:39

estão presentes e devem ser

00:42

interpretados por qualquer outro harness,

00:47

seja o Codex, Open Code e coisas nesse sentido.

00:51

E existem outras propriedades que são basicamente específicas do Cloud Code. Então,

00:57

a gente vai focar, basicamente, nas que são padrão aberto,

01:01

certo? E, em especial, vamos focar na parte de description,

01:06

porque ela é muito importante, beleza?

01:10

Primeiro ponto, name. Assim como o próprio nome já diz,

01:14

tem que ser o nome da minha skill.

01:16

E, obviamente, vou seguir esse padrãozinho aqui, ó. Minha pasta, mesmo nome, tá?

01:23

Description. Esse cara aqui é o nosso... classificador de disparo, tá? Então,

01:28

ele é o mais importante. Por enquanto, vamos deixar ele aqui, bem quietinho,

01:32

que logo mais a gente vai falar sobre ele.

01:35

Temos também um carinha que vocês já até viram,

01:39

que é o Allowed Tools,

01:43

tá? Esse cara vai fazer o quê? Ele vai, basicamente,

01:48

permitir com que a sua skill utilize tools sem pedir permissão, tá bom?

01:57

Temos também... um carinha que se chama metadata, temos

02:04

também um outro carinha que é o license e para finalizar o compatibility,

02:10

ok? Então, todos esses itens aqui são os itens conforme eu disse,

02:16

de padrão aberto, ou seja,

02:19

aquele que diversos runners conseguem ler sem problema nenhum,

02:26

fechado? O que esperar?

02:29

de cada itemzinho desse. Bom, compatibilidade,

02:33

licença e metadados são coisas já conhecidas no nosso mundo, né? Então,

02:39

metadados, vou colocar informações adicionais aqui. Licença,

02:42

vou definir o tipo de licença que eu quero.

02:44

E compatibilidade é muito a nível de requisito do ambiente, né?

02:51

Será que ele é compatível ou não? Quando você vai utilizar isso,

02:55

vai utilizar. Quando você precisa sinalizar algum tipo de pré-requisito.

03:01

Ou seja, quando a skill depende,

03:04

por exemplo, de um runtime ou de uma versão específica de alguma biblioteca, de runtime,

03:10

coisas neste sentido. Beleza?

03:13

O nosso Aloe Tool já havia falado com vocês.

03:17

No nosso caso aqui, não vou precisar utilizar neste caso.

03:21

Vou deixar ele aqui só por enquanto, mas a gente não vai precisar utilizar.

03:26

Metadata também não. E o License também não. Então,

03:29

por enquanto, vamos permanecer com eles aqui. Agora,

03:32

o nosso foco é este carinha aqui. Por quê? Porque o Description, assim como já dito,

03:37

ele é o nosso classificador.

03:39

É ele que vai dizer se o negócio vai executar ou não.

03:44

Se a nossa skill vai executar ou não. E isso é muito importante, tá, galera?

03:50

Isso é tão importante que mais pra frente a

03:53

gente vai entender que a gente consegue até...

03:55

Testar se isso realmente vai fazer a função que deve ser feita ou não.

04:00

Então, quando eu devo utilizar? Como eu já disse, sempre. E aí,

04:06

existe um pequeno padrãozinho que

04:11

eu recomendo bastante o uso,

04:13

que é o quê? O

04:16

formato de quatro itens, vamos dizer assim.

04:21

Primeiro item, ele é o quando utilizar.

04:26

Segundo item, é o gatilho.

04:29

Ou seja, qual o gatilho que eu posso acionar isso aqui? Geralmente,

04:33

a gente coloca sempre entre aspas. Então, log,

04:38

no nosso caso aqui, seria um dos gatilhos.

04:41

Terceiro ponto, quando não usar.

04:44

E o quarto formato é o que produz. Então,

04:50

nota que a gente meio que montou uma metodologia acerca do processo de descrição.

04:58

Só que, dentro ainda desta metodologia,

05:01

existem diversas outras questões que nós devemos estar atentos.

05:08

E é isso que a gente vai falar a partir de agora.

05:10

Então, entendemos aqui os nossos parâmetros,

05:13

entendemos que esse carinha aqui é muito importante. O que eu vou fazer?

05:17

Eu vou, basicamente, fazer uma cópia desse cara, jogar para cá,

05:22

voltar à minha descrição e

05:28

vou retirar. Fechado?

05:31

Então, temos aqui a nossa primeira skill da forma que a gente criou.

05:36

E agora o nosso foco maior vai ser no nosso cara chamado description.

05:42

Como eu mostrei para vocês, existe ali aquele formato dividido em quatro partes,

05:47

que é bem importante de vocês saberem,

05:49

mas dentro daquele formato ainda existem boas práticas.

05:55

E para isso a gente vai fazer aqui novamente algumas anotações.

06:00

São bem importantes de vocês entenderem, tá?

06:03

Então, o que nós temos que ter como boa

06:07

prática quando a gente vai trabalhar com descrições?

06:11

Primeiro, sempre escreva em terceira pessoa.

06:15

Isso aqui é muito importante, tá,

06:18

pessoal? Ou seja, na prática, o que é isso? Bom,

06:25

Processa arquivos...

06:32

Excel e gera

06:34

relatório. Tendo

06:40

a evitar, posso

06:44

ajudar a processar arquivos do Excel.

06:51

Ou algo mais descritivo, de fato.

06:56

Você pode usar isso para processar Excel.

07:03

Foque sempre na terceira pessoa. Além de focar na terceira pessoa, mais

07:10

uma outra regrinha super importante.

07:12

Seja específico e

07:17

inclua termos-chave.

07:21

Ou seja,

07:23

lembra que eu colocava gatilhos entre aspas duplas?

07:28

Pois é, aqui é basicamente aquela regrinha,

07:33

porém aplicada no formato de texto corrido, junto à sua descrição.

07:39

Seguindo aqui, temos também...

07:43

O que a gente pode evitar como boa prática?

07:51

Precisamos, primeiro ponto, evitar coisas muito vagas.

07:54

Então, vamos colocar aqui, evite coisas

07:59

muito vagas. E também,

08:03

junto ali do nosso texto,

08:07

que vai formatar a descrição,

08:15

Só que neste caso aqui,

08:18

a ideia por trás disso é

08:23

basicamente falar sobre as capacidades para

08:31

funcionalidades específicas. Então, entenda que quanto

08:38

mais específico, mais gatilhos de execução em

08:43

terceira pessoa, evitar

08:46

coisas vagas, a gente vai conseguir.

08:50

E garantir. Que o Cloud. Ou qualquer outro. Harness.

08:55

Dentro. De uma pool ali. De 100. 200 skills. Supondo. Consiga.

09:01

Executar. E trigar aquela. Que realmente. Faz sentido. Para aquele momento.

09:08

Na prática. Para ficar claro. Para vocês. Vamos criar.

09:13

Mais uma outra skill aqui. Que vai ser. Message. Commits. Esse carinha.

09:20

Vou criar aqui uma skill .md, vou

09:24

copiar a minha skill Simple Logger, tá? E vou fazer

09:31

aqui um message commits. Bom, a ideia aqui é o quê?

09:36

A ideia é gerar uma skill que seja capaz de gerar as nossas

09:39

mensagens ali para os commits que nós vamos fazer para um determinado repositório,

09:45

tá? Então... Vamos pensar aqui na nossa descrição,

09:49

seguindo ali o formato, seguindo essas boas práticas e tudo mais,

09:53

beleza? Eu já tenho isso pronto, tá, pessoal? Então, basicamente,

09:56

vou pegar minha colinha aqui e vou escrevendo junto com vocês, tá?

10:00

A ideia é o quê? Gerar a minha mensagem. Então, generate a

10:09

descriptive message.

10:25

E agora

10:28

vou começar a colocar quando

10:32

nós devemos utilizar isso aqui,

10:37

quando nós devemos chamar. Message. Reviewing. Message. Or. Change.

11:08

Prontinho. Algo mais simplificado.

11:11

Mas já é o suficiente.

11:13

Para a gente já ter. Um resultado.

11:16

Bacana. E aí. O que eu vou ter que fazer. Vou ter que agora.

11:22

Começar a atacar aqui o corpo. Da minha. Skill. Então.

11:27

Vamos colocar aqui.

11:30

Commit. Message. Format.

11:35

E também vou dar um exemplo. Para ele.

11:39

Então o

11:42

que eu espero aqui. Da minha mensagem.

11:46

Quando eu for comitar alguma coisa. Então eu vou.

11:50

Gerar. A mensagem de commit.

11:53

E vou pedir. Para que ele siga. O formato abaixo.

12:01

Exemplo, input.

12:04

Added user authentication

12:08

With JWT tokens, por exemplo.

12:13

Qual vai ser o meu output que eu espero disso aqui?

12:20

Output vai ser, por exemplo, pitch off.

12:25

E eu já tenho aqui o meu resultado.

12:28

Posso colocar também alguns outros exemplos. Por exemplo, exemplos de fix.

12:34

Sure. E assim por diante. Então vamos fazer aqui.

12:39

Um exemplo. Dois.

12:44

Pode ser esse carinha aqui. E aí eu tenho. O meu output.

12:51

Vamos fazer mais um. De sure.

12:57

E eu tenho aqui.

12:59

Um update de docs.

13:01

E daí. Agora. Eu já tenho mais uma vez. A nossa. Skill.

13:07

Pronta para ser utilizada.

13:11

O que eu vou fazer aqui é, primeira coisa, cloud aberto,

13:17

Reload skills e já aparece aqui para mim.

13:22

Obviamente, eu não tenho nenhum tipo de repositório, tá?

13:26

Vou rodar aqui só para vocês verem aí que ela vai rodar.

13:31

E aí, como a gente já suspeitava,

13:34

Obviamente não existe nenhum tipo de repositório ativo. Então, vou fazer aqui um git init.

13:45

Rodar novamente. E vamos ver o que vai acontecer.

13:51

Agora tivemos aqui. Um outro.

13:56

Resultado. Mas nesse caso aqui. O resultado foi que.

13:59

Eu ainda preciso trabalhar nela. Porque não existe nenhum tipo de repositório.

14:04

Inicializado. Como eu abri um novo Bash. E inicializei.

14:08

O que eu vou fazer? Vou fechar esse cara aqui.

14:10

E vou abrir de novo. Só para a gente ter o contexto correto.

14:14

E vou usar de novo. A nossa skill.

14:18

Entender de fato. Qual vai ser o resultado agora. E aí.

14:22

Agora sim. Fez o load. E está analisando. Os meus. Chains.

14:32

Ainda não temos nada. Em stage.

14:35

Mas basicamente. Ele já consegue.

14:38

Produzir. Algumas coisas para a gente. Então o que ele fez. Se você reparar bem.

14:43

Foi lá. Viu. Que não existe nada. Mas notou que existe. Coisas a serem comitadas.

14:49

Para ficar em stage, viu quais são os arquivos, deu uma lida, e baseado nisso,

14:55

a gente conseguiu criar aqui as nossas mensagens de sugestão, tá?

15:03

Da forma que eu mostrei aqui, pessoal, basicamente,

15:05

O que tá acontecendo é, eu estou indo lá e

15:10

Invocando a minha skill.

15:12

Eu ainda não testei se através da minha description está sendo chamado ou não,

15:18

Tá? Então,

15:20

Vamos fazer aqui uma nova seção.

15:23

E vamos testar. Baseado na description que a gente tem aqui.

15:27

Vamos fazer o seguinte. Init. Create.

15:36

Commit. Message. For. Changes.

15:43

Vamos ver o que vai acontecer. Olha só.

15:47

Já deu o load.

15:50

E agora sim.

15:52

Através da minha description.

15:54

Foi feito o processo de classificação.

15:58

E aí agora ele vai executar a minha skill,

16:02

vai ler os meus arquivos e vai

16:04

me dar de novo

16:06

as minhas mensagens desejadas.

16:12

Olha só, já tenho aqui novamente o resultado.

16:19

Fiz uma limpeza aqui e vamos executar novamente o seguinte.

16:34

commit para as alterações feitas no projeto,

16:42

separe cada alteração e gere

16:47

a mensagem de commit baseada

16:52

nas mudanças. Vamos

16:56

ver o que vai acontecer agora.

17:00

Novamente, temos o load da nossa skill e

17:05

agora é bem provável que ao invés dele agrupar,

17:09

todas as skills que foram criadas em uma única mensagem,

17:15

ele vai fazer

17:18

um agrupamento diferente.

17:23

Então, olha só. Temos aqui a nossa mensagem. 1, 2, 3, até a 6.

17:30

Então, repare que a gente conseguiu fazer uma

17:36

habilidade, que é, no caso, gerar as mensagens de commit.

17:41

ser replicada de tal forma que, a partir do prompt que eu desejo,

17:47

que eu faço, eu consigo ter N resultados.

17:51

Mas aquele resultado, aquela ação a ser executada,

17:55

ela permanece sendo exatamente a mesma coisa.

## Resumo IA

[RESUMO_IA]