Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17965)

## Resumo da aula

Uma skill codifica decisões arquiteturais; ela não cria, sozinha, uma arquitetura madura para o projeto. Antes de escrever qualquer instrução para o agente, é necessário definir camadas, componentes, regras de dependência, bibliotecas padrão, organização de pastas, criação de módulos e estratégia de testes. Se o time adota Clean Architecture, DDD, arquitetura hexagonal, MVC, arquitetura modular ou microservices, esse padrão precisa estar explícito. Só depois disso a skill consegue transformar essas escolhas em instruções reutilizáveis.

O ponto de partida não é o sistema completo, mas um esqueleto funcional que rode de ponta a ponta. Esse hello world precisa incluir um endpoint /health, porque o agente depende de uma forma objetiva de verificar se o ambiente subiu corretamente. O health check não deve validar apenas o web server; ele também precisa consultar dependências críticas como banco de dados, mensageria, cache, storage e serviços externos. Sem isso, o agente não consegue distinguir entre aplicação realmente operacional e processo apenas iniciado.

Retomando o uso do agente no projeto, o /health vira uma peça operacional do harness. Ele permite validar se o back-end responde, se o banco está acessível e se os serviços principais estão disponíveis antes de implementar uma feature, testar endpoints, rodar avaliações ou validar entregas. Isso reduz falsos positivos de execução e melhora a automação do fluxo. Um health check bem construído deixa de ser só observabilidade e passa a ser infraestrutura de trabalho para o agente.

O arquivo skill.md concentra as regras essenciais que orientam o comportamento do agente. Ele deve registrar filosofia da arquitetura, convenções, responsabilidades por camada, regras invioláveis, formatos canônicos de artefatos, nomenclatura, validação, distinções como repositories versus queries, checklist de self-audit e índice de referências. A função desse arquivo é dar contexto suficiente sem se tornar um manual exaustivo. Quando o arquivo principal cresce demais, a skill perde clareza e fica mais difícil de aplicar com consistência.

Em vez de redigir a skill inteira manualmente desde o início, vale usar a IA em modo exploratório para extrair os requisitos do projeto. Esse processo funciona como uma entrevista estruturada sobre stack, módulos, camadas, entidades, casos de uso, handlers, validação, subida de ambiente, health check e regras que não podem ser quebradas. O ganho está em transformar conhecimento tácito da equipe em respostas organizadas. Com isso, a primeira versão da skill nasce a partir de decisões explícitas, e não de suposições do agente.

O primeiro draft da skill é apenas uma versão inicial baseada na entrevista e no esqueleto existente. Ele precisa ser revisado em busca de ambiguidades, conflitos entre instruções, excesso de detalhe no arquivo principal e incompatibilidades com a estrutura real do projeto. Uma revisão útil é pedir ao próprio agente que procure regras difíceis de seguir, instruções repetidas e trechos que deveriam virar referência externa. Como a skill orienta o comportamento do agente, qualquer confusão no texto tende a se refletir diretamente na execução.

Os detalhes extensos não precisam ficar no skill.md; eles podem ser movidos para arquivos de apoio carregados sob demanda. Exemplos longos, templates e aprofundamentos específicos cabem melhor em uma pasta de referências com documentos como anti-patterns.md, authorization.md, domain modeling.md ou error handling.md. Essa separação mantém o núcleo da skill enxuto, em torno de um limite prático de algumas centenas de linhas, e preserva a profundidade onde ela realmente é necessária. O resultado é uma skill modular: o essencial fica centralizado, e o aprofundamento é consultado conforme o contexto.

O scaffolding inicial do projeto não serve apenas para começar mais rápido; ele também fornece a base concreta que depois pode ser portada para dentro da skill. Em vez de iniciar cada projeto do zero, a equipe reaproveita um template base com estrutura, convenções e verificações já definidas. Quando esse template é incorporado à skill, o agente passa a conseguir gerar automaticamente a estrutura inicial do projeto de forma alinhada ao ambiente real. A skill deixa de ser apenas documentação e passa a atuar como mecanismo de reprodução do padrão adotado.

## Transcrição

00:01

Bom pessoal, eu sei que você tá querendo ver a skill que a gente criou,

00:04

como é que funciona esse processo,

00:05

tá? Mas o grande ponto é que o que eu vou mostrar pra vocês, o que você vai ter acesso,

00:11

a gente vai fazer algumas coisas aqui na prática,

00:13

a minha ideia principal é que você tenha independência, tá?

00:16

Por quê? Porque hoje a gente tem uma stack,

00:19

a gente tá trabalhando dentro de um projeto exemplo.

00:21

Porém, a nossa ideia aqui...

00:24

é que se amanhã você estiver num projeto com outra stack,

00:27

outra arquitetura, outras bibliotecas, outro estilo de código,

00:30

com outra convenção,

00:31

você ainda precisa ser capaz de criar uma skill que represente esse ambiente.

00:36

Então vamos pensar rapidinho numa checklist prática,

00:39

somente para você entender a linha de raciocínio que pelo menos eu utilizo

00:43

na hora de criar uma skill ali do zero para o meu projeto.

00:47

Beleza? Então vamos lá.

00:49

O primeiro passo é definir a arquitetura base do software.

00:53

Então, antes de escrever a skill,

00:55

você precisa saber qual é o padrão que o projeto vai seguir.

00:59

Quais camadas vão existir?

01:01

Quais componentes arquiteturais são importantes?

01:04

Como as dependências devem se comportar?

01:07

Quais bibliotecas externas a gente vai utilizar por padrão?

01:11

Quais são as bibliotecas internas que fazem parte da base do projeto?

01:16

Qual é a organização das pastas? Como os módulos devem ser criados?

01:20

Como que os testes devem ser organizados. Então, se você perceber,

01:24

a gente entra aqui numa fronteira que sai um pouco do escopo desse módulo,

01:28

porque a gente começa a falar mais de arquitetura de software,

01:31

padrões arquiteturais,

01:33

organização de código e algumas decisões técnicas do projeto. Então,

01:37

eu estou partindo do princípio de que você já tem essas

01:40

guidelines ou pelo menos tem a condição de definir.

01:43

A skill não vai inventar uma arquitetura madura completamente sozinha.

01:48

Ela vai codificar a arquitetura que você decidiu seguir. Então,

01:52

se o seu time usa Clean Architecture, DDD, arquitetura hexagonal,

01:55

MVC, modular, microservice ou qualquer outro padrão,

02:00

isso precisa estar muito claro antes.

02:02

A skill entra depois para a gente transformar essas

02:05

decisões em instruções reutilizáveis para o agente.

02:09

Agora, o segundo passo... é criar o esqueleto base do projeto.

02:15

Basicamente, fazer um hello world funcional.

02:17

Não precisa começar com o sistema completo,

02:20

mas você precisa ter uma base que rode.

02:23

E aqui eu recomendo que você crie um endpoint de health,

02:27

ou seja, um barra health.

02:28

Só que esse endpoint não deve retornar apenas um OK do web server.

02:33

Ele deve verificar também os serviços importantes que a aplicação utiliza.

02:38

Por exemplo... banco de dados, sistema de mensageria, cache, storage,

02:43

serviços externos ou qualquer dependência crítica do ambiente.

02:47

Isso é extremamente útil e importante para os

02:50

Projetos trabalharem em conjunto com o agente. Por quê?

02:54

Porque o próprio agente pode usar esse endpoint para

02:57

verificar se a aplicação está no ar.

02:59

Se ele consegue subir o ambiente, ele consegue chamar o Barra Health.

03:04

Ele consegue entender se o back-end está funcionando e respondendo,

03:08

se o banco de dados está acessível,

03:09

se os serviços principais estão funcionando. Então,

03:12

esse tipo de detalhe parece super simples, mas ajuda pra caramba na automação.

03:16

Se o agente precisa implementar uma feature, testar um endpoint,

03:20

rodar uma avaliação ou validar uma entrega,

03:23

ele precisa saber se o seu sistema realmente está de pé.

03:26

Então, um health check bem feito vira uma peça

03:28

de apoio extremamente importante para o seu harness.

03:32

O terceiro passo é colocar as guidelines no papel.

03:36

E aqui entra a criação da skill.md.

03:39

A skill.md é o arquivo principal da skill.

03:42

É ali que você vai descrever todas as regras mais importantes,

03:46

a filosofia da arquitetura, as convenções,

03:49

as responsabilidades de cada camada e os padrões que o agente deve seguir.

03:53

Eu recomendo estruturar essa skill com seções bem claras.

03:57

Por exemplo, no caso da skill que a gente está utilizando como base,

04:00

a estrutura possível seria a filosofia da arquitetura,

04:04

a regra de dependência, estrutura canônica de pasta,

04:08

regras invioláveis, formatos canônicos dos principais artefatos,

04:13

padrões de nomenclatura e sufixos,

04:15

responsabilidade de validação, repositories versus queries,

04:20

checklist de self-audit, índice de referências.

04:23

Perceba que nesse momento eu não estou falando para você

04:26

colocar todos os detalhes possíveis dentro da skill.

04:29

Pelo contrário.

04:30

Esse skill.md precisa ser objetivo e o suficiente para que o agente consiga

04:37

entender a base do projeto sem virar um arquivo gigante e difícil de usar.

04:43

Agora, o outro passo, o quarto passo é... entrar em um módulo exploratório com o IA.

04:50

Ou seja, você não precisa digitar 500 linhas do zero.

04:54

Na prática, esse é um ótimo momento para usar um plain mode,

04:58

um grilled me, qualquer extensão, alguma skill para entrevista,

05:03

para que a IA faça as perguntas de uma forma

05:07

extremamente exaustiva para você conseguir extrair os detalhes do seu projeto.

05:11

Você pode pedir para a gente te entrevistar sobre a arquitetura base,

05:15

as bibliotecas usadas, os padrões de código,

05:17

a estrutura de pastas, as regras de dependências,

05:20

os tipos de artefatos, o fluxo de testes, o health check e os scripts necessários.

05:26

A ideia é usar a IA como parceira para levantar os requisitos da própria skill.

05:32

Então, ao invés de a gente começar escrevendo a skill diretamente,

05:35

você começa respondendo às perguntas. Qual stack vamos usar?

05:40

Como os módulos vão ser organizados?

05:42

Quais camadas existem? Onde ficam as entidades? Onde ficam os casos de uso?

05:47

Como é que funcionam os handlers? Como que a biblioteca de validação vai ser usada?

05:52

Como que o ambiente sobe?

05:53

Como que o agente verifica que a aplicação está funcionando?

05:56

Quais são regras que a gente não pode quebrar? Depois dessa entrevista,

06:01

a IA já vai ter o material suficiente para gerar um primeiro draft.

06:05

E aí, a gente tem o quinto passo, que é a geração da skill.

06:09

Aqui o agente cria a primeira versão da skill com base

06:13

nas respostas da sua entrevista e no esqueleto que você já tem.

06:18

Mas esse primeiro draft, ele não deve ser,

06:21

vamos dizer assim, aceito automaticamente. Você vai precisar revisar,

06:24

você vai procurar inconsistências, você vai ver se alguma regra ficou ambígua,

06:29

você vai conferir se a estrutura sugerida combina com o projeto,

06:33

você vai ver se tem instruções conflitantes, isso acontece bastante,

06:37

tá? E você vai ter que analisar se o

06:40

agente colocou detalhes demais também no arquivo principal.

06:44

Então, uma dica de ouro para você.

06:47

Peça para o próprio agente revisar a skill. Você pode pedir algo assim,

06:51

analise essa skill procurando por ambiguidades, conflitos,

06:55

regras difíceis de seguir,

06:56

instruções repetidas e pontos que deveriam virar referência externa.

07:01

Esse tipo de revisão é mega importante porque a skill...

07:05

vai orientar o comportamento do agente no projeto. Então,

07:08

se ela estiver confusa, o agente também vai estar confuso.

07:12

E aí a gente chega no sexto passo, que é organizar as referências.

07:16

Essa é uma das grandes vantagens de a gente conseguir trabalhar com a skill,

07:20

porque você não precisa colocar tudo dentro do skill.md.

07:24

O skill pode ter materiais de apoio, em pastas de referências,

07:29

e esses materiais podem ser carregados conforme a necessidade.

07:33

Então, ao invés de transformar o skill.md num documento enorme,

07:36

a gente vai tentar manter ele o mais enxuto possível,

07:40

normalmente em torno de 500 linhas, ali já é um bom limite, de forma geral.

07:45

E os detalhes mais específicos, como exemplo longo,

07:49

template, explicações mais profundas de casos particulares,

07:52

eles podem ir tudo isso para um arquivo separado dentro de uma pasta de referências.

07:58

No nosso caso, por exemplo,

08:00

a gente vai ter arquivos como... anti-patterns.md, authorization,

08:04

composition root, config and dev env, cross-feature use cases,

08:09

domain events, domain modeling, error handling, folder structure. Então,

08:14

você vai ver que a gente tem um monte de arquivo

08:16

de referência que foi criado ao longo do tempo.

08:19

Então, esse formato deixa a skill mais modular e

08:23

a skill.md fica apenas ali como o essencial,

08:28

vamos dizer assim. E as referências vão...

08:31

guardando o aprofundamento. Se o agente precisa mexer com autorização,

08:35

ele pode consultar o authorization.md.

08:37

Se ele precisa trabalhar com modelagem de domínio,

08:39

ele pode consultar, por exemplo, o domainmodeling.md. Então, essa aqui é a ideia.

08:44

Então, isso vai evitar que o arquivo principal fique pesado.

08:48

Então, recapitulando rapidinho o processo. Primeiro,

08:51

definir a arquitetura base e as principais convenções do projeto. Depois,

08:55

crie um esqueleto principal incluindo o endpoint de health

08:58

que vai validar não só o web server,

09:00

mas também os serviços críticos. Em seguida,

09:02

transforme as decisões em uma skill de forma

09:05

objetiva com as principais regras e guidelines.

09:08

Depois, use a IA em modo exploratório para levantar os detalhes,

09:13

refinar as decisões para gerar o primeiro draft. Revise esse draft com cuidado,

09:17

procurando inconsistências e ambiguidades. Por fim, mova os exemplos longos.

09:23

templates e aprofundamentos para dentro de uma pasta de referências.

09:26

Esse é o primeiro passo para a gente criar a skill,

09:29

inclusive um scaffolding que vai ser útil no dia a dia,

09:35

porque você já bem sabe, toda vez que você vai começar um projeto,

09:38

você não vai dar um arquivo novo, você vai ter uma base,

09:41

um scaffolding, ou seja, um template base para você começar.

09:44

E por isso que esse template inicial que eu falei para vocês, ele vai ajudar,

09:48

porque depois a gente pode portar ele para dentro da skill.

09:52

Para quando a gente rodar,

09:53

ele já criar toda a estrutura automática do projeto para a gente.

09:56

Beleza? Então, vamos nessa para o próximo vídeo.

## Resumo IA

**Abreviações**
*   **DDD**: Domain-Driven Design
*   **IA**: Inteligência Artificial
*   **MD**: Markdown (formato de arquivo de texto simples)
*   **MVC**: Model-View-Controller

**Resumo**
O objetivo desta aula é capacitar os alunos a criar "skills" para um agente de IA, permitindo-lhes codificar decisões arquiteturais e padrões de projeto para qualquer stack ou arquitetura, garantindo independência e adaptabilidade. A aula enfatiza que uma skill não cria a arquitetura, mas a transforma em instruções reutilizáveis para o agente.

Os conceitos e ferramentas abordados incluem:
*   **Definição da Arquitetura Base**: Antes de qualquer skill, é crucial definir a arquitetura (ex: Clean Architecture, DDD, arquitetura hexagonal, MVC, modular, microservices), suas camadas, componentes, regras de dependência, bibliotecas padrão, organização de pastas, criação de módulos e estratégia de testes.
*   **Esqueleto Funcional e Health Check**: O ponto de partida é um esqueleto funcional ("hello world") que rode de ponta a ponta, incluindo um endpoint `/health`. Este health check deve validar não apenas o web server, mas também dependências críticas como banco de dados, mensageria, cache, storage e serviços externos, permitindo ao agente verificar o ambiente operacional.
*   **Arquivo `skill.md`**: Este é o arquivo principal da skill, que concentra as regras essenciais. Ele deve registrar a filosofia da arquitetura, convenções, responsabilidades por camada, regras invioláveis, formatos canônicos de artefatos, nomenclatura, validação e um índice de referências. O `skill.md` deve ser objetivo e conciso.
*   **Uso da IA em Modo Exploratório**: Em vez de redigir a skill manualmente, a IA pode ser usada para entrevistar o usuário sobre a stack, módulos, camadas, entidades, casos de uso, handlers, validação, processo de subida do ambiente, health check e regras inquebráveis. Isso ajuda a transformar conhecimento tácito em requisitos organizados para a skill.
*   **Geração e Revisão do Draft**: A IA gera um primeiro draft da skill com base na entrevista e no esqueleto. Este draft exige revisão cuidadosa para identificar ambiguidades, conflitos, excesso de detalhes ou inconsistências com a estrutura real do projeto. O próprio agente pode ser solicitado a realizar essa revisão.
*   **Organização de Referências**: Detalhes extensos, exemplos longos e aprofundamentos específicos devem ser movidos para arquivos de apoio (ex: `anti-patterns.md`, `authorization.md`, `domain modeling.md`) em pastas de referências. Isso mantém o `skill.md` enxuto e modular.
*   **Scaffolding e Templates**: Um template base de projeto (scaffolding) pode ser incorporado à skill, permitindo que o agente gere automaticamente a estrutura inicial de novos projetos, alinhando-se aos padrões estabelecidos.

O fluxo prático explicado pelo instrutor envolve os seguintes passos: (1) Definir a arquitetura base; (2) Criar um esqueleto funcional com health check robusto; (3) Registrar as guidelines no `skill.md` de forma objetiva; (4) Usar a IA para levantar requisitos e refinar decisões; (5) Gerar e revisar o primeiro draft da skill; e (6) Organizar referências externas para modularidade. Por fim, o scaffolding inicial do projeto pode ser portado para a skill, transformando-a em um mecanismo de reprodução de padrões.

**Pontos de atenção**
*   **A Skill Codifica, Não Cria Arquitetura**: A skill não inventa uma arquitetura madura; ela apenas codifica as decisões arquiteturais que já foram definidas previamente pela equipe.
*   **Health Check Abrangente**: O endpoint `/health` deve validar não só o web server, mas também *todas* as dependências críticas do sistema (banco de dados, mensageria, cache, serviços externos). Isso é fundamental para o agente diferenciar uma aplicação operacional de um processo apenas iniciado e é uma peça operacional vital para o harness do agente.
*   **Objetividade no `skill.md`**: O arquivo `skill.md` deve ser conciso e objetivo, fornecendo contexto suficiente sem se tornar um manual exaustivo. Evite que ele cresça demais (manter por volta de 500 linhas é uma boa prática), pois isso compromete a clareza e a consistência da aplicação pelo agente.
*   **IA como Entrevistadora**: Utilize a IA em modo exploratório para extrair requisitos e detalhes do projeto, transformando conhecimento tácito da equipe em informações organizadas para a skill, ao invés de redigir tudo manualmente.
*   **Revisão Crítica e do Agente**: Nunca aceite o primeiro draft da skill automaticamente. Revise-o cuidadosamente em busca de ambiguidades, conflitos, excesso de detalhes e incompatibilidades. Uma boa prática é pedir ao próprio agente para revisar a skill, procurando falhas como regras difíceis de seguir ou instruções repetidas.
*   **Modularização com Referências**: Mova exemplos longos, templates e aprofundamentos para arquivos de apoio em uma pasta de referências. Essa modularização mantém o núcleo da skill enxuto e permite ao agente consultar informações específicas conforme a necessidade, evitando que o arquivo principal fique pesado.
*   **Scaffolding na Skill**: Incorpore o scaffolding (template base) do projeto à skill. Isso permite que o agente gere automaticamente a estrutura inicial de novos projetos de forma consistente e alinhada aos padrões definidos.