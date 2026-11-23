Módulo: Desenvolvimento de Agentes com IA\
Aula: [Primeiro Exemplo de Subagents](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18257)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos ter o primeiro exemplo com subagentes.

00:04

Eu dupliquei o operador conta acrescentando essa pasta de subagent,

00:10

operador conta subagent,

00:12

e nós vamos trabalhar aqui para preservar o exemplo anterior.

00:17

Então, nós temos o agente que pode listar faturas,

00:22

cancelar assinatura. Nós não estamos nos preocupando aqui em...

00:28

fazer uma boa divisão sobre o que nós conversamos na última aula,

00:31

de pensar se caberia subagente ou não.

00:35

Nesse caso aqui não caberia subagente porque nós temos um agente muito simples,

00:40

então é importante falar isso.

00:43

Mas vamos pegar essas duas tarefas, essas duas responsabilidades do agente,

00:49

que é tirar dúvidas da fatura e cancelar a assinatura e transformar isso...

00:56

em subagentes. Eu vou criar os subagentes dentro desse arquivo,

01:01

mas eu poderia criar um outro arquivo separado, com qualquer nome,

01:05

e colocar esses agentes lá. O que importa no padrão, na convenção do ADK,

01:10

é que você tenha uma pasta com o agent.py.

01:13

Agora, se você tem os subagentes e onde que eles vão estar,

01:16

pode estar até em outra pasta, não tem problema nenhum.

01:19

Então, eu vou começar pelo consultor de faturas.

01:24

Vou adicionar um subagent na variável para ficar fácil de lidar.

01:29

Um subagent nada mais é do que um próprio agent.

01:33

No caso do ADK não tem nenhuma classe separada.

01:36

Então colocamos um nome para ele que pode ser o próprio consultor de faturas.

01:40

Não preciso colocar subagent aqui.

01:42

A variável serve para que fique fácil. E vamos deixar com que...

01:49

A IA preencha, o restante vamos avaliar. Obviamente,

01:52

nós não vamos listar faturas mais aqui, não

01:56

é competência mais do agente coordenador. O

02:06

modelo podemos deixar o mesmo,

02:08

mas aí nós ganhamos aquela liberdade de definir o modelo mais adequado,

02:12

que vai trazer mais custo ou menos custo, dependendo do que nós queremos.

02:18

No System Prompt, vamos ver o que está sendo colocado aqui.

02:22

Você é um consultor de faturas da Acme, ok.

02:26

Nós colocamos justamente isso aqui.

02:28

Você é responsável por listar faturas de um cliente específico.

02:33

O usuário precisa fornecer o ID.

02:35

Isso aqui não é necessário porque nós já podemos colocar isso no agente principal.

02:43

Isso vai satisfazer tanto a esse subagente de listar faturas quanto o de assinatura. Então,

02:50

isso aqui já é mais do que suficiente. Na verdade, seja cordial direto,

02:53

eu vou tirar também. Ele vai ser responsável,

02:55

apenas por fazer a listagem de faturas e obviamente

02:58

aqui nós poderíamos colocar quaisquer outras informações.

03:02

Se ele é um consultor de faturas,

03:04

poderia ter somatórias ou uma análise

03:07

mais distinta sobre aquilo que foi pesquisado.

03:12

Então, esse tirar dúvidas sobre fatura do cliente,

03:16

eu poderia remover daqui sim

03:20

ou não. Não temos a resposta porque...

03:26

Isso aqui pode ser bom para ele entender o contexto que ele tem,

03:30

mas uma vez que eu tenho subagente,

03:31

Esse contexto vai acabar sendo agregado. Nós vamos verificar isso depois,

03:36

mas por enquanto nós vamos tirar essa informação daqui. Então agora eu

03:43

tenho subagentes em

03:48

que eu encaixo todos os meus agentes que eu quero. Aqui tem um underscore. Pronto.

03:56

Então agora vamos criar... O consultor de assinatura, que

04:08

acho que a IA vai nos ajudar, ela pegou aqui consultor de assinaturas,

04:13

você é responsável por,

04:15

tem o modelo e agora tem a tool. Então, nesse caso,

04:21

o nosso agente coordenador não tem mais nenhuma tool. Ele pode ter ou pode não ter.

04:27

Ele pode fazer outras coisas que não estão no subagente.

04:32

Aqui só não está alinhado e a ideia também não está.

04:38

Aliando de forma default.

04:40

Então, a princípio, não mudou nada. Então,

04:43

por isso que nós temos que tomar cuidado. Isso aqui também vai acabar saindo.

04:47

E você é responsável por restou a questão das informações sobre assinatura. Nós não temos isso.

04:54

Nós colocamos isso apenas de praxe.

04:57

Nós precisamos adicionar o outro consultor de assinaturas. Então, pronto.

05:02

Temos um agente coordenador com dois subagentes.

05:07

E não temos nenhuma informação sobre o que ele tem que fazer.

05:10

Ele só vai receber o ID do cliente e ser cordial e direto. Então, vamos rodar esse

05:18

agente. Primeiro, quero listar minhas ações.

05:24

Vou pedir o ID. Está

05:32

correto. 2024 e tudo mais.

05:35

Quero cancelar minha

05:40

assinatura.

05:46

Então, ele está pedindo aqui

05:49

o ID do cliente.

05:51

E também a minha senha secreta. É assim.

05:58

Pronto. Vou dar a confirmação. Sua assinatura foi cancelada com sucesso.

06:04

Então veja que nós conseguimos fazer as duas coisas com

06:09

o mínimo de prompt.

06:12

Mesmo utilizando um modelo muito barato

06:18

e que não tem tanta qualidade assim,

06:21

ele conseguiu desempenhar tudo o que foi necessário.

06:27

Obviamente temos muitas coisas acontecendo aqui,

06:30

nós não vamos ver exatamente nessa aula,

06:33

mas aqui fica como lição. Isso serve também para qualquer framework.

06:38

Todos esses não-dizeres ou

06:41

delimitação eficiente que nós fizemos no

06:45

System Prompt vai ser aquele

06:48

centavos agregado a milhares de solicitações.

06:53

que vai ser uma economia expressiva a médio e longo prazo.

06:59

Com isso aqui feito, nós já tivemos esse primeiro contato,

07:03

como que é fácil criar os subagentes com o ADK,

07:06

nós vamos entender como essa comunicação está acontecendo na próxima aula.

07:12

Nós vamos fazer um debug com o ADK Web e ver

07:14

várias outras coisas aprofundando um pouco mais nesse conceito.

## Resumo IA

[RESUMO_IA]