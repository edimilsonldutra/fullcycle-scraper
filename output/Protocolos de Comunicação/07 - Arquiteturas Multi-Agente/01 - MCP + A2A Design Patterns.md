Módulo: Protocolos de Comunicação\
Aula: [MCP + A2A: Design Patterns](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18624)

## Resumo da aula

Patterns funcionam como vocabulário arquitetural porque descrevem responsabilidades e formas de coordenação sem prender a conversa ao detalhe de implementação. Dizer que um sistema é delegado, hierárquico ou pipeline comunica imediatamente como os agentes se organizam, onde está a decisão e como a falha deve ser tratada. Isso reduz ambiguidade entre times e evita a “arquitetura da fofoca”, em que um agente chama outro sem contrato claro, sem previsibilidade e sem fronteiras de responsabilidade. Nessa separação, MCP abstrai as ferramentas, A2A abstrai a comunicação e o pattern define a estratégia de composição.

O padrão delegado é um roteador de intenção: um agente principal recebe a solicitação, identifica o domínio correto e encaminha para o agente especialista adequado. Ele existe para cenários em que uma mesma entrada pode cair em áreas muito diferentes, como um assistente corporativo que precisa decidir entre RH, jurídico e TI. O ganho central está em ativar apenas o agente com a skill e as tools corretas, reduzindo desperdício de contexto, risco de alucinação e exposição indevida de acesso. Nesse modelo, o agente principal se comporta como um intent router, não como o executor do trabalho especializado.

A delegação só funciona bem quando o roteamento é guiado por descoberta de skill, e não por heurísticas frágeis. Agent cards cumprem esse papel ao explicitar o que cada agente faz, quais contratos oferece e em que tipo de tarefa deve ser acionado. Isso evita que o roteador “adivinhe” capacidades com base em palavras soltas e permite trocar ou evoluir especialistas sem reescrever toda a lógica de coordenação. O resultado é um sistema mais previsível e com acoplamento menor entre decisão e execução.

O principal antipattern do delegado acontece quando o agente principal para de rotear e tenta resolver tudo sozinho. Nesse ponto, a arquitetura volta a se comportar como um monólito disfarçado, concentrando contexto, aumentando alucinação e anulando a especialização dos nós. Outro erro comum é usar if/else por palavra-chave, como mapear “férias” diretamente para RH; isso parece simples no início, mas quebra assim que a linguagem do usuário varia ou que as fronteiras entre domínios ficam ambíguas. Delegação madura depende de contratos explícitos de capability, não de adivinhação lexical.

O padrão hierárquico organiza um coordenador acima de vários especialistas que trabalham em paralelo e devolvem pareceres para síntese. Ele resolve problemas em que uma única resposta depende da combinação de visões distintas, como uma due diligence que exige análise técnica, jurídica e financeira ao mesmo tempo. O coordenador não é o especialista do conteúdo; sua função é planejar, distribuir, consolidar e resolver conflitos entre respostas parciais. A arquitetura deixa de buscar “quem responde” e passa a buscar “como combinar respostas especializadas em um parecer único”.

Síntese é a capacidade de transformar respostas potencialmente conflitantes em uma saída coerente e útil para o usuário. No cenário de due diligence, o jurídico pode considerar a empresa segura enquanto o financeiro detecta risco de caixa; sem coordenação, cada resposta isolada seria apenas uma verdade parcial. O coordenador existe para reconciliar essas tensões e produzir uma visão completa do negócio, em vez de escolher arbitrariamente um lado. Esse padrão é adequado quando a qualidade da resposta depende mais da composição entre domínios do que do roteamento inicial.

Retomando o cenário de due diligence, os especialistas podem trabalhar em paralelo, de modo que a latência total tende a ser limitada pelo worker mais lento, e não pela soma de todos. O coordenador enxerga cada worker como caixa-preta por meio de contratos e agent cards, o que preserva acoplamento fraco e permite substituir um especialista sem reescrever a orquestração. Como falhas parciais são inevitáveis em sistemas distribuídos, graceful degradation impede que a queda de um worker derrube toda a execução. Em vez de interromper tudo, o sistema entrega o máximo de valor possível e explicita quais partes ficaram indisponíveis.

O pipeline é uma cadeia sequencial em que cada agente transforma o estado recebido e entrega o resultado para a próxima etapa. Ele é apropriado quando a ordem importa e cada fase depende diretamente da saída anterior, como no fluxo de newsletter: fazer scraping, resumir, traduzir e publicar. Aqui não há síntese entre opiniões nem um coordenador central consolidando pareceres; há uma linha de montagem de dados em que cada nó executa uma transformação específica. O valor do padrão está na clareza do fluxo e na separação rigorosa entre etapas.

Cada etapa do pipeline deve conhecer apenas o formato de entrada que consome e o formato de saída que produz. Isso permite, por exemplo, trocar um scraper por um leitor de PDF sem alterar o agente de tradução, desde que o contrato intermediário permaneça estável. A estrutura reforça responsabilidade única: um agente extrai, outro resume, outro traduz, outro publica. Essa especialização aumenta precisão e facilita evolução incremental, mas também introduz latência acumulada porque o fluxo é sequencial.

A diferença central é geométrica e semântica ao mesmo tempo. O hierárquico diverge para vários especialistas e depois converge em uma síntese; o pipeline segue linearmente, etapa após etapa, sem agregação de perspectivas. No hierárquico, o problema é combinar opiniões especializadas; no pipeline, o problema é transformar um artefato ao longo de estados sucessivos. Se uma etapa posterior precisar voltar e consultar arbitrariamente uma anterior, a linearidade se rompe e surgem dependências circulares que descaracterizam o pipeline.

Use delegado quando a principal dificuldade for decidir qual especialista deve assumir a solicitação. Use hierárquico quando vários especialistas precisam trabalhar sobre o mesmo caso e alguém deve consolidar conflitos e produzir síntese. Use pipeline quando o trabalho é uma sequência de transformações em que a ordem é fixa e cada etapa prepara a próxima. A escolha correta não depende de qual pattern é “melhor”, mas de qual forma de coordenação reduz entropia, preserva contratos e entrega valor com menor complexidade operacional.

## Transcrição

00:00

Fala galera, beleza?

00:01

Natan Pasquarelli na área novamente, satisfação estar com vocês aqui,

00:06

dando mais uma aula, uma aula super importante aqui,

00:10

a gente vai falar um pouquinho sobre a parte de design patterns,

00:13

quando a gente está falando ali de utilização de MCP e Agent to Agent,

00:16

vamos falar um pouco disso, vamos falar dos padrões de composição ali de delegado,

00:20

hierárquico e pipeline, vamos aprofundar nesses temas,

00:23

mas antes da gente começar a entrar na nossa aula,

00:25

vamos lá, primeiro, estão gostando das aulas aí com o Isaac?

00:30

Aposto que então o Isaac é um cara muito fera.

00:32

Ele tem muito conhecimento para compartilhar.

00:34

Espero que vocês estejam gostando bastante do que ele está passando.

00:37

É um cara que conhece pra caramba.

00:38

E que tem muito a ensinar. No dia a dia eu aprendo muito com o Isaac também.

00:42

É um cara muito bom de conhecimento de AI.

00:44

Um cara que conhece demais. Sabe explicar muito bem também.

00:47

Então, vocês estão tendo aí a possibilidade de aprender

00:50

com um cara que eu admiro demais. Agora,

00:52

parando de rasgar a seda para o nosso querido amigo Isaac,

00:56

vamos ao que interessa. Vamos falar um pouquinho aqui sobre a nossa aula.

01:01

Então, onde a gente está agora?

01:02

A gente está falando agora aqui de MCP, Agent to Agent,

01:06

a gente vai aprofundar um pouquinho em Design Patterns e depois

01:09

disso a gente vai falar um pouquinho de LandGraph,

01:11

a parte ali de Agent SDK,

01:13

Observabilidade e a gente depois vai ali para a parte do projeto

01:17

e um recap final de domínios de arquiteturas multiagentes ali para vocês, beleza?

01:23

Então, vamos lá, MCP mais Agent to Agent,

01:26

como é que a gente fala sobre isso, pessoal? Falar um pouquinho de design patterns.

01:30

Então, a nossa agenda vai passar por esses cinco capítulos principais.

01:35

A primeira coisa que a gente tem que falar é o porquê dos padrões,

01:38

por que a gente define padrão,

01:40

por que a gente usa vocabulário compartilhado. Vamos relembrar isso.

01:43

Sei que você que está aqui,

01:45

possivelmente, já conhece bastante de arquitetura, já domina ali sistemas. E daí, com isso,

01:52

você já entende um pouquinho do porquê do vocabulário compartilhado. Mas vamos relembrar.

01:55

Caso você não esteja lembrando do porquê que a gente usa esses padrões.

01:59

Depois a gente vai falar um pouquinho do primeiro deles, que é o delegado,

02:01

então a gente vai falar um pouquinho depois do hierárquico,

02:04

depois a gente vai seguir para o pipeline,

02:05

e depois a gente vai falar um pouquinho de comparativos e antipatterns no final.

02:09

Cada um deles eu devo tocar um pouco no assunto de antipatterns também,

02:12

para já ficar colado ao seu respectivo,

02:15

mas no final a gente fala um pouquinho disso também,

02:17

de como é que a gente... foge dos erros principais que podem acontecer, tá bom?

02:21

Então o nosso roteiro aqui vai ser simples,

02:23

a gente vai falar basicamente de três padrões que resolvem 90%

02:27

dos problemas de arquitetura de multiagente que a gente tem,

02:30

que são esses aqui que eu acabei de falar para vocês,

02:32

e a gente vai falar um pouquinho de quando usar cada um deles e quando não usar.

02:36

Quando a gente pode não trazer aqui essa complexidade no dia a dia também.

02:40

Vamos lá, então...

02:42

Falando um pouquinho das arquiteturas de multiagentes,

02:45

o que a gente tem que pensar aqui?

02:47

Arquitetura, no final das contas, vocês sabem que eu adoro falar de arquitetura,

02:50

então, pô, ótimo capítulo para eu falar, né, gente?

02:53

Arquitetura, em essência,

02:55

vai ser a arte da gente gerenciar a entropia de um sistema,

02:58

certo? Então, quando a gente está falando de arquitetura,

03:00

a gente tem que ter essa arte na cabeça.

03:02

Se você descrever um sistema como um agente que chama o outro, teoricamente...

03:07

Você vai estar preso ali num nível de implementação, ou seja,

03:11

você está descrevendo ali um ruído que vai acontecer e não um sinal.

03:15

É o que eu chamo aqui de arquitetura da fofoca. Não há contrato,

03:19

você não tem responsabilidade clara e principalmente

03:21

você não tem previsibilidade de falha.

03:23

Você vai criar no final das contas uma dívida técnica que vai...

03:27

você paga com um bug de difícil rastreio. O que eu quero dizer com isso,

03:30

pessoal? Se você não começar definindo qual é o seu vocabulário,

03:34

como é que você vai organizar as coisas,

03:36

como é que você vai conversar sobre os assuntos,

03:38

você vai começar a falar cada uma língua e vai ser como se

03:42

você estivesse conversando com pessoas de vários países sem uma conhecer o outro.

03:47

Você precisa delimitar,

03:48

você precisa falar a mesma língua, você precisa trazer a arquitetura para a sala.

03:52

Então, quando a gente está falando aqui de arquitetura,

03:54

vai ser muito importante a gente começar a trabalhar vocabulário compartilhado,

03:59

a gente começar a falar a mesma língua, a gente começar a se entender.

04:02

No final das contas, a arquitetura é muito sobre a arte de se entender.

04:06

Costumo dizer que uma das linguagens mais difíceis que

04:09

a gente tem no mundo é a nossa,

04:10

é a língua portuguesa. A gente tem muita dificuldade de se entender,

04:13

por isso que vocês devem ficar em reuniões, atrás de reuniões,

04:16

que no final das contas são nada mais do que alinhamentos,

04:19

porque no final do dia estamos sempre desalinhados. E alinhar é uma arte.

04:23

Então, quando a gente está falando de arquitetura, sem mais delongas...

04:25

a gente está falando disso. Quando a gente adota aqui um design pattern,

04:29

por exemplo, de delegado, hierárquico ou pipeline,

04:31

a gente está aplicando uma abstração de alto nível.

04:33

A gente cria um modelo mental que vai ser compartilhado entre todos. Ou seja,

04:38

pensa mais ou menos assim. Quando a gente fala que a gente vai usar um hierárquico,

04:42

eu não estou dando a instrução do código, de como codar essa bagaça.

04:46

O que eu estou definindo é um contrato de responsabilidade.

04:48

Qual a estratégia que está por trás disso? Quando a gente fala isso, o time...

04:52

que detém esse conhecimento e entende instantaneamente que

04:55

é um nó central que vai orquestrar,

04:58

os nossos subordinados que vão ser executados.

05:00

E a gente vai falar um pouco mais disso,

05:01

por isso que a gente está aqui. Mas, basicamente, a partir desse momento,

05:04

todos vocês que estão assistindo essa aula já entendem do que a gente está falando.

05:07

A gente vai falar o que é o orquestrado,

05:09

no delegado, e na sequência, toda vez que vocês ouvirem falar do delegado,

05:15

vocês vão saber do que a gente está falando.

05:16

Então, todo time vai entender instantaneamente essa estratégia.

05:20

Então, a gente profissionaliza aqui o sistema.

05:23

E tira o time ali do que o código faz no detalhe, e coloca do porquê da arquitetura,

05:27

como é que a gente dita o comportamento do que vai ser feito.

05:31

Então, basicamente, vai ser isso.

05:33

Vamos lembrar aqui que o MCP vai ser a interface que vai abstrair as ferramentas,

05:37

ou seja, o que a gente faz,

05:39

e o A2A é o protocolo que abstrai a comunicação, o como a gente se compõe.

05:44

Os patterns que a gente está usando aqui são o

05:46

manual de instruções de como a gente conecta...

05:48

Lé com cré, não tem jeito melhor de explicar isso, certo pessoal?

05:51

Então vamos lá, a gente vai agora aprender a fazer isso.

05:55

Então a gente está falando aqui de três cenários reais que eu trouxe para vocês,

05:58

três cenários para a gente começar a compreender.

06:01

O caso 1 a gente está falando de um assistente corporativo,

06:04

um RH com jurídico e TI ali,

06:06

um assistente que está juntando três casinhas, RH, jurídico e TI.

06:10

Quando o usuário manda uma pergunta,

06:12

ela vai para um dos três com base na nossa intenção ali, beleza? Então,

06:16

esse daqui é o estágio delegado que a gente já vai aprofundar.

06:19

A gente tem o caso 2, que é o caso de due diligence,

06:22

que vai ser um técnico mais jurídico, mais financeiro ali, por exemplo,

06:25

onde cada especialista precisa opinar. Então, eles têm que falar sobre tal assunto,

06:31

eles vão opinar. A gente vai falar um pouco mais dele também.

06:33

Então, é esse o segundo caso que a gente vai trabalhar.

06:37

E aqui a gente está falando depois do caso 3, que é um caso de newsletter,

06:40

onde a gente tem que fazer scrap, depois resumir, traduzir, publicar, ou seja,

06:46

cada etapa transforma um pedacinho da coisa para o output de uma,

06:51

vai ser o input da outra e a ordem aqui importa,

06:54

é um pipeline, é uma sequência linear aqui de trabalho.

06:57

Então a gente está falando desses três.

07:00

Desses três cenários, esses três casos que são extremamente importantes,

07:03

já que resolvem a maior parte dos problemas do dia a dia, beleza?

07:07

Então, vamos começar a aprofundar em cada um deles,

07:09

a gente vai começar a compreender como eles funcionam. Vamos falar aqui,

07:12

então, primeiro do delegado. O delegado vai ser o quê? Por definição,

07:17

ele é o padrão delegado ali, que é o roteador.

07:21

Ele tem um agente top, tá? Um agente inicial ali,

07:25

que está ali em cima aqui, se vocês puderem ver.

07:27

Ele aparece aqui no halter que decide. Esse agente aqui, ele vai...

07:34

Recebeu uma pergunta, ou seja,

07:35

o usuário faz uma pergunta para esse agente halter

07:38

que vai analisar qual é a intenção, o que está rolando aqui,

07:41

e ele vai delegar para quem sabe resolver.

07:43

Pode ser o agente X com a sua skill ou o agente Y com a sua skill. Então,

07:46

ele vem aqui e vai conseguir fazer essa separação.

07:50

Ele é muito eficiente para assistentes que

07:52

Precisam agregar vários conhecimentos diferentes. Então, no nosso cenário,

07:55

imagina que o usuário fez uma pergunta para o seu agente de atendimento aqui,

08:00

o agente top que está fazendo a decisão.

08:01

Esse agente top... ele vai falar o seguinte,

08:04

essa conversa faz mais sentido estar com o RH. Ele vai lá e chama...

08:10

O papel do RH, o cara que conhece do RH,

08:12

o agente X que conhece a skill de RH.

08:14

Se ele fizer mais sentido ser alguma coisa que se resolve com o jurídico, ele vai para o jurídico.

08:19

Imagina se esse cara tivesse que conhecer jurídico e RH,

08:22

ele aumenta a sua capacidade de alucinação,

08:24

aumenta a janela de contexto e assim por diante. Ou seja,

08:27

nessa estratégia onde você delega para quem tem

08:30

determinado conhecimento de algo extremamente complexo,

08:34

você começa a trabalhar com este carinha aqui, o agente top, como um. Intent Routing.

08:40

A gente pode falar que é um cara que está decidindo qual a

08:42

intenção e roteando ela como se fosse um load balancer pessoal,

08:46

inteligente, sobre o que eu quero fazer. Então aqui, basicamente,

08:50

essa é a estratégia. O valor que a gente traz vai ser a eficiência de ativação.

08:54

Você não vai querer enviar um input genérico ali para um

08:57

agente que é super especializado e vai desperdiçar processamento,

09:01

vai desperdiçar uma porrada de coisa.

09:02

E nem para um agente genérico que não tem a ferramenta certa, o MCP correto.

09:07

O delegador vai definir. Vai garantir que você está delegando para quem

09:12

tem o maior conhecimento e tem as ferramentas para trabalhar o assunto.

09:15

E aí aqui você resolve uma porrada de coisa. Você vai resolver problemas de...

09:20

Acesso que não deveria ter,

09:21

você vai resolver o problema de conhecimento que precisa ter e assim por diante. Ou seja,

09:25

o delegador vai garantir que a janela de contexto vai ser

09:29

consumida apenas pelo nó que vai ter autoridade para fazer isso.

09:33

Ou seja, a ferramenta necessária para resolver aquela intenção específica.

09:38

Vamos falar aqui do nosso cenário.

09:39

Então, tem aqui o meu agente... ele está decidindo mandar algo para o RH,

09:43

você concorda que o RH não precisa ter acesso aos dados do jurídico,

09:48

por exemplo? Ele precisa ter acesso realmente aos dados de RH. Então,

09:52

ele vai ter tools aqui para ver folha de pagamento, vai ver cargos e salários, etc.

09:57

Enquanto a gente do jurídico não precisa ter acesso a isso.

10:00

Então, até na gestão de acesso,

10:02

essa estratégia é super importante quando você não

10:04

pode dar acesso para todos a tudo,

10:07

que também nem é saudável,

10:08

não pode nem deve. Então, basicamente...

10:10

Essa é a estratégia quando a gente está falando de delegação,

10:14

beleza? E qual que é o antipattern disso? O que a gente precisa tomar cuidado?

10:19

Então, quando a gente está falando do delegado, quanto que a gente não deve usar?

10:23

Então, quando a gente está olhando ali o antipattern,

10:26

o erro mais comum que a gente vê é o agente top querer resolver tudo,

10:30

querer resolver todo o nosso problema. Então, o que acontece?

10:35

Quando a gente está falando do...

10:37

de uma solicitação, pode ser que o agente queira não fazer o roteamento.

10:40

Ele vai fazer o trabalho,

10:42

Em vez de usar a estrutura de multiagente. Então, você vai ter um monolito ali e,

10:46

No final das contas, você não vai estar jogando para cada um dos nós.

10:48

Outro ponto que a gente precisa pensar é que a gente não pode usar um if-else ali,

10:51

Baseado em palavras-chave, por exemplo. Não vai colocar férias,

10:56

Manda para o RH e assim por diante.

10:57

Usa a estratégia de descoberta de skill, que a gente já falou também.

11:00

Usa agentes cards ali. O agente deve saber o que o outro faz e não adivinhar.

11:04

Ele não pode ser um agente adivinho. Ele precisa conhecer.

11:08

Beleza? Basicamente,

11:09

Essas são as estratégias que a gente precisa ter aqui e a gente não pode furar elas,

11:15

Porque, senão, a gente vai criar um antepartner e isso vai

11:16

Virar um baita de um problema lá na frente. Fechou?

11:20

Aqui a gente muda um pouquinho o foco.

11:22

Agora a gente começa a resolver um outro tipo de problema.

11:26

O problema não é mais você ser um roteador,

11:28

Não é ser um cara que delega e que trabalha

11:31

O problema de complexidade da síntese com os seus grandes conhecedores,

11:36

Detentores do conhecimento daquele determinado assunto.

11:39

O problema agora é outro. A gente precisa,

11:41

No padrão hierárquico, uma dinâmica onde eu tenho, sei lá, um PM,

11:44

Pensa um Product Manager ali trabalhando, e o time de especialistas.

11:48

Essa é a diferença agora do hierárquico que a gente está falando.

11:51

Então, nessa estratégia, a gente muda um pouquinho.

11:54

Por que a gente não deixa o PM,

11:56

Ou aqui na nossa estratégia, ele como um coordenador da operação,

12:00

Fazer todo o trabalho sozinho?

12:02

Porque ele vai entrar em colapso, certo?

12:04

Se a gente tentar colocar todo o contexto ali de lei,

12:07

Finanças, engenharia dentro da memória de um único agente,

12:11

Ele vai começar a ter lapsos, ele vai perder o foco,

12:14

Ele vai ter aquele overload cognitivo que a gente fala.

12:17

Assim como uma pessoa, certo? No dia a dia, acontece a mesma coisa com a gente.

12:20

Se a gente pegar todo o conhecimento de todas as áreas que a gente trabalha,

12:23

Enfiar tudo num ser humaninho só,

12:25

Possivelmente, esse ser humano vai começar a confundir...

12:31

Então, aqui o que a gente está falando é que o PM,

12:34

Como esse coordenador da brincadeira,

12:37

Ele não vai trabalhar sozinho,

12:39

Ele vai trabalhar agregando a resposta de vários

12:43

Outros carinhas aqui no meio do caminho.

12:45

Então, o padrão hierárquico que ele faz, na verdade,

12:48

É que ele divide para conquistar. Ele vai dividir ali a atenção.

12:52

Para conseguir conquistar um resultado melhor. Então,

12:55

Ele tem ali os especializadores,

12:57

Os workers. Cadê meu mouse? Está aqui.

12:59

Você tem as especializações, Worker 1, Worker 2, Worker 3.

13:03

E o coordenador. O coordenador vai planejar e consolidar.

13:07

Ele não responde por si só. Ele planeja e consolida.

13:10

Então, ele planejou ali alguma coisa,

13:12

Jogou para cada um deles, para tomar ali a informação de cada um deles. E daí, com base nisso,

13:18

Ele vai seguir a próxima etapa. Então, aqui...

13:22

O coordenador não é um especialista em nada,

13:24

Ele é um mestre na intersecção dos domínios, ou seja,

13:27

Ele compreende basicamente quem faz o quê e como ele

13:31

faz para trabalhar com essa intersecção de domínios,

13:33

como é que ele... ele complementa e consolida esses domínios.

13:36

A função dele não é executar,

13:38

A função dele é a resolução de conflito de síntese,

13:41

ou seja, e síntese, perdão,

13:44

Se ele tiver um conflito entre as áreas ali, em cada worker,

13:48

que eles não conseguem se resolver por si só,

13:51

Quando chega nele, ele resolve, ou seja,

13:53

Se o worker 1, que ele não sabe o que o worker 2 está fazendo,

13:55

que ele não sabe o que o worker 3 está fazendo, manda... que podem ser conflitantes,

14:00

Ele vai resolver esse conflito e vai sintetizar isso numa resposta.

14:04

Então, pensa que o usuário chamou o coordenador,

14:06

que é esse agente ali de cima, esse agente aqui,

14:09

Ele planejou, disparou para cada um desses carinhas aqui trabalhar,

14:13

Esses carinhas pegam e jogam de volta para o coordenador,

14:16

Que vai agregar a resposta, vai agregar...

14:20

Vai desambiguar possíveis problemas e responder a

14:25

Sua resposta final ali no final das contas.

14:27

Então, o coordenador, no final das contas, ele trabalha desse jeito.

14:31

Ele vai trabalhar a gestão de conflitos e a síntese da

14:35

Resposta para conseguir entregar com uma estratégia de A a A paralela. Então,

14:41

Qual o valor que traz no final das contas quando a gente está falando?

14:45

O valor final aqui é que a agregação faz essa junção de visões diferentes.

14:51

Ou seja, no exemplo aqui do diligence,

14:53

O jurídico pode dizer que a empresa é segura,

14:56

Mas o financeiro pode ver um risco de caixa ali,

14:59

No fluxo de caixa. E daí, se você estivesse com ele sozinho,

15:03

Você tem visões parciais. Se só um deles responder, a visão vai ser parcial.

15:07

O coordenador é o único que consegue olhar para o

15:09

Parecer dos dois e vai identificar o seguinte.

15:12

Essa contradição...

15:13

Ela precisa ter um relatório único que reflita

15:17

A realidade completa do negócio inteiro,

15:19

Do business que você está trabalhando.

15:20

Não pode ser só um lado ou outro.

15:23

Se você não usar esse padrão para problema complexo, por exemplo,

15:27

O que vai acontecer é que o seu agente único vai começar a alucinar no consenso ali.

15:32

Ele vai responder um ou outro, ele não vai conseguir fazer essa segregação.

15:36

Ou seja, ele vai fingir que entendeu tudo só para entregar uma resposta sem...

15:40

Ter processado com profundidade a técnica de cada um dos domínios,

15:44

Porque ele está com uma janela muito grande de interpretação.

15:47

Então, essa estratégia é extremamente importante para quando

15:51

A gente precisa dar opinião de

15:53

Várias áreas cruzadas e alguém que decida depois como que vai fazer a síntese disso, beleza? Vamos lá.

16:00

Então aqui a gente vai sair um pouquinho da teoria pura

16:03

E vai olhar um pouquinho de engenharia mais robusta aqui.

16:06

Quando a gente monta um fluxo hierárquico,

16:08

a gente não tem apenas prompts conectados ali,

16:12

a gente está desenhando uma arquitetura assíncrona que precisa ser resiliente.

16:15

Então a gente vai dividir isso em três pilares fundamentais.

16:17

A otimização da complexidade, que é a latência. O uso assíncrono aqui,

16:21

o Async Together, não é apenas para ser rápido,

16:26

é porque quando a gente olha dessa complexidade,

16:28

se você não trabalhar com ele, você vai começar a capotar.

16:32

Se a gente rodar de forma síncrona,

16:34

a latência final vai ser o quê? A soma do tempo de cada worker trabalhando,

16:39

o que vai inviabilizar qualquer sistema de trabalhar no dia a dia.

16:43

Como a gente está trabalhando com uma estratégia diferente,

16:46

a gente trabalha com o getter forçando o paralelismo ali.

16:50

A latência total do sistema vai ser o quê?

16:52

Vai ser o alinhamento apenas do worker mais lento. Ou seja,

16:56

você tem três workers trabalhando. Um demora um segundo,

17:00

outro dois, outro três. Você vai gastar três. Agora,

17:03

se você trabalhar sem usar essa estratégia, você vai fazer o seguinte.

17:06

Vai somar dois com três com um.

17:08

Vai trabalhar em seis em vez de três. Dobrou o tempo. Então,

17:12

no final das contas, o seu limite ali vai ser a performance do seu gargalo.

17:16

E não a performance de uma sequência. Beleza? Então,

17:19

a primeira coisa é a otimização da complexidade.

17:22

Segunda coisa que a gente vai falar aqui é o princípio da ignorância seletiva,

17:25

então o encapsulamento ali,

17:27

vocês podem notar que o coordenador não conhece a lógica dos workers,

17:30

ele vai tratar cada worker como uma caixa preta,

17:33

então ele está trabalhando ali os black box dele e...

17:36

O que o coordenador vai enxergar é apenas o contrato que ele tem,

17:39

o que a gente chama ali de um agent card, vai?

17:42

E esse agent card, se o worker ali de TI, por exemplo,

17:45

for substituído por um modelo novo ou por um sistema de regra diferente,

17:49

o coordenador não vai precisar ser alterado.

17:51

Então aqui você já segrega a responsabilidade e começa

17:54

a trabalhar com domínio sem vazão de contrato.

17:56

Desse jeito você consegue não capotar uma coisa quando a outra se altera.

18:00

Então é isso que garante ali um acoplamento fraco no final das contas.

18:05

Permitir que você consegue aí evoluir cada peça do sistema de forma independente.

18:09

Se você não fizer desse jeito,

18:11

cada vez que mudar alguma coisa, você vai ter que mexer na bagaça toda. Ah, beleza,

18:14

eu estou trabalhando com dois workers. É uma coisa, quando você estiver com 30 aí,

18:17

você vem me contar como é que foi a brincadeira.

18:20

Então, aqui é uma das coisas super importantes,

18:23

que é você ser um ignorante seletivo, que eu chamo,

18:26

que é o encapsulamento ali das coisas.

18:28

Então, é trabalhar com essa estratégia de caixa preta para cada um do sistema.

18:31

Tem uma outra coisa também importante que a gente está trazendo para cá,

18:34

que é a parte de resiliência,

18:36

usando aquela estratégia que a gente já conhece de Graceful Degradation,

18:38

básica de sistemas. Então aqui a gente entra com um ponto crítico.

18:43

De quando a gente retorna uma exception, por exemplo.

18:45

Se vier uma exception igual a true,

18:47

a gente está falando de uma arquitetura distribuída no final das contas.

18:51

As falhas, elas são uma certeza. A gente sabe que isso vai acontecer.

18:54

Então, quando acontecer isso, por exemplo, em um único worker,

18:58

por exemplo, ele falhou ali por timeout, ou deu erro na hora que ele faz essa atualização,

19:02

ou algum problema que ele não conseguiu responder,

19:04

ele não pode derrubar toda a execução no efeito cascata.

19:08

A gente precisa tratar o erro...

19:10

com o valor, não com uma interrupção. Seu sistema, então,

19:13

vai ter que tentar trabalhar com uma degradação mais graciosa no final das contas,

19:19

ou seja, se o worker de TI cair e o coordenador receber essa falha,

19:22

ele pode avisar o usuário que aquela parte específica está indisponível,

19:26

mas ainda assim entregar o restante,

19:28

falar, olha, a parte de finanças do RH veio, mas a parte da TI caiu,

19:34

está fora, então estou com uma visão aqui meio míope do que está rolando. Então, basicamente, o coordenador...

19:40

Ele não é um chefe autoritário que para tudo se alguma coisa der errado.

19:44

Ele é mais um orquestrador resiliente que garante que

19:47

o sistema sempre entregue o valor máximo possível,

19:49

mesmo quando tiver falhas parciais acontecendo.

19:52

Beleza, galera? Vamos lá. Agora vamos falar do próximo carinha aqui,

19:57

que é o nosso pipeline,

19:59

a parte sequencial. Uma estratégia mais de cadeia aqui, tá? Então,

20:04

se o hierárquico vai ser sobre uma agregação de opiniões,

20:07

você já entendeu onde está o pipeline, certo?

20:09

O pipeline é a transformação de estado.

20:11

A melhor maneira que a gente tem para entender esse negócio é...

20:15

quando a gente pensa numa filosofia do Unix ali. Você pega um dado,

20:19

aplica uma transformação e passa o resultado para o próximo e

20:22

o fluxo de processamento de pipeline em linha reta. Ou seja,

20:26

um faz um trampo, passa para o outro, faz um trampo, passa para o outro,

20:29

faz um trampo, passa para o outro e assim por diante.

20:31

Nesse cenário aqui, você pode ver, então, que tem o usuário mandando uma pergunta,

20:36

um trabalho aqui para o agente A. O agente A...

20:39

passa para a gente B depois de enriquecer e trabalhar,

20:42

que vai extrair qualquer informação aqui, enriquecer,

20:45

formatar e mandar para a gente C,

20:47

que vai fazer a mesma coisa, vai pegar,

20:49

vai enriquecer essa brincadeira aqui e responder.

20:52

Ou seja, você tem um fluxo de cadeia ali, um pipeline de execução.

20:57

Então aqui, quando a gente fala dessa estratégia,

21:00

o segredo dele vai ser basicamente o seguinte,

21:03

a gente precisa pensar em dois conceitos de engenharia mais fortes. Primeiro,

21:08

o desacoplamento por contrato. Ou seja, a gente precisa ter ali,

21:12

precisa notar que o agente de tradução não sabe nada sobre o scraper, por exemplo.

21:19

Ele não precisa saber de onde o dado veio,

21:21

qual site foi acessado ou se a conexão falhou.

21:24

Ele trabalha com o contrato de interface ali.

21:27

Ele espera um input com o formato X e garante

21:30

a entrega de um output com o formato Y. De novo,

21:32

aquela segregação de responsabilidade para você ter

21:35

um sistema onde você pode trocar, por exemplo,

21:36

o scraper ali por um leitor de PDF, por exemplo,

21:39

sem alterar nada. numa linha de código do seu tradutor,

21:43

num cenário ali de tradução.

21:45

Então a gente está falando basicamente dessa estratégia.

21:48

Você tem um estado evolutivo,

21:49

então você pensa nisso como uma linha de montagem de dados,

21:52

é como se fosse um trabalho em cadeia.

21:54

O dado que entra no pipeline é uma matéria -prima bruta,

21:57

e cada etapa da gente amadurece esse dado. Então a gente a extrai e limpa.

22:02

O agente B vai lá e resume, sei lá, condensa essa conversa.

22:06

O agente C vai lá e traduz para uma formatação final.

22:09

O valor aqui no agente C, quando a gente está falando,

22:13

é especificidade do processamento. Cada agente tem uma única responsabilidade,

22:18

o single responsible principle,

22:20

que a gente já conhece, o S, né?

22:21

Do nosso querido, do nosso querido pattern ali, certo?

22:27

Então, a gente está ali com o single

22:28

responsibility principle e por isso ele consegue

22:31

ser muito mais preciso do que um agente que tentasse fazer tudo de uma vez. Então, no final das contas,

22:38

a gente está usando os princípios de solid dentro dessa estrutura,

22:42

de certa forma. Qual a diferença fundamental para o hierárquico,

22:46

pessoal? No hierárquico... a gente tem a divergência.

22:50

Vários agentes pesquisando coisas diferentes,

22:52

trabalhando coisas diferentes para depois ter uma convergência. Então,

22:56

eu abro um diamante, para quem já conhece essa estrutura,

22:59

para depois fechar com o coordenador juntando tudo e dando uma resposta. No pipeline,

23:05

a gente tem a linearidade. Não tem conversa, você não tem agregação,

23:11

cada um faz um pedaço e passa para o próximo.

23:13

Você tem um fluxo de valor incremental. Se você...

23:17

tentar ramificar ou fazer o agente C perguntar algo para o agente A,

23:22

você vai quebrar o pipeline e você criou uma dependência circular. Aí vai dar ruim.

23:27

O pipeline é a arquitetura mais simples que a

23:29

gente tem no dia a dia aqui trabalhando,

23:32

justamente porque ele vai remover a necessidade de um chefe coordenando.

23:36

Ele é basicamente um passo a passo.

23:39

que não tem um coordenador direto. É um fluxo pré -determinado,

23:43

é mais fácil de você gerenciar,

23:45

mas traz esse outro ponto aqui, por exemplo, de mais demora,

23:48

mais latência, porque cada um vai fazer um pedaço,

23:50

você não consegue diversificar e nem consegue fazer

23:52

aquelas outras estratégias que a gente falou.

23:54

Pessoal, vou te falar aquela verdade absoluta,

23:57

não existe arquitetura certa. Existe arquitetura certa...

24:02

para determinada necessidade.

24:05

Cada uma delas tem seus prós e contras e vai depender do que você precisa resolver.

24:09

Então, a grande resposta para vocês aqui é qual é

24:12

o melhor dos três que a gente falou?

24:14

Depende. É o grande depende de sempre. E eu vou precisar que vocês,

24:18

No dia a dia, pensem em como resolver cada um desses problemas.

24:22

Beleza? Então, vamos lá. Se o hierárquico era sobre agregação de opinião,

24:27

o pipeline é sobre transformação de estado. Então,

24:29

essa é a melhor maneira da gente entender tudo isso que a gente falou até agora.

24:34

Essa é a maneira mais fácil de compreender.

24:37

Beleza? Basicamente,

24:38

essa é a nossa aula que a

24:41

gente tinha falado aqui de utilização de patterns.

24:46

Eu espero que vocês tenham gostado.

24:48

É muito bom a gente pensar que é nessa estrutura de usar patterns,

24:54

porque daí a gente erra menos. Porque se a gente já teve...

24:57

pessoas que fizeram, que definiram padrões, que já passaram por problemas,

25:02

a gente não precisa passar igual, certo? Bom, basicamente,

25:05

se eu parar para pensar e olhar aqui no meu dia a dia,

25:08

a maior parte das vezes, contando para você aqui um pouco dos bastidores,

25:12

que eu acho importante, a maior parte das vezes,

25:13

os bastidores, eu tenho implementado este carinha,

25:17

que é mais simples até para a gente evoluir depois, ou seja,

25:20

a parte de pipeline, mas, por exemplo, dentro da minha empresa lá no Eureka,

25:25

eu utilizo... Esta estrutura aqui, que é uma das mais complexas que eu vejo,

25:30

que é a estrutura hierárquica para conseguir

25:33

criar os nossos sistemas multiagentes.

25:35

Então, dentro do Eureka, eu uso muito essa.

25:37

Dentro de sistemas mais complexos,

25:40

empresas maiores e que precisam de mais correlação,

25:42

eu tento ir por esse normalmente para diminuir o atrito e a entropia entre os times.

25:47

Mas, de novo, foi o que eu falei para vocês,

25:49

vai depender muito de cada coisa que você tem para fazer.

25:53

Você precisa compreender cada uma delas e saber como responder.

25:57

Já vi os três cenários,

25:58

o Isaac sei que estava trabalhando há um pouco tempo atrás no cenário A,

26:03

que eu conversei com ele, em uma das estratégias que ele estava trabalhando lá,

26:07

ele estava muito nesse cenário A, sei que ele já passou por todos esses três também,

26:10

e aqui fica a nossa aula sobre a arquitetura

26:14

multiagente e a parte de design patterns,

26:17

espero que vocês tenham gostado, um forte abraço.

## Resumo IA

[RESUMO_IA]