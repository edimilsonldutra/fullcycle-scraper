Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17778)

## Resumo da aula

Retomando o problema de integração entre features já estabelecido, a qualidade de uma especificação não depende só de descrever bem uma feature isolada. O ponto crítico é explicitar como ela se conecta às demais sem invadir responsabilidades que pertencem a outras partes do sistema. Na landing page, isso aparece nas rotas /register, /login e /app, que já nascem como pontos de contato com features futuras. Esse “grude” precisa estar documentado antes da implementação, porque é ele que evita que o sistema evolua como blocos desconectados.

O spec.md traduz a feature em decisões técnicas executáveis. Aqui, a especificação classifica a landing page como full scope, parte do núcleo da aplicação e de complexidade simples, além de registrar o comportamento esperado, a stack usada e a direção visual mínima. O valor desse documento não está em repetir o PRD, mas em transformar critérios de produto em estrutura técnica concreta. Quando a especificação cita arquivos, fluxo de navegação e componentes afetados, ela reduz ambiguidade para a implementação.

Uma feature bem especificada delimita claramente o que ela entrega e o que fica para outras features. Na landing page, links para autenticação e acesso ao app aparecem no escopo porque fazem parte da navegação, mas a implementação real de login, registro, sessão, banco e ORM permanece fora dela. Essa separação impede que a Feature 1 absorva responsabilidades da Feature 2 ou da Feature 4. O resultado é uma implementação menor, mais previsível e compatível com desenvolvimento incremental.

Lembra da autenticação que ainda será implementada depois? Aqui ela já influencia a Feature 1 por meio de um getSession em forma de stub. O stub funciona como um módulo fake que preserva o contrato necessário para a integração, mesmo sem existir ainda uma sessão real. Isso permite que a landing page seja construída com pontos de acoplamento corretos desde o início, sem bloquear o avanço por dependências ainda não concluídas.

O fluxo descrito na especificação mostra como a navegação atravessa os artefatos da feature. O visitante acessa a rota, a requisição chega ao page.tsx, a página consulta o getSession stubado e então renderiza os elementos da interface, incluindo logo, proposta de valor e links para rotas pertencentes a outras features. Esse fluxo importa porque transforma uma ideia visual em sequência técnica verificável. Quando o fluxo está explícito, fica mais fácil validar se a feature realmente respeita os contratos definidos.

A especificação também registra por que certas escolhas foram feitas, quais alternativas foram consideradas e qual trade-off foi aceito. Esse trecho é especialmente importante em SDD porque a decisão não fica implícita no código nem perdida na conversa com a IA. Documentar a justificativa reduz retrabalho e ajuda a manter consistência quando outras features precisarem se integrar a essa base. Em vez de apenas dizer “faça assim”, o documento preserva o raciocínio técnico que sustenta a escolha.

Os critérios de aceitação do PRD continuam sendo a referência de validação, mas a especificação os converte em cobertura técnica da feature. Quando algum ponto não foi totalmente definido durante a clarificação, o documento explicita suposições ou levanta perguntas pendentes, em vez de esconder a incerteza. Isso é essencial para evitar que a implementação invente comportamento sem rastreabilidade. Uma boa especificação não elimina dúvidas; ela torna as dúvidas visíveis e controláveis.

O plan.md organiza a execução em fases (stages) e passos (steps), conectando pré-requisitos da stack com a ordem de construção da feature. No caso da landing page, o plano distribui o trabalho em oito passos, passando por guidelines visuais, composição da página e verificação final. A utilidade do plano está em transformar a especificação em sequência operacional, com granularidade suficiente para um agente executar sem precisar reinterpretar o documento inteiro a cada ação. Ele não substitui a especificação; ele operacionaliza a especificação.

Aqui ainda não existe um documento de tarefas para marcar o que foi concluído, o que significa que o agente não mantém estado explícito de execução entre interrupções. Isso limita a continuidade do trabalho, porque não há registro formal de onde ele parou ou de qual passo já foi validado. O plano descreve a ordem de execução, mas não funciona como trilha de progresso persistente. Esse detalhe separa planejamento de execução stateful: um define o caminho, o outro registra o avanço real.

## Transcrição

00:01

E bom, pessoal, o seguinte, olha só que interessante agora, tá?

00:06

A gente teve a geração da nossa feature 01,

00:10

que é a nossa landing page, tá? Então,

00:13

eu vou mostrar esse documento aqui e depois a

00:16

gente vai fazer a implementação ali dessa feature.

00:19

Depois eu vou mostrar para vocês como que

00:22

a gente pode fazer uma implementação mais sem guidance.

00:29

Ou como a gente pode usar uma outra skill que dá

00:32

mais guidance para a IA na hora dela fazer a criação.

00:36

Então, basicamente, aqui dentro da landing page,

00:40

você vai perceber que eu tenho um arquivo de spec.

00:43

Deixa eu fechar o Cloud Code aqui enquanto isso vai,

00:45

para ficar melhor para a gente ler.

00:48

Então, eu tenho aqui uma especificação. Então,

00:50

ele fala o seguinte, landing page, technical specification.

00:54

É um full scope, faz parte da parte core da aplicação.

00:59

A complexidade dela é simples,

01:02

tem um technical overview explicando o que tem que acontecer,

01:06

vai aparecer VideoMax MBA,

01:07

vai ter um CTA apontando para a barra register,

01:10

um login apontando para a barra login,

01:12

uma barra app, ele vai usar o Create Next App.

01:18

vai ter um design minimalista parecendo com o HubSpot, o HubSpot é um CRM e etc.

01:24

E perceba que eu não fui fundo no front-end,

01:27

depois a gente vai fazer uma parte só pensada em front-end,

01:32

porque merece uma atenção completamente distinta, tá? Mas se você perceber,

01:39

perceba que essa barra login, barra app, barra register, ela cai exatamente no quê?

01:47

naquele grude das funcionalidades. Então,

01:51

esse aí é o ponto importante antes de a gente desenvolver.

01:55

Daí ele traz o porquê, a Feature 1, ele está falando,

01:58

vai trabalhar com o app Global CSS,

02:00

o app Components, e ele vai gerar aqui para ele,

02:04

vai evitar para fazer com que a

02:07

Feature 2 de autenticação tenha que trabalhar,

02:12

e sabe que a Feature 2 precisa de sessões, ele vai...

02:16

entregar um getSession pronto como uma stub, ou seja, como um módulo fake,

02:21

somente para que essa parte desse grude

02:27

entre a autenticação e a landing page funcione.

02:30

Então, isso aí é um ponto interessante. O que está incluso no escopo?

02:35

O que está excluído? Porque vai ser lidado por outras features, ou seja,

02:41

o register e o login vão ser feitos pela feature 2.

02:44

A criação da sessão vai ser pela feature 2. O barra app vai ser na feature 4.

02:49

O database, o RM, etc., vai ser na feature 02.

02:55

Internacionalização e marketing analytics, por exemplo. Então,

02:58

essas coisas estão excluídas porque eu quero focar somente no que tem.

03:02

E aqui tem a arquitetura e o impacto aqui. Componentes afetados,

03:07

o nome dos arquivos que ele vai gerar, aqui para mim. E o fluxo.

03:11

de como que funciona essa minha landing page. Então, o visitante acessa essa barra,

03:16

vai cair no page.tsx, vai pegar um getSession aqui, que vai ser uma stub,

03:22

ele vai fazer o render da landing page, vai ter a chamada,

03:26

A proposição da página, o register,

03:30

que vai ser feito pela feature 2 de autenticação,

03:33

o logo, o barra login, que também é dono dela, a...

03:38

a feature 2. Então, se você perceber,

03:41

o que eu acho que é mais importante antes de a gente começar a rodar código aqui,

03:45

é que você entenda essas relações e como uma feature gruda na outra.

03:50

O que eu diria para você é que todas as vezes que você pensar em SDD,

03:55

fazer especificação sendo gerada, é

04:00

difícil, é, ter um bom prompt, criar uma skill bem feita, é. Mas,

04:04

mais difícil ainda é conseguir fazer com que... as features,

04:09

elas consigam estar entrelaçadas, tá? E aí tem decisões técnicas.

04:14

Essas decisões técnicas, galera,

04:16

elas foram feitas baseadas na entrevista que eu tive ali com a IA.

04:22

Então, ó, decisão, como que foi escolhido,

04:25

qual que é a alternativa que foi considerada, qual o trade-off. Então,

04:28

ele traz isso para as principais decisões que acabou trazendo.

04:32

Daí o overview do componente, a página, global .css,

04:37

e etc, e etc, e etc,

04:40

assets estáticos, onde ele vai poder trabalhar,

04:45

e aqui, o back-end não tem nada de API,

04:49

API contratos basicamente é o page só,

04:52

não tem data model, e a estratégia de teste, e

04:56

também, se eu quiser, os arquivos de test function,

05:01

como é que isso vai ser feito, e etc, aqui para a gente. Então,

05:07

Basicamente, ele traz aqui tudo que é critério que está no PRD

05:13

de aceitação para garantir que essa feature consiga cobrir todos esses critérios.

05:18

E o que ele vai tomar como ele acredita que

05:24

deve ser e que durante uma discussão não foi feita.

05:28

Então, basicamente,

05:30

são algumas perguntas aqui que ele acaba trazendo ali para a gente. Então...

05:35

Essa é a base e ele

05:38

fala aqui a rastreabilidade entre as features.

05:43

Então, se você perceber, galera, eu acho que grande diferencial,

05:46

inclusive no que você está vendo agora, apesar de ser...

05:49

É difícil falar que é teórico ou é prático,

05:54

porque gerar e rodar uma skill é algo prático,

05:58

mas que gera documento que acaba sendo teórico.

06:01

Mas você vai ver que o principal entendimento que você tem que ter é...

06:05

Como você estrutura e como que você gruda uma coisa na outra.

06:08

Esse aí eu acho que é o grande ponto.

06:11

O outro passo aqui é o nosso plano .md, tá? Esse plano aqui, ele já é

06:18

diferente, né? Porque aqui ele traz os pré-requisitos com a minha stack, tá?

06:27

Daí foundational visual guidelines,

06:30

ou seja, cada stage desse é uma fase.

06:35

E cada item desse aqui é um step. Então, step 1, step 2, step 3.

06:43

Aí passo 2, landing page composition.

06:46

Step 4, step 5, step 6. Verificação e setup.

06:50

Step 3 aqui, quer dizer, step 7 e step 8.

06:54

Então, em oito passos, ele vai criar esse cara aqui. Se você perceber,

06:59

eu não tenho aqui nenhum documento de tarefas para

07:02

Ele marcar o que está feito ou não.

07:04

Então, eu não estou falando ainda em armazenamento de estado,

07:07

de onde que o meu agente parou, de onde que o meu agente continuou.

07:13

Então, esse aí é um aspecto aqui importante para vocês. No próximo vídeo,

07:18

eu vou pedir para isso ser executado finalmente,

07:22

para a gente brincar e ver como é que...

07:27

tudo isso aí acaba funcionando. Vamos nessa.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirements Document
*   **SDD**: Software Design Document
*   **CTA**: Call To Action
*   **CRM**: Customer Relationship Management
*   **IA**: Inteligência Artificial
*   **ORM**: Object-Relational Mapping
*   **CSS**: Cascading Style Sheets
*   **API**: Application Programming Interface
*   **TSX**: TypeScript XML (referindo-se à extensão de arquivo para componentes React com TypeScript)

**Resumo**
A aula aborda a importância da integração de features e como a documentação técnica é fundamental para garantir que o sistema não evolua como blocos desconectados. O objetivo é demonstrar como especificar e planejar a construção de uma feature (a landing page, Feature 1) que se conecta a outras funcionalidades futuras, como autenticação e o aplicativo principal.

A especificação técnica, detalhada no arquivo `spec.md`, traduz os critérios de produto em decisões técnicas executáveis. Para a landing page, isso inclui classificá-la como "full scope", parte do núcleo da aplicação e de complexidade simples. O documento registra o comportamento esperado, a stack utilizada (ex: Create Next App), a direção visual mínima e, crucialmente, explicita como ela se conecta a rotas como `/register`, `/login` e `/app`. Ele diferencia o que está no escopo (links de navegação) do que está excluído (implementação real de login, registro, sessão, banco de dados e ORM), que será tratado por outras features.

Um conceito chave é o uso de "stubs" ou módulos fake, como o `getSession`, para simular o contrato de integração com dependências futuras (ex: autenticação, Feature 2) que ainda não foram implementadas. Isso permite que a landing page seja construída com pontos de acoplamento corretos desde o início, sem bloquear o avanço.

O `spec.md` também descreve o fluxo de navegação, detalhando como o visitante acessa a rota, a requisição chega ao `page.tsx`, a página consulta o `getSession` stubado e então renderiza os elementos da interface. Além disso, documenta as decisões técnicas, justificativas, alternativas consideradas e trade-offs aceitos, transformando os critérios de aceitação do PRD em cobertura técnica e explicitando suposições ou perguntas pendentes.

Paralelamente, o arquivo `plan.md` organiza a execução da feature em fases (stages) e passos (steps), conectando pré-requisitos da stack à ordem de construção. Para a landing page, o plano distribui o trabalho em oito passos, cobrindo diretrizes visuais, composição da página e verificação final. Este documento serve para operacionalizar a especificação, fornecendo uma sequência de ações detalhada, embora não funcione como um registro de progresso persistente do agente de execução.

**Pontos de atenção**
*   **Integração de Features**: O ponto crítico de uma especificação é explicitar como uma feature se conecta às demais sem invadir responsabilidades de outras partes do sistema.
*   **Documentação Precoce da Integração**: O "grude" entre as features (pontos de contato) precisa estar documentado *antes* da implementação para evitar que o sistema evolua como blocos desconectados.
*   **Escopo Claro e Separação de Responsabilidades**: Uma feature bem especificada delimita claramente o que ela entrega e o que fica para outras features, resultando em implementações menores, mais previsíveis e compatíveis com desenvolvimento incremental. Evite que uma feature absorva responsabilidades alheias.
*   **Uso de Stubs para Dependências Futuras**: Utilize stubs (módulos fake) para preservar contratos de integração com funcionalidades futuras. Isso permite que o desenvolvimento avance sem ser bloqueado por dependências ainda não concluídas, garantindo pontos de acoplamento corretos desde o início.
*   **Valor do `spec.md`**: Não repita o PRD; use o `spec.md` para transformar critérios de produto em estrutura técnica concreta, citando arquivos, fluxo de navegação e componentes afetados para reduzir a ambiguidade na implementação.
*   **Fluxo de Navegação Explícito**: Documente o fluxo de navegação para transformar uma ideia visual em uma sequência técnica verificável, facilitando a validação dos contratos definidos.
*   **Registro de Decisões Técnicas**: Documentar as justificativas, alternativas consideradas e trade-offs aceitos para as escolhas técnicas no `spec.md` (especialmente em SDD) é essencial para reduzir retrabalho e manter a consistência, em vez de deixar a decisão implícita no código.
*   **Visibilidade de Incertezas**: Uma boa especificação não elimina dúvidas, mas as torna visíveis e controláveis, explicitando suposições ou levantando perguntas pendentes, evitando que a implementação "invente" comportamento sem rastreabilidade.
*   **Propósito do `plan.md`**: O `plan.md` operacionaliza a especificação, distribuindo o trabalho em etapas granulares. Ele não substitui a especificação, nem serve como um documento de tarefas para registro de estado de execução (ou seja, não mantém o progresso persistente do agente).