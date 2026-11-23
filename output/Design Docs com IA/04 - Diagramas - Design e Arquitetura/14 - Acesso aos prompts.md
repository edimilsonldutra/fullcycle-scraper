Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17083)

## Resumo da aula

Centralizar os artefatos em um workspace como o Notion reduz o custo de acesso e reuso do processo de documentação. A organização útil não reúne apenas os diagramas finais, mas também os documentos-fonte e os prompts que levaram até eles, como High-Level Document, Feature Design Doc, research e instruções de geração. Isso transforma o exemplo do Rate Limiter em um pacote reaproveitável, no qual o time consegue inspecionar tanto o resultado quanto o processo. Quando os insumos e os prompts ficam lado a lado, adaptar o fluxo para outro projeto se torna muito mais rápido.

No Rate Limiter, os artefatos foram organizados por tipo de documento e por finalidade de geração. Há os documentos de definição, como HLD e FDD, os artefatos de apoio, como research, e os outputs de diagramas, como C4 e Mermaid, cada um acompanhado de seus respectivos prompts. Essa estrutura importa porque o diagrama não nasce isolado: ele depende de uma cadeia documental anterior. Reusar apenas o prompt final, sem considerar os documentos que o alimentam, tende a produzir saídas fracas ou desalinhadas.

Os prompts de C4 e Mermaid devem ser tratados como artefatos operacionais do processo, não como detalhes descartáveis. No caso do C4, o prompt acompanha o diagrama gerado e pode estar associado a um subagente e a um comando base; no caso do Mermaid, o pacote inclui tanto o subagente quanto o comando de execução. Isso permite copiar, colar e adaptar rapidamente o fluxo em Markdown, preservando o formato textual que já vinha sendo usado. O valor prático está em reduzir o trabalho de começar do zero sem prender o processo a um único modelo ou fornecedor.

Manter prompts em Markdown facilita versionamento, edição e reaproveitamento em diferentes ambientes. Como o conteúdo fica em texto puro, o desenvolvedor consegue ajustar instruções, trocar contexto e registrar variações por projeto com o mesmo cuidado aplicado a código e documentação. Retomando o uso de Mermaid já estabelecido, esse formato combina bem com fluxos em que o diagrama também é textual. O resultado é um processo mais portátil, auditável e simples de iterar.

Um prompt bem testado acelera a geração, mas não substitui definição de produto nem elimina ambiguidades do problema. Isso fica ainda mais evidente em documentos como HLD e FDD, porque eles dependem de decisões reais sobre escopo, comportamento e restrições do sistema. Se o projeto ainda não está definido, a IA não tem como inventar uma definição confiável apenas porque recebeu uma instrução sofisticada. O prompt ajuda a estruturar e acelerar, mas não resolve ausência de clareza.

Prompts reutilizáveis funcionam melhor como baseline do que como receita fixa. Mesmo quando foram testados em vários cenários e produzem bons resultados de forma geral, projetos diferentes exigem ajustes de contexto, nomenclatura, restrições e nível de detalhe. Esses refinamentos podem inclusive ser feitos com apoio da própria IA, mas continuam sendo refinamentos guiados por julgamento técnico. Reuso eficiente não significa copiar sem pensar; significa partir de uma base madura e adaptá-la ao domínio atual.

A revisão e validação continuam obrigatórias: a IA pode errar mesmo quando o resultado parece convincente e bem formatado. Essa responsabilidade cobre documentação, código, diagramas e qualquer outro artefato produzido com assistência automatizada. Em termos práticos, o profissional precisa conferir se a saída representa corretamente o sistema, se não omite restrições importantes e se não introduz suposições indevidas. A utilidade da IA aumenta a produtividade, mas não transfere a responsabilidade final de decisão e aprovação.

O fluxo prático é simples: acessar o workspace, localizar os artefatos do Rate Limiter, copiar o prompt de C4 ou Mermaid em Markdown, executar com o documento-fonte equivalente e então revisar o resultado gerado. Se o projeto tiver diferenças relevantes, o ajuste deve acontecer antes e depois da geração: antes, refinando o prompt e o contexto; depois, validando fidelidade técnica e clareza do diagrama. Esse processo conecta a teoria ao uso real dos artefatos, porque mostra que o ganho está no reaproveitamento estruturado, não na automação cega. O pacote pronto acelera a execução, mas a qualidade continua dependendo da adaptação e da revisão humana.

## Transcrição

00:01

Bom, pessoal, somente para que você possa ver e olhar aqui, eu estou deixando disponível aqui o link do Notion para vocês. E aqui, de forma geral, está a organização de High-Level Document aqui do nosso...

00:18

a Rate Limiter, o Prompt que eu utilizei, o Feature Design Doc, o Prompt também para gerar o FDD. Lembrando que esses dois caras aqui, eles são muito mais complexos para a gente gerar, porque ele fala do produto, é definição de produto. Então os Prompts, eles vão te ajudar a facilitar essa geração.

00:36

mas lembrando sempre que não existe mágica quando você está criando um produto que não tem definição, você precisa definir e esses caras não tem muito para onde fugir. Aqui também tem o documento de research, o prompt que a gente fez para documento de research, mas referente ao que a gente está falando hoje nesse capítulo são os diagramas C4, certo? Então tem o diagrama C4 do Rate Limiter, onde eu coloquei as imagens dele somente para você

01:05

ter uma visão melhor, e também o prompt para a geração desse diagrama C4, que eu coloquei do cloud sub-agent base comando, mas, como eu disse para vocês, eu não quero enviesar ninguém a utilizar o cloud, tanto que eu gerei esses diagramas hoje aqui com você, utilizando um outro modelo, beleza? E aqui eu tenho os diagramas mermaid, que eu mostro como é que ficaram os do rate limiter, e também o prompt, tanto o sub-agente quanto o comando aqui para vocês. Então, se vocês entrarem,

01:35

Está prontinho aqui para você copiar e colar em Markdown. Aqui está o agente. É grande, né, galera? E aqui está o comando que você pode utilizar para trabalhar.

01:50

Maravilha? Então, galera, espero que vocês tenham curtido esse capítulo para diagramas. Diagramas são muito importantes, principalmente quando a gente está arquitetando qualquer coisa, e sempre dão muito trabalho, e cada vez mais as pessoas pararam de utilizar.

02:11

Agora, com o IA, eu acredito que você e muitas outras pessoas vão começar a reconsiderar em utilizar, ou se você já usava, você vai poder reconsiderar se não dá pra gente fazer isso usando com o IA. Legal? E um ponto que eu queria sempre deixar claro aí pra vocês, pessoal, é que esses prompts aqui,

02:34

Estão baseados em experiências minhas, em projetos meus. Eu testei demais isso em diversos tipos de projetos e, de forma geral, eu tive diversos resultados legais. Em determinados projetos, eu tive que fazer alguns ajustes ou outros, usando o IA mesmo, mas eu tive que fazer ajustes. Por que eu estou dizendo isso? Porque esses prompts que você tem acesso, eles não são uma bala de prata.

03:00

Mas, de forma geral, ele já é um baita começo pra você não começar do zero, né, e investir um super tempo pra conseguir fazer a geração desses diagramas, tá? Então, eu acho que eles já vão te ajudar bastante e, novamente, eu gostaria de ressaltar, seja responsável com qualquer coisa que a IA gera pra você. Inteligência artificial erra.

03:26

você é a pessoa que tem responsabilidade em revisar tudo, desde a documentação, desde o seu código, desde os seus diagramas, desde tudo. Beleza? É por isso que você é contratado de forma geral, inclusive, principalmente daqui pra frente, com a entrada da inteligência artificial. Fechou? Um grande abraço pra vocês, espero que vocês tenham curtido esse capítulo e vamos pro próximo.

## Resumo IA

**Abreviações**
- **HLD** — *High-Level Document* (Documento de Alto Nível)
- **FDD** — *Feature Design Doc* (Documento de Design de Funcionalidade)
- **C4** — Modelo de diagramas de arquitetura em níveis (*Context*, *Container*, *Component*, *Code*)
- **IA** — Inteligência Artificial

**Resumo**
A aula mostrou como centralizar artefatos de documentação e arquitetura em um workspace, como o Notion, para reduzir o custo de acesso, inspeção e reuso. O instrutor organizou o caso do Rate Limiter em um pacote reutilizável contendo documentos-fonte, prompts e saídas geradas, incluindo HLD, FDD, research e diagramas. A ideia principal foi que o diagrama final não deve ser tratado como algo isolado, pois depende de uma cadeia anterior de definição e contexto. Por isso, manter juntos os insumos e os prompts facilita adaptar o fluxo para novos projetos e acelera a geração de artefatos.

A organização apresentada separa documentos por tipo e finalidade: documentos de definição, como HLD e FDD; artefatos de apoio, como research; e outputs visuais, como diagramas C4 e Mermaid, cada um com seu prompt correspondente. O instrutor destacou que os prompts de C4 e Mermaid são artefatos operacionais do processo e podem vir associados a subagentes e comandos de execução, permitindo copiar e adaptar o fluxo com facilidade, inclusive em Markdown. Esse formato textual é útil porque favorece versionamento, edição e portabilidade entre ambientes, sem prender o processo a uma ferramenta ou fornecedor específico. A proposta é reaproveitar uma base madura e ajustá-la ao contexto de cada projeto.

Também foi reforçado que prompts não substituem definição de produto. Em documentos mais complexos, como HLD e FDD, ainda é necessário tomar decisões reais sobre escopo, comportamento e restrições; se essas definições não existirem, a IA não consegue inventá-las com confiabilidade. Assim, os prompts funcionam como aceleradores e estruturadores, mas não eliminam ambiguidades nem resolvem ausência de clareza. O fluxo prático descrito foi: acessar o workspace, localizar os artefatos do Rate Limiter, copiar o prompt adequado em Markdown, executá-lo com o documento-fonte correspondente e revisar cuidadosamente o resultado. Se houver diferenças relevantes no projeto, o ajuste deve ser feito antes da geração, refinando contexto e instruções, e depois, validando a fidelidade técnica e a clareza do diagrama.

**Pontos de atenção**
- Prompts reutilizáveis não são “bala de prata”; funcionam melhor como base inicial do que como receita fixa.
- Projetos diferentes exigem ajustes de contexto, nomenclatura, restrições e nível de detalhe.
- HLD e FDD dependem de definição real de produto; se o escopo não estiver claro, a IA não cria uma definição confiável sozinha.
- Diagramas não devem ser gerados a partir de um prompt isolado: os documentos-fonte anteriores importam muito para a qualidade da saída.
- É importante manter prompts e artefatos em texto puro/Markdown para facilitar versionamento, edição e reaproveitamento.
- A IA pode gerar saídas convincentes e ainda assim erradas; sempre revisar documentação, código e diagramas.
- O profissional continua responsável por confirmar se o artefato representa corretamente o sistema e não omite restrições importantes.
- O ganho real vem do reuso estruturado e da adaptação consciente, não da automação cega.