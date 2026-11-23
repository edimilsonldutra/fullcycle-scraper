Módulo: DevOps e SRE com IA\
Aula: [Observabilidade de Agentes pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18537)

## Resumo da aula



## Transcrição

00:00

Então, vamos lá, vamos fazer aquele teste lá dentro daquele agent que a gente criou,

00:05

Kubernetes Trash World, troubleshooters, na verdade.

00:09

Vamos perguntar aqui, listar quais são meus

00:14

pods dentro

00:21

do meu

00:23

namespace de observabilidade. Vamos ver.

00:32

Ele vai fazer a chamada aqui das funções.

00:35

Em teoria vai fazer essa chamada e passar lá para o Langfield já.

00:38

Assim que ele começar a processar.

00:42

Ok. Fez a primeira chamada. A gente já tem o tracing aqui. O pré-tracing.

00:46

Que provavelmente é 8 e 10.

00:51

8 e 10. Está aqui. A gente já tem um pré-tracing aqui. List.

00:55

E provavelmente esse trace agora já foi atualizado porque a resposta já veio.

00:59

Então vamos pegar aqui.

01:02

Ele listou para mim quais são os meus pods lá dentro.

01:07

Vamos dar uma olhada? Ah, ele colocou aqui todos os detalhes para mim,

01:11

então o list que teve, etc.

01:13

E minha resposta está tudo aqui, bem descrito, com os dias, horários,

01:19

todas essas partes aqui que a gente tem lá dentro da geração.

01:26

E aqui o LLM Response, que é a parte de Intimidation. Então está tudo...

01:31

bem descrito aqui para a gente conseguir ver o que está acontecendo,

01:36

tá? Deixa eu ver se tem uma parte de tools aqui.

01:40

Tool aqui, tool call. A gente consegue ver as tools aqui.

01:44

Namespace, olha lá. Então ele mostrou aqui que ele fez a chamada dessa tool.

01:49

Então a gente tem aqui a tool, olha lá.

01:51

Todas as tools que ele fez a chamada estão descritas aqui no metadata. Entendeu?

01:56

O script está bem simples, se você quiser aprimorar ele,

02:00

colocar mais pontos ali de entrada do LingFuse, é possível também,

02:04

porque o LingFuse tem várias outras possibilidades,

02:07

você conseguir rastrear sessões de usuário também,

02:09

então você consegue ver a sessão completa do usuário,

02:12

aqui a gente tem a sessão, está vendo?

02:14

Aqui a gente tem também a sessão, a primeira sessão que eu fiz,

02:17

então a gente consegue ver, vamos ver se está certinha a sessão?

02:21

Então vamos ver qual,

02:24

vamos lá, vou perguntar.

02:27

Pegar o status deles, vou pedir para ele pegar o status dele aqui, dos meus pods.

02:36

Ok, está listando, pegando o resource, está fazendo cinco chamadas de tools aqui,

02:41

e pegando o status de cada um dos meus pods aqui.

02:46

Ok, temos os status, running,

02:49

pod 1 de 1, 5 de antes, detalhes do pod,

02:53

tempo, aqui tem vários detalhes do meu pod.

02:56

Então, ele pegou só o do tempo, não sei porquê.

03:00

Provavelmente por causa de contexto, tamanho de contexto.

03:04

Prometheus, engraçado, ele pegou só o do tempo, mas não tem problema.

03:09

Aqui a gente pode olhar que ele atualizou a sessão.

03:14

Vamos pegar nossa sessão aqui.

03:16

A gente tem atualizado aqui o

03:19

nosso detalhe do que aconteceu.

03:24

Então a gente tem uma sessão completa com todos os

03:26

Dados aqui que foram enviados e assim por diante.

03:29

Legal? Então, a gente vê em Traces aqui, vamos pegar,

03:34

aqui tem uma latência e a gente consegue ver o chat completo.

03:38

A primeira pergunta que eu fiz,

03:39

aqui a resposta, a segunda pergunta que eu fiz, aqui a resposta e assim por diante.

03:44

Então, a gente consegue ter uma rastreabilidade 100% aqui. Além de conseguir criar,

03:50

essa versão não tem, mas na versão mais nova tem o LLMT Django.

03:56

onde a gente consegue fazer, as duties, né? Que a gente consegue fazer,

04:01

julgar com o outro LLM se aquela resposta foi ok,

04:05

se aquela resposta foi como esperado e assim por diante, tá bom?

04:10

Então a gente consegue fazer tudo isso aqui, tá? Ah,

04:13

e na última aula, faltou eu criar o agent do Prometheus.

04:16

Deixei essa missão pra vocês aí,

04:18

mas vamos criar ele aqui agora, pra gente validar o Prometheus.

04:22

Temos aqui a ferramenta dele.

04:24

O prompt dele. Vamos colocar aqui. O prompt dele.

04:30

Vou mandar para vocês também. Vai estar disponível.

04:32

A gente vai selecionar nosso modelo 3.5.

04:35

E vamos dar o nome dele aqui de Prometheus Analyst.

04:42

Prometheus Analyst. Analyst. Ok.

04:51

Prometheus Analyst.

04:53

Então a gente vai ter aqui o modelo, já selecionamos,

04:56

a gente vai colocar só aqui o padrão de função,

05:01

padrão, chamado de função,

05:03

colocamos ali e vamos selecionar a ferramenta Prometheus aqui.

05:07

Então vamos falar com ela agora.

05:10

Vamos fazer alguma pergunta aqui de Prometheus?

05:16

Quero saber, deixa

05:19

eu ver aqui uma pergunta interessante.

05:22

que a gente pode fazer quero saber

05:26

quero

05:30

saber o server duration em

05:37

milissegundos do

05:42

meu sistema app

05:46

api vamos ver se

05:49

ele vai me entregar esse resultado vamos

05:54

esperar lembrando que o tracer já está indo lá para o link fiz também

06:04

Not found. Ele conseguiu achar mais algumas coisas aqui. Query range.

06:12

Targets. Está puxando algumas coisas para a gente aqui. Vamos ver.

06:22

Conseguiu achar alguma coisa. Hotel collector.

06:24

Job. API.

06:27

Conseguiu achar aqui.

06:30

Vamos ver o que a gente tem.

06:41

Ficou lento aqui. Será que o LLM já está agarrando aqui de novo? Pode

06:46

ser que sim. Vamos

06:50

ver aqui o LLM Studio.

06:53

Não, ele está processando ele ali não. Quem ficou lento agora foi o OpenAPI. Vou

07:03

recadar na página aqui e ver o que ele vai fazer. Vamos

07:12

dar uma olhada aqui na nossa stack.

07:18

Vamos ver nossos pods.

07:21

Olha, o OpenAPI, o LingFuse reiniciou duas vezes aqui.

07:25

Tivemos algum probleminha no LingFuse.

07:28

Reach from project grid only.

07:31

Mas o OpenAPI está de pé. Cadê ele?

07:37

Open UI. Está aqui embaixo. Está de pé.

07:41

Só que ele teve um probleminha.

07:44

Vamos ver qual foi o probleminha. Open UI.

07:58

Vamos tirar ele aqui. Tentar ir para a primeira página.

08:02

Acho que ele deu uma travada geral aqui. Morreu.

08:06

Acontece. Acontece na metade da demo. Vamos lá. Vamos reiniciar ele.

08:13

Já que não quer funcionar, a gente aplica a solução aqui de reiniciar.

08:19

Ele morreu de vez. Ok.

08:25

Temos ele de volta. Vamos ver.

08:29

Está explicada a memória do sistema.

08:33

Está lá no talo.

08:35

Vamos ejetar aqui. E subir de novo. E

08:42

colocar um contexto um pouquinho maior aqui. 15 mil.

08:46

Colocar esse aqui. E vamos subir o modelo de novo. Vamos

08:52

voltar aqui para o OpenAPI. Deixa

09:05

eu dar um pause aqui, pessoal. Até eu resolver esse OpenAPI.

09:09

E assim que ele estiver up novamente.

09:12

Eu retomo aqui só para a gente fazer o último teste.

## Resumo IA

[RESUMO_IA]