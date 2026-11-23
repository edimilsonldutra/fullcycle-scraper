Módulo: Desenvolvimento de Agentes com IA\
Aula: [Dicas de desenvolvimento de agentes usando IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18580)

## Resumo da aula



## Transcrição

00:00

Nesta aula, eu quero falar sobre, agora, codificação com IA,

00:04

porque agora que nós já aprendemos,

00:06

nós já podemos usar um agente de IA de

00:09

desenvolvimento para desenvolver os nossos agentes de IA,

00:13

mas nós devemos tomar alguns cuidados.

00:17

Quando nós estamos trabalhando com ADK,

00:22

Lengraph, Lengchain ou N outros que já existem no mercado,

00:27

nós temos que entender

00:30

que os melhores modelos podem estar

00:34

treinados ou não com as últimas versões. Nós não sabemos.

00:40

E isso traz um risco,

00:41

porque se você está utilizando uma última versão de um framework de agente de IA,

00:47

você pede para o agente de IA de desenvolvimento criar as coisas para você,

00:51

ele pode criar as coisas de forma incorreta, utilizando...

00:56

coisas depreciadas. Então,

00:58

vem todas aquelas dicas de você criar a sua fundação de IA,

01:02

criar os Harners, para que você evite problemas.

01:06

São os trade-offs que nós vamos ter que lidar.

01:08

Ou a gente está treinado com versões mais antigas, ou às vezes nem está treinado.

01:13

E nós vamos ter que contorná-lo,

01:16

controlar a LLM para que ela crie as coisas de forma correta.

01:20

Na documentação do ADK, nós temos essa parte de coding, o IFAI,

01:25

que ele dá algumas dicas de como você pode melhorar

01:28

a sua experiência com a sua ferramenta de desenvolvimento.

01:31

Ele fala sobre o agent CLI,

01:33

que é um CLI que te ajuda a fazer o scaffold de um projeto,

01:37

fazer build, test, evaluate, nós não vimos no curso,

01:40

mas também recomendo que você dê uma olhada nele.

01:45

Tem a documentação acessível via MCP e

01:49

um índice que nós podemos pegar aqui

01:54

da própria documentação, que aí a...

01:58

Qualquer LLM vai entender o que ela tem que pesquisar,

02:00

aonde que ela tem que pesquisar.

02:03

Mas o que eu recomendo a princípio é que você faça

02:06

o uso dessa skill que está aqui no Skills.sh.

02:10

Você pode simplesmente pesquisar ADK.

02:13

O primeiro resultado é o mais conhecido.

02:17

Rode esse comando aqui no terminal e

02:24

escolha qual é a sua ferramenta.

02:27

Como ele já identificou aqui que eu tenho o Cloud Code.

02:30

Eu quero só no projeto, quero copiar todos os agentes.

02:36

Então, temos

02:41

aqui essa

02:44

parte do código, que

02:48

vai falar sobre essa estrutura do ADK, questão das pastas,

02:54

como criar os agentes e, obviamente,

02:57

a parte do workflow que nós vimos anteriormente. Então,

03:01

essa skill aqui é a skill para codificação.

03:06

Mas existem outras skills também para você poder

03:09

criar scaffold e outras coisas que estão nesse Agents.

03:14

CLI.

03:16

Você pode ler

03:22

um pouco mais sobre ele.

03:24

Tem um comando inicial, você pode fazer que é esse aqui,

03:28

que ele instala outras skills, cria um ambiente melhor.

03:33

Aqui eu só dou um aviso para que você use a opção menos --workspace.

03:39

para que ele coloque as coisas dentro do seu projeto e não faça global,

03:43

porque se você rodar esse comando,

03:45

ele vai instalar outras skills, vai ficar tudo global.

03:48

Eu prefiro fazer sempre no meu projeto quando eu estou trabalhando com isso.

03:53

Você coloca também sua Gemini API Key,

03:56

aí tem como até você rodar os agentes sempre por essa opção.

04:03

Vamos falar sobre... Cadê a minha documentação que eu perdi? Aqui. Na verdade, aqui.

04:15

A outra opção que nós temos é trabalhar com

04:17

o acesso à documentação através de um servidor MCP.

04:22

Então ele mostra aqui como configurar com anti-graft, cloud code.

04:29

Recomendo sempre que você faça configuração local, se você não trabalha só com ADK,

04:34

esse MCP só fica disponível nos seus projetos,

04:38

tem o cursor também e outras tools, você consegue configurar em qualquer lugar.

04:42

Isso aqui é uma boa opção justamente para poder

04:44

contornar essa situação que nós estamos falando,

04:48

dos agentes de ar não estarem devidamente adaptados às últimas versões.

04:53

Então você cria o seu arquivo de memória principal de qualquer ferramenta, por exemplo, o meu CloudMD,

04:58

e aí você fala que não

05:01

pesquise na internet sobre o ADK.

05:08

Sempre use o MCP do ADK.

05:13

Então ele sempre vai fazer essa pesquisa dessa forma.

05:17

Pode ser que em algum momento você queira pesquisar,

05:19

você poderia até deixar só pesquisar se eu autorizar ou se eu falar sobre isso. Então isso é interessante.

05:27

Nós vemos aqui que ele vai apontar para esse índice,

05:32

que é a outra opção que ele está dizendo,

05:34

se eu quisesse até,

05:35

sem usar o MCP e pedir para ele pesquisar alguma coisa na documentação,

05:42

Seria interessante pegar esse link e falar assim, olha,

05:44

eu quero pesquisar aqui sobre o workflow,

05:46

então esse aqui é o índice da documentação, me fale mais sobre ele.

05:51

Então seria interessante passar isso aqui para que você não

05:54

precisasse passar o ADK Web e ele descobrisse,

05:56

ou ficasse navegando desnecessariamente pelo HTML até que ele encontre alguma coisa.

06:03

Então essa opção, ela seria uma

06:07

opção oficial para a história do ADK.

06:11

Mas nós temos também a outra opção, que é o Contact7, que

06:17

é um serviço de documentação que nós conectamos via MCP.

06:22

Então, por exemplo, tem o ADK aqui?

06:24

Tem, ele está atualizado faz um mês.

06:27

Tinha uma época que ele não estava sendo tão atualizado assim,

06:30

então você pode configurar o Contact7 e colocar ali nos

06:34

seus arquivos de instrução para ele sempre se basear e pesquisar.

06:40

Focado na versão que você está, muito importante, se você está na 2.0 alguma coisa,

06:44

sempre pesquisando, ainda mais, colocar somente 2.0 não é legal.

06:50

porque se você estiver na versão 2 .0 alguma coisa,

06:53

e tem muitas correções, muitas diferenças,

06:57

então frisar ali a versão é essencial. Então,

07:03

eu não tenho trabalhado ultimamente com o Contact 7,

07:08

nem mesmo com o MCP para poder fazer essa consulta,

07:10

porque como eu já tinha falado durante a disciplina,

07:12

às vezes a documentação não é atualizada com tanta frequência.

07:17

E aí você está pegando uma versão muito nova, uma release, um patch que foi lançado,

07:23

e você precisa que o seu agente de IA leia o código -fonte,

07:27

esteja ali com o código -fonte debaixo do braço.

07:32

Então, o que eu tenho preferido fazer, essa é a outra dica,

07:35

então eu vou até falar para...

07:38

o lane chain e o lane graph também, é colocar a documentação na sua pasta docs.

07:45

Sempre você vai conseguir pegar essas documentações que vão estar no GitHub.

07:52

E a documentação aliada ainda com o código -fonte,

07:55

porque aqui eu tenho o código -fonte do Python,

07:58

apesar que do ADK do Python, você tem ali o venv, na

08:03

verdade eu acho que eu até tinha excluído o venv daqui, eu acabo tendo isso no venv.

08:10

Mas, enfim, se você quiser colocar o código -fonte aqui também como referência,

08:14

a questão é você colocar como referência tudo isso e colocar nas suas instruções.

08:19

Olha, então, no ADK

08:24

Docs,

08:27

documentação, no ADK

08:32

VM, mais o caminho até o ADK,

08:38

o Google ADK, código

08:43

-fonte, sempre

08:50

consulte aqui.

08:54

para você poder saber tudo o que você precisa. Então,

08:58

evite a internet, etc. Então, essas dicas são cruciais

09:04

para que você tenha um bom resultado com o seu agente de desenvolvimento.

09:10

E acredite, eu já experimentei muitas alternativas e essa aqui,

09:15

para mim, é a melhor.

09:17

E acaba sendo mais benéfico que o MCP no

09:20

sentido de você ter a confiabilidade local com o MCP.

09:25

Ele sempre vai fazer a chamada, pode demorar um pouco mais,

09:28

apesar que pode gastar menos tokens,

09:31

porque ele acaba fazendo pesquisas mais diretas,

09:34

mas às vezes essa pesquisa mais direta pode

09:38

não ter todo o contexto que você precisa para a IA poder

09:43

te dar a melhor resposta para que você faça o seu desenvolvimento. Então,

09:49

recomendado, você pode fazer da maneira que você quiser, mas...

09:54

Quero informar que esse é o melhor resultado que eu tenho no momento.

09:59

Então, dessa forma, você vai ter uma boa experiência.

10:04

Sempre também busque skills ou crie skills para

10:10

que você reforce boas práticas ou determinados comportamentos.

10:14

Não se limite apenas às skills da sua ferramenta.

10:16

Buscou, viu lá que o LinkedIn tem skill.

10:21

Mas eu sei que eu tenho aqui o comportamento...

10:25

Vamos pegar o caso do ADK. Nós sabemos que tool

10:30

confirmation com workflow, nesse momento, não é suportado. Então,

10:36

Isso aqui poderia virar instrução no Cloud MD?

10:39

Sim, mas dependendo da situação,

10:42

nós podemos criar skills para ter ali uma base e não carregar muita coisa.

10:48

Se você começa a ter muitas informações...

10:52

O seu arquivo de memória, porque a ideia é que esse arquivo aqui,

10:55

um CloudMD como esse, seja pequeno. Então,

10:58

essas são as dicas para que a gente consiga

11:01

desenvolver bem com IA os nossos agentes de IA.

## Resumo IA

[RESUMO_IA]