Módulo: IA Labs\
Aula: [Arquitetura por trás da Skill](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18269)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, então dando continuidade aqui,

00:02

dessa vez eu decidi trazer para vocês uma skill já pronta, tá?

00:05

Para que a gente consiga associar com uma realidade de fato,

00:09

beleza? Então como vocês podem perceber,

00:11

neste momento nós temos aqui uma skill de chamada Team Code Review.

00:15

E aí eu tenho o meu arquivo skill.md e

00:19

também tenho aquelas outras pastas que eu havia citado para vocês,

00:24

que são... A parte de scripts,

00:26

a parte de referências e também eu tenho aqui a parte de avaliação,

00:31

para saber se realmente minha skill está funcionando da forma que eu quero ou não,

00:36

perfeito? Mas abrindo aqui o nosso skill.md,

00:39

eu queria mostrar alguns itens que são importantes

00:43

para a gente entender também sobre...

00:46

como funciona internamente a arquitetura dessa execução,

00:50

da leitura da skill, perfeito?

00:52

Primeira coisa que eu queria mostrar para vocês é em relação ao front matter.

00:56

Lembra que eu falei que é o nosso YAML ali,

00:59

no qual eu tenho alguns metadados, como, por exemplo,

01:03

o nome da minha skill, description e allowed tools, perfeito?

01:08

Posso também ter algumas outras informações aqui, como path,

01:12

que eu vou dizer... aonde essa skill deve ou não rodar,

01:16

dentre outras informações, tá?

01:19

Mas o ponto que eu quero tocar aqui neste momento é falar

01:23

um pouco de como é que vai funcionar essa questão da leitura,

01:29

execução, decisão dessa execução por meio do Cloud Code, tá?

01:34

Vou utilizar aqui o Cloud Code porque acaba sendo mais utilizado aí como base,

01:39

perfeito? Então, a gente pode, galera, é...

01:42

definir isso em três fases principais. Então,

01:49

a gente tem aqui fase 0, fase 1,

01:51

posteriormente vou colocar a fase 2 e a fase 3.

01:56

Na verdade, acaba sendo quatro fases. Vou botar aqui logo.

02:00

E o que acontece?

02:02

Cada uma dessas fases vai ser responsável por uma coisa específica.

02:08

É sobre isso que eu vou falar neste momento.

02:11

Primeira parte. Fase zero. Aqui é a fase de startup.

02:15

Ou seja, quando eu venho aqui e inicio o meu cloud.

02:19

O que vai acontecer aqui?

02:21

Ele vai fazer o processo de startup e vai executar um processo de indexação.

02:27

Ou seja, isso vai acontecer uma vez todas as vezes que eu inicio uma nova sessão.

02:33

Perfeito? Então, se... eu abro uma nova sessão,

02:37

automaticamente ele já vem aqui e faz o processo de indexação e vê que,

02:42

opa, eu tenho ali a presença de skills. Tanto que, se eu vim aqui nessa sessão,

02:48

colocar uma barra Team Code Review,

02:50

eu já consigo utilizar a minha skill, perfeito? Então, fase 0,

02:54

fase da startup e fase da indexação, perfeito? Show!

03:00

Agora, nós temos também a fase 1.

03:05

E essa fase 1 é uma fase interessantíssima,

03:08

que é a fase de roteamento e decisão. Aqui, o que vai acontecer?

03:13

Lembrando o nosso front matter, que eu havia falado para vocês neste momento.

03:18

Pois é, aqui eu tenho o name, eu tenho o description,

03:21

E eu tenho diversos outros parâmetros que eu posso utilizar aqui,

03:24

que logo mais a gente entra em aprofundamento acerca disso.

03:28

Mas, neste momento... Na fase de roteamento barra decisão, vamos colocar assim,

03:35

é o momento em que eu peço que o

03:42

meu agente, no caso o Cloud Code, que aqui a gente vai chamar de Harness,

03:46

que é o cara que vai encapsular toda a LLM,

03:51

vai fazer o quê? Ao pedir alguma coisa, como por exemplo, revise...

03:57

as minhas mudanças que estão em staged, ele vai fazer o quê?

04:03

Ele vai pegar esse carinha aqui e vai começar a olhar a minha skill

04:08

para ver se a descrição desta minha

04:11

skill vai classificar para uma execução ou não.

04:17

E o ponto que é importante

04:19

aqui dizer que a decisão acaba sendo... do próprio modelo,

04:25

a decisão de execução ou não.

04:27

Por isso que é tão importante a gente ter esse processo, por exemplo, de EVOL,

04:32

no qual a gente consegue fazer uma garantia de que, de fato,

04:37

aquilo ali vai disparar na hora certa ou não vai disparar em horas erradas,

04:43

tanto para um quanto para o outro.

04:46

Então, por isso que a descrição aqui, ela literalmente é a feature classificadora.

04:53

É ela que vai nos proporcionar o roteamento e essa decisão de,

04:57

opa, vai ou não vai ser executado.

05:01

E um ponto que é importante ser analisado é

05:03

que aqui embaixo nós temos o nosso corpo,

05:06

veja só. E quando isso acontece,

05:08

automaticamente nós ainda não lemos o corpo,

05:13

porque eu só fiz um pedido. Então, o que está acontecendo aqui no primeiro momento?

05:17

Eu tenho a minha fase de startup e indexação, na qual eu tenho ali,

05:23

O Harness Cloud Code varrendo toda a minha estrutura de projeto.

05:28

Neste caso em específico, nessa primeira fase,

05:31

ele vai varrer a parte das pastas .cloud e as informações aqui dentro.

05:38

Posterior a isso, eu vou para a fase 1,

05:42

que é a fase de roteamento e decisão.

05:47

Neste momento, baseado na minha description, no meu front matter,

05:51

ele vai fazer a decisão se executa ou não executa.

05:57

E a partir disso,

05:58

o que vai acontecer? Eu entro na minha fase 2.

06:02

E essa minha fase 2 é a fase de carregar o corpo.

06:08

Ou seja, carregar de fato as instruções da minha skill.

06:13

Então, quando foi decidido...

06:16

acionar aquela skill, o modelo vai emitir uma tool call.

06:21

E esta tool call é uma tool call de leitura.

06:24

E como que eu sei que ele vai emitir isso? Simples,

06:28

pessoal. Lembrando o nosso front matter, voltando nele de novo,

06:31

olha só, nós temos aqui o nosso allow tools.

06:35

E aqui eu estou dizendo o seguinte, eu tenho read, eu tenho rep,

06:39

eu tenho bash. Da mesma forma que na skill eu digo

06:45

o que ela pode usar e quais são as tools que ela internamente vai poder usar,

06:50

o meu Harness consegue utilizar essas tools para fazer a minha leitura do corpo e,

06:57

de fato, fazer essa carga das instruções para, então,

07:01

começar o processo de execução. E aí, quando acontece o meu processo de execução,

07:08

Nós entramos na fase 3. Na verdade,

07:12

Aqui acaba sendo... a fase 4, que é a parte da leitura, de fato,

07:19

Só que é uma leitura de forma condicional.

07:26

E essa leitura de forma condicional vai

07:31

vir de encontro com o que nós escrevemos,

07:36

com as instruções que foram passadas. Então, o que acontece?

07:39

A cada read, uma tool é chamada e note...

07:44

Que aqui eu tenho steps, por exemplo, nesta skill em específico,

07:48

Eu tenho steps. Não que toda skill eu precise ter esse step,

07:53

mas aqui o modelo vai ter essa decisão.

07:55

Então, ele vai interpretar isso aqui,

07:58

vai fazer o load do meu contexto, vai interpretar isso aqui,

08:01

vai pegar as minhas chains que estão no staging. Nesse caso,

08:07

Nesse projeto ainda nós não temos nada de staging.

08:10

Depois, ele vai ler o step 2, o step 3, assim.

08:13

E tem um ponto aqui que é muito importante,

08:16

que o modelo, neste caso, ele está apto a decidir se ele vai, de fato,

08:23

seguir tudo isso aqui ou não. E aí, novamente,

08:25

nós entramos com o teste para garantir se realmente

08:29

o resultado está sendo esperado ou não.

08:32

Da mesma forma que a nossa skill aqui de referência, que é o...

08:39

CodeReview, eu posso passar também links nos quais

08:42

eu pego os meus arquivos de referência.

08:46

E aí, o modelo vai decidir ou não se ele vai fazer o download no contexto,

08:50

se ele vai ler e tudo mais.

08:52

Então, step zero aqui, o que está acontecendo?

08:54

Eu já deixo uma instrução que é requerido que ele faça a

08:58

leitura e acesse a linha de referência, tema, convenção e leia esse arquivo também.

09:06

E aí, depois, ele tem que vir aqui,

09:10

desde que nós temos aqui algum

09:14

tipo de alteração que afete input,

09:18

autenticação, consultas ao banco de dados ou requests externas. Se isso acontecer,

09:24

então eu tenho que vir aqui e ler. E o que tem aqui dentro?

09:28

Basicamente, nós temos o quê? Convenções, neste caso, convenções de WASP e...

09:34

Aqui, convenções do nosso time, como por exemplo, arquitetura, naming, errors, teste,

09:40

como tudo vai funcionar a nível de projetos, convenções do nosso projeto.

09:44

Então, veja bem que se a gente voltar aqui,

09:48

a gente meio que consegue gerar um modelo mental,

09:51

ou seja, eu indexo, eu tomo a decisão,

09:55

eu carrego as informações como necessárias e a

09:58

partir disso, eu capturo os resultados,

10:01

faço as leituras e... crio as minhas condições. Se você reparar bem,

10:06

bate muito com aquilo que nós estávamos falando lá das questões dos níveis,

10:12

né? Ou seja, se a gente retorna aqui no nosso guia,

10:16

deixa eu fechar esse cara rapidinho, a gente percebe que o nível 1,

10:21

ele vai fazer o quê? Ele vai ler só a parte de front matter.

10:25

Aqui, lá no nível 2, a gente tem o carregamento do corpo,

10:28

né? Onde ele vai ler, ou seja...

10:31

associando às fases. E, por fim,

10:35

o nível 3, onde a gente consegue atingir referências.

10:39

Scripts e tudo mais que pode acontecer aqui dentro. Só que,

10:43

Até aqui, eu acho que está super claro, mas temos

10:49

ainda a fase 4 e a fase 5.

10:54

Eu dividi elas em situações um pouco diferentes.

10:59

Na verdade, a gente pode até colocar a fase 3 aqui embaixo também.

11:03

E aí eu vou completar com algumas informações que são bem importantes,

11:08

Beleza? Por quê? Porque como eu disse,

11:11

Na fase 3 nós temos ali uma leitura de forma condicional, ou seja,

11:15

Ele vai buscar se existem referências e tudo mais

11:18

e vai me trazer quando for necessário.

11:21

Já quando nós estamos falando da fase 4,

11:24

Basicamente, nós estamos nos referindo a scripts / execução. E aí,

11:33

Retornando aqui na nossa skill, você pode perceber que já no step 1,

11:37

Isso aqui é a nossa instrução,

11:39

É o nosso corpo, tá? Na nossa instrução, então,

11:42

A gente já tem primeiro as referências,

11:45

Depois a gente pede para executar os scripts que estão

11:48

aqui dentro da nossa skill de code review. Para quê?

11:51

Para que eu colete as diferenças em stage, beleza? Então,

11:56

Nesta fase aqui, ele vai fazer a execução desse meu script.

12:02

E por fim, qual vai ser a fase 5? A execução de

12:08

Fato da tarefa. Ou seja,

12:11

Ele vai passar por todas essas etapas para me devolver lá

12:16

Na fase 5 o resultado da tarefa que a skill está resolvendo.

12:22

Então, para a gente finalizar, o que nós teríamos aqui em relação a ciclos?

12:27

Para ficar fácil de ser entendido. Eu poderia ter, por exemplo,

12:32

Uma skill que é muito mais simplificada, no caso,

12:38

A minha pasta e o meu arquivo skill.md,

12:41

Que funcionaria no seguinte ciclo. Quando eu digo ciclo aqui,

12:45

São ciclos de fase. Então, vai lá na fase 0,

12:51

Depois vai para a fase 1,

12:53

Depois vai para a fase 2 e automaticamente eu teria a minha fase 5.

13:02

Seria um dos ciclos. Poderia ter.

13:05

Um outro tipo de skill. Que vai, fase 1,

13:10

Fase 2,

13:14

Faz a leitura. E vai para a fase 5. Poderia ter.

13:24

Mais um aqui no meio,

13:27

Que é o que está acontecendo nesta skill que nós estamos utilizando.

13:31

De exemplo. Então, você repare que,

13:34

A gente consegue,

13:36

Criar diversas formas,

13:39

Cenários e, consequentemente, habilidades para a gente

13:44

tratar quando nós estamos falando de skill.

13:47

É importante que a gente entenda essa arquitetura por trás

13:51

para que a gente consiga entender realmente como ela vai funcionar.

13:57

E, obviamente, estou usando aqui o harness do Cloud Code como referência,

14:02

mas... O processo é muito similar em todos os outros.

14:08

Entendido essa parte mais técnica, mais arquitetural,

14:13

agora a gente vai partir para uma outra etapa que

14:18

já é mais voltada para a criação de fato da skill.

## Resumo IA

[RESUMO_IA]