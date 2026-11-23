Módulo: Desenvolvimento de Agentes com IA\
Aula: [Introdução aos workflows](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18565)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos iniciar um novo capítulo dedicado a trabalhar com workflows,

00:05

que é um recurso do ADK que permite criar agentes complexos,

00:11

ou melhor, a forma mais avançada de criar agentes com ADK.

00:17

Eu chamo a atenção nessa parte da documentação,

00:20

que ele vai falar desse Graph-Based Agent Workflows.

00:24

Ele mostra que nós temos suporte no momento à versão 2.0,

00:29

porque esse recurso foi lançado na 2.0, para Python e para Go.

00:34

Mas pode ser que já tenha suporte a outras linguagens que o ADK suporta,

00:39

porque muitas vezes a documentação não tem sido atualizada, ou

00:46

atualizada com certa frequência. Então,

00:48

eu recomendo que você vá lá no GitHub do ADK, tem o...

00:53

ODK central e de cada linguagem de programação e faça a verificação.

00:57

GitHub é sempre um lugar mais certeiro,

01:01

mais confiável, para que a gente possa verificar, na verdade, qualquer coisa que

01:06

a documentação está dizendo.

01:11

Aqui nós temos esse grafo, eu quero falar sobre ele.

01:17

Veja que aqui é um processo, um fluxo de trabalho que foi determinado,

01:24

que... Tem agentes, mas também tem processos determinísticos.

01:29

Tem momentos que nós não vamos ter nenhum agente executando.

01:33

Vai ser uma função que nós vamos programar,

01:36

como se fosse uma tool. Então eu tenho um grafo dirigido.

01:45

E justamente um grafo, é aquele conceito da matemática, que eu tenho os nós,

01:49

cada lugar, aqui é um nó, eles estão interligados.

01:55

E ele é dirigido porque ele tem uma direção,

01:57

ele tem um começo e vai chegar até aqui no eixo upgrade ou no deny upgrade.

02:05

E assim nós processamos esse fluxo de trabalho que nós queremos.

02:11

Mas nós devemos entender por que esse workflow é importante e se a gente

02:17

conseguiria criar a mesma coisa com o conceito de agentes que nós já aprendemos.

02:23

Aprendemos durante as aulas a criar operador de conta,

02:26

o ticket receptionist, e

02:33

agora temos o ticket resolution,

02:35

que é a resolução desse ticket. O

02:39

que nós teremos nesse ticket resolution? A

02:44

resolução de dúvidas, poderíamos ter uma base de conhecimento, um banco de dados,

02:49

trabalhar com regex e outras coisas. A verificação do status dos serviços, então

02:56

a gente aponta lá para os serviços ou tem...

02:58

um ServiceJobTime, que verifica se as coisas estão ok.

03:03

Estorno, obviamente, porque nós vamos ter estorno automático,

03:07

quando o valor é menor que 50 dólares,

03:10

e um estorno escalonado, porque se for um valor maior,

03:15

tem que ter um humano no meio do processo. Então,

03:18

maior que 50 dólares, aí tem o human in the loop, o humano no meio do processo.

03:26

Ele vai fazer essa aprovação. Então, pensando nesse cenário,

03:30

eu conseguiria até pegar o Ticket Receptionist e agregar tudo num lugar só?

03:37

Eu consigo fazer isso.

03:40

Consigo ter os meus subagentes,

03:43

que até os seus subagentes podem ter os seus subagentes.

03:51

Então pensa que aqui está o coordenador, aí chega uma chamada,

03:54

vem para cá, aí ele volta para o coordenador,

03:57

aí dependendo do que for, ele vem para cá,

04:01

Volta para o coordenador de novo. E aí nós temos uma comunicação que

04:06

pode se tornar bem complexa dentro desse agente.

04:11

E o que nós temos que entender é que agentes

04:14

de IA são bons em fazer tarefas específicas.

04:20

E, obviamente, não só por conta disso, mas pense em manter algo assim, em testar,

04:27

manter um agente de IA desse tamanho, em testar, em manter a qualidade,

04:33

em otimizar o gasto com tokens.

04:36

Tudo isso vai se tornando muito difícil.

04:40

E até mesmo nós vamos ter problemas para ter consistência nas operações.

04:46

Ou seja, fazer as operações conforme

04:51

elas têm que ser. Eu tenho que fazer a operação completa,

04:54

tem que acontecer isso. Mas se não acontecer, eu tenho que desfazer tudo.

05:00

Tem que ter um processo de um rollback.

05:04

Quando nós estamos falando de um software que é não determinístico,

05:09

tudo isso é muito complicado. E na hora de fazer o estorno,

05:11

a gente vai deixar que o estorno seja feito ou

05:15

que ele tenha alguma chance de não acontecer por alguma coisa?

05:20

Ou às vezes uma operação que envolve dinheiro que pode ter um valor errado?

05:26

Então, em muitas situações, nós vamos preferir trabalhar

05:32

de forma determinística e

05:36

deixar o não determinismo para outros momentos.

05:41

Então, fazer isso.

05:44

Com essa forma tradicional ali com agentes, é muito difícil.

05:49

Então, para isso que serve o workflow.

05:52

Para quando nós precisamos ter múltiplos agentes se

05:56

comunicando e nós não estamos falando apenas de subagentes,

06:00

eu posso ter o agente de ticket

06:05

receptionist e outro agente que é um agente independente,

06:09

mas os dois podem se comunicar através de um processo.

06:13

Então, nós conseguimos...

06:15

criar essa orquestração, criar um fluxo mais complexo, fazendo o mix.

06:20

A beleza do workflow é justamente esse mix do determinismo com o não determinismo.

06:27

Então, nós conseguimos fazer functions,

06:33

são códigos que nós criamos, conseguimos colocar tools como está aqui,

06:39

nós vemos que essa função vai fazer uma checagem

06:44

usando linguagem de programação convencional. Então,

06:47

ela vai ver se Miles é menor que 5,

06:49

ou entre 5 e 20, ou maior que 20.

06:52

Então, se for menor que 5, vem para cá. Maior que 20,

06:56

vem para cá. Mas o fluxo mais complexo é entre 5 e 20.

07:00

Aí ela pega o input do ser humano, executa uma tool,

07:03

e depois tem um processo de agente,

07:06

e aí é aprovado. Então, veja que eu tenho duas formas de aprovar essa issue.

07:15

E uma forma que vai rejeitar, que vai ser nesse caminho aqui,

07:19

que vai chegar aqui na LLM, e nesse caso,

07:23

na verdade, eu tenho duas formas, porque ele pode ir para cima também,

07:29

tenho duas formas de rejeitar e de fazer a aprovação.

07:34

Então, isso vai nos dar oportunidade de ter esse processo com esses nós,

07:40

permitindo que ao longo do tempo...

07:43

tenhamos mais ramificações.

07:45

Sendo que isso se torna mais simples de adicionar,

07:51

Ou se às vezes a ramificação não precisar

07:55

Existir, nós podemos remover sem quebrar esse grafo,

07:59

Algo que quando nós estamos em um agente,

08:02

Vai acabar mudando ali os subagents e o system prompt.

08:06

Mudar o system prompt, dependendo do que for feito,

08:09

Pode ser que o seu agente quebre.

08:11

Se você não está fazendo de forma correta. E mesmo assim,

08:14

Ainda pode ter testes que não foram feitos, coisas que você só vai ver em produção.

08:21

Então, o Workflows permite isso.

08:24

Eu quero chamar a atenção também para alguns fluxos que nós podemos...

08:29

Antes eu vou falar desses fluxos. Nós podemos implementar

08:33

Fluxos sequenciais, como

08:39

Esse que está aqui. Um chama o outro, chama o outro.

08:45

Podemos ter...

08:48

Fluxos paralelos, podia

08:53

Ser que o function checkMiles poderia executar três nós ao mesmo tempo.

08:59

Esses nós poderiam ser agentes.

09:02

Então eles vão executar e aí vão devolver uma

09:06

Resposta e o próximo nó processa toda essa resposta.

09:11

Nós podemos ter um condicional, que é justamente o que já está presente aqui,

09:18

Se eu tiver um condicional, eu venho para cá.

09:20

Se eu tiver outro condicional, eu venho para cá.

09:23

Cada vez fica mais bagunçado o meu desenho. Inclusive, não só nós conseguimos ir

09:30

Para

09:31

Um caminho no gráfico, como eu poderia chegar aqui e voltar para cá,

09:36

Se for necessário.

09:37

Eu consigo rotear para o nó anterior.

09:41

E também nós temos o loop. Nós podemos ficar executando nós.

09:48

Até satisfazer alguma condição, é aquela história do loop de agentes,

09:51

Então eu tenho uma condição e aí vai ter um loop de agentes,

09:58

De funções,

10:00

Pode ter uma mistura de um monte de coisas,

10:03

E aí no momento que satisfaz essa condição,

10:05

Então tem o resultado, mas aquilo pode ficar executando minutos ou horas.

10:12

É o recurso mais avançado, nós conseguimos implementar várias coisas,

10:16

Mas tome cuidado na hora que você olhar na documentação,

10:18

Por exemplo, ele fala aqui do Sequential Agents, aí

10:21

Ele vai mostrar um

10:24

Código que funciona, está vendo aqui esse Sequential Agent,

10:29

É a forma que era usada na versão 1, que

10:34

Não tinha suporte ao workflows. Então, todos esses fluxos de trabalho,

10:39

Essas formas de implementar, tudo é suportado pelo workflows.

10:44

Então cuidado na hora que você estiver vendo a documentação

10:47

Ou pedindo alguma coisa para o seu agente

10:49

De codificação, codificar o agente do ADK para que

10:53

Ele não use essas formas que vão ser depreciadas,

10:57

Que não vão ser recomendadas mais.

10:59

Então você vai ver, você tem o agente paralelo, o

11:05

Loop agent, tudo isso faz parte da versão 1. Então tudo foi colocado

11:11

No workflows. Então nós vamos aprender como montar.

11:15

Agentes com esses workflows nesse capítulo.

## Resumo IA

[RESUMO_IA]