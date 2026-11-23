Módulo: Desenvolvimento de Agentes com IA\
Aula: [Trabalhando com state temporários](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18560)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre state temporário.

00:03

Nós já entendemos que o state é uma informação que vive na sessão,

00:07

porém, esse state tem um modificador,

00:11

na verdade um namespace,

00:12

que faz com que a vida dele possa ser muito pequena ou muito longa,

00:19

ou convencional, que é a forma que nós estávamos trabalhando.

00:24

Com o último teste que nós fizemos, o

00:27

ticket foi registrado com sucesso.

00:30

Temos aqui o ID dele,

00:33

inclusive até se a gente quiser verificar no banco de dados, nós podemos fazer o

00:39

SELECT asterisco FROM do ticket.

00:45

Se eu quiser registrar outro ticket, será que é possível? Nessa mesma sessão?

00:50

Numa outra sessão, sim. Mas será que eu posso registrar outro?

00:55

Vamos falar que agora eu quero registrar outro ticket.

01:05

com a mensagem. A gente pode até enviar tudo num só.

01:11

Ele vai lá fazer a classificação de novo.

01:18

Pronto, então tem um outro ticket sendo registrado.

01:24

E nós temos que tomar cuidado com

01:28

a continuidade da sessão.

01:30

Ela pode trazer um comportamento inesperado para o

01:34

seu agente dependendo de como você define esse fluxo.

01:39

Veja, na tool temos

01:44

uma verificação se...

01:46

O output key do classifier está presente no state,

01:51

porque se ele não estiver, vai retornar esse erro aqui.

01:57

Ok, mas uma

02:00

vez que nós definimos um

02:06

state convencional, isso

02:11

aqui pode causar um comportamento inesperado. Quer ver só? Porque uma vez que eu criei o ticket,

02:20

esse state aqui permanece em todo o tempo de vida da sessão.

02:29

E se numa segunda mensagem,

02:32

apesar de nós termos colocado aqui que ele

02:36

precisa ativar o processo de classificação,

02:38

o usuário pode tentar fazer uma trapaça, ou o modelo pode ficar confuso,

02:44

o nosso system prompt pode ter mais informações e o modelo se confundir,

02:48

são várias possibilidades, e ao invés dele fazer a classificação, ele

02:57

já ativa o registro do ticket.

03:01

Eu enviei a mensagem,

03:07

E aí ele não vai fazer a classificação. Se ele chegar na tool,

03:11

ele vai ver que tem a classificação e a classificação é antiga.

03:15

Então teremos uma mensagem corrente registrada com a classificação anterior.

03:23

Então o que eu quero chamar a atenção justamente para a definição do state,

03:28

porque existem três formas

03:33

de você definir esse state. Um state convencional,

03:37

que é esse que nós fazemos com um nome,

03:41

convencional qualquer. Um

03:44

temporário, como é esse que está aqui.

03:48

Ele só vai sobreviver à noite. Sobrevive

03:55

à noite. Parece que até que está

03:59

me ouvindo. E de usuário, que vai sobreviver para

04:06

O usuário. Ou seja, entre sessões.

04:11

Esse aqui é o state que tem a sobrevida maior.

04:16

Enquanto... estivermos trabalhando com aquele usuário,

04:18

nós conseguimos usar esse state através de sessões.

04:21

Até isso aqui vai de encontro um pouco com memória de longo prazo.

04:30

Então, trabalhar com esse state dessa forma é interessante porque

04:36

toda vez que a gente olha para cá,

04:37

para o state, não tem nada.

04:39

Porque quando o modelo já vai terminar o turno enviando a mensagem para o usuário,

04:46

ele morre. Ele não fica armazenado. Eu preciso ficar armazenando...

04:52

O ticket classifier output, não.

04:54

Eu estou precisando apenas como uma forma de comunicação.

04:57

Nós já vimos que o state é usado por essa forma. Então, pense

05:02

bem na hora de você determinar o state,

05:04

porque tem essas alternativas e também se uma definição,

05:08

um valor que vai ter uma sobrevida maior, se ele não pode causar um problema.

05:14

Isso é muito comum.

05:17

O modelo se confunde, começa a entrar num loop e vai chamando as informações,

05:23

vai chamando as tools de forma inesperada, chamando a

05:27

LLM várias vezes,

05:29

e aí ela pode até chamar esse registrar ticket algumas vezes,

05:35

mas eu não quero falar sobre essa questão dele

05:38

poder duplicar esse ticket que nós estamos registrando aqui.

05:44

Mas a questão é que esse state temporário, ele

05:49

nem seria obrigatório, mas é aquele conhecimento,

05:53

aquele fundamento que nos dá segurança.

05:56

Agora que você já sabe, você vai tomar decisão mais

06:02

assertiva. Se você estiver utilizando a inteligência

06:04

artificial para desenvolver com a ADK,

06:06

você vai olhar para isso e saber que...

06:10

tem os três modos e isso aqui pode trazer

06:12

um problema dependendo do rodeio que está acontecendo,

06:15

porque ele vai lá, faz a classificação,

06:17

depois o coordenador vai fazer a chamada da tool.

## Resumo IA

[RESUMO_IA]