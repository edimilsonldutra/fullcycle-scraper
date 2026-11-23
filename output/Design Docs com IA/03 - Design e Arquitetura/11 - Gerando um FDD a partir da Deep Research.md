Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17062)

## Resumo da aula

Um draft útil de FDD surge quando o prompt combina três artefatos com papéis diferentes: o HLD fixa as decisões arquiteturais já tomadas, o PDF de Deep Research amplia o repertório técnico com alternativas e referências, e o esqueleto do FDD define a estrutura mínima de saída. Essa composição evita pedir “um documento do zero”, porque a IA passa a preencher uma moldura com contexto real. Retomando o rate limiter, a geração deixa de depender só de entrevista e passa a reutilizar tudo o que já foi produzido no fluxo.

O prompt pode ser simples e ainda funcionar bem se o contexto estiver forte. A instrução central é pedir um Feature Design Doc para a feature alvo, informar que o HLD será fornecido, anexar a pesquisa técnica e exigir que a saída siga o esqueleto do FDD. Também vale orientar o nível de detalhe: não descer para implementação linha por linha, mas explicitar contratos, comportamento e decisões suficientes para orientar a execução.

O HLD não entra no prompt como referência decorativa; ele serve para ancorar o draft nas decisões já estabilizadas. Isso faz a IA herdar elementos como arquitetura escolhida, componentes, responsabilidades e trade-offs, em vez de reinventar a solução. No exemplo do rate limiter, é esse insumo que ajuda a saída a manter coerência com middleware, estratégias, storage e limites arquiteturais já definidos.

A pesquisa estruturada complementa o HLD porque traz detalhes que normalmente não cabem no documento arquitetural, como comparações, estratégias, referências externas e implicações operacionais. Quando esse PDF entra no mesmo prompt, a IA ganha base para enriquecer seções do FDD com maior precisão técnica. O efeito prático é um rascunho menos genérico e mais próximo de uma especificação utilizável.

O esqueleto do FDD continua sendo o mecanismo que força cobertura mínima das seções relevantes. Em vez de confiar que a IA lembrará espontaneamente de contexto, escopo, exclusões, erros, observabilidade, compatibilidade e critérios de aceite, o template transforma isso em obrigação estrutural. O resultado tende a ser mais revisável, porque a equipe consegue inspecionar lacunas por seção, não apenas pela impressão geral do texto.

Um prompt “mal feito” ainda pode produzir um draft valioso quando os insumos são bons. Isso acontece porque a qualidade da saída não depende só da redação do comando, mas da densidade e da complementaridade do contexto fornecido. A lição prática não é abandonar bons prompts, e sim entender que contexto forte reduz fragilidade e acelera a primeira versão.

Grounding é a indicação explícita de onde a IA tirou determinada informação, como trechos ou referências do PDF anexado. Isso pode poluir a leitura quando o objetivo é obter um documento mais limpo, mas é útil para auditoria, validação e revisão crítica do draft. Em fluxos de design, grounding funciona como mecanismo de rastreabilidade: ele mostra se a saída está realmente apoiada nos insumos ou se começou a improvisar.

Um draft bom não é aquele que sai perfeito, e sim aquele que evita a página em branco e já organiza o trabalho de refinamento. A revisão deve verificar aderência ao HLD, cobertura das seções do template, presença de detalhes úteis e possíveis distorções de foco, como ênfase excessiva em multi-tenant quando isso não era central. No rate limiter, a utilidade do resultado aparece quando ele já traz contratos, headers, erros, fallback, observabilidade, dependências, compatibilidade e critérios de aceite em formato editável.

A geração assistida não elimina edição humana; ela desloca o esforço de escrever tudo para revisar, corrigir, compor e ajustar. Esse ponto é essencial porque nem todas as informações virão corretas, completas ou no nível certo de detalhe. O fluxo robusto assume várias iterações curtas sobre um rascunho inicial, em vez de esperar uma geração automática definitiva.

Documentação dá trabalho, mas se torna um ativo quando passa a ser lida por pessoas e por IA ao longo do ciclo de vida do software. Um FDD inicial bem gerado acelera implementação, revisão técnica, testes, manutenção e futuras automações baseadas em contexto. Em engenharia de software, isso importa porque o desenvolvimento não termina no código: decisões, contratos e restrições precisam continuar acessíveis, atualizáveis e reutilizáveis.

## Transcrição

00:01

Bom, pessoal, o seguinte, somente para a gente conectar um pouco os pontos, tá? Eu vou fazer algumas simulações aqui, somente para você ter mais ou menos uma ideia de como que você pode fazer também para gerar esses documentos que a gente acabou falando, usando a Deep Research. Porque, inicialmente, eu cheguei, falei sobre o documento, mostrei um exemplo do documento, mostrei um prompt de entrevista para esse tipo de documento. Por outro lado,

00:26

Eu não fiquei criando esses documentos somente com aquele prompt, como eu disse, às vezes somente uma entrevista não vai resolver todo o seu problema e a gente precisa de outros recursos. Então, o que eu fiz aqui, pessoal? Eu vou pegar, por exemplo, um dos PDFs da nossa Deep Research, que a gente acabou fazendo, e também o que eu quero fazer aqui, de forma geral, é o seguinte,

00:50

eu vou pegar o feature design prompt para um FDD. Se você olhar aqui, o que eu quero fazer é, mesmo fazendo um prompt, vamos dizer, bem mal feito,

01:06

você vai entender como que isso consegue me ajudar na hora de desenvolver, por exemplo, uma especificação de uma feature. E o porquê que eu estou dizendo isso? Eu vou pegar aqui para mim o high-level design do nosso rate limiter. Vou pegar aqui o nosso high-level design.

01:27

Então, eu vou copiar esse documento porque eu quero fazer o de feature agora aqui também para mim. Então, o que vai acontecer? Eu vou chegar aqui no meu GPT e vou falar... Preciso que você crie um feature design doc para um rate limiter desenvolvido na linguagem Go. Abaixo, colocarei

01:57

um documento de High Level Design desse Rate Limiter. Também anexei um PDF com uma pesquisa completa sobre o assunto, inclusive com diversas referências e estratégias.

02:26

Preciso que você gere um documento de um FDD, um Feature Design Doc, baseado no esqueleto abaixo, usando as informações passadas.

02:56

Perceba que eu estou escrevendo, perceba, escrevi meio que da minha cabeça. Outra coisa, pense passo a passo para garantir que todas as sessões estejam completas, que esse documento não seja extremamente de baixo nível,

03:22

mas que ainda traga informações claras de implementações e seus contratos. Tá? Então, escrevi esse texto aqui. Perceba que não é o melhor prompt do mundo, mas você vai ver como que, passando o contexto, isso vai te ajudar. Então, aqui, a primeira coisa que eu vou colocar é... Vou fazer o seguinte. Vou colocar... Hi...

03:52

Level Design. E eu vou copiar o documento de High Level, de Rate Limiter aqui pra mim. Vamos copiar esse cara e vamos colar aqui no nosso amigo GPT, tá aqui o nosso High Level Design. Agora, aqui eu vou colocar, vou fazer mais um tracinho, e vou colocar modelo de saída para o Feature

04:24

design.doc. Você deve gerar o documento nesse formato. E aí, o que eu vou fazer nesse documento, nesse formato? Eu vou chegar no meu prompt, aqui que eu tenho para o nosso FDD, e aqui, se você olhar, tá?

04:54

Eu tenho o esqueleto, tá? Então, ó, contexto, motivação, escopo, inclusões, exclusões, etc. Aqui, é que esse documento aqui não tá me ajudando aqui no meu... Cara, deixa eu copiar tudo isso aqui. Deixa eu conseguir pegar melhor, galera. Pera aí.

05:15

Pronto, consegui pegar e colar aqui no GPT, tá? Então, agora, qual que é a ideia? Eu consegui gerar um rascunho, porque eu sei que isso que ele vai gerar não vai ter necessariamente tudo o que eu preciso e nem todas as informações vão estar corretas. Por outro lado, eu já não estou partindo do zero.

05:37

Então, eu vou mandar essa informação agora aqui e a gente tem que aguardar a IA começar a gerar esse documento aí pra gente. Então, eu vou dar um pauso aqui rapidinho, somente pra esperar ela terminar de fazer.

05:52

Prontinho, pessoal! Fez aqui, até que foi mais rápido do que eu imaginei. Então, ele gerou aqui um Rate Limiter SDK em Go com o modo Redis em Memory, Data, Versão e tal aqui, Motivação Técnica. A única coisa que você pode pedir também depois para a IA fazer é não utilizar Grounding. O que é Grounding? Quando ela aponta a referência de onde ela tirou a informação.

06:13

E aqui ela está fazendo o grounding para mim do arquivo PDF, tá? Então, às vezes isso atrapalha, mas é importante você saber também de onde ela tirou a informação. Agora, uma coisa que é interessante é como ela leu o documento de high level e entendeu também todo o contexto de rate limiting, olha só que interessante.

06:32

Objetivo técnico, decisão de alol, oferecer paridade funcional, suportar política e isolamento, key space e método, API in process, escopo de exclusões, estratégias, token bucket e fixer window, armazenamento e memory, resolução de política de tenant, middleware, os cabeçalhos, telemetria, fallback, o que está excluído, autenticação,

06:56

Se você olhar, esse documento começa a parecer muito com aquele documento que eu mostrei pra vocês do que eu tinha criado antes. Você consegue perceber? Nem tudo aqui vai estar exatamente da forma como eu queria, mas olha só! Ele trouxe o Options muito parecido com aquilo que a gente estava falando. Ele trouxe uma estrutura um pouco diferente, porque ele está focando muito em multi-tenant aqui nesse caso.

07:22

Mas, olha só, headers de semântica 4.2.9, os exemplos que ele acabou trazendo, como é que ele trabalha com erros, exceções, fallback, como é que ele está trabalhando com a parte de observabilidade, logs, tracings, as dependências, as versões, garantia de compatibilidade, critérios de aceites, risco de mitigação e etc. Pessoal, somente de

07:44

você já ter um documento desse, pra você não partir do zero. E a partir disso, você começar, vamos dizer assim, a editar, a compor e ajustar, já te ajuda muito. Por isso que o que eu tô querendo trazer aqui pra vocês é

08:02

Existem 10 milhões de formas de criar documentos. Não existe algo e uma fórmula mágica que eu faça e ele já gere tudo. O que eu estou mostrando aqui para você são formas de como você pode utilizar e trabalhar no dia a dia para que isso seja feito de uma forma cada vez

08:20

mais simples, você vai ter que ter provavelmente diversas iterações, mas o que eu acho que é o mais importante é que você nunca vai ou deve partir do absoluto zero, tá? Partir do zero realmente vai dar muito trabalho ali pra você. Por isso que um esqueleto muito bem feito, os templates que você vai ter acesso e tudo mais, vai te ajudar demais

08:42

para que você não comece simplesmente um novo documento, tá? Então, isso aí acaba sendo muito, mas muito importante mesmo na hora que você tem que... Como que eu posso dizer?

08:54

criar esses tipos de documento. Criar documento não é algo prazeroso, é algo importante, quem é adulto faz o que precisa ser feito, mas, ao mesmo tempo, com inteligência artificial, com fluxos corretos, com templates, com prompts, sem dúvidas, esse processo acaba ficando até um pouco mais prazeroso, porque você consegue ver as coisas sendo feitas, você consegue ir ajustando,

09:18

e pontos desse tipo, tá? Então, espero que o que eu passei agora, tenha passado aqui pra vocês nesse conteúdo, tenha te ajudado a entender melhor documentos de high level, documentos focados mais em feature, como você consegue realmente fazer uma pesquisa, como que você consegue ajustar o conteúdo dessa pesquisa, e como que você consegue fazer com que essa pesquisa e outros documentos te ajudem

09:45

a gerar documentos que você vai ter que lapidar, mas que você não vai precisar mais partir do zero daqui para frente. Beleza? Então, aproveitem bastante isso, pessoal. Acredite, documentação é um asset. Quando falavam de testes automatizados, para mim, eu simplesmente queria chorar porque era muito chato fazer, porque parecia que eu demorava mais tempo para fazer o teste do que a aplicação, mas documento é a mesma coisa.

10:13

demora pra fazer, dá trabalho, mas a IA vai ler, seu time vai ler, você vai manter essa parada, como que eu posso dizer, atualizada, utilizando IA, de qualquer forma, e, simplesmente, uma coisa que eu tenho certeza,

10:30

é que vai fazer com que você tenha resultados muito melhores na hora do processo de desenvolvimento. Lembrando que a gente está falando de engenharia de software, engenharia de software não é apenas desenvolvimento. Esses processos, documentações, a gente está pensando sempre no ciclo de vida completo de uma aplicação.

10:48

Fechou? Espero que vocês tenham gostado, eu sei que teve bastante informação, você vai ter acesso a todos esses prompts, esses documentos, e espero que você comece a fazer os seus testes, comece a utilizar isso que você está vendo aí na sua empresa, e espero que isso realmente consiga te ajudar no dia a dia. Abraço aí pra você!

## Resumo IA

**Abreviações**
- **FDD** — *Feature Design Doc* (Documento de Design de Feature)
- **HLD** — *High-Level Design* (Projeto de Alto Nível)
- **SDK** — *Software Development Kit* (Kit de Desenvolvimento de Software)
- **Go** — linguagem de programação Go
- **PDF** — *Portable Document Format* (Formato Portátil de Documento)

**Resumo**
A aula mostrou como gerar um rascunho útil de Feature Design Doc combinando três insumos principais: o HLD da feature, um PDF de Deep Research com comparações, referências e estratégias, e um esqueleto/template do próprio FDD. O instrutor enfatizou que, em vez de pedir um documento “do zero”, a IA deve receber contexto já estabilizado para preencher uma moldura bem definida, o que reduz a chance de uma saída genérica e melhora a coerência técnica.

No exemplo do rate limiter em Go, o prompt foi montado de forma simples, mas com contexto forte: solicitou-se um FDD para a feature, informou-se que o HLD seria anexado, adicionou-se a pesquisa técnica em PDF e exigiu-se que a resposta seguisse o template do FDD. Também foi orientado que o resultado não deveria ser detalhado em nível de implementação linha por linha, mas precisava explicitar contratos, comportamento, decisões arquiteturais e elementos suficientes para orientar a execução.

O HLD foi apresentado como ancoragem das decisões já tomadas, fazendo a IA reutilizar arquitetura, componentes, responsabilidades e trade-offs, em vez de reinventar a solução. Já a pesquisa estruturada complementou com comparações, implicações operacionais e referências externas, enriquecendo o documento com mais precisão técnica. O esqueleto do FDD garantiu cobertura mínima de seções relevantes, como contexto, motivação, escopo, inclusões, exclusões, observabilidade, erros, fallback, compatibilidade e critérios de aceite.

A aula também destacou o conceito de grounding, isto é, a indicação explícita da origem de certas informações no material anexado. Embora isso possa poluir a leitura em alguns casos, é útil para auditoria e validação do rascunho. O instrutor mostrou que o documento gerado já vinha com boa aderência ao contexto, incluindo tópicos como headers, erros, fallback, telemetria, dependências, compatibilidade e critérios de aceite, mesmo que ainda precisasse de revisão e ajuste humano.

Por fim, a mensagem central foi que a documentação não deve começar do zero: a combinação de bons templates, bons insumos e bons prompts acelera a geração da primeira versão e desloca o esforço para revisão, edição e composição. A IA é vista como apoio ao ciclo de vida completo da engenharia de software, e não como substituta da validação humana.

**Pontos de atenção**
- Não pedir “um documento do zero”; o ganho vem de combinar HLD, pesquisa e template.
- O HLD deve ser usado como base real de decisão arquitetural, não como referência decorativa.
- O PDF de pesquisa deve complementar o HLD com alternativas, comparações e referências que não cabem no documento arquitetural.
- O esqueleto do FDD é essencial para garantir cobertura das seções mínimas e evitar lacunas.
- O prompt pode ser simples, desde que o contexto esteja forte; a qualidade da saída depende muito dos insumos.
- Não exigir nível de detalhe extremo: o documento deve orientar implementação, mas não virar código comentado.
- Revisar aderência ao HLD, porque a IA pode introduzir foco excessivo em temas secundários ou distorcer prioridades.
- Grounding ajuda na rastreabilidade, mas pode atrapalhar a leitura final; use conforme a necessidade de auditoria.
- Tratar o resultado como rascunho inicial: a IA acelera, mas não elimina revisão humana.
- Esperar iterações curtas de ajuste e refinamento; a geração rara vez sai perfeita na primeira tentativa.
- Documentação é trabalho, mas é um ativo importante para desenvolvimento, testes, manutenção e automações futuras.
- Não partir do absoluto zero aumenta muito o retrabalho; templates e prompts bem estruturados reduzem fragilidade.