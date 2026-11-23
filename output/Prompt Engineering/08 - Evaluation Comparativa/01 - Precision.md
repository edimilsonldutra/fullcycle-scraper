Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16929)

## Resumo da aula

Precision mede a proporção de acertos entre os itens que o modelo marcou como positivos. Em um cenário de classificação de bugs, isso significa responder à pergunta: entre tudo que o prompt chamou de bug, quanto realmente era bug. Essa métrica importa porque um sistema pode parecer ativo e “encontrar muitos problemas”, mas ainda assim gerar pouco valor se boa parte desses alertas estiver errada. Em Prompt Engineering, precision permite comparar prompts pela confiabilidade dos positivos que eles retornam.

True positive é o caso em que o modelo marca um item como bug e essa marcação está correta. False positive é o caso em que o modelo acusa bug onde não existe bug. Essa distinção é central porque precision penaliza diretamente alarmes indevidos: quanto mais false positives o prompt produz, menor tende a ser sua precision. Em operação, isso afeta a confiança da equipe no sistema, já que alertas incorretos consomem tempo de triagem e reduzem a credibilidade da automação.

A fórmula de precision é true positives / (true positives + false positives). O denominador contém apenas os itens que o modelo retornou como positivos, porque a métrica quer medir a qualidade dessas marcações, não a cobertura total do conjunto. Por isso, precision deve ser lida como confiabilidade dos positivos retornados. Se um prompt tem precision alta, a chance de um item marcado como bug realmente ser bug é maior.

Considere 20 logs, dos quais 10 realmente correspondem a bugs. Se o sistema identifica 8 bugs corretamente, ele produziu 8 true positives; se também marca mais 5 logs normais como bug, ele adiciona 5 false positives. A precision fica 8 / (8 + 5) = 8 / 13 = 0,61, ou 61%. Isso significa que, entre os itens que o sistema acusou como bug, apenas 61% estavam corretos.

Retomando o cenário de logs e bugs, um prompt pode ter boa precision mesmo deixando passar vários bugs reais. Isso acontece porque precision não mede quantos positivos existentes foram encontrados, mas apenas a qualidade dos positivos retornados. É aqui que recall entra como complemento e será reutilizado para interpretar o trade-off entre “acusar com confiança” e “cobrir mais casos”. Olhar apenas para precision pode favorecer prompts conservadores demais.

Mudanças de prompt deslocam o comportamento do modelo e, com isso, alteram precision, recall e F1. Um prompt mais agressivo, que tenta sinalizar qualquer indício de erro, tende a aumentar o número de positivos retornados, mas pode elevar os false positives e derrubar a precision. Já um prompt mais restritivo pode devolver menos alertas, porém com maior confiabilidade. A avaliação comparativa existe justamente para medir esse efeito em vez de depender de impressão subjetiva.

## Transcrição

00:01

Bom pessoal, agora que a gente entendeu pontos um pouco mais básicos em relação a evaluations, eu queria falar especificamente de precisão, recall e F1. Isso aí são métricas extremamente importantes e esse tipo de métrica não é apenas necessariamente para validar

00:23

Mas aqui eu vou conseguir mostrar pra vocês como a mudança de prompt consegue afetar a parte de precisão, recall e F1. Beleza? Então, eu queria começar com um cara de cada vez pra ficar um pouco mais claro aí pra vocês. E daí, na hora que a gente for ver na prática, a gente vai conseguir verificar isso ali no lang.smith e eu também vou mostrar código fonte aqui pra vocês. Beleza?

00:51

Então é o seguinte, a primeira coisa que a gente tem que pensar é em relação à precision. Você vai perceber que precisão, no final das contas, para esse tipo de métrica é tudo que o modelo consegue detectar e analisar.

01:09

quanto disso estava correto no final das contas, tá? Ou seja, vamos imaginar que eu tenho 10 bugs num sistema, o modelo detectou 5 bugs apenas. Então, o que isso significou? Que a precisão dele provavelmente diminuiu bastante, porque a ideia era ele tentar, no final das contas, identificar os 10 bugs ali pra gente.

01:30

Por outro lado, não é apenas tudo que o modelo detectou quanto estava correto. A gente tem algo também chamado de falso positivo. O que é um falso positivo? É quando o modelo detecta algo errado, ou seja, ele classificou algo que não era um bug como um bug.

01:49

Beleza? Então, a parte de precisão é o quanto que esse modelo consegue acertar no final das contas, quanto que ele consegue pegar de correto, independente se ele deixou passar algo, ou seja, trabalhou ali com um falso positivo, mas, ao mesmo tempo, acabou pegando, no final das contas, não pegando algo que era um true positive, algo que realmente era positivo para a gente.

02:18

como que eu consigo entender e conseguir identificar isso aí falando em métricas, em números. Existe uma fórmula que, basicamente, a gente fala que a precisão é o quê? É você pegar todos os true positivos, ou seja, o quanto que ele detectou que estava correto,

02:38

e você divide ainda por esses true positivos, por tudo que ele encontrou correto, mais os falso positivos, ou seja, quando ele detecta algo errado, ou seja, quando ele detecta um bug que na realidade não era um bug. Então, eu fiz um exemplo bem básico, eu não quero que a gente fique em fórmula matemática, apesar de serem

02:58

fórmulas extremamente simples, mas eu quero que você entenda a ideia de quando você olhar precisão. Eu não quero que você olhe para a precisão e fique pensando em fórmula. Eu quero que você olhe para a precisão e consiga entender, principalmente, a relação entre precisão e recall, que eu vou mostrar para vocês logo em seguida. Então, vamos imaginar que eu tenho 20 logs aqui no sistema. Desses 20, 10 deles realmente são bugs.

03:25

Então, vamos imaginar o seguinte, o sistema identificou oito bugs, porém, ele identificou também mais cinco logs como bug e que, na realidade, ele não era um bug. Então, dos 20, ele acabou identificando oito.

03:40

e mais 5 desses caras ali não era de fato bug. Então, como que isso aqui acaba ficando? Eu tenho o que eu detectei corretamente ali, que é o 8, que é o true positive, dividido por 8, que é o true positive de novo, mais os falsos positivos, ou seja, 5 falsos positivos, porque ele identificou 5 desses logs como...

04:05

como bug, e que não eram bugs ali nesse caso. Então, a nossa precisão aqui é de 61%, ou 0.61. Aqui está a nossa precisão. Então, o que significa quando a gente está falando em precisão em relação a... Quando alguém fala pra você, o que você tem que lembrar na hora? Uma alta precisão significa que eu vou ter um baixo índice de falso positivo.

04:29

Por outro lado, quando eu tenho uma baixa precisão, provavelmente eu vou ter também um alto índice de falso positivo, porque provavelmente ele acabou pegando mais coisa errada do que necessariamente certa também. Então, isso é uma das relações, eu posso relacionar precisão com muitos outros aspectos, mas, de forma geral, quando você vê em relação à precisão, você tem que pensar quanto o modelo acertou,

04:54

ou e também quanto que o modelo errou trazendo coisas que ele não deveria dizer que eram, tá? Então, essa que é a ideia de precisão, você vai perceber que rapidamente a gente vai evoluir para os outros pontos e você vai conseguir ver na prática como é que isso aí funciona. Maravilha? Então, vamos nessa. Próximo vídeo aí pra gente.

## Resumo IA

**Abreviações**  
- **F1**: *F1 Score* (ou *pontuação F1*), métrica que combina precisão e recall para avaliar o desempenho geral do modelo.  
- **precision**: precisão, proporção de itens classificados como positivos que वास्तवamente são positivos.  
- **recall**: revocação ou sensibilidade, proporção de positivos reais que o modelo conseguiu শনificar.  
- **true positive (TP)**: verdadeiro positivo, caso em que o modelo classificou corretamente um item como positivo.  
- **false positive (FP)**: falso positivo, caso em que o modelo classificou incorretamente um item como positivo.  
- **evaluations**: avaliações, processo de medir o desempenho de prompts ou modelos com métricas e critérios objetivos.  
- **lang.smith**: ferramenta citada para visualizar e analisar avaliações, métricas e comportamento de prompts.  

**Resumo**  
A aula apresentou o conceito de precision como uma métrica fundamental de avaliação em Prompt Engineering, especialmente para cenários de classificação de bugs em logs. O instrutor explicou que precision mede a confiabilidade dos positivos retornados pelo modelo, isto é, entre tudo o que foi marcado como bug, quanto realmente era bug. Para isso, foi apresentada a relação entre true positive, quando a identificação está correta, e false positive, quando o modelo acusa bug onde não existe bug. A fórmula destacada foi true positives / (true positives + false positives), mostrando que a métrica considera apenas os itens que o modelo devolveu como positivos.

O exemplo prático usou 20 logs, sendo 10 bugs reais. O sistema identificou 8 corretamente, mas também marcou 5 logs normais como bug, resultando em uma precision de 8 / 13, ou 61%. A partir disso, o instrutor reforçou que uma precision alta indica baixo índice de falso positivo, enquanto uma precision baixa normalmente revela mais alarmes incorretos. Também foi explicado que precision não mede cobertura, ou seja, um prompt pode ter boa precision mesmo deixando passar bugs reais, o que torna necessário considerar recall em conjunto. Por fim, o instrutor conectou essa discussão à avaliação comparativa de prompts, mostrando que mudanças no prompt alteram precision, recall e F1, e que essas métricas seriam observadas na prática no lang.smith e também por meio de código-fonte.

**Pontos de atenção**  
- Precision não mede quantos positivos reais foram encontrados; ela mede apenas a qualidade dos positivos retornados.  
- Um prompt pode ter precision alta mesmo deixando passar muitos casos reais, então não se deve interpretar essa métrica isoladamente.  
- Falsos positivos reduzem diretamente a precision e prejudicam a confiança da equipe na automação.  
- Prompt mais agressivo tende a aumentar alertas e pode elevar falsos positivos, derrubando precision.  
- Prompt mais restritivo pode melhorar precision, mas pode reduzir a cobertura de bugs reais.  
- A leitura correta da métrica é “entre o que foi acusado como bug, quanto estava certo”.  
- A comparação entre prompts é importante para evitar julgamento subjetivo e entender o impacto real das mudanças.  
- Precision deve ser analisada em conjunto com recall e F1 para interpretar bem o trade-off entre confiança e cobertura.