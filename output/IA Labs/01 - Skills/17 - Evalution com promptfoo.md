Módulo: IA Labs\
Aula: [Evalution com promptfoo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18283)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, agora a gente vai falar sobre uma outra forma de eval,

00:04

que é utilizando uma ferramenta chamada Promptful.

00:08

E o porquê que você deve pensar em outra ferramenta ou outra forma

00:14

de eval quando a gente está falando na parte de avaliação de skills?

00:20

Pelo simples motivo de que a forma que foi mostrada via Skill Creator, ela...

00:27

Funciona, ela é muito boa e é muito aconselhável de você utilizar.

00:31

Porém, o mais importante é que a

00:35

sua skill passe a funcionar em multimodelos. Logo,

00:40

se você tentar trabalhar com o skill creator dentro de outros modelos,

00:46

é bem provável que você terá algumas dificuldades.

00:49

Mesmo que a skill seja um padrão hoje adotado de forma geral,

00:56

por qualquer tipo de CLI que você esteja utilizando,

01:00

a questão é,

01:01

você vai ter que ficar fazendo configurações e configurações em múltiplos CLIs.

01:06

E isso não é interessante. Então, existem ferramentas que a gente consegue utilizar,

01:11

uma delas é o PromptFull,

01:13

para fazer esse processo de avaliação de forma

01:16

muito mais simplificada e que atenda multimodelos.

01:20

E é isso que a gente vai trabalhar neste momento com...

01:24

este carinha chamado promptful então acessando o site aí promptful

01:29

.dev tá ele vai ser um pacote que vocês vão

01:32

instalar via npm e aqui vocês conseguem perceber que existem

01:36

n maneiras da gente utilizá -lo tá basicamente esse cara aqui

01:41

é um avaliador de saídas de LLM ou seja você

01:45

coloca o teu prompt lá e ele vai avaliar mediante métricas

01:49

que você selecionar se está de acordo ou não A

01:53

diferença é que aqui a gente tem aquela questão de multimodelo.

01:57

Então, eu tenho uma percepção real daquilo que eu estou pedindo.

02:02

Ele tem muita coisa.

02:06

Atualmente, o PromptFull não é mais só sobre a parte de avaliação.

02:10

Ele tem várias outras coisas aí.

02:12

Mas o nosso foco vai ser exatamente essa parte

02:15

de avaliação para que a gente consiga...

02:19

te dar aí uma outra opção. Mas fora isso,

02:22

tem a parte de code scanning também, segurança,

02:25

guardrails, MCP também, que a gente pode trabalhar com o próprio MCP do Promptful.

02:30

Enfim, realmente é uma plataforma bem ampla, tá?

02:34

E o mais bacana disso tudo é que ele é open source. Então,

02:39

a gente consegue utilizá -lo aí de forma gratuita e se você quiser pagar,

02:44

você pode pagar pela versão cloud, que também...

02:48

está disponível tá nós vamos lá primeira coisa que a

02:51

gente precisa entender aqui é o seguinte é como

02:54

trabalhar com esse carinho né E aí é muito simples

02:57

a gente vai utilizar aqui um comando npx prompt

03:00

full tá E aqui a gente já vai dar

03:03

início a ao processo de configuração que é extremamente simples

03:08

tá basicamente um comando voltando aqui no nosso vs

03:12

code vamos lá então vou abrir aqui o nosso terminal,

03:17

vou acessar aquela

03:20

nossa pastinha, mcp skills, e

03:25

aí aqui dentro eu vou fazer o seguinte,

03:27

npx prompt full, a minha versão é latest,

03:32

e vou dar um init, ok? E aí ele vai pedir para instalar.

03:38

Aguardamos um pouquinho e aqui ele já começou

03:40

a fazer algumas perguntas para a gente. Então,

03:43

o que eu quero fazer? Basicamente, eu quero comparar prompts e modelos, por exemplo.

03:48

Aí eu posso vir aqui. Qual modo eu pretendo utilizar?

03:53

Eu posso escolher agora ou, se preferir, posso escolher depois também.

03:58

Mas só caso de não precisar fazer nenhum tipo de configuração posterior,

04:04

vamos escolher aqui que eu vou usar o Cloud, por exemplo.

04:07

E agora... ele vai fazer aí o setup inicial, tá?

04:11

Note que este setup inicial, ele é relativamente bem simples de ser feito.

04:16

Por quê? Porque ele vai gerar um arquivo chamado promptful config .yaume,

04:21

ok? E aqui dentro,

04:22

você pode perceber que o yaume em si, ele é extremamente simples de se trabalhar.

04:28

A gente tem aqui a descrição do que ele é,

04:30

o prompt em si a ser testado e os providers que nós queremos testar.

04:35

Aqui a gente tem... basicamente o nosso dataset.

04:39

E nota o seguinte, você reparou que o PromptFull,

04:42

em especial, ele não fala muita coisa sobre a skill em si.

04:47

Porém, o que é uma skill?

04:49

De forma geral, a skill é uma habilidade que vai ter ali instruções específicas.

04:55

Então, trocando em miúdos,

04:57

basicamente a skill é um conjunto de prompts. Óbvio que a gente tem as referências,

05:03

a gente pode ter os scripts e tudo mais, mas de forma geral,

05:06

se a gente for olhar, a gente trabalha basicamente com prompt, ok? Então, pessoal,

05:11

o que vai ser necessário aqui para a gente configurar o nosso Evolve via PromptFull?

05:18

Primeiramente, vai ser necessário nós utilizarmos aí uma key de API,

05:23

tá? E aí você pode utilizar Duntropic, você pode utilizar de OpenAI,

05:28

pode utilizar qualquer outra que você quiser.

05:31

O processo em si, ele é super simples. Basicamente, você vai...

05:35

exportar diretamente no seu terminal, tá? A sua aqui,

05:39

e aí você já vai conseguir fazer com que o prompt

05:43

full encontre essa variável de ambiente e faça o uso dela.

05:48

Depois que você configurou isso no seu terminal,

05:51

aí sim a gente pode vir aqui para a configuração do prompt full,

05:56

e aqui nós vamos fazer o seguinte, vou mudar aqui para prompt, dessa forma, ok?

06:04

Vou começar a fazer algumas configurações.

06:07

Acabei esquecendo de colocar as aspas. Agora já está certinho. Então,

06:12

o que nós vamos fazer aqui? Nessa parte de Provider,

06:17

eu vou utilizar o meu Cloud Agent SDK. Então,

06:23

vamos fazer uma breve alteração aqui.

06:28

Vai ficar bem mais fácil.

06:31

Vamos voltar. Vamos colocar aqui. ID.

06:39

E aí eu vou dizer. ID que vai ser.

06:43

Propic Cloud.

06:45

Agent SDK. Vou ter.

06:50

O meu config.

06:51

E aqui dentro do meu config.

06:55

Será necessário. Utilizar aqui algumas.

07:01

Informações a mais. Para que a gente consiga.

07:05

Trabalhar 100%. Então API aqui. Como eu disse. Vocês vão exportar isso.

07:10

no seu terminal, juntamente com a chave de API. Logo,

07:14

a gente já vai conseguir encontrar por aqui.

07:17

Em relação ao modelo,

07:19

eu vou colocar para utilizar o CloudSony 4 .6.

07:25

Essas informações referentes a modelo e tudo mais,

07:28

basta você digitar no Google Model List e o seu provedor,

07:32

que vai ter ali todos os modelos que a gente pode...

07:36

utilizar, tá? Mostro isso agora pra vocês aqui.

07:39

Então, model list, por exemplo, topic,

07:45

aqui eu tenho lista de modelo, posso fazer a mesma coisa pro OpenAI,

07:50

eu tenho aqui a lista de modelo, ok?

07:53

Vamos voltar lá no VS Code pra gente dar continuidade.

07:57

Vou colocar aqui também o meu working dir,

08:02

que vai ser ponto, tá?

08:05

Vou ter um setting sources project

08:11

depois

08:13

disso vou ter a minha skill que é

08:21

triagem issue

08:25

então

08:27

temos aqui nosso API key temos também o

08:34

modelo vou colocar aqui as questões de tools

08:40

que a gente pode utilizar ou não. Nesse caso aqui,

08:42

a gente vai fazer o uso somente da tool de read,

08:46

tá? E o permission mode vai ser accept edits.

08:53

Nesse caso aqui, é a permissão do próprio modelo, tá bom?

08:57

Feito isso, galera, eu já tenho aqui um dataset preparado com algumas informações,

09:03

então eu vou copiar e colar aqui.

09:06

E como vocês podem perceber, basicamente o que nós temos aqui é...

09:10

A mesma coisa que a gente tinha na parte de evals .json,

09:14

porém agora no formato Yalm,

09:17

né? Fechado? Nada muito diferente daquilo que a gente já tinha.

09:23

Com essa pequena configuração, o que a gente vai fazer?

09:26

A gente vai retornar aqui no nosso terminal.

09:31

E aí eu vou utilizar npx prompt full

09:35

eval.

09:38

Dar um yes aqui novamente.

09:41

E vamos ver o que vai acontecer.

09:43

O resultado não conseguiu identificar o nosso provedor.

09:47

Vamos dar uma olhadinha aqui. Aqui, na verdade, é

09:53

dois pontos, tá? Vamos rodar aqui de novo. Então, npx promptful evol.

10:02

Provavelmente vai dar um outro errinho,

10:03

exatamente como imaginado. Então, se por acaso,

10:08

galera, vocês ainda nunca utilizaram o Cloud Agent SDK,

10:14

Na máquina de vocês, tá?

10:15

Será necessário a instalação deste pacote. Como vocês podem perceber,

10:19

ele rodou o eval, porém ele não conseguiu chamar o SDK do cloud.

10:23

Por quê? Porque a gente não tem o agent SDK.

10:26

Então, o que a gente tem que fazer?

10:28

Fazer o processo de instalação. Vou fazer o seguinte.

10:32

Só copiar aqui, ó.

10:35

E aí eu faço o npm i e colo ele aqui. Aguarda aí o processo.

10:43

Aparentemente, tudo certo. Então, vamos lá, pessoal.

10:46

NPEX Promptful Evolve, mais uma vez.

10:50

E aí, vamos verificar. Praticamente finalizando aí o nosso teste.

10:55

Vamos aguardar mais um pouquinho.

10:57

E aí, eu tenho aqui o resultado.

11:01

Para que eu consiga ver, basta eu fazer um NPEX Promptful View. Vou

11:10

deixar que ele abra.

11:13

E aí, eu tenho o meu resultado.

11:16

Volto aqui no browser para mostrar para vocês e nós temos aqui o que aconteceu.

11:21

Como vocês podem ver, pessoal,

11:23

logo aqui em cima nós temos o apanhado geral daquilo

11:28

que aconteceu juntamente com as métricas que foram definidas no dataset,

11:32

que é o Promptful Config ali,

11:34

juntamente com o meu custo, total de tokens utilizados.

11:39

A média de tokens, latência e tokens por segundo, tá?

11:43

E logo abaixo a gente consegue ter uma ideia de estrutura,

11:47

o que passou, o que não passou, os itens que falharam e tudo mais.

11:52

Esses dois carinhas aqui que falharam, na verdade, eles deveriam ter passado, né?

11:56

Só não foi passado porque acabei esquecendo de

11:59

alterar ali para o nosso repositório correto,

12:02

tá? Mas, fora isso...

12:08

Ajustando isso aí, eles iriam passar também, beleza? Então, aqui,

12:12

o mais legal de tudo é o que?

12:14

É que a gente consegue, por meio do nosso Promptful Config,

12:18

aquele nosso arquivo que a gente estava trabalhando,

12:21

a gente consegue definir as nossas métricas, já mostro para vocês sobre isso,

12:25

e entender se elas vão disparar da forma que a gente deseja ou não.

12:30

Se a gente volta aqui no VS Code, dá uma olhada aqui, a gente tem a métrica AC,

12:39

E para ficar um pouco mais fácil,

12:41

para entender o que é a métrica que vai ser analisada ou não,

12:45

eu costumo separar isso em dois grandes mundos.

12:49

O primeiro deles é a métrica agregada, ou seja,

12:54

a gente tem ali métricas acerca de pass rate,

12:57

percentual dos casos que passaram em todas as ações ou não,

13:02

métricas voltadas para pass e fail.

13:07

Se cada ação de forma individual passou ou não.

13:11

A gente tem a parte geral de custo, de latência,

13:16

o tanto de token que foi utilizado. Temos também o threshold,

13:21

que é a nota mínima da média que

13:24

a gente considera interessante para ser aceito ou não.

13:30

Temos também a métrica de score ponderado, que é a média ponderada das ações.

13:37

É importante a gente entender que ele sempre vai ter um peso padrão de 1.

13:41

E eu também tenho algumas outras métricas que aí já entram em um critério um

13:46

pouco mais analítico e que realmente importa para a

13:49

gente na hora de pensar isso aqui,

13:50

que são os tipos de ação que a gente pode começar a trabalhar.

13:56

Então, eu tenho alguns grupos.

13:59

Na verdade, eu tenho dois grupos,

14:00

mas vários tipos de métricas que eu posso trabalhar.

14:04

O primeiro grupo é o determinístico e o segundo grupo são os models graded.

14:10

Quando a gente fala de métricas determinísticas,

14:12

a gente está falando de algo um pouco mais exato. Então, textos, estruturas, código,

14:17

lógica, coisas operacionais, similaridade e formato de forma geral. Então,

14:23

texto vai ter itens ali que a gente pode medir.

14:27

E qualidade, se contém, se não contém, se contém por completo,

14:30

se contém somente uma parte, não contém, coisas nesse sentido.

14:34

A gente tem coisas estruturais, que são validações de esquema,

14:39

lógicas de booleano e coisas nesse sentido.

14:45

Código e lógica, basicamente a gente consegue trabalhar com coisas mais arbitrárias,

14:50

baseado no output que a gente tem.

14:54

Temos também métricas de similaridade,

14:57

que é aquilo relacionado à similaridade de texto,

15:01

né? Com fórmulas de Leibniz, Rugen, Meteor.

15:09

E de outro lado, a gente tem os models graded, né?

15:13

Que é o que a gente está utilizando neste nosso exemplo, tá?

15:17

E o primeiro e talvez o mais usado são as rubricas de LLM,

15:21

que estão aqui, ó. Que são os types, né? As modalidades aí.

15:25

Dos tipos de avaliação que nós temos. E esse cara aqui. Ele vai avaliar para você.

15:31

O critério que você escrever. Então. O que eu quero.

15:36

Nesse teste aqui. Pergunta genérica de Git. Que não toca na skill.

15:43

O prompt. Qual a diferença entre Git merge e Git rebase. E o assertion.

15:49

É o que? Um type. Aonde eu tenho a métrica,

15:54

não dispara, ou seja, não deve disparar,

15:57

e o valor aprovado se responde conceitualmente sobre merge e rebase,

16:02

e não produz nenhuma triagem da issue, nem chama o GitHub MCP.

16:08

O que está acontecendo aqui? Basicamente,

16:10

a gente vai ver a resposta e automaticamente vai ser analisado via LLM,

16:16

claro, se bate com a rubrica. Se o resultado disso tudo aqui

16:22

não for o resultado da nossa skill,

16:27

é porque está aprovado.

16:29

Então, a gente consegue fazer essa rubrica e consegue entender se passou ou não.

16:34

E aí, já trazendo a nível de prompt full,

16:37

que eu não havia mostrado ainda o nosso dataset,

16:40

se vocês repararem bem, a gente tem uma estrutura bem definida,

16:42

que é o quê? A descrição,

16:44

no qual a gente precisa avaliar as variáveis que a gente

16:47

vai trabalhar e o que a gente espera de assertion.

16:50

O assertion em si vai ser o quê? O tipo que a gente espera,

16:54

a métrica desejada a ser avaliada e o nosso valor, beleza?

16:59

Além da rubrica, que é aquilo que eu falei, a gente vai utilizar bastante,

17:03

a gente tem ainda alguns outros contextos de model graded, tá? Então,

17:08

a gente tem aqui um carinha que se chama Gievol,

17:11

ok? Esse cara, ele vai se assimilar muito...

17:16

com LLM Rubric, mas com raciocínio estruturado,

17:20

ou seja, utilizando ali meio que um chain of thoughts. Temos também o Factuality,

17:26

que vai medir referência de resposta. Temos o Similar também,

17:30

Que vai analisar a similaridade mais voltada a coisas de embed,

17:36

similaridade semântica ali. Temos o Select Best,

17:40

que vai comparar a saída de vários providers /,

17:45

Pronto. E escolher qual foi o melhor.

17:49

E, além disso, temos também o moderation, que vai,

17:53

como o próprio nome já diz, fazer...

17:56

comparações ali relacionadas a conteúdo tóxico,

17:59

de forma inadequada e coisas nesse sentido. Além disso,

18:03

a gente também tem algumas métricas voltadas para RAG e coisas acerca disso aí,

18:08

mas eu não vou cobrir muito, por quê?

18:10

Porque nosso foco aqui é skill. Quando a gente está utilizando skill de forma geral,

18:15

nossa tendência é utilizar bastante aqui a parte de rúbrica,

18:18

que é o que mais vai fazer sentido, vamos dizer assim, para o teste.

18:24

Da skill em si, da habilidade do resultado que está sendo utilizado. E uma outra também,

18:30

que eu gosto bastante de utilizar, é o Select Best,

18:33

porque quando a gente está testando em diversos modelos diferentes,

18:36

a gente pode trabalhar de forma a testar e já

18:40

unificar a melhor resposta a partir daquele modelo que foi exibido. Então, pessoal,

18:46

o PromptFull é mais uma alternativa para a gente avaliar de fato

18:54

se foi coberto e o que foi produzido por aquela skill,

18:56

se faz sentido a nível de multimodelo ou não. E, obviamente,

19:01

tudo que eu mostrei aqui foi uma breve demo do que o PromptFull pode fazer,

19:05

mas a gente pode ir trabalhando ele com diversas outras maneiras,

19:10

não só a nível de skill, mas de prompt e coisas a mais.

19:15

Inclusive, se você quiser,

19:17

você pode pegar exatamente isso aqui que a gente fez e colocar em uma pipeline.

19:21

De CI e CD que fica rodando ali e a gente meio que forma uma pipeline ágil, né?

19:27

Pra todo momento que a nossa skill for alterada,

19:32

for atualizada, tiver algum processo de manutenção,

19:35

a gente faz aí de novo todo o processo de assertion e

19:38

tal pra garantir que ela continua viável ainda pra uso,

19:41

fechado? Então fica aí a dica pra vocês.

## Resumo IA

[RESUMO_IA]