Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17056)

## Resumo da aula

Um prompt de HLD pode operar como uma entrevista guiada: em vez de pedir um texto livre, ele conduz a coleta de contexto por perguntas estruturadas e transforma as respostas em um draft inicial. Isso reduz o esforço de começar do zero e força a cobertura de seções que costumam ser esquecidas, como riscos, observabilidade e interfaces públicas. O valor não está em automatizar a arquitetura inteira, mas em organizar a extração de contexto técnico de forma repetível.

Retomando o encadeamento já estabelecido, o PRD entra aqui como insumo para que o HLD não nasça apenas de respostas improvisadas durante a entrevista. Quando o prompt recebe também documentos técnicos, anotações de reunião ou pesquisa prévia, o draft sai mais próximo da realidade do problema e exige menos preenchimento manual. A qualidade do resultado depende menos da eloquência do prompt e mais da densidade do contexto anexado.

Um template reutilizável fixa o formato esperado do documento antes da geração, com seções como contexto, arquitetura geral, componentes, fluxo de requisição, modelo de dados, interfaces públicas, escalabilidade, segurança, observabilidade e riscos. Isso evita que a IA produza texto solto ou reorganize o HLD de maneira inconsistente a cada execução. O template também facilita revisão humana, comparação entre documentos e adaptação ao padrão interno do time.

Defaults inteligentes são valores ou decisões assumidas pelo prompt quando a informação ainda não foi fornecida explicitamente, desde que isso seja feito de forma controlada. Eles existem para reduzir fricção na geração inicial e impedir que o processo pare por falta de detalhes menores. O uso correto desses defaults acelera o draft, mas exige revisão posterior porque uma suposição plausível ainda pode estar errada para a empresa ou para a feature.

JSON funciona como formato operacional para o HLD gerado por IA porque transforma seções do documento em uma estrutura previsível e manipulável por ferramentas. Em vez de depender apenas de texto corrido, o time pode validar campos, reaproveitar blocos, versionar estruturas e até alimentar outros fluxos automatizados. O objetivo não é substituir a leitura humana, mas tornar a geração mais consistente e integrável.

Checagem de consistência é a etapa em que o prompt verifica se as partes do HLD não se contradizem antes de finalizar o draft. Se a arquitetura geral sugere um componente centralizado, por exemplo, o fluxo principal, os riscos e as preocupações de escalabilidade precisam refletir essa escolha. Essa validação evita documentos formalmente bonitos, mas internamente incoerentes.

A IA acelera a produção do HLD porque ajuda a estruturar perguntas, preencher o esqueleto e expandir partes técnicas recorrentes. Ainda assim, ela não gera sozinha um documento confiável para contextos específicos de empresa, domínio e funcionalidade. O papel humano continua sendo decidir, corrigir, complementar e remover generalizações inadequadas.

O prompt não deve ser tratado como peça fixa; ele precisa ser modificado conforme o workflow do time, o tipo de projeto e o nível de documentação já existente. Em alguns contextos, a entrevista será o ponto de partida; em outros, o processo começa com PRD, pesquisa técnica e um template já preenchido parcialmente. Adaptar o prompt ao processo real reduz atrito e aumenta a utilidade do draft gerado.

Retomando o HLD de rate limiting já conhecido, a nova camada aqui não é redesenhar a solução, mas reconstruí-la por meio de insumos, perguntas e um esqueleto de documento. O prompt pode pedir objetivos técnicos, componentes, fluxo principal, riscos e preocupações transversais, usando aquele documento como referência estrutural. Com isso, o time passa de escrita manual integral para geração assistida de um primeiro rascunho revisável.

O fluxo mais útil é: reunir insumos, executar a entrevista guiada, gerar o draft no template escolhido, rodar checagem de consistência e revisar manualmente. Esse processo reduz a fricção de começar do zero sem terceirizar o raciocínio arquitetural. O resultado esperado não é um documento final perfeito, mas um draft inicial mais mastigado e mais barato de evoluir.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente falou sobre high-level design e aqui eu quero trazer para vocês, somente para você conseguir ter uma ideia de como é que funciona um prompt para gerar esse documento. Então, a ideia desse prompt é que ele funciona exatamente como o prompt que aquele PRD faz, mas a ideia aqui é que ele acabe te entrevistando e no final ele vai gerar um documento como esse.

00:28

Qual é o ponto principal que eu gostaria que você sempre entendesse? Essas entrevistas, esses tipos de prompts vão te ajudar a gerar realmente esse documento. Por outro lado, o que acontece? Às vezes,

00:44

Eu prefiro não ficar apenas sendo entrevistado pra ir agirar tudo, mas eu, muitas vezes, o que que eu acabo fazendo, e depois eu vou dar algumas dicas pra vocês, tá? Mundo real, como que eu trabalho. Isso não significa que você precisa trabalhar da mesma forma.

01:00

mas normalmente eu pego um PRD, normalmente eu faço uma pesquisa sobre o assunto que eu quero trabalhar, e daí, baseado nisso, eu começo a fazer uma espécie de entrevista dessa, eu tenho o formato do documento que eu quero,

01:16

e aí eu começo a trabalhar em cima desse formato, em cima desse template, tá? Por quê? Porque aqui não é simplesmente sair cuspindo conteúdo. Basicamente, o conteúdo que é gerado nesse documento é específico da empresa, da funcionalidade que você quer colocar. Então, não necessariamente ela vai conseguir te ajudar em tudo. Ela vai te ajudar em muita coisa, principalmente na parte técnica, porque ela tem conhecimento técnico de forma geral. Mas ela não vai ser responsável por gerar 100% do seu documento.

01:45

porque são pontos realmente muito peculiares que acabam acontecendo, tá? Mas, basicamente, tem os princípios da entrevista para trabalhar com uma linguagem simples e direta, e aqui, se você perceber, eu tenho regras para coletar informação, ou seja, quais são os objetivos técnicos, a arquitetura geral, os componentes, e aqui eu tenho um processo de entrevista, ou seja, eu faço as principais perguntas que fazem sentido para a gente gerar esse documento.

02:13

O contexto, a arquitetura geral, os componentes, o fluxo de requisição, o modelo de dados, as interfaces públicas, as considerações de escalabilidade, segurança, observabilidade, riscos, ADRs, caso eu queira associar, porque uma ADR pode ser feita

02:31

tanto na hora de definir um high-level design ou também ela pode ser feita depois que uma decisão já foi tomada e a gente só quer registrar esse camarada aqui. Então, se você entender, essa que é a ideia. E aqui tem estrutura de dados em JSON caso você queira trabalhar.

02:48

Então tenho os defaults inteligentes, checar a consistência antes de finalizar, e aqui eu tenho um esqueleto de como que ela deve ser gerada, que se você perceber é bem parecido com o que eu acabei mostrando ali pra vocês, eu não adicionei a parte de ADR. E aqui tá pra gente...

03:08

a mensagem inicial do usuário. Agora, até que ponto você deve utilizar isso? Eu acho que vale a pena sim você utilizar, mas, normalmente, eu colocaria mais contexto, dependendo desse prompt, anexando documentos um pouco mais técnicos, documentos, reuniões, ou até mesmo, principalmente, o PRD, porque vai ajudar para que esse documento saia

03:35

mais mastigado o draft dele do que você ficar respondendo 100% das perguntas a todo momento, tá? Então, o que eu recomendo é, utilize esse prompt ou modifique esse prompt de acordo com o seu fluxo de trabalho, tá? Esse aqui é um prompt que ele vai realmente te ajudar a gerar esse documento, mas normalmente, quando a gente vai criar algo do zero, a gente sempre tem mais fricção. Por isso que...

04:02

vale a pena você ver se você tem algum documento complementar para te ajudar a gerar isso e você conseguir sair fazendo também as correções, tá? Então, dá para a gente fazer isso bastante, eu faço bastante isso. Depois eu vou mostrar para vocês, inclusive, como é que eu faço o meu ponto de pesquisa, a minha Deep Research, como é que eu consigo, inclusive, padronizar

04:27

os arquivos e as Deep Researches que eu faço, que vão ajudar eu criar o projeto, principalmente quando eu tiver mais dúvidas técnicas e de implementação. Fechou? Então, esse Prompt vai estar disponibilizado aí pra você. Dê uma olhada, teste, modifique, mas o importante que eu quero deixar claro aqui, pessoal, a gente está falando de documento, e normalmente documento específico da sua empresa,

04:52

Então, por isso que é importante que você atue diretamente para trabalhar, aí ela vai te ajudar. Uma das coisas que eu acho que é mais útil nesse prompt e coisas desse tipo é dar, pelo menos para vocês, o esqueleto de como que fica o documento, tá? Então, baseado também no documento do Rate Limiting, eu acho que acaba sendo um exemplo bom que você pode utilizar como base

05:16

falando que você quer um documento seguindo aquele esqueleto ou essas sessões que eu acabei colocando aqui pra gente, tá? Então, eu queria que vocês levassem isso aí em conta em relação a esse documento. Fechou? Então é isso, a gente vai pra um próximo documento. Esse documento, na minha opinião, é um dos mais importantes pra quem é desenvolvedor, porque aí ele já vai entrar com um nível maior de detalhe técnico. Então, vamos nessa.

## Resumo IA

**Abreviações**
- **PRD** — *Product Requirements Document* (Documento de Requisitos do Produto)
- **HLD** — *High-Level Design* (Projeto/Design de Alto Nível)
- **ADR** — *Architecture Decision Record* (Registro de Decisão de Arquitetura)
- **JSON** — *JavaScript Object Notation* (Notação de Objeto JavaScript)

**Resumo**
A aula apresentou como usar um prompt de HLD como uma entrevista guiada para coletar contexto técnico de forma estruturada e, ao final, gerar um primeiro rascunho de documento. O instrutor explicou que esse tipo de prompt não deve ser visto como uma solução completa para criar a arquitetura sozinho, mas como um mecanismo para organizar perguntas e garantir que seções importantes não fiquem de fora, como contexto, arquitetura geral, componentes, fluxo de requisição, modelo de dados, interfaces públicas, escalabilidade, segurança, observabilidade e riscos.

Foi destacado que o PRD e outros insumos, como documentos técnicos, anotações de reunião e pesquisa prévia, aumentam bastante a qualidade do draft gerado. Quanto mais rico o contexto anexado, menos o prompt depende de respostas improvisadas durante a entrevista. O instrutor reforçou que o valor está na densidade do contexto e na capacidade de transformar esse material em um documento mais próximo da realidade da empresa e da funcionalidade.

Também foi explicado o uso de um template reutilizável para fixar a estrutura esperada do HLD antes da geração. Esse template ajuda a manter consistência entre documentos, facilitar revisão humana e alinhar o resultado ao padrão interno do time. Em seguida, o instrutor mencionou o uso de defaults inteligentes, isto é, decisões assumidas pelo prompt quando faltam detalhes explícitos, para acelerar a produção inicial sem travar o processo.

Outro ponto abordado foi o uso de JSON como formato operacional para tornar o HLD mais previsível e manipulável por ferramentas. A checagem de consistência aparece como etapa importante para evitar contradições internas entre as partes do documento, por exemplo quando a arquitetura sugere uma centralização, mas os riscos e as preocupações de escalabilidade não refletem essa escolha. O fluxo recomendado foi: reunir insumos, executar a entrevista guiada, gerar o draft no template escolhido, validar consistência e revisar manualmente.

Por fim, o instrutor enfatizou que o prompt deve ser adaptado ao fluxo de trabalho real do time e ao nível de documentação já existente. Em alguns casos, o ponto de partida será a entrevista; em outros, será um PRD já pronto e uma pesquisa técnica complementar. A ideia é reduzir a fricção de começar do zero sem abrir mão do raciocínio arquitetural, gerando um documento inicial mais mastigado e fácil de evoluir.

**Pontos de atenção**
- O prompt de HLD não substitui o trabalho de arquitetura; ele apenas organiza a coleta de contexto e acelera o rascunho.
- Documentos gerados por IA tendem a ser mais úteis quando recebem contexto rico e específico da empresa e da funcionalidade.
- Não confiar apenas em respostas da entrevista: anexar PRD, pesquisas técnicas e notas de reunião melhora muito o resultado.
- O template é essencial para evitar texto solto, inconsistência de estrutura e variações indevidas entre execuções.
- Defaults inteligentes ajudam a destravar a geração, mas sempre precisam de revisão, pois suposições podem estar erradas.
- Checar consistência antes de finalizar é obrigatório para evitar contradições entre arquitetura, fluxo, riscos e escalabilidade.
- JSON é útil para padronização e integração com ferramentas, mas não elimina a necessidade de leitura e validação humana.
- O prompt deve ser ajustado ao workflow do time; não existe uma única versão ideal para todos os contextos.
- O objetivo final é produzir um draft inicial revisável, não um documento final perfeito e pronto sem intervenção.
- Em documentos específicos da empresa, a revisão humana é indispensável para corrigir generalizações inadequadas e preencher pontos peculiares do domínio.