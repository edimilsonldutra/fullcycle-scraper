Módulo: DevOps e SRE com IA\
Aula: [Observabilidade de Agentes pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18531)

## Resumo da aula



## Transcrição

00:00

Isso aí, pessoal. Estamos de volta aqui para a nossa última parte desse módulo,

00:06

onde a gente vai falar um pouco da observabilidade

00:09

de Agents e de processos de LLM através do LangFuse.

00:15

Então, basicamente, a nossa stack que a gente criou lá no início,

00:19

a gente já subiu o LangFuse,

00:20

então já temos ele aqui disponível,

00:22

aquela stack de observabilidade que a gente criou.

00:25

E agora a gente vai aprender aqui como ativar isso, tá?

00:29

Na aula passada,

00:30

eu disse que tem duas maneiras de a

00:34

gente ativar o LangFuse para rodar com o OpenMUI.

00:38

Quais são essas duas maneiras? Via OpenTelemetry, que eu conecto o LangFuse,

00:43

conecto o OpenMUI no OpenTelemetry e o OpenTelemetry

00:50

faz o export das informações para dentro do LangFuse.

00:53

E via pipelines aqui dentro do LangFuse, chamadas de funções aqui dentro, tá?

00:58

Sendo que a segunda é a maneira mais simples de fazer,

01:00

tá bom? Então vamos focar nessa maneira mais simples,

01:03

até porque a gente está usando a versão mais defasada do LangFuse,

01:08

que não tem também a possibilidade de conectar via OpenTelemetry.

01:13

Então usem a versão 3 superior, tá?

01:16

A gente está usando a versão 2.

01:18

Usem a versão 3 superior se vocês quiserem fazer o teste para fazer a conexão.

01:23

do Open Web UI através do OpenTelemetry. Ok? Então, vamos lá. Primeiro passo aqui,

01:30

a gente vai criar, vamos começar direto com a demo,

01:33

né? Observabilidade com o NetVLM. Então,

01:35

a gente vai criar uma org lá dentro do LangFuse, gerar as APIs, keys,

01:39

a gente vai instalar filter dentro do Open Web UI,

01:42

vai fazer uma pergunta no Open Web UI e observar

01:45

os traces chegando no LangFuse e vai verificar os dois pipelines,

01:49

o hotel, o tempo, essas coisas tudo, se vai chegar tudo lá.

01:53

Tá bom?

01:56

Vamos validar aqui, isso vai funcionar tudo legal.

02:00

Vamos numa primeira parte aqui de criar a nossa org lá dentro do LangFuse.

02:07

Vamos abrir aqui o LangFuse, LMStudio, Docker, opa, está aqui do lado.

02:14

Vamos abrir aqui o LangFuse.

02:17

Que até lindo prometeu, se vocês quiserem fazer alguns testes, tá?

02:20

Mas vamos abrir aqui o nosso LangFuse. DTP, dois pontos, barra, barra, LangFuse. LangFuse. Teste.

02:34

Dois pontos, 80, 80.

02:38

Ok, temos o LangFuse aqui. No primeiro login,

02:41

você pode criar aqui um login para você.

02:43

Então, vamos chamar o Robson aqui. Robson, arroba, MBA .com.

02:49

Vamos colocar uma senha aqui para a gente

02:52

fazer um primeiro login na nossa ferramenta.

02:56

E ele redirecionou aqui para o localhost. Não era para fazer isso,

02:59

mas tudo bem. Provavelmente as configurações dele lá.

03:03

Só vou fazer a entrada de novo aqui.

03:05

Provavelmente as configurações dele estão com o redirect para localhost. Não deveria.

03:09

Tinha que estar com o redirect para cá. Mas tudo bem.

03:11

Basta você recarregar aqui que você vai conseguir já entrar na área logada. Legal?

03:16

Primeira parte. Vamos criar uma organização aqui.

03:19

Vamos chamar ela de MBA, ok?

03:23

E aqui a gente vai ter um tracer que a gente vai chamar de Open Web,

03:30

tracer não, né?

03:31

Um projeto que a gente vai chamar de Open Web UI, ok? E vamos criar ele aqui agora.

03:39

Ok, após o projeto criado,

03:41

a gente vai fazer agora a parte aqui de gerar as APIs aqui, tá bom?

03:49

Nas APIs Keys do LangFuse, ele sempre gera duas, tá?

03:53

Uma que chama Secret Key e a outra que chama Public Key, esse padrão.

03:57

E aqui é o host que ele vai ser chamado, tá?

04:01

Vamos deixar essa tela aberta que a gente vai precisar dela ainda.

04:03

Por agora, a gente vai voltar no OpenMBY, ok?

04:08

Basicamente, para a gente fazer a criação aqui do nosso function,

04:15

a gente vai abrir o Playground aqui, não é Playground não,

04:18

a gente vai aqui em Painel de mim,

04:19

vir aqui em funções, tá bom? E vamos aqui adicionar nova função.

04:25

Ok, adicionar nova função. Tem a possibilidade de você importar do link também,

04:29

tá? Se você quiser algum link,

04:31

quer colocar um link de internet, etc,

04:32

que tenha algum arquivo .python, você pode importar.

04:35

Aqui a gente já tem nosso arquivo .python pronto,

04:38

que eu vou disponibilizar para vocês.

04:39

Aqui ele te dá até um exemplo de função.

04:42

Lá no Open

04:46

Web UI Functions,

04:50

a gente tem aqui as várias funções que a gente pode usar.

04:56

Aqui tem um catálogo aqui em algum lugar.

04:59

Topic Guild, Commit, Function Library.

05:02

Então aqui a gente tem um catálogo de várias funções aqui que a gente pode usar.

05:06

Então a gente tem algumas possibilidades aqui.

05:11

de usar algumas funções que foram criadas pela comunidade dentro do seu ambiente, ok?

05:15

Só um exemplo aqui do que a capacidade da function aqui dentro. Tá bom?

05:21

Então vamos deletar esse exemplo aqui e vamos pegar o

05:24

que a gente criou para que se chama LengthFusePipeline.

05:28

Vou colar ele aqui, ok?

05:31

Basicamente, ele tem aqui algumas coisas do LengthFuse,

05:35

tem aqui o import LengthFuse. Ah, tem que colocar aqui também,

05:40

Aqui eu já tenho a parte de dependência, requirements na verdade.

05:43

Ele tem um requirement que basicamente ele vai instalar pra

05:47

gente aqui o LangFuse 3 menor que 3, né?

05:51

Pra ter compatibilidade com o ambiente que a gente tá rodando.

05:55

Vai importar o LangFuse aqui.

05:58

vai fazer alguns filtros aqui, etc, e assim por diante.

06:01

Deem uma lida no código para vocês entenderem como funciona.

06:06

Mas a parte que importa para a gente é esse inlet.

06:09

O inlet é tudo, quando a gente faz a chamada, manda a mensagem,

06:12

ele sempre vai passar por esse inlet.

06:15

Nesse inlet a gente vai conseguir pegar alguns dados que são

06:18

interessantes para a gente e mandar para o LangFuse.

06:22

E aqui no outlet é justamente o retorno. Basicamente,

06:26

você só retorna aqui o body original para ele dar continuidade.

06:30

Beleza? Então, vamos salvar essa função aqui. Confirmar.

06:36

Feito isso, a gente já tem a função pronta aqui para ser usada.

06:40

Quando a gente clica nessa engrenagemzinha aqui de configurações,

06:44

a gente vai ter as possibilidades de informar a secret key, que está padrão.

06:49

A gente vai clicar aqui em padrão.

06:51

A gente tem a possibilidade de informar a public key.

06:54

E aqui o host já da Langfuse 3000,

06:58

que já vai pegar internamente como o Langfuse está no mesmo pod,

07:01

mesmo esquema que a gente fez do MCPO, a gente já consegue chamar ele diretamente,

07:07

a gente já vai verificar se é isso mesmo lá nele.

07:10

Aqui a gente tem a possibilidade de inserir algumas tags e aqui algum debug,

07:13

se a gente quiser ver os logs aparecendo lá dentro do OpenWebWire.

07:18

Ok? Então vamos aqui pegar primeiro a Secret Key.

07:22

Vamos pegar a CircuitKey, copiar ela, colar aqui dentro do LangFuse. Copiou, não?

07:31

Coloque tudo. Está copiando, não?

07:34

Vamos copiar aqui de maneira tradicional.

07:39

Agora temos a CircuitKey aqui. Vamos pegar a PublicKey,

07:44

copiar ela também e colocar aqui dentro.

07:49

Aqui o LangFuse 2.3 mil. Vamos verificar lá no nosso...

07:56

K8S, sei onde que o Langfuse está respondendo. Então está aqui,

07:59

Langfuse 2.3000. Está respondendo nessa porta aqui. Ok? Tudo certo. Vamos

08:08

voltar aqui no OpenAPI e vamos validar se está tudo certo.

08:14

Vamos salvar essa configuração.

08:17

Vamos ativar esse debug aqui para a gente ver ela rodando.

08:20

Salva a configuração aqui. Salva a configuração.

08:24

A gente vai habilitar ela, porque ela está desativada. Então, habilitou.

08:29

E aqui a gente tem um global. O que é esse global?

08:32

Para todos os modelos que rodam dentro do OpenMUI,

08:36

todos os modelos, agents, etc.,

08:39

vão usar essa Langfuse aqui.

08:43

Essa pipeline do Langfuse. Pipeline não, desculpa. Essa função do Langfuse.

08:48

Tá bom? Então... Vamos ativar o Global,

08:51

porque qualquer modelo que eu mandar mensagem,

08:53

o tracing vai ser enviado lá para o Langfuse para a gente.

08:57

Então vamos fazer um primeiro teste aqui, o modelo local rodando.

09:00

Vamos fazer um teste, dar um oi aqui para o nosso modelo.

09:04

Então, em teoria, se tudo deu certo,

09:06

a gente vai ter isso aqui dentro do nosso tracing, tracers. Temos aqui o nosso oi.

09:13

Então basicamente a gente consegue ver o evento de geração,

09:17

que é um oi, e o generation,

09:19

que é a resposta, que está aqui embaixo.

09:22

Legal? Então aqui a gente tem um olá, como você está, e o meu usuário aqui, oi.

09:27

Então a gente consegue ver tudo completinho aqui o que aconteceu dentro do meu,

09:31

da minha chamada e de meus usuários, de todos os meus usuários.

## Resumo IA

[RESUMO_IA]