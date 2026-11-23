Módulo: DevOps e SRE com IA\
Aula: [Kill Switch + Governance Cycle pt3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18543)

## Resumo da aula



## Transcrição

00:00

Então, vamos continuar, né?

00:03

Fazer aqui os testes dentro de um único chat,

00:05

para a gente ver o comportamento aqui do nosso ambiente, ok?

00:11

Primeiro, vamos aqui na área de trabalho, na parte do espaço de trabalho,

00:15

vamos editar nosso agent aqui de novo.

00:18

Já colocamos aqui, né? Já está tudo certo,

00:21

desativamos as automações, beleza. Já fizemos isso. Então, vamos lá.

00:25

A primeira coisa que a gente vai fazer é selecionar ele aqui de novo,

00:28

que ele saiu daqui da minha seleção,

00:30

e colocar um SRE troubleshoot aqui.

00:36

Então, vamos pedir para ele simular.

00:39

Simule um crash loop

00:45

back off no app API.

00:52

Vamos pedir para ele fazer essa simulação aqui.

01:08

Ok, tá fazendo aqui a simulação, retorno da simulação, fault injection,

01:14

ele já injetou aqui e já fez uma verificação pra mim de como que estão os pods.

01:21

Ok, simulação bem concluída, ele conseguiu aqui fazer a simulação, pegou aqui os pods,

01:26

a gente vê que todos os pods agora estão com crash loop backoff aqui.

01:32

Ok, vamos olhar lá no nosso Kubernetes como que ele está.

01:39

Olha lá. Estão todos aqui com Crash Loop backoff aqui agora.

01:46

Ok? Então vamos voltar e

01:49

ver o que a gente pode fazer para arrumar esse problema.

01:54

Depois que a gente fez isso, a primeira coisa que a gente vai fazer...

01:58

Ele já conseguiu diagnosticar o problema, né?

02:00

Então ele já fez aqui a segunda parte.

02:02

A segunda parte seria diagnosticar o problema,

02:03

mas ele já conseguiu fazer. Agora a gente vai ativar aqui. Ative.

02:10

O kill switch.

02:16

Desabilite o agent. Vou

02:20

pedir para ele desabilitar o agent aqui.

02:25

Está desabilitando.

02:28

Incidentes kill switch. Verificação de status.

02:30

Então agora ele não vai conseguir. Check kill switch.

02:35

Então agora ele está desativado. Tudo bloqueado.

02:38

Então a gente está com o agent aqui bloqueado para fazer qualquer tipo de ação.

02:44

Então, se a gente pedir para ele fazer um rolling restart

02:50

do app API deployment.

02:57

Vou pedir para ele fazer um rolling restart aqui do app.

03:03

Ação bloqueada, aqui o switch ativo.

03:06

Está vendo que dentro do mesmo chat ele consegue fazer as verificações necessárias?

03:11

Então, a gente está com... as ações todas necessárias.

03:15

Restart, tal, tal, tal. Bloqueada.

03:17

Porque o switch impede todas as operações automáticas.

03:19

Então agora eu não consigo fazer nada automático.

03:21

Isso é uma chave que você consegue desabilitar a possibilidade

03:26

de alguém ir lá e mexer no seu sistema.

03:28

Então é bom a gente ter essas chaves, botões do pânico, né?

03:32

Que a gente pode falar. Tipo assim, cara, ninguém vai fazer mais nada. Pá,

03:34

aperta esse botão. A gente sempre pode ter isso pra gente conseguir fazer...

03:39

Proteger o ambiente de alguma forma. Entendeu?

03:43

Vou pedir para ele desativar. Desative.

03:45

Ou Kill Switch.

03:58

Reabilite o agent.

04:00

Vou pedir para ele reabilitar o agent aqui de novo. Ok.

04:06

Agent reabilitado. Vou fazer um check.

04:10

Habilitado. Ativado. Ok.

04:11

Agora já viu ali. Pegou um código CTL.

04:14

Verificação do status atual do pod.

04:16

Ele ficou com o brush para registrar a mitigação. Então,

04:21

ele já registrou aqui que ele quer fazer um restart no backoffice.

04:27

Restart deployment, falei errado.

04:32

Então, o que a gente vai fazer agora?

04:36

A gente já verificou o status que o switch já está funcionando,

04:40

já habilitou. Então, registra e já registrou ali a ação.

04:45

Já registrou a ação que a gente tem.

04:47

Então, vamos rejeitar.

04:54

Rejeitar a ação.

04:58

Simples assim. Rejeitar a ação. Vamos pegar o númerozinho dela aqui. A ação.

05:05

Opa, ele pegou completo. Quero só o número dela. Esse número aqui.

05:09

Rejeitar a ação.

05:12

Act. Alguma coisa.

05:14

Mandei ele rejeitar aqui essa ação.

05:18

Ele vai agora...

05:20

simplesmente não fazer nada porque ele está rejeitando. Reject action.

05:25

Então, ele nem sempre vai fazer tudo que a gente pedir, que a gente pode rejeitar.

05:30

Então, nem sempre vai ser aprovado. Legal?

05:33

A gente pode fazer interações através de chat, por exemplo,

05:37

que tem a possibilidade de a gente compartilhar e

05:39

criar um chat compartilhado com todo mundo.

05:41

Se a gente criar um chat compartilhado com todo mundo, colocar lá as pessoas,

05:44

tipo assim, o aprovador. O aprovador é o Joãozinho,

05:47

quem pediu para reiniciar a Maria.

05:49

Aí a Maria fala reiniciar, aí o Joãozinho pode ir lá e responder, ok,

05:53

pode reiniciar. A Maria registra o Blast Rails e o Joãozinho pode falar,

05:58

ok, pode reiniciar. Legal? E a Maria não consegue pedir para reiniciar e nem dar ok,

06:05

porque você pode colocar isso tudo pronto,

06:07

você pode fazer verificações internamente.

06:09

Então a gente tem como compartilhar chats e ir

06:11

trabalhando assim num chat compartilhado com a equipe.

06:13

Dá para fazer também, é bem interessante.

06:16

Legal? Rejeitei. Então, registro pendente.

06:20

Agora vamos pedir aqui para ele registrar uma ação aqui.

06:26

Aqui, resumo completo da simulação. Simulação inicial,

06:29

tentativa de mitigação, ação rejeitada,

06:32

remoção da falha. Aqui está falando para remover a falha.

06:36

Remoção da falha, feito com sucesso. Inclusive,

06:39

ele já conseguiu remover a falha aqui.

06:43

Ele já fez a remoção da falha usando o nosso MCP Remove Fault.

06:48

Então, em teoria, nossos pods estão agora saudáveis.

06:51

Vamos dar uma olhada? Olha lá, estão todos saudáveis. Então,

06:53

Ele já conseguiu fazer a remoção aqui da falha para a gente.

06:56

Como ele entende que está em uma simulação, ele conseguiu fazer isso aqui.

07:01

O que a gente pode fazer aqui agora é pedir para ele aumentar a réplica. Vamos lá.

07:07

Aumente a réplica.

07:11

Ou réplica count, né?

07:14

Replica count do app .api para 6. Vou pedir para aumentar para 6.

07:21

Ele vai criar uma nova ação. Como

07:30

você pode ver, 6 réplicas.

07:31

Primeiro vou verificar o status atual. Ele tem 3 réplicas.

07:34

Então agora ele vai conseguir registrar aqui uma ação. Olha que legal.

07:39

Registrou uma ação para a gente. Legal? Blast array médio.

07:45

Precisa da nossa aprovação. Então eu vou pedir para ele aprovar. Aprovado.

07:52

Aprovado. Vamos

07:56

ver o que ele vai fazer. Ok. Ele está fazendo a ação.

07:59

Aprove a ação. Aprovado. Agora ele vai fazer o scale. Cubo estrela scale.

08:04

Vamos ver o que ele fez aqui. Olha lá. Escalou para 6.

08:06

Réplica 6. Deu uma falha. Vamos ver o que ele está fazendo.

08:11

Ele mexeu aqui no spec.

08:14

Aplicado com sucesso. Agora ele escalou. Vamos ver. Olha lá.

08:18

Tem mais dois, três, temos seis réplicas aqui agora. Tudo feito por conversação.

08:24

O chat humano aqui, tá? Fala a linguagem natural. A gente conseguiu escalar.

08:30

Então, a gente conseguiu ver que a

08:32

gente consegue ativar certas ações aqui dentro.

08:40

E até depois,

08:41

se a gente quiser melhorar o código, vocês podem testar isso aí com mais calma.

08:46

A gente pode melhorar o código e pedir para ele...

08:51

Assim, só, por exemplo, só o...

08:55

Só eu, o Robson, só o Robson pode ir lá e fazer a trava do QSuite.

09:02

Então eu vou lá, peço para fazer a trava, aí eu verifico se o usuário é o Robson.

09:06

Ah, não é o Robson, então você não pode fazer.

09:09

Entendeu? Só o fulano de tal... pode fazer aprovações.

09:13

Você pode colocar isso tudo dentro do seu código,

09:15

dentro do seu MCP, mas com o texto. Então,

09:18

com o contexto também você consegue colocar uma lista de pessoas,

09:21

etc. Então, você tem essas possibilidades, entendeu? Vamos fazer só um teste aqui,

09:25

que é uma feature do próprio OpenWebWire. Vamos pedir para ele registrar uma

09:31

nota com essas ações.

09:34

Vamos pedir para ele registrar uma nota para

09:36

a gente aqui dentro do próprio OpenWebWire,

09:38

para a gente ver essas ações que ele tomou aqui.

09:41

Esperar um pouquinho, ele tem lá a feature de nota,

09:45

né? Vocês viram que tem aqui dentro do OpenUI,

09:47

a gente tem várias features que são próprias dele,

09:49

inclusive umas são as notas aqui, né? Tá aqui, ó, notas.

09:53

A gente tem essas features aqui que são bacanas. Então, ele,

09:56

em teoria, vai chamar as notas aqui do próprio OpenUI, que está aqui no cantinho,

10:00

e vai registrar uma nota para a gente falando o que aconteceu aqui.

10:06

Então, vamos esperar um pouquinho aqui que ele vai conseguir fazer a geração, ó.

10:12

Resultado de escrever nota.

10:13

Tudo criado com sucesso. A nota foi criada, tudo certinho.

10:18

E temos tudo lá. Vamos ver a nota?

10:22

O que a gente tem aqui agora?

10:24

Hoje, há segundos atrás. É essa aqui.

10:28

Simulação de incidente, cronologia dos eventos, status final dos recursos.

10:35

Lições aprendidas, colocou bonitinho. Como aqui é uma simulação,

10:39

ele registrou como simulação. Então,

10:41

o QSuite aqui funcionou corretamente,

10:43

eu bloqueei as ações automáticas, governança de ações,

10:45

sistemas de registro e aprovação funcionaram bem para as ações de médio blast radius,

10:50

bem para operações de médio blast radius,

10:53

permissão para K8S,

10:57

ele pode falhar por permissão.

11:00

Então, o CoupPath vai funcionar. Foi uma alternativa eficaz. Então, ele tentou fazer o scale,

11:04

não conseguiu, e ele foi para o CoupPath. Então, ele tentou uma,

11:08

mas depois tentou outra. Então, simulação da demo.

11:10

É importante distinguir entre incidentes reais e simulações,

11:14

antes de executar mitigações. Então, a gente tem várias coisinhas aqui.

11:19

Referência, homebook utilizado, o namespace, o deployment.

11:23

Ele colocou uma nota completa aqui para a gente, do que a gente pode...

11:28

do que aconteceu. Então, isso aqui é muito poderoso.

11:31

Isso aqui é muito legal que a gente consegue documentar vários processos com isso.

11:35

Isso é muito legal. Ok?

11:37

Pessoal, essa aqui foi a simulação, a segunda demo nossa. Legal?

11:42

Vamos falar aqui um pouquinho da terceira demo,

11:44

que é um pós-mortem automático. Então,

11:47

o modelo de pós-mortem ele consome audit logs, mais métricas,

11:50

mais timeline e gera o rascunho de Blast Radius 5W aqui pra gente.

11:59

Vou encerrar esse vídeo por aqui e no próximo a gente vai

12:01

fazer um pós-mortem dos nossos problemas que a gente teve. Fechado? Volto já.

## Resumo IA

[RESUMO_IA]