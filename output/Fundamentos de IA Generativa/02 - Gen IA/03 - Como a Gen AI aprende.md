Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16368)

## Resumo da aula

A IA tradicional, já definida anteriormente, aprende um mapeamento entre entrada e saída esperada. A IA generativa muda o foco: em vez de procurar apenas a resposta correta para um input, ela aprende distribuições de probabilidade sobre padrões, sequências e combinações possíveis. Esse aprendizado permite construir um mapa probabilístico do que tende a fazer sentido em determinado contexto. O resultado não é uma escolha entre rótulos conhecidos, mas a navegação por caminhos plausíveis para produzir uma saída nova e coerente.

O treinamento em grandes volumes de dados serve para capturar estruturas implícitas que organizam a informação, mesmo quando elas não estão rotuladas explicitamente. O modelo aprende regularidades de linguagem, estilo, associação e continuidade, o que aumenta sua capacidade de distinguir sequências prováveis de sequências estranhas ao contexto. Essa é a base da geração coerente: a saída parece fazer sentido porque respeita padrões recorrentes aprendidos durante o treinamento. Quanto melhor o treinamento, maior a chance de o modelo produzir algo consistente e menor a chance de desviar para uma alucinação.

A analogia do artista reduz a abstração do processo. Um artista observa muitas obras, internaliza estilos, composições e relações, e depois produz algo novo sem copiar literalmente uma peça específica. O modelo generativo opera de forma parecida: ele usa repertório estatístico aprendido para compor uma saída original condicionada ao contexto recebido. A originalidade surge da recombinação coerente de padrões, não de criação a partir do nada.

O cartógrafo não apenas registra montanhas, rios e florestas já vistos; ele aprende a lógica do terreno e passa a inferir onde novos elementos poderiam existir. Essa imagem ajuda a entender o mapa probabilístico: o modelo não memoriza apenas exemplos, ele aprende a estrutura do espaço de possibilidades. Quando recebe um pedido para gerar algo parecido com o que conhece, ele projeta uma nova configuração compatível com as regularidades observadas. Por isso consegue criar uma “cidade ilusória” coerente com cidades anteriores, mesmo que aquela cidade específica nunca tenha existido.

Modelos autoregressivos geram conteúdo token a token, escolhendo cada próximo elemento com base nos anteriores. Em texto, isso significa que cada palavra produzida altera o contexto disponível para a próxima decisão, formando uma cadeia de dependências locais. Retomando o cenário de geração de um livro parecido com Harry Potter, o modelo usa o repertório aprendido de estilo e estrutura, mas a construção concreta acontece passo a passo durante a geração. A coerência emerge porque cada nova escolha precisa ser compatível com o que já foi escrito.

A analogia do escritor mostra por que a autoregressão funciona bem para linguagem. Um escritor não materializa o texto inteiro de uma vez; ele escreve uma frase, usa essa frase para orientar a seguinte e ajusta o rumo conforme a narrativa avança. O modelo faz o mesmo em escala estatística: ele se autocompleta continuamente até concluir a sequência. Esse mecanismo explica tanto a fluidez da geração quanto a possibilidade de desvio quando a cadeia começa a seguir um caminho plausível, mas incorreto.

Atenção e contexto já foram introduzidos antes; aqui o ponto novo é o mecanismo de self-attention como forma de preservar relações relevantes ao longo da sequência. Self-attention permite ponderar quais partes anteriores do texto importam mais para interpretar ou gerar o próximo token. Em um texto longo, isso ajuda o modelo a manter vínculos entre elementos distantes, como um personagem apresentado no início e retomado muitos parágrafos depois. Sem esse mecanismo, a geração perderia continuidade com muito mais facilidade.

Em termos práticos, self-attention funciona como um sistema de foco seletivo sobre o histórico disponível. O modelo não trata todos os tokens anteriores como igualmente importantes; ele atribui pesos maiores às relações mais úteis para a decisão atual. Retomando o exemplo do livro, isso permite sustentar a identidade do personagem principal e a lógica da narrativa mesmo quando há muitos eventos intermediários. Essa capacidade é decisiva para geração de textos longos com consistência temática.

Antes de operar sobre palavras, imagens ou código, o modelo converte esses elementos em vetores numéricos chamados embeddings. Essa representação vetorial transforma itens simbólicos em pontos de um espaço matemático onde relações podem ser medidas computacionalmente. O modelo não “lê português” ou “lê inglês” como um humano; ele processa padrões numéricos que codificam propriedades semânticas e contextuais. Isso torna possível comparar significado por proximidade geométrica entre vetores.

Quando dois termos aparecem em contextos parecidos, seus vetores tendem a ficar próximos no espaço semântico; quando aparecem em contextos muito diferentes, tendem a ficar distantes. Por isso, pares como “rei” e “rainha” ocupam regiões próximas, enquanto “rei” e “cachorro” normalmente ficam mais afastados. A analogia com coordenadas geográficas ajuda: proximidade vetorial funciona como proximidade de localização, mas em um espaço de significado. Essa estrutura é uma das bases para o modelo reconhecer relações, manter contexto e escolher continuações mais plausíveis.

## Transcrição

00:00

Pessoal, então deixa eu passar pra vocês um panorama super importante. Como que a IA generativa aprende no final do dia? Isso é muito importante pra gente ter na nossa cabeça. A IA generativa, ela aprende de um jeito diferente. Então, vamos recapitular.

00:16

Imagina o seguinte, a IA normal antes da generativa, como que ela fazia? Ela entendia os dados de entrada categorizados e catalogados, com base nesses dados ela sabia o que se esperava de saída e tentava prever a sua saída. Então uma IA normal normalmente funcionava desse jeito, beleza? Então até aqui a gente consegue compreender que a gente tem os dados de entrada, um algoritmo

00:44

de inteligência por aqui que vai tentar prever os dados de saída com base óbvio em cálculo em modelos matemáticos beleza com a generativa não é assim que a manda toca ela não segue esse caminho convencional ela começa a pensar um pouco diferente então imagina que a convencional então ela mapeia diretamente

01:06

a entrada para tentar chegar numa resolução de saída. Em vez disso, a IA generativa vê probabilidades com base nos dados que ela está recebendo de entrada para compreender o contexto de entrada e montar um novo contexto de saída. Então, é mais ou menos como um artista que está ali estudando vários e milhares de obras, com base nesses estilos, nesses conhecimentos que ele buscou,

01:35

Ele ir atrás de algo novo. Criar com base em inspiração, mais do que com base em probabilidade de repetição. Lógico que para inspirar, você tem que em determinado momento ver uma base de probabilidade de repetição. E eu já vou explicar um pouco disso pra vocês. Mas vamos entrar um pouquinho mais a fundo pra vocês entenderem do que eu tô falando.

02:01

Então, como que essa IA vai aprender? Ela é treinada com um volume gigantesco de dados de entrada, beleza? Então, dentro dessa IA generativa, a gente vai capturar quais são os padrões subjacentes e quais são as estruturas que a gente poderia chamar de invisíveis, que estão organizando as informações.

02:20

Então, com isso, ela desenvolve uma capacidade quase que intuitiva de prever quais são os elementos que fazem sentido e quais não fazem sentido. É com base no que eu falei para vocês, por exemplo, de uma conversa. Como você sabe qual o contexto que eu estou falando as palavras? Por exemplo, eu posso estar falando de encadeamento, estou falando de cadeia. Pode ser de pessoa presa, talvez, o encadeamento de palavras, ou o encadeamento de alguma outra coisa.

02:48

é muito importante você conseguir prever como essas palavras vão se conectar na linguagem é assim que funciona então querendo ou não ela junta essas capacidades de previsão da próxima palavra que vem para ela conseguir entender qual o sentido para este conjunto e que não faz sentido para esse conjunto isso para compreender para depois sim ela pensar no mapa probabilístico que ela vai fazer dado o universo que ela tá vendo

03:16

E a partir desse mapa, ela consegue viajar por alguns caminhos que até então a gente não conhecia, nem ela conhecia. E vai produzir coisas novas. Exemplos coerentes com o que foi aprendido, mas diferentes do que foi aprendido. Então, é basicamente a conexão neural que eu falo pra vocês. Imagina que ela tem as suas sinapses, assim como o ser humano, a gente pode pensar desse jeito.

03:40

E essas conexões neurais, elas são montadas com base no contexto de entrada e com base no que ela já tem de treinamento inicial. Então você treina ela com um monte de dados. Com esse monte de dados, ela consegue ser mais assertiva. Você conseguiu calibrar a assertividade dela. Aí com base numa entrada, a assertividade dela em conseguir chegar no resultado de saída que faça sentido e não seja uma alucinação, fica cada vez maior.

04:08

Deu pra entender? Vamos dar mais um passinho pra ver se a gente aprofunda mais esse conhecimento. Então vamos fazer uma abstração aqui entre nós. Imagina o seguinte, imagina que a gente tem um cartógrafo, uma pessoa que faz ali os mapas. E essa pessoa que faz os mapas, ela consegue observar que tem montanha, que tem rio,

04:26

que tem árvores, que ele consegue entender tudo que tem ali no meio dessa composição do mapa, que são os dados de entrada, beleza? Então com base nisso você sabe mais ou menos como funcionam os terrenos, fechou? Então você já sabe como é que a banda toca, quais são as regras. Mas em vez dele só marcar, por exemplo, aqui é o Monte Tibete, aqui é o Pico de Everest, aqui é a Praia de Santos, aqui é não sei o que, ele consegue determinar

04:55

onde pode surgir uma nova montanha com base naquilo que ele tá enxergando e fala, olha normalmente a probabilidade é ter uma montanha aqui então consigo compreender que vai ter uma montanha ali pode ter um rio que pode virar pra cá eu consigo criar um novo mapa por mais que este não exista

05:11

com base no mapa que eu aprendi então com base no mapa que eu aprendi você pode falar agora cria um mapa de uma cidade parecida com essa eu vou lá e começa a construir esse mapa porque eu já sei como funciona essa cidade eu vou criar um mapa original de uma nova cidade ilusória e com base na cidade inicial que eu olhei por exemplo então com isso ele pode então desenhar coisas novas tá bom

05:35

Quais são os modelos autoregressivos? Acho legal a gente falar um pouco disso. Quando eu falo de um modelo autoregressivo, eu estou dando, por exemplo, o chat GPT. Esses modelos vão operar como se eles estivessem escrevendo um texto.

05:51

Palavra por palavra. E eles vão decidir qual a próxima palavra com base nas palavras anteriores. Beleza? Então, cada escolha de palavra influencia a seguinte palavra. Então, imagina que você dá seus dados de entrada que você quer. E daí, com base nisso, você pediu pra ele gerar um texto novo. Então, eu fui lá e falei, cara, com base nos livros do Harry Potter, crie um livro parecido.

06:16

Ele vai fazer o seguinte, vai ver essa base de conhecimento, vai pegar o estilo e as regras. Aqui ele montou a sua regra, como se fosse o algoritmo se montando. Estruturou. Vou começar a gerar o próximo passo. Para gerar, cada escolha de palavra na geração vai determinar a próxima. Então, além dessa,

06:35

Nessa entrada de aprendizado dos livros que já existem, as palavras que ele vai construindo vão gerando a próxima palavra. Então, é autoregressivo, ele vai se autocompletando conforme o processo de criação, até o conteúdo estar completo. Com isso, ele consegue garantir que aquilo está tendo contexto coerente.

06:57

Então, como o escritor, quando ele tá compondo a história dele, o que ele faz? Com base no que já foi escrito, ele vai mantendo coerência ao longo do fluxo que ele tá fazendo, ao longo da sequência que ele tá seguindo. Ele não simplesmente escreve ali duas, três palavras e já sabendo o que tem lá no fim, normalmente.

07:15

ele vai pensar no texto e vai vendo se aquilo tem coerência e montando isso. Por mais que isso seja às vezes até intuitivo, é isso que a nossa cabeça faz. Então quando a gente tá falando, a mesma coisa. A frase que eu tô falando agora, vai preparando a frase subsequente. Por isso que várias vezes a gente gagueja, a gente pensa um pouco mais, a gente tem que se preparar porque a nossa cabeça ainda tá falando,

07:36

Como é que eu conecto tudo isso que eu tô falando com o caminho que eu tava indo? Como que a gente consegue então, de vez em quando, por exemplo, a gente chegar à conclusão de por que eu tava indo pra esse assunto mesmo? Ou seja, eu comecei uma explicação no meio, eu me perdi, porque em algum momento eu alucinei, assim como o Mai alucina, e comecei a falar de um contexto que às vezes eu não soube ligar de volta.

07:59

Fui pra esse caminho aqui que até tinha alguma relação, mas no momento eu me perdi. E chega em determinado momento eu falo, por que eu fui pra cá mesmo? Então, eu até sei qual era a ideia inicial e eu me perdi. É a mesma coisa, quando a gente tá falando de modelos autoregressivos, eu tô tentando buscar essas informações e montando elas ao longo da conversa, ao longo da geração. Aí ela vai fazer isso também pra garantir a sua conexão. E o ChatGPT é muito forte nisso.

08:26

tem um outro modelo que é de auto-atenção ou de self-attention, que a gente fala. Quando a gente tá falando desse mecanismo, esse modelo, ele mantém o foco, tá? É focar nas relações importantes dentro de uma sequência longa, ou seja, ele exclui tudo aquilo que são elementos muito distantes um do outro. Então, quando a gente tá falando

08:49

de, por exemplo, lendo um livro. O modelo é como se ele conseguisse lembrar do personagem principal apresentado lá no primeiro capítulo do livro, e com base nisso, ele vai chegando ao longo dos capítulos e mantendo a continuidade da história com base nesse personagem principal. Então, a habilidade de você manter a atenção naquilo, por mais que você tenha um conjunto muito grande de contextos,

09:15

você consegue manter a atenção naquilo que é crucial para a história, por mais que tenha coisas desconexas ao longo do caminho. Então, essa habilidade consegue ser muito utilizada para a geração, principalmente de textos longos, quando a gente está falando de criação de conteúdo. Então, quando eu falo para o Gen AI criar um livro, por exemplo, como eu falei, essa ideia de self-attention ajuda ele a manter a conexão inicial com tudo que está saindo para a ponta. Deixa eu tentar recapitular aqui, então, para a gente entender.

09:44

Imagina que você tem várias coisas rolando de contextos que estão muito distantes um do outro dentro de um texto, mas você tem a relação inicial daquilo que você passou para ele como correlação do que está sendo descrito. Então, você consegue criar uma certa conexão.

10:03

a gente vai aprofundar muito mais nesse modelo ao longo dos próximos capítulos mas já é legal vocês terem na cabeça um pouco disso e depois eu vou dando mais abstrações trazendo mais formas de pensar não tem problema se até aqui você não pegou porque é complexo mesmo é difícil até de explicar

10:18

Mas a gente vai explicar de outras maneiras ao longo do curso também, eu vou passar pra vocês mais detalhes e aí vocês vão conseguindo fixar mais isso. Então, self-attention é mais ou menos isso que eu passei pra vocês. Vamos falar de um outro contexto que é super importante que a gente vai falar. São os embeddings e a representação de vetores, tá bom?

10:38

Quando a gente está falando desses contextos, a gente está falando basicamente o seguinte, antes de processar dados como palavras, por exemplo, imagem, código, aí ela vai transformar tudo isso em vetor matemático. Ela não vai olhar uma palavra, ela vai olhar um cálculo, é um vetor. Então, por trás ela está fazendo o quê? Vetorização e com base nessa representação numérica, que querendo ou não é uma linguagem universal, se a gente parar para pensar assim,

11:02

a gente é capaz de entender o significado do texto então ela vai transformar tudo em vetor com base no vetor ela vai entender a correlação vetorial e com base nisso ela vai conseguir compreender o contexto então ela não tá olhando português ou inglês ela tá olhando por trás cálculo matemático esses vetores eles são como se fosse coordenado imagina que a gente está falando aqui de sair pela rua e indo para algum lugar a gente está pegando as coordenadas de um espaço só que semântico aqui de palavras e não

11:28

um espaço temporal ou um espaço geográfico, e dentro desse contexto de palavras, desse contexto semântico, a gente consegue ver a proximidade entre pontos que vai refletir uma similaridade ali do conteúdo que eu tô falando. Então eu vou dar um exemplo pra vocês que fica mais fácil de entender. Vou dar um exemplo assim, por exemplo, rei e rainha são próximos?

11:54

são próximos. Na semântica, nessa proximidade, eu consigo dizer que rei e rainha é como se fosse São Paulo e Osasco. Agora se eu falasse rei e cachorro,

12:11

São próximos. Depende se for o rei da Inglaterra, que tinha a rainha com vários corgis, talvez. Brincadeira. Mas rei e cachorro são diferentes, são distantes. Normalmente rei e cachorro não estão no mesmo contexto.

12:27

podem estar, mas normalmente não estão. A probabilidade de estar é muito baixa, então no vetor você vai deixar esses caras distantes. Para a Gen AI ele vai olhar isso de uma forma distanciada. Seria como falar São Paulo e Rio de Janeiro, ou São Paulo e... vamos ver... São Paulo e Nova Iorque, você está cada vez mais distante, cada vez o contexto não faz mais sentido, então esse cara possivelmente não vai ser o caminho traçado por essa Gen AI, beleza?

## Resumo IA

**Abreviações**  
- IA — Inteligência Artificial  
- Gen AI — Inteligência Artificial Generativa  
- ChatGPT — Chat Generative Pre-trained Transformer  
- self-attention — autoatenção  
- token — unidade mínima de processamento/geração de texto  

**Resumo**  
A aula explicou como a IA generativa aprende de forma diferente da IA tradicional. Enquanto a IA convencional mapeia entradas conhecidas para saídas esperadas, a IA generativa aprende distribuições de probabilidade sobre padrões, sequências e combinações possíveis, construindo um mapa probabilístico do que faz sentido em cada contexto. O instrutor usou analogias como a de um artista, que internaliza estilos ao observar muitas obras e depois cria algo novo sem copiar literalmente, e a de um cartógrafo, que aprende a estrutura de um terreno e passa a inferir possibilidades novas a partir dele. A ideia central é que a geração não surge do nada, mas da recombinação coerente de padrões aprendidos em grandes volumes de dados.  

Também foi explicado que o treinamento com muitos dados permite capturar estruturas subjacentes e regularidades de linguagem, estilo e associação, aumentando a capacidade do modelo de prever o que vem a seguir e reduzindo a chance de alucinações. Em seguida, a aula abordou os modelos autoregressivos, que geram conteúdo token a token, escolhendo cada próximo elemento com base nos anteriores, como acontece na escrita humana ao construir frases e parágrafos progressivamente. Por fim, foram introduzidos os mecanismos de self-attention, que ajudam o modelo a manter relações relevantes ao longo de sequências longas, e os embeddings, que transformam palavras, imagens ou código em vetores numéricos em um espaço semântico onde proximidade representa similaridade de significado.  

**Pontos de atenção**  
- A IA generativa não busca apenas “respostas corretas”; ela trabalha com probabilidades e plausibilidade contextual.  
- Quanto melhor e mais amplo for o treinamento, maior a chance de coerência e menor a chance de alucinação.  
- A originalidade da Gen AI vem de recombinação de padrões aprendidos, não de criação sem base prévia.  
- Em modelos autoregressivos, cada token gerado afeta o próximo; erros podem se propagar ao longo da sequência.  
- Self-attention é essencial para manter continuidade em textos longos, especialmente para retomar عناصر mencionados no início.  
- Embeddings traduzem símbolos em vetores; o modelo opera matematicamente, não “lendo” linguagem como um humano.  
- Proximidade vetorial indica similaridade semântica: termos de contextos parecidos ficam próximos, e termos desconexos tendem a ficar distantes.  
- Em prompts longos ou muito abertos, a chance de o modelo “se perder” aumenta se o contexto inicial não estiver claro.  
- As analogias usadas na aula ajudam a entender, mas não substituem o mecanismo técnico real do modelo.