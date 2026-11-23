Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16376)

## Resumo da aula

Tokens são as unidades que o modelo realmente processa no lugar de palavras inteiras. Essa escolha existe porque linguagem natural é aberta: surgem palavras novas, há erros de escrita, múltiplos idiomas e variações de uso. Em vez de depender de um vocabulário fechado de palavras completas, o modelo trabalha com partes recorrentes de texto, o que reduz a complexidade do vocabulário e aumenta a flexibilidade para lidar com entradas desconhecidas. O resultado final continua sendo linguagem, mas a representação interna é fragmentada.

Tratar cada palavra como unidade básica tornaria o treinamento mais frágil diante de neologismos, grafias incorretas e termos raros. A tokenização resolve isso quebrando palavras em segmentos mais frequentes, de modo que uma palavra nunca vista ainda possa ser interpretada a partir de partes conhecidas. Isso permite generalização melhor entre idiomas, estilos de escrita e variações ortográficas. A entrada e a saída deixam de ser sequências de palavras e passam a ser sequências de tokens.

Byte Pair Encoding, ou BPE, é um esquema de tokenização baseado em frequência de coocorrência entre partes do texto. O processo começa com unidades menores e vai agrupando combinações que aparecem muitas vezes no corpus de treinamento. Quanto mais recorrente for uma sequência, maior a chance de ela virar um token estável; quando a combinação é fraca, os elementos tendem a permanecer separados. Modelos da família GPT usam esse tipo de estratégia para construir seu vocabulário.

Retomando a ideia de quebrar cachorro, o texto pode começar separado em unidades mínimas e depois formar grupos como CA, CH ou OR conforme a incidência observada nos dados. Não existe tamanho fixo para token: ele pode ter uma letra, um pedaço de palavra ou uma palavra inteira. Se uma sequência como cache aparecer com força estatística suficiente, ela pode virar token mesmo sendo apenas parte da palavra original. Já outra palavra, como artificial, pode permanecer inteira se sua ocorrência recorrente justificar isso.

A tokenização não preserva fronteiras linguísticas humanas de forma rígida. Uma palavra curta como sol pode corresponder a um único token, enquanto uma palavra maior como interessante pode ser dividida em dois ou mais tokens. Termos longos, técnicos ou pouco frequentes tendem a ser quebrados em mais partes porque suas subunidades aparecem com mais regularidade do que a palavra completa. Por isso, contar palavras não é uma boa aproximação para contar custo ou contexto em modelos de linguagem.

Em uma sequência como GPT-4 é poderoso, partes muito recorrentes podem se consolidar como tokens independentes, como GPT, 4, é, poder e oso. A lógica não é semântica no sentido humano; ela é estatística e depende do que apareceu repetidamente durante o treinamento. Um fragmento pode virar token mesmo sem “significar” algo isoladamente, desde que seja útil para compor muitas sequências. Isso explica por que o vocabulário do modelo mistura palavras completas, prefixos, sufixos e fragmentos frequentes.

Os tokens não são criados dinamicamente a cada conversa. O vocabulário tokenizado é consolidado durante a fase de treinamento, quando o modelo lê grandes volumes de texto e aprende quais agrupamentos são mais úteis. Depois disso, novas entradas são convertidas usando essa cadeia de tokenização já estabelecida. Retomando os conceitos anteriores de embeddings e atenção, cada token resultante é a unidade que segue para essas etapas do modelo.

Onde antes era conveniente falar em “palavras”, agora a unidade correta é token. Cada token passa por embedding e depois participa do mecanismo de atenção e do cálculo probabilístico de próxima saída, como já foi introduzido anteriormente. Essa troca de unidade altera a forma correta de medir entrada, saída e contexto. Em LLMs, o pipeline opera sobre tokens do início ao fim.

Limites como 8.000 tokens ou 32.000 tokens medem capacidade de contexto em tokens, não em palavras nem em caracteres. Isso importa porque uma mesma frase pode consumir quantidades diferentes de tokens dependendo do idioma, da escolha de palavras e da presença de termos raros. O custo computacional e financeiro também costuma ser calculado dessa forma. Em serviços gerenciados, como provedores de IA e ML, a cobrança normalmente acompanha o volume de tokens processados.

## Transcrição

00:00

Fala galera, beleza? E aí, prontos pra mais uma aula? Vamos falar um pouquinho agora sobre tokens. Lembra que no comecinho dessa conversa, dessas aulas que a gente começou aqui, eu falei pra vocês que ia simplificar ao máximo quando a gente estivesse falando sobre os padrões e como funciona a inteligência artificial por trás dos panos, e que depois eu ia ir complicando um pouquinho essa história. Chegou a hora de começar a complicar um pouco. Então, eu vou começar a explicar pra vocês o que são os tokens.

00:29

Por que que eu vou explicar isso aí agora? Porque na próxima aula, no próximo capítulo, a gente vai começar a falar de LLM. E daí, pra isso, é mais interessante a gente já conhecer como funciona a tokenização de palavras antes da gente entrar no LLM. Então, o que que acontece? Por que que existe o token? Durante todo o curso, eu tava falando com vocês o seguinte... Olha, pra treinamento de uma IA, a gente tem as palavras que entram, a gente tem as palavras que saem, a gente tem...

00:55

toda a discussão ali de como a gente faz a correlação entre palavras e assim por diante, beleza? Então a gente falou muito sobre isso, encadeamento e tal, pra facilitar a vida. Porque no final das contas, por trás dos panos, não é bem assim que a IA pensa. Ela pensa de uma forma um pouco mais quebrada, e eu vou explicar pra vocês. Então, a IA não usa palavra diretamente. Já tem que ficar claro na nossa cabeça. Eu trouxe pra palavras

01:19

porque era a forma mais fácil de explicar naquele momento. Então ela não usa palavras. Diferente da linguagem natural que a gente tem, que é essa que a gente fala, ela pensa um pouquinho diferente. Por quê? Porque a nossa linguagem natural tem muita variável. Imagina o seguinte, na nossa linguagem natural tem novas palavras surgindo, porque a gente inventa a palavra, a gente não consegue fechar, olha, só essas palavras, nunca mais vai ter uma palavra nova, a gente inventa a palavra.

01:44

A gente tem erro que ocorre, por exemplo, tem palavras que eu escrevo errado ou que eu falo errado. Então, isso também é uma variável importante quando a gente está treinando uma máquina. A gente tem muitos idiomas, óbvio que tem várias variações, variações de interpretação e assim por diante. Então, se eu tivesse que usar só palavras para treinar IA, provavelmente ia dar merda.

02:07

Então, a ideia é que a gente consiga simplificar isso para a linguagem da máquina. Então, o processamento não vai usar palavras inteiras, nem vai usar o que a gente conhece como palavra. Ele tem como se fosse o seu vocabulário próprio. E é um pouquinho diferente do que a gente está acostumado. Mas, no final das contas, chega no mesmo lugar, tá bom? Então, quando a gente está usando o Token,

02:29

A gente diminui o vocabulário total que a gente vai ter, fica mais fácil de entender quais são as entradas que vão chegar. A gente trabalha com palavras desconhecidas, mas quebrando elas em palavras mais familiares. Então, ele faz uma quebra de palavras para fazer esse entendimento e a gente ganha muita facilidade e flexibilidade ali para lidar com qualquer tipo de língua ou com estilo de escrita diferente, caso você erre inclusive. Então, aqui você ganha algumas coisas utilizando tokens.

02:55

E o que que é um token na prática? Um token na prática, ele vai ser uma forma de reorganização de letras ali. Então vamos lá, o que que a gente faz? Imagina, eu vou dar um exemplo de tokenização, porque tem vários exemplos, tá? Então eu vou dar um exemplo pra vocês que se chama o Byte Pair Encoding. Esse Byte Pair Encoding é o que é usado pelo chat GPT, tá bom? GPT-3, GPT-4 e esses assim por diante. Acho que o 3.5 e o 4 usam o Byte Pair Encoding.

03:24

O que que ele faz? Imagina um texto aqui, uma palavra, cachorro. Em vez dele pensar em cachorro, possivelmente ele vai quebrar em cache e orro. Isso poderia ser um token, cache e orro. Imagina que ele separou isso em duas coisas. Ou ele podia também ter cachorro como token. E eu já vou explicar isso pra vocês o porquê. Agora vamos colocar duas palavras, inteligência artificial. Eu podia ter, por exemplo, intelig

03:53

ência e depois artificial tá não tá fazendo muito sentido mas já vai fazer eu garanto pra vocês agora vou dar outro exemplo o Chat GPT é poderoso gpt 4 é poderoso gpt traço

04:10

são dois tokens, quatro, três tokens, é quatro tokens, poder, outro token e uso outro token. Vou usar este exemplo para explicar como funciona por trás, tá gente? E ainda de forma abrangente, eu não vou explicar o detalhe do detalhe, mas só para vocês entenderem como o cálculo é feito.

04:31

imagina o seguinte, a máquina normalmente está a hora pro byte então a gente está falando de letras então vamos dar um exemplo do cachorro inicialmente depois eu vou entrar nesse do chip t4 que ele é mais fácil de explicar então imagina que no cachorro eu vou quebrar c a c h o r r o beleza separei ele em oito

04:51

bytes, aqui no nosso caso. Então, eu quebrei ele em oito letrinhas. Primeiro ele faz isso. Então, a primeira ideia dessa máquina é fazer isso. Depois ela faz o que? Quais são as letras que se agrupam? Então, ela começa a fazer um trabalho por trás ali de quais letras deveriam se agrupar. Por exemplo, CA, CH, OR. E ela vai vendo quais as letras que se agrupam. Como que ela faz isso? Com base em incidência. Então, quando você está treinando,

05:18

a linguagem dessa máquina, ela vai entendendo e interpretando isso com base em quantas vezes essas combinações acontecem. Quanto mais ela ver CA junto, mais ela vai deixar isso como um token forte. Quanto menos ela ver CA junto, mais ela vai deixar como um token forte, ou seja, o C fica sozinho e o A fica sozinho.

05:37

beleza então vamos continuar aqui imagina que eu fui lá e coloquei então as oito letras separadinhas e eu fui juntando isso pela sua força não significa que tem que ser de duas letras nem de uma letra nem de quatro letras nem nada disso tem tokens que são mais fortes que podem ser um pouco maiores tá bom

05:58

e tem tokens que podem ser palavras, por exemplo, e tem tokens que vão ser conjuntinhos. Então, C-A-C-H de cachorro, CACHE, pode ser um token. Mas em compensação, artificial também pode ser um token. Tá vendo que são diferentes tamanhos e diferentes... uma palavra e outra meia palavra? Por que que acontece isso? Porque se você tiver mais força em CACHE,

06:21

do que em cachorro, cache vai ficar virando um token e cachorro não, entendeu? Então ele faz essa separação, vou explicar melhor com gpt

06:32

GPT-4 é poderoso. Então vamos lá. GPT-4 é poderoso. Se eu estiver trabalhando este conjunto, GPT provavelmente vai aparecer várias vezes, certo? Porque a gente fala muito sobre isso. Então quando eu estou ali digitando e falando com a IA, vai aparecer várias vezes GPT. Então a gente sabe que GPT normalmente vem junto. Agora,

06:53

Quando eu falo ifing também, ifing normalmente não vem junto de nada, certo? Ifing é uma parte que pode estar em qualquer texto, é difícil correlacionar ele com outras coisas. Então, nesse cenário, possivelmente o GPT vai ser um token, o ifing vai ser um token, porque ele não vai ter nenhuma ligação forte com outra cadeia. 4 vai ser outro token, porque 4 é número mais difícil de você conectar também.

07:17

E, poxa, a incidência de E sozinho é muito grande. O E em palavras é menor do que o E sozinho no português. Então, você vai ter o E muito forte, possivelmente ele vai ser um token. Poder pode ser um token também. E o uso pode ser outro token nesse cenário. Então, tá vendo que eu tô colocando tudo como pode ser? Porque na hora que você treina a máquina, que você entende como é que vai sair isso da outra ponta. Na verdade, você talvez nem entenda. Ela vai conseguir montar isso.

07:43

E daí, aqui é importante também dizer, isso não acontece quando você está conversando. Os tokens já foram formados. Quando você está treinando a máquina, ou seja, quando o chat GPT foi montado, criado e organizado, quando foi criada a linguagem de conversação dele, para ele entender o que é uma linguagem, ele ficou lendo vários textos ali. Vários textos e formando tokens. E daí, com essa formação de token, ele começou a ter a sua cadeia de tokenização. Então, é mais ou menos assim que funciona.

08:13

Espero que vocês tenham entendido, tentei ser o mais prático possível aqui, o mais didático, mas é meio chatinho, não é bem uma palavra, como eu disse, pode ser pedaços de palavra, pode ser uma letra ou pode ser uma palavra inteira. Então quando a gente está falando dessa tokenização, ela pode ser então, por exemplo, um token como SOL, sendo uma palavra, VOCÊ pode ser uma palavra de um token,

08:35

mas em compensação você pode ter tokens maiores, por exemplo, você pode ter palavras com dois tokens, então interessante é uma palavra maior e que possivelmente vai ter quebra de token por ter trechos que são mais fortes como eu expliquei anteriormente, então você pode ter uma palavra como interessante, naturalmente, indelicavelmente, coisas desse jeito que vão virar

09:01

palavras com mais de um token então pode ser dois tokens pode até ter até eu já vi palavras com cinco tokens depende de quando você tá falando do que você tá falando se for um termo muito complexo muito grande ou muito técnico normalmente vai virar um número maior de token mas a maior incidência vai ser de dois três e um token tá bom então

09:24

No próximo capítulo que a gente vai conversar agora, a gente vai começar a entrar nas LLMs, que é super interessante também. Então, é importante a gente começar a assimilar o que é Token, porque vai ajudar a gente nos próximos capítulos e aprofundar um pouco mais também no nosso conhecimento aqui, tá? Então, a entrada e a saída do modelo, elas vão ser sempre sequências de Tokens e não de palavras, como a gente vinha falando até então. A gente também vai ter cada Token desse passando por um embedding.

09:48

Então, vai ter também ele passando pelo módulo de atenção e pelo cálculo de probabilidade também, como a gente falou anteriormente. Então, tudo aquilo que eu expliquei, token no lugar de palavra, tá bom? O custo computacional e a limitação de contexto também fica mais organizado quando a gente está falando de token. Então, por exemplo, quando a gente está trabalhando com token, um exemplo, 8.000 tokens ou 32.000 tokens são medidos em número de token.

10:19

e não em número de palavras ou caracteres. Então, quando você estiver fazendo, por exemplo... Por que eu estou contando isso? Imagine o seguinte... Eu vou fazer o treinamento de uma máquina e eu faço uma requisição dentro de algum serviço, por exemplo, da AWS, de um Bedrock da vida. Estou treinando ele ou estou treinando algum outro serviço da AWS, ou de qualquer outro provedor de IA, de ML já preparado.

10:40

normalmente ele vai cobrar por token. Então, o número de tokens é o que vai fazer a cobrança daquele serviço. Então, quando a gente estiver falando lá para frente também, a gente não vai estar falando sobre palavras para fazer cobrança de serviço ou para fazer organização de estratégia de criação da sua própria IA. Você vai trabalhar por token, vai cobrar por token, porque o processamento é em cima de um token.

11:03

Beleza? Então dado tudo isso, agora que a gente já falou de todos esses assuntos, a gente começa a aprofundar em LLM na próxima aula. Até já, já!

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **GPT** — *Generative Pre-trained Transformer*  
- **BPE** — *Byte Pair Encoding*  
- **AWS** — *Amazon Web Services*  
- **ML** — *Machine Learning* (Aprendizado de Máquina)  
- **Bedrock** — serviço gerenciado de IA da AWS para uso de modelos generativos  

**Resumo**  
A aula apresentou o conceito de tokens como a unidade real de processamento usada pelos modelos de linguagem, em vez de palavras inteiras. O instrutor explicou que isso é necessário porque a linguagem natural é aberta e variável, com surgimento de novas palavras, erros de escrita, múltiplos idiomas e estilos diferentes, o que tornaria o uso de um vocabulário fechado baseado apenas em palavras muito frágil. Com tokens, o texto é fragmentado em partes recorrentes, permitindo maior flexibilidade e melhor generalização para entradas desconhecidas.

Em seguida, foi introduzida a ideia de tokenização e o esquema Byte Pair Encoding (BPE), usado em modelos da família GPT. O funcionamento foi descrito de forma intuitiva: o texto é inicialmente quebrado em unidades mínimas e, com base na frequência de coocorrência no corpus de treinamento, certas combinações passam a formar tokens estáveis. Assim, um token pode ser uma letra, um pedaço de palavra ou até uma palavra inteira, dependendo da força estatística daquele agrupamento. Foram usados exemplos como “cachorro”, “inteligência artificial” e “GPT-4 é poderoso” para mostrar que diferentes fragmentos podem virar tokens distintos, e que isso não segue fronteiras linguísticas humanas rígidas.

O instrutor também destacou que esses tokens não são criados dinamicamente a cada conversa: eles são definidos durante o treinamento, quando o modelo aprende quais agrupamentos são mais úteis. Depois disso, toda nova entrada é convertida segundo essa tokenização já consolidada. A partir daí, os tokens seguem o pipeline do modelo, passando por embedding, atenção e cálculo probabilístico da próxima saída. Por fim, foi reforçado que limites de contexto e cobrança de serviços de IA são medidos em tokens, e não em palavras ou caracteres, o que torna essa unidade fundamental para entender custo, capacidade e uso de LLMs.

**Pontos de atenção**  
- Não tratar palavras como unidade básica do modelo: em LLMs, a unidade correta é o token.  
- Token não tem tamanho fixo: pode ser letra, pedaço de palavra, palavra inteira ou combinação frequente.  
- A lógica de criação de tokens é estatística, não semântica; um fragmento pode virar token mesmo sem “significar” algo isoladamente.  
- Palavras raras, técnicas, longas ou com grafias incomuns tendem a ser quebradas em mais tokens.  
- Não assumir que contagem de palavras equivale a custo ou contexto; o que importa é a contagem de tokens.  
- Os tokens já vêm definidos do treinamento; eles não são montados “ao vivo” a cada conversa.  
- Ao dimensionar contexto, cobrança ou processamento em serviços de IA, considerar sempre a métrica em tokens.  
- Entender que a tokenização afeta diretamente o pipeline do modelo: entrada, embedding, atenção e saída dependem dessa unidade.