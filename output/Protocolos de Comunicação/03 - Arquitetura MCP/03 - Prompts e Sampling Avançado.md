Módulo: Protocolos de Comunicação\
Aula: [Prompts e Sampling Avançado](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18594)

## Resumo da aula

Resources e tools já resolvem leitura de contexto e execução, mas esse arranjo ainda produz um sistema predominantemente reativo. Operações complexas exigem também uma forma padronizada de orientar a interação com o modelo e de reintroduzir inferência quando a lógica determinística não basta. É nesse ponto que prompts e sampling ampliam a arquitetura do MCP. Eles transformam o fluxo de dados em uma via de mão dupla, em vez de um simples comando do host seguido por execução do server.

No MCP, prompt não é texto solto copiado para um chat; ele é um primitivo formal exposto pelo server. Isso significa que o prompt passa a ter nome, descrição, interface definida e versionamento, tornando-se um artefato estável do sistema. Em vez de entregar apenas palavras, o server publica uma interação pré-configurada que o host e o modelo conseguem interpretar de forma previsível. Essa formalização reduz improviso e torna o uso de IA parte explícita do contrato arquitetural.

Concentrar prompts no server evita espalhar lógica de interação por front-ends, extensões e aplicações clientes. Retomando o cenário de um server de Code Review, uma mudança de regra de estilo ou a descoberta de um novo edge case de segurança exige alteração em um único ponto, e todos os hosts conectados passam a consumir a versão atualizada. Essa centralização melhora governança, reduz divergência entre interfaces e cria uma base operacional para evoluir prompts sem reimplementar a aplicação inteira. O resultado prático é uma arquitetura mais modular e menos propensa a virar um agente monolítico.

PromptOps é a disciplina operacional de tratar prompts como ativos versionados, governáveis e distribuíveis, e não como strings escondidas no código. Quando os prompts vivem no server, sua evolução passa a seguir um fluxo controlado de atualização, revisão e propagação para todos os consumidores. Isso viabiliza consistência entre ambientes e reduz o custo de manutenção em times grandes. Sem essa camada, cada front-end tende a carregar sua própria variante do comportamento semântico.

Prompts no MCP podem aceitar argumentos, o que os aproxima mais de uma interface do que de um texto fixo. Se o server publica um template de análise de bug que exige um logId, o host pode gerar automaticamente uma interface de preenchimento com base nesse contrato. Em cenários mais elegantes, esse parâmetro pode ser obtido a partir de resources já disponíveis, fundindo instrução e dado sem costura manual de strings. A consequência é um fluxo menos frágil, com menor fricção cognitiva para usuários e desenvolvedores.

Quando o server publica prompts reutilizáveis, ele deixa de ser apenas executor e passa a orientar o uso correto das próprias capacidades. Em vez de exigir que cada pessoa memorize a melhor formulação para uma tarefa, o sistema oferece perguntas prontas e de alta qualidade, alinhadas ao domínio. Isso reduz variabilidade de uso e melhora a consistência dos resultados. A inteligência de interação deixa de ficar concentrada na aplicação principal e passa a acompanhar o contexto do próprio domínio encapsulado pelo server.

Sampling é o fluxo em que o server, durante sua própria execução, pede ao host que consulte o modelo para resolver uma ambiguidade semântica. A direção da iniciativa muda: antes o host chamava o server; agora o server também pode solicitar inferência de volta ao host. Essa inversão de controle permite injetar capacidade probabilística dentro de um fluxo determinístico sem transformar toda a aplicação em um agente opaco. O server passa a saber quando o código basta e quando precisa delegar uma subtarefa cognitiva ao modelo.

Sampling é especialmente útil quando o volume de dados é grande demais para ser enviado integralmente ao modelo. Retomando o cenário de um log gigantesco, o server pode processar o arquivo localmente, extrair apenas um trecho suspeito e perguntar ao modelo se aquilo parece, por exemplo, um estouro de memória. O modelo atua como filtro semântico local, ajudando a separar sinal de ruído sem consumir contexto desnecessário. Isso reduz custo, evita desperdício de tokens e preserva a janela de contexto para o que realmente importa.

Ao usar sampling em subtarefas de baixo nível, o server ganha autonomia para continuar o fluxo sem intervenção humana a cada passo. Essa autonomia não substitui decisões de alto nível; ela apenas resolve ambiguidades técnicas que um if-else ou switch-case não consegue tratar bem. O efeito arquitetural é um back-end menos dependente de intervenção manual e mais capaz de operar continuamente. Ainda assim, a decisão de escalar para human in the loop continua sendo parte da governança do host.

Cada chamada de sampling deve ser tratada como uma subtarefa governável, com modelo, temperatura e limite de tokens definidos conforme o objetivo. Uma classificação binária rápida pode usar um modelo simples e barato com temperatura zero, enquanto uma análise mais sofisticada pode justificar um modelo mais potente. Esse controle evita que toda inferência seja tratada com o mesmo custo e o mesmo perfil de risco. Governança, aqui, não é apenas segurança; é também engenharia econômica da inferência.

Sampling só faz sentido quando o server encontra uma barreira semântica que o código determinístico não resolve de forma adequada. Classificar linguagem natural, resumir texto para extrair um parâmetro ou desambiguar significado são bons candidatos. Regra de negócio expressável com if-else ou switch-case não deve ser terceirizada para LLM, porque código determinístico é mais barato, mais previsível e mais seguro. A LLM entra como especialista de plantão, não como substituta indiscriminada da lógica de software.

Ao permitir que o server peça sampling e que o modelo, em resposta, acione tools que disparam novos samplings, a arquitetura abre espaço para recursão operacional. Sem limites explícitos, esse encadeamento pode formar loops infinitos de chamadas, elevando custo e degradando o sistema. Por isso, fluxos MCP com sampling exigem guardrails como profundidade máxima de recursão, circuit breaking, observabilidade e monitoramento de custo em tempo real por sessão. Autonomia sem supervisão vira risco financeiro e arquitetural.

A combinação de prompts estruturados com sampling desloca a arquitetura de um modelo centralizado no host para uma inteligência distribuída entre componentes. O host continua soberano na governança, mas o server passa a carregar parte da semântica operacional: publica interações reutilizáveis e solicita inferência quando necessário. Esse desenho evita o acúmulo de lógica em um único ponto e aproxima o ecossistema MCP de uma modularidade comparável à de sistemas orientados a serviços. O ganho não é apenas técnico; é capacidade de evoluir, trocar modelos e escalar sem reconstruir toda a integração.

## Transcrição

00:00

Fala galera, beleza? Vamos dar mais um passo então aqui no nosso curso.

00:04

A gente está chegando aqui num ponto de virada, né?

00:07

A gente já aprendeu aqui como é que a gente cuida dos resources ali,

00:11

do que a gente chamou de olhos,

00:13

para a gente conseguir enxergar os dados que a gente tem,

00:15

e as tools que são as mãos ali para executar as ações.

00:20

Beleza, a gente já está equipado com isso.

00:22

Mas se a gente parar por aqui,

00:23

a gente tem um sistema que só reage. Não é um sistema bem determinado,

00:27

nem um sistema que a gente precisa para uma operação complexa no dia a dia.

00:32

A gente sabe que uma operação complexa precisa de mais do que ferramenta.

00:35

A gente precisa de padrão de comunicação, é super importante.

00:38

Então a peça que está faltando aqui é como que a gente vai

00:41

padronizar a forma como a IA vai interagir com o usuário.

00:45

Ou até mais do que isso, como que a gente permite que o servidor...

00:49

no meio aqui de uma tarefa pesada, então ele está lá executando,

00:53

no meio de uma tarefa ele dá um passo para

00:55

trás e pede um favor cognitivo para o modelo.

01:00

Então, a gente precisa começar a entrar agora num terreno

01:02

aqui que é dos prompts e do sampling.

01:04

A gente vai falar um pouquinho disso,

01:06

tá? Então, quando a gente está falando desse negócio,

01:08

a gente precisa pensar um pouco na via de mão dupla.

01:11

Então, a gente vai elevar aqui o nível da conversa sobre arquitetura

01:14

e vai falar um pouco no MCP o fluxo de dados.

01:18

Que não é uma via de mão única, onde o host vai lá,

01:21

manda, o servidor obedece e pronto. Não é assim que funciona.

01:24

A gente está saindo de um paradigma de um servidor

01:27

escravo para um servidor que ele é consultor.

01:30

Então, com prompt,

01:31

a gente consegue pegar o servidor que vai passar a sugerir ali templates, fluxo de trabalho,

01:38

guiando o usuário sobre como a ferramenta deve ser usada da melhor maneira.

01:42

Beleza? E com o sampling,

01:44

o jogo inverte. O servidor ao encontrar alguma ambiguidade,

01:48

alguma coisa que ele precisa de classificação semântica, por exemplo,

01:51

ele vai solicitar para a inteligência de volta ali para o modelo através do host.

01:56

Então a gente consegue ter uma via de mão dupla funcionando.

01:59

Isso muda tudo que a gente está falando.

02:00

O servidor deixa de ser só um executor de código e começa a ser um

02:04

parceiro que sabe quando a lógica determinística está falhando

02:07

e onde a lógica probabilística deve entrar.

02:11

E daí com isso a gente consegue ter uma arquitetura complexa e que funciona.

02:15

Então, a gente começa a ter aqui o que eu chamo de tese da inteligência distribuída. Então,

02:21

com essa tese central,

02:23

a gente precisa começar a elevar aqui o design dos nossos sistemas.

02:28

A inteligência não precisa e não deve

02:33

estar concentrada e centralizada só no host. Então,

02:37

a gente vai tentar mudar aqui e não colocar toda a lógica de prompt,

02:41

toda a camada de decisão dentro da sua aplicação principal.

02:44

Senão você vai acabar tendo um monolítico agente.

02:46

Imagina coisa horrível. Então um agente monolítico, coisa péssima.

02:50

Então a gente vai ter dificuldade de manter se a gente fizer desse jeito.

02:54

Quando a gente distribui essa inteligência,

02:56

a gente deixa cada servidor MCP gerenciar os próprios templates,

03:00

solicitar o próprio refinamento ali via sampling.

03:03

E daí com isso você tem uma arquitetura modular.

03:06

que é mais ou menos o que a gente faz

03:07

quando a gente está falando de microserviços também.

03:08

Então, você consegue ser escalável,

03:10

consegue ter mais resiliência, consegue mudar o modelo. Então,

03:13

é disso que a gente vai falar agora nessa aula.

03:16

Então, vamos lá. Vamos desmistificar aqui um conceito.

03:22

No MCP, quando a gente está falando do MCP,

03:24

um prompt não é só um bloco de texto solto que você

03:26

copia de um bloco de notas e cola no chat,

03:29

igual a gente está acostumado quando a gente está falando ali de uso de Gemini,

03:33

uso do DeepSeek, GPT e assim por diante. Não é igual você faz em casa,

03:38

você não vai chegar lá, copiar o negócio do bloco de notas e colar.

03:41

Ele é elevado à categoria de primitivo,

03:44

como a gente falou anteriormente, certo? Então o que significa?

03:47

Que o prompt é um template estruturado e versionado. Então,

03:52

o seu servidor ali, ele vai oferecer esse prompt ao host, certo?

03:57

A gente já entendeu esse pedaço que é o que a gente falou nas duas últimas aulas.

04:01

Então, ele tem que possuir um nome ali,

04:02

descrição e principalmente uma interface definida. Ele vira um arquivo,

04:06

um atributo, um pedaço do seu sistema.

04:09

O servidor não vai entregar apenas as palavras,

04:11

ele entrega uma interação pré-configurada que o

04:14

modelo de IA já sabe como interpretar. Beleza?

04:19

Então, esse é o primeiro ponto que a gente tem que fechar aqui.

04:22

Outra coisa que a gente tem que pensar,

04:24

em como deixar a

04:25

manutenibilidade centralizada.

04:33

Quando a gente fala disso, a gente tem que pensar no seguinte,

04:35

como que eu vou deixar isso aqui,

04:39

tirando a lógica do prompt e do meu front-end, para colocar no servidor MCP.

04:45

Bom, se a gente fizer isso,

04:47

a gente consegue deixar com essa manutenibilidade centralizada.

04:54

Então, imagina que você tem um servidor ali de Code Review,

04:57

certo? E as regras no estilo da sua empresa mudam.

05:00

Ou você descobriu que tem um novo Edge ali, um case de segurança.

05:04

Você altera o servidor apenas, você altera o prompt apenas no servidor.

05:09

Você não precisa alterar em todos os lugares.

05:12

Então, instantaneamente, todos os hosts...

05:14

Seja ele um Cloud Desktop de um desenvolvedor,

05:17

um VS Code ou qualquer outra plataforma que está batendo ali, que o time construiu,

05:22

vai receber essa atualização e você ganha em governança.

05:26

Então você tem um prompt ops aqui,

05:28

que é impossível de alcançar se os prompts

05:30

estiverem espalhados pelo código do front-end. Ou seja,

05:32

Cada um estiver jogando esse prompt ali dentro do seu

05:35

front e não eles centralizados dentro de uma camada,

05:39

você vai acabar tendo essa dificuldade de atualização no futuro.

05:43

Então nesse tipo de ideia a gente consegue trazer,

05:47

eu não vou falar essa palavra de novo porque está difícil de sair, né?

05:51

Manutenibilidade. Poxa, olha, boa palavrinha.

05:54

Então bom, esse é um dos pontos que a gente tem que pensar.

05:58

Esses prompts também não são estáticos, eles têm que ser inteligentes,

06:03

então eles aceitam argumentos. O servidor ali,

06:05

ele anuncia para o mundo, tem um template que é, sei lá, análise de bug, beleza?

06:12

E ele vai precisar aqui de um log ID. O host,

06:15

quando lê esse contrato,

06:16

ele pode montar automaticamente uma interface para o usuário preencher.

06:20

Ou seja, você está vendo? A gente não está mais falando de um fluxo determinístico,

06:23

você tem que ter isso fechado. Você tem uma troca,

06:25

você tem uma interação, as coisas vão sendo construídas.

06:28

De forma ainda mais elegante, se a gente parar para pensar aqui...

06:32

ele pode buscar esse log ID diretamente ali e ver os recursos.

06:36

Então, ao invés de pedir para o usuário, ele pode pegar os recursos,

06:39

que são os olhos que a gente falou,

06:40

e lá buscar para ver se ele não acha isso.

06:42

E com isso ele cria um fluxo onde o dado e a

06:46

instrução vão se fundir sem que o desenvolvedor precise ir lá e criar,

06:51

costurar uma string manualmente no código. Então,

06:55

você está deixando isso de forma mais aberta, beleza?

06:59

Então... Aqui, quando a gente começa a olhar para esse ponto,

07:02

é importante porque você diminui a fricção cognitiva.

07:07

Ou seja, aqui, quando a gente está falando dessa utilização,

07:11

a gente não tem mais um prompt ali. Quer dizer,

07:15

a gente tem um prompt ali que está movido para o servidor

07:17

e você está oferecendo as perguntas prontas e de alta qualidade.

07:21

Você reduz a carga cognitiva do time e eles não

07:24

precisam ficar aprendendo a sequência de prompt ou precisam escolher,

07:28

eles precisam só escolher a ferramenta certa de trabalho no final

07:30

do dia e o servidor vai guiar o resto.

07:34

Se você colocar isso dentro da sua camada ali,

07:35

da sua aplicação, a mesma situação.

07:38

Ele vai seguir usando ali o que você deixou determinado.

07:44

E com uma prateleira ali,

07:45

uma ferramenta de prateleira mais confiável. Beleza?

07:48

Agora vamos falar um pouquinho do sampling.

07:50

Quando a gente está falando do sampling, gente,

07:52

é um conceito um pouquinho mais chato.

07:55

A gente tem que inverter a nossa linha de raciocínio do

07:59

que a gente aprendeu até agora com o MCP.

08:02

Antes, antes do sampling,

08:03

a gente estava falando só de um sistema que ele tem só um fluxo linear, né? É só de uma mão.

08:09

Então, ele vai ali nesse fluxo. Então, o host vai pedir alguma coisa,

08:12

o servidor vai lá, responde. No sampling, a gente inverte.

08:17

Daí, a gente tem que pensar o seguinte.

08:19

Vamos dar um case aqui para ficar mais fácil.

08:21

O server pediu alguma coisa lá para a LLM através do host, beleza?

08:26

Imagina que o seu código de back-end, no meio da execução,

08:29

a sua LLM chamou lá uma API, e o seu código,

08:32

no meio da execução, chegou num ponto de decisão semântica,

08:34

ali num if-else que ele tinha, que não resolve. Ele travou ali,

08:39

ele não sabe o que fazer. Ou seja,

08:41

em vez de retornar um erro ou tentar adivinhar como sair desse problema,

08:44

o servidor vai mandar uma mensagem de volta, falando host,

08:48

pergunta aí para o modelo o que eu tenho que

08:50

fazer com esse dado aqui que eu não sei.

08:52

Aqui que é a inteligência do modelo que está sendo injetada

08:56

diretamente no fluxo de execução dentro do seu servidor,

08:58

sem precisar dar um problema,

09:00

dar um erro e fazer o seu desenvolvedor entrar para trabalhar aqui.

09:04

Então, esse é o primeiro ponto.

09:05

Essa inversão de controle, onde você está usando a LLM ao seu favor,

09:12

usando essa estratégia de sampling com o MCP. Aí você sai de uma via de mão única,

09:18

onde você só vai lá, faz a chamada da LLM, executa e volta,

09:22

e começa a ter uma mão dupla, onde essa execução, ela pode ser,

09:27

ter ida e volta, ida e volta, assim por diante, para fazer a coisa acontecer.

09:33

Agora vamos falar de um outro assunto que é super importante,

09:35

um processamento mais inteligente aqui,

09:37

tá bom? Quando a gente está falando de volume de dado grande.

09:41

Quando a gente está falando desse assunto,

09:42

a gente tem que pensar no seguinte. Primeira coisa,

09:44

primeira coisa. Imagina um servidor ali, por exemplo,

09:46

processando um log de erro gigantesco ali, 500 MB.

09:51

A gente sabe que é impossível e financeiramente até irresponsável a gente

09:55

mandar tudo isso para uma janela de contexto do modelo. Vai fritar.

09:59

É token e você possivelmente vai ter que atualizar seu LinkedIn,

10:02

certo? Então, quando a gente está falando do sampling,

10:05

o servidor vai poder ler o arquivo localmente e daí ele

10:09

vai extrair um trecho suspeito e perguntar ao LLM.

10:12

Isso aqui parece um estouro de memória?

10:15

Aí ele vai responder apenas sim ou não.

10:17

O servidor vai usar o cérebro do modelo para filtrar o

10:22

ruído e entregar para o usuário final o que é relevante.

10:25

Então você tem um fim de desperdício de token aqui com um dado que é inútil.

10:29

Você pode trabalhar desse jeito também.

10:31

Então esse é um ponto extremamente importante.

10:35

Tem uma outra coisa também que é importante a gente pensar,

10:37

é usando o embed, a parte aqui de embedada no back-end.

10:43

Quando a gente está falando disso,

10:45

a grande vantagem que a gente tem é que você dá autonomia agêntica.

10:48

O sampling permite que o servidor utilize a

10:52

inteligência do modelo para tomar decisão.

10:55

de baixo nível, quando ele está executando alguma tarefa,

10:58

sem que o usuário precise ficar intervindo a cada passo.

11:01

Não fica aquela necessidade de você estar ali respondendo a cada passo.

11:06

A gente não está mais falando de um IA que ela vai só responder perguntas.

11:09

A gente está falando de um IA que age dentro de uma lógica do seu back-end. Lembra disso.

11:13

O servidor vai ser capaz de resolver a ambiguidade técnica em

11:17

tempo real e vai permitir que o fluxo do trabalho vá seguindo.

11:21

Ele não precisa de você para tudo.

11:23

Ele vai seguindo autônomo lá até que a decisão de alto

11:28

nível ali seja realmente necessária para daí voltar para alguma pessoa,

11:33

algum human in the loop aqui.

11:35

Então essas são as coisas importantes da gente pensar.

11:38

Tem uma outra coisa também importante quando a gente está falando de sampling,

11:41

que é o controle de qualidade,

11:42

a governança ali das subtarefas que a gente está falando. Então primeiro,

11:47

como é que a gente vai garantir que essa conversa do

11:49

servidor com o modelo não vai fugir de controle? Ou seja,

11:52

não vai meter o louco e sair falando um monte de aleatoriedade,

11:56

queimar token e não ter nada de resposta ou até ter uma resposta nada a ver.

12:00

O MCP tem ali a capacidade de dar governança total.

12:04

Então o servidor pode especificar exatamente qual nível de

12:08

modelo que ele quer para aquela subtarefa.

12:11

Então, ele vai conseguir determinar, por exemplo,

12:13

parâmetro máximo de token, temperatura.

12:15

Se o servidor precisa de uma classificação binária rápida,

12:19

ele pode solicitar um modelo mais simples,

12:21

por exemplo, mais barato, com a temperatura zero.

12:24

Se ele precisar de uma análise criativa,

12:26

alguma coisa mais maluca de código,

12:27

ele pode pedir para um modelo mais potente e isso vai garantir que

12:31

a tarefa vai ser executada com a precisão que precisa ser executada.

12:35

Então, com isso, você consegue manter a engenharia ali sob controle. Pessoal!

12:39

Eu resolvi criar mais esse slide aqui só para contar

12:43

para vocês uma coisa que eu acho extremamente importante,

12:45

que agora que a gente está trabalhando com modelos mais complexos,

12:48

com esse tipo de arquitetura um pouco mais requintada, a gente precisa saber,

12:52

senão a gente vai fazer uma besteira gigantesca. Por quê?

12:55

Porque eu já vi algumas pessoas fazendo essa estratégia

12:58

de implementação e criando ali alguns loops infinitos.

13:02

Então, em alguns testes que eu já vi acontecendo,

13:04

a galera começa a rodar e vê que a estratégia de sampling,

13:07

principalmente, começa a ficar numa recursão ali. E daí, com isso,

13:12

a gente acaba torrando o token e fazendo com que não dê certo, tá?

13:16

Então, a primeira coisa é que a gente tem que pensar o seguinte.

13:19

Quando a gente está trabalhando com sampling,

13:21

a gente abre uma porta para um fluxo aqui de uma complexidade que é gigantesca,

13:26

certo? Então, imagina o cenário aqui.

13:28

O seu servidor ali pede um sampling para o modelo.

13:33

O modelo para de responder e decide invocar o ato.

13:36

Essa ação executa o código e daí, por sua vez, ela dispara outro sampling.

13:40

Olha onde a gente entrou. Se a gente não for criterioso,

13:42

a gente cria um loop infinito de chamadas que vai derreter o seu cartão de crédito.

13:47

Vai fazer a sua empresa torrar a grana.

13:50

Isso se você não estiver fazendo um teste em casa, senão você vai torrar uma grana.

13:53

Então, a gente tem que pensar no seguinte. Como que eu desenho guardrails aqui?

13:58

Para a gente conseguir implementar,

13:59

mas com limite de profundidade de recursão e com monitoramento de custo.

14:04

E esse monitoramento de custo não é um painelzinho que você vai

14:07

entrar uma vez por mês quando o seu chefe cobrar.

14:10

Aqui é um painel de custo em tempo real para cada sessão.

14:14

E a autonomia da IA aqui vai ser celebrada,

14:19

mas sem deixar uma supervisão rigorosa em cima do que está acontecendo.

14:23

Esse é o ponto principal.

14:25

Então essas coisas a gente tem que ter na cabeça. Uma outra coisa para pensar,

14:29

fronteira de decisão de quando usar e quando não usar uma LLM.

14:34

Uma pergunta que vocês vão ouvir muito do time é onde eu coloco a lógica?

14:37

Como é que eu vou fazer isso?

14:39

A regra de ouro é que a decisão de usar

14:42

um sampling deve ser estritamente técnica e de semântica.

14:46

O sampling tem que aparecer quando o servidor encontrar

14:49

uma barreira que o código não consegue resolver.

14:51

Se não for isso, você não precisa do sampling. Então,

14:54

como classificar o sentimento, por exemplo, de um log,

14:56

resumir um documento para extrair um parâmetro,

14:59

resolver uma ambiguidade de linguagem natural e assim por diante?

15:01

Você não vai usar o sampling para uma lógica de

15:03

negócio que dá para resolver com if-else.

15:06

Ou com switch case, por exemplo. A primeira coisa que você tem que pensar,

15:09

gente, é que se der para resolver com if-else,

15:12

é if-else. Não é para querer inventar de usar sampling,

15:14

usar LLM e assim por diante.

15:16

O determinístico do código é mais barato, sempre foi.

15:19

É mais seguro. O LLM tem que ser usado.

15:23

Como especialista de plantão para coisa complexa,

15:25

coisa que o motor de regra básica não consegue fazer, tá bom?

15:30

Outra coisa para a gente pensar também, nada de puxadinho.

15:34

A infraestrutura que a gente está fazendo é uma infraestrutura,

15:37

uma arquitetura aqui de elite.

15:38

Então, a gente precisa dominar aquela trilha de tool, resources,

15:43

prompt e o sampling aqui entrando no meio do caminho.

15:47

O que significa que a gente está separando aqui

15:49

aquelas integrações que eram feitas de qualquer jeito,

15:52

de puxadinho e assim por diante.

15:54

O MCP está dando para a gente e a ferramenta para a gente

15:57

conseguir construir o sistema onde a inteligência

16:00

está distribuída de forma inteligente mesmo,

16:03

segura, escalável. Agora que você entendeu isso,

16:06

você consegue ter um mapa para você construir o seu ecossistema real.

16:11

Beleza? Espero que vocês tenham gostado da aula. Um grande abraço!

## Resumo IA

[RESUMO_IA]