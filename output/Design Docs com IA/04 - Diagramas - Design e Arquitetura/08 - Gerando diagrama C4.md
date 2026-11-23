Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17077)

## Resumo da aula

Modelos em modo thinking tendem a seguir melhor um workflow longo porque gastam mais processamento em raciocínio intermediário. Isso costuma aumentar a precisão dos passos, mas não garante automaticamente um resultado melhor; apenas indica que houve mais análise antes da saída. Em contrapartida, alguns modelos surpreendem pela combinação de velocidade e qualidade, o que muda o custo operacional de gerar diagramas. A escolha prática não é “modelo lento é melhor”, e sim “qual modelo entrega artefatos úteis com menos iteração para o seu caso”.

Retomando o pipeline já estabelecido, o prompt pode ser executado fora do ambiente em que foi criado, desde que o workflow esteja bem especificado. Um agente no Cursor, no Cloud Code, no Copilot ou em outra ferramenta pode receber o comando de geração e produzir arquivos equivalentes porque o valor principal está no prompt e nos parâmetros, não na interface. Isso reduz lock-in e permite comparar agentes por velocidade, aderência ao formato e capacidade de corrigir a própria saída. A consequência prática é simples: troque a ferramenta quando fizer sentido, sem reescrever todo o processo.

A execução concreta transforma o FDD do Rate Limiter em arquivos versionáveis, tipicamente .puml e .md, e opcionalmente em imagens PNG. O .puml contém o código PlantUML/C4 que descreve os elementos e relações do diagrama; o Markdown registra justificativas, validações ou observações do processo. Esse passo importa porque o diagrama deixa de ser uma ideia no prompt e vira artefato auditável no repositório. Quando a geração funciona bem, a ferramenta cria a pasta de saída, escreve os arquivos e tenta validar dependências locais antes da renderização.

A renderização para PNG é uma etapa útil, mas mais frágil do que a geração textual. O modelo pode conseguir escrever corretamente os arquivos .puml e ainda falhar ao converter para imagem por dependência ausente, erro de sintaxe residual ou problema no ambiente local. Por isso, o sucesso real do pipeline não deve depender apenas do PNG; o artefato textual continua sendo a base confiável para revisão e correção. Se a imagem falhar, a estratégia correta é inspecionar o .puml, corrigir o problema e rerodar a exportação.

Um arquivo C4 em PlantUML costuma começar com @startuml, declaração de codificação como UTF-8 e includes da biblioteca C4 adequada ao nível representado. Depois disso, o código define elementos como Person, System, System_Ext, fronteiras como System_Boundary e relações como Rel, que conectam os blocos com verbos e descrições. No exemplo do Rate Limiter, isso aparece como variáveis nomeadas para Redis, Prometheus e OpenTelemetry, além das relações entre desenvolvedor, operador e serviço. Ler esse código é importante porque a revisão arquitetural acontece no texto antes de acontecer na imagem.

O preview por extensão acelera a inspeção porque permite abrir o .puml e renderizar o diagrama sem sair do editor. Extensões de PlantUML no VS Code costumam oferecer visualização imediata, mas dependem de bibliotecas auxiliares instaladas na máquina; quando faltam, o próprio erro geralmente informa o pacote necessário para instalar via brew ou apt. Esse fluxo é valioso porque encurta o ciclo entre editar, visualizar e corrigir. Em vez de depender só do agente, o desenvolvedor consegue validar localmente o resultado gerado.

Retomando o exemplo já conhecido, o valor aqui não está em redefinir C1, C2, C3 ou C4-Code, mas em verificar se cada nível virou arquivo coerente. O C1 mostra atores, boundary e sistemas externos; o C2 expõe containers e tecnologias; o C3 abre os componentes internos; e o nível mais detalhado aproxima contratos e estruturas do código. A leitura prática consiste em conferir se os nomes, relações, notas laterais e dependências externas batem com o FDD, sem assumir que a primeira saída está correta. Similaridade visual com versões anteriores ajuda, mas não substitui validação semântica.

Dois agentes podem produzir diagramas funcionalmente parecidos e ainda divergir em detalhes de acabamento, como ícones, convenções visuais ou aderência mais estrita ao prompt. Um modelo mais rápido pode entregar um rascunho excelente em segundos, enquanto outro mais cuidadoso segue mais fielmente certas regras de estilo. Essa diferença não invalida nenhum dos dois; apenas muda o esforço de revisão posterior. O critério técnico deve ser o custo total: tempo de geração mais tempo de correção.

A saída do modelo deve ser tratada como rascunho, nunca como documentação definitiva. Mesmo quando o diagrama parece correto, ele ainda precisa ser lido como código: conferir elementos, relações, notas, encoding, includes e aderência ao FDD. Esse cuidado existe porque a IA pode produzir algo plausível, rápido e visualmente convincente, mas semanticamente incorreto. Revisão humana continua sendo parte do pipeline, não um detalhe opcional.

Com geração rápida, passa a fazer sentido automatizar a revalidação dos diagramas antes do commit. Um hook pode verificar se o código, o FDD e os arquivos gerados continuam consistentes entre si e, quando houver divergência, bloquear o commit ou disparar a regeneração. Isso transforma diagramas em artefatos vivos do fluxo de engenharia, não em documentação esquecida. A automação ideal não substitui revisão humana, mas impede que inconsistências óbvias cheguem ao repositório principal.

## Transcrição

00:01

Bom, pessoal, voltando aqui, eu estava falando para vocês que a gente tem e é totalmente possível da gente conseguir utilizar esses prompts sem ser o Cloud Code, etc. Apesar de ele estar dentro da pasta do Cloud e tudo mais. E eu vou mostrar isso aqui para vocês, tá? Agora, um ponto importante que eu quero que vocês se liguem é o seguinte.

00:24

Normalmente, quanto mais você coloca o modelo em modo thinking, onde ele pensa, ele raciocina e etc., normalmente isso traz mais precisão em relação aos passos que eles vão seguir. Normalmente, quanto mais tempo demora, não é que necessariamente isso seja algo bom, mas você entende que a gente está utilizando uma análise, uma forma de raciocínio.

00:51

Por outro lado, muitas vezes existem modelos que nos surpreendem com a velocidade e com a qualidade que ele sai. Eu fiz alguns testes com esse modelo que o Cursor tem aqui, tá? E esse modelo que o Cursor tem nesse caso aqui, nesse momento, é o Composer 1, pode ser Composer 10 na hora que você esteja vendo esse vídeo. O maior ponto que eu quero trazer aqui para vocês é que

01:20

você pode testar diversos agentes para gerar suas paradas e você vai ver que pode funcionar muito bem, mesmo sem ser exatamente no padrão que ele tem. Então, olha o que eu vou colocar aqui e eu vou fazer um prompt extremamente simples para ver qual é o resultado que ele vai gerar aqui na sua frente. Então, eu vou fazer o seguinte, vou colocar assim, baseado no arroba e aqui eu vou colocar a C4 generator,

01:50

Execute o comando, vou passar o meu comando que é generateCIFOR aqui pra ele, usando o

02:01

meu Rate Limiter como um FDD. E aqui, a gente está com o Composer, que é um modelo lançado para a empresa que faz o Cursor. E o grande diferencial dele é ser muito rápido. E realmente, esse modelo é muito rápido. Eu fiz alguns testes com ele. Em alguns testes, ele conseguiu gerar rapidamente o diagrama C4 e conseguiu gerar o PNG.

02:26

E, em alguns momentos, ele ficou sofrendo um pouco para gerar o PNG e eu tive que fazer algumas interações com ele. O ponto é que ele é realmente muito rápido e depois vale a pena você olhar. Se você utilizar Cursor, provavelmente você pode estar utilizando qualquer outra ferramenta como o GitHub Copilot, pode estar usando alguma ferramenta da Google e etc. Mas aqui é somente para casos de exemplo. Então, eu vou dar um...

02:52

mandar esse cara fazer, e vamos ver o quão rápido ele consegue fazer, porque realmente esse cara é bem rápido para trabalhar. Então, gerou a pasta, e aqui já está gerando os arquivos plant.uml para a gente, de uma forma bem rápida realmente. Está gerando aquele arquivo umd, é o markdown que eu pedi para ele.

03:17

Está refazendo as validações. Agora que ele gerou todos, ele vai começar a recorrigir as coisas. Verificou se eu tenho o plant.uml instalado na minha máquina. E ele vai tentar gerar agora os nossos PNGs. E vamos ver se ele conseguiu gerar esse cara aqui.

03:43

Eu acho que ele não está conseguindo gerar o PNG, galera. Deixa eu olhar aqui nos documentos aqui. Ele conseguiu gerar um PNG e depois ele está tentando... Opa, ele está corrigindo o arquivo. Provavelmente, na hora que ele foi gerar, deve ter dado algum erro e ele deve ter colocado aqui para a gente. Bom, seguinte, ele não gerou os PNGs aqui para mim, mas eu não estou me importando muito com isso não.

04:09

Beleza? Principalmente pela velocidade que ele conseguiu fazer. Provavelmente, se eu colocar outra iteração e falar gérios, pngs, tudo bem, provavelmente ele ia conseguir. Mas o ponto é, realmente foi bem rápido esse processo todo para gerar essa quantidade de código.

04:26

Também, eu não vou olhar nesse momento o mérito da coisa, o quão bom ou ruim ele gerou isso, tá? Só estou dizendo que você pode testar diversos modelos, é isso que eu quero deixar na sua mente e não achar que eu estou aqui usando só o Cloud Code, beleza? Então, o que acontece é o seguinte, galera. Eu vou abrir esse Rate Limiter C1 aqui. Deixa eu colocar Keep All aqui somente para ele... para o cursor...

04:51

não ficar pedindo para eu fazer revisão, eu vou colocar KeepAll aqui, assim ele coloca todos esses caras. Então, somente para que vocês consigam entender aqui, pessoal, isso aqui é um código PUML, Plain to UML, ou seja, você tem o StartUML aqui pra gente,

05:11

Eu estou falando que ele é um UTF-8, e para ele incluir aqui o C4, o C4 Context, e aqui basicamente ele define, eu tenho o componente Person, eu tenho o System Boundary, que é aqueles tracejados que eu tenho em volta de mim, e eu tenho um System, que ele é um Service,

05:29

que ele é o serviço host, microserviço que utiliza o rate limiting. Eu tenho um system ext, que é o sistema externo, que aparece fora daquele meu system boundary, que ele aparece como cinza, onde eu falo que ele é um redis, ou seja, aqui eu estou nomeando, é como se fosse uma variável, que eu estou falando que essa variável é um redis, que está escrito armazenamento de estado.

05:52

Prometheus, coleta de métricas. OpenTelemetry, coleta de exportação. E aqui, o R e L são as relações. Então, eu estou falando que o Dev, o desenvolvimento, desenvolve e configura o serviço. O Op, o operador, também tem relação com o serviço.

06:10

O meu serviço utiliza o Redis, o meu serviço utiliza o Prometheus e os meus serviços usam o OpenTelemetry. E aqui ele criou uma nota no lado do service, falando que é um SDK embutido com o RateLimiter SDK integrado em process, decisões locais, suporta o modo Redis e Memory, e aqui eu posso ter para ele mostrar a legenda.

06:32

como que você pode verificar esse plant.uml aqui. Existem extensões do Visual Studio Code que se você digitar a diagrama C4 ou plant.uml, deixa eu olhar aqui para vocês juntos, extension, eu vou colocar aqui, plant.uml,

06:58

Eu acho que esse cara aqui, que é o mais usado, que é o que eu tenho, que eu utilizo, é esse cara aqui. O Plain2ML, o que ele tem que é algo interessante aqui pra gente? Se eu colocar ele em modo visualização, aqui, ele consegue fazer um preview pra gente do código que apareceu.

07:20

Para fazer esse preview, provavelmente você vai precisar instalar uma bibliotequinha na sua máquina, esqueci o nome dela, mas normalmente quando ele dá erro ele fala o nome, aí você dá um brew install, um apt install o nome dessa biblioteca que ele usa para gerar. Mas olha só que interessante, galera. Isso aqui foi gerado em questão de um minuto pelo composer do cursor. E perceba que eu não trabalhei com o Cloud Code aqui nesse nosso caso.

07:50

E aqui é o PNG, vamos ver se ele gerou aquela hora. No final das contas, ele tinha conseguido gerar o PNG. Ele não continuou por algum motivo. Provavelmente, se a gente continuasse insistindo, ele ia trazer. Aqui o Rate Limiter, a parte 2, que é a parte de container. Vamos ver como é que ele gerou aqui pra gente.

08:09

Aqui, Gerol, desenvolvedor, desenvolvedor de microserviços, a plataforma microserviços, o Go, Rate Limiting, colocou as tecnologias que eu vou usar, colocou as configurações que eu vou utilizar no Redis, botou o Prometheus, botou o OpenTelemetry e trouxe aqui pra mim o Container. Mesmo esquema aqui, o Rate Limiter do C3.

08:31

Vamos lá. E trouxe aqui o serviço Go, que tem API pública, o middleware, métricas, o tracing, estratégia janela fixa, estratégia de token bucket, storage Redis ou storage in memory, o Redis aqui de fora, colocou as observações do lado e tal. Eu não quero chegar nos detalhes, mas dá para perceber que é bem similar ao que a gente já tinha visto. E eu vou olhar aqui o C4 do Plant1ML, que ele acaba gerando aqui para a gente. E aqui ele gerou aquele diagrama lá,

09:02

que ele coloca configuração, API pública, as estratégias, ele tem aqui o storage, se é local ou não.

09:10

E botou as anotações do lado e colocou aqui as APIs, provavelmente, para a parte de observabilidade. Galera, o que eu estou querendo dizer aqui, no final das contas, é que com qualquer sistema de inteligência artificial, com bom prompt, você consegue ter resultados bem similares. Perceba que eu gerei isso e não foi com o próprio Cloud Code. Se eu fosse fazer com o Cloud Code, basicamente, eu tenho, sei lá, nesse caso aqui, a extensão do Cloud Code,

09:38

Aí eu iria colocar generate C4, ia passar o meu feature design doc, ia dar enter aqui pra mim e ele ia começar a fazer esse processo. Se eu fosse utilizar, sei lá, o Codex da OpenAI, se eu fosse usar aqui o Google Assistant, provavelmente seria tudo muito parecido, tá? Por isso que eu queria deixar sempre muito claro aqui pra você que eu não estou sendo ou querendo enviesar você a utilizar o Cloud Code ou qualquer coisa desse tipo, tá?

10:07

Mas o que o Cláudio Codd me ajudou, na realidade, foi também construir esse prompt com workflow, apesar de eu ter iniciado esse processo no SharedGPT. Então, a gente tem muita ferramenta, pessoal, para todos os gostos e para todos os tipos de teste. Então, o que eu recomendo é que você teste bastante, porque no final do dia o importante vai ser o resultado final. O que eu mais queria trazer aqui especificamente, inclusive, é que

10:37

Agora, com um arquivo de feature muito bem feito, detalhado, a gente tem a capacidade de gerar esses diagramas automaticamente. E eu quero até te provocar no seguinte, será que você não pode criar um hook ou qualquer coisa que, antes de você dar um commit, você pede para ele revisar e verificar se o seu código ainda reflete o FDD?

11:02

ou se o FDD está refletindo os diagramas, e se não está refletindo, vamos regerar esses diagramas ali. Então, a gente tem essas opções agora, pessoal. Fazer isso ficou rápido. Então, não é mais aquele sofrimento que era antes. Imagina você digitar toda vez isso, apesar de ser bem simples, dá pra você perceber, né?

11:23

Uma das coisas que acabaram acontecendo aqui, e que o Composer não fez, foi botar os ícones chamando um monte de coisa, que provavelmente se você for usar o Cloud, etc., ele vai seguir mais a risca. O Composer não, mas ele gerou muito rápido. Então...

11:40

Sempre teste modelos, verifique sempre se, inclusive, esses modelos estão gerando as coisas certas. Esses caras sempre pensam que eles geram um rascunho na sua vida. É um rascunho que ele está gerando para você. Você precisa conferir. Você realmente tem que olhar se faz sentido e, se não fizer, você tem que pedir para ser corrigido.

12:02

Beleza? Então é isso aí galera, espero que você tenha curtido essa parte aqui onde nós temos essa possibilidade agora de gerar rapidamente esses diagramas. Vamos nessa!

## Resumo IA

**Abreviações**  
- **FDD** — *Feature Design Document*  
- **PNG** — *Portable Network Graphics*  
- **C4** — *Context, Containers, Components, Code*  
- **C1** — nível de contexto do C4  
- **C2** — nível de containers do C4  
- **C3** — nível de componentes do C4  
- **C4-Code** — nível de código do C4  
- **PUML / PlantUML** — linguagem/ferramenta para modelagem de diagramas em texto  
- **UTF-8** — *Unicode Transformation Format 8-bit*  
- **SDK** — *Software Development Kit*  
- **API** — *Application Programming Interface*  
- **VS Code** — *Visual Studio Code*  
- **Redis** — banco/armazenamento em memória usado como base de dados e cache  
- **Prometheus** — sistema de monitoramento e coleta de métricas  
- **OpenTelemetry** — framework de observabilidade para métricas, traces e logs  

**Resumo**  
A aula mostrou que a geração de diagramas arquiteturais não depende de uma única ferramenta, mas de um bom prompt, de um workflow bem especificado e de parâmetros consistentes. O instrutor comparou modelos em modo *thinking*, que tendem a gastar mais tempo em raciocínio intermediário e, por isso, geralmente seguem melhor os passos do processo, com modelos mais rápidos, que podem surpreender pela combinação de velocidade e qualidade. A conclusão prática é que o critério correto não é escolher o modelo mais lento, e sim aquele que entrega artefatos úteis com menos retrabalho.

Em seguida, foi demonstrado que o mesmo prompt pode ser executado fora do ambiente original, em ferramentas como Cursor, GitHub Copilot, Cloud Code ou outras integrações, reduzindo dependência de plataforma e facilitando comparar agentes por velocidade, aderência ao formato e capacidade de correção. O exemplo usado foi a geração automática dos artefatos do Rate Limiter a partir de um FDD, com saída em arquivos versionáveis como `.puml` e `.md`, e opcionalmente imagens `.png`. O `.puml` guarda o código PlantUML/C4, enquanto o Markdown registra justificativas e observações, tornando o diagrama um artefato auditável no repositório.

A aula explicou também que a parte textual do pipeline é mais confiável do que a renderização para imagem. Embora o modelo consiga gerar o arquivo PlantUML, a conversão para PNG pode falhar por falta de dependências locais, erro de sintaxe residual ou problema do ambiente. Por isso, o foco principal deve ser a validade do `.puml`, que pode ser revisado, corrigido e reexecutado. O instrutor mostrou como um arquivo C4 em PlantUML é estruturado com `@startuml`, codificação UTF-8 e includes das bibliotecas C4, além de elementos como `Person`, `System`, `System_Ext`, `System_Boundary` e relações `Rel`. No exemplo do Rate Limiter, foram citados Redis, Prometheus e OpenTelemetry, bem como os atores desenvolvedor e operador.

Outro ponto abordado foi o uso de extensões no VS Code para pré-visualizar o diagrama diretamente do arquivo `.puml`, acelerando o ciclo de edição e validação. O preview depende de bibliotecas auxiliares instaladas localmente, mas permite revisar a estrutura sem sair do editor. A aula retomou ainda os níveis do C4, reforçando que o importante é verificar se cada arquivo está coerente com o FDD: o C1 com atores e sistemas externos, o C2 com containers e tecnologias, o C3 com componentes internos e o nível de código com contratos e estruturas mais detalhadas. O instrutor destacou que a similaridade visual não substitui a validação semântica.

Por fim, foi defendido que a saída da IA deve ser tratada como rascunho, não como documentação definitiva. Mesmo quando o diagrama parece correto, é necessário conferir elementos, relações, notas, encoding, includes e aderência ao FDD. Como a geração ficou rápida, passou a fazer sentido automatizar revalidações antes do commit, por exemplo com hooks que comparam código, FDD e arquivos gerados, bloqueando inconsistências ou disparando regeneração. A ideia central é transformar diagramas em artefatos vivos do fluxo de engenharia, mantendo a revisão humana como parte do processo.

**Pontos de atenção**  
- Modelos em modo *thinking* podem ser mais precisos no processo, mas isso não garante resultado final melhor.  
- Velocidade e qualidade devem ser avaliadas juntas; o melhor modelo é o que reduz tempo total de geração e correção.  
- O workflow deve estar bem especificado para que o prompt funcione em ferramentas diferentes sem reescrita.  
- Não há necessidade de lock-in em uma única plataforma: Cursor, Cloud Code, Copilot e outras podem executar o mesmo fluxo.  
- A geração textual (`.puml`, `.md`) é mais confiável do que a renderização em PNG.  
- PNG pode falhar por dependência ausente, erro de sintaxe ou ambiente local; nesses casos, a correção deve começar no `.puml`.  
- Arquivos PlantUML/C4 precisam ser revisados como código: `@startuml`, encoding, includes, elementos e relações.  
- A validação deve começar pelo texto e não pela imagem final.  
- A leitura dos níveis C1, C2, C3 e C4-Code deve ser semântica, não apenas visual.  
- Similaridade com diagramas anteriores não substitui conferência de nomes, dependências, notas e fronteiras.  
- A IA gera rascunhos; a revisão humana continua obrigatória.  
- Quando a geração fica rápida, vale automatizar checagens antes do commit para evitar inconsistências no repositório.  
- Hooks de validação/regeneração podem impedir que diagramas desalinhados com o FDD cheguem à base principal.