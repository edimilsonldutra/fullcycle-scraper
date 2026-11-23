Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17883)

## Resumo da aula

Arquivos como cloud.md, agents.md e registros de decisão ajudam a orientar o agente, mas não conseguem carregar toda a complexidade real de um codebase maduro. Regras de negócio, exceções históricas, motivos de falha e decisões arquiteturais se acumulam mais rápido do que esses artefatos conseguem representar. Além disso, esse tipo de documentação envelhece com facilidade quando módulos mudam, pull requests são mergeadas e o comportamento esperado do sistema evolui. Domar o agente exige reconhecer que instruções estáticas são úteis como base, mas insuficientes como mecanismo único de controle.

Retomando o harness específico de projeto já estabelecido, uma árvore de diretórios explícita pode servir como guia inicial para reduzir ambiguidade. Isso é especialmente útil no começo de um projeto ou ao entrar em um codebase grande já existente, quando o agente ainda não tem pistas suficientes para navegar com segurança. O problema é que a própria estrutura do sistema muda, e qualquer representação rígida dessa organização tende a ficar obsoleta. Por isso, esse tipo de apoio funciona melhor como instrumento transitório do que como fonte permanente de verdade.

A velocidade de produção com agentes pode ultrapassar a capacidade humana de validação, e esse descompasso vira um problema operacional. Quando várias features críticas avançam ao mesmo tempo, surgem pull requests grandes, interfaces alteradas e conflitos frequentes entre mudanças concorrentes. O gargalo deixa de ser escrever código e passa a ser revisar, integrar e garantir que tudo continua funcionando após o merge. Harness Engineering precisa tratar confiabilidade como disciplina de contenção de fluxo, não apenas como instrução de comportamento do modelo.

Receber dezenas de PRs por dia muda a natureza do desenvolvimento: o risco principal passa a ser integração incorreta, não falta de produtividade. Revisões com milhares de linhas alteradas têm baixa auditabilidade, porque nenhum humano consegue validar com profundidade cada impacto estrutural, cada regressão potencial e cada interação entre mudanças paralelas. Nesse cenário, confiar apenas em revisão manual é insuficiente. O harness precisa criar condições para que o código já chegue com um nível mínimo de funcionamento e qualidade antes de depender do olhar humano.

Lembra da arquitetura definida anteriormente como parte do ambiente do agente: ela não se perde de uma vez, mas por pequenas violações acumuladas. Um DTO fora do padrão, um if acessando algo indevido, uma dependência colocada no lugar errado parecem desvios locais, porém viram exemplos observáveis para a IA repetir. Como o agente é muito bom em detectar e propagar padrões, ele amplia essas exceções até que elas se tornem o novo normal do codebase. O resultado é deriva arquitetural: repositórios aparecem em services, regras de negócio escorrem para controllers e a estrutura original se degrada sem ruptura explícita.

Quanto maior a pressão por velocidade, menor tende a ser a tolerância para correções estruturais que não entregam feature imediatamente. Isso favorece a aceitação de desvios pequenos, porque cada um parece barato no curto prazo. O acúmulo, porém, cobra depois em forma de caos local, dificuldade de manutenção e perda de previsibilidade do agente. Organizar o harness passa a ser uma estratégia para impedir que a urgência operacional redefina a arquitetura por erosão.

O crescimento do codebase aumenta a complexidade independentemente de usar IA, mas agentes aceleram a taxa de expansão e, com isso, a taxa de acúmulo de resíduos. Se novas features são adicionadas sem refatoração contínua e intencional, partes antigas deixam de fazer sentido e permanecem no sistema sem utilidade real. Código morto inclui fluxos abandonados, recursos substituídos e trechos que deveriam ter sido removidos quando a feature mudou. Esse excesso aumenta fricção, eleva risco de regressão e dificulta futuras decisões do próprio agente, que passa a enxergar exemplos inválidos como se fossem válidos.

Quando o volume de mudanças torna a revisão humana insuficiente, a remoção ativa de código morto deixa de ser higiene opcional e vira rotina operacional. A referência a um “garbage collector de agente” ilustra exatamente isso: usar processos recorrentes para localizar resíduos que sobraram após sucessivas iterações automáticas. O mesmo raciocínio vale para code review: humanos continuam importantes, mas não são necessariamente os melhores revisores em escala. Uma IA bem contida por um harness robusto pode atuar como revisora eficaz, desde que o ambiente imponha critérios claros de qualidade e consistência.

## Transcrição

00:01

Bom, pessoal, agora a gente vai começar a chegar em alguns pontos mais tangíveis,

00:05

já que a gente falou bastante sobre Harness Engineer e etc.

00:09

Mas a gente entra num ponto aqui de domar o agente. O que isso significa?

00:15

Bom, a primeira coisa que a gente vai começar a perceber é que a

00:19

gente começa a ter desafios para a gente conseguir fazer o controle do agente.

00:23

No final das contas, isso é a parte de Harness Engineer.

00:27

Então, o que acontece é o seguinte.

00:29

Quando a gente tem ali um conhecimento aprofundado do Codebase,

00:33

mesmo com os modelos extremamente avançados, você pode ter um super modelo,

00:37

super avançado, a gente vai perceber que,

00:40

mesmo que você tenha um CloudMD, um AgentsMD,

00:43

eles não vão conseguir comportar todas as regras do seu sistema,

00:47

todas as Architecture Decision Records,

00:50

todos os motivos de falha ali do seu sistema.

00:53

Uma outra coisa que é super comum é que as regras vão ficar...

00:59

desatualizadas de uma forma muito fácil ao longo do tempo.

01:02

O grande problema é que a gente não consegue

01:05

verificar se essas regras estão desatualizadas o tempo todo.

01:11

Conforme módulos vão entrando, por requests vão sendo mergeados,

01:15

comportamentos dos agentes vão sendo mudados,

01:18

a gente começa a ter esses desvios. Então, o que acontece?

01:25

Mesmo que a gente coloque uma estrutura básica de

01:28

diretórios e que muitas vezes é muito útil,

01:31

tem gente que é contra colocar uma estrutura de diretórios.

01:36

E eu muitas vezes sou a favor no início

01:41

de um determinado projeto ou num projeto que já

01:43

tem um codebase grande e eu estou chegando lá naquele

01:46

momento e eu quero dar uma guiada no agente.

01:49

Muitas vezes eu coloco e aí, ao longo do projeto, eu removo a árvore de diretórios.

01:54

Mas, por exemplo, o que acontece no meio dessa história?

01:59

Essa estrutura vai mudar também. Então, é muito fácil de o seu CloudMD,

02:05

esse AgentsMD e etc.,

02:07

esses caras começarem a mudar. Fora que ele não vai comportar,

02:11

esses arquivos não podem ser muito grandes. Então,

02:13

esse é um problema e faz parte dos desafios que a gente acaba tendo.

02:20

Outro ponto é confiabilidade. Ou seja,

02:24

um dos grandes problemas hoje em dia é que a velocidade que a

02:30

gente entrega acaba sendo muito maior do que nós humanos podemos validar.

02:37

Quando a gente tem...

02:39

uma quantidade enorme de entregas ali de milhares de linhas alteradas.

02:43

A gente tem interface modificada,

02:45

a gente tem um monte de features que são

02:47

mega críticas sendo implementadas ali naquele momento.

02:50

O que acontece é que nós vamos ter o quê?

02:54

Um monte de pull requests criadas e a gente vai ter uma quantidade enorme de conflitos.

03:01

Eu não sei até que ponto hoje em dia você

03:03

está desenvolvendo diversas features simultaneamente e eu não

03:07

sei o quanto você já se enrolou com conflitos porque

03:10

você teve várias features sendo desenvolvidas ao mesmo tempo.

03:14

Agora, quando você começa a ter lá 20, 30, 40 PRs por dia,

03:18

Fazer o merge de tudo isso e garantir que está tudo funcionando,

03:22

Cada vez vai se virando um desafio maior. Então, às vezes,

03:28

Tudo que a gente quer é desenvolver mais rápido, mas nós mesmos,

03:31

Às vezes, a gente não consegue dar vazão. E você,

03:34

Inclusive, tem um artigo da própria OpenAI falando exatamente sobre

03:39

Esse desafio que eles acabaram tendo ao longo do tempo.

03:44

Um outro ponto, que é um outro desafio,

03:47

Que é o desvio gradual da arquitetura.

03:51

Então, vamos imaginar que eu comecei a definir claramente a minha arquitetura.

03:56

Desde os fundamentos ali da minha arquitetura,

03:59

Vamos dizer que eu quero trabalhar com Solid,

04:01

Quero trabalhar com Domain-Driven Design, Clean Architecture,

04:04

Arquitetura Hexagonal, tanto faz, tá? Aí,

04:07

Ao longo do tempo, a gente vai vendo pequenas violações acontecendo ali.

04:12

E elas vão se acumulando.

04:14

No começo, é um DTO ali tendo um negocinho um pouquinho diferente.

04:19

Outro ali é um IF chamando um repositório, não sei de onde, né?

04:25

E o que acontece? Conforme esses pequenos desvios vão se acumulando, a IA começa,

04:32

Ela é mestre em seguir padrões. E o que acontece?

04:35

Esses padrões vão se acumulando e ela vai se desviando, se desviando,

04:40

Se desviando, até que aquilo que você imaginava que deveria ser no início,

04:46

Não é mais, tá? Então, de repente,

04:49

A gente vai ter repositório dentro dos services,

04:52

Regras de negócio no controller e as coisas vão ali degringolando ao longo do tempo.

04:58

E o grande ponto é que a gente só percebe isso

05:01

Quando as coisas já estão entrando no meio do caos.

05:04

Por quê? Porque são muitas PRs, são muitas coisas para corrigir,

05:08

São muitas coisas que a gente tem que entregar

05:10

E eu acredito que daqui para frente...

05:15

Nós, cada vez mais, a gente vai ser mais pressionado a entregar mais rápido,

05:19

Porque temos agentes já na nossa mão programando pra gente. Então,

05:23

Esses desvios, eles vão acontecer. E o ponto é,

05:28

Mais uma forma de como que a gente

05:31

Tem que trabalhar e organizar todo esse harness,

05:35

Desenhar tudo isso para evitar que isso aconteça.

05:40

Outra coisa que acontece demais, isso já aconteceu diversas vezes em projetos que eu

05:46

Estava trabalhando, desenvolvendo, que é dívida técnica e código morto,

05:51

Ou chamado de ghost mode. O que isso significa?

05:55

Conforme a grande quantidade de código cresce,

05:59

Maior vai ficar sempre a complexidade.

06:01

Isso aí é regra básica, independente de A. Quanto maior meu codebase,

06:06

Mais complexidade eu tenho. Quanto mais complexidade eu tenho,

06:10

Normalmente, eu tenho mais fricção para entregar coisa nova,

06:13

Porque o risco aumenta e...

06:16

Aí eu tendo a fazer menos merges, eu tendo a fazer menos releases do meu software,

06:22

Porque tenho medo de fazer com que o

06:24

Meu software dê problema ou tenha regressões.

06:28

Outra coisa,

06:29

Se eu não fizer processos contínuos de refatoração,

06:35

De forma intencional, o que acontece?

06:39

Eu vou aumentar ainda mais essas dívidas técnicas e código morto.

06:44

Quando eu digo código morto,

06:45

são realmente códigos que ficam ali que não servem mais para nada,

06:49

uma feature que desapareceu,

06:50

uma mudança que normalmente acabou mudando uma feature e

06:55

aquele recurso não deveria mais existir e acabou ficando porque

06:59

a IA foi programando as novas features e ela não

07:02

foi removendo coisas que não precisam mais ser usadas.

07:05

São códigos que realmente não deveriam estar lá, tá?

07:08

Então, o que acontece?

07:10

A gente vai acumulando essas tranqueiras, vamos dizer, de código que vão ficando.

07:16

Só para vocês terem uma ideia, a OpenAI, pelo menos em um dos artigos dela,

07:20

ela coloca que, sei lá,

07:21

toda sexta-feira eles rodam garbage collector de

07:24

agente somente para ficar procurando código morto.

07:27

Olha o ponto que nós estamos pelo fato de que... Eu tenho tanta pull request,

07:33

e não é uma pull request que o code review é simples.

07:36

Imagina que você recebe uma pull request com mais de mil linhas alteradas.

07:40

Como que a gente consegue revisar tudo isso?

07:43

Eu pedi uma nova feature, veio ali 50 mudanças dentro de um mesmo arquivo,

07:50

ou entraram ali 3 mil linhas novas,

07:53

saíram mil linhas. Cara, conseguir fazer esses tipos de revisões é muito difícil.

08:00

Então... Cada vez mais a gente vai ter que acreditar que o código que vai chegar, ele

08:07

tem que estar ali minimamente funcionando,

08:12

mas minimamente com uma qualidade decente.

08:15

E a gente vai começar a perceber que nós não somos, às vezes,

08:18

os melhores revisores de código. Que a IA pode ser uma ótima revisora de código,

08:23

desde que essa parte de Harness esteja muito bem feita também.

## Resumo IA

**Abreviações**
*   **ADR**: Architecture Decision Record (Registro de Decisão de Arquitetura)
*   **DTO**: Data Transfer Object (Objeto de Transferência de Dados)
*   **IA**: Inteligência Artificial
*   **PR**: Pull Request

**Resumo**
A aula aborda o desafio de "domar o agente" de IA no desenvolvimento de software, reconhecendo que a complexidade de um codebase maduro excede a capacidade de documentações estáticas (como arquivos `cloud.md`, `agents.md` e ADRs) e estruturas de diretórios rígidas, que se tornam rapidamente obsoletas. O objetivo principal é discutir como a Engenharia de Harness é fundamental para controlar o comportamento dos agentes, garantindo confiabilidade e mantendo a integridade arquitetural em um ambiente de alta velocidade de produção.

O instrutor explica que a agilidade dos agentes pode gerar um volume de código que supera a capacidade humana de validação, resultando em pull requests (PRs) massivas, conflitos frequentes e gargalos na revisão e integração. Nesse cenário, o foco da confiabilidade muda de "instrução de comportamento do modelo" para uma "disciplina de contenção de fluxo". É destacado o perigo da deriva arquitetural, onde pequenas violações de padrões (como DTOs fora do padrão ou repositórios em services) são detectadas e propagadas pela IA, degradando a arquitetura original. Além disso, o crescimento acelerado do codebase, potencializado pelos agentes, leva ao acúmulo de dívida técnica e "código morto", que aumenta a fricção, o risco de regressão e confunde as futuras decisões do agente.

Como solução, a aula propõe que o harness deve criar condições para que o código gerado já possua um nível mínimo de funcionamento e qualidade. É sugerida a remoção ativa de código morto através de processos recorrentes, metaforicamente chamados de "garbage collector de agente". Por fim, o instrutor aponta que a IA, quando bem contida por um harness robusto, pode se tornar uma revisora de código eficaz em larga escala, complementando ou substituindo a revisão humana em certas etapas, dado que humanos não conseguem auditar com profundidade milhares de linhas alteradas.

**Pontos de atenção**
*   **Limitações da Documentação Estática:** Arquivos como `cloud.md`, `agents.md` e ADRs são úteis como base, mas insuficientes para carregar a complexidade real de um codebase e envelhecem rapidamente com a evolução do sistema.
*   **Obsolescência de Estruturas Rígidas:** Árvores de diretórios explícitas funcionam melhor como guias transitórios no início de um projeto ou ao entrar em um codebase existente, pois a estrutura do sistema também muda e representações rígidas se tornam obsoletas.
*   **Descompasso Produção vs. Validação:** A velocidade de geração de código por agentes pode ultrapassar a capacidade humana de revisão e validação, criando PRs gigantes e um gargalo na integração, aumentando o risco de integrações incorretas.
*   **Inadequação da Revisão Manual em Escala:** Revisões de código com milhares de linhas alteradas têm baixa auditabilidade humana, exigindo que o harness garanta um nível mínimo de funcionamento e qualidade no código antes da dependência do olhar humano.
*   **Perigo da Deriva Arquitetural:** Pequenas violações arquiteturais (e.g., DTOs fora do padrão, repositórios em services, regras de negócio em controllers) são detectadas e propagadas pela IA como padrões, degradando a arquitetura original de forma gradual e difícil de perceber. A pressão por velocidade acelera a aceitação desses desvios.
*   **Acúmulo de Dívida Técnica e Código Morto:** Acelerado pelos agentes, o crescimento do codebase sem refatoração contínua leva ao acúmulo de código morto (fluxos abandonados, recursos substituídos), aumentando a fricção, o risco de regressão e dificultando decisões futuras do agente.
*   **Necessidade de Contenção de Fluxo:** Harness Engineering deve tratar a confiabilidade como uma disciplina para conter o fluxo de mudanças, não apenas como instrução de comportamento do modelo, para gerenciar os riscos de integração e a degradação arquitetural.
*   **Remoção Ativa de Código Morto:** A remoção de código morto deve ser uma rotina operacional ("garbage collector de agente") para combater o resíduo deixado por sucessivas iterações automáticas e manter a sanidade do codebase.
*   **Potencial da IA na Revisão de Código:** Em escala, uma IA bem contida por um harness robusto pode atuar como revisora eficaz, impondo critérios claros de qualidade e consistência, onde humanos são insuficientes.