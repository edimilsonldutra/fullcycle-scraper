Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16940)

## Resumo da aula

Uma decisão pairwise fica muito mais útil quando o juiz não retorna apenas A, B ou tie, mas também explica por que escolheu aquele vencedor. Essa justificativa transforma a comparação em evidência auditável, porque permite inspecionar a linha de raciocínio do judge em vez de aceitar um placar opaco. Em tarefas mais subjetivas, como documentação long-form, isso é essencial para revisar decisões, contestar julgamentos e ajustar critérios sem perder rastreabilidade.

A comparação pode ser decomposta em categorias como conciseness, reference alignment, clarity, utility, technical precision e structural completeness. Cada categoria isola uma dimensão de qualidade que, sozinha, não resolve a decisão final, mas ajuda a explicar onde uma saída supera a outra. Essa decomposição evita um julgamento genérico de “melhor resposta” e produz uma leitura mais estável sobre trade-offs entre brevidade, completude, precisão técnica e aderência à referência.

Retomando a comparação controlada entre duas saídas para o mesmo input, o cenário agora deixa de ser uma resposta curta e passa a ser uma documentação gerada a partir de vários arquivos de código. Nesse contexto, o prompt mais forte pede documentação high-level, factual, concisa e estruturada em Markdown, enquanto a variante mais fraca reduz exigência técnica e profundidade. O objetivo não é só descobrir qual documentação parece melhor, mas qual entrega melhor equilíbrio entre estrutura, precisão e utilidade para desenvolvedores.

Scores auxiliares como cobertura, terminologia e nível de detalhe continuam úteis, mas não bastam quando cada saída vence em dimensões diferentes. Uma documentação pode ser mais concisa, enquanto a outra é mais completa ou tecnicamente mais precisa; sem uma regra de arbitragem, a decisão fica ambígua. O judge pairwise resolve esse conflito ao consolidar múltiplos critérios em uma preferência final, preservando a explicação por categoria.

O judge recebe o código, a referência disponível, as documentações A e B e um conjunto de regras de pontuação por categoria. Essa estrutura permite comparar as saídas com base em critérios explícitos e ainda ancorar a decisão em um material de referência complementar, como um ground truth de documentação. O resultado deixa de ser uma preferência intuitiva e passa a ser uma decisão guiada por uma rubrica verificável.

Na execução, primeiro são geradas as duas documentações e só depois ocorre o julgamento comparativo, como já estabelecido no fluxo pairwise. O ponto novo está na inspeção do output do judge: o trace mostra a pontuação por categoria e a justificativa textual correspondente. Quando o judge afirma, por exemplo, que a documentação A venceu em structural completeness e technical precision, ele explicita se isso ocorreu por melhor visão geral do projeto, uso mais correto de nomes, funções, contexto e fluxo de dados.

Anotações humanas podem ser incorporadas ao processo como fonte adicional de avaliação, especialmente quando a qualidade desejada não cabe totalmente em uma regra automática. Elas funcionam como referência complementar para validar, calibrar ou contestar o comportamento do judge em casos difíceis. Isso é particularmente valioso quando a tarefa envolve documentação, utilidade prática e julgamento editorial, onde a preferência do modelo precisa ser confrontada com critérios humanos.

Documentação long-form tende a consumir muitos output tokens, o que aumenta tempo de execução e custo operacional. Mesmo com poucos exemplos, cada iteração pode ser lenta porque a geração é extensa e o julgamento ainda adiciona uma chamada extra. Por isso, a avaliação precisa equilibrar profundidade analítica com orçamento, principalmente quando o experimento for escalado para datasets maiores.

A validade de um experimento não é permanente, porque o comportamento muda quando o modelo muda. Um prompt que vence com ChatGPT-4o mini pode perder, empatar ou justificar de outro modo com GPT-5, Claude ou Gemini. Evaluation contínua existe para revalidar decisões sempre que mudam modelo, tarefa, critérios ou contexto operacional.

Em Prompt Engineering, comparar saídas lado a lado é parte do trabalho de engenharia, não um detalhe periférico. A utilidade real da avaliação aparece quando os objetivos de medição estão claros e o experimento produz evidência discutível por outras pessoas da equipe. Uma comparação com justificativa auditável permite defender escolhas, revisar critérios e iterar prompts com muito mais segurança metodológica.

## Transcrição

00:01

Bom pessoal, a gente fez essas avaliações, eu acho que ficou claro para vocês mudando o prompt e tudo mais, mas eu tenho mais um exemplo aqui de pairwise, baseado num dataset de documentação. Inclusive, esse tipo de coisa eu acredito que até em aulas ao vivo eu já mostrei esse tipo de exemplo. O grande ponto aqui é o seguinte, se eu olhar essa outra versão aqui de pairwise, você vai olhar dois prompts aqui para mim.

00:29

É um prompt que é focado em fazer documentações. Então, você é um experto em fazer documentação especializada em Python e IA, a sua documentação tem que ser high-level, tem que ter uma descrição, explanação, há um sumário e etc. Os dados têm que ser factuais e concisos, usar markdown e tudo mais. E aqui tem os arquivos do projeto para você verificar.

00:53

Tem aqui files. E, no caso, os nossos files aqui, galera, eles são os nossos datasets. Então, eu tenho um dataset que tem prompt.py, são três arquivos, basicamente, que eu peguei de um projeto da galera da LangChain. São três arquivos, eu botei o conteúdo desses três arquivos, ele tem que gerar uma documentação. O meu outro prompt é mais sem vergonha.

01:18

você é especialista, você vai receber alguns códigos fontes de um projeto, e o seu ponto é explicar, fazendo a documentação, que seja boa para os desenvolvedores, concise e concisa, mas não dando muitos detalhes técnicos específicos, detalhes e tudo mais.

01:36

Ou seja, deixei propositalmente esse prompt mais fraco. E aqui eu tenho o juiz. E o juiz, cara, olha só o que eu acabei fazendo. Criei um juizão bem grande, onde ele vai falar que ele é um juiz, aqui está o código, aqui está a referência, a...

01:53

do que eu estou querendo trazer, ou seja, o Ground Truth que eu tenho, a documentação A, a B, e eu criei as métricas de o que ele tem que avaliar, somando pontos, para ver quem vai ganhar. E eu criei as regras e falei como ele tem que retornar o resultado aqui para mim. Mas, aqui tem uma coisa que é importante em relação ao resultado, e é isso que eu queria mostrar para vocês e no exemplo anterior não tinha. Que é o quê? O resultado do juiz

02:23

ele vai falar quem ganhou e ele vai trazer a linha de pensamento dele, o porquê que ele escolheu. E aí, o que vai acontecer? Para cada item que eu coloquei, ou seja, consiteness, reference, alignment, clarity, utility aqui, technical precision, structural completeness, você vai perceber que para cada um

02:47

dessa categoria, ele vai falar para mim quem ganhou. E, ainda, ele vai justificar, de forma objetiva, o que aconteceu com isso aqui. Então, ele vai justificar. Então, não é só que o juiz vai falar quem ganhou e quem perdeu, que nem aconteceu aqui. Aqui, a gente tem algo mais implementado e incrementado para que a gente consiga entender realmente, vamos dizer, auditar a decisão. E não somente ter quem ganhou, A ou B.

03:16

é basicamente essa pegada aqui, tá? Então, o que eu vou fazer aqui vai ser o seguinte, eu vou dar um Python, vou rodar aqui um createPrompt, não sei nem se esses prompts estão criados, é capaz de eles já estarem criados lá. Beleza? Eu tenho que fazer o upload do dataset. Então, eu tenho aqui 4, uploadDataset,

03:46

Beleza? Então, já tenho meu dataset de geração de documentação, que tem um exemplo apenas. E agora, eu tenho que fazer a minha execução. O arquivo de execução, galera, é praticamente a mesma coisa que todos os outros. A diferença é o nome dos prompts e a evaluation. Basicamente, é a mesma coisa que a gente fez no outro, tá? Então, eu vou rodar aqui. 4 perwise doc. Eu vou dar um run aqui pra gente.

04:15

e vamos ver como é que esses caras aí vão sair. Então, ele vai começar a fazer a avaliação. Então, ele vai rodar o Prompt A e depois o Prompt B aqui pra gente. E, finalmente, depois que ele rodar esse, ele vai fazer a comparação. E a parte que, na minha opinião, é mais legal aqui nesse caso é exatamente a comparação, porque se você fizer o seu juiz bem feito, o que vai acontecer? Esse seu juiz

04:42

ele vai te justificar, e daí, eventualmente, você pode concordar ou não. Existe a forma de a gente fazer evaluação, onde você tem anotações, você anota aquela parada, ou uma anotação de um humano, entendeu? E daí, esses dados podem também ser utilizados para fazer evaluation baseado naquele dataset e coisas desse tipo. Então, é importante a gente saber disso aqui.

05:09

Enquanto ele está rodando, e aparentemente ele demora, por quê? Porque aqui é criação de documentação, então tem muito output token no final das contas. Mas ele tem apenas uma iteração, porque a gente tem apenas um registro. Diferente dos outros, que a gente tinha 10 registros, ele tinha que iterar pelos 10. Aqui ele demora

05:29

para uma interação, mas a gente sabe que uma interação ele vai executar, ele vai fazer a criação de uma documentação, né? Então, por isso que esse cara acaba demorando. Vamos ver se esses caras já estão começando a ser refletidos aqui. Então, apareceu aqui o dataset docgen, que é geração de documentação, mas agora você vai começar a perceber que eu fiz o seguinte também, eu pedi

05:54

para além de, eu pedi para que além de ele faça o pairwise, eu também pedi para ele trazer métricas, que na minha opinião são importantes nesse caso. Então, conciseness, a parte de detalhe,

06:13

e etc. Por exemplo, a cobertura de conteúdo aqui é muito baixa, porque eu pedi para ele ser conciso e não escrever muito. Então, você vai começar a perceber que existem algumas diferenças mais gritantes entre um e outro. Terminologia aqui é 0.4, aqui é 0.20, aqui é 0.6, tem caras que é 1, e daqui a pouco a gente já vai ver esses caras sendo completados e vamos ver como é que vai acontecer as diferenças aqui dos resultados. Vamos esperar ele acabar.

06:43

essa evaluation aqui. Na realidade, já deve estar acabando. Esse cara deve estar calculando agora aqui, ó. 1 e 1 aqui, 0.10, 0.20, 0.30. Então, a gente começa a perceber que existem diferenças por conta dos dois prompts que a gente acabou colocando aqui. E aí, a gente começa a ter um problema, tá? E qual que é esse problema? Eu tenho todos esses scores. E agora, quem que ganhou?

07:08

Você entende como é que a parte de pairwise é importante? Ela é importante exatamente por conta disso. Porque aqui eu tenho vários com 1, eu tenho um 0.9, mas aqui eu tenho um 0.7, aqui eu tenho um 0.6. Eventualmente, aqui é o 0.20, aqui é 10, aqui é 40, aqui é 30. Então, baseado nos critérios que eu coloquei aqui, quem ganhou? Então, por isso que o pairwise ajuda muito

07:37

porque ele não pega apenas essas métricas que são muito importantes, obviamente, mas ele consegue bater um cara com o outro, tá? Então, porque seria muito difícil a gente dizer aqui quem ganhou. Quem ganhou em qual perspectiva, né? Por isso que eu criei aquelas categorizações para ficar um pouco melhor ali para a gente. Então, se eu for agora aqui em pairwise experiments, eu vou ver que quem ganhou foi o prompt A versus o prompt B de 1 a 0. E por que 1 a 0? Porque só tinha um exemplo.

08:05

Se eu tivesse dez exemplos, aí a gente ia ter mais experimentos. Eu coloquei um só, mas o ponto importante agora aqui é o seguinte, eu vou ver a comparação, e aqui na comparação você vai perceber alguns pontos. Ele vai pegar todos os evaluators que a gente utilizou e vai trazer todos os evaluators que a gente utilizou, mas

08:28

Por que esse cara está vermelho e esse verde? Ele usou isso aqui para comparar? Não. Ele está olhando isso aqui, pairwisejudge e pairwisejudge. Aqui é 1, aqui é 0, e a gente vai tentar entender o porquê agora. Então, se eu clico agora aqui e quero ver o run dessa parada, como é que isso aqui vai funcionar? Aqui tem input, output, etc. Mas, quando eu clico agora em chat openAI,

08:53

Olha só que interessante, eu vou ter um output, e agora no output eu tenho o resultado da IA com a justificativa. Então, o reasoning dele, quando a gente está falando em estrutura e parte completa, o prompt A ganhou de 9 a 7, e a justificativa foi a documentação A, dados mais compreensivos, com uma visão geral do projeto, incluindo contexto, objetivos, tecnologias, data flow, etc.

09:19

Aí a gente tem Technical Precision, 9 a 7. A documentação A é mais acurada, traz mais nomes, funções, etc. Clarity e Utility, 8 a 7. A documentação A está mais ou menos organizada, etc. Reference Alignment.

09:36

Aqui, a documentação A também está melhor. Consciousness versus detail. Aqui ele empatou. As duas têm a mesma pegada e tudo mais. E aqui a A ganhou também. Então, se você perceber, agora eu tenho a justificativa daquele experimento, daquela linha específica. E agora, para mim, fica muito mais fácil entender a linha de raciocínio que o juiz colocou. Ou seja, é uma forma de eu...

10:03

ter um tracing do que realmente o juiz pensou com a justificativa para dar aquele resultado ali para a gente. Então, galera, eu espero realmente que tenha feito sentido isso para vocês. O nosso objetivo aqui principalmente não é aprender ferramenta, não é...

10:24

ficar fazendo um monte de cálculos e coisas desse tipo, mas como a gente está falando de Prompt Engineering, quando a gente coloca algum do lado do outro, é importante a gente saber e entender que isso é uma das coisas mais importantes e que elas são contínuas, porque os modelos mudam. O Prompt que você está agora com o modelo X,

10:45

às vezes o resultado dele é muito diferente. Aqui eu botei o chat GPT-4O mini. Talvez se eu colocasse o chat GPT-5, talvez se eu colocasse o Cloud, talvez se eu colocasse outro modelo, o Gemini, talvez a resposta fosse diferente. Então, é importante a gente ter essa clareza que

11:07

A gente precisa saber fazer evaluation, tá? E evaluation são coisas que aparecem em todos os lugares. Nesse nosso caso, e o prisma que a gente fez aqui, principalmente nesses capítulos, é realmente conseguir entender evaluation, mas muito mais pelo prisma da parte de...

11:29

Prompt Engineer. Legal? Então, agora eu acredito que para você que assistiu essas aulas, prestou atenção, usou, mexeu com os exemplos, vai ser muito mais fácil agora você sentar numa mesa com outras pessoas e conseguir discutir isso, entender as métricas, não ficar por fora e, principalmente, agora, se você tem objetivos claros do que você quer medir, sem dúvidas, esse aqui foi um ótimo ponto de partida para você.

11:57

Maravilha? Então é isso, galera. Espero que vocês tenham curtido. Grande abraço e é isso aí.

## Resumo IA

**Abreviações**  
- **A/B**: versão A e versão B, usadas para comparar duas saídas/prompts.  
- **AI**: Inteligência Artificial.  
- **GPT-4o mini**: versão menor do modelo GPT-4o da OpenAI.  
- **GPT-5**: versão do modelo GPT-5 da OpenAI.  
- **IA**: Inteligência Artificial.  
- **Markdown**: linguagem de marcação leve usada para formatar documentação.  
- **OpenAI**: empresa provedora dos modelos GPT.  
- **Prompt Engineering**: engenharia de prompts, prática de criar e ajustar instruções para modelos de IA.  
- **Python**: linguagem de programação usada nos exemplos da aula.  
- **IA/LLM**: modelo de linguagem de grande porte, quando o contexto se refere ao modelo gerando texto.  
- **Ground Truth**: referência considerada como base correta para comparação/avaliação.  

**Resumo**  
A aula mostrou como aprimorar avaliações pairwise em cenários de geração de documentação técnica. O instrutor explicou que, em vez de o juiz apenas indicar se a documentação A ou B venceu, é muito mais útil exigir que ele também justifique a decisão, tornando o processo auditável e permitindo entender a linha de raciocínio por trás do resultado.  

O exemplo apresentado usou um dataset com três arquivos de código de um projeto e dois prompts diferentes para gerar documentação. O Prompt A foi desenhado para produzir uma documentação high-level, factual, concisa, estruturada em Markdown e voltada a desenvolvedores. Já o Prompt B foi intencionalmente enfraquecido, pedindo uma documentação mais genérica e com menos profundidade técnica.  

Em seguida, o instrutor mostrou um juiz pairwise mais completo, que recebe o código, a referência/ground truth, as documentações A e B e uma rubrica de avaliação por categorias. As categorias destacadas foram conciseness, reference alignment, clarity, utility, technical precision e structural completeness. Essa decomposição permite analisar dimensões específicas da qualidade, em vez de depender de uma noção vaga de “melhor resposta”.  

O fluxo explicado foi: gerar as duas documentações, executar o julgamento comparativo e então inspecionar o output do juiz. A novidade principal foi o trace com a pontuação por categoria e a justificativa textual correspondente, permitindo ver exatamente por que a documentação A venceu em alguns aspectos, como completude estrutural e precisão técnica. O instrutor também comentou que anotações humanas podem ser usadas como referência complementar para calibrar ou contestar o comportamento do juiz em casos difíceis.  

Por fim, a aula reforçou que avaliações precisam ser contínuas, porque os resultados mudam conforme o modelo muda. Um prompt que funciona bem em um modelo pode ter desempenho diferente em outro, como GPT-4o mini, GPT-5, Claude ou Gemini. Por isso, avaliar saídas lado a lado, com critérios claros e justificativa auditável, é parte central do trabalho de Prompt Engineering.  

**Pontos de atenção**  
- Exigir justificativa do juiz é essencial para tornar a decisão auditável, especialmente em tarefas subjetivas como documentação long-form.  
- Não confiar apenas em scores auxiliares isolados; diferentes saídas podem vencer em critérios distintos e ainda assim gerar dúvida sobre o vencedor final.  
- Quebrar a avaliação em categorias explícitas ajuda a reduzir julgamentos genéricos e a entender trade-offs entre brevidade, completude, precisão e aderência à referência.  
- Em documentação técnica, a comparação deve considerar utilidade prática para desenvolvedores, não apenas aparência de qualidade.  
- Manter um prompt de referência forte e um prompt deliberadamente mais fraco ajuda a evidenciar o efeito das instruções na qualidade final.  
- A presença de ground truth/referência melhora a robustez da avaliação, mas não elimina a necessidade de análise humana em casos ambíguos.  
- Documentações long-form consomem muitos tokens de saída; isso aumenta custo e tempo de execução.  
- Mesmo com poucos exemplos, uma execução pode ser lenta porque a geração é extensa e a etapa de julgamento adiciona uma chamada extra.  
- Comparações pairwise são especialmente importantes quando vários critérios entram em conflito e não existe um vencedor óbvio.  
- Anotações humanas podem ser usadas para validar, calibrar ou contestar o juiz, principalmente em avaliações editoriais ou subjetivas.  
- Resultados de avaliação não são permanentes: mudar modelo, tarefa, critérios ou contexto pode alterar completamente o ranking.  
- Avaliação contínua é indispensável para revalidar prompts e critérios sempre que houver mudança de modelo ou de cenário operacional.