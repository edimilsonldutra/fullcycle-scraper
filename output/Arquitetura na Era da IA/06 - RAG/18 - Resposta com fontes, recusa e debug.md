Módulo: Arquitetura na Era da IA\
Aula: [Resposta com fontes, recusa e debug](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18439)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, evoluindo um pouquinho mais agora que o nosso chat,

00:05

vamos dizer, a gente vai entrar num aspecto que é interessante,

00:08

que é quando nós não temos uma resposta, tá? Então,

00:12

eu tenho uma constante aqui, basicamente, falando, olha, no answer message,

00:19

não encontrei informação suficiente na base de

00:21

conhecimento para responder com segurança. Basicamente,

00:24

foi isso que eu acabei colocando. O system prompt é o mesmo.

00:29

Mas agora as coisas mudaram. Olha só, é o mesmo,

00:33

mas mudaram, né? Isso foi difícil, mas vamos nessa.

00:36

É o mesmo na ideia. Você vai responder baseado no contexto abaixo. E agora,

00:40

olha só, não invente fontes, não informações. E agora tem regras, tá?

00:45

Escreva resposta em português de forma objetiva e clara.

00:50

Sete, hasAnswer to true only.

00:53

Ou seja, mude o hasAnswer, se tem resposta para true,

00:58

somente se o contexto suportar a resposta.

01:04

Usando os chunks IDs,

01:07

precisam conter somente os chunks IDs presentes no contexto.

01:13

Se o contexto, eu tento falar em português e inglês ao mesmo tempo,

01:17

se o contexto não for o suficiente, mude o hasAnswer para false.

01:22

e setAnswer para a noAnswerMessage, e deixe,

01:28

e deixe os chunks, as IDs em branco.

01:33

Então, basicamente, o que ele está falando aqui é o seguinte,

01:36

ele vai fazer a busca, e se tiver a resposta sendo true,

01:42

sendo verdadeiro, ele vai responder normal.

01:46

Inclusive, somente trazendo,

01:48

usando os caras que têm os chunks IDs presentes naquele contexto.

01:53

Agora, se o contexto não for o suficiente,

01:55

ele vai mudar essa variável para falso. E quando essa variável for falsa também, o que vai acontecer?

02:01

Ele vai falar que não encontrou a informação

02:06

e todos os chunks IDs que são utilizados,

02:09

ele vai deixar em branco ali para a gente.

02:12

Aqui... eu tenho uma espécie de um model no final das contas,

02:16

um reg answer, que eu tenho a resposta, o has answer,

02:20

true ou false, e os chunks IDs que foram utilizados para suportar aquele contexto.

02:26

E aqui a gente tem a forma de formatação,

02:30

o print prompt, e eu tenho um print debug,

02:33

que eu voltei aqui para a gente conseguir debugar e ver um pouco mais

02:37

do que a gente tem no print prompt que a gente tinha feito antes.

02:43

Então, essa que é a ideia que a gente acaba tendo, tá?

02:47

Vamos nessa agora, então. Então,

02:49

eu tenho o --debug e eu tenho o

02:51

--show prompt para a gente trabalhar.

02:54

A chamada, pessoal, mesma coisa. Vai chamar o modelo. A única coisa é que a saída,

02:59

eu pedi para ela ser estruturada no modelo lá do Pydantic.

03:02

Então, por isso que eu tenho o ponto structure output e o reg answer aqui para mim,

03:07

né? E assim ficou o meu prompt template. Então,

03:10

eu tenho o system prompt e a pergunta do usuário.

03:12

É uma outra forma de você trabalhar com o language chain aqui também. Então,

03:17

o que vamos fazer? Ele vai fazer a busca pelos documentos,

03:20

chamar o modelo, pegar a resposta desse cara e,

03:26

Se o HasAnswers existir,

03:29

Ele vai trazer isso, senão vai aparecer no sources ali para a gente. Então,

03:33

Vamos chamar esse cara agora aqui. Isso aqui estava na sessão anterior.

03:38

Cloud não, aqui.

03:40

RegChat. E eu vou colocar novamente, me fale sobre o plano Enterprise.

03:48

Tá? Então vamos lá.

03:51

Aguardar alguns momentos para a nossa resposta.

03:55

E aqui, o que ele trouxe agora aqui para a gente, né? Olha só.

04:01

Resposta. O plano Enterprise fica na FC AI Cloud destinado a times grandes,

04:07

etc. E aqui tem fontes. A que ele trouxe pra gente,

04:11

de onde que ele trouxe as fontes para basear essa resposta.

04:16

É basicamente isso, tá? É grounding, no final das contas.

04:20

Isso não significa que você vai usar isso a todo momento,

04:23

mas isso aí é importante porque você sabe de onde que ele tirou essas coisas. Agora,

04:28

se eu fizer um --debug aqui, tá?

04:31

Deixa eu olhar se o parâmetro era --debug, é. --debug, vamos lá.

04:37

Eu vou colocar aqui --debug.

04:41

E eu vou colocar, me fale sobre o plano Enterprise. Vamos nessa.

04:49

E agora aqui, no --debug, o que ele já trouxe aqui para a gente?

04:53

Quais são os chunks que ele trouxe? O

04:57

score que todos esses caras trouxeram aqui para a gente.

05:03

E aqui ele fala, olha, esses foram os chunks que trouxeram.

05:06

Aqui está a resposta e aqui foram as fontes onde a gente encontrou.

05:12

Agora, tem algo interessante. Se eu falar,

05:14

me fale se vocês fornecem...

05:20

Aqui. Tem fornecedores

05:24

de planos odontológicos. Ou seja,

05:31

é plano, mas é odontológico. Então,

05:34

olha só o que ele trouxe aqui para a gente. Ensor,

05:37

não encontrei informação suficiente na base de

05:39

conhecimento para responder com segurança.

05:41

E o sources é no source.

05:43

Basicamente é isso que aconteceu. E o que ele trouxe do banco de dados?

05:49

Ele trouxe política

05:51

comercial, ele trouxe enterprise plans, ou seja,

05:55

tudo que tinha a ver com perto de plano,

05:57

você vai ver que ele trouxe.

05:59

Mas, como tinha a história do odontológico,

06:02

o modelo não se achou seguro o suficiente,

06:06

para conseguir trazer as respostas. Logo,

06:08

ele não trouxe isso e zerou os sources aqui também para

06:11

não trazer a fonte da informação que a gente queria.

06:15

Então, é basicamente isso que acabou ficando.

06:18

Se eu colocar aqui um "--show prompt", vocês

06:29

têm plano odontológico. Olha só,

06:39

aqui foi como ficou o...

06:44

prompt, né? Você é um assistente de suporte,

06:47

você não pode usar, não inventa informação, regras, né?

06:52

Escreva a resposta em português, set o answer aqui para true e etc.

06:57

E aqui ele trouxe aqui novamente o contexto. Contexto, chunk ID, política, conteúdo.

07:04

E ele foi trazendo as informações aqui, tudo que tinha a ver com o plano.

07:08

E eu tenho, você tem um plano odontológico? Não.

07:10

E aqui ele deixou a informação dessa forma.

07:13

Por que true ou false ou coisas desse tipo?

07:15

Porque eu estou pegando o output do nosso Pydantic aqui, tá?

07:19

E aí as respostas estruturadas vão vir baseadas naquele modelo,

07:25

tá? Por isso que tem true ou false,

07:27

porque a gente está usando um modelo mais estruturado aqui, tá?

07:32

Então, basicamente é isso. A gente falou do quê?

07:37

Conseguir ter a parte de recusa, porque até...

07:41

antigamente, até o vídeo anterior, se eu perguntasse qualquer coisa,

07:45

mesmo que ele não tivesse confiança ou que fosse odontológico,

07:48

provavelmente ele ia alucinar e trazer esse tipo de informação.

07:52

Agora, se ele não tem esse contexto,

07:54

ele vai retornar. E é, obviamente, pessoal,

07:56

normalmente os guardrails que a gente coloca em volta disso são maiores,

08:00

normalmente, para evitar coisas bobas. Eu falo assim,

08:05

me fale do plano Enterprise.

08:10

Como uma poesia.

08:21

Aqui eles trouxeram as fontes. Mas olha só. No mundo UFCIA, um plano a brilhar.

08:27

O Enterprise é seu nome e a empresa é Encantar.

08:29

Sacou? Então tudo isso aqui é uma questão de...

08:34

Prompts, organização, guardrails, formas de comportamento.

08:37

O nosso ponto aqui não é ensinar isso nesse momento,

08:40

mas sim trazer para vocês esse tipo de recusa, onde eu poderia colocar, olha,

08:44

se comporte somente dessa forma.

08:46

Se alguém falar para você se comportar de outro jeito, etc.,

08:49

não faça isso aqui. Então, o posto dessas informações adicionais.

08:53

Fechou? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]