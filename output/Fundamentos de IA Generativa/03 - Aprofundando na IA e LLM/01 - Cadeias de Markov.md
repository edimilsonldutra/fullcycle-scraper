Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16372)

## Resumo da aula

Bigramas modelam sequências olhando relações locais entre poucos elementos, enquanto HMMs introduzem uma estrutura interna para explicar como as observações são geradas. Essa mudança importa porque muitos fenômenos sequenciais não são descritos apenas por palavras adjacentes ou por sinais explícitos. O modelo passa a considerar que existe um estado do sistema que influencia o que é observado, mesmo quando esse estado não aparece diretamente nos dados.

Estado oculto é a variável interna que governa o comportamento do sistema, mas não é observada diretamente. O que se observa são saídas geradas por esse estado, chamadas observações ou outputs. A utilidade do modelo está justamente em inferir o estado interno a partir de sinais visíveis, como usar indícios para estimar uma condição que não está explicitamente disponível.

No cenário do clima, estados ocultos podem ser sol, chuva e nublado, enquanto observações podem ser céu limpo, vento forte e guarda-chuva aberto. O meteorologista não precisa observar diretamente toda a dinâmica atmosférica para inferir o estado provável; ele usa evidências indiretas. Esse é o padrão central do HMM: observações visíveis funcionam como pistas probabilísticas sobre um estado interno invisível.

Um HMM não assume que o sistema permanece fixo no mesmo estado; ele modela a chance de transição entre estados ao longo do tempo. Isso permite representar mudanças como sair de nublado para chuva ou reinterpretar um contexto quando uma nova evidência aparece. A matriz de transição codifica essas probabilidades e define como o estado atual influencia o próximo estado.

Cada estado oculto possui uma distribuição de emissão, isto é, uma probabilidade de gerar determinadas observações. Em termos práticos, o modelo responde perguntas como: se o estado for chuva, qual a chance de observar guarda-chuva aberto? Essa camada é essencial porque conecta o mundo interno do modelo ao dado efetivamente disponível para inferência.

Os elementos centrais do HMM são estados ocultos, observações, matriz de transição e matriz de emissão. A matriz de transição modela a probabilidade de mudar de um estado para outro, enquanto a matriz de emissão modela a probabilidade de cada estado produzir certas evidências observáveis. Juntas, essas estruturas permitem calcular sequências prováveis e interpretar dados sequenciais com incerteza.

O algoritmo forward-backward calcula a probabilidade de uma sequência observada, o que permite avaliar quão compatíveis os dados estão com o modelo. O algoritmo de Viterbi encontra a sequência de estados ocultos mais provável para explicar as observações. Já Baum-Welch, frequentemente associado a EM, ajusta os parâmetros do modelo com base nos dados observados, refinando transições e emissões.

Em reconhecimento de fala, os estados ocultos podem representar sons fonéticos e as observações correspondem aos sinais de áudio. Em POS tagging, os estados ocultos representam categorias gramaticais, como verbo e substantivo, enquanto as observações são as palavras da sequência. Isso melhora a construção de frases porque o modelo passa a considerar uma estrutura gramatical implícita, e não apenas a proximidade entre palavras.

Sequências genéticas também se ajustam bem a HMMs porque exibem estrutura sequencial probabilística clara. O modelo foi usado para identificar regiões específicas em cadeias de DNA a partir de padrões observáveis ao longo da sequência. Esse tipo de problema combina bem com HMMs porque a inferência depende de estados internos que não são diretamente rotulados no dado bruto.

HMMs capturam bem dependências de curto prazo, mas assumem que a próxima observação depende apenas do estado atual e que o estado atual depende apenas do estado anterior. Essa hipótese de Markov simplifica o problema, porém limita a modelagem de dependências longas e de interações cruzadas complexas. Em linguagem natural, isso reduz a capacidade de manter coerência em frases longas ou em contextos que exigem retroalimentação entre partes distantes da sequência.

A estrutura do HMM é linear no sentido de avançar estado a estado, sem representar naturalmente ciclos complexos de retroalimentação como os que aparecem no raciocínio humano e em modelos mais modernos. Além disso, muitos usos práticos dependiam de dados rotulados, e a rotulagem é cara e demorada. Por isso, embora HMMs tenham sido um avanço importante e ainda sejam úteis, eles não são a melhor escolha para geração livre de texto longo e coerente como a realizada por LLMs atuais.

## Transcrição

00:00

Fala galera, beleza? E aí, vocês estão prontos pra dar o próximo passo e pra fritar o cérebro? Agora é a hora da gente gastar nossa massa cinza, tá bom? Começar a falar algumas coisas um pouquinho mais complicadas, tá bom? Então a gente vai sair um pouco do conceito de bigrama e vai entrar nos HMMS.

00:17

HMMS é o Hiding Markov Models, tá bom? Então aqui a gente vai estar falando de um cara, querendo ou não. Markov foi um grande matemático, estatístico, que trouxe bastante coisa pra gente. Pra não ficar falando uma besteira, eu dei uma pesquisada aqui ó, no Wikipédia, sobre o Markov. Podia ter pesquisado no Chat de GPT? Poderia, mas eu fui na Wikipédia porque tem gente que ainda não confia tanto. Eu confio bastante, possivelmente lá ia vir a mesma coisa. Mas vamos lá.

00:44

Andrei Markov é o cara que criou basicamente a estrutura do que a gente vai conversar aqui, beleza? Quem era esse cara? Ele era um professor russo, ele estudou na faculdade de São Petersburgo,

00:59

se formou lá em 1888 e foi professor até 1886. Ele criou algumas teorias bem relevantes aqui sobre o limite de integrais, que deve ser bem complicado, teoria de aproximação e assim por diante. E depois ele criou algumas outras coisas aqui que foram na mão de coisas de probabilidade estatística.

01:23

E o principal ponto que ele fez, que é o estudo que a gente vai falar aqui um pouco, são as cadeias de Markov. Essas cadeias de Markov vão gerenciar aqui, vão seguir um pouco o que a gente vai conversar aqui no nosso papo, tá bom? Ele também teve um filho com o mesmo nome dele e que também foi matemático, seguiu ali basicamente a mesma ideia de profissão do pai. Então vamos lá.

01:44

Vamos dar sequência, parar de falar dele, vamos falar um pouco do que ele fez, tá bom? Então a gente tá saindo um pouco do que a gente tava falando ali dos bigramas e começando a evoluir a coisa. Porque é engraçado, quando a gente olha hoje os modelos de LLM que tem por aí, então olha, a gente vai falar agora de HMMS, a gente não tá falando de LLM ainda. Então os modelos de LLM que tem hoje são tão requintados, tão evoluídos, que quando a gente olha pra eles, a gente fala, poxa, como que alguém chegou nisso?

02:08

Alguém chegou nisso passando por um monte de dificuldade, as coisas são evolutivas. Então aqui a gente foi evoluindo ao longo do tempo e o HMMS foi uma evolução dos bigramas e que depois a gente conseguiu ir evoluindo até chegar no que tem hoje. HMMS é um pouquinho mais complicado, então vamos devagar, eu vou tentar explicar pra vocês e a gente vai evoluindo.

02:27

Se eu estiver falando um pouquinho e vocês não tiverem entendido ainda, fica tranquilo que conforme eu for falando na explicação, eu vou dando exemplos e possivelmente você vai conseguir pegar. Caso não consiga, volta no vídeo, tenta assistir de novo. Se não der, não entendeu, me chama nas redes sociais, me procure e a gente troca mais uma ideia sobre o assunto, tá bom? Então vamos lá.

02:46

A primeira coisa que a gente tem que pensar é que é o seguinte, lembra que eu falei pra vocês que a gente tava com os modelos de bigrama que pensam muito sobre um modelo linear, que eu só consigo ver as duas primeiras palavras ali, então só os dois conjuntos, nem duas primeiras, perdão, os dois conjuntos, tanto pra frente quanto pra trás, eu tô sempre trabalhando com dois.

03:06

Dois grupinhos de palavra. Aqui quando a gente tá falando da cadeia de Markov, a gente começa a fugir um pouquinho disso, a gente começa a incluir uma complexidade interessante. Então lembra que eu falei pra vocês sobre... Poxa, se vocês estiverem olhando a minha blusa, vocês vão achar que tá frio? Tudo isso são...

03:25

são tomadas de decisão observáveis que vão trazer para vocês a capacidade de inferir algo. Com essa tomada de decisão observável para inferir algo, eu consigo pensar numa conexão

03:42

basicamente é isso que foi colocado aqui nessa matemática no final do dia tá então a gente sai um pouquinho ali nesse modelo só de duas palavras e começa a olhar mais um contexto global e fora o contexto global eu começo a incluir essa visão de itens que eu não conseguiria traduzir diretamente em dados eu preciso observá-los tá bom então é basicamente isso então você vai sair das

04:07

das dependências explícitas que a gente tem só de palavras, e você vai começar a olhar uma ideia de uma estrutura interna que governa toda essa geração de observação e tomada de decisão, que não é diretamente visível, como por exemplo está escrito na minha testa aqui quantos graus está hoje.

04:25

Beleza? Isso seria totalmente visível, você conseguiria saber do que eu tô falando sem ter que olhar e inferir, certo? Então é basicamente disso que a gente tá falando, tá bom? Então esse conceito de estado oculto que a gente vai falar aqui, que vai permitir a gente modelar

04:42

um comportamento um pouco mais realista sobre as sequências de criação que a gente tem para falar. Então vai começar a ajudar a gente a pensar em sons como a Alexa fez lá atrás ou o Google mesmo quando a gente usava ali as nossas assistentes, uma parte de fala, a gente começa a ter ali um encadeamento que permite essa relação, beleza?

05:05

Então vamos lá, o que que significa esse HMM? A gente tá falando nada mais do que um sistema estatístico por trás. Eu expliquei pra vocês o conceito que gere o sistema estatístico, mas é um sistema estatístico. E ele vai ser montado com base em um carinha que chama Estado Oculto.

05:23

Vocês vão ver na literatura como Hiding States, porque normalmente vai estar em livro em inglês. Tem pouca literatura, ao meu ver, em português que consegue dar esse apoio. Vocês conseguem achar os livros traduzidos, mas tem muito mais coisa em inglês para ler, tá? Eles vão representar ali a estrutura interna do sistema que vai tentar

05:40

ajudar a gente com aquilo que não é observado diretamente, tá bom? Então, o Siding States vai trazer essa visão do que não é de observação direta, não é um dado direto, é um dado que você precisa trabalhar. Tem as observações que são os outputs disso, que são os dados que a gente vê

05:57

que eles são gerados nos estados. Então, eu estou olhando os estados e com base nisso eu vou gerar dados, que são os outputs. E a gente tem as transições de estados. Ou seja, quando você começa no estado, ele não precisa continuar o tempo todo naquele estado, você pode transitar entre estados. Foi aquilo que eu falei para vocês. Imagina que eu estou de blusa, você está tomando as decisões e do nada sai um solzão aqui e você fala... Opa, calma aí... Informação nova, talvez ele não esteja com frio, ele colocou a blusa porque ele é bobo, sei lá... A gente pode pensar em uma outra coisa. Então, aqui...

06:27

você consegue trazer a probabilidade para essa tomada de decisão. Eu tô sempre trazendo exemplos mais simples possíveis pra não complicar ainda mais. Então, pensa que essa transição de estados pode acontecer. E daí depois você tem uma coisa chamada de distribuição de emissão. Cada estado oculto pode ter uma probabilidade

06:46

associada de gerar uma determinada observação, tá bom? Então a gente vai evoluir mais nisso pra vocês entenderem também. Deixa eu dar um exemplo pra vocês. Imagina que o meteorologista é muito em cima do que a gente tá falando aqui sobre a blusa. Imagina que o meteorologista tá tentando prever o clima. E ele precisa fazer isso com base em observações indiretas, não só com balão de meteorologia. Então, por exemplo, a cor do céu pode influenciar em como tá o tempo? Sim, se eu olhar pra cima e ver que tá tudo nublado, possivelmente o tempo não tá legal.

07:15

O vento, se estiver ventando muito, possivelmente deve estar mais gelado porque o vento ajuda a gente a ter essa sensação térmica. O que mais que eu posso ter aqui? Putz, tá incidindo sol, não tá? Então tudo isso vira ali observações indiretas, ou seja, ele não tá vendo direto no sistema atmosférico de balão, de meteorologia, etc. Mas ele consegue inferir nesse estado oculto e conseguir entender com base nesses sinais invisíveis.

07:42

querendo ou não, são invisíveis, né? Quer dizer, perdão, são visíveis, mas não são diretamente visíveis, se a gente pensar assim, tá? Então, se não são diretamente visíveis, você consegue inferir se isso tá gerando alguma informação legal pra você seguir na sua tomada de decisão. Beleza, vamos em frente.

08:03

Então, quais são os elementos centrais desse modelo? A gente tá falando então dos estados ocultos que eu falei ali. Vamos dar exemplo pra eles, pra facilitar? Sol é um estado oculto, chuva é um estado oculto, nublado é um estado oculto, no caso do clima que a gente falou aqui pra você. Agora, vamos lá. Se eu tiver falando de conjunto de observações dados esses estados ocultos, por exemplo,

08:27

céu limpo, vento forte, guarda-chuva aberto de uma pessoa que passou, eu consigo ver aqui observações possíveis dentro dos estados ocultos. Então eu sei que tem sol, tem chuva, tem nublado e com base nisso, nesses estados ocultos, eu consigo ter um conjunto de observações que vão me ajudar nisso. Então o céu tá limpo? Vai me ajudar. Vento tá forte? Vai me ajudar. Guarda-chuva tá aberto? É outro ponto aqui de observação possível que eu posso usar.

08:54

e tem a matriz de transição entre esses estados. Então, dependendo da minha matriz de observação, ou seja, o conjunto de observação que eu estou trazendo, eu posso definir a probabilidade de ir para um estado ou de ir para outro estado. Então, com isso, eu consigo evoluir um pouco nesse conceito. Qual é a matriz de emissão que eu falei para vocês? Ela vai definir a probabilidade que a gente tem de observar determinado evento. Então, imagina que eu olhei todos esses itens que eu falei para vocês, a minha matriz de emissão

09:24

Ela vai me falar como eu consigo determinar um evento a partir do estado oculto. Então eu tô olhando ali os estados ocultos e determinando o evento que é o próximo item de evolução da nossa conversa aqui, beleza?

09:39

Quais são os algoritmos principais que estão nessa cadeia? A gente tem um cara que chama forward, backward. Esse cara vai calcular a probabilidade de uma sequência observada. Então, qual a probabilidade dessa sequência acontecer? Olha o que eu falei. Qual a probabilidade dessa sequência acontecer? Sequência, beleza? Guarda isso, porque a gente vai falar disso nas limitações desse modelo.

10:05

Eu tenho outra coisa que eu sempre erro o nome, chama Viterbi. Por quê? Porque eu não sei a origem dessa palavra, sendo muito honesto, mas eu chamo de Viterbi. Vocês vão ver desse jeito. V-I-T-E-R-B-I. Isso vai mostrar a sequência de estados ocultos mais provável, tá bom?

10:28

Então, essa palavra Viterbi, normalmente ela vai estar falando sobre essa sequência de estados ocultos mais prováveis. E a gente tem uma outra coisa que chama Bound Welk EM, e normalmente vai estar entre parênteses, EM para vocês, que vai ajudar a gente a ajustar os parâmetros do HMMS, com base nos dados observados. Então, pensa nisso tudo que eu falei para vocês, deixa eu voltar... Então, back forward, eu estou falando da probabilidade de uma sequência observada. Quando eu estou falando do Viterbi,

10:58

como a gente encontra a sequência dos estados ocultos mais provável. Então, aqui eu tô falando do que eu consegui encontrar a dada probabilidade, beleza? E tem o BoundWalk, que é o que vai ajustar os parâmetros. Então, o primeiro ponto é eu calculo a probabilidade, o segundo ponto eu encontro qual é a sequência mais provável, e o terceiro ponto é como eu ajusto os parâmetros para ter os dados observados nos ajudando na definição do contexto, beleza?

11:27

Vamos lá! Chatinho, né? Esse aqui é um pouco mais complicado. Depois que eu evoluir isso, o que eu consigo aplicar dado essa relação que eu falei pra vocês? Primeiro ponto, reconhecimento de fala. Os estados ocultos, eles vão representar pra gente, por exemplo, sons fonéticos, as observações, são ali, por exemplo, os sinais de áudio que a gente tem.

11:53

Eu tenho um outro negócio super importante da gente pensar que são os post tagging, são part of speech tagging, post tagging, beleza? Part of speech tagging.

12:09

são os estados da categoria gramatical, tá bom? Então, verbo, substantivo e as observações, elas vão ser as palavras que a gente tá conseguindo colocar ali. Tá vendo que verbo, substantivo, etc, eles são estados de categoria, eles não são um dado direto, certo? Você trouxe pra cá uma complexidade gramatical pro meio da conversa. Como eu fiz a relação lá sobre chuva, sol e etc, aqui você começa a trazer

12:36

esses post tagging como itens que eu adiciono ali para a gente conseguir fazer essa observação acontecer. Então, eu consigo usar isso, aquela lógica que a gente falou de sol, chuva, etc, para pensar o que está vindo de categoria gramatical, verbo, substantivo, etc. Isso vai fazer o quê? Construção da frase. Então, eu vou conseguir, com base nisso, evoluir a construção da frase. Então, eu consegui ter uma aplicação direta, que é esse post tagging,

13:04

que me fez evoluir nas observações gramaticais, assim como eu faço com as observações temporais. E daí, com isso, eu consigo ter a criação de textos melhores do que a gente tinha antigamente, beleza? Eu também tenho uma outra coisa de aplicação importante, que é a biologia computacional.

13:23

Então, sequência genética, a gente usou muito isso pra gente conseguir quebrar, lembra as cadeias de DNA e etc? Isso foi muito utilizado, usado pra identificar quais são as regiões do DNA que são mais específicas e assim por diante. Então, esses casos, eles vão funcionar muito bem porque tem uma estrutura sequencial probabilística muito clara.

13:46

eu consigo ter uma sequência probabilística que vai dar certo possivelmente. Então você consegue capturar as dependências de curto prazo. Mas quando você tá falando de frases muito distantes, coisas muito desconexas, ele já começa a quebrar. E a gente já vai falar disso. Mas você já começa a sair de duas palavrinhas pra algo muito mais evoluído, tá bom?

14:07

E quais são as limitações? Lembra que eu falei pra vocês? Tem limitações aqui. Eu vou trazer algumas pra vocês. Ele vai, o HMMS, ele vai assumir que a próxima observação depende apenas do estado atual.

14:20

E o estado atual depende apenas do estado anterior. Então, isso vai limitar ele de capturar dependência de longo prazo. Então, quando a gente está falando de estrutura complexa de linguagem, como a gente tem no português, como a gente tem no nosso dia a dia, você começa a quebrar essa cadeia. Por que isso acontece? Porque ele é linear, é um sistema linear. Lembra que eu falei para vocês segurarem aquela informação há um pouco de tempo atrás? Ele é linear. Essa linearidade dele, significa que ele vai só numa direção.

14:50

Eu estou indo só para frente. Eu não tenho um dado que retroalimenta, se eu pensar desse jeito. Então, ele está indo sempre em uma só direção, sem ciclos complexos de interações cruzadas, que é o que a gente faz no nosso dia a dia. A gente não vai só em uma direção de linha de raciocínio e pensamento. A gente fica voltando. Lembra que eu falei para vocês? Eu tenho uma informação, uma decisão. Uma decisão, outra decisão. Com base nessa decisão, eu posso trazer informação para a primeira decisão.

15:16

Então a minha conexão neural funciona se retroalimentando, enquanto que numa cadeia de Markov ela é linear, tá bom? Então nessa cadeia linear ela vai só numa direção. Então você não consegue ter esses ciclos complexos de cruzamento de informação de múltiplos estados. Então isso deixa ele um pouquinho mais fragilizado.

15:36

com base nos modelos atuais que a gente tem que ser um pouco mais evoluído nesse sentido. Mas já é um baita salto. Parabéns pro Markov, ele foi um monstro porque ele criou uma ideia que ajudou muito a gente. Beleza? Quais são as outras limitações da cadeia de Markov? A gente tem um negócio chamado... Pensa que pros dados você precisa rotular eles, tá? Coisa que a gente já conseguiu resolver.

15:57

Então, você precisava rotular os dados pra você conseguir trabalhar. Então, um conjunto de dados, você não podia deixar ele solto. Você deveria trazer pra ele um rótulo, pra ele saber do que você tá falando. Então, você dá o contexto, dá o rótulo, principalmente pra você conseguir fazer as tarefas supervisionadas, e daí depois você evoluir isso. E o que tem de problema nisso? A rotulagem é um processo caro, pra quem já fez, de dados, é um processo de dados super caro,

16:24

e que demora pra fazer. E daí pra você conseguir treinar essas máquinas aqui, treinar esses algoritmos, você tinha um pouco mais de custo e era mais demorado pra fazer. Então tinha essa limitação também.

16:38

A gente ainda usa, tá? Tem bastante lugar que ainda usa os modelos de Markov, mas eles têm essas limitações aqui. Pra geração de texto, ele não foi muito gerado pra geração de texto livre. Então, pra conversas como, por exemplo, a GPT faz, não vai funcionar.

16:55

pra criação de frase longa, texto coerente, etc. Quando a gente manda, por exemplo, o chat de apt criar, sei lá, criar uma explicação sobre quem é Markov. Você precisa passar todos os itens ali e ele possivelmente vai quebrar a coerência e vai repetir alguns padrões. Vai ficar meio prolixo, tá bom? Então, possivelmente não vai ser a melhor estratégia. Pessoal, é um pouquinho mais chato, mas vocês já viram que a gente já deu um salto, né? A gente tava falando, então,

17:22

Primeiro de um modelo muito mais simplificado aqui, a gente falou bastante sobre os modelos de bigrama, a gente passou um pouco pelos modelos de bigrama e agora a gente foi pelas cadeias de Markov, então a gente já começou a evoluir. Olha a diferença, bigrama só tinha lá duas palavrinhas pra gente tratar por vez,

17:48

E agora a gente tá falando de cadeias de Markov, só que lineares e com dificuldade de conexão e de criação de textos mais prolongados. Mas vocês já veem que a conversa ficou mais complicada e a gente tá conseguindo seguir numa direção importante e interessante. Já já a gente volta pra dar o próximo passo.

## Resumo IA

**Abreviações**  
- **HMM** — *Hidden Markov Model* (Modelo Oculto de Markov)  
- **EM** — *Expectation-Maximization* (Expectativa-Maximização)  
- **POS tagging** — *Part-of-Speech tagging* (marcação de classes gramaticais)  

**Resumo**  
A aula apresentou a evolução dos modelos de bigramas para os HMMs, mostrando como eles adicionam uma estrutura interna capaz de explicar como as observações são geradas ao longo de uma sequência. O instrutor explicou o conceito de estado oculto como a variável interna que governa o comportamento do sistema sem ser observada diretamente, enquanto as observações são os sinais visíveis gerados por esses estados. Para tornar a ideia concreta, usou o exemplo de clima, no qual estados como sol, chuva e nublado geram observações como céu limpo, vento forte e guarda-chuva aberto, permitindo inferir probabilisticamente o estado interno a partir de evidências indiretas.

Também foram apresentados os componentes centrais do HMM: estados ocultos, observações, matriz de transição e matriz de emissão. A matriz de transição define a probabilidade de passagem entre estados ao longo do tempo, e a matriz de emissão define a probabilidade de cada estado produzir determinadas observações. Em seguida, o instrutor explicou os algoritmos principais associados ao modelo: forward-backward, que calcula a probabilidade de uma sequência observada; Viterbi, que encontra a sequência de estados ocultos mais provável; e Baum-Welch, associado ao EM, que ajusta os parâmetros do modelo com base nos dados observados.

Na sequência, foram mostradas aplicações práticas em reconhecimento de fala, em que estados ocultos podem representar sons fonéticos e as observações correspondem ao áudio, e em POS tagging, em que os estados são categorias gramaticais como verbo e substantivo e as observações são as palavras da frase. Também foi citada a biologia computacional, especialmente na análise de sequências genéticas e identificação de regiões específicas do DNA, área em que o modelo funciona bem por lidar com dependências probabilísticas sequenciais. Por fim, a aula destacou as limitações dos HMMs: eles capturam bem dependências de curto prazo, mas assumem que o estado atual depende apenas do estado anterior e que a próxima observação depende apenas do estado atual, o que restringe a modelagem de contextos longos e de interações complexas. Além disso, a necessidade de dados rotulados eleva o custo e o tempo de treinamento, e o modelo não é a melhor escolha para geração livre de texto longo e coerente, como nos LLMs atuais.

**Pontos de atenção**  
- O HMM é um avanço em relação aos bigramas, mas ainda é um modelo linear e com capacidade limitada para capturar dependências longas.  
- A hipótese de Markov simplifica a modelagem: o próximo estado depende apenas do estado anterior, e a observação depende apenas do estado atual.  
- Estados ocultos não são observáveis diretamente; é preciso inferi-los a partir das observações.  
- É importante distinguir claramente entre:
  - **estados ocultos**;
  - **observações**;
  - **matriz de transição**;
  - **matriz de emissão**.  
- O algoritmo **forward-backward** serve para calcular a probabilidade da sequência observada, não para descobrir diretamente a melhor sequência de estados.  
- O algoritmo **Viterbi** é o responsável por encontrar a sequência de estados ocultos mais provável.  
- O **Baum-Welch/EM** é usado para ajuste de parâmetros, com base nos dados observados.  
- HMMs funcionam bem em problemas com estrutura sequencial probabilística clara, como fala, categorias gramaticais e DNA.  
- A rotulagem de dados é cara e demorada, o que impacta o uso prático do modelo em tarefas supervisionadas.  
- Para geração de texto longo e coerente, HMMs não são a melhor opção, pois tendem a perder coerência em contextos extensos.  
- Em linguagem natural, a limitação principal é a dificuldade de manter informação contextual distante e retroalimentação entre partes da sequência.