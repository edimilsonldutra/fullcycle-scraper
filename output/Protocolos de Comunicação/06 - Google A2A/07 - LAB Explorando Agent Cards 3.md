Módulo: Protocolos de Comunicação\
Aula: [LAB: Explorando Agent Cards 3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18619)

## Resumo da aula

Retomando o cenário de descoberta automática já validado, o orquestrador só consegue coordenar agentes porque primeiro enxerga quem está disponível e quais skills cada um publicou. Aqui, o ponto novo não é a descoberta em si, mas o uso operacional desse catálogo para decidir a execução. Quando o ambiente retorna dois especialistas — logística e estoque — o orquestrador passa a ter base concreta para decompor uma solicitação composta. Se uma skill não estiver publicada corretamente, a capacidade existe no servidor, mas continua invisível para o roteamento.

Uma pergunta como “qual é o status do pedido 123 e o estoque do SKU-TEC01?” mistura duas intenções de negócio diferentes no mesmo prompt. O orquestrador precisa separar a parte ligada ao pedido da parte ligada ao SKU e mapear cada trecho para o agente especializado correspondente. Essa decomposição evita enviar contexto irrelevante para um único agente e preserva a responsabilidade de cada serviço. O resultado é uma coordenação horizontal: cada agente resolve apenas o que seu contrato indica que sabe fazer.

O agente de estoque entra no fluxo como um especialista de domínio, não como um detalhe secundário do exemplo. Sua função é responder consultas de disponibilidade a partir da skill de verificação de estoque descoberta no Agent Card. Isso importa porque o orquestrador não decide com base em nomes arbitrários de serviço, mas na capacidade publicada e consumível. Quando a consulta contém um SKU, esse sinal semântico é suficiente para justificar o encaminhamento ao agente de estoque.

Observar o fluxo por baixo do capô significa inspecionar a sequência real de decisões e chamadas que o orquestrador executa depois de receber o prompt. Primeiro ele reconhece que a solicitação é composta; depois emite uma resposta intermediária informando que vai consultar pedido e estoque; em seguida chama os agentes adequados e coleta as respostas individuais. Essa visibilidade é valiosa para debugging porque mostra se o erro está na descoberta, no roteamento ou na execução do especialista. Sem essa inspeção, uma resposta final incorreta parece um problema único, quando na verdade pode ser uma falha em qualquer etapa da coordenação.

O agente logístico retorna o resultado de rastrear-pedido, enquanto o agente de estoque devolve a resposta de verificar-estoque. O orquestrador recebe essas saídas separadamente e produz uma resposta consolidada para o usuário, mantendo a interface simples mesmo com múltiplas chamadas internas. Essa consolidação é a camada que transforma composição distribuída em experiência unificada. O usuário faz uma pergunta só, mas o sistema executa um pequeno plano multiagente para respondê-la.

O Streamlit funciona aqui como a superfície de interação: ele recebe o texto do usuário e exibe a resposta final. A lógica de decidir “o que pedir” e “para quem pedir” fica no orquestrador implementado com LangGraph, que usa o conhecimento obtido dos Agent Cards para montar o fluxo. Essa separação é importante porque a interface não precisa conhecer detalhes de cada agente. O acoplamento principal fica concentrado na camada de coordenação, que conversa com especialistas via A2A.

As engrenagens manuais do A2A puro continuam existindo e são o fundamento da interoperabilidade entre agentes. O ganho da coordenação assistida com o padrão ReAct e LangGraph está em absorver a complexidade de seleção, decomposição e agregação sem esconder o contrato subjacente. Em vez de o desenvolvedor orquestrar cada passo manualmente, a camada inteligente usa as skills descobertas para planejar as chamadas. Isso reduz atrito operacional, mas continua dependente de Agent Cards corretos e especialistas bem definidos.

## Transcrição

00:00

Pessoal, estava com um probleminha aqui de

00:02

dados dos agentes que estavam quebrando a aplicação,

00:08

mas agora deu tudo certo, tá?

00:10

Deixa eu mostrar aqui para vocês uma coisa.

00:16

Vou pedir para descobrir que agentes que têm na rede, tá? Ah, eu vou apagar aqui,

00:22

pessoal, porque isso aqui foi eu testando. Deixa eu abrir de novo aqui, tá? Vamos lá.

00:34

Vamos pedir para o orquestrador aqui, tá? Que é o multiagente do LinkGraph,

00:38

descobrir que outros agentes ele tem na rede, tá?

00:44

Aí ele descobriu, pessoal, o sistema descobriu agentes e os skills.

00:47

Então ele descobriu dois agentes, tá? O agente logístico,

00:49

o agente estoque, obviamente, é o que a gente esperava, né?

00:52

E só para mostrar, pessoal, que no agente de... No

00:58

agente de logística, né? A gente tinha implementado o rastrear pedido,

01:02

tá aqui tudo certinho, ó. Beleza? Tá?

01:06

Então, ótimo. Então, beleza. Então, vamos lá.

01:10

Agora, vamos colocar aqui, ó. Vamos colocar aqui, ó.

01:18

Qual o status do pedido 123 e o estoque do SKU -TEC01, né?

01:24

Ele deveria chamar os dois agentes, né?

01:27

O rastrear pedido e o verificar estoque. Beleza? Vamos ver, ó.

01:33

Ele falou, ó, o status do pedido 123 é esse e o estoque é esse aqui. Então,

01:37

agora vamos ver o que está acontecendo por debaixo dos panos aqui,

01:39

por debaixo do capô, pessoal. Olha só.

01:42

O agente executou o ato. O agente respondeu via2way.

01:49

Vou consultar o status do pedido e a disponibilidade do estoque para você.

01:53

Então, vem aqui. O agente logístico executou rastrear pedido e respondeu via2way.

01:57

Pedido 2, 3, status entregue, data de entrega, tal hora.

02:01

E o agente estoque executou verificar estoque e respondeu via2way.

02:06

Mesma coisa. Ou seja, então olha que interessante,

02:09

nesse caso aqui, o Streamlit, ele é o

02:15

chat, na verdade, ela é a interface através do qual o orquestrador do LinkGraph,

02:21

ele recebe esse prompt do usuário, e ele,

02:24

por saber que existem dois agentes,

02:27

um especialista em estoque e outro especialista em logística,

02:31

ele sabe exatamente o que pedir para quem.

02:35

Beleza, pessoal. Então, hoje a gente descobriu a comunicação multiagente.

02:40

Vimos uma comunicação multiagente usando o E2A.

02:44

Vimos como as engrenagens manuais rodando soltas no protocolo E2A puro. E, na sequência,

02:50

comprovamos como inteligência artificial poderosa engole essa complexidade para

02:55

a gente usando o padrão React com o LegGraph.

02:59

Beleza, pessoal. Até a próxima.

## Resumo IA

[RESUMO_IA]