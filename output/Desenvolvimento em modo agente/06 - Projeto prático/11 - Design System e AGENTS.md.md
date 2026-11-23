Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17974)

## Resumo da aula

Exports do Cloud Design transformam referência visual em contexto explícito para o agente. Aqui, dois arquivos cumprem papéis diferentes: um HTML autocontido com os tokens de design e outro com as páginas já desenhadas. Retomando o uso de design system e artefatos visuais já estabelecido, a novidade está em empacotar essas referências em arquivos consultáveis diretamente durante a implementação. Isso reduz a necessidade de inferir cores, estilos e estrutura de tela a partir de descrições vagas.

O arquivo de tokens funciona como uma fonte única para cores e demais definições visuais do sistema. Como ele é autocontido em HTML, o agente consegue consultar esse conteúdo sem depender de ferramentas externas ou de navegação adicional. Isso torna os tokens utilizáveis na geração de páginas, componentes e elementos visuais com menos ambiguidade. Em vez de “inventar” estilos, o agente passa a operar sobre um conjunto explícito de decisões de design.

O arquivo com as páginas desenhadas serve como referência estrutural para construir as próximas telas. Lembra das screenshots e referências visuais já usadas como guidance? Aqui essa ideia evolui para um catálogo navegável de páginas prontas, que orienta layout, hierarquia e consistência entre telas novas e existentes. O agente deixa de compor a interface apenas por heurística e passa a seguir um padrão visual previamente materializado.

O AGENTS.md deixa de conter apenas regras gerais do projeto e passa a incluir orientação operacional específica para front-end. Nesse caso, ele aponta onde estão os tokens, onde estão as páginas de referência e qual skill deve ser usada para implementar a interface. Isso concentra, em um único ponto, o contexto necessário para a geração de UI. O efeito prático é restringir a liberdade do agente em favor de maior previsibilidade visual.

A skill de Tailwind CSS funciona como camada especializada de orientação para a implementação visual. Em vez de depender apenas do conhecimento genérico do modelo sobre Tailwind, o agente recebe uma referência explícita de como aplicar essa stack no projeto. Isso é especialmente útil quando se quer padronizar a forma de compor classes utilitárias e evitar soluções inconsistentes entre arquivos. A skill complementa os artefatos visuais: um lado informa o que construir, o outro orienta como construir.

A orientação para usar sempre classes do Tailwind e tipos primitivos impõe um estilo de implementação mais disciplinado. O objetivo não é apenas preferência estética de código, mas controle de variabilidade: quanto menos CSS ad hoc, menor a chance de divergência visual e acúmulo de exceções locais. Essa regra também reduz a tendência de concentrar estilos improvisados em global.css, que costuma virar um ponto de desorganização quando cresce sem critério. O agente passa, assim, a montar a interface dentro de um vocabulário visual mais restrito e reutilizável.

Evitar raw CSS é uma restrição deliberada para conter deriva de implementação. Quando o agente escreve CSS livremente, ele tende a criar regras locais, duplicar decisões de estilo e escapar do design system. Ao limitar essa possibilidade, o projeto força a reutilização de tokens, utilitários e convenções já definidas. A consequência é menos flexibilidade imediata, mas mais consistência e manutenção mais simples.

Essas instruções não garantem acerto total; elas aumentam a probabilidade de resultados aceitáveis. Retomando a lógica de harness engineering já discutida, o papel dessas barreiras é cercar o espaço de decisão do agente para que ele erre menos e de forma mais controlada. Se a saída visual continuar ruim, o caminho não é abandonar a abordagem, mas refinar os artefatos, a skill e as instruções do AGENTS.md. O processo é iterativo: guidance bom nasce de observação, correção e novo teste.

## Transcrição

00:00

Bom, pessoal, continuando essa parte de UI, se você percebeu o que eu fiz.

00:06

Eu fui lá no Cloud Design e exportei dois arquivos,

00:10

no caso. Um arquivo foi os meus arquivos de token,

00:14

onde eu consigo ver, de fato, todos aqueles...

00:20

documentos, as cores, etc. É um arquivo HTML autocontido, né?

00:25

Então, com um único arquivo você consegue pegar tudo.

00:28

E também um arquivo de páginas,

00:30

onde tem todas aquelas páginas lá que eu mostrei pra você.

00:34

Então, essa aqui é a... Deixa eu ver se eu consigo colocar aqui o...

00:37

abrir open browser aqui pra gente. Ah, ele não tá conseguindo pegar aqui.

00:42

Deixa eu pegar o caminho correto desse cara.

00:46

Bom, independente disso, é aquela página que eu acabei mostrando para vocês. Então,

00:51

isso aqui ele vai usar como guia para criar as próximas páginas ali para a gente.

00:56

No agents.umd, o que eu fiz é,

00:58

ainda mais se você é uma pessoa que entende mais ainda de Tailwind,

01:02

CSS, etc., você pode melhorar bastante.

01:05

Mas o que acontece? Eu estou usando uma skill chamada Tailwind CSS,

01:09

você pode ir lá no skills.sh.

01:13

fazendo que ele utilize essa skill como guidance.

01:16

Falei que os tokens estão naquela pasta que eu passei para você,

01:21

para ele desenvolver qualquer página, componente, visual ou elemento.

01:25

Coloquei também que as páginas já estão

01:27

desenhadas e estilizadas aqui nesse endereço,

01:30

onde tem todas as páginas desenhadas,

01:32

e que a estilização do Tailwind usa sempre as classes e os tipos primitivos.

01:39

A não escrever raw CSS, para não ter um monte de CSS num arquivo só,

01:44

e evitar colocar um monte de coisa lá naquele global.css,

01:48

e aí você pode ir melhorando conforme você vai tendo o resultado ali do front-end.

01:53

Mas o ponto principal aqui é, eu agora,

01:56

eu tentei cercar um pouco mais a forma de como

01:59

que ele vai produzir toda essa parte de design,

02:02

e a gente vai vendo ao longo do tempo.

02:05

Como é que isso vai ficando, se a gente vê que não tá legal,

02:07

que ele não tá conseguindo seguir, a gente vai modificar.

02:10

O interessante de A é que eu tô gravando esse curso, né, esses vídeos pra você,

02:14

mas nem eu mesmo sei qual que vai ser a saída disso do que eu tô colocando.

02:18

O que eu sei é que eu tô criando algumas barreiras

02:22

que vão maximizar a chance dessas coisas darem certo.

02:25

Mas nem sempre elas vão dar 100%,

02:27

e a gente vai ajustando conforme as coisas vão andando. Fechou? Então, vamos nessa.

## Resumo IA

**Abreviações**
*   **UI**: User Interface
*   **HTML**: HyperText Markup Language
*   **CSS**: Cascading Style Sheets
*   **AI**: Artificial Intelligence

**Resumo**
O objetivo da aula é transformar referências visuais em um contexto explícito e consultável para o agente de desenvolvimento, visando aumentar a previsibilidade e consistência na geração de interfaces de usuário (UI). Para isso, o instrutor demonstra o uso de exports do Cloud Design, gerando dois arquivos: um HTML autocontido com os tokens de design (cores e definições visuais) e outro com as páginas já desenhadas, servindo como catálogo estrutural.

O fluxo explicado consiste em:
1.  **Exportação de Artefatos Visuais:** Do Cloud Design, são exportados um arquivo HTML de tokens (fonte única para o design system) e um arquivo HTML com as páginas já desenhadas (referência estrutural e de layout). Estes arquivos são autocontidos e diretamente consultáveis pelo agente, reduzindo a necessidade de inferir estilos.
2.  **Configuração do AGENTS.md:** Este arquivo é atualizado para incluir orientação operacional específica para front-end. Ele aponta para a localização dos tokens e das páginas de referência, e especifica qual skill (habilidade) deve ser utilizada para a implementação da interface. Isso concentra o contexto necessário em um único ponto, restringindo a liberdade do agente em prol de maior previsibilidade visual.
3.  **Utilização de Skill Especializada:** Uma skill de Tailwind CSS é usada para fornecer orientação explícita sobre como aplicar essa stack no projeto, padronizando a composição de classes utilitárias e evitando inconsistências. Essa skill complementa os artefatos visuais, informando "o que construir" e "como construir".
4.  **Imposição de Boas Práticas de Código:** Instruções são dadas para que o agente utilize sempre classes do Tailwind e tipos primitivos, e evite escrever CSS "raw" (puro) ou estilos improvisados no `global.css`. Isso visa um estilo de implementação mais disciplinado, controlando a variabilidade e prevenindo a criação de regras locais e a duplicação de decisões de estilo.

Em suma, a aula demonstra como "cercar" o espaço de decisão do agente com barreiras explícitas, refinando a abordagem de harness engineering para maximizar as chances de resultados visuais aceitáveis, embora o processo seja iterativo e requeira ajustes contínuos dos artefatos e instruções.

**Pontos de atenção**
*   **Evitar inferência e "invenção" de estilos:** A criação de referências explícitas (tokens e páginas desenhadas) é crucial para que o agente não precise adivinhar cores, estilos ou a estrutura da tela a partir de descrições vagas ou heurísticas.
*   **Fonte única da verdade:** O arquivo de tokens autocontido em HTML serve como a fonte definitiva para todas as definições visuais, prevenindo divergências.
*   **Restrição de liberdade para previsibilidade:** O AGENTS.md e as regras impostas visam restringir a liberdade do agente em favor de uma maior previsibilidade e consistência visual na geração da UI.
*   **Padronização na implementação:** O uso de uma skill de Tailwind CSS e a instrução para usar apenas classes e tipos primitivos visam padronizar a forma de construir classes utilitárias e evitar soluções inconsistentes.
*   **Controle da variabilidade:** A imposição de evitar "raw CSS" e não sobrecarregar o `global.css` é uma restrição deliberada para conter a deriva de implementação, que pode levar a CSS ad hoc, duplicação de decisões de estilo e escape do design system.
*   **Processo iterativo e não garantido:** As instruções e artefatos não garantem um acerto de 100%, mas aumentam a probabilidade de resultados aceitáveis. Se a saída visual não for satisfatória, a abordagem não deve ser abandonada, mas sim refinada (artefatos, skill, AGENTS.md) de forma iterativa, seguindo a lógica de harness engineering.