Módulo: Desenvolvimento de Agentes com IA\
Aula: [O Que É Um Agente de IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18092)

## Resumo da aula



## Transcrição

00:00

Nesta aula nós vamos falar o que é um agente de IA.

00:04

É muito importante ter essa definição na sua cabeça.

00:09

Você não vai decorar isso agora,

00:12

vai ficar muito mais claro uma vez

00:17

que esse processo de aprendizado vai sendo construído,

00:19

você vai vendo as coisas acontecendo,

00:22

mas é um novo tipo de software que nós vamos construir,

00:26

é uma nova competência nossa.

00:31

Entender o que ele é porque acaba se gerando muita confusão com outras coisas,

00:37

com outros padrões já existentes.

00:39

Então eu coloquei aqui uma definição do Google que

00:44

simboliza exatamente o que é um agente de IA.

00:49

O agente de IA é um sistema de software,

00:51

um software que usa IA para alcançar objetivos

00:54

e concluir tarefas em nome dos usuários.

00:58

Ou seja... É um software em que a IA é o coração. Se

01:06

você tira a IA, acabou o software.

01:11

Então, por conta disso, esses sistemas vão demonstrar raciocínio,

01:15

planejamento e memória, com

01:19

autonomia para tomada de decisões, usando aprendizado e adaptação.

01:27

Isso é um agente de IA.

01:30

Ele vai ter essas quatro características.

01:35

como autonomia, porque

01:38

ele não precisa de nenhuma intervenção humana, a princípio,

01:41

ele não precisa de nenhuma intervenção constante,

01:43

ele pode tomar decisões, executar ações por conta própria.

01:48

E é por isso que nós estamos querendo criar um agente de IA,

01:51

por conta dessa habilidade que ele tem que um software tradicional não vai ter.

01:57

Ele tem raciocínio, porque ele processa informações...

02:01

E analisa situações e tomadas de decisão com base nos dados e regras.

02:10

Ele tem também o sistema de aprendizado,

02:13

que ele aprende com as experiências passadas,

02:15

porque ele tem um sistema de memória.

02:18

Nós podemos colocar dentro do contexto da IA tudo que

02:23

é necessário com base em execuções passadas ao longo do tempo.

02:28

Isso faz a tal diferença. E também tem interação.

02:32

Ele interage com os usuários e outros sistemas,

02:35

não somente os usuários. Ele pode interagir,

02:36

o agente de IA pode acessar um banco de dados, acessar o sistema de arquivos, ele

02:44

compreende linguagem natural e vai responder de forma

02:47

adequada conforme um sistema ou um usuário requisitou.

02:53

E aí nós temos que deixar uma definição muito clara.

02:57

Eu posso construir uma aplicação com IA em

03:02

um agente de IA. São duas coisas totalmente diferentes.

03:08

Uma aplicação com IA é uma aplicação tradicional que nós desenvolvemos,

03:12

mas vamos fazer uma chamada para a LLM para atender alguma necessidade.

03:18

Então o que muda é que eu tenho uma entrada de dados,

03:21

vou validar essa entrada, imagine que você tem uma API REST, validou os dados,

03:26

em algum momento vai cair na LLM que você vai

03:29

fazer a chamada utilizando um token de API.

03:33

E ela vai devolver alguma coisa que você pediu, uma classificação, um resumo, algum cálculo.

03:41

Você vai usar o seu software para gravar a resposta e responder para o usuário.

03:46

Então, esse fluxo é determinístico.

03:50

Foi você que definiu, e não a IA.

03:55

Se acontecer qualquer coisa fora da caixa,

03:59

o seu software vai acabar devolvendo um erro.

04:01

Ele não vai processar aquilo que aconteceu. Ao contrário de um agente de IA,

04:07

o caminho é decidido em runtime.

04:11

Ele vai ter um objetivo e, para que ele atinja aquele objetivo,

04:15

uma vez que o usuário ou algum sistema

04:18

fez alguma chamada para esse agente de IA,

04:23

ele pode decidir pedir mais informações para o usuário.

04:28

E quando o usuário dá mais informações,

04:30

ele decide chamar uma ferramenta que vai invocar uma consulta no banco de dados.

04:35

Depois dessa consulta,

04:37

ele decide novamente que precisa de mais informações do usuário.

04:41

E aí ele faz mais três chamadas, uma para o banco de dados novamente,

04:46

uma para buscar na web alguma coisa e outra para ler o sistema de arquivos.

04:52

Ele pode ficar aqui nesse loop,

04:56

muito tempo até tomar a decisão de terminar e responder. Então,

05:02

é o modelo de inteligência artificial que está definindo a próxima lacuna.

05:09

Isso aqui é muito importante.

05:11

Não é você.

05:13

Você vai criar o agente, dar as capacidades, falar o que ele deve fazer,

05:18

mas vai ser ele que vai tomar essas decisões.

05:29

Os agentes de IA têm o que a gente chama de...

05:34

Agent Loop, ou loop agêntico.

05:37

Você já viu isso acontecer usando qualquer ferramenta de agente de IA,

05:43

como o Cloud Code, o Copilot, o OpenCode, qualquer uma.

05:48

Coloque uma mensagem, mande um prompt, para que ele deixe os testes verdes.

05:56

Dependendo do seu projeto,

05:58

ele vai criar

06:00

um plano totalmente inovador.

06:06

Para deixar esses testes verdes.

06:08

Talvez ele precise invocar uma ferramenta, editar arquivos, mas,

06:15

de alguma forma, a gente sabe que ele vai rodar os testes.

06:18

Então, ele planeja o que ele vai fazer, dado o objetivo que foi dado,

06:24

ele toma uma atitude,

06:27

depois disso tem o resultado e vem a adaptação.

06:31

Então, os testes podem ter tido erro.

06:35

Ele vai ver o erro, então vai tentar de novo.

06:37

Então vai ter um novo objetivo, vai criar um novo plano,

06:42

que agora, com esse erro, eu preciso apagar o

06:46

banco de dados para depois executar o teste novamente.

06:51

Até que esse loop se resolva nos

06:56

testes verdes, ou seja, no objetivo final do usuário.

07:01

Então, a questão é que ninguém programou essa sequência. O agente que escolheu.

07:08

Quando você pede algo, ele tem total liberdade para poder fazer essas escolhas.

07:13

Quando falamos de agente de IA, estamos falando desse DNA não determinístico.

07:18

Se eu passar um JSON inválido para um software tradicional,

07:22

Ele vai devolver logo de cara uma exceção, um Bad Request.

07:27

Ele não vai conseguir processar aquilo,

07:30

porque está tudo programado. Agora,

07:33

se eu passo para um agente de IA um JSON inválido,

07:38

ele pode tentar corrigir se caso tiver alguma questão,

07:42

pedir mais informações para o usuário.

07:45

E aí depois de analisar todo esse processo, não,

07:48

não dá para processar isso aqui, não vai rolar.

07:52

Então ele vai lá e falha,

07:53

não significa que sempre ele vai consertar e tentar fazer as coisas.

07:58

Mas vê a diferença?

08:00

Mas no caso, se eu passar uma informação incorreta ou faltando alguma coisa,

08:05

ele pode subentender.

08:07

Ele pode conseguir processar de forma correta aquela

08:12

informação. Então é o não determinismo. Nós não temos algo

08:18

batido em pedra. O agente de IA vai ter uma liberdade de pensamento,

08:23

ele vai ter um cérebro para poder executar aquela tarefa.

08:27

E é esse não determinismo que torna algo tão poderoso.

08:33

E, obviamente, isso é uma faca de dois gumes,

08:36

porque, como eu estou amplificando o poder...

08:41

eu tenho uma amplitude de possibilidades,

08:45

nós vamos ter também vários problemas, como problemas de segurança,

08:50

prompt injection,

08:52

vamos ter que fazer guardrails, os agentes podem alucinar,

08:56

vou ter que escolher os modelos, a temperatura dele,

08:59

como o prompt vai ter que ser feito, entender também os custos disso,

09:04

porque nós já sabemos que o gasto de token é alto, mas enfim.

09:09

Um agente de app muito bem construído,

09:12

encaixado muito bem dentro do ambiente corporativo,

09:16

é algo muito valioso e algo que provavelmente você já

09:19

deve ter usado fora do agente de IA,

09:22

ter usado algum agente de IA em alguma outra

09:24

situação e você tem uma experiência totalmente distinta.

09:28

Então nós vamos criar esse agente,

09:32

ver vários exemplos e com certeza vai te abrir...

09:37

uma série de ideias e possibilidades para que você possa

09:40

criar os seus agentes e fazer coisas dentro da sua empresa.

## Resumo IA

[RESUMO_IA]