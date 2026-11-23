Módulo: Arquitetura na Era da IA\
Aula: [Custos, budgets e governança operacional](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18760)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior, a gente falou sobre categorias de ferramentas de observabilidade, tá?

00:07

Agora... Quando a gente começa a medir tokens,

00:10

modelo, latência, quantidade de chamadas,

00:13

custo e tudo mais,

00:14

a nossa primeira reação vai ser criar dashboards. Isso ajuda muito,

00:20

mas um dashboard sozinho não impede uma aplicação de gastar demais,

00:25

chamar o modelo errado ou permitir que uma feature consuma

00:29

muito mais do que ela deveria no final das contas.

00:33

E é aqui que entra a governança operacional. Então vamos lá,

00:39

a governança operacional é transformar aquilo que

00:42

a arquitetura decidiu em regras executáveis.

00:46

Não é só olhar o que aconteceu depois,

00:48

é definir limites antes,

00:50

acompanhar durante e reagir quando algo sai ali do esperado.

00:55

Em aplicações com IA, o custo precisa ser tratado como parte da arquitetura.

01:00

E isso acontece porque cada decisão técnica pode

01:04

afetar diretamente o valor da requisição.

01:06

Se o aumento do contexto enviado ao modelo,

01:09

o aumento de tokens de entrada, acaba acontecendo tudo isso.

01:14

Se eu deixo o modelo responder, inclusive, sei lá, texto muito longo,

01:18

a gente começa também a ter aumento no token de saída.

01:22

Então, se eu adiciono uma query planner,

01:24

um re-ranking na chamada final, talvez eu tenha, sei lá,

01:27

três chamadas no modelo dentro de uma única interação.

01:30

Se um agente entra em loop, o custo pode crescer sem o usuário perceber.

01:35

Então, a pergunta não é apenas quanto essa chamada custou. Na realidade,

01:41

a pergunta melhor é: essa chamada deveria poder custar isso?

01:46

E essa diferença é importante.

01:49

Por quê? Se eu tenho uma feature simples, como classificar uma mensagem,

01:53

talvez ela não possua, vamos dizer, ela não vai precisar utilizar um modelo caro.

02:00

Se eu tenho uma feature crítica,

02:02

como gerar um relatório importante para um cliente em enterprise,

02:05

talvez um modelo mais caro, nesse caso, faz sentido.

02:08

Se eu tiver um tenant em um plano gratuito, talvez ele tenha um orçamento menor.

02:14

Se eu tenho um cliente corporativo, talvez o orçamento seja maior,

02:18

mas ainda assim precisa de limite. E isso nos leva a budget.

02:24

Budget pode ser por tenant, por usuário, por feature, por modelo ou por período.

02:30

Por exemplo, um tenant pode ter um limite mensal de custo.

02:34

Uma feature pode ter um limite máximo por requisição.

02:38

Um modelo pode ser permitido apenas em certos fluxos.

02:41

Um usuário pode ter limite de chamadas por minuto.

02:45

Uma geração pode ter limite de output de tokens. Então,

02:49

essas regras ajudam a gente a evitar surpresa. Mas o ponto não é só bloquear.

02:54

Às vezes a aplicação pode degradar o comportamento.

02:58

Se o budget está perto do limite, ela pode usar um modelo mais barato.

03:02

Se o contexto está grande demais, ela pode reduzir a quantidade de chunks.

03:07

Se a ferramenta externa está lenta, ela pode retornar uma resposta parcial.

03:12

Se o modelo premium não está autorizado, por exemplo,

03:15

pode cair para um fluxo mais simples.

03:17

Então, isso é chamado de degraded mode. Então,

03:21

ao invés de a aplicação simplesmente falhar,

03:24

ela opera num modo mais limitado, mas controlado.

03:28

O outro ponto é o allow list de modelos. Em uma arquitetura mais madura,

03:34

o código não deve poder chamar qualquer modelo porque alguém mudou uma variável.

03:40

A aplicação pode ter uma política dizendo quais

03:43

são os modelos permitidos para cada feature.

03:46

Por exemplo, o reg de suporte usa um modelo específico,

03:50

a classificação usa outro. Uma análise mais pesada pode usar um terceiro modelo,

03:55

mas apenas para determinados tenants.

03:58

E isso evita que o custo e comportamento virem decisões espalhadas ali no código.

04:05

Também vale pensar em limites por etapa. Em um reg,

04:09

talvez o query planner tenha um custo aceitável,

04:13

o re-rank outro, a geração final no outro. Num agente,

04:17

talvez exista um limite máximo de passos. Numa tool calling,

04:21

talvez a gente tenha um limite de retries. Numa geração de relatório,

04:26

talvez exista um limite de tempo ou necessidade de rodar isso de forma assíncrona.

04:31

Percebe que a governança não é uma planilha financeira.

04:35

Ela é um controle realmente operacional do comportamento da aplicação.

04:39

E é aqui que a observabilidade entra como base.

04:43

Sem telemetria, você não sabe quanto cada feature custa.

04:47

Sem tokens, você não entende consumo. Sem o request ID,

04:51

você não investiga uma execução específica.

04:53

Sem o modelo usado, você não compara o comportamento. E sem tenant e sem feature,

04:59

você não sabe... Quem gerou o custo? Sem traces,

05:02

você não sabe em qual etapa aquele custo apareceu.

05:06

Mas depois de medir, no final das contas, você precisa agir.

05:10

A arquitetura precisa responder perguntas como quando bloquear,

05:15

quando reduzir, quando trocar o modelo, quando exigir aprovação,

05:20

quando registrar um alerta, quando avisar o usuário,

05:23

quando adicionar fallback, quando desligar temporariamente uma feature.

05:27

No nosso projeto, a gente já tem várias informações necessárias para isso.

05:31

Por exemplo, request ID, os modelos,

05:33

os tokens, o tempo, o custo estimado, o tenant, a feature, o uso de re-rank,

05:39

a quantidade de chunks e tudo mais. O próximo passo prático é usar, por exemplo,

05:44

esses sinais para aplicar política simples. A ideia não é criar um sistema,

05:48

por exemplo, de billing completo.

05:50

O objetivo é mostrar o princípio que uma feature de A...

05:55

deve operar dentro de limites específicos. Então,

05:59

essa mensagem principal dessa aula é que a observabilidade mostra o que está acontecendo,

06:04

mas a governança define o que pode acontecer.

06:08

Em sistemas com IA,

06:09

essa diferença é fundamental porque o custo, latência e comportamento

06:13

podem variar muito mais do que uma aplicação tradicional.

06:17

Então, no próximo vídeo, a gente vai seguir nessa linha.

## Resumo IA

[RESUMO_IA]