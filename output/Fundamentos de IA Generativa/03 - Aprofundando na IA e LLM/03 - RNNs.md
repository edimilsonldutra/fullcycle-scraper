Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16374)

## Resumo da aula

RNNs foram projetadas para processar dados sequenciais, como texto, áudio, séries temporais e vídeo, preservando informação entre passos consecutivos. Retomando a limitação das redes feedforward já discutida, o problema central era a perda de contexto: o modelo processava uma janela fixa e não carregava adiante o que havia ocorrido antes. A RNN introduz um estado interno que funciona como memória próxima do processamento atual. Com isso, a saída em cada instante depende tanto da entrada corrente quanto do estado acumulado dos passos anteriores.

O ganho prático dessa memória aparece quando a ordem dos elementos importa. Retomando o contraste entre frases com as mesmas palavras em ordens diferentes, a RNN consegue usar o histórico processado para favorecer sequências mais coerentes ao longo do texto. Esse mecanismo permitiu avanços relevantes em tradução automática, geração de texto, reconhecimento de fala e análise de sentimento. O ponto central não é apenas representar palavras em vetores, mas manter um rastro computacional do que já foi processado.

O principal limite das RNNs clássicas surge quando a dependência entre elementos fica muito longa. Durante o treinamento, os gradientes podem se tornar pequenos demais ao serem propagados por muitos passos, e a rede perde a capacidade de relacionar o estado atual com informações distantes do início da sequência. Esse fenômeno é o desvanecimento de gradiente. A consequência prática é o esquecimento de contexto longo, como errar a concordância entre um sujeito no começo da frase e um verbo no final.

O problema oposto também ocorre: os gradientes podem crescer demais e tornar o treinamento instável. Quando isso acontece, pequenas atualizações passam a produzir mudanças excessivas nos parâmetros, o que degrada a aprendizagem e compromete a rastreabilidade do contexto. Esse fenômeno é chamado de explosão de gradiente. Assim, a mesma arquitetura que introduz memória também cria uma dinâmica de treinamento difícil de estabilizar em sequências extensas.

RNNs processam a sequência passo a passo, porque cada estado depende do anterior. Essa dependência impede paralelização eficiente no treinamento e na inferência, o que reduz throughput e dificulta escalar para grandes volumes de dados. O resultado é um modelo mais lento do que arquiteturas que conseguem processar múltiplos elementos simultaneamente. Essa limitação se torna crítica quando o vocabulário cresce e o contexto necessário fica mais complexo.

LSTM, sigla para Long Short-Term Memory, modifica a RNN para controlar melhor o fluxo de informação na memória. Em vez de apenas acumular estado, a arquitetura decide o que entra, o que deve ser esquecido e o que segue para a próxima etapa. Esse controle é implementado por portas, incluindo entrada, esquecimento e saída. A ideia é reter padrões relevantes por mais tempo e descartar ruído antes que ele degrade o estado interno.

GRU, sigla para Gated Recurrent Unit, persegue o mesmo objetivo da LSTM com uma arquitetura mais enxuta. Ela combina mecanismos que na LSTM aparecem separados, reduzindo o número de portas e, portanto, a quantidade de parâmetros. Essa simplificação tende a acelerar o treinamento e frequentemente entrega desempenho comparável em muitas tarefas. A troca é arquitetural: menos complexidade interna para tentar preservar boa capacidade de memória.

Mesmo com essas melhorias, o processamento continua sequencial e o contexto muito longo ainda permanece difícil de capturar de forma robusta. LSTM e GRU mitigam os problemas de memória, mas não eliminam a limitação estrutural de depender do passo anterior para computar o próximo. Também continuam com dificuldade para escalar bem em grandes volumes e para modelar relações estruturais distantes entre tokens. Esse conjunto de limites motivou a próxima geração de arquiteturas voltadas a paralelismo e dependências de longo alcance.

## Transcrição

00:00

Fala galera, beleza? Queria falar agora com vocês um pouquinho sobre as redes neurais recorrentes, as RNNS. RNNS, porque tá em inglês, então Network vira N em vez do R. Isso me confunde toda hora que eu for falar em português, porque toda vez que eu falar em português, eu vou falar recorrentes e tal. Então, ao longo da nossa conversa, pode ser que eu erre isso, inclusive. Mas vamos lá. O desafio que a gente tem pra resolver até agora, sendo bem honesto, a gente falou aqui ó, bigrama,

00:29

onde a gente conseguiu evoluir duas palavras, certo? Então eu consigo ter uma coerência de duas palavras indo sempre pra frente, então no feedforward, e esse bigrama eu consigo manter coerência entre a palavra 1 e a 2, depois a 2 e a 3, depois a 3 e a 4, mas a 1 já perdeu ligação, certo? Isso era um grande problema. Depois eu fui pra uma ideia da cadeia de Markov, onde eu consegui trabalhar com um conjunto maior de palavras, beleza?

00:54

Depois eu fui para as redes neurais profundas. As redes neurais profundas trouxeram uma habilidade muito maior de você conseguir trabalhar grandes textos. Ótimo! Mas ela ainda tinha limitações. Lembra que a gente falou de algumas limitações? As redes neurais recorrentes resolveram algumas dessas limitações. Mas algumas, não conseguiram resolver todas. Então você vê aqui o que? Que a academia

01:19

estava tentando buscar uma forma de resolução desta coerência de textos encadeados longos. Por quê? Quando a gente fala da nossa linguagem natural, e aí vocês vão ver que hoje em dia a gente fala muito da linguagem natural, a gente já vai chegar nela. Mas quando a gente fala da nossa linguagem natural aqui, o português, o inglês e assim por diante, cada palavra que a gente fala, ela depende da palavra que veio anterior e até mais, de algumas palavras que vieram antes. Porque a gente formula a nossa frase estruturando com o que foi falado antes.

01:47

para manter sentido e coerência, beleza? Então, para você conseguir fazer isso, essa conversa, casar, fechar, etc, você precisa ir construindo isso ao longo do tempo. Isso foi um problema durante toda a construção e a concepção de inteligência artificial que conseguisse gerar algo. Ainda mais quando a gente está falando de texto, de imagem, de vídeo e assim por diante. Tudo isso depende desta capacidade de encadeamento. Então, quando a gente está falando das

02:16

redes feedforward que a gente estava falando que só vai pra frente não consegue ver o que aconteceu para trás o processamento é um bloco fixo de entrada certo então você colocou um bloco fixo de entrada desse tamanho desse tamanho desse tamanho e com base nisso a gente vai é conseguir evoluir e você vai precisar de um modelo então

02:35

que consiga guardar na memória o que foi processado anteriormente para conseguir ter essa evolução. Então, diferente de você só processar para frente, agora você precisa processar para frente e guardar o que foi processado. Então as redes naturais recorrentes vieram para isso, para conseguir então guardar em memória o que já foi processado. É como se a gente tivesse agora

02:56

um poder de processamento e geração que consegue acessar uma memória próxima e com base nessa memória, dá uma resposta melhorada. Beleza? Então, essa é a grande sacada. Então, o que são as RNNS no fim das contas?

03:10

são elas foram projetadas então pra lidar com dados sequenciais tá bom então por exemplo texto, áudio, série temporal ou até mesmo vídeo quando a gente tá falando destes itens as redes naturais recorrentes vão muito bem pra época óbvio lógico se você pegar hoje você vai achar que ela não tá indo tão bem mas pra época ela já começava a ir muito melhor do que a gente tinha nas redes nas redes neurais profundas então essa

03:39

é uma grande diferença. Então em uma RNNS a saída que a gente tem de um instante de tempo ali depende não só de uma entrada como anteriormente a gente tinha, mas também do que a gente tem de estado

03:56

guardado em memória, que é o processamento passado. Então, você vai e processa um feedforward. Então, você vai processando para frente e guardando o que tinha no passado para ser acessado pelo próximo passo de processamento. Então, aqui você tem como se fosse uma memória em cache do que já foi processado e daí dentro... Em cache, guarde isso. Então, uma memória próxima, memória que está aqui mais perto do seu processamento, para te falar o que já foi feito e te dar coerência

04:21

na evolução do seu encadeamento de palavras, do seu encadeamento de informações. Eu tô falando muito de palavras porque fica mais fácil de entender. Se a gente for trazer isso pra vídeo, é muito mais complicado. Então, vamos pensar desse jeito. Você tá gerando um texto, você precisa fazer esse encadeamento. Para o encadeamento acontecer, você monta desse jeito.

04:39

Olha, direto quando eu vou falar redes neurais recorrentes, vem na minha cabeça naturais, não sei porquê. Então eu devo ter falado algumas vezes aqui, redes naturais recorrentes. Não é naturais, é neurais. Mas direto na minha cabeça vem naturais, não sei porquê. Acho que é o costume de falar em inglês, na hora que eu vou falar em português eu me confundo, gente. Perdão. Uma hora eu melhoro. Por que as RNNs foram um avanço para o nosso dia a dia?

05:05

Primeira coisa, lembra que eu falei pra vocês que o cachorro mordeu o homem?

05:25

Lembra que eu falei que a gente poderia perder a coerência colocando o homem mordeu o cachorro? Por que isso acontece? Porque a gente não tem essa capacidade de saber o que vem primeiro, o que é coerente aqui. Porque eu trabalhei tudo isso aqui transformado muitas vezes em vetor, e daí o vetor vai dar muito próximo, como eu falei para vocês. Agora, quando eu guardo isso em memória como processamento, eu consigo nas RNNS,

05:52

colocar sempre o cachorro mordeu o homem não o homem mordeu o cachorro porque eu vou guardar em memória o que foi dito o que foi processado e com isso consigo acessar e dar mais coerência e daí pra isso com isso quer dizer eu consigo evoluir algumas coisas como por exemplo a tradução automática

06:10

que a gente teve uma evolução muito grande quando chegou as RNSS, a geração de texto, reconhecimento de fala também vem bem, até uma coisa bacana que veio junto, análise de sentimento, você começa a entender o tom do que está sendo dito, pensa assim, do que está escrito e assim por diante, então isso é muito importante, a gente conseguiu ter boas evoluções aqui.

06:33

E quais são as limitações que ela traz? A primeira coisa que é muito grave é processamento, poder de processamento. Ela gasta um pouco de poder de processamento, mas eu não vou falar disso agora, porque isso foi resolvido, pacificado, andamos para frente. Mas a gente tem um salto aqui gigantesco, só que tem um negócio muito crítico. Pensa no seguinte, imagina que eu fui guardando memória, vocês vão ver onde eu vou chegar.

06:56

O que pode acontecer? Quando uma sequência é muito longa, eu posso ter um negócio que chama desvaneciamento de gradiente. Palavra difícil, né? Desvaneciamento. Esse desvaneciamento de gradiente é o seguinte, eu perdi a memória. Eu não consigo mais acessar uma memória muito longa. Então, os sinais de aprendizado, as gradientes que eu tinha, elas se tornam muito pequenas,

07:22

E com isso eu não consigo voltar o elemento de sequência. Ou seja, a rede esquece o início. Ela não sabe onde começou aquilo. Então você começa a ter a sua memória guardada gradientes que tem valor tão pequeno que você não consegue entender qual foi o primeiro elemento gerado.

07:39

porque aqui eu tô falando pra vocês que eu guardo em memória, não vou guardar em memória lá por exemplo o cachorro, não é isso que eu guardo eu guardo a gradiente e daí com base nisso como é que eu busco isso depois se ela começa a ficar muito pequena eu perco essa rastreadibilidade então a minha memória se perde ao longo do treinamento e daí com base nisso eu capoto então aqui tá um grande problema desvaneciamento de gradiente esse cara é uma das grandes limitações um grande problema das rnns e faz ela alucinar querendo ou não

08:09

e tem o inverso, se pode ser para menos, pode ser para mais, então tem a explosão do gradiente também que pode acontecer, a explosão já é um nome melhor né, porque o outro nome é difícil de falar, o oposto então também pode acontecer, o gradiente ele pode ficar muito grande e daí vai gerar uma instabilidade no treinamento dessa

08:29

dessa rede neural. Então, aqui é um grande ponto também de problema. Foi lá, aumentou muito a minha gradiente, explodiu. Com isso, eu não consigo mais acessar, eu perdi a rastreadibilidade e alucino de novo. Então, mesmo com essa memória, ela tem dificuldade de ter uma dependência de muito longo prazo. Então, se eu for fazer uma coisa muito grande, possivelmente eu vou capotar. Então, eu vou dar um exemplo. Imagina que você escreveu toda uma frase.

08:55

Você lembrar qual o sujeito da frase que foi falado no início para depois aplicar em um verbo no final, por exemplo, você vai errar. Você pode colocar um verbo lá no final que não vai casar com o sujeito do início, aí você não vai entender o que está sendo dito ali. Então, é importante pensar nisso. Outro problema que ela traz, esse também é muito grande e trava muito o poder de processamento e velocidade, foi o que eu comecei a falar com vocês.

09:20

Como cada processamento é sequencial, ou seja, cada palavra vai depender da palavra anterior, eu não tenho como paralelizar isso de uma forma a deixar o treinamento mais rápido. Eu preciso processar isso encadeado, uma coisa de cada vez. Então, eu não consigo paralelizar e com isso eu fico lento para fazer as coisas. Então, eu não consigo treinar grandes volumes e para quem conhece, quem sabe de A, grandes volumes dão mais instabilidade, grandes volumes de dados, grandes volumes de treino,

09:50

deixar uma I.A. melhorada e mais preparada. E com isso, a gente tem esse problema também. Deixa eu só tomar uma colher d'água. Perdão, gente. Tava dando vontade de tossir. Vamos lá. Mais um item pra gente pensar aqui.

10:11

Temos esses problemas, vamos resolver? Então veio uma evolução, que são as LSTM. Você não precisa guardar esse monte de nomezinho não, depois você volta no vídeo e vê, ou depois eu vou até fazer um compilado do que a gente falou aqui de grandes siglas pra ficar pra você buscar, caso você tenha alguma dúvida, tá bom? Eu deixo aqui um documentinho pra você buscar.

10:36

Mas então, quais são as evoluções aqui? Ou até no material direto que você consegue buscar. Quais são as evoluções que a gente tem aqui? As LSTM e a GRU. Vou falar primeiro da LSTM. Ela ajuda a gente a contornar algumas limitações que a gente tem. É uma melhoria de arquitetura, tá gente? Eu vou trazer pra vocês, mas só pra vocês entenderem como isso foi sendo montado. Vocês não precisam decorar isso também, pelo amor de Deus.

11:05

ela começa a adicionar um controle na memória. Então imagina que antes você estava guardando memória, guardando memória, guardando memória e estoura a memória. Você pode estourar a memória para cima e pode estourar a memória para baixo. Então a LSTM, a significada é Long Short Term Memory. Isso mesmo, Long Short Term Memory. Então essa LSTM, ela faz o seguinte,

11:29

Eu não lembro o GRU, GRU é... Gated Recurrent... Eu não lembro o U, já vou. Depois eu falo pra vocês ao longo aqui. Eu vou lembrar. Mas, bom... As LSTMs e as GRUs, elas fazem a mesma coisa. Elas vão limpar a memória, pensa assim. Então, pensa que você pode estourar pra cima ou pra baixo. Gated Recurrent Unit, é isso. Unit U. Então, elas podem estourar tanto pra cima quanto pra baixo.

11:58

Como elas podem estourar tanto pra cima quanto pra baixo, você vai limpar essa memória. Limpando a memória, você diminui esse problema, mas você não vai resolver ele também. Então, quando a gente tá falando das LSTM,

12:12

ela começa a controlar o fluxo de informação então você tem um controle de porta de entrada que decide o que entra na memória decide o que precisa ser apagado na memória que é a porta de esquecimento então aqui você vai ter porque não é simplesmente ir lá e apagar a memória do nada você tem que controlar o que entra com base no que entra você vai controlar o que você quer seguir de processamento tem uma porta de esquecimento que é onde você

12:39

posta ou coloca o que você precisa apagar, e tem uma porta de saída que decide o que vai ser passado adiante. Então pensa que a memória vai sendo evoluída. Com isso eu tenho então, o que vai entrar, o que está sendo apagado e o que vai seguir. E depois eu evoluo isso ao longo do tempo. Então essa estrutura vai fazer o que? Com que a rede retém informação relevante e esqueça aquilo que não faz sentido.

13:01

Então, o que é mais relevante, ela guarda ao longo do tempo. As que são ruído, irrelevante, você vai jogando fora. Querendo ou não, se você parar para olhar, é uma forma bruta de resolver uma necessidade de processamento massivo, ou uma necessidade de guarda de informação que a gente não conseguia ter. Então, com isso você consegue guardar mais os padrões que você precisa, que são úteis,

13:26

para manter o seu aprendizado funcionando. Então, é basicamente isso que a gente resolve com essas duas estratégias, tá bom? Só que... Uma veio primeiro que a outra. O LSTM veio primeiro e depois veio a GRU. Então, a Gated Recurrent Unit veio com a ideia de evoluir um pouco isso. Então, ela começa a...

13:50

resolver um pouco a arquitetura que eu te falei das LSTM deixando elas mais simplificadas então a porta de entrada e de esquecimento viram uma coisa só isso inclusive de vez em quando eu confundo as duas arquiteturas sendo bem honesto porque quando eu olho para a arquitetura GRU ela foi muito mais simplificada e a gente acaba falando mais dela no dia a dia

14:15

Então ela tem um treinamento mais rápido, porque você tem só três portas para trabalhar, perdão, duas portas para trabalhar, você não tem mais três portas como a LSTM. Então você vai conseguir ter menos parâmetros também para cuidar, porque imagina que aqui tudo é parâmetro, que você vai jogando de um lado para o outro, e você tem uma performance bem comparável com a LSTM. Então em muitas tarefas você chega muito próximo disso. Então as duas foram para resolver esse problema, beleza gente?

14:41

Quais são as limitações que continuam apesar dessas duas estratégias chegarem? Você ainda é sequencial, então você não consegue paralelizar, o aprendizado ainda é lento. O modelo muito longo ainda tem dificuldade de manter contexto, porque tudo isso é estratégia, estratégias que eu acho que são mais do mesmo. Você está trabalhando ainda do status quo atual para conseguir resolver o problema de contexto.

15:10

Isso só vai ser resolvido lá para frente. Então, é difícil de você escalar para grande volume, vocabulário muito grande, complexo, fica mais difícil... E você não consegue buscar relações estruturais e dependência entre cada um desses tokens ou vetores. E daí, isso fica muito mais difícil de você conseguir manter a coerência. Então, a gente continua com essas limitações, mas a gente evoluiu bastante coisa. Você está vendo que a gente está começando a chegar perto do que a gente entende como hoje? Porque pensa assim...

15:39

Depois diz qual o próximo passo. Agora eu preciso resolver duas coisas. Poder de processamento em paralelo. Na verdade, acho que são três coisas. Poder de processamento em paralelo. Começar a conseguir processar um número maior de dados sem precisar guardar em memória um poder aqui de busca de passado. E conseguir enxergar esse passado. Não só como faz no Feedforward. Então a gente tem essas três coisas para resolver ainda.

16:08

Eu já fui até o máximo se você parar pra pensar. Com as RNNS a gente quase chega no máximo do que poderia ser evoluído. Qual o próximo passo que a gente tem pra dar agora? Na próxima aula eu trago pra vocês qual foi a próxima evolução e como que a gente começa a se aproximar cada vez mais do modelo que a gente conhece hoje. Beleza?

## Resumo IA

**Abreviações**
- **RNN / RNNs** — *Rede Neural Recorrente* / *Redes Neurais Recorrentes*
- **LSTM** — *Long Short-Term Memory* (*Memória de Curto e Longo Prazo*)
- **GRU** — *Gated Recurrent Unit* (*Unidade Recorrente com Portas*)
- **IA** — *Inteligência Artificial*
- **feedforward** — rede neural *de avanço direto* (processamento apenas para frente)
- **A.I.** — *Inteligência Artificial*

**Resumo**
A aula apresentou as Redes Neurais Recorrentes (RNNs) como uma evolução importante para o processamento de dados sequenciais, como texto, áudio, séries temporais e vídeo. O instrutor retomou a limitação das redes feedforward e de modelos anteriores, como bigrama e cadeia de Markov, destacando que eles perdiam contexto ao trabalhar com janelas fixas ou dependências curtas. A proposta das RNNs é introduzir um estado interno que funciona como memória próxima, permitindo que a saída em cada passo dependa não só da entrada atual, mas também do histórico já processado.

Ao longo da explicação, foi enfatizado que essa capacidade de manter contexto é fundamental para tarefas em linguagem natural, especialmente quando a ordem importa, como na construção de frases coerentes, tradução automática, geração de texto, reconhecimento de fala e análise de sentimento. O instrutor usou exemplos simples para mostrar que a rede consegue preservar o encadeamento das informações e melhorar a coerência do que está sendo gerado ou interpretado.

Também foram discutidas as principais limitações das RNNs clássicas. Em sequências longas, surgem problemas de desvanecimento de gradiente, quando os sinais de aprendizado ficam pequenos demais e o modelo perde a capacidade de relacionar elementos distantes, e de explosão de gradiente, quando os valores crescem demais e o treinamento fica instável. Além disso, como o processamento é sequencial, a paralelização é difícil, o que reduz desempenho e dificulta o uso em grandes volumes de dados.

Para contornar parte desses problemas, a aula apresentou duas variações arquiteturais: LSTM e GRU. A LSTM foi descrita como uma RNN com controle de fluxo de informação por portas, decidindo o que entra, o que é esquecido e o que segue adiante. Já a GRU foi mostrada como uma versão mais enxuta, com menos portas e menos parâmetros, mantendo desempenho comparável em muitas tarefas e com treinamento mais rápido. Ao final, o instrutor reforçou que essas melhorias mitigam, mas não eliminam, as limitações estruturais de sequencialidade e dependência de longo prazo, preparando o terreno para a próxima evolução das arquiteturas neurais.

**Pontos de atenção**
- RNNs lidam melhor com **dados sequenciais**; não são a melhor escolha quando a ordem e o contexto temporal não importam.
- O principal benefício é a **memória de curto prazo** do estado interno, que ajuda a manter coerência entre passos consecutivos.
- Em **sequências longas**, ocorre **desvanecimento de gradiente**, fazendo a rede “esquecer” informações do início.
- Também pode ocorrer **explosão de gradiente**, tornando o treinamento instável.
- O processamento é **sequencial**, o que dificulta paralelização e reduz desempenho em grandes volumes.
- **LSTM** melhora o controle da memória com portas de entrada, esquecimento e saída, mas **não resolve totalmente** o problema do longo prazo.
- **GRU** simplifica a LSTM e costuma treinar mais rápido, porém continua sujeita às limitações estruturais das RNNs.
- Mesmo com LSTM e GRU, ainda há dificuldade para capturar **dependências muito distantes** e relações estruturais complexas entre tokens.
- É importante não confundir a utilidade dessas arquiteturas: elas **mitigam** limitações, mas não substituem soluções posteriores voltadas a paralelismo e contexto amplo.