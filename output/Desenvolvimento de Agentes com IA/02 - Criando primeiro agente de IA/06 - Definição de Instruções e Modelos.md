Módulo: Desenvolvimento de Agentes com IA\
Aula: [Definição de Instruções e Modelos](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18097)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos trabalhar com instrução e a definição de um modelo no agente.

00:07

Nós fizemos o exemplo da última aula, que apenas definiu este agente com o name,

00:13

que é a única informação obrigatória, mas nós podemos, obviamente,

00:16

passar o System Prompt para esse agente e também definir quaisquer outros modelos.

00:24

Então, começando aqui com a definição de um novo agente,

00:28

como que eu deveria trabalhar?

00:31

Eu poderia criar uma outra pasta, que

00:35

poderia ser outro agente,

00:38

criando o agent .md,

00:41

mas também uma convenção é criar uma pasta agents,

00:47

ou com qualquer nome que você queira, não precisa ser necessariamente dessa forma.

00:52

Então eu vou mover esse agente para cá,

00:54

e vou mover esse outro que nós vamos criar aqui,

00:59

mas este outro eu vou chamar de... meu

01:05

agente 2 e

01:08

esse aqui vai virar 1, apenas para que a gente possa mudar.

01:13

Então eu vou usar esse código no nosso novo agente e

01:20

também copiando o

01:24

init .md.

01:25

Então agora nós podemos fazer um

01:29

adk run passando a pasta agents.

01:35

Veja que ele não vai conseguir encontrar o mesmo erro que nós vimos na aula passada,

01:40

basta passar qual é. Isso aqui é o número 1.

01:44

E agora vamos para o número 2.

01:49

Então nós podemos definir primeiramente a instrução.

01:52

Aqui eu vou colocar o número 2 também. Então temos a

01:57

instrução.

02:00

Podemos colocar aqui que você é

02:07

um especialista em Python. Então,

02:15

vamos rodar o agente 2,

02:18

mandando um olá para ele.

02:22

Ele não vai devolver apenas um olá,

02:25

ele vai falar que ele é um especialista em Python

02:27

e está pronto para poder ajudar com essa situação.

02:31

Então, aqui nós podemos passar quaisquer instruções.

02:35

Também é muito comum que o system prompt do agente seja uma instrução...

02:41

que necessite várias linhas.

02:43

Então nós temos algumas formas de fazer isso com o Python.

02:47

Essa primeira que está aqui utiliza parêntese,

02:52

então você abre e fecha parêntese, cada linha tem uma aspas.

02:59

Ou usando três aspas para abrir a

03:03

cadeia de string e três aspas para fechar.

03:08

Inclusive isso aqui pode ser usado,

03:10

normalmente isso aqui é usado até no topo do arquivo,

03:13

você vai encontrar arquivos dessa forma, ou no topo de métodos como comentário.

03:19

É uma forma de comentário,

03:20

na verdade o comentário no Python oficialmente é usado a hashtag.

03:25

Então vamos pegar aqui essa instrução de baixo.

03:31

Eu coloquei para que ele possa fazer um código Python.

03:38

que é a instrução que está aqui,

03:39

Escreva um código Python que imprima Olá Mundo e

03:41

Certifique-se de usar a função do print.

03:47

Então ficam essas opções para que você possa definir da forma que você quiser.

03:53

Agora vamos trabalhar com o modelo.

03:57

É necessário que seja especificado um modelo,

04:00

Na verdade, ele já tem um modelo padrão,

04:03

Mas ele precisa de um modelo.

04:05

Aqui eu estou navegando para a classe que está dentro

04:11

Da parte de lib, llm-agent, então alias é apenas,

04:16

Na verdade, o agent é um alias para o llm-agent.

04:20

Digitando aqui default em cima na classe, nós vemos que existe um default model,

04:25

Que é o Gemini 3 Flash Preview. Esse aqui é um modelo bem barato,

04:31

Mas é um modelo em preview.

04:33

Nós podemos definir o modelo através da propriedade model,

04:36

E existem duas formas de fazer essa definição.

04:41

Aqui ele está mostrando um erro, mas ir para a propriedade vai ser melhor.

04:47

Vendo esse union string e base LLM,

04:50

Nós podemos definir o modelo através de uma string convencional ou

04:56

Através de uma classe que seja compatível com esse base LLM.

05:00

No final das contas, acaba sendo uma classe do Pydantic, que é uma lib base,

05:07

Que faz validação das coisas dentro do ADK. É muito bom,

05:11

Na verdade, que ele usa esse Pydantic.

05:14

Então, uma

05:18

Classe como essa vai definir algumas situações de

05:23

Como que o modelo tem que ser definido.

05:27

Nós podemos passar apenas uma string dos modelos do Gemini,

05:31

E aqui nessa documentação do Google,

05:33

No ai.google.dev/gemini-api-docs,

05:38

Nós temos todos os modelos disponíveis, então tem o modelo PRO,

05:42

Basta clicar, e aí temos o código do modelo,

05:47

Vai ser exatamente isso que nós passamos ali.

05:49

Quando eu estou fazendo testes muito básicos,

05:52

Eu uso nem o Flash, eu uso o Flashlight. Então

05:58

Podemos pegar este valor e

06:02

Passar para cá. Vamos rodar o agente novamente,

06:06

Vou passar lá com mensagem inicial.

06:10

É um modelo tão básico que ele simplesmente

06:12

Desconsiderou qual é o System Prompt dele.

06:15

Eu posso perguntar qual é o seu System Prompt. Como

06:25

Modelo de linguagem, eu nem tenho o System Prompt.

06:29

Mas se eu pedir execute o seu System Prompt.

06:41

Vamos rodar de novo. Vou falar assim, execute

06:46

Sua função.

06:54

E na verdade até eu tomei um erro.

06:57

E nem estou usando por nada, execute sua função.

07:04

Aí pronto. Vocês viram que é

07:10

Bom deixar isso na gravação.

07:12

Por isso que você tem a opção de retry para

07:17

Evitar esse tipo de problema. Então ele seguiu exatamente o que estava ali. Mas se eu mandar um olá,

07:23

Ele simplesmente me respondeu e desconsiderou o que ele tinha que fazer.

07:28

Então, assim, eu posso passar qualquer modelo,

07:30

mas se eu quiser trabalhar com um modelo externo,

07:35

aí, vamos passar aqui até um Sonnet 4.6 da Anthropic,

07:40

obviamente nós não temos nenhuma

07:45

API Key ainda, mas assim que seria a definição do modelo. Então,

07:49

ao fazer aqui o carregamento, vou colocar um Olá, e

07:56

nem ele vai fazer a chamada, mas é porque não é simples passar...

08:02

ali o modelo, ele já vai fazer a comunicação.

08:07

Eu preciso saber como me comunicar com esse modelo,

08:11

por isso que ele está até recomendando que nós usemos esse Lite LLM,

08:17

que é um pacote famoso da comunidade Python,

08:20

que tem adapters para vários modelos.

08:23

Então você vai poder usar aqui o modelo da OpenAI, da Anthropic.

08:26

Então nós poderíamos fazer um uv-add exatamente com essa instrução que está aqui.

08:34

Ele vai fazer a instalação. Então

08:39

pronto. Então agora no PyProject vamos ter o LightLLM.

08:45

Eu vou deixar comentado o

08:48

modo que nós utilizamos antes com o Gemini Flashlight.

08:53

Então aqui em Model eu vou precisar importar o LightLLM.

09:00

Será que ele vai encontrar aqui do Google ADK fácil? Eu não coloquei também o...

09:06

Um rastreamento no VS Code muito grande? Não, não vai. Então,

09:09

eu vou colocar google

09:10

.adk .models .lightllm import lightllm. Então,

09:17

eu passo a classe passando o model da Anthropic.

09:27

Então, a questão aqui é que nós estamos pegando

09:34

uma classe do Google ADK que vai

09:37

conversar com o LightLLM que está instalado.

09:42

Vamos rodar novamente o agente. Então, agora, ao fazer um Olá,

09:46

obviamente ele vai dar um erro porque eu não coloquei a Anthropic API Key.

09:52

Eu posso pegar a minha Key e colocar no

09:58

Env. E você já deve ter percebido que, por padrão,

10:02

tudo isso que está sendo executado através do ADK Run,

10:09

ele está carregando o ponto Env por padrão.

10:13

Porque senão nem iria funcionar, eu tenho que ter a Google API Key definida.

10:20

Então, aqui eu posso passar uma infinidade

10:24

de modelos para usar o meu modelo específico. Então,

10:28

ele vai interagir com a biblioteca e assim você faz a definição do seu agente.

10:33

Então, o que temos de mais básico na definição de um

10:36

agente com ADK é o nome que é obrigatório.

10:40

obviamente o System Prompt que você vai acabar definindo e

10:44

qual é o modelo que você vai utilizar,

10:47

seja com LightLLM,

10:48

seja uma String ou até mesmo com definições em uma variável,

10:54

porque se você vai usando os mesmos modelos em vários lugares,

10:57

você pode fazer organizações com Python.

11:01

Aí vem a questão específica de linguagem de programação,

11:04

que não é a nossa preocupação aqui.

11:08

Então, definido isso, vamos avançando.

## Resumo IA

[RESUMO_IA]