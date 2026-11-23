Módulo: Protocolos de Comunicação\
Aula: [Primitivos: Tools e Resources](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18593)

## Resumo da aula

Primitivos são as unidades básicas de troca de informação no MCP. Em vez de tratar tudo como texto solto ou prompt ad hoc, a arquitetura passa a expor capacidades com significado operacional explícito. Essa mudança importa porque sistemas escaláveis não podem depender de interpretação livre para decidir como ler contexto e como executar ações. O ganho real é sair de um bilhete informal para um contrato tipado entre modelo e mundo externo.

A decisão de modelagem começa com uma pergunta simples: essa capacidade observa o estado do sistema ou age sobre ele? Se a necessidade é consultar contexto, ler dados ou inspecionar estrutura, a modelagem correta tende a ser resource. Se a necessidade é alterar estado, disparar efeitos externos ou executar computação ativa, a modelagem correta tende a ser tool. Essa heurística evita confundir leitura com execução e organiza a superfície do server de forma governável.

Resources são capacidades de leitura expostas pelo server para que o modelo consulte dados sem provocar efeitos colaterais. Eles funcionam como os “olhos” do sistema: mostram logs, arquivos de configuração, tabelas dinâmicas ou código-fonte, mas não executam nada por si só. Isso reduz ambiguidade porque o modelo não precisa decidir se deve agir apenas para obter informação. Em fluxos com LLM, a leitura primeiro melhora a decisão posterior.

Modelar leitura como tool força o modelo a raciocinar sobre chamadas executáveis quando ele só precisava inspecionar contexto. Esse desenho aumenta a chance de alucinação, porque a interface sugere ação onde deveria haver apenas consulta. Também desperdiça tokens, já que cada tool adiciona definição, parâmetros e carga de contexto desnecessária. A consequência prática é um agente menos previsível e mais caro de operar.

Cada resource é identificado por uma URI, e isso faz mais do que apontar localização: carrega semântica. Uma URI estruturada informa hierarquia, domínio e relação entre dados, permitindo que o modelo navegue de forma lógica em vez de tentar adivinhar onde cada informação está. O efeito arquitetural é semelhante ao de um diretório bem organizado ou de um índice navegável. A URI transforma consulta em exploração orientada por estrutura.

Para quem já trabalha com Web API, resource se comporta semanticamente como um GET: serve para leitura e contextualização. A regra prática é direta: se não há alteração de estado, disparo de e-mail, escrita em banco ou efeito externo, a capacidade deve ser modelada como leitura. Essa analogia não substitui o protocolo MCP, mas ajuda a manter a fronteira semântica limpa. A IA passa a distinguir com clareza quando está observando e quando está operando.

Retomando o cenário de inspeção de repositório, o modelo pode ler classes, dependências e estrutura do projeto via resources antes de abrir um pull request ou executar um refactoring via tool. Essa ordem importa porque primeiro se constrói contexto, depois se decide a ação. O fluxo fica mais confiável quando a máquina enxerga antes de agir. Em termos operacionais, isso reduz decisões precipitadas e melhora a qualidade da execução.

Tools são capacidades executáveis expostas pelo server para transformar intenção em efeito concreto. Elas funcionam como as “mãos” do sistema: interagem com sistemas externos, alteram registros, disparam e-mails, iniciam deploys ou executam cálculos pesados. O ponto decisivo não é o nome da operação, mas a presença de ação ativa sobre o ambiente ou produção de resultado computacional. Sempre que houver efeito, há necessidade de tool.

Uma tool não deve ser anunciada apenas em linguagem natural; ela precisa de um contrato explícito, normalmente descrito por schema JSON. Esse schema define campos, tipos e obrigatoriedade de parâmetros como to, subject e body em uma operação send_email. O objetivo é restringir a ambiguidade da LLM e tornar a chamada mais determinística. Quanto mais claro o contrato, maior a chance de execução correta e menor a liberdade para inferências erradas.

Se resources ocupam o espaço semântico do GET, tools se aproximam de POST, PUT e DELETE: são operações transacionais ou ativas. Elas existem para alterar estado ou produzir efeitos concretos no output do sistema. Essa analogia ajuda a classificar capacidades do server sem depender de intuição vaga. Nos próximos cenários com PostgreSQL MCP e GitHub MCP, esse critério separa o que deve ser navegado como contexto do que deve ser invocado como ação.

## Transcrição

00:00

Fala galera, beleza? Sejam bem-vindos à nossa próxima aula. Então, vamos lá,

00:06

vamos relembrar. Na aula passada a gente fez o quê? A gente definiu...

00:09

Quais são os personagens aqui da nossa história,

00:11

do joguinho que a gente está jogando aqui.

00:13

Então a gente colocou no tabuleiro aqui o host,

00:15

o client e o server, beleza?

00:17

Então eu expliquei para vocês mais ou menos como é que eles funcionam,

00:19

o que cada um faz, responsabilidades e assim por diante.

00:23

Agora que a gente já está com essas peças aqui no tabuleiro,

00:26

a gente precisa definir o que elas vão usar de vocabulário para conversar.

00:30

Então no desenvolvimento que a gente tem aqui de A tradicional,

00:33

a gente costuma fazer o quê? A gente pensa tudo como string, certo?

00:37

Então normalmente a gente pensa em um prompt, em uma string solta,

00:40

mas quando a gente está falando de um sistema que é escalável, já não dá para pensar assim.

00:45

A gente precisa ser um pouco mais estratégico, a gente precisa subir o nível.

00:48

E daí quando a gente está falando do modelo de context protocol,

00:52

a gente passa não só de texto de um lado para o outro,

00:55

mas a gente começa a trabalhar com os primitivos

00:57

que a gente vai aprender um pouquinho aqui.

00:59

Então os primitivos do MCP.

01:01

Antes de entender os primitivos, a gente precisa entender... Para que eles servem?

01:07

Eles são, no final das contas, uma unidade básica de troca de informação.

01:11

Então, a gente está falando, por isso que ele é chamado de primitivo,

01:13

porque ele é aquela estrutura mais primitiva,

01:16

mais básica de troca de informação,

01:17

que vai ser usada para a troca de informação do cérebro com o mundo real.

01:22

É a diferença entre você enviar um bilhete

01:26

desorganizado e você entregar um contrato assinado,

01:29

tipado e assim por diante. Essa é a ideia, tá bom?

01:33

Qual é a ideia que a gente tem para resolver aqui?

01:36

Qual é o conceito da anatomia da operação que a gente vai trabalhar?

01:41

Vamos voltar para facilitar a visualização a nossa analogia

01:45

principal que a gente falou na última aula.

01:48

Se o host é o comandante que está tomando as

01:50

decisões e o server está sendo a força bruta,

01:54

o músculo que faz a coisa,

01:55

o primitivo aqui vai ser a ferramenta de trabalho que

01:58

eles vão usar para fazer a coisa acontecer.

02:01

Os documentos de consulta que eles trocam entre si e assim por diante.

02:04

Então hoje, nessa aula,

02:06

a gente vai focar nos dois pilares que vão sustentar 90%

02:09

da implementação que a gente tem de IA.

02:11

Os tools, que são as ferramentas, e os resources,

02:14

que são os recursos que a gente tem para trabalhar.

02:16

As tools, elas são a mão do seu sistema. Pensa assim,

02:19

o jeito mais fácil de entender é que as tools são as mãos do seu sistema.

02:23

Elas vão agir, alterar o estado e executar funções. Então,

02:27

é o que está fazendo as coisas, beleza? E os resources,

02:30

eles são os olhos do seu sistema. Eles vão prover ali a visão de contexto,

02:33

dado bruto, para que a decisão seja tomada com mais precisão.

02:38

Então, ali você vai ter toda a organização para você

02:41

conseguir tomar a melhor decisão e você conseguir fazer...

02:44

com que as suas mãos façam as coisas certas.

02:47

No final das contas, é isso que a gente está falando.

02:49

Sem essa distinção clara, o que você pode fazer?

02:52

Você pode acabar, ao invés de construir um agente,

02:54

você vai construir ali um script que vai chutar o que ele

02:56

tem que fazer e vai fazer o melhor que ele pode.

02:59

Então não vai estar organizado,

03:00

escalável e assim por diante.

03:01

Essa é a diferença de fazer um promptzinho e fazer um sistema agêntico.

03:05

Então aqui que mora o segredo da coisa, tá?

03:09

Então... O que a gente precisa pensar agora é que

03:11

você não pode usar a ferramenta para tudo.

03:14

Você vai começar a pensar em como você trabalha

03:17

utilizando essa estratégia que eu te falei.

03:20

Então, muito desenvolvedor comete um erro de achar que

03:24

tudo vai ser resolvido com a ferramenta. Ah,

03:26

eu preciso de um log, crio uma ferramenta. Preciso consultar um esquema, crio uma ferramenta.

03:30

Para tudo, crio uma ferramenta. Então, quando a gente está falando disso,

03:34

a ideia é a gente parar de fazer isso e a gente pensar como arquitetura.

03:38

Como que você vai entender a diferença entre constar um estado e executar uma ação? Então,

03:43

a grande diferença aqui. Quando você transforma a leitura de dado em uma ferramenta,

03:47

você está obrigando o modelo ali a raciocinar sobre o

03:50

que ele deve chamar ou não para aquela função.

03:52

Isso vai gerar dois problemas em produção. Um deles,

03:55

aumento de alucinação, para quem já fez isso, já viu acontecendo,

03:59

você dá as opções ali de execução,

04:02

mas ele não precisava executar, ele só precisava ler aquele negócio.

04:06

Outra coisa é o desperdício de token.

04:08

Cada definição de ferramenta vai acabar consumindo uma

04:11

janela de contexto gigante e agressiva aqui.

04:13

Isso eu estou falando para você construir agentes no seu sistema,

04:16

mas se você está construindo agentes copilotos também vai te atrapalhar.

04:18

Ter essa organização também ajuda muito, tá gente?

04:21

Então essa distinção aqui semântica que a gente está discutindo

04:25

é o que a gente vai aprender nessa aula,

04:27

beleza? Vamos em frente, vamos começar a aprender um pouco mais sobre isso.

04:30

Então vamos começar imaginando que você está em uma biblioteca.

04:33

E antes de você começar a tomar a decisão, fazer qualquer coisa,

04:37

você precisa consultar quais são os livros na

04:39

prateleira que fazem sentido para você.

04:41

Quando a gente está falando do MCP, os resources são esses livros, tá? Então,

04:46

eles são, por definição, os dados que o seu servidor está dando para você,

04:51

exclusivamente para que a IA possa ler ali e

04:54

pensar nele como conteúdo que vai ser consultado na aplicação, beleza?

05:00

Pode ser um arquivo de log que acabou de ser gerado ali,

05:03

pode ser um arquivo de configuração,

05:04

um .env, pode ser uma tabela de preço dinâmica que muda a cada hora,

05:09

pode ser tudo isso.

05:11

Diferente de uma função que você chama,

05:13

O resource vai estar lá e ele é passivo, ele não é ativo.

05:18

Ele serve para fornecer para você a base de

05:21

conhecimento que você vai precisar para trabalhar.

05:23

Essa é a grande diferença.

05:25

O modelo não precisa adivinhar e daí você corre menos risco dele alucinar também. Então,

05:30

aqui a gente está falando de uma base

05:33

controlada para você conseguir buscar informações.

05:37

Antes da gente dar o próximo passo,

05:39

vamos falar um pouquinho da semântica da URI, tá bom? Então,

05:44

a gente vai falar um pouquinho desse assunto que é super importante.

05:46

O que é URI? URI é Uniform Resource Identifier, beleza?

05:51

Então imagina que como arquiteto a gente acaba gostando pra caramba de padrões,

05:56

né? Então aqui que está a elegância do MCP.

05:59

Todo resource vai ser identificado através de uma URI, ou seja, de um identificador.

06:06

Um identificador uniforme que vai ajudar você a

06:10

entender do que a gente está falando.

06:11

Então a gente não está falando aqui de caminhos aleatórios de arquivo.

06:15

A gente está falando de identificador estruturado.

06:18

Por exemplo, um Postgres ou um Database ali,

06:21

etc., para a gente conseguir achar cada um desses pontos, tá bom?

06:25

Por que é um divisor de águas? Porque com essa URI,

06:29

a gente consegue carregar a semântica por trás disso. Quando o modelo de ar,

06:34

ele vê a estrutura que a gente tem,

06:35

ele entende imediatamente qual é a hierarquia e a

06:38

localização do dado que ele está precisando,

06:41

e ele sabe que Customers está dentro da Database,

06:46

por exemplo. Então, ele consegue achar isso. Então,

06:48

isso vai permitir que o modelo fique navegando ali pelos

06:51

dados de uma forma lógica e não alucinadamente,

06:54

de um jeito maluco, buscando do jeito que ele acha que tem que buscar.

06:58

Então, a gente traz lógica para essa execução.

07:00

Então, é como se fosse um desenvolvedor navegando,

07:02

mas com uma estrutura de diretório bem organizada ou com um indexador, um índice,

07:07

que consiga mostrar para ele onde está cada coisa. Então,

07:11

é o fim daquela confusão de onde está o quê.

07:14

Imagina uma mesa toda bagunçada.

07:16

Diferente de uma gaveta organizada ou de um arquivo organizado. Essa é a grande diferença.

07:21

Vamos fazer uma analogia, gente?

07:23

Imagina o GET, o protocolo GET.

07:26

Se a gente parar para pensar, para quem está acostumado com Web API,

07:30

REST, pensa no resource como se fosse um GET do protocolo.

07:34

Ele vai servir para leitura.

07:36

Ele vai fazer uma leitura e contextualização do que você precisa fazer.

07:39

É um modelo que não vai executar.

07:43

É um modelo... que ele consome para entender o mundo ao redor dele.

07:47

Se não tem alteração de estado no banco de dados,

07:50

não tem disparo de e-mail, por exemplo. Provavelmente,

07:53

o que você precisa é de um resource e não de um ato.

07:56

Quando a gente está falando disso tudo que a gente comentou até agora,

08:00

A gente precisa manter essa distinção limpa na sua arquitetura,

08:03

para garantir que a IA saiba quando ela está só observando o

08:07

ambiente e quando ela precisa de fato agir sobre o ambiente.

08:10

Essa é uma grande separação. Tá bom?

08:13

Deixa eu dar mais um exemplo prático para vocês.

08:15

Então, pense o seguinte. Um exemplo que eu acho matador aqui.

08:19

A gente usa muita ferramenta de produtividade, certo? Então,

08:22

imagina que você expôs ali todo o seu código fonte de

08:25

um repositório ali e o LLM pode folhear esse código.

08:29

Ele pode ler as classes, entender dependências,

08:31

mapear o projeto e assim por diante. Tudo isso consumindo via resource.

08:35

Então, antes de usar uma tool para realizar,

08:37

por exemplo, para fazer um refactoring de alguma coisa,

08:41

ou para abrir um pull request e assim por diante,

08:44

você dá visão à máquina antes de dar o comando de execução.

08:48

Então, agora você já consegue entender como é que você dá a

08:52

visão via resources para depois sim você usar as mãos,

08:55

como a gente comentou lá atrás, para fazer as execuções. Beleza? Bom,

08:59

pessoal, agora que a gente já falou um pouquinho dos resources,

09:02

vamos aprender um pouquinho, então,

09:03

como é que funciona as mãos do seu sistema, né? A gente falou ali dos olhos, então,

09:08

ele já consegue entender onde ele está localizado, qual o contexto dele.

09:12

Agora, vamos falar um pouquinho de como ele executa as coisas.

09:15

Então, a gente está falando aqui em como transformar a intenção,

09:19

certo? Do modelo em realidade.

09:22

Então, a gente está falando de como ele vai

09:23

executar algo para te entregar alguma coisa.

09:26

Quando a gente está falando de MCP,

09:27

a gente vai chamar as tools como se fosse um músculo,

09:32

e isso tem um motivo, elas são feitas para agir.

09:35

Enquanto o resource vai ser só para ver, para ler, etc., o tool faz, beleza? Então,

09:41

se você precisa que o modelo vá interagir com o sistema externo,

09:44

que ele faça, deixa eu ver,

09:46

um cálculo pesado, por exemplo, ele precisa...

09:48

fazer um cálculo complexo e assim por diante,

09:50

ou precisa alterar algum registro, ou você precisa, sei lá, calcular a ROI,

09:57

que você precisa ter uma regra clara e assim por diante,

09:59

você está indo para uma tool, certo?

10:02

Então, você já está saindo do contexto de resources e indo para um executável.

10:07

Então, beleza. Aqui, a conversa fica um pouco mais séria,

10:11

porque você precisa gerenciar na arquitetura do MCP.

10:15

Não apenas uma função de leitura, mas ela precisa ter um contrato mais rigoroso.

10:20

Então, o servidor anuncia para o host,

10:23

olha, eu possuo uma função, por exemplo, de mandar e-mail, um send e-mail da vida,

10:28

e ela precisa que você me mande alguns parâmetros.

10:31

Eu preciso saber para quem, preciso saber o subject,

10:35

preciso saber o body disso. Então, esse anúncio não é feito só em linguagem natural.

10:42

Ele acaba sendo feito em um esquema de JSON. Então,

10:45

a gente precisa ter um pouquinho disso para fazer a coisa funcionar.

10:48

Por que isso é tão importante? Porque quando a gente está falando do JSON,

10:52

O esquema vai garantir que a LLM... ela receba uma definição técnica precisa. Bom,

10:58

a gente sabe que uma LLM pode abrir ali a

11:01

sua linha de raciocínio e ir inventando coisas,

11:04

fazendo o que ela acha que faz mais sentido. Lógico,

11:06

você consegue controlar isso ali com o top P,

11:08

com o top K, mas aqui, quando a gente está falando da execução,

11:12

é legal você fechar isso. E quando você coloca um esquema do JSON,

11:16

você já deixa claro a definição técnica que é precisa,

11:19

ou seja, algo que você quer de forma mais...

11:22

determinística, vamos dizer dessa forma.

11:24

Ela sabe ali exatamente quais são os dados que ela precisa mandar.

11:27

Se são string, number,

11:29

se é booleano e assim por diante. Então,

11:31

quais são os campos que são obrigatórios para ela conseguir executar aquela tool.

11:36

Então, para a gente, isso significa ali,

11:38

a gente que está liderando tecnicamente ali no dia a dia,

11:40

a previsibilidade que você precisa.

11:42

Você vai conseguir definir uma interface ali do

11:44

modelo que é obrigatório ter respeito,

11:47

que ela não pode simplesmente sair quebrando para fazer

11:50

o que ela imaginar que faça sentido, tá? Então, é que a chamada,

11:53

ela consegue ser bem-sucedida quando a gente trabalha desse jeito.

11:57

Então, tá bom. Para facilitar o mapa mental ali com o que a gente já...

12:01

já conhece, de novo, eu sempre gosto de fazer esse paralelo,

12:04

pensa no mundo transacional que a gente tem ali de uma arquitetura,

12:07

uma web ali. Se o resource é o GET,

12:10

a tool é o POST, o PUT, o DELETE e assim por diante.

12:13

Então, é aquilo da nossa estrutura que está fazendo a alteração. Então,

12:16

a tool, ela vai ser como se fosse um transacional.

12:20

Ela existe para alterar o estado do sistema ou para realizar ali algum computing,

12:26

que vai fazer de forma ativa ali um resultado no output e assim por diante.

12:30

Ela não é passiva como a resource, ela é invocada,

12:34

algo acontece quando ela é chamada.

12:36

Então pode ser um e-mail que foi disparado, uma linha deletada no banco de dados,

12:40

um deploy que foi iniciado e assim por diante.

12:43

Então, na teoria ali, é a transição do que a gente

12:48

está dizendo que era até então um teórico para um contexto prático, para uma ação.

12:53

Então aqui basicamente é isso que separa os resources de tool e é por isso que

12:59

é importante a gente ter essa camada de separação

13:02

para você conseguir trabalhar da melhor forma possível.

## Resumo IA

[RESUMO_IA]