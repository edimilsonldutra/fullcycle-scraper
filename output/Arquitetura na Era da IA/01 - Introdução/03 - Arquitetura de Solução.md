Módulo: Arquitetura na Era da IA\
Aula: [Arquitetura de Solução](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18108)

## Resumo da aula



## Transcrição

00:03

Bom, pessoal, no vídeo anterior a gente falou ali mais

00:06

sobre arquitetura tecnológica e também arquitetura corporativa,

00:10

né? A gente fez um resumo ali no meio de toda essa história.

00:12

E agora a gente vai falar sobre arquitetura de solução. Essa aqui,

00:18

ela é muito importante para esse nosso módulo. Por quê?

00:21

Porque a arquitetura de solução, ela fica entre o negócio e a tecnologia.

00:26

Ela pega uma necessidade de negócio e transforma isso numa solução viável.

00:30

E repara que eu falei solução,

00:32

não necessariamente um software novo que a gente vai desenvolver.

00:36

Às vezes a melhor solução é criar um sistema novo,

00:39

mas às vezes é integrar sistemas existentes, às vezes é comprar ali um SaaS,

00:44

às vezes é automatizar um processo e às vezes é

00:46

mudar algum fluxo operacional ou combinar várias coisas.

00:50

Então a arquitetura de solução olha para o problema

00:52

como um todo e ela considera sistemas existentes, integrações,

00:57

dados, pessoas, processos, fornecedores, custos, risco,

01:00

operação e impacto ali pro negócio,

01:03

então imagina que uma empresa quer melhorar o

01:05

atendimento ao cliente usando tecnologia. A

01:07

arquitetura de solução não deveria começar perguntando qual

01:10

framework utilizar. Ela deveria entender o problema,

01:13

o atendimento tá caro, tá lento, tem muita

01:16

pergunta repetida. O time de suporte não encontra informação?

01:19

O cliente está esperando demais?

01:21

A empresa precisa reduzir custo? Qual é a melhor experiência que eu posso dar?

01:25

Você quer aumentar a escala? A gente quer atender mais canais?

01:29

Então, dependendo da resposta, a solução pode ser completamente diferente.

01:33

Pode ser um chatbot, pode ser uma base de conhecimento melhor,

01:36

pode ser uma automação interna para um atendente ou

01:41

pode ser uma integração com o CRM.

01:43

Não interessa. O grande ponto pode ser até a utilização da IA.

01:47

Mas a ideia pode ser, de

01:52

forma geral, simplesmente melhorar um processo.

01:54

Então você consegue perceber a diferença que a

01:56

arquitetura de solução não é sair implementando.

01:58

É desenhar uma solução que resolve um problema do negócio de forma viável.

02:04

Então, normalmente, quando a gente está falando em arquitetura de solução,

02:09

eu consigo trabalhar com um jogo de Legos, vamos dizer.

02:12

Então, imagina que eu tenho uma determinada aplicação,

02:17

que ela tem que falar com uma outra aplicação,

02:19

e no meio de tudo isso eu posso perder dados. Então, eventualmente,

02:23

eu posso colocar camadas intermediárias que garantam que

02:27

esses dados não vão ser perdidos.

02:29

Imagina que eu tenho um software A, um software B,

02:32

eu posso jogar isso para um Apache Kafka,

02:34

o Apache Kafka pode jogar isso para um outro sistema,

02:37

pode ter um filtro de dados, pode trabalhar com outras...

02:42

para daí o dado chegar já pronto ali para o software B.

02:46

Ou diversos microserviços precisam se conversar naquele momento.

02:51

Como que vai ser a orquestração desses caras?

02:53

Quais são as tecnologias que eu vou utilizar?

02:56

Qual vai ser, sei lá, o cloud provider que eu vou utilizar?

03:00

Quais ferramentas que o cloud provider,

03:02

soluções que ele pode trazer para eu conseguir montar isso de uma forma mais rápida?

03:07

Por outro lado é...

03:09

Será que essas ferramentas não vão trazer um lock-in muito

03:12

forte onde eu vou ficar preso nesse cloud provider?

03:15

Então, quando a gente está falando em arquitetura de solução,

03:18

a gente está pensando muito em requisitos, inclusive,

03:22

não funcionais do sistema. A gente está pensando em latência,

03:27

a gente está pensando em carga de usuários,

03:30

a gente está pensando em escala,

03:32

e isso muda completamente a forma de como você desenvolve software.

03:35

Uma coisa é desenvolver um software...

03:38

para atender 100 pessoas, outra 1.000, outra 10.000, outra 1.000.000.

03:43

Então perceba que a solução, a forma de como isso é feito...

03:48

muda completamente a estrutura e a arquitetura do software,

03:51

porque a arquitetura de solução não está preocupada apenas com o software em si,

03:56

com o código em si.

03:58

Ela está se preocupando com tudo que está em volta da solução,

04:01

principalmente as integrações que esse software vai tendo

04:06

ao longo do tempo para a gente

04:08

ter um input de um lado e um output que o cliente está precisando do outro.

04:12

No meio de toda essa história, a gente entra com...

04:17

Daí a gente tem muito na parte de system design. Então,

04:21

todas essas contas e esses níveis de complexidade entram

04:25

no meio da parte de arquitetura de solução.

04:28

E é por isso que é importante entender que quando a gente ouve

04:31

alguém falar de arquitetura de solução ou a pessoa é um arquiteto de solução...

04:37

quer dizer que ele consegue ter uma visão geral de como que as coisas se integram,

04:41

como as coisas se falam,

04:42

quanto que essas coisas vão custar ali para a empresa.

04:45

E cada vez mais a gente vê arquitetos de solução focados,

04:49

por exemplo, em cloud providers. Então eu sou um arquiteto de solução para AWS,

04:54

um arquiteto de solução para Google. Por quê?

04:57

Porque eu entendo muito bem quais são as ferramentas,

04:59

quais são as tecnologias daquele cloud

05:03

provider que podem me ajudar a montar,

05:07

e a integrar o problema que eu tenho para eu resolver o meu...

05:11

para eu trazer a solução para aquilo que o meu cliente ali precisa. Então,

05:16

a arquitetura de solução tem uma visão mais de alto nível

05:20

em relação a um problema que a gente vai resolver,

05:23

que é um pouco diferente da parte de arquitetura de

05:26

software que a gente vai falar em seguida. Então, vamos nessa.

## Resumo IA

[RESUMO_IA]