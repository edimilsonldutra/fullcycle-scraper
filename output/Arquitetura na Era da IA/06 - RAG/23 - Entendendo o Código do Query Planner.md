Módulo: Arquitetura na Era da IA\
Aula: [Entendendo o Código do Query Planner](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18444)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior eu mostrei aqui para vocês a diferença que faz esse query planner.

00:06

Eu também mostrei para vocês como é importante os filtros,

00:09

porque se o filtro estiver errado, os documentos que podem vir vão ser errados aqui.

00:13

Então, no nosso caso aqui, o que eu tenho aqui?

00:17

Eu vou começar de trás para frente. Quando nós estamos naquele chat, ou seja,

00:21

quando a gente está fazendo a pergunta, a gente cai naquele while true,

00:25

para ele ficar sempre fazendo um loop de pergunta, mas agora eu tenho...

00:29

algumas coisas que eu não tinha antes, que basicamente são essas linhas aqui.

00:34

O que essas linhas fazem? Primeira coisa,

00:38

ele vai ter um Planner Prompt,

00:40

que vai ser um prompt que a gente tem especificamente

00:42

para ele fazer o entendimento e a classificação,

00:47

baseado na pergunta que o usuário trouxe aqui para a gente.

00:50

Uma vez que eu tenho esse prompt consolidado, baseado na pergunta,

00:55

o que eu vou fazer? Eu vou...

00:59

rodar esse prompt chamando o modelo. Então, nesse momento aqui,

01:03

eu estou fazendo uma consulta no modelo,

01:04

mas eu não estou consultando o modelo para responder algo para o usuário.

01:08

Eu estou consultando o modelo para

01:10

eu classificar a intenção do usuário para

01:15

que eu tenha aquele planejamento como eu mostrei para vocês no vídeo anterior.

01:21

Uma vez que eu tenho a classificação, o resultado aqui, o que eu vou fazer?

01:26

Eu vou pegar e eu tenho uma função de build filters,

01:29

porque os filters vão falar onde o plano é

01:32

igual a PRO e o tipo de documento é SLA.

01:36

É mais ou menos como se fosse um SQL. Então,

01:39

eu tenho os filtros que eu vou utilizar.

01:41

Também, eu vou verificar se o needs clarification for true. Se for true,

01:46

ele vai imprimir a pergunta do needs

01:51

clarification para o usuário responder de volta.

01:54

E vai dar um continuar, porque agora ele nem vai buscar no banco de dados ainda,

01:58

porque ele sabe que ele precisa de mais resposta para fazer a busca. Legal?

02:03

Caso não precise de clarificação,

02:07

vai seguir a mesma coisa que a gente sempre já fez.

02:10

Ele vai buscar os chunks no banco de dados, passando essa query plan,

02:16

onde vai ter exatamente a pergunta que a gente precisa.

02:21

Normalizada que ele vai usar, com os filtros que a gente montou aqui.

02:25

E aí ele vai percorrer todos os documentos

02:28

e vai executar a

02:33

chamada no modelo e retornar,

02:36

que é basicamente o que a gente sempre fazia.

02:38

O que muda aqui é esse cara. Aqui basicamente, tá?

02:43

Agora, como é que esse cara funciona? Eu criei um arquivo específico,

02:47

tem um prompt grande, poderia otimizar esse prompt sim,

02:49

mas eu tentei deixar da forma mais didática possível aqui para vocês, tá?

02:52

Então, basicamente é o seguinte, ele está trazendo aqui oito possíveis...

03:00

chunks que ele pode trazer para ranquear.

03:02

Mas a grande questão aqui que eu quero que você preste atenção é aqui.

03:06

Safe filters. Existem alguns filtros que eu sempre vou trazer hardcoded,

03:11

nesse caso, para ele fazer a busca.

03:13

Que é o status está publicado,

03:14

o tipo de produto é FCIA Cloud e o tenant é FCIA. Então,

03:19

vamos imaginar que eu tenho um login no

03:22

sistema e esse meu login é da empresa FCIA.

03:28

Se eu for fazer um login com outra empresa, o login pode ser FCXPT0.

03:34

Ou seja, eu escolho o tenant. Como aqui é um exemplo,

03:37

eu estou fazendo simplesmente esses filtros safe, hardcoded aqui.

03:41

Mas isso poderia ser critérios na hora que você faz um login,

03:45

na hora que você está fazendo uma busca ou coisa desse tipo.

03:47

Outra coisa importante é quais são os tipos de documento que eu

03:51

tenho e quais são os tipos de plano que eu tenho.

03:53

E eu tenho que fazer esses dados aqui baterem.

03:56

com os tipos de documento que eu fiz a ingestão.

03:58

Ou criar um algoritmo, na realidade,

04:01

que faça uma consulta antes e tenha todos os

04:03

tipos de documento ou coisas desse tipo. Nesse caso,

04:06

eu coloquei hardcoded. E aqui,

04:08

all plans sempre vai ser aplicado para todos os planos,

04:12

caso eu não tenha algum plano escolhido. Então,

04:16

se o plano for none, vai servir all plans. Então,

04:19

ele vai buscar... qualquer tipo de plano nos registros.

04:22

Então isso não vai ser um filtro que vai excluir.

04:24

E aqui eu tenho um System Prompt.

04:26

Eu não quero ficar lendo linha por linha do System Prompt,

04:30

mas eu quero trazer alguns pontos importantes. Uma das coisas,

04:34

eu poderia resumir bem ainda esse System Prompt,

04:36

principalmente porque ele vai ser executado o tempo todo, de forma geral.

04:42

Existem as técnicas de cache e tudo mais,

04:43

mas o grande ponto aqui é, você... é um planejador de retrieval.

04:48

Você não tem que responder pergunta,

04:49

porque eu vou mandar uma pergunta para ele e

04:51

eu não quero que ele responda à pergunta.

04:53

E aqui o que eu fiz? Estou falando aqui para ele o seguinte,

04:57

existe uma base de conhecimento com esses tipos de documento.

05:01

Aí tem aqui SLA, Policy,

05:05

Produto e Plano e Company.

05:07

E ele explica o que significa ou o que se aplica a cada esse tipo de documento.

05:13

E aqui tem as regras.

05:16

Primeiro, verifique se a pergunta pode ter mais uma

05:21

forma de entendimento que pode dar uma resposta diferente. Ou seja,

05:27

se é uma pergunta ambígua. Qual é o tipo de plano?

05:30

Eu tenho um monte de plano. Então, o que eu faço? Então,

05:33

isso aqui ele ensina para falar o seguinte. Olha,

05:36

se tiver alguma coisa que eu possa responder lendo e tendo uma diferença...

05:43

Uma resposta diferente, então isso aqui é true,

05:46

porque eu preciso de questões de clarificação em português.

05:50

Então esse é um ponto importante.

05:53

Outro ponto, normalization question, ou seja,

05:56

reescrever a pergunta em português, self-contida,

06:01

autocontida, de uma forma específica para conseguir trazer a informação melhor.

06:06

Outro ponto, quais são os tipos de documento? Cada documento pode ter uma resposta.

06:10

Então, busque somente dentro dos documentos daquela nossa lista.

06:15

E daí, ele traz ali, Policy and Plan. SSO está dentro de Plan,

06:21

então vai ter o Product também. Então, tem a regrinha basicamente aqui.

06:24

O plano, selecione isso somente quando a resposta for especificamente de um plano.

06:29

Ou comparação de planos, a questão de planos, etc., deixe isso em branco.

06:33

E outra coisa, termos exatos.

06:35

Quais são termos literais que vão ajudar mais para eu fazer o retrieval?

06:41

Exemplo, P1, SSO, Enterprise, etc.

06:43

E aqui eu tenho os exemplos. Para a IA aprender,

06:46

ela aprende muito sobre exemplos. Por exemplo, e se der problema no Enterprise?

06:50

Leia somente uma leitura.

06:54

que é um P1 incident, então ele vai dizer que é o Doctype SLA com o plano,

06:59

o plano é Enterprise, Needs Clarification,

07:01

falso. Se eu coloco, como funciona o suporte da empresa?

07:04

O plano da empresa lê os dois planos e o ponto é,

07:09

qual o plano da empresa que está querendo saber no final das contas?

07:12

Então ele precisa... de uma clarificação.

07:15

O que acontece se eu ultrapassar a cota?

07:17

Aqui são os exemplos que eu dei ali para você. Então, basicamente,

07:20

é isso que acaba acontecendo. Eu filtro e categorizo isso nesse modelo de dados,

07:26

nessa classe, no final das contas. Ou seja,

07:28

onde eu tenho a pergunta normalizada, o tipo de documento, o plano,

07:32

os termos exatos, a clarificação e a pergunta de clarificação.

07:35

E aqui é aquele invoco que eu dou no Planner Prompt.

07:38

Basicamente, eu estou pegando esse prompt, esse System Prompt e...

07:41

estou anexando depois nele a pergunta do usuário. Então,

07:45

é basicamente isso. Então, esse aí é um ponto importante.

07:52

Uma vez que eu tenho a clarificação,

07:54

isso aqui é só uma função para garantir que

07:56

todos os tipos de documento que estão inseridos

07:59

na ingestão são os mesmos documentos que eu tenho

08:02

aqui naquela minha lista de tipos de documento.

08:04

Porque se eu tiver algum diferente, eu vou ter problema.

08:08

Por que eu vou ter problema?

08:10

Porque se eu tiver um documento do tipo privacidade no banco de dados,

08:17

mas privacidade não estiver nessa minha lista do query planner,

08:20

eu jamais vou buscar nada sobre privacidade e

08:23

todos aqueles documentos vão ser ignorados.

08:25

Então, eu acabo trabalhando isso. E aqui é o build filters, né? Então, se o doc,

08:30

se ele consegue entender o doc type,

08:32

ele vai falar que o doc type é in nos planos de doc type.

08:36

Se o plano é in... Nos planos, se não,

08:38

se estiver em branco, ele entra aqui como all plans.

08:40

Então, aqui é na hora que ele faz os filtros.

08:43

E aqui é o build search query. Basicamente,

08:46

ele vai pegar o plano normalizado e vai concatenar

08:50

com os termos exatos que a gente fez.

08:52

Para ele trazer mais informações,

08:55

mais contexto na hora de fazer a busca.

08:57

Que é basicamente isso aqui que ele acaba fazendo.

08:59

Cadê o nosso querido amigo do planejamento? Aqui.

09:04

Qual é a capital da França? Capital... e França.

09:07

São termos exatos que ele concatena dentro da minha pergunta.

09:11

Então é basicamente isso que ele acaba fazendo.

09:14

E agora a busca nos chunks é a mesma coisa.

09:17

Ele vai fazer busca por similaridade com score, vai passar o nosso plano,

09:21

que é o nosso build search query, que é esse cara aqui,

09:25

passando quais são quantos documentos eu quero e com os filtros que eu trouxe.

09:32

E aqui ele só imprime na tela para o nosso debug.

09:35

O que ele acabou planejando. Então,

09:38

se você perceber, eu tenho uma etapa antes disso.

09:41

E essa etapa muda muito a qualidade da resposta.

09:45

Ela faz com que eu use os meus metadados e coisas desse tipo.

09:48

Agora, uma coisa importante que eu quero trazer aqui para você.

09:52

Se você perceber, para cada pergunta que eu tenho que fazer,

09:55

eu vou fazer duas chamadas para o modelo.

09:58

E isso custa, tanto em termos de tempo, quanto em termos de dinheiro e etc.

10:06

O que que muitas vezes é feito, tá, pessoal?

10:09

E às vezes isso pode cheirar mal pra gente.

10:12

Muitas vezes a busca que acaba sendo feita,

10:15

até mesmo para planejamento ou coisa desse tipo, pode ser até uma busca léxica.

10:20

O que que isso significa? Que não necessariamente eu preciso chamar o modelo.

10:24

Eu posso fazer com rejects,

10:25

eu posso ver quais são as palavras-chave que estão sendo

10:28

utilizadas e juntar para criar esse tipo de coisa.

10:31

Então, se você perceber,

10:33

nem sempre para classificar algo eu preciso do modelo. Por exemplo,

10:38

aparece na pergunta parada a palavra enterprise. Opa,

10:42

talvez eu possa colocar dentro do plano que tenha enterprise.

10:47

Ah, você perguntou qual o tipo de... Tudo que é palavra-chave,

10:52

no final das contas, eu posso tentar... Pergunta, qual é o SLA daquele plano? Opa,

10:58

talvez o tipo de documento seja documento de SLA e documento de plano. Então,

11:02

esse tipo de coisa pode ser feito com um monte de if,

11:05

ou seja, algo determinístico mesmo, ou seja, sem chamar o modelo.

11:10

Esse tipo de comportamento faz com que o processamento seja muito mais rápido e, ao mesmo tempo,

11:16

pode fazer com que eu poupe chamadas para o modelo.

11:20

Mas isso vai depender caso a caso.

11:22

Por isso que você tem que entender o sistema,

11:24

o domínio da empresa e verificar. Ou você pode fazer de forma híbrida.

11:28

Você tenta fazer a busca léxica.

11:31

Não deu certo, viu que ficou um monte de buracos ali importantes no planejamento?

11:37

Aí sim você faz a...

11:40

a busca como fallback ali no modelo para tentar classificar um pouco melhor, tá?

11:45

E obviamente se tem buscas que já aconteceram ou

11:48

são muito parecidas e coisas desse tipo,

11:50

né? A gente pode utilizar o cache, a gente já falou sobre cache no passado,

11:54

eu acho que essas coisas vão ficando cada vez mais

11:57

claras e se encontrando e fazendo sentido junto, beleza?

12:00

Então era isso aí que eu queria trazer em relação a essa parte de

12:03

Planejamento e aí a gente já começa a melhorar muito a qualidade do nosso RAG.

## Resumo IA

[RESUMO_IA]