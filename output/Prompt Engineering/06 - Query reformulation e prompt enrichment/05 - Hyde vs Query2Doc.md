Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16749)

## Resumo da aula

Agora vamos falar sobre uma técnica que é bem similar ao Query-to-Doc, mas que possui algumas diferenças sutis que mudam completamente a categoria dessas abordagens. Essa técnica é chamada de HyDE, que significa Hypothetical Document Embedding. Somente pelo nome já é possível perceber que o tipo de busca é diferente.

A ideia é gerar um documento com a intenção de representar a resposta final, o que é diferente da geração de um documento que apenas explica a consulta. Vou mostrar a diferença de prompts para que isso fique mais claro. A proposta é criar um prompt bem elaborado para que, mesmo que a pergunta seja um pouco vaga, possamos gerar um documento bem estruturado.

Uma vez que você tem esse documento estruturado, ele pode ser utilizado para realizar a busca. O passo a passo é parecido com o que vimos anteriormente, mas com algumas diferenças importantes. Primeiro, recebemos a query do usuário. Em seguida, criamos um prompt para gerar um documento. Depois concatenamos esse documento com a query original e então geramos os embeddings.

Os embeddings, no final das contas, são a representação desse documento e da pergunta em formato vetorial. Depois disso realizamos a busca semântica. Ou seja, cruzamos o vetor gerado a partir do documento e da pergunta do usuário com os vetores armazenados no banco de dados.

Esse banco de dados pode ser, por exemplo, um Pinecone ou um PostgreSQL utilizando pgVector. O ponto principal é que realizamos a busca vetorial e recuperamos os trechos mais relevantes. Esses trechos são então utilizados para gerar a resposta final.

Se você perceber, o HyDE já nasce com a ideia de trabalhar com busca semântica utilizando embeddings. O Query-to-Doc surge antes disso, pois o principal foco dele está na busca léxica. Embora seja possível utilizar embeddings com Query-to-Doc, nesse caso você tende a se aproximar do estilo de abordagem utilizado no HyDE.

Para deixar isso mais claro, eu criei algumas comparações e exemplos de prompts para mostrar a diferença entre os dois. No Query-to-Doc pedimos um mini-artigo explicativo e neutro para enriquecer o vocabulário. Ou seja, o foco está em sinônimos, termos alternativos e variações de linguagem.

Essas informações ajudam no ranqueamento de palavras dentro de mecanismos de busca como Elastic utilizando algoritmos como BM25. Já no caso do HyDE, pedimos um documento que se pareça com uma resposta real para capturar melhor a semântica e o contexto relevante.

Uma coisa é ter mais palavras para melhorar a busca. Outra coisa é trazer mais contexto e compreender melhor as nuances da pergunta para realizar uma busca semântica no banco de dados.

O Query-to-Doc surgiu voltado para quem já utiliza BM25 ou Elastic e deseja enriquecer suas queries. Essa técnica não é algo totalmente novo, já existe há bastante tempo. O HyDE, por outro lado, surgiu para quem utiliza bancos vetoriais e precisa melhorar o Dense Retrieval em cenários de zero-shot.

Isso significa melhorar a capacidade de recuperar informações relevantes a partir da pergunta do usuário sem fornecer exemplos adicionais. Quando alguém faz uma pergunta em um sistema, normalmente não temos a oportunidade de fornecer exemplos ou trabalhar com few-shot.

Então a pergunta que recebemos precisa ser densa o suficiente para permitir a recuperação de informações relevantes em um cenário zero-shot. No final das contas, essa é a principal ideia.

Essas duas técnicas são similares, mas o estilo de texto que você pede para o LLM gerar é a grande diferença entre elas. O Query-to-Doc trabalha de uma forma mais neutra, pedindo descrições adicionais sobre o tema. O HyDE busca gerar uma resposta hipotética.

Vou mostrar um exemplo para deixar isso mais claro. Um prompt básico de Query-to-Doc poderia ser algo como: escreva um texto informativo e neutro, de 100 a 150 palavras, que explique o tópico abaixo. Inclua definições, termos técnicos, sinônimos e contexto relacionado, mas não forneça uma resposta direta caso seja uma pergunta.

Se você observar, nesse prompt de Query-to-Doc o objetivo é gerar conteúdo informativo. Não queremos a resposta final da pergunta, queremos apenas expandir o vocabulário relacionado ao tema.

Isso acontece porque, nesse cenário, o vocabulário é o principal fator que influencia a busca léxica em mecanismos baseados em ranking de palavras. Ou seja, o objetivo é enriquecer a consulta com mais termos relevantes.

Agora veja um exemplo de prompt para HyDE. Escreva um parágrafo conciso que responda de forma clara à pergunta abaixo. A resposta deve parecer um documento real, contendo datas, fatos ou descrições plausíveis, mesmo que hipotéticas. Não utilize linguagem especulativa e não use expressões como talvez ou possivelmente.

Se você observar, nesse caso já estamos pedindo diretamente uma resposta. Queremos gerar informações mais diretas, mesmo que não sejam necessariamente 100% corretas.

Isso acontece porque estamos criando um documento hipotético que será utilizado apenas para gerar embeddings e melhorar a busca semântica. Nesse contexto, sabemos que o documento pode conter informações que não são necessariamente corretas.

E nesse caso específico não estamos preocupados com a exatidão absoluta do conteúdo, porque ele não será apresentado diretamente ao usuário como resposta final. O objetivo principal é apenas gerar um documento suficientemente rico em contexto para melhorar o processo de recuperação de informações.

Para mim, uma resposta hipotética já é suficiente para ajudar na busca no banco de dados. Quando eu fizer a busca no banco de dados vetorial, baseado nessas palavras, nesse contexto, na semântica e nas nuances dessa resposta, eu vou recuperar as informações do banco de dados. E as informações do banco de dados, sim, contêm os dados corretos.

A resposta final será baseada nos trechos que vieram do banco de dados, e não nos trechos ou no documento hipotético gerado anteriormente. Uma coisa, e é muito importante que você entenda isso, é ter um documento hipotético, que podemos chamar aqui de documento “fake”, apenas para facilitar o entendimento.

Esse documento possui diversas palavras, contexto e nuances que, quando combinadas com a pergunta do usuário e transformadas em vetores, permitem realizar a consulta no banco de dados. Nesse banco de dados é onde está a fonte da verdade.

Mesmo sendo um documento hipotético, ele ajuda a recuperar trechos muito mais precisos da fonte de verdade presente no banco de dados. Isso acontece porque ele adiciona contexto que uma pergunta genérica normalmente não possui.

Por exemplo, se a pergunta for apenas “o que é Go?” ou “o que é a linguagem Go?”, a consulta possui pouco contexto. Agora, quando eu gero um documento sobre a linguagem Go, posso falar sobre documentação, versão, APIs, biblioteca padrão e diversos outros aspectos.

Mesmo que parte dessas informações não esteja 100% correta, o simples fato de termos esses termos e esse contexto permite que, ao consultar o banco de dados, ele traga documentos ou trechos de documentos muito mais próximos do que o usuário realmente procura.

Ou seja, ele recupera os chunks de documentos que possuem maior proximidade semântica com o contexto da pergunta. No resultado final, o que teremos no prompt é a pergunta original do usuário.

Em seguida teremos o contexto, que são os trechos recuperados do banco de dados. No momento de gerar a resposta final para o usuário, o documento hipotético não é utilizado diretamente.

Isso acontece porque ele contém dados hipotéticos e não necessariamente corretos. No entanto, esses dados hipotéticos ajudaram a enriquecer a busca no banco de dados para recuperar informações reais, corretas e mais precisas.

Portanto, esse documento funciona apenas como um elemento temporário que ajuda a melhorar a recuperação de dados. É importante perceber também a diferença em relação ao Query-to-Doc.

No caso do HyDE, estamos mais interessados em gerar algo que se pareça com uma resposta à pergunta do usuário, mesmo que ela não esteja totalmente correta. Ainda assim, as palavras, o contexto e as ideias presentes nesse texto ajudam a expandir a busca.

Isso aumenta as chances de recuperar documentos mais relevantes. Nesse cenário estamos falando muito mais de semântica, vetores e busca vetorial.

Já no Query-to-Doc estamos muito mais focados em palavras, vocabulário expandido e repetição de termos que ajudam no ranqueamento de documentos em mecanismos de busca léxica.

Por isso é importante entender que a ideia não é pegar informação incorreta e entregá-la ao usuário final. A ideia é usar uma informação hipotética para enriquecer a busca no banco de dados.

Assim, o banco de dados consegue trazer as informações corretas para o usuário, mas com uma probabilidade muito maior de recuperar trechos realmente relevantes. Essa é a ideia principal.

Espero que tenha ficado clara a diferença entre Query-to-Doc e HyDE.

## Transcrição

00:00

Bom, pessoal, agora a gente vai falar sobre um camarada que é bem similar ao Queer2Doc, mas ele tem algumas diferenças que são sutis, mas mudam completamente a categoria desses camaradas. Então, é uma técnica que a gente chama de HIDE, que é Hypothetical Document Embedding. Então, somente pelo nome já dá para perceber que o tipo de busca é diferente. Então, a ideia é a gente gerar um documento com a intenção de ser a resposta final.

00:30

que é um pouco diferente da geração de um documento que explica a consulta. Eu vou mostrar a diferença de prompts, daí vai ficar um pouco mais claro para você. Mas a ideia é que a gente consiga realmente criar um prompt bem elaborado para que aquela pergunta, mesmo que seja um pouco vaga, a gente tenha realmente um documento bem estruturado.

00:53

Uma vez que você tem esse documento bem estruturado, a gente consegue usar esse documento para fazer a busca. Então, o passo a passo é similar ao de cima, mas tem algumas diferenças, e aí a gente vai entender. Um, a gente vai receber a query do usuário, a gente vai fazer o prompt para gerar o documento, a gente vai concatenar esse documento com a query original, e aqui a gente vai gerar os embeddings. Então, os embeddings, no final das contas, são

01:19

a representação desse documento e a pergunta no formato de vetores. E aí, o que vai acontecer? Nós vamos realizar a busca semântica, ou seja, eu vou cruzar o vetor com essa informação que eu acabei de gerar desse documento e a pergunta do usuário,

01:35

com os vetores que estão no meu banco de dados, por exemplo. Eu posso estar usando um Pinecone, um Postgres com um pgVector, não interessa. Mas o ponto é que eu vou realizar essa busca e eu vou retornar com os trechos recuperados para daí eu gerar a resposta final. Então, se você perceber, o Hide já veio com a ideia sempre de fazer busca semântica.

01:59

trabalhar já com embeddings e etc. O QueryToDoc vem antes disso, porque o principal aspecto dele é na busca léxica. Apesar de você pode fazer embeddings, mas aí você vai perceber que você vai tender indiretamente a cair nessa pegada do hide. Então, para ficar um pouco mais claro isso aqui, eu criei algumas...

02:26

diferenças e prompts para que você consiga perceber a diferença entre os dois, tá? Então, ali, o Query-to-Doc versus o Hide. Então, o Query-to-Doc, ele pede um mini-artigo explicativo neutro para enriquecer o vocabulário. Então, se você está a perceber, ele está muito mais focado em vocabulário, sinônimos, palavras alternativas e coisas desse tipo, porque é a partir dessas informações

02:52

que a gente vai ter ranqueamento de palavras no formato de busca num banco de dados como o LASC usando o BM25, por exemplo. No caso do Hydro, o que acontece? Eu peço um documento que parece com a resposta real para capturar a semântica e o contexto relevante. Então, uma coisa é você ter palavras

03:15

a mais para fazer com que a busca funcione. E outra coisa, eu trazer mais contexto e entender as nuances para que eu consiga fazer uma busca semântica no banco de dados.

03:30

O Query-to-Doc nasceu focado para quem já utiliza a BM25 e também Elastic e quer enriquecer as suas queries. Então, essa técnica, de forma geral, não é a coisa mais nova do mundo. Já é algo que já existe já faz um bom tempo.

03:48

O HIDE nasceu já para quem usa banco de vetorial e precisa melhorar o Dense Retrieval Zero-Shot. O que isso significa? Ou seja, a forma de como eu consigo pegar a informação que o usuário está perguntando numa tacada só, sem eu dar exemplo.

04:08

Por que isso acontece? Porque, quando alguém faz uma pergunta, de forma geral, eu não estou tendo oportunidade de ficar dando exemplos, trabalhar com feelshot, etc. Ou seja, como que eu consigo fazer com que a pergunta que eu recebi seja densa o suficiente para que eu consiga pegar dados com zero shot? No final das contas, é isso, tá?

04:31

Esses caras são similares, mas o estilo de texto que você vai pedir para o LLM é a grande diferença. Então, o Query-to-Doc, por exemplo, ele vai trabalhar de uma forma mais...

04:47

neutra, pedindo mais descrição das coisas. O hide quer uma resposta mais hipotética. Então, eu vou dar um exemplo, acho que vai ficar mais claro aqui pra você. Então, o lance é o seguinte, olha só. Um prompt básico de query to doc.

05:03

Escreva um texto informativo e neutro, de 100 a 150 palavras, que explique o tópico abaixo, inclua definições, termos técnicos, sinônimos e contexto relacionado, mas não dê uma resposta direta se for uma pergunta. Então, se você perceber, nesse prompt para Queer2Doc, eu estou querendo, na realidade, é pegar algo informativo.

05:27

Eu não estou querendo a resposta de uma pergunta, eu quero simplesmente expandir o meu vocabulário, porque o vocabulário aqui nesse caso é o que interessa para eu fazer tipos de busca léxica, por exemplo, tá?

05:42

Então, acho que essa que é a grande pegada. Se você perceber, eu estou muito mais pedindo a informação adicional do que necessariamente querendo ter a resposta do usuário. Agora, olha aqui o prompt para a raid, por exemplo. É o seguinte, escreva um parágrafo conciso que responda de forma clara as perguntas abaixo.

06:04

A resposta deve parecer um documento real, com datas, fatos ou descrições prováveis, mesmo que hipotéticas. Não use linguagem especulativa, não diga talvez ou possivelmente. Então, se você perceber, aqui nesse nosso caso, eu já estou querendo uma resposta. Eu já estou querendo trazer informações mais diretas, mesmo que ela não seja a informação 100% correta.

06:33

E o porquê que eu estou colocando dessa forma? E ainda eu coloquei, não diga talvez ou possivelmente. Por que eu estou querendo isso? Porque ele vai gerar um documento hipotético, mas nesse documento a gente sabe que vai ter um monte de informação que não necessariamente vai ser informação correta.

06:53

E eu não estou preocupado de ser realmente, aqui nesse caso, a situação correta, a resposta correta. Para mim, uma resposta hipotética já é o suficiente para me ajudar com o quê?

07:10

para a minha busca no banco de dados. Porque quando eu fizer a busca no meu banco de dados vetorial, aí sim, baseado nessas palavras, nesse contexto, na semântica, nas nuances daquela resposta,

07:26

eu vou pegar as informações do banco de dados, e as informações do banco de dados, sim, elas têm os dados corretos. E a minha resposta vai ser baseada nos trechos que vieram do banco de dados, mas não

07:43

dos trechos, ou do documento hipotético gerado aqui. Então, uma coisa, e é muito importante que você entenda isso, uma coisa é eu ter um documento hipotético, vou colocar fake aqui só pra gente saber, mas ele tem aqui diversas palavras

08:07

contexto, nuances, etc., que, na hora que eu juntar com a pergunta do usuário, transformar esses dois caras aqui em vetor, e, com esse vetor, eu fazer a minha consulta no meu banco de dados,

08:33

E, nesse meu banco de dados, aqui eu tenho a fonte da verdade. Mas, com esse documento fake, ele vai fazer com que eu traga trechos de fontes da verdade do meu banco de dados muito mais acurados ou que tenha mais relevância do que simplesmente uma pergunta genérica. O que é goal?

08:54

Ou o que é linguagem Go? É algo muito pequeno. Agora, quando eu crio um documento sobre linguagem Go, eu vou estar falando sobre documentação, eu vou estar falando sobre versão, eu vou estar falando sobre API, eu vou estar falando de biblioteca padrão, mesmo que essa informação não esteja 100% correta.

09:11

Mas somente de eu ter esses trechos e essas informações aqui, quando eu consultar o banco de dados, o banco de dados vai trazer para mim os documentos, os trechos de documentos aqui, os chunks dele, que estão muito mais próximos com palavras que provavelmente tem no contexto da pergunta do usuário. E aí, no resultado final, o que eu vou ter? No meu prompt, eu vou ter question,

09:35

E aqui eu vou ter os trechos, o contexto do banco de dados. Esse cara aqui, na hora que é para gerar a resposta final para o usuário, esse meu camarada aqui, ele não é utilizado porque eu não tenho dados necessariamente corretos, são dados hipotéticos. Mas esses dados hipotéticos me ajudaram a enriquecer

10:02

a minha busca no banco de dados para eu trazer dados reais, corretos, acurados, do meu banco de dados. Então, esse cara aqui é um temporário que me ajuda a gerar isso. Mas perceba a diferença do Query-to-Doc. Aqui, eu estou muito mais realmente interessado em responder a pergunta do usuário, mesmo que seja errada, entre aspas. Por mais que ela esteja errada,

10:27

provavelmente as palavras, o contexto ou coisas parecidas têm chance de ser expandido para eu conseguir buscar os documentos mais corretos. Então, aqui a gente está falando muito mais de semântica, vetores e buscas, aqui no Career2Doc a gente está falando muito mais em palavras,

10:46

e aparecem mais repetidas e coisas desse tipo para o tipo de busca que eu vou fazer. Então, é importante que você entenda que a minha ideia não é pegar informação errada e dar para o usuário final. É pegar informação hipotética que pode ser errada e usá-la para fazer a busca no banco de dados e o banco de dados, sim, trazer a informação correta para o usuário, mas agora o banco de dados tem mais chance de capturar trechos mais relevantes. Então, essa que é a ideia principal.

11:14

Fechou? Então, espero que vocês tenham entendido essas diferenças aí entre o query-to-doc e o hide aí também.

## Resumo IA

**Abreviações**  
- **HyDE**: *Hypothetical Document Embedding*  
- **LLM**: *Large Language Model*  
- **BM25**: algoritmo de ranqueamento probabilístico para busca léxica  
- **Elastic**: *Elasticsearch*  
- **pgVector**: extensão para PostgreSQL que permite armazenamento e busca vetorial  
- **Pinecone**: banco de dados vetorial

**Resumo**  
A aula apresentou a técnica HyDE (*Hypothetical Document Embedding*) e a comparou com Query-to-Doc, destacando que, embora pareçam semelhantes, elas atendem a objetivos diferentes. No HyDE, o instrutor explicou que o sistema recebe a query do usuário, gera um prompt para produzir um documento hipotético que pareça uma პასუხa real, concatena esse documento com a query original e gera embeddings para realizar busca semântica em um banco vetorial, como Pinecone ou PostgreSQL com pgVector. O foco está em enriquecer o contexto e a semântica da consulta para melhorar o *Dense Retrieval* em cenários *zero-shot*, sem depender de exemplos anteriores. Já o Query-to-Doc foi descrito como uma técnica voltada principalmente à busca léxica, especialmente em ferramentas como Elasticsearch com BM25, onde a prioridade é expandir vocabulário, incluir sinônimos, termos alternativos e variações de linguagem para favorecer o ranqueamento por palavras. A aula também mostrou exemplos de prompts: no Query-to-Doc, o texto gerado deve ser neutro, informativo e voltado a vocabulário; no HyDE, deve parecer uma resposta plausível, com fatos e descrições, mesmo que hipotéticas. Por fim, foi enfatizado que o documento hipotético não é entregue ao usuário final: ele serve apenas para melhorar a recuperação de trechos corretos e relevantes da fonte da verdade armazenada no banco de dados.

**Pontos de atenção**  
- Não confundir o objetivo das técnicas:  
  - **Query-to-Doc** → expansão lexical, sinônimos, termos relacionados, ranqueamento por palavras.  
  - **HyDE** → expansão semântica, contexto, recuperação vetorial.
- O documento gerado no HyDE pode conter informações hipotéticas ou imprecisas; ele **não deve ser usado como resposta final**.
- A “fonte da verdade” precisa estar no banco de dados; é dele que devem vir os trechos usados para responder ao usuário.
- No HyDE, o valor está em gerar um texto denso em contexto para melhorar a recuperação semântica, especialmente em cenários **zero-shot**.
- No Query-to-Doc, o prompt deve evitar responder diretamente a pergunta e focar em enriquecer o vocabulário.
- No HyDE, o prompt deve evitar linguagem especulativa como “talvez” ou “possivelmente”, pois o texto precisa parecer uma resposta real.
- A escolha da técnica depende do tipo de busca: mecanismos léxicos como BM25/Elastic favorecem Query-to-Doc; bancos vetoriais favorecem HyDE.
- A query original continua importante: ela é combinada com o documento gerado antes da criação dos embeddings.
- O documento hipotético é um elemento temporário de recuperação, não uma verdade a ser apresentada ao usuário.