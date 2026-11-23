Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16371)

## Resumo da aula

Modelo de bigrama, ou 2-grama, estima a próxima palavra usando apenas a palavra imediatamente anterior. Ele funciona como uma simplificação extrema da geração token a token já vista antes: em vez de considerar um contexto amplo, reduz a decisão a pares locais de palavras. Isso foi útil historicamente porque permitia modelar linguagem com estatística simples e custo computacional baixo. O problema é que linguagem natural não se sustenta apenas com transições locais frequentes.

Nesse tipo de modelo, gerar texto significa escolher a continuação mais provável com base nas combinações observadas no treinamento. Se “bom” aparece muitas vezes seguido de “dia”, o sistema aprende que “dia” é uma continuação forte para “bom”. Essa lógica captura regularidades reais da língua, mas só no nível de vizinhança imediata. Ela não distingue bem quando a continuação correta depende de intenção, tema ou estrutura mais longa.

Dependências de longo prazo são relações entre partes distantes de uma sequência que ainda precisam permanecer conectadas para o texto fazer sentido. Em linguagem humana, uma ideia introduzida no início pode orientar várias frases depois, mesmo sem repetição literal. Um modelo de bigrama falha nesse ponto porque sua janela operacional é curta demais para preservar esse vínculo. Por isso ele pode produzir frases localmente plausíveis e globalmente desconexas.

Retomando o cenário de geração de texto, o bigrama não mantém memória efetiva do que já foi construído além do par atual. Ele também não projeta um objetivo global para a frase, como concluir uma ideia, manter um tópico ou preparar a próxima informação relevante. O resultado é uma sequência que avança sem plano e sem histórico amplo. Isso explica por que esses modelos perdem coerência mesmo quando cada passo isolado parece estatisticamente aceitável.

Quando o modelo aprende que uma combinação ocorre com frequência, ele tende a reutilizá-la excessivamente. Na frase “o gato preto dorme no sofá”, se “gato preto” for um par muito forte, a geração pode cair em repetições como “o gato preto dorme no sofá, gato preto” ou repetir o bloco inteiro. Esse comportamento não surge de intenção semântica, mas de uma preferência estatística local. A consequência prática é texto fragmentado, repetitivo e com aparência de looping.

Um bigrama pode acertar transições curtas e ainda assim fracassar como modelo de linguagem fluida. “Gato preto” e “preto dorme” podem ser pares aceitáveis, mas isso não garante que a frase inteira preserve sentido, progressão e unidade temática. Coerência local significa que pequenos trechos parecem plausíveis; coerência global exige que o texto inteiro se sustente como raciocínio. Modelos antigos ficavam presos no primeiro nível.

Esses modelos não compreendem semântica no sentido forte; eles operam sobre padrões de ocorrência. Isso basta para reproduzir associações frequentes, mas não para acompanhar construção de significado ao longo de uma sequência maior. Linguagem envolve relação entre termos, contexto acumulado e continuidade de raciocínio, não apenas proximidade entre palavras. Por isso a limitação não era só de qualidade superficial, mas estrutural.

A passagem para arquiteturas mais avançadas aconteceu porque modelos estatísticos locais não sustentavam linguagem natural com fluidez, memória e contexto amplo. Retomando a progressão histórica já vista, o ganho de processamento ajudou, mas a mudança decisiva foi representar linguagem com mecanismos capazes de conectar partes distantes da sequência. Essa transição prepara diretamente a entrada nos LLMs, que existem justamente para superar ausência de memória local, repetição e perda de coerência. A simplificação com bigramas é intencional porque deixa visível o problema que os modelos modernos precisaram resolver.

## Transcrição

00:00

Fala galera, beleza? Vamos dar mais um passinho aqui no nosso aprendizado sobre IA, mas antes da gente evoluir, eu queria pedir um enorme favor pra vocês. Eu vou precisar fazer uma coisa aqui pra gente conseguir entender e a gente conseguir aprofundar nos modelos e nos

00:19

nas estratégias de IA, beleza? O que eu vou precisar fazer? Eu vou precisar abstrair o máximo do que a gente tá falando sobre o conhecimento de como funciona e como que são os frameworks e como é que são os algoritmos de IA, pra daí depois a gente começar a aprofundar. Por quê? Porque a partir de agora eu vou entrar num modelo mais técnico, a gente vai ter que entrar um pouquinho numa parte um pouco mais chata, numa parte que a gente precisa aprofundar mais de forma técnica.

00:47

Pra eu não chegar e já jogar na cabeça de vocês aqui um monte de estratégia de framework e de álgebra pra vocês entenderem como funcionam os modelos, eu vou tentar abstrair pra gente chegar num nível mais simplificado e depois aprofundando. Por quê?

01:03

Porque se não, o que eu precisaria fazer é passar um monte de base literária pra vocês pra gente conseguir chegar no mesmo nível de conversa e conseguir evoluir isso. Então, pra não fazer isso, como eu tô aqui pra ser um facilitador, o que que eu vou tentar fazer? Eu vou trazer vocês pra uma abstração simplificada e vou ir evoluindo ela e complicando ela ao longo das aulas. Então vocês vão notar que, por exemplo, quando vocês chegarem na última aula, se vocês assistirem essa de novo, vocês vão falar, nossa, o Natan falou ali uma coisa tão simples, é tão mais complexo do que isso.

01:33

Tudo bem. É isso mesmo que eu quero que aconteça, tá bom? E se você já conhece um pouco mais de A, possivelmente você vai assistir essas primeiras aulas e vai falar, pô, Nathan, você simplificou demais, faltou isso, faltou aquilo, faltou aquilo outro. Isso mesmo. É proposital. Eu vou trazer de uma forma simplificada e vou ir colocando mais complexidade ao longo das nossas aulas, tá bom? Então, a primeira coisa que a gente tem que entender é da onde a gente veio. Então, uma das coisas principais é a gente compreender quais eram os modelos que a gente tá falando de IA generativa

02:02

para depois conseguir chegar no conceito de LLMs. LLMs são os modelos que a gente usa principalmente ali no chart GPT-4, que a gente usa no DeepSeek, que a gente usa nos principais modelos de geração de ar hoje em dia. Então, normalmente a gente está usando este conceito, LLMs, beleza?

02:21

Mas antes da gente chegar nisso, eu preciso explicar como a gente chegou nisso, porque a gente chegou nisso, quais problemas a gente tinha pra ter que ir pra um LLM. Aí depois eu aprofundo com vocês o que é o LLM, beleza? Então vamos partir do princípio de como começou a surgir os modelos de IA generativa. Então vamos voltar um pouquinho

02:43

na estratégia e na lógica que a gente tinha pra codificação. Então, pensa o seguinte, a lógica básica que a gente tem é uma lógica de sim ou não, certo? Então, quando a gente olha pra computação, a gente basicamente tá falando de ligado ou desligado, sim ou não, a gente tá falando de binário, no fim das contas, a gente tá falando de zero ou um...

03:01

Quando a gente vai evoluindo nessa linguagem, a gente vai entendendo que isso é muito bom pra resolver raciocínio lógico e contas. Então a gente partiu de um modelo matemático, que era basicamente uma calculadora, e foi evoluindo ela, transformando em um poder de computar as coisas, beleza? Esse poder de computar, esse poder de você ir fazendo operações no fim das contas matemáticas,

03:24

fez a gente ir evoluindo. Então a gente criou as linguagens, conseguiu criar todas as automações que a gente tem e assim por diante. Tudo isso por trás segue muito uma lógica de tomada de decisão baseada em um caminho. Você tem um caminho, outro caminho, daí desse outro caminho você diverge pra outro e assim por diante. Então normalmente é uma tomada de decisão, depois a próxima tomada de decisão, depois a próxima tomada de decisão e assim por diante.

03:47

Esse era o básico, beleza? Por quê? Porque se eu pedir pra você contar como você toma as decisões no dia a dia, possivelmente você vai me contar desse jeito, mas não é desse jeito. Você não toma as decisões com tomadas de decisão, sim ou não. Tomadas de decisão, sim ou não. Você toma as suas decisões mais com base em estatística e probabilidade. Tomadas de decisão, acho que é mais pra cá do que pra cá. Então vamos pra cá. Daqui, acho que é mais pra cá do que pra cá. Daqui.

04:15

Olhando agora tem um contexto diferente, pode ser que eu tenha que voltar. Então você vai tomando as decisões com base no axômetro. Vamos ser bem honestos, como que a gente tangibiliza o axômetro? É probabilidade, certo? Então se eu te perguntar se tá

04:30

hoje, aqui onde eu tô. Vocês estão vendo a minha aula. Eu tô com frio? Você pode falar, pô sim Nathan, parece que você tá com uma blusa de manga comprida, parece que é um dia frio. Mas e se não? Você não sabe, você acha, você tá colocando alguns aspectos que podem colocar isso. Então, por exemplo, a iluminação que tá saindo aqui da janela, que eu deixei proposital pra gente entender como tá o dia. A gente pode olhar sobre a minha blusa, poxa, ah, ele tá de blusa, então deve tá frio. Tudo isso você tá, tá

04:58

inferindo, você está colocando algumas informações que você está vendo com base nisso, falando que é ou não uma realidade, certo? É assim que a mente humana funciona, e isso que começou a movimentar as I.A.S. Então a gente saiu desse modelo de sim ou não básico e começou a ir para um modelo de

05:15

probabilidade, um modelo de estatística, tá bom? Então, isso é a primeira coisa que a gente tem que pensar. Então, a gente sai de um modelo que era assim, não básico, e a gente começa a ir para um modelo baseado em estatística simples. Aí começa como a gente vai para o conceito da coisa. A estatística simples é tão simples quanto qual a maior probabilidade, como acabei de mostrar para vocês. Eu ainda estou numa lógica

05:40

de sim e não, certo? Mas com base em probabilidade e não com base em um critério firme, certo? Então, basicamente, a gente parte deste princípio. Então, a gente ainda tem ali regras rígidas de conhecimento que são limitados. Então, a gente tem ali os modelos que eles vão conseguir gerar uma linguagem, mas sem tanta fluidez.

06:01

eles têm mais dificuldade para isso, têm mais dificuldade de gerar uma coerência, criatividade e assim por diante. Então a gente consegue fazer uma linguagem simples rolar, mas não uma linguagem fluida.

06:16

bom? Então, a partir desse momento eu começo a ter uma visão de geração, tá? Que eu tô querendo dizer assim, eu consigo gerar um texto, eu consigo gerar uma imagem, eu consigo gerar coisas, mas eu gero coisas simples e possivelmente sem fluidez, sem conexão. Então, eu não consigo gerar algo complexo como a mente humana faz. É como se a gente tivesse começando a criar um cérebro. Então, aqui a gente já tem muita simplicidade nessa criação. Então, são regras simples e uma linguagem não fluida. Então, a gente parte desse

06:46

princípio. Então, quando a gente está falando disso, a gente tem um próximo passinho que a gente tem que dar. A gente começa a ter uma mudança ali tecnológica acontecendo. Então, a gente tem uma grande mudança em poder de processamento e assim por diante. E a gente também tem uma mudança conceitual muito grande. A gente para de entender

07:07

essa tomada de decisão com representação de linguagem direta e a gente começa a criar uma ideia de representação por contexto e criatividade mais do que uma base rígida de estratégia e de coerência. Então a gente está indo para uma visão um pouco mais de linguagem, contexto e criatividade que é o que a gente ser humano faz no dia a dia, beleza?

07:33

Tá bom. Quais são as principais limitações desse primeiro momento que a gente tá falando? A primeira coisa é que a gente tem muita dificuldade de capturar dependências de longo prazo. O que eu tô querendo dizer com isso? Imagina que quando eu comecei a minha frase lá no começo, então olha, a gente começou a conversar, eu tava falando de quê? Eu tava falando que eu ia ter uma conversa com vocês mais técnicas, ia começar a aprofundar, tal, tal, tal.

07:57

Olha como isso conecta com o que eu tô falando agora. Quase nada, certo? Eu falei lá atrás sobre isso e agora eu tô falando sobre estatística e modelo de linguagem. Essa conexão de longo prazo com o que eu tô falando é muito complicada de fazer pra uma máquina.

08:13

Para a gente, para os seres humanos é um pouco mais simples, mas até a gente se perde. Então vamos lá, eu comecei uma conversa, se você parar e assistir o nosso vídeo inteiro, ela tem conexão com o que eu estou falando agora, mas é uma conexão tão leve que não consegue ser direcionada com uma regra simples.

08:28

de probabilidade estatística. Se eu tivesse te perguntado lá no comecinho qual era a probabilidade de eu estar falando agora com vocês sobre, por exemplo, dependência de longo prazo, dificilmente vocês iam conseguir prever isso. Uma máquina também. Então pense o seguinte, essa baixa capacidade de capturar essa dependência de longo prazo estava no nosso cerne do problema. Era muito difícil de fazer isso. A gente conseguia fazer coisas muito mais simplificadas. Perdão, gente.

08:59

Por que eu estou falando isso? Porque a gente era baseado em um conceito que chama Bigrama. Vocês vão ver ele normalmente, se vocês forem ler livros, etc. Ele normalmente vai estar com o número 2 traço grama. É um Bigrama. O que isso significa? Significa que eu tento entender, compreender ou até...

09:18

Prever a próxima palavra que vai aparecer, de uma forma muito simples. E a gente já vai falar um pouco disso. Então você tende, quando você está trabalhando com esse modelo de bigrama, a ter frases fragmentadas, repetitivas ou incoerentes. Então você começa a ter algumas frases que não vão fazer tanto sentido ao longo do texto.

09:38

Você gera texto, mas você gera um texto meio fragmentado. Eu tô falando de texto aqui porque eu acho que é mais fácil da gente entender. Se a gente for pra imagem, fica muito complicado. Depois a gente fala de imagem, de som e etc. Então, vamos lá. Tem essa complexidade. Então, quando a gente tá falando dessa complexidade, você não tem uma real compreensão da máquina, da semântica que tá vindo. Ela tá só olhando padrão estatístico. Então, olha que diferença.

10:05

A gente não tá tratando a linguagem humana, a gente tá tratando o padrão estatístico, ainda é uma visão de matemática, ainda é uma visão muito de exatas. Então, o que a gente precisa entender é que a linguagem, ela não é tão zero ou um com base em, ah, falei isso, talvez a próxima seja aquilo, depois talvez a próxima seja aquilo. Você tem uma conexão semântica, você tem uma construção de raciocínio, você tem outras tantas coisas além do padrão estatístico.

10:30

Vamos dar um exemplo pra você. Imagina que você está treinando uma máquina com bigrama. Você vai falar o seguinte, toda vez que vier um bom

10:46

possivelmente depois vem dia, certo? Possivelmente. Podia ser bom-bom, um chocolate, mas normalmente vem dia, bom dia. Então ela vai entender que a maior parte das vezes a probabilidade que quando ela falar sobre bom depois vem dia. Isso é um exemplo bem tonto, mas isso é o que normalmente acontece quando a gente está treinando. Então para um modelo de bigrama, ela entende que é bom dia.

11:09

A próxima palavra ela já não tentou conectar, porque ela está conectando bom com dia. Possivelmente, a próxima interação dela vai tentar conectar dia com a próxima coisa. Então, ela vai tentando ir para esses modelos probabilísticos para chegar na próxima palavra. Está vendo que é simples, né? É simples. Mas se você parar para pensar, já fugiu muito daquela ideia de árvore de tomada de decisão de sim ou não. Aqui eu estou olhando probabilidade. Se eu fosse por sim ou não, eu não ia chegar nem no dia.

11:36

porque eu podia ser bom, bom, bom dia, bom, sei lá, bom ar, bom, vários bons, podia conectar vários bons aqui no meio do caminho. E eu não sou a melhor pessoa para fazer isso, a Yafa é melhor do que eu. Aqui a gente tem então essa quebra de paradigma, mas a gente ainda é bem fragilizado nessa estratégia. Vou dar um exemplo para vocês mais claro sobre essa estratégia de bigrama.

12:02

nossa tô com a garganta ruim perdão gente é imagina que é o seguinte imagina que você tem uma frase que assim o gato preto dorme no sofá para uma estratégia de bigama ela ela vai possivelmente entender que gato preto quando estiver treinando ela é um bigama forte ou seja normalmente isso acontece junto e daí a tendência que ela tem é de sempre trazer

12:27

o gato junto com o preto. Então, você vai trazer sempre gato preto. Então, imagina que nesta construção de frase, a tendência que vai acontecer é que ela coloque, por exemplo, o gato preto dorme no sofá, gato preto. Ou gato preto dorme no sofá, gato preto dorme no sofá.

12:43

Ela vai tentar trazer de novo, e daí ela vai começar a ter uma certa alucinação ou frases desconexas e incoerentes. Ou seja, se o modelo aprendeu que gato preto ocorre com frequência, ele vai ficar gerando gato preto toda hora. Sempre que ele ver gato, ele vai colocar preto. Então, isso é muito importante de entender. Lógico que eu fiz aqui uma frase muito simples, mas é muito importante de entender. Eu vou aprofundar nessa frase simples, tá? Pra conseguir contar pra vocês o que tá acontecendo por trás. Então pensa o seguinte...

13:13

Quando a gente tá falando, o gato preto dorme no sofá, ela tem um foco limitado no contexto, ela não consegue olhar o todo, então ela tá olhando só primeira palavra, segunda palavra, primeira palavra, segunda palavra, primeira palavra, segunda palavra, sempre esse bigrama, certo? Então, duas palavras por vez, o modelo só consegue ver isso, ele não consegue ver quinze, ele não consegue ver o gato preto dorme no sofá.

13:37

olha o tanto de coisa que tem aqui tem cinco palavras né gato preto dorme no sofá são cinco palavras ela tá olhando a primeira gato preto depois ela não sabe que vai vir de preto pra dormir tá longe possivelmente vai vir o que gato porque gato é preto você entendeu a conexão dela possivelmente vai trazer ela pra isso tô simplificando demais gente mas é mais ou menos isso tá bom então ela vai enxergar mais ou menos ali duas palavras por vez e ela não tem noção do que foi dito antes porque eu tô falando ó uma

14:07

projeção linear pra frente. Ela não sabe o que vem depois, mas ela também não sabe o que veio antes. Ela consegue focar só nas duas palavras. Então, gato preto dorme. Ela não viu dorme. Quando ela fez gato preto, ela vai pro preto e dorme. Ela só viu preto e dorme. Ela não vê mais o gato. Então, essa construção semântica, chance zero de dar certo, né? Vamos ser bem honestos. Mas a gente já começa a voltar. O que que acontece quando a gente faz isso e a gente treina realmente a máquina? A gente começa a ver que ela tá

14:37

repetindo muitos blocos, isso acontece demais, ela começa a não manter uma coerência global do que a gente está discutindo. Então, aqui, a gente está falando de uma probabilidade muito local e isolada, ela vai gerar ali palavra com base na frequência de combinação, como eu falei para vocês. Então, você vai ver a frequência de combinação que está rolando, mas você não vai conseguir fazer a evolução disso. Então, possivelmente, você vai entrar num looping repetitivo,

15:07

e você não vai conseguir construir uma memória. Você vai ter essa ausência de memória e ausência de projeção. Beleza? Então você não consegue ter uma memória além do... a gente chama de enigrama atual. Então pensa que o seu enigrama é esse pedacinho que a gente tá construindo. Você não consegue olhar pra trás e você não consegue olhar pra frente. Então, por isso você vai gerando essa ideia de conversa meio desconecta.

15:37

Beleza? Esse era o grande problema que a gente tinha. Dado esse problema, a gente evolui para o próximo conceito.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **LLM** — Large Language Model (Modelo de Linguagem de Grande Porte)
- **2-grama / bigrama** — Sequência de duas palavras consecutivas usada para modelar a próxima palavra com base na imediatamente anterior

**Resumo**
A aula explica, de forma simplificada e progressiva, como os modelos de geração de linguagem evoluíram até os LLMs. O instrutor começa reforçando que a proposta é abstrair inicialmente o funcionamento técnico para depois aumentar a complexidade ao longo das próximas aulas. Em seguida, contextualiza a mudança histórica da computação baseada em decisões binárias, sim ou não, para abordagens estatísticas e probabilísticas, que se aproximam mais da forma como humanos inferem e tomam decisões no dia a dia.

Dentro desse percurso, é apresentado o conceito de bigrama, também chamado de 2-grama, como um modelo que tenta prever a próxima palavra usando apenas a palavra imediatamente anterior. O exemplo de “bom dia” é usado para mostrar como o modelo aprende combinações frequentes e reproduz a continuação mais provável com base na estatística observada no treinamento. O instrutor destaca que isso representa uma geração de linguagem muito local, útil por ser simples e barata computacionalmente, mas limitada por não capturar semântica, intenção, criatividade ou contexto mais amplo.

A aula aprofunda então o principal problema desses modelos: a dificuldade de lidar com dependências de longo prazo, isto é, conexões entre partes distantes do texto que precisam permanecer relacionadas para que haja coerência. Com o exemplo de “o gato preto dorme no sofá”, é mostrado que um bigrama tende a repetir combinações fortes como “gato preto”, o que pode gerar loops, frases fragmentadas e repetição excessiva. O texto produzido pode parecer plausível em pequenas partes, mas falha na coerência global.

Por fim, o instrutor conclui que o avanço para arquiteturas mais modernas aconteceu porque os modelos estatísticos locais não conseguiam sustentar fluidez, memória e contexto amplo. A transição para modelos mais avançados foi motivada pela necessidade de conectar partes distantes da sequência e representar linguagem de forma mais contextual, preparando o terreno para o estudo dos LLMs.

**Pontos de atenção**
- Modelos de bigrama consideram apenas a palavra imediatamente anterior; não há visão ampla do contexto.
- A geração é guiada por frequência estatística, não por compreensão semântica real.
- Combinações frequentes podem ser reproduzidas de forma excessiva, causando repetição e “looping”.
- É comum produzir frases localmente plausíveis, mas globalmente incoerentes.
- Dependências de longo prazo são um ponto crítico: o modelo não preserva bem relações entre partes distantes do texto.
- A ausência de memória efetiva limita a continuidade de tópicos, objetivos e raciocínio.
- A coerência local não garante coerência global; pequenos trechos corretos não significam texto consistente.
- O exemplo com “bom dia” e “gato preto” ilustra probabilidades locais, mas não deve ser interpretado como entendimento real da linguagem.
- A simplificação da aula é proposital; conceitos mais avançados serão aprofundados nas próximas etapas.