Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17880)

## Resumo da aula

User harness é a camada de ambiente construída pelo usuário sobre as capacidades já expostas pelo coding agent e pelos harness de propósito geral. Essa camada inclui artefatos como agents.md, cloud.md, custom hooks, skills, linters e MCP servers, desde que estejam sendo usados para moldar o comportamento do agente no contexto real de desenvolvimento. A ideia central não é redefinir harness, já tratado antes, mas mostrar que parte relevante dele nasce da customização feita por quem usa o sistema. O valor dessa camada está em transformar capacidades genéricas em um ambiente operacional ajustado ao modo de trabalho do time ou do projeto.

Nem todo user harness precisa nascer específico para um único repositório. É comum manter instruções recorrentes no agents.md, scripts reutilizáveis em uma linguagem específica e padrões internos da empresa que aparecem em vários projetos. Esse conjunto forma um harness genérico do usuário: não é o harness universal do agente, mas um kit pessoal ou organizacional de convenções reaproveitáveis. Ele acelera o setup inicial porque reduz a necessidade de reconstruir o ambiente do zero a cada novo contexto.

Com o avanço do projeto, o harness genérico tende a sofrer especializações locais. Retomando o uso de arquivos como cloud.md, uma regra ampla de estrutura de pastas pode deixar de servir quando um módulo exige organização ou comportamento diferente do restante do sistema. Nesse ponto, o harness sofre um fork conceitual: a base continua existindo, mas passa a receber instruções específicas para partes particulares do código. O resultado é um ambiente progressivamente mais aderente ao projeto real do que ao template inicial.

Harness não deve ser tratado como configuração estática congelada no início do trabalho. Como ele contém e controla o ambiente em que o agente opera, qualquer mudança relevante no ambiente pode exigir ajuste correspondente no harness. Isso inclui mudanças na organização do código, nas restrições do projeto e nas formas desejadas de interação com o agente. Um harness útil acompanha a evolução do sistema em vez de tentar impor para sempre a mesma estrutura inicial.

Trocar o modelo sem revisar o harness não é necessariamente um erro, mas introduz risco operacional. Um modelo novo pode interpretar instruções de outra forma, respeitar menos certos limites ou agir com mais iniciativa do que o fluxo anterior tolerava. Como o comportamento do agente emerge da combinação entre modelo e harness, mudar o modelo altera o sistema efetivo, mesmo que os arquivos de configuração permaneçam iguais. Por isso, compatibilidade prática precisa ser validada, não presumida.

Quando o projeto já está estável e há pressão de entrega, a troca imediata para um modelo novo tende a custar produtividade. A abordagem mais segura é manter o fluxo atual no caminho principal e executar testes em paralelo com o novo modelo, observando regressões, desvios de comportamento e mudanças de iniciativa indesejada. Esse cuidado é especialmente importante quando o agente começa a executar ações antes da confirmação esperada ou passa a responder de forma mais ousada. A decisão de migração deve ser guiada por estabilidade operacional, não apenas por novidade tecnológica.

## Transcrição

00:01

Bom, pessoal, o seguinte,

00:02

No vídeo anterior a gente falou sobre harness de propósito geral

00:07

E agora a gente vai falar de outer harness ou user harness. O que isso significa?

00:12

Basicamente, é o ambiente o qual o usuário constrói

00:16

Em cima, utilizando as features que o coding agent expõe.

00:21

Ou seja, quando a gente pega as ferramentas ou aqueles harness de propósito geral,

00:27

A gente consegue...

00:29

Criar coisas em cima dela. Ou seja, eu posso ter o meu agents.md, o meu cloud.md,

00:34

Eu posso ter custom hooks, eu posso ter skills,

00:38

Eu posso ter linters, MCP servers. Ou seja,

00:41

Todo aquele aparato que a gente pode ter em cima na hora

00:46

Que a gente está criando o nosso ambiente para a gente programar,

00:50

Isso aí a gente pode considerar como um user harness.

00:55

Ou seja, é algo que nós criamos. Agora,

00:58

Um ponto importante que a gente tem que se ligar

01:00

É que nós podemos sim ter harness genéricos criados por nós,

01:06

Pelo usuário. Como assim? Olha,

01:08

Existem algumas coisas que são padrão que eu acabo utilizando em todo o projeto. Sei lá,

01:14

Algumas instruções do meu agents.md normalmente eu

01:18

Utilizo para quase todo o projeto.

01:20

Alguns scripts em determinada linguagem eu utilizo para tudo quanto é projeto.

01:25

Ah, eu tenho... um padrão que normalmente a empresa utiliza,

01:29

Então eu vou trabalhar isso nesses meus projetos. Ou seja,

01:33

São coisas que vão me ajudar de forma mais geral,

01:37

Tá? E acabam sendo ferramentas, scripts, muitas vezes MCP servers,

01:42

Hooks, skills e etc, tá? Agora,

01:46

Uma coisa que é importante é que você vai

01:49

Perceber que, conforme o tempo vai passando,

01:51

Você vai pegar esse seu harness,

01:53

Vamos dizer assim, mais genérico,

01:56

E esse harness vai começar aos poucos a

02:00

Se tornar algo mais específico para o projeto.

02:04

Vou dar um exemplo para você. Vamos imaginar que eu tenho um harness e, sei lá,

02:09

No meu cloud.md eu coloco como eu quero uma

02:12

Determinada estrutura de pastas e organização de arquivos.

02:16

Mas eu começo a perceber que, durante aquele projeto, existe um módulo

02:22

Que ele vai ter que trabalhar de uma forma um pouco diferente.

02:25

Então, eu vou sair daquele ponto genérico e eu

02:28

Vou começar a chegar naquele aspecto de aqui. Agora,

02:32

Para esse pedaço do programa,

02:34

Eu quero que você se comporte dessa forma. Ponto. A partir dali,

02:38

A gente começa a ter um fork no nosso harness mais genérico,

02:42

Como se fosse o nosso scaffolding,

02:44

E a gente começa a avançar e, conforme o projeto vai passando,

02:50

A gente vai mudando.

02:52

E quando você vai comparar algo que você começou,

02:55

Sei lá, de uma forma mais genérica,

02:57

E você vai comparar ao longo do projeto,

03:00

Você vai perceber que tudo isso vai se modificando,

03:06

Tudo isso vai se adaptando.

03:08

E quando você vai ver, você vai ter um harness específico para o projeto.

03:12

Agora, novamente, eu coloquei ali um importante,

03:15

Harness não é algo fixo. Ele é todo o ambiente que contém e controla o ambiente.

03:22

Se o ambiente muda, o harness também pode mudar. Esse aí é o grande ponto.

03:28

E o que eu percebo é que muita gente tem um projeto,

03:32

está desenvolvendo, está funcionando super maneiro, de repente muda o modelo.

03:37

E o cara continua trabalhando exatamente com a mesma estrutura. Está errado? Não.

03:43

Mas você vai perceber algumas coisas. Quando você pode trocar o modelo,

03:47

pode ser que as coisas não funcionem. Da mesma forma,

03:51

às vezes pode funcionar até pior por conta de

03:53

limitações ou coisas que você está fazendo. Então,

03:56

uma dica que eu dou para você é, se você está trabalhando, precisa de produtividade,

04:00

você tem que ter uma tarefa que você tem que entregar para amanhã, você tem uma feature,

04:06

você tem sprints e etc. Lançou um modelo novo? Poxa, super bacana você testar. Mas,

04:11

se você tem um projeto que já está estável... que já está funcionando decentemente,

04:16

o que eu super recomendo? Continue com o modelo da forma como você está trabalhando,

04:21

faça os seus testes em paralelo, veja se não tem regressão,

04:25

vê se o modelo não deixa de se comportar da forma como você estava querendo,

04:29

para que isso não afete a sua produtividade e, principalmente,

04:34

para que não gere um desvio muito grande ali no seu projeto,

04:37

porque há uma grande chance de acontecer isso,

04:40

já aconteceu isso comigo e eu acredito que muitas vezes quando troca o modelo

04:45

você acha que aquele modelo ele fica mais ousado, ele sai fazendo coisa antes de

04:49

você confirmar, e todos esses tipos de coisa podem mudar completamente a forma de

04:55

programar. Então, você vai ter que fazer testes

04:57

sempre em paralelo no meio dessas coisas,

05:00

beleza? Então, vamos nessa.

## Resumo IA

**Abreviações**
Não foram mencionadas abreviações com definições explícitas na aula.

**Resumo**
A aula focou no conceito de "User Harness", também chamado de "Outer Harness", que representa a camada de ambiente construída pelo próprio usuário. Essa camada é desenvolvida sobre as capacidades já expostas por um "coding agent" e pelos "harnesses de propósito geral", visando moldar o comportamento do agente para um contexto real de desenvolvimento. O principal objetivo é demonstrar que uma parte relevante do harness nasce da customização feita por quem utiliza o sistema, transformando funcionalidades genéricas em um ambiente operacional ajustado ao modo de trabalho de uma equipe ou projeto específico.

Os artefatos que compõem o user harness incluem arquivos como `agents.md`, `cloud.md`, custom hooks, skills, linters e MCP servers, desde que sejam empregados para personalizar a operação do agente. Inicialmente, é comum desenvolver um "harness genérico do usuário" – um conjunto de instruções recorrentes, scripts reutilizáveis em linguagens específicas e padrões internos da empresa que se aplicam a diversos projetos. Esse harness genérico acelera o setup inicial, pois reduz a necessidade de reconstruir o ambiente do zero.

Com o avanço e especialização do projeto, o harness genérico tende a sofrer adaptações locais. Um exemplo é a personalização de uma regra de estrutura de pastas definida em `cloud.md` para atender às necessidades específicas de um módulo. Nesse ponto, o harness passa por um "fork conceitual", onde a base genérica persiste, mas recebe instruções específicas para partes particulares do código. O fluxo é, portanto, dinâmico: o harness evolui progressivamente, tornando-se mais aderente ao projeto real do que ao seu template inicial, acompanhando mudanças na organização do código, restrições do projeto e formas desejadas de interação com o agente.

**Pontos de atenção**
*   **Harness não é configuração estática:** Ele deve evoluir com o projeto e o ambiente. Mudanças na organização do código, restrições do projeto ou interações desejadas com o agente exigem ajustes correspondentes no harness para manter sua utilidade e relevância.
*   **Risco ao trocar o modelo sem revisar o harness:** Mudar o modelo de IA subjacente sem validar a compatibilidade com o harness existente introduz risco operacional. Um novo modelo pode interpretar instruções de forma diferente, desconsiderar limites ou agir com mais iniciativa, alterando o comportamento efetivo do agente mesmo que o harness permaneça o mesmo. A compatibilidade prática deve ser validada, não presumida.
*   **Estratégia para migração de modelos em projetos estáveis:** Quando há pressão de entrega em um projeto estável, a troca imediata para um novo modelo pode impactar negativamente a produtividade. A boa prática é:
    *   Manter o fluxo de trabalho atual com o modelo existente no caminho principal.
    *   Realizar testes em paralelo com o novo modelo.
    *   Observar cuidadosamente regressões, desvios de comportamento e mudanças de iniciativa indesejadas (como o agente executando ações antes da confirmação esperada ou agindo de forma "ousada").
    *   A decisão de migração deve ser guiada pela estabilidade operacional e pelos resultados dos testes, e não apenas pela novidade tecnológica.