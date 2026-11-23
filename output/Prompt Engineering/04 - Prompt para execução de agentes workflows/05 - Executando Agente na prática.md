Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16576)

## Resumo da aula

Retomando o padrão de comparação entre prompts, a forma correta de testar Chain of Thought é manter a tarefa fixa e mudar apenas a instrução de raciocínio. No caso da classificação do log Disk Usage at 85%, um prompt pede apenas Info, Warning ou Error, enquanto o outro exige justificativa passo a passo e resposta final após answer. Esse desenho isola o efeito operacional do CoT: ele não muda o problema, muda a forma como o modelo processa e expõe a decisão. Sem esse controle, fica difícil atribuir diferença de acerto, custo ou auditabilidade à técnica em si.

Quando o modelo recebe a instrução para pensar passo a passo, ele passa a externalizar a justificativa da classificação. Isso permite inspecionar por que Disk Usage at 85% foi tratado como info ou warning, o que é útil para depuração e validação de critério. O ganho vem acompanhado de mais tokens e, portanto, maior custo e latência; no experimento, a versão com raciocínio explícito consumiu bem mais que a resposta direta. A utilidade do CoT, portanto, não está em “sempre melhorar”, mas em tornar o processo observável quando isso compensa operacionalmente.

A pergunta sobre quantos R's existem em strawberry funciona como um teste simples, mas eficaz, para observar mudança de comportamento. Sem CoT, um modelo retornou 2, errando uma contagem elementar; com a instrução para quebrar a palavra em bullet points e apontar cada letra, o mesmo tipo de tarefa passou a produzir 3. O ponto importante não é a palavra em si, mas o mecanismo: decompor a entrada reduz o risco de resposta impulsiva e força uma verificação intermediária. Esse tipo de experimento mostra empiricamente quando o raciocínio explícito melhora acurácia.

Pedir passo a passo pode corrigir um erro em uma execução e ainda assim não garantir comportamento idêntico em todas as rodadas. O modelo pode variar a forma da explicação, o detalhamento e até a linha de raciocínio, mesmo quando mantém a resposta final correta. Isso significa que CoT melhora observabilidade e pode melhorar acurácia, mas não transforma o sistema em um mecanismo determinístico. Em aplicações críticas, a técnica precisa ser validada por repetição e comparação entre execuções.

O comportamento muda bastante quando o modelo já possui reasoning embutido, como no caso do GPT-5 Nano. Mesmo sem pedir passo a passo, ele acertou a contagem de strawberry, mas consumiu muitos tokens porque já executa raciocínio interno por padrão. Quando o prompt ainda adiciona um CoT explícito, o custo pode escalar de forma desproporcional, chegando a centenas ou milhares de tokens para uma resposta trivial. O conflito prático é este: instruir explicitamente um modelo que já raciocina pode redundar em sobrecusto sem ganho proporcional de qualidade.

Um ponto importante do experimento é que o modelo com reasoning não necessariamente devolve a cadeia de raciocínio visível, mesmo quando o prompt pede isso. Na classificação do log, ele respondeu apenas warning, sem mostrar as etapas intermediárias solicitadas. Isso indica que “raciocinar” e “exibir o raciocínio” não são a mesma coisa: alguns modelos usam processamento interno mais elaborado, mas não materializam esse processo na saída. Para quem depende de auditabilidade explícita, essa diferença afeta diretamente a escolha do modelo.

No mesmo log de disco a 85%, um modelo classificou como info e outro como warning. A divergência não é ruído superficial; ela revela que modelos diferentes aplicam heurísticas e contextos operacionais distintos ao mesmo input. Um modelo pode tratar 85% como estado ainda informativo, enquanto outro interpreta esse valor como sinal preventivo de risco de capacidade. Em Prompt Engineering, trocar de modelo sem revalidar o prompt significa aceitar mudança potencial no próprio critério de classificação.

Ao trocar para o GPT-4o, o experimento mostrou um comportamento intermediário: menos custo que o modelo reasoning e mais capacidade de detalhamento que o modelo mais antigo. Ele acertou strawberry e produziu uma justificativa mais elaborada para classificar o log como warning, contextualizando a necessidade de gerenciar capacidade de storage antes de um estado crítico. Esse resultado ilustra uma decisão comum de engenharia: nem o modelo mais barato nem o mais sofisticado é automaticamente a melhor escolha. O ponto ótimo depende da combinação entre acurácia suficiente, explicabilidade necessária e orçamento de tokens.

Lembra da referência anterior a custo, latência e auditabilidade: aqui esses fatores aparecem de forma mensurável no comportamento do sistema. Adicionar CoT pode melhorar a resposta, revelar o caminho lógico e facilitar troubleshooting, mas também aumenta tempo de resposta e consumo de tokens. Em modelos reasoning, o mesmo comando pode ser redundante ou até contraproducente em tarefas simples. A decisão correta é contextual: usar CoT quando o processo importa, e evitar quando a resposta direta já atende com custo menor.

## Transcrição

00:01

Bom, pessoal, então vamos ver o exemplo do Chain of Thought. Você vai ver como tem uma diferença muito grande nos nossos exemplos, e ainda mais quando a gente mudar o modelo, tá? Eu acredito que você vai ficar surpreso aqui com isso. Então é o seguinte, eu tenho uma mensagem principal aqui, novamente. Classifique o nível de criticidade desse log.

00:24

O input daí tem lá, Disk Usage at 85%. E eu coloquei aqui pra ele, responda somente, Info, Warning ou Error. Tá? Então, se você olhar aqui, não tem absolutamente nada de Chain of Thought. Só estou escrevendo aqui pra ele colocar. Beleza? Agora, eu tenho uma segunda mensagem aqui pra você se ligar. Classifique o log.

00:49

O disco tá em 85%, mas olha só agora como é que tá o meu prompt. Pense passo a passo sobre...

00:57

o porquê, tá? Isso é uma info, um warning ou um erro, tá? No final, dê somente, né, a resposta, no final de tudo, né, dê somente a sua resposta final depois de answer, né, eu pedi pra ele colocar, escrever answer ali no final, beleza? Temos o outro exemplo aqui, ó, questão. Quantos Rs

01:24

você tem na palavra strawberry, que é morango em inglês? Responda somente com o número de Rs.

01:33

Beleza? E a resposta aqui, a nossa mensagem aqui, 4, é quantos Rs tem na palavra strawberry? E daí eu coloquei assim, ó, explique passo a passo by breaking down, que é, ou seja, quebrando cada letra em bullet points, apontando os Rs antes de dar uma resposta final.

01:56

E daí eu coloquei, dê a resposta final depois de answer, tá? Então, é basicamente isso que eu acabei de colocar. Então, perceba que são quatro mensagens, elas são parecidas, e cada uma, uma usa...

02:14

chainOfThoughts e outra não usa chainOfThoughts e a gente vai testar essa parada com modelos diferentes aqui pra gente ver também os resultados, tá? Então, vamos lá, galera. Vou executar esse cara. Então, Python 1 e 3 aqui chainOfThoughts. Deixa eu rodar.

02:36

e a gente está usando o modelo mais fraco, que é o GPT Turbo aqui para a gente. Então, vamos lá. Primeira coisa aqui que a gente tem, né? Classifique o nível de severidade, né? E o response, ele deu info aqui para mim. Beleza. Beleza. Segundo prontips. Classifique o nível de criticidade, né? O disco é esse, eu coloquei. Pense passo a passo isso, aquilo e etc. Responda. E aqui, olha o tipo de resposta que ele já deu.

03:05

A mensagem de erro está informando o usuário sobre a utilização da percentagem do disco, o que é normal em sistemas de informação. Não existe nada, nenhuma indicação imediata de algum problema referente à utilização do disco a 85%. Então, não existe nenhuma ação para que o usuário tenha que tomar dessa informação. Então, a resposta é info.

03:33

Olha só o que ele fez aqui, nos dois ele deu info, mas aqui ele explicou o nível de pensamento, o porquê que ele chegou no info. Perceba como que eu consigo auditar o nível de resposta e a linha de raciocínio dele somente falando o passo a passo. E também você vai ver a diferença de tokens, eu tive aqui 110 tokens e aqui eu tive 35, então custou mais caro para mim.

03:56

E agora a gente chega no caso do strawberry. Pergunta quantos Rs tem na palavra strawberry. Responda somente com a quantidade de Rs. E aqui ele retornou pra mim dois, cara. Olha só.

04:11

E Strawberry tem três Rs, e ele está errando a contagem de Rs de uma palavra. E aqui o output tokens ele colocou 1, que é a letra 2 aqui pra gente. Agora vamos ali no passo a passo e ver o que acontece aqui pra gente. Quantos Rs tem no Strawberry? Pense passo a passo, quebrando em bullet points, etc.

04:32

Aqui, olha o que ele fez. Ele quebrou passo a passo, gerou o bullet point, e aqui ele deu que existe três Rs na palavra strawberry aqui pra mim. Então, perceba como colocar e fazer ele pensar em passo a passo pode mudar completamente o tipo de resposta. Isso significa que as respostas e as formas vão ser sempre iguais quando eu rodo? Não necessariamente, tá?

04:58

Aqui a resposta é diferente, mas ainda assim ele encontrou os três Rs do Strawberry aqui pra mim. Então, isso aqui pode mudar. Agora, eu vou fazer algo diferente agora. Ao invés de eu usar o GPT 3.5 Turbo, que é um modelo mais antigo,

05:18

Eu vou usar o GPT-5 Nano, que tem Reasoning. Ele vai demorar mais para responder. E vamos ver como é que ele vai trabalhar, principalmente em relação ao Strawberry.

05:30

Mesmo sem eu falar que ele tem que pensar passo a passo. Vamos ver o que ele vai responder aqui pra gente agora, porque isso muda bastante pelo fato desse modelo ele também pensar antes de responder, vamos dizer assim. Então, olha só, galera.

05:50

Ele gastou 1.300 tokens para responder se Strawberry tem 3 Rs, o meu prompt maior, porque eu pedi para ele pensar passo a passo. Beleza? Aqui,

06:04

onde eu falo pra ele quantos Rs tem no Strawberry, ele acertou aqui como 3, e eu não pedi pra ele pensar passo a passo, tá? Mas mesmo assim, ele gastou 235 tokens. Por que ele gastou bastante token? Porque, por padrão, ele pensa, e cada pensada que ele vai dar internamente, ele tá tendo output tokens aqui pra gente também, tá? Aqui, em relação à classificação, ele deu aqui pra mim como um warning,

06:35

tá, a utilização dos tokens né, ele respondeu aqui como warning e aqui em cima

06:43

ele trouxe aqui pra mim como warning. Mas perceba, tá? Quando eu falei, pense passo a passo e etc, etc, dê a resposta, ele só respondeu o warning e ele não trouxe pra mim o passo a passo. Por que isso pode ter acontecido? Talvez porque ele já é o modelo de reasoning e ele já está pensando passo a passo, logo ele respondeu apenas assim.

07:06

Você consegue perceber que quando você muda o modelo, você muda tudo. E quando você está trabalhando com Chain of Thought, a coisa vai para um outro nível, porque já tem modelos que já pensam e você embute um Chain of Thought e você consegue chegar a um nível de gastar 1.300 tokens para conseguir ter, no final das contas, uma resposta boba dessa. Se eu mudar esse cara aqui para o GPT-4O, vamos ver como é que ele vai responder aqui para a gente.

07:35

Ele vai responder mais rápido, porque por padrão ele não é de reasoning. Então, vamos lá. Aqui eu já melhorei. Eu tenho 247 tokens. Então, aqui ele conseguiu falar que tem 3 Rs o strawberry aqui pra mim, tá?

07:52

E aqui para mim, ele conseguiu resolver para mim o Strawberry com três Rs também no GPT-4. No 3.5, ele respondeu 2. Aqui é o passo a passo que ele dá do erro. Então, ele gerou o Step 1. Agora, se você perceber, o nível de detalhamento do passo a passo que o GPT-4 deu em relação ao passo a passo do 3.5 foi muito grande.

08:20

E ele gerou quatro passos, daí ele gerou aqui como um warning. E ele falou, cara, isso é um warning, não é uma info. E por que ele gerou o warning? Poderia ser uma info só, né? Falar que chegou a 85%. Por que ele fez isso? Aí ele colocou, pra contextualizar,

08:37

Pensando nos padrões operacionais e práticas, quando um disco bate 85%, a gente está num cenário que a gente tem que estar preparado para gerenciar a capacidade do storage, evitando um estado crítico de falhas. Por isso que ele considerou 85% alto.

08:55

E quando a gente olhou em outro caso, ele considerou, por exemplo, nesse caso com o GPT-4, ele entendeu como warning, mas com outro ele entendeu como info. Então, olha só como mudar o modelo, ele pode inferir, ele pode gerar outras linhas de raciocínio, linhas de raciocínio mais elaboradas, menos elaboradas e tudo mais. Então, o Chain of Thought, ele muda o jogo na hora de você trabalhar

09:22

com a IA e trabalhar com o prompt, porque ele vai determinar qualidade, ele vai determinar a latência, porque ele demora mais, e ele vai determinar o custo por conta da utilização de tokens. Beleza? Então, é isso aí.

## Resumo IA

**Abreviações**
- **CoT** — *Chain of Thought*; técnica de prompting que incentiva o modelo a explicitar o raciocínio passo a passo.
- **GPT** — *Generative Pre-trained Transformer*; família de modelos de linguagem usados nos exemplos da aula.
- **Info** — nível de severidade informativo.
- **Warning** — nível de severidade de alerta.
- **Error** — nível de severidade de erro.
- **CPU** — não mencionada.
- **Storage** — armazenamento.
- **Tokens** — unidades de texto processadas/geradas pelo modelo.

**Resumo**
A aula demonstrou como testar corretamente o efeito de Chain of Thought em prompts, mantendo a tarefa fixa e alterando apenas a instrução de raciocínio. O instrutor usou dois tipos de experimento: a classificação de criticidade do log “Disk Usage at 85%” e a contagem de letras R na palavra “strawberry”. Em ambos os casos, comparou uma versão de prompt direto, que pedia apenas a resposta final, com outra que exigia raciocínio passo a passo e resposta ao final após “answer”.

Nos exemplos com o log de disco, o objetivo foi mostrar que o CoT não altera o problema em si, mas a forma como o modelo processa e expõe a decisão. Sem CoT, o modelo respondeu diretamente com Info; com CoT, passou a justificar a escolha, permitindo auditar melhor o critério aplicado. Já no caso de “strawberry”, o raciocínio explícito ajudou o modelo a contar corretamente as ocorrências de R, mostrando que decompor a entrada pode reduzir erros de resposta impulsiva.

A aula também comparou diferentes modelos, incluindo o GPT Turbo, o GPT-5 Nano com reasoning e o GPT-4o. O GPT Turbo apresentou erro na contagem sem CoT e consumiu menos tokens quando respondeu diretamente. O modelo com reasoning acertou mesmo sem instrução explícita de passo a passo, mas gastou muitos tokens e, em alguns casos, não exibiu a cadeia de raciocínio solicitada, indicando que raciocinar internamente e mostrar o raciocínio são coisas diferentes. O GPT-4o ficou em um ponto intermediário: respondeu com mais detalhamento que o modelo mais antigo, acertou a contagem e justificou melhor a classificação do log.

O fluxo explicado pelo instrutor foi: criar prompts comparáveis, executar os testes em diferentes modelos, observar a resposta final, medir consumo de tokens e analisar a justificativa gerada. Com isso, ficou evidente que o Chain of Thought pode melhorar observabilidade e acurácia, mas também aumenta custo e latência. A escolha entre prompt direto e CoT, assim como entre modelos, deve considerar o equilíbrio entre precisão, auditabilidade e orçamento de tokens.

**Pontos de atenção**
- Para comparar CoT corretamente, mantenha a tarefa fixa e altere somente a instrução de raciocínio.
- CoT pode melhorar a observabilidade da decisão, mas aumenta consumo de tokens, custo e latência.
- Mesmo com passo a passo, o modelo não se torna determinístico; a forma da explicação pode variar entre execuções.
- Raciocinar internamente não significa necessariamente exibir a cadeia de raciocínio na resposta.
- Modelos diferentes podem aplicar heurísticas diferentes para o mesmo input; trocar o modelo exige revalidação do prompt.
- Em modelos que já têm reasoning embutido, adicionar CoT explícito pode gerar sobrecusto sem ganho proporcional.
- Em tarefas simples, pedir raciocínio detalhado pode ser contraproducente se a resposta direta já for suficiente.
- Use CoT quando a explicabilidade ou depuração forem necessárias; evite quando o custo adicional não compensar.
- A classificação de criticidade, como no caso de 85% de uso de disco, depende do contexto operacional e pode variar entre Info e Warning.
- Em tarefas de contagem ou decomposição textual, quebrar a entrada em etapas ajuda a reduzir respostas impulsivas e erros elementares.