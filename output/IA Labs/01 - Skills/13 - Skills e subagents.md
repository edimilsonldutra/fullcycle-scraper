Módulo: IA Labs\
Aula: [Skills e subagents](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18279)

## Resumo da aula



## Transcrição

00:00

Bom galera, show de bola aí. Continuando a nossa ideia aqui de skills,

00:04

o que a gente vai falar agora?

00:05

Agora a gente vai falar sobre a parte de como uma skill pode executar um sub-agent, tá?

00:13

E pra isso, o que eu fiz? Preparei mais uma demo aqui pra vocês, tá?

00:17

No qual a gente tem um pequeno projeto,

00:19

ele é um pouquinho maior dessa vez, mas é basicamente um projetinho JavaScript.

00:24

Contém testes, tem aqui uma migration, tem uma conexão junto ao banco de dados,

00:29

tem também uma pipeline, bem simples,

00:32

mas que vai dar para a gente fazer uma coisa muito interessante e começar

00:38

a entender um pouco mais sobre essa parte do uso de skills com subagent.

00:43

Primeira coisa que é muito importante da gente esclarecer.

00:46

Que esta aula em específico e o assunto em questão

00:50

vai depender muito do tipo de CLI que você está utilizando,

00:54

do tipo de harness que você está utilizando.

00:56

E por que eu falo isso?

00:57

Porque existem harness que têm agentes que fazem exatamente

01:02

a mesma coisa que eu vou falar aqui,

01:04

porém com nomes diferentes.

01:05

Existem CLIs, harnesses, que não têm nenhum tipo de agente. Então,

01:10

vai depender de fato de qual você está utilizando,

01:14

se é o Cloud Code, se é o Codex,

01:16

ou se é qualquer um que existe aí no mercado, tá? Em especial,

01:21

falando do Cloud Code, e aí, agora é exclusivo do Cloud Code, tá? Porém,

01:27

tudo que eu explicar aqui vai servir de forma geral para qualquer outro harness,

01:32

ele trabalha com esses tipos de agentes. Então,

01:37

a gente tem um carinha chamado de Explorer.

01:40

Uma parte de plan e outra de general purpose, beleza?

01:46

Conforme eu disse para vocês,

01:47

esses nomes podem ser alterados aí de acordo com o CLI que você está utilizando,

01:54

perfeito? Então, como que a gente faz para usar esses carinhas?

01:58

Antes da gente trabalhar na skill, de fato,

02:02

eu queria mostrar para vocês o que cada um desses carinhas fazem.

02:06

Primeiro, temos aqui o agente de exploração. Ou seja,

02:11

ele é um agente super rápido.

02:13

Geralmente vai utilizar sempre o modelo mais barato

02:16

e o mais rápido para realmente ser eficiente.

02:20

E ele trabalha bastante com ferramentas de leitura. Por quê?

02:25

Porque ele tem o propósito de basicamente fazer o mapping

02:30

ou a busca de forma muito rápida para o usuário.

02:34

Temos também um carinha chamado Plan.

02:37

Este cara. Ele tem acesso a itens externos, então ele vai ser um agente de pesquisa.

02:45

Diferente do carinha de cima, que é o Explorer,

02:48

ele vai sempre herdar o modelo no qual a gente está utilizando.

02:52

No meu caso aqui, todo esse tempo,

02:54

estou utilizando o Opus 4.8. Então, caso eu entre em planejamento,

02:59

ele vai herdar por padrão. E ele tem as ferramentas somente leitura também.

03:07

E edit são negados por padrão, tá?

03:10

E quando eu vou utilizar esse carinha aqui, como por exemplo,

03:13

eu vou planejar alguma coisa, né? Inclusive, o modo plan do Cloud Code,

03:17

a gente faz o uso desse cara.

03:19

E para finalizar, a gente tem um carinha de general purpose.

03:23

E esse cara aqui, ele vai fazer o quê?

03:25

Ele é um agente generalista, ou seja,

03:28

ele é capaz de executar N tipos de tarefas diferentes com múltiplas etapas.

03:34

Isso geralmente envolve exploração, alguma ação,

03:39

seja de edição, seja de write.

03:41

Ele é inteligente o suficiente, vamos dizer assim,

03:45

para que ele consiga iniciar uma tarefa que tem múltiplas etapas

03:50

e consiga concluir isso sem problema algum ou com poucos problemas.

04:04

que nós estamos utilizando na conversa, tá?

04:06

Esse cara aqui é basicamente o que a gente utiliza no dia a dia,

04:10

tá? E o propósito dele, como eu disse,

04:13

vai ser para trabalhar com tarefas de múltiplas etapas, ok?

04:19

Entendido essa parte dos tipos de agente que nós temos hoje disponível,

04:23

agora o ponto é, ok,

04:25

o que eu faço com isso, né? E é exatamente isso que eu vou mostrar para vocês.

04:30

O Cloud Code, em especial, se a gente quiser,

04:33

a gente pode disparar subagentes por padrão.

04:37

Mas o nosso foco aqui não está em entender

04:40

como utilizar subagentes e coisas nesse sentido.

04:44

Nosso foco aqui é mais voltado,

04:46

a nossa ótica vai ser mais voltada para o uso da skill. Porque dentro da skill,

04:50

a gente também pode fazer o uso desses subagentes e disparar

04:54

subagentes específicos para colher determinadas informações e

04:58

trabalhar dentro da nossa skill.

05:00

Bom, pessoal, então vamos fazer o seguinte aqui.

05:03

Eu vou gerar uma nova skill. Essa skill,

05:07

ela vai ser uma skill que, inclusive, bem útil aí também pra vocês, que vai ser...

05:11

Imagine quando você tem aqui um onboarding de um novo projeto ou até,

05:17

eventualmente, você quer fazer documentações e coisas nesse sentido,

05:21

atualizar documentações, manter atualizada,

05:23

você vai poder utilizar essa skill aqui também,

05:25

claro, com as devidas atualizações e

05:30

customizações aí de acordo com o teu projeto, tá?

05:32

Ele vai basicamente mapear todo o nosso diretório ali e vai me

05:37

dizer o que tem em cada layer e coisas nesse sentido, tá?

05:42

Então, abrindo o Cloud Code, já estou aqui com ele aberto, o que eu vou fazer?

05:46

Vou pedir pra ele criar uma

05:49

skill dentro do projeto, subagentes criados,

05:56

Cloud

05:58

Skills, o

06:01

nome da skill

06:03

Será mapping project.

06:08

E aí, nós vamos fazer o seguinte.

06:12

O passo 1 dessa skill vai ser o quê?

06:16

Quebrar o projeto em questão.

06:22

Diretório / projeto em

06:26

questão em frentes independentes. Vou

06:32

colocar aqui, que é importante, que é obrigatório.

06:37

Depois iremos utilizar subagentes.

06:42

E aí eu já explico um pouco melhor do porquê que isso é importante a gente entender,

06:49

porque subagents basicamente não vão compartilhar o mesmo contexto.

06:54

E aí eu vou dar, por exemplo, um exemplo de como poderia

07:01

ser essa quebra.

07:04

Vamos colocar aqui, por exemplo, uma quebra a nível de

07:09

A arquitetura, então ele poderia pegar ali entry point,

07:13

as camadas, módulos,

07:15

como o fluxo dos dados funciona,

07:22

camada

07:24

de dados, né? Vamos pegar ali a camada específica de dados,

07:29

models, esquemas, conexão de dados,

07:38

onde

07:40

o estado mora, por exemplo.

07:44

Alguma coisa relacionada. A testes também. Então. Dizer aí. Qual que é o framework.

07:52

Onde. Se localizam.

07:58

Qual a cobertura.

08:00

Atual. E. O que. Está coberto. Ou não.

08:06

O que mais que a gente pode colocar aqui. Ah. Vamos falar do build.

08:09

Build. E CI. Que a gente tem ali. O nosso GitHub. Scripts. De build. Pipeline.

08:22

Deploys. Enviar.

08:24

Se existir.

08:31

Segurança. Botar alguma coisa de segurança também. Notificação. Autorização. Segredos. Middlewares. Específicos.

08:50

Permissão. Segurança.

08:54

Show. Bom.

08:56

Mas o que a gente pode fazer aqui de quebra?

08:59

Creio que somente isso. E o passo 2 aqui. O que a gente vai fazer?

09:04

Galera. A gente vai ter aqui.

09:10

Comece lançando. Lance. Subagents.

09:19

Por cada frente disponível. Para. Curação.

09:26

Pode até colocar aqui. Utilize. Agents. Type. Explorer. E aí.

09:42

O que eu vou fazer. Todas as

09:49

mensagens, ou

09:53

seja, várias

09:56

chamadas que rodam

10:01

de forma concorrente.

10:07

E para cada

10:11

agente,

10:13

adicione um prompt.

10:21

E aí a gente vai pedir e capturar a conclusão. Vou botar aqui o prompt.

10:30

Subagent é o que? Explore.

10:33

O diretório. Mais.

10:38

Diretório. Da frente.

10:41

Subagent.

10:43

E mapeei. A frente.

10:50

List. Os arquivos. Como.

10:54

Caminho. E a linha.

10:59

Escreva. De forma.

11:04

Enxuta. O

11:08

que faz. E como funciona.

11:12

E aponte. Um.

11:16

Botar somente um ou dois riscos ou pontos de atenção.

11:22

Fique somente nessa frente de análise.

11:28

Devolva apenas o resumo. E, obviamente,

11:34

aqui eu poderia definir algo um pouco mais estruturado a nível de resultado. Mas,

11:40

no nosso caso aqui, só para a gente entender... Como que a gente pode fazer isso.

11:45

Já é o suficiente. Então vou botar aqui mais um passo.

11:50

Que é o passo 3. Que vai ser basicamente o wrapper disso tudo aqui.

11:55

Então junte.

11:57

Todos os resumos.

12:01

Das frentes que foram analisadas. E baseado nisso.

12:06

Gere um mapa do projeto repositório. Visão geral.

12:15

Uma seção por frente. Por onde começar,

12:21

riscos, prioridades. Aí, óbvio,

12:26

poderia descrever também para entender de fato o que

12:29

eu gostaria em cada parte aqui do meu relatório,

12:35

mas para agora não tem tanta necessidade.

12:38

Vamos rodar e vamos verificar o que vai acontecer.

12:43

Bom, galera, vamos lá.

12:45

Finalizamos aqui após 50 segundos praticamente.

12:49

Vamos dar uma olhada aqui no nosso resultado, né? Então, mapping project.

12:55

Inclusive, deixa eu já fazer um reload aqui nas minhas skills.

13:00

Vamos ver o que vai acontecer aqui.

13:02

Mapear o nosso repositório com o nosso SubAgent Explorer.

13:08

Ou seja, eu vou utilizar o modelo mais tranquilo ali,

13:11

que é o Raico. Vou abrir aqui no preview para ficar mais fácil.

13:18

Ok, quebrou a frente.

13:21

Lança. O nosso SubAgent.

13:24

Em paralelo. E

13:28

sintetiza. Perfeito.

13:33

Vamos testar. E vamos ver aqui qual vai ser o resultado.

13:38

Bom. Já trouxe aqui.

13:41

Alguma pequena amostra. Fez aqui.

13:45

Basicamente a ideia.

13:47

Das minhas frentes. E agora. Olha só. Os meus.

13:51

Sub-agents aqui já sendo disparados, todos ao mesmo tempo,

13:55

e explorando cada etapa aqui. E, obviamente,

13:59

o que vai acontecer aqui? Se eu quiser, por exemplo,

14:01

dar uma olhada nesse cara aqui, eu posso vir.

14:04

Volto para o main, posso vir para cá, volto para o main, posso vir no de segurança,

14:09

volto para o main e assim a gente vai brincando aqui.

14:12

Vamos ver o que vai acontecer como resultado final.

14:16

Bom, vamos lá. Todas as frentes foram lidas.

14:20

Vamos ver aí o que o modelo Raico nos trouxe, né? Então,

14:24

agora a gente tem o mapa do projeto e agora

14:26

sintetizado da forma que a gente havia pedido,

14:30

né? Então, nossa API de loja, temos aqui uma versão,

14:34

é uma API REST com Node e Express, utilizando Postgres.

14:39

O fluxo de requisição acontece no HTTP.

14:43

Temos um middleware, depois ele vai para pedido, entra no serviço,

14:48

o serviço consome a minha conexão e busca os dados lá no Postgres.

14:53

Depois, obviamente, para responder o usuário,

14:55

é só inverter isso aí que a gente tem o resultado,

14:58

né? Agora, por frente, a gente tem aqui a nível de arquitetura, o entry point,

15:02

a gente tem aqui as camadas HTTP, né?

15:06

Dois endpoints aqui específicos e temos também o nosso serviço.

15:11

Dado... Temos aqui somente a connection e a migration sobre testes.

15:19

Temos apenas um teste. Exatamente isso. E o build.

15:23

Temos ali o nosso workflow que eu havia mostrado para vocês.

15:26

E segurança. Por onde começar vamos ver a que

15:31

ponta que ele mostra. Então aqui a gente consegue entender stack.

15:36

Aqui é o nosso entry point. Aqui é como tudo funciona a nível de autoindicação.

15:42

Aqui é o caminho da requisição até a regra de negócio. Bacana.

15:46

Aqui é onde o estado mora. O banco de dados. E aqui.

15:50

É onde vivem os testes. Em relação a risco e prioridade. Prioridade. Crítica.

15:59

Alta ou média. Ele também conseguiu. Fazer uma pré-classificação.

16:05

Show de bola. E aí no final.

16:07

Ele me deu aqui uma ordem de ataque. Build quebrado.

16:12

Trabalhar com segredos. Hope Stays da API. E também qualidade da pipeline.

16:17

Ou seja. A gente tem aqui um resultado.

16:21

Bacana aí que, obviamente, com toda a customização necessária,

16:26

tanto da sua parte para exibir os dados que você precisa,

16:29

como também do projeto,

16:31

a gente consegue criar algo que dá para a gente aplicar em vários locais,

16:36

como, por exemplo, permanecer com a nossa documentação sempre atualizada,

16:39

fazer o onboarding de novas pessoas,

16:42

ou você fazer o seu próprio onboarding em novos

16:46

projetos que você for buscar e tudo mais.

16:48

Beleza? Então fica aí a dica de como que a gente

16:50

pode trabalhar com os subagents dentro das nossas skills.

## Resumo IA

[RESUMO_IA]