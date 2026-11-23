Módulo: Arquitetura na Era da IA\
Aula: [Testando retrieval isolado](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18436)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, e agora a gente tem, finalmente, um retrieval. Então,

00:07

eu criei, a gente tem esse arquivo retrieve.py, e esse arquivo,

00:11

o que ele vai fazer no final das contas?

00:14

Ele vai fazer aquela busca vetorial no banco de dados.

00:20

Então, somente para a gente entender alguns pontos que a gente acabou falando,

00:24

mas vale a pena trazer aqui.

00:27

Primeira coisa. A gente tem aqui uma constante chamada Default Top K.

00:33

O que significa isso? Top K, basicamente,

00:37

vai ser a quantidade de registros que vai

00:39

ser trazido baseado na pesquisa que a gente faz.

00:44

E isso, basicamente,

00:46

se reflete em bastante coisa. Por exemplo, às vezes,

00:49

eu posso ter um sistema onde, nesse sistema, eu quero...

00:54

e preciso trazer a maior quantidade de

00:56

informação relevante possível para eu verificar.

01:01

Então, ao invés de eu trazer 5, eu posso trazer 10,

01:04

eu posso trazer 20. Aí eu escolho a quantidade de chunks,

01:07

no final das contas, que vão vir no meu banco de dados.

01:10

Isso não significa que eu vou usar os 20. Lembra?

01:14

A gente está falando ali de candidatos a serem utilizados.

01:18

Então, nesse caso, eu coloquei aqui 5,

01:20

nós temos aqui o filter fields, que vai ser utilizado para filtrar,

01:25

e o preview limit é somente para a gente poder olhar ali na saída no nosso terminal.

01:31

E aqui são argumentos que eu posso passar, ali, tipo,

01:37

quantos top K eu quero passar, qual o parâmetro,

01:39

ou seja, eu consigo fazer filtros aqui.

01:41

para facilitar a minha vida na hora de eu trabalhar. Então, vamos lá.

01:46

Aqui eu tenho uma Insure Collection Ready.

01:49

Isso aqui é só para verificar se realmente o banco

01:51

de dados e essas coisas estão no ar.

01:53

Novamente, pessoal, é exemplo. É óbvio que em um sistema que você vai fazer,

01:56

você não vai criar uma função de Insure Collection Ready dessa forma.

02:01

Mas é importante você saber.

02:04

Aqui a gente tem a nossa função de se conectar com o banco de dados.

02:09

Então, nesse caso, a gente está usando o Pinecone Vector Store.

02:12

Isso vem do Langchain. Mas, basicamente, para todos os bancos de dados de mercado,

02:18

você tem um Vector Store implementado no Langchain. Então, por exemplo,

02:23

se você quer utilizar, sei lá, o Pinecone, então, provavelmente,

02:26

você vai ter lá um Pinecone Vector Store. Então,

02:30

aqui a gente está utilizando o Pinecone Vector Store.

02:32

Porque é o Postgres que normalmente a gente tem na nossa aplicação.

02:36

Mas dependendo da situação, você pode optar por outro banco de dados.

02:40

Então, aqui ele vai fazer a conexão com o banco de dados.

02:43

Aqui é o ponto onde a gente consegue formatar os filtros,

02:47

onde eu posso passar --status igual a x, --tenant igual a y.

02:53

Então, eu posso escolher aqui para eu conseguir fazer os filtros.

02:56

Ou seja, a formatação dos filtros.

02:58

E aqui é para eu printar o resultado. Então, a ideia é trazer os metadados,

03:02

um pouco do resumo do que foi encontrado.

03:05

Aí o score que a gente teve, ou seja,

03:08

Basicamente, o grau de confiabilidade que a gente tem naquela aplicação.

03:12

A gente tem o Chunk ID, ou seja, o pedaço do chunk.

03:15

A gente tem de onde veio esse cara,

03:18

qual é o título dele. Se ele tiver a parte de sessão, traz a sessão. Aí o plano,

03:23

o type, o version status e o preview.

03:24

Basicamente, são essas informações aqui de metadados.

03:27

E aqui o nosso arquivo main, basicamente,

03:30

onde eu posso fazer a minha pergunta. Ele vai pegar os filtros.

03:33

E aqui que vem a grande sacada, tá? Por quê?

03:37

Uma vez que eu tenho como eu quero filtrar,

03:39

olha isso aqui. Basicamente,

03:40

é essa linha que está fazendo a mágica que vem

03:43

de implementação aqui do Langchain nessa parte do Store.

03:47

Então, se você ver, eu tenho aqui,

03:48

buscando por similarity search with... O que significa?

03:53

Ou seja, ele vai fazer uma busca de similaridade trazendo também o score.

03:57

E aqui eu coloco a query que eu quero. Ou seja,

04:01

a query, o que significa no final das contas?

04:03

Ele vai pegar a nossa pergunta, tá? E por trás dos panos,

04:08

ele vai transformar essa pergunta em um vetor também.

04:12

Por quê? Porque baseado nesse vetor, ele consegue fazer a busca por similaridade.

04:18

Então, isso aí é um ponto importante.

04:21

Ou seja, a busca que acontece por similaridade,

04:25

ela tem as duas etapas. A primeira etapa, onde ele pega a pergunta que eu tenho,

04:30

o ponto que eu quero buscar, e ele bate isso contra o banco de dados. Então, aqui,

04:37

se você olhar, eu tenho a query,

04:39

que é basicamente o que a gente está pegando de resultado.

04:42

O key aqui é aquele top key que a gente tem. O filtro...

04:47

São aqueles filtros que a gente pode passar ali no programa.

04:51

E aqui, esses filtros ajudam demais. Por quê?

04:54

Porque evita eu percorrer todo o banco de dados.

04:58

Então, se eu quiser fazer uma busca mudando a quantidade de resultados,

05:02

mudando o tenant,

05:03

mudando quais são as opções que a gente tem mesmo, a versão, o status, o plano.

05:09

Então, todos esses filtros aqui que a gente acaba colocando aqui como argumento,

05:15

acabam nos ajudando, no final das contas,

05:19

a poder filtrar e fazer com que a nossa query seja muito mais rápida e específica.

05:25

Então, novamente, pessoal, esses filtros,

05:28

esses metadados são uma das coisas mais importantes para você fazer um resultado decente.

05:34

Então, eu vou rodar algo sem nenhum filtro, vou colocar aqui 10 candidatos por padrão.

05:41

Então, deixa eu rodar aqui.

05:45

python -m .app .retrieve.

05:50

A questão é me

05:53

Fale sobre SLA.

05:59

Ele está pegando o 'me fale sobre SLA' e transformou

06:03

isso em vetor e bateu no banco de dados. Então,

06:06

se você olhar aqui, olha só o que vai acontecer.

06:10

Ele trouxe o retrieval, aqui o início do teste, a query 'me fale sobre SLA',

06:16

o top key é 10.

06:18

Nenhum filtro eu usei e ele trouxe 10 resultados.

06:21

Agora que a questão é o seguinte, olha só. Score, 0.51. Ele trouxe o Chunk ID.

06:27

E por isso que eu gosto de no Chunk ID ter um nome, né? Fácil,

06:31

porque aqui eu já sei que ele tá vindo um determinado cara.

06:33

Apesar que eu poderia vir o Search também.

06:36

Então eu sei de qual documento isso veio. Eu sei de qual título que isso veio.

06:40

De qual sessão que isso veio. Tá vendo? Qual é o plano?

06:44

Serve pra todos. Qual o tipo de documento?

06:46

SLA? Versão? Está publicado ou não? E aqui ele tem um preview,

06:50

para que o SLA seja aplicável,

06:52

o cliente deve classificar e etc. Mas se você ver,

06:55

eu perguntei o quê? Me fale sobre SLA.

06:58

Então, ele está trazendo alguma informação sobre SLA.

07:01

Se você olhar aqui, 0.56 é um outro pedaço.

07:05

Aqui também, deixa eu ver. Aqui, pedaço 9 desse chunk. Aqui é 0.57.

07:11

Aqui é 0.58.

07:14

E conforme vai subindo esse score,

07:17

maior a chance daquilo ter relevância para a gente. E aí,

07:22

aqui ele vai até no 0.64 de relevância aqui para a gente.

07:27

E aqui tem os valores. Então, esse aí é um ponto.

07:31

Se eu pegar aqui e vou colocar quais

07:38

planos eu tenho disponível.

07:45

E aqui ele vai trazer os scores.

07:49

novamente, e os recursos.

07:50

Então perceba que ele vai pegando os pedaços daquilo que eu tenho. Então, a versão,

07:56

e aqui ele traz aplicável ao plano Enterprise.

08:00

Perceba que ele não trouxe uma lista de planos.

08:02

Aqui está falando do plano Starter, está falando do plano Pro,

08:06

mas perceba que eu não tenho necessariamente algo

08:09

falando especificamente sobre uma lista de planos.

08:12

Perceba que ele está achando tudo que tem a ver com o plano referente

08:18

aquilo, ó, plano para empresas, a contratação anual do plano Pró,

08:22

então perceba que ele vai trazendo essas informações até

08:25

tentar ter o que tem mais confiabilidade,

08:27

ó, política comercial, planos mensais, etc, anuais, etc,

08:31

aqui ele traz. O que pode acontecer aqui nesses casos,

08:35

tá, só pra você saber, inclusive ele tá,

08:37

acho que buscando por inverso os registros,

08:41

deixa eu colocar aqui 30, depois eu posso mudar a...

08:46

O argumento da ordem, para ele trazer o score baseado...

08:50

Quais os planos disponíveis?

09:00

Aqui, 30. O score começa a subir. É invertido. Mas, de qualquer forma,

09:05

perceba que ele traz chunks aqui para a gente. Se você olhar aqui, Enterprise,

09:10

o tipo é plano. E aqui, se você olhar,

09:13

ele tem como se fosse uma tabela de planos aqui para a gente. Se você olhar.

09:18

Tá vendo? Então, o que eu posso fazer também na minha busca?

09:21

Eu posso colocar retrieve, eu acho que é "-type", igual a plan.

09:28

Vamos ver se é isso que funciona. Deixa eu ver,

09:30

"-product", "-plan". Ah, é "-plan". E

09:37

aqui, eu poderia passar o nome do meu plano,

09:40

que eu acho que não tem algo específico com o nome do plano.

09:43

Eu posso colocar, sei lá, starter. Acho que ele não vai achar nada. Me fale,

09:50

explique sobre...

09:55

O plano... Vou

09:58

colocar. O que tem no plano.

10:04

É, ele não tem nenhum plano específico nos metadados com o plano starter. Tá vendo?

10:09

Mas se ele tivesse, ele ia trazer,

10:10

mas ele ia trazer específico do plano starter, tá?

10:13

E aí que eu acho que a coisa,

10:14

ela começa a ficar mais interessante, tá? Porque isso aí acaba mudando muito,

10:19

muito, muito daquilo que a gente quer trazer.

10:21

Deixa eu tentar pegar alguma outra informação.

10:24

Mas... É basicamente isso, ó.

10:26

Eu tenho os tipos de documento e tudo isso vai ser baseado no quê,

10:30

no final das contas? Nos documentos, né? Então, ó,

10:32

enterprise plan, né? É que o doc type tá aqui como plan apenas.

10:37

Eu poderia colocar uma outra... Ah, tem um plan igual ao enterprise na realidade, né?

10:43

Deixa eu ver se eu tenho um documento desse, menos menos plan. Enterprise. Enterprise.

10:54

Me fale sobre o plano.

10:59

Aqui, ele achou. A gente tem um arquivo específico do plano Enterprise.

11:04

Agora, se você olhar aqui,

11:07

uma das coisas que é mais importante que você se ligue

11:10

é que o filtro que eu fiz é Enterprise. Então,

11:13

se eu tivesse outros documentos com outros tipos de plano e eu pergunto sobre plano,

11:18

não interessa.

11:20

Como eu fiz o filtro para o Enterprise,

11:21

todos os documentos que eu sei que vão ser trazidos aqui são do plano Enterprise.

11:27

Então, eu não fico preocupado em trazer informações do plano starter,

11:31

porque ele vai fazer a busca nos documentos onde o metadado,

11:34

o tipo de documento é plano e o plano é o Enterprise,

11:37

por exemplo. Então, eu posso falar qual o plano,

11:41

me fale mais informações do plano. Se o filtro for Enterprise...

11:45

Vai ser óbvio que ele só vai fazer buscas e trazer informações do plano Enterprise.

11:50

Logo, eu não preciso que na busca do usuário esteja escrito plano Enterprise.

11:55

Obviamente, eu tenho que tentar entender a intenção do usuário.

11:58

Vai depender do filtro,

11:59

das coisas como isso acontece.

12:00

Mas o importante é você entender que filtrar é extremamente importante.

12:05

No próximo vídeo,

12:06

a gente vai seguir um pouco mais essa linha e a gente vai avançando aí.

12:10

O importante é você entender que a gente tem esse Retriever.

12:14

E ele está fazendo essa busca vetorial para a gente. Beleza? Vamos nessa então.

## Resumo IA

[RESUMO_IA]