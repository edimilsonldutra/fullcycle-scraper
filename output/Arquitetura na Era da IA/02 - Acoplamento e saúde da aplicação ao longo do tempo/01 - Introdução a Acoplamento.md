Módulo: Arquitetura na Era da IA\
Aula: [Introdução a Acoplamento](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18111)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

Hoje a gente vai falar sobre acoplamento na arquitetura de software.

00:07

E esse aí é um tema extremamente importante,

00:10

mas que muitas vezes acaba ficando ali mais na teoria do que na prática.

00:15

Não porque que ele seja simples ou até mesmo um pouco relevante. Na verdade,

00:21

é justamente o contrário. Quando a gente começa a analisar acoplamento de verdade,

00:25

aparecem aí vários conceitos, cálculos,

00:28

métricas e formas diferentes de interpretar a arquitetura de um sistema.

00:33

A gente pode olhar... para quem depende de quem,

00:36

pode calcular o acoplamento aferente,

00:39

acoplamento eferente, instabilidade, nível de abstração, distância na linha real,

00:45

ciclo de dependências e outras informações que vão ajudar a

00:49

gente pra caramba a entender a saúde arquitetural de uma aplicação.

00:53

Só que aí que entra o grande problema. No dia a dia,

00:57

pouca gente faz isso de forma contínua. E não é porque isso não tem valor.

01:02

O ponto é que esses conceitos são muito úteis,

01:05

o problema é que aplicar tudo isso manualmente dá trabalho.

01:10

Você precisa analisar o código, extrair as dependências,

01:13

montar um grafo, calcular os números, interpretar o que eles significam,

01:18

gerar um tipo de visualização e depois ainda manter

01:22

isso atualizado conforme o software vai evoluindo.

01:25

Então, se você perceber... Na realidade, o software, ele muda o tempo todo. Então,

01:31

hoje, você mede o acoplamento de uma aplicação. Amanhã, entra uma nova feature,

01:36

depois alguém cria uma dependência nova,

01:39

depois o outro time altera um módulo compartilhado,

01:42

depois uma refatoração muda completamente a direção de algumas chamadas.

01:47

E, na real, em pouco tempo, aquela análise que fazia mega sentido...

01:53

começa a ficar super desatualizada. Então, por muito tempo,

01:57

esse tipo de análise acabou ficando preso em um lugar meio que estranho. Na teoria,

02:02

ele era extremamente útil, mas na prática era difícil de manter esse negócio, vamos dizer,

02:08

todas essas informações vivas dentro de um fluxo real de desenvolvimento.

02:13

Agora, com a IA, esse cenário começa a mudar.

02:17

Agora fica muito mais viável transformar esse tipo de análise em algo recorrente.

02:22

A IA pode ajudar a ler o código,

02:25

identificar as dependências, gerar cálculos, montar gráficos,

02:28

detectar ciclos,

02:30

apontar os módulos críticos e até

02:32

explicar o porquê determinado componente merece atenção.

02:37

Isso muda bastante a forma como a gente olha para a arquitetura.

02:42

Antes, muitas decisões de refatoração eram guiadas, por exemplo, por experiência,

02:47

percepção de dor acumulada no dia a dia. E isso continua importante.

02:53

O olhar do time, no final das contas, continua sendo totalmente essencial.

02:58

Só que agora a gente consegue complementar esse olhar.

03:03

Com dados. A gente consegue enxergar melhor onde o sistema está ficando frágil,

03:08

onde ele está ficando mais rígido e onde o

03:12

custo de mudança está começando a crescer. Então,

03:16

é como se a gente passasse a ter uma espécie de mapa da aplicação.

03:22

Um mapa que mostra os pontos mais críticos,

03:25

os componentes que a gente mais depende,

03:28

os módulos que dependem de coisas demais e os

03:31

Lugares onde talvez exista um risco maior para futuras mudanças.

03:36

Então, pensa num sistema de pedidos. No começo,

03:38

um Order Service pode parecer apenas um serviço responsável

03:42

para coordenar a criação de um pedido.

03:44

Só que, com o tempo,

03:46

ele começa a conhecer um catálogo, o estoque, pagamento,

03:51

notificações, cliente, promoções, fretes, auditoria, banco de dados.

03:56

E quando isso acontece, ele não é mais apenas um serviço de pedido.

04:00

Ele começa a virar um ponto que puxa boa parte do sistema. E aí,

04:04

qualquer mudança que essas dependências podem afetar esse serviço,

04:11

acaba gerando um nível de fragilidade muito grande.

04:13

Ou seja, porque ele conhece coisa demais. Ou seja,

04:17

se ele depende de 15 caras, se um desses caras,

04:21

mesmo pequenos que eles sejam, quebrar esse seu módulo,

04:27

esse seu componente mais rígido, o seu Order Service,

04:30

ele pode quebrar. Então, isso aí realmente é complexo. Agora,

04:35

olha o outro lado. Existem componentes que quase não dependem de ninguém,

04:39

mas muita gente depende dele.

04:41

Pode ser que, se um arquivo... de tipos compartilhados,

04:44

um banco de dados global, um logger, qualquer coisa misturada,

04:48

esses pontos podem parecer pequenos,

04:51

mas podem virar ali regiões extremamente sensíveis na nossa arquitetura.

04:56

E é exatamente esse tipo de análise,

04:59

de acoplamento, que a gente vai conseguir revelar.

05:02

No final das contas, a IA entra com uma grande facilitadora.

05:06

Ela não substituiu o julgamento arquitetural,

05:09

mas ajuda a gente a tornar a arquitetura muito mais, vamos dizer, observável.

05:14

Em vez de a gente depender apenas de sensação de que algo ali está acoplado demais,

05:19

a gente consegue ver números.

05:21

Então, ao longo desse módulo, a gente vai sair...

05:25

da explicação abstrata e ir para a prática.

05:28

A ideia é olhar para um projeto realista, extrair os dados,

05:32

calcular métricas e entender como esses números

05:34

dizem sobre a evolução do software.

05:37

Então, a gente vai falar sobre acoplamento aferente,

05:39

eferente, mostrar quando os módulos dependem um do outro.

05:43

A gente vai falar também sobre...

05:46

instabilidade, que ajuda a entender se um módulo está mais

05:49

no papel de depender dos outros do que dependidos.

05:52

E também a gente vai falar sobre abstrações. Então,

05:56

esse ponto é muito importante porque não basta sair criando interfaces para tudo.

06:00

O que importa é entender se aquela abstração... está realmente protegendo o sistema,

06:05

se a dependência ali realmente foi invertida e se

06:08

o código ali ficou mais fácil de evoluir.

06:10

Então, o objetivo não é decorar a fórmula,

06:12

o objetivo é a gente conseguir usar essas informações para tomar a decisão. Então,

06:17

onde vale a pena, por exemplo, refatorar primeiro?

06:19

Qual componente merece um alerta? Qual módulo que acaba...

06:24

acumulando ali mais dependência.

06:26

Qual parte do sistema está virando um ponto crítico?

06:28

Então esse aí é o ganho principal.

06:30

Com a IA a gente consegue trazer isso para o dia a dia e usando

06:33

esses conceitos que antes eram muito difíceis de a gente colocar na prática.

06:37

Beleza? Então,

06:38

o que a gente tem que entender é que

06:40

arquitetura de software não é só organizar pasta,

06:42

desenhar caixinha ou escolher tecnologia.

06:45

A arquitetura é entender o custo da mudança.

06:47

E o acoplamento, inclusive,

06:49

é um dos sinais mais importantes para a gente conseguir, inclusive,

06:53

enxergar esse custo que, no final das contas,

06:56

pode ficar caro demais. Beleza? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]