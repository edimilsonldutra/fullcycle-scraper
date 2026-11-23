Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17971)

## Resumo da aula

Os gates já definidos anteriormente ganham aqui uma aplicação mais operacional no back-end: além de validar arquitetura com ferramentas como Dependency Cruiser, ESLint e Knip, eles também controlam o ambiente de execução. Isso evita que o projeto dependa de configuração manual sempre que um agente ou desenvolvedor inicia o sistema. O valor não está apenas em “rodar checks”, mas em transformar expectativas do projeto em regras executáveis. Quando essas regras falham, o próprio fluxo barra desvios da estrutura esperada.

A criação desses scripts não exige domínio profundo de cada biblioteca, desde que a estrutura desejada esteja clara. O ponto central é fornecer à IA um boilerplate funcional, com imports, pastas e convenções já definidos, para que ela derive configurações coerentes com esse padrão. Retomando o scaffolding e a skill já estabelecidos, o agente passa a produzir gates e scripts de suporte em vez de depender de escrita manual do zero. O trabalho humano fica concentrado em revisar, iterar e ajustar até que as regras reflitam o comportamento esperado.

Um script de init não serve apenas para “subir o projeto”; ele detecta dependências disponíveis e escolhe a estratégia adequada para inicialização. Se houver Postgres instalado no ambiente, o fluxo pode usar essa instância; se não houver, o script tenta recorrer ao Docker Compose, desde que ele exista. Isso permite que o mesmo projeto funcione tanto na máquina local quanto em ambientes de cloud com restrições diferentes. A inicialização deixa de ser uma sequência informal de passos e passa a ser uma política automatizada.

Ambientes diferentes exigem decisões diferentes, e o script precisa incorporar essa variação explicitamente. Em uma plataforma cloud, pode não existir Docker, mas já haver um Postgres disponível; na máquina local, o caminho preferido pode ser um container gerenciado por Docker Compose. Essa lógica condicional reduz atrito operacional e evita que o setup dependa de instruções paralelas fora do código. O script vira uma camada de compatibilidade entre o projeto e o ambiente onde ele roda.

Retomando o uso de worktrees já mencionado antes, o isolamento agora aparece como regra automatizada de infraestrutura local. Quando cada Worktree recebe seu próprio banco de dados, execuções paralelas deixam de competir pelo mesmo estado persistido. Isso é especialmente importante quando múltiplos agentes ou branches estão ativos ao mesmo tempo, porque elimina interferência cruzada entre testes, migrations e dados temporários. O gate operacional protege o fluxo antes que o conflito aconteça.

Portas também precisam ser tratadas como recurso concorrente. Se o projeto detectar que a porta prevista já está em uso, o script pode selecionar a próxima porta disponível em vez de falhar ou exigir intervenção manual. Esse comportamento é simples, mas muda bastante a experiência de desenvolvimento paralelo, porque reduz colisões entre instâncias locais do mesmo sistema. Em harnesses com múltiplas execuções automatizadas, essa verificação deixa de ser conveniência e passa a ser requisito de estabilidade.

Esses scripts não saem prontos de uma receita universal, porque cada projeto tem estrutura, restrições e prioridades próprias. O processo correto é iterativo: definir o padrão desejado, gerar regras com ajuda da IA, testar, observar onde o fluxo falha e refinar. Por isso, a pergunta relevante não é “qual é o script certo?”, mas “qual comportamento operacional o projeto precisa garantir?”. A partir dessa clareza, os gates deixam de ser genéricos e passam a refletir a realidade do codebase.

Shell script é apenas uma opção de implementação, não uma exigência arquitetural. Se a equipe tiver mais domínio de TypeScript ou outra linguagem, os mesmos gates podem ser implementados ali, desde que preservem automação, verificações e previsibilidade. O critério de escolha deve ser manutenção e integração com o restante do projeto, não preferência pessoal isolada. O que importa é ter scripts que inicializem o ambiente e controlem concorrência de forma confiável.

## Transcrição

00:00

Bom pessoal, no vídeo anterior eu dei uma visão geral dos gates que a gente vai utilizar,

00:05

e novamente, eu estou focando muito, mas muito mais mesmo no quê?

00:10

Na parte do back-end do que na parte do front-end aqui nesse projeto,

00:15

principalmente por conta da skill que eu criei.

00:18

E grande parte desses gates você vai ver aqui no lado do back-end,

00:22

senão a gente iria deixar esse projeto gigante de todos os aspectos.

00:26

Mas se você olhar aqui, tá?

00:28

Você vai perceber que eu tenho o Prisma,

00:32

onde tem ali a pasta do Prisma, tem a pasta ali de scripts,

00:35

e depois a gente entra ali com a parte do DepCruise,

00:41

né? O Dependency Cruiser,

00:43

você vai ver que a gente tem o S-Link configurado,

00:46

você vai ver que a gente tem o NIP, você vai ter...

00:50

uma pancada de script no final das contas que vão ajudar a gente

00:55

a conseguir executar um determinado script pra

00:59

sair fazendo a verificação da nossa arquitetura,

01:03

tá? Então, como que eu criei todas essas coisas?

01:07

E novamente, pessoal, eu não sou o mago do TypeScript,

01:11

eu não sou o mago que entende de todos os detalhes de todas essas bibliotecas,

01:17

tá? Mas o que eu tenho?

01:19

Eu tenho a IA do meu lado, eu tenho um modo de planejamento, eu tenho o Grilled Me,

01:25

e obviamente eu tenho o conhecimento, obviamente, de TypeScript também.

01:30

Mas o que eu estou querendo dizer é que,

01:32

a partir de hoje, você não precisa também ficar somente preso ao que você sabe.

01:38

Você vai pedir para a IA criar os seus gates,

01:41

fazer essas configurações para você. Você vai revisar,

01:44

mas aos poucos você vai começar a perceber que essa criação dos gates,

01:49

essas gerações desses scripts de init,

01:52

de stop, de limpar banco de dados,

01:55

de evitar conflito de porta, todos esses tipos de detalhes,

01:59

não vai você que vai desenvolver. Vai ser o seu próprio agente. E é por isso que...

02:05

Eu super recomendo que você trabalhe com scaffolding e coisas desse tipo,

02:09

porque nos próximos projetos que você vai tendo,

02:12

você já vai reutilizando e sempre melhorando essa sua skill,

02:16

que ela vai te ajudar. Com determinados tipos de projeto,

02:20

tá? Então, essa que é a, como que eu posso dizer, a ideia principal, né,

02:24

que eu levo principalmente na hora que eu estou desenvolvendo, tá? Então,

02:28

você vai ver que ele já inicia ali com env.example,

02:32

mas eu tenho um slint configurado, eu tenho um NIP configurado,

02:36

perceba que ele já está olhando as pastas,

02:39

né, que eu preciso ter, né? Então, a gente começa a olhar aqui...

02:45

diversos padrões que ele começa a buscar, olha só o Dependency Cruiser,

02:50

com vários padrões, simplesmente por quê?

02:53

Porque eu quero que ele siga esse cara. E como que eu fiz para ele seguir?

02:58

Eu coloquei o meu boilerplate, a estrutura, o meu hello world que eu queria,

03:03

e pedi para ele criar essas configurações baseado naqueles imports,

03:09

naquela estrutura que eu acabei trabalhando.

03:11

Se ele fizer algo diferente, ele vai barrando. Então,

03:13

isso é um trabalho entre astros e formiguinha.

03:16

Depois, um dia, se você quiser seguir esse padrão que eu estou utilizando aqui,

03:19

Você vai fazer o download lá no GitHub e você vai

03:22

poder utilizar e ver como é que foi feito, tá?

03:24

Mas se você perceber, basicamente,

03:27

ele vai criando várias regras e eu fui iterando até facilitar a minha vida,

03:33

até eu ver que isso está aceitável, tá? Então,

03:37

um ponto importante que eu quero que você esteja muito claro é Wesley,

03:42

de onde você tirou esses scripts? Por que estão assim?

03:45

De onde veio? Você está cuspindo código? Não.

03:49

Cada projeto, cada desenvolvedor tem uma necessidade, tem uma estrutura diferente.

03:54

O importante é você conseguir ter clareza do que você quer,

03:58

porque o restante, principalmente nesses scripts de controle,

04:02

a IA vai te ajudar. Por exemplo, o script de inicialização.

04:07

Basicamente, esse cara vai iniciar meu banco de dados,

04:10

ele vai verificar se o Docker Compose existe.

04:13

Tem diversas manhas aqui que eu acabei colocando e melhorando

04:17

ao longo do tempo para facilitar um pouco a minha vida.

04:20

Vou dar um exemplo aqui para você.

04:22

Quando eu dou um init, ele busca se eu tenho um Postgres instalado na minha máquina.

04:27

Se eu não tiver, ele vai e busca o Docker Compose.

04:31

Se ele não tiver, ele vai fazendo isso. Por quê?

04:33

Porque às vezes eu quero testar esse script na web,

04:36

usando dentro da plataforma da cloud, e eles não têm Docker lá dentro.

04:41

Mas eles já têm um Postgres instalado. Então, nesse caso, o que eu acabo fazendo?

04:46

Eu utilizo um Postgres local lá. Mas na minha máquina,

04:49

eu utilizo o Docker Compose com o Postgres ali.

04:52

Por exemplo, se eu vou trabalhar em diversos branches,

04:56

eu não quero que um banco de dados atrapalhe,

05:00

quer dizer... Uma execução atrapalha outra,

05:04

então eu quero que eles trabalhem em bancos de dados separados.

05:06

Então, a regra que eu crio é, toda vez que eu tiver uma WorkTree diferente,

05:10

ele vai criar um banco de dados diferente.

05:13

Mesma coisa com portas. Ele vai verificar qual porta está rodando aquele projeto.

05:19

Se aquele projeto estiver rodando uma porta que já está criada,

05:23

o que ele vai fazer? Vai pegar uma próxima porta. Então,

05:26

esses detalhes vão fazer muita diferença para você.

05:32

Quando você estiver trabalhando em forma paralela,

05:34

principalmente porque você vai começar a ter problema de porta,

05:37

você vai começar a ter problema de concorrência com banco de dados,

05:41

esses tipos de coisa, tá?

05:42

Então, depois você analisa com calma, perceba aqui que eu resolvo,

05:46

verifico se está no branch main,

05:48

como é que vai funcionar e etc, um monte de rejeições,

05:51

quem fez isso foi a IA, basicamente foi isso, tá? Então...

05:56

A gente tem que ficar sempre muito ligado nesses tipos de scripts,

06:00

nessas coisas, porque isso aí vai facilitar o desenvolvimento,

06:04

mas você não precisa ficar, ó, eu não sei fazer alguma coisa. Cara, pega a IA,

06:09

pede pra ela fazer code review, pega o seu par, dá uma olhada,

06:13

sempre tem um cara muito bom na sua empresa que manja de shell script,

06:16

ou você não precisa fazer isso em shell script,

06:18

você pode fazer na linguagem que você quiser.

06:20

Você pode fazer utilizando o TypeScript, não interessa.

06:22

O grande ponto é que você tenha esses scripts

06:25

que vão ajudar você a fazer a inicialização,

06:28

que vão ajudar a você a ter esses gates de controle,

06:31

porque... Um script simples de inicialização,

06:34

ele tem que conseguir fazer parte de uma espécie de um gate

06:38

para evitar concorrências com outras execuções de agentes que vão rodar em paralelo.

06:44

Beleza? Então, fiquem ligados,

06:46

vocês vão poder baixar esse repositório e tudo mais,

06:50

mas é importante você ter essa clareza sobre esses gates,

06:54

porque fazem muita diferença e é uma das coisas principais que

06:59

você tem ali na hora que você está customizando o seu harness.

## Resumo IA

**Abreviações**

*   **DepCruise**: Dependency Cruiser
*   **ESLint**: Uma ferramenta de linting para identificar e relatar padrões de código problemáticos em JavaScript e TypeScript.
*   **IA**: Inteligência Artificial
*   **Knip**: Uma ferramenta para encontrar arquivos e dependências não utilizadas em projetos JavaScript e TypeScript.
*   **Postgres**: PostgreSQL, um sistema de gerenciamento de banco de dados relacional.
*   **Worktree**: Um recurso do Git que permite ter múltiplos diretórios de trabalho conectados a um único repositório, cada um com um branch diferente, facilitando o desenvolvimento paralelo isolado.
*   **Docker Compose**: Uma ferramenta para definir e executar aplicativos Docker de múltiplos contêineres, orquestrando-os através de um único arquivo de configuração.

**Resumo**

Esta aula aborda a aplicação operacional de "gates" no back-end, visando validar a arquitetura e controlar o ambiente de execução. O objetivo central é transformar as expectativas e padrões do projeto em regras executáveis, utilizando ferramentas como Dependency Cruiser, ESLint e Knip para garantir a conformidade arquitetural e evitar a dependência de configurações manuais.

O processo de criação desses scripts é predominantemente guiado por Inteligência Artificial (IA), mas de forma iterativa e com supervisão humana. O instrutor destaca a importância de fornecer à IA um "boilerplate" funcional — com imports, estruturas de pastas e convenções já estabelecidas — para que ela possa gerar configurações e scripts coerentes com o padrão desejado. O papel do desenvolvedor se concentra em revisar, iterar e ajustar as saídas da IA até que as regras reflitam o comportamento operacional esperado. Essa metodologia, combinada com scaffolding e a reutilização de "skills" (conjuntos de regras ou configurações) já estabelecidas, permite que agentes de IA produzam gates e scripts de suporte, minimizando a necessidade de escrita manual do zero.

A aula detalha a funcionalidade de scripts de inicialização inteligentes, que atuam como uma camada de compatibilidade entre o projeto e diversos ambientes. Esses scripts não apenas iniciam o sistema, mas também detectam dependências disponíveis (como uma instância local de Postgres ou Docker Compose) e adaptam a estratégia de inicialização, permitindo que o projeto funcione tanto em máquinas locais quanto em plataformas de cloud com restrições variadas.

Além disso, é enfatizada a importância do isolamento de ambientes e do gerenciamento de recursos concorrentes. A utilização de Worktrees do Git para criar bancos de dados dedicados por ambiente garante que execuções paralelas (de diferentes branches ou agentes) não interfiram umas nas outras. Da mesma forma, os scripts são configurados para detectar portas em uso e selecionar automaticamente a próxima disponível, prevenindo colisões e aprimorando a experiência de desenvolvimento e de testes automatizados paralelos. A escolha da linguagem de implementação para esses scripts (Shell, TypeScript, etc.) deve ser baseada na facilidade de manutenção e integração com o projeto, priorizando a automação e a previsibilidade.

**Pontos de atenção**

*   **Evite Dependência de Configuração Manual**: A configuração manual do ambiente introduz atrito operacional e inconsistências, tornando o projeto dependente de agentes ou desenvolvedores específicos. Automatize com scripts para garantir consistência.
*   **Transforme Expectativas em Regras Executáveis**: O verdadeiro valor dos gates está em converter requisitos e padrões arquiteturais em regras operacionais que, ao falharem, previnem desvios da estrutura esperada.
*   **Guie a IA com um Boilerplate Sólido**: Ao utilizar IA para gerar configurações e scripts, forneça um "boilerplate" funcional e claro (com imports, pastas e convenções definidas) para que as saídas sejam coerentes com o padrão do projeto.
*   **Foco Humano na Revisão e Refinamento**: O trabalho do desenvolvedor deve se concentrar em revisar, iterar e ajustar as regras geradas pela IA até que elas reflitam o comportamento operacional desejado, em vez de escrever tudo do zero.
*   **Adaptação Inteligente ao Ambiente**: Scripts de inicialização devem ser capazes de detectar dependências disponíveis (e.g., Postgres local vs. Docker Compose) e adaptar a estratégia de execução para diferentes ambientes (local, cloud), atuando como uma camada de compatibilidade.
*   **Isolamento de Bancos de Dados por Worktree**: Utilize Worktrees do Git para isolar ambientes de trabalho, criando bancos de dados dedicados para cada um. Isso elimina interferência cruzada entre testes, migrations e dados temporários em execuções paralelas.
*   **Gerenciamento Dinâmico de Portas**: Implemente lógica nos scripts para detectar portas em uso e selecionar automaticamente a próxima porta disponível. Isso previne colisões em desenvolvimento paralelo e em cenários de execução automatizada com múltiplas instâncias.
*   **Processo Iterativo de Criação de Gates**: A construção de gates é iterativa: defina o padrão desejado, gere regras com IA, teste, observe onde o fluxo falha e refine. A pergunta chave é "qual comportamento operacional o projeto precisa garantir?".
*   **Escolha da Linguagem para Scripts**: Selecione a linguagem de implementação dos scripts (Shell, TypeScript, etc.) com base na facilidade de manutenção da equipe e na integração com o restante do projeto, não em preferência pessoal. A prioridade é a automação e a previsibilidade.
*   **Reutilização através de Scaffolding e Skills**: Invista em scaffolding e aprimore a "skill" (o conhecimento ou conjunto de regras) para gerar scripts com IA. Isso permite reutilizar e melhorar os gates em projetos futuros, economizando tempo e garantindo consistência.
*   **Prevenção de Conflitos**: Os gates operacionais devem ser projetados para proteger o fluxo de trabalho *antes* que conflitos (de concorrência, portas, etc.) ocorram, garantindo a estabilidade e a previsibilidade do desenvolvimento.