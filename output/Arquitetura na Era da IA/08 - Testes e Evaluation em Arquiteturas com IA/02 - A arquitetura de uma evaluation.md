Módulo: Arquitetura na Era da IA\
Aula: [A arquitetura de uma evaluation](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18781)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente falou sobre por

00:04

que um teste tradicional continua sendo importante,

00:07

mas não é mais suficiente para a gente colocar ali,

00:10

quando a gente coloca uma IA dentro da aplicação.

00:13

Agora a gente precisa organizar o vocabulário e

00:16

entender a arquitetura de uma evaluation,

00:19

vamos chamar assim, tá?

00:20

Por que evaluation não é simplesmente perguntar para o modelo?

00:23

Essa resposta está boa.

00:25

Isso pode até fazer parte do processo, mas não é o processo inteiro.

00:30

Então, uma evaluation bem pensada tem algumas peças principais. A principal é,

00:36

a principal não, vamos dizer, a primeira é o dataset.

00:39

O dataset é um conjunto de casos que você

00:42

vai usar para avaliar o comportamento da aplicação.

00:45

No nosso caso, por exemplo, podemos ter, por exemplo,

00:49

perguntas que o nosso knowledge chat deveria responder,

00:51

perguntas que ele deveria recusar.

00:54

Perguntas ambíguas que devem gerar esclarecimentos e

00:57

perguntas que exigem uma fonte específica.

01:00

Então, o dataset não é só uma lista de perguntas.

01:04

Ele carrega a intenção de teste. Para cada caso,

01:08

eu posso dizer se o sistema deveria responder,

01:11

se ele deveria pedir esclarecimento, quais arquivos deveriam aparecer como fonte,

01:15

quais termos deveriam estar presentes na resposta e

01:18

quais tags ajudam a classificar aquele caso.

01:22

Por exemplo, Uma pergunta sobre o SLA P1 no nosso plano Enterprise,

01:27

ele pode ter como expectativa que a resposta cite o

01:31

documento de SLA e mencione 1 hora e 24 por 7.

01:36

Já é uma pergunta sobre o contrato da empresa Acme,

01:40

por exemplo, é bem comum a gente sempre usar esses nomes fakes,

01:44

que não existe na base. Ele deveria ter uma expectativa de recusa.

01:51

E aí a gente vem para a nossa segunda peça, que é o nosso target.

01:56

Então o target é aquilo que está sendo avaliado.

02:01

Pode ser, por exemplo, primeiro a API inteira, a pipeline do reg, o query planner,

02:06

o retrieval, o re -ranking, uma chamada simples a um modelo,

02:10

uma tool call ou um agente, por exemplo. Então,

02:13

isso é importante porque nem toda evaluation precisa

02:16

rodar o sistema de ponta a ponta.

02:19

Às vezes eu quero avaliar só se o query planner identificou o doc type correto.

02:24

Às vezes eu quero avaliar se o retrieval trouxe o documento esperado.

02:27

Às vezes eu quero avaliar se a resposta final ficou boa.

02:30

Cada target responde uma pergunta diferente. A terceira parte aqui,

02:35

a terceira peça, vamos dizer assim,

02:36

de um evaluation é o evaluator. O evaluator é quem avalia o resultado.

02:43

E é aqui que a gente tem tipos diferentes.

02:45

Então, um evaluator pode ser determinístico.

02:49

Por exemplo, a resposta tem hasAnswer igual a true.

02:54

E a lista de fontes contém product, suporte, sla .md.

03:00

e o JSON tem todos os campos obrigatórios, o sistema recusou quando deveria recusar,

03:05

Então esse tipo de avaliação é mais objetiva e deve ser usada sempre que possível.

03:11

Mas também a gente pode ter evaluators mais subjetivos,

03:15

principalmente quando a gente avalia a qualidade da resposta. Nesse caso,

03:20

a gente pode utilizar um LLM como juiz, com uma rubrica bem definida. Então,

03:27

ele pode avaliar se a resposta está fundamentada no contexto,

03:31

se está completa e se ela é relevante e se ela não inventou, por exemplo, uma informação.

03:37

Legal? E aí a gente tem a nossa quarta peça,

03:40

que é o score. O score é o resultado da avaliação.

03:43

Pode ser booleano, ele pode ser como passou, falhou, no final das contas.

03:48

Pode ser numérico, como uma nota de 0 a 1. Pode ser categórico, como passou,

03:53

falhou ou needs review.

03:55

E o importante é que o score transforme a avaliação em algo comparável.

04:01

E aí a gente tem a quinta peça, que é o threshold.

04:05

O threshold é o limite mínimo aceitável. Por exemplo,

04:09

eu posso dizer que a taxa de fontes corretas precisa ser pelo menos em 85%.

04:14

Ou seja, a taxa de recusa correta precisa ser pelo menos 90%.

04:21

Que o score médio do judge precise ficar acima de 0.8.

04:26

Sem threshold, a avaliação vira apenas um relatório.

04:29

Com threshold, ele começa a virar um mecanismo de qualidade,

04:33

certo? E aí a gente tem a sexta peça,

04:36

que é o baseline. O baseline é uma versão de referência.

04:41

Ele pode ser um comportamento atual do sistema,

04:44

uma versão anterior do prompt,

04:46

um modelo anterior ou uma configuração anterior do pipeline.

04:50

Isso é essencial porque em A, muitas vezes,

04:53

a pergunta não é apenas ficou bom. A pergunta é,

04:57

ficou melhor ou ficou pior do que antes? Então, se eu mudo o prompt, troco o modelo,

05:02

altero o chunking, ou mesmo no re-raking, ou preciso comprar uma versão anterior,

05:06

talvez uma métrica melhore e outra piore. Então,

05:11

talvez a resposta ficou mais completa, mas ficou mais cara.

05:14

Talvez o retrieval melhore para a SLA,

05:17

mas piore para a parte de billing. Então, sem baseline,

05:20

é difícil perceber regressão. E a última peça é o experimento.

05:25

Um experimento é uma execução organizada da avaliação.

05:29

Você pega um dataset, roda contra um target, aplica os evaluators,

05:34

gera os scores, compara os thresholds ou os baselines.

05:40

Então, a estrutura fica mais ou menos assim.

05:43

Eu tenho um dataset com casos representativos.

05:46

Eu escolho o que eu quero avaliar, rodo a aplicação,

05:50

coletar os outputs, aplico evaluators e salvo ali os scores.

05:55

Depois eu comparo o resultado com a versão anterior

05:59

ou com os limites mínimos que eu defini. Então,

06:02

esse é o fluxo que a gente vai construir aos poucos.

06:05

No nosso projeto, a gente vai começar avaliando o nosso Knowledge Chat.

06:09

Então, primeiro com os casos bem objetivos,

06:11

depois olhando os componentes internos, depois a resposta final,

06:15

e mais para frente, um agente simples para a gente fazer uma triagem.

06:19

A mensagem principal dessa aula, vamos dizer assim,

06:22

é... Avaliação precisa ter arquitetura. Não é uma opinião solta sobre uma resposta.

06:28

É um processo com um dataset.

06:30

Um target, um evaluator, um score, um threshold,

06:33

Baseline e experiment. Beleza? Então, no próximo vídeo,

06:37

A gente vai começar ali com a prática criando o

06:40

Nosso dataset inicial no LangFuse para avaliar o nosso Knowledge Chat.

06:45

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]