Módulo: Arquitetura na Era da IA\
Aula: [Fallback com modelo fraco](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18329)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, agora a gente vai para esse último caso que eu estava querendo dizer para vocês.

00:05

O lance é o seguinte, não adianta eu ter um modelo de fallback,

00:10

sendo que esse modelo de fallback não é adequado

00:13

para que ele resolva o problema que eu estou querendo.

00:18

Então, aqui eu criei um exemplo que é o seguinte.

00:21

No meu arquivo principal eu tenho algumas categorias. de produtos,

00:26

de um agente de suporte, de ticket, ou seja, cai tickets,

00:30

ele analisa os tickets, né? E aqui tem uma mensagem padrão,

00:33

que ele foi cobrado duas vezes na minha assinatura e quer resolver isso.

00:37

E aqui tem um prompt falando, ó,

00:38

você é um classificador, responde estritamente em JSON válido,

00:42

sem texto fora do JSON, sem blocos de código Markdown,

00:46

sem crases, responde apenas com o objetivo com JSON puro,

00:49

exatamente nesse formato. E eu trouxe o formato aqui do JSON.

00:53

E aqui eu tenho uma função que eu verifico o resultado que veio para saber,

00:59

inclusive, se aquele JSON é válido ou não.

01:03

E a grande questão é que a gente vai tentar

01:06

testar com um modelo e depois a gente vai

01:09

deixar esse modelo com problema para que o fallback

01:12

seja ativado e a gente vai verificar se o fallback,

01:17

apesar de ter funcionado, se ele teve a mesma... Então,

01:22

essa aqui é a ideia principal. Então, só para você saber,

01:25

no meu .env aqui,

01:27

eu coloquei o meu modelo primário GPT 4

01:31

.1 Mini e o backup do Raico 4 .5.

01:35

E para você olhar a configuração, basicamente é o nome do modelo,

01:39

Ticket Classifier Backup, que está chamando o Raico,

01:43

e o outro modelo que está chamando o da OpenAI,

01:47

que é o principal. Então, a gente tem o modelo de backup,

01:51

que vai ser o nosso fallback aqui para a gente. Então,

01:54

o que eu vou fazer? Eu vou botar esse cara aqui para rodar.

01:56

Então, eu vou colocar Python main .py. E aqui,

01:59

a gente está rodando com o GPT 4 .1 mini.

02:02

E aqui, o modelo retornou isso aqui para a gente,

02:06

a resposta crua. Billing, Reason, cobrança duplicada da assinatura. Então,

02:10

aqui eu tive uma resposta válida para o fluxo, categoria e o motivo,

02:14

que é a cobrança duplicada. Beleza? Agora, o que eu vou fazer?

02:18

Eu vou no meu .env aqui e vou colocar um modelo

02:22

inexistente para garantir que o primary model dê problema na realidade.

02:26

Eu não vou nem mexer com .env ou qualquer coisa desse tipo.

02:29

Vou dar um down aqui no meu container.

02:33

Vou dar um up novamente no meu container para ele pegar as variáveis de ambiente.

02:37

Eu acho que só dando um restart ele não atualiza as variáveis de ambiente, se eu não me engano.

02:43

E agora, vamos esperar só um pouquinho.

02:46

e eu vou rodar o mesmo cara, o PythonMan .py,

02:50

e agora ele vai ter que chamar o fallback,

02:52

porque o modelo principal deu problema. E olha só a diferença.

02:56

Foi cobrado exatamente como resolver isso, resposta crua do modelo.

03:00

Nesse caso, olha só o que ele trouxe.

03:02

Ele trouxe as três tracinhos de aspas aqui, JSON, né? E etc. Então,

03:08

Ele quebrou porque não é o Jason Puro como eu pedi. Ou seja,

03:11

veio embrulhado no Markdown com o Krazy da forma como eu queria.

03:15

Então, o fallback respondeu 200, mas o modelo de backup é fraco.

03:20

Então, ele teve um fallback,

03:22

mas não adianta se a resposta não serve para esse fluxo.

03:25

Então, essa que era a ideia que eu queria trazer.

03:28

Hoje em dia, a gente pode ter redundância,

03:30

mas essa redundância de modelos tem que ser equivalente.

03:34

E aí, quando eu falo equivalente,

03:36

não é só equivalente ao quanto ela responde bem,

03:39

mas equivalente em relação à quantidade de custo que

03:43

ela vai trazer e em relação à latência. Com certeza,

03:47

se eu colocar um modelo mais inteligente por trás com uma latência maior,

03:50

ele vai resolver esse problema.

03:53

O ponto aí é que eu vou gastar mais, vai demorar mais e etc.

03:56

Então, é esse trade-off que a gente tem que trabalhar,

03:59

e na hora que a gente desenvolve as aplicações,

04:02

e arquitetar as aplicações, na hora de configurar um gateway ou qualquer coisa,

04:06

a gente tem que ter isso em mente.

04:08

Mas, novamente, aqui era só uma demonstração,

04:11

e trazendo aqui para vocês, de uma forma simples,

04:14

inclusive para alinhar a expectativa, que nós temos proxies.

04:18

E esses proxies funcionam como um AI Gateway,

04:21

mas ao mesmo tempo nós temos aí AI Gateways de mercado com diversos recursos.

04:25

O Light LLM,

04:27

por padrão, ele tem um monte de outros recursos, muito além do que fazer fallback,

04:31

ele tem um monte de recursos, você consegue agrupar,

04:34

você consegue criar categorias de usuários,

04:36

dar permissões diferentes para grupos de usuários e coisas desse tipo,

04:40

né? Usuários podem ter keys diferentes e tudo mais.

04:43

Mas o nosso objetivo aqui não é um curso de Light LLM,

04:46

é você entender arquiteturalmente falando que agora a gente tem um componente no

04:51

meio que normalmente quando a gente falava em arquitetura de software de solução,

04:55

antigamente a gente não tinha.

04:57

E aí está mais alguma coisa que a gente tem

05:00

que aprender e aí vai depender de qual provider,

05:03

qual solução você vai escolher ou a sua empresa vai escolher,

05:08

dependendo do tipo de empresa que você vai trabalhar, porque às vezes o provider...

05:13

vai depender do contrato que a sua empresa tem. Então,

05:16

hoje em dia tem empresas que trabalham com AWS,

05:19

com Azure, com GCP, e da mesma forma que todas as empresas têm um API Gateway,

05:25

e que normalmente é utilizado nos serviços, essas empresas,

05:29

de forma geral, agora a gente tem AI Gateways.

05:32

E é importante você entender que esse componente agora existe.

05:35

Beleza? Então é isso aí.

## Resumo IA

[RESUMO_IA]