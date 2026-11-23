Módulo: Arquitetura na Era da IA\
Aula: [Main Sequence e As Zonas de Acoplamento](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18114)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente falou sobre quando o

00:05

acoplamento começa a virar uma dor arquitetural.

00:08

A gente viu que não basta olhar apenas se um módulo

00:11

depende de muita coisa ou se muita gente depende dele.

00:15

A gente também precisa entender se esse módulo é concreto demais,

00:18

se ele existe uma abstração protegendo aquele ponto,

00:21

se a dependência foi invertida de verdade ou se a

00:24

gente só criou a interface ali que ninguém usa.

00:27

Agora, eu quero dar um passo antes de mostrar isso na prática.

00:32

No próximo vídeo, a gente vai abrir...

00:34

um gráfico e olhar para os módulos de um projeto que eu criei, um projeto real,

00:39

para que a gente tenha isso aí como exemplo. Eu vou mostrar o CA, o CE,

00:44

a instabilidade, a estabilidade, a abstração, a main sequence,

00:50

a zona de dor, a zona de... inutilidade, tá?

00:54

E tudo isso aparecendo de uma forma bem visual, tá?

00:58

Mas pra que esse gráfico ele faça mais sentido,

01:02

vale a pena a gente entender primeiro a ideia por trás dele,

01:06

tá? A main sequence ficou muito conhecida, tá?

01:09

A partir de um dos trabalhos ali do Uncle Bob, né? O Robert C. Martin.

01:13

Um cara absurdamente fantástico, já fiz mentoria, inclusive, com ele.

01:18

E quando ele fala sobre estabilidade e abstração, é bem interessante.

01:23

A ideia principal é tentar enxergar uma proporção saudável entre

01:29

quanto um módulo é estável e quanto ele é abstrato.

01:34

Pensa assim, se um módulo é muito estável,

01:37

no sentido de que muita gente depende dele, ele deveria...

01:42

tender a ser mais abstrato. Porque se muita gente depende daquele ponto,

01:47

ele precisa ser mais fácil de evoluir, estender ou substituir,

01:51

ou substituir sem quebrar o sistema inteiro.

01:54

Agora, se um módulo é mais instável, ou seja,

01:58

depende de muitas coisas, e ele está mais próximo,

02:02

no final das contas, de detalhes de implementação. Então,

02:05

ele pode ser ali mais concreto. Isso não necessariamente é um problema.

02:10

Muitas vezes faz sentido com códigos mais próximos de infraestrutura,

02:14

integração, formatação, ou inclusive orquestrações que sejam mais concretas.

02:19

Então, o main sequence é essa linha que

02:23

tenta representar uma relação saudável entre abstração e instabilidade.

02:30

Só para você saber de onde isso vem, a instabilidade é calculada com uma fórmula,

02:37

que é I é igual a C dividido,

02:41

daí entre parênteses, CE mais CA,

02:45

onde o CE é o acoplamento eferente que

02:48

mostra quantas dependências saem de um módulo.

02:52

O CA é o acoplamento aferente que mostra quantas dependências entram nele.

02:58

Quando o resultado se aproxima de zero, o módulo tende a ser mais estável.

03:04

Quando ele se aproxima de 1, ele tende a ser mais instável.

03:09

Já no caso da abstração, representada ali por A,

03:12

normalmente ela é calculada como a proporção de elementos

03:17

abstratos em relação ao total dos elementos daquele módulo.

03:22

Então, eles entram nessa conta de interfaces,

03:26

classes abstratas e estruturas equivalentes.

03:29

que dependendo da linguagem e da forma como a gente analisa,

03:34

isso aí muda completamente a forma que foi feita.

03:38

Mas o ponto é entender essa abstração. O A representa a abstração.

03:44

E aí existe a ideia dessa linha ideal,

03:48

que é uma forma bem simplificada,

03:50

onde a gente pode ter uma formulinha que basicamente é assim.

03:54

A abstração mais I é igual a 1. Então,

03:59

quanto mais perto dessa relação,

04:02

mais próximo o módulo... está nessa main sequence.

04:08

Quanto mais distante, maior a chance dele cair em uma relação problemática.

04:14

Então, não se preocupe em decorar a fórmula.

04:16

O ponto aqui não é transformar isso em matemática e qualquer coisa desse tipo.

04:21

Eu só estou trazendo essas contas apenas para você

04:24

perceber que esse gráfico não surgiu do nada.

04:27

Ele vem de uma tentativa de medir proporção entre dependência,

04:31

estabilidade e abstração. E essas proporções ajudam muito.

04:36

Quando a gente tem estabilidade alta e abstração alta,

04:40

geralmente a gente está numa região saudável. Por exemplo,

04:44

contratos centrais ou tipos bem definidos podem ser usados

04:48

por muita gente sem necessidade de criador.

04:51

Quando temos instabilidade alta e código concreto, isso também pode ser aceitável.

04:58

Um módulo concreto que depende de muitos detalhes pode fazer sentido.

05:03

dependendo do papel dele.

05:05

O problema aparece nos extremos. A zona de dor aparece quando um módulo é estável,

05:11

porque muita gente depende dele, mas ele é concreto demais.

05:16

Ele é difícil de mudar e difícil de estender.

05:18

Então aí é o caso típico de um banco de dados global

05:24

ou um logger concreto que é utilizado ali por todo mundo.

05:29

A zona de inutilidade... Aparece em outro extremo,

05:33

que é quando a gente tem uma abstração demais,

05:36

tem a necessidade de a gente ter.

05:38

A gente cria interface, contrato e um monte de arquivo,

05:42

mas essas abstrações acabam não protegendo nenhuma dependência.

05:47

A implementação concreta continua sendo usada diretamente

05:50

e isso acaba virando overengineering.

05:53

Então, guarda essa ideia. Concreto demais em ponto estável gera rigidez,

05:57

abstração demais sem uso gera peso.

06:01

No próximo vídeo, quando a gente olhar para o gráfico do projeto,

06:04

essas zonas vão ficar muito mais claras e a gente vai

06:07

conseguir ver quais dos módulos estão próximos de uma

06:10

proporção saudável e quais estão ali numa zona de dor

06:14

e quais podem estar caminhando para uma zona de inutilidade.

06:19

Beleza? Então vamos nessa para entender melhor esse gráfico.

## Resumo IA

[RESUMO_IA]