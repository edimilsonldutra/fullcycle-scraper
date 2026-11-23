Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16731)

## Resumo da aula

Gestão de prompts precisa existir desde o dia zero do sistema, não como correção posterior. Quando o time adia essa decisão, o prompt cresce sem convenção, sem histórico claro e sem responsabilidade definida, o que dificulta evolução, auditoria e colaboração. A escolha inicial não precisa ser sofisticada, mas precisa estabelecer como organizar, revisar e versionar os prompts ao longo do ciclo de vida da aplicação. Essa estratégia é o que transforma prompt em artefato governável, em vez de texto solto espalhado pelo projeto.

Prompts de produtividade e prompts de aplicação já foram diferenciados anteriormente, mas aqui o ponto central é a consequência prática dessa diferença: o modelo de gestão muda de forma drástica. Um prompt usado para trabalho individual ou colaboração interna pode tolerar mais flexibilidade, enquanto um prompt que compõe comportamento de software exige controle mais explícito de evolução, responsabilidade e impacto operacional. Misturar os dois contextos sob a mesma governança costuma gerar ruído, porque eles têm riscos e expectativas diferentes. A estratégia correta começa reconhecendo que nem todo prompt merece o mesmo processo.

A pessoa que cria e aperfeiçoa um prompt não precisa ser a mesma que implementa a aplicação. Em muitos times, produto, operação, especialistas de domínio ou pessoas dedicadas à curadoria do comportamento textual assumem essa responsabilidade, enquanto desenvolvimento integra, executa e protege o uso desse artefato no sistema. Essa separação importa porque evita concentrar em uma única função decisões de negócio, redação do prompt e implementação técnica. Quando o time reconhece papéis distintos, a gestão do prompt fica mais clara e menos dependente de conhecimento informal.

Organizar e versionar prompts resolve apenas uma parte do problema. Aspectos como caching, latência, velocidade e desenho arquitetural da aplicação pertencem a outra camada de decisão, mesmo quando afetam diretamente o uso do prompt. Delimitar esse escopo evita confundir governança do artefato com operação completa do sistema de IA. Essa separação também ajuda a escolher ferramentas sem esperar que um mecanismo de gestão de prompt resolva sozinho problemas de runtime e infraestrutura.

Retomando os exemplos já vistos com Git, arquivos locais e soluções externas como LangSmith, o princípio importante não está na tecnologia específica, mas na capacidade de manter organização, histórico e referência estável do prompt. Markdown, YAML, repositório local ou registry remoto são apenas formas de materializar a mesma disciplina de engenharia. Quando o conceito está claro, a troca de framework, linguagem ou plataforma não destrói o processo, porque a governança continua válida. Ferramentas mudam; a necessidade de controlar a evolução do prompt permanece.

Armazenar prompts no repositório do projeto ou usar uma plataforma externa são alternativas legítimas, desde que a estratégia de gestão esteja definida. A escolha depende do contexto do time, do fluxo de trabalho e do grau de desacoplamento desejado entre código e prompt. Se a equipe entende como versionar, organizar e promover revisões, consegue aplicar esses princípios tanto em arquivos locais quanto em hubs remotos. Sem essa base, trocar de ferramenta apenas desloca a desorganização para outro lugar.

## Transcrição

00:01

Bom, pessoal, para a gente concluir um pouco esse nosso aspecto em relação de versionamento de prompts e coisas desse tipo...

00:10

Eu acho que o mais importante, independente de ferramenta, solução que você vai utilizar, é que você entenda o conceito que está por trás. Porque eu acho que muitas pessoas acabam não tendo essa clareza. Prompts para produtividade, onde eu, desenvolvedor, vou trabalhar, vou me organizar e tudo mais. Prompts para aplicações. A forma de como você gerencia muda drasticamente. E o ponto que eu acho bem crítico é que

00:38

A responsabilidade de quem vai criar também pode ser de outra pessoa, de outra área da empresa ou de alguém que trabalhe do seu lado, mas que o foco dele está realmente no gerenciamento, no aperfeiçoamento do prompt. O que você, desenvolvedor, talvez, dependendo da empresa, do projeto, você não precise fazer, tá? Então, o que eu recomendo aí de forma geral é

01:07

no dia zero, crie pelo menos uma forma e uma estratégia de como que você vai organizar e fazer a gestão dos prompts dentro da aplicação com IA que você está querendo. Lembrando também, pessoal, que o nosso prisma que eu estou falando agora aqui, ele está muito mais no prisma de gestão do prompt, de organização, versionamento, mas perceba que eu não estou falando muito em relação à parte de arquitetura de aplicações.

01:37

caching, velocidade, latência, todos esses tipos de coisa. Por quê? Porque o prisma dessa nossa disciplina está, na realidade, no prompt em si, e não em toda uma arquitetura de um software onde o prompt também é utilizado. Então, ao longo de todo o nosso curso, a gente vai acabar caindo no mesmo assunto, mas com prismas, com olhares diferentes,

02:00

em relação a isso. Eu posso olhar em prompt em relação à arquitetura, eu posso olhar em prompts em relação à organização, a workflow de trabalho dentro das equipes. Mas, eu acredito que agora, você tendo um pouco mais de clareza desses papéis diferentes para fazer a gestão dos prompts, as possibilidades que você pode utilizar em gerenciar esses prompts, utilizando desde um Git, um controle de diversão, num repositório do seu

02:27

do seu projeto, até mesmo ferramentas externas. Então, uma vez que você entende isso, eu acho que as coisas começam a ficar mais claras. Independente se você vai trabalhar com Markdown, independente se você vai trabalhar com YAML, independente de qualquer coisa, porque uma vez que você entende o conceito, o resto acaba sendo detalhe de implementação e, obviamente, não é objetivo, inclusive, dessa disciplina ficar focando em detalhes.

02:53

Eu só queria trazer coisas prontas para demonstrar, por isso que nesse caso eu estou usando a LangChain, o LangSmith, mas poderia ser qualquer outro framework, com qualquer outra linguagem de programação. Maravilha?

03:06

Bom galera, então falamos aí então sobre gestão de prompts, tanto pra produtividade quanto pra parte de gerenciamento de prompts para softwares que você vai trabalhar aí, provavelmente no seu futuro, com inteligência artificial. Se é que você já não tá trabalhando, obviamente.

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **Git** — Sistema de controle de versões distribuído  
- **Markdown** — Linguagem de marcação leve para formatação de texto  
- **YAML** — YAML Ain’t Markup Language; formato de serialização de dados legível por humanos  
- **LangChain** — Framework para desenvolvimento de aplicações com modelos de linguagem  
- **LangSmith** — Plataforma para observabilidade, teste e gestão de aplicações com LangChain e prompts  

**Resumo**  
A aula enfatiza que a gestão de prompts precisa ser definida desde o dia zero do sistema, e não tratada como uma correção posterior. O instrutor destaca que, sem uma estratégia inicial, os prompts tendem a crescer de forma desorganizada, sem convenção, histórico ou responsabilidade clara, o que prejudica a evolução, a auditoria e a colaboração no time. O foco não é a ferramenta em si, mas o conceito de governança do prompt como artefato versionável e controlável ao longo do ciclo de vida da aplicação.

Também é reforçada a diferença entre prompts de produtividade e prompts de aplicação. No primeiro caso, o uso é mais individual ou voltado à organização do trabalho; no segundo, o prompt passa a fazer parte do comportamento de um software e, por isso, exige maior controle de mudança, responsabilidade e impacto operacional. O instrutor aponta que não faz sentido tratar ambos com a mesma governança, pois os riscos e expectativas são distintos.

Outro ponto central é a separação de papéis. A pessoa que cria e aperfeiçoa o prompt não precisa ser a mesma que implementa a aplicação. Em muitos contextos, esse trabalho pode ficar com produto, operação, especialistas de domínio ou pessoas responsáveis pela curadoria do comportamento textual, enquanto desenvolvimento cuida da integração e proteção do uso desse artefato no sistema. Essa divisão reduz dependência de conhecimento informal e deixa a gestão mais clara.

A aula também delimita o escopo da disciplina: aqui o tema é gestão e versionamento de prompts, não arquitetura de aplicações, caching, latência ou desempenho de runtime. Esses assuntos pertencem a outra camada de decisão, embora se relacionem com o uso do prompt. Por fim, o instrutor mostra que tanto armazenar prompts no repositório do projeto quanto usar plataformas externas são caminhos válidos, desde que exista disciplina de organização, revisão e promoção de versões. O importante é que ferramentas como Git, Markdown, YAML, LangChain e LangSmith são apenas meios de materializar uma estratégia de gestão; o valor real está na clareza do processo.

**Pontos de atenção**  
- Definir a estratégia de gestão de prompts desde o início do projeto, evitando tratar isso como algo posterior.  
- Não misturar na mesma governança prompts de produtividade e prompts de aplicação, pois eles têm riscos e exigências diferentes.  
- Reconhecer que a responsabilidade pelo prompt pode ser de outra área ou função, e não necessariamente do desenvolvedor.  
- Separar claramente gestão de prompt de arquitetura da aplicação, como caching, latência e velocidade.  
- Entender que ferramenta não substitui processo: Git, repositório local, Markdown, YAML ou plataformas externas só funcionam bem com uma estratégia definida.  
- Manter organização, histórico e referência estável do prompt para evitar perda de rastreabilidade e descontrole de mudanças.  
- Evitar assumir que uma plataforma externa resolverá sozinha problemas de governança, colaboração ou versionamento.  
- Tratar a gestão de prompts como disciplina contínua de engenharia, e não como detalhe secundário da implementação.