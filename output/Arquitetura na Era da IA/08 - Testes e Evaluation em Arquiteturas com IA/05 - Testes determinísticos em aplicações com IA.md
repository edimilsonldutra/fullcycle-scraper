Módulo: Arquitetura na Era da IA\
Aula: [Testes determinísticos em aplicações com IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18784)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente criou o primeiro

00:05

dataset de avaliação no nosso Knowledge Chat.

00:08

A ideia ali foi organizar casos representativos.

00:11

Perguntas que o sistema deve responder,

00:14

perguntas que ele deve recusar e perguntas

00:17

ambíguas onde o melhor comportamento é pedir esclarecimento.

00:22

Agora, antes de sair usando...

00:25

Judge, Ragas, Score Semântico ou qualquer avaliação mais sofisticada,

00:31

a gente precisa voltar para uma base que continha...

00:35

que continua sendo fundamental na realidade,

00:38

que são os nossos testes determinísticos.

00:41

E aqui é importante separar bem as coisas. Quando a gente fala de sistemas com IA,

00:47

muita gente já pensa direto em avaliação subjetiva.

00:52

Será que a resposta ficou boa? Será que o modelo foi relevante?

00:56

Será que o texto ficou claro? Será que o judge deu uma nota alta?

01:02

Tudo isso é de fato importante,

01:05

mas existe uma camada anterior que não deveria depender do julgamento semântico.

01:10

A aplicação continua tendo,

01:14

no final das contas, um contrato. Então,

01:16

se a API diz que retorna answer, has answer, needs clarification,

01:21

sources e debug, esses campos precisam existir.

01:25

Se a sua pergunta não tem a resposta na base,

01:29

o sistema precisa retornar uma recusa controlada. Se o hasAnswer é falso,

01:35

não deveria ter fonte. Se o hasAnswer é verdadeiro,

01:39

a resposta precisa ter pelo menos uma fonte.

01:42

Se o debug for igual a falso, a API não deveria retornar debug.

01:48

Se o debug é igual a true, o debug precisa aparecer como uma estrutura válida.

01:53

Nada disso precisa de um LLM as judge.

01:58

Isso aí, no final das contas, é teste determinístico.

02:01

É o tipo de avaliação que a gente consegue fazer com um acerto normal,

02:05

com um PyTest, com um teste de API, com esquema, com contrato e etc.

02:13

Ela é extremamente importante, porque antes de discutir se a resposta está boa,

02:18

a aplicação precisa estar se comportando de forma previsível.

02:22

E pensa no nosso Knowledge Chat.

02:25

A resposta pode variar um pouco no texto. O modelo pode responder.

02:29

O plano Enterprise tem a resposta até uma hora para P1.

02:34

Ou, para incidentes P1 no Enterprise,

02:36

o tempo de resposta é de até uma hora com atendimento 24 por 7.

02:41

As duas respostas podem estar corretas,

02:43

mas o contrato não pode variar do mesmo jeito.

02:47

Se a aplicação respondeu com hasAnswer .true,

02:51

ela precisa sustentar isso com fonte. Se o sistema pediu esclarecimento,

02:55

ele não deveria fingir que respondeu. Se a pergunta está fora da base,

02:59

ele não deveria devolver fonte aleatória só para preencher o campo.

03:04

E esse tipo de teste pega problemas que

03:06

uma avaliação semântica poderia deixar passar.

03:10

Por exemplo, imagina que uma resposta textual está boa,

03:14

mas o campo sources veio vazio. Para o usuário final, talvez o texto pareça correto,

03:19

mas arquiteturalmente o sistema quebrou uma regra importante.

03:23

Resposta com regra precisa ser rastreável.

03:26

Outro exemplo, o modelo gera uma resposta perfeita,

03:30

mas o output estruturado falha e a API devolve erro.

03:34

Nesse caso, o problema não é a qualidade da resposta, é o contrato de integração.

03:39

Outro exemplo, o sistema responde, não encontrei informação suficiente,

03:44

mas o resensor veio como true. Então, isso quebra qualquer métrica posterior,

03:49

porque os evaluators vão interpretar aquele caso como resposta válida. Então,

03:54

testes determinísticos continuam sendo a primeira linha de defesa.

03:59

Eles não testam de forma geral só o RAG. Em uma chamada simples, o modelo,

04:05

eles podem validar se a saída está em gestão válida,

04:08

se os campos obrigatórios existem, se os limites de tokens foram respeitados.

04:13

Em tool calling, eles podem variar se a ferramenta chamada existe,

04:17

se o argumento respeita os esquemas,

04:19

se uma ação perigosa exige confirmação ou se uma

04:22

falha de ferramenta gera um erro controlado.

04:24

Em agentes, eles podem validar número máximo de passos,

04:29

se uma ferramenta proibida não foi chamada,

04:31

se o agente parou quando ele deveria e se o resultado final,

04:35

por exemplo, tem uma estrutura esperada. Ou seja,

04:38

antes de avaliar a inteligência, a gente avalia o contrato.

04:42

E isso é uma ideia muito importante,

04:44

porque a pior coisa é transformar avaliação em uma camada nebulosa,

04:48

onde tudo depende de interpretação.

04:51

Sistemas com IA ainda são sistemas de software.

04:54

Eles têm API, contrato, tipo, esquema, política, erro, status,

04:59

limite, fonte, permissão e observabilidade. Então, a ordem saudável é... Primeiro,

05:05

garanta o contrato, depois avalie a qualidade. No nosso projeto,

05:10

a próxima prática vai ser exatamente isso.

05:13

A gente vai usar o dataset que a gente criou.

05:16

Mas ainda a gente não vai julgar se o texto da resposta está perfeito.

05:20

A gente vai validar coisas objetivas.

05:22

A pergunta deveria gerar resposta, então esperemos, por exemplo,

05:26

um resensor igual a true. A pergunta devia pedir esclarecimento,

05:30

então a gente espera que o needs clarification seja igual a true.

05:33

A pergunta deveria ser recusada, a gente espera resensor igual a false.

05:39

Então, se existe resposta, a gente quer fonte.

05:42

Se não existe, a gente não quer fonte.

05:45

Então, esses testes, eles parecem super simples,

05:47

mas eles criam uma base muito importante para o restante do módulo,

05:51

tá? Porque quando a gente chega, por exemplo, em RAGAs ou LLMS Judge,

05:56

Langfields Experiment e comparação de versões,

05:59

a gente não vai estar testando e tentando avaliar

06:02

apenas o sistema que nem respeita o próprio contrato,

06:06

na realidade, né? Então, guarda essa ideia.

06:10

Evaluation não substitui teste determinístico,

06:12

ele complementa. Teste determinístico responde.

06:15

O sistema cumpriu o contrato? Evaluation responde.

06:19

O comportamento foi bom? Em sistemas com IA,

06:22

a gente precisa das duas coisas trabalhando junto. E no próximo vídeo,

06:26

a gente vai colocar isso em prática e criar testes de

06:29

Contrato para o Knowledge Chat usando os casos do nosso dataset.

06:33

Fechou? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]