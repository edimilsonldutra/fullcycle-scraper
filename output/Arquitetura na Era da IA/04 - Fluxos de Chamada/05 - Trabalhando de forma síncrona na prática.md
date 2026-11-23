Módulo: Arquitetura na Era da IA\
Aula: [Trabalhando de forma síncrona na prática](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18315)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, já que a gente falou dessas três categorizações no formato de a gente trabalhar,

00:07

vou trazer um pouquinho aqui de código apenas para que

00:10

você dê uma olhada nesses três aspectos que eu coloquei.

00:15

Lembrando que eu usei aqui como Python,

00:17

mas isso poderia ser utilizado com qualquer linguagem de programação.

00:21

Então é o seguinte, esse primeiro exemplo, basicamente, o que eu tenho,

00:25

só para você entender? Eu tenho como esquemas,

00:28

ou seja, um model básico, que é o request que eu vou receber no endpoint HTTP,

00:35

que vai ser a mensagem do cliente, e aqui eu vou ter o base model.

00:42

Ali que vai trabalhar no final das contas com análise,

00:44

ou seja, o response que vai trabalhar.

00:46

Então, eu vou ter um endpoint onde eu faço um request

00:49

e recebo um response no meio de toda essa história.

00:53

Então, se você olhar o meu main aqui, basicamente é isso que você vai ver.

00:58

Então, independente de linguagem de programação que você utiliza,

01:01

dá para perceber que eu tenho aqui um POST mandando para /barra tickets,

01:06

/barra analyze, onde eu passo o...

01:11

aquele request, quer dizer, eu passo esse request e recebo o response aqui para mim.

01:16

E aqui, lembrando que eu vou fazer a chamada para IA, ou seja,

01:20

esse analyze ticket, no final das contas, é uma chamada que eu vou fazer para IA.

01:25

Então, se você olhar aqui, eu tenho o meu AI client.

01:28

O AI Client vai trabalhar aqui com o modelo padrão do GPT-4.1 Mini,

01:34

poderia ser qualquer outro modelo, e tem a chave no arquivo .env aqui também.

01:39

E aqui eu tenho um System Prompt muito parecido nos outros exemplos.

01:42

Você é um assistente que analisa tickets de suporte,

01:46

sempre retorna um JSON válido, e trouxe aqui as chaves,

01:50

categoria, prioridade e resumo.

01:52

E aqui eu tenho basicamente a função que vai fazer isso.

01:57

Ou seja, eu estou fazendo a chamada para a API da OpenAI,

02:01

passando o prompt e a mensagem do usuário que eu recebi aqui.

02:06

E aí, no final das contas,

02:08

eu tenho o resultado e se tiver algum problema, é tratado esse erro. Caso contrário,

02:15

no final das contas, eu vou retornar isso no formato...

02:18

do ticket analysis, né? Que, no final das contas,

02:22

vai ser retornado um JSON, né? E lembrando que isso aqui é só um PyDent,

02:26

que é um modelo pra gente trabalhar,

02:29

pra ele formatar e deixar os dados dentro do formato que eu queria.

02:32

Beleza? Então, basicamente, é isso.

02:35

E quando eu vou rodar, somente pra que você saiba, né?

02:40

Quando eu fizer a execução desse cara, eu tenho um main aqui fora, tá?

02:45

Ou seja, eu tenho dentro da pasta app um main.

02:47

Mas eu tenho um main.py aqui que vai executar o servidor web,

02:52

que eu preciso agora de um servidor. Então, basicamente,

02:55

esse main simplesmente vai rodar o meu servidor. Então, o que eu vou fazer agora?

03:00

Eu vou rodar aqui um Python main.py

03:04

e agora aqui ele está chamando o servidor.

03:07

Para facilitar a nossa vida,

03:09

o que eu fiz? Eu criei um requests.http.

03:14

E se você tem esses plugins, que por exemplo, REST, HTTP Client,

03:19

no seu próprio VS Code ou coisas desse tipo,

03:22

Esse plugin fica mais fácil para a gente ver os resultados.

03:26

Então, eu criei um exemplo de cada.

03:29

Então, se eu clicar aqui, Send Request, ele vai mandar Analyze,

03:32

e aqui tem a mensagem que vai entrar,

03:35

que é Fui cobrado duas vezes. Então, deixa eu dar um System Request aqui,

03:38

ele vai abrir aqui para mim uma janelinha do lado.

03:41

Vamos lá, deixa eu...

03:44

Ver, ele tem que abrir a janelinha. Será que foi?

03:51

Foi, mas ele não abriu a minha janela do lado aqui. Pera aí.

03:55

Bom, pessoal, depois eu ter apanhado um pouquinho aqui com VS Code e Cursor e etc. Era uma bobeira.

04:01

Basicamente, quando eu dei um Send Request, aqui ele trouxe Billing High e etc.

04:07

Se eu tenho um outro exemplo aqui, quando eu clico aqui, o

04:11

tipo era Technical High e a app trava ou abriu o relatório. Se você olhar...

04:17

Olha como é que aparece aqui a mensagem.

04:19

Ou seja, ele está fazendo uma classificação normal,

04:22

né? E aqui, quando eu não passo nada,

04:24

ele tem o erro de validação normal do JSON que está sendo feito ali pelo Pydantic, tá? Basicamente,

04:29

é isso que acontece. Então, isso aqui é uma chamada síncrona normal,

04:33

que acontece rápido porque eu recebi uma mensagem e eu consigo categorizar.

04:38

Então, parte síncrona,

04:40

eu acho que é aqui, chover no molhado,

04:42

então o próximo passo pra gente vai ser a parte

04:45

de streaming que muda um pouquinho o comportamento,

04:49

então vamos nessa

## Resumo IA

[RESUMO_IA]