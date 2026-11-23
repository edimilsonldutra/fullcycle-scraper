Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17230)

## Resumo da aula

Então aqui está o prompt para vocês terem um comando que vai executar e gerar esses documentos de guidelines, como acabei de mostrar. Como isso funciona de forma geral? A grande filosofia por trás disso é que quis dar uma flexibilidade bem grande para que possamos escolher o que faz sentido especificar na hora de gerar a guideline do nosso projeto.

Defini o comando como generate-development-guideline, onde informamos a linguagem de programação e podemos passar infinitos parâmetros. Coloquei aqui os parâmetros suportados, mas já fiz outros testes e vocês não precisam necessariamente usar todos esses parâmetros. Se quiserem, podem escrever naturalmente outros parâmetros que a IA vai entender e conseguir gerar para vocês.

A ideia é: eu digo generate-development-guideline, passo a linguagem e depois parâmetros como -orm=prisma, -web-framework=express ou -web-framework=nestjs, -database=mysql, -test=jest, -log=log4j, -validation=zod para TypeScript, -validation=pydantic para Python, e assim por diante. Conforme passamos os parâmetros, o comando vai registrar essas informações no documento e, ao mesmo tempo, fazer uma pesquisa de pontos interessantes para correlacionar durante a geração da guideline.

Um exemplo prático: generate-guideline go -orm=sqlc -database=postgres -test=testify. E assim vai.

Precisamos entender alguns pontos importantes, e acho que essa é a maior pegadinha desse tipo de comando. Esse documento tende a ser muito grande. Não só isso: é muito fácil fazer com que a IA ultrapasse o mínimo que coloquei aqui, que é entre mil e mil e quinhentas linhas no total. Mil e quinhentas linhas é linha pra caramba. Mas também precisamos entender que, apesar de ser bastante conteúdo, tem muito exemplo de código e, às vezes, uma linha é apenas uma chave. Mesmo assim, é muita coisa.

Um ponto importante que percebi é que, na hora em que o agente fica pensando, buscando as coisas e gerando o documento para gravar no disco, pode acontecer de a janela de contexto estourar ou a memória não suportar tanto conteúdo sendo gerado de uma vez. Por isso, quero deixar claro que, nesse comando, coloquei algumas regras para que ele vá fazendo apêndices no arquivo de forma incremental, em vez de tentar gerar tudo de uma vez, porque isso dá problema.

Essa é uma das grandes pegadinhas. Também coloquei autovalidação, critérios de qualidade, a quantidade de exemplos que considero importante ter, e pedi para ele seguir alguns requisitos importantes. Outra coisa: como algumas seções são opcionais, ele precisa renumerar as seções de acordo com as que forem utilizadas.

Na fase 1, ele entende os parâmetros que estão sendo passados, extrai essas informações para que tudo funcione, e não faz autopopulação dessas categorias. Ele entende o objeto final como a stack que será utilizada, mas algumas bibliotecas são autopopuladas. Lembram que mostrei para vocês que algumas bibliotecas escolhi e outras são autopopuladas, ou seja, normalmente são padrões da linguagem. Então, dei o exemplo: se eu não passar certos parâmetros, ele vai trazer os padrões da linguagem, como em Python, TypeScript, JavaScript, Rust, etc.

Outra coisa interessante: ele gera internamente um resultado em JSON. Assim, ele sabe se fui eu que especifiquei, se foi autopopulado, ou se alguns desses itens não se aplicam a esse tipo de guideline, de acordo com o que passei. E ele traz a estrutura de como queremos trabalhar. Lembram que coloquei Project Stack, nome da linguagem, User Specified Libraries, etc.

Na fase 2, é a pesquisa. Peço para ele fazer uma pesquisa em tudo o que foi feito. Ele vai buscar em documentações oficiais, em documentações de grandes empresas, como o padrão do Google, por exemplo. Também pesquisa as ferramentas e o ecossistema da linguagem, as características da linguagem. Por exemplo, algumas linguagens focam muito em concorrência, outras têm tipagem estática ou dinâmica. Ele levanta essas características, faz uma pesquisa aprofundada e entende exemplos do dia a dia para trabalharmos.

Ele também pesquisa as principais bibliotecas, tanto as que escolhi quanto as que foram autopopuladas na fase anterior. Para isso, ele traz documentações com URLs, descrição, última versão, mas sem se aprofundar em exemplos. Porque se trouxer muitos exemplos, a documentação deixa de ser uma guideline geral e vira um tutorial específico sobre autenticação com Spring, por exemplo. Quero apenas os dados principais sobre esses aspectos.

Coloquei aqui o mínimo que ele precisa fazer para considerar que a pesquisa foi realizada.

Pessoal, para este vídeo não ficar gigante, vou cortar aqui e continuamos no próximo, porque quero trazer mais alguns aspectos.

## Transcrição

00:01

Bom pessoal, então aqui está o prompt para você ter um comando que vai conseguir executar e gerar esses documentos de guidelines como eu acabei de mostrar para você. Então, como é que isso funciona de forma geral? Eu acho que a grande filosofia da coisa está no seguinte,

00:27

eu quis fazer com que esse comando desse uma flexibilidade bem grande para que nós pudéssemos escolher o que faz sentido a gente especificar na hora de gerar a guideline do nosso projeto. Então aqui eu defini como é que funciona o nome do comando que é generate development guideline onde eu coloco a linguagem de programação e eu posso passar infinitos parâmetros. Então eu coloquei aqui

00:54

parâmetros suportados, mas eu já fiz outros testes claros ali que você não necessariamente precisa ter todos esses parâmetros, ou se você quiser, você pode escrever naturalmente outros parâmetros que a IA vai entender e vai conseguir gerar para você, tá? Então, a ideia é, eu falo Generate Development Guidelines, eu passo a linguagem e depois eu falo "-rm="prisma".

01:18

Menos, menos web, é web framework. Então, eu vou trabalhar, sei lá, com o Express. O framework que eu vou utilizar vai ser o NestJS. O meu banco de dados, eu vou trabalhar com o MySQL. Eu vou trabalhar com o teste. Qual que vai ser? Eu vou trabalhar com o Jest. Vou trabalhar com a parte de log. Vou trabalhar ali com o Log4J. A parte de validação, quais são as bibliotecas de validar. Vou trabalhar com o Zod, lá no TypeScript. Vou trabalhar com o Pydent.

01:43

E aqui, então, você consegue ir passando os parâmetros, e conforme você faz isso, esse comando vai fazer o quê? Vai registrar, obviamente, no documento que você está utilizando isso, mas, ao mesmo tempo, ele vai fazer uma pesquisa de pontos interessantes para correlacionar isso durante a geração do guideline. Então, um exemplo fica aqui, o generate-guideline, o go, o rm,

02:09

SQL C, o X e o D, a parte de banco de dados é o PDX, a parte de test é o TESTIFY e assim vai, tá? E aqui, o que acontece? A gente tem que entender alguns pontos importantes e eu acho que essa é a maior pegadinha desse tipo de comando aqui pra você, tá? Por que eu tô dizendo isso?

02:33

Porque esse documento, ele tende a ser muito grande, tá? E o ponto importante aqui, não é só que ele tende a ser muito grande. É muito fácil fazer com que a IA, ela passe ainda desse mínimo que eu coloquei aqui, de entre mil a mil e quinhentas linhas no total. E se você olhar, mil e quinhentas linhas é linha pra caramba. Mas a gente também tem que entender que, apesar de ser bastante linha,

02:56

Tem muito exemplo de código e, às vezes, uma linha é uma chave, mas, mesmo assim, acaba sendo bastante conteúdo. Então, apesar de eu colocar entre 1.000 e 1.500 linhas no total, daí você pode escolher, um ponto importante que eu acabei percebendo é o seguinte...

03:16

Na hora de tanto que o agente fica pensando, ele fica buscando as coisas e depois ele vai gerar esse documento para gravar no disco, às vezes, o que acontece? Acaba a janela de contexto. Ou, às vezes, estoura a memória com tanto conteúdo que ele está gerando naquele momento. Então, uma das coisas que eu...

03:39

Quero já deixar claro aqui para você em relação desse comando, é que eu coloquei algumas regras para que, incrementalmente, ele vá fazendo apêndices no arquivo, ao invés de tentar gerar tudo de uma vez, porque dá ruim, tá? Então, essa eu acho que é uma das grandes pegadinhas de tudo isso e a autovalidação. Então, eu coloquei alguns critérios de qualidade, coloquei a quantidade de exemplos que eu acho que é importante ter e etc.

04:07

E aqui, eu pedi para ele seguir alguns requisitos importantes para trabalhar. Outra coisa também é que, como algumas sessões são opcionais, então ele tem que renumerar essas sessões de acordo com as sessões que foram a ser utilizadas. Então, passo a primeira fase aqui, que é

04:27

Entender os parâmetros que estão sendo passados. Então, aqui é a nossa fase 1, tá? Então, entenda esses parâmetros, então extrai os parâmetros para que isso aqui funcione, né? Não faça autopopulação dessas categorias e tudo mais.

04:42

E daí, Jerry entenda o objeto final como uma stack que vai ser utilizada, mas bibliotecas autopopuladas. Ou seja, lembra que eu mostrei para vocês que são algumas bibliotecas que eu escolhi e outras que são autopopuladas? Ou seja, que normalmente são padrões da linguagem ali para a gente. Então, eu dei o exemplo aqui.

05:07

regras, padrões de uma determinada linguagem. Então, se eu não passar isso, ele vai trazer isso aqui como padrão. No exemplo de Python, TypeScript, Javascript, Rust, etc. Outra coisa interessante é, ele vai gerar internamente ali pra ele, né, um resultado como um JSON internamente. E aí, ele vai saber se foi eu que especifiquei, né, ou se foi autopopulado, ou se alguns desses caras aqui não vão se aplicar pra esse tipo de guideline de acordo com o que eu passei, tá? E aí,

05:36

ele vai trazer a estrutura de como que a gente quer trabalhar. Lembra que eu coloco o Project Stack, o nome da linguagem, User Specified Libraries, etc. Aí fase dois é pesquisa. Aí eu peço pra ele fazer uma pesquisa em tudo aquilo que foi feito. Então ele vai sair pesquisando, então ele vai buscar em documentações oficiais, documentações onde

06:02

grandes empresas utilizam, então, ah, eu vou seguir o padrão do Google para ele trabalhar com o Google, ou coisa desse tipo, tá? Então, ferramentas em torno de tudo isso, ou seja, as ferramentas e o ecossistema daquela linguagem,

06:18

as características daquela linguagem. Então, por exemplo, eu tenho determinada linguagem que foca muito em concorrência, eu tenho linguagem que é de tipagem estática, tenho linguagem que é de tipagem dinâmica. Então, ele vai entender e levantar as características da linguagem, ou seja, fazer uma pesquisa aprofundada e entender exemplos no dia a dia para a gente trabalhar. E daí ele faz também uma pesquisa

06:45

ali das principais bibliotecas, onde eu escolhi, e aquelas bibliotecas que foram autopopuladas na fase anterior, tá? E aí, pra isso, aí eu vou trazer, né, ali pra tudo isso, eu vou trazer essas documentações com RLs, a descrição, a última versão, né, e eu não fazer e trazer

07:08

exemplos daquilo. Porque se eu trago muitos exemplos, essa minha documentação deixa de ser de Java e acaba virando sobre autenticação com Spring. Então, eu quero só os dados principais em relação a esses aspectos. E coloco aqui o que ele tem que fazer, no mínimo, para ele dizer que ele fez a pesquisa para a gente. Pessoal, só para esse documento não ficar gigante, porque ele já é, esse vídeo não ficar gigante, eu vou cortá-lo aqui e a gente continua com o próximo, porque eu quero trazer mais alguns aspectos aqui. Fechou?

## Resumo IA

**Abreviações**
- **ORM** — *Object-Relational Mapping*
- **Web Framework** — framework web
- **TypeScript** — linguagem de programação
- **MySQL** — sistema de gerenciamento de banco de dados relacional
- **Jest** — framework de testes em JavaScript/TypeScript
- **Log4J** — biblioteca de logging para Java
- **Zod** — biblioteca de validação de esquemas para TypeScript
- **Pydantic** — biblioteca de validação e modelagem de dados para Python
- **JSON** — *JavaScript Object Notation*
- **SQLC** — ferramenta para gerar código a partir de SQL
- **Postgres / PostgreSQL** — sistema de banco de dados relacional
- **Testify** — biblioteca/framework de testes para Go
- **Express** — framework web para Node.js
- **NestJS** — framework web para Node.js/TypeScript
- **Go** — linguagem de programação também conhecida como Golang
- **Python** — linguagem de programação
- **JavaScript** — linguagem de programação
- **Rust** — linguagem de programação

**Resumo**
A aula apresentou a estrutura de um comando chamado `generate-development-guideline`, criado para gerar documentos de guideline de projeto com alta flexibilidade. O instrutor explicou que o comando recebe a linguagem de programação como base e aceita múltiplos parâmetros opcionais, como ORM, framework web, banco de dados, biblioteca de testes, logging e validação, permitindo que a IA monte um documento alinhado à stack desejada. Também foi mostrado que, além dos parâmetros suportados explicitamente, a IA pode interpretar descrições naturais adicionais.

O fluxo foi dividido em fases. Na fase 1, o comando identifica e extrai os parâmetros informados, monta uma representação interna em JSON e determina o que foi especificado pelo usuário, o que deve ser autopopulado por padrão da linguagem e o que não se aplica ao contexto. Na fase 2, a IA realiza pesquisa sobre a linguagem, seu ecossistema, características técnicas e bibliotecas relevantes, consultando documentação oficial e referências de grandes empresas. Essa pesquisa inclui URL, descrição e versão mais recente das bibliotecas, mas evita exemplos excessivos para não transformar a guideline em um tutorial específico.

O instrutor também destacou que o documento gerado tende a ser muito grande, chegando a mil ou mil e quinhentas linhas, o que traz desafios de contexto e memória durante a geração. Por isso, o comando foi desenhado para escrever o conteúdo de forma incremental, fazendo apêndices no arquivo em vez de tentar produzir tudo de uma vez. Além disso, foram adicionadas regras de autovalidação, critérios de qualidade, quantidade mínima de exemplos e a necessidade de renumerar as seções quando algumas delas forem opcionais e não utilizadas.

**Pontos de atenção**
- O comando precisa lidar com documentos muito extensos; gerar tudo de uma vez pode estourar a janela de contexto ou a memória.
- A geração deve ser incremental, com apêndices no arquivo, para evitar falhas durante a escrita.
- O volume de saída pode ultrapassar facilmente o mínimo esperado de 1.000 a 1.500 linhas.
- Como o documento pode conter muito código, uma “linha” pode equivaler apenas a uma chave, mas ainda assim o conteúdo total é grande.
- Nem todos os parâmetros precisam ser informados; a IA pode interpretar parâmetros escritos naturalmente.
- Algumas bibliotecas são autopopuladas com padrões da linguagem quando não são explicitamente informadas.
- É importante distinguir o que foi especificado pelo usuário, o que foi autopopulado e o que não se aplica, usando uma estrutura interna em JSON.
- Seções opcionais podem ser omitidas, mas a numeração do documento precisa ser ajustada conforme as seções realmente usadas.
- A pesquisa deve focar em dados essenciais das bibliotecas e tecnologias, sem aprofundar em exemplos para não descaracterizar a guideline.
- A guideline deve consultar fontes oficiais e referências de grandes empresas para dar mais credibilidade e alinhamento técnico.
- Critérios de qualidade, autovalidação e quantidade mínima de exemplos devem ser respeitados para garantir consistência no documento final.