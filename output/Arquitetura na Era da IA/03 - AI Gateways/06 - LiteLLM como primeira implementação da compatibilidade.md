Módulo: Arquitetura na Era da IA\
Aula: [LiteLLM como primeira implementação da compatibilidade](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18290)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente separou uma parte importante de Capability,

00:07

uma parte de capacidade dentro da ideia de AI Gateway,

00:10

que é a parte de compatibilidade.

00:12

Agora a gente vai olhar para uma ferramenta

00:14

que implementa muito bem essa primeira etapa,

00:16

que é o LightLLM.

00:18

E aqui eu quero que você enxergue o LightLLM

00:21

do jeito certo dentro dessa nossa sequência,

00:24

dessa nossa linha de raciocínio.

00:25

Ele não entra nesse módulo como mais uma biblioteca para chamar IA.

00:30

Também ele não entra como uma resposta final para todos os

00:33

problemas arquiteturais que a gente vai ter que discutir.

00:36

Ele entra como um primeiro passo prático para tirar

00:38

a aplicação do acoplamento direto com os providers. Ou seja...

00:42

O LightLLM nos ajuda a sair daquele cenário onde cada

00:45

integração conhece de mais um provider que está chamando.

00:48

A aplicação deixa de depender tanto do SDK específico,

00:52

do formato específico e da parte,

00:54

da diferença de integração entre os modelos. Então,

00:58

esse que é o papel dele nesse momento. Então,

01:01

ele cria uma interface mais comum para as chamadas de AI e por baixo...

01:05

ele faz a tradução para o provider real.

01:07

Então, quando você troca ou compara modelos,

01:10

a mudança tende a ficar muito mais controlada.

01:13

Mas o mais importante aqui é entender o posicionamento arquitetural.

01:17

O LightLLM pode aparecer em dois formatos. O primeiro é como SDK,

01:23

rodando dentro da nossa própria aplicação. Nesse caso,

01:26

ele funciona como uma camada local de compatibilidade.

01:29

A aplicação ainda carrega a dependência,

01:32

ainda executa a chamada a partir do próprio código,

01:35

mas já não conversa diretamente com cada SDK de provider.

01:39

E esse é o caminho mais simples para a gente começar.

01:42

Agora... O segundo formato é como proxy. Nesse caso,

01:46

o LightLLM roda como um serviço separado.

01:49

A aplicação passa a chamar esse serviço via HTTP e

01:52

aí começa a se aproximar mais de uma AI Gateway,

01:56

porque ele deixa de ser apenas uma dependência local

01:58

e passa a ser uma fronteira centralizada.

02:01

E essa diferença vai guiar a gente bastante nos próximos vídeos.

02:05

Primeiro, a gente tem que olhar o LightLLM como SDK. Então, a pergunta aqui é...

02:11

O que eu ganho quando o LightLLM dentro da minha aplicação vai me ajudar,

02:15

ou seja, sem criar uma infraestrutura nova?

02:17

E depois a gente vai olhar o LightLLM como um proxy e a pergunta muda.

02:21

O que acontece quando essa camada sai da aplicação e

02:25

vira um ponto central para várias chamadas de IA? Então,

02:28

essa sequência é importante porque evita ali uma bela de uma confusão.

02:32

Então, se eu uso o LightLLM como SDK,

02:34

eu melhoro a integração local. Se eu uso o LightLLM como proxy,

02:38

eu começo a criar uma camada compartilhada de acesso.

02:42

E se eu preciso de regras específicas de produto,

02:44

como fallback semântico, degradação,

02:47

revisão humana ou decisões de caso de uso,

02:49

aí a gente já entra num outro nível de arquitetura.

02:53

O grande ponto desse vídeo aqui é simples,

02:55

o LightLLM é a primeira ferramenta que a gente

02:57

vai usar para materializar essa ideia de compatibilidade,

03:00

mas também ele não fecha toda a nossa conversa sobre AI Gateway,

03:04

mas no final das contas ele vai aí criar uma

03:06

base muito boa para a gente conseguir avançar,

03:08

beleza? Então, vamos nessa!

## Resumo IA

[RESUMO_IA]