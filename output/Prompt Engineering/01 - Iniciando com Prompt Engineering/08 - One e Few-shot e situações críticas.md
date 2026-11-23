Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16574)

## Resumo da aula

One-shot e few-shot orientam o modelo por demonstração: em vez de apenas descrever a tarefa, você mostra um ou poucos pares de entrada e saída para induzir um padrão de resposta. A utilidade principal está em tarefas nas quais o formato importa tanto quanto o conteúdo, como padronizar e-mails, gerar casos de teste semelhantes, resumir textos no mesmo estilo ou manter consistência em documentação de API. Em contraste com zero-shot, a instrução deixa de ser apenas declarativa e passa a incluir exemplos que funcionam como referência operacional. O ganho é mais controle sobre a forma da saída; o custo é maior dependência da qualidade e da clareza dos exemplos.

Quando o prompt mostra uma pergunta e uma resposta curta, o modelo tende a repetir esse mesmo formato na próxima resposta. Se o exemplo for “Qual é a capital da França? Paris”, a continuação “Qual é a capital do Brasil?” induz uma saída enxuta como “Brasília”, sem explicações extras. Esse comportamento é útil quando a aplicação precisa de respostas compactas, previsíveis e fáceis de consumir por código. O exemplo não apenas ensina o conteúdo esperado, mas também a estrutura exata da resposta.

Ensinar por exemplos funciona bem quando a tarefa depende de imitação controlada de estilo ou estrutura. Isso inclui formatar um e-mail com um padrão específico, criar um novo caso de teste a partir de um caso já mostrado, gerar um resumo semelhante ao exemplo fornecido ou produzir perguntas no estilo de quiz. Nesses cenários, o modelo não precisa apenas “entender o pedido”; ele precisa reproduzir uma transformação observada. A qualidade do resultado depende diretamente de quão representativo é o exemplo usado como referência.

Few-shot não cobre automaticamente todas as variações possíveis da tarefa. Se os exemplos forem rígidos, estreitos ou pouco representativos, o modelo aprende um padrão enviesado e passa a responder sempre na mesma linha, mesmo quando o caso novo exigiria adaptação. Isso reduz criatividade, empobrece a generalização e pode contaminar até o tipo de comentário ou classificação que o modelo produz. Mais exemplos só ajudam quando aumentam clareza; quando aumentam ruído, eles degradam a resposta.

Retomando o custo de tokens já discutido, one-shot e few-shot encarecem o prompt porque cada exemplo ocupa contexto adicional. Esse custo não é apenas financeiro: ele também compete por espaço na janela de contexto e pode aumentar latência. A decisão de usar exemplos precisa considerar se o ganho de previsibilidade compensa o volume extra de entrada. Em aplicações de alto tráfego, esse trade-off afeta diretamente a viabilidade da solução.

Um prompt com DatabaseConnectionLost at 10h34 -> error seguido de DiskUsage at 85% tenta ensinar uma regra de classificação a partir de uma única demonstração. O problema é que um exemplo isolado pode ser insuficiente para delimitar o critério real, e o modelo pode responder com algo inesperado, como status, em vez de warning ou error. Isso mostra que one-shot não garante entendimento semântico da tarefa; ele apenas oferece um indício de padrão. Quando o exemplo é pouco informativo, o modelo preenche as lacunas com inferência própria.

Quando a classificação inclui exemplos como Database Connection Lost -> error, Disk Usage at 85% -> warning e Response Time above threshold -> warning, o modelo passa a ter um padrão mais claro para mapear novos logs. Nesse cenário, API Response Time is above the threshold tende a ser classificado como warning porque há analogia direta com um exemplo anterior. O few-shot funciona melhor quando os exemplos são coerentes entre si e delimitam bem a fronteira de decisão. A técnica não “treina” o modelo no sentido tradicional, mas condiciona fortemente a resposta naquele contexto.

Adicionar muitos exemplos não significa aumentar qualidade de forma monotônica. Quando o conjunto inclui casos parecidos rotulados de formas diferentes, como Disk Usage at 90% -> error e outros sinais de threshold tratados como warning, o prompt passa a carregar conflitos internos. O modelo deixa de enxergar uma regra nítida e começa a arbitrar entre padrões concorrentes. Esse excesso de demonstrações pode introduzir mais ambiguidade do que clareza.

Em tarefas críticas, a consequência do conflito entre exemplos é variação de resposta para a mesma entrada. Um caso como CPU usage at 95% pode sair como warning em uma execução e como error em outra se o prompt contiver sinais contraditórios sobre thresholds, severidade e contexto operacional. Essa oscilação é especialmente perigosa quando a classificação aciona automações, como abrir uma issue no GitHub apenas em caso de erro. Se a saída muda entre execuções, o sistema deixa de ser confiável para decisões operacionais.

Quando o prompt acumula exemplos demais, o modelo pode perder a regularidade do critério que deveria seguir. Em vez de aplicar uma regra estável, ele passa a navegar por múltiplas pistas parciais e responde de forma inconsistente ao longo das execuções. O efeito observado não é apenas erro pontual, mas instabilidade estrutural: a mesma entrada produz respostas diferentes sem mudança real na tarefa. Em Prompt Engineering, isso é sinal de que o prompt está superespecificado de forma ambígua, não de que está bem calibrado.

One-shot e few-shot são úteis para ensinar padrão de saída, mas exigem curadoria rigorosa dos exemplos. Em cenários sensíveis, o objetivo não é maximizar quantidade de demonstrações, e sim reduzir conflito semântico entre elas. Um conjunto pequeno, claro e consistente costuma ser mais seguro do que uma coleção extensa com rótulos ambíguos. A técnica deve ser escolhida com base em previsibilidade observável, não na intuição de que “mais contexto sempre ajuda”.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente falou sobre zero-shot, ou seja, não dou exemplos para a IA responder para mim. A gente conseguiu ver, inclusive, diferenças de modelos. Agora, a gente tem outros tipos. Normalmente é chamado de one-shot ou few-shot, ou seja, ele dá um ou poucos exemplos de entrada e saída para o modelo aprender o padrão esperado. Então, quando que eu uso? Quando eu quero ensinar como formatar um e-mail, por exemplo.

00:27

Como eu quero criar um caso de teste adicional a partir de um exemplo. Mostrar um exemplo de um resumo de uma notícia e pedir um outro semelhante. Padronizar um estilo de documentação de API. Criar perguntas no estilo de quizzes de estudo. Qual é a limitação aí? A gente depende muito da qualidade do exemplo.

00:46

A gente não vai cumprir sempre todas as variações, porque dependendo do que a gente pede pode ser mais complexo ou menos complexo. Vai aumentar custo de token, porque você vai adicionar mais tokens no seu prompt para você dar os seus exemplos. Você pode enviesar a resposta, e esse é um problema.

01:04

porque às vezes eu dou exemplos tão rígidos que ele acaba criando um viés de sempre quando ele olhar aquilo, ele vai responder exatamente daquela forma e ele acaba sendo um pouco menos criativo, porque ele segue muito a linha, muito a risco os exemplos que você deu. E ele pode imitar demais e não inovar. Tem uma coisa

01:25

meio que parecida com outra, né? Então, você pode enviesar o exemplo até mesmo no tipo de comentário que ele vai dar, mas ele pode, por exemplo, imitar extremamente tudo o que você pede no exemplo que você coloca, ou seja, você começa a ter um nível de repetitibilidade muito grande,

01:41

e quando, às vezes, a gente tem que mostrar coisas menos consistentes, até mesmo numa redação, eu sei que a gente pode trabalhar com temperatura, isso aí pode atrapalhar um pouco ali pra gente, beleza? Vamos ver one shot e few shot aqui na prática? E eu quero trazer alguns pontos que poucas pessoas, às vezes, acabam falando, tá? Na realidade, eu comecei a entender isso na dor,

02:08

Daí, quando eu comecei a pesquisar, eu vi que realmente um monte de gente que estudou bastante sobre isso sabe, tá? Mas eu vou falar pra você sobre isso agora, tá? Então, vamos lá. Eu vou trazer aqui o exemplo pra você de one shot aqui pra gente. E eu vou renomear, porque ficou copy, porque eu tava duplicando meus arquivos. Aqui, ó. Prontinho. One ou few shot aqui pra gente.

02:32

E vamos aqui então, deixa eu fechar meu terminal para a gente ver melhor aqui para a gente. Então, o lance é o seguinte, eu tenho uma mensagem que é o seguinte, a mensagem número 1 aqui para mim. A minha mensagem número 1 é o seguinte, eu coloco o exemplo, questão, qual é a capital da França? E eu coloco Paris.

02:53

Questão, qual que é a capital do Brasil? E a response? Ele vai tender a retornar apenas Brasília puro. Por quê? Porque eu dei um exemplo aqui de como é uma resposta de uma capital. Então, esse aqui é um exemplo de one shot que a gente está dando. Agora, olha só que interessante, mensagem dois.

03:14

Eu dei um exemplo onde o input é DatabaseConnectionLost at 10h34. E o output é um erro, certo? Aí eu coloquei aqui pra ele. Agora classifique input DiskUsage at 85%.

03:32

Qual que é a output que ele vai retornar aqui pra mim? O que você acha que ele vai colocar aqui como output? Uma vez que eu dei também apenas mais um exemplo aqui pra ele. A gente vai ver como é que ele vai classificar isso aqui.

03:50

E eu tenho um terceiro exemplo aqui pra gente, tá? E o nosso terceiro exemplo vai funcionar da seguinte forma. Classifique o nível de severidade, o nível de criticidade, o quão crítico são os logs. Aí eu trouxe aqui, exemplo 1, Database Connection Lost, erro.

04:08

Exemplo 2, Disk Usage at 85% é um warning. Exemplo 3, Database Response Time is above the threshold at 30 milissegundos. Warning. O usuário foi logado com sucesso. Info. Agora classifique. API Response Time is above the threshold.

04:29

Então, vamos ver o que ele vai classificar nessa mensagem 3, onde eu dei quatro exemplos aqui para ele. Beleza? Agora, olha só, eu criei mais uma mensagem e ela é muito parecida com a anterior. Eu tenho o exemplo da conexão com banco de dados, eu tenho a utilização de 85%, que o cara conseguiu fazer o login, não encontrou um arquivo YAML, teve um erro,

04:55

a utilização de memória detectada em 75% está um warning, a background job finish está info, a retry and request payment gateway error, e aqui um disk usage at 90% ele está como erro e você

05:12

Eu coloquei aqui, somente para você se ligar, que é ambíguo, porque isso aqui pode ser um erro ou pode ser um warning, dependendo de como você está pensando na sua aplicação. Aqui eu botei como erro para exatamente gerar um nível de ambiguidade para ele.

05:27

Coloquei também, exemplo 9, a latência está acima do threshold, coloquei um warning. Então, perceba que o disk usage está acima de 90%, eu botei como um erro. A latência deu acima de um threshold, eu dei um warning aqui para ele. A memória saiu em cima de 75%, eu dei um warning aqui também. O backup foi completo, info. O disco está baixo, eu coloquei o warning.

05:56

E agora, eu coloquei o disco está baixo, aqui 5% left, eu coloquei um erro, ou seja, ambíguo também. Coloquei um exemplo 13, o warning do cache está completo. Exemplo 14, connection timeout, retrying, pode ser um warning ou, dependendo da situação, pode ser um erro. Coloquei autenticação e agora classifique. A utilização da CPU está em 95%.

06:25

Você percebe? Eu dei 15 exemplos. E a gente fala, cara, 15 exemplos, né? Talvez a parada seja top. Então, vamos ver como é que essa parada fica aqui pra gente. Então, eu vou executar. Então, eu vou dar um Python. Vou colocar aqui um. E o nosso é one shot, few shot aqui pra gente olhar. Vou dar um Enter. Deixa esse cara executar aí essas responses que a gente tem. Então, vamos voltar lá na primeira response que a gente tem. Não é de Brasília. Aqui.

06:55

Aqui, user prompt. Exemplo... Não, não, ele tem um outro aqui. Tá, aqui. One shot, né? Qual a capital da França? Paris. Qual a capital do Brasil? A resposta é Brasília. Perfeito. Maravilha. Agora, um exemplo de conexão com banco de dados perdida. Database connection foi perdida. Output error. Classifique. Disk usage. E ele trouxe aqui output status.

07:20

Olha só que estranho, cara. O que será que era isso? O que é status essa response? Perceba que, nesse caso aqui, parece que não deu muito bom essa história da response, ainda mais com o GPT 3.5 Turbo.

07:34

Vamos lá. Agora vamos aqui para baixo. User prompt. Classifique o nível de criticidade. Exemplo 1, database connection. Exemplo 2, discos 85%. Exemplo 3, passou do threshold. Exemplo 4, o user foi logado. Exemplo 5, a response da API passou do threshold. Qual que é o output? Warning.

07:55

Beleza! Ele trouxe o warning aqui pra mim e, provavelmente, porque ele olhou um pouco desse exemplo, onde passou do threshold, ele também trouxe como warning aqui pra gente. Aí...

08:07

Eu tenho outro prompt, exemplo 1, exemplo 2, exemplo 4, exemplo 5, e fui lá até o exemplo 15, classifique aqui para mim. Usage está acima de 95%. Ele retornou para mim como warning. O lance é o seguinte, galera, é que agora aquela história de depender da sorte, tá? Olha só, rodei o mesmo exemplo e olha só o que aconteceu.

08:35

Se você olhar, classifique agora, CPU 95%. Ele retornou para mim como um erro. Dei um Enter aqui novamente, vamos ver o que ele vai retornar. Retornou como um erro. Antes ele tinha retornado como warning. Agora, retornou como warning. Agora, se você pegar exemplos anteriores onde fez essa mesma pergunta,

08:59

você vai perceber que ele sempre vai retornar como warning, porque eu dei menos exemplos e um exemplo tá muito claro aqui, que quando o threshold passa é um warning. O que que eu tô querendo dizer com isso aqui pra vocês, pessoal? O que eu tô querendo dizer é que muitas vezes, tá? Muitas vezes,

09:18

Dar muitos exemplos vai gerar mais ambiguidade e mais margem para a interpretação da IA para dar respostas que a gente não estava esperando. Então, não é porque você dá muitos exemplos que normalmente você vai ter a melhor resposta. Então, tome muito cuidado.

09:38

com exemplo de menos no one-shot, dependendo da situação. O one-shot retornou status, que não fazia sentido nenhum, mas muitos exemplos também podem fazer com que gere mais possibilidades na cabeça da IA, ela perca uma linha de raciocínio e dê cada hora uma resposta diferente. E nesse tipo de situação, imagina que esse log poderia verificar se é para criar uma issue no GitHub ou não por conta desse erro.

10:07

Se der um erro, cria uma issue no GitHub. Se não der um erro, não cria uma issue. E daí, tem hora que dá erro, tem hora que não dá e ele ia sair criando issues simplesmente porque a gente deu um monte de exemplo aqui. Então, não necessariamente um monte de exemplo vai ser sempre a resposta aí para você.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **API** — Application Programming Interface (Interface de Programação de Aplicações)
- **GPT 3.5 Turbo** — Generative Pre-trained Transformer 3.5 Turbo
- **CPU** — Central Processing Unit (Unidade Central de Processamento)
- **GitHub** — plataforma de hospedagem e colaboração de código-fonte

**Resumo**
A aula explicou as técnicas de **one-shot** e **few-shot** como formas de orientar um modelo por demonstração, fornecendo um ou poucos exemplos de entrada e saída para induzir o padrão esperado. O instrutor contrastou essa abordagem com o zero-shot, destacando que, nesses casos, o prompt deixa de ser apenas uma instrução descritiva e passa a funcionar como referência operacional para o modelo. A ideia central é ensinar não só o conteúdo da resposta, mas também sua forma, o que é útil para padronizar e-mails, gerar casos de teste, resumir textos no mesmo estilo, manter consistência em documentação de API e criar perguntas em formato de quiz.

Foram mostrados exemplos práticos de uso, como a pergunta “Qual é a capital da França? Paris” seguida de “Qual é a capital do Brasil?”, para ilustrar como o modelo tende a repetir o formato curto e direto da resposta. Também foi apresentado um cenário de classificação de logs, em que entradas como “Database Connection Lost” deveriam ser mapeadas para rótulos como **error**, **warning** ou **info**. O instrutor demonstrou que, com poucos exemplos claros, o modelo tende a seguir bem o padrão, mas que o comportamento pode ficar inconsistente quando os exemplos são insuficientes ou pouco representativos.

Outro ponto abordado foi que o ganho de previsibilidade vem acompanhado de custos: mais exemplos aumentam o consumo de tokens, ocupam espaço na janela de contexto e podem elevar a latência. Além disso, exemplos rígidos ou contraditórios podem enviesar a resposta, reduzir a criatividade e gerar saídas instáveis, inclusive variando entre execuções para a mesma entrada. O instrutor mostrou que, em alguns testes, um único exemplo foi insuficiente e resultou em uma saída sem sentido, enquanto muitos exemplos, especialmente com critérios ambíguos, também levaram a respostas inconsistentes, como classificar a mesma severidade ora como **warning**, ora como **error**. A conclusão prática foi que a qualidade do resultado depende mais da curadoria dos exemplos do que da quantidade, e que em cenários críticos a escolha deve priorizar clareza, consistência e previsibilidade.

**Pontos de atenção**
- One-shot e few-shot não “treinam” o modelo de forma permanente; apenas condicionam a resposta no contexto do prompt.
- A qualidade dos exemplos é निर्णante: exemplos fracos, rígidos ou pouco representativos podem induzir respostas ruins.
- Poucos exemplos podem ser insuficientes para definir a regra corretamente, levando o modelo a inferir de forma errada.
- Muitos exemplos não garantem melhor resultado; podem aumentar ambiguidade e gerar respostas inconsistentes.
- Exemplos contraditórios ou com rótulos conflitantes criam ruído e confundem o critério de classificação.
- Aumentar a quantidade de exemplos eleva o custo de tokens e pode afetar latência e viabilidade em alta escala.
- Exemplos muito rígidos podem reduzir a criatividade e fazer o modelo imitar demais o padrão mostrado.
- Em tarefas críticas, variações de saída para a mesma entrada são um sinal de prompt mal calibrado.
- Quando a saída aciona automações, como abrir issues no GitHub, a inconsistência pode causar erros operacionais.
- A melhor prática é usar um conjunto pequeno, claro e coerente de exemplos, evitando superespecificação ambígua.