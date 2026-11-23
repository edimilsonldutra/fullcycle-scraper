Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17886)

## Resumo da aula

Orquestrar subagentes não significa construir cadeias cada vez mais complexas de chamadas entre agentes, modelos e workflows. Em ambientes modernos, o próprio harness já assume boa parte dessa coordenação, inclusive decidindo quando lançar subagentes e como administrar esse fluxo. O erro comum é tratar orquestração como um exercício de malabarismo técnico para economizar tokens ou extrair desempenho marginal. Antes de otimizar, o objetivo precisa ser entregar software funcional com um processo controlável.

Quando um agente chama outro, que chama outro, surge overhead de contexto, sincronização e transferência de estado. Esse custo pode consumir tempo de execução, aumentar gasto e ainda produzir um resultado que não supera o de um único modelo forte operando com um harness bem configurado. Retomando o princípio já estabelecido de que o harness é o principal determinante do resultado, a consequência prática é simples: forçar uma arquitetura de subagentes sem necessidade frequentemente piora o sistema. Complexidade extra só se justifica quando resolve um gargalo real.

Executar agentes em paralelo depende de decompor o trabalho em partes específicas, verificáveis e suficientemente independentes. Sem uma especificação clara do que cada agente deve fazer, o paralelismo vira concorrência desorganizada, não produtividade. Em engenharia de software, o trabalho passa por etapas que precisam ser avaliadas por critérios objetivos e também pelo usuário final. Por isso, paralelizar só faz sentido quando as fronteiras entre tarefas estão bem definidas.

Criar agentes para tarefas específicas é útil, mas isso não implica manter vários agentes interagindo continuamente dentro do mesmo contexto. Em muitos casos, a melhor organização é dividir responsabilidades e reduzir acoplamento entre execuções, em vez de montar uma rede de agentes trocando contexto o tempo inteiro. Essa separação torna o processo mais previsível e diminui o risco de comportamento emergente difícil de depurar. Orquestração eficaz depende mais de clareza operacional do que de interatividade constante entre agentes.

Quando um subagente é lançado por um harness, ele pode herdar o contexto da sessão pai por meio de um fork. Isso significa que ele não começa do zero: parte de um estado anterior já estabelecido e continua o trabalho a partir dali. Esse mecanismo reduz retrabalho e preserva continuidade sem exigir que toda a coordenação seja implementada manualmente. A implicação prática é que muitos cenários de delegação já estão cobertos pela infraestrutura da ferramenta.

Retomando a ideia de organização do processo, uma estratégia é manter agentes em sessões separadas que se comunicam por artefatos persistidos, como arquivos. Nesse modelo, o estado não depende de uma conversa contínua entre agentes, mas de evidências concretas produzidas por uma execução e consumidas por outra. Isso torna a troca mais auditável e menos frágil do que repassar contexto informalmente entre múltiplos agentes. O uso de recursos como teammate segue essa lógica de isolamento com comunicação explícita.

WorkTrees permitem executar subagentes em ambientes de trabalho isolados, preservando separação entre mudanças concorrentes no mesmo codebase. Esse isolamento é valioso quando diferentes agentes precisam atuar sem interferir diretamente uns nos outros. Em vez de compartilhar o mesmo espaço de edição e gerar conflitos desnecessários, cada execução opera em sua própria árvore de trabalho. A coordenação passa a ser uma questão de integração posterior, não de convivência caótica durante a execução.

O uso intensivo de subagentes faz sentido quando o trabalho é repetitivo, bem delimitado e facilmente distribuível. Um caso típico é refatorar várias partes equivalentes de um codebase, em que múltiplos agentes podem aplicar a mesma transformação em paralelo com baixo risco de ambiguidade. Nessa situação, a divisão do trabalho reduz tempo sem exigir coordenação sofisticada. Já tarefas muito diferentes entre si, no mesmo contexto, tendem a aumentar a complexidade e a chance de erro.

Separar um modelo para planejar e outro para executar pode parecer uma otimização elegante, mas frequentemente introduz mais complexidade do que benefício. Cada troca de modelo cria novas fronteiras de contexto, novas possibilidades de desalinhamento e mais pontos de falha operacional. Como modelos de fronteira já resolvem grande parte do problema sozinhos, essa fragmentação pode até limitar a capacidade global do sistema. A decisão de combinar modelos deve responder a uma necessidade concreta, não a uma preferência arquitetural abstrata.

A decisão de orquestrar subagentes deve partir da dor do processo: onde ele falha, onde está lento e onde o custo sai do esperado. O formato de cobrança da ferramenta, seja por tokens ou assinatura, também influencia o desenho operacional mais eficiente. A regra prática é evitar reinventar a roda com workflows extravagantes quando o harness já faz a maior parte do trabalho por baixo dos panos. O foco deve estar em organizar sessões, chamadas e etapas de execução de forma previsível, com ganho real de tempo ou qualidade.

## Transcrição

00:00

Bom, pessoal, agora um outro ponto em relação ao

00:04

ambiente é como que você consegue orquestrar subagentes,

00:09

tá? E aqui é um ponto que eu quero que você preste muito,

00:12

mas muito atenção mesmo. Por que eu estou dizendo isso?

00:16

Porque eu vejo cada dia mais pessoas tentando fazer um malabarismo gigante,

00:21

trocando o modelo de tudo quanto é lado, criando todo um sistema,

00:26

mudando... para tentar forçar subagentes rodarem de formas espetaculares,

00:32

tentando economizar tokens, tentando fazer um monte de coisa,

00:36

para que simplesmente se você pegasse um modelo super top,

00:41

ele resolveria o problema todo.

00:43

Então eu não quero confundir essa orquestração de subagentes

00:48

com você querendo fazer um super malabarismo na sua máquina.

00:54

Para fazer com que uma coisa chame a outra,

00:56

que chame a outra e a coisa mais complexa do mundo. Então,

01:00

primeiro, antes de você querer, vamos dizer assim,

01:03

fazer uma otimização prematura na hora de desenvolver um software,

01:07

pense primeiro em conseguir entregar o software antes de você querer sair fazendo

01:11

todos os workflows mais malucos e forçando agentes e tudo quanto é lado.

01:17

Hoje, os mecanismos de harness, por exemplo,

01:20

um Cloud Code da vida, um Codex, por padrão,

01:23

eles já conseguem entender quando eles têm que lançar subagentes.

01:29

Eles já conseguem fazer uma administração muito boa disso. Então,

01:33

muitas vezes, você querer forçar e fazer coisas completamente diferentes vai fazer, no final das contas,

01:40

com que você gaste mais tempo e, às vezes,

01:43

nem tenha um resultado tão melhor em relação a você trabalhar.

01:49

Com todo um setup maluco que você pode criar.

01:53

Não estou dizendo que você não deve tentar melhorar, fazer os seus testes.

01:59

O que eu quero dizer para você é que tome muito

02:01

cuidado na hora de você querer ficar chamando um agente,

02:05

chamar outro agente, que chama um outro,

02:07

fazendo todo o maior malabarismo do mundo, porque às vezes você tem até um overhead,

02:13

ou seja, você tem um agente que tem que mandar contexto para o outro,

02:16

que recebe do outro, e daí simplesmente...

02:19

Você está fazendo uma coisa que simplesmente o seu harness padrão já faz.

02:26

Por outro lado, o que acontece?

02:29

A gente tem que partir do princípio que o harness que a

02:32

gente utiliza por padrão já vai resolver grande parte dos nossos problemas.

02:37

O grande ponto é que muitas vezes nós precisamos

02:42

organizar a forma de como a gente trabalha para que...

02:48

o seu processo consiga funcionar de uma forma um pouco mais previsível.

02:54

Por que eu estou dizendo isso?

02:56

Quando você não tem uma especificação clara,

02:58

quando você não tem necessariamente o que o agente vai ter que fazer,

03:02

simplesmente você não vai conseguir fazer as coisas rodarem em paralelo.

03:08

E rodar em paralelo não significa você dar um enter em uma única sessão

03:13

e ele sair disparando um milhão de agentes e fazendo todo o malabarismo do mundo.

03:18

Mas o que eu estou querendo dizer é que quando você consegue orquestrar agentes e

03:23

subagentes é você conseguir fazer com que

03:26

você crie agentes que façam coisas específicas, mas

03:31

não necessariamente esses agentes eles precisam

03:37

Estar rodando em paralelo um conversando com o

03:42

outro o tempo todo fazendo todo o maior malabarismo. E eu digo isso por quê?

03:47

Porque na prática,

03:48

principalmente quando a gente está falando em engenharia de software,

03:51

ninguém trabalha simplesmente rodando um Enter e o

03:55

software sai pronto do outro lado.

03:57

O desenvolvimento do software passa por diversas etapas,

04:00

que elas têm que ser verificáveis não somente pelos agentes,

04:03

pelas avaliações que a gente vai fazer e etc.,

04:06

mas pelo próprio usuário final. Então,

04:09

na prática, não adianta a gente querer atualizar o mundo.

04:13

Por outro lado, o que acontece?

04:16

Quando a gente entende por trás o que o Harness está fazendo,

04:19

por exemplo, tem um subagente que é lançado,

04:21

ele gera um fork, ou seja, ele pega um contexto anterior,

04:24

do contexto pai, e começa a partir dali,

04:28

ele já não começa do zero, porque ele já tem os dados de uma sessão.

04:32

O teammate, que é um recurso,

04:34

por exemplo, do Cloud, onde ele cria sessões separadas e,

04:37

através de arquivos que um agente vai gerando para o outro,

04:41

eles conseguem se comunicar.

04:42

Mas perceba que eles têm persistência ali de estado através de arquivos.

04:47

Ou quando a gente roda em WorkTrees,

04:50

ou seja, eu consigo trabalhar com diversos subagentes,

04:53

porém esses caras estão em WorkTrees totalmente isolados. Agora,

04:57

o ponto que é importante que você tem que se ligar é,

04:59

você só vai começar e trabalhar dessas formas, principalmente em paralelo,

05:05

se você tem... realmente, mecanismos,

05:08

especificações e pontos extremamente claros do que isso tem que ser feito,

05:12

porque se não, simplesmente,

05:14

na maioria das vezes eu acredito que não vai valer a pena,

05:17

principalmente porque grande parte dos modelos, hoje em dia, os modelos de fronteira, vamos dizer assim,

05:22

eles já conseguem resolver grandes partes do problema

05:26

e você pode estar limitando ele.

05:28

Então, o que eu digo hoje sobre orquestração de agentes e subagentes?

05:34

Grande parte disso vai ser feito pelo seu Harness.

05:37

Grande parte disso vai ser feito pela ferramenta que você vai estar utilizando.

05:42

Agora, como as sessões vão ser organizadas?

05:46

Como elas vão ser chamadas? Isso aí, as coisas podem ser feitas por você.

05:52

A única coisa que eu não quero é que você

05:55

faça uma engenharia totalmente prematura

05:57

para simplesmente querer fazer algo que...

06:03

Às vezes, um simples agente que você iria rodar iria resolver o problema,

06:07

tá? Agora, se você tem ferramentas ou se você tem problemas como,

06:13

ah, eu preciso, por exemplo,

06:15

refatorar esse codebase onde toda aquela parte é exatamente igual.

06:20

Poxa, aí eu posso soltar um monte de agentes

06:23

porque eles vão fazer trabalhos extremamente repetitivos, tá?

06:26

Agora tome muito cuidado com agentes e subagentes fazendo

06:29

tarefas muito diferentes dentro ali do mesmo contexto.

06:33

Tentando mudar um modelo para planejar, outro modelo para executar.

06:37

Aí as coisas começam a ficar muito complexas.

06:41

Então tome muito cuidado.

06:43

Grande parte dessas orquestrações já vão sendo feitas pelo harness que você tem.

06:48

O que você vai ter que saber é, principalmente,

06:50

é organizar o processo de execução desses caras.

06:54

A dica que eu dou é...

06:56

Não tente ficar reinventando a roda com workflows malucos.

07:00

Não estou dizendo que você não tem que testar,

07:02

mas o que eu estou querendo dizer é que grande parte de todas

07:06

essas orquestrações hoje em dia já estão sendo feitas por baixo do pano.

07:12

Você tem que ser sábio e conseguir entender onde está a dor,

07:17

onde está fazendo com que o seu processo fale,

07:19

ou onde você consegue fazer para que o seu

07:22

processo consiga rodar um pouco mais rápido,

07:24

mantendo o custo ali dentro do que você está esperando.

07:30

Então, isso vai depender, inclusive,

07:32

muito de como você vai estar rodando. Se você vai estar pagando por tokens,

07:36

se você está no modelo de assinatura,

07:38

como que a sua empresa trabalha. Agora, de forma geral,

07:41

evite criar processos de orquestrações malucas de subagentes.

07:46

Por outro lado, é interessante você saber que, sim,

07:50

você pode jogar um esquadrão de subagentes fazendo um monte de trabalho.

07:54

Mas tome muito cuidado para qual é o tipo de

07:57

trabalho que você vai pedir para esses casos.

## Resumo IA

**Abreviações**
(Nenhuma abreviação foi mencionada na aula que necessite de definição por extenso neste contexto.)

**Resumo**
A aula aborda a orquestração de subagentes em desenvolvimento de software, desmistificando a ideia de que complexas cadeias de chamadas são sempre a melhor solução. O objetivo central é alertar contra a otimização prematura e o "malabarismo técnico" na criação de workflows complexos, ressaltando que o harness (ambiente de execução/ferramenta) moderno já assume grande parte da coordenação, decidindo quando lançar subagentes e administrando o fluxo.

Forçar a orquestração de múltiplos agentes pode gerar overhead de contexto, sincronização e transferência de estado, resultando em maior tempo de execução e custo, muitas vezes sem superar o desempenho de um único modelo forte com um harness bem configurado. A complexidade extra só se justifica quando resolve um gargalo real.

A execução paralela de agentes é eficaz quando o trabalho pode ser decomposto em partes específicas, verificáveis e independentes, com fronteiras bem definidas. Criar agentes para tarefas específicas é útil, mas não implica interação contínua; a melhor abordagem é dividir responsabilidades e reduzir o acoplamento, comunicando-se por artefatos persistidos (como arquivos, no caso do recurso *teammate*) para maior auditabilidade. Ferramentas como *WorkTrees* permitem executar subagentes em ambientes isolados, evitando conflitos no *codebase*.

O uso intensivo de subagentes faz sentido para trabalhos repetitivos, bem delimitados e facilmente distribuíveis (ex: refatorar partes equivalentes de um código). A decisão de orquestrar deve ser motivada por problemas concretos no processo (lento, falho, custoso) e não por uma preferência arquitetural abstrata. O instrutor enfatiza que o harness já cuida da maior parte da orquestração, e o foco deve ser na organização previsível de sessões, chamadas e etapas de execução para ganho real de tempo ou qualidade.

**Pontos de atenção**
*   **Evite malabarismo técnico e otimização prematura**: Não tente construir cadeias complexas de chamadas entre agentes ou trocar modelos incessantemente para economizar *tokens* ou extrair desempenho marginal. Muitas vezes, um único modelo forte com um *harness* bem configurado resolveria o problema com menos esforço.
*   **Cuidado com o overhead**: Chamar um agente que chama outro gera custo de contexto, sincronização e transferência de estado, que pode aumentar tempo e gasto, sem melhoria real.
*   **Não force arquiteturas de subagentes**: Introduzir complexidade extra sem uma necessidade clara pode piorar o sistema em vez de melhorá-lo.
*   **Paralelismo exige clareza**: Não use paralelismo de agentes sem uma especificação clara do que cada um deve fazer; caso contrário, resultará em concorrência desorganizada e improdutiva.
*   **Reduza o acoplamento**: Evite que múltiplos agentes interajam continuamente no mesmo contexto. Prefira dividir responsabilidades em sessões separadas e usar comunicação via artefatos persistidos (como arquivos) para maior previsibilidade e auditabilidade.
*   **Cuidado com ambientes compartilhados**: Se agentes atuam no mesmo *codebase*, utilize *WorkTrees* ou mecanismos de isolamento para evitar conflitos diretos e gerenciar a coordenação posteriormente.
*   **Evite fragmentação desnecessária de modelos**: Separar um modelo para planejar e outro para executar pode introduzir mais complexidade, desalinhamento e pontos de falha do que benefícios, especialmente quando modelos de fronteira já resolvem grande parte dos problemas.
*   **Não reinvente a roda**: O *harness* já faz grande parte da orquestração "por baixo dos panos". Concentre-se em organizar sessões, chamadas e etapas de execução de forma previsível, buscando ganhos reais de tempo ou qualidade.
*   **Analise a "dor do processo"**: A decisão de orquestrar subagentes deve ser guiada por onde o processo falha, está lento ou excede o custo esperado.
*   **Considere o formato de cobrança**: A forma como a ferramenta é cobrada (por *tokens*, assinatura, etc.) deve influenciar o desenho operacional mais eficiente.
*   **Subagentes para tarefas específicas e repetitivas**: O uso intensivo de subagentes faz sentido quando o trabalho é repetitivo, bem delimitado e facilmente distribuível (ex: refatorar múltiplas partes equivalentes de um *codebase*). Evite que subagentes façam tarefas muito diferentes no mesmo contexto.
*   **Foque na funcionalidade e controle**: Priorize a entrega de software funcional com um processo controlável antes de buscar otimizações avançadas de orquestração.