Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16867)

## Resumo da aula

Embedding Distance mede proximidade de significado entre dois textos comparando seus embeddings, em vez de pedir julgamento direto a um LLM. O evaluator transforma predição e referência em vetores e calcula uma distância ou similaridade, como cosseno ou L2. Isso importa quando o interesse está na aderência semântica geral da resposta, não apenas em formato ou presença literal de termos. O resultado é um sinal contínuo de quão próxima a saída está da referência em espaço vetorial.

Um evaluator baseado em embeddings delega a comparação semântica ao modelo de embedding, não a um modelo que produz reasoning textual sobre a resposta. Essa escolha reduz a avaliação a uma operação geométrica entre vetores, o que tende a ser mais simples e rápido operacionalmente. Em contrapartida, a métrica perde capacidade de interpretar intenção, contexto de tarefa e adequação funcional além da semântica capturada no embedding. Por isso, ela funciona melhor como sinal específico de proximidade semântica, não como juiz universal de qualidade.

Retomando o uso de referência já estabelecido, aqui ela precisa representar de forma fiel a resposta esperada. Se a referência for apenas uma lista simplificada de outputs ou exemplos parciais, a distância pode ficar baixa mesmo quando a resposta do modelo é útil. O problema não está necessariamente no prompt nem no evaluator isoladamente, mas no desalinhamento entre o que a métrica compara e o que o caso realmente considera correto. Embedding Distance depende fortemente da qualidade semântica da referência.

Um resultado como 0.11 sinaliza baixa proximidade entre a saída gerada e a referência usada no experimento. Esse número, sozinho, não prova que o prompt piorou nem que a resposta está errada para o caso de uso. Ele apenas mostra que, no espaço vetorial adotado, os dois textos ficaram distantes. A interpretação correta exige verificar se a referência era adequada e se proximidade semântica é mesmo a dimensão que interessa medir.

A implementação segue um fluxo direto: configurar o evaluator built-in de embedding distance, preparar prediction e reference, executar a avaliação e inspecionar o score retornado. No cenário de revisão de código, a saída gerada é comparada semanticamente com a referência do dataset para medir quão próxima ela está do esperado. O prefixo do experimento ajuda a identificar a execução no dashboard, mas o ponto central é que a comparação depende integralmente do par resposta-referência enviado ao evaluator. Se esse par estiver mal definido, o score será tecnicamente válido e analiticamente fraco.

Nem toda métrica serve para todo caso, e Embedding Distance é um exemplo claro disso. Se o dataset não contém algo próximo de uma resposta final esperada — por exemplo, se guarda apenas itens resumidos, pistas ou listas incompletas — a comparação semântica tende a gerar sinal pobre. Nessa situação, a métrica pode induzir conclusões erradas sobre a qualidade do prompt. A escolha da métrica deve partir do objetivo da avaliação e do tipo de evidência disponível no dataset.

A decisão de engenharia não é “qual métrica parece mais sofisticada”, mas “qual métrica mede o comportamento que importa neste problema”. Se o objetivo é proximidade semântica com uma resposta-alvo bem representada, Embedding Distance pode ser apropriada. Se o objetivo depende de correção operacional, aderência a rubrica, formato ou julgamento contextual, outras métricas tendem a produzir sinal mais confiável. Métrica adequada é a que combina com o objetivo e com o desenho da referência.

## Transcrição

00:01

Bom, pessoal, agora que a gente passou da metade aqui, né? A gente tá aqui, ó, Embedding Distance, tá? Esse aí é um outro camarada, que ele é extremamente importante, tá? Mas ele foca muito mais na parte semântica, tá? Por que eu tô dizendo isso? Porque ele é um critério, tá? Que, no final das contas, o que ele acaba fazendo?

00:24

ele utiliza uma forma de calcular a distância entre embeddings, ou seja, eu pego o dado que está vetorizado, pego outro dado vetorizado e faço ali ver o nível de similaridade. Nós temos, por exemplo, a similaridade do cosseno, que é mais utilizado, mas tem L2 que usa

00:50

a parte euclidiana, a gente tem bastante normas que a gente consegue trabalhar com esse tipo de coisa, tá? Então, nesse nosso caso aqui, se você vê, eu estou trabalhando com um cara built-in aqui para mim, tá? E ele não está usando o LLM em si, tá? Mas ele usa o embedding do OpenAI ali nesse nosso caso, tá? Então, esse aí é o ponto importante. Então, basicamente, o que acontece aqui é

01:19

eu coloco embedding distance, passo os dados como referência, porque eu preciso ter referência em relação a alguma coisa nesse nosso caso, vou executar, pedir para ele colocar aqui inclusive um prefixo para a gente saber, e agora ele vai pegar basicamente o resultado, vai comparar com a minha referência e vai ver o quão isso próximo está. Então, deixa eu rodar aqui, Python, basic, e aqui eu tenho

01:48

o nosso Embedding Distance Evolve aqui pra gente, tá? E enquanto ele tá rodando, apesar que esse aqui provavelmente é mais rápido, é só um evaluator aí nesse nosso caso, ele vai rodar mais rápido, então eu nem vou começar a falar de outro porque provavelmente a gente vai conseguir terminar esse cara nessa rodada sem esperar muito e sem ficar com o nosso vídeo

02:12

gigante mas o importante é que a gente entender é como que a gente tem critérios e ferramentas diferentes pra gente conseguir fazer a análise dos nossos prontos então ele já executou a nossa análise aqui já apareceu aqui ó embed distância então vamos rodar aqui e vamos ver onde esse cara tá e aqui o resultado dele foi 0.11 galera o negócio foi baixo mesmo aqui pra gente em

02:38

Ou seja, teve uma distância bem baixa aqui, e daí, provavelmente, se a gente for olhar fundo, a gente vai tentar entender o que aconteceu aqui, o porquê que essa distância está tão longe. Por outro lado,

02:54

Não significa necessariamente que isso pode ser um fator determinante para você melhorar ou mudar seu prompt. Depende muito no contexto que você está. Provavelmente, as referências que eu estou dando ou da forma como ele está gerando a resposta não é o suficiente. E muitas vezes, o porquê? Porque a resposta, a distância que ele vai ver, não é necessariamente

03:18

o feedback, o resultado, é apenas um nível de referência. Então, ele trabalhou aqui com o cosseno à distância, ele rodou, basicamente, e ele pegou o que ele tinha de exemplo antes e fez a verificação. Então, é o que é, galera. Agora, um ponto importante que você sempre tem que pensar é

03:41

Para rodar esses tipos de testes, você tem que garantir que realmente o seu dataset, o que você usa como referência, ele seja realmente não apenas um exemplo, uma listinha de exemplos como eu coloquei do outputs, mas realmente seja a resposta final da LLM para que sim, ali sim, conseguir mostrar mais coerência. Então, provavelmente por isso que ele não está deixando

04:04

isso aí é algo, vamos dizer assim, mais apurado, porque eu tenho uma listinha de exemplos e eu não tenho, na realidade, uma simulação de como seria a resposta como Ground Truth, por isso que provavelmente a gente está tendo esse descolamento, vamos dizer assim, da nossa realidade, fechou? Mas é mais um exemplo para você saber que você pode

04:26

Esse aí é um ponto importante, nem todos esses critérios, nem todas essas métricas são aplicáveis em todos os casos. Novamente, o importante é você saber o objetivo que você tem, baseado no seu objetivo, aí sim você vai escolher quais são as métricas que fazem mais sentido aí pra você. Beleza? Vamos nessa.

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (modelo de linguagem de grande porte)  
- **L2** — distância euclidiana  
- **OpenAI** — plataforma/modelos de IA da OpenAI  
- **Ground Truth** — verdade de referência, resposta correta esperada  
- **Evolve / evaluator** — avaliador

**Resumo**  
A aula apresentou a métrica **Embedding Distance** como uma forma de medir proximidade semântica entre a predição do modelo e uma referência, sem depender de julgamento textual de um LLM. O instrutor explicou que a comparação é feita convertendo ambos os textos em embeddings e calculando uma distância ou similaridade entre vetores, como **cosseno** ou **L2**, resultando em um score contínuo que indica quão próximos os textos estão no espaço vetorial.

Foi destacado que esse tipo de avaliador usa um modelo de embedding — no exemplo, da OpenAI — e não um LLM para “pensar” sobre a resposta. Isso torna a avaliação mais simples e rápida, mas também mais limitada, pois a métrica capta principalmente semântica e pode não refletir correção funcional, contexto da tarefa, rubrica ou formato esperado. Assim, Embedding Distance foi apresentada como um sinal específico de aderência semântica, e não como métrica universal de qualidade.

O fluxo mostrado foi direto: configurar o evaluator built-in de Embedding Distance, fornecer **prediction** e **reference**, executar a avaliação e analisar o score retornado. No exemplo prático, o resultado foi **0.11**, interpretado como baixa proximidade entre a saída gerada e a referência. O instrutor reforçou que esse número, isoladamente, não prova erro do prompt nem indica necessariamente piora; ele apenas mostra distância semântica no espaço vetorial adotado.

Também foi enfatizado que a qualidade da **reference** é decisiva. Se o dataset contém apenas exemplos parciais, listas resumidas ou pistas, a métrica pode gerar sinal fraco ou enganoso. Para funcionar bem, a referência precisa representar de forma fiel a resposta esperada, idealmente algo próximo de uma **Ground Truth**. Por isso, a escolha da métrica deve ser guiada pelo objetivo da avaliação e pelo tipo de evidência disponível no dataset, e não pela sofisticação aparente da técnica.

**Pontos de atenção**  
- **Embedding Distance mede semântica, não qualidade global**: não avalia adequação funcional, contexto ou cumprimento de rubrica com profundidade.  
- **A referência precisa ser bem construída**: se for parcial, resumida ou pouco fiel à resposta esperada, o score pode ficar baixo sem que a saída seja realmente ruim.  
- **Score baixo não significa automaticamente prompt ruim**: pode indicar apenas desalinhamento entre o que foi comparado e o que o caso de uso considera correto.  
- **A métrica depende fortemente do par prediction/reference**: se o par estiver mal definido, o resultado será tecnicamente válido, mas analiticamente fraco.  
- **Nem toda métrica serve para todo cenário**: a escolha deve partir do objetivo da avaliação e do tipo de dado disponível no dataset.  
- **Cosseno é comum, mas não é a única opção**: outras normas, como **L2**, também podem ser usadas conforme a necessidade.  
- **Use Embedding Distance quando a dimensão principal for proximidade semântica**: para correção operacional, formato ou julgamento contextual, outras métricas tendem a ser mais apropriadas.  
- **Evite concluir só pelo número**: é necessário inspecionar a referência, entender o contexto e validar se a distância semântica é mesmo o critério relevante.