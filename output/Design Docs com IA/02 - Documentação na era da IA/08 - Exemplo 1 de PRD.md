Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16971)

## Resumo da aula

Um catálogo de produtos vira uma feature com identidade própria quando centraliza informações críticas do e-commerce e passa a alimentar múltiplos pontos do sistema. Nesse cenário, ele deixa de ser apenas uma tabela de produtos e se torna a fonte única da verdade para descrições, variações, preço, estoque e disponibilidade. Isso importa porque reduz divergência entre áreas, evita planilhas paralelas e cria uma base confiável para vitrine, checkout e operação interna. No exemplo, a centralização existe para que toda leitura relevante de produto venha do mesmo serviço oficial.

O resumo do PRD de feature não precisa ser longo; ele precisa condensar o que a feature faz, por que ela existe e quais partes do sistema dependem dela. No caso do catálogo, poucas linhas já deixam claro que há um serviço central, APIs de leitura, painel interno e um contexto de sistema proprietário, sem depender de plataformas prontas como Shopify ou VTEX. Essa densidade inicial é valiosa para IA porque reduz inferência solta logo no começo do documento. O objetivo do resumo é permitir que qualquer agente, humano ou não, entenda rapidamente a unidade de produto que será detalhada depois.

Bullet points não são apenas escolha estética; eles funcionam como mecanismo de compressão semântica para documentos operacionais. Em PRDs de feature, essa forma melhora escaneabilidade, reduz burocracia textual e facilita localizar público, cenários, problemas, escopo e restrições sem percorrer blocos longos de prosa. Isso também ajuda a IA a segmentar melhor o contexto, porque cada item tende a carregar uma ideia mais isolada e referenciável. Quando o documento precisa ser consultado repetidamente durante implementação e refinamento, legibilidade rápida vira ganho operacional.

Retomando a estrutura já conhecida do PRD de feature, o valor novo aqui está em como cada seção ganha texto concreto. O público não é só o cliente final da loja: inclui também o time comercial e operacional, além de serviços internos como carrinho e checkout. Os cenários de uso mostram a cadeia completa de consumo do catálogo, desde a vitrine até a compra, e deixam explícito que alterações internas precisam refletir rapidamente no front-end. Esse encadeamento transforma o catálogo em infraestrutura de produto, não apenas em cadastro administrativo.

Objetivos ficam úteis quando são amarrados a uma métrica observável e a uma meta explícita. “Tornar o catálogo a única fonte de produto” só vira direção operacional quando se mede a porcentagem de páginas servidas pelo catálogo oficial e se define uma meta como 100% da loja. O mesmo vale para reduzir exposição de itens indisponíveis ou acelerar atualização comercial: cada intenção precisa de um indicador verificável e de um alvo numérico. Essa ligação evita objetivos vagos e melhora tanto priorização quanto validação posterior.

Lembrando a seção de escopo já estabelecida anteriormente, o ponto central aqui é a concretização dos limites. Colocar dentro do escopo itens como SKU, variações, preço, estoque, APIs de listagem e painel interno delimita claramente o que a feature entrega. Colocar fora do escopo checkout, frete, regras fiscais, multimoeda, CMS editorial e blog impede que o catálogo absorva responsabilidades de outros domínios. Essa separação reduz expansão informal de requisitos e protege o design técnico de premissas erradas.

SKU é a unidade operacional que conecta cadastro, estoque, preço e compra, por isso ele aparece como elemento estrutural do catálogo. A vitrine consome dados de leitura para exibir produto e disponibilidade, enquanto o checkout depende de um snapshot consistente de preço, estoque e SKU no momento da compra. Juntar esses três pontos no PRD mostra que a feature precisa servir tanto navegação quanto transação, mesmo sem incluir o checkout no escopo. O documento, assim, registra dependência funcional sem confundir fronteiras de responsabilidade.

Um painel interno de gestão muda a natureza da feature porque transfere autonomia operacional para a área comercial. Em vez de depender de desenvolvedores para publicar produto, alterar preço, ajustar estoque ou controlar visibilidade, o time de negócio passa a operar diretamente sobre o catálogo. Isso reduz tempo de atualização e conecta o objetivo de agilidade a uma capacidade concreta do sistema. No exemplo, essa autonomia é parte do valor de produto, não um detalhe de interface administrativa.

Os requisitos funcionais já foram definidos anteriormente; a novidade aqui é a forma de escrevê-los para uso operacional com IA. Ao numerar itens como RF-001, RF-002 e assim por diante, o time ganha uma referência estável para pedir implementação, revisão, teste ou refinamento sem repetir o texto inteiro do requisito. Esse padrão melhora rastreabilidade humana e também reduz ambiguidade em prompts, porque “implemente o requisito funcional 001” aponta para um bloco específico do documento. A numeração transforma o PRD em contexto indexável.

No exemplo, o requisito de criar produto com nome, descrição e categorias já inclui fluxo principal, alternativas, erros previstos e prioridade, o que aproxima o texto de uma especificação acionável. Os requisitos não funcionais complementam esse bloco com restrições como P95 abaixo de 150 ms, alta disponibilidade, segurança, observabilidade e acessibilidade. A arquitetura registra apenas o necessário para alinhamento — microserviço dedicado, API em Go, PostgreSQL, indexação, painel em Next.js e integrações relevantes — sem substituir o design doc. Fechando o ciclo, critérios de aceitação e estratégias de validação convertem o documento em base verificável para entrega, testes e liberação.

Essas seções já são conhecidas, mas aqui aparecem materializadas em decisões reais do domínio. Isolar o catálogo em um microserviço, usar PostgreSQL como fonte da verdade e depender de pipeline de imagens ou política de estoque são escolhas que afetam implementação e operação. Riscos como produto sem estoque aparecer como disponível, divergência de preço e navegação lenta mostram por que o PRD precisa antecipar falhas plausíveis antes do desenho técnico detalhado. O ganho não é burocrático: é reduzir surpresa durante construção e evolução da feature.

## Transcrição

00:01

Bom, pessoal, agora chega um pouco de escalidró. Eu sei que é bastante teoria, é bastante fundamento, mas realmente não tem como a gente fugir disso. A gente tem que entender um pouco melhor essas coisas. Então, somente para a gente poder tangibilizar um pouco mais aquilo que eu falei agora há pouco, eu criei dois exemplos de um PRD

00:23

para uma feature. E que, normalmente, isso pode ser muito útil, tá? Tanto para a sua equipe, mas também para a inteligência artificial ver como é que as coisas funcionaram, tá? Então, é o seguinte, esse PRD é para uma plataforma de e-commerce de catálogo de produtos.

00:40

Basicamente é isso. Ou seja, são um catálogo de produtos que eu quero desenvolver para um e-commerce. Eu posso colocar a versão, a data, o responsável, os responsáveis, última atualização e coisas desse tipo. Não tem problema nenhum. Esses são os campos que você pode escolher tranquilamente.

00:55

E aqui, se você perceber, olha só o resumo desse cara. Perceba que esse documento, ele não é gigante, tá? Então, ele fala, ó, essa feature implementa um catálogo de produtos central do e-commerce, esse catálogo será a fonte única da verdade para os dados de produto, que vão ter descrições, variações, preço, estoque, disponibilidade, ele expõe APIs de leituras para vitrine e checkout e fornece um painel interno de gestão para o time comercial operacional sem depender de engenharia,

01:21

o catálogo nasceu num sistema novo proprietório de e-commerce, não em cima de um Shopify, um Vitex da vida ou outras plataformas prontas. Ou seja, é um resumo simples, mas que já dá uma ideia geral do que é o produto, tá? Aí, a granularidade, a quantidade de informação vai depender muito da necessidade do tamanho do projeto.

01:40

E aqui a gente tem contexto do problema, tá? Galera, eu gosto muito de trabalhar em bullet points, que é mais fácil para ler, tem menos burocracia e a gente consegue simplesmente tangibilizar melhor. Então, contexto do problema. Público-alvo. Time interno de operações e comercial que precisa cadastrar e atualizar produtos sem depender do desenvolvedor. Clientes que navegam e compram na loja online. Serviços internos com carrinho e checkout que precisam de dados consistentes e atualizados.

02:06

Cenários de uso chave. O cliente navega pela vitrine e vê o produto com preço e disponibilidade. O checkout lê o snapshot do preço, de estoque, o SKU no momento da compra. O time comercial pode alterar o preço, o estoque, visibilidade. Isso reflete imediatamente na vitrine.

02:24

Onde essa feature vai ser implementada? Novo sistema proprietário de e-commerce, é um serviço de catálogo de produtos exposto a uma API interna, é consumido por um front-end público e pelo módulo de checkout. Problemas priorizados. Não existe hoje uma base central de produtos, cada área mantém uma planilha própria, o que causa a divergência de preço e disponibilidade, produtos esgotados continuam aparecendo, não há controle de avaliação e etc. Não vou ficar lendo isso tudo.

02:53

Objetivos e métricas. Aqui está um ponto importante. Ou seja, objetivo, tornar o catálogo a única fonte de produto. Métrica, porcentagem de páginas servidas a partir do catálogo oficial. Ou seja, eu consigo realmente ver que todas as páginas que

03:12

as pessoas estão acessando se essas páginas que elas estão acessando realmente estão vindo do catálogo de produto. Ou seja, qual que é a minha meta para esse objetivo? 100% da loja. Ou seja, eu quero que 100% das pessoas acessem todos os produtos por esse catálogo. Outro ponto, reduzir exposição de itens indisponíveis. Taxa de cliques em itens marcados como indisponíveis, menor que 2%. Acelerar a publicação e atualização pelo time comercial. Tempo médio para publicar ou atualizar preço, menor que duas horas, por exemplo.

03:42

E aqui a gente tem o escopo. Perceba, galera, eu sempre tento trabalhar ao máximo com bullet points. Então, escopo. Estrutura do produto e SKU com nome e descrição, suporte a múltiplas variações, preço base e preço promocional, estoque para SKU, flags de publicação, API de deslistagem, API de detalhe de produto, painel interno de cadastro, auditoria, integração. O que está fora do escopo? Checkout e cobrança, cálculo de frete, regras fiscais, recomendação personalizada, catálogo multilingua, multimoeda,

04:11

CMS Editorial Avançado, com reviews, landing page promocional, blog, etc. Então, isso aqui é o que está fora e ali é o que está dentro. Agora, aqui a gente entra com requisitos funcionais, tá? E, normalmente, os requisitos funcionais você pode criar um prefixo para ele, tá? Não é obrigatório, mas normalmente você pode trabalhar isso, principalmente porque quando você for falar com a IA, você pede para ela implementar o requisito funcional 001,

04:37

E aí, já vai estar claro para ela o que ela vai ter que implementar, por exemplo, tá? Então, primeiro requisito funcional é criar o produto com nome, descrição e categorias. O fluxo principal é usuário interno acessa, seleciona, cria o produto, informa o nome, salva o rascunho e o publica. Fluxos alternativos, erros previstos, prioridade alta. Gestão de variações.

04:57

O requisito funcional 3, API de listagem de produto, API de detalhe do produto, auditoria de alteração de preço, requisitos não funcionais, P95 das APIs menor que 150 milissegundos, a listagem deve continuar responsiva, disponibilidade 99.9, segurança e autorização, observabilidade, confiabilidade, compatibilidade e portabilidade, compliance, acessibilidade, etc.

05:24

Arquitetura e abordagem. O catálogo de produtos será um microserviço dedicado. O front-end público consegue consumir apenas endpoints de leitura. Componente. A gente vai ter uma API back-end escrita em Go, um banco de dados PostgreSQL, a gente vai ter uma camada de indexação para busca e listagem, vai ter um painel administrativo em Next.js, vai ter um módulo de auditoria, vai ter integração com o checkout, módulo de frete, serviço de mídia que armazena e serve imagens.

05:49

Trade-offs, catálogo isolado com o microserviço, a justificativa, o trade-off, a decisão, o post-release como fonte da verdade, dependências externas, design, dependência organizacional, política de estoque, dependência técnica, pipeline de imagens, risco e mitigação, produto sem estoque aparecer como disponível, o que a gente tem que fazer,

06:14

divergência de preço, pode ser um risco, navegação lenta, critérios de aceitação. Aqui é aquele checklist que eu falei para vocês, que tudo isso aqui tem que constar ok para garantir que realmente essa minha feature, ela realmente vá para o ar. E como que eu valido isso aqui também? Ou seja, quais são os testes e como que eu valido isso? Então, eu tenho diversas estratégias aqui para validação.

06:41

Pessoal, é bastante pra caramba, coisa pra caramba, né? E você deve tá pensando, cara, é chato fazer isso, realmente, gasta um tempo e tudo mais.

06:51

mas, novamente, é um ativo para o seu projeto. Eu tenho um segundo exemplo aqui que eu vou mostrar para vocês em seguida. Obviamente, eu não vou ler ele totalmente, mas é importante para você conseguir entender que pode ser desde um catálogo de produtos ou até um projeto mais técnico que a gente queira desenvolver, tá? Então, vamos nessa.

## Resumo IA

**Abreviações**  
- **PRD**: *Product Requirements Document* (Documento de Requisitos do Produto).  
- **SKU**: *Stock Keeping Unit* (Unidade de Manutenção de Estoque).  
- **P95**: percentil 95, métrica de latência usada para indicar o tempo abaixo do qual 95% das requisições são atendidas.  
- **API**: *Application Programming Interface* (Interface de Programação de Aplicações).  
- **Go**: linguagem de programação Go.  
- **PostgreSQL**: sistema gerenciador de banco de dados relacional PostgreSQL.  
- **Shopify**: plataforma de e-commerce Shopify.  
- **VTEX**: plataforma de e-commerce VTEX.  
- **CMS**: *Content Management System* (Sistema de Gerenciamento de Conteúdo).  
- **Next.js**: framework web baseado em React.  

**Resumo**  
A aula mostrou como transformar um catálogo de produtos em uma feature com identidade própria dentro de um e-commerce, tratada como fonte única da verdade para descrições, variações, preço, estoque e disponibilidade. O instrutor explicou que um PRD de feature não precisa ser longo, mas deve ser objetivo e denso o suficiente para que humanos e IA entendam rapidamente o que será construído, por que a feature existe e quais partes do sistema dependem dela. Para isso, apresentou a estrutura em bullet points como forma de compressão semântica e melhor escaneabilidade, destacando contexto do problema, público-alvo, cenários de uso, local de implementação, problemas priorizados, objetivos com métricas, escopo, requisitos funcionais, requisitos não funcionais, arquitetura, trade-offs, riscos, critérios de aceitação e validação.  

No exemplo, o catálogo atende não só clientes da loja, mas também times internos de operação e comercial, além de serviços como carrinho e checkout, que precisam consumir dados consistentes. Foram descritos cenários como navegação na vitrine, leitura de snapshot no checkout e atualização de preço, estoque e visibilidade pelo time comercial, com reflexo rápido no front-end. O objetivo principal é centralizar o produto no catálogo oficial e medir isso por métricas observáveis, como porcentagem de páginas servidas pelo catálogo, taxa de exposição de itens indisponíveis e tempo médio de publicação ou atualização. Também foi reforçada a importância de delimitar claramente o que está dentro e fora do escopo, evitando que o catálogo absorva responsabilidades de checkout, frete, regras fiscais, multimoeda, CMS editorial ou blog.  

A aula também mostrou como numerar requisitos funcionais para facilitar rastreabilidade e uso com IA, permitindo citar itens específicos para implementação, revisão e testes. Um exemplo de requisito funcional foi a criação de produto com nome, descrição e categorias, com fluxo principal, alternativas, erros e prioridade. Os requisitos não funcionais incluíram metas de desempenho, disponibilidade, segurança, observabilidade, confiabilidade e acessibilidade. Na parte de arquitetura, o catálogo foi posicionado como um microserviço dedicado, com API em Go, PostgreSQL como base de dados, camada de indexação para busca e listagem, painel administrativo em Next.js, módulo de auditoria e integrações com checkout, frete e serviço de mídia. Por fim, o instrutor destacou trade-offs, dependências externas e riscos como produto indisponível aparecer como disponível, divergência de preço e navegação lenta, reforçando que o PRD deve antecipar problemas e servir como base verificável para desenvolvimento, testes e liberação.  

**Pontos de atenção**  
- O PRD de feature deve ser conciso, mas suficientemente denso para evitar interpretações vagas.  
- Bullet points ajudam na leitura, na organização do contexto e na consulta recorrente durante implementação.  
- Defina claramente o público-alvo: clientes, operação, comercial e serviços internos podem ter necessidades diferentes.  
- Sempre relacione objetivos a métricas observáveis e metas numéricas; objetivo sem métrica vira intenção genérica.  
- Delimite bem o escopo para evitar expansão informal de requisitos e confusão entre domínios.  
- Separar o que está fora do escopo é tão importante quanto listar o que está dentro.  
- SKU é elemento estrutural: conecta catálogo, estoque, preço e compra; trate-o com cuidado.  
- Mesmo sem incluir checkout no escopo, o catálogo precisa fornecer dados consistentes para ele.  
- Um painel interno de gestão dá autonomia ao time de negócio e reduz dependência de engenharia.  
- Numerar requisitos funcionais melhora rastreabilidade, referência em conversas e uso com IA.  
- Requisitos funcionais devem incluir fluxo principal, alternativas, erros previstos e prioridade.  
- Requisitos não funcionais não são opcionais: performance, disponibilidade, segurança e observabilidade precisam aparecer.  
- A arquitetura deve registrar o necessário para alinhamento, sem substituir o design técnico detalhado.  
- Escolhas como microserviço dedicado, PostgreSQL e indexação têm impacto direto em implementação e operação.  
- Antecipe riscos plausíveis, como divergência de preço, estoque incorreto e lentidão de navegação.  
- Critérios de aceitação e estratégias de validação são essenciais para confirmar que a feature realmente pode ir para produção.