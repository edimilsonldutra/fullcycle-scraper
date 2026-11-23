Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16395)

## Resumo da aula

Retomando o cenário de explicar buracos negros, o experimento útil é manter a mesma pergunta e variar apenas a temperatura ou o modelo. Isso isola o efeito de cada mudança e evita confundir diferença de prompt com diferença de geração. No Playground, o campo de mensagem concentra o prompt e o painel lateral reúne modelo, provider e parâmetros de geração. A comparação só faz sentido quando a variação é controlada.

Com temperatura em 0,1, a resposta tende a seguir caminhos mais estáveis e a errar menos palavras. No exemplo, o modelo produziu analogias consistentes, como ralo de pia cósmico e cachoeira para horizonte de eventos, mantendo boa coerência entre as seções. O resultado fica mais previsível, mais organizado e mais próximo de uma explicação técnica guiada. Para tarefas explicativas, esse comportamento reduz desvios desnecessários.

Em 0,5, a saída ainda preserva estrutura, mas ganha mais flexibilidade lexical e analogias um pouco mais variadas. No mesmo prompt, a resposta continuou compreensível, com menos rigidez do que em 0,1 e sem a dispersão observada em valores extremos. Esse ponto intermediário costuma ser útil quando se quer didatismo com alguma riqueza de formulação. A escolha é prática: clareza suficiente sem engessar demais a resposta.

Quando a temperatura sobe para 1, o modelo começa a introduzir elementos não solicitados explicitamente, como curiosidades, metáforas mais ousadas e associações menos previsíveis. No exemplo, surgiram formulações como “pipoca queimada” e explicações adicionais sobre dilatação do tempo, mesmo sem pedido direto. Isso pode enriquecer a resposta em tarefas abertas, mas também aumenta a chance de exagero, imprecisão ou perda de foco. O ganho de criatividade vem junto com menor controle.

Valores como 2 não apenas deixam a resposta mais criativa; eles podem degradar a geração a ponto de torná-la incoerente. No experimento, apareceram mistura de idiomas, trechos desconexos e raciocínio textual quebrado, sinal de que a amostragem ficou aberta demais. O efeito prático é perda de qualidade, não apenas aumento de variedade. Por isso, em uso normal, faz sentido restringir a faixa operacional a algo entre 0,1 e 1.

Alguns modelos exibem um campo Thinking, que revela uma etapa intermediária de planejamento da resposta. Esse campo mostra intenções como simplificar termos técnicos, escolher analogias e organizar tópicos antes da saída final. Ele é útil para inspeção qualitativa do comportamento do modelo, porque permite comparar o plano interno com o texto entregue. Nem todo modelo ou provider expõe esse campo, então sua ausência não significa ausência de raciocínio, apenas ausência de visibilidade.

Trocar apenas a temperatura mostra como um mesmo modelo varia; trocar o modelo mostra diferenças de capacidade, estilo e cobertura linguística. No experimento, DeepSeek gerou respostas mais longas e com Thinking, Minimax respondeu em inglês, Gemini produziu saídas mais curtas e Mistral não expôs o planejamento interno. Além do modelo, o provider também interfere na execução: alguns endpoints funcionam melhor, outros falham mais ou exigem plano pago. Comparar modelo sem fixar prompt e contexto de execução produz conclusões fracas.

No Playground, alguns modelos ou rotas de execução podem exigir upgrade de plano. O comportamento típico é exibir um pop-up de cobrança ou bloquear a execução daquele endpoint específico. Isso não invalida o experimento; basta trocar para outro modelo ou provider disponível. Em ambiente exploratório, a estratégia prática é priorizar opções gratuitas estáveis antes de comparar alternativas pagas.

Falhas no botão de execução são comuns em Playground, especialmente quando o provider está instável ou o endpoint está sobrecarregado. O procedimento operacional é simples: fechar a tentativa com erro e executar novamente, ou trocar o provider quando houver opção. Esse tipo de erro não deve ser confundido com problema conceitual no prompt ou no parâmetro de temperatura. Separar erro de infraestrutura de comportamento do modelo evita diagnósticos errados.

O experimento mais informativo usa a mesma pergunta, fixa um modelo e varia a temperatura em pontos como 0,1, 0,5, 1 e 2. Depois, mantém a temperatura e troca o modelo para observar profundidade, idioma, estilo, presença de Thinking e robustez da resposta. No cenário dos buracos negros, isso permite perceber quando a resposta é precisa, quando fica criativa e quando degrada. Esse método transforma impressão subjetiva em comparação técnica reproduzível.

## Transcrição

00:01

Fala galera, beleza? Agora que a gente já aprendeu como entrar no Hugging Face, como a gente log assim por diante. Espero que tenha dado tudo certo com você na criação do email e depois na aprovação ali. Espero que tenha dado tudo certo. Se deu tudo certo, você vai estar nessa telinha aqui pra gente conversar.

00:19

Se não, volta lá no vídeo e tenta fazer o passo a passo pra você conseguir chegar nessa telinha em qualquer coisa, pede ajuda, a gente tá por aqui pra te ajudar. Mas vamos lá. Imagina que você chegou aqui nessa hora no Hugging Face, o que que tem aqui pra gente brincar um pouco? Primeiro, então a gente tava nesta página, a gente já clicou em Playground, chegamos no Playground, beleza? No Playground,

00:42

Eu tenho algumas coisas, eu posso ficar mexendo em busca, eu posso ir aqui em cima nessa parte de cima mudando de aba, indo pra outras áreas, saindo do playground, então eu posso ir nos modelos, nos bancos de dados, space, comunidade, docs, inclusive tem bastante coisa legal aqui pra gente mexer depois.

00:58

E aqui tá o seu perfil e assim por diante. Então você tem aqui toda uma mudança, saída e etc. Daqui um menuzinho pra você mexer em tudo que você quiser. Tem coisa pra caramba pra brincar aqui. Algumas coisas do Hugging Face vão ser pagas, então dependendo de onde você clicar ele vai pedir pra você subir seu nível e assim por diante.

01:16

Porque o que a gente vai fazer aqui não precisa. A gente só precisa conhecer como funcionam as coisas. O que a gente vai focar nesta aula? Quero focar no seguinte. Primeiro, vamos olhar este pedaço. Este pedaço aqui vai ser o lugar onde você vai colocar as mensagens, os comandos que você quer dar.

01:32

E quando você olha aqui para o modelo, para o seu lado direito, você vai ter aqui os modelos que você pode mexer e quais são os parâmetros que você pode brincar aqui. Então tem temperatura, topeira, depois a gente vai falar um pouco disso também. Beleza? Vamos falar então de temperatura que é o que a gente veio falar nessa aula. Então aqui na temperatura você vai ver que você consegue mexer nela. Qual que é a grande sacada da temperatura? Aqui ele permite que você abra muito essa temperatura.

01:58

Então lá na aula eu falei que a gente ia rodar entre 0,1 ou 0, na verdade a gente trabalha sempre com 0,1, 0 não faz nem muito sentido, até 1, olha que 1 tá aqui. Pô Nathan, mas dá pra ir até 2, veja só. Aqui no Game Face ele deixa você brincar justamente pra você conseguir ver como muda. Vamos ver junto como muda então?

02:20

Mas antes de a gente colocar qualquer mensagem, eu vou deixar no 01, ou seja, pra ela ficar bem fechadinha, ela ter pouca criatividade, e vou deixar aqui um modelo que a gente já tá mais acostumado. Esse minimax, a gente não falou, então vamos falar de um que já tá mais bombado, que a gente conhece, que é o DeepSeek R10528. Esse cara é muito legal pra brincar. Tem outros aqui embaixo, tem vários. Se vocês forem olhar, tem uma porrada. Só da DeepSeek, olha o tanto que tem. DeepSeek com lhama, tem uma porrada aqui.

02:50

Lhama, 3B, Pi... Nossa, uma porrada de... Tem o da meta aqui, cadê? Perdi, mas tava ali. A gente tem uma porrada aqui de tipos pra você brincar. Qual que é o grande ponto que você tem que prestar atenção? Se eu pegar, dependendo do...

03:09

DLLM que eu puxo aqui, por exemplo, uma da Microsoft, etc. Pode ser que você já pague. O próprio da DeepSeek, a gente fala que a DeepSeek é de graça, os da Google, GME, tudo pago normalmente. Quando você pega os da DeepSeek, a DeepSeek é de graça, mais ou menos. Se você pegar o DeepSeek R1 aqui direto, ele vai pedir para você subir o plano. Vamos pegar o DeepSeek R1-0528 que ele tem uma

03:33

uma quebra por trás. Eu vou mexer aqui em quem tá gerando isso pra gente. Você pode colocar automático. Eu gosto de colocar da Novita, normalmente funciona. Esses outros às vezes eles quebram, mas é legal você testar também. Não tem problema você testar. Aqui você tá decidindo uma IA que já tá preparada, já tá EPizada pra você fazer esse tipo de brincadeira. É um Playground pra você, tá bom? Então vamos colocar aqui um

03:59

Eu fiz uma pergunta aqui ó, me explique como funciona um buraco negro utilizando exemplos claros de abstração com temas mais fáceis para melhorar o entendimento. Como eu coloquei abstração, exemplos etc, ele já vai ir um pouco mais longe na sua capacidade criativa, porque eu promptei isso. Depois a gente vai mexer nesse prompt pra vocês verem a grande diferença também.

04:22

Mas vamos direto desse jeito aqui. Se eu for desse jeito, com temperatura 0,1, o que que acontece? Vamos pôr play nesse carinha. Quando põe play aqui, às vezes ele dá um erro, tá? Quando der um erro é só você fechar e pôr play de novo. Quando a gente vai brincando aqui, talvez aconteça e vocês vão ver, mas nenhum problema pra isso é que às vezes a peita fora, acontece alguma coisa nesse sentido. Então, primeira coisa que eu queria ver com vocês. Tá vendo que ele tá gerando aqui. Ó, tá rodando ali, gerando tudo quanto é tipo de informação pra gente.

04:51

Tá ficando grande o texto. Vamos subir ali enquanto ele gera pra baixo, pra gente não ficar só esperando. Primeira coisa que vocês tem que olhar é que normalmente a gente não vê numa IA que a gente tá acostumado a lidar ali no dia-a-dia. Tá vendo o que ele colocou aqui? Thinking. Ele tá pensando, então ele coloca o que ele precisa fazer. Ó, vamos explicar buracos negros usando analogia simples e temas do dia-a-dia. Eu não coloquei nada de temas do dia-a-dia aqui, tá vendo?

05:15

A ideia é evitar termos técnicos complexos e focar em conceitos fundamentais. Gravidade extrema, horizontes de evento e singularidade. Então ele já focou no que ele quer passar, ele já mostrou pra gente o que ele tá pensando por trás, pra daí sim gerar toda essa camada de coisas aqui. Aí beleza, ele tá gerando todo esse monte de informação aqui ó. Ainda tá gerando ó, o resumo visual,

05:42

Calma aí que ele tem coisa pra gerar ainda. Beleza, gerou tudo. Então aqui ó, ele gerou tudo que ele tinha pra gerar. Vamos ver... tá bom. Vamos ler aqui mais ou menos um pedacinho só pra gente poder comparar depois. Então ó, primeira coisa, o que é um buraco negro?

06:03

A analogia é um ralo de pia cósmico. Então ele já foi numa imaginação aqui e conseguiu abstrair alguma coisa. Imagine um ralo de pia com água correndo em direção ao buraco. Quanto mais perto da abertura, mais rápido a água gira e mais forte é o puxão.

06:19

Foi uma boa explicação inclusive. Um buraco negro é como um ralo tão poderoso que nada escapa nele. Nem mesmo a luz. A água representa tudo que se aproxima de mais. Gás, poeira, estrela e assim por diante. E o ralo é o buraco negro. Então ele explicou aqui dessa forma. Vamos lá. Outra coisa. Horizonte de eventos. Horizonte de eventos é legal.

06:39

Quando a gente olha o horizonte de eventos, que é o ponto sem volta, ele fez uma analogia, nadar em um rio com uma cachoeira. Imagine que você está nadando em um rio calmo que deságua em uma cachoeira gigante. Existe um ponto crítico onde a correnteza fica tão forte que mesmo se você nadar com toda a força,

06:57

você não consegue voltar e inevitavelmente cai na cachoeira. Esse ponto é o horizonte de eventos. O buraco negro, depois cruzá-lo, não há retorno. Tem uma porrada de coisa. Fala de singularidade, porque a luz não escapa e assim por diante. Um monte de coisa. Inclusive, achei que ele mandou super bem. Fez aqui um resumo visual. Ele falou... Termina aqui. Espero que esta comparação torne o tema mais claro. E aqui no Thinking, ele fecha...

07:24

e depois ele pega tudo que ele pensou aqui tá vendo que tá tudo que ele pensou e joga para a resposta que ele vai dar para você e no final das contas aqui é ele já está te dando uma resposta um pouco mais direta tá vendo então depois de tudo que ele pensou aqui ó tá vendo que ele pensou em um monte de tralha

07:45

que é o pensamento dele, e aqui ó, quando ele fecha essa barrinha aqui, ele vai mostrar o que ele mostraria na tela pra você, o que você veria, tá? E aqui nesse ponto onde você tá vendo,

08:02

Ele vai contar mais ou menos aquilo que a gente acabou de falar. Então olha, só que ele tá deixando mais aberto. Então ó, um ralo cósmico sem fundo. Pensa em um ralo de pi extremamente poderoso. Tudo que se aproxima de mais água, folha, inseto é sugado e nunca mais volta. Não importa o quão rápido tente escapar. O buraco negro faz o mesmo. Tudo no espaço. Luz, planilhas, estrelas.

08:20

gera uma gravidade tão forte que nem a luz a coisa mais rápida do universo consegue fugir. Então aqui ele já falhou num token, ele gerou um grava e era pra ser gera possivelmente.

08:36

Como a gravidade funciona, o ponto sem volta, que a gente acabou de falar, o horizonte de evento, na analogia de uma cachoeira mortal. Imagine um rio tranquilo, que deságua em uma cachoeira gigante, antes da queda você ainda pode nadar contra a correnteza, na borda da cachoeira. Então tudo aquilo que a gente falou, foi este tipo de remensagem que ele deu. Vamos aumentar essa temperatura para 1, então vamos deixar ele ser mais abrangente, ele ir mais longe na resposta dele. Então eu vou fechar esse, e agora a temperatura em 1, vamos para o Play e ver como é que ele vai gerar.

09:22

Vamos ver o que que mudou. Então vamos lá, ele pensou aqui a mesma coisa que a gente viu no outro, deixa eu subir pra vocês olharem junto. Então ó, thinking, vamos explicar buracos negros usando analogia simples de termos cotidianos. Então a mesma coisa, ele pensou, certo? E daí aqui ele foi montando mais ou menos o que ele queria contar.

09:42

E aqui vamos ver o que ele gerou de saída. Vamos explorar buracos negros passo a passo usando a analogia simples de temas cotidianos, que é o buraco negro, a analogia e o ralo cósmico no espaço-tempo. Imagine o universo como uma cama elástica esticada.

09:55

Se você colocar uma bola pesada no centro, ele forma uma depressão. Agora imagine colocar um objeto tão pesado que rasga o tecido da cama elástica, criando um buraco sem fundo. Isso é um buraco negro, uma região onde a gravidade é tão extrema que nada nem mesmo a luz consegue escapar. Como se forma a analogia de uma estrela que virou pipoca queimada. Olha só que doideira já.

10:15

Tá vendo como ele começa a gerar algumas coisas um pouco mais malucas? Uma estrela que virou pipoca queimada. No outro ele não falaria pipoca queimada. Pense em uma estrela com uma panela de pipoca no fogão. Estrela comum. O calor da fusão nuclear mantém grãos, matérias, se expandindo e equilibrando e assim por diante. E daí é que ele tá falando, olha...

10:36

sobre grãos, sendo matéria, pipoca queimada que vira um caroço minúsculo super pesado, tá vendo que ele já foi um pouco mais longe, vamos ver da cachoeira que ele gerou, imagina um rio correndo em direção a uma cachoeira

10:52

longe da queda, você pode remar contra a corrente escapar, como uma nave distante de um buraco negro. Bordo da cachoeira, horizonte, se você chegar muito perto, a correnteza te puxa irreversivelmente, ao limite onde nem a luz tem velocidade para voltar. Curiosidade, se você caísse num buraco negro, um observador de fora veria você congelado na borda por causa da dilatação do tempo, mas você seria puxado para dentro em segundos. Tá vendo que engraçado? Ele já deu uma curiosidade, eu não pedi curiosidade, mas ele deu.

11:19

Então, ele já começou a ir um pouco além, falando da singularidade e tal, porque nada escapa, falar aqui umas partes um pouco mais das velocidades e assim por diante. Efeitos curiosos, então ele trouxe aqui os efeitos curiosos, fez também aquele visual,

11:36

Talvez tenha feito, eu não lembro direito na outra resposta, mas parece que o exumo visual na outra era maior, e aqui ele foi mais na parte que é mais abstrata, ele seguiu mais do que nessa parte que é mais direta ao ponto. Vamos fazer uma outra ideia? Vamos colocar dois e vamos ver o que ele gera? Vamos ver se ele consegue gerar alguma coisa ainda pior, ainda mais diferentona do que a gente viu aqui. Vamos brincar. Eu não fiz pra ver, vamos ver o que é.

12:09

Olha que loucura! Já ficou totalmente perdida. Olha! O que é isso aqui? Foi falando outra língua, inclusive. Ficou malucão. Eu passei tanta temperatura que ele ficou doido. Então, vou pôr de novo pra gente ver que não foi um erro. Foi porque a gente abriu muito. Nessa tradução, vamos adaptar o resumo em chinês para o português de duas maneiras possíveis que eu vou tentar abordar entre duas soluções. Solução alternativa.

12:39

Tá doidão. Tá vendo? Ficou doido. Porque com o 2 se abriu tanto, que ele nem sabe mais gerar. Lembra que quando a gente tá falando da geração textual, foi o que eu falei. Aqui fica muito claro. É muito bom esse teste. Eu não tinha feito esse teste, eu tô fazendo com vocês, tá?

12:58

É muito bom fazer esse teste, ainda mais na DeepSeek, porque olha que doideira, pra DeepSeek ela tem um trabalho, ela precisa pegar sua pergunta em português, possivelmente ela vai jogar pra chinês, que é a língua que deve ser mais fácil pra ela de treinamento, treina e depois retraduz. Creio que ela deve fazer algo nesse sentido, tá? Não tenho certeza, mas acho que é por aí. Ela fazendo isso,

13:18

ela tem um trabalho aqui é pra ela conseguir fazer isso ela tem que fazer um monte de processamento olha aqui o tanto de doideira que ela tá gerando e quando você pega e abre a temperatura você pode pensar assim poxa ele vai falar coisas alucinadas do tipo assim o que a gente viu na temperatura um na temperatura um que ele fez ele começou a falar pra gente coisas do tipo a ser um pouco mais abstrata fazer piadas talvez e um pouco mais criativo

13:47

Quando eu vou para uma temperatura 2, o token, a geração do token, você está abrindo para ele fazer o que ele quiser. Então, você está indo em um nível que a gente não deveria ir. Por isso que eu falei no nosso curso que a gente fica entre 0,1 e 1. Quando a gente chega em mais do que 1, normalmente você vai ter esse tipo de maluquice, porque alucinação ou abertura para ele fazer o diferente, pode deixar ele fazer o diferente na criação do próximo token. Lembra do que a gente falou?

14:16

Eu tenho que pensar qual o próximo token que está vindo. Ah, eu toquei em 2, toquei em 3 e assim por diante. Então eu estou tendo lá uma frase de 10 palavras, eu tenho até a oitava. Quando eu chego da oitava para a nona, eu vou tentar identificar qual o próximo token. Quando eu abro a minha temperatura, essa identificação vai para onde quiser lá dentro da rede neural.

14:37

Então, como ele está indo a cada grupo de palavras ali, abrindo para conseguir entender qual que é a próxima palavra, com uma temperatura de 2, ele vai para qualquer lado. Para a gente, parece que ele alucinou. Olha só, ele não consegue falar a nossa língua. Ele começa, ó, traduzindo em buz... ó, ó, que loucura. Aqui está no pensamento dele. No pensamento dele já fica, ó, nada a ver. Vamos ver quando ele sai do pensamento. Cadê? Nem consegui achar onde ele saiu do pensamento, porque está tão bagunçado esse treco aqui.

15:10

Você está pedindo uma explicação sobre os buracos negros usando comparações simplificadas que se conectam à vida real? Essa situação pode ser abordada com alegorias da vida diária.

15:33

Aqui eu não faço ideia do que ele tá falando com os eventos concretos. Assim você recebe duas estratégias didáticas conforme... Hum, tá bom. Acho que ele falou que ele tentou colocar em português esse treco aqui.

15:47

Por onde começa? Como exemplo, racionais natureza, elementos extremamente fáceis. Tá vendo? Não dá pra entender nada do que ele tá falando. Porque aqui, ele abriu muito. Bom, acho que era isso que eu queria mostrar pra vocês. Temperatura, então, a gente fez com uma temperatura muito baixa. A gente fez com uma temperatura, então a gente fez aqui, ó, com 0,1. A gente fez com 1,1, que é mais ou menos aqui.

16:09

e a gente fez com 2 vamos fazer com meio que é onde eu acho que a gente deveria trabalhar normalmente aqui ó 0,5 acho que é um lugar legal para a gente trabalhar esse tipo de pergunta e vamos pôr play gera aí fio

16:26

Aí tem o think, deixa ele pensar, deixa ele gerar pra gente. Mas tá vendo que ele tá com uma resposta parecida com a resposta que a gente gerou mais fechada, mas é com uma resposta que é mais direto ao ponto, talvez, também não abrindo tanto quanto na 1. Então, ele vai gerar aqui mais facilidade de acertar palavras e também vai conseguir gerar pra gente uma explicação que seja com uma analogia interessante pra gente conseguir compreender.

16:54

então olha ele tá indo nas analogias parecidas com as respostas anteriores porque é a mesma máquina aqui de pensamento a gente tá falando do mesmo da mesma LLM mas tem essas diferenças que eu queria mostrar pra vocês espero que vocês tenham conseguido entender já ele tá gerando aqui eu vou dar uma lida rapidinho nesse pedaço pra vocês mas aqui vocês vão ver que ele tá gerando a uma coisa muito parecida

17:18

que é um buraco negro, um ralo da piscina, pense no espaço da piscina cheia d'água, estrelas comuns são... tá vendo que ele já tá explicando um pouco mais... um pouco mais direcionado, mais quebrado, tá vendo que ele fica um pouco mais organizado e ele erra menos palavras, tá vendo, é o ralo fundo da piscina que suga tudo ao redor, a gravidade dele já é tão forte que nem a luz... tá vendo?

17:41

ele começa a gerar isso um pouco mais organizado. Bom, faz esse teste você também, coloca aí, lê com calma, vê as diferenças, é importante para vocês entenderem como isso funciona. Vou fazer mais uma brincadeira com vocês, vamos tentar achar um outro aqui, eu não sei, vou pegar um qualquer, vamos pegar o Minimax.

18:01

é eu não sei nem se ele vai ser pago vamos descobrir não é pago é tá vendo esse cara ele só responde inglês pelo jeito possivelmente o jeito que ele tá organizando aqui ele já nem nem tá acostumado a responder em português vamos deixar ele

18:21

mais lento, você vê a diferença como ele vai jogando grupos de palavras, a forma de entregar isso nem é lento, mas talvez o CX dele é diferente, você consegue ver que no DeepSeek ele tem aquele cuidado de ir jogando palavras ao longo pra você ter a impressão que ele tá processando bem, aqui ele já mostra mais que truncado e daí dá a impressão às vezes que ele é até mais lento, nem sei se é mais lento tá, porque eu não vi qual que é a velocidade dele

18:44

mas ele tem esse tipo de dificuldade já e olha tá gerando tudo em inglês. Pra gente não ficar comparando inglês por português, deixa eu ver se eu pego alguma outra aqui. Vamos pegar uma que a gente já tá mais acostumado. O GM2 acho que ele vai conseguir gerar de graça, vamos ver. Vamos ver o que o 2 faz. Ó, bom.

19:11

tá vendo aqui ó ele foi muito menorzinho porque esse é o de entrada da google né se eu for para um mais preparado 3 por exemplo 3x4 tal esses daqui possivelmente vão ser pagos a gente já olha eles pra vocês verem também mas aqui você consegue comparar imagina o colchão de água se você colocar uma bolinha de gude no colchão ele afundará um pouco certo então aqui ó ele tá sendo muito mais

19:38

resumido, porque ele é outro tipo de LLM mais barata, mais simples, foi treinado com menos tokens, então consegue dar até uma resposta menor. Agora, vamos pegar essa mesma aqui, que ela é mais simples do que a DeepSeek, e vamos deixar ela abrir para 1, para a gente ver o que acontece. A temperatura, possivelmente, ó. Ó, ela gerou mais coisa, beleza?

20:09

Imagine um trampolim gigante de espaço, se você colocar uma bola de bolinha no trampolim vai afundar um pouco, certo? Agora se você colocar algo muito pesado como uma montanha, uma montanha afundaria o trampolim muito mais, criando um buraco profundo. Um buraco negro é como essa montanha, um trampolim de espaço é um objeto com tanta massa concentrada em um espaço tão pequeno que a sua gravidade é extremamente forte. Essa gravidade é tão forte que nada, nem mesmo a luz consegue escapar. Aqui estão alguns exemplos, funil gigante, imagina um funil gigante de espaço. Então tá vendo que ele gerou um pouco diferente

20:38

E se eu pegar esse cara aqui e abrir pra dois? Vamos ver, a gente fez o teste, eu tô curioso, igual vocês aí pra ver o que acontece. Mas vai fazendo com várias. Olha que doideira, ficou malucaço. Colocou japonês com... sei lá se é japonês. Olha que doideira, coisa em cima da outra.

20:57

Ficou pior esse bobeado que o outro, porque ele não entendeu nada. Porque talvez ele é programado com menos tokens. Então ele alucina até mais. Agora vamos deixar 1 aqui e vamos ver até onde ele vai.

21:15

Você vê que ele vai menos, tá vendo? Ele escreve até menos coisas. Se você pegar o número de caracteres, parece que tá menor, tá? Eu não vou ficar lendo de novo, que você já deve estar cansado de ouvir eu lendo, mas é mais ou menos isso que acontece. Deixa eu tentar pegar só um pra vocês verem o que que ele faz quando é pago. Eu queria que vocês vissem isso pra vocês não se assustarem. Esse cara é pago? Esse cara é de graça também. Ele vai deixar... Eu achei que ele ia deixar cobrado.

21:41

Então, outra coisa legal pra vocês fazerem, vocês conseguem... Vocês viram que eu nem me atentei aqui de ficar mexendo. Tem vezes que ele vai pegar algum que pode dar erro, daí você muda aqui, tá? Mas por enquanto ele tá pegando os que tão funcionando. Normalmente é de graça qualquer... Deixa eu pegar o DeepSeek... O DeepSeek R1. Às vezes ele cobra.

22:07

não tá bom eu não tô achando nenhuma delas que pode gerar algum tipo de de pedido de upgrade então por enquanto as que estão aqui estão deixando você brincar em todas de cá mas o que vai acontecer é dar um pop-up falando que é da upgrade você vem aqui e fala que não quer e vem aqui muda para outra acontece pouco tá acho que aconteceu comigo umas duas vezes isso ou às vezes você vai dando play aqui uma hora ele pode dar um erro aqui no run

22:33

aparece aqui um errinho, aí você só fecha e continua. Vamos lá, então brinca, eu quero que você faça algumas brincadeiras aí. Uma, ficar mudando a temperatura com a mesma IA, outra você ficar trocando aqui a IA e compara entre uma e outra, sempre com a mesma pergunta, não muda o seu prompt para você poder

22:52

é ver qual a diferença de um então copia e cola ou deixa ele aqui colado e vai mandando para você ver é super importante para você como elas pensam para você ver como elas respondem qual o grau de profundidade de cada uma e você consegue já começar a comparar uma com a outra quando a gente perguntar ah mas a de psique é melhor do que a de m&i você pode falar cara as perguntas que eu fiz são muito parecidas então é importante você fazer isso para você conseguir comparar também e você vê por exemplo a grande diferença entre uma de psique e uma austral por exemplo

23:21

Vamos ver, essa aqui gerando. Já é lerdo né, possivelmente travou. Não, tá indo.

23:55

Olha que engraçado! Essa daqui ela deu uma resposta resumida, perto do que a gente viu na DeepSeek e na Gemini. Na Gemini 3 né, na 2 foi bem resumida também. E aqui ó, ele não abriu o Trinket pra você, não sei se você notou, ele não mostrou o que ele tava pensando. Então alguém já, a Austral já traz isso fechado, não deixou aberto pra você ver.

24:22

como foi o pensamento e ela já nichou ela usou a montanha-russa como ponto de entrada e foi levando tudo com a montanha-russa então tá vendo que ela é uma IA mais nichada para tratar um assunto de ponta do começo até o fim quando você colocar um de temperatura ela manda assim então é legal você fazer esse tipo de teste para você ver como é que tá

24:41

A Austral, perto da DeepSeek, como é que tá a Gemini e assim por diante também é bacana. Bem legal esse Playground da Hugging Face. Te dou essa dica aí de ficar testando, brincando um pouco. Vai te ajudar bastante a compreender como elas estão pensando por trás. Beleza? Já já a gente volta pra aprender um pouquinho mais. Um grande abraço. Falou!

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **LLM** — Large Language Model (Modelo de Linguagem de Grande Escala)
- **GPU** — não mencionada na aula
- **Playground** — ambiente de testes/interação com modelos, usado para experimentar prompts e parâmetros
- **Prompt** — comando ou instrução enviada ao modelo
- **Provider** — provedor/serviço que executa o modelo
- **Thinking** — etapa intermediária de “pensamento”/planejamento exibida por alguns modelos

**Resumo**
A aula mostrou como usar o Playground do Hugging Face para comparar o comportamento de modelos de linguagem de forma controlada. O instrutor explicou que, para tirar conclusões confiáveis, é importante manter a mesma pergunta e variar apenas um fator por vez, como a temperatura ou o modelo/provedor, evitando confundir diferenças de prompt com diferenças de geração. No Playground, o campo principal é usado para inserir a mensagem, enquanto o painel lateral concentra o modelo selecionado, o provider e os parâmetros de geração.

O foco central foi a temperatura e seu efeito na resposta do modelo. Com temperatura baixa, como 0,1, a saída tende a ficar mais estável, coerente e com menos desvios, sendo mais adequada para explicações técnicas e objetivas. Em 0,5, o modelo continua organizado, mas ganha flexibilidade lexical e alguma variação nas analogias. Em 1, a resposta passa a incorporar mais criatividade, metáforas e informações não solicitadas, o que pode ser útil em tarefas abertas, mas aumenta o risco de excesso e perda de foco. Já em 2, a geração pode degradar bastante, com incoerência, mistura de idiomas e texto desconexo, mostrando que a faixa prática de uso costuma ficar entre 0,1 e 1.

A aula também apresentou o campo Thinking em alguns modelos, que revela um planejamento intermediário da resposta, como a intenção de simplificar termos técnicos, escolher analogias e organizar tópicos. O instrutor destacou que nem todo modelo ou provider expõe esse campo, então sua ausência não significa ausência de raciocínio, apenas falta de visibilidade. Em seguida, foram comparados diferentes modelos e providers: alguns retornam respostas mais longas, outros mais curtas, alguns mostram Thinking e outros não, e alguns podem responder em outro idioma ou ter comportamento mais limitado. Também foi comentado que certos modelos ou rotas exigem plano pago, e que falhas no botão de execução podem ocorrer por instabilidade do provider ou do endpoint, devendo ser tratadas como problema de infraestrutura, não do prompt. No geral, a atividade proposta foi repetir o mesmo prompt, variar a temperatura e depois trocar o modelo para observar profundidade, estilo, idioma, robustez e presença de planejamento interno, transformando uma impressão subjetiva em comparação técnica reproduzível.

**Pontos de atenção**
- Manter o **mesmo prompt** ao comparar temperatura ou modelos; mudar o texto invalida a comparação.
- Variar **apenas um fator por vez**: primeiro temperatura, depois modelo, depois provider.
- Temperatura muito baixa tende a deixar a resposta mais previsível; muito alta pode gerar **alucinação, incoerência e mistura de idiomas**.
- A faixa prática sugerida na aula é, em geral, entre **0,1 e 1**.
- Em temperatura alta, o modelo pode incluir **informações não solicitadas** e perder o foco do pedido.
- O campo **Thinking** é útil para inspeção, mas sua ausência não significa que o modelo “não pensou”.
- Diferentes **providers** podem alterar o resultado, a estabilidade e até o idioma da resposta.
- Alguns modelos/rotas podem exigir **upgrade de plano**; isso é limitação de acesso, não erro conceitual.
- Erros no botão de execução no Playground costumam ser **falhas de infraestrutura**; tentar novamente ou trocar o provider é o procedimento esperado.
- Comparações confiáveis exigem **contexto de execução fixo**: mesma pergunta, mesmo cenário e parâmetros controlados.
- Modelos diferentes podem ter **profundidades e estilos distintos**, então não basta olhar apenas o tamanho da resposta.
- Em tarefas explicativas, priorizar **clareza e organização** antes de buscar criatividade excessiva.