Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16965)

## Resumo da aula

Documentação de software se organiza melhor quando cada categoria responde a uma pergunta diferente do projeto. Documentação de produto define o que será construído e por que isso existe; documentação de design e arquitetura define como a solução será implementada; documentação de infraestrutura define onde e com quais recursos a solução será provisionada. A camada operacional cobre como manter a aplicação em funcionamento, enquanto conhecimento e referência registram como trabalhar no contexto do sistema. Essa separação evita que documentos misturem objetivos incompatíveis e melhora a comunicação entre produto, engenharia e operação.

A fronteira principal está entre intenção de produto e decisão técnica. Produto descreve escopo, objetivo e motivação; não detalha a estrutura técnica necessária para implementar a solução. Design docs começam quando a discussão sai do “o quê” e “por quê” e entra no “como”, “onde”, “como manter” e “como trabalhar”. Essa distinção é central porque o restante do capítulo trata PRD como documento de produto e design docs como documentos técnicos complementares, não como sinônimos.

Design docs não formam um único documento universal, mas um conjunto de artefatos técnicos com finalidades diferentes. Entram nesse guarda-chuva documentos de design e arquitetura, infraestrutura, operação e conhecimento técnico de referência, porque todos orientam a construção, provisão, manutenção e evolução do software. Chamar qualquer documento de design doc apaga diferenças importantes de público, profundidade e uso. Tratar design docs como categoria técnica ajuda a escolher formato, nível de detalhe e momento de criação de cada documento.

Um mapa simples resolve boa parte da ambiguidade documental: produto responde o quê e por quê; design e arquitetura respondem como; infraestrutura responde onde e com o quê; operacional responde como manter; conhecimento e referência respondem como trabalhar. Esse mapeamento funciona como vocabulário comum do time e reduz confusão sobre o papel de cada artefato. Quando um documento tenta responder tudo ao mesmo tempo, ele tende a ficar genérico, redundante ou difícil de manter. Separar por função torna a documentação mais útil tanto para pessoas quanto para sistemas de IA.

Cada tipo de documentação representa uma necessidade diferente do projeto e, por isso, exige decisões diferentes de escopo, timing e granularidade. Um documento técnico não precisa repetir a justificativa de produto inteira, assim como um documento de produto não precisa antecipar detalhes de provisionamento ou operação. A escolha do tamanho e da profundidade do documento depende da situação: o tipo correto de documento vem antes do template correto. Essa visão mais crítica evita produzir artefatos extensos, mas pouco acionáveis.

A documentação já foi posicionada anteriormente como contexto operacional para IA; aqui, o avanço está em organizar esse contexto por categoria documental. Quando os tipos de documento estão bem delimitados, a IA consegue gerar artefatos mais coerentes com o objetivo de cada um, em vez de misturar requisitos, arquitetura e operação no mesmo texto. A mesma lógica vale para manutenção: atualizar um documento fica mais simples quando seu papel está claramente definido. Estrutura documental clara melhora tanto a produção quanto a preservação do contexto ao longo do tempo.

Prompt Engineering ganha relevância porque a qualidade do documento gerado depende da instrução dada à IA sobre tipo, objetivo, escopo e profundidade do artefato. Pedir “gere um design doc” é vago; pedir um documento técnico de arquitetura, infraestrutura ou operação produz saídas mais úteis porque a categoria já delimita o conteúdo esperado. Isso transforma prompt em mecanismo de operacionalização da taxonomia documental. Quanto mais claro o enquadramento do documento, maior a chance de a IA gerar e manter artefatos consistentes.

## Transcrição

00:01

Agora, galera, chegou um ponto muito, mas muito importante aqui da nossa disciplina, que é em relação aos tipos de documentação. Por que eu estou dizendo isso? Porque a nossa disciplina, principalmente, o foco dela é em design docs, ou seja, documentos, vamos dizer assim, de design.

00:23

Agora, o que acontece que a gente tem que ter uma clareza enorme na hora de fazer documentação ou os famosos design docs? Você tem que ter uma clareza do que

00:38

faz parte de Design Docs e do que não faz parte de Design Docs. Então, normalmente, a gente tem diversos tipos de documentação. A gente tem documentações que têm muito foco no produto. E o que isso significa? Significa define o quê e o porquê.

00:56

Toda vez que você vai desenvolver um software, esse software por si é um produto, e esse produto, a gente tem a definição do que é esse produto e o porquê que esse produto está sendo criado. Então, nós temos documentações mais focadas especificamente na área de produtos. Agora,

01:18

Além da documentação de produto, nós temos documentações de design e arquitetura, ou seja, é o como. Então o produto define o quê e o porquê. O design e arquitetura define como que a gente vai fazer isso, tá?

01:37

A infraestrutura, ou seja, a gente tem documentações de infraestrutura, elas vão falar o quê? Onde e com o quê a gente vai fazer o nosso produto? Ou seja, aonde que eu vou provisionar esse meu produto? E com o quê? Quais ferramentas? Qual plataforma? Como que isso vai ser? Tá?

01:55

E a gente tem a parte operacional, ou seja, como que eu vou manter a minha aplicação. E também eu tenho documentações de conhecimento e referência, que no final das contas significa como trabalhar.

02:11

Então, se você entender essas categorizações, eu acho que vai ficar cada vez mais claro a gente manter um nível de comunicação nessa disciplina, que a gente fale a mesma língua. Obviamente, essas categorias que eu estou falando aqui para vocês, em algumas empresas, elas podem ser

02:34

chamadas de outros nomes e etc, mas a nossa questão aqui é você entender a ideia, tá? E tudo isso que eu coloquei entre parênteses é muito importante para que você consiga entender, né? Por que que a gente tem tipos de documentação e o que que aquele tipo de documentação representa para o projeto. Então, o produto define o quê e o porquê.

02:57

design e arquitetura fala pra gente como, infraestrutura fala onde e com o que, operacional como que eu mantenho e o conhecimento e documentações de conhecimento e referência é como que eu vou trabalhar. Agora, o ponto importante é que quando a gente está falando de documentações, de design e arquitetura, infraestrutura, operacional e conhecimento e referência,

03:20

Esses tipos de documentação são o que a gente chama de design docs. Então, claramente para você, pense o seguinte, design docs normalmente sempre vão ser documentações de nível técnico.

03:37

de nível de como você desenha o seu software, para que esse software seja provisionado, mantido, e quais são as guidelines que eu vou ter, ou metodologias, etc., que eu vou utilizar para desenvolver esse software.

03:55

Então, é muito comum você ver no mercado pessoas falando que qualquer coisa é Design Docs, ou que Design Docs é apenas uma única coisa, ou um único documento. Não, entenda que Design Docs acabam sendo um conjunto de documentos, onde cada conjunto de documentos tem objetivos diferentes,

04:18

E esses objetivos podem estar dentro dessas categorias que eu acabei trazendo aqui para você. E durante essa disciplina, basicamente, o que a gente vai fazer é entender, na realidade, quais são os principais design docs que a gente tem dentro dessas categorias,

04:37

você vai ver como é que são esses caras, aí eu vou mostrar templates desses caras pra vocês, e você também vai ter prompts que vão te ajudar a também gerar essas documentações, tá? Então, eu acho que o nosso ponto principal aqui é exatamente esse, que você tenha uma clareza.

04:57

clareza, claro, ficou bonito, né? Mas que você tenha ali uma visão mais crítica agora do que é design docs pra você, o que você precisa, em qual situação, como, quando, qual tamanho do documento e coisas desse tipo. E o mais interessante de tudo isso que é tendo a IA por trás, nos ajudando a

05:17

criar, a gerar essas documentações. E por isso que a parte de Prompt Engineering brilha nesses aspectos, porque simplesmente é um caminho muito forte para que a gente faça com que essas documentações sejam geradas, se elas sejam mantidas e etc. Beleza? Então, vamos nessa!

## Resumo IA

**Abreviações**
- **PRD**: *Product Requirements Document* — documento de requisitos de produto.
- **IA**: Inteligência Artificial.

**Resumo**
A aula apresentou uma visão organizada dos tipos de documentação em projetos de software, enfatizando que cada categoria deve responder a perguntas diferentes para evitar confusão e sobreposição de conteúdo. A documentação de produto foi posicionada como responsável por definir o quê será construído e por quê; a documentação de design e arquitetura, por explicar como a solução será implementada; a documentação de infraestrutura, por indicar onde o sistema será provisionado e com quais recursos; a documentação operacional, por descrever como manter a aplicação em funcionamento; e a documentação de conhecimento e referência, por orientar como trabalhar no contexto do sistema. O instrutor destacou que essa separação melhora a comunicação entre produto, engenharia e operação, além de facilitar a criação, manutenção e reutilização dos documentos.

Foi reforçado que “design docs” não significam um único documento, mas um conjunto de artefatos técnicos com finalidades distintas, incluindo design e arquitetura, infraestrutura, operação e conhecimento técnico de referência. A aula enfatizou a fronteira entre intenção de produto e decisão técnica: documentos de produto tratam de escopo, objetivo e motivação, enquanto documentos técnicos entram no “como”, “onde” e “como manter”. Também foi mostrado que o nível de detalhamento e o tamanho do documento dependem do tipo de documentação e da necessidade do projeto, evitando artefatos genéricos, redundantes ou difíceis de manter. Por fim, o instrutor conectou essa taxonomia documental ao uso de IA e Prompt Engineering, explicando que prompts mais específicos, que informam tipo, objetivo, escopo e profundidade do artefato, geram documentos mais consistentes, úteis e fáceis de atualizar.

**Pontos de atenção**
- Não misturar documentação de produto com documentação técnica.
- Produto responde **o quê** e **por quê**; design e arquitetura respondem **como**; infraestrutura responde **onde** e **com o quê**; operacional responde **como manter**; referência responde **como trabalhar**.
- “Design docs” não é um único documento: é um conjunto de documentos técnicos com propósitos diferentes.
- Evitar documentos que tentam responder tudo ao mesmo tempo, pois tendem a ficar genéricos, redundantes e difíceis de manter.
- O tipo de documento deve vir antes do template: primeiro definir a categoria e o objetivo, depois o formato.
- O nível de detalhe e o tamanho do documento devem ser ajustados à situação e à necessidade do projeto.
- A clareza na taxonomia documental ajuda tanto pessoas quanto IA a produzir e manter artefatos mais coerentes.
- Pedidos vagos para IA, como “gere um design doc”, tendem a gerar saídas pouco úteis; é melhor especificar tipo documental, escopo e profundidade.
- A documentação deve ser pensada também como contexto operacional para manutenção e continuidade ao longo do tempo.