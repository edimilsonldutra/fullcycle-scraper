Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16383)

## Resumo da aula

Pré-treinamento é a fase em que o modelo aprende a partir de exposição massiva a texto bruto. O objetivo não é ensinar uma tarefa específica, mas fazer o modelo absorver regularidades de linguagem em escala: sintaxe, semântica, estilo e estrutura. Como LLMs já foram apresentados como modelos treinados com grandes corpora, o ponto novo aqui é a lógica operacional dessa etapa: o valor está no volume e na diversidade dos dados. Livros, sites, artigos, código, fóruns e interações na web funcionam como fonte porque ampliam a cobertura de padrões linguísticos que o modelo consegue internalizar.

Dados textuais em larga escala viraram um ativo estratégico porque o pré-treinamento depende diretamente deles. Plataformas com grande volume de interação humana concentram linguagem natural em uso real, o que aumenta a utilidade desses dados para treinar modelos. Quando grande parte da web já foi convertida em tokens e reutilizada em treinamento, a disputa deixa de ser apenas por compute e passa a ser também por acesso a novas fontes de dados. Isso explica por que dados passam a ter valor econômico comparável a infraestrutura.

No pré-treinamento, o modelo não precisa receber explicações humanas sobre cada trecho lido. Em vez de depender de classes como “jurídico”, “médico” ou “código Python”, ele aprende diretamente dos padrões presentes no texto. Isso reduz drasticamente o custo de preparação dos dados e permite escalar o treinamento para bilhões de tokens. A consequência prática é um modelo generalista, que aprende regularidades amplas antes de qualquer especialização posterior por fine-tuning.

Rotular dados é associar exemplos a categorias explícitas para orientar o que o modelo deve aprender. Em classificação de sentimento, por exemplo, frases como “Este produto é ótimo” recebem rótulo positivo, enquanto “O atendimento foi horrível” recebe rótulo negativo. Esse processo ensina a máquina por supervisão, mas exige trabalho manual ou pipelines de anotação, o que encarece a operação. A diferença central para o pré-treinamento moderno é que aqui o modelo aprende sem essa marcação explícita.

O modelo não precisa “saber” se está falando sobre foguetes ou bolos para gerar texto plausível. O que ele aprende é a continuidade estatística e estrutural da linguagem, isto é, quais sequências tendem a ocorrer juntas e em que forma. Isso ajuda a entender por que a expressão “inteligência” em IA é controversa: o sistema pode dominar a forma textual sem possuir entendimento humano do conteúdo. Ainda assim, esse domínio estrutural já é suficiente para produzir respostas fluentemente conversacionais.

Retomando a previsão do próximo token, já conectada à ideia de modelos autoregressivos vista antes, CLM é o mecanismo de treinamento em que o modelo recebe uma sequência e tenta prever o próximo elemento. GPT-2, GPT-3, GPT-4, Llama, Mistral e modelos da família Phi usam essa lógica causal. Se a entrada for “O cachorro latiu ontem”, o treinamento consiste em estimar qual continuação é mais provável. O modelo aprende repetindo esse processo em escala massiva, ajustando seus parâmetros a cada erro.

“Causal” significa que a previsão só pode usar o contexto anterior da sequência. O modelo olha apenas para os tokens à esquerda para prever o próximo token, sem acessar o futuro da frase. Essa restrição é implementada por uma máscara causal, que bloqueia a atenção para posições posteriores. O efeito é alinhar o treinamento com o comportamento de geração real, em que cada novo token depende apenas do que já foi produzido.

Durante o treinamento, o texto completo é tokenizado, mas o modelo recebe apenas uma parte da sequência para fazer a previsão. O token correto fica oculto até o momento da comparação. Se o modelo prever “portão” quando o esperado era “parque”, esse erro vira sinal de ajuste. Esse mecanismo transforma geração em aprendizado iterativo: prever, comparar, medir erro e corrigir parâmetros.

Depois de comparar a saída prevista com o token real, o erro é propagado de volta pela rede por backpropagation. Como LayerNorm, conexões residuais e estabilidade de treinamento já foram discutidos antes, o ponto relevante aqui é a função desse passo dentro do pré-treinamento: redistribuir o erro para ajustar pesos e vieses em toda a arquitetura. Cada atualização torna o modelo um pouco melhor em prever continuações plausíveis. Em escala, esse processo produz a fluência observada em LLMs.

Cross Entropy Loss mede a distância entre a distribuição prevista pelo modelo e a resposta correta. Em vez de avaliar apenas acerto ou erro binário, ela quantifica quão mal calibrada estava a previsão para o próximo token. Esse valor funciona como sinal numérico para otimização, permitindo que o treinamento aproxime gradualmente a distribuição prevista da distribuição desejada. Sem uma função de perda desse tipo, o ajuste dos parâmetros seria muito menos eficiente e muito mais custoso.

## Transcrição

00:00

Fala galera, beleza? Vamos então dar o próximo passo e falar um pouquinho sobre o momento do pré-treinamento? Então até agora o que a gente fez? A gente falou de todo o histórico, de como foi nascendo a IA. Eu contei para vocês cada desafio que foi aparecendo e como a gente foi resolvendo esse desafio.

00:15

Para facilitar o entendimento e vocês entenderem no final como funciona o cérebro dessa IA, como que ela é montada, como é organizada. Para daí sim, a gente entra agora em como ela aprende. Então o ponto principal desta aula é a gente entender como ela aprende no dia a dia.

00:32

E aqui, esse primeiro momento de pré-treinamento, ela aprende com uma enorme exposição a dados, ela precisa de muito texto, muita informação. Por isso aqui que tem uma sacada muito interessante. Quando você olha para as Big Techs,

00:47

Elas têm lutado faz algum tempo pelo domínio das redes sociais. Por quê? Porque isso mostra muito texto e muita interação humana que facilita pra você depois treinar uma máquina de IA, por exemplo. Então, esses dados são riquíssimos.

01:03

Então, aqui ter fonte de dados, de livros, perdão, de sites, de artigos, código, fórum, conversação dentro da web e assim por diante, tudo isso ajuda pra caramba a você conseguir

01:19

treinar uma máquina. E aqui fica um dado importante, se a gente olhar para o momento atual, tudo que tem na web já foi mapeado, já foi jogado como token para as máquinas aprenderem. Então, isso já foi jogado, a maior parte dessa informação já foi utilizada. Então, o dado hoje é um ouro para essas empresas para conseguir treinar, porque a gente tem pouco dado. A gente já usou muito dado, na verdade tem muito dado, mas a gente já usou muito dado para treinar essas IAs.

01:46

Então aqui, o que é o mais interessante nesse momento de pré-treinamento? Essa máquina não precisa mais de rótulo humano, ela não precisa de dado rotulado. Então ela consegue fazer esse treinamento de forma não supervisionada. Ela não precisa saber se ela está lendo um artigo de medicina ou se é uma...

02:06

uma cláusula jurídica, ou se é um código em Python, por exemplo, ou qualquer outro tipo de coisa, da mais diversa possível. Basta que você tenha um texto.

02:17

que ela consegue aprender os padrões linguísticos daquele texto, sintaxe, semântica, estilo de estrutura... E a partir desses dados, ela começa a se treinar para dar o próximo passo e começar a ser conversacional. Então, o que significa no final das contas? Ela não está precisando que você explique para ela tudo o que ela está lendo, ela não importa na verdade para ela o que ela está lendo, importa padrão. Ela começa a procurar padrões textuais e com base nesses padrões, ela cria a sua inteligência de geração de texto.

02:47

Aqui fica uma grande mudança, uma grande paradigma. Quando a gente fala que a IA é inteligência, muita gente fala assim, é uma inteligência que não é inteligente. Tem certo sentido, porque no fim das contas ela nem sabe o que ela está lendo. Ela só está pegando um monte de texto e gerando em uma certa estrutura. Ela sabe muito bem como funciona talvez o português, se a gente parar para pensar, ou como funciona o inglês e assim por diante. Ela consegue entender muito bem como funciona essa estruturação textual.

03:14

mais do que a gente se bobear, que muita gente aqui deve ser ruim de português, vamos ser meio honestos, inclusive eu. Então aqui, essa IA, ela normalmente tem esta capacidade. Ela não sabe se ela está te ensinando a fazer um foguete ou se ela está te ensinando a fazer um bolo. Ela sabe montar frases olhando o padrão textual dela, e por isso que essa forma de pré-treinamento é interessante, porque você está jogando para ela um monte de texto e ela está pegando isso para gerar padrão, beleza?

03:42

E por que é importante você ter dados não rotulados? A gente podia estar explicando pra ela o que ela tá lendo. Isso se chama rotular dados. Mas, quando você tem dados rotulados, você precisa rotular isso manualmente. E lá atrás era isso que acontecia. Só que o custo disso é muito alto. Você pegar um monte de dados e ficar falando, ó, isso aqui é isso, isso aqui é aquilo, é muito alto.

04:01

Então, o cuidado que a gente precisa ter é que com dados não rotulados, a gente consegue escalar o aprendizado para bilhões de tokens. A gente não precisa ter um monte de gente aqui batucando para conseguir gerar informação. Você não precisa enriquecer essa informação, você pode dar essa informação crua para a IA. Então, isso é super importante e é uma grande mudança no modelo de pré-treinamento.

04:25

Então esse modelo ele vai aprender de forma geral, sem precisar limitar ali a uma tarefa específica, por exemplo, a uma atividade específica. Isso vai permitir que você use o modelo depois para uma adaptação de finetuning, que a gente vai falar na sequência. Mas Natan, seu desgraçadinho, o que que é o rótulo?

04:44

Falei aqui, tentei já deixar nas entrelinhas o que é um rótulo, já falei durante o treinamento um pouquinho do que é o rótulo, mas deixa eu explicar pra vocês o que significa rotular um dado. Rotular um dado significa que você vai...

04:59

atribuir uma informação específica, ou seja, um rótulo a um conjunto de dados, para que o modelo de aprendizado depois saiba o que ele deve aprender com cada rótulo, com cada exemplo. Então, imagina que você está pegando os dados e colocando em caixinhas de assuntos, pensa desse jeito, é o melhor jeito de você entender. Então, imagina que você tem, por exemplo, várias frases e você quer

05:23

treinar um modelo para detectar sentimentos. Então, por exemplo, você vai separar as frases em duas caixinhas. Uma caixinha são os positivos e outra são os negativos. Então, você vai detectar sentimentos positivos e negativos. Para isso, você rotulou. Esses daqui têm cunho positivo, estes outros têm cunho negativo. Com isso, deixa eu treinar a minha máquina.

05:45

Mas você vai fazer isso na hora de montar o dado? Você pode, por exemplo, fazer o seguinte... Pegar uma frase do tipo... Este produto é ótimo. Rótulo positivo. Vou dar isso pra máquina pra ela já entender qual é o treinamento dela em cima disso. Outra coisa que eu posso fazer é... Esse produto foi péssimo. Ou o atendimento foi horrível. Rótulo negativo. Então, ela já vai saber que quando ela pegar coisas nesse sentido, é negativo. O que vai acontecer? Possivelmente ela vai pegar...

06:11

os atributos que a gente incluir uma frase por exemplo ótimo é bom é legal e vai entender que isso é positivo ao longo do tempo quando a gente colocar para ela que a gente tem frases como péssimo ruim horrível a gente vai

06:27

entender que esses atributos são negativos. Então você está treinando ela rotulando. Só que pra isso você foi lá na mão, o ser humano foi lá e falou, ó, isso é positivo, isso é negativo, isso é positivo, isso é negativo. Você pode até criar alguma automação pra fazer, mas no final das contas você vai ter que ficar fazendo esse negocinho chato pra caramba. Então quando você está falando de rotulação, você precisa fazer isso. Os pré-treinamentos de hoje em dia não precisam dessa rotulação.

06:49

Você só joga lá os dados e ela vai começar a entender como a coisa funciona com base na estrutura que ela já consegue pegar de texto. Beleza? Então, cada frase, nesse caso que eu contei pra vocês, ela tem um rótulo de sentimento. Eu podia dar outro rótulo pra ela. Podia dar rótulo de várias coisas. Então, cada frase, inclusive, pode ser rotulada diferente dependendo pra o que você quer treinar uma máquina.

07:11

Então, aqui você não precisa rotular. Você consegue deixar a máquina aprender a associar os seus padrões independentemente de rótulo e mais de sintaxe. Ela vai funcionar mais em cima de sintaxe.

07:24

Como que esse modelo ele vai aprender ali? Durante o pré-treinamento a gente tem algumas abordagens, eu vou fechar aqui em duas pra vocês, tá? Uma delas se chama CLM, que é a Causal Language Modeling. Essa CLM ela é usada ali no GPT-2, GPT-3, GPT-4. Normalmente os GPTs estão usando bastante ela. A ideia dela

07:46

é que ela vai pegar uma sequência de palavras e vai aprender a prever a próxima palavra. Então, ela é preditiva. Eu peguei aqui uma sequência de palavras. O cachorro latiu ontem. E daí, essa sequência de palavras, eu vou tentar escolher qual que é a próxima.

08:01

Um cachorro latiu ontem no meu bairro, por exemplo. Então, eu estou tentando entender quais são as próximas palavras que estão chegando. Então, é assim que ela faz. Ela tem as primeiras palavras e vai tentando entender as próximas. É uma orientação parecida com o que tinha no bigrama, que a gente foi evoluindo ao longo do tempo. Então, essa evolução é o que o ChatGPT faz para prever. E com todas aquelas camadas que eu já ensinei para vocês. Óbvio que não faço a comparação que... Então, é tão simples quanto o bigrama. Não!

08:27

Tudo isso super evoluído em cima de tudo aquilo que a gente falou, multiprocessamento, trabalhar em várias layers e assim por diante. Então aqui, neste exemplo de entrada, imagina assim ó... O céu hoje está muito... Eu preciso achar o que ele está muito. Ele pode prever azul ou nublado, por exemplo. E aí a gente vai decidir o que é melhor ao longo do tempo para esse fine-tuning entender se azul ou nublado é o que a gente está procurando ali.

08:55

Tá bom? Tem uma outra coisa super importante que a gente precisa entender, é que essa relação, quando a gente está falando, ela é uma relação causal que a gente fala. O que isso significa? Que ela é uma relação de causa e efeito na sequência. Então, quando a gente está falando lá do modelo, a gente está falando que é causal language modeling, certo? Então, o que é esse causal? Causal significa que

09:23

A próxima palavra tem a intencionalidade das palavras anteriores, ou ela tem a causa sendo criada pelas palavras anteriores. Então, você tem uma relação de causa e efeito numa sequência. Então, qualquer coisa que a gente vai criar vai ter influência direta do que veio antes, tá bom?

09:44

Ou seja, o modelo só pode usar o contexto anterior, a esquerda, para prever o próximo token. Então, ele precisa olhar sempre uma frase e falar o que vem da esquerda para eu prever o próximo token. Então, essa ideia aqui que a gente tem, ela cria então uma máscara causal que a gente fala, ou seja, o modelo só pode olhar para trás, ele nunca olha para frente. E com base nisso, durante o treinamento, o texto a gente vai pegar um texto completo, vai dividir ele em tokens, tá bom?

10:12

Ou seja, os pedaços de palavras que a gente já falou, ou de caracteres, dependendo da situação. E o modelo vai receber uma sequência incompleta, você não vai entregar tudo pra ele. Vou deixar ele pegar uma sequência incompleta. Depois da previsão eu jogo a completa ali. Então ele vai comparar a predição com o token real. Então imagina que ele foi lá e fez a predição. O céu está,

10:38

nublado, o céu está azul, assim por diante. Você vai jogar para ele o céu, está o nublado ou o azul, você não joga, você deixa guardado. Na hora que ele gera esta informação, aí sim você dá para ele a predição

10:55

comparada a real frase e daí ele vai comparar e vai falar opa errei ou não errei e daí com base nisso ele vai ajustar os pesos que ele tem e fazer um backpropagation vai jogar isso de volta para toda a estrutura dele então ele vai sempre linear para frente e depois que ele aprende ele faz uma propagação contrária para conseguir fazer com que toda máquina aprenda sobre aquela informação e ajuste seus pesos e vieses para dentro da inteligência ali beleza esse é um jeito tá

11:24

Então, de novo, vou dar mais um exemplo pra vocês. O cachorro correu para o parque, por exemplo. Então, o que eu quero esperado é parque. Só que ele gerou

11:35

Portão. Quando ele gerou o portão, ele vai entender que isso foi um erro. E este erro vai gerar uma correção de pesos. E nessa correção de pesos, ele vai pegar e propagar pra todo mundo entender, toda sua rede neural entender que ele gerou uma coisa errada e que não é este caminho. Então é outro caminho que ele tem que aprender. É como se fosse uma criança aprendendo de forma muito rudimentar, uma criança aprendendo, fazendo errado, aprendendo que é certo e tomando algum tipo de...

12:03

informação contrária ou sendo avisado que aquele não é o caminho certo. Então, qual que é a função de perda que a gente usa aqui? Porque tem uma função de perda, se você parar para analisar, você tem uma perda relacionada. Normalmente, quando a gente está falando desse tipo de trabalho, você tem uma função de perda chamada Cross Entropy Loss.

12:26

Tá bom? Eu vou explicar pra vocês o que é a cross entropy loss. Segura só um pouquinho. Mas o que ela vai fazer? Ela vai medir quão longe essa distribuição que a gente fez, prevista ali, tá pelo modelo real. Então, isso vai fazer o seguinte, ele vai entender qual token era realmente o próximo e quão longe você tá dele. E daí essa...

12:48

criação de proximidade ou mostrando quão longe você está, o Delta, vai te ajudar a fazer o treinamento de máquina. Deixa eu explicar pra vocês o que é Cross Entropy Loss. Ela é uma função, então, de perda de entropia cruzada, se a gente parar pra pensar.

13:04

É uma função que ela vai pensar, então, o quão distante você está da previsão de um modelo em relação à resposta correta. Então, eu fiz um modelo e eu gerei minha resposta correta. Depois, eu comparo um com o outro. Vai virar cálculo. Lembra que a gente falou dos cálculos? No final das contas, eu vou gerar vetores. Então, eu vou comparar quanto que um vetor está distante do outro. Depois disso,

13:24

eu vou entender se isso está muito distante ou não, para prever o próximo token em um modelo de linguagem. Então, eu estou começando a ver esse delta, para me ajudar a alinhar esse delta, arrumar o delta e chegar mais perto do modelo de linguagem. Se eu não usar um cross entropy loss ou algum estilo, esse é um jeito de fazer

13:47

função de perda. Se você não usar nenhuma função de perda, vai ser muito mais complicado possivelmente treinar essa máquina, vai ser muito mais custoso. Então, essa é uma ideia, uma forma de fazer, tá bom? Então, deixa eu contar pra vocês mais alguns carinhas que usam essa arquitetura. Eu falei dos GPTs, mas não são só os GPTs, de DeepSeek ou também.

14:06

só que de uma forma mais robusta ainda, então eles usam ainda de uma forma mais otimizada porque eles tem menor poder de processamento. A Mistral usa também o Llama, também usa

14:19

em modo causal, dá para você usar também. E daí, isso vai ajudar a gente nesse modelo de treinamento, gerando fluidez e coerência, principalmente quando a gente está falando de textos que são maiores e que a gente está tentando organizar sem categorização e etc. Ou seja, textos generalistas que é o que essas IAs fazem. Então, basicamente pessoal, é isso. Quando a gente está falando de CLM, já já a gente volta para falar de mais uma.

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **LLM** — Large Language Model (Modelo de Linguagem de Grande Porte)  
- **CLM** — Causal Language Modeling (Modelagem de Linguagem Causal)  
- **GPT** — Generative Pre-trained Transformer  
- **Python** — Linguagem de programação Python  
- **Cross Entropy Loss** — Função de perda de entropia cruzada  
- **Big Techs** — Grandes empresas de tecnologia  
- **Web** — World Wide Web  
- **Fine-tuning** — Ajuste fino de um modelo pré-treinado  
- **Backpropagation** — Retropropagação do erro  

**Resumo**  
A aula abordou a etapa de pré-treinamento de modelos de linguagem, explicando que nela o modelo aprende por meio da exposição massiva a texto bruto, sem receber orientação explícita sobre tarefas específicas. O instrutor destacou que o objetivo não é classificar conteúdos em categorias como jurídico, médico ou código, mas sim absorver padrões linguísticos em larga escala, como sintaxe, semântica, estilo e estrutura. Para isso, são usados grandes volumes e variedade de dados, como livros, sites, artigos, código, fóruns e interações na web, que funcionam como fonte rica para internalizar regularidades da linguagem. Também foi enfatizado que dados textuais se tornaram um ativo estratégico, porque a disputa atual não depende apenas de capacidade computacional, mas também de acesso a novas fontes de dados.

Em seguida, foi feita a comparação entre pré-treinamento não supervisionado e dados rotulados. Rotular dados significa associar exemplos a categorias explícitas, como sentimentos positivos e negativos, o que exige trabalho manual ou pipelines de anotação e aumenta o custo operacional. No pré-treinamento moderno, isso não é necessário: o modelo aprende diretamente dos padrões presentes no texto, sem precisar saber o tema específico do conteúdo lido. O foco está em reconhecer continuidades estatísticas e estruturais da linguagem, permitindo que o modelo se torne generalista antes de uma possível especialização posterior via fine-tuning. O instrutor também reforçou a ideia de que o modelo não “entende” como um humano, mas consegue produzir texto fluente porque aprende a forma e a distribuição de padrões textuais.

A aula então detalhou o mecanismo de aprendizado por previsão do próximo token, ligado aos modelos autoregressivos. Foi apresentado o CLM, ou Causal Language Modeling, como a estratégia usada por modelos como GPT-2, GPT-3, GPT-4, Llama, Mistral e Phi. Nesse processo, o modelo recebe uma sequência e tenta prever o próximo elemento com base apenas no contexto anterior, caracterizando a causalidade da geração. Essa restrição é implementada por uma máscara causal, que impede o modelo de olhar para tokens futuros. Durante o treinamento, o texto é tokenizado, o modelo faz uma predição a partir de uma sequência incompleta, e depois essa previsão é comparada ao token real. O erro obtido é então propagado de volta pela rede por meio de backpropagation, ajustando pesos e vieses da arquitetura. Para medir a diferença entre a distribuição prevista e a correta, foi explicada a Cross Entropy Loss, função de perda que quantifica quão distante a predição está da resposta esperada e fornece o sinal numérico necessário para otimização eficiente do treinamento.

**Pontos de atenção**  
- O pré-treinamento moderno não depende de rótulos humanos; confundir isso com aprendizado supervisionado gera uma compreensão errada da etapa.  
- A principal matéria-prima do pré-treinamento é o volume e a diversidade dos dados textuais; textos repetidos ou pouco variados limitam a qualidade do modelo.  
- Dados da web e de plataformas com muita interação humana têm alto valor porque capturam linguagem natural em uso real.  
- Grande parte da web já foi explorada em treinamento, então acesso a dados novos virou um diferencial estratégico.  
- Rotulagem manual é cara e difícil de escalar; por isso, é importante diferenciar claramente dados rotulados de dados não rotulados.  
- O modelo aprende padrões textuais, não significado humano profundo; ele pode gerar respostas fluentes sem “entender” o conteúdo como uma pessoa.  
- No CLM, o modelo só pode usar o contexto anterior; olhar para o futuro viola a lógica causal do treinamento.  
- A máscara causal é essencial para garantir que o treinamento reflita o comportamento real de geração.  
- O fluxo correto é: tokenizar, prever o próximo token, comparar com o token real, calcular o erro, aplicar backpropagation e ajustar parâmetros.  
- A Cross Entropy Loss é a função de perda central nesse processo; sem uma métrica desse tipo, o ajuste do modelo fica muito mais difícil e custoso.  
- O pré-treinamento prepara o modelo para uso geral, mas a especialização costuma vir depois, com fine-tuning.