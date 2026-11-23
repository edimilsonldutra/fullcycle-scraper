Módulo: Arquitetura na Era da IA\
Aula: [A Entrada da IA no Mundo da Arquitetura](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18110)

## Resumo da aula



## Transcrição

00:03

Bom, pessoal, agora que a gente entendeu,

00:05

conseguiu separar melhor esses tipos de arquitetura e etc.,

00:09

eu queria entrar num ponto mais importante para esse módulo, no final das contas,

00:13

é como que a inteligência artificial começa a afetar a

00:16

arquitetura de solução e a arquitetura de software.

00:19

E aqui tem uma coisa importante. Quando a IA entra numa empresa,

00:24

ela não entra só como... uma biblioteca nova,

00:28

ou como uma API que você vai chamar, ou só como um modelo que vai gerar um texto.

00:33

Ela muda a forma de como que a gente pensa na solução.

00:37

Antes, quando uma empresa queria resolver um problema,

00:40

normalmente a gente pensava num fluxo, regra, tela,

00:42

banco de dados, integração e processo.

00:44

O usuário clica em algum lugar, preenche alguma coisa, o sistema valida,

00:48

executa e grava no banco, por exemplo,

00:50

e chama uma API trazendo uma resposta.

00:55

Claro que eu estou simplificando, mas a lógica era mais ou menos essa.

00:58

Com IA, principalmente com GNI,

01:01

IA generativa, a gente começa a ter uma nova capacidade dentro da solução,

01:07

que é a interpretação. Ou seja,

01:09

o sistema deixa de depender apenas de cliques e campos,

01:13

fluxos totalmente definidos. Agora o usuário pode expressar uma intenção.

01:18

Ele pode escrever o que ele precisa, ele pode pedir uma análise,

01:21

ele pode pedir uma recomendação e etc.

01:27

E isso muda a arquitetura de solução,

01:29

porque agora a pergunta não é só qual sistema vamos criar.

01:33

A pergunta vai ser onde que a IA entra no processo do negócio.

01:37

Ela vai ajudar uma pessoa ou vai falar direto com o cliente?

01:40

Ela vai sugerir uma resposta ou vai tomar uma decisão?

01:42

Ela vai consultar dados internos? Ela vai acionar alguma ferramenta?

01:46

Ela vai mexer no sistema da empresa?

01:48

Ela vai operar um fluxo crítico ou um fluxo de baixo risco?

01:52

Consegue perceber a diferença? Na arquitetura de solução,

01:55

a IA não é uma escolha técnica isolada.

01:57

Ela é uma decisão sobre o papel que a IA terá dentro de um processo.

02:02

E esse papel pode mudar completamente a solução.

02:06

Vou imaginar uma empresa que tem que melhorar o atendimento ao cliente.

02:09

Sem a, talvez a solução fosse criar uma central de ajuda melhor,

02:12

melhorar o CRM, integrar sistemas, criar automações,

02:16

organizar a base de conhecimento e melhorar o fluxo de atendimento.

02:20

Com o IA, as novas possibilidades apareceram.

02:23

A IA pode ajudar a atender a encontrar resposta mais rápida.

02:29

Ela pode resumir o histórico do cliente.

02:31

Ela pode classificar os tickets. Ela pode sugerir resposta.

02:34

Ela pode responder perguntas simples, diretamente.

02:37

Ela pode identificar qual é a intenção.

02:40

Mas cada uma dessas possibilidades tem um nível diferente de risco.

02:43

Se a IA só resume um histórico para um atendente, o risco é menor.

02:47

Se ela responde diretamente para o cliente, o risco vai aumentar.

02:50

Então, na arquitetura de solução,

02:52

uma das decisões mais importantes passa a ser qual é

02:56

O nível de autonomia que a IA vai ter.

02:58

A IA vai ser um assistente,

03:00

vai ser um copiloto, ela vai fazer parte do fluxo principal,

03:03

ela vai executar a ação,

03:04

ela precisa de aprovação. E essa decisão não é um detalhe técnico,

03:08

é um detalhe que afeta o negócio, a operação, a segurança, o suporte,

03:11

o custo de todo o sistema e afetando até o usuário final.

03:16

E é por isso que na era da IA,

03:18

a arquitetura de solução precisa pensar muito mais em limites.

03:21

O limite de autonomia,

03:23

o limite de dados, o limite de ação, o limite de custo,

03:26

de responsabilidade. Antes de perguntar qual modelo usar,

03:29

o arquiteto precisa entender qual é o papel seguro

03:31

e útil da IA dentro daquela solução.

03:35

E agora, depois dessa decisão da solução,

03:39

começa a ficar mais clara a entrada da arquitetura de software.

03:43

Porque uma coisa é dizer...

03:45

A IA vai ajudar a atender, a responder bem os clientes.

03:48

Outra coisa é estruturar um software para isso funcionar.

03:51

E aqui a conversa vai mudar.

03:53

Na arquitetura de software, a IA passa a ser um componente dentro do sistema.

03:57

Um componente poderoso, mas ainda assim um componente.

04:00

O modelo não é uma aplicação inteira.

04:02

Ao redor existe, sei lá, autenticação, autorização, banco de dados e etc.

04:07

Mas aqui começam a entrar novas perguntas arquiteturais que a gente não fazia antes.

04:13

Como que a aplicação monta o contexto que será enviado para o modelo?

04:16

De onde vêm os dados que a gente vai utilizar para as respostas?

04:20

Como que eu consigo garantir que o usuário só

04:22

receba informação que ele tem permissão para ver?

04:24

Como que eu vou registrar o prompt,

04:26

o contexto, a resposta e as ações tomadas?

04:29

Como que eu evito que a minha aplicação fique acoplada a um único...

04:35

provider, por exemplo. Como que eu lido com latência alta?

04:38

Às vezes eu chamo um modelo e ele demora pra caramba pra responder.

04:41

Como que eu consigo controlar, por exemplo, o custo por chamada?

04:45

Como que eu testo o comportamento que pode variar?

04:47

Como que eu crio um fallback quando o modelo vai falhar?

04:50

Então essas perguntas são também de arquitetura de software e

04:54

aqui existe uma mudança muito grande em relação aos sistemas tradicionais.

04:58

Em um sistema mais convencional, o agente trabalha com contratos mais explícitos.

05:02

Uma API tem uma resposta esperada,

05:04

uma função recebe uma entrada e devolve uma saída,

05:07

uma query retorna dados num formato mais previsível.

05:10

Tem falha, claro, mas existe um timeout, um bug,

05:13

um problema de rede. e etc. Com a generativa,

05:16

a resposta pode variar mesmo quando a entrada parece parecida.

05:20

Ela depende ali do modelo,

05:22

do prompt, do contexto, dos dados recuperados e tudo mais. Então,

05:26

a arquitetura de software precisa criar

05:28

mecanismos para controlar essa variabilidade.

05:31

Não no sentido de tornar tudo 100% determinístico, porque é impossível,

05:36

mas no sentido de colocar limites, validações,

05:41

rastreabilidades e fallbacks, por exemplo.

05:44

Vou dar um exemplo aqui. Por exemplo, se a IA gera uma resposta para o cliente,

05:49

talvez a aplicação precise validar se aquela

05:51

resposta está baseada em fontes confiáveis.

05:54

Se a IA chama uma ferramenta,

05:55

talvez a aplicação precise verificar se aquela ação é permitida,

05:59

se ela tem acesso a dados internos,

06:01

o sistema precisa respeitar a permissão do usuário. Então,

06:04

esse ponto em relação à parte de arquitetura,

06:08

ela precisa envolver IA. Mas não é somente ali confiar nela.

06:13

Aqui a gente vê um monte de gente errando, pagando um preço...

06:17

muito alto em relação a, desde custo da utilização,

06:20

mas ainda trazendo um resultado ruim para os clientes e ainda problema de segurança,

06:25

que normalmente, quando vai para a produção, acaba sendo bem frágil.

06:29

A gente vê muita gente criando protótipo e beleza,

06:32

mas quando o negócio vai para a produção,

06:34

a coisa começa a ficar mais complicada. Então, a gente começa a falar de camadas,

06:40

e aí a gente tem as camadas de orquestração, de integração com os modelos,

06:43

camadas de ferramentas, de avaliação, camadas de...

06:46

de observabilidade específicas para IA. Então,

06:49

eu não quero complicar tudo desde o início,

06:51

mas é importante você saber que essas preocupações existem,

06:54

tanto quando a gente está falando na parte de arquitetura de solução,

06:57

quanto na de software. A gente começa a ter problemas que a gente não tinha antes e, para isso,

07:03

a gente vai começar a precisar ter camadas que a nossa aplicação não tinha,

07:06

a gente vai precisar tratar erros de forma diferente e a gente vai...

07:10

precisar pegar dados de fontes diferentes,

07:13

a gente tem que pensar em segurança, em permissão, ou seja,

07:15

muita coisa começa a ser repensada uma vez que a IA entra no meio de tudo isso,

07:21

beleza? Então, somente essa reflexão para você entender, não digo o problema,

07:27

mas o desafio que a gente tem agora na era da IA.

07:30

As coisas mudaram e o grande ponto é, a gente tem que se adaptar a esses novos...

07:36

Pontos, muitas coisas vão ajudar bastante a nossa vida,

07:39

mas muitas coisas vão deixar as coisas, vamos dizer, muito mais complexas.

07:44

Quando a gente está desenvolvendo software, usando IA, usando ferramentas,

07:47

é muito bom para a produtividade.

07:49

Mas quando o software que a gente vai desenvolver é integrado com a IA,

07:54

o desafio é completamente diferente, é outro.

07:57

Às vezes você vai sentir que a sua maior dificuldade é integrar aplicações com IA.

08:02

Às vezes a gente está muito feliz com a produtividade.

08:05

Mas, no final das contas, o buraco é muito mais embaixo porque, a partir de agora,

08:10

os softwares que a gente vai desenvolver cada dia mais vão ser integrados com

08:13

a IA e a gente precisa entender como arquitetar esses tipos de software.

08:18

Beleza? Então é isso aí.

## Resumo IA

[RESUMO_IA]