Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16936)

## Resumo da aula

Pairwise evaluation é uma forma de avaliar qualidade sem depender de um ground truth absoluto para cada saída. Em vez de perguntar se uma resposta está correta contra uma referência fixa, a comparação pergunta qual de duas respostas para o mesmo input é melhor segundo um critério explícito. Essa mudança é importante quando a decisão útil é relativa, não absoluta. Ela inaugura um novo bloco de avaliação comparativa: comparar variantes entre si, e não apenas medir acertos contra rótulos.

Pairwise evaluation é o tipo de avaliação; Pairwise Evaluator é o componente que executa esse tipo de julgamento. A distinção importa porque ferramentas como LangSmith nomeiam o mecanismo operacional como evaluator, enquanto o método conceitual continua sendo a avaliação pairwise. Em termos práticos, o primeiro responde à pergunta “que forma de avaliação estou usando?” e o segundo responde “quem aplica essa forma de avaliação?”. Separar método de executor evita confundir estratégia de experimento com implementação da ferramenta.

A comparação pairwise só é útil quando o critério de julgamento está explícito. Esse critério pode ser correctness, como no exemplo de timeout em HTTP request com Go, mas também pode ser outro atributo comparável, desde que esteja claramente definido. O juiz não decide “qual gostou mais”; ele decide qual saída vence segundo a régua informada. Sem esse critério, a preferência gerada perde valor técnico e fica difícil auditar por que uma resposta ganhou da outra.

Retomando a lógica de comparação entre prompts já usada antes, a entrada agora permanece fixa e o foco passa a ser a disputa entre duas saídas. Para o input “como trabalhar com timeout em um HTTP request com Go”, a resposta A usa context.WithTimeout e a resposta B usa time.Sleep. Se o critério for correctness, a preferência recai sobre a alternativa que implementa timeout de forma correta no contexto da linguagem e da API. O resultado da avaliação não é um score contra ground truth, mas uma escolha entre A e B.

A avaliação pairwise normalmente envolve três chamadas lógicas. Primeiro, executa-se a opção 1; depois, executa-se a opção 2; por fim, uma terceira chamada recebe as duas respostas e produz o julgamento comparativo. Essa terceira etapa é a do juiz, que consolida as saídas concorrentes e retorna a preferência com base no critério definido. O custo e o desenho do experimento mudam porque a comparação exige gerar as alternativas antes de julgá-las.

Pairwise evaluation se aproxima de A/B testing porque ambos comparam alternativas, mas a natureza da comparação é diferente. No pairwise, duas saídas para o mesmo input são julgadas diretamente por um avaliador, geralmente offline e em ambiente controlado; no A/B testing, a comparação acontece online, em produção, observando comportamento real de usuários ou métricas de negócio. Um método não substitui automaticamente o outro. Pairwise serve para decidir preferências de qualidade entre respostas; A/B testing valida impacto operacional no sistema em uso.

Precision, recall e F1 continuam adequados quando existe ground truth confiável e a tarefa é objetivamente mensurável, como já foi estabelecido. Pairwise entra quando a comparação entre duas saídas é mais natural do que a checagem contra uma resposta única esperada. Isso acontece em cenários em que várias respostas podem ser aceitáveis, mas uma é melhor que a outra segundo um critério definido. Nesses casos, a avaliação relativa complementa a avaliação absoluta e amplia o repertório experimental de prompts.

No LangSmith, pairwise aparece como um evaluator porque a ferramenta precisa de um componente concreto para aplicar o julgamento comparativo. O ponto central não é a nomenclatura da interface, mas entender que o evaluator operacionaliza uma avaliação relativa entre duas execuções. Essa leitura ajuda a estruturar experimentos corretamente: duas opções são executadas sobre o mesmo input, e o juiz decide a preferência. A partir daí, as próximas iterações podem inspecionar justificativas, versionar prompts e repetir comparações com mais controle.

## Transcrição

00:01

Bom, pessoal, e agora a gente vai falar de um assunto que é muito importante, principalmente nós nesse momento onde a gente está focando bastante em prompt, que é a parte de pairwise. Então, se você olhar, você vai encontrar pairwise em alguns contextos. Um contexto aqui é o pairwise evaluator, ou seja, é realmente fazer a comparação

00:22

de duas respostas usando o mesmo input. Ou seja, basicamente, o que eu vou fazer é pegar dois caras diferentes, pegar um cara que vai julgar esses dois caras, e aí a gente vai criar critérios para escolher quem ganhou. Basicamente, é isso que vai acontecer. Então, por exemplo, nesse caso que eu falei de pairwise evaluator,

00:47

A gente colocou, por exemplo, como trabalhar com timeout em um HTTP request com Go. A resposta A era context with timeout, a resposta B era time.sleep, o tipo de avaliação aqui no final das contas era correctness, para ver o que estava correto, e aqui a gente tem a preferência do pairwise falando que quem acertou foi o item A aqui para a gente. Então, o tipo de pairwise, por exemplo, quando você está falando em langsmith, inclusive, ele é um tipo de evaluator.

01:15

Por quê? Porque pairwise também acaba sendo um tipo de avaliação, ou seja, eu tenho o tipo de avaliação que é pairwise, onde eu comparo as duas saídas,

01:31

Ou seja, são formas comparativas, onde eu tenho prompts diferentes, ou posso ter um A-B testing, que no final das contas é quando a parada está acontecendo online, em produção. E a gente tem a forma comparativa, que é um pairwise evaluation, ou seja, é um tipo de evaluação.

01:50

Aqui, eu tenho o Pairwise Evaluator. Esse cara aqui é o que avalia, é quem faz a avaliação do tipo Pairwise Evaluation, ok? Somente para vocês entenderem o porquê. Porque você vai encontrar esse tipo de Evaluator em diversas ferramentas, inclusive no Langsmith. Por isso que é importante vocês entenderem. Qual que é a ideia, como que você faz o Pairwise Evaluator de forma geral? Você vai executar a opção 1,

02:19

você vai executar a opção 2, você vai pegar os dados das duas opções e executar uma terceira vez utilizando o evaluator de pairwise, que vai usar as duas respostas para trazer ali o critério que ele quis utilizar para dizer quem ganhou. Então, na realidade, são três requisições, vamos dizer assim. A requisição da opção 1,

02:48

a requisição da opção 2 e a rodada número 3, onde ele gruda os dois e faz essa evaluação. Basicamente, é isso que acaba acontecendo. No próximo vídeo, eu vou mostrar para vocês como é que a gente faz isso aqui na prática com os nossos exemplos. Vamos nessa!

## Resumo IA

**Abreviações**  
- **A/B testing**: teste comparativo entre duas variantes, geralmente realizado em produção para medir impacto real em usuários ou métricas de negócio.  
- **HTTP**: HyperText Transfer Protocol.  
- **Go**: linguagem de programação Go.  
- **LangSmith**: plataforma/ferramenta citada na aula para experimentação e avaliação de prompts e saídas.  
- **Pairwise Evaluation**: avaliação comparativa entre duas saídas para o mesmo input, usando um critério explícito.  
- **Pairwise Evaluator**: componente/ferramenta que executa a avaliação pairwise, fazendo o julgamento entre as duas respostas.  
- **F1**: medida que combina precision e recall em uma única métrica.  

**Resumo**  
A aula apresentou o conceito de pairwise evaluation como uma forma de avaliar a qualidade de respostas sem depender de um ground truth absoluto. Em vez de verificar uma única saída contra uma referência fixa, a comparação é feita entre duas respostas geradas para o mesmo input, escolhendo qual delas é melhor segundo um critério explícito, como correctness. O instrutor destacou a diferença entre o método de avaliação e o componente que o executa: pairwise evaluation é o tipo de avaliação, enquanto pairwise evaluator é o agente que realiza esse julgamento, nomenclatura que aparece em ferramentas como o LangSmith.

O fluxo explicado foi: executar a opção 1, executar a opção 2 e, em seguida, fazer uma terceira rodada em que um evaluator compara as duas saídas e declara a vencedora com base no critério informado. Foi usado como exemplo um prompt sobre timeout em uma requisição HTTP com Go, em que a resposta correta era a que utilizava context.WithTimeout, enquanto uma alternativa inadequada usava time.sleep. A aula também comparou pairwise evaluation com A/B testing, explicando que o primeiro é geralmente offline e voltado a julgamentos de qualidade entre respostas, enquanto o segundo ocorre online em produção e mede impacto operacional real. Por fim, reforçou-se que métricas como precision, recall e F1 continuam úteis quando existe ground truth confiável, mas que a avaliação pairwise é especialmente valiosa quando a comparação relativa entre alternativas é mais apropriada do que uma checagem absoluta.

**Pontos de atenção**  
- Pairwise evaluation exige um **critério de julgamento explícito**; sem isso, a preferência entre respostas perde valor técnico e fica difícil de auditar.  
- É importante não confundir **o tipo de avaliação** com **o componente que a executa**: pairwise evaluation não é o mesmo que pairwise evaluator.  
- A comparação pairwise sempre usa **o mesmo input para as duas saídas**; o que muda são as respostas candidatas.  
- O processo normalmente envolve **três chamadas lógicas**: gerar a opção 1, gerar a opção 2 e depois fazer a avaliação comparativa.  
- Pairwise evaluation **não substitui automaticamente** A/B testing: um é voltado à comparação de qualidade, o outro à validação em produção.  
- Métricas clássicas como precision, recall e F1 continuam adequadas quando há **ground truth confiável**; pairwise é mais útil quando a resposta certa não é única ou a comparação relativa é mais natural.  
- Em ferramentas como LangSmith, entender a nomenclatura do evaluator evita erro na configuração de experimentos e na interpretação dos resultados.  
- Ao usar pairwise, vale manter controle sobre **justificativas, versionamento de prompts e repetição dos testes**, para garantir rastreabilidade das decisões.