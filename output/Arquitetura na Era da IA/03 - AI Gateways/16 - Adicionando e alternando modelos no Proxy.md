Módulo: Arquitetura na Era da IA\
Aula: [Adicionando e alternando modelos no Proxy](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18327)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, no vídeo anterior, a gente viu ali na prática nós chamando,

00:06

a gente estava chamando o nosso

00:08

proxy usando a nossa aplicação main.py,

00:13

onde o nosso proxy, a gente tem um modelo cadastrado chamado,

00:17

como é o nome do nosso model?

00:21

Developer Assistant, por padrão.

00:24

Então, o que isso significa? Que quando a gente chama a nossa aplicação,

00:28

minha aplicação não sabe... qual modelo que o Developer Assistant utiliza,

00:32

ou seja, a minha aplicação trata o Developer Assistant como um modelo,

00:35

mas eu sei que na configuração do meu proxy,

00:38

o Developer Assistant, o que acontece? Esse cara,

00:43

ele já é um cara que está sendo mascarado pelo nosso proxy,

00:48

que está utilizando o GPT ali por trás, tá? Então,

00:52

a nossa mudança agora aqui que eu acabei de fazer, na realidade, é o seguinte.

00:58

Aqui no meu config.yaml, o que eu fiz? Eu adicionei um novo modelo,

01:03

tá? Ou seja, mas ao invés de utilizar o meu Developer Assistant,

01:09

eu criei um outro cara chamado Architecture Advisor e ao

01:12

invés de utilizar o GPT 4.1 mini,

01:15

eu estou utilizando o CloudSonic 4.6 e ambos têm a API key,

01:20

tá? Só para você saber, tá?

01:22

Aqui no meu .env, eu criei mais uma variável de ambiente.

01:26

onde eu tenho a Anthropic API Key.

01:29

Eu não sei se eu restartei o meu proxy, tá?

01:33

Deixa eu dar um docker compose, docker compose,

01:39

deixa eu dar um docker compose down, vai, só para garantir,

01:44

e eu dar um docker compose up -d.

01:46

Poderia dar um restart, mas vamos aguardar esse cara subir um pouquinho.

01:51

Então, o que acontece agora, tá? Quando eu rodei isso, o meu proxy carregou,

01:57

E agora ele está iniciando e ele vai reconhecer esse meu Architecture Advisor.

02:03

Então, primeira coisa, se eu rodar o meu Python main.py,

02:06

o que vai acontecer é, não vai mudar nenhum comportamento,

02:10

porque ele vai estar chamando aquele modelo inicial,

02:14

que é o que a gente chamou no vídeo anterior, que é o Developer Assistant.

02:18

Mas agora, o que acontece?

02:21

Se eu chegar e mudar o meu model,

02:26

Então eu posso,

02:27

eu acho que se eu chegar aqui dessa forma e colocar model igual a Architecture

02:36

Advisor e

02:39

chamar o Python main.py, vamos ver o que vai rolar.

02:49

Vamos ver se ele mudou. Ele está com o Developer Assistant.

02:52

Deixa eu ver. Deixa eu só mudar aqui, vai.

02:55

Por que

02:59

ele não chamou o meu Architecture Advisor?

03:00

Alguma besteira minha na hora de passar essa variável de ambiente aqui. Espera aí.

03:05

Eu vou pegar meu ArchitectureAdvisor, deixa eu colocar ele aqui como ModelName,

03:09

eu não sei porque que ele não... Ah, já sei. Aqui no meu .env,

03:14

eu posso colocar aqui no final das contas quem que é o meu...

03:19

a minha variável padrão de modelo,

03:23

na realidade. Deixa eu só pegar aqui no meu main.py,

03:27

eu tenho uma variável chamada Model, tá?

03:33

E nessa minha variável model, eu posso colocar aqui no meu ponto env.

03:39

Em vez de colocar esse cara, eu vou colocar o meu

03:43

Developer Assistant. E eu já entendi o porquê que ele não está colocando,

03:48

porque ele está usando como AI model.

03:50

Basicamente é por conta disso. Por isso que não funcionou.

03:53

Eu vou colocar aqui de qualquer forma. Mas...

03:58

Cadê o nosso camarada?

04:04

Como que era o nome dele?

04:09

Cadê? Nossa, aqui. Pronto. Architecture Advisor. Então,

04:14

eu posso colocar aqui Architecture Advisor ou eu poderia colocar aqui AI Model,

04:19

AI Gateway Model. Então, por isso que essa minha variável não funcionou.

04:23

Ela não funcionou porque eu coloquei a variável errada.

04:26

Não era Model, era AI Gateway Model.

04:28

Mas aqui eu já passei. Então, vamos ver o que vai rolar agora. Vamos lá.

04:43

Aguardando uns segundinhos, pelo jeito o Cloud Sonnet está demorando mais.

04:47

Mas, olha só.

04:51

Modelo, Architecture, Advisor. A pergunta e a resposta que a gente teve.

04:56

Então, nesse momento, o que aconteceu?

04:59

A minha aplicação está chamando esse módulo,

05:01

mas eu sei que por trás dos panos, ela está utilizando o quem?

05:06

O meu Cloud Sonnet, aqui nesse caso. Então, está aqui na minha módulo list.

05:11

E eu não estou utilizando agora o Developer Assistant. Então,

05:15

isso é uma forma de a gente ver que,

05:16

uma vez que você está desenvolvendo uma aplicação na sua empresa,

05:20

e você tiver uma AI Gateway, os seus desenvolvedores, você e etc.,

05:25

não precisam ficar grudados ou tentando ter

05:29

detalhes ali de qual modelo você vai utilizar.

05:33

E daí a gente vai entrando naquele aspecto que eu falei.

05:36

Você não começa a chamar modelos tipo GPT,

05:40

não sei o que, Cloud, não sei o que,

05:43

Gemini, não sei o que, baseado no modelo, mas sim pela intenção de uso.

05:49

Entendeu? E pela intenção é muito melhor,

05:51

porque eu não fico mais preocupado com parâmetro,

05:53

com nada. Eu sei que eu preciso de um assistente desenvolvedor.

05:56

Eu sei que eu preciso de um arquiteto.

05:57

Eu sei que eu preciso de um cara do financeiro.

05:59

E aí as coisas vão ficando mais fáceis. Próximo vídeo,

06:02

a gente vai dar mais um passo aqui de mudança pra ficar mais claro pra vocês

06:07

outros aspectos que agora a gente vai começar a trazer aqui com o Lite LLM Proxy.

## Resumo IA

[RESUMO_IA]