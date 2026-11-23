Módulo: Desenvolvimento de Agentes com IA\
Aula: [Output schema](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18489)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre o Output Schema,

00:04

que nos permite padronizar a saída dos agentes. Esse assunto está relacionado com a

00:11

saída estruturada.

00:12

Esse assunto é muito relevante agora com inteligências artificiais,

00:16

que é o Structured Output, a saída estruturada.

00:20

Nós já entendemos que LLM é algo totalmente incerto, trabalha com não determinismo.

00:26

Então, uma vez que nós mandamos uma solicitação para ela,

00:29

a não ser que nós pedimos exatamente que o formato deve ser de tal forma,

00:34

e mesmo assim isso não é garantia de que ela vai retornar correto,

00:38

ela retorna com o texto livre.

00:42

Em muitas situações, nós vamos precisar não ter esse não determinismo,

00:47

ou seja, nós vamos precisar ter determinismo.

00:51

Nas respostas que a LLM vai mandar para o agente,

00:54

que o agente vai processar alguma coisa e mandar para o usuário.

00:58

A gente está trabalhando com dinheiro ou qualquer coisa assim,

01:01

eu vou precisar pegar um valor.

01:03

Imagine que eu estou recebendo um texto livre e eu quero extrair um valor.

01:08

Vai ser algo muito incerto.

01:09

Nós vamos dar chance para o acaso e ainda correr vários riscos de segurança,

01:16

processar alguma coisa com o valor que não devia,

01:20

enfim. Teve várias consequências ruins.

01:22

Então, com o Output Schema,

01:24

nós podemos passar em qualquer agente ou subagente e

01:28

definir o formato que ele vai retornar aquele resultado.

01:32

Eu fiz essa aplicação no consultor Faturas,

01:35

então defini o Output Schema passando o formato que eu quero.

01:39

Esse Output Schema aceita vários tipos de definições,

01:44

mas a mais elegante delas vai ser trabalhar com o Pydantic,

01:47

que nós já vimos aqui no curso.

01:49

Nós podemos modelar a saída através de uma classe que estende de BaseModel,

01:54

damos um nome para ela, o nome pode ser qualquer um,

01:58

eu gosto sempre de colocar o nome do próprio agente,

02:02

sem o 'agent' no final, sem o 'subagent', e o output,

02:06

que assim, quando eu for importar em qualquer outro lugar, usar,

02:09

eu sei que é exatamente a saída daquele agente. Então,

02:12

é só colocar os campos e pronto. Mas na hora que nós colocamos os campos,

02:17

dê um nome sugestivo para o campo,

02:19

coloque um tipo também sugestivo, e aqui eu poderia até melhorar,

02:24

porque como esse subagente vai ter lá as faturas com ID,

02:29

com client ID, a lista está ok, mas o dicionário está muito genérico.

02:34

Então, a gente poderia passar um tipo melhor aqui.

02:37

Mas também é importante colocar igual a field,

02:41

que é um campo que, na verdade, é uma classe que a gente importa do Pydantic,

02:46

que aplica mais definições nessa modelagem que nós estamos fazendo,

02:51

porque nós passamos a descrição.

02:55

Isso significa que todo esse cuidado de fazer essa

02:59

saída é exatamente porque ela é enviada para a LLM.

03:04

Vai ser convertido isso aqui em um JSON Schema, que é uma validação de um JSON,

03:10

porque a gente garante que um JSON esteja no formato. Então,

03:14

ao passar isso para a LLM, ela vai sempre...

03:19

Retornar os dados naquele formato. A gente não pode falar sempre,

03:23

porque como é não determinismo,

03:24

ainda assim há chance para o acaso. Mas aqui,

03:28

nesse caso, ela vai retornar uma lista das faturas.

03:32

Ou seja, quando ela receber a solicitação, ela vai lá na tool, processa as faturas,

03:38

ela não vai mais retornar um texto livre para o coordenador.

03:43

Então, nesse caso, nós vamos ganhar tokens,

03:46

porque o texto livre pode ter um monte de coisas necessárias.

03:50

Então, economizamos tokens,

03:52

estruturamos o formato, a saída estruturada, e

03:57

ganhamos mais assertividade na hora de trabalhar com essas informações.

04:03

Eu já deixei aqui o meu agente rodando.

04:05

Vamos ver isso aqui na prática. Eu vou gerar uma nova seção, colocar

04:11

um usuário.

04:14

que já respondeu à pesquisa de satisfação, que nós tínhamos feito essa adição.

04:20

Então, vamos colocar aqui, cliente 1, 2, 3,

04:24

listando minhas faturas.

04:31

O nosso subagente é uma task, então ele vai ali, chama ele como um ator,

04:36

como nós já tínhamos visto, e veja aqui a saída.

04:38

Tanto o finish task, que é a operação final desse agente task,

04:42

recebe ele faturas, e aqui nós temos o resultado.

04:48

Então, o coordenador... pegou um resultado em um JSON, que vai acabar sendo um JSON,

04:54

e fez a formatação. Nós podemos colocar a

04:59

request que foi feita aqui. Então, você é o consultor de faturas,

05:01

tem todo o system prompt, tem aquela questão do finish task, que

05:06

é adicionada em todo o agent task.

05:08

Então, na parte de tools, temos o transfer to agent,

05:11

que é a primeira posição, o listar faturas, que é a segunda.

05:16

E o finishTask, que é a outra tool, agora tem um parameters .json .schema.

05:21

Então, em properties vai ter todas as propriedades.

05:25

Então, tem o fator, a descrição dele. Obviamente,

05:28

vai ser um item com propriedades adicionais.

05:31

Nós não fizemos nenhuma modelagem desse tipo.

05:34

Aí tem o título, faturas, enfim, todos esses campos são padrões de um JSON schema.

05:40

Então, isso vai ser um array, tem os campos requeridos.

05:44

É interessante nós entendermos também que se eu acrescentar um XPTO inteiro,

05:51

isso vai aparecer lá como um campo requerido.

05:53

Poxa, mas o meu agente não tem esse XPTO. O que vai acontecer? Ele vai vir para cá e

06:01

como a LLM não sabe trabalhar com ele,

06:04

é um campo inteiro, então ela vai inventar um valor.

06:07

Ela vai colocar um valor default, ela tenderia a colocar um valor como zero,

06:13

então você precisa fazer uma boa modelagem,

06:15

saber se esse campo é opcional ou não, se

06:20

ele é opcional, não precisar nem vir preenchido,

06:24

então tem o optional do Python que você poderia preencher,

06:29

faça uma boa modelagem e coloque tudo sugestivo,

06:31

nós já aprendemos isso no começo da nossa disciplina.

06:37

Isso aqui faz agora com que eu consiga chegar ali

06:40

no agente ou em outras estruturas e pegar essa informação formatada.

06:45

Como eu tenho um PIDENTIC

06:47

Em algumas situações de lifecycle do

06:54

Meu agente, que eu consigo pegar esses eventos, eu consigo pegar essa informação e validá-la.

07:03

Isso é muito bom, porque

07:07

Em determinadas situações eu pego ali e vejo se o dado

07:10

está válido de acordo com o que eu preciso.

07:12

Não, não está. Então já vou processar um erro, enfim,

07:15

Eu tenho determinismo dentro de um ambiente não determinístico.

07:20

Mesmo que a LLM invente um valor, pode

07:26

Acontecer um cenário mais extremo dela colocar um valor nada a ver.

07:30

Se ela não colocar um

07:34

Texto livre, vai acontecer um erro também.

07:39

Que apesar do PyDantic que nesse processo aqui não validar logo de cara,

07:43

Nós podemos invocar essa validação depois,

07:46

Mas eu preciso pelo menos ter esses dados estruturados.

07:49

Então isso aqui me garante pelo menos que nós vamos ter um JSON a princípio,

07:55

Que se esse JSON não for válido,

07:57

Vai dar algum erro.

07:59

Eu coloquei também esse output schema no subagente de pesquisa de satisfação.

08:06

Então ele está aqui também. Nós vamos precisar... do feedback e sentimento.

08:11

Aqui nós não vamos ter nenhum ganho com isso

08:14

Porque nós registramos dentro do state o resultado da pesquisa de satisfação, que

08:24

Já vai ser usado lá pela assinatura,

08:26

Porque nós já vimos que não adianta nada ter um output

08:30

Key em um agente task que esse state não vai ser acessível.

08:35

Então, aproveitando a oportunidade,

08:37

Nós podemos combinar o output schema com o output key. Então, veja que interessante.

08:42

Se esse state estiver acessível,

08:45

Eu consigo pegar essa informação no state com essa aqui, já no formato esperado.

08:53

Mas aqui nesse caso, não vai ter nenhum efeito,

08:57

Mas mesmo assim, a saída que esse agente vai retornar,

09:02

Até mesmo que vai aqui para o coordenador, vai ser forçada também.

09:07

Então, se a gente até quisesse fazer aqui um new

09:10

Dessa classe antes aqui com esses dados e...

09:15

Jogar nesse state, nós poderíamos. Então, vamos simular mais uma seção.

09:21

Se nós colocarmos aqui o

09:26

Cliente ID 456,

09:33

Que não respondeu à pesquisa,

09:34

Vou falar para listar minhas faturas. Vai

09:43

Para a pesquisa de satisfação, vai perguntar.

09:47

Então, é caro e ruim, como nós tínhamos colocado antes.

09:54

Então, veja só, eu tenho aqui o state, que ele está formatado

09:58

Conforme nós colocamos.

10:01

Ele foi para o agente dessa forma.

10:03

O que importa é que ele vá lá para

10:04

O agente de assinatura para oferecer aquele desconto,

10:07

Aquela lógica ali para um cliente que está insatisfeito.

10:12

Nós vemos aqui a resposta que foi feita.

10:16

Então, nós precisamos ter cuidado porque nós podemos,

10:19

Como nós estamos acostumados a sempre trabalhar de forma determinística,

10:24

Aí eu posso querer colocar output schema em todos os meus agentes.

10:29

E isso é muito errado. Por quê?

10:32

Primeiro, estando trabalhando com inteligência artificial,

10:36

a questão do não determinismo pode

10:40

ser fundamental para que você consiga avaliar,

10:44

processar coisas que não

10:46

são lineares ou diretamente lógicas.

10:55

Colocar sempre output schema pode fazer com que o

10:57

seu agente não funcione de forma correta.

11:00

Na verdade, é isso que eu quero mostrar no momento. Vamos mudar ele para chat.

11:07

E aí eu não posso ter esse finish task que está aqui,

11:09

a instrução, apenas para poder garantir que ele sempre use essa tool.

11:16

Então o operador vai fazer a transferência para ele

11:18

e ele tem que fazer as perguntas,

11:21

ou melhor, a pergunta...

11:23

da pesquisa de satisfação. Já estava aqui com a gente, ok,

11:27

então vamos criar uma nova seção,

11:36

cliente 456, que novamente nós vamos responder pesquisa de satisfação.

11:47

Ele vai transferir para pesquisa de satisfação, e veja só o que aconteceu.

11:58

Ele transferiu de volta para o operador da conta, então comeu totalmente a

12:06

pergunta que deveria ser feita para o usuário. Por quê?

12:09

Vamos pegar esse transfer que está sendo feito.

12:16

Na verdade, é esse aqui.

12:18

Foi a decisão do agente de pesquisa de satisfação

12:21

de retornar para o operador da conta.

12:23

Então, você é um agente de pesquisa de satisfação e tudo mais.

12:28

Aí, essa instrução que está aqui é a instrução por conta

12:31

que nós adicionamos aquele output schema no agente chat.

12:36

Ele é obrigado a retornar um setModelResponse com a saída formatada, estruturada.

12:46

Então, a primeira tool vai ser esse setModelResponse com o JSON Schema.

12:53

Veja só, feedback e sentimento. Eles são obrigados.

12:57

Então, passando isso para

13:01

a LLM, ela transfere para o operador da conta.

13:06

Ela pode decidir que

13:09

o agente não tem condições de retornar a resposta adequada,

13:15

uma vez até que a gente tenha aquela instrução.

13:18

Como ele vai mostrar o

13:21

operador da conta como disponível, ele vai falar, se você ver

13:27

um outro agente que é melhor, direcione para ele,

13:30

mas ele vai falar, você tem acesso a outras tools,

13:33

mas você precisa prover uma resposta final usando a setToModelResponse tool. Então ele é obrigado.

13:42

Então, nesse caso, se eu tivesse uma situação como essa,

13:46

trabalhar com o modo chat mais o output

13:49

schema dessa forma aqui não seria recomendado. O

13:53

task não vai acontecer isso.

13:56

Mas também eu preciso de ter um modelo,

14:00

e veja que o modelo básico nós não estamos tendo problema, mas é um modelo gratuito.

14:05

Seria melhor usar um

14:08

modelo melhor que esses flashes aqui para teste do Google.

14:12

Outro ponto importante é sobre o que está no System Prompt.

14:16

Nós podemos achar que porque temos o output,

14:20

Não é necessário colocar as informações que nós queremos na saída. Não,

14:26

pelo contrário. Isso aqui é um reforço.

14:28

Isso aqui dá mais confiabilidade para o que a LLM precisa nos retornar.

14:35

Na verdade, aqui poderíamos até colocar no formato JSON.

14:42

Colocar ali o formato bonitinho, feedback, sentimento.

14:45

Isso aqui também é extremamente relevante.

14:48

Então combine isso com o seu output quando você julgar que seja necessário.

14:56

Tem uma outra manha que ela não é nada assim uma boa prática, mas seria possível.

15:03

Uma vez que nós conseguimos determinar essa saída,

15:06

nós podemos colocar aqui que ele vai retornar uma questão para o usuário.

15:15

Esse output pode ser a questão ou feedback sentimento.

15:18

Isso aqui é perigoso porque ele pode retornar tudo junto.

15:22

Ele deveria retornar somente questão, somente feedback

15:28

sentimento. Então você teria que determinar isso aqui, mesmo assim,

15:32

se um usuário mandar algo confuso ou até...

15:39

algo premeditado, pode quebrar o comportamento. Você tem os três campos,

15:44

aí você teria que fazer validações para poder lidar com isso,

15:47

mas isso aqui também seria possível de ser feito,

15:50

mas é aquela coisa que nós estamos lidando

15:52

com um cenário totalmente não determinístico.

15:55

Mas é importante nós sabermos que isso aqui também seria possível de fazer,

15:59

porque às vezes, dependendo do tipo de agente,

16:02

onde que ele vai rodar, dependendo do que ele vai receber,

16:04

isso pode ser perfeitamente possível.

16:07

E nós precisamos trabalhar com um formato mais estruturado.

16:12

Então, aqui nós temos o nosso schema de output.

16:17

Eu não mostrei aqui,

16:19

mas você pode trabalhar também com o schema de input da mesma forma.

16:23

Você consegue determinar o que o agente recebe logo na entrada.

16:28

Isso aqui também é muito relevante.

16:30

Para que você não receba um texto totalmente desestruturado, você pode receber...

16:36

dados exatamente conforme você precisa para trabalhar nesse agente.

## Resumo IA

[RESUMO_IA]