Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16966)

## Resumo da aula

PRD é um documento de produto usado para explicitar o que está sendo construído, por que isso existe e qual valor entrega. Embora não seja um design doc, ele entra antes dos documentos técnicos porque a IA precisa desse contexto para interpretar corretamente o projeto. Sem essa camada, o modelo tende a inferir objetivos apenas a partir de código ou pedidos isolados, o que aumenta ambiguidade. O papel do PRD, aqui, é servir como base de contextualização para pessoas e para IA.

A distinção entre documentação de produto e design docs já foi estabelecida; o ponto novo é que essa separação melhora a qualidade do contexto fornecido à IA. O PRD não descreve como implementar a solução em termos de arquitetura, componentes ou infraestrutura, mas pode incluir questões técnicas relevantes para alinhar produto e engenharia. Isso evita misturar intenção com implementação e preserva a função de cada artefato. Quando o time parte de um PRD claro, os design docs passam a responder ao problema certo.

PRD deve existir quando há entrega de valor percebido para o usuário ou para o negócio. Esse critério impede transformar qualquer requisito funcional em documento formal e concentra esforço documental no que realmente altera objetivos, métricas, escopo ou impacto do produto. Se uma iniciativa gera dúvidas relevantes, tem alto valor percebido ou exige alinhamento entre áreas, ela já se aproxima do limiar em que um PRD faz sentido. O documento passa a tratar aquele item como uma unidade de produto, não apenas como uma tarefa de implementação.

Nem toda feature merece PRD, especialmente quando ela é apenas mais um requisito funcional dentro de algo maior. A exceção aparece quando a feature é tão expressiva que funciona como um subproduto: ela tem objetivo próprio, métricas próprias, escopo próprio e impacto suficientemente alto para justificar contextualização separada. Nessa situação, tratá-la apenas como uma linha em um documento geral reduz clareza e dificulta o alinhamento. O PRD isola essa feature para que seu valor e seus limites fiquem explícitos.

Um PRD útil precisa organizar o item documentado como algo mensurável e delimitado. Isso significa explicitar objetivos, escopo e formas de medir resultado, para que o time não trate uma iniciativa relevante como uma descrição vaga de intenção. A clareza desses elementos ajuda tanto a coordenação entre produto e engenharia quanto a interpretação da IA, que passa a operar com menos suposições implícitas. Quando o documento não delimita bem o que está dentro e fora, o contexto perde valor operacional.

PRDs existem em níveis diferentes de granularidade. Um PRD de produto cobre o produto como um todo e, por isso, tende a ser mais amplo e menos detalhado; já um PRD de módulo aprofunda uma parte relevante da aplicação; um PRD de feature foca uma entrega específica com contexto próprio. A escolha do nível depende do tamanho da iniciativa e da autonomia conceitual daquele recorte. Pensar em granularidade evita tanto documentos genéricos demais quanto fragmentação excessiva.

Um mesmo software pode ter um PRD macro do produto e, adicionalmente, PRDs específicos para módulos ou features críticas. O termo EPIC pode aparecer como aproximação do nível de módulo no vocabulário de produto, mesmo que a equivalência não seja exata em todos os contextos. O importante é reconhecer quando uma parte do sistema concentra valor, complexidade de alinhamento ou identidade suficiente para merecer documentação própria. Isso transforma o PRD em ferramenta de organização do contexto, não em burocracia fixa.

PRD não é um artefato exclusivo de product managers. Desenvolvedores também podem participar da criação desse documento quando precisam aumentar clareza sobre a feature que será construída, especialmente em iniciativas com alto impacto ou escopo sensível. Esse uso é particularmente valioso em ambientes com IA, porque o documento deixa explícito o contexto que o time já conhece informalmente. O que parece redundante para pessoas experientes no domínio ainda é informação ausente para a IA.

Retomando a ideia de documentação como contexto operacional, o PRD resolve um problema simples: o time conhece o produto, mas a IA não. Por isso, registrar o que parece óbvio internamente não é desperdício; é a forma de transferir intenção, valor e limites para um agente que entra sem histórico do projeto. Antes de pedir como construir algo, é preciso explicitar o que esse algo é e por que existe. Essa ordem melhora a qualidade das respostas técnicas geradas depois.

## Transcrição

00:01

Bom, pessoal, agora que você entendeu os tipos de documentação, você já deve estar estranhando o que está aí na minha tela. E por que eu estou dizendo isso? Porque existe uma sigla ou um tipo de documento que é chamado de PRD, ou Product Requirement Document. Ou seja, é um documento focado em produto.

00:27

E aí você já deve estar pensando, Wesley, por que você está trazendo, então, essa documentação de produto para a disciplina de Design Docs, sendo que o nosso objetivo é aprender a parte de Design Docs? Faz muito sentido você fazer essa pergunta aí. E a minha resposta é o seguinte, pessoal. Apesar de nós, como pessoas técnicas, nós temos que

00:56

Como que eu posso dizer? A gente tem que dominar a parte design docs. Porém, quando a gente está falando em inteligência artificial, a parte de documentação de um produto é extremamente importante para que a IA entenda o que é o projeto.

01:18

e o porquê esse projeto existe. Se a inteligência artificial entende isso, tudo vai ficar um pouco mais simples de você conseguir acabar entendendo. Então, qual é o meu objetivo agora aqui para que você entenda um pouco melhor sobre PRDs, documentos de produto?

01:42

Por que ele é importante? Porque, eventualmente, você vai criar um documento desse, e esse documento não vai ser um design docs, mas ele é um documento de contextualização. Ele vai ser um documento que vai te ajudar a dar base para a IA trabalhar. Em tese, a sua empresa ou o projeto que você trabalha, em tese, você já deveria ter um documento desse.

02:06

mas eu acredito que nem todas as empresas têm, ou muitas empresas acabam utilizando esses documentos em contextos um pouco diferentes. Então, deixa eu falar rapidamente para você sobre PRDs, para que isso possa...

02:25

fazer sentido com essa nossa disciplina aqui. Então, vamos lá. O PRD é um documento de produto que visa alinhar as nossas equipes de produto e também a equipe técnica. Então, apesar de ser um documento de produto, há questões técnicas que podem e que devem estar dentro de um PRD. Então, esse PRD existe quando há uma entrega de valor percebido para o usuário ou para o negócio. E o porquê que eu estou dizendo isso

02:55

quando há uma entrega de valor percebido. Porque o que acontece é o seguinte, um PRD pode ser um projeto gigante inteiro como ele pode ser uma feature pequena.

03:08

Agora, não significa que toda feature merece um PRD. Mas também, muitas vezes, uma feature é tão expressiva que ela precisa de um documento desse tipo. A gente vai falar com isso daqui a pouco. Mas, de forma geral, se algo está entregando um valor extremamente alto para o cliente, para o negócio, tem dúvidas, você precisa de um PRD. Então, ele deve ser tratado como um produto

03:37

ou uma feature independente com objetivos, métricas e escopo próprio. O que eu estou dizendo isso? Quando eu vou gerar um PRD, eu tenho que pensar que aquele documento vai trazer para mim informações de um produto.

03:53

E se ele é um produto em si mesmo, ou se ele é um software em si mesmo, ou se ele é uma feature realmente importante ali daquele software, que ele é tão relevante, ou seja, esse produto tem que ter formas importantes de você conseguir medir, de você conseguir contextualizar, para que ele não seja simplesmente mais uma linha num PRDzão geral, vamos dizer assim.

04:20

Agora, um ponto importante que eu quero que você entenda é que nem toda feature merece um PRD, principalmente quando ela é apenas um dos requisitos funcionais do sistema. E a gente vai falar disso, inclusive, daqui a pouco. Agora, dependendo de uma determinada feature,

04:40

ela é tão relevante que ela pode ser considerada como se fosse um subproduto dentro do produto do software. E aí, nesse caso, ela não é mais só um requisito funcional.

04:53

acaba sendo algo muito maior, tá? E aí, quando a gente tem esse tipo de situação, aí, nesse caso, a gente vai querer um PRD pra ele, tá? Então, isso é um ponto importante. Agora, uma coisa interessante que você tem que se ligar é o seguinte, quando a gente tá falando em PRDs, existem, vamos dizer assim, níveis de PRDs, tá? E o que que são níveis, tá?

05:21

Esses níveis são basicamente a granularidade de informação que você vai trazer. Se é algo mais de alto nível ou se é algo que acaba sendo mais de baixo nível. Por exemplo, um PRD de produto vai ver o produto como um todo. E, provavelmente, esse produto como um todo não vai ter detalhes tão granulares.

05:43

Ok? Agora, se eu tenho um módulo dentro da minha aplicação, ou um EPIC... EPIC, normalmente, a galera de produto usa muito, mas vamos fazer uma correlação grosseira aqui entre que módulo e EPIC é a mesma coisa. Normalmente, módulo, a galera técnica fala mais, e EPIC, a galera de produto fala mais. Ok?

06:01

O ponto importante é que, se eu vou desenvolver um módulo, um sistema, uma parte que engloba um monte de coisa embaixo dele, talvez eu precise de um PRD específico para esse módulo. Ou, às vezes, dentro de um módulo, eu posso ter features, mas existem features tão relevantes que eu posso também ter um PRD. Então, não pense que um PRD é apenas um documento do produto em si, um documento geralzão. Não!

06:30

você como desenvolvedor, eventualmente, você pode ajudar a criar um PRD para fazer com que você tenha mais clareza, inclusive, da feature que você vai desenvolver. Por isso que eu fiz questão de trazer o PRD aqui, mesmo sabendo que ele não é necessariamente um design doc, ok? Mas ele é um documento extremamente relevante porque ele contextualiza. E essa contextualização hoje

06:57

ela é importante para a inteligência artificial. Às vezes, você está dentro de um time, o time que você está lá, todo mundo entende o produto, sabe o que faz, etc. E, se você for documentar isso, vai aparecer, no final das contas, que você está chovendo no molhado, porque todo mundo já sabe. Mas, a gente tem que lembrar que a IA não sabe. Então, os PRDs hoje são muito importantes por conta disso aí. Beleza? Próximo vídeo, a gente vai falar um pouco das sessões dos PRDs e coisas desse tipo. Vamos nessa!

## Resumo IA

**Abreviações**  
- **PRD** — *Product Requirement Document*  
- **EPIC** — *Épico* (termo de produto para agrupar trabalho/funcionalidades em um nível maior de escopo)

**Resumo**  
A aula apresentou o PRD (*Product Requirement Document*) como um documento de produto usado para explicitar o que está sendo construído, por que existe e qual valor entrega. O instrutor destacou que, embora o PRD não seja um design doc, ele deve aparecer antes da documentação técnica porque serve como camada de contextualização para orientar tanto pessoas quanto a inteligência artificial. Sem esse contexto, a IA tende a inferir objetivos apenas a partir de código ou pedidos isolados, o que aumenta a ambiguidade e prejudica a interpretação correta do projeto.

Foi explicado que o PRD é um artefato de alinhamento entre produto e equipe técnica, podendo conter questões técnicas relevantes sem misturar intenção de negócio com implementação. O documento deve existir quando há entrega de valor percebido para o usuário ou para o negócio, especialmente em iniciativas que alteram objetivos, métricas, escopo ou impacto. Nem toda feature precisa de PRD, mas features muito relevantes podem ser tratadas como subprodutos, com objetivos, métricas e escopo próprios, justificando documentação dedicada.

A aula também abordou níveis de granularidade do PRD: um PRD de produto cobre a visão geral, enquanto PRDs de módulo ou de feature aprofundam recortes específicos e mais autônomos do sistema. O instrutor mencionou que o termo EPIC pode ser usado como aproximação para esse nível intermediário de documentação, embora a equivalência não seja absoluta. Por fim, reforçou que desenvolvedores também podem participar da criação de PRDs para ganhar clareza sobre o que será desenvolvido, especialmente em contextos com IA, onde documentar o que parece óbvio para o time é necessário para transferir intenção, valor e limites ao agente.

**Pontos de atenção**  
- PRD não substitui design doc: ele vem antes e serve para contextualizar o problema e o valor da entrega.  
- Evitar misturar objetivo de produto com detalhes de implementação; o PRD não deve descrever arquitetura, componentes ou infraestrutura em profundidade.  
- Nem toda feature merece um PRD: só faz sentido quando há valor percebido relevante, impacto maior, dúvidas importantes ou necessidade forte de alinhamento.  
- Features muito expressivas podem exigir PRD próprio, funcionando como um subproduto com escopo, métricas e objetivos independentes.  
- Um PRD precisa deixar explícitos objetivos, escopo e formas de medir resultado; sem isso, vira uma descrição vaga e pouco operacional.  
- Definir bem o que está dentro e fora do escopo é essencial para evitar ambiguidade e retrabalho.  
- Escolher o nível certo de granularidade é importante: documentos genéricos demais perdem utilidade, e fragmentação excessiva também atrapalha.  
- PRD pode existir em nível de produto, módulo ou feature; a decisão depende do tamanho da iniciativa e da autonomia do recorte.  
- Desenvolvedores podem e devem colaborar na construção do PRD quando isso aumentar a clareza do trabalho a ser entregue.  
- Em contextos com IA, documentar o que parece óbvio internamente é boa prática, porque a IA não possui conhecimento prévio do produto.