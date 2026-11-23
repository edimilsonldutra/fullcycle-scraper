Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17794)

## Resumo da aula

Desenvolver várias features ao mesmo tempo muda o problema de engenharia. A dificuldade deixa de ser apenas derivar features do PRD e passa a incluir coordenação operacional entre execuções concorrentes. A analogia com uma orquestra é precisa: tocar sozinho exige menos estrutura; tocar em conjunto exige regras de convivência, sincronização e isolamento. Em SDD, isso significa que a qualidade da especificação continua importante, mas já não basta sem uma infraestrutura mínima de execução.

Agentes trabalhando em paralelo precisam receber contexto operacional explícito, não apenas instruções funcionais. Isso inclui onde executar, quais recursos usar e como evitar interferência entre execuções simultâneas. Sem esse mínimo, o agente não falha por incapacidade de programar, mas por estar perdido no ambiente em que precisa operar. O problema central deixa de ser “o que implementar” e passa a incluir “em que condições essa implementação consegue rodar e ser validada”.

Em localhost, múltiplas features concorrentes disputam os mesmos recursos da máquina, especialmente portas de serviços como 5432 para Postgres e 3000 para aplicações web. Esse conflito aparece quando cada feature precisa subir a aplicação, executar testes ou rodar fluxos end-to-end de forma independente. Se duas execuções assumem a mesma porta, uma delas falha ou bloqueia a outra. O desenvolvimento paralelo, portanto, exige alguma estratégia de alocação ou isolamento de portas desde o início.

Algumas features dependem de credenciais e configurações específicas, como uma chave da OpenAI para transcrição de vídeos. O problema não é apenas armazenar a variável de ambiente, mas decidir como esse valor chega ao agente sem comprometer segurança nem autonomia operacional. Esse handoff precisa ser previsível: o agente deve saber se consome variáveis do host, de arquivos ou de um ambiente isolado. Quando isso não está definido, a implementação pode até estar correta, mas a execução falha por configuração ausente.

Retomando o cenário de múltiplas features em paralelo, cada execução precisa saber quais portas usar, qual banco instanciar e quais nomes de recursos reservar. Essa parametrização não pode ficar implícita, porque agentes concorrentes tendem a colidir quando assumem defaults idênticos. Ensinar esse comportamento ao agente faz parte do trabalho de orquestração, mesmo quando o harness é built-in. O agente precisa receber não só a tarefa, mas também as regras de ocupação do ambiente.

Conflitos de código são inevitáveis quando várias features alteram arquivos relacionados e convergem para o mesmo branch ou linha de integração. A primeira feature integrada costuma sofrer menos, mas as seguintes acumulam risco de merge conflict e revisão mais cara. Isso afeta não só Git, mas também a cadência de pull requests, porque mudanças paralelas aumentam a chance de retrabalho. Em desenvolvimento paralelo, conflito não é exceção operacional; é uma condição normal que precisa ser prevista.

SDD não elimina revisão humana nem transforma integração de software em processo totalmente automático. Durante a implementação, decisões técnicas e até decisões de negócio podem mudar, mesmo quando o PRD já parecia fechado. Por isso, o fluxo real não é “disparar e esquecer”, mas acompanhar, revisar e corrigir desvios ao longo do tempo. A autonomia útil é parcial e supervisionada, não mágica.

Cada projeto impõe um flow diferente: monorepo, múltiplos repositórios, front-end separado de back-end, ou dezenas de microserviços necessários para um teste end-to-end. Não existe uma fórmula universal que resolva o desenvolvimento paralelo em todos esses cenários. O ponto decisivo é adaptar o comportamento do agente ao ecossistema real em que ele opera. Quem fica preso apenas ao framework perde a capacidade de fazer o agente sobreviver fora do cenário idealizado.

Retomando a ideia de dar o mínimo de guidance ao agente, o ajuste não precisa virar um harness customizado completo. Um caminho intermediário é registrar regras operacionais em cloud.md e complementar isso com uma skill que oriente a implementação e peça um relatório do que funcionou ou falhou. Esse arranjo reduz ambiguidade sem transformar o processo em controle excessivo. O objetivo é aumentar a previsibilidade da execução, não remover toda a autonomia.

Docker reduz boa parte dos problemas de convivência entre execuções paralelas porque isola processos, dependências e serviços como banco de dados. Com containers, cada feature pode subir seu próprio Postgres e sua própria stack sem interferir diretamente nas demais. Isso também ajuda quando diferentes execuções exigem versões distintas de Node, Python ou Go. O isolamento não elimina toda a complexidade, mas troca conflitos difusos de máquina local por fronteiras operacionais mais controláveis.

Mesmo com containers, a navegação visual e alguns testes ainda dependem das portas expostas no host. Se vários ambientes internos usam a porta 3000, alguém precisa mapear corretamente essas execuções para portas distintas ou para algum mecanismo de roteamento. O container resolve o isolamento interno, mas não apaga a limitação física da máquina do desenvolvedor ao acessar serviços simultâneos. Por isso, Docker melhora muito o cenário, mas não substitui a necessidade de estratégia operacional.

## Transcrição

00:01

Bom, pessoal, e agora a gente chegou num momento importante.

00:06

Somente para você saber o que está acontecendo agora,

00:08

o nosso gerador aqui das nossas funcionalidades,

00:13

ele acabou rodando e ele gerou aqui a feature 04,

00:18

07 e 12. Ou seja, a gente está nessa wave 3.

00:22

E agora é um momento que acaba começando a ser crítico. Por que eu digo isso?

00:30

principalmente pelo fato de que quando você tem

00:33

que fazer várias coisas ao mesmo tempo,

00:35

o seu workflow muda. Eu vou dar um exemplo muito simples.

00:41

Eu sou músico e eu toco saxofone. E o que acontece?

00:47

Quando eu pego o sax para tocar,

00:49

eu vou lá e estou tocando sozinho e não tem problema nenhum.

00:53

Mas quando eu vou tocar com uma orquestra,

00:55

com uma banda, existe uma fundação muito clara.

00:59

Para que todas as pessoas consigam tocar ao mesmo tempo,

01:02

de forma coordenada, e que não exista, vamos dizer assim,

01:07

um conflito que um consiga atrapalhar o outro.

01:11

E a mesma coisa começa a acontecer aqui nesse momento,

01:16

quando a gente vai trabalhar em paralelo.

01:18

Quando a gente for falar em Harness Engineering,

01:21

a gente vai ver isso muito mais a fundo.

01:24

Como o nosso foco aqui é principalmente a parte de especificação,

01:29

eu vou trazer essas informações, eu vou trazer a base simples sobre isso,

01:35

mas a gente não vai se aprofundar tanto. Então, o que acontece?

01:40

Toda vez que você vai fazer um trabalho paralelo,

01:43

você tem que ter uma infraestrutura mínima para trabalho,

01:47

para você não ter tantos conflitos entre os agentes que estão trabalhando.

01:52

Então, deixa eu vir aqui no meu Scaledraw,

01:56

para ficar um pouco mais fácil para que vocês consigam entender.

02:00

Quando eu tenho determinadas tarefas para fazer junto,

02:04

eu começo a esbarrar em alguns detalhes.

02:07

Então, eu vou colocar aqui, por exemplo, Feature 01,

02:11

Feature 02 e

02:16

Feature 03 aqui para mim.

02:20

Imagina que eu quero fazer essas três Features ao mesmo tempo e vai dar tudo certo.

02:25

A gente organizou os pré-requisitos, a gente fez um monte de coisa,

02:29

mas em relação à estrutura, algumas coisas podem acontecer.

02:36

Primeira coisa que vai acontecer é o fato de ambiente.

02:40

Lembra que eu falei para você?

02:41

O ambiente em que a gente vai rodar o nosso sistema. O que acontece é o seguinte,

02:48

hoje a gente está rodando aqui na minha máquina localmente.

02:52

Então aqui está o computador do Wesley.

02:55

Então, estou aqui com o meu computador.

02:57

E esse meu computador tem algumas coisas aqui que são

03:01

importantes na hora que eu vou fazer o desenvolvimento.

03:04

Que coisas são essas? Eu tenho as minhas portas que eu vou trabalhar.

03:11

Ou seja, deixa eu colocar aqui as portas.

03:16

Ou seja, eu tenho a minha porta 5432 do meu Postgres,

03:21

eu tenho a 3000 que vai rodar o Next.js,

03:24

eu tenho diversas portas que eu vou trabalhar. Então, o que acontece?

03:28

Quando eu estou trabalhando aqui na minha máquina,

03:31

e eu vou trabalhar com três features, essas features, eventualmente,

03:35

elas vão ter que ser testadas. Essas features, elas vão ter que subir,

03:38

eventualmente fazer teste end-to-end,

03:41

e aí a gente começa a ter alguns problemas. Quais são esses problemas?

03:45

Nenhuma dessas funcionalidades consegue rodar exatamente nas mesmas portas. Então,

03:51

isso acaba sendo algo que vai dar problema na hora de você rodar.

03:56

Principalmente se você está trabalhando, por exemplo,

04:00

em um ambiente que não é isolado,

04:01

utilizando o Docker, por exemplo. Então, esse aí é um ponto importante.

04:07

Outro ponto importante aqui são variáveis de ambiente. O que acontece?

04:15

Dependendo da feature, por exemplo, a gente vai passar por essa situação,

04:18

para fazer as transcrições dos nossos vídeos, nós vamos precisar,

04:21

por exemplo, da chave da OpenAI.

04:25

Então, o que vai acontecer? Na hora de eu fazer o desenvolvimento dessa feature,

04:30

o que eu vou precisar fornecer essa chave?

04:34

Então, como que eu vou fazer o handoff dessa chave para o meu agente?

04:37

Eu posso deixar essa chave nas minhas variáveis de ambiente do meu computador,

04:44

para o agente não precisar acessar o arquivo ou

04:49

até mesmo para eu trabalhar de forma autônoma e etc.

04:54

Esse aí é um outro ponto que eu preciso pensar.

04:57

A outra forma,

04:59

o outro ponto aqui é que como que eu faço para

05:02

que na hora que eu for iniciar o trabalho,

05:05

ou seja, iniciar o processo de desenvolvimento com o agente,

05:09

ele consiga, por exemplo, atribuir.

05:13

Quais portas que ele vai usar?

05:16

Qual é o nome do banco que ele vai usar?

05:20

Nome do banco de dados.

05:22

Como é que ele vai trabalhar com as variáveis de ambiente?

05:27

Aí, nesse outro caso aqui também é,

05:30

como que ele vai trabalhar com conflitos?

05:35

Porque o que vai acontecer? É inevitável.

05:37

Quando eu trabalho com três coisas ao mesmo tempo,

05:40

arquivos vão ser mexidos. E nesse caso,

05:45

nós vamos ter conflitos. Os conflitos, na realidade,

05:47

hoje em dia são um dos maiores dilemas na hora que a gente vai trabalhar,

05:52

inclusive para fazer revisões de pull requests e etc.

05:57

Por quê? Porque você vai terminar uma feature,

05:59

provavelmente a feature que termina primeiro,

06:01

ela provavelmente não vai ter problema de conflito,

06:04

mas na hora que você vai começar a fazer o merge das outras features,

06:08

você vai começar a ter o problema de conflito.

06:10

E esse tipo de problema é inevitável. Então,

06:14

há uma discussão hoje muito grande em como que

06:17

isso pode ser tratado nos dias de hoje.

06:20

Teve o nosso camarada lá da HashiCorp que ele falou, se eu não me engano,

06:24

cara, talvez o Git tenha que se reinventar de alguma forma. Então,

06:28

assim, existem diversos aspectos que a gente acaba não pensando. Então,

06:34

alguns desses comportamentos do nosso agente,

06:38

Nós vamos ter que ensiná-lo a como trabalhar.

06:43

Então, como isso, e esse nosso capítulo aqui especificamente,

06:48

ele não foca especificamente em harness customizado, ou seja,

06:53

harness do Cloud Code, ou seja,

06:55

é tudo aquilo que está embutido no Cloud Code, que é uma plataforma.

07:00

Então, isso é considerado um harness built-in, vamos dizer.

07:03

Mas a forma de como nós vamos fazer o comportamento do agente é o nosso... Então,

07:10

a gente tem que pensar nesses aspectos aqui.

07:13

Para que a gente consiga fazer isso, a gente tem que dar o mínimo de ambiente,

07:19

o mínimo de informação para o agente, para ele não ficar, na realidade,

07:24

completamente perdido na hora que ele for fazer o processo de desenvolvimento. E, novamente,

07:30

eu não estou aqui nesse momento e, como eu disse para vocês desde o início,

07:34

trabalhar com o SDD não é uma mágica e não

07:37

é algo que a gente está pensando nesse momento,

07:40

que é algo 100% autônomo, que eu vou dar um enter,

07:42

eu vou tomar um café e depois, no dia seguinte,

07:45

eu vou chegar e vai estar todas as features integradas.

07:48

Isso não existe e também, em tese,

07:50

ela não deve existir por um bom tempo,

07:53

pelo fato de que todo software precisa ser revisado.

07:58

Os softwares têm desvios. O software precisa,

08:03

ao longo do tempo, mudar. Às vezes, no meio de uma implementação,

08:07

a gente descobre que aquela decisão,

08:09

inclusive de negócio, apareceu, mas eu já tinha todo o meu PRD definido.

08:15

Como que essas coisas vão se contornar? Então,

08:18

não existe ali uma mágica que você consiga simplesmente...

08:23

fazer tudo acontecer. Você vai ter que manter essas coisas ao longo do tempo.

08:28

É um desafio interessante de trabalhar,

08:33

porque cada projeto tem um flow diferente, vamos dizer assim,

08:38

e por isso que eu insisto tanto em que quando a

08:41

gente está falando em SDD ou qualquer coisa desse tipo,

08:43

você não fique preso necessariamente no framework,

08:46

mas que você tenha intenção, a intencionalidade de entender

08:52

como que você pode fazer com que o seu agente consiga sobreviver no seu ecossistema. Mas, principalmente,

08:59

como que você consegue manter essas coisas funcionando com diversos desvios?

09:06

Mas eu não estou aqui,

09:07

nesse momento, querendo focar no desvio em si.

09:10

Eu estou querendo focar no quê? O que,

09:13

nesse caso, pode gerar impedimentos para que esses meus processos,

09:17

que vão rodar ali em paralelo,

09:22

aconteçam. Então, ó, porta, banco de dados,

09:25

variável de ambiente, conflito, certo?

09:29

Então, todas essas coisas aí vão simplesmente começar a aparecer. Então,

09:36

o que que eu fiz aqui pra adiantar o nosso passo

09:39

e é o que eu vou mostrar no próximo vídeo,

09:42

tá? Eu fiz duas coisas, tá? Uma coisa, né,

09:47

eu falei pra vocês que eu queria trabalhar da forma mais pura possível, porque o nosso

09:52

fator aqui hoje não é necessariamente focar

09:57

em apenas controlar e guiar o agente.

09:59

O nosso maior foco aqui é focar na especificação e

10:03

Pedir para ele desenvolver com o mínimo de guidance, tá?

10:06

Mas o nosso principal ponto aqui é que eu fiz mudanças

10:12

no meu cloud.md e eu vou mostrar para vocês,

10:15

tá? Então,

10:16

tem o meu cloud.md e também...

10:20

Na hora de eu pedir para ele implementar a feature,

10:25

eu criei uma skill que

10:29

dá algumas guidelines para que

10:32

nós possamos implementar e conseguir pedir, vamos dizer assim,

10:37

uma espécie de relatório para a gente conseguir entender o que deu certo e

10:41

o que não deu certo na hora que o agente implementou a determinada feature.

10:46

Mas isso aqui...

10:49

A gente sempre vai precisar fazer,

10:51

a gente sempre vai ter que ter esse cara em volta da gente.

10:59

Isso aqui acontece quando eu estou trabalhando aqui no meu localhost,

11:04

vamos dizer aqui. Aqui é a minha máquina. Então,

11:06

esse aqui é um desafio. Agora,

11:10

existem algumas coisas que vão facilitar e que eu super recomendo que você,

11:16

de fato, utilize.

11:19

Que é o seguinte, eu tenho uma outra coisa aqui chamada Docker.

11:26

E quando eu estou trabalhando com Docker,

11:28

e nesse caso eu vou colocar aqui com containers, a minha vida facilita bastante.

11:34

Por que ela facilita bastante? Como eu estou rodando dentro de um container,

11:38

eu não vou ter problema de conflito de porta.

11:41

Quando eu estou rodando dentro de um container,

11:43

eu ainda vou ter que fornecer uma chave de API.

11:48

Mas... Eu não vou ter problema com banco de dados, porque eu vou subir um Postgres,

11:52

por exemplo, isolado,

11:54

então não tem perigo do meu Postgres mexer com o Postgres do outro camarada.

11:59

Eu consigo necessariamente

12:01

ter maior controle.

12:08

E de isolamento, tá? Porque, eventualmente, eu vou trabalhar em um ambiente onde,

12:14

sei lá, eu estou usando Node numa versão,

12:16

eu estou usando Python na outra, eu estou usando Go na outra.

12:19

Então, quando a gente trabalha com containers,

12:21

a gente consegue normalizar, a gente consegue deixar as coisas mais isoladas.

12:26

Então, eu sempre vou recomendar, de forma geral,

12:29

que você trabalhe com Docker para você evitar, inclusive, esses...

12:34

problemas aqui que acabam acontecendo ali o tempo todo. Mesmo assim,

12:40

na hora que você for fazer os testes

12:45

e navegar sobre os testes visualmente no seu computador,

12:49

ainda assim, portas,

12:52

elas vão ser um calcanhar de Aquiles para a gente. Por quê?

12:57

Porque no meu computador eu só consigo acessar uma porta de cada vez.

13:00

Se ela está utilizada, eu não consigo. Então, como que eu consigo, por exemplo,

13:03

navegar num ambiente onde todos estão rodando dentro do container na porta 3000,

13:09

mas o meu computador só tem uma porta 3000? Então,

13:13

se eu quiser acessar a feature 1, a feature 2, a feature 3,

13:16

isso aí vai ter que estar apontado corretamente pelo container.

13:19

Então, o que eu estou querendo trazer aqui,

13:21

Na realidade, não é uma solução para os nossos problemas no momento.

13:26

O que eu estou querendo trazer aqui para você são pontos

13:28

relevantes que você agora vai ter que começar a prestar mais atenção,

13:33

porque o jogo começa a mudar. Quando você trabalha em paralelo,

13:37

você começa a ter problemas que você não tinha antes,

13:40

parecem problemas elementares, mas esses problemas vão escalando ao longo do tempo,

13:45

fazendo com que você queira voltar ao passado.

13:51

E o passado é fazer uma feature de cada vez.

13:54

E eu vou dizer para vocês, não dá mais para voltar no passado.

13:57

Uma vez que você vê várias coisas sendo construídas,

14:00

várias sessões funcionando ao mesmo tempo,

14:02

você não consegue mais se desver. O ponto aqui é,

14:05

são estratégias que você vai ter que ter para conseguir lidar.

14:09

E o mais interessante é que não existe aí, no caso,

14:12

uma fórmula mágica. O seu ambiente é o seu ambiente.

14:16

Você pode estar rodando no MonoRepo,

14:18

você pode ter diversos repositórios rodando ao mesmo tempo,

14:21

você pode ter um repositório de front-end,

14:23

um de back-end, você pode ter um repositório ali específico,

14:27

você pode estar rodando com diversos microserviços que você tem que fazer um

14:31

end-to-end e subir ali 50 sistemas simultaneamente para as coisas rodarem,

14:35

para você poder testar. Então, isso vai depender muito do seu ambiente.

14:40

O que eu quero trazer aqui, vamos dizer, a parte de awareness,

14:43

vamos dizer, é que você entenda...

14:45

que a partir de agora o jogo é outro e nós precisamos nos adaptar.

14:51

E eu acredito que você vai conseguir se adaptar claramente desde que você soubesse,

14:58

vamos dizer, o mínimo e não ficasse tropeçando nesses pontos.

15:02

Por isso que eu estou querendo adiantar. Então, no próximo vídeo,

15:05

o que eu vou mostrar aqui para vocês?

15:08

Eu vou mostrar algumas alterações,

15:09

algumas coisas que eu coloquei no meu cloud.md para que você...

15:15

minimamente consiga compreender os desafios que a gente está

15:19

agora para trabalhar e o mínimo de guidance.

15:22

Depois também eu vou trazer aqui para você como que nós

15:26

vamos organizar o processo de implementação de uma forma agora mais intencional,

15:31

com uma skill. E novamente, é uma skill que eu criei especificamente nesse caso,

15:37

para esse curso, para que nós possamos desenvolver...

15:43

trazendo algumas informações necessárias,

15:45

mas que a gente não faça simplesmente um prompt.

15:47

Implemente baseado na PRD tal, a feature tal. Ou seja,

15:52

eu vou dar um pouquinho de guidance agora aqui para o meu agente.

15:56

Beleza? Então, no próximo vídeo a gente vai falar sobre isso.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirements Document - Documento que especifica os requisitos de um produto.
*   **SDD**: Software-Driven Development - Desenvolvimento de Software Orientado por Software (ou Impulsionado por Software).
*   **API**: Application Programming Interface - Interface de Programação de Aplicações.

**Resumo**
A aula aborda a transformação do problema de engenharia quando se desenvolvem múltiplas *features* (funcionalidades) de forma concorrente. A principal dificuldade deixa de ser apenas a derivação de *features* de um PRD e passa a incluir a coordenação operacional entre execuções paralelas. Através da analogia com uma orquestra, o instrutor ilustra que, assim como músicos em conjunto precisam de regras de convivência, sincronização e isolamento, o desenvolvimento paralelo em SDD exige uma infraestrutura mínima de execução e contexto operacional explícito.

Agentes trabalhando em paralelo necessitam de instruções funcionais e, mais importante, de contexto operacional explícito, que inclui onde executar, quais recursos usar e como evitar interferências entre execuções simultâneas. O instrutor ressalta que, sem essa orientação, o agente pode falhar por estar desorientado no ambiente. O foco se desloca de "o que implementar" para "em que condições essa implementação consegue rodar e ser validada".

No ambiente de `localhost`, a concorrência de *features* frequentemente leva a disputas por recursos, como portas de serviços (ex: 5432 para Postgres, 3000 para Next.js). Configurações sensíveis, como chaves de API da OpenAI, também exigem um *handoff* previsível e seguro. A parametrização de portas, nomes de bancos e variáveis de ambiente deve ser explícita para evitar colisões entre agentes.

Conflitos de código em sistemas de controle de versão (como Git) são considerados inevitáveis e uma condição normal no desenvolvimento paralelo, aumentando o risco de *merge conflicts* e retrabalho. A aula enfatiza que o SDD não é uma "mágica" nem uma automação total, pois a autonomia dos agentes é parcial e supervisionada, exigindo revisão humana e adaptação a mudanças de requisitos.

Não existe uma fórmula universal para o desenvolvimento paralelo, uma vez que cada projeto possui um *flow* diferente (monorepo, múltiplos repositórios, microserviços). É crucial adaptar o comportamento do agente ao ecossistema real em que ele opera.

O Docker é apresentado como uma ferramenta fundamental que resolve muitos problemas de convivência entre execuções paralelas ao isolar processos, dependências e serviços, permitindo que cada *feature* tenha sua própria *stack* e versões de *runtime* (Node, Python, Go). No entanto, mesmo com containers, o acesso visual e os testes ainda dependem do mapeamento de portas no *host*, exigindo uma estratégia de roteamento.

O instrutor conclui o fluxo explicando que, para dar o mínimo de *guidance* ao agente, foram feitas modificações no arquivo `cloud.md` para registrar regras operacionais e foi criada uma "skill" que orienta a implementação e solicita um relatório sobre o sucesso ou falha da execução. Essa abordagem visa aumentar a previsibilidade sem excesso de controle.

**Pontos de atenção**
*   **Mudança de paradigma**: O desenvolvimento paralelo transforma a engenharia de software de um problema puramente funcional para um problema que exige coordenação operacional e gestão de ambientes concorrentes.
*   **Contexto operacional explícito**: Não basta dar instruções funcionais aos agentes; eles precisam de contexto explícito sobre o ambiente de execução, recursos e como evitar interferências.
*   **Conflitos em `localhost`**: Em ambientes `localhost`, múltiplas execuções concorrentes inevitavelmente disputam recursos como portas de serviço e nomes de bancos de dados, exigindo estratégias de alocação ou isolamento.
*   **Gerenciamento de credenciais**: A passagem de variáveis de ambiente e chaves de API (ex: OpenAI) para os agentes deve ser previsível, segura e autônoma, sem comprometer a segurança.
*   **Parametrização explícita**: Assumir *defaults* implícitos para portas, nomes de bancos ou outros recursos leva a colisões entre agentes; a parametrização deve ser explícita.
*   **Conflitos de código são normais**: Conflitos de *merge* no Git são uma condição esperada no desenvolvimento paralelo e precisam ser previstos e gerenciados, não tratados como exceções.
*   **Autonomia supervisionada**: SDD não significa automação total ou "mágica". A autonomia útil dos agentes é parcial e requer revisão humana, acompanhamento e capacidade de corrigir desvios.
*   **Adaptação ao ecossistema**: Não existe uma "fórmula mágica" universal. É crucial adaptar o comportamento do agente ao *flow* e às características específicas do projeto (monorepo, múltiplos repositórios, microserviços), em vez de se prender a *frameworks* idealizados.
*   **Docker para isolamento**: O uso de Docker e containers é altamente recomendado para isolar processos, dependências e serviços (como bancos de dados e *runtimes* de linguagens), minimizando conflitos de ambiente.
*   **Limitações do Docker no *host***: Mesmo com Docker, a navegação visual e alguns testes ainda podem ser limitados pelas portas expostas no *host*, exigindo uma estratégia de mapeamento ou roteamento de portas.
*   **Aumento da previsibilidade**: Um caminho intermediário para guiar o agente é registrar regras operacionais em arquivos como `cloud.md` e complementar com *skills* que orientem a implementação e solicitem relatórios de execução, aumentando a previsibilidade sem controle excessivo.