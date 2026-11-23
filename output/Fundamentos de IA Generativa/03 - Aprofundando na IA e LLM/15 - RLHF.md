Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16386)

## Resumo da aula

Theoretical

RLHF combina Fine-Tuning com feedback humano para alinhar a saída do modelo ao que pessoas consideram útil, seguro e apropriado. Retomando o Fine-Tuning supervisionado já citado anteriormente, a novidade aqui é que o ajuste não depende só de pares fixos de entrada e saída: ele também incorpora preferências humanas sobre a qualidade das respostas. Isso permite controlar melhor estilo, aderência a instruções e comportamento do modelo em situações ambíguas. O objetivo não é apenas prever o próximo token, mas aproximar a resposta do que humanos avaliam como melhor.

SFT, ou Supervised Fine-Tuning, usa pares de pergunta e resposta escritos por humanos como exemplos de alta qualidade. Quando alguém fornece uma instrução como “explique a teoria da relatividade como se eu fosse uma criança” e escreve a resposta esperada, o modelo aprende o formato, o nível de detalhe e o tom desejado para esse tipo de pedido. Essa etapa cria uma base inicial de comportamento alinhado a instruções. Ela ainda não aprende preferências relativas entre respostas concorrentes; apenas imita exemplos considerados bons.

O Reward Model aprende a transformar preferências humanas em um sinal numérico de qualidade. Em vez de marcar uma resposta apenas como certa ou errada, humanos comparam múltiplas saídas para a mesma pergunta e as ranqueiam, por exemplo A melhor que C, e C melhor que B. Com isso, o sistema aprende padrões do que costuma receber notas mais altas, como clareza, utilidade e segurança. Essa etapa é importante porque muitas tarefas abertas não têm uma única resposta correta, mas várias respostas com qualidades diferentes.

Depois que o modelo de recompensa foi treinado, o ajuste por Reinforcement Learning usa esse sinal para otimizar o comportamento do modelo gerador. PPO, citado aqui como Proximal Policy Optimization, é o algoritmo usado para atualizar a política de geração de forma a maximizar a recompensa prevista sem alterar o modelo de maneira instável. Na prática, o modelo passa a favorecer respostas que o Reward Model considera mais úteis, seguras e claras. Essa etapa fecha o ciclo do RLHF ao transformar preferências humanas em atualização efetiva dos parâmetros.

Retomando o pré-treinamento autoregressivo já visto, um LLM aprende principalmente a prever o próximo token com base no contexto. Esse objetivo produz fluência linguística, mas não garante consistência lógica, concisão, segurança ou obediência a instruções do usuário. Sem alinhamento adicional, o modelo pode repetir vieses presentes nos dados, ser prolixo ou gerar conteúdo ofensivo. RLHF atua justamente nesse espaço entre “texto plausível” e “resposta desejável”.

Um modelo alinhado tende a admitir melhor quando não sabe algo, seguir instruções com mais precisão e reduzir alucinações. Também muda o tom de interação: respostas podem ficar mais respeitosas, menos agressivas e menos inclinadas a agradar o usuário a qualquer custo. Essas diferenças aparecem ao comparar versões de um mesmo sistema ou produtos distintos, porque pequenas mudanças no processo de alinhamento alteram bastante o comportamento percebido. O ganho principal não é conhecimento bruto, mas qualidade de interação e controle sobre a saída.

Quando o prompt é excessivamente social, com rodeios e tentativas de suavizar o pedido, o modelo pode interpretar que precisa priorizar agradabilidade em vez de objetividade. Um comando mais direto, com critérios explícitos e sem firulas, tende a reduzir prolixidade e diminuir respostas inventadas, porque restringe melhor o espaço de geração. Isso não substitui RLHF, mas interage com ele: o comportamento aprendido pelo modelo responde aos sinais que o usuário fornece no prompt. Em sistemas alinhados para serem prestativos, a forma do pedido influencia bastante o resultado.

Instruction Tuning pode ocorrer antes ou junto de RLHF para ensinar o modelo a responder bem a uma grande variedade de instruções humanas. Em vez de especializar o sistema em um domínio único, essa etapa amplia a capacidade generalista, como escrever uma carta de demissão em tom amigável ou criar um roteiro sobre IA. Retomando a ideia de modelos generalistas já discutida no capítulo, o ponto novo aqui é que a generalização é treinada explicitamente por tarefas formuladas como instruções. RLHF então refina quais dessas respostas são preferíveis do ponto de vista humano.

RLHF depende de julgamento humano, e julgamento humano é inevitavelmente subjetivo. Quando várias respostas são aceitáveis e muito parecidas, a escolha da “melhor” pode refletir preferência de estilo, vocabulário ou tom, não uma verdade objetiva. Além disso, o processo é caro, exige anotação humana e herda vieses de quem avalia. Essa limitação não invalida o método; apenas mostra que alinhamento também carrega valores e critérios humanos para dentro do modelo.

## Transcrição

00:00

Fala galera, beleza? Preparados pra aprender mais um pouquinho de Fine Tuning? Tem bastante conteúdo quando a gente tá falando de Fine Tuning, pessoal. Vamos aprender então de mais um pedacinho. Mas antes, deixa eu falar com você que tá aí. A gente não se conhece tanto porque eu tô aqui falando e você tá me ouvindo, então a gente ainda não tem proximidade. Se você tá curtindo a aula, se você tá gostando do conteúdo, tá gostando do que a gente tá trocando aqui de informação, deixa eu te pedir uma coisa.

00:25

Me adiciona lá no LinkedIn, vamos criar a conexão, deixa eu saber quem é você, deixa a gente se aproximar e criar essa rede que é super importante e super bacana para o nosso networking. Então, eu conto com isso, vai lá, clica no Linkedin, adiciona na tampa as parelifreitas e vamos criar essa conexão que é super importante para a gente, beleza? Vamos em frente, deixa eu te conhecer e vamos lá. Então, agora a gente vai falar um pouquinho sobre uma outra estratégia de finetuning, que chama RLHF.

00:50

O que significa o RLHF? Ele vai ser uma estratégia que ensina os modelos a seguir algumas instruções humanas. Então aqui você tem o humano junto com a interação de finetuning de máquina e de modelo lógico que a gente já falou. Então vamos entender como essa brincadeira vai funcionar. Então o que você vai ter basicamente é um finetuning que você já existe, já tem supervisionado. Só que agora com algumas instruções humanas vindo junto.

01:17

Então, você vai ter um aprendizado por reforço, guiado pelo feedback humano, para fazer essa máquina de aprendizado ser ainda melhorada. Então, você consegue ajustar como que esse modelo vai responder, não só com o que você já preparou de massa de dados, etc., mas também com a interação humana ali para fazer isso acontecer. E esse pipeline de RLHF,

01:41

Ele é super interessante, ele é quebrado basicamente em 3 etapas. Eu vou usar aqui o modelo de treinamento de GPT-4 como ideia, tá? Pode ser um pouco diferente disso, mas o GPT-4 pelo menos faz assim, acho que já ajuda a gente a entender como funciona. Se eu for falar de todos, a gente vai ficar com várias aulas sendo repetitivas, porque muda pouca coisa de um pro outro. Essas 3 grandes etapas vão estar em quase todos os modelos de treinamento que a gente tem com RLHF, tá?

02:09

O que a gente tem primeiro? A primeira etapa vai ser uma Supervisão de Fine Tuning. Normalmente vai estar em inglês, que significa SFT. Então, você vai ver essa sigla, SFT, que é Supervised Fine Tuning. Então, quando a gente está falando de SFT, o que significa? O humano vai escrever ali pares de perguntas e respostas de qualidade. Então, ele vai fazer assim... Essa pergunta, quando eu fizer essa pergunta, essa é a resposta esperada com qualidade. Então, vai fazer aquela resposta super bem escritinha. O modelo vai ser treinado com esses exemplos.

02:38

Então ele vai entender que quando vier uma pergunta desse tipo, ele vai conseguir responder diretamente as instruções dado que ele tá tendo ali de pergunta e resposta. Então ele tem um feedback direto, cara, normalmente é isso que se espera da minha resposta. Então eu vou te dar um exemplo, você vai ter lá um input

02:54

uma pergunta que vai ser me explique a teoria da relatividade como se eu fosse uma criança a resposta disso o output vai ser um humano fazendo uma explicação simples e clara de como funciona o modelo da teoria da relatividade como se fosse para uma criança então você vai lá escrever um textão funciona assim beleza deu essa resposta como se você fosse uma criança

03:16

O resultado disso vai ser o modelo entendendo que este tipo de formato de resposta é importante quando vier este tipo de formato de pergunta. Então você conseguiu dar para este modelo a melhor resposta possível que um humano criaria para ele conseguir aprender. Então ele está aprendendo basicamente com um dado que o humano está gerando para esta especificidade, beleza?

03:40

O segundo passo que a gente faz é o treinamento que a gente chama de Reward Model, que é o treinamento com base em recompensa, tá bom? Então, é basicamente uma ideia de recompensar quando tiver indo para o caminho certo. Então, dado o conjunto que a gente tem ali de respostas que foram geradas pelo modelo, o humano lá, chegou um ser humano e vai classificar, beleza. Então, eu fiz a pergunta, aí o modelo foi lá e eu fiz a mesma pergunta, eu fiz a pergunta lá ó, explique a teoria da relatividade para uma criança.

04:09

A resposta A, resposta B e resposta C. O ser humano vai chegar lá e vai dar uma nota pra cada uma dessas. Ele vai classificar. A A foi nota 10.

04:22

A B foi nota 5 e a C foi nota 7. Ou seja, você classificou. Para esse modelo, a partir de agora, ele vai entender que as melhores respostas estão ranqueadas assim. A, C e B. Então, ele está vendo que a resposta dele, por exemplo, C foi melhor do que a B. Então, a B no ranking foi para um caminho pior do que as outras duas respostas.

04:44

não significa que essas respostas são erradas você classifica qual que é a melhor qual que é a segunda e qual que é a terceira melhor assim por diante com isso ele vai entender que ele tem uma recompensa quando ele acerta então assim ele vai compreender que aquele modelo de respostas que foi o que você deu o maior ranking vai ser o melhor que tem entendeu? é mais ou menos assim você tá rankeando qual que tá melhor então esse é o segundo passo desse treinamento

05:12

supervisionado que a gente está fazendo aqui. E depois tem um terceiro passo, que chama RL com PPO, beleza? Mas vamos falar do RL primeiro, Reinforcement Learning. O que significa? Ele vai pegar o modelo original que ele tinha, só que agora ajustado com as bases que a gente previu e organizou ali com a parte do modelo de Reward Model ali.

05:36

com o modelo que a gente acabou de falar de recompensa, beleza? Então, com esse modelo de recompensa, ele teve essa estratégia ajustada. Então, o que você vai fazer? Vai usar esse PPO que chama Proximal Policy Optimization. Nossa, demorou pra ser proximal. Proximal Policy Optimization. Nossa, meu inglês tá difícil hoje. Proximal Policy Optimization.

06:02

Esse carinha aqui, ele vai fazer o que? A meta dele vai ser gerar uma resposta que maximize a recompensa prevista. Então a partir desse momento ele vai pegar as respostas mais úteis, as seguras e as claras e colocar como as primeiras que ele tem que fazer. Então ele vai aumentar a recompensa para o próximo nível. Então com isso você acabou fazendo

06:25

3 camadas, a ultima dela vai ser o reforço de aprendizagem e com isso você vai deixar o seu fine tuning melhorado, beleza? E por que que é importante esse tipo de fine tuning aqui, tá?

06:41

O modelo de LLM não vai ter uma consistência lógica, se você parar para pensar. Ele tem um modelo de aprendizagem por palavra. Então, qual é a próxima palavra? Qual é a próxima palavra? Qual é a próxima palavra? Ele está tentando fechar uma análise gramatical de evolução textual. Ou seja, ele pode não entender muito claramente para que caminho ele está indo. Ele vai estar falando só de tentar decifrar ou descobrir qual a próxima palavra.

07:10

Então, se você não tiver o ajuste, o que ele pode fazer? Ele pode, por exemplo, reproduzir viés de dado, que a gente falou anteriormente. Ele pode pegar dados enviesados, reproduzir e falar uma grande besteira. Ele pode ser prolixo, começar a gerar um monte de informação repetida. Isso aconteceu no começo do ChatGPT, quando lançou, não sei se vocês se lembram. Ele era prolixo, um pouco impreciso, ele ficava repetindo várias vezes as mesmas coisas.

07:34

Ele dava uma viajada ali, era um pouco mais difícil. Depois ele foi tendo mais Tuning, mais TOKENS entrando no GPT-4. Agora ele tá sensacional e assim por diante. Então aqui você nota que ele começa a ter essa dificuldade. Ele vai ser prolixo, vai ser impreciso se você não tiver esse Fine Tuning.

07:52

E ele pode também fazer uma outra coisa que também aconteceu, todo mundo viu isso acontecendo. Ele gerar conteúdo inseguro ou ofensivo. Quantas vezes a gente não viu saindo na mídia, e a tal empresa estava usando uma I.A. e ela ofendeu, ou ela gerou alguma coisa de racismo, de ofensa a minorias, e assim por diante, que a gente não quer, a gente acha que isso não pode acontecer, e a I.A. reproduziu, porque infelizmente, nas bases utilizadas isso apareceu, porque o ser humano é horrível.

08:20

e a gente acaba tendo isso nas nossas bases de dados que foram replicadas durante anos e isso acabou gerando essa poluição no treinamento dessas IAs. Aí você faz o fine tuning e limpa isso e daí com isso você para de ter isso. Então é super importante você fazer isso com as LLMs pra você deixá-las melhoradas, tá bom? Então o RLHF aqui ele vai atuar como se fosse uma bússola ética

08:47

guiando o modelo para ter certeza que esse modelo vai ser mais educado, que ele vai ser mais respeitoso e assertivo. Se você pegar outro comparativo aqui ó, GPT, faz esse teste, GPT de psique faz a mesma pergunta. Você vai ver que cada um tem um nível de educação, de respeito, etc. O jeito como ele te trata já é diferente. Duas outras coisas, dentro do próprio GPT, pega o GPT

09:12

Não pago, eu pago. Você vai ver que eles já mudam. Você pega o GPT mais antigo. Quando o GPT lançou, ele era de um jeito nessa visão de ser respeitoso, etc. Aí teve uma atualização do GPT que deixou ele extremamente chato. Ele virou um puxa-saco. A galera errou a mão pra cima. Puta, vamos deixar esse cara muito puxa-saco.

09:33

Aí agora veio uma atualização que ele ficou mais comum, vamos ser bem honestos. Então ele ficou um pouco menos puxa saco. Ele começa já a falar que ele não sabe de tal assunto, etc. Antes ele respondia qualquer coisa só pra te agradar. Ainda faz isso. Inclusive daqui a pouco eu vou dar uma dica pra vocês, mas ele ainda faz isso.

09:49

só que você consegue já começar a diminuir e a reduzir isso com base nesses treinamentos, tá? Então, por exemplo, acabei de falar pra você, ele dizer o que ele não sabe, quando for mais apropriado, você consegue fazer isso com base em Finetuning, ele seguir melhor as instruções do usuário, ao invés de querer ficar inventando, ele seguir o que você tá promovendo, e evitar alucinação, porque ele vai ter mais instrução, menos chance dele alucinar ao longo do percurso aqui. O que que eu vou falar pra vocês? Não sei se vocês já notaram,

10:17

Mais uma dica que eu dou.

10:20

A gente as vezes fica com uma brincadeira lá de ter que dar bom dia pra torradeira, ter que falar boa noite pro liquidificador, pra máquina de café, etc. Eu acho engraçada essa brincadeira, inclusive eu também faço ela falando, poxa, um dia vai ter aqui um maiá que vai dominar tudo, e daí se ela dominar tudo eu não quero que a minha cafeteira queira me matar, e etc. Brincadeiras à parte. Mas o que que acontece? Quando a gente tá falando de um chat ali que ele é de generativo textual, então um chat de PT, de psique, etc.

10:49

E eu tenho notado, eu tenho feito muitos testes quanto a isso, que quando você trata ele de uma forma muito educada, e aqui muito educada eu estou pedindo por favor, faça isso, aquilo, aquilo outro... Talvez você não tenha ido para o caminho correto e tal, ele te dá um nível de resposta. E aqui é só achômetro, é só o que eu estou testando.

11:10

Quando você trata ele mais diretamente, sem tanta firula, e pede pra ele te dar dados reais, diretos, direcionados, sem tentar te convencer, sem tentar te agradar, ou seja, você está dando a direção pra ele que não é pra ele entrar nessas camadas de te agradar e etc. Eu sinto que ele responde melhor o que você está pedindo, ele não viaja tanto, não fica tão prolixo, não fala tanta besteira, não inventa... Então, quando você fala com ele de uma forma mais direta, como se você estivesse falando com...

11:40

Não como se você estivesse falando, por exemplo, com um amigo ou com uma pessoa da sua equipe, assim por diante. Falando mesmo como se você estivesse falando com uma máquina. Cara, eu quero isso, isso e isso. Diretamente. Normalmente vem uma resposta melhor. Pelo menos eu tô ouvindo bastante isso. Queria te ouvir também. Se você fizer esse teste, me conta o que você tá achando. Aproveita que você me adicionou lá e me conta o que você tá achando disso. Mas eu tenho sentido isso, tá? Fica aqui uma dica pra vocês testarem e ver se funciona também. Voltando pro...

12:08

Voltando para a aula, olha que parênteses gigantes que eu abri, perdão minha gente, vamos voltar para a aula. Vamos falar então de instrução de Tuning, que é um passo complementar no meio desse caminho aqui de Fine Tuning. Então, antes ou junto com o RLHF, você pode fazer uma instrução de Tuning, tá bom? Você pode passar por um modelo ali, pegar o seu modelo e passar ele por uma instrução de Tuning.

12:33

O que significa? Você vai treinar ele com várias instruções humanas para diversas tarefas, então você vai dar um monte de instrução para ele conseguir ser mais generalista e fácil de usar. No caso do GPT-4, por exemplo, ele precisa ser generalista. Se você estiver falando de uma

12:48

de um fine tuning lá pra você deixar a sua IA mais especialista em um determinado assunto, talvez não seja essa conversa. Mas como a gente tá falando do chat GPT-4 como exemplo, no nosso caso, a gente tá falando de um cara generalista. Então, você colocar essas instruções de tuning vão te ajudar. Então, por exemplo, você pode pegar

13:08

Esse tipo de instrução para fazer o chat GPT-4, por exemplo, ser capaz de responder alguma coisa do tipo assim... Escreva uma carta de demissão, mas em um tom amigável. Ou crie um roteiro para um podcast de IA. Aí com isso ele consegue evoluir quando você dá essas instruções de Tuning. Então o RLHF, ele é super interessante para a gente usar e fazer isso acontecer, mas ele tem algumas limitações também, tá? Primeiro, ele vai depender do ser humano.

13:38

E o ser humano é falho. Então, vai ter subjetividade. O ser humano vai colocar a subjetividade em dado, aquela tomada de decisão, qual é a resposta melhor, qual é a pior, etc. Se for uma resposta alucinada, qual era o nosso exemplo ali? Explique a teoria da relatividade para uma criança. Aí imagina que veio na resposta A. Olha, a teoria da relatividade é como se fosse uma casa de Barbie com o boneco do Ken saindo de carro.

14:08

Tem nada a ver com a teoria da relatividade, certo gente? Não explicou nada. Essa tá muito clara que é uma porcaria, mas às vezes vai vir três respostas muito próximas. E eu não consigo explicar a teoria da relatividade pra uma criança, sendo bem honesto. Eu tenho dificuldade de explicar pra um adulto, apesar dela ser extremamente simplificada.

14:25

Dá pra explicar de forma simplificada, mas não é tão simples de entender. A galera inclusive tem o costume de usar mal, mal demais, falando que tudo é relativo, não tem nada a ver com isso, tá? Mas, eu não vou nem tentar explicar aqui pra uma criança que eu não pensei nisso, vai sair horrível, vou até ser xingado por vocês, não vou tentar, mas imagina que saiu três respostas muito parecidas. Nessas três respostas muito parecidas, o que vai acontecer? O ser humano vai chegar e falar, cara, essa eu gostei mais do que essa, do que daquela. Cara,

14:54

eu não consigo decidir o que é melhor mesmo, que é subjetivo, cada ser humano vai achar uma melhor, pode ser que uma alisou um tom melhor, uma palavra que eu conheço mais, ou assim por diante, um jeito que eu gostei mais, porque eu tenho que achar um critério para isso. Então a subjetividade vai gerar um certo impacto ali, que na minha opinião

15:16

É certamente positivo, porque a gente é subjetivo e a nossa linguagem, a nossa resposta é subjetiva. Então, os chats que a gente fala todos no GPT como exemplo, porque é o mais conhecido, mas todos os geradores textuais, etc. Eles precisam ser o mais próximos possível, só que talvez com uma gama de conhecimento melhorada, uma base de conhecimento melhorada. Então assim, eu não acho ruim, sendo bem honesto, eu não acho isso um problema, mas isso acontece. Custo caro,

15:45

E ele vai ter viés, porque também, como um ser humano tem viés, então você vai acabar jogando isso pra ele também.

## Resumo IA

**Abreviações**
- **RLHF** — *Reinforcement Learning from Human Feedback* (Aprendizado por Reforço com Feedback Humano)
- **SFT** — *Supervised Fine-Tuning* (Ajuste Fino Supervisionado)
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **PPO** — *Proximal Policy Optimization* (Otimização de Política Proximal)

**Resumo**
A aula apresentou o RLHF como uma estratégia de fine-tuning que combina ajuste supervisionado com feedback humano para alinhar o comportamento de modelos de linguagem ao que as pessoas consideram útil, seguro, claro e apropriado. O instrutor explicou que, diferente do pré-treinamento autoregressivo, cujo objetivo é apenas prever o próximo token, o RLHF busca aproximar as respostas do modelo de preferências humanas, melhorando instruções, tom, aderência ao pedido e reduzindo comportamentos indesejados.

O fluxo foi dividido em três etapas principais. Primeiro, o **SFT** usa pares de pergunta e resposta escritos por humanos para ensinar exemplos de alta qualidade e formar uma base inicial de comportamento orientado a instruções. Depois, o **Reward Model** aprende a transformar comparações e rankings humanos entre múltiplas respostas em um sinal numérico de qualidade, identificando quais saídas são preferidas em termos de utilidade, clareza e უსაფრთხidade. Por fim, o **Reinforcement Learning** usa esse modelo de recompensa, com destaque para o algoritmo **PPO**, para atualizar a política de geração e favorecer respostas com maior recompensa prevista.

Também foi abordado o **Instruction Tuning** como etapa complementar, ocorrendo antes ou junto do RLHF, para treinar o modelo em uma variedade de instruções humanas e aumentar sua capacidade generalista. O instrutor relacionou esses processos com melhorias observáveis em LLMs, como maior capacidade de seguir instruções, admitir limitações, reduzir alucinações, evitar conteúdo ofensivo e apresentar um tom mais respeitoso. Como exemplo prático, comentou que prompts mais diretos e objetivos tendem a gerar respostas melhores do que pedidos excessivamente “sociais” ou cheios de rodeios, pois restringem melhor o espaço de geração. Ao final, destacou que o RLHF depende de julgamento humano e, por isso, carrega subjetividade, custo elevado e possíveis vieses das pessoas que realizam a avaliação.

**Pontos de atenção**
- O RLHF não substitui o pré-treinamento; ele atua no alinhamento do modelo depois da aprendizagem baseada em próximos tokens.
- **SFT** ensina por imitação de exemplos bons, mas não compara preferências entre respostas concorrentes.
- O **Reward Model** depende de rankings humanos; a tarefa não é marcar “certo/errado”, e sim ordenar qual resposta é melhor.
- O uso de **PPO** precisa evitar atualizações instáveis, buscando maximizar a recompensa sem “destruir” o comportamento aprendido.
- Sem alinhamento adicional, LLMs podem ser prolixos, imprecisos, enviesados ou produzir conteúdo inseguro/ofensivo.
- O modelo pode melhorar ao seguir instruções, admitir que não sabe algo e reduzir alucinações, mas isso depende do treinamento e da forma do prompt.
- Prompts muito indiretos, sociais ou cheios de rodeios podem incentivar respostas mais longas, menos objetivas ou mais “agradáveis” do que corretas.
- Prompt mais direto e com critérios explícitos tende a orientar melhor a geração.
- **Instruction Tuning** é especialmente útil para modelos generalistas; em modelos especialistas, a estratégia pode ser diferente.
- RLHF depende de julgamento humano, portanto sofre com subjetividade: respostas muito parecidas podem ser avaliadas de forma diferente por pessoas diferentes.
- O processo é caro e carrega viés humano para dentro do modelo, o que deve ser considerado no desenho do treinamento.