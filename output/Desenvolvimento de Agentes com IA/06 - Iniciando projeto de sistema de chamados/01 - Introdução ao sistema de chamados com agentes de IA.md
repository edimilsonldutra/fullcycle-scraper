Módulo: Desenvolvimento de Agentes com IA\
Aula: [Introdução ao sistema de chamados com agentes de IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18556)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos iniciar um novo projetinho de sistema

00:04

de chamados utilizando agentes de IA.

00:07

Um sistema de chamados é algo muito fácil de entender.

00:11

Nós vamos continuar nessa dobradinha de teoria e prática ao mesmo tempo,

00:17

mas focados ali no código.

00:20

Mas este projetinho vai permitir explorar outros

00:23

fundamentos muito importantes do ADK.

00:27

Além de responder dúvidas pontuais, que eu tenho certeza que talvez você já tenha,

00:32

ou você vai ter na hora de criar os seus agentes,

00:35

como se eu estivesse criando um agente, eu preciso salvar aqui um resultado.

00:39

Poderia usar uma tool, poderia explorar de outra forma.

00:43

Ou se eu preciso fazer uma chamada HTTP, eu usaria uma tool,

00:46

ou usaria uma outra forma. Coisas desse tipo.

00:49

Nós vamos construir agora um agente muito mais robusto, abordando esses conceitos.

00:55

Então, no sistema de chamadas, o usuário vai abrir tickets por

01:01

qualquer situação. Ele quer cancelar, ele quer tirar uma dúvida,

01:05

ele quer fazer N coisas.

01:08

Então, com o que nós já aprendemos aqui através das aulas,

01:13

nós já entendemos que esse usuário interage diretamente com a

01:17

gente de IA e vai gerenciar os tickets.

01:20

Poder listar os tickets, abrir novos, já solucionar o que o usuário precisa. Poderia ser

01:30

dúvidas, cancelamento, até um reembolso,

01:35

enfim, N coisas.

01:38

Esse agente já poderia ser totalmente autossuficiente,

01:41

não precisaria de nenhuma intervenção de fora,

01:45

de ninguém da empresa, ele já poderia resolver tudo.

01:48

Mas nós sabemos que em várias situações,

01:54

este

01:56

agente poderia existir,

01:59

mas ele não vai conseguir fazer, às vezes,

02:01

um reembolso que envolve um valor maior ou uma situação específica.

02:06

A mesma coisa vale para um cancelamento.

02:09

Enfim, qualquer tarefa,

02:11

quaisquer tarefas que vão necessitar a intervenção de alguém de dentro da empresa.

02:17

E aí a questão é,

02:19

alguém de dentro da empresa vai continuar interagindo com a mesma sessão, agora que nós já sabemos?

02:26

Sair da sessão, vai continuar interagindo com essa mesma sessão do usuário,

02:30

isso não seria nada bom,

02:32

porque o usuário já teve o histórico de interação

02:35

com a gente para abrir esse ticket, e

02:39

se existir um funcionário que vai interagir com essa mesma sessão,

02:46

vamos ter todo o histórico dos eventos que

02:51

vão poder ser acessíveis pelo usuário.

02:57

Então, nós podemos ter uma situação em que...

03:01

Temos um agente de IA que gerencia os tickets para o usuário,

03:05

abre tickets, lista, tira dúvidas, poderia

03:10

até resolver algumas situações mais pontuais. Mas nós podemos ter um

03:17

agente de IA que vai ser a resolução dos tickets. Ele

03:26

pode agir sozinho, não é necessário ter um funcionário,

03:33

inclusive vou jogar esse funcionário.

03:35

Aqui em segundo plano,

03:37

porque quando acontecer uma situação que precisa de aprovação,

03:41

nós já vimos lá que tem a tal da tool confirmation,

03:45

ou qualquer coisa que necessite o human in the loop,

03:49

um funcionário vai ter que fazer a

03:53

sua interação direta ou através de alguma ferramenta.

03:59

Isso é para que você entenda que existem várias

04:01

formas de interagir com esse agente de IA.

04:04

Não é necessariamente que...

04:06

ele vai abrir um chat e vai dar um comando autorizando.

04:10

Às vezes o agente de IA tem integração,

04:12

você pode integrá-lo com um Gira,

04:15

com Linha ou com qualquer outra ferramenta que tem esse outro ticket em algum lugar,

04:20

você move, faz alguma coisa lá, bate no agente de IA aqui.

04:23

Tudo através de HTTP, nós vimos como fazer isso.

04:28

Então nós vamos trabalhar com esse cenário em que nós

04:31

teremos este agente dos tickets e um agente de resolução interna.

04:36

Assim, nós

04:38

vamos ter duas sessões distintas para a resolução do problema.

04:48

Essa sessão vai ficar gravada só

04:53

internamente. Ela vai ser acessível somente pela empresa.

04:56

Já a sessão do usuário vai ficar somente o que está...

05:01

Qual o histórico de interação dele.

05:03

Ele consegue ver o resultado dessa interação exatamente porque nós

05:08

vamos gravar o que acontecer aqui no banco de dados.

05:12

E aí ele pode receber lá a notificação dele,

05:14

vir aqui depois, fazer as suas devidas perguntas, enfim.

05:19

Então nós vamos ter um sistema de chamados que tem dois agentes.

05:25

Mas não

05:27

vai ser tão simples assim, porque esse agente de resolução vai

05:33

demandar mais complexidade.

05:36

E o que nós já aprendemos até o momento em relação ao agente,

05:40

subagentes, não vai ser suficiente.

05:44

para que atenda a essas necessidades.

05:47

E aí nós vamos aprender alguns conceitos novos,

05:49

que aí vai fechar todo esse arco para que você possa ter uma base sólida

05:55

com a ADK e tomar as decisões de como você vai orquestrar os seus agentes.

06:01

Estou colocando aqui no plural.

06:03

Não significa que é referência só desses agentes aqui.

06:08

Nós teremos mais agentes nesse contexto.

06:11

Vamos começar a nossa nova saga aqui na disciplina.

## Resumo IA

[RESUMO_IA]