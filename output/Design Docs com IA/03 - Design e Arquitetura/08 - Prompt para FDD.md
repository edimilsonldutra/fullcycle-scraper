Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17059)

## Resumo da aula

O template do FDD funciona como um contrato de completude: ele define quais partes mínimas precisam existir para que o documento seja útil como especificação, mesmo antes de estar perfeito. O valor principal não está só em formatar a saída, mas em impedir que contratos, comportamento, dependências e critérios importantes fiquem implícitos ou esquecidos. Quando a IA recebe esse template como estrutura de saída, ela não escreve livremente; ela preenche um espaço técnico já delimitado. Isso aumenta consistência entre documentos e torna o draft mais revisável.

As perguntas do prompt não servem apenas para conduzir uma entrevista; elas funcionam como checklist de definição da feature. Mesmo sem usar o fluxo interativo, você ainda precisa responder essas perguntas em algum formato, porque são elas que revelam lacunas de escopo, comportamento e integração. Por isso, o prompt tem valor mesmo quando não é executado literalmente: ele explicita o que precisa ser decidido. Ler as perguntas com atenção é uma forma de validar se a feature já está suficientemente definida para virar FDD.

A codebase entra como contexto adicional quando o conhecimento necessário para especificar a feature não está todo no PRD, no HLD ou na memória de quem escreve. Trechos de código, contratos existentes, convenções internas e estruturas reais do projeto ajudam a IA a produzir um draft mais aderente ao sistema que já existe. Isso reduz respostas genéricas e aproxima o documento do ambiente real da empresa. O uso da codebase não substitui decisão técnica, mas melhora a precisão do ponto de partida.

Retomando o fluxo já conhecido, o FDD pode nascer de múltiplos insumos combinados: template, HLD, PRD, respostas da entrevista e contexto adicional do projeto. O documento pode existir sozinho, mas a qualidade do rascunho aumenta quando a IA recebe também os artefatos que já fixaram arquitetura e objetivos de negócio. No exemplo do rate limiter, isso significa aproveitar o que já foi decidido e usar o template para detalhar a feature sem recomeçar do zero. A combinação de insumos transforma geração em composição guiada, não em improviso.

A IA é mais confiável como geradora de rascunho do que como autora final autônoma do FDD. Ela acelera a estruturação inicial, preenche seções recorrentes e organiza o conteúdo em um formato útil para revisão, mas continua dependente de contexto suficiente e validação humana. Em ambientes reais, informações específicas da empresa, restrições locais e exemplos concretos quase sempre exigem complementação manual. O objetivo correto é sair do zero para um draft útil, não automatizar a decisão técnica inteira.

O workflow prático segue uma sequência simples: reunir insumos, usar o template e as perguntas como guia, gerar um draft e revisar o resultado. Se a entrevista for útil, ela ajuda a coletar respostas; se for mais lento do que escrever diretamente, o mesmo template pode ser preenchido com contexto já preparado. Esse fluxo é flexível porque o centro do processo não é a entrevista em si, mas a qualidade dos insumos e da estrutura de saída. A revisão humana fecha o ciclo, corrigindo suposições e adicionando o que só o contexto da empresa pode fornecer.

Retomando o cenário do rate limiter, a camada nova aqui não é redefinir a feature, mas gerar sua especificação detalhada com apoio da IA. Em vez de depender apenas de perguntas soltas, você pode anexar o HLD já existente, o PRD correspondente, trechos da codebase e o template do FDD para pedir um draft inicial. Se preferir, pode até pular a entrevista e usar diretamente o esqueleto de saída como instrução de preenchimento. O resultado esperado é um documento próximo do que a empresa precisa, mas ainda tratado como rascunho a ser refinado.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente falou sobre o nosso Feature Design Doc, e aqui é um prompt para te ajudar, de forma geral, a conseguir fazer com que você tenha uma entrevista que te ajude também a gerar esse tipo de documento.

00:20

Mas, novamente, pessoal, eu não acredito que é apenas como uma simples entrevista que você consiga detalhar tudo o que precisa. Então, você pode sim responder esse tipo de entrevista, vai te ajudar a gerar um draft desse documento.

00:35

provavelmente você sempre vai ter que adicionar mais informações, você sempre vai ter que trazer mais exemplos, provavelmente você vai ter que trazer mais contexto, você pode pegar o projeto atual, você pode pegar arquivos do seu CodeBase e talvez você possa colocar no contexto, tudo isso para fazer com que

00:58

tanto esse prompt quanto o documento final, ele seja gerado da forma mais completa e do nível que faz mais sentido para você. Por que eu estou dizendo isso? Porque esse documento pode existir sozinho ou ele pode, por exemplo,

01:16

a depender de um high-level document que você pode anexar junto, ou até mesmo uma PRD que foca mais em negócio e no produto, tá? Então, a ideia é essa. Então, eu tenho os princípios da entrevista e aqui tem as informações que são basicamente aquelas... as sessões que a gente precisa.

01:35

Então, ele vai fazer sempre suposições, ele vai adicionar detalhes, ele vai nos ajudar a fazer o nosso processo de entrevista, e aí tem a estrutura em Jason, desse camarada, e aqui está o esqueleto de saída. Então, é basicamente esse esqueleto aqui,

01:52

que é o que faz a gente conseguir ter um documento parecido com aquele que eu acabei te mostrando. Então, se você olhar, aqui está a mensagem para o usuário, quer que eu gere o arquivo MD também, etc. Então, o que acontece?

02:08

Esse esqueleto, na minha opinião, é uma das partes, entre aspas, mais importantes desse prompt. Por quê? Porque caso você não queira partir de um prompt para ficar sendo entrevistado, para ele gerar esse documento de saída, o que você pode fazer é pegar esse... é pegar esse... como que eu digo?

02:30

esse esqueleto, trazer os contextos que você quer e pedir pra ele começar a gerar o draft também pra você a partir desse template, porque também às vezes acaba conseguindo ser mais rápido. Eu vou fazer isso um pouco com vocês daqui a pouco na prática, porque eu não quero apenas ficar mostrando documentos pra você, mas eu acho que na prática vai conseguir

02:55

você ter uma ideia um pouco melhor de como que uma pesquisa bem feita ou com outros documentos possam fazer com que a gente chegue em documentos muito próximos daquele que você vai precisar ali na sua empresa, tá? Então, de forma geral, tá aqui o prompt, pelo menos pra que você tenha acesso a tudo isso, mas, novamente, tá? Eu quero trazer mundo real aqui pra vocês, pessoal.

03:22

o modelo de saída e a forma desse template de saída, ele acaba sendo muito maior ou melhor do que essa própria entrevista. E uma outra coisa, toda hora que você for pensar em fazer esse documento e não for usar esse prompt para ser entrevistado, olhe as perguntas que estão...

03:40

nessa entrevista, que provavelmente você vai ter que responder de qualquer forma, baseado em texto, colocando o conteúdo dentro daquele template, porque são essas perguntas que vão ajudar a definir essa feature. Então, eu vou dar um exemplo para vocês. Para mim, é mais importante eu conseguir ler e entender o que eu tenho que colocar, porque aqui acaba virando uma checklist que você tem que ter para conseguir definir qualquer tipo de feature, entendeu? Então, olhe bem esses dados, independente se você vai usar isso como prompt ou não.

04:10

Pense em todas essas perguntas, como que isso vai conseguir te ajudar a estruturar uma feature, uma funcionalidade ou algum módulo do sistema que você vai trazer. Então é importante que você tenha isso claro, mesmo que você vai fazer isso manual no Google Docs, no Word. Como a gente utiliza bastante A, usar um template como base e saber quais são essas perguntas que a gente vai trabalhar,

04:36

acaba funcionando bem. O máximo que eu acho que, na minha opinião, você vai conseguir fazer, como são informações específicas da sua empresa, é gerar um rascunho. E esse rascunho você pode gerar sendo entrevistado, adicionando outros

04:53

outros conceitos e etc. Isso vai fazer com que você consiga trabalhar de uma forma mais clara. Beleza? Então, é isso aí. Vamos falar agora sobre pesquisa, uma Deep Research e como ela pode te ajudar no dia a dia a desenvolver esses documentos, inclusive desenvolver o seu software, também dando mais contexto para a IA.

## Resumo IA

**Abreviações**

- **FDD** — *Feature Design Doc* (Documento de Design da Funcionalidade)
- **PRD** — *Product Requirements Document* (Documento de Requisitos do Produto)
- **HLD** — *High-Level Design* (Design de Alto Nível)
- **MD** — *Markdown*
- **IA** — *Inteligência Artificial*
- **Codebase** — base de código do projeto

**Resumo**

A aula explica como usar um template de FDD como estrutura de completude para gerar especificações mais úteis e consistentes, mesmo antes do documento estar finalizado. O instrutor destaca que o valor do template não está apenas na formatação da saída, mas em garantir que aspectos essenciais como contrato, comportamento, dependências e critérios não fiquem implícitos ou esquecidos. Nesse fluxo, a IA atua como apoio para estruturar um rascunho técnico a partir de um espaço previamente delimitado, o que facilita revisão e aumenta a padronização entre documentos.

Também é mostrado que as perguntas da entrevista/prompt funcionam como um checklist de definição da feature, e não apenas como um mecanismo de coleta interativa. Mesmo quando o processo de entrevista não é usado literalmente, essas perguntas continuam relevantes porque ajudam a identificar lacunas de escopo, integração e comportamento. Por isso, ler e responder essas questões é uma forma de validar se a funcionalidade já possui informações suficientes para ser transformada em FDD.

Outro ponto central é o uso de contexto adicional, como codebase, PRD e HLD, quando o conhecimento necessário não está todo concentrado em um único artefato. Trechos de código, convenções internas e documentos de alto nível ajudam a IA a produzir um draft mais aderente ao sistema real e menos genérico. O fluxo apresentado é flexível: reunir insumos, usar o template e as perguntas como guia, gerar um rascunho e então revisar manualmente. O objetivo não é automatizar toda a decisão técnica, mas sair do zero com um documento inicial útil, especialmente em cenários como o do rate limiter, onde já existem decisões arquiteturais e de produto que precisam apenas ser detalhadas.

**Pontos de atenção**

- O prompt/entrevista sozinho não costuma ser suficiente para definir tudo; quase sempre será necessário complementar com mais contexto, exemplos e detalhes.
- A IA deve ser tratada como geradora de rascunho, não como autora final autônoma do FDD.
- Informações específicas da empresa, restrições locais e exemplos concretos normalmente exigem validação e ajuste manual.
- O template de saída é um elemento crítico: ele orienta a completude do documento e pode ser mais importante do que a entrevista em si.
- As perguntas do prompt devem ser lidas como checklist obrigatório de definição da feature, mesmo quando o preenchimento for manual.
- O FDD pode ser produzido com múltiplos insumos combinados; quanto melhor o contexto fornecido, mais aderente será o draft.
- Codebase, PRD e HLD não substituem decisão técnica, mas aumentam bastante a precisão inicial do documento.
- O uso prático recomendado é gerar um rascunho próximo do ideal e depois revisá-lo, corrigindo suposições e preenchendo lacunas.
- Em alguns casos, preencher diretamente o template com contexto já preparado pode ser mais rápido do que executar a entrevista completa.