Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17128)

## Resumo da aula

ADR Generator é o agente que transforma um artefato intermediário em uma ADR formal. Retomando as Potential ADRs já identificadas, ele usa esse dossiê técnico como entrada e produz um documento estruturado em formato MADR, com contexto, decisão, opções consideradas, consequências e referências. A utilidade dele está em converter evidência dispersa em documentação padronizada, sem começar do zero. Essa geração, porém, só é confiável quando a decisão pode ser inferida a partir de código, histórico e documentos de apoio.

A passagem de Potential ADR para ADR formal reduz especulação porque a escrita não parte diretamente do codebase cru. O agente lê categoria, prioridade, score, datas, decisões extraídas e contexto histórico, e reorganiza isso em um template estrito. Esse fluxo é deliberado: primeiro levantar evidência, depois formalizar. Quando essa ordem é invertida, a IA tende a preencher lacunas com texto plausível, mas não necessariamente verdadeiro.

A geração automática pode ser limitada às decisões classificadas como Must Document, deixando Consider fora do fluxo padrão. Isso impõe um filtro operacional importante: a automação formaliza primeiro o que já tem evidência forte de impacto arquitetural. Se for necessário incluir casos intermediários, o comando pode aceitar um parâmetro adicional para expandir o escopo. O efeito prático é evitar inflar o acervo com ADRs fracas ou prematuras.

O comportamento do gerador depende fortemente do prompt e dos parâmetros passados. É possível definir idioma, limitar a quantidade de arquivos de referência, remover code blocks e instruir o agente a escrever em nível arquitetural, enfatizando padrões, tecnologias high-level, trade-offs e fatores de negócio. Esse controle existe para impedir que a ADR vire uma colagem de trechos de código ou uma descrição excessivamente local da implementação. O resultado esperado é um documento legível como decisão, não como dump técnico.

Needs Input é um marcador explícito de lacuna informacional dentro da ADR gerada. Ele aparece quando a IA consegue estruturar o draft, mas não consegue sustentar partes do racional com evidência suficiente, especialmente em fatores de negócio, estratégia, stakeholders, iniciativa ou custo. Em vez de alucinar uma justificativa, o agente sinaliza exatamente onde o complemento humano é obrigatório. Isso transforma incerteza em item revisável, o que é muito mais seguro do que esconder a ausência de contexto.

Uma ADR é inferível quando o código, o histórico de Git e os documentos correlatos deixam claro o problema, a escolha feita e parte relevante dos trade-offs. Já uma ADR que exige input humano depende de motivações que não ficam materializadas nos artefatos técnicos, como restrições contratuais, decisões executivas, contexto competitivo ou critérios comerciais da época. A distinção é operacional, não filosófica: ela define se o agente pode concluir a redação sozinho ou se deve interromper com perguntas abertas. Esse critério evita tratar toda decisão arquitetural como se fosse puramente técnica.

As datas não são detalhe cosmético; elas ancoram a decisão no momento em que ela fez sentido. Quando o gerador consulta first commit, evolução de arquivos e relações temporais, ele consegue reconstruir quando uma escolha surgiu, o que ela substituiu e com quais outras decisões ela se conecta. Isso melhora a qualidade do contexto e reduz ADRs anacrônicas. Se o repositório não tem histórico disponível, a formalização perde precisão temporal e parte do racional fica mais fraca.

Uma ADR formal pode registrar dependências, substituições e alterações parciais entre decisões. No exemplo de meios de pagamento, uma decisão inicial baseada em PayPal pode depois ser parcialmente alterada por outra ADR ligada ao uso de Pagar.me, preservando a linha evolutiva em vez de apagar o passado. O mesmo vale para decisões complementares, como auditoria por webhooks ou ajustes de confiabilidade em mensageria. Essas relações transformam ADRs isoladas em memória arquitetural navegável.

O fluxo operacional é simples: executar o comando de geração, ler as Potential ADRs priorizadas, disparar agentes por candidato e produzir arquivos formais em uma pasta de saída. O template pode usar numeração provisória como XXX quando ainda não faz sentido consolidar a ordem definitiva do acervo. Depois da geração, a revisão humana verifica contexto, datas, relações, trade-offs e campos marcados com Needs Input. Só então o documento deixa de ser draft automatizado e passa a ser ADR confiável.

Em projetos pequenos, sem histórico de Git e com pouco contexto documental, a IA ainda consegue montar contexto, opções, prós, contras e referências de código, mas o resultado tende a ser mais raso. Já em repositórios com histórico real, a qualidade sobe porque o agente recupera datas, decisões relacionadas e sinais de evolução arquitetural ao longo dos anos. Retomando o cenário de RabbitMQ, a formalização não para na adoção inicial: ela também consegue registrar decisões posteriores, como confirmações para aumentar confiabilidade. Mesmo assim, quando surgem perguntas como “por que a empresa exigiu checkout com e-mail corporativo?” ou “qual restrição de negócio motivou autenticação básica em 2013?”, a resposta correta continua sendo pedir complemento humano.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior, a gente colocou aqui onde nós conseguimos gerar as ADRs potenciais. Isso não significa que nós vamos criar as nossas ADRs nessas, elas são potenciais. Agora, uma coisa interessante é que a gente tem um outro agente aqui, e esse agente aqui é o ADR Generator. Esse cara, sim, é o cara que gera o ADR aqui pra gente. Então,

00:32

Ele é especialista em gerar ADR, ele tem alguns princípios críticos, eu posso escolher até a linguagem, se é em português, se é inglês, da ADR que eu vou trabalhar, pedir para ele considerar no máximo de 3 a 5 arquivos de referência. E uma das coisas que são muito importantes, pessoal, que eu queria trazer aqui para você é o seguinte, muitas ADRs,

00:55

elas não são tomadas apenas por questões técnicas, são por questões estratégias, de negócio e etc. Então, se você olhar, não dá pra eu sair gerando ADR da minha cabeça, principalmente quando eu tô falando de uma ADR que foi

01:15

A decisão dela ter sido criada foi uma decisão estratégica da empresa, tá? Então, uma coisa que eu queria que você entendesse é que não tem mágica de como você fazer uma IA sair criando ADRs desenfreadamente e falar que elas estão todas prontas. Por quê? Porque não tem como elas estarem 100% prontas, porque ela não tem como adivinhar a cabeça do seu chefe há cinco anos atrás, quando ele decidiu fazer com que

01:44

Essa biblioteca foi usada em relação à outra e depois, naquela época, ele lembrou que os termos de uso daquela licença não dava para a empresa. Entende? Então, o que eu tomei o cuidado de fazer aqui para que fique mais fácil de você entender? Todas as ADRs que forem extremamente técnicas e que esteja cada vez claro por que a decisão foi tomada, ela vai ser gerada já meio que automaticamente. Agora,

02:15

quando, baseado obviamente no prompt e tudo mais, quando pauta alguma informação, eu coloco na DR esse needs input. O que isso significa? Que a DR vai ter o draft dela, mas no meio dela vai ter needs input, onde eu tenho que complementar com informações,

02:41

porque não tem como AIAD adivinhar. É basicamente isso. Porque não tem como você gerar uma ADR da sua cabeça. Não. Existem ADRs que até dá para ser geradas sem precisar de um input humano depois, porque dá para inferir muita coisa. Agora, existem outras ADRs que são claramente o que você precisa. Então, na hora que a gente for gerar ADR, deixa eu já dar um generate aqui enquanto a gente está falando,

03:08

Quando a gente for gerar ADR, eu vou dar aqui, barra ADR, Generate aqui pra mim, tá? E eu vou dar um Enter agora aqui.

03:20

E ele vai começar a rodar e ele vai começar, no final das contas, a olhar todo o relatório que eu gerei de Potential ADRs, que ele acabou gerando, ele vai olhar aquilo e provavelmente ele vai começar a rodar os agentes. Olha só, ele está com vários agentes rodando, provavelmente cada um agente por ADR, por Must Document. E se você perceber, esse comando que eu estou dando, ele vai gerar ADR somente das que eu falei Must Document.

03:49

o consider ele não está gerando a não ser que eu passe um parâmetro menos menos inclui de consider aí ele vai gerar dos que é pra gente considerar ter a dr ou não tá mas aqui ele tá pegando aqueles documentos potenciais da dr então aqui eu falo da linguagem a pedir pra ele remover code blocks né não ficar colocando código no meio de tudo isso manter sempre conceitos arquiteturais padrões a tecnologias

04:17

de high-level, trade-offs, fatores de negócio, e aí eu dou exemplos aqui muito claros, para ele não ficar usando o código, mas no final das contas transformar isso em texto, tá? Então, o que é bom, o que é ruim? O que é bom, o que é ruim? Como que você pode extrair os dados? Olha lá no Git,

04:37

Olha, o first commit foi tal dia, quando que ele foi identificado. Então, eu pedi pra ele colocar também, olha, pra ele detectar quando um documento substituiu o outro documento também, tá?

04:53

Aí, como que a ADR tem que funcionar? Pode ver que é MADR Format, ou seja, Formato Estrito de como que deve ser. Aqui é o template de como que a ADR deve ser gerada. Aí são os inputs, onde ela vai gerar os dados, pontos críticos, output. E aí, como que funciona o workflow? Inicialize, passo argumentos, faço o numbering. Como eu não sei quais ADRs eu vou querer ou não,

05:17

eu fiz questão de não colocar o número da ADR, eu tô colocando XXX e depois se a gente quiser, a gente pode rodar um prompt e pedir pra ele sair numerando as ADRs pra gente caso tenha essa necessidade, tá? Mas o ponto importante aqui pra gente entender é que eu não quero sair dando números nas ADRs aqui, nesse momento pelo menos não.

05:39

E aí ele fala, olha, olhe a potencial ADR, extrai os dados, a categoria, a prioridade, o score, extrai a informação, extrai as decisões, as datas, falo muito das datas, para ele buscar o contexto estratégico caso eu tenha passado, sei lá, o meu FDD ou outros documentos. E daí eu coloquei, ó,

06:02

pedir para ele separar as que ele acha que a gente precisa dar informações adicionais dentro de uma pasta chamada Needs Input.

06:11

Ou seja, ele vai pedir que a gente complemente aquele documento porque ele não tem informação para falar daquilo, tá? E daí tem algumas palavras, keywords, para ele colocar ali no needs input, stakeholder, business, iniciativa, estratégia, cost... Ou seja, todas essas palavras principais vão fazer com que a IA fale, opa, essas informações não tem como eu ter, logo, eu vou colocar como needs input ali pra gente.

06:40

e daí cria umas lógicas, daí gera o arquivo formal, os decisions e etc. Basicamente é prompt, prompt, prompt, galera. Mas o ponto que eu mais queria trazer aqui pra vocês em relação é vocês entenderem o fluxo e depois você pode olhar com calma aqui pra gente. Bom, aparentemente ele gerou

07:03

as ADRs aqui pra gente, não tenho a mínima ideia de como que vai ficar esse documento aqui, mas vamos aqui olhar documentos, e aqui eu tenho Generated, e aqui ele tem CMD e ele gerou uma ADR.

07:20

Domain, ele gerou outra cara aqui, middleware. Esses caras aqui já deveriam estar colocados, por isso que ele numerou, eu acho. Na realidade, eu acho que já devia ter uma pasta aqui no passado, alguma coisa desse tipo. Mas, storage, tá? Então, sei lá, vamos ver storage. Aqui ele gerou uma ADR.

07:39

de storage. Então, foi aceito. A data não sabe, porque eu não tenho histórico de commit, não tem repositório aqui dentro. E aqui ele traz o contexto, os pontos de decisão, porque ele olhou o contexto do meu documento, opções que foram consideradas, decisões

08:00

que resultaram nisso, prós e contras ele já sugere aqui pra você, as consequências que isso acabam trazendo, e as referências em código e etc que ele encontrou. Então foi dessa forma que ele acabou gerando essas ADRs pra mim, tá? Mas essas aqui, olhando, pessoal, elas são meio chatas, por quê?

08:20

É um código muito pequeno, de um projeto bem simples, que não está usando histórico de Git, um tema extremamente pequeno. Então, para que eu pudesse mostrar um pouco para vocês que ficasse talvez um pouco mais legal, o que eu resolvi fazer? Eu criei um repositório privado no GitHub, esses documentos são documentos secretos, vamos dizer assim, tá? Mas olha só que interessante.

08:47

Eu vou rodar com eles aqui, um a um, para que vocês consigam entender um pouco melhor. Porque dá para perceber que tem um monte de ADR aqui gerada, né? Então, olha só que interessante esse tipo de documento.

08:58

ADR XXX, porque eu não nomeei. E ele fala, ela foi aceita e ela foi criada, baseada em 2013, 1º de janeiro de 2013. Como que ele sabe disso? Histórico de GitHub, de commit. E ela está relacionada com essas outras ADRs aqui também. Trouxe o contexto.

09:19

os decisions drivers aqui pra mim, as opções eram consideradas no momento daquela época, inclusive tem grupos, anotações, etc. Cara, é muito legal porque eu participei do desenvolvimento desse sistema lá em 2013. Na realidade foi em 2012 que a gente começou a mexer nele.

09:37

aí mostrou os padrões, prós e contras, as consequências, as referências e tudo mais. Então, se você olhar, ele gerou realmente uma ADR. E se eu clico nesse cara aqui, ele vai me mandar para um outro documento que fala sobre esse cara. E aqui ele fala, olha, em julho de 2013, a Full Cycle Code Platform precisava de um framework para lidar com autenticação, autorização, registrar frameworks, etc.

10:05

e foi utilizado esse cara e etc. E aqui, olha o que ele colocou aqui pra mim, galera. Isso que eu queria falar pra vocês. Needs Input. Quais foram os requisitos de negócio que fizeram com que, em 2013, você realmente precisasse, de uma forma clara, trabalhar com essa forma de autenticação básica.

10:31

E aqui tem Decision Drivers, tudo que ele acha que ele tem que perguntar, ele pergunta. E é óbvio, galera, você vai fazer algo, você tem que revisar. Mas o ponto é que ele trouxe muita coisa interessante. Ele trouxe o que pode ser de bom, o que pode ser de ruim, pontos alternativos, consequências, opa, outras formas alternativas. Existe alguma outra alternativa lá em 2013 que poderia te ajudar? E trouxe mais referências, consequências e pediu também outros inputs de consequências que esse cara

11:00

poderia ter sido gerado. Outro cara aqui interessante, tá? Olha só, pessoal. Lembra que eu falei dos status pra vocês? Essa decisão, ela foi tomada em 2014. E é uma decisão que ela depende da decisão que a gente usou, que a gente usava tanto pra empresa no Brasil como nos Estados Unidos, o PayPal.

11:23

Depois a gente teve uma decisão relacionada, que depende, com um sistema de auditoria baseado em webhooks.

11:32

quando a gente começou a trabalhar com outras formas de pagamento no Brasil, e o mais louco é que foi amended by, ou seja, e foi parcialmente essa DR, foi grudada, baseada na decisão dessa outra DR, onde a gente mudou, por exemplo, naquela época, para trabalhar com o Pagar.me, que é o gateway de pagamento.

11:56

E aqui está a DR que foi aceita especificamente dessa do Pagar.me em relação ao Paypal e etc e tudo mais. Então, você consegue ver exatamente o que aconteceu aqui. Outra coisa aqui...

12:12

Paypal Domestic vs International Market Segmentation. Aqui ele pegou um outro caso, aqui foi o que a gente clicou na realidade. E isso você vai perceber que vai precisar de input, provavelmente aqui, needs input.

12:27

Ou seja, existem decisões, galera, que a IA não tem como saber. E aí, ó, precisa de input. Precisa de input pra gente conseguir colocar ali pra gente. Ah, aqui tem um outro cara, RabbitMQ. A gente começou a usar RabbitMQ em 2021 na empresa.

12:46

E aí, estratégia, o que estava acontecendo, porque que rolou, as decisões e tudo mais. Quais foram as opções consideradas, porque a gente estava realmente, na época, na dúvida, quais as formas e os padrões que a gente ia utilizar para fazer com que as informações fossem parar na fila, se a gente ia trabalhar com outras formas. As decisões, a decisão que foi tomada, prós e contras, as outras opções que a gente tinha, que era o Reds Pub Sub.

13:15

e a forma de ficar chamando do banco de dados direto, consequências que aconteceram, arquivos e tudo mais aqui pra gente. E aí, o muito louco de tudo isso, sabe o que que é? É que ao longo do caminho, a gente teve que mudar algumas coisas no RabbitMQ em relação à parte de confiabilidade. Então, se eu clicar aqui numa decisão,

13:36

vai falar que aqui eu precisei tomar uma decisão de sempre fazer a confirmação para não ter perigo de perder a mensagem na fila. E aqui foi a decisão, o que foi bom, o que foi ruim, etc, etc, em relação às decisões. Outra coisa, a parte de vendas aqui, a gente teve uma época, a gente teve que começar a trabalhar com o RabbitMQ e outras formas assíncronas para fazer a integração na parte de vendas.

14:04

Então, trouxe toda a parada aqui novamente pra gente em relação às categorias e tudo mais. Outro cara aqui, Needs Input também.

14:14

A... Checkout, Authorization, tá? Então, a gente tem a área B2B na empresa e a gente tem uma forma de Checkout, onde quem tá naquela empresa tem que ter o e-mail corporativo e dados corporativos pra ele conseguir fazer o pagamento, tá? Ó, é algo novo que, inclusive, que acabou implementando. E o porquê disso? Needs Input, tá vendo?

14:37

Qual outra forma de decisão? Por que você resolveu fazer isso aqui fora esses outros pontos prováveis? Qual foi o outcome? O que aconteceu? A fricção? Quais outros pontos foram contra em relação a isso? Então, needs input. Então, sempre tem coisas que a IA não tem como saber. E é por isso que é interessante. Olha esse cara aqui.

15:01

ele depende dessa e está parcialmente amended com esse cara aqui de como trabalhando com serviços e aqui foi para o link para outra DR tá então isso aqui galera somente alguns exemplos bem básicos em relação a como que você consegue gerar DR de sistemas antigos ou de novos obviamente né e que você vai o que revisar e complementar mas você não vai sair do zero e lembrando que o nível né de

15:31

de granularidade, de gerar ADR ou não e tudo mais, vai depender do prompt que você vai poder alterar, beleza? Próximo vídeo eu vou falar sobre linkagem de ADR.

## Resumo IA

**Abreviações**  
- **ADR** — *Architecture Decision Record*  
- **MADR** — *Markdown Architectural Decision Records*  
- **Git** — sistema de controle de versão distribuído  
- **GitHub** — plataforma de hospedagem e colaboração para repositórios Git  
- **FDD** — *Functional Design Document*  
- **RabbitMQ** — broker de mensagens usado para comunicação assíncrona  
- **B2B** — *Business to Business*  
- **PayPal** — plataforma de pagamentos digitais  
- **Pagar.me** — gateway de pagamentos  

**Resumo**  
A aula apresentou o agente **ADR Generator**, responsável por transformar **Potential ADRs** em ADRs formais, seguindo um template estrito em formato **MADR**. O instrutor explicou que o fluxo correto começa pela identificação e organização de evidências técnicas e históricas — como código, commits, documentos de apoio, datas, decisões e relações entre documentos — para só depois formalizar a decisão arquitetural. Dessa forma, evita-se gerar ADRs a partir de suposições ou de “texto plausível” produzido pela IA sem base suficiente.

O gerador pode ser configurado por prompt e parâmetros, como idioma, quantidade máxima de arquivos de referência, remoção de blocos de código e orientação para escrever em nível arquitetural, com foco em padrões, tecnologias de alto nível, trade-offs e fatores de negócio. Também foi mostrado que o comando pode ser restrito às ADRs classificadas como **Must Document**, deixando as de **Consider** fora do fluxo padrão, a menos que um parâmetro adicional amplie o escopo. O objetivo dessa filtragem é evitar a criação de ADRs fracas, prematuras ou desnecessárias.

Outro ponto central foi o uso de **Needs Input** como marcador de lacuna informacional. Quando a IA consegue estruturar o documento, mas não consegue sustentar parte do racional com evidências suficientes — especialmente em temas como estratégia, negócio, stakeholders, iniciativa e custo — ela marca explicitamente a necessidade de complemento humano. Isso torna a ausência de contexto visível e revisável, em vez de escondê-la em uma narrativa inventada.

A aula também mostrou como o agente extrai e organiza dados como categoria, prioridade, score, decisões, relações de dependência, substituições, datas e referências. As datas são tratadas como parte essencial da decisão, porque permitem situar a ADR no momento em que ela fez sentido e reconstruir a evolução arquitetural ao longo do histórico. O instrutor exemplificou casos em sistemas reais e antigos, como decisões envolvendo autenticação, **PayPal**, **Pagar.me** e **RabbitMQ**, mostrando como uma ADR pode apontar para outras ADRs relacionadas, registrar substituições e preservar a linha evolutiva das decisões.

O fluxo operacional descrito foi: executar a geração, analisar as Potential ADRs priorizadas, disparar agentes por candidato, produzir arquivos formais em uma pasta de saída e depois revisar manualmente o resultado. Nessa revisão, verificam-se contexto, datas, relações entre ADRs, trade-offs e campos marcados com **Needs Input**. Em projetos pequenos, sem histórico e com pouco contexto documental, a saída tende a ser mais rasa; já em repositórios com histórico real, a qualidade da formalização melhora bastante porque o agente consegue inferir melhor a trajetória das decisões.

**Pontos de atenção**  
- Não gerar ADR “do zero” sem evidência: a IA pode preencher lacunas com conteúdo plausível, mas incorreto.  
- Priorizar primeiro a identificação das **Potential ADRs** e só depois a formalização.  
- Restringir a automação às ADRs com evidência forte, especialmente as classificadas como **Must Document**.  
- Usar **Needs Input** sempre que faltar contexto de negócio, estratégia, stakeholders, iniciativa ou custo.  
- Revisar manualmente toda ADR gerada; o resultado automático é draft, não versão final confiável.  
- Controlar o prompt para evitar que a ADR vire colagem de código ou descrição excessivamente local da implementação.  
- Limitar a quantidade de arquivos de referência quando necessário, para manter o foco e reduzir ruído.  
- Registrar datas e relações temporais, pois elas ancoram a decisão no período correto e evitam ADRs anacrônicas.  
- Aproveitar o histórico de Git/commits sempre que existir; sem histórico, a precisão temporal e contextual cai.  
- Preservar relações como dependência, substituição e alteração parcial entre ADRs, em vez de apagar decisões antigas.  
- Não assumir que toda decisão arquitetural é puramente técnica; muitas dependem de fatores estratégicos e comerciais.  
- Quando a motivação da decisão não estiver materializada nos artefatos técnicos, interromper o fluxo e pedir complemento humano.  
- Manter o nível de escrita em alto nível arquitetural: padrões, tecnologias, trade-offs e impacto de negócio.  
- Tratar o número da ADR como algo que pode ser consolidado depois; usar numeração provisória, como **XXX**, se necessário.