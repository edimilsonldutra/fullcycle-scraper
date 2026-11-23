Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16373)

## Resumo da aula

Redes neurais profundas marcaram uma virada importante porque permitiram escalar a modelagem de problemas que modelos anteriores, como bigramas e cadeias de Markov, tratavam de forma mais restrita. Esse avanço dependeu de dois fatores que se reforçaram mutuamente: crescimento massivo da disponibilidade de dados e aumento do poder computacional, com destaque para GPUs. Quando esses fatores se alinham, treinar modelos maiores deixa de ser inviável e a IA volta a ganhar relevância prática e científica.

O termo profundo se refere à quantidade de camadas entre a entrada e a saída. Em vez de uma transformação simples e facilmente rastreável, a informação atravessa várias etapas de combinação e transformação até produzir um resultado. Isso aumenta a capacidade de representar padrões complexos, mas também torna o processo interno menos transparente do que em modelos mais lineares.

Palavras não entram diretamente em uma rede neural como unidades simbólicas compreensíveis pelo modelo. Para que a rede opere sobre linguagem, cada palavra precisa ser convertida em uma representação numérica adequada ao cálculo. Essa conversão deixa de tratar a palavra como bits isolados e passa a representá-la em um espaço vetorial contínuo.

Word embeddings são vetores de alta dimensão usados para representar palavras de modo que similaridades semânticas apareçam como proximidade nesse espaço vetorial. Se duas palavras têm usos ou significados parecidos, seus vetores tendem a ocupar regiões próximas. Essa estrutura permite que a rede opere sobre relações entre palavras, em vez de apenas sobre símbolos discretos sem noção de semelhança.

Uma palavra como array pode ser representada por um vetor como [0.25, -0.14, 0.88, ...]. O valor exato de cada dimensão isoladamente não é o ponto principal; o que importa é a posição relativa desse vetor em relação aos vetores de outras palavras. A partir dessa geometria, o modelo consegue explorar proximidade entre termos para apoiar previsões e composições de sequência.

Em redes feedforward, o fluxo de dados é unidirecional: a entrada passa pelas camadas e segue apenas para frente até a saída. No caso de linguagem, a sequência de palavras é convertida em embeddings e propagada pela rede para produzir uma previsão, como a próxima palavra provável. Essa arquitetura já supera abordagens muito simples, mas ainda não modela adequadamente dependências sequenciais mais ricas.

Embeddings capturam proximidade entre palavras, mas isso não garante que a arquitetura preserve a ordem com precisão suficiente. Frases como “o cachorro mordeu o homem” e “o homem mordeu o cachorro” podem compartilhar palavras muito próximas no espaço vetorial, embora expressem eventos diferentes. Quando a arquitetura não trata a ordem como parte central da representação, ela corre o risco de aproximar demais sequências semanticamente distintas.

Uma forma de reduzir esse problema é usar uma janela fixa de palavras anteriores para prever a próxima. Retomando a ideia de contexto local, uma sequência como “o cachorro está no” restringe bastante a próxima palavra provável, e a rede pode prever algo como “jardim” combinando os vetores dessas quatro palavras. Isso amplia o contexto em relação a abordagens baseadas em poucas palavras, mas continua limitado a um alcance curto e pré-definido.

O principal limite do feedforward é que ele enxerga apenas um número fixo de palavras anteriores e não mantém memória real do que foi processado antes dessa janela. Dependências que atravessam frases ou parágrafos se perdem, o que prejudica tarefas que exigem coerência contínua, como tradução, diálogo e resumo. Retomando a limitação de longo prazo já observada em modelos anteriores, o problema persiste aqui, embora em uma forma mais sofisticada.

Redes neurais profundas já representam um salto importante porque introduzem camadas profundas, embeddings e processamento vetorial mais expressivo para linguagem. Ainda assim, feedforward com janela fixa não resolve bem ordem, memória e dependências longas. Essas limitações explicam por que arquiteturas posteriores se tornam necessárias para chegar aos modelos de linguagem modernos.

## Transcrição

00:01

Bora pessoal, então dá o próximo passo aqui na nossa jornada. Eu queria falar um pouco com vocês agora de um assunto que eu acho extremamente relevante e é quando a coisa começa a pegar um corpo mais parecido com o que a gente vê hoje, tá? O que eu queria falar com vocês? Deixa só eu arrumar o fio aqui, pronto. O que eu queria falar com vocês? O seguinte, a gente tem um momento onde a gente começa a falar de redes neurais profundas, vocês já devem ter ouvido falar disso, tá?

00:28

E aqui é quando a gente começa a ter uma virada de chave um pouco mais importante dos modelos de IA que a gente tinha até então. A gente começa a dar um salto no que realmente vai fazer a IA ser o que ela é hoje. No final das contas aqui, a IA começa a ter de novo uma relevância importante nos seus estudos e nos seus avanços. Então a rede neural profunda,

00:50

foi o que deu um start pra gente ter hoje as coisas que a gente usa, beleza? Então, muito importante esse capítulo, aqui eu vou falar de como surge essa conversa e como isso fala pros nossos modelos de hoje em dia. Então, quando a gente chega ali nas décadas de 80 até 90, a gente começa a pensar na inteligência artificial

01:11

com aquela evolução um pouco mais lenta, uma evolução que não consegue dar o seu boom por alguns modelos. A primeira coisa é que a gente usava os modelos ali como os bigramas, como a gente acabou de falar, e os modelos de Markov muito para algumas aplicações muito específicas. Mas quando a gente começa a pensar em aplicações maiores, começa a pensar em uma relevância maior para IA,

01:37

a gente começa a ter uma dificuldade em escalar tanto esses modelos quanto criação de novos modelos. E daí, quando a gente começa a ter alguns fatores se alinhando, ali como, por exemplo, o crescimento exponencial da disponibilidade de dados, que vem muito com internet, redes sociais, sensores e sistemas digitais começaram a ser usados muito mais fortemente, a gente começa a ter muito mais dados. Então, pensa que antes

02:06

Quando a gente olha ali antes de 1990, a gente não tinha isso de forma relevante. Depois disso começa a aparecer uma internet mais latente, e essa internet dá a capacidade da gente conseguir ter mais dados de forma mais massiva. Então a gente começa a ter todos esses dados rolando por aí. E dado, no final das contas, é a matéria-prima para uma IA funcionar. Isso é importante da gente pensar, beleza? Então a gente tem esse crescimento exponencial dessa disponibilidade de dados.

02:36

Outra coisa super relevante que acontece é que a gente começa a ter um aumento do poder computacional, como eu falei pra vocês também ao longo das nossas aulas. Começa até as GPUs chegando muito forte. E a GPU mostrou que tinha um poder muito grande pra processamento de quando a gente falava de algoritmos de IA. E daí isso ajudou muito a gente conseguir evoluir os algoritmos de redes neurais profundas. Então foi super importante também.

03:02

Então com esses avanços a gente começa a ter de novo redes neurais aparecendo, a gente começa a ter a inteligência artificial voltando ao hype e a gente começa a ter muito mais pesquisa em cima disso. Então o mercado começa a olhar pra isso com um pouco mais de interesse e aí a coisa começa a deslanchar.

03:19

Então a gente começa a focar mais na modelagem dessa linguagem e na criação das redes neurais profundas com um pouco mais de gás, pensa assim. Beleza? Então demos esse passo. Dando esse passo a gente começa então a ter as redes neurais profundas que tem basicamente o seu funcionamento vai ser da seguinte forma.

03:44

A gente não tem mais camadas tão simplificadas como a gente tinha antes, apesar de eu ter explicado Markov, e eu acho que Markov já é um pouco mais chatinho. As redes neurais profundas, elas são um pouco além disso. Elas vão simular o nosso comportamento de redes neurais biológicas. Elas começam a simular, eu posso dizer assim. Então a gente começa a ter

04:04

uma entrada de informação que vai passar por uma cadeia gigantesca, cadeias profundas para conseguir ser transformada e combinada e até reinterpretada até gerar uma saída que faça sentido. Então, quando a gente fala do termo profundo,

04:20

significa o número de camadas que você vai passar antes de ter uma saída. Antes você tinha uma entrada e uma saída, estavam mais claras quais eram os passos que ela passou, por onde ela passou até chegar a uma saída. Quando a gente está falando das redes neurais profundas, você começa a se perder nisso, são tantos passos

04:40

É tanta complexidade e tantos locais por onde essa tomada de decisão passou que parece muito mais com a tomada de decisão do ser humano que passa querendo ou não por várias ligações de neurônios e assim por diante. As nossas sinapses ficam muito mais complexas. Então aqui a gente começa a falar desse surgimento e daí essas transformações conseguiram evoluir a matéria, tá bom?

05:03

Beleza, e como que isso funcionou quando a gente tá falando de linguagem natural? E agora eu vou começar a explicar pra vocês como é o funcionamento de uma rede neural profunda quando a gente fala de linguagem natural, que é onde a gente chega e desencadeia na utilização grande de Gen AI no futuro, tá? Então lá no futuro eu vou dar mais acho que uns dois passos até a gente chegar na Gen AI  que a gente tem hoje, a gente vai passar por mais duas formas de fazer aqui, mas a gente já começa a ver isso presente aqui um pouquinho, tá bom?

05:32

Então, quando a gente fala de linguagem, ela não vai ser um dado que pode ser diretamente processado por uma rede neural. Você não consegue colocar uma palavra e ela vai ser processada. Você não vai pegar essa palavra e transformar, por exemplo, em bits e bytes como a gente fazia anteriormente, zeros ou uns. Você não vai fazer isso. Então, para uma rede neural, você não consegue processar a palavra diretamente, assim como para o computador também você não conseguia, você transformava em zero ou um. Aqui você começa a usar um termo que chama...

06:01

Embeddings, tá bom? Esses Embeddings, eles são uma forma de você organizar informação para uma rede neural conseguir trabalhar. Então, quando a gente está falando disso, desses Word Embeddings, a gente está falando de uma representação

06:18

vetorial, pensa assim, é uma representação vetorial e não mais uma representação numérica direta, sobre uma palavra. Então, eu consigo mapear uma palavra, gerar um vetor em um espaço contínuo e de alta dimensão. E daí, com isso, eu consigo traduzir para o computador o que é aquela palavra. Então, eu paro de trabalhar com 0 e 1 e começo a trabalhar com vetor. Então, eu vou dar um exemplo para vocês, para ficar mais claro aqui.

06:45

que essa parte é chatinha. Imagina que eu tenho a palavra array, tá bom? E essa palavra array, ao invés de eu representar ela com R sendo alguma coisa, ou E outra coisa, ou I outra coisa, em bits e bytes, como eu falei anteriormente, eu vou representar ela como um vetor. Então, por exemplo, eu vou colocar um vetor que é 0.25, menos 0,14, 0,88.

07:10

e assim por diante. Então, eu vou gerenciar essa palavra, transformando ela num vetor. Gerei lá um linguição no meu vetor, beleza? Guardei esse treco. O objetivo é que quando eu gere vetores com palavras com significados semelhantes, eu vou ter um valor próximo disso. E daí, esse valor próximo vai me ajudar a pensar num encadeamento de palavras, entendeu? Então, eu vou vetorizando cada palavra e com essa vetorização das palavras, eu consigo

07:37

construir uma forma de conversa neural dentro disso. Então, a gente tem algumas técnicas que começaram a surgir, principalmente a GloVe, a gente teve a BERT também muito forte e o GPT mesmo vindo muito forte aqui para a criação dessas propostas de como a gente transforma uma palavra em um vetor para ser utilizado por uma rede neural.

08:03

Então, isso é super importante. Depois a gente vai aprofundar mais pra vocês entenderem como isso funciona. Mas, pra agora, já começa a entender isso. Você transforma a palavra num vetor, essa palavra vai buscar suas palavras similares e próximas disso, e com base nisso, ela evolui pro próximo item, pra próxima construção de frase. Aqui a gente tem uma ideia também, muito forte, de redes neurais

08:29

Feedforward. Então, o que a gente está querendo dizer? É uma estrutura neural ainda mais simples, que tem ainda aquela ideia de, igual à cadeia de Markov, de fluxo de dados unidirecional. Você não tem dados que vão e voltam. Então, você recebe uma entrada,

08:45

transforma essa entrada, essa sequência de palavras em embeddings, e depois você propaga isso pra frente, camada por camada, até chegar numa saída. E daí você produz alguma saída, por exemplo, uma previsão da próxima palavra que viria nesse encadeamento de vetores, tá bom?

09:04

essa estrutura vai ser muito poderosa, mas ela ainda tem um grande problema. Você já começa a pensar nesse problema aí, certo? Ela não considera, por exemplo, a ordem ou a dependência temporal das palavras. O que isso significa? Eu vou dar um exemplo já para vocês, mas para conseguir lidar com essa sequência, a gente pensa em algumas outras estratégias

09:27

que são as janelas de contexto fixas. Mas antes de eu falar das janelas de contexto fixas, vamos pensar no seguinte. Imagina que eu tenho uma estrutura que não tem conexão. O que vai acontecer ao longo do tempo?

09:44

eu posso ter uma combinação de palavras que não respeita a sequência que a gente tem na nossa fala normalmente. Ela vai ver proximidade, certo? Então, essa proximidade, ela vai mostrar as palavras que poderiam vir, mas ela não mostra a ordem de palavra. Eu vou dar um exemplo aqui, acho que é um bom exemplo. Imagine o seguinte, se eu for nessa visão de encadeamento, eu posso gerar uma frase que é, por exemplo, o cachorro mordeu o homem.

10:14

beleza? então o cachorro mordeu o homem vai ser a minha frase para uma categorização vetorial aqui quando a gente está falando dos embeddings isso poderia virar o que? o homem mordeu o cachorro não teria uma mudança relevante na estrutura então para ir aqui nesse sentido para as redes neurais a gente não tem uma mudança

10:37

fixa, uma mudança clara de uma frase para outra, pode ser um homem mordendo um cachorro, ou um cachorro mordendo um homem, porque a correlação de palavras vai ser muito próxima, você vai conseguir transformar isso num vetor e no final das contas você vai chegar no mesmo resultado, num resultado muito aproximado, essa saída pode ser um ou outro, e na verdade muda totalmente o contexto, certo? então para essas redes neurais isso vira um problema, e daí com este problema vem a ideia de janelas de contexto fixo

11:04

Então, por exemplo, imagina que você cria uma janela com quatro palavras, tá bom? Então, eu vou colocar uma palavra que é a seguinte... O cachorro está no... É, o cachorro está no... Já tem quatro palavras. Então, ó... O cachorro está no... Qual a próxima palavra?

11:20

dificilmente eu vou falar no casa, não vai funcionar, então ele vai tentar prever aqui qual é a próxima palavra, imagina que aqui ele vai colocar então, o cachorro está no jardim, porque a sua janela são quatro palavras, olha que engraçado, como isso se é uma evolução

11:37

do que a gente falou lá atrás da construção de duas palavras, lembra? Então, a gente estava com aquela construção de duas palavras, aqui eu consigo colocar uma janela de palavras para conseguir garantir a coerência. E daí, eu coloquei quatro palavras aqui no nosso caso. E daí, eu consigo ir lá e prever. O cachorro está no jardim, beleza. Essa rede vai combinar os vetores das quatro palavras para conseguir chegar na quinta palavra. E com base nisso, ela consegue prever e criar uma certa conversação.

12:07

Beleza? Então, aqui você já começa a ver a coisa funcionando, mas você tem algumas limitações ainda no Feedforward. O contexto primeiro vai ser limitado. Então, a gente consegue olhar um número fixo de palavras, igual fiz aqui com 4, então você consegue olhar um número fixo de 4, 5, 3 palavras, que são as palavras anteriores pra você prever a próxima palavra. Você ainda não tem aquela correlação complexa entre ida e volta, é só pra frente, tá bom?

12:36

isso vai impedir o nosso modelo então de entender quando a gente está falando de contextos mais longos a gente continua com essa mesma problemática que a gente já tinha anteriormente então por exemplo a dependência que atravessa um parágrafo inteiro diferente daqui ó o cachorro está no jardim agora se eu tivesse um texto que está passando por um parágrafo inteiro onde eu falo cachorro está no jardim porque estamos limpando a casa e a casa é

13:04

não pode ter um cachorro dentro dela. Tá vendo que eu já tenho uma correlação aqui maior num espaço maior que eu não vou conseguir conectar porque eu tenho um contexto limitado de palavras que estão só vindo pra trás. Eu vou perder esse próximo cachorro quando eu for falar da casa novamente e da limpeza que eu tô fazendo lá dentro. Eu tentei dar um exemplo aqui um pouco maior, mas mais ou menos é por esse caminho que a gente passa, entendeu? Essa é a problemática que você traz. Então isso continua acontecendo, tá bom?

13:34

Outra limitação que a gente tem deste modelo ainda, a ordem da sequência, como eu falei para vocês, ela ainda é muito difícil, por mais que você tenha a ideia das janelas, você não consegue fechar a ordem tão facilmente, a ordem continua dando problema. Então, o que eu falei para vocês, o cachorro mordeu o homem, por mais que eu feche com uma janela, eu posso inferir em colocar o homem mordeu o cachorro dentro dessa sequência.

14:02

porque é muito difícil a correlação pra frente. Quando você pega os embendings e soma ele, ou concatena, ele vai chegar no mesmo resultado em ambos os casos, tá bom?

14:16

É outro problema muito relevante, a falta de memória. Esse carinha não conhece contexto, conceito e a conversa que a gente tem hoje, por exemplo, com o chat GPT da vida. Ele só sabe o que você está falando com ele ali naquele momento. Então, ele não consegue ver o que ele processou anteriormente para pensar no próximo. Lembra do encadeamento que a gente acabou de falar? De 5, 4, etc. Esse encadeamento, ele acaba trazendo o mesmo problema que a gente tinha dos bigramas, como eu falei para vocês. Então, você não consegue pensar

14:46

em uma estratégia onde você precisa de coerência ao longo de uma conversa ou de uma tradução, por exemplo, imagine eu vou traduzir um texto, pra você conseguir fazer essa coerência fica difícil, um diálogo, um resumo, fica muito difícil de você usar isso no dia a dia, beleza gente? Bom, basicamente é isso quando a gente tá falando de redes neurais profundas e já já volto pra falar com vocês de um outro conceito muito importante pra daí sim depois a gente começar a entrar

15:12

nos conceitos dos Transformers, que é onde eu tô doido pra chegar com vocês, pra gente conseguir dar um passo maior nessa nossa conversa. Fechou?

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **GPU** — Unidade de Processamento Gráfico (*Graphics Processing Unit*)  
- **Gen AI** — Inteligência Artificial Generativa  
- **BERT** — *Bidirectional Encoder Representations from Transformers*  
- **GPT** — *Generative Pre-trained Transformer*  

**Resumo**  
A aula apresentou a virada de chave trazida pelas redes neurais profundas na evolução da inteligência artificial, destacando que esse avanço se tornou viável pela combinação entre o crescimento massivo da disponibilidade de dados e o aumento do poder computacional, especialmente com o uso de GPUs. O instrutor explicou que, nas décadas anteriores, modelos como bigramas e cadeias de Markov eram úteis, mas limitados para aplicações mais amplas, e que o surgimento de redes mais profundas recolocou a IA em evidência científica e prática. Em seguida, foi definido o conceito de “profundo” como a presença de várias camadas entre entrada e saída, o que aumenta a capacidade de representação, mas também torna o processamento interno menos transparente.

Na parte de linguagem natural, foi explicado que palavras não podem ser processadas diretamente por uma rede neural e precisam ser convertidas em representações numéricas adequadas. Para isso, entram os embeddings, especialmente os word embeddings, que representam palavras como vetores em um espaço contínuo e de alta dimensão, permitindo que termos semanticamente próximos fiquem próximos nesse espaço. O instrutor exemplificou a ideia com uma palavra transformada em vetor e destacou que o valor isolado de cada dimensão importa menos do que a relação geométrica entre os vetores. Também citou técnicas e modelos associados a essa abordagem, como GloVe, BERT e GPT, para mostrar a evolução da representação vetorial da linguagem.

Por fim, foi abordada a arquitetura feedforward, caracterizada por fluxo de dados unidirecional: a sequência de palavras é convertida em embeddings e propagada camada por camada até gerar uma saída, como a previsão da próxima palavra. Apesar de ser mais poderosa do que soluções anteriores, essa abordagem ainda apresenta limitações importantes, como dificuldade para preservar ordem, dependências temporais longas e memória de contexto. Para contornar parcialmente isso, foi apresentada a ideia de janelas de contexto fixas, nas quais um número limitado de palavras anteriores é usado para prever a próxima, mas sem resolver de forma satisfatória relações mais amplas entre frases, parágrafos e conversas inteiras. A aula encerra conectando essas limitações à necessidade de arquiteturas posteriores, preparando o terreno para o estudo de Transformers.

**Pontos de atenção**  
- O termo “profundo” se refere à quantidade de camadas; mais camadas aumentam a capacidade do modelo, mas reduzem a interpretabilidade.  
- O avanço das redes neurais profundas dependeu fortemente de dois fatores: mais dados e mais poder computacional.  
- Palavras não são processadas diretamente pela rede; precisam ser convertidas em embeddings.  
- Embeddings capturam similaridade semântica por proximidade vetorial, não pelo significado isolado de cada dimensão.  
- Palavras semanticamente parecidas podem gerar representações próximas mesmo em contextos diferentes.  
- Modelos feedforward têm fluxo unidirecional e não possuem memória real do que foi processado antes.  
- A ordem das palavras continua sendo um problema: frases com as mesmas palavras podem ter sentidos opostos.  
- Janelas de contexto fixas ajudam, mas limitam o alcance do modelo a poucas palavras anteriores.  
- Dependências longas entre frases, parágrafos e partes distantes do texto se perdem facilmente.  
- Esse tipo de arquitetura ainda é fraco para tarefas que exigem coerência contínua, como tradução, diálogo e resumo.  
- A limitação de contexto e memória explica por que arquiteturas posteriores se tornaram necessárias.