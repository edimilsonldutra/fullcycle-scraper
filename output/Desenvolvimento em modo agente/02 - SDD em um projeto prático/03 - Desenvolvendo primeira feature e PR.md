Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17781)

## Resumo da aula

A implementação orientada por especificação começa quando a skill correta está ativa no ambiente e o prompt pede explicitamente a execução usando esse contexto. Retomando o fluxo já preparado com scaffold, guidance e branch de feature, o ganho aqui é transformar a especificação em código executável com o mínimo de ambiguidade. Em um projeto Next.js, uma skill de boas práticas reduz desvios estruturais e ajuda a manter a implementação alinhada ao ecossistema esperado. O valor não está em “automatizar por automatizar”, mas em fazer a geração seguir restrições já definidas antes do código existir.

A execução não depende apenas da skill principal da stack. Durante a criação da feature, o agente pode carregar uma skill complementar, como Playwright CLI, para inspecionar a interface gerada e validar se o resultado visual atende aos critérios de aceitação. Isso evita depender exclusivamente de leitura estática de arquivos e permite que a IA interaja com a aplicação em execução, capture screenshots e observe a renderização real. Quando esse recurso existe via CLI, ele reduz a necessidade de acionar MCP continuamente para cada interação.

Playwright CLI permite abrir o navegador, navegar pela aplicação, tirar snapshots e registrar evidências visuais do estado da interface. Esse fluxo é especialmente útil quando a feature tem critérios de aceitação ligados a layout, presença de seções ou comportamento básico de navegação. No exemplo da landing page, a validação incluiu subir o servidor em uma porta disponível, abrir a aplicação, capturar a tela e verificar se as seções renderizaram corretamente. Esses artefatos podem evoluir para referências persistentes em ciclos futuros, conectando implementação e Harness Engineering.

A automação precisa lidar com o estado real da máquina, inclusive conflitos de porta. Em vez de falhar porque 3000, 3001 e 3002 já estavam ocupadas, a execução subiu o servidor em 3005 e continuou o processo. Esse detalhe mostra que a feature não é validada em um ambiente idealizado, mas em um ambiente de desenvolvimento sujeito a interferências. Ferramentas e prompts eficazes precisam tolerar esse tipo de variação sem quebrar o fluxo inteiro.

A landing page foi considerada pronta mesmo sem navegação funcional em create account e login, porque os links foram preparados para a próxima etapa sem inventar comportamento ainda não especificado. Isso é importante em SDD: cada feature entrega exatamente o que foi pedido e deixa pontos de integração explícitos para a sequência do projeto. Retomando a ideia de que uma feature “gruda” na outra, os caminhos /login e /register funcionam como contratos de continuidade entre entregas. O sistema avança por incrementos coerentes, não por completude prematura.

Depois da geração, subir novamente o ambiente e inspecionar a interface no navegador confirma se o que foi produzido corresponde à especificação. A checagem visual não precisa avaliar refinamento de design neste momento; ela serve para validar estrutura, identidade visual esperada e presença dos elementos essenciais, como hero, CTA, footer e fluxo principal descrito no PRD. Quando o objetivo é entregar uma primeira feature, “clean e aderente ao pedido” costuma ser mais importante do que polimento estético. Essa distinção evita retrabalho antes da hora.

Ao concluir a implementação, o próximo passo é registrar a mudança com um commit que reflita o conteúdo real do diff. Ferramentas integradas ao fluxo conseguem interpretar o que foi alterado e gerar uma mensagem mais estruturada, reduzindo commits vagos e melhorando a rastreabilidade. Isso acelera a passagem da implementação para a revisão sem exigir que o desenvolvedor escreva tudo manualmente. O benefício é maior quando o histórico do projeto precisa servir como documentação operacional.

A pull request consolida a entrega em um formato revisável: sumário da mudança, evidências de teste e pontos de atenção para quem revisa. No caso da landing page, o plano incluiu npm test, build e smoke test manual no navegador, além da orientação para conferir aderência visual ao estilo minimalista definido no PRD. Uma PR boa não apenas mostra “o que mudou”, mas também “como validar” e “o que ainda exige julgamento humano”. Isso torna o merge mais seguro mesmo quando parte da implementação foi assistida por IA.

O principal ganho do fluxo não é fazer tudo funcionar de primeira, e sim deslocar decisões para antes da implementação. Quando a especificação é detalhada o suficiente, inclusive com entrevistas e critérios de aceitação, muitos edge cases aparecem cedo e deixam de virar surpresa no código. Isso aumenta a assertividade da geração e reduz o espaço para interpretações arbitrárias do agente. O investimento inicial é maior, mas ele compra consistência nas features seguintes.

## Transcrição

00:01

Bom, pessoal, agora que a gente já tem essa skill instalada,

00:04

para quem utiliza Cloud Code,

00:06

vale a pena você dar um reload de skills,

00:09

mas isso vai valer para qualquer plataforma que você for falar,

00:14

a skill tem que estar ativa ali no seu sistema. E o que acontece?

00:20

Eu vou falar aqui para ele o seguinte,

00:23

eu vou colocar aqui no meu prompt, na minha chamada, faço implementação.

00:30

usando a skill, e

00:35

eu coloquei o nome da skill aqui para mim.

00:37

E agora eu vou pedir para ele fazer a execução aqui do meu projeto.

00:42

Então, vou dar um enter aqui, e

00:47

agora é onde que a mágica começa a acontecer, né? Ou seja,

00:53

tudo que a gente fez com esse monte de vídeo que a gente viu...

00:56

foi na realidade para a gente chegar nesse momento. Se você perceber,

00:59

ele já carregou a skill Next Best Practice aqui para mim,

01:03

então isso vai pelo menos dar um mínimo de

01:06

guideline para a gente não sair criando muita coisa errada,

01:10

apesar de que como o Next

01:13

.js já é um projeto muito conhecido,

01:18

a Yala já é muito treinada para isso,

01:20

então raramente ela vai fazer algo muito diferente. Ali no Next, tá?

01:27

Mas o grande ponto aqui é que a gente consegue ver

01:30

esse processo de criação e de como que ele vai fazer.

01:36

Existem também, pessoal, algumas abordagens que cada dia estão acontecendo mais, tá?

01:41

Que é usar as ferramentas, como que eu posso dizer,

01:46

sem estar dentro da IDE, tá?

01:49

E parte de algumas features eu vou mostrar isso aqui para vocês,

01:53

mas não necessariamente...

01:55

você é obrigado a trabalhar qualquer coisa dessa forma, tá? Mas se você ver,

02:00

ele está aqui trabalhando e ele está aqui produzindo a minha

02:04

landing page e está rodando e a gente tem que aguardar,

02:08

ele está dando build. Vamos ver quanto tempo ele demora para criar.

02:12

Se ele fizer isso de uma forma mais rápida, vai ser melhor aqui para a gente olhar.

02:19

Vou dar um pause aqui somente para ele terminar esse processo.

02:23

E pessoal, olha só o que está acontecendo aqui. Ele saiu criando,

02:28

ele foi ver portas que estavam utilizadas, viu que a minha porta 3000,

02:31

3001, 3002 estavam usadas, ele subiu na porta 3005.

02:34

Mas olha só o que começou a acontecer, o que ele começou a fazer aqui.

02:40

Ele utilizou uma skill chamada Playwright CLI,

02:46

que eu vou falar dessa skill aqui para vocês também.

02:49

E o que ela faz? Ela utiliza o Playwright.

02:52

para conseguir tirar screenshots e ver como é que está a tela.

02:58

Mas o que acontece?

03:00

O Playwright é algo muito importante.

03:06

Ele é extremamente utilizado, mas normalmente ele é utilizado via MCP.

03:12

Por outro lado,

03:14

existe um projeto do próprio Playwright que é chamado de Playwright CLI.

03:19

Ou seja, você não precisa usar MCP.

03:22

Basta você ter uma skill do Playwright CLI que a IA não

03:26

fica ali o tempo todo chamando o MCP e toda aquela história.

03:31

Ele saiu executando o comando CLI,

03:33

tirando os prints e conseguindo fazer todas as interações no site,

03:38

no sistema. Então, por padrão aqui, como tinha critério de aceitação,

03:43

provavelmente o meu modelo já olhou e falou: deixa eu ver como é

03:47

que está saindo esse site para ver se a parada está funcionando.

03:50

Então, ele criou aqui para mim, carregou a skill Playwright CLI. Perceba,

03:54

eu não coloquei nada disso no cloud.md, tá?

03:59

Mas ele conseguiu carregar, porque eu tinha,

04:01

e aí o nosso próximo passo eu vou mostrar depois

04:04

melhor aí para vocês o Playwright CLI também,

04:06

tá? Então, ele subiu o servidor, tá? Na porta 3005.

04:11

Aí ele, com o Playwright, abriu o browser,

04:14

né? Depois disso, tirou o snapshot.

04:18

Depois disso, salvou o snapshot.

04:21

Depois disso, colocou, deixa eu scrollar mais para baixo agora.

04:25

Depois disso, tirou, viu que está renderizando correto todas as sessões.

04:29

Parou o servidor. E aqui, ele falou para mim que fez a landing page,

04:34

implementando conforme a especificação, a página, os componentes, a CSS,

04:40

a testing harness, ou seja...

04:42

Tem um teste aqui que depois eu vou mostrar para vocês

04:45

os detalhes que fazem com que uma feature grude na outra,

04:50

inclusive, tá? Fez aqui next build,

04:53

next test, criou o header, o hero com CTA, laranja, né? Como que isso funciona,

04:59

o footer, os CTAs apontando para barra login e barra register, conforme o snapshot.

05:05

Depois... Quando a gente entrar especificamente só em Harness Engineering,

05:09

a gente pode ter os nossos critérios de aceitação,

05:12

inclusive pedindo que aqueles screenshots fiquem

05:15

salvos como referência para próximos desenvolvimentos,

05:19

inclusive. Então,

05:21

esse aí é um aspecto interessante para a gente.

05:26

Como que eu consigo ver o que foi feito? Eu vou pedir aqui para ele.

05:34

Seguinte, mate todos

05:36

os processos, eu

05:41

vou escrever aqui para ele subir o ambiente, né?

05:44

Suba, tuba novamente, o ambiente.

05:53

Então, ele está dando aqui, o Bashport NPM Rundev,

05:56

e ele subiu aqui o ambiente para mim.

06:00

Obviamente, eu poderia estar usando o próprio, sei lá,

06:04

o cursor que ele tem no navegador,

06:06

ou eu posso entrar no meu navegador e acessar e tudo mais,

06:11

isso aqui não seria, na realidade, o problema.

06:14

Posso chegar aqui e vamos ver como é que ficou

06:17

toda essa história aqui que ele acabou criando.

06:20

Então, foi isso aqui que ele criou aqui para mim.

06:24

Ou seja, Videomax MBA, Private Video Library, AI Transcription,

06:30

Turning every video you own into a searchable, readable archive.

06:36

Então, ele criou, utilizou lá o laranjão aqui do HubSpot, criou aqui o login,

06:43

criou o create account, explicou como é que funciona,

06:46

upload, transcribe e summarize.

06:49

Basicamente, é isso que ele criou de landing page.

06:51

Eu não estou preocupado muito com o design,

06:53

mas ele criou alguma coisa bem clean,

06:55

que é o que eu tinha pedido lá na especificação.

06:57

Se eu clicar em criar conta, o que vai acontecer? Não vai mandar para nenhum lugar.

07:02

E ele não vai mandar para nenhum lugar de propósito.

07:06

Simplesmente por quê? Porque nós não queríamos isso.

07:10

Mas ele deixou o Jarolink preparado para a próxima feature.

07:14

A mesma coisa acontece aqui para login.

07:18

Então, insights e pontos importantes.

07:22

Integração entre essas features. Então, a gente já fez a nossa primeira parte.

07:28

O que eu vou fazer agora é,

07:30

eu vou pedir para ele fazer o commit disso aqui para mim.

07:35

Gerar a pull request aqui para mim,

07:37

para a gente fazer o merge no branch main. Legal? Depois disso,

07:41

eu quero mostrar para vocês como é que funciona logicamente

07:45

essa parte onde faz uma

07:48

feature sair grudando na outra.

07:52

Isso aí é um ponto super, mas super importante mesmo para você conseguir entender.

07:58

Beleza? Então vamos voltar aqui para o nosso editor.

08:04

E agora, o que eu vou pedir para ele fazer, simplesmente,

08:07

comitar, né? Então, eu vou pedir aqui para ele dar um commit.

08:14

E, pessoal, não estou olhando qualidade de código nesse momento, tá?

08:17

Não é nem a minha intenção, nem de longe, fazer isso aqui nesse momento, tá?

08:21

E quando ele dá esse commit aqui para mim, é um comando, né?

08:24

É um plugin da Anthropic que ele entende o que foi mudado e ele cria já descrição,

08:28

utilizando diversos padrões aqui para mim. Então, ele criou esse commit aqui no...

08:34

nesse branch, f01 landing page, e se eu quiser eu posso dar um commit,

08:39

push pr, ou seja,

08:42

ele vai dar um push e vai criar a pull request ali para mim. Então,

08:46

vou dar um enter aqui, eu já poderia ter feito isso direto, na realidade.

08:51

E agora, vamos lá, vamos ver ele criando ali a nossa pull request,

08:56

que é o que a gente está querendo aqui nesse momento. Então, vamos lá.

09:03

E ele gerou aqui o link da nossa pull request agora aqui para mim.

09:08

Vou clicar para ele abrir o meu GitHub com a minha pull request aqui colocada, bonitinha aqui para mim.

09:15

Então, o que nós temos aqui na minha pull request?

09:20

Sumário, ou seja, foi adicionada uma landing page pública com todos aqueles aspectos.

09:25

O testing plan colocou o npm test, o build rodou,

09:30

ele fez um manual smoke test, ou seja, abrindo o browser.

09:35

Ele tem o cta barra register barra login.

09:38

E ele conseguiu renderizar, e o reviewer,

09:42

quem vai fazer a revisão desse pull request,

09:44

precisa verificar a identidade visual para ver se bate com

09:48

a forma minimalista do HubSpot como tinha sido pedido no PRD.

09:53

E aqui foi gerado como Cloud Code, aqui tem o commit, não tem nenhum conflito,

09:59

então posso dar um merge pull request, aqui para mim, vou dar um confirm merge, vou

10:06

aproveitar e já deletar o branch lá de cima,

10:09

E aqui a gente terminou a nossa primeira funcionalidade,

10:13

galera. Então, essa primeira funcionalidade nossa foi importante para a gente ter,

10:19

na realidade, a nossa landing page que ele acabou criando. Agora,

10:23

o mais importante que eu queria trazer aqui para vocês é que ele fez

10:29

Tudo baseado em uma especificação e essa especificação tem

10:33

uma ordem lógica até chegar no final do meu projeto.

10:38

Então, esse aí é o grande ponto.

10:41

Você gasta um tempo muito forte no início para que nesses

10:45

momentos você consiga fazer as coisas da forma mais assertiva possível.

10:49

Vai tudo funcionar de primeira? Não, não vai. Mas,

10:54

obviamente, grande parte do trabalho de decisões.

10:59

Uma coisa que eu gosto muito da parte de SDD é pelo fato

11:03

de quando você para para especificar no nível

11:05

de detalhes com entrevistas dessa forma,

11:07

como é colocado,

11:09

você começa a pegar muitos edge cases que a gente consegue trabalhar. Então,

11:15

agora que a gente tem essa parte aqui,

11:18

vou acabar esse vídeo e eu vou para a feature número 2 de autenticação.

11:24

Eu não vou ficar rodando aqui na sua frente

11:28

a geração da especificação dessa feature 2,

11:31

porque... Se não,

11:32

vai demorar um tempão. Então, enquanto ele vai rodar,

11:36

eu quero trazer algumas outras explicações ali para você. Vamos nessa.

## Resumo IA

**Abreviações**
*   **CLI**: Command Line Interface
*   **CTA**: Call To Action
*   **IA**: Inteligência Artificial
*   **IDE**: Integrated Development Environment
*   **MCP**: (Mencionado no contexto de uma forma mais complexa de uso do Playwright, mas sem definição explícita na aula)
*   **PR**: Pull Request
*   **PRD**: Product Requirements Document
*   **SDD**: Specification-Driven Development

**Resumo**
A aula abordou a implementação orientada por especificação em um projeto Next.js, enfatizando como ativar a skill correta e fornecer prompts explícitos para guiar a execução por um agente de IA. O objetivo é transformar especificações em código executável com o mínimo de ambiguidade, gerando valor não pela automação em si, mas pela aderência a restrições e guias predefinidas.

O fluxo inicia com a ativação de uma skill principal, como a "Next Best Practice", que garante a conformidade com as boas práticas do ecossistema Next.js. Durante a criação da feature (exemplo de uma landing page), o agente pode carregar skills complementares, como a Playwright CLI. Esta skill permite inspecionar a interface gerada em tempo de execução, abrindo um navegador, navegando pela aplicação, tirando screenshots e validando visualmente se o resultado atende aos critérios de aceitação, como layout e presença de seções. Isso reduz a dependência de análise estática de arquivos e a necessidade de acionar métodos mais pesados (como MCP) continuamente. A automação também demonstrou capacidade de lidar com o estado real da máquina, como conflitos de porta, subindo o servidor em uma porta disponível (ex: 3005) e continuando o processo.

A landing page foi considerada pronta mesmo sem navegação funcional para "/login" e "/register", pois os links foram preparados como "contratos de continuidade" para features futuras, alinhando-se ao princípio de SDD de entregar exatamente o que foi pedido sem completude prematura. Após a geração, a inspeção manual no navegador confirmou a estrutura, identidade visual e presença dos elementos essenciais (hero, CTA, footer) conforme o PRD.

O processo continua com o registro da mudança através de um commit, que é gerado de forma estruturada por ferramentas integradas (plugin da Anthropic), interpretando as alterações. Finalmente, uma Pull Request (PR) é criada, consolidando a entrega com um sumário, um plano de testes (npm test, build, smoke test manual) e pontos de atenção para o revisor (ex: aderência visual ao estilo minimalista do PRD). O instrutor ressalta que o maior ganho do fluxo é deslocar as decisões para antes da implementação, investindo em especificações detalhadas para antecipar edge cases e aumentar a assertividade da geração, garantindo consistência em features subsequentes.

**Pontos de atenção**
*   **Ativação Explícita da Skill**: A implementação orientada por especificação exige que a skill correta esteja ativa e seja explicitamente invocada no prompt para guiar o contexto da execução.
*   **Valor da Automação**: A automação deve seguir restrições e especificações predefinidas, e não ser apenas "automatizar por automatizar". O foco é a redução de ambiguidade e o alinhamento com o ecossistema e as boas práticas.
*   **Validação Dinâmica vs. Estática**: Não depender exclusivamente da leitura estática de arquivos. Utilizar ferramentas como Playwright CLI permite que a IA interaja com a aplicação em execução, capture evidências visuais (screenshots) e valide o resultado visualmente, crucial para critérios de aceitação ligados a layout e comportamento.
*   **Resiliência a Ambientes Reais**: A automação deve ser capaz de lidar com interferências e estados reais da máquina (ex: conflitos de porta), adaptando-se e continuando o processo sem falhar.
*   **Princípios de SDD**: Cada feature deve entregar exatamente o que foi especificado, deixando pontos de integração explícitos para features futuras. Evitar a "completude prematura" e focar em incrementos coerentes.
*   **Propósito da Validação Visual Inicial**: A checagem visual inicial serve para validar estrutura, identidade visual esperada e presença de elementos essenciais, não para refinamento estético. "Clean e aderente ao pedido" é mais importante do que polimento de design nesta fase para evitar retrabalho antes da hora.
*   **Qualidade dos Commits e PRs**: Utilizar ferramentas integradas para gerar mensagens de commit estruturadas e pull requests detalhadas (sumário, plano de teste, pontos de atenção para revisores) melhora a rastreabilidade e a segurança do merge.
*   **Investimento na Especificação**: O maior ganho do fluxo é o investimento inicial em especificações detalhadas (incluindo entrevistas e critérios de aceitação). Isso permite identificar edge cases cedo, aumenta a assertividade da geração e reduz interpretações arbitrárias do agente, garantindo consistência nas features subsequentes, mesmo que nem tudo funcione perfeitamente de primeira.