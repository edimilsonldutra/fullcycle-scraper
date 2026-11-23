Módulo: Protocolos de Comunicação\
Aula: [LAB: Comparativo Prático 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18590)

## Resumo da aula

A base do experimento fica organizada em pastas separadas para a API externa, os adapters de tool calling por provider, o servidor MCP e os testes. Essa estrutura existe para isolar responsabilidades e permitir observar exatamente onde o contrato da API aparece no código. O README funciona como roteiro operacional: subir a API, executar testes, rodar os adapters e aplicar o patch da V2. Retomando o cenário de clima já estabelecido, a novidade aqui é transformar a comparação arquitetural em execução reproduzível.

A API V1 expõe um endpoint simples que recebe city e devolve cidade, temperatura e condição climática. O serviço é fake e usa dados hardcoded porque o objetivo não é modelar meteorologia, e sim tornar visível o acoplamento ao contrato externo. Subir a API com FastAPI e Uvicorn permite validar rapidamente o comportamento pelo Swagger antes de integrar com LLMs. Esse passo reduz ambiguidade: se a API falhar aqui, o problema ainda não está no adapter nem no protocolo.

Os testes da API verificam se o serviço sobe, se os campos esperados existem e se os tipos retornados continuam corretos. Isso não substitui testes de integração ponta a ponta, mas cria uma linha de base para detectar regressões no próprio serviço. Ler esses testes ajuda a entender o contrato real melhor do que olhar apenas para funções locais. Quando a API evoluir para V2, essa camada será a primeira a confirmar que a mudança foi intencional.

Os adapters de tool calling para Anthropic e OpenAI são parecidos na intenção, mas diferentes no schema e no envelope de execução. O código precisa declarar a tool no formato exigido por cada SDK e executar a chamada no mesmo processo em que o modelo roda. Isso concentra a integração no host, não em um serviço compartilhado. A consequência prática é que a assinatura real da API de clima vaza para cada provider consumido.

A divergência entre tool_use, tool_result, tool_use_id e tool_call_id mostra que a compatibilidade é conceitual, não estrutural. Dois providers podem oferecer tool calling e ainda assim exigir envelopes, nomes de campos e parsing diferentes. Esse detalhe importa porque a mudança de contrato da API não afeta só a função de negócio; ela também exige revisar o schema proprietário de cada adapter. O custo de manutenção nasce justamente dessa multiplicação de pontos de conhecimento.

Executar o adapter da Anthropic confirma o fluxo completo: prompt do usuário, decisão do modelo, chamada da API externa e resposta final. Os testes associados verificam se os parâmetros corretos foram enviados e se os dados retornados pela API aparecem na resposta processada. Esse tipo de teste é útil apenas quando observa o comportamento real da integração. Se ele se apoia em mocks cegos, pode continuar verde mesmo com o contrato quebrado.

O servidor MCP encapsula a chamada da API de clima em uma tool publicada uma única vez com decorator. A função continua chamando a mesma API externa, mas agora o contrato fica centralizado no servidor em vez de ser repetido em cada host. Retomando o exemplo anterior, aquilo que antes era um adapter local por provider vira um ponto único de exposição compartilhável. O ganho principal não é só menos código; é menos lugares conhecendo a assinatura externa.

O Inspector permite verificar discovery e invocação no nível da mensagem, incluindo tools/list, inputSchema e execução da tool. Essa inspeção é valiosa porque confirma que o servidor MCP está publicando a capacidade correta e recebendo os argumentos esperados. O sessionId ajuda a acompanhar a continuidade da conexão durante a depuração. Quando o protocolo é padronizado, ferramentas de observabilidade se tornam reutilizáveis entre implementações diferentes.

Os testes do MCP Server validam que a tool está registrada, que aceita os argumentos previstos e que chama corretamente a fonte externa. Como o contrato fica concentrado no servidor, essa suíte protege o ponto mais sensível da integração compartilhada. O efeito arquitetural aparece aqui: um teste bem posicionado cobre todos os clientes MCP que dependem daquela tool. Isso contrasta com o cenário de tool calling, em que cada host precisa de sua própria proteção.

A V2 introduz state como parâmetro obrigatório e renomeia campos de saída, como temperature para temperature_c e condition para summary. Essa mudança simula uma evolução legítima de produto: sair de um escopo restrito a São Paulo para atender o Brasil inteiro. O erro 422 aparece porque o consumidor continua enviando a assinatura antiga. Aqui a quebra deixa de ser abstrata e vira evidência operacional observável.

Quando o teste do adapter continua passando após a quebra da API, o problema não está no backend novo, mas no teste antigo. O mock cego devolve uma resposta compatível com o contrato antigo e mascara o fato de que a integração real já falhou. Esse é o falso verde mais perigoso: a pipeline sinaliza segurança exatamente quando o sistema está inconsistente. Teste útil precisa falhar quando o contrato externo muda de verdade.

Ao executar o adapter real contra a API V2, o erro 422 expõe que faltou o argumento state. A LLM não tomou uma decisão errada; o schema local ficou desatualizado em relação à API. Isso é importante porque evita culpar o modelo por um problema que, na verdade, é de integração. O ponto de correção está no adapter e na definição da tool, não no prompt nem no raciocínio do modelo.

Corrigir o tool calling exige editar manualmente o schema e a chamada da função para incluir os dois parâmetros novos. Se houver adapters para Anthropic, OpenAI e Gemini, a mesma mudança precisa ser repetida em cada implementação proprietária. O esforço cresce com o número de hosts e providers, mesmo quando a mudança de negócio é uma só. Esse é o custo distribuído do acoplamento já discutido anteriormente, agora visível em código.

No caminho com MCP, a correção principal acontece no servidor: a tool passa a receber city e state e a chamar a API V2 com a nova assinatura. O cliente MCP permanece estável porque ele depende do protocolo e do discovery, não do detalhe interno da API externa. Essa é a diferença estrutural do laboratório: a mudança de contrato continua existindo, mas o custo de absorvê-la fica concentrado. Em vez de refatorar vários adapters, refatora-se um ponto central.

O cliente MCP criado para o experimento continua o mesmo antes e depois da refatoração do servidor. Mesmo quando a tool falha, a interação tende a retornar uma resposta tratada pelo fluxo do cliente, em vez de estourar diretamente uma exceção crua para o usuário final. Isso não elimina a necessidade de corrigir o contrato, mas melhora a superfície operacional da integração. O comportamento observável fica mais estável porque o cliente conversa com uma camada intermediária padronizada.

No recorte de um único SDK, o tool calling exige mais linhas porque combina schema proprietário e adapter local, enquanto o MCP reduz o código do host ao consumo do servidor. O acoplamento à API real fica espalhado no primeiro caso e centralizado no segundo. A troca de provider de LLM força reescrita de schema no tool calling, mas não altera o servidor MCP já publicado. A refatoração após quebra de contrato confirma a tese prática: o MCP não remove a mudança, mas reduz drasticamente o número de lugares que precisam conhecê-la.

## Transcrição

00:00

Pessoal, tudo bem?

00:02

Agora o que a gente vai fazer é de fato seguir

00:05

aqui como se estivesse aí com você fazendo um pair programming,

00:11

tá? E ao mesmo tempo explorando aqui o nosso ambiente para fazer o lab acontecer, tá bom?

00:17

Então, acho que a primeira coisa que a gente tem que fazer, né?

00:21

Que eu queria, obviamente, mostrar para vocês a estrutura aqui, né?

00:24

Das nossas pastinhas, tá? De laboratório. Dos laboratórios, tá?

00:29

Dentro dos módulos que você vai encontrar quando você clonar, tá?

00:34

Especificamente, a gente está no módulo 8, tá?

00:39

Desculpa, na aula 8 do módulo 1, tá? E, gente, assim,

00:43

eu fiz um Readme bem completinho aqui para vocês,

00:46

tá? Assim vocês vão ver que está didático,

00:51

está simples, tá? Mas, obviamente, sempre aberto a feedbacks,

00:54

mas no final do dia a ideia era que eu repassasse isso aqui do zero,

00:59

né? Eu fiz isso algumas vezes aqui para garantir que,

01:02

de fato, vocês conseguiriam fazer sozinho, tá?

01:05

Mas agora a gente vai fazer aqui grande parte dele, inclusive os passos aqui.

01:09

que estão dentro deles, vocês vão poder replicar, tá bom? Bem,

01:13

primeira coisa, né, pessoal,

01:17

que eu quero fazer é abrir os principais arquivos aqui nossos, tá bom? Vamos lá.

01:25

Deixa eu abrir os principais

01:27

pastinhos nossos aqui.

01:44

Deixa eu inicializar, né? Deixa eu entrar dentro do laboratório aqui.

01:47

Eu não estava dentro do lab. Agora sim.

01:51

Abrir as pastinhas, abrir os principais arquivos, tá gente?

01:53

Os principais arquivos que vale a pena,

01:55

que a gente vai explorar é, obviamente, o primeiro,

01:59

que é o desenvolvimento da própria API, tá?

02:04

Faltou um, faltou dois, pera aí.

02:06

É, da própria API, né, que eu vou explicar pra vocês,

02:09

tá? Depois a gente vai passar pela...

02:13

Pela forma como a gente desenvolveria o

02:17

Tocoli para o PNA e para o Anthropic, tá?

02:21

Depois a gente vai subir o MCPC,

02:24

vai fazer as alterações e vai ver o que vai acontecer,

02:26

tá bom? Bem, a API na versão 1, pessoal,

02:30

desse nosso sistema fictício aqui, é o seguinte, tá? A especificação dela...

02:34

É que é o serviço de detecção, de informação sobre clima de cidade de São Paulo,

02:40

tá? Por algum motivo, tá? O escopo do sistema era só São Paulo.

02:44

Alguém decidiu, ah, vamos fazer.

02:45

Não precisa fazer temperatura, desculpa, não precisa fazer,

02:49

entender como é que tá a temperatura,

02:50

as condições de clima em todas as cidades do Brasil,

02:53

não. A gente só foca no estado de São Paulo, né?

02:55

E é isso aí. Então, obviamente, pessoal, né?

02:57

Uma API que tá hardcore dada aqui, tá? É fake, né, pessoal?

03:03

Esse aqui é só para fim didático mesmo, tá?

03:08

Como vocês podem ver aqui, ela basicamente recebe uma cidade, né?

03:14

E ela retorna o nome da cidade,

03:17

a temperatura e a condição do clima, tá bom? No JSON, tá?

03:21

Basicamente isso que ela faz, tá bom?

03:23

Mas vamos colocar ela aqui para executar, tá? A gente usa FastAPI,

03:27

então eu vou inicializar ela com o vCorn aqui, tá bom?

03:32

O legal com o FastAPI, quando você implementa,

03:35

ele disponibiliza uma página

03:41

de documentação, um Swagger aqui de documentação,

03:47

em que a gente consegue chegar aqui, por exemplo,

03:50

até testar a API. Eu vou chegar aqui,

03:53

vou colocar aqui Campinas, uma das cidades possíveis que estão lá.

03:58

Eu vou falar, tá vendo? Campinas está ensolarado, com temperatura de 26 graus.

04:02

Agora eu vou colocar aqui uma cidade que não está lá, tá? Recife, por exemplo, tá?

04:07

Eu vou falar, ó, cidade desconhecida, tá bom?

04:11

O que mais?

04:15

Bem, então, a gente fez aqui, tanto que, você vê,

04:18

na primeira vez que eu chamei com Campinas funcionou,

04:20

da segunda vez que eu chamei com Recife não funcionou.

04:23

Esse aqui é só para vocês verem que está funcionando,

04:26

que está tudo certinho aqui, tá?

04:27

E eu vou até abrir agora aqui uma outra, uma outra janela, né? Deixei nos

04:33

mover a pasta correta, que a pasta do

04:36

Lab é do lado 08, né? E eu

04:41

vou fazer o seguinte, pessoal: eu fiz uma suíte de testes, é bem interessante aqui, tá? É

04:48

se vocês podem até olhar por aqui, inclusive, deixa eu dar o clique, tá? E aí, então,

04:52

vocês podem até olhar por aqui.

04:57

Você tem como executar, obviamente, aqui pela própria IDE.

05:03

Nesse caso aqui, eu vou testar esse aqui. Vamos fazer por aqui.

05:06

Vou testar esse aqui, que é da API.

05:09

Tudo rodou, tudo bonitinho.

05:11

Ele faz um teste para saber se ela subiu,

05:18

se retorna os três campos, se os tipos estão certos, enfim,

05:24

são testes que vão surgindo. Depois, vocês dão uma navegada aqui,

05:28

que entendendo os testes, acabam também entendendo melhor o sistema, tá?

05:35

Então, eu poderia também chegar aqui e executar aqui,

05:38

tá? API de teste, a mesma coisa,

05:40

usando o PyTest diretamente, né? Vocês viram que todos os testes passaram,

05:44

tá? Por enquanto, tudo certo, tá?

05:47

Agora aqui eu quero...

05:52

Eu quero mostrar para vocês, pessoal,

05:54

basicamente a gente já tinha feito isso antes no PPT, que é mostrar a diferença. Olha para você ver,

06:01

são classes muito próximas uma da outra, de implementação

06:05

do True Calling, usando a OpenAI e usando a Tropic.

06:10

O que muda basicamente no esquema,

06:13

mudar basicamente no esquema significa mudar o coração do negócio.

06:17

A chamada do get to add,

06:20

que eles têm que fazer no mesmo ambiente, em

06:24

que a definição do esquema e o modelo estão, obviamente,

06:30

porque é local, não tem um serviço, não tem um servidor por enquanto.

06:35

É isso que o MCP vai trazer dessa arquitetura cliente-servidor.

06:42

E a gente aqui tem o run de cada um, que é como...

06:45

Que é basicamente a execução propriamente dita. Está vendo?

06:49

Como está o clima em Campinas.

06:51

Nesse caso aqui. Como está o clima em Curitiba. Inclusive ia dar erro.

06:56

Vou até mudar aqui. Aproveitar. Campinas.

07:00

Ele até mudou lá embaixo também. Para deixar aqui certinho para vocês.

07:05

Daqui a pouco eu vou comentar. Vou fazer isso aqui logo.

07:10

Muito bacana aqui. Só também aproveitar.

07:13

E ter um.

07:17

Um gostinho, não sei se vocês já usaram, alguma ideia semelhante, como o cursor,

07:22

ou como, nesse caso aqui, o anti-gravity ou o windsurf,

07:26

de vez em quando eu vou dar umas navegadas aqui

07:30

e vou até pedir algumas ajudas aqui para a gente,

07:33

que a gente faz via essa conversa aqui, aqui do lado, tá bom?

07:37

Bem, vamos lá, por enquanto não, a gente fica quietinho aí. Então,

07:42

bem... é obviamente começam umas questões mais diferentes né olha só

07:47

né de estrutura tá é que tá vendo é o o da o

07:54

da troca tá vendo tem lá o use né aqui é

07:58

tu costa aqui tem um rolê assistente conta entre lá o motor né

08:05

está vendo o row aqui é uma ferramenta para determinar que

08:08

é uma mensagem que vem da execução de uma

08:10

ferramenta nesse caso aqui o row a gente descobre através

08:14

do type que é o tool result mas os dois aqui

08:18

esse aqui tem o tool use id lá tem o tool

08:20

call id então assim pessoal são as especificidades proprietárias

08:24

de cada um dos providers você quer para mostrar a

08:28

dificuldade aquela questão de a gente ter que Para cada provider,

08:32

né? Um adaptador diferente, tá?

08:35

Daqui para frente, pessoal, nós vamos focar no Dantropic, tá?

08:38

Só para fins didáticos mesmo e para o dinamismo aqui da nossa aula, tá bom? Bem, o

08:44

que mais? Ah, deixa eu executar aqui, pessoal, né?

08:50

Quero executar aqui o teste, tá bom?

08:52

Eu quero executar o run, tá? Eu quero ver a LLM chamando o modelo, tá?

09:00

Desculpa, a LLM chamando o modelo. A LLM recebendo o prompt,

09:04

que é como está o Clímica Pinas, né?

09:05

E ela fazendo ali a solicitação de chamada da ferramenta, tá?

09:09

Vou até colocar um breakpointzinho aqui, ó. Vou colocar um breakpoint aqui. Vou

09:16

colocar um breakpoint aqui. Ah,

09:19

não. Não vou conseguir debugar agora não, tá, pessoal?

09:21

Na verdade, tá? Mas... Vamos

09:27

fazer para sonar aqui, né? Vamos executar aqui, ó. Vamos lá.

09:34

O clima em Campinas está ensolarado com uma temperatura de 26 graus,

09:39

né? E é um dia bonito para aproveitar,

09:41

tá? Se vocês quiserem, tá? Se vocês quisessem, vocês poderiam colocar aqui aquele...

09:46

Fazer um export do Anthropic Log como debug, tá?

09:51

Para vocês verem todas as mensagens aqui bem formatadinhas, tá?

09:55

Aconselho vocês a fazerem isso aí no computador de

09:58

vocês para vocês verem o negócio acontecendo, tá?

10:01

é mas se não bastasse isso pessoal que que eu vou fazer eu vou também rodar

10:06

minha suíte de testes tá é olha só

10:08

ó que era basicamente é se com o input

10:14

do usuário tá chamada da API externa tá e se passou né vamos só dar uma olhada

10:19

Nos testes pessoal de curiosidade então vamos ver aqui o que é o Texan Tropic tá ó

10:26

Nesse caso aqui ó todos os parâmetros estão certos, segundo se chamou corretamente,

10:32

Então aqui a gente consegue debugar, vamos lá, olha que massa, aqui por exemplo, eu

10:39

Quero essa de baixo,

10:43

Vamos ver, data por enquanto ela está com nada,

10:48

Desci, então agora a data tem todas as informações, ó.

10:52

Esse aqui é o retorno da API, ó. Cidade, temperatura e condição, tá? Tá campinho,

10:57

26 graus de Celsius, né? O que ele tá checando,

11:01

Essas informações vieram dentro do próprio...

11:06

Da resposta aqui que o modelo recebeu, tá? Então, bem,

11:12

Eu vou rodar tudo aqui, ó.

11:14

Então, todos os testes... Todos os testes rodaram,

11:17

Né? Você consegue até ver aqui depois,

11:19

Rodar separado. Pessoal, enfim, dê uma navegada depois aqui na IDE.

11:24

Não sei se todo mundo aqui já teve essa experiência.

11:27

Sugiro vocês fazerem, até aproveitarem o momento para fazer isso, tá? Bem,

11:33

Vamos agora, pessoal, para o MCP, tá? Então, no caso aqui,

11:40

Olha, pessoal, olha a elegância do MCP, cara. Olha só.

11:44

Nesse caso aqui, olha só, vamos lá.

11:47

A primeira coisa que só tô criando uma constante aqui tá que determina aonde

11:53

Que tá a minha API, tá bom? Aí eu começo aqui inicializando aqui lá

12:00

Oferece MCP criando esse esse esse objeto que é o objeto MCP, tá? Olha,

12:06

Olha que coisa, olha que coisa maravilhosa, isso aqui é basicamente a chamada da API,

12:14

E eu coloco o decorador MCP Tool aqui em cima. E a partir desse momento,

12:17

O MCP Server já tem essa tool. Quer ver?

12:21

Eu vou até encapsular, gente, para vocês verem o seguinte.

12:24

É isso aqui.

12:26

É a forma que vocês põem o motor.

12:28

No MCP Server. Então, vamos fazer o MCP. Vamos subir o MCP Server, pessoal? Vamos

12:38

Subir? Vamos lá. Subiu.

12:42

Eu vou abrir aqui.

12:48

O espectro tá bom para abrir o espectro aqui com

12:51

Vocês esse aqui tá desatualizado, chave outro com outro toque, tá?

12:55

Vou me conectar, tá? Então aqui, pessoal, eu vou saber ó

13:00

Quais são as tuas que estão disponíveis aí, que tá lá,

13:03

E get weather, tá? Isso aqui mostra que tá funcionando,

13:05

Tá inclusive, olha aqui, olha isso, olha o JSON RPC,

13:10

Funcionando aqui, é uma tudo. Essa aqui é uma chamada de notification,

13:13

Tá vendo? Ó, isso aqui é uma chamada de notification, tá?

13:18

Nesse caso aqui, é uma chamada de lista de parâmetros, tá?

13:23

Tem aqui o put esquema, tudo bonitinho, tá bom?

13:29

Bem, e

13:32

Aqui eu vou fazer aqui, ó, Campinas.

13:35

Vamos executar a tool.

13:37

Agora, olha que interessante, tá?

13:41

Campinas, content, isErro, false.

13:45

Deixa eu ver se eu acho aqui mais informações. Request.

13:53

Cadê? Cadê? Cadê?

14:02

Boa. Então, vamos lá.

14:05

Retornou tudo certinho, pessoal.

14:09

Prova que o nosso MCP-Server está rodando. Sem erros. Vamos voltar aqui no código.

14:17

Está vendo aqui? Esse aqui é ele executando,

14:19

recebendo todos os... Está vendo? Tem o session ID.

14:24

que equivale à forma... Está vendo?

14:27

Ele compartilha o mesmo Session ID para garantir que

14:31

é o mesmo usuário que está chamando. Beleza?

14:34

Tipicamente é isso. Uma conexão de cliente gera um Session ID.

14:40

Então, o

14:45

Spectre prova que é uma ferramenta super poderosa. Isso que é legal.

14:50

Quando a gente lida com um padrão universal, um padrão que...

14:54

que é como do MCP, né?

14:59

A gente tem essa ferramenta aqui, prova que, assim, cara,

15:03

é sem complicação, simples, tá? Mostra, obviamente,

15:07

se tivesse riscos, você ia mostrar aqui,

15:09

pronto, enfim, pessoal, ferramenta super poderosa, tá?

15:12

Aconselho vocês também darem uma navegada e uma brincada com ela,

15:15

tá? Bem, vamos agora rodar o nosso teste, pessoal.

15:19

Também tem teste unitário para o...

15:24

Por MCP serve, tá? Deixa eu só pegar aqui os comandos, né?

15:30

Que é igual na Maria Braga, tá, gente? Deixa os comandos já tudo prontinho antes. Vamos lá.

15:38

Ó, vamos

15:42

rodar aqui a suíte de teste para o MCP, tá?

15:46

Então, ele testou, ele testou do antrópico, ele testou do esquema do antrópico,

15:52

ele testou o adaptador, ele testou passando a cidade,

15:55

tá bom? Então, de novo, pessoal.

15:58

Dê uma olhada aqui nos testes para vocês entenderem o

16:03

que ele está pedindo, tá?

16:07

Coisas que vale a pena vocês dar uma estudada.

16:10

Coloca os breakpoints aqui para vocês entenderem melhor.

16:13

Vocês conseguem, inclusive, entrar dentro do código. Enfim,

16:16

sugiro fortemente que vocês façam isso, tá?

16:19

Vamos rodar aqui também, né? Para deixar tudo verdinho.

16:23

Eu dou o PNI. Eu vou até rodar, mas possivelmente ele vai quebrar.

16:29

Ah, tá. Como ele tá como fake, tá, gente? Ele tá como fake LLM. É por isso, tá?

16:33

Ele não tá executando a dopeneide de verdade, não. Diferentemente dos outros, tá? Bem.

16:43

Então, assim. Então, vejam, assim. Nossos testes unitários,

16:46

na verdade, nesse caso agora, tá?

16:48

Ele tá sem mock, tá bom, pessoal? Quer ver? Vamos olhar aqui,

16:52

ó. Vamos ver se ele tá mockado ou não. Vamos ver se eu tô...

16:54

Se ele tá executando mesmo ou não o servidor. Vamos ver aqui, ó. não

17:06

está bocado, está tudo certinho. Então, vamos lá. Agora, vamos ver o seguinte.

17:13

Então, o que a gente viu? Só para repassar.

17:16

Vimos a API sendo criada.

17:18

Vimos o modelo chamado API com Function Calling.

17:26

Transformamos, criamos o MCP Server que encapsula essa chamada dessa API.

17:31

E agora, pessoal, a gente vai...

17:34

quebrar o contrato.

17:37

Agora a ideia é que a gente quebre o contrato. Agora, na verdade, a versão 2 da API,

17:42

o comercial foi lá e vendeu para o resto do Brasil. Então,

17:47

a versão 2 agora, ela tem que receber um parâmetro que é o estado do Brasil também.

17:54

Então, tem um patch aqui para a gente poder rodar. Vamos rodar esse patch.

18:04

Vamos mudar esse patchzinho aqui.

18:08

E com esse patch, vocês vão ver que o código da API mudou agora.

18:15

Essa é a ideia do patch. Então, agora, olha só. O nosso banco de dados,

18:21

na verdade, está vendo? Agora ele tem não só a entrada,

18:24

que é uma dupla. É uma dupla agora. É a cidade e o estado.

18:31

Então, o nosso método, a assinatura do método mudou. Cidade e estado.

18:36

E ele agora, inclusive, mudou o nome do retorno.

18:41

Ao invés de ser temperatura, passou para temperatura C.

18:44

Ao invés de condição, passou para sumário.

18:46

Vamos entender os impactos desse negócio agora?

18:50

Vamos lá. Vamos rodar o teste da Antropic, pessoal.

18:56

Vamos rodar o teste da Antropic. Ou seja,

18:59

eu quero rodar de novo esse mesmo teste aqui.

19:02

Vamos ver se vai dar bom. Beleza. Dá uma olhada que passou. Todos passaram.

19:12

Ou seja, pessoal, de alguma forma, os nossos testes não conseguiram capturar.

19:19

E isso não é bom.

19:21

Porque a partir do momento em que os nossos testes não capturaram uma falha,

19:27

possivelmente o modelo tentou resolver a resposta errada.

19:32

Ou seja, o nosso teste não está bom.

19:35

Ou ele está mockado, ou ele não fez os acertos corretamente.

19:40

Então, o mock mentiu para a gente. Então,

19:44

olha que perigo. Nós acabamos de quebrar a API,

19:46

mas se a gente rodar o teste de integração do nosso adapter antropico,

19:51

ele passa verde, porque ele usa mock cego, pessoal.

19:54

Ele mente para você dizendo que está tudo bem e o

19:57

seu CI e CD ele deixaria isso em produção.

20:01

Agora... Vamos ver o que acontece na vida real, né?

20:04

Eu vou subir a API novamente com a nova versão, tá? Agora, olha só.

20:11

Vou subir novamente com a mesma versão.

20:16

Com a versão 2 agora, tá? Beleza? Ah, desculpa.

20:27

Tem que chegar aqui.

20:29

Tem que matar aqui.

20:31

Eu tenho que matar aqui também. Então, vamos lá.

20:44

Quero um ctrl-c aqui para poder matar. Matei.

20:53

Subir novamente o serviço.

20:56

Vamos ver como é que ficou agora. De novo. No Swagger.

21:01

Vou dar um refresh aqui no Swagger. Agora tem cidade e tem estado. Vamos testar.

21:10

Eu quero Campinas, São

21:18

Paulo. Vamos ver.

21:21

Campinas, São Paulo. Campinas, São Paulo e Solarando.

21:24

Beleza? Então o nosso API está funcionando. Agora a gente vai

21:32

rodar o

21:35

nosso carinha aqui, que

21:43

é o... Cadê, meu Deus? Tá aqui,

21:46

a gente vai rodar esse cara aqui, que é o Eder Dantrop,

21:49

que estava lá com o Fusion Collie.

21:51

Vamos ver se vai ter algum impacto nele, pessoal. Deixa eu abrir outro aqui.

21:56

Deixa eu inicializar.

22:00

Deveria já ter deixado aberto, mas tudo bem.

22:03

Vamos aqui embaixo.

22:07

Beleza, vamos rodar o

22:11

teste da Tropic.

22:14

Só lembrando que é o function call, tá?

22:18

Ó, deu errado. Por que deu errado?

22:21

Ou seja, bom, quebrou, né? Deu erro 422, né? Ó, erro 422.

22:27

Unprocessable entity na cara do usuário. Então, o LLM nem errou.

22:31

Quem desmoronou foi o nosso esquema desatualizado,

22:35

né? Então, de novo, ó. Vamos ver se agora o nosso teste ia passar ou não.

22:40

Vamos ver se o nosso teste ia passar ou não. Tá?

22:43

Deixa eu ver agora. Vamos ver se o nosso teste ia passar ou não.

22:46

Agora. Ah, o nosso teste quebrou.

22:47

Então, se a gente tivesse rodado o nosso teste,

22:49

a gente ia ver que quebrou. Deu. Deu lá. Deu. Deu. Erro. Erro. inesperado, né?

22:58

Então, vamos ver, vamos aqui.

23:03

Faltou uma, faltou, faltou um argumento, né? Então, vamos aqui. Então,

23:11

o que a gente vai fazer agora? A gente vai refatorar esse código, tá?

23:16

Eu fiz, eu fiz um gabarito de refatoração, eu fiz, gente,

23:20

pra gente não perder muito tempo aqui,

23:22

eu basicamente corrigi todo o código, tá?

23:28

E com isso, usando o scriptzinho aqui, tá? Opa!

23:35

Usando o scriptzinho aqui,

23:38

vocês vão ver que eu vou mostrar...

23:41

Ele corrige o código, ele substitui os arquivos aqui,

23:46

os arquivos corretos, tá? Deixa eu mostrar para vocês antes,

23:49

né? Então, vamos ver aqui, ó.

23:51

Aqui nesse caso... ele adiciona aqui o estado, tá? Então, assim,

23:56

é isso que ele faz aqui no caso do Eder Antropic, tá?

24:01

No caso do Eder da MCP da Antropic, né? Ele precisa também,

24:05

num lugar só, né? Ele precisa vir aqui e mudar, né?

24:10

A chamada da tool, quer dizer, a chamada da tool... Não,

24:17

desculpa, isso aqui é o client, perdão.

24:19

É o Eder Server. Ele precisa chamar...

24:22

e ele precisa mudar a chamada da tu que

24:24

agora que agora também recebe estado, tá? E

24:31

eu criei um clientezinho aqui, tá, gente, da

24:34

Tropic, tá, pra gente poder ver ele funcionando usando

24:38

MCP Server, tá aqui. É o MCP cliente, foi isso que eu criei, tá? Eu criei MCP

24:42

cliente na Tropic, vou poder fazer funcionar com nosso

24:44

MCP Server ali, tá bom? Então, vamos, vamos

24:47

seguir aqui, ó. Sugestão para vocês, tá?

24:50

É usar esse script, tá? E a gente vai...

24:55

Ele está bem passo a passo.

24:57

Eu fiz isso para vocês entenderem o que precisa ser feito.

25:00

Depois, a gente roda os testes novamente.

25:12

Beleza. Porrada de teste falhou. O backend adicionou um parâmetro adicional.

25:17

Esse aqui a gente já sabia. Deixa eu expandir aqui.

25:20

Esse aqui a gente já sabia.

25:24

Antes da refatoração.

25:26

Executando o Tukoli da Tropic. Deu aquele erro com a 422.

25:30

Tá agora executando o MCP, o MCP Client nativo.

25:35

Tá, eu criei um MCP Client pessoal para a

25:38

Gente, não ter que criar, usar o Cloud, um código ou 10.

25:44

Conclui o desktop, faz, facilita demais aqui para a gente aqui no

25:48

curso, tá bom? Aqui nesse lado, tá? Ele

25:51

basicamente, processou lá, enviou a mensagem,

25:55

ele pegou a informação de volta e falou,

25:59

Desculpa, tive um problema ao tentar consultar o clima de Campinas,

26:01

parece que houve um erro ao processar a requisição,

26:04

pode ser que haja um problema temporário com o serviço de clima,

26:07

o nome da cidade precisa ser formatado de forma diferente,

26:10

Você gostaria que eu tentasse novamente alguma outra

26:12

cidade que você gostaria de consultar?

26:15

Isso aqui é LLM mostrando

26:18

para o cliente que há

26:25

possibilidades de...

26:27

de dar uma resposta, né? O Christian fica sem resposta,

26:32

né? Mas, querendo ou não,

26:34

tem que ter uma resposta. Querendo ou não,

26:35

é uma resposta que demonstra que houve um erro, tá?

26:38

Mas, diferentemente do Tukoli, né, pessoal?

26:41

Ele não estoura um erro, tá?

26:43

Vamos lá. Então, a gente vai refatorar agora,

26:46

que é basicamente, vai copiar aqueles arquivos,

26:49

Tá? Ele basicamente copiou os arquivos e substituiu

26:52

os arquivos que estavam com problema,

26:54

Tá bom? Foi isso que ele fez, tá?

26:56

Vocês podem ver que tá até com modificado aqui, tá?

26:59

Então, aqui, só para mostrar para vocês, ó.

27:02

O Eder Dantrop, que agora recebe os dois parâmetros,

27:05

esse aqui que ele tá fazendo, ele tá corrigindo, tá? Então, vamos ver agora... Opa!

27:10

Vamos ver agora... Caramba!

27:13

Vamos ver agora rodando, né? Então, ó.

27:17

Então, o MCP, refatorando o serviço central, tá?

27:21

Agora, ele também refatorou o Eder Server também, tá?

27:26

Então, agora mais. Como você percebe, foi curado.

27:28

O cliente MCP, não foi modificado. Agora, vamos ver depois da refatoração.

27:35

Obviamente, o toCalling voltou a funcionar,

27:38

porque eu fui lá e alterei na mão e adicionei lá na chamada do esquema.

27:44

Eu vim aqui e adicionei os dois parâmetros. Eu tive que fazer isso aqui na mão.

27:50

No caso do MCP Server, eu também tive que fazer. Eu fiz em um lugar só. Mas, lembrando,

27:55

a partir do momento que eu faço nesse lugar, eu não preciso,

27:59

se eu tivesse, por exemplo, aqui, o header da OpenAI,

28:03

o header da Gemini, eu não precisaria sair fazendo em todos os lugares aqui.

28:08

Por exemplo, da OpenAI, eu precisei mudar também.

28:10

Da OpenAI também aparecem dois parâmetros. Se todos estivessem usando o MCP,

28:15

eu mudaria só o MCP Server.

28:19

Então, agora, depois da refatoração, eu rodei todos os testes.

28:24

Tá, eu dei todos os testes, tá funcionando, tá? E aqui só para limpar

28:28

o ambiente aqui, tá? Sugestão, né? Executem esse aqui.

28:32

Quando tiver na máquina de você está

28:34

Voltando aqui, é o nosso resultado pessoal, vamos lá, né? E aí, esse aqui,

28:41

Olhando somente um SDK,

28:43

Tá? Imagina que aqui é o da Anthropic, no caso, tá bom? Então, olha lá,

28:46

Linhas de código e qualquer linha,

28:48

Linhas de código e esforço para fazer um tool call, aproximadamente 15 linhas,

28:51

Tá? Que é o esquema mais o adapter. No caso do MCP, são 6 linhas de código.

28:56

É acoplamento API real, ou seja, no caso do Tutocall, ele está espalhado.

29:03

Para cada provider que você tem, a definição de um esquema,

29:07

Você tem um arquivo, no final do dia, que é o host,

29:11

Você tem um arquivo em cada host. Então, ou seja, da OpenAI tem o seu,

29:16

O de Gemini vai ter o seu, no caso do MCP é centralizado, está apenas o servidor.

29:21

O custo de troca de LLM, né? Você tem que reescrever o esquema 100% do zero.

29:26

No caso do MCP, o custo é zero.

29:27

Você não tem que mexer nada. O servidor já é universal, tá?

29:31

Proteção dos testes. Como vocês viram ali, pessoal,

29:33

Mock cegos dão falso verde na quebra, né? No caso do MCP,

29:38

O contrato é real, tá? É teste cliente na fonte, tá?

29:41

E para refatorar, você refatora um arquivo por projeto, tá?

29:45

Ou seja, de novo, se você tem... Se você tem vários providers,

29:49

Seria um arquivo para cada provider que você tem que refatorar.

29:52

E no caso do MCP7, não importa a quantidade de providers,

29:55

Você faria somente uma vez, tá? Beleza?

30:00

Então, a tese desta aula, tá?

30:05

Realmente, a forma que a Anthropic trouxe de resolver o problema de N para M,

30:09

De chamada de tools, tá? A partir de modelos, tá? É sensacional, tá, gente?

30:14

É realmente fundamental para ganho de escala.

30:18

E foi um marco super importante no final de 2024,

30:23

Logo de 2025 e agora em 2026, tá bom? Obrigado, pessoal.

30:28

Vejo vocês na próxima.

## Resumo IA

[RESUMO_IA]