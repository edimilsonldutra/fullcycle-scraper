Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16869)

## Resumo da aula

Um prompt pode degradar a resposta não por falta de conteúdo, mas por excesso de instruções irrelevantes. No caso Bad Verbals, a revisão de código é cercada por exigências como introdução histórica, reflexão filosófica, ética e agradecimento ao leitor. Isso desloca o modelo da tarefa principal: analisar o código. O problema não é escrever muito, e sim gastar tokens com texto que não melhora a decisão técnica.

Detalhe útil é informação que aumenta a capacidade de agir sobre o código analisado. Quando a resposta adiciona história da linguagem, importância genérica de code review e comentários amplos sobre o futuro, ela parece rica, mas não fica mais específica nem mais útil. Retomando o cenário de revisão de código já usado antes, o evaluator penaliza justamente essa diferença entre volume textual e aderência à tarefa. Verbosidade sem foco reduz objetividade e compete com o espaço que deveria ser usado para apontamentos técnicos.

A execução mantém o mesmo padrão de avaliação sem referência já estabelecido anteriormente, mas agora o experimento isola um novo tipo de degradação: irrelevância por floreio. Os critérios observados são consistency, coherence, helpfulness e detail, suficientes para mostrar que a resposta pode parecer elaborada e ainda assim falhar funcionalmente. A escolha de não usar referência continua válida aqui porque o problema é visível na própria saída gerada. O experimento mede se o prompt produz uma revisão utilizável, não se ela coincide com um texto-alvo.

Os scores baixos mostram degradação ampla: coherence 0.35, consistency 0.23 e detail 0.37. A queda em consistency é especialmente esperada, porque o prompt força uma resposta longa e dispersa em vez de direta e objetiva. O ponto importante é que o score de detail também cai, mesmo com muito texto. Isso evidencia que quantidade de texto e qualidade de detalhamento são dimensões diferentes.

O comentário do evaluator explica a falha com precisão: o usuário forneceu código em Go, mas a resposta não entregou feedback sobre o código. Em vez disso, desviou para discussão sobre code review e história do Go. Esse tipo de feedback é mais valioso do que olhar apenas a nota, porque mostra a causa operacional da penalização: perda de contexto da tarefa. Quando o reasoning aponta irrelevância, a correção não é “pedir mais detalhes”, e sim remover instruções que empurram o modelo para fora do escopo.

Prompts verbosos podem deixar o dashboard “vermelho” mesmo quando a saída parece sofisticada à primeira leitura. Em revisão de código, introduções filosóficas e contexto enciclopédico não compensam a ausência de observações acionáveis sobre o trecho analisado. A regra prática é simples: toda instrução extra precisa justificar sua presença pelo valor que agrega à tarefa. Se o texto adicional não melhora a análise do código, ele tende a prejudicar relevância, utilidade e aderência ao objetivo.

## Transcrição

00:01

Agora, pessoal, a gente tem um outro cara, tá? E olha o que a gente vai avaliar. Consistency, a gente vai avaliar coerência, a gente vai avaliar helpfulness e detalhes aqui também, tá? E tô trazendo tudo sem referência.

00:18

E eu coloquei esse cara chamado Bad Verbals, ou seja, eu estou querendo colocar aqui, se você olhar, Bad Verbals, eu criei um prompt da seguinte forma, você é um professor de programação extremamente detalhista e filosófico, antes de analisar o código escreva uma introdução sobre a importância da revisão,

00:37

a história da linguagem, os princípios de programação, a filosofia. Agora analise esse código brevemente, depois analise e conclua com reflexões do futuro, considerações sobre ética, agradecimento ao leitor. Então, perceba que esse cara é o cara mais verboso que possa existir. E o que eu vou analisar com o cara verboso no final das contas?

01:01

Consistency, ou seja, o quanto mais esse cara tem que ser direto e objetivo aqui. Outra coisa que eu estou colocando é coerência, o quão coerente está aquilo baseado no que ele está escrevendo ali na saída.

01:17

E outra coisa, o quão... Help, né? O quanto aquilo realmente vai ajudar ali o usuário. E o nível de detalhes, né? Como é que isso também acaba trazendo. Então, vamos avaliar esses pontos aqui, porque eles são interessantes também. Então, vamos lá. Um aqui é oito. Vamos executar esse nosso camarada aqui. Vamos aguardar agora, somente para ver como é que vai ser os resultados, né? Dá uma baita curiosidade para ver.

01:46

E agora ele rodou aqui, então vamos ver como é que ficou. Então vamos entrar aqui.

01:53

Apareceu aqui o Bad Verbals, aqui o nosso camarada. Então, vamos olhar aqui. Coerência 0.35. Consistency 0.23, obviamente, ele escreveu pra caramba. Death a gente não pediu. Nível de detalhe 0.37. Apesar dele deve ter trazido muita coisa, ele não deve ter entendido que tudo que ele trouxe necessariamente teve

02:18

o nível de relevância que ele gostaria. Eu acho que se eu clicar aqui a gente consegue até depois explorar e entender o porquê que o nível de detalhe ele achou baixo aqui, por exemplo. Então, nesse cara aqui ele achou baixo, eu posso clicar e tentar entender o feedback aqui que rolou.

02:36

O assistente não trouxe informações relevantes. O usuário colocou um pedaço de código em Go, mas o assistente não proveu nenhum feedback em relação ao código. Ao invés disso, ele começou a colocar uma discussão de uma importância de um conto de review e a história do Go. Então, ele simplesmente levou em consideração que tudo saiu do contexto. Então, novamente, pessoal...

03:03

Como o prompt pode fazer assim a sua tela ficar completamente vermelha e por isso que trabalhar direito com prompts e ter essas métricas muito claras para a gente faz uma bela de uma diferença.

## Resumo IA

**Abreviações**  
- **Go**: linguagem de programação Go  
- **code review**: revisão de código  
- **feedback**: retorno/comentário sobre o resultado ou sobre o código  
- **prompt**: instrução textual dada ao modelo para gerar uma პასუხa  

**Resumo**  
A aula mostrou como um prompt excessivamente verboso pode degradar a qualidade de uma resposta em uma tarefa de revisão de código, não por falta de conteúdo, mas por excesso de instruções irrelevantes. No experimento “Bad Verbals”, o instrutor configurou um prompt com exigências como introdução filosófica, contexto histórico da linguagem, princípios de programação, reflexões sobre o futuro, considerações éticas e agradecimento ao leitor, antes de pedir a análise do código. A ideia foi demonstrar que esse tipo de floreio desloca o modelo da tarefa principal, que é analisar o código de forma objetiva e acionável.

A avaliação foi feita sem referência, observando as métricas consistency, coherence, helpfulness e detail. O resultado mostrou degradação clara, com scores baixos de coerência, consistência e detalhamento, evidenciando que uma resposta longa não significa necessariamente uma resposta útil. O ponto central é que o avaliador penaliza a falta de aderência ao objetivo: em vez de comentar o código em Go, a saída se perdeu em discussões genéricas sobre revisão de código e história do Go. O instrutor reforça que o problema não é a quantidade de texto, mas o uso inadequado de tokens em informações que não ajudam na decisão técnica. Assim, a correção não é pedir “mais detalhes”, e sim remover instruções que empurrem a resposta para fora do escopo.

**Pontos de atenção**  
- Verbosidade excessiva pode piorar a resposta mesmo quando ela parece sofisticada.  
- Introduções históricas, filosóficas e éticas geralmente não agregam valor em uma tarefa de análise de código.  
- Quantidade de texto não é sinônimo de detail: é possível ter muita verbosidade e pouco detalhamento útil.  
- A métrica consistency sofre quando o prompt força uma saída dispersa e pouco objetiva.  
- A métrica coherence cai quando a resposta perde aderência ao trecho de código analisado.  
- Helpfulness depende de o conteúdo ser acionável para o usuário; texto genérico não ajuda na revisão.  
- Em revisão de código, o foco deve ser sempre o código e seus problemas, não o contexto enciclopédico.  
- Toda instrução extra precisa justificar claramente o valor que traz para a tarefa principal.  
- O feedback do evaluator é importante para diagnosticar a causa da falha, e não apenas observar a nota.  
- Prompts mal desenhados podem deixar o resultado “vermelho” no dashboard por desvio de contexto.