Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17878)

## Resumo da aula

Agent Harness é a camada que envolve o modelo para transformá-lo em algo útil para um problema real. A formulação “agente = modelo + harness” resume bem a ideia: o modelo fornece a inteligência, enquanto o harness cria as condições para essa inteligência operar com direção, restrições e contexto. Sem essa camada, o modelo continua genérico, mesmo quando foi otimizado para código. O valor do harness está em converter capacidade bruta em comportamento aplicável.

Harness Engineering consiste em construir sistemas em volta do modelo para que ele funcione como uma engine de trabalho. Isso inclui tudo o que conecta o modelo ao problema que precisa ser resolvido: limites, ambiente, instruções e estruturas de apoio. A frase “se você não é o modelo, você é o harness” delimita bem o escopo: quase toda a engenharia do agente acontece fora do core do LLM. O foco, portanto, não é treinar o modelo, mas moldar como ele atua.

Colocar limites no modelo não significa mantê-lo rigidamente preso a um conjunto fixo de regras ou ferramentas. Modelos melhoram com o tempo e passam a executar tarefas mais complexas com mais autonomia, o que torna contraproducente um ambiente excessivamente restritivo. Se o harness for apertado demais, ele reduz o espaço de ação do modelo e desperdiça capacidades que poderiam gerar melhores resultados. Se for solto demais, o modelo pode agir de formas indesejadas.

Um modelo com alta capacidade de codificação perde valor quando recebe apenas tarefas excessivamente granulares, porque passa a operar como executor mecânico de instruções mínimas. Nesse cenário, o harness limita o modelo a reproduzir passos, em vez de explorar sua capacidade de resolver problemas com mais amplitude. O equilíbrio está em permitir autonomia suficiente para aproveitar o potencial do modelo, sem abrir mão de restrições que preservem o comportamento esperado. Esse ajuste é uma decisão de engenharia, não uma configuração universal.

O harness precisa evoluir junto com o modelo e com os erros observados no uso real. Quando o agente falha repetidamente em um mesmo ponto, esse padrão de erro indica que o ambiente precisa ser ajustado. Uma forma prática de fazer isso é refinar artefatos como agent.md, alterando instruções e limites para reduzir reincidências. O harness, portanto, não é estático: ele é calibrado continuamente conforme o comportamento do agente.

Harness Engineering tende a ser específico para cada projeto, porque os limites e o ambiente necessários dependem do tipo de problema, do fluxo de trabalho e dos erros recorrentes daquele contexto. Por isso, não faz sentido assumir que um mesmo repositório ou configuração será reutilizável sem adaptação entre projetos diferentes. Mesmo dentro de um time, dois projetos podem exigir harnesses distintos. A unidade de ajuste costuma ser o problema concreto, não a organização.

A construção de harnesses depende fortemente de repertório técnico consolidado em artigos e referências da área. Como esse campo evolui rapidamente, acompanhar essas fontes ajuda a entender por que certos limites funcionam, quando devem ser removidos e como adaptar o ambiente à evolução dos modelos. Esse hábito evita decisões baseadas apenas em tentativa e erro local. Em engenharia de agentes, leitura técnica faz parte da prática de implementação.

## Transcrição

00:00

Bom, pessoal, então vamos lá começar a falar sobre esse conceito de Harness,

00:05

tá? Então, seguinte, Harness,

00:07

ele já é um termo que ele é utilizado já faz

00:10

muito tempo e não necessariamente no mundo da IA,

00:14

tá? Mas nesse nosso caso,

00:16

quando a gente está falando em Harness e principalmente em Agent Harness,

00:20

a gente quer dizer o seguinte,

00:22

como que eu consigo colocar limites no meu modelo, né?

00:25

Como que eu consigo criar um ambiente propício para isso, né?

00:30

Existe um artigo no blog da Langchain que os caras colocam o seguinte,

00:34

que um agente é igual ao modelo mais o Harness.

00:38

Então ele fala que o Harness Engineering é como que

00:42

você consegue construir sistemas em volta do modelo.

00:46

para torná-los como se fosse uma engine de trabalho,

00:49

ou seja, uma máquina realmente de trabalho. Então,

00:53

a ideia é que o modelo tem a inteligência e

00:58

o Harness faz com que essa inteligência realmente seja útil. Então,

01:03

o que define o Harness é aquilo que deriva o core componente,

01:09

daquilo que a gente vai ter hoje ou amanhã nas necessidades do agente.

01:16

Então, basicamente, tem uma frase que eles acabam colocando ali,

01:20

que é o seguinte, se você não é o modelo,

01:24

você é o Harness, tá? E isso aí muda muito o conceito.

01:29

Por quê? Pensa que um modelo de LLM,

01:32

por mais que ele tenha sido treinado,

01:35

mesmo que ele seja um modelo treinado ou otimizado para código,

01:41

de forma geral, ele é um agente...

01:45

geralzão, vamos dizer assim. Ele serve ali para resolver qualquer tipo de problema.

01:50

O grande ponto no meio de toda essa história é como

01:53

que você consegue fazer com que esse modelo resolva o seu problema.

01:57

E é aí que é o grande ponto. Quando ele fala que se você não é o modelo,

02:02

você é o Harness, significa que tudo que está conectando e sendo pedido pelo modelo,

02:09

aquilo é considerado um Harness de forma geral.

02:13

O grande ponto é que o Harness consegue limitar

02:17

e gerar um ambiente favorável ali para o modelo.

02:21

Agora, uma das coisas que ali é muito importante que você entenda é o seguinte, tá?

02:28

Quando a gente está falando de Harness Engineering,

02:30

não é que você vai construir um framework ou

02:34

um monte de ferramenta em torno do modelo,

02:37

para que ele fique ali no cabresto, basicamente,

02:40

fazendo exatamente as coisas da forma como você quer.

02:45

E por que eu estou dizendo isso?

02:47

Porque cada dia os modelos ficam melhores.

02:50

Cada dia os modelos conseguem fazer coisas que antes eles não conseguiam fazer.

02:55

E isso pode se tornar, na realidade, uma grande vantagem. Mas ao mesmo tempo,

03:02

se você não souber lidar com essa situação,

03:04

pode ser o maior tiro no pé que você pode dar.

03:08

Imagina que você tem um modelo que conseguiu

03:11

chegar a um nível muito alto de codificação,

03:14

que se você começar, por exemplo, a passar tarefas extremamente granulares para ele,

03:18

você vai limitar esse modelo a fazer exatamente aquela tarefa

03:23

E não vai deixar aquele modelo usar todo o potencial dele.

03:27

O grande ponto é que quando você deixa ele utilizar todo o potencial dele,

03:31

Às vezes esse potencial pode fazer as coisas da forma como você não gostaria.

03:36

E aí que é aquele grande limite onde o harness evolui conforme o modelo.

03:42

Conforme o modelo vai melhorando, por exemplo,

03:45

você vai podendo tirar alguns limites, colocar outros limites.

03:50

Você vai ter que ir ajustando isso conforme o tempo vai passando.

03:55

Conforme o seu agente erra persistentemente em algum local,

04:00

em alguma parte daquilo que você está fazendo,

04:03

você começa a perceber aquele erro padrão e você vai ajustando aquele ambiente,

04:09

aquele seu agent.md, por exemplo,

04:12

para evitar que ele continue fazendo aquele mesmo erro.

04:17

Então, o que é importante é que você

04:20

entenda que o Harness Engineering não é algo que

04:24

eu vou compartilhar um repositório com meu amigo e naquele

04:27

meu projeto e no seu projeto vai funcionar.

04:30

Não. Isso aí acaba, na maioria das vezes,

04:33

sendo inclusive individual para cada projeto e

04:36

não necessariamente para um determinado time.

04:39

Um outro lembrete que eu queria trazer extremamente forte

04:43

aqui é que eu vou passar uma série...

04:46

mesmo de artigos, eu preciso muito que vocês leiam esses artigos.

04:51

Muito do que eu estou trazendo aqui para vocês vem desses artigos e,

04:55

obviamente, eu tento trazer as coisas de uma forma mais mastigada,

04:58

mais didática, que consiga fazer sentido dentro desse nosso contexto, mas, novamente,

05:05

eu queria sempre lembrar para que vocês leiam esses

05:07

artigos que eu vou trazer aqui para vocês.

05:10

Beleza? No próximo vídeo,

05:11

a gente vai falar sobre Harness Base ou Harness Building.

05:16

Isso aí é super importante para a gente

05:17

entender algumas diferenças aqui daqui para frente.

## Resumo IA

**Abreviações**
*   **IA**: Inteligência Artificial
*   **LLM**: Large Language Model
*   **agent.md**: Arquivo de markdown utilizado para definir ou configurar as instruções e limites de um agente.

**Resumo**
A aula introduziu o conceito de Agent Harness, definindo-o como a camada essencial que envolve um modelo de Inteligência Artificial (IA) para transformá-lo em uma solução útil para problemas reais. A formulação "agente = modelo + harness" sintetiza a ideia, onde o modelo fornece a inteligência bruta, e o harness cria o ambiente, direções, restrições e contexto necessários para que essa inteligência opere de forma eficaz. Sem o harness, um modelo, mesmo que otimizado, permanece genérico.

Harness Engineering foca na construção de sistemas ao redor do modelo, permitindo que ele funcione como uma "engine de trabalho". Isso abrange tudo o que conecta o modelo ao problema, incluindo limites, ambiente e instruções. O instrutor enfatiza que "se você não é o modelo, você é o harness", indicando que a maior parte da engenharia de um agente ocorre fora do core do LLM, concentrando-se em como o modelo atua, e não em seu treinamento.

O harness deve encontrar um equilíbrio: não pode ser excessivamente restritivo, o que limitaria a autonomia e desperdiçaria o potencial de modelos mais avançados, nem demasiadamente solto, o que poderia levar a comportamentos indesejados. A necessidade de ajuste contínuo é destacada, pois o harness precisa evoluir com o modelo e ser calibrado com base nos erros observados no uso real, muitas vezes refinando artefatos como arquivos `agent.md`. A construção de harnesses é inerentemente específica para cada projeto, dependendo do problema e do fluxo de trabalho, o que descarta a reusabilidade genérica de configurações. Por fim, a importância de acompanhar o repertório técnico da área e ler artigos e referências é ressaltada para embasar as decisões de engenharia, evitando a abordagem de tentativa e erro.

**Pontos de atenção**
*   **Harness não é restrição absoluta**: Evite criar um ambiente excessivamente apertado que limite o modelo e impeça-o de usar todo o seu potencial, especialmente com a evolução constante dos LLMs.
*   **Evite tarefas excessivamente granulares**: Para modelos com alta capacidade (e.g., de codificação), tarefas muito detalhadas transformam o modelo em um executor mecânico, desperdiçando sua capacidade de resolver problemas de forma mais ampla.
*   **Equilíbrio é fundamental**: Encontre o balanço entre dar autonomia suficiente ao modelo para aproveitar seu potencial e manter as restrições necessárias para garantir o comportamento esperado. Esta é uma decisão de engenharia específica, não uma configuração universal.
*   **Harness não é estático**: Ele deve evoluir junto com o modelo e ser ajustado continuamente com base nos erros e falhas observados no uso real do agente (e.g., refinando `agent.md`).
*   **Harness é específico do projeto**: Não espere que um harness ou sua configuração seja reutilizável entre projetos diferentes, mesmo dentro da mesma equipe. A unidade de ajuste é o problema concreto.
*   **Mantenha-se atualizado**: Acompanhar artigos e referências técnicas da área é crucial. O campo evolui rapidamente, e a leitura técnica ajuda a entender as melhores práticas, a razão por trás de certos limites e como adaptar o ambiente à evolução dos modelos, evitando decisões baseadas apenas em tentativa e erro.
*   **Identifique padrões de erro**: Erros repetitivos do agente são um forte indicativo de que o ambiente do harness precisa ser ajustado.