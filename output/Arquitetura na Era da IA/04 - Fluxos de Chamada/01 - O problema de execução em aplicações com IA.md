Módulo: Arquitetura na Era da IA\
Aula: [O problema de execução em aplicações com IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18311)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? No capítulo anterior a gente organizou, vamos dizer assim,

00:06

entendeu melhor como é que a gente faz integrações com diversos modelos,

00:12

tendo de forma geral uma camada de abstração um pouco maior para a gente trabalhar

00:18

com compatibilidade ou eventualmente um componente novo como

00:22

uma AI Gateway ou algo desse tipo.

00:24

Então isso nos ajudou a gente falar sobre controlar um pouco mais a... as chamadas,

00:30

a gente entendeu um processo de fallback,

00:32

tem um mínimo ali de governança de forma geral, tá?

00:35

Mas, quando esse tipo de coisa existe,

00:40

começa a aparecer uma nova pergunta no meio de tudo isso, que é,

00:44

como que essa chamada que a gente faz, né,

00:47

pra IA, ela entra no fluxo real do nosso software.

00:51

Porque uma coisa é a gente conseguir chamar o modelo de forma organizada.

00:55

Outra coisa é decidir se o usuário vai esperar a resposta na hora,

01:01

se ele vai acompanhar a resposta chegando em partes,

01:03

ou se aquilo deveria ficar sem um processo, vamos dizer assim, em background.

01:08

Então, esse é o ponto central desse capítulo.

01:12

Quando a gente desenvolve uma aplicação tradicional,

01:15

principalmente uma aplicação web, é muito comum pensar em um request

01:19

e response. O usuário faz uma ação, a aplicação recebe a requisição,

01:23

processa alguma coisa, talvez busca alguma coisa no banco de dados,

01:27

chama uma API externa, monta uma resposta e devolve. Então,

01:31

esse é o fluxo muito natural para muita coisa que a gente está acostumado.

01:34

Ele funciona muito bem para criar cadastro, fazer busca,

01:38

atualizar registro, aplicar regra de negócio mais direta. Agora,

01:43

quando a gente faz uma chamada para IA, vamos dizer assim, nem sempre...

01:49

essas chamadas vão se comportar como a gente está acostumado nessas chamadas comuns.

01:55

Às vezes ela vai responder rápido,

01:57

às vezes ela vai demorar um pouco mais, às vezes as respostas vêm em partes,

02:01

às vezes a IA precisa analisar um texto maior,

02:04

gerar uma explicação, resumir documento, processar várias informações,

02:09

construir uma resposta mais elaborada.

02:11

E se a gente tratar tudo isso sempre da mesma forma,

02:15

como se fosse apenas mais uma chamada bloqueante dentro de uma requisição,

02:19

a experiência ali para o usuário começa a ficar muito ruim.

02:23

O usuário clica no botão e fica esperando, a tela não dá feedback,

02:26

o back-end segura a conexão, o tempo vai passando, pode estourar o timeout,

02:31

a pessoa, sei lá, pode clicar de novo achando que não funcionou,

02:35

a aplicação, sei lá, gera e replica a mesma tarefa, ou seja...

02:40

a gente começa a ter um problema no fluxo de como que é desenhado em torno da IA.

02:46

Então aqui a discussão não é sobre qual modelo utilizar,

02:49

também não é sobre qual provider, gateway ou fallback entre modelos.

02:54

Isso aí já ficou bem claro para a gente no outro capítulo. A pergunta aqui é outra.

02:58

Qual fluxo é o fluxo de execução correto

03:02

para determinada feature que eu vou utilizar utilizando IA?

03:07

Em alguns casos, uma chamada assíncrona faz sentido. Por exemplo,

03:10

se a aplicação recebe um ticket de suporte e

03:12

só precisa classificar rapidamente aquele ticket como cobrança,

03:16

como suporte técnico, como uma dúvida comercial.

03:18

Talvez faça sentido a gente esperar a resposta e devolver um JSON logo em seguida.

03:23

Agora, se a IA vai gerar uma explicação mais longa para o usuário,

03:26

talvez um streaming seja uma opção melhor. Não porque a IA ficou mais rápida,

03:31

mas porque a percepção que o usuário tem vai mudar.

03:34

O usuário começa a ver alguma coisa já acontecendo.

03:37

A resposta começa a aparecer aos poucos e isso aí já melhora bastante a experiência.

03:42

E aí a gente tem casos que nem o síncrono,

03:45

nem com o streaming vai nos ajudar. Na realidade,

03:49

a aplicação às vezes vai analisar um documento muito

03:51

grande e ter que gerar um relatório.

03:53

E aí, nesse caso,

03:54

talvez seja certo a gente criar um job,

03:56

jogar para uma fila ou alguma coisa desse tipo,

03:59

processar em background e depois a gente dá um jeito do usuário acompanhar.

04:04

Isso não é nenhuma novidade quando a gente tem que

04:07

trabalhar com requisições mais pesadas dos dias de hoje.

04:11

Então, você consegue perceber como é que essa

04:13

discussão acaba mudando no meio dessa história?

04:16

Uma feature com IA pode até funcionar tecnicamente da forma como a gente faz,

04:20

mas, na prática, para o usuário final,

04:23

a percepção é diferente e aí que a gente tem que tomar cuidado.

04:27

Então, no próximo vídeo,

04:28

a gente vai começar pelo caso mais simples, que é uma chamada assíncrona. Tem o seu lugar,

04:34

mas a gente precisa entender bem quando faz sentido

04:37

e quando ela começa a virar um problema.

04:40

Beleza? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]