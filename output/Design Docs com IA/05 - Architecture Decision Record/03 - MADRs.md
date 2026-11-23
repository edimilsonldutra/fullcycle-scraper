Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17120)

## Resumo da aula

MADR é um formato padronizado em Markdown para registrar decisões arquiteturais de forma legível para pessoas e parseável por máquina. Ele não substitui o ADR como conceito; ele torna o registro mais previsível, o que reduz variações de estrutura entre autores e facilita o uso contínuo do acervo. A diferença central em relação ao template clássico já conhecido está menos no conteúdo lógico da decisão e mais na disciplina documental aplicada ao arquivo.

Quando cada ADR usa campos, nomes e seções diferentes, busca, validação e automação ficam frágeis. O MADR resolve isso ao definir campos recorrentes e uma estrutura fixa que pode ser interpretada por ferramentas sem depender de leitura humana caso a caso. Essa previsibilidade é o que torna o documento processável em pipelines, CLIs, indexadores e fluxos assistidos por IA.

Campos como status, date, tags, supersedes, amends e superseded by adicionam semântica explícita ao documento. Eles não servem apenas para ornamentar o cabeçalho: permitem saber se a decisão está ativa, quando foi registrada, quais temas ela cobre e como se relaciona com outras decisões. Sem esses metadados, a timeline arquitetural continua existindo, mas fica implícita e muito mais difícil de consultar automaticamente.

Retomando a ideia de timeline arquitetural, o MADR explicita vínculos documentais em vez de deixá-los apenas no texto corrido. supersedes indica que uma decisão substitui outra; superseded by registra a substituição no sentido inverso; amends mostra que um documento complementa ou ajusta parcialmente outro. Esse encadeamento transforma um conjunto de arquivos soltos em uma rede navegável de decisões.

Além dos metadados, o MADR costuma organizar o corpo do documento com seções como Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Pros and Cons of the Options, Consequences e References. Essas seções refinam a estrutura clássica já conhecida ao separar melhor motivadores, opções avaliadas e efeitos da escolha. O ganho não é burocracia; é consistência suficiente para leitura rápida, comparação entre ADRs e extração automatizada de informação.

Retomando o cenário de comunicação interna, uma ADR pode registrar a adoção de gRPC no lugar de REST e declarar supersedes ADR 02. Isso informa, sem ambiguidade, que a decisão anterior deixou de ser a referência principal para aquele contexto. Se no futuro outra abordagem substituir gRPC, o campo superseded by fecha o ciclo e preserva a evolução da decisão sem apagar o histórico.

A padronização do MADR permite integração com ADR Tools, ADR Log, scripts CLI e extensões de editor. Um CLI pode criar uma nova ADR com a próxima numeração, aplicar template consistente e já preparar os campos esperados para relacionamento e rastreabilidade. Ferramentas desse tipo dependem de convenções estáveis; sem isso, automatizar criação, busca e manutenção vira uma coleção de exceções.

Como o formato é previsível, o repositório pode validar ADRs em CI/CD com lint e checagens estruturais. GitHub Actions, por exemplo, podem verificar se os campos obrigatórios existem, se a nomenclatura está correta e se os links entre documentos permanecem íntegros. Isso reduz deriva documental e impede que o acervo perca consistência à medida que cresce.

IA se beneficia de ADRs quando encontra contexto explícito, mas o ganho aumenta quando esse contexto também está estruturado. Um conjunto de MADRs permite identificar quais decisões substituíram outras, quais temas se repetem e em que momento certas escolhas foram feitas. Em vez de inferir tudo apenas do código, a IA passa a operar sobre uma memória arquitetural com relações e metadados claros.

MADR é um padrão útil, não um ritual imutável. Templates, campos adicionais e variações como Informed e Consulted podem fazer sentido em alguns times e ser excesso em outros. O critério correto é preservar consistência suficiente para leitura, governança e automação, ajustando o formato ao contexto real da empresa.

## Transcrição

00:01

Bom, pessoal, a gente falou um pouquinho dessa estrutura clássica, né? Vamos dizer assim, sobre uma Architecture Decision Record. E agora eu quero trazer pra você uma outra coisa que começou a acontecer ao longo do tempo, tá? Onde apareceu um nome novo.

00:19

no meio de toda a história, tá? E o nome disso é chamado de MADR, tá? Ou seja, Markdown ADR. Então o MADR, que é o Markdown Architecture Decision Record, ele é um formato padronizado em Markdown para registrar decisões arquiteturais de forma legível e processável. Ele evoluiu do modelo original de ADR, do NIGAR,

00:44

e foi trazendo mais consistência em metadados e previsibilidade, tá? Ou seja, quais são os principais pontos, e a gente vai um pouquinho mais a fundo em relação a isso, tá? Os campos, hoje em dia, de uma MADR, eles são padronizados. Normalmente, eles têm status, date, tags, supersedes, a gente vai falar sobre isso, estrutura fixa e validável em pipeline, se necessário, compatibilidade com ferramentas ADR Tools, ADR Log,

01:13

e facilita o rastreamento e a visualização e documentação contínua. E por que isso é importante, pessoal? Porque se cada pessoa começa a utilizar uma forma diferente de criar suas ADRs, acaba ficando mais difícil de você encontrar, entender o nível de padronização e, somente para você saber, hoje em dia existem diversas ferramentas para você trabalhar e gerenciar ADRs.

01:41

Existem ferramentas CLI, inclusive, que você vai lá, create new ADR, ele já vê a última numeração da ADR que foi criada, você coloca o título, você vai escrevendo, daí eu falo, olha, essa ADR eu quero desativar porque ela foi substituída por essa ADR. Então, tem diversas ferramentas. Mas para que essas ferramentas funcionem, inclusive no pipeline de ICD, por exemplo,

02:04

Esses campos, esses nomes, todas essas coisas, elas precisam realmente ter um padrão. Então, quando, entre aspas, surgiu esse Markdown ADR, o que começou a acontecer é que esse tipo de padrão ajudou e isso facilitou muito mais, muito mais a vida para que a gente possa gerenciar. Porque imagina que cada decisão arquitetural você gera um arquivo, tá? E eu vou falar quais as decisões arquiteturais que você deve

02:33

criar uma DR e, eventualmente, algumas que você não deve, tá? Então, a gente vai falar disso daqui a pouquinho. Somente para que você consiga entender aqui, de forma geral, ele tem

02:45

Aqui é um exemplo de uma ADR, deixa eu colocar aqui para ficar um pouco melhor para você ver. Mas eu tenho, por exemplo, ADR 03, perceba que eu estou trabalhando com o Markdown ali, então ele tem um pouco dos metadados, ou seja, status, eu tenho supersedes ADR 02. O que significa? Que essa ADR está substituindo a ADR 02.

03:08

Ou seja, escolher gRPC para comunicação interna. Então, vamos imaginar que eu escolhi gRPC para comunicação interna e antes eu usava REST. Então, o que essa DR vai fazer? Essa DR vai ter o status de SuperSEEDS da versão anterior que utilizava REST. Aí a gente tem a data, ela é referente com o quê? Com a DR001 e com a DR003. Não, aqui era para ser 002, provavelmente.

03:37

E aqui a gente tem também outros metadados como, por exemplo, a Mendes. A Mendes significa ela pode grudar ou resolver parcialmente alguma coisa que está

03:54

em alguma outra ADR, tá? Então, isso aí é interessante. Eu tenho superseded by, se for substituída no futuro por uma outra ADR, a gente vai falar que, olha, essa ADR agora, ela foi substituída por essa ADR, tá? Então, é bem interessante como é que isso funciona.

04:12

Agora, imagina a inteligência artificial lendo esses documentos e saber o porquê cada decisão aconteceu, qual substituiu uma, qual substituiu outra, para ela começar a tomar decisões entendendo melhor o contexto do seu software. E o contexto, nesse caso, é a timeline, tá?

04:32

Então, aqui, se você olhar, ele traz o Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Pros and Cons of the Options, Consequences e Referências. Então, se você perceber aqui,

04:48

é o padrão, vamos dizer assim, de um MEDR, de como isso funciona, está escrito em inglês, pode traduzir, não tem problema nenhum. O grande ponto é que esse MEDR tem um nível de padronização muito grande, ele tem linkagem, ele gera relacionamentos, não que as outras não tinham isso,

05:07

Mas hoje em dia, tudo trabalhando em markdown, com links, chamadas, hoje em dia com o IA também no meio dessa história, as coisas, elas acabam mudando um pouco de lugar, tá? Somente pra você saber de onde eu tirei isso, tá, galera? Isso aqui hoje em dia tá bem comum.

05:25

Se você acessar esse site aqui, tá? madr.github.com barra madr, tá? Então, basicamente, aqui é a página onde você pode entender melhor como é que funciona uma madr. Recomendo que você acesse. Então, ele vai trazer isso aqui pra você. Como que você aplica isso aqui? Ele traz os templates.

05:49

em relação a como que você usa, tem muito material aqui que você consegue utilizar, ele traz os exemplos de como eles são feitos, se você clicar aqui você dá pra ir mais exemplos lá na página no GitHub, então tem algo assim que realmente acaba sendo muito

06:08

mas muito interessante na hora que você acaba trabalhando em relação a isso. Uma coisa interessante é que ele sempre traz templates para você utilizar, tem locais onde você pode usar o script CLI para fazer GA, eu vi inclusive extensões para o VSCode para trabalhar com tudo isso. Eu assumo para vocês que eu não

06:29

Ah, vamos dizer assim, sou tão acostumado a ficar usando extensões e algumas... Muita tecnologia para gerenciar as minhas ADRs, tá? Principalmente nesses últimos tempos com inteligência artificial. Mas é interessante que você tem até workflows de GitHub Actions, por exemplo, para ele fazer um link, né?

06:49

no markdown da sua ADR pra garantir que tá tudo feito no mesmo padrão, tá? Então, aqui ele começa a mostrar, inclusive, pra você como que você pode, inclusive, trabalhar com essas ADRs baseadas em contextos diferentes do projeto. Por exemplo,

07:08

Backend, UI, e assim vai. Então, eu posso trabalhar. E aqui ele tem Full Template de como pode trazer, Informed, Consulted. Então, tem diversas formas. E eu vou dizer, tá, pessoal? Nunca levem essas coisas a ferro e fogo, tem que ser desse jeito e etc, tá? Porque...

07:26

No final do dia, você vai fazer o que faz mais sentido para o contexto da sua empresa. Eu acho que o que vale a pena é você ler esse site, entender, prestar atenção nisso que eu estou passando agora, porque eu acredito que isso vai fazer com que você adapte como que as coisas devem ser seguidas e o que fazem sentido ali para você.

07:51

inversões, eles dão exemplos, tem a parte de ferramentas, que você pode ir para a Decision Capture Tools, para você tentar organizar suas ADRs, etc. Mas, tá? Uma das coisas que eu vou recomendar é que você continue fazendo e assistindo as próximas aulas, porque eu vou mostrar para vocês o que eu fiz e eu acho que vai poder ajudar bastante aí na empresa que você está trabalhando em relação a isso.

08:18

Fechou? Mas está aqui MADR, no próximo vídeo a gente vai entender um pouquinho mais sobre o gerenciamento, mas principalmente os status de como que essas ADRs podem ter para que faça sentido você ter múltiplos documentos aí nesses casos. Beleza? Então vamos nessa!

## Resumo IA

**Abreviações**  
- **ADR** — *Architecture Decision Record*  
- **MADR** — *Markdown Architecture Decision Record*  
- **CLI** — *Command Line Interface*  
- **CI/CD** — *Continuous Integration / Continuous Delivery*  
- **GitHub Actions** — sistema de automação de workflows do GitHub  
- **REST** — *Representational State Transfer*  
- **gRPC** — *gRPC Remote Procedure Calls*  
- **VSCode** — *Visual Studio Code*  
- **NIGAR** — referência ao modelo original de ADR mencionado pelo instrutor

**Resumo**  
A aula apresentou o MADR como uma evolução padronizada do formato de ADR em Markdown, voltada a tornar decisões arquiteturais mais legíveis para humanos e mais fáceis de processar por máquinas. O instrutor explicou que o valor central do MADR não está em mudar a natureza da decisão arquitetural, mas em impor consistência documental, reduzindo variações de estrutura entre autores e facilitando uso contínuo do acervo de decisões. Em contraste com ADRs escritas de formas muito distintas, o MADR define campos e seções recorrentes que permitem busca, validação, automação e integração com ferramentas.

Foram detalhados os metadados mais importantes, como status, date, tags, supersedes, superseded by e amends, que adicionam semântica explícita ao documento e ajudam a entender se a decisão está ativa, quando foi registrada, quais temas cobre e como se relaciona com outras decisões. O instrutor reforçou a ideia de timeline arquitetural, mostrando que esses vínculos documentais transformam arquivos isolados em uma rede navegável de decisões, especialmente útil quando uma ADR substitui outra, como no exemplo de adoção de gRPC no lugar de REST. Também foram citadas seções típicas do corpo do documento, como Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Pros and Cons of the Options, Consequences e References, destacando que essa organização melhora a comparação entre ADRs e a extração automatizada de informação.

A aula ainda abordou o ecossistema de ferramentas ao redor do MADR, incluindo ADR Tools, ADR Log, scripts CLI, extensões de editor e integrações com GitHub Actions. O fluxo explicado foi o de criar ADRs com template consistente, manter numeração e relacionamento entre documentos, validar estrutura em pipelines de CI/CD e usar esses registros como base de rastreabilidade e apoio à leitura por IA. O instrutor também comentou que o MADR é um padrão útil, mas não deve ser tratado como ritual rígido: cada time deve adaptar campos e variações ao seu contexto, preservando consistência suficiente para governança e automação sem exagerar na formalidade.

**Pontos de atenção**  
- Padronização é essencial: se cada pessoa criar ADRs com nomes, campos e seções diferentes, a busca, validação e automação ficam frágeis.  
- Os metadados não são decorativos; campos como status, date, supersedes, superseded by e amends têm função prática de rastreabilidade e relacionamento entre decisões.  
- `supersedes` indica que a decisão atual substitui uma anterior; `superseded by` registra o inverso, preservando a evolução histórica.  
- `amends` deve ser usado quando a nova decisão complementa ou ajusta parcialmente outra, e não necessariamente quando a substitui por completo.  
- A consistência do template é o que viabiliza uso com ferramentas como CLI, ADR Tools, ADR Log e validações em CI/CD.  
- Em pipelines, checagens estruturais podem validar campos obrigatórios, nomenclatura e integridade de links entre documentos.  
- O formato em Markdown facilita leitura humana e processamento por ferramentas, inclusive por fluxos assistidos por IA.  
- O ganho do MADR está na previsibilidade do documento, não em aumentar burocracia; o objetivo é melhorar leitura rápida, comparação e automação.  
- Existem variações de template e abordagens como Informed e Consulted, mas elas devem ser adotadas conforme o contexto da empresa e não por regra absoluta.  
- O instrutor reforçou que não se deve seguir o padrão “a ferro e fogo”; o melhor uso do MADR é adaptar com critério mantendo consistência suficiente para governança.