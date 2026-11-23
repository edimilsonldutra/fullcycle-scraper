Módulo: Desenvolvimento de Agentes com IA\
Aula: [O Que É Uma Tool](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18098)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre as tools,

00:03

que é um conceito muito comum nesse advento da IA.

00:06

Eu imagino até que você já tenha ouvido falar, e não somente pouco,

00:10

mas muitas vezes essa palavra tool. Nós vamos aprender o que é essa tool nesta aula.

00:16

Eu tenho um novo agente, que é um operador de conta.

00:20

Estou passando o modelo Flashlight, mas uma versão mais atualizada do Gemini,

00:25

que é o 3.1, que também tem...

00:28

o uso gratuito, e no System Prompt,

00:32

dizendo que ele é um atendente de conta interativo de uma Acme,

00:36

que é uma empresa fictícia.

00:37

Você é responsável por informar ao cliente sobre a assinatura dele,

00:41

tirar dúvidas sobre as faturas, cancelar a assinatura do cliente se solicitado,

00:47

e o usuário precisa fornecer as informações corretas,

00:52

no caso que é o ID do cliente, para que...

00:55

o agente possa fazer as operações. Então,

00:57

seja direto e objetivo, um system prompt básico.

01:03

Obviamente, se nós rodarmos esse agente, dizendo assim, list as faturas, ele

01:12

vai pedir que eu informe o ID do cliente. Ele está falando justamente isso.

01:17

Então, se eu informar qualquer coisa, ele não tem acesso a dados.

01:20

Veja que ele até inventou.

01:24

Eu posso até pedir para ele assim, você

01:28

inventou? Os dados.

01:32

Agora está falando que, como não tem acesso ao banco de dados real,

01:36

então os dados são fictícios, né? Enfim,

01:38

nós poderíamos até melhorar aquelas instruções aqui,

01:41

mas isso aqui foi apenas um laboratório. Antes de entender as tools,

01:45

nós precisamos entender que a LLM sozinha é um cérebro inútil.

01:55

Por quê? Se eu preciso acessar banco de dados, fazer chamadas HTTP,

02:04

ler arquivos, ela não consegue fazer isso e nem vai conseguir em nenhum momento.

02:12

Se eu preciso realizar essas tarefas e mais outras,

02:17

isso vai ser feito através das tools. E, obviamente,

02:22

quem dá o comando de quais tools

02:25

vão ser executadas vai ser a própria LLM.

02:29

Então, por isso que o agente é importante, porque...

02:34

Ele que vai obedecer aos comandos da LLM. Então,

02:41

uma tool é essa extensibilidade da LLM,

02:47

permitindo que ela consiga,

02:50

de forma indireta, ter acesso aos dados, fazer chamadas HTTP. A gente vai entender isso agora.

02:56

Então, se eu quero trabalhar com faturas, vou criar uma tool que,

03:01

no final das contas, é apenas uma função.

03:04

Eu quero listar faturas como?

03:07

Todas ou por cliente?

03:09

Quero por cliente. Vamos colocar cliente ID, que

03:14

vai ser uma string, e aí nós vamos fazer uma

03:20

busca. Por enquanto, vamos fazer apenas com uma lista do Python.

03:25

Então, aqui eu tenho uma lista de faturas, uma pequena lista com ID,

03:29

client ID, valor, data de emissão, data de vencimento e status.

03:34

Então aqui eu posso fazer um retorno, e

03:38

o Python é muito bom nesse caso de selecionar dados,

03:43

porque nós conseguimos fazer isso numa linha só.

03:46

Então veja que eu tenho aqui um for,

03:48

que para cada fatura que for capturada, eu

03:56

tenho um if que verifica se o client ID da fatura...

04:01

é igual ao que está sendo passado.

04:03

Então, ele acaba colocando isso nessa lista,

04:06

esse padrão aqui do Python chamado de List Comprehension.

04:13

Enquanto em outras linguagens eu teria que fazer isso...

04:15

Deve fazer em uma linha só, mas acabaria se fazendo em várias linhas.

04:22

Então, uma tool é apenas uma função que desempenha qualquer coisa. Então,

04:28

aqui nós poderíamos ter acesso ao banco de dados, fazer chamada HTTP, ler arquivos.

04:35

É uma função comum.

04:37

Então vamos declarar

04:41

tools no agente,

04:44

passamos uma lista e eu passo apenas a assinatura da função,

04:50

porque quem vai decidir executar vai ser o agente através da LLM.

04:57

Então vamos rodar isso aqui novamente.

05:03

Eu vou aproveitar e colocar duas instruções no...

05:11

Vou colocar, na verdade, uma primeiro, que a gente vai colocando isso aos poucos.

05:15

Para não ficar mostrando esses warnings toda hora,

05:17

nós podemos colocar uma variável de ambiente, que

05:22

é essa aqui de fazer uma supressão dos warnings.

05:27

Ele vai mostrar... Na

05:30

verdade, eu tenho que iniciar o terminal de novo, porque

05:34

aqui ele vai colocar a variável de ambiente no novo terminal.

05:37

Deixa ele ativar.

05:43

Virtualenv, então agora fica bem melhor. Então eu quero listar as faturas.

05:51

Aí aqui nós já temos a confirmação em que ele está chamando essa tool,

05:58

porque o ADK chama a tool como function tool.

06:01

Então aqui ele está mostrando um warning que

06:03

ele teve que fazer o carregamento daquela função,

06:09

ele não executou nada ainda.

06:13

Mas aqui ele pediu o ID do cliente, então vamos colocar

06:17

Na verdade, vamos colocar 001, porque nós não vamos ter nenhuma fatura associada. Então, olha só.

06:25

Verifiquei, mas não encontrei faturas registradas para o seu ID.

06:28

Então, com o ID válido, vou

06:32

pegar esse cliente, 123, é o meu ID.

06:38

Ele vai ter que mostrar as faturas. Pronto.

06:44

Eu poderia pedir uma explicação para as faturas.

06:52

E agora, com o contexto,

06:54

ela vai conseguir me falar sobre. Uma já foi paga, outra está pendente, enfim.

07:00

Um agente pode ter quantas tools forem necessárias.

07:04

Aqui nós temos apenas uma. Nós vamos empilhando tools conforme for preciso.

07:12

Então, a tool é fácil de entender.

07:14

É porque você já tem um conhecimento básico de programação.

07:18

É uma função que você vai criando para poder desempenhar qualquer coisa local,

07:23

acessar qualquer coisa externa, enfim.

## Resumo IA

[RESUMO_IA]