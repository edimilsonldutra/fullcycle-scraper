Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16970)

## Resumo da aula

Um PRD de feature não replica integralmente a estrutura de um PRD macro. Ele mantém apenas as seções que aumentam clareza operacional para uma entrega específica, com foco no que precisa ser entendido antes da implementação. Retomando a ideia de granularidade já estabelecida, a diferença aqui não é só de tamanho, mas de tipo de detalhe: o documento sai do enquadramento estratégico e entra no nível de execução do time. A estrutura continua flexível, mas alguns blocos tendem a aparecer com frequência porque concentram as decisões mínimas para alinhar produto, desenvolvimento e IA.

O resumo da feature abre o documento com uma descrição curta do que está sendo construído e do problema que isso resolve. Essa seção existe para evitar que a feature seja lida como uma lista solta de requisitos, sem causa nem finalidade. No exemplo do rate limiter, o resumo não é “implementar limitação de requisições”, mas registrar que há excesso de acessos derrubando o sistema e que a feature existe para conter esse comportamento. Quando esse contexto está explícito, decisões posteriores deixam de depender de interpretação implícita.

Objetivos e métricas já fazem parte do repertório do PRD; no nível da feature, eles ficam mais diretos e verificáveis. Os objetivos costumam aparecer como bullet points que declaram o resultado esperado da entrega, enquanto as métricas definem como confirmar se esse resultado foi alcançado. Essa combinação impede que a feature seja considerada bem-sucedida apenas porque foi implementada. O critério passa a ser impacto observável, não apenas conclusão técnica.

Escopo delimita o que entra e o que fica de fora da feature, reduzindo expansão informal durante a execução. Em um PRD de feature, essa seção precisa ser objetiva porque pequenas ambiguidades já viram retrabalho técnico rapidamente. O valor dela está em proteger a unidade da entrega: o time sabe o que precisa resolver agora e o que pertence a outra iniciativa. Sem essa fronteira, a feature tende a crescer por acúmulo de expectativas não registradas.

Requisitos funcionais descrevem as capacidades concretas que a feature precisa oferecer. Eles respondem quais recursos existirão, quais comportamentos o sistema deve suportar e quais elementos precisam estar presentes para que a solução cumpra sua função. Se a feature exigir login, uma estratégia específica de storage ou outros componentes necessários ao comportamento esperado, isso precisa aparecer aqui. Esse bloco organiza o que será entregue em termos de funcionalidade observável, sem virar desenho técnico detalhado.

Requisitos não funcionais registram restrições de qualidade e operação que condicionam a solução. Eles não dizem apenas o que o sistema faz, mas em que condições ele precisa funcionar adequadamente, como latência, disponibilidade ou limites de indisponibilidade. No exemplo do rate limiter, exigir latência de pelo menos 10 milissegundos e controlar tempo máximo de indisponibilidade muda diretamente a viabilidade da implementação. Sem esse bloco, a solução pode cumprir a função e ainda assim falhar no contexto real de uso.

Fluxo do usuário é a descrição de como a feature será utilizada do ponto de vista de interação e sequência de uso. Essa seção torna explícito o caminho esperado, o que ajuda a detectar lacunas entre requisito listado e experiência real. Em um PRD de feature, o fluxo evita que o time implemente capacidades isoladas sem entender a ordem, a dependência e a lógica de uso entre elas. Para IA, esse bloco também reduz inferências erradas sobre comportamento esperado.

Dependências identificam tudo aquilo de que a feature precisa para existir ou funcionar corretamente, seja outro sistema, módulo, serviço ou decisão prévia. Torná-las explícitas evita planejar a implementação como se ela fosse autônoma quando, na prática, depende de integrações ou pré-condições. Esse mapeamento melhora estimativa, priorização e coordenação entre times. Também ajuda a IA a não propor soluções desconectadas do ecossistema real do projeto.

Critérios de aceitação definem a checklist que precisa estar satisfeita para a feature ser considerada completa. Eles transformam a noção vaga de “pronto” em condições verificáveis, úteis para validação de produto, desenvolvimento e testes. Em vez de depender de julgamento subjetivo, o time passa a ter uma referência explícita de encerramento da entrega. Esse bloco é especialmente importante quando a feature envolve múltiplas regras e pode parecer concluída antes de realmente atender ao esperado.

Riscos continuam relevantes, mas aqui aparecem conectados à execução concreta da feature, não ao enquadramento macro da iniciativa. Eles registram incertezas que podem comprometer desenvolvimento, adoção ou comportamento esperado da solução. As considerações gerais funcionam como fechamento do documento: reúnem observações complementares que não cabem bem nas outras seções, mas ainda influenciam decisão e implementação. Esse fechamento preserva nuances importantes sem forçar encaixes artificiais em blocos inadequados.

O PRD de feature se aproxima mais do cotidiano de desenvolvimento porque organiza informações diretamente acionáveis para construir a entrega. Retomando o papel do PRD como contexto para IA, esse formato reduz ambiguidade sobre o que o código precisa resolver, quais limites respeitar e quais condições definem sucesso. Ele não substitui design docs, mas melhora muito a qualidade dos artefatos técnicos produzidos depois. Quanto mais explícitas estiverem essas seções, menor a chance de o time ou a IA preencherem lacunas com suposições erradas.

## Transcrição

00:01

Bom, pessoal, agora que eu acredito que ficou um pouquinho mais claro para a gente entender um pouco mais sobre PRD de alto nível, um PRD de mais baixo nível, nesse caso eu estou colocando ele como uma feature, provavelmente você vai ter sessões também nesse documento. E um ponto importante é que provavelmente você não vai ter

00:24

todas aquelas sessões daquele PRD de mais alto nível. Então, novamente, o documento é flexível, nem sempre você vai precisar utilizar todas as sessões, mas, normalmente, ainda mais se o projeto for um pouco maior,

00:40

você vai ter que ter sessões pelo menos parecidas ou correlatas com isso aqui, que é resumo da feature, o resumo do módulo, o resumo daquilo que você está fazendo, ou seja, o que essa parada faz e o porquê. Ou seja, o que ela vai resolver? Qual é o contexto? Eu vou desenvolver um rate limiter porque tem muita gente derrubando acesso ao meu sistema e tudo mais. Ou seja, eu estou falando o que está acontecendo e com o rate limiter a gente vai resolver esse problema.

01:10

Qual que é o objetivo principal? Aí, objetivo, normalmente, são bullet points explicados. Objetivo eu falo, eu quero isso, eu quero isso, eu quero aquilo. E, novamente, métrica. Como que eu meço se eu conseguir achar aquele objetivo? Qual o escopo? Ou seja, o que vai entrar e o que não vai entrar? Quais são os requisitos funcionais? Ou seja, o que vai ter? Quais são os recursos que vão ter?

01:36

vai precisar ter esse sistema de login, a gente vai precisar fazer uma estratégia de storage fazendo dessa forma, eu vou precisar fazer isso, vou precisar fazer aquilo, os requisitos funcionais vão ser muito mais focados de coisas muito mais qualitativas, por exemplo, o rate limiter tem que ter uma latência de pelo menos 10 milissegundos, ele tem que...

02:00

ele não pode ficar indisponível por tanto tempo, ou seja, são requisitos não funcionais, como que é o fluxo do usuário, ou seja, como é que vai ser a utilização desse cara, quais são as dependências que eu tenho, quais são os critérios de aceitação, ou seja,

02:16

Para eu dizer que esse negócio está completo, eu preciso dessa checklist preenchida. E quais são os riscos que eu tenho a utilizar ou tentar desenvolver esse projeto, e quais são considerações gerais que eu devo fazer. Então, se você perceber, esse documento já acaba caindo um pouco mais no nosso mundo do desenvolvimento.

02:39

Porque, se você perceber, tem muito a ver com o que a gente faz no dia a dia. E é por isso que eu estou dizendo aqui para vocês que é o seguinte, apesar de um PRD não ser um documento de design doc, ele é um documento extremamente importante, principalmente para a inteligência artificial entender do que se trata aquele monte de código e projetos que você está pedindo para ela desenvolver.

03:03

e também, obviamente, para o seu time, para você e tudo mais, tá? Então, nessa PRD de feature, vamos dizer, essas sessões, normalmente, elas vão estar por aí. Beleza?

## Resumo IA

**Abreviações**
- **PRD** — *Product Requirements Document* (Documento de Requisitos do Produto)
- **IA** — Inteligência Artificial
- **UI** — não mencionado explicitamente na aula

**Resumo**
A aula explicou como estruturar um PRD de feature, deixando claro que ele não precisa repetir integralmente a estrutura de um PRD macro. Nesse nível mais granular, o documento deve priorizar informações diretamente acionáveis para a implementação, reduzindo ambiguidade e alinhando produto, desenvolvimento e IA.

O instrutor destacou que o PRD de feature normalmente começa com um resumo da feature, descrevendo o que está sendo construído e qual problema ela resolve. O objetivo dessa abertura é evitar que a feature seja interpretada como uma lista isolada de requisitos, sem contexto de negócio ou operação. Foi dado o exemplo de um rate limiter criado para conter excesso de acessos que derrubam o sistema.

Em seguida, foram apresentados os blocos mais recorrentes desse tipo de documento: objetivos, métricas, escopo, requisitos funcionais, requisitos não funcionais, fluxo do usuário, dependências, critérios de aceitação, riscos e considerações gerais. Os objetivos descrevem o resultado esperado; as métricas definem como verificar se esse resultado foi atingido. O escopo delimita o que entra e o que fica fora da entrega. Os requisitos funcionais listam as capacidades e comportamentos que a feature precisa oferecer, enquanto os requisitos não funcionais tratam de condições de qualidade e operação, como latência e disponibilidade.

O fluxo do usuário serve para explicitar a sequência de uso da feature, ajudando a evitar implementação fragmentada ou desconectada da experiência real. As dependências deixam claro o que a feature precisa para existir ou funcionar, como outros sistemas, módulos ou decisões prévias. Os critérios de aceitação transformam o conceito de “pronto” em uma checklist verificável. Por fim, riscos e considerações gerais registram incertezas, restrições e observações importantes que influenciam a execução.

A aula concluiu reforçando que o PRD de feature se aproxima bastante do cotidiano de desenvolvimento e é muito útil tanto para o time quanto para a IA, porque reduz suposições erradas e melhora a qualidade dos artefatos técnicos produzidos posteriormente.

**Pontos de atenção**
- O PRD de feature não deve copiar integralmente a estrutura do PRD macro; ele deve manter apenas o que ajuda na execução.
- O documento é flexível, mas precisa conter seções correlatas às principais decisões da entrega.
- O resumo da feature deve explicitar contexto e problema, não apenas descrever a funcionalidade de forma genérica.
- Objetivos e métricas precisam ser verificáveis; não basta a feature estar implementada, ela precisa gerar o resultado esperado.
- O escopo deve ser bem delimitado para evitar expansão informal durante a execução.
- Requisitos funcionais devem descrever o que a feature precisa fazer, sem virar um design técnico detalhado.
- Requisitos não funcionais são críticos para viabilidade e operação; ignorá-los pode gerar soluções corretas na função, mas inadequadas no uso real.
- O fluxo do usuário ajuda a identificar lacunas entre requisitos isolados e a sequência real de utilização.
- Dependências devem ser explicitadas para evitar falsas suposições de autonomia da feature.
- Critérios de aceitação precisam funcionar como checklist objetiva de conclusão.
- Riscos e considerações gerais não devem ser omitidos, pois podem impactar desenvolvimento e adoção.
- Quanto mais explícito o PRD, menor a chance de o time ou a IA preencherem lacunas com suposições incorretas.