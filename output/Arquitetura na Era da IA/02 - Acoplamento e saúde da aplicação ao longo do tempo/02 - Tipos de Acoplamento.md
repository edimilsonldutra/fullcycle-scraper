Módulo: Arquitetura na Era da IA\
Aula: [Tipos de Acoplamento](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18112)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior falamos sobre como a análise de

00:06

acoplamento deixou de ser uma ideia bonita na

00:08

teoria e passou a ser algo muito mais viável no dia a dia com o apoio da IA.

00:13

Agora a gente vai entrar nos conceitos em si,

00:16

começando por duas métricas fundamentais,

00:19

que são o acoplamento eferente e acoplamento aferente.

00:24

A primeira coisa que a gente precisa entender é a direção de uma dependência.

00:29

Quando um módulo importa,

00:30

chama, instancia ou precisa conhecer outro para funcionar,

00:34

existe uma dependência saindo dele. Então,

00:37

uma regra mental muito importante e bem

00:39

simples é: setas saindo representam um acoplamento eferente.

00:44

Setas entrando representam um acoplamento aferente.

00:48

Vamos começar pelo acoplamento eferente, que normalmente aparece como CE.

00:55

Ele começa quando...

00:58

Os módulos de um determinado módulo dependem dele.

01:02

Em outras palavras, ele mede quantas dependências saem daquele ponto.

01:08

Pense em um Order Service dentro de um sistema de pedidos. No começo,

01:13

ele deveria coordenar o fluxo principal da criação de um pedido.

01:17

Só que com o tempo, esse service começa a importar catálogo,

01:21

estoque, pagamento, notificação, clientes, histórico, auditoria, banco de dados.

01:29

Quando você olha para um grafo de dependências,

01:32

percebe que ele tem setas saindo para vários lugares.

01:37

Então, esse é um sinal muito forte.

01:39

Não necessariamente porque o Order Service tem muitas linhas de código,

01:43

mas porque ele conhece coisa demais.

01:45

E quando uma classe conhece coisa demais, ela começa a ficar frágil.

01:50

Se o módulo de pagamento muda,

01:52

pode quebrar o pedido. Se o estoque muda,

01:55

pode quebrar o pedido. Se a regra de promoção vai mudar,

01:58

pode quebrar o bendito do pedido. Então, na realidade,

02:03

qualquer função compartilhada pode quebrar o nosso Order Service.

02:07

Então, ele passa a depender de muitas peças que acabam sendo,

02:12

vamos dizer assim, móveis dentro do sistema.

02:15

E esse aí é o risco de um CE alto.

02:19

O módulo fica muito sensível ao que acontece ao redor dele.

02:25

E nesse caso, ele acaba se tornando instável,

02:29

porque muitas mudanças externas podem afetar o seu comportamento.

02:35

Agora vamos olhar para o outro lado, que é o acoplamento aferente, ou o CA.

02:41

Aqui a pergunta muda completamente.

02:44

A gente não está mais perguntando quantos módulos eu dependo.

02:48

A gente está falando e perguntando quantos módulos dependem de mim. Nesse caso,

02:55

olhamos para as setas entrando. Ou seja,

02:58

se muitos módulos apontam para o mesmo componente,

03:02

esse componente tem um CA alto.

03:05

É muito comum isso acontecer com arquivos compartilhados.

03:08

Por exemplo, um shared, um types. Ele pode ser usado por quase todo o sistema.

03:15

Então, um shared, um database, pode concentrar o acesso a um banco de dados.

03:19

Um sistema de logger pode ser usado em vários services.

03:24

Um sistema de utils ali pode ter funções usadas em módulos completamente diferentes.

03:29

O impacto aqui é outro.

03:31

Um módulo com CE alto é frágil porque depende de muita coisa.

03:36

Já um módulo com CA alto é crítico porque muita coisa depende dele.

03:42

Então, se você... Se você muda um módulo com CA alto,

03:46

a chance de gerar impacto em várias partes da aplicação aumenta bastante.

03:51

É aquele cenário em que você altera uma função,

03:54

aparentemente simples, em utils, por exemplo, e, de repente,

03:58

vários testes começam a quebrar em áreas que pareciam

04:02

que não tinham relação nenhuma com aquela mudança.

04:05

Só que aqui que existe um detalhe importante.

04:08

O CA alto não é automaticamente um problema.

04:12

Se muitos módulos dependem de um conjunto de tipos bem definidos,

04:17

contratos estáveis ou abstrações de domínio,

04:20

isso pode ser saudável. Afinal, em muitos sistemas,

04:24

a gente tem elementos centrais que precisam ser compartilhados.

04:27

O problema não é muita coisa depender de algo.

04:30

O problema é muita gente depender de algo concreto,

04:34

instável conceitualmente ou mal organizado. Por exemplo...

04:39

Types pode ter um CA alto e ainda assim pode

04:42

ser um ponto saudável porque ele representa um contrato estável,

04:46

ele é uma interface. Agora, se Logger tem um CA alto,

04:49

porque vários módulos fazem um new Logger...

04:52

ou seja, um new Logger diretamente, aí temos uma nova situação.

04:57

Nesse caso, o sistema não depende de uma abstração,

05:00

ele depende de uma implementação concreta que está espalhada ali pelo código. Então,

05:05

isso acaba tornando o sistema ali muito, muito mais rígido.

05:09

Então, quando a gente olha para...

05:11

O CA e o CE, a gente não quer apenas decorar números,

05:14

a gente está querendo entender o que eles estão

05:17

dizendo sobre o comportamento arquitetural da aplicação.

05:20

Se o módulo tem CE alto, ele provavelmente conhece coisa demais.

05:24

Talvez ele esteja acumulando responsabilidades demais,

05:27

talvez ele esteja ali coordenando fluxos que

05:30

deveriam estar ali melhor distribuídos.

05:34

Ou seja, no final das contas, ele acaba ali virando uma classe Deus.

05:38

Vamos dizer assim, tá? Agora, se um módulo tem CA alto,

05:41

ele virou um ponto de sustentação do sistema. Isso pode ser bom ou ruim,

05:45

vai depender se ele é uma abstração ou se no

05:48

final das contas ele é uma implementação concreta.

05:51

E por isso que a direção dessas setas é tão importante.

05:55

Quando a seta muda de um módulo, ele depende demais do mundo,

05:59

tá? Então isso aí é um ponto importante.

06:03

Agora, quando muita seta sai de um módulo, né?,

06:08

a gente acaba pensando demais ali no mundo externo e tudo mais,

06:13

tá? Agora, vamos nessa.

06:16

Entendendo isso de acoplamento aferente e eferente, tendo essa ideia geral, tá?

06:23

A gente tem um ponto que acaba sendo mais importante,

06:26

que é a instabilidade, tá? E instabilidade não é um xingamento, não é algo ali que,

06:32

olha, vou ser instável, né? Não. Um módulo instável não é necessariamente ruim.

06:37

Às vezes ele está em uma camada mais externa,

06:40

coordenando detalhes de infraestrutura, integrando serviço, e isso pode fazer sentido.

06:45

O problema é que quando essa instabilidade aparece junto com baixa coesão,

06:51

responsabilidade demais e dependências de controle.

06:54

Da mesma forma, estabilidade não é sempre uma, vamos dizer, uma virtude.

06:59

Um módulo estável que está sendo usado por todo mundo

07:03

pode ser ótimo se ele for uma abstração bem desenhada.

07:07

Mas pode ser muito perigoso se for uma dependência concreta e

07:10

global que ninguém consegue trocar no final das contas.

07:13

Então o CA e CE...

07:15

E a instabilidade são ferramentas para a gente enxergar melhor.

07:18

Elas ajudam a gente a transformar a sensação em dados.

07:21

Em vez de a gente apenas falar, eu acho que esse service está acoplado demais,

07:25

a gente consegue olhar para um grafo, por exemplo,

07:28

e ver quantas dependências saem dele e discutir ali com mais clareza. Então,

07:32

esse é o tipo de análise que ajuda muito na priorização de refatorações.

07:36

Então, antes da gente sair mexendo no sistema inteiro,

07:39

a gente consegue identificar quais os componentes estão puxando dependências demais,

07:43

quais componentes... eles se concentram, vamos dizer, dependências demais.

07:48

Então, no próximo vídeo,

07:50

a gente vai avançar em cima disso e a gente vai falar sobre abstração,

07:53

zona de dor, interfaces que existem que não estão protegendo o sistema,

07:58

duplicação de regras, ciclo de dependências,

08:01

e aí que a gente começa a ligar os

08:03

números com as decisões arquiteturais mais profundas. Então, vamos nessa.

## Resumo IA

[RESUMO_IA]