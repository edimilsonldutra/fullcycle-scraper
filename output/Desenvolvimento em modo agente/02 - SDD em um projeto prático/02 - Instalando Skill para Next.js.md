Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17780)

## Resumo da aula

Uma forma direta de acionar o agente é pedir a implementação com base nos artefatos já definidos, como @PRD e EN01. Nesse formato, o agente recebe um objetivo de alto nível e precisa inferir sozinho como organizar o trabalho. Isso reduz o esforço de especificação inicial, mas transfere para o agente a responsabilidade de decidir padrões, estrutura e abordagem de implementação.

Quando o objetivo é evitar uma execução totalmente aberta, vale adicionar guidance explícito por meio de uma skill. A skill Next Best Practice funciona como uma camada de orientação para projetos em Next.js, fornecendo boas práticas de desenvolvimento para o agente seguir durante a implementação. Retomando o uso do @PRD e da EN01, a diferença aqui é que a tarefa continua em linguagem natural, mas passa a ser executada com um conjunto técnico de referências mais consistente.

A skill pode ser encontrada no diretório ou catálogo skills.sh, onde aparece como uma skill criada pela Vercel. O nome exato da skill importa porque é ele que será referenciado na configuração ou no comando usado com o agente. Esse detalhe evita ambiguidade e garante que a orientação aplicada seja exatamente a de boas práticas para Next.js.

A instalação pode ser feita com npx, copiando o comando disponível e executando-o no terminal. Esse fluxo baixa o pacote e inicia um processo interativo para definir onde a skill será instalada. O uso de npx é conveniente porque dispensa instalação prévia permanente do utilitário e executa diretamente o pacote necessário.

Durante a instalação, a ferramenta pergunta se a skill deve ficar disponível apenas no projeto atual ou globalmente no ambiente do usuário. Instalar no projeto é útil quando a orientação precisa ficar restrita a um repositório específico; instalar globalmente faz sentido quando a mesma skill será reutilizada em vários projetos no mesmo computador. Essa escolha define o alcance da configuração e impacta a padronização do ambiente de desenvolvimento.

A opção de instalar como link simbólico evita copiar os mesmos arquivos para múltiplos locais. Em vez de duplicar conteúdo, o sistema cria uma referência para a origem da skill, o que reduz redundância e simplifica manutenção. Esse detalhe é especialmente útil quando a instalação é global e a skill pode ser compartilhada por vários projetos.

Ferramentas de agentes nem sempre seguem a mesma convenção de diretórios, e isso afeta a interoperabilidade das skills. O ponto levantado aqui é a diferença entre estruturas como .agents/skills e convenções específicas de ferramentas, como .claude. Quando o ecossistema adota padrões diferentes, a instalação e o reaproveitamento de configurações ficam menos uniformes.

Instalar a skill representa um guidance mínimo: o agente continua recebendo instruções em linguagem natural, mas agora com um apoio explícito de boas práticas de Next.js. Isso é um meio-termo entre deixar toda a inferência por conta do agente e usar uma automação mais rígida. O próximo nível de controle surge quando a implementação passa a usar uma skill específica com passos mais claros e mais direcionamento operacional.

## Transcrição

00:01

Bom, pessoal, então vamos nessa.

00:03

A gente parou onde nós estávamos mudando aqui o branch e a

00:08

nossa ideia agora aqui é fazer o que no final das contas?

00:12

Pedir para ele fazer essa implementação. Eu posso pedir de diversas formas, tá?

00:17

Uma das formas que eu posso simplesmente pedir é escrever dessa forma,

00:21

olha só. Baseado no arroba PRD e

00:26

nas...

00:30

vou colocar en01 aqui, que é na feature 01 de landing page,

00:37

faça a implementação.

00:40

Beleza? Ou seja,

00:42

essa é a forma mais simples de fazer com que

00:47

o meu agente enfira basicamente tudo de como ele vai trabalhar.

00:52

Por outro lado,

00:54

para não dizer que eu não estou dando guidance nenhum para o meu agente, de forma geral,

01:00

Eu vou fazer uma coisa aqui nesse momento, tá?

01:04

Eu vou fazer uma coisa bem simples aqui, que é o seguinte.

01:11

Eu vou,

01:14

no meu, aqui dentro, eu vou falar o seguinte.

01:18

Eu quero que ele utilize uma skill especificamente

01:21

de Next Best Practice ali pra gente, tá?

01:25

Eu tenho essa skill instalada no meu computador.

01:30

Mas eu vou mostrar aqui para vocês aonde esse cara está.

01:34

Então, se você for aqui no skills .sh, e

01:40

nesse skills .sh existe uma

01:43

skill criada ali pela Verso,

01:47

que é o nosso Next Best Practice.

01:52

Então, é basicamente o nome dessa skill que a gente vai colocar.

01:59

Somente para que você consiga ter uma ideia ali para a gente,

02:03

tá? Então, vai ser o nome dessa skill. Então, chama Next.

02:07

Deixa eu colocar aqui na busca. Next Best Practice. Se você ver,

02:13

é uma skill que já teve nessa semana,

02:17

pelo menos nesse momento, 66 mil instalações.

02:20

E ela traz as boas práticas de desenvolvimento com Next.js.

02:24

Para não dizer que eu não estou dando guidance. nenhuma aqui pro meu agente.

02:29

Como que eu instalo essa skill, tá? Você pode instalar via NPX,

02:34

você pode dar um copy aqui, tá?

02:36

Rode no seu terminal.

02:39

Então, deixa eu subir aqui meu terminal. Ela já tá instalada, mas eu vou rodar.

02:46

Daí ela fala, você deseja instalar esse pacote? Eu vou falar que sim.

02:52

Ele vai baixar e ele fala, você quer instalar na onde tanto? Então,

02:56

primeiro ele vai pegar todos os caras que normalmente são universais, porque tem...

03:00

.agents barra skills, ou seja, o Cloud é o único que usa .cloud,

03:05

se o Cloud usasse .agents, a gente não teria nenhum desses problemas,

03:09

mas tudo bem, a galera da Anthropic valeria a pena usar o .agents,

03:13

o .agents e em vez de cloud .md,

03:16

agents .md, mas eu quero usar o Cloud Code, e aqui ele fala,

03:21

se eu quero instalar essa skill no meu projeto,

03:26

ou que essa skill fique instalada de forma global

03:30

para todos os projetos que eu tenho no meu computador.

03:34

Então, basicamente,

03:35

Ele vai falar se eu quero instalar no escopo do usuário

03:38

ou ali para mim também no meu escopo global.

03:41

Nesse momento, eu vou colocar aqui que é no meu escopo global.

03:45

Vou pedir para ele fazer como link simbólico,

03:48

para ele não ficar duplicando os arquivos.

03:50

Quer prosseguir? Quero.

03:52

E prontinho, ele instalou aqui a minha skill. Então, esse aí é um ponto importante,

03:59

então instalar essa skill vai ser pelo menos o mínimo de

04:03

guidance que eu vou dar aqui para o meu agente,

04:06

inicialmente escrevendo de forma em linguagem natural,

04:10

sem nenhuma skill ou comando pedindo para ele fazer a implementação.

04:15

Depois eu vou mostrar para vocês uma skill de implementação

04:18

que tem alguns passos um pouco mais claros,

04:21

dando mais guidance ali inclusive para o agente, beleza?

04:25

Vamos botar esse negócio para rodar aí no próximo vídeo.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirement Document (Documento de Requisitos de Produto)
*   **EN01**: Especificação/Feature Número 01 (referente a uma funcionalidade de landing page)
*   **Next.js**: Uma estrutura de desenvolvimento web (framework) baseada em React.
*   **npx**: Uma ferramenta para executar pacotes Node.js sem a necessidade de instalá-los globalmente.

**Resumo**
A aula teve como objetivo principal demonstrar como acionar um agente para realizar implementações de software, abordando diferentes níveis de orientação. Inicialmente, o instrutor explicou uma abordagem direta, onde o agente recebe um objetivo de alto nível e artefatos predefinidos como um `@PRD` e a `EN01` (Especificação/Feature Número 01, referente a uma landing page). Neste cenário, o agente infere sozinho a organização do trabalho, padrões, estrutura e abordagem de implementação, reduzindo o esforço de especificação inicial.

Para evitar uma execução completamente aberta e fornecer alguma orientação, foi apresentada a utilização de "skills". A skill `Next Best Practice`, desenvolvida pela Vercel e disponível no catálogo `skills.sh`, funciona como uma camada de direcionamento, fornecendo boas práticas de desenvolvimento para projetos em Next.js. Com ela, a tarefa para o agente continua sendo em linguagem natural, mas é executada com um conjunto técnico de referências mais consistente.

O processo de instalação da skill foi detalhado: ela é baixada e instalada via `npx` no terminal, que executa o pacote diretamente sem necessidade de instalação permanente prévia do utilitário. Durante a instalação, o usuário pode escolher se a skill será disponibilizada apenas no projeto atual ou globalmente para todos os projetos no ambiente. Foi destacado também a opção de instalar como link simbólico, o que evita a duplicação de arquivos e simplifica a manutenção. A instalação dessa skill representa um "guidance mínimo", servindo como um meio-termo entre a inferência total do agente e uma automação mais rígida. O instrutor mencionou que um controle ainda maior poderia ser alcançado com skills de implementação com passos mais claros e direcionamento operacional explícito.

**Pontos de atenção**
*   **Responsabilidade da Inferência:** Ao dar um objetivo de alto nível sem guidance explícito, o agente assume a responsabilidade total de decidir padrões, estrutura e abordagem de implementação, o que pode não estar alinhado com as expectativas do desenvolvedor.
*   **Nome Exato da Skill:** Ao referenciar uma skill, o nome exato (e.g., `Next Best Practice`) é crucial para evitar ambiguidades e garantir que a orientação correta seja aplicada.
*   **Escopo de Instalação:** A escolha de instalar uma skill no projeto atual ou globalmente deve ser consciente, pois afeta o alcance da configuração e a padronização do ambiente de desenvolvimento.
*   **Uso de Link Simbólico:** Para instalações globais, utilizar a opção de link simbólico é uma boa prática que evita a duplicação de arquivos, reduzindo redundância e simplificando a manutenção da skill.
*   **Inconsistência de Diretórios:** Ferramentas de agentes podem usar diferentes convenções de diretórios (e.g., `.agents/skills` vs. `.claude`), o que pode dificultar a interoperabilidade e o reaproveitamento uniforme de configurações entre ecossistemas.
*   **Níveis de Orientação:** A instalação de uma skill como `Next Best Practice` fornece um guidance mínimo. Para maior controle e direcionamento operacional, é necessário o uso de skills mais específicas com passos e comandos detalhados.