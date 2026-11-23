Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17054)

## Resumo da aula

High Level Design organiza a solução no nível em que a arquitetura precisa fazer sentido como sistema, não como código. Ele responde perguntas sobre estrutura, componentes, módulos, comunicação, tecnologias adotadas e padrões principais, permitindo enxergar como a solução se sustenta antes de entrar em detalhes de implementação. A utilidade prática desse documento está em alinhar a visão técnica ampla entre pessoas que precisam decidir, revisar ou decompor o trabalho. A metáfora mais útil é tratá-lo como o terreno arquitetural onde as features precisam caber.

Um HLD bom não tenta dizer linha por linha como construir; ele esclarece como o sistema é organizado e como suas partes se conectam. Isso inclui identificar componentes relevantes, descrever os fluxos principais e explicitar como os módulos se comunicam entre si. Também entram aqui as tecnologias e os padrões adotados, porque essas escolhas moldam restrições e possibilidades para os documentos mais detalhados. O valor do HLD está menos em exaustão e mais em remover ambiguidade estrutural.

O diagrama C4 no nível de containers é uma forma adequada de representar o HLD porque mostra os principais serviços, APIs e relações entre blocos executáveis da solução. Esse nível não detalha classes nem contratos completos, mas já permite visualizar responsabilidades, fronteiras e fluxos de comunicação. Quando bem usado, ele transforma uma descrição abstrata em uma arquitetura legível, suficiente para discutir composição do sistema e dependências relevantes. É o ponto em que a solução deixa de ser apenas intenção e passa a ter forma arquitetural.

O HLD costuma começar pelo objetivo do documento ou da feature, mas esse objetivo já aparece antes no PRD e aqui ganha recorte técnico. A partir daí, entram arquitetura geral, principais componentes, responsabilidades, fluxo das requisições, modelo de dados em alto nível e interfaces públicas expostas pelos módulos. Essas seções existem para responder o que precisa ser construído do ponto de vista estrutural, sem cair em especificação detalhada de implementação. Os nomes das seções podem variar; o importante é cobrir as perguntas arquiteturais certas.

Interfaces públicas entram no HLD para deixar claro o que cada módulo ou serviço expõe para o restante do sistema, mesmo sem detalhar todos os contratos. Isso é importante porque a arquitetura depende das fronteiras entre partes do sistema, e essas fronteiras aparecem justamente nas interfaces. Em alto nível, basta identificar quais pontos de integração existem e qual papel cumprem. O detalhamento fino fica para documentos mais próximos da implementação.

Segurança, escalabilidade, disponibilidade e observabilidade aparecem no HLD porque afetam a arquitetura desde o início, e não apenas na fase de implementação. Se um sistema precisa crescer, resistir a falhas, proteger acesso ou ser monitorável, isso influencia componentes, fluxos e padrões de comunicação escolhidos. Essas preocupações não exigem ainda a definição completa de mecanismos e configurações, mas precisam estar registradas como direcionadores arquiteturais. Ignorá-las no alto nível costuma empurrar problemas estruturais para tarde demais.

Riscos já fazem parte da cadeia de documentação, mas no HLD eles aparecem conectados à forma da solução. O documento ajuda líderes e arquitetos a entender o que será desenvolvido com detalhe suficiente para orientar decisões posteriores, inclusive a decomposição em um Feature Design Doc quando necessário. Ele não entrega instruções executáveis para implementação direta, mas oferece base para que alguém refine a solução em um nível mais baixo. Esse limite é intencional: clareza arquitetural sem confundir visão geral com especificação detalhada.

Retomando a distinção de níveis de abstração já estabelecida, o HLD não substitui o documento de feature quando a solução exige detalhamento operacional. Dizer apenas que haverá autenticação pode ser suficiente em um cenário simples, especialmente quando o framework já resolve quase tudo; em um cenário mais complexo, o HLD deixa claro que existe uma preocupação arquitetural, mas o detalhamento precisa descer para outro artefato. A fronteira correta depende do contexto da mudança e da complexidade envolvida. O erro comum é tentar fazer o HLD virar especificação completa ou, no extremo oposto, deixá-lo genérico demais para orientar qualquer decisão.

Não existe conjunto obrigatório e universal de seções para todo HLD. O documento funciona melhor como guideline adaptável: muitos artefatos compartilham uma espinha dorsal parecida, mas cada contexto pode exigir seções extras, ênfases diferentes ou até nomenclaturas distintas. Essa flexibilidade é parte do próprio papel do HLD, porque a arquitetura precisa refletir o problema real, não obedecer rigidamente a um template. Um bom documento preserva a cobertura das decisões essenciais e ajusta a forma ao contexto do sistema.

## Transcrição

00:02

Bom pessoal, agora vamos falar aí sobre High Level Design, tá? Ou seja, ele é um tipo de documento e normalmente eu vou tentar sempre te ajudar a entender o contexto desses documentos baseados em que tipo de perguntas que esse documento tem que responder pra gente, tá?

00:19

Então, a ideia do High Level Design é fornecer um panorama macro, a arquitetura geral e as principais relações entre os componentes. Então, ele vai responder perguntas como, como que esse sistema é estruturado? Quais são os componentes, os módulos que existem? Como que esses caras se comunicam? Quais são as tecnologias e padrões que estão sendo adotados?

00:39

Então, o que a gente pode mostrar é, ah, vai ter um diagrama, um diagrama C4 no container, no segundo container do diagrama. Eu vou mostrar quais são os serviços que tem, as APIs, os fluxos principais, quais são os padrões de comunicação, considerações de segurança, escalabilidade, disponibilidade. Então, vamos imaginar assim que o high-level design, ele define qual é o terreno

01:04

onde as features que a gente vai desenvolver vai ser implementada. Ou seja, ele traz uma visão realmente geral para que a gente consiga entender como tudo aquilo vai conseguir se conectar. Então, normalmente, quais são essas seções encontradas no high level design? Normalmente, a gente traz qual é o objetivo daquele documento ou daquela feature naquele momento, ou seja, do design daquilo que você está desenvolvendo,

01:33

E, obviamente, se você começar a perceber, existe objetivo também no Product Requirement Document, certo? E, eventualmente, a gente vai ter, vamos dizer, um overlapping, ou seja, o objetivo pode ser compartilhado com o que veio do PRD.

01:50

Por outro lado, quando a gente está falando em objetivo aqui, agora a gente começa a ser mais técnico e não ficar tão falando tanto a nível de produto, mas em relação à parte técnica que vai ser implementada baseado naquele produto. Então, a gente vai trazer pontos de arquitetura geral, quais são os principais componentes e a responsabilidade desses componentes, como que vai funcionar o fluxo das principais requisições,

02:15

como que vai ser o modelo de dados em alto nível, de como que isso vai ser organizado, quais são as interfaces públicas. Eu não preciso dar detalhes, mas eu preciso entender quais são as principais interfaces que os módulos vão colocar.

02:27

Quais são considerações que eu vou precisar para fazer a escalabilidade desse sistema? Quais são considerações que eu posso falar em relação à segurança? Quais são as considerações que eu tenho em relação à observabilidade? Quais são os pontos referentes a riscos? Então, se você perceber, apesar de ele ser um high level,

02:47

design, ele traz realmente, de uma forma um pouco mais ampla, como que as coisas se conectam ali pra gente. Então, isso realmente ajuda a gente bastante

03:01

ter uma visão mais de alto nível, mas com certo nível de detalhe. Dependendo é quem que vai ler esse documento. Será que eu consigo implementar algo a partir desse documento? Bom, de forma geral, tá? A minha visão é que eu não consigo chegar e entender detalhes de implementação com esse documento, mas eu acredito que um líder

03:22

Um arquiteto que tem acesso a esse documento, ele consegue entender um pouco melhor sobre o que vai ser desenvolvido, ao ponto de ele conseguir definir melhor como que esse processo vai ser feito mais abaixo nível num documento de feature, por exemplo, que vai ser desenvolvido. E toda vez que eu falo feature, pode ser um recurso específico, pode ser um módulo ou até mesmo um produto um pouco maior,

03:46

que seja justificado documentos desse tipo, tá? É mais ou menos como o exemplo que eu dei. Ah, a gente vai fazer uma autenticação normal que vem no meu framework, eu vou falar que a gente vai ter autenticação. Agora, se isso for um pouco mais complexo, provavelmente eu vou precisar detalhar mais porque existem muitas informações que acabam trabalhando em relação a tudo isso, tá? Então, essas são as principais sessões que a gente acaba encontrando no high-level design. O grande ponto aqui é que

04:15

Essas sessões não são obrigatórias, os nomes delas não precisam necessariamente ser esses, e se você precisar adicionar outras sessões, você vai precisar ficar na liberdade. Isso aqui para você é um guideline, a maioria dos documentos de high level design você vai encontrar pontos

04:36

como esse que eu te trouxe, mas a partir dali você vai ter a liberdade pra você customizar e entender um pouco mais, tá? No nosso próximo vídeo, eu vou pegar aqui pra vocês um exemplo de high-level design que eu tenho, e a gente vai utilizar esse exemplo de forma geral pro resto desse nosso capítulo, desse nosso módulo, porque as coisas vão começar a se conectar entre um documento e outro, pra que a gente, inclusive, consiga comparar

05:03

um ao outro e quando eu realmente preciso ter todos ou quando eu preciso apenas ter um e que já é o suficiente para aquilo que eu preciso. Beleza? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **HLD** — *High Level Design*  
- **C4** — Modelo de documentação arquitetural em quatro níveis, usado aqui no nível de **containers**  
- **PRD** — *Product Requirement Document*  

**Resumo**  
A aula apresentou o High Level Design (HLD) como um documento de arquitetura em nível macro, cujo objetivo é organizar a solução como sistema, e não como código. O instrutor explicou que o HLD responde perguntas centrais sobre estrutura, componentes, módulos, comunicação entre partes, tecnologias e padrões adotados, funcionando como o “terreno” onde as features serão implementadas.  

Foi destacado que um bom HLD não deve detalhar linha por linha a implementação, mas sim esclarecer como o sistema está organizado, quais são as responsabilidades dos principais componentes, como ocorrem os fluxos de requisições e como os módulos se conectam. Para representar isso, o diagrama C4 no nível de containers foi apontado como uma forma adequada, pois permite visualizar serviços, APIs, fronteiras e dependências sem entrar no nível de classes ou contratos completos.  

O instrutor também explicou que o HLD costuma começar pelo objetivo do documento ou da feature, em recorte mais técnico do que o objetivo presente no PRD, podendo haver sobreposição entre os dois. Além disso, o documento pode incluir arquitetura geral, modelo de dados em alto nível, interfaces públicas expostas, considerações de segurança, escalabilidade, disponibilidade, observabilidade e riscos. A ideia é oferecer clareza arquitetural suficiente para orientar decisões e permitir que líderes e arquitetos decomponham o trabalho em documentos mais detalhados, como um Feature Design Doc, quando necessário.  

Por fim, foi reforçado que não existe um template universal obrigatório para HLD: as seções são um guideline adaptável ao contexto. O importante é cobrir as decisões arquiteturais essenciais sem transformar o documento em especificação completa nem deixá-lo genérico demais.  

**Pontos de atenção**  
- O HLD deve ficar no nível de arquitetura geral, sem cair em detalhes de implementação linha a linha.  
- Não confundir o objetivo do HLD com o objetivo do PRD: pode haver overlap, mas o foco aqui é técnico.  
- O documento precisa explicitar componentes, responsabilidades, fluxos e interfaces públicas para deixar claras as fronteiras do sistema.  
- Considerações de segurança, escalabilidade, disponibilidade, observabilidade e riscos devem aparecer cedo, porque impactam a arquitetura.  
- O diagrama C4 no nível de containers é útil para representar a solução, mas não substitui documentação mais detalhada quando necessário.  
- O HLD não costuma ser suficiente para implementar sozinho em cenários complexos; pode ser preciso descer para um Feature Design Doc.  
- Evitar dois extremos: HLD genérico demais, que não orienta decisões, ou detalhado demais, que vira especificação completa.  
- As seções do HLD não são fixas; o documento deve ser adaptado ao contexto, mantendo cobertura das decisões arquiteturais essenciais.