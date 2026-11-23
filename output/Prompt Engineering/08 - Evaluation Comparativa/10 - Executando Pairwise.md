Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16938)

## Resumo da aula

pull prompt carrega do LangSmith uma versão já registrada do prompt, em vez de manter o texto apenas no código local. Isso permite versionamento, reaproveitamento por API e rastreabilidade entre execuções, o que é especialmente útil quando prompt A e prompt B evoluem ao longo de vários experimentos. Retomando o cenário de comparação entre prompts, aqui A e B vêm do repositório remoto, enquanto o juiz permanece local; essa combinação mostra que geração e julgamento não precisam usar a mesma estratégia de armazenamento. Se quiser centralizar tudo, o prompt do juiz também pode ser criado remotamente e recuperado depois por API.

Cada variante precisa de uma função própria de execução, mesmo quando a estrutura é quase idêntica. A função do prompt A monta o chat prompt com o template correspondente, injeta os campos do dataset — como code e linguagem — e envia isso ao modelo; a função do prompt B repete o pipeline trocando apenas o prompt. Essa separação preserva o isolamento experimental: o dataset e a chamada ao modelo permanecem constantes, e a variável que muda é a instrução. Quando os resultados divergirem, a diferença fica atribuível ao prompt, não ao restante do pipeline.

O pairwise evaluator é instanciado a partir do template do judge e da conexão com o modelo que fará o julgamento. Como o método pairwise já foi definido anteriormente, o ponto novo aqui é operacional: o juiz recebe as duas saídas geradas e executa a terceira chamada do fluxo, produzindo a comparação dentro do LangSmith. O template do juiz concentra as regras de decisão, e por isso ele determina como a preferência será computada, inclusive quando há ranqueamento por pontos. Se o critério estiver mal especificado, o experimento continua executando, mas a auditoria posterior perde valor.

A execução completa ocorre em três blocos: primeiro roda o prompt A sobre o dataset, depois o prompt B sobre o mesmo conjunto de exemplos e, por fim, o evaluator compara os pares de respostas. Essa ordem importa porque o experimento pairwise no LangSmith referencia os nomes dos dois experimentos já concluídos para montar a comparação. Na prática, o código captura o nome retornado por cada run e o reaproveita na etapa comparativa. Sem esse encadeamento explícito, o sistema não sabe quais execuções devem ser confrontadas.

O prefixo nomeia o experimento de forma legível e ajuda a localizar runs relacionadas no painel, principalmente quando você repete o teste várias vezes após alterar o prompt. Já a concorrência controla quantas execuções podem ocorrer em paralelo, afetando tempo total, pressão sobre a API e previsibilidade de custo. Esses parâmetros não mudam a lógica do julgamento, mas mudam a operabilidade do experimento. Em ambiente de iteração rápida, nomear bem e ajustar concorrência evita confusão entre versões e gargalos desnecessários.

Antes de executar, vale confirmar que o dataset existe, está no projeto correto e contém a quantidade esperada de samples. No exemplo, a checagem mostra um dataset pairwise com 10 registros e ainda sem experimentos associados, o que valida o ponto de partida antes de consumir tokens. Essa verificação simples evita dois erros comuns: rodar contra o dataset errado e interpretar resultados de um experimento anterior como se fossem da execução atual. Em avaliação comparativa, esse tipo de erro compromete a leitura inteira do teste.

Quando o objetivo é exclusivamente pairwise, adicionar correctness, helpfulness ou outros evaluators paralelos aumenta custo sem responder à pergunta principal do experimento. Cada evaluator extra pode gerar chamadas adicionais ao modelo, consumindo tokens e poluindo a leitura com métricas que não serão usadas na decisão. Por isso, faz sentido deixar os experimentos A e B sem avaliações complementares quando a única saída desejada é a comparação entre eles. Otimização de custo aqui não é detalhe financeiro; é foco experimental.

Depois da execução, o LangSmith cria um experimento de comparação com placar agregado, como vitória de A por 5,5 contra 4,5. Esse número depende da regra embutida no prompt do juiz, que pode atribuir pontos em vez de apenas contar vitórias simples. O painel oferece uma leitura rápida de quem venceu no conjunto, mas esse resumo só é confiável quando você entende a política de pontuação usada pelo judge. Sem essa leitura do critério, o placar vira um número opaco.

O valor prático do pairwise aparece quando você abre cada registro e verifica quem venceu caso a caso. O painel marca visualmente vitórias e derrotas, e o detalhamento mostra o input original, a linguagem, a saída da versão A e a saída da versão B. Isso permite depurar decisões concretas: por exemplo, um lado apontou command injection, o outro missing output validation, e o juiz precisou decidir qual resposta era superior para aquele código. A comparação deixa de ser apenas um placar agregado e passa a ser um artefato auditável.

Ao abrir o trace ou a API Run, você consegue ver exatamente o que foi enviado ao modelo julgador: o prompt completo, as regras, os inputs e o output final. Essa visibilidade é crucial quando o resultado parece estranho, porque permite verificar se o judge recebeu contexto suficiente, se as regras estavam claras e se a resposta vencedora foi escolhida pelos motivos esperados. No exemplo, o trace mostra o texto que instrui o modelo a agir como juiz imparcial e o output final indicando vitória de A. Quando necessário, o próximo refinamento é pedir justificativa textual da decisão para tornar a auditoria ainda mais forte.

## Transcrição

00:01

Bom pessoal, agora que a gente já entendeu essa pegada, nós vamos fazer o seguinte nesse momento, tá? Nós vamos fazer a execução. E somente para você ver a execução aqui, é um run. E como é que funciona no final das contas? Eu tenho um dataset, que eu fiz o upload, eu já fiz o upload do dataset, tenho que verificar. Tenho o prompt A, o prompt B,

00:28

Tenho o prompt do meu juiz, tá? E se você olhar aqui, eu estou dando um pull prompt. O que é pull prompt? Porque o prompt A e o prompt B, eu estou pegando ele lá do lang.smith, que eu queria mostrar pra vocês um exemplo de que você pode também criar por API um prompt lá no lang.smith, onde você pode fazer o versionamento. Inclusive, a gente já viu isso.

00:47

só quis trabalhar dessa forma, mas eu poderia estar trabalhando local, como eu estou fazendo com o juiz. O juiz, eu estou pegando local. Se eu quisesse, eu podia dar um create prompt para o juiz também e pegar tudo online. Então, aqui eu tenho o prompt A e o prompt B. Agora, aqui que está o negócio importante, pessoal. Eu tenho uma função chamada rodar o prompt A.

01:07

onde eu vou executar um chat prompt, que no final das contas é pegar os dados do prompt, a minha input, minha conexão, os dados de input vêm do quê? Do code. A language inputs, basicamente, vai vir do meu dataset ali também. E aí eu tenho a mesma coisa com o prompt B, a única coisa é que eu vou fazer com o prompt que é diferente.

01:29

E daí, por último, olha só o que eu falei para vocês. Eu tenho um pairwise judge, que eu vou criar um pairwise evaluator, onde eu pego o template do judge, pego a conexão, o wrap e a conexão do OpenAI, e aí, quando eu for fazer essa evaluação, no final das contas, ele vai fazer essas minhas comparações. Então, aqui está a execução do resultado A, a execução do resultado B,

01:57

E aqui tem os meus pontos de comparar. Então, eu tenho aqui o nosso Evaluation Comparative, que é lá do Langsmith. Eu estou passando o resultado do A, ou seja, passando o nome do experimento, inclusive, porque eu rodei aqui, ele retorna para mim o nome do experimento. Ele pega o nome do experimento B, aqui também.

02:19

fala quem é o meu evaluator, é o meu pairwise judge no final das contas, que é esse cara aqui, esse cara que é o evaluator. E aqui eu coloquei o nome do prefixo e a parte de concorrência. Então, vamos executar esse cara agora aqui, vou dar um python

02:41

Aqui tem o 3 barra run. Deixa eu só, antes de fazer isso, verificar se o nosso dataset existe. Eu não lembro se eu subi o dataset ou não. Vamos clicar, dataset experiments pairwise, está aqui. A gente tem o nosso dataset com nenhum experimento dentro e a gente tem aqui 10 samples aqui dentro. Então, está aqui o nosso dataset que a gente tem. Agora que a gente tem esses nossos datasets, eu vou pedir para a gente fazer execução.

03:08

Então, vamos lá fazer a execução do nosso dataset. Então, ele falando qual o prompt A, qual o prompt B, e agora ele está executando aqui os exemplos do prompt A. Depois, em seguida, ele vai fazer a mesma coisa ali com a execução do prompt B, e depois ele vai fazer uma terceira execução da evaluação. Então, eu vou dar um pause rapidinho nesse vídeo, somente para ele não ficar muito grande, e a gente já volta aqui. Você viu que ele já terminou a A, e vamos nessa então.

03:43

Na realidade, eu nem vou dar um pause, tá, galera? Eu vou fazer o seguinte. Enquanto ele vai olhando esse cara, eu vou fazer assim, ó. Eu vou chegar aqui no meu experimento. Tá, aqui, ó. Experiments. E aqui ele já está começando a carregar os meus experimentos, se você olhar aqui. Agora, tem algumas coisas que são um pouco curiosas, se você olhar. Se você olhar,

04:12

O meu objetivo aqui é fazer a evaluação pairwise. Então, o que significa? Significa que, tanto no experimento A quanto no B, para mim, eu não quis trazer nenhuma outra métrica. Eu poderia trazer correctness, poderia trazer helpful, poderia trazer um monte de métricas.

04:34

Mas como nesse caso os experimentos que eu estou fazendo são apenas para pairwise, eu não vou ficar gastando token no final das contas para ele ficar fazendo a execução de outros tipos de evaluação, uma vez que eu queria saber apenas

04:50

a comparação do A com o B. Então, isso que a gente está esperando. Agora, quando você olha aqui no código, de forma geral, você vai ver que ele já executou o A e o B, e ele também fez o nome da minha comparação, que é pairwise14, 28, aqui que ele trouxe. Então, se você olhar aqui, está executado basicamente todos esses caras. Mas, aqui no langsmith, eu tenho pairwiseexperiments. Então, quando eu venho aqui,

05:20

e aqui que o negócio fica mais interessante. Olha só que interessante, galera. Esse cara aqui é a comparação do meu evaluator. Então, olha só que interessante. Quem ganhou foi o A, aqui no meu caso. Por que foi o A? Porque eu estou com um joinha no A e ele ganhou de 5,5.

05:40

A por 4,5. Por que tem esse nome? Porque, na minha regra lá do juiz, eu pedi pra ele trabalhar ali, fazendo esse ranqueamento pra ver quem ganha e tem mais ponto ou coisa desse tipo, tá? E se eu clico no experimento, aí a gente consegue entender algumas coisas que são bem interessantes. Deixa eu mostrar aqui pra vocês. Pra cada registro que ele rodou,

06:04

eu falo quem ganhou, tá? Então, o experimento A, tudo que está verde aqui, foram caras que ele ganhou no final das contas. E tudo que está vermelho, ele perdeu. Então, você começa a conseguir ver que esse cara aqui tem um... Opa, espera um pouquinho, será que é o DF5?

06:23

Não, aqui ele estava trazendo a referência. Então, esse cara aqui tem 1, esse tem 0, esse tem 1, e a gente acaba tendo essa opção para esses casos. Mas olha só que interessante, se eu chegar aqui e clicar nesse 1, tá vendo? Ele mostra aqui, e eu acho que se eu clicar aqui em API, Run, ele vai mostrar como que foi a execução desse cara.

06:43

E aqui que fica mais interessante, porque eu vejo o input que teve, ele viu que a linguagem é Go, o output da versão A foi esses resultados,

06:55

E o output da versão B foram esses resultados, ou seja, são os exemplos, no final das contas, que acabaram a gente pegando isso aqui, ou seja, foram o que a gente acabou passando. Mas o mais interessante é que ele trouxe aqui,

07:14

O que aconteceu aqui nesse caso? Um teve command injection, outro teve missing output validation, e aqui eu teve zero de um cara, um do outro, etc. Mas, Weisler, o que isso significa? A coisa fica interessante porque isso aqui a gente consegue ver o que entrou, aqui não vai ter feedback, tem o metadata aqui do que a gente rodou, mas quando eu clico aqui em chat OpenAI, eu consigo, na realidade, ver o prompt que foi colocado,

07:42

tudo que entrou no input e eu consigo ver o output. Então, olha só que interessante. Aqui eu tenho o prompt inteiro que entrou, tá? Então, se você olhar, analise o código abaixo, você é um juiz imparcial. Depois de analisar o código abaixo, ele tem as rules e etc. aonde ele vai fazer o julgamento. E o output aqui da IA, aqui pra gente, no final das contas, foi quem ganhou a sua opção, foi o A.

08:08

Então, é basicamente que a gente consegue ir muito nesse nível de profundidade para conseguir trabalhar. O que a gente pode fazer também, eventualmente, é com que a IA justifique o porquê que ela tomou essa decisão. A gente consegue também fazer isso, mas

08:29

Somente para ficar claro para todo mundo, eu consegui trazer que o meu prompt A, olhando aqui, ele ganhou com essa pontuação. Mas, agora, a gente vai fazer o seguinte no nosso próximo vídeo. Eu vou mudar o meu prompt e vou executar de novo isso aí. E daí a gente vai ver se a gente tem quem ganha e quem perde, ou se teve alguma mudança. Vamos nessa?

## Resumo IA

**Abreviações**
- **API** — Application Programming Interface (Interface de Programação de Aplicações)
- **DF** — DataFrame

**Resumo**
A aula mostrou como executar uma comparação entre dois prompts versionados no LangSmith, usando uma estratégia em que os prompts A e B são carregados remotamente por meio de *pull prompt*, enquanto o prompt do juiz pode permanecer local, embora também pudesse ser versionado e recuperado via API. O instrutor explicou que cada variante de prompt precisa de sua própria função de execução, mesmo que o pipeline seja quase idêntico, para manter o isolamento experimental: o dataset e o modelo permanecem os mesmos, e a única variável alterada é a instrução do prompt.

Também foi apresentado o fluxo de avaliação *pairwise*, em que um *pairwise evaluator* é criado com base no template do juiz e na conexão com o modelo julgador. A execução acontece em três etapas: primeiro roda o prompt A sobre o dataset, depois o prompt B sobre o mesmo conjunto de exemplos e, por fim, o avaliador compara os dois conjuntos de respostas. O nome dos experimentos retornado em cada execução é reutilizado na etapa comparativa, pois o LangSmith precisa desses identificadores para relacionar corretamente os resultados.

O instrutor destacou a importância do *prefix* para nomear experimentos de forma legível no painel e da concorrência para controlar execuções paralelas, impacto de custo e previsibilidade. Antes de rodar, ele reforçou a necessidade de conferir se o dataset existe, está no projeto correto e contém a quantidade esperada de samples, evitando comparar execuções erradas ou consumir tokens desnecessariamente. Como o objetivo era apenas a comparação *pairwise*, ele evitou adicionar avaliadores paralelos como correctness ou helpfulness, que aumentariam o custo sem ajudar na decisão principal.

Após a execução, o LangSmith gerou um experimento comparativo com placar agregado, no exemplo apontando vitória do A por 5,5 contra 4,5, resultado dependente da regra definida no prompt do juiz. Em seguida, o instrutor demonstrou como abrir cada registro individualmente para ver quem venceu em cada caso, inspecionar o input, a linguagem, as saídas das versões A e B e entender os motivos da decisão. Ao acessar o trace ou a API Run, foi possível visualizar o prompt completo enviado ao juiz, as regras de julgamento e o output final, o que torna a auditoria do experimento mais transparente e permite refinar o prompt do juiz, inclusive pedindo uma justificativa textual da escolha.

**Pontos de atenção**
- Confirmar sempre se o dataset existe, está no projeto correto e possui o número esperado de samples antes de executar.
- Garantir que os nomes retornados das execuções A e B sejam reutilizados corretamente na etapa de comparação.
- Manter cada variante com sua própria função de execução para preservar o isolamento experimental.
- Usar *pull prompt* quando quiser versionamento, rastreabilidade e reaproveitamento remoto dos prompts.
- Ajustar o *prefix* com nomes claros para facilitar a identificação de runs e experimentos no painel.
- Controlar a concorrência para evitar sobrecarga na API, aumento de custo e perda de previsibilidade.
- Evitar adicionar avaliadores extras quando o objetivo for apenas comparação *pairwise*.
- Entender a regra de pontuação do juiz antes de interpretar o placar agregado.
- Validar os resultados caso a caso, não apenas o total final, para auditar melhor as decisões.
- Inspecionar o trace/API Run quando a decisão parecer estranha, verificando prompt, regras, input e output.
- Se necessário, pedir ao juiz uma justificativa textual da decisão para fortalecer a auditoria.