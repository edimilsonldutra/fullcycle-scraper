Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16930)

## Resumo da aula

Recall mede a capacidade de encontrar os positivos que realmente existem. Retomando o cenário de classificação de bugs, a pergunta agora não é se os alertas emitidos são confiáveis, mas quantos bugs reais foram capturados pelo sistema. Essa métrica existe porque um classificador pode parecer bom por errar pouco nos positivos retornados e, ainda assim, deixar passar casos importantes. Um recall alto indica cobertura alta dos bugs reais.

False negative é o erro em que um caso realmente positivo não é identificado pelo modelo. No exemplo de bugs, se existem 10 bugs reais e o sistema encontra apenas 7, os 3 restantes são false negatives. Esse erro importa porque representa falha de detecção: o problema existe, mas o sistema não o trouxe para análise. Em contextos operacionais, false negatives costumam ser caros porque bugs reais seguem adiante sem tratamento.

A distinção central entre as métricas está no tipo de erro que cada uma penaliza. Precision, já definida anteriormente, cai quando o sistema acusa bug onde não havia bug; recall cai quando havia bug e o sistema não encontrou. Essa diferença muda a pergunta de avaliação: uma métrica mede confiabilidade dos positivos retornados, a outra mede cobertura dos positivos existentes. Separar esses dois erros evita interpretar um sistema “cuidadoso” como bom quando ele apenas deixa muitos casos passarem.

A fórmula do recall é TP / (TP + FN). O numerador contém os bugs reais encontrados corretamente, e o denominador representa todos os bugs reais que deveriam ter sido encontrados, tanto os detectados quanto os perdidos. Por isso, recall não depende de quantos positivos incorretos o modelo retornou, e sim de quantos positivos reais ele deixou escapar. A métrica responde diretamente à pergunta: entre os casos positivos existentes, qual fração foi recuperada?

Recall pode ser lido como uma medida de sensibilidade do sistema a casos positivos. Um sistema mais sensível tende a sinalizar mais itens como bug para reduzir a chance de deixar bugs reais passarem. Esse comportamento melhora a cobertura, mas frequentemente aumenta o risco de incluir itens incorretos entre os positivos retornados. Sensibilidade alta, portanto, costuma deslocar o sistema em direção a mais recall e potencialmente menos precision.

Em Prompt Engineering, o texto do prompt altera o comportamento de decisão do modelo mesmo sem mudar pesos ou arquitetura. Um prompt mais fechado pode parecer bom porque acusa menos bugs indevidos, mas também pode falhar em encontrar bugs reais importantes, reduzindo o recall. Já um prompt mais agressivo tende a ampliar a cobertura e encontrar mais positivos reais, ao custo de possivelmente introduzir mais falsos alarmes. O efeito prático do prompt é deslocar o ponto de equilíbrio entre cobertura e confiabilidade.

Retomando a comparação com precision, as duas métricas observam lados diferentes do mesmo sistema de classificação. Quando o modelo é ajustado para encontrar quase tudo, o recall sobe, mas a precision pode cair porque mais itens duvidosos entram como positivos. Quando o comportamento fica mais restritivo, a precision tende a melhorar, mas o recall pode piorar porque alguns bugs reais deixam de ser marcados. Esse trade-off é a base para interpretar prompts conservadores, agressivos e balanceados nas comparações posteriores.

Um recall alto significa que poucos casos reais escaparam; um recall baixo significa que muitos positivos verdadeiros ficaram para trás. No exemplo citado, encontrar 9 de 10 bugs implica que apenas 1 escapou, o que caracteriza boa cobertura. A leitura correta da métrica sempre depende do custo de perder casos reais no domínio analisado. Quando deixar um bug passar é mais grave do que investigar um alerta extra, recall ganha prioridade na avaliação.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente falou sobre precisão, né? Então, a precisão, ela fala pra gente o quanto que o modelo estava correto, né? E quando ele fala em estar correto, é o quê? O quanto que ele não errou em relação a falsos positivos, tá? Ou seja, ele encontrou cinco logs, né, que...

00:21

não eram, de fato, bugs. Então, isso é um falso positivo, é quando ele erra. O recall é um pouco diferente. O recall, a gente pensa o seguinte, de tudo que o modelo devia ter detectado, quanto que ele encontrou, não é o quanto que ele errou nesse aspecto de falso positivo, do que ele pensou que era e não é mais. Aqui, no caso do recall, eu tenho o falso negativo.

00:47

Por exemplo, de 10 bugs encontrou apenas 7, então eu tenho 3 falsos negativos, porque 3 bugs não foram detectados. Não sei se você conseguiu entender a ideia, e eu vou repetir novamente, porque quando eu comecei a estudar sobre isso, me gerava uma confusão. A principal confusão aqui é o que é falso negativo,

01:10

e o que é falso positivo, tá? Então, o falso positivo é quando ele identifica algo e está errado. Ele pensa que está certo, mas ele está errado, tá? Agora, o falso negativo é quando ele não acha.

01:28

aquilo que estava correto, tá? Então, esse aí, o ponto é esse, tá? Então, o recall, ele pega, no final das contas, quanto que o modelo acertou e quanto que o modelo errou, mas ele errou pelo fato de não ter encontrado. Aqui em cima, ele errou pelo fato de ele ter encontrado errado, tá? Então, a nuance está aí. A nuance está na diferença de falso positivo, tá?

01:57

com a diferença de falso negativo. Falso negativo não acha, ou seja, ele olha ali e não acha, e o falso positivo acha errado. Basicamente é isso. Então, a fórmula é basicamente isso.

02:13

o que é positivo, true positives, dividido por true positives, mais o falso negativo. E aqui, o que muda é o falso positivo. Então, isso é a diferença que a gente tem entre recall e também imprecisão. Agora, o ponto é que, se a gente pensar de forma geral, é o seguinte, toda vez que eu acho um recall alto,

02:39

significa que eu encontrei a maioria dos bugs, ou seja, poucos caras escaparam, vamos dizer assim. Então, eu tinha dez problemas e ele encontrou nove, ou seja, escapou um. Então, é basicamente isso que eu tenho em relação a recall. Então, quanto maior o recall,

02:57

melhor. Quanto mais baixo o recall, ele é pior pelo fato de ele deixar de passar. Então, se você olhar, a gente acaba tendo essa conta, ou seja, precisão, ou seja, quando ele erra,

03:16

e o recall quando ele deixa de acertar. E se você começa a pensar dessa forma, a gente começa a tentar equiparar e balancear no final das contas. Por que eu estou dizendo isso? Se eu tenho, por exemplo, um alto recall, significa, no final das contas, que ele acha a maioria das coisas que eles deveriam achar. Por outro lado,

03:46

Um auto-recall pode fazer com que eu, além de achar o que eu deveria ter achado, ele pode ter achado também o que não era. E quando isso acontece, eu tenho uma precisão menor.

04:01

Agora, quando eu tenho um alto índice de precisão, ou seja, eu acho quase tudo que eu tinha que achar, que é o objetivo do recall, muitas vezes eu também acho errado. Então, é aí que está o trade-off que a gente tem. Ou seja, normalmente, se eu tenho muita precisão, significa que eu errei bastante também para eu ter muita precisão.

04:28

Ou seja, eu abri muito, vamos dizer, o leque para eu conseguir encontrar algo. É como se fosse sensibilidade. Quanto mais sensível eu sou, eu sou mais restritivo. Quanto menos sensível eu sou, eu sou menos restritivo. Mas quanto menos restritivo eu for, mais coisa errada eu vou fazer. Por outro lado, quanto mais restritivo eu for,

04:55

Provavelmente, eu vou ser achar mais coisas. Ah...

05:01

corretas, mas eu também vou deixar de achar as coisas que eu estava precisando. Então, eu sei que pode parecer até um pouco confuso. Se você não entendeu, eu recomendo que você assista novamente esses dois vídeos e tente fazer essa relação. Então, a gente acaba tendo dois lados ali da moeda e, se você perceber, é um trade-off. Não tem como você ter uma precisão extremamente alta

05:29

com um recall extremamente alto também. Normalmente, esses caras medem coisas diferentes e, às vezes, eles chegam a ser inversamente proporcionais. Se eu tenho um recall muito alto, provavelmente eu tenho uma precisão mais baixa porque eu posso...

05:50

no final das contas, ter errado mais nesse caso. Então, essa que é a ideia de precisão e recall. Então, tentem entender a ideia principal, não fiquem focados no que é fórmula e etc., mas sempre tente entender o nível de sensibilidade. Quanto mais sensível e mais restritivo, eu vou ter, provavelmente,

06:17

ali, um recall maior. Por outro lado, se eu tenho um recall muito maior, significa que eu vou deixar, muitas vezes, de pegar outros casos. Então, essa aqui é o tipo de proporção. E, no próximo vídeo, a gente vai falar sobre F1. O F1 é uma métrica extremamente importante e você vai entender por quê. Vamos nessa!

## Resumo IA

**Abreviações**
- **TP (True Positives)**: verdadeiros positivos; casos positivos que o modelo identificou corretamente.
- **FN (False Negatives)**: falsos negativos; casos que eram positivos, mas o modelo não detectou.
- **FP (False Positives)**: falsos positivos; casos que o modelo identificou como positivos, mas que não eram positivos.

**Resumo**
A aula explicou a métrica **recall** como uma forma de medir a capacidade do modelo de encontrar os casos positivos reais, usando o cenário de detecção de bugs como exemplo. O instrutor retomou a diferença entre recall e precision: enquanto a precision avalia o quanto os positivos retornados são confiáveis, o recall mede quantos dos positivos existentes foram efetivamente encontrados. Foram detalhados os erros relacionados a essa métrica, especialmente o **false negative**, que ocorre quando existe um bug real, mas o sistema não o detecta, gerando falha de cobertura.

Também foi apresentada a fórmula do recall, **TP / (TP + FN)**, destacando que o denominador considera todos os casos positivos reais que deveriam ter sido detectados, tanto os encontrados quanto os perdidos. O instrutor enfatizou que recall alto significa poucos casos reais escapando, enquanto recall baixo indica que muitos positivos verdadeiros ficaram sem detecção. Na parte prática, a aula conectou essa ideia com **Prompt Engineering**, mostrando que o texto do prompt pode tornar o modelo mais conservador ou mais agressivo, alterando o equilíbrio entre recall e precision. Por fim, foi reforçado que existe um **trade-off** entre essas métricas: aumentar a cobertura tende a reduzir a confiabilidade dos positivos retornados, e vice-versa.

**Pontos de atenção**
- **Não confundir false positive com false negative**:
  - false positive = o modelo acusa algo errado;
  - false negative = o modelo deixa passar algo que era positivo.
- **Recall não mede confiabilidade dos resultados retornados**; isso é foco da precision.
- **Recall alto significa boa cobertura**, ou seja, poucos positivos reais ficaram de fora.
- **Recall baixo indica falha de detecção**, com muitos casos positivos escapando.
- **Aumentar recall pode reduzir precision**, pois o modelo tende a aceitar mais casos como positivos, inclusive alguns incorretos.
- **Reduzir a quantidade de alertas indevidos pode prejudicar o recall**, porque o modelo fica mais restritivo e pode deixar bugs reais sem detecção.
- **O prompt influencia diretamente o comportamento do modelo**, mesmo sem alterar pesos ou arquitetura.
- **Prompts mais fechados/restritivos** tendem a aumentar precision, mas podem diminuir recall.
- **Prompts mais agressivos/sensíveis** tendem a aumentar recall, mas podem piorar precision.
- **A interpretação correta depende do custo do erro no domínio**: quando deixar um caso real passar é mais grave do que gerar um alerta extra, recall deve ter prioridade.