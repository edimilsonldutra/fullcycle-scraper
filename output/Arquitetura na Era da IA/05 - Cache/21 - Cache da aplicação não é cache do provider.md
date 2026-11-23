Módulo: Arquitetura na Era da IA\
Aula: [Cache da aplicação não é cache do provider](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18357)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente organizou as camadas onde o

00:05

cache pode aparecer em uma aplicação com IA.

00:07

A gente falou do cache dentro da aplicação,

00:10

do cache em uma camada de gateway ou um proxy e

00:13

também do cache que pode acontecer no próprio provider.

00:16

Agora eu quero separar melhor uma confusão comum.

00:21

Cache da aplicação e cache do provider não resolvem o mesmo problema.

00:26

Essa diferença é importante porque se a gente misturar as duas coisas,

00:29

a arquitetura começa a ficar confusa.

00:32

Você pode achar que está economizando chamadas para IA,

00:35

quando na verdade só está reduzindo parte do custo daquela chamada.

00:39

Ou pode achar que o provider está protegendo sua regra de negócio,

00:43

quando na realidade ele não sabe nada sobre o

00:46

significado daquela resposta dentro da sua aplicação.

00:49

Então vamos começar pelo cache da aplicação.

00:52

Quando a nossa aplicação retorna uma resposta do cache exato ou do cache semântico,

00:57

o modelo de chat não é chamado.

00:59

O fluxo para antes disso aí. A aplicação olha para o que já tem,

01:04

decide que aquilo pode ser reaproveitado e devolve ali a resposta.

01:09

Nesse caso, o cache é uma decisão do sistema.

01:13

Foi isso que a gente implementou no nosso analisador de tickets.

01:16

Se a mesma mensagem chega com o mesmo fingerprint...

01:19

vem do cache exato, se a mensagem diferente chega,

01:22

mas ela é parecida o suficiente com uma resposta anterior,

01:26

dentro do mesmo fingerprint, e é acima do threshold,

01:29

ela pode vir do cache semântico.

01:31

Nos dois casos, a aplicação está dizendo,

01:34

eu já tenho uma resposta válida para isso. Agora,

01:38

o cache do provider, ele tem uma outra natureza.

01:41

No cache do provider, normalmente, a chamada ainda acontece.

01:46

A aplicação ainda envia... uma requisição para OpenAI,

01:49

para o Gemini, para o Anthropic ou outro provider.

01:51

O que acontece é que o provider reconhece uma parte

01:55

repetida do prompt e consegue reaproveitar

01:58

internamente algum processamento daquela parte.

02:02

E então o benefício é diferente.

02:04

Você pode ter redução de latência,

02:07

redução de custo de input ou algum ganho

02:10

quando usa prompts grandes com partes fixas.

02:13

Mas você não eliminou completamente a chamada.

02:17

O provider ainda está no caminho. A rede existe,

02:21

a dependência externa ainda também existe, o modelo ainda vai gerar uma resposta.

02:26

Por isso que a pergunta muda.

02:28

No cache da aplicação, a pergunta é, eu preciso chamar o modelo?

02:31

No cache do provider, a pergunta é,

02:34

já que eu vou chamar o modelo,

02:35

existe alguma parte repetida que o provider consegue reaproveitar?

02:39

Essa distinção parece simples,

02:41

mas ela muda o desenho do sistema.

02:42

Se o objetivo é evitar uma chamada repetitiva para que a resposta,

02:46

porque a resposta já foi calculada e continua válida,

02:49

isso é um cache de aplicação. Se o objetivo é otimizar prompts longos,

02:54

com uma parte estática, que grande parte disso acaba não variando, vamos dizer assim,

03:00

aí o cache do provedor pode ajudar. Um outro ponto é o controle.

03:05

No cache da aplicação, você controla a chave,

03:08

você controla o fingerprint, você sabe qual versão do prompt gerou aquela resposta,

03:13

você sabe qual a versão das regras que estão ativas,

03:16

você consegue decidir o que entra e o que não entra no cache,

03:21

você consegue invalidar,

03:22

você consegue auditar, você consegue retornar o payload que é a origem,

03:26

se a origem foi de cache de execução,

03:28

se foi de cache semântico ou se foi de AI model. Agora, no cache do provedor,

03:34

parte desse controle muda de lugar. Você depende do comportamento do provedor,

03:39

das regras dele, do modelo usado, do tamanho do prompt,

03:43

da forma como ele identifica partes repetitivas e também da

03:47

forma de como ele expõe essas informações de utilização da resposta.

03:52

Isso não é ruim. Ele só não é basicamente a mesma coisa.

03:56

Na prática, os dois podem conviver.

03:58

Imagina um sistema com prompt grande, cheio de instrução fixa,

04:02

exemplos de classificação e regras de formato.

04:05

Mesmo quando a aplicação precisa chamar um modelo,

04:08

pode ser interessante estruturar esse prompt de forma, vamos dizer, cache-friendly,

04:13

para que o provedor consiga reaproveitar o prefixo fixo.

04:19

Mas se a resposta inteira já foi gerada antes e continua válida,

04:24

talvez a melhor decisão nem seja... chamar o provedor. Então,

04:28

a camada da aplicação continua sendo a principal

04:32

quando falamos de reutilização de resposta.

04:35

O cache do provedor entra na otimização complementar

04:39

para as chamadas que ainda precisam acontecer.

04:42

Tem também uma consequência para a observabilidade.

04:45

Se a resposta veio do cache da aplicação,

04:47

a aplicação sabe disso claramente.

04:50

Ela pode registrar que não houve chamada ao modelo,

04:53

que a resposta veio do cache exato ou do cache semântico,

04:57

qual chave foi utilizada, em qual tempo retornou e etc.

05:00

No cache do provedor,

05:02

a aplicação precisa olhar para os metadados retornados da chamada,

05:06

quando eles existem,

05:08

e mesmo assim, a leitura é outra.

05:11

Você não está medindo... evitei uma chamada. Você está medindo.

05:15

Chamei o provedor, mas parte da entrada foi reaproveitada.

05:19

Então, quando vamos falar de cache de provedor,

05:21

o foco não será substituir o que a gente fez até aqui.

05:24

O foco vai ser entender como escrever prompts e estruturar

05:28

chamadas para aproveitar melhor essa camada quando ela fizer sentido.

05:33

Vamos dizer assim, o ponto é para guardar essa ideia, como que eu posso dizer?

05:41

O cache da aplicação decide se a chamada deve acontecer.

05:44

Cache do provedor otimiza a chamada que ainda vai acontecer.

05:48

Aí na próxima aula a gente vai olhar como os principais

05:52

Providers tratam desse tipo de prompt caching para que você possa, vamos dizer,

05:58

entender a utilização e saber quando trabalhar com cache de providers

06:03

dependendo dos principais providers que a gente tem aí no mercado.

06:07

Beleza? Então vamos nessa.

## Resumo IA

[RESUMO_IA]