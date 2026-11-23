Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16397)

## Resumo da aula

Top-k sampling limita o conjunto elegível do próximo token aos k candidatos mais prováveis da distribuição atual. Em vez de permitir que qualquer token participe da escolha, o modelo ordena os candidatos por probabilidade e descarta tudo o que estiver fora desse recorte. Isso existe para controlar a geração sem cair nem no comportamento totalmente determinístico nem em uma abertura excessiva para opções improváveis. Retomando a ideia de temperatura já conhecida, a temperatura altera a forma da distribuição; o top-k decide quantos candidatos continuam vivos depois desse ranqueamento.

O mecanismo é simples: o modelo calcula as probabilidades do próximo token, ordena os tokens do maior para o menor valor e mantém apenas os k primeiros. Se k = 2, só os dois tokens mais prováveis podem ser escolhidos; se k = 5, os cinco primeiros continuam na disputa. Todos os demais são excluídos da amostragem naquele passo, mesmo que ainda tenham alguma probabilidade não nula. O efeito prático é um limite rígido por quantidade de candidatos, independentemente de quanto da massa probabilística esses candidatos representam.

Na continuação de o sol está brilhando no ..., suponha os candidatos céu (0,35), horizonte (0,25), mar (0,15), campo (0,10) e deserto (0,08), seguidos por outros tokens menos prováveis. Com top-k = 5, apenas esses cinco entram no conjunto elegível; o sexto em diante é descartado. A escolha final ainda não precisa ser sempre céu, porque a seleção ocorre dentro desse subconjunto filtrado. Isso mostra que controlar geração não é só “mais ou menos criatividade”, mas também decidir quais opções podem concorrer.

Sem um mecanismo de corte, a geração pode ficar presa demais ao caminho mais provável ou aberta demais a alternativas ruins, dependendo da combinação de parâmetros. Um recorte por k ajuda a reduzir repetição mecânica sem liberar tokens muito improváveis demais cedo demais. O resultado tende a ser uma saída mais natural do que uma escolha sempre gulosa do token líder. Em aplicações reais, isso é útil quando se quer previsibilidade estrutural com alguma diversidade local.

Top-p sampling, também chamado de nucleus sampling, não fixa um número de candidatos; ele fixa um limiar de probabilidade acumulada. O modelo ordena os tokens por probabilidade e vai somando esses valores até atingir ou ultrapassar p. Só os tokens necessários para alcançar essa massa acumulada permanecem elegíveis. A diferença central para top-k é que o tamanho do conjunto varia conforme o formato da distribuição em cada passo.

Massa acumulada de probabilidade é a soma progressiva das probabilidades dos tokens mais prováveis após a ordenação. Esse conceito importa porque o top-p não pergunta “quantos candidatos entram?”, mas sim “quanta probabilidade total eu quero cobrir antes de parar?”. Se poucos tokens já concentram quase toda a distribuição, o conjunto será pequeno; se a distribuição estiver mais espalhada, mais tokens precisarão ser incluídos. Por isso, top-p responde melhor à incerteza real do modelo em cada contexto.

Retomando os mesmos candidatos, a soma acumulada fica céu 0,35, depois horizonte 0,60, depois mar 0,75, depois campo 0,83 e depois deserto 0,90. Com top-p = 0,9, o conjunto elegível vai até deserto, porque é nesse ponto que a massa acumulada atinge 90%. Um token seguinte como luz (0,04) já fica fora, mesmo que fosse o sexto colocado. O corte, portanto, não depende da posição ordinal do token, mas da cobertura probabilística acumulada.

O corte por k é rígido em quantidade e variável em cobertura probabilística; o corte por p é rígido em cobertura probabilística e variável em quantidade. Isso faz o top-k ser mais simples de prever operacionalmente, enquanto o top-p é mais adaptativo ao formato da distribuição. Em distribuições muito concentradas, top-p pode manter poucos tokens; em distribuições mais dispersas, ele amplia o conjunto automaticamente. Essa distinção é a base para interpretar corretamente experimentos práticos com parâmetros de geração.

Temperatura e top-k/top-p atuam em camadas diferentes do processo de amostragem. A temperatura altera a distribuição antes da escolha, tornando-a mais concentrada ou mais dispersa; top-k e top-p definem quais tokens continuam elegíveis depois desse cenário probabilístico. Na prática, combinar esses controles permite ajustar tanto o formato da distribuição quanto o tamanho efetivo do espaço de escolha. Ler resultados no Hugging Face sem separar essas duas funções costuma levar a interpretações erradas sobre “criatividade” do modelo.

## Transcrição

00:00

Fala galera, beleza? Antes da gente evoluir aqui e conversar um pouquinho sobre como a gente faz um hands-on ali do Top K e do Top P, eu queria contar pra vocês o que que isso significa, tá bom? Então vamos lá, primeira coisa. Quando a gente tá falando do modelo de linguagem como GPT, a gente tá falando de uma geração de modelo de textos ali, certo? Então eu tô falando da geração de textos e a gente falou daquela esquema sempre que eu tô lembrando pra vocês de eu gero o próximo token tentando prever qual a palavra que viria ali, beleza?

00:29

Só que qual que é a grande sacada aqui? Essa geração não é de texto fixo. Não é simplesmente assim, olha... Cara, fui lá, calculei a probabilidade da próxima palavra e a que der a probabilidade maior é ela que será. Então imagina que eu calculei a probabilidade e a probabilidade da próxima palavra deu, sei lá, 60% e as demais são todas abaixo de 60% de probabilidade de serem a próxima palavra.

00:53

Ela não vai pegar direto essa de 60%. Deixa eu voltar e explicar isso de novo pra vocês. Imagina o seguinte, imagina que você tem uma frase lá, onde você tem cinco palavras já na frase. Sei lá, o céu hoje estava limpo. Um exemplo. O céu hoje estava, a próxima palavra que você tem que achar é o limpo.

01:12

Ele não vai ir lá e decidir entre os percentuais que ele tem, que limpo é a palavra certa e pronto. Ele tem um certo grau de aleatoriedade que a gente coloca aqui nele, que é um parâmetro que você consegue complementar junto com o que a gente falou há pouco sobre a temperatura. Você vai na temperatura abrir ou a mais ou menos,

01:38

essa aleatoriedade, mas você também consegue abrir o seu Top K que a gente fala aqui dentro disso também. O que isso significa aqui? Ao invés dele pegar a última carinha, o mais provável, ele vai ter um certo grau de aleatoriedade dependendo do K que você coloca. Eu já vou explicar isso melhor pra vocês.

01:58

Por que a gente precisa disso? Se você não deixar esse certo grau de abertura, ele pode ficar muito repetitivo em palavras, porque ele vai sempre escolher as mesmas, ele vai ter dificuldade de ser criativo, de criar palavras e contextos novos, então ele vai acabar sendo um pouco repetitivo, que vai ser ruim pra sua geração.

02:15

pode ter um outro problema também dele gerar frases sem sentido ali porque ele vai sempre pegar o que é o mais direto e com isso ele pode acabar gerando frases sem sentido e ele pode ser excessivamente previsível ou seja vai ficar uma conversa muito parecida com o chatbot

02:35

Então, se você pegasse aqueles chatbots de árvore de decisão, ia ficar muito parecido com aquilo, algo muito mecânico. Então, você precisa ter um certo grau de abertura para isso ficar um pouco mais normal, mais parecido com a linguagem humana, tá bom? Então, para isso, a gente usa uma técnica, que é o TopK, que é uma técnica de definição de estatística, tá? Nem é uma técnica só utilizada para LLMs, é uma técnica estatística, tá bom?

03:05

rapidinho para vocês entenderem o que isso significa. O TopK Sampling vai ser o seguinte, ele é uma técnica onde o modelo vai considerar apenas os K tokens com maior probabilidade para decidir qual será o próximo token da sequência. O que isso significa? Imagina que o K vai virar como se fosse uma variável, um X da vida.

03:26

Então, imagina que o K é esta variável. Eu vou aceitar os K tokens, ou seja, o número X ou o número K de variáveis, que dentro deste número, deste conjunto, eu vou escolher qual eu quero utilizar. Ficou confuso? Vamos lá. Então, ele vai fazer o seguinte.

03:45

Ele vai lá e pega todos os tokens possíveis, ou seja, todas as palavras possíveis que a gente pode ter em uma frase. Então, ele vai lá e pega todas as palavras que ele pode calcular probabilidade. Dentro dessa palavra, ele ordena pelo grau de probabilidade mais alto até o mais baixo. Dentro dessas probabilidades mais altas até o mais baixo, ele fecha um range. Então, imagina que você tem 10 palavras que foram escolhidas ali. Normalmente são muito mais do que isso, mas imagina que você tem 10 palavras que foram escolhidas ali para ser a próxima palavra que você está tentando procurar.

04:14

ele vai ordenar entre qual é a mais provável até a menos provável. Então vai ter uma lá com grau de 60%, uma de 30%, uma de 10%, 5, 0,2 e assim por diante. Vai lá e vai ordenar pela probabilidade maior até a probabilidade menor.

04:31

Dentro deste grau de ordenação, o que ele vai fazer? Ele vai pegar e fazer o seguinte... Qual que é o Top K que a gente quer usar? É 10? Então se o Top K é 10, eu vou pegar as 10 palavras e é essas que eu vou usar. Não, Top K é 2, eu vou pegar só as duas primeiras. Top K é 3, só as três primeiras.

04:48

eu desprezo as demais e trabalho dentro dessas três primeiras qual que eu quero utilizar com base em certo grau de aleatoriedade dentro dessas palavras, tá bom? Então é mais ou menos assim que a banda toca ali. Então imagina o seguinte, imagina que você tem um Top K com 5, tá? Vou fazer um exemplo aqui junto. O seu Top K é 5. E a gente tem um exemplo que é o sol está brilhando no...

05:10

pode ser várias palavras na sequência, certo? Então imagina que o sol está brilhando no... e meu tópico K5 eu vou ordenar aqui algumas palavras, pode ser no céu, certo? Então o céu tem uma probabilidade 0,35, beleza? Eu tenho a segunda que é horizonte, horizonte vai ser 0,25. Eu tenho a terceira que é mar,

05:34

Pode ser no mar, 0,15. A chance é menor. Pode ser no campo, 0,10. É menor ainda. Ou no deserto, 0,08. Tá vendo que eu coloquei aqui 5 palavras com 5 graus de probabilidade? E eu tenho outros tokens que foram gerados.

05:51

o 6, o 7, o 8, o 9, o 10, assim por diante. Com o TopK 5, o que ele vai fazer? Vai pegar só esse 5, o resto ele vai jogar fora. Dentro desse 5, com o grau de aleatoriedade que a gente abre, ele vai decidir qual que ele quer jogar pra você como resposta. Ele não vai colocar sempre o seu. Vai depender do seu grau de abertura aqui, de temperatura também, pra decidir qual, dentro dessa 5, ele quer atuar, quer usar pra te entregar. Entendeu? Então é mais ou menos assim que o TopK funciona, pra ficar fácil pra vocês.

06:18

E por isso que fica desse jeito. Eu vou aproveitar para explicar para vocês também como funciona o TOP-P. Quando a gente está falando do TOP-P, ele pode fazer uma outra estratégia. Enquanto o TOP-K você fixa um número, são 5, o TOP-P ele vai olhar a distribuição total e dentro da distribuição total ele decide.

06:40

Então, pega o Top K que a gente acabou de aprender, deixa de ladinho um pouquinho e vamos pro Top P. Quando a gente tá falando de Top P, eu vou colocar quais são os tokens mais prováveis que somem X% da probabilidade total. Então, aqui no Top K eu tô falando de 5, vai ser sempre 5. No Top P, eu vou abrir por percentual.

07:01

e daí dentro do percentual não vai ser sempre cinco tokens, pode ser seis, pode ser sete, pode ser só dois, vai depender do percentual de representatividade de cada token. Então o que significa o Top Sampling? Ele vai fazer o seguinte, eu pego um modelo onde o conjunto de tokens

07:20

cuja soma das probabilidades seja maior ou igual ao P que eu coloquei. Então, imagina que eu coloquei lá que o meu Top P é de 60%. Ele vai pegar qual é o conjunto que somado dá 60%. Então, se no meu caso eu tiver duas palavras iniciais que já batem 60%, esse vai ser meu Top P. Se eu precisar de três palavras para bater 60% na somatória, vai ser esse meu Top P e assim por diante. Então, vamos lá.

07:50

Imagina que o meu TopP é 0.9 significa o que? Que os tokens mais prováveis que somarem 90% vão ser utilizados, vão ser considerados, beleza? Então imagina o seguinte, vamos dar um exemplo de TopP de 90% dentro do que a gente acabou de falar também. Imagina que eu tenho lá o céu, a gente falou que era 0.35, então somou 35%. Depois o próximo é horizonte, eu falei que era 0.25, beleza? Então somou 25%.

08:19

depois eu vou lá e falo mar, mar era 0,15 então aqui já deu 35,25 50,60 com 15,75 ainda não bateu 90 o próximo é campo 0,08 o outro a gente falou que era deserto 0,07 e o outro era luz sei lá 0,04 agora sim dentro deste grupo eu bati

08:43

é 90%, se a minha conta tá sendo feita certa, acho que sim. Então, deu 0,35 mais 0,25, deu 30, 50, 60%. Com 15, 60, 75%. Com mais 0,8, 75% mais 0,8 vai dar 80 e

09:06

2% né 3% perdão 83% com mais 7,90% é isso acho que é isso então cheguei até o deserto ali luz possivelmente seria desconsiderado se eu fiz a conta certo mas você entendeu aqui a somatória das probabilidades é que de cabeça lembra todas probabilidades que eu falei e ainda fazer a conta minha cabeça não tá boa para isso tudo não mas daria mais ou menos isso entendeu

09:28

Então aqui, quando eu tô falando dessa somatória, eu iria até então deserto e depois de deserto luz eu já não colocaria, porque no deserto já deu 90%. Beleza? Então os outros tokens ali que tem pra baixo disso vão ser desconsiderados. Então eu vou trabalhar com céu, horizonte, mar, campo e deserto. E daí dentro destas palavras eu vou abrir a minha estratégia

09:55

de qual que eu quero entregar. Aí a LLM vai decidir isso, beleza? Então, basicamente, essa é a diferença do Top K e do Top P. A gente vai brincar agora um pouquinho com o Top P. Na hora que eu estiver mostrando pra vocês, eu vou contar um pouquinho como ele funciona de novo, pra vocês lembrarem. E daí a gente mostra lá como que funciona essa variação dentro do Hugging Face também, beleza? Valeu, galera!

## Resumo IA

**Abreviações**  
- **LLM**: *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **GPT**: *Generative Pre-trained Transformer* (Transformador Generativo Pré-treinado)  
- **Top-k**: amostragem por “k melhores” candidatos  
- **Top-p**: amostragem por probabilidade acumulada, também chamada de **nucleus sampling**  

**Resumo**  
A aula explicou como controlar a geração de texto em modelos de linguagem por meio de estratégias de amostragem, destacando a relação entre aleatoriedade, previsibilidade e diversidade na escolha do próximo token. Primeiro, foi retomada a ideia de que o modelo prevê o próximo token com base em probabilidades, mas não necessariamente escolhe sempre o mais provável de forma determinística. Para evitar saídas excessivamente repetitivas ou mecânicas, o instrutor apresentou o **top-k sampling**, que limita a escolha aos **k tokens mais prováveis** após ordenar os candidatos por probabilidade. Assim, se k for 5, apenas os cinco primeiros tokens permanecem elegíveis, e a decisão final acontece dentro desse subconjunto filtrado, com influência também da temperatura.

Em seguida, foi introduzido o **top-p sampling**, ou **nucleus sampling**, que funciona de forma diferente: em vez de fixar a quantidade de candidatos, ele define um **limiar de probabilidade acumulada**. O modelo ordena os tokens por probabilidade e vai somando suas probabilidades até atingir o valor de p definido; somente os tokens necessários para alcançar essa massa acumulada entram no conjunto elegível. Dessa forma, o número de candidatos varia conforme a distribuição em cada contexto. A aula comparou os dois métodos, mostrando que o top-k controla diretamente a quantidade de opções, enquanto o top-p controla a cobertura probabilística, e reforçou que temperatura, top-k e top-p atuam em camadas diferentes do processo de geração. Também foi mencionado que essas estratégias podem ser observadas na prática em ferramentas como o Hugging Face.

**Pontos de atenção**  
- O **top-k** não escolhe obrigatoriamente o token de maior probabilidade; ele apenas restringe o conjunto de candidatos aos k primeiros.  
- Um valor de **k muito baixo** pode deixar a geração excessivamente rígida e repetitiva.  
- Um valor de **k muito alto** aumenta a abertura para alternativas menos prováveis e pode reduzir a coerência.  
- O **top-p** não fixa quantidade de tokens; ele fixa uma **massa acumulada de probabilidade**.  
- No **top-p**, o número de tokens permitidos varia conforme o formato da distribuição em cada passo.  
- A interpretação correta depende de distinguir **temperatura** de **top-k/top-p**: temperatura altera a distribuição; top-k e top-p filtram os candidatos após essa etapa.  
- Em distribuições concentradas, o **top-p** tende a manter poucos tokens; em distribuições dispersas, tende a ampliar o conjunto.  
- A escolha entre top-k e top-p impacta o equilíbrio entre **previsibilidade, naturalidade e diversidade** da resposta.  
- Ao analisar resultados em ferramentas como o **Hugging Face**, é importante não confundir o efeito da temperatura com o efeito do método de amostragem.