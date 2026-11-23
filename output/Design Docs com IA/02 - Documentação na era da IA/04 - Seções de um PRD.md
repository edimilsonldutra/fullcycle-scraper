Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16967)

## Resumo da aula

PRD não é um template rígido com campos obrigatórios e nomenclatura fixa. As seções variam conforme o tamanho da iniciativa, o nível de granularidade e a necessidade real de alinhamento. Em projetos pequenos, algumas partes podem ser omitidas sem prejuízo; em iniciativas mais amplas, a ausência dessas seções costuma reduzir clareza. O ponto central é cobrir o contexto necessário para contar a história do produto de forma útil para o time e para a IA.

A seção de visão e propósito registra a ideia central do produto e a razão de sua existência. Ela responde qual problema ou direção estratégica justifica a iniciativa, sem entrar ainda em implementação técnica. Esse bloco funciona como referência de intenção: quando decisões posteriores geram dúvida, a visão ajuda a verificar se o produto continua coerente com o motivo original de existir.

Contexto e oportunidade explicam em que cenário o produto surge e qual benefício ele pode gerar para a organização. Isso inclui tanto produtos voltados ao mercado quanto soluções internas, desde que exista ganho operacional, estratégico ou econômico. Sem esse enquadramento, o documento vira apenas uma lista de desejos; com ele, cada decisão passa a ter vínculo com uma necessidade real do negócio.

Público identifica quem será afetado ou atendido pelo produto, enquanto personas transformam esse público em perfis mais concretos de uso. Uma persona pode representar um grupo por faixa etária, domínio técnico, idioma, rotina ou tipo de problema enfrentado; em alguns casos, também pode refletir papéis internos de um departamento. O objetivo não é inventar personagens por formalidade, mas explicitar para quem o produto faz sentido e quais necessidades devem orientar decisões de produto.

Os objetivos já definem o que a iniciativa quer alcançar; aqui, o ponto novo é que eles precisam aparecer acompanhados de medição verificável. Se não há forma de observar resultado, o objetivo não orienta priorização nem valida sucesso. Métricas tornam o PRD auditável: elas permitem saber se o produto avançou na direção esperada ou se apenas gerou entrega sem impacto.

O escopo, já estabelecido como limite da iniciativa, ganha aqui uma função estrutural dentro do PRD: delimitar fronteiras explícitas. Ele informa o que faz parte do produto e o que fica de fora, evitando que o documento cresça por expectativa implícita. Quando esse limite não é declarado, times diferentes passam a assumir versões diferentes do mesmo projeto.

Requisitos de alto nível descrevem capacidades macro que o produto deve oferecer, sem decompor fluxos técnicos ou regras detalhadas. No exemplo do e-commerce, vender camisetas, permitir escolha de cor, realizar checkout e viabilizar entrega são capacidades do sistema, não especificações de implementação. Esse tipo de requisito organiza o produto em blocos funcionais amplos e prepara a transição para documentos mais detalhados depois.

Uma seção de estratégia registra como a iniciativa pretende sair da intenção para a execução. Isso pode incluir fases, marcos ou uma sequência de evolução do produto, ajudando o time a entender ordem, dependências e prioridades. Mesmo sem detalhamento técnico, essa visão evita tratar o produto como um pacote monolítico que será entregue de uma vez só.

Riscos documentam fatores que podem comprometer prazo, valor, adoção ou viabilidade da iniciativa. Eles existem para antecipar incertezas relevantes, não para listar qualquer possibilidade genérica de problema. Quando o PRD explicita riscos, o time consegue avaliar trade-offs com mais maturidade e evita planejar como se o cenário fosse totalmente estável.

KPIs são indicadores usados para acompanhar se a iniciativa está progredindo corretamente ou se já atingiu o resultado esperado. Diferentemente de uma meta genérica, um KPI precisa ser observável ao longo do desenvolvimento ou após a entrega. Essa seção transforma sucesso em algo monitorável, o que é essencial para decidir continuidade, ajuste de rota ou encerramento.

Stakeholders são todas as pessoas ou papéis com interesse direto na iniciativa, como desenvolvimento, produto, liderança executiva e outras áreas impactadas. Torná-los explícitos no PRD reduz ruído sobre quem influencia decisões, quem valida entregas e quem precisa ser consultado. Essa seção também ajuda a evitar que o documento seja lido como se dissesse respeito apenas ao time de produto.

Essa lista representa uma anatomia típica de um PRD amplo, não um checklist universal. Nem todo documento precisará de todas as seções, e o nível de detalhe muda conforme a granularidade: um PRD mais macro tende a ser mais amplo e menos minucioso do que um PRD de feature. A utilidade do documento depende menos do nome exato das seções e mais da presença das informações necessárias para contextualizar corretamente o produto.

## Transcrição

00:01

Bom, pessoal, e falando em PRD ainda, então a gente tem alguns pontos importantes, tá? Quais são sessões, partes importantes que normalmente a gente vê em um PRD? E somente para fazer já um disclaimer aqui, não significa que todo PRD tem exatamente todas essas sessões, com esses nomes e coisas desse tipo, tá? Mas normalmente são coisas muito parecidas ou com palavras, a semântica acaba sendo a mesma, tá? Mas, de forma geral,

00:31

Primeira coisa que você tem que saber é que o PRD pode ser totalmente flexível. Então, não fique ali agoniado querendo que o PRD, às vezes, tenha todas as sessões somente porque você viu aqui nesse Scaledraw. Então, um PRD pode ser totalmente flexível e, em muitos casos, nem todas as sessões necessariamente devem ser utilizadas, principalmente em um projeto pequeno. Mas a gente tem alguns pontos importantes aqui de sessões.

00:59

visão e propósito, ou seja, qual que é a ideia principal por trás do projeto e o porquê que esse cara existe, ou seja, falar do produto e o propósito desse produto. O contexto que a gente tem e a oportunidade, perceba galera, isso é um documento de produto,

01:21

o produto que você entrega vai ajudar a empresa, ou seja, existem oportunidades que vão trazer pra empresa, de alguma forma, quando esse produto existir, tá? Nem que seja até um produto pra desenvolvimento interno, isso vai ser, de alguma forma, benéfico pra empresa. Público e personas, ou seja, quem são as pessoas afetadas, tá? E personas, normalmente, o que a gente acaba fazendo? A gente pode mapear, inclusive, a...

01:50

pessoas específicas de um determinado departamento, ou eu posso definir, né, olha, esse produto vai ser utilizado para pessoas que tenham entre 18 e 25 anos, que normalmente sabem falar inglês, que entendem de inteligência artificial, que têm problemas assim e assim assado. Eu posso criar isso, o nome desse cara é Roberto.

02:12

Eu tenho agora a Roberta, eu tenho o Fulano e o Ciclano. É muito comum a gente fazer esses tipos de mapeamento, mas normalmente nos PRDs a gente não chega nesse ponto tão detalhado, mas a gente pode falar que são as pessoas que participam, que vão utilizar, que vão ter relações com esse produto.

02:29

Outra coisa que é importante é quais são os objetivos claros desse projeto. E se eu tenho um objetivo, eu tenho que conseguir metrificar se eu conseguir alcançar esse objetivo. Então, você vai perceber que as métricas são pontos extremamente importantes, porque quem não mede, não gerencia. Basicamente é isso. E nós temos também o escopo. A parte do escopo é muito importante porque acaba dizendo o que entra

02:55

naquele projeto, naquele produto, e o que não entra. Então, o escopo realmente vai criar ali um muro dizendo até onde esse projeto vai. E aí a gente começa a entrar em requisitos de alto nível, ou seja, são capacidades macro que o produto deve oferecer.

03:15

Ou seja, de forma geral, esse produto, esse e-commerce, ele deve permitir com que a gente consiga fazer vendas de camiseta, que a pessoa consiga escolher a cor e, em seguida, ela pode fazer a compra e ter entregue esse produto um dia na casa dela. Ou seja, basicamente, é algo bem de alto nível, mas, se você perceber,

03:39

Eu estou falando em camiseta, eu estou falando em checkout, eu estou falando em entrega, e se você começar a perceber, isso são capacidades, capabilities, que o sistema acaba tendo. E aí, qual vai ser a estratégia para desenvolver esse produto? Quais são as fases que a gente vai ter para desenvolver esse produto? Quais os riscos que a gente tem para alguma coisa der errado?

04:02

quais são as KPIs, ou seja, os Key Performance Indicators, ou seja, quais são os indicadores que eu tenho que esse projeto está pronto ou que ele está sendo desenvolvido e que ele está indo pelo caminho certo, e quais são os Stakeholders, ou seja, todas as pessoas que estão envolvidas nesse projeto.

04:20

desde o desenvolvedor até a pessoa de produto, até um CTO, até um CEO. Não interessa. Então, essas são as seções encontradas em um PRD. Agora, você vai ver que no próximo vídeo, apenas para esse aqui não ficar muito grande, a gente vai começar a separar dois tipos de PRD. E vai ter um dos tipos de PRD que é o que a gente mais vai focar aqui. Beleza?

## Resumo IA

**Abreviações**  
- **PRD** — *Product Requirements Document* (Documento de Requisitos do Produto)  
- **KPI** — *Key Performance Indicators* (Indicadores-Chave de Desempenho)  
- **CTO** — *Chief Technology Officer* (Diretor de Tecnologia)  
- **CEO** — *Chief Executive Officer* (Diretor Executivo)  

**Resumo**  
A aula explicou que um PRD não é um documento rígido com um conjunto fixo de seções, nomes ou estrutura obrigatória. Sua composição varia conforme o tamanho da iniciativa, o nível de detalhamento necessário e o contexto do projeto, podendo ser mais enxuto em demandas pequenas ou mais completo em produtos maiores. O instrutor destacou que o objetivo principal do PRD é registrar o contexto necessário para comunicar a história do produto de forma útil para o time e para a IA, evitando ambiguidades e alinhando expectativas.

Entre as seções mais comuns, foram citadas visão e propósito, que registram a ideia central do produto e a razão de sua existência; contexto e oportunidade, que situam o problema ou cenário de negócio e mostram o benefício esperado para a organização; público e personas, que identificam quem será afetado ou atendido e transformam esse público em perfis mais concretos; objetivos e métricas, que definem o que se quer alcançar e como medir se houve sucesso; escopo, que delimita claramente o que entra e o que fica fora do produto; requisitos de alto nível, que descrevem capacidades macro sem entrar em detalhes técnicos; estratégia, que organiza fases e evolução da iniciativa; riscos, que antecipam incertezas e possíveis impactos; KPIs, que monitoram progresso e resultado; e stakeholders, que listam as partes interessadas e envolvidas na iniciativa. A aula também reforçou que a utilidade do PRD está menos no nome exato das seções e mais em conter as informações necessárias para orientar decisões e dar clareza ao desenvolvimento.

**Pontos de atenção**  
- O PRD deve ser flexível; nem todo projeto precisa conter todas as seções.  
- Em projetos pequenos, algumas partes podem ser omitidas sem prejuízo.  
- Os nomes das seções podem variar, mas a semântica e a intenção devem permanecer equivalentes.  
- A seção de visão e propósito não deve entrar em detalhes de implementação técnica.  
- Contexto e oportunidade são essenciais para evitar que o documento vire apenas uma lista de desejos sem vínculo com necessidade real do negócio.  
- Personas não devem ser criadas apenas por formalidade; elas precisam representar usuários ou perfis relevantes de forma útil para decisão de produto.  
- Objetivos precisam ser acompanhados de métricas verificáveis; sem mensuração, não há como validar sucesso.  
- O escopo deve deixar explícito o que faz parte e o que não faz parte da iniciativa, para evitar interpretações diferentes entre times.  
- Requisitos de alto nível devem permanecer macro, sem descer para regras detalhadas ou fluxo de implementação.  
- Estratégia deve mostrar fases, marcos ou sequência de evolução, evitando tratar o produto como algo monolítico entregue de uma vez.  
- Riscos devem registrar incertezas relevantes, não qualquer problema genérico.  
- KPIs precisam ser observáveis durante o desenvolvimento ou após a entrega.  
- Stakeholders devem ser explicitados para reduzir ruído sobre influência, validação e consulta.  
- Em PRDs mais amplos, a ausência dessas informações tende a reduzir clareza e alinhamento.