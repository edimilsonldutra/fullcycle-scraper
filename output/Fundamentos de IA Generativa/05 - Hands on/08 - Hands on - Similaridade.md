Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16401)

## Resumo da aula

Similaridade semântica é a comparação entre textos pelo significado aproximado, não apenas por palavras idênticas. Retomando embeddings já vistos anteriormente, a aplicação prática aqui é transformar cada frase em um vetor e medir o quanto esses vetores ficam próximos no espaço vetorial. Essa abordagem permite detectar relação entre frases formuladas de modo diferente, embora o resultado continue sendo uma aproximação numérica, não uma compreensão humana do texto.

A similaridade por cosseno mede o alinhamento entre dois vetores, produzindo um score que indica o quanto eles apontam para direções parecidas. Ela é útil porque compara a orientação semântica das representações, mesmo quando os valores absolutos dos vetores diferem. No app, o fluxo é direto: gerar emb1 e emb2 a partir de duas frases, calcular o cosseno entre eles e retornar esse valor como saída da interface.

Um Space próprio é uma aplicação hospedada no Hugging Face sob sua conta, com interface, código e configuração versionados. Isso importa porque permite testar ideias rapidamente sem depender do ambiente local nem impactar sistemas da empresa. O processo básico consiste em abrir Spaces, criar um New Space, definir nome, descrição, licença, visibilidade e escolher a infraestrutura gratuita de CPU quando o objetivo for apenas prototipação.

Ao criar o Space, a escolha do Gradio define que a interface será construída como uma aplicação web simples baseada em componentes de entrada e saída. Em vez de editar apenas o arquivo padrão gerado automaticamente, é possível criar o próprio app file e controlar explicitamente o código da aplicação. Essa decisão deixa o experimento mais claro: um arquivo concentra o modelo, a função de cálculo e a definição da interface.

Gradio é a camada de interface que expõe a função Python como um formulário interativo. Aqui, a interface precisa de dois campos de texto como entrada e um campo numérico de saída para exibir o score de similaridade, além de título e descrição para orientar o uso. O valor do Gradio está em reduzir o esforço de front-end: com poucos componentes, o experimento já fica publicável e testável no navegador.

A função central recebe duas frases, converte ambas em embeddings com um modelo Transformer já disponível e calcula a similaridade entre os vetores resultantes. O passo importante não é apenas “usar um modelo”, mas encadear corretamente as etapas: entrada textual, geração dos vetores, cálculo do cosseno e retorno do score. Esse pipeline materializa a ideia abstrata de proximidade semântica em uma medição observável.

O requirements.txt declara as dependências que o ambiente remoto precisa instalar antes de iniciar a aplicação. Quando esse arquivo não existe ou está incompleto, o build pode falhar mesmo que o código esteja correto, porque o runtime não sabe quais bibliotecas instalar. Neste caso, o erro após o primeiro deploy é resolvido criando o requirements.txt e adicionando as dependências usadas pelo app.

Depois do commit na main, o Space entra em etapas de build e start, que podem ser lentas na infraestrutura gratuita. Essa lentidão não significa travamento; significa apenas que o ambiente remoto está instalando dependências e inicializando a aplicação. Quando ocorre erro logo após a publicação inicial, a primeira verificação prática deve ser a presença dos arquivos essenciais, especialmente o requirements.txt.

Frases mais longas tendem a produzir resultados mais informativos do que palavras isoladas, porque oferecem mais contexto para a representação vetorial. No experimento, trocar “gato” por “cachorro” aumenta a similaridade, enquanto substituir a frase por algo sobre “avião” reduz o score, o que confirma que o modelo está capturando parte da semântica. Ainda assim, o resultado não é perfeito: elementos genéricos como tempo, estrutura frasal e temas vagamente relacionados podem manter alguma proximidade residual.

O score de similaridade não equivale a entendimento completo do contexto. Duas frases quase idênticas, mas com uma negação ou mudança sutil de sentido, ainda podem aparecer como muito próximas porque a estrutura textual e grande parte dos termos permanecem semelhantes. Além disso, o app usa uma configuração simples e infraestrutura modesta, então o objetivo aqui é demonstrar o mecanismo de embeddings em ação, não entregar uma avaliação semântica de alta precisão.

## Transcrição

00:01

Fala galera, beleza? A gente já evoluiu pra caramba, espero que vocês estejam gostando bastante aqui do nosso treinamento. Então a gente já conseguiu aprender uma porrada de coisas.

00:11

Indo na ideia de aprofundar um pouquinho mais com vocês, para vocês entenderem ainda mais tecnicamente como a coisa funciona, eu quero falar um pouquinho com vocês de novo de embeddings, tá? Quando a gente está falando de embeddings, a gente tem bastante coisa para aprender e eu preparei uma forma aqui para conversar com vocês um pouquinho mais sobre isso. A gente vai fazer um hands-on sobre embeddings, foi difícil de eu conceituar ele para trazer para vocês sem ter que aprofundar muito,

00:40

a ponto de ensinar o detalhe do detalhe de como isso funciona mas eu consegui fazer aqui um lab pra gente treinar junto aqui espero que vocês curtam e quem quiser fazer um lab também eu deixo aqui um passo a passo pra vocês fazerem logo na sequência eu tento fazer com vocês também pra vocês conseguirem criar esse tipo de conteúdo caso vocês precisem, tá bom? então deixei de uma forma mais simplificada aqui então o objetivo dessa aula é a gente repassar um pouquinho aqui o que são os Embeddings pra que eles funcionam, como eles funcionam, pra que eles são usados e assim por diante

01:09

e eu vou fazer um hands-on com vocês para vocês verem isso na prática de como funciona, de como que por trás a máquina vai pensar quando a gente estiver criando alguma coisa nesse sentido. Beleza? Então vamos lá! Vamos voltar a nossa memória aqui e entender o que são os Envys primeiro.

01:26

Quando a gente tá falando dos modelos de linguagem ali, eles não vão trabalhar com o texto diretamente, eles não são como seres humanos que compreendem o texto. Você concorda que até nós, seres humanos, a gente entende um texto que tá vindo, a gente entende uma comunicação e decifra ela ao longo do caminho.

01:42

A gente coloca aqui a nossa análise semântica pra decifrar isso, a gente pega tudo que a gente conhece de gramática, do que a gente já conhece de conversa, e a gente vai trazendo tudo isso pra dentro do nosso cérebro pra, quem sabe de algum jeito, compilar isso como uma máquina faria.

02:00

e transformar em um resultado que seja interessante para os nossos neurônios conseguirem trabalhar. Olha eu falando de biologia aqui de uma forma que eu nem conheço tanto, mas creio que deva ser algo neste sentido. Professores aí que conhecem mais sobre o assunto de neurociência, por favor, não me matem. Mas vamos voltar. Quando a gente está falando das máquinas, como é que elas fazem esse negócio?

02:25

Elas vão transformar isso no que elas conhecem, no que para elas faz sentido, em número. Então, elas precisam transformar isso de algum jeito em alguma representação numérica. E elas fazem isso transformando em vetores. Por isso que a gente tem as representações vetoriais. Então, quando a gente está falando de embeddings, ele vai ser um tipo de representação

02:45

vetorial de uma informação. Um vetor, nesse caso, é como se fosse um armazenamento de informação. Então, você vai armazenar a informação textual de tudo aquilo que eu acabei de falar para vocês. E tem uma porrada de coisas aqui. Então, eles vão trazer para você os significados, as relações e o contexto que a gente tem dentro de uma comunicação, de um texto, beleza? Então, eles são nada mais do que...

03:12

Representações vetoriais densas. A gente tem que lembrar disso. Não é uma representação vetorial trivial de uma informação única, mas ela é um embutido de informações que são incluídas dentro desse vetor, tá bom? Então, aqui elas vão conseguir colocar dentro desse espaço vetorial a semelhança semântica. Quando a gente está falando dos embeddings. A gente vai trazer para dentro disso a semelhança semântica.

03:39

E o que isso significa? Como funciona? Quando a gente está falando de, por exemplo, um vetor gato, deve estar mais perto de um cachorro, de um vetor cachorro, do que um vetor avião. Por que eu estou falando como vetor e não como tokens? Porque aqui eu não estou falando mais só de uma palavra ou de algo próximo a uma palavra, que é representado por um token.

04:06

Quando eu estou falando de embeddings, eu estou falando da semelhança vetorial entre gato e cachorro, que é muito diferente de gato e avião, beleza? Então, vocês notam que aqui a gente tem um cálculo, um delta entre semelhanças de palavras para a gente conseguir compreender contextos, tá bom? Então, cada palavra ou cada sentença vai ser transformada em um vetor,

04:31

com uma centena ou milhares, etc, de dimensões. Ela vai começar a abrir-se em várias dimensões para ver a similaridade. Eu estou tratando a primeira dimensão, similaridade das palavras mesmo. Mas quando a gente está falando de textos maiores e assim por diante, a gente tem outras tantas similaridades. Eu até estou tirando aqui do jogo a mudança aqui de linguagem, por exemplo, que eu posso estar falando em dois idiomas diferentes e assim por diante. Então tem uma porrada de coisa que entra aqui no meio do caminho.

05:01

eu simplifiquei ao nível de quase um Tolkien para a gente conseguir discutir aqui. Então, essa distância entre os vetores, ela normalmente é calculada por uma função de cosseno ou uma função euclidiana, beleza? Mas a gente não precisa entrar nisso, se você não conhece tanto de cálculo não tem problema, mas aqui a gente vai medir quanto

05:21

essa semântica e essa contextualidade são próximas. É pra isso que serve, pra você conseguir compreender a proximidade, beleza? Então, Embeddings, proximidade. Embeddings é difícil de falar, hein, gente? Se eu falar errado, por favor, não me matem. É a proximidade dos seus

05:38

das suas representações vetoriais no final do dia ali de palavras, tokens ou de frases, textos e assim por diante. Você está tentando ver quanto isso se aproxima ou se distancia em proximidade de informações. Beleza? Vamos entrar agora no Hugging Face? Já loga aí, se você quiser fazer junto comigo, a gente entra e vamos fazer um hands-on para vocês verem como que isso funciona a hora que a gente está vendo na prática, tá bom?

06:07

Fala galera, beleza? E aí? Vamos fazer um hands-on aqui rapidinho para vocês entenderem como funciona o Embeddings na prática, vocês vendo ele funcionando? Então vamos lá! A primeira coisa que eu quero fazer com vocês é o seguinte...

06:21

tá aqui o Hugging Face, eu vou clicar aqui no Hugging Face só pra voltar pra cá, então imagina, você tá lá em outro lugar, tá em Community, não, vamos lá, Docs. Você tá aqui em Docs, abriu, sei lá, o seu Hugging Face abriu errado, clica aqui que você vai voltar pra este pedaço. Estando aqui, você pode vir aqui ó, no Spaces, lá você também podia? Também podia, mas só pra você tá na mesma tela que eu.

06:43

Fui para Spaces e quando eu vejo Spaces, você vai ter o que? A gente já deu uma olhada aqui. Os espaços que estão bombando mais na semana, que é o que a galera tá criando. Que tem mais gente entrando, possivelmente, e assim por diante, tem mais gente curtindo e tal. E aqui você pode procurar algum Space. Então, NatanPF, por exemplo. Você vai ver meus Spaces aqui, que eu criei pra essa aulinha nossa aqui, então. Pra gente brincar.

07:07

Nessa conta tem quase nada, então vocês não vão achar muita coisa minha. Mas você pode procurar também por algum tipo de space, se você quiser algum tipo de brincadeira que você quiser fazer, você pode vir por aqui, separar por grupo de espaços, tá bom? Mas pra agora o que a gente vai fazer é criar um novo. Então até agora eu já tinha mostrado aqui mais ou menos como funciona. Vamos criar um novo space. Em new space, nada muito sigiloso, meio fácil de fazer. Vamos colocar aqui aula, nome do espaço.

07:36

Owner você, né? Aula em B2. Genuinus. Pronto. Short description. Vamos colocar aqui uma descrição. Deixa eu ver. Aula de verificação vetorial.

07:59

Proximidade. Pronto. Licença. Aqui na licença a gente coloca essa do emit aqui, que acho que ela é a melhor pra gente usar. Agora vamos ao grade, o que lançou. Vamos ver como ele funciona. Acho que dá bom.

08:15

é aqui cpu cpu tá vendo que é tudo pago gpu cpu tudo pago aqui ó eu vou trabalhar com essa aqui que é de graça é a mais lerda mas é de graça aí você pode escolher se você quer público ou privado como vocês vão usar esse espaço depois eu vou colocar ele público se você ficar só brincando aí na sua é no seu espaço para ver como é que funciona coloca privado assim ninguém fica olhando as traias que você tá fazendo bom

08:42

aqui então você tem a aula tal abriu tudo que você tem aqui você pode pegar e mexer nesse radio api file mas eu não vou fazer isso não eu vou criar um novo tá vendo eu posso em vez de usar esse eu posso vir aqui criar o meu e vou criar o meu create the new api file então este carinha aqui que eu vou usar e como que a gente vai criar esse cara primeiro vou dar um import aqui vou puxar um

09:06

o início do nosso Gradle aqui pra gente conseguir trabalhar vou usar um modelo de Transformer que já tem aqui pronto e vou colocar pra gente o código que eu já tinha feito pra vocês não ficarem vendo eu digitar aqui um tonto então coloquei o modelo

09:24

de transformer que já existe que eu sei que tem aqui já que a gente pode considerar pra gente e vou colocar aqui uma calculadora de similaridade então eu coloco a entrada de duas frases dentro das duas frases eu vou calcular o amb1 e o amb2 convertendo eles etc assim por diante faço esses caras virarem um vetor e depois disso eu tiro o cosseno deles e depois volto com o score então basicamente é isso que eu tô fazendo tá

09:53

de forma muito simplificada e corrida aqui pra explicar. Tá, dá pra usar? Ainda não dá pra usar não, precisa de uma interface. Então vamos criar uma interface aqui, vou colocar uma interface de calcular similaridade, e aqui eu vou ter então dois textos de entrada, uma saída que é um número de quão similar é, que é o nosso percentual de similaridade, e um título, uma descrição aqui também do que precisa ser feito e blá blá blá, mas aqui não é nada demais. Tá certo? Pronto? Pronto. Vamos então

10:24

É isso, vou dar um commit direto na main, vamos lá, comanda pra dentro. Ele tá buildando aqui, daqui a pouco ele processa e tal, esse carinha aqui é um pouco mais rápido, vai dar erro, vocês vão ver né, se não der erro vai ter alguma coisa estranha, tem que dar erro. Vai buildar, daqui a pouco ele starta ela e na hora que ele startar ele vai possivelmente dar um erro.

10:46

É um pouco lento, como eu falei para vocês, isso que dá você usar GPU gratuita, mas também não usar gratuita é um absurdo de caro, então é isso aí. Vai meu filho! Builda!

11:03

Se demorar muito mais, eu vou cortar e daqui a pouco a gente volta pra aparecer aquela mágica. Mas saiba que demora. Então se o seu estiver demorando, não travou. Tá bom? É isso mesmo. O negócio é lento. Ai minha gente, dá pra ver um filme. Foi, tá estartando. Eu não vou cortar então, que é pra vocês conseguirem ver esse tempo real e não se assustar. Porque às vezes eu tenho medo de cortar e vocês falarem, pô, mas o meu tá demorando pra caramba. Demora mesmo.

11:29

Ele está startando, demora também um pouquinho. Às vezes vai mais rápido o start. Dessa vez está lerdeza. Vai meu filho!

11:43

Deu erro. Normal, tá gente? Não clica aqui, não precisa clicar aqui. Se você clicar aqui, você vai abrir o log de erro. Eu não quero que você abra o log de erro, eu quero que você venha aqui pro aula. Aqui ó, tá vendo? Aqui ó, aula em B2. Aqui embaixo.

12:00

Vamos lá. Aqui você vai abrir a sua pastinha, se assim posso dizer. E aqui você criou então lá, o Webpack tá aqui, tá ali com o que a gente acabou de fazer. Vamos fazer mais um treco? Contribute. Vou criar um new file. Por quê? Ele deu erro porque ele ainda não tá com o TXT dele pronto, requirements. Então a gente vai criar o requirements. Vamos lá, requirements.txt.

12:30

tá aí ó e a gente vai usar colocar aqui dentro dele o que a gente chamou lá grade 1 e vamos pra dentro cadê? commit de novo agora quando ele criar esse carinha aqui ó eu vou deixar esses dois esses dois textos aqui pra vocês assim fica mais fácil tanto o requirements.txt quanto a criação do API já separado em texto fica mais fácil pra vocês copiarem e colarem aí tá bom?

12:57

Ele tá startando já, você viu que ele buildou? Nossa, nem vi. Buildou rápido dessa vez, mas ele tá startando. Normalmente esse starting dele aqui é um pouco mais demorado, porque ele tem que startar a aplicação como um todo. Não deveria, mas como a gente tá de graça, ele demora um pouco mais.

13:18

é algo super simples, vocês vão ver, mas pelo menos a gente consegue fazer um testezinho e eu acho interessante vocês conseguirem cada vez mais se aprofundar em Hugging Face pra quando vocês precisarem fazer algum tipo de estratégia um pouco mais complexa, tá gente? aí vocês conseguem fazer os seus testezinhos, ver o que que tá dando certo, o que que não tá dando certo sem quebrar nada na sua empresa, sem quebrar nada no seu note também, você vai e trabalha aqui que é mais fácil

13:41

você tem um espaço mais colaborativo e que você consegue brincar. Acho que é o principal para você brincar, ver como estão as coisas e assim por diante. Tá estartando, eu vou cortar e vou voltar ao vídeo. Já já a gente volta então para vocês verem o que aconteceu. Fechou? Até já já.

14:02

Bom pessoal, terminou aqui, agora tá como running, vamos ver esse trequinho funcionando? Gente, é só um exemplo, eu fiz aqui uma coisa bem simplesinha pra gente conseguir pegar, então vamos lá pra nossa aula, vai abrir esta telinha. Dentro dessa telinha, você consegue então colocar duas frases e ver qual é o output.

14:20

O que que eu noto que acontece? Se você colocar uma palavra, a similaridade ele não vai conseguir ver muitas coisas, porque ele não consegue quebrar muitas camadas, e é muito difícil pra uma LLM conseguir um transformer ali, conseguir entender a similaridade entre duas palavras, tá? Agora, quando você coloca frases mais longas, a chance de você conseguir ter um output que varia mais é um pouco maior, então vamos lá. Vamos colocar assim, hoje...

14:46

Hoje cedo meu cachorro passou mal pois comeu algo que não deveria. Beleza? Hoje cedo meu gato comeu

15:10

Algo estragado por isso não está bem. São coisas diferentes. Vamos ver o que ele vai dar de similaridade. Está vendo? 0.69%. Vamos mudar o gato para cachorro. E vamos ver o que ele fala. Viu que aumentou a similaridade? Agora vamos colocar aqui, em vez de cachorro,

15:40

Comeu algo estragado, por isso não está bem. Eles estão muito similares, beleza? Agora, vamos mudar aqui. Hoje... é... Durante a tarde, meu rinoceronte... rinoceronte comeu... Correu, em vez de comeu...

16:11

vou mudar bastante pela savana por isso está

16:30

está machucado ele ainda tem algum grau de similaridade aqui porque ele deve estar pegando

16:45

a similaridade de tempo, tá falando de animal, e tá falando de alguém que não está bem, mas você viu que diminuiu um pouco? Agora vamos mudar totalmente esse negócio aqui, olha... Meu avi não precisa de um mecânico novo... Opa! Mecânico novo...

17:12

pois está com problemas no trem de pouso. Pronto, vamos ver o que ele vai falar aqui.

17:26

tá vendo que caiu aqui o que o avião que precisa de um mecânico novo tem a ver com um cachorro que passou mal não sei mas no cálculo de similaridade ele buscou e ele mostrou que tem alguma similaridade agora deixa eu ver uma coisa mais simples tá é

17:52

Como que acontece? Tô brincando aqui com vocês, não tinha feito também esse teste. Tá vendo que ele já piorou muito mais, até porque ele tem menos texto pra procurar, e daí o output foi lá pro... abaixou muito. Agora vamos pegar esse cara, copiar tudo igualzinho, e vamos ver o que que ele vai falar, porque é importante vocês verem que possivelmente ele não vai dar um output de 100.

18:17

Deu. Viu que a similaridade é igualzinha. Que legal. Hoje cedo meu cachorro passou mal pois comeu algo que não deveria. E se eu virar e falar assim, hoje cedo meu cachorro passou mal pois comeu algo que...

18:30

deveria. Vamos ver o que ele vê. Tá vendo? É muito similar. Então, tá vendo que pra ele, o contexto, ele não entende o contexto. Isso é importante vocês verem. Ele não entende o que você tá falando. Ele vai fazer cálculo. Tá vendo que aqui mudou totalmente. Aqui ele deveria ter comido aquilo, por isso ele passou mal.

18:47

Não dá uma impressão totalmente diferente da frase de cima, mas, similarmente, quando a gente fala de contexto, elas são muito parecidas. Então, a gente está falando ali que na parte de análise textual dos vetores, elas vão ser parecidas. Bom, fica aqui para vocês brincarem. Então, se vocês forem lá no Spaces, tá vendo? Aula Emb2. Se vocês virem aqui em Spaces e procurarem aula Emb2,

19:11

vocês vão achar ela aqui, a aula em b2, vocês podem entrar nela e ficar brincando aqui, coloca a frase 1, frase 2, frase 1, frase 2, vai jogando aqui, beleza? E aí vocês conseguem ir vendo como que essa coisinha funciona por trás, eu fiz um código super simples, não tá tendo o melhor dos motores por trás, na verdade tá um bem porcariazinho, só para vocês verem como funciona

19:34

essa estratégia de Embeddings, beleza? Então Embeddings, similaridade entre frases, era isso que eu queria colocar na cabeça de vocês. E aqui a gente consegue ver essa similaridade, brinca um pouquinho pra entrar na mente, mas lembrem-se que vai dar umas doideiras aqui, porque eu tô com uma máquina qualquer por trás, tô com um GPU ruim, então possivelmente vai ter algumas distorções aqui, ele vai dar uma certa alucinadinha, porque a gente não fez da melhor forma possível, fechou?

20:00

espero que vocês tenham gostado daqui a pouco a gente vem para o nosso último módulo estamos chegando no final último módulo vamos aprender um pouquinho mais como que a gente faz toda essa parte de prompt como é que a gente utiliza isso no nosso dia a dia e é isso aí galera espero que vocês estejam gostando um forte abraço até mais

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **CPU** — *Central Processing Unit* (Unidade Central de Processamento)
- **GPU** — *Graphics Processing Unit* (Unidade de Processamento Gráfico)
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **TXT** — arquivo de texto simples (`.txt`)
- **emb1 / emb2** — embeddings gerados a partir da primeira e da segunda frase
- **Gradio** — biblioteca para criação de interfaces web para funções Python
- **Hugging Face** — plataforma usada para hospedar e compartilhar modelos, apps e Spaces

**Resumo**
A aula apresentou o conceito de similaridade semântica como uma forma de comparar textos pelo significado aproximado, indo além da correspondência literal de palavras. O instrutor retomou a ideia de embeddings para explicar que frases e palavras podem ser transformadas em vetores num espaço vetorial, permitindo medir a proximidade entre representações numéricas para estimar relação semântica. Em seguida, foi explicada a similaridade por cosseno, usada para medir o alinhamento entre dois vetores e gerar um score que indica o grau de semelhança entre duas frases. O fluxo prático do app foi mostrado de forma simples: receber duas frases, gerar os embeddings correspondentes, calcular o cosseno entre os vetores e exibir o valor na interface.

Na parte prática, o instrutor demonstrou como criar um Space próprio no Hugging Face, destacando que um Space é uma aplicação versionada com interface, código e configuração hospedada na plataforma, útil para prototipação rápida sem depender do ambiente local. Foi criado um novo Space com Gradio, escolhendo uma infraestrutura gratuita de CPU para testes e definindo nome, descrição, licença e visibilidade. O código da aplicação foi concentrado em um arquivo principal, com importação de um modelo Transformer já disponível, implementação da função de cálculo de similaridade e montagem da interface com dois campos de texto de entrada e um campo numérico de saída. Também foi mostrado que o arquivo `requirements.txt` é essencial para declarar as dependências necessárias ao ambiente remoto, evitando falhas de build.

Por fim, o instrutor testou o app com diferentes pares de frases para mostrar o comportamento do score. Frases mais longas e semanticamente próximas geraram valores maiores, enquanto frases com temas distantes reduziram a similaridade. Ao mesmo tempo, ele reforçou que o resultado é apenas uma aproximação numérica: o modelo não “entende” o contexto como um humano e pode manter proximidade mesmo em frases com mudanças sutis, como negação ou alterações pequenas de sentido. A aula fechou reforçando que o objetivo era demonstrar o mecanismo de embeddings em ação e permitir que os alunos experimentassem a ideia no Hugging Face Spaces.

**Pontos de atenção**
- Embeddings não representam compreensão humana do texto; eles produzem aproximações numéricas de significado.
- Similaridade alta não garante equivalência de sentido completo, especialmente em casos com negação ou mudanças sutis.
- Frases muito curtas, como palavras isoladas, tendem a gerar resultados menos informativos.
- A similaridade por cosseno mede alinhamento vetorial, não “verdade semântica” absoluta.
- Em Spaces, o `requirements.txt` é indispensável; sem ele, o build pode falhar mesmo com o código correto.
- No deploy inicial, erros comuns podem vir da falta de dependências ou de arquivos essenciais.
- A infraestrutura gratuita de CPU pode ser lenta no build e no start; demora não significa travamento.
- Escolher Gradio simplifica a interface, mas o app precisa de uma função bem encadeada: entrada textual → embeddings → cosseno → score.
- O exemplo da aula usa um motor simples e não otimizado; resultados podem apresentar distorções e “alucinações” numéricas.
- Spaces são úteis para experimentação segura, sem impactar o ambiente local ou sistemas da empresa.
- Para avaliar proximidade semântica, frases com mais contexto costumam funcionar melhor do que termos isolados.