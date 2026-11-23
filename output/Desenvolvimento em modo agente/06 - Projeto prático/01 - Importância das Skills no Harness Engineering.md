Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17964)

## Resumo da aula

Skills transformam decisões técnicas implícitas do projeto em instruções explícitas para o agente. Isso importa porque, em um ambiente com arquitetura definida, stack escolhida, bibliotecas padronizadas e convenções de organização, deixar tudo subentendido força o agente a inferir demais. Quanto maior a inferência, maior a chance de gerar código fora do padrão, quebrar limites arquiteturais ou adotar soluções que o time não queria. A função central da Skill é reduzir esse espaço de ambiguidade e tornar o comportamento esperado mais previsível.

Documentação tradicional costuma ser escrita principalmente para pessoas, enquanto a Skill é estruturada para orientar a atuação do agente. Por isso, ela precisa ser operacional: deve indicar como agir, quais padrões seguir, quais arquivos consultar, quais scripts executar e quais decisões respeitar durante a implementação. Ela também pode incluir exemplos de referência, porque agentes tendem a produzir resultados mais consistentes quando conseguem comparar a tarefa atual com artefatos reais do projeto.

Dentro do Harness, a Skill funciona como uma camada que organiza o contexto de execução do agente. Ela não substitui gates, testes ou avaliações, mas complementa esses mecanismos ao fornecer direção antes e durante a geração de código. Em vez de depender apenas de instruções soltas na conversa, o agente passa a operar em um ambiente que comunica as regras do projeto de forma contínua. Isso melhora consistência e reduz desalinhamento ao longo da evolução do software.

Uma Skill completa precisa explicitar os padrões arquiteturais do projeto. Entram aqui decisões como modelo adotado, camadas existentes, comportamento esperado das dependências, localização dos módulos, limites que não podem ser violados e padrões que precisam ser preservados. Esse bloco impede que o agente misture responsabilidades ou atravesse fronteiras arquiteturais sem perceber. O resultado é uma implementação mais alinhada com a estrutura real do sistema.

Além da arquitetura, a Skill deve definir o jeito esperado de escrever código naquele repositório. Isso inclui nomenclatura, organização de arquivos, formato de artefatos, responsabilidade de cada tipo de componente, padrões de validação, tratamento de erro, testes e convenções complementares. Esse conjunto reduz variação desnecessária entre implementações e aumenta a consistência do código produzido. Em projetos com múltiplos agentes ou múltiplas interações, essa padronização se torna ainda mais importante.

Instruções abstratas nem sempre bastam para orientar geração de código com precisão. Quando o agente precisa criar uma entidade, um caso de uso, um handler, um repositório, um DTO ou um teste, exemplos reais do próprio projeto funcionam como referência concreta de forma, estrutura e responsabilidade. Isso reduz a chance de interpretações erradas das regras e aproxima a saída gerada do estilo já consolidado no código-base. O exemplo não substitui a regra, mas torna a regra aplicável.

A Skill também pode incorporar scripts usados como parte do Harness, como validações arquiteturais, linters, type check, testes, análise de dependência e detecção de código morto. Esses mecanismos convertem parte das decisões do projeto em verificações executáveis, o que reduz dependência de julgamento informal. Em vez de confiar apenas na probabilidade de o agente seguir corretamente as regras, o processo passa a ter checagens determinísticas. Isso fecha o ciclo entre orientação e verificação.

Scripts e templates de scaffolding ajudam a gerar estruturas iniciais seguindo um padrão recorrente do projeto. Eles podem criar esqueletos de back-end, front-end, módulos, features ou outros artefatos frequentes, acelerando a produção sem abrir mão da consistência. Ainda assim, scaffolding é apenas um dos recursos disponíveis dentro da Skill. Reduzir a Skill a geração automática de boilerplate empobrece seu papel como mecanismo de orientação ampla.

O arquivo skill.md é o núcleo da Skill porque reúne instruções principais de forma direta, resumida e operacional. Ele não deve concentrar todos os detalhes, já que um arquivo grande demais perde clareza e pode até deixar de ser carregado em alguns contextos do Harness. Seu papel é preparar o agente para o contexto geral e apontar quando consultar referências específicas, como modelagem de domínio, autorização, estrutura de pastas, composition root, tratamento de erros, testes ou antipatterns. Essa divisão torna a Skill modular, escalável e mais fácil de manter.

Além de orientar comportamento, o skill.md pode funcionar como ponto de entrada para índices, referências e scripts de validação. Retomando a estrutura anterior, as regras curtas ficam no arquivo principal, enquanto o detalhamento e os scripts associados ficam em arquivos complementares da própria Skill. Os templates ajudam a gerar artefatos consistentes, e os gates executam verificações sobre o código produzido. Essa combinação faz o agente trabalhar com contexto operacional persistente, e não apenas com instruções temporárias fornecidas na interação.

Prompts isolados não bastam quando o objetivo é incorporar o conhecimento do time ao processo de desenvolvimento com IA. A Skill cumpre esse papel ao consolidar padrões, referências, validações e mecanismos de geração em uma estrutura consultável pelo agente. Quanto mais claro e explícito estiver esse conhecimento, menor a chance de produzir soluções desalinhadas com a arquitetura, com as convenções e com a evolução esperada do projeto. No cenário do Videomax, essa estrutura serve como base para sustentar o desenvolvimento do projeto com mais consistência.

## Transcrição

00:00

Bom, pessoal, eu sei que a gente já falou sobre Skills no passado,

00:04

mas eu quero dar uma recapitulação agora,

00:06

principalmente porque as Skills, de forma geral,

00:10

elas são extremamente importantes para fazer parte dos componentes, vamos dizer assim,

00:16

para o nosso Harness. Então, o que acontece é o seguinte.

00:20

Quando a gente fala em Harness Engineering,

00:22

a gente não está falando em apenas criar validações,

00:25

rodar testes ou escrever prompts melhores.

00:28

A gente está falando de preparar realmente um

00:30

ambiente que consiga trabalhar com mais direção,

00:33

mais contexto e mais previsibilidade. Então,

00:36

uma das formas mais importantes que a gente tem para fazer isso,

00:39

de fato, são as skills. Porque o que acontece é o seguinte,

00:43

normalmente já existe uma forma esperada de desenvolver naquele ambiente.

00:48

Existe uma arquitetura escolhida, uma stack definida,

00:51

bibliotecas que o time costuma usar, padrões de organização, convenções de código,

00:57

scripts de validação e um monte de decisão técnica que a gente precisa respeitar. Então,

01:02

se essas decisões ficam totalmente implícitas,

01:05

o que vai acontecer? O agente vai precisar inferir.

01:10

E quando a gente infere demais,

01:13

a gente aumenta a chance de criar um código fora do padrão,

01:17

misturar responsabilidades, usar uma biblioteca que o time não queria que usasse,

01:22

organizar os arquivos do jeito esquisito que a gente não está acostumado a utilizar,

01:27

fazendo com que a gente quebre, na realidade, um monte de padrão. Então,

01:31

a skill vai entrar justamente para reduzir esse espaço de inferência.

01:37

Ela ajuda a transformar o conhecimento do projeto em algo mais explícito,

01:42

reutilizável,

01:43

ao invés de a gente ficar explicando tudo novamente em cada interação. Então,

01:48

você passa a ter uma estrutura que o agente pode

01:51

consultar sempre que precisar para trabalhar naquele contexto.

01:55

E aqui vale entender uma coisa. A skill,

01:58

ela não é apenas para uma documentação do agente,

02:01

tá? Porque documentação, normalmente,

02:02

hoje em dia, ela é feita muito mais para pessoas, tá? A skill,

02:06

ela pode ser lida por pessoas, obviamente,

02:09

mas ela é pensada principalmente para orientar a atuação do agente.

02:14

Então, por isso que a gente precisa ser muito mais,

02:16

vamos dizer assim, operacional. A skill, ela é operacional.

02:20

Ela precisa dizer como que o agente tem que agir,

02:23

quais são os padrões que ele vai seguir,

02:25

quais são os arquivos que ele deve consultar,

02:27

quais os scripts que ele vai ter que utilizar,

02:29

quais as decisões que ele vai ter que tomar para que ele não quebre o nosso software.

02:35

E também a gente pode dar um monte de exemplos

02:37

para ele entender e usar como referência.

02:41

Então, dentro de um Harness,

02:42

a skill funciona como uma camada de orientação. Ela não vai substituir os gates,

02:48

a gente vai falar bastante sobre os gates, tá?

02:51

Mas ela vai ajudar a gente de forma geral,

02:54

inclusive, tanto os gates, testes, avaliações,

02:59

Eventualmente, eles vão poder estar dentro da skill e

03:02

A gente vai mostrar isso durante o projeto, tá?

03:05

Agora, um ponto importante é que é o seguinte,

03:08

Normalmente, uma skill que ela é preparada, né?

03:12

Exatamente para cobrir... o nosso projeto como um todo,

03:16

Ela é composta por alguns elementos principais. Então é o seguinte,

03:21

Os primeiros são as regras de padrões arquiteturais,

03:24

Onde entram as decisões mais importantes sobre a arquitetura de software.

03:29

Ou seja, qual o modelo que o projeto segue, quais as camadas que existem,

03:34

Como as dependências devem se comportar, onde ficam os módulos,

03:38

Quais são os limites que não podem ser quebrados e

03:41

Quais são os padrões que precisam ser totalmente preservados.

03:45

O segundo elemento são os guidelines e o code style.

03:49

Então, essa parte vai definir o jeito esperado de escrever no código do projeto,

03:56

Incluindo desde nomenclatura, organização de arquivos, formatos de artefatos,

04:01

Responsabilidade de cada tipo de componente,

04:04

Os padrões de validação, tratamento de erro,

04:07

Teste e umas outras convenções que vão fazer com que

04:10

O nosso código fique cada vez mais consistente.

04:14

Agora, o terceiro elemento são os exemplos de referência.

04:19

Só a instrução ali para skill às vezes não é o suficiente.

04:23

Muitas vezes, o agente trabalha melhor quando

04:26

Ele consegue olhar para exemplos concretos.

04:29

Então, se você precisa criar uma entidade,

04:31

Um caso de uso, um handler, um repositório, um DTO ou um teste,

04:36

Os exemplos reais vão reduzir bastante a chance de uma implementação fora do padrão.

04:43

Já a gente tem o quarto elemento,

04:45

Que são os scripts que serão utilizados como harness.

04:49

Aqui entram os scripts de validação.

04:53

Técnicas arquiteturais, linters, type check, testes, análise de dependência,

04:59

Detecção de código morto e um monte de mecanismos

05:02

Que vão ajudar o projeto a verificar...

05:05

Se tem algumas regras que podem estar fora.

05:08

Ou seja, se todas as regras realmente foram respeitadas.

05:12

Então, esses scripts são extremamente importantes porque eles vão

05:16

Transformar parte das decisões do projeto em verificações executáveis.

05:23

Ou seja, a gente não vai mais trabalhar ali por probabilidade.

05:26

Vai ser determinístico todo esse processo.

05:29

E nós temos aí o nosso quinto elemento, que são os scripts

05:34

E templates para scaffolding. Então, o que acontece?

05:38

Essa parte é a parte que ajuda a gente a criar

05:41

As estruturas iniciais ou os novos artefatos seguindo um determinado padrão.

05:47

Pode ser aquele esqueleto de um back-end, de um front-end,

05:50

De um módulo, uma feature ou qualquer estrutura recorrente dentro do projeto.

05:54

Mas o ponto principal é entender que o scaffolding é apenas um recurso da skill.

06:00

Ou seja, a skill é algo muito maior.

06:04

Agora, no centro de toda essa estrutura está o nosso famoso skill.md.

06:10

Ele é o coração da skill e ele deve trazer as instruções principais de forma direta,

06:16

Resumida e operacional.

06:18

A ideia não é colocar todos os detalhes possíveis dentro dele.

06:23

Então, o que acontece?

06:25

Se o arquivo principal... ele fica muito grande, esse skill.md muito grande,

06:29

ele vai perder clareza e vai ficar difícil de utilizar.

06:33

Fora que, dependendo ali do modelo,

06:36

do harness que você está usando, ela pode nem ser carregada dependendo da situação, tá? Então,

06:41

o papel do skill.md é preparar o agente para trabalhar o

06:46

contexto geral e saber quando consultar os

06:49

arquivos de referência conforme a demanda.

06:52

Por exemplo, se o agente precisar mexer com modelagem de domínio,

06:56

ele pode consultar uma referência específica sobre isso.

06:59

Se ele precisa trabalhar com autorização, tem um outro arquivo.

07:02

Se ele precisa entender melhor a estrutura de pastas,

07:04

composition root, tratamento de erros, testes ou antipatterns,

07:08

cada tema pode ter a sua própria referência.

07:12

Assim, a skill fica muito mais modular e fácil de manter. Então,

07:17

o skill.md fica com uma direção operacional.

07:21

As referências a gente guarda ali com ela, legal?

07:25

E ela pode ir aprofundando ali com a gente. Então, vamos lá.

07:30

O outro ponto que nós temos também aí nas skills,

07:34

no skill.md, são o quê? Os scripts e as validações.

07:38

Então, o que acontece é o seguinte,

07:40

o skill.md vai ter ali tudo o que a gente precisa, com índices e etc.

07:46

também ele vai poder citar os scripts que vão executar as validações.

07:51

A gente vai chamar isso de gates, tá? Então, o que acontece?

07:54

Os templates ajudam a gente gerar uma estrutura consistente

07:59

e essa combinação é muito poderosa dentro de um Harness,

08:03

porque o agente deixa de trabalhar apenas com a

08:06

instrução solta na conversa e também ele passa

08:09

a trabalhar dentro de um ambiente que comunica ali com

08:13

o projeto como um todo durante a evolução.

08:15

Então, basicamente, imagina que eu tenho a minha skill.md,

08:19

onde ela tem algumas referências,

08:21

algumas regras muito curtas para ser lidas pelo agente. Depois disso,

08:26

eu tenho as referências falando dessas regras e também eu tenho

08:31

referências a scripts que vão estar dentro da minha própria skill,

08:35

que vão poder ser utilizadas.

08:38

Para a gente poder fazer validações no nosso próprio código.

08:43

Inclusive, scripts de scaffolding. Então, antes da gente pensar só nos prompts,

08:49

é importante a gente pensar em um mecanismo como as skills. Então,

08:54

elas vão ajudar a gente a levar o conhecimento do time

08:57

para dentro do processo de desenvolvimento com a IA.

09:00

E quanto mais claro for esse conhecimento,

09:02

menor a chance de a gente criar a solução totalmente desalinhada no nosso projeto.

09:07

Então, vamos nessa. Eu acho que essa é a ideia. E a minha ideia aqui,

09:11

inclusive, é fazer com que você entenda esse processo de criação das skills,

09:16

mas para isso você tinha que entender meio que essa estrutura.

09:20

E a gente vai ver também a skill que eu criei

09:24

para que a gente siga com o nosso projeto do Videomax. Então, vamos nessa.

## Resumo IA

**Abreviações**
*   **DTO**: Data Transfer Object
*   **IA**: Inteligência Artificial
*   **MD**: Markdown

**Resumo**
O objetivo central da aula é recapitular e aprofundar o entendimento sobre as *Skills* como componentes fundamentais do *Harness Engineering*. A aula destaca a importância das Skills para transformar decisões técnicas implícitas de um projeto em instruções explícitas para agentes de desenvolvimento, reduzindo a necessidade de inferência e, consequentemente, a chance de gerar código fora do padrão arquitetural ou das convenções do time.

As Skills funcionam como uma camada de orientação operacional dentro do Harness, não substituindo gates, testes ou avaliações, mas complementando-os ao fornecer direção contínua ao agente. Ao contrário da documentação tradicional, que é focada em pessoas, a Skill é estruturada para guiar a atuação do agente, indicando como agir, quais padrões seguir, arquivos consultar, scripts executar e decisões respeitar.

Uma Skill completa é composta por cinco elementos principais:
1.  **Regras e padrões arquiteturais**: Definem o modelo adotado, camadas, comportamento de dependências, localização de módulos, limites e padrões a preservar, impedindo que o agente viole fronteiras ou misture responsabilidades.
2.  **Guidelines e code style**: Estabelecem o jeito esperado de escrever código, incluindo nomenclatura, organização de arquivos, formato de artefatos, responsabilidade de componentes, padrões de validação, tratamento de erros e testes, garantindo consistência.
3.  **Exemplos de referência**: Artefatos reais do projeto (entidades, casos de uso, handlers, repositórios, DTOs, testes) que servem como guia concreto, tornando as regras mais aplicáveis e reduzindo interpretações erradas.
4.  **Scripts como Harness**: Validações arquiteturais, linters, type checks, testes, análise de dependências e detecção de código morto. Convertem decisões em verificações executáveis, tornando o processo determinístico.
5.  **Scripts e templates para scaffolding**: Auxiliam na geração de estruturas iniciais (esqueletos de back-end, front-end, módulos), acelerando a produção com consistência, mas sem esgotar o papel da Skill.

O coração da Skill é o arquivo `skill.md`, que deve conter instruções principais de forma direta, resumida e operacional. Ele atua como um ponto de entrada para o agente, preparando-o para o contexto geral e indicando quando consultar referências mais específicas (modelagem de domínio, autorização, estrutura de pastas, composition root, tratamento de erros, testes ou anti-patterns), o que torna a Skill modular, escalável e fácil de manter. Essa combinação de prompts, Skills, templates e gates permite que o agente opere com um contexto operacional persistente, alinhado ao conhecimento do time e à evolução esperada do projeto.

**Pontos de atenção**
*   **Decisões Implícitas Geram Inferência Excessiva**: Deixar decisões técnicas subentendidas força o agente a inferir demais, aumentando drasticamente a chance de gerar código fora do padrão, misturar responsabilidades, usar bibliotecas não desejadas ou quebrar limites arquiteturais.
*   **Skill Não é Documentação Tradicional**: A documentação é geralmente para pessoas. A Skill precisa ser operacional, focada em guiar o "como agir" do agente, indicando padrões, arquivos, scripts e decisões.
*   **Evitar Skill.md Excessivamente Grande**: Um arquivo `skill.md` muito extenso perde clareza, dificulta a utilização e pode até deixar de ser carregado por alguns modelos ou contextos do Harness. Ele deve ser um resumo operacional que aponta para referências mais detalhadas.
*   **Scaffolding é Apenas um Recurso**: Reduzir o papel da Skill apenas à geração automática de boilerplate empobrece sua função mais ampla como mecanismo de orientação e consolidação do conhecimento do projeto.
*   **Prompts Isolados São Insuficientes**: Apenas instruções soltas em conversas ("prompts") não são eficazes para incorporar o conhecimento do time ao processo de desenvolvimento com IA de forma consistente. As Skills fornecem um contexto persistente.
*   **Preferência por Verificações Determinísticas**: Em vez de confiar na probabilidade de o agente seguir corretamente as regras, a Skill deve incorporar scripts que transformam decisões em verificações executáveis e determinísticas, garantindo o alinhamento.
*   **Boas Práticas**:
    *   **Tornar o Conhecimento Explícito**: Usar as Skills para transformar o conhecimento do projeto em algo explícito, reutilizável e consultável pelo agente.
    *   **Orientação Operacional**: As Skills devem ser operacionais, indicando como o agente deve agir, quais padrões seguir, arquivos consultar, scripts executar e decisões respeitar.
    *   **Fornecer Exemplos Reais**: Incluir exemplos de referência do próprio projeto para que o agente possa comparar a tarefa atual com artefatos reais, gerando resultados mais consistentes.
    *   **Estruturar a Skill Modularmente**: Dividir os detalhes em arquivos de referência complementares, mantendo o `skill.md` como o núcleo conciso e operacional, facilitando a manutenção e escalabilidade.
    *   **Integrar Validações Executáveis**: Incorporar scripts de validação (linters, testes, verificações arquiteturais) diretamente na Skill, que podem ser executados como "gates" para garantir o cumprimento das regras.
    *   **Definir Padrões Claros**: Explicitar padrões arquiteturais, guidelines de código e code style para garantir consistência e evitar desalinhamento.