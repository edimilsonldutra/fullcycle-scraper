Módulo: Protocolos de Comunicação\
Aula: [Implementando o Server A2A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18621)

## Resumo da aula

Um servidor A2A válido não devolve apenas uma string; ele precisa publicar a evolução da execução como uma Task persistente. Retomando o fluxo já conhecido do cliente, a novidade aqui é a borda do servidor: receber a requisição, criar a Task, emitir progresso e fechar o ciclo com um estado terminal. O exemplo minimalista usa um servidor de eco que transforma texto em maiúsculas justamente para isolar a mecânica do protocolo da lógica de negócio. Isso permite enxergar o pipeline obrigatório sem o ruído de uma integração com LLM.

A composição básica do servidor reúne quatro peças: in-memory task store, executor, default request handler e rotas no Starlette. O in-memory task store guarda o estado das Tasks em memória, o que simplifica laboratório e debugging, mas não serve para persistência real entre reinícios. O executor concentra a lógica da operação, enquanto o handler conecta essa lógica ao contrato público do agente. O framework HTTP entra por último, apenas expondo as rotas que o protocolo precisa.

O Agent Card, já definido anteriormente como contrato de descoberta, aparece aqui como parte da montagem do servidor. Ele publica nome do agente, interface JSON-RPC e skills disponíveis, permitindo que o cliente descubra e invoque a capacidade correta sem hardcoding adicional. Na implementação, isso significa que o servidor não é apenas executável: ele também precisa ser encontrável e descritível de forma padronizada. Sem esse card, a lógica pode existir, mas continua invisível para o ecossistema A2A.

O executor manual revela a coreografia exata exigida pelo protocolo. A sequência começa com a criação e o enfileiramento da Task, porque todo update posterior precisa estar ancorado em uma execução identificável. Em seguida, o servidor publica working, executa a lógica de negócio, anexa o artifact produzido e encerra com completed. A ordem importa porque o cliente acompanha estado e resultado por eventos, não por inferência a partir de uma resposta solta.

O primeiro passo é criar a Task e colocá-la na fila de eventos; isso registra formalmente a intenção recebida. O segundo é emitir working, sinalizando que a execução começou e permitindo observabilidade imediata. O terceiro é rodar a lógica de negócio, que no exemplo é apenas upper(), mas ocupa exatamente o ponto onde uma LLM ou outro processamento real seria chamado. O quarto publica o artifact, e o quinto fecha a Task com completed, consolidando o lifecycle esperado pelo cliente.

O in-memory task store é a implementação mais simples para armazenar Tasks durante a execução do processo. Ele existe para que sendMessage e getTask compartilhem a mesma visão de estado sem exigir banco de dados ou infraestrutura externa. A limitação é estrutural: reiniciar o processo apaga tudo, e múltiplas instâncias do servidor não compartilham estado. Em produção, a ideia permanece a mesma, mas o armazenamento precisa migrar para um backend persistente e compartilhável.

O default request handler funciona como a cola entre protocolo, Agent Card, store e executor. Em vez de espalhar parsing de requisição e despacho manual por várias rotas, ele centraliza o fluxo padrão esperado pelo SDK. Isso reduz código repetitivo e diminui o risco de inconsistência entre métodos do protocolo. A lógica de negócio continua no executor; o handler apenas garante que ela seja chamada dentro da moldura correta.

O TaskUpdater é a abstração que substitui a emissão manual de vários eventos por uma API menor e mais segura. A regra principal não muda: a Task ainda precisa ser criada e enfileirada primeiro, porque o SDK não elimina a semântica do protocolo. Depois disso, chamadas como startWork, addArtifact e complete encapsulam a montagem dos eventos corretos. O ganho está em reduzir boilerplate e evitar erros de conformidade na fila de eventos.

Um servidor de produção não pode assumir apenas o caminho feliz. Se a lógica de negócio falhar, a Task precisa terminar em failed, em vez de ficar presa em working indefinidamente. Isso preserva observabilidade, evita polling infinito no cliente e transforma erro interno em sinal protocolar explícito. O try/except ao redor da execução não é detalhe de estilo; ele é parte da conformidade operacional do servidor.

A substituição de upper() por uma chamada real a LLM mostra a separação entre protocolo e inteligência. O pipeline externo continua igual: Task criada, working, produção de artifact e estado terminal. Só muda o miolo da execução, que deixa de ser determinístico e passa a depender de um modelo generativo. Esse desacoplamento é valioso porque permite evoluir a capacidade do agente sem alterar suas bordas de interoperabilidade.

Quando o cliente visual descobre o agente, lê o Agent Card e acompanha working até completed, a implementação valida descoberta, contrato e execução ao mesmo tempo. No servidor minimalista, o resultado final aparece como texto em maiúsculas; no servidor com LLM, a resposta muda, mas o lifecycle observado permanece o mesmo. Esse teste confirma que a troca da lógica interna não quebrou o protocolo. Em debugging, essa equivalência ajuda a separar erro de negócio de erro de implementação A2A.

## Transcrição

00:01

Pessoal, bem-vindos. Na aula passada nós exploramos como construir um cliente H2A.

00:06

Agora vamos inverter os papéis.

00:08

Vamos construir o nosso próprio servidor H2A do absoluto zero.

00:11

E nesta demonstração veremos primeiro o protocolo no braço, puro.

00:18

E depois aplicaremos a abstração oficial do SDK, plugado a uma LLM real.

00:24

Bem, aula de laboratório, essa agenda é muito prática.

00:27

A gente vai ver como construir um servidor H2A.

00:30

Com uma implementação primeiro minimalista,

00:34

Vamos entender o ciclo de vida inegociável de uma task na versão 1.0,

00:39

Depois vamos subir o nível utilizando o TaskUpdater oficial do SDK e

00:44

Por fim testaremos tudo isso usando nossa interface visual simulando o cliente real.

00:50

Então, para o servidor H8Way ser válido,

00:52

Ele não pode simplesmente devolver uma string,

00:55

Ele tem uma responsabilidade contratual de gerenciar o estado da tarefa.

00:59

Então, como veremos nesse código minimalista,

01:02

Precisamos avisar que recebemos a task, sinalizar que estamos trabalhando,

01:07

Acionar a inteligência artificial,

01:09

Anexar o artefato resultante e declarar o fechamento.

01:15

Escrever todos aqueles eventos em queue e na mão é cansativo e sujeita a erros.

01:20

E o SDK versão 1.1 nos dá a classe TaskUpdated.

01:27

E abstraem os eventos do protocolo e nos deixam focar apenas

01:30

Na lógica de negócios e na chamada da nossa IA.

01:34

Resumindo, as chamadas de estado em .startWork, .addArtifact e .complete.

01:43

Vamos então para o código, tá bom? Vamos lá.

01:50

Aqui, pessoal, aqui

01:56

É o seguinte, vamos lá. Então...

02:01

Para essa primeira demonstração, nós criamos o que chamamos de servidor minimalista.

02:06

Ele é basicamente um servidor de eco.

02:08

Ele pega o seu texto e devolve em letras maiúsculas.

02:11

Não tem inteligência artificial aqui ainda.

02:14

O foco absoluto nesse momento é entender puramente o encanamento,

02:18

A estrutura, a base, o pipeline, no caso, do protocolo.

02:22

Então, vamos aqui na 143. Vamos descer aqui um pouquinho.

02:40

Aqui a gente tem o Agitcart, tá, pessoal? Olha que bacana, né?

02:45

E aqui a gente tem...

02:48

Então, o servidor precisa de uma fundação, né? Então,

02:53

Aqui nós temos a montagem das peças de infraestrutura,

02:56

Ó. O in-memory task store, para guardar o estado das requisições, tá?

03:01

O nosso echo executor, né? Vamos dar uma olhada nele, tá?

03:07

Ele, basicamente, ele pega a mensagem, tá?

03:12

E texto, vai lá e faz um upper nela, tá bom?

03:16

O default request handler, vamos botar aqui,

03:22

Que amarra tudo com o nosso agent card, tá? O agent card tá aqui,

03:28

Que a gente viu também, tá? Ele aqui.

03:32

E por fim, entregamos nossas rotas para o framework e Starlet.

03:37

É um boilerplate clássico, tá? Mas que garante a robustez da API. Agora...

03:49

Interessante aqui, nesse Identity Card. Identidade do nosso agente.

03:55

Isso aqui é a identidade do nosso agente. Então, é aqui

04:01

Que o servidor grita para a rede. Eu me chamo EcoAgentMinimal.

04:05

Esse aqui é o nome.

04:08

Recebo e devolvo o texto.

04:10

Recebo e devolvo o texto. Está aqui.

04:15

Opero via JSON RPC.

04:17

Está aqui. E possui a skill Echo. Está aqui.

04:25

É graças a esse card que o Cliente A2A sabe exatamente com quem está conversando.

04:30

Agora vamos dar uma olhada aqui.

04:34

Agora olha o Echo.

04:37

Que é de fato o nosso verdadeiro coração do servidor.

04:43

Ele bate aqui. Dentro do método Echo execute.

04:48

Aqui dentro. Vamos lá.

04:53

Bem, preste muita atenção nessa coreografia.

04:56

O Lafayette Sarkozy exige uma sequência de eventos muito estrita, tá?

05:01

E nós estamos fazendo isso no braço,

05:04

orquestrando a fila em cinco passos explícitos. O passo um,

05:09

que é a task, tá? Olha só, o passo um é a task.

05:12

Aqui é o passo um. Estou criando a task, né? Lembra que a task é o que fica,

05:17

é de verdade quem guarda o estado do que está acontecendo, tá?

05:21

E a regra manda que sempre devemos criar e enfileirar a task no começo.

05:26

Isso diz ao cliente, recebi e registrei a sua intenção.

05:29

Foi lá e enfileirou.

05:32

Segundo passo, disparamos o evento de status alterando para o Work.

05:36

Agora eu peguei a task,

05:38

está aqui o Task ID, e estou mudando o status para o Work.

05:41

E estou passando uma informação aqui de processando.

05:47

O terceiro passo é a execução da lógica de negócio. Aqui, apenas um upper no texto,

05:52

mas no mundo real é aqui que a LLM entra em ação.

05:55

Então, aqui a execução, aqui apenas um upper,

05:57

mas a LLM entra em ação aqui. O quarto passo é o Artifact.

06:03

O trabalho gerou um resultado, nós enfileiramos um Artifact.

06:07

É a entrega do pacote final.

06:10

Então, a gente cria o Artifact e

06:13

envia.

06:18

E o

06:22

quinto passo é o Completed.

06:25

Sinalizamos o status terminal de Completed, missão cumprida.

06:29

Veja que não é apenas cuspir uma string de volta,

06:32

é orquestrar uma máquina de status assim que não é perfeita.

06:35

Eu vou inicializar o servidor para

06:40

a gente poder ver ele em ação.

06:43

Pessoal, eu já tinha inicializado o Streamlit.

06:48

Como vocês podem ver, nenhum servidor 8-way consegue enxergar ainda.

06:53

Mas vamos dar uma olhada aqui. Vamos fazer esse negócio acontecer.

06:57

Vou inicializar o servidor.

07:00

Esse 8-way serve agora.

07:04

Ele inicializou na porta 90.

07:08

Vamos dar uma olhada.

07:10

Agora aqui eu vou dar um refresh na tela.

07:13

Bem, ele já identificou o servidor. Ele fica lendo, já identificou o servidor.

07:18

Está aqui o AgitCard, exatamente como a gente tinha feito lá atrás.

07:23

Está aqui o AgitCard bonitinho, com skill e tudo mais.

07:29

Vamos ver aqui. Bom dia.

07:36

Ele retornou com tudo, maiúsculo. Agora vamos ver aqui.

07:40

Bem, o

07:44

cliente enviou a mensagem,

07:46

fez o pull e acompanhando os eventos de work de completed.

07:52

E recebeu o nosso artefato final com texto em maiúsculas perfeitamente.

07:59

Recebeu bonitinho, perfeitamente. Beleza?

08:03

Agora, vamos subir o nível, pessoal.

08:08

Vamos subir o nível. Agora é o seguinte.

08:21

Escrever cinco chamadas explícitas de ponto em que o event,

08:25

que é o que a gente fez ali.

08:26

Está vendo? Em que o event aqui, colocando todas as informações.

08:33

com todas essas constantes, ela funciona? Claro, vocês viram que funciona. Agora,

08:37

ajudou a entender o protocolo? Também, né? Mas no dia a dia, cara,

08:41

não é o que a gente deveria usar,

08:45

porque é propenso a erros, principalmente, tá?

08:49

Então, vamos subir o nível e ver como se faz um código de produção.

08:54

Aqui nós vamos apresentar, aqui nós apresentamos o TaskUpdater, tá?

09:00

Ele é um helper fornecido pelo... Vamos ver aqui. TaskUpdate. O

09:12

TaskUpdate, pessoal, ele é um helper. Uma helper class fornecida pelo SDK.

09:17

E a regra de ouro do protocolo da versão 1.0 se mantém.

09:20

Nós ainda criamos e enfileiramos a task manualmente como o primeiro passo.

09:24

Então, aqui. Vamos dar uma olhada aqui.

09:29

A gente cria a task. Olha lá. EventKeyway.

09:38

EventAdScoreKeyway. E aí, eu adiciono a task.

09:41

Beleza, é

09:44

manualmente então aí, assim, então vamos lá, é então

09:48

a gente, a gente, nós inicializamos e

09:50

passamos a fila de eventos e os aí diz da TESC e do contexto, tá? Beleza, o

10:07

teste update. Olá, eu evento, o agir da TESC e o contexto, tá bom? E

10:15

ele encapsula tudo isso para gente, tá? Ó, desse eu vou

10:20

e agora todo aquele boilerplate de antes só abstraído para três

10:23

metros extremamente limpos, né, que é o update start work,

10:29

né? Aí ele faz aqui, ó, update de artefato, update

10:35

complete, né? E, obviamente, se der problema, pede para você, que isso tá bem.

10:41

Agora, vamos

10:45

Agora nós vamos apenas trocar o alvo. O que eu vou fazer, pessoal?

10:49

E agora a cereja do bolo.

10:51

Onde tínhamos um simples ponto upper,

10:53

nós plugamos

10:59

uma chamada de verdade por uma LLM.

11:02

E esse é o grande insight arquitetural do 8-way.

11:04

O ciclo de vida é totalmente agnóstico da inteligência.

11:07

Nós removemos o código determinístico,

11:10

plugamos o MI-A generativo no meio do pipeline,

11:12

e as bordas não precisam mudar absolutamente nada.

11:16

Então, deixa eu inicializar esse outro servidor aqui. Deixa

11:25

eu copiar aqui, tá, pessoal? Ele vai dar aqui no controle.

11:47

Deixa eu ver se está baixinho, certo. Agora sim.

12:15

Se eu voltar aqui no Strelitz, agora ele também enxerga.

12:19

O segundo tá e também enxerga o segundo o

12:23

Segundo a gente que tá na segunda porta então

12:31

Ó agora nós nós trocamos apenas o alvo do

12:35

Nosso cliente tá descoberta ativa já atualizou o

12:37

Card tá com vocês podem ver aqui beleza é e vamos colocar um texto lá ó o

12:46

Que é um e-jet card 10 palavras vamos colocar aqui ó nesse

12:57

Caso é o cartão de dedicação profissional usado por

12:59

Agentes imobiliários e vendedores tá Está aqui.

13:02

O que é indicar dentro do

13:05

Contexto do

13:07

Protocolo

13:11

A2A?

13:15

Indicador digital que apresenta um agente A2A. Beleza. Então,

13:19

Vamos dar uma olhada aqui no Lifecycle.

13:22

Mesma coisa. Está vendo? Test Completed. E aqui o resultado.

13:27

Beleza, pessoal? Então, essa foi a nossa aula de hoje aqui. O walkthrough no código.

13:34

Espero que vocês tenham gostado.

## Resumo IA

[RESUMO_IA]