Módulo: Desenvolvimento de Agentes com IA\
Aula: [Agente investigador de estorno](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18573)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos criar o Investigador do Estorno,

00:04

que vai ser o nosso agente no meio do workflow,

00:06

que vai fazer a investigação e vai dar

00:09

o veredito se tem algo indevido para ser estornado.

00:14

Ele não vai executar nada que mude o estado do sistema.

00:20

Então, vamos brincar com esse agente. Eu já fiz a criação dele.

00:25

Ele tem a parte de Dev, como nós já tínhamos aprendido,

00:28

nós vamos testar ele de forma separada no ADK Web. E aqui está

00:35

o código-fonte dele. Então, tem o nome, a descrição,

00:38

ele vai ser o especialista em julgar a política de Refund.

00:44

Tem a sua instrução, ele tem um retorno, uma saída estruturada com

00:50

a sua key, e

00:53

tem acesso a uma tool de Find Invoices, porque no meio do processo ele vai...

00:59

usar o Customer ID para buscar as invoices do cliente.

01:05

E aí ele recupera isso,

01:07

traz para o meio do contexto e faz a investigação.

01:10

Então, antes, na verdade, de ver o código-fonte,

01:13

nós vamos ver que essa tool está presente aqui na parte de Tools, é o Billing Tools.

01:20

Recebe o Customer ID, nós já temos no State.

01:25

Também sabemos que... Pode ser pego com o toContext.

01:29

Podemos passar ali toContext .state para poder fazer a captura.

01:34

Então, diretamente já fazemos o listInvoices. Então,

01:38

esse billing que está aqui é um mock.

01:40

Vamos supor que a gente tivesse uma API de billing.

01:44

Então, como no Platform Status nós temos uma API fake,

01:49

temos também para o billing.

01:58

Então, temos aqui o endereço fake, as invoices que...

02:02

É um dicionário e a chave desse dicionário é um

02:07

valor composto entre o ID do cliente e o mês.

02:13

Nós vamos sempre lidar com o mês para poder identificar os problemas.

02:17

Então, por exemplo,

02:19

tem essa aqui que foi cobrada duas vezes e vai

02:23

ficar na faixa que nós podemos fazer o estorno automático,

02:26

que nós vamos fazer depois. Então, tem essa linha duplicada,

02:30

está dentro dos 50 dólares, 50 reais.

02:33

E tem até um mais abaixo aqui, que é o duplicado acima de 50 reais,

02:37

que nós podemos testar outra lógica também. Enfim. Então,

02:42

mais aqui abaixo, nós vamos ter a configuração do

02:48

servidor e as operações. Então, veja. Eu tenho listInvoices.

02:55

Tem o mock da chamada, ele vai devolver as invoices.

02:59

Se eu quiser pegar apenas uma, ele vai buscar apenas uma invoice.

03:04

E o issue Refund.

03:06

que vai ser a operação que nós vamos fazer esse re-estorno.

03:12

Passa o Customer ID, o Amount e o Reason,

03:16

ele vai fazer o estorno para o usuário de alguma forma.

03:19

Isso aqui não importa no nosso projeto.

03:23

Se ele está fazendo devolução de cartão de crédito ou qualquer coisa assim,

03:27

é só para simbolizar essa operação. Então,

03:30

são três operações que nós temos no nosso servidor.

03:34

Listar as faturas, pegar invoice e fazer o refund.

03:38

Então a nossa tool,

03:40

onde está a tool,

03:42

ela chama o billing direto e ela tem acesso aos métodos.

03:48

Tudo que não está com underscore antes são métodos acessíveis.

03:53

Enfim, então o nosso agente acessa, vamos pegar novamente

04:01

o nosso agente, ele vai acessar essa tool.

04:04

Em termos de saída estruturada, esse nosso agente tem que emitir uma decisão,

04:10

que vai ser o veredito,

04:12

ou é para fazer o refund, que é para estornar,

04:15

nós vamos fazer o estorno automático,

04:17

ou é para escalar.

04:19

A ideia aqui do escalar um ser humano é fazer um registro em algum lugar

04:24

em que um ser humano vai analisar aquele ticket e ele pode tomar ações lá, ou

04:31

até mesmo voltar

04:34

para esse workflow e tomar alguma providência.

04:38

Mas nós estamos falando aqui do human in the loop,

04:41

então de qualquer forma vai ter o ser humano no meio do processo.

04:46

Tem o mês que identificou a fatura que é para ser estornada, os itens envolvidos,

04:53

que vai ser uma lista das linhas indevidas,

04:59

e o reasoning,

05:00

o raciocínio, que é justificar essa decisão para...

05:03

Vou fazer um handoff humano,

05:06

se nós vamos escalar ou estamos

05:09

fazendo o estorno por tal motivo.

05:13

Isso é importante porque fundamenta o que nós estamos fazendo.

05:17

No System Prompt, nós vamos falar a persona do agente,

05:21

que ele é o investigador de Founder Alchemy Cloud,

05:23

seu único trabalho é julgar a política.

05:27

Aí ele tem acesso à mensagem do ticket e ao Customer ID.

05:34

A primeira coisa que vai ser feita, nós temos três passos. A primeira coisa,

05:38

usar a tool de find invoices,

05:40

ele vai buscar as faturas uma

05:43

vez e aí vai identificar as informações.

05:48

Caso contrário, se o cliente não tiver nada, então o veredito é escalar,

05:52

porque às vezes pode ser que tenha alguma questão,

05:56

então o escalar significa que um ser humano vai olhar.

06:02

No passo dois, vai ser julgada a política.

06:05

É aí que vai brilhar esse não determinismo com a gente de A.

06:10

Porque nós pegamos a fatura, temos o que é legítimo não estornar,

06:15

o que é indevido, por exemplo, a questão de duplicidade.

06:19

Imagina que dependendo do contexto da empresa,

06:21

nós poderíamos colocar aqui várias regras que poderiam ser analisadas,

06:25

que demoraria um pouco de tempo para um ser humano poder fazer toda essa análise.

06:30

Imagina em grande escala ao longo dos dias e semanas. Então essa política,

06:36

aqui, ganharia em produtividade.

06:41

E aí eu ponto, porque aqui como eu não estou tomando nenhuma decisão,

06:46

essa decisão depois fica para um function code em um nó,

06:51

então nós ainda vamos ter a validação disso. Então,

06:55

no veredito final, se há linhas indevidas,

06:58

ele vai colocar um decision refund, vai colocar o mês, os itens.

07:04

Nunca informe o valor apenas dos IDs,

07:07

Se não há linhas indevidas, a fatura é legítima,

07:10

Ou a mensagem não permite escolher o mês com segurança,

07:13

Então vai para o escalate, decisão igual escalate.

07:17

E o reason é apenas uma justificativa curta e objetiva,

07:22

Vira contexto do handoff se escalar.

07:25

E aí tem aqui o formato oficial da saída.

07:31

Então o nosso agente não tem... nenhuma complexidade em si,

07:35

Mas ele carrega essa regra importante de análise,

07:42

Essa inteligência de como que vai ser feita essa análise dos estornos.

07:48

Então vamos fazer aqui um ADK passando todo o caminho do ReFound Investigator,

07:54

Agora apontando para o Dev, que nós possamos brincar. Então agora, se

08:01

Eu só recarregar ele

08:04

Aqui, nós precisamos de duas informações.

08:08

Que são

08:10

TicketMessage e o CustomerID, ambos no Station.

08:19

E a gente envia qualquer coisa aqui na mensagem. Então vamos preencher

08:25

O TicketMessage, falando

08:29

Assim, estorno da fatura de junho de 2026.

08:36

E o CustomerID, que

08:40

É o C203, que eu sei que tem um duplicado, para que nós possamos analisar.

08:47

Vamos dar o Enter, então veja só,

08:49

Tem o Find Invoices, ele retorna as invoices, então tem a decisão.

08:57

Decisão Refund, o

09:00

Mês de junho, o item que é somente o item devido,

09:03

Porque o outro foi cobrado de forma devida, e a Reasoning,

09:08

É identificada a cobrança de duplicidade do plano PRO no mês de junho de 2026,

09:14

O item de ID,

09:18

É a cópia excedente e será estornado.

09:22

Então, imagina acrescentando uma lógica mais complexa,

09:26

Nós podemos fazer uma análise muito legal

09:30

E permitir que esse processo seja totalmente automatizado,

09:34

Que ganharemos uma produtividade incrível. Enfim, então,

09:38

Esse a gente vai emitir esse parecer e aqui que nós vamos fazer a junção,

09:45

Ganhar as vantagens do determinismo.

09:48

Pegamos esse parecer e aí nós vamos executar num nó com o function code.

## Resumo IA

[RESUMO_IA]