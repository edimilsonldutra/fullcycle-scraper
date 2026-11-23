Módulo: Arquitetura na Era da IA\
Aula: [Operação de agentes e tool calling](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18762)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior, a gente saiu da observabilidade passiva

00:05

e a gente começou a aplicar governança operacional,

00:09

ou seja, a gente não fica mais apenas olhando tokens,

00:12

custo, modelo e latência, e a gente começa a transformar esses sinais em políticas,

00:17

ou seja, modelo permitido, limite de saída, budget por tenant,

00:21

budget por feature, bloqueio controlado e...

00:25

Quando qualquer coisa acontece que a gente consegue

00:27

fazer bloqueios quando alguma regra é violada,

00:30

né? Agora,

00:31

eu quero ampliar um pouquinho mais essa conversa para

00:34

um outro tipo de arquitetura com IA,

00:36

tá? Que são aplicações com tool calling e agentes. Por quê? Até aqui,

00:43

o nosso laboratório principal foi um de RAG, certo?

00:46

E isso fez sentido porque RAG tem várias etapas observáveis,

00:50

como query planner, retrieval, re-ranking, a geração,

00:54

fontes, recusa e tudo mais. Só que a mesma lógica,

00:58

ela vale para outros sistemas com IA.

01:01

Então, quando a aplicação usa tool calling, por exemplo,

01:05

a LLM não está apenas respondendo a um texto.

01:08

Ela pode decidir em chamar uma ferramenta.

01:11

Essa ferramenta pode consultar uma API, buscar um pedido, abrir um ticket, consultar um banco,

01:17

disparar um workflow ou executar alguma ação controlada ali pelo sistema.

01:21

Então, a observabilidade precisa mostrar mais do que a chamada de um modelo.

01:27

Ela precisa mostrar qual ferramenta foi chamada,

01:29

quanto tempo essa chamada para essas ferramentas acabou demorando,

01:34

se ela respondeu com sucesso, se deu timeout, se houve algum retry,

01:38

se o payload era grande demais, se a resposta...

01:40

da ferramenta foi usada na resposta final e se aquela

01:43

ferramenta realmente deveria ter sido chamada naquele contexto.

01:47

E isso é importante porque quando uma tool calling

01:51

no final das contas acaba dando errado,

01:53

o problema pode estar em lugares diferentes. Ele pode estar, por exemplo,

01:58

no modelo que você escolheu, a ferramenta errada,

02:02

pode estar no esquema da ferramenta,

02:04

pode estar na API que foi chamada, pode estar na parte de permissão,

02:08

na parte que está da timeout para a gente,

02:11

ou até mesmo no retorno das informações que são trazidas ali pela ferramenta. Então,

02:17

cada vez essas coisas começam a ficar mais complicadas e sem trace,

02:22

tudo isso aí vira novamente aquela caixa preta que a gente falou.

02:26

E em agentes, esse problema, ele cresce ainda mais.

02:30

Por quê? Porque um agente normalmente não executa apenas uma etapa.

02:35

Ele pode planejar,

02:36

chamar a ferramenta, observar o resultado,

02:39

decidir o próximo passo, chamar outra ferramenta,

02:42

revisar o estado e continuar até chegar numa resposta ou numa ação final. Então,

02:48

para operar agentes, a gente precisa observar também o quê? O loop.

02:54

Quantos passos o agente executou?

02:56

Quais foram as ferramentas chamadas? Alguma ferramenta falhou?

02:59

Houve retry? O agente repetiu a mesma ação várias vezes?

03:02

Ele parou por alguma condição clara ou apenas atingiu um limite?

03:07

O custo total ficou concentrado em qual etapa?

03:10

A maior latência veio do modelo ou das ferramentas externas?

03:14

Essas perguntas são arquiteturais, porque um agente sem limite pode entrar num loop,

03:19

um agente sem observabilidade pode gastar muito sem ninguém perceber,

03:23

e um agente sem rastreabilidade pode tomar decisões

03:26

difíceis de a gente conseguir explicar. Então,

03:29

isso aí acaba impactando completamente as coisas. Então,

03:34

aqui entra uma separação muito importante.

03:37

Observar a gente não significa

03:40

registrar raciocínio interno sensível do modelo.

03:45

A gente não precisa e muitas vezes a gente não deve...

03:49

Tentar capturar tudo que parece, vamos dizer assim, pensamento do modelo.

03:53

O que a gente precisa capturar são os eventos operacionais.

03:57

Etapa iniciada, ferramenta escolhida, ferramenta executada,

04:00

tempo de execução, erro, retry, status,

04:04

número de passos, custo acumulado, condição de parada e o resultado final.

04:08

Ou seja, não é sobre expor a cadeia de pensamento.

04:12

É sobre auditar o comportamento do sistema.

04:16

Se a aplicação tem um agente que chama ferramentas,

04:19

os spans podem representar algo como agent.run,

04:24

agent.step, tool.call,

04:27

tool.result e model.call. Cada um desses spans pode carregar atributos seguros,

04:34

como o nome da ferramenta, duração, status, o número da tentativa,

04:38

o tipo de erro, tokens usados e o custo estimado.

04:42

Então, a governança também precisa entrar aqui.

04:47

Então, você pode ter um limite máximo de passos por execução,

04:50

um limite de retries por ferramenta, um timeout por tool call,

04:54

um allow list de ferramentas por feature.

04:58

Ferramentas que só podem rodar em determinados tenants,

05:01

ferramentas que exigem confirmação humana antes de executar uma ação irreversível.

05:06

Então, quando a gente fala de observabilidade em agentes,

05:09

a ideia não é apenas ver o que aconteceu,

05:12

é também garantir que o agente opere dentro de limites para a gente muito claros.

05:18

E esse é o ponto que conecta tudo que a gente está vendo nesse módulo.

05:22

A observabilidade mostra o caminho,

05:24

a governança define os limites e a arquitetura precisa garantir que essas duas

05:30

coisas estejam presentes antes de colocar um fluxo de IA ali em produção.

05:35

E no nosso projeto a gente usou um reg como laboratório.

05:39

Mas numa aplicação com tool calling ou agentes,

05:42

você deve aplicar o mesmo raciocínio. Criar traces para os fluxos,

05:45

spans para as etapas importantes, os atributos seguros para a investigação,

05:50

as métricas de custo e latência,

05:52

a política para impedir o comportamento fora do esperado.

05:55

Então, a mensagem principal dessa aula é...

05:58

Quanto mais autonomia a IA ganha dentro da aplicação, mais observável e,

06:04

entre aspas, governado o fluxo ele precisa ser. Fechou? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]