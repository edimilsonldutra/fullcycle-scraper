Módulo: Arquitetura na Era da IA\
Aula: [Primeira resposta com RAG](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18438)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, agora a gente está chegando num ponto que começa a ficar legal,

00:05

porque finalmente a gente saiu de um retrieval e

00:09

agora a gente tem o nosso primeiro chat, ele é simples,

00:11

mas agora a gente já vai montar o nosso prompt.

00:16

E esse prompt é o que vai fazer com que a

00:19

resposta do nosso chat seja uma resposta gerada por IA,

00:22

mas com o contexto que a gente tem.

00:27

Então, basicamente, destaquei cinco, ou seja,

00:29

vai trazer cinco registros no banco de dados,

00:31

tem os meus filtros, e agora comece a prestar atenção.

00:35

Eu tenho aqui o meu system prompt, tá? O meu system prompt, ele está em inglês,

00:39

poderia estar em português, aí vai depender muito de como você quer trabalhar,

00:42

por padrão aqui está em inglês. Está falando,

00:44

você é um assistente de suporte para o FCAI,

00:47

responda às perguntas do usuário,

00:50

somente com o contexto abaixo, não use...

00:54

conhecimentos anteriores e não invente informações.

00:57

Se esse contexto não tiver informação suficiente para responder,

01:02

diga claramente. Você não tem informação suficiente na sua base de conhecimento.

01:08

Seja objetivo e claro e sempre responda em português, aqui nesse caso. E aqui,

01:13

se você olhar, eu tenho o contexto que está sendo interpolado,

01:18

concatenado com o meu contexto.

01:22

E agora sim a gente vai entender qual que é esse contexto.

01:25

Então, tem uma função aqui chamada de format context.

01:28

O que ela está fazendo? Ela está pegando uma lista de documentos,

01:32

pegando os metadados e organizando as linhas desses documentos para como?

01:36

O nome do documento e de onde ele vem,

01:39

o título dele, se tiver a seção, traz o título,

01:42

traz a versão, traz conteúdo dois pontos e o conteúdo do documento embaixo.

01:47

E ela dá um join, ou seja,

01:48

ela pega todos os conteúdos e gera exatamente nesse formato aqui para a gente.

01:55

Então, essa que é a ideia. E aqui,

01:57

só para você saber como é que vai ficar depois,

01:59

eu criei um --show prompt para a gente

02:02

ver como é que o prompt ficou sendo exibido. Então,

02:06

eu tenho --show prompt para a gente conseguir verificar.

02:09

Então, na prática aqui, na minha função principal, é...

02:13

Eu me conecto com o banco de dados, chamo o modelo da OpenAI, tá?

02:17

E agora sim eu vou chamar o modelo, entende?

02:21

Agora sim eu estou fazendo a chamada do LLM.

02:24

Então, eu estou pegando o meu prompt inicial, mais a pergunta do usuário, ok?

02:32

E aqui é um loop, né? Que eu posso ficar fazendo várias perguntas.

02:35

Mas agora o que vai acontecer? Ele busca aqui por similaridade, né?

02:41

Faz a chamada agora para a IA. Então, quando você olha aqui o prompt .invoke,

02:47

nesse momento, eu estou chamando o LLM. Então, pela primeira vez,

02:53

entre aspas, a gente está chamando o LLM,

02:56

porque antes a gente estava chamando e fazendo consulta no banco de dados. Agora aqui não.

03:01

Eu estou pegando os documentos que recebi baseado

03:05

nesse prompt e jogando esse prompt lá para,

03:08

nesse caso, a OpenAI.

03:09

para pegar esse resultado e retornar para o usuário baseado naquelas instruções.

03:14

E aqui a gente pega a resposta do modelo para fazer essa chamada aqui.

03:21

Então, é basicamente isso que acaba acontecendo. E aqui tem a resposta e o texto.

03:25

Então, primeiro eu vou fazer uma pergunta normal e

03:29

depois eu vou rodar com o menos menos prompt,

03:33

só para a gente olhar. Então, Python, aqui, RegChat,

03:37

eu vou perguntar. Me fale sobre o suporte P1.

03:46

E agora ele vai trazer aqui para mim, olha só.

03:49

O suporte P1 no plano Enterprise oferece atendimento 24

03:53

por 7 com respostas em até uma hora.

03:56

Chamados classificados com P1 são considerados críticos e

03:59

são relacionados imediatamente com o plantão local.

04:01

Ok. Me fale do plano Enterprise.

04:07

Então você vai começar a perceber que no final das contas...

04:12

ele vai responder aqui para mim agora.

04:15

Perceba que ele já está pegando informações do meu contexto.

04:18

O plano Enterprise do FC Cloud é voltado para empresas com times grandes,

04:23

alto volume. Agora, se você perceber, eu nunca treinei o meu modelo.

04:27

A única coisa que eu fiz é como se fosse, na realidade, na minha opinião,

04:31

é como se Reg fosse uma espécie de uma gambiarra,

04:33

onde você concatena a resposta junto com a pergunta do usuário para ele responder.

04:38

Então, vou dar um Ctrl C aqui para ele sair.

04:41

E vou colocar aqui, menos show prompt. Eu vou fazer a pergunta novamente.

04:45

Olha só. Me fale sobre o plano enterprise.

04:50

E vamos ver o que foi enviado para o LLM.

04:53

Então, vamos lá. Olha só que interessante.

04:56

Lembra aquelas instruções iniciais? Sistema. Você é um assistente de suporte,

05:01

responda isso em português. Isso a gente tinha lido. Agora aparece contexto.

05:07

Documento enterprise plan .md. O título. O section, a version,

05:12

o conteúdo. E aqui tem um trecho, tá?

05:16

Que veio dos meus chunks, tá?

05:20

Aqui eu tenho um outro cara aqui também, olha só.

05:24

Enterprise, plano. Aqui, sessão, gestão de usuários de acesso.

05:28

E aqui ele traz um conteúdo sobre essa parte.

05:31

Aqui um outro documento de perguntas frequentes,

05:34

a sessão aqui, tá vendo? E aqui tem,

05:37

enterprise tem seu limite de usuários? Não. Então está trazendo informação.

05:40

Billing, ou seja, está trazendo coisas desse plano em relação à parte de pagamento.

05:45

Política comercial. E depois tem, acabou o conteúdo, se você perceber,

05:50

tudo isso aqui é conteúdo que ele montou.

05:52

Eu tenho agora humano aqui para mim e está escrito aqui a pergunta do humano.

05:58

Me fale sobre o plano enterprise.

06:00

E aqui eu coloquei aqui end of prompt, basicamente.

06:03

E aqui tem a resposta. Então, a resposta que ele trouxe aqui para a gente.

06:07

Então, no final das contas,

06:09

o LLM está recebendo esse prompt aumentado para fazer a geração.

06:15

E por isso que a gente fala sobre RAG, que é Retrieval.

06:18

A gente pegou Augmented, onde a gente aumentou o contexto.

06:22

Generation, onde a gente gerou a resposta aumentada,

06:27

mas não necessariamente vindo do treinamento do modelo, mas sim...

06:34

Injetada dentro do prompt do cara. Então, isso aqui é o nosso primeiro reg, assim,

06:40

o mais simples, mas isso aqui, vamos dizer, já é um reg. Beleza?

## Resumo IA

[RESUMO_IA]