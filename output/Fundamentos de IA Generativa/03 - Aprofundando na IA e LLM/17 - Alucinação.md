Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16388)

## Resumo da aula

Alucinação e factualidade são problemas próximos, mas não idênticos. O ponto central é que a LLM produz respostas linguisticamente plausíveis sem necessariamente estar ancorada em fatos corretos. Como o modelo foi pré-treinado para prever tokens e não para garantir verdade factual, ele pode gerar saídas convincentes mesmo quando o conteúdo está errado. Isso torna perigosa a suposição de que “se parece certo, então está certo”.

Retomando o pré-treinamento por previsão do próximo token, a LLM opera por composição probabilística de sequências, não por compreensão semântica equivalente à humana. Ela transforma texto em representações numéricas e estima quais tokens têm maior probabilidade de aparecer em seguida. Por isso, a mesma mecânica usada para responder sobre física quântica também é usada para responder sobre bolo de cenoura: o mecanismo é textual, não uma checagem interna de verdade. O resultado é uma resposta fluente que pode soar correta sem ser.

Alucinação factual ocorre quando o modelo afirma algo objetivamente incorreto como se fosse verdadeiro. Um exemplo é dizer que Marie Curie ganhou três prêmios Nobel, quando na realidade ganhou dois. Esse tipo de erro é especialmente perigoso porque costuma aparecer em frases bem escritas e plausíveis, o que reduz a chance de o usuário suspeitar do problema. Em contextos triviais o impacto pode ser pequeno, mas em medicina, direito ou engenharia o erro pode ser crítico.

O modelo também pode inventar referências, artigos, frases atribuídas a pessoas conhecidas ou fontes que nunca existiram. Isso acontece quando ele completa o padrão esperado de uma resposta com elementos que parecem compatíveis com o pedido, mas não foram verificados factualmente. Pedidos enviesados ou indutivos, como solicitar artigos que “comprovem” uma premissa falsa, aumentam a chance de o modelo fabricar citações inexistentes. Sempre que a resposta depender de autoridade externa, a fonte precisa ser validada fora da LLM.

Alucinação estrutural aparece quando a saída tem forma técnica correta, mas conteúdo inválido. Isso inclui fórmulas matemáticas inexistentes, instruções erradas e código que compila mal, usa APIs incorretas ou referencia elementos que não existem. Retomando o uso de IA para desenvolvimento, isso exige revisão humana efetiva: trate a geração como apoio de pair programming, não como substituto de validação. A fluidez sintática do código não garante correção lógica nem aderência ao ambiente real.

Na alucinação contextual, a resposta começa coerente e se desvia ao longo da geração. Esse desvio tende a aumentar em interações longas, quando o modelo perde consistência com premissas estabelecidas no início e passa a introduzir trechos incompatíveis com o próprio contexto. O mesmo padrão pode aparecer em texto e imagem: a geração começa alinhada ao pedido e degrada no final. O problema não é apenas um fato isolado errado, mas a quebra progressiva do raciocínio local.

A alucinação surge com mais frequência quando falta conhecimento específico no treinamento, quando a pergunta exige inferências que o modelo não consegue sustentar ou quando o prompt induz o preenchimento de lacunas com suposições. Como o modelo tem uma “intuição estatística” sobre o que deveria vir a seguir, ele tende a completar padrões mesmo sem base factual suficiente. Além disso, modelos ajustados para interação natural podem preferir responder de forma convincente em vez de admitir incerteza. Isso aumenta a taxa de respostas plausíveis, porém falsas.

Prompts diretos, específicos e com exemplos do formato esperado reduzem espaço para preenchimento especulativo. Em tarefas técnicas, a saída deve passar por verificação humana, especialmente quando envolve código, cálculo, decisão médica, jurídica ou qualquer resposta de alto impacto. Se o usuário não domina o assunto, não deve reutilizar a resposta como se fosse conhecimento validado. LLM é útil como acelerador de trabalho, mas não substitui checagem factual nem julgamento especializado.

O dano mais imediato da alucinação é operacional: decisões podem ser tomadas com base em informação falsa. O dano sistêmico é a erosão de confiança, porque usuários que encontram erros recorrentes passam a desconfiar do modelo mesmo em tarefas onde ele seria útil. Como não é viável validar manualmente cada resposta em fluxos rápidos, o uso responsável depende de selecionar bem os casos de uso e aplicar validação proporcional ao risco. Quanto maior a criticidade do domínio, menor deve ser a tolerância a saídas não verificadas.

## Transcrição

00:00

Fala galera, beleza? Queria abordar agora com vocês um tema super importante que a gente tem para trabalhar. Então vamos lá! O que a gente já falou? A gente falou como nasceu a IA, como que ela foi evoluindo, passamos lá pelos bigramas, passamos pela evolução das redes neurais, a gente falou de tudo sobre a evolução dessa bagaça. Quais foram os problemas que ela foi achando no meio do caminho, o processamento linear, o processamento

00:30

é único sem conseguir paralelizar qual era o estouro de de gradiente a gente foi falando de tudo que tinha possível imaginável depois a gente foi lá falou de fine tuning falou de tudo que a gente faz para treinar para criar uma IA e depois para treinar uma IA beleza

00:47

Então acho que aqui a gente já conseguiu explicar bastante do funcionamento principal dessa bagaça. Então eu quis trazer pra vocês o primeiro capítulo que é de onde vem, como surge, como evolui, como essa coisa cresce e vira o que a gente conheceu e depois como eu treino ela e como que eu consigo chegar nos modelos que a gente tem atuais de treinamento pra utilização no dia a dia. Mas antes da gente ir pro próximo capítulo, eu queria aprofundar sobre os desafios que ela traz.

01:16

Então, quando a gente fala de IA, de LLM, a gente tem alguns desafios que vão estar presentes aqui no nosso dia a dia. O primeiro deles que eu queria trazer para vocês, eu queria, na verdade, começar pelo desafio que está mais perto do assunto que a gente vem falando até agora, que é da arquitetura, estruturação e assim por diante.

01:35

Esse primeiro desafio não é o mais importante, nem o mais relevante. Ele é o que está mais perto da conversa que a gente vem falando. Depois eu vou falar dos demais desafios, que eles estão um pouco mais distantes dessa conversa. Então vamos partir desse primeiro.

01:49

Ele, na verdade, é quebrado em dois. A gente vai falar de alucinação. Mas quando a gente fala de alucinação, eu já falei algumas vezes aqui, a galera tende a juntar tudo num bololo só. Então, quando a gente tá falando de alucinação, a gente fala, na verdade, de dois temas. Alucinação e factualidade. São coisas diferentes, mas que elas estão muito próximas. Elas são bem parecidas.

02:10

Para falar de alucinação a gente tem que primeiro começar a entender como que a LLM ela pensa no final das contas. E se pensa vamos deixar entre aspas. A LLM ela tem um pensamento um pouco diferente como a gente veio falando até agora. Mas deixa eu traduzir isso para vocês.

02:29

A LLM é mestre em fluência textual, ela é mestre em falar uma língua, pensa assim, em saber decifrar o que virá pela frente, em prever a fluência textual, se a gente puder falar dessa forma. Então tem um cara que é super interessante da gente olhar, vou até pegar aqui, Miguel Nicolelis, não sei se vocês conhecem, Miguel Nicolelis é... Vou ler...

02:54

lidera um grupo de pesquisadores da área de neurociência na Universidade de Duke, nos Estados Unidos, no campo de fisiologia de órgãos e sistemas. Seu objetivo é integrar o cérebro humano com máquinas.

03:09

Então, esse cara manja muito de neurociência. Ele ganhou o prêmio de neuroplasticidade em 2009 e o prêmio Nobel IEEE 2017. Esse cara manja demais, até onde eu vi aqui.

03:27

Ele tem muita coisa publicada, manja bastante, tem uma carreira bastante importante, então ele tem graduação de medicina pela Universidade de São Paulo, doutorado pela Universidade de São Paulo, pós-doutorado pela Universidade de Hahnemann, e ele é professor titular de Neurobiologia e Engenharia Biométrica no Centro de Neurociência lá em Duke, como eu falei pra vocês. É um cara que manja pra caramba!

03:55

Ele tem uma coisa que ele sempre fala, e que de certa forma eu concordo, mas nem tanto. Olha quem sou eu pra concordar com um cara desse aqui que manja de tudo. Ele fala o seguinte, a IA não é nem inteligente, nem artificial. Ele costuma dizer isso. O que eu concordo aqui, e é por isso que eu falei desse cara.

04:16

Quando a gente fala de IA e da LLM que a gente tem falado até agora, a gente tem esse pequeno paradigma. Ela é mestre fluência textual, ou seja, com base no que ela já conhece de texto.

04:29

ela prevê a construção textual que ela tem pela frente. Mas ela não consegue fazer um entendimento do que ela está te falando. Ela desconhece o assunto tratado. Então quando a gente fala que ela é inteligente, a gente leva por base que ela deveria conhecer algo. E na verdade ela não conhece, ela busca essa informação e faz uma construção textual com base no que ela tem de tokens. Ou seja, ela não sabe o que tem ali. Se a gente trocasse todos os tokens dela por um monte de sinal, se você pensar dessa forma,

04:58

chegaria no mesmo lugar. O que ela faz é transformar a linguagem e o número de tokens que ela tem de linguagem em cálculo e dentro desse cálculo pensar em variações em vetores e dentro dos vetores pensar qual é a

05:15

probabilidade de cada novo token aparecer. Se você olhar dessa forma, você tá falando o seguinte, cara, então quando eu pergunto pra ela sobre física quântica, pra ela, ela não tá me respondendo sobre física quântica, a estratégia por trás pra ela me trazer sobre física quântica, seria a mesma se eu tivesse perguntado pra ela como fazer um bolo de cenoura.

05:35

Então, ela é inteligente? Essa é a crítica que ele faz. Ela é inteligente ou ela é capaz de criar texto? Então, se ela é capaz de criar texto, uma criança é capaz de criar texto. Aí, lógico, ela tem uma base de informações extremamente grande que faz com que ela consiga gerar textos que são, na nossa visão, de um conhecimento vasto? Pode ser. Mas seria como se eu falasse que um banco de dados é muito inteligente porque ele tem muita informação. Faz sentido? Bom, essa é a forma de pensamento

06:04

que algumas pessoas tem e que por trás gera este problema de factualidade e alucinação. Como ela não sabe o que ela está te respondendo, ela não sabe mesmo. Não é igual um ser humano que consegue raciocinar sobre o sentido das palavras que sai da nossa boca. Ela não faz isso. Então, como ela não sabe, elas geram respostas

06:25

que são naturais, são bem estruturadas e confiantes.

06:41

Ela mente com categoria, é mais ou menos isso que a gente tá dizendo. Brincadeira da parte, a maior parte das vezes ela acerta no que ela tá falando, mas quando ela erra, ela erra de uma forma que pode até te convencer de que ela tá certa, ou seja, ela é uma boa mentirosa. Então isso pode criar uma ilusão poderosa pra gente que tá usando essa IA.

07:00

Se o texto parece certo, então ele deve estar certo.

07:17

essa suposição de que se parece certo está certo ela é muito perigosa porque nem sempre tá então às vezes essa construção textual pode te convencer mas pode ter errado e daí isso a gente vai chamar de alucinação ou factualidade quando a gente chega em algum desses pontos tá bom

07:35

Então, no final das contas, o que eu estou dizendo aqui é o seguinte, esse modelo não sabe de verdade, ele consegue prever construção textual e não consegue compreender o texto que ele está gerando. É mais ou menos essa diferença, tá bom? Então, ele pode tanto gerar

07:52

tokens errados e te dar uma informação errada, como ele pode inventar informações para tentar te agradar, inclusive, dependendo da forma como ele foi treinado. Ele pode te dar informações plausíveis, mas falsas. Então, o que significa aqui mesmo a alucinação? A alucinação, primeiro, ela vai ser um fenômeno ali onde a LLM vai gerar afirmação que, factualmente, está incorreta.

08:18

Então ela está falando de uma informação que não é embasada em dados factuais. Ela inventou, ela imaginou aquilo ali. Então mesmo sem intenção de errar, ela foi construindo aquela relação de palavras como a gente foi dizendo anteriormente e no meio disso em algum momento ela criou

08:35

algo que não é realidade. Ela só é uma composição probabilística que consegue te dar uma frase bem construída, mas que traz uma mentira junto com ela. Então, essa alucinação factual, por exemplo, vamos dar um exemplo aqui. Um modelo pode chegar pra você e falar o seguinte, a Marie Curie ganhou três prêmios Nobel. Parece fazer sentido, afinal ela ganhou prêmios Nobel.

09:02

Só que na verdade ela ganhou 2 né, ela não ganhou 3. Então se ela trouxer pra você 3 e você não conhece a história da Marie Curie, você possivelmente vai falar, pô faz sentido, eu sei que essa mulher ganhou prêmios Nobel. Nobel, não sei se fala prêmios nobels ou prêmios Nobel, olha o meu português aqui, tem que aprender kaiá depois. Tá aí ó, anotar pra perguntar.

09:21

Bom, ela ganhou dois prêmios e não três. E você pode às vezes entender que isso está correto, porque no final das contas é só um errinho. Então, por exemplo, se você falasse assim pra mim, bom, isso pode gerar algum tipo de impacto

09:37

Relevante? Depende. Se você for usar essa informação pra conversar comigo, conversar com um amigo, etc? Não. Se você for usar essa informação pra fazer uma cirurgia? Possivelmente. Então, tá vendo como começa a ficar complicado? Você não pode usar uma LLM, possivelmente, pra algo que é tão preciso a ponto de não poder ter nenhum tipo de erro, porque ela ainda alucina. Mas isso significa que você não pode usar? Não. Não significa. Significa que tem que tomar um pouquinho de cuidado de vez em quando. Bom, voltando.

10:05

Outra coisa que ela pode fazer também é citar fonte ou falar de citações que não são verdade. Isso aqui eu já vi acontecer, já aconteceu bastante comigo, tá? Você chega pra ela e fala assim, olha, por exemplo, me fala uma frase legal aqui do Steve Jobs. Ela fala a frase, aí você pergunta lá, mas ele disse isso onde? Ah, ele disse isso em tal negócio. Tá, em qual artigo saiu isso? Ela fala, mas na verdade isso não aconteceu não, eu inventei.

10:30

Isso acontece, tá? Ainda mais dependendo de qual modelo de LLM que você tá usando. Algumas alucinam mais, outras alucinam menos. Mas ela traz informações que às vezes não são reais. Ou, por exemplo, quando são informações muito novas, que acabaram de acontecer, ela tem que buscar fonte de dados na internet. Algumas vezes ela dá uma viajada aqui e erra também, tá bom? Então, aqui a gente tá falando de uma alucinação de citação ou fonte, onde ela acha que existe aquela fonte, mas na verdade não existe. Ela citou um case, um artigo, que na verdade não existe.

10:58

Isso também acontece quando eu viro e falo o seguinte, olha... Eu queria que você me desse artigos que corroborem que a Terra é plana. Aí ela vai e coloca lá um monte de artigo corroborando que a Terra é plana, porque eu induzi ela. Na hora que você clica no artigo, ele não existe. Ela faz isso às vezes também, então é importante pensar nisso. Outra coisa que tem é a alucinação estrutural. Ela produz ali então, por exemplo, fórmula matemática que não existe, código que não existe,

11:28

instrução com erro que pode acontecer na hora de criação de codificação principalmente então por isso que por exemplo quando a gente fala pra você usar IA pra codificar você sempre precisa fazer um peer review dela ali fazer um pair programming se a gente parar pra pensar assim pra você ver se o que ela tá produzindo realmente é a realidade ou se ela tá dando uma alucinada

11:48

Tem outra alucinação que é contextual. Essa é mais difícil de pegar, eu acho. Ela começa num contexto correto, coerente, quando vai chegando no final, como eu falei, essa conversa, quanto maior, mais difícil você manter a correlação, ela começa a derivar pra trechos que não vão fazer sentido com o começo do que você gerou. E daí ela perde o raciocínio ali no meio. Isso pode acontecer pra texto, e eu vejo isso acontecendo pra imagem. Pra imagem acontece ainda mais. Ela começa bem,

12:17

criando uma imagem e às vezes ela se perde no finalzinho. Então, como ela faz isso via token na construção, no final ela acaba dando uma alucinadinha. Bom, essas são algumas formas de alucinação. E por que que isso acontece? O modelo, no final das contas, ele tá gerando o texto, então com base em probabilidade, certo? É a sequência de tokens que ele tá recebendo. O que que significa?

12:40

ele não tem uma base de dados factual real pra ele voltar lá e falar, pô, isso é realidade porque eu tenho certeza. Então, essa certeza que o ser humano fala, ele não tem. Ela tem uma intuição estatística. Essa é uma boa forma de explicar. É uma intuição estatística do que deveria vir ali pela frente, ou seja, ela consegue meio que prever quais são as palavras que vão ser interessantes colocar naquele contexto. Então,

13:06

Essas alucinações podem surgir, por exemplo, quando falta algum conhecimento específico no treinamento. Ou quando a pergunta exige, por exemplo, a inferência combinada a alguma coisa que o modelo não aprendeu, quando ele vai precisar inferir. Então, se eu fizer uma pergunta, por exemplo, faça uma inferência sobre a teoria blá blá blá, combinada com a teoria tal tal tal.

13:33

Ela vai ter que imaginar alguma coisa aqui no meio, daí pode virar uma viagem em zona também, isso acontece. Outra coisa que também pode acontecer é quando o prompt leva o modelo a preencher as lacunas que ele não encontra com suposições. Por isso que eu falei um pouco antes pra vocês, que às vezes é melhor você tratar mal a IA. Você só faz a pergunta direto, específico, inclusive quando você puder colocar exemplos do que você espera de resposta. Menos chance de dar uma merda.

14:00

Então às vezes ela dá essas alucinadas também. E o modelo também, no final das contas, o que que acontece? Ele tem um contexto, a maior parte das LLMs, de não só te responder, mas de parecer um humano. Então ele não quer parecer um humano que você ache ele uma porcaria, chatão. E como ele quer criar essa relação, porque ele quer que você continue utilizando este modelo, a chance dele te tratar bem e dele trazer

14:24

essa entrega de uma forma a te convencer, por mais que seja falso, é muito grande. Então, quanto mais direto ao ponto você for, mais ele vai tentar interagir com você da forma como você interage com ele e possivelmente menos chance de erro você tem, tá bom?

14:39

E por que esse problema é um problema crítico, que a gente precisa ficar de olho? De novo, se eu estiver fazendo uma conversa aqui com meu amigo falando sobre quais são as semelhanças entre a Bíblia e o Rei Leão. Pô, estamos viajando, alucinando, criando na nossa cabeça alguma loucura aqui. Não tem problema eu falar besteirona e ele falar besteirona, porque a conversa inteira possivelmente vai ser meio maluca.

15:05

Mas se eu tiver que resolver um problema crítico, se eu precisar fazer um cálculo estrutural de um prédio que não pode cair, se eu precisar fazer isso para contextos médicos, jurídicos, pode alguém ser preso porque eu fiz errado, ou uma resposta onde se for gerada incorretamente, o BO vai ser muito grande.

15:22

Então, isso a gente tem que ficar muito esperto, tá bom? Daí, isso pode gerar o que? A perda de confiança. Quando um usuário, por exemplo, ele cai nesse sentido, ele percebe esses erros, ele começa a ter menos confiança no modelo. E daí, com isso, ele acaba parando de usar e você vai perdendo um pouco desse boom da IA, querendo ou não, e o medo da gente voltar para uma...

15:43

para o inverno da AI, se a gente começa a fazer isso muito. Porque as pessoas vão começar a não confiar e elas vão querer usar. Então, isso é super importante a gente pensar também, porque isso não pode acontecer. E é muito difícil de você validar, porque como a gente tem muita resposta, a gente tem muita troca, é muito rápido e ela é fluente, você não vai conseguir validar tudo que ela falar. Você não vai poder checar tudo olhando o site, etc. Você tem algumas estratégias que a gente usa para fazer isso, mas é muito difícil de você validar tudo que ela manda.

16:11

Por isso que é super importante você, quando for usar algum conteúdo gerado por ela, você ter conhecimento. Não adianta você não ter conhecimento e querer falar de um assunto que você só pegou lá cuspido da IA, ou querer usar aquilo a seu favor pra você, por exemplo, gerar algum trabalho, fazer alguma entrega. Então, por isso que é super importante você ficar esperto nisso, você entender que tem esses desafios pela frente. Já já eu volto pra falar de outro desafio crítico também,

16:38

Mas antes eu queria dar mais um exemplo pra você.

16:43

Imagina que eu chego lá e falo pra essa IA também, ó, quem foi o vencedor do Prêmio Nobel de Física em 2023? E ela pega e fala pra mim assim, ó, o Prêmio Nobel de Física de 2023 foi concedido a Cláudia Miller pelo trabalho que ela fez ali revolucionário em criação da estrutura de prótons aplicada a quântica no clima. Olha que complicado que eu falei.

17:12

Mas, no final das contas, essa estrutura pode fazer você acreditar que foi isso mesmo. Só que olha que engraçado. Primeiro, a Claudia Miller não foi nem indicada. Segundo, ela não estuda isso. Ela estuda nanotecnologia aplicada ao clima.

17:27

Então, olha que doideira, eu inventei uma maluquice que nem sei de próton, que eu tirei da minha cabeça enquanto eu tava falando aqui, até nem sei se soou tão real assim quanto eu deveria, mas olha que doideira, se a IA entregar isso pra você, você vai acreditar, faz essa reflexão antes.

17:43

Antes de eu encerrar essa aula aqui, faça essa reflexão. Se ela bater isso aí pra você, você vai lá validar se é isso mesmo? Deveríamos. Então, é muito importante quando você estiver, então, usando uma LLM, você treinar ela direitinho e quando você estiver usando ali um chat GPT da vida, você validar toda a informação que ele te dá caso você não conheça, não tenha domínio pra você não falar nenhuma besteirona por aí. Beleza? Já já eu volto pra falar de mais um desafio que a gente tem aí pela frente da IA pra gente poder evoluir e usar ela cada vez mais no nosso dia a dia. Fechou? Um abraço.

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **IA** — Inteligência Artificial
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **IEEE** — *Institute of Electrical and Electronics Engineers*
- **Nobel** — Prêmio Nobel

**Resumo**
A aula aborda um dos principais desafios no uso de LLMs: a relação entre alucinação e factualidade. O instrutor explica que a LLM é excelente em produzir fluência textual, pois foi treinada para prever o próximo token com base em padrões probabilísticos, mas isso não significa que ela compreenda o conteúdo ou garanta verdade factual. Assim, a saída pode soar correta, bem estruturada e convincente, mesmo quando contém erros ou invenções. A aula reforça que a LLM trabalha com composição textual e “intuição estatística”, não com validação interna de realidade, o que torna perigosa a suposição de que algo “se parece certo, então está certo”.

Foram apresentados diferentes tipos de alucinação. A alucinação factual ocorre quando o modelo afirma algo objetivamente incorreto, como atribuir três prêmios Nobel a Marie Curie em vez de dois. A alucinação de citação ou fonte acontece quando o modelo inventa artigos, frases atribuídas a pessoas ou referências inexistentes, especialmente quando o prompt induz uma resposta com autoridade externa. A alucinação estrutural aparece quando a forma parece técnica, mas o conteúdo é inválido, como fórmulas falsas, instruções erradas ou código com APIs inexistentes. Já a alucinação contextual ocorre quando a resposta começa coerente e vai se desviando ao longo da geração, perdendo consistência com o contexto inicial, algo que também pode acontecer em texto e imagem.

O instrutor também explica por que essas falhas acontecem: falta de conhecimento específico no treinamento, necessidade de inferências que o modelo não sustenta, prompts que induzem preenchimento especulativo e o fato de muitos modelos serem ajustados para responder de forma convincente e natural, em vez de admitir incerteza. Como consequência, o uso correto exige prompts diretos, específicos e, quando possível, com exemplos do formato esperado. Em tarefas técnicas, a resposta da LLM deve ser tratada como apoio, semelhante a um pair programming, e sempre submetida à revisão humana, principalmente em contextos de código, cálculo, medicina, direito e outros domínios críticos. O fluxo recomendado é usar a LLM como acelerador de trabalho, mas validar externamente qualquer informação importante, especialmente quando o usuário não domina o assunto.

**Pontos de atenção**
- Alucinação e factualidade são problemas próximos, mas não idênticos.
- A LLM gera texto por probabilidade, não por compreensão semântica equivalente à humana.
- Texto fluente e convincente não garante verdade.
- Erros factuais podem parecer pequenos, mas em áreas críticas podem gerar grande impacto.
- A LLM pode inventar fontes, artigos, citações e referências inexistentes.
- Prompts enviesados ou indutivos aumentam a chance de respostas falsas “com autoridade”.
- Em código e tarefas técnicas, a fluidez sintática não garante correção lógica nem compatibilidade com o ambiente real.
- Use revisão humana efetiva em código, cálculos e decisões de alto impacto.
- Em interações longas, a resposta pode perder consistência contextual progressivamente.
- Quanto mais específico e direto o prompt, menor a chance de preenchimento especulativo.
- Fornecer exemplos do formato esperado ajuda a reduzir ambiguidades.
- Não reutilize conteúdo da LLM como verdade validada sem checagem externa, principalmente se você não domina o tema.
- Em domínios críticos, a tolerância a saídas não verificadas deve ser muito baixa.
- A validação completa de tudo o que a LLM produz é impraticável; por isso, a escolha do caso de uso deve considerar o risco.