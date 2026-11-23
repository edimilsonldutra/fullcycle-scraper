Módulo: Arquitetura na Era da IA\
Aula: [Por que teste tradicional não basta](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18780)

## Resumo da aula



## Transcrição

00:02

Olá pessoal, tudo bem?

00:03

Agora a gente vai começar um novo módulo dentro dessa nossa disciplina, tá?

00:08

E o grande ponto aqui é que eu quero começar com uma ideia bem importante.

00:15

Teste tradicional continua sendo necessário. Ele não morreu.

00:19

Ele não ficou ultrapassado, ele não deixou de ser importante,

00:23

só porque agora a gente tem modelos de linguagem dentro das nossas aplicações.

00:28

Na verdade, em muitos casos, ele ficou até mais importante,

00:32

só que ele não é mais suficiente sozinho.

00:35

Quando a gente trabalha com software tradicional,

00:38

normalmente a gente tem uma expectativa muito clara.

00:41

Eu passo uma entrada, executo uma função,

00:43

recebo uma saída e valido se aquela saída bate com o esperado.

00:48

Se eu estou testando uma regra de desconto,

00:51

eu sei exatamente qual o valor que deveria voltar.

00:53

Se eu estou testando uma API, eu sei o status code, eu sei o esquema do JSON,

00:57

os campos obrigatórios, os cenários de erro. Se eu estou testando uma função pura,

01:02

eu espero sempre o mesmo resultado para a mesma entrada.

01:06

E esse tipo de teste é fundamental.

01:08

Só que quando a gente coloca IA no meio...

01:11

principalmente LLMs, a natureza do problema muda.

01:16

A mesma pergunta pode gerar respostas diferentes. Uma resposta pode estar correta,

01:23

mesmo usando palavras diferentes. A outra pode estar muito bem escrita, mas errada.

01:28

Uma resposta pode seguir o formato esperado, mas usar uma fonte ruim.

01:32

Uma outra pode responder parcialmente.

01:35

A outra pode inventar um detalhe que parece plausível.

01:38

E a outra pode se recusar.

01:40

corretamente a responder porque não havia contexto suficiente.

01:44

Então o problema deixa de ser apenas a saída é exatamente igual ao

01:49

que eu estou esperando e passa a ser também a resposta faz sentido?

01:53

Está baseada no contexto correto? Ela cumpre a intenção do usuário?

01:57

Ela respeita o contrato da aplicação? Ela usa as fontes certas?

02:01

Ela deveria ter respondido ou deveria ter recusado?

02:05

Ela chamou a ferramenta correta? Ela seguiu para o caminho esperado?

02:09

Então é aqui que entra o conceito de evaluation ou evals.

02:14

Quando a gente fala de evaluation em sistemas de IA,

02:18

a gente está falando de uma forma mais ampla de medir comportamento.

02:22

Não é só verificar se uma função retorna true ou false.

02:26

É criar um processo para avaliar se o sistema

02:29

está se comportando do jeito esperado em diferentes cenários.

02:34

E isso pode envolver várias camadas.

02:36

Em uma aplicação simples com IA,

02:38

talvez a gente queira avaliar se o modelo classificou uma mensagem corretamente,

02:42

se ele retornou um... são válidos,

02:44

se ele respeitou o formato combinado e se não saiu do escopo.

02:48

Num sistema com RAG, como um Knowledge Chat, por exemplo, que a gente construiu,

02:53

a gente precisa avaliar se o sistema recuperou os documentos certos,

02:56

se ele selecionou os chunks corretos,

02:58

se ele respondeu com base no contexto e se citou as fontes adequadas.

03:02

Num sistema com Tool Calling,

03:04

a gente precisa avaliar se o modelo escolheu a ferramenta certa,

03:07

Se ele passou os argumentos corretos e se ele lidou bem com o retorno da ferramenta.

03:12

E em um agente, no caso, a gente precisa olhar também para a trajetória.

03:18

Quais são os passos que ele tomou? Quais são as ferramentas que ele chamou?

03:22

Se ele entrou num loop, se ele parou no momento certo,

03:25

se ele cumpriu a tarefa sem sair dos limites.

03:28

Então percebe que agora a qualidade não é só na resposta final.

03:33

Ele está... no caminho, no final das contas.

03:36

Isso é uma mudança grande para quem vem de,

03:40

vamos dizer assim, de uma forma de um teste tradicional, porque no mundo da IA,

03:46

muitas vezes a gente não consegue validar a qualidade

03:49

apenas com um acerto exato ali do texto.

03:52

A gente precisa validar contrato, comportamento e resultado.

03:56

Por isso, nesse módulo, a gente vai separar bem as coisas. Primeiro,

04:01

a gente vai continuar valorizando os testes determinísticos.

04:04

Eles ainda validam esquema, status,

04:08

campos obrigatórios, fontes, flags, como, por exemplo, has answer,

04:12

erros controlados, limites e contratos da API.

04:16

Isso é a base. Antes de perguntar se a resposta é boa,

04:20

a aplicação precisa, pelo menos, devolver uma resposta no formato correto. Depois,

04:26

a gente vai entrar em avaliação. Aí a gente começa a falar de dataset,

04:31

casos de teste, métricas, scores, baselines, comparação entre inversões,

04:37

regressão e também LLM como juiz.

04:41

Também a gente vai utilizar já o projeto que a gente já construiu,

04:46

o nosso Knowledge Chat.

04:47

Ele vai virar um primeiro alvo de avaliação.

04:50

A gente vai criar casos para avaliar. Perguntas conhecidas,

04:56

perguntas ambíguas, perguntas sem resposta na base,

05:00

perguntas com termos exatos e cenários onde a fonte correta importa.

05:06

E mais para frente,

05:07

a gente também vai criar um agente simples de triagem de suporte,

05:11

não para ensinar agentes de profundidade agora,

05:14

mas para mostrar algo que RAG sozinho não mostra bem,

05:18

que é avaliação de ferramentas, argumentos e trajetória. Então,

05:22

a mensagem principal dessa aula é, em sistemas com IA,

05:26

testar continua sendo necessário, mas avaliar... passa a ser ali indispensável.

05:32

O teste tradicional valida os contratos de forma objetiva. A avaliação,

05:37

ela mede comportamento. E a qualidade nasce da combinação dos dois.

05:42

Então, se você só testa o contrato,

05:44

pode deixar uma resposta ruim passar. Se você só faz avaliação subjetiva,

05:48

pode deixar a aplicação quebrar com coisas básicas. Então, a arquitetura...

05:53

Nesse caso, ela precisa estar dos dois lados. Então, no próximo vídeo,

05:57

a gente vai entender a arquitetura de uma, vamos dizer assim,

06:01

uma avaliação e a gente vai organizar os principais conceitos.

06:05

Dataset, Target, Evaluator, Score,

06:08

Threshold, Baseline e Experiment.

06:11

Isso vai dar uma base bacana para a gente

06:14

começar a construir as nossas avaliações aí na prática. Vamos nessa!

## Resumo IA

[RESUMO_IA]