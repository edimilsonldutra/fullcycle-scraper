Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16384)

## Resumo da aula

Masked Language Modeling substitui parte dos tokens de uma sequência por máscaras e treina o modelo para reconstruir os termos ausentes. Diferentemente do CLM, já referenciado anteriormente, a previsão não acontece apenas no próximo token, mas em posições internas da frase. Isso muda o objetivo do treinamento: em vez de continuar uma sequência, o modelo aprende a inferir palavras faltantes a partir do contexto ao redor.

O ponto central do MLM é o uso de contexto bidirecional. Como a palavra mascarada fica no meio da sequência, o modelo pode usar tanto os tokens anteriores quanto os posteriores para fazer a predição. Em uma frase como O [MASK] hoje está muito azul, a inferência depende do que vem antes e depois da máscara, o que favorece tarefas em que entender o sentido global importa mais do que gerar texto token a token.

O mascaramento não cobre a frase inteira, porque o modelo ainda precisa de contexto suficiente para inferir o conteúdo ausente. Um procedimento típico é mascarar cerca de 20% das palavras de forma aleatória durante o pré-treinamento. Esse equilíbrio preserva informação contextual e, ao mesmo tempo, cria dificuldade suficiente para que o modelo aprenda relações semânticas e sintáticas úteis.

Depois de prever os tokens mascarados, o modelo compara sua saída com os valores esperados e ajusta pesos e vieses por backpropagation. A mecânica de otimização é a mesma já usada em outras redes neurais profundas; o que muda aqui é a tarefa de treinamento. O sinal de erro vem da diferença entre a palavra prevista e a palavra original escondida pela máscara.

Retomando a distinção entre modelos voltados a continuação de sequência e modelos voltados a inferência contextual, o MLM tende a ser melhor em compreensão de texto do que em geração livre. Ele aprende a detectar pistas distribuídas ao longo da frase e a reconstruir significado mesmo com partes faltando. Isso o torna especialmente adequado para classificação, busca semântica e outras tarefas em que interpretar contexto é mais importante do que produzir uma resposta longa token por token.

Gerar texto fluentemente exige modelar a dependência causal entre os tokens já produzidos e o próximo token a ser emitido. Como o MLM foi treinado para preencher lacunas com acesso aos dois lados da sequência, seu objetivo não coincide com o fluxo natural de geração autoregressiva. Por isso, arquiteturas como BERT, que usam MLM, se destacam em entendimento de linguagem, mas não são a escolha natural para chatbots gerativos.

Uma boa intuição é pensar em leitura seletiva de documentos. Ao procurar textos sobre um assunto, o leitor costuma bater o olho em palavras-chave espalhadas no meio do conteúdo para decidir rapidamente se aquele documento trata do tema desejado. O MLM aprende um comportamento análogo: usa fragmentos contextuais distribuídos na sequência para inferir significado e identificar de que assunto o texto trata.

Tanto o CLM quanto o MLM se encaixam em pré-treinamento sem supervisão externa, ou unsupervised, porque o próprio texto fornece o alvo de aprendizado. No CLM, remove-se o próximo token esperado; no MLM, escondem-se alguns tokens internos com máscaras. Em ambos os casos, não é necessário um anotador humano rotulando exemplos manualmente, porque o corpus já contém a informação que o modelo precisa para aprender.

## Transcrição

00:00

Bom pessoal, agora que eu já expliquei pra vocês como funciona a CLM, eu vou falar de uma outra. Ela vai ser muito mais simples e muito mais rápida, então essa aula vai ser super curtinha. Porque como eu já expliquei a CLM, elas são parecidas, só mudam uma estratégia. Então eu não preciso te explicar tudo que eu acabei de te explicar. Vamos lá, a próxima que eu tenho pra te falar é a MLM, que é a Masked Language Modeling. Essa MLM, ela vai ter ali um modelo que ele faz uma coisa diferente.

00:29

Em vez dele olhar da esquerda para a direita e tentar entender qual a próxima palavra que ele vai gerar, ele vai fazer o seguinte, ele vai olhar bidirecionalmente, beleza? Então ele não está olhando mais só para frente, ele consegue olhar para trás e para frente. E aqui olhando bidirecionalmente, como é que a gente faz isso? A gente faz uma máscara faltando palavras no meio, não só no final.

00:56

E daí com isso ele vai precisar preencher as lacunas. Ele não vai olhar só... Olha... O céu está azul. O céu hoje está cinza. Você, por exemplo, vai colocar... O céu... Não põe está? Hoje... Não, perdão. Eu comi nas frases aqui. Hoje... O céu hoje está muito azul. Precisa ser um pouquinho maior para conseguir fazer o exemplo. Hoje eu ia fazer besteira. O céu hoje está muito azul. Você pode colocar, então, por exemplo... O... Máscara...

01:26

Hoje está muito azul. Tá no meio. Ou o máscara hoje está máscara azul. Um exemplo. Você pode colocar ele desta forma. Então a máscara ela vem no meio do texto. Então essa informação mascarada no meio faz com que ele olhe para ambos os lados. E olhando para ambos os lados é totalmente diferente do que a gente tinha falado do outro modelo. Tá vendo que o outro modelo ele tá calculando só pra frente? Esse modelo ele tem um modelo de cálculo bidirecional. Que vai ajudar ele a pensar um pouquinho diferente, tá bom?

01:56

Então, um cara que faz isso, o BERT, por exemplo, e qual que é a ideia que a gente faz aqui? Nessa ideia de mascaramento, 20% das palavras eu vou mascarar. Eu não vou mascarar tudo. Então, por exemplo, o exemplo que eu dei aqui pra vocês foi um exemplo hipotético. Eu não vou mascarar 50% da frase, pelo amor de Deus. Eu mascaro ali 20% das palavras aleatoriamente durante o treinamento e deixo ela ir atrás disso.

02:23

e depois você faz a coisa muito parecida, você coloca qual era o esperado e deixa ela processar, depois que ela processa ela vai bater um com o outro e vai fazer a sua organização de pesos e vieses e com isso ela vai fazer um peg backpropagation e melhorar a sua inteligência, beleza? Qual que é o benefício desse modelo?

02:43

Por ele usar o contexto bidirecional, ele vai considerar tanto que vem antes do que vem depois. E depois disso, ele vai ser ótimo pra, por exemplo, compreensão de texto. Ele tem muito mais facilidade de entender o que tá vindo e não tão bom pra geração de texto. Ele não é uma coisa muito de geração. Ele é ótimo pra entender contexto.

03:03

porque ele consegue pegar coisas faltando e entender onde você quer chegar com aquilo. É muito mais difícil para ele gerar uma conversa, porque a conversa tem sim relação da palavra anterior muito mais forte do que fechar lacunas. Você não vai começar uma conversa quando a gente está pensando em estruturar uma frase, pensando em palavras e depois em tampar essas palavras. É igual para o modelo de Machine Learning. Então, ali ele está olhando

03:27

como que ele vai fazer esta atividade de formas diferentes. Uma delas é, eu vou fazer só linear para frente e vou começar a construir frases. Isso é o jeito como a gente pensa para a construção de frases. Outra coisa é como que eu consigo interpretar um texto. Então, se eu falasse para você, olha, busca para mim aí documentos sobre tal assunto. Possivelmente o seu olho, na hora que você estivesse olhando, ia bater. Putz, é...

03:50

algumas palavras-chave ali no meio do documento pra saber se aquilo ali é o assunto. Aí depois você lê com calma e fala, putz, é esse assunto mesmo, não é assim que a gente faz? Então é muito parecido com isso. Eu tô tentando trazer de um jeito que facilite a nossa compreensão aqui pro nosso dia-a-dia. Então é mais ou menos isso, tá? Ele vai pegar frases, lacunas, fechou as lacunas, com base nesse fechamento de lacunas, ele consegue compreender se ele tá falando de assunto A, assunto B e assim por diante. Então é o MLM e ele é muito bom pra isso, tá bom?

04:18

Esse cara, ele é sem supervisão e ele consegue dentro do próprio texto, esses dois caras na verdade, quando a gente tá falando, ele é um treinamento sem supervisão, você não precisa ter alguém lá supervisionando eles. Dentro do próprio texto, você consegue preparar ele pra realizar essa tarefa. Então no CLM você vai remover a última palavra e deixar que o modelo faça a previsão.

04:41

E no MLM você vai colocar uma máscara que vai tampar algumas e deixar aquele adivinha. Então aqui você não precisa de um rótulo externo para ambos os modelos e nem você precisa de alguma pessoa ali acompanhando, você pode deixar ele rodando. E o processo de aprendizado aqui então ele é auto-organizado, ele não precisa ser supervisionado. Então quando você estiver olhando sobre esses carinhas eles vão aparecer normalmente com o nome unsupervised, que significa que ele não é supervisionado por um humano, ele consegue tocar a vida sozinho.

05:09

Beleza? Esses são os dois principais modelos que eu tinha pra combinar com vocês pra explicar sobre o pré-treinamento. Já já a gente volta pra falar de Fine Tuning. Um abraço!

## Resumo IA

**Abreviações**  
- **MLM**: *Masked Language Modeling* (modelagem de linguagem mascarada)  
- **CLM**: *Causal Language Modeling* (modelagem causal de linguagem)  
- **BERT**: *Bidirectional Encoder Representations from Transformers*  
- **ML**: *Machine Learning* (aprendizado de máquina)  
- **unsupervised**: sem supervisão

**Resumo**  
A aula apresentou o conceito de *Masked Language Modeling* (MLM) como uma estratégia de pré-treinamento em que parte dos tokens de uma sequência é substituída por máscaras, e o modelo aprende a reconstruir as palavras ausentes. Em contraste com o CLM, que prevê apenas o próximo token em ordem linear, o MLM trabalha com contexto bidirecional, isto é, considera tanto os tokens anteriores quanto os posteriores à lacuna para inferir o conteúdo faltante. O instrutor explicou que esse método é útil quando o objetivo principal é compreender o sentido global do texto, e não gerar sequência token a token.  
Foi descrito o fluxo típico de treinamento: mascarar uma porcentagem das palavras — em torno de 20% aleatoriamente —, deixar o modelo prever os termos ocultos, comparar a saída com o valor esperado e ajustar pesos e vieses por backpropagation. Também foi destacado que esse processo é auto-supervisionado/sem supervisão externa, pois o próprio texto fornece o alvo de aprendizado, sem necessidade de rótulos humanos. O exemplo citado foi o BERT, um modelo que usa MLM e se destaca em tarefas de compreensão de linguagem, como classificação e busca semântica, mas não é a escolha natural para geração de texto ou chatbots, já que sua dinâmica de treinamento não coincide com o fluxo autoregressivo usado na produção de texto fluente.

**Pontos de atenção**  
- O MLM não é um modelo de geração autoregressiva; ele é mais adequado para compreensão de texto do que para criação de respostas longas.  
- O mascaramento não deve cobrir toda a frase: a ideia é ocultar uma parte pequena da sequência, preservando contexto suficiente para inferência.  
- A taxa de mascaramento mencionada na aula foi de cerca de 20% das palavras, escolhidas aleatoriamente durante o pré-treinamento.  
- O modelo depende de contexto bidirecional; por isso, a posição da máscara no meio da sequência é essencial para que ele use ambos os lados da frase.  
- A tarefa de treinamento muda, mas a mecânica de otimização continua a mesma: previsão, cálculo do erro e ajuste de parâmetros por backpropagation.  
- MLM e CLM são ambos formas de pré-treinamento sem supervisão externa, então não há rótulo humano separado para cada exemplo.  
- Para tarefas de interpretação de linguagem, classificação e recuperação semântica, o MLM tende a performar melhor do que modelos voltados à continuação de sequência.  
- Para chatbots e geração livre de texto, arquiteturas treinadas de forma autoregressiva são mais apropriadas do que modelos treinados com MLM.