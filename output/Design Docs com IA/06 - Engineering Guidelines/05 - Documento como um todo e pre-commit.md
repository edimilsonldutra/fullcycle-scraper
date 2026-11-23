Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17229)

## Resumo da aula

Agora que já falamos sobre a stack, vamos abordar os princípios fundamentais, os core principles. Aqui vou trazer alguns pontos inegociáveis sobre como trabalhar. No caso da linguagem Go, vou destacar filosofias e estilo. Por quê? Porque Go tem uma filosofia própria, é uma linguagem que preza pela simplicidade. Existem diversos manuais sobre como trabalhar com Go e, apesar de ser uma linguagem mais nova em comparação com outras, tem peculiaridades justamente por essa busca pela simplicidade.

Então, as diretrizes incluem: usar a formatação padrão, seguir as convenções estabelecidas, escrever de forma simples e clara, evitar abstrações desnecessárias, rodar go vet e outras análises estáticas antes de commitar. O código deve ser autoexplicativo, ou seja, quero bater o olho e entender, sem precisar de comentários excessivos. Obviamente, muitos desses princípios podem ser aplicados a outras linguagens também.

Ferramentas principais: formatação, imports, análise estática, lint. Em seguida, a inicialização do projeto: gerenciamento de dependências, estrutura para projetos pequenos e grandes. Isso varia para cada linguagem. As sugestões aqui são um ponto de partida, não estou partindo do zero. Isso poderia ser adaptado para um projeto real da sua empresa, baseado em como o projeto realmente funciona.

Diretórios principais, uso de containers: como configurar o Dockerfile para desenvolvimento, o Docker Compose, volumes compartilhados, cache de pacotes, uso de Postgres, .dockerignore, comandos essenciais para subir containers, verificar logs, rodar a aplicação. Costumo trabalhar com docker compose exec para rodar comandos dentro do container, garantindo que não preciso ter o Go instalado localmente ou me preocupar com versões específicas. Tudo é executado dentro do container.

Makefiles podem ajudar na automação. Convenções de nomenclatura: PascalCase para tipos exportados, camelCase para não exportados. Variáveis, constantes, organização de arquivos, sistema de tipagem, type safety, alocação e inicialização, funções e métodos, assinaturas, retorno de erros, boas práticas.

Tratamento de erros: em Go, isso é bastante peculiar. Mostrar como verificar erros, boas práticas, o que é bom e o que é ruim. Concorrência e paralelismo: sincronização, goroutines, context e cancelamento. Cada linguagem tem suas particularidades.

Testes: table-driven tests, algo muito comum em Go, asserções, comandos para rodar testes, mocks, dependency injection, test doubles (stubs, mocks, fakes, spies), testes de integração, profiling, benchmarks, otimização de strings e memória, segurança, validação de inputs, padrões de código.

Enfim, estamos cobrindo tudo o que imaginamos nas seções que passei anteriormente, incluindo log, observabilidade e muito mais. É uma quantidade enorme de informações.

Mas vejam só, ao mesmo tempo, temos uma pré-commit checklist. Antes de commitar, quero garantir que tudo isso foi aplicado: que o código compilou, que todos os testes passaram (inclusive com detecção de race conditions), que a qualidade está boa, que os erros foram tratados, que os recursos estão adequados, que a documentação está em dia, que o Docker e o Docker Compose estão funcionando, que o container está operacional.

E por fim, documentações, guias de referência e ferramentas que podem ser utilizadas em todos esses aspectos. É um documento grande, e o que faz sentido para você ou não, vai depender do projeto. Vale a pena avaliar se faz sentido ter isso no seu contexto. Esse documento pode ser maior ou menor, conforme a necessidade.

Da mesma forma que tenho para Go, tenho guidelines para Java. Escolhi algumas bibliotecas, manuais, princípios, Google Java Style Guide, convenções, clareza, inicialização de projetos, estrutura, Docker, e assim vai. São muitos detalhes para cada linguagem.

Peguei outro exemplo mais específico: pedi para criar guidelines para Python, mas com foco em LangGraph como framework. LangGraph é extremamente importante para desenvolvimento de agentes, então a forma de trabalhar é diferente, pois envolve um framework específico.

Resumindo, temos diversas formas de criar guidelines. Vocês terão acesso a todos esses exemplos para analisar e ver o que faz sentido para o projeto de vocês. O mais importante é que também terão acesso a um comando, um prompt específico, que vai ajudar a gerar esses documentos. Depois, podem iterar, remover partes, comparar com o código e refinar.

Essa é a ideia que queria trazer. Vamos seguir para esse comando e ver como tudo funciona na prática.

## Transcrição

00:01

Bom, pessoal, agora que a gente já falou da nossa stack aqui, tá? Aqui a gente vai naqueles pontos de princípios, né? Core principles aqui. Então, aqui eu vou trazer alguns pontos que é inegociável, de forma geral, de como que eu vou trabalhar, tá? E nesse caso aqui na linguagem Go, eu vou colocar filosofias e estilo. Por quê?

00:23

Porque a linguagem Go tem uma filosofia, é uma linguagem que tem que ser extremamente simples. Existem diversos manuais de como você trabalha com o Go. O Go, apesar de ser uma linguagem nova em relação às outras linguagens, tem algumas peculiaridades exatamente pela forma de ela ser simples.

00:42

Então, fala que, olha, você tem que usar a parte de formatação, você tem que focar nesse manual para convenções, você tem que escrever de forma simples e clara e evitar um monte de abstrações, golvete, static check antes de comitar. Aí, como que você consegue ser claro, né? Tipo, como que eu posso me comunicar, como que as coisas elas têm que ser auto, né? Self-explanatory, né? Ou seja, eu não quero ficar

01:11

comentando pra caramba, mas, ao mesmo tempo, eu quero bater o olho no código, eu quero entender. E, obviamente, muitas dessas coisas podem ser aplicadas para outras linguagens também. Ferramentas principais. Então, eu falei de formatação, eu falei disso e etc. Então, vamos lá, como é que eu formato? Como é que eu importo? Como é que eu faço análise estática? Como é que eu faço a parte de lint? E aqui é como que eu inicializo um projeto. Como é que funciona a parte de dependência? Como é que ele trabalha? E aí, para cada linguagem é diferente.

01:40

a estrutura de um projeto pequeno, a estrutura de um projeto grande, e aqui são sempre sugestões da forma como colocou o ponto, aqui eu não estou partindo do zero, e isso aqui poderia ser um projeto da sua empresa ou não, mas aí vai ser baseado exatamente em como o seu projeto funciona.

01:58

diretórios principais, como é que funciona a parte de container, nesse caso aqui, como é que funciona o meu Dockerfile para eu desenvolver, como é que vai funcionar o meu Docker Compose. Então, olha, eu vou ter o meu Dockerfile, o volume que eu vou compartilhar, a parte para eu ter caching nos pacotes, ele vai utilizar o Postgres, depois a gente vai falar um pouco sobre isso.

02:20

docker ignore, quais são os comandos essenciais. Então, para subir o meu container, para verificar os logs, para rodar a minha aplicação. Eu costumo trabalhar muito com docker compose exec com o nome dos meus containers e rodando sempre dentro do container para eu, por exemplo, garantir que

02:40

eu não precise ter o Go instalado na minha máquina, ou ter o Go da versão específica para eu trabalhar. Então, eu sempre executo as coisas dentro do container. Então, tem diversos pontos. Makefiles, que podem me ajudar. Convenções de como que eu trabalho, com tipos, structs e etc. Aqui, Pascal Cases. Quando eu não vou exportar aqui,

03:03

variáveis, constantes, arquivos, como é que funciona a separação, sistema de tipagem, type safety, alocação e inicialização, funções e métodos, como é que funcionam as assinaturas, como é que funciona, como que eu retorno o erro, boas práticas.

03:18

como é que funciona a parte de... somente a parte de Error Handling, porque no Go principalmente... No Go não, né? Acho que toda linguagem de programação tem formas diferentes de trabalhar com erro. O Go tem uma forma ainda mais peculiar, né? Então, aqui mostra como que você deve fazer, convenções, né? Ou seja, o que é bom, o que é ruim, tá? Como que eu faço verificação de erro? Como que eu trabalho com boas práticas, né? Como é que eu trabalho com concorrência e paralelismo?

03:47

sincronização, Go rotinas, context e cancellation. Então, tem diversas áreas aqui que, para cada linguagem, eu acabo olhando de uma forma diferente. Então, como é que eu trabalho com testes? Como é que eu trabalho com table-driven test? Porque no Go é muito comum a parte de acerções. Quais são os comandos que eu utilizo para rodar testes? Como é que eu trabalho com mock? Como é que eu trabalho com dependency injection? Como é que eu faço com...

04:14

testes doubles, dublês, stubs, mocks, fakes, spice, testes de integração, a parte de profiling, a parte de benchmarks, a parte de otimização, a parte de string optimization, memory optimization, parte de segurança, validação de inputs, padrões de código. Então, se você vai ver, aqui a gente está indo longe

04:35

em tudo que você pode imaginar naquelas sessões que eu acabei passando pra você. Desde log, observabilidade e tudo mais. Então, assim, é coisa pra caramba. Mas olha só aqui, ao mesmo tempo, que interessante. Eu tenho uma pre-commit checklist. Então, antes de eu comitar, eu quero garantir que foi aplicado

04:53

no meu código tudo isso aqui e garantiu que o meu código compilou, que todos os meus testes estejam passando, inclusive a parte de race condition, por exemplo, qualidade, né? Se os meus erros foram colocados, os meus resources e etc., nesse caso aqui específico do Go, como é que a documentação está feita, como é que o Docker se está válido, o Docker Compose está funcionando, se o meu container está funcionando e tudo mais.

05:16

E aqui são documentações e guias de referência e ferramentas que podem ser utilizados aqui em todos aqueles aspectos que eu coloquei. Então, se você olhar, é um documento grande e aí vai depender muito o que faz sentido pra você ou não, tá? Então...

05:32

Vale a pena você realmente ver se isso faz sentido ter no meu projeto ou não. Esse documento pode ser maior, menor e tudo mais. E da mesma forma que eu tenho o Gold, eu tenho para a Java. Então, eu pegar aqui Java, Guidelines, eu tinha escolhido algumas bibliotecas do Java para trabalhar e tudo mais. Então, está aqui Manual de Java, Princípios, como é que funciona a filosofia, usar o Google Java Style Guide, Conventions.

05:58

a parte de trazer clareza, como é que eu inicializo um projeto, há projetos de estrutura, como é que funciona com o Docker, como é que funciona... E aí vai longe, tá vendo? Então, assim, é muito detalhe para cada linguagem de programação. Aqui eu peguei um outro exemplo, um pouco mais específico, que eu pedi para ele criar um guideline de Python,

06:17

mas onde eu vou utilizar LandGraph como um framework. E o LandGraph é um cara extremamente importante porque eu vou desenvolver especificamente para agentes. Então, a forma de como ele trabalhar vai ser um pouco diferente, porque ele vai falar de um outro framework e as coisas vão funcionar dessa forma.

06:33

Basicamente, pessoal, a gente tem diversas formas de ter guidelines. Eu peguei alguns exemplos, você vai ter acesso a tudo isso para você depois dar uma olhada e também ver o que faz sentido ou não para o seu projeto. Mas eu acho que o mais importante, você também vai ter acesso a um comando, um prompt bem específico que vai te ajudar, no final das contas, a gerar esses documentos. E depois você pode ir iterando, você pode ir removendo parts, você pode ir batendo com o seu código.

07:01

e refinando tudo isso aí, tá? Então, basicamente, essa é a ideia que eu queria trazer. E aí, vamos nessa para esse comando e ver como é que tudo isso funciona.

## Resumo IA

**Abreviações**  
- **Go** — Linguagem de programação Go  
- **Dockerfile** — Arquivo de instruções para gerar uma imagem Docker  
- **Docker Compose** — Ferramenta para definir e executar aplicações com múltiplos containers  
- **Postgres** — PostgreSQL, sistema de gerenciamento de banco de dados relacional  
- **Go vet** — Ferramenta de análise estática da linguagem Go  
- **Lint** — Processo/ferramenta de análise para identificar problemas de estilo e qualidade de código  
- **Type safety** — Segurança de tipos  
- **Pascal Case / PascalCase** — Convenção de nomenclatura com iniciais de cada palavra em maiúscula  
- **Camel Case / camelCase** — Convenção de nomenclatura com a primeira palavra em minúscula e as seguintes capitalizadas  
- **Context** — Mecanismo de contexto em Go para cancelamento, deadlines e propagação de valores  
- **Cancellation** — Cancelamento de execução/fluxo  
- **Race condition** — Condição de corrida  
- **Dependency Injection** — Injeção de dependência  
- **Mocks** — Objetos simulados usados em testes  
- **Stubs** — Dublês de teste com respostas predefinidas  
- **Fakes** — Implementações simplificadas usadas em testes  
- **Spies** — Dublês que registram chamadas e interações  
- **LangGraph** — Framework para construção de grafos/fluxos voltados a agentes  
- **Google Java Style Guide** — Guia oficial de estilo para Java do Google  

**Resumo**  
A aula apresentou os princípios fundamentais e as diretrizes de trabalho para desenvolvimento de software, com foco principal na linguagem Go, mas também com exemplos aplicáveis a Java e Python com LangGraph. O instrutor reforçou que Go tem uma filosofia própria baseada em simplicidade, clareza e baixo nível de abstração, por isso as guidelines devem priorizar formatação padrão, convenções consistentes, código autoexplicativo, uso de ferramentas de análise estática e lint antes do commit. A partir disso, foram organizados tópicos essenciais para orientar a criação e o uso de um documento de boas práticas: inicialização do projeto, gerenciamento de dependências, estrutura para projetos pequenos e grandes, organização de diretórios, convenções de nomes, tipagem, alocação e inicialização, funções, métodos e tratamento de erros.  

Também foi detalhado o uso de containers no fluxo de desenvolvimento, incluindo Dockerfile, Docker Compose, volumes compartilhados, cache de pacotes, uso de Postgres, .dockerignore e comandos para subir containers, ver logs e executar a aplicação. O instrutor destacou a prática de usar `docker compose exec` para rodar comandos dentro do container, evitando dependências locais como instalação de Go ou problemas de versão. Além disso, mencionou automações com Makefiles, boas práticas de concorrência e paralelismo, sincronização, goroutines, context e cancelamento. Na parte de testes, abordou table-driven tests, asserções, comandos para execução, mocks, dependency injection, dublês de teste, testes de integração, profiling, benchmarks, otimização de strings e memória, segurança e validação de inputs.  

Por fim, a aula enfatizou a existência de uma pré-commit checklist para garantir que o código compile, que os testes passem, inclusive com detecção de race conditions, que erros estejam tratados, que recursos e documentação estejam adequados e que Docker e Docker Compose estejam funcionando corretamente. O instrutor mostrou que esses guidelines podem variar em tamanho e profundidade conforme a linguagem e o contexto do projeto, citando exemplos para Go, Java e Python com LangGraph, e explicou que o objetivo é usar um prompt específico para gerar esses documentos, refiná-los por iteração e adaptá-los à realidade do projeto.  

**Pontos de atenção**  
- Priorizar simplicidade e clareza; evitar abstrações desnecessárias, especialmente em Go.  
- Seguir a formatação padrão e as convenções da linguagem antes de commitar.  
- Manter o código autoexplicativo; não depender de comentários excessivos para explicar o óbvio.  
- Executar análise estática e lint antes do commit, além de validar o código com ferramentas específicas como `go vet`.  
- Adaptar a estrutura do projeto, dependências e organização de diretórios ao contexto real da empresa/projeto.  
- Usar Docker e Docker Compose corretamente para padronizar o ambiente e evitar dependências locais divergentes.  
- Preferir executar comandos dentro do container com `docker compose exec` para reduzir problemas de versão e configuração.  
- Garantir que `.dockerignore`, volumes, cache de pacotes e serviços auxiliares como Postgres estejam bem configurados.  
- Seguir convenções de nomenclatura e tipagem para manter legibilidade e consistência.  
- Tratar erros de forma explícita e seguindo as convenções da linguagem; em Go, isso é especialmente importante.  
- Considerar cuidadosamente concorrência, paralelismo, sincronização, goroutines e cancelamento para evitar falhas sutis.  
- Escrever testes abrangentes, incluindo table-driven tests, integração, mocks e demais dublês de teste quando necessário.  
- Verificar race conditions, qualidade geral e cobertura dos testes antes de commitar.  
- Incluir profiling, benchmarks e otimizações apenas quando houver necessidade real e com base em evidências.  
- Validar segurança e inputs, evitando confiar em dados externos sem checagem.  
- Usar a pré-commit checklist como gate obrigatório: compilação, testes, qualidade, documentação e operação dos containers.  
- Tratar guidelines como documentos vivos: revisar, remover excessos, comparar com o código real e refinar continuamente.  
- Ajustar o nível de detalhe das guidelines ao tamanho e à complexidade do projeto; nem tudo precisa ser incluído sempre.  
- Considerar que cada linguagem ou framework pode exigir regras específicas, como Java com Google Java Style Guide ou Python com LangGraph.