Módulo: Arquitetura na Era da IA\
Aula: [O que é um modelo de embedding](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18345)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente evoluiu o cache para usar fingerprint, ou seja,

00:06

a chave deixou de depender só da mensagem do usuário

00:09

e passou a considerar também a versão do prompt,

00:12

versão das regras e da capacidade do modelo.

00:14

Agora a gente vai começar uma nova parte do nosso capítulo,

00:18

porque até aqui o nosso cache ainda depende de uma ideia simples.

00:21

Mensagem precisa ser igual depois de normalizada para

00:25

a gente reutilizar a nossa resposta.

00:28

Só que em aplicações com IA,

00:30

muitas vezes o texto muda, mas a intenção é praticamente a mesma.

00:34

Por exemplo, uma pessoa pode escrever,

00:36

como eu cancelo minha assinatura? A outra pode escrever, quero cancelar meu plano.

00:42

Outra pode mandar, onde eu paro a minha cobrança?

00:46

Os textos são diferentes. Se eu fizer um cache exato,

00:50

olhando só para o texto normalizado,

00:52

cada uma dessas mensagens vai gerar uma chave diferente.

00:55

Então a aplicação vai chamar a IA. De novo,

00:58

em todos os casos. Só que, semanticamente,

01:01

talvez todas estejam falando de uma única intenção ou uma intenção parecida.

01:08

E é aqui que começa a entrar o conceito de embedding.

01:12

Um modelo de embedding não é um modelo de chat.

01:16

Essa é a primeira coisa que precisa ficar clara. Ele foi feito para conversar,

01:22

responder perguntas, gerar textos ou explicar alguma coisa para o usuário.

01:27

Ele recebe um texto e devolve uma representação numérica desse texto.

01:33

Ou seja, na prática, ele transforma uma frase em um vetor,

01:37

um array de números gigante.

01:40

Esse vetor não é algo que a gente olha e interpreta manualmente.

01:45

Não faz sentido olhar para o número a número

01:48

e tentar descobrir o que cada posição significa.

01:51

O valor dele está no fato de que textos

01:55

com sentidos próximos tendem a gerar vetores mais próximos.

02:00

Textos com sentidos mais distantes tendem a gerar vetores mais distantes.

02:07

Então, em vez de eu comparar duas strings,

02:10

a gente começa a comparar duas representações semânticas.

02:14

Essa é uma mudança muito importante.

02:17

Quando eu comparo texto puro, a pergunta é,

02:20

essas duas frases são iguais? Quando eu comparo embeddings,

02:24

a pergunta muda para...

02:26

Essas duas frases estão próximas em significado e isso

02:30

abre um espaço para o cache semântico.

02:32

No cache exato, eu só consigo reaproveitar uma resposta quando a entrada é igual.

02:38

No cache semântico,

02:39

eu tento descobrir se já existe uma resposta

02:42

anterior para algo parecido o suficiente.

02:45

Se existir,

02:47

talvez eu consiga reutilizar aquela resposta sem chamar a IA de novo.

02:52

Mas aqui tem um cuidado grande.

02:54

Parecido. não quer dizer igual.

02:57

Similaridade não quer dizer equivalência.

03:01

Duas mensagens podem ser próximas no embedding e

03:04

mesmo assim não deveriam reaproveitar a mesma resposta.

03:08

Por exemplo, quero cancelar a minha assinatura e quero cancelar uma reunião.

03:14

Elas podem ter palavras parecidas,

03:17

mas são problemas completamente diferentes. Ou então,

03:21

uma mensagem pode parecer parecida com a outra, mas...

03:25

Tem um detalhe que muda ali a decisão.

03:27

Por isso o embedding não decide sozinho. Ele ajuda a encontrar candidatos.

03:34

A aplicação ainda precisa ter política.

03:37

Ela precisa ter um threshold. Ela precisa validar a versão do prompt,

03:40

a versão da regra, da capacidade no modelo. E dependendo do sistema,

03:45

outros contextos também. O embedding ajuda a dizer, olha, isso aqui parece próximo.

03:51

Mas a aplicação ainda precisa decidir se é seguro reutilizar. No capítulo,

03:57

nesse nosso capítulo, a gente vai utilizar embeddings de uma forma bem específica.

04:02

A gente não está nem entrando em regex ainda.

04:05

Essa distinção, inclusive, é bem importante.

04:08

No regex, a gente vai falar sobre isso.

04:10

Eu uso embeddings para buscar trechos de documentos.

04:13

ou conhecimento externo para montar um contexto e

04:16

chamar IA para gerar uma nova resposta.

04:19

Aqui no cache semântico, a pergunta é outra.

04:22

Eu quero saber se eu já respondi algo parecido

04:25

antes e se eu posso reaproveitar aquela resposta.

04:29

Então, a tecnologia começa a ser parecida,

04:33

mas a intenção arquitetural é completamente diferente. Nesse momento, guarda isso.

04:39

O modelo de embedding transforma texto em

04:41

vetor para permitir comparação por proximidade de significado.

04:46

Ele não gera a resposta final.

04:48

Ele cria uma representação que a aplicação pode usar para buscar,

04:54

para comparar, para gerar decisão em todos esses aspectos.

04:59

Então, na próxima aula,

05:00

a gente vai gerar embeddings de algumas mensagens

05:02

para ver isso acontecendo no código.

05:04

Ainda não vamos integrar tudo isso com um cache semântico. Primeiro,

05:08

a gente vai entender a chamada de modelo de embedding, ver o retorno,

05:12

ver a dimensão do vetor e separar bem isso de modelos

05:17

ali que a gente está acostumado a trabalhar em modelos de chat,

05:20

por exemplo. Ok? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]