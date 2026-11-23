Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17053)

## Resumo da aula

Documentos de design e arquitetura formam uma cadeia de abstração que começa no problema de produto e termina na implementação e no registro das decisões. Retomando a noção de níveis de abstração já estabelecida, a diferença aqui é a pergunta que cada artefato responde: o PRD descreve o problema e o valor esperado, o HLD organiza a solução em alto nível, o Feature Design Doc detalha uma feature específica, o LLD aproxima a solução do código, a RFC delibera alternativas e o ADR registra a decisão tomada. Nem todo projeto precisa de todos esses artefatos; a adequação depende do porte da mudança, do risco técnico e da necessidade de alinhamento entre áreas.

HLD, ou High Level Design, descreve como o sistema é estruturado sem entrar em detalhes finos de implementação. Ele existe para transformar contexto de produto em visão técnica compartilhada, mostrando componentes, responsabilidades, integrações e limites da solução. Seu papel costuma aparecer depois do PRD, quando já existe clareza sobre o problema e é preciso discutir a forma geral da solução. Se a mudança for pequena, esse nível pode ser condensado ou até absorvido por um documento mais específico.

Feature Design Doc especifica como uma feature ou módulo será implementado, com foco maior que o HLD e menor que o LLD. Ele responde perguntas como escopo técnico da feature, fluxo principal, impactos no sistema e escolhas necessárias para entregar aquele recurso. A sigla FRD aparece em muitas organizações como nomenclatura legada, próxima desse mesmo papel documental, com herança de uma abordagem mais centrada em requisitos funcionais. O nome importa menos que a função: tornar explícito como uma parte específica do sistema será construída.

Uma feature pequena ou isolada nem sempre exige um HLD completo antes do detalhamento. Nesses casos, o próprio Feature Design Doc pode concentrar o nível de decisão necessário para alinhar implementação, dependências e impacto técnico. Quando a mudança afeta múltiplos módulos, envolve arquitetura mais ampla ou exige coordenação entre times, faz sentido subir um nível e produzir antes um artefato mais high level. A escolha do documento, portanto, é contextual e não ritualística.

LLD, ou Low Level Design, aproxima o design da implementação concreta. Ele detalha endpoints, contratos de comunicação, campos de API, patterns adotados e outras decisões que já orientam diretamente o código. A diferença para o Feature Design Doc está no grau de precisão: o documento de feature pode dizer que haverá determinados endpoints, enquanto o LLD define quais endpoints existirão e como seus contratos serão estruturados. Por isso, o LLD é útil quando a equipe precisa reduzir ambiguidade técnica antes de implementar.

RFC, ou Request for Comments, é um documento de deliberação técnica. Ele circula uma proposta para receber comentários, objeções e alternativas antes da decisão final, sendo especialmente comum em projetos open source e em mudanças com impacto relevante, como novas features ou breaking changes. Seu valor está em expor o raciocínio enquanto a decisão ainda está aberta, permitindo revisão coletiva em vez de validação tardia. RFC não registra a decisão definitiva; ela organiza a discussão que antecede essa decisão.

ADR, ou Architecture Decision Record, registra uma decisão arquitetural já tomada, junto com sua justificativa e seu contexto. Diferentemente da RFC, que é deliberativa, o ADR é o artefato de memória técnica: ele responde por que uma tecnologia, stack, banco de dados ou abordagem foi escolhida e em que condições essa escolha faz sentido. Um ADR pode ficar ativo, ser substituído ou tornar-se inativo quando a decisão deixa de valer. Esse histórico evita que o time precise redescobrir continuamente o motivo das escolhas anteriores.

A diferença central entre RFC e ADR é temporal e funcional. A RFC aparece antes, quando ainda há debate sobre a melhor alternativa; o ADR aparece depois, quando a organização precisa registrar a decisão que venceu esse debate. Em um fluxo maduro, a RFC captura argumentos e contrapontos, e o ADR consolida a decisão técnica de forma clara e sucinta. Nem toda decisão exige os dois documentos, mas confundir discussão com registro costuma gerar perda de contexto.

Retomando o mesmo problema de produto já contextualizado anteriormente, o PRD define o objetivo e as restrições do recurso. O HLD transforma isso em visão estrutural da solução; o Feature Design Doc desce para a implementação daquela feature específica; o LLD fixa contratos, endpoints e detalhes executáveis; se houver dúvida relevante entre alternativas, a discussão pode passar por uma RFC; quando a escolha é feita, ela deve ser registrada em ADR. O valor do ecossistema documental está justamente nesse encadeamento: cada artefato responde uma pergunta diferente sem competir com os demais.

## Transcrição

00:00

Bom, pessoal, e agora nós vamos falar, tá? Vamos fazer um review aí, de forma geral, desses documentos que eles acabam sendo mais comuns. Eu vou dar uma pincelada nesses caras, e depois eu vou trazer com mais detalhes os que eu acredito são mais importantes, e também vou trazer isso aí com exemplos pra vocês, alguns prompts que vão te ajudar a gerar, e também algumas técnicas que eu utilizo pra, inclusive, fazer uma exploração mais clara de como que o design das coisas podem ser realizadas.

00:30

Beleza? Então, vamos lá. Primeiro documento em comum que a gente vai olhar é o HL dele. Na realidade, ele significa High Level Design, ou High Level Document. Basicamente, o grande ponto é que você consiga entender como o sistema é estruturado.

00:48

é uma visão mais de alto nível, ela não contém detalhes tão grandes de implementação, mas ela sim vai conseguir te ajudar de uma visão um pouco mais geral e um pouco mais técnica, te ajudar a falar o que aquilo que você está desenvolvendo faz. Então, normalmente, se eu fosse gerar uma espécie de uma hierarquia, eu iria com o PRD e depois disso eu iria com HLD.

01:14

que na realidade é o documento de High Level Design, e aí esse documento já não tem tanto foco no produto, ele já tem mais foco na parte técnica, enquanto os PRDs acabam falando muito de produto de forma geral.

01:29

Nós também temos um camarada que ele é o Feature Design Doc, tá? Ou, na realidade, muitas pessoas acabam chamando esse também de FRD, que é Feature Requirement Documents, mas normalmente esse nome é um pouco mais legado, vamos dizer, porque eles vêm muito daquela época do HOOP, focando muito em requisitos funcionais e etc.

01:51

mas, ao mesmo tempo, ele ajuda a definir um módulo, uma feature e etc. E, novamente, eu gosto de falar aqui pra vocês, pessoal, não interessa a sigla, não interessa necessariamente o nome específico do documento ou título, o importante é o que o documento acaba mostrando, tá? Então, às vezes, na empresa que você trabalha, esse documento pode ser chamado de outro nome, tá? A ideia desse documento é como que uma feature específica vai ser implementada, tá?

02:19

E normalmente, quando eu falo de feature, pode ser um recurso novo, baseado em um produto, ou como pode ser realmente uma parte do sistema que você está querendo fazer. Então, dependendo da situação, ou dependendo do tamanho do seu projeto, ou se a feature que você vai desenvolver não é algo tão grande, somente com o feature design doc já vai te ajudar.

02:41

Dependendo do nível de tamanho dessa feature, do produto que você está desenvolvendo, aí provavelmente você precisa de algo de mais high level até você chegar nesse feature design doc, tá? Outro camarada que também existe é o LLD, que é o Low Level Design. O Low Level Design, na realidade, ele traz realmente mais detalhes de implementação.

03:05

Ou seja, apesar de um feature design doc, a gente pode falar que a gente vai ter determinados endpoints, o low-level design traz quais serão os endpoints que a gente vai utilizar. Ele vai trazer quais são os contratos de comunicação que aquele sistema vai fazer. Ele vai trazer quais são os principais patterns que vão ser trabalhados. Ou seja, ele vai focar muito mais em regras de implementações.

03:31

algo realmente mais low-level, algo que tende muito mais em trazer, inclusive, códigos ali pra você. Não que no Feature Design Doc a gente não tenha código, a gente pode ter snippets e coisas desse tipo, mas não a nível de implementação, tá? Ao ponto de falar quais vão ser cada campo que vai ser utilizado no contrato de uma API, beleza?

03:54

Depois disso, a gente tem o ADR, que são os Architecture Decision Records. É um dos documentos que são mais comuns e importantes para a gente ter nos dias de hoje. Porque o que ele faz? Ele registra as decisões arquiteturais que foram feitas ao longo de todo o processo. E o interessante é que uma ADR pode ser ativa ou inativa. Ela pode ter sido substituída por uma outra ADR. Então, a gente vai falar especificamente de ADR nas próximas aulas também.

04:24

Mas é importante por quê? Porque ADRs são documentações que você pode ir fazendo para os seus projetos, inclusive, que eles já existem. Por quê?

04:33

porque você olha para aquilo que foi desenvolvido e fala, por que eu tomei aquela decisão? Por que eu tomei aquela decisão? E esses documentos, eles viram ativos, inclusive, como justificativas para ir a entender até que ponto ela deve utilizar determinada tecnologia, ou por que aquela stack, aquela tecnologia, aquele banco de dados foi utilizado

04:54

por qual contexto e até onde esse camarada deve atuar, por exemplo. E nós temos aqui também documentos que são realmente muito comuns de você encontrar, que são as RFCs, que são as Requests for Comments. Então, essas Requests for Comments, na realidade, é um documento que normalmente é gerado por alguém do time, que ele pede para que outras pessoas comentem baseadas naquela

05:22

naquela decisão que ele está querendo tomar tecnicamente. É muito, mas é muito comum esse documento, principalmente em projetos open source. Então, vai ter uma nova feature, vai ter uma breaking change, alguém cria uma RFC, aí outras pessoas discutem, as pessoas votam e tudo mais. Então, a gente poderia dizer que uma RFC é a discussão pela qual vai se tomar uma decisão técnica.

05:46

A ADR basicamente é uma vez que eu tive essa discussão, eu vou registrar essa minha decisão técnica de uma forma clara, sucinta, para que isso fique registrado. Então, vamos dizer que a RFC é a discussão, a ADR é a formalização do motivo pelo qual uma feature, um recurso, um banco de dados ou qualquer coisa que foi

06:12

implantado no projeto, em relações arquiteturais, eles foram realizados, tá? Então, de forma geral, esses documentos aqui, eles são importantes, nem todos os projetos, eles precisam existir, e dependendo do projeto, todos eles, na minha opinião, deveriam existir. Vai depender muito do projeto que você vai trazer, tá? De forma geral, eu vou trazer aqui os mais importantes que a gente acaba utilizando no dia a dia, tá?

06:39

E hoje, eu quero falar especificamente do nosso próximo bate-papo, que é o HLD, o High Level Design. Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **PRD** — *Product Requirements Document*  
- **HLD** — *High Level Design*  
- **FRD** — *Feature Requirement Document*  
- **LLD** — *Low Level Design*  
- **ADR** — *Architecture Decision Record*  
- **RFC** — *Request for Comments*  

**Resumo**  
A aula apresentou os principais documentos usados em design e arquitetura de software como uma cadeia de abstração que vai do problema de produto até a implementação e o registro das decisões técnicas. O instrutor explicou que o **PRD** descreve o problema, o valor esperado e as restrições do produto; o **HLD** traduz esse contexto para uma visão técnica de alto nível, mostrando estrutura do sistema, componentes, responsabilidades, integrações e limites; o **Feature Design Doc** detalha como uma feature ou módulo específico será implementado; o **LLD** aprofunda ainda mais a solução, aproximando-a do código com definição de endpoints, contratos, campos e patterns; a **RFC** é usada para discutir alternativas antes de tomar uma decisão; e o **ADR** registra a decisão arquitetural final, com contexto e justificativa. Também foi destacado que nem todo projeto precisa de todos esses artefatos, e que a escolha depende do tamanho da mudança, do risco técnico e da necessidade de alinhamento entre times. Em termos de fluxo, a sequência geral apresentada foi: PRD para entender o problema, HLD para estruturar a solução, Feature Design Doc para detalhar a feature, LLD para reduzir ambiguidade de implementação, RFC para debate quando houver alternativas relevantes, e ADR para consolidar a decisão tomada.

**Pontos de atenção**  
- A escolha do documento não deve ser ritualística; ela depende do contexto do projeto e do tamanho da mudança.  
- O nome do artefato varia entre empresas, mas o mais importante é a função que ele cumpre.  
- **HLD** não deve entrar em detalhes finos de implementação; seu foco é a visão estrutural e compartilhada da solução.  
- **Feature Design Doc** é suficiente para features pequenas ou isoladas, mas mudanças maiores podem exigir um nível anterior de documentação mais alto.  
- **LLD** deve eliminar ambiguidade técnica e detalhar contratos, endpoints e regras de implementação.  
- **RFC** serve para debate e comparação de alternativas; não deve ser usada como registro definitivo da decisão.  
- **ADR** é o documento de memória técnica: registra a decisão já tomada e o motivo da escolha.  
- Confundir **RFC** com **ADR** pode causar perda de contexto e dificultar a rastreabilidade das decisões.  
- ADRs podem ficar ativas, ser substituídas ou tornarem-se inativas; é importante manter esse histórico organizado.  
- Nem todo projeto precisa de todos os documentos, mas em mudanças mais complexas o encadeamento completo ajuda no alinhamento entre produto, arquitetura e implementação.