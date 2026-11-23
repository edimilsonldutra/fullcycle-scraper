Módulo: Protocolos de Comunicação\
Aula: [LAB: Explorando Agent Cards](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18617)

## Resumo da aula

O laboratório sai da teoria e entra no tráfego real de protocolo: dois agentes de e-commerce sobem localmente, publicam seus contratos e recebem chamadas A2A de verdade. O ambiente depende do A2A SDK na versão 1.1, além de LangGraph e Streamlit para a camada de orquestração e visualização. Como os testes usam modelos reais, o .env precisa conter uma chave de API válida; sem isso, o fluxo falha antes mesmo da integração entre agentes. O uso de uv acelera instalação e execução, o que reduz atrito em um lab com múltiplos processos.

A pasta source concentra os agentes especialistas, mantendo o código de domínio separado dos clientes de teste e orquestração. Já a pasta client contém um script de baixo nível para chamadas JSON-RPC diretas e scripts mais altos para coordenação multiagente com LangGraph e Streamlit. Essa separação importa porque permite validar o protocolo em duas camadas: primeiro a borda A2A pura, depois a composição assistida. Quando o teste falha, essa divisão ajuda a localizar se o problema está no contrato do agente, no transporte ou na orquestração.

O cenário usa dois processos independentes, um para logística na porta 9001 e outro para estoque ou suporte na 9002, reproduzindo a mesma separação que seria usada com containers em produção. A semelhança arquitetural com AWS ou GCP não está no provedor, mas no isolamento entre serviços e no contrato público exposto por cada agente. Se aparecer address already in use, o problema não é do protocolo, mas do ambiente local; lsof -i :9001 ou equivalente resolve o conflito identificando o processo ocupando a porta. Esse tipo de debug operacional é parte da conformidade prática do lab, porque um agente indisponível invalida toda a cadeia de descoberta.

Retomando a descoberta padronizada já conhecida, o ponto crítico aqui é a mudança de rota mencionada no laboratório. O caminho esperado passa a ser /.well-known/agent-card.json; usar variantes antigas como agent.json quebra a descoberta automática e normalmente retorna 404. A mudança parece pequena, mas afeta qualquer cliente, script de teste ou orquestrador que dependa da convenção exata. Em protocolo, nomes de rota fazem parte do contrato tanto quanto os campos do JSON.

O Agent Card já foi definido anteriormente; o avanço aqui é tratá-lo como contrato executável que precisa refletir a capacidade real do agente. No laboratório, o array de skills começa vazio e deve ser preenchido com a skill rastrear-pedido, alinhando o que o agente anuncia com o que ele realmente processa. Se o nome da skill estiver incorreto, o problema não aparece só como erro semântico: ele pode impedir descoberta útil, roteamento correto e testes automatizados. Orquestradores não inferem intenção do código-fonte; eles leem o contrato publicado.

O discovery.py existe para mostrar o protocolo sem abstrações de framework na borda do cliente. O fluxo começa com sendMessage, enviando a mensagem do usuário dentro de params, e continua com polling em getTask até a Task sair de submitted ou working para completed. Isso evidencia que a resposta final não precisa vir na primeira chamada e que o resultado formal aparece em artifacts, não perdido no histórico conversacional. A alternativa para esse acompanhamento seria streaming ou webhook, já vistos antes; aqui o foco é dominar o caminho mais explícito para inspeção manual e debug.

A primeira resposta do servidor não entrega o rastreio pronto; ela devolve a identidade da execução para que o cliente acompanhe o lifecycle. O polling em getTask deve observar status.state até o estado terminal esperado, sem assumir que o processamento será instantâneo. Quando a Task completa, o dado útil precisa estar no artifact, porque esse é o entregável consumível por outros sistemas do fluxo. Se o cliente procurar o resultado apenas em mensagens intermediárias, a integração fica frágil e desalinhada com o contrato do protocolo.

Retomando o mesmo cenário de logística e estoque, a camada com LangGraph não substitui o protocolo; ela automatiza a decisão de qual agente chamar e em que ordem. O Streamlit entra como superfície visual para observar esse encadeamento, o que facilita validação funcional e demonstração do fluxo multiagente. Essa composição só funciona de forma previsível porque cada agente publica um contrato legível por software e responde de forma consistente ao ciclo de Task. O ganho arquitetural está em trocar coordenação ad hoc por orquestração baseada em contratos públicos.

O script verify_lab.sh sobe os agentes em background, espera a disponibilidade das portas, valida a publicação dos Agent Cards e executa testes end-to-end com pytest e o pipeline de discovery. Esse tipo de automação transforma o laboratório em um teste de conformidade operacional, não apenas em uma execução manual bem-sucedida. Se o resultado esperado não vier, o primeiro suspeito costuma ser typo em skills, rota incorreta do card ou falha de inicialização do ambiente. Um “4 de 4 verde” significa que descoberta, execução e consumo do resultado estão coerentes ponta a ponta.

Um executor A2A precisa respeitar a ordem dos eventos: o primeiro item emitido deve ser a Task, e só depois podem vir atualizações de estado. Se o agente emite working mas nunca publica completed, o cliente fica preso em polling infinito, o que denuncia erro de implementação e não de transporte. O bloco try/except em execute evita que exceções internas virem silêncio operacional, convertendo falhas em failed observável pelo cliente. Além disso, o método cancel deve existir mesmo quando a lógica de cancelamento ainda não foi implementada, porque a conformidade da interface também faz parte do contrato.

A passagem das versões iniciais para a linha 1.x afeta a implementação porque o Agent Card passa a expressar mais de uma interface, além de suportar extendedAgentCard e modos padrão de entrada e saída. Múltiplas interfaces permitem expor bindings diferentes sem duplicar a identidade do agente. O card estendido resolve o problema de catálogos públicos incompletos em ambientes empresariais, onde certas skills só devem aparecer para clientes autenticados. Já defaultInputModes e defaultOutputModes reduzem ambiguidade sobre MIME types aceitos e produzidos, o que melhora interoperabilidade antes mesmo da primeira chamada.

## Transcrição

00:00

Pessoal, agora nós vamos para o lab,

00:03

e nesta etapa nós vamos rodar o laboratório completo.

00:09

Então, notem que não estamos usando agentes genéricos de resumo,

00:13

estamos seguindo o nosso cenário de e-commerce dos demais labs.

00:17

O primeiro passo é o setup,

00:19

instalando o SDK, depois vamos subir os dois departamentos,

00:22

que é a logística na porta 9001 e o suporte na 9002.

00:25

E no passo 3, provamos que eles serão...

00:28

que eles estão vivos inspecionando os agent cards.

00:31

E no passo 4, sujamos as mãos, tá? No bom sentido, né?

00:35

Usamos o discovery.py para fazer requisições A2A puras usando o JSON-RPC,

00:40

que é o SendMessageGetTask. E no último passo,

00:43

elevamos o nível, conectamos um orquestrador construído em LingGraph,

00:47

rodando no Strelit,

00:49

que vai coordenar chamadas para esses dois agentes automaticamente.

00:53

Vamos lá? Bem,

00:56

então... Pessoal, qual é a grande sacada de hoje?

01:00

O protocolo Letway nada mais é do que a lógica de descoberta que vimos no MCP,

01:06

só que aplicada a interlocutores independentes e com memória,

01:09

que são os nossos agentes.

01:11

O agent card diz que ele é capaz e o JSON-RPC faz o handshake e gerencia a tarefa.

01:17

É uma dica de ouro para quem for tech lead. Quando construírem isso em produção,

01:22

não tentem modelar o envelope JSON-RPC ou o Zenon na mão.

01:28

Insisto no uso do SDK oficial do H2A,

01:30

que agora já está na versão 1.1,

01:32

inclusive, para brindar comunicação entre as equipes.

01:35

Então, os pré-requisitos para hoje incluem o nosso amado

01:38

H2A SDK atualizado para a versão 1.1,

01:41

mas além dele, precisamos instalar o Link Graphistry Elite,

01:45

que aqui nesse laboratório é usado para a gente poder ter...

01:49

uma melhor visibilidade do que está acontecendo.

01:52

Então, felizmente, já deixamos tudo pronto no requirements.txt para vocês.

01:56

Basta vocês também verem o readme lá. E além disso,

02:00

lembre-se, os laboratórios da setup não possuem mais versão mockable.

02:04

Na verdade, a gente precisa colocar a API real no .env.

02:09

Então, enfim, pessoal, a sugestão é pegar uma API da Antropico,

02:14

como eu fiz, uma API do modelo mais barato, funciona super bem.

02:18

E fico atento às mudanças na rota do agent card que ocorreu na versão 1.1,

02:22

né? Se vocês tentarem acessar /elnom/agent.json, né?

02:29

Vai dar 4004. O correto agora possui hífen, que é agent-card.json, tá?

02:36

Uma mudança simples, uma pequena mudança, tá?

02:39

Mas que no final impacta muito o resultado. Bem...

02:46

Aqui, pessoal, vamos nos familiarizar com o campo de batalha.

02:51

Note que para deixar o repositório dos padrões da indústria,

02:54

todos os códigos foram, fontes do laboratório,

02:57

foram encapsulados dentro dessa pasta source, como também nos demais labs.

03:01

Lá nós temos os nossos especialistas de e-commerce, que é a logística e estoque.

03:05

Na pasta cliente temos três arquivos.

03:08

Um script puro para rodar o JSON e o IPC no braço.

03:12

e dois scripts que rodam a extração multiagente de forma super robusta.

03:15

Usando o LangGraph e a interface visual do Streetlit.

03:20

Para fazer o setup, vamos usar a ferramenta UV, que é absurdamente rápida.

03:24

E como agora nossos testes validam com o sistema com LLMs de verdade,

03:28

não se esqueçam de configurar o .wav com a sua chave de API.

03:33

Aqui, pessoal, nós vamos dar vida aos nossos agentes de e-commerce.

03:38

Lembre-se que os arquivos agora ficam dentro da raiz só, como eu já falei.

03:42

Então, abram dois terminais separados. No primeiro,

03:46

subiremos a logística na porta 9001 e no segundo, o estoque 9002.

03:53

E uma dica clássica, tá? Se vocês tomarem o erro address already used,

03:57

significa que tem algum outro laboratório rodando nessas portas.

04:01

Talvez vocês esqueçam do módulo passado ligado. Então, use o comando...

04:09

LSOF -i :9001 para descobrir quem é e mate o processo, tá? Tipo assim.

04:14

O que estamos simulando aqui com os dois processos UV-Corn locais é

04:18

exatamente a mesma topologia que usaríamos em produção na AWS ou no GCP,

04:24

enfim, com dois containers independentes atrás de um load balancer.

04:27

A arquitetura é idêntica, tá?

04:30

Bem, e aqui está o documento de identidade do nosso agente logístico, o famoso Agente Card.

04:37

Se vocês derem um simple call na porta 9001,

04:41

no perfil padronizado, ele vai cuspir esse JSON para vocês.

04:44

Notem o campo name acusando que ele é o agente logístico.

04:49

Mas a verdadeira mágica acontece no array de skills.

04:52

O código inicial do laboratório de vocês está com o array vazio. Tem tudo lá, tá?

04:58

E a missão de vocês é justamente inserir o skill para o ID Rastrear.

05:02

Com ID Rastrear pedido.

05:04

Lembre-se da regra de ouro que vimos na teoria.

05:07

É este JSON que atua como contrato universal.

05:10

O orquestrador não faz a menor ideia de qual

05:12

linguagem vocês usaram para programar a logística.

05:15

Ele simplesmente lê o Agent Card e entende na hora que

05:18

o agente aceita JSON RPC e sabe fazer rastreio.

05:22

E aqui a gente chega no coração da aula, que vocês estão vendo na tela,

05:26

o gateway puro, sendo dissecado através de um simples comando curl.

05:31

É aqui que vocês entendem que não tem mágica.

05:34

É só JSON ou RPC trafegando sobre o HTTP.

05:37

A primeira etapa é invocar o método sendMessage.

05:39

Note a estrutura.

05:41

Envelopamos a mensagem do usuário perguntando sobre o pedido 123

05:44

dentro da propriedade params e batemos na porta da logística.

05:49

O servidor não nos dá a resposta final.

05:52

Ele nos devolve a task no estado task underscore state underscore submitted.

05:57

E a segunda etapa?

05:59

Nós entramos em um loop de pooling chamando o método getTask

06:02

até que o status .state mude para task .state underscore completed.

06:08

Quando isso acontecer, o resultado não virá solto,

06:11

ele virá fortemente tipado dentro de um artifact.

06:14

A missão de vocês no laboratório é abrir o discovery.py e

06:18

codificar exatamente essa estrutura de um NPC no Shudu 1 e 2.

06:23

E para fecharmos a etapa prática do nosso laboratório 2A puro,

06:27

com chave de ouro, temos o nosso script de verificação automatizado.

06:32

Enfim, que é o verify underscore lab ponto sh.

06:37

O que esse script faz? Ele sobe os dois agentes da background,

06:40

pinga a porta destes aguardando os JSONs dos agent cards e depois

06:44

roda todo o nosso ecossistema de testes end-to-end com o PyTest.

06:47

E o pipeline do discovery, obviamente.

06:50

Se o terminal de vocês baterem 4 de 4 verde, sintam-se abraçados, tá?

06:56

Vocês acabaram de provar que conseguem conectar múltiplos agentes

06:59

conversando via JSON RPC de forma padronizada.

07:02

Se não passar, dê uma olhada atenta e se não sobrou nenhum typo no nome das skills,

07:08

tá? E com isso a gente termina o módulo 5.

07:11

E para fecharmos nossa aula, antes de colocar a mão na massa,

07:14

eu trouxe um cheat sheet de debug,

07:17

tá? Esqueceu um agente rodando na outra aula, mata a porta 9001.

07:22

Não ativou o .env ou não rodou o uvicorn install,

07:26

o Python não vai gritar que não acha o SDK.

07:30

Está tomando 404 no edit card? Lembre-se do if agent-card.json.

07:35

O discover.py ficou no loop infinito?

07:40

Certeza que no código de seu agente você enfileirou o evento de working,

07:45

mas esqueceu de enviar o evento final completed no agent executor.

07:49

Tomou a temida invalid agent response error?

07:53

A especificação A2A V1.0 é linha dura. No padrão B,

07:58

o absolutamente primeiro evento que o seu agente deve

08:02

cuspir na fila é o objeto task.

08:04

Você não pode mandar um status update antes de declarar qual é a task.

08:08

Se fizer isso, o SDK quebra sua resposta para proteger o cliente.

08:15

Agora, pessoal, a gente vai dar uma olhada debaixo do capô.

08:18

A especificação 8-way evoluiu da versão 0.3,

08:21

que era o rascunho, para a versão 1.0,

08:24

que é production-ready. O que mudou na anatomia do identificar,

08:27

que afeta a forma como codificamos, primeiramente,

08:33

é o suporte de interface.

08:38

Antes, o agente só tinha uma URL global.

08:41

Agora ele pode falar de JSON RPC com RL e JRPC em outra.

08:46

O cliente que se vire para escolher.

08:49

Segundo, a flag extended agent card. Em cenários empresariais,

08:53

como faremos no módulo 6,

08:55

o agent card público esconde as skills secretas e o

08:59

cliente autenticado pode pedir o card estendido com o catálogo completo.

09:05

E terceiro, que é o default input modes e o default input modes.

09:10

Agora a gente deixa claro quais MIME types,

09:14

como text/plain ou application/json,

09:18

ele aceita mastigar e que ele vai cuspir de volta.

09:21

E para fecharmos a teoria do lab,

09:23

se vocês estiverem fazendo code review de agent A2A nas empresas de vocês,

09:28

esse é o checklist de ouro. Número 1,

09:30

se o desenvolvedor enfileirar qualquer coisa antes de enfileirar o event task,

09:34

reprove a PR. Número 2. Nada de inventar estado como processando o passo 2.

09:40

A especificação exige os 8 estados fixos. Se quiser detalhar o que está rolando,

09:45

use o campo de texto do status update.

09:48

Número 3. Sempre blindem o execute, tá gente? Como com o bloco de try-except.

09:54

Garantindo que se tudo explodir,

09:56

A gente avisa o cliente com o task state failed. E número 4,

10:01

O método cancel é obrigatório,

10:03

Mesmo que seu agente não saiba como abortar a

10:05

operação e a função fique só com o pass.

10:12

Se você declarar o método, o servidor nem compila.

10:16

Pessoal, então chegamos ao final do nosso laboratório, tá?

10:19

E eu vou repassar agora com vocês.

10:21

Obviamente, vocês vão dar uma pausa no vídeo.

10:24

Eu vou voltar lá para o código, tá? Mas antes de eu ir para o código, pessoal,

10:27

Eu quero que vocês levem para casa e apliquem nas empresas de vocês amanhã de manhã, tá?

10:32

Nós subimos dois especialistas de e-commerce usando o 8-way SDK atualizado.

10:36

Nós vimos como a especificação força é descoberta através de agent card,

10:41

agent-card.json.

10:44

Que obrigou a gente a usar o ré dentro em baixo e como diz o RPC e

10:49

fui, é fui no sem mestre de para o get task e mais do que isso nós, nós

10:54

pegamos essa complexidade inteira usando o orquestrador do link greve.

10:57

Lembre-se na nossa frase âncora para o

11:00

mundo, muita gente antes de você se preocupar qual usar,

11:03

preocupa-se com o protocolo, tá bom? É

11:08

isso aí pessoal, agora, né? É

11:11

É o momento em que eu vou migrar para o IDR e nós vamos continuar de lá, tá bom?

## Resumo IA

[RESUMO_IA]