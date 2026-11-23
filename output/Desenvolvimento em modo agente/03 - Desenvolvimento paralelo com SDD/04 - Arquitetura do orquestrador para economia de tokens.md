Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17793)

## Resumo da aula

Quando cada subagente repete a mesma exploração inicial do codebase, o sistema consome tokens várias vezes para produzir essencialmente o mesmo resultado. Esse desperdício aparece com frequência em arquiteturas de desenvolvimento paralelo, porque a etapa de entendimento do contexto é cara e tende a ser comum a várias features. Retomando o uso de subagentes por feature, o problema não está no paralelismo em si, mas em repetir trabalho de fundação que poderia ser centralizado.

Uma primeira alternativa é delegar a exploração inicial a um agente orquestrador, ou a um agente especializado em pesquisa, e reutilizar esse resultado nos subagentes seguintes. A vantagem imediata é econômica: a exploração acontece uma única vez, e os agentes de execução passam a trabalhar sobre uma base já levantada. Esse desenho reduz custo, mas ainda não resolve sozinho a transferência completa do conhecimento obtido.

O conhecimento detalhado produzido por um agente fica contido na janela de contexto dele e não é transferido integralmente para outro agente por padrão. Se o orquestrador apenas “repassa” o que descobriu no prompt dos subagentes, esse repasse tende a ser resumido, parcial ou filtrado. O efeito prático é perda de informação fina sobre o codebase, o que compromete a qualidade das decisões locais de cada subagente.

A forma mais robusta de preservar a exploração é materializá-la em um artefato explícito, como um arquivo research.md. Em vez de pedir que cada subagente explore novamente o codebase, a instrução passa a ser ler esse arquivo e trabalhar a partir dele. O arquivo funciona como interface entre agentes: ele externaliza o estado que antes estava preso à janela de contexto de um único agente.

Sistemas multiagente precisam de algum mecanismo de compartilhamento de estado, porque agentes não acessam diretamente 100% do contexto interno uns dos outros. Um arquivo compartilhado é uma solução simples e eficaz para esse problema, especialmente em workflows baseados em geração de especificações e implementação paralela. Frameworks e plataformas de agentes costumam formalizar esse mesmo princípio com objetos de estado, memória compartilhada ou artefatos persistidos.

Centralizar a exploração só vale a pena quando o resultado é preservado de forma completa para consumo posterior. Se a exploração única virar apenas um resumo curto no prompt, o custo cai, mas a qualidade também pode cair. Ao persistir a pesquisa em arquivo, o sistema reduz o número de explorações de três para uma sem sacrificar o acesso ao conteúdo integral descoberto na etapa inicial.

Retomando o desenvolvimento paralelo com features independentes, a velocidade não vem apenas de “rodar comandos em paralelo”, mas de desenhar corretamente o fluxo de informação entre agentes. A arquitetura do orquestrador define onde o contexto nasce, como ele é preservado e de que forma cada subagente o consome. Entender esse mecanismo é o que permite escolher frameworks adequados ou construir workflows próprios com autonomia, em vez de apenas operar ferramentas prontas.

## Transcrição

00:01

Bom pessoal, enquanto os nossos sub-agentes estão rodando aqui,

00:04

eu quero mostrar qual que é uma falha.

00:08

Vamos dizer, se eu fosse trabalhar de forma otimizada,

00:11

eu não faria desse jeito. O que acontece é o seguinte,

00:14

e é importante eu dar ciência para você. O lance é o seguinte,

00:19

no prompt para eu gerar uma feature, o que eu falo para ele fazer?

00:24

Eu não lembro se você lembra,

00:26

mas eu falo para ele fazer uma exploração muito mais de fundação,

00:32

e depois uma exploração mais de alto nível.

00:38

E o que acontece?

00:41

Toda vez que eu lançar um subagente,

00:43

o que vai acontecer? Esse agente vai fazer essa exploração,

00:47

esse agente vai fazer essa exploração, esse agente vai fazer essa exploração.

00:52

E eu tenho um problema grave com isso. Por quê?

00:55

Porque eu estou pedindo para três subagentes fazer a

00:58

mesma exploração que vai ter exatamente o mesmo resultado.

01:02

Ou seja, essa exploração inicial, que inclusive gasta tokens,

01:07

essa exploração inicial que inclusive gasta tokens,

01:12

está sendo feita três vezes,

01:15

onde ela poderia estar sendo feita somente uma vez. Então,

01:19

eu queria trazer aqui para vocês duas soluções

01:22

de como você pode resolver esse problema.

01:25

Isso é um desafio legal para você trabalhar.

01:28

A primeira solução é que você... vai pedir para o agente

01:37

orquestrador explorar, ok?

01:43

E daí, pedir para o agente, ou agente explorador,

01:50

que ele vai fazer essa exploração, essa exploração vai

01:56

ser utilizada pelos subagentes que estão sendo lançados, logo,

02:02

eu tenho apenas uma única exploração, tá?

02:06

E aí eu economizei os meus tokens.

02:10

Porém, o que acontece?

02:13

Na prática, da forma como eu estou falando,

02:16

ela pode ser uma prática muito simplória no aspecto de detalhes.

02:22

Por que eu estou querendo dizer isso aqui para você?

02:25

Se eu chegar e falar, explore o Codebase da mesma forma que eu falei aqui para você,

02:30

e depois, baseado nisso, lance os subagentes para fazer as features,

02:35

a gente tem que entender que...

02:37

O conhecimento fino de tudo que foi explorado está na janela de contexto desse cara.

02:44

Depois que ele explorar e mandar isso para os subagentes,

02:48

não necessariamente ele vai mandar 100% daquilo que ele explorou.

02:53

E aí esses subagentes não vão ter toda a

02:57

informação quanto à exploração real que esse agente fez.

03:02

É como se esse agente aqui...

03:05

essa exploração fosse enviada como prompt para esses

03:08

agentes aqui de uma forma mais resumida.

03:11

E aí a gente perde informação.

03:15

Qual é um cenário mais ideal de você fazer?

03:18

É o seguinte, você pegar um agente orquestrador,

03:22

nesse agente orquestrador você pede para ele explorar,

03:26

mas essa exploração gera

03:31

Um arquivo chamado research.md,

03:35

Por exemplo. Ok?

03:37

E aí, o que eu falo? Eu peço para o meu orquestrador lançar os subagentes,

03:42

mas nessa instrução eu falo para que os subagentes,

03:47

ao invés de explorar o codebase, leiam,

03:51

no final das contas, a exploração que já foi feita.

03:58

Porque essa exploração que já foi feita está num arquivo,

04:02

de forma completa. Então eu não perco os dados que foram explorados.

04:06

Então eu faço com que um agente se

04:09

conecte com o outro através de um arquivo.

04:14

Que é uma das coisas mais comuns que acontecem.

04:17

Que é compartilhamento de estado entre agentes.

04:21

Um agente não consegue ter acesso a 100% da janela de contexto do outro.

04:25

Então nesse caso, eu estou utilizando uma forma de...

04:29

ter uma interface entre um e ele. Nesse caso,

04:32

essa interface é um arquivo. Então, basicamente,

04:35

é isso que acontece. Então, tem inclusive recursos,

04:38

sei lá, do Cloud Code com teammates,

04:40

eles trabalham como se fossem arquivos compartilhados entre os subagentes que eles

04:44

ficam trocando entre os times para que eles consigam mudar de estado.

04:49

Se você pegar um framework como o Google SDK, se você pegar como o Land Graph,

04:53

toda vez que você vai trabalhar com subagentes,

04:56

você tem um estado... e você consegue compartilhar com o outro.

04:59

Então, nesse caso aqui, o meu estado,

05:02

eu estou compartilhando através de um arquivo que pode ser lido,

05:05

e nesse caso, ao invés de eu explorar três vezes,

05:08

eu exploro uma vez só e disparo para os subagentes,

05:11

onde eles não precisam passar por essa etapa.

05:13

Então, esse aí é um ponto importante. Hoje,

05:16

como está acontecendo aqui, os três fizeram a exploração.

05:21

Significa que eu gastei três vezes mais tokens só com exploração. Entendeu?

05:26

Então, esse aí tá, vamos dizer, é uma falha proposital, né,

05:33

de gasto de token, e eu fiz isso para facilitar, inclusive, a explicação,

05:37

mas, obviamente, eu não iria deixar de falar isso para você,

05:41

porque se você pegar isso e sair usando isso para tudo quanto é lugar na sua empresa,

05:46

eu não quero que você gaste tokens à toa

05:48

por uma questão de arquitetura e orquestração dessa skill,

05:54

tá bom? Então,

05:55

essa que era a ideia básica que eu queria passar para você em relação a isso.

05:59

Agora, o que nos basta agora é

06:02

esperar esses três caras gerarem essas especificações,

06:07

tá? E aí a gente vai para a parte do desenvolvimento em paralelo,

06:12

que é uma das partes, eu acredito,

06:14

mais importantes que a gente acaba tendo, porque a gente multiplica... triplica,

06:21

quadruplica a velocidade do nosso trabalho. Mas se você perceber,

06:25

sem a base que foi sendo passada ao longo do tempo,

06:30

fazer essas coisas rodarem em paralelo e etc., para você seria apenas rodar comando.

06:36

E a gente não está criando esse curso,

06:39

essa disciplina, para você virar um operador de skill. Qualquer pessoa roda skill,

06:45

entendeu? Agora, a grande questão é, como você entende como elas funcionam,

06:49

Para que você escolha um framework certo ou para que você crie

06:52

o seu próprio workflow para você trabalhar no dia a dia.

06:54

A coisa mais gostosa do mundo que eu percebo é

06:57

quando eu mesmo estou usando as minhas próprias skills,

07:00

as minhas próprias ferramentas para resolver o problema da forma como eu gosto.

07:03

E eu quero que você tenha autonomia para fazer isso aqui. Beleza? Então,

07:08

duas das features provavelmente aqui, eu acho que elas já foram geradas.

07:13

Então, se eu chegar aqui nos meus docs,

07:17

eu tenho aqui... A feature 4 já está com o plano e especificação.

07:22

A feature 7 está faltando o plano.

07:24

E a feature 12 já está com o plano e a especificação aqui para a gente.

07:29

Então, é esperar esses caras terminarem de rodar. E depois, no próximo vídeo,

07:35

a gente vem e organiza como que a gente vai

07:38

fazer com que essas paradas rodem em paralelo.

07:40

Beleza? Então, é isso aí.

## Resumo IA

**Abreviações**
*   **SDK**: Software Development Kit.

**Resumo**
A aula aborda uma ineficiência comum em sistemas multiagente focados em desenvolvimento de software paralelo: o desperdício de tokens e trabalho repetido quando múltiplos subagentes, ao lidar com features independentes, realizam a mesma exploração inicial do codebase. Essa etapa de entendimento do contexto é cara e frequentemente redundante.

A primeira alternativa para mitigar o problema é delegar a exploração inicial a um agente orquestrador ou especializado em pesquisa, com o objetivo de reutilizar esse resultado. Essa abordagem busca economia, realizando a exploração apenas uma vez. No entanto, ela apresenta uma limitação crucial: o conhecimento detalhado fica contido na janela de contexto do agente explorador e não é transferido integralmente aos subagentes. Um simples "repassem" no prompt dos subagentes tende a ser resumido, parcial ou filtrado, resultando em perda de informação fina e comprometendo a qualidade das decisões locais.

A solução mais robusta proposta é materializar o resultado completo da exploração em um artefato explícito, como um arquivo `research.md`. Dessa forma, em vez de cada subagente explorar o codebase novamente, sua instrução passa a ser ler esse arquivo e trabalhar a partir do conhecimento nele contido. O arquivo atua como uma interface para o compartilhamento de estado entre os agentes, externalizando o conhecimento que antes estaria isolado na janela de contexto de um único agente. Essa abordagem permite que a exploração seja feita uma única vez, garantindo acesso completo ao conteúdo descoberto pelos subagentes, sem perdas de informação. Frameworks e plataformas de agentes geralmente formalizam esse princípio com objetos de estado, memória compartilhada ou artefatos persistidos, como exemplificado por Google SDK e Land Graph. A aula enfatiza que a verdadeira velocidade no desenvolvimento paralelo provém do desenho correto do fluxo de informação e da arquitetura do orquestrador, proporcionando autonomia para construir ou escolher workflows eficientes.

**Pontos de atenção**
*   **Custo da exploração inicial**: A etapa de entendimento do codebase é dispendiosa em termos de tokens e tempo. A repetição dessa exploração por múltiplos subagentes é um desperdício significativo.
*   **Perda de informação fina**: O repasse de conhecimento entre agentes, se não for feito de forma completa e explícita, pode levar à perda de detalhes cruciais contidos na janela de contexto do agente explorador, prejudicando a qualidade das decisões dos subagentes.
*   **Materialização do conhecimento**: Centralizar a exploração só é eficaz se o resultado for preservado de forma *completa* (ex: em um arquivo persistido como `research.md`), e não apenas como um resumo no prompt, para garantir o acesso integral ao conhecimento.
*   **Compartilhamento de estado**: Agentes não possuem acesso direto a 100% do contexto interno uns dos outros. Mecanismos de compartilhamento de estado, como arquivos persistidos, são essenciais para a comunicação e coordenação eficazes em sistemas multiagente.
*   **Equilíbrio entre custo e qualidade**: É fundamental reduzir o gasto de tokens com a exploração, mas sem sacrificar o acesso ao conteúdo integral do conhecimento, o que é crucial para a qualidade das decisões dos subagentes.
*   **Arquitetura do orquestrador**: O design do orquestrador é determinante para como o contexto nasce, é preservado e consumido pelos subagentes, sendo um fator chave para a velocidade e eficiência do desenvolvimento paralelo.
*   **Autonomia e compreensão do fluxo**: O objetivo é ir além da simples execução de comandos (operar uma skill), buscando compreender o funcionamento dos mecanismos para construir ou escolher workflows e frameworks que melhor se adequam às necessidades.