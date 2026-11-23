Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16962)

## Resumo da aula

O Manifesto Ágil surgiu em 2001 como uma resposta à insatisfação com processos de desenvolvimento excessivamente pesados. Retomando o contexto de forte formalização visto antes, a crítica não era à existência de método, mas ao fato de o processo e seus artefatos frequentemente dominarem o trabalho a ponto de afastá-lo do objetivo principal: entregar software útil. Agile marca essa virada porque recoloca a entrega de valor em posição central. A mudança relevante não é “parar de documentar”, mas deixar de tratar a documentação como produto principal.

A frase “software em funcionamento é mais importante que documentação abrangente” estabelece uma prioridade, não uma proibição. Ela afirma que documentação só faz sentido quando sustenta entendimento, implementação, evolução e operação do sistema, em vez de consumir energia apenas para satisfazer o processo. Quando um time passa a usar essa lógica, a pergunta deixa de ser “quanto documento conseguimos produzir?” e passa a ser “qual documentação realmente ajuda o software a funcionar e evoluir?”. Isso reposiciona a documentação como meio de engenharia, não como fim em si mesma.

Antes dessa virada, era comum a documentação ganhar peso semelhante ou até superior ao do próprio software, como se o projeto estivesse representado principalmente nos artefatos. O problema desse arranjo é que o cliente precisa de um sistema utilizável, enquanto documentos extensos, por si só, não entregam comportamento executável. A documentação continua necessária, mas com outro propósito: registrar contexto, decisões e alinhamentos que aumentam a capacidade de construir e manter o produto. Documentar o suficiente passa a ser mais importante do que documentar tudo.

A crítica ágil atinge a burocracia documental quando a produção de artefatos vira pré-condição excessiva para avançar, mesmo sem ganho proporcional de clareza ou qualidade. Nessa situação, o time gasta esforço mantendo documentos grandes, abrangentes e formais que nem sempre ajudam a decidir melhor ou implementar mais rápido. O efeito prático é transformar documentação em fricção operacional. A objeção, portanto, é ao excesso sem propósito, não ao registro técnico útil.

A reação ao excesso anterior produziu dois extremos problemáticos. De um lado, equipes permaneceram presas à ideia de que só é possível desenvolver com documentação extensa, múltiplas fases rígidas e forte formalização; de outro, surgiu a interpretação equivocada de que documentação seria sempre desperdício. Os dois lados falham porque confundem forma com finalidade. Sem equilíbrio, ou o processo sufoca a entrega, ou o conhecimento do projeto fica implícito demais para sustentar continuidade.

Retomando o cenário do projeto documentado, o critério agora não é maximizar volume, mas manter informação suficiente para apoiar software em funcionamento. Documentação com propósito é a que ajuda o time a implementar, alinhar decisões, reduzir ambiguidades e preservar contexto relevante sem competir com o produto pelo centro do processo. Isso exige proporcionalidade: cada registro precisa justificar seu custo pela utilidade que gera. Quando esse princípio é seguido, a documentação deixa de ser peso burocrático e vira suporte real à engenharia.

A engenharia de software muda quando muda a forma de organizar trabalho, feedback e tomada de decisão. Agile foi um marco porque alterou a relação entre planejamento, execução e adaptação, afetando diretamente o papel da documentação dentro do fluxo. Processos diferentes produzem necessidades documentais diferentes: quanto mais iterativo e adaptativo o desenvolvimento, mais a documentação precisa ser útil, atualizável e conectada ao trabalho real. A evolução do processo, portanto, redefine também o que vale a pena registrar.

A inteligência artificial adiciona uma nova camada a essa transformação porque muda novamente a economia da documentação. Se antes o debate era apenas entre excesso e ausência, agora documentos úteis também funcionam como contexto operacional para ferramentas capazes de apoiar implementação, análise e manutenção. Isso reforça a necessidade de registros claros e proporcionais, não de burocracia. O princípio continua o mesmo: documentar para fazer o software funcionar melhor, agora também em um ambiente em que pessoas e sistemas usam esse contexto.

## Transcrição

00:01

Bom, pessoal, e agora a gente vai falar um pouco sobre a Jail e o Manifesto Ágil, tá? Mas saiba que eu estou dando uma pincelada bem clara em diversos aspectos aqui para que a gente tenha essa contextualização inicial, tá? Então, a gente falou de Hooper, a gente falou da forma como o software era desenvolvido antes, em 2001 foi criado o famoso Manifesto Ágil, foi uma galera muito bacana que desenvolvia software,

00:29

mas já não concordava mais de como o formato dos softwares eram desenvolvidos. E aí, então, a gente teve o famoso Manifesto AJAIO. E teve uma frase muito comum, muito interessante, que todo mundo falou é a seguinte, que software em funcionamento é mais importante que documentação abrangente. Ou seja, o AJAIO nunca veio para eliminar a documentação.

00:54

mas mudar o propósito da documentação, ou seja, a documentação deixa de ser um fim nela mesma. Por quê? Porque antes, basicamente, a documentação era o projeto em si também. O cliente quer usar o software, mas, no final das contas, a documentação era o produto.

01:13

tão importante, vamos dizer assim, quanto o próprio software, ou seja, ela não tinha um objetivo necessariamente de ajudar só o software a ser desenvolvido e ser uma plataforma para que o software funcione, mas ela tinha um valor tão expressivo que muitas vezes ela

01:33

acabava sendo até mais importante que o próprio software, tá? E com o Manifesto Ágil, muitas coisas acabaram se desmembrando, metodologias foram criadas, houve também situações onde pessoas iam pro lado do 880, pessoas que já estavam extremamente acostumadas a trabalhar com documentações extremamente grandes, abrangentes, etc.

01:56

que jamais conseguiam, naquela época, assumir que daria para desenvolver software de uma forma diferente, sem ter todas aquelas fases, todos aqueles frameworks para desenvolvimento de um software. Por outro lado, tinha gente que começou a falar, cara, eu nem preciso de documentação.

02:14

eu vou criar o software e acabou, porque documentação é uma perda de tempo. Então, a gente sempre tem que conseguir balancear e, até mesmo hoje, tomar cuidado para a gente nunca ficar ali muito nos extremos, tá? Mas o que aconteceu é que o Manifesto Ágil, as metodologias ágeis, elas surgiram,

02:39

modificaram completamente a forma de desenvolver software, e, hoje em dia, a nossa forma de desenvolver software acaba variando um pouco, e agora, inclusive, com a inteligência artificial, está sendo totalmente reformulada. Eu acredito que, ao longo dos anos agora, a forma de fazer software vai ser cada vez mais diferente mesmo.

03:04

e o Agile foi um marco para aquele momento. E é um marco importante para a gente até hoje. Maravilha? Agora que falamos de Agile, no próximo vídeo eu quero falar com você sobre alguns probleminhas conhecidos e comuns ao trabalharmos com documentação. Beleza? Vamos nessa!

## Resumo IA

**Abreviações**
- **Agile**: Metodologias Ágeis
- **IA**: Inteligência Artificial

**Resumo**
A aula apresenta o surgimento do Manifesto Ágil, em 2001, como resposta à insatisfação com processos de desenvolvimento excessivamente pesados, formais e centrados em documentação. O instrutor destaca que o Agile não veio para eliminar a documentação, mas para mudar seu propósito: ela deixa de ser um fim em si mesma e passa a existir para apoiar o desenvolvimento, a evolução e o funcionamento do software. A frase “software em funcionamento é mais importante que documentação abrangente” é explicada como uma prioridade de valor, e não como uma proibição de documentar. Antes do Manifesto Ágil, a documentação muitas vezes tinha peso equivalente ou até maior que o próprio produto, o que fazia o projeto girar em torno de artefatos em vez de entregar um sistema utilizável.

O fluxo explicado mostra que, com o Agile, a produção de documentação deve ser proporcional à utilidade gerada: deve ajudar a implementar, alinhar decisões, reduzir ambiguidades e preservar contexto relevante, sem criar burocracia desnecessária. O instrutor também alerta para dois extremos comuns após essa mudança: equipes que ainda acreditam que software só pode ser desenvolvido com documentação extensa e processos rígidos, e equipes que interpretam erroneamente o Agile como uma licença para não documentar nada. A aula conclui reforçando que o Agile foi um marco na forma de desenvolver software e que, hoje, com a influência da inteligência artificial, a forma de produzir e registrar conhecimento no desenvolvimento continua mudando, exigindo documentação clara, útil e conectada ao trabalho real.

**Pontos de atenção**
- O Manifesto Ágil **não elimina a documentação**; ele redefine sua finalidade.
- A frase “software em funcionamento é mais importante que documentação abrangente” indica **prioridade**, não proibição.
- Documentação não deve competir com o software como produto principal.
- Evitar **excesso de burocracia documental**, especialmente quando os artefatos não trazem ganho real de clareza ou qualidade.
- Cuidado com os **extremos**:
  - achar que só é possível desenvolver com documentação extensa e processos rígidos;
  - achar que documentação é sempre perda de tempo.
- A documentação deve ser **proporcional ao valor que entrega**.
- Registrar o suficiente para apoiar:
  - entendimento do sistema;
  - implementação;
  - alinhamento de decisões;
  - redução de ambiguidades;
  - preservação de contexto para manutenção.
- Em processos mais iterativos e adaptativos, a documentação precisa ser **atualizável, útil e conectada ao trabalho real**.
- Com o avanço da inteligência artificial, documentos bem feitos passam a servir também como **contexto operacional** para ferramentas e times, reforçando a necessidade de clareza e objetividade.