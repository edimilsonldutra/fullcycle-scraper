Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16963)

## Resumo da aula

A ausência de documentação já cria dependência de memória informal, mas a documentação desatualizada pode ser ainda mais perigosa porque transmite confiança falsa. Quando números, regras ou guidelines estão errados, o time toma decisões com base em um retrato incorreto do sistema. O problema deixa de ser apenas falta de contexto e passa a ser contexto enganoso. Nesse cenário, o documento não reduz risco: ele introduz risco operacional.

Um documento técnico influencia implementação, priorização e manutenção; por isso, erro documental não é neutro. Se o time acredita em métricas, fluxos ou restrições que já não correspondem ao software real, as decisões seguintes herdam esse erro. A analogia do velocímetro resume bem o efeito: agir com base em uma leitura incorreta produz uma resposta incorreta, mesmo quando a execução parece racional. Documentação confiável precisa ser tratada como fonte de decisão, não como arquivo histórico decorativo.

A pressão por deploy, sprint e entrega imediata empurra a documentação para depois, mesmo quando o time reconhece seu valor. Isso não contradiz a ideia já vista de que documentação não deve ser um fim em si mesma; o problema surge quando “depois” vira “nunca”. O resultado é um fluxo em que o software evolui, mas o contexto das decisões não acompanha essa evolução. A dívida não é apenas técnica: é também informacional.

A dificuldade de documentar não nasce só de escolha individual; ela também reflete cultura organizacional e pressão operacional. Times sob urgência constante tendem a tratar registro de contexto como atividade secundária, porque o benefício aparece no médio prazo, enquanto a cobrança da entrega é imediata. Isso enfraquece o valor percebido da documentação no dia a dia. Quando a organização mede apenas velocidade de entrega, o comportamento natural é sacrificar manutenção do conhecimento.

Em ambientes regulados, como bancos e setores com forte atuação de compliance, a documentação mínima deixa de ser opcional. Ela existe para garantir rastreabilidade, padronização e capacidade de auditoria, mesmo quando o time está sob pressão. Isso muda o custo de não documentar: além de desorganização técnica, surge risco regulatório. Nesses contextos, documentar faz parte da operação formal do produto.

Escrever documentação de qualidade costuma ser lento, cansativo e cognitivamente caro, especialmente quando o autor precisa estruturar contexto para onboarding, continuidade e alinhamento técnico. O esforço não termina na primeira versão: assim que o software muda, o documento começa a envelhecer. Retomando o cenário do projeto com documentação, o problema não é apenas escrever um bom texto, mas sustentar sua utilidade ao longo do tempo. Sem manutenção recorrente, o investimento inicial perde valor rapidamente.

Documentação que quase ninguém lê gera baixo retorno percebido, mesmo quando exigiu alto esforço para ser produzida. Em projetos corridos, a urgência por corrigir bugs, implementar features e fazer deploy empurra a leitura para o fim da fila. Isso cria um ciclo ruim: o time lê pouco porque a pressão é alta, e passa a valorizar menos a documentação porque quase não a usa. Quando isso acontece, o problema não é só produzir conteúdo, mas inseri-lo no fluxo real de trabalho.

Nem todo problema de documentação é falta de disciplina; muitas vezes o time simplesmente não sabe qual documento criar para cada necessidade. Retomando a escolha do documento adequado ao contexto, já estabelecida antes, o ponto novo aqui é a consequência prática do desconhecimento: usar um template genérico para tudo produz documentos confusos, longos e pouco úteis. Cada tipo documental atende uma função específica, e errar essa escolha compromete leitura, manutenção e decisão. Documentar bem depende tanto de escrever quanto de selecionar o artefato correto.

Quando a documentação é vista como tarefa paralela, ela compete com desenvolvimento e tende a ser adiada. O valor percebido aumenta quando o time entende que registrar decisões, restrições e contexto reduz retrabalho, acelera onboarding e melhora continuidade operacional. Isso exige integrar documentação ao fluxo real de desenvolvimento, e não tratá-la como atividade eventual. Sem essa integração, o documento envelhece, perde credibilidade e deixa de orientar o trabalho.

Esses problemas explicam por que a discussão não termina em “documentar mais” ou “documentar menos”. O desafio real é produzir documentação confiável, proporcional, lida e sustentável dentro da rotina de engenharia. Esse diagnóstico prepara a transição para o próximo contexto: usar inteligência artificial para reduzir atrito de produção, manutenção e consumo documental. A questão central passa a ser como tornar a documentação útil o suficiente para pessoas e também para sistemas apoiados por IA.

## Transcrição

00:01

E pessoal, seguinte, a gente falou rapidamente sobre a Jail, e agora eu quero que a gente volte, de forma geral, a pensar especificamente sobre documentação, tá? Porque a gente viu da onde nós estávamos, lá daquele modelo waterfall, até a gente chegar no momento que a gente está hoje, que a gente está começando a mudar muita coisa por conta da inteligência artificial,

00:27

Mas documentação é algo que existe até hoje. Empresas que trabalham de uma forma extremamente séria, elas têm documentação. Mas a gente tem alguns problemas extremamente conhecidos e comuns para que a gente trabalhe com documentação. E eu acredito que, se você está no mercado já há algum tempo, eu acho que esses pontos que eu estou trazendo aqui é quase que chover no molhado, mas vale a pena a gente lembrar.

00:54

Ou seja, muitas vezes a gente pega um documento, um projeto que a documentação praticamente não existe. E, honestamente, tem hora que eu não sei o que é pior, uma documentação que não existe ou uma documentação fortemente desatualizada. Porque quando você tem números errados, quando você tem guidelines errados, faz com que normalmente você comece a...

01:20

tomar decisões erradas, a mesma coisa como olhar o velocímetro de um carro e você achar que está andando a 100 por hora e na realidade você está a 140. Então, dados errados fazem com que a gente tome decisões erradas.

01:38

Outra coisa é que um outro problema grave que a gente tem é que a gente tem uma priorização na criação do software ao invés de documentar. Eu não estou dizendo que o mais importante é o software, a documentação não deve ser um fim em si mesma, mas como a gente sempre vive naquela pressão, vamos fazer deploy, tem que entregar aquela sprint e daqui a pouco a gente documenta assim que for para o ar, a gente acaba deixando muitas vezes de documentar, tá? Por quê? Porque

02:08

Além de ser cultural, existe muitas pressões que a empresa sofre, então vai depender muito de como que funciona a empresa, né? Normalmente, por exemplo, grandes bancos, áreas que têm muitos departamentos de compliance e coisas desse tipo, você forçadamente precisa ter o mínimo de documentação dentro de um determinado padrão e tudo mais, tá? Um outro ponto, um ponto aí interessante também é que

02:36

Se você já criou alguma documentação alguma vez, provavelmente você já deve saber que é um processo extremamente chato, é um processo extremamente lento. Eu não sei o que você acha disso, mas eu não gosto de abrir um arquivo novo e começar a escrever um documento. Às vezes, eu gastava três, quatro dias para criar um documento realmente decente para que o software ficasse

03:01

realmente bem documentado para novos funcionários, para facilitar o onboarding e coisas desse tipo, mas era chato, era amassante, e depois, três semanas, cinco semanas depois, a gente via essa documentação desatualizada, e aí você tem um filho que você criou, você criou essa documentação, você tem que manter esse cara atualizado sempre, tá?

03:23

Uma outra coisa também, e isso aí dá vontade de chorar, é que raramente a documentação é lida por todo o time, tá? Ou seja, a documentação acaba agregando pouco valor, tá? Eu não sei se na empresa que você trabalha você realmente já leu todas as documentações do projeto que você está trabalhando.

03:45

Eu conheço muita gente que não leu, eu já entrei em projetos que estavam extremamente corridos, tinha que fazer o deploy para ontem, já passaram uma feature, alguns bugs que eu tinha que corrigir, e a última coisa que eu fui fazer foi ler documentação, tá? E um ponto importante também é que muitos desenvolvedores, líderes de diversas áreas, tem área de produto também, eles não sabem criar um documento certo para cada caso de uso.

04:14

Então, isso aí também é algo que faz com que a gente tenha um problema muito grande de gerar documentação, porque a gente não sabe documentar, porque existem diversos tipos de documento. Cada tipo de documento tem uma função, cada tipo de documento tem um objetivo, e se você quiser criar um documento

04:37

um template, vamos dizer assim, que sirva para qualquer coisa, simplesmente você vai ficar muito perdido. E aprender a fazer uma documentação provavelmente não é algo que você quer comprar um curso só para aprender a documentar. Ou se na sua empresa você vai ter um treinamento apenas de como documentar. Algumas Big Decks tem, passam por muitos desses processos.

05:02

Mas, o grande ponto é que a gente conhece muito pouco sobre tipos de documento, o que documentar, o que não documentar, o que é importante e o que não é importante. Beleza? Então, esse aí é um ponto que é extremamente relevante. Próximo vídeo, a gente vai começar a contextualizar agora com o mundo da inteligência artificial. Vamos nessa!

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **Jail** — termo mencionado na aula, sem definição explícita no conteúdo

**Resumo**
A aula retoma o tema documentação de software e destaca que o problema não é apenas a ausência de documentação, mas também a documentação desatualizada, que pode ser ainda mais perigosa por transmitir uma falsa sensação de confiabilidade. O instrutor explica que quando números, regras, guidelines ou fluxos estão errados, o time toma decisões com base em um retrato incorreto do sistema, o que afeta implementação, priorização e manutenção. A analogia do velocímetro é usada para ilustrar como uma leitura errada leva a uma decisão errada, mesmo quando a ação parece lógica.

Também é abordado o motivo pelo qual a documentação costuma ser negligenciada: a pressão por deploy, sprint e entrega imediata faz com que o registro de contexto seja adiado, muitas vezes indefinidamente. O instrutor ressalta que isso não significa que documentação deva ser um fim em si mesma, mas sim que ela precisa acompanhar a evolução do software para não se tornar dívida informacional. Em ambientes regulados, como bancos e áreas com compliance, a documentação mínima é obrigatória para garantir rastreabilidade, padronização e auditoria.

Outro ponto central é que escrever documentação de qualidade é um processo lento, cansativo e cognitivamente caro, e que o esforço não termina na primeira versão, pois o documento envelhece à medida que o software muda. Além disso, a documentação muitas vezes não é lida pelo time, o que reduz seu retorno percebido e reforça o ciclo de desvalorização. O instrutor também destaca que muitos profissionais não sabem escolher o tipo correto de documento para cada necessidade, o que leva ao uso de templates genéricos e documentos pouco úteis. Ao final, a aula prepara a transição para o uso de inteligência artificial como forma de reduzir o atrito na produção, manutenção e consumo da documentação.

**Pontos de atenção**
- Documentação ausente e documentação desatualizada são problemas diferentes; a desatualizada pode ser mais perigosa por induzir decisões erradas.
- Dados, métricas, regras e guidelines incorretos contaminam decisões técnicas e operacionais.
- Não tratar documentação como atividade opcional em ambientes regulados, onde ela é parte da operação formal.
- Evitar cair na lógica de “documentar depois”, porque isso frequentemente vira “nunca”.
- A documentação precisa ser mantida continuamente; escrever uma boa primeira versão não basta.
- Documentação que não é lida perde valor e entra em um ciclo de baixa utilidade percebida.
- Não usar template genérico para tudo; cada tipo de documento tem função e objetivo específicos.
- Integrar documentação ao fluxo real de desenvolvimento, em vez de tratá-la como tarefa paralela.
- Considerar a pressão cultural e organizacional: times medidos apenas por velocidade tendem a sacrificar conhecimento registrado.
- Buscar documentação proporcional, confiável, sustentável e realmente útil para o time.