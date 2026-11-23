Módulo: Desenvolvimento de Agentes com IA\
Aula: [Criando Ambiente do Projeto](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18093)

## Resumo da aula



## Transcrição

00:00

Nesta aula nós vamos preparar o ambiente do projeto para

00:03

que nós possamos criar os nossos exemplos práticos.

00:06

Já estou com o VS Code em aberto,

00:09

não tenho nada no projeto, nós vamos criar tudo do zero.

00:12

Eu vou começar pelas extensões. Digite Python e

00:17

instale essas extensões que estão ativas, porque tem algumas que não estão ativas.

00:23

A principal é essa, todas na verdade são mantidas pela Microsoft.

00:28

Então essa é a Python. Faz com que a IDE consiga entender o Python.

00:32

Mas com todas essas extensões instaladas, dá para fazer debugger com Python,

00:38

alinhamento de código, que é esse AutoPep8,

00:41

PyLint e PyLance vai nos ajudar a identificar

00:45

erros no momento que nós estamos digitando,

00:47

porque o Python é uma linguagem igual ao Java, que você não pode...

00:55

cometer erros ou tentar acessar alguma propriedade que não existe.

00:59

Com Python você só vai descobrir isso no momento

01:02

que você fizer a execução do código.

01:05

Então, com tudo isso aqui,

01:07

nós já temos um bom suporte e principalmente não é só para desenvolver com Python,

01:12

mas para o nosso aprendizado,

01:13

que nós estamos focados aqui em aprender a desenvolver esses agentes.

01:18

Nós vamos utilizar o gerenciador de pacotes chamado uvicorn.

01:22

A comunidade Python é um pouquinho diferente das outras comunidades,

01:26

porque enquanto em outras linguagens você tem um gerenciador de pacotes,

01:30

dois ou três no máximo, com Python você tem mais de dez,

01:34

só aqui nós temos vários.

01:36

Mas esse uvicorn tem o diferencial de ser construído

01:39

em Rust e muito focado em performance,

01:42

então é muito legal para que nós possamos utilizar.

01:45

Faça a instalação dele aqui com o comando de curl.

01:49

Como você vai estar no Windows com o WSL,

01:51

na verdade, esse comando aqui vai ser igual para todo mundo.

01:56

Então, vamos voltar aqui para a IDE.

02:00

Eu vou rodar o uvicorn init. Eu poderia passar o nome de uma pasta,

02:05

mas como eu já tenho um projeto, só coloco o ponto.

02:07

Então, ele já vai criar tudo o que é necessário

02:10

para que a gente já possa trabalhar com Python.

02:12

Esse Python version, que é o enfoque de qual é a versão...

02:19

do Python que nós vamos utilizar.

02:21

Na verdade, ele até colocou errado isso aqui que eu estou utilizando a 3.12,

02:26

então vou colocar exatamente essa versão. Crie um main.py com

02:32

um hello world muito simples e o pyproject.toml que equivale a

02:38

qualquer arquivo de gerenciador de pacotes que você tem no seu projeto.

02:44

O toml é meio que um irmãozinho do YAML, é uma forma

02:50

de estruturar dados como JSON, como YAML, enfim. Então,

02:56

é só isso que nós temos no nosso projeto.

02:58

Então, nós podemos fazer aqui um

03:01

uvicorn run apontando por main.py.

03:06

Então, ele vai mostrar o Hello World.

03:11

Veja que ele está pegando o Python, que

03:15

eu tenho o instalado, o 3.12.

03:18

Nós não queremos apontar para esse Python global, por isso que...

03:23

Nós queremos o virtualenv. Então, quando você faz essa primeira execução,

03:28

ele já cria esse virtualenv aqui.

03:31

Então, eu tenho o binário do Python que aponta para o meu global,

03:37

mas ele faz o gerenciamento local de todas as minhas bibliotecas.

03:40

Tudo que eu instalo vai aqui para essa pasta lib ou essa lib64.

03:47

Então, não fica no meu Python global.

03:49

Então, quando eu tenho esse virtualenv, se eu continuar rodando...

03:54

Com o venv, ele vai acabar apontando para o meu Python local.

03:58

Mas se eu fizer dessa forma aqui, python main.py, ele

04:05

não pega esse Python local.

04:08

Então, quando você rodar as coisas com o venv,

04:12

você já tem a praticidade de usar o virtualenv.

04:14

Mas, quando você quer rodar vários comandos, utilizar o Python,

04:18

nós temos que rodar o comando source, apontando para o venv,

04:26

E aqui dentro,

04:27

veja que nós temos vários scripts activate

04:32

para ativar esse ambiente como principal no terminal que você está.

04:37

Então, colocando o bin, como o meu terminal é o Fish, não é um

04:44

bash padrão ou um zsh, eu tenho que colocar ele para ser compatível.

04:49

Então, agora eu tenho esse ambiente sendo demonstrado aqui.

04:54

Se eu fizer qualquer coisa agora com o Python, eu

04:58

não vou ter nenhuma diferença, mas o Python utilizado é exatamente esse.

05:03

Então, lembre-se desse detalhe.

05:06

Precisamos fazer também uma configuração do VS Code

05:09

para que ele entenda melhor o Python,

05:11

porque se a gente não apontar que estamos utilizando o virtualenv,

05:16

ele vai acabar apontando para o Python global e não

05:19

vai entender as bibliotecas que estão instaladas localmente.

05:23

Então... Esse arquivo aqui pode definir qualquer coisa local do seu projeto.

05:27

A primeira configuração é onde está o Python.

05:31

Justamente apontando para o workspace, que é o diretório raiz,

05:35

para o venv/bin/python.

05:38

Então, qualquer coisa que vá acontecendo, ele sabe que está...

05:42

Uma vez que a gente aponta para cá, já está tudo amarrado.

05:48

Então, ele consegue entender a pasta lib, lib... 64, enfim,

05:53

ele vai conseguir dar suporte a tudo que a gente precisa.

05:57

O Python terminal activate environment igual a true serve para

06:04

que a gente já tenha o virtualenv ativo por padrão.

06:08

Então, toda vez que eu abro o terminal,

06:10

esperando um pouquinho, ele vai rodar o comando source,

06:15

aí ele coloca o caminho completo,

06:17

aí ele já identificou que eu estou utilizando o Fish.

06:21

Então, isso já serve de praticidade, porque agora, quando eu rodar Python,

06:25

eu não preciso ficar rodando mais o source.

06:29

Isso aqui faz com que a gente tenha um efeito colateral, por exemplo, no Cloud Code,

06:33

se você estiver utilizando ele ou qualquer outro CLI,

06:37

quando eu abrir o Cloud Code, ele

06:43

vai executar o source, mas aí você pode fazer um Ctrl+C,

06:46

no caso, para o CLI de compilação também e outros.

06:49

É só fazer essa limpeza, mas sempre que ele ver um terminal integrado,

06:53

que é a configuração descrita, ele vai tentar jogar e habilitar isso.

07:00

Essa configuração do Terminal Integrated em VS Code, ela

07:06

pode ser habilitada para qualquer outro sistema operacional,

07:09

dependendo do que você estiver utilizando,

07:10

mas ela é relevante porque às vezes nós podemos fazer um CD numa pasta,

07:15

e aí eu faço um Python alguma coisa, por exemplo, xptl .py.

07:20

E aí nesse arquivo nós temos lá um monte de importes,

07:25

relativos para outros lugares do projeto, e aí ele pode se confundir,

07:30

porque ele considera a pasta atual como se fosse a pasta raiz do projeto.

07:36

Então, estou falando para ele que sempre que abrir um terminal,

07:41

passe o Python path como diretório do projeto. Então,

07:45

não interessando a pasta que eu estou aqui em aberto,

07:48

ele sempre vai carregar as coisas olhando a pasta raiz.

07:53

Aí daqui para baixo são configurações para que ele melhore o autocomplete.

07:58

Essa aqui de análises extra paths para que ele considere todo o projeto,

08:04

para que ele analise e indexe tudo.

08:07

Queremos habilitar o autocompletions e o

08:12

type checking porque senão nós vamos

08:16

digitando coisas e ele não faz nenhuma verificação de tipos porque o Python...

08:21

Se você tiver uma variável inteira e você acessa alguma coisa de string,

08:27

você só vai descobrir quando você rodar as coisas. Então,

08:32

ativando pelo menos o básico, nós já vamos ter alguns avisos,

08:37

mas tem modos mais fortes.

08:39

Nós podemos trabalhar aqui no modo mais forte, que é o strict.

08:41

Então, dessa forma aqui, agora eu já consigo...

08:48

E quando aparecer essas linhas é o call palette

08:51

que eu estou habilitado no meu terminal.

08:54

Mas eu já consigo então pegar uma string qualquer,

08:59

ter o autocomplete de tudo, tudo indexado.

09:03

Então agora nós podemos instalar quaisquer bibliotecas e ir criando o nosso projeto.

## Resumo IA

[RESUMO_IA]