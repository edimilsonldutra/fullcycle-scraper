Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16573)

## Resumo da aula

Zero-shot é a técnica em que o modelo recebe apenas a tarefa, sem exemplos de entrada e saída. O ponto central não é o tamanho do prompt, mas a ausência de demonstrações do tipo “se entrar isso, responda aquilo”. Por isso, uma pergunta curta como “Qual é a capital do Brasil?” e uma instrução longa sem exemplos continuam sendo zero-shot. Essa técnica explora a capacidade base de generalização do modelo e costuma ser a forma mais frequente de uso em interações simples.

Zero-shot é adequado para tarefas diretas, como resumir um parágrafo, traduzir uma frase curta, responder uma pergunta factual ou gerar um esqueleto inicial de API. Ele também é útil em sistemas com alto volume de chamadas, porque tende a exigir menos tokens de entrada do que técnicas com exemplos. Essa economia importa quando a aplicação faz milhões de requisições e o custo acumulado do contexto vira restrição arquitetural. A simplicidade do prompt, nesse caso, não é só conveniência: é uma decisão de eficiência.

A técnica perde força quando a tarefa exige raciocínio mais elaborado, maior precisão procedural ou forte padronização de resposta. Sem exemplos, o modelo tem mais liberdade para escolher estrutura, vocabulário e nível de detalhe, o que reduz controle sobre o formato de saída. Pequenas mudanças no wording do prompt também podem alterar bastante o resultado, especialmente em modelos mais sensíveis. Além disso, zero-shot não elimina alucinação; ele apenas reduz a complexidade da instrução.

Retomando a estrutura de mensagens já usada antes, o comportamento aqui depende mais da instrução explícita do que de exemplos. Se o prompt for apenas “Qual é a capital do Brasil?”, o modelo pode responder só “Brasília” ou produzir uma frase completa, como “A capital do Brasil é Brasília”. Quando a instrução inclui uma restrição como “responda apenas com o nome da cidade”, o formato tende a ficar mais controlado, mas ainda sem a rigidez de um few-shot ou de um esquema formal. Em zero-shot, pedir formato ajuda, mas não substitui demonstração quando a saída precisa ser altamente estável.

Detecção de intenção consiste em inferir o objetivo implícito do usuário a partir do texto enviado. Um prompt como “Descubra a intenção do usuário do seguinte texto” seguido de “Estou procurando um restaurante perto de São Paulo que tenha uma boa classificação para comida japonesa” já permite ao modelo extrair algo como busca por restaurante japonês bem avaliado na região de São Paulo. Isso é útil em aplicações que precisam decidir filtros, rotas ou consultas antes de responder. Em fluxos com RAG, por exemplo, a intenção pode orientar quais dados recuperar e como restringir a busca.

Três prompts ilustram bem o comportamento do zero-shot: uma pergunta factual, uma tarefa de detecção de intenção e uma pergunta factual com restrição de formato. O primeiro mede resposta direta; o segundo mostra inferência sem exemplos; o terceiro testa quanto uma instrução curta já consegue moldar a saída. Essa comparação é valiosa porque isola a técnica e permite observar o efeito do modelo sem adicionar outras variáveis. O experimento continua simples, mas já revela diferenças de aderência, estilo e custo.

Retomando a comparação prática entre modelos, o mesmo conjunto de prompts pode ser executado em um modelo mais antigo, como GPT-3.5 Turbo, e depois em um modelo mais recente, como GPT-4 ou GPT-5 nano. No GPT-3.5 Turbo, a resposta para “Qual é a capital do Brasil?” tende a ser mínima, como “Brasília”; no GPT-4, a mesma pergunta pode virar uma frase completa. A tarefa de intenção também muda de redação entre modelos, mesmo preservando o sentido geral. Isso mostra que zero-shot não é apenas “perguntar e receber”: o modelo escolhido altera concisão, estilo e quantidade de tokens consumidos.

Alguns modelos usam reasoning interno mesmo em prompts extremamente simples. Nesses casos, a resposta visível pode ser curta, mas o consumo de tokens cresce porque o modelo gera etapas intermediárias de raciocínio que não aparecem integralmente para o usuário. Foi isso que ocorreu ao comparar uma resposta como “Brasília” com custos muito diferentes entre modelos: um respondeu de forma direta, enquanto outro consumiu mais de uma centena de tokens para entregar praticamente a mesma saída. Em produção, esse comportamento muda custo e latência de forma relevante, mesmo quando o prompt parece barato.

A análise correta não é apenas “qual modelo respondeu certo”, porque todos podem acertar uma pergunta simples. O que importa é observar aderência ao formato pedido, variação de estilo, tempo de resposta e custo total de tokens. Um modelo com reasoning pode parecer mais sofisticado, mas ser economicamente inadequado para tarefas triviais e massivas. A escolha do modelo, portanto, precisa considerar a complexidade real da tarefa, e não apenas a capacidade máxima do sistema.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente viu um pouquinho de código em relação a essa parte de role prompt, mas agora a gente vai começar com categorias que são muito mais fortes e utilizadas no dia a dia. E um dos prompts que eu acredito, se eu tivesse que dar um chute, que é mais utilizado no mundo, eu acho que é esse de zero shot. O que significa? É uma técnica em que o modelo recebe apenas a instrução da tarefa,

00:29

Sem nenhum exemplo. O objetivo é realmente testar a generalização e a capacidade base que o modelo tem. Então, quando que eu uso um zero-shot da vida? Resuma um parágrafo de um artigo para mim. Qual é a capital daquele país? Gere rapidamente o esqueleto de uma API. Traduza uma frase curta. Explicar o que é uma arquitetura orientada a eventos. Um sistema de alta escala que precisa de economia de tokens. Então, por exemplo,

00:58

Às vezes, eu tenho um sistema que vai ter milhões de chamadas para um LLM, né? E a gente sabe que token custa muito caro. Então, o que acontece? Quanto menos você escrever, é melhor. E, muitas vezes, o zero-shot te ajuda porque, mesmo você sem escrever muito, sem dar exemplos de como a IA deve responder, ele ainda assim consegue trabalhar. Então, eu acredito que quantas vezes você já não foi, sei lá, no GPT e perguntou, o que é isso?

01:24

Ponto. Isso é um zero shot, de cara. Mas a principal característica do zero shot é que você não dá exemplos pra ela. Às vezes você pode escrever, tá? Duas páginas perguntando algo pra IA.

01:40

Se você não der um exemplo, isso ainda pode ser considerado zero-shot. Então, zero-shot é muito mais em mostrar em de para. Se for assim, faz assim. Em relação principalmente à exemplificação. Mas, novamente, é muito comum a gente usar zero-shot quando nós temos, no final das contas, prompts menores. Quais são as limitações de zero-shot, galera?

02:05

Pode falhar em problema complexo, você não vai pedir uma pergunta extremamente complexa sem dar exemplo, sem nada. Você tem pouco controle no formato de saída, porque você perguntou e ela vai responder do jeito que ela quiser, da forma como ela quiser, de acordo com a temperatura que você setou.

02:21

Pode gerar alucinação, ou seja, a IA escrever coisa que ela não tem ideia e ela inventa a informação. A saída varia com pequenas mudanças no prompt, ou seja, às vezes eu mudo uma pequena palavra ou alguma coisa ali e a saída muda muito o resultado. E qualquer coisa que você precisa de raciocínio lógico mais elaborado, zero shot não é para isso, porque simplesmente é perguntar e responder.

02:46

deixa eu mostrar já aqui para você um exemplo da gente trabalhando aqui com zero shot então vamos lá deixa eu pegar aqui meus arquivos eu tenho um exemplo aqui de zero shot que eu quero mostrar para você para ficar mais fácil para gente olhar aqui tá então zero shot eu acho que não tem muita

03:06

muita diferença, mas você vai perceber que o modelo que você chama, usando o zero-shot, a coisa muda também. Então, o que acontece é o seguinte, eu tenho uma mensagem, qual que é a capital do Brasil, beleza? Então, essa é a minha primeira mensagem, se você perceber, é um zero-shot, tá? Simplesmente estou fazendo uma pergunta clara, não estou dando exemplo e nada disso. Aí, eu tenho um outro exemplo aqui de zero-shot, olha só.

03:32

descubra a intenção do seguinte texto, a intenção do usuário do seguinte texto. Por que isso é importante, galera? Muitas vezes a gente tem alguma arquitetura no sistema que vai trabalhar com LLM, por exemplo, um RAG, Retrieval Augmented Generation, onde

03:49

Quando o usuário faz uma pergunta, a gente tenta entender a intenção do usuário por trás, para saber, inclusive, quais filtros você vai usar para filtrar no banco de dados de acordo com a intenção. Então, essa história de intent, ela está muito ligada a deep learning, coisas desse tipo, ou seja, você entender o que está por trás da pergunta. Então, o que está dizendo esse segundo exemplo aqui? Busque a intenção do usuário do seguinte texto.

04:13

Eu estou procurando para um restaurante perto de São Paulo que tenha uma boa classificação para comida japonesa. E eu tenho um outro exemplo aqui. Qual é a capital do Brasil? Responda apenas com o nome da cidade.

04:29

basicamente é isso que eu tô colocando então o que que acontece o seguinte se você perceber olha só que interessante eu coloquei aqui o modelo gpt5 nano tá e eu pedi para ele responder essas três perguntas aqui tá antes de eu botar esse modelo o gpt5 nano eu vou mudar esse cara

04:52

para o 3.5 Turbo que ele tem. Não sei se quando você for ver esse vídeo exista ainda o Turbo, se eles estiverem dando suporte ou não. Se não tiver, você vai para o GPT-4 e assim vai. Mas o ponto importante aqui é que o modelo Turbo é um modelo bem antigo e ele é um modelo que não tem a linha de raciocínio automática ou qualquer coisa desse tipo. E ele

05:18

De forma geral, a performance dele é rápida, mas os nossos modelos também são rápidos. Então, a questão não é muito a performance aí. Mas o grande ponto é a maneira de raciocínio. Então, vamos ver como é que ele trabalha com essas três chamadas aqui pra gente. Então, eu vou colocar Python, vou colocar um barra aqui.

05:34

zero shot. Então, vou dar um enter aqui, deixa ele trabalhar com essas três possibilidades aqui pra gente. E prontinho, foi rapidão. Então, olha só, galera. Olha a quantidade de tokens que ele gastou aqui em cada requisição. Então, primeira requisição aqui é qual é a capital do Brasil? Ele respondeu aqui pra mim, Brasília, tá? E input token entrada, token de saída 3 e o total de tokens ali. Aqui,

05:59

O meu prompt foi, busque a intenção do usuário do seguinte texto, estou procurando por um restaurante em São Paulo que tem um good rating. Então, ele respondeu para mim, user intent, intenção do usuário, está buscando por recomendações de restaurante em São Paulo com good ratings de comida japonesa. Ou seja, ele respondeu quase que com a pergunta

06:22

com a pergunta que foi colocada, mas ele entendeu essa intenção. Mas perceba, eu não dei formato, eu não falei como ele tem que responder, nada disso.

06:34

E aqui, o prompt que ele trouxe, qual a capital do Brasil, responda com o nome da cidade, ele trouxe Brasília também. Vou reexecutar, porque conforme a gente vai reexecutando prompts, às vezes as respostas são diferentes. E eu quero mostrar algumas coisas aqui para você. Aqui. Capital do Brasil, Brasília. Galera, só para vocês saberem, eu vou mudar agora de modelo. Eu vou colocar aqui o GPT-4.

07:01

e vou executar novamente. E a gente vai conseguir ver um pouquinho de diferença para ver como que se muda um pouco as respostas, como que elas podem ser mudadas. Opa, eu já rodei? Foi rápido assim? Vamos lá. Então, vamos lá. Aqui, ó. Qual é a capital do Brasil? A resposta dele. A capital do Brasil é Brasília. Perceba que ele utilizou mais tokens agora

07:30

porque ele deu uma resposta mais completa, ele não escreveu apenas Brasília. Se você perceber, o GPT 3.5 Turbo, ele respondeu apenas Brasília. E aqui, a busca de comida japonesa, ele falou de uma forma um pouco mais fancy, a intenção do usuário no texto é buscar um highly rated Japanese restaurant em São Paulo.

07:55

E aqui embaixo, responde apenas com o nome da cidade. E aqui ele respondeu apenas Brasília. Então, se você perceber, tudo isso é zero shot. E tudo isso muda conforme você muda o modelo. E aqui eu vou dar para você pasmar um pouco. Olha a quantidade de tokens que a gente tem utilizado aqui. 19 tokens, 53 tokens. A gente está usando 21 tokens aqui. Agora, o que eu vou fazer? Eu vou mudar aqui para a gente, para o GPT-5.

08:24

Nano, não vou nem usar Mini, tá? Vou colocar aqui e vou executar. A primeira coisa que você vai perceber é a demora na resposta. Tá? Então, a primeira coisa que você vai perceber aí nesse caso são demoras um pouco mais na resposta. E o segundo ponto que você vai perceber é a quantidade de tokens. Então, a primeira resposta ele respondeu Brasília, tá? Olha a quantidade de tokens que ele utilizou de saída

08:51

para responder apenas Brasília e ponto no final. Perceba que tem ponto, tá? Ele utilizou 151 tokens. Se a gente comparar com os exemplos anteriores, gastou muito menos, tá? E o output token normalmente é o mais caro.

09:05

Agora, qual que é a intenção do usuário? Ele respondeu e deu um botão entre parênteses, location-based restaurant search with Japanese cuisine preference aqui, a intenção. E se você olhar, olha a quantidade total de tokens que ele trabalhou.

09:22

Aqui também, responda com uma única cidade, apenas com nome, Brasília, e aqui 157 tokens. Por que ele gastou muito mais tokens, dependendo da situação, do que os outros modelos? Se eu colocar novamente aqui o GPT 3.5, 3.5 Turbo, compare a primeira resposta aqui, 151 tokens,

09:52

com a primeira resposta que ele deu, 16 tokens. Por que isso aconteceu? Troquei o modelo GPT-5 nano, ele usa reasoning, ou seja, ele fica gerando uma linha de raciocínio, a gente vai falar sobre linha de raciocínio e tipos de prompt para isso, e cada vez que ele vai gerando essas linhas de raciocínio, ele vai cuspindo token, mesmo que ele não mostre o resultado para você final.

10:16

Mas daí, você tem o resultado ali com uma palavra, mas ele torrou os seus tokens ali por baixo dos panos. E por isso que entender o tipo de modelo é importante e como você pode ver a mudança drástica da qualidade ou tipo de resposta baseado no modelo que a gente colocou. Então, somente para você ter um pouco mais de clareza como que o Zero Shot funciona. Mas, ao mesmo tempo, acabei falando de outros assuntos

10:43

em relação a modelos que eu não vou precisar ficar repetindo muito nos próximos vídeos também. Fechou? Então, a gente acabou de ver zero shot.

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model*; modelo de linguagem de grande porte.
- **RAG** — *Retrieval Augmented Generation*; geração aumentada por recuperação.

**Resumo**
A aula apresentou a técnica de **zero-shot**, explicando que ela consiste em enviar ao modelo apenas a instrução da tarefa, sem exemplos de entrada e saída. O instrutor destacou que o ponto central não é o tamanho do prompt, mas a ausência de demonstrações do tipo “se entrar isso, responda aquilo”. Por isso, até uma pergunta curta como “Qual é a capital do Brasil?” continua sendo zero-shot, assim como instruções mais longas, desde que não haja exemplos.

Foram citados usos comuns da técnica em tarefas diretas, como resumir textos, traduzir frases curtas, responder perguntas factuais, gerar um esqueleto inicial de API e até inferir intenção do usuário. A aula também relacionou zero-shot com cenários de alta escala, em que a economia de tokens é relevante para reduzir custo em sistemas com muitas chamadas a LLMs. Nesse contexto, a simplicidade do prompt é tratada como uma decisão arquitetural e não apenas como conveniência.

Na sequência, o instrutor explicou as limitações do zero-shot: menor controle sobre o formato de saída, maior sensibilidade a pequenas mudanças no wording do prompt, possibilidade de alucinação e baixa adequação para problemas complexos ou que exigem raciocínio mais elaborado. Foi mostrado que, mesmo com uma instrução curta, o modelo pode responder de formas diferentes, como retornar apenas “Brasília” ou elaborar uma frase completa, dependendo do modelo e da formulação.

A aula então comparou diferentes modelos executando os mesmos prompts em zero-shot, como perguntas factuais, detecção de intenção e restrições de formato. A comparação entre modelos mais antigos e modelos mais novos mostrou que a escolha do modelo impacta o estilo, a concisão, a aderência ao pedido e o consumo de tokens. O instrutor demonstrou que alguns modelos com *reasoning* interno podem gastar muito mais tokens para entregar uma resposta simples, o que afeta custo e latência.

Por fim, foi reforçado que a análise correta não deve se limitar a “acertou ou errou”, mas incluir aderência ao formato, variação de estilo, tempo de resposta e custo total. A conclusão prática é que zero-shot funciona muito bem para tarefas simples e diretas, mas a escolha do modelo e a natureza da tarefa determinam se a técnica é realmente eficiente em produção.

**Pontos de atenção**
- Zero-shot **não depende do tamanho do prompt**, e sim da **ausência de exemplos**.
- É adequado para tarefas simples e diretas, mas **não é ideal para problemas complexos** ou com alta exigência de precisão procedural.
- Há **pouco controle sobre o formato de saída**; pedir uma restrição ajuda, mas não substitui exemplos quando a estabilidade é importante.
- O modelo pode **alucinar**, mesmo em zero-shot.
- **Pequenas mudanças no prompt** podem gerar respostas bem diferentes.
- A escolha do **modelo** impacta diretamente estilo, concisão, aderência e custo.
- Modelos com **reasoning interno** podem consumir muitos tokens mesmo quando a resposta visível é curta.
- Em produção, é importante considerar **custo de tokens e latência**, especialmente em sistemas de alto volume.
- Para tarefas em que a saída precisa ser altamente estável, **few-shot ou outros esquemas mais estruturados** tendem a ser mais apropriados.
- Em fluxos com **RAG**, a detecção de intenção pode ser útil para orientar filtros e recuperação, mas deve ser tratada com cuidado para não enviesar a busca.