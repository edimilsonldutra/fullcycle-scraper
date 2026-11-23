Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17986)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, seguinte, a feature foi escrita, a gente recebeu aquele relatório,

00:05

mas lembra, a gente está falando de Harness Engineering.

00:08

Harness Engineering não é algo que é mágico, porque se fosse algo mágico,

00:13

era qualquer pessoa somente dando comando em diversos workflows e etc.

00:19

E a nossa ideia não é essa, é conseguir entender esse ciclo de desenvolvimento,

00:24

inclusive pegar inconsistências e problemas que acontecem no meio do caminho.

00:29

Quando você olha para software,

00:31

o que você mais percebe é que grande parte do tempo que você passa

00:34

trabalhando em desenvolver o software não é

00:37

necessariamente em gastar esse tempo criando novas features,

00:44

mas sim arrumando o ambiente, refatorando, corrigindo testes, organizando,

00:49

ajustando pipelines de CI, CD e etc.

00:53

E quando a gente termina, por exemplo, uma feature que foi o que a gente fez...

00:57

A gente tem que verificar se tudo realmente está funcionando.

01:01

Mas quando eu digo funcionando,

01:03

não no sentido apenas de você chegar e testar a

01:06

interface do sistema e ver se está ok.

01:07

É na realidade ver se tudo está funcionando no processo de desenvolvimento em si.

01:13

Então, se você olhar agora aqui,

01:15

o que eu tenho? Eu tenho aqui, estou no meu branch main,

01:18

tá? E eu tenho aqui o meu cloud.md. Nesse momento,

01:23

são momentos que eu posso testar e revisar e refazer

01:27

algumas coisas que podem me ajudar nos próximos ciclos.

01:30

Por exemplo, eu tenho uma estrutura de diretórios agora.

01:33

Tem algumas dicas que eu posso passar aqui para a gente que talvez possam me ajudar.

01:38

Então, a primeira coisa que eu fiz aqui foi o seguinte.

01:41

Eu derrubei todo o meu ambiente e eu vou colocar aqui.

01:44

Inicie o ambiente.

01:48

E vamos ver se realmente esse script está agora conseguindo iniciar o ambiente.

01:53

Porque a gente tem migrações que às vezes vão ter que ser aplicadas,

01:56

ele vai haver banco de dados e coisas desse tipo.

01:58

E se a gente tiver qualquer tipo de problema nesse momento,

02:02

aí é o momento de a gente resolver o problema.

02:04

Aparentemente, está tudo rodando aqui, onde eu posso parar,

02:07

inclusive dar um clean e tudo mais para colocar.

02:11

E ele trouxe aqui para mim, backend, web, database, arquivos de log,

02:17

e de backend e arquivos de log de frontend aqui para mim.

02:21

Beleza. Então, o ambiente aqui iniciou. Se eu abrir agora o meu web,

02:27

aqui o meu frontend,

02:28

o que vai acontecer? Eu tenho que, deixa eu dar um atualizar,

02:32

tem que aparecer aqui para mim.

02:34

Maravilha, abriu o sistema, ok.

02:37

Está realmente muito igual ao que a gente tinha colocado,

02:40

eu não quero chegar em nível de detalhe agora,

02:42

a gente vai falar de alguns aspectos qualitativos depois.

02:45

Mas agora, o que que acontece? Eu vou criar uma conta aqui,

02:48

tá? Vou colocar uma conta chamada Wesley, vou colocar

02:53

Wesleyadmin, arroba admin.com, vou chamar esse cara de admin,

02:59

vou colocar aqui admin, apesar de que ele nem vai deixar,

03:02

né? Eu vou colocar a 1, a 2, a 3, a 4, arroba, a 1, a 2, a 3.

03:09

A 4, arroba, e criar a minha conta aqui. Então,

03:12

eu vou criar a minha conta, e ele criou,

03:14

e ele já fez e caiu autenticado na minha tela de login.

03:17

Certo? Agora eu vou fazer o logout.

03:20

Beleza, fez o logout. Vou tentar fazer o login de novo.

03:23

E eu vou colocar admin, arroba admin .com.

03:27

A1, A2, A3, A4, arroba. E ele fez o login de novo. Beleza,

03:32

está funcionando aqui essa minha feature. E beleza, estou feliz da vida.

03:37

Mas o que eu posso melhorar em relação a ciclos aqui? Bom,

03:41

a primeira coisa que a gente tem que pensar é...

03:43

Lembra que a IA tem que ter um processo fácil de testar e utilizar o sistema.

03:50

Se você perceber,

03:51

o que eu tive que fazer agora para conseguir

03:53

entrar na área entre aspas administrativas do sistema?

03:56

Eu tive que criar uma conta.

03:59

Então, o que eu posso, nesse momento,

04:01

melhorar de cara que eu posso chegar e pedir aqui para a IA?

04:04

Eu posso chegar aqui e falar para ela criar uma

04:07

SID com usuário e senha padrão para mim.

04:10

Dessa forma, fica mais fácil para eu logar nas outras vezes.

04:14

Mas não é somente para eu logar,

04:16

para ela logar também. Então, eu vou colocar assim, ó.

04:19

Crie uma seed de

04:23

usuário com o nome admin,

04:28

email admin, arroba admin .com e

04:34

senha admin, tá?

04:38

vou pedir para ele colocar, fazer essa criação dessa seed. Agora, o grande ponto,

04:42

se você perceber agora aqui,

04:43

a gente vai começar a pensar em fluxo também de desenvolvimento.

04:48

O que isso significa?

04:50

Se eu simplesmente peço para ele sair e criar alguma coisa desse tipo,

04:54

nesse momento eu estou fazendo isso no branch main.

04:58

Então, eu vou fazer isso no main.

05:00

Mas você vai perceber que eu vou pedir para ele

05:02

mudar de branch depois em seguida para mim,

05:04

para a gente fazer um commit e daí, por exemplo,

05:08

fazer uma pull request. Então,

05:10

eu vou dar um enter aqui e vou pedir para ele fazer isso,

05:13

para ele fazer essa...

05:14

Provavelmente ele vai criar uma espécie de alguma migration aqui para mim.

05:18

Mas antes da gente, inclusive, cair nesse aspecto,

05:21

a gente vai entrar também em outros níveis também de

05:25

melhoramento que a gente tem que trabalhar aqui para a gente.

05:29

Então, vamos aguardar ele trabalhar e vamos nessa.

05:35

E está ele aqui criando a SID para a gente. Então,

05:38

ele criou aqui, está criando aqui no Prisma e etc.

05:42

E agora, o que ele vai fazer aqui, se você perceber?

05:45

Ele vai dar aqui para a gente um Run Migrations.

05:47

Perceba que ele está rodando o Run Migrations para ver se

05:50

ele encontra algum problema aí no meio do processo. Então, ele achou um erro.

05:56

Então, vamos aguardar ele ajustar aqui todo esse processo.

06:02

Aqui tem uma coisa interessante pra gente olhar, inclusive, tá?

06:06

Ele falou que ele tava encontrando um erro e daí ele resolveu mudar...

06:11

O script para gerar seed de dentro de Prisma barra seed para scripts barra seed. E aí, nesse momento,

06:17

eu tenho que refletir porque eu poderia falar, poxa,

06:19

não, eu não quero misturar seed com script.

06:22

Mas se você pensar bem, esses scripts me ajudam exatamente nesse tipo de coisa,

06:27

para carregar coisas e etc. Então, eu acho que,

06:30

pelo menos na minha interpretação agora,

06:32

está adequado deixar dentro da pasta scripts.

06:34

Mas esses tipos de detalhes aqui para a gente,

06:37

ele é muito importante para a gente olhar.

06:39

Então, ele fez isso,

06:41

rodou a aplicação e ele trouxe aqui para mim o que foi criado. Então,

06:45

ele criou seeds e depotente, ou seja,

06:48

ele consegue criar admin .admin .com. Se ele é admin, it's true.

06:53

Adicionou isso aí lá no package .json, né? E eu posso dar um npm run seed,

06:59

prisma seed, e ele vai rodar essa seed aqui para mim,

07:02

tá? Agora, olha só que interessante. Então,

07:05

quer dizer que toda vez que eu subir o sistema,

07:09

Eu posso pedir, inclusive,

07:11

para ele trabalhar comigo na criação do usuário por padrão. Então,

07:17

o que eu posso colocar aqui? Eu posso ter algumas opções. Eu posso ter uma opção de,

07:23

quando eu iniciar o ambiente, que é o meu init .sh,

07:28

pedir apenas para ele iniciar e estartar o projeto,

07:31

mas também, se eu quiser, eu posso chegar e falar,

07:35

cara... Se eu der um init .sh e pedir para ele dar um "-seed",

07:40

eu poderia pedir para ele já criar os usuários administrativos ali para mim. Então,

07:46

isso aí é uma opção que eu posso trabalhar.

07:48

Vamos fazer isso e no próximo vídeo a gente faz rapidinho essa implementação.

07:53

Eu vou pedir para ele fazer para a gente testar.

## Resumo IA

**Abreviações**
*   **CI:** Continuous Integration (Integração Contínua)
*   **CD:** Continuous Deployment / Continuous Delivery (Implantação Contínua / Entrega Contínua)
*   **IA:** Inteligência Artificial (referindo-se a uma ferramenta assistente ou copilot)
*   **NPM:** Node Package Manager
*   **Seed:** Dados iniciais ou de configuração que são inseridos em um banco de dados para fins de desenvolvimento ou teste.

**Resumo**
A aula aborda a importância do "Harness Engineering", que vai além da simples execução de comandos, focando na compreensão do ciclo de desenvolvimento de software e na identificação e resolução de inconsistências. O instrutor destaca que grande parte do tempo de desenvolvimento não é gasto na criação de novas features, mas sim na arrumação do ambiente, refatoração, correção de testes e ajuste de pipelines CI/CD.

O objetivo prático da aula é aprimorar a experiência do desenvolvedor (DX) e a robustez do processo. Para isso, o instrutor demonstra o fluxo de trabalho após a conclusão de uma feature:
1.  **Verificação do Ambiente:** Inicia-se o ambiente de desenvolvimento (`init.sh`), garantindo que todas as partes (backend, frontend, banco de dados, logs) funcionem corretamente, incluindo a aplicação de migrações.
2.  **Teste Funcional:** Realiza-se um teste funcional básico da feature recém-implementada (criação de conta, login e logout) para validar sua funcionalidade.
3.  **Identificação de Otimização:** Percebe-se que o processo de criação de uma conta para cada teste é repetitivo e ineficiente.
4.  **Automação com IA:** Utiliza-se uma ferramenta de IA para gerar uma *seed* de usuário padrão (e.g., admin@admin.com, senha admin), facilitando o acesso e teste do sistema.
5.  **Reflexão sobre o Fluxo:** O instrutor pondera sobre o fluxo de desenvolvimento, observando que a alteração está sendo feita no branch `main` e que, idealmente, deveria ser em um novo branch para um commit e Pull Request.
6.  **Gerenciamento de Scripts:** A IA gera o script de seed usando Prisma e resolve um erro ajustando o caminho do script de `Prisma/seed` para `scripts/seed`, o que gera uma reflexão sobre a organização dos scripts no projeto.
7.  **Execução da Seed:** O script gerado é verificado e pode ser executado via `npm run seed` ou `prisma seed`.
8.  **Proposta de Melhoria do Ambiente:** Sugere-se integrar a execução da seed diretamente no script `init.sh` com uma flag (e.g., `init.sh -seed`), permitindo que usuários administrativos sejam criados automaticamente ao iniciar o ambiente de desenvolvimento.

**Pontos de atenção**
*   **Harness Engineering vs. Mágica:** Não se trata de uma solução mágica, mas sim de uma abordagem que exige compreensão profunda do ciclo de desenvolvimento para identificar e resolver problemas.
*   **Priorização do Tempo:** A maior parte do tempo de desenvolvimento é dedicada à manutenção e otimização do ambiente e processo (refatoração, testes, CI/CD), e não apenas à criação de novas funcionalidades.
*   **Verificação Abrangente:** O "funcionamento" de uma feature não se limita à sua interface. É crucial verificar se todo o processo de desenvolvimento, incluindo ambiente, migrações e logs, opera sem problemas.
*   **Melhoria Contínua da Experiência do Desenvolvedor (DX):** Buscar constantemente maneiras de tornar o processo de desenvolvimento mais fácil e rápido, como a criação de seeds para dados de teste.
*   **Gerenciamento de Fluxo de Trabalho (Git):** Atenção ao branch de trabalho; mudanças de otimização, como a criação de seeds, devem seguir o fluxo padrão de branches, commits e pull requests, mesmo que geradas por IA.
*   **Tomada de Decisão na Organização de Código:** Ao delegar tarefas a ferramentas de IA, é fundamental refletir sobre as decisões tomadas por elas (ex: mudança de diretório de scripts) e garantir que se alinham às boas práticas e arquitetura do projeto.
*   **Idempotência:** A criação de seeds deve ser idempotente, ou seja, pode ser executada múltiplas vezes sem causar efeitos colaterais indesejados, garantindo a consistência do ambiente.