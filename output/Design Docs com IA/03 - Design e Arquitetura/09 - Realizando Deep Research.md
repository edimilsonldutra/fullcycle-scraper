Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17060)

## Resumo da aula

Deep research é um modo de trabalho em que a IA não responde apenas com conhecimento imediato do modelo: ela navega por fontes, cruza informações e produz um documento longo de pesquisa. Isso importa quando a equipe precisa especificar uma feature sem depender apenas de memória, intuição ou conhecimento parcial do tema. No exemplo do rate limiter em Go, a pesquisa vira um insumo técnico para evitar que o detalhamento da feature seja escrito no escuro.

Um documento extenso de pesquisa não é o objetivo final; ele funciona como contexto reutilizável para gerar artefatos posteriores com mais qualidade. Quando a IA recebe esse insumo, ela tende a produzir drafts mais completos e menos genéricos para documentos de design. Retomando o cenário do rate limiting, a pesquisa ajuda a sustentar decisões sobre estratégias, bibliotecas, restrições e pontos de atenção antes de transformar isso em especificação.

Modelos diferentes se comportam de forma diferente ao gerar arquivos extensos. Em alguns casos, o Gemini produz documentos maiores e mais completos; em outros, o ChatGPT atende bem, e outras ferramentas como Claude também podem servir. A decisão prática não é ideológica: escolha o modelo que sustenta melhor volume, completude e consistência para o tipo de pesquisa que você precisa gerar.

O problema mais frequente não está na ferramenta, mas na formulação do pedido. Pedir “faça uma pesquisa sobre X” costuma gerar um resultado amplo demais, superficial ou desalinhado com o uso real do documento. Deep research precisa de contexto explícito sobre problema, ambiente, profundidade, tecnologias relevantes e resultado esperado.

Um fluxo mais robusto separa a pesquisa em duas fases. Na primeira, a IA conduz uma entrevista curta e monta um resumo preparatório; na segunda, a pesquisa longa é disparada com base nesse resumo já calibrado. Essa divisão melhora a qualidade do resultado porque a navegação longa parte de um briefing técnico mais preciso, em vez de um pedido genérico.

O resumo preparatório consolida os campos que realmente orientam a pesquisa: tema técnico, motivação, foco principal, contexto de uso, profundidade desejada, stack relevante, necessidade de exemplos reais e resultado esperado. Esse artefato reduz ambiguidade e força o autor a explicitar o que quer aprender. Quando a pesquisa começa sem esse alinhamento, a IA tende a gastar esforço em tópicos irrelevantes ou a deixar lacunas justamente nas decisões que mais importam.

A entrevista guiada, já usada antes para estruturar documentos, aqui aparece com outra função: preparar a pesquisa, não gerar o documento final. A IA faz uma pergunta por vez e usa as respostas naturalmente para compor o briefing. No exemplo, perguntas sobre motivação, contexto HTTP em microserviços, profundidade e uso de Redis refinam o escopo antes de iniciar a busca longa.

Depois que o resumo preparatório está pronto, o disparo da pesquisa pode ser simples: pedir que a IA realize a pesquisa com base naqueles aspectos. O ganho não está na sofisticação do comando final, mas na qualidade do contexto acumulado antes dele. Em termos operacionais, a etapa longa pode levar dezenas de minutos, então faz sentido tratá-la como um job de coleta e síntese, não como uma resposta instantânea.

Na fase de deep research, a IA nem sempre respeita bem um esqueleto rígido de saída. Por isso, é mais eficaz deixar a pesquisa sair em formato livre e só depois adaptar o conteúdo para um template próprio. Essa escolha separa duas preocupações diferentes: primeiro obter conhecimento amplo e útil; depois reorganizar esse conhecimento para consumo recorrente.

Uma pesquisa de 27 páginas pode ser excelente como base técnica e ainda assim ruim como insumo operacional para o restante do fluxo. A segunda etapa existe para converter esse conteúdo em uma estrutura mais compatível com os templates usados pelo time, inclusive para gerar feature design docs depois. O valor está em transformar pesquisa bruta em contexto estruturado, pronto para alimentar novos prompts e novos documentos.

## Transcrição

00:01

Bom, pessoal, olha só o que eu vou trazer e vou mostrar aqui pra vocês, tá? O negócio é o seguinte, tá? Se você olhar aqui, existe um PDF que eu tô te mostrando, que ele possui 27 páginas, e que provavelmente você viu que eu gerei ele com o chat GPT, tá? Esse PDF, se você perceber,

00:22

Ele é um PDF que traz muitos, mas muitos detalhes sobre como é que funcionam processos de Rate Limiting na linguagem Go. Então, é um documento realmente extenso, ele traz diversos tipos de estratégia, ele traz bibliotecas, ele mostra pontos importantes, pontos que você tem que levar em conta, ou seja, ele é um documento que

00:47

ele tenta equilibrar a parte técnica com a parte conceitual e esses tipos de coisa ali são importantes. Ou seja, é um baita documento aqui de pesquisa sobre você trabalhar ali com o Rate Limiting, porque realmente ele dá informação sobre o que você precisa saber sobre o assunto.

01:09

E lembra que eu falei agora há pouco para vocês que realmente é complexo você nem saber sobre o assunto e você ter que definir uma feature ou alguma coisa desse tipo? Então, em tese, se você vai gerar e vai definir uma feature e vai escrever isso tecnicamente, pelo menos você domina um pouco o assunto. Mas eu tenho que admitir para você que muitas vezes a gente não sabe do que a gente não sabe,

01:35

e ter um documento de pesquisa pra guiar a gente, vai ajudar pra caramba, tá?

01:40

Então, o que acontece nesse tipo de coisa? Eu costumo, e eu vou mostrar pra vocês aqui na prática, como que eu faço e como que eu trabalho. Porque, em cima disso, você vai perceber que eu consigo, inclusive, gerar aqueles outros documentos baseados nessas pesquisas que eu acabo fazendo. Então, por padrão, pessoal, mesmo que eu já domine um assunto,

02:05

eu sempre faço uma Deep Research ou faço uma busca no modo agente, e aí pode funcionar tanto no Chat GPT, funciona bem no Gemini... Eu vou ser bem honesto, inclusive, com vocês, nos últimos tempos eu tenho usado muito o Gemini para quando ele precisa gerar arquivos realmente muito grandes. Às vezes, o Chat GPT, pelo menos,

02:29

em alguns momentos, ele acaba não gerando o documento tão completo ou tão grande da forma como eu gostaria, tá? Mas, de forma geral, eu acredito que nós já temos muitas ferramentas de IA, inclusive Cloud e tudo mais, que vai poder te ajudar, tá?

02:44

O ponto importante aqui é que você entenda que isso aqui não é simplesmente um prompt que é colocado. Ele funciona como um recurso que normalmente as IAs têm, que é a parte de Deep Research, ou pesquisa profunda, onde ele sai, fica meia hora navegando na internet, juntando conteúdo e gera um documento para você.

03:05

Qual que é o grande problema do Deep Research? Existem alguns problemas. O primeiro ponto é você ter um prompt para pedir esse Deep Research. E aí somente ter esse tipo de prompt já faz muita diferença naquilo que você quer

03:22

a saber, aquele tipo de informação que você realmente precisa ter. Então, o primeiro erro que eu vejo que as pessoas acabam tendo em relação a trabalhar e tentar gerar esses documentos de pesquisa, que muitas vezes pode ser utilizado como contexto para IA também,

03:39

é não saber, perguntar e solicitar um Deep Research ali pra IA. Então, o que eu faço? Eu faço um processo de duas etapas, tá? É um prompt de duas etapas, eu vou mostrar pra vocês, vou fazer aqui na frente de vocês, de forma geral, mas ele é um prompt de duas etapas. E, obviamente, eu não vou ficar esperando meia hora, eu vou mostrar um que ele acabou sendo gerado, mas eu vou rodar esse prompt aqui pra você conseguir entender como é que esse cara funciona, tá?

04:09

Então, vamos lá. Somente para você saber, eu tenho um prompt que eu vou passar para você, que é um prompt para a geração de uma Deep Research, e eu chamei isso aqui de fase 1. Por quê? Porque quando você pede uma Deep Research, por mais que você peça um esqueleto de saída,

04:27

As yaas não aceitam esse esqueleto de saída, ela traz o dado do jeito que ela quiser. Então eu prefiro não passar um esqueleto de saída e pedir pra ela gerar da forma como ela acha que ela deve gerar, de forma geral, e depois eu tenho um segundo prompt que eu peço pra ela adaptar essa minha saída,

04:47

A saída que ela teve, baseado num template que eu gosto de utilizar, e daí você pode inclusive usar o seu próprio template. Então aqui, mesmo esquema, objetivo, prompt, entrevista de contexto, diretrizes, uma pergunta por vez, use as respostas naturalmente.

05:05

Aqui que é o grande ponto, tá? A estrutura esperada no resumo final, ou seja, o resumo preparatório para o Deep Research. O tema técnico, a motivação, o foco principal, o contexto do que vai ser utilizado, nível de profundidade, tecnologias e stacks relevantes, desejo incluir exemplos reais e o resultado esperado do que vai acontecer.

05:28

Então, depois disso, eu quero que a IA pergunte para mim, você deseja fazer um Deep Research agora? Então, é basicamente isso que acaba sendo o meu prompt aqui para vocês. Eu vou copiar e vou fazer no GPT aqui de forma geral aqui.

05:45

Vou copiar, eu poderia ter criado aquele MyGPT, os MyGPTs, ou o Gemini tem o Gems, então você poderia fazer de qualquer forma, eu vou trabalhar aqui da forma mais simples possível aqui pra gente conseguir colocar. Então, como eu tô colocando, colando aqui um prompt, aqui de forma geral, o que que eu vou fazer aqui? Normalmente eu coloco assim, ó.

06:09

execute o prompt abaixo só pra garantir que ele vai executar realmente aquilo que eu tô pedindo porque às vezes ele entende outra coisa tá então eu vou colocar e vou dar um enter aqui né vou pedir pra ele colocar aqui a parada

06:26

Então, em tese agora, ele vai trabalhar aqui. Vamos conversar brevemente para que eu entenda o que você queria pesquisar. No final, vou gerar um resumo com tudo o que será necessário para a sua ferramenta de A possa fazer um Deep Research. Então, qual é o tema técnico ou tecnologia? Eu vou colocar um Rate Limiter Angle. Vamos aguardar.

06:49

Ele está thinking, então vamos lá, só para alinhar, você quer que eu pesquise um rate limiting goal, confirma? Se sim, qual a principal motivação ou problema? Como que você quer resolver isso? Por exemplo, evitar sobrecarga, garantir fairness entre clientes, reduzir o custo de infraestrutura e padronizar? Eu vou colocar esses aqui, vou colocar esses. Só para facilitar a nossa vida aqui, galera. Aí ele vai pensar de novo.

07:19

E ele está pensando, provavelmente, por quê? Porque o prompt que eu coloquei faz ele pensar, tá? Como que você quer evitar essa sobrecarga, padronização? Seguindo o contexto, vai rodar num API HTTP microserviços, jobs assíncronos, eu vou colocar HTTP REST em microserviços. Vamos nessa.

07:47

Próxima pergunta é qual o nível de profundidade? Você deseja pesquisar sobre Rate, Limiting e Goal? Algum conceitual, mão na massa, exemplos do código? Eu vou colocar equilibrado, mas com muito conceito nas estratégias com exemplos didáticos. Agora, vamos aguardar novamente.

08:16

Então, perfeito, você quer um nível equilibrado, com bastante fundamento, para calibrar sua pesquisa. Quais tecnologias e stacks? Exemplos? Libs, etc. Reds. Eu vou colocar todos esses itens somente para seguir, tá, galera?

08:34

Porque, pessoal, mesmo que a gente vá fazer sempre um Deep Research, saber pedir para IA é importante. Então, a gente conseguir padronizar a forma de como a gente faz o Deep Research ajuda bastante. Última pergunta, qual o resultado esperado e se há requisitos críticos? Aqui, ele está trazendo respeitar metas, latências, descreva do jeito que você preferir. Todos esses.

08:58

e conseguir deixar o sistema flexível para outros storages e também outras estratégias de rate limiting. Aqui para mim. Vamos lá.

09:24

Então olha só que interessante pessoal, olha só, resumo preparatório, tema técnico, motivação, foco principal, contexto, nível de profundidade, tecnologias, desejo incluir sim, resultado esperado, base conceitual, desejo agora fazer a deep research agora. Então se você perceber, eu dei bastante contexto para ele, para que ele faça a minha deep research.

09:50

Perceba que eu não simplesmente pedi uma pesquisa. A Yaa me entrevistou, essa entrevista é bem simples, mas ela já deu bastante informação ali para eu conseguir pedir a pesquisa. E agora, baseado nisso aqui que eu faço, adiciono aqui Deep Research, por exemplo, eu coloco assim, realize a pesquisa baseado nesses aspectos.

10:14

E aí, pessoal, o que vai acontecer? Você confirma o Gostaria de Research, que vem o relatório estruturado, sessões e exemplos? Sim. Vou colocar ele sempre em pergunta. E agora, ele vai ficar ali fazendo a Deep Research e isso pode demorar algumas...

10:31

algumas boas meia hora pelo menos, tá? Então, o que eu vou fazer? Eu vou cortar o vídeo aqui, vou mostrar pra vocês um documento de Deep Research que ele gerou, tá? Baseado naquele PDF, porque eu gerei ele basicamente com o mesmo prompt, mas a gente tem a segunda fase dessa Research, que no final das contas é o quê? No final das contas...

10:54

a conseguir transformar essa research de 27 páginas numa estrutura que não necessariamente seja a que eu mais gosto, tá? Para uma estrutura que faça mais sentido eu utilizar ainda mais caso eu precise gerar mais documentos como aqueles features design docs e coisas desse tipo, tá? Então vamos nessa, vamos para a nossa parte 2 para que a gente consiga gerar esses documentos aí.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **Deep Research** — Pesquisa profunda
- **PDF** — Portable Document Format
- **GPT** — Generative Pre-trained Transformer
- **HTTP** — Hypertext Transfer Protocol
- **REST** — Representational State Transfer
- **API** — Application Programming Interface
- **Go** — Linguagem de programação Go
- **Redis** — Banco de dados em memória Redis
- **Claude** — Modelo/ferramenta de IA da Anthropic
- **Gemini** — Modelo/ferramenta de IA do Google
- **ChatGPT** — Assistente/modelo de IA da OpenAI

**Resumo**
A aula apresentou o conceito de deep research como um modo de trabalho em que a IA não responde apenas com conhecimento imediato, mas navega por fontes, cruza informações e produz um documento longo de pesquisa. O instrutor mostrou que esse tipo de pesquisa é especialmente útil quando a equipe precisa especificar uma feature técnica — como rate limiting em Go — sem depender apenas de memória ou conhecimento parcial do tema. Nesse cenário, a pesquisa funciona como um insumo técnico para sustentar decisões sobre estratégias, bibliotecas, restrições e pontos de atenção antes de transformar o assunto em uma especificação ou design doc.

Foi explicado que o objetivo da pesquisa longa não é ser o produto final, e sim servir como contexto reutilizável para gerar documentos posteriores com mais qualidade. A partir de um documento extenso, a IA tende a produzir drafts mais completos e menos genéricos para artefatos de design. O instrutor também comparou ferramentas e modelos, comentando que diferentes IAs se comportam de forma distinta ao gerar arquivos grandes: em alguns casos o Gemini produz resultados mais extensos, em outros o ChatGPT ou o Claude podem atender melhor. A escolha prática deve considerar volume, completude e consistência, não preferência ideológica.

Um ponto central da aula foi que o maior problema costuma estar na formulação do pedido, e não na ferramenta em si. Pedidos genéricos como “faça uma pesquisa sobre X” tendem a gerar respostas amplas, superficiais ou desalinhadas com o uso real do documento. Para evitar isso, o instrutor propôs um fluxo em duas fases: primeiro, uma entrevista curta com a IA para montar um resumo preparatório; depois, a execução da deep research com base nesse briefing já calibrado. Esse resumo reúne informações como tema técnico, motivação, foco principal, contexto de uso, profundidade desejada, stack relevante, necessidade de exemplos reais e resultado esperado.

Na prática, a entrevista guiada é usada para reduzir ambiguidades e orientar melhor a pesquisa. A IA faz uma pergunta por vez e vai consolidando as respostas em um briefing técnico mais preciso. No exemplo mostrado, foram refinados aspectos como a motivação para rate limiting, o contexto de uso em HTTP REST e microserviços, o nível de profundidade e o uso de Redis. Depois disso, o comando final para a pesquisa longa fica simples: pedir que a IA realize a deep research com base nesses aspectos.

Por fim, foi destacado que a deep research pode levar bastante tempo e deve ser tratada como um job de coleta e síntese, não como resposta instantânea. Também foi apontado que, durante a pesquisa longa, a IA nem sempre respeita bem um esqueleto rígido de saída; por isso, é mais eficaz deixar o conteúdo sair em formato livre e só depois adaptá-lo para um template próprio. Assim, a pesquisa bruta é convertida em uma estrutura mais compatível com os documentos e fluxos do time, inclusive para alimentar futuras gerações de feature design docs.

**Pontos de atenção**
- Não pedir “uma pesquisa sobre X” de forma genérica; é essencial fornecer contexto técnico e objetivo claro.
- O maior risco não é a ferramenta, mas um briefing mal formulado.
- A deep research pode gerar saídas longas, porém nem sempre alinhadas a um template rígido; é melhor adaptar depois.
- Separar o fluxo em duas etapas melhora a qualidade: entrevista/briefing primeiro, pesquisa longa depois.
- A entrevista deve capturar motivação, contexto, profundidade, stack, exemplos reais e resultado esperado.
- Tratar a deep research como um processo demorado, semelhante a um job de coleta e síntese.
- Escolher a ferramenta/modelo pelo que entrega melhor volume, completude e consistência para a necessidade.
- Usar a pesquisa como contexto reutilizável para gerar documentos posteriores, e não como fim em si mesma.
- Em temas técnicos complexos, não assumir que já se sabe tudo; a pesquisa ajuda a revelar lacunas e decisões importantes.
- Após obter a pesquisa bruta, reorganizar o conteúdo em um template próprio para facilitar o uso recorrente no time.