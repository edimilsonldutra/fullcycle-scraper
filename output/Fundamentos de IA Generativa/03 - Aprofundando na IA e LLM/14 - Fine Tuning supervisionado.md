Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16385)

## Resumo da aula

Fine tuning supervisionado é um processo mixed: combina conceito de treinamento com decisões práticas sobre dataset, custo computacional e escolha de técnica de adaptação.

Fine tuning supervisionado pega um modelo já pré-treinado e o adapta para uma tarefa específica usando exemplos rotulados. Em vez de expor o modelo a texto genérico, o treinamento passa a usar dados alinhados a um objetivo concreto, como responder dúvidas médicas, traduzir texto, escrever código ou resumir notícias. O efeito principal é sair de um comportamento generalista para um comportamento especializado em um domínio ou fluxo de trabalho. A analogia útil é a de alguém que já sabe português e depois aprende a linguagem operacional de um hospital para atuar melhor naquele contexto.

O núcleo desse treinamento é um dataset com pares explícitos de entrada e saída. Esses pares podem ser pergunta e resposta, código incompleto e código completo, ou qualquer estrutura em que exista um resultado esperado conhecido. O rótulo informa ao treinamento qual resposta está correta e qual está errada, guiando o ajuste do modelo. Sem esse pareamento, o processo deixa de ser supervisionado e perde o sinal direto de correção.

Retomando o ajuste de pesos já visto no pré-treinamento e em outros regimes de fine tuning, o mecanismo continua sendo backpropagation sobre a função de perda. Aqui, a diferença prática é que a perda compara a saída do modelo com uma resposta-alvo rotulada para a tarefa específica. A cross entropy loss, mencionada anteriormente, continua útil para medir a distância entre a previsão e a resposta correta. Esse sinal de erro atualiza pesos e vieses internos para aumentar a probabilidade de respostas adequadas naquele domínio.

Essa abordagem é indicada quando a aplicação exige desempenho alto em uma tarefa estreita, e não conhecimento amplo sobre qualquer assunto. Um chatbot corporativo da Magalu, por exemplo, precisa responder bem sobre catálogo, atendimento e tom de voz da empresa, mas não precisa dominar física quântica. O mesmo raciocínio vale para domínios com linguagem técnica, como medicina, jurídico e tecnologia. Também faz sentido quando os prompts sozinhos não conseguem carregar todo o contexto necessário de forma confiável.

Fine tuning supervisionado também serve para moldar estilo de resposta e regras de comunicação. Se a empresa exige um tom específico, proíbe respostas grosseiras ou não quer menções a concorrentes, essas preferências podem aparecer no dataset como exemplos corretos e incorretos. O caso do chatbot do Nubank ilustra isso: responder sugerindo um empréstimo no Bradesco é um comportamento desalinhado, então esse tipo de saída deve ser marcado como inadequado no treinamento. Guardrails continuam sendo outra camada possível, mas aqui o alinhamento já entra no próprio ajuste do modelo.

Quando o diferencial está em dados privados, o fine tuning supervisionado ganha valor porque o modelo passa a aprender padrões que não existem na internet pública. Conversas históricas de atendentes, documentos internos e linguagem própria da empresa podem formar um conjunto rico de exemplos sobre o que funciona, o que gera atrito e como responder melhor. Isso permite construir uma IA mais preparada para atendimento real do que simplesmente usar um modelo genérico sem adaptação. O ganho vem menos de “saber mais fatos” e mais de internalizar comportamento, vocabulário e critérios de resposta do domínio.

Overfitting acontece quando o dataset é pequeno, pouco diverso ou repetitivo demais, fazendo o modelo decorar padrões em vez de generalizar. O resultado tende a ser uma saída mecânica, com repetição excessiva e maior risco de respostas ruins fora dos exemplos vistos. Outro risco está nos rótulos errados: se o dado foi classificado incorretamente, o treinamento reforça um comportamento inadequado como se fosse correto. Além disso, modelos grandes com muitos dados e tokens exigem bastante computação, o que torna o processo caro.

Domínios que mudam com frequência, como medicina, exigem retreinamentos recorrentes para incorporar informação nova. Isso cria um custo operacional contínuo, porque a especialização envelhece à medida que o conhecimento do domínio evolui. Nesses cenários, a estratégia de atualização precisa ser pensada junto com a estratégia de treinamento inicial. Sem isso, o modelo fica caro para manter ou rapidamente desatualizado.

Fine tuning completo atualiza todos os parâmetros do modelo e costuma ser reservado para casos em que o novo domínio está muito distante do pré-treinamento original. O ganho potencial é alto, mas o custo computacional e financeiro também cresce bastante. Fine tuning parcial atualiza apenas parte da arquitetura, preservando mais do conhecimento anterior e reduzindo custo. O exemplo de um modelo treinado em inglês que precisa aprender contratos jurídicos em português mostra bem esse cenário: não é necessário reconstruir tudo para adicionar essa capacidade.

LoRA, sigla para Low-Rank Adaptation, insere matrizes adicionais em camadas do modelo para adaptar seu comportamento sem reescrever todos os parâmetros. Isso reduz o custo do treinamento e torna viável fazer ajustes incrementais, como atualizar um modelo médico com apenas os últimos seis meses de informação. PEFT, ou Parameter-Efficient Fine-Tuning, reúne técnicas com essa mesma filosofia de adaptar menos parâmetros para obter bom resultado. Em ecossistemas como Hugging Face, essas abordagens tornam a especialização mais acessível em infraestrutura real.

Prefix Tuning e Prompt Tuning seguem outro caminho: em vez de alterar amplamente os pesos do modelo, treinam um prefixo ou prompt interno que passa a orientar o comportamento da inferência. O efeito é parecido com manter uma instrução persistente acoplada ao modelo, funcionando como guia estrutural do que ele deve fazer. Isso pode ser vantajoso em modelos muito grandes, quando atualizar parâmetros é caro demais. A troca é que o controle vem mais da orientação aprendida do que de uma reconfiguração profunda da rede.

## Transcrição

00:00

Fala pessoal, beleza? Vamos falar agora um pouquinho sobre uma outra matéria super importante nessa nossa jornada que é o Fine Tuning Supervisionado. Então a gente falou primeiro do Fine Tuning Sem Supervisão, agora vamos entrar um pouquinho no Supervisionado para a gente entender como que ele vai funcionar. O Fine Tuning Supervisionado

00:18

ele vai ser um pouco diferente. A diferença aqui é que você vai pegar um modelo de linguagem que já foi pré-treinado lá atrás, tá bom? E esse fine tuning que você vai fazer, ao invés de você jogar um monte de texto genérico, você vai colocar texto especializado em uma determinada tarefa.

00:34

Então aqui imagina que você já tem o modelo pré-treinado, todo pronto, etc. Você vai fazer um fine tuning em cima dele, só que com uma tarefa específica. Você vai nichar o seu negócio, pensa assim. Então você não vai estar mais falando de uma IA generalista, e sim de uma IA que vai ser específica para alguma coisa.

00:50

Então, aqui você vai encher a memória dessa IA com respostas certas e erradas que você já conhece. Para isso, você vai precisar, por exemplo, de uma grande base de dados, se a gente parar para pensar. Vamos fazer uma analogia rápida aqui. Imagina que você aprendeu português aqui. Leu um monte de carta para aprender português. Carta, livro, etc.

01:11

no seu pré-treinamento. Agora você vai precisar fazer uma faculdade ou um curso intensivo para falar sobre hospital, para ser atendente de hospital. Você não vai ser um médico, mas você vai começar a atender as ligações e falar, olha, acho que vai fazer uma pré-triagem ali, por exemplo. Então imagina que você foi lá e fez um curso para fazer essa pré-triagem.

01:32

para fazer essa pré-triagem, então você aprendeu algo a mais, já sabia português, certo? você já tinha aprendido isso, agora você vai aprender a linguagem de hospital, como funciona, como as coisas se relacionam, e depois disso você vai começar a trabalhar no hospital, agora você já sabe o português, você já conhece aquele contexto, se você usar esse contexto numa borracharia vai funcionar não, mas o português vai, então a sua máquina generalista continua te apoiando durante toda a sua vida, mas a sua máquina que especifica isso, o seu

02:02

Fine Tuning sobre este assunto, sobre este aspecto, vai fazer você conseguir ir muito melhor naquela ação do que se você tivesse só a parte de português, beleza? Então é basicamente você transformar essa IA numa IA que tenha mais especialização.

02:17

tá bom esse é o finetuning supervisionado e como que ele funciona para vocês entenderem um pouco mais a fundo é primeiro você escolheu uma tarefa específica então por exemplo você vai querer que ele responde dúvida médica que ele quer traduzir texto ou que ele vai escrever código ou vai resumir notícias assim por diante esse é o primeiro passo

02:35

Segundo passo, você vai ter que montar um dataset específico, supervisionado, que a gente fala. Você vai montar um monte de dados ali pra conseguir passar pra ele. O que que significa montar esses dados? Aqui você vai ter que meio que classificar esses dados. Então você vai ter que falar quais são os dados de entrada, sempre em parzinho. Um exemplo, por exemplo, é uma pergunta e uma resposta.

02:53

um código incompleto e um código completo. Então, você tem uma entrada e uma saída já preparado, sempre em parzinho. Com cada exemplo desse, o rótulo vai decidir se aquilo está certo ou está errado e vai guiar o aprendizado. Qual que é o treinamento adicional que a gente tem?

03:11

o modelo inteiro vai receber todas as instruções que a gente tá falando e vai ajustar aqueles pesos e vieses internos como a gente falou anteriormente igual no pré-treinamento anterior, no fine tuning anterior, perdão. E com base nesse novo conjunto aí sim ele vai trabalhar o seu backpropagation pra conseguir melhorar a sua inteligência, pensa assim.

03:35

Neste fine tuning você também vai usar aquela função de perda, por exemplo, a cross entropy loss que a gente falou na última aula. Então você vai precisar dela para comparar também o que ela respondeu, qual a resposta correta, para conseguir ver qual que é o delta aqui e tirar a função de perda. Então você também vai usar isso, ele também é presente aqui.

03:53

Vamos falar de alguns exemplos práticos de utilização disso, chatbot médico, geração de código, etc.

04:08

sumarização automática, pergunta e resposta, tom de voz, você pode falar, olha pra minha empresa precisa ter um tom de voz específico, eu não quero que na minha empresa ele saia falando no tom de voz normal, eu quero que ele fale sempre de acordo com o que eu já tenho aqui do meu atendimento e falar no mesmo tom da minha empresa, por exemplo, não aceitar nenhum tipo de resposta que seja um pouco mais

04:29

grosseira, não falar nome de outra empresa, por exemplo. Eu trabalho no Nubank, aí eu faço lá o meu treinamento e o meu chatbot responde que é para o cara contratar um empréstimo lá no Bradesco. Não sei se eu quero, então você já tem que deixar ele já mais treinado para o seu contexto. Tem outros jeitos de você fazer isso também, com guardrails, mas aqui eu tô falando que você pode colocar dentro da sua função de fine tuning,

04:55

essa especificação, a resposta que fala isso está errada, você precisa ter uma resposta que fale outra coisa, então já deixa ele mais direcionado, mais organizado para o que você quer. Então quando você precisa de uma performance

05:07

alta em alguma tarefa específica, ou seja, você precisa que ele responda super bem naquela tarefa específica, você não precisa que ele responda. Vou dar esse exemplo de novo. Olha, eu sou o cara lá da Magalu, e da Magalu eu quero que ele responda muito bem sobre os artigos que eu tenho lá dentro, ele precisa responder isso super bem, mas não precisa que ele responda como funciona, sei lá, física quântica, ele não precisa saber isso.

05:28

Então, eu vou forçar ele, formar ele para saber muito sobre os artigos que eu tenho de venda, como funciona a Magalu, o Tom de Voz da Magalu e assim por diante, entendeu? Então, a maior parte das empresas, elas acabam passando um pouco por isso. Então, quando por exemplo, também os prompts que você tem sozinho já não vão bastar para guiar esse modelo, ou seja, quem vai promptar, ou seja, quem vai perguntar direto ali, não vai conseguir trazer o contexto direto, inteiro, então você já deixa isso já mais organizado para o contexto ser mais facilitado.

05:55

Não sei se vocês estão acostumados com o prompt, mas quando você vai promptar, é legal você falar qual base de dados você vai buscar, qual é a informação que você quer, o que você não quer e assim por diante. Querendo ou não, isso já nicha e guia o pensamento, a neural dele. Agora, se você tem um cliente que só vai perguntar, oi, como tá o tempo? Ele não tá falando de onde buscar, onde não buscar, ele pode falar como tá o tempo, buscando informação, sei lá, nos episódios do Chapolin.

06:19

Deu uma alucinada aqui né, mas vai que ele poderia teoricamente fazer isso. Então pô, se nichou, você já fala assim, olha, sempre que perguntado o tempo é pra buscar nos sites de padrão meteorológico, se você for promptar. Agora, se você quiser deixar isso já preparado pro seu cliente usar, por exemplo, ele não vai promptar. Então você já deixa isso direcionado, dando um monte de informação pra ele sobre como funciona

06:43

essa resposta de tempo, o que pode, o que não pode, assim por diante. Aqui eu misturei duas coisas que é base de dados e finetuning, mas só pra vocês entenderem um pouquinho de como funcionaria, tá? Outra coisa também que você pode usar o finetuning ali, supervisionado, perdão,

07:00

é quando o domínio, por exemplo, vai precisar de alguma linguagem técnica. Então, como eu falei, medicina, você trabalhar com a parte jurídica, tem uma linguagem técnica complicada, tecnologia, tem algumas áreas que tem uma parte técnica bastante difícil de ser implementada, então você consegue fazer um fine tuning pra ele entender também.

07:17

Ou quando, por exemplo, os dados que você tem são sensíveis, isso acontece muito também. Então, poxa, se eu preciso de dados sensíveis para usar, documento interno, informação de cliente, e esse tipo de coisa, ou a linguagem da empresa como eu falei, só você vai ter, não vai ter na internet. Então, por exemplo...

07:33

Se eu falar... Olha, todos os dados de conversas dos atendentes da empresa X durante os últimos 20 anos. Aqui eu tenho uma base de dados muito rica que fala o que eles falam que funciona, o que eles falam que não funciona, o que gera atrito, o que não gera atrito. Então, aqui você consegue deixar uma IA muito mais preparada para um atendimento do que você pegar direto um chatGPT e colocar lá, por exemplo. Então, aqui é super importante você pensar nesse tipo de aspecto quando você for fazer um fine tuning supervisionado, beleza?

08:03

Quais são as limitações que a gente tem? Quais são os cuidados que é legal a gente prestar atenção? Tem um negocinho chamado Overfitting. O que significa? Imagina que isso acontece bastante, tá gente? Imagina que o seu dataset, ou seja, o número de informações que você tem não é robusto o suficiente. Eu tenho pouca informação. Eu tenho ou muita informação repetida. Então olha, eu tenho uma base de dados pequena ou com muita informação repetida.

08:27

O que o modelo vai entender? Ele vai entender que essas respostas repetidas vão virar como se fosse uma pessoa decorando. Ele não vai mais gerar, ele vai acabar sempre gerando as mesmas coisas, porque ele meio que decorou o que você passou pra ele. Então essa pergunta e resposta vai ficar meio mecânica e ter uma chance grande dele alucinar ou dele responder besteira, porque ele não vai estar fazendo uma geração continuada como a gente normalmente tem. Então é importante você ter uma base,

08:54

de um tamanho considerável e você não ter texto sempre repetitivo ali. Se você tiver muita informação repetida, por exemplo, toda vez a pessoa pergunta a mesma coisa, o atendente responde a mesma coisa. Possivelmente isso vai gerar overfitting, tá? Outra coisa também que pode acontecer, e também acontece bastante, são os vieses nos dados. Quando você vai categorizar esses dados, o rótulo que você coloca neles,

09:16

Você pode ter erro. Então, você pode colocar no rótulo erro e gerar um viés errado e daí você vai atualizar os pesos e vieses do seu backpropagation estragando a sua IA de certa forma. E daí ela vai entender que aquilo é certo, mas você treinou ela errado. Pensa assim, você falou que estava certo. Então, ela está entendendo que está certo. Então, você pode fazer isso errado e dar um baita de um problema.

09:36

O custo, custo aqui também é um problema, o finetuning ele vai precisar de muito recurso computacional, principalmente se você tiver um modelo muito grande, base de dados muito grande e treinar um modelo muito grande, com muitos dados, muitos tokens, então isso vai dar um custo considerável.

09:53

Então é importante você pensar nisso também. Ou atualização constante. Se você, por exemplo, treinou, mas daqui seis meses você quer treinar de novo, você vai ter que retreinar, daí daqui seis meses retreinar de novo. Toda vez que o domínio muda, por exemplo, medicina, toda hora tá chegando coisa nova. Cara, possivelmente você vai ter que ficar retreinando. Então isso pode gerar

10:12

um problema já vou falar um pouquinho de alguns jeitos que você tem de resolver isso mas pode gerar um problema tá bom é esse tipo de atualização constante que vai sair caro é agora vamos pensar o seguinte hoje tem como que a gente resolve isso tá hoje tem algumas ferramentas por exemplo Hugging Face Transformers é uma delas o LoRA o

10:32

PEFT também é uma outra ferramenta que ajuda nisso. PEFT é Parameter Efficient Fine Tuning. Essas três ferramentas principais que eu conheço, elas ajudam você a fazer o fine tuning mais acessível e leve. Por quê? Porque aí você vai adaptar esse fine tuning, tá bom?

10:50

Então você vai conseguir trabalhar com menos dados e menos recursos do que você precisaria e vai gerar um ótimo resultado. Vou dar um exemplo, a gente já entra um pouco mais a fundo nisso, mas vou dar um exemplo do que eu falei. Imagina que você fez um Fine Tuning médico ali, pesado. Quero deixar esse cara bonitão, gastei dinheiro. Fui lá e fiz um Fine Tuning do que eu tenho de medicina dos últimos 20 anos. Agora eu preciso, depois de 6 meses, atualizar 6 meses. Eu posso pegar uma base reduzida, usar um LoRA, por exemplo, pra você deixar mais leve esse treinamento em cima só do que você tá incrementando.

11:20

porque esse cara já tá preparado, então você faz um fine-tuning incremental e usa uma ferramenta como se fosse o LoRa ou o Hugging Face e você consegue melhorar um pouquinho esse tuning com as novas informações, tá bom? Vamos lá!

11:34

O que é alterado quando a gente faz o fine tuning? Gente, é igual quando a gente tá fazendo o fine tuning que é não supervisionado, é igual ao supervisionado que vai acontecer. Os pesos da rede neural vão ser ajustados, então todos aqueles cálculos que a gente conversou lá no começo de rede neural, você vai ajustar os pesos e vieses.

11:54

Você vai fazer o backpropagation disso, igual no pré-treinamento, então isso vai pegar e vai voltar tudo de informação e vai gerar um novo cálculo da sua matriz neural. Depois, e aqui, o que acontece? Como os dados são muito mais direcionados e com rótulos específicos,

12:12

aqui você vai ter isso mais refinado e no final possivelmente a sua resposta vai ser melhor, você entendeu? Então você pegou toda uma base generalista, atualizou o peso disso, então a chance dele achar a palavra certa que vem na sequência melhora dado o seu contexto, você tá deixando ele contextualizado, ele não precisa ir muito longe, ele já sabe mais ou menos por onde ele tem que passar pra chegar ali, é como se você tivesse facilitado a vida dele no final das contas, tá bom?

12:37

Quais são os tipos de Fine Tuning que a gente tem aqui pra fazer? Você pode fazer um completo, ou seja, todos os parâmetros você vai atualizar. Qual que é o problema disso? Você vai precisar de muito poder computacional e você normalmente faz isso quando você tem um novo domínio ou quando você tem uma diferença muito grande do pré-treinamento.

12:54

Então, se você tiver que deixar um carinha totalmente diferente do que ele foi treinado inicialmente, possivelmente você vai ter que fazer um fine tuning completo pra conseguir preparar isso. Mas se prepara pra gastar dinheiro e pra ter tempo, porque isso aqui vai demorar e vai gastar dinheiro. Segundo ponto, fine tuning parcial, usando, por exemplo, LoRA como eu falei ou algum adapter tuning aqui.

13:13

Quando você faz esse cara, você tem só algumas camadas que vão ser atualizadas, você não vai atualizar ele inteiro. Vai ser muito mais leve e vai ser muito mais barato. E você não vai perder o conhecimento que você já tinha aprendido. Você vai continuar esse conhecimento. Então, por exemplo...

13:28

Imagina que você tem um modelo aqui que ele foi feito em inglês, isso acontece muito tá gente? Fiz um modelo em inglês, mas ele ainda não tá preparado pra atender por exemplo, contratos jurídicos em português. Eu posso pegar esse cara, jogar um finetuning parcial pra ele de contratos jurídicos em português, mas ele não precisa esquecer o inglês, ele só aprendeu agora português e contratos jurídicos, ele vai falar este linguajar dado meu finetuning parcial, eu não preciso adaptar ele inteirinho pra conseguir fazer essa coisa, beleza?

13:58

Como eu falei, tem algumas arquiteturas que podem apoiar. Deixa eu falar primeiro do LoRa. O LoRa, o que significa? É Low Rank Adaptation.

14:08

Low Rank Adaptation, isso, ele faz a inserção de algumas matrizes dentro das camadas que a gente tem ali do modelo e vai permitir que o fine-tuning seja mais leve e mais eficiente, tá bom? Então é um padrão que você tem, por exemplo, nas plataformas Hugging Face, que eu falei pra vocês, a PEFT, eles acabam usando esse LoRa por trás também pra funcionar, tá bom?

14:30

E você tem também o Prefix Tuning e o Prompt Tuning. Esses outros dois jeitos de fazer essas duas arquiteturas, ao invés de moldar o modelo, você vai treinar um prefixo, ou seja, um prompt interno, e daí esse prompt interno vai guiar o comportamento do modelo. Então, é como se fosse um prompt acompanhando o comportamento do seu modelo. Você não vai fazer todo um backpropagation, atualizando pesos,

14:56

e sim ter como se fosse um guard rail ou um guia que vai sempre pegando e jogando isso pro lugar certo. Esse vai ser melhor se você tiver um modelo muito grande pra você acabar gastando um pouco menos. Então são alguns jeitos de você fazer esse fine tuning mais direcionado, beleza? Já já a gente volta pro próximo passo da nossa aula. Um grande abraço.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **GPU** — Unidade de Processamento Gráfico
- **LoRA** — *Low-Rank Adaptation*
- **PEFT** — *Parameter-Efficient Fine-Tuning*
- **ChatGPT** — Modelo de linguagem da OpenAI baseado em GPT

**Resumo**
O fine tuning supervisionado é uma técnica de adaptação de um modelo pré-treinado para uma tarefa específica usando exemplos rotulados, em vez de texto genérico. A aula explicou que o objetivo é transformar um modelo generalista em um modelo especializado em um domínio, fluxo de trabalho ou estilo de resposta, como atendimento médico, tradução, geração de código, sumarização ou chatbot corporativo. A analogia usada foi a de alguém que já sabe português e depois aprende a linguagem e o contexto de um hospital para atuar melhor naquele ambiente.

O fluxo apresentado começa com a escolha de uma tarefa clara e, em seguida, a montagem de um dataset supervisionado com pares de entrada e saída, como pergunta/resposta ou código incompleto/código completo. Esses pares precisam de rótulos corretos para indicar o que está certo e o que está errado, pois esse sinal guia o aprendizado. O treinamento ajusta pesos e vieses da rede por backpropagation, usando função de perda como a cross entropy loss para comparar a saída prevista com a resposta-alvo e reduzir o erro.

A aula destacou que essa abordagem é especialmente útil quando a aplicação exige alta performance em um domínio estreito ou quando os prompts sozinhos não conseguem carregar todo o contexto. Também pode ser usada para moldar tom de voz, regras de comunicação e restrições específicas, como evitar respostas grosseiras ou menções a concorrentes. O instrutor reforçou que dados privados e linguagem interna da empresa são um grande diferencial, pois permitem ensinar padrões que não existem na internet pública e melhorar muito a qualidade do atendimento.

Por fim, foram apresentados os principais tipos e estratégias de fine tuning. O fine tuning completo atualiza todos os parâmetros e é indicado quando o novo domínio está muito distante do original, mas custa caro. O fine tuning parcial atualiza apenas parte do modelo e preserva mais conhecimento anterior. Entre as técnicas citadas para tornar esse processo mais eficiente estão LoRA, PEFT, Prefix Tuning e Prompt Tuning, que reduzem custo computacional e permitem adaptação mais leve e incremental, especialmente em ecossistemas como Hugging Face.

**Pontos de atenção**
- O dataset precisa ser realmente supervisionado, com pares explícitos de entrada e saída.
- Rótulos errados contaminam o treinamento e fazem o modelo aprender comportamentos inadequados.
- Dataset pequeno, repetitivo ou pouco diverso aumenta o risco de overfitting.
- Overfitting pode levar a respostas mecânicas, repetitivas e com pior generalização.
- Fine tuning em modelos grandes e com muitos dados pode ter custo computacional alto.
- Domínios que mudam com frequência, como medicina, exigem retreinamentos recorrentes.
- O custo operacional de manter o modelo atualizado pode ficar alto se não houver estratégia de atualização.
- Fine tuning completo é mais caro e deve ser reservado para casos em que há grande diferença em relação ao pré-treinamento.
- Fine tuning parcial e técnicas como LoRA são alternativas mais leves quando não é necessário atualizar tudo.
- Dados sensíveis e dados internos trazem valor, mas exigem cuidado com organização, qualidade e curadoria.
- O objetivo não é apenas “saber mais fatos”, e sim internalizar comportamento, vocabulário, tom e critérios de resposta do domínio.
- Guardrails podem complementar o fine tuning, mas não substituem a necessidade de um dataset bem alinhado.
- Em casos de tom de voz e restrições de comunicação, é importante incluir exemplos de respostas inadequadas e adequadas no treinamento.