Módulo: Arquitetura na Era da IA\
Aula: [Miss semântico e gravação automática no pgvector](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18354)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, e agora a gente vai aqui nessa nossa última parte,

00:05

que no final das contas segue bem a mesma estrutura da última que a gente fez,

00:11

porém, o que acontece?

00:12

A única diferença é que quando não há nada,

00:19

ou seja, quando a IA não, a IA não,

00:23

quando o nosso sistema não consegue dar nenhum hit,

00:25

nem no semântico e nem no hit exato, o que vai acontecer?

00:30

ele vai guardar isso tanto na memória,

00:33

mas ele também vai salvar isso no cache semântico também.

00:38

Então daí, isso vai me ajudar,

00:40

porque se em algum momento eu fizer uma pergunta parecida,

00:43

eu vou usar o cache semântico por conta dessa pergunta anterior.

00:49

Eu zerei meu banco de dados,

00:51

dei um docker-compose down -v para zerar meu banco,

00:54

subi de novo o banco de dados, e aqui... O que eu fiz?

00:59

Deixei mais organizado para ficar mais fácil para testar.

01:02

Então, threshold 0.9 é o padrão,

01:04

mas estou dando aqui somente para a gente deixar certo.

01:09

E aqui, a primeira coisa, eu vou mandar a minha primeira mensagem sem nenhum cache.

01:14

Então, vai chamar a IA e vai salvar no PG Vector. Então,

01:18

o source aqui vai ser como AI model. Então, deixa eu dar um send aqui.

01:23

Beleza, então ele deu um cache miss,

01:25

a IA foi chamada, o semantic cache foi rejeitado,

01:29

porque não tinha nenhum, chamou a IA true, foi salvo no cache,

01:33

teve o item ID lá no nosso banco de dados,

01:36

teve uma chamada IA e a chamada foi cancelada aqui.

01:40

Se você olhar, o AI model é o source, porque ele teve que chamar a IA. Agora,

01:46

o que eu vou fazer? Eu vou fazer a mesma busca, com a mesma palavra aqui.

01:52

Então, quando eu der um send request, ele vai dar um exato hit. Por quê?

01:57

Estava na memória aquilo ali. Então, ele nem precisou fazer o quê?

02:01

Busca semântica e nem precisou gravar no cache semântico,

02:05

porque isso já estava na memória. Então, eu não precisei chamar a IA.

02:09

Agora, o que acontece?

02:11

Eu vou mandar uma mensagem parecida.

02:13

Eu preciso cancelar meu plano ao invés de quero cancelar meu plano.

02:17

Então, vou enviar isso aqui.

02:20

E o que vai acontecer?

02:22

Ele vai dar um hit no cache.

02:25

A IA não foi chamada, porém, não foi memória.

02:30

Ele teve que chamar o banco de dados. Então, ele deu um semantic cache.

02:34

Ele não precisou gravar no banco de dados,

02:37

porque ele já tinha achado algo parecido, a similaridade foi de 0.94,

02:43

e não precisou fazer a chamada para a nossa querida IA nesse momento.

02:48

Então, por isso que acabou acontecendo isso. Agora,

02:52

eu vou mandar uma mensagem diferente, sem um candidato bom. Então,

02:57

a IA vai ter que chamar a IA e salvar isso para a gente.

03:00

Então, eu coloquei, meu aplicativo está travando ao abrir.

03:03

Então, quando eu der um send request, o que vai acontecer?

03:08

conseguiu ter um cache semântico adequado.

03:11

Ele teve que chamar a IA, salvou no banco de dados.

03:15

Agora, no total,

03:17

a gente teve duas chamadas para IA e a categoria é Technical Support.

03:20

Provavelmente, agora, você deu um Send Request.

03:23

Ele nem vai passar pelo cache semântico, porque a gente já está na memória,

03:28

o fingerprint foi exatamente o mesmo. Então, se você olhar,

03:32

agora a gente tem uma visão completa dessas camadas sendo chamadas.

03:36

E a vantagem de a gente sempre salvar no banco de dados,

03:39

quando a gente não dá um hit exato nesse caso,

03:43

é que se alguém fizer alguma pergunta parecida, ele consegue... de forma geral,

03:48

fazer essa busca semântica e trazer o resultado sem

03:52

fazer com que a gente tenha que chamar a IA.

03:56

Então, esses exemplos, galera, que eu acabei dando aí para vocês,

03:59

de forma geral, eles serviram principalmente para quê?

04:02

Que você consiga entender essas camadas que acabam existindo no meio da história.

04:08

Cache pode parecer algo básico, de forma geral, para muita gente.

04:12

Mas, de forma geral, quando a gente trabalha com IA,

04:15

a gente acaba tendo essas mudanças e isso aí vai ajudando,

04:20

por isso que eu quis tentar ser o mais detalhado possível,

04:22

passando passo a passo aqui para vocês.

## Resumo IA

[RESUMO_IA]