Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17967)

## Resumo da aula

A skill pode ser deliberadamente limitada a uma parte do sistema quando o projeto possui múltiplos contextos, como back-end, front-end e monorepo. Aqui, o foco fica apenas no back-end, o que reduz ambiguidade e evita que o agente misture convenções de áreas diferentes. Essa delimitação torna as regras mais precisas e melhora a qualidade das decisões automáticas durante a implementação.

Retomando a estrutura base já definida anteriormente, a skill registra a visão tática da arquitetura com ênfase em Clean Architecture e DDD aplicado ao código. Ela organiza o back-end em domínio, aplicação/use cases, mundo externo — como protocolos e bancos de dados — e composition root, onde as dependências são resolvidas e o fluxo começa. O valor disso não está em redefinir a arquitetura, mas em transformá-la em instruções operacionais que o agente consegue seguir sem depender de inferência.

As regras de importação explicitam quais camadas podem depender de quais outras, como domínio não importando use case, infra ou config, e use case importando apenas domínio. Esse tipo de restrição impede vazamento de responsabilidades e preserva os limites arquiteturais durante a evolução do código. Quando essas regras aparecem na skill, elas deixam de ser convenções implícitas e passam a funcionar como contrato de implementação.

Um esqueleto claro de pastas e arquivos reduz o custo de decisão na hora de criar novas partes do sistema. A skill mostra tanto o fluxo da requisição quanto a organização estrutural esperada, permitindo que o agente entenda onde cada artefato deve nascer. Isso acelera a geração de código porque a arquitetura deixa de ser apenas conceitual e vira um mapa concreto de construção.

As 19 regras invioláveis funcionam como política operacional do projeto. Em vez de depender de bom senso genérico, o agente recebe restrições explícitas sobre como as coisas devem funcionar, o que diminui respostas inconsistentes entre tarefas diferentes. Quanto mais estáveis e específicas forem essas regras, maior a previsibilidade do código produzido.

A skill pode conter exemplos curtos de entidades ricas, value objects, use cases, handlers, sufixos de arquivos e responsabilidades de validação por camada. Esses exemplos não substituem a documentação detalhada; eles servem como âncoras rápidas para orientar decisões recorrentes durante a implementação. O objetivo é oferecer contexto suficiente para agir, sem transformar o arquivo principal em um repositório pesado de conhecimento.

O skill.md permanece curto porque delega aprofundamentos para um índice de referências. Em vez de concentrar toda a explicação sobre modelagem de domínio, tratamento de erro, hierarquia e outros tópicos em um único arquivo, a skill aponta para documentos especializados que podem ser consultados sob demanda. Esse uso de Progressive Disclosure melhora o consumo de contexto pela IA, porque ela carrega primeiro as regras gerais e só acessa detalhes quando a tarefa exige.

Um skill.md com cerca de 400 linhas pode ser suficiente quando ele concentra regras gerais e links para referências complementares. O arquivo principal funciona como camada de orientação e navegação, enquanto os documentos referenciados concentram a profundidade técnica. Essa divisão reduz ruído no contexto principal e mantém a base de conhecimento expansível sem perder legibilidade.

A skill resolve uma parte importante da orientação do agente, mas não elimina todos os problemas de inferência. Retomando o que já foi introduzido sobre o ecossistema do harness, outras camadas de controle ainda são necessárias, como gates e scaffolding, para validar e restringir a execução. A skill orienta; os mecanismos complementares reforçam conformidade e reduzem desvios durante o desenvolvimento.

## Transcrição

00:01

Bom, pessoal, seguinte, partindo dali,

00:04

eu tenho essa minha skill que eu criei e eu queria só

00:07

passar aqui com vocês rapidamente para vocês terem uma ideia de como que,

00:11

o que ela tem e como é que ela foi criada e etc.

00:17

Basicamente, eu pedi para ela criar uma arquitetura meio que focada

00:22

na parte de Clean Architecture com DDD na parte mais tática,

00:26

não naquela parte mais de definições.

00:30

E o ponto importante aqui é que essa skill

00:34

vai tomar conta apenas do back-end da minha aplicação.

00:37

A nossa aplicação vai ser uma aplicação que vai ter um back-end,

00:40

um front-end e um mono-repo, na realidade. E aqui eu só queria,

00:44

eu fiz com que a minha skill focasse especificamente aqui no nosso back-end.

00:49

Então, o que acontece aqui?

00:52

Aqui eu estou trazendo, pedi para ela trazer...

00:55

a ideia das camadas de como que funciona, tem as regras de negócio,

00:59

eu tenho a minha camada de aplicação e use cases,

01:03

aí eu tenho o mundo externo que eu consigo falar,

01:06

com os protocolos, bancos de dados e tudo mais, e eu tenho o meu composition root,

01:11

que no final das contas é onde que inicia as chamadas,

01:14

as resoluções principais das dependências e etc.

01:17

E aí eu mostro qual que basicamente são os apontamentos,

01:25

para as minhas pastas, para as minhas camadas, principalmente.

01:29

Então, eu falo que o domínio nunca pode importar nada de um use case, infra e config.

01:36

O use case, ele importa somente do domínio,

01:38

nunca disso aqui. A infra nunca importa...

01:41

Aqui eu criei algumas regras de apontamento para as camadas.

01:44

Então, eu mostro meio que o fluxo da requisição.

01:47

Aqui é uma outra forma, aqui também,

01:49

para que você consiga entender qual que é a ideia...

01:53

de como que vai ficar as pastas, os arquivos.

01:56

Quando a sua aplicação acaba tendo um esqueleto,

02:02

fica muito mais fácil para ele entender como que vai ser o processo de criação ali.

02:07

E aqui tem regras de estrutura de pastas e aqui tem 19 regras invioláveis.

02:13

Então ele tem aqui 19

02:15

regras que foram criadas de como que as coisas vão funcionar. Então,

02:20

tem detalhes aqui que eles vão ajudar.

02:22

E tudo isso foi feito baseado em uma entrevista,

02:25

baseado em um projeto que eu já tinha. Então, eu não quero que você, nesse momento,

02:28

gaste tempo tentando entender isso. Você vai ter acesso ao código-fonte,

02:32

você pode brincar, melhorar e tudo mais.

02:35

E aqui, ele dá pequenos exemplos de como que funciona, por exemplo,

02:40

uma entidade rica, sem ficar precisando de getter, setter e etc.

02:47

E aqui já fala, tudo que você quiser saber mais,

02:49

você vai em referências. Então, eu dou alguns exemplos, value objects.

02:55

Em um use case, como é que funciona? Como é que é um handler?

02:58

E aqui é como que fica o sufixo e os nomes dos arquivos.

03:03

E aqui é como que funcionam as validações,

03:06

ou seja, de quem que é a responsabilidade de validar o quê em qual camada.

03:11

Então, queries e como que eu faço daí para... o agente se auto-auditar.

03:18

A gente vai falar isso depois, eu não quero falar disso agora aqui com vocês.

03:21

E depois, aqui tem o índice de referências. Esse índice de referências, basicamente,

03:26

tá aqui, ó. Então, tudo isso aqui são caras que a IA,

03:31

ela pode acessar conforme ela vai desenvolvendo ali Progressive Disclosure,

03:36

que vai ajudar ela a carregar conforme ela precisa.

03:39

Ah, eu quero saber mais de modelagem de domínio. Então,

03:42

tá aqui, ó. Modelagem de domínio, como é que funciona. Aí sim,

03:46

é um arquivão com tudo sobre como que eu trabalho aqui com a modelagem e etc.

03:52

Tratamento de erro, hierarquia, traz um monte de detalhe aqui. Mas perceba,

03:57

isso aí ela vai poder consultar on demand. Por isso que o meu skill .md,

04:03

ele é curto aqui, ele tem 400 linhas aqui de forma geral. Então, se você perceber,

04:09

eu trago as regras gerais e depois faço um índice de referências,

04:12

apontando para todos os arquivos ali para você conseguir dar uma olhada.

04:17

Então, isso aqui já vai ajudar você muito,

04:22

mas assim, muito, muito mesmo,

04:23

na hora que o agente vai seguir no seu processo de desenvolvimento.

04:29

Agora, novamente, isso aqui resolve muita coisa,

04:34

mas a gente vai entender que conforme a gente vai

04:38

entrando e vai se aprofundando mais em Harness Engineering,

04:41

não é apenas uma skill que vai conseguir garantir, né?

04:46

Ou simplesmente resolver alguns problemas que simplesmente a IA infere.

04:52

Por isso que a gente vai depois entrar em gates,

04:55

a gente vai entrar na parte de scaffolding e a gente vai seguindo a partir dali.

05:00

Fechou? Então, vamos nessa.

## Resumo IA

**Abreviações**
*   **DDD**: Domain-Driven Design (Projeto Orientado ao Domínio)
*   **IA**: Inteligência Artificial

**Resumo**
A aula apresenta a construção e o propósito de uma "skill" para um agente de IA no contexto de desenvolvimento de software, focando em arquitetura e código. O objetivo principal é transformar a visão tática de uma arquitetura baseada em Clean Architecture e DDD em instruções operacionais explícitas para o agente, minimizando a inferência e garantindo a consistência do código gerado.

Inicialmente, a skill é deliberadamente limitada ao back-end da aplicação, mesmo que o projeto inclua front-end e um monorepo, para reduzir ambiguidades e evitar a mistura de convenções de diferentes domínios. A estrutura base da arquitetura é delineada em camadas: Domínio (regras de negócio), Aplicação/Use Cases, Mundo Externo (protocolos, bancos de dados) e Composition Root (resolução de dependências e início do fluxo).

São estabelecidas regras de importação explícitas, definindo quais camadas podem depender de outras (ex: domínio não importa use case, infra ou config; use case importa apenas domínio), funcionando como um contrato de implementação. A skill também inclui um esqueleto claro de pastas e arquivos, além do fluxo da requisição, para guiar o agente na organização estrutural e na criação de artefatos.

Dezenove regras "invioláveis" são apresentadas como políticas operacionais do projeto, fornecendo restrições explícitas para o funcionamento do sistema. Exemplos curtos de entidades ricas, value objects, use cases, handlers, sufixos de arquivos e responsabilidades de validação por camada são incluídos para servir como âncoras rápidas nas decisões recorrentes.

O arquivo principal da skill (`skill.md`) é mantido conciso (cerca de 400 linhas), aplicando o conceito de Progressive Disclosure. Ele delega o aprofundamento de tópicos como modelagem de domínio, tratamento de erro e hierarquia para um índice de referências externas, que a IA pode consultar sob demanda. Essa abordagem otimiza o consumo de contexto pela IA, carregando primeiro as regras gerais e acessando detalhes apenas quando necessário.

Por fim, é destacado que a skill resolve uma parte da orientação do agente, mas não todos os problemas de inferência. Outras camadas de controle do ecossistema de Harness Engineering, como "gates" e "scaffolding", são necessárias para validar e restringir a execução, reforçando a conformidade e reduzindo desvios no desenvolvimento.

**Pontos de atenção**
*   **Delimitação de Contexto:** Limitar a skill a uma parte específica do sistema (ex: apenas back-end) é crucial para reduzir ambiguidade e evitar que o agente misture convenções de áreas distintas.
*   **Explicitação de Regras:** A arquitetura deve ser transformada em instruções operacionais explícitas, não dependendo da inferência ou do "bom senso genérico" do agente. Isso torna as decisões automáticas mais precisas.
*   **Regras de Importação como Contrato:** As regras explícitas sobre dependências entre camadas funcionam como um contrato de implementação, impedindo vazamento de responsabilidades e preservando os limites arquiteturais.
*   **Esqueleto e Fluxo Claros:** Fornecer um esqueleto de pastas e arquivos e o fluxo da requisição reduz o custo de decisão do agente e acelera a geração de código.
*   **Políticas Operacionais Invioláveis:** Definir regras operacionais claras e estáveis (ex: as "19 regras invioláveis") aumenta a previsibilidade do código produzido e diminui respostas inconsistentes.
*   **Exemplos como Âncoras, não Substitutos:** Exemplos curtos devem servir como guias rápidos para decisões recorrentes, sem substituir a documentação detalhada.
*   **Progressive Disclosure:** Manter o `skill.md` conciso com regras gerais e delegar o aprofundamento para referências externas melhora o consumo de contexto pela IA, reduz ruído e mantém a base de conhecimento expansível.
*   **Limitações da Skill:** A skill é uma ferramenta de orientação, mas não elimina todos os problemas de inferência. Outros mecanismos complementares de controle, como "gates" e "scaffolding", são essenciais para validar, restringir e reforçar a conformidade.