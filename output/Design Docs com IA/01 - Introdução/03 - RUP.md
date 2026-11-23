Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16961)

## Resumo da aula

RUP é um processo de desenvolvimento criado pela Rational Software e depois incorporado pela IBM para oferecer uma alternativa mais iterativa ao modelo sequencial já conhecido. A mudança central não foi abandonar documentação, mas reorganizá-la dentro de um fluxo com ciclos menores e pontos de revisão mais frequentes. Isso torna o projeto menos rígido que o waterfall, sem abrir mão de forte controle sobre artefatos, planejamento e coordenação.

O RUP estrutura o desenvolvimento em disciplinas como levantamento de requisitos, análise, design, implementação, teste e gerenciamento de configuração. A função dessa divisão é modularizar o trabalho e deixar explícito o que precisa ser produzido, acompanhado e validado ao longo do projeto. Retomando o cenário de registrar decisões do projeto, esse contexto deixa de ficar preso a um único pacote documental inicial e passa a ser distribuído entre disciplinas que evoluem ao longo das iterações.

As fases do RUP se repetem de forma iterativa, o que cria feedback loops mais curtos do que em processos puramente lineares. Em vez de documentar por longos períodos para só então implementar, o time revisa continuamente o que foi definido, construído e aprendido. O ganho prático é descobrir problemas antes, quando o custo de ajuste ainda é menor.

Inception é a fase em que o projeto define escopo, objetivos e viabilidade de negócio. Ela existe para responder se vale a pena iniciar o esforço e qual problema o sistema realmente pretende resolver. Sem essa base, as iterações seguintes podem ser eficientes na execução, mas desalinhadas quanto ao propósito.

Elaboration aprofunda o projeto ao detalhar a arquitetura, identificar riscos e refinar os requisitos principais. É nessa fase que ambiguidades começam a aparecer com mais clareza, porque decisões de mais baixo nível testam a consistência do escopo inicial. Quando a elaboração revela contradições, o projeto precisa decidir se ajusta a arquitetura ou se revisa o próprio escopo.

Construction corresponde ao desenvolvimento incremental do produto com base na arquitetura já aprovada. O sistema passa a ser construído em partes progressivas, em vez de esperar uma especificação total e imutável antes de começar a codificação. Isso permite entregar blocos funcionais coerentes com as decisões arquiteturais tomadas anteriormente.

Transition cobre a entrega do sistema, o treinamento dos usuários e a correção de falhas observadas na passagem para uso real. Essa fase existe porque software pronto para desenvolvimento interno ainda não está necessariamente pronto para adoção operacional. A transição fecha o ciclo técnico com preocupações de implantação, adaptação do usuário e estabilização.

O RUP usa fortemente casos de uso para modelar requisitos a partir da interação do usuário com o sistema. Se o usuário precisa cadastrar um novo produto para disponibilizá-lo em estoque e verificar esse estoque, esse fluxo vira um caso de uso documentado e implementável. Quando um caso de uso fica pronto, o projeto não ganha apenas texto aprovado: ganha um pedaço funcional do sistema alinhado ao comportamento esperado.

A arquitetura ocupa posição central no RUP porque o processo busca consolidar uma base técnica sólida antes de ampliar a construção do produto. Isso reduz o risco de cada iteração seguir em direções incompatíveis e ajuda a manter coerência entre decisões locais e estrutura global do sistema. Retomando o contexto de decisões do projeto, a arquitetura passa a ser o ponto de referência que organiza o que cada iteração pode construir com segurança.

O RUP explicita papéis como analistas, desenvolvedores e testadores para distribuir responsabilidades com clareza. Em especial, o papel do analista de sistemas concentra atividades de conversar com o cliente, estruturar fluxos, produzir diagramas e preparar insumos para implementação. Essa separação melhora coordenação em ambientes mais formais, mas também aumenta dependências entre funções e etapas.

Gerenciamento de configuração integra o conjunto de disciplinas para controlar versões, mudanças e consistência dos artefatos do projeto. Esse controle combina com a documentação forte do RUP, na qual o avanço depende de registros formais e planejamento detalhado. O benefício é maior rastreabilidade; o custo é mais burocracia e maior esforço operacional.

Em comparação com o waterfall, o RUP permite revisões e ajustes a cada iteração, reduz riscos por validação progressiva e melhora a comunicação entre times e stakeholders. Ainda assim, ele continua mais complexo de gerenciar, exige muita documentação e pode ser caro demais para projetos pequenos. A lição importante dessa transição histórica é que o problema não era documentar ou não documentar, mas encontrar um equilíbrio entre documentação, iteração e coordenação.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior eu falei um pouco, dei uma contextualizada sobre o que acontecia e como a documentação era importante, mas, ao mesmo tempo, existia uma fragilidade muito grande para que as empresas pudessem acompanhar, quer dizer, as documentações, os softwares pudessem acompanhar o mesmo passo que a empresa estava dando ali no mercado. Durante todo esse processo,

00:26

existe um método, existe ainda, que é chamado de ROOP. O ROOP, na realidade, é de uma empresa chamada Rational, e esse método era Rational Unified Process. O ROOP, de forma geral, foi criado pela Rational Software,

00:45

e ele foi comprado pela IBM para oferecer, vamos dizer assim, um processo mais iterativo e flexível que o padrão que era o Waterfall. Mas o RUP ainda tinha um controle extremamente forte de documentação. Então, o que acontece? Quando a gente pega o RUP, a gente acaba pensando em diversas disciplinas que você precisa

01:11

registrar e trabalhar para o desenvolvimento de um software. Então, ele acabava modularizando um pouco mais essas coisas. Então, essas disciplinas como levantamento requisito, análise, design, implementação, teste, gerenciamento de configuração, ele acaba se organizando em algumas fases, tá? E essas fases, elas acabam se repetindo de forma interativa. E a gente já pode imaginar, quando algo se repete de forma interativa, significa que a gente tem

01:37

um feedback loop um pouco mais rápido do que a gente passar um ano apenas documentando para daí começar a desenvolver o software, tá? Então, a ideia inicial ali era a gente ter o quê? Um fluxo muito claro. A primeira parte do fluxo do Rupee, basicamente, era a inception, ou a concepção, onde a gente definia o escopo do projeto, os objetivos do projeto e a viabilidade do negócio.

02:05

a parte de elaboração, que acaba detalhando a arquitetura do sistema, identifica riscos e acaba refinando os requisitos principais. Isso é muito legal porque, uma vez que você tem o escopo do projeto, e quando você começa a entrar num ponto um pouco mais baixo nível, a gente começa a entrar em decisões ambíguas, coisas que acabam se contradizendo. E aí, a gente acaba tirando ali a prova dos nove, ou seja,

02:32

o que está certo? É o escopo que foi colocado ou essa elaboração? Será que, baseada nessa elaboração, vale a pena mudar o escopo do projeto? Então, esses são pontos que são importantes aí também. Aí, a gente tem a parte de construção, que é o desenvolvimento incremental do produto com base na arquitetura aprovada, ou seja, no passo anterior.

02:56

E aí, a gente tinha o outro ponto, que é Transition, que é a entrega do sistema, treinamento dos usuários e as correções de falha. Então, basicamente, era esse fluxo que a gente acabava trabalhando com o Rupee. Eu lembro que quando eu comecei a fazer uma pós-graduação em Engenharia de Software, eu estava bem na época

03:21

que estava tendo uma transição muito forte do Scrum ou das metodologias ágeis, do manifesto ágil que tinha surgido, mas ainda nessa minha

03:36

nessa minha disciplina que eu fazia de pós-graduação em engenharia de software, no final das contas, eu também aprendi e vi como é que funcionava o HUP. Por outro lado, eu também estava começando a entender bem ali quando começava a gente falar de

03:55

de TDD, BDD, a gente falava de pair programming e coisas desse tipo, tá? Agora, voltando aqui no Rupee, o lance é o seguinte, quais eram os principais diferenciais desse cara, tá? Era o seguinte, o processo era iterativo, ou seja, a gente conseguia criar ciclos de desenvolvimento menores dentro de cada fase, ou seja, não precisava esperar

04:17

tudo fica pronto para eu falar, daqui um ano, que a coisa não funcionou, tá? E o RUP, ele tem uma forte utilização do quê? De caso de uso. Ou seja, os requisitos que a gente tem no sistema, eles são modelados a partir de como que o usuário interage com o sistema. Então, ah, eu tenho um momento onde eu vou cadastrar um novo produto para disponibilizar isso para um estoque e fazer uma verificação de estoque.

04:45

Ou seja, eu tenho esse caso de uso documentado, eu tenho esse caso de uso de como ele vai ser feito. Quando esse caso de uso fica pronto, eu tenho um pedaço já do meu sistema. Então, isso acabava ajudando bastante. O Ruby também tinha uma arquitetura centralizada, ou seja, ajudava a gente a definir uma arquitetura realmente sólida antes de construir o produto.

05:09

Parece óbvio, principalmente pra gente hoje, mas acredite que há muito tempo atrás fazer uma organização e trabalhar e organizar muito arquitetura de software não era tão simples assim. Hoje a gente tem muita documentação, a gente tem muito histórico desde 70 até 2025, 2030 e etc.

05:33

Um legado muito grande que a gente consegue estudar, mas, nessa época, as coisas estavam sendo criadas. Um outro ponto era... Um dos diferenciais era a parte que a gente tinha role, papéis. Ou seja, a gente tinha claramente os papéis de analistas, desenvolvedores, testadores, etc. Ou seja, nessa época, principalmente, nós tínhamos o papel do analista de sistema.

05:57

Ou seja, o cara que fala com o cliente, o cara que analisa, o cara cria os fluxos, ele cria os diagramas, ele faz ali todas aquelas análises para garantir que as coisas estão redondas, para daí o desenvolvedor pegar aquilo e transformar em código. Basicamente, era essa a ideia.

06:14

Agora, quais eram essas principais vantagens que o ROOP tinha em relação ao método waterfall? Basicamente, ele permite revisões e ajustes em cada iteração, porque cada vez que eu tenho uma nova iteração, eu acabo vendo antes se o que eu fiz gerou um problema ou se está fazendo sentido a minha próxima tarefa, baseado naquilo que já existe, por exemplo.

06:40

Acabava também reduzindo o risco, porque partes do sistema são validadas progressivamente, melhora também a comunicação entre os times e os stakeholders, ou seja, os participantes de forma geral dos projetos. Desvantagens é mais complexo de gerenciar do que waterfall.

06:59

Existe ainda, exige muita documentação e planejamento e pode ser custoso, inclusive para projetos pequenos. E aí era um ponto importante, tá? Como a gente trabalhava muito no modelo ali de fábrica e dentro de processos extremamente definidos, às vezes um software muito simples, ele demorava muito tempo para ser desenvolvido pelo fato de uma burocracia

07:22

exagerada em relação a isso, tá? Mas, de forma geral, quando a gente falava em RUP, tinha toda uma metodologia, software, que organizava todos esses projetos, etc, tá? Então, é bem interessante, realmente, e o foco ali nos casos de usos muito bacanas, tá? Então, falamos rapidamente aqui sobre RUP, a gente vai, em seguida, falar agora sobre Agile, e vamos nessa.

## Resumo IA

**Abreviações**  
- **RUP** — *Rational Unified Process* (Processo Unificado Rational)  
- **IBM** — *International Business Machines*  
- **TDD** — *Test-Driven Development* (Desenvolvimento Orientado a Testes)  
- **BDD** — *Behavior-Driven Development* (Desenvolvimento Orientado a Comportamento)  

**Resumo**  
A aula apresentou o RUP como um processo de desenvolvimento criado pela Rational Software e posteriormente incorporado pela IBM, com o objetivo de oferecer uma alternativa mais iterativa e flexível ao modelo waterfall, sem abrir mão de forte controle documental. O instrutor destacou que a principal mudança não foi abandonar a documentação, mas reorganizá-la em disciplinas e ciclos menores, com revisões frequentes e feedback mais rápido, permitindo identificar problemas antes e reduzir custos de correção.

O RUP foi explicado a partir de suas disciplinas principais, como levantamento de requisitos, análise, design, implementação, teste e gerenciamento de configuração, que ajudam a modularizar o trabalho e deixar explícitos os artefatos e validações esperados em cada etapa. Também foram descritas as fases do processo: **Inception**, responsável por definir escopo, objetivos e viabilidade do negócio; **Elaboration**, dedicada ao detalhamento da arquitetura, identificação de riscos e refinamento dos requisitos; **Construction**, que trata do desenvolvimento incremental do produto com base na arquitetura aprovada; e **Transition**, voltada à entrega do sistema, treinamento dos usuários e correção de falhas em uso real.

Outro ponto central foi o uso intenso de **casos de uso** para modelar requisitos a partir da interação do usuário com o sistema, transformando necessidades de negócio em comportamento implementável. O instrutor enfatizou ainda que a arquitetura ocupa posição central no RUP, servindo como base técnica sólida para orientar as iterações, evitar incoerências entre decisões locais e manter a coerência global do sistema. Além disso, o processo explicita papéis como analistas, desenvolvedores e testadores, destacando o papel do analista de sistemas como responsável por conversar com o cliente, estruturar fluxos, produzir diagramas e preparar insumos para implementação.

Por fim, o gerenciamento de configuração foi apontado como parte essencial do processo, controlando versões, mudanças e consistência dos artefatos. Na comparação com o waterfall, o RUP foi apresentado como mais adaptável e capaz de reduzir riscos por validação progressiva e melhor comunicação entre times e stakeholders, embora com maior complexidade de gestão, mais documentação e custo elevado para projetos pequenos.

**Pontos de atenção**  
- O RUP não elimina documentação; ele a reorganiza e exige controle formal dos artefatos.  
- A abordagem iterativa reduz riscos, mas não dispensa planejamento detalhado e coordenação entre disciplinas.  
- A fase de **Inception** é crítica para evitar que o projeto avance com escopo mal definido ou sem viabilidade de negócio.  
- Na **Elaboration**, inconsistências e ambiguidades tendem a aparecer; pode ser necessário revisar escopo ou arquitetura.  
- A arquitetura deve ser consolidada antes da expansão da construção, para evitar que iterações sigam em direções incompatíveis.  
- Casos de uso são centrais: requisitos devem ser modelados com foco na interação do usuário com o sistema.  
- A separação de papéis melhora a organização, mas aumenta dependências entre analistas, desenvolvedores e testadores.  
- O gerenciamento de configuração é indispensável para controlar versões, mudanças e rastreabilidade.  
- Apesar das vantagens, o RUP pode ser complexo, burocrático e caro, especialmente em projetos pequenos.  
- O processo funciona melhor em contextos que aceitam forte formalização e documentação; pode ser pesado para equipes que buscam alta agilidade.