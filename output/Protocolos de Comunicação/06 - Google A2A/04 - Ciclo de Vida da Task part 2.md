Módulo: Protocolos de Comunicação\
Aula: [Ciclo de Vida da Task part 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18616)

## Resumo da aula

message e artifact não cumprem o mesmo papel, mesmo quando ambos carregam conteúdo útil. A message sustenta a conversa operacional da Task: confirmações, pedidos de esclarecimento, instruções intermediárias e sinais de progresso. O artifact concentra o produto formal da execução, pronto para consumo por outro sistema, download ou versionamento. Essa separação evita que uma UI de chat dite o contrato de integração de toda a solução.

A fronteira correta depende do destino do conteúdo. Se a informação existe para orientar o próximo turno da interação, ela pertence ao histórico de messages; se existe para ser reutilizada como saída estável, ela deve aparecer em artifacts. Retomando o cenário de processamento de PDF, “aguarde um instante” ou “preciso de mais contexto” são conversa, enquanto o .txt resumido é entrega formal. Quando essa distinção é mal desenhada, a experiência humana pode até parecer aceitável, mas automação downstream, auditoria e reprocessamento ficam frágeis.

O acompanhamento da Task pode ser síncrono, por streaming ou por webhook, e a escolha precisa seguir o custo temporal da operação. O modo síncrono mantém a conexão aberta até a resposta final, o que simplifica o cliente, mas se torna arriscado quando a duração é imprevisível. Streaming mantém o canal vivo para receber atualizações incrementais em tempo real; webhook desacopla totalmente o cliente da espera, permitindo retorno assíncrono posterior. Antes de escolher, o cliente deve verificar no Agent Card se o agente realmente declara suporte ao modo desejado.

sendStreamingMessage ativa um fluxo no qual o servidor emite eventos estruturados enquanto a Task evolui. O ganho principal não é apenas “ver texto chegando”, mas substituir polling cego por observabilidade semântica do lifecycle. Em vez de consultar repetidamente o estado com getTask, o cliente passa a reagir a fatos emitidos pelo servidor. Isso reduz ruído operacional e melhora a responsividade da interface.

TaskStatusUpdateEvent comunica mudanças de estado da Task durante a execução. Ele informa ao cliente que a execução avançou no grafo operacional já conhecido, sem exigir consultas periódicas para descobrir se algo mudou. Esse evento é especialmente valioso em tarefas longas, porque UI, logs e métricas podem refletir progresso quase em tempo real. O resultado é menos polling, menos latência percebida e maior coerência entre backend e front-end.

TaskArtifactUpdate entrega fragments do artifact final em vez de obrigar o cliente a esperar um bloco monolítico. Cada fragmento, ou chunk, representa uma parte do entregável, e o cliente recompõe o resultado usando semântica de append. Esse desenho reduz pressão de memória, melhora a experiência em redes instáveis e permite exibir progresso concreto de produção do arquivo. Em front-end, a preocupação central deixa de ser “quando chega tudo” e passa a ser “como remontar corretamente o que já chegou”.

Streaming não elimina a persistência da Task; ele apenas muda a forma de observá-la. Se a conexão cair, a execução continua existindo no servidor e pode ser retomada por reconexão ou inspeção posterior do estado. Isso preserva a identidade da Task e evita que falhas transitórias de rede sejam confundidas com falhas de negócio. A robustez vem justamente da combinação entre estado persistente e entrega incremental.

Retomando o cenário do PDF, sendMessage inicia a Task com um turno role: user que combina um filePart apontando para o documento e um textPart com a instrução “resuma em português-BR”. O servidor responde com o id da Task e o estado inicial submitted, o que transforma a solicitação em execução rastreável. A partir daí, o cliente pode acompanhar a evolução por getTask, streaming ou webhook, conforme a capacidade publicada pelo agente. O ponto decisivo é que a saída final não fica enterrada em conversa: ela aparece em artifacts como um novo .txt reutilizável.

input-required introduz um fluxo multiturno sem quebrar a continuidade da Task. Quando o agente detecta ambiguidade ou falta de dados, ele pausa a execução e emite uma mensagem explicando exatamente o complemento necessário. O cliente responde usando o mesmo task id, anexando o novo conteúdo sem reiniciar o processo do zero. Depois disso, a Task retorna a working e segue com rastreabilidade contínua do início ao fim.

Quatro verificações capturam boa parte dos erros iniciais em integrações A2A. A primeira é conformidade de estado: não inventar estados fora do TaskState oficial, porque isso quebra interoperabilidade, tracing e UI. A segunda é conformidade de entrega: resultado formal vai em artifact, não em message; a terceira é conformidade de transição: estado terminal não retorna para working; a quarta é conformidade de acompanhamento: evitar polling agressivo quando streaming ou webhook são suportados. Esse checklist é simples, mas impede bugs que normalmente aparecem cedo e custam caro depois.

## Transcrição

00:01

E com os blocos de comunicação bem consolidados,

00:04

Deparamos com o maior desafio da programação de interfaces em IA.

00:09

Onde começa o documento formal e onde termina o chat orgânico.

00:13

Esse slide destaca a diferença rigorosa entre message e artifact.

00:18

Uma message abarca todo o ruído logístico da execução.

00:23

É o aguarde um instante ou não entendi sua diretriz.

00:28

Ela nutre e orienta a interação passo a passo.

00:31

O artefato, por outro lado, é o artefato final em si.

00:35

Ele incorpora o valor entregável puro, desprovido de abstrações discursivas.

00:40

Pode ser o arquivo finalizado no formato PDF ou a

00:43

análise consolidada pronta para uma planilha de saída.

00:46

No papel de líderes técnicos e arquitetos,

00:48

Desenhar a fronteira entre as mensagens efêmeras exibidas na janela de chat

00:52

e os artefatos permanentes que alimentam o botão de download

00:56

É a decisão arquitetural que mais tem impacto

00:58

positivo na usabilidade da sua solução. A

01:02

flexibilidade do ecossistema TASC nos oferece três abordagens de conexões distintas,

01:07

que devem ser casadas exatamente com o peso operacional da tarefa.

01:11

A abordagem mais familiar é o modelo síncrono.

01:14

Mandamos a solicitação de processamento rápido e nossa conexão

01:18

fica congelada aguardando o resultado no mesmo fôlego.

01:21

Ele atende de maneira simples,

01:23

porém perigosa diante de tempos de execução muito imprevisíveis.

01:27

Em contrapartida, temos o streaming via server-safe events.

01:32

Essa abordagem permite despachar a ordem e manter o túnel receptivo enquanto

01:36

o servidor empurra atualizações e fragmentos em tempo real na tela do cliente.

01:41

É um mecanismo vital para fluxos logísticos sofisticados. Finalmente,

01:45

oferecemos a camada push assíncrona via um atalho de webhook. Nela,

01:50

submetemos o pedido junto com uma rota de retorno.

01:55

Desplugamos a interface com segurança e confiamos que o

01:59

agente fará uma chamada autônoma de volta horas depois.

02:02

A escolha de qual usar sempre começa validando

02:07

as capacidades declaradas pelo agente no seu agent card.

02:12

Observando o modelo de streaming em detalhes,

02:14

é essencial destrinchar o mecanismo acionado via Send Streaming Message.

02:18

Nele, sua rede não entra em estado de letargia.

02:21

O servidor pulsa informações em tempo real.

02:25

Você escuta ativamente eventos estruturados.

02:27

O primeiro deles é o Task Status Update Event,

02:30

o passo instantâneo avisando sobre cada milímetro do

02:35

gráfico de estado de uma aplicação atravessou.

02:37

É o...

02:38

É o fim definitivo do loop perigoso de pooling.

02:41

O segundo componente fundamental é o task artifact update.

02:44

Como não queremos que o navegador engasgue

02:47

aguardando um bloco gigantesco de arquivos,

02:50

o servidor fragmenta o artifact em pedaços menores,

02:53

chamados chunks. Na interface de front-end,

02:55

uma lógica simples utiliza a propriedade de apêndice para

02:58

fundir o arquivo final na memória do dispositivo.

03:02

Essa infraestrutura foi modelada para ser altamente resiliente. Se a rede caiu,

03:05

o estado continua vivo na nuvem, esperando a sua reconexão.

03:10

Colocando nossa lupa na camada JSON oficial trafegada na rede,

03:14

esse diagrama ilustra uma rotina madura, a sumarização técnica de um arquivo PDF.

03:20

O processo parte da modelagem inicial via sendMessage,

03:24

agregando sobre a tag

03:29

roleUser como duas dependências vitais.

03:32

a URL de file part, sinalizando o documento original,

03:35

e a ordem declarada no text part,

03:38

indicando resuma em português BR. Ao interagir na API,

03:43

a plataforma acusa o recebimento,

03:45

gerando a chave exclusiva, o ID, sob o rótulo inicial submitted.

03:50

Evoluindo no percurso, observamos que a etapa seguinte...

03:53

Observamos na etapa seguinte uma mudança ativa rastreada pelo método GET,

03:58

onde o indicador gira os motores no estado de WORK. Por fim,

04:03

chegamos à etapa 4, fechamento total.

04:06

A plataforma devolve o carimbo absoluto de COMPLETED,

04:08

mas o detalhe crucial se esconde na saída.

04:11

Nós não coletamos transabstrações convencionais efêmeras.

04:15

Nós puxamos diretamente na raiz de artifacts uma

04:18

resposta sólida contendo o novo arquivo .txt.

04:24

Nós concluímos esse ciclo focando na engenharia elegante

04:27

do cenário de pausas e retomadas multiturno,

04:30

com o estado de input required.

04:32

Essa flexibilidade é crucial. No desenvolvimento com modelos massivos,

04:36

é fato que as inteligências se chocam com ambiguidades.

04:40

A plataforma processa isso fluidamente em três passadas lógicas.

04:44

O fluxo se rompe primeiro numa solicitação reflexiva de pausa.

04:48

O agente nota a deficiência de estados,

04:51

encosta a máquina de inferência e gera ativamente

04:55

no log uma mensagem detalhando exatamente o que precisa.

05:00

Segundo, temos o período de resposta ativa.

05:03

Uma aplicação aguarda que o supervisor injete o complemento e

05:06

devolva e aproveitando o exato task ID da função de usuário,

05:10

empilhando conteúdo sem... reinício os sujos.

05:15

Terceiro, vivenciamos a reentrada inteligente.

05:19

Munido da resposta faltante, a engine desativa a barreira,

05:24

mudando instantaneamente o estado perante o servidor para

05:28

o working e a orquestração avança livre.

05:30

Trata-se de evolução contínua em torno de uma porta fixa,

05:33

garantindo rastreabilidade do início ao fim do processo.

05:38

E aqui, pessoal, esse slide, ele traduz a aula para Code Review.

05:42

Eu estou revisando uma implementação 8-way, olho para esses quatro pontos cedo.

05:48

É porque eles costumam aparecer antes dos problemas mais sofisticados.

05:52

Primeiro estado custom.

05:54

O agente inventa o estado como Process Stage 2.

05:58

Parece útil no começo, mas quebra cliente,

06:02

UI, tracing, métricas e interoperabilidade.

06:05

O estado task não é lugar para criatividade. Use o Task State oficial.

06:10

Segundo, Message vs Artifact. Se o agente entrega o resultado final como Message,

06:17

Talvez funcione bem em uma UI Chart.

06:19

Mas quando outro sistema precisa baixar, validar,

06:22

versionar ou encaminhar esse Output,

06:24

a integração começa a sofrer. Se é entrega formal, trate como Artifact.

06:30

Terceiro, Transação Inválida.

06:31

Um exemplo clássico é tentar sair de Task State

06:34

Completed e voltar para Test State Working.

06:38

Isso não é retomada, é violação de ciclo de vida. Estado terminal é terminal.

06:43

4. Pule regressivo. Agressivo.

06:45

Cliente que chama GetTask em loop curto

06:48

para simular tempo real acaba criando custo,

06:53

ruído operacional e risco de rate limit.

06:55

Se o agente declara streaming, prefere streaming de eventos.

07:00

Para tarefas longas ou clientes desconectados, considere push notification.

07:04

A regra prática para review é simples. Validação de estado,

07:08

transição, entrega e modo de acompanhamento.

07:11

Esses quatro checkpoints evitam boa parte dos bugs iniciais em integração E2A.

07:16

Bem, fechando aqui, pessoal. No E2A, a task é a unidade rastreável de trabalho.

07:22

Ela organiza identidade, estado, histórico de interações e entregas formais.

07:26

Se você entende task, fica muito mais fácil desenhar cliente, agente, UI,

07:32

observabilidade e debug. O primeiro bloco da aula foi sobre test state.

07:37

A gente viu os estados operacionais,

07:39

as transações válidas e a regra mais importante,

07:46

estado terminal é terminal.

07:48

Uma task que chegou em test state completed, test state failed,

07:52

test state canceled ou test state rejected não volta para o work, pessoal.

07:59

Bom então, seja pessoal, assim de tudo que a gente viu, que é esse vocabulário que você

08:03

leva para casa: estado, transar, transição, mensagem, parte aqui

08:08

que é artefato e o modo de

08:12

acompanhamento e na próxima aula a gente vai, a gente

08:14

vai para a parte mais legal que é

08:16

o de lado, tá pessoal? A gente vai implementar e vai explorar a parte de gente. Cá está.

## Resumo IA

[RESUMO_IA]