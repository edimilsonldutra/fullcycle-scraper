Módulo: Prompt Engineering
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16601)

## Resumo da aula

Sumarização é a compressão semântica de interações anteriores para liberar espaço na janela de contexto sem simplesmente descartar conteúdo. Retomando o cenário em que o histórico crescia até exigir corte, a mudança aqui é substituir remoção literal por um resumo que preserva os pontos principais. Isso reduz a perda bruta de contexto em comparação com truncamento, embora não preserve todos os detalhes. O ganho prático é manter continuidade com menos tokens.

Um resumo mantém a estrutura geral do que já foi dito, o que ajuda o modelo a continuar a conversa com mais coerência do que teria após um corte seco. Ainda assim, resumir implica compressão, e compressão remove nuances, exceções e detalhes finos. Por isso, a sumarização diminui o risco de respostas desconectadas, mas não elimina risco de alucinação. Ela troca detalhe por capacidade de continuidade operacional.

A sumarização depende de um prompt explícito que instrui o modelo a condensar o histórico anterior em uma forma reutilizável. Um comando como “pegue todo o histórico até este ponto e crie um resumo” já expressa a ideia central, mas a qualidade do resultado depende de como o pedido é formulado. Prompt, aqui, deixa de ser apenas instrução textual e vira estratégia de compressão de contexto. O objetivo não é produzir um texto bonito, e sim um estado compacto que continue útil nas próximas chamadas.

Depois de gerado, o resumo pode ser reinjetado no início das próximas interações para substituir a parte antiga do histórico. Essa reinjeção transforma o resumo em contexto ativo: o sistema deixa de reenviar todas as mensagens anteriores e passa a reenviar uma versão condensada delas. O efeito operacional é liberar espaço para novas mensagens sem perder completamente a memória da conversa. Essa técnica é especialmente útil em fluxos longos, nos quais o histórico cresce continuamente.

A tarefa de resumir nem sempre exige o mesmo modelo usado para responder à tarefa principal. Se o modelo principal é caro e foi escolhido por capacidades mais sofisticadas, pode ser economicamente melhor enviar o histórico para um segundo modelo mais barato especializado ou suficientemente bom em sumarização. A lógica é simples: resumir informação já existente costuma exigir menos capacidade do que resolver o problema principal. Isso transforma a sumarização em uma decisão arquitetural de custo, não apenas em uma decisão de prompt.

A sumarização normalmente é acionada por uma rotina interna que monitora o crescimento da conversa e dispara a compressão quando um limite é atingido. Esse limite pode ser definido por quantidade de tokens, tamanho do histórico ou outra regra operacional da aplicação. Quando o gatilho ocorre, o sistema gera o resumo e pode armazená-lo para reutilização posterior. A técnica deixa de ser um evento manual e passa a fazer parte do ciclo normal de gerenciamento de contexto.

Uma implementação comum é persistir o resumo no banco de dados e, em interações futuras, verificar se já existe uma versão sumarizada daquela conversa. Se existir, o sistema ignora a parte antiga já condensada e injeta o resumo correspondente. Isso evita recomputar o mesmo contexto repetidamente e simplifica a reconstrução do estado conversacional. Retomando a arquitetura já conhecida, a novidade aqui é a camada de compressão inteligente entre histórico bruto e prompt final.

Não existe um único prompt de sumarização que funcione igualmente bem para qualquer domínio. Resumir um livro e resumir o histórico de codificação de uma aplicação são tarefas semanticamente diferentes, com critérios distintos de relevância, granularidade e fidelidade. Por isso, o prompt precisa refletir o tipo de conteúdo que está sendo comprimido. O conceito de sumarização permanece o mesmo, mas a estratégia de prompt muda conforme o objetivo do resumo.

Em Prompt Engineering, sumarizar não significa apenas pedir “resuma isso”, mas decidir o que precisa sobreviver à compressão para a próxima etapa do sistema. Essa decisão afeta custo, continuidade e qualidade da resposta, porque define quais sinais permanecem disponíveis após a redução de tokens. O prompt de sumarização, portanto, funciona como uma política de retenção semântica. Ele determina quais partes do passado continuam influenciando o comportamento futuro do modelo.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente falou sobre truncamento, tá? Agora eu quero falar com você sobre sumarização. Essa é uma técnica bem inteligente, tá? Que é muito utilizada. Ela é utilizada a pacas, inclusive, grande parte das IDEs, inclusive, que você trabalha no dia a dia, hoje em dia elas acabam fazendo o processo de sumarização automaticamente, tá? O que isso significa? Significa o seguinte,

00:30

que, ao invés de eu utilizar uma técnica de truncamento, o que vai acontecer? Eu vou usar uma outra técnica de sumarização. Ou seja, ao invés de eu cortar ou perder a informação, eu posso fazer um resumo

00:45

dos conteúdos anteriores e liberar espaço na janela de contexto. Então, ao invés de eu cortar esse pedaço que eu tinha dado de exemplo aqui para vocês, eu posso fazer um prompt e falo o seguinte, pegue todo o histórico de mensagens, até essa parte aqui, e crie um resumo para que eu não esqueça do que eu estou falando.

01:09

Estou dando um exemplo bem bobo aqui. A gente vai ver técnicas de como a gente escreve prompts, inclusive, para a sumarização, para deixar esse tipo de coisa bem mais claro, bem mais simples, porque existem prompts e prompts para você fazer sumarização. Mas o importante é você entender esse conceito. Então, ao invés de eu perder a mensagem, eu peço para ele pegar tudo o que ele viu até agora e fazer um resumo para mim.

01:37

E quando ele faz esse resumo, eu tenho os pontos principais do que foi falado, então eu não perco o contexto e eu minimizo o risco de fazer a IA sair alucinando. Por outro lado,

01:53

É muito claro de você entender que, se eu estou resumindo algo, significa que eu não tenho todos os detalhes daquilo. Então, eu ainda tenho chances maiores de alucinação na minha IA, porque ela não tem toda a informação, mas, pelo menos, eu estou dando um contexto para ela.

02:11

Uma outra coisa que é interessante é que, na hora que você vai sumarizar, você pode utilizar o próprio modelo para fazer essa sumarização. Ou seja, eu posso chegar e falar, olha, resuma todo o histórico que a gente tem agora e...

02:26

e daí ele vai gerar esse resumo, e aí a gente injeta esse resumo no início, antes das próximas respostas. Então, isso aí acontece. O ponto é que existem diversas técnicas para a gente colocar essa sumarização. A gente vai falar disso.

02:44

Outro ponto também é que você não necessariamente precisa usar o mesmo modelo para sumarizar. Por que eu estou dizendo isso? Muitas vezes eu quero criar um resumo, e para eu criar o resumo de algo,

03:00

não necessariamente eu preciso do melhor modelo, porque eu já tenho as informações. Então, vamos imaginar que eu posso pegar o modelo X, que ele é muito bom para fazer os cálculos e tudo mais, e a janela de contexto ali está diminuindo. O que eu posso fazer? Pegar essas informações, jogar para um outro modelo que é mais barato, mas que ele é muito bom para resumir.

03:24

Então, o que é capaz de acontecer? Eu gasto dinheiro com o modelo mais caro, mas, na hora de resumir, eu utilizo um modelo mais barato para fazer essa sumarização, para continuar. Porque eu não necessariamente preciso de um modelo extremamente

03:40

grande, um modelo extremamente caro para fazer um resumo. Então, eu sempre quero deixar isso em mente aqui para você, tá? Quando que nós fazemos essa sumarização? Aí vai depender muito em relação da arquitetura que você está utilizando, como essa é uma disciplina de Prompt Engineering, a gente não vai chegar nesse nível de detalhe.

03:59

Mas, normalmente, você pode fazer uma rotina interna que vai monitorando a conversa. Quando chega num limite, você faz a sumarização e daí você pode pegar esse resumo, guardar no banco de dados. Quando você for, por exemplo, continuar uma conversa e fazer uma outra interação, você faz uma verificação se existe uma sumarização daquela conversa. Se existir, ele ignora até onde a conversa foi e injeta aquela sumarização.

04:26

Então, são rotinas, são estratégias que você tem, não apenas do Prompt para sumarizar, mas da parte técnica que você precisa realmente para fazer essa sumarização. Como aqui o nosso objetivo é Prompt Engineering, eu não quero falar desse tipo de especificidade porque tem muito mais a ver com arquitetura. Mas, o que tem a ver de sumarização com Prompt Engineering? Como eu sumarizo?

04:52

como eu posso criar um prompt que realmente consiga sumarizar uma conversa gigante. Imagina que eu tenho um livro. Qual é o melhor prompt para eu fazer para que esse livro seja resumido? Então, isso aí não é fácil e não é um prompt de sumarização que vai resolver todos os problemas de sumarização. Então, provavelmente, você vai perceber que o prompt para resumir um livro

05:20

não é o mesmo prompt para eu resumir o histórico de codificação de uma aplicação que eu estou fazendo, mas o conceito de sumarização acaba sendo o mesmo. Beleza? Então, falamos um pouco de sumarização somente para você ter em mente para que ela serve e a gente vai seguir com isso aí. Vamos nessa!

## Resumo IA

**Abreviações**
- IA: Inteligência Artificial
- IDEs: Integrated Development Environments (Ambientes de Desenvolvimento Integrados)
- Prompt Engineering: Engenharia de Prompt

**Resumo**
A aula apresentou a sumarização como uma técnica de compressão semântica do histórico de interações para liberar espaço na janela de contexto sem simplesmente apagar informações, em contraste com o truncamento. O instrutor explicou que, em vez de cortar mensagens antigas, o sistema pode gerar um resumo com os pontos principais da conversa, preservando a continuidade operacional e reduzindo a perda de contexto. Esse resumo pode ser reinjetado nas interações seguintes, substituindo o histórico bruto e funcionando como contexto ativo para novas respostas.

Também foi destacado que a sumarização ajuda a reduzir respostas desconectadas, mas não elimina totalmente o risco de alucinação, pois a compressão sempre remove detalhes, nuances e exceções. O processo pode ser acionado por um prompt explícito, como um pedido para resumir todo o histórico até certo ponto, e sua qualidade depende da formulação desse prompt. O instrutor enfatizou que, em Prompt Engineering, sumarizar não é apenas “pedir um resumo”, mas definir quais informações precisam sobreviver à compressão para manter utilidade futura.

Outro ponto abordado foi a perspectiva arquitetural: a sumarização pode ser feita pelo próprio modelo principal ou por outro modelo mais barato e adequado à tarefa, já que resumir costuma exigir menos capacidade do que resolver o problema central. O fluxo comum envolve uma rotina que monitora o crescimento da conversa, dispara a sumarização ao atingir um limite, armazena o resumo — muitas vezes em banco de dados — e o reutiliza nas próximas interações. Por fim, foi reforçado que não existe um único prompt universal de sumarização, pois resumir um livro, por exemplo, é diferente de resumir um histórico de codificação, exigindo estratégias distintas conforme o domínio.

**Pontos de atenção**
- Sumarização não é truncamento: ela preserva o sentido geral, mas não mantém todos os detalhes.
- A técnica reduz, mas não elimina, o risco de alucinação.
- Resumos devem ser pensados para serem reutilizáveis como contexto nas próximas chamadas.
- A qualidade da sumarização depende fortemente de um prompt bem formulado.
- Não existe um prompt único que sirva para todos os domínios; o tipo de conteúdo muda os critérios de resumo.
- O objetivo do resumo não é ficar “bonito”, e sim ser funcional para continuidade da conversa.
- Pode ser mais econômico usar um modelo menor e mais barato para sumarizar.
- Em implementações reais, é comum monitorar tokens ou tamanho do histórico para disparar a compressão.
- Persistir o resumo em banco de dados facilita reaproveitamento e evita recomputar o mesmo contexto.
- Ao resumir, sempre há perda de nuances; por isso é preciso decidir o que realmente deve sobreviver à compressão.
