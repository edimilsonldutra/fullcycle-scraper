Módulo: DevOps e SRE com IA\
Aula: [Demo Prática pt3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18545)

## Resumo da aula



## Transcrição

00:00

Ok, o chat começou a gerar aqui.

00:03

Ação pendente registrada com sucesso.

00:05

Então ele registrou uma ação de pendente lá, aguardando aprovação humana.

00:08

Modo Copilot, requer aprovação. Legal? Ação proposta.

00:13

Ele vai fazer um rollout aqui do serviço.

00:15

Rollout restart e assim por diante.

00:17

Blast Rails, justificativa, próximos passos. Incidente,

00:21

MCP, approve action. Então a gente consegue mandar essa aprovação aqui.

00:26

Incidente MCP, reject action, motivo da rejeição. Então,

00:32

a gente consegue aprovar e rejeitar aqui qualquer ação. Tá bom? Então,

00:36

registramos lá um blast grade certinho. E agora,

00:41

a gente vai aprovar essa ação. Então,

00:45

aprove a ação pendente com

00:52

id, vamos copiar,

00:55

action, isso aqui.

00:58

Como? Ah, vamos colocar só assim, tá bom.

01:02

Aprova a ação pendente com id, alguma coisa. A gente vai enviar,

01:07

o modelo vai chamar o approve action no incident,

01:09

MCP e a ação aprovada registrada no log.

01:12

Então a gente vai registrar isso aqui no log.

01:15

Approved by human, executando o how to restart.

01:18

Então ele tá fazendo um restart da nossa aplicação lá. Vamos ver ela restartando?

01:26

Ó, fez o restart aqui, porém não...

01:31

Deployment restart. O restart foi iniciado.

01:34

Agora vou verificar o status do rollout e monitorar a recuperação dos pods.

01:43

Executando o kubectl rollout status.

01:46

Vamos esperar um pouquinho aqui para ele fazer o restart. Vou

02:00

dar um pause aqui até ele terminar. Essa ação aqui já volta.

02:05

Então aqui ele gerou a resposta, tá bom? Do que a gente pediu para lá.

02:10

Ele reiniciou o serviço. Vou mostrar para vocês aqui.

02:15

Então, se a gente vier aqui nos serviços, ele reiniciou.

02:20

Aqui, três minutos, etc. Ele conseguiu reiniciar o serviço,

02:24

porém, ele não conseguiu resolver o problema,

02:27

né? Porque só reiniciar não vai resolver o nosso problema aqui. Entendeu?

02:32

Então, vamos verificar se os SLOs aqui foram restaurados.

02:37

Vamos pedir para ele fazer essa verificação.

02:40

Então, verifique.

02:43

Verifique se...

02:47

Se os SLOs foram

02:51

restaurados.

02:57

Vamos ver se ele vai verificar aqui.

02:59

Se o SLO foi restaurado.

03:04

Executando aqui. Assim que começar a responder, eu volto.

03:10

Então ele já começou a fazer as consultas aqui.

03:12

E está vendo que... Inclusive já fez aqui.

03:18

Ele falou que inclusive o próximo passo que eu ia fazer,

03:21

ele já fez automaticamente. E removeu a fault injetada aqui.

03:25

Então eu vou lá, removeu a fault e agora ele vai fazer a parte final aqui,

03:30

que é olhar se o SLO está funcionando. Se a gente vier aqui,

03:35

a fault está aqui ainda. Ah não, está aqui não.

03:41

Terminei e sumiu. Ele reiniciou de novo e sumiu. A fault foi removida.

03:46

Então a gente tirou o problema lá que a gente criou.

03:49

A gente pediu para ele verificar se as acelerações foram restauradas.

03:53

Ele automaticamente teve a capacidade aqui de remover o problema. Legal?

04:00

Então ele viu que tem a disponibilidade de remover o problema,

04:05

de ajustar o problema. Ele já conseguiu fazer isso.

04:09

Então vamos ver o que ele vai terminar de responder para a gente aqui.

04:13

Ele está dando um describe pod, está dando um to query aqui.

04:22

Todos os pods estão como run e, no entanto, notei que há uma variável de ambiente.

04:25

Ele está casquetando com essa variável de ambiente aqui.

04:29

Veja, gente, em todos os pods.

04:30

Vou verificar se isso está causando algum problema e tentar

04:33

buscar a métrica de disponibilidade de SLO completo.

04:35

Ele está fazendo algumas queries aqui para validar para

04:38

a gente se isso está acontecendo algum problema.

04:40

Se está gerando algum problema.

04:41

Apesar que essa variável não deve existir,

04:43

mas ela não gera nenhum problema para os nossos pods,

04:45

não. Os pods já estão... up lá e saudáveis.

04:48

Vamos esperar ele fazer o retorno aqui pra gente.

04:51

Tá processando alguns prompts aqui. Porque o chat tá muito grande,

04:55

né? A gente tem um chat muito grande aqui já.

04:57

Então os prompts já estão sendo processados aqui.

05:04

Vamos esperar um pouquinho e assim que ele terminar

05:06

de processar eu retorno aqui com vocês.

05:10

Ele tá continuando a geração aqui.

05:13

Falando que o nosso pode tá ruim e notei que ainda ele tá com

05:20

ainda com problema nesse crash loop inject aqui.

05:26

Ele está fazendo mais algumas verificações para o SLO, olha

05:31

lá, target API, prometeu os valor 1, verificar o status final do deployment,

05:35

então aqui ele faz algumas chamadas aqui para ver como é que está o deployment,

05:40

se tem algum problema, e

05:46

SLO restaurado com sucesso. Então o status atual do API está aqui, running, true.

05:55

Está aqui falando que o nosso cara está ativo. Result count zero.

06:01

Total de potes. Aqui alguns status do SLO.

06:04

E ele está construindo o restante da resposta aqui para

06:08

a gente que o nosso ambiente agora está saudável. Legal?

06:13

Então a gente tem o SLO P95 aqui, que é requisito 200 milissegundos.

06:18

Status atual atendido. Então está funcionando tudo.

06:24

corretamente é basicamente a gente conseguiu fazer um troubleshoot aí né de ponta a

06:30

ponta de um serviço poderíamos fazer com

06:34

outros serviços aí também se a gente notar

06:37

vamos aqui abrir o nosso link fusing

06:39

tracers a gente tem aqui as sessões

06:44

essa sessão aqui eu acho que é que tá sendo feita agora 1h32 são 21h57

06:53

17 .1 .32, dia 16, deixa eu ver, parece que tá atualizado não.

07:02

Tracers... A

07:07

gente tem todos os tracers aqui no OpenRBI,

07:11

que a gente consegue ver os nossos chats aqui.

07:16

Deixa eu pegar qual que é o tracer atual.

07:25

Hum, estranho, parece que o tracer não tá caindo aqui.

07:29

Pode ser algum problema.

07:33

Vamos verificar se ele tá sendo chamado.

07:37

Vamos verificar se ele está ativo primeiro, né?

07:39

Antes de a gente dar uma olhada lá. Painel do admin. Funções. Ah!

07:45

Olha o danado aqui, ó. Está desativado. Que ótimo, hein?

07:50

Então a gente não tem tracer para essa aqui.

07:53

Podemos fazer um teste aqui de mandar mais um novo prompt

07:59

para ver se ele consegue gerar esse tracer para a gente.

08:04

Vamos abrir aqui um novo chat. Vamos verificar.

08:07

Vamos fazer a primeira pergunta lá,

08:09

só para a gente pedir para ele verificar o status.

08:14

Deixa eu pegar esse aqui que eu já tenho digitado.

08:17

E vamos pedir para ele fazer um testezinho aqui.

08:20

Só para a gente validar se nossos traces com o LingFuse estão ativos.

08:24

Só um ponto, gente. Fiquem sempre de olho,

08:26

porque se esse aqui ficar desativado e não tiver como global aqui,

08:31

a gente tem a opção global ativa.

08:33

O tracer não envia lá para o LingFuse.

08:36

Então é sempre bom a gente ficar de olho nas nossas configurações do ambiente.

08:41

Então esse chat que a gente tem aqui, o chat vai estar guardado,

08:44

a gente consegue ver via banco de dados dele e assim por diante.

08:48

Porém, não está o tracer feito lá dentro do nosso LingFuse.

08:51

Tá bom? Vamos ver se ele iniciou esse tracing aqui agora. Vamos

09:00

dar uma olhada. Em

09:03

teoria era para ter iniciado.

09:07

Ele está rodando aqui algumas tools. Vamos verificar.

09:17

Vamos ver aqui no painel do Jimmy.

09:19

Tracer está ativo.

09:21

Está aqui certinho com as nossas credenciais do LingFuse,

09:24

que a gente já tinha definido. Final 43, vamos validar nossas credenciais aqui.

09:34

Final 47C, final E43, está bom. Credencial está certinha.

09:40

E43, 47C. Está aqui certinho as nossas credenciais.

09:47

Vamos ver lá.

09:50

Se nós temos o nosso tracing aqui, pronto.

09:56

É, o tracing não está caindo aqui não.

09:58

A gente dá uma revisada nessa parte do tracing aqui.

10:01

Realmente ele não está fazendo o envio. Vou dar uma olhada.

10:10

Vou dar uma olhada aqui.

10:13

E verifico porque ele está acontecendo. Essa parte do tracing não fazendo o envio. Ok?

10:22

Vamos abrir o nosso código. Que junto com vocês.

10:27

Aí a gente já faz essa verificação.

10:33

Versões. Vamos abrir aqui. Nós temos aqui um inlet. Filter.

10:47

Filter. Outlet.

10:51

Inlet. Estamos recebendo. Está recebendo o valve aqui. Tudo certinho. O

10:58

link do fio está no mesmo namespace.

11:05

Aparentemente está tudo certo aqui com o nosso...

11:10

com o nosso código.

11:12

Vamos dar uma olhada aqui nas configurações.

11:18

HTTP, LENGTHUSE, porta 3000.

11:22

Aparentemente tudo ok. Debug está habilitado aqui, mas não tem problema.

11:26

Aparentemente está tudo certo aqui. Era para ter enviado.

11:30

Esses são os problemas reais. Você configura e acaba que ele não envia.

11:36

Então pegar aqui 30 minutos, não tem nada. Generation,

11:40

não tem nada. Score, não tem nada.

11:43

Então, vamos dar uma verificada aqui.

11:45

Deixa eu dar uma verificada e ver se eu já encontro

11:48

a solução aqui para mostrar para vocês o que aconteceu. Tá bom?

11:54

Vamos fazer o seguinte, então.

11:56

Vamos encerrar essa demo, que a gente conseguiu ver tudo certinho,

11:59

porém a gente não conseguiu ver a parte de tracing.

12:02

Vou verificar o que está acontecendo com o tracing aqui,

12:04

ajustá-lo e mostro para vocês onde estava o problema e como que eu ajustei. Tá bom?

12:10

Pra ficar claro aqui para todo mundo por que que não

12:12

tava sendo enviado o tracing lá para o nosso LingFuse.

12:16

Ok? Então é isso, pessoal. Eu volto em breve aí com a nossa próxima demo.

12:20

Então a nossa próxima demo a gente vai falar

12:22

aqui do Kill Switch mais Governança Cycle. Ok?

12:26

Então, um abraço. Daqui a pouco eu tô de volta aí com a nossa próxima demo.

## Resumo IA

[RESUMO_IA]