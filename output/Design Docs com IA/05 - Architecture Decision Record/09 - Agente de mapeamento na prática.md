Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17126)

## Resumo da aula

Mapear ADRs em sistemas antigos exige um passo intermediário entre código bruto e documentação formal. Em projetos novos, as decisões podem ser registradas desde o início; em legados, o desafio é reconstruir decisões a partir de estrutura, contexto e histórico. O ADR Analyzer existe para automatizar essa descoberta inicial e transformar o codebase em evidência navegável. O objetivo não é gerar ADRs imediatamente, mas localizar candidatos plausíveis com base em sinais arquiteturais.

A primeira fase percorre o repositório para construir uma visão estrutural do sistema. Esse mapeamento identifica diretórios, módulos, padrões, tecnologias, banco de dados, mensageria, caching, cloud services, integrações e elementos cross-cutting. Também cruza código com arquivos de contexto fornecidos, como documentos do projeto, para enriquecer a interpretação. Em codebases grandes, o processo pode ser incremental, mas a função continua a mesma: produzir uma base confiável para análise posterior.

O arquivo mapping.md consolida o retrato técnico do projeto em um formato consumível por pessoas e por agentes. Ele reúne nome do projeto, propósito, overview, stack, notas de contexto, insights, módulos, localização dos componentes, dependências, padrões, arquivos principais, escopo e referências cross-cutting. Esse documento não é uma ADR e também não substitui documentação de arquitetura mais ampla; ele funciona como inventário estruturado para a próxima etapa. A qualidade desse arquivo influencia diretamente a precisão da identificação de decisões.

Arquivos de contexto melhoram o mapeamento porque ajudam o agente a interpretar o código além da superfície sintática. Quando o projeto inclui documentos explicativos, o analisador consegue fazer cross-reference entre intenção declarada e implementação observada. O campo de notas adicionais, como addContextNotes, serve para registrar inferências úteis que não aparecem claramente na estrutura do repositório. Isso reduz falsos positivos e aumenta a chance de detectar decisões realmente arquiteturais.

A segunda fase lê o mapping.md, consulta ADRs existentes e reanalisa os arquivos mais relevantes para localizar decisões estruturais. O processo não produz ADRs finais; ele gera documentos intermediários com informação suficiente para justificar uma ADR formal depois. Essa separação é importante porque mapeamento não basta para escrever uma decisão completa com contexto, trade-offs e consequências. Primeiro se identifica o candidato, depois se formaliza a decisão.

O analisador busca sinais em categorias que costumam carregar impacto arquitetural: infraestrutura, framework, plataforma, data layer, APIs, protocolos, autenticação, pagamentos, AI, real time, media processing e IoT. Essas categorias funcionam como heurísticas para concentrar a análise em escolhas com efeito sistêmico e duradouro. Elas não são fixas; podem ser adaptadas ao domínio e à stack da empresa. O ponto central é ensinar o agente a procurar decisões estruturais, não detalhes locais de implementação.

Red flags são filtros automáticos para impedir que o agente promova ruído documental ao nível de ADR. Modelagem de domínio, entidades de negócio, workflows operacionais, configurações triviais, implementações locais e detalhes excessivamente granulares devem ser desqualificados, salvo quando aparecem como estilo estrutural explícito e compartilhado. Esse filtro impede que o acervo seja inflado por classes, parâmetros e regras de negócio que pertencem a outros artefatos. A exclusão é tão importante quanto a detecção, porque um agente sem poda tende a documentar demais e documentar mal.

Depois dos filtros, o agente aplica uma pontuação baseada em critérios como escopo, impacto e aderência aos critérios já estabelecidos para ADR. O resultado separa candidatos que claramente precisam ser documentados (must document) daqueles que ainda exigem julgamento humano (consider). Essa gradação evita a falsa dicotomia entre “gera ADR” e “ignora”, que costuma produzir ou excesso documental ou omissão. A pontuação organiza a fila de análise e prioriza o que tem maior valor arquitetural.

O histórico de Git adiciona dimensão temporal à análise, algo que o estado atual do código não consegue mostrar sozinho. Com git log, --follow, diffs e busca por keywords, o agente identifica quando certos módulos surgiram, mudaram ou foram substituídos, o que ajuda a reconstruir a timeline arquitetural já vista anteriormente. Isso também reduz duplicação de ADRs e melhora a detecção de relações entre decisões. Se o Git não estiver disponível, a análise continua, mas perde evidência histórica importante.

O fluxo prático fica em quatro passos: mapear o codebase, gerar mapping.md, identificar ADRs potenciais e só então produzir ADRs formais. Retomando o cenário do Rate Limiter, o primeiro resultado útil não é uma decisão pronta, mas um mapa com módulos, storage, middleware, bootstrap, componentes centrais e trade-offs observados. Em um sistema maior, o mesmo processo ainda ordena por onde começar, indicando módulos prioritários para análise profunda. Isso transforma um repositório legado em uma fila racional de decisões candidatas, em vez de depender apenas de memória oral do time.

## Transcrição

00:01

Bom, pessoal, vamos ver as coisas aqui um pouquinho mais na prática aqui, para que vocês consigam entender, tá? E tudo isso que eu estou colocando aqui, você vai ter acesso a todos esses prompts, os agentes, etc, que eu criei. Eu tenho que dizer que eu fiquei muito feliz com que o resultado disso

00:22

que eu fui criando e lapidando ao longo do tempo, tá? E acredite, foram muitas e muitas horas dedicadas pra conseguir gerar esses tipos de resultado, tá? Isso significa que o que eu vou mostrar pra vocês é perfeito? Não!

00:41

de forma alguma, mas ele é um ponto de partida que talvez você possa fazer na sua empresa e testar, tá? Seguinte, pessoal, estou usando aqui, novamente, Cloud Code, mas, novamente, eu já falei diversas vezes, no final das contas, a gente está falando de prompts. É óbvio que cada agente de A tem o seu comportamento diferente, mas prompt é prompt e, eventualmente, você consegue utilizar isso com

01:08

com uma outra ferramenta, fazendo algumas adaptações, tá? O que acontece é o seguinte, tá? Eu criei, somente pra você olhar aqui, eu criei alguns agentes aqui. Eu criei um agente chamado ADR Analyzer,

01:26

eu criei um outro agente chamado ADR Generator, e eu criei um outro camarada chamado ADR Linker. O que esses caras fazem? Porque a gente tem uma complexidade muito grande com software, sabe qual é? Quando a gente está começando um software do zero, as coisas são mais simples na nossa vida, porque a gente define as decisões e a gente começa a criar ADRs desde o início.

01:55

Ok? Agora o ponto é, como que você consegue fazer a Architecture Decision Record de um projeto que tem 10 anos de idade?

02:06

Então, isso aí é um desafio em qualquer lugar. Agora, você já pensou em algum momento você ter a possibilidade de pegar aquele projeto legado e fazer com que a IA saia gerando as ADRs para esses projetos de tudo que foi mudado ao longo do tempo com as decisões?

02:26

Então, é exatamente isso que eu fiz nesse projeto, tá? Então, somente para você entender a dinâmica desse cara, e depois eu vou mostrar para vocês, eu peguei um sistema nosso aqui bem antigo, e vou mostrar algumas ADRs para vocês entenderem o que você é capaz de fazer hoje, tá? Então, é o seguinte, esse nosso agente ADR Analyzer, o que ele acaba fazendo aqui? Deixa eu...

02:58

Abrir aqui pra gente conseguir ver melhor. Aqui o meu zoom tá bem grande, né? Deixa eu fechar esse cara aqui. Então, basicamente, a gente tem duas fases, tá? A primeira fase é mapear o codebase do projeto. Ou seja, ele vai rodar e ele vai gerar dentro dessa pasta aqui. E depois você vai ver que a gente tem algumas regras que você pode escolher o output da pasta.

03:28

mas ele vai navegar por todo o seu projeto, e somente pra você saber, eu fiz testes com projetos enormes e o mapeamento ficou legal, tá? Mas, dependendo da situação, do tamanho do seu projeto, você pode, talvez, mapear de uma forma diferente, ou você fazer mapeamentos incrementais, etc. Mas o ponto aqui é fazer um mapeamento. O que esse mapeamento faz?

03:52

ele vai entender os diretórios do projeto, o contexto, ele vai ver qual que é o output, o diretório que ele vai gerar, ele vai ler o contexto do projeto, caso existam arquivos de contexto no projeto, posso passar documento de projeto para ficar mais fácil, ele vai analisar a estrutura do projeto, diretórios, módulos, padrões,

04:15

a localização de onde estão os arquivos do projeto, eu posso passar qual é o parâmetro. Eu vou identificar a tecnologia, a linguagem, o framework, o tipo de banco de dados, mensageria, caching, cloud services e etc. Vai mapear a arquitetura dos componentes, os módulos, os serviços, as integrações, autorização e etc. Ele vai integrar isso com insights do contexto que ele tem do projeto para fazer referência cruzada na estrutura de código com arquivos de contexto.

04:44

e também ele vai gerar um arquivo chamado mapping.md num output dir que a gente vai passar por parâmetro ali pra gente. E aqui tem os principais argumentos que eu posso passar ali como parâmetro pra esse meu agente. Então, aqui acontece o seguinte, qual que é o ponto? Carregue todos os arquivos, extrai insights, faça cross-reference, faça um enriquecimento desse contexto pra ficar um pouco melhor, tá?

05:11

e documente o contexto como addContextNotes, caso ele entenda melhor o contexto do projeto, aí ele vai gerar essa estrutura, por isso que é importante você sempre conseguir definir

05:26

qual que é o output do documento que você quer. Isso muda muito. Então eu coloquei o nome do projeto, proposta, overview, a linguagem, a stack que está sendo utilizada, as notas de contexto caso eu tenha passado o documento de contexto, os insights que ele conseguiu, os módulos do sistema,

05:45

a ideia de cada módulo, o que acontece, qual é o motivo, a localização, os componentes principais, as tecnologias, as dependências, os padrões, os arquivos principais, o escopo do projeto, ou seja, projetos ou módulos que são muito grandes, muito pequenos, e referências cross-cutting, ou seja, são aqueles layers que cruzam o projeto inteiro, independente do componente que ele está rodando.

06:13

Essa é a fase 1. A fase 2, o que ele vai fazer? Ele vai ler esse mapeamento que é gerado, tá? E aí, baseado nesse mapeamento, ele vai fazer algo bem interessante, que é fazer o quê, na realidade? Ele vai analisar tudo isso, e aqui, galera,

06:33

Foi toda uma fórmula que foi feita, acredite, deu um bom trabalho, por isso que eu não quero chegar aqui e falar, é só fazer desse jeito, não. Houve muitas, mas muitas iterações pra isso aqui ficar dessa forma, tá? Mas a ideia aqui vai ser o seguinte na fase 2. Eu vou ler o arquivo mapping, tá?

06:51

Eu vou ler também ADRs existentes, caso elas já existam, eu vou analisar os códigos baseados naquele mapping, porque o mapping traz os arquivos principais, eu vou aplicar alguns filtros de passo a passo, red flags, eu vou explicar pra vocês, e mais uma pontuação.

07:10

Vou checar isso aqui que eu acabei de filtrar e vou verificar se eu já não vou, para eu não criar uma DR que já existe ou também para que eu consiga detectar uma relação de uma DR com a outra dentro de uma timeline, tá? Porque timeline para mim é importante. Outra coisa que muda o resultado de tudo que a gente está fazendo é o Git.

07:35

porque eu peço aqui para ele usar depois na parte de comandos e etc, você vai entender um pouco melhor, onde eu falo o seguinte, começa a usar o histórico do Git para você entender melhor a timeline do projeto. Ele vai ver todos os seus commits, ele vai ver o diff dos seus commits, ele vai começar a filtrar por lá para entender a timeline do projeto, para entender os arquivos do projeto, para entender aquilo que já está mapeado, para ele conseguir fazer o quê?

08:07

Decision Identification Process. O que isso significa? Eu, nesse momento, quero identificar possíveis ADRs, tá? Por que eu estou falando possíveis? Porque eu não quero dizer que eu quero sair gerando ADRs. Porque gerar ADRs depende de muita informação.

08:33

e não apenas de um mapeamento. Então, o que eu estou fazendo? Com a base no mapeamento que eu tenho, eu faço com que esse agente, mas é uma outra parte desse agente, ele vai fazer o quê? Ele vai entender as decisões estruturais. Então, ele vai tentar capturar o que tem de mais valioso na arquitetura para isso realmente ser documentado.

08:59

e veja se ele cai em alguma das categorias. Se é um serviço de infraestrutura, como Docker, Docker Compose, Kubernetes, Cloud Services. Outra coisa, framework ou plataforma. Por exemplo, Django, Java,

09:15

usando o TypeScript com Next.js, Nest.js, Express, PHP, Symfony, Laravel, coloquei algumas categorias e coloquei também uma outra categoria que é importante, ORMs, Data Layer, no final das contas. Outra categoria, APIs e protocolos em relação à parte arquitetural. Então, o que o cara tem que detectar, pontos específicos de infraestrutura, como

09:43

processo de pagamento, autenticação, coloquei também a parte de AI, Machine Learning, caso precise, Real Time, Media Processing, IoT. Então, tudo isso você pode mudar e complementar ao longo do tempo. E eu falei, você tem que aplicar um julgamento, tá? E verificar se esse julgamento, ele é crítico o suficiente pra ter um valor e um propósito pra gente gerar isso como uma possível

10:11

a ADR, ou seja, uma Possible Architecture Decision Record. E aí a gente vai aqui ó, Red Flags for Decision que você não tem que capturar. Ou seja, é crítico. Se essa decisão bater com qualquer coisa do Step 0, em relação à categoria acima, você não vai aplicar um Red Flag, você vai dar um skip, porque a gente vai fazer uma programação baseada em pontos. Então, eu vou pontuando

10:38

para ver se vale a pena ele gerar uma DR ou não. Então, por exemplo, primeiro red flag, Domain Modeling, Entidades e não Modeling Styles. Ou seja, se

10:53

O que está sendo descrito é uma entidade de regras de negócio, ou seja, o que está sendo modelado, exemplo, uma entidade, user, order, curso, entidade de relacionamento, hierarquias de domínio, agregados, business concepts, e se sim, disqualify.

11:14

Ok? Ou seja, cara, tá falando de regra de negócio, tá falando de um monte de classe, etc. Meu, eu não quero tornar isso uma ADR. Daí eu coloquei alguns pontos importantes. Por exemplo, em DDD, as entidades por elas mesmas não devem gerar ADRs, mas...

11:30

Se o CDDD trabalha com agregados, que estão dentro de um contexto de modelagem explícita, ou se eu estou utilizando valores imutáveis de domínio para mim, ou seja,

11:52

eu posso, eventualmente, utilizar uma ADR. Porque se eu tenho coisas imutáveis, parâmetros que todo mundo vai utilizar em todos os lugares do meu projeto, eventualmente isso vale a pena virar uma ADR. Outra coisa, Red Flag 2, Business Workflow. Eu não vou ficar até o fim, galera, falando, depois você lê com calma, mas tudo que for de Business Workflow, do dia a dia, é negócio. Dados de configuração, vai rodar na porta 300, o seu timeout é de 30.

12:21

Outra coisa, implementações triviais, o código não muda faz duas semanas, ele não cruza nenhum contexto a mais, ele não afeta contratos externos, ou seja, não é ADR. Se há algo extremamente granular, também não vai ter AGR, ou seja, o tempo de expiração do meu JWT é de 15 minutos.

12:47

Ou seja, isso pra mim não faz sentido ter uma DR, ok? Agora, a gente tem a parte de pontuação, e aí a gente vai naquelas regras do 3D, por isso que eu botei ela lá. Ou seja, é estrutural, é evidente, é estável, aí a gente pode começar a trabalhar. E aí tem todo um sistema de pontos, tá? Ou seja, o escopo, o impacto, vai dar 25, 20...

13:08

Galera, é toda uma fórmula, depois você olha aqui com calma, mas o que é importante você entender, tá? E o mais importante de tudo, eu não quero deixar esse vídeo absurdamente grande, é que eu usei uma linha de raciocínio que é o seguinte. Existem algumas decisões que elas estão gritando que precisam de uma ADR.

13:30

Existem decisões que eu estou chamando de must document, ou seja, é certeza que esse cara precisa de uma DR. Mas existem alguns outros documentos, lembra que a gente caiu naquela parte meio que opcional, que eu posso considerar em fazer com que esse cara vire uma DR. Então, o que aconteceu? Eu pedi para ele fazer o seguinte, dependendo da pontuação que vai ter aqui,

14:00

você vai criar must documents, ou seja, garantido que esses documentos vão existir. Porém, dependendo da classificação, ou seja, uma prioridade média, eu coloco ele dentro de uma consider. O que isso significa? Eu vou considerar, em geral, uma DR para esse documento, tá? E eu dei vários exemplos aqui e a coisa foi longe, tá, pessoal?

14:23

E aqui é como que eu vou utilizar o Git em meu favor, tá? Ou seja, porque com o Git eu consigo ter o contexto temporal, ou seja, o contexto de tudo que aconteceu no projeto desde o início. Então, olha só, coloquei alguns exemplos. Olha, ele vai dar um Git log, menos o menos follow, pegar o GIF, a formatação, ele vai ver os commits por keywords, ele vai ver as modificações mais novas, aí ele vai extrair insights e começar a entender

14:53

baseado naquilo que ele vai pesquisar, se aquilo pode ser e como que ele vai pegar informações para gerar esse nosso documento de uma possível ADR. Então, ele vai entender o padrão, ele vai trazer evidência para a gente. Se o Git não estiver disponível, ele vai pular essa fase. Então, essa fase 2, o que ela vai fazer no final das contas, galera? Ela não vai gerar ADR.

15:20

ela vai gerar um documento de uma ADR potencial com informações o suficiente caso eu queira gerar aquela ADR.

15:32

E aí essas informações vão fazer eu gerar ADR formal. Ou seja, eu tenho algumas etapas. A minha primeira etapa é mapear, para eu conseguir ter uma ideia geral do Codebase. A segunda etapa, uma vez que eu mapeei, já que eu tenho esse mapeamento, agora eu vou tentar entender quem talvez precise ter uma ADR.

15:54

E pra cada cara desse, eu faço um zoom e trago a maior quantidade de informação que eu preciso pra esse documento que pode ser uma potencial ADR, tá? E depois disso, que a gente fizer isso, a gente vai fazer o quê?

16:10

gerar as ADRs. Então, nessa primeira parte aqui, para que você consiga entender, eu peguei um exemplo bobo aqui de Rate Limiter, mas depois eu vou mostrar exemplos de um sistema real que tem muitas ADRs criadas para ficar um pouco melhor para que vocês consigam entender. Se você olhar aqui,

16:31

eu rodei o comando //adrmap, que eu tenho comandos aqui, adrmap. Esse comando aqui, ele vai pedir para analisar o projeto, identificar as tecnologias, dividir o codebase, etc. Ele vai utilizar o map, eu posso ter os parâmetros que eu quero passar, mas no final das contas,

16:51

eu estou pedindo para ele usar o subagente que a gente está utilizando, que é o ADR Analyzer, tá? Então, esse é um comando bem simples, no final das contas, para ele fazer essa preparação. E aqui está o nosso map, mapping, deixa eu ver aqui, docs, ADRs, mapping.md. Esse mapping.md, galera, o que no final das contas ele faz?

17:19

ele é o mapeamento do que ele achou dentro do meu sistema. Então, ele colocou que o nome do projeto é um Rate Limiter em Gol, o propósito é ter uma forma previsível, com baixa latência, do Rate Limiter...

17:34

Bom, não vou ficar lendo aqui, mas identificou a linguagem, o framework, as ferramentas, a forma de storage, a forma de deployment, notas de contexto, os principais insights que ele acabou trazendo, as tecnologias, os princípios de design, aí os módulos que ele conseguiu separar, mostrou o que tem em cada módulo aqui pra mim,

17:58

botou os patterns que precisam, os arquivos principais, falou que o escopo é pequeno, botou o limiter, que é o algoritmo da parte do rate limiter, pegou os key components, trouxe alguns trade-offs, pegou a parte de persistência de storage, pegou a parte de integração com middleware, pegou também a parte de bootstrap da aplicação,

18:26

a parte cross-cutting, ou seja, aquilo que cruza o projeto inteiro, nesse caso, a como que o erro funciona, gerenciamento de configuração, de testing, de logging, de timing, research cleanup, o sumário, vamos dizer aqui, da arquitetura, o resumo da minha arquitetura,

18:45

E aqui pra mim, então, ele fez meio que um mapeamento de cada pedaço ali pra mim, tá? Então, isso aí é uma forma, mas é um projeto, vamos dizer assim, bem simples, com muito pouco, com um codebase muito pequeno, tá? E é isso que eu quero que você entenda. Agora, eu vou colar aqui pra você um mapping um pouquinho maior só pra que você consiga entender do que eu tô falando, tá? Então, olha só esse mapping aqui pra gente.

19:18

Arquitetura do sistema, esse aqui tem 1.600 arquivos, a primeira vez que foi feito, o último, quando ele foi gerado, foi a data, mas aqui, o nome do full cycle, uma platform, a linguagem que ele iniciou, era o PHP 5 na época, hoje já não roda, com uma versão legado do framework, que não é mais hoje,

19:38

Mas daí, galera, olha só, ele trouxe os principais pontos do sistema, o que usou, serialização, front-end, validação de formulários, bibliotecas adicionais, testes, ferramentas de desenvolvimento, infraestrutura, os principais módulos aqui do sistema, aqui nossos, a modelagem, daí ele traz o core, é baseado nesse bundle, os key components, etc, os arquivos principais, e assim ele vai, trazendo todos os componentes,

20:07

Vai, vai, vai, vai, vai bem longe aqui. E aí, chega uma parte desse cara, tá? Desses caras que eles começam a trazer aqui pra gente a ordem de análise. Pra eu fazer o quê?

20:23

os meus Must Documents, ou seja, ele recomenda para mim, para eu gerar a fase 2 desse meu projeto, baseado nesses módulos, onde ele fala quantos arquivos tem esses módulos e por ali que eu devo começar. Depois, uma prioridade média e uma prioridade baixa e outros caras que eu posso querer fazer de infraestrutura.

20:48

Então aqui ele já me dá uma dica por onde eu posso começar, mas gerar os documentos, mas lembre-se, ele não vai gerar a ADR, ele vai gerar um documento

21:02

que consiga trazer informações o suficiente pra gente gerar a nossa ADR. Beleza? No próximo vídeo eu vou mostrar pra vocês essa segunda parte quando ele gera esses documentos de ADRs potenciais pra que você consiga ver. Beleza?

## Resumo IA

**Abreviações**
- **ADR** — *Architecture Decision Record* (Registro de Decisão de Arquitetura)
- **AI** — *Artificial Intelligence* (Inteligência Artificial)
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **DDD** — *Domain-Driven Design* (Projeto Dirigido ao Domínio)
- **DR** — usada na aula como referência a **ADR**
- **Git** — sistema de controle de versão distribuído
- **IoT** — *Internet of Things* (Internet das Coisas)
- **JWT** — *JSON Web Token*
- **ML** — *Machine Learning* (Aprendizado de Máquina)
- **ORM** — *Object-Relational Mapping* (Mapeamento Objeto-Relacional)

**Resumo**
A aula mostrou uma abordagem prática para identificar e organizar decisões arquiteturais em projetos legados, usando agentes de IA como apoio e não como substituição do julgamento humano. O instrutor explicou que, em sistemas antigos, não basta olhar o código bruto: é preciso reconstruir contexto, estrutura e histórico para encontrar candidatos plausíveis a ADRs. Para isso, ele apresentou um fluxo em duas fases com os agentes **ADR Analyzer**, **ADR Generator** e **ADR Linker**, destacando que o foco inicial não é produzir ADRs finais, mas gerar evidências navegáveis e documentos intermediários confiáveis.

Na primeira fase, o agente percorre o codebase para mapear diretórios, módulos, padrões, tecnologias, banco de dados, mensageria, caching, cloud services, integrações e elementos que cruzam o sistema inteiro. Quando existem documentos de contexto do projeto, eles são cruzados com a estrutura do código para enriquecer a análise e registrar inferências em campos como *addContextNotes*. O resultado dessa etapa é o arquivo **mapping.md**, que consolida nome do projeto, propósito, overview, stack, insights, módulos, localização de componentes, dependências, padrões, arquivos principais, escopo e referências cross-cutting. O instrutor reforçou que esse arquivo não é uma ADR, mas um inventário estruturado que aumenta a precisão da etapa seguinte.

Na segunda fase, o agente lê o **mapping.md**, consulta ADRs já existentes e reanálise os arquivos mais relevantes para identificar decisões estruturais. Para concentrar a busca, ele usa categorias heurísticas como infraestrutura, framework, plataforma, data layer, APIs, protocolos, autenticação, pagamentos, AI, real time, media processing e IoT. Em seguida, aplica red flags para filtrar ruído documental: modelagem de domínio, entidades, workflows de negócio, configurações triviais, implementações locais e detalhes excessivamente granulares não devem virar ADR, salvo quando representam uma escolha arquitetural explícita e compartilhada. Depois disso, o agente pontua os achados por escopo, impacto e aderência aos critérios de ADR, separando o que é **must document** do que fica como **consider**.

O histórico do Git foi apresentado como um reforço importante para reconstruir a timeline arquitetural. Com comandos como `git log`, `--follow`, diffs e busca por palavras-chave, o agente consegue entender quando módulos surgiram, mudaram ou foram substituídos, reduzindo duplicações e conectando decisões em uma linha do tempo. O fluxo final explicado foi: mapear o codebase, gerar o **mapping.md**, identificar ADRs potenciais com documentação suficiente e, só então, produzir ADRs formais. Como exemplo, o instrutor mostrou um caso simples de *Rate Limiter* e outro sistema legado maior, evidenciando que o mapeamento também ajuda a priorizar por onde começar a análise profunda.

**Pontos de atenção**
- O objetivo da primeira etapa não é gerar ADRs, e sim criar um mapa técnico confiável do sistema.
- A qualidade do **mapping.md** influencia diretamente a precisão da identificação das decisões arquiteturais.
- Documentos de contexto do projeto são valiosos para reduzir falsas interpretações e enriquecer o mapeamento.
- **Mapping** não substitui documentação arquitetural mais ampla; ele serve como base para a próxima etapa.
- Não transformar qualquer detalhe do sistema em ADR: configurações triviais, workflows de negócio e modelagem de domínio normalmente devem ser descartados.
- Só considerar como ADR o que tiver caráter estrutural, evidente e estável ao longo do tempo.
- Usar pontuação e classificação ajuda a evitar a falsa dicotomia entre “gerar tudo” e “ignorar tudo”.
- Categorias de análise devem ser adaptadas ao domínio e à stack da empresa; não são fixas.
- O histórico do Git melhora muito a análise, mas, se não estiver disponível, o processo ainda pode seguir com perda de evidência temporal.
- Em projetos grandes, o mapeamento pode precisar ser incremental para continuar útil e manejável.
- A partir de documentos potenciais, ainda é necessário julgamento humano para formalizar a ADR final.
- Evitar excesso documental: documentar demais sem filtro tende a produzir ruído e piorar a qualidade do acervo.