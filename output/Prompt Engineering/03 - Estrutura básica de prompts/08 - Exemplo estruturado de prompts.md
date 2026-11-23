Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16617)

## Resumo da aula

Um prompt estruturado organiza instruções em blocos explícitos, em vez de concentrar tudo em um texto corrido. Essa divisão reduz ambiguidade, facilita manutenção e torna o prompt reutilizável como artefato de trabalho. Em tarefas de desenvolvimento, o ganho principal não está em “falar mais”, mas em separar intenção, contexto e restrições de forma auditável.

Persona e escopo definem quem o modelo deve ser naquela tarefa e até onde ele pode ir. No exemplo de Node.js com Jest, dizer que o agente é especializado em Node.js e testes com Jest, além de proibir refatorações no código original, reduz improviso e evita mudanças fora da fronteira da tarefa. Essa seção funciona como um enquadramento operacional: ela orienta competência esperada e limita comportamento ao mesmo tempo.

O objetivo precisa descrever a tarefa de forma direta e específica. “Escreva testes para o código abaixo” é amplo demais; “escreva testes unitários para a função abaixo usando Jest, cobrindo entradas válidas e inválidas” já informa tipo de teste, ferramenta e cobertura mínima. A diferença prática é que o modelo deixa de inferir sozinho o que você quis dizer e passa a executar um pedido mais controlado.

A entrada deve conter apenas o necessário para resolver a tarefa e aparecer separada visualmente do restante do prompt. Retomando o cenário de geração de testes, a função alvo entra em um bloco próprio, sem misturar código com instruções de objetivo. Essa separação evita que o modelo confunda dado de entrada com regra de execução e ajuda a manter o prompt sistemático.

O formato de saída já foi discutido antes como mecanismo de previsibilidade; aqui ele vira uma seção explícita da estrutura. Exigir um objeto JSON com campos como testFile e coverageNotes reduz respostas fora do padrão e facilita integração com agentes ou outros programas. JSON não é obrigatório em todos os casos, mas formatos com regras claras diminuem variação e tornam a resposta mais processável.

Critérios de qualidade definem o que conta como uma resposta boa antes da execução começar. No exemplo, os testes precisam rodar com npm test sem ajustes, cobrir casos válidos e inválidos e não usar bibliotecas externas além de Jest. Sem essa seção, o modelo pode até cumprir a tarefa em aparência, mas falhar no que realmente importa para aceitação técnica.

Tratamento de ambiguidades especifica como o modelo deve agir quando faltar informação necessária. Se a versão do Node não estiver informada, o prompt pode mandar assumir Node 18 e registrar isso no campo assumptions. O valor dessa seção está em transformar inferências implícitas em pressupostos declarados, o que melhora revisão, rastreabilidade e confiança no resultado.

Instruções negativas listam explicitamente o que não pode aparecer ou acontecer na resposta. No exemplo, proibir explicações ou comentários fora do JSON impede que o modelo “enfeite” a saída e quebre o contrato esperado. Esse tipo de restrição é especialmente útil na camada de saída, onde pequenas variações já podem inviabilizar automação.

Tratamento de erro define como o modelo deve responder quando não conseguir cumprir a tarefa. Em vez de improvisar ou entregar algo parcialmente inválido, ele pode retornar um JSON com statusError e a explicação do problema. Isso transforma falha em resposta estruturada, o que é mais útil para depuração e para fluxos automatizados.

Um prompt completo para esse cenário combina, na mesma ordem, Persona and Scope, objetivo, entrada, formato de saída, critérios, ambiguidades, instruções negativas e tratamento de erro. Retomando o exemplo de testes em Node/Jest, a força da estrutura não está em prometer o “melhor prompt do mundo”, mas em tornar a intenção explícita e reaproveitável. Quando você pede apenas “gere o teste disso aqui”, a chance de sair fora do padrão aumenta; quando cada seção define papel, tarefa, dados, qualidade e exceções, o comportamento fica muito mais previsível.

Prompts estruturados dão trabalho para construir, mas esse custo inicial compra reutilização futura. Assim como testes e documentação acumulam valor no projeto, prompts bem organizados deixam de ser texto descartável e passam a compor uma base reaproveitável entre tarefas, agentes e programas. O ganho real está na intencionalidade persistente: você para de começar do zero e passa a evoluir um padrão.

## Transcrição

00:01

Bom, pessoal, e agora a gente começou a chegar finalmente, depois de eu ter passado um pouco esse overview, à forma de como você pode estruturar prompts mais elaborados. E uma coisa importante, normalmente, esses tipos de prompt não são executados em alta escala. Vai depender muito mesmo do que você vai querer.

00:25

Mas, normalmente, uma escala muito grande de milhões, centenas de milhares de requisições, normalmente, você não vai ter algo tão grande ou tão elaborado de uma forma, a não ser quando você tem uma especificidade muito grande. Às vezes, você acaba fazendo diversas chamadas para um modelo, com prompts menores, do que fazer ele ler uma quantidade enorme de tokens. Mas, nada é regra. Realmente, você só vai decidir isso na hora, no momento que você está com o problema na mão.

00:53

Mas, de uma forma ou de outra, é importante você entender como que você pode organizar a estrutura de um prompt. Então, por exemplo, aqui eu estou dando um exemplo bem simples, não estou dizendo que esse prompt vai ser o melhor prompt do mundo, não. Então, o primeiro ponto aqui é persona e escopo. Persona é o que é o papel dele, no que é a especialidade, qual é a role dele. Então, você vai definir quem é o modelo, ou seja, defina quem o modelo é e o que

01:22

ele não deve fazer, tá? O que não fazer. Outro ponto aí, isso ajuda a gente a reduzir improvisos e garante alinhamento técnico. Então, eu vou dar um exemplo que a gente tem aqui, tá? Deixa eu até aumentar um pouco o meu...

01:40

o meu ScaledRaw aqui, tá? Então, eu vou colocar assim ó, você é um assistente especializado em Node.js versão X e testes com Jest. Não faça refaturações no código original. Então, isso aqui

01:56

Eu já falei o que ele é, especialista, e eu já falei de cara o que ele não vai fazer. Somente de fazer isso vai fazer com que aquele nosso amigo do Code Review vai ficar um pouco mais feliz, porque vai ter menos coisa para ele revisar pelo fato da IA não sair mexendo em códigos que ele não devia, tá? Aí eu tenho uma outra sessão, que é o objetivo. Então, descreva de forma direta e sem ambiguidade o que precisa ser feito.

02:22

Então, se eu colocar o seguinte, escreva testes para o código abaixo. Isso aí é errado, porque é muito aberto, é muito ambíguo. Essa pergunta é extremamente vaga. Se eu colocar dessa forma aqui, escreva testes unitários para a função abaixo, usando o Jest, cobrindo casos de entradas válidos e inválidos.

02:46

Eu não estou dizendo que essa frase é a melhor frase do mundo para você pedir para um IA fazer testes unitários, mas a única coisa que eu estou querendo mostrar aqui para você é a diferença do que é algo muito generalista do que algo que acaba sendo um pouco mais direto ao ponto, tá?

03:09

Outro ponto importante, uma vez que a IA entende o que ela tem que fazer, o que você precisa definir claramente para ela é a entrada, ou seja, a entrada dos dados. Então, o que eu estou querendo dizer é o seguinte,

03:24

você vai listar somente o necessário para resolver a tarefa. Você vai manter uma separação visual e você vai evitar colar arquivos inteiros se só a parte que você precisa é realmente importante. Então, nesse caso aqui, o que eu coloquei? Eu escrevi função e coloquei aqui a função que eu quero que ela resolva os meus testes unitários.

03:51

Ou seja, eu estou ali separando, inclusive visualmente, os meus blocos do prompt para garantir que a IA não confunda partes do objetivo dela com a entrada que você está passando.

04:08

Se a entrada que você está passando está junto com o objetivo, passa esse teste, você cola o teste para cobrir isso aqui, aí ela misturou o objetivo dela, ela misturou com a função que ela tem que trabalhar, e aí as coisas começam a ficar menos sistemáticas, gerando ainda mais ambiguidade.

04:25

O outro ponto, que é o ponto mais crítico, na minha opinião, sempre, porque muitas vezes a gente sabe o que pedir para IA, mas a gente não sabe definir como a gente quer, principalmente em documentação. Então, você define ali o formato de saída. Por exemplo,

04:42

Defina o formato exato para minimizar riscos de resposta fora de padrão. Então, nesse caso aqui, eu forcei um pouco a barra e coloquei Responda apenas com um objeto JSON no formato, o testfile e o conteúdo do arquivo de teste.

04:58

E daí eu coloquei ali coverage notes e a breve descrição da cobertura que esse teste está fazendo. Então, o Wesley está pedindo para ela retornar um JSON, o conteúdo do teste dentro do JSON. Nesse caso, eu fiz para garantir

05:14

porque ela vai sair exatamente nesse formato. Precisa ser assim? Você precisa fazer a sua IA trabalhar com o JSON? Não! Apesar que quando você for trabalhar com agentes de IA e esses caras se comunicando, JSON ou qualquer formato que tenha uma clareza de regras sempre vai mitigar um monte de problemas, inclusive riscos de segurança, tá?

05:37

Bom, uma vez que eu defini o formato de saída, eu vou definir agora os critérios de qualidade. Ou seja, eu vou especificar para a IA o que define para mim uma resposta boa dela. Então, quais são esses critérios que eu estou passando aqui para ela? Critérios. O teste deve rodar com NPM test sem ajustes. Ele deve cobrir os casos de entrada válidos e inválidos.

06:03

não usar bibliotecas externas além do Jest. Então, aqui, eu já falei claramente aqui para ele como são os critérios que eu quero para ele conseguir realmente seguir para ele trabalhar com o que eu preciso, tá?

06:19

E, depois, a gente tem algo que é muito importante e que normalmente a gente deixa de fazer, que é o tratamento de ambiguidades ou assumptions, são pressupostos. Por exemplo, eu digo para ela ir a fazer caso ela não tenha a informação que eu estou partindo do princípio que ela tem. Por exemplo, se faltar a versão do Node, que você não consiga achar alguma coisa desse tipo, assuma que a versão é a versão do Node 18.

06:48

Liste todos os pressupostos feitos no campo Assumptions. Por que eu estou dizendo isso? Toda vez que a própria IA tiver dúvida e que ela teve que assumir algo para terminar a tarefa, eu quero que ela fale para mim, no final das contas, que ela fez essa tarefa,

07:11

Partindo do princípio que o Node é 18, que o Jest vai funcionar dessa forma, que quando ele rodou NPM test, todos os testes iriam ser corrigidos, e não somente aquele teste que eu estava trabalhando, assim e assim assado. Então, ela consegue informar para você o que ela assumiu na hora que ela estava atendendo os seus critérios de qualidade.

07:35

E depois, algo importante também, que são instruções negativas. Ou seja, você lista o que não pode aparecer em uma resposta. Por exemplo, não inclua explicações ou comentários fora do JSON. Então, você já está falando, cara, você não vai fazer isso.

07:56

Porque às vezes ela pode fazer, às vezes ela não pode fazer. Então você sempre vai colocar claramente o que ela não deve fazer na saída, principalmente. Ou seja, as instruções negativas normalmente são feitas para a saída. Esse é um ponto importante. E aqui é tratamento de erro. Então...

08:17

Toda vez que ela acredita que pode ter um erro, ou se ela tá fazendo algum tratamento adicional pra fazer aquilo funcionar, você vai fazer o seguinte, né? Olha, não consegui fazer funcionar, deu pau, deu errado, ou seja, já não conseguiu cumprir a tarefa, você explica pra ela como que ela pode retornar

08:36

se ela não foi possível de cumprir aquilo que a gente pediu. E daí, nesse caso, eu posso pedir para ela fazer um JSON statusError e a explicação do problema

08:49

do motivo pelo qual ela não conseguiu cumprir aqueles meus critérios de qualidade para rodar os meus testes. E aqui tem, então, um exemplo completo de como ficaria um prompt estruturado. Estou dizendo que esse prompt tem todas as explicações e todos os detalhes do mundo e que é o melhor prompt que você vai colocar e você vai resolver todos os seus testes automatizados?

09:15

Não estou dizendo, mas o que eu quero que você veja é que há uma estrutura clara por sessões e que ficam muito mais fáceis de aí a entender e de você também, até mesmo quando você for reaproveitar esse prompt para outras coisas. Então, você tem o Persona e Scope, você é um assistente especializado em Node.js versão 18, teste com o JS, não faça refatorações no código original.

09:39

O objetivo é gerar teses unitários para a função abaixo usando o Jest. A entrada está aqui, a função. O formato de saída é responda apenas com o objeto JSON nesse formato. Critérios. O teste deve rodar com npm test sem ajustes. Cobrir os casos. Não usar bibliotecas. Ambiguidade de pressupostos. Se faltar a versão do Node, assuma a versão 18 e adicione isso em Assumptions.

10:00

instruções negativas, inclua as explicações ou comentários fora do JSON, tratamento de erro, se der alguma coisa ruim, retorne para mim um JSON com erro e com a explicação porque aquilo não foi trabalhado. Então, se você perceber, galera,

10:17

Tem uma diferença muito grande de você realmente criar um prompt claro, estruturado e intencional para resolver problemas, do que você simplesmente vai lá e fala, olha, você copia um pedaço do código, gera o teste desse aqui, baseado em todos esses outros testes que eu tenho nesses arquivos. Cara...

10:39

A chance de não sair como você quer é grande. A chance de sair fora do padrão é grande. A chance, às vezes, de ela fazer testes que são inúteis pode ser grande. Então, você sempre pensando numa estrutura, independente de qual seja ela, você consegue ser intencional. Agora, aqui vai uma dica, tá, pessoal? Porque dá trabalho e leva tempo fazer esses prompts. E eu sei disso, porque eu faço um monte desses prompts.

11:07

Mas, novamente, da mesma forma que a gente trata o teste como um ativo no projeto ao longo dos anos, a documentação como um ativo no projeto ao longo dos anos, você vai começar a tratar os seus prompts como um ativo ao longo dos anos. E a parte mais interessante

11:26

é que os seus prompts vão poder ser reutilizados em diversos programas e que você não vai mais precisar partir do zero. Fechou? Então, é isso aí, galera. Ficou meio grande esse vídeo, mas eu queria passar esse tipo de estrutura somente para você ter uma ideia de como você pode fazer.

## Resumo IA

**Abreviações**
- **Node.js**: plataforma de execução de JavaScript no servidor.
- **Jest**: framework de testes para JavaScript.
- **JSON**: JavaScript Object Notation, formato de dados estruturado e legível.
- **NPM**: Node Package Manager, gerenciador de pacotes do ecossistema Node.js.
- **Code Review**: revisão de código feita por outra pessoa ou ferramenta.

**Resumo**
A aula apresentou como estruturar prompts mais elaborados de forma clara, modular e reutilizável, em vez de concentrar tudo em um texto corrido. O instrutor explicou que esse tipo de prompt não costuma ser usado em altíssima escala, mas pode ser muito útil quando há necessidade de especificidade, controle e previsibilidade, especialmente em tarefas de desenvolvimento de software.

O fluxo proposto começa pela definição de **persona e escopo**, indicando quem o modelo é naquela tarefa e o que ele não deve fazer. No exemplo dado, o assistente é especializado em Node.js e testes com Jest, com a restrição explícita de não refatorar o código original. Em seguida, vem o **objetivo**, que precisa ser direto e sem ambiguidades, como pedir testes unitários para uma função específica, cobrindo casos válidos e inválidos, em vez de apenas “gerar testes” de forma genérica.

Depois, a aula destacou a importância de separar a **entrada** em um bloco próprio, contendo apenas o necessário para a execução da tarefa, evitando misturar código com instruções. A seguir, o **formato de saída** é definido de maneira explícita, preferencialmente com regras rígidas como um JSON contendo campos como `testFile` e `coverageNotes`, o que facilita automação e integração com outros programas ou agentes. Na sequência, entram os **critérios de qualidade**, que especificam o que caracteriza uma boa resposta: por exemplo, os testes devem rodar com `npm test` sem ajustes, cobrir entradas válidas e inválidas e não usar bibliotecas externas além do Jest.

A aula também abordou o tratamento de **ambiguidades e pressupostos**, orientando o modelo a declarar o que assumiu quando faltarem informações, como a versão do Node.js, que poderia ser assumida como Node 18 e registrada em um campo `assumptions`. Em paralelo, foram apresentadas as **instruções negativas**, usadas para proibir explicitamente comportamentos indesejados, como incluir explicações fora do JSON. Por fim, foi explicado o **tratamento de erro**, para quando a tarefa não puder ser cumprida: nesse caso, o modelo deve retornar uma resposta estruturada, por exemplo um JSON com `statusError` e a explicação do problema.

O instrutor concluiu reforçando que um prompt estruturado não é necessariamente o “melhor prompt do mundo”, mas torna a intenção mais explícita, reduz ambiguidades, facilita revisão e aumenta a chance de respostas consistentes. Apesar de dar mais trabalho inicialmente, esse tipo de prompt passa a ser um ativo reutilizável, assim como testes e documentação, evitando começar do zero em cada nova tarefa.

**Pontos de atenção**
- Prompts muito genéricos aumentam a ambiguidade e a chance de respostas fora do padrão.
- A seção de **persona e escopo** deve limitar tanto o papel do modelo quanto o que ele não pode fazer.
- O **objetivo** precisa ser específico: “faça testes unitários com Jest cobrindo casos válidos e inválidos” é melhor do que “escreva testes”.
- A **entrada** deve ser separada visualmente e conter somente o necessário; não misturar código com instruções evita confusão.
- Definir um **formato de saída** rígido, como JSON, ajuda na previsibilidade e na automação.
- **Critérios de qualidade** devem ser explícitos antes da execução, para evitar respostas corretas “na aparência”, mas inválidas tecnicamente.
- Quando houver falta de informação, é importante registrar os **pressupostos** em vez de deixá-los implícitos.
- **Instruções negativas** são especialmente importantes na saída, para evitar comentários, explicações ou conteúdo fora do contrato esperado.
- O **tratamento de erro** deve ser estruturado; se a tarefa falhar, o modelo deve devolver uma resposta útil para depuração.
- Prompts estruturados exigem tempo de construção, mas devem ser tratados como **ativos reutilizáveis** ao longo do projeto.
- Em contextos de integração entre agentes e sistemas, formatos com regras claras reduzem erros e melhoram a processabilidade.