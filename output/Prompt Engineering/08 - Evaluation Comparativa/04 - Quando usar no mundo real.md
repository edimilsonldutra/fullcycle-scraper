Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16932)

## Resumo da aula

Métricas como precision, recall e F1 só fazem sentido quando a tarefa admite verificação objetiva. Isso exige um critério externo claro para decidir se a saída está certa ou errada, em vez de depender de opinião, gosto ou interpretação aberta. Sem essa base, o número calculado parece preciso, mas não representa qualidade real. Em Prompt Engineering, isso define quando uma avaliação quantitativa é válida e quando ela apenas produz falsa confiança.

Ground truth é o conjunto de respostas de referência usado para comparar a saída do sistema. Ele funciona como a “verdade operacional” do experimento: sem ele, não há como contar acertos, erros, falsos positivos ou falsos negativos de forma consistente. Por isso, métricas clássicas dependem de um dataset rotulado com critério estável. Se o rótulo não é confiável ou não existe, a métrica perde validade antes mesmo do cálculo.

Essas métricas aparecem com mais força em problemas de classificação, porque a tarefa pede decidir entre categorias observáveis. Retomando o raciocínio de bugs já conhecido, o mesmo vale para casos como identificar se uma mensagem indica usuário bravo ou não. O ponto central não é o domínio, mas a existência de uma regra verificável para marcar cada item. Quando cada exemplo pode ser rotulado de forma consistente, o prompt passa a ser comparável como qualquer outro classificador.

O prompt não é apenas texto de instrução; ele é uma variável que altera o comportamento do sistema. Pequenas mudanças na formulação podem tornar a classificação mais agressiva, mais conservadora ou mais ambígua, deslocando o equilíbrio entre erros e acertos. Isso transforma avaliação em experimento de engenharia: muda-se o prompt, executa-se no mesmo dataset e mede-se o efeito. Sem esse controle, a comparação entre versões vira impressão subjetiva.

Considere um conjunto grande de conversas em que existe um critério para marcar quando o usuário está bravo. Se o prompt instrui o LLM a procurar sinais como o uso recorrente de uma palavra específica, a saída pode ser comparada com os rótulos esperados do dataset. A partir daí, mede-se quanto o sistema acertou e quanto errou de forma objetiva. Esse tipo de problema é adequado porque a decisão final pode ser tratada como classificação binária.

Tarefas como medir o quanto um conteúdo ajudou alguém, o quanto ele é “bom” ou a qualidade de um código em sentido amplo tendem a ser subjetivas demais para esse tipo de métrica. Nesses casos, o problema não está na fórmula, mas na ausência de um critério objetivo e reproduzível para rotular os dados. Se pessoas diferentes discordam estruturalmente sobre a resposta correta, precision, recall e F1 deixam de ser indicadores confiáveis. A avaliação precisa migrar para abordagens qualitativas ou comparativas.

O F1, já definido anteriormente, continua útil como resumo do equilíbrio entre cobertura e confiabilidade. Aqui, o ponto novo é o critério de aplicabilidade: ele só deve orientar decisão quando a tarefa realmente permite contagem objetiva de acertos e erros. Em classificação de bugs, por exemplo, F1 alto indica equilíbrio operacional aceitável; F1 baixo sinaliza que o prompt está perdendo casos relevantes ou gerando ruído excessivo. O número só é interpretável porque existe ground truth para sustentar a comparação.

Evaluation em sistemas com LLM cumpre papel análogo ao de testes em software. Ela não existe para “embelezar” o experimento, mas para garantir que mudanças no prompt não degradem o comportamento do sistema ao longo do tempo. Isso exige datasets, critérios de aceitação e comparação entre versões, exatamente como em práticas de qualidade de software. Quando o prompt é sensível a pequenas alterações, avaliar deixa de ser opcional e passa a ser parte do processo de desenvolvimento.

## Transcrição

00:00

Bom, pessoal, para a gente terminar, então, essa linha de raciocínio, quando que eu devo usar esses tipos de métrica para fazer algum tipo de validação? Novamente, esse tipo de métrica não é necessariamente focado apenas em prompt. A gente está falando de prompt engineer. Por que a galera de prompt engineer tem que se preocupar com isso? Mas o grande ponto aqui que eu quero que vocês entendam é que esse tipo de métrica é uma métrica objetiva.

00:30

Se você perceber, eu tenho uma fórmula. Não tem algo, no final das contas, que é subjetivo. Ou o quanto esse conteúdo é tóxico. O quanto esse conteúdo ajudou alguém. Ou o quanto eu achei bom a qualidade do código que aquele desenvolvedor fez.

00:52

Tudo isso que eu acabei de falar pra vocês é algo subjetivo, né? Ou seja, eu não consigo necessariamente calcular uma matemática tão exata, tá?

01:03

Já quando a gente está falando de precisão, recall e F1, a gente está falando de algo extremamente objetivo. E quando que você usa, então? Então, quando eu tenho situações que eu consigo realmente medir de forma objetiva. E, normalmente, isso acontece quando? Quando, normalmente, eu tenho que classificar alguma coisa. Como assim classificar?

01:29

Eu vou fazer o exemplo bobo novamente de... Tem um rabo, é um cachorro. Tem um rabo, é um gato. Mas tem uma orelha maior que a outra. Então, é uma orelha grande. Então, pode ser um coelho. Então, se você perceber, isso são formas como eu começo a classificar dados. E esse tipo de classificação, no final das contas,

01:50

Não é algo que principalmente existiu ou veio por conta de prompt ou por conta de a generativa. Esse tipo de métrica já existe faz muito tempo. Faz muito e muito tempo mesmo. A grande sacada aqui e o porquê que eu estou trazendo ela aqui é porque muitas vezes você vai ver com que o seu prompt

02:13

objetivamente consegue trazer mais coisas certas do que mais coisas erradas, tá? Então, a tangente que eu estou abrindo aqui para falar especificamente dessa métrica é exatamente para mostrar para vocês, e eu vou mostrar isso na prática, como que o Prompt influencia na classificação de pontos importantes ali para a gente, né? Dependendo, eu posso, vamos dizer, eu tenho uma conversa,

02:41

com o usuário final, e o usuário final muitas vezes escreveu de uma forma e eu quero saber se ele está bravo. Obviamente, a IA no LLM pode tentar identificar o mood da pessoa e saber se está bravo ou não.

02:57

Mas vamos imaginar que toda vez que o cara utiliza a palavra X, para mim é um indicador de que ele está bravo. Toda vez que ele usa aquilo, é um indicador de que ele está bravo. E aí vamos imaginar que eu pego um dataset gigante, e aí a IA sai varrendo aquilo ali para mim, e aí eu vou ver o quanto eu acertei e o quanto eu errei.

03:17

uma forma de medir isso é utilizando esses tipos de métrica. Então, se em algum momento você quiser validar o seu prompt para ver se ele acerta objetivamente algumas coisas ou algumas outras coisas não, com certeza esse tipo de métrica deve ser usado. Agora, se você estiver precisando de métricas que te ajudam a entender muito a parte qualitativa da coisa, a parte mais subjetiva,

03:43

Eu não gostaria nem tempo de ter esse tipo de métrica, porque ela não vai nem fazer sentido no seu dataset. Então, sempre vamos pensar o seguinte, se você tem o F1 alto, você tem um bom equilíbrio, ou seja, ele encontra, no nosso caso, bugs, sem muitos falsos positivos, e se tem o F1 baixo, é que ele tem um desequilíbrio, ou ele perde muito bugs, ou ele inventa bugs ali no nosso caso. Então, perceba que eu tenho formas objetivas de fazer essa metrificação.

04:13

E eu estou falando muito isso, pessoal, porque, principalmente quando a gente começa a cair em assuntos de evaluation, fazer verificações, testar, ver se a gente está acertando ou errando, é uma preocupação mais do que genuína, né? Você é obrigado a fazer isso, é como você desenvolver software sem testes. Se você não desenvolve software sem testes, você não consegue garantir esse software ao longo do tempo. E evaluation é algo que também acontece da mesma forma, mas eu precisava muito passar isso para você,

04:41

porque o prompt é algo extremamente sensível, nesse nosso caso, para conseguir resolver esses tipos de problemas. Beleza? Então, chegue de falação um pouco agora, vamos para o código, eu vou mostrar para vocês isso aí, como é que fica na prática.

## Resumo IA

**Abreviações**  
- **F1**: medida que resume o equilíbrio entre **precision** e **recall**.  
- **LLM**: *Large Language Model*; modelo de linguagem de grande porte.  

**Resumo**  
A aula explicou que métricas como precision, recall e F1 só devem ser usadas quando a tarefa permite verificação objetiva, isto é, quando existe um critério claro e reproduzível para decidir o que está certo ou errado. O instrutor destacou que, sem uma base confiável de comparação, como um dataset rotulado com **ground truth**, o número calculado pode parecer preciso, mas não reflete qualidade real. Esse tipo de avaliação é especialmente útil em problemas de classificação, nos quais cada exemplo pode ser rotulado de forma consistente, como identificar se uma mensagem indica que o usuário está bravo ou não.

Também foi reforçado que o prompt é uma variável que altera o comportamento do sistema, podendo torná-lo mais agressivo, mais conservador ou mais ambíguo. Por isso, avaliar prompts deve ser tratado como um experimento de engenharia: mantém-se o mesmo dataset, altera-se o prompt e mede-se o efeito sobre os resultados. O instrutor usou o exemplo de classificar conversas com base em sinais específicos, como o uso de uma palavra indicativa, para mostrar como a saída do LLM pode ser comparada aos rótulos esperados.

A aula diferenciou tarefas objetivas, nas quais precision, recall e F1 fazem sentido, de tarefas subjetivas, como medir se algo é “bom”, se ajudou alguém ou se a qualidade de um código é boa em sentido amplo. Nesses casos, o problema não está na métrica, mas na falta de um critério objetivo para rotular os dados. Por fim, o instrutor comparou evaluation em sistemas com LLM aos testes em software: ambos existem para garantir qualidade ao longo do tempo, prevenir degradação e permitir comparação entre versões de forma sistemática.

**Pontos de atenção**  
- Métricas como precision, recall e F1 só são válidas quando existe **verificação objetiva**.  
- Sem **ground truth** confiável, a métrica perde sentido antes mesmo do cálculo.  
- Tarefas subjetivas, como “qualidade” ou “utilidade” em sentido amplo, não devem ser avaliadas com essas métricas.  
- O uso correto dessas métricas é mais comum em **classificação**, especialmente quando há categorias claramente observáveis.  
- Pequenas mudanças no **prompt** podem alterar significativamente o comportamento do modelo; isso deve ser tratado como experimento controlado.  
- Comparar prompts sem usar o mesmo dataset e o mesmo critério de avaliação leva a conclusões subjetivas e pouco confiáveis.  
- Um **F1 alto** indica bom equilíbrio entre encontrar casos corretos e evitar ruído; um **F1 baixo** pode indicar perda de casos relevantes ou excesso de falsos positivos.  
- Evaluation deve ser tratada como parte do processo de desenvolvimento, assim como **testes em software**.  
- Se o problema for subjetivo, a avaliação deve migrar para abordagens qualitativas ou comparativas, e não forçar métricas objetivas.