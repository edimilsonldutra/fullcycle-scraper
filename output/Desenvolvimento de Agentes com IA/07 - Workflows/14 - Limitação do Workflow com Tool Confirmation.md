Módulo: Desenvolvimento de Agentes com IA\
Aula: [Limitação do Workflow com Tool Confirmation](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18578)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre uma limitação do workflow em relação a esse request input que

00:06

nós utilizamos na última aula para poder finalizar o

00:09

workflow pedindo uma autorização para o usuário.

00:12

Nós tivemos aqui essa etapa do await e found

00:18

input note, ficou esperando que a gente mandasse o confirmed igual a true,

00:23

depois tivemos aqui o resultado final, grava no banco de dados e tudo mais.

00:32

Ele é idêntico ao toConfirmation em questão de parar

00:36

o processo esperando que um humano faça a interação.

00:43

E quando nós estamos trabalhando com esse workflow,

00:46

você vai continuar utilizando esse request input substituindo o toConfirmation.

00:54

Então, vamos pegar... O que eu quero dizer com isso?

00:57

Vamos pegar o código que nós já havíamos criado. Nós tínhamos feito...

01:03

que é um cancelar assinatura que precisa da autorização.

01:08

Então tem que ter lá o tool confirmation confirmed, e aí sim, se ele tiver ok

01:16

até a questão da senha, nós vamos autorizar.

01:19

No momento que eu estou gravando esse vídeo,

01:22

por isso que eu tomo bastante cuidado com isso,

01:24

porque como esses frameworks, o SDK e outros, são muito novos,

01:28

com

01:29

certeza... Com o passar das releases, nós vamos ter mudanças, transformações,

01:36

expansões, mas no momento, quando nós colocamos tool confirmation,

01:41

vamos colocar assim a receitinha,

01:43

workflow mais agent mais tool confirmation,

01:50

não tem problema nenhum,

01:52

nós usamos durante todo o capítulo, não funciona.

02:00

Nessa comunicação do agent com...

02:04

na verdade do workflow do agent com o LLM, quando

02:08

você para e pede para o usuário interagir e manda de novo,

02:13

é como se você não tivesse iniciado o processo do tool confirmation, então ele não consegue manter.

02:18

Então eu acredito que isso aqui deva ser corrigido,

02:20

mas a gente tem que entender no momento que mesmo que seja corrigido,

02:25

nós conseguimos mudar a dinâmica de trabalho para adaptar com o request input.

02:33

Então vamos imaginar que você tenha um agent que vai ter

02:38

determinadas tools.

02:43

Você vai ter que criar o seu agent de modo que pode ser uma tool

02:47

que vai ser executada, que vai precisar mudar o

02:51

estado de alguma coisa ou várias tools.

02:54

Você vai transformar isso num function code.

02:57

Na verdade também dá para poder fazer tool como nó,

03:01

como nós já vimos falar lá atrás.

03:04

Você vai ter que tirar esse comportamento de dentro do agent,

03:08

fazer com que o agent retorne esses valores,

03:11

você pode muito bem usar a saída estruturada,

03:13

como nós usamos na maioria dos nossos agents,

03:17

deu a saída estruturada, então você

03:22

cria o request input, você

03:26

pode passar aqui também o payload, como eu já havia falado com as informações,

03:31

então você recebe aqui o node input e passa o payload,

03:36

falando assim, ah, tem a informação tal, etc, etc, etc.

03:44

Aí mostra lá para o usuário se ele autoriza ou não.

03:48

Então você vai num

03:53

próximo nó com o function code,

03:56

pega esses valores, vê se confirmou, se não confirmou, e executa o seu código.

04:02

Então, você

04:04

tem o agente, tem a saída estruturada, aí

04:13

nó request input, de processamento.

04:22

A dinâmica é essa.

04:25

Quando tiver alguma versão que corrija isso, não vai precisar fazer isso,

04:31

mas esse é o ponto. Mesmo que tenha, você pode trabalhar dessa forma também.

04:35

O que eu acho interessante de um ponto de vista de organização, porque você

04:42

deixa também para as coisas serem mais determinísticas. Você aproveita,

04:48

colhe os frutos do agente de IA,

04:53

mas processa as coisas com mais certeza.

04:55

Enfim, outras pessoas podem ter outras visões,

04:58

mas já deixo essa informação aqui registrada.

05:02

Em versões mais para frente da 2.2, que é a que nós usamos, ainda não foi corrigido,

05:07

mas pode ser que seja corrigido a qualquer momento,

05:11

então fica registrado para que você tome atenção.

## Resumo IA

[RESUMO_IA]