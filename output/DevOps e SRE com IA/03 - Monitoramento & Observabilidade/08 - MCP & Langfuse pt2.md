Módulo: DevOps e SRE com IA\
Aula: [MCP & Langfuse pt2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18509)

## Resumo da aula



## Transcrição

00:00

Legal? Então, temos um modelo sozinho fazendo

00:04

essas chamadas do LLM local. Então,

00:09

basicamente, se eu pegar o modelo sozinho aqui e falar Olá,

00:13

você consegue olhar meu

00:18

cluster K8S e me

00:21

falar quais são os serviços que temos disponíveis? Vamos lá!

00:29

Coloquei uma pergunta aqui para falar do serviço que a gente tem disponível. Está pensando?

00:34

Deixa eu analisar a resposta aqui.

00:37

Enquanto isso aqui está rodando dentro do OpenABY.

00:41

Vou desativar algumas coisas aqui. Por exemplo, ele gera aqui nomes para os chats.

00:48

Só que isso vai acabar pesando o meu LLM à toa.

00:51

Eu não preciso de nome para chat agora. Então vamos aqui no painel do admin.

00:54

E vamos desativar aqui algumas coisas da interface. Então,

00:58

geração de título, geração de modelo de prompt,

01:04

prompt com geração de acompanhamento, geração de tags, eu não quero.

01:10

Geração de tags, eu não quero.

01:12

Geração de consultas e recuperação, também não quero.

01:17

Geração de consultas web, não, também não quero. Então,

01:20

eu vou desativar a geração de acompanhamento aqui, acho que vai dar pena.

01:23

Prompt geração de acompanhamento. Vamos deixar todos desativados por enquanto.

01:28

Porque assim eu consigo que o meu LLM responda só o

01:30

que eu estou perguntando e não fique gerando prompts lá.

01:34

Tá bom? Mas vamos lá.

01:37

Cadê a pergunta que eu fiz? Tá aqui. Então o que ele fez?

01:40

Infelizmente não consigo acessar diretamente o cluster Kubernetes.

01:42

Ele já me falou que não tem como.

01:44

Porque ele não tem nenhuma capacidade agêntica, capacidade de tools.

01:49

para fazer as chamadas do meu serviço.

01:51

Então ele me deu alguns comandos aqui de CUP CTL,

01:55

como que eu posso pegar, ele me instruiu como que eu posso fazer essas informações,

01:59

tá? Porém, ele não conseguiu ir lá de maneira automática e pegar isso para mim,

02:06

tá? Ah, acompanhamento é essa sugestão aqui, vamos colocar lá.

02:09

Acompanhamento é legal para a gente conseguir ver qual que

02:12

é as possibilidades que a gente tem de...

02:16

De próximas perguntas. Que ele consegue fazer isso para a gente.

02:19

Legal? Então vamos ativar esse acompanhamento aqui.

02:22

Porque isso aqui é interessante para a gente ver as perguntas que ele pode entregar.

02:26

Geração. Pronto. Geração de acompanhamento. Opa.

02:31

Modelos. Geração de acompanhamento. Tá ativo. Só esse aqui.

02:34

Vamos lá. Salvo. Então temos a geração de acompanhamento ativa. Legal?

02:39

Então a gente viu aqui que o modelo não consegue recuperar.

02:43

Ele vai te sugerir. Vai te mostrar como que você pode fazer isso.

02:46

mas ele não vai conseguir fazer de fato para você.

02:50

Então, primeiro passo.

02:52

A gente já tem o MCPO lá de pé. Então,

02:57

vamos tentar fazer a configuração desse MCPO. Vocês vão vir aqui em painel do admin,

03:03

configurações, agora a gente vai vir aqui dentro de

03:07

integrações e a gente vai adicionar um OpenAPI aqui,

03:12

que é basicamente a nossa capacidade

03:17

de criar tools, tá bom?

03:20

Então a gente vai criar aqui uma ferramenta de k8s - Prometheus, ok?

03:27

E a gente tem um lock lá ainda de quebra.

03:29

Então aqui ele vai criar esse ID automático,

03:33

a gente vai dar uma descrição para ele aqui,

03:35

k8s - Prometheus

03:42

- MCP.

03:47

Prometheus é com H, tem um Hzinho aqui.

03:51

Ok, K8s Prometheus MCP. Então, RL base aqui, verificar a conexão,

03:57

vamos pegar o RL base. Basicamente, como ele está rodando no mesmo serviço,

04:01

a gente vai pegar aqui a mesma estrutura de URL que a gente tem.

04:05

Deixa eu procurar uma aqui, que basicamente, vamos olhar aqui dentro, não é aqui,

04:12

dentro aqui do iTerm.

04:15

Vamos abrir aqui nosso cluster e a gente vai no nosso service.

04:20

A gente tem aqui o nosso MCP. Então vai ser

04:26

http://mcp. Ele

04:40

está rodando dentro do mesmo pod,

04:42

então a gente nem tem necessidade de colocar o nome do namespace.

04:46

Porém, vamos ver se a gente consegue...

04:49

Colocar aqui o nome do namespace para vocês.

04:52

Deixa eu só achar aqui certinho onde que tá.

04:56

Beleza, encontrei aqui.

04:58

Então, basicamente, é mcp 2.8000,

05:04

que é a porta que ele está rodando lá, tá bom?

05:07

E aqui embaixo ele vai usar na URL um openapi.json, que é o padrão.

05:13

Então ele vai fazer as chamadas para essa URL aqui. Legal?

05:17

Então, se a gente vier aqui dentro do nosso cluster,

05:20

a gente vai ver que o MCP está rodando na porta 8000.

05:23

Então basicamente é isso, é simples fazer a chamada.

05:26

Como eu estou dentro do mesmo namespace,

05:28

está tudo dentro do mesmo lugar, ele vai fazer só uma chamada lateral,

05:31

a gente pode usar esse MCP 2.8000. Beleza?

05:36

Vai funcionar. Porém, se você estiver dentro de outro namespace,

05:40

a gente pode colocar a URL mais completa. Essa é a URL interna dele.

05:44

Então vai ser mcp.openweby,

05:50

que é basicamente o namespace que ele está, .srv,

05:54

que é de serviço, .cluster, .local,

06:00

que ele está chamando de cluster local.

06:03

Beleza? 2.8000. É a mesma coisa daquela parte pequena.

06:07

Se a gente testar a conexão aqui,

06:09

ela vai dar falha. Será que eu digitei alguma coisa errada?

06:13

É S, aqui, digitei errado, é SVC.

06:20

SVC, cluster.local. Então,

06:23

a gente consegue fazer a conexão bem-sucedida do mesmo jeito, tá?

06:26

Só que ele vai fazer a chamada aqui. Não importa a maneira,

06:28

tá, gente? Isso aqui não muda nada, tá?

06:31

Somente se você tiver um pod separado, tiver algumas restrições dentro do cluster,

06:35

que você tem que colocar isso, que você pode colocar.

06:37

Como a gente está dentro do mesmo namespace, vamos manter a URL curtinha aqui,

06:41

que a gente consegue validar, tá bom? Aqui a gente tem algumas opções de acesso,

06:45

a gente consegue mandar um token de acesso.

06:47

A gente consegue mandar a sessão do usuário, a gente consegue mandar um OAuth,

06:51

A gente tem várias possibilidades aqui para fazer autenticação. No nosso caso aqui,

06:54

Vamos colocar nenhum. Só para a gente que não tem autenticação nenhuma.

06:58

E aqui a gente pode inserir alguns cabeçalhos personalizados,

07:02

inclusive com variáveis de ambiente do sistema.

07:05

Se vocês forem na documentação do OpenWebWire,

07:08

lá você consegue ver quais são essas variáveis de

07:11

ambiente que vocês podem usar nesse envio de token.

07:15

Então vamos salvar esse cara aqui. Tá salvo.

07:21

Basicamente agora a gente consegue já usá-lo. Então,

07:25

se a gente vier aqui no OpenWebUI, aqui no modelo do Queen,

07:29

espero que não dê errado, né? Demonstração assim sempre dá errado. Então, vamos lá.

07:34

K8S prometeu-se perguntar quais são meus

07:38

pods dentro do

07:40

namespace do OpenWebUI.

07:47

Então, a partir desse momento, estou com a ferramenta ativada aqui. Eu não mostrei,

07:51

né? Deixa eu mostrar. A gente tem aqui ferramentas, tá?

07:55

E a gente tem a capacidade aqui da ferramenta que eu acabei de criar. K8S Prometheus.

07:59

Então, se eu fizer essa pergunta, eu já tenho uma ferramenta habilitada. Vou mandar.

08:03

E, basicamente, ele está pensando aqui o que ele deve fazer.

08:08

Deixa ele terminar de pensar.

08:12

Nesse momento eu estou enviando a capacidade da ferramenta já lá para o meu LLM,

08:16

então ela já tem reconhecimento de que ela tem a possibilidade de fazer aquela chamada.

08:20

E acabou de dar um erro. Vamos descobrir aqui o porquê.

08:26

Ele não fez a chamada da ferramenta. Pode ser que... Chamada de função.

08:32

Normalmente isso aqui tem que estar como nativo. Vamos fazer uma nova chamada?

08:37

Vamos fazer aqui. De novo. Mesmo prompt.

08:42

Vamos colocar esse aqui e vamos mandar esse cara.

08:46

Pensando. Está aqui rodando.

08:58

E provavelmente eu acho que não vai conseguir chamar de novo,

09:02

hein, gente? A demonstração dando problema aí.

09:05

Então vamos aqui descobrir o que está

09:08

acontecendo para ele não conseguir chamar essa sua.

09:13

Isso aqui não era para ter dado erro, não. Mas vamos dar uma investigada aqui.

09:18

Vamos pegar essa URL aqui.

09:21

Lembra que a gente criou o ingress lá no começo, quando a gente fez a stack?

09:27

Vamos tentar chamar aqui o HTTP MCPO 8000 OpenAI. Ah, beleza.

09:31

Não temos um roteamento aqui. Porém, a URL está incorreta aqui.

09:36

A gente tem que colocar a URL do ingress para a gente fazer alguns testes.

09:39

Então, mcpo.test, que é o nosso URL aqui local.

09:45

Todas as portas são 8080. Então, mcpo.test:8080,

09:50

openapi.json. Temos aqui um retorno do OpenAI. Ok.

09:56

Automatization API from MCP2 esquemas. A gente tem aqui os esquemas Kubernetes,

10:02

Prometheus e Lock. Ah, bacana. Então,

10:06

faltou uma parte aqui, porque ele está disponibilizando essas ferramentas.

10:11

Temos essas ferramentas aqui para usar. Porém,

10:15

faltou isso aqui, ó.

10:17

Barra Kubernetes barra OpenAPI.json. Aí a gente vai ter acesso às tools.

10:24

Então, eu tinha feito a configuração errada. Vamos refazer essa configuração. Então,

10:30

vamos olhar aqui. Tem como trocar o nome? Tem. Então, vamos lá. Kubernetes.

10:36

Então, a gente agora começa a ter os MCPs separadinhos para o Kubernetes,

10:40

não todos juntos mais, porque ele dá essa possibilidade.

10:44

Então, temos o Kubernetes aqui.

10:46

Vamos fazer aqui o MCPO 2.8000, MCPO 2.8000,

10:52

barra Kubernetes, barra OpenAPI.json. Vamos salvar aqui agora, mesmo esquema.

10:59

Ok, salvo com sucesso. Agora a gente tem a ferramenta Kubernetes ativa aqui.

11:04

Vamos ver só o nome dela aqui, tudo certinho,

11:06

ID opcional. Ok, vamos lá de novo no nosso chat.

11:12

Sempre lembrem de manter a chamada de função nativa,

11:15

porque o próprio LLM vai definir quem quer chamar

11:18

e qual vai ser o loop dessa chamada.

11:20

No modo padrão, funciona como uma gama mais ampla de modelos,

11:25

chamado de as ferramentas uma vez antes da execução.

11:30

Ou seja, com o modo nativo, ele consegue fazer um loop,

11:34

O próprio LLM consegue fazer um loop de chamadas ali.

11:37

O modo nativo aproveita os recursos integrados de chamadas de ferramenta do modelo,

11:41

mas exige que o

11:42

modelo suporte

11:44

o recurso internamente.

11:52

Inerentemente. Falei errado. Mas é isso.

11:55

Então usem o modo nativo porque ele vai ter a possibilidade.

11:58

Vamos tentar fazer um teste aqui no padrão para mostrar para vocês.

12:01

Vamos lá. Vamos pegar a mesma pergunta. Que eu fiz. Copiar ela aqui.

12:07

Vamos criar um novo shot. Colocar a pergunta.

12:11

E ativar agora a ferramenta nossa que vai chamar Kubernetes.

12:14

Ok? E fazer a chamada. Vamos lá.

12:18

Cruzei os dedos e foi.

12:21

Então agora o modelo está pensando.

12:23

O processamento.

12:26

Já conseguiu chamar a origem. Ele tem aqui uma origem.

12:31

A origem a gente pode criar. Ele conseguiu fazer.

12:35

Namespace, Open Web UI. E aqui tem todos os resultados do namespace. Olha que legal.

12:40

A gente consegue saber tudo que tem dentro do nosso namespace. Legal?

12:44

Então, olha, dentro do namespace, Open Web UI, os pods identificados são.

12:49

E aqui tem toda a listinha. Colocou, inclusive,

12:52

uma referência lá da minha chamada. Legal? Então, o que ele fez?

12:57

Eu fiz uma pergunta. O próprio Open Web UI, por trás,

13:03

fez a chamada, tá? Lá dentro do...

13:07

O próprio OpenBI orquestrou essa chamada

13:11

e fez lá dentro das tools.

13:14

Conseguiu definir que é essa tool que eu iria usar. Legal?

## Resumo IA

[RESUMO_IA]