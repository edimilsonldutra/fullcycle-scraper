Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16613)

## Resumo da aula

Em desenvolvimento de software, contexto costuma valer mais do que economia de tokens. Código é um domínio altamente interdependente: uma mudança pequena pode depender de convenções locais, fluxo entre módulos e restrições implícitas do projeto. Por isso, reduzir contexto cedo demais aumenta a chance de a IA interpretar errado o problema ou propor alterações desconectadas do sistema real. O critério principal deixa de ser “usar menos tokens” e passa a ser “fornecer contexto suficiente para a tarefa”.

O custo de uso da IA não depende apenas de tokens; ele também depende do modelo de cobrança da ferramenta adotada. Em muitos ambientes, especialmente IDEs e assistentes integrados, o consumo percebido pelo desenvolvedor aparece como plano de uso, limite operacional ou assinatura mensal, e não como contagem explícita por token. Isso muda a decisão prática: em vez de otimizar cada prompt como se cada token fosse um gasto visível, faz mais sentido comparar previsibilidade de custo, produtividade e qualidade de resposta. A escolha correta é a que sustenta o workflow com menos surpresa operacional.

Ferramentas diferentes podem entregar resultados parecidos com estruturas de custo muito distintas. Um setup baseado em API pode ficar caro em uso intensivo, enquanto um plano fixo pode dar previsibilidade financeira mesmo sem ser barato em valor absoluto. Também existem opções com entrada gratuita ou limites generosos, úteis para experimentação e validação de fluxo antes de escalar investimento. A comparação relevante não é “qual ferramenta é melhor em abstrato”, mas “qual combinação de custo, limite e qualidade atende este time neste momento”.

Nem toda tarefa exige expor o codebase inteiro para a IA. O ponto central é entregar o contexto necessário para que ela resolva o problema com segurança, sem abrir escopo desnecessário. Isso inclui indicar onde começa a investigação, quais módulos importam, qual fluxo deve ser seguido e o que deve ser ignorado. Estruturar esse recorte melhora previsibilidade porque reduz liberdade de navegação e interpretação.

Pensar o codebase como árvore ajuda a orientar a IA por ramificações em vez de despejar todos os arquivos de uma vez. Branches representam caminhos ou agrupamentos de componentes; leafs representam pontos mais terminais, onde a implementação concreta costuma estar. Quando a tarefa é localizada, a instrução pode mandar a IA seguir apenas uma ramificação específica até os leafs relevantes. Esse raciocínio restringe busca, reduz ruído e evita que o modelo contamine a solução com partes irrelevantes do sistema.

Retomando a ideia já conhecida de que o caso de uso determina a estrutura, em desenvolvimento isso se traduz em modularizar também o contexto fornecido à IA. Uma aplicação com componentes suficientemente desacoplados permite isolar um pedaço do sistema e trabalhar nele sem exigir compreensão global do projeto inteiro. Esse isolamento não serve apenas para arquitetura; ele vira mecanismo de prompting. Quanto melhor o módulo delimita responsabilidades, mais fácil fica instruir a IA a permanecer naquela bolha.

Quando cada parte do sistema possui documentação e instruções próprias, a IA consegue operar com menos ambiguidade dentro do recorte escolhido. Essas instruções podem registrar fluxo esperado, limites do módulo, convenções e pontos de integração permitidos. O efeito prático é impedir que o modelo “escape” para outras áreas do sistema sem necessidade. Em vez de depender de um prompt central gigantesco para tudo, você distribui contexto útil ao longo da estrutura do projeto.

A previsibilidade em desenvolvimento não vem apenas de escrever prompts claros; ela depende de organizar o sistema e o contexto de forma que a IA saiba por onde começar, até onde ir e o que ignorar. Lembra da preocupação anterior com controle de escopo? Aqui ela ganha uma camada operacional: além de limitar comportamento, você limita a superfície de leitura do codebase. Um prompt previsível, nesse cenário, combina contexto suficiente com fronteiras explícitas de navegação. Isso reduz respostas dispersas e melhora a aderência ao fluxo real de engenharia.

Ao pedir uma alteração, indique o módulo de entrada, a ramificação relevante e o fluxo que deve ser seguido até os arquivos terminais. Se o sistema for modular, anexe apenas a documentação local e as instruções daquele trecho, deixando explícito que o restante deve ser ignorado. Depois, peça a saída no formato adequado ao workflow já definido anteriormente, mantendo escopo e revisão controláveis. A combinação entre contexto suficiente e recorte estrutural é o que torna o uso da IA viável em codebases grandes.

## Transcrição

00:01

Bom pessoal, agora que eu acho que a gente está na mesma página e eu acho que deu para a gente dar uma contextualizada da importância que é você ter uma estrutura clara ali de prompt, eu quero agora chegar e ir um pouco mais para essas estruturações. Então é o seguinte, a gente tem alguns casos importantes.

00:22

Quando o problema não será respondido pela IA em larga escala, não economize em tokens?" Essa é uma pergunta muito comum que acontece. Quando eu começo a desenvolver e eu coloco um prompt gigante lá, a primeira coisa que algumas pessoas torcem o nariz para mim, pelo meu comportamento, é o seguinte.

00:47

Meu, e a janela de contexto? E a quantidade de tokens? Não vai dar certo isso que você está fazendo. E o que eu tenho percebido, pessoal, e novamente eu não sou o rei da verdade, é que quando a gente vai trabalhar com código e desenvolvimento, se a gente economizar em tokens, e codificação é algo extremamente complexo, então se a gente

01:13

não economizar, a gente tem uma chance maior de diminuir o problema. E o grande ponto é que, muitas vezes, você pode usar um prompt gigante para resolver um problema pequeno. Então, você não vai ter problemas em janela de contexto. Coisas interessantes, por exemplo, é se você pegar

01:31

um Gemini da vida com mais de 1 milhão de prompts, de prompts não, de janela de contexto, chega a 2 milhões, você pegar um GPT-5 da vida, ele tem, eu acho que perto de 500 mil tokens, mas ele tem algo fantástico, que é 128 mil tokens de saída em alta performance.

01:49

Então, a primeira coisa que você não deve ficar preocupado é, no momento que você for desenvolver software, você ficar economizando tokens. Principalmente porque, hoje em dia, grande parte dos planos, das IDEs e etc., eles não estão mais cobrando necessariamente por tokens. Normalmente, eles estão cobrando por utilização. É óbvio que, por trás dos planos,

02:19

eles devem estar fazendo as contas por token, mas não é como era antes, que você passava a sua API Key e cada token contava e saía uma conta muito clara. Vou dar um exemplo para você, e esse exemplo está acontecendo no momento dessa gravação, provavelmente daqui a um ano, daqui a seis meses, ou alguma coisa desse tipo, isso aqui pode estar em um formato completamente diferente. Mas, por exemplo, se eu pegar uma API Key da Antropic,

02:48

e colocar isso no Cloud Code, eu vou gastar uma grana absurda para passar o dia inteiro desenvolvendo, tá? Agora, se eu assinar o plano do Cloud Code, eu acho que é Max, sei lá como é o nome do plano, custa 100 dólares por mês, ou seja, não é um valor também tão barato. Eu hoje consigo trabalhar quase que de forma ilimitada com esse modelo, sem ter surpresas no final do mês.

03:13

E, além disso, em alguns momentos eu posso utilizar modelos de reasoning, sei lá, o Opus, por exemplo, que consegue, inclusive, ter resultados melhores, mas daí ele gasta mais ali a sua possibilidade de trabalhar com ele. Mas daí vai depender da empresa o quanto você quer gastar dinheiro no seu bolso, porque existem planos, sei lá, de 200 dólares por mês, que você acaba utilizando ele quase de forma ilimitada.

03:42

Ah, pessoal, a minha questão aqui não é falar de dinheiro e não é falar que 100 dólares é barato, tá? 100 dólares é bastante dinheiro, mas, tá? Pra mim, tá? 100 dólares perto da produtividade que eu tenho, por exemplo, se eu for usar o cloud,

03:58

Assim, ele se paga muito rápido. E eu espero que, ao longo do tempo, cada vez mais as empresas possam fornecer ferramentas de IA inclusas aí no pacote. E um ponto inicial que poderia acontecer, e são testes que, por exemplo, hoje eu estou fazendo na empresa, porque a gente tem desenvolvedores, é o seguinte.

04:23

Eu comecei a fazer comparação, por exemplo, do Gemini, CLI, Command Line Interface do Gemini, tá? E com o resultado com o Cloud Code, com o GPT-5, com os Anu Codecs e tudo mais. E o que eu acabei percebendo é que os resultados, por exemplo, que o Gemini tem me retornado, eles são muito similares ao que o Cloud. A única coisa é que o Gemini, pelo menos nesse momento, não tem tantos recursos

04:51

no CLI, mas o resultado final está sendo quase que o mesmo. E, pelo menos, nesse momento que eu estou gravando, o que acontece? O Gemini está ali, basicamente, prometendo que você faça, eu acredito, 1.000 requests por dia e 60 requests por minuto. Para você conseguir fazer isso,

05:16

É muita coisa, tá? É muita coisa. E essa possibilidade é gratuita, pelo menos por enquanto. Então, muitas vezes, para colocar o pé na água, você não precisa gastar um centavo, tá?

05:31

para trabalhar com inteligência artificial, porque, por exemplo, o Google ou o Gemini, pelo menos no momento dessa gravação, você tem um plano que você acaba não pagando nada, usando um limite absurdo. Pode ser que no futuro eles cobrem e tirem esses planos? Podem ser. Mas eu acredito que sempre vale a pena a gente manter a mente aberta e ver

05:53

quais são as soluções mais baratas que conseguem resultados similares. Às vezes, o resultado não é tão bom, mas é um resultado que, no final do dia, vai fazer eu economizar dinheiro ou a empresa economizar dinheiro também. Então, são coisas que eu quero que você acabe pensando, tá? Mas, para resumir, o que eu queria trazer aqui para vocês é

06:14

Toda vez que você for trabalhar para desenvolvimento com o IA, não economize em tokens. O que você pode ter são estratégias que vão fazer com que a IA não precise ler o seu codebase inteiro com 100 mil arquivos. Você consegue dar instruções mais claras para que ela consiga trabalhar com branches e leafs, ou seja, eu tenho um projeto

06:41

e esse projeto começa aqui, e daí ele tem uma ramificação de componentes, que são componentes que vão para cá, daí ele tem componentes que vão para cá, então ele vai gerando quase que fosse uma árvore, esse componente se quebra para cá, legal, esse componente se quebra para cá, bacana, esse cara aqui se quebra para cá,

07:12

Legal? E aí, no final das contas, quando eu peço para ir a resolver algum problema, eu chego e falo o seguinte, olha, eu quero que você resolva os meus problemas, os meus componentes, mas eu quero que você parta a partir desse princípio, seguindo esse fluxo aqui.

07:32

Todo o restante você ignora e você consegue mapear. Mas tudo isso depende muito de como você estrutura a sua aplicação. Se a sua aplicação trabalha de uma forma bem modular, os componentes estão desacoplados o suficiente, você consegue, sim, fazer com que a IA entenda o contexto desse pedaço sem ter que internalizar toda essa outra parte. E, nesses casos, você pode, por exemplo, criar documentações e instruções em cada pedaço para que ela evite

08:02

sair e entrar em outra bolha de partes do seu sistema. Então, são coisas que você pode fazer. O ponto importante aqui é que, independente de qualquer coisa, eu não quero que você economize com tokens para você explorar, para você gerar documento, para você processar informação, principalmente em um workflow de desenvolvimento, tá? Agora, no próximo vídeo, a gente vai falar do outro lado da moeda e esse outro lado realmente é muito importante. Então, vamos nessa.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **CLI** — *Command Line Interface* (Interface de Linha de Comando)
- **IDE** — *Integrated Development Environment* (Ambiente de Desenvolvimento Integrado)
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **API Key** — chave de acesso à API

**Resumo**
A aula explica que, em desenvolvimento de software, o mais importante não é economizar tokens a todo custo, mas sim fornecer contexto suficiente para que a IA compreenda corretamente o problema. Como código é um domínio altamente interdependente, reduzir demais o contexto pode levar a interpretações erradas e soluções desconectadas da realidade do sistema. O instrutor destaca que, em muitos cenários, vale mais a pena enviar um prompt mais completo do que tentar ser excessivamente econômico.

Também é abordada a questão de custo no uso de ferramentas de IA. O instrutor observa que o modelo de cobrança varia bastante entre soluções: algumas cobram por uso ou por API, enquanto outras oferecem assinatura mensal com uso mais previsível. Ele compara ferramentas como Cloud Code, Gemini CLI, GPT-5 e modelos de reasoning, mostrando que a decisão prática depende de custo, limite de uso, previsibilidade e produtividade, e não apenas do preço nominal.

Outro ponto central é que nem toda tarefa exige expor o codebase inteiro para a IA. A orientação é delimitar o escopo com clareza, indicando por onde ela deve começar, quais módulos deve seguir e o que deve ignorar. O instrutor usa a ideia de árvore para representar o projeto, com branches e leafs, defendendo que a IA percorra apenas a ramificação relevante até os arquivos terminais necessários para a tarefa.

A aula também reforça que a organização arquitetural da aplicação influencia diretamente a qualidade do uso da IA. Sistemas modulares e desacoplados permitem isolar contextos menores, o que facilita o prompting e reduz ambiguidade. Quando cada parte do sistema tem sua própria documentação e instruções, a IA consegue atuar dentro de uma “bolha” bem definida, sem se perder em partes irrelevantes do projeto. No fluxo sugerido, ao solicitar uma alteração, deve-se informar o módulo de entrada, a ramificação relevante, o fluxo a ser seguido e anexar apenas a documentação local pertinente, mantendo o restante do sistema fora do contexto.

**Pontos de atenção**
- Não otimizar prompts apenas para reduzir tokens em tarefas de desenvolvimento; contexto insuficiente pode piorar a resposta.
- Em código, pequenas mudanças podem depender de convenções locais, módulos relacionados e restrições implícitas do projeto.
- O custo de uso de IA varia conforme a ferramenta: API com cobrança por uso pode sair cara em uso intensivo, enquanto planos fixos oferecem mais previsibilidade.
- Comparar ferramentas pela combinação de custo, limite de uso, qualidade e produtividade é mais útil do que comparar apenas “qual é melhor”.
- Nem sempre é necessário enviar o codebase inteiro; o ideal é recortar o contexto necessário para a tarefa.
- Estruturar o projeto como árvore ajuda a guiar a IA por branches relevantes até os leafs corretos.
- Sistemas mais modulares e desacoplados são mais fáceis de usar com IA, pois reduzem a necessidade de contexto global.
- Documentações e instruções por módulo ajudam a evitar que a IA “escape” para outras áreas do sistema.
- Ao pedir uma alteração, explicite módulo de entrada, fluxo esperado e o que deve ser ignorado.
- Manter fronteiras explícitas de navegação melhora previsibilidade, reduz ruído e aumenta a aderência da IA ao fluxo real de engenharia.