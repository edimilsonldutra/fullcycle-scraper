Módulo: Arquitetura na Era da IA\
Aula: [Evaluation de tool calling e agentes simples](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18798)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente comparou versões do

00:04

nosso Knowledge Chat usando o Experiment.

00:07

A ideia foi sair de uma avaliação isolada e começar a pensar em Baseline,

00:11

Regressão, Comparação entre Variações do Pipeline.

00:15

Agora a gente vai abrir um novo bloco aqui,

00:17

que vai ser o Evaluation de Tool. Calling e agentes mais simples aqui, tá?

00:23

Até aqui, a maior parte dos nossos exemplos,

00:26

ele ficou em cima do Knowledge Chat com o Reg. Isso fez sentido,

00:30

porque o projeto já tinha várias partes boas para avaliar. O query planner,

00:36

o retrieval, o re -ranking, a resposta final, as fontes,

00:40

a recusa e a comparação entre versões. Mas sistemas com IA,

00:43

eles não são baseados em reg, eles não param aí. Em muitas aplicações,

00:49

o modelo não apenas responde, ele também escolhe uma ferramenta, chama uma API,

00:54

consulta um sistema, cria um ticket, busca dados transacionais,

00:58

dispara um workflow ou continua executando vários passos até a concluir uma tarefa.

01:04

Quando isso acontece,

01:06

a evaluation muda, porque agora não basta mais avaliar só a resposta final.

01:11

A gente precisa também avaliar o caminho que o sistema tomou.

01:17

Imagine um usuário dizendo,

01:18

abra um chamado P1 porque o painel está fora do ar para todos os usuários.

01:23

Se o sistema responde um texto bonito explicando o que é P1,

01:26

mas não abre o chamado, ele falhou. Então,

01:29

a resposta pode estar até correta do ponto de vista textual,

01:33

mas a tarefa não foi concluída.

01:35

Agora, imagine outro cenário. O sistema abriu um chamado,

01:38

mas classifica como P3. Então, ele executou a ferramenta certa,

01:42

mas com o argumento errado. Então, ele também falhou. Outro caso,

01:47

o sistema chama uma ferramenta de uso atual da

01:51

conta para uma pergunta que era apenas sobre documentação.

01:55

Então, a resposta final pode até ficar aceitável,

01:58

mas ele chamou uma ferramenta desnecessária, gerou custo,

02:02

aumentou a latência e talvez acessou um sistema que não precisava acessar.

02:06

E é por isso que Tool Calling e

02:08

Agentes Evaluation precisa olhar para mais dimensões.

02:13

A primeira é a Tool Selection. O sistema escolheu a ferramenta certa?

02:19

Se a pergunta é sobre uma política interna,

02:22

Talvez a ferramenta correta seja buscar na base de conhecimento.

02:25

Se a pergunta é sobre o consumo atual,

02:28

talvez a ferramenta correta seja consultar uma API de uso.

02:31

Se a pergunta pede uma abertura de um chamado,

02:34

talvez a ferramenta correta seja criar um ticket.

02:37

A segunda dimensão é o argument correctness.

02:41

Os argumentos enviados para ferramentas estavam corretos?

02:45

Não basta chamar somente um create, underline, support,

02:49

underline, ticket. A severidade precisa estar certa.

02:53

Então, o resumo precisa fazer sentido.

02:57

O tenant precisa estar correto.

02:59

O sistema não deveria preencher campos importantes como suposição.

03:04

A terceira dimensão é o task success. A tarefa foi concluída,

03:08

Às vezes o caminho não precisa ser exatamente o igual esperado,

03:13

mas o resultado precisa cumprir o objetivo do usuário. Em outros casos,

03:17

principalmente em fluxos críticos, o caminho também importa.

03:22

E é aqui que entra a ideia de trajetória.

03:26

Trajetória é a sequência de passos que o agente executou.

03:30

Por exemplo... Primeiro consultou a base de conhecimento,

03:33

depois abriu um ticket, depois respondeu o usuário.

03:37

Ou então chamou uma ferramenta de uso,

03:39

recebeu os dados e explicou o resultado.

03:42

Avaliar a trajetória ou *trajectory* é diferente de avaliar só o output.

03:48

A gente já começa a perguntar, as ferramentas esperadas foram chamadas?

03:52

Foram chamadas na ordem certa? Alguma ferramenta proibida foi usada?

03:58

O agente repetiu passos, ele entrou em um loop,

04:01

ele respeitou o limite máximo de interações,

04:05

ele pediu esclarecimento quando estava faltando informação.

04:09

Isso é extremamente importante em agentes.

04:12

Um agente pode chegar a uma resposta final razoável,

04:16

mas com uma trajetória ruim. Então pode dar passos demais.

04:21

Pode chamar a ferramenta errada e se recuperar depois,

04:23

pode consultar dados que não precisava,

04:25

pode executar uma ação sem confirmação e pode

04:28

gastar muito para resolver algo simples.

04:30

Então, a avaliação de agentes precisa combinar várias visões. Então,

04:35

a resposta final ainda importa, mas também importam as ferramentas chamadas,

04:40

os argumentos usados, a ordem dos passos, o número de iterações,

04:44

os limites operacionais e a conclusão da tarefa. Então, nesse nosso módulo,

04:49

a gente não vai criar, vamos dizer, uma disciplina inteira de agentes aqui.

04:54

Não é o nosso objetivo. Isso vai ser assunto de outro momento. Agora,

04:57

o objetivo agora é mostrar a diferença de avaliação. Por isso,

05:03

vamos criar um mini projeto bem controlado. Um agente simples de triagem de suporte.

05:08

Ele vai ter poucas ferramentas. Uma para buscar na base de conhecimento,

05:12

uma para consultar o uso atual fictício e outra para criar um ticket de suporte.

05:18

Com isso, a gente consegue avaliar casos simples, mas muito reais.

05:22

Por exemplo, a pergunta sobre SLA deveria usar a base de conhecimento.

05:27

Uma pergunta sobre consumo atual deveria usar uma ferramenta de uso.

05:33

Um pedido claro de abertura de chamado deveria criar um ticket.

05:38

Um pedido ambíguo devia pedir esclarecimento.

05:41

E o dataset de avaliação desse agente não vai ter só a pergunta esperada.

05:46

Ele vai ter também as expectativas como ferramentas esperadas,

05:50

ferramentas proibidas, argumentos esperados,

05:53

o máximo... a contagem de passos e se o agente deveria pedir esclarecimento.

05:59

E essa é a virada de chave. Quando a IA só responde,

06:03

a gente avalia principalmente a resposta. Quando a IA usa ferramentas,

06:07

a gente avalia a decisão e execução.

06:09

Quando a IA vira agente, a gente avalia a trajetória. Então,

06:15

guarda essa ideia. Em sistemas com tool calling e agentes,

06:18

qualidade não está apenas no texto final.

06:20

A qualidade está no comportamento do sistema durante a execução.

## Resumo IA

[RESUMO_IA]