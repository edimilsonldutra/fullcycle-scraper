Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16933)

## Resumo da aula

Retomando o cenário de code review em Go, o dataset continua sendo a base do experimento: cada input contém um trecho de código e o ground truth define o output esperado para comparação. O ponto novo não está na estrutura dos dados, mas em como o prompt passa a funcionar como política de decisão. Em vez de pedir apenas “analise o código”, o prompt define o quanto o modelo deve suspeitar, o quanto deve se conter e quais tipos de evidência são suficientes para reportar um problema.

Um prompt agressivo instrui o modelo a reportar qualquer indício de erro, mesmo quando a evidência é fraca ou a possibilidade é remota. Essa política existe para maximizar cobertura: perder um bug é considerado pior do que gerar alertas indevidos. No code review, isso desloca o comportamento do modelo para uma postura de suspeita constante, aumentando a chance de capturar mais bugs reais, mas também de introduzir mais falsos positivos.

Um prompt conservador impõe um limiar de decisão alto: o modelo só deve reportar o que puder sustentar com certeza muito forte. A utilidade dessa política aparece quando o custo de investigar falso positivo é alto e a confiabilidade dos findings precisa ser máxima. No exemplo, restringir o escopo a poucas vulnerabilidades críticas e exigir certeza explícita torna o modelo seletivo, reduz o ruído e tende a favorecer precision, ainda que alguns bugs reais deixem de ser reportados.

Um prompt balanceado não tenta maximizar apenas um lado do trade-off; ele organiza o julgamento por categorias e define critérios diferentes para cada uma. No code review em Go, segurança, robustez/performance e qualidade de código recebem prioridades próprias porque não exigem o mesmo nível de evidência nem têm o mesmo custo de erro. O resultado é uma política intermediária: o modelo continua útil para cobertura, mas com freios explícitos para evitar acusações fracas ou estilísticas demais.

Few-shot, neste contexto, não serve apenas para mostrar formato de resposta; ele calibra o padrão de decisão esperado em cada classe de problema. Ao incluir exemplos de falhas de segurança, gargalos de performance, problemas de N+1, verbosidade excessiva ou nomes inadequados, o prompt ensina o que conta como finding relevante dentro daquele experimento. Isso reduz ambiguidade e aproxima o comportamento do modelo da política desejada, especialmente quando as categorias têm fronteiras diferentes.

A checklist transforma uma instrução genérica de revisão em um procedimento observável. Em vez de depender de uma noção vaga de “qualidade”, o modelo recebe uma lista de tipos de erro que deve procurar em cada categoria. Essa estrutura melhora consistência entre execuções, facilita auditoria do prompt e ajuda a deslocar o comportamento do modelo de forma controlada, porque cada item da checklist funciona como um lembrete operacional do que merece atenção.

Definir confiança mínima, como exigir 80% ou mais para reportar um finding, cria um limiar explícito de emissão de alertas. Esse mecanismo é especialmente útil no prompt balanceado, porque evita que o modelo reporte hipóteses fracas apenas por associação superficial. Quando combinado com regras específicas por categoria — análise mais profunda em segurança, padrões claros em robustez, exclusão de borderline cases em qualidade — o prompt passa a codificar uma política de risco, não apenas uma instrução textual.

Calibrar um prompt significa ajustar instruções, exemplos, categorias e critérios de confiança para deslocar deliberadamente o perfil de erro do modelo. Isso conecta diretamente o design do prompt às métricas já conhecidas: um texto mais permissivo tende a aumentar cobertura, um texto mais restritivo tende a aumentar confiabilidade, e um texto balanceado tenta preservar utilidade nos dois lados. Em avaliação comparativa, o prompt deixa de ser redação e passa a ser instrumento de engenharia experimental.

Comece com o mesmo código em Go e o mesmo ground truth para todas as variantes, porque a comparação só é válida quando o prompt é a variável experimental. Em seguida, escreva três versões: uma agressiva, instruindo o modelo a suspeitar de tudo; uma conservadora, limitando o reporte a casos de alta certeza; e uma balanceada, separando categorias, exemplos e regras de confiança. Execute cada prompt sobre o mesmo dataset, colete os findings no formato esperado e compare como cada política desloca o comportamento do modelo em relação às métricas já estabelecidas.

## Transcrição

00:01

Bom pessoal, então indo para o lado agora de código, eu quero trazer aqui para vocês como que eu organizei o dataset que a gente vai trabalhar. Então, nesse nosso caso aqui, eu tenho um input que eu tenho um código em Go, aqui colocado tudo numa linha. E aqui eu tenho o meu Ground Truth. Então, basicamente, o que eu estou esperando de output em relação a esse código.

00:22

Porque a IA vai analisar esse código, ela vai trazer um resultado nesse formato aqui, e a gente vai verificar se o formato que ela está trazendo bate com o que a gente está esperando. É basicamente isso, e é o que a gente tem feito inclusive nos exemplos anteriores. Então, aqui somente para você entender a ideia do dataset.

00:43

Agora, eu quero mostrar para você em relação à parte de prompt, que é uma das coisas que a gente está aqui para isso, certo? Então, o que acontece aqui é o seguinte, eu tenho três prompts diferentes aqui que eu quero mostrar para você. Um primeiro prompt, ele é um prompt bem agressivo. E por que eu estou chamando ele de agressivo? Eu estou falando o seguinte, o cara é um esperto em segurança, em code review, ele vai tentar identificar qualquer tipo de erro, mesmo que seja um erro bem remoto.

01:13

mesmo que ele ache que seja um erro. Então, o que eu tô falando é o seguinte, olha, você vai trazer tudo que você acha que é um erro, certo? Mesmo que for bem pequena essa possibilidade. É melhor você trazer coisa errada do que você perder

01:25

um erro, ou seja, você perdeu um bug. Você tem que ser extremamente rigoroso e suspeitar de tudo. Qualquer coisa que você olhar que pode estar abaixo, eu quero que você olhe e reporte isso aqui para mim. E aqui eu trouxe um monte de tipos de erro que ele pode encontrar. Então, se você perceber aqui, eu estou focando muito aqui em precisão.

01:48

Por quê? Porque eu tô mais preocupado em ele achar o máximo de coisa possível, mesmo que ele traga coisa errada pra mim. Porque pra mim, o mais importante é ele acertar tudo. E quando eu digo acertar tudo, é ele achar 100% dos bugs. Ele pode achar 100% dos bugs e errar trazendo alguns bugs que não existem, tá? Então, eu estou sendo agressivo por isso.

02:10

Aqui, eu estou sendo conservador. Aqui, eu estou focando ali muito mais no recall. Então, eu estou falando, olha, você só vai trazer o que você tem 100% de certeza. É melhor você não colocar nada do que gerar falso positivo. Foque apenas nas vulnerabilidades críticas. Eu passei apenas três vulnerabilidades. E analise o código abaixo. Aqui, os nossos findings. E aqui, basicamente, como esse cara vai responder. Eu coloquei os tipos forçados aqui. Ou seja, esse cara vai ser muito mais restrito.

02:39

ele só vai achar e vai trazer pra gente só o que ele tiver certeza e a gente tendenciou aqui o nosso prompt, vamos dizer aqui nesse nosso caso, tá? Ou seja, esse cara tem a intenção de ter um recall mais alto. Por que ele tem um recall mais alto? Porque ele é mais restritivo, ele prefere acertar, ele prefere não errar do que trazer coisa errada, né? Obviamente, né? Ou seja, ele quer ser muito mais

03:08

assertivo aqui nesse espaço, nesse ponto, ou seja, ele acaba sendo mais conservador. E eu tenho um cara mais balanceado aqui, esse cara eu escrevi um baita prompt aqui pra ele, ele tem que analisar o código Go, eu dei algumas prioridades pra ele, que é a parte de segurança, a parte de robustez e performance, a parte de qualidade de código, tá?

03:29

E o porquê que eu falei isso? Porque esses três tipos de situações são coisas que tem no nosso dataset, tá? E perceba que eu sempre trabalhei aqui com o Phil Schott para que ele tenha alguns exemplos de problemas que ele pode encontrar de segurança, problemas que ele pode encontrar de performance, problemas que ele pode encontrar de código de qualidade, qualidade de código, tá? Ou seja, nomes errados, tudo muito verboso, tem coisas que ele pode ter problema de N mais 1,

03:57

e coisas desse tipo. E eu coloquei aqui para a gente algumas regras para ele dizer em relação à confiança. Você só vai reportar o que você tiver 80% ou mais de confiança no código que você vai olhar, entendeu? Para a parte de segurança, o layer 1, você tem que ser thorough, ou seja, você tem que ser mais preciso, ou seja, verificar realmente o que é a vulnerabilidade. Para a parte de robustez, você tem que olhar padrões claros, ou seja, tem que ser óbvio.

04:24

que aquilo tem um problema. Então, perceba que eu estou tentando balancear em confiança, mas também em algo que é menos restrito. E a parte de qualidade, somente violações, mas também para ele escapar borderline case, ou seja, casos que são exceção. Então, eu falei para ele quais são as categorias,

04:42

de tipos de problemas que eu tenho e fiz uma checklist para ele de tipos de erro que ele pode encontrar, pontos que eu acho importante aqui para ele entender e trouxe o código para ele conseguir trabalhar. Então, se você perceber aqui, o que eu tive no final das contas é criei três prompts totalmente distintos para um prompt focar mais no recall, o outro mais em precision e o outro conseguir focar muito mais em tentar balancear

05:10

esses tipos de coisa. No próximo vídeo eu vou mostrar como que a gente vê isso um pouco mais na prática.

## Resumo IA

**Abreviações**  
- **Ground Truth**: referência/resultado esperado usado para comparar a saída do modelo.  
- **IA**: Inteligência Artificial.  
- **N+1**: padrão de acesso ineficiente em que uma consulta inicial gera várias outras consultas repetidas, causando gargalo de performance.  
- **Checklist**: lista de verificação de itens que devem ser analisados.  
- **Recall**: taxa de acerto para encontrar casos reais; mede quanto dos bugs verdadeiros foram reportados.  
- **Precision**: taxa de acerto dos alertas emitidos; mede quantos findings reportados são realmente corretos.  
- **Layer 1**: primeira camada/nível de análise mencionado no contexto de segurança.  

**Resumo**  
A aula retoma o cenário de code review em Go e mostra como o dataset é usado para avaliar o comportamento do modelo: cada input contém um trecho de código e o ground truth define o resultado esperado para comparação. O foco principal passa a ser o prompt, tratado não apenas como instrução de tarefa, mas como uma política de decisão que define o nível de suspeita, o grau de contenção e quais evidências são suficientes para reportar um problema.

O instrutor compara três estratégias de prompt. No prompt agressivo, o modelo é orientado a suspeitar de tudo e reportar qualquer indício de erro, mesmo com evidência fraca, priorizando cobertura máxima e aceitando mais falsos positivos. No prompt conservador, o objetivo é elevar o limiar de decisão: o modelo só deve reportar problemas com certeza muito alta, reduzindo ruído e favorecendo precision, ainda que isso faça alguns bugs passarem despercebidos. Já no prompt balanceado, a revisão é organizada por categorias com prioridades próprias, como segurança, robustez/performance e qualidade de código, cada uma com critérios específicos de análise e confiança mínima.

Também é explicado o papel do few-shot, que não serve apenas para mostrar o formato da resposta, mas para calibrar o padrão de decisão esperado em cada tipo de problema, usando exemplos de falhas reais como segurança, gargalos de performance, N+1, verbosidade excessiva e nomes inadequados. A checklist complementa essa abordagem ao transformar uma instrução genérica em um procedimento observável, ajudando a manter consistência e auditoria. Por fim, o instrutor reforça que calibrar o prompt é ajustar instruções, exemplos, categorias e critérios de confiança para alterar deliberadamente o perfil de erro do modelo. O fluxo prático recomendado é usar o mesmo código e o mesmo ground truth em todas as variantes, criar os três prompts com políticas distintas, executar cada um sobre o dataset e comparar os findings e métricas resultantes.

**Pontos de atenção**  
- O dataset deve permanecer o mesmo entre as variantes; o único fator a mudar é o prompt, para garantir comparação válida.  
- Prompt agressivo tende a aumentar cobertura, mas também gera mais falsos positivos.  
- Prompt conservador reduz ruído e falsos positivos, mas pode deixar bugs reais sem reporte.  
- Definir um limiar explícito de confiança, como 80%, ajuda a evitar alertas baseados em evidência fraca.  
- Em segurança, a análise deve ser mais profunda e criteriosa; em robustez/performance, devem ser considerados padrões claros; em qualidade de código, é importante evitar casos limítrofes e exceções borderline.  
- Few-shot deve refletir o tipo de finding esperado em cada categoria, senão o modelo pode interpretar mal o que é relevante.  
- A checklist melhora consistência e facilita auditoria, mas precisa ser bem alinhada às categorias do experimento.  
- O prompt balanceado exige separar prioridades e critérios por tipo de problema, em vez de aplicar uma regra única para tudo.  
- Calibrar prompt é uma tarefa de engenharia experimental: o texto influencia diretamente a relação entre recall, precision e utilidade prática.