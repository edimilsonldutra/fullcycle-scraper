Módulo: Protocolos de Comunicação\
Aula: [LAB: Comparativo Prático 1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18589)

## Resumo da aula

O experimento compara três implementações da mesma consulta de clima contra a mesma API externa: Anthropic com tool calling, OpenAI com tool calling e MCP com FastMCP. O objetivo não é descobrir qual abordagem “funciona”, porque as três funcionam, mas localizar onde o impacto aparece quando o contrato externo muda. Retomando o cenário de clima já usado antes, a nova camada do exemplo é operacional: medir acoplamento, esforço e refatoração diante de uma mudança real de API.

getWeather fica fora do processo da aplicação e é exposto por um Weather Service simulado. Isso força a integração a lidar com uma dependência real de contrato, mantida por “outra equipe”, em vez de esconder a função localmente. O ponto didático está em observar que o consumidor não controla a evolução da interface e, por isso, precisa de proteção por testes e desenho de integração.

O ambiente exige Python 3.10 ou superior, acesso ao repositório do lab e a subida da API com Uvicorn na porta 8000. Antes de integrar com LLM, a rota deve ser validada manualmente em localhost:8000/docs, usando o Swagger do FastAPI para inspecionar endpoint, payload e respostas. Essa etapa reduz ambiguidade, porque separa erro da API externa de erro da camada de integração com modelo.

A API mockada inclui cidades e entradas tortas pensadas para comportamento de LLM, como variações de formatação e ambiguidades. Esses casos existem para expor falhas que não aparecem em um caminho feliz artificialmente limpo. O contrato observável não é só o JSON de sucesso; ele inclui também erros, sugestões de correção e respostas a parâmetros malformados.

Os testes do laboratório congelam duas dimensões independentes: contrato de dados e contrato de erro. Os testes de TestWeatherAPI verificam se a API continua entregando a estrutura esperada, enquanto TestWeatherAPIEdges protege os comportamentos de borda que um LLM pode acionar ao formatar argumentos. Essa proteção evita falso verde em integração contínua quando a API muda silenciosamente.

A comparação usa cinco métricas: linhas de código, acoplamento à assinatura real da API, custo de troca de LLM, proteção por testes e custo de refatoração. Linhas de código medem esforço inicial; acoplamento mede quantos arquivos conhecem o contrato externo; troca de LLM mede o quanto a base depende de SDKs específicos; testes medem capacidade de detectar quebra real; refatoração mede o custo inevitável quando a V2 chega. O valor do experimento está em observar essas métricas juntas, não isoladamente.

Tool calling, já definido anteriormente, reaparece aqui como implementação local acoplada ao SDK e ao runtime do provider. No experimento, Anthropic e OpenAI exigem adaptações paralelas para a mesma API, com pouca ou nenhuma reutilização entre si. Isso torna visível o custo estrutural do N por M no nível microscópico: a mesma capacidade precisa ser reembalada para cada integração.

No caminho da Anthropic, logs em nível debug ajudam a enxergar o tool_use_id, a ida da chamada ao modelo e o retorno da resposta final. Esse tipo de inspeção é importante porque mostra o fluxo real de execução, não apenas a abstração do SDK. Quando a integração falha, o log revela se o problema está no schema enviado, no argumento gerado pelo modelo ou na chamada à API externa.

FastMCP reduz o trabalho manual ao expor a função externa como tool por meio de um decorator. Em vez de reescrever schemas manualmente para cada host, a função getWeather é publicada uma vez no servidor MCP. O ganho não é “mágica”; é centralização do contrato em um ponto reutilizável por múltiplos consumidores.

O schema da tool pode ser inferido automaticamente a partir de type hints, como city: str, e da docstring da função. Isso transforma assinatura e documentação em parte ativa do contrato exposto, o que aumenta consistência e reduz duplicação. Em integrações com LLM, docstrings semanticamente precisas também ajudam o modelo a usar a tool com menos ambiguidade.

O MCP Inspector permite observar a conversa real em JSON-RPC, incluindo mensagens como tools/list e tools/call. Como JSON-RPC já foi definido anteriormente como wire format do MCP, o ponto novo aqui é o uso operacional dessa visibilidade para depuração. Inspecionar as mensagens ajuda a confirmar discovery, invocação e argumentos efetivamente trafegados entre host e servidor.

A V2 do Weather Service introduz um novo parâmetro obrigatório, state, porque a cobertura deixa de ser apenas São Paulo e passa a incluir o Brasil inteiro. Essa mudança resolve a ambiguidade entre cidades homônimas em estados diferentes, mas revela imediatamente onde o acoplamento estava escondido. O erro 422 funciona como sinal concreto de quebra contratual e obriga a localizar todos os pontos que conheciam a assinatura antiga.

Quando a mudança ocorre em implementações por tool calling, cada adaptação que embute a assinatura da API precisa ser revista no respectivo projeto ou provider. Quando a mudança ocorre no servidor MCP, a correção tende a se concentrar no ponto central que encapsula a API externa, enquanto os hosts continuam plugando no mesmo protocolo. A diferença prática não está na capacidade de chamar a API, mas no número de lugares que precisam mudar para preservar o produto.

A métrica decisiva não é quem coloca a integração de pé mais rápido no primeiro dia, mas quem sofre menos quando o mundo externo muda. Esse laboratório transforma uma discussão arquitetural abstrata em evidência observável: o custo aparece na manutenção, na troca de provider, na cobertura de testes e na refatoração após mudança de contrato. A decisão entre abordagens passa a ser guiada por impacto operacional mensurável, não por preferência estética.

## Transcrição

00:01

Oi pessoal, tudo bem? Vamos lá,

00:03

vamos para o nosso laboratório de cooperação, cooperativo prático. Vamos lá? Bem,

00:10

esse lab tem seis blocos. Então,

00:13

primeiro vamos fazer o setup e subir a API externa que chama Weather Service,

00:18

muito parecida com aquela que a gente viu

00:20

no exemplo de cooperação da chamada de função.

00:27

Nantropic, no PNI e no Gmini, não sei se vocês lembram,

00:31

mas já já eu falo sobre eles aqui.

00:33

Depois nós vamos consumir a CPI com o Tocoli, Nantropic,

00:36

que é exatamente o que a gente fez lá atrás. Vocês vão ver aqui, pessoal,

00:41

aqui eu dei uma focada mais no provider, em termos de execução geral,

00:45

mas vocês vão ver o código tanto da PNI como Nantropic, que seria...

00:52

o próximo passo tá seja não só fazer para tu colhe

00:55

para troca fazer para apanhar vou mostrar para vocês

00:57

lá no código é na terceira etapa nós vamos fazer

01:01

a mesma chamada via mcp com flash mcp tava aí vocês

01:05

vão ver a diferença tá depois vem a parte principal onde

01:08

que a gente muda o contrato de API a

01:10

gente observa o impacto né e no final a gente a

01:13

gente faz um comparativo ele exige avaliação tá bom então

01:17

A ideia é simples, a mesma API, três caminhos,

01:20

depois a mesma mudança de contrato e aí que o custo real aparece.

01:27

Beleza, então antes de entrar no código,

01:29

vamos alinhar a nossa motivação aqui. Ou seja,

01:32

tu colhe versus MCP pode parecer uma discussão abstrata de arquitetura,

01:36

mas essa discussão muda de figura quando você coloca uma integração em produção.

01:42

Imagina um cenário super comum, você tem várias ferramentas, o tools,

01:47

usa mais de um vendor de LLM, como a Tropic ou PDA,

01:51

e de repente uma API externa muda o contrato.

01:54

E não é um caso raro.

01:56

É o tipo de coisa que acontece quando outra equipe evolui um serviço

01:59

e diz a partir de hoje o parâmetro X é obrigatório. Quando avisa.

02:04

Então esse LAB simula esse exato problema em escala pequena, obviamente.

02:08

Todo mundo vai consumir a mesma API externa de clima, que é o GetWeather.

02:15

só que por três caminhos diferentes, via Anthropic to Collie,

02:19

via OpenAI to Collie e via MCP.

02:22

Então, a primeira conclusão do LAB vai ser simples,

02:25

as três abordagens funcionam. Então, a nossa pergunta aqui é,

02:29

a nossa pergunta não é qual funciona,

02:32

a verdadeira pergunta é quando a API muda, onde o impacto aparece.

02:36

Então, no meio do LAB,

02:38

nós vamos simular que o tio do back -end publicou uma V2 da API.

02:43

Agora... Ah, só um parênteses, tá?

02:46

Essa API, pessoal, essa API de GetWeather, por uma questão aqui do sistema,

02:51

imagina assim, tá bom? Então, o sistema aqui que a gente está simulando,

02:54

ele só funciona na versão 1 da API para o estado de São Paulo.

02:58

Eles acharam o seguinte, caramba, vamos... Coisas de decisões, né?

03:03

Não necessariamente as melhores, mas as pessoas falaram,

03:05

gente, por questão de simplicidade,

03:07

vamos só fazer para o estado de São Paulo,

03:08

Que é onde o nosso sistema atende mesmo, tá?

03:11

Só que aí o cara do comercial foi lá e vendeu para o Brasil inteiro. Aí eu penso,

03:15

Vamos ter que fazer uma nova API, uma V2 da API,

03:19

que eu vou precisar adicionar a sigla de estado.

03:21

Por que isso, pessoal? Já imaginaram? Cidades que são homônimas,

03:26

que escrevem do mesmo jeito em estados diferentes, vocês vão ver o impacto disso.

03:30

É o que pode acontecer.

03:35

E agora enviar a sigla do estado passou a ser obrigatória,

03:38

e aí a gente vai medir na prática quantos arquivos quebram com o

03:42

Erro 422 e precisam ser abertos e refatorados em cada uma das abordagens.

03:47

Bem, esse é o ponto central.

03:49

O problema real não é escrever um adaptador no primeiro dia.

03:52

O problema é manter dezenas de adaptadores vivos quando o mundo externo muda.

03:57

Então, o que dói não é escrever o adaptador,

04:00

é refatorar em 80 lugares diferentes quando o controle muda, quando o contrato muda.

04:05

E é a partir daqui que o MCP deixa de ser uma

04:08

ideia bonita de arquitetura e vira uma resposta operacional pragmática. Aqui

04:13

é o centro do laboratório.

04:15

Nós vamos construir a mesma funcionalidade exata como eu falei.

04:22

Enquanto vocês estão ali programando, vocês vão medir tudo.

04:28

Não há xismo, mas em números reais.

04:31

Primeiro, quantas linhas de código...

04:33

Puras você gasta para construir os adaptadores.

04:37

Segundo, a métrica de acoplamento.

04:40

Quantos arquivos espalhados no seu projeto sabem a assinatura real dessa API?

04:45

Para a gente entender o impacto quando ela mudar.

04:48

Terceiro, o custo de dependência. Se a gente trocar da Antropic para o PNI amanhã,

04:53

o que acontece com sua base de código?

04:56

Ou se a gente adiciona o Gemini.

04:59

Quarta, confiança na integração contínua, no Continuous Integration.

05:04

Que tipo de erro seus testes de IA realmente pegam?

05:07

Se a API externa mudar o JSON dela enquanto você está dormindo,

05:12

os seus testes unitários vão estourar ou vão dar

05:14

um falso no verde e quebrar a produção?

05:17

E, finalmente, a prova de fogo, o custo da refatoração.

05:20

Quando a API inevitavelmente mudar de versão,

05:23

quantos arquivos você vai ter que alterar para não parar seu produto?

05:26

Então, são pontos... que a gente vai levantar ao longo do nosso laboratório.

05:33

E aqui, pessoal, um tema para a gente pensar.

05:37

A métrica mais importante da nossa profissão não é

05:40

quem coloca a porta de pé primeiro.

05:42

É a arquitetura de quem muda e sofre menos quando o mundo externo muda.

05:48

Essa é a métrica.

05:50

Qual a arquitetura de quem muda e sofre menos quando o mundo externo muda?

05:56

Então, chegamos ao cerne deste laboratório. Nós vamos construir a exata,

06:00

nós vamos construir a mesma funcionalidade, tá?

06:03

E, de novo, pessoal,

06:06

aqui a ideia é vocês realmente exercitarem não só a solução,

06:12

mas exercitarem um caso real,

06:17

tá? Se entenderem o impacto na pele aqui, tá?

06:19

No laboratório. Bem, com o ambiente controlado.

06:23

Então, antes de rodar o LAB,

06:25

vamos olhar rapidamente a questão do que a gente precisa ter. Primeiro,

06:29

confira a versão do seu Python, com Python menos menos version.

06:33

A ideia está no Python 3.0 ou maior.

06:36

Depois, entra na pasta do LAB.

06:39

Tem um caminho aí, pessoal, para vocês. Eu até coloquei no slide anterior.

06:47

Deixa eu ver. Está aqui.

06:52

Eu coloquei aqui para você usar o GitHub, então essa aqui é a parte do Lab, tá bom?

07:01

Lá dentro, pessoal, vocês vão ver o seguinte,

07:02

inclusive tem um vídeo lá dentro super completinho, tá?

07:06

Que vai explicar isso aqui para vocês, tá bom? Todos os passos,

07:09

não quero ficar entrando aqui no detalhe do detalhe,

07:11

mas assim, os pontos mais importantes, tá?

07:15

Também o segundo ponto mais importante,

07:17

é que vocês vão ver que nos exemplos eu usei...

07:20

É até para sair um pouco de OPNI, né? Eu usei até...

07:23

Eu usei uma chave de criptografia, da criptografia P & Q, né?

07:27

Eu criei uma chave de criptografia P & Q para eu poder usar aqui no laboratório. Ou seja,

07:31

cada um de vocês aí vai ter que tomar essa decisão,

07:34

porque vocês vão ter que usar uma chave de vocês, né?

07:37

Se vai ser uma criptografia, vai ser uma OPNI, né?

07:39

Agora, se não quiser usar a chave, tá?

07:41

Tem como usar a fake LLM, só para vocês entenderem o conceito,

07:44

tá? Ele meio que simula os resultados lá, tá bom?

07:47

Mas assim, pessoal, vocês vão ver que para o laboratório o custo é super baixo. Eu acho que vale a pena.

07:56

Então, etapa zero, pessoal. A ideia é que você suba uma API externa.

08:01

Aqui que começa o laboratório de verdade.

08:03

A função getWeather não está embutida no nosso código.

08:07

Ela está exposta por uma API externa simulada,

08:11

chamada WeatherService. Então, a ideia aqui é muito simples.

08:15

Outra equipe mantém essa API e você só consome. Você não controla o contrato,

08:19

então aqui tem todos os passos de novo,

08:22

lá no README vão ter todos os passos para poder subir essa API,

08:26

a gente vai usar o vCorn para poder subir na porta 8000,

08:30

vocês vão ver que ela vai expor a função GET, GETWEATHER, GETWEATHER CITY,

08:37

que aí você põe lá a cidadezinha,

08:41

uma das cidades que estão lá, MOCARES, obviamente,

08:47

A API, propriamente dita, ela está mockada, tá? Depois eu vou mostrar para vocês, né?

08:53

Ou dá uma navegada lá, vocês vão ver que são cidades específicas, tá?

08:59

E uma sugestão para vocês, antes de vocês conectarem a Tropical PNA,

09:03

dá uma olhada lá no local roxo,

09:06

local roxo, dois pontos, na porta 8 mil, na barra DOCS,

09:10

tá? E vocês vão ver o Swagger lá dentro,

09:13

tá? Vocês vão poder testar manualmente, né?

09:16

Vocês vão ver a rota, vocês vão observar o JSON, enfim, tá?

09:18

Bem interessante essa funcionalidade que o

09:24

Face API disponibiliza para a gente, tá?

09:29

Você também vai notar que existem edge cases pensados para LLM,

09:33

por exemplo, né? Campinas e Minozco.

09:35

São Paulo com a Descore, né? Enfim, né? Isso é importante até para vocês.

09:40

Checarem os tipos de erro, tá?

09:43

Bem, a gente vai rodar. Então, assim, a expectativa são 12 testes.

09:47

Ah, desculpa. Agora a gente vai...

09:49

A ideia é que vocês rodem os testes, tá? A gente tem... Eu fiz lá uma...

09:53

Já está desenvolvido lá no laboratório um conjunto de testes unitários.

09:57

Já estão prontos para vocês,

09:59

né? Para vocês... Eu gosto, inclusive,

10:01

eu sugiro que vocês estudem os testes unitários,

10:04

né? Estudar os testes unitários é importante até para

10:05

vocês entenderem o que se espera de cada...

10:08

de cada funcionalidade, né? Através dos testes,

10:11

entender os testes também é uma forma didática de aprender melhor.

10:14

Então, se você está na dúvida,

10:15

entenda os testes, que talvez vai te ajudar também mais, que eu quero dizer, tá?

10:20

Então, são 12 testes lá, tá? Então, tem 4 testes do TestWeather API, né?

10:25

Ou seja, congela o contrato de dados, garante que a API fornece lá a temperatura.

10:29

Tem 8 testes do TestWeather API Edges,

10:33

né? Que congela o contrato de erro, né?

10:35

Mas garante que as variações tortas que usa o LLM...

10:38

que o LLM devolve sugestões de correção, são duas dimensões independentes. Então,

10:44

tudo isso que acabamos de fazer se conecta com duas métricas cruciais do nosso LAB,

10:48

a métrica 2, que é de acoplamento.

10:52

Guarde isso para a sua vida, pessoal. Se integrações com agentes de A,

10:55

você não testa a sua cama infeliz,

10:57

você testa se a tua é resiliente ao caos e o que o

11:00

modelo pode gerar na hora de formatar os parâmetros por conta do não determinismo.

11:08

Aqui, a etapa 1 e a etapa 2, pessoal,

11:12

é a história lá do Tukoli, seja da Anthropic, seja da OpenAI, tá?

11:16

Acho que como a gente já falou disso aqui antes,

11:19

acho que não quero entrar no detalhe,

11:21

dar uma olhadinha aqui depois com calma nesse slide, tá?

11:25

Mas, enfim, tá? Ou seja, tem um ponto interessante aqui, na verdade, tá?

11:31

A minha sugestão aqui, pessoal, até eu coloquei aqui,

11:35

é de usar a Anthropic e a Discord Log igual debug.

11:39

Isso ajuda demais, que é como debugar.

11:43

Isso ajuda demais a vocês entenderem o que está acontecendo ali debaixo do capô.

11:53

Enfim, quando vocês executarem,

11:55

vocês olharem os logs que o Anthropic Log Debug cuspiu no terminal,

12:01

dá para ver exatamente o To Use ID chegando no

12:04

modelo e voltando na nossa requisição de resposta.

12:07

Então, no fim... E no fim a chamada finaliza a execução com stop reason,

12:13

going, return, entregando o texto final.

12:17

Agora, de novo, sempre indo na linha dos testes,

12:21

agora a gente vai garantir que está blindada e vocês vão lá rodar o PyTest,

12:25

testes barra teste antrópico.

12:28

Esse teste antrópico testa exatamente

12:32

esse código usando o toCalling.

12:36

De novo, a expectativa, três testes verdes, tá?

12:39

Eles garantem que o esquema está no padrão do Anthropic.

12:41

Que a data é batida na API e que o parâmetro será repassado corretamente, tá?

12:47

Quer mais? Quer mais?

12:52

Bem, né?

12:54

Reflexão, tá, gente? Funciona? Funciona, né? Não apoca o caminho mais rápido,

12:58

né? Mas tira um, né? Assim, pra gente ficar...

13:03

A função que conhece a assinatura do mundo externo,

13:07

ela vive no mesmo processo do orquestrador,

13:09

do LLM, quando a gente fala de Tukolin,

13:11

tá? Então, assim, enfim, dê uma olhada, faça a sua própria,

13:16

traga a sua própria visão crítica em cima do problema aqui, tá? Beleza.

13:21

Gente, aqui, dar o PNA é a mesma coisa do Dantropik, não vou me repetir aqui.

13:27

Use esse slide, dê uma pausa, dê uma navegada, uma entendida, tá? De novo.

13:34

Use o README que está lá no laboratório.

13:39

Ele também está bem explicadinho lá.

13:42

Eu vou abrir daqui a pouco para vocês.

13:44

Isso aqui é só para a gente passar de maneira mais macro.

13:49

E, de novo, o famoso N por M problema que a gente discutiu até aqui,

13:56

a gente vai conseguir ver ele no microscópico. Então,

13:59

duas funções idênticas tocando a mesmíssima API,

14:02

só que... para agarrar dois SDKs diferentes,

14:05

tá? Então, assim, zero linhas foram aproveitadas entre os dois projetos, tá?

14:09

Imagine 20 tools em vez de uma. Três SDKs do seu produto.

14:14

Daqui a seis meses, entra o Gemini, por exemplo, tá? Então, para cada API externa,

14:18

três cópias cegas da função adaptada espalhadas pelo seu repositório, tá?

14:22

Essa multiplicação silenciosa é a que mata a velocidade de times em produção, tá?

14:29

Tá, agora, pessoal, a parte que começa a ficar interessante, né?

14:32

Que é o MCP com o FastMCP, tá? Então, assim, agora

14:37

é a questão da abstração do protocolo, tá? Ou seja,

14:44

você escreve um servidor que conhece a API externa,

14:47

né? E, obviamente, todos os hosts eles podem plugar,

14:50

né? Não importa qual host é, inclusive, pode ser o seu custom,

14:53

que é o que a gente vai fazer aqui, inclusive, tá bom? Bem...

14:58

E a beleza do negócio, pessoal, é o decorator, tá? Que o FastMCP faz para a gente.

15:03

Você coloca o decorator MCP2 em cima da função get to add,

15:07

tá? E vocês vão ver, cara,

15:09

que basta isso para poder disponibilizar a ferramenta, tá?

15:13

Ou seja, são seis linhas reais, tá?

15:16

O esquema é inferido automaticamente do type hint do sit 2 .str,

15:23

né? E também, gente, do docstring. Então, gente, assim, ó.

15:28

Façam docstrings que tenham semântica.

15:32

Aqui não está mostrando os docstrings bonitinhos,

15:34

mas se você for lá no código, vocês vão ver que está bem bonitinho lá.

15:38

Inclusive aqui é super importante

15:42

a gente perceber quanto a partir

15:46

de agora semântica é tudo quando a gente fala de LLM.

15:49

Então quanto melhor semântica, quanto melhor explicado, com detalhe correto.

15:59

Você diminui os riscos de alucinação.

16:02

E aqui,

16:04

pessoal, como debugar?

16:07

Usa o MCP Inspector. O MCP Inspector, ele roda,

16:12

Ele mostra cada JSON RPC voando de um lado para o outro.

16:15

Tem os tools / list na conexão,

16:17

tem o tools / call quando você invoca. Então, enfim, gente,

16:21

o MCP Inspector realmente é um caso à parte.

16:24

É uma ferramenta super poderosa para

16:27

a gente poder fazer o nosso lab,

16:31

e mesmo quando vocês estiverem trabalhando no projeto de vocês,

16:36

no dia a dia, MCP Inspector é super importante para a gente poder debugar o MCP.

16:43

Bem, a etapa 4 é quando o contrato da API muda.

16:49

O que aconteceu? Lembra da história lá antes? Só funcionava para São Paulo,

16:54

porque o sistema só englobava o estado de São Paulo,

16:56

só que agora o comercial foi lá e vendeu para o Brasil inteiro.

16:59

Então, de novo, expandiu a cobertura de São Paulo para o Brasil inteiro.

17:03

Então, o parâmetro de estado passou a ser obrigatório.

17:06

Olha só, olha que interessante.

17:11

É um cenário clássico de evolução do produto.

17:16

E o que acontece? Quem usa Tukoli tem que caçar,

17:21

Tem que caçar e refatorar um arquivo para o projeto, espalhado pela empresa,

17:24

por exemplo. Só que quem usa MCP refatora um arquivo no total.

17:28

Eu não quero dar spoiler em cima disso aqui não, pessoal,

17:31

porque isso vocês vão ver que vai fazer parte do resultado final,

17:35

vocês entenderem essas métricas. Mas, de novo, os clientes, os hosts,

17:38

eles apenas plugam. Então, quando a API exige um parâmetro novo,

17:42

o host atualiza... super rápido,

17:46

ele é atualizado pelo próprio protocolo do MCP, tá? Bem,

17:56

obviamente vocês vão ver que tanto o Tukoli da OpenAI

18:00

quanto o Tukoli da Anthropic que vai quebrar,

18:02

né? E do FastMCP ele vai quebrar uma única vez, né? Esse aqui é o ponto. Então,

18:07

se você estiver usando o Tukoli, ele vai quebrar em todos os lugares.

18:10

Se você estiver usando o MCP,

18:11

ele vai quebrar em um lugar só, você corrige em um lugar só, tá? Bem, o que mais?

18:20

Então aqui, pessoal, agora, esse aqui é o momento em que você pausa o vídeo,

18:24

eu espero uns segundos do lado de cá, que equivale a alguns minutos aí para vocês,

18:29

para a gente poder repassar o lab juntos e preencher essa tabela,

18:33

para a gente poder refazer os passos aqui e ver o que vocês...

18:39

Obviamente, pessoal, não tem resposta certa ou errada,

18:42

não tem melhor ou pior, mas assim, mas...

18:46

É super importante vocês tentarem e aplicarem aí e

18:50

seguir o que está lá no repositório,

18:52

que está bem guiado lá, bem roteirizado, tá bom? Beleza? Boa, pessoal.

19:02

Então, vamos fazer o seguinte.

19:03

Agora é a hora que eu passo para a parte do laboratório, tá?

## Resumo IA

[RESUMO_IA]