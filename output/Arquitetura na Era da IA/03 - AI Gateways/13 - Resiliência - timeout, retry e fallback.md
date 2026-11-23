Módulo: Arquitetura na Era da IA\
Aula: [Resiliência - timeout, retry e fallback](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18297)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

Agora que a gente falou sobre capacidades internas, acesso, custo, limite,

00:06

a gente precisa olhar para um outro ponto importante de uma gateway,

00:09

que é a resiliência. Quando uma aplicação começa a depender de modelos de AI,

00:14

ela também passa a depender de disponibilidade,

00:16

da latência e dos limites dos providers.

00:19

E isso precisa ser considerado ali muito no desenho.

00:22

A primeira peça aqui é o timeout.

00:24

Timeout é uma decisão simples, mas assim, é muito importante.

00:28

A aplicação não pode ficar esperando indefinidamente uma resposta do modelo.

00:33

Se o provider demora demais, se a rede oscila,

00:36

se o modelo está lento,

00:37

em algum momento o sistema precisa decidir que

00:40

aquela chamada passou do tempo aceitável.

00:42

Mas esse tempo aceitável muda conforme o caso de uso.

00:46

Uma resposta em uma tela de atendimento talvez precise voltar rápida.

00:50

Uma análise longa de um documento talvez possa demorar um pouquinho mais.

00:54

Um processo em lote pode talvez rodar ali em segundo plano.

00:58

Então o timeout não deveria ser um número aleatório igual para tudo.

01:02

Depois disso vem retry. Retry é tentar novamente...

01:07

quando uma falha aparece temporária.

01:09

Então, por exemplo, a gente tem uma oscilação de rede,

01:12

um erro transitório do provider,

01:14

um limite momentâneo ali que teve alguma falha e,

01:18

de forma geral, essa falha desaparece alguns segundos depois.

01:23

Mas o retry também precisa de critério. Se você tenta de novo sem pensar,

01:28

pode piorar o problema. Você aumenta a latência,

01:30

aumenta custo e ainda coloca mais pressão em um provider que, às vezes,

01:34

já está falhando. Então, o retry... precisa ter limite,

01:38

você precisa ter tempo entre tentativas,

01:41

você precisa fazer sentido no final das contas

01:44

para aquele fluxo que você está trabalhando.

01:47

E depois disso vem o famoso fallback técnico, o fallback. O fallback é uma...

01:53

tentativa de um outro caminho quando o caminho principal acaba falhando.

01:57

Então, pode ser um modelo, um outro deployment,

02:00

um outro provider ou alguma outra configuração. Então, isso é útil,

02:04

porque ele evita que uma chamada pontual derrube tudo. Mas, em IA,

02:09

um cuidado que a gente não pode ignorar.

02:13

Trocar o caminho técnico não garante que...

02:17

a mesma resposta vai ser equivalente. Então,

02:20

se você troca de um modelo para o outro, a chamada pode funcionar,

02:23

mas a resposta pode mudar de qualidade, de formato,

02:27

de estilo e de comportamento. Então, um modelo pode seguir melhor uma instrução,

02:31

o outro pode lidar melhor com o JSON,

02:34

o outro pode melhorar a sua parte de velocidade, mas ser pior, sei lá,

02:39

numa análise mais aprofundada. Então,

02:42

o fallback técnico responde apenas uma pergunta.

02:46

Eu consegui tentar outro caminho?

02:49

E ele responde sozinho ali. Essa nova resposta ainda é boa para esse caso de uso,

02:55

entende? Então, a questão é ali. Não consegui,

02:58

Deixa eu tentar para esse caminho, mas esse caminho que eu vou tentar,

03:01

A resposta que ele vai trazer é boa o suficiente?

03:05

E a segunda pergunta já entra em política arquitetural.

03:08

E isso é o que a gente vai discutir, inclusive, nos próximos vídeos. Por enquanto,

03:12

O ponto é entender que uma gateway

03:14

Pode concentrar mecanismos importantes de resiliência.

03:18

Ela pode aplicar timeout,

03:20

Pode fazer o retry, pode... fazer políticas de fallback, registrar falhas e etc.

03:25

Mas muitos desses mecanismos precisam ser usados com intenção. Não são números,

03:31

Isso não pode sair chutado da sua cabeça.

03:34

E é por isso que conhecimento em arquitetura,

03:37

De forma geral, faz muita diferença. Porque isso acaba mudando também,

03:41

Não somente a parte financeira, mas muda a infraestrutura e também a aplicabilidade,

03:48

A utilização da aplicação para o usuário final. Então a ideia é,

03:53

Uma gateway não serve apenas para encaminhar chamadas,

03:56

Ela também ajuda a proteger o sistema contra falhas,

03:59

Lentidão e responsabilidade. Mas ali o limite continua muito claro,

04:03

A ferramenta sempre vai poder fazer um fallback. O grande ponto aqui é,

04:07

Para onde a gente vai fazer esse fallback? Será que é possível?

04:11

Será que a gente pode degradar? Uma resposta e fazer alguma coisa a mais. Então,

04:15

Essas decisões que acabam sempre entrando e diferenciando,

04:20

Na realidade, um desenvolvedor, um arquiteto de outro.

04:22

Porque, no final das contas, isso aí, no mundo da IA, faz muita diferença.

## Resumo IA

[RESUMO_IA]