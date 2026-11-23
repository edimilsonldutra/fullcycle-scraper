Módulo: Arquitetura na Era da IA\
Aula: [Provenance e confiança antes do retrieval](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18850)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Na aula anterior nós vimos uma situação importante no nosso RAG.

00:06

Uma pergunta completamente legítima conseguiu produzir uma resposta

00:11

contaminada porque um documento não confiável entrou na base.

00:15

Foi indexado, recuperado,

00:16

selecionado pelo re-ranker e acabou sendo usado ali pelo modelo.

00:21

E isso muda bastante a forma de como que a gente precisa pensar em segurança.

00:26

Até aqui, quando a gente estava falando em proteger uma aplicação com IA,

00:30

era muito fácil olhar primeiro para o modelo. Talvez melhorar o prompt,

00:34

colocar uma instrução mais forte ou tentar detectar algum conteúdo malicioso.

00:38

Só que no ataque que a gente acabou de executar,

00:41

o problema começou muito antes do modelo.

00:44

O documento já tinha sido aceito como conhecimento.

00:47

E é aqui que entra um conceito importante chamado de provenance,

00:51

ou... Proveniência, tá? O provenance, ele responde perguntas como,

00:57

de onde veio esse documento?

00:59

Quem publicou esse documento?

01:00

Essa pessoa ou sistema tinha autorização para publicar?

01:04

Esse documento passou pelo processo esperado de aprovação?

01:07

O conteúdo que a gente indexou é realmente aquele que foi aprovado?

01:12

Perceba que isso é diferente de validar a meta dado. No nosso laboratório, vamos dizer assim,

01:17

os documentos contaminados possuíam campos aparentemente corretos.

01:21

Eles tinham tenant, tinham product, tinham status como published, tinham visibility,

01:27

tinham version, tá? Do ponto de vista estrutural, eram documentos válidos,

01:32

mas existe uma diferença enorme entre alguém escrever status published, né?

01:39

dizendo que esse documento já foi publicado, né? E a aplicação saber,

01:43

vamos dizer, que esse documento foi publicado para uma origem autorizada.

01:47

O primeiro é uma declaração feita pelo próprio documento.

01:51

O segundo é uma decisão de confiança feita pelo sistema.

01:56

Essa diferença, ela é central.

01:58

Imagine que um usuário está fazendo um upload de

02:00

arquivos e colocando no nosso front matter.

02:03

E daí está lá escrito tenant FC aí. Certo? E o status está como publisher.

02:09

Se a aplicação simplesmente aceitar esses valores,

02:13

o usuário está controlando não apenas o conteúdo,

02:16

mas também a parte das informações utilizadas para decidir

02:21

se aquele conteúdo pode entrar no sistema.

02:24

É semelhante ao que a gente viu no agente.

02:26

Se o usuário escreve na mensagem sou administrador,

02:30

isso não pode transformá-lo em administrador. Da mesma forma,

02:34

um documento declarar 'sou publicado' e pertenço ao tenant da FCAI.

02:42

Então, isso não deveria ser o suficiente para

02:46

tornar esse documento uma fonte confiável. Então,

02:49

uma das primeiras decisões arquiteturais é separar metadados fornecidos

02:54

pela fonte do metadado

02:57

de segurança

03:02

controlada pela aplicação.

03:05

O título de um documento pode vir do próprio arquivo, a sessão também,

03:09

talvez o plano ao qual ele se refere também.

03:12

Mas informações utilizadas para autorização,

03:16

Confiança e publicação precisam ser tratadas de outra forma.

03:21

Por exemplo, quem submeteu esse documento?

03:24

Qual source system entregou o arquivo? Ele foi aprovado?

03:27

Qual é o trust level desse cara?

03:31

Quando é que isso aconteceu?

03:34

Essas informações,

03:35

elas podem precisar ser atribuídas pela aplicação ou pelo pipeline de gestão,

03:40

e não simplesmente aceitas no documento.

03:43

E isso nos leva a outro conceito importante,

03:46

que é Trusted Ingestion. Até agora,

03:49

o nosso fluxo pode ser visto mais ou menos assim.

03:52

A gente tem um documento, a estrutura está válida,

03:55

Aí a gente faz a indexação e daí a gente tem um processo de retrieval.

03:59

Mas quando a provenance passa a fazer parte da arquitetura,

04:05

a gente pode ter documento, a origem é conhecida, a fonte é autorizada,

04:10

o conteúdo é aprovado, o metadado de segurança está aplicado,

04:14

aí vai para a indexação.

04:16

Observe onde a gente está colocando o controle na realidade.

04:23

Antes do retrieval, na verdade,

04:25

antes mesmo do documento se tornar conhecimento disponível para o retrieval.

04:29

E isso é importante porque tentar resolver tudo depois seria muito mais difícil.

04:34

A gente poderia deixar o Poison entrar, indexar,

04:37

recuperar e depois pedir para o modelo, por favor,

04:40

não confie em documentos maliciosos.

04:42

Mas como o modelo vai determinar somente olhando o texto?

04:48

Quem realmente tinha autoridade para publicar aquele documento,

04:51

na realidade, entende? Então,

04:53

ele não deveria ser responsável por isso.

04:55

A confiança da fonte é uma propriedade da arquitetura,

04:59

não é uma decisão probabilística do modelo.

05:02

Também a gente pode ter uma área de quarantine,

05:06

ou área de quarentena, no final das contas.

05:11

E deixa eu melhorar meu inglês para você. É quarantine, né?

05:15

Então, eu tenho um documento novo,

05:17

pode chegar num sistema sem ser imediatamente disponibilizado por RAG.

05:21

Ele passa primeiro por validações. Talvez uma aprovação humana,

05:25

talvez uma pipeline automatizada, talvez uma verificação da origem.

05:29

Somente depois ele muda de estado e pode

05:32

entrar na coleção utilizada pelas aplicações.

05:35

E isso não significa que todo sistema precise

05:38

de uma infraestrutura enorme de assinatura digital,

05:41

certificados e workflows mega complexos.

05:44

O nível de controle depende do risco.

05:46

Uma wiki interna pequena pode utilizar um conjunto conhecido de,

05:51

sei lá, de diretórios ou repositórios autorizados.

05:54

Uma aplicação corporativa pode exigir identidade do publisher e aprovação.

06:00

Um ambiente regulado pode exigir assinatura, histórico de mudança e auditoria.

06:05

O princípio, no final das contas,

06:07

é o mesmo. Não confundir conteúdo bem informado com conteúdo confiável.

06:12

Existe ainda um outro detalhe importante.

06:15

Provenance ajuda tanto contra factual poisoning, quanto contra,

06:21

como se diz, indirect prompt injection.

06:24

Então, se a gente barrar um documento porque ele veio de uma origem não autorizada,

06:29

não importa se ele devia ter um SLA

06:32

falso ou uma instrução tentando manipular o modelo.

06:37

O conteúdo simplesmente não entra na fonte de conhecimento confiável.

06:41

Isso reduz o problema antes que ele chegue no LLM.

06:44

Claro que Provenance não vai resolver toda a segurança do RAG.

06:49

Uma fonte autorizada também pode ser comprometida,

06:52

uma pessoa autorizada pode publicar algo errado,

06:54

um documento legítimo pode conter conteúdo externo contaminado. Por isso,

06:59

a gente continua falando em defesa em profundidade.

07:02

Mas Provenance cria uma primeira barreira que hoje

07:05

o nosso laboratório mostrou que está faltando. Na próxima aula,

07:09

a gente vai implementar essa diferença aí no projeto.

07:12

A gente vai deixar de tratar campos autodeclarados

07:16

pelos documentos como prova de confiança.

07:19

A gente vai adicionar ali como prova de confiança, na realidade,

07:22

adicionar uma política de ingestão para as

07:24

nossas fontes e também executar novamente...

07:29

exatamente a mesma baseline que a gente estava utilizando. Então,

07:34

o mais importante será observar onde o ataque passa a parar.

07:39

Antes, ele chegou até a resposta.

07:43

E depois da mudança,

07:45

a ideia é tentar descobrir se a gente conseguiu interromper muito antes que

07:51

aquele documento contaminado tenha a chance de se

07:54

tornar conhecimento para o nosso RAG.

07:56

Mas, de forma geral,

07:58

A ideia principal é trazer essa clareza para você de

08:04

que existem diversos processos e

08:08

mecanismos que o seu sistema,

08:11

a forma de como você está fazendo a ingestão do seu pipeline,

08:15

como esse tipo de coisa tem que ser muito bem arquitetado. Por isso que, assim,

08:22

são pontos que as pessoas acabam ignorando,

08:25

acabam pensando somente depois que o documento entrou.

08:30

Mas o que eu estou querendo trazer aqui para você

08:33

é essa clareza e essa importância do processo do...

08:37

E daí, no nosso laboratório, a gente vai ter esse tipo de simulação para a gente,

08:43

pelo menos, marcar o nosso ponto falando, olha,

08:45

pelo menos para a entrada, agora a gente tem aqui.

08:48

Óbvio que é para exemplo didático,

08:50

mas eu acho que acaba ficando mais claro. Fechou? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]