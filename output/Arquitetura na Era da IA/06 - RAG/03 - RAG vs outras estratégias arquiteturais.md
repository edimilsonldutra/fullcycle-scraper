Módulo: Arquitetura na Era da IA\
Aula: [RAG vs outras estratégias arquiteturais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=19128)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente falou sobre o que o Reg não resolve.

00:05

A gente viu que o Reg não substitui banco de dados, não substitui API,

00:09

não executa ações no sistema e também não deve ser usado só porque parece moderno.

00:14

Agora a gente vai dar um próximo passo,

00:17

comparar o Reg com outras estratégias que podem aparecer

00:20

na arquitetura de uma aplicação com IA.

00:22

E aqui tem uma pergunta que ajuda muito.

00:25

Onde está a informação que eu preciso usar para responder ou agir?

00:30

Dependendo da resposta, a solução muda.

00:33

Se a informação está em documentos, políticas,

00:37

packs, manuais, contratos, páginas internas ou bases de conhecimento,

00:41

REG começa a fazer sentido porque a ideia é recuperar trechos

00:45

relevantes dessa base e entregar o contexto para o modelo responder.

00:49

Mas se a informação está numa tabela em um sistema transacional ou está numa API,

00:54

talvez o REG seja o caminho errado. Por exemplo,

00:57

se eu quero saber quantos alunos estão ativos num sistema na minha turma,

01:00

isso não é um problema de REG, é uma consulta de banco,

01:03

API ou algum serviço interno. A IA pode ajudar a explicar o resultado depois,

01:09

mas a origem da informação precisa vir no sistema correto. Então,

01:13

uma comparação importante é REG versus SQL e API.

01:17

SQL e API,

01:19

são melhores quando a resposta depende de dado estruturado,

01:25

estado atual ou informação transacional.

01:27

Reg é melhor quando a resposta depende de conhecimento textual espalhado

01:33

em documentos e difícil de consultar apenas com uma query tradicional.

01:37

Agora, existe um outro caminho que ganhou força com modelos de contexto maior.

01:42

Simplesmente colocar muita informação direto no prompt.

01:46

Isso pode funcionar muito bem quando a base é pequena.

01:50

Se você tem um documento de duas páginas,

01:52

um contrato curto, uma política simples ou um conjunto pequeno de regras,

01:57

talvez você não precise montar um Reg completo.

01:59

Você pode colocar aquele conteúdo no contexto e pedir

02:03

para o modelo responder com base nele.

02:05

Isso é mais simples,

02:07

menos componentes, menos índices, menos pipelines, menos moving parts.

02:12

Mas tem um limite. Quando a base cresce,

02:14

quando os documentos mudam com frequência, quando existem permissões diferentes,

02:18

quando você precisa buscar só uma parte específica,

02:21

quando você precisa citar fonte, quando precisa controlar custo, latência,

02:26

mandar tudo para um prompt começa a ficar pesado.

02:29

Você aumenta input tokens, aumenta custo,

02:31

aumenta latência e ainda pode colocar contexto demais para o modelo processar. Então,

02:36

long context não elimina RAG.

02:40

Ele reduz alguns casos onde antes a gente talvez precisasse de Reg.

02:45

Mas quando a base é grande,

02:47

a dinâmica precisa de recuperação seletiva. Reg continua fazendo sentido.

02:52

Outra comparação é Reg versus cache.

02:56

Cache entra quando eu quero reaproveitar... que algo já foi calculado,

03:02

buscado ou respondido. Se várias pessoas fazem a mesma pergunta,

03:07

Onde uma mesma consulta gera sempre o mesmo resultado,

03:11

talvez eu consiga reutilizar a resposta ou parte do processamento.

03:16

Reg é diferente. Reg não existe principalmente para reaproveitar respostas.

03:22

Ele existe para recuperar contexto relevante antes da geração.

03:28

Em muitos sistemas, inclusive, os dois aparecem juntos.

03:32

O Reg busca o contexto e o cache evita repetir as

03:37

etapas quando a mesma pergunta ou o mesmo contexto aparece de novo.

03:43

Então, o cache não substitui o Reg,

03:45

mas às vezes o cache evita que você precise acionar o Reg em toda requisição.

03:52

E agora tem o Fine Tuning. Fine Tuning é um outro tipo de solução.

03:58

Ele não serve para colocar uma base de conhecimento

04:01

inteira dentro do modelo toda vez que o documento muda.

04:06

Fine Tuning faz mais sentido quando você quer ajustar comportamento,

04:10

estilo, formato de resposta ou padrões muito específicos. Por exemplo,

04:15

responder sempre em um determinado formato,

04:18

classificar algo de uma forma específica,

04:20

seguir uma estrutura de saída ou adaptar um

04:23

modelo a um determinado tipo de tarefa extremamente específica.

04:28

Se o problema é conhecimento que muda toda semana, Reg normalmente é mais adequado.

04:34

Se o problema é comportamento repetitivo, formato ou especialização em uma tarefa,

04:41

Fine Tuning pode fazer mais sentido.

04:44

E temos também Tool Calling.

04:46

Tool Calling entra quando a aplicação precisa usar ferramentas. Consultar uma API,

04:53

buscar um pedido, criar um ticket, cancelar uma assinatura,

04:57

atualizar um cadastro, chamar um serviço externo.

05:00

Nesse caso, o modelo não deve inventar a resposta.

05:04

Ele deve chamar uma ferramenta certa,

05:06

receber o resultado e, então, ajudar a explicar ou conduzir o fluxo.

05:11

Então, a decisão fica mais clara.

05:14

Se eu preciso recuperar conhecimento textual, eu penso em Reg.

05:17

Se eu preciso consultar o estado atual... penso em banco de dados ou API.

05:21

Se eu penso em executar numa ação,

05:23

eu penso normalmente numa Tool Calling ou num workflow.

05:26

Se eu preciso reaproveitar a resposta, eu penso em cache.

05:30

Se a base cabe inteira no contexto,

05:32

talvez long context seja suficiente. Se eu preciso mudar o comportamento do modelo,

05:38

talvez Fine Tuning entre na conversa.

05:42

O papel do arquiteto não é escolher a tecnologia mais famosa,

05:46

é entender a natureza do problema.

05:48

O Reggae é uma peça importante,

05:50

mas ele entra melhor quando existe uma base de conhecimento externa,

05:55

textual, atualizável e que precisa ser recuperada.

05:58

Aí no próximo vídeo a gente vai apresentar um projeto desse

06:02

capítulo e aí a gente vai avançando em relação a tudo isso. Vamos nessa!

## Resumo IA

[RESUMO_IA]