Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17061)

## Resumo da aula

Uma Deep Research em PDF ou Markdown costuma ser rica, mas pouco operacional para fluxos posteriores. O objetivo da adaptação não é resumir a pesquisa, e sim transpor o mesmo conteúdo para um template estruturado que facilite consulta, revisão e reaproveitamento. Essa exigência muda completamente o prompt: a IA precisa reorganizar, não condensar. Se ela resumir demais, o documento deixa de ser base técnica e vira apenas uma visão geral.

A reorganização pode usar um template com seções como contexto e motivação, fundamentos, conceitos-chave, panorama, arquiteturas, estratégias, algoritmos, tecnologias, boas práticas, métricas, casos de uso, riscos, segurança, tendências e impacto. Esse formato funciona como documento coringa porque distribui a pesquisa em blocos previsíveis, o que facilita localizar decisões e alimentar outros artefatos. As 16 seções não são regra fixa; são um ponto de partida que pode ser adaptado ao tipo de projeto. O valor real está na padronização suficiente para reutilização, sem engessar o conteúdo.

O fluxo é direto: abrir um novo chat, colar o prompt de adaptação e anexar o PDF ou Markdown gerado na Deep Research. A instrução central deve pedir preservação integral do conteúdo e adequação ao formato desejado, sem resumo indevido. Retomando o exemplo do rate limiter, a pesquisa bruta vira um documento com arquiteturas, tipos de rate limiting, estratégias, algoritmos e referências organizadas por seção. O resultado continua extenso, mas passa a ser navegável e mais útil como insumo técnico.

A IA frequentemente tenta resumir documentos longos, mesmo quando o prompt pede o contrário. Por isso, a revisão humana precisa verificar se exemplos, estratégias, links, trechos técnicos e nuances importantes foram preservados. Quando a saída vier superficial, a correção não é aceitar o texto como está, mas iterar o prompt, repetir a geração ou trocar de modelo. O critério de qualidade aqui não é elegância do texto, e sim fidelidade estrutural e densidade técnica.

Modelos diferentes se comportam de forma diferente em tarefas longas de reestruturação. Quando o documento é muito grande, vale comparar a capacidade de manter volume, detalhamento e aderência ao pedido de não resumir. O Gemini é citado como alternativa útil para saídas extensas, inclusive em cenários gratuitos, enquanto o ChatGPT pode resumir além do desejado em alguns casos. A decisão prática é empírica: testar o mesmo insumo em mais de um modelo e avaliar qual preserva melhor o conteúdo.

O ganho principal não está apenas em “ter um texto mais bonito”, mas em transformar pesquisa crua em contexto reutilizável. Esse documento reestruturado pode servir de base para gerar drafts de Feature Design Doc, complementar prompts e reduzir a dependência de entrevistas guiadas quando o contexto já está bem consolidado. Em vez de começar do zero, o fluxo passa a compor documentos a partir de insumos preparados. Isso reduz fricção e melhora a qualidade do rascunho inicial.

Uma Deep Research extensa não garante cobertura equilibrada do que realmente importa para o projeto. Quando o pedido é genérico, a IA tende a aprofundar demais alguns aspectos e tratar superficialmente outros que seriam decisivos para design e implementação. Estruturar o escopo no prompt ajuda a distribuir a atenção da pesquisa entre fundamentos, mecanismos, riscos, segurança e aplicação prática. O resultado é um documento mais útil para engenharia, não apenas mais longo.

Quando vários documentos se acumulam — pesquisa técnica, documentos de mais alto nível, detalhes técnicos e guidelines — a IA passa a operar com contexto muito mais forte. Isso permite quebrar implementação em partes, derivar tarefas, sugerir snippets e apoiar decisões com menos improviso. O trabalho documental não substitui programação, mas antecipa decisões e reduz ambiguidade na fase de execução. Esse valor aumenta quando os documentos continuam sendo atualizados conforme o desenvolvimento avança.

## Transcrição

00:01

Bom, pessoal, seguinte, tá? Estamos na nossa parte 2 de fazer Deep Research, tá? E o que acontece? Qual é a diferença dessa Deep Research com a Research inicial que a gente fez ali, né?

00:17

Na realidade, o ponto principal desse prompt é conseguir pegar, por exemplo, aquele PDF que ele gerou com aquela Deep Research, a gente importar num outro chat e rodar esse prompt aqui em cima, tá? Esse prompt, no final das contas, ele tenta ao máximo pedir para a IA gerar um documento para você,

00:40

que tenha tudo, absolutamente tudo, que exista naquele PDF ou na Deep Research, mas que ele transponha esse documento num formato que eu gostaria que estivesse, porque é um formato que comigo funciona muito bem,

00:59

Fica bem mais fácil, inclusive, outros documentos usarem essa research baseado nessas sessões, que podem me ajudar, inclusive, a desenvolver o meu feature design docs ou coisas desse tipo. Então, basicamente, são essas sessões que eu utilizo, contexto e motivação, fundamentos, conceitos-chave, panorama e abordagens existentes, arquiteturas e modelos de aplicação, estratégias, algoritmos, mecanismos, tecnologias, frameworks e ferramentas,

01:29

boas práticas, diretrizes técnicas, métricas e critérios de avaliação, casos de uso, riscos, considerações de segurança, tendências de evolução, impacto. Perceba, galera, tem bastante coisa aqui que eu acabo colocando nesse prompt, são 16 sessões, você não precisa fazer necessariamente com essas 16 sessões, tá?

01:49

mas o que eu sempre quero dizer é, você tem que ter essa flexibilidade, mas aqui é simplesmente um ponto de partida que você pode fazer. Então, eu posso iniciar um novo chat aqui, colar esse cara aqui que eu coloquei aqui no prompt, e também, que eu acho que é um dos pontos mais importantes aqui, é conseguir, deixa eu ver se eu...

02:13

tem arrastar o PDF que foi gerado pela minha Deep Research, tá? E aí, a partir disso, ele consegue gerar esse tipo de documento. Agora, uma dica, se eu puder dar pra você, eu dou nesse momento.

02:28

Algumas vezes, quando eu tento fazer isso no chat GPT, dependendo do tamanho do documento, o chat GPT começa a resumir algumas coisas que eu não gostaria, e muitas vezes isso funciona muito bem. Então, o que acontece?

02:46

você vai ter que ser bem crítico com o resultado que ele gerou daquela pesquisa, baseado no documento que você está solicitando, tá? Se você perceber, eu tentei, baseado nesse prompt, falar diversas vezes para não resumir, para simplesmente adequar o conteúdo e tudo mais,

03:03

Mas, às vezes, chat GPT funciona de um jeito, do outro você pode tentar mais vezes, ou até mesmo testar com outros modelos de inteligência artificial. O Gemini é um cara que eu recomendo. Normalmente, quando eu preciso gerar conteúdos muito extensos, eu sinto que o Gemini acaba me respondendo, pelo menos no modelo que ele está rodando agora, no modelo que o GPT dá nesse momento.

03:26

Talvez quando você esteja assistindo esse vídeo a gente tenha GPT-10, mas o fato é que, de forma geral, vale a pena às vezes você testar com outros modelos. Eu acredito que no Gemini, até mesmo com conta gratuita, você consegue fazer coisas parecidas aí com isso, tá? Então, basicamente, é colocar o seu PDF ou Markdown, que foi gerado na Deep Research, e mandar ver aqui nesse cara, tá? Com isso aqui,

03:52

ele vai gerar, basicamente, um documento. Eu vou mostrar pra vocês o documento que ele gerou pra mim aqui, tá? Então, esse documento aqui, se você olhar, é o resultado desse prompt que eu botei o PDF, onde ele readecou o documento baseado

04:11

naquele prompt, ou seja, tinha aquele pdf, ele transformou esse pdf nesse documento aqui, e é também um documento grande, mas ele está um pouco mais estruturado, aqui provavelmente é problema de copiar e colar, mas...

04:28

ele traz bastante estrutura, bastante código em relação a como que essas paradas funcionam. Então, arquiteturas, modelos da aplicação, explica os tipos de rate limiting, arquiteturas híbridas, estratégias, algoritmos, aqui ele trouxe diversas estratégias aqui pra gente.

04:46

Ou seja, é um documento bem grande se você for olhar, tá? Mas ele segue aquela estrutura que eu normalmente gosto e essa estrutura, de forma geral, eu acho ela bem coringa para qualquer tipo de projeto, tá? Então, eu acho que vale a pena você testar essa estrutura que eu estou utilizando ou, eventualmente, você adaptar essa estrutura para...

05:08

para uma que faça mais sentido. Normalmente, essa que eu coloquei, se não me engano, tem 16 seções. Ela é bastante grande, mas ela é uma Deep Research que acaba nos dando bastante insumo para que você consiga...

05:22

trabalhar, tá? Então... Então, aqui tem documentos, pesquisas recomendadas, diversos links e coisas desse tipo. Então, isso aqui acabou virando a minha Deep Research da forma como eu pedi para estruturar, tá? Nada impede de você usar a Deep Research crua que foi gerada naquele PDF, etc. Mas o que, pelo menos, eu recomendo é que você use um prompt parecido ao que eu utilizei para contextualizar

05:51

pra IA o que você quer naquela Deep Research, porque na maioria das vezes, quando eu vejo a galera utilizar, acabam pedindo isso de uma forma muito genérica, e daí a Deep Research sai trazendo informações muito de um aspecto e pouco daquele que você quer, e as coisas acabam ficando desequilibradas.

06:11

Não é porque é uma Deep Research e tem muita informação que vai ter toda a informação que você queira. Então, por isso que trazer esses tipos de escopo acabam ajudando bastante aí nesse aspecto, tá? Agora, como uma Deep Research ou um documento desse tipo de coisa poderia me ajudar a gerar, por exemplo, um feature design doc?

06:35

E eu acho que são nesses aspectos que a gente começa a evoluir. E por isso que eu digo que não necessariamente você tem que usar aqueles prompts que eu te passei para você ser entrevistado. Muitas vezes, com uma deep research, com algumas outras informações, vão fazer com que você consiga gerar aqueles documentos de uma forma mais fácil ou um draft inicial para que você consiga ali trabalhar. Eu sei que...

07:05

Gerar documento não é a coisa mais prazerosa do mundo. Eu sei que é muito bom a gente estar programando e tudo mais, mas, de forma geral, pessoal, não tem muito para onde a gente fugir quando a gente vai utilizar documentação. Trabalhar com documentação fica muito legal quando a gente começa a codificar e a gente já tem os documentos prontos.

07:27

porque daí a coisa fica realmente muito legal, tá? Mas no momento que a gente está agora, eu preciso que você entenda os tipos de documento, como que você faz pesquisa para conseguir gerar esses diversos tipos de documento, e uma hora que a gente tem já, vamos dizer, um bundle de documentos que são importantes, você vai ver que conforme a gente vai evoluindo,

07:48

Para começar a desenvolver uma feature, por exemplo, com o IA, você tem esses documentos de mais alto nível, você tem detalhes técnicos, daí você já consegue falar para o IA, me ajude a separar essa implementação em diversas partes. Agora que eu tenho diversas partes, me ajude a criar essas tarefas. Agora, baseado nessas informações, me ajude a trazer quais são os principais snippets. Ah, fora isso, eu tenho documentos de guidelines que eu quero criar também. Então, isso aí vai sempre te ajudar muito

08:18

pra que na hora que você for implementar, trabalhar. Agora, não dá pra gente, vamos dizer, fazer um MBA partindo do princípio que você tem todos os documentos prontos pra você sair programando na IA. Não. Você tem que entender, não é a coisa mais feliz do mundo como programar, mas eu não tenho dúvidas que quando você vê esses documentos em ação no momento que a gente vai programar, por exemplo,

08:41

você vai ver o quanto que tudo isso acaba valendo a pena. E lembrando que essas documentações, elas precisam ser atualizadas conforme a gente vai desenvolvendo. E isso aí é um outro aspecto importante de Workflow que a gente vai ver aí em outras disciplinas e coisas desse tipo. Fechou?

## Resumo IA

**Abreviações**  
- IA — Inteligência Artificial  
- PDF — Portable Document Format  
- Markdown — linguagem de marcação leve para formatação de texto  
- GPT — Generative Pre-trained Transformer  
- Gemini — modelo/plataforma de IA generativa do Google  
- Feature Design Doc — documento de design de feature  

**Resumo**  
A aula explicou como transformar uma Deep Research gerada em PDF ou Markdown em um documento mais estruturado e reutilizável, em vez de apenas resumir o conteúdo. O objetivo central não é condensar a pesquisa, mas reorganizá-la em um template fixo que facilite consulta, revisão, reaproveitamento e alimentação de outros artefatos técnicos, como Feature Design Docs. Para isso, o instrutor propõe um fluxo simples: abrir um novo chat, colar um prompt de adaptação e anexar o PDF ou Markdown produzido pela Deep Research.

O prompt deve solicitar explicitamente a preservação integral do conteúdo, pedindo que a IA adeque o material ao formato desejado sem resumir indevidamente. O instrutor sugeriu uma estrutura com várias seções, como contexto e motivação, fundamentos, conceitos-chave, panorama e abordagens existentes, arquiteturas e modelos de aplicação, estratégias, algoritmos, mecanismos, tecnologias, frameworks e ferramentas, boas práticas, diretrizes técnicas, métricas e critérios de avaliação, casos de uso, riscos, considerações de segurança, tendências de evolução e impacto. Embora tenha mencionado 16 seções, deixou claro que isso não é uma regra fixa, mas um ponto de partida adaptável ao tipo de projeto.

Também foi destacado que a IA costuma tender ao resumo, especialmente em documentos longos, mesmo quando o prompt pede o contrário. Por isso, a revisão humana é essencial para verificar se exemplos, estratégias, links, trechos técnicos e nuances importantes foram preservados. Se a saída vier superficial, a recomendação é iterar o prompt, repetir a geração ou testar outro modelo. O instrutor mencionou que diferentes modelos se comportam de forma distinta em tarefas extensas de reestruturação, citando o Gemini como uma alternativa útil para saídas longas, inclusive em cenários gratuitos, enquanto o ChatGPT pode resumir além do desejado em alguns casos.

O principal ganho desse fluxo é transformar pesquisa bruta em contexto reutilizável para engenharia. Um documento reestruturado passa a servir como base para gerar rascunhos de Feature Design Docs, complementar prompts e reduzir a dependência de entrevistas guiadas quando o contexto já está consolidado. A aula também enfatizou que a Deep Research deve ser orientada por escopo, porque pedidos genéricos tendem a produzir documentos desequilibrados, aprofundando demais certos aspectos e deixando outros superficiais. Quando vários documentos se acumulam e são mantidos atualizados, a IA consegue apoiar melhor a decomposição de implementação, a geração de tarefas, a sugestão de snippets e a tomada de decisão durante o desenvolvimento.

**Pontos de atenção**  
- Não confundir adaptação estrutural com resumo: o objetivo é preservar o conteúdo e reorganizá-lo.  
- A IA tende a condensar documentos longos; é necessário validar criticamente a saída.  
- Se faltar detalhe, repetir a geração, ajustar o prompt ou trocar de modelo pode ser necessário.  
- Prompt genérico gera pesquisas desequilibradas; é importante definir escopo e áreas de foco.  
- O template com várias seções é um ponto de partida, não uma regra fixa; deve ser adaptado ao projeto.  
- Verificar se exemplos, estratégias, links e nuances técnicas foram mantidos.  
- O critério de qualidade é fidelidade estrutural e densidade técnica, não “beleza” textual.  
- Comparar modelos é uma boa prática quando o documento é muito grande, pois o comportamento varia.  
- Manter a documentação atualizada ao longo do desenvolvimento aumenta bastante o valor do workflow.  
- Documentação não substitui programação, mas reduz ambiguidade e melhora os insumos para implementação.