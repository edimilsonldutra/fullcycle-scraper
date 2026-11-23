Módulo: Arquitetura na Era da IA\
Aula: [Expondo capacidades, não modelos físicos](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18295)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

Agora que a gente viu o Lite LLM Proxy funcionando de forma simples,

00:06

a próxima pergunta não é mais se conseguimos colocar uma camada no meio.

00:12

Isso a gente já entendeu.

00:13

A pergunta agora é, o que a aplicação deveria pedir para essa camada?

00:18

Porque existe um erro bem comum aqui.

00:20

A pessoa coloca um gateway no meio,

00:22

mas continua fazendo a aplicação pensar exatamente do mesmo jeito.

00:27

Antes ela chamava diretamente um modelo físico, agora ela chama o proxy,

00:31

mas continua passando o nome físico do modelo,

00:34

o provedor específico e todos os detalhes da execução.

00:37

Nesse caso, você só mudou a topologia, mas não mudou tanto a abstração.

00:42

A aplicação, ela continua pensando em modelo,

00:44

não em capacidade.

00:46

E nas primeiras evoluções que uma gateway técnica acaba permitindo

00:51

é justamente criar um vocabulário interno para o uso da IA.

00:55

Em vez da... aplicação chamar diretamente um modelo específico,

00:59

ela pode chamar algo mais próximo da intenção daquele fluxo.

01:03

Por exemplo, classificador simples,

01:06

resposta suporte, extração de documento,

01:10

análise profunda, embedding padrão. Esses nomes,

01:14

eles não precisam ser os nomes reais dos modelos dos provedores.

01:17

Eles são nomes internos da arquitetura.

01:20

E isso muda bastante a forma de evoluir o sistema.

01:23

Se amanhã você percebe que a classificação simples pode usar um modelo mais barato,

01:27

você pode trocar isso na configuração da camada.

01:30

Se percebe que a extração de um documento precisa de um modelo mais forte,

01:34

você ajusta o mapeamento daquela capacidade.

01:37

Se um provedor começa a ficar caro ou instável,

01:40

você pode mudar a implementação por trás daquilo.

01:42

Então, a aplicação não precisa necessariamente saber mais de tudo isso.

01:48

Ela só precisa saber que existe uma capacidade chamada,

01:51

por exemplo, classificador simples, só que aqui tem um cuidado importante.

01:57

Não adianta também criar nomes genéricos demais,

02:00

como modelo 1, modelo 2, modelo rápido,

02:02

sem ninguém entender o que significa.

02:04

O ideal é que o nome represente o uso esperado.

02:07

Se é para classificação, deixe claro isso aí. Se é para resposta ao usuário,

02:12

deixe isso mais claro. Se for para análise mais pesada,

02:15

então é importante que todo mundo tenha clareza em relação a esses nomes,

02:20

porque senão a gente começa a perder o controle e essa camada...

02:26

começa também a virar parte do design da aplicação.

02:31

A aplicação passa a depender de capacidades internas

02:34

da IA e não de provedores externos diretamente.

02:40

Então, esse é um salto ali que é bem pequeno no código,

02:44

mas é importante na arquitetura. Então,

02:47

a mensagem desse vídeo que eu deixaria aqui é,

02:49

depois que existe um gateway ali na sua frente,

02:52

a próxima evolução é parar de expor o modelo físico

02:56

para todo mundo e começar a expor as capacidades internas.

03:00

A aplicação não deveria ficar perguntando qual modelo eu chamo,

03:04

Ela deveria perguntar qual capacidade eu preciso usar.

03:08

E aí, no próximo vídeo, a gente vai olhar para outra decisão que aparece logo depois.

03:14

Quem pode usar cada uma dessas capacidades?

03:20

Quanto que isso pode custar e quais os limites que precisam existir.

## Resumo IA

[RESUMO_IA]