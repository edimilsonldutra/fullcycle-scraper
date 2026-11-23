Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16597)

## Resumo da aula

Janela de contexto é a quantidade máxima de conversa, documento ou código que o modelo consegue considerar de uma vez para gerar a próxima resposta. Retomando a restrição já conhecida de tokens, o ponto novo aqui é tratá-la como limite concreto de projeto: tudo o que entra na chamada compete pelo mesmo espaço. Mensagem de sistema, mensagem do usuário, respostas anteriores e trechos adicionais de dados ocupam a mesma janela. Quando esse espaço é excedido, parte da informação deixa de ser considerada, e a aplicação passa a operar com perda de contexto.

A janela não contém apenas o prompt principal; ela inclui todo o conteúdo enviado naquela interação. Em uma conversa, isso significa instruções, histórico e a nova pergunta; em um fluxo com documentos, significa também os trechos recuperados; em código, entram arquivos, funções ou partes relevantes anexadas à solicitação. Esse detalhe muda o desenho do sistema porque o limite real não é o tamanho de uma única mensagem, mas a soma de tudo o que precisa caber junto. Quanto mais componentes a aplicação injeta no prompt, menos espaço sobra para o restante.

Ultrapassar a janela de contexto não é apenas um problema de tamanho; é um problema de decisão sobre o que o modelo consegue usar. Se a conversa cresce demais, mensagens antigas podem ficar de fora; se um documento é grande demais, apenas uma parte dele cabe; se o código enviado é extenso, arquivos ou funções relevantes podem não entrar. O efeito prático é resposta menos consistente, porque o modelo passa a responder sem acesso a partes importantes do estado da interação. Por isso, o limite de contexto afeta diretamente a confiabilidade do comportamento do sistema.

A capacidade de contexto mudou bastante ao longo do tempo, e isso altera o tipo de problema que cada modelo consegue atender. Um exemplo citado é o GPT-3 com 2.048 tokens, contraste forte com modelos mais recentes que trabalham com janelas muito maiores, chegando a ordens de grandeza muito superiores. Essa evolução amplia o volume processável por chamada, mas não elimina a necessidade de engenharia de contexto. Janela maior reduz pressão em alguns cenários, porém não torna irrelevante a seleção do que deve entrar.

Uma janela de contexto maior não torna um modelo automaticamente melhor. A escolha correta depende do caso de uso, porque um modelo menor e mais barato pode ser suficiente quando a aplicação trabalha com interações curtas, contexto controlado ou execução local. Em sistemas reais, a decisão combina capacidade de contexto com restrições operacionais já conhecidas, como custo e latência. O critério útil não é “qual modelo é o mais poderoso”, mas “qual modelo atende o problema com o menor desperdício”.

A janela de contexto influencia a arquitetura porque obriga o sistema a decidir continuamente o que enviar ao modelo e o que deixar de fora. Retomando o cenário da aplicação com LLM, a camada nova aqui é o encaixe do contexto: quais mensagens da conversa, quais partes do documento e quais trechos de código realmente cabem na chamada atual. Essa decisão não é cosmética; ela define se o modelo terá insumos suficientes para responder corretamente. Projetar a aplicação sem considerar esse limite costuma gerar fluxos frágeis, especialmente quando o volume de informação cresce.

Prompt Engineering, nesse ponto, deixa de ser apenas escrita de instruções e passa a ser gerenciamento de espaço escasso. A estratégia precisa organizar o contexto para manter conversa e documentos dentro da janela disponível, preservando o que é mais relevante para a próxima resposta. Isso exige pensar em ordem, prioridade e volume do conteúdo enviado, em vez de simplesmente acumular informação no prompt. As técnicas específicas de controle desse contexto aparecem na sequência, mas a base é esta: cada token usado precisa justificar sua presença.

## Transcrição

00:01

Vamos nessa então, pessoal. Seguinte, janela de contexto e limite de tokens. Então, o que a gente precisa revisitar? O que a gente precisa entender claramente? A janela de contexto, toda vez que a gente falar em janela de contexto, eu vou estar falando sobre a quantidade máxima de mensagens na nossa conversa, documento ou código que o modelo consegue utilizar de uma vez para gerar a próxima resposta.

00:27

Então, basicamente, o que acontece aqui é que eu tenho um espaço, vamos dizer aqui, que o modelo consegue fazer o processamento das mensagens. Então, quando eu mando uma mensagem do sistema, uma mensagem do usuário, aí eu tenho a resposta do LLM, tudo isso aqui

00:47

A gente vai ter, no final das contas, os nossos tokens, que são palavras, ou pedaços de palavras, que é como que o LLM consegue entender para ele conseguir trabalhar e trazer as nossas respostas. O ponto é que, se a gente passa esse limite aqui, simplesmente a gente vai começar a perder a informação.

01:09

E por que isso é importante a gente entender? Porque, apesar de parecer algo óbvio, e muitas vezes a gente está pensando em prompt engineering, então o meu prompt não vai ter um tamanho, vamos dizer assim, tão grande para estourar uma janela de contexto,

01:25

É importante você entender porque isso vai mudar completamente a forma, inclusive, de como você pode vir a arquitetar uma aplicação ou quais estratégias de prompt você vai utilizar para poder realizar o processamento de diversas mensagens ao mesmo tempo. Então, somente para a gente ficar claro aqui, cada modelo tem ali o tamanho da sua janela

01:48

de contexto, context window, que é a palavra em inglês que você vai escutar por aí. Então, eu vou dar um exemplo para você ver, inclusive, como que isso foi mudando ao longo do tempo. Então, se você pegar o GPT-3, ele tinha 2.048 tokens, que era possível você falar, vamos dizer, interagir com o modelo, sem ele perder informação.

02:12

Acima disso, você já começava a perder dados, ou seja, 2048 tokens perto de 10 milhões de tokens, aí as coisas acabam mudando bastante. Então, você pode perceber que do GPT-3 para o 4.0, para o Cloud 4, para o GPT-4.1, o Gemini 2.5, independente do momento que você está assistindo esse vídeo, provavelmente, no momento que você assistiu, a gente pode ter outras versões, outros modelos

02:42

com uma janela maior ou uma janela menor, GPT-5, por exemplo, você vai perceber que cada vez a gente tem mais limite de tokens. Agora, um ponto importante que você tem que entender é que não é porque um modelo tem uma janela de contexto maior,

03:01

que ele é o melhor modelo, principalmente pelo fato de que, quando você for trabalhar no dia a dia, você não vai escolher necessariamente o melhor modelo. Você vai escolher o, entre aspas, melhor modelo para o seu caso de uso. Então, você pode trabalhar com modelos pequenos, modelos com uma janela de contexto bem pequena,

03:25

mas que seja muito barato, que você, às vezes, pode rodar local ou pode, sei lá, rodar com docker fazendo offload. Então, tem diversas opções, mas tendo clareza dessa janela de contexto, vai dar muito mais base e...

03:41

e uma flag que fica acendendo em você o tempo todo é, como que eu faço para dentro de tudo que eu vou trabalhar na minha aplicação, no meu agente, como que eu consigo trabalhar de uma forma que eu não ultrapasse essa janela de contexto, tá? E isso é importantíssimo para a parte de Prompt Engineering, porque tem técnicas e diversas técnicas para a gente conseguir manter uma conversa, documentos dentro dessa janela aí.

04:09

Legal? Então, isso aí é importantíssimo para que você consiga entender. No próximo vídeo, a gente vai falar um pouquinho mais sobre esse assunto, inclusive, como o LLM trata isso aí e por que isso acaba importando bastante para a gente entender um pouquinho por baixo dos panos. Vamos nessa!

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem Grande)
- **GPT** — *Generative Pre-trained Transformer*
- **GPU/CPU offload** — não foi citada explicitamente como sigla, mas aparece a ideia de executar parte do processamento fora do ambiente principal; “offload” significa descarregar/processar externamente
- **Docker** — plataforma de containers para empacotamento e execução de aplicações

**Resumo**
A aula apresentou o conceito de janela de contexto como o limite máximo de informação que um modelo consegue considerar de uma vez para gerar a próxima resposta. O instrutor destacou que essa janela não inclui apenas o prompt principal, mas a soma de tudo o que entra na chamada: mensagens de sistema, mensagens do usuário, respostas anteriores, documentos recuperados e trechos de código. Quando esse limite é excedido, parte do conteúdo deixa de ser considerada, o que provoca perda de contexto e reduz a consistência das respostas.

Foi explicado que a janela de contexto é uma restrição prática de arquitetura, não apenas um detalhe de prompt. Isso influencia diretamente como uma aplicação com LLM deve ser desenhada, porque o sistema precisa decidir continuamente o que enviar ao modelo e o que omitir. O instrutor usou o exemplo do GPT-3, com 2.048 tokens, para mostrar como os modelos evoluíram para janelas muito maiores em versões mais recentes, mas reforçou que ter mais contexto não significa automaticamente ter um modelo melhor.

Também foi ressaltado que a escolha do modelo deve considerar o caso de uso, custo, latência e viabilidade operacional. Modelos menores podem ser suficientes em cenários com contexto curto ou execução local. Nesse cenário, Prompt Engineering deixa de ser apenas a arte de escrever instruções e passa a envolver o gerenciamento de espaço escasso, organizando a informação para caber dentro da janela disponível e preservando o que é mais relevante para a resposta.

**Pontos de atenção**
- A janela de contexto inclui tudo o que é enviado na chamada, não apenas a última mensagem do usuário.
- Exceder o limite não “falha” necessariamente de forma explícita; o problema pode aparecer como perda silenciosa de informação.
- Mensagens antigas, trechos de documentos ou partes de código podem ficar de fora quando o contexto cresce demais.
- Respostas tendem a ficar menos consistentes quando o modelo não tem acesso a partes importantes do estado da interação.
- Uma janela maior não implica, por si só, em um modelo melhor.
- A seleção do modelo deve priorizar adequação ao caso de uso, custo e latência, e não apenas capacidade máxima.
- Em aplicações reais, é essencial planejar continuamente o que entra na chamada ao modelo.
- Prompt Engineering deve ser tratado como gestão de espaço e prioridade de informação, e não como simples acumulação de conteúdo.
- É importante pensar em estratégias para manter conversa e documentos dentro da janela disponível.
- Projetos que ignoram a janela de contexto tendem a ficar frágeis à medida que o volume de informação cresce.