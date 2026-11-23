Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16400)

## Resumo da aula

Decoder-only é a variação do Transformer especializada em geração textual passo a passo. Em vez de processar a sequência inteira com visão bidirecional, ele restringe o cálculo ao histórico disponível para prever o próximo token. Essa escolha reduz complexidade para tarefas generativas e alinha a arquitetura ao problema central de completar texto, responder e continuar sequências de forma coerente.

A causal self-attention é o mecanismo que impede cada posição de acessar tokens futuros. Cada token pode atender apenas a si mesmo e aos tokens anteriores, o que força o modelo a construir a saída da esquerda para a direita. Essa restrição existe porque, na geração, o próximo token precisa ser inferido apenas a partir do contexto já produzido, não de informação que ainda não existe no momento da predição.

A máscara triangular inferior implementa essa restrição diretamente na matriz de atenção. Em uma sequência como “o cachorro correu rápido”, a posição de “correu” pode usar “o” e “cachorro”, mas não pode acessar “rápido”; a posição de “rápido” já pode usar todo o histórico anterior. O triângulo de zeros e permissões garante que o modelo libere contexto gradualmente e não “trapaceie” olhando para o futuro durante treino ou inferência.

A matriz de atenção pode ser lida como uma tabela de visibilidade entre posições da sequência. Sem máscara, todas as posições poderiam se enxergar; com máscara causal, cada linha só enxerga a diagonal e o passado. Isso transforma a previsão do próximo token em um processo temporal consistente: a cada passo, o contexto cresce, mas nunca inclui informação futura.

A explicação com palavras serve como simplificação visual, mas o cálculo real acontece sobre tokens e, mais profundamente, sobre vetores. Na prática, a matriz de atenção relaciona representações vetoriais das posições da sequência, não palavras literais. A máscara continua válida nesse nível: ela não depende do significado textual explícito, e sim da posição relativa entre elementos da sequência.

Retomando a diferença para RNNs, o Transformer não precisa processar token por token de forma sequencial para respeitar ordem. A noção de posição continua presente por meio da ordenação da sequência, e a máscara causal impõe a direção temporal mesmo com processamento paralelo das camadas. O resultado é combinar paralelismo computacional com comportamento autoregressivo controlado.

A multi-head attention com máscara causal faz duas coisas ao mesmo tempo: restringe o acesso ao passado e permite múltiplas leituras do mesmo contexto. Cada head aprende relações diferentes entre os tokens anteriores, como dependências sintáticas, semânticas ou padrões locais de continuação. Isso aumenta a capacidade do modelo de decidir quais partes do histórico realmente importam para prever o próximo token sem violar a causalidade.

O feedforward position-wise é uma transformação aplicada individualmente à representação de cada posição após a atenção. Ele não mistura posições entre si; em vez disso, refina localmente a informação já contextualizada e ajuda a modelar padrões não lineares. Essa etapa amplia a capacidade expressiva do bloco decoder e melhora a combinação de significado em contextos mais abstratos.

Layer norm estabiliza os valores internos do modelo para evitar escalas descontroladas durante o treinamento e a inferência. As conexões residuais preservam informação das camadas anteriores ao somá-la à saída transformada, o que facilita o fluxo de gradiente e reduz perda de informação ao empilhar muitos blocos. Juntas, essas duas peças tornam o decoder-only treinável em profundidade e mais estável numericamente.

Uma forma útil de visualizar a máscara causal é pensar em uma prova em que a resposta atual só pode usar o que já foi resolvido antes. Ao responder a questão 6, faz sentido consultar as questões 1 a 5, mas não a 8, 9 ou 10. O decoder-only opera com a mesma disciplina: usa o passado disponível, bloqueia o futuro e, por isso, consegue gerar texto de maneira consistente token a token.

## Transcrição

00:00

Fala galera, beleza? Vamos falar agora então do próximo carinha aqui dentro da nossa aula sobre arquiteturas e tipos de modelo, tá bom? Então a gente vai falar um pouquinho agora do decodificador. Então a gente falou lá da parte de encoder e agora a gente vai falar do decoder only, beleza? Então vamos falar do decoder only. Então a gente tá no mesmo momento histórico.

00:23

Chegamos lá em 2017, teve o paper Attention Is All You Need, e em cima disso a gente começa a discutir as arquiteturas de Transformer. E a gente separou no primeiro momento falando só do encoder only. Agora vamos falar do decoder only, o próximo passinho dessa coisa. O Transformer trouxe os dois conceitos, vamos separar os dois então pra gente ser mais eficiente em outro aspecto, em outra forma de trabalho.

00:48

Qual forma de trabalho é essa? Na geração textual, que a gente já falou um pouco lá atrás quando a gente estava falando dos nossos modelos, beleza? Então aqui, quando você começa a separar, o que vai acontecer? A mesma coisa que a gente falou no encoder, você está focando em um tipo de atividade e com isso você vai ter menos complexidade arquitetural, você vai ter mais foco para tentar prever o próximo token com base no seu histórico,

01:14

e você não vai perder a sua atenção olhando de forma bidirecional. O modelo vai ser mais eficiente, vai conseguir te trazer um resultado melhor, vai ser mais barato e vai ser mais rápido de executar do que você estivesse olhando para o todo. Então é só gerar um resultado mais eficiente com base em tudo isso que eu te falei. Então essas tarefas autoregressivas vão ter mais facilidade utilizando o Decoder Only.

01:40

Por exemplo, a geração de storytelling vai ser facilitada, a geração de complemento textual, a geração de respostas. Basicamente, essas estratégias são evoluídas com base nesse tipo de arquitetura. Fechou? E como é que isso funciona?

01:56

Você tem uma estrutura interna avançada ali dentro do Transformer, quando a gente tá falando do Decoder Only, que chama Causal Self-Attention, que é a atenção autoregressiva, o melhor jeito de falar dela, tá? Cada token, ele só vai poder ver o que tem pra trás, ele só vê o passado, ele não vê o futuro. Ele foca a sua atenção em entender o passado pra conseguir descobrir com a próxima palavra. Ele não fica focando a sua atenção no que vem pela frente.

02:26

beleza? e para isso uso uma estratégia que eu vou explicar agora para vocês com um pouquinho mais de detalhe para vocês entenderem como funciona o CERN dessa operação dessa arquitetura que é uma máscara triangular inferior tá bom? essa máscara triangular inferior é uma estratégia matemática para você transformar uma matriz para que ela consiga fazer isso que a gente está falando então vou tangibilizar em cálculo basicamente

02:54

Não posso dizer que em matemática, nem tanto em cálculo. Eu vou tangibilizar em cálculo o que a gente tá falando aqui de forma mais abstrata. Beleza? Então vamos falar um pouquinho dela pra vocês entenderem. Quando vocês olham essa matriz, eu deixei aqui a matriz porque senão fica muito complicado de vocês entenderem comigo só falando, vai ficar confuso. Então vamos olhar pra matriz. Matriz 1, a primeirinha aqui que a gente tá olhando.

03:15

Quando a gente olha pra ela, a gente vai fazer o seguinte, a gente vai falar sobre a seguinte frase, o cachorro correu rápido, beleza? Essa é a frase, o cachorro correu rápido. Dentro dessa frase, eu vou pegar cada palavra, o cachorro correu rápido, e vou transformar elas em colunas, beleza? Então são colunas.

03:35

e eu vou fazer a mesma coisa para baixo transformando em linhas o cachorro correu rápido e então você vai ter isso aplicado virou uma matriz beleza porque que essa matriz tá com check em tudo porque neste momento estou te dizendo que se eu colocasse isso para o meu modelo ele olharia tudo tudo que tá com check tal que ele poderia olhar tá sem mascaramento

03:56

Agora, quando a gente fala da máscara triangular inferior, você muda isso para o segundo modelo que a gente está vendo ali. No segundo modelo vocês estão vendo que tem um triângulo sendo formado?

04:08

entre zeros e cheques. O que tá com zero significa que ele não tá vendo. O que tá com cheque significa que ele está vendo. Agora vamos colocar isso numa visão temporal. Imagina que no primeiro momento ele tá com só a palavra o pra prever. Então ele tá enxergando o que? O e o. Certo? Em cima o, do lado o. Chegou no segundo momento. Ele tá tentando prever o cachorro. Beleza? Então ele vai conseguir ver o que? O

04:38

e prever o cachorro. Então, quando ele chegar no cachorro, ele tá vendo o O, ele vai prever o cachorro e daí ele vai ter atenção nos dois. Então, ele vai ver o O e vai ver o cachorro. Aí, depois, você vai pro correu. A mesma coisa. Correu, correu. Ele consegue ver cachorro e O, prever correu.

04:57

Quando você vai para o rápido ele consegue ver o cachorro correu e prever o rápido. Você viu que você fechou uma matriz onde você a cada passinho que você dava você liberava o passo futuro. Isso é uma matriz onde você mostra para o seu modelo que é para ele focar a atenção na próxima palavra e não no todo. Por que isso é importante gente? Se você tivesse um modelo que você não tem o mascaramento triangular

05:24

inferior, você ia fazer o que? Logo na hora que você estivesse só com o, você só tá com o preparado, possivelmente você podia tentar prever ali o rápido, e daí você ia prever o rápido e ia prever errado, porque o seu Transformer ele não ia conhecer as demais palavras e a probabilidade dele chegar no rápido seria muito baixa, ele ia fazer meleca

05:47

e ia gerar aqui um modelo que alucinou possivelmente. Então aqui quando você coloca esse mascaramento, você consegue facilitar esse tipo de estratégia, beleza? E tá Nathan, pô, ficou fácil, né? Mas não é bem assim, eu simplifiquei a conversa pra gente, tá bom? Quando você olhar essa matriz no dia a dia,

06:07

caso você pegue uma, você não vai olhar primeiro palavras, você vai olhar tokens. Então, se você transformasse essa matriz em um passo menos abstrato, são tokens, não são palavras. Então, possivelmente ela ia ser um pouquinho maior, porque você ia ter que quebrar aqui em tokens.

06:22

Mas ele vem em tokens? Não, porque ele é um computador. Então por trás o que ele tá vendo são vetores, nem são tokens. Ele tá vendo uma matriz com vetor e vetor. Beleza? Esses vetores transformaram em uma matriz, ou seja, essa brincadeirinha aqui fica gigante.

06:40

com vetores e dentro desses vetores eu vou fazer esse mascaramento para ele conseguir focar atenção de cálculo probabilístico na próxima no próximo touca no próximo vetor beleza então é mais ou menos isso abstrai um pouco para ficar mais fácil para a gente entender e deixa eu falar com vocês então para quem pode não ter pego ainda eu gosto de trazer sempre algum tipo de abstração

07:05

Vamos colocar uma historinha aqui. Imagina que você é um aluno e está fazendo uma prova de 10 perguntas. E você está na pergunta número 5. O que aconteceria nesse esquema? Você pode olhar as perguntas de 5 a 1, que são as que você já respondeu. Respondeu 1, 2, 3, 4, 5. Essa você pode ver. Você pode olhar a que está rolando agora, a 6, que é a que você está tentando responder. Ou seja, você está focando a sua atenção na sexta pergunta, na sexta resposta que você tem que dar.

07:35

Mas você não está lendo a décima, a nona, a oitava. Por quê? Porque se você lê a décima, você vai perder sua atenção e não vai focar na quinta. Na sexta você dá a resposta da décima, você vai perder sua atenção. Então aqui o que eu estou dizendo é que você vai focar na quinta.

07:52

sexta você não vai mais olhar mais nada vai olhar para o amiguinho do lado vai tentar colar você vai olhar só aquela pergunta então eu tô fazendo o que é um modelo de self attention para você focar naquela ali beleza então é basicamente essa ideia que a gente faz com esse tipo de mascaramento tá bom então essa máscara

08:11

Em resumo, ela vai bloquear a atenção para o futuro e focar no presente, com base nos seus aprendizados passados. Olha que bom, se a gente conseguisse fazer isso como ser humano, a gente ia ter menos ansiedade. Ia ser legal, vamos tentar colocar aqui uma máscara triangular inferior para todo mundo. Então aqui, modelos autoregressivos como o GPT, por exemplo, usam esse tipo de estratégia. Isso vai garantir o quê? A consistência entre o treino,

08:37

e a inferência que a gente tem de tokens, beleza? Isso funciona então como um tampão visual para o seu transform, para o seu LLM conseguir focar naquilo que ele está fazendo naquele momento, beleza? Basicamente é isso, é assim que funciona. Aí você vai falar para mim o seguinte, mas Nathan, esse mecanismo, como que ele funciona?

09:00

com essa estrutura temporal do modelo, sendo que ele não tem uma RNNS. Uma RNNS. Por que que ele não... Ele... Eu penso o seguinte, quando eu abro ele em multi-thread, se eu puder falar desse jeito, ou seja, em várias camadas, como a gente falou que os Transformers conseguem processar, eu não tenho mais aquela dependência de RNNS pra fazer desse jeitinho que eu falei pra vocês, certo? Então, na teoria, eu não tenho como fazer essa brincadeirinha.

09:28

O que acontece? Por mais que o Transformer não processe palavra por palavra como uma RNNS, uma RNN por exemplo, ele ainda precisa respeitar a ordem das palavras, porque ele leva com ele aquela ordenação que a gente falou.

09:43

Essa máscara, então, ela garante que o modelo ele vai olhar só para o passado por mais que você esteja expandindo. Viu como ficou mais complicado? Porque do jeito que eu expliquei, eu expliquei como se fosse uma RNN trabalhando, certo? Palavra, palavra, numa forma só. Só que ele não fez isso. Ele abriu isso em multicamadas. Só que ele foi dando ali aquela senha de, ó, você é A1, você é A2, você é A3 e etc.

10:08

então ele foi jogando isso e isso foi transformando em uma matriz e na simplificação eu fiz como se fosse uma RNN mas no fim das contas o Transformer está fazendo a mesma coisa com uma máscara triangular só que aberto isso para várias threads rolando ao mesmo tempo e com isso cada uma com a sua numeração de sequência para ele focar na orientação esquerda para a direita que é a nossa noção de tempo de leitura, beleza?

10:37

Então essas camadas empilhadas, elas vão conseguir trabalhar ainda assim desse jeito. Fechou? Tem umas outras coisas que eu queria conversar com vocês aqui, vamos falar o seguinte.

10:50

Essas camadas, elas são divididas em algumas partes. Vamos quebrar ela em três partes pra gente discutir aqui. Tá bom? A primeira delas é a multi-head attention com máscara causal. Beleza? O que que isso significa? O modelo, ele vai olhar pros tokens anteriores e decidir quais desses tokens anteriores são importantes pra prever o próximo. Então ele não vai nem olhar todos, ele vai olhar quais tokens são importantes pra isso.

11:17

Beleza? E daqui ele faz um negócio que chama multihead. Ele faz isso com diferentes olhares ao mesmo tempo. Ele tem várias formas de olhar isso.

11:27

e cada uma aprendendo uma relação diferente, beleza? Então, cada head vai estar olhando de um jeito diferente para aquela mesma informação. Isso eu expliquei para vocês lá atrás, lembra? Quando a gente está fazendo a composição, a gente tem que olhar diferentes formas textuais do que está sendo gerado pela frente. Esses multi-heads com a máscara causal vão fazer isso para conseguir organizar

11:51

o modelo sem deixar ele olhar para o futuro. Então ele está olhando para trás com uma máscara triangular inferior e com uma multi-head deixando ele olhar os mesmos vetores em diferentes estratégias. Fechou?

12:08

Segundo ponto para falar com vocês, o Feedforward Position Wise. O que significa? É como se fosse um mini cérebro, tá bom? Que ele tá aplicado a cada palavra ali que você tem de forma individual. Então ele vai transformar a informação daquela palavra

12:26

em uma posição, e com isso ele vai ajudar a captar os padrões que são não lineares, para conseguir combinar significado quando a gente está falando de coisas mais abstratas. Então é super importante você ter essa camada também. Tem a terceira camada, que é o Layer Norm.

12:44

Ou seja, esse cara vai trabalhar as conexões residuais. A lei enorme funciona como? Ele vai manter esses valores equilibrados para não deixar que nada explode, nada exploda ou nada morra. Então ele vai estar olhando para aqueles valores que a gente tem e não vai deixar dar nenhuma explosão de vetor e nem deixar nenhum vetor chegar a morrer durante o treino. E com isso ele consegue normalizar

13:10

os resíduos que a gente tem, ou seja, os outliers que estão fugindo do nosso contexto aqui, tá bom? Essa conexão residual, ela vai adicionar, então, como a gente já falou lá atrás, na camada, na próxima camada, o resultado final. Isso vai facilitar, então, que você consiga andar com a informação e evitar que a gente esqueça informações no meio do caminho das camadas anteriores. Então, com isso, você consegue resolver

13:40

tudo que a gente tem no Transformer ali. Eu tentei trazer pra vocês da forma mais tranquila, mais simples, pra vocês captarem como funciona a arquitetura dentro desse modelo de Decoder Only, beleza?

## Resumo IA

**Abreviações**  
- **Transformer**: arquitetura de rede neural baseada em atenção, proposta em 2017 no paper *Attention Is All You Need*.  
- **LLM**: *Large Language Model* (modelo de linguagem de grande porte).  
- **RNN**: *Recurrent Neural Network* (rede neural recorrente).  
- **RNNS**: referência informal a *RNNs*, no plural, isto é, redes neurais recorrentes.

**Resumo**  
A aula apresentou a arquitetura **decoder-only** dentro da família Transformer, destacando seu uso principal em tarefas de geração textual autoregressiva, como continuação de texto, storytelling e respostas. O instrutor explicou que essa variação do Transformer é especializada em prever o próximo token com base apenas no histórico já produzido, evitando a visão bidirecional típica de outros arranjos e reduzindo a complexidade para esse tipo de tarefa. Também foi contextualizado que essa abordagem deriva do avanço iniciado com o paper *Attention Is All You Need*, em 2017.

O conceito central da aula foi a **causal self-attention**, mecanismo que restringe cada posição a acessar apenas os tokens anteriores e a si mesma. Para materializar essa regra, foi apresentada a **máscara triangular inferior**, que zera a atenção para posições futuras e libera o contexto gradualmente ao longo da sequência. O professor usou a frase “o cachorro correu rápido” para ilustrar como a matriz de atenção funciona: a cada passo, uma posição pode consultar apenas o passado disponível, sem “olhar para frente”. A ideia foi reforçada com a analogia de uma prova, em que só faz sentido consultar questões já vistas e não as futuras.

A aula também esclareceu que, embora a explicação use palavras para facilitar a compreensão, o processamento real ocorre sobre **tokens** e, mais profundamente, sobre **vetores**. Ou seja, a máscara causal atua sobre representações vetoriais organizadas em matriz, mantendo a restrição temporal mesmo em um nível mais abstrato de cálculo. Foi feita ainda a comparação com **RNNs**, mostrando que, diferente delas, o Transformer não precisa processar estritamente token por token para respeitar a ordem; ele consegue trabalhar em paralelo nas camadas, mas continua obedecendo à direção esquerda-para-direita graças à máscara causal.

Por fim, o instrutor detalhou três partes importantes do bloco decoder-only: a **multi-head attention com máscara causal**, que permite múltiplas leituras do mesmo contexto passado; o **feedforward position-wise**, que refina individualmente a representação de cada posição sem misturar posições entre si; e o **Layer Norm** junto das **conexões residuais**, que estabilizam os valores internos, preservam informação das camadas anteriores e facilitam o treinamento profundo. No conjunto, esses elementos garantem geração consistente, paralelismo computacional e comportamento autoregressivo controlado.

**Pontos de atenção**  
- A máscara causal é obrigatória em modelos autoregressivos: sem ela, o modelo poderia acessar informação futura e “trapacear” no treino.  
- A explicação por palavras é apenas didática; na prática, o modelo trabalha com **tokens** e **vetores**, não com palavras literais.  
- A matriz de atenção representa visibilidade entre posições, e a restrição depende da posição relativa, não do significado semântico.  
- O decoder-only não funciona como uma RNN clássica, apesar de também respeitar a ordem temporal; ele faz isso com processamento paralelo e máscara causal.  
- A consistência entre **treino** e **inferência** depende do mesmo padrão de mascaramento.  
- A **multi-head attention** não elimina a causalidade: ela amplia os pontos de vista sobre o passado, mas sem permitir acesso ao futuro.  
- O **feedforward position-wise** atua por posição individual; ele não mistura informações entre tokens.  
- **Layer Norm** e **conexões residuais** são essenciais para estabilidade numérica, fluxo de gradiente e preservação de informação em redes profundas.  
- Sem o mascaramento adequado, o modelo pode produzir saídas incoerentes ou “alucinar” por falta de restrição temporal.