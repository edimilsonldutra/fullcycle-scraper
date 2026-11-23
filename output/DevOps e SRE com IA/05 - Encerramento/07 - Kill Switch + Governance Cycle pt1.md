Módulo: DevOps e SRE com IA\
Aula: [Kill Switch + Governance Cycle pt1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18546)

## Resumo da aula



## Transcrição

00:00

E aí pessoal, partimos aqui para a nossa demo 2.

00:07

Primeiro, antes de começar a demo 2,

00:09

vamos solucionar o problema que a gente teve na aula passada,

00:13

no vídeo anterior, tá bem? Que era o nosso problema com o LingFuse.

00:18

Então, como a gente tinha visto,

00:19

o LingFuse não estava conseguindo enviar nenhum tracing para...

00:23

O OpenMBI não estava conseguindo enviar os traces para o LingFuse.

00:28

Então eu fiz algumas investigações aqui e achei aquele famoso,

00:32

faltou o ponto e vírgula no final do código, no final da linha.

00:35

Então basicamente, qual que é o problema que a gente tinha aqui, tá?

00:39

Os fluxos que rodam aqui em funções, esses negócios,

00:44

eles precisam de um cabeçalho específico aqui em cima,

00:47

tá bem? E esse cabeçalho estava faltando. Esse cabeçalho,

00:51

ele faz com que a gente consiga instalar...

00:56

algumas bibliotecas que vão ser usadas no código aqui para baixo.

00:58

Um exemplo é essa biblioteca do LingFuse. Então,

01:01

se a gente não tiver esse cabeçalho,

01:02

se o pod for reiniciado, alguma coisa assim do tipo,

01:06

a gente vai ter problemas

01:10

para rodar o LingFuse aqui dentro,

01:14

porque ele não vai ter a biblioteca instalada. Então,

01:17

basicamente, o que a gente fez aqui? O que eu precisei fazer?

01:21

Eu precisei pegar o cabeçalho correto.

01:24

para colocar aqui dentro, para ele conseguir fazer a instalação.

01:27

O cabeçalho nada mais é que segue com

01:29

algumas partes aqui que vão ser o título, essas coisas.

01:35

Deixa eu colar ele aqui para ficar mais fácil para mostrar.

01:37

Então a gente vai ter o título aqui da nossa função, o autor, a data, a versão,

01:42

a licença, uma descrição e aqui por último o requirements.

01:46

O que é esse requirements,

01:48

gente? Ele basicamente vai falar quais são as

01:50

bibliotecas que eu vou precisar instalar.

01:52

Na primeira vez ou quando esse cara for rodar. Então, toda vez que ele for rodar,

01:55

ele vai fazer a tentativa de instalação dessas bibliotecas.

01:59

E, por exemplo, instalou uma vez, beleza.

02:01

Na próxima ele vai tentar e vai só falar que já está instalado.

02:04

Mas se por um acaso o seu pod for reiniciado, e ele é um stateless,

02:09

então pode acontecer de fato ele reiniciar, ele vai tentar instalar de novo.

02:15

Então a gente não perde a função.

02:17

Ela vai funcionar sempre porque ele sempre vai

02:20

tentar fazer a instalação aqui do LingFuse.

02:22

Então basicamente o problema era esse.

02:24

Então foi simples aqui de resolver e eu vou

02:26

disponibilizar esse ajuste aqui lá dentro do nosso módulo 4,

02:31

tá? No módulo anterior para vocês não terem esse problema. Legal?

02:36

Mas foi bacana para a gente ver que somente um cabeçalho aqui dá um problema e são...

02:41

e assim, os problemas moram nos detalhes, né?

02:45

Então a gente conseguiu resolver simplesmente ajustando

02:47

o cabeçalho aqui do nosso código.

02:51

Legal? Para o OpenMBA exclusivamente. Ok? Então vamos fazer só um teste aqui.

02:56

Eu já coloquei lá e já salvei.

02:58

Vamos fazer um teste aqui, tipo, vou colocar. Olá,

03:02

Esse é um teste de tracing do

03:08

LangFuse.

03:11

Vamos dar uma olhada aqui no LangFuse, se ele vai chegar.

03:17

Ó, 11:27.

03:19

Temos aqui, ó. Esse é um teste de tracing do LangFuse. Tudo gerado, com o usuário,

03:25

com a LLM response e assim por diante. Então,

03:28

temos aqui os nossos tracers funcionando perfeitamente a partir de agora.

03:32

Tá? Então, vamos lá. Voltando aqui para a nossa demo 2,

03:36

nós vamos falar agora um pouco de QSuite e Governance Cycle.

03:40

O que é isso, cara? Nós vamos, de novo, fazer uma injeção.

03:46

Injetar um problema dentro do nosso servidor, do nosso API.

03:51

Vamos usar o SRE Troubleshoot para tentar diagnosticar e

03:55

agir em cima desse problema com o QSuite ativado,

03:58

que vai bloquear as coisas aqui que vão ser

04:02

feitas e o humano depois vai desabilitar o QSuite.

04:09

E vai fazer a nova tentativa de approve e reject para ver se vai funcionar.

04:14

Então aqui é o ciclo de governança, reject action,

04:16

humano recusa, approve action e assim por diante.

04:20

O QSuite vai bloquear todas as opções até a desativação

04:24

e o LangFuse vai registrar tudo através do audit trace.

04:28

Então vamos iniciar aqui. Mas antes de iniciar, eu queria fazer uma coisa.

04:33

Vamos criar um agent dedicado para injetar problemas. Então vai ser inject fault.

04:41

Vou criar esse cara aqui que vai chamar inject.

04:43

Inject Fault lá dentro da

04:47

nossa lista de modelos disponíveis.

04:51

Então, vou colocar o mesmo nome aqui,

04:53

Inject Fault to API.

04:59

Bem simples aqui, só para ter um prompt de sistema mesmo,

05:03

selecionar Inject Fault aqui e selecionar a nossa opção aqui de chamada nativa,

05:09

opção de baixo. Opção nativa aqui, salvar.

05:13

Temos aqui o inject fault e após isso nós vamos aqui pedir no

05:18

SRE Troubleshoot, vamos editar ele e desativar o inject fault dentro dele então

05:24

ele vai ficar com Kubernetes Prometheus Incident MCP, ok? Então vamos lá, primeira

05:30

coisa que a gente vai fazer é selecionar aqui o inject fault, fechou?

05:36

Selecionar o inject fault e vamos pedir para ele inserir

05:40

um problema para a gente lá dentro do nosso serviço.

05:46

Beleza? Então, vamos lá. Vamos pedir para ele gerar.

05:51

Simule um crash loop

05:57

backoff no API.

06:02

Simples assim. Vamos pedir para ele injetar esse problema lá para a gente.

06:07

Já respondeu aqui. Já está injetando o problema. Ok.

06:14

Temos aqui um problema injetado lá e já temos aqui um pod em crash loop backoff.

06:22

Backoff não, backoff.

06:25

Então esse problema vai ficar ocorrendo aí até a gente conseguir solucioná-lo.

06:31

Então, vamos agora tentar diagnosticar esse problema.

06:36

Como que a gente vai fazer? SRE Troubleshooter e vamos pedir para ele. Diagnostic.

06:44

O problema que está ocorrendo com

06:49

os pods do API. Vamos ver.

06:57

Vamos ver qual vai ser a resposta dele aqui. Ok, está tentando nadar um get pod.

07:04

Não encontrei nenhum pod com o nome App API.

07:09

Achou um App API deployment ali, detalhadamente.

07:11

Ele está pegando os problemas aqui do pod e fazendo a verificação,

07:15

fazendo o diagnóstico inicial que é agora. Legal?

07:20

Vamos esperar um pouquinho aqui.

## Resumo IA

[RESUMO_IA]