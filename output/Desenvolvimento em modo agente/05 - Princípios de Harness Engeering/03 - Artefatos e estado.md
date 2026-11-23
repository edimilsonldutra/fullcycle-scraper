Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17887)

## Resumo da aula

Harness Engineering depende de artefatos persistentes para manter o estado do trabalho fora da sessão do agente. Esses artefatos incluem documentos, arquivos e outros dados que registram decisões, progresso e critérios verificáveis. Sem esse suporte, o agente até consegue inferir padrões, mas não consegue reconstruir com segurança decisões de negócio, restrições históricas ou condicionantes de migração. O resultado é perda de continuidade e maior chance de decisões tecnicamente plausíveis, porém erradas para aquele projeto.

Design docs, especificações, planos de execução e ADRs entram como contexto para orientar a execução. Eles não existem apenas para descrever arquitetura; também preservam o motivo de escolhas que não aparecem no código, como dependências de legado ou decisões impostas pelo negócio. Retomando o papel do ambiente já estabelecido, esses artefatos ampliam a capacidade do agente de agir com contexto real, e não apenas com reconhecimento de padrões. Quanto mais o projeto acumula história, mais esse contexto passa a ser determinante.

À medida que o projeto sai de Greenfield para Brownfield, arquivos como CLAUDE.md e AGENTS.md tendem a funcionar melhor como pontos de entrada para o restante da base documental. Em vez de concentrar todas as regras em um único arquivo, eles apontam para pastas, documentos e fontes específicas que o agente consulta sob demanda. Esse uso favorece Progressive Disclosure: o agente lê apenas o que precisa no momento em que precisa. Em projetos grandes, isso é mais sustentável do que tentar condensar todo o conhecimento operacional em um único prompt permanente.

Além das instruções gerais, o projeto precisa de um artefato central que marque o que já foi feito, o que funciona e o que ainda não funciona. Esse registro é o ponto de continuidade entre sessões e entre execuções, porque indica exatamente de onde o trabalho deve prosseguir. O valor principal não está em manter uma lista de tarefas por si só, mas em tornar explícito o estado atual do sistema. A granularidade desse artefato depende do harness e do modelo adotado, desde que o progresso fique legível e acionável.

Esse artefato central não serve apenas para continuidade; ele também funciona como contrato para outros agentes ou para uma fase posterior de avaliação. Quando o estado informa o que foi implementado e o que deveria estar funcionando, um verificador consegue checar se a entrega realmente passou. Isso conecta execução e validação com a mesma fonte de verdade. Sem esse contrato, cada etapa precisa reinterpretar o projeto do zero, o que aumenta ambiguidade e custo.

O estado do projeto precisa ficar no repositório, onde qualquer agente ou sistema possa consultá-lo. Sessões morrem ao fim do processo, então qualquer informação crítica mantida apenas no contexto temporário desaparece junto com a execução. Persistir esse estado em arquivos ou banco local evita que cada nova sessão dependa de memória implícita. Isso reduz o custo de retomada e acelera o onboarding de novos agentes.

O mesmo mecanismo que registra progresso deve indicar se algo passou ou não passou, se está funcionando ou não. Essa marcação transforma o estado em unidade verificável, porque não basta saber que uma tarefa foi tocada; é preciso saber se ela atingiu o critério esperado. Retomando a ideia de unidades verificáveis mencionada no início, o artefato de estado é onde essa verificação ganha forma operacional. Ele permite distinguir trabalho iniciado, trabalho concluído e trabalho validado.

O formato específico é secundário diante da função que o artefato cumpre. Um arquivo Markdown pode ser suficiente em fluxos simples, enquanto SQLite pode atender melhor cenários com consultas, concorrência ou estrutura mais rígida. A escolha depende do harness e do nível de complexidade do projeto, não de uma preferência abstrata por ferramenta. O requisito invariável é existir um ponto de partida persistente, simples de ler e confiável para retomada.

Como a janela de contexto é limitada e novas sessões podem ser iniciadas repetidamente, o agente precisa conseguir entrar no projeto com rapidez. Quando ele encontra documentação de apoio e um estado central claro, entende o que deve fazer e de onde deve continuar sem reconstruir todo o histórico. Isso torna a execução mais previsível e diminui o desperdício de contexto com redescoberta. Em harnesses bem desenhados, a velocidade de onboarding vem da qualidade dos artefatos persistidos.

## Transcrição

00:01

Bom, pessoal, e agora vamos falar de outra categoria aqui que é muito importante,

00:06

que é em relação a artefatos.

00:09

Basicamente, quando a gente está pensando em Harness Engineering,

00:12

a gente tem que pensar como que nós vamos gerar documentos,

00:18

arquivos ou qualquer tipo de dado para que

00:23

a gente consiga manter o estado do nosso projeto.

00:26

E também nós temos unidades verificáveis. Então,

00:30

a primeira coisa que a gente tem que pensar é o seguinte,

00:32

toda vez que vai acontecer um processo de desenvolvimento,

00:36

a gente tem que pensar que nós precisamos ter uma

00:40

forma com que a gente mantenha o estado do projeto.

00:44

Quando o desenvolvimento vai acontecer,

00:47

a gente tem que fazer com que a gente entenda o

00:50

projeto e em qual momento do projeto a gente está.

00:54

Então... Artefatos super importantes, design docs, especificações,

01:00

planos de execução, ADRs e etc.

01:03

Todos esses artefatos vão entrar como contexto para o agente,

01:06

para ele entender o que ele tem que fazer.

01:09

Muita gente fala, a gente não precisa mais de um monte dessas documentações,

01:12

porque o agente consegue fazer ali...

01:16

as buscas, ele é muito rápido, ele entende padrão e tudo mais,

01:20

sim, ele entende padrão, ele é muito inteligente,

01:22

mas o grande ponto é que muitas vezes uma decisão que

01:26

a gente tomou não foi baseada apenas num padrão,

01:29

foi uma decisão às vezes de negócio,

01:31

às vezes foi uma decisão que um sistema legado

01:35

antes que esse cara foi migrado aconteceu,

01:38

quando a gente entende esse tipo de coisa, ele começa a tomar decisões diferentes.

01:43

Outra coisa importante também aí nesse caso é,

01:46

conforme o seu projeto vai evoluindo, ele vai saindo de Greenfield para Brownfield,

01:51

ou se o projeto já existe, tanto o seu Cloud MD, o seu Agents.md,

01:56

eles tendem a ficar quase mais como

01:59

um índice apontando para uma determinada pasta,

02:03

para um determinado arquivo,

02:05

onde o agente pode ir fazendo aquele...

02:11

Progressive Disclosure.

02:13

Basicamente, ele vai lendo conforme ele vai precisando.

02:16

Quando você começa a colocar muita coisa nesses arquivos,

02:20

e o projeto começa a ficar muito grande,

02:23

você não vai conseguir colocar todas as regras do mundo.

02:25

Nesse caso, vai ser muito melhor você ter uma documentação,

02:29

ou principalmente, você pode ter uma skill para conseguir te ajudar nesses aspectos. Então,

02:36

o ponto importante do meio da história é... As instruções,

02:40

sim, elas sempre vão ser lidas ali no CloudMD,

02:42

no Agents.md. Os artefatos,

02:45

eles são importantes para que o agente entenda o projeto. Agora,

02:49

uma das coisas que a gente vai precisar sempre é

02:52

um artefato central de estado marcando o que já foi feito,

02:57

o que está funcionando e o que não está funcionando.

03:00

Isso aí é independente de qualquer coisa,

03:03

Porque é a partir dali que o agente vai continuar o progresso.

03:08

Do que ele está fazendo. Então,

03:11

Sabe aquele arquivinho de tarefas que todo mundo acha que não sei se vale a pena,

03:15

Ou tarefa por tarefa, granular ou não? O ponto não é a tarefa em si,

03:21

É o que já foi feito e o que não foi feito.

03:24

O nível de granularidade disso você vai poder definir baseado no seu Harness,

03:29

Baseado no modelo que você está utilizando.

03:32

Agora, um ponto importante que você vai perceber...

03:35

É que esse artefato central de estado,

03:38

Ele vai se tornar um contrato para que

03:42

Um outro agente ou uma outra fase de avaliação,

03:47

Ele consiga fazer o seu trabalho,

03:50

Que é fazer o que no final das contas?

03:52

Verificar se aquilo realmente está funcionando. Ou seja,

03:56

A ideia é que o estado do projeto seja

03:59

De uma forma extremamente simples e que ele fique...

04:05

No repositório,

04:06

Onde qualquer sistema, qualquer agente que for utilizar vai saber.

04:11

Isso não pode ficar na sessão do agente,

04:13

Porque a sessão do agente vai morrer ali

04:16

Na hora que você acabar o processo de desenvolvimento. Então,

04:21

O que acontece é o seguinte,

04:22

Você tem que ter um mecanismo para marcar se aquilo passou ou se não passou,

04:27

Se está funcionando ou não.

04:29

E esse mesmo mecanismo é uma forma de verificação para realmente...

04:34

Você saber se aquilo ali já está feito ou não. Beleza? Então,

04:39

Isso aqui é quando a gente está falando de

04:42

Artefatos e estrutura como mecanismo de estado.

04:46

Então, independente de como você vai trabalhar,

04:48

Se você vai trabalhar até mesmo com SQLite,

04:51

Hoje em dia tem muita gente que faz isso,

04:52

Ou se você vai trabalhar com arquivo Markdown, não interessa.

04:56

O ponto é que você tem que ter um ponto de partida onde, quando a gente começar,

05:00

Ele saber de onde que ele vai ter que continuar.

05:03

Lembre-se, que o contexto, a janela de contexto é limitada.

05:08

A gente pode querer começar várias vezes novas sessões.

05:13

O agente tem que ter um onboarding muito rápido.

05:16

Então, uma vez que ele lê as documentações,

05:18

Ele sabe o que tem que fazer e ele sabe onde o processo parou,

05:21

Vai ficar muito mais fácil de ele continuar.

## Resumo IA

**Abreviações**
*   **ADR**: Architecture Decision Record
*   **MD**: Markdown (formato de arquivo)

**Resumo**
A aula aborda a importância crítica dos artefatos persistentes na Engenharia de Harness para manter o estado do trabalho fora das sessões temporárias dos agentes. O objetivo principal é garantir continuidade, contexto real e decisões informadas ao longo do ciclo de vida de um projeto, especialmente à medida que ele amadurece de Greenfield para Brownfield.

O instrutor explica que artefatos como design docs, especificações, planos de execução e ADRs fornecem contexto essencial, registrando decisões de negócio, restrições históricas e condicionantes de migração que não são evidentes apenas no código. Sem esse suporte, agentes podem inferir padrões, mas correm o risco de tomar decisões tecnicamente plausíveis, porém inadequadas para o projeto.

É destacado que, em projetos grandes ou já existentes, arquivos como CLAUDE.md e AGENTS.md devem funcionar mais como índices ou pontos de entrada para a base documental, apontando para outros documentos e fontes. Isso permite a "Progressive Disclosure", onde o agente acessa informações sob demanda, o que é mais sustentável do que tentar condensar todo o conhecimento em um único prompt.

Um artefato central de estado é fundamental para marcar o progresso – o que já foi feito, o que funciona e o que ainda não funciona. Este artefato não serve apenas como uma lista de tarefas, mas como um registro explícito do estado atual do sistema, funcionando como um ponto de partida confiável para a retomada do trabalho e um contrato para a validação por outros agentes ou fases de avaliação. A granularidade desse artefato deve ser definida com base no harness e modelo do projeto, desde que seja legível e acionável.

A persistência desse estado no repositório do projeto é um requisito inegociável, pois as sessões dos agentes são efêmeras. Manter informações críticas apenas no contexto temporário da sessão leva à perda de dados e ao aumento do custo de retomada. O formato do artefato (Markdown, SQLite, etc.) é secundário à sua função de ser um ponto de partida persistente, simples de ler e confiável. Artefatos bem desenhados garantem um "onboarding" rápido para os agentes, permitindo que eles compreendam rapidamente o contexto, o que foi feito e o que precisa ser feito, otimizando a execução e minimizando a redescoberta de contexto devido às janelas limitadas de contexto e à natureza de novas sessões.

**Pontos de atenção**
*   **Risco da ausência de artefatos persistentes**: Agentes inferem padrões, mas não conseguem reconstruir decisões de negócio, restrições históricas ou condicionantes de migração sem artefatos. Isso leva à perda de continuidade e decisões erradas para o projeto.
*   **Contexto real vs. reconhecimento de padrões**: Documentos como design docs, ADRs e especificações são cruciais para fornecer o contexto que o código não revela, como dependências de legado ou imposições de negócio. Não se deve subestimar a necessidade dessas documentações.
*   **Evolução da documentação (Greenfield para Brownfield)**: Em projetos maduros, arquivos como CLAUDE.md e AGENTS.md devem funcionar como índices ou pontos de entrada, apontando para uma base documental distribuída, em vez de tentar concentrar todas as regras.
*   **Princípio de Progressive Disclosure**: Favorece a sustentabilidade em projetos grandes, permitindo que o agente leia apenas o que precisa, no momento em que precisa, evitando a sobrecarga de informações.
*   **Artefato central de estado**: É indispensável para marcar o que já foi feito, o que funciona e o que não funciona. Este é o ponto de continuidade entre sessões e execuções.
*   **Estado como contrato de validação**: O artefato de estado serve também como um contrato para outros agentes ou fases de avaliação, permitindo verificar se o que foi implementado atinge os critérios esperados.
*   **Persistência do estado no repositório**: A informação crítica do estado do projeto *deve* residir no repositório, nunca apenas na sessão temporária do agente, que morre ao fim do processo.
*   **Marcação verificável no estado**: O mesmo mecanismo que registra progresso deve indicar se uma tarefa passou ou não passou, transformando o estado em uma unidade verificável e distinguindo trabalho iniciado, concluído e validado.
*   **Função sobre formato**: A escolha do formato para o artefato de estado (Markdown, SQLite, etc.) é secundária. O requisito invariável é que seja um ponto de partida persistente, simples de ler e confiável para retomada.
*   **Rapidez no onboarding do agente**: A qualidade dos artefatos persistidos é determinante para a velocidade com que um agente (ou uma nova sessão) consegue entrar no projeto, reduzir o desperdício de contexto e evitar a redescoberta.