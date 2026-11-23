Módulo: Arquitetura na Era da IA\
Aula: [Logs, tempos e resposta auditável](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18453)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, e agora a gente vem aqui e fala um pouco sobre observabilidade.

00:06

Mas o que eu estou querendo trazer aqui em

00:08

relação à observabilidade é em relação ao conceito. E o que isso significa?

00:13

Significa que eu quero mostrar para vocês que você precisa,

00:18

de uma forma ou de outra,

00:19

ter uma forma de conseguir entender como

00:22

cada etapa do seu pipeline está agindo.

00:26

Quanto tempo ela demora? Eventualmente, quanto ela custa?

00:29

Então, esses tipos de coisa ajudam demais,

00:33

inclusive, para você entender onde está o problema, onde estão os gargalos e etc.

00:37

Existem muitas ferramentas de mercado que podem te ajudar,

00:41

inclusive, com chamadas de modelo,

00:43

fazer essas integrações como um Langsmith da vida e etc.

00:47

Da forma como a gente está fazendo aqui, a gente está,

00:50

na realidade, pegando os dados que eu considero importantes,

00:53

específicos nesse pipeline de uma forma simples,

00:56

mas eu acho que você vai conseguir entender

00:59

bem a ideia, tá? Porque eu estou juntando dados da aplicação,

01:04

como tempo de resposta e etc,

01:06

mas ao mesmo tempo dados que a gente recebe via a chamada do modelo,

01:12

porque o Langchain ele traz também algumas informações quando a chamada é realizada,

01:18

quando o modelo é chamado.

01:19

Então eu consegui juntar aqui essas informações.

01:22

Então eu vou executar aqui para o nosso chat aqui.

01:26

E eu vou colocar uma pergunta assim, por exemplo, qual o preço do plano Pro?

01:35

E o que que acontece agora aqui? Você vai perceber o seguinte, tá?

01:41

Vamos voltar lá em cima porque ele tá em meio ao debug e vem coisa pra caramba, né? Então vamos lá.

01:46

Qual o preço do plano Pro? Se você olhar aqui, ó, eu tenho um JSON,

01:50

tá? E esse JSON aqui, ele vai ter um request ID. Primeira coisa, para observabilidade,

01:56

você tem que ter um ID daquela request para você conseguir recuperar depois.

02:00

Tem resposta? Sim. Precisa de clarificação? Não. Está usando o re-rank? Está. Retrieve counts.

02:07

O quanto que ele trouxe de documentos? Oito.

02:10

Quantos chunks foram selecionados? Quais foram os arquivos?

02:15

Quanto foram os tempos? Tipo, o query planning foi 121,2 segundos.

02:21

O retrieval demorou esse tempo.

02:23

O re-rank demorou esse tempo.

02:25

A geração da resposta em milissegundos, quanto que ele demorou aqui,

02:30

qual foi o modelo que foi utilizado, quanto que foi de input token,

02:34

quanto que veio de output token,

02:36

quanto que foi o total gasto de token aqui nessa resposta.

02:40

Com output token, input token,

02:42

e se eu tiver uma tabela de preços atualizada, eu consigo saber,

02:46

inclusive, estimar o custo que essa requisição e esse processo gastou ali no total.

02:52

Então, se você perceber aqui, eu tenho esse request ID,

02:57

que normalmente é o que acontece quando a gente tem

03:00

qualquer coisa em relação à parte de observabilidade. Então,

03:03

se eu olhar aqui, o debug do meu pipeline é request ID,

03:06

os tempos para fazer o planejamento,

03:09

para a gente fazer o retrieval, para pegar a informação no banco de dados,

03:12

para a gente fazer o re-rank, que é o cara que também demora,

03:15

Porque a gente chamou o banco de dados, o tempo de geração da resposta e o total.

03:21

Que a gente demorou para fazer tudo aqui, que é um tempo alto, 4 segundos. Então,

03:25

A gente tem que sempre trabalhar e entender onde está um grande gargalo,

03:29

Como que eu consigo melhorar,

03:30

Ajustar prompt e tudo mais. Então,

03:33

Isso aqui são coisas extremamente importantes que a gente precisa ter

03:37

Em qualquer tipo de aplicação que você vai trabalhar com a IA.

03:42

Independente se você vai usar uma plataforma...

03:44

De algum outro provedor ou coisa desse tipo,

03:46

Ou se você vai estar desenvolvendo o seu,

03:49

Tá? Hoje em dia,

03:51

Grandes ferramentas e plataformas de observabilidade ajudam muito

03:54

Com integrações em relação à IA.

03:56

Você pode trabalhar com OpenTelemetry, tem muita coisa interessante, tá?

04:00

Nosso ponto aqui não é a fundo em... observabilidade especificamente,

04:04

Mas é importante eu falar sobre observabilidade dentro desse

04:08

Pipeline para você entender que, como o pipeline tem etapas,

04:13

É importante você saber quanto tempo você gastou em cada etapa,

04:17

Quanto que você gastou em relação a tokens em tudo,

04:21

Aonde está o meu gargalo. Então, a gente fez de uma forma simples,

04:24

Mas pelo menos você consegue entender a ideia.

04:28

De como que tudo isso acaba funcionando. Então, isso aí ajuda bastante.

04:33

Eu também coloquei esse cara no servidor web para que a gente consiga trabalhar.

04:40

Então, você pode ver depois o JSON nele aqui.

04:42

Deixa eu ver se eu consigo subir esse cara aqui.

04:46

Cadê esse cara aqui?

04:49

Eu vou aqui no meu teste .http.

04:56

Nesse cara, e aqui provavelmente se eu chamar esse cara,

05:01

Fazer uma chamada HTTP do chat que tem um debug, debug igual a true,

05:07

Provavelmente eu vou ter uma resposta aqui mais completa em relação

05:12

A essa parte dos tracings aqui que a gente vai ter.

05:15

Aqui, tem resposta, precisa de clarificação,

05:18

O sources ele trouxe aqui para a gente, o debug, request ID.

05:22

O plano normalizado, os documentos, os termos exatos, precisa de clarificação,

05:27

Os filtros, o plano, os chunks recebidos,

05:30

Que ele trouxe ali no meio de toda essa história aqui para a gente,

05:34

Que é bastante chunk que ele recebeu,

05:36

Os chunks que foram selecionados e os tempos, que é para planejar,

05:41

O retrieval, o re-ranking,

05:43

A resposta de geração e o tempo que ele demorou com tudo.

05:46

Qual o modelo, input tokens,

05:48

Output tokens e total de tokens que a gente acabou utilizando. Então,

05:52

Aqui a gente tem uma informação bem completa que

05:55

A gente consegue debugar e coisas desse tipo.

05:58

Então, é importante que você consiga se ligar disso.

06:02

Por exemplo, se você vê quanto tempo eu demorei,

06:06

Eu demorei, sei lá, quase 5 segundos para resolver esse problema.

06:09

Se eu chegar agora aqui e pegar,

06:12

Deixa eu ver se eu tenho uma opção onde eu estou com o re-ranking.

06:16

Sem re-ranking, aqui use re-ranking, false aqui pra mim.

06:21

E eu vou ver se eu consigo aqui colocar

06:23

Debug true, deixa eu dar um send request, ó.

06:30

A primeira demorou cinco e poucos segundos, olha quanto que demorou a segunda, dois

06:35

Ou seja, caiu quase pela metade. Por quê?

06:38

Porque eu pulei a etapa do re-ranking, por exemplo. Então,

06:41

Olha só como que a gente já começa a ver gargalos

06:44

Dentro da nossa aplicação e como que a gente pode

06:47

Começar a trazer esses tipos de coisa no dia a dia

06:51

Para a gente conseguir tomar o melhor tipo de decisão.

06:53

Eu não estou aqui para falar em ferramentas,

06:55

A gente está aqui para falar de arquitetura. Então, nesse ponto,

06:58

Eu quero que você entenda o nível de importância que você tem que dar.

07:03

Na hora que você vai criar qualquer tipo de aplicação.

07:06

Observabilidade, em forma geral, já é algo muito discutido e maduro nos momentos,

07:11

Nos pontos em relação à arquitetura.

07:13

O que entra agora aqui em relação à IA normalmente é, em relação à observabilidade,

07:18

Quais são etapas que eu preciso realmente observar.

07:22

E quando a gente está falando em tokens, etc.,

07:24

Os modelos, os frameworks,

07:26

Eles já trazem os tokens e essas informações ali para você.

07:30

E você pode também ter integrações com plataformas

07:33

Externas para trazer essas outras informações.

07:37

Então, era essa que a ideia que eu queria trazer para vocês,

07:40

Pelo menos mostrar e comentar em relação a essa parte de observabilidade,

07:44

Porque muda muito a forma de como que você vai conseguir

07:48

Depurar e entender os grandes gargalos dentro da sua aplicação. É isso aí.

## Resumo IA

[RESUMO_IA]