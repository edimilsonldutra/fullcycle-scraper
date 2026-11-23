Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16968)

## Resumo da aula

Um PRD de alto nível é o recorte mais amplo da documentação de produto. Ele não entra no detalhamento operacional de uma feature; sua função é enquadrar a iniciativa como produto, deixando explícito o contexto macro que orienta decisões posteriores. Esse documento ganha valor sobretudo em projetos grandes, nos quais várias decisões dependem de uma visão comum antes da decomposição em módulos, EPICs ou features. Sem esse enquadramento, o time pode até executar entregas, mas continua sem clareza sobre o que está construindo como produto.

O nível alto do PRD pode ser entendido como um conjunto de perguntas que o produto precisa responder. Entre elas estão: por que o produto existe, o que se quer alcançar, o que será entregue e o que ficará fora, para quem se constrói, qual problema é resolvido, como os objetivos serão perseguidos, quais capacidades gerais o produto deve ter, como o sucesso será reconhecido, o que pode dar errado, qual roadmap orienta a evolução, quem participa e como tudo isso se conecta à estratégia da empresa. Essas perguntas não são um questionário solto; elas funcionam como uma estrutura de raciocínio para consolidar visão, direção e critérios de decisão.

Muitas perguntas desse tipo são estratégicas porque antecedem a implementação e, em vários casos, nem nascem no time de desenvolvimento. Parte delas pode vir de decisões top-down, definidas por liderança, diretoria ou pela estratégia mais ampla da empresa. Isso não torna o documento menos útil para desenvolvedores; ao contrário, torna explícitas premissas que normalmente chegariam apenas de forma implícita. Quando esse contexto não é registrado, a execução técnica passa a depender de interpretação parcial.

No PRD macro, o produto não aparece como um item isolado, mas como uma resposta a uma direção maior da empresa. A pergunta relevante não é apenas “o que vamos construir”, mas “por que isso merece existir dentro desta organização agora”. Essa conexão ajuda a justificar prioridade, investimento e trade-offs, além de dar sentido a objetivos, riscos e métricas já conhecidos. Um produto sem esse vínculo pode parecer coerente localmente e ainda assim estar desalinhado com a estratégia global.

Roadmap e definição de papéis entram no PRD de alto nível porque o documento precisa mostrar como a iniciativa se organiza no tempo e quem participa dela. O roadmap, nesse contexto, não é cronograma detalhado de execução, mas uma visão de evolução do projeto em etapas ou direções. Já os papéis tornam explícito quem influencia, decide, valida ou executa partes da iniciativa, o que reduz ambiguidade organizacional. Esse enquadramento é macro porque prepara coordenação e alinhamento, não especificação técnica.

Se as perguntas centrais do PRD de alto nível não podem ser respondidas, o problema não é apenas documental; é falta de clareza sobre o próprio projeto. Retomando o uso de PRD para IA, esse ponto é ainda mais importante porque o modelo depende desse contexto para interpretar corretamente a iniciativa antes de qualquer design doc. Um documento macro bem formulado reduz inferência implícita e melhora a qualidade das decisões derivadas. O próximo passo natural é descer desse enquadramento estratégico para o nível em que uma feature específica passa a exigir seu próprio contexto.

## Transcrição

00:01

Bom, pessoal, seguinte, como a gente está falando de PRD, eu tenho que deixar muito claro para você, de uma forma bem honesta, que a gente sempre pode ter, e eu não estou dizendo que o seu projeto precisa disso, mas entenda que existe um PRD de mais alto nível. Ou seja, ele dá uma contextualização macro de um projeto.

00:25

Então, no final das contas, o PRD, para um projeto grande, ele é um artefato extremamente importante, pois ele vai responder algumas perguntas, tá? E normalmente, com essas perguntas, você vai perceber que essas respostas dessas perguntas tendem a cair muito bem naquela sessão

00:45

naquelas sessões de um PRD que eu acabei de passar. Então, vamos lá. Por que esse produto existe? O que a gente quer alcançar com esse produto? O que esse projeto vai entregar e o que ele não vai entregar? Para quem a gente está construindo isso? Qual o problema que esse produto resolve e por que ele é importante?

01:06

Como a gente pretende alcançar esses objetivos? O que o produto deve ser capaz de fazer em linhas gerais? Como a gente sabe se o produto deu certo? O que pode dar errado e como a gente vai lidar com isso? Qual é o roadmap que a gente vai ter desse projeto? Quem está envolvido e qual é o papel de cada um? E como esse produto se conecta à estratégia da empresa?

01:31

Então, se você perceber, pessoal, quando a gente está pensando em produto, naquilo que você vai desenvolver, se você pensar muito bem, todas essas perguntas fazem muito sentido, tá? E perceba que muitas dessas perguntas acabam sendo extremamente estratégicas, inclusive, e que muitas vezes não tem nem um pouco a ver ou que você nem tem a opção de discutir isso, porque, normalmente,

01:58

muitas vezes são decisões top-down, ou seja, bem uma decisão lá de diretoria, e às vezes você é um desenvolvedor que simplesmente caiu no seu colo um determinado produto para você desenvolver. Mas, se você olhar e realmente prestar bem atenção nessas perguntas, você realmente vai ver que elas fazem sentido, e se você não conseguir responder, é porque realmente você não tem uma clareza do que o seu projeto deve fazer.

02:28

Então, essa é a ideia de um PRD de alto nível. E dá canseira, às vezes, só de olhar para isso e falar, nossa, será que eu vou ter que desenvolver isso? E aí eu vou falar, calma, meu querido amigo e amiga, porque tem uma outra coisa aqui que eu preciso te mostrar e que vai fazer mais sentido ainda para você.

## Resumo IA

**Abreviações**  
- **PRD** — *Product Requirements Document* (Documento de Requisitos do Produto)  
- **EPICs** — *Epics* (macrofuncionalidades ou grandes blocos de trabalho)

**Resumo**  
A aula apresentou o conceito de um PRD de alto nível como o recorte mais amplo da documentação de produto, usado para contextualizar uma iniciativa em nível macro antes de qualquer detalhamento de implementação. O instrutor destacou que esse tipo de documento é especialmente importante em projetos grandes, pois ajuda a alinhar visão, direção e critérios de decisão antes da decomposição em módulos, EPICs ou features. Em vez de descrever funcionalidades operacionais, o PRD de alto nível organiza o raciocínio do produto por meio de perguntas estratégicas: por que o produto existe, o que pretende alcançar, o que entrega e o que não entrega, para quem é construído, qual problema resolve, como os objetivos serão perseguidos, quais capacidades gerais precisa ter, como medir sucesso, quais riscos existem, qual é o roadmap, quem participa e como a iniciativa se conecta à estratégia da empresa.  
O fluxo explicado pelo instrutor mostra que essas respostas não são apenas documentação, mas uma base para orientar decisões e reduzir interpretações implícitas, especialmente quando parte das definições vem de cima para baixo, como da diretoria ou liderança. Ele reforça que, em muitos casos, o desenvolvedor recebe o produto já como uma decisão estratégica e precisa compreender o contexto para executar corretamente. Também foi enfatizado que o roadmap e os papéis dos envolvidos devem aparecer nesse nível macro porque servem para organizar a evolução da iniciativa e explicitar responsabilidades, sem entrar ainda em detalhes técnicos. Por fim, o instrutor aponta que, se as perguntas centrais do PRD de alto nível não puderem ser respondidas, isso indica falta de clareza do próprio projeto e não apenas uma lacuna documental.

**Pontos de atenção**  
- O PRD de alto nível não deve entrar em detalhamento operacional de uma feature.  
- Ele é mais útil em projetos grandes, onde o alinhamento macro é necessário antes da decomposição.  
- As perguntas estratégicas do documento precisam estar conectadas à estratégia da empresa, não apenas ao que será construído.  
- Muitas definições podem vir de decisões top-down; é importante registrá-las para evitar premissas implícitas.  
- Se não for possível responder às perguntas centrais, o problema é de clareza do projeto, não apenas de escrita do documento.  
- O roadmap nesse nível é uma visão de evolução, não um cronograma detalhado de execução.  
- Os papéis dos envolvidos devem ser explicitados para reduzir ambiguidade organizacional.  
- Um produto pode parecer coerente localmente e ainda assim estar desalinhado com a estratégia global.  
- O PRD de alto nível serve como base para etapas posteriores; primeiro vem o enquadramento estratégico, depois o detalhamento de features e design docs.