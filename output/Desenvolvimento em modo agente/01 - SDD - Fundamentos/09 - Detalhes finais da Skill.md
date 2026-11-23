Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17773)

## Resumo da aula

Core scope é o conjunto de features que sustenta todo o restante da especificação. Retomando a estrutura de skill já definida anteriormente, aqui a novidade é explicitar quais funcionalidades são base e quais entram depois como extensões, evitando que o desenvolvimento trate tudo com a mesma prioridade. Essa separação reduz ambiguidade na implementação e melhora a ordem de execução do trabalho. Quando o core está claro, as demais features passam a ser planejadas como incrementos sobre uma fundação já estabelecida.

A especificação precisa declarar o que acontece quando alguma situação falha, porque comportamento de erro também faz parte do contrato do sistema. Além disso, regras como evitar descrições genéricas forçam a skill a produzir instruções mais operacionais e menos vagas. A seção de out of scope complementa esse controle ao registrar explicitamente o que não pertence à feature. Isso impede que o agente extrapole o escopo e introduza funcionalidades não solicitadas.

Foundation features são as funcionalidades que precisam existir antes de qualquer outra, porque servem de base estrutural para o restante do sistema. Em projetos Greenfield, onde não há código prévio nem funcionalidades existentes, essa identificação se torna crítica: sem uma base mínima, o desenvolvimento paralelo tende a gerar bloqueios e conflitos de integração. A consequência prática é que nem toda feature pode ser iniciada ao mesmo tempo. Primeiro se estabelece a fundação; depois se empilha o restante sobre ela.

A tabela de dependências transforma relações implícitas entre features em uma estrutura visível e verificável. Em vez de assumir que a sequência de implementação será descoberta durante a execução, a skill registra quais partes dependem de quais outras e quais devem vir antes. Isso é especialmente importante quando várias features parecem independentes, mas compartilham pré-requisitos técnicos ou funcionais. A tabela funciona como mecanismo de coordenação entre planejamento e implementação.

Execution Waves agrupam as fases que podem ser executadas em paralelo sem violar dependências já mapeadas. Retomando a ideia de integração entre features, o ponto novo aqui é distinguir paralelismo viável de paralelismo destrutivo. Se duas features dependem da mesma fundação ainda inexistente, colocá-las na mesma wave só antecipa retrabalho. A wave correta nasce da dependência correta, não da vontade de acelerar o cronograma.

O diagrama Mermaid representa graficamente a estrutura de dependências definida pela skill. Ele não substitui a tabela, mas facilita a leitura do fluxo entre foundation features, etapas paralelas e pontos de bloqueio. Em especificações mais densas, o grafo ajuda a detectar encadeamentos ruins, dependências circulares ou excesso de acoplamento entre features. Visualizar a rede de relações torna a revisão mais rápida e menos sujeita a erro interpretativo.

O checklist de validação interna força a IA a revisar a consistência do que acabou de gerar antes de salvar o artefato. Essa validação cobre seções do documento, coerência entre gráfico e dependências, correção das waves e aderência às regras internas da skill. Retomando a autovalidação já mencionada em aulas anteriores, aqui ela aparece aplicada ao fechamento da especificação, não apenas à redação do conteúdo. O objetivo é reduzir falhas estruturais antes que o documento seja usado como base de desenvolvimento.

A fundação do SDD não está em produzir muito texto, mas em produzir uma especificação que organize prioridade, dependência, paralelismo e validação. O valor da skill está em transformar essas decisões em estrutura reutilizável, seja com implementação própria, seja com soluções de terceiros. Entender essa arquitetura interna evita uso superficial da ferramenta e ajuda a reconhecer onde surgem as pegadinhas reais: escopo mal delimitado, integração frágil entre features e ausência de mecanismos de autocorreção.

## Transcrição

00:00

Bom pessoal, voltando e chegando quase que ao final aqui,

00:03

a gente vai ter também na skill,

00:07

vai falar quais são os caras que têm o core scope,

00:11

ou seja, quais são features que a gente vai ter que desenvolver,

00:16

que elas são a base de tudo para que as outras possam ser desenvolvidas, ou seja,

00:21

qual é o core e o que é aquilo que vem depois do core,

00:25

ou seja, são adições ao core da nossa feature.

00:29

Então, esse aí é um ponto importante.

00:32

Outra coisa é como que a gente vai trabalhar com erro durante esse processo.

00:37

Ou seja, o que acontece quando alguma situação falha.

00:41

E aqui tem algumas regras gerais, nunca seja genérico e etc.

00:46

E aqui tem uma seção de out of scope para reforçar para

00:50

o nosso agente na hora de gerar o que não vai estar incluso.

00:57

Dentro dessa feature para ficar mais específico,

01:00

para não ter perigo do agente desviar as nossas features.

01:03

Ele vai gerar uma tabela de dependências e também ele

01:07

vai gerar algo que nessas tabelas que é a foundation features, basicamente, ou seja,

01:13

aquelas features que têm que ser desenvolvidas antes de qualquer coisa.

01:17

Principalmente se o projeto for Greenfield, ou seja,

01:19

o projeto não existe, não tem código nenhum ali. Ou seja,

01:24

ele é um Greenfield, a gente não tem funcionalidades. Então,

01:27

quando acontece esse tipo aqui para a gente,

01:29

a gente tem que ter algumas features base para construir em cima da outra,

01:34

porque senão a gente só vai ter conflito em cima do conflito,

01:37

porque fazer features simultâneas nesse caso vai dar ruim.

01:41

E também nós vamos ter pontos que são execuções, a gente chama Execution Waves,

01:47

ou seja, quais fases a gente consegue fazer em paralelo.

01:50

E também um gráfico, usando um diagrama Mermaid, por exemplo,

01:56

de como é que ficam essas dependências ali no final da história.

02:00

E depois tem um checklist de validação interna, que eu falei para vocês,

02:05

onde ele vai verificar se todas as sessões estão consistentes,

02:08

se a dependência do gráfico está correta, se as waves estão corretas,

02:12

as regras internas para eu fazer com que a IA

02:16

autoavalide o que ela acabou de estar gerando.

02:19

E feito isso...

02:20

ele vai salvar aqui para a gente. Então,

02:23

essa aqui é a ideia da skill, você vai ter acesso a isso,

02:26

vai ler com calma, mas eu queria pelo menos passar isso aqui,

02:29

porque assim, por mais que a gente esteja vendo um monte de texto,

02:33

é exatamente isso que é a foundation do SDD,

02:37

a possibilidade de você gerar especificação.

02:40

Então, o meu objetivo aqui é que você entenda estruturas para que você possa...

02:46

fazer isso ou utilizar isso que eu fiz,

02:49

utilizar de terceiros,

02:50

mas que você tenha aquele entendimento por trás

02:52

das grandes pegadinhas como se autovalidar,

02:56

a integração entre as próprias features e tem um monte

02:59

de detalhes no meio de toda essa história,

03:01

beleza? No próximo vídeo, a gente vai executar essa skill,

03:04

a gente vai começar a ter algumas experiências aqui

03:07

Em relação à entrevista e tudo mais,

03:09

Mas obviamente vai ter um momento onde eu vou dar uma pausa no

03:12

vídeo e a gente já vai entrar com o PRD gerado.

03:15

Porque senão a gente vai ficar uma hora de vídeo somente

03:17

Respondendo perguntas para dar um exemplo do nosso projeto.

03:20

Fechou? Então vamos lá.

## Resumo IA

**Abreviações**
*   **IA**: Inteligência Artificial

**Resumo**
A aula tem como objetivo principal aprofundar a compreensão sobre a estruturação de especificações técnicas para o desenvolvimento de software, focando na organização de prioridades, dependências, paralelismo e validação. O instrutor detalha como a definição de um "core scope" de features fundamentais é crucial para sustentar a especificação, distinguindo-as das extensões e evitando que o desenvolvimento trate tudo com a mesma prioridade, o que reduz a ambiguidade e melhora a execução do trabalho.

Entre os conceitos abordados, destaca-se a necessidade de explicitar o comportamento do sistema em caso de falha, considerando-o parte integrante do contrato. A seção "out of scope" é apresentada como uma ferramenta para registrar o que não pertence à feature, impedindo que o agente de desenvolvimento extrapole o escopo. A identificação das "foundation features" é crítica, especialmente em projetos Greenfield (onde não há código ou funcionalidades pré-existentes), pois estabelecem a base estrutural para o restante do sistema e previnem conflitos de integração.

A aula também explica a importância da "tabela de dependências" para transformar relações implícitas entre features em uma estrutura visível e verificável. As "Execution Waves" são introduzidas para agrupar fases que podem ser executadas em paralelo sem violar dependências mapeadas, diferenciando o paralelismo viável do destrutivo. Para visualização, utiliza-se o "diagrama Mermaid", que representa graficamente a estrutura de dependências, auxiliando na detecção de encadeamentos ruins, dependências circulares ou excesso de acoplamento. O fluxo é complementado por um "checklist de validação interna", uma autovalidação pela IA para garantir a consistência do artefato gerado antes de ser salvo e utilizado como base de desenvolvimento, cobrindo seções, coerência gráfico-dependências, correção das waves e aderência a regras internas.

**Pontos de atenção**
*   **Priorização clara do Core Scope:** Evitar que o desenvolvimento trate todas as features com a mesma prioridade; a separação entre "core scope" e extensões reduz ambiguidade e otimiza a ordem de execução.
*   **Declaração explícita de comportamento de erro:** O que acontece quando uma situação falha deve ser declarado na especificação, pois faz parte do contrato do sistema.
*   **Evitar descrições genéricas:** Regras como "nunca seja genérico" forçam a produção de instruções mais operacionais e menos vagas.
*   **Controle de escopo com "Out of Scope":** Registrar explicitamente o que não pertence à feature impede que o agente extrapole o escopo e introduza funcionalidades não solicitadas.
*   **Criticalidade das Foundation Features em projetos Greenfield:** Em projetos sem código prévio, a falta de uma base mínima leva a bloqueios e conflitos de integração, impedindo o desenvolvimento paralelo. Nem toda feature pode ser iniciada ao mesmo tempo.
*   **Visibilidade das dependências:** A tabela de dependências deve transformar relações implícitas em uma estrutura visível e verificável, em vez de assumir que a sequência de implementação será descoberta durante a execução.
*   **Paralelismo Viável vs. Destrutivo:** As "Execution Waves" devem distinguir paralelismo viável de destrutivo. Colocar features dependentes de uma fundação ainda inexistente na mesma wave só antecipa retrabalho. A wave correta nasce da dependência correta, não da vontade de acelerar o cronograma.
*   **Visualização de dependências:** O diagrama Mermaid é uma ferramenta poderosa para detectar encadeamentos ruins, dependências circulares ou excesso de acoplamento, tornando a revisão mais rápida e menos sujeita a erro interpretativo.
*   **Autovalidação como mecanismo preventivo:** O checklist de validação interna força a revisão da consistência do artefato gerado, cobrindo seções, coerência entre gráfico e dependências, e correção das waves, reduzindo falhas estruturais antes que o documento seja usado.
*   **Valor da estrutura sobre o volume de texto:** A fundação da especificação não está em produzir muito texto, mas em organizar prioridade, dependência, paralelismo e validação de forma eficaz.
*   **Identificação de "pegadinhas reais":** O entendimento da arquitetura interna da skill ajuda a reconhecer armadilhas como escopo mal delimitado, integração frágil entre features e ausência de mecanismos de autocorreção.