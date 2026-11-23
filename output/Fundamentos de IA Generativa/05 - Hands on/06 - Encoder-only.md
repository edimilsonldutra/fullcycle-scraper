Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16399)

## Resumo da aula

Transformers deram origem a três famílias arquiteturais: encoder-only, decoder-only e encoder-decoder. Essa divisão existe porque o transformer completo combina codificação e decodificação, o que aumenta custo e complexidade. Em muitas tarefas, usar a arquitetura inteira é desnecessário; basta isolar a parte mais adequada ao problema. Quando o objetivo é entender texto, classificar conteúdo ou medir similaridade, a família encoder-only é a escolha natural.

Encoder-only é a versão do transformer que mantém apenas o bloco de codificação. Seu foco não é gerar texto token a token, mas construir uma representação contextualizada da entrada inteira. Isso o torna especialmente adequado para tarefas de compreensão, como classificação, extração de informação e transformação de frases em vetores. Em troca, ele tende a ser mais leve, mais rápido e mais barato do que arquiteturas voltadas à geração.

BERT foi o marco inicial da família encoder-only e consolidou essa arquitetura como padrão para compreensão textual. O nome significa Bidirectional Encoder Representations from Transformers, destacando que o modelo lê o contexto em duas direções. Em vez de prever a continuação de uma sequência como um modelo gerativo, ele aprende a representar o significado do texto de forma rica e contextual. Essa diferença explica por que BERT se encaixa melhor em análise e entendimento do que em geração aberta.

Atenção bidirecional significa que cada token pode considerar simultaneamente os tokens à esquerda e à direita. Isso muda a qualidade da representação porque o significado de uma palavra depende do contexto completo, não apenas do que veio antes. Em um encoder-only, o modelo calcula pesos de atenção para ambos os lados e produz embeddings contextualizados em cada camada. O resultado é uma leitura global da sentença, útil para identificar intenção, entidade, tema e relação semântica.

O processamento começa com tokenização, seguida da conversão dos tokens em vetores com informação posicional. A partir daí, as camadas do encoder refinam essas representações ao relacionar cada token com os demais da sequência. No fim de cada camada, cada token deixa de ser apenas um símbolo isolado e passa a carregar contexto semântico. Essa base vetorial é o que viabiliza classificação, NER, embeddings e busca semântica.

O treinamento clássico do BERT usa Masked Language Modeling, no qual algumas palavras da entrada são ocultadas e o modelo precisa inferi-las a partir do restante da frase. Esse objetivo força o encoder a aprender dependências contextuais completas, porque a resposta correta pode depender tanto do lado esquerdo quanto do direito. O ganho principal não é fluência gerativa, mas capacidade de compreensão. Por isso, encoder-only aprende a preencher lacunas com base no contexto global, e não a continuar texto livremente.

Classificação é uma das aplicações mais diretas de encoder-only. O modelo recebe um texto e produz uma representação suficiente para decidir, por exemplo, se o conteúdo trata de medicina, romance ou outro tema, ou se expressa sentimento positivo, negativo ou neutro. Retomando o cenário de análise textual já familiar em produtos digitais, isso permite ler feedbacks, atendimentos e comentários e transformá-los em categorias úteis para operação. A vantagem é que a arquitetura foi otimizada exatamente para entender o texto antes de rotulá-lo.

Named Entity Recognition identifica trechos do texto que representam categorias como pessoa, organização e local. Em uma frase como “Steve Jobs fundou a Apple em Cupertino”, o modelo separa “Steve Jobs” como pessoa, “Apple” como organização e “Cupertino” como local. Esse tipo de saída é valioso para extração estruturada de informação, preenchimento automático e indexação de grandes volumes de texto. A tarefa depende de contexto fino, e por isso se beneficia da leitura bidirecional do encoder.

Encoder-only também é amplamente usado para gerar embeddings de sentenças e documentos. Nessa abordagem, textos semanticamente próximos tendem a produzir vetores próximos, mesmo quando não compartilham as mesmas palavras. O par “como fazer um bolo” e “receita para preparar um bolo” ilustra isso: a superfície lexical muda, mas o significado permanece semelhante. Essa propriedade sustenta busca semântica, em que a consulta e os documentos são comparados por similaridade vetorial em vez de simples coincidência de termos.

A família BERT inclui variantes com compromissos diferentes entre custo, velocidade e qualidade. RoBERTa amplia treinamento e dados para obter representações mais fortes; DistilBERT compacta o modelo para reduzir latência e custo; ALBERT compartilha parâmetros para diminuir tamanho e acelerar inferência. Essas variantes preservam a lógica encoder-only, mas ajustam o ponto de equilíbrio operacional. A escolha entre elas depende da restrição dominante do sistema: qualidade máxima, orçamento ou tempo de resposta.

## Transcrição

00:00

Fala pessoal, beleza? E aí, prontos pra mais uma rodada aqui de aulas sobre LLMs e sobre IA generativa? Galera, vamos lá! Eu quero falar com vocês nessa aula de um assunto extremamente importante, tá?

00:17

a gente vai falar um pouco das arquiteturas e os tipos de modelo de IA, tá bom? Então vamos começar a entender um pouco mais isso. Mas, pensa no seguinte, a minha estratégia aqui com vocês foi ir colocando de pouco a pouco as matérias e o aprendizado pra vocês, porque IA é complexo. Então a gente teve aqui até agora, sei lá, sete horas de curso, dentro dessas sete horas eu fui colocando cada hora um pouquinho do tema pra vocês irem se ambientando, irem entendendo como que essa coisa funciona.

00:47

Se minha estratégia deu certo, alguns de vocês vão começar a achar o que eu tô falando daqui pra frente um pouquinho repetitivo. Porque a ideia agora é a gente colocar os conceitos dentro dos quadradinhos dos quais eles pertencem. Então, ao longo de todo o curso eu vou contando pra vocês como as coisas funcionam. E a ideia é que agora esteja simplificada a ponto de vocês olharem e falarem, poxa, mas era só isso?

01:10

Se for isso, ótimo, consegui atingir meu objetivo. Se não, problema zero, porque a gente vai repassar de alguma forma e você tende agora a conseguir consolidar esse conhecimento, tá bom? Então vamos lá, quando a gente tá falando de arquiteturas e tipos de modelos, vocês vão notar que a gente já passou por isso, tá bom? Só que a gente passou por isso de uma forma mais simplificada.

01:30

Vamos então entender agora no detalhe. Quando a gente tá falando de LLM, a gente teve lá aquela discussão da criação dos Transformers, beleza? Então a gente foi lá e definiu que a gente ia trabalhar com Transformers. Quando a gente falou sobre Transformers, surgiram basicamente três tipos de arquitetura, tá?

01:49

Uma delas é chamada de encoder only, outra é decoder only e a outra é encoder decoder, beleza? São essas três arquiteturas que a gente vai falar aqui. Vamos falar da primeira então, tá?

02:04

é logo na sequência mas antes dela o que que a gente vai falar de cada uma delas a gente vai aprender quando a gente usa cada uma delas tá então qual o sentido faz qual momento deveria usar a gente vai aprender qual a diferença de cada uma delas como que elas são treinadas e como que elas são organizadas e com base nisso a gente saber escolher então qual é a ferramenta ideal para cada tarefa que a gente vai executar quando a gente vai falando de uma arquitetura beleza então

02:32

basicamente essa é a estrutura dessa aula aqui com vocês quando a gente está falando de encoder, eu tenho dificuldade de falar em encoder only porque eu acho que é as palavras se juntam em encoder only vamos lá então seja apenas codificador traduzindo para o português que facilita

02:54

Quando a gente está falando de encoder only, a gente vai entender como essa arquitetura funciona, porque ela é uma das arquiteturas que ajuda em grande parte do que a gente faz no dia a dia, tá bom? Então, por que essa arquitetura surgiu lá atrás? Pensa que é o seguinte... Lá, a gente teve o lançamento daquele paper que eu falei para vocês, que é... Attention is all you need.

03:16

em 2017, lá pelo pessoal do Google. Então a gente teve esse lançamento desse paper e esse paper lançou os Transformers, beleza? Mostrou pelo menos para o mundo Transformers. A partir desse momento,

03:30

Começou a discussão ali de uma nova maneira de lidar com as sequências sem depender daquela ordem rígida de RNNS que a gente falou lá no começo da nossa aula. Beleza? Até aqui todo mundo junto. Tá bom. Só que tinha um problemão acontecendo. Esse modelo completo, que é o Transformer, ele é um cara que ele junta encoder e decoder. Então ele tá com os dois juntos.

03:58

é muito pesado. Você tem que trabalhar os dois lados da arquitetura de um LLM. E daí veio uma ideia. Para algumas atividades eu não preciso ter isso completo. Eu posso quebrar aqui e usar só o encoder ou usar só o decoder. E por isso que viraram três. Uma encoder only, decoder only e a outra é com os dois juntos. Quando a gente está falando de encoder only,

04:23

foi uma simplificação que a gente criou para a gente conseguir executar algumas tarefas que não exigem a criação de conteúdo, ou seja, eu não preciso gerar um conteúdo textual extenso, mas eu preciso compreender um conteúdo textual extenso. Então quando a gente está falando aqui do encoderole, ele tem basicamente a sua principal função é na compreensão e não na geração, tá bom?

04:50

Então, por exemplo, quando a gente vai usar esse carinha aqui? Se eu precisar classificar um texto, se eu precisar extrair informações, se eu precisar transformar a frase em vetor... Para isso, ele é ótimo. Então, a gente vai conseguir usar ele porque ele vai ser mais leve, ele vai ser mais rápido, ele vai ser mais barato e a gente consegue resolver esses problemas. Agora, eu preciso classificar esse texto e usar ele para criar um novo texto. Não é o melhor cara.

05:15

Mas se eu precisar só classificar, por exemplo, se esse texto é romance, ou se esse texto é sobre um assunto específico, sobre medicina, ele vai ser melhor para isso, porque ele consegue ter esse modelo de entendimento melhor.

05:30

Então quando a gente tá falando desse carinha aqui, ele teve o seu primeiro modelo de encoder only lançado lá em 2018, logo na sequência. Então o Attention Is All You Need foi lançado em 2017 e logo na sequência já veio a ideia do encoder only, que foi o BERT.

05:48

O BERT significa Bidirectional Encounter Representation from Transformers. Então, esse carinha, ele veio pra conseguir resolver esses problemas que eu falei, foi o primeiro que foi lançado pelo Google também. Então, eles já estavam fazendo ali toda uma estratégia, então em 2018 eles já soltaram isso também, que era essa estratégia de usar só um pedacinho.

06:12

Então essa arquitetura é como eu falei para vocês, composta só da parte de codificação do Transformer, ela não vai usar a outra parte do Transformer, ele usa só o primeiro pedaço.

06:28

ela usa então ali pra gente compreender os textos e assim por diante então diferente dos modelos giradores ela não vai tentar entender qual o próximo token acho que essa é a grande sacada ela não quer saber qual é o próximo token da sequência ela quer sim

06:44

conseguir entender toda a entrada de texto ao mesmo tempo. Esse é o melhor jeito da gente pensar nela. Então, ela não quer prever o próximo e sim compreender tudo que ela tá lendo. Ela é mais uma leitora do que uma criadora, tá bom?

06:59

Então quando a gente tá falando dessa tensão bidirecional, que a gente tem que diferenciar o grande direcional que veio com o Berti, ou com os similares deles, ela consegue fazer o que? Ela não vai olhar só pra frente, como a gente já falou, isso aqui a gente já falou ao longo do nosso curso, ela olha tanto pra frente quanto pra trás, ela olha a sentença inteira ao mesmo tempo, e com isso ela consegue ver o total do texto, tanto que vem antes, tanto que vem depois, e calcular os pesos

07:23

e atenção para ambos os lados. Então ela consegue olhar mais de forma geral porque ela tá enxergando ali de texto. Isso é totalmente diferente do GPT que ele vai olhar só pra frente. Então ele olha só pro passado e gera o futuro. O BERT não. Ele consegue olhar pra frente e pra trás e ir fazendo essas coisas se falarem, tá bom?

07:43

Quando a gente tá falando do treinamento, ele muda um pouquinho, a gente também já falou do treinamento dele, de certa maneira, em determinado momento a gente falou logo no comecinho das nossas aulas, mas eu vou retomar aqui com vocês. Primeira coisa, o que ele vai fazer quando a gente tá montando esse modelo? Ele vai ter a tokenização, sempre tem a tokenização.

08:03

O texto vai ser dividido em tokens e depois ele vai ser convertido em vetores, beleza? Isso é básico de qualquer LLM. Com os elements posicionais que ele precisa ter ali, fechou? Então cada um vai ter ali a sua senha de posição. A camada que ele tem de atenção bidirecional é colocada. Cada token vai olhar para os outros tokens, a esquerda e a direita. E daí o modelo vai calcular qual é a importância relativa entre as palavras da esquerda e da direita.

08:32

Com base nisso, ele monta uma saída contextualizada, ou seja, ao final de cada camada do encoder, cada token ganha uma representação vetorial que já tem dentro dele esse entendimento de importância relativa entre palavras. E daí com isso vai refletir o significado no texto. E como é que ele treina esse modelo? A gente falou um pouco disso, aquele modelo de mascaramento, é o Masked Language Model.

09:00

Esse Masked Language Modeling, ele tem o que? Algumas palavras vão ser ocultas e o modelo vai ter que prever quais são essas palavras com base no contexto completo. Então isso mostra que ele conseguiu compreender o todo, olhar pra frente e pra trás e tapar os buracos. Com isso ele tem uma capacidade de compreensão textual mais do que criação do texto todo. Então basicamente é assim que ele é treinado, tá bom gente? A gente falou um pouco disso.

09:28

Mas agora você consegue colocar ele na caixinha certa. Você sabe que esse carinha, ele vai ser um Encounter Only, beleza? Que é o Bert. Marca isso na sua cabeça, ou caras similares ao Bert. Onde você vai usar esse cara?

09:45

Por exemplo, classificação de sentimentos. Se você estiver fazendo alguma atividade onde você precisa, por exemplo, ter todo o atendimento de telefonia de uma empresa e saber se o cliente está atritado ou não, assim por diante, você pode usar isso como classificação de sentimento. Ou se você precisa saber se as pessoas estão achando o seu produto bom ou ruim, em alguma análise de NPS que seja um pouco mais inteligente, você consegue fazer isso também.

10:10

desde que você pegue o texto que essas pessoas estão trocando. Você poderia usar isso até nas redes sociais para entender como o seu produto está sendo falado por aí. Então, esta é uma maneira de você usar os modelos de encoder only. Outra coisa que também é legal de usar, usar ele no NER, tá? Named Entity Recognition. O que significa? Se eu colocar, por exemplo, Steve Jobs fundou a Apple em Cupertino, beleza?

10:38

Eu preciso saber quem é a pessoa, Steve Jobs. Qual é a organização? Apple. E qual é o local? Cupertino. Então ele consegue jogar isso, ele quebrou isso em categorias. Nome, local e organização.

10:55

porque ele conseguiu olhar no texto e falar, putz, isso aqui é dessa categoria, isso é dessa, isso é dessa. Então, pode te ajudar, inclusive, se você precisar, por exemplo, fazer estratégias de preenchimento automático de texto, ou de categorização de análise de dados massivos, assim por diante. Você consegue fazer várias coisas aqui.

11:14

Outra coisa bacana que também tem é a busca semântica, tá bom? Para a busca semântica, o texto precisa ser convertido primeiro em um vetor de significado. Então, você vai transformar esse texto em significado e depois você vai buscar nos documentos com base de similaridade do vetor

11:36

qual é parecido com ele. Então pense o seguinte, em vez de você procurar a palavra, você vai pegar no documento, você vai pegar o texto, vai converter ele num vetor. Aí depois você vai pegar todos os documentos que você tem, vai pegar os textos e converter em vetores. E quando você chegar num vetor similar, você vai falar, opa, esses dois caras estão falando do mesmo assunto. E daí você vai conseguir ter similaridade vetorial, tá bom? Esse é um jeito de você fazer.

11:59

Outra coisa também que tem interessante para você ter na cabeça é que você também tem os Embeddings para similaridade, eles não são iguaizinhos os outros Embeddings que a gente estava falando, tá? Então, você tem ali a primeira entrada, por exemplo, como fazer um bolo, tá bom? Essa é a entrada 1. Você tem a entrada 2, receita para preparar um bolo. Os dois textos, eles têm Embeddings similares porque eles são

12:28

de semânticas parecidas. Como preparar um bolo e receita para preparar um bolo são parecidos, então eles vão ter embedings de similaridades, beleza? Então isso é importante de ter na cabeça também porque é assim que o modelo vai funcionar. Bom,

12:45

basicamente é isso tá gente qual que é a sacada aqui que eu quero que vocês tenham agora a gente sabe qual o nome como funciona e onde se encaixa e pra que usar era aqui que eu queria chegar com vocês acho que com esse compreendimento é com essa compreensão perdão compreendimento é complicado com essa compreensão vocês vão conseguir é saber muito melhor o modelo porque e quando está usando e como funcionar por trás tá bom

13:13

Não existe só o Bert. Tem mais alguns e parece até uma brincadeira, mas eu vou tratar, trazer aqui pra vocês, pra quando vocês olharem os nomes, vocês saberem do que a gente tá falando. Mas é só pra conhecimento, tá? Então o Bert, ele foi o originalzão lá, tem seu bidirecional, treinado com MLM e INSP, então são dois jeitos de treinamento do Bert. Depois vem um outro cara que era o Robert A. Roberta, não vim das contas.

13:39

Esse cara aqui foi treinado com mais dados e mais processamento batch. Então ele foi um cara mais treinado.

13:50

tem um outro cara que chama distilbert também é uma versão mais compacta do bert mais rápido então pensa o primeiro cara ele foi gerado para fazer o todo o segundo é mais pesado mas é mais eficiente que é o roberta o terceiro distilbert ele é menorzinho ele é simplificado vai gerar um resultado um pouquinho piorado mas ele é mais veloz e mais barato e tem o albert que ele vai usar ali parâmetros compartilhados

14:20

Ele reduz o tamanho dele e acelera a inferência também. Então ele é mais eficiente do que o Bert, mas ele é mais caro também. Ele acaba funcionando com um resultado melhor, tá bom? Então basicamente são esses carinhas, se vocês ouvirem por aí. O que eu acho mais engraçado é o Roberta, parece o nome de uma mulher, mas não é. Inclusive, eu sempre tento trazer ele do jeito Robert A, pra vocês lembrarem depois como o Roberta. Porque daí fica fácil de vocês separarem quais são.

14:49

são esses caras que vocês vão ouvir no dia a dia beleza e pra fazer essas funções que a gente falou vamos voltar já já pra falar do próximo modelo de arquitetura tá bom a gente falou do encoder only o próximo que a gente vai falar agora vai ser do decoder decoder only e é isso aí valeu

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem Grande)
- **IA** — Inteligência Artificial
- **RNNs** — *Recurrent Neural Networks* (Redes Neurais Recorrentes)
- **BERT** — *Bidirectional Encoder Representations from Transformers*
- **NLP** — *Natural Language Processing* (Processamento de Linguagem Natural)
- **MLM** — *Masked Language Modeling*
- **NER** — *Named Entity Recognition*
- **NPS** — *Net Promoter Score*
- **GPT** — *Generative Pre-trained Transformer*
- **RoBERTa** — *Robustly Optimized BERT Approach*
- **DistilBERT** — versão destilada/compacta do BERT
- **ALBERT** — *A Lite BERT*

**Resumo**
A aula apresentou as três famílias arquiteturais derivadas dos Transformers — encoder-only, decoder-only e encoder-decoder — com foco na arquitetura encoder-only. O instrutor explicou que o Transformer completo combina codificação e decodificação, o que aumenta custo e complexidade, e por isso, em várias tarefas, faz sentido usar apenas a parte mais adequada ao problema. No caso do encoder-only, o objetivo é compreender o texto, e não gerar conteúdo token a token.

Foi destacado que o encoder-only surgiu como uma simplificação útil para tarefas de entendimento textual, sendo o BERT o modelo marco dessa família. O BERT, lançado pelo Google em 2018, lê o contexto de forma bidirecional, considerando simultaneamente o que vem antes e depois de cada token. Isso permite construir representações contextualizadas mais ricas, úteis para classificação, extração de informação, embeddings e busca semântica.

O fluxo explicado começa com a tokenização do texto, seguida da conversão dos tokens em vetores com informação posicional. Em seguida, as camadas do encoder aplicam atenção bidirecional, refinando a representação de cada token com base nos demais elementos da sequência. No treinamento, o modelo usa Masked Language Modeling, ocultando algumas palavras e tentando inferi-las a partir do contexto completo, o que fortalece sua capacidade de compreensão. A aula também mostrou aplicações práticas como classificação de sentimentos, identificação de entidades nomeadas, geração de embeddings e recuperação semântica por similaridade vetorial. Por fim, o instrutor citou variantes importantes da família BERT, como RoBERTa, DistilBERT e ALBERT, cada uma com trade-offs diferentes entre qualidade, velocidade e custo.

**Pontos de atenção**
- Encoder-only é indicado para **compreensão**, não para **geração de texto**.
- A atenção **bidirecional** é o diferencial principal: o modelo considera contexto à esquerda e à direita ao mesmo tempo.
- O treinamento com **Masked Language Modeling** força o modelo a aprender dependências contextuais completas.
- Para tarefas como **classificação**, **NER** e **busca semântica**, encoder-only costuma ser a escolha mais natural.
- Em busca semântica, o importante é **similaridade vetorial**, não coincidência literal de palavras.
- Textos semanticamente parecidos podem gerar embeddings próximos mesmo com vocabulário diferente.
- **RoBERTa** tende a ser mais forte em qualidade, mas pode exigir mais dados/processamento.
- **DistilBERT** reduz tamanho e latência, mas pode perder desempenho em relação ao BERT original.
- **ALBERT** usa compartilhamento de parâmetros para reduzir tamanho e acelerar inferência.
- A escolha da variante depende do equilíbrio desejado entre **qualidade**, **custo** e **tempo de resposta**.