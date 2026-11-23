Módulo: Desenvolvimento de Agentes com IA\
Aula: [Padrão generators](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18483)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos falar sobre o padrão generators,

00:04

que é o padrão crucial que permite que nós tenhamos esse formato de

00:10

execução do ADK.

00:13

Veja que essa linha do runner run async não significa que nós temos um array para

00:21

cada evento que está acontecendo, nós estamos capturando. Não,

00:25

nós temos uma estrutura de repetição que captura esse evento,

00:28

mas esses eventos vão sendo produzidos de forma dinâmica.

00:34

Porque acontece HTTP, principalmente, porque tem a chamada para LLM,

00:40

mas pode ter banco de dados,

00:42

pode ter N coisas que nós não temos certeza quando vão acontecer. Então,

00:48

esse evento que está aqui, ele é recebido à medida que ele vai acontecendo.

00:55

Então, nós temos uma função que, na verdade,

00:58

não devolve apenas um valor como retorno,

01:03

mas devolve vários valores.

01:05

E o for ajuda com que a gente vá

01:09

capturando esses eventos conforme eles vão acontecendo.

01:13

Então, a base disso, na verdade, uma das bases,

01:17

porque nós temos o padrão assíncrono que eu não vou falar nessa aula, é o padrão generators,

01:22

que existe no Python, existe no JavaScript, em várias outras linguagens.

01:27

Você precisa entender como funciona esse padrão, porque, de alguma forma,

01:32

ele vai estar no seu projeto, ou no seu framework, ou na sua biblioteca.

01:37

Nós podemos ter uma função que processa algo, que

01:43

normalmente vai ter um return, com um valor, ou se eu quero retornar vários valores,

01:49

gera um array, uma lista, no caso do Python.

01:53

Mas o problema é que, para o caso do ADK, eu tenho eventos dinâmicos. Então,

01:59

a função vai ter que ficar retornando as coisas conforme elas acontecem.

02:05

É como se fosse um stream, ela vai colocando os pedacinhos.

02:09

Com uma função convencional, eu não consigo fazer isso.

02:14

E o generator me permite fazer esses retornos dinâmicos.

02:18

Então, vamos idealizar que eu vou processar

02:22

algo e eu retorno um primeiro resultado.

02:27

Depois eu processo algo novamente e retorno outro resultado.

02:35

Este yield...

02:37

ativa o padrão Generators. Ele equivale ao retorno,

02:42

porém ele faz muito mais do que isso. Veja só,

02:46

se eu colocar aqui resultado é igual a processar algo, ao

02:55

ativar um atalho aqui do VSCode, ele me mostra a tipagem.

03:01

Então, quando eu executo essa função, ela não retorna nem um nem dois,

03:06

ela retorna um objeto que é desse tipo de Generator aqui.

03:11

Aqui, ao clicar, nós temos um

03:16

pouco do código - fonte dele, enfim, você pode dar uma olhada nisso.

03:22

Vamos fazer um print do resultado.

03:27

Então, aqui, eu vou executar esse generator.py.

03:32

Então, veja que não retornou nada. Não tem o 1 nem o 2,

03:38

eu tenho apenas o objeto. Nada na minha função aconteceu.

03:45

Vamos colocar alguns prints,

03:50

espalhados pelo código,

03:53

para que nós vejamos como

03:58

vai ser esse processo. Poxa, então se eu não consigo pegar o resultado,

04:04

como que eu executo essa função?

04:06

Nós chamamos o nextResultado,

04:10

que vai executar o próximo retorno, ou seja,

04:15

o próximo yield. Então aqui podemos passar o print, veja só.

04:24

Então temos a linha 2 executada. E a linha 4 que retornou 1.

04:30

Mas o processamento parou aqui.

04:34

Então é como se nós pudéssemos controlar a execução da função.

04:39

Para que eu veja o próximo resultado, eu tenho que fazer o outro next.

04:45

Veja só. Ele parou aqui e não mostrou o finalizando o processo.

04:51

Se eu fizer mais um, ele

04:59

vai encaixar o finalizando o processo.

05:03

Então, esse primeiro foi a linha 13 somente.

05:09

Continuando o processo 2, foi a linha 14.

05:13

E finalizando o processo mais esse erro que aconteceu, foi o próximo next.

05:19

Por quê? Eu não tinha mais nenhum yield depois,

05:24

então ele tenta

05:29

puxar até o próximo yield. Como não tem,

05:33

eu não tenho mais nada a iterar nessa função,

05:37

ele vai lançar esse erro de StopIteration que serve até o ponto de parada.

05:42

Nós sabemos que aqui não tem mais nada a ser retornado.

05:46

Então, a função é executada aos poucos.

05:51

Aqui nós estamos com dois retornos, dois yields,

05:55

mas eu poderia ter aqui um for ou um while True se

06:02

eu não tivesse um número de eventos a serem executados.

06:08

Soubesse quantos, poderia ter aqui um código que ia gerar um yield dinâmico,

06:13

retornar alguma coisa.

06:19

Então isso aqui é legal para muitas situações,

06:22

quando você tem uma gama muito grande de dados,

06:25

imagina se você está produzindo um CSV,

06:28

você pode ir fazendo a leitura desse arquivo grandão,

06:34

enorme, pouco a pouco.

06:35

Você não precisa carregar tudo para a memória.

06:38

Isso acontece também com leitura em banco de dados.

06:42

Quando utilizamos o padrão coroutine,

06:44

você vai lendo a linha pouco a pouco de uma tabela monstruosa.

06:51

Então, isso permite que a função vá retornando algo,

06:55

mas o Python permite que a gente faça um

07:01

for valor em

07:04

processar algo, o próprio resultado. Na

07:12

verdade, aqui nem seria necessário colocar

07:18

nenhum print. Está bom. Foi feito.

07:26

Então, ao executar novamente, nós vamos ver o comportamento.

07:31

Na verdade aqui sem esse etc.

07:36

Então pronto, finalizando o processo.

07:38

Então veja que ele tentou, depois do segundo retorno,

07:43

ele tentou ver se tinha mais alguma coisa.

07:46

Então o que está aqui depois desse último yield também é executado.

07:49

Ele vai lançar um erro, mas esse erro vai ser omitido para a gente.

07:56

Então, nós estamos streamando os resultados.

07:58

É o que está acontecendo aqui por detrás, mas a diferença é que,

08:02

como nós temos ainda o padrão assíncrono,

08:05

Nós estamos fazendo as execuções de I.O. usando

08:11

o event loop, que nós vamos ver depois.

08:15

Mas isso é muito legal para todas essas situações, porque,

08:19

veja, no momento que eu estou executando os agentes,

08:23

eu poderia querer apenas o evento final,

08:27

Muitas situações, sim, né? Ah, não, para mim,

08:30

se tiver 10 eventos acontecendo, eu não me importo,

08:34

eu só quero o evento que é o que o agente retornou.

08:39

Ok, mas você já usou muitas vezes o ChatGPT, Cloud

08:48

AI, qualquer coisa de IA ali no browser, e você vê que o resultado,

08:53

ele não vem de uma vez, ele vai vindo usando o streamer, vai vindo aos pouquinhos.

09:00

Então isso aqui é interessante porque eu posso pegar,

09:03

posso falar para ele não me retornar toda a resposta de uma vez,

09:07

que ele vai me retornando os pedacinhos. Desses pedacinhos, nós vamos retornando

09:13

respostas HTTP.

09:17

Então esse padrão Generator me permite ter mais controle,

09:20

mais visibilidade nessa gama de retornos,

09:24

nessa gama de eventos que estão acontecendo.

09:27

Então lembrando que esse padrão funciona... aqui no Python,

09:32

no JavaScript, em várias outras linguagens.

09:34

As principais linguagens sempre vão ter esse generator de alguma forma e

09:39

talvez ele esteja embutido em alguma biblioteca que você não está nem percebendo.

09:45

E muitas vezes ele serve para a gente poder criar essas soluções em que

09:49

nós temos uma gama de coisas acontecendo e eu quero processar pouco a pouco.

## Resumo IA

[RESUMO_IA]