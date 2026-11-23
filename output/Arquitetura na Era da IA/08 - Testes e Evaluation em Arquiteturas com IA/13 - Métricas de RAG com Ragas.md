Módulo: Arquitetura na Era da IA\
Aula: [Métricas de RAG com Ragas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18792)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Então agora a gente vai ver um pouquinho mais sobre o RAGAS na prática,

00:06

mas a ideia aqui não é ficar focando necessariamente no framework ou coisa do tipo,

00:10

tá? É entender o problema, tá? Então o que que acontece?

00:13

O nosso Knowledge Chat, ele responde, mas ele responde bem?

00:17

Nada do projeto respondeu isso agora ainda para a gente.

00:21

O teste de contrato só olha o formato das respostas,

00:24

a avaliação por componente, para antes de responder. No final,

00:28

ela mede se o pipeline chegou nos documentos certos e acaba encerrando ali.

00:33

Agora, falta a última pergunta. A resposta que saiu está boa?

00:37

Então, por que que, nesse caso, a gente tem a seguinte situação? Por exemplo...

00:44

Todo o evaluator que a gente escreveu até agora era uma comparação de campo,

00:48

ou seja, o plano é igual ao expected plan, o arquivo está dentro das fontes aceitas,

00:54

ou seja, agora a gente tem uma outra situação. Essa resposta afirma só...

01:01

O que os documentos sustentam, essa que eu acho que é a grande ponto,

01:05

né? Não existe um if pra isso.

01:07

A gente precisa de um modelo lendo a resposta e comparando ali com o material.

01:12

E é o que o RAGAS, ele faz.

01:14

E é por isso que hoje eu não vou escrever

01:17

uma métrica nenhuma ali em Python no final das contas,

01:21

tá? Então, o que acontece é o seguinte.

01:24

Depois eu mostro a implementação do código, mas eu vou rodar aqui para eu,

01:29

inclusive, explicar a filtragem aqui para você.

01:32

Então, eu tenho aqui observability enabled, app,

01:35

eval RAGAS, menos, menos, limite igual a 5.

01:39

Então, o que acontece é o seguinte.

01:43

Dos 37 casos que eu tenho,

01:47

só 29 são respondíveis. Por quê?

01:50

Eu tenho 4 de recusa, eles vão ficar de fora.

01:54

Por quê? Porque não existe a resposta para comparar com o contexto.

01:57

Os quatro ambíguos também, porque o pipeline parou de buscar,

02:02

então não existe o contexto. E para eu medir a fidelidade de uma recusa correta,

02:09

daria nota zero no final das contas.

02:11

Ou seja, a gente ia punir o sistema por ter acertado.

02:14

Esses dois comportamentos já foram medidos na realidade na aula passada.

02:19

Agora aqui, deixa ele terminar de rodar. Vamos botar.

02:27

E eu vou esperar o summary que ele vai trazer ali para a gente.

02:30

Ele demora um pouquinho porque ele está batendo no

02:33

modelo para a gente ter ali os resultados.

02:35

E aqui eu estou retornando aqui como se fosse um JSON,

02:39

mas eu gerei ali um evaluation summary. Então,

02:43

se você olhar aqui, eu tenho 37 casos.

02:49

Casos que são respondíveis são 29.

02:52

Cinco casos foram avaliados pelo RAGAS.

02:56

E teve esses caras que falhavam. Se você olhar agora aqui,

03:00

eu tenho três métricas aqui importantes,

03:03

que são a Faithfulness, Responsive Relevance e Context Precision.

03:08

Você vai ver que eu tenho ali Faithfulness como 1 e Context Precision.

03:13

E aqui... Eu tenho o lowest scoring case, né?

03:17

Então ele vai trazer aqui no final das contas quais foram os casos, né?

03:21

Que eu tive com o pior score aqui no final das contas.

03:27

E você já vai entender por conta disso,

03:29

porque a gente tem algo que acaba entrando como

03:32

uma média no meio de toda a história, tá?

03:35

O que acontece é o seguinte, né? Se você perceber, eu tenho três notas.

03:41

Porque uma resposta pode dar errado de três jeitos diferentes.

03:46

Por exemplo, Faithfulness me responde, o modelo inventou.

03:51

Se a resposta afirma algo que não está no material, essa nota vai cair.

03:56

Aí eu tenho Response Relevance, ou seja, ele respondeu o que perguntei.

04:01

Uma resposta pode ser inteiramente verdadeira e ainda assim ser sobre outro assunto.

04:08

E eu tenho também o Context Precision, que é,

04:11

o material entregue prestava, no final das contas,

04:14

o pipeline separa, por exemplo, quatro trechos e manda para o modelo escrever.

04:19

Se só um tinha a ver com a pergunta,

04:22

os outros três, no final das contas, foram ruídos. Então,

04:26

esse é o grande ponto. Então, se eu tenho apenas uma nota,

04:29

eu esconderia, no final das contas, o que os três aconteceram.

04:33

Então, nesse nosso caso, eu tenho o Faithfulness com um...

04:37

E isso não é uma métrica sendo inútil,

04:39

é um resultado e ele tem causa no final das contas, certo?

04:44

Porque ele tem que responder à pergunta somente que o contexto abaixo.

04:48

É falado isso inclusive no nosso documento lá no System Prompt,

04:53

tá? E o 1.0 ele vem daí.

04:55

A Faithfulness no final das contas é o alarme que

04:57

você quer que fique quieto no final das contas.

05:00

No dia em que alguém afrouxar esse prompt,

05:02

esse número vai cair e é pra isso que ele existe, tá?

05:05

A terceira nota é a que, no final das contas,

05:09

acaba se movendo no meio da história, tá?

05:11

Que a gente tem o Response, inclusive,

05:15

a Relevance no meio da história, tá? Então, a resposta certa,

05:22

no final das contas, ela acaba pontuando baixo. Então, o que eu vou fazer aqui?

05:27

Eu vou colocar o seguinte aqui nesse código para que

05:31

fique mais fácil para a gente conseguir ver.

05:33

Quer ver? Deixa eu pegar aqui.

05:35

Que fica, inclusive, mais fácil.

05:41

Pra eu não trabalhar aqui com aquela média lá geral.

05:44

Deixa esse cara rodar. Vamos lá.

05:57

Perceba que eu tô passando um case aí de específico aqui,

06:00

que é o SLAP1 do plano PRO,

06:02

tá? E ele tá fazendo a parte de score com Faithfulness, Response, Relevância, etc.

06:07

Então, se você olhar agora aqui, ó, eu tenho Faithfulness com 1, Response,

06:12

Relevância com 0.9, e eu tenho Context Precision com 1.

06:17

Agora, qual que é a pergunta que foi feita no final das contas?

06:21

Qual é o prazo de resposta para o chamado P1 no plano PRO?

06:25

Essa foi a pergunta que a gente tem.

06:27

Aí a resposta que a gente tem é,

06:29

o prazo de resposta para um chamado P1 no plano PRO é

06:33

de até 8 horas úteis em horário comercial de segunda a sexta-feira.

06:37

E as fontes que foram utilizadas foram o ProPlan.md,

06:41

o Product Support SLA e o ProPlan, aqui novamente como MD Comfort,

06:45

provavelmente foi em chunks ali diferentes, tá? E a grande pergunta agora aqui é,

06:51

essa resposta está errada? E a questão é, ela não está.

06:56

O fato que o dataset cobra é 8 horas úteis e elas estão lá,

07:01

ele não inventou nada, o material era o certo, tá?

07:04

E mesmo assim, o relevance é a nota mais baixa,

07:08

tá? Então, por que que isso acontece?

07:10

Então, é importante que você entenda, nesse caso,

07:13

o conceito de como que o Ragas trabalha.

07:16

O Ragas, ele trabalha de trás pra frente.

07:19

Ele pega só a resposta e esconde a pergunta original e faz algo muito interessante. Ele fala assim, ó.

07:27

Modelo. E manda o modelo perguntar tipo isso, ó.

07:31

Qual pergunta... essa resposta responderia.

07:34

E faz isso umas três vezes e compara com a pergunta de verdade,

07:39

tá? Então, isso aí que é o ponto,

07:42

acho que é mais interessante. Ao invés de eu já passar a pergunta,

07:45

eu pergunto ali no Ragas, ele pergunta.

07:49

Baseado nessa resposta, qual seria a pergunta?

07:51

Ele faz isso três vezes e compara com a pergunta que eu tenho, tá? E...

07:57

No final das contas, a nossa resposta,

08:00

ela emendou em horário comercial de segunda a sexta-feira. Agora,

08:05

ninguém perguntou isso. Uma das perguntas reconstruídas, ela sai,

08:08

por exemplo, qual o horário de atendimento pró?

08:11

Que é outra pergunta. Ou seja, as duas,

08:14

elas acabam se afastando e a nota acaba caindo. Então,

08:18

a relevância, ela não mede se a resposta está certa.

08:21

Ela mede se ela responde o que foi perguntado.

08:25

Resposta correta... ela, vamos dizer assim,

08:28

ela acaba passeando, vamos dizer assim,

08:33

é como se ela pontuasse baixo e no final das

08:36

contas isso acaba sendo uma métrica que está funcionando. Ou seja,

08:39

o número aqui que a gente teve não está dizendo que foi errado.

08:43

Ele disse que no final das contas,

08:45

qual dimensão nesse caso a coisa acabou escapando.

08:51

Então isso aí é um ponto importante.

08:53

Lembrando que nesse caso também a gente pode ter, como que eu posso dizer,

08:59

casos que a gente acaba não tendo nota,

09:05

por exemplo. E por que isso acaba acontecendo no meio de toda essa história?

09:12

Vamos rodar aqui.

09:16

Eu passei um case de company e meio financeiro,

09:19

que a gente sabe que a gente tem aquela situação dele pegar os chunks,

09:25

e deixar esse cara ali de fora, mas olha só que interessante.

09:29

Ele rodou aqui e falou, Patroness, No Cases Scored,

09:35

Response e Context Precision. Por que isso aconteceu no final das contas?

09:41

Porque ele deu aqui, Pailed Before Regas, ou seja, Company Email Financeiro.

09:46

Isso significa o que no final das contas?

09:50

Acabou acontecendo como se fosse o mesmo caso da aula passada.

09:52

O e-mail do financeiro em que a busca trouxe

09:55

o documento de cobrança e ele acabou deixando,

09:58

de forma geral, a resposta certa de fora.

10:01

Agora, nesse caso, a consequência está aparecendo. O pipeline não achou,

10:06

recusou responder e não existia uma resposta para pontuar. Então,

10:11

repare o que ele não fez. Ele não contou como zero.

10:14

O zero misturaria a resposta, que a resposta estaria meio que ruim.

10:20

Tipo, não houve resposta. Então,

10:22

são problemas diferentes com consertos diferentes no final das contas.

10:26

O caso aí da média acaba aparecendo separado. Então,

10:31

acaba sendo a mesma falha, mas visto de dois lugares diferentes.

10:35

Lá era o retrieval errando e aqui é a resposta

10:38

que não existe por conta que aquela parte acabou falhando.

10:43

Então, isso aí é um ponto interessante para que você consiga trabalhar.

10:49

Existe uma quarta métrica que é meio óbvia e eu não usei aqui, que é,

10:53

imagina que você pediu para um estagiário separar

10:56

os documentos que respondem uma pergunta.

10:59

Dá para cobrar duas coisas dele, por exemplo,

11:02

do que ele trouxe, quanto aquilo prestava,

11:06

e veio o lixo junto, por exemplo, e do que prestava, quanto ele trouxe,

11:12

ele esqueceu alguma coisa? Então, a primeira... parte que eu tenho, né,

11:17

é o que a gente chama de precision, que está no relatório ali pra gente. Agora,

11:23

a segunda parte é chamada de recall, tá? A primeira, vamos dizer,

11:28

eu consigo medir sozinho. Por quê? Eu olho o que veio junto, se era útil.

11:34

A segunda parte eu não consigo, por quê? Para saber se ele esqueceu algo,

11:39

eu precisaria saber de antemão qual era a lista completa,

11:43

ou seja, eu teria que ter um gabarito. O nosso dataset não tem a parte de rubricas,

11:49

a gente não tem um gabarito. A gente tem, por exemplo, required terms,

11:53

ou seja, que são pedaços que a nossa resposta precisa conter,

11:56

como oito áreas úteis. Agora, isso aí é um checklist,

12:00

ele não é uma resposta como um modelo. Então,

12:04

eu poderia sentar e escrever 29 respostas modelo,

12:09

vamos dizer assim, como um gabarito,

12:11

e aí sim eu estaria escrevendo a resposta certa

12:14

e conferindo se o sistema chegou perto dela.

12:18

E aí, medindo o quanto o modelo escreveu, a gente conseguiu escrever parecido.

12:23

Então, a gente tem que usar as métricas, no final das contas,

12:27

que os dados conseguem sustentar. Ou seja, eu não tento...

12:32

fabricar um dado para eu conseguir caber uma métrica.

12:34

Então esse aí é um dos pontos importantes aí, tá?

12:38

Então... O RAGAS precisa do texto dos trechos que alimenta a resposta.

12:43

Ele não precisa dos IDs. Esse conteúdo não sai do pipeline.

12:48

Então, os prompts, o contexto, o conteúdo do chunk, etc.,

12:52

eles acabam nunca entrando na telemetria, inclusive.

12:55

Isso é regra, inclusive, do projeto.

12:59

Então, acho que esse aqui é o grande ponto que eu

13:02

quero trazer aqui para vocês em relação a essa parte do RAGAS.

13:06

Eu tenho essas métricas.

13:08

E essas métricas foram feitas e

13:10

verificadas por ele baseado nesses critérios.

13:15

Inclusive, quando eu pego essas respostas,

13:18

a gente vê como ele faz de trás para frente para conseguir associar a

13:22

pergunta que foi feita com a pergunta do usuário também que a gente tem.

13:26

Tá? No próximo vídeo,

13:27

Eu vou passar rapidamente aqui pelo código,

13:30

Eu não quero ficar focando muito em código,

13:32

Eu quero focar muito mais na ideia, nesse caso,

13:36

Então você tem um cara que chama Ragas,

13:38

A gente tem aqui o que ele conseguiu medir aqui pra gente,

13:41

Como que esse cara acabou fazendo aí nesse caso, né?

13:45

E a gente tem inclusive um dado aqui,

13:48

Mas eu mostro no outro vídeo, que é Eval Runs,

13:52

Onde eu tenho os Ragas aqui que eu rodei, onde ele tem, né? Tudo que aconteceu,

13:57

O caso por resultado aqui. Então,

14:00

A gente tem aqui toda a informação que acabou acontecendo e

14:04

Qual a resposta que ele acabou trazendo para cada item aqui.

14:08

Então, casos por resultado, quais foram os dados,

14:11

A precisão, então ele acabou trazendo.

14:13

Mas depois a gente olha esses caras aí com calma. Vamos nessa.

## Resumo IA

[RESUMO_IA]