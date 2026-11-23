Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16622)

## Resumo da aula

Um prompt isolado descreve comportamento; um agente encapsulado transforma esse comportamento em um artefato operacional descobrível pela ferramenta. Retomando o auditor de dependências já definido anteriormente, a novidade aqui é que ele deixa de ser apenas texto colado em uma execução manual e passa a existir como uma unidade registrada, com nome, descrição e regras de ativação. Isso importa porque o sistema consegue decidir quando reutilizar esse especialista sem depender de o usuário reescrever toda a instrução a cada chamada.

Metadados declarativos são campos externos ao prompt interno que registram identidade e condições de uso do agente. Nesse caso, o arquivo do agente inclui informações como nome, descrição, modelo e atributos visuais, formando uma camada de registro que a ferramenta consulta antes da execução. Essa separação permite manter o comportamento técnico do auditor dentro do prompt e, ao mesmo tempo, expor ao sistema quando e por que ele deve ser selecionado.

A descrição do agente funciona como um contrato semântico de descoberta. Em vez de instruir detalhadamente como auditar dependências — algo que já está no prompt interno — ela informa em quais tipos de problema esse agente é especialista, como análise de saúde, segurança e status de dependências. Uma descrição bem escrita reduz ambiguidade na seleção do agente, porque aproxima a intenção do usuário das capacidades registradas no artefato.

Um subagente é um agente especializado que pode ser chamado por outro agente mais geral durante a execução. No cenário mostrado, o agente principal de codificação delega a auditoria para o Dependency Auditor quando detecta uma necessidade compatível com esse domínio. Essa divisão melhora previsibilidade, porque cada agente opera com escopo mais estreito e produz saídas mais consistentes do que um agente genérico tentando resolver tudo sozinho.

A invocação contextual acontece quando o sistema escolhe um agente com base no pedido atual, e não por chamada rígida e explícita em todos os casos. O mecanismo observa o contexto da solicitação, compara com os metadados e decide se aquele especialista deve entrar no fluxo. Isso é especialmente útil em workflows, porque o usuário pode pedir uma verificação em linguagem natural e ainda assim acionar o agente correto.

Exemplos de trigger são amostras de situações que ensinam ao sistema quando o agente deve ser ativado. Eles não servem para executar a tarefa em si, mas para mapear padrões de contexto, pedido do usuário e resposta esperada de encaminhamento. Quando a ativação falha, um dos primeiros pontos a revisar é se os exemplos realmente representam as formas reais pelas quais o usuário pede aquela análise.

O XML aparece nos exemplos como uma estrutura explícita para separar contexto, fala do usuário, resposta do assistente e comentários de roteamento. Essa organização torna o padrão de ativação mais legível para a ferramenta, porque cada parte da interação fica marcada por tags ou blocos semanticamente distintos. O valor do XML aqui não está no formato em si, mas na clareza estrutural que ele oferece para descrever gatilhos de uso.

O prompt continua existindo mesmo quando o agente ganha uma camada declarativa externa. A diferença é que agora ele passa a conviver com metadados operacionais que orientam descoberta, seleção e execução dentro da ferramenta. Retomando a estrutura do auditor já conhecida, inputs, outputs e workflow permanecem no núcleo do agente; o que muda é que esse núcleo agora pode ser encontrado e acionado automaticamente.

O fluxo prático tem duas camadas. Primeiro, registra-se o agente em um arquivo declarativo com nome, descrição, exemplos de uso e demais metadados; depois, abaixo dessa camada, mantém-se o prompt interno especializado que já define comportamento, entradas e formato de saída. Quando o usuário faz um pedido como “verifique se nossas dependências estão atualizadas e seguras antes de um major release”, a ferramenta compara esse pedido com os exemplos de trigger, identifica aderência ao Dependency Auditor e delega a execução ao subagente.

Se o agente não for acionado quando deveria, o problema nem sempre está no prompt interno; muitas vezes está na camada de descoberta. A correção consiste em revisar a formulação da chamada real e adicioná-la como exemplo de trigger, aproximando o registro declarativo da linguagem que os usuários realmente usam. Esse ajuste reduz falsos negativos de ativação e torna o workflow mais confiável sem alterar a lógica central da auditoria.

## Transcrição

00:01

Bom, pessoal, seguinte, tô aqui com a minha ideia aberta. Esse aqui é o projeto que tem um monte de dependência desatualizada, faz um bom tempo que eu criei, é um projeto exemplo que eu faço, então não é nada que esteja em produção, mas é legal pegar esses projetos principalmente porque passa tempo se ele começa a utilizar versões antigas e coisas desse tipo, tá?

00:24

Aqui, que você está vendo, é o report que ele acabou gerando, que eu mostrei para vocês no nosso último vídeo. Agora, o que acontece aqui, que é interessante, é o seguinte... Na hora de rodar, eu pedi para ele gerar um nome do arquivo aqui como libreport. Agora, tem algo importante aqui para você entender. O negócio é o seguinte...

00:51

Apesar disso ser um prompt, ou seja, aquele prompt que eu acabei de mostrar para você, eu resolvi, nesse caso, e aqui a gente está falando de ferramenta, tá? A gente está falando de prompt, mas em ferramenta que utiliza esse prompt. Não necessariamente, sei lá, dependendo de quando você está assistindo esse vídeo, essa ferramenta, por exemplo, do Cloud CLI, ela vai estar exatamente nesse padrão que dê para você utilizar exatamente dessa forma.

01:19

mas o importante é você entender a ideia de como a gente está trabalhando em relação ao aqui o prompt, tá? Por que eu estou dizendo isso? Porque quando eu clico aqui, ó, run Cloud Code, ou seja, eu tenho o Cloud Code instalado aqui no meu computador, tá? O que acontece aqui? Ele tem um recurso chamado de agents, tá? Ou de agentes. E você pode criar novos agentes com esse recurso. Então, se eu colocar aqui, ó, barra,

01:45

Agents, ele pode trazer aqui para mim para eu criar um novo agente, ou eu tenho outros agentes que eu já tenho aqui na minha máquina. Então, se eu dou um criar novo agente, ele vai criar, ele vai passar um passo a passo, você depois pode brincar em relação a isso. Mas o porquê que eu estou falando desse cara de como criar agente? Porque é o seguinte, o Cloud Code é um agente de codificação.

02:15

Certo? Ou seja, ele é um cara que faz o que a gente manda baseado num prompt que a gente acaba colocando aqui. A grande questão em relação a isso, ao Cloud Code, é que ele tem esse recurso de agentes que faz com que, de acordo com o que você peça na hora que você está desenvolvendo, ele vai olhar a lista de agentes que ele tem e, baseado nessa lista, ele pode

02:41

chamar um agente especialista em algo para fazer isso ou fazer aquilo. Então, por isso que eu deixo esse meu prompt feito no formato de subagente, porque toda hora que eu peço para ele fazer uma verificação, alguma auditoria, eu sei que ele vai chamar esse agente, e esse agente vai gerar o report exatamente da forma como eu estou querendo, tá? Mas,

03:01

Tem algo interessante aqui que eu preciso mostrar para você, mas que o próprio Cloud Code gerou, e eu apenas complementei com algumas coisas. A legibilidade é um pouco ruim, mas eu vou mostrar aqui para vocês. Eu tenho uma pasta aqui chamada .cloud. Dentro da pasta .cloud, eu tenho uma pasta Agents, e se você olhar aqui, eu tenho um agente de auditoria, um Auditor Agent. E nesse cara aqui, deixa eu esconder, deixa eu aumentar a minha fonte, tá?

03:31

Se você olhar aqui, vou tentar deixar o maior possível pra você ver, ele tem aqui três tracinhos que ele utiliza como metadado. E o que ele coloca nesse metadado? O nome do agente.

03:46

então é Dependency Auditor, e aqui ele traz uma description do agente aqui pra mim, ou seja, use-se agente quando você precisa analisar ou auditar a saúde, a segurança, o status das dependências de um software e tudo mais. Grande parte dessa descrição é

04:05

ele criou na hora que eu falei o que eu queria de acordo com o que eu queria dos objetivos no agente naquele assistente dele, tá? Então, eu simplesmente dei algumas modificadas, mas aqui tem alguns pontos que eu só queria confirmar e dar essa ciência pra você. Tem muito mais a ver com o Cloud do que necessariamente o Prompt em si, óbvio que tem Prompt no meio,

04:29

mas somente para você entender como que esse agente sabe que ele vai ser invocado. Então, ele dá exemplos aqui de quando esse agente tem que ser utilizado. E uma coisa interessante é, normalmente, a Antropic, que é a que cria o cloud e essas ferramentas, ela usa muito o XML. Então, se você olhar aqui, olha os exemplos como ela trouxe para deixar mais claro como

04:56

que fica mais simples daí a entender. Então, ele trouxe aqui exemplos entre a XML, onde ele traz o contexto. Legal? Então, perceba, ele tem aqui... Vou até pular a linha. Contexto. Vou colocar um tracinho só para a gente ver melhor. Depois, ele traz user aqui para mim. Legal? Depois que ele trouxe isso, ele traz assistant.

05:23

Beleza? E depois do Assistant, aqui que ele colocou aqui pra mim, ele coloca aqui dentro ainda comentário. Legal?

05:39

e depois disso, ele fecha o exemplo dele começando um outro cara. Por que ele está trabalhando desse tipo? Porque aqui, nesse caso, a ideia do prompt dele, e novamente é tudo uma questão de prompt, aqui é uma forma de como ele estruturou esse prompt. Então, ele fala o seguinte, olha, já que isso aqui é um agente e ele vai ser usado para isso, como que pode ser algum exemplo de alguma chamada

06:08

e faça com que esse agente seja chamado. Então, ele traz um contexto. O usuário quer entender o estado atual das dependências do projeto dele antes de um major release, ou seja, antes de ele botar algo grande em produção. Esse é um contexto. E daí, ele tem aqui o usuário falando assim para ele. Você pode verificar as nossas dependências, se elas estão atualizadas e seguras?

06:35

E aí, o assistente vai falar o que para ele? Ah, eu vou usar o Dependency Auditor Agent para analisar as dependências do projeto e prover uma forma compreensiva de um repositório, de um report, um relatório de auditoria.

06:52

Então, aqui, ele está simulando como poderia ser a conversa da IA com o usuário e o contexto. E aqui, ele coloca, entre XML novamente, um comentário. Olha só que interessante!

07:09

desde que o usuário esteja perguntando sobre análise de dependências, use o Dependency Auditor Agent para revisar a saúde dos pacotes, segurança e etc. Ou seja, aqui ele está simplesmente confirmando ou gerando, pelo fato disso aqui,

07:32

está acontecendo, você vai fazer isso aqui. Basicamente é isso. Então, ele traz o tempo inteiro um monte de exemplos desse tipo, para que isso seja usado como trigger, no final das contas, quando o agente precisar, quando o agente sentir que ele tem que ser chamado. Ou seja, a IA vai ter um agente como se ele fosse uma espécie de uma ferramenta,

07:57

E, uma vez que ele tem ali uma espécie de uma ferramenta com ele, ele vai saber em qual momento esse agente vai ser útil. E, por isso, esses exemplos aqui são tão importantes para que o Cloud saiba quando chamar esse nosso agente que a gente criou. Então, nesse caso, se você estiver utilizando o Cloud para criar algum agente ou qualquer coisa similar, e você precisar desses exemplos,

08:23

e você estiver fazendo uma chamada e mesmo assim ele não está ativando a gente, tente verificar como você fez essa chamada e coloque essa chamada como um exemplo para isso poder te ajudar, tá? Então, embaixo disso ele coloca como metadados o modelo que eu quero usar e a cor que vai aparecer ali no modelo e acabou os meus metadados aqui no final das contas, tá?

08:50

Agora, olha só que interessante, embaixo disso é tudo que eu já tinha te mostrado antes. Inputs, outputs, foi o que eu mostrei naquele documento no vídeo anterior. Então, aqui tem todo o nosso workflow e aqui tem todo esse prompt que a gente colocou, lembrando que mesmo utilizando esses metadados e toda essa parte aqui do cloud,

09:15

perceba ainda que ele tem uma estrutura de prompt aqui pra gente, tá? Então, é importantíssimo você conseguir entender que, até mesmo com metadados, a gente tem esses conceitos de prompt, beleza? Próximo vídeo...

09:33

Eu vou trazer algo bem simples para você de como você fazer um trigger direto desse agente usando um prompt simples, mas também para evitar redundância e também evitar que ele faça coisa que não deveria fazer. Então, vamos ver isso no nosso próximo vídeo.

## Resumo IA

**Abreviações**
- **CLI** — *Command Line Interface* (interface de linha de comando)
- **XML** — *eXtensible Markup Language* (linguagem de marcação extensível)
- **IA** — Inteligência Artificial

**Resumo**
A aula explicou como transformar um prompt isolado em um agente encapsulado e operacional dentro da ferramenta, no caso o Cloud Code. O instrutor retomou o exemplo de um auditor de dependências para mostrar que, em vez de manter a instrução apenas como texto reutilizado manualmente, ela passa a existir como um artefato registrado, com nome, descrição, modelo, cor e demais metadados que ajudam a ferramenta a descobri-lo e acioná-lo automaticamente.

Foi destacada a separação entre a camada declarativa de registro e o prompt interno do agente. Os metadados, armazenados em um arquivo dentro de `.cloud/Agents`, funcionam como identidade e critério de seleção: informam quando o agente deve ser usado e em qual tipo de problema ele é especialista. A descrição, nesse contexto, atua como um contrato semântico de descoberta, aproximando a intenção do usuário da capacidade do agente, sem repetir todo o passo a passo da auditoria.

O instrutor mostrou que o Cloud Code pode chamar subagentes especializados durante a execução, delegando tarefas quando o contexto se encaixa no domínio daquele agente. No exemplo, o agente principal de codificação pode acionar o **Dependency Auditor** para analisar saúde, segurança e status das dependências antes de um *major release*. Isso torna o fluxo mais previsível e consistente, pois cada agente trabalha com escopo mais restrito.

Outro ponto importante foi o uso de exemplos de trigger para ensinar o sistema a reconhecer quando o agente deve ser ativado. Esses exemplos simulam contexto, fala do usuário, resposta do assistente e comentários de roteamento, frequentemente estruturados em XML para aumentar a clareza. O instrutor reforçou que o valor do XML está na organização explícita das partes da interação, o que facilita ao sistema identificar padrões de uso.

Por fim, foi explicado que, se o agente não estiver sendo acionado corretamente, o problema pode estar na camada de descoberta e não no prompt interno. A recomendação é revisar a forma real como o usuário faz a solicitação e transformar essa formulação em um novo exemplo de trigger, reduzindo falsos negativos de ativação. Assim, o workflow fica mais confiável sem necessidade de alterar a lógica principal da auditoria.

**Pontos de atenção**
- O agente não é apenas um prompt; ele precisa estar encapsulado como artefato descobrível pela ferramenta.
- A camada de metadados é decisiva para a seleção automática do agente; não basta ter um prompt bem escrito.
- A descrição do agente deve ser clara e sem ambiguidade, pois ela orienta quando o sistema deve acioná-lo.
- Exemplos de trigger são essenciais para ensinar o momento correto de ativação; se forem mal escritos, o agente pode não ser chamado.
- Se a ativação falhar, revise primeiro a linguagem real do usuário e adicione essa formulação como exemplo.
- O uso de XML nos exemplos não é obrigatório por si só, mas ajuda a estruturar contexto, usuário, assistente e comentários de forma legível.
- Mesmo com metadados e automação, o prompt interno continua existindo e precisa manter a lógica de entradas, saídas e workflow.
- Separar tarefas em subagentes especializados aumenta previsibilidade e consistência em comparação com um agente genérico tentando resolver tudo.
- A seleção automática depende do alinhamento entre intenção do usuário, descrição do agente e exemplos de uso registrados.