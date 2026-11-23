Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17121)

## Resumo da aula

Draft e Proposal não são sinônimos. Draft representa um documento ainda em elaboração, que pode até circular de forma restrita; Proposal indica que a decisão já foi formalmente colocada em discussão ou aprovação. A diferença prática é de governança: um rascunho pode existir sem entrar no processo decisório, enquanto uma proposta já entra no fluxo institucional da arquitetura.

Accepted marca o ponto em que a decisão passa a valer como referência oficial. Isso não significa que toda implementação já foi concluída, mas que o direcionamento arquitetural foi aprovado e deve orientar novas mudanças. Retomando a timeline arquitetural já conhecida, esse status é o marco que torna a decisão vigente no acervo.

Rejected significa que a proposta foi analisada e descartada após avaliação. Withdrawn é diferente: a decisão foi retirada de pauta antes de seguir adiante ou antes de ser aprovada, normalmente por mudança de contexto, prioridade ou interesse. A distinção importa porque um documento rejeitado registra uma negativa deliberada, enquanto um documento retirado registra interrupção do processo, não necessariamente discordância técnica.

Deprecated não apaga a decisão nem invalida automaticamente o que já foi construído com base nela. Esse status apenas informa que a escolha não deve mais ser adotada em novos contextos, embora continue relevante para interpretar sistemas legados. No exemplo recorrente, uma decisão pode deixar de ser recomendada hoje sem exigir migração imediata de tudo que a utilizou no passado.

Superseded indica que uma decisão anterior foi substituída por outra mais recente. Esse estado deve aparecer junto com o vínculo superseded by, que aponta para o ADR sucessor; do outro lado, o novo documento pode declarar supersedes para indicar qual decisão tomou o lugar da anterior. Esse pareamento evita ambiguidade sobre qual ADR está vigente e preserva a leitura histórica da mudança.

O status informa a situação atual do documento, mas os metadados mostram como ele se conecta ao restante do acervo. Campos como supersedes, superseded by e amends transformam ADRs isolados em uma sequência interpretável de decisões. Isso é o que permite reconstruir a evolução arquitetural ao longo do tempo sem depender da memória do time.

Amends deve ser usado quando a decisão antiga continua existindo, mas recebe um ajuste parcial. A lógica aqui não é substituir completamente o ADR anterior, e sim registrar uma correção, extensão ou refinamento que altera apenas parte do seu conteúdo ou escopo. Esse vínculo evita criar uma falsa impressão de ruptura total quando, na prática, houve continuidade com modificação localizada.

relatesTo expressa relação técnica sem dependência obrigatória. No exemplo de ADRs sobre gateways de pagamento, duas decisões podem tratar do mesmo domínio e compartilhar contexto, mas cada uma continua existindo de forma independente. dependsOn é mais forte: a decisão atual só faz sentido ou só funciona porque uma decisão anterior já foi tomada.

O fluxo típico começa com um Draft, que nem sempre é público desde o início e, em alguns contextos, ocupa o espaço que uma RFC ocuparia. Quando o documento é submetido ao time, ao tech lead ou à diretoria, ele passa a operar como proposta; se aprovado, torna-se Accepted. Depois disso, a governança continua: a decisão pode permanecer vigente, ser Deprecated para novos usos ou ser Superseded por uma decisão posterior.

Os status devem refletir o estado real da decisão, e os links devem refletir a relação real entre documentos. Não use Deprecated quando houve substituição explícita por outro ADR; nesse caso, Superseded com referência cruzada comunica melhor a mudança. Também não use relatesTo para esconder dependência estrutural: se a decisão só existe porque outra a sustenta, o vínculo correto é dependsOn.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente falou sobre MADRs e agora eu quero trazer aqui pra vocês alguns pontos que são importantes pra você entender esses tipos de padrão, tá? E eu não quero que você decore essas coisas, mas eu quero que você saiba que essas coisas existem, tá? Então, quando a gente tá trabalhando com uma MADR, principalmente, ou mesmo uma ADR normal, você pode escolher o status e tudo mais, mas existem alguns status que são interessantes, tá?

00:27

Então, a gente tem o status de Proposal. Basicamente, a decisão foi criada, mas ainda ela está em discussão ou aguardando uma aprovação. Então, eu já posso fazer o draft do documento e propor isso ativamente na empresa. Ou seja, eu fiz um rascunho, mas eu propus. Ou seja, eu mandei o documento para frente.

00:48

Aí eu tenho a opção Accepted, ou seja, a decisão foi aprovada e ela está vigente. Eu tenho Rejected, que a proposta que foi analisada foi descartada. Eu tenho Deprecated, ou seja, a decisão continua registrada, mas ela não deve ser mais usada em novos contextos. A gente tem Superseded, ou seja, ela foi substituída por um outro ADR.

01:12

e usado junto com o superseded by apontando para o novo. Ou seja, eu falo que o status dela é superseded, ou seja, ela foi substituída, e embaixo eu tenho outro campo chamado superseded by, e aí eu coloco a ADR que substituiu essa atual, tá?

01:33

E aí a gente tem Draft, que é opcional, basicamente o rascunho do documento que você está fazendo, e Withdrawn, basicamente, é que essa decisão, mesmo antes de ser discutida ou antes de ser aprovada, por algum motivo, o pessoal fala assim, sabe de uma coisa?

01:50

Vamos tirar isso de pauta, acabou, e tá lá. Então, são decisões, normalmente, tanto draft como withdrawal, é bem opcional, e pra falar bem a verdade, eu nunca vi alguém, por exemplo, trabalhando ali com withdrawal, sendo bem honesto durante a minha carreira. Mas, provavelmente, sempre vai ter pessoas que já passaram por essa experiência e tudo bem, tá?

02:11

Agora, metadados importantes para manter as ADRs ao longo do tempo. Eu acho que isso aí é uma das coisas mais importantes, porque se tem algo que faz sentido num projeto, é a linha do tempo no projeto.

02:26

porque você consegue entender como que foi a evolução dele ao longo dos anos. Então, quais metadados são importantes? E, normalmente, eles fazem partes, inclusive, ali do status, mas, normalmente, eles ficam... O status mostra o que aconteceu. Os metadados fazem essas relações. Então, por exemplo, eu tenho superseeds, ou seja, esse ADR substitui o outro,

02:52

por outro anterior, eu tenho o superseded by, ou seja, ele foi substituído por um ADR mais novo, ou seja, quem supersede alguma coisa vai falar quem ele está substituindo, e quem foi substituído vai falar por quem ele foi substituído, essa é a ideia. Amendes significa que eu modifiquei parcialmente uma decisão antiga.

03:16

Eu tenho o relatesTo, que está tecnicamente relacionado, mas não necessariamente ela depende daquela DR para existir. Ou seja, eu tenho uma DR de pagamento com um determinado gateway de pagamento.

03:33

e eu tenho uma forma de pagamento referente a um outro gateway de pagamento. E as ADRs que eu tenho, provavelmente, elas podem estar relacionadas, mas não necessariamente uma depende da outra. Por outro lado, a gente tem dependzone, ou seja, quando uma decisão...

03:52

anterior, a gente depende de uma decisão anterior para funcionar, legal? Somente para você saber como que, normalmente, isso começa a acontecer dentro da empresa. Tem um draft, e nem sempre esse draft é exposto já para todo mundo. Às vezes, esse draft pode substituir uma RFC, que é uma Request For Comments. Feito esse draft, a gente vai propor essa DR para alguém. Pode ser para uma diretoria, pode ser para o tech lead, para o time.

04:20

Uma vez que isso fica aceito, ou seja, ela fica ativa ali, para todo mundo ver que essa DR está valendo, ou nesse ponto depois ela pode ser deprecated, ou seja, a partir de agora a gente não usa mais essa decisão, mas isso não significa que os softwares que a gente tem, que a gente utilizou dessa decisão, eles vão ter que ser migrados.

04:44

Ou seja, ele parou de ser usado daqui a pouco, ou seja, não dá mais suporte. A partir de agora, a gente vai utilizar uma outra abordagem, mas o que a gente já tem está depreciado. Basicamente é isso. Ou a gente pode ter um super cíder, ou seja, eu fiz ADR, ela foi aceita, e daí, eventualmente, surgiu uma outra decisão arquitetural, e com essa outra decisão arquitetural, essa ADR acabou sendo substituída por outra.

05:14

Basicamente, é isso aí, tá? Eu não vou continuar agora porque a gente precisa entrar em alguns pontos de boas práticas e tudo mais, mas a gente continua no próximo vídeo para esse aqui não ficar muito grande.

## Resumo IA

**Abreviações**

- **ADR** — *Architecture Decision Record* (Registro de Decisão de Arquitetura)
- **MADR** — *Markdown Architecture Decision Record* (variação de ADR escrita em Markdown)
- **RFC** — *Request For Comments* (Solicitação de Comentários)

**Resumo**

A aula apresentou os principais status e metadados usados em ADRs/MADRs para organizar e preservar a evolução das decisões arquiteturais ao longo do tempo. O instrutor destacou que **Draft** é apenas um rascunho em elaboração, enquanto **Proposal** indica que o documento já foi formalmente colocado em discussão ou aprovação dentro do fluxo da empresa. Entre os status de vida de uma decisão, **Accepted** representa a aprovação e vigência da decisão, **Rejected** indica que a proposta foi analisada e descartada, **Withdrawn** significa que a decisão foi retirada de pauta antes de ser concluída, **Deprecated** marca que a decisão continua registrada, mas não deve mais ser usada em novos contextos, e **Superseded** mostra que ela foi substituída por outra mais recente.

Também foram explicados os metadados que conectam os ADRs entre si e tornam a linha do tempo arquitetural rastreável. **Supersedes** e **Superseded by** criam o vínculo entre decisão antiga e decisão sucessora, deixando claro qual documento substituiu o outro. **Amends** é usado quando uma decisão anterior continua válida, mas recebe um ajuste parcial, sem substituição completa. **RelatesTo** indica apenas relação técnica entre documentos, sem dependência obrigatória. Já **DependsOn** é usado quando uma decisão só faz sentido ou só funciona porque outra decisão anterior já existe.

O fluxo típico descrito começa com um **Draft**, que pode até ser interno ou substituir uma RFC em alguns contextos, depois ele é submetido ao time, tech lead ou diretoria, passando a ser uma **Proposal**. Se aprovado, vira **Accepted**. A partir daí, a decisão pode seguir vigente, tornar-se **Deprecated** para novos usos ou ser **Superseded** por uma decisão posterior. O foco da aula foi mostrar que o status deve refletir a situação real do documento, enquanto os metadados devem representar corretamente as relações entre decisões, permitindo entender a evolução da arquitetura sem depender da memória do time.

**Pontos de atenção**

- **Draft não é sinônimo de Proposal**: rascunho em elaboração não significa que a decisão já entrou no processo formal de aprovação.
- **Accepted não quer dizer implementação concluída**: indica que a decisão foi aprovada e passou a ser referência oficial.
- **Rejected é diferente de Withdrawn**:
  - **Rejected** = analisado e descartado.
  - **Withdrawn** = retirado de pauta antes de avançar, sem necessariamente haver discordância técnica.
- **Deprecated não invalida o passado**: a decisão continua registrada e pode ser importante para sistemas legados.
- **Não usar Deprecated quando houve substituição explícita**: nesse caso, o correto é **Superseded** com referência cruzada.
- **Sempre parear Superseded com Superseded by**: isso evita ambiguidade sobre qual ADR substituiu qual.
- **Use Amends apenas para ajustes parciais**: não deve ser confundido com substituição completa da decisão anterior.
- **Use RelatesTo apenas para relação técnica**: se houver dependência real, o vínculo correto é **DependsOn**.
- **A semântica do vínculo importa tanto quanto o status**: o status mostra o estado atual, mas os metadados contam a história e a relação entre decisões.
- **A rastreabilidade histórica é essencial**: os links entre ADRs ajudam a reconstruir a evolução arquitetural ao longo do tempo.