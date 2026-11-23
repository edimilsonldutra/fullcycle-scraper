Módulo: Arquitetura na Era da IA\
Aula: [Governança mínima - acesso, custo e limites](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18296)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? No vídeo anterior a gente falou sobre uma mudança importante.

00:05

Quando existe uma gateway técnica,

00:07

a aplicação pode começar a pedir capacidades internas e

00:11

não necessariamente os modelos físicos dos providers.

00:14

Agora vem a próxima pergunta. Quem pode usar...

00:17

cada uma dessas capacidades. Porque quando tudo está espalhado,

00:20

normalmente cada aplicação resolve isso do seu jeito.

00:23

Mas quando você começa a criar uma camada de acesso à IA,

00:26

naturalmente aparece a necessidade de governança.

00:29

E aqui eu não estou falando de governança no sentido burocrático,

00:33

eu estou falando de controle básico para o sistema

00:36

não virar uma bagunça ali em produção.

00:39

Por exemplo, será que qualquer aplicação pode usar um modelo mais caro?

00:42

Será que um processo em lote, um batch process,

00:45

ele pode disparar milhares de chamadas sem limite?

00:48

Será que uma feature experimental pode consumir o

00:51

mesmo orçamento que uma feature crítica?

00:53

Será que um usuário pode executar a mesma operação pesada que um usuário interno?

00:59

e esse tipo de pergunta no final das contas começa a aparecer rápido quando a IA

01:04

ela deixa de ser um teste e vai virar produto e ela vai para a produção

01:09

Uma gateway, no final das contas,

01:11

ajuda porque ela pode criar um ponto onde essas regras começam a ser aplicadas.

01:16

Você pode ter chaves diferentes para aplicações diferentes,

01:19

pode ter limites diferentes por ambiente,

01:22

pode permitir que um serviço acesse apenas um modelo mais barato,

01:26

você pode separar uma capacidade para um uso interno do que para o uso público,

01:31

você pode limitar requests, tokens, custo e tudo mais.

01:35

O importante é entender que o custo em IA...

01:38

Ele é muito diferente de custo em uma API tradicional.

01:42

Quando a gente chama um modelo, o custo pode variar conforme o modelo escolhido,

01:46

o tamanho do prompt, o tamanho da resposta,

01:48

a quantidade de tokens e o volume de chamadas.

01:50

Então, não basta saber que uma chamada aconteceu. Você precisa saber quem chamou,

01:56

qual capacidade usou, qual modelo foi usado por trás,

01:59

quanto que consumiu, qual foi a frequência de uso. Então,

02:03

isso não é apenas uma preocupação, inclusive, financeira.

02:07

é também uma questão que afeta diretamente a arquitetura.

02:12

Porque uma feature sem limite pode consumir cota do

02:15

provider e afetar outras partes do sistema.

02:18

Um fluxo mal desenhado pode gerar um custo alto sem agregar valor proporcional.

02:23

Um agente mal controlado pode fazer chamadas demais,

02:26

uma operação síncrona pode ficar lenta porque ela está

02:30

usando um modelo muito pesado sem necessidade.

02:33

Então... Acesso, custo e limite precisam entrar no desenho.

02:38

Mas aqui tem uma separação importante.

02:40

Uma gateway pode aplicar limites. Ela pode registrar o uso, pode bloquear chamadas,

02:45

pode controlar a capacidade. Mas ela não decide sozinha qual limite faz sentido.

02:50

Essa decisão depende da aplicação,

02:52

do produto e do risco de cada fluxo. Uma classificação simples,

02:57

talvez possa usar um modelo barato e ter um limite alto.

02:59

Uma análise crítica pode ser algo muito mais caro.

03:03

Então, o grande ponto aqui é,

03:05

quando você começa a tratar IA como capacidade compartilhada,

03:09

você precisa controlar acesso, custo, desde o início.

03:13

Então, você não pode travar a evolução,

03:16

mas também para evitar... que cada aplicação use de um jeito,

03:20

vamos dizer assim, invisível,

03:21

e que acabe ficando ali muito difícil de governar. Então, no próximo vídeo,

03:27

a gente também vai olhar para um outro grupo

03:29

de mecanismos que normalmente entram nessa camada,

03:32

que é quando a gente fala de timeout,

03:35

retry e fallback técnico. Beleza? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]