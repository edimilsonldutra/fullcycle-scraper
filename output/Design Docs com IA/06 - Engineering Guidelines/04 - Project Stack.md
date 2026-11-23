Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17228)

## Resumo da aula

Agora para continuarmos de onde paramos, tenho alguns exemplos de guidelines que gerei. Depois mostrarei como vocês podem aplicar no dia a dia e algumas dicas para não partirem do zero. O ponto mais importante em relação a tudo isso é conseguir entender o que é relevante ter no seu projeto ou não.

Obviamente, o que vou apresentar é um exemplo, mas é um exemplo que poderia ser claramente utilizado em um projeto real. Uma das coisas importantes que gosto de resumir logo de cara é a stack. Ao bater o olho, a IA precisa saber imediatamente o que está sendo utilizado. E por que digo isso? Porque não é necessário dar super detalhes de como aquele framework funciona. Imagine que vou criar guidelines para Java com Spring. O ecossistema do Spring é gigantesco. O ponto aqui é ter clareza: quando olhamos para isso, já temos uma versão muito clara do que foi especificado, baseado no meu prompt.

Qual ORM será utilizado? Qual framework web? Como serão feitos os testes? Como trabalhar com o banco de dados? Nesses casos, percebam que tenho a biblioteca e o link para os projetos, o que facilita eventuais referências para que a IA consiga buscar documentações quando precisar fazer consultas e coisas do tipo.

Outros pontos importantes, neste caso específico com Go, são os itens que devem ser incluídos na hora de desenvolver: formatação, linting, logs, build, entre outros. Por que alguns campos aparecem como "auto-populated"? Isso é baseado no comando e no prompt que utilizei, onde passo explicitamente o que será usado. Quando não passo, ele assume como padrão as boas práticas comuns.

A stack é o primeiro ponto que qualquer desenvolvedor ou inteligência artificial, ao olhar, consegue identificar: "É assim que eles estão trabalhando, são essas bibliotecas, esses padrões". Está tudo ok. A partir daí, seguiremos com outros pontos. Alguns serão analisados de forma mais aprofundada, outros apenas superficialmente. Mas é importante entender como cada coisa começa a se encaixar no dia a dia.

## Transcrição

00:00

Bom pessoal, agora pra gente continuar de onde parou, eu tenho alguns exemplos de algumas guidelines que eu gerei, depois eu vou mostrar pra você como você pode aplicar no seu dia a dia e algumas dicas pra você realmente não partir do zero. Agora, qual que é o ponto mais importante em relação a tudo isso? É você conseguir entender

00:22

o que é importante você ter no seu projeto ou não. Obviamente, aqui é um exemplo, mas é um exemplo que poderia ser claramente utilizado dentro de um projeto. Então, uma das coisas importantes que eu gosto de resumir logo de cara. Stack. Aí, a bater o olho, ela tem que saber o que você está utilizando ali de cara, tá? E o porquê que eu estou dizendo isso? Porque você não precisa, necessariamente,

00:46

dá super detalhezinhos de como que aquele framework funciona. Porque imagina que eu vou dar guidelines de Java e daí eu tô falando que eu tô trabalhando com Spring. Meu, o ecossistema do Spring é gigante, tá? Então, o ponto importante aqui é a gente ter clareza de que quando a gente olha pra isso, eu já tenho uma versão muito clara. O que que tá sendo... o que que foi especificado, se foi baseado no meu prompt, tá?

01:09

Mas qual o RM que eu vou utilizar? Qual o framework web que eu vou trabalhar? Como que eu vou testar? Como que eu vou trabalhar com o banco de dados? Então, nesses casos aqui, perceba que eu tenho a minha biblioteca, o link para os projetos, que vão facilitar eventuais referências para que a IA consiga buscar documentações quando ela precisar fazer fetches e coisas desse tipo. Outra coisa aqui são outras...

01:34

pontos mais populares nesse caso aqui com o Go, que isso deve ser incluído na hora de você trabalhar para a parte de desenvolver. Então, como que eu trabalho com formatação, linting, a parte de log, a parte de build e tudo mais.

01:49

Por que aqui está como auto-populated? Isso é muito mais baseado no comando, no prompt que eu acabei colocando, porque aqui eu passo explícito o que eu vou utilizar e aqui ele parte do princípio que, se eu não passei, ele vai utilizar isso aqui como padrão, como boas práticas para serem utilizados. Então, stack é o nosso

02:09

Primeiro ponto que qualquer desenvolvedor ou inteligência artificial que olhar consegue bater o olho e saber, olha, é assim que eles estão trabalhando, são essas bibliotecas, são esses padrões aqui e está tudo ok. Beleza? Aí a gente vai seguir com outros pontos, obviamente alguns pontos a gente vai olhar de uma forma mais profunda, alguns outros pontos a gente vai mais bater o olho, mas é importante você entender como cada coisa começa a se encaixar ali no dia a dia.

## Resumo IA

**Abreviações**  
- **ORM** — *Object-Relational Mapping* (Mapeamento Objeto-Relacional)

**Resumo**  
A aula apresentou exemplos de guidelines geradas para orientar o desenvolvimento e mostrou como estruturá-las para uso no dia a dia, evitando começar do zero. O instrutor reforçou que o ponto central é identificar o que realmente importa incluir em um projeto, de acordo com o contexto e as necessidades reais. O primeiro elemento destacado foi a **stack**, que deve ser evidente logo de início para que qualquer desenvolvedor ou IA entenda rapidamente quais tecnologias, bibliotecas e padrões estão sendo utilizados. Em seguida, foram citados exemplos do que precisa ficar explícito na stack, como o ORM, o framework web, a estratégia de testes e a forma de interação com o banco de dados. Também foi enfatizada a utilidade de incluir bibliotecas e links para documentação e projetos, facilitando consultas futuras pela IA. No caso de Go, o instrutor mencionou ainda itens práticos de desenvolvimento que devem constar nas guidelines, como formatação, linting, logs e build. Por fim, explicou que alguns campos aparecem como “auto-populated” porque foram preenchidos automaticamente com base no prompt/comando utilizado, assumindo boas práticas como padrão quando algo não é especificado.

**Pontos de atenção**  
- Deixar a **stack** clara logo no início para identificar rapidamente tecnologias, bibliotecas e padrões.  
- Não entrar em detalhes excessivos sobre frameworks quando a intenção é apenas orientar o uso geral.  
- Especificar claramente componentes importantes, como:
  - ORM utilizado
  - framework web
  - estratégia de testes
  - forma de acesso ao banco de dados
- Incluir links e referências de documentação para facilitar consultas futuras pela IA.  
- Para linguagens como Go, considerar práticas operacionais essenciais nas guidelines:
  - formatação
  - linting
  - logs
  - build
- Entender que campos “auto-populated” podem refletir padrões assumidos automaticamente quando não há especificação explícita no prompt.  
- Priorizar o que é relevante para o projeto, evitando informações desnecessárias ou genéricas demais.