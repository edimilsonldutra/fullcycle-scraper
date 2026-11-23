Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16599)

## Resumo da aula

Parâmetros são os pesos internos do modelo, ajustados durante o treinamento para representar padrões aprendidos. Eles funcionam como a memória adquirida pelo modelo: é neles que ficam codificadas correlações entre palavras, estruturas de texto, código, imagens e outras regularidades dos dados. Quando o modelo reconhece nuances como diferentes sentidos de “go”, essa capacidade vem dos parâmetros, não da janela de contexto. Por isso, parâmetros estão ligados ao que o modelo sabe, e não ao quanto ele consegue ler de uma vez.

Depois que o treinamento termina, o modelo permanece estático em uso normal. Isso significa que os parâmetros não ficam mudando a cada prompt; eles só são alterados em novo treinamento ou ajuste fino. Em inferência, o modelo apenas aplica o que já aprendeu para processar a entrada atual. Essa distinção evita confundir uso do modelo com aprendizado contínuo.

Em termos gerais, mais parâmetros aumentam a capacidade do modelo de representar padrões complexos e capturar mais nuances. Isso pode melhorar a inferência porque o modelo passa a ter mais possibilidades internas para relacionar contexto e prever a próxima saída. Esse ganho, porém, vem com custo maior de memória, treinamento e operação. Mais parâmetros significam mais capacidade potencial, não garantia automática de melhor resultado em qualquer cenário.

Retomando a janela de contexto, ela continua sendo apenas o espaço de tokens disponível em uma chamada, enquanto os parâmetros representam conhecimento aprendido. Essas duas dimensões são independentes: um modelo pode ter muitos parâmetros e pouca janela, ou pouca quantidade de parâmetros e uma janela grande. O exemplo clássico é o GPT-3, com 175 bilhões de parâmetros e apenas 2.048 tokens de contexto. Isso mostra que “saber muito” e “conseguir considerar muito contexto de uma vez” são propriedades diferentes.

Um modelo com muitos parâmetros pode continuar ruim se tiver sido mal treinado. Nesse caso, o sistema apenas terá muitos pesos armazenando padrões inadequados, incompletos ou mal ajustados. O efeito prático é simples: aumentar a escala do modelo não corrige automaticamente problemas de qualidade. Para Prompt Engineering, isso importa porque nem toda limitação percebida na resposta vem do prompt ou da janela; parte pode vir da capacidade aprendida e da qualidade do treinamento.

## Transcrição

00:01

Bom, pessoal, a gente falou aí um pouco sobre custo, latência, a gente falou da janela de contexto, mas também, para a gente relembrar uma outra coisa que é importante, é que você tem que ter em mente que janela de contexto é diferente de número de parâmetros do modelo.

00:18

Isso aqui eu quero passar rapidamente com você, mas é importante você sempre ter em mente, o nosso foco aqui é Prompt Engineering, desenvolvimento e tudo mais, mas somente para você não confundir quando alguém for falar com você, tá? Janela de contexto é o quanto da quantidade de tokens que o modelo consegue trabalhar para fazer o processamento.

00:39

Parâmetros já é outra coisa, tá? Os parâmetros são os pesos. É como se fosse uma memória do modelo que ele foi treinado, ou seja, é onde ele guarda o que ele aprendeu. Então, é como se fosse a memória que o modelo tem, ok? Então, toda vez que eu tenho um modelo, esse modelo, ele é estático, tá? Esse modelo, ele não muda de forma geral, a não ser se ele esteja em treinamento. Agora, tudo aquilo que ele pegou de informação, que ele aprendeu,

01:07

tudo aquilo que ele pode fazer ter uma correlação entre uma coisa e outra, acaba sendo parâmetros, porque, baseado nesses parâmetros, ele consegue fazer todas essas correlações. Então, quando é feito o treinamento do modelo, esses dados, que acabam virando todos esses parâmetros, eles vão ser ali meio que, como posso dizer, entendendo o padrão. Então, toda vez que ele falou go,

01:34

Ele pode entender que é uma linguagem de programação, ou pode ser goal de a pessoa continuar em frente. Então, esses padrões, essas nuances, ele vai entendendo. E quanto maior o número de parâmetros, maior

01:49

é a quantidade de possibilidades que o modelo tem de fazer o quê? Esse tipo de conhecimento. Então, esses parâmetros, no final das contas, armazenam os conhecimentos sobre a linguagem que o modelo vai utilizar, sobre as imagens, sobre código. Quando eu digo linguagem, não é linguagem de programação.

02:08

mas o formato de texto, a forma como ele escreve, a forma como ele trabalha e tudo mais. E, quanto mais parâmetros, isso também vai me ajudar na inferência para gerar uma resposta. Quanto mais possibilidades eu fui treinado, no final das contas, mais opções eu tenho de resposta. E você vai perceber sempre que quando a gente pergunta algo para uma inteligência artificial,

02:31

ela vai fazer a geração para a gente e essa resposta nem sempre é igual. Exatamente porque a correlação entre os dados de parâmetro e as probabilidades que você tem do próximo token, elas podem, cada vez mais, serem a...

02:48

pesadas e utilizadas em conjunto. E por isso que essa parte de parâmetros é importante. Então, somente para ter uma regra bem simples na sua cabeça, a bem grosso modo, a nossa ideia aqui não é entrar nesse ponto de treinamento de modelo, machine learning, deep learning, mas o ponto importante que eu quero que você tenha em mente é

03:10

Normalmente, se você tem mais parâmetros, o modelo tem mais capacidade de aprendizado, ou seja, o modelo consegue capturar mais nuances, textos complexos e etc. Quanto mais parâmetros a gente tem, mais consumo de memória, mais tempo de treinamento e mais custo. Por exemplo, eu gosto de falar bastante do GPT-3 porque é um modelo antigo. E, mesmo sendo um modelo antigo, eu quero que você entenda, olha só essa relação.

03:40

O GPT-3 tem 175 bilhões de parâmetros treinados e a sua janela de contexto era de apenas 2.048 tokens. Por isso que eu estou dizendo, a relação entre o número de parâmetros que um modelo tem

03:56

em comparação à janela de contexto, não é proporcional. Então, não é porque o meu modelo tem ali bilhões, trilhões de parâmetros, que a minha janela de contexto vai ter que ser grande também. Eu posso ter um modelo que tem uma janela de contexto gigante, com poucos parâmetros, tá? Agora, um ponto importante que eu quero deixar claro é que, apesar de

04:18

quanto mais parâmetros eu tiver, melhor pode ser essa performance, os dados de como que eu extraio do meu modelo, não adianta nada o meu modelo ser mal treinado. E aí significa que eu vou ter muitos parâmetros mal treinados e aí a gente vai ter problema, tá? Eu não quero ficar falando muito em treinamento, mas eu só queria deixar esse vídeo registrado para a gente apenas relembrar que

04:43

A janela de contexto é diferente de parâmetros e não é porque eu tenho muitos parâmetros que a minha janela de contexto é maior. Beleza? Então, vamos nessa aí porque a gente tem outros aspectos que a gente tem que lembrar pra gente falar de Prompt Engineering aqui também.

## Resumo IA

**Abreviações**  
- **GPT-3** — *Generative Pre-trained Transformer 3*.

**Resumo**  
A aula reforça a diferença entre janela de contexto e número de parâmetros do modelo, um ponto importante para não confundir capacidade de leitura com conhecimento aprendido. A janela de contexto foi explicada como a quantidade de tokens que o modelo consegue processar em uma chamada, enquanto os parâmetros foram descritos como os pesos internos do modelo, isto é, a “memória” adquirida durante o treinamento, onde ficam armazenados padrões, correlações e nuances aprendidas a partir dos dados. O instrutor destacou que, em uso normal, o modelo é estático e não vai alterando seus parâmetros a cada prompt; eles só mudam em novas etapas de treinamento ou ajuste.  
Também foi explicado que, quanto maior o número de parâmetros, maior tende a ser a capacidade do modelo de capturar relações complexas, textos variados, código e outras regularidades, o que pode melhorar a inferência e a geração de respostas. Porém, esse aumento de capacidade vem acompanhado de maior consumo de memória, maior custo e maior tempo de treinamento. O exemplo do GPT-3 foi usado para ilustrar que um modelo pode ter muitos parâmetros e, ainda assim, uma janela de contexto relativamente pequena: 175 bilhões de parâmetros com 2.048 tokens de contexto. A aula conclui reforçando que essas duas dimensões são independentes e que ter muitos parâmetros não garante qualidade se o modelo tiver sido mal treinado.

**Pontos de atenção**  
- Janela de contexto e número de parâmetros são coisas diferentes e não devem ser confundidas.  
- Janela de contexto é a quantidade de tokens que o modelo consegue processar em uma chamada; não representa conhecimento.  
- Parâmetros são os pesos internos do modelo e representam o que ele aprendeu durante o treinamento.  
- O modelo não “aprende” a cada prompt em uso normal; os parâmetros não mudam durante a inferência.  
- Mais parâmetros podem significar mais capacidade e mais nuances, mas também aumentam custo, memória e tempo de treinamento.  
- Ter muitos parâmetros não garante melhor desempenho automaticamente.  
- Um modelo mal treinado pode ter muitos parâmetros e ainda assim gerar resultados ruins.  
- A relação entre número de parâmetros e janela de contexto não é proporcional; um modelo pode ter muitos parâmetros e pouca janela, ou o contrário.  
- Em Prompt Engineering, nem toda limitação da resposta vem do prompt ou da janela de contexto; parte pode estar na qualidade do treinamento e na capacidade aprendida do modelo.