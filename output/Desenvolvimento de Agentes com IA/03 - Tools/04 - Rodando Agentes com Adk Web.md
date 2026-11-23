Módulo: Desenvolvimento de Agentes com IA\
Aula: [Rodando Agentes com Adk Web](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18101)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos conhecer o ADK Web,

00:04

que é uma interface gráfica, um Developer UI,

00:07

para que nós possamos rodar e testar os nossos agentes.

00:10

É uma interface voltada para desenvolvimento.

00:13

Então, através do browser, nós conseguimos rodar os agentes,

00:18

ver toda a comunicação que está acontecendo com a LLM,

00:23

com as tools, interceptar tudo, ver cada detalhe da comunicação.

00:29

É algo muito melhor do que o ADK run,

00:32

que serve apenas para poder rodar o agente usando um CLI.

00:37

Para fazer essa execução, basta fazer o ADK,

00:42

em vez do run, web, passando o agente. Então, se eu fizer dessa forma,

00:48

ele vai disponibilizar apenas o agente operador de conta.

00:52

Mas, no nosso projeto, nós temos três agentes.

00:58

E como nós estamos trabalhando com as convenções do ADK, de

01:03

ter uma pasta para os agentes e cada agente vai ter o seu agent.py,

01:09

nós vamos ter o benefício de poder passar apenas a pasta agents.

01:15

Então, todos esses três agentes vão estar disponíveis.

01:20

Pronto. Então, a interface já está rodando.

01:26

Nessa porta 8000, vamos acessá-la.

01:35

Então aqui em cima, nós

01:38

selecionamos os agentes.

01:41

Vamos até providenciar um zoom, tomara que não atrapalhe a interface.

01:47

Eu posso escolher qual agente que eu quero trabalhar.

01:50

Então, ao selecionar aquele primeiro agente que nós queremos,

01:53

vamos colocar apenas um Olá,

01:55

para ver se ele está funcionando. Então, nós já temos um chat para trabalhar,

02:02

posso digitar qualquer coisa aqui, uma série de opções.

02:06

Tem várias configurações que podem ser feitas para que você

02:10

possa fazer a simulação de cenários em cima desses agentes.

02:14

Então, vamos aqui para o operador da conta,

02:18

que é o último agente que nós tínhamos criado.

02:22

Então, eu vou colocar assim, listar minhas faturas.

02:31

Então, ele está pedindo para que eu

02:35

informe o ID do cliente. Mas antes disso,

02:38

vamos ver essa parte aqui do lado esquerdo.

02:42

Então, nós temos dois eventos que aconteceram.

02:46

Os eventos vão sendo cada passo que o agente vai executando.

02:50

O primeiro evento é a mensagem que nós enviamos para o agente.

02:55

E o segundo evento é a resposta que o

03:00

agente pegou lá do LLM e mandou para cá.

03:05

Mas aqui nós já vemos...

03:08

que o agente já

03:11

reconhece a tool, mas que ele não chamou ela.

03:14

Por isso que ele está marcado como se ele estivesse desabilitado.

03:20

Então, aqui nós conseguimos ver cada etapa e as informações disso.

03:25

Nós conseguimos ver também as informações da request. Então, veja só.

03:33

Eu tenho o modelo que foi utilizado,

03:38

headers que foram enviados.

03:42

O System Prompt, então olha só,

03:45

você é o atendente interativo e tal, mas aqui

03:51

Embaixo nós temos algo que não foi definido no System Prompt,

03:55

isso acaba sendo juntado quando o agente é montado.

03:59

Então ele está falando assim, você é um agente,

04:02

seu nome interno é operador de conta,

04:06

porque isso aqui faz total diferença na hora que você tem uma malha de agentes ou...

04:12

vários se comunicando,

04:13

você pode se referenciar, olha, acesse esse outro agente com o nome tal.

04:19

Então, por isso que a definição do nome é

04:23

muito importante, como nós já tínhamos feito antes.

04:28

Então, ele pega esse valor e gruda lá.

04:31

Então, nós já vimos aqui que na primeira comunicação, ele envia a tu.

04:38

Então, veja que a descrição dela é a docstring.

04:43

Tem o nome, que é o nome da própria função, e os parâmetros.

04:48

Então, cada detalhe definido ali, a tipagem,

04:53

ela vai virar contexto. Então,

04:55

cada detalhe definido vai ser crucial para o sucesso do seu agente,

05:00

como nós já havíamos conversado.

05:02

E aqui embaixo tem a parte de contents.

05:04

À medida que nós vamos fazendo a interação, esses contents vão aumentando,

05:10

que é onde está o histórico de toda a conversa. Então,

05:13

sempre o content 0 é a primeira interação com o usuário.

05:18

Ainda mostra que há role user, porque se for uma resposta da LLM,

05:24

então nós vamos ter uma outra role aqui.

05:28

Então, temos a resposta. No

05:33

caso da resposta, o content 0 é exatamente o que a LLM pediu.

05:38

Então, a LLM retornou isso para a gente.

05:42

E mais algumas outras informações relativas aos tokens.

05:50

Com essa interação toda desse conteúdo. Então, nós conseguimos ver aqui

05:56

os tokens de entrada, o total de tokens utilizados.

06:02

Vamos continuar fornecendo aqui uma outra informação.

06:07

Vou deixar aqui na parte do gráfico.

06:13

Temos aqui no evento 2.

06:15

Agora eu vou digitar cliente 1, 2, 3.

06:21

Então, nós vemos que ele invocou,

06:26

a função, a

06:30

tool, e aqui deu a resposta.

06:32

Então, nós temos

06:37

o evento anterior que mostra o que o operador de conta chamou essa tool.

06:45

Mas, aqui em traces vai ficar muito

06:48

mais visível como que essa comunicação aconteceu.

06:53

Cada vez que nós...

06:55

interagimos com o agente, é gerado o que é chamado de invocation ID, que

07:02

é um ID para aquela invocação.

07:05

Então eu mandei listar minhas faturas.

07:09

Acabou caindo no agente, ele fez uma chamada para a LLM,

07:13

que significa esse call LLM, então

07:18

a LLM gerou um conteúdo e nós conseguimos ver as informações pertinentes. Veja só.

07:27

Aqui é toda a informação da request que foi passada e dá response.

07:33

Nós mandamos o system prompt, fica um pouco bagunçado aqui,

07:38

mas lá na resposta ele está pedindo o ID do cliente.

07:43

Então, quando nós fazemos a segunda interação,

07:48

cai no agente, o agente chama a LLM, então

07:54

ele está passando o modelo, configurações, aqui o system prompt,

08:01

é como se eu tivesse um array de um

08:04

monte de informações aqui em determinado momento.

08:12

Aí aqui na resposta, isso

08:15

aqui é importante, agora fica claro como que o agente interpreta.

08:19

Porque a LLM vai falar assim, olha, tá, então você vai fazer um function call

08:28

passando parâmetro client ID com esse valor,

08:33

chamando a função listar faturas.

08:36

Então o agente captura essa informação e faz a chamada.

08:42

E obviamente, quando chegar... Aqui,

08:46

a LLM retornou o conteúdo para o agente,

08:52

ele vai lá e invoca. Então nós vemos aqui a resposta da ferramenta.

08:56

Então o agente faz a chamada novamente,

09:00

aí agora grudando o resultado final, a function response.

09:07

Então a LLM faz a

09:11

resposta, que é aqui no de cima. Ele vai pegar,

09:15

falar pago, não pago, data de emissão, etc.

09:19

Então, através desse painel aqui do Trace e dos eventos,

09:24

nós conseguimos acompanhar cada etapa,

09:26

ver cada informação, ver os tokens que estão sendo gastos nessa comunicação.

09:32

Além de outras coisas como o estado que nós não utilizamos, os artifacts,

09:36

os evaluations também que não foram setados,

09:40

é a plataforma mais amigável para que nós possamos...

09:44

fazer os nossos debugs, testar os nossos agentes.

## Resumo IA

[RESUMO_IA]