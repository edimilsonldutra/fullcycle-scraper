Módulo: Arquitetura na Era da IA\
Aula: [Buscando respostas parecidas com pgvector](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18350)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, na parte prática anterior, o que a gente fez no final das contas?

00:06

A gente conseguiu pegar um item e inserir no banco de dados ali.

00:10

E aí a gente conseguiu, no final das contas,

00:12

ter esses dados que a gente passou de forma vetorizada no banco.

00:16

Agora, a gente entra num outro aspecto,

00:20

que agora a gente vai fazer uma busca no

00:22

banco de dados para verificar a similaridade e a distância.

00:28

entre a frase que a gente está passando em

00:34

relação àquilo que está no banco de dados.

00:36

Então, se a gente olhar aqui para cá,

00:38

eu tenho agora uma semente que traça o cache/search. Então,

00:42

o que a gente vai fazer no final das contas aqui? Primeira coisa,

00:47

a gente vai pegar o request que a gente recebeu

00:50

e a gente vai gerar o fingerprint dele.

00:52

Aí, o que a gente vai fazer? A gente vai...

00:55

pegar esse fingerprint com os dados todos aqui, com o dado normalizado,

00:59

e a gente vai gerar um embedding disso.

01:01

Então, nesse momento,

01:02

eu tenho o embedding que eu acabei de receber na minha request.

01:07

Não tem nada a ver isso aqui com o banco de dados ainda.

01:11

E agora, o que eu vou fazer? Eu vou fazer uma busca.

01:15

Está vendo aqui? Search similar semantic cache items. O que eu vou fazer?

01:20

Eu vou passar qual é a versão do meu prompt.

01:22

Qual que são as rules versions, qual que é o model capability,

01:25

qual que é o embedding que eu acabei de gerar, e qual é o limite.

01:29

O limite é quantos itens eu quero trazer baseado nessa busca.

01:33

E por que eu estou passando todas as versões?

01:36

Porque na hora que eu rodar no banco de dados,

01:38

eu vou fazer um select aqui. Onde o Prompt Version é isso,

01:42

onde o Rules Version é isso, onde o Model Capability é isso.

01:46

Então, ele já vai fazer o filtro automático,

01:48

como se ele fizesse o filtro ali da nossa fingerprint de forma automática, tá?

01:52

E depois que ele faz essa busca, o que a gente vai fazer?

01:56

A gente vai trazer aqui, né, todos os caras que eles...

02:03

foram encontrados e que tiveram, vamos dizer ali,

02:07

uma distância próxima ao nosso vetor que a gente tem no banco de dados.

02:14

Então, é basicamente isso que acabou acontecendo. Então,

02:17

a gente tem a nossa busca semântica.

02:19

Ele pega o que a gente recebeu,

02:21

vai no banco de dados,

02:22

faz uma busca e vê a distância em relação ao vetor que a gente tem.

02:29

que a gente acabou de gerar em relação ao vetor que

02:31

a gente está comparando lá no banco de dados.

02:34

E somente para você saber aqui como que eu faço essa busca aqui.

02:39

Eu tenho aqui no meu arquivo db.py um SQL simples.

02:45

E somente para você saber, quando eu trabalho com o Wi-Fi...

02:48

aqui, eu crio como se fosse uma subquery,

02:51

para que eu não tenha que ficar fazendo a

02:54

comparação e transformando esse cara no embedding o tempo inteiro.

02:59

Então, quando eu tenho query embedding,

03:00

eu consigo reutilizar esses dados do vetor para que eu não precise ficar...

03:07

utilizando ele para cada item que eu vou fazer a comparação.

03:11

Então, ele vai fazer o select, trazendo o id,

03:15

o input text, o texto normalizado, o response, etc.

03:18

E aqui que tem uma coisa interessante que eu quero que você perceba.

03:24

Eu tenho aqui o embedding e aí eu tenho, se você perceber,

03:29

esse maior, igual e menor aqui. O que é isso aqui?

03:33

É a forma de como ele vai buscar lá no banco de dados,

03:40

verificando a distância de um vetor para o outro, utilizando,

03:44

vamos dizer, nesse caso, a fórmula no formato de cosseno.

03:48

Normalmente, a gente tem forma euclidiana por cosseno,

03:51

por produto, etc. Para texto, normalmente,

03:54

a gente trabalha com a distância de cosseno. Então, nesse caso,

03:58

o que acontece aqui? Ele está fazendo e trazendo, basicamente...

04:03

Esse cara baseado nessa distância. E aqui embaixo, se você perceber,

04:08

eu tenho um menos esse cara aqui. Ou seja,

04:13

esse camarada que eu estou trabalhando dessa forma, ele é chamado de distância,

04:20

onde eu faço a comparação de um vetor com o outro.

04:23

Esse outro cara aqui que eu estou trazendo é um menos a distância.

04:28

que eu chamo de similaridade,

04:30

onde nesse caso eu estou pegando o valor arbitrário entre 0 e 1,

04:34

quanto mais próximo a 1, mais similar ele é.

04:38

Se ele for idêntico, ele vai ser 1 aí naquele caso. Quer dizer, ou seja, se bater 1,

04:44

significa que a similaridade desse cara, os vetores são idênticos,

04:48

logo a gente está falando do mesmo cara.

04:50

Daí ele vai falar from a tabela, cross, e aí ele vai...

04:54

verificar entre o prompt version, o rules, o model e etc.

04:59

E esse cross join que ele faz é para que ele não

05:02

tenha que ficar rodando vários selects ali ao mesmo tempo em relação,

05:07

porque ele vai fazer isso a cada registro que ele trazer aqui para a gente.

05:11

Então, e o toPG vector é quando a gente vai,

05:17

como que se diz?

05:20

É aquela função helper que a gente tem para ele

05:22

deixar o vetor adequado para o Postgres para a gente. Então,

05:27

aqui são os dados que eu estou passando para ele fazer a busca ali no começo.

05:32

Então, é basicamente isso que ele faz.

05:34

Eu acho que o ponto importante dessa query é você entender isso.

05:37

Aqui ele vai verificar a distância.

05:39

E aqui esse 1 menos, a gente vai atribuir a similaridade entre um cara e outro.

05:46

Mas uma coisa que é importante você saber,

05:48

não é porque um vetor tem um nível de similaridade

05:54

que necessariamente ele vai poder ser utilizado como cache nessa história.

06:00

E aí que a gente não pode confundir as coisas.

06:02

Não é porque um vetor tem nível de similaridade, ele tem cache.

06:05

O que a gente está conseguindo agora aqui é

06:08

ter uma lista de candidatos a possíveis caras...

06:11

que vão poder ser utilizados como cache. Então,

06:14

essa que é a ideia. Se eu chegar agora aqui no meu teste .http,

06:19

eu posso dar aqui um search aqui para a gente. Vamos dar um search.

06:26

E aqui, olha só o que ele trouxe.

06:27

Preciso cancelar meu plano. O limite 5, ele trouxe 3 resultados.

06:32

E o cara que tem a melhor similaridade, ele trouxe de 0.94.

06:37

E aqui... tal resultado que a gente tem. Então, a query foi,

06:40

Preciso cancelar meu plano, o texto normalizado, o modelo de embedding,

06:44

as dimensões, os filtros, onde a gente trabalhou com o prompt,

06:48

com as rules, com o modelo, quantos caras a gente trouxe,

06:51

foram três itens, e aqui ele traz item por item.

06:54

Quero cancelar meu plano, aqui a distância que esse cara tem, e a similaridade,

06:59

e o resultado disso que estava no banco de dados,

07:02

que é quero cancelar meu plano, cancellation,

07:04

e a confidence é 0.9. Aqui eu tenho um segundo cara, como cancela minha assinatura.

07:09

Se você perceber, a similaridade dele já vai mais longe, ele já vai para 0.66,

07:14

diferente do 0.94, porque eu quero cancelar meu plano,

07:20

já é muito mais parecido do que o preciso cancelar

07:25

meu plano do que algo a ver com assinatura.

07:28

E o de cobrança,

07:29

ele vai também a 0.46, porque ele está mais longe, tá? Então,

07:35

eu tenho esses candidatos a serem os meus caches,

07:37

eu tenho quais são os caras que estão mais similares nesse momento,

07:41

mas não necessariamente eu decidi que eu vou usar esses caras. Então, nesse momento,

07:45

esse vídeo foi muito mais pra gente entender essa busca

07:49

que ele faz no valor que eu entrei,

07:51

com o valor que tá no banco de dados,

07:53

onde eu vou ter uma lista de candidatos possíveis pra eu trabalhar com cache.

07:57

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]