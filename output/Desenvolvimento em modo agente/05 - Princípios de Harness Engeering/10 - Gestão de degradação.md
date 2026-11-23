Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17894)

## Resumo da aula

Gestão de degradação é o conjunto de práticas usadas para detectar e remover lixo estrutural introduzido ao longo do desenvolvimento, como código morto, lógica desnecessária, desvios arquiteturais e implementações mais lentas do que o necessário. Em ambientes com agentes, esse problema cresce porque a IA produz muito código em pouco tempo e, com isso, também amplia a taxa de resíduos acumulados. O harness não serve apenas para gerar saídas melhores; ele também precisa conter mecanismos para limitar a deterioração contínua da base.

AI slop é o acúmulo de artefatos de baixa qualidade produzidos por agentes: trechos redundantes, resquícios de features antigas, caminhos de execução inúteis e simplificações ruins. Uma resposta prática para isso é usar agentes que operam como garbage collectors de código, escaneando o repositório em background e abrindo PRs de refatoração quando encontram oportunidades de limpeza. Esse processo trata a degradação como uma fila operacional recorrente, e não como um problema excepcional.

A premissa operacional é simples: a IA vai falhar, vai desviar e vai introduzir soluções subótimas de forma recorrente. Isso inclui algoritmos mais lentos, lógica desnecessária e resíduos que parecem inocentes, mas aumentam custo de manutenção e risco de regressão. Por isso, a estratégia correta não é presumir perfeição do modelo, e sim construir contenção sistemática para erros previsíveis.

Retomando o papel do harness já estabelecido, uma prática útil é executar um simplificador de código ao final de cada feature. Esse passo compara os commits recentes, identifica complexidade desnecessária e tenta reduzir o código para uma forma mais limpa antes que o resíduo se consolide no repositório. A vantagem é deslocar a limpeza para perto da origem do problema, evitando depender apenas de ciclos posteriores de coleta de lixo.

Existem duas estratégias complementares para lidar com degradação: remediar depois ou prevenir durante o fluxo. A abordagem de garbage collector atua depois da geração, encontrando sujeira já inserida e propondo refatorações; a abordagem preventiva usa o evaluator e outras verificações do fluxo para barrar ou reduzir a entrada desse material. Em Harness Engineering, prevenção tende a ser mais barata, mas remediação continua necessária porque nenhum gate elimina completamente os desvios.

A IA acelera a degradação porque aumenta drasticamente o volume de mudanças, mas o problema já existia em times humanos sem qualquer automação generativa. Se um agente de limpeza for executado em um sistema legado nunca tocado por IA, ele ainda tende a encontrar código morto, resquícios e oportunidades de simplificação. A diferença está na escala e na velocidade com que o problema aparece, não na sua natureza fundamental.

Gestão de degradação precisa ser tratada como processo ativo do time, não como esforço eventual de faxina técnica. Isso implica criar rotinas intencionais para impedir a entrada de sujeira e, quando ela entrar, removê-la rapidamente por meio de mudanças controladas. Em um contexto com agentes, essa disciplina se torna parte estrutural da governança do código, assim como guardrails, avaliação e verificações funcionais já discutidos anteriormente.

## Transcrição

00:01

E pessoal, por último aqui, a gente tem um ponto que é gestão de degradação.

00:06

O tempo inteiro eu falei para vocês de como é importante a gente ter um harness.

00:10

De uma forma com que a gente consiga fazer com que o modelo gere o código,

00:16

que ele consiga trazer o melhor resultado possível.

00:19

Mas o que acontece é que, na prática, baseado nos últimos artigos,

00:24

pelo menos no momento da gravação desse vídeo,

00:26

tanto... Diversas empresas, inclusive, que eu conheço,

00:31

mas nesse caso eu estou pegando o exemplo tanto da Anthropic quanto da OpenAI,

00:34

é até curioso que eles faziam o que no final das contas?

00:42

Pegavam uma grande parte do tempo, por exemplo,

00:45

de uma sexta-feira, exatamente para remover AI slop. Ou seja,

00:51

agentes que simplesmente funcionam como garbage collectors para quê?

00:57

Rodando em background, começam a olhar código morto,

01:01

coisas que não precisam mais ser utilizadas,

01:03

ou seja, tudo aquilo de lixo que foi ficando,

01:06

resquício, desvio que a IA foi gerando. E aí, quando eles escaneiam esses desvios,

01:13

são abertas PRs para fazer a refatoração. Então,

01:18

para você ter uma ideia de como que essas coisas são sérias, a IA,

01:23

invariavelmente, vai falhar. Invariavelmente ela vai desviar,

01:27

invariavelmente ela vai colocar lógicas desnecessárias,

01:32

algoritmos que às vezes são mais lentos.

01:35

Então a gente tem que tomar muito cuidado com isso,

01:38

porque às vezes algumas coisas inocentes podem gerar dano.

01:41

Então recomendo também no seu harness,

01:43

por exemplo, toda vez que você terminar uma feature, roda um code... um simplificador,

01:50

onde ele tenta olhar as diferenças dos commits e tenta simplificar o código,

01:54

deixando esse código mais limpo. Ou seja, para que você evite ter que, sei lá,

02:01

ficar rodando um garbage collection exatamente para remover

02:05

tranqueiras que a IA foi colocando.

02:07

Ou seja, buscando oportunidades de remoção de coisas erradas que a IA trabalhou.

02:12

Isso aqui foi...

02:14

Inicialmente, o Garbage Collector, a OpenAI começa a utilizar.

02:20

E tem uma abordagem, obviamente, aqui da Anthropic,

02:23

que basicamente é o fluxo de desenvolvimento,

02:27

ele tenta prevenir esse processo. Então,

02:30

na hora que eu estou desenvolvendo o evaluator,

02:32

ele faz essa verificação para que minimize essa entrada de sujeira dentro do código. E sim, galera,

02:40

a gente voltou para uma época onde o nosso código pode ter sujeiras.

02:44

Quem é da época do Dreamweaver, do FrontPage, há muitos anos atrás,

02:49

e a gente programava usando o HTML puríssimo, todo bonitinho,

02:54

e a gente usava aqueles editores que sujavam todo o nosso HTML.

02:58

Então, o que dá a impressão que a gente voltou

03:00

um pouco nesse tempo onde parte do nosso código vira lixo,

03:06

ou parte do nosso código... ele fica morto,

03:09

ou parte do nosso código são resquícios de features

03:11

anteriores que a IA não conseguiu tirar. Então,

03:15

independente de como está o modelo,

03:17

independente do momento que você está vendo esse vídeo,

03:19

o que a gente tem que entender é que a gestão de degradação do código,

03:24

ela deve existir.

03:25

Na minha opinião, isso não é um problema necessariamente somente da IA.

03:29

A IA, ela potencializa isso com certeza,

03:32

mas todo time de engenharia deve ter um...

03:38

um processo de ativo de degradação de código,

03:41

independente se foi IA que foi gerado ou não,

03:44

porque nós humanos fazemos muito, mas muito isso também.

03:48

É que a IA, como ela faz muito rápido,

03:50

com uma grande quantidade de código, agora tem agentes limpando sujeira de código.

03:55

Mas isso não significa,

03:57

se você rodar esse mesmo agente para limpar o código do seu software atual,

04:01

que nunca uma IA tocou,

04:03

isso também vai gerar um monte de PR.

04:07

Mas o ponto importante é que vocês tenham conhecimento e que vocês tenham

04:11

em mente que nós possamos ter processos ativos para evitar degradação do código.

04:17

Hoje em dia, é mais fácil fazer porque a gente tem IA.

04:22

Antigamente, fazer essa gestão toda era muito mais complexa. Agora,

04:27

o grande ponto é que, como a IA gera muito código,

04:30

isso aí tem que ser feito de uma forma mais intencional,

04:33

mais proativa e tentando sempre ao máximo.

04:37

Evitar, através de todo o harness que você está organizando,

04:41

com que essa sujeira entre e, quando ela entrar,

04:44

com alguma mudança, ela tenha que sair. Fechou? É isso aí. Então, galera,

04:49

falamos um pouco mais sobre os princípios de Harness Engineer e aí

04:53

a gente vai seguir e tentar colocar mais a mão na massa.

## Resumo IA

**Abreviações**
*   **AI**: Inteligência Artificial
*   **PR**: Pull Request
*   **HTML**: HyperText Markup Language

**Resumo**
A aula aborda a Gestão de Degradação, um conjunto de práticas essenciais para detectar e remover o "lixo estrutural" que se acumula no código ao longo do desenvolvimento. Este lixo inclui código morto, lógica desnecessária, desvios arquiteturais e implementações subótimas. Em ambientes com agentes de IA, o problema é amplificado, pois a IA produz grandes volumes de código rapidamente, aumentando drasticamente a taxa de resíduos acumulados, conhecidos como "AI slop" (artefatos de baixa qualidade).

O objetivo principal é tratar a degradação do código como uma fila operacional recorrente, e não como um evento excepcional. O instrutor explica que o `harness` (mecanismo de controle e validação de saída de IA) não deve apenas focar em gerar resultados melhores, mas também em conter a deterioração contínua da base de código.

São apresentadas duas estratégias complementares:
1.  **Remediação (depois da geração)**: Agentes de IA configurados como "garbage collectors" de código operam em background, escaneando o repositório para identificar sujeira (código morto, resquícios de features antigas, caminhos inúteis) e abrindo Pull Requests (PRs) de refatoração para propor a limpeza. Empresas como OpenAI e Anthropic já utilizam essa abordagem.
2.  **Prevenção (durante o fluxo)**: Utilizar ferramentas e verificações no fluxo de desenvolvimento (como um `evaluator` ou um simplificador de código) para barrar ou reduzir a entrada de material de baixa qualidade. Uma prática recomendada é executar um "simplificador de código" ao final de cada feature para comparar commits recentes, identificar complexidade desnecessária e limpar o código antes que o resíduo se consolide.

O fluxo ideal, portanto, combina prevenção (no `harness` e após features) com remediação contínua (agentes de limpeza em background), garantindo que a sujeira seja evitada ou rapidamente removida.

**Pontos de atenção**
*   **IA vai falhar**: A premissa fundamental é que a IA, invariavelmente, falhará, desviará e introduzirá soluções subótimas (algoritmos mais lentos, lógica desnecessária, resíduos aparentemente inocentes que aumentam custos de manutenção e riscos de regressão). Não se deve presumir a perfeição do modelo.
*   **Construir contenção sistemática**: A estratégia correta é construir contenção sistemática para esses erros previsíveis, em vez de depender da perfeição da IA.
*   **Papel do Harness**: O `harness` é crucial não apenas para gerar saídas de melhor qualidade, mas também para conter a deterioração contínua da base de código.
*   **Simplificador de código pós-feature**: Recomenda-se executar um simplificador de código ao final de cada feature para comparar commits, identificar complexidade desnecessária e limpar o código, deslocando a limpeza para perto da origem do problema.
*   **Prevenção vs. Remediação**: Em `Harness Engineering`, a prevenção (impedir a entrada de sujeira) tende a ser mais barata do que a remediação (limpar depois).
*   **Remediação é sempre necessária**: Mesmo com fortes mecanismos de prevenção, a remediação continua sendo essencial, pois nenhum "gate" (verificação) eliminará completamente todos os desvios e falhas.
*   **Degradação não é só problema de IA**: O problema da degradação de código (código morto, resquícios) já existia em times humanos sem IA. A IA apenas acelera e potencializa a escala e velocidade com que o problema aparece, não sua natureza fundamental.
*   **Processo ativo e contínuo**: A gestão de degradação deve ser tratada como um processo ativo e intencional do time, parte estrutural da governança do código (assim como guardrails e avaliações funcionais), e não como um esforço eventual de "faxina técnica".
*   **Remoção rápida**: É crucial criar rotinas intencionais para impedir a entrada de sujeira e, quando ela entrar, removê-la rapidamente por meio de mudanças controladas.