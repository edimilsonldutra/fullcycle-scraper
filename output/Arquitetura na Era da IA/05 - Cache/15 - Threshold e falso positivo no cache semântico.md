Módulo: Arquitetura na Era da IA\
Aula: [Threshold e falso positivo no cache semântico](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18351)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, a gente tinha chegado naquele ponto onde nós conseguimos

00:05

gerar um dado para gravar no banco de dados,

00:09

onde a gente consegue fazer uma busca semântica.

00:12

E agora a nossa ideia é o quê?

00:15

Nós termos ali o nosso endpoint que ele vai conseguir fazer a nossa busca.

00:21

E, na realidade, nesse momento, o que acontece?

00:26

A gente vai verificar...

00:28

O threshold, o threshold basicamente é a linha de

00:31

corte onde eu falo que a similaridade ela é

00:37

tão grande ou tão longe daquilo que eu posso

00:41

aceitar esse cara como o cache que eu vou utilizar,

00:45

ou seja, como meu best match,

00:47

mas a gente tem que tomar cuidado com isso pra gente não ter casos de falso positivo.

00:51

Porque não é porque a gente tem uma distância curta entre um vetor e

00:55

outro que significa que aquele cara é o cara que a gente vai utilizar.

00:59

Por isso que quando a gente trabalha com threshold, a gente fala,

01:02

olha, não é porque esse cara tem uma similaridade X

01:06

que ele vai ser necessariamente o cara que eu vou usar.

01:10

Então eu posso, através de um threshold,

01:11

colocar uma pontuação mínima que eu acho que...

01:16

eu posso ter de confiança para trabalhar.

01:19

E aí vai variar muito o nível de risco que você tem. Eventualmente,

01:24

você pode trabalhar ali com uma pontuação menor

01:26

ou uma pontuação mais restritiva para evitar falsos positivos,

01:31

por exemplo. Então, o que acontece aqui?

01:35

Se você olhar, eu tenho agora aqui uma função chamada Evaluate Best Match.

01:42

Basicamente, o que ela vai fazer?

01:45

Ela vai verificar se das matches que ela encontrou, ou seja,

01:50

de todas as buscas que ela encontrou para fazer a busca semântica,

01:54

ela vai verificar se isso passa pelo nosso threshold,

02:00

por aquele limite mínimo que eu falei aqui para vocês.

02:03

Então, ela vai fazer a busca da mesma forma como ela fez,

02:06

vai trazer o resultado ali para a gente,

02:09

tudo certinho como a gente sempre acabou fazendo. Mas nós temos uma...

02:14

uma evaluate best match. Então,

02:16

ela vai pegar um cara que tem o maior nível de similaridade. Porém, ainda assim,

02:21

ela vai verificar se esse cara, ele é maior ou igual ao threshold.

02:28

Porque se ele for maior ou igual,

02:29

eu dou ele como accepted. E se ele está como accepted,

02:33

eu posso vir a utilizar ele como um cache.

02:36

Agora, se ele está como rejeitado, significa o quê? Que mesmo dele ter sido similar,

02:43

a pontuação dele, o threshold dele não chegou no nível que eu queria.

02:48

Então, eu vou preferir, por exemplo,

02:50

chamar a IA de novo. Então,

02:51

essa que é a ideia quando a gente está trabalhando dessa forma,

02:56

onde a gente consegue verificar. Então,

02:58

o importante aqui é você ficar ligado com falsos positivos,

03:02

porque isso vai fazer uma diferença gigantesca.

03:05

Vamos rodar esse cara aqui para a gente dar uma olhada nesse cara. Vamos aqui.

03:15

Configuração atual do banco, criar manual do cache semântico.

03:18

Criar outro item manual.

03:20

Aqui, ativar candidato bom. Vamos,

03:23

deixa eu achar aqui, similares no cache semântico.

03:26

Então, primeira coisa, eu vou fazer uma busca similar aqui.

03:30

Baseado nesse cara, deixa eu adicionar mais itens aqui,

03:33

na realidade, para ficar um pouquinho melhor.

03:35

Criar um item manual. Deixa eu olhar aqui. Eu tenho análise, análise.

03:40

Eu tenho aqui um criar um item manual.

03:42

Esse cara eu já tenho da assinatura. Deixa eu colocar esse outro cara aqui.

03:50

E deixa eu colocar esse cara aqui também,

03:52

só para garantir. Não sei se ele já existe,

03:54

mas eu quero mais dados aqui no meu banco de dados para trabalhar.

03:58

Eu vou fazer uma busca de dados similares no que a gente já tinha feito.

04:02

Ótimo. E aqui eu quero avaliar o candidato bom. Vamos ver. Então,

04:08

o que eu vou fazer? Eu tenho aqui, preciso cancelar meu plano. Então,

04:12

eu estou passando que o threshold é de 0.9. Então,

04:15

quando eu der um enter aqui, o que vai acontecer? Ele vai,

04:19

preciso cancelar meu plano, o threshold é de 0.9,

04:22

tive 3 resultados e a decisão foi aceita,

04:25

porque um dos caras teve a similaridade de 0.94.

04:30

Então, se eu olhar aqui, dos meus candidatos que eu tive,

04:34

o meu best match foi esse cara aqui.

04:36

E a similaridade dele foi de quanto? De 0.94. E nesse caso,

04:42

então... Nesse meu best match, eu estou aceitando esse cara.

04:46

Dos candidatos, foram esse cara,

04:49

mais esse cara e mais esse cara aqui. Ou seja, de três possibilidades,

04:54

um para mim foi o meu best match e desse best match,

04:57

eu aceitei porque o threshold dele bateu. Se eu chegar aqui,

05:03

por exemplo, a um caso perigoso, eu vou colocar aqui,

05:07

vamos ver se esse cara aqui, ver se ele vai ser rejeitado ou não. Olha aqui.

05:14

Quero cancelar a minha reunião de amanhã. Está vendo que o threshold é 0.9.

05:19

Eu consegui trazer os três resultados, mas a decisão foi rejeitada.

05:23

Por quê? Porque a minha similaridade era 0.66.

05:28

Então perceba que o quero cancelar minha é algo muito

05:32

mais perto do que aquilo que está no banco de dados.

05:35

Mas quando ele colocou assinatura, isso aí mudou completamente e a...

05:41

E a similaridade acabou baixando o nível do 0.9.

05:46

E aí a gente tem esse tipo de coisa.

05:48

Se eu fizesse e usasse um threshold um pouco menor,

05:52

deixa eu colocar aqui, um 0.6, o que aconteceria?

05:57

Ele teria aceitado isso como cache.

06:00

E aí eu teria o problema que eu não quero ter.

06:04

que é retornar a resposta errada para o cara. Imagina que eu vou lá e coloco,

06:08

quero cancelar meu plano, quero cancelar minha reunião,

06:11

e de repente a resposta que o sistema retorna para mim é,

06:16

ok, a sua reunião vai ser cancelada,

06:19

etc, etc. Não tem nada a ver com o plano. E por que isso acontece?

06:24

Por conta que o threshold aqui nesse caso estava muito baixo,

06:27

e aí quando ele está muito baixo,

06:29

a chance de eu pegar e ter falso positivo é maior.

06:32

Então... Essa calibragem aqui é algo extremamente importante e

06:36

vai depender do contexto que você tiver.

06:38

Quanto mais crítico é o tipo de pergunta, o tipo de solicitação,

06:43

mais você tem que ser restritivo para garantir que a similaridade seja muito,

06:49

muito parecida para que você consiga reutilizar isso.

06:53

Então isso é muito mais decisão de negócio da aplicação,

06:56

não existe uma fórmula mágica,

06:57

o grande ponto é você saber que você tem que lidar com esse tipo de situação. Fechou?

## Resumo IA

[RESUMO_IA]