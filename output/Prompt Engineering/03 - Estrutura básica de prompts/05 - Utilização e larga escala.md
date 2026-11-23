Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16614)

## Resumo da aula

A mesma estrutura de prompt não serve igualmente para todos os cenários operacionais. Em uso pontual, como desenvolvimento de software ou exploração de um problema, o objetivo é maximizar entendimento e qualidade da resposta, mesmo com contexto amplo. Retomando a ideia já estabelecida de não economizar tokens em desenvolvimento, a restrição principal continua sendo não estourar a janela de contexto, e não reduzir o prompt a qualquer custo. O critério muda quando a interação deixa de ser ocasional e passa a ser multiplicada por volume.

Processos de exploração são aqueles em que o usuário ainda está descobrindo o problema, o espaço de solução ou até o que precisa perguntar. Nesses casos, faz sentido fornecer mais contexto e permitir que a IA pesquise no código-fonte e na internet para produzir algo mais contextualizado, como documentação ou entendimento técnico. Esse tipo de tarefa tolera prompts mais pesados porque não costuma rodar milhares de vezes em paralelo. O custo adicional existe, mas não domina a decisão quando a execução é esporádica.

Quando uma aplicação baseada em IA vai para produção em larga escala, economia de tokens deixa de ser otimização e vira requisito de viabilidade. Cada token de entrada e de saída é multiplicado pelo volume de chamadas, então um excesso pequeno por requisição pode se transformar em um custo mensal grande o suficiente para inviabilizar o produto. A decisão sobre o tamanho do prompt passa a ser arquitetural e financeira, não apenas técnica. Um prompt excelente em uso humano pontual pode ser economicamente ruim quando executado milhares ou milhões de vezes.

Prompts longos e instruções que exigem mais processamento, como pedir para pensar passo a passo ou revisar etapas anteriores, tendem a aumentar a latência. Em produção, isso afeta tempo de resposta percebido pelo usuário, throughput do sistema e até a necessidade de mais infraestrutura ao redor da aplicação. O problema não é apenas esperar alguns segundos a mais; é acumular atraso em cada chamada de um fluxo repetido em escala. Por isso, sofisticação de prompt precisa ser tratada como custo operacional de tempo, e não só de tokens.

Em ferramentas pagas por assinatura, o custo marginal de uma interação pode parecer invisível para o usuário. Com API key, a cobrança por milhão de tokens de entrada e saída torna explícito quanto cada requisição consome, o que força uma disciplina maior no desenho do prompt. Nesse contexto, reduzir verbosidade, instruções redundantes e contexto desnecessário passa a ser parte do design do sistema. O prompt deixa de ser apenas uma instrução e vira também uma unidade de custo.

A decisão correta raramente maximiza tudo ao mesmo tempo. Em escala, o objetivo costuma ser encontrar o ponto em que a qualidade é suficiente para o caso de uso sem empurrar custo e latência para níveis desproporcionais. A pergunta relevante não é se um prompt maior produz uma resposta um pouco melhor, mas se essa melhora justifica o impacto financeiro e operacional quando multiplicada pelo volume. Um ganho marginal de assertividade pode não compensar milhares de dólares extras por mês.

Retomando o raciocínio de trade-offs já conhecido, custo, latência e qualidade precisam ser avaliados como variáveis de produto. Se a resposta chega devagar demais, custa caro demais ou melhora pouco em relação à alternativa mais enxuta, o problema não é apenas técnico: o caso de uso pode deixar de fazer sentido economicamente. Projetar prompts para produção exige pensar em sustentabilidade do serviço, experiência do usuário e margem de operação. Escalar IA não é só fazer funcionar; é fazer funcionar de modo viável.

## Transcrição

00:01

Bom pessoal, no vídeo anterior ele ficou até meio grandinho, mas eu precisava passar esse posicionamento que pelo menos é meu, tá? Então, pra resumir, se eu tenho

00:13

estou desenvolvendo software, eu não vou economizar com tokens. Eu não estou preocupado com isso. Se eu ficar me limitando a isso, eu estou enrolado. O que eu vou sempre fazer é tentar fazer com que o meu chat, a minha comunicação com o IA, ela não ultrapasse a janela de tokens. Se ela ultrapassar, eu vou criar um novo chat para ela não perder contexto, informação e tudo mais, tá? Agora,

00:36

O grande ponto aqui é casos importantes. Quando o problema não será respondido pela IA em larga escala, você também não vai economizar tokens, porque você vai pegar a melhor informação

00:53

Precisa. Um exemplo é o processo de desenvolvimento, que eu falei bastante, mas também processos de exploração. O que significa processos de exploração? Muitas vezes você não sabe o que você não sabe e que você quer entender mais sobre esse assunto.

01:09

Outra coisa, às vezes, vale a pena você fazer com que a IA faça pesquisas baseadas no seu código-fonte na internet para gerar uma documentação mais contextualizada daquilo que você precisa. Então, você vai explorar. Então, todas as vezes que você tiver que criar tarefas pontuais

01:30

e que elas não vão rodar em larga escala, afinal de contas, você não vai rodar mil pesquisas simultaneamente com janela de tokens gigante para ela gerar mil documentos simultaneamente, porque isso, no final do dia, não vai se aplicar ali no seu dia a dia de desenvolvimento, por exemplo, isso aí não tem problema nenhum você também trabalhar com um grande contexto em relação à parte de token. Agora,

01:56

O ponto é o seguinte, quando há ou pretende-se escalar uma aplicação, economize ao máximo, tá? Então, isso aqui é o ponto importante, economize ao máximo, porque aí cada token vale, cada token é você realmente inviabilizar, às vezes, um projeto de A na empresa que você está trabalhando.

02:21

Então, obviamente, a gente já falou disso, mas mais token, mais custo. Mais regras de negócio ou cadeias de pensamento, maior a latência. Então, dependendo do token, dependendo do prompt que eu fizer para a IA, e eu pedir, por exemplo, para ela pensar passo a passo, ou ela rever etapas anteriores e tudo mais, ela vai depender mais, ela vai demorar mais para responder. Então, se eu tenho um custo maior

02:50

pela utilização de tokens. E se o prompt que eu uso vai fazer com que a gente gere mais latência, porque gera, isso aí acaba sendo inviável. E por que eu estou dizendo mais token, mais custos? Porque nesse caso aqui, eu não estou pagando um plano mensal do cloud, sei lá, de 100 dólares, 50 dólares, de 30 dólares. Aqui eu estou pagando, o custo aqui é custo por token.

03:20

Tá?

03:21

E quando eu digo custo por token, é custo por um milhão de token, token de entrada, token de saída, esse tipo de coisa. Mas o ponto aqui, aqui eu estou usando a API key. E se eu estou usando a API key, a parada aqui é cara, tá? Então, aqui eu vou usar a API key aqui para mim. Então, a gente tem que tomar cuidado com isso. E os trade-offs são sempre aquela história. Custo, latência e qualidade do resultado. Será que vale a pena, eu com 90% de assertividade,

03:51

pagar mil dólares a mais por mês para eu ter 91% de assertividade. A gente já falou sobre isso, tá? Então, seguinte, pessoal, algumas guidelines que eu queria passar para você, e eu vou falar isso no próximo vídeo, porque eu estou dizendo que são guidelines, mas não estou dizendo que é uma regra escrita em pedra. Então, vamos falar sobre isso.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **API** — Interface de Programação de Aplicações
- **API key** — Chave de acesso para uso da API
- **tokens** — Unidades de texto processadas pelo modelo, usadas para entrada e saída

**Resumo**
A aula explicou que a estrutura de prompt ideal depende do cenário de uso. Em tarefas pontuais, como desenvolvimento de software ou exploração de um problema, o foco deve ser maximizar a qualidade da resposta e o entendimento do contexto, sem se preocupar excessivamente com economia de tokens, desde que a janela de contexto não seja ultrapassada. Nesses casos, é aceitável usar prompts mais longos, pesquisar no código-fonte e até consultar a internet para gerar documentação ou respostas mais contextualizadas, porque a execução é esporádica e não ocorre em grande escala.

O instrutor destacou que, quando uma aplicação com IA vai para produção e passa a ser executada em volume, a economia de tokens deixa de ser apenas uma otimização e passa a ser um requisito arquitetural e financeiro. Cada token de entrada e saída multiplicado por milhares ou milhões de chamadas pode inviabilizar o produto. Além disso, prompts mais complexos, com instruções como pensar passo a passo ou revisar etapas anteriores, tendem a aumentar a latência, o que afeta a experiência do usuário, o throughput e os custos de infraestrutura.

Também foi ressaltado que o tipo de cobrança influencia o design do prompt: em modelos com custo por API key e cobrança por token, a disciplina para reduzir verbosidade, redundâncias e contexto desnecessário se torna ainda mais importante. O fluxo recomendado é avaliar constantemente o trade-off entre custo, latência e qualidade, buscando um ponto em que a resposta seja suficiente para o caso de uso sem gerar despesas e atrasos desproporcionais. Em resumo, a aula reforçou que escalar IA não é apenas fazê-la funcionar, mas fazê-la operar de forma viável e sustentável.

**Pontos de atenção**
- Não economizar tokens em tarefas pontuais de desenvolvimento ou exploração, desde que isso não ultrapasse a janela de contexto.
- Se o chat ficar grande demais, criar um novo chat para não perder contexto e evitar estouro da janela de tokens.
- Em processos de exploração, faz sentido fornecer bastante contexto e permitir pesquisas no código-fonte e na internet.
- Em aplicações que vão escalar, reduzir tokens é essencial para evitar custos mensais elevados e possível inviabilização do projeto.
- Prompt mais longo e com instruções mais complexas tende a aumentar a latência.
- “Pensar passo a passo” e revisar etapas anteriores pode piorar tempo de resposta e custo operacional.
- Em cobrança por token via API key, cada token de entrada e saída impacta diretamente o custo.
- Avaliar sempre o trade-off entre custo, latência e qualidade, sem buscar maximizar tudo ao mesmo tempo.
- Um ganho pequeno de qualidade pode não justificar um aumento grande de custo em escala.
- Projetar prompts para produção exige olhar para viabilidade econômica, experiência do usuário e sustentabilidade do sistema.