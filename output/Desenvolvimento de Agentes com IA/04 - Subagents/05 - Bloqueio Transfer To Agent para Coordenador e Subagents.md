Módulo: Desenvolvimento de Agentes com IA\
Aula: [Bloqueio Transfer To Agent para Coordenador e Subagents](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18260)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre controlar o comportamento de como

00:05

pode ser delegado para outro agente poder assumir o controle.

00:11

Nós tivemos um comportamento interessante na última aula,

00:14

em que nós iniciamos com 'quero cancelar minha assinatura', do

00:20

agente operador de conta passou a bola para o consultor de assinatura,

00:24

teve aquela questão do tool confirmation.

00:28

Depois que terminou o processamento, nós pedimos para listar as minhas faturas,

00:33

ou seja, um outro subagente que vai ser especialista em fazer isso.

00:39

Então, ele delegou direto para o irmão dele, que é o consultor de faturas.

00:45

Ele não precisou passar pelo operador da conta.

00:48

Então, assinatura delegou para o consultor de faturas.

00:53

Então, nós podemos ter, como já foi falado,

00:55

de um subagente... delegar o controle para outro.

01:02

Ele pode até delegar para algum filho dele, que é outro subagente dele mesmo, que

01:08

está cadastrado nele. Ou ele pode voltar para o coordenador,

01:14

aí o coordenador processa alguma coisa e vai para o subagente,

01:17

até que isso fique satisfeito e uma resposta aconteça.

01:24

Mas nós podemos querer fazer um controle,

01:28

mas...

01:32

Restrito. Nós temos esse autoflow, às vezes o autoflow pode não ser interessante.

01:39

Então, por exemplo, se nós chegarmos aqui no cancelar minha assinatura,

01:46

podemos proibir que ele faça a delegação direta para irmãos dele.

01:51

Então, vamos colocar aqui, disallow,

01:55

transfer to peers, igual a true.

02:00

Então, estou negando o padrão, isso aqui é falso.

02:04

Da mesma forma, se

02:08

eu quiser centralizar tudo no meu agente coordenador,

02:11

coloco também no listar faturas.

02:15

Vamos realizar um novo teste. Vou

02:21

colocar listar minhas faturas.

02:26

Já vai delegar para o subagente.

02:32

Então vai listar as faturas. Mas agora eu quero

02:37

cancelar minha

02:40

assinatura. Veja só.

02:49

Ele fez o transfer to agent para o operador da conta.

02:56

E o operador da conta depois fez o transfer

02:59

to agent para o consultor de assinaturas.

03:02

Aí vem todo aquele processo.

03:05

Então aqui nós já podemos ver esse procedimento.

03:19

Aqui eu estou no operador da conta. É a primeira chamada que nós

03:27

temos permissão. Ele vai mostrar os dois subagentes. Tudo ok.

03:34

No transfer to agent, que é passado lá para o LLM,

03:37

ele está falando que você pode usar um ou outro. Ok.

03:42

Mas aí depois que tivemos o nosso resultado chegando aqui, aqui

03:48

nós já estamos no cancelar, na verdade aqui eu estou no listar,

03:54

na verdade o consultor de faturas, né? Nós mudamos para ele.

03:59

Então veja que

04:00

mudou o prompt que é passado.

04:10

Eu tenho a descrição.

04:12

Até mesmo agora, toda vez que é passado, a descrição é acrescentada também.

04:16

Isso até nós não tínhamos frisado na última aula.

04:20

Então, ele só libera o operador da conta.

04:26

E aqui embaixo também só tem essa opção.

04:29

Então, veja, tudo é algo abstrato.

04:34

Nós estamos criando esse ciclo com base no system prompt que é passado para a LLM.

04:41

E nós, como agentes, só obedecemos. Da mesma forma...

04:46

Se eu passasse aqui, agora que eu quero listar as minhas faturas,

04:52

ele iria mostrar somente o operador da conta de novo. Temos também o

04:58

disallowTransferToParent.

05:03

E ele pode ter, na verdade, ele tem uma interpretação dúbia,

05:07

porque se nós entendemos que ToPears não vai

05:10

listar ali os outros irmãozinhos dele para transferir,

05:15

ele vai fazer a mesma coisa por parent. E, na verdade, é isso. Ele vai

05:20

impedir que a

05:24

gente seja transferida para o pai, mas,

05:29

na verdade, ele vai obrigar a

05:34

transferência para o

05:41

coordenador, vou colocar root agent, no próximo turno.

05:52

Vamos rodar mais uma vez.

05:56

Então, eu quero

05:59

listar minhas faturas, ID

06:07

do cliente, e veja só.

06:14

Aqui nós vemos que ele mudou para o consultor de faturas e

06:19

depois voltou para o operador da conta. Aí ele coloca que, como

06:26

sou operador da conta, vi que você está sendo atendido pelo especialista de faturas.

06:30

Ele solicitou o seu ID para progredir e dar continuidade.

06:34

Obviamente, aqui nós vamos ficar presos. Mas veja só,

06:39

se colocarmos assim, quero listar minhas faturas.

06:45

E meu client ID é 223.

06:53

Porque como eu já passei todas as informações, aí sim ele vai conseguir fazer o

07:00

que é executado. Então, o ponto dessa configuração é

07:09

que em algumas situações nós podemos ficar nesse jogo de vai para o subagente, vai

07:17

para o parent. Então, o usuário fica preso.

07:24

Na verdade, também o two peers acaba sendo... Nesse sentido.

07:29

Nós podemos até usar um modelo melhor, que

07:33

o comportamento também pode melhorar um pouco. Então, usando esse modelo 3

07:44

.5, e não é o Lite, ele vai ser um pouquinho melhor, veja só.

07:52

Então, listar minhas faturas, somente sem o ID, ele vai pedir o ID. Então, agora,

08:01

cliente 1, 2, 3, aí sim.

08:09

Então, o modelo também influencia nesse ponto.

08:18

Nós podemos ter uma resposta vazia.

08:23

E também, como eu já havia falado,

08:26

nós temos que prestar atenção nas novas versões do ADK,

08:31

porque esse comportamento aqui é o comportamento que, dependendo do modelo,

08:35

ele pode ter aquela resposta invasiva, mas ele vai

08:42

sendo melhorado ao longo do tempo. Então, dessa forma,

08:45

veja só, nós até não fizemos a inspeção.

08:49

Quando nós ditamos aqui o cliente 123,

08:52

que o controle já foi passado para o consultor de faturas, exatamente aqui,

09:07

veja que o operador não

09:13

Aparece aqui mais.

09:15

Mas o ponto é que se eu mandar um obrigado, o

09:20

controle não vai mais ficar com a gente.

09:24

Quando eu mandei esse obrigado, está

09:32

vendo que o system prompt quer passado? Porque quando ele é acionado novamente e...

09:39

Dado que aconteceu o turno da interação,

09:42

nós vamos ter uma nova interação ou a

09:46

gente vai acabar obrigando o coordenador a assumir novamente.

09:51

Aí ele pode fazer a transferência e etc.

09:56

Então, em muitas situações, a gente faz esse controle para travar o comportamento,

10:01

para que ele seja mais restrito.

10:06

Em algumas situações vai ser interessante. Então, com isso aqui a gente fecha.

10:10

Esse comportamento básico dos subagentes.

## Resumo IA

[RESUMO_IA]