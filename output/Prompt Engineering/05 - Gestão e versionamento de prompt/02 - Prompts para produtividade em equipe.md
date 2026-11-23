Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16699)

## Resumo da aula

O orquestrador atua como agente de governança do workflow, não como executor das análises especializadas. Sua função central é preservar estrutura, caminhos, cobertura e auditabilidade enquanto outros agentes produzem artefatos. Retomando o workflow já estabelecido, ele não decide quais especialistas rodar nem substitui o coordenador; ele mantém o processo íntegro e verificável. Essa distinção reduz sobreposição de responsabilidades e torna o estado do sistema mais confiável.

Responsabilidades core são compromissos inegociáveis do papel, não uma lista procedural de passos. Aqui, elas incluem inicializar o manifesto.md, registrar outputs concluídos, manter convenções de nome e caminho baseadas nos argumentos de execução, comparar a cobertura real com a lista de componentes e finalizar a integridade do manifesto. O valor dessa seção está em delimitar o que o agente deve preservar mesmo quando a execução variar. Isso produz consistência sem transformar o prompt em um roteiro excessivamente rígido.

O manifesto.md concentra o estado persistido do workflow e se torna o único lugar autorizado para registrar o que foi produzido. Quando apenas o orquestrador escreve nesse arquivo, o sistema reduz conflitos de autoria, evita divergência entre agentes e cria uma trilha auditável de artefatos. Cada registro precisa apontar para algo verificável: título, caminho absoluto, agente responsável e timestamp. Sem essa disciplina, a consolidação final passa a depender de memória conversacional ou inferência, o que enfraquece a confiabilidade operacional.

O framework operacional define como o orquestrador trabalha sobre o estado, não como os especialistas executam suas análises. Ele estabelece regras como não inventar diretórios, não criar caminhos alternativos e sempre validar a existência do artefato antes de registrá-lo. Também determina que o manifesto deve refletir cobertura por componente e pendências abertas, permitindo que o coordenador reaja a gaps reais. O resultado é um fluxo em que o estado acompanha a execução em vez de ser reconstruído no final.

Registrar um artefato não é apenas anotar que algo terminou; é vinculá-lo a uma estrutura que permita verificar completude. Retomando o relatório arquitetural já conhecido, a lista de componentes vira referência para o orquestrador acompanhar quais análises existem, quais faltam e quais ainda estão pendentes. Se um componente não tiver relatório correspondente, o orquestrador não resolve isso sozinho: ele sinaliza o gap ao coordenador. Assim, cobertura deixa de ser uma suposição e passa a ser uma condição verificável do workflow.

Prevenir duplicidade é parte do controle de estado, não apenas uma limpeza cosmética no final. O orquestrador precisa validar caminhos e identificar registros repetidos antes de consolidar o manifesto, porque relatórios redundantes distorcem a noção de progresso e poluem a saída final. Esse cuidado é especialmente importante quando há nomes parecidos, múltiplas execuções ou reprocessamento parcial. Um estado confiável precisa distinguir claramente entre ausência, pendência e repetição.

Decision making principles reduzem ambiguidade ao explicitar como o agente deve escolher entre comportamentos possíveis. Separation of concerns impede que o orquestrador assuma despacho de tarefas, preservando a divisão entre quem decide a execução e quem governa o estado. Minimum necessary state limita o manifesto a notas factuais e operacionais, evitando recomendações, sumários ou interpretações que não pertencem a esse papel. Safety over convenience prioriza rejeitar registros duvidosos ou duplicados em vez de aceitar entradas convenientes, porém inseguras.

Em execução paralela, o risco não está apenas em esquecer resultados, mas em corromper o estado compartilhado. O princípio de parallel-safe recording orienta o orquestrador a registrar outputs o mais cedo possível e a tratar o manifesto como recurso sensível, já que múltiplos agentes podem produzir artefatos simultaneamente. Mesmo sem garantias transacionais de banco de dados, a disciplina de escrita centralizada e validação prévia reduz a chance de inconsistência. O objetivo não é eliminar totalmente conflitos, mas tornar o comportamento previsível e recuperável.

O orquestrador se comunica com o coordenador por um protocolo textual explícito, com formato previsível para status, pendências e artefatos registrados. Em vez de conversar diretamente com especialistas, ele devolve ao coordenador listas estruturadas contendo arquivo, caminho absoluto, agente, timestamp e checklist de componentes faltantes. Esse padrão transforma linguagem natural em interface operacional suficientemente estável para coordenação multiagente. Quanto mais regular for essa comunicação, menor a chance de o coordenador disparar ações com contexto incompleto.

A disciplina do manifesto restringe o arquivo ao que interessa para governança: reports, componentes, status, timestamps e notas mínimas. O orquestrador não deve criar novos agentes, prescrever mudanças de código, estimar esforço, redigir sumários executivos nem registrar vulnerabilidades no manifesto. Essas proibições impedem que o agente expanda seu escopo e contamine o estado com conteúdo analítico ou prescritivo. Um manifesto útil é enxuto porque serve para continuidade operacional, não para substituir relatórios especializados.

Um template de manifesto normalmente inclui identificação do projeto, gerador, caminho do orquestrador, lista de reports, componentes monitorados, tasks do workflow, timestamps e status como concluído, pendente ou falho. Essa estrutura permite retomar a execução a partir do ponto correto e saber rapidamente o que já existe de fato. O ganho prático aparece quando o workflow é interrompido: em vez de depender da memória do agente, o sistema consulta um artefato persistido. Quanto mais consistente for esse template, mais fácil fica automatizar validação, síntese e retomada.

Há um custo operacional em registrar estado a cada conclusão individual. Se cada tarefa concluída disparar uma nova execução do orquestrador apenas para atualizar o manifesto, o tracking fica mais próximo do tempo real, mas a latência total aumenta porque há mais ciclos de coordenação e escrita. Se o registro ocorrer apenas ao final de um lote paralelo, o workflow roda mais rápido, porém uma interrupção no meio pode exigir reprocessamento por falta de estado intermediário persistido. A escolha depende do tamanho das tarefas, do custo de reexecução e do nível de tolerância a perda de progresso.

O prompt do orquestrador tende a ser mais simples que o de agentes analíticos porque seu trabalho é governar estado, não interpretar profundamente a codebase. Por isso, uma especificação enxuta com responsabilidades, framework operacional, princípios de decisão e padrões de comunicação costuma ser suficiente. A simplificação não reduz importância; ela reduz ambiguidade em um papel que precisa ser previsível. Em prompts operacionais, menos texto útil costuma produzir mais aderência do que instruções extensas e sobrepostas.

## Transcrição

00:01

E agora, pessoal, a gente chegou nesse último camarada que é o nosso orquestrador, tá? E somente pra deixar muito claro aqui pra vocês, tá? Essas são sessões sugeridas que eu recomendo pra agentes desse tipo. Isso não significa que você não consegue fazer a mesma coisa aqui com essa estrutura ou, eventualmente, com essa. É tudo a forma de como você quer trabalhar.

00:27

Essas estruturas vão te ajudar a não partir do zero e são recomendações, beleza? Então, por conta disso, eu quero trazer agora aqui esse Role Specification, onde a gente deixa claro esses aspectos aqui de definições, responsabilidades, framework operacional, decision making e communication standards. Então, vamos lá, galera. Vamos falar do nosso orquestrador.

00:53

Então, basicamente, eu estou criando um papel, como sempre a gente acaba fazendo isso, dizendo quem ele é. Então, nesse caso, eu estou falando que ele é um agente orquestrador de tarefas que vai ajudar a coordenar um ambiente onde o Cloud Code, nesse caso, que é o Mastercard, vai conseguir controlar agentes e ir fazendo a chamada desses agentes de forma paralela.

01:20

Então, a ideia aqui é que esse agente consiga garantir a estrutura, caminhos e a auditabilidade desse multi-agente work. Ou seja, a ideia desse nosso orquestrador é ele garantir a fonte única da verdade para esse nosso manifesto .md que ele vai criar, para garantir que tudo que for gerado do nosso projeto,

01:47

seja traqueado ali, para daí nós termos certeza de todo o material que foi feito durante a execução, para daí, então, aquele comando gerar o nosso índex com todos os relatórios gerados, tá? Então, responsabilidade core dele. Perceba aqui que eu não estou colocando necessariamente o que ele tem que fazer, tá? Mas sim o senso do que

02:13

são pontos inegociáveis desse camarada. É um pouco diferente de objetivo, porque o objetivo dá uma visão mais a curto prazo, vamos dizer assim, do que vai ser feito. Aqui, na especificação e no papel, a gente já deixa uma ideia do que vai ser feito pelo escopo,

02:34

mas a gente traz algumas responsabilidades que são importantes aqui para ele. Nesse caso é inicializar a estrutura do projeto criando um arquivo de manifesto, registrar todo o output das tarefas que foram completadas e eu dei aqui usando o barra na frente com

03:01

que vai ser utilizado como o nome do relatório com o agente que vai produzir, certo? Garanta que essas políticas e normalizações vão ser baseadas nos argumentos que vão ser passados e que a gente manda lá nos comandos. Garantir que cada componente possa ser comparável com a lista de componentes que vão ser gerados no nosso

03:25

relatório de arquitetura, para garantir que estão todo mundo registrado lá bonitinho, para quando todo o trabalho terminar, ele conseguir sumarizar e a gente ter todos os relatórios que a gente precisa. E também, a ideia é que, como esse cara mantém o tracking de tudo que está sendo registrado, ele vai ajudar a prevenir, validando se há duplicações ou não.

03:48

nesses camaradas. E, no final das contas, também ele vai ter que validar e finalizar o manifesto.md. Então, se você perceber, pessoal, eu consigo, se eu fizer uma força não tão grande, portar essa estrutura

04:08

para algo desse tipo ou para algo desse tipo. Porém, esse camarada aqui, ele não tem uma complexidade tão grande que a gente precisa tanta coisa nele. Então, eu consigo deixar ele um pouco mais leve para não ser, inclusive, um prompt tão grande. E lembrando, quanto maior o prompt, maior a ambiguidade, maior a chance das coisas darem errado, tá? Então, o nosso prompt tem que ser o mais assertivo possível.

04:37

Outro ponto agora aqui é o framework operacional, ou seja, o workflow que ele vai trabalhar. Então, pontos importantes, ponto da verdade. Aqui vai estar o caminho do manifesto e tudo que vai ser armazenado vai ser aqui, por outros agentes vão estar registrados aqui. Somente o orquestrador escreve no manifesto.md. Como é que vai ser gerado os arquivos? A partir de onde? De qual parte isso aqui vai ser gerado? Então, isso aqui para a gente é um ponto super importante.

05:07

Outra coisa importante é, não invente nome de pasta, não crie reports, outputs. Então, a gente está aqui no final das contas garantindo que esse nosso orquestrador, ele só vai trabalhar com o manifesto.md e garantir que tudo que está sendo feito pelos outros agentes, ele vai estar fazendo o double-checking para garantir que

05:27

Quando todo o trabalho terminar, ele vai poder sintetizar tudo, para daí a gente ter o resultado final. Registration Workflow. Quando o Master Coordinator, que é no caso o nosso Cloud, completar um artefato, grave imediatamente isso no manifest.md, com o título, com o caminho absoluto, o nome do agente e o timestamp.

05:50

Antes de gravar isso, verifique se o caminho existe. Componente Average Control. Leia o diretório de arquitetura, o reporte de arquitetura,

06:05

para garantir que todos os componentes fiquem lá no manifesto.md. Importante, grave no manifesto.md de uma forma que eu posso conseguir fazer o tracking de tarefas que estão pendentes para cada componente. Se qualquer componente faltar algum relatório e você verificar esse gap, passe isso para o seu coordenador, que é o cloud, para que daí ele vá, provavelmente,

06:31

chamar outros agentes para terminar aquele relatório. E aqui, a parte de finalizar a integridade. Então, confirme que todas as sessões estão no manifesto.md, valide cada caminho registrado, remova as duplicações. Então, isso aqui são pontos negociáveis que é como ele vai trabalhar. E aqui, eu tenho um decision making principles. É uma forma de eu remover a ambiguidade também. Então, por exemplo, separation of concerns.

07:00

The master coordinator decides which... qual agente deve rodar e quando. O orquestrador apenas enforça a estrutura, a cobertura e o registro. Parallel safe recording. Registrar os outputs S1 o quanto antes para evitar problemas de race conditions, ou seja, porque eu vou ter... eu posso ter vários agentes modificando o mesmo arquivo ao mesmo tempo,

07:27

Então, esse aí é um problema que pode acontecer e a gente não está isento. Isso aqui não é um banco de dados que a gente tem isolamento, mas, de forma geral, eu já percebi que, por exemplo, no comportamento do Cloud, ele percebe quando tem arquivos abertos e ele acaba mudando através de uma diferença ali, ele faz um diff para não...

07:47

ter aquele tipo de problema, tá? Então, eu não tive problema de race condition em relação a isso, tá? State mínimo necessário, ou seja, mantenha as notas operacionais mínimas e factuais para não ter que ficar fazendo recomendação, sumarização, nada disso, ou seja, trabalhe com o menos dado possível. Trabalhe com caminhos determinísticos para garantir certamente onde vão estar os nossos relatórios, né? Safety over convenience, então,

08:15

ele vai refutar, ele não vai registrar qualquer item de um caminho ou qualquer coisa duplicada que ele possa verificar. Então, ele tem que verificar. Então, a grande sacada aqui é que eu vou trazer para ele conceitos que fazem com que eu tenha mais segurança na hora que esse orquestrador vai rodar.

08:39

Tudo isso vai funcionar da melhor forma possível, vai depender muito do modelo que você vai utilizar, vai depender muito do projeto que estiver rodando. Com todos os testes que eu fiz aqui, eu tive ótimos resultados, mas isso não significa que sempre você vai ter o melhor resultado do mundo. Por isso que Prompt é algo evolutivo a cada momento, principalmente quando lançam modelos novos de A.

09:03

E aqui, communication standards. Por que isso aqui é importante? Porque o nosso orquestrador vai falar com o coordenador, então a gente tem que garantir algumas coisas. Ou seja, nunca se comunique diretamente com o agente especialista.

09:18

Sempre traga de forma clara e estruturada as atualizações. Quando for perguntar o status, retorne uma lista de reports com o arquivo, com o título absoluto, com o nome do agente, com o timestamp, e a checklist com os componentes que estão faltando. Aqui, instrução e formato para o Master Coordinator.

09:40

A gente tem que lembrar que o nosso orquestrador vai falar diretamente com o Cloud Code. Então, eu estou querendo gerar para ele uma forma de fazer com que esse orquestrador se comunique de uma forma muito clara para esse cara, porque o Cloud Code é ele que vai executar as outras tarefas e chamar outros agentes. Então, eu estou querendo fazer com que essa comunicação seja muito bem feita. Então, olha...

10:07

a instrução e o formato para o coordenador master. Então, especifique o diretório de saída para o especialista, seguindo o mesmo padrão, ignore qualquer coisa que não seja respeitada. Lembre-se sempre que, quando um especialista finalizar, o resultado tem que ser retornado para o orquestrador para registrar.

10:31

E aqui, Manifesto Discipline. Somente o orquestrador edita e mantém o manifesto limitado a trackear reports com o mínimo workflow, notas e coisas desse tipo. E ações proibidas.

10:47

Ele não vai poder gerar vários agentes, ele não vai gerar sequências de agentes ou vai fazer prescrições de mudanças de código. Ele não vai criar sumário executivo, recomendações, vulnerabilidades ali no manifesto.md.

11:03

Ele não vai estimar horas, não vai trabalhar com linguagens vagas e vai trabalhar da forma mais segura possível. Por que eu estou colocando isso? Porque esse tipo de comunicação, apesar de muitas dessas coisas estarem em outros prompts, aqui eu estou reforçando do que vai ser o comportamento do agente orquestrador.

11:23

Então, se você perceber, é um template, é um prompt muito mais simples, porque ele traz basicamente a responsabilidade, como ele vai trabalhar, que é uma forma simples de manter o tracking de algo, e alguns princípios para tomar decisão em algum momento, ou seja,

11:44

separar as responsabilidades, trabalhar de uma forma segura quando for trabalhar de forma paralela, gravar e sempre mandar as informações com o mínimo possível, trabalhar com os caminhos determinísticos e também...

11:59

não registrar qualquer coisa que viole o que já foi combinado, tá? E as nossas comunicações são importantes porque é como ele fala com o Cloud Code ali de forma geral. Então, essas instruções para o Cloud Code é importante porque aí eles mantém, eles criam uma espécie de um protocolo de comunicação

12:19

É em linguagem natural, vamos dizer assim, mas ainda assim a gente garante que o Cloud Code está recebendo respostas e o orquestrador também está recebendo informações de uma forma mais precisa, baseado nesses standards aí, que você pode ir aprimorando o tempo todo, tá? E aqui eu coloquei um template de como que vai ser um manifesto.template, .md, ou seja, o nome do projeto, o gerador, o caminho do orquestrador,

12:49

Aí eu coloquei os reports, os componentes, por exemplo, e o workflow, tasks, ideas, timestamp para cada report colocado, se já foi completado, se está pendente, se falhou, e anota as mínimas ali do que acontece. Então, com esse tipo de comportamento, a gente já vai conseguir, no final das contas, ter esse arquivo de manifesto, que na realidade é um arquivo apenas para a gente saber de onde a gente parou.

13:17

É o arquivo que mantém o estado do nosso workflow em geral quando eu tenho muitos agentes rodando. Eu poderia ser mais específico, inclusive nos comandos,

13:33

sendo mais enfático que, dentro das regras, terminou um agente iniciar um novo orquestrador para ele somente registrar. E você pode fazer isso, e o Cloud vai criar um orquestrador para cada vez que uma tarefa for concluída. Porém, o que eu percebi ao longo do tempo é que o resultado demora mais, porque ele vai ter que subir um novo orquestrador,

13:59

dá baixa no arquivo e etc. Então, isso acaba demorando um pouco mais. Por outro lado, eu tenho o tracking mais em tempo real, tá? Então, da forma como tá aqui, na maioria das vezes ele vai fazer aqui pra mim o tracking dos dois relatórios primeiros, aí ele vai terminar a fase 3 ali, fazendo o relatório

14:21

de cada componente e vai mudar o manifesto quando ele terminar todos. O grande problema de estado aí é que, se a gente encerrar a sessão no meio desse processo e o orquestrador não tem anotado, a gente vai ter que refazer esse processo como um todo. Então, é um trade-off, no final das contas. Para cada tarefa, gera um orquestrador para ele guardar,

14:45

Vai demorar um pouco mais, mas eu mantenho o tracking, ou ele mantém o tracking quando ele terminar todos aqueles trabalhos em paralelo. Vai depender de como você quer, da forma como tá aqui, ele vai esperar todo...

14:59

todos aqueles em paralelo terminar pra ele sair registrando. Mas vai depender muito do seu comportamento, do tamanho da tarefa, do tempo do projeto. O que eu quero sempre deixar claro, galera, é que prompt é algo infinito, é algo que você testa, gasta muito tempo, gasta muito token pra fazer isso no final das contas,

15:18

Mas é um trabalho que, quando você vê tudo isso funcionando, acaba dando bastante orgulho porque ele acaba realmente matando diversas dores que a gente tem na hora de a gente desenvolver um software ou fazer, por exemplo, relatórios dessa forma como a gente está trabalhando. Beleza? Então...

15:38

Esse aqui é o nosso orquestrador, ele é bem simples, por isso que eu não quis utilizar outras estruturas que acabam sendo um pouquinho mais complexas.

15:56

em uma estrutura que pode ser mais simples nesse caso, por conta do orquestrador. Então, por isso que a gente categorizou dessas formas, mas, vamos dizer assim, a grosso modo, a gente consegue adaptar e você não precisa ficar preso exatamente nisso, da forma como eu coloquei.

16:19

Fechou? Então, era isso, galera, que eu queria passar por essas estruturas de prompts. Elas realmente são importantes e eu espero que você esteja aproveitando. Saiba que você vai ter acesso ao repositório com todos esses prompts para você fazer os seus testes, para você melhorar esses prompts, para você ter uma visão mais crítica e, inclusive, conseguir tirar resultados ainda melhores. Fechou? Um grande abraço e é isso aí.

## Resumo IA

**Abreviações**
- **md**: Markdown.
- **workflow**: fluxo de trabalho.
- **prompt**: instrução textual dada ao agente/modelo.
- **Cloud Code**: ambiente/agente principal mencionado na aula para orquestrar e chamar outros agentes.
- **race conditions**: condição de corrida.

**Resumo**
A aula apresentou o papel do **orquestrador** em um fluxo multiagente, destacando que ele não executa análises especializadas nem decide quais especialistas devem rodar, mas atua como agente de governança do workflow. Seu objetivo é preservar estrutura, caminhos, cobertura e auditabilidade, funcionando como a fonte única da verdade para o arquivo **manifesto.md**, onde ficam persistidos os estados e artefatos do processo.

O instrutor explicou que as **responsabilidades core** do orquestrador são compromissos essenciais do papel: inicializar o manifesto, registrar outputs concluídos, normalizar nomes e caminhos com base nos argumentos de execução, conferir a cobertura dos componentes em relação ao relatório de arquitetura e finalizar a integridade do manifesto. O foco não é listar passos operacionais rígidos, mas delimitar o que o agente deve manter consistente mesmo quando a execução variar.

Também foi detalhado o **framework operacional**, isto é, como o orquestrador trabalha sobre o estado. O manifesto.md é o único local autorizado para escrita, e nele devem ser registrados artefatos com título, caminho absoluto, agente responsável e timestamp. Antes de registrar qualquer item, o orquestrador deve validar se o caminho existe, evitar inventar diretórios ou criar saídas alternativas, e manter o tracking de componentes, incluindo pendências e gaps. Caso algum componente não tenha relatório correspondente, ele deve sinalizar isso ao coordenador master, que no contexto da aula é o Cloud Code.

A aula ainda reforçou **princípios de decisão** para reduzir ambiguidade: separation of concerns, minimum necessary state, safety over convenience e registro paralelo seguro. O orquestrador deve registrar outputs cedo, tratar o manifesto como recurso sensível e rejeitar entradas duvidosas ou duplicadas. Em execução paralela, isso ajuda a evitar inconsistências e problemas de concorrência no estado compartilhado.

Na parte de **communication standards**, foi explicado que o orquestrador se comunica apenas com o coordenador master, nunca diretamente com agentes especialistas. A comunicação deve ser textual, clara e estruturada, retornando listas de reports com arquivo, caminho absoluto, agente, timestamp e checklist de componentes faltantes. Esse padrão cria um protocolo operacional estável para coordenação multiagente.

Por fim, a aula mostrou um template de manifesto com campos como identificação do projeto, gerador, caminho do orquestrador, reports, componentes, tasks, timestamps e status de execução. O instrutor também discutiu o **trade-off** entre registrar o estado a cada conclusão individual, o que aumenta a latência mas melhora o tracking em tempo real, e registrar ao final de lotes paralelos, o que acelera a execução mas pode exigir reprocessamento em caso de interrupção. O prompt do orquestrador foi descrito como mais simples que o de agentes analíticos justamente por governar estado, não por interpretar a codebase.

**Pontos de atenção**
- O orquestrador **não deve executar análises especializadas** nem substituir o coordenador na decisão de quais agentes rodar.
- O arquivo **manifesto.md** deve ser a **única fonte de verdade** e o **único lugar de escrita** do orquestrador.
- Sempre registrar artefatos com dados verificáveis: **título, caminho absoluto, agente e timestamp**.
- **Validar a existência do caminho** antes de gravar qualquer registro.
- **Não inventar nomes de pasta, diretórios, reports ou outputs**.
- Manter no manifesto apenas **estado operacional mínimo e factual**; evitar recomendações, sumários executivos e interpretações.
- Controlar a **cobertura por componente** com base no relatório de arquitetura e sinalizar ao coordenador qualquer **gap**.
- **Prevenir duplicidades**: registros repetidos distorcem o progresso e poluem o estado.
- Em cenários paralelos, considerar risco de **race conditions** e registrar o quanto antes para reduzir inconsistências.
- O orquestrador deve se comunicar **somente com o coordenador master**, nunca diretamente com especialistas.
- Retornar respostas em **formato estruturado e previsível**, especialmente para status, pendências e artefatos registrados.
- O manifesto não deve conter **ações proibidas** como criação de novos agentes, prescrições de mudança de código, vulnerabilidades, estimativas de horas ou linguagens vagas.
- Há um **trade-off** entre tracking em tempo real e velocidade de execução: registrar a cada tarefa aumenta latência; registrar por lote pode exigir reexecução em caso de falha.
- **Prompt mais simples e assertivo** tende a gerar menos ambiguidade; excesso de texto aumenta risco de erro.