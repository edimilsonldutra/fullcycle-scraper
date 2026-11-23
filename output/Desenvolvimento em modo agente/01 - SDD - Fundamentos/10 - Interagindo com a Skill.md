Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17774)

## Resumo da aula

A PRD Writer pode ser invocada como comando em ferramentas que suportam esse formato, como o Claude Code, mas isso não é um requisito da skill em si. O ponto central é fornecer os inputs que ela espera, independentemente de o acionamento ocorrer por sintaxe específica ou por linguagem natural. Essa portabilidade já tinha sido estabelecida anteriormente; o avanço aqui está em observar a interação real: o mesmo artefato funciona em diferentes modelos, com variações apenas de qualidade, latência e custo em tokens.

Em vez de preencher parâmetros formais, os dados necessários podem ser escritos diretamente em um texto curto com contexto suficiente do produto. No exemplo, o prompt informa o nome do projeto, o domínio da aplicação, funcionalidades esperadas e a instrução de saída para salvar o PRD em docs. Isso mostra que a skill consome requisitos sem depender de uma interface rígida, desde que os elementos essenciais estejam explícitos.

A primeira resposta útil da skill é consolidar o entendimento do problema em uma formulação mais estruturada do que o texto original. Essa reescrita funciona como um checkpoint semântico: ela confirma se o modelo entendeu corretamente upload de vídeos, biblioteca, categorias, tags e transcrição sincronizada com navegação por minutagem. Se esse resumo inicial estiver errado, o erro se propaga para o restante da especificação.

Retomando a fase de entendimento já definida anteriormente, a skill não depende apenas do prompt; ela também inspeciona o diretório para descobrir o estado real do projeto. No caso de um projeto Greenfield, ela identifica ausência de código, ausência de documentação prévia e presença de uma pasta docs vazia. Essa leitura do ambiente evita que o PRD assuma artefatos inexistentes ou deixe de aproveitar contexto já disponível.

Depois do entendimento inicial, a skill entra em uma fase de perguntas sequenciais para reduzir ambiguidade antes de escrever o PRD. As perguntas cobrem público-alvo, contexto de uso, tipo de vídeo, restrições de upload, estratégia de transcrição e prioridade de funcionalidades para o MVP. O valor dessa etapa está em transformar uma ideia ampla em decisões especificáveis, sem exigir que tudo esteja perfeito no primeiro prompt.

A entrevista aceita tanto seleção entre alternativas quanto texto livre, e isso muda a ergonomia da interação sem mudar o objetivo da skill. Quando a ferramenta oferece opções como biblioteca privada, uso corporativo ou compartilhamento público, ela acelera a decisão e força recortes de produto. Quando o usuário responde em linguagem natural, como “aulas, reuniões, qualquer tipo de vídeo” ou “2 GB no máximo”, ele adiciona nuance sem sair do fluxo.

Algumas perguntas já começam a converter intenção de produto em decisões técnicas relevantes para a especificação. Escolher Whisper da OpenAI, exigir suporte multi-idioma e pedir detecção automática de idioma são exemplos de requisitos que afetam arquitetura, custo, experiência do usuário e escopo. O mesmo vale para decidir se busca na transcrição entra no MVP ou fica para uma versão posterior.

A qualidade do PRD depende diretamente do quanto o ciclo de perguntas e respostas é levado adiante. Quanto mais o usuário responde, mais granular fica a especificação de comportamentos, limites e prioridades; por isso a entrevista pode se estender por bastante tempo. A skill não está apenas coletando dados: ela está refinando o espaço de solução até que o documento final tenha densidade suficiente para orientar as próximas etapas.

## Transcrição

00:01

Bom, pessoal, então vamos aí colocar o nosso modo de ação no meio da história aqui.

00:07

Então o negócio vai ser o seguinte, eu vou chamar a nossa skill, que é PRD Writer.

00:14

Lembrando que essa skill, o Cloud Code especificamente,

00:17

ele consegue usar a skill como um comando,

00:18

mas eu poderia escrever totalmente em linguagem natural

00:21

pedindo para ele utilizar essa skill.

00:23

E essa skill, de forma geral, ela não tem nada de mais,

00:26

então eu poderia estar usando o Codex, o Gemini,

00:28

isso basicamente é indiferente, obviamente que cada modelo ele vai trabalhar,

00:34

vai gerar uma qualidade diferente, demora mais, demora menos, quantidade de tokens,

00:38

mas eu vou utilizar aqui o Cloud Code, ok?

00:42

E eu criei uma descrição aqui, tá? A básica que eu quero...

00:48

Deixa eu só criar um arquivo bobo aqui pra que você leia a minha descrição.

00:54

Escrevi de cabeça, assim. Que é o meu projeto, é chamado de VideoMax,

00:58

onde é uma plataforma que o usuário pode fazer upload de vídeos,

01:02

e nesse processo ele pode gerenciar seus vídeos,

01:05

acessar e visualizar, ver a transcrição do vídeo,

01:07

podendo clicar na minutagem,

01:09

fazer com que o vídeo seja exibido naquele determinado momento,

01:12

preciso ter gerenciamento de categorias, tags, e eu coloquei aqui,

01:16

use o nome PRD e salve na pasta docs.

01:20

Basicamente, o que eu estou colocando aqui para ele,

01:24

são aqueles requisitos de input que a minha skill estava pedindo.

01:28

Então, eu não preciso ficar necessariamente passando parâmetros aqui. Então,

01:31

eu vou dar um colar aqui para a gente e vamos ver esse cara aqui rodando aqui. Então,

01:38

deixa eu apagar esse arquivo aqui, a .md,

01:41

e vou dar um enter aqui para a gente começar.

01:45

O que ele vai fazer aqui nesse momento,

01:49

no final das contas, é... Ele vai explorar o meu projeto,

01:52

meu projeto praticamente não tem nada, é um Greenfield.

01:54

Então, olha só o que ele fez.

01:57

Entendimento, o VideoMax é uma plataforma web onde

02:00

os usuários fazem upload dos vídeos,

02:02

gerenciam sua biblioteca, incluindo categorias e tags,

02:04

assistem aos vídeos com transcrição sincronizada e podem clicar em qualquer

02:08

trecho da transcrição para pular para aquele momento específico do vídeo.

02:12

Legal? Então, perceba que ele colocou o entendimento, ou seja,

02:15

ele reescreveu um pouco o prompt que eu acabei de colocar.

02:18

Aí ele explorou o diretório e aqui ele trouxe algumas coisas importantes. Contexto do projeto,

02:24

é um novo projeto, Greenfield, sem código,

02:27

documentação ou PRDs existentes. A pasta docs já existe,

02:31

mas ela está vazia. E agora eu vou para a fase 2 de esclarecimento.

02:35

Vou fazer perguntas, uma por vez, e entender profundamente o produto.

02:39

Ele está escrevendo inteiro em português aqui, galera,

02:41

porque a minha descrição foi em português.

02:44

E aqui ele começa aquela história, olha só. Pergunta 1,

02:48

o público-alvo e o contexto de uso. Ele coloca aqui,

02:51

a plataforma é uma plataforma para pessoas individuais,

02:56

cada usuário gerencia a sua própria biblioteca privada de vídeos,

02:59

a plataforma educacional corporativa,

03:01

onde organizações fazem um pilote para seus alunos,

03:04

a plataforma compartilhamento público,

03:06

tipo o YouTube, etc. Eu vou colocar que é a opção A aqui para mim.

03:11

Se você perceber,

03:14

o que acontece aqui é,

03:18

Características dos vídeos. Qual o tipo de vídeo que você imagina? Aula gravada,

03:23

palestra, reunião, videoconferência, tantos minutos, né?

03:26

Videoaulas curtas, variado e tudo mais.

03:29

E eu vou colocar aqui como se fosse aula gravada,

03:32

ou eu posso escrever da forma que eu quiser.

03:34

Eu vou colocar aqui... Posso colocar aulas,

03:39

reuniões, qualquer

03:42

tipo de vídeo, tá? E aqui ele pergunta qual que é o limite de tamanho.

03:47

Eu vou colocar... 2 GB no máximo.

03:53

Então, se você começa a perceber,

03:57

ele vai passar por todo esse processo de entrevista.

04:00

E aqui ele vai começar a cair.

04:02

Como é que você vai gerar a transcrição?

04:04

Vai ser feito automático? Vai utilizar o Whisper da OpenAI?

04:08

Então perceba que ele já começa a fazer algumas perguntas aqui para mim. Então eu vou falar,

04:12

eu vou colocar, vou usar o Whisper,

04:14

eu vou colocar aqui a 1, eu vou colocar o Whisper,

04:19

OpenAI.

04:26

multi -idioma, vou colocar aqui,

04:29

detecção, detecção automática.

04:35

Daí ele está perguntando,

04:36

a busca dentro da transcrição é importante para o

04:39

MVP ou pode ficar para uma versão 2?

04:41

Eu vou falar assim, eu quero busca, quero busca, por exemplo.

04:46

Então, se você perceber, ele vai ficar iterando.

04:48

Se eu for tendo dúvidas, ele vai colocar,

04:50

e eu vou ficar nesse ciclo. aqui, categorias e tags é misto, como é que funciona,

04:55

como é que não funciona isso faz sentido,

04:57

então ele vai ficar nessa iteração ali meio que pra sempre,

05:01

a gente vai ficar se eu continuar respondendo aqui, sei lá,

05:03

meia hora dependendo do nível de granularidade e de

05:06

especificação que eu posso dar pro nosso PRD

05:09

obviamente que eu não vou fazer e ficar aqui na sua frente até o fim fazendo isso,

05:15

então eu vou fechar esse vídeo e vou trazer pra você como é que ficou o

05:19

meu PRD feito no final para que você entenda a estrutura de como tudo isso ficou.

05:25

Beleza? Então vamos nessa.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirements Document
*   **MVP**: Minimum Viable Product
*   **LLMs**: Large Language Models (referência implícita aos modelos como Claude Code, Codex, Gemini)

**Resumo**
A aula demonstra a `PRD Writer` skill, uma ferramenta flexível para gerar documentos de requisitos de produto (PRDs). O objetivo é mostrar a portabilidade da skill, sua capacidade de ser invocada tanto como comando quanto por linguagem natural, e seu processo iterativo para refinar requisitos.

A skill aceita inputs em linguagem natural, sem depender de parâmetros formais, bastando que os requisitos essenciais estejam explícitos no texto. No exemplo, o instrutor fornece o nome do projeto (VideoMax), domínio (plataforma de upload de vídeos), funcionalidades (gerenciamento, visualização, transcrição sincronizada, categorias, tags) e instrução de salvamento.

O fluxo inicia-se com a skill consolidando o entendimento do problema, reescrevendo o prompt inicial em uma formulação mais estruturada. Essa reescrita funciona como um "checkpoint semântico", crucial para confirmar se o modelo compreendeu corretamente os requisitos. Em paralelo, a skill inspeciona o diretório do projeto para entender o contexto (ex: projeto Greenfield, ausência de código/documentação, pasta `docs` vazia), evitando suposições incorretas.

Após essa fase inicial, a skill entra em um ciclo de perguntas sequenciais, projetadas para reduzir ambiguidades e aprofundar o entendimento do produto. Essas perguntas cobrem aspectos como público-alvo, contexto de uso, tipo de vídeo, restrições de upload, estratégia de transcrição (ex: Whisper da OpenAI, suporte multi-idioma) e priorização de funcionalidades para o MVP (ex: busca na transcrição). O usuário pode responder tanto por seleção de alternativas quanto por texto livre, adicionando nuances conforme necessário.

A qualidade e granularidade do PRD final são diretamente proporcionais à profundidade das respostas do usuário durante essa "entrevista" interativa. A skill continua refinando o espaço de solução até que o documento gerado tenha densidade suficiente para orientar as próximas etapas do desenvolvimento.

**Pontos de atenção**
*   **Portabilidade vs. Qualidade**: A `PRD Writer` skill é portátil e funciona com diferentes LLMs (Claude Code, Codex, Gemini), mas a qualidade, latência e custo em tokens variam significativamente entre eles.
*   **Checkpoint Semântico Crítico**: A primeira resposta da skill, que consolida e reescreve o entendimento do problema, é um "checkpoint semântico" vital. Se esse resumo inicial estiver incorreto, o erro se propagará para toda a especificação do PRD.
*   **Contexto do Projeto é Essencial**: A skill inspeciona o diretório do projeto (ex: identificar um projeto Greenfield, ausência de código ou documentação prévia, pasta `docs` vazia) para entender seu estado real. Isso é crucial para evitar que o PRD assuma artefatos inexistentes ou deixe de aproveitar o contexto disponível.
*   **Refinamento Iterativo é a Chave**: A fase de perguntas sequenciais é fundamental para reduzir a ambiguidade de uma ideia inicial e transformá-la em decisões especificáveis. Não é necessário que o primeiro prompt seja perfeito.
*   **Granularidade Depende da Interação**: A qualidade e a densidade do PRD final são diretamente proporcionais ao engajamento do usuário no ciclo de perguntas e respostas. Quanto mais o usuário responde, mais granular e detalhada se torna a especificação.
*   **Decisões Técnicas Diretas**: As perguntas da skill são projetadas para converter intenções de produto em decisões técnicas concretas que impactam a arquitetura, custo, experiência do usuário e escopo do projeto (ex: escolha do modelo de transcrição, suporte multi-idioma, priorização de funcionalidades para o MVP).
*   **Ergonomia da Interação**: Embora a forma de resposta (seleção de alternativas vs. texto livre) mude a ergonomia da interação, o objetivo da skill permanece o mesmo: coletar e refinar requisitos. A seleção pode acelerar decisões, enquanto o texto livre permite adicionar nuances.