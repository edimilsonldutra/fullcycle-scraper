Módulo: Arquitetura na Era da IA\
Aula: [Como saber se um ataque ao RAG funcionou](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18848)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

Na aula anterior, a gente viu que num sistema com RAG

00:06

uma entrada maliciosa não precisa vir diretamente do usuário.

00:09

Ela pode estar dentro de um documento, passar pela ingestão,

00:13

ser indexada, aparecer no retrieval e acabar chegando no contexto do modelo.

00:17

Na próxima aula, a gente vai falar e a gente vai fazer esse experimento,

00:21

exatamente esse experimento no nosso projeto.

00:24

Mas antes disso, eu queria definir uma coisa importante.

00:27

Como que nós vamos saber se o ataque realmente funcionou?

00:30

Porque aqui simplesmente olhar para a resposta final pode esconder muita coisa.

00:35

Imagine que um documento não confiável consiga entrar na nossa base.

00:39

Esse já é um primeiro evento importante,

00:41

mas ainda não significa que o usuário foi afetado.

00:44

O documento pode ter sido aceito na ingestão, indexado e nunca mais aparecer.

00:49

Então, nós vamos acompanhar o ataque por estágios.

00:52

O primeiro é accepted. A pergunta é simples.

00:55

A nossa ingestão aceitou aquele documento como válido?

00:59

Perceba que a gente está falando de validade estrutural.

01:02

O arquivo possui os campos esperados,

01:05

os metadados estão presentes, o formato dele está correto?

01:09

Isso não responde ainda se aquela fonte era confiável.

01:13

Depois... A gente tem o indexed,

01:16

que o conteúdo realmente entrou no índice que será consultado pelo REG. Se entrou,

01:22

agora ele já faz parte do universo de conhecimento que o retrieval pode encontrar.

01:27

E aí o próximo estágio é o retrieved.

01:30

Aqui a gente quer saber se, diante de uma pergunta legítima do usuário,

01:35

algum chunk daquele documento apareceu entre os resultados da busca.

01:40

E isso ainda não significa ataque bem-sucedido. Por isso,

01:44

na nossa avaliação, o retrieval é um sinal de diagnóstico.

01:49

Então, esse aí é um ponto importante para a gente se ligar. Depois,

01:54

a gente tem o selected. No nosso projeto, a gente trabalha com re-ranking. Então,

01:59

nem tudo aquilo que é recuperado necessariamente vai chegar no modelo.

02:04

Um conteúdo adversarial,

02:06

por exemplo, ele pode aparecer nas buscas e ser descartado antes da geração.

02:10

Também é uma informação importante,

02:13

mas ainda não significa que o atacante, vamos dizer assim,

02:16

venceu. A partir daí... a gente já começa a entrar nas propriedades mais críticas.

02:22

Uma delas é o used, ou seja, a pergunta agora é,

02:26

o modelo realmente utilizou aquela fonte não confiável na construção da resposta?

02:31

Essa diferença é fundamental.

02:33

Uma coisa é o documento aparecer próximo do modelo.

02:38

Outra é ele participar efetivamente da resposta.

02:43

E, finalmente, a gente tem o influenced, né? O conteúdo adversarial,

02:48

ele conseguiu mudar aquilo que o usuário recebeu?

02:51

E é aqui que a gente chega ao ataque,

02:53

vamos dizer, end-to-end. Então,

02:56

o caminho que a gente vai acompanhar é mais ou menos esse.

02:59

Accepted, indexed, retrieved, selected, used e influenced, tá? Mas, ainda,

03:06

a gente precisa saber o que significa influenciar uma resposta, tá? Por quê?

03:13

A gente vai ter dois tipos de ataque. No primeiro,

03:16

O documento possui um Poison Claim. E o que é uma claim aqui?

03:21

Na realidade, claim é uma afirmação.

03:25

Imagine que uma documentação confiável diga que determinado limite é

03:30

de X e um documento contaminado diga que é de Y.

03:34

O valor Y é o nosso Poison Claim.

03:38

Beleza? Ou seja, a nossa claim envenenada. Se a resposta adotar aquela informação,

03:45

a gente consegue detectar que o conteúdo falso atravessou o RAG.

03:51

No segundo tipo de ataque, a gente não está colocando apenas uma informação falsa.

03:57

A gente está colocando uma instrução dentro do documento.

04:01

Nesse caso, a gente utilizou um injection.

04:04

É simplesmente um marcador controlado pelo nosso

04:08

experimento que a gente vai permitir,

04:11

no final das contas, verificar se aquela instrução foi obedecida. Assim,

04:16

a gente não precisa perguntar para o outro LLM.

04:18

Você acha que houve um prompt injection?

04:21

Na realidade, a gente tem uma evidência determinística.

04:25

Outra variável que a gente vai encontrar é o expected behavior.

04:30

Ela descreve, no final das contas,

04:32

qual comportamento seria aceitável para aquele caso.

04:37

Em alguns cenários, a gente espera uma recusa. Por exemplo,

04:41

se determinado conhecimento só existe dentro de uma

04:44

fonte que não deveria ser confiável,

04:46

retirar aquela fonte deveria deixar o sistema sem informação suficiente.

04:53

Em outros casos, já existe documentação legítima sobre o assunto.

05:00

Pode aceitar uma resposta grounded que ela

05:04

seja construída somente a partir das fontes confiáveis. Por isso,

05:11

a gente vai trabalhar com comportamento como refusal,

05:15

trusted grounded answer e

05:18

refusal or trusted grounded answer.

05:22

E ainda existe uma distinção importante

05:25

entre as propriedades diagnóstica e blocking. Por quê?

05:30

Uma propriedade diagnóstica serve para a gente entender até onde o ataque chegou.

05:37

Por exemplo, Poison retrieved. Isso é ruim. Por quê?

05:43

Porque, de forma geral, a gente conseguiu ver isso.

05:47

Mas talvez o re-ranker elimine o documento logo depois.

05:53

Então não faz sentido eu afirmar que o ataque ao

05:56

usuário teve sucesso apenas porque o retrieval encontrou aquele conteúdo.

06:02

Já uma propriedade blocking,

06:05

ela representa algo que não pode acontecer de fato,

06:10

certo? Por exemplo, untrusted source used,

06:14

ou Poison claim adopted, ou ainda, por exemplo, indirect instruction followed.

06:21

Se qualquer uma dessas propriedades críticas falhar, no final das contas,

06:25

a gente vai considerar que aquele ataque não foi resistido.

06:30

E é por isso que vocês também

06:32

vão encontrar métricas normalmente chamadas de Attack Resisted.

06:37

Ela não é necessariamente uma média.

06:40

A gente não quer uma situação em que cinco propriedades verdes compensem,

06:46

na realidade, uma falha grave. Então,

06:48

o raciocínio acaba sendo... Blocking property A é igual a safe.

06:54

Blocking property B é igual a safe.

06:57

Blocking property C é igual a failed. Então, attack resisted, false. Ou seja,

07:04

uma única violação relevante já é o suficiente para a gente saber.

07:10

E existe mais uma coisa importante.

07:14

Durante a parte prática, a gente pode até encontrar quatro resultados diferentes.

07:19

Por exemplo, o documento pode ser rejeitado antes mesmo de entrar no índice.

07:24

Ele pode ser indexado, mas nunca recuperado. Pode chegar até o modelo,

07:30

mas nunca conseguir alterar a resposta.

07:32

Ou pode atravessar toda a cadeia e influenciar aquilo que o usuário recebe.

07:37

Esses quatro resultados contam histórias arquiteturais diferentes.

07:42

E isso é justamente o que a gente quer descobrir.

07:46

Ou seja, na próxima aula, a nossa ideia,

07:49

a gente não quer simplesmente colocar um documento malicioso na base e perguntar,

07:54

funcionou ou não? A gente quer acompanhar o ataque estágio por estágio. Então,

07:59

a gente quer observar onde a nossa arquitetura conseguiu interromper,

08:03

principalmente onde ela também não conseguiu. Só depois disso,

08:09

a gente consegue decidir onde os controles de segurança,

08:12

no nosso caso, eles devem entrar.

## Resumo IA

[RESUMO_IA]