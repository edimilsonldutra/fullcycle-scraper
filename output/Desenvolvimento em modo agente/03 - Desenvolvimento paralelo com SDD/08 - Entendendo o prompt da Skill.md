Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17797)

## Resumo da aula

O prompt da skill começa definindo como o agente encontra os artefatos de entrada que governam a execução. Isso inclui localizar spec.plan.md, identificar padrões de feature, extrair a feature ID quando ela existir e procurar referências explícitas a arquivos de PRD, normalmente dentro de docs. Essa etapa reduz ambiguidade logo no início e permite abortar cedo quando a especificação necessária não está disponível. A escolha por instruções explícitas força um parsing mais determinístico, mesmo que modelos mais capazes consigam inferir parte disso sozinhos.

A skill exige leitura integral do arquivo de plano e da especificação para evitar execução baseada em leitura parcial. O PRD é tratado como fonte de critérios de aceitação, e o agente deve reconhecer diferentes formas de expressá-los, como seções nomeadas, AC e estruturas em checklist. Esses critérios alimentam as verificações posteriores e funcionam como contrato de validação da implementação. Se o PRD não trouxer critérios explícitos, a execução continua, mas a ausência pode ser registrada como soft fail.

A exploração do codebase deve ser feita de forma lazy, abrindo arquivos apenas quando a fase atual exigir. Essa restrição não redefine a economia de tokens já discutida antes; aqui ela aparece como regra operacional dentro do prompt da skill. O objetivo é evitar leitura ampla e prematura do repositório, reduzindo custo e dispersão de contexto. Isso transforma a exploração em uma atividade guiada pelo plano, e não em uma varredura indiscriminada.

Os overrides permitem alterar o comportamento padrão da skill sem reescrever sua estrutura principal. É possível mudar o número máximo de tentativas antes de declarar hard fail, exigir parada ao fim de cada fase, pedir um commit por fase, desabilitar testes ou linter e restringir a execução a fases específicas, como fase 1 ou fase 2. Essa camada torna o prompt configurável para diferentes cenários de execução. O valor prático está em separar política padrão de exceções pontuais solicitadas pelo operador.

A política de retries existe para impedir que o agente fique preso em ciclos intermináveis ao tentar corrigir uma falha. Em vez de permitir tentativas indefinidas, o prompt define um teto explícito; ao ultrapassá-lo, a falha deixa de ser tratada como recuperável e interrompe a execução. Isso é especialmente importante em tarefas que envolvem comandos, validações ou correções automáticas repetitivas. Um agente autônomo sem limite de repetição pode consumir tempo e tokens sem convergir.

O modo padrão pode ser full autônomo, no qual o agente executa todas as fases sem pedir confirmação intermediária. Ainda assim, o prompt preserva a possibilidade de impor checkpoints, como parar ao fim de cada fase ou gerar um commit por fase concluída. Essa escolha altera o grau de supervisão humana sem mudar o fluxo lógico da skill. O mesmo mecanismo permite pedir execução parcial quando só algumas fases devem ser implementadas.

Retomando o uso do PRD e do plano como contrato, a checklist é tratada como um núcleo imutável que precisa ser trackeado durante toda a execução. Antes de implementar, o agente faz um pre-flight com dependency check para verificar se a feature pode ser desenvolvida no estado atual do software. Isso inclui validar o grafo de dependências entre features, tema já estabelecido anteriormente, agora aplicado como regra de abort precoce dentro da skill. Se um pré-requisito ainda não foi entregue, a implementação não deve começar.

A fase de execução segue o plan.md e pode dar skip em itens já implementados ou já commitados, usando o ID como referência. Essa regra evita retrabalho e permite retomar execuções interrompidas com mais segurança. O plano deixa de ser apenas documentação e passa a funcionar como roteiro operacional verificável. A implementação acontece somente depois dessa checagem de estado.

A skill diferencia falhas que impedem continuidade de falhas que apenas reduzem a confiança na validação. Hard fail ocorre quando falta algo essencial para executar ou validar a tarefa; soft fail ocorre quando a implementação pode continuar, mas a validação não foi completa. Pre-existing failure isola erros que já existiam antes da mudança e não devem ser atribuídos ao código recém-alterado. Essa classificação melhora o relatório final e evita que o agente trate todo erro como bloqueador.

Nem toda limitação de ambiente deve interromper a execução. Se faltar, por exemplo, uma OpenAI API key, isso pode afetar testes específicos sem impedir a implementação do serviço em si; nesse caso, a ausência é tratada como soft fail ligado à validação. A regra importante é distinguir incapacidade de implementar de incapacidade de comprovar completamente o resultado. Essa separação preserva produtividade sem mascarar risco.

A skill pode instruir o agente a seguir o padrão dos últimos 10 commits para manter consistência com o histórico do projeto. Na ausência de padrão, ela pode cair em uma convenção alternativa, como incluir a feature ID na mensagem. Essa prática é útil em contexto didático ou em workflows fortemente baseados em SDD, mas não deve ser adotada automaticamente em produção. IDs de feature nem sempre ajudam humanos a navegar o histórico e podem introduzir ruído quando o projeto tem múltiplas convenções ou nomenclaturas repetidas.

A validação final combina execução da suíte, navegação por componentes, rotas e schemas, rechecagem dos critérios de aceitação e um smoke check com o ambiente em execução. Retomando a regra de ouro das integrações, os critérios cross-feature também entram no relatório quando aplicável. O objetivo não é apenas confirmar que o código compila, mas verificar regressão funcional e aderência ao contrato definido na especificação. O resultado final precisa distinguir sucesso completo, sucesso com regressões, incompletude e abort.

O final report padroniza a resposta do agente ao fim da execução. Ele deve informar branch, fases executadas, critérios atendidos, integrações validadas, partes não implementadas da especificação, regressões encontradas, desvios adotados, problemas pré-existentes, instruções reaplicadas, instruções ignoradas e, se houver abort, sua causa. Esse formato transforma a saída do agente em artefato auditável. Em vez de uma resposta narrativa solta, o operador recebe um resumo operacional rastreável.

Modelos tendem a dar mais peso às instruções mais recentes do contexto, então o fim do prompt é um lugar estratégico para reforçar regras críticas. Um recap com comandos do tipo always e never ajuda a impedir comportamentos indesejados, como declarar sucesso apesar de regressão ou pular verificações obrigatórias. Essa redundância não é mero excesso textual; ela funciona como mecanismo de alinhamento comportamental. O conjunto ideal dessas repetições é descoberto empiricamente, observando onde o agente ainda desvia.

Casos de borda precisam aparecer de forma explícita no prompt para evitar decisões improvisadas em situações não previstas. Se o agente não encontrar PRD, SPEC ou dependências necessárias, ele deve abortar com mensagem clara, em vez de seguir com suposições frágeis. Essa abordagem reduz falsos positivos de sucesso e melhora a depuração do workflow. Edge cases bem definidos tornam a skill mais previsível.

O valor principal dessa skill não está em ser um template universal, mas em explicitar uma estrutura que pode ser adaptada. Cada desenvolvedor tende a precisar de controles, tolerâncias e relatórios diferentes ao trabalhar com IA. Por isso, entender a lógica do prompt é mais importante do que copiar sua forma literal. À medida que os modelos evoluem, parte dessas instruções deve ser removida para evitar microgerenciamento que limite capacidades úteis do agente.

## Transcrição

00:00

Bom, pessoal, então é o seguinte. Olha aqui essa skill que eu acabei colocando.

00:05

Então, a primeira coisa que eu falei é para ele resolver os inputs.

00:09

Ou seja, para ele procurar o spec .plane.md, procurar esses padrões de features,

00:14

para ele saber a feature ID, caso passe.

00:17

Normalmente, por padrão,

00:18

ele está na pasta docs e para ele

00:21

procurar referências explícitas de arquivos de PRD.

00:24

Se você olhar aqui, uma coisa que é importante eu dizer,

00:28

pessoal, cada vez mais os nossos modelos são mais inteligentes.

00:32

Da forma como eu estou colocando aqui, eu estou forçando ele a parsear algo.

00:37

de uma forma mais explícita. Então, você vai perceber que ao longo do tempo,

00:42

ou provavelmente, eu não precisaria ser tão explícito dessa forma,

00:48

porque provavelmente o agente já seria capaz de descobrir tudo isso.

00:54

Então, apenas uma observação.

00:56

Mas eu deixei isso aqui mais forte, mais, como se diz, mais explícito aqui para ele.

01:02

E por quê? Porque caso ele não encontre a especificação,

01:07

eu vou pedir para ele abortar aqui para mim também.

01:10

Então, basicamente, é isso. Outra coisa,

01:13

eu pedi para ele ler completamente o arquivo

01:16

de plano e também o arquivo de especificação,

01:21

falando o que ali esse cara tem dentro. E também,

01:25

para ele entender que o PRD tem,

01:28

basicamente, critérios de aceitação. Ou seja,

01:33

para ele buscar algo como critérios de aceitação,

01:35

Critérios eu coloquei em português, inclusive. AC,

01:38

Typical Shape, tipo espécies de checkbox. Então,

01:43

tudo isso pode ser considerado como critérios de aceitação que ele

01:46

vai utilizar na hora que ele for fazer verificações.

01:49

Se o PRD não tiver nenhum critério, ele vai, na realidade,

01:53

seguir. E ele pode colocar isso sobre soft fails,

01:58

caso ele não consiga passar ali para a gente.

02:01

E aí eu coloquei algumas coisas bem simples aqui.

02:05

Você não precisa explorar o

02:08

codebase mais do que você precisa.

02:14

Você pode abrir os arquivos de forma lazy,

02:17

ou seja, on demand. Eu não quero que ele leia tudo ao mesmo tempo.

02:21

Ou seja, vá trabalhando de acordo com a fase que você vai utilizar.

02:27

O que eu estou tentando aqui é minimizar a utilização um pouco de tokens.

02:30

Isso não necessariamente vai garantir.

02:33

Outra coisa. Apply overrides. Então, por exemplo,

02:36

algumas coisas eu coloquei ali para ele como padrão. Por exemplo,

02:41

toda vez que ele tentar algo e que pode dar para ele um hard fail,

02:47

ele vai tentar três vezes. Se ele não conseguir,

02:50

ele vai simplesmente parar ali para mim.

02:53

Então, o que eu estou falando para ele é, olha,

02:56

se você estiver fazendo algo que não der certo, tente cinco vezes, tente dez vezes.

03:02

Então, ele fica no ciclo,

03:04

porque eu não quero que ele fique rodando para sempre

03:08

dentro de um loop que nunca vai acabar.

03:11

Outra coisa, eu posso falar que, por padrão, ele é full autônomo, ou seja,

03:15

Eu não quero que ele fique parando para cada fase que ele terminar.

03:19

Mas, se eu quiser, eu posso pedir para ele, olha, para cada fase, pare ali para ele.

03:24

Para cada fase que ele terminar, um commit por fase ali para ele.

03:29

E depois, para cada key, se eu quiser, eu posso falar para ele, olha,

03:33

você não precisa testar, você não precisa fazer o linter e etc.

03:36

E, caso eu fale para ele, por padrão, ele vai implementar todas as fases,

03:41

mas eu posso falar, olha, implemente a fase 1,

03:44

a fase 2. Então,

03:45

são overrides simples que somente para ele ter ali como

03:49

guia de coisas que eu posso pedir para ser substituído.

03:55

Não que outras informações que eu passe, ele não vai utilizar.

03:59

Então esse aí é um ponto importante aqui para a gente.

04:06

Immutable Core, basicamente a checklist.

04:10

Ela tem que ser sempre traqueada, ali baseado no PRD,

04:14

e agora aqui tem a parte de pre-flight,

04:17

que é o dependency check, então ele vai verificar se as dependências,

04:21

se os grafos de dependência estão todos corretos, ou seja,

04:25

se eu posso desenvolver realmente aquela feature no momento que o software está,

04:30

porque às vezes eu estou tentando desenvolver uma feature que tem

04:33

um outro pré-requisito que não foi feito ainda,

04:35

então ele vai abortar esse tipo de coisa, e aí... a fase de execução, ou seja,

04:40

ele vai seguir o meu plano .md e ele vai dar um skip se isso aqui já foi feito,

04:47

ou se já está comitado,

04:48

baseado no ID, e a implementação, e ele vai implementar.

04:53

E aqui, toda vez que ele fizer uma fail,

04:57

algo que não deu certo ali,

04:59

para ele guardar ali para ele que isso aqui pode ser uma soft fail.

05:05

Abortar, rodar somente quando tem dependências faltando ou quando

05:09

tiver um hard fail que passe o limite.

05:11

Ali ele realmente vai parar de trabalhar. E quando,

05:15

aqui nesse caso, está faltando uma OpenAI API que não está available,

05:20

eu falei para ele assim, olha, você não precisa parar de rodar.

05:25

Isso aqui pode ser um soft fail afetado por teste. Mas você pode,

05:31

por exemplo, terminar a implementação desse serviço caso ele já esteja escrito, tá? Então,

05:35

eu não estou falando nesse caso da chave que

05:37

ele precisa parar porque ele tem testes automatizados.

05:40

Eu pedi para ele continuar de qualquer forma.

05:42

E eu pedi aqui para ele validar, né? Então,

05:45

primeira coisa para ele inspecionar os comandos,

05:47

né? E aqui eu defini para ele o que é hard fail, né? Ou seja,

05:51

quando você não tem ou você não consegue

05:56

fazer algo que realmente vai trabalhar ali para ele.

05:59

O soft fail é quando ele não consegue validar completamente aquilo que ele fez.

06:05

Então, isso aí é um ponto importante para a gente.

06:07

E eu tenho uma fail que é chamada pre-existing failure,

06:10

que é quando uma validação falhou,

06:14

mas não está atribuída ao código que foi mudado ali naquele momento.

06:19

Ou seja, pode ser algo que já existia antes ali para mim.

06:23

E depois eu tenho o commit.

06:25

Estou falando aqui para ele fazer o commit. E nesse caso, pessoal,

06:29

Novamente, por favor, eu estou pedindo o seguinte,

06:33

para ele seguir o padrão dos últimos 10 commits da forma como foi feita.

06:37

Se não tiver nenhum padrão, eu estou pedindo para ele,

06:41

quando ele for criar uma feature, ele coloque o ID da feature. Isso aqui,

06:45

na minha opinião, no dia a dia, não é necessariamente uma boa ideia.

06:50

Porque não faz muito sentido... para nós humanos,

06:55

ou para tracking, etc.,

06:57

saber o ID de uma feature, sendo que não necessariamente esse projeto...

07:04

Imagine que eu tenho várias features de várias implementações

07:07

e eu tenho features com nomes iguais.

07:09

Isso aí pode gerar algum grande problema. Então,

07:12

eu teria que ter uma certeza muito grande de que eu

07:14

sempre vou trabalhar com SDD dessa forma e etc.

07:18

Então, eu não amarraria num projeto em produção ou qualquer coisa.

07:22

Eu não pediria para que ele colocasse...

07:25

absolutamente nada referente à ID de feature ou qualquer coisa baseado num PRD

07:31

ou comentários realizados dentro do seu código baseado

07:35

na feature X que foi colocada.

07:38

Eu estou colocando aqui muito mais para fins didáticos aqui no nosso caso. E aqui,

07:44

para ele fazer a verificação final, rodar a switch para verificar se tem regressões.

07:51

Entrar e navegar ali sobre os componentes, as rotas, os esquemas,

07:56

e fazer um recheck de regressão nos critérios

08:00

de aceitação e verificar um smoke check no ambiente,

08:05

ou seja, ele sobe o ambiente,

08:06

garante que as coisas estão funcionando ali somente para garantir ali.

08:09

E depois ele vai ter o resultado do que ele vai terminar,

08:14

se foi tudo certo, se foi... completado, mas com algumas regressões,

08:19

ou se está incompleto, está faltando isso aqui, que ele não fez,

08:23

ou se ele abortou na fase tal, por conta de alguma coisa.

08:26

E aqui tem o final report,

08:28

que eu coloquei como que ele deve retornar o resultado daquela implementação.

08:33

Se foi o sucesso, quais são as frases,

08:35

qual foi o branch que ele colocou, quais os critérios que passaram,

08:38

quais foram os critérios de integração cross-feature que passaram,

08:42

o que faltou da especificação. Nesse caso que estava colocando,

08:46

quais as regressões que ele achou, quais são os desvios, ou seja,

08:49

ele teve que adaptar porque não estava tão explícito para ele e

08:53

esses desvios podem ir aos poucos mexendo ali com o nosso software, né?

09:00

Problemas pré-existentes,

09:01

o que ele reaplicou daquilo que estava nas instruções iniciais,

09:05

né? E o que ele ignorou e etc.

09:08

E se ele abortou, qual que é a razão, né?

09:10

Então eu coloquei algumas regras aqui no final, somente para você saber, tá?

09:15

Tem algo muito interessante em relação a modelos de

09:18

comportamento é que normalmente no final de uma skill,

09:23

de um prompt ou alguma coisa,

09:24

você pode fazer um resumo do que ele tem que trabalhar.

09:28

Normalmente o modelo sempre vai dar um bias pelas últimas instruções ali.

09:34

Então, normalmente você faz um recap aqui. Ou seja,

09:38

sempre para ele fazer isso e para ele nunca fazer um sucesso.

09:42

Caso ele, por exemplo, arriscou uma regressão. Para ele nunca pular uma verificação.

09:47

Existem algumas coisas bobas, né? Que podem parecer redundantes,

09:53

mas às vezes redundâncias ajudam.

09:55

Como que você vai descobrir essas redundâncias ao longo do tempo?

10:00

Quando você pedir para ele fazer alguma coisa e mesmo pedindo,

10:05

ele ainda está se comportando de forma diferente. Então,

10:09

o que você vai fazer? Você vai lá e vai...

10:12

ser mais redundante ou mais específico ou colocar um important de uma

10:16

forma que chame mais atenção do modelo para ele seguir aquele passo, tá? Então,

10:22

existem alguns pontos aqui de never e always que vale a pena você colocar,

10:27

mas não necessariamente todos esses itens aqui necessariamente eu precisaria.

10:32

Eu já coloquei aqui como padrão,

10:33

como resumo na hora que eu fui fazer esse prompt,

10:35

tá? Expliquei novamente como... que é freeform,

10:38

eu posso passar as instruções. E aqui, edge cases, ou seja, são casos de borda.

10:44

O que acontece caso tal situação que não está prevista ali em cima?

10:50

O que faz? Então,

10:51

se não achar o PRD, aborta. Se não achar o SPEC,

10:55

também aborta. Se não achar as dependências ali, etc.,

10:59

mostra com uma mensagem clara. Então, tudo...

11:02

que ele achar que pode ser inconsistente, ou casos de borda,

11:06

edge cases, eu acabei colocando aqui. Então, basicamente, essa ideia,

11:12

você pode ler com calma aqui esse prompt.

11:14

Normalmente, não é nada perfeito,

11:17

isso aqui foi feito especificamente para a implementação desse curso,

11:22

para falarmos de SDD. E o mais importante é o que eu falo para vocês.

11:29

O importante é que quando você entende essas estruturas,

11:32

você vai ser capaz de criar o seu próprio, tá?

11:35

A coisa mais bacana do mundo é você ter

11:38

orgulho de utilizar aquilo mesmo que você criou,

11:41

porque no momento que a gente tá para trabalhar com a IA,

11:44

cada desenvolvedor tem o seu jeito,

11:48

né? Então, eu não acho que vai ter um framework salvador que vai resolver tudo.

11:53

Eventualmente, tenha para grande parte dos problemas, mas...

11:56

Para as peculiaridades, é super importante que a gente entenda as coisas, tá?

12:01

E cada vez os modelos ficam mais inteligentes e cada vez muitas dessas instruções a

12:05

gente vai ter que ir diminuindo porque senão a

12:08

gente vai acabar limitando o nosso modelo,

12:11

tá? Quando você coloca muita coisa do que ele precisa fazer,

12:14

de como ele tem que fazer,

12:16

mas ele vai deixar de fazer algo que ele

12:19

poderia fazer melhor porque você limitou ele.

12:22

E às vezes você é mais limitado do que seu próprio modelo,

12:26

dependendo do tipo de problema que você vai pedir para ele resolver.

12:29

Fechou? Então, vamos nessa,

12:31

porque no próximo vídeo a gente vai pedir para ele começar as implementações. Vamos nessa.

## Resumo IA

**Abreviações**
*   **AC**: Acceptance Criteria (Critérios de Aceitação)
*   **API**: Application Programming Interface
*   **PRD**: Product Requirements Document
*   **SDD**: Specification-Driven Development

**Resumo**
A aula aborda a construção de uma "skill" ou prompt para um agente de IA especializado em desenvolvimento de software, focando em como ele encontra, processa e atua sobre artefatos de entrada para executar tarefas. O objetivo principal é guiar o agente através de um fluxo de trabalho de desenvolvimento, desde a leitura de especificações até a validação e o relatório final, garantindo clareza, eficiência e rastreabilidade.

O fluxo inicia com a **resolução de inputs**, onde o agente localiza arquivos como `spec.plan.md`, identifica padrões de features, extrai `feature ID` e busca referências explícitas a arquivos `PRD` (tipicamente na pasta `docs`). Essa etapa visa reduzir a ambiguidade e permitir abortar cedo se a especificação for insuficiente. Há uma preferência por instruções explícitas para um parsing mais determinístico.

Em seguida, o agente deve fazer a **leitura integral** do arquivo de plano e da especificação para evitar execuções parciais. O `PRD` é tratado como a fonte principal de critérios de aceitação (`AC`), que podem ser expressos em seções nomeadas, listas ou checklists, alimentando as verificações futuras e funcionando como um contrato de validação. A ausência de critérios explícitos no `PRD` permite a continuidade, mas é registrada como `soft fail`.

A **exploração do codebase** é feita de forma "lazy" (sob demanda), abrindo arquivos apenas quando a fase atual exige, visando economizar tokens e reduzir a dispersão de contexto. Essa abordagem transforma a exploração em uma atividade guiada pelo plano.

A skill permite o uso de **overrides** para modificar o comportamento padrão sem reescrever a estrutura principal. Isso inclui ajustar o número máximo de tentativas (`retries`) antes de um `hard fail`, exigir paradas ou commits ao fim de cada fase, desabilitar testes ou linter, e restringir a execução a fases específicas. A **política de retries** impede que o agente fique preso em ciclos intermináveis, definindo um teto para tentativas de recuperação. O **modo padrão** pode ser totalmente autônomo, mas a skill preserva a opção de impor checkpoints para maior supervisão humana ou execução parcial.

O `PRD` e o plano são tratados como um **contrato**, e a checklist é um "núcleo imutável" a ser rastreado. Antes da implementação, um **pre-flight check** de dependências verifica se a feature pode ser desenvolvida no estado atual do software, abortando se pré-requisitos não foram entregues. A **fase de execução** segue o `plan.md`, permitindo pular itens já implementados ou commitados com base em IDs para evitar retrabalho.

A skill classifica as falhas em: **Hard Fail** (algo essencial para executar ou validar está ausente), **Soft Fail** (implementação pode continuar, mas validação não foi completa) e **Pre-existing Failure** (erro anterior não atribuível à mudança atual). Essa diferenciação melhora o relatório final e a tomada de decisão. Por exemplo, a ausência de uma `OpenAI API key` para testes pode ser tratada como `soft fail` se não impedir a implementação do serviço.

As mensagens de commit podem seguir padrões existentes (últimos 10 commits) ou incluir o `feature ID` (com ressalvas para uso em produção). A **validação final** é abrangente, combinando a execução de suítes de teste, navegação por componentes/rotas/schemas, rechecagem dos critérios de aceitação e um smoke check no ambiente em execução, além de critérios `cross-feature`.

O **final report** padroniza a resposta do agente, informando detalhes como branch, fases executadas, critérios atendidos, integrações validadas, partes não implementadas, regressões, desvios, problemas pré-existentes, instruções reaplicadas/ignoradas e a causa de um aborto. Regras críticas são reforçadas estrategicamente no fim do prompt (`always`/`never`) devido à tendência dos modelos de dar mais peso às instruções recentes. **Casos de borda** (edge cases), como a falta de `PRD` ou dependências, são explicitamente definidos para provocar um aborto claro em vez de suposições frágeis. O instrutor enfatiza que a skill é um modelo adaptável e que, com a evolução dos modelos de IA, muitas instruções podem ser removidas para evitar limitar suas capacidades.

**Pontos de atenção**
*   **Redução de Ambiguidade**: Definir claramente como o agente encontra os artefatos de entrada (`spec.plan.md`, `PRD`) é crucial para evitar ambiguidades e permitir abortar cedo se a especificação estiver incompleta.
*   **Leitura Integral vs. Parcial**: A skill exige a leitura completa dos arquivos de plano e especificação para evitar execuções baseadas em informações incompletas, que podem levar a resultados incorretos.
*   **Economia de Tokens e Contexto**: A exploração "lazy" (sob demanda) do codebase é uma boa prática para minimizar o custo de tokens e evitar a dispersão de contexto ao não ler todo o repositório desnecessariamente.
*   **Controle de Retries**: É essencial definir um número máximo de tentativas (`retries`) para falhas, impedindo que o agente fique preso em ciclos infinitos de correção, o que geraria custos e atrasos.
*   **Supervisão e Checkpoints**: Mesmo em modo autônomo, a possibilidade de impor checkpoints (parar ao fim de cada fase, commit por fase) é importante para manter o controle humano e a rastreabilidade do progresso.
*   **Pré-requisitos e Aborto Precoce**: Realizar um "pre-flight" dependency check é fundamental para evitar iniciar o desenvolvimento de features que dependem de pré-requisitos ainda não entregues, abortando a execução cedo e de forma clara.
*   **Classificação de Falhas**: Distinguir `Hard Fail`, `Soft Fail` e `Pre-existing Failure` é vital para relatórios precisos e para que o agente possa priorizar e reagir adequadamente a diferentes tipos de problemas (ex: uma `OpenAI API key` ausente para testes pode ser `soft fail`, não bloqueando a implementação).
*   **Consistência em Commits**: Embora o uso de `feature ID` em mensagens de commit possa ser útil em alguns contextos (ex: didático), é uma **armadilha** para projetos em produção se não houver um workflow `SDD` rigoroso, pois pode introduzir ruído e dificultar a navegação humana no histórico.
*   **Reforço de Instruções Críticas**: Modelos de linguagem tendem a dar mais peso às instruções mais recentes. Portanto, reforçar regras críticas (`always`/`never`) no final do prompt é uma boa prática para alinhar o comportamento do agente.
*   **Definição Explícita de Casos de Borda (Edge Cases)**: Especificar claramente como o agente deve agir em situações não previstas (ex: falta de `PRD`, `SPEC` ou dependências) evita decisões improvisadas e melhora a previsibilidade e depuração do workflow, reduzindo falsos positivos de sucesso.
*   **Adaptabilidade vs. Template Universal**: O valor principal da skill reside em sua estrutura adaptável, não em ser um template rígido. Entender a lógica por trás do prompt permite que os desenvolvedores personalizem controles e relatórios.
*   **Evitar Microgerenciamento**: Com a evolução dos modelos, é crucial diminuir gradualmente a quantidade de instruções para evitar limitar suas capacidades, permitindo que o agente utilize sua inteligência de forma mais autônoma e eficaz.