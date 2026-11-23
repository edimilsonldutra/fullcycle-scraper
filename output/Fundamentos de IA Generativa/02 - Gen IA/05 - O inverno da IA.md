Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16370)

## Resumo da aula

O inverno da IA foi um período de frustração em que a promessa técnica superou a capacidade real de execução. Entre as décadas de 1970 e 1980, os sistemas não conseguiam resolver problemas complexos porque faltavam processamento, dados e métodos capazes de lidar com linguagem, imagem e som em escala útil. O efeito prático foi a queda de investimento e de interesse, já que a IA baseada em regras e redes muito simples não sustentava as expectativas criadas. Esse momento importa porque mostra que boas ideias não bastam quando a infraestrutura computacional ainda não permite implementá-las com eficácia.

A principal barreira daquele período não era apenas teórica, mas operacional. Sem capacidade de processamento e sem volume de dados para treinamento, modelos não conseguiam aprender padrões ricos nem generalizar para tarefas abertas. Isso explica por que reconhecimento de fala, compreensão de linguagem natural e visão computacional eram objetivos distantes: o problema não era só formular a técnica, mas executar o treinamento com recursos compatíveis. Retomando a base já vista sobre a viabilidade recente da Gen AI, essa convergência tecnológica ainda não existia naquele momento.

John Hopfield ajudou a recolocar as redes neurais no debate ao introduzir uma estrutura em que a saída de neurônios pode realimentar outras partes da rede, inclusive a si mesma. Essa ideia rompe com o fluxo puramente linear de entrada e saída e aproxima o modelo de um comportamento de estado interno, no qual o sistema preserva e reutiliza informação anterior. A noção de memória associativa surge daí: ao receber um padrão incompleto, a rede tenta convergir para uma configuração coerente já aprendida. Esse avanço foi importante porque abriu caminho para tratar sequências e dependências, algo essencial para linguagem e sinais temporais.

Redes neurais recorrentes, ou RNNs, são arquiteturas projetadas para processar dados em sequência, como texto, áudio e séries temporais. Em vez de tratar cada entrada como isolada, elas carregam informação de passos anteriores para influenciar o processamento atual. Isso as tornou relevantes para tarefas como reconhecimento de fala e modelagem de linguagem, nas quais a ordem dos elementos altera o significado. A limitação histórica dessas redes estava em treinar dependências longas com estabilidade, mas elas representaram uma transição decisiva entre modelos estáticos e sistemas com noção de contexto temporal.

A mudança de regras determinísticas para modelos probabilísticos foi uma ruptura metodológica. Em vez de responder apenas com “sim” ou “não” a partir de regras explícitas, o sistema passou a estimar qual hipótese é mais plausível dado o contexto observado. O exemplo do “boneco de neve” ilustra isso: a máquina não precisa ter certeza absoluta sobre o objeto, mas precisa atribuir maior probabilidade à interpretação mais consistente com os sinais disponíveis. Essa transição foi crucial porque problemas reais quase sempre envolvem ambiguidade, ruído e informação incompleta.

Cadeias de Markov modelam sequências assumindo que o próximo estado depende do estado atual, ou de uma janela limitada de estados anteriores. Esse formalismo foi útil para prever a próxima palavra, estimar transições em sinais e estruturar tarefas em que a ordem importa. Embora sejam muito mais simples que modelos modernos, elas introduziram uma forma operacional de tratar linguagem e sequência como processos probabilísticos. Em aplicações iniciais, isso ajudou em jogos, música e nas primeiras tentativas de modelagem textual.

Reconhecimento de fala ganhou tração quando a IA passou a usar estatística para lidar com incerteza acústica e linguística. O sistema não “ouve” como um humano; ele compara sinais sonoros com padrões prováveis e escolhe a interpretação mais plausível. A mesma lógica vale para classificação automática de dados, em que o objetivo é decidir a qual classe um item pertence mesmo quando os sinais são imperfeitos. Esses problemas ajudaram a consolidar a visão de aprendizado de máquina orientada por probabilidade, em vez de depender apenas de regras escritas manualmente.

Naive Bayes é um classificador probabilístico que estima a chance de um item pertencer a uma classe com base em evidências observadas. Seu uso em filtro de spam se tornou emblemático porque transformou um problema cotidiano em uma aplicação prática de IA: dado o conteúdo de um e-mail, o sistema calcula se a mensagem se parece mais com spam ou com comunicação legítima. Retomando o exemplo de spam já conhecido, o ponto novo aqui é a virada técnica: a solução deixou de depender de listas rígidas de regras e passou a operar por probabilidade condicional. Isso marcou uma fase em que a IA voltou a entregar valor concreto antes mesmo da explosão generativa atual.

A partir de 2010, o avanço de GPUs, Big Data e infraestrutura permitiu treinar redes profundas em escala muito maior. O ponto central não é redefinir Deep Learning, já visto antes, mas observar seu papel histórico: ele removeu parte do bloqueio que impedia ideias antigas de se tornarem úteis. Com mais camadas, mais dados e mais computação, tarefas como tradução automática e reconhecimento de fala passaram a atingir desempenho prático. A área saiu da experimentação limitada e voltou a crescer com resultados visíveis.

GANs são arquiteturas compostas por dois modelos em competição: o gerador produz amostras sintéticas e o discriminador tenta distinguir o que é real do que foi gerado. Esse jogo adversarial força o gerador a melhorar continuamente, porque ele só “vence” quando produz saídas suficientemente realistas para enganar o discriminador. O resultado foi um salto na geração de imagens, rostos e cenários artificiais, mostrando que a IA podia não apenas classificar dados, mas sintetizar novos artefatos convincentes. Esse mecanismo foi uma etapa importante na transição para sistemas explicitamente generativos.

A arquitetura apresentada em Attention Is All You Need mudou o processamento de linguagem ao substituir a dependência sequencial estrita por mecanismos de atenção, já referenciados anteriormente. O ganho histórico foi permitir que o modelo relacionasse partes distantes da entrada com mais eficiência computacional e melhor captura de contexto. BERT, lançado em 2018, mostrou o impacto dessa mudança em representação e compreensão de linguagem, enquanto os modelos generativos posteriores ampliaram esse avanço para geração de texto em larga escala. A ruptura aqui não foi apenas melhorar um algoritmo anterior, mas mudar a forma de modelar dependências em linguagem.

O boom a partir de 2020 não surgiu do nada; ele é o resultado acumulado de várias viradas técnicas. O campo passou por um ciclo recorrente de expectativa, limitação, nova abordagem e ganho obtido: regras falharam em escalar, probabilidade lidou melhor com incerteza, redes profundas exploraram mais dados e computação, GANs ampliaram a geração e Transformers consolidaram o uso de contexto em escala. Retomando a diferença já conhecida entre IA tradicional e generativa, o ponto decisivo aqui é histórico: a geração moderna só se tornou viável quando essas camadas de evolução finalmente se combinaram.

## Transcrição

00:01

E aí pessoal, chegamos ao inverno da IA. Quem aqui já ouviu falar deste momento? O inverno da IA foi, querendo ou não, um grande momento ruim para quem era muito focado em IA. Então aqui, e até isso é um dos pontos que trazem até hoje alguns pensamentos. Esse grande inverno da IA, que foi entre 1970 e 1980,

00:26

foi quando a gente começou a ver que os sistemas da época não conseguiam resolver problemas complexos, ou seja, a galera criou muita expectativa, a gente tava falando de rede neural já, tava falando ali de começar algumas estratégias interessantes pra resolução de problemas pra uma máquina que pensa, só que criou uma expectativa muito alta.

00:47

Galera colocou uma grana, teve investimento, etc. Galera foi atrás pra fazer isso acontecer. Só que a gente se frustrou. O que a gente começou a ver? Que a gente não tinha poder de processamento de dados, como eu falei, pra ter sistemas baseados em regras de redes neurais simples ali, e a gente não tinha

01:06

como trabalhar problemas complexos quando a gente estava falando das ideias de processamento mais normais ali como eu falei para vocês de sei se não então ali a gente tinha muita dificuldade para fazer a coisa andar então a gente não conseguia por exemplo entender a linguagem natural que é o básico que a gente vê hoje acontecendo a gente não conseguia

01:26

reconhecer a imagem, a gente não conseguia reconhecer som, então a IA não conseguia reconhecer, como se ela fosse cega, surda e muda. Ela não conseguia estar próximo do nosso linguajar e ela não conseguia aprender também, porque a gente não tinha dado o suficiente para o aprendizado. Então esse período ele foi conhecido como o primeiro inverno da IA.

01:47

Então ali os investimentos começaram a cair drasticamente, a gente começou a ter menos gente interessada e com isso poucas pessoas ficaram ainda indo atrás deste sonho que seria um computador que consegue trabalhar como uma inteligência artificial.

02:02

E daí chega ali, durante esse inverno da IA também, algumas coisas importantes acontecendo mesmo assim, tá bom? Então 1982, foi mais pra 82, tá aqui 1970, 1980, mas a coisa vingou menos mesmo em 82, apesar de ter sido os

02:21

as ideias começarem muito antes disso, começou entre 1970 e 70, deve ter começado em 77, 78 se não me engano, mas em 1982 a coisa vingou sobre uma coisa super importante, que foram as redes neurais recorrentes, então o John Hopfield, ele colocou pra gente um novo paradigma, que foi de colocar

02:44

as redes neurais frequentes, onde a saída de um neurônio podia ser a entrada de outro. Então pensa, antes a gente não tinha essa conexão neural bem estruturada, a saída de um neurônio já era a saída, agora não, a gente começa a colocar uma cadeia de saída e entrada de neurônios, e com isso a gente consegue ter uma ideia

03:05

de conexão neural como a gente tem na mente humana, possivelmente. E essa saída desse neurônio poderia ser a entrada para esse próprio neurônio. Então a gente para de querer ter só uma linha de entrada e saída, ou seja, pergunta e resposta, a gente começa a ter pergunta, resposta, que entra como pergunta para outro neurônio, que entra como resposta, que pode ser a pergunta para esse primeiro neurônio. Então essa

03:25

Essa complexidade, essa ideia diferente, começou a trazer uma outra ideia. Então aqui a gente começa a pensar um pouquinho na ideia de simulação de uma memória associativa que a gente tem no ser humano. E daí isso a gente consegue aproximar mais do que a gente chama da rede neural dos humanos e a gente começa a pensar em ter como lembrar padrões incompletos para conseguir completá-los ao longo do tempo. E daí isso é um paradigma extremamente importante que ajudou na evolução pós-inverno da IA.

03:55

Então, quando a gente fala do pós-inverno da IA aqui, quando a gente fala do pós-inverno da IA, na verdade, quando ela estava chegando ali no finalzinho desse inverno, a gente começa também a discutir um pouquinho dos modelos probabilísticos, então a gente começa a usar mais probabilidade, não lógica básica direta de resposta de sim ou não, a gente começa a entrar na ideia de probabilidade,

04:18

E a gente tem aqui algumas coisas acontecendo que a gente ouve falar muito até hoje então. Então a gente fala muito das cadeias de Markov, a gente começa a ter isso entrando no dia-a-dia ali da discussão sobre ela.

04:33

Então a gente começa a falar de, por exemplo, algumas tarefas que começam a aparecer como reconhecimento de fala e classificação automática de dados, que isso vai ajudar muito a gente na evolução dos próximos passos. Então a gente fala muito de reconhecimento de fala nesse primeiro momento e classificar os dados que depois vão ser usados para treinamento de IA, que consegue fazer a associação e essa visão mais orientada a aprendizado de máquina, tá bom? Então a gente começa

04:59

a fazer isso de que forma? Usando a estatística para resolver o problema que a gente não tinha, que era de incerteza. Antes a gente estava muito dentro de certeza, é sim ou não? Só que a nossa mente não é certa de tudo. Então se eu perguntar para você assim, cara, o que você está vendo na sua tela aqui é um boneco de neve? Você vai me responder, sim, mas podia ser de algodão, podia ser de várias outras coisas, certo? Então a gente trabalha com um certo grau de incerteza

05:24

para responder algo com certeza. Então eu falo, é um boneco de neve? Sim, porque o contexto me diz que isso é um boneco de neve. Provavelmente isso é um boneco de neve. Agora, será que é um boneco de neve mesmo? Pode não ser, pode ser duas bolas de sorvete. Então a gente pode pensar em outras tantas coisas que poderiam ser isso que está aqui na nossa tela. Mas o que a gente faz? Dentro desse contexto a gente vê qual a maior probabilidade de dar isso como certeza. Antes as máquinas não conseguiam fazer isso. Acho que essa é a melhor forma de explicar a grande mudança que a gente tem

05:54

neste momento. Então a estatística começa a tomar conta ali em 1990 e nos anos 2000. Aqui a gente já começa a ter um aumento da IA de novo vindo para o hype do momento até chegar no que a gente tem hoje. Então a gente começa a ter um aumento de dados, então a gente começa a ter um poder computacional mais bacana, a ideia de coletar dados, guardar dados, modelos estatísticos usados para conseguir

06:21

categorizar e usar esses dados, e isso faz a gente conseguir voltar para o jogo, trazer a IA de novo para um alto nível de discussão. Então, por exemplo, o Knife Banes aqui que eu coloquei para você, Knife Banes na verdade, ele se destacou ali como um classificador que foi baseado em probabilidade condicional. Então aqui a gente começa a olhar o seguinte,

06:46

Qual a probabilidade que eu tenho de um item pertencer a uma classe, dado o seu grau de certeza ou incerteza. Um pouco do que eu fiz agora de brincadeira com vocês. Isso foi muito utilizado aonde? Aí que começa a entrar IA no nosso dia a dia e isso eu acho legal. Quando a gente começa a olhar pra isso, começa a ter aplicação prática.

07:07

Então, aqui em 1990 e nos anos 2000, a gente tinha um problema e veio uma solução. Isso é muito interessante de ver, porque quando o problema aparece, a solução vem mais rápido. A gente tinha um problema, a gente recebeu uma porrada de spam no e-mail. E aonde que a gente usou esse modelo probabilístico pra saber se aquilo é um spam ou não?

07:24

no modelo de classificação de spam. Antes a palavra spam nem era conhecida, nem era utilizada se você parar pra usar. A gente sabia que recebia ali spams, mas era um monte de lixo na nossa caixa até o momento que a gente deu a nomenclatura e depois tentou achar uma resolução pra isso. A IA veio e conseguiu resolver isso. Então hoje no seu email você já usa isso muito e nem nota.

07:44

Você já percebeu que a maior parte das vezes que cai algo em spam, ele é realmente spam? Cada vez mais isso tem ficado com mais acurácia, consegue fazer isso de uma forma melhorada. Então a gente tem aqui o primeiro modelo de IA que trouxe benefícios para a nossa vida. Imagina você ter que ficar tirando spam da sua caixa ali na mão.

08:04

E daí quando a gente começa a ir mais à frente aqui, a gente começa a ver essas cadeias de Markov, como eu falei para vocês, que começam a modelar as sequências que a gente tem de aprendizado para permitir a próxima palavra de um texto, por exemplo. Então pense o seguinte, antes...

08:22

eu tinha aqui uma linguagem de máquina que conseguia até entender e compreender um texto, mas não conseguia prever a próxima palavra e com isso sem a previsão da próxima palavra eu não consigo conversar, porque eu não consigo compreender um texto inteiro, prever a próxima palavra para entender o contexto daquilo e daí com isso

08:41

é conseguir ter uma conversa, trocar, te dar uma nova cadeia de palavras com base no que eu acabei de entender. Então esse modelo de Markov, essas visões aqui de estatística e de modelo de sequência começa a ter isso aqui utilizado principalmente ali para jogos e músicas, você já consegue compreender um modelo de sequência de coisas sendo feitas, sendo criadas, então aqui você já começa a ter um pouquinho disso acontecendo.

09:09

E aqui, mesmo menos inteligente do que a gente conhece hoje, o modelo estatístico já começa a mostrar eficiência. Então, a gente já começa a ver um caminho por onde resolver as coisas. Lógico que ainda, de novo, eu tô falando pra vocês de uma forma mais bonita e bacana, mas a gente ainda tinha uma porrada de problema pra resolver aqui. Ainda eram umas coisas um pouco meio tapadas, assim por dizer. E daí, quando a gente chega ali entre 2010 e 2014, a gente começa a entrar na Deep Learning.

09:35

O Deep Learning começa a aparecer com a popularização do conceito de Big Data e com as GPUs. Então aqui a gente começa a ganhar muita força, a gente começa a ter um poder computacional gigante para a resolução de vários outros problemas, como por exemplo armazenamento de dados, etc. E com isso a gente usa disso para adicionar as camadas aqui de Deep Learning

09:57

para as redes neurais, tá bom? E com isso a gente começa a ter técnicas que antes eram limitadas por conta dos recursos computacionais, lembra que a gente falou lá atrás da limitação? A gente começa a aplicar isso em larga escala e daí começa a mostrar algo um pouco mais promissor. Então a gente começa a ter que usar as redes neurais aqui

10:17

sendo utilizadas para algumas coisas mais legais. A gente começa a ter elas sendo usadas para reconhecimento de fala, tradução automática, começa a aparecer no nosso dia a dia ali um Google Translate e assim por diante e outras tantas outras ferramentas que vem para ajudar a gente no dia a dia.

10:34

E aí quando chega em 2014, a gente começa a ter as GANs chegando aqui com a gente, que são as Generative Adversarial Networks. Essas ideias aqui vêm pra gente com basicamente dois modelos. Eu tô pensando num jeito de explicar isso da melhor forma pra vocês.

10:54

São dois modelos que competem para gerar os dados realistas, tá bom? Um deles é o gerador e o outro é o discriminador. Então é como se fosse alguma... Uma ideia de alguém gerando e alguém vendo se isso tá certo ou não. Então eles aprendem juntos. Um modelo vem aqui, cria e o outro fala, isso tá certo ou tá errado, tá certo ou tá errado, tá certo ou tá errado. E daí com isso, com base em rostos, imagens, até em ambientes fictícios, muitas das vezes,

11:17

a gente começa a conseguir treinar essa IA pra ela ser capaz de aprender e de criar novos conteúdos. Esse modelo de aprendizado e de... mais do que de aprendizado, de ensino de máquina, porque a gente tá falando aqui da máquina aprendendo, mas também o modelo de como eu ensino essa máquina a aprender, que foi uma grande...

11:38

uma grande sacada e fez a gente conseguir evoluir um pouco mais nessa estratégia de IA, tá bom? E daí depois chega o grande cara da moda que a gente fala até hoje, que todo mundo usa, que são os Transformers, a revolução dos Transformers em 2017. Aqui tem esse artigo que é Attention is all you need, que foi muito bem aceito pela comunidade, onde a gente apresenta os Transformers e aqui

12:06

Essa apresentação dos Transformers traz uma arquitetura que realmente muda todo o conceito de processamento de linguagem natural. Os Transformers chegam para ajudar muito a gente e eles usam a atenção para entender melhor o contexto do que a gente está falando. Então, pensa assim, diferente das redes neurais recorrentes que a gente tinha lá atrás, eles usam o modelo de atenção para focar em um determinado dado, um determinado...

12:31

uma determinada parte do dado de entrada que você tem, pra conseguir compreender o contexto inteiro e com isso ser mais eficiente. Então essa ideia, essa inovação, ela vem pra criar alguns modelos que vão ajudar a gente, como o BERT, que foi criado em 2018, e depois o chat de GPT,

12:49

que consegue trazer pra gente isso pra criação de textos, e que foi o boom que a gente viu aparecendo nos modelos de IA mais modernos que a gente conhece. Depois eu vou entrar muito mais a fundo com vocês em Transformers, em todos esses algoritmos ou frameworks que a gente pode utilizar, mas basicamente essa foi a ideia

13:10

da evolução da IA ao longo dos tempos aí. E daí quando a gente chega em 2020, a gente tem os modelos generativos aparecendo por conta dos Transformers principalmente e que começa a ter um boom. Já GPT-3, 4 pra geração de texto, vem o DALL-E pra geração de imagens, vem o Sora muito forte, tem outros tantos que a gente pode citar aqui.

13:31

Mas os principais que a gente olha aqui, agora o Viu 3 chegando, estourando, mandando muito bem. Então a gente tem uma porrada de outras inteligências artificiais chegando pra conseguir ajudar a gente, todas elas numa visão mais generativa. Aí a começa a aprender a falar, a gerar imagem, a fazer tudo de uma forma muito mais eficiente.

13:51

E agora a gente tá falando da IA podendo fazer tudo quanto é tipo de coisa com a gente, e a gente vai conseguir ter isso cada vez mais no nosso dia a dia, com a criação, com a ideia de ajudar a gente, e por isso que a gente tá aqui, pra ver como que isso vai ajudar a gente daqui pra frente. Acabou a história. Chega de contar história.

14:11

no próximo capítulo a gente vem pra falar um pouquinho de como a gente vai usar isso, como isso casa com o nosso contexto aqui nesse curso, beleza? Obrigado por ficar até aqui, obrigado por me ouvir e já já a gente volta pra conversar um pouco mais. Um abraço!

## Resumo IA

**Abreviações**

- **IA** — Inteligência Artificial
- **RNNs** — Redes Neurais Recorrentes
- **GPU** — Unidade de Processamento Gráfico
- **Big Data** — grande volume de dados
- **GANs** — Redes Adversariais Generativas
- **BERT** — Bidirectional Encoder Representations from Transformers
- **GPT** — Generative Pre-trained Transformer
- **DALL·E** — modelo generativo de imagens da OpenAI
- **Sora** — modelo generativo de vídeo da OpenAI

**Resumo**

A aula apresentou a evolução histórica da Inteligência Artificial, começando pelo chamado inverno da IA, período entre as décadas de 1970 e 1980 em que houve frustração com as promessas da área. O instrutor explicou que, embora existissem ideias promissoras, faltavam recursos computacionais, volume de dados e métodos capazes de lidar com problemas complexos como linguagem natural, visão e reconhecimento de fala. Isso levou à queda de investimentos e interesse, mostrando que boas ideias só se tornam viáveis quando há infraestrutura adequada para sustentá-las.

Em seguida, foi destacada a contribuição de John Hopfield e das redes neurais recorrentes, que permitiram a realimentação entre neurônios e a criação de uma noção de estado interno e memória associativa. A aula conectou esse avanço à necessidade de lidar com sequências e dependências temporais, algo essencial para linguagem e sinais. Depois, o foco passou para a mudança de uma IA baseada em regras para uma abordagem probabilística, em que o sistema estima a hipótese mais plausível diante de incertezas, em vez de responder apenas com sim ou não.

Nesse contexto, foram citadas as cadeias de Markov, o reconhecimento de fala e a classificação automática de dados como exemplos de modelos estatísticos aplicados a problemas reais. O instrutor usou o exemplo de spam para mostrar como o Naive Bayes ajudou a transformar uma necessidade cotidiana em uma aplicação prática de IA, baseada em probabilidade condicional. A partir dos anos 2010, com o avanço de GPUs, Big Data e capacidade de armazenamento e processamento, as redes profundas passaram a escalar e a entregar resultados mais úteis em tarefas como tradução automática e reconhecimento de fala.

A aula também abordou as GANs, formadas por gerador e discriminador em competição, como marco importante na geração de dados sintéticos realistas, especialmente imagens e rostos. Por fim, foi apresentada a revolução dos Transformers, iniciada com o artigo Attention Is All You Need, que substituiu a dependência sequencial estrita por mecanismos de atenção para captar contexto de forma mais eficiente. Essa mudança abriu caminho para modelos como BERT e, depois, para o boom de modelos generativos a partir de 2020, como GPT, DALL·E e Sora, consolidando a IA generativa como resultado da combinação entre avanços em algoritmos, dados e computação.

**Pontos de atenção**

- O inverno da IA mostrou que **expectativa sem infraestrutura** gera frustração e queda de investimento.
- A limitação histórica não era apenas teórica; havia **falta de processamento e de dados** para treinar modelos úteis.
- Sistemas baseados apenas em **regras e lógica determinística** não lidam bem com ambiguidade e incerteza.
- A mudança para abordagens **probabilísticas** foi decisiva para tratar problemas reais.
- Em tarefas como linguagem e fala, a **ordem e o contexto** importam; modelos que ignoram sequência perdem desempenho.
- As **cadeias de Markov** ajudam, mas têm limitação por dependerem de estados anteriores próximos.
- O exemplo de **spam** ilustra a importância de substituir regras rígidas por classificação estatística mais flexível.
- O avanço do Deep Learning só se viabilizou com a combinação de **GPUs, Big Data e mais capacidade computacional**.
- As **GANs** exigem equilíbrio entre gerador e discriminador; a competição é central para melhorar a qualidade das saídas.
- Os **Transformers** mudaram a modelagem de linguagem ao priorizar atenção e contexto, superando limitações de arquiteturas sequenciais.
- O boom da IA moderna não surgiu repentinamente; ele é resultado de **evolução acumulada** de várias técnicas e capacidades tecnológicas.