Módulo: Arquitetura na Era da IA\
Aula: [Fingerprint de prompt e contexto](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18343)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente implementou o primeiro

00:05

cache exato no nosso analisador de tickets.

00:08

A aplicação passou a olhar para o cache antes de chamar IA.

00:11

Se a mesma mensagem aparecesse de novo,

00:13

a resposta vinha do cache e o contador de chamadas para o modelo ali não aumentava.

00:18

E isso já mostrou o primeiro ganho e agora a gente

00:21

precisa corrigir uma simplificação que a gente fez de propósito. Até agora,

00:25

a chave de cache está muito dependente da mensagem do usuário.

00:30

A gente normaliza o texto,

00:32

gera uma chave e usa aquilo para decidir se a resposta pode ser reaproveitada.

00:36

Para a primeira versão, tudo bem. Mas em uma aplicação real,

00:40

a resposta da IA não depende só da mensagem.

00:43

Ela depende do prompt utilizado, depende das regras de classificação,

00:48

depende do modelo ou pelo menos da capacidade do modelo que você escolheu usar.

00:54

E pode depender de qualquer contexto relevante que entrou naquela chamada.

00:58

Então, quando a gente fala em fingerprint, a ideia é justamente essa,

01:03

criar uma assinatura do contexto que gerou aquela resposta.

01:08

Não é só perguntar, essa mensagem já apareceu antes? A pergunta melhor é,

01:13

essa mensagem já apareceu antes dentro do mesmo contexto de execução?

01:18

Vamos voltar para o nosso analisador de ticket. Imagine que hoje...

01:22

o prompt classifique o ticket em billing,

01:25

technical support, account, cancellation e order.

01:29

A aplicação chama o modelo e classifica a mensagem e salva no cache.

01:34

Agora imagina que amanhã eu melhoro o prompt.

01:36

Talvez eu deixe mais claro quando algo deve ser

01:40

billing e quando algo deve ser cancellation.

01:43

Ou talvez eu mude uma regra e digo que pedidos

01:46

de reembolso não devem mais cair como cobrança,

01:50

mas em algum outro tipo de atendimento.

01:52

A mensagem do usuário pode ser exatamente a mesma,

01:56

mas o comportamento esperado da aplicação mudou.

01:59

Se a chave de cache só usa o texto normalizado,

02:03

a aplicação pode continuar retornando uma resposta antiga,

02:08

criada com uma versão anterior do prompt.

02:12

Tecnicamente, o cache funcionou, arquiteturalmente, ele errou. Por isso,

02:16

a gente começa a colocar versão nova na chave, algo como...

02:21

Uma cache key é igual a um hash que tem um

02:24

prompt version mais rules version

02:27

mais model capability mais normalized text.

02:33

Então, o prompt version representa a versão do prompt que gerou a resposta.

02:39

O rules version representa a versão das regras que a aplicação está utilizando.

02:44

O model capability representa o tipo de modelo ou capacidade esperada. naquele fluxo.

02:51

E o normalized text continua sendo a entrada do usuário num formato previsível.

02:57

Com isso, se eu mudar o prompt, a chave muda. Se eu mudar a regra, a chave vai mudar.

03:03

Se eu decidir que aquele fluxo agora precisa de outro tipo de modelo,

03:06

a chave também vai mudar. E esse é um detalhe importante.

03:11

O fingerprint não é só gerar uma string bonita.

03:15

Ele é uma forma de evitar que a aplicação

03:17

misture respostas que parecem iguais por fora,

03:21

Mas que foram produzidas em condições diferentes.

03:25

Também não precisa complicar demais. Nessa etapa,

03:28

a gente não vai criar um sistema sofisticado de versionamento de prompt.

03:32

Vamos apenas deixar essas versões mais explícitas

03:35

no código para mostrar o princípio.

03:37

Algo como prompt v1, rules v1 e fastmod.

03:41

Depois, quando... uma dessas partes mudar,

03:45

a própria chave do cache tem que mudar naturalmente.

03:48

Isso torna a invalidação mais previsível,

03:51

em vez de precisar apagar

03:53

manualmente tudo que o prompt muda,

03:59

você simplesmente vai lá e muda a versão. O cache antigo continua armazenado,

04:05

mas deixa de ser usado por aquele fluxo novo.

04:08

Essa é uma diferença importante entre cache, vamos dizer,

04:11

ingênuo e cache pensado para aplicação com IA. O cache mais ingênuo,

04:16

ele olha só para a entrada. O cache com fingerprint,

04:19

ele olha para a entrada e para o contexto que dá significado à resposta.

04:24

No próximo vídeo prático, a gente vai evoluir o projeto para fazer exatamente isso.

04:29

Sair de uma chave baseada só na mensagem normalizada

04:32

e passar a gerar a chave considerando,

04:35

Prompt Version, Rules Version e Model Capability e o texto normalizado.

04:41

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]