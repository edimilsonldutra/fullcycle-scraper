Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17786)

## Resumo da aula

Avaliar critérios de aceitação com um agente não garante que ele seguirá o método de validação que você imaginou. Quando o prompt pede apenas para verificar se as features 01 e 02 atendem ao PRD, o agente pode interpretar a tarefa como uma auditoria ampla de código, testes e consistência documental. Esse comportamento parece proativo, mas introduz trabalho não solicitado e aumenta o consumo de tokens. Em fluxos com SDD, critério de sucesso sem critério operacional costuma gerar execução divergente.

Retomando o uso de ambientes já vistos, o Codex App executa tarefas muito parecidas com as do Cloud Desktop, mas isso não implica comportamento equivalente. Mesmo com prompt semelhante, cada combinação de ferramenta e modelo tende a priorizar caminhos diferentes, como navegação, leitura de arquivos, inspeção de rotas ou auditoria de testes. Essa variação importa porque altera custo, profundidade da análise e tipo de evidência produzida. Ferramenta de agente não é apenas interface; ela influencia a estratégia de execução.

Quando o agente decide verificar rotas, módulos de autenticação e consistência entre testes e PRD sem instrução explícita, ele está expandindo o escopo da tarefa. Isso é indesejável quando o objetivo era apenas validar critérios de aceitação de forma objetiva. O efeito prático é desperdício de tokens e aumento de tempo de execução em atividades que não agregam valor imediato ao pedido. Proatividade só é útil quando está alinhada com boundaries claros.

Lembra do papel do harness e do guidance operacional nas execuções anteriores: eles existem para reduzir ambiguidade e tornar o comportamento do agente previsível. Aqui fica claro que a ausência desses controles deixa mais espaço para o viés do modelo, e modelos diferentes respondem à mesma instrução com estratégias distintas. Por isso, o harness precisa evoluir junto com o modelo e com a ferramenta usada. Sem esse ajuste contínuo, o processo perde repetibilidade.

O resultado apresentado pelo agente indicou cobertura dos critérios, mas a explicação do método revelou outra coisa: a validação foi feita via Shell, com análise estática de código, testes automatizados e build estático. Isso produz evidência técnica útil, porém não substitui uma validação comportamental no navegador quando o critério depende de fluxo real de interface, redirect ou navegação. Se o requisito envolve algo como lands on /app, a ausência de execução com Playwright limita a confiança no resultado. Método de validação precisa ser compatível com o tipo de critério avaliado.

No caso da feature F02, o agente marcou o atendimento como parcial porque a rota /app não estava implementada. Há redirect, mas não existe destino funcional para completar o fluxo esperado. Isso mostra uma distinção importante: um critério pode parecer encaminhado no código e ainda assim permanecer incompleto no comportamento final. Em aceitação orientada a fluxo, redirect sem landing válida não fecha o requisito.

Se a intenção é validar critérios com Playwright, isso precisa aparecer de forma explícita no guidance. O agente poderia executar esse caminho sem problema, mas não o escolheu porque a instrução não restringia o método. Em sistemas com múltiplas capacidades, omitir a ferramenta desejada equivale a delegar a decisão metodológica ao modelo. Quanto mais importante for a evidência produzida, menos essa escolha deve ficar implícita.

O ambiente do Codex App também oferece um painel para inspecionar diffs, itens staged no Git, skills ativas, terminal e árvore de arquivos. Esse painel não resolve a ambiguidade da execução, mas ajuda a auditar o caminho seguido pelo agente e a revisar o que ele alterou ou analisou. Em tarefas de avaliação, essa visibilidade é útil para distinguir conclusão correta de processo correto. Um agente pode chegar a uma resposta plausível usando um método inadequado para o objetivo.

## Transcrição

00:01

Bom, pessoal, só para vocês saberem, ele está nos critérios de aceitação,

00:05

ele resolveu aquele bug, mas eu não estou preocupado com isso.

00:10

Aqui ele está trazendo o resumo do status final,

00:13

modificações do que ele resolveu em relação ao bug e etc.

00:17

Aí, o que acontece aqui?

00:21

Eu tenho aqui o Codex. O que é o Codex?

00:26

É o Codex App da OpenAI que usa o modelo GPT. Então,

00:33

o que eu estou fazendo? Aqui é uma outra forma,

00:36

um outro ambiente, onde eu posso fazer,

00:39

basicamente, coisas muito parecidas, por exemplo,

00:43

como o Cloud Desktop está fazendo. O que eu acredito,

00:46

sempre ao longo do tempo,

00:47

empresas concorrentes tendem a criar produtos que

00:51

acabam sendo muito parecidos em diversas funcionalidades.

00:55

Então, somente para você saber, eu adicionei aqui o projeto.

01:00

Falei que ele vai rodar local e escolhi o branch que ele vai trabalhar,

01:05

tá? E o que eu vou fazer aqui é o seguinte, né?

01:10

Eu vou chegar e vou falar,

01:12

baseado nos critérios

01:17

de aceitação das

01:21

features

01:24

01 e

01:27

02, tá?

01:31

Ou posso até colocar... as features,

01:34

vou colocar aqui, 01 e

01:39

02, né? Cada um, ele está provavelmente colocando as features 01 e 02 em

01:47

docs e seu

01:50

prd .md,

01:55

verifique se eles estão sendo atendidos.

02:02

Estou dando um enter agora aqui e permissões padrão,

02:07

se ele pedir alguma coisa, beleza.

02:08

Então, eu vou dar um send agora aqui para ele,

02:10

e o que vai começar agora a acontecer é que eu vou

02:15

rodar basicamente a mesma coisa que eu estava fazendo ali no Cloud Desktop, tá?

02:21

No Cloud, no Codex, aqui para a gente.

02:26

E você vai ver, ó, Skill Next.js já foi carregado,

02:30

vou mapear os documentos de critério, os docs,

02:32

ele está lendo, né? Já extraiu as especificações.

02:36

o que atende parcialmente ou não,

02:38

e agora ele vai verificar provavelmente se o ambiente

02:42

está no ar ou alguma coisa desse tipo,

02:44

ele vai seguir. No final das contas,

02:46

como a gente não trouxe nenhuma, vamos dizer,

02:48

nenhum guidance, o que ele tem que fazer especificamente,

02:51

ele vai fazer da forma como ele está trabalhando. Agora, olha só que interessante. Ele falou,

02:57

eu estou começando a auditoria do código das rotas e nos

03:00

módulos de autenticação para verificar cada critério de implementação,

03:03

não só o teste.

03:04

Eu vou buscar também consistência entre os testes que cobrem e que estão no PRD.

03:09

Ou seja, se você olhar aqui, ele está fazendo mais do que eu pedi.

03:16

Entendeu? E isso é ruim, na minha opinião.

03:19

Ele está sendo proativo porque ele está buscando outros problemas.

03:24

O grande ponto daqui é que ele está queimando um monte de

03:27

tokens de algo que eu não queria que ele fizesse.

03:30

Isso provavelmente só está acontecendo por alguns motivos.

03:35

Falta de guidance e harness, de forma geral,

03:38

e mudança de modelo.

03:41

Cada modelo acaba trabalhando ali de uma forma diferente.

03:46

Então as coisas acabam sendo mudadas ali.

03:49

Então, a gente consegue ver ele rodando os comandos,

03:51

a gente consegue ver ele fazendo as coisas,

03:53

mas a grande questão que está por trás

03:56

de tudo isso é como cada agente acaba.

04:01

Cada agente e cada modelo,

04:04

ele tende a enviesar e fazer as coisas de uma

04:08

outra forma de como o outro está fazendo.

04:10

O Cloud, ele não fez.

04:12

Eu pedi para ele validar os critérios de aceitação para navegar ali.

04:17

E o que esse cara fez? Ele está indo de uma forma muito mais profunda.

04:22

Eventualmente, eu não gostaria que ele fizesse isso ali para mim. Então,

04:26

esse aí é um outro ponto que a gente sempre tem que se ligar.

04:30

E por isso que Harness evolui junto com o modelo.

04:35

A gente vai falar isso daqui a um tempo,

04:39

nos próximos capítulos. Mas é interessante a gente ver como é diferente.

04:47

a forma de trabalho de cada um dos caras.

04:51

Ele está muito mais ali mexendo em arquivo necessariamente do que

04:55

tentando fazer esses testes da forma como eu tinha pedido ali. Ok, Wesley,

05:02

eu posso ter pedido um prompt bem sem vergonha.

05:04

O ponto é que eu botei meio que o mesmo prompt

05:06

nos dois e ele está indo bem a fundo nessa parada.

05:14

Pronto, aqui ele diz que ele terminou.

05:17

Por que o F02 impede de ser totalmente testado?

05:21

Porque não existe a rota /app, implementada no app,

05:26

e nesse estado os critérios lands on app,

05:28

né? Ficam parciais, porque há um redirect e não tem.

05:32

Mas basicamente ele falou que ele testou tudo,

05:35

tá? Batendo com o PRD.

05:38

Mas eu vou perguntar assim, como você testou?

05:45

Usando Playwright?

05:47

ou alguma outra ferramenta,

05:50

ou foi apenas

05:53

de forma estática e

06:00

interativa via Shell.

06:06

Vamos lá, vou colocar aqui como que ele fez, somente para você saber, tá?

06:10

Aqui você tem um painel onde eu consigo ver também os diffs de tudo que, basicamente,

06:17

para eu fazer o review, ou seja, do que está on stage no meu Git.

06:21

tem um sumário do que está colocando,

06:23

quais as skills que estão trabalhando e tudo mais. Se eu quiser,

06:28

eu consigo ver o terminal e consigo ver

06:30

a minha tri de arquivos ali para mim.

06:36

Daí ele falou, foi via Shell, sem Playwright. Usei três frentes,

06:40

análise estática de código, testes automatizados e build estático.

06:44

Eu não fiz nada, nenhuma validação com o navegador, com o Playwright. Então,

06:50

eu não quero ficar aqui falando e discutindo,

06:53

então faz com Playwright ou qualquer coisa desse tipo.

06:55

Só estou querendo dizer como que muda o comportamento de um agente para o outro,

07:00

uma ferramenta de uma para a outra.

07:03

Nesse momento, pelo menos na hora que eu estou gravando,

07:05

o Cloud Desktop tem aquele preview onde ele cria aquele arquivo,

07:09

o Codex não tem, mas de forma geral... Cada uma tem uma forma. Obviamente,

07:14

se eu falasse desse guidance, faça todos esses testes,

07:16

esses critérios com Playwright, ele poderia ter feito sem nenhum problema.

07:20

Meu maior ponto aqui é mostrar que

07:22

ferramentas diferentes fazem coisas diferentes também.

## Resumo IA

**Abreviações**

*   **PRD**: Product Requirement Document (Documento de Requisitos de Produto)
*   **SDD**: Software Design Document (Documento de Design de Software)
*   **F01**: Feature 01 (Funcionalidade 01)
*   **F02**: Feature 02 (Funcionalidade 02)
*   **GPT**: Generative Pre-trained Transformer (modelo de linguagem usado pela OpenAI)
*   **Git**: Sistema de controle de versão distribuído

**Resumo**

A aula abordou os desafios e nuances da validação de critérios de aceitação utilizando agentes de IA no contexto de desenvolvimento de software. O objetivo principal foi demonstrar como a ausência de um "guidance" operacional claro e um "harness" adequado pode levar a comportamentos inesperados do agente, resultando em desperdício de recursos e validações imprecisas.

Os conceitos e ferramentas abordados incluíram: o ambiente Codex App (da OpenAI, utilizando um modelo GPT) comparado com o Cloud Desktop, a importância do "harness" e do "guidance" operacional, ferramentas de validação como Playwright (para testes comportamentais de navegador) e Shell (para análise estática de código, testes automatizados e build estático), e documentos como PRD e SDD. Foi discutida a avaliação de "features" específicas (F01 e F02).

O fluxo explicado pelo instrutor envolveu a configuração de um projeto no Codex App e a atribuição de uma tarefa ao agente: verificar se as features F01 e F02 atendem ao PRD. O agente, em vez de focar apenas na validação objetiva dos critérios de aceitação, expandiu o escopo para uma auditoria ampla de código, rotas, módulos de autenticação e consistência entre testes e PRD. Essa proatividade, embora pareça útil, foi destacada como indesejável por aumentar o consumo de tokens e o tempo de execução em atividades não solicitadas. O agente, ao ser questionado sobre o método, revelou que utilizou análise via Shell, sem validação comportamental em navegador (como Playwright), o que é inadequado para critérios que dependem de fluxo de interface real, como "lands on /app" para a F02. A aula concluiu que a explicitação do método e da ferramenta desejada é crucial para garantir a qualidade e a repetibilidade da validação.

**Pontos de atenção**

*   **Escopo expandido e consumo de tokens**: Agentes de IA podem interpretar prompts de forma ampla, realizando auditorias de código, testes e documentação não solicitadas. Esse comportamento proativo, sem boundaries claros, resulta em desperdício de tokens e aumento do tempo de execução.
*   **Necessidade de guidance e harness**: A ausência de instruções operacionais detalhadas (guidance) e mecanismos de controle (harness) permite que o viés do modelo influencie a execução, tornando o comportamento do agente imprevisível e não repetível. O harness deve evoluir junto com o modelo e a ferramenta.
*   **Variabilidade entre ferramentas e modelos**: Diferentes combinações de ferramentas (e.g., Codex App vs. Cloud Desktop) e modelos de IA priorizam caminhos de execução distintos (navegação, leitura de arquivos, inspeção de rotas, auditoria de testes). Essa variação altera custo, profundidade da análise e o tipo de evidência produzida.
*   **Alinhamento do método de validação com o critério**: O método de validação escolhido pelo agente precisa ser compatível com o tipo de critério avaliado. Para requisitos que envolvem fluxo real de interface, redirects ou navegação (e.g., "lands on /app"), uma validação comportamental em navegador (como Playwright) é indispensável, e a análise estática (via Shell) não a substitui.
*   **Diferença entre código e comportamento**: Um critério pode parecer encaminhado no código, mas ainda estar incompleto no comportamento final. Um redirect sem um destino funcional válido, por exemplo, não completa um requisito de "landing" em uma rota específica.
*   **Explicitar a ferramenta desejada**: Em sistemas com múltiplas capacidades, omitir a ferramenta específica para a validação (e.g., Playwright) equivale a delegar a decisão metodológica ao modelo, o que pode levar a um método inadequado para o objetivo e reduzir a confiança no resultado.
*   **Visibilidade para auditoria**: Painéis como o do Codex App, que permitem inspecionar diffs, itens staged, skills ativas, terminal e árvore de arquivos, são úteis para auditar o caminho seguido pelo agente e distinguir uma conclusão correta de um processo correto, especialmente quando um método inadequado é usado.