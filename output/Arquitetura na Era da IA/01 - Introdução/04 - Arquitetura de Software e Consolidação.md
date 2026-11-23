Módulo: Arquitetura na Era da IA\
Aula: [Arquitetura de Software e Consolidação](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18109)

## Resumo da aula



## Transcrição

00:03

Bom pessoal, no vídeo anterior a gente falou sobre arquitetura de solução e agora

00:08

eu queria trazer um pouco mais sobre a parte de arquitetura de software.

00:11

Então, a arquitetura de software,

00:13

ela olha para a estrutura fundamental ali do sistema.

00:16

Aqui, a conversa já entra mais na organização do software em si.

00:21

Quais são os componentes principais? Quais são as responsabilidades de cada parte?

00:25

Como que esses componentes se comunicam? Onde devem ficar as regras de negócio?

00:29

Como que os dados ali vão ser armazenados?

00:32

Como é que o sistema se integra com outro sistema?

00:34

Como que ele escala? Como que ele lida com falhas? Como que ele vai ser testado?

00:38

Como que ele evolui sem virar ali uma bola de neve?

00:41

Então, a arquitetura de software também está ligada a atributos de qualidade.

00:46

Então, ele vai sim focar em performance,

00:48

em segurança, em escalabilidade, em resiliência, na parte de manutenção,

00:51

observabilidade e etc. Mas é aqui que tem um ponto importante.

00:56

A arquitetura de software não é só a gente criar,

00:58

por exemplo, um diagrama ou coisas desse tipo, tá?

01:02

Mas a arquitetura ali não é o desenho em si, tá?

01:06

Mas sim a forma de como que a gente comunica essas decisões.

01:11

Para que elas sejam aplicadas no software. Então,

01:13

a arquitetura está nas decisões que estruturam o software para ele conseguir

01:18

atender os objetivos do negócio dentro das restrições que o nosso negócio possui.

01:24

Por exemplo...

01:25

Eu preciso decidir se o sistema vai ser modular

01:28

ou se ele vai ser dividido em serviços,

01:30

se ele vai usar eventos ou se ele vai ter processamento assíncrono,

01:34

se ele vai centralizar ou descentralizar os dados,

01:36

se ele vai isolar uma integração externa ou se ele vai ter uma

01:39

camada anticorrupção ou se ele vai utilizar

01:42

fila para desacoplar algumas partes críticas.

01:46

Então, essas decisões... podem afetar a evolução, o custo, a performance,

01:50

a segurança e a operação da manutenção desse software.

01:54

E algumas dessas decisões acabam entrando, inclusive,

01:56

no mundo da arquitetura de solução. Porém, nesse caso,

02:00

a visão é muito mais focada no software. Ou seja, naquele pedaço de software,

02:06

como que ele vai se comportar dentro de um determinado ecossistema. Então,

02:11

por isso que ele tem um peso ali muito arquitetural.

02:15

Ok? Então, quando a gente está criando um software,

02:18

o peso arquitetural ali é forte porque ele vai

02:22

definir como aquele software vai evoluir ao longo do tempo,

02:27

vai falar com todos os outros sistemas e, eventualmente,

02:29

todo esse ecossistema foi criado ali através, sei lá,

02:33

por um arquiteto de solução ou existe uma arquitetura

02:37

ali de solução em relação a tudo isso,

02:39

tá? Então, agora, para ficar simples, guarda essa divisão.

02:43

A arquitetura tecnológica ajuda a usar bem as tecnologias e as plataformas.

02:48

A arquitetura corporativa olha para a empresa como um todo.

02:51

A arquitetura de solução transforma uma necessidade

02:54

de negócio em uma solução viável,

02:55

encaixando diversas partes para resolver um problema.

02:59

E a arquitetura de software... ela estrutura o sistema para essa solução funcionar,

03:05

evoluir e sustentar. Então, essas arquiteturas não vivem separadas.

03:09

Uma decisão corporativa pode limitar quais tecnologias que a empresa usa.

03:14

Uma decisão de solução pode exigir a integração...

03:17

com o sistema legado.

03:18

Uma decisão tecnológica pode influenciar como o software

03:21

vai ser construído especificamente naquela tecnologia.

03:24

Uma decisão de arquitetura de software pode impactar no custo,

03:28

na operação, na estratégia do negócio,

03:30

porque é a forma de como o software vai evoluir ao longo do tempo.

03:35

Então, isso aí que é um ponto importante.

03:37

Quanto mais micro... você chega nas decisões,

03:41

mas você começa a chegar perto ali da arquitetura de software.

03:44

Então, quando eu estou falando em design patterns,

03:46

quando eu estou falando em SOLID,

03:47

quando eu estou falando em arquitetura hexagonal e coisas desse tipo,

03:51

a gente está muito mais voltado para a arquitetura de software,

03:54

porque ali... que o código está, de forma geral.

03:58

É ali que as decisões vão ser tomadas e que vão começar a afetar, inclusive,

04:03

a construção desse software e também a integração desse software com

04:07

outros softwares que vêm ali no meio de toda essa história.

04:11

Então, e agora começa a entrar um ponto importante para quem está estudando,

04:16

vamos dizer assim, engenharia de software com IA,

04:19

que é muitos projetos com IA vão dar errado

04:22

porque as pessoas tratam tudo como uma decisão.

04:25

Então a pessoa pensa, eu vou escolher um modelo,

04:27

um framework, um banco de dados vetorial,

04:29

e aqui a gente vai tomar a determinada decisão.

04:34

Só que a decisão mais importante talvez ela venha bem antes disso.

04:39

Talvez a empresa nem precise de um agente,

04:42

talvez ela precise apenas de uma automação mais simples,

04:45

às vezes precisa criar um fluxo, uma aprovação humana, não interessa.

04:49

O grande ponto é que quando você tem claro os tipos de arquitetura,

04:53

na nossa mente vai ficando mais fácil a gente

04:56

entender em qual layer da empresa a gente está trabalhando.

05:00

E grande parte, inclusive,

05:02

desse módulo que a gente vai trabalhar em relação à arquitetura,

05:06

a gente vai estar falando mais em arquitetura

05:09

de software e também arquitetura de solução. Beleza? Então,

05:13

isso aqui é mais um alinhamento para ficar um pouco

05:16

mais claro para você esses tipos de arquitetura

05:18

e aonde que a gente vai entrar e vai começar

05:22

a se aprofundar ao longo desse nosso curso.

05:25

Fechou? Um grande abraço e é isso aí.

## Resumo IA

[RESUMO_IA]