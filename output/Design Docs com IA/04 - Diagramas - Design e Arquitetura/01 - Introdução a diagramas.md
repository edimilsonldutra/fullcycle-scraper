Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17070)

## Resumo da aula

Diagramas existem para reduzir o custo cognitivo de entender um sistema descrito em texto. Documentos técnicos acumulam regras, componentes, decisões e exceções em muitas linhas, o que dificulta perceber estrutura, dependências e fluxo de informação de forma rápida. A representação visual comprime esse volume em relações espaciais mais fáceis de inspecionar e comunicar. Isso melhora tanto a análise técnica quanto o alinhamento com time, liderança e outras áreas interessadas.

Diagramas sempre foram valiosos, mas historicamente eram caros de produzir e manter. Ferramentas específicas, metodologias mais pesadas e o esforço manual de atualização faziam muitos times desistirem ou deixarem o diagrama desatualizado pouco tempo depois. O resultado era um paradoxo comum: justamente onde a arquitetura era mais complexa, a documentação visual era a que mais faltava. Sem manutenção contínua, o diagrama deixava de esclarecer o sistema e passava a competir com a realidade.

O ponto central não é desenhar manualmente a arquitetura do zero, mas derivar o diagrama a partir da especificação que já existe. Quando High Level Design, Feature Design Docs, Low Level Design, ADRs e RFCs concentram as decisões do sistema, eles funcionam como fonte de verdade para gerar visões visuais consistentes. Isso muda o papel do diagrama: ele deixa de ser um artefato isolado e passa a ser uma projeção da documentação textual. Quanto melhor a especificação, maior a chance de produzir diagramas úteis e coerentes.

IA muda a equação porque reduz o esforço de transformar texto técnico em representação visual. Em vez de modelar cada elemento manualmente, é possível pedir que a IA extraia atores, componentes, relações e níveis de detalhe diretamente da especificação. O ganho não está apenas na velocidade inicial, mas também na manutenção: quando o projeto evolui, atualizar o documento-fonte tende a ser mais barato do que redesenhar tudo. Ainda assim, a automação não elimina validação; ela acelera a produção de um rascunho técnico revisável.

Diagramas gerados com IA não podem ser tratados como verdade automática. O modelo pode inferir relações inexistentes, omitir restrições importantes ou exagerar granularidade em pontos que não ajudam a comunicação. A revisão humana garante aderência à arquitetura real, ao vocabulário do domínio e ao objetivo do diagrama. O uso correto da IA, portanto, é assistivo: ela produz e atualiza mais rápido, mas a responsabilidade técnica continua com quem conhece o sistema.

C4 é uma forma de representar sistemas em níveis progressivos de detalhe. Seu valor está em organizar a arquitetura por camadas de granularidade, permitindo mostrar desde uma visão mais ampla até recortes muito específicos do sistema. Essa progressão ajuda a escolher o nível certo para cada conversa, evitando misturar contexto executivo com detalhe de implementação. Ao mesmo tempo, granularidade excessiva pode gerar custo e ruído, então nem todo nível precisa ser usado em todos os casos.

Mermaid segue outra lógica: em vez de priorizar uma estrutura arquitetural como o C4, ele oferece uma sintaxe textual simples para descrever diagramas diretamente em texto. Isso o torna especialmente útil em fluxos de documentação versionada, porque o diagrama pode viver no mesmo repositório e no mesmo arquivo em que a especificação é mantida. A barreira de criação é menor, o que favorece adoção no dia a dia. Em cenários em que rapidez, portabilidade e edição simples importam mais que formalismo arquitetural, Mermaid costuma ser uma escolha eficiente.

Uma vantagem prática do Mermaid é a renderização automática em ambientes que suportam Markdown enriquecido, como o GitHub. Quando o arquivo contém o bloco com a codificação Mermaid, a plataforma transforma aquele texto em diagrama visual sem exigir ferramenta externa para visualização. Isso reduz atrito operacional, facilita revisão em pull requests e mantém código, documentação e diagrama próximos. A consequência direta é que atualizar o diagrama passa a se parecer mais com editar texto do que com operar software gráfico.

C4 e Mermaid não competem necessariamente; eles resolvem problemas diferentes e podem coexistir no mesmo processo de documentação. C4 oferece uma estrutura forte para pensar níveis de abstração arquitetural, enquanto Mermaid oferece uma forma leve e textual de materializar diagramas em ambientes de documentação contínua. A combinação dos dois permite escolher a melhor representação para cada necessidade. Com IA, essa combinação fica ainda mais útil porque a mesma especificação pode originar visões distintas com menos esforço manual.

## Transcrição

00:00

Bom, pessoal, nas aulas anteriores a gente está falando sobre Design Docs, principalmente focado mais na área de Design e Arquitetura nesse momento. A gente falou sobre os documentos mais comuns que a gente acaba entrando no meio de toda essa história, a gente falou sobre High Level Design, a gente falou sobre Feature Design Docs, a gente falou sobre Low Level e também, em seguida, a gente vai chegar a falar também um pouco mais sobre ADRs de uma forma mais profunda, RFCs e etc.

00:28

Mas, uma das coisas que é muito comum na hora que você está fazendo a documentação para qualquer tipo de arquitetura e sistema, é você conseguir também representar isso de uma forma visual. Porque o que acontece é o seguinte, muitas vezes nós temos muita documentação,

00:47

Muitas vezes, a gente tem muitas linhas escritas que fazem com que as coisas fiquem um pouco mais complexas de se ver. E, normalmente, quando a gente consegue olhar isso através de uma forma visual mais clara, inclusive para compartilhar isso com o seu time, para os seus líderes, para o seu chefe, para a diretoria, etc.,

01:09

Diagramas são coisas extremamente úteis para a gente fazer no dia a dia, tá? E o grande ponto é que fazer diagrama sempre foi algo chato, a gente sempre tinha diversos tipos de ferramenta para fazer, muita metodologia e tudo mais, e isso, ao longo do tempo, foi desencorajando com que muitos projetos tivessem diagramas que pudessem realmente ajustar e dar mais clareza sobre o sistema, tá?

01:36

E, durante todo esse tempo, o que a gente começou a perceber é que existem dois tipos fundamentais de formas de você apresentar informação nos dias de hoje que são bem populares, tá? Uma é um pouco mais popular que a outra porque é mais nova, mas, de forma geral, diagramas sempre foram coisas importantes no passado e até hoje é importante.

02:02

E o grande ponto é que, nesse capítulo especificamente, nós vamos falar sobre diagramas, tá? Mas o grande ponto é que agora que a gente tem inteligência artificial do nosso lado, conseguir fazer a geração desses diagramas acabou ficando muito mais fácil.

02:21

muito mais rápido. E o mais interessante é que fica mais fácil de você modificar esses diagramas conforme o projeto vai evoluindo sem você ter um trabalho extremamente grande, tá? E é por isso que, nesse capítulo, a gente vai acabar falando sobre dois caras. A gente vai falar sobre diagramas C4, que são bem comuns. Eu não sei se você já teve algum contato com ele, mas é uma das formas mais

02:49

interessante de você representar um sistema e etc. Eu vou falar um pouco para vocês daqui a pouco sobre ele, mas, ao mesmo tempo, ele consegue chegar a um nível de granularidade muito grande e que, de forma geral, muitas vezes, inclusive, eu não recomendo. Mas trabalhar com o diagrama C4 realmente é algo que muda bastante o jogo para você conseguir representar o seu sistema.

03:14

E outros diagramas que a gente tem, eles acabam entrando numa categoria um pouco diferente do C4, que são diagramas Mermaid. Em grande parte, o ponto interessante desses diagramas é que eles são muito fáceis de você criar, e hoje em dia eles são renderizáveis automaticamente quando você tem arquivos Markdown. Então, se você sobe um arquivo Markdown que tem ali

03:44

a codificação em mermaid, simplesmente lá no seu GitHub esse diagrama já vai aparecer automaticamente. Então, durante esse capítulo, a gente vai falar sobre esses diagramas, lembrando que o meu objetivo aqui não é ensinar C4 pra você, não é ensinar mermaid pra você, a gente vai passar sobre esses aspectos principais,

04:06

Mas o meu ponto aqui é como que a gente consegue transformar a especificação que a gente já tem em diagramas de uma forma automática, de uma forma mais apurada, utilizando inteligência artificial. Obviamente, tudo sempre tem que ser revisado e etc., mas você vai ver que IA nesse aspecto muda bastante o jogo. Então, vamos lá, porque tem bastante coisa para a gente ver nesse capítulo.

## Resumo IA

**Abreviações**

- **IA** — Inteligência Artificial
- **HLD** — High Level Design
- **FDD** — Feature Design Docs
- **LLD** — Low Level Design
- **ADRs** — Architecture Decision Records
- **RFCs** — Request for Comments
- **C4** — Modelo C4 de diagramas arquiteturais
- **Markdown** — linguagem de marcação leve para formatação de texto

**Resumo**

A aula explica que diagramas são essenciais para reduzir o custo cognitivo de entender sistemas e arquiteturas descritos em texto, pois transformam longas especificações em uma representação visual mais fácil de analisar, comunicar e alinhar com diferentes públicos, como time, liderança e diretoria. O instrutor destaca que, apesar de úteis, diagramas historicamente eram difíceis de produzir e manter, o que fazia muitos projetos ficarem sem documentação visual atualizada. A proposta central da aula é inverter esse fluxo: em vez de desenhar tudo manualmente, usar a especificação já existente como fonte de verdade para derivar diagramas consistentes.

Nesse contexto, são mencionados documentos técnicos como High Level Design, Feature Design Docs, Low Level Design, ADRs e RFCs, que concentram decisões e detalhes do sistema e podem ser usados como base para geração automática de visões visuais. A aula enfatiza que a inteligência artificial altera esse cenário ao facilitar a extração de atores, componentes, relações e níveis de detalhe diretamente do texto técnico, acelerando tanto a criação quanto a atualização de diagramas conforme o projeto evolui. Ainda assim, a IA é apresentada como assistiva: ela produz um rascunho técnico, mas a revisão humana continua obrigatória para garantir fidelidade à arquitetura real e ao vocabulário do domínio.

O instrutor também apresenta dois estilos de diagramas abordados no capítulo. O primeiro é o C4, que organiza a arquitetura em níveis progressivos de detalhe e ajuda a escolher a abstração adequada para cada necessidade, evitando misturar visão executiva com detalhe de implementação. O segundo é o Mermaid, que usa uma sintaxe textual simples para descrever diagramas diretamente em arquivos de documentação, especialmente em Markdown, o que facilita versionamento, edição e renderização automática em plataformas como o GitHub. A aula reforça que C4 e Mermaid não são excludentes: eles atendem objetivos diferentes e podem coexistir, com a IA ajudando a transformar a mesma especificação em representações diversas com menos esforço manual.

**Pontos de atenção**

- Diagramas devem ser derivados da documentação existente, e não tratados como artefatos isolados sem vínculo com a fonte de verdade.
- A manutenção contínua é essencial; um diagrama desatualizado pode confundir mais do que ajudar.
- A IA acelera a geração, mas não substitui revisão técnica.
- Modelos podem:
  - inferir relações que não existem;
  - omitir restrições relevantes;
  - exagerar o nível de detalhe em pontos desnecessários.
- A responsabilidade final pela correção da arquitetura representada continua sendo humana.
- No C4, é importante escolher o nível certo de granularidade para evitar ruído e excesso de detalhe.
- Nem todo contexto exige todos os níveis do C4; usar granularidade demais pode aumentar custo sem melhorar a comunicação.
- Mermaid é mais indicado quando a prioridade é simplicidade, portabilidade, edição textual e integração com documentação versionada.
- Em Markdown com suporte a Mermaid, o diagrama pode ser renderizado automaticamente, reduzindo atrito operacional.
- C4 e Mermaid resolvem problemas diferentes; a escolha deve considerar o objetivo da documentação.
- A combinação de documentação textual bem feita, IA e diagramas adequados gera melhores resultados do que depender apenas de desenho manual.