Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17988)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, no vídeo anterior a gente fez essas mudanças do init, etc.

00:06

Mas agora está na hora de a gente botar as barbas de molho e

00:10

dar uma refletida no que a gente pode melhorar aqui no meio do processo.

00:14

Bom, como eu tinha colocado aqui para vocês, essa city vai nos ajudar.

00:21

a fazer com que o agente e nós mesmos

00:23

não precisemos ficar criando contas o tempo todo.

00:26

Então, o que eu vou pedir aqui para mim?

00:28

Eu vou pedir para no meu cloud.md, no meu cloud.md,

00:34

eu vou colocar assim, adicione, agora no meu arroba aqui,

00:39

agent.md, uma nota

00:44

passando o usuário e senha padrão para login.

00:51

E a URL.

00:55

Por que eu já coloquei passando a URL? Pode parecer lógico, né?

00:58

Mas o grande ponto aqui no meio da história é que,

01:03

já que eu já estou passando usuário e senha,

01:06

não custa ter a URL ali no meio do processo,

01:09

porque daí fica mais fácil ainda para a gente trabalhar.

01:14

É óbvio que ele poderia processar, olhar as rotas e tudo mais,

01:17

mas já é uma coisa que está tão na mão que já fica mais fácil. Então, aí que está o negócio.

01:22

O grande ponto aqui é que a gente tem que tomar cuidado com o quê?

01:29

Com a parte de informação a mais que ela coloca, aqui nesse caso,

01:34

que eu acho que eu não preciso ter no meu Cloud.md, tá?

01:37

Por exemplo, sign in at the web URL, printed, etc., colocando, por exemplo,

01:43

extract the port. Cara, eu não preciso entrar nesse nível de detalhe, entendeu?

01:51

sign in, eu posso simplesmente nesse ponto colocar aqui,

01:55

posso colocar nesse caso aqui

01:59

sign in

02:02

url, posso

02:08

colocar sign in url, eu não vou colocar printed by,

02:11

eu posso colocar já direto aqui url e aqui eu posso colocar port

02:17

aqui para ele, barra login,

02:21

para mim e acabou.

02:26

e eu vou contar com o bom senso dele aqui em relação à porta. Mas o que acontece?

02:31

Quando esse cara inicializar, ele vai ter esse conhecimento em relação às portas.

02:36

Caso ele não tenha, e a gente vê que ele começa a ter problema,

02:40

aí eu posso colocar qual é a porta que eu quero trazer.

02:44

E eu não quero, eu poderia colocar a porta padrão é a porta 3000,

02:47

mas como na maioria das vezes a gente vai trabalhar em WorkTree,

02:50

eu não quero ficar dando um padrão para ele,

02:52

já que grande parte das vezes a gente não vai rodar na 3000. Então,

02:56

eu vou trabalhar dessa forma aqui com a gente. Então, vou deixar aqui.

03:01

Então, uma vez que nós já temos esse detalhe em relação à parte de seed,

03:06

o que a gente pode melhorar aqui para a gente em relação aos nossos...

03:11

aos nossos... aos nossos... o nosso...

03:16

como se diz no meu agent.md? Bom, seguinte.

03:20

Quando eu estou... aqui falando sobre o meu backend development, aqui,

03:26

né? Onde eu falo, onde eu tenho o monorepo e etc.

03:30

E tudo mais.

03:32

Eu poderia agora começar a melhorar um pouquinho esses tipos de detalhe,

03:38

né? Eu posso agora fazer o seguinte.

03:41

Eu posso colocar, né? Eu tenho apps barra web,

03:45

onde eu falo que eu tenho o Next.js, eu tenho um package.json,

03:48

mas eu posso, na realidade... dar uma melhorada e colocar algo desse tipo aqui,

03:54

ó. Inclusive eu preparei isso aqui pra gente, tá?

03:58

Eu posso colocar apps barra web aqui pra mim

04:02

e tentar deixar um pouco mais claro dessa forma.

04:07

Onde eu posso passar já a pasta pra tentar

04:10

deixar um pouquinho mais claro ali pra ele.

04:12

Mas o grande ponto não é isso, na realidade, tá? Isso aí é só uma frescura.

04:16

Mas o ponto principal tá aqui. Em relação ao back-end,

04:21

porque isso aqui que eu acho que acaba mudando bastante aqui.

04:26

E aí vai depender muito de cada pessoa e de cada...

04:30

e do entendimento de cada um, tá? Mas eu acho,

04:35

pelo menos no momento que a gente está do projeto,

04:38

vale a pena a gente colocar apps back-end,

04:41

passando qual que é o back-end, e colocando Clean Architecture API,

04:45

tá? Eu vou colocar aqui, na realidade...

04:49

eu vou colocar da seguinte forma. É, Clean Architecture API, e eu vou colocar aqui, ó,

04:56

src split into config, domain, use case, infra.

05:00

Entry, o ponto de entrada é src,

05:04

src main.ts, tá? Então,

05:07

isso aqui pode ajudar a IA se identificar um pouquinho

05:13

melhor em relação à arquitetura de como que isso está rodando, tá?

05:18

Significa que eu vou colocar isso no restante do projeto?

05:22

Acredito que não, mas a gente já tem essa estrutura de pastas hoje.

05:26

Eu não quero colocar aquela árvore inteira onde eu poderia,

05:30

mas eu já estou dando um indicativo aqui pra ela.

05:33

Aí provavelmente, o agente provavelmente iria achar isso.

05:38

no nosso ambiente, dando um grep, entendendo esse tipo de coisa? Sim,

05:42

mas eu só estou querendo reforçar aqui pra ele a

05:44

forma de como eu estou trabalhando com arquitetura.

05:46

Depois disso eu posso até criar um documento só sobre

05:49

a parte de arquitetura em relação ali pra ele,

05:52

e daí talvez a gente possa remover essa linha

05:54

e fazer apenas uma ligação depois com isso.

05:57

Eu acho que isso aí é um ponto importante.

06:01

Outra coisa que a gente poderia colocar...

06:08

Mudanças em relação ao banco de dados, eu acho que por enquanto está ok.

06:14

Eu acho que a gente está de boas. Então,

06:20

o que a gente pode pensar daqui pra frente, galera?

06:24

Que a cada mudança, a cada parte que a gente evolui,

06:29

a cada feature que a gente faz no projeto, nós podemos...

06:33

e melhorar e fazer algumas atualizações ali no nosso cloud.md.

06:39

E é o que eu vou fazer agora aqui,

06:41

que eu fiz essas alterações muito básicas,

06:43

mas elas já vão nos ajudar nas próximas iterações ali com a IA.

06:48

A gente tem que ficar de olho nessa alteração aqui pra gente. Então,

06:53

como que eu consigo fazer essa verificação agora? Meu agents.md está salvo.

06:59

Então, pra gente fazer uma validação, o que eu posso fazer aqui nesse momento?

07:03

Vou colocar assim, derrube o ambiente e limpe, né?

07:08

Ou seja, ele vai dar um stop, vai dar um menos clean ali para a gente.

07:12

E agora, o que eu vou fazer? Eu vou criar uma nova sessão, tá?

07:20

E eu vou fazer o seguinte, tá?

07:24

Inicie o ambiente aqui para mim.

07:34

Vamos aguardar.

07:36

Está iniciando o ambiente. Vamos lá.

07:54

Pronto. E aqui ele falou, ah, o ambiente já estava rodando e etc.

07:58

Eu vou falar assim, não.

08:01

Derrube todos os ambientes e limpe.

08:06

Não tem essa. Eu tenho que testar da forma certa. E é isso.

08:09

São pontos que a gente gasta aquele nosso tempo precioso com a IA. Mas lembrando,

08:15

é pelo um bem maior aqui para a gente. Vou colocar agora.

08:19

Eu vou limpar e vou pedir para ele subir.

08:21

O ambiente de novo aqui para mim, para garantir que vai estar tudo funcionando.

08:26

Vamos aguardar,

08:34

rodando, Docker, e etc, e beleza,

08:38

e agora aqui ele já está trazendo aqui para mim,

08:42

já estava rodando no Docker, o branch seed,

08:44

e agora aqui ele trouxe o usuário e uma porta,

08:47

e já com a tela de login. E agora, o que eu vou fazer?

08:50

Eu vou tentar fazer o login aqui, com o meu admin,

08:53

arroba admin.com, sem espaço, e conseguir fazer...

08:59

o login aqui, beleza, aqui pra mim. Então, beleza, rodou,

09:02

ele já trouxe e ele já sabe o usuário e senha,

09:05

ele não teve problema em descobrir a porta,

09:07

né, então pra gente já é um ponto importante. Então, agora,

09:11

o que eu vou fazer? Vou dar um commit aqui pra mim e

09:21

maravilha, ele já fez as alterações.

09:25

Alguns fluxos comuns, tá, pessoal? Sei lá,

09:28

usando o cloud, ou você poderia escrever manualmente,

09:31

ou usar qualquer skill pra fazer isso, eu posso trabalhar com pull requests,

09:36

então eu posso dar um commit a push .pr e aqui ele já vai criar pra

09:42

mim uma pull request pra que eu possa fazer o merge ali no meu branch main,

09:47

tá? Então só tô fazendo algumas vezes, eu vou fazer esse processo,

09:51

somente pra gente alinhar o tempo todo.

09:55

Que normalmente, né, no dia a dia, a gente não faz push direto no master,

10:00

como que a gente fez nas interações anteriores, tá? Mas de qualquer forma,

10:06

somente pra gente olhar aqui, pra gente, ou seja, adicionar as credenciais, Monohap,

10:11

arquitetura, e eu vou dar um merge nessa pull request, não

10:17

temos ainda pipelines, ICA e CD, beleza, e eu vou dar um delete branch remoto, tá?

10:25

Uma vez que eu dei esse delete remoto, esse branch remoto,

10:29

o que eu posso fazer é o seguinte, eu posso dar aqui um git checkout main, tá?

10:35

Somente para você saber, toda vez que eu dou uma exclamação aqui na frente,

10:39

significa que eu estou digitando um comando bash e

10:41

esse comando entra no contexto aqui do agente.

10:44

Então, eu posso colocar aqui, eu posso falar para ele dar um pull, ou

10:52

seja, vai pegar as alterações novas.

10:55

E aqui, o que acontece agora?

10:59

Eu posso dar também um commit clean gone.

11:03

Eu não sei se você conhece esse plugin,

11:06

Isso aqui é bem útil porque ele verifica se o

11:10

repositório que eu tenho local na minha máquina existe remoto.

11:14

Se ele não existe mais remoto, ele fica marcado como clean gone, ou seja,

11:18

a gente já até removeu ele lá de cima,

11:20

então eu quero que ele remova local aqui na minha máquina.

11:23

Então quando eu faço isso...

11:24

ele já vai matar todos os meus repositórios locais que já estão mesclados

11:28

e que nem já existem mais lá no GitHub ou lá no seu repositório, tá?

11:36

E ele trouxe aqui pra mim, ó,

11:38

Deleted ali o seed ali pra gente. O seed aparece como gone,

11:43

então ele mandou esse cara trabalhar.

11:46

E o feature01 landing page é a mesma coisa,

11:50

eu vou colocar também pra ele remover, remova.

11:53

O F01 landing page. Esse cara a gente não fez por request,

11:56

por isso que tá trabalhando,

12:00

né? E óbvio, eu poderia digitar, né? Git rm, git branch -d,

12:07

mas ele já foi.

12:08

Então tô com um repositório aqui e eu tô feliz em

12:12

tê-lo porque eu tenho a minha primeira parte das minhas features desenvolvidas.

12:16

Agora a gente vai entrar numa outra fase.

12:20

que vai ser a nossa fase do desenvolvimento do nosso feature número 3.

12:24

E aí tem alguns aspectos que a gente vai ter que levar em consideração. Vamos nessa.

## Resumo IA

**Abreviações**

*   **API**: Application Programming Interface
*   **CI/CD**: Integração Contínua/Entrega Contínua (Continuous Integration/Continuous Delivery ou Deployment)
*   **IA**: Inteligência Artificial
*   **Next.js**: Um framework de desenvolvimento web baseado em React.js.
*   **PR**: Pull Request (Pedido de Pull)
*   **src**: Source (diretório de código fonte)
*   **WorkTree**: Em contextos Git, refere-se a um diretório de trabalho vinculado a um repositório, mas no contexto da aula, sugere um ambiente de desenvolvimento onde a porta padrão (e.g., 3000) pode não ser a utilizada.

**Resumo**

A aula focou na otimização da interação com um agente de desenvolvimento de software, aprimorando sua capacidade de entender e operar no ambiente do projeto. O objetivo principal foi refinar as instruções fornecidas ao agente para aumentar sua eficiência e reduzir a necessidade de intervenção humana repetitiva, especialmente na criação de contas e no entendimento da arquitetura do sistema.

Inicialmente, o instrutor demonstrou como melhorar a configuração de `seed` no `cloud.md` e `agent.md`. Foi adicionado ao `agent.md` o usuário, senha padrão e a URL de login, visando simplificar o processo de inicialização do ambiente e login. A instrução foi refinada para evitar detalhes excessivos que poderiam confundir a IA ou fazê-la "gastar tempo precioso", focando apenas nas informações essenciais como "sign in url" e "port".

Em seguida, a aula abordou a melhoria da comunicação da arquitetura do projeto ao agente. No `agent.md`, foi adicionada uma descrição mais detalhada da estrutura do monorepo, especificando as aplicações (`apps/web` com Next.js) e, crucialmente, o backend. Para o backend, foi explicitado que ele segue a "Clean Architecture API", com a estrutura de pastas (`config`, `domain`, `use case`, `infra`) e o ponto de entrada (`src/main.ts`). Esta clareza visa auxiliar a IA a identificar e compreender melhor como o código está organizado.

Para validar as alterações, o instrutor demonstrou um fluxo de teste: derrubar e limpar completamente o ambiente, criar uma nova sessão e iniciar o ambiente novamente. Após o ambiente estar pronto, o login foi realizado com as credenciais padrão, confirmando que a IA conseguiu inicializar o ambiente e apresentar a tela de login corretamente, além de inferir a porta sem problemas.

Finalmente, a aula concluiu com a demonstração de um fluxo de trabalho Git padrão, incluindo `commit`, `push .pr` para criar uma Pull Request, o processo de merge e a exclusão da branch remota. Foi apresentada a ferramenta `commit clean gone`, um plugin que remove automaticamente branches locais que já foram mescladas e não existem mais remotamente, mantendo o ambiente de desenvolvimento local limpo e organizado.

**Pontos de atenção**

*   **Evitar Detalhes Excessivos para a IA**: Ao fornecer instruções no `agent.md`, é crucial ser conciso e direto. Detalhes minuciosos, como "extract the port" ou "printed by", podem confundir a IA e levá-la a processar informações irrelevantes, desperdiçando tempo e recursos. Focar na informação essencial é a chave.
*   **Clareza na Arquitetura**: É fundamental descrever a arquitetura do projeto (e.g., Clean Architecture, estrutura de pastas como `config`, `domain`, `use case`, `infra` e o entry point) para que a IA possa compreender a organização do código e operar de forma mais eficaz, sem precisar "adivinhar" ou usar comandos como `grep` para entender o ambiente.
*   **Atualização Contínua da Documentação**: A cada nova feature ou mudança significativa no projeto, é uma boa prática atualizar os arquivos de configuração do agente (como `cloud.md` e `agent.md`). Isso garante que a IA esteja sempre ciente do estado atual do projeto e de suas características.
*   **Validação Rigorosa das Alterações**: Após fazer modificações nas instruções para a IA, é essencial validar se as alterações funcionam conforme o esperado. Isso inclui derrubar, limpar e reiniciar o ambiente completamente para garantir um teste em um estado inicial limpo, evitando problemas de cache ou estados antigos.
*   **Fluxo de Trabalho Git Robusto**: A adoção de um fluxo de trabalho Git com Pull Requests é uma boa prática para projetos colaborativos. Além disso, utilizar ferramentas como `commit clean gone` para limpar branches locais mescladas e deletadas remotamente mantém o repositório local organizado e gerenciável.
*   **Comunicação da Porta**: Embora a IA possa inferir a porta na maioria dos casos, estar preparado para explicitá-la se surgirem problemas é importante. Evitar a porta padrão (e.g., 3000) se o ambiente de trabalho (`WorkTree`) frequentemente utiliza outras portas é uma boa prática para evitar suposições incorretas.