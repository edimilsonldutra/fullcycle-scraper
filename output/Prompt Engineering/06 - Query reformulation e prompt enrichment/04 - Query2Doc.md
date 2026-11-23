Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16748)

## Resumo da aula

Agora que entendemos um pouco desse fluxo básico, quero trazer algumas técnicas utilizadas nesse processo. Essas técnicas normalmente possuem um contexto muito importante quando falamos de obtenção de dados externos, acesso a banco de dados e coisas desse tipo.

Vamos começar com a primeira técnica, chamada Query-to-Doc. A ideia desse Query-to-Doc é bastante interessante. Quando recebemos uma instrução do usuário, pedimos para que seja gerado algo como um documento que explique melhor o que aquela consulta realmente quer dizer.

Ou seja, será gerado um texto para expandir a query antes de executarmos a busca. É como se o usuário fizesse uma pergunta e, antes de utilizá-la diretamente, pedíssemos algo como: gere um pequeno artigo sobre esse tema considerando a pergunta do usuário. Esse é apenas um exemplo simples.

Quando você recebe esse texto gerado, percebe que passa a ter mais informações sobre aquele assunto. Isso faz com que, no momento em que realizamos a busca sobre aqueles termos, possamos receber dados muito mais precisos.

Digo isso porque o Query-to-Doc tem uma relação muito forte com um tipo de busca chamado busca léxica. Normalmente temos funções ou algoritmos como o BM25, ou mecanismos utilizados por ferramentas como Elastic e Apache Lucene.

Esses mecanismos funcionam, basicamente, realizando um ranqueamento de palavras-chave e termos que mais aparecem para encontrar documentos relacionados àquela consulta. Então, quando recebemos a instrução do usuário, podemos pedir a geração de alguns exemplos.

Também podemos trabalhar com Few-Shot Prompting, onde fornecemos exemplos de perguntas e demonstramos como gerar um mini-documento objetivo sobre aquele tema. Depois que temos a resposta do LLM, o que fazemos é concatenar esse conteúdo com a pergunta do usuário.

Podemos estruturar algo mais ou menos dessa forma: question, onde colocamos a pergunta do usuário. Em seguida, adicionamos informações adicionais geradas pelo modelo. Quando enviamos isso para realizar uma busca em um Elastic, por exemplo, o mecanismo não utiliza apenas a pergunta original.

Ele também passa a considerar todas as outras palavras presentes nesse mini-documento gerado, o que aumenta o contexto da busca e melhora as chances de encontrar resultados mais relevantes. Obviamente, é necessário ajustar bem o prompt utilizado para gerar esse documento.

Além disso, é importante que o texto gerado seja o mais neutro possível, pois ele não representa a resposta final. O objetivo é apenas trazer informações relevantes que facilitem o processo de busca.

Então, inicialmente, o Query-to-Doc tem a ideia de gerar textos neutros que ampliem o contexto da consulta para facilitar uma busca léxica. Não estamos falando ainda de busca semântica baseada em vetores.

Mais adiante falaremos sobre busca vetorial. Existem outras técnicas que são mais direcionadas a esse tipo de abordagem, embora tenham algumas semelhanças.

A grande ideia aqui é ter uma estratégia para fazer com que a pergunta do usuário ou as informações necessárias possuam mais contextualização durante o processo de busca. Esse é o ponto principal.

Outro ponto importante é entender que, nesse cenário, o modelo não é o responsável direto pela resposta final. Na realidade, o modelo é utilizado apenas para gerar esse mini-documento.

O resultado final desse processo será a recuperação de diversos trechos de documentos. Imagine que você está consultando um banco de dados e recebe vários trechos desses documentos, cada vez mais relevantes para aquela pergunta.

Quando chega o momento de gerar a resposta final, teremos primeiro a pergunta original do usuário. Em seguida, teremos algo chamado context.

Nesse contexto, incluímos os trechos de documentos que foram encontrados no banco de dados com base naquela busca enriquecida. A partir disso, podemos pedir para a IA responder à pergunta.

Ela irá analisar o contexto fornecido e gerar a resposta baseada nessas informações. Ou seja, tudo isso é uma forma de manipular e estruturar melhor o prompt.

Esse processo é muito parecido com técnicas de RAG, que funcionam exatamente dessa maneira. A grande diferença é que a principal função da IA aqui não é gerar a resposta final.

A principal função é gerar conteúdo adicional que melhore o processo de busca, permitindo recuperar documentos mais relevantes e, somente depois, produzir a resposta final. Então vamos continuar, porque ainda temos mais uma técnica para analisar.

## Transcrição

00:01

Bom, pessoal, e agora que a gente entendeu um pouco esse fluxo básico, eu quero trazer aqui para vocês algumas técnicas que são utilizadas, mas essas principais técnicas normalmente têm um contexto extremamente importante no que tange a pegar dados

00:24

de externos, acesso a banco de dados e coisas desse tipo. Então, seguinte, vamos falar do primeiro cara aqui, que é o famoso Query-to-Doc. Então, basicamente, a ideia desse Query-to-Doc é bem interessante. Então, quando a gente recebe uma instrução do usuário, a gente pede para ter a geração num tipo de um documento.

00:48

que vai explicar o que a consulta realmente quer. Ou seja, eu vou ter o texto gerado para expandir a query antes de executar. Então, é como se eu fosse fazer uma pergunta...

01:01

o usuário fez a pergunta e eu peço o seguinte, gere um artigo, estou dando um exemplo simples, eu tenho um prompt aqui que eu vou te mostrar, sobre esse tema e coloca a pergunta do usuário. Na hora que você recebe esse texto, você vai perceber que você tem mais informação sobre aquele assunto. E o que isso faz com a gente? Faz com que na hora que a gente vai fazer uma busca

01:31

sobre aqueles termos, eu consiga receber dados muito mais acurados. E por que eu estou dizendo isso? Porque esse Query-to-Doc tem um apontamento muito grande para um tipo de busca, que é o que a gente chama de busca léxica. Normalmente, a gente tem funções, algoritmos, como o BM25, depois você pode pesquisar, ou até mesmo a forma como o Elastic e o Apache Lucid funcionam.

02:01

Mas, basicamente, na hora que você faz uma busca, ele começa a fazer um ranqueamento de palavras-chaves e termos que mais repetem para trazer documentos referentes a isso. Então, o que acontece? Quando a gente recebe a instrução do usuário, a gente vai fazer o quê?

02:22

pedir alguns exemplos, e a gente pode até dar alguns exemplos, trabalhar com o Prompt Fill Shot, onde você dá exemplos de perguntas de como fazer um mini-documento bem objetivo sobre aquele tema. E aí, quando eu tenho essa resposta do LLM, o que eu vou fazer? Eu vou concatenar a pergunta do usuário, então eu posso colocar mais ou menos dessa forma aqui. Eu posso colocar assim, question,

02:52

Aqui é a pergunta do usuário. Em seguida, eu posso colocar informações adicionais.

03:07

E aí, o que acontece? Quando eu mando isso pra fazer uma busca num Elastic, por exemplo, o que vai acontecer? Ele vai pegar, obviamente, a pergunta, mas ele vai trazer ainda, ele vai buscar ainda por mais palavras lá no Elastic pra dar mais contexto pra gente ter mais chance de pegar esse tipo de resultado. Obviamente, né,

03:30

e você tem que ajustar bem o prompt para ver como que você vai gerar esse documento, e, inclusive, fazer com que as respostas e esse prompt trabalhem de uma forma mais neutra possível, porque ele não é como se fosse a resposta final, mas é simplesmente

03:50

trazer informações relevantes para facilitar esse processo de busca, tá? Então, isso aqui que é importante que você consiga entender, tá? Então, inicialmente, o Query2Doc tem a ideia de fazer um prompt para trazer textos cada vez mais neutros para eu fazer uma busca léxica e...

04:11

não é uma busca semântica, ou seja, busca em vetores, a gente já vai falar sobre isso, mas também você pode fazer busca vetorial, de forma geral. Mas aí a gente já tem um outro tipo de técnica que acaba sendo mais intencional nesse tipo de coisa, mas são bem parecidos. Então, a grande sacada aqui é você ter uma estratégia e técnica para fazer com que a sua pergunta ou

04:38

as informações que você precisa, elas tenham mais contextualização na busca. E aqui que é o ponto importante que eu estou querendo dizer, o seu modelo aqui, no final das contas, ele não é o maestro. Na realidade, o modelo, nesse ponto que a gente vai utilizar, ele vai gerar esse mini documento,

04:59

E o resultado disso vai ser, no final das contas, diversos trechos de documentos. Imagina que você está consultando um banco de dados e vai receber um monte de trechos desses documentos, cada vez mais apurados, para na hora que você gera a resposta final, basicamente, você vai ter para a resposta final

05:22

a pergunta que o cara colocou, a instrução. Aí o que eu vou pegar? Eu vou pegar algo chamado context.

05:31

E, nesse contexto aqui, eu vou pegar, no final das contas, os trechos dos documentos que foram encontrados no banco de dados, baseado naquele mini-documento de na pergunta. Então, quando eu tenho isso, eu posso pedir aqui pra IA. Responda a pergunta e

05:57

ela vai olhar o contexto e ela vai responder essa pergunta baseado nesse contexto ou na resposta ou qualquer coisa desse tipo. Então, é tudo uma forma de você conseguir manipular o prompt. Isso é muito parecido com técnicas de reg, que acabam fazendo exatamente isso, mas a grande sacada não está na ia gerar resposta final.

06:19

Aqui, a grande sacada é a IA conseguir gerar mais conteúdo para fazer a busca, para trazer o resultado, para, sim, trazer a resposta final. Beleza? Então, vamos nessa porque a gente tem mais um cara para a gente ver aí.

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model*.
- **BM25** — *Best Matching 25*.
- **Elastic** — *Elasticsearch*.
- **Apache Lucene** — mecanismo/biblioteca de busca e indexação de texto.
- **RAG** — *Retrieval-Augmented Generation*.
- **Prompt Fill Shot / Few-Shot Prompting** — técnica de prompting com poucos exemplos no enunciado.

**Resumo**
A aula apresentou a técnica **Query-to-Doc**, usada principalmente em cenários de obtenção de dados externos, acesso a banco de dados e busca em mecanismos de recuperação textual. A ideia central é transformar a consulta do usuário em um **mini-documento** mais explicativo e neutro, antes de executar a busca. Em vez de pesquisar apenas com a pergunta original, o sistema pede ao LLM que gere um texto expandido sobre o tema, aumentando o contexto disponível para a busca.

Esse conteúdo gerado é então **concatenado à pergunta do usuário** e enviado ao mecanismo de busca, como Elastic ou soluções baseadas em **BM25** e **Lucene**, que operam com **busca léxica**, ranqueando palavras-chave e termos recorrentes. O instrutor destacou que isso melhora a chance de recuperar trechos mais relevantes, pois a consulta passa a incluir mais termos associados ao assunto. Também foi citado o uso de **Few-Shot Prompting** para ensinar o modelo, com exemplos, a produzir esse mini-documento de forma objetiva.

Por fim, a resposta final não é gerada diretamente pela IA nesse primeiro passo: o modelo serve principalmente para enriquecer a consulta. Depois da busca, os **trechos recuperados** formam um **contexto** que é combinado com a pergunta original, permitindo que a IA responda com base nesses documentos. O fluxo se aproxima de técnicas de **RAG**, com a diferença de que aqui o foco está em melhorar a busca por meio da geração de texto auxiliar.

**Pontos de atenção**
- O texto gerado pelo modelo deve ser **neutro** e servir apenas para ampliar a consulta, não para antecipar a resposta.
- O **prompt** precisa ser bem ajustado para gerar um mini-documento útil e consistente.
- A técnica é voltada para **busca léxica**, não para busca semântica/vetorial.
- O ganho vem da **expansão de contexto** da consulta, aumentando a chance de recuperar documentos relevantes.
- O LLM, nesse fluxo, **não é o responsável pela resposta final**; ele atua na etapa de enriquecimento da busca.
- É importante separar bem **question** (pergunta do usuário) e **context** (trechos recuperados) na etapa final de resposta.
- O processo se assemelha a **RAG**, mas com ênfase em usar o modelo para **melhorar a recuperação**, antes de responder.