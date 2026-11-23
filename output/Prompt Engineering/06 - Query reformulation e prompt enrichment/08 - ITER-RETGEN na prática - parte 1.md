Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16752)

## Resumo da aula

Agora que entendemos a ideia básica, pedi para ele explicar sobre LangChain e LangGraph, com uma resposta simples do GPT. O que farei agora? Vou abrir outro arquivo e tentar explicar a ideia principal dele, executando-o. Ele ficou um pouco grande, mas consegue enriquecer as coisas em um fluxo bem interessante. Achei que ficou bacana como exemplo.

Preciso da sua atenção agora. Vamos nessa. Criei o chat, e você perceberá que tenho alguns prompts aqui. Se voltarmos ao diagrama, esses quatro elementos vão se comportar como quatro tipos de prompt.

Primeiro prompt (draft):

Tenho uma variável de input "question". Este prompt inicial gera um rascunho. Instruo que ele é um expert assistente com conhecimento inicial limitado, e que deve responder à pergunta, mas marcando pontos e detalhes específicos que estejam faltando. Uso [MISSING] como marcador para coisas como: versões específicas, datas de lançamento, especificações técnicas, parâmetros, performance, comparação de dados, implementação, casos de uso reais, limitações, roadmap, etc. Peço para ser detalhista, mas sem gerar mais de cinco missing markers para não ficarmos horas iterando. A resposta gerada aqui é um draft com lacunas.

Segundo prompt (geração de perguntas): Este prompt recebe o draft com os gaps e, para cada item faltante, formata como uma pergunta. Instruo para trazer os dados mais reais possíveis, com exemplos como "for missing version numbers, LangChain at 0.1.0". O objetivo é gerar queries para obter as informações faltantes.

Terceiro prompt (fill): Recebe a questão original, o draft atual (que pode ser de primeira ou segunda interação) e as informações coletadas. Instruo para substituir entre um e dois missing markers com informações concretas, usando as informações fornecidas. É importante não adicionar novos missing markers e substituir o texto [MISSING] por conteúdo real. Dou exemplos do que fazer e do que não fazer. A ideia é manter o progresso conforme preenchemos as lacunas. Ao final, deve escrever toda a resposta com os missing markers substituídos.

Quarto prompt (expansão): Adicionei este porque, muitas vezes, o modelo é muito inteligente. Ao fazer uma pergunta, todas as lacunas já eram respondidas de uma vez, e quase não havia interação. Quando isso acontece, peço para ele pegar o draft e buscar informações ainda mais específicas, gerando mais partes faltantes para enriquecer o documento com mais uma rodada.

Para o vídeo não ficar muito longo, vou parar aqui e continuo em seguida.

## Transcrição

00:01

Bom, pessoal, agora que a gente entendeu essa ideia básica, pedi para ele explicar sobre LengChain e LengGraph, com uma resposta simples aqui do GPT, o que eu vou fazer agora? Eu vou abrir um outro arquivo, mas eu vou tentar passar por esse arquivo explicando a ideia principal dele e executar, porque ele ficou meio grandinho, eu tenho que admitir,

00:29

mas ele consegue enriquecer as coisas num fluxo bem legal. Eu achei que ele ficou bacana pra dar como exemplo aqui pra gente, tá? Então, o lance é o seguinte, tá? Então, agora que eu preciso muito da sua atenção. Vamos nessa. Então, criei o chat, mas agora você vai perceber que eu tenho alguns prompts que eu criei aqui, tá? Se a gente voltar no Scalidraw,

00:55

você vai perceber que esses quatro caras aqui, eles vão basicamente se comportar como quatro tipos de prompt. Então, ele tem aqui uma variável de input question, e aqui eu tenho esse meu prompt inicial, que é o meu draft. Lembra que a gente gera um rascunho. E aqui eu estou falando que ele é um expert assistente, com conhecimento

01:20

inicial limitado, para ele responder a pergunta, mas ele tem que marcar...

01:28

muitos pontos e detalhes específicos que estejam faltando. Então, eu pedi use missing, três tracinhos, markers para o quê, por exemplo? Specific version, numbering, release dates, technical specification e parameters, performance, comparação de dados, implementação, casos de uso de real world, limitações,

01:54

roadmap e etc. Então, nesse caso aqui, se você perceber, eu estou pedindo para que, baseado na pergunta do cara, eu vou responder

02:08

Mas na hora que eu vou responder, eu vou ter que marcar coisas que podem estar faltando que eu não tenho total acesso ou que eu não sei até agora. Então é basicamente isso. Eu falei, seja thorough, ou seja, seja bem detalhista,

02:27

para no que especificar que realmente entendo o que é uma resposta completa. Não gere mais de cinco missing markers. Eu coloquei isso para a gente não ficar uma hora iterando, porque esse negócio pode ficar ali um bom tempo num loop até ele pegar uma resposta gigante, tá? E daí, eu tenho question, que entra no meu template, e a answer, que ele vai responder aqui com esse draft aqui para mim.

02:52

O outro cara que eu tenho aqui é um draft, mas esse draft, ele é para fazer o quê? As perguntas, tá?

03:03

referentes às partes que estão missing nessa primeira resposta. Deixa eu fechar isso aqui. Então, basicamente, ele está fazendo o seguinte, olha, você recebeu o seguinte draft com os seguintes gaps e eu peguei o draft que veio do prompt de cima. Daí eu falei, para cada item que está faltando, pegue essas informações como um gap e formate elas como

03:30

o nome do Missing que está faltando, o tópico, e trazer realmente real informação sobre isso. E daí eu coloco, tente trazer os dados mais reais possíveis. Daí eu dei um exemplo, for MissingVersion, numbers, LangChain, at the...

03:49

0.1.0 e trouxe aqui a informação. Aí, liste essas informações para cada gap, no máximo de cinco itens. Então, aqui, nesse momento, o que eu estou fazendo é pegando esses itens e gerando isso como uma query para a gente ter essas informações. Então, no final das contas, aqui eu estou gerando perguntas daquilo que está faltando.

04:12

Aí, nesse outro prompt que eu tenho, eu tenho um fill prompt. O que ele vai fazer? Ele vai pegar a minha questão original, ele vai pegar o meu draft, tá?

04:24

a iteração que eu estou ali no meu draft, porque eu posso ter primeira, segunda iteração, eu posso fazer o loop várias vezes, e aí eu coloco assim, olha só, informação para ajudar você a completar os gaps. E aqui tem a pergunta, que foi feita no prompt anterior, e a resposta.

04:45

E agora, o que eu estou colocando aqui? Você tem que, pelo menos, substituir entre um e dois Missing Markers com informações concretas. Você tem que substituir o texto Missing com conteúdo real e não mantém o Marker, porque senão vai ficar escrito Missing. Use a informação acima, que foi dada no conteúdo. Não adicione nenhum Missing Marker mais, porque, às vezes, ele poderia começar a criar outro Missing. E aqui eu dei alguns exemplos. Exemplos do que fazer.

05:14

a Missing está faltando a versão, mantém o Keep in the Marker. O jeito certo, o language chain, etc., substituindo o conteúdo. E daí eu falei que é importante entender a iteração, que ela vai manter o progresso conforme a gente vai filling the gaps, a gente vai resolvendo os buracos das perguntas que a gente não completou ainda. E depois, escreva

05:42

toda a resposta com os missing markers replaced. Então, basicamente, agora que você conseguiu pegar tudo isso, todas as informações que você já tem, substitua esse cara e gere o texto inteiro com o que foi substituído. Então, essa que é a ideia.

06:00

Um outro prompt que eu adicionei aqui, no caso, foi para expandir. Por quê? Porque, muitas vezes, o modelo é muito inteligente. Aconteceu isso várias vezes aqui. Então, eu fazia uma pergunta sobre LandGraph, sobre Go, e as perguntas...

06:17

que eram geradas como missing no primeiro prompt, todas elas já eram respondidas no segundo. Então, a gente quase não tinha interação, porque o modelo era muito bom para responder todas as perguntas. Então, quando a gente, numa tacada só, consegue resolver todas, o que eu peço? Eu peço para ele pegar o draft agora e buscar a informação ainda mais específica.

06:42

para ele gerar mais partes que estão missing, para ele fazer mais uma rodada e enriquecer mais o documento. Para o nosso vídeo não ficar muito grande, eu vou parar aqui e eu continuo em seguida.

## Resumo IA

**Abreviações**
- **GPT**: Generative Pre-trained Transformer.
- **LangChain**: framework para construção de aplicações com modelos de linguagem.
- **LangGraph**: biblioteca/framework para orquestração de fluxos e agentes com grafos.
- **Go**: linguagem de programação Go.

**Resumo**
A aula apresenta uma estratégia de refinamento iterativo de respostas usando múltiplos prompts em cadeia, aplicada em um fluxo com GPT para enriquecer um conteúdo sobre LangChain e LangGraph. O instrutor explica que criou um chat com quatro tipos principais de prompts, cada um com uma função específica no processo.

No primeiro prompt, chamado de **draft**, há uma variável de entrada `question` e a instrução para gerar um rascunho inicial como um assistente com conhecimento limitado. A resposta deve ser detalhada, mas deve marcar com **[MISSING]** os pontos que estejam faltando, como versões específicas, datas de lançamento, especificações técnicas, parâmetros, performance, comparações, implementação, casos de uso reais, limitações e roadmap. Também foi definido um limite de até cinco marcadores de ausência para evitar iterações excessivas.

No segundo prompt, o draft produzido anteriormente é transformado em perguntas. Cada lacuna identificada vira uma query específica, com foco em obter informações reais e concretas. O instrutor destaca que esse passo serve para converter os “gaps” em solicitações objetivas, facilitando a busca por dados faltantes.

No terceiro prompt, chamado de **fill**, o sistema recebe a pergunta original, o draft atual e as informações coletadas. A instrução é substituir um ou dois marcadores [MISSING] por conteúdo real, sem criar novos marcadores. O objetivo é manter o progresso entre iterações, preenchendo gradualmente as lacunas até completar a resposta final.

Por fim, o quarto prompt, de **expansão**, foi adicionado para os casos em que o modelo já responde tudo de uma vez e elimina a interação entre as etapas. Nesse cenário, o prompt força uma nova rodada de refinamento, pedindo informações ainda mais específicas para gerar novos pontos em falta e enriquecer o documento. O fluxo geral descrito é, portanto, um ciclo de rascunho, detecção de lacunas, geração de perguntas, preenchimento das respostas e expansão quando necessário.

**Pontos de atenção**
- Limitar o número de marcadores [MISSING] no rascunho evita loops longos e iterações intermináveis.
- As lacunas devem ser substituídas por conteúdo real, nunca mantidas como texto literal “Missing”.
- O prompt de preenchimento não deve criar novos [MISSING], para não interromper o progresso já alcançado.
- É importante usar perguntas e respostas bem específicas para que o preenchimento seja efetivamente útil.
- Quando o modelo responde tudo logo na primeira rodada, pode ser necessário usar um prompt de expansão para aprofundar o conteúdo.
- O fluxo depende de iteração controlada: gerar, perguntar, preencher e repetir somente quando ainda houver lacunas relevantes.