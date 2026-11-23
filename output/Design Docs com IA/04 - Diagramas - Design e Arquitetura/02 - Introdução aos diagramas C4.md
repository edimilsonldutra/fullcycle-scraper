Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17071)

## Resumo da aula

O modelo C4 organiza a arquitetura do mesmo sistema em níveis progressivos de detalhe. Em vez de concentrar tudo em um único diagrama, ele separa contexto, containers, componentes e código para que cada visão responda a uma pergunta diferente. Isso reduz ambiguidade na comunicação arquitetural e permite aprofundar a análise sem perder coerência entre as camadas. Retomando a ideia de diagramas como redução de custo cognitivo, o ganho aqui está em estruturar essa redução de forma sistemática.

C1, C2, C3 e C4-Code representam quatro profundidades de leitura do mesmo sistema. O C1 mostra o sistema em seu ambiente, incluindo usuários e sistemas externos; o C2 mostra os containers que compõem a solução; o C3 detalha os componentes internos de um container; e o C4-Code, quando necessário, aproxima a documentação da organização do código. A utilidade do modelo está justamente nessa progressão: sair de uma visão macro e chegar ao detalhe estrutural sem trocar de domínio nem reconstruir a explicação do zero.

A leitura progressiva é a regra central do C4: cada nível aprofunda o anterior, em vez de substituí-lo. Isso evita diagramas superlotados e permite adaptar a explicação ao público, à decisão técnica e ao tipo de dúvida em discussão. Em uma conversa executiva, o contexto pode bastar; em uma revisão de implementação, componentes ou código passam a ser mais úteis. O valor não está em produzir todos os níveis sempre, mas em escolher o nível certo para a pergunta certa.

O site c4model.com funciona como a referência oficial para entender a proposta do modelo, sua terminologia e os tipos de diagrama esperados. Como foi escrito por Simon Brown, criador do C4, ele serve como fonte primária para alinhar nomenclatura e intenção arquitetural. Isso é especialmente importante quando times diferentes usam o termo “C4” de forma vaga ou incompleta. Consultar a referência oficial reduz interpretações divergentes e melhora a consistência da documentação.

Structurizr é uma ferramenta associada ao ecossistema C4 que ajuda a modelar uma base arquitetural e visualizar os diagramas derivados dela. A ideia central é manter uma representação estruturada do sistema e explorar diferentes visões a partir dessa base, em vez de desenhar cada diagrama manualmente e de forma isolada. Esse tipo de abordagem favorece consistência entre níveis e facilita evolução da documentação ao longo do tempo. Para equipes que querem operacionalizar C4 com menos esforço manual, Structurizr é uma referência importante.

PlantUML é um meio textual comum para gerar diagramas C4 sem depender de edição gráfica manual. A definição do diagrama passa a ser escrita em texto, o que permite versionamento, revisão e automação com o mesmo fluxo já usado em desenvolvimento de software. Isso combina bem com a proposta do capítulo de gerar e manter diagramas a partir de documentos-fonte. Quando a equipe quer integrar arquitetura ao repositório e ao processo de revisão, a abordagem textual reduz atrito operacional.

A IA pode apoiar a interpretação arquitetural ao ler descrições do sistema e inferir contexto, fronteiras, relações e níveis de detalhe compatíveis com o modelo C4. O ponto importante não é apenas desenhar caixas e setas, mas ajudar a transformar uma base textual em visões arquiteturais úteis para análise, refatoração e geração de artefatos técnicos. Esse apoio depende de uma estrutura clara de leitura, e o C4 oferece exatamente essa moldura conceitual. Ainda assim, a validação humana continua sendo necessária para confirmar se a interpretação corresponde ao sistema real.

Retomando o exemplo do Rate Limiter, o avanço agora não está no domínio do problema, mas na forma de observá-lo em camadas. O mesmo sistema será lido em contexto, containers, componentes e código, sem trocar de exemplo a cada aprofundamento. Isso permite acompanhar como uma única solução arquitetural muda de escala conforme a pergunta fica mais ampla ou mais detalhada. A próxima etapa natural dessa progressão é o C1, que mostra o Rate Limiter no seu ambiente externo.

## Transcrição

00:00

Bom, pessoal, então, conforme eu falei no vídeo anterior, vamos agora mergulhar um pouco nesse mundo dos diagramas, tá? Diagrama C4, tá? O que, resumidamente, é um diagrama C4? Depois eu vou deixar, inclusive, aqui pra você o site oficial do Simon Brown, que é um camarada que criou esse formato de diagrama, mas a ideia é o seguinte.

00:23

A Diagrama C4, na realidade, é um modelo para representar a arquitetura em diversos níveis de detalhes. Ele organiza a visualização de como o sistema se relaciona com os usuários e sistemas externos, quais containers o compõem,

00:42

como cada parte interna é estruturada e, se necessário, como o código está organizado. Essa estrutura também facilita para que os agentes de A possam entender o contexto do sistema, permitindo análise, refatoração e geração de artefatos técnicos com mais precisão.

01:00

Então, o que você pode tirar aqui desse parágrafo que eu coloquei? É o seguinte, o diagrama C4 consegue representar o nosso sistema e com quem o nosso sistema se conversa. Mas o ponto interessante do diagrama C4 é o nível de granularidade que esse tipo de diagrama tem. E ele chama C4 porque existem quatro Cs no final das contas. Então, a gente tem o C1, o C2, o C3 e o C4.

01:27

E cada um desses C's tem um nível de cobertura em relação à parte de detalhes. Então isso é interessante porque você consegue ver o sistema de um nível extremamente alto, mas ao mesmo tempo você consegue ver o sistema de um nível extremamente baixo. Antes de eu seguir, inclusive aqui com a apresentação, galera, eu queria

01:52

recomendar que vocês acessassem depois esse site, ele chama c4model.com e, basicamente, se você olhar aqui embaixo, fala que esse é o site oficial do diagrama C4 que foi escrito pelo Simon Brown. O Simon Brown é o camarada que criou esse diagrama, inclusive existe diversos workshops, vídeos no YouTube, etc, dele falando isso.

02:16

inclusive ferramentas que ele chegou a criar e etc., que ajudam a gerar esses diagramas também de uma forma bem interessante, tá? Mas, aqui fica uma referência bem interessante, onde ele acaba explicando e trazendo os tipos de diagramas, e você vai perceber que nós temos o System Context Diagram, aqui, o Container, a Component e o Code, tá? E, baseado nesses quatro tipos de diagrama,

02:44

O nosso objetivo aqui é como que eu consigo gerar esse cara, porque existem diversas ferramentas para fazer. Inclusive o Simon Brown, se eu não me engano, ele tem, ou ele é uma empresa, alguma coisa desse tipo, que tem uma ferramenta chamada Structurizer, que ajuda muito você conseguir pegar uma base,

03:00

e conseguir brincar pelos aspectos que esse sistema tem através dessa base, desse Structurizer, para que você consiga ver os diagramas, tá? Mas, normalmente, é muito comum de a gente trabalhar com Plant,

03:16

UML, plant UML, para fazer esses tipos de geração. Então, essa era a ideia que eu queria deixar claro aqui para você. C4 são quatro níveis de profundidade para você entender o seu sistema e, novamente, para a gente sempre ajustar as expectativas aqui, galera.

03:34

Meu ponto aqui não é dar aula de C4 pra vocês, tá? Meu ponto aqui é como que facilmente você consegue entender a ideia dos diagramas C4 e como que a gente consegue fazer com que a IA nos ajude nesse processo, tá bom? E recomendo, claramente, depois, que você se aprofunde um pouco mais, entenda um pouco melhor sobre isso porque

03:58

Esses diagramas, eles não são aqueles diagramas extremamente difíceis de entender e chatos de olhar, tá? Então, eu acho que fica aí a dica para você se aprofundar um pouco depois, beleza? No nosso próximo vídeo, nós vamos aí conseguir entender um pouco melhor sobre o nosso C1, tá? O System Context ali pra gente. Vamos nessa!

## Resumo IA

**Abreviações**  
- **C1**: primeiro nível do modelo C4, equivalente ao **System Context Diagram**.  
- **C2**: segundo nível do modelo C4, equivalente ao **Container Diagram**.  
- **C3**: terceiro nível do modelo C4, equivalente ao **Component Diagram**.  
- **C4**: quarto nível do modelo C4, equivalente ao **Code Diagram**.  
- **IA**: Inteligência Artificial.  
- **UML**: Unified Modeling Language.  

**Resumo**  
A aula apresentou o modelo C4 como uma forma de representar a arquitetura de software em níveis progressivos de detalhe, evitando a concentração de informações em um único diagrama. O instrutor explicou que o objetivo central do C4 é organizar a leitura do sistema em quatro profundidades: C1 para mostrar o sistema em seu contexto, incluindo usuários e sistemas externos; C2 para identificar os containers que compõem a solução; C3 para detalhar os componentes internos de um container; e C4 para aproximar a documentação da organização do código, quando isso for necessário. A ideia principal é que cada nível responde a uma pergunta diferente e aprofunda o anterior, sem substituí-lo, o que ajuda a manter coerência entre as visões e reduz o custo cognitivo da análise.

Também foi destacada a importância do site oficial **c4model.com**, criado por Simon Brown, como referência para terminologia, intenção do modelo e tipos de diagrama esperados. O instrutor mencionou ainda ferramentas do ecossistema C4, como o **Structurizr**, usado para manter uma base arquitetural estruturada e gerar visões derivadas com consistência, e o **PlantUML**, abordado como alternativa textual para descrever e versionar diagramas diretamente no fluxo de desenvolvimento. Em seguida, reforçou que o foco da aula não era ensinar o C4 em profundidade, mas mostrar como entender rapidamente sua lógica e como a IA pode ajudar a interpretar descrições do sistema para produzir visões arquiteturais mais úteis. O exemplo citado foi o **Rate Limiter**, que será analisado nas próximas etapas nas camadas de contexto, containers, componentes e código.

**Pontos de atenção**  
- O modelo C4 não deve ser usado para “colocar tudo em um diagrama”; a proposta é separar as visões por nível de detalhe.  
- Cada nível tem uma finalidade específica: escolher C1, C2, C3 ou C4 depende da pergunta que se quer responder.  
- Em discussões executivas, o C1 pode ser suficiente; em revisões de implementação, C3 ou C4 tendem a ser mais adequados.  
- O valor do C4 está na progressão entre níveis, e não na produção obrigatória de todos os diagramas em todo projeto.  
- Consultar a referência oficial em **c4model.com** ajuda a evitar uso impreciso ou “vago” do termo C4 entre equipes diferentes.  
- **Structurizr** é útil para manter consistência entre diagramas a partir de uma base única, evitando desenhos isolados e inconsistentes.  
- **PlantUML** favorece versionamento, revisão e automação, sendo mais alinhado ao fluxo de desenvolvimento do que diagramas puramente gráficos.  
- A IA pode auxiliar na leitura e síntese arquitetural, mas a validação humana continua necessária para confirmar se a interpretação corresponde ao sistema real.  
- O exemplo do **Rate Limiter** será reutilizado nas próximas aulas; a atenção deve estar em como o mesmo sistema muda de escala entre as camadas, e não em trocar de domínio a cada aprofundamento.