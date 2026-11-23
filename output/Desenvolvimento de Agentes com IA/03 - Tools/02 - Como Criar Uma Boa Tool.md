Módulo: Desenvolvimento de Agentes com IA\
Aula: [Como Criar Uma Boa Tool](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18099)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos aprofundar um pouco mais no conceito de TO.

00:06

Nós entendemos que essa função que é declarada no agente,

00:10

o agente que está executando ela, obviamente,

00:13

mas a definição da função

00:16

é crucial para a execução dela.

00:22

Veja que nas instruções do agente no System Prompt,

00:26

não foi falado em nenhum momento...

00:30

que é para invocar essa tool quando é para listar as faturas.

00:34

Inclusive, não temos nem a palavra listar, apenas na própria tool.

00:41

Eu poderia passar uma instrução do tipo,

00:44

para listar as faturas, use a tool

00:51

Listar faturas. Sim,

00:54

em alguns momentos nós tendemos a fazer isso

00:56

para dar um direcionamento para o agente.

01:00

Mas aqui nós devemos tomar o cuidado, porque...

01:04

Nesse caso, como nós temos um agente mais simples,

01:07

isso não é necessário.

01:09

Isso que eu estou falando serve também para

01:12

as outras tecnologias de criação de agentes. O

01:18

próprio nome da tool já é sugestivo.

01:22

Então está aqui listar faturas. Quando esse agente é executado,

01:26

ele vai mandar tanto o System Prompt quanto o nome dessas tools lá para a LLM.

01:33

Então consolidando tudo.

01:36

E uma vez que eu pedir para listar as faturas,

01:39

ela vai ver que tem uma tool, ela vai pensar.

01:44

Ela é um modelo que

01:47

vai raciocinar com todo o contexto que ela tem. Então,

01:50

ela vai ver que tem uma tool de listar faturas.

01:51

Opa, então eu vou acabar executando ela.

01:57

Portanto, é crucial que o seu nome seja muito sugestivo.

02:01

Não crie aqueles nomes simplistas,

02:08

em que você tenta reduzir, às vezes, o nome do

02:13

método por qualquer motivo,

02:16

isso você faz nas suas classes convencionais fora do ambiente dos agentes.

02:24

Quanto mais sugestivo for o nome, melhor vai ser,

02:28

porque aí vai permitir que o modelo faça a inferência.

02:33

Quando você tem que fazer um system prompt,

02:35

tem que ficar quase como explicando... Cada detalhe para

02:42

o agente e para a LLM, então, há um alerta. Então,

02:47

listar faturas é um nome muito bom.

02:50

Outra dica importante, não coloque tool, porque isso

02:57

já vai ser considerado uma tool e acaba atrapalhando o contexto.

03:00

E dependendo do que você tivesse,

03:02

tool pode ser interpretado de outra forma. Então,

03:05

só coloque o nome da função conforme...

03:08

tem que ser, e obviamente aqui eu estou utilizando dentro do mesmo arquivo,

03:11

nós podemos usar todas as boas práticas de

03:14

programação para organizar isso no arquivo separado,

03:18

modularizar e etc.

03:21

Em relação aos parâmetros, nós

03:26

Podemos declarar n parâmetros ou quantos nós quisermos,

03:31

Eu poderia receber aqui qualquer outra coisa, e

03:36

A recomendação é que, para usar os tipos

03:41

Primitivos da linguagem.

03:43

Ou, na verdade, os tipos, não só os primitivos, os tipos básicos.

03:49

Exatamente porque nós estamos lidando aqui com o conceito de serialização.

03:53

Se eu, em vez do cliente ID,

03:58

Eu passasse aqui uma classe cliente,

04:02

Não é que ele não vai conseguir trabalhar, mas ele vai acabar pegando esse objeto

04:07

Porque imagina que essa informação transaciona lá para o LLM,

04:11

Então ela vai converter esse objeto em texto.

04:15

E, dependendo do que tiver dentro desse cliente,

04:18

Aqui pode ter bibliotecas e outras coisas,

04:21

Isso pode não ser serializado, dar qualquer problema. Então, a

04:27

Recomendação é usar inteiro,

04:30

String, se eu tiver que passar uma lista, não tem problema,

04:34

Posso colocar o tipo list.

04:37

Se tiver que passar um dicionário, também não tem problema,

04:40

Mas não use objetos mais complexos.

04:44

Então, não se acanhe de colocar vários parâmetros.

04:51

Essa é a dinâmica de programação com as tools.

04:56

Também em relação aos retornos. O que eu fiz de errado aqui?

05:05

Client ID, string.

05:08

Em relação aos retornos. Coloquei...

05:15

Indefinido, variável, às

05:18

Vezes, é porque a própria ideia demora para tirar.

05:23

O retorno também é importante.

05:27

Dessa forma que está aqui, não tem nenhum problema retornar.

05:32

O que acontece é que, internamente, o

05:37

SDK nunca vai retornar o dado diretamente.

05:40

Se você coloca aqui qualquer retorno dessa forma, ele sempre vai converter para um dicionário.

05:51

Então, ele colocaria assim, resultado dicionário do Python,

05:56

Que é igual a um JSON, muito parecido com um JSON.

05:59

E mais a lista, exatamente como meu

06:04

Próprio autocompletado está demonstrando aqui.

06:09

Isso aqui é ruim? Não necessariamente.

06:12

Mas é aquela história de deixar muito claro o que é o dado.

06:18

Nós estamos retornando uma lista de faturas. Então, ter um resultado,

06:24

Vai fazer diferença zero na execução do agente. Mas,

06:29

Numa situação atípica, isso pode ter a sua influência.

06:34

Então, a recomendação é que sempre retorne à boa prática,

06:40

Sempre retorne no

06:42

Dicionário.

06:47

Então, só envolver aqui no dicionário e pronto.

06:50

Porque aí, quando isso for passado lá para o LLM,

06:56

Está bem claro que eu tenho uma lista de faturas.

06:59

Nós podemos até executar de novo.

07:01

Só para desencargo de consciência. Listar minhas faturas.

07:09

Inclusive, esse warning que ele está mostrando aqui sobre o carregamento da tool,

07:15

Nós podemos desativá-lo também colocando essa instrução aqui.

07:21

Disable JSON Schema para função.

07:25

Então, agora... No próximo, ele não vai mostrar mais.

07:29

Vamos colocar aqui o cliente, 1, 2, 3, e

07:36

pronto, agora nós temos o mesmo resultado.

07:41

E até veja que o formato em relação ao que

07:44

nós vimos na última aula ficou um pouquinho diferente,

07:46

ficou até mais estruturado. Enfim, não

07:53

tem problema que no seu dicionário você tenha n key values.

08:00

Mas desde que tenha aqui chaves. Então,

08:02

com nomes também sugestivos. Não coloque aqui também result,

08:07

bori ou qualquer coisa genérica. Tudo é contexto.

08:12

Mas tem também uma outra informação crucial para tu,

08:19

que é a documentação dela.

08:24

Lembra que nós falamos aqui das três aspas

08:28

que nós podemos definir uma string multilinha? No Python,

08:32

uma das formas de gerarmos uma documentação para

08:36

uma função também é usando essas três aspas,

08:41

que é chamado de docstring. Então,

08:48

na primeira linha, coloque a documentação e quanto melhor a documentação,

08:55

mais contexto. Nós podemos falar um pouco sobre a função, aí se...

09:03

Se quisermos, podemos colocar aqui sobre os argumentos e sobre o retorno.

09:11

Isso é importante porque quando o agente vai invocar essa tool,

09:17

além

09:20

do nome da função, dos parâmetros que vão estar tipados,

09:25

a documentação da tool também é importante.

09:29

Isso vai dar ainda mais contexto para a LLM, para ela entender.

09:34

Qual tool ela vai chamar. Ela pode, na verdade,

09:38

talvez entender que ela vai chamar várias tools em batch.

09:44

Ela devolve essa informação para a gente. Nós vamos entender isso depois. Então,

09:48

essa tool que está aqui é a tool recomendada. Veja que, a princípio,

09:54

eu poderia definir uma tool muito simples e isso poderia ser ruim.

09:59

Então, esses conhecimentos aqui são os conhecimentos cruciais.

10:03

Para que você consiga criar um bom agente utilizando as tools.

## Resumo IA

[RESUMO_IA]