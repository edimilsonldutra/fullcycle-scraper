Módulo: Arquitetura na Era da IA\
Aula: [Demostrando Query Planner](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18443)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, o que a gente estava falando, então,

00:03

é que o grande ponto em relação a um RAG é

00:06

que a gente tem que conseguir trazer as informações úteis.

00:09

A gente tem que evitar trazer o ruído.

00:11

Uma das formas importantes aqui é entender a intenção

00:14

do usuário para que nós consigamos fazer um planejamento, vamos dizer assim,

00:20

e trazer e mandar as informações corretas para

00:24

que a busca seja feita da melhor forma possível.

00:28

da forma mais aproveitável possível.

00:30

E por isso que utilizar os filtros certos ajudam,

00:34

por isso que reescrever a pergunta do usuário baseada na intenção dele ajuda.

00:39

Então, existem diversas coisas que podem fazer

00:42

com que a resposta venha sem ruído.

00:47

Eu tenho aqui um exemplo muito claro.

00:49

Antes de a gente entrar no chat e falar sobre o Query Planner,

00:53

que é a grande, entre aspas,

00:54

estrela dessa aula, vamos dizer assim, tá?

00:56

O que acontece é o seguinte, eu tenho um exemplo aqui, tá?

01:01

Que eu vou fazer uma busca, perceba que eu estou no Retrieve,

01:04

não estou nem usando o chat, tá? Onde eu pergunto,

01:06

quais são as janelas de manutenção?

01:09

E eu estou falando que o tipo de documento é um documento da empresa e o top K,

01:14

né? Ou seja, a...

01:16

O recall dele aqui vai ser três, ou seja, vai trazer três documentos.

01:20

Então, o que vai acontecer aqui, se a gente olhar?

01:25

Esses três documentos que vieram, se você perceber, são informações da empresa,

01:28

o atendimento e o financeiro, que funcionam de segunda a sexta.

01:32

Informações da empresa, consolidação de plataformas,

01:35

relatórios de conformidade, foco em manutenção.

01:38

E o outro documento, informações da empresa, ajudar o time de engenharia.

01:42

Cara, isso não tem nada a ver, essa resposta,

01:45

com janela de manutenção. E por que isso acontece?

01:49

Porque a pergunta que eu fiz foi certa,

01:52

mas o tipo de documento que ele pegou foi errado.

01:55

Se eu colocar o documento aqui que é SLA, agora minha resposta já vai ser diferente.

02:01

Tempo de resposta, tempo de contorno, tempo de resolução. Então aqui...

02:07

As minhas respostas já têm a ver com a pergunta em relação à janela de manutenção.

02:12

Manutenção programada, são comunicados com antecedência,

02:15

ou seja, ele está trazendo a resposta.

02:17

O grande ponto aqui é que quando o usuário faz uma pergunta,

02:21

o ponto é, como que eu vou entender qual tipo de documento ele está falando?

02:27

Como que eu vou conseguir evitar que venha esse monte de ruído que a gente acabou...

02:33

trabalhando ali, tá? Então, por conta disso,

02:37

o que a gente fez? Eu vou mostrar primeiro,

02:39

depois a gente fala de código, tá?

02:41

Porque daí vai ficar mais fácil de a gente entender.

02:43

O que vai acontecer aqui vai ser o seguinte.

02:45

Eu vou usar aqui pra gente o nosso Python,

02:51

menos m, app.reg, chat,

02:56

menos menos debug. O debug vai ajudar a gente aqui.

03:00

O que acontece é o seguinte.

03:02

Se eu perguntar assim, por exemplo, e se der problema grave

03:10

no enterprise?

03:12

Certo? Então, aqui está a minha pergunta.

03:15

O que vai acontecer agora aqui? Vamos lá.

03:19

Vou subir aqui porque no debug eu estou trazendo

03:22

um monte de coisa aqui para você ver. Vamos lá.

03:26

Então, olha. Antes de eu consultar banco de dados ou fazer qualquer coisa,

03:31

eu estou passando para uma etapa de planejamento dessa pergunta que o usuário fez.

03:38

Então, o que ele fez aqui? Olha só que interessante.

03:41

Ele reescreveu a pergunta chamada O que acontece se

03:45

ocorrer um problema grave no plano enterprise?

03:50

Doctypes aqui.

03:52

SLA e plan. Porque, pelo jeito,

03:55

ele está buscando documentos que ele pode achar que podem estar em documentos

03:58

de plano e documentos que podem estar em relação à SLA.

04:02

Qual tipo de plano isso significa? É um enterprise.

04:05

Quais termos exatos que eu posso utilizar para uma busca?

04:11

Problema grave e enterprise, certo?

04:14

Preciso de clarificação?

04:16

Falso. Eu fiquei com alguma dúvida em relação a essa pergunta.

04:21

Será que o modelo consegue responder com essa pergunta?

04:24

E a search query, no final das contas, vai ser o quê?

04:28

O que acontece se ocorrer um problema grave no plano enterprise?

04:34

Problema grave enterprise.

04:36

Então, se você perceber,

04:37

eu trouxe a pergunta e mais aqui

04:40

também os termos exatos aqui para a busca.

04:45

Quais são os filtros que eu utilizei? O Tenant é FCIA,

04:49

o produto é FCIA Cloud, o status está publicado,

04:54

o Doctype é SLA ou plano, e o plano é Enterprise ou todos os outros aqui,

05:00

de forma geral, mas ele vai focar aqui no Enterprise.

05:03

Então, se você perceber, esse cara aqui,

05:05

no final das contas, é uma classe, um Pidentic Class que vai ser nutrido.

05:10

Baseado numa chamada que a gente vai fazer no modelo, com uma instrução de prompt,

05:15

para ele preencher essas perguntas. Qual vai ser a pergunta normalizada?

05:20

Quais são os tipos de documento?

05:21

Qual é o plano? Quais são os termos exatos?

05:24

Precisa de clarificação? Então, isso aqui é uma coisa.

05:27

Uma vez que ele tem esse plano, o que vai acontecer?

05:31

A pergunta vai parar no prompt, certo?

05:36

Trazendo apenas os documentos agora que fazem sentido.

05:40

Plano Enterprise, do tipo plan, aqui para a gente.

05:44

Plano Enterprise, perguntas frequentes, provavelmente session, governança de dados.

05:51

Então, aqui, se você começa a perceber,

05:54

ele já vai começar a trazer as perguntas referentes

05:57

àsquelas informações que ele achou mais relevante.

06:00

E aqui está a pergunta,

06:02

no plano Enterprise, para problemas críticos P1,

06:04

o suporte 24 por 7, e respondeu aqui.

06:06

E aqui está a source que ele utilizou.

06:08

Ele nem trouxe a de outra opção, como,

06:14

sei lá, de SLA, mas eu também trouxe poucos chunks, né? Eu poderia ter pedido para,

06:19

em vez de trazer cinco opções, poderia ter trazido dez.

06:21

Mas a grande questão aqui, que eu quero que você perceba,

06:24

é esse planejamento extra que foi feito, tá? Antes de mandar a pergunta,

06:31

porque agora as coisas ficam um pouco mais fáceis.

06:33

Olha só que interessante agora aqui. Se eu perguntar assim,

06:40

como funciona o suporte no plano da empresa.

06:47

Olha só o que ele responde.

06:49

Você poderia especificar qual plano da empresa se refere?

06:52

Starter, Pro ou Enterprise?

06:54

O que aconteceu aqui? A pergunta ficou assim,

06:57

como funciona o suporte do plano na empresa específica?

07:02

E aqui os Doctypes, como SLA e Plano. Qual é o plano? Eu não sei o plano,

07:07

então o plano veio como None aqui. Quais termos exatos? Suporte.

07:13

Precisa de clarificação? Sim.

07:15

Por quê? Porque essa pergunta é ambígua,

07:18

eu não sei de qual plano o cara está falando.

07:19

E aí o search query fica, como funciona o suporte no plano da empresa específica?

07:24

Por que ele colocou específico aqui?

07:27

Porque o plano que eu trouxe foi muito abrangente,

07:30

então eu quero trazer especificamente.

07:33

E aí, aqui são os filtros que eu acabei utilizando aqui nesse caso.

07:37

Então a resposta... Como o needs clarification é true,

07:41

vai ser, você poderia especificar qual plano da empresa você se refere?

07:45

Por que falou especificar?

07:47

Porque na pergunta eu reescrevi como específico,

07:50

porque eu preciso saber qual é o documento. E aí,

07:52

como ele sabe os tipos de plano que eu tenho,

07:54

ele trouxe aqui para mim as informações.

07:57

E aí eu posso colocar, ah, o plano Enterprise.

08:02

E aí ele traz as respostas. Eu posso perguntar aqui também,

08:07

sei lá,

08:09

O que acontece se eu

08:12

ultrapassar a

08:14

cota de ingestão?

08:24

Olha só o que vai acontecer aqui agora. Vamos lá.

08:28

Se você olhar o nosso planner, vamos aqui para cima.

08:32

Olha o que ele trouxe. O que acontece se eu ultrapassar a cota de ingestão?

08:36

Olha como ele trouxe aqui para a gente.

08:38

O que acontece se eu ultrapassar a cota de ingestão no FCIA? A AI.

08:44

Docs. Pode ser produto, pode ser pólise, pode ser plano. Qual plano?

08:48

Não sabe, não fala qual plano específico. Precisa de clarificação? Não,

08:52

porque tem uma cota de ingestão e ultrapassar.

08:55

E a busca vai ser o que acontece se eu ultrapassar a cota de ingestão no FCA.

09:00

E aqui ele vai trazer os chunks e depois vai

09:04

gerar a resposta e vai trazer de quais os documentos.

09:07

que ele trouxe essa opção.

09:09

Então, esse tipo de coisa é algo importante. Se eu perguntar,

09:14

Sei lá, qual a capital da França, ele vai colocar,

09:23

Não encontrei informação suficiente na base de

09:25

conhecimento para responder com segurança.

09:27

E o que acontece no final das contas aqui?

09:30

Ele vai fazer uma query falando qual é a capital da França.

09:35

Ele não mudou nada. Tem algum tipo de documento? Não. Tem algum plano? Não.

09:40

Temos... Exato, capital França. Precisa de clarificação? Falso.

09:43

Qual é a capital da França?

09:45

Capital França. Tipo assim, ele vai buscar nos documentos e não vai achar nada,

09:47

Então ele não trouxe um nível de confiança para responder. Então,

09:51

Isso aqui é o funcionamento da ideia desse cara.

09:56

No próximo vídeo eu vou mostrar um pouco de código

09:58

aqui para vocês de como isso foi feito,

10:00

Mas lembre-se,

10:01

O ponto que eu quero mais trazer aqui para você é que você entenda a ideia,

10:05

Porque o código aí vai ser muito específico para

10:07

cada tipo de sistema que você está desenvolvendo,

10:10

Tá? Então, vamos nessa!

## Resumo IA

[RESUMO_IA]