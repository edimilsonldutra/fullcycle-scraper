Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17969)

## Resumo da aula

AGENTS.md e CLAUDE.md funcionam como arquivos de instrução para ferramentas diferentes, por isso é comum manter os dois sincronizados com link simbólico. Retomando a ideia de skill e contexto explícito já estabelecida, aqui o ponto novo é a compatibilidade operacional entre harnesses: Codex e outras ferramentas tendem a ler AGENTS.md, enquanto Claude usa CLAUDE.md. Manter ambos alinhados evita divergência de comportamento entre agentes. O arquivo não nasce definitivo; ele começa com uma base útil e evolui junto com o projeto.

O scaffolding pode entregar um AGENTS.md inicial já preenchido com instruções práticas do projeto. Esse conteúdo não deve ser tratado como versão final, mas como uma baseline operacional que reduz trabalho manual e já orienta o agente desde o primeiro ciclo. Em vez de começar com um arquivo vazio, o projeto passa a expor comandos, convenções e restrições logo no bootstrap. Isso acelera a execução e diminui inferência desnecessária.

Uma seção de environment documenta como iniciar, parar e limpar o ambiente por meio de scripts como init.sh e stop.sh. Isso transforma operações recorrentes em comandos explícitos, o que reduz erro operacional do agente e padroniza a forma de subir a aplicação. Quando o arquivo também informa como encerrar processos e regenerar estado local, ele deixa claro como voltar o projeto para uma condição conhecida. Esse tipo de instrução é especialmente valioso em fluxos automatizados.

Retomando a skill de back-end já definida anteriormente, o AGENTS.md deve instruir o agente a reutilizar os linters e self-audit gates já providos por ela, em vez de criar validações paralelas. A razão é simples: múltiplos scripts de autovalidação tendem a fragmentar o critério de qualidade e gerar redundância. Centralizar os gates preserva consistência entre geração, revisão e execução. O arquivo, portanto, não apenas descreve regras; ele limita a liberdade do agente onde a padronização é estratégica.

Quality Gates são instruções que orientam a IA a verificar se a implementação respeita exatamente as regras do projeto. Aqui o foco não é redefinir gates em geral, mas registrar no AGENTS.md que a validação deve acontecer de forma intencional e alinhada às convenções já estabelecidas. Isso cria um ciclo em que o agente implementa, valida e corrige usando critérios explícitos. Sem esse direcionamento, ele pode improvisar verificações inadequadas ou incompletas.

O AGENTS.md pode consolidar regras como limite de 400 linhas por arquivo, adesão a SOLID e aplicação estrita de responsabilidade única. Essas convenções deixam de ser apenas preferência humana e passam a ser restrições operacionais para o agente. A orientação sobre nomes fáceis de localizar, associada a buscas simples no codebase, também melhora manutenção e descoberta de arquivos. O efeito prático é tornar o projeto mais navegável tanto para pessoas quanto para ferramentas automatizadas.

Para navegação automatizada no front-end, a instrução específica é usar Playwright CLI, não a integração padrão com Playwright nem fluxos baseados em MCP. Essa distinção importa porque a ferramenta escolhida afeta velocidade de execução e o tipo de artefato que o agente tende a gerar. Ao proibir criação de arquivos E2E e pastas dedicadas nesse contexto, o AGENTS.md evita que o agente derive para uma estratégia de teste diferente da desejada. A redundância na regra é deliberada quando o modelo insiste em um caminho incorreto.

Cada nova função deve vir acompanhada de teste, e bugs devem gerar testes específicos de regressão com mocks externos quando necessário. As propriedades citadas — independente, repeatable, self-validating e timely — definem um teste confiável para automação contínua. O AGENTS.md transforma esses critérios em expectativa explícita de entrega, não em recomendação opcional. Isso força o agente a produzir código verificável desde a origem.

O arquivo também pode registrar a topologia do monorepo, com apps/web para Next.js 16 e apps/backend para o back-end, cada um com seu próprio package.json. Retomando a estrutura de projeto já discutida em aulas irmãs, o avanço aqui é explicitar essa organização dentro do contexto consumido pelo agente. Quando a ferramenta sabe onde cada aplicação vive e onde estão seus manifests, ela reduz erros de execução no diretório errado. Um package.json adicional na raiz pode atuar como agregador do workspace.

Criar um banco de dados por branch evita que mudanças de uma linha de trabalho contaminem outra. Essa regra se torna especialmente útil ao usar worktree, porque múltiplas branches podem coexistir localmente com contextos independentes. Ao registrar isso no AGENTS.md, o agente passa a tratar isolamento de dados como requisito operacional. O ganho é previsibilidade durante desenvolvimento paralelo.

Uma observação com link de documentação do Next.js 16 ajuda o agente a não aplicar suposições herdadas de versões anteriores. Esse tipo de comentário é temporário, mas útil enquanto o ecossistema ainda está consolidando padrões e o modelo ainda confunde APIs ou comportamentos antigos. Em vez de explicar Next.js do zero, o arquivo aponta a fonte correta quando houver dúvida relevante. O resultado é menos erro por conhecimento desatualizado.

O AGENTS.md inicial é apenas a base operacional do projeto. À medida que o time identifica comportamentos recorrentes do agente, novas instruções podem ser adicionadas para corrigir desvios, reforçar padrões e capturar decisões arquiteturais. O valor do arquivo está justamente nessa evolução incremental. Ele começa com o scaffolding, mas amadurece com o uso real.

## Transcrição

00:00

Bom, pessoal, agora que a gente tem o esqueleto da nossa aplicação,

00:05

eu quero falar sobre um dos aspectos mais do que importantes que a gente não

00:10

pode ignorar e que isso engloba muito quando a gente está falando de Harness,

00:15

que a gente já cansou de ouvir falar, mas a gente tem que voltar nesse cara,

00:19

que é o Agents.md e o Cloud.md.

00:22

Uma coisa que normalmente eu estou acostumado a fazer é ou eu crio o Agents.md...

00:28

e depois vou e crio um link simbólico para o Cloud.md, e vice-versa.

00:33

Mesma coisa aqui com o diretório agents.md e o cloud.md,

00:37

porque isso, se você for usar o Codex,

00:39

se você for usar outras plataformas, outros Harness para programar,

00:43

normalmente esses caras vão usar o agents.md. Então,

00:47

basicamente, é o Cloud que utiliza o cloud.md,

00:50

então a gente tem que conseguir conviver com isso,

00:53

beleza? Agora, o negócio é o seguinte. Se eu for aqui nesse meu agent.md,

00:58

você vai ver que eu não tenho esse cara em branco.

01:01

Ele já veio meio que assim na hora que eu fiz aquele processo de scaffolding.

01:06

Isso significa que ele está perfeito? Não.

01:08

Esse cara vai ser modificado ao longo do tempo.

01:11

Porém, ele traz algumas coisas para a gente aqui que são importantes.

01:15

Por exemplo, environment. Como que eu inicio o ambiente? init.sh.

01:20

Como que eu paro o ambiente? stop.sh.

01:22

Como que eu paro todos os processos e gero o local state dele?

01:27

Ou seja, ele limpa, acaba limpando tudo. Então, esse tipo de coisa,

01:33

ele vai sempre ajudar. Ou seja, back-end development.

01:37

Use sempre a clean architecture skill para o desenvolvimento de back-end.

01:43

Use linters e self-audit gates que são providos,

01:48

provided by the... da Clean Architecture Skill,

01:52

não crie seus próprios linters ou self-audit gates.

01:56

Por que eu estou falando isso? Muitas vezes a aplicação vai se auto-validar,

01:59

a gente vai falar bastante ainda sobre gates, e isso é uma das coisas importantes,

02:04

porque senão você pode tender a sair criando scripts de auto-validação.

02:10

E a nossa ideia é a gente fazer isso... de propósito, vamos dizer assim, tá?

02:15

E aqui a gente tem a parte de Quality Gates, eu vou gravar um vídeo só sobre isso,

02:19

mas basicamente é como que eu faço para a IA validar para

02:23

ver se ela está seguindo exatamente as regras que eu estou querendo.

02:26

Isso aqui é uma das coisas mais importantes.

02:29

Estilo de código, arquivos com menos de 400 linhas,

02:32

seguir o SOLID, Single Responsibility Principle,

02:34

se você tiver mais de uma responsabilidade em um arquivo, crie outro arquivo, né?

02:39

Você vai preferir nomes...

02:43

para fazer a busca na hora de criar os arquivos,

02:45

com grep menor que 5 para facilitar a busca no codebase.

02:50

Teste de front-end,

02:51

utilizar o Playwright CLI para qualquer tipo de navegação de teste.

02:55

Então você vai ter que carregar a skill do

02:58

Playwright CLI e não usar o Playwright normal,

03:02

não crie e também para ele não criar

03:06

arquivos E2E e nem pastas para fazer esses testes com Playwright.

03:10

Pode ver aqui que está bem redundante,

03:12

porque às vezes ele cisma em usar o Playwright normal. Eu, particularmente,

03:16

Pelo menos no momento que eu uso esse vídeo, estou gravando esse vídeo, para mim,

03:20

Eu utilizo o Playwright CLI,

03:21

Ele é muito mais rápido do que usar o Playwright com MCP.

03:25

Outras coisas aqui, teste de backend, ou seja, cada nova função...

03:30

Criar um teste para bugs, criar e fazer mocks externos.

03:34

O teste tem que ser independente, repeatable, self-validating e timely.

03:39

E aqui pontos importantes. Estou dizendo que é um monorepo,

03:42

E onde eu tenho apps / web,

03:45

Vai ter o meu Next.js 16, apps / backend, vai ter o meu backend,

03:50

E eu vou ter um package.json para cada aplicação.

03:54

Então, se você for olhar aqui o ponto, o meu apps backend, eu tenho um package.json,

04:00

E se eu tenho o web,

04:03

Eu tenho também o meu package.json e provavelmente depois

04:07

Ele tem um package.json que engloba os dois,

04:11

Trabalhando ali como namespace. E vai utilizar por padrão o Postgres,

04:16

Que já está instalado nesse meu caso.

04:18

Se ele não está instalado para você, você deixa rodando. Nesse caso,

04:21

Eu não estou usando o Docker no projeto como um todo,

04:23

Mas o meu Postgres está utilizando...

04:28

Docker, né? Então, eu subi o Postgres utilizando o Docker aqui pra mim.

04:31

Uma coisa que eu coloquei é,

04:33

Crie um novo banco de dados para cada branch de trabalho,

04:36

Porque se eu tiver com branches diferentes,

04:38

Eu não quero que ele mexa no banco de dados do branch que eu estou trabalhando.

04:42

Isso vai ajudar muito para eu trabalhar com o worktree,

04:44

Né? E login, né? Para como ele vai trabalhar com a parte de log,

04:48

Para ele colocar como plaintext, etc.

04:51

Uma coisa que eu estou deixando ultimamente, tá?

04:54

É um comentário que está vindo meio que de graça

04:57

Quando você instala o esqueleto do Next.js 16.

05:00

Ele fala, esse não é o Next.js que você conhece,

05:03

Então, qualquer coisa relevante ao Next,

05:05

Olhe essa documentação aqui, tá? Eu estou deixando isso por enquanto.

05:09

Isso está ajudando bastante em relação a ele programar e utilizar melhor o Next 16,

05:15

Porque às vezes ele ficava se confundindo com coisas do Next anterior.

05:19

Logo, logo, provavelmente,

05:20

Você não precisa mais disso, porque ele já vai estar bem treinado com o Next 16,

05:23

Mas eu reduzi bastante os meus problemas ali com o Next, tá? Então, de forma geral,

05:29

Isso aqui é o que está vindo. Vamos dizer aqui, de graça,

05:33

Na hora que eu criei o esqueleto da minha aplicação. Ou seja,

05:38

Isso aqui é a base e a gente vai mudar e

05:42

A gente vai melhorar isso ao longo do tempo,

05:44

Com certeza. Inclusive, logo, logo,

05:46

A gente já vai começar a colocar novas instruções nesse cara aqui.

05:49

Fechou? Então, vamos nessa.

## Resumo IA

**Abreviações**

*   **AGENTS.md**: Arquivo de instrução para agentes de desenvolvimento de software (ex: Codex e outras ferramentas).
*   **CLAUDE.md**: Arquivo de instrução específico para o harness Claude.
*   **init.sh**: Script shell para iniciar o ambiente de desenvolvimento.
*   **stop.sh**: Script shell para parar o ambiente de desenvolvimento.
*   **SOLID**: Princípios de design de software (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion).
*   **CLI**: Command Line Interface (Interface de Linha de Comando).
*   **E2E**: End-to-End (Testes de ponta a ponta).
*   **MCP**: Mencionado como uma integração do Playwright, mas sem detalhamento específico sobre o acrônimo.
*   **IA**: Inteligência Artificial.
*   **package.json**: Arquivo de manifesto de projetos JavaScript/Node.js, descrevendo dependências e scripts.
*   **Postgres**: Abreviação de PostgreSQL, um sistema de gerenciamento de banco de dados relacional.
*   **Next.js**: Framework React para desenvolvimento web full-stack.
*   **worktree**: Funcionalidade do Git que permite ter múltiplas branches de trabalho de um repositório em diferentes diretórios simultaneamente.
*   **API**: Application Programming Interface (Interface de Programação de Aplicações).
*   **grep**: Comando Unix para buscar padrões em arquivos.

**Resumo**

A aula aborda a importância e a evolução dos arquivos de instrução `AGENTS.md` e `CLAUDE.md` no desenvolvimento de software assistido por agentes de IA. O objetivo principal é guiar essas ferramentas de IA, como Codex e Claude, para que sigam padrões, convenções e restrições específicas do projeto, garantindo consistência e eficiência.

Esses arquivos atuam como uma fonte de verdade para os agentes, sendo crucial mantê-los sincronizados (com links simbólicos, por exemplo), pois diferentes harnesses (ferramentas que orquestram a IA) leem arquivos distintos (`AGENTS.md` para Codex, `CLAUDE.md` para Claude). O processo de scaffolding pode iniciar o projeto com um `AGENTS.md` já preenchido, fornecendo uma baseline operacional que reduz o trabalho manual e orienta o agente desde o primeiro ciclo, expondo comandos, convenções e restrições.

O fluxo de instruções inclui:
1.  **Configuração de Ambiente**: Uma seção dedicada a scripts como `init.sh` e `stop.sh` para iniciar, parar e limpar o ambiente, padronizando operações e reduzindo erros.
2.  **Desenvolvimento Back-end**: O agente é instruído a reutilizar linters e Quality Gates providos por skills existentes (ex: Clean Architecture Skill), evitando a criação de validações paralelas que fragmentam o critério de qualidade.
3.  **Quality Gates**: Direcionamento explícito para a IA validar implementações conforme as regras do projeto, criando um ciclo de implementar, validar e corrigir com critérios claros.
4.  **Estilo de Código e Boas Práticas**: Consolidação de regras como limite de 400 linhas por arquivo, aplicação de princípios SOLID e responsabilidade única, e preferência por nomes de arquivos que facilitem buscas (ex: via `grep`), tornando o projeto navegável para humanos e ferramentas.
5.  **Testes de Front-end**: Instrução específica para usar Playwright CLI para navegação e testes, proibindo o uso de Playwright padrão/MCP e a criação de arquivos ou pastas E2E, para alinhar a estratégia de testes.
6.  **Testes de Back-end**: Exigência de testes para cada nova função e testes de regressão com mocks para bugs, garantindo que os testes sejam independentes, repetíveis, auto-validáveis e oportunos.
7.  **Topologia do Monorepo**: Detalhamento da estrutura de pastas (ex: `apps/web` para Next.js 16, `apps/backend` para o back-end), com `package.json` para cada aplicação e um `package.json` raiz para o workspace, minimizando erros de execução.
8.  **Gerenciamento de Dados**: Regra para criar um banco de dados por branch, promovendo o isolamento de dados e facilitando o trabalho com `worktree`.
9.  **Contexto Específico**: Inclusão de observações temporárias ou links para documentação (ex: Next.js 16) para mitigar confusões do agente com versões anteriores ou APIs desatualizadas.

O `AGENTS.md` não é estático; ele é um documento vivo que evolui com o projeto, incorporando novas instruções para corrigir desvios, reforçar padrões e capturar decisões arquiteturais conforme a equipe identifica comportamentos recorrentes dos agentes.

**Pontos de atenção**

*   **Sincronização Essencial**: É crucial manter `AGENTS.md` e `CLAUDE.md` sincronizados (idealmente via link simbólico) para evitar divergência de comportamento entre diferentes harnesses (Codex vs. Claude) que consomem arquivos distintos.
*   **`AGENTS.md` Não é Estático**: O arquivo inicial, gerado por scaffolding, é apenas uma baseline operacional e não deve ser tratado como a versão final. Ele deve evoluir e ser modificado ao longo do tempo conforme o projeto e o comportamento dos agentes se desenvolvem.
*   **Padronização de Ambiente**: Documentar scripts de início, parada e limpeza (`init.sh`, `stop.sh`) no `AGENTS.md` é uma boa prática para padronizar operações recorrentes, reduzir erros operacionais e assegurar um estado conhecido do projeto.
*   **Centralização de Quality Gates e Linters**: Evite criar múltiplos scripts de autovalidação ou linters paralelos, pois isso fragmenta os critérios de qualidade. Em vez disso, instrua o agente a reutilizar os gates e linters já providos por skills existentes (ex: Clean Architecture Skill).
*   **Direcionamento Explícito da IA**: Assegure-se de que o `AGENTS.md` instrua a IA a verificar e validar a implementação *intencionalmente* e alinhada às convenções estabelecidas, em vez de improvisar verificações inadequadas ou incompletas.
*   **Regras como Restrições Operacionais**: Consolide regras de estilo e arquitetura (limite de linhas, SOLID, responsabilidade única, nomes buscáveis) no `AGENTS.md` para que se tornem restrições operacionais para o agente, e não apenas preferências humanas.
*   **Especificidade em Ferramentas de Teste Frontend**: Seja explícito quanto à ferramenta preferencial (ex: Playwright CLI, não Playwright padrão ou MCP) e proíba a criação de artefatos indesejados (ex: arquivos/pastas E2E) para garantir a adesão à estratégia de teste do projeto. A redundância nessas instruções pode ser deliberada se o modelo insistir em um caminho incorreto.
*   **Testes Confiáveis Obrigatórios**: O `AGENTS.md` deve transformar os critérios de um teste confiável (independente, repetível, auto-validável, oportuno) em expectativa explícita de entrega, forçando o agente a produzir código verificável desde a origem, incluindo testes para novas funções e de regressão para bugs com mocks externos.
*   **Clareza na Topologia do Monorepo**: Explicitar a estrutura do monorepo e a localização dos `package.json` para cada aplicação e para o workspace ajuda a reduzir erros de execução em diretórios errados por parte do agente.
*   **Isolamento de Dados por Branch**: A regra de criar um novo banco de dados para cada branch de trabalho é vital para evitar contaminação entre linhas de trabalho, especialmente ao usar `worktree`, garantindo previsibilidade no desenvolvimento paralelo.
*   **Mitigar Conhecimento Desatualizado da IA**: Inserir observações temporárias ou links para documentação relevante (ex: Next.js 16) é uma boa prática para guiar o agente quando o ecossistema está em consolidação e o modelo pode confundir APIs ou comportamentos antigos.