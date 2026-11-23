Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17125)

## Resumo da aula

ADR registra decisão arquitetural, não o histórico de execução do trabalho diário. Commits, pull requests, issues, code review e changelog já cobrem alterações operacionais, correções incrementais e justificativas locais. Quando um documento nasce para explicar uma mudança de feature, e não uma escolha estrutural, ele tende a duplicar informação que já existe em outros artefatos. O resultado é ruído documental: mais texto para manter, sem ganho real de memória arquitetural.

Refatoração interna de baixo impacto raramente merece ADR porque seu efeito costuma ficar restrito ao código local e pode ser explicado no próprio PR ou em documentação de engenharia. O mesmo vale para linters, formatter e convenções triviais de implementação, que funcionam melhor como guideline em README, CONTRIBUTING.md ou padrões internos do time. Retomando o critério de impacto estrutural já visto, a pergunta útil aqui é se a mudança altera a forma como o sistema evolui ou apenas como o time escreve código no dia a dia. Se a resposta for a segunda, ADR tende a ser excesso.

Decisões temporárias são um anti-caso clássico porque ADR existe para preservar escolhas duradouras. Se a equipe diz “vamos usar Redis só para testar”, está diante de uma prova de conceito, experimento ou validação técnica, não de uma decisão estabilizada. Registrar isso como ADR congela prematuramente algo que talvez nem sobreviva às próximas semanas. O documento correto, nesse caso, costuma ser uma issue, um RFC leve, uma nota de experimento ou o próprio registro do spike técnico.

Uma decisão que muda toda hora dificilmente deve virar ADR, porque ainda não atingiu maturidade suficiente para compor a memória arquitetural do sistema. Estabilidade não significa imutabilidade, mas sim expectativa razoável de permanência por meses ou anos. Essa duração importa porque o valor do ADR aparece quando alguém precisa entender no futuro por que uma direção foi adotada e mantida. Se a escolha ainda está oscilando a cada iteração, o documento formal tende a envelhecer antes de gerar valor.

Bug, hotfix e ajuste operacional pertencem ao fluxo de manutenção, não ao acervo de ADRs. O registro principal desses eventos deve ficar em changelog, issue, postmortem ou documento de incidente, porque o fato relevante ali é o problema ocorrido e sua correção imediata. A exceção aparece quando o incidente revela a necessidade de uma mudança arquitetural estável; nesse ponto, o incidente continua documentado no seu artefato próprio, e o ADR passa a registrar a nova decisão tomada para evitar recorrência. O ADR não substitui o incidente; ele documenta a resposta estrutural ao incidente.

A regra dos 3 Es ajuda a podar casos duvidosos sem transformar ADR em burocracia. A decisão deve ser estrutural, isto é, afetar construção ou integração do sistema; evidente, no sentido de que outras pessoas precisarão entender seu racional no futuro; e estável, com expectativa de durar meses ou anos. Quando um dos três elementos falta, o valor do ADR cai bastante. Essa regra não é uma lei absoluta, mas funciona como filtro prático para separar memória arquitetural de documentação transitória.

“Documentacite” descreve o impulso de documentar tudo só porque a documentação parece sempre benéfica. Esse excesso produz o efeito oposto: o acervo cresce, a manutenção piora e fica mais difícil distinguir o que realmente orienta a arquitetura. Um repositório inflado com ADRs triviais reduz a confiança no conjunto, porque o leitor passa a encontrar documentos importantes misturados com registros irrelevantes. Boa governança documental exige poda, não apenas produção.

Em ambientes com IA, documentação em excesso não é neutra: ela compete por atenção com os documentos realmente importantes. Se o repositório contém ADRs sobre detalhes operacionais, temporários ou triviais, modelos podem inferir relevância arquitetural onde ela não existe. Isso aumenta ambiguidade, piora recuperação de contexto e pode induzir respostas ou implementações baseadas em sinais fracos. ADR bom melhora a IA porque organiza a memória do sistema; ADR irrelevante piora a qualidade dessa memória.

Retomando o mesmo cenário do capítulo, nem toda mudança aparentemente relevante deve subir ao nível de ADR. Se a equipe ajusta um formatter, muda um valor operacional, faz um hotfix ou testa provisoriamente uma tecnologia antes de decidir, isso ainda não representa uma escolha arquitetural estável. O ADR só entra quando a mudança deixa de ser experimento ou operação e passa a orientar a estrutura do sistema por tempo suficiente para exigir memória explícita. O objetivo não é documentar mais, e sim documentar melhor.

## Transcrição

00:01

Bom, pessoal, e agora chegou uma parte importante, que é quando pode não fazer tanto sentido para a criação de um ADR? E por que eu falei quando não pode fazer tanto sentido? É porque eu não quero ser muito assertivo aqui, dizendo quando você deve ou não fazer algo.

00:23

porque tudo pode ser muito subjetivo no mundo de desenvolvimento, então eu acho que seria até ligeiramente uma falta de responsabilidade falar que você nunca vai fazer isso, que é como se eu fosse impor uma regra na sua vida, entendeu? Essa não é a minha intenção, mas são pontos que normalmente eu não recomendaria você utilizar. Quando o ADR, ADR é apenas um ruído. Você tem que entender que ADR não é um log de decisão operacional.

00:53

Não é porque você fez uma alteração até que grande ali naquela feature, que você fez 10 commits e etc, que você necessita de uma DR.

01:03

Você... Cara, você tem pull request, você tem issues que você pode criar, você pode ter code review, você pode ter outros documentos que tenham ali um changelog ou qualquer coisa desse tipo, mas não necessariamente isso acaba virando... Não deve virar uma DR, tá? Então, situação. Refatoração interna de baixo impacto. Pode ser justificado em outros documentos. Decisões temporárias. Vamos usar o REDI só para testar. Ou seja, eu estou criando uma prova de conceito

01:34

para ver se faz sentido eu utilizar aquela ferramenta. E, às vezes, eu nem vou utilizar aquela ferramenta. Cara, ADR serve para decisões douradoras, ou seja, decisões que vão acompanhar o projeto ao longo do tempo. Não é para um simples teste. Não é algo ali que você vai fazer porque você acha que está legal, mas você pode tirar em seguida. Perceba que código que você muda toda hora raramente vai tender a virar uma ADR.

02:04

quanto mais você mexe no código, mais você vai perceber que essas mudanças, e quanto é muita mudança, não necessariamente isso vai virar uma DR, porque é algo... provavelmente não é algo tão fundacional, vamos dizer assim, não está muito na foundation do software. Outras coisas, configurações triviais, linters, formatter e um monte de coisa. Cara, use documentações de engenharia.

02:30

Guidelines, como o seu software deve ser feito, como ele não deve ser feito, a gente vai falar sobre isso, tá? Inclusive com o IA, hoje, isso acabou se tornando cada vez mais importante, mas isso não faz sentido. Eu não vou criar uma ADR para falar que você vai usar um tab no Python ao invés de dois espaços, do que quatro espaços, entendeu? Bug, hotfixes, ajustes operacionais. Meu, isso é changelog. Ou deu um problema, é um incidente, tá? Agora, se aquele incidente

03:00

ele fez com que a gente entendesse que a gente precisa mudar arquiteturalmente o sistema, aí eu posso criar uma DR tomando uma decisão de mudança para resolver aquele incidente. E daí você pode até colocar que essa DR tem relação com aquele incidente que aconteceu. Mas a DR não é para registrar incidente.

03:26

A DR é para registrar o que você acabou de tomar de decisão e, nesse caso, para que aquele incidente não aconteça mais. Beleza? E, regrinha aqui para vocês, regrinha dos 3 Es, galera. Seguinte, você vai criar uma DR quando a decisão for estrutural, ou seja, ela afeta como o sistema é construído ou integrado,

03:50

quando é evidente, ou seja, outros desenvolvedores precisarão entender o porquê no futuro, e estável, tem de

04:00

a durar meses ou anos e não semanas. Então, se aquilo que você vai mudar é estrutural, se aquilo que você vai mudar vai ser muito importante para que os outros possam entender ao longo do tempo, ou se aquilo que você está fazendo vai, inclusive, ficar por muito tempo ali em produção, rodando o seu sistema, ou seja, ele gera estabilidade no seu sistema,

04:27

provavelmente você vai querer criar uma ADR. Então, toda vez que você pensar em criar uma ADR... Porque eu vou falar a verdade pra você, tá, galera? Quando eu comecei a aprender Design Patterns, eu não sei se você já sofreu da doença da Paternit. A Paternit é uma doença, assim, incontrolável. Eu queria usar Design Patterns pra qualquer coisa que eu fizesse. Eu tinha 10 interfaces com 10 não sei o quê pra escrever um Olá, Mundo.

04:53

aí eu consegui me curar dessa doença. Aí eu consegui ter uma outra, tá? Que virou, tipo, documentaíte, documentacite. E aí, no final da história, ADR virou um outro sintoma dessa doença, que eu queria sair criando ADR pra qualquer coisa na minha vida, tá? Então, pra que você esteja imune a essa doença, vai aqui a minha vacina pra você.

05:17

Use bem esses critérios, não está escrito em pedra, mas não saiam também criando ADRs para qualquer coisa no seu sistema, porque vai virar mais documento para você dar conta, vai gerar mais ambiguidade na inteligência artificial e pode ser mais prejudicial do que ajudar, tá? Mas eu não tenho dúvidas que você ter

05:39

esses tipos de documentos estruturais que vão ajudar a gerar uma timeline do seu projeto, eu não tenho dúvidas que vai fazer muita diferença aí no seu dia a dia, beleza? Próximo vídeo, a gente vai para um lado um pouco mais prático para eu mostrar algumas coisas para vocês, inclusive mostrar a beleza de você conseguir ver o seu projeto evoluindo ao longo do tempo através de Architecture Decision Records, beleza? Então vamos nessa.

## Resumo IA

**Abreviações**
- **ADR**: *Architecture Decision Record* — registro de decisão arquitetural.
- **PR**: *Pull Request* — solicitação de alteração/revisão de código.
- **README**: arquivo de documentação inicial do projeto, geralmente com orientações gerais de uso e contexto.
- **CONTRIBUTING.md**: arquivo com diretrizes para contribuição no projeto.
- **RFC**: *Request for Comments* — documento leve para discutir e amadurecer propostas.
- **IA**: inteligência artificial.
- **Redis**: banco de dados em memória, frequentemente usado como cache, fila ou armazenamento temporário.

**Resumo**
A aula explicou quando não faz sentido criar um ADR, reforçando que esse tipo de documento serve para registrar decisões arquiteturais duradouras, e não o histórico de execução do trabalho diário. O instrutor destacou que commits, pull requests, issues, code review, changelog e outros artefatos já cobrem mudanças operacionais, correções incrementais e justificativas locais, evitando duplicação e ruído documental.

Foram citados como casos em que ADR geralmente não se justifica: refatorações internas de baixo impacto, decisões temporárias, provas de conceito, experimentos, mudanças que oscilam com frequência, bugs, hotfixes e ajustes operacionais. Nesses cenários, a documentação mais adequada costuma ser issue, changelog, postmortem, documento de incidente, RFC leve, nota de experimento ou documentação de engenharia como README e CONTRIBUTING.md. O ponto central é diferenciar mudanças que apenas afetam o modo como o time trabalha no dia a dia daquelas que alteram a forma como o sistema é construído ou evolui.

Também foi apresentada a regra dos 3 Es para avaliar se uma decisão merece ADR: ela deve ser **estrutural**, **evidente** e **estável**. Estrutural significa afetar a construção ou integração do sistema; evidente significa que outras pessoas precisarão entender o racional no futuro; e estável significa ter expectativa razoável de durar meses ou anos. Essa regra foi apresentada como um filtro prático para evitar transformar ADR em burocracia.

Por fim, a aula alertou para o problema da “documentacite”, o impulso de documentar tudo sem critério. O excesso de ADRs triviais reduz a qualidade do repositório, dificulta a manutenção e piora até o uso por ferramentas de IA, que podem interpretar sinais irrelevantes como se fossem decisões arquiteturais importantes. A mensagem final foi que ADR deve ser usado para construir memória arquitetural útil, e não para registrar qualquer alteração.

**Pontos de atenção**
- ADR **não é log de decisão operacional** nem substitui commit, PR, issue, code review ou changelog.
- **Refatorações internas de baixo impacto** normalmente não justificam ADR.
- **Linters, formatters e convenções triviais** devem ficar em documentação de engenharia, não em ADR.
- **Decisões temporárias**, provas de conceito e experimentos não devem ser “congelados” como ADR.
- Mudanças que **oscilam com frequência** ainda não têm maturidade suficiente para ADR.
- **Bug, hotfix e ajuste operacional** pertencem ao fluxo de manutenção, incidente ou changelog.
- Se um incidente revelar necessidade de mudança estrutural, o **incidente continua documentado no seu artefato próprio** e o ADR registra a nova decisão tomada.
- A regra dos **3 Es** é um bom filtro: se faltar estrutura, evidência futura ou estabilidade, provavelmente não vale ADR.
- Evitar a **“documentacite”**: produzir documentação em excesso aumenta ruído, manutenção e ambiguidade.
- Em contextos com **IA**, documentação irrelevante pode piorar recuperação de contexto e induzir interpretações erradas.
- O objetivo é **documentar melhor, não documentar mais**.