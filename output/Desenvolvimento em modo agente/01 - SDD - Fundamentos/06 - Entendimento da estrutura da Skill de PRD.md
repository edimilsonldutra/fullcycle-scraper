Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17770)

## Resumo da aula

O PRD Writer é usado como uma skill especializada para transformar uma intenção de produto em um documento estruturado. Retomando a ideia de skills já estabelecida, o ponto novo aqui é a interface mínima de entrada: descrição do que será desenvolvido, nome do projeto, pasta de destino e caminho completo do arquivo de saída. Essas entradas são suficientes porque a interação principal não depende de um formulário rígido; ela pode começar em linguagem natural. Isso reduz atrito no início e desloca o refinamento para as fases seguintes.

A primeira fase confirma o objetivo informado e inspeciona o ambiente disponível. Isso inclui verificar codebase existente e documentação adicional, porque o PRD pode ser gerado tanto para um projeto novo quanto para um sistema já em andamento. Essa leitura inicial evita que a skill trate o pedido como algo isolado e permite incorporar contexto real do repositório. O efeito prático é diminuir lacunas logo no começo do processo.

A fase de clarificação funciona como uma entrevista iterativa, com uma pergunta por vez. O valor dessa etapa está em expandir a descrição inicial até que features, integrações e processos fiquem explícitos o suficiente para sustentar a especificação. Quanto mais curta ou vaga for a entrada inicial, mais longa tende a ser essa entrevista, porque a IA precisa reduzir ambiguidades antes de escrever. Esse processo também revela perguntas que o próprio autor ainda não havia formulado, o que melhora a qualidade do entendimento do produto.

A entrevista não termina diretamente na geração do documento; antes disso, há um resumo do que foi entendido. Esse resumo funciona como um checkpoint de alinhamento para confirmar se a interpretação está correta ou se ainda precisa de ajustes. A utilidade dele é evitar que a geração formalize premissas erradas cedo demais. Corrigir entendimento nessa etapa custa menos do que revisar uma especificação inteira depois.

A escrita do PRD combina duas fontes: o que foi explicitamente aprendido e o que pode ser inferido a partir do contexto. A regra central é usar informação objetiva sempre que ela existir e recorrer à inferência apenas para preencher lacunas necessárias à coerência do documento. Isso torna a especificação mais completa, mas também cria uma responsabilidade de revisão maior sobre o artefato final. Retomando a noção de especificação como fonte de verdade, aqui ela passa a exigir leitura crítica porque parte do conteúdo foi deduzida, não apenas declarada.

O documento gerado é organizado em nove seções que precisam atravessar o fluxo completo de construção e validação. O ponto relevante não é apenas a divisão formal, mas o fato de que a skill trata essa estrutura como algo verificável. Em vez de produzir texto livre sem controle, ela precisa garantir que cada parte esperada esteja presente e coerente com o restante. Isso aproxima a geração de um pipeline disciplinado, e não de uma simples resposta textual.

Depois de gerar o PRD, a skill executa uma checklist interna para verificar completude, organização e integridade das fases. Essa validação atua como controle de qualidade do próprio artefato antes de salvá-lo. Se os critérios forem atendidos, o fluxo segue para releitura, reverificação e persistência do arquivo no caminho informado. O resultado final inclui um aviso explícito ao usuário sobre onde o documento foi salvo.

Quando a checklist falha, o processo não encerra imediatamente; a skill tenta corrigir o PRD e repetir a validação até três vezes. Esse limite impede loops indefinidos e transforma erro em iteração controlada. Se a validação continuar falhando, o usuário recebe a indicação do problema e o processo volta a depender de intervenção humana. Isso deixa claro que a automação ajuda a elevar a qualidade, mas não elimina a necessidade de supervisão.

A integração entre features aparece aqui como o principal ponto sensível da estrutura do PRD Writer. Retomando a dor já mencionada em SDD, o problema não é apenas listar funcionalidades isoladas, mas capturar como elas se relacionam dentro da especificação. As fases de entrevista, inferência e validação existem em parte para reduzir esse risco de fragmentação. Quando essa integração é mal especificada, o documento pode até parecer completo, mas falha como base para evolução consistente do sistema.

## Transcrição

00:00

Bom pessoal, seguinte,

00:02

Antes de a gente colocar a mão na massa nesse PRD Writer aqui,

00:07

Eu quero mostrar rapidamente para você a estrutura, eu fiz um diagrama simples aqui,

00:12

A estrutura de como que ele funciona, as principais fases dele.

00:16

E depois a gente vai gerar, quando a gente fizer a geração do documento,

00:20

A gente vai olhar mais diagramas e entender algumas nuances desse

00:24

Documento que vão fazer uma diferença gigante da água para o vinho.

00:28

De como que você vai conseguir fazer a integração entre features,

00:32

Que é a grande dor da maioria de todos os frameworks que você pode encontrar de SDD,

00:38

Beleza? Então,

00:39

Vamos lá e entender um pouco o fluxo desse nosso PRD Writer, tá?

00:44

Para a gente, ele vai ser uma skill, ele vai precisar de alguns inputs, tá?

00:49

Qual que vai ser o input? O que eu quero desenvolver, tá?

00:53

Como que vai ser ali o nome do meu projeto, né? Em qual pasta ele vai ser gerado,

01:00

E o caminho com o nome ali do arquivo. Basicamente é isso,

01:05

E eu posso rodar isso de uma forma escrita, com linguagem natural,

01:10

Sem nenhum problema ali para a gente. Então,

01:13

Como que são essas fases que a gente vai passar

01:17

Na hora que a gente for gerar essa especificação?

01:20

A fase 1 vai ser entendimento.

01:22

Primeira coisa, ele vai confirmar com a gente o que a gente...

01:26

Quer desenvolver depois que a gente der entrada.

01:29

Ele vai verificar o nosso codebase para ver se existe mais coisa, se já tem código,

01:35

Se tem mais documentação, para ajudar ele a entender melhor o projeto,

01:40

Porque eu posso gerar esse PRD baseado em um projeto existente também. Então,

01:45

Esse aí é um aspecto importante aqui para você entender.

01:49

Uma vez que a gente passou pela fase 1, a gente vai para a segunda fase.

01:54

E essa segunda fase é uma das fases mais importantes,

01:58

Tá? Porque é uma fase de clarificação, ou seja,

02:01

Vai ser uma entrevista. A Yá vai perguntar para você uma questão de cada vez, tá?

02:08

E a gente vai responder e cada vez mais

02:11

Ela vai tender a ir mais a fundo nos detalhes.

02:15

E você também vai conseguir guiar...

02:20

E ir mais a fundo nos detalhes e você vai conseguir

02:23

Fazer com que ela tenha realmente uma visão geral do projeto.

02:28

A grande sacada que eu vejo aqui é que quando você fala o que você quer desenvolver,

02:34

Esse processo da fase 2,

02:36

Ele vai expandir aquele prompt ou aquela descrição do que você quer fazer.

02:42

Para ele conseguir entender as features, as integrações,

02:45

Os processos e tudo mais. Então,

02:47

Isso aí que é um dos pontos mais importantes.

02:50

Essa entrevista. E, dependendo do projeto,

02:53

Você vai ficar muito tempo nessa entrevista.

02:56

E o porquê que eu estou dizendo? Porque,

02:58

Quanto menor for a entrada do que você quer fazer,

03:04

Mais dúvidas a IA vai querer tirar.

03:09

E o que eu acho mais interessante nesse processo de feedback é

03:13

Que ela vai começar a fazer perguntas que você também não tinha pensado.

03:17

E aí, até chegar num comum acordo, e daí você fala,

03:22

Ok, eu acho que deu bom.

03:24

E ela vai gerar um resumo do que foi entendido ali para a gente,

03:29

para ver se a gente concorda ou se a gente quer fazer ajuste.

03:33

Depois dessa fase 2, o que vai acontecer aqui?

03:38

Ela vai fazer a construção do nosso PRD. Então,

03:43

tem algumas regras de ouro aqui, que é o seguinte,

03:47

usar toda essa entrevista e essas perguntas e

03:52

o que ele utilizou como contexto para inferir,

03:58

para gerar a construção do documento. Ou seja,

04:02

o que ele sabe claramente, de forma objetiva, ele vai utilizar,

04:08

E na hora da geração, se faltar alguma informação ou alguma coisa,

04:14

ele vai inferir e colocar.

04:16

E por isso que se a especificação é o artefato mais importante que você tem,

04:21

eventualmente vai chegar um momento que você vai ter que

04:24

revisar melhor a especificação do que necessariamente o código.

04:27

Mas o ponto aí está que a gente vai ter essa regra de ouro.

04:32

Use o que você aprendeu e infira o que você conseguiu captar. Ali no ambiente.

04:38

E aí, em cima disso,

04:40

ele vai gerar um documento ali pra gente com nove sessões,

04:46

pra que elas vão ter que passar nesse processo.

04:50

Então, como é que vai funcionar uma validação interna na construção desse documento?

04:55

Porque ele vai gerar o documento. Aí, o que ele vai fazer?

04:59

Ele vai rodar uma checklist pra ver se tudo que foi feito... Foi feito,

05:04

se todas as fases estão intactas, se as coisas estão organizadas e estruturadas.

05:09

Se todas essas checagens que ela fez, passaram, o que vai acontecer?

05:16

Vai falar que sim, e a gente vai cair na fase de salvar o documento,

05:21

ler de novo o conteúdo e reverificar,

05:23

e gerar simplesmente um aviso falando onde que

05:28

esse documento foi gerado para o usuário.

05:31

Caso... essa checklist não tenha batido,

05:34

ele vai corrigir o PRD, vai tentar três vezes,

05:38

se não, ele vai falar ali para o usuário, olha, deu ruim, aconteceu isso,

05:43

e você vai continuar iterando no meio do processo. Então,

05:46

essa é a estrutura do PRD que eu criei para a gente fazer isso.

05:52

Mas, como eu disse, isso aqui é muito alto nível.

05:56

Então, eu vou mostrar esse PRD ali funcionando,

06:00

mas depois... eu vou descer para outros diagramas,

06:04

tá? Para que você entenda alguns pontos que, na minha opinião,

06:08

é o grande calcanhar de Aquiles, tá? Que é a parte de integração entre features.

06:13

Mas a gente vai ver isso daqui a pouco, beleza? Então, vamos nessa.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirements Document.
*   **PRD Writer**: Uma skill especializada para transformar a intenção de produto em um documento estruturado.
*   **IA**: Inteligência Artificial.
*   **SDD**: Software Design Document.

**Resumo**
A aula aborda o funcionamento do PRD Writer, uma skill especializada desenvolvida para transformar uma intenção de produto em um Product Requirements Document (PRD) estruturado. O objetivo central é otimizar a criação de especificações, minimizando o atrito inicial através de uma interface simples e garantindo a qualidade e a integração das funcionalidades ao longo do processo.

O PRD Writer inicia com uma entrada mínima: a descrição do que será desenvolvido, o nome do projeto, a pasta de destino e o caminho completo do arquivo de saída. Essas informações podem ser fornecidas em linguagem natural. O fluxo do processo é dividido em várias fases:

1.  **Entendimento**: A primeira fase confirma o objetivo do usuário e inspeciona o ambiente, verificando o codebase e documentação existentes. Isso permite que o PRD seja gerado tanto para projetos novos quanto para sistemas em andamento, incorporando o contexto real e reduzindo lacunas.
2.  **Clarificação**: Esta é uma fase crítica que funciona como uma entrevista iterativa, onde a IA faz perguntas uma por vez. O propósito é expandir a descrição inicial do produto, explicitando features, integrações e processos até que estejam suficientemente detalhados para a especificação. Quanto mais vaga a entrada inicial, mais longa será esta etapa, que também ajuda o usuário a formular perguntas que ainda não havia pensado.
3.  **Resumo de Alinhamento**: Antes da geração do documento, a IA apresenta um resumo do que foi entendido ao usuário. Este checkpoint permite confirmar a interpretação ou solicitar ajustes, evitando que premissas incorretas sejam formalizadas prematuramente no PRD.
4.  **Construção do PRD**: Nesta etapa, o documento é escrito combinando informações explicitamente aprendidas na entrevista e inferências contextuais. A regra é utilizar dados objetivos sempre que disponíveis e recorrer à inferência apenas para preencher lacunas necessárias à coerência. O PRD é estruturado em nove seções, e a skill garante que cada parte esteja presente e coesa.
5.  **Validação Interna**: Após a geração, o PRD Writer executa uma checklist interna para verificar a completude, organização e integridade do artefato.
6.  **Persistência e Feedback**: Se a validação for bem-sucedida, o documento é salvo no caminho indicado, e o usuário recebe um aviso explícito sobre onde o arquivo foi armazenado. Caso a validação falhe, o sistema tenta corrigir o PRD e repetir a validação até três vezes. Se as falhas persistirem, o usuário é notificado sobre o problema, indicando a necessidade de intervenção humana.

**Pontos de atenção**
*   **Redução de Atrito Inicial vs. Refinamento**: A interface mínima e a entrada em linguagem natural reduzem o atrito no início do processo, mas deslocam a complexidade do refinamento para as fases interativas de clarificação com a IA.
*   **Contextualização é Chave**: A inspeção inicial do codebase e da documentação é fundamental para evitar que o pedido seja tratado de forma isolada, garantindo que o PRD reflita o contexto real do projeto e minimize lacunas.
*   **Entrevista Iterativa Aprofunda o Entendimento**: A fase de clarificação, com perguntas sequenciais da IA, é crucial para expandir descrições vagas, detalhar funcionalidades e integrações, e até mesmo revelar pontos que o próprio autor ainda não havia formulado, resultando em um entendimento mais robusto do produto.
*   **Checkpoint de Resumo Evita Erros Caros**: O resumo do entendimento da IA antes da geração do documento é um ponto de alinhamento crítico. Corrigir interpretações erradas nesta fase é significativamente mais barato do que revisar uma especificação completa posteriormente.
*   **Inferencia Exige Revisão Crítica**: Embora a inferência ajude a completar o documento, ela aumenta a responsabilidade do usuário por uma revisão crítica do PRD. Como parte do conteúdo é deduzida (e não declarada explicitamente), o PRD, como "fonte de verdade", exige uma leitura atenta para validar as premissas inferidas.
*   **Estrutura Verificável e Disciplina**: A geração do documento em nove seções verificáveis garante um pipeline disciplinado, em vez de uma resposta textual livre, aproximando a especificação de um artefato controlável e coerente.
*   **Controle de Qualidade Integrado**: A checklist interna após a geração atua como um mecanismo de controle de qualidade do próprio artefato, garantindo sua completude e integridade antes de ser salvo.
*   **Automação Ajuda, mas Não Elimina a Supervisão Humana**: O limite de três tentativas de correção do PRD em caso de falha de validação evita loops indefinidos e demonstra que, embora a automação eleve a qualidade, a supervisão humana continua sendo essencial.
*   **Integração de Features é o "Calcanhar de Aquiles"**: O principal desafio reside em capturar e especificar como as diferentes funcionalidades se relacionam, e não apenas listá-las isoladamente. Uma integração mal especificada no PRD, mesmo que o documento pareça completo, pode comprometer a evolução consistente do sistema. As fases de entrevista, inferência e validação são projetadas para mitigar esse risco de fragmentação.