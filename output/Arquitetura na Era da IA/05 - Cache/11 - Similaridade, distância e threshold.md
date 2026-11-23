Módulo: Arquitetura na Era da IA\
Aula: [Similaridade, distância e threshold](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18347)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente gerou embeddings de alguns textos e viu que

00:06

o retorno de um modelo de embeddings não é uma resposta numa linguagem natural.

00:10

Ele retorna um vetor, uma representação numérica daquele texto. Agora a pergunta é,

00:16

o que a gente faz com esse vetor? E a resposta curta é, a gente compara.

00:21

Só que essa comparação não é igual a duas strings. Quando eu comparo texto puro,

00:26

normalmente eu estou perguntando se uma coisa é igual a outra.

00:30

Quando eu comparo embeddings,

00:31

eu estou tentando entender a proximidade, ou seja,

00:34

dois textos podem ser diferentes nas palavras,

00:38

mas eles podem, vamos dizer assim,

00:41

ter um significado ali muito próximo. Por exemplo,

00:44

como eu cancelo a minha assinatura e quero cancelar meu plano?

00:48

Provavelmente não vão gerar embeddings,

00:50

mas... do que como cancelo minha assinatura e não consigo acessar a minha conta.

00:57

Isso não quer dizer que o modelo entendeu tudo como um humano entenderia.

01:01

Quer dizer que dentro daquela representação numérica,

01:04

esses textos ficaram ali mais próximos. E aí que entram duas ideias,

01:09

distância e similaridade.

01:12

A distância tenta responder o quão longe um vetor está do outro.

01:18

Quanto menor a distância, mais próximos eles estão.

01:21

Já a similaridade, normalmente, é apresentada no sentido oposto.

01:27

Quanto maior a similaridade, mais parecidos eles são.

01:32

Então, dependendo da ferramenta,

01:34

você pode ver isso de formas diferentes.

01:36

Em algumas APIs ou bancos, você ordena pela menor distância.

01:42

Em outras, você trabalha com uma pontuação de similaridade maior.

01:46

O importante é não se prender ao nome da função.

01:50

O que importa é entender o comportamento. Vamos dizer assim,

01:55

eu quero encontrar os itens semanticamente mais próximos.

02:00

Quando a gente usa o PG Vector,

02:02

por exemplo, uma extensão ali que a gente utiliza junto com o Postgres,

02:05

a gente vai fazer uma busca ordenando pela distância entre

02:10

embeddings da nova mensagem e os embeddings que já estão salvos.

02:15

O banco vai retornar os mais próximos.

02:18

Só que retornar os mais próximos ainda não significa

02:22

que a gente deve reutilizar a resposta.

02:26

E esse é o ponto que muita gente erra.

02:28

Busca por similaridade encontrada, ela encontra candidatos, vamos dizer assim.

02:33

Ela não toma, de forma geral, aquela decisão final. Se a mensagem nova,

02:38

quero cancelar meu plano, e o banco encontra uma resposta antiga,

02:42

como cancela minha assinatura,

02:44

talvez esse seja um bom candidato para cache semântico. Agora,

02:48

se a mensagem nova é, quero cancelar minha reunião,

02:52

pode parecer algum... Pode aparecer, vamos dizer assim,

02:55

alguma proximidade por conta da palavra cancelar.

02:59

Mas a intenção é outra. Se a gente reutilizar a resposta errada,

03:03

o cache virou um bug.

03:04

E por isso entra o threshold. O que o threshold faz?

03:08

Ele é um limite mínimo para aceitar aquela similaridade.

03:12

Por exemplo, a aplicação pode dizer,

03:15

eu só vou considerar cache semântico se a

03:18

similaridade for maior ou igual a 0.9.

03:22

Esse número não é mágico, ele depende do domínio, do tipo da resposta,

03:27

do risco do fluxo e dos testes que você faz.

03:30

Em alguns cenários pode ser 0.85, ali, sei lá,

03:34

ele pode ser mais aceitável. Em outros,

03:36

você talvez só queira aceitar... 0.95 ou mais.

03:41

E em alguns casos, mesmo com similaridade alta,

03:45

você ainda prefere chamar IA de novo,

03:48

porque aquele tipo de decisão é sensível

03:50

demais para reaproveitar uma resposta anterior.

03:53

Então a lógica que a gente vai construir não é simplesmente encontrou algo parecido,

03:59

retorna o cache. A lógica correta é gerar o embedding da mensagem nova,

04:05

busca por candidatos parecidos, olha a pontuação, aplica o threshold,

04:10

valida se o contexto do cache ainda é compatível,

04:14

então só decide se pode reutilizar aquele cache.

04:20

Perceba como o embedding ajuda,

04:22

mas ele não substitui a arquitetura.

04:26

Ele melhora a capacidade da aplicação de encontrar coisas parecidas,

04:30

mas a decisão de reutilizar continua sendo da aplicação.

04:34

E é a aplicação que sabe... A versão do prompt, a versão das regras,

04:39

as capacidades do modelo e os riscos daquele fluxo. Então, para fechar essa parte,

04:44

distância e similaridade são formas de medir proximidade entre embeddings.

04:50

Threshold é o corte mínimo para decidir se essa proximidade é o suficiente.

04:55

E cache semântico é o uso disso para tentar evitar uma nova chamada de IA. Mas,

05:02

sem esquecer que parecido não significa igual. No próximo vídeo,

05:07

antes de entrar no PG Vector,

05:09

a gente vai separar bem cache semântico de reg,

05:13

porque os dois usam embeddings,

05:17

os dois podem usar busca vetorial,

05:20

mas a intenção arquitetural é bem diferente. Então, vamos nessa.

## Resumo IA

[RESUMO_IA]