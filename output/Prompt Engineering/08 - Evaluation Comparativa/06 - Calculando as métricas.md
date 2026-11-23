Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16934)

## Resumo da aula

O cálculo das métricas entra depois da execução do modelo, não durante a geração da resposta. O fluxo é: rodar o prompt, capturar os outputs, alinhar cada output ao example correspondente do dataset e transformar essa comparação em contagens que o LangSmith consegue registrar. Como o LangSmith não calcula automaticamente essas métricas nesse cenário, o pipeline precisa devolver os scores já prontos.

extractPredict é a função que normaliza e extrai do output do modelo apenas a estrutura comparável que interessa para a avaliação, como a lista de findings previstos. extractExpected faz a mesma operação do lado do dataset, convertendo o ground truth em uma estrutura com o mesmo formato lógico. Essas duas funções existem para evitar comparar objetos brutos incompatíveis, como texto livre de um lado e labels estruturados do outro.

O uso de zip faz o pareamento entre output previsto e example esperado pela posição, assumindo que ambos estão na mesma ordem e têm o mesmo comprimento. Isso simplifica o loop de evaluation porque cada iteração já recebe o par correto de itens para comparação. Se a ordem estiver desalinhada ou houver diferença de tamanho entre as listas, o cálculo inteiro fica contaminado, então esse é um ponto crítico do pipeline.

Retomando o cenário de code review em Go, os findings previstos e esperados precisam virar coleções comparáveis antes do cálculo. A operação central é tratar os itens de forma que interseção e diferença representem acertos e erros de classificação. Sem essa etapa, não há como derivar TP, FP e FN de maneira consistente.

True positives surgem da interseção entre o conjunto previsto e o conjunto esperado. Se o modelo retornou bug e error, e o esperado era bug e crash, a interseção contém apenas bug, que conta como acerto. Essa escolha funciona porque a interseção preserva somente os itens presentes nos dois lados.

False positives aparecem na diferença entre o previsto e o esperado. No mesmo exemplo, error foi retornado pelo modelo, mas não estava no ground truth daquele registro, então ele entra como excesso indevido. Essa operação captura exatamente o que o prompt acusou sem respaldo no dataset.

False negatives vêm da diferença inversa: esperado menos previsto. Se o dataset esperava error e o modelo não trouxe esse item, então esse finding foi perdido e precisa entrar como FN. Esse cálculo mede a parte do ground truth que ficou descoberta pela resposta do modelo.

O pipeline precisa tratar explicitamente casos em que os denominadores das fórmulas ficam zerados. Quando TP + FP é zero, a precision não pode ser calculada pela divisão direta; o mesmo cuidado vale para recall e, por consequência, para F1. Retornar 0 nesses casos evita exceções em runtime e mantém a evaluation executável em lotes inteiros, inclusive em exemplos vazios ou respostas sem findings.

O formato de retorno precisa ser compatível com a integração de evaluation, por isso cada métrica é devolvida como um dicionário com nome, score e comment. score carrega o valor numérico calculado, enquanto comment registra contexto útil para auditoria, depuração ou leitura no LangSmith. Em vez de retornar apenas um número solto, o pipeline produz uma estrutura que já serve tanto para processamento quanto para inspeção humana.

Precision, recall e F1 já foram definidos anteriormente; aqui o ponto novo é como alimentá-los corretamente a partir dos findings extraídos. Se a extração, o pareamento ou a comparação estiverem errados, a fórmula continua correta, mas o score deixa de representar o comportamento real do prompt. Em evaluation comparativa, a confiabilidade da métrica depende mais da qualidade desse pipeline do que da fórmula em si.

## Transcrição

00:01

Bom, pessoal, agora que vocês viram os prompts, eu quero trazer pra você como que a gente consegue calcular essas métricas. Por exemplo, o Langsmith não faz automaticamente essa conta. Então, a gente roda o processo de evaluation, pega o resultado da IA e a gente...

00:17

aplica essa fórmula e retorna lá para o Langsmith, para o nosso processamento. Então, basicamente, aqui eu tenho uma função que faz o cálculo de precisão e recall. Então, a ideia aqui é... eu tenho alguns parâmetros, eu já vou pegar aqui, basicamente, na documentação, que fica mais fácil no docstring, fica mais fácil para você. Então, basicamente, os outputs é a lista dos outputs que o modelo trouxe.

00:44

Os exemplos são os exemplos que eu tenho no meu dataset baseado nos dados que eu tenho para cada registro. A struct predict basicamente é uma chamada de função que eu estou ali pegando e tentando pegar exatamente o que a IA trouxe para a gente no nosso output. Ou seja, eu vou pegar o resultado da IA do modelo,

01:09

e extrair o output dele. Basicamente é isso. E o extract expected, eu vou pegar o nosso dataset e vou extrair aqueles exemplos do meu dataset, porque daí eu consigo comparar o output da IA com o output dos exemplos, lembrando sempre que o meu exemplo é o que eu considero correto, a minha referência. Beleza? Então, aqui, no final das contas, ele vai retornar esse tipo de dicionário. Uma aqui é precision, um score e um comentário.

01:38

recall, score e comentário, e o f1, score e comentário. Então, é basicamente dessa forma que a gente vai pegar a situação. Beleza? Então, aqui somente para ficar um pouco mais fácil de você entender com aquelas fórmulas que eu mostrei antes para você, o negócio é o seguinte, eu fiz um loop, esse loop, se você perceber, eu percorri o resultado da IA,

02:01

com os exemplos dela, com os exemplos que eu estava trazendo no meu dataset. Quando eu dou um zip, basicamente eu estou comparando a primeira linha dos primeiros exemplos do meu output com a primeira linha dos meus exemplos, ou seja, eu estou comparando dois objetos para mim simultaneamente.

02:19

Então, eu criei uma variável extractPredict, que vai extrair, é uma função, depois eu posso mostrar aqui para você, que vai pegar todos os resultados de output que a IA trouxe depois que ela rodou. E aqui, ele vai pegar todos os nossos outputs que o meu dataset tinha. E agora, a primeira coisa que a gente vai ter que fazer é calcular o que é

02:40

A verdadeiro positivo, true positive, falso positivo e falso negativo. Porque com esses três caras eu consigo calcular a precision recall e o F1. Então, o falso positivo, o que ele é aqui pra gente no final das contas?

02:56

Ele é a intersecção, por isso que eu estou colocando, eu estou dando um predict e commercial expected, ou seja, eu estou pegando somente o que é intersecção, ou seja, tudo que ele acertou. Então, nesse caso aqui, olha só que interessante, aqui desse lado eu tenho o bug e um error. Então, isso aqui é o que a IA trouxe para mim.

03:21

E aqui eu tenho um bug e um crash. Ou seja, aqui é o que é o certo que está no meu dataset. O que a IA acertou aqui nesse meu caso? Bug. Ou seja, o bug tinha aqui, o bug tinha aqui, então eu tenho um true positive aqui para mim. Beleza? Agora, eu tenho o falso positivo. O que é o falso positivo? É o que o modelo previu a mais, mas que não era verdade.

03:48

Ou seja, é o que ele errou, o que ele trouxe a mais para a gente. Então, a IA trouxe aqui para a gente um bug e um erro. E aqui eu estou subtraindo de um bug e um crash. O que isso significa? Esse erro aqui

04:11

ele está errado, vamos dizer assim, não era para a IA ter colocado aqui como erro, era a IA, ela tinha que ter colocado aqui como crash, então ela identificou um erro

04:24

que não existia. Então, isso é um falso positivo, ou seja, ela preveu a mais do que ela deveria ter previsto. Então, esse aqui que é o grande ponto. Então, eu tenho um falso positivo, é quando ela acertou a mais. E aqui embaixo, eu tenho o falso negativo, que é o que eu esperava menos o que foi previsto pela IA, o que a IA trouxe. Então, enquanto falso positivo, eu pego o que a IA

04:52

trouxe subtraio pelo que estava sendo esperado pelo meu dataset, aqui eu estou trazendo o que o meu dataset tinha menos o que a IA preveu. Então, nesse meu caso aqui, o que significa esse falso negativo? O que era esperado da IA, mas o modelo não conseguiu prever? Ou seja, foi um falso negativo. Então, a IA trouxe um bug e um crash. Legal?

05:17

E o que eu estava aqui, nesse caso, esperando? Eu tinha aqui, nesse meu caso,

05:26

eu tinha um bug e um erro aqui para mim. E aí, nesse caso, o que aconteceu? Esse crash aqui para mim foi um falso negativo. Então, esse é o grande ponto. Enquanto o 1 trouxe algo que não existia, ou seja, um falso positivo, o falso negativo estava esperando aquele erro, mas ele não trouxe aquele erro.

05:54

Esse aí que é o grande ponto, ou seja, eu esperava, ali naquele meu caso, o meu crash, e aí no lugar ele trouxe um erro ali para mim. Então, ali foi um falso negativo. Então, o true positive no final das contas, o bug ele acertou em todas, então o true positive.

06:12

Aqui, a gente tem um falso positivo porque, no final das contas, ele achou um erro que não era um erro. E aqui, a gente tem um falso negativo porque ele devia ter trazido, ali no nosso caso, o erro e ele trouxe o crash no final das contas. E daí, a conta aqui é simples, é a conta matemática, aquilo que eu falei. True positivo dividido por true positivo e mais falso positivo.

06:33

Se esses caras aqui forem maiores de 0, se não for, dá 0 aqui para eles, basicamente isso. E o recall é a mesma fórmula que eu mostrei para vocês e o f1 é a mesma fórmula que eu trouxe aqui para vocês. E aqui é a forma de como eu estou retornando aquele dicionário. Estou trazendo precisão, recall e f1.

06:57

E aqui, basicamente, como eu estava extraindo aquelas informações dos exemplos que eu estava colocando aqui, não vem ao caso. O importante é você entender isso aqui, que às vezes dá um nó na nossa cabeça. Beleza? Então, agora que a gente entendeu um pouco melhor de como essas métricas são calculadas, no próximo vídeo a gente vai fazer o upload do nosso dataset, a gente vai executar esses nossos caras e a gente vai ver como tudo vai ficar.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **TP** — True Positive (verdadeiro positivo)
- **FP** — False Positive (falso positivo)
- **FN** — False Negative (falso negativo)
- **F1** — F1-score

**Resumo**
A aula explica como calcular métricas de avaliação de um modelo depois da execução da resposta, e não durante a geração. O instrutor destaca que o LangSmith não faz esse cálculo automaticamente nesse cenário, então o pipeline precisa rodar o prompt, capturar os outputs, alinhar cada saída com o example correspondente do dataset e devolver os scores já calculados para registro.

Para isso, são usadas duas funções de normalização e extração: **extractPredict**, que pega do output do modelo apenas a estrutura comparável para avaliação, e **extractExpected**, que faz o mesmo lado do dataset, transformando o ground truth em um formato equivalente. O objetivo é evitar comparar objetos brutos incompatíveis, como texto livre contra labels estruturados.

O pareamento entre previsão e exemplo é feito com **zip**, assumindo que as duas listas estejam na mesma ordem e com o mesmo tamanho. A partir daí, o instrutor mostra como transformar os findings previstos e esperados em coleções comparáveis para calcular acertos e erros. O **true positive** vem da interseção entre previsto e esperado, o **false positive** da diferença entre previsto e esperado, e o **false negative** da diferença inversa. Com essas três contagens, é possível calcular precision, recall e F1.

A aula também reforça o cuidado com casos em que os denominadores das fórmulas ficam zerados. Nesses casos, o pipeline deve retornar 0 para evitar falhas em runtime e permitir a execução em lote, inclusive com exemplos vazios. Por fim, o retorno é estruturado como um dicionário com nome da métrica, score numérico e comment, para servir tanto ao processamento automatizado quanto à auditoria no LangSmith.

**Pontos de atenção**
- O LangSmith não calcula automaticamente essas métricas nesse fluxo; o pipeline precisa devolver os scores prontos.
- **extractPredict** e **extractExpected** devem produzir estruturas compatíveis; comparar dados brutos pode invalidar toda a avaliação.
- O uso de **zip** pressupõe mesma ordem e mesmo comprimento entre outputs e examples; desalinhamento contamina os resultados.
- Se a lista do modelo e a do dataset estiverem fora de sincronia, todos os cálculos de TP, FP e FN ficam comprometidos.
- A interseção entre previsto e esperado representa os acertos; se a normalização estiver errada, os acertos e erros serão classificados incorretamente.
- **False positive** é o item previsto a mais pelo modelo; **false negative** é o item esperado que não apareceu na previsão.
- É necessário tratar divisões por zero nas fórmulas de precision, recall e F1, retornando 0 em vez de gerar exceção.
- O formato de saída deve ser compatível com a integração, incluindo **score** e **comment** em cada métrica.
- A confiabilidade da métrica depende mais da qualidade do pipeline de extração, pareamento e comparação do que da fórmula matemática em si.