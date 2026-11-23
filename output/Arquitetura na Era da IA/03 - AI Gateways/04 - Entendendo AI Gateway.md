Módulo: Arquitetura na Era da IA\
Aula: [Entendendo AI Gateway](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18288)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, no vídeo anterior a gente falou que a nossa aplicação ao longo do tempo pode ficar

00:05

fragilizada conforme a gente vai crescendo a utilização de

00:08

recursos de IA dentro da nossa aplicação. E por conta disso,

00:11

muitas vezes é interessante nós termos uma camada intermediária dentro da

00:16

nossa aplicação e essa camada a gente chama de AI Gateway.

00:19

Então uma AI Gateway é uma fronteira arquitetural para centralizar,

00:24

padronizar e controlar o acesso aos modelos de IA. Ela não é simplesmente um helper,

00:29

também não é só uma função que encapsula uma chamada HTTP.

00:33

A ideia é ter um ponto controlado por onde essas chamadas já passam

00:37

para que a aplicação não precise conhecer todos os detalhes de cada provider.

00:41

Em vez de uma feature chamar diretamente um modelo específico,

00:45

ela passa a pedir uma capacidade.

00:48

Por exemplo, resumir um texto, classificar uma mensagem, gerar uma resposta,

00:52

analisar uma intenção ou até mesmo enriquecer uma informação. A partir daí,

00:56

essa camada pode decidir como executar essa chamada. Ela pode escolher um modelo,

01:01

pode aplicar timeout, fazer políticas de retry,

01:05

fallback, ou até mesmo utilizar um outro provider.

01:08

No final das contas, ela pode também entregar respostas mais simples,

01:11

quando a resposta mais completa ali não for possível,

01:14

pode trabalhar ali com processamento assíncrono e

01:17

também pode inclusive bloquear ali operações.

01:20

E uma das coisas importantes também é registrar custo,

01:23

latência, utilização. Ou seja,

01:26

a gente consegue aplicar políticas totalmente diferentes

01:29

dependendo do tipo de operação.

01:32

E isso muda bastante o desenho do sistema,

01:34

porque agora a IA, ela deixa de ser chamada de qualquer lugar, de qualquer jeito,

01:40

e passa a ser consumida por meio de uma fronteira ali mais clara.

01:43

Claro que existem níveis diferentes de maturidade aqui. Em alguns casos,

01:47

você só precisa sair do SDK direto e usar uma camada

01:51

de compatibilidade para acessar múltiplos providers de forma mais padronizada.

01:55

Em outros casos,

01:56

você precisa construir uma gateway manual dentro da sua própria arquitetura,

02:00

porque as regras são muito específicas do seu produto. E em outros cenários,

02:04

pode fazer sentido usar uma solução pronta de

02:07

mercado que já traz recursos de roteamento,

02:09

métricas, fallback, controle de uso e padronização operacional.

02:14

Então, ao longo desse módulo, a gente vai passar por essa evolução.

02:17

Nós vamos começar pelo SDK direto como um ponto de partida,

02:21

só para entender onde normalmente tudo começa. Depois, vamos olhar...

02:26

para as ferramentas como Lite e LLM,

02:29

que ajudam nessa ideia de compatibilidade e padronização entre providers. Em seguida,

02:34

a gente vai discutir o que muda quando você constrói uma gateway manual,

02:38

colocando dentro delas políticas com timeout,

02:41

retry, fallback, degradação, resposta parcial,

02:44

revisão humana e processamento assíncrono.

02:46

E depois, vamos falar também de gateways prontos de mercado.

02:50

Por exemplo, a gente tem a Verso AI Gateway, a gente tem a Cloudflare Gateway.

02:55

Existem diversas alternativas. A ideia aqui não é decorar ferramenta,

03:00

a ideia é entender a progressão arquitetural.

03:03

Porque a IA entra de verdade em uma aplicação,

03:06

Agora o grande ponto é, a pergunta no final das contas é,

03:10

A pergunta deixa de ser apenas,

03:12

Como que eu chamo o modelo? Na realidade,

03:14

A pergunta passa a ser, como a minha arquitetura controla, padroniza,

03:19

Protege e evolui o uso de IA dentro do sistema?

03:23

Então é isso que a gente vai trabalhar nesse módulo.

## Resumo IA

[RESUMO_IA]