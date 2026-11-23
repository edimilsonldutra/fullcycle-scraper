Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17122)

## Resumo da aula

Uma ADR deve registrar uma única decisão arquitetural relevante, não tentar capturar o sistema inteiro em um só documento. Essa granularidade evita documentos longos, vagos e difíceis de manter, além de tornar a timeline arquitetural mais precisa. Quando uma decisão recorrente aparece em vários pontos do sistema, o correto é consolidá-la em um ADR próprio e referenciá-lo onde necessário, em vez de duplicar o raciocínio em vários lugares.

ADR não é narrativa histórica extensa; é registro técnico do raciocínio que levou a uma escolha. O contexto continua indispensável, mas ele existe para sustentar a decisão, não para transformar o documento em texto prolixo. Quanto mais direto o documento for, mais fácil fica revisar, comparar alternativas e usar esse conteúdo em busca, automação e apoio por IA.

Identificadores estáveis como ADR001, ADR002 e variações por domínio, módulo ou componente só funcionam quando seguem uma convenção previsível. O objetivo não é estética, mas rastreabilidade operacional: localizar, ordenar, citar e relacionar decisões sem ambiguidade. Se o time não encontra rapidamente um ADR, o repositório deixa de funcionar como memória técnica e vira apenas um diretório de arquivos.

ADR precisa passar pelo mesmo mecanismo de revisão usado para código: pull request, comentários, aprovação e histórico de mudanças. Isso transforma documentação em artefato governado, reduz decisões mal formuladas e cria responsabilização explícita sobre o que entra no acervo. Em ambientes com IA, essa disciplina é ainda mais crítica, porque prompts, instruções e documentos alteram diretamente o comportamento do agente sobre o sistema.

Retomando a separação entre tipos de documento já estabelecida, o ADR precisa apontar para os artefatos que explicam requisitos e desenho mais amplo, e esses artefatos também precisam apontar de volta para a decisão. Essa linkagem bidirecional cria navegação confiável entre motivo, impacto estrutural e origem funcional da escolha. Sem esse encadeamento documental, o leitor encontra peças soltas, mas não reconstrói o raciocínio completo.

Uma decisão arquitetural raramente nasce isolada: ela pode depender de um requisito descrito em um FDD, de uma restrição consolidada em um HLD ou de outra decisão anterior já aceita. Encadear documentos significa explicitar essas dependências e relações de leitura, para que o acervo forme uma malha coerente em vez de arquivos independentes. Esse cuidado é essencial tanto para humanos quanto para agentes de IA, que inferem melhor quando as conexões já estão declaradas.

A preservação do histórico exige que decisões antigas permaneçam registradas como foram tomadas, mesmo quando deixam de valer. Quando surge uma nova escolha, o correto é criar um novo ADR e ajustar o status ou a relação do anterior, em vez de reescrever retroativamente o documento antigo. Isso mantém a evolução histórica auditável e evita apagar o contexto que justificou decisões passadas.

Quando uma decisão deixa de ser vigente, ela precisa ser explicitamente sinalizada como substituída, em vez de permanecer ambígua no repositório. A referência a status como superseded, já vista anteriormente, ganha aqui um papel operacional: impedir que leitores e ferramentas tratem uma decisão antiga como atual. Em acervos consumidos por IA, essa marcação reduz respostas incorretas baseadas em documentação obsoleta.

Documentação incompleta, contraditória ou mal conectada cria falsa confiança. Um time humano ainda pode desconfiar e investigar, mas um agente de IA tende a usar o texto disponível como contexto válido e propagar o erro em código, sugestões ou análises. Por isso, qualidade documental não é luxo editorial; é requisito operacional para que automação e assistência por IA funcionem com segurança.

Gerar documentação com IA não elimina a necessidade de entendimento profundo sobre o tipo de documento produzido, nem substitui governança. Sem prompt claro, convenção estável e revisão humana, o resultado tende a ser prolixo, inconsistente e contraditório com o restante do acervo. A utilidade da IA depende diretamente da qualidade estrutural dos ADRs e dos vínculos que eles mantêm com os demais documentos do sistema.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior eu falei o status de uma ADR e coloquei alguns metadados que normalmente fazem sentido a gente ter ali, inclusive para a gente entender o histórico de tudo que está acontecendo ali na nossa aplicação. Falei um pouco do fluxo, de que na prática, no dia a dia, acaba sendo dessa forma. E agora, existem alguns pontos de boas práticas que eu recomendaria para você, mas em seguida eu vou tentar deixar isso

00:28

com uma clareza muito maior, como se fosse um esquema, uma forma que você pode usar como um baseline para você. Então, boas práticas. Vamos lá. Crie um ADR por decisão e não por sistema inteiro. Então, entenda que um ADR é uma... Porque uma decisão arquitetural foi tomada. E você não consegue decidir em um documento todos os detalhes de uma...

00:58

do seu software. E fora que uma DR não deve ser grande. Evite narrativa, seja objetivo e técnico. Ou seja, você não precisa contar uma super história e gerar uma complexidade nesse documento para que esse documento exista. No final das contas, você vai dar um contexto. O contexto ajuda muito. Mas, no final do dia, a DR é um documento técnico.

01:25

porque ele vai mostrar qual foi a decisão técnica que a gente escolheu, e por isso que a gente precisa do contexto, tá? Outra coisa, mantenha uma nomenclatura consistente, ADR01, 02, e por incrível que pareça, o padrão de mercado é exatamente esse, ADR001, 002, e depois tem algumas variações que você vai ver por módulo, por componente, por projeto, por back-end, por font-end, por microserviço, tá? Então,

01:53

Depende muito de como você quer organizar, mas tem que ficar fácil de você conseguir gerenciar e achar esses documentos, tá? Use pull requests para revisar e aprovar ADRs. Galera, nunca, como antes inclusive, fazer pull requests de documentação e de texto é tão importante no mundo da inteligência artificial, principalmente porque você mudar um prompt, você mudar uma documentação, vai afetar diretamente como o agente de área vai se portar no seu programa, tá?

02:23

sempre inclua links bidirecionais entre ADRs, HLDs e FDDs. Por quê? Porque eu posso falar que uma ADR foi substituída, ela está relacionada, ela foi depreciada e estão usando essa. Essa ADR tomou uma decisão baseada em um requisito funcional que estava no meu documento.

02:43

de Feature Design Doc, por exemplo, tá? E, normalmente, marque ADRs desatualizadas como superseded, ou seja, para dizer que essa decisão foi substituída. Isso aí, pessoal, é muito importante.

02:59

principalmente por conta de I.A. hoje em dia, tá? Porque a I.A. ela vai olhar a sua DR eventualmente e vai pensar que essa decisão ainda está ativa, mas na real ela foi... já foi substituída por outras decisões ou o pessoal não está usando mais e tudo mais. Então, é importante manter esses documentos organizados. E aí a gente começa a entrar num aspecto que eu acredito que é a grande preocupação de todo mundo que trabalha como documentação, que é

03:29

como fazer para eu manter as minhas documentações atualizadas, tá? E para fazer isso, eu não vou entrar nesse aspecto aqui agora, tá? Isso tem muito mais com o workflow de desenvolvimento, mas saiba que ao longo do tempo a gente não só vai discutir como a gente vai fazer isso na prática, tá bom?

03:46

Mas é importante você entender que esses documentos têm que ser vivos. Mas a grande sacada da ADR é que você não fica alterando a documentação viva, vamos dizer assim. A ADR você muda o status dela e cria um novo documento.

04:04

Então, não é que você fica com documentação desatualizada, você cria novas decisões. Então, ADR é para você colocar algo novo, de alguma decisão nova, e não para você ficar atualizando aquele cara que foi feito há 10 anos atrás.

04:21

Entendeu? Então, isso aí é muito importante porque faz muita diferença. Tomei uma nova decisão, essa nova decisão está registrada, se ela substitui outra, eu só mudo o status da outra. É muito mais simples seguir nesse fluxo do que necessariamente ter que revisitar uma documentação que fez em 2015 e daí sair mudando, escrevendo texto e tudo mais. A gente sabe que no dia a dia isso acaba sendo cada vez mais complicado.

04:47

Hoje, com IA está mais fácil, mas, galera, não caia na seguinte falácia, ah, com IA agora é fácil gerar documentação. Não é, galera. Não é fácil gerar documentação com IA. Você tem que entender muito bem de prompt, você tem que entender profundamente os tipos de documentação que você quer trabalhar, senão vai ficar muito bagunça, muita desorganização, documentações pela metade ou mal organizadas e, às vezes, elas acabam mais atrapalhando do que ajudando.

05:15

Então, se você está utilizando o IA nos dias de hoje para trabalhar com documentação, tome muito cuidado, tenha um prompt muito claro, padronize todo esse processo, porque se você não fizer isso, acredite, você vai ter um monte de encheção de linguiça no seu projeto e que ninguém vai ler, e que quando a IA ler aquele negócio para tentar entender aquilo melhor, para desenvolver o seu software, você vai ver que aquilo tem tanta ambiguidade, tanta contradição com outros documentos,

05:45

que isso mais vai atrapalhar do que ajudar. Beleza? Às vezes, num contexto da IA, é muito melhor você não ter documentação e fazer com que... e você guie ela de uma forma bem mais assertiva do que você ter documentação errada e aí ela pode fazer muita besteira ali no seu código. Beleza? Então vamos nessa porque a gente tem mais coisa ainda pra ver sobre isso.

## Resumo IA

**Abreviações**
- **ADR**: *Architecture Decision Record* — registro de decisão arquitetural.
- **HLD**: *High-Level Design* — documento de desenho de alto nível.
- **FDD**: *Feature Design Doc* — documento de design de funcionalidade.
- **IA**: inteligência artificial.
- **PR**: *Pull Request* — solicitação de revisão/integração de mudanças no repositório.
- **superseded**: substituído, indicando que uma decisão deixou de ser vigente.

**Resumo**
A aula explicou boas práticas para documentação de decisões arquiteturais com foco em ADRs. O instrutor reforçou que cada ADR deve registrar apenas uma decisão arquitetural relevante, evitando tentar documentar o sistema inteiro em um único arquivo. A orientação é manter o texto curto, objetivo e técnico, usando o contexto apenas para sustentar a decisão tomada, sem transformar o documento em narrativa extensa.

Também foi destacada a importância de uma nomenclatura consistente e previsível, como ADR001, ADR002 e variações por domínio, módulo ou componente, para facilitar busca, ordenação e rastreabilidade. O instrutor recomendou que ADRs passem por revisão via pull request, com comentários e aprovação, tratando documentação como artefato governado, especialmente em ambientes onde IA consome esses textos para orientar comportamento, análise e geração de código.

Outro ponto central foi a necessidade de criar links bidirecionais entre ADRs, HLDs e FDDs, permitindo navegar entre requisitos, desenho e decisão. Quando uma decisão é substituída, o correto é marcar o ADR anterior como superseded e criar um novo documento, preservando o histórico sem reescrever retroativamente o passado. Por fim, foi enfatizado que documentação incompleta, contraditória ou mal organizada pode induzir erros tanto em humanos quanto em agentes de IA, e que o uso de IA para gerar documentação exige entendimento profundo, padronização e revisão humana.

**Pontos de atenção**
- Um ADR deve registrar **uma única decisão arquitetural**; não use o documento para descrever o sistema inteiro.
- Evite **narrativa longa ou prolixa**; ADR é documento técnico, não histórico detalhado.
- Mantenha **nomenclatura padronizada e previsível** para facilitar busca, ordem e rastreabilidade.
- Use **pull request** para revisar e aprovar ADRs, tratando documentação com o mesmo rigor do código.
- Inclua **links bidirecionais** entre ADRs, HLDs e FDDs para preservar o encadeamento do raciocínio.
- Marque decisões antigas como **superseded** quando forem substituídas, para evitar ambiguidade.
- Não tente “atualizar” retroativamente ADRs antigos; **crie um novo ADR** para a nova decisão.
- Considere que documentação é **viva**, mas o histórico precisa permanecer auditável e preservado.
- Em contextos com IA, documentação ruim pode gerar **respostas erradas e código incorreto**.
- Não confie apenas em IA para produzir documentação: é necessário **prompt claro, padronização e revisão humana**.
- Documentos mal conectados ou contraditórios geram **falsa confiança** e dificultam a recuperação do raciocínio arquitetural.