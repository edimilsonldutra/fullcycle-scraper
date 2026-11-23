Módulo: Desenvolvimento de Agentes com IA\
Aula: [Criando Primeiro Agente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18096)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos criar o primeiro agente com o Google ADK.

00:06

Então, eu vou pegar esse main.py, apagando todo o conteúdo dele, de

00:13

google.adk, que é onde está a biblioteca,

00:17

eu vou importar o agent, e aí defino uma variável qualquer,

00:22

e faço um new nela. No Python não é necessário colocar uma instrução com um new.

00:29

E a única informação obrigatória é o name. O name não é para colocar o nome formal.

00:36

Coloque o nome como se você estivesse definindo uma variável do Python.

00:41

Nós temos algumas regras.

00:45

Eu não posso definir a variável começando com um número,

00:49

enfim. Então aqui está o meu agente.

00:51

Eu não preciso definir qual é o modelo,

00:54

porque ele vai usar o modelo GPT-4 por padrão. E nem colocar um system prompt.

01:02

Então vai ser uma comunicação genérica que nós vamos fazer.

01:05

Agora, como que nós executamos esse agente?

01:08

E aqui que está o ponto crucial para que você já consiga começar com

01:15

o uso dos agentes. O agente por si só,

01:18

ele não define como você vai interagir com ele. Vai ser através de um HTTP,

01:25

vai ser através de um CLI.

01:28

Nós poderíamos, de forma manual, conectar esse agente

01:33

com uma API ou com um CLI qualquer.

01:39

Então, uma aplicação agêntica, ela pode ser uma aplicação web, pode ser um CLI,

01:45

pode ser uma aplicação desktop, e lá dentro tem um agente rodando.

01:51

Para que a gente não tenha que fazer isso ainda de forma manual,

01:55

nós podemos usar o executável do ADK. Como eu já estou com o Virtual Env ativo,

02:02

então eu consigo fazer o ADK run.

02:06

E é aqui que eu tenho várias opções.

02:10

Se eu rodar apenas python main.py, não vai acontecer nada com o arquivo.

02:17

Passamos mensagem, o agente não é executado.

02:20

Então, o ADK run serve para que a gente possa invocar esse agente.

02:24

Vai acontecer uma série de questões por trás.

02:27

Ele vai deixar o agente pronto para que aqui

02:29

no CLI nós já consigamos fazer a interação.

02:33

Ele não carrega o arquivo.

02:38

Ele sempre olha para a pasta para tentar carregar

02:41

o arquivo e tentar encontrar o agente que está definido.

02:45

Então, como eu defini esse main.py,

02:48

eu vou colocar apenas ponto para ele carregar dessa forma.

02:52

E aí ele mostra o nome de InvergeAgentNameDevAgentsAI. É estranho esse nome,

02:59

falando que o nome do agente precisa ser o identificador válido do Python.

03:06

Ter letras, dígitos e underscore only.

03:10

O que ele está querendo dizer aqui é que a pasta do

03:14

meu projeto não tem um nome

03:17

que seja válido para o módulo Python.

03:21

O módulo Python é justamente uma pasta, podemos definir assim o XPTO, e

03:29

aí dentro dela nós podemos ter N arquivos Python.

03:33

Então, dessa forma, eu

03:36

posso chegar no outro arquivo e falar de...

03:41

xpto.etc, eu vou importar qualquer coisa que esteja lá dentro.

03:45

Então, esse xpto é o módulo Python, uma vez que eu

03:51

tenho esse arquivo, mas tem uma convenção de colocar um __init__.py.

03:59

Isso aqui, na verdade, com as versões que foram evoluindo,

04:03

isso aqui não é mais obrigatório,

04:06

mas acaba sendo uma formalidade, uma convenção.

04:12

Esse módulo Python, que pode ser importado em qualquer lugar,

04:15

tem uma regra que nomes não podem começar com um número.

04:21

Eu não posso colocar um traço, não é válido isso aqui.

04:25

Se eu tenho palavras, elas têm que ser ligadas via underscore.

04:32

Então, nesse caso, até poderia ter o agente na raiz, mas não vale a pena.

04:36

O que normalmente nós fazemos é criar uma pasta para esse agente.

04:40

Então, vou colocar aqui meu agente.

04:44

Vou tirar essa parte aqui do main.

04:46

Na verdade, até o main pode cair fora daqui.

04:51

Então, vamos definir um

04:58

main.py. Vou deixar esse init.py. Então,

05:01

novamente, google.adk, import agent, meu

05:09

agente, meu agente novamente. Pronto.

05:22

Então, será que se eu passar agora meu agente, ele

05:28

vai apontar para a pasta, ele vai conseguir carregar o agente? Também não.

05:36

Ele mostra que quando ele tem uma pasta, ele

05:42

precisa ou

05:44

de ter um agent.py, ele coloca um or, ou o root_agent.yml,

05:51

que é uma outra forma de fazer a definição desse agente.

05:57

Então esse arquivo tem que ser agent.py.

06:01

Então quando nós olhamos para essa estrutura aqui,

06:05

é a estrutura básica do ADK. Eu crio uma pasta,

06:10

coloco o init.py por convenção e crio o agent.py.

06:17

Tem outras formas também de criar agentes,

06:19

nós vamos ver depois, agentes mais complexos, mas a base é essa.

06:24

Então, com isso aqui agora, vamos rodar novamente,

06:28

mas mesmo assim, ele

06:32

ainda não consegue encontrar o

06:37

meu agente. Por quê?

06:39

Quando ele vai carregar esse arquivo,

06:43

ele vai tentar ver se tem duas variáveis que ele pode...

06:49

Imagina que o ADK run,

06:51

na verdade, vai tentar importar esse... É como se ele estivesse fazendo assim,

06:56

ó. From meu agente import

07:01

alguma coisa.

07:04

Então, esse alguma coisa,

07:06

ele vai tentar encontrar se eu tenho uma variável chamada de root_agent ou se...

07:12

eu também fiz a definição desse agente através de um app.

07:16

Então, se eu mudar somente isso aqui para root_agent, ele

07:23

vai fazer

07:27

o import, veja só.

07:29

Então, agora eu tenho um CLI já carregado para fazer a interação.

07:34

Vamos só fazer um olá, e

07:38

ele vai mostrar uma

07:40

resposta, que é o meu agente que respondeu.

07:45

Essas informações que estão aqui em cima,

07:49

são alguns avisos, não teve nenhum problema.

07:51

Então eu tenho o log desse agente que está na pasta temporária,

07:55

posso acessar exatamente com esse comando, e

08:00

ele dá um aviso que como nós estamos utilizando o CLI, a

08:05

forma como ele está usando as credenciais em memória, e

08:13

outro aviso também sobre a questão de credenciais,

08:16

não tem nenhum problema. Nós podemos até rodar...

08:19

aqui com uma variável de ambiente, tirando esses warnings.

08:23

Na verdade, eu até não me incomodo com eles.

08:25

Então, aqui eu posso continuar fazendo qualquer coisa que eu queira.

08:33

Me fale sobre a linguagem Python.

08:36

Para que a gente veja que ele consegue responder quaisquer coisas.

08:42

Não temos nenhuma persona em volta dele.

08:47

Então, olha só.

08:50

Aqui está o resumo da linguagem Python, sintaxe simples.

08:54

Então eu posso fazer um

08:58

CTRL-C duas vezes para sair desse agente.

09:03

Então isso aqui é uma boa prática da

09:07

definição de agente. Isso aqui costuma gerar um pouco de confusão a princípio.

09:14

Então o que o ADK faz é criar convenções.

09:19

para que você possa carregar o agente através das próprias ferramentas do ADK.

09:25

Isso aqui de fato não é obrigatório, não é uma lei que você tem que seguir.

09:30

Você pode fazer uma definição totalmente distinta disso e carregar o seu

09:35

agente de forma manual ali na sua aplicação web ou num CLI.

09:40

Mas o ponto é que o próprio ADK...

09:43

tem o ADK run e depois o web que nós vamos ver,

09:47

para que você possa testar, fazer os debugs. Então,

09:50

trabalhar nas convenções faz com que você esteja integrado com o CLI,

09:56

até mesmo na hora de fazer o deploy, enfim.

09:58

Então, a recomendação é que você sempre siga essas recomendações.

10:03

Em relação ao nome do agente...

10:07

Não é obrigatório, mas é uma recomendação,

10:10

isso vai ajudar na hora que você fizer aqui as execuções com o ADK,

10:14

fizer debugs e etc., que este nome seja igual ao nome da pasta.

10:23

Então, se aqui está meu agente,

10:25

é recomendado que o nome da pasta também seja meu agente,

10:28

porque ambos os nomes têm que trabalhar na forma de identificação do Python,

10:35

ou seja, utilizando a underscore ou começando com o número.

10:39

Então, assim, você trabalha nas convenções.

10:41

Isso é interessante porque toda vez que você pegar um projeto ADK,

10:47

você sabe que ele vai já estar nesses padrões. Você vai ter a pasta,

10:53

vai ter o agent.py, aí poderíamos até,

10:57

se a gente quisesse pegar esse root agent e já colocar aqui,

11:01

porque quando ele vai fazer o carregamento...

11:05

Se ele ver que tem o init.py com alguma coisa,

11:09

ele já tenta pegar o que está sendo exportado.

11:12

É como se a gente tivesse aqui um index.ts ou um JavaScript.

11:16

Você pode já

11:20

habilitar o que você quer que seja exportado diretamente.

11:24

Eu coloquei este documento consolidando todas essas informações que nós

11:29

vimos aqui nessa aula para sempre lembrar sobre essas boas práticas.

## Resumo IA

[RESUMO_IA]