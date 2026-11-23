Módulo: DevOps e SRE com IA\
Aula: [MCP & Langfuse pt4](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18510)

## Resumo da aula



## Transcrição

00:00

Então vamos fazer o seguinte, vou descarregar ele no local,

00:03

vou dar um eject nele aqui, vou iniciar ele de novo, vou

00:09

ejectar ele, se vocês notarem aqui, deixa eu pegar meu monitor de atividade,

00:12

como é que ele já estava, quando eu ejectei já desceu aqui, até lá embaixo.

00:17

Então vamos pegar

00:21

aqui esse cara,

00:25

vamos carregar de novo e fazer um teste.

00:30

Cadê gente? Sumiu?

00:32

LLM Studio. Vamos carregar ele de novo.

00:34

Vamos subir ele aqui.

00:37

Vamos aumentar a capacidade dele aqui.

00:39

E vamos aumentar aqui para um contexto de 17 mil. Agora ele vai fritar mesmo.

00:44

Vamos lá. Vamos subir esse LLM aqui. Ok.

00:50

Vamos mandar a mesma mensagem para ele aqui. Aqui eu já aumentei muito o contexto.

00:55

Deixa eu criar um novo aqui. E vamos jogar aqui de novo. Bora.

01:01

Agora o contexto vai estar um pouco menor.

01:12

Olha lá. Está analisando.

01:15

Está fazendo aqui. Open UI. Do resource.

01:18

Agora ele foi até mais rápido. Conseguiu já achar. Resource pod.

01:23

Resource cat k8s namespace. Ó, achou o pod. O pod tal, tal, tal.

01:28

Run it red. Agora ele está pegando os logs. Pegou os logs.

01:32

Agora ele vai fazer a parte aqui do... Tem muito log.

01:36

Por isso que estourou o contexto. Então aqui ele me deu a análise completa.

01:39

Os logs mostram como a API está operacional, está restando em localização HTTP,

01:43

normais, com código 200 e assim por diante.

01:46

Então a gente consegue, direto dentro do Kubernetes, fazer essas análises.

01:51

Legal? Eu vou dar um stop aqui, para não terminar,

01:54

porque senão meu computador vai fritar aqui. Vou dar um reject aqui.

01:58

E a gente tem agora o nosso agent aqui rodando. Legal?

02:03

Então a gente consegue fazer a mesma coisa para o Prometheus,

02:06

que a gente tem lá. Estou fazendo uma demonstração para vocês aqui. desse carinha,

02:10

e eu vou deixar o Prometheus e o Lock

02:13

para vocês configurarem e fazerem os testes aí,

02:16

e validar o funcionamento dos outros agents. Legal?

02:22

Então, a gente tem aqui algumas perguntinhas que você pode fazer,

02:27

porque o meu deployer iniciou, vai no Event Lead, mas o query rende aqui,

02:31

então a gente tem várias possibilidades, tá? Para configurar o Prometheus,

02:35

bem simples, vamos configurar ele rapidinho aqui para vocês.

02:41

Então, vamos aqui em espaço de trabalho.

02:44

Cadê? Painel do admin. Configurações.

02:49

Integrações. Falei espaço de trabalho, mas não é não,

02:51

gente. É para o painel do admin.

02:53

Vamos ver se a gente consegue duplicar esse cara. Será que tem como? Não,

02:56

acho que não tem como, não. A gente tem que adicionar um novo. Então, vamos lá. Prometheus.

03:04

Então, aqui tem a descrição.

03:05

MCP Prometheus.

03:09

O que a gente vai ter aqui? A gente vai ter uma RL base,

03:11

que vai ser http://mcpo 2

03:16

.8000 barra que a gente tem,

03:22

vou voltar aqui, vamos pegar o nome certinho, do Prometheus. Prometheus.

03:28

Aqui em avançado você vai manter, barra aqui você coloca nenhum.

03:32

Faz um teste de conexão, tudo funcionando. Ok, salvo.

03:36

Então, vamos fazer só um teste rápido aqui com

03:39

uma pergunta que a gente tem lá dentro.

03:41

Vamos aqui dentro do nosso troubleshoot do Kubernetes, editar,

03:47

vamos ativar o Prometheus para dentro dele também.

03:50

Legal? Agora eu quero ver essa máquina fritar agora de jeito.

03:54

Kubernetes troubleshoot, vamos pegar lá no nosso slide uma pergunta.

04:01

Que vai usar aqui, tipo assim, por que meu pod reiniciou?

04:04

Por que meu deployment reiniciou?

04:06

Na verdade não teve nenhum deployment que reiniciou.

04:09

Mas vamos fazer essa pergunta aqui para ele, ver o que ele consegue me retornar.

04:15

Vamos lá. Por que meu deployment reiniciou?

04:18

Pergunta aqui que está meio sem contexto. Ele vai fazer aqui as chamadas.

04:22

Agora ele tem o Prometheus para usar também.

04:25

Vamos ver se ele não vai estourar o meu contexto, né?

04:27

Está um pouco maior, mas não está muito grande igual os negócios aí.

04:33

Deu um pod list, não conseguiu achar nada. Pod resource não achou nada.

04:39

Então aqui, tool investigation pod.

04:41

Ele já começou a chamar um dos seus diferentes ali. Que legal.

04:45

Então ele conseguiu fazer isso aqui. Análise do Kubernetes.

04:50

Deixa eu abrir isso aqui de novo. E openada.

04:54

Vamos pegar aqui um Prometheus / docs.

04:58

E aqui a gente vai conseguir exatamente todas as possibilidades dele. Está aqui. Então, vamos formatar aqui.

05:04

A gente tem todas as tools que ele tem disponível para ser usada pelo LLM.

05:10

Então, ele até agora está no Prometheus aqui. No Prometheus 1, no K8S.

05:15

Ele está tentando achar um namespace de MBA App, sem especificação de contexto.

05:21

Então, eu acho que ele não vai conseguir achar.

05:24

Get Cluster Health Post Tool.

05:28

Ah, esse aqui é legal.

05:31

Esse cara aqui... Ele é do Prometheus. Essa chamada aqui é do Prometheus. Tu,

05:40

vamos ver. Tu, Get Cluster. Vamos ver.

05:44

Opa, não consegui copiar. Vamos ver.

05:50

Vamos pesquisar essa tu aqui. Tu,

05:55

Get Cluster.

05:59

Get Cluster. Não, não é do Prometheus não. Esse aqui é do K8s mesmo.

06:08

Ele ainda está fazendo algumas coisas lá dentro do Prometheus.

06:11

do K8s, do Diagnostic, Namespace Diagnostic.

06:17

Então aqui tem uma saída, PVC

06:21

Usage, e assim por diante. O computador começou a fritar de novo aqui, gente.

06:27

Tá ventoinha, tá fazendo até barulho.

06:31

Não vai dar não. Vou

06:34

cancelar aqui, como eu não tenho nenhum LLM pago,

06:38

eu não vou dar continuidade aqui não, mas se vocês tiverem,

06:42

sugiro vocês testarem aí as ferramentas do Prometheus que a gente tem disponível.

06:48

Então, a gente tem várias aqui. Diagnostic Namespace.

06:50

Ah, essa ferramenta é essa aqui mesmo.

06:53

Diagnostic Namespace. Aqui, ó.

06:57

Diagnostic Namespace. Ele está chamando o Prometheus ali,

07:00

que está conectado com o nosso...

07:02

Vamos ver como é que está a memória lá?

07:05

Vou mostrar para vocês a memória. Está queimada.

07:09

O computador até esquentou aqui agora.

07:13

Então... Vamos injetar esse modelo aqui para dar uma descansada na máquina aqui.

07:18

Mas vocês conseguem usar.

07:20

Está vendo que ele está usando já as tools do Prometheus,

07:21

que está retornando informações sobre o nosso cluster Kubernetes.

07:24

Então, PVC usage,

07:26

a gente tem aqui várias atividades que a gente

07:28

pode fazer a chamada lá dentro do cluster. Esse aqui,

07:33

esse cluster health-check que também ele fez a chamada lá dentro. Então,

07:37

se estiver tudo conectado bacaninha, ele consegue trazer os resultados lá de dentro

07:42

do cluster Kubernetes e puxar essas informações para a gente, tá?

07:45

Para meter os dados no monitoramento lá de dentro do cluster.

07:50

Ok, pessoal? Então, vamos ver aqui a observabilidade, né?

07:57

Se a IA está operando na sua infraestrutura, quem observa a IA?

08:01

Então, agora a gente vai passar aqui para a parte do LensFuse.

08:05

Então, todas as perguntas que a gente fez, tudo que a gente chamou,

08:08

todas as pipes que a gente chamou,

08:10

a gente vai precisar ver o que está acontecendo, tá bom?

08:13

Então a gente vai ter algumas pipelines aqui dentro do próprio Light do OpenMBI,

08:18

que vai fazer esse report para dentro do LensFuse,

08:21

e lá a gente vai conseguir ver todas as partes

08:24

aí das chamadas que a gente está fazendo, tá bom?

08:28

Então o LensFuse vai ter um filter function dentro do OpenMBI,

08:34

beleza? Então a gente vai criar esse filter function,

08:36

toda chamada que eu fizer vai passar por isso.

08:39

Passar para esse filtering function e vai enviar para o nosso LensFuse.

08:43

Toda chamada que eu fizer dentro do OpenAPI e

08:45

a gente vai conseguir ver a observabilidade, tá bom?

08:49

Então, a gente viu aqui um pouco de MCP,

08:51

fizemos uma demo aqui de um troubleshoot conversacional.

08:54

Claro que eu tive uns problemas aqui com o LLM local,

08:57

porém, vocês aí, se tiver um LLM pago,

08:59

uma API que vocês usam, vocês podem testar que ele não vai dar problema,

09:04

vocês vão conseguir puxar tudo certinho.

09:06

E aqui na observabilidade de IA, a gente...

09:08

Viu que vai usar o LensFuse Filter

09:11

dentro do OpenMBI para fazer o rastreio disso,

09:16

ver realmente o que está acontecendo dentro do OpenMBI,

09:20

lá dentro do LensFuse. Então,

09:24

o próximo bloco aqui, a próxima parte,

09:26

a gente vai ter a observabilidade de agente. Então,

09:29

a gente vai criar esse LensFuse Filter, vai colocar dentro do OpenMBI e vai ver ali,

09:34

basicamente, como essas informações são entregues para a gente.

09:38

Então é isso, pessoal,

09:40

nessa parte aqui é isso.

09:42

Nos vemos na próxima e última etapa desse módulo. Abraço, tchau.

## Resumo IA

[RESUMO_IA]