Módulo: Arquitetura na Era da IA\
Aula: [Gerando chunks com metadados](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18414)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, agora chegou o momento onde a gente vai fazer o nosso processo de ingestão.

00:06

Mas essa ingestão a gente não vai salvar em banco de dados ainda,

00:09

a gente está falando em chunking.

00:11

E aqui é uma das formas que são importantes para você olhar.

00:16

Eu estou utilizando o Langchain. Então, tem dois caras aqui específicos, nesse caso,

00:21

como a gente está trabalhando com Markdown, tem o Markdown Header Text Splitter,

00:25

e esse cara é um dos caras mais famosos,

00:27

que é o Recursive Character Text Splitter, tá?

00:31

Eu vou explicar aqui para vocês como é que vai funcionar de forma geral, tá?

00:35

Aqui, né, são as pastas, os caminhos que eu vou trabalhar,

00:39

mas também eu tenho um Output Path,

00:43

onde eu vou ter chunks .jsonl, jsonl é um JSON numa linha só.

00:47

No final das contas, dentro da pasta data para a gente ver o resultado.

00:50

E aqui eu tenho meus metadados padrão,

00:53

mas agora começa a perceber a linha de raciocínio que a gente tem.

00:57

Se você olhar, eu tenho aqui chunk size,

01:00

eu estou dizendo que eu vou ter 900 caracteres por pedaço,

01:04

ou seja, eu imagino que eu tenho um texto gigante,

01:06

eu vou pegar 900 caracteres desse cara aqui.

01:10

E o que é chunk overlap?

01:12

Ou seja, de... Depois dos 900 caras,

01:15

eu vou pegar 150 caras da sessão anterior. Para quê?

01:19

Caso eu tenha perdido uma parte do contexto,

01:22

daquele conteúdo que faz parte de tudo,

01:27

eu garanto que eu não perco completamente o que estava acontecendo antes.

01:31

Porque imagina que tem lá, o preço é 50,

01:35

mas não fala o preço do quê?

01:37

Mas na linha anterior falava o preço do produto X. Então...

01:41

Como eu pego essa linha anterior no meu overlap,

01:44

eu garanto que eu tenho um pouco de contexto. O grande ponto é,

01:47

um overlap muito grande, eu tenho muita duplicação de conteúdo,

01:50

porque vai ter que estar também no banco de dados gravado.

01:53

Porém, um overlap muito pequeno, eu tenho risco, na realidade,

01:56

de perder esses contextos nessas fronteiras onde eu tenho.

02:01

Aqui eu coloquei 900 e 150, é algo bem comum de forma geral.

02:06

Aí a gente tem o load documents, que a gente tem,

02:08

eu estou usando uma biblioteca de front matter aqui para ficar melhor,

02:11

e eu tenho aqui a parte de carregar os nossos documentos.

02:17

E até então não tem segredo,

02:19

carregar documento não tem segredo e também ler

02:24

esses documentos aqui também não tem.

02:26

Então um eu carrego um documento específico e o outro eu

02:29

carrego todos os documentos ali para mim numa lista.

02:32

Agora, olha só que interessante.

02:34

Eu tenho uma função chamada sectionOf,

02:37

onde eu passo aqui para ele um dicionário de metadados de headers.

02:43

O que isso significa? Se você olhar aqui, headersToSplitOn,

02:47

eu estou relacionando o seguinte no meu dicionário.

02:50

Quando eu encontrar um hash, uma hashtag é H1. Quando eu encontrar dois, é H2.

02:55

Quando eu encontrar três, são H3, certo? Então, o que ele vai fazer?

03:00

Ele vai...

03:01

pegar o que a gente recebe nessas informações e conseguir fazer

03:07

essa relação dos três sustentados

03:12

para os títulos da nossa aplicação.

03:16

E isso vai ser muito importante,

03:18

porque é aqui que entra o X da questão. Então, basicamente,

03:23

quase tudo isso que eu acabei de mostrar foi para chegar nesse momento.

03:27

Eu até pedi para colocar comentário aqui para ficar melhor.

03:30

Então, esse Chunk Document é a função que realmente

03:33

vai separar o nosso documento em pequenos pedaços. Mas, novamente,

03:38

tem que ser feito isso de uma forma inteligente. Então,

03:40

aqui eu estou passando uma das formas que é bem comum de você utilizar.

03:43

Primeira coisa, eu vou ter alguns Splitters.

03:46

Splitters é aquele cara que faz a separação. Então,

03:49

o primeiro Splitter que eu tenho é que eu vou pegar... os headings do meu Markdown,

03:54

e eu vou separar em seções, tanto nos headings H1, H2,

03:58

H3, tá? Então, isso aí já vai me ajudar.

04:01

Então, se você olhar aqui, ó,

04:02

eu tenho o Markdown Splitter, Markdown Header Text Splitter,

04:06

e eu tô falando quais são os headers que eu tenho pra fazer a separação,

04:09

que é o Header to Split On,

04:11

e é aquela constante que a gente viu logo no começo, beleza? Então, agora,

04:17

imagina que eu tenho um documento e eu peguei esse documento

04:20

e todos esses headers eu fiz a separação agora aqui para mim. Então, agora,

04:25

eu já não estou pegando um documento e quebrando ele sem nenhum critério.

04:31

Eu estou usando como critério títulos,

04:34

porque sessões fazem mais sentido estar juntos ali.

04:38

Mas, às vezes, uma sessão também é muito grande.

04:42

Então, eu tenho a parte de character splitter.

04:45

O que esse cara faz? Ele pega baseado naquelas,

04:49

os textos que a gente tem, né? E quebra no tamanho que a gente queria. Então,

04:55

nesse caso, eu tenho o chunk size de 900 e o chunk overlap de 150,

05:00

tá? Então, eu tenho esses dois caras.

05:02

Eu tenho a separação das seções e eu tenho a pegar os nossos chunks,

05:09

né? E quebrar nos formatos de texto.

05:12

Agora que eu tenho declarado os dois splitters que eu tenho, o que que eu vou fazer?

05:17

Eu vou pegar aqui sessões, tá?

05:19

É o Markdown Text Splitter e colocar o conteúdo dele,

05:23

né? Que eu recebo aqui, ó, o post, né? Aqui pra mim.

05:26

O post.content. Então, o que que eu fiz agora nesse caso?

05:29

Peguei meu conteúdo inteiro e separei eles nas minhas sessões, certo? E agora, o que que eu fiz agora?

05:36

Eu criei uma outra variável agora chamada pieces, que são os pedaços.

05:40

onde eu pego esse carácter aqui, TextSplitter,

05:44

e faço a separação desses documentos baseado nas seções que eu quebrei.

05:50

Entende? Então,

05:51

eu não estou pegando aleatoriamente o meu documento

05:55

e quebrando ele em vários pedaços.

05:56

Não. Eu separo as seções.

05:58

Agora que eu tenho as seções, eu vou quebrar os pedaços baseado naquela seção.

06:03

E agora que eu tenho os pedaços aqui comigo,

06:07

O que eu vou fazer? Eu tenho aqui...

06:09

Eu declarei aqui um array de chunks e agora eu vou fazer um loop.

06:14

E esse loop é muito importante, porque olha só o que vai acontecer.

06:19

Eu vou pegar aquele meu pedaço, ou seja, eu recebo vários pedaços,

06:26

Eu vou pegar o meu pedaço e vou pegar o quê?

06:28

Vou pegar todo o metadado que tem daquele documento e vou preencher aqui no metadata.

06:36

Então isso significa que todos esses metadados aqui

06:39

Vão estar junto aqui dentro desse meu chunk. Ou seja,

06:43

Eu tenho o chunk e tenho todos aqueles metadados

06:46

Que para mim são obrigatórios do documento.

06:48

Mas, além disso, e agora que eu quero que você preste bem atenção,

06:52

Eu vou ter alguns metadados a mais que eu tinha comentado com você.

06:57

Eu tenho nesse caso o Chunk ID, para eu saber...

07:00

Qual é o índice daquele chunk?

07:02

Imagina que eu tenho uma sessão inteira falando sobre, sei lá,

07:06

Suporte P1, mas essa sessão tem 10 documentos,

07:12

10 caras de 900 caracteres. Então, o que eu faço?

07:16

Eu pego esse chunk e gero um Chunk ID aqui para mim.

07:21

Ou seja, vai ser o ID desse cara.

07:24

Outra coisa, eu vou pegar o Search File.

07:26

Ou seja, de onde vem esse documento? Outra coisa.

07:30

Qual que é o índice desse chunk aqui para mim?

07:33

Ou seja, porque quando eu recebo, eu vou receber ele enumerado,

07:39

Então eu quero saber se esse chunk vem antes de um

07:41

Ou antes do outro ou qualquer coisa desse tipo.

07:44

Outra coisa que eu separei aqui é em qual sessão esse chunk veio.

07:49

E por que isso é importante,

07:51

Por exemplo, nesse caso? Se eu for fazer uma busca no banco de dados,

07:54

Se alguém fizer alguma pergunta específica, eu posso também filtrar por sessão.

08:00

Porque isso também faz parte do metadado, vai me ajudar a buscar caso eu precise.

08:04

E aqui eu tenho também Content Length,

08:06

Que vai falar para mim a quantidade de caracteres que eu tenho ali dentro.

08:11

E aí, no final,

08:12

Eu dou um append no conteúdo aqui que

08:17

Eu tenho e nos metadados aqui para mim.

08:20

Então o meu chunk vai ter Content com o conteúdo,

08:24

E ele vai ter metadados com todos os

08:27

Metadados que eu tenho especificamente daquele conteúdo. Ou seja,

08:31

Eu tenho o chunk e eu tenho os metadados para eu conseguir trabalhar.

08:34

E depois disso, eu tenho a minha função aqui de Save Chunks,

08:38

Que vai pegar esses chunks e vai salvar dentro de um arquivo

08:42

Ali na minha pasta de output que eu tinha colocado.

08:45

E aqui eu tenho um print sample somente para a gente entender.

08:48

Peguei ali cinco chunks para a gente ver como é que fica,

08:50

Tá? Mas, basicamente, é isso. E aqui, no main,

08:53

Eu simplesmente estou carregando e executando essas funções aqui para mim.

08:57

Então, vamos executar esse cara aqui para você ver.

09:01

Então, é novamente o Ingest, né? Então, vou dar um Enter e

09:06

Prontinho. Então, olha só que interessante. Ele carregou seis documentos,

09:11

Gerou os chunks e, desses seis documentos, foram gerados 106 chunks, tá?

09:17

E os chunks foram salvos aqui dentro da pasta data-chunks.jsonl aqui para mim.

09:23

Então, somente para a gente entender um exemplo de um chunk. Então,

09:26

eu tenho billing policy 0, que ele vem do source billingpolicy.md,

09:31

que é da parte de política de faturamento, que tem 349 caracteres. Wesley,

09:38

mas não poderia ter 900? Poderia, mas essa sessão... É pequena,

09:42

então eu não preciso ter 900 caracteres dentro de cada documento necessariamente, tá?

09:49

Depois eu posso até aumentar aqui pra gente o tamanho dos

09:53

nossos arquivos e pra ter um conteúdo maior ainda, tá?

09:56

Mas perceba como é que ele foi separando e principalmente aqui dá

10:00

pra perceber que ele foi pegando ali pra gente por sessão.

10:03

Se eu abrir aqui meu data e ver o chunks.jsonl,

10:06

olha só, aqui tem... O conteúdo inteiro, esse documento descreve a formação,

10:11

etc, etc. Como é JSONL, ele fica numa linha só, ruim para ler,

10:16

mas olha só, metadata, está vendo?

10:18

Título, política de faturamento, o tenant FCIA, FCIA Cloud,

10:23

o plano para todos, documento Policy, a versão 2601.

10:30

2026, a gente pode estar em 2028, está escrito aqui 2026,

10:33

se está publicado, a visibilidade é interna, e agora a gente tem,

10:37

chunk ID, zero, search file, billingpolicy.md, chunk index, zero,

10:43

política de faturamento, e depois o tamanho do chunk.

10:47

Se você olhar aqui, eu tenho agora princípios de faturamento, o section,

10:52

está vendo? Aqui outra seção, boleto bancário, eu tenho outra seção aqui,

10:55

que ele vem de... Aqui tem o title,

11:00

deixa eu ver se eu tenho aqui outro cara com sessão.

11:03

Certify, que já é outro arquivo,

11:04

é cobrança por consumo excedente. Então, se você perceber,

11:08

eu já tenho todos esses caras aqui separados para mim.

11:12

São arquivos, é um monte de JSON que eu gerei,

11:15

mas o que eu mais queria mostrar, na realidade,

11:17

é como que a gente usou essa lógica para a gente fazer a quebra desses arquivos.

11:22

nos pedaços que fazem sentido desse conteúdo,

11:25

separando ali os metadados.

11:27

Se você começou errado pela estrutura dos seus metadados,

11:29

você vai ter problema lá na frente.

11:31

E esse problema custa caro,

11:33

porque quando você percebe que você precisa de mais coisa,

11:36

eventualmente você vai ter que reindexar tudo.

11:38

Aí você vai ter que gerar os embeddings tudo de novo,

11:40

vai ter que salvar tudo de novo e etc.

11:42

Gera um custo danado para a empresa.

11:44

Então planeje bem essa parte aqui. Fechou? Então vamos nessa.

## Resumo IA

[RESUMO_IA]