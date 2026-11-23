Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17777)

## Resumo da aula

A especificação técnica nasce do PRD da feature e transforma intenção de produto em decisões implementáveis. Retomando o PRD já definido anteriormente, o Spec Writer usa esse documento como insumo principal para entender capacidades, experiência esperada e restrições da feature. O resultado não é apenas um resumo técnico: ele inicia um processo de refinamento que força escolhas de stack, estrutura e comportamento. Isso reduz ambiguidade antes da implementação e melhora a previsibilidade do desenvolvimento por agentes.

Antes de aprofundar a especificação, a ferramenta inspeciona o diretório do projeto e identifica o estado da codebase. Quando o cenário é Greenfield only com apenas um PRD, a especificação parte quase inteiramente do documento de produto e das decisões tomadas na entrevista técnica. No exemplo da feature 01, a landing page é classificada como foundation feature, porque estabelece uma base pública inicial que influencia o restante do sistema. Essa classificação importa porque certas decisões, como framework e estrutura de rotas, tendem a propagar impacto para outras features.

O primeiro artefato útil da geração é um sumário técnico curto, que consolida o que a feature precisa entregar em termos operacionais. No caso da landing page, isso inclui ser uma página pública em /, expor CTA de Create Account, oferecer login e descrever o fluxo principal do produto. Esse sumário funciona como uma ponte entre o PRD e a entrevista: ele confirma o entendimento inicial antes de entrar em decisões de arquitetura. Se esse entendimento estiver errado, o erro é corrigido cedo, quando o custo de ajuste ainda é baixo.

A entrevista técnica não se limita a coletar respostas; ela propõe alternativas concretas e recomendações de implementação. Em vez de perguntar apenas “qual stack usar?”, ela pode sugerir Next.js, App Router, TypeScript e React 19, além de registrar alternativas consideradas. Esse formato acelera decisão porque o usuário responde sobre opções plausíveis, não sobre um espaço totalmente aberto. O efeito prático é transformar a coleta de requisitos técnicos em uma sessão guiada de design.

A recomendação da ferramenta não é imposição. Mesmo que ela sugira Next.js 15, a decisão final pode ser outra, como Go, Java ou uma versão diferente do próprio Next.js. O valor da entrevista está em tornar essa escolha explícita e rastreável dentro da especificação, em vez de deixá-la implícita no código. Isso é especialmente importante em features de foundation, nas quais uma decisão inicial errada pode contaminar múltiplos layers depois.

Depois da escolha macro de stack, a entrevista aprofunda detalhes estruturais, como uso de Global CSS, Tailwind e organização de módulos. Lembra da especificação como base do desenvolvimento: aqui ela deixa de ser apenas funcional e passa a capturar convenções arquiteturais que orientarão a implementação. Cada resposta reduz espaço de interpretação da IA e melhora a consistência entre sessões futuras. Quanto maior a profundidade desse refinamento, menor a chance de decisões arbitrárias durante a geração de código.

Uma das partes mais valiosas da entrevista é a exploração de edge cases. Perguntas condicionais do tipo “se isso acontecer, o que deve ocorrer?” revelam comportamentos que normalmente ficariam implícitos ou seriam descobertos tarde demais. Esse tipo de detalhamento expõe requisitos arquiteturais e operacionais que o autor da feature muitas vezes não formularia sozinho. Em SDD, edge case não é detalhe periférico; é parte do contrato que define como a IA deve agir diante de variações reais do sistema.

A clareza do desenvolvimento por IA depende diretamente da profundidade da especificação. Se a entrevista for superficial, a implementação terá mais lacunas para preencher por inferência; se for profunda, o agente recebe um mapa muito mais preciso do que construir. Isso não elimina a necessidade de revisão, mas desloca a maior parte das decisões para um momento controlado, antes do código. O ganho principal é previsibilidade: fica mais claro por que a IA implementará de um jeito e não de outro.

## Transcrição

00:00

Bom, pessoal, que nem o vídeo anterior, como eu falei para vocês,

00:04

vamos nessa aqui para gerar a nossa especificação. O que eu quero fazer aqui,

00:10

basicamente, é eu vou colocar um spec writer e eu vou falar

00:13

que eu quero gerar a especificação baseada no meu PRD da feature 01,

00:19

ok? E aqui eu vou dar um enter agora aqui para a gente e vamos ver

00:23

como é que o Cloud vai se comportar e

00:27

como que essa parada vai funcionar aqui também,

00:29

tá? Então, ó. Ele vai ler o nosso diretório,

00:33

provavelmente vai tentar entender o nosso projeto,

00:38

mas principalmente ele vai ter que ler o nosso PRD e baseado nesse

00:43

PRD ele vai entrar naquele momento onde a gente faz as entrevistas técnicas, tá?

00:48

E daí na hora que ele começar muito a entrevista técnica,

00:51

eu vou parar e vou trazer para vocês

00:55

olharem como é que ficou esse nosso primeiro arquivo,

00:59

tá? Esse arquivo é o mais simples porque é uma landing

01:01

page que não tem praticamente nada ali para a gente,

01:05

então acaba sendo ele mais tranquilo ali na hora dele ser gerado.

01:10

Então vamos só aguardar ele pensar aqui para a gente poder trabalhar.

01:22

E olha só o que ele gerou aqui de cara, olha só que interessante.

01:26

Baseado na minha análise, isso aqui é uma landing page,

01:28

que é uma feature de foundation,

01:30

e o sumário técnico aqui é... É uma página pública que não tem indicação,

01:36

que ao acessar um barra, ele vai ter uma CTA, Create Account,

01:40

vai ter um login, como que funciona e tudo mais.

01:43

O Codebase State é um Greenfield only, somente com um PRD.

01:47

O PRD foi carregado com as capacidades, experiências e etc.

01:52

E aqui ele começa com a entrevista já de cara, entendeu? E ele vai sugerir aqui,

01:58

por exemplo, o Next .js. Esse projeto pode afetar todos os layers das features.

02:03

eu posso ter uma recomendação de usar o Next. Eu poderia falar,

02:05

eu quero usar Go, posso querer usar o Next .js, eu quero poder usar Java,

02:09

não tem problema nenhum. E eu quero utilizar com App Router,

02:13

com esse padrão, usando TypeScript, com React 19 e etc.

02:19

Outras alternativas consideradas. E pergunta,

02:22

você confirma que pode ser um Next .js 15?

02:25

Eu vou colocar, eu quero o Next .js, sei lá, 16, tá? e etc.

02:33

E aí, ele vai ficar cada vez mais crítico,

02:38

né? E como é que você imagina isso?

02:40

Você vai ter um Global CSS, você vai trabalhar com Tailwind, quais são os módulos?

02:45

Ele sempre vai trazer uma recomendação ali pra você.

02:49

Eu gosto muito desse tipo de entrevista, por quê?

02:52

Porque ele faz a pergunta e ele traz alternativas pra você.

03:00

E ele traz também recomendações do que ele acha.

03:03

Ou seja, vira não só uma entrevista,

03:06

mas vira uma sessão de brainstorming aqui com você e com a gente.

03:10

E aí fica muito louco, porque no final das contas,

03:12

você tem muito mais clareza e o mais interessante

03:17

é que ele começa a perguntar muito sobre edge cases.

03:21

Se acontecer isso, o que você faz?

03:24

Mas se acontecer isso e você começa a ter acesso...

03:28

a perguntas e a detalhes arquiteturais que raramente você mesmo iria pensar.

03:34

E como isso acaba dependendo do nível de profundidade que você quiser ir até o fim,

03:39

cada vez mais fundo,

03:41

isso vai ficar muito,

03:43

mas muito mais claro de como que a IA vai desenvolver o seu projeto.

03:48

Então, novamente, eu poderia passar aqui meia hora,

03:51

o tempo que fosse necessário para fazer a geração dessa feature.

03:55

Então, o que eu vou fazer, eu vou fazer igual eu fiz com o PRD,

03:58

pra gente não ficar até amanhã aqui,

04:00

porque daí a gente já consegue ir um pouco mais pra prática.

04:03

Fechou? Então, vamos nessa, galera!

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirement Document
*   **CTA**: Call to Action
*   **IA**: Inteligência Artificial
*   **SDD**: Software-Defined Design
*   **CSS**: Cascading Style Sheets

**Resumo**
A aula aborda o processo de geração de uma especificação técnica a partir de um PRD (Product Requirement Document), transformando intenções de produto em decisões implementáveis. O objetivo é reduzir a ambiguidade antes da implementação e melhorar a previsibilidade do desenvolvimento, especialmente quando realizado por agentes de IA.

O processo começa com o `Spec Writer`, que utiliza o PRD como insumo principal para entender as capacidades, a experiência esperada e as restrições da feature. A ferramenta inspeciona o diretório do projeto para identificar o estado da codebase; em cenários `Greenfield only` (apenas com um PRD), a especificação parte majoritariamente do documento de produto.

Um primeiro artefato gerado é um sumário técnico curto, que consolida os requisitos operacionais da feature (ex: landing page pública em `/`, CTA de Create Account, login, descrição do fluxo principal). Esse sumário funciona como uma ponte entre o PRD e a entrevista técnica, confirmando o entendimento inicial e permitindo correções de baixo custo.

A seguir, a ferramenta inicia uma entrevista técnica guiada. Em vez de perguntas abertas, ela propõe alternativas concretas e recomendações de implementação para a stack tecnológica (ex: Next.js, App Router, TypeScript, React 19, ou alternativas como Go, Java). O usuário valida ou ajusta essas sugestões, tornando as escolhas explícitas e rastreáveis na especificação. A entrevista aprofunda-se em detalhes estruturais, como o uso de Global CSS ou Tailwind e a organização de módulos, capturando convenções arquiteturais.

Uma parte crucial da entrevista é a exploração de `edge cases` (casos de contorno). Perguntas condicionais revelam comportamentos que poderiam ficar implícitos, expondo requisitos arquiteturais e operacionais que o autor da feature raramente formularia sozinho. Em SDD (Software-Defined Design), os `edge cases` são tratados como parte do contrato que define a ação da IA. A profundidade da especificação resultante determina a clareza e precisão com que a IA desenvolverá o projeto, deslocando as decisões para um momento controlado antes da geração do código.

**Pontos de atenção**
*   **Refinamento Precoce**: O processo de especificação força escolhas de stack, estrutura e comportamento em uma fase inicial, o que é crucial para reduzir a ambiguidade e melhorar a previsibilidade do desenvolvimento.
*   **Custo de Ajuste**: Corrigir erros de entendimento na etapa do sumário técnico é significativamente mais barato do que fazê-lo em fases posteriores, como a implementação.
*   **Impacto das Foundation Features**: Features classificadas como "foundation" (que estabelecem uma base inicial, como uma landing page) têm decisões (ex: framework, estrutura de rotas) que podem propagar seu impacto para múltiplos layers e features futuras.
*   **Decisões Explícitas e Rastreáveis**: A entrevista técnica não é impositiva. É fundamental que as escolhas (mesmo que contrárias às recomendações da ferramenta) sejam tornadas explícitas e rastreáveis na especificação. Isso evita que decisões iniciais erradas contaminem ou compliquem o sistema posteriormente.
*   **Profundidade da Especificação**: A clareza e precisão do desenvolvimento por IA dependem diretamente da profundidade e detalhamento da especificação. Uma entrevista superficial resultará em lacunas preenchidas por inferência da IA, enquanto uma especificação profunda serve como um mapa preciso.
*   **Edge Cases como Contrato**: Em Software-Defined Design (SDD), os `edge cases` não são detalhes periféricos; eles são parte integrante do contrato que define como a IA deve se comportar diante de variações e cenários incomuns do sistema.
*   **Previsibilidade do Desenvolvimento**: Uma especificação detalhada desloca a maior parte das decisões para antes do código, resultando em maior previsibilidade sobre o comportamento da IA e a forma como o projeto será construído.
*   **Não Substitui a Revisão**: Apesar da profundidade da especificação, ela não elimina a necessidade de revisão do código gerado pela IA.