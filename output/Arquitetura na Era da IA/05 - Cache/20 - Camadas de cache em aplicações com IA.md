Módulo: Arquitetura na Era da IA\
Aula: [Camadas de cache em aplicações com IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18356)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente fechou o fluxo do

00:04

cache semântico dentro do nosso analisador de tickets.

00:07

A aplicação já consegue tentar o cache exato,

00:12

depois o cache semântico,

00:14

e daí é só chamar IA quando nenhum desses dois tipos de cache acaba resolvendo.

00:20

Agora eu quero dar um passo para trás e organizar

00:23

isso como se fosse um mapa mais arquitetural.

00:26

onde o cache pode existir em uma aplicação com IA. Até aqui,

00:31

a maior parte do que a gente fez estava dentro da aplicação.

00:35

Primeiro como um cache exato,

00:37

usando o fingerprint, depois como um cache semântico,

00:41

usando embeddings, com o pgVector e o Threshold.

00:44

E esse cache dentro da aplicação é o mais importante para a decisão de negócio,

00:49

porque é ali que a gente sabe que a

00:52

gente está reutilizando em qual versão do prompt,

00:55

em qual versão da regra, em qual a capacidade do modelo e qual a política.

00:59

Esse ponto é essencial, porque o cache da aplicação não é só uma otimização técnica.

01:05

Ele conhece o significado da resposta.

01:07

Ele sabe se aquela classificação de ticket ainda faz sentido.

01:11

Ele sabe se aquele resultado pode ser devolvido diretamente

01:14

ou se precisa chamar algum modelo novo. Então,

01:17

quando a gente está falando de cache exato e cache semântico,

01:20

nós estamos falando de uma camada que participa da decisão do produto.

01:25

Mas essa não é a única camada possível.

01:28

Uma segunda chamada pode estar no gateway ou no proxy de A.

01:34

No capítulo anterior, a gente falou bastante sobre gateway, proxy, fallback e etc.

01:40

Essa chamada também pode ter algum tipo de cache,

01:44

só que o papel dela tende a ser diferente.

01:48

Um gateway normalmente enxerga chamadas passando por ele.

01:53

Ele pode aplicar regras mais transversais,

01:56

como limitar chamadas repetitivas, registrar uso, padronizar logs, controlar retry,

02:01

ou até evitar algumas chamadas muito óbvias dependendo da arquitetura.

02:05

Mas tenha um cuidado, o Gateway nem sempre conhece o domínio da aplicação.

02:11

Ele pode enxergar o prompt, o modelo, a rota,

02:14

os headers, o usuário, o custo, a latência,

02:17

mas talvez ele não saiba se aquela resposta

02:20

continua válida para uma regra específica dentro do negócio.

02:24

Por isso que o cache no gateway pode ser útil,

02:27

mas não deve automaticamente substituir a decisão de cache de dentro da aplicação.

02:34

A terceira camada é o cache do próprio provider.

02:39

Entram mecanismos como prompt caching, token caching ou cache de conteúdo,

02:44

dependendo do provider. A ideia geral é que partes repetidas,

02:51

vamos dizer assim, do prompt,

02:52

possam ser reaproveitadas para reduzir o custo ou a latência.

02:57

Só que isso é diferente do cache que a gente implementou.

03:01

Quando a aplicação retorna o cache exato ou semântico,

03:05

a chamada para o modelo de chat nem acontece.

03:08

Já o cache do provider, a chamada acontece ainda normalmente.

03:13

O provider apenas consegue reaproveitar uma parte do processamento.

03:18

Porque ele já conhece o começo do prompt,

03:21

e também muitas vezes quando o conteúdo é grande.

03:25

Então ele já viu que aquele conteúdo apareceu antes.

03:28

Então nesse caso a pergunta muda.

03:31

No cache da aplicação, a pergunta é: eu preciso chamar a IA?

03:36

Agora, no cache do provider, a pergunta é: já que eu vou chamar a IA,

03:41

existe alguma parte dessa entrada que o provider consegue reaproveitar?

03:47

E essa diferença parece pequena, mas ela muda bastante também a arquitetura.

03:53

Por exemplo, se sua aplicação tem um prompt grande com instruções fixas,

03:57

regras, exemplos de pedaços de variáveis no final,

04:00

por exemplo, o cache do provider pode ajudar bastante.

04:04

Mas se você quer evitar completamente uma nova

04:07

chamada porque aquela resposta já foi calculada,

04:10

isso continua sendo responsabilidade da aplicação ou de uma chamada sua.

04:16

Então, quando a gente fala em camadas de cache em aplicações com IA,

04:20

não é para a gente sair colocando cache em todo lugar.

04:23

É para a gente conseguir entender o papel de cada camada.

04:29

A aplicação boa para cachear decisões e respostas com contexto de negócio,

04:35

essa camada de aplicação é fantástica.

04:38

O gateway é bom para controle transversal das chamadas.

04:42

E o provider é bom para otimizar partes repetidas

04:46

do prompt que continuam passando por ele.

04:48

O erro seria então tentar tratar...

04:51

todas essas camadas como se elas fossem a mesma coisa.

04:54

Então, se eu acho que o cache do provider resolve o problema de cache de resposta,

04:58

eu posso continuar apagando chamadas desnecessárias.

05:01

Se eu coloco o cache no gateway sem considerar a versão ou a regra do prompt,

05:05

eu posso reutilizar a resposta em um contexto errado.

05:09

Se eu coloco tudo dentro da aplicação sem pensar em provider caching,

05:14

eu posso perder uma otimização importante em prompts

05:16

que são muito grandes e repetitivos.

05:19

Então, o ponto... essa aula é realmente organizar esse mapa. O cache,

05:24

ele não é uma única peça. Em aplicações com IA,

05:27

ele pode aparecer em lugares diferentes,

05:29

com responsabilidades diferentes.

05:31

O mais importante é você saber qual pergunta cada camada está respondendo.

05:38

A aplicação pergunta se pode realizar uma resposta,

05:41

o gateway ajuda a controlar, a padronizar chamadas e o provider,

05:44

ele tenta reaproveitar partes repetidas do nosso prompt. Beleza? Então,

05:50

na próxima aula, a gente segue por aí.

## Resumo IA

[RESUMO_IA]