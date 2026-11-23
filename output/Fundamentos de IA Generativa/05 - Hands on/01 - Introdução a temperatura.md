Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16394)

## Resumo da aula

Temperatura é um parâmetro de controle de geração que altera o grau de aleatoriedade aplicado à distribuição de probabilidades do próximo token. Um modelo de linguagem não escolhe a “palavra certa” de forma determinística; ele estima quais tokens são mais prováveis dado o contexto atual e seleciona a continuação a partir dessa distribuição. Esse parâmetro importa porque a mesma entrada pode produzir saídas mais previsíveis ou mais variadas, dependendo de quanto espaço se dá para opções menos prováveis. Em termos práticos, temperatura baixa favorece continuidade conservadora; temperatura alta amplia diversidade e risco de respostas inesperadas.

Quando o modelo recebe uma frase incompleta como “O cachorro hoje latiu no...”, ele precisa prever qual token vem a seguir. Essa decisão não é binária nem exata: o modelo atribui probabilidades a várias continuações possíveis e escolhe uma delas com base nesse ranking probabilístico. O próximo token pode ser uma palavra inteira, parte de palavra ou símbolo, dependendo da tokenização do modelo. A temperatura atua exatamente nesse ponto, achatando ou acentuando a distribuição antes da escolha.

Na faixa baixa, como 0,1 a 0,3, o modelo tende a privilegiar os tokens de maior probabilidade e reduz a chance de desvios criativos. Isso é útil quando a saída precisa ser previsível, técnica e conservadora, como em textos jurídicos ou respostas em que precisão importa mais que originalidade. O ganho é consistência; a perda é variedade. Se a tarefa exigir expressão artística, essa configuração tende a produzir resultados pobres ou excessivamente rígidos.

Na faixa alta, como 0,7 a 1,0, a distribuição fica mais aberta a tokens improváveis e a saída ganha diversidade lexical e estrutural. Esse comportamento favorece brainstorm, poesia, música e outras tarefas em que surpresa e exploração são desejáveis. O custo dessa liberdade é a redução de previsibilidade e o aumento da chance de escolhas menos adequadas ao contexto. Em aplicações sensíveis, elevar a temperatura sem critério pode degradar a qualidade factual e técnica da resposta.

Uma forma intuitiva de entender temperatura é imaginar um especialista dentro de uma biblioteca. Com temperatura baixa, ao pedir referências jurídicas, ele vai direto ao Vade Mecum porque a escolha mais provável domina a decisão. Com temperatura alta, esse mesmo especialista passa a considerar livros menos relacionados e pode retornar com opções improváveis, como literatura infantil ou fantasia. A metáfora mostra que temperatura não adiciona conhecimento novo ao modelo; ela altera o quanto ele se afasta do caminho mais provável.

O Hugging Face Playground é um ambiente web para testar modelos e ajustar parâmetros de geração sem precisar começar por código. Ele permite observar rapidamente como mudanças em temperatura afetam a resposta para o mesmo prompt, o que o torna útil para experimentação inicial. Como este parâmetro será reutilizado junto com janela de tokens e top-k/top-p, o Playground funciona como base operacional para comparar comportamentos. O objetivo aqui é validar visualmente que o controle de geração altera a escolha do próximo token.

Para usar o Playground autenticado, é necessário criar uma conta no Hugging Face e gerar um token de acesso nas configurações da conta. Esse token funciona como uma credencial que autoriza o uso da plataforma e libera o ambiente de teste após o login. O fluxo básico é: acessar huggingface.com/playground, fazer cadastro ou login, confirmar o e-mail e depois criar um token em huggingface.com/settings/tokens. Após copiar o token e submetê-lo no Playground, a interface principal fica disponível para experimentação.

Abra huggingface.com/playground e ignore inicialmente a solicitação de token, porque o primeiro passo é autenticar a conta. Se ainda não houver cadastro, crie usuário, senha e username; em seguida, confirme o e-mail para liberar a geração de credenciais. Depois acesse settings/tokens, crie um novo token, copie o valor gerado e cole no campo solicitado pelo Playground. Com isso, a interface passa a exibir os controles laterais, incluindo o parâmetro de temperatura que será usado nos testes.

Ao alterar a temperatura no Playground, você não está “mudando o assunto” do modelo, mas ajustando a política de escolha entre tokens prováveis e improváveis. O experimento mais útil é repetir o mesmo prompt em diferentes valores, como 0,1 e 1,0, para observar a diferença entre precisão e criatividade. Retomando a frase incompleta e a metáfora da biblioteca, o comportamento esperado é simples: valores baixos aproximam a resposta do caminho mais previsível; valores altos aumentam a abertura para alternativas inesperadas. Esse é o primeiro mecanismo concreto de controle de geração em LLMs.

## Transcrição

00:01

Fala galera, beleza? Quero falar com vocês agora de um tema novo. Vamos falar um pouquinho sobre temperatura. Bom, quando eu tô falando de temperatura eu não estou falando do tempo, do clima, se tá sol, se tá chuva. Inclusive hoje tá um dia horrível, um dia frio, um dia nublado e assim por diante. Mas não é disso que a gente tá falando.

00:22

Quando estou falando de temperatura não tem nada a ver com o clima. Quando estou falando de temperatura então você deve estar pensando, pô Natan, temperatura olhando pra LLM deve ser a temperatura lá do GPU, da GPU processando, deve estar quente pra caramba né, porque afinal tem que processar um monte de tokens ali, modelos e tal.

00:41

Não é também. Temperatura é algo super específico e importante pra quando a gente tá falando dos contextos de LLM. O que ele vai fazer? Pensa no seguinte, um modelo, por exemplo, de EPT, ele vai precisar gerar um texto. Quando ele tá gerando um texto, então tudo isso que a gente falou lá, lembra? Big Drama, blá blá blá, voltando tudo aquilo que a gente já falou. Chegamos nos Transformers. Os Transformers, eles vão fazer o seguinte, imagina que eu tenho aqui uma frase. O cachorro hoje latiu no quintal.

01:10

O cachorro hoje latiu no quintal. O quintal ele não tem. Então, ele sabe que o cachorro hoje latiu no... Não sabe o quintal. Ele vai ter que, então, falar qual é a próxima palavra, certo? Então, ele vai fazer esse cálculo para decidir quais são os vetores e decidir qual é a palavra, como a gente falou anteriormente. Então, ele vai decidir qual é a palavra correta, certo?

01:33

errado, brincadeiras, mas pensa o seguinte, não é bem assim, ele não decide com a palavra certa, ele decide com a palavra mais próxima de ser a correta, porque é probabilidade, ele não é uma matemática exata, exata, exata, ele é mais probabilístico.

01:50

Então, como ele vai em cima de probabilidade, ele vai pegar qualquer palavra que possivelmente você vai entender como correta. Então, em cima disso, ele vai ter esse cálculo de qual o próximo token, qual o próximo pedaço de palavra, qual o próximo símbolo que ele vai te mostrar. Tá bom?

02:07

Mas pense que para fazer isso ele tem algumas formas de fazer. Quando a gente está falando da temperatura, ela consegue te ajudar a controlar isso. Então você pode controlar ela por algumas estratégias de amostragem que podem influenciar qual é a tomada de decisão dele para desistir com a palavra correta. Então você pode por exemplo falar, poxa eu preciso de uma LLM que ela seja mais criativa.

02:28

Ou eu preciso de uma que seja mais conservadora? Não. Eu preciso de uma LLM que ela precisa ser mais precisa ou mais surpreendente? Depende. Depende do que você vai fazer. Quero mais fluente ou mais técnico? Depende do que você vai fazer.

02:44

Eu quero ela mais criativa? Porque a gente fala, olha, a IA não consegue criar. Eu quero ela mais criativa? Depende. Se eu for fazer um texto jurídico, possivelmente, eu não vou querer ela muito criativa. Nem quero que ela me surpreenda e nem quero que ela vá por uma linha fluente. Eu quero que ela seja mais técnica, eu quero que ela seja precisa, eu quero que ela seja conservadora. Então, quando eu tô falando de um texto jurídico, essa é a ideia.

03:07

Aí você fala, poxa, então eu sempre quero isso. Não! Você precisa criar um poema, por exemplo, um livro, escrever uma música. Eu preciso que ela seja criativa, eu preciso que ela seja surpreendente. Então eu vou ter que ir pro outro lado. Então quando a gente tá falando de temperatura, ela vai ajudar a gente a ficar chaveando nesses caminhos de pra onde a gente quer que a nossa LLM ande.

03:25

O que vai acontecer por trás dos panos? Ela vai fazer o cálculo dos vetores e na hora de dar tomada de decisão, ela vai dar abertura por inesperado. Quanto maior a temperatura, mais ela dá abertura. Quanto menor a temperatura, menos ela dá essa abertura. Então, essa é a grande sacada aqui. Então, pense o seguinte, a função dessa temperatura é dar um tom de aleatoriedade à distribuição de probabilidades que ela está trazendo. Então, antes dela te entregar,

03:54

ela vai liberar alguma certa aleatoriedade nas trocas dentro dos vetores que ela está criando e dentro de toda a camada dos transformers ali. Então, vamos lá. Imagina que você tem a temperatura, ela normalmente vai ser de 0,1 até 1,0, tá bom? Então, ela roda dentro disso. De 0,1 até 1,0, subindo de 0,1 a 0,1. Então, você tem

04:19

0,1, 0,2, 0,3, 0,4, 0,5, 0,6, 0,7, 0,8, e assim por diante. Até 10. Quando você chegar no 10, você vira 1, tá bom? Então, pense que é mais ou menos isso. Você tem 10 espaços, mais ou menos, para trabalhar ali.

04:35

Se você estiver numa baixa temperatura, então vai ser de 0.1 a 0.3. Aqui é a baixa temperatura. O que ela vai fazer? Ela vai reduzir a aleatoriedade, não vai deixar ela dar uma viajada. Ela vai ser mais precisa, como eu falei pra vocês. Pô, que era um texto jurídico, como eu falei. Preciso disso. O modelo, ele vai tender a escolher ali os tokens que tem maior probabilidade, sem dar abertura pra uma aleatoriedade na distribuição que ele tá fazendo. Então ele vai ser ideal pras coisas que a gente falou aqui. Coisas previsíveis, técnicas, etc.

05:04

Se eu colocar ele para escrever um poema com base em uma LLM com uma temperatura de 0.1, possivelmente vai vir uma porcaria. Então, quando você está indo para uma visão um pouco mais criativa, você tem que trabalhar entre 0.7 e 1.0 e assim por diante. Então, você vai aumentar a diversidade quando estiver entre 0.7 e 1.0, porque a temperatura está alta.

05:29

E daí ele aumenta a diversidade, ele libera mais essa aleatoriedade. Então ele vai ser mais propenso a escolher palavras que são improváveis. Ele vai ter texto mais criativo, é bom pra brainstorm, pra uma coisa mais artística e assim por diante.

05:43

Então pensa o seguinte, imagina que o seu Transformer, sua LLM, ela é uma... um especialista entrando numa sala, e você fala pra ele, olha, eu preciso que você busque pra mim todos os itens jurídicos. Ele vai olhar pra sala ali, pra biblioteca, vai falar, putz, pros itens jurídicos o melhor é aquele livro ali, o Vad Mekon que eu tô vendo, é ele que vai me ajudar nisso. Então ele já sabe, vai direto e não vai dar abertura.

06:10

Se você fizesse a mesma pergunta pra esse mesmo especialista numa sala e der um grau de aleatoriedade dele de 1.0, ele tá capaz de te votar com o livro do Monteiro Lobato.

06:20

com, sei lá, um livro do Harry Potter pra você. Então, ele vai dar um quê de aleatoriedade. Eu chutei o balde aqui, mas vai ter um quê de aleatoriedade. Acho que esse é um jeito fácil da gente entender. Mas vamos aprofundar mais? Eu quero fazer um rendizão com vocês pra vocês verem na prática como que eu mexo com a temperatura e como que vocês podem entender ela funcionando. A gente vai fazer alguns

06:42

testes ali juntos pra vocês conseguirem entender mais a fundo, beleza? Vamos pro hands-on? Alguns minutinhos e eu já volto com você só o tempo de eu trocar câmera aqui e abrir as páginas pra gente conseguir olhar junto ali o como é que a gente faz essa brincadeira, tá bom? Até já já!

07:00

Fala galera, então a gente vai começar agora a fazer o hands-on pra entender como funciona essa temperatura, tá bom? E nesse hands-on a gente vai então usar essa plataforma aqui, chama Hugging Face. Como que a gente vai fazer? Primeiro eu quero que vocês entrem nesse link aqui, huggingface.co.br joga lá.

07:19

Eu vou deixar aqui também para vocês poderem copiar, mas é huggingface.com barra playground. Dentro desse huggingface.com barra playground, você vai ter que fazer algumas coisas. Está vendo que ele já começa pedindo um Face token? Nem olha para essa janela por enquanto, vamos ignorar ela. Primeiro, vamos fazer um login. Eu abri aqui até uma aba anônima para não entrar direto na minha conta. Vamos entrar em uma conta nova aqui. Eu não tenho endereço, certo? Então, eu preciso primeiro me cadastrar.

07:50

Primeiro ele vai ver se eu sou humano, vai que eu não sou, escura todas as cortinas. Olha, se eu errar isso aqui é capaz dele falar que eu não sou humano. Acho que é que isso aqui é cortina, aquilo ali parecia ser um saco. Então vamos colocar aqui um e-mail, Natan, arroba natanpf.com, uma senha.

08:10

Escolhe sua senha aí, você que manda. Next. Username. Aqui o username você vai ter que colocar algum tipo de usuário que não exista. Então, por exemplo, o meu já tem natanpf. Natanpf2. Super criativo. E depois eu vou colocar o meu nome direto. Vamos lá.

08:31

o avatar eu posso deixar, não preciso colocar nada disso aqui, isso aqui você coloca só se você quiser tá, você não precisa colocar, você pode colocar, eu não vou colocar nada disso aqui não tá, upload file, eu não quero por avatar, não quero por nada disso aqui, nada é coisa desnecessária bom, eu aceito, porque se eu não aceitar eu não consigo criar, criei, e ele vai querer um avatar de qualquer jeito, eu posso escrever aqui quem eu sou e tal tal tal, qualquer coisa, mas eu vou deixar ele fazer alguma coisa aleatória aqui ó, eu cliquei no dadinho

08:58

só pra ele gerar um avatar, porque ele é chato. Posso até pular aqui, mas vamos pôr um avatarzinho, vai. Pensa aí, jovem. Vai vir algum avatar bem zoado, normalmente vem umas coisas nada a ver. O meu outro é uma águia. Esse aqui ficou horrível também, mas vai ser esse mesmo. Vamos lá. Vamos criar nossa continha aqui. Criei a conta.

09:17

Ixi, tem uma porrada de tralha aqui, depois eu ensino vocês a mexer melhor aqui, porque tem coisa legal pra caramba pra vocês fazerem aqui. Mas ó, então ó, tá vendo que ele tem learning, uma porrada de coisa legal, depois a gente... Eu até mostro pra vocês, porque é uma página bem legal de vocês ficarem brincando, tá? Mas vamos lá, o que a gente quer fazer aqui ó, cadê o meu...

09:38

Playground. Vocês vão vir aqui no Playground, tá vendo? Playground. Cliquei no meu Playground. Aí ele tá pedindo um token. Agora a gente entra naquele pedaço. Token.

09:49

Vamos entrar então nesta outra página, huggingface.com barra settings barra tokens. Vamos criar um token. Agora que eu já estou logado, ele já entra direto. Por isso que eu até deixei aqui já preparado só para eu dar enter, a gente já entra direto e não ia ter que logar tudo de novo. Então vamos lá. Eu preciso ter um token. Vamos criar um novo token. Cadê?

10:12

Eu preciso mandar um e-mail de confirmação, muito legal. Então eu vou ter que abrir aqui meu e-mail. Vamos fazer o seguinte, eu vou só abrir meu e-mail de confirmação, vou dar uma pausa no vídeo pra confirmar o e-mail. Depois de confirmado, eu volto aqui pra gente abrir o Token, tá bom? Então eu só preciso confirmar lá no e-mail.

10:29

Vocês também vão receber um e-mail de confirmação, mas como o meu não está aberto, vai demorar muito tempo aqui para eu abrir para vocês, eu vou dar uma pausa e já volto com o e-mail confirmado. Então, vocês vão receber o e-mail, clica no linkzinho, vai confirmar que é você mesmo, aí aqui vai voltar para uma outra tela onde vai deixar você criar o token, tá bom? Bom...

10:47

Consegui voltar aqui, ele já me aprovou, tudo certo e eu fui lá no Create New Token, certo? Vamos ver se eu volto aqui. Então, a gente estava nessa telinha, quando ele foi lá e me perguntou se eu tinha validado meu e-mail, eu validei meu e-mail, espero que você tenha validado o seu também. Depois eu venho aqui ó, Create New Token. Se você perdeu o link aqui no Playground, fica aqui ó, Create New Token. Você pode clicar aqui também e vai vir no mesmo lugar, ó, vamos clicar junto. Veio para o mesmo lugar.

11:16

Tá? Pô, quero voltar. Volta aqui e create new token, tá bom? Então, você consegue ficar brincando aqui. Tá bom. Eu quero um token que me libere tudo. Então, eu vou vim aqui, vou flegar tudo isso aqui, eu não vou ficar explicando para vocês este ponto agora, porque depois a gente vai fazer com mais calma o aprendizado sobre o Hugging Face em um outro momento. Para agora, porque a gente precisa, eu só vou deixar ele liberado para fazer tudo, tá vendo? Então, dei permissão para este usuário fazer qualquer coisa.

11:46

é que o resto você não precisa pôr, tá vendo? Então daqui ó, repository permissions, tudo isso aqui você não precisa porque a gente vai fazer. A gente vai usar ele de forma bem simplificada aqui. Opa, token name, aula 2. Sei lá, só porque ele falou 1 eu não quero pôr 1. Create token, tô criando token. Criou, beleza, copy.

12:07

Token copiado, eu venho aqui e colo, beleza? Submit. Entrei na minha página principal. Então agora eu já tenho acesso ao Hugging Face. A próxima coisa que a gente vai fazer é, eu vou mostrar pra vocês um pouquinho como funciona esse Playground, tá bom?

12:25

então como que você mexe aqui mais ou menos sem quebrar nada e vou te mostrar como que a gente faz então os testes para você ver a temperatura você já deve ter conseguido ver aqui na lateral tem temperatura é com isso que a gente vai brincar belezinha já já volto pra gente evoluir essa aula então

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **GPU** — *Graphics Processing Unit* (Unidade de Processamento Gráfico)
- **token** — unidade de entrada/saída do modelo, podendo ser parte de palavra, palavra inteira ou símbolo
- **top-k** — seleção dos k tokens mais prováveis para amostragem
- **top-p** — amostragem por núcleo (*nucleus sampling*), considerando o menor conjunto de tokens cuja probabilidade acumulada atinge um limite p

**Resumo**
A aula apresentou o parâmetro de **temperatura** em modelos de linguagem, explicando que ele controla o grau de aleatoriedade na geração do próximo token a partir da distribuição de probabilidades do modelo. O instrutor destacou que um LLM não escolhe a “palavra certa” de forma exata, mas estima várias continuações possíveis com base no contexto e seleciona uma delas conforme a política de geração. Com isso, a temperatura atua como um ajuste entre respostas mais conservadoras e previsíveis, ou mais variadas e criativas.

Foi explicado que, em **baixa temperatura** — aproximadamente entre 0,1 e 0,3 — o modelo tende a favorecer os tokens mais prováveis, reduzindo desvios e aumentando a consistência. Esse comportamento é indicado para tarefas técnicas, previsíveis e factuais, como textos jurídicos, em que precisão e conservadorismo são mais importantes do que originalidade. Em contrapartida, quando a tarefa exige expressão artística, como poesia, música ou brainstorming, esse nível tende a deixar a saída rígida e pouco interessante.

Na faixa de **alta temperatura** — por volta de 0,7 a 1,0 — a distribuição se abre mais para tokens menos prováveis, aumentando diversidade lexical e estrutural. O instrutor associou esse uso a contextos em que surpresa e exploração são desejáveis, mas alertou que isso também eleva o risco de respostas improváveis ou menos adequadas ao contexto. Para reforçar o conceito, foi usada a metáfora de um especialista em uma biblioteca: com temperatura baixa ele segue direto para a referência mais adequada; com temperatura alta, passa a considerar opções mais aleatórias.

A aula também apresentou um fluxo prático com o **Hugging Face Playground**, um ambiente web para testar modelos e parâmetros de geração sem escrever código. O instrutor orientou a criar conta, confirmar o e-mail, gerar um token de acesso em *settings/tokens* e colá-lo no Playground para liberar a interface. A ideia do hands-on é repetir o mesmo prompt em diferentes valores de temperatura e observar como a saída muda, validando visualmente como o parâmetro altera a escolha entre o caminho mais provável e alternativas mais abertas.

**Pontos de atenção**
- Temperatura **não altera o conhecimento** do modelo; ela ajusta apenas o grau de aleatoriedade na escolha dos tokens.
- **Baixa temperatura** prioriza consistência e previsibilidade, mas reduz criatividade e variedade.
- **Alta temperatura** aumenta diversidade e exploração, porém eleva o risco de respostas imprecisas ou inadequadas.
- Para tarefas **técnicas, jurídicas ou factuais**, evitar temperaturas altas sem necessidade.
- Para tarefas **criativas**, temperaturas muito baixas podem gerar resultados pobres, rígidos ou “sem graça”.
- O valor da temperatura deve ser testado **repetindo o mesmo prompt** em diferentes configurações para comparar comportamento.
- O **Hugging Face Playground** foi usado como ambiente de experimentação; é importante autenticar corretamente a conta antes de tentar usar os controles.
- Para acessar o Playground, é necessário **confirmar o e-mail** e criar um **token de acesso** nas configurações da conta.
- O instrutor mencionou uma faixa prática de **0,1 a 1,0** e destacou os extremos como referência didática: baixo para precisão, alto para criatividade.
- A escolha da temperatura deve sempre considerar o **objetivo da tarefa**: precisão, fluidez, surpresa ou criatividade.