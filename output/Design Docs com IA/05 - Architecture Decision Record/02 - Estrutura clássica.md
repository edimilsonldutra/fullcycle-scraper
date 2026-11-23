Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17119)

## Resumo da aula

Architecture Decision Record é o documento que registra por que uma decisão técnica relevante foi tomada. Ele não substitui PRD, HLD ou low-level design; cada um responde a uma pergunta diferente. PRD e HLD descrevem o que a solução é e como será estruturada em nível mais amplo, enquanto o ADR preserva a justificativa da escolha arquitetural. O low-level design, por sua vez, detalha como a decisão será implementada no código.

Um ADR se justifica quando a decisão foi debatida, envolveu trade-offs e afeta o design ou a arquitetura do sistema. Esse critério evita registrar escolhas triviais e concentra o esforço nas decisões cujo motivo tende a se perder com o tempo. Como o formato é curto e simples, o custo de manutenção costuma ser baixo em comparação com o valor histórico gerado. Retomando a ideia de timeline arquitetural já vista, cada ADR adiciona um ponto explícito nessa evolução.

O template clássico associado a Michael Nygard organiza o ADR em campos simples e suficientes para preservar o raciocínio arquitetural. A estrutura começa com um identificador numérico e um título descritivo, como “ADR-001 — Usar Redis como cache distribuído”. Esse padrão facilita referência cruzada, ordenação histórica e leitura rápida em repositórios com muitos registros. Ele funciona como baseline conceitual para entender templates posteriores mais elaborados.

O número do ADR cria uma identidade estável para o documento, independentemente de mudanças futuras no texto. O título precisa nomear a decisão de forma específica, porque ele será usado como ponto de entrada para buscas, links e discussões. “Usar Redis como cache distribuído” é melhor do que títulos vagos como “Decisão de cache”, pois já informa o objeto da escolha. Essa combinação de número e título transforma o ADR em uma unidade documental fácil de citar e relacionar.

O contexto descreve o problema, a motivação, as restrições e as forças em jogo no momento da decisão. Aqui entram limitações técnicas, conhecimento do time, custos, infraestrutura e condições do negócio que pressionam a escolha arquitetural. O objetivo não é defender uma tecnologia abstratamente, mas mostrar em que cenário concreto aquela decisão fazia sentido. Sem esse campo, a decisão vira apenas uma conclusão solta, sem as condições que a justificaram.

A seção de decisão registra qual caminho foi adotado a partir do contexto apresentado. Ela deve ser direta, porque o valor explicativo do ADR não está em esconder a escolha, mas em conectá-la às condições que a tornaram aceitável. Uma boa formulação evita ambiguidade e deixa claro o compromisso técnico assumido pelo time. Esse campo é o núcleo do documento, mas só faz sentido completo quando lido junto com contexto, alternativas e consequências.

Alternativas registram quais opções foram consideradas e por que não foram escolhidas. Esse campo é essencial porque arquitetura quase nunca envolve solução perfeita; envolve troca entre benefícios, custos, risco, prazo e capacidade operacional. Retomando o cenário comparativo entre RabbitMQ e Kafka, a escolha por RabbitMQ pode ser inferior em algum aspecto técnico isolado, mas ainda ser a melhor decisão sob restrições reais de custo, infraestrutura e conhecimento interno. O ADR torna esses trade-offs explícitos para que o futuro do sistema seja interpretado com justiça técnica.

Consequências documentam os efeitos e implicações da decisão adotada. Elas incluem ganhos esperados, limitações aceitas, impactos operacionais e possíveis custos futuros decorrentes da escolha. Esse campo impede que a decisão pareça gratuita, porque mostra o que o time aceitou em troca do benefício principal. Também ajuda revisões futuras, já que mudanças arquiteturais costumam surgir justamente quando essas consequências deixam de ser aceitáveis.

Referências conectam o ADR a outros artefatos, como outras ADRs, documentos de produto, HLDs e RFCs. Essa linkagem transforma documentos isolados em uma rede navegável de raciocínio técnico e histórico. Quando uma decisão depende de outra ou altera uma escolha anterior, o vínculo explícito reduz ambiguidade e acelera investigação. Em sistemas que evoluem por anos, essas conexões são tão importantes quanto o texto do ADR em si.

Retomando o cenário de escolha entre RabbitMQ e Kafka, o template clássico organiza a decisão em camadas claras. No contexto, entram restrições de custo, infraestrutura disponível e conhecimento do time; na decisão, registra-se a adoção de RabbitMQ; nas alternativas, Kafka aparece como opção considerada e descartada; nas consequências, ficam explícitos os benefícios operacionais e as limitações aceitas. O resultado é um documento curto, mas suficiente para explicar por que a arquitetura seguiu esse caminho e como essa escolha se conecta à evolução do sistema.

## Transcrição

00:00

Bom, pessoal, como eu falei no vídeo anterior, Architecture Decision Record é um documento extremamente relevante. Ele começou a surgir não faz muito tempo, de forma geral, se a gente comparar com outros tipos de documento que a gente acabou falando por aqui, tá?

00:15

Mas vamos lá, vamos a algumas definições e alguns pontos para ficar um pouco mais fácil de você entender, tá? Então vamos lá, um Architecture Decision Record é um documento curto e objetivo que registra uma decisão arquitetural significativa tomada em um projeto. Ele normalmente possui a seguinte estrutura.

00:35

Normalmente ele vai trazer aqui para a gente o contexto, que é o problema, a motivação e as restrições pela qual aquela decisão arquitetural está sendo realizada. Qual foi a decisão adotada, baseada nesse contexto?

00:50

Quais eram as alternativas que a gente poderia ter naquele momento e o porquê essas alternativas foram descartadas e uma determinada foi acatada. E, obviamente, os efeitos e implicações dessa decisão. A gente sabe, no mundo da tecnologia, que tudo tem o seu pró e contra. A gente sempre tem que lidar com os trade-offs e a parte de ADR a gente acaba

01:20

Nossa, mas por que você não usou isso? Opa, tá ali as alternativas e tal, porque eu acabei indo por esse caminho, tá? Mesmo que eventualmente você não concorde com o caminho que o desenvolvedor, o arquiteto, naquele momento acabou tomando, pelo menos você entendeu a linha de raciocínio e sabe que aquilo não surgiu absolutamente ali do nada, tá?

01:44

Agora, qual é a função da ADR no meio de toda essa história? Porque a ADR é apenas um documento, um tipo de documento, dentro de um ecossistema gigante de documentos que a gente pode ter num projeto. Agora, o ponto interessante aqui da ADR é que ele é um complemento vivo, entre aspas, de documentos como um PRD, um HLD, um FDD, etc. Por quê?

02:12

Porque um Product Requirement Document, um High-Level Document, eles dizem pra gente o que é e como a solução vai ser estruturada. Um ADR vai explicar o porquê uma decisão técnica foi tomada.

02:28

Um low-level design mostra como ela será materializada no código. Então, a ADR, no final das contas, ela explica, deixa eu colocar aqui, explica o porquê uma decisão técnica foi tomada. Independente se você gostou da decisão ou não, pelo menos essa decisão vai estar muito clara ali na ADR.

02:51

Então, de forma geral, tá, galera? E eu vou tentar simplificar, e ao longo aqui desse nosso bate-papo, você vai perceber que eu vou trazer, entre aspas, regrinhas, e quando eu digo regrinhas, não é algo que tá escrito em pedra, mas pelo menos que você tenha...

03:08

um baseline, um guideline para não partir do zero, basicamente é isso. Então, de regra geral, se algo foi debatido, teve trade-offs na hora da execução e teve impacto no design do sistema, na arquitetura do sistema, normalmente a gente vai...

03:28

precisar gerar uma Architecture Decision Record. Agora, uma coisa que é interessante em relação a isso é que, diferente de muitos documentos, inclusive do que os documentos que eu acabei mostrando para vocês durante todo esse processo, o desenvolvimento e o documento de uma ADR acaba sendo extremamente simples. E é por isso que é algo que vale a pena a gente investir de forma geral.

03:57

Uma coisa também que é interessante é que a DR vai acompanhar o projeto ao longo dos anos. Porque se cada momento você tomou uma decisão e essas decisões foram substituindo decisões que aconteceram antes, você consegue ver uma timeline das decisões do seu projeto. E isso realmente vale ouro. Agora, o lance é o seguinte.

04:21

tem um cara que ele se chama Michael Nygaard, tá? Esse cara é um cara extremamente inteligente, vale a pena você acessar o blog dele, apesar de faz um tempinho que ele não tinha postado, mas ele também é muito também do mundo da Microsoft, mas de forma geral, ele, em 2011, ele veio, né? Eu não sei nem dizer necessariamente se ele é o criador do conceito da DR,

04:47

Mas ele é muito famoso principalmente porque o template clássico de como que você trabalha com a Architecture Decision Record tem um padrão dele ali, tá? Então, galera, aqui tem uma estrutura bem clássica de uma ADR. Então, basicamente, a ADR tem um número, certo? E ali ela tem o título dela, que é Usar Reds como Cache Distribuído, por exemplo.

05:11

E aí, tem o contexto. Ele vai descrever o problema, as restrições que estavam acontecendo e as forças em jogo. O que isso significa? O que é aquilo que eu estava querendo? Por que aquilo estava brigando? Essas restrições que estão acontecendo aqui comigo, o negócio de como as coisas acontecem. Porque, lembre-se pessoal, quando a gente está falando em desenvolvimento de software, a gente está falando em restrições.

05:41

a gente está falando de tecnologias, a gente está falando de entendimento do time, que a gente está no momento da empresa, tá? Então, nesse momento, a gente é apertado de todos os lados, e nem sempre a decisão técnica maravilhosa vai ser tomada, mas ela vai ser tomada... Alguma decisão vai ser tomada baseada naquele contexto, tá? Então, ADR, apesar de ele ser um documento técnico também, ele vai explicar, e muitas vezes em...

06:10

em relação ao negócio, o porquê que essa decisão foi tomada. Porquê que eu resolvi utilizar o RabbitMQ em relação a Kafka, já que o Kafka me atenderia um pouco melhor que o RabbitMQ?

06:23

E ali pode estar escrito, por conta de custos, infraestrutura e mão de obra que a gente tinha na empresa, que não conheciam Kafka. Então, deu pra entender o porquê dessa decisão, entendeu? Alternativas, a que ele traz, as consequências de a gente colocar isso e também referências, ou seja, são outros links

06:45

para outras ADRs ou para outros documentos de produto, high-level designs, RFCs, ou seja, tudo que tiver a ver com aquele assunto, eu posso fazer uma linkagem aqui. Beleza? Então, essa, vamos dizer assim, é o clássico do mundo da ADR.

07:03

Essas coisas foram evoluindo ao longo do tempo, hoje a gente tem diversos templates e modelos de ADR, eu vou mostrar e a gente vai trabalhar em cima de um deles, de forma geral, mas entenda que a ideia da ADR é registrar mudanças ao longo dos anos, e você consegue ter uma timeline bem clara em relação aí, tá?

07:26

Então, galera, vamos nessa, vamos seguir pra que a gente comece a andar a entender e depois eu vou mostrar bem na prática algumas coisas que eu trabalhei bastante nesses últimos tempos e eu acredito que você vai gostar bastante, tá? Vamos nessa!

## Resumo IA

**Abreviações**  
- **ADR** — *Architecture Decision Record*  
- **PRD** — *Product Requirement Document*  
- **HLD** — *High-Level Design*  
- **FDD** — *Functional Design Document*  
- **LLD** — *Low-Level Design*  
- **RFC** — *Request for Comments*  
- **Redis** — plataforma/motor de armazenamento em memória usado comumente como cache distribuído  
- **RabbitMQ** — broker de mensagens  
- **Kafka** — plataforma de streaming e mensageria distribuída  

**Resumo**  
A aula apresentou o **Architecture Decision Record (ADR)** como um documento curto e objetivo usado para registrar o motivo de uma decisão arquitetural relevante ter sido tomada em um projeto. O instrutor destacou que o ADR não substitui outros documentos, porque cada um cumpre um papel diferente: o **PRD** e o **HLD** explicam o que a solução é e como ela será estruturada em alto nível, enquanto o **LLD** detalha como a decisão será implementada no código. Já o ADR preserva a justificativa técnica e contextual da escolha, funcionando como um registro histórico da evolução da arquitetura ao longo do tempo.

Foi explicado que um ADR deve ser criado quando uma decisão foi debatida, envolveu **trade-offs** e teve impacto no design ou na arquitetura do sistema. O objetivo é evitar registrar escolhas triviais e concentrar esforço nas decisões cujo racional tende a se perder com o tempo. O instrutor reforçou que o documento é simples de produzir e manter, e que seu valor está justamente em registrar uma “timeline” arquitetural, permitindo entender como e por que o sistema chegou ao estado atual.

A aula também apresentou o template clássico associado a **Michael Nygard**, com estrutura baseada em campos simples: **número/identificador**, **título**, **contexto**, **decisão**, **alternativas**, **consequências** e **referências**. O número garante identidade estável e ordenação histórica; o título precisa ser específico para facilitar busca e citação; o contexto descreve problema, motivação, restrições e forças em jogo; a decisão registra o caminho adotado; as alternativas documentam as opções consideradas e descartadas; as consequências mostram impactos, ganhos e limitações aceitas; e as referências conectam o ADR a outros artefatos, como outros ADRs, PRDs, HLDs e RFCs.

Como exemplo prático, foi citado o cenário de escolha entre **RabbitMQ** e **Kafka**: mesmo que Kafka pudesse atender melhor tecnicamente em algum aspecto, a decisão por RabbitMQ poderia ser justificada por custo, infraestrutura disponível e conhecimento da equipe. O instrutor enfatizou que o ADR torna esse tipo de escolha transparente, permitindo que futuras revisões entendam o raciocínio por trás da decisão, em vez de julgá-la isoladamente sem o contexto original.

**Pontos de atenção**  
- Não usar ADR para decisões triviais; priorizar apenas escolhas que envolvam debate, trade-offs e impacto arquitetural relevante.  
- Não confundir o papel do ADR com o de PRD, HLD ou LLD: cada documento responde a uma pergunta diferente.  
- O campo de **contexto** é essencial; sem ele, a decisão fica solta e sem justificativa histórica.  
- A **decisão** deve ser direta e inequívoca, sem ambiguidades sobre o que foi adotado.  
- Registrar **alternativas** é obrigatório para deixar claro por que outras opções foram descartadas.  
- Descrever **consequências** é importante para evidenciar os custos, limitações e efeitos aceitos com a escolha.  
- Usar **título específico** e identificador numérico estável para facilitar busca, referência cruzada e evolução temporal.  
- Linkar **referências** a documentos relacionados para criar uma rede navegável de raciocínio técnico.  
- Lembrar que a arquitetura evolui ao longo do tempo; novos ADRs devem refletir mudanças e substituir decisões anteriores quando necessário.  
- Não tratar o ADR como defesa da tecnologia escolhida, mas como registro do porquê ela fazia sentido naquele cenário real.