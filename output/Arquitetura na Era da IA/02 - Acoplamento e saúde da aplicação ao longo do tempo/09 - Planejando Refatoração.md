Módulo: Arquitetura na Era da IA\
Aula: [Planejando Refatoração](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18119)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, agora que a gente viu os problemas que nós temos,

00:05

se você for olhar o nosso gráfico aqui e tudo mais,

00:09

qual que seria o primeiro passo, no final das contas,

00:13

para fazer a nossa refatoração ou, eventualmente,

00:19

o nosso alerta e etc.

00:22

Então, o que a gente precisa fazer é primeiro ter uma rede de segurança.

00:26

Eu sei que esse software que a gente desenvolveu tem testes, porém, o que acontece?

00:32

Nós temos que pensar de forma,

00:35

se eu for tentar fazer uma refatoração ou fazer com que esse

00:39

meu software consiga sair dessa zona de dor e ir para outro lado,

00:43

eu preciso garantir que existam testes suficientes para eu não ter medo,

00:49

de forma geral, de fazer mudanças.

00:51

Por outro lado, a gente tem um outro problema. E o problema é o seguinte.

00:56

Muitas vezes, softwares que têm um acoplamento muito forte,

00:59

eles são difíceis de testar, porque dentro deles tem o famoso new.

01:05

Quando você instancia um componente dentro de uma classe,

01:11

o acoplamento ali é extremamente forte. Então, até mesmo para testar,

01:16

a gente acaba tendo esse tipo de problema. Então,

01:18

o que eu vou fazer aqui pra gente começar, tá? Então, primeira rede de segurança,

01:23

testes, tá? Eu não vou usar, não vou fazer nenhuma mágica,

01:27

cada pessoa pode ter uma skill. Eu aqui no Cloud Code, tá?

01:32

Eu vou... fazer um prompt extremamente simples,

01:36

porque ele também não é um software complexo, tá?

01:39

Ele tem ali um plugin que se chama Superpowers pra ele disparar diversos agentes,

01:43

mas eu poderia colocar manualmente.

01:45

Também eu não vou nem mudar de branch aqui, tá, galera?

01:48

Vou seguindo aqui no main por conta de exemplos que a gente vai trabalhar.

01:52

Então, eu vou colocar aqui...

01:54

Eu vou colocar aqui pra ele...

02:02

Deixa eu ver se ele consegue aqui.

02:04

Dispatching Parallel Agents.

02:06

Basicamente o que eu estou falando é usar vários agentes

02:09

em paralelo para fazer a verificação do meu programa.

02:11

Para tentar ir um pouco mais rápido. Vamos ver se isso aí ajuda,

02:13

mas eu poderia colocar. Então eu coloco assim, ó.

02:16

Verifique no software.

02:19

Verifique qual

02:22

é o nível de cobertura de testes desse software. Também

02:32

verifique

02:35

os componentes que estão

02:39

em uma zona de dor.

02:44

E aqui eu posso passar para ele a documentação,

02:49

caso queira, que é o main sequence, arroba HTML.

02:54

Eu posso colocar veja ou arroba main sequence, main sequence

03:01

ponto HTML.

03:05

Verifique os componentes de dor.

03:12

principalmente, e

03:15

também o grau de dificuldade que teríamos para

03:23

fazer uma refatoração

03:26

nesses componentes mais críticos.

03:31

Então, o que eu estou pedindo aqui para ele, de forma geral,

03:34

é ele fazer uma análise de cobertura de testes.

03:41

Obviamente, sistemas determinísticos na hora que eu vou rodar para

03:46

que ele consiga trazer a cobertura de testes e tudo mais.

03:49

Mas também, eventualmente, eu consigo fazer isso também.

03:52

E trabalhar de forma determinística para esse tipo de coisa é muito melhor.

03:57

Aqui ele está criando aqui,

03:58

falando que ele vai usar uma skill para despachar agentes paralelos.

04:01

E essa análise tem três domínios independentes. Cobertura de teste.

04:06

Componentes de zona de dor, dificuldade de refatoração.

04:09

Basicamente é assim que ele vai espalhar os documentos aqui para a gente.

04:12

E ali ele falou, já tem alguns dados,

04:14

então agora aqui ele está despachando os agentes

04:17

para que ele consiga fazer essas verificações.

04:22

Se você olhar,

04:24

ele percebeu que a gente está

04:25

usando a parte do V-Test ali.

04:31

Então, ele já deu um menos, menos coverage. Então, rodando aquilo, ele já,

04:36

de forma determinística, ele consegue já trazer o nível de cobertura.

04:39

Então, ele mesmo, obviamente,

04:40

foi esperto o suficiente e executou a parte

04:44

de cobertura utilizando isso de forma determinística,

04:47

usando a parte do framework de testes aqui da nossa aplicação. Então,

04:51

eu acho que esse aí é o principal ponto que a gente tem que ligar.

04:55

Se eu olhar aqui no cloud, eu vejo os agentes que ele criou e aqui dois,

05:01

e ainda estão ativos, outros já terminaram, né? Aqui é analisar a cobertura de teste,

05:05

eu acho que esse foi o mais simples,

05:06

porque ele teve ferramenta ali para fazer do framework de teste,

05:10

tá? Agora, vamos aguardar as outras ferramentas aqui terminarem,

05:16

e a gente já volta para que a gente consiga entender,

05:20

né? O que a gente tem nessa aplicação em relação a teste, tá?

05:25

Então... Passo 1, em relação ao acoplamento e etc., a qualquer mudança,

05:30

a gente tem que fazer esses tipos de cobertura ou ter

05:34

uma rede de segurança de testes aí para a gente.

05:38

Bom, galera, para sermos honestos aqui com a nossa inteligência artificial,

05:42

ele gerou diagnóstico,

05:44

mas tem uma parada aqui que já é fogo, né?

05:46

Olha só, cobertura de testes, rede de segurança ilusória.

05:51

Não há cobertura quantitativa mensurável. O provider aqui do teste, o Cover V8,

05:57

não está instalado e não há um script de coverage no package.json.

06:01

Jason, lembra que eu falei que ele estava indo atrás de forma determinística?

06:05

Qualquer percentual seria inventado.

06:08

O que dá para afirmar com evidência é 11 arquivos de teste,

06:11

54 testes, 53 passando. A maioria são assertões rasas,

06:15

verificando o tipo de retorno. Não o valor do negócio.

06:19

Dos 35 arquivos em SRC, só 11 têm alguns testes. Sem teste,

06:23

ele trouxe aqui. Os três caminhos críticos estão deliberadamente ausentes. Ou seja,

06:30

confirmado lendo os testes aqui. Bom,

06:33

nesse momento, eu posso tomar algumas decisões.

06:37

A primeira decisão é, eu quero ter isso no script mais mensurável,

06:42

então, antes de fazer qualquer coisa, eu falo, instale, então, né?

06:47

o nosso provider pra rodar a cobertura de testes, tá?

06:52

Mas existe uma coisa que é importante, tá, galera?

06:56

Não é porque você tem X % de cobertura de

07:01

testes que você pode ter uma rede de segurança forte. Por quê?

07:05

Porque existem testes como esse. Verifica o tipo de retorno. Ou seja,

07:11

você tem a falsa sensação que o seu software está sendo bem testado,

07:17

mas no final das contas ele está testando que 1 mais 1

07:20

é igual a 2 sem gerar valor para o negócio.

07:23

Então vamos tentar entender a linha de raciocínio dele e aí a

07:26

gente vê o que a gente faz em relação a isso.

07:30

Então ele falou, os três caminhos críticos estão deliberadamente ausentes,

07:34

confirmando os testes.

07:36

Decremento de estoque está ausente.

07:39

cálculo de cupom de desconto sem acerção de valor e falha de pagamento,

07:45

está com um skip que é importante,

07:49

não dá para ele forçar. O ponto pedagógico,

07:53

a suíte está verde, esconde os três comportamentos financeiros.

07:59

que não tem verificação real e o caso de pagamento recusável

08:01

é intestável por conta da ausência de injeção de dependência,

08:05

defeito arquitetural que a gente plantou. Ou seja,

08:08

a gente plantou um monte de erro de propósito aqui nesse projeto.

08:12

Zona de dor, confirmado, cinco módulos,

08:14

todos estáveis, ou seja, muitos dependem dele,

08:18

e concretos com A igual a zero, ou seja,

08:21

ele não tem contrato. O ranking por risco real é esse,

08:24

então ele trouxe o ranking aqui para a gente dos arquivos,

08:29

que são mais complexos nesse caso,

08:32

e ele trouxe agora alguns insights em relação a logger,

08:35

duplicação de trio, dificuldade de refatorar, ele trouxe os principais caras aqui,

08:41

e muitos deles podem ser classes deuses, ou seja,

08:45

uma classe que o acoplamento diferente

08:50

é muito grande ali no nosso caso.

08:53

Ele trouxe ciclos de dependência, legacy order processor, etc.

08:58

e tudo mais. Então, galera, se vocês olharem,

09:01

a gente tem que tomar algumas decisões aqui para frente.

09:04

Uma é instalar aquela cobertura de código, isso aí é uma coisa interessante.

09:09

E a outra coisa é a gente tentar criar um plano

09:12

básico para a gente refatorar de forma geral aqui o nosso sistema.

09:18

Porém, o que eu gosto de fazer? Muitas vezes, colocar o pé na água para ver,

09:23

se o que a gente está fazendo está ok,

09:25

porque eu poderia pedir aqui, saia refatorando e etc e tudo mais,

09:29

e provavelmente ele faria,

09:30

e muitas vezes ele faria inclusive muito bem.

09:33

Eu acho que o grande aspecto aqui no meio de toda essa história é,

09:37

eu queria entender como que ele faria uma refatoração. E não só isso,

09:42

eu gostaria de criar um plano que fique mais fácil. E agora,

09:45

nesse momento que a gente tem que pensar... Da forma seguinte,

09:49

a gente tem um software que ele tem problemas. Esse aqui é um olhar de arquiteto.

09:53

Eu não estou preocupado nesse momento aqui em automatizar e criar

09:57

Um monte de skill para ele resolver esse problema.

09:59

Eu posso fazer isso depois,

10:00

mas eu quero aqui nesse vídeo e nessas aulas de arquitetura

10:04

onde a gente está focando é entender a raiz,

10:06

entender o conceito e depois você consegue automatizar de forma geral.

10:11

O ponto aqui interessante que ele trouxe é em relação a...

10:18

as situações que acabam trazendo aqui.

10:22

Então, a partir de agora, o que eu vou fazer?

10:25

Eu vou continuar iterando com a IA para ver como

10:27

a gente consegue trabalhar aqui com ela nesse aspecto.

10:31

Então, a primeira coisa que eu posso pedir aqui para

10:37

ela em relação a tudo

10:39

isso é instalar a ferramenta

10:46

para fazer a cobertura de código.

10:48

O que mais que eu posso pedir para ela fazer aqui para mim, tá?

10:54

Para ela, no final das contas,

10:56

fazer essa verificação de todos os outros aspectos para a gente trabalhar. Então,

11:04

nesse ponto aqui, o que eu quero fazer?

11:07

Eu vou mudar o cara aqui para o modo planejamento, tá?

11:13

E vou chegar agora aqui o seguinte, olha.

11:16

Preciso que você crie

11:20

um plano efetivo, obviamente, deveria ser efetivo,

11:25

para instalar os

11:28

componentes e bibliotecas para

11:33

fazer a verificação de cobertura de código,

11:39

mas determinística,

11:43

determinística,

11:46

revalidar.

11:48

Uma coisa que é interessante, galera,

11:51

a IA muitas vezes sai soltando um monte de agentes, etc.

11:54

Mas antes de você gerar qualquer plano ou coisa desse tipo,

11:57

eu recomendo que você peça,

11:58

revalide algumas informações.

12:00

Precisa revalidar os componentes mais críticos e

12:08

crie um plano de refatoração para

12:13

apenas

12:16

um componente crítico para verificarmos

12:22

se essa linha de refatoração pode ser

12:28

seguida.

12:32

E vou dar um Enter aqui.

12:34

Agora, tem uma outra coisa e uma dica que eu vou dar para vocês em seguida,

12:38

assim que ele consiga fazer essa análise ali para a gente,

12:44

tá? Então, vamos aguardar ele fazer essa análise,

12:46

vamos esperar um pouquinho e a gente já volta aqui.

12:50

Bom, outra coisa que ele fez aqui então, né?

12:52

Ele gerou qual componente piloto que eu gostaria...

12:55

pra gente utilizar, que é um cara crítico e etc,

12:59

pra refatoração, validar se a linha de refatoração se sustenta.

13:04

Eu vou colocar aqui para a gente no Payment Gateway,

13:08

porque ele é um cara que tem uma interface

13:13

E não está sendo muito utilizado e tudo mais,

13:16

Porque ele é utilizado no Order Service, isso aqui é um aspecto,

13:21

E tem outro ponto aqui também, tá?

13:24

Como existem partes do nosso software que não têm nem a cobertura de teste,

13:29

Um dos pontos que a gente vai ter que ajustar, inclusive,

13:32

Nesse plano é por onde que ele deve começar.

13:35

E o nosso primeiro ponto que ele tem que começar é pela nossa,

13:39

Como que eu posso dizer?

13:42

Pela nossa rede de segurança. E o que é uma rede de segurança?

13:46

Criar testes que ainda não foram criados.

13:50

Ou seja, garantir essa cobertura de código.

13:52

Antes de eu sair mexendo nesses caras aqui.

13:55

Então, primeiro ele está analisando,

13:57

Então perceba que esse meu plano vai ter algumas etapas aí,

14:00

Uma das etapas é um piloto de um componente crítico,

14:05

Mas perceba que eu vou iterar aqui e vou falar, cara,

14:09

Antes de qualquer componente crítico, eu preciso de uma rede de segurança,

14:12

De verdade,

14:13

Então eu preciso que você escreva esses testes aqui pra gente, tá? Então...

14:20

Vamos aguardar aqui, ele está falando que ele tem tudo o que precisa, etc, etc.

14:25

Bom, galera, ele gerou o plano aqui pra gente,

14:28

Vamos lá. Então, a primeira coisa que ele trouxe aqui, parte

14:34

A, NPM Run Coverage, vamos lá, tem mais que contexto,

14:39

Switch passa, componentes críticos, aqui, esse plano tem três coisas pedidas.

14:47

Tornar a verificação de cobertura determinística, revalidar os componentes críticos,

14:51

Executar uma refatoração piloto,

14:53

Injetar a interface do Payment Gateway no Order Service,

14:57

Aqui pra gente,

14:58

Pra provar que a linha de refatoração do Guia se sustenta no meio da história.

15:03

Então, isso é um ponto importante. Então,

15:05

Ele está falando o que ele vai fazer. Primeira coisa,

15:07

Vai instalar o Provider, vai criar os arquivos e tudo mais,

15:11

Git Ignore, revalidar os componentes críticos,

15:16

E etc. Mas antes de eu fazer isso, o que eu vou fazer?

15:20

Eu vou iterar aqui com ele e vou falar que

15:22

Antes disso, eu quero também que os testes sejam escritos,

15:27

Tá? E daí a gente vai falar um pouquinho de TDD, de Test Driven Development também,

15:31

Tá? Então, vamos nessa somente para esse vídeo não ficar gigante.

## Resumo IA

[RESUMO_IA]