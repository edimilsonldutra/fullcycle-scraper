Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16572)

## Resumo da aula

Em aplicações de chat, o papel vira implementação por meio da estrutura de mensagens. system carrega as instruções de mais alto nível, user representa a solicitação do usuário e assistant corresponde à resposta gerada pelo modelo. Retomando o role prompting já definido anteriormente, a novidade aqui é que ele deixa de ser uma ideia abstrata e passa a ser uma mensagem concreta dentro do array enviado ao modelo. Isso importa porque o comportamento observado depende não só do texto do prompt, mas também de onde essa instrução foi colocada.

A comparação mais útil é manter o user prompt fixo e variar apenas o system prompt. Um system pode instruir o modelo a agir como professor universitário de ciência da computação, com explicações conceituais, definições formais e pseudocódigo; outro pode pedir o comportamento de um estudante de high school, com linguagem simples e exemplos. Essa montagem isola a variável “papel” e permite observar com clareza o efeito da role sobre estilo, vocabulário e tipo de explicação. Se várias partes mudarem ao mesmo tempo, a comparação perde valor diagnóstico.

No LangChain, a composição do prompt pode ser feita criando duas estruturas de chat: uma com system + user para o primeiro papel e outra com system + user para o segundo. Cada ChatPrompt representa uma versão controlada da mesma interação, pronta para ser formatada em mensagens antes da invocação do modelo. Essa separação é útil porque evita concatenar strings manualmente e torna explícita a hierarquia entre instrução de sistema e solicitação do usuário. Como alternativa, seria possível montar a lista de mensagens diretamente, mas o ChatPrompt melhora legibilidade e reutilização.

Uma função como printLlmResult não altera o comportamento do modelo, mas melhora muito a inspeção do experimento. Ela exibe o prompt enviado e a resposta recebida de forma organizada, inclusive com destaque visual, o que facilita comparar execuções lado a lado. Em prompt engineering, esse tipo de utilitário reduz atrito de análise e ajuda a detectar rapidamente se a diferença observada veio do papel, do modelo ou de algum erro na montagem das mensagens. É uma forma simples de observabilidade local antes de usar ferramentas mais completas.

Depois de formatar as mensagens, a chamada ao modelo ocorre por invocação direta, passando a estrutura resultante para o chat model configurado. O ponto central não é o nome exato do modelo, mas o fato de que ele recebe uma sequência de mensagens com papéis distintos, e não um bloco único de texto sem estrutura. Isso afeta como a instrução é interpretada e torna o experimento mais próximo do padrão usado em aplicações reais. Trocar o modelo mantendo as mesmas mensagens também permite comparar sensibilidade a role prompting entre modelos diferentes.

Quando a pergunta “explique recursão em 50 palavras” é enviada com o papel de professor universitário, a resposta tende a usar termos mais formais, como caso base, casos recursivos e terminação. Quando a mesma pergunta é enviada com o papel de estudante de high school, a resposta migra para linguagem mais simples e exemplos concretos, como a metáfora do espelho refletindo outro espelho. O conteúdo central continua sendo recursão, mas o enquadramento muda: vocabulário, densidade técnica e estratégia pedagógica passam a refletir o papel definido. Esse é o efeito prático que justifica usar role prompting quando estilo e postura importam.

Escrever apenas “você é um engenheiro de software” costuma produzir um efeito mais fraco do que especificar domínio, estilo e forma de resposta. Um papel mais operacional descreve também especialidade, linguagem, nível técnico, formato de explicação e critérios de comunicação. Isso torna a role menos decorativa e mais executável pelo modelo, porque reduz ambiguidade sobre como responder. A diferença entre “engenheiro de software” e “engenheiro de software que programa em determinada linguagem e explica tecnicamente” é justamente a diferença entre rótulo e instrução utilizável.

O experimento também pode registrar tokens de entrada, tokens de saída e total consumido em cada chamada. Como o custo de tokens já foi discutido anteriormente, o ponto novo aqui é usar essa medição para comparar o impacto de duas instruções de papel diferentes sobre a mesma tarefa. Mesmo quando a pergunta do usuário é idêntica, o system prompt altera o volume de contexto enviado e pode influenciar o tamanho e o estilo da resposta. Medir tokens junto com qualidade evita avaliar role prompting apenas por impressão subjetiva.

Embora seja comum colocar o papel no system prompt, role prompting não está limitado a essa posição. Um usuário também pode introduzir uma instrução de papel no meio da interação e induzir o modelo a mudar de comportamento a partir daquele ponto. A diferença é que a posição da instrução afeta prioridade e estabilidade ao longo da conversa, então escolher entre system e user não é apenas detalhe sintático. Em implementações reais, essa decisão interfere em previsibilidade e controle.

O mesmo conjunto de mensagens pode produzir respostas diferentes em modelos distintos, mesmo quando a técnica aplicada é a mesma. Alguns modelos seguem o papel com mais consistência; outros suavizam a diferença entre os dois system prompts e entregam respostas mais parecidas. Por isso, a unidade de teste não é só o prompt isolado, mas a combinação entre modelo, estrutura de mensagens e objetivo da tarefa. Role prompting deve ser validado empiricamente na stack que será usada em produção.

## Transcrição

00:01

Bom pessoal, eu falei no vídeo anterior sobre o role prompting, então vamos direto aqui pra tela da minha IDE pra gente entender melhor como é que esse cara funciona, tá? Somente pra você ter uma ideia, os exemplos que eu vou mostrar aqui de código, principalmente nessa parte onde eu vou mostrar os tipos de prompt,

00:20

Eu estou usando o LangChain, da forma mais simples possível. Uma das coisas que eu fiz, você vai ter acesso a esse repositório de qualquer forma, mas uma das coisas que eu fiz aqui foi o seguinte, eu criei um arquivinho bem bobinho aqui chamado printllmresult, onde eu tenho o prompt e eu tenho a response. Por que eu estou dizendo isso? Porque eu quero, toda hora que eu

00:44

pedir e retornar e IA pra mim, eu quero que ela responda coloridinha, eu quero poder ver o prompt que eu coloquei e a resposta dela embaixo, fica melhor pra gente visualizar os resultados, tá? Então, o negócio é o seguinte, pessoal. Eu tenho aqui dois prompts um pouco diferentes.

00:59

Eu tenho um system prompt, ou seja, é o prompt inicial de instruções iniciais que a IA vai receber, ou seja, é a instrução antes de iniciar a comunicação com o usuário final. Então, normalmente, a gente tem system, a gente tem user, e a gente tem assistant, que é o assistente que vai responder o usuário, e o system prompt é o prompt inicial que acaba colocando.

01:24

Então, eu criei um prompt do tipo system aqui, e eu coloquei assim para ele, olha, você é um professor universitário de ciência da computação, que é extremamente técnico e explica as coisas de forma conceitual, com definições formais e pseudocódicos. Ou seja, eu acabei de colocar, cara, você é um cientista, você é técnico para caramba, e você responde isso de uma forma extremamente técnica para a gente.

01:53

Então, eu tenho esse primeiro prompt. O segundo prompt que eu criei aqui foi o seguinte. Você é um aluno que está fazendo high school, você está no colegial e está começando a aprender a programar. Você não é muito técnico e você prefere explicar os conceitos de uma forma simples, com palavras simples e com exemplos. Beleza? Então, eu tenho dois system prompts aqui para mim.

02:19

E aqui eu tenho um user prompt, ou seja, aqui é a interação que o usuário vai fazer ali com a IA. E esse user prompt, o que ele está falando é o seguinte, ó, explique recursão em 50 palavras, ou seja, recursão, quando uma função chama a outra, né? Se é desenvolvedor, acho que a gente está na mesma página. Então, o que eu fiz aqui?

02:36

Eu criei um ChatPrompt 1, onde eu tenho o sistema e eu tenho o usuário, e eu criei um ChatPrompt 2, onde eu tenho o sistema, o Prompt 2 e o usuário. E eu criei aqui para ele formatar as minhas mensagens quando eu for trabalhar aqui no meu ChatPrompt 1, e eu posso ter as mensagens também do meu ChatPrompt 2, caso eu queira trabalhar.

03:01

Quem que eu fiz aqui também? Estou instanciando um modelo, peguei o GPT-4 ou... A gente já tem GPT-5 e dependendo da época que você está assistindo esse vídeo, a gente pode ter GPT-10. Mas o ponto aqui é entender essas principais diferenças. Então, se você perceber aqui, o que eu estou fazendo aqui? Eu peguei o meu modelo, tá?

03:23

E o meu resultado é, eu estou invocando, eu estou chamando, nesse caso, passando essas mensagens para o meu modelo, para o meu GPT aqui, e aqui eu estou usando aquela minha função que deixa as coisas coloridinhas ali para a gente. Então, é basicamente isso que está acontecendo.

03:43

O que eu vou fazer? Eu vou executar agora esse script e a gente vai ver a diferença, tá? O que um usuário fez a mesma pergunta para dois System Prompts diferentes e esses System Prompts, no final das contas, a gente está utilizando aqui um Role Prompt. A gente está dando um papel específico para esse cara aqui e um pouquinho de comportamento. Então, eu vou rodar aqui e vou fazer o seguinte. Então, eu vou colocar aqui Python.

04:06

Eu acho que tem uma pasta 1 e exemplo 0, role prompting aqui pra gente. Então, vou dar um Enter e vamos botar esse cara pra rodar pra gente ver como é que ele retorna os resultados aqui pra mim. Então, seguinte...

04:21

A gente tem duas chamadas. A primeira chamada é que o cara é o professor universitário que a gente falou. E a segunda chamada que a gente tem aqui... A segunda chamada é, na realidade, a resposta do nosso modelo. Ou seja, a gente acabou de explicar o que é recursão em 50 palavras e ele está respondendo aqui.

04:43

Recursão é uma técnica de programação onde uma função chama ela mesma para resolver problemas. Isso consiste de uma base de casos recursivos garantindo uma terminação eventual.

04:58

Cara, ele tá escrevendo de uma forma bem fancy aí o que é recursão de uma forma bem técnica, tá? Naquele meu script eu tô trazendo aqui também pra vocês quantos tokens de entrada e quantos tokens de saída, depois a gente vai falar um pouco mais disso, com o total de tokens que foram gastados, né, gastos pra trabalhar aí com esse prompt, né, dessa chamada aqui pra gente.

05:19

E aqui a gente tem o user prompt mais simples, que é o menino da high school, ou seja, ele está aprendendo a estudar. E aí, olha a resposta que a IA deu aqui. Recursão é uma técnica de codificação, onde uma função chama ela mesma, com partes de uma parte maior, e aí você começa a perceber

05:41

linguagem de alguém de high school, né? Por exemplo, quando, em inglês, né, se alguém começa a falar algo pra você, it's like, it's like, tipo, é tipo assim, né? Bom, se você fala inglês, ou mesmo se você não fala inglês, quando a gente usa, quando a gente fala, oh, it's like something, né? Significa, isso é tipo assim, quando a gente fala em português, né? E aqui ele tá dando um exemplo, é como se você tiver olhando

06:06

refletindo no espelho, mostrando isso repetidamente até você ver uma parte que você não consegue ver mais. Então, é uma forma de ensinar recursão. Ou seja, ele está dando um exemplo de um espelho, olhando para o próprio espelho e fazendo isso de forma recursiva. Então, se você perceber, mudou completamente a forma e o exemplo de como se trabalha. Então, o System Prompt realmente muda muito o comportamento,

06:34

E, sim, falar qual é o papel daquelas instruções é importante, mas, na minha opinião, não é só o papel, porque muita gente confunde papel com engenheiro de software. Engenheiro de software é um papel, é uma role, mas um engenheiro de software que programa em tal linguagem e normalmente explica, tecnicamente, porque ele é muito bom, também é um papel.

07:01

Então, entenda que quando você está falando de role prompting, você não está falando, você é um cozinheiro. Não, você é um cozinheiro especialista em fazer steaks americanos, bem apimentados, onde as maiores lojas

07:16

os maiores restaurantes usam essa técnica. Então, você já muda completamente o papel. Então, o role prompt vai mostrar o papel da IA naquele caso. Agora, um ponto importante aqui para você se ligar é o seguinte, não é porque...

07:33

não significa que é porque é um role prompt que ele vai ser um system prompt, tá? Nesse caso, é. Mas eu posso, às vezes, ter uma instrução de sistema e eu, como usuário, fazer um role prompt para, a partir dali, ele começar a se comportar de uma outra forma, tá? Então, não necessariamente o role prompting tem que ser no sistema. Normalmente, ele é, mas ele não tem que ser ali no sistema. Beleza? Então, esse é o nosso primeiro exemplo aqui

08:02

E eu espero que tenha ficado um pouco mais claro para você como é essa história de role prompting, somente para você não sair sentindo muitas vezes meio inocente de... Você é um engenheiro de software, resolva esse bug para mim. E achar que somente escrever engenheiro de software vai mudar muita coisa no resultado da sua aplicação. Fechou? Então, no próximo vídeo, a gente vai para o nosso próximo exemplo.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **IDE** — Ambiente de Desenvolvimento Integrado
- **GPT** — Generative Pre-trained Transformer
- **LLM** — Large Language Model
- **high school** — ensino médio/colegial

**Resumo**
A aula explicou como o role prompting funciona em aplicações de chat, mostrando que o papel atribuído ao modelo deixa de ser uma ideia abstrata e passa a existir concretamente como mensagem na estrutura enviada ao modelo. O instrutor destacou os papéis básicos de uma conversa — **system**, **user** e **assistant** — e enfatizou que a posição da instrução altera o comportamento observado, já que o modelo interpreta não apenas o texto, mas também a hierarquia das mensagens.

Para demonstrar isso, foram criados dois **system prompts** com estilos bem diferentes, mantendo o mesmo **user prompt**: um orientava o modelo a agir como um professor universitário de ciência da computação, com linguagem técnica, definições formais e pseudocódigo; o outro o fazia agir como um estudante de high school, com explicações simples e exemplos. A intenção foi isolar a variável “papel” para observar claramente como o estilo, o vocabulário e a forma de explicar mudam quando apenas o system prompt é alterado.

Na implementação, o instrutor utilizou o **LangChain** de forma simples, montando dois **ChatPrompts**: um com system + user para o primeiro papel e outro com system + user para o segundo. Em seguida, as mensagens formatadas foram enviadas ao modelo por invocação direta. Foi citada também uma função utilitária, como **printLlmResult**, para exibir o prompt e a resposta de modo organizado, facilitando a comparação visual entre as execuções e a análise do experimento.

O exemplo prático usou a pergunta “explique recursão em 50 palavras”. Com o papel de professor universitário, a resposta veio mais formal e técnica, citando conceitos como caso base, casos recursivos e terminação. Com o papel de estudante, o modelo respondeu com linguagem mais simples e exemplos concretos, como a metáfora do espelho. O instrutor também comentou a medição de tokens de entrada, saída e total, para comparar não só a qualidade da resposta, mas também o custo de cada variação.

Por fim, a aula reforçou que role prompting não se resume a dizer “você é um engenheiro de software”: um papel eficaz precisa incluir domínio, nível técnico, estilo de comunicação e formato de resposta. Também foi destacado que o role prompt não precisa obrigatoriamente estar no system prompt, embora essa seja a posição mais comum; ele pode aparecer em outras partes da conversa, influenciando o comportamento a partir daquele ponto. O instrutor concluiu que o efeito do role prompting deve ser validado empiricamente, pois diferentes modelos podem reagir de formas distintas às mesmas mensagens.

**Pontos de atenção**
- Manter o **user prompt fixo** é essencial para isolar o efeito do **system prompt**; se várias variáveis mudarem ao mesmo tempo, a comparação perde valor.
- O **papel** não deve ser descrito de forma genérica demais; quanto mais operacional for a instrução, maior a chance de o modelo seguir o comportamento esperado.
- A posição da instrução importa: usar **system** tende a dar mais prioridade e estabilidade, mas instruções de papel também podem aparecer no **user** em certos fluxos.
- Não assumir que “escrever um cargo” já é suficiente; “engenheiro de software” sozinho é fraco se não vier acompanhado de estilo, profundidade técnica e formato esperado.
- Comparar apenas pela impressão subjetiva pode enganar; é importante observar também **tokens de entrada, saída e total** para avaliar custo e impacto da instrução.
- O mesmo conjunto de mensagens pode produzir resultados diferentes em modelos distintos; por isso, os testes devem ser feitos no modelo que será usado em produção.
- Usar utilitários como **printLlmResult** ajuda na observabilidade local e facilita identificar se a diferença veio do papel, do modelo ou de erro na montagem das mensagens.
- Preferir estruturas como **ChatPrompt** melhora legibilidade e reutilização em vez de concatenar strings manualmente.