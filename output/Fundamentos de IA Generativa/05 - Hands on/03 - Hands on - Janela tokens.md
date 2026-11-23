Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16396)

## Resumo da aula

Máximo de tokens é o limite de geração que interrompe a resposta quando o modelo atinge a quantidade configurada de tokens. Esse controle existe porque gerar mais texto consome mais processamento e, em muitos cenários, aumenta custo operacional. Quando o limite é baixo demais para o tamanho da resposta esperada, o texto é truncado e pode terminar no meio de uma frase ou de uma ideia.

Retomando o mesmo prompt sobre explicar buracos negros, o efeito novo não está na criatividade da resposta, mas no quanto ela consegue avançar antes de ser cortada. Com o limite aberto, o modelo produz uma explicação longa; com um valor intermediário, ainda consegue concluir a ideia; com 512 tokens, a saída pode ser interrompida no meio. Isso mostra que controlar geração não é apenas escolher estilo: também é decidir quanto de resposta a aplicação consegue pagar e entregar.

Custo operacional aparece porque cada token processado ou gerado consome recursos do provider e da aplicação. Limitar a saída é uma forma prática de evitar respostas excessivamente longas, reduzir latência e manter previsibilidade de gasto. O problema é que um corte agressivo demais transfere complexidade para o design do prompt, que passa a precisar pedir respostas mais curtas e mais focadas para caber no orçamento de tokens.

Em aplicações reais, esse ajuste não deve ser feito isoladamente. Se a resposta está sendo truncada, o caminho não é apenas aumentar o limite; muitas vezes é melhor reescrever o prompt para pedir menos itens, menos detalhes ou um formato mais compacto. O parâmetro controla a janela de saída, mas a qualidade final depende de alinhar limite, objetivo da tarefa e formato esperado da resposta.

Top-p é um mecanismo de amostragem que restringe a escolha do próximo token ao menor conjunto de candidatos cuja probabilidade acumulada atinge um certo limiar. Diferente da temperatura, já vista anteriormente, ele não espalha ou concentra toda a distribuição da mesma forma; ele corta a cauda menos provável e mantém apenas uma faixa de opções consideradas plausíveis. Isso importa porque dois controles de geração podem produzir saídas diferentes mesmo com o mesmo prompt e o mesmo modelo.

Quando a interface expõe top-p junto com temperatura e máximo de tokens, ela permite separar três decisões operacionais: quão variada a resposta pode ser, quantos candidatos entram na amostragem e quanto texto pode ser emitido. No experimento, top-p foi mantido aberto em 1 para não interferir tanto na observação do truncamento. Essa escolha isola o efeito do limite de tokens e facilita enxergar por que a resposta foi cortada.

Spaces são aplicações publicadas pela comunidade dentro do ecossistema Hugging Face. Eles funcionam como vitrines executáveis: em vez de apenas ler sobre um modelo, você interage com uma interface pronta e observa como alguém empacotou um caso de uso. Isso é útil para explorar geração de texto, imagem, vídeo, síntese de fala e outros fluxos sem começar implementando tudo do zero.

A qualidade dos Spaces varia bastante porque eles dependem da configuração e da disponibilidade mantidas por quem publicou. Alguns expõem parâmetros como temperatura, máximo de tokens e top-p; outros falham, ficam fora do ar ou têm descrições insuficientes. Por isso, Spaces servem bem para exploração e prototipagem, mas não devem ser tratados automaticamente como ambientes estáveis de produção.

O ecossistema Hugging Face organiza recursos diferentes para necessidades diferentes. Docs concentra documentação técnica, bibliotecas e guias de integração; Community reúne artigos e interações sociais; Models cataloga modelos com metadados, downloads e snippets de uso; Datasets centraliza conjuntos de dados; Spaces oferece aplicações interativas publicadas pela comunidade. Essa separação reduz atrito de navegação: você procura documentação em um lugar, experimentos em outro e ativos reutilizáveis em outro.

Para quem está consolidando fundamentos, a navegação mais útil costuma começar por artigos da comunidade e por Spaces, porque esses pontos mostram aplicações concretas e tendências de uso. A documentação tende a ser mais valiosa quando surge uma necessidade específica de implementação, como integrar com AWS ou entender uma biblioteca. Já a página welcome funciona como um hub mais organizado para acessar essas áreas sem depender apenas do menu principal.

Daily Papers agrega publicações e referências mais próximas de pesquisa acadêmica. O valor dessa área está em acompanhar o que está sendo proposto, comparado e testado na fronteira do campo, em vez de apenas consumir tutoriais ou posts introdutórios. Para desenvolvedores, isso ajuda a identificar tendências, novas técnicas e termos que depois aparecem em bibliotecas, benchmarks e produtos.

Esse tipo de conteúdo exige mais maturidade técnica do que artigos gerais da comunidade. A leitura tende a ser mais densa, mais formal e menos orientada a passo a passo de implementação imediata. Ainda assim, filtros por período e tema tornam o espaço útil para monitoramento contínuo, mesmo quando o objetivo não é reproduzir o paper naquele momento.

Retomando o Playground já usado anteriormente, o procedimento é manter o mesmo prompt e alterar apenas o limite máximo de tokens. Use uma pergunta idêntica, como a explicação simplificada sobre buracos negros, mantenha os demais controles o mais estáveis possível e gere uma resposta com limite aberto. Em seguida, repita com um limite intermediário e depois com um valor baixo, como 500 ou 512 tokens, para comparar o ponto em que a resposta passa a ser truncada.

A leitura do resultado deve observar completude, não apenas tamanho. Se a resposta termina abruptamente, o problema não é necessariamente falta de conhecimento do modelo, mas interrupção forçada pela configuração. Essa distinção é importante em debugging de aplicações com LLM, porque evita atribuir ao modelo um erro que na verdade foi causado por uma restrição operacional da própria chamada.

## Transcrição

00:01

Fala pessoal, vamos aprender mais um pouquinho então sobre o Hugging Face? Quero mostrar para vocês algumas outras coisas que a gente pode fazer aqui para vocês verem na prática como é que a brincadeira funciona. Então a gente estava aqui olhando no nosso Playground

00:17

o que a gente tinha para brincar aqui, para testar e etc, mostrar para vocês como funciona assim por diante. Aqui vocês podem ver que tem umas coisas adicionais aqui, você pode olhar que tem o máximo de tokens que você pode mexer e você tem o top P para fazer também. Mas eu vou mudar, eu quero ir para outro lugar com vocês para a gente ver outras coisas e depois se necessário a gente volta e olha aqui, mas acho que não vai ser, acho que a gente consegue em outro ambiente aqui mostrar como a gente brinca com isso também, para vocês conhecerem um pouco mais

00:47

do Hugging Face. Vamos ver junto como é que isso vai funcionar? Então vamos lá. Primeira coisa que eu queria ver com vocês é o seguinte, vamos dar uma passeada, tá? Pra vocês entenderem o contexto geral do Hugging Face, o que que tem de legal aqui, pra vocês poderem olhar e depois a gente vai pra nossa aula. Então vamos dar uma olhada geral aqui. Pricing, você vai olhar lá toda uma parte de compra pra uma conta Pro, uma conta em grupo ou Enterprise.

01:12

Minha opinião, pra agora vocês não precisam disso. Então deixei aqui aberto pra vocês olharem. Eu às vezes uso a minha conta PRO, tô deixando aqui até a minha conta que não é PRO pra vocês poderem olhar e a gente ver junto as mesmas coisas. Aqui você não precisa se preocupar porque o que a gente vai fazer não tem necessidade de você ter uma conta PRO. Então só pra você saber que existe, tá? Então existe aqui e não precisa vir aqui.

01:35

Vamos lá, Docs. Aqui no Docs você tem bastante coisa que é legal para você. Se você precisar, por exemplo, de algumas informações, vamos traduzir aqui para quem não está tão acostumado com inglês, facilitar. Então aqui você tem algumas coisas que você pode buscar de documentação para te ajudar no dia a dia. Sendo muito honesto, aqui é para quem já está mais acostumado a usar realmente os modelos

01:57

e a treiná-los no dia a dia. Não acho que você deveria gastar tanta bala aqui, mas quando você precisa de alguma documentação, você pode buscar aqui. Por exemplo, imagina que você precisa de alguma documentação para saber como implementar alguma coisa na AWS utilizando os modelos do Hugging Face. Você tem aqui ó, implementando na AWS, facilita a sua vida, você consegue fazer isso mais fácil lendo aqui. Você pode também ver como você pode fazer, por exemplo,

02:22

modelos onde você junta um machine learning junto com uma execução de tarefas e assim por diante. Tem vários tipos aqui de bibliotecas que você pode usar também, então dos transformers, difusores, conjuntos de dados e assim por diante, como funciona a tokenização... Então, tem várias coisas aqui que você pode ler. Possivelmente, vai estar num nível mais alto, mais avançado para vocês, dado que a gente está pegando por enquanto. Mas aqui é legal você ir dando uma fuçada de vez em quando, tá bom?

02:51

Na comunidade tem coisas mais legais, sendo bem honesto. Você pode olhar os artigos, então ó, fui comunidade artigos, tá bom? Vamos lá. Quando a gente olha nos artigos, ó, eu deixei em português, tá? Porque tem muita gente que não tá tão familiarizada com inglês, então vamos no português pra facilitar a vida de todo mundo.

03:08

Se tiver alguma coisa aqui muito diferente, eu vou traduzindo para o inglês de volta para vocês pegarem. Então, aqui você consegue pegar vários artigos e assim por diante. É uma comunidade bem rica. Aqui sim, acho que vale você gastar um pouco mais de tempo, você investir mais o seu tempo. Você consegue olhar aqui o que você tem de IA em várias situações aqui dentro do que a gente tem nos artigos da comunidade. Então, você pode ver aqui, por exemplo... Gema totalmente disponível... Gema...

03:35

3N totalmente disponível no ecossistema de código aberto, dá para você ler algumas coisas sobre isso, como é que tá o Lora, você consegue ver algumas coisas aqui que eles estão jogando de... De... De... Artigos, perdão, tinha fugido a palavra, de artigos para vocês poderem olhar aqui também. Então tem várias coisas aqui legais para vocês lerem e vocês podem ir filtrando e assim por diante. Nada mais do que um grande blog, tá gente? Mas eu acho que é legal vocês olharem. Fora isso, você tem...

04:05

uma parte social. Então tem aqui a rede social onde a galera troca uma ideia. Então se você precisar trocar com alguém, você consegue trocar por aqui também. Você consegue mandar mensagens e assim por diante. Consegue ler, seguir as pessoas. É mais a rede social mesmo, tá bom? Então se você precisar fazer alguma coisa aqui, você consegue seguir aqui colocando também.

04:24

Tá bom? Lendo o que a galera tá postando e assim por diante. Então você pode seguir, eu não sigo ninguém aqui, até porque aqui não tá na minha conta direta, mas você pode ir colocando as coisas que tão rolando aqui, tá bom? Então aqui é bacana pra você ver o que tá rolando na comunidade. Vamos pra outra parte aqui que é Daily Papers. Aqui é um pouco mais técnico,

04:43

mas tem bastante coisa que você consegue pegar bem legal aqui é para usar no dia a dia então você consegue ver mais as pesquisas que a galera tá fazendo o Hugging Face até traduziu aqui olhei abraçando o rosto nunca tinha lido desse jeito o Hugging Face

05:01

ele tem esse Q de quem está estudando o assunto, então é um lugar realmente onde a galera vai trazer para você. Você pode pesquisar aqui qualquer artigo que tem com IA, mas aqui se você olhar são mais artigos acadêmicos, não são artigos tão simples quanto aqueles outros que a gente estava vendo. Você consegue filtrar se quer semanal, diário, etc... Ele inclusive deixa você jogar aqui qualquer coisa, se você não souber o que você quer buscar, ele deixa você escolher aqui e ele vai buscar o que ele acha que faz sentido para você.

05:31

Então, tem aqui algumas coisas assim. Tem mais uma coisa que pra algumas pessoas é importante, pra mim não é tanto, deixa eu voltar aqui. Você pode mudar o seu tema aqui ó, escuro, deixar claro, etc. Eu não ligo tanto, não sendo meio honesto, pra mim tanto faz. E aqui você tem a parte de espaço. Então, vamos sair de comunidade e vamos para os espaços. Dentro dos espaços, você tem o que a galera tá testando. Então, os espaços da semana, o que a galera tá gerando? Você pode vir aqui ó, o que eu quero fazer com o IA?

05:57

geração de imagem, você pode pegar aqui quais são os espaços que a galera tá fazendo, o que elas estão fazendo, se você não quiser criar o seu espaço. Depois eu te mostro como criar o seu espaço, mas aqui também é um pouco mais avançado. Aqui você pode ver o que a galera tá gerando, você pode clicar neles e ir vendo aqui o que a galera tá testando, o que tá rolando aqui dentro de cada espaço. Então tá vendo aqui ó, tem alguém testando alguma coisa de imagem, onde você joga uma imagem e pelo jeito você faz a pessoa ficar com a roupa e etc, assim por diante. É legal você ir lendo e entendendo o que cada um tá tentando fazer ali.

06:26

Deixa eu ver, que mais? Tá vendo? É bem isso. Ele tá colocando aqui um teste onde você coloca uma pessoa, a roupa que você quer pra essa pessoa e ele veste. Isso aqui é bem importante, principalmente pra quem faz venda, etc. Você tem vários modelos, você pode ir adequando. Bom, alguém tá testando isso, deve fazer sentido.

06:43

Daí você pode clicar em outro e ver outras coisas que tem aqui. Isso aí é pra imagem, pra vídeo. Tem outros caras fazendo outros testes aqui. Vamos ver o que que é isso aqui. Então você tem aqui um outro vídeo que você pode ir entendendo. Tem que ler e entender o que que a galera tá fazendo. Então, por exemplo, esse cara aqui tá fazendo uns vídeos de... De um pinguim dançando, etc. Eu não sei onde ele quer chegar com isso. Deixa eu ver... Não deu pra entender por aqui. Mas cada um desses você pode ir fuçando, tá? Você entendeu, né? Geração de texto, tradução de idiomas...

07:11

síntese de fala, modelagem em 3D, vamos ver a modelagem em 3D, o que que tá rolando aqui. Você pode ver o que a galera tá fazendo, ó, você vai jogar uma imagem pra cá e daí ver o que que ela vai conseguir gerar de resultado, então a pessoa tá colocando aqui a geração de imagens em 3D mesmo pra ver o que acontece, então colocando essa imagem, qual o resultado que ela vai gerar, então é mais ou menos você vendo o que que os diretórios das pessoas tão fazendo, tá bom? Você dá uma visão geral, você consegue vir mais pra cá,

07:39

E vendo tudo que tem, tem coisa pra caramba gente, de verdade. Tem vários tipos de estratégias que a galera pode estar fazendo. Você pode filtrar também, como é que você quer, o que você quer fazer... Você pode classificar também, um jeito diferente aqui... Mas basicamente é onde você olha os espaços do outro. Pô, quero criar meu espaço. Eu posso criar aqui uma breve descrição. Você viu que a galera coloca uma descrição muito ruim. Então, às vezes você não consegue entender o que é. Minha dica, se você quiser fazer com que essa comunidade seja cada vez mais legal, coloca uma descrição legal, coloca o que você está esperando com o que você está colocando aqui, tá bom?

08:09

Você pode gerar um espaço público ou privado. Depois que você criei esse espaço, você pode brincar ali com algumas coisas. Não vou aprofundar nisso, tá gente? Depois, no modo mais avançado, é importante pra vocês. Mas por enquanto, quando a gente tá falando ainda de fundamentos, não vamos aprofundar nisso, senão só vai dar nó na cabeça.

08:26

Beleza? Então aqui são os espaços. Conjuntos de dados, vocês vão ver todos os conjuntos de dados que a galera tá usando ali pra fazer seus modelos e assim por diante. Também não vou entrar nesse detalhe. E aqui você tem os modelos também, que você também consegue ir olhando o que a galera tá tendo de modelo. Aqui tem normalmente uma capa de como é que é o modelo, falando sobre ele, esse modelo tá? Então aqui a gente vai ver tudo que tá falando sobre cada modelo, o que tem de código dele e assim por diante.

08:52

Enquanto isso, na sua direita ele vai falar quantas pessoas estão baixando e assim por diante para cada modelo. E você pode falar, quero usar este modelo, você quer usar ele com Transformer e etc. Ele te dá o código para você copiar e colar dentro do seu Git, o que você for fazer com esse carinha aqui. Bom, de novo, esse cara aqui também a gente não vai aprofundar. Eu vou levar vocês para um outro lugar que eu acho bacana da gente ir fora o que a gente estava fazendo ali no nosso...

09:22

no nosso Lab, tá? Então deixa eu ver aqui, se eu vier aqui, olha, em... em Hugging Face, em vez de Models, vamos colocar o Welcome, barra, o Welcome, é legal vocês olharem também por aqui. Tá vendo? Aqui você tem os espaços,

09:38

Você tem vários modelos, você tem os daily papers, você também pode vir por aqui, tá vendo? A mesma coisa que tem ali em cima, você tem por aqui mais organizado. Eu prefiro vir por aqui quando eu quero fazer alguma coisa, porque aqui é mais organizado. Então, você pode ter seus modelos locais, o que você quer fazer de aprendizado e assim por diante. Então, aqui também é legal para você dar uma brincada. Se você for tentar ir navegando por aqui, eu sempre perco o Elcom, tá? Então, eu normalmente entro no Elcom e por aqui eu vou navegando para onde eu quero ir.

10:08

Isso é super importante para você conseguir chegar no resultado que você quer, nos lugares, etc... E eu acho mais fácil do que por aquele outro caminho que eu mostrei para vocês, tá? Então, se vocês precisarem, vocês podem entrar por aqui e ver as coisas que estão rolando também. Beleza?

10:25

basicamente é isso que a gente tem aqui no Hugging Face, agora eu vou levar vocês para olhar outra brincadeirinha aqui, vamos olhar dentro dos modos, nos modos não, perdão, dos spaces e eu vou pegar um space de alguém para a gente brincar tá, então vamos lá, eu vou colocar um de geração de texto e vamos pegar o de psique

10:48

Agora é a nossa aula, tá? Até agora eu tava só olhando, mostrando pra vocês o que que tem dentro do Hugging Face. Vamos ver o que que tem aqui. Se a gente tem algum que dá pra brincar legal. Deep Seeker... Vai meu filho, tá uma lerdiza? Vamo lá. Deep Seeker... Deep Seeker... Vamo ver esse aqui.

11:17

Não, geração de texto, vamos deixar ele aberto. DeepSeek. E vamos ver esse DeepSeek teste aqui que ele tem. Ó, esse é legal. Vamos ver se tem algum mais legal ainda do que ele.

11:31

Esse é de imagem não, esse aqui não vai ser legal. Quero ver um de texto com vocês, tá? Que a gente tá falando bastante de texto, vamos aprofundar no texto. Vamos nesse aqui mesmo. Aqui você vai ter o chatbot pra você colocar onde vai sair as coisas, pelo que eu tô entendendo, porque é de alguém, então tão aprendendo junto, tá gente? Aqui você pode dar like no modelo da pessoa pra ver o que tem aqui ou não. E aqui ó, isso que eu quero mostrar pra vocês, Additional Inputs. Nesse cara ele deixou aberto, ó.

11:56

o que ele tem de temperatura, o máximo de tokens e o top P. Lembra que eu mostrei para vocês ali que a gente podia mexer no top P e no top K? Aqui a gente também consegue. Então, é um outro jeito dentro do DeepSeek que alguém está brincando para você mexer também. Então, é outro caminho para você chegar numa brincadeira parecida. Vamos fazer uma brincadeira parecida com o que a gente estava falando? Então, eu tinha pedido para... Deixa eu voltar e lembrar o que eu tinha feito de pergunta. Era o seguinte... Explique a...

12:25

um buraco negro de forma simplificada com

12:36

para facilitar o entendimento então vamos lá explique um buraco negro de forma simplificada com abstrações para opa tem um toque aqui para facilitar o entendimento tá bom vamos ver isso aqui pode dar erro hein gente que eu não testei esse chat vamos ver aqui eu posso colocar o máximo de tokens que eu quero que sejam gerados isso é importante para vocês verem

12:56

como que vocês tem que ter cuidado de vocês, eu vou deixar aberto o máximo de tokens que ele pode gerar temperatura, eu posso colocar 4 aqui, tá vendo ele abriu pro máximo, vamos meter 4 pra vocês verem o que acontece na verdade não, vamos fazer o seguinte, vamos brincar com o topK primeiro eu vou deixar a temperatura 5 e vou deixar o topK em 1 beleza, vamos ver o que ele vai gerar deixa eu copiar isso aqui pra gente poder fazer igual a gente fez naquela hora oxi, tá dando erro

13:23

Vamos ver se baixar aqui o número de tokens ele deixa. Tá vendo? Aí você vai querer brincar com o negócio dos outros, ele dá erro. Já dá pra você dar um like no modelo desta pessoa, porque não funcionou. Vamos tentar menos.

13:53

Bom, tá fora dele, não tá funcionando, não deu certo vir por aqui porque este não está funcionando. Vamos ver se tem outro carinha aqui que a gente consegue brincar. Não, também tá fora. Bom, ali você consegue mexer com alguns modelos, mas como tá fora, é legal a gente olhar com mais calma ali se tem algum que tá no ar pra vocês brincarem.

14:11

Vamos no Playground de volta e mostrar por aqui o que a gente pode fazer pra vocês testarem. Então a gente já deu uma passeada, vocês viram que tem aquele outro lugar que dá pra ir também, mas infelizmente eu não achei um ali que tá aberto, que a gente consegue mexer na temperatura sem capotar. Na temperatura não, no Top P sem capotar. Vamos colocar aqui ó...

14:30

deixar aberto o máximo de tokens então você viu que eu cliquei aqui né ó tá vendo ele tá é fechado você clica no set ele vai abrir para você o máximo de tokens vou eu quero brincar com duas coisas aqui para vocês a primeira coisa seguinte opa aqui ó se eu colocar aquela pergunta e deixar o máximo de token do jeito que tá ele vai gerar um montão de ovo deixar abertão e uma temperatura ponto cinco

14:55

0.4 0.5 e eu vou deixar no top 1 vamos gerar e ver o que acontece vai roda meu filho então a gente está lá com o top de psik r1 mesmo que a gente estava usando e deixei aberto para ele gerar o máximo de token que ele puder olha o tanto de informação que ele está trazendo beleza ele gerou um montão de informação

15:21

E eu deixei o TopP abertão lá com 1 no máximo dele. Então aqui quando a gente olha pra isso, você vê que ele gerou esse tipo de mensagem. Beleza? Vamos pegar essa mensagem, deixar ela aqui e criar uma outra agora, baixando o número de tokens pra vocês verem. Beleza? Vou deixar o TopP daquele jeito lá. Vamos lá, com outro número de tokens. Play. Vai lá meu filho.

16:19

Beleza, você viu que ele continuou gerando uma informação grande aqui. Deixa eu colocar uma nova mensagem e a gente jogar um agora. E eu vou colocar pouquíssimo token pra ele. Eu vou deixar aqui ó. Vou deixar ele com 500 tokens, só pra vocês verem o que acontece. E aí eu vou jogar aqui e mandar ele gerar pra gente comparar. Vai, play.

16:55

Olha lá, tá vendo que engraçado? O que eu tô querendo mostrar pra vocês? Aqui no primeiro, eu tinha deixado o token abertão. Depois, eu joguei ele mais pro meio, tá? E daí, olha o do meio como é que ele gerou. Ele gerou um texto bem grande, certo? Ele conseguiu gerar tudo que ele precisava. Aqui, depois, eu peguei o tokens e coloquei no máximo 512 tokens. Você viu que ele cortou no meio do caminho? Por quê? Porque isso é o que acontece quando você tá fazendo, por exemplo, uso de alguma...

17:22

de alguma aplicação de LLM e você precisa cortar ele pra não gastar muito, por exemplo, olha gerou muito token, tá saindo muito caro meu processamento e eu vou dar uma limitada aqui na galera. Normalmente vai dar um erro desse, aí você tem que fazer o que? Você tem que limitar no prompt

17:37

pra ele entrar certo, isso que eu quis mostrar pra vocês. Quando você mexe nesse máximo de tokens, você pode acabar gerando esse tipo de problema. Então, o máximo de tokens aqui, ou seja, o máximo de palavras que você vai liberar pra ele fazer, vai te atrapalhar dependendo do que você tem pra executar. Eu queria mostrar aqui, e primeiro a gente viu como funciona a contagem de tokens,

17:57

Depois a gente viu como funciona a temperatura para você ver como que ele abre ou não a mensagem, e agora eu estou te mostrando que você consegue cortar uma mensagem para ela não chegar inteira para você. O máximo tokens vai fazer isso acontecer, vai fechar a janela para você não ter tantos tokens sendo gerado. Aqui você pode brincar, aumentar, diminuir e assim por diante. Então, isso é importante para você ver como essa coisa funciona. Deixa eu fazer um teste com vocês...

18:22

para vocês verem também uma outra coisa que a gente tem aqui é na verdade faz o seguinte eu vou cortar esse vídeo para não ficar tão grande e eu volto pra gente falar de top rapidinho é vai ser jogo rápido só pra gente não deixar esse vídeo tão grande tá bom

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **AWS** — *Amazon Web Services*  
- **Git** — sistema de controle de versão distribuído  
- **ML** — *Machine Learning* (Aprendizado de Máquina)  
- **IA** — Inteligência Artificial  
- **Hugging Face** — plataforma/ecossistema de modelos, dados e aplicações de IA

**Resumo**  
A aula apresentou uma visão geral do ecossistema Hugging Face e, principalmente, demonstrou na prática como parâmetros de geração afetam o comportamento de modelos de linguagem. O instrutor começou passeando pelas áreas principais da plataforma — Docs, Community, Daily Papers, Spaces, Datasets e Models — explicando o papel de cada uma: documentação técnica, artigos e posts da comunidade, publicações acadêmicas, aplicações interativas, conjuntos de dados e catálogo de modelos. Também destacou a página Welcome como um hub mais organizado para navegação e reforçou que, para iniciantes, Spaces e artigos da comunidade tendem a ser os pontos mais úteis para explorar casos reais.

Na parte prática, o foco foi a configuração de geração no Playground e em Spaces de terceiros, mostrando como ajustar temperatura, top-p e, principalmente, o máximo de tokens. O instrutor explicou que o máximo de tokens define o limite de saída do modelo e que, quando esse valor é baixo demais, a resposta pode ser truncada no meio de uma ideia ou frase. A demonstração comparou o mesmo prompt com limites diferentes: com valor aberto, a resposta veio longa; com um limite intermediário, ainda ficou completa; com um limite baixo, a saída foi cortada. A aula também mostrou que top-p é um mecanismo de amostragem que restringe os candidatos ao próximo token com base na probabilidade acumulada, e que esse parâmetro pode ser combinado com temperatura e limite de tokens para controlar variabilidade, seleção e tamanho da resposta.

O instrutor ainda ressaltou que Spaces são vitrines executáveis criadas pela comunidade, úteis para explorar modelos e fluxos sem começar do zero, mas com qualidade e estabilidade variáveis. Ele reforçou que esses ambientes servem bem para experimentação e prototipagem, mas não devem ser tratados automaticamente como produção. Por fim, a mensagem central foi que, em aplicações reais com LLMs, ajustar apenas o limite de tokens não basta: muitas vezes é melhor reescrever o prompt para pedir menos itens, menos detalhes ou um formato mais compacto, alinhando objetivo da tarefa, orçamento de geração e formato esperado da resposta.

**Pontos de atenção**  
- **Máximo de tokens não muda a “criatividade”, e sim o quanto a resposta pode avançar antes de ser cortada.**
- **Limite baixo demais pode truncar a resposta no meio de uma frase ou ideia.**
- **Respostas truncadas nem sempre indicam falha do modelo; muitas vezes são efeito da configuração de geração.**
- **Ao encontrar truncamento, não basta aumentar o limite: frequentemente é melhor reescrever o prompt para ser mais enxuto e focado.**
- **O custo operacional cresce com a quantidade de tokens processados ou gerados; limitar saída ajuda a reduzir custo e latência.**
- **Ajuste de geração deve considerar em conjunto temperatura, top-p e máximo de tokens, e não isoladamente.**
- **Top-p corta a cauda menos provável da distribuição; ele interfere diretamente na amostragem do próximo token.**
- **Spaces da comunidade são úteis para exploração, mas podem estar fora do ar, mal configurados ou com descrições ruins.**
- **Não assumir que tudo em Spaces é estável o suficiente para produção.**
- **A leitura correta do resultado deve observar completude e não apenas tamanho da resposta.**
- **Em debugging de aplicações com LLM, diferenciar erro do modelo de restrição operacional evita diagnóstico errado.**