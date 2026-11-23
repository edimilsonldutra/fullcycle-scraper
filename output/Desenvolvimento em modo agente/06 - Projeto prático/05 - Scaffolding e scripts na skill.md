Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17968)

## Resumo da aula

Scaffolding é a automação da criação da estrutura inicial de um projeto. Retomando a skill e o template base já definidos anteriormente, o avanço aqui é embutir scripts executáveis dentro da própria skill para gerar diretórios, arquivos e configurações sem começar do zero. Isso reduz trabalho manual repetitivo e transforma convenções do projeto em execução concreta. A utilidade prática depende do contexto: quanto mais padronizada e compartilhada for a criação de projetos na empresa, maior o ganho.

Uma forma de estruturar isso é manter uma pasta templates com um projeto inicial ou um conjunto de arquivos-base, e uma pasta scripts com os comandos que materializam esse template. O ponto importante não é o nome da pasta, mas a separação entre referência estática e automação executável. Quando os comandos, argumentos e nomes ficam organizados em arquivos distintos, o scaffolding deixa de ser uma “linguiça” difícil de manter. Essa separação facilita evolução, leitura e ajuste fino do processo.

O scaffolding.sh funciona como ponto de entrada operacional e pode delegar a lógica principal para um arquivo JavaScript. Essa combinação é útil porque o shell integra bem com o ambiente e com a execução direta, enquanto o JavaScript lida melhor com fluxos, parâmetros e composição de etapas mais complexas. O resultado é um pipeline simples de invocar e mais flexível de implementar. Em vez de concentrar tudo em um único arquivo monolítico, cada parte assume uma responsabilidade clara.

Um script de scaffolding pode perguntar o nome da aplicação, se a criação será na pasta atual ou em uma nova pasta, se o projeto terá apenas back-end ou também front-end, se deve ativar Prisma, instalar dependências, rodar gates e inicializar Git. Essas perguntas transformam o scaffold em um gerador parametrizável, capaz de adaptar a base inicial ao cenário desejado sem exigir edição manual posterior. No exemplo de Video Max, o script usa essas respostas para montar o projeto conforme as escolhas feitas. Isso acelera a preparação do ambiente e reduz inconsistências na configuração inicial.

A skill não precisa apenas descrever regras e convenções; ela também pode carregar os scripts que executam essas regras. Quando isso acontece, a skill se torna autocontida: além de orientar o agente, ela oferece meios concretos para criar a base do projeto. Retomando a ideia de harness já estabelecida, a skill passa a atuar como parte central desse mecanismo operacional. O valor está em dar à IA condições reais de executar a preparação do sistema, e não apenas de sugeri-la.

O script pode ser executado manualmente por caminho direto, como .cloud/skills/clean-arc/scripts/scaffolding.sh, ou disparado por um agente como Cloud Code ou Codex. A diferença está na interface de acionamento, não no mecanismo final: em ambos os casos, o mesmo script realiza o trabalho. Isso preserva uma única fonte de verdade para a criação do projeto. Quando o agente invoca esse script, ele deixa de improvisar a estrutura inicial e passa a seguir um processo explícito.

Antes de entrar em código de negócio, DDD e implementação funcional, é necessário estabelecer a base do projeto. Essa base inclui estrutura de pastas, dependências, inicialização do repositório e demais decisões operacionais mínimas para começar com consistência. O scaffolding cumpre exatamente esse papel: preparar o terreno para que o desenvolvimento aconteça sobre uma fundação previsível. Sem essa etapa, o agente e o desenvolvedor tendem a gastar energia reconstruindo o básico a cada novo projeto.

## Transcrição

00:01

Bom, pessoal, agora que eu tenho essas minhas referências com a minha skill e tudo mais,

00:06

o que você pode fazer que pode ajudar,

00:10

aí vai depender do seu nível de preciosismo ou não,

00:12

é o quê? Dentro de templates, por exemplo,

00:16

você pode criar uma pasta chamada templates e dentro de templates você pode

00:20

criar um projeto inicial ou você tem um scaffold básico que vai te ajudar...

00:26

a gerar o esqueleto de arquivos daquilo que você precisa, tá?

00:30

Então, isso pode ajudar. Nem sempre vale a pena,

00:34

então vai depender muito de como você vai trabalhar,

00:37

principalmente se isso vai ficar espalhado pela empresa ou não e tudo mais.

00:40

Eu criei aqui um exemplo, tá? E como que eu criei nesse caso?

00:45

Eu criei através do quê? Dentro de uma pasta scripts,

00:48

você vai perceber que eu tenho diversos arquivos aqui dentro,

00:54

tá? Um desses arquivos,

00:56

olha só a quantidade de arquivos que a gente tem aqui,

00:59

depois a gente vai falar desses caras, tá?

01:01

Mas um desses arquivos é o meu arquivo de scaffolding, que é o meu scaffolding .sh.

01:08

Esse cara aqui, no final das contas,

01:10

ele vai chamar o meu arquivo, o meu JavaScript aqui,

01:14

que vai começar a rodar diversos programas

01:18

que estão dentro desse meu scaffolding aqui dentro.

01:22

Então, eu tenho comandos, argumentos, os nomes, etc.

01:25

Eu pedi para ele deixar bem separado para ficar um pouco mais

01:27

fácil de eu trabalhar para não ficar uma linguiça só.

01:30

Basicamente, é isso que eu acabei fazendo. E por que esse cara funciona dessa forma?

01:36

Eu criei esse cara apenas para dar o exemplo aqui. Então, somente para você saber.

01:41

Não fiquei revisando detalhes, melhorando o código,

01:44

mas é somente para te dar uma ideia do que você poderia fazer.

01:47

Por exemplo, eu posso chegar aqui.

01:50

em relação à parte usando a minha própria skill e eu posso

01:55

chamar ou executar diretamente o meu arquivo .sh aqui no meu caso,

02:02

então se eu quiser eu dou um

02:03

.cloud barra skills clean arc e daí

02:10

eu tenho scripts e daí eu posso dar um scaffold .sh aqui pra mim

02:16

E esse cara, olha o que ele vai falar aqui para mim.

02:18

Como que vai ser o nome da minha aplicação?

02:21

Eu vou colocar um ponto aqui para ele criar o nome do meu projeto.

02:26

Eu vou chamar de Video Max.

02:28

Vou colocar. Você quer criar uma nova pasta dentro do projeto ou na pasta atual?

02:34

Vou dar na pasta atual.

02:36

O diretório não está em branco.

02:39

Se você mesmo assim quer persistir os arquivos, substituir... Sim, eu quero.

02:44

Você quer somente back-end ou back-end e front-end?

02:48

Eu vou falar, eu quero que os dois,

02:49

tá? Você quer ativar o post-brisco prisma? Sim.

02:53

Você quer que instale as dependências? Sim.

02:56

Você quer rodar os gates depois do scaffolding?

03:00

Depois a gente vai falar sobre gates especificamente, tá?

03:04

Eu vou falar que sim. Você quer que inicialize o git? Sim.

03:07

Yes, yes, yes, yes? Yes. E agora ele vem aqui.

03:12

Vai criar meu projeto e vai fazer em tese aqui toda a mágica,

03:15

citando as dependências e organizando tudo aqui da forma como eu estava querendo.

03:20

Então, isso aqui acaba me ajudando para eu não partir do

03:24

zero na hora que eu vou criar um projeto em branco.

03:27

Então, a sua skill pode estar autocontida tendo scripts

03:32

que vão te ajudar a fazer isso.

03:34

Wesley, mas você teve que ir digitar o .sh direto. Sim.

03:39

Eu podia ter aberto o Cloud Code,

03:42

o Codex e pedido para ele executar, né? Falar, olha,

03:45

cria um scaffold para mim,

03:46

ele ia executar esse script aí para mim no final das contas, tá?

03:50

É basicamente isso que ia acontecer. Agora,

03:54

o ponto principal que eu acho aqui, pessoal,

03:57

é que vocês consigam entender que, de forma geral,

04:00

a nossa ideia aqui não é só automação.

04:04

A nossa ideia é fazer com que a IA tenha condições de criar as coisas para a gente.

04:10

Na skill, você tem a possibilidade de adicionar scripts que vão te ajudar.

04:15

Fora isso, de forma geral,

04:18

a skill vai ser um dos pontos centrais do seu harness.

04:23

Ou seja, a skill é um harness também nesse nosso caso. E agora, se você perceber,

04:29

ele falou, olha, seu ambiente está todo pronto.

04:32

Se você quiser iniciar a execução, você dá um script barra init.

04:37

E aí no próximo vídeo a gente vai falar um pouquinho mais sobre gates,

04:41

sobre esses scripts, etc.

04:43

Que é a partir daí que a gente começa o nosso processo de desenvolvimento.

04:47

Então perceba que antes de eu criar o meu projeto,

04:51

ou seja, começar a desenvolver o código,

04:53

as regras de negócio, entrar com toda a parte de...

04:57

SDD e tudo mais, eu preciso ter a base do meu projeto. Então, nesse caso aqui,

05:01

eu tenho uma skill que fez isso. No seu caso,

05:03

você não precisa ter uma skill que fez isso,

05:04

mas você precisa, de forma geral, ter uma skill para ajudar essas diretrizes aí.

05:09

Essa é uma das formas que eu trabalho para fazer isso. Fechou?

## Resumo IA

**Abreviações**
*   **DDD**: Domain-Driven Design
*   **IA**: Inteligência Artificial

**Resumo**
A aula tem como objetivo demonstrar o Scaffolding, a automação da criação da estrutura inicial de um projeto, integrando scripts executáveis dentro de "skills" e "templates base" previamente definidos. Isso permite gerar diretórios, arquivos e configurações sem começar do zero, visando reduzir o trabalho manual repetitivo, transformar convenções em execução concreta e garantir um ganho significativo em empresas com criação de projetos padronizada.

O instrutor explica um fluxo onde uma pasta `templates` armazena o projeto inicial ou arquivos-base, enquanto uma pasta `scripts` contém os comandos de automação. Essa separação é crucial para evitar scripts monolíticos e facilitar a manutenção. O script `scaffolding.sh` serve como ponto de entrada operacional, delegando a lógica principal para um arquivo JavaScript. Essa combinação é eficiente, pois o shell integra bem com o ambiente para execução direta, e o JavaScript lida melhor com fluxos, parâmetros e composição de etapas mais complexas, resultando em um pipeline flexível e simples de invocar.

O script de scaffolding é parametrizável, realizando perguntas ao usuário sobre o nome da aplicação, local de criação (pasta atual ou nova), inclusão de back-end/front-end, ativação de Prisma, instalação de dependências, execução de "gates" e inicialização do Git. As respostas moldam o projeto conforme as escolhas, acelerando a preparação do ambiente e reduzindo inconsistências. A "skill" não apenas descreve regras, mas se torna autocontida ao carregar esses scripts, atuando como um "harness" que permite à IA condições reais de executar a preparação do sistema. O script pode ser acionado manualmente ou por agentes como Cloud Code ou Codex, mantendo uma única fonte de verdade para a criação do projeto e assegurando que uma base consistente seja estabelecida antes de iniciar o desenvolvimento do código de negócio e a implementação funcional (DDD).

**Pontos de atenção**
*   **Utilidade Contextual do Scaffolding**: O benefício do scaffolding é maior quanto mais padronizada e compartilhada for a criação de projetos na empresa. Em cenários de baixa padronização, a complexidade pode não compensar.
*   **Separação de Responsabilidades**: É crucial manter a pasta `templates` (referências estáticas/arquivos-base) separada da pasta `scripts` (automação executável). Essa organização evita scripts monolíticos ("linguiça"), facilitando a evolução, leitura e ajuste fino do processo.
*   **Combinação Estratégica de Tecnologias**: Utilizar `scaffolding.sh` (shell) como ponto de entrada para integração com o ambiente e execução direta, delegando a lógica principal para JavaScript, otimiza o pipeline. O shell integra bem com o ambiente, e JavaScript lida melhor com fluxos e parâmetros complexos.
*   **Scripts Parametrizáveis**: Desenvolver scripts que interagem com o usuário (perguntando nome da aplicação, tipo de projeto, tecnologias, etc.) permite adaptar a base inicial a diferentes cenários sem exigir edição manual posterior, reduzindo inconsistências na configuração.
*   **Skills Autocontidas como Harness**: A "skill" deve ir além de apenas descrever regras; ela deve carregar os scripts que executam essas regras. Isso a transforma em um "harness" que confere à Inteligência Artificial a capacidade real de executar a preparação do sistema, e não apenas de sugeri-la.
*   **Fonte Única de Verdade**: Garanta que o mesmo script de scaffolding seja utilizado, independentemente de ser executado manualmente ou por um agente (Cloud Code, Codex). Isso impede a improvisação da estrutura inicial e garante um processo explícito e consistente.
*   **Prioridade na Base do Projeto**: É essencial estabelecer a base do projeto (estrutura de pastas, dependências, inicialização do repositório e demais configurações operacionais mínimas) *antes* de iniciar o desenvolvimento do código de negócio, DDD e implementação funcional. Isso evita que desenvolvedores e agentes gastem tempo e energia reconstruindo o básico.