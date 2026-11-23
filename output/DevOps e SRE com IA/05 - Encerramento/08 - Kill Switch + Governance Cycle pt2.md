Módulo: DevOps e SRE com IA\
Aula: [Kill Switch + Governance Cycle pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18542)

## Resumo da aula



## Transcrição

00:00

Tá terminando aqui as origens, que ele conseguiu fazer o Crash Loop Backoff.

00:03

Ele conseguiu pegar os detalhes lá do Homebook.

00:06

Que legal. Então, ele puxou, pra fazer o diagnóstico,

00:09

ele puxou algumas coisas dentro do Knowledge Base.

00:13

Então, dentro do Knowledge Base lá,

00:15

ele pegou algumas informações pra fazer esse diagnóstico pra gente. Ok?

00:20

Ele tá terminando de processar aqui. Aí, ó. Processo terminado.

00:25

Diagnóstico completo do problema. Então, a gente tem o problema.

00:30

Vamos lá. O pod tá no namespace tal, comando falho. Então,

00:35

ele tá rodando esse comando, tá? O inject fault lá,

00:39

ele insere esse comando lá no comando do pod, acaba que ele fica lá em problema.

00:44

Então, ele já identificou que é esse aqui, entendeu?

00:47

Identificou de novo esse crash loop inject aqui, igual a true.

00:53

Então, status atual tem três réplicas totais,

00:55

duas com saudades e uma com seis reinícios aqui, igual a gente tinha antes.

01:01

Ok? Então agora, antes da gente dar continuidade, o que a gente vai fazer?

01:07

Vamos aqui pedir para, falar um pouco da parte de governança,

01:12

pedir para ativar o QSuite antes de qualquer coisa.

01:19

Entendeu? Vamos pedir para desabilitar o agent. Então, vamos lá.

01:23

Vamos criar um novo chat, depois a gente retorna para esse,

01:26

porque esse aqui a gente está fazendo um diagnóstico.

01:28

O outro chat vai ser para a gente pedir para ele desabilitar o QSuite.

01:34

Esse aqui eu vou criar de maneira mais fácil,

01:36

para vocês verem que tem várias opções de a gente fazer.

01:38

Vou selecionar o Queen,

01:39

vou selecionar a ferramenta e esse aqui vai ser o incidente MCP.

01:45

Vamos aqui ativar a nossa função padrão aqui.

01:49

Então, vamos lá, ative o QSuite.

01:57

QSuite, desabilite o agent.

02:02

Ok, vamos ver qual vai ser a resposta dele aqui.

02:10

Vamos aguardar aqui qual que é a resposta. Que

02:14

o switch, ele fez lá enable falso. Legal. Então,

02:19

com o switch desativado, o agent bloqueado, nenhuma ação será executada.

02:23

O switch foi ativado com sucesso,

02:26

o agent SRE agora está desabilitado e todas as ações só estão bloqueadas,

02:32

nenhuma ação será executada pelo agent até que ele seja reativado.

02:37

Se precisar do agent posteriormente,

02:39

posso fazer isso quando for necessário. Legal? Então,

02:42

vamos voltar aqui para o nosso troubleshoot.

02:47

Então, o que ele fez lá?

02:49

Ele chamou a nossa MCP e

02:51

desativou a API de fazer o incidente. Então,

02:57

ele não consegue fazer mais nada agora. Então,

03:00

vamos tentar registrar uma nova ação aqui dentro.

03:05

Ah, legal.

03:08

Preciso que você faça

03:15

rolling restart do

03:19

app API deployment.

03:23

Vou pedir para ele fazer. Com o switch agora ativo,

03:28

Em teoria, ele não vai conseguir fazer nada. Vamos fazer um teste.

03:32

Primeiro, ele vai fazer uma verificação. Vamos

03:40

esperar um pouquinho. Ok.

03:42

Executar o restart de tal coisa.

03:44

Como o demo foi injetada, ele

03:49

já executou o restart com sucesso. Isso não era para ter acontecido.

03:56

Ele não era para ter acontecido esse detalhe.

04:01

Vamos olhar aqui o que aconteceu.

04:07

End out time. Houve um timeout na verificação do status. Vamos verificar aqui.

04:13

Ele tentou fazer um rollout ali.

04:17

Incidentes, QSuite está desativado. Significa que ações estão bloqueadas.

04:21

Ah, então ele deu problema mesmo.

04:23

Ele tentou ali, mas não conseguiu. Ele só tentou fazer.

04:28

Então acabou que o QSuite está desativado.

04:33

Significa que todas as ações estão bloqueadas.

04:35

Devo reativá-lo primeiro para poder executar as ações de mitigação.

04:40

Ele já conseguiu ativar aqui o nosso QSuite. Então...

04:46

Em teoria, esse cara de trouble switch não poderia fazer essa ação,

04:50

poderia se separar, isso seria uma opção para a gente separar.

04:53

Então a gente consegue fazer os testes e ir vendo no

04:57

ambiente de desenvolvimento como que vai se comportando o agent,

04:59

isso é bacana pra caramba.

05:01

Então a gente consegue ver que ele tentou fazer ali em cima,

05:06

deu problema porque o kill switch está desativado.

05:10

Na primeira vez, eu imaginei que ele ia tentar restartar direto,

05:13

mas não. Estava desativado. Ele foi e ativou por conta própria,

05:16

sendo que eu não pedi para ele ativar.

05:18

Isso tem que estar talvez explícito lá no próprio subsistema,

05:21

que ele não pode fazer isso.

05:23

E basicamente, quando ele fez isso,

05:28

ele conseguiu ativar e agora está tentando fazer algumas coisas ali.

05:32

Então, parece que pods antigos estão em execução e continuam falhando.

05:36

Vou verificar se há alguma coisa. Então, ele já está aqui em loop tentando fazer.

05:40

Ajustes aqui de maneira automatizada para a gente,

05:43

justamente pela possibilidade dele usar aqui várias tools em paralelo. Legal?

05:49

Mas vocês conseguem ver ali que ele falou, ó, tá desativado.

05:52

Mas aí foi e ativou. Não era para acontecer. Mas tudo bem.

05:56

Então, vamos dar continuidade aqui.

06:00

Por mais que ele tenha feito essa ativação automática ali que eu não pedi,

06:04

e o QSwitch está aqui dentro, então ele fez isso, né?

06:10

Então, vamos aqui tentar fazer a ativação de novo,

06:16

a desativação do QSuite. Vamos

06:20

pedir para ele desativar aqui.

06:24

Reative o QSuite.

06:35

Ixi, não tinha nenhuma tool listada aqui. Ah,

06:42

não tinha sim. Então, enable tool. Então,

06:45

tool incident QSuite not found. Não houve problema. Vamos

07:17

verificar o que aconteceu.

07:19

Ele listou a automação para a gente.

07:23

Enable to Incident NGP Queue Switch.

07:28

Not found. Então vamos lá. Deixa eu ver o que aconteceu com ele aqui.

07:32

Vamos ativar a Queue Switch e pedir para ele ativar de novo.

07:35

Reative a Queue Switch.

07:42

Agora com a tool ativada, né?

07:43

Vamos pedir para ele ativar aqui e vamos ver o que ele vai retornar. Reativando aqui o switch.

07:49

Ok. É porque eu não tinha realmente ativado. Ele tentou aqui rodar,

07:52

mas eu acredito que ele tentou rodar por causa do contexto,

07:55

não por causa que a tool estava ativada.

07:58

Então, a gente reativou. Acesso normal retornado.

08:03

Então a gente já tem todos os acessos

08:05

aí funcionando perfeitamente a partir de agora.

08:08

O nosso chat aqui está fazendo ainda a chamada de tools.

08:12

Ele está tentando fazer aqui. Várias coisas aqui, mas não está conseguindo.

08:17

Puxou alguns pods.

08:19

Há pods em Cushmabrack.

08:21

O problema persiste porque os dados

08:23

antigos estão sendo substituídos automaticamente.

08:26

Eu vou tentar uma abordagem mais direta e verificar se posso usar

08:29

o CTL Rollout Undo para olhar

08:34

uma versão anterior que está funcionando.

08:37

Ele está tentando diagnosticar sozinho, ele está dando continuidade sozinho.

08:41

Então, provavelmente agora com o QSuite lá ativado de novo,

08:46

ele vai tentar fazer esse registro aí de ação

08:51

que ele está tentando fazer aqui agora, tá bem?

08:53

Vou esperar um minutinho aqui e vamos ver qual vai ser o resultado desse chat,

08:59

senão a gente vai ficar só olhando o chat servindo aqui, tá?

09:01

Volto em seguida para a gente ter o nosso resultado aqui,

09:05

para mostrar para vocês o que aconteceu.

09:11

Pessoal, terminou aqui. E eu tenho só um ponto para mostrar para vocês,

09:16

que ele tomou ações aqui dentro do ambiente.

09:18

Acredito eu que porque a gente foi fazendo em chats diferentes,

09:23

ele começou a tomar ações aqui deliberadamente,

09:26

sem pedir as aprovações necessárias. Então,

09:29

por isso que é super importante a gente

09:31

colocar as ferramentas certas no lugar certo.

09:34

Entendeu? Então, ele conseguiu resolver o problema. De fato, o problema está resolvido.

09:39

Só que ele não perguntou se poderia fazer alguma coisa,

09:41

não perguntou, não anotou nada.

09:44

Então a gente pode ter problema com isso. Lá em cima,

09:46

a gente viu que ele conseguiu ativar uma coisa que a gente já tinha desativado.

09:53

Entendeu? Então isso pode ser um grande problema para a gente

09:55

durante os nossos troubleshooters que a gente pode ter.

10:00

Eu vou refazer a simulação agora,

10:02

usando um novo chat e ativando de novo a ingestão.

10:08

A injeção do problema aqui pelo mesmo chat,

10:11

para a gente ver o comportamento, tá?

10:13

Mas aqui a gente conseguiu perfeitamente ver o comportamento

10:15

de quando a gente tira algumas coisas,

10:18

pode ser que ele faça coisas sem fazer pergunta para o usuário,

10:22

e isso aí já torna ele muito autônomo. Então,

10:24

O que ele fez? Vou voltar no pod para vocês verem.

10:27

Ele falou que resolveu, os três pods estão up agora, legal?

10:31

Só que o que ele fez aqui? Vou fazer um deploy aqui.

10:35

Ele criou, ele renomeou o meu deploy antigo e criou um novo, ajustando.

10:41

Então ele criou um novo, ajustando, e os três antigos ficaram aqui com o problema.

10:45

Está vendo? Os três aqui ficaram com o problema. Mas o problema, em teoria,

10:49

foi resolvido. Temos um pod operacional aqui agora que está perfeitamente rodando.

10:55

Então o que ele fez? Ele foi lá, tirou o problema, o Python aqui,

10:59

que em teoria quem poderia tirar era somente o remove que a gente tinha lá.

11:05

E ele tirou também a variável de Press Loop Injection, o True.

11:09

Legal? Ambiente de demo.

11:11

Então, o que a gente vai fazer aqui? Vamos deletar esse deployment.

11:15

Opa, dois pontos deployment. Deploy.

11:20

Vamos deletar esse aqui que é o antigo, que ele renomeou para mim.

11:23

Botar em pods. Temos os três pods aqui ativos. Agora a gente tem três.

11:27

E agora,

11:30

vamos ver aqui. Pods.

11:34

Ok, temos os três pods ativos aqui.

11:36

Então o que a gente vai fazer agora? Vamos voltar aqui.

11:39

Vamos editar de novo o nosso agent SRI de troubleshoot aqui.

11:43

E vamos ativar o fault inject MCP de novo para ele. Ok?

11:49

Criar um novo chat.

11:51

SRI troubleshoot. E vamos reiniciar aqui os nossos testes.

11:57

Porque ele não deveria fazer isso.

12:00

Inclusive, tem até algumas coisas rodando aqui até agora. Ah!

12:05

Vamos fechar esse aqui, porque ele também fez um agendamento,

12:08

ele rodou um agendamento para mim.

12:10

Vamos ver aqui em automações, ele ativou alguns monitoramentos, está vendo?

12:16

Então tem algumas coisas que não são legais,

12:18

a gente tem que restringir ao máximo o contexto dele

12:22

para evitar que ele faça esses tipos de coisa. Então,

12:25

por exemplo, tirar o contexto dele, ativar essa automação,

12:27

se a gente vier aqui dentro,

12:29

a gente tem a possibilidade de... tirar o acesso dele em automação.

12:33

Então aqui a gente tem notas, histórico de chat,

12:36

pesquisa web, geração, intento de código,

12:38

gerenciamento de tarefas, automações, tá vendo?

12:41

Então seria tirar essa possibilidade de gerar automação.

12:44

Então vamos tirar essa automação para não acontecer de novo. E vamos salvar aqui,

12:50

tá bom? Ele gerou uma automação para mim lá. Ativou, na verdade, uma automação.

12:54

Ele entendeu que precisava ativar aquela automação.

12:57

E o legal aqui é que ele também gerou uma nota.

13:01

Deixa eu ver se vai carregar aqui.

13:03

Ele falou comigo que gerou uma nota detalhando os problemas. Isso é interessante.

13:08

Você pode pedir lá dentro do projeto,

13:12

lá dentro do seu agent que você criou.

13:17

Você pode pedir para ele gerar uma nota do problema,

13:21

essas coisas, para deixar documentado também dentro do seu ambiente,

13:25

dentro do seu chat, para você conseguir fazer até algumas documentações. Legal?

13:30

Então... Vamos dar continuidade aqui e vamos

13:34

Gerar de novo a nossa demo aqui,

13:40

trabalhando com um chat só.

## Resumo IA

[RESUMO_IA]