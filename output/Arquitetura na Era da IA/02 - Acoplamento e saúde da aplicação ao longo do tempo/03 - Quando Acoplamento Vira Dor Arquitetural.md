Módulo: Arquitetura na Era da IA\
Aula: [Quando Acoplamento Vira Dor Arquitetural](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18113)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? No vídeo anterior a gente falou sobre acoplamento aferente,

00:05

acoplamento eferente e instabilidade.

00:07

A gente viu que a direção das dependências muda completamente a leitura do sistema.

00:12

Agora a gente vai avançar para o próximo passo,

00:15

entender... quando esses números começam a mostrar ali a dor arquitetural. Para isso,

00:20

a gente precisa juntar as duas ideias, estabilidade e abstração.

00:24

Quando um módulo é estável pela métrica,

00:26

significa que muita gente depende dele e ele depende de pouca coisa. E isso pode ser bom.

00:31

Um conjunto de tipos bem definidos pode ser muito

00:34

bem usado e ainda assim ser saudável. Agora,

00:39

o problema aparece quando algo muito estável também é muito concreto.

00:43

Pensa num database global.

00:45

uma classe de banco de dados

00:47

global importado diretamente por vários módulos.

00:52

Pensa num sistema de logger instanciado com um new em várias partes do sistema.

00:59

ou numa mistura de dados de moeda,

01:02

geração de ID ou um cálculo de total que é

01:05

concreto e ali está dentro de outras classes.

01:09

Esses componentes podem até parecer pequenos,

01:11

mas eles ficam perigosos porque muita gente depende deles diretamente e

01:16

a arquitetura fica rígida e não porque o código parou de funcionar,

01:19

mas porque para mudar qualquer coisa ali passa a ter um risco bem maior.

01:24

Então essa região é conhecida como zona de dor.

01:28

É quando um componente é difícil de mudar porque muita gente depende dele.

01:35

E difícil de estender porque não existe

01:38

uma abstração clara protegendo o resto do sistema.

01:42

O logger é um bom exemplo. O log é algo normal em qualquer aplicação.

01:46

O problema não é registrar o log.

01:48

O problema é espalhar o new logger pelo sistema inteiro. A partir desse momento,

01:53

vários módulos deixam de depender de uma capacidade e

01:57

passam a depender de uma implementação específica.

02:00

Se amanhã você precisar trocar esse logger ou simular ele nos testes, por exemplo,

02:05

essa troca não é mais simples. Você não troca simplesmente uma peça,

02:10

você precisa alterar vários pontos da aplicação.

02:13

E é por isso que a inversão de dependência é tão importante. Não porque...

02:17

a interface deixa o código ali mais bonito,

02:20

mas porque ela protege o módulo de alto nível dos detalhes concretos.

02:25

O service não deveria depender diretamente do detalhe de infraestrutura.

02:29

Ele não deveria depender de um... Ele deveria depender de um contrato.

02:34

Só que criar interface por criar também não resolve nada.

02:38

Às vezes existe uma interface, sei lá,

02:40

Payment Gateway, mas os services continuam fazendo new...

02:44

no Stripe Gateway, diretamente. Nesse caso, a interface existe,

02:48

mas não inverteu a dependência. Ela não protegeu o código,

02:52

ela virou só mais um arquivo.

02:53

Então, a pergunta certa não é apenas se a interface existe.

02:57

A pergunta certa é quem depende dela?

03:00

O código passou a depender do contrato ou

03:02

ele continua preso numa implementação concreta?

03:05

Então, essa leitura ajuda quando a gente olha para abstrações e instabilidade.

03:10

Os componentes estáveis tendem a precisar mais de abstração.

03:15

Se muita gente depende deles,

03:17

eles precisam ser mais fáceis de estender sem quebrar todo mundo.

03:22

Mas nenhum número sozinho acaba explicando uma arquitetura inteira.

03:27

Um order service pode aparecer como concreto e instável,

03:32

só que se ele depende de 15 módulos,

03:36

o CE dele, o acoplamento aferente bruto, mostra outro problema.

03:41

Ele conhece coisa demais. Ele pode estar virando ali uma classe deus.

03:46

Por outro lado, um logger pode parecer estável, porque quase não depende de nada,

03:52

mas se 14 módulos dependem dele diretamente, ele é concreto, e concreto,

03:58

ele tem ali uma zona de dor muito clara.

04:02

Um outro sintoma aparece na duplicação de regra.

04:06

Imagine que eu tenho uma regra de cupom que deveria estar num serviço de promoção,

04:10

mas ele acaba sendo copiado dentro do order service.

04:14

Depois a regra evolui em um lugar e não evolui no outro.

04:17

Agora mesmo o cenário pode gerar respostas

04:21

diferentes dependendo do caminho executado.

04:23

Então isso não é só um bug, é um sinal de fronteira mal definida.

04:27

Então a responsabilidade não ficou só num lugar claro.

04:30

E o acoplamento começou a espalhar regras de negócio.

04:34

E ainda a gente tem ciclo de dependência.

04:37

Um módulo chama o outro, que chama o outro.

04:39

Em algum momento a cadeia volta para o primeiro e isso cria ali um emaranhado.

04:45

No meio do nosso código e essas nossas camadas, elas perdem ali a direção.

04:49

Cada alteração acaba ficando mais difícil de prever.

04:52

Então, quando a gente analisa acoplamento,

04:55

a ideia é encontrar sinais mais práticos,

04:57

rigidez, fragilidade, abstração desperdiçada,

05:01

regra duplicada e ciclos ali que a gente

05:04

acaba nem pensando que podem acabar existindo.

05:08

Então, arquitetura boa não é aquela arquitetura que ela não muda.

05:11

Arquitetura boa é aquela que permite mudar com menos medo,

05:15

com menos efeito colateral e com mais controle sobre impacto,

05:19

mas ao mesmo tempo a gente não faz aquela overengineering.

05:23

Eu não sei se você é esse tipo de desenvolvedor,

05:25

mas eu conheço muitos desenvolvedores que, para criar uma classe,

05:28

ele cria uma interface antes para tentar manter a abstração.

05:32

Mas aí, dependendo da situação,

05:33

ele tem tantas interfaces que são utilizadas apenas para um arquivo. Então,

05:39

nesse caso, eventualmente, ele vai cair numa zona, vamos dizer, de inutilidade.

05:44

Porque você não precisa também a todo momento sair criando interface.

05:49

Você tem que usar ali o seu bom senso.

05:52

Se você começa a perceber que aquilo vai começar

05:55

a ser utilizado em diversos locais do sistema,

05:58

aí sim você vai criar uma interface ali muito clara.

06:01

Eu não estou dizendo que eu sou contra a interface. Eu sou contra utilizar...

06:05

e criar excessivamente interfaces que acabam sendo, entre aspas, inúteis no sistema.

06:11

Aquelas interfaces que claramente não vão ser utilizadas

06:15

por várias partes ou por várias classes naquele contrato.

06:19

Então a gente tem que ficar ligado nisso também. Fechou?

## Resumo IA

[RESUMO_IA]