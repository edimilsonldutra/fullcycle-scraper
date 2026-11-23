Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17779)

## Resumo da aula

Em um projeto Greenfield, o ponto de partida pode ser totalmente gerado pelo agente a partir das especificações ou parcialmente inicializado com um scaffold já pronto. Usar um scaffold básico do framework reduz gasto desnecessário de token com boilerplate previsível e preserva o esforço do agente para decisões mais relevantes de implementação. Nesse cenário, npx create-next-app --latest --yes cria rapidamente a base do projeto Next.js sem comprometer a abordagem orientada por especificação. A escolha não contradiz SDD; ela apenas evita delegar ao agente uma tarefa mecânica que já tem uma ferramenta consolidada.

A ausência inicial de CLAUDE.md é uma decisão deliberada quando o foco ainda está em entender especificações e geração de código. O guidance do agente entra em outra camada de trabalho, mais ligada a observar erros, ajustar comportamento e refinar a atuação do agente ao longo do tempo. Essa separação impede confundir base conceitual com tuning operacional do agente. Primeiro se estabelece como o sistema deve ser descrito; depois se melhora como o agente executa essa descrição.

Em versões recentes do Next.js, o scaffold pode gerar um agents.md com instruções específicas sobre breaking changes, APIs e estrutura de arquivos. Isso existe porque a versão do framework pode divergir do conhecimento anterior usado em exemplos ou treinamentos, e o arquivo atua como um aviso operacional para evitar código incompatível. Quando o texto aponta para documentação interna antes de escrever código, ele está reduzindo o risco de o agente aplicar padrões de uma versão anterior. Em especial no Next 16, essa proteção faz diferença porque mudanças estruturais afetam diretamente a geração correta do código.

Quando CLAUDE.md referencia @agents.md, o arquivo referenciado passa a ser carregado obrigatoriamente no contexto do agente. Isso funciona como um mecanismo de composição de contexto: um arquivo central inclui outro para garantir que certas instruções sempre estejam disponíveis durante a execução. Retomando esse cenário, algumas equipes mantêm o conteúdo principal em agents.md e usam CLAUDE.md apenas como ponte para ferramentas compatíveis com Cloud Code. A escolha entre concentrar o conteúdo em um arquivo ou em outro é menos importante do que manter uma fonte de verdade consistente.

Uma alternativa comum é substituir a duplicação entre CLAUDE.md e agents.md por um link simbólico com ln -s CLAUDE.md agents.md. Nesse arranjo, os dois caminhos passam a apontar para o mesmo conteúdo, o que evita divergência entre instruções equivalentes mantidas em arquivos separados. Isso é útil quando o ecossistema espera nomes diferentes de arquivo, mas a equipe quer editar apenas um ponto. Se você encontrar esse padrão em um repositório, a intenção normalmente é compatibilizar ferramentas sem replicar guidance manualmente.

Depois de ajustar scaffold e arquivos de guidance, o próximo passo é registrar esse estado com um commit no main. Esse commit inicial fixa a base do projeto e cria um ponto confiável para comparação, revisão e rollback. Mesmo mudanças pequenas, como inclusão de CLAUDE.md ou reorganização de agents.md, merecem ser versionadas antes de iniciar features. Isso mantém o histórico limpo e separa infraestrutura inicial de desenvolvimento funcional.

Criar o repositório remoto logo no início permite publicar o estado atual do projeto e habilitar um fluxo de colaboração baseado em push, pull request e merge. Esse passo deixa o trabalho pronto para revisão incremental, mesmo quando o desenvolvimento ainda está sendo feito de forma sequencial. A vantagem é estrutural: o projeto já nasce com um processo de integração definido, em vez de receber governança só depois que o código cresce. Com isso, cada feature pode evoluir em branch própria e ser integrada de forma rastreável.

A criação de uma branch como feature-01-landing-page delimita claramente a próxima unidade de trabalho. Em ferramentas como Cloud Code, comandos executados com ! no Bash também entram no contexto do agente, o que permite que ele acompanhe mudanças de branch e outras operações de ambiente sem depender de explicações adicionais. Esse detalhe importa porque o agente passa a agir com consciência do estado real do repositório. Assim, quando a implementação começar, ele já saberá em qual branch está trabalhando e poderá seguir o fluxo esperado.

## Transcrição

00:01

Bom, pessoal, finalmente chegou a hora de sair algum código.

00:07

Mas, novamente, galera, SDD,

00:09

você tem que entender de especificação e como isso é gerado. Para mim,

00:15

poderia ser muito mais simples trazer essas skills e

00:18

ficar dando comando aqui na sua frente,

00:20

mas a ideia é que você tenha profundidade em relação a isso, mas, óbvio,

00:25

que a gente tem que ver o nosso sistema sendo

00:27

gerado e como as coisas funcionam e tudo mais.

00:30

Então, aqui eu tenho algumas opções, tá?

00:33

Como vai ser uma aplicação utilizando o Next.js,

00:36

eu posso fazer algumas coisas aqui.

00:40

E como o meu objetivo é a gente trabalhar de uma forma mais purista ainda com o SDD,

00:47

perceba que eu não tenho nem CloudMD ainda, tá?

00:51

Olha só que interessante, eu não tenho CloudMD.

00:53

E o mais interessante, eu não vou criar o CloudMD agora, tá? Por quê? Porque...

00:59

Qualquer coisa mais focada na parte de guidance do agente,

01:04

nós vamos ver na parte de Harness Engineering.

01:07

E aí sim, o negócio é muito mais prático,

01:10

porque a gente vai começar a detectar erros do agente,

01:14

como que a gente melhora o agente,

01:16

como que a gente vê besteiras que o agente está fazendo,

01:19

e a gente vai corrigindo ao longo do tempo, aprendendo ao longo do tempo,

01:23

cercando todo esse cara. Então,

01:25

eu quero que fique muito claro para você essa

01:28

separação que a gente está fazendo para

01:30

você não achar que a gente só está colocando o skill para você ler e digitar.

01:35

Não. Isso é a base que você tem que saber. Beleza? Então,

01:40

o que acontece? Eu posso ter algumas opções aqui. Como é um projeto Greenfield,

01:45

eu posso ter duas opções. Eu posso pedir para ele já sair gerando,

01:50

né? Baseado nas minhas especificações. Se eu quiser,

01:52

eu posso ter um scaffold básico,

01:54

tá? Então, se eu quiser, eu posso chegar aqui,

01:56

por exemplo, que é o que eu vou fazer,

01:58

e eu vou dar um npx create-next-app, --latest --yes,

02:04

aqui para ele criar o scaffolding ali do Next.js aqui para mim, tá?

02:10

Somente para não fazer com que o meu agente fique gastando token à toa.

02:15

Para um boilerplate que normalmente ele já existe ali para mim.

02:20

Então, ele gerou aqui para mim o meu Next.js,

02:23

ele gerou essa parada para mim. Eu poderia, obviamente,

02:25

ter pedido isso para o meu agente ou até mesmo na especificação,

02:29

ou provavelmente o meu agente já iria fazer isso.

02:32

Uma coisa interessante que eu queria trazer aqui para vocês,

02:34

por exemplo, em uma aplicação Next.js,

02:36

pelo menos nesse momento, ele está gerando um agents.md.

02:41

E nesse agents.md, ele está falando, para começar,

02:45

esse não é o Next.js que você conhece.

02:49

Essa versão tem breaking changes, APIs, file structure, etc, etc.

02:54

Então, para saber mais, leia... o NodeModulesNextDistDocsBeforeWriting.

03:00

Por que ele está falando isso?

03:01

Porque nesse caso eu estou no Next 16 e muitas das coisas

03:04

Que a gente pode ter feito estavam no Next 15,

03:07

Nos treinamentos, então para evitar esses tipos de problema. Então ele coloca isso.

03:12

E no cloud.md, ele coloca um arroba agents.md.

03:17

O que isso significa?

03:20

Significa uma gambiarra.

03:22

Por que eu estou dizendo isso?

03:24

Toda vez que no cloud.md você coloca um arroba com o caminho de um outro arquivo,

03:29

isso significa o quê?

03:31

Que o cloud vai ler obrigatoriamente aquele arquivo

03:34

e carregar na janela de contexto.

03:36

O que isso significa é que, claramente, o pessoal da Verso, que faz o Next.js,

03:43

eles usam por padrão o agents.md,

03:48

mas eles também criam o cloud.md para quê?

03:53

Para que quem estiver utilizando o Cloud Code tenha esses dados

03:59

entrando ali como guidance do agente na hora que ele trabalhar.

04:04

Então, isso é uma forma que ele fez.

04:07

Normalmente, eu não trabalho assim, mas meio que dá na mesma.

04:13

Uma alternativa que eu vejo muita gente fazer.

04:16

Eu posso, por exemplo,

04:18

pegar o que está...

04:22

Aqui, por exemplo, no meu agents.md,

04:24

posso colocar o que está aqui no meu cloud.md, né?

04:28

Depende de quem você quer dar preferência, isso aí tanto faz,

04:30

eu estou invertendo somente para que você consiga ver.

04:34

E eu posso, por exemplo, apagar o meu agents.md, tá?

04:40

Eu estou colocando isso, pessoal,

04:42

porque está sendo muito comum no mercado e eu queria que você soubesse disso,

04:46

tá? E eu posso dar o quê? Um ln -s.

04:52

cloud.md

04:54

agents.md Ou seja, eu criei aqui um link simbólico.

05:01

É basicamente isso que eu fiz. Ou seja,

05:04

tudo que eu escrever agora no cloud vai aparecer ali no agents.md para mim.

05:10

Então, é basicamente isso que eu acabei fazendo aqui.

05:15

Mas, do jeito que estava, também funciona. Tanto faz, nesse caso.

05:20

Mas é somente alguma dica ali para quem sabe te ajudar,

05:23

ou se você ver algum momento, link simbólico, alguma coisa apontando ali,

05:27

provavelmente você já deve entender o que está rolando aqui.

05:32

Por padrão, na hora que eu fiz isso,

05:34

ele já criou o nosso repositório, o nosso main aqui para a gente.

05:40

E uma vez que ele fez isso, o que eu vou trabalhar agora aqui?

05:46

Eu vou dar um git commit.

05:48

Aqui nesse caso, você pode escrever commit para mim e tudo mais. E para quê?

05:53

Para ele pegar essas alterações ali do cloud.md,

05:56

agents.md e etc. aqui para mim. Legal?

06:03

E agora, perceba que ele comitou e trouxe aqui para mim. Ou seja,

06:08

o meu main está pronto aqui para funcionar.

06:13

Mas nós somos pessoas muito interessantes.

06:18

Então, eu vou trabalhar também em conjunto com o

06:22

repositório remoto para a gente conseguir utilizar.

06:25

Então, nesse nosso caso aqui,

06:28

o que eu vou fazer?

06:29

Eu vou pedir aqui para ele o seguinte, crie um repositório remoto

06:37

chamado devfullcycle .com .br o push. Legal?

06:55

Então eu estou pedindo para ele criar um repositório remoto aqui para mim e

07:00

ele já está jogando ali para a gente.

07:02

Então esse repositório já está disponível ali para qualquer

07:06

pessoa acessar e a gente já tem isso aqui organizado.

07:10

Por que eu estou colocando isso?

07:12

Porque a partir de agora a gente consegue trabalhar com pull requests para que

07:17

a gente consiga ir fazendo merge e ir trabalhando dentro de todos esses aspectos.

07:23

Temos duas opções agora, tá? A primeira opção que eu vou trabalhar,

07:28

porque nesse momento a gente vai fazer as coisas de forma mais sequencial,

07:31

é simplesmente criar um branch e depois pedir para criar uma pull request,

07:39

tá? Então, essa aí é uma forma de a gente trabalhar, beleza?

07:44

A outra forma de a gente trabalhar é trabalhando com o worktree,

07:47

mas a gente vai falar de worktree um pouquinho depois,

07:50

quando a gente for fazer lá. e fazer as coisas de forma paralela. Beleza?

07:55

Então, o que eu vou fazer aqui nesse momento? Eu vou dar um

08:02

git checkout "-b", e eu vou chamar de feature

08:09

-01

08:13

landing page.

08:19

Somente para quem usa especificamente Cloud Code,

08:22

toda vez que você dá um exclamação,

08:24

você está digitando... um comando no Bash, tá?

08:29

Mas quando você digita esse comando no Bash, ele joga no contexto do agente também.

08:35

Então, ele sabe que você fez isso e você não fez isso num terminal.

08:40

Então, ele sabe o que você acabou de fazer.

08:43

O que eu estou fazendo aqui, no final das contas,

08:44

é mudando de branch aqui para mim. Se você olhar agora aqui,

08:48

eu estou no branch F01 landing page aqui.

08:53

Uma vez que eu estou aqui, na realidade, vamos para o próximo vídeo,

08:56

para não ficar esse vídeo muito grande,

08:58

e a gente vê agora a parte de implementação. Vamos nessa.

## Resumo IA

**Abreviações**
*   **SDD**: Specification-Driven Development
*   **APIs**: Application Programming Interfaces

**Resumo**
A aula tem como objetivo demonstrar a transição do entendimento de especificações para a geração inicial de código em um projeto Greenfield, focando na aplicação de **Specification-Driven Development (SDD)**. O instrutor explica como configurar uma aplicação Next.js de forma eficiente, gerenciar arquivos de guidance para agentes de IA e preparar o ambiente para um fluxo de trabalho colaborativo.

Inicialmente, o projeto Next.js é gerado usando `npx create-next-app --latest --yes`. Essa abordagem é justificada como SDD-compatível, pois evita o gasto desnecessário de tokens do agente com boilerplate previsível, preservando seu esforço para decisões de implementação mais relevantes. É destacado que a ausência inicial de um `CLAUDE.md` é uma decisão deliberada para separar a base conceitual do sistema do tuning operacional do agente, que será abordado em "Harness Engineering".

A aula aprofunda nos arquivos de guidance: o `agents.md` pode conter instruções críticas sobre *breaking changes*, APIs e estrutura de arquivos para versões específicas do framework (como Next.js 16), atuando como um aviso operacional. É demonstrado como o `CLAUDE.md` pode referenciar `@agents.md`, garantindo que o conteúdo referenciado seja carregado obrigatoriamente no contexto do agente para composição de contexto. Uma alternativa prática para evitar duplicação de instruções é o uso de links simbólicos (`ln -s CLAUDE.md agents.md`), fazendo com que ambos os arquivos apontem para o mesmo conteúdo.

Finalmente, são abordados os passos de versionamento e colaboração: registrar o estado inicial do projeto (scaffold e guidance) com um `git commit` no `main`, criar um repositório remoto para habilitar um fluxo de trabalho baseado em push, pull request e merge, e criar uma *feature branch* (ex: `feature-01-landing-page`) para delimitar a próxima unidade de trabalho. É ressaltado que em ferramentas como Cloud Code, comandos Bash executados com `!` também são incluídos no contexto do agente, conferindo a ele consciência das operações do ambiente.

**Pontos de atenção**
*   **Uso Eficiente do Agente:** Utilize scaffolds básicos de frameworks (`npx create-next-app`) para gerar boilerplate previsível. Isso economiza tokens do agente e direciona seu esforço para decisões de implementação mais relevantes, alinhando-se com o SDD.
*   **Separação Conceitual e Operacional:** Mantenha uma clara distinção entre o estabelecimento da base conceitual (especificações e geração de código) e o tuning operacional do agente (Harness Engineering). Não confunda como o sistema deve ser descrito com como o agente executa essa descrição.
*   **Atenção a Versões do Framework:** Esteja ciente de que arquivos como `agents.md` podem conter avisos operacionais cruciais sobre *breaking changes*, APIs e estrutura de arquivos em versões específicas do framework (ex: Next.js 16). Ler esses documentos antes de codificar é fundamental para evitar a aplicação de padrões incompatíveis.
*   **Gestão de Contexto do Agente:** Entenda como arquivos de guidance (`CLAUDE.md`, `agents.md`) interagem. A referência `@agents.md` dentro de `CLAUDE.md` garante que instruções específicas sejam obrigatoriamente carregadas no contexto do agente, compondo seu conhecimento.
*   **Evitar Duplicação de Guidance:** Para manter uma fonte de verdade consistente e evitar divergências entre instruções, utilize links simbólicos (`ln -s CLAUDE.md agents.md`). Isso permite que diferentes nomes de arquivo apontem para o mesmo conteúdo, compatibilizando ferramentas sem replicar o *guidance* manualmente.
*   **Versionamento da Base do Projeto:** Sempre registre o estado inicial do projeto (scaffold e arquivos de guidance) com um `git commit` no `main` antes de iniciar o desenvolvimento de features. Isso cria um ponto de partida confiável para comparação, revisão e rollback, além de manter o histórico limpo.
*   **Habilitação Precoce de Colaboração:** Crie o repositório remoto e publique o estado inicial com um `git push` logo no início. Isso estabelece um fluxo de colaboração (pull requests, merges) desde o princípio, garantindo que o projeto já nasça com um processo de integração definido.
*   **Delimitação de Unidades de Trabalho:** Crie branches específicas para cada feature (ex: `feature-01-landing-page`) para delimitar claramente as unidades de trabalho e permitir um desenvolvimento rastreável.
*   **Consciência do Agente sobre o Ambiente:** Em ferramentas como Cloud Code, comandos executados com `!` no Bash são incluídos no contexto do agente. Isso garante que o agente esteja ciente de operações de ambiente (como mudança de branch) e possa agir com conhecimento do estado real do repositório.