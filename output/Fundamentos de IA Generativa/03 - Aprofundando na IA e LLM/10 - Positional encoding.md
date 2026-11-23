Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16380)

## Resumo da aula

As Position-wise Feedforward Layers são as camadas aplicadas após a atenção para transformar cada token individualmente. Retomando a atenção já vista anteriormente: ela mistura contexto entre tokens; o feedforward pega o vetor resultante de cada posição e o refina de forma independente. O mesmo bloco de rede é reutilizado para todas as posições da sequência, mas cada token passa por ele com seus próprios valores. Isso permite enriquecer a representação de cada token sem misturar novamente as posições nesse estágio.

A atenção funciona como uma conversa entre tokens, na qual cada posição coleta informação relevante das demais. O feedforward corresponde à etapa de reflexão posterior: depois de receber contexto, cada token “processa internamente” o que fazer com aquilo. Dois tokens podem passar pela mesma rede e ainda assim produzir saídas diferentes, porque entram com vetores diferentes. A utilidade dessa etapa está em converter contexto recebido em uma representação mais útil para a próxima camada.

O bloco é composto por duas transformações lineares com uma não linearidade entre elas, tipicamente na forma max(0, xW1 + b1) seguida de uma segunda projeção com W2 e b2. W1 e W2 são matrizes de peso que aprendem como transformar a representação do token, enquanto b1 e b2 são vetores de viés que ajustam essas transformações. A primeira projeção expande ou reorganiza a informação em um espaço intermediário; a segunda consolida o resultado em uma nova representação vetorial. O efeito combinado é mais expressivo do que uma única transformação linear.

A expressão xW1 + b1 produz a primeira transformação do token. W1 atua como um conjunto de filtros aprendidos, mudando o ponto de vista sob o qual o vetor é interpretado; b1 desloca esse resultado para ajustar a ativação de cada dimensão. Em termos práticos, essa etapa cria um vetor intermediário mais rico, ainda bruto, mas já reorganizado para destacar padrões úteis. É a preparação para a etapa seletiva seguinte.

O max(0, ·) introduz não linearidade, normalmente via ReLU. Essa operação zera valores negativos e preserva os positivos, funcionando como um filtro que descarta ativações sem contribuição útil naquele ponto do processamento. Sem essa não linearidade, empilhar transformações lineares continuaria equivalente a uma única transformação linear, limitando a capacidade do modelo de representar relações complexas. É essa quebra de linearidade que permite ao bloco aprender padrões mais profundos do que a atenção sozinha consegue expressar.

Depois da ativação, a segunda transformação usa W2 e b2 para condensar o vetor intermediário em uma forma final refinada. Se a primeira projeção abre espaço para explorar características, a segunda reorganiza esse conteúdo para produzir uma saída compatível com a próxima camada do Transformer. O token resultante já não é igual ao vetor de entrada: ele carrega o contexto recebido pela atenção e a interpretação local feita pelo feedforward. Essa saída segue adiante como uma representação mais apurada.

O termo position-wise indica que o bloco opera separadamente em cada posição da sequência. Isso não contradiz o uso de contexto global no Transformer, porque a mistura entre tokens já ocorreu na atenção; aqui o trabalho é local, sobre cada vetor individual. O ganho dessa separação é permitir que cada token reorganize internamente a informação contextual que recebeu. Depois, as camadas seguintes voltam a combinar essas representações refinadas no processamento global do modelo.

A atenção identifica de onde vem a informação relevante; o feedforward decide como transformar essa informação dentro de cada token. Essa divisão de responsabilidades torna o Transformer mais expressivo: primeiro ele relaciona posições, depois aprofunda semanticamente cada representação. O resultado é uma sequência de vetores progressivamente mais úteis para tarefas como previsão do próximo token e modelagem de dependências complexas. Sem esse bloco, o modelo perderia capacidade de refinamento local e de aprendizado não linear.

## Transcrição

00:00

Bom, galera, vamos seguir para o segundo conceito que a gente tem aqui embutido. Vai ser a parte de Feedforward, a gente já falou de Feedforward, certo? Mas é o Feedforward Position-wise Layers, que a gente fala. Esse carinha vai ter uma estrutura bem interessante e fundamental para as coisas funcionarem. Então, dentro do Transformer, depois que o modelo decidiu ali quais são as palavras que a gente falou há pouco, ele deve prestar atenção

00:26

uma nas outras ali, via o que a gente acabou de explicar de multi-head, ele vai passar por um conjunto de camadas de feedforward, que vão ser aplicadas para conseguir chegar no raciocínio final. Então o que vai acontecer? Esse feedforward ele processa individualmente cada posição que a gente tem ali pra acessar, tá? Então essas camadas que a gente tá falando de processamento de cada posição, são as position-wise feedforward layers. É delas que a gente vai falar aqui agora, tá bom?

00:56

Então, deixa eu tentar trazer uma abstração pra vocês, pra ficar mais fácil o entendimento do que ficar falando só palavras difíceis, que são difíceis de entender. Quando a gente tá falando de Feed Forward Position Wise Layers, a gente tá falando o seguinte, imagina que você tem uma... é... imagina que a atenção que a gente falou antes é como se fosse uma conversa, tá bom? A nossa conversa aqui, por exemplo. Então, eu tô aqui falando com você e a gente tá conversando.

01:20

Feedforward é como se fosse a reflexão pós a conversa. Depois da conversa, o que você vai refletir sobre esse assunto? Imagina que nessa relação é como se você fosse um componente ou outro componente. Você está recebendo uma informação, você vai refletir e a sua reflexão, a sua

01:39

O que você vai reter disso vai ser diferente, por exemplo, do que eu vou reter. Isso é importante de pensar. Então, quando a gente usa essa metáfora, vamos imaginar o seguinte, o mecanismo que a gente tem de atenção, ele vai ser como se fosse um grupo de pessoas conversando e trocando ali as suas informações. Então, as pessoas estão ali trocando as informações. O Feedforward vai ser como se cada uma dessas pessoas, no momento seguinte, começasse a refletir sobre o que foi falado, tudo que ouviu ali. E daí, com base nisso, vai tomar as decisões ou vai formar uma nova ideia,

02:09

Embasado em tudo que foi falado. Ou seja, se a gente parar pra pensar é como se a atenção fosse com quem eu preciso falar pra entender melhor alguma coisa. E Feedforward é como se fosse o que eu faço com essa informação agora que ela está comigo. Ou seja, eu busquei essa informação com quem ela tem e agora o que eu faço com ela?

02:30

é mais ou menos isso de forma simplificada e como que isso funciona tecnicamente por trás eu vou passar para vocês e a gente começa a aprofundar tá então cada token ou palavra é da sequência que a gente tem vai passar por pela mesma rede neural lá de feedforward essa rede ela vai aplicar posição por posição

02:52

de forma independente a sua ação. A estrutura que a gente tem normalmente de cálculo pra isso é essa que eu tô deixando aqui pra vocês na tela. Essa estrutura é bem robusta e ela conta pra gente uma situação. O que significa nessa estrutura, por exemplo, vamos quebrar essa matriz pra ficar mais fácil da gente entender. Então imagina o seguinte, a gente tá olhando aqui na tela.

03:18

W1 e W2 ali. O que significam esses W? São as matrizes de peso. Vocês já vão entender isso. E tem ali o B1 e o B2, por exemplo. Eles são os vetores de viés, que a gente chama. E tem esse carinha ali, que é o max, que depois abre parênteses zero. Essa é uma função para introduzir uma não linearidade, tá bom?

03:49

Com isso você monta tudo isso que eu falei pra vocês. Mas vamos aprofundar um pouco mais pra não ficar só nesse básico que eu tô falando aqui pra vocês. Vamos lá, deixa eu tentar criar uma abstração pra vocês. Imagina que cada token desse pode ser uma palavra.

04:08

representada com um vetor. Então, vamos simplificar e trazer isso para uma palavra. Então, é como se fosse um aluno. Imagina que a gente está em uma sala de aula e a gente tem um aluno que recebeu a informação da aula anterior. Ele acabou de receber a informação da aula anterior. Com isso, é atenção, beleza? Então, ele recebeu essa informação.

04:26

Agora ele vai começar a processar essa informação sozinho. Ele vai fazer três passos. Primeiro ele vai pegar, vamos pegar esse trechinho aqui do nosso cálculo, que é o xw1 mais b1. Esse pedacinho aqui. Como está entre parênteses a gente vai fazer ele primeiro, certo? Então xw1 mais b1.

04:45

Quando eu olho pra esse carinha aqui, o que ele tá me contando? É como se fosse a primeira transformação do grupo. Você pensa que esse aluno vai ser o vetor X. Então, esse aluno vamos transformar ele no X. O aluno X vai entrar nessa sala de aula de transformação e vai receber a matriz W1. Ou seja, você tá multiplicando, você tá recebendo essa matriz. Quando ele recebe esse novo ponto de vista,

05:15

sobre a informação que ele tinha, ele repensa a informação, então ele evolui essa informação, então pensa que era o aluno, ou seja, eu tinha uma carga de informação, chegou W1 com outra carga de informação, eu recebo e transformo. Essa matriz da W1 vai representar os filtros, como se fossem as lentes que a gente tem

05:36

para transformar esse conhecimento do aluno. Ou seja, você está dando uma nova lupa para esse aluno conseguir ter um espaço mais abstrato ali de compreensão, tá bom? Aí depois você vem com o B1. O B1 é como se fosse o ajuste fino. Você adiciona este ajuste fino

05:54

como se fosse um conselho adicional do tipo, depois dessa transformação que você fez, preste atenção nisso aqui, e dá o B1 pra ele. O resultado que você vai ter aqui vai ser um vetor mais intermediário, ou seja, você evoluiu o aluno X para um vetor mais intermediário, só que com novas ideias, mas ainda bruto. Então é como se você tivesse conseguido colocar mais ideias aqui, tá bom? O próximo passo que você vai fazer é o passo 2, que é o Max (0).

06:22

Esse cara tá fazendo o que? Ele é uma função de ativação. Qual que é a analogia que a gente pode fazer com ele? Imagina que agora esse aluno ele tá refletindo tudo que aprendeu e tudo que for negativo, que foi inútil, ele vai desprezar. Então, tudo aquilo que não tem nada a ver com o que ele tava querendo aprender, ele vai desprezar. Então, cor da roupa do professor, se tava com muita luz ou pouca luz na sala, tudo aquilo que não tem nada a ver com o que ele queria aprender, ele vai jogar fora. Pensa que é isso, tá? Então, essa função, ela só vai manter os valores positivos.

06:52

Quando você olha pra isso, já fica declarado que tudo que é negativo vai ser zerado quando você faz esse cálculo. E daí com isso você evita que alguma ideia que é inútil desvirtue a sua evolução de criação de inteligência de aprendizado.

07:09

Então, com isso você consegue simular a escolha do que vale a pena seguir e guardar, e o que não vale a pena guardar dentro do seu aprendizado. Então, só o que tem potencial positivo vai pra frente, vai pra próxima etapa, que é a terceira etapa que a gente tem, que é a segunda transformação, que é o que vai enriquecer essa conversa.

07:29

Essa segunda transformação faz o seguinte, imagina que o conhecimento que a gente conseguiu com esse primeiro filtro, a gente dá uma lente adicional que vai consolidar o que foi refletido, com um entendimento adicional.

07:46

pronto para o que você recebeu, você se prepara para compartilhar essa informação para os tokens da próxima camada. Então, o W2 vai condensar o valor numa forma final, vai condensar esse valor que a gente já calculou anteriormente e o B2 dá aquele ajuste final no que a gente tem. Então, são dois vetores

08:09

e duas transformações que depois, quando se unem, fica com uma acurácia melhor, mais apurada, tá bom? Então, no resultado que a gente tem aqui, a gente vai ter um token que vai sair com uma representação nova vetorial, já não tem nada a ver com a de entrada, refinada, pronto para a próxima aula, pensa assim, para a próxima camada desse modelo que a gente está processando. É mais ou menos assim que funciona esse cálculo de forma abstraída para vocês entenderem. Mais do que só colocar esse cálculo na mão e fazer,

08:38

É isso que está funcionando por trás. Por que é importante fazer este cálculo? Primeiro ponto tem a não linearidade. A não linearidade é super importante aqui, porque cada camada de atenção que a gente tem é linear.

08:54

Então significa que mesmo que eu processe informações contextuais ali, você precisa incluir depois uma camada de não linearidade pra conseguir representar as coisas mais complexas, as correlações que a gente falou. Que na minha opinião é a grande sacada da Gen AI, né?

09:10

é conseguir aprender as relações profundas e cruzadas que a gente tem. Então o Feedforward vai conseguir cumprir esse papel adicionando tudo isso que a gente falou aqui pra fazer esse esquema que a gente falou de Position Wise Layers dentro do Feedforward. Então é mais ou menos assim que a coisa funciona. Um outro ponto que a gente tem aqui também é o raciocínio local.

09:36

A Feedforward age localmente dentro de cada um desses tokens ou palavras, como se fosse um processamento individual. Então ele vai conseguir fazer cada token reorganizar a informação que recebeu de atenção, criar uma nova representação vetorial mais enriquecida para depois jogar para a próxima camada. Então você tem esse raciocínio local para depois você transformar em global e conseguir evoluir na sua construção.

10:03

Bom pessoal, basicamente é isso quando a gente está falando de Position Wise Layers, espero que vocês tenham entendido, é uma coisa um pouquinho mais chata, eu tentei trazer da forma mais prática possível e mais simplificada, mas essa é outra camada que é adicionada nos Transformers quando a gente está falando de IA, beleza? Está começando a ficar mais complicado né? Começa a deixar a conversa um pouco mais complexa e começa a esquentar um pouco mais o cérebro, mas

10:31

Vamos lá, vamos seguir em frente que ainda tem muito mais coisa pra gente aprender por aqui, beleza? Um grande abraço!

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **W1 / W2** — Matrizes de peso  
- **B1 / B2** — Vetores de viés  
- **ReLU** — Unidade Linear Retificada (*Rectified Linear Unit*)  
- **xW1 + b1** — Primeira transformação linear aplicada ao vetor de entrada  
- **max(0, ·)** — Função de ativação que zera valores negativos e preserva os positivos  

**Resumo**  
A aula explicou as *Position-wise Feedforward Layers* no Transformer, destacando que essa etapa acontece depois do mecanismo de atenção. Enquanto a atenção mistura contexto entre tokens e identifica de onde vem a informação relevante, o feedforward processa cada token individualmente para refinar sua representação de forma local e independente. O instrutor usou a metáfora de uma conversa seguida de reflexão: a atenção seria a troca de informações entre posições da sequência, e o feedforward seria o momento em que cada posição interpreta internamente o que recebeu e transforma isso em uma nova ideia.

Do ponto de vista técnico, foi apresentada a estrutura típica do bloco feedforward: uma primeira transformação linear com `xW1 + b1`, seguida de uma não linearidade `max(0, ·)` e, por fim, uma segunda transformação com `W2` e `b2`. As matrizes `W1` e `W2` funcionam como pesos aprendidos que reorganizam e condensam a informação, enquanto `b1` e `b2` fazem o ajuste fino dos valores. A primeira projeção expande ou reconfigura o vetor do token em um espaço intermediário; a ativação elimina valores negativos, introduzindo não linearidade; e a segunda projeção produz a saída final refinada, pronta para a próxima camada.

A aula também enfatizou o significado de *position-wise*: a mesma rede é reutilizada em todas as posições da sequência, mas cada token passa por ela separadamente, com seus próprios valores. Isso permite que o Transformer combine duas responsabilidades complementares: primeiro, relacionar tokens por meio da atenção; depois, aprofundar semanticamente cada representação por meio do feedforward. O resultado é uma sequência de vetores mais ricos e úteis para modelar dependências complexas e apoiar tarefas como previsão do próximo token.

**Pontos de atenção**  
- A camada *feedforward* não faz a mistura entre tokens; essa função já ocorreu na atenção. Aqui o processamento é **individual por posição**.  
- O termo *position-wise* significa que a mesma rede é aplicada em todos os tokens, mas **com entradas diferentes**, o que gera saídas diferentes.  
- A primeira transformação `xW1 + b1` serve para **reorganizar e expandir** a informação do token, não para gerar a saída final.  
- A função `max(0, ·)` ou ReLU é essencial porque introduz **não linearidade**; sem isso, várias camadas lineares continuariam equivalentes a uma única transformação linear.  
- Valores negativos são **zerados** pela ativação, o que ajuda a filtrar informações menos úteis naquele estágio.  
- `W1` e `W2` são **matrizes de pesos aprendidas**; `b1` e `b2` são **termos de viés** que ajustam as transformações.  
- O bloco feedforward existe para **refinar localmente** a representação contextual recebida da atenção, preparando o token para a próxima camada.  
- A separação entre atenção e feedforward é uma boa prática central do Transformer: primeiro **relacionar posições**, depois **aprofundar a representação** de cada uma delas.