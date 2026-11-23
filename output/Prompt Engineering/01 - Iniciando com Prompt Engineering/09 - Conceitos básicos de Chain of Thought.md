Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16575)

## Resumo da aula

Chain of Thought é a técnica de instruir o modelo a produzir ou seguir um raciocínio em etapas antes de entregar a resposta final. Ela se torna útil quando a tarefa depende do caminho, e não apenas do resultado, como em cálculos, explicação de lógica de algoritmo, análise de bug ou decomposição de um plano. A mudança central é esta: a saída deixa de ser apenas “qual é a resposta?” e passa a incluir “como o modelo chegou nela”. Isso altera tanto a forma de interação quanto a forma de avaliar a qualidade da resposta.

A técnica faz sentido em problemas nos quais o processo intermediário ajuda a validar a solução ou a tornar a resposta mais útil para quem vai consumi-la. Se você precisa ver etapas de correção de um bug, justificar uma conclusão em debate técnico ou decompor uma tarefa complexa em subtarefas, pedir pensamento passo a passo aumenta observabilidade. Retomando o repertório de técnicas já visto, aqui o ganho não está em estilo ou formato, mas em expor a sequência de inferências. Em tarefas simples, esse benefício normalmente não compensa.

Modelos mais recentes podem decidir internamente se respondem de forma direta ou se ativam um modo de reasoning mais elaborado. Esse roteamento funciona como uma camada de decisão: a pergunta é analisada e o sistema escolhe entre resposta curta ou processamento mais profundo. Ao adicionar instruções como “pense passo a passo antes de responder”, você pode induzir esse desvio para um caminho mais custoso e mais detalhado. Isso importa porque o prompt não afeta apenas o texto gerado; ele também pode alterar qual regime de inferência o modelo vai usar.

O valor mais forte do Chain of Thought é a auditabilidade. Quando o modelo expõe as etapas, você consegue inspecionar onde a conclusão começou a se desviar, em vez de observar apenas um resultado errado no final. A analogia do “justifique” é precisa: não basta dizer que a resposta é 22; é preciso mostrar como se chegou a 22. Em desenvolvimento de software, isso ajuda a depurar prompts e a localizar falhas de interpretação, regra ou cálculo.

Expor o passo a passo não garante correção. O modelo pode apresentar uma linha de raciocínio aparentemente plausível e ainda assim terminar com uma conclusão incompatível, ou até cometer erro dentro das próprias etapas intermediárias. O caso de “1 + 1” que é explicado como 2 e concluído como 3 ilustra uma falha de consistência entre processo e saída. Por isso, Chain of Thought melhora inspeção, mas não substitui validação.

Como o modelo passa a gerar mais texto e, em alguns casos, aciona reasoning mais pesado, o consumo de tokens tende a subir. Esse aumento afeta custo operacional e também latência, especialmente em sistemas com alto volume de chamadas ou agentes que executam múltiplas etapas. A referência anterior sobre custo de tokens continua valendo aqui, mas com um agravante: o ganho de transparência pode vir acompanhado de desperdício quando a tarefa já era simples. Usar Chain of Thought por padrão é uma decisão cara e frequentemente desnecessária.

Quando um software responde errado e a causa não está clara, ativar temporariamente Chain of Thought é uma estratégia de diagnóstico. Em vez de ajustar o prompt no escuro, você observa a sequência de inferências e identifica onde o modelo interpretou mal a instrução ou aplicou uma regra incorreta. Esse uso é especialmente valioso porque transforma um erro opaco em um erro inspecionável. Depois da correção, faz sentido reavaliar se o passo a passo precisa continuar exposto em produção.

## Transcrição

00:01

Bom pessoal, e agora a gente vai começar a entrar em tipos de prompts que são mais elaborados e mais complexos. Porque até agora a gente conseguiu entender que você dá um exemplo para a IA e a IA vai tentar imitar aquilo e adaptar aquilo com o contexto. Basicamente é isso que a gente fez, grosso modo falando.

00:23

Mas nós temos aí um tipo de prompt, uma técnica, e que ela mudou completamente, inclusive, como que os modelos trabalham, que é chamado de Chain of Thought, ou C.O.T. O que significa o Chain of Thought, no final das contas? Ele vai instruir o modelo a pensar em etapas antes de dar a resposta final.

00:45

Então, quando que eu uso? Quando eu quero resolver um cálculo matemático passo a passo, eu quero explicar a lógica de um algoritmo, eu quero listar etapas da correção de um bug, eu quero mostrar como a IA chegou a uma conclusão em um determinado debate, como que eu estruturo passo a passo de um plano de projeto. Então, eu tenho tudo que você pensar em passo a passo, você está pensando em chain of thought.

01:11

Depois, você faça um teste, entre no GPT ou em qualquer IA, e faça uma pergunta. Ele vai responder. Aí, coloque a mesma pergunta e escreva no final. Pense passo a passo. Você vai perceber que a resposta vai mudar completamente.

01:29

Hoje em dia, com o GPT-5, ele tem algo bem interessante que é um roteador. O que é um roteador? Basicamente, quando você chama o GPT-5 na interface, ele entende a sua pergunta e ele determina se ele vai...

01:47

responder direto ou se ele vai criar uma linha de pensamento, essa parte de reasoning que ele faz. Então, esse roteador verifica isso e aponta para o modelo de reasoning ou não, tá? Agora, se você quiser forçar, vá, por exemplo, no GPT-5 da vida, no chat GPT,

02:05

Escreva alguma pergunta e, no final, coloque, pense passo a passo antes de responder. Você vai perceber que o roteador dele vai mudar para a parte de reasoning simplesmente porque você escreveu, pense passo a passo. Isso é um ponto importante. Quais são limitações ou problemas que a gente tem? Resposta longa e verbosa, ou seja, porque ele pensa passo a passo, ele vai mostrar passo a passo para você.

02:30

Às vezes, ele pode inventar passos irreais, e isso aí é um problema até em modelos mais avançados. Tem pesquisas e tem algo que é chamado, se não me engano, inclusive, de deception e coisas desse tipo, que ele mostra a linha de raciocínio que ele fez, mas aquela linha de raciocínio não bate com a resposta final. Então, como que soma um mais um? Ele coloca, primeiro eu vou pegar um, depois eu vou pegar outro um,

02:59

aí eu vou somar, eu vou ter a resposta 2, e daí ele fala, conclusão final, 3. E daí existem esses problemas, e a IA não é perfeita. Melhora muito conforme os lançamentos e os modelos e o seu prompt.

03:14

Mas ela não é perfeita, então, chain of thought, você pode encontrar esse tipo de problema. Ou seja, nem sempre porque você falou para ela pensar passo a passo, a sua resposta vai ser correta. Às vezes ela erra no passo a passo dela na hora de fazer as contas. E quando a tarefa é simples,

03:30

você não vai usar isso, tá? Quando são coisas mais simples, ficar simplesmente usando isso vai te atrapalhar e vai fazer você gastar token, vai demorar mais para você ter a resposta e, às vezes, o resultado da resposta, a qualidade que você tinha sem fazer isso ia ser exatamente a mesma, tá? E vai aumentar bastante o custo de token. Então, você tem que pensar dez vezes antes de usar chain of thought

03:56

na hora de desenvolver um agente de IA ou um sistema que vai trabalhar às vezes, você escreveu no prompt ali de um jeito, meu amigo, ele vai moer token ali para você. Então, tome muito cuidado na hora de você optar por isso. O importante agora é que você conhece e entende melhor esse chain of thought, e uma vez que você entende isso, o passo a passo, já fica muito mais claro as coisas para você.

04:20

Uma coisa interessante também, em relação ao Chain of Thought, é que ele te ajuda a auditar a resposta. Ou seja, imagina que a professora vai lá e dá uma prova para você e faz uma pergunta, e daí você responde. A resposta é 22.

04:38

E daí, a gente sempre esquece que quando a gente estava na escola, a professora também, no final da pergunta, ela colocava justifique, né? Então, o justifique nesse caso é o chain of thought. Você vai ter que mostrar passo a passo como você chegou no 22, tá? Então, essa aí que é a grande sacada que a gente tem que pensar.

04:59

Você precisa justificar, auditar uma resposta para você entender... Imagina que você desenvolveu um software, aí ela está respondendo errado, cara. E você mexe no prompt, etc., assim, cara, como ela está chegando errado? Aí, você pode mudar o prompt temporariamente, colocar para ela trabalhar com chain of thought,

05:17

e aí ela vai mostrar o passo a passo dela, e aí você vai entender o porquê que ela está respondendo errado, porque naquela linha de raciocínio ela está raciocinando errada, e daí você pode corrigir isso no prompt. Então, isso aí é uma forma de você conseguir pensar. Para o vídeo não ficar muito grande, eu vou cortar aqui e a gente vai no exemplo prático para a gente ver.

## Resumo IA

**Abreviações**  
- **C.O.T. / CoT**: *Chain of Thought*.

**Resumo**  
A aula apresentou a técnica de **Chain of Thought (CoT)**, usada para instruir modelos de IA a resolverem uma tarefa em etapas antes de gerar a resposta final. O instrutor explicou que essa abordagem é mais útil quando o valor está no **processo** de raciocínio, e não apenas no resultado, como em cálculos passo a passo, explicação da lógica de algoritmos, análise de bugs, justificativa de conclusões em debates técnicos e decomposição de planos de projeto. A ideia central é tornar o raciocínio mais observável, permitindo entender como o modelo chegou a uma resposta.

Também foi abordado que modelos mais recentes, como o GPT-5 citado em aula, podem usar um **roteador** interno para decidir entre uma resposta direta ou um modo mais profundo de **reasoning**. Segundo o instrutor, prompts como “pense passo a passo” podem influenciar esse roteamento, levando o modelo a produzir respostas mais elaboradas. O principal benefício destacado foi a **auditabilidade**: ao expor as etapas, fica mais fácil identificar onde a lógica começou a falhar, especialmente em contextos de desenvolvimento de software e depuração de prompts.

Por outro lado, a aula ressaltou que expor o raciocínio não garante correção. O modelo pode apresentar uma sequência plausível, mas ainda assim chegar a uma conclusão errada, ou até incoerente com as próprias etapas intermediárias. Também foi enfatizado que o uso de CoT tende a aumentar a quantidade de texto gerado, o consumo de tokens, o custo operacional e a latência. Por isso, o instrutor recomendou cuidado ao aplicar essa técnica em tarefas simples, onde o ganho pode não compensar. Como estratégia prática, foi sugerido usar Chain of Thought temporariamente para diagnosticar erros e entender por que o modelo está respondendo incorretamente, e depois decidir se vale manter o passo a passo exposto em produção.

**Pontos de atenção**  
- Chain of Thought é mais indicado para problemas em que o **processo de raciocínio** importa, não para tarefas simples.  
- O uso de “pense passo a passo” pode alterar o comportamento do modelo e direcioná-lo para um modo de **reasoning** mais custoso.  
- Explicar o raciocínio **não garante** que a resposta final esteja correta.  
- O modelo pode produzir **etapas intermediárias falsas, incoerentes ou inventadas**, mesmo em respostas aparentemente bem estruturadas.  
- Em tarefas simples, o CoT pode ser **desnecessário**, aumentando latência e consumo de tokens sem melhorar a qualidade.  
- Em agentes e sistemas de produção, o uso indiscriminado de CoT pode elevar bastante o **custo operacional**.  
- A técnica é muito útil para **auditar respostas**, depurar prompts e localizar falhas de interpretação ou de lógica.  
- Uma boa prática é ativar CoT **temporariamente para diagnóstico** e reavaliar se o passo a passo deve permanecer exposto depois da correção.