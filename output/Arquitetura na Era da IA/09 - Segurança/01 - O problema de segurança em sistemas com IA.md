Módulo: Arquitetura na Era da IA\
Aula: [O problema de segurança em sistemas com IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18839)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Agora a gente vai começar um novo módulo dentro dessa nossa disciplina,

00:06

tá? E a gente vai falar sobre segurança, guardrails e riscos em sistemas com IA.

00:12

E eu quero começar com uma mudança importante de perspectiva.

00:16

Quando a gente coloca um modelo de linguagem dentro de uma aplicação,

00:20

a gente não está simplesmente adicionando mais uma API ao sistema.

00:23

A gente está adicionando um componente que interpreta o conteúdo,

00:27

toma decisões probabilísticas e pode influenciar o que

00:30

outras partes da aplicação vão fazer.

00:32

Numa aplicação tradicional,

00:34

uma entrada normalmente passa por regras relativamente claras.

00:37

O sistema recebe dados, valida o formato,

00:40

verifica a autorização, executa uma operação conhecida e devolve um resultado.

00:45

Numa aplicação com IA, o caminho pode ser bem diferente.

00:48

O usuário envia uma mensagem, um modelo interpreta essa mensagem,

00:51

um query planner pode decidir quais documentos procurar.

00:54

Um sistema de RAG recupera contexto,

00:57

o outro modelo pode selecionar os trechos mais relevantes.

01:00

A resposta pode ser enviada para o usuário e utilizada

01:03

também por outras aplicações ou transformada em uma chamada de ferramenta.

01:09

Num caso de um agente,

01:10

esse fluxo pode ir ainda mais longe. O modelo pode consultar dados,

01:15

criar um ticket, enviar uma solicitação,

01:17

atualizar um registro ou iniciar outra operação.

01:20

Perceba que agora o texto não é apenas informação,

01:24

o texto também pode influenciar nas decisões.

01:27

E essa é uma das mudanças centrais de segurança nos sistemas com IA.

01:32

Uma frase enviada pelo usuário pode tentar alterar o comportamento do modelo.

01:36

Um documento recuperado pelo RAG pode conter instruções maliciosas.

01:41

Uma resposta de ferramenta pode trazer conteúdo que

01:44

influencia o próximo passo do agente.

01:46

Uma saída aparentemente válida pode carregar um valor perigoso para outro sistema. Por isso,

01:52

segurança em aplicações com IA não significa apenas proteger a

01:56

chave de API ou impedir um acesso a um endpoint.

02:01

Nós precisamos proteger o fluxo inteiro.

02:05

Precisamos olhar para a entrada do usuário,

02:08

para os prompts, para o contexto recuperado,

02:10

para os documentos indexados, para o modelo, para a resposta,

02:14

para as ferramentas,

02:15

para as ações executadas e também para as cópias secundárias desses dados,

02:20

como logs, traces e datasets de avaliação.

02:24

Vamos pensar no nosso Knowledge Chat que a gente construiu durante essa disciplina.

02:28

O sistema recebe uma pergunta,

02:30

planeja a consulta, recupera documentos no PgVector,

02:34

faz o re-ranking e gera uma resposta com fontes.

02:37

Em uma situação normal, isso funciona bem.

02:40

Mas o que acontece se o usuário pedir para o

02:42

modelo ignorar as regras e revelar as instruções internas?

02:46

O que acontece se um documento...

02:49

Dentro da base de conhecimento,

02:51

disser que o modelo deve desconsiderar o system prompt.

02:54

O que acontece se uma pergunta tenta induzir o

02:57

query planner a buscar um documento de um outro tenant?

03:02

O que acontece se uma resposta contiver informações sensíveis e for

03:07

registrada em um trace ou copiada para um dataset de evaluation?

03:11

Agora pense no nosso support triage agente.

03:15

Ele pode consultar a base de conhecimento,

03:18

verificar o consumo atual de um tenant e criar um ticket de suporte.

03:21

Se o modelo for manipulado, ele pode escolher a ferramenta errada,

03:26

pode usar argumentos incorretos, pode tentar acessar dados de outro tenant,

03:30

pode criar um ticket que o usuário não pediu,

03:33

pode executar uma ação com uma severidade diferente da autorizada.

03:37

O problema não é apenas o modelo produzir uma frase errada.

03:41

O problema é o efeito que essa decisão... pode gerar no restante do sistema.

03:46

E é por isso que uma ideia que vai acompanhar todo esse

03:50

módulo é o modelo não deve ser tratado como uma fronteira de segurança.

03:55

A gente não pode depender apenas de uma instrução dizendo não faça isso.

04:00

Também a gente não pode assumir que um system prompt permanecerá,

04:05

vamos dizer ali, totalmente secreto. Se uma informação é realmente sensível,

04:09

ela não deveria estar no contexto do modelo. Da mesma forma,

04:14

o modelo não deve decidir sozinho se o usuário pode acessar um documento,

04:18

utilizar uma ferramenta ou executar uma ação crítica.

04:21

Essas decisões precisam ser aplicadas por código confiável. fora no modelo,

04:26

de forma determinística e auditável. Isso não significa que os prompts,

04:31

classificadores e guardrails não sejam úteis.

04:34

Eles são úteis para dictar conteúdo suspeito,

04:37

reduzir determinados ataques,

04:39

aplicar políticas de domínio e interromper fluxos de risco.

04:43

Mas eles não são, na realidade, uma barreira. Perfeita.

04:48

Um guard rail pode falhar. Um classificador pode gerar um falso positivo.

04:52

Um ataque pode ser escrito de uma forma que

04:55

a gente não estava esperando ali no dataset.

04:58

Uma atualização do modelo pode alterar o comportamento do sistema.

05:02

Por isso, a arquitetura precisa assumir que alguma camada pode falhar.

05:07

Se um prompt injection funcionar,

05:09

o sistema ainda deve limitar quais dados o modelo consegue acessar.

05:14

Se o modelo tenta chamar uma ferramenta indevida,

05:17

uma política externa deve bloquear a execução. Se a ferramenta for permitida,

05:22

seus argumentos ainda precisam ser validados. Se a ação for crítica,

05:26

pode ser necessário pedir aprovação humana. Se o conteúdo for sensível,

05:30

ele não deve aparecer automaticamente nos logs, nos traces ou nos datasets.

05:36

Essa combinação de controles é o que chamamos de defesa em profundidade.

05:41

Ao longo desse módulo, nós vamos, na realidade,

05:44

a gente não vai apenas listar ataques.

05:47

A gente vai usar o projeto que a gente

05:49

já construiu para tornar os riscos mais visíveis.

05:53

Primeiro, a gente vai mapear a superfície de ataque,

05:55

a gente vai criar casos controlados.

05:57

em que determinadas vulnerabilidades possam aparecer e etc.

06:02

Em alguns cenários o ataque pode ser bloqueado,

06:04

Em outros, o impacto será apenas reduzido.

06:07

Em alguns casos, ainda teremos um risco, vamos dizer, residual.

06:11

Isso também é importante,

06:13

porque segurança não significa afirmar que o sistema se tornou impossível de atacar.

06:18

Significa conhecer os riscos, limitar o impacto,

06:21

medir o comportamento e tomar decisões arquiteturais conscientes. No próximo vídeo,

06:26

a gente vai entender o que são superfícies de

06:29

ataque e trust boundaries em aplicações com IA.

06:33

Vamos percorrer o fluxo do usuário até a ação final e identificar

06:37

em quais pontos conteúdos não confiáveis

06:42

atravessam limites importantes dentro da arquitetura.

06:46

Então, bora lá!

## Resumo IA

[RESUMO_IA]