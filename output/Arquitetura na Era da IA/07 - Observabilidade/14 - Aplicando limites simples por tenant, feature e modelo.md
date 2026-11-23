Módulo: Arquitetura na Era da IA\
Aula: [Aplicando limites simples por tenant, feature e modelo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18761)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, agora trazendo mais um exemplo aqui mais prático

00:05

para a gente falar sobre essa parte de modelos,

00:08

governança e limites que a gente pode colocar no nosso sistema,

00:12

tá? Obviamente, o exemplo que eu quero trazer aqui é simples,

00:16

mas a ideia é que você entenda o conceito,

00:19

tá? Uma das coisas que é super comum,

00:22

e isso você vai encontrar em qualquer local que você vai trabalhar,

00:25

ou empresas, etc.,

00:27

que é algo já convenção, é algo chamado de Allowed List.

00:31

Basicamente, é a listagem dos modelos que você pode trabalhar.

00:35

Então, se no seu sistema você não tem isso, é super importante,

00:40

porque no final das contas você consegue colocar uma trava.

00:44

Então, se você olhar aqui,

00:45

eu coloquei AI Allowed Models,

00:47

então eu posso colocar quais são os modelos que eu permito,

00:50

quanto que eu posso ter de budget,

00:52

ou seja, quanto que eu posso gastar,

00:54

quanto que eu tenho de output tokens que eu posso

00:56

colocar no máximo e aonde que eu quero...

01:00

guardar nesse caso aqui, é chamado de ledger,

01:03

mas basicamente nesse caso eu estou gerando no formato de um JSON,

01:07

que tem todas essas informações,

01:09

e isso aí obviamente você colocaria isso num banco de dados,

01:12

eu não tenho necessidade de colocar num banco de dados.

01:15

Agora o ponto importante aqui para vocês é claro,

01:18

normalmente esse tipo de coisa você pode colocar no seu sistema como se fosse,

01:23

sabe quando você tem...

01:26

Sistemas que têm a parte de autorização e autenticação. E na parte de autorização,

01:31

você pode escolher esse usuário, pode fazer isso nessa ação e tudo mais.

01:37

Então, é quase que o mesmo conceito. Você pode falar,

01:41

essa feature pode usar esse modelo com budget digital.

01:45

Essa tool calling pode ser utilizada, chamada três vezes.

01:49

Esse modelo, para esse tipo de uso,

01:52

pode trabalhar com o máximo de output tokens de 1.200.

01:56

Entende? Então, toda vez que você vai arquitetar o seu sistema,

02:00

você vai ter que pensar, nesse sistema, onde a IA vai ser utilizada?

02:05

E o segundo passo é, nesse caso,

02:07

onde que eu vou colocar as minhas restrições,

02:11

os meus bloqueios? Porque isso evita...

02:15

claramente, de catástrofes acontecendo, de dados vazarem,

02:17

mas principalmente também nesses casos,

02:19

de qual modelo que vai usar,

02:21

de qual o orçamento. Então, eu posso falar, olha,

02:23

para esse tipo de cliente premium, eu posso...

02:26

ter um budget de tanto e o output pode ser maior. Então, você escolhe,

02:30

mas é importante que você tenha em mente que

02:33

você precisa de uma espécie de uma matriz,

02:35

dependendo do sistema,

02:36

para você conseguir definir quais agentes, quais tools, quais etapas,

02:40

qual pipeline que você vai poder utilizar baseado

02:43

Nas ferramentas ali que você vai ter.

02:45

Beleza? Então, aqui são as minhas variáveis de ambiente.

02:49

No meu próximo vídeo, eu vou... Somente para esse vídeo aqui não ficar grande,

02:53

eu vou... rodar aqui alguns exemplos, somente para a gente ver,

02:56

mas a ideia principal é essa,

02:58

você conseguir colocar restrições e fazer com que a

03:01

aplicação ela trabalhe em cima dentro dessas restrições, fechou?

## Resumo IA

[RESUMO_IA]