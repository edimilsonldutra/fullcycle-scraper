Módulo: Arquitetura na Era da IA\
Aula: [Analisador sem cache](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18339)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, vamos começar a colocar essas coisas aqui na prática, tá?

00:04

E para não ficar muito complexo tudo que a gente vai desenvolver aqui,

00:08

eu vou fazer da forma mais simples possível e eu

00:12

vou utilizar aqui o Langchain para fazer isso,

00:15

para facilitar a nossa vida,

00:16

para fazer chamadas de modelo de IA e coisas desse tipo, tá?

00:20

Então, somente para a gente entender o nosso problema central,

00:24

vamos dizer, né? Nós temos o seguinte,

00:27

a gente quer fazer análise de ticket de suporte.

00:30

Ou seja, quando cai um novo ticket,

00:32

a gente tem que, por exemplo, categorizar esse ticket,

00:36

a gente tem que colocar o nível de confiança,

00:39

o nível de confiança que a gente tem que aquela categoria é

00:42

a correta e também o motivo pelo qual a gente acha isso. Então,

00:48

somente para você entender aqui nesse caso, o que eu tenho aqui? Eu tenho...

00:53

uma análise de ticket, que é um modelo base aqui do Pai Dente,

00:57

que isso aqui é detalhe, mas basicamente eu tenho as minhas categorias,

01:01

o meu nível de confiança e a minha razão.

01:04

Aqui eu tenho o request, ou seja, a gente tem uma API, ou seja,

01:08

eu tenho o request onde eu recebo uma mensagem e eu tenho o response,

01:11

que eu vou retornar o quê? O source, ou seja, de onde que veio essa resposta,

01:16

a quantidade de chamadas para IA que foram feitas, o tempo que demorou e...

01:22

o resultado da análise, né?

01:24

Que é essa nossa análise de ticket que vai trazer a categoria,

01:27

a confiança, a confiança e a razão aqui pra gente,

01:31

tá? Aqui também nós temos o nosso prompt, tá? Ou seja...

01:35

o nosso prompt principal que vai ser colocado para que essa categorização aconteça. Então,

01:41

aqui eu tenho um system prompt que fala, você é um classificador de tickets de suporte,

01:44

classifique a mensagem em uma das categorias: Billing,

01:48

Technical Support, Account Cancellation e Other.

01:51

Retorne uma confiança entre 0 e 1 e um motivo curto.

01:54

Não invente categorias fora da lista.

01:56

E aqui eu tenho a mensagem que estou passando pela minha request.

02:02

E agora... Aqui, trabalhando com o Langchain, as coisas ficam bem simples.

02:06

Eu estou inicializando aqui um chat com um modelo,

02:10

então eu estou passando o nome do modelo,

02:12

que nesse caso está o GPT-4.1, poderia ser o GPT-5.4, etc.

02:17

Não interessa, eu coloquei um que é bem rápido aqui.

02:20

O provedor eu falo que é o OpenAI,

02:22

a temperatura zero para ele ser realmente bem exato.

02:24

Lembrando, se eu estou usando o Langchain aqui,

02:26

eu poderia mudar o provedor que eu quisesse e

02:28

colocar a chave daquele provedor que iria funcionar. E agora,

02:32

aqui eu tenho o meu chain, ou seja, o meu encadeamento de chamadas.

02:37

Então, eu tenho o chain, que é o meu prompt que vai entrar,

02:40

o meu prompt vai jogar como input a chamada para esse LLM,

02:45

que vai trazer para a gente como output o resultado.

02:52

Preenchendo essa análise de ticket, ou seja,

02:55

preenchendo o resultado dessa nossa classe,

02:59

ou seja, esse modelo vai ser preenchido. Então, eu pego o meu prompt,

03:03

Injeto o meu prompt na chamada do LLM e

03:05

Falo para o meu LLM fazer essa saída estruturada aqui.

03:12

Aqui eu tenho uma variável global que é AI count,

03:16

que vai mostrar para mim quantas chamadas eu fiz para a IA.

03:21

E aqui eu estou chamando o FastAPI,

03:23

que é para a gente poder trabalhar com o servidor web aqui no Python.

03:28

Então, eu tenho aqui no final das contas um endpoint que é /tickets /analyze,

03:34

onde no final das contas o response dele vai

03:39

ser o nosso ticket response que nós já temos aqui,

03:42

que é o source, AI call number, o tempo e etc.

03:46

Então, o que acontece? Ele recebe uma request.

03:49

E vai retornar a response. Então ele vai ter aqui a nossa contagem global.

03:53

Da nossa quantidade de chamadas para a IA.

03:55

E aqui tudo que eu estou fazendo. Eu estou colocando bastante log.

03:58

Então, às vezes a gente vai ver mais log do que código.

04:00

Aqui de forma geral. Então aqui eu inicio a contagem de tempo.

04:04

E aqui eu faço o invoke. Toda vez que você vê o invoke aqui em relação ao LangChain.

04:10

Significa que aqui eu estou fazendo uma chamada para o modelo.

04:13

E ele vai fazer o invoke no que?

04:16

Nessa mensagem. A mensagem que ele recebeu, que é no meu request. Então,

04:21

esse message aqui é o message que está substituindo aqui o prompt. Então,

04:26

é esse prompt que vai ser a chamada aqui para o nosso modelo.

04:30

Feita essa chamada, ele vê quanto tempo ele demorou.

04:34

A gente soma que houve uma chamada para a IA e a gente coloca aqui no log.

04:40

IA, o call number,

04:41

o tempo que demorou e a categoria que ele conseguiu categorizar.

04:46

E retorna para a gente, então, a nossa response com AI model,

04:50

falando que a gente chamou o modelo de A, AI call count,

04:54

o tempo e o resultado que a gente queria. Embaixo aqui,

04:57

como é um arquivo main.py,

04:58

eu estou simplesmente subindo o servidor web na porta

05:02

8000 e com hot reload aqui nesse caso. Então,

05:06

vamos botar esse cara aqui para rodar somente para a gente ter uma ideia,

05:09

porque tudo vai variar agora a partir desse programa. Então, eu vou dar um.

05:15

um python main.py, então aqui o servidor web subiu,

05:19

para evitar eu ficar dando um curl, trabalhando com código manual de forma geral,

05:26

eu tenho aqui o meu client.http com uma extensão,

05:30

então aqui eu já tenho os meus posts prontos, então o primeiro aqui,

05:34

ele vai aparecer com a mensagem, tenho dúvida sobre cobrança,

05:37

pode me ajudar? Então, eu vou dar um send request, pum.

05:42

E agora ele está chamando a IA aqui para mim. Então, teve AI model,

05:46

uma chamada, o tempo que ele demorou. O resultado é billing,

05:49

o número de confiança 0.95.

05:52

E a mensagem menciona dúvidas sobre cobrança que se enquadram na categoria billing.

05:57

E aqui aparecem os logs que a gente acabou colocando aqui.

06:02

Beleza? Então, esse vídeo eu só queria mostrar de forma geral.

06:06

O setup básico para a gente fazer uma chamada para uma IA

06:10

e perceba que aqui a gente não fez nada de cache.

06:12

Chamadas totalmente normais.

06:14

Tanto que se eu rodar de novo a minha segunda chamada exatamente igual,

06:18

O que vai acontecer?

06:21

A gente vai, de forma geral, ter uma nova chamada,

06:25

vai ser exatamente a mesma coisa. Ou seja,

06:28

não tem nada de cache, nada que vai nos ajudar aqui para a gente.

06:33

Se eu colocar outra pergunta também...

06:36

ele vai também processar sem nenhum problema,

06:39

mas ele muda a categoria agora aqui para cancellation,

06:42

por exemplo. Então, tem mensagem para o suporte técnico.

06:46

A gente vai pegar aqui, technical support,

06:48

então consigo mostrar que ele está conseguindo realmente fazer a categorização. Mensagem de conta,

06:54

não consigo acessar a minha conta. Então,

06:56

aqui ele está trazendo que a categoria é account,

06:58

usuário relata problema para acessar a conta relacionada.

07:02

Beleza? Então,

07:03

aqui começa a nossa história para a gente começar a

07:07

navegar nesse mundo do cache com o IA. Vamos nessa.

## Resumo IA

[RESUMO_IA]