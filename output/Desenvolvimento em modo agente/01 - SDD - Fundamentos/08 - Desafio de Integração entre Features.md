Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17772)

## Resumo da aula

O principal risco em SDD não está apenas em especificar features isoladas, mas em garantir que elas se conectem corretamente quando são implementadas em momentos diferentes. Um PRD pode descrever bem a Feature 1 e a Feature 2, mas isso não garante que a transição entre elas exista no sistema real. O problema aparece quando cada feature é gerada como uma unidade coerente por si só, porém sem pontos de ligação explícitos com as demais. Nesse cenário, a especificação faz sentido no papel, mas a experiência do usuário quebra na integração.

Retomando a ideia de PRD e desenvolvimento por fases já estabelecida, o ponto novo aqui é que a consistência semântica entre features não produz, sozinha, consistência operacional. Dizer que uma landing page leva ao login e que o login leva ao dashboard não basta se essas conexões não estiverem claramente previstas para a implementação. O agente pode gerar cada parte corretamente e ainda assim deixar faltar o link para /login ou o redirecionamento após autenticação. A falha não está na existência das features, mas na ausência de contratos explícitos entre elas.

Quando a landing page permite criar conta ou iniciar login, ela precisa preparar a navegação para a feature seguinte. Isso inclui apontar para a rota correta, usar os fluxos esperados e manter coerência com o comportamento definido para autenticação. Se a landing page foi implementada antes, mas sem considerar como a feature de login será acoplada depois, o resultado tende a ser uma interface visualmente pronta, porém desconectada do fluxo real do sistema. A integração precisa ser tratada como requisito funcional, não como ajuste posterior.

Lembra do fluxo em que o usuário faz login e segue para outra área do sistema? Aqui a camada nova é perceber que autenticar com sucesso não encerra a feature; o comportamento de continuação também faz parte dela. Se o sistema apenas retorna algo como “estou logado”, mas não redireciona para o dashboard previsto, a feature de login está tecnicamente funcionando e, ao mesmo tempo, funcionalmente incompleta. Em SDD, esse tipo de quebra é comum quando a próxima etapa do fluxo pertence a outra feature e não foi amarrada de forma explícita.

Features precisam declarar não só o que fazem internamente, mas também como entregam contexto para a próxima etapa do sistema. Essa conexão pode envolver rotas, navegação, redirecionamentos, estados esperados após uma ação e dependências de fluxo entre partes implementadas separadamente. Sem isso, o desenvolvimento paralelo aumenta a chance de produzir blocos corretos, porém incompatíveis entre si. A integração deixa de ser detalhe de implementação e passa a ser parte central da especificação.

Quando duas features não se conversam, o desenvolvedor precisa interromper o fluxo orientado por especificação e passar a corrigir manualmente a ligação entre elas. Isso reduz o ganho operacional do SDD, porque a IA deixa de seguir uma fonte de verdade integrada e passa a depender de instruções pontuais para costurar o sistema. Minimizar esse problema exige pensar nas interfaces entre features desde o início, especialmente em cenários com implementação em sessões separadas ou em paralelo. O custo real não é apenas um bug de navegação, mas a perda de continuidade do processo orientado por especificação.

## Transcrição

00:01

Pessoal, como eu estava falando que eu queria mostrar isso mais de perto,

00:05

que é o seguinte, o que já aconteceu comigo inúmeras vezes,

00:09

e eu não sei se isso já aconteceu com você, é que você cria um PRD,

00:14

e esse PRD tem diversas features.

00:17

Feature 1, Feature 2, e assim vai.

00:23

E o que acontece? Como essas features são desenvolvidas em sessões diferentes,

00:28

em momentos diferentes, o grande problema...

00:30

é que a feature 1 e a feature 2, elas acabam não se comunicando.

00:35

A gente tem um problema grande aqui nesse aspecto, tá?

00:39

E eu vou dar um exemplo bem simples.

00:41

Imagina que eu falo para ele fazer uma landing page, tá?

00:44

E nessa landing page, eu falo que quando o cara fizer login, ele, sei lá,

00:49

ele vai cair num dashboard. Ou quando eu estou na landing page,

00:55

ele vai criar uma conta.

00:58

e essa conta vai cair na feature de login.

01:01

Se você perceber, aqui é uma feature de landing page,

01:05

aqui é uma feature de login. Como essa feature foi feita antes dessa feature aqui,

01:10

como que essa feature aqui consegue preparar o usuário, o agente,

01:16

para quando ele for criar essa feature aqui,

01:18

ela esteja linkada com essa? Na maioria das vezes, tá?

01:23

eu acredito que se você já trabalhou com SDD ou dependendo dos frameworks,

01:27

vai acontecer coisa mais ou menos assim,

01:29

ele vai gerar a landing page, aí na hora que ele for gerar o login,

01:33

ele vai gerar uma rota barra login,

01:35

mas na landing page não vai ter necessariamente o link certo para o login,

01:40

ou o que pode acontecer é,

01:42

depois que o cara fizer o login na feature retrace, que vai ser um dashboard,

01:47

o cara vai fazer o login, mas quando ele fizer o login vai falar, estou logado.

01:52

mas não necessariamente ele vai redirecionar o usuário para a tela do dashboard.

01:58

Por quê? Porque essas features, nas especificações, elas existem e fazem sentido,

02:04

mas na hora da implementação, o que acontece? Elas não se conversam.

02:10

Esse é o maior calcanhar de Achilles na hora que você vai trabalhar com o SDD,

02:15

pelo fato de as features têm que ter conexões claras.

02:20

Então, quando a gente for falar em trabalhar paralelo,

02:22

eu vou dar mais detalhes, inclusive, criei alguns diagramas,

02:25

porque, na minha opinião,

02:26

essa é a maior complexidade que você vai ter ao longo do tempo,

02:31

que é fazer com que uma feature fale com a

02:34

outra e elas não fiquem isoladas dentro do sistema,

02:37

e aí você tem que sair do SDD e ficar lá falando com a IA,

02:41

porque uma coisa não está falando com a outra.

02:43

A ideia aqui é minimizar esse tipo de problema.

02:47

Beleza? Então, esse aqui é um parênteses que eu queria trazer para você.

## Resumo IA

**Abreviações**
*   **IA**: Inteligência Artificial
*   **PRD**: Product Requirements Document
*   **SDD**: Software-Driven Development

**Resumo**
O principal objetivo desta aula é abordar o risco crítico em SDD onde features, embora bem especificadas individualmente em um PRD, falham em se conectar operacionalmente quando implementadas em momentos ou sessões distintas. O instrutor destaca que a consistência semântica das especificações não garante a consistência operacional na prática.

A aula explora o problema de features serem geradas como unidades coerentes por si só, mas sem pontos de ligação explícitos com as demais. Isso leva a uma experiência do usuário quebrada na integração, mesmo que no papel a especificação faça sentido. Um exemplo ilustra essa falha: uma landing page que deveria levar ao login, e o login que deveria redirecionar para um dashboard. Se as conexões (como a rota para `/login` ou o redirecionamento pós-autenticação) não forem explicitamente previstas e implementadas, as features podem existir e funcionar tecnicamente, mas o fluxo completo da aplicação é interrompido.

Os conceitos abordados incluem a importância de considerar a integração como um requisito funcional, e não como um ajuste posterior. As features devem declarar não apenas o que fazem internamente, mas também como entregam contexto para a próxima etapa do sistema. Isso envolve a especificação clara de rotas, navegação, redirecionamentos, estados esperados após uma ação e dependências de fluxo entre partes que podem ser implementadas em paralelo. A ferramenta principal mencionada é o PRD, mas o foco é na sua aplicação e detalhamento para garantir a conectividade. O fluxo explicado enfatiza que o comportamento de continuação de uma feature (como um redirecionamento após o login) é parte integrante dela, e não um detalhe externo.

**Pontos de atenção**
*   **Risco de Desconexão**: O principal risco em SDD não é a especificação de features isoladas, mas garantir que elas se conectem corretamente quando implementadas em momentos diferentes.
*   **Quebra da Experiência do Usuário**: A especificação pode fazer sentido no papel, mas a experiência do usuário pode quebrar na integração se as features não tiverem pontos de ligação explícitos.
*   **Consistência Semântica vs. Operacional**: A consistência semântica entre features não produz, sozinha, consistência operacional. É preciso prever as conexões operacionais.
*   **Integração como Requisito Funcional**: A integração entre features deve ser tratada como um requisito funcional desde o início, e não como um ajuste posterior ou um "bug de navegação".
*   **Features Incompletas**: Uma feature pode estar tecnicamente funcionando (ex: "estou logado"), mas funcionalmente incompleta se seu comportamento de continuação (ex: redirecionar para o dashboard) não for amarrado explicitamente à próxima etapa do fluxo.
*   **Declaração de Contexto**: Features precisam declarar não só o que fazem internamente, mas também como entregam contexto para a próxima etapa do sistema (rotas, navegação, redirecionamentos, estados esperados, dependências de fluxo).
*   **Custo da Desconexão**: Quando as features não se comunicam, o desenvolvedor precisa interromper o fluxo orientado por especificação e corrigir manualmente, o que reduz o ganho operacional do SDD e faz com que a IA dependa de instruções pontuais.
*   **Boas Práticas**: Pensar nas interfaces entre features desde o início, especialmente em cenários com implementação em sessões separadas ou em paralelo, para minimizar problemas. As conexões claras devem ser parte central da especificação.