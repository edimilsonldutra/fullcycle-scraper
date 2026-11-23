Módulo: DevOps e SRE com IA\
Aula: [Visão Geral, End-to-End, Arquitetura](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18541)

## Resumo da aula



## Transcrição

00:00

Ok, automação criada. E agora a gente vai desativar ela aqui também,

00:05

para a gente não precisar gastar recurso aqui à toa.

00:09

Tá bom? A outra aqui ainda está rodando. Meu computador começou a fritar de novo,

00:14

porque ela está processando muita coisa.

00:16

Então eu vou provavelmente parar a execução dela lá,

00:20

porque a gente tem muito...

00:22

Ela gasta muito recurso. Vou parar a execução, mas quero que vocês testem aí depois.

00:29

A execução desse cara agendado,

00:32

para ele te entregar alguns resultados ali de maneira automática. Ele inicia,

00:38

faz o processamento para você e te entrega o

00:41

resultado de tempo em tempo com essas automações.

00:43

Eu vou inclusive injetar aqui o meu modelo,

00:46

porque o computador aqui começou a rodar muito forte aqui,

00:50

não está aguentando rodar o modelo.

00:53

Mas acontece, nas melhores famílias. Vamos subir aqui o modelo de novo.

01:00

Download do modelo aqui. Vou pegar só o monitor de atividade aqui.

01:05

E ver como é que eu subi a requisição aqui.

01:11

Estava bem travado aqui mesmo. Ok.

01:16

Vamos criar a última automação aqui que é esse postmortem remember.

01:21

Ele vai criar para a gente um postmortem.

01:24

A cada nove horas ele vai gerar um postmortem para a gente aqui.

01:28

Se houver problema, né?

01:30

Vamos gerar aqui mais uma automação.

01:33

Nova automação. O nome dela é PostMortemReminder.

01:36

Vamos pegar aqui o texto dela, PostMortemReminder. O description dela.

01:43

Simples. E aqui o prompt. Tem

01:49

prompt aqui. Para evitar que ela faça muita operação ou algo do tipo,

01:55

vocês podem refinar o prompt.

01:57

Vocês podem dar uma melhorada nele para evitar que ela faça tanta...

02:03

Tanta coisa assim. Quando você colocar para rodar.

02:07

Então ela vai usar o Pós-Mortem Generator.

02:12

Cadê o nosso Pós-Mortem Generator? Está aqui. E vai executar a cada 9 horas aqui. Personalizado.

02:21

E criado.

02:22

Essa criou até rápido.

02:24

Criado aqui o nosso Pós-Mortem. Que vai executar a cada 9 horas. Ok?

02:30

Vamos também desativar ela. Porque a gente não precisa que ela rode agora. Então, pessoal,

02:34

criamos aqui toda a nossa infraestrutura para a gente chegar na integração completa,

02:40

que é a nossa demo lá do módulo 5.

02:44

Legal? Então, a verificação aqui de end-to-end,

02:47

a gente conseguiu simular um fault lá quando a gente criou

02:50

o nosso MCPL para inserir um problema dentro dos nossos pods.

02:55

A gente conseguiu configurar um SRE, Trace to Road, dentro do OpenMBY,

03:00

que ele consegue receber alertas e MCP, gerar alguns pós-mortems,

03:07

gerar algumas coisas que a gente precisa para fazer

03:12

o diagnóstico de algum problema dentro da nossa infraestrutura.

03:18

Basicamente...

03:22

A gente conseguiu pegar alguns incidentes, a gente consegue pegar

03:25

uns incidentes

03:26

com linguagem natural,

03:33

tá bom? Então aqui é bem possível a gente fazer com linguagem natural,

03:36

É bem legal a gente fazer isso, tá?

03:39

A gente conseguiu fazer uma consulta no Gnome de Base,

03:41

claro que a gente não rodou, mas a gente vai rodar no próximo módulo aí,

03:46

essa consulta no Gnome de Base, que a gente vai lidar, e a governança.

03:51

A gente tem a governança bem feita aí que a gente consegue

03:53

aprovar se ele vai tomar alguma ação de write dentro do nosso servidor.

04:00

Então, qualquer ação de write que ele for tomar dentro do servidor,

04:03

ele precisa de uma determinada aprovação lá dentro.

04:08

Criamos algumas automações, tá?

04:10

Só que essas automações eu vou fazer alguns testes com

04:12

ela aqui pra ver se a gente consegue refinar.

04:14

Só pra demonstrar como funciona,

04:16

porque senão o meu servidor não vai conseguir rodar meu...

04:20

Minha máquina local não vai conseguir rodar a parte do LLM,

04:23

tá bom? Porque demora bastante para gerar, que é muito contexto.

04:27

E o aluno vai revisar, editar e aprovar o pós-mortem aí no final,

04:33

tá bom? A gente vai fazer tudo isso lá na próxima aula,

04:36

ok? No próximo módulo.

04:38

Então essa verificação vai confirmar que está tudo pronto

04:41

para a nossa demo completa do módulo 5, tá bom?

04:45

Então, aqui a gente tem a arquitetura completa para o nosso módulo 5. Temos o Open UI,

04:50

que vai registrar tudo no LingFuse, vai chamar os nossos serviços de MCP.

04:55

Aqui está só via StreamHttp,

04:57

mas ele está chamando através de MCP-OLA também.

05:00

Vamos conseguir ver coisas dentro do Kubernetes,

05:04

prometer os incidentes do MCP, que a gente vai conseguir confirmar ou não.

05:11

uma ação de WART dentro da nossa infraestrutura e a gente vai ter um

05:16

fault injection ali para a gente propositalmente

05:21

inserir um problema dentro do nosso cluster,

05:28

dentro do nosso serviço. Então a gente vai conseguir diagnosticar,

05:31

ter governança e fazer um pós-morte no final do incidente. Beleza?

05:39

A gente aqui vai ter um Lengfuse Pipeline, que é um Dual Audit Track, ou seja,

05:44

a gente tem um audit lá que é do nosso incidente MCP,

05:47

lá também a gente consegue ver os audits,

05:50

tá? E a gente vai ter a observabilidade ainda dentro do Lengfuse.

05:56

Se a gente testar aqui,

05:58

deixa eu ver aqui aquele que a gente fez, ah, é esse cara aqui.

06:03

Posso ver os logs de auditoria do... do restart.

06:13

Vamos ver se ele vai retornar aqui.

06:15

Tudo certinho nos logs. Vamos validar.

06:21

Deixa eu ver se o serviço aqui está rodando.

06:25

Serviço não, né? O modelo.

06:27

Cadê o nosso LLM?

06:32

LLM Studio. Está rodando. Está rodando lá. Vamos esperar ele retornar aqui. Perdi.

06:41

Docker rollout. Log de auditoria. Ah, que legal. Então,

06:47

a gente tem que buscar o log de auditoria. Então, ele deu um get audit log.

06:50

A gente tem todo o registro de audit logs lá dentro do nosso pod,

06:54

dentro do nosso serviço de incidentes.

06:58

Então, a gente tem aqui ação recente, timestamping, action register,

07:02

que é o número da ação, rolling start e ação.

07:05

Tá bom? Então, a gente consegue ver tudo o que aconteceu dentro desse cara.

07:09

Podemos criar até, talvez, um...

07:12

um serviço de exportação para dentro de um data lake, onde a gente consegue tomar ações,

07:17

mostrar para auditoria, etc., o que foi feito e assim por diante.

07:21

A gente tem aqui que ela foi aprovada, o histórico adicional e assim por diante.

07:26

A gente consegue puxar tudo aqui certinho na parte de audit log aqui. Legal?

07:31

E ainda temos o link Fuse ali para a gente conseguir validar se precisar,

07:37

se for necessário também. E...

07:41

Passando aqui para o próximo slide,

07:44

a gente tem um pós-mortem 2.0,

07:46

que basicamente a gente vai ter a IA gerando 80% do conteúdo do pós-mortem.

07:52

Então temos aí uma geração de 80%

07:55

do conteúdo para você validar somente os outros 20%.

08:00

Então você vai conseguir refinar os outros 20% ali,

08:03

que é melhor do que fazer os 100%.

08:06

Bem mais fácil a gente fazer os 20% do refinamento do que

08:12

digitar todos os pós-mortem do zero, então você não vai ter esse

08:18

trabalho. O LLM mesmo vai conseguir fazer a geração para você pegar o

08:23

que ocorreu nas últimas 24 horas, criar um pós-mortem e te entregar então,

08:30

o que o LLM não vai fazer por você? Ele não vai

08:34

entender o contexto institucional. Então, se der um problema em alguma coisa,

08:39

qual é o risco da sua operação? Qual é o risco da sua empresa?

## Resumo IA

[RESUMO_IA]