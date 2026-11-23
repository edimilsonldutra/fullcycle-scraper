Módulo: Protocolos de Comunicação\
Aula: [LAB Orquestração Direta part 1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18926)

## Resumo da aula

Orquestração central concentra a decisão de coordenação em um nó único, como ocorre em topologias com um maestro que escolhe qual agente chamar, em que ordem e com qual contexto. Esse desenho simplifica o controle inicial, mas cria gargalo de conhecimento e ponto único de falha, porque toda a inteligência de composição fica presa no coordenador. Orquestração direta remove esse intermediário: um agente especializado pode chamar outro agente por conta própria quando identifica que depende de uma capacidade externa para concluir seu trabalho.

Orquestração direta acontece quando um agente deixa de ser apenas executor de uma requisição recebida e passa a atuar também como consumidor de outro agente durante o mesmo fluxo. O ponto central não é só haver múltiplos agentes, mas haver colaboração descentralizada entre eles. Isso muda a arquitetura porque a composição do workflow deixa de estar toda fora dos especialistas e passa a emergir dentro do processamento de cada agente.

O agente de estoque ocupa dois papéis no mesmo fluxo: primeiro, recebe a solicitação do GenUI como servidor A2A; depois, ao detectar necessidade de dados logísticos ou alfandegários, assume o papel de cliente A2A para consultar o agente de logística. Esse comportamento é a peça nova da arquitetura, porque o estoque não apenas responde ao usuário: ele coordena uma subtarefa externa para completar sua própria resposta. Um agente com papel duplo continua sendo um especialista de domínio, mas agora também participa ativamente do encadeamento multiagente.

Retomando o cenário de e-commerce já conhecido, a topologia agora forma uma cascata: o GenUI fala com estoque, e estoque fala com logística. O GenUI continua sendo a interface de entrada, mas deixa de carregar a responsabilidade de coordenar todos os especialistas. A consequência é que a lógica de composição fica mais próxima do domínio que realmente sabe quando precisa escalar a consulta para outro agente.

Agente servidor é o que expõe capacidade para ser invocado; agente cliente é o que consome a capacidade publicada por outro agente. Na orquestração direta, essas funções não são identidades fixas do processo inteiro, mas papéis assumidos em momentos diferentes do workflow. O mesmo serviço pode começar atendendo uma requisição e, no meio da execução, emitir outra requisição A2A para completar a tarefa corrente.

Um workflow multiagente descentralizado distribui a coordenação entre os próprios especialistas, em vez de concentrá-la em um orquestrador externo. Isso reduz acoplamento arquitetural, porque cada agente decide quando precisa delegar parte do trabalho com base no seu próprio contexto de negócio. Também melhora evolução incremental: novos agentes podem ser conectados ao ecossistema sem reescrever um coordenador central para cada combinação possível.

A2A continua sendo a base de interoperabilidade entre os agentes, e o Agent Card segue como contrato público de descoberta e invocação já estabelecido anteriormente. O avanço aqui não está em redefinir esses elementos, mas em aplicá-los a uma colaboração lateral entre especialistas. Em vez de apenas um cliente externo consumir agentes, um agente passa a descobrir e consumir outro dentro do próprio processamento.

A implementação gira em torno de um ponto crítico: o método chamar_agente, acionado pelo estoque quando ele conclui que não consegue finalizar a resposta sozinho. Esse método materializa a transição de papel do estoque, que sai da posição de servidor e passa a emitir uma chamada A2A para logística. O agente logístico já está preparado, então o foco prático fica em codificar a decisão, disparar a chamada e consolidar a resposta recebida na saída final do estoque.

O agente de logística é tratado como especialista e depende de grounding no prompt para reduzir alucinações e melhorar a confiabilidade dos dados retornados. Isso importa porque, em um fluxo encadeado, um erro do agente chamado contamina a resposta consolidada do agente chamador. Quando a especialização é bem ancorada, a colaboração direta entre agentes produz respostas mais previsíveis e mais úteis para produção.

## Transcrição

00:00

Pessoal, chegamos ao laboratório mais importante deste módulo. Então, até agora,

00:05

nossos clientes conversavam com um único agente por vez. No mundo real,

00:10

sistemas de produção precisam de agentes conversando entre si,

00:12

e muitas vezes de forma autônoma ou semautônoma.

00:15

Sem uma E, só o coordenador central.

00:17

Então, vamos construir um agente que atua ao mesmo

00:19

tempo como servidor e cliente H -Way. Então assim, pessoal,

00:24

quando as pessoas pensavam em múltiplos agentes trabalhando juntos,

00:27

elas pensavam em orquestração central, ferramentas como o LingGraph,

00:30

o CruEI, atuando como maestros. O problema?

00:35

Esse maestro vira um gargalo de conhecimento e um ponto único de falha.

00:38

A orquestração direta, baseada no protocolo 8 -way,

00:41

muda totalmente essa topologia. Um agente chama o outro diretamente.

00:44

No nosso e -commerce, o cliente GenUI,

00:47

que é o cliente que faz a interface com o usuário,

00:50

chama o estoque. O estoque percebe que precisa de transporte e chama a logística.

00:55

A grande sacada técnica aqui é o papel duplo do estoque.

00:58

Ele recebe a requisição atuando como servidor,

01:00

mas no meio do processamento ele vira cliente para acionar outro agente.

01:04

A frase que vocês devem levar para o time é exatamente essa.

01:07

A orquestração direta é quando um agente vira cliente do outro.

01:10

Vamos dar uma olhada melhor nisso.

01:12

Então, aqui nós vemos a diferença estrutural no ICRUA. Do lado esquerdo,

01:16

o padrão central, frameworks como o LengGraph, CRUA,

01:20

enfim, neles você precisa de um nó coordenador.

01:23

O coordenador é o único que decide o que vai fazer,

01:26

quando fazer e que ordem. Os agentes A e B sequer sabem que o outro existe.

01:32

Já do lado direito, temos o padrão E2A direto,

01:36

que no caso é com sucesso workflow agêntico.

01:38

que é exatamente o que nós vamos construir hoje.

01:40

A gente tem um front -end, que eu chamei de GNY,

01:43

que é de Generative User Interface,

01:46

que atua como cliente, aciona o agente de estoque.

01:49

O estoque, de forma autônoma e descentralizada,

01:52

é a orquestra chamada para o logístico usando o protocolo E2E puro.

01:55

Não existe coordenador no meio, o próprio agente toma rédea.

01:59

E por que isso é poderoso?

02:01

Porque o protocolo E2A com agent cards, zone RTC e pooling,

02:05

ele foi desenhado desde o dia zero para suportar

02:08

esse ecossistema sem ponto único de falha.

02:10

Você pluga e despluga agentes como se fossem legos e o sistema continua fluido.

02:16

Pessoal, essa é a topologia que vamos rodar hoje, tá?

02:19

Pensem nisso como um efeito cascata. No nosso ponto à esquerda,

02:22

temos o nosso Strelit app. Ele não é mais um protein de burro,

02:25

ele é um GNY, um agente de interface. Quando ele...

02:30

entende que precisa de dados e eles param sendo message para o agente de estoque.

02:34

O agente de estoque,

02:35

que vai estar na porta 9002,

02:36

recebe essa chamada atuando como servidor H2A para o agente de NY.

02:41

Mas aí entra a mágica.

02:42

No meio do processamento, o estoque percebe que precisa de dados alfandegários.

02:47

Ele invoca a função chamar agente e neste exato mês

02:49

de segunda ele se transforma em um cliente A2A,

02:52

disparando requisições para o agente de logística,

02:55

que no caso virou um A2A server para o agente de estoque na porta 9001.

03:00

Esse papel duplo, nascer como servidor e atuar como cliente no meio do ciclo,

03:05

é o segredo que viabiliza a orquestração direta e redes centralizadas.

03:09

A gente vai ver isso no código.

03:11

Então, só para a gente ir para o lado, pessoal, algumas dicas aqui.

03:17

A logística, ele é o agente especialista, tá?

03:20

É importante vocês prestarem atenção na injeção de conhecimento no prompt,

03:24

que é o grounding, tá? Para zerar alucinações de dados, tá? Nesse caso,

03:29

o agente logístico já está pronto, tá, pessoal?

03:31

Vocês não vão ter que mexer nada nele,

03:32

só dá uma olhada. O orquestrador, que é o estoque, tá?

03:36

e aí a, aí a pensando e analisando a intenção do usuário antes de parar, antes de

03:40

disparar a linha mágica, tá? Eu chamei de linha mágica.

03:43

Pessoal, o método chamar a gente tá dando

03:46

uma olhada lá depois, aqui já é uma super dica,

03:48

porque vocês precisam fazer, né? E por fim,

03:50

gente, momento aqui: 3LM front-end estoque, logística, conversa e

03:54

consolida os dados em cascata, tá bom? Então,

03:57

agora vamos para o código, tá? A

04:01

hora que você dá uma pausa, eu vou, vamos para o código.

## Resumo IA

[RESUMO_IA]