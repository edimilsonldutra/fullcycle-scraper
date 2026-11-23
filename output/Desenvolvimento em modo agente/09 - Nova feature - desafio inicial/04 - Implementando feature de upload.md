Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17992)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, eu acho que chegou a hora da gente fazer o nosso processo de implementação agora.

00:06

Então, o que eu vou fazer? Eu vou dar um implement e evaluate, por enquanto.

00:13

E vou passar qual é a feature que eu vou trabalhar,

00:17

que é a minha feature 3. Vou passar aqui também qual é o meu PRD.

00:22

E vou mandar ver aqui para esse cara trabalhar.

00:28

E agora a gente vai ter que esperar,

00:30

provavelmente eu vou dar várias pausas aqui para a gente ir

00:34

entendendo e toda vez que tiver problema começar a acontecer algumas coisas,

00:40

eventualmente a gente pode até interromper o

00:42

desenvolvimento da feature para arrumar,

00:44

ajustar o nosso agente ou qualquer coisa desse tipo. Para quê?

00:49

Para que ele fique evitando de cair sempre no mesmo erro. Então,

00:53

basicamente a partir de agora a gente vai ver que o que a gente fez...

00:57

Se o que a gente fez está fazendo sentido para o nosso agente ou

01:04

se ele vai começar a bater cabeça agora no meio de toda essa história.

01:10

E aqui ele já saiu criando o arquivo de orquestração.

01:15

E daí, aqui ele subiu um agente de implementação, tá?

01:19

Somente para você saber, galera, cada harness é diferente.

01:22

Se você pegar o Codex, ele é de um jeito,

01:25

o Cloud Code é do outro, o Open Code é do outro.

01:28

Se você pegar o Anti-Gravity, se você pode pegar o que for,

01:31

o que acontece é que cada cara funciona diferente.

01:35

Por exemplo, o Cloud Code, nessas últimas versões dele,

01:37

ele tem um esquema de workflow que você pode fazer,

01:41

cria um workflow onde ele vai soltar um monte

01:43

de agentes para fazer várias tarefas massivas,

01:45

mas ele também tem uma parada chamada de superpowers,

01:49

que ele ajuda você a criar a especificação,

01:53

que ele ajuda você a fazer a avaliação,

01:55

basicamente o que a gente está fazendo aqui, ele tem plugins que dá para fazer.

02:00

Por outro lado, o que a gente percebe é o seguinte,

02:04

tudo que é igual para todo mundo, provavelmente...

02:10

acaba sendo algo que se é igual para todo mundo,

02:15

é fácil para todo mundo e nada é igual.

02:17

Então, por isso que esse exemplo dessas skills que a gente está trabalhando,

02:22

por exemplo, elas são,

02:23

vamos dizer, custom made, eu criei, né? Para o exemplo desse curso,

02:27

é importante você saber para você criar a sua.

02:29

Você pode usar de outro cara, você pode usar do cloud. Por exemplo, esse cara aqui,

02:33

ele usa um contrato entre eles para conseguir fazer as verificações.

02:38

Então, ele toma cuidado com alguns outros aspectos que,

02:43

por exemplo, um superpower, pelo menos em alguns pontos,

02:46

ele não trata. Por quê? Porque, para mim,

02:48

nesse caso, o meu ponto importante é o meu arquivo de contrato.

02:51

Um superpower não tem isso. Então...

02:54

Esse aí que eu acho que são os pontos que

02:56

a gente sempre tem que levar em consideração.

02:59

Ferramentas, skills, plugins, todos esses tipos de coisa,

03:02

cada dia vai ter coisa nova, entendeu?

03:05

Por isso que, para mim, o importante não é você ficar apegado ao spec writer.

03:09

PRD writer e etc.

03:12

O que eu quero que você entenda aqui nesse ponto é que o processo de harness,

03:17

ele acaba sendo muito mais importante do que necessariamente...

03:23

o framework SDD, o plugin que você vai usar para gerar especificação e etc.

03:28

Perceba que essas interações que a gente está fazendo entre as features,

03:32

elas acabam sendo, às vezes,

03:34

mais importantes que o desenvolvimento porque o agente, cada dia,

03:37

ele está mais inteligente para criar. Agora, esses ajustes que a gente vai fazendo,

03:41

essas decisões que a gente vai tomando,

03:43

isso aí faz parte de arquitetura de software,

03:46

entender um pouco mais de desenvolvimento,

03:48

entender um pouco mais de sistema operacional e é nesse ponto que você,

03:51

desenvolvedor, se garante no seu emprego,

03:53

porque senão você não precisaria nem estar trabalhando nos dias de hoje.

04:00

Então, o importante de tudo nesse aspecto é o que eu faço entre interações,

04:07

o que eu faço entre as features, porque não existe mágica.

04:10

Se você comparar isso com o nosso capítulo de SDD,

04:15

ali foi um comando rodado após o outro.

04:19

Sem nada. Aqui a gente já está sendo mais criterioso,

04:22

e eu poderia ser muito mais na realidade,

04:25

é que a nossa ideia aqui é dar essa passada geral

04:28

para você entender que a mágica por trás não existe,

04:31

mas também que a gente tem que ser ágil e

04:35

que grande parte do tempo a gente não passa programando,

04:38

a gente passa preparando o ambiente.

04:40

Agora uma coisa que é interessante é que conforme você

04:44

vai chegando no nível de maturidade do seu projeto,

04:47

o que vai acontecer é que cada vez menos ajustes,

04:52

menos ajustes desses mais grosseiros vão ser necessários,

04:58

porque o projeto já chegou num nível de estabilidade.

05:01

onde os testes estão rodando, onde assets estão prontos,

05:04

onde subir e descer scripts,

05:07

subir e descer ambiente está funcionando, a parte de CI,

05:12

CD, etc. já estão estáveis, rodando. Então, no começo do projeto,

05:17

você vai gastar tempo, você vai bater cabeça até isso estabilizar.

05:23

Quando isso está estável...

05:25

você vai começar a perceber que cada vez acaba

05:27

ficando mais simples e mais fluido o processo.

05:31

Agora, esse boost inicial dá trabalho.

05:36

Sabe aquela história de escrever um Hello World com uma linha fácil?

05:39

Agora, criar um framework em volta para gerar um Hello World dá muito mais trabalho,

05:46

mas a infraestrutura que você cria em volta

05:48

disso vai possibilitar você escalar esse processo.

05:52

E é a ideia que a gente está trabalhando aqui.

05:55

Beleza? Então agora temos que aguardar ele desenvolver.

06:00

Tem um subagente que está desenvolvendo esse cara aqui, né?

06:04

Da mesma forma como outros plugins, outros frameworks vão trabalhar,

06:08

sempre a ideia principal é trabalhar realmente com o subagente para

06:11

evitar que ele utilize a janela de contexto principal,

06:14

né? E vamos aguardar aí ver como é que esse cara está se saindo.

06:21

Bom, pessoal, aqui o negócio é o seguinte.

06:24

Ele deu que ele conseguiu fazer o primeiro ciclo,

06:26

que é o Implement Feature,

06:27

e conseguiu passar nas cinco fases e etc., verificando o contrato.

06:33

Agora, ele vai fazer o Dispatching do Evaluator,

06:38

que é esse cara aqui que realmente vai conseguir verificar se tudo

06:43

que aconteceu realmente funcionou e se a Feature está funcionando e etc.

06:48

Então, vamos ver o que acontece até agora.

06:51

Aparentemente, nenhum problema, nenhum erro,

06:54

mas vamos ver como é que a coisa se porta daqui para frente.

06:58

Bom, pessoal, só para vocês irem pegando uma atualização aqui parcial,

07:02

eu estou acessando aqui no agente que

07:06

está fazendo a avaliação na parte 3.

07:10

Então, não estou no agente principal,

07:11

estou no subagente vendo o que ele está escrevendo.

07:13

Por enquanto, as coisas aqui estão passando.

07:16

Mas depois a gente vai dar alguma olhada no que

07:19

ele pode estar sofrendo ou coisas desse tipo.

07:22

Ele cria vários arquivos temporários para confirmar o upload. Então, basicamente,

07:28

já trabalhando. Está chamando o Playwright CLI para fazer os testes.

07:34

Então, vamos aguardar aqui o nosso querido evaluator para

07:39

ver como é que ele está se saindo.

07:42

Uma outra coisa interessante nesses aspectos, que vale muito,

07:47

mas muito a pena você considerar é... ver se realmente esse agente evaluator,

07:52

ele precisa ser um modelo extremamente inteligente. Nesse caso aqui,

07:56

ele está pegando o default e ele está pegando o opus,

07:58

entendeu? Mas eventualmente um Sonnet aqui, ou se eu fosse utilizar,

08:03

estou falando aqui de modelos antropológicos,

08:05

mas mesmo que fosse em relação à parte do GPT, por exemplo,

08:08

você pode, dependendo da situação, utilizar modelos mais baratos para avaliação.

08:13

Porque basicamente o que ele vai fazer é checklist.

08:15

Então, isso pode ficar mais rápido e mais barato ali

08:19

em relação a fazer toda essa parte de avaliação, tá?

08:22

Então, tá aqui um ponto importante porque da forma como está aqui rodando com X-High, por exemplo,

08:28

ele vai demorar bastante aí para rodar, tá?

08:31

Então, esse aí é um aspecto e você pode fazer eventualmente,

08:34

no caso... de, sei lá, Cloud Code, por exemplo,

08:37

na própria skill você pode setar qual é o modelo que você

08:40

quer rodar na hora de lançar um agente ou qualquer coisa desse tipo,

08:44

tá? Então, isso é importante em relação à parte de velocidade,

08:49

dinheiro, tokens e tudo mais.

08:51

Então, essa é uma observação aí que eu não posso deixar de fazer para você.

08:56

E finalmente, ele trouxe aqui para mim, ó.

08:59

Evaluator, Returned Clean, os 19 itens passaram,

09:03

todos os atributos de qualidade passaram, não tive nenhum fail, block, manual e etc.

09:09

E ele gerou o relatório aqui para mim. Agora, uma coisa é o que ele está colocando,

09:15

outra coisa é o que a gente vai ver na hora que o desenvolvimento.

09:20

Vamos imaginar para ver se ele fez da forma como eu imaginava,

09:24

apesar de que eu não quero exigir muito dele nesse momento,

09:27

porque quando eu fiz a geração da documentação da Feature 03,

09:32

Eu pedi para ele fazer meio que no piloto automático.

09:35

Então, se não estiver legal do jeito que eu estou querendo,

09:37

também, principalmente, é culpa minha,

09:39

porque ele está fazendo como a especificação ali está mandando,

09:42

Tá? Outra coisa importante, eu não passei uma tela, né?

09:47

Como base para ele fazer exatamente como eu estava imaginando, né?

09:54

Na realidade, eu passei sim, né? Na parte do Design System,

09:57

eu tenho ali as telas, etc.

09:59

Vamos ver como é que vai ficar, né? Vamos ver.

10:01

Ele mudou aqui, né? No Journal Upload, etc.

10:05

E vamos aguardar agora ele terminar as documentações

10:10

finais. Ele criou uma pull request,

10:12

e aqui para a gente ver como é que toda essa parada vai funcionar.

10:18

Eu vou fazer o seguinte então, no próximo vídeo a gente continua,

10:23

e ver como é que tudo isso ficou ali para a gente.

## Resumo IA

**Abreviações**

*   **PRD**: Product Requirements Document
*   **SDD**: Software-Defined Development
*   **CI**: Continuous Integration
*   **CD**: Continuous Delivery/Deployment
*   **CLI**: Command Line Interface
*   **GPT**: Generative Pre-trained Transformer
*   **OS**: Operating System
*   **LLM**: Large Language Model

**Resumo**

O objetivo desta aula é demonstrar e iniciar o processo de implementação e avaliação de uma feature específica (Feature 3) utilizando agentes de desenvolvimento. O instrutor inicia o comando `implement` e `evaluate`, passando a Feature 3 e o PRD correspondente para que um agente de implementação comece a trabalhar. O processo envolve a criação de arquivos de orquestração e o monitoramento contínuo, com pausas planejadas para identificar e corrigir problemas, ajustando o agente para evitar que caia nos mesmos erros.

Durante a execução, é explicado que cada "harness" ou framework de agentes (como Codex, Cloud Code, Open Code, Anti-Gravity) possui funcionalidades e fluxos de trabalho distintos. Alguns oferecem "superpowers" para ajudar na criação de especificações ou avaliações, enquanto outros dependem de contratos ou skills customizadas para verificações, como o exemplo do curso. O instrutor enfatiza que a compreensão do processo de harness é mais importante do que a adesão a ferramentas ou frameworks específicos.

Após a fase de implementação, que inclui a passagem por várias etapas e verificações de contrato, o processo avança para o "Dispatching do Evaluator". Um subagente avaliador é despachado para verificar se a Feature está funcionando corretamente, utilizando ferramentas como o Playwright CLI para testes e criando arquivos temporários. O instrutor destaca a importância de usar subagentes para evitar a sobrecarga da janela de contexto principal. A aula termina com o agente avaliador retornando um resultado "clean", indicando que todos os itens e atributos de qualidade passaram, e a geração de um relatório e uma pull request.

**Pontos de atenção**

*   **Ajuste e Melhoria Contínua dos Agentes**: É crucial interromper o desenvolvimento quando surgem problemas para ajustar o agente ou o processo, garantindo que ele aprenda e evite repetir os mesmos erros. Isso faz parte da arquitetura de software e do entendimento do desenvolvimento.
*   **Adaptação a Ferramentas e Processos Variados**: Não se apegue a ferramentas específicas (como `spec writer` ou `PRD writer`) ou frameworks de SDD. O processo de "harness" e a adaptabilidade a diferentes sistemas (Codex, Cloud Code, Open Code, Anti-Gravity), que variam em suas abordagens (workflows, superpowers, plugins, contratos), são mais importantes.
*   **Valor das Skills Customizadas**: Soluções genéricas ou plugins prontos podem não tratar de todos os aspectos específicos de um projeto (e.g., um arquivo de contrato). A capacidade de criar e adaptar skills customizadas é fundamental.
*   **Interações entre Features são Críticas**: As interações e decisões tomadas entre o desenvolvimento de diferentes features são mais significativas do que o código gerado pelos agentes, pois demonstram o conhecimento do desenvolvedor em arquitetura de software, desenvolvimento e sistemas operacionais.
*   **Maturidade do Projeto e Estabilização Inicial**: O início de um projeto requer um investimento significativo de tempo na preparação do ambiente, estabilização de testes, assets e pipelines de CI/CD. Essa fase inicial, embora trabalhosa, é essencial para criar uma infraestrutura escalável e garantir que o processo se torne mais fluido e com menos ajustes grosseiros à medida que o projeto amadurece.
*   **Otimização de Custos na Avaliação**: Para tarefas de avaliação baseadas em checklists, é possível utilizar modelos de LLM mais baratos (como Sonnet ou modelos GPT de menor custo) para economizar tempo, dinheiro e tokens, em vez de usar modelos mais caros (como Opus ou X-High).
*   **Uso de Subagentes para Eficiência**: Implementar subagentes para tarefas específicas é uma boa prática para evitar o consumo excessivo da janela de contexto principal, otimizando o desempenho e os custos.
*   **Qualidade da Especificação Inicial**: A precisão e detalhe do PRD e dos recursos visuais (como telas de Design System) fornecidos ao agente impactam diretamente a qualidade da implementação final. Um piloto automático com especificações incompletas ou genéricas pode levar a resultados que não atendem totalmente às expectativas.