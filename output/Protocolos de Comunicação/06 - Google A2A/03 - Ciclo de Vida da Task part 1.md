Módulo: Protocolos de Comunicação\
Aula: [Ciclo de Vida da Task part 1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18615)

## Resumo da aula

A Task é a camada operacional que transforma uma solicitação entre agentes em uma execução rastreável, com identidade, histórico, estado e entregas formais. Retomando a ideia de Task já estabelecida, o ponto novo aqui é tratá-la como objeto persistente, e não como chamada efêmera. Isso permite acompanhar progresso, pausar o fluxo quando faltar insumo e distinguir conversa intermediária de resultado consolidado. A estrutura mínima gira em torno de id, status, messages e artifacts, porque esses campos sustentam identificação, observabilidade, histórico e saída final.

O lifecycle da Task pode ser entendido por quatro pilares. O primeiro é a máquina de estados, que define em que momento a execução está e quais transições são válidas. O segundo é o conteúdo conversacional, formado por Message e Part, que carrega texto, arquivos e dados estruturados no mesmo fluxo. O terceiro é artifacts, usado para separar o produto final do ruído da interação. O quarto pilar cobre fluxos avançados, como streaming e interações multi-turno, que dependem diretamente dessa base operacional.

Os oito estados se organizam em quatro fases lógicas: submissão, atividade, interrupção e terminal. submitted marca que o pedido foi aceito no protocolo, mas ainda não entrou em processamento efetivo. working representa execução ativa, com inferência e consumo computacional. input-required e auth-required interrompem o fluxo para aguardar ação externa; completed, failed, canceled e rejected encerram a Task de forma definitiva.

A Task nasce em submitted e segue para working quando o agente inicia o trabalho, ou para rejected quando a solicitação é recusada antes da execução. A transição para input-required ou auth-required só é válida a partir de working, porque a interrupção pressupõe que a execução já começou e encontrou um bloqueio operacional. Quando o cliente envia o insumo faltante no mesmo contexto, a Task retorna para working. Estados terminais não voltam para estados ativos, o que preserva consistência de histórico e simplifica observabilidade.

canceled funciona como uma rota de escape acionada pelo cliente para interromper a execução antes do término natural. Ele não depende de a Task chegar a failed nem de o agente concluir o trabalho, porque sua função é encerrar o processamento de forma explícita e segura. Esse atalho é importante em integrações reais, nas quais timeout de negócio, desistência do usuário ou mudança de contexto exigem parada imediata. O efeito prático é evitar processamento desnecessário e manter o estado final semanticamente claro.

Cada Message representa um turno da interação, com papel explícito de user ou agent. O avanço aqui não está em redefinir Message, mas em entender que ela serve como envelope para um payload composto, capaz de reunir diferentes tipos de conteúdo na mesma troca. Em vez de espalhar contexto em múltiplas chamadas paralelas, o protocolo permite enviar texto, arquivos e dados estruturados juntos. Isso reduz fragmentação e facilita a correlação entre instrução, insumos e resposta.

textPart carrega linguagem natural e instruções discursivas. filePart referencia objetos externos, como imagens, vídeos e PDFs, normalmente por URL, para que o agente consuma conteúdo não textual sem quebrar a semântica do protocolo. dataPart transporta JSON estruturado, útil para parâmetros, flags, campos de controle e dados que precisam ser interpretados de forma determinística. A combinação desses tipos cria um payload unificado, no qual prompt e estrutura convivem no mesmo turno.

artifacts separam o resultado consolidado da conversa intermediária que ocorreu durante a execução. Essa distinção importa porque nem toda Message produz valor final; muitas apenas negociam contexto, pedem insumos ou registram passos transitórios. Ao indexar os entregáveis em um campo próprio, a Task facilita consumo posterior, auditoria e integração com sistemas que só precisam do produto final. Retomando o cenário de colaboração entre agentes, é aqui que a execução deixa de ser apenas diálogo e passa a expor saída formal.

## Transcrição

00:01

Pessoal, bem-vindo a mais uma aula.

00:04

Nesse caso, nós vamos falar sobre o ciclo de vida da TASC do ecossistema A2A.

00:11

Nas aulas anteriores, nós discutimos profundamente a questão de agentes,

00:16

descoberta e funcionamento do Agent Cards. Hoje,

00:19

nosso objetivo é essencialmente prático.

00:21

Vamos entender o que acontece a partir do minuto em

00:24

que o agente aceita e inicia uma nova solicitação.

00:26

Onde essa execução mora?

00:29

E a resposta é a TASC.

00:31

Uma task é um container estrutural onde o

00:33

pedido de um usuário ganha identidade rastreável,

00:36

um ciclo de estados bem definidos e um local para entregas formais.

00:40

Nos próximos minutos, nós vamos mapear juntos três componentes primários.

00:45

Primeiro, os oito estados operacionais de uma task. Segundo, as partes.

00:50

Segundo, as partes, que são nossas engrenagens de texto, arquivos e dados.

00:55

E terceiro, a diferença crucial entre a comunicação intermediária e os artifacts,

01:00

que são os entregáveis finais.

01:02

A meta central é garantir que você adquira um

01:05

modelo mental maduro para desenhar integrações limpas,

01:08

ler logs e debugar o comportamento do agente sem atritos técnicos.

01:13

Então, primeiramente, o que é uma task do ponto de vista do ecossistema A2A?

01:19

Ou seja,

01:23

uma task organiza e encapsula o documento trabalhativo.

01:26

Nós a desdobramos em quatro pilares para facilitar o desenvolvimento.

01:31

O primeiro pilar são os estados oficiais.

01:33

Eles representam o momento operacional exato da tarefa e gerenciam as regras

01:38

rígidas do que é ou não é permitido na transação do fluxo.

01:42

O segundo pilar cobre as mensagens e partes,

01:47

que nada mais são do que blocos atômicos que combinam textos,

01:52

arquivos binários e JSON em um único trânsito bidirecional.

01:56

O terceiro ponto trata dos artifacts,

01:58

os nossos produtos finais,

02:00

separando o que é ruído conversacional do que é valor consolidado.

02:03

E o último pilar será o de fluxos avançados,

02:07

onde abordaremos ferramentas potentes de streaming

02:09

e interações multiturno para lidar

02:12

com gargalos onde a máquina precisa pedir nossa ajuda para continuar operando.

02:17

A arquitetura do H2A não trata requisições como fluxos voláteis. Pelo contrário,

02:23

a TESC é desenhada como uma unidade de trabalho persistente.

02:26

Pense nela como uma sessão colaborativa. O cliente gera a ordem,

02:29

o agente assume o volante e ambos monitoram o progresso continuamente.

02:34

Na engenharia dessa API,

02:35

cada objeto task possui propriedades obrigatórias.

02:38

Temos o ID como chave de identificação absoluta,

02:41

o status como seu carimbo de tempo indicando o exato andamento,

02:46

as mensagens que retêm cada etapa de troca de contexto

02:49

no histórico e os artifacts que indexam o trabalho gerado.

02:53

Na prática,

02:55

a sua aplicação criará tasks via métodos de send,

02:58

fará a sondagem do progresso usando chamadas periódicas de GET.

03:02

E caso seja necessário abortar a execução prematura,

03:05

acionará o método formal de cancelamento, garantindo o encerramento seguro.

03:11

A estabilidade de qualquer integração depende do

03:14

monitoramento preciso e de transações.

03:16

O H-Way formaliza isso via TaskState. Ao longo de sua...

03:23

da sua implementação, você verá oito estados atuando em quatro fases lógicas.

03:28

A operação inicia na fase de submissão.

03:31

O task state submitted, ou só para fins de simplificação,

03:36

submitted, confirma que o pedido foi validado,

03:39

embora o agente não tenha começado o trabalho bruto.

03:42

Logo, evoluímos para a fase ativa,

03:45

com o estado working,

03:46

o momento onde o gasto computacional e a inferência acontecem. Porém,

03:51

se o modelo atingir um impasse por falta de contexto,

03:54

a task entra na fase de interrupção,

03:56

acionando o status inputRequired ou offRequired para aguardar a ação do cliente.

04:02

Superadas essas fases, chegamos aos status terminais,

04:06

completed para sucessos absolutos,

04:09

failed para exceções críticas ou canceled para decisão ativa

04:13

do cliente e rejected por bloqueios do próprio agente.

04:17

Lembre-se, estados terminais são definitivos.

04:20

O ciclo ali encerra sem margem para regressão estrutural.

04:27

Dominar as regras de trânsito entre estados separa

04:30

integrações frágeis e singulares de sistemas resilientes.

04:34

Este slide representa o grafo oficial do A2A.

04:37

Toda task parte de submitted e avança para o working

04:40

quando aceita ou cai direto para rejected se for negada previamente.

04:45

Durante a fase working,

04:47

e somente nela o agente pode transacionar

04:51

o status para input required ou off required,

04:56

sem faltar insumo.

04:59

Esse é o mecanismo de pausa desenhado organicamente.

05:03

Assim que o cliente fornece a peça faltante respondendo no mesmo turno,

05:10

a task volta automaticamente para a trilha ativa de work.

05:14

No desfecho do ciclo, o processo desce aos portões terminais de Completed ou Failed.

05:21

Note que estados terminais não retornam para

05:23

processos ativos sob nenhuma circunstância.

05:26

Apenas o estado de cancelamento funciona como atalho livre de escape.

05:30

O Cancelled age como um disjuntor remoto que pode ser disparado

05:35

pelo cliente a qualquer segundo para paralisar a engine ativa imediatamente.

05:43

Superamos a máquina de estados. Chegou a hora de observar a anatomia do transporte,

05:47

as nossas messages e paths.

05:50

Dentro do A2A, a message isolada representa um turno discursivo.

05:55

O papel dessa mensagem é delimitado explicitamente como usuário

06:00

para o cliente ou agente para IA.

06:02

Contudo, em vez de passar textos puros, como vemos em modelos de chat simples,

06:07

a plataforma empacota o contexto das chamadas partes,

06:10

que agem como as verdadeiras moléculas de dados.

06:13

Nós usamos textPart para comandos em linguagem natural,

06:17

implementamos filePart quando precisamos referenciar vídeos.

06:24

Imagens e PDFs diretamente de buckets via URL.

06:29

E nós ancoramos a confiabilidade no data-part,

06:32

Injetando chaves de formato JSON puro para direcionar o comportamento estruturado.

06:38

Essa flexibilidade elimina requisições fragmentadas.

06:41

O desenvolvedor injeta o prompt de texto e o arquivo

06:45

JSON com os parâmetros de um payload unificado,

06:47

Empurrando o lote completo num único turno de mensagem.

## Resumo IA

[RESUMO_IA]