Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17232)

## Resumo da aula

Estamos aqui dando um exemplo utilizando o Claude Code, mas novamente, comando é comando, prompt é prompt. Se vocês estivessem utilizando outros agentes de IA, teriam basicamente o mesmo resultado. Então, como isso vai funcionar?

Vou digitar meu comando: guidelines-generate, que é o nome do comando. Em seguida, vou passar a linguagem. Vamos imaginar que vou colocar PHP. Depois, vou passar --framework=Laravel, --database=Postgres, --test=PHPUnit. Posso ir além e incluir front-end, por exemplo, --front-end=React ou --front-end=Next.js. Mesmo com esses parâmetros adicionais, o comando vai funcionar. Por quê? Porque esses parâmetros serão extraídos pela IA e farão com que tudo se encaixe. Vale a pena explorar, ser criativo e passar basicamente o que faz sentido para o seu contexto.

Imaginem que vou trabalhar com autenticação em Java. Qual pacote do Spring devo usar? Posso ir colocando esses parâmetros para dar mais clareza nas guidelines.

Então, dou Enter e ele começa a execução. Conforme o processo avança, ele vai gerar aquele arquivo final que mostrei para vocês. Uma coisa importante: vou deixar rodando aqui rapidamente, mas observem que interessante. Ele está mostrando a Fase 0, fazendo o parsing e entendendo a configuração da stack. Lembram daquele JSON interno? Ele colocou a linguagem PHP, framework Laravel, banco de dados Postgres, teste PHPUnit. E já começa a trabalhar.

Reparem que ele fez uma nota: "Front-end frameworks estão outside do PHP scope". É importante notar isso. E ele também identificou outros pontos que fazem parte do mundo PHP e que eu não especifiquei, como a parte de log, que é o Monolog, padrão do Laravel, e o Composer. Tudo isso é autopopulado, são aspectos importantes que qualquer linguagem de programação provavelmente vai precisar.

Gosto muito desse aspecto do comando: mesmo que você não passe algo que normalmente é importante, ele tenta pesquisar e buscar o que é padrão no mercado, autopopulando para a gente. Ele segue para a parte de Research, onde faz uma busca em tudo que estamos trabalhando.

Não tem jeito, ele vai entrar na fase de geração. Observem o que está fazendo: Geração Fase 3.1, ou seja, seções 1 a 8. Por quê? Porque ele não gera tudo de uma vez. Se gerasse tudo de uma vez, poderíamos ter problemas de estouro de memória, travamentos ou outras experiências ruins que tive no passado. Então, ele começa a gerar as seções, as fundações. Ele decidiu quais seções adicionar e, o mais interessante, quais seções devem ser incluídas ou não. Por exemplo, ele não vai incluir concorrência, testes de carga, benchmarks. Tudo que não é nativo da linguagem ou que não tem uma biblioteca popular, ele exclui por padrão. O PHP não tem concorrência nativa.

Obviamente, existem outros casos no PHP em que conseguimos trabalhar de forma excelente com esses recursos, mas isso aqui não é uma aula de PHP. Quero apenas que vocês entendam como aquele prompt faz com que a IA compreenda o que precisa pesquisar, o que vai colocar nas seções, o que não vai, como mapear o que entra, e como gerar a stack final logo no início, indicando o que foi especificado e o que foi autopopulado. A partir disso, ele começa a criar o arquivo.

Esse processo leva um tempo, mas ele segue seção por seção. Bom, eu dei uma pausa aqui, mas quero trazer uma coisa interessante para vocês. Observem que ele está começando a remover conteúdo. Ele está dando exemplos de código e tudo mais. Percebam que há trechos sendo adicionados em verde, mas conforme ele desce, está removendo partes do documento. Por que ele está fazendo isso? Porque ultrapassou o limite de 1.500 linhas. Agora, ele está tentando resumir ou retirar pontos importantes para que o documento caiba dentro desse limite.

Neste momento, ele está fazendo aquela revisão final, avaliando como pode apresentar um contexto completo sobre logs, erros, etc., sem precisar de todo aquele código verboso. Além disso, ele revisa se o que foi colocado anteriormente faz sentido. Percebam que ele está sempre gravando e atualizando o arquivo.

Esse aspecto é muito importante, independentemente de estar gerando um design doc. Na minha opinião, um dos pontos mais cruciais é sempre deixar claro como você quer que a IA faça as validações. Essa é a única forma de conseguir manter um agente rodando por muito tempo. Instruções extremamente claras e uma estrutura onde ele consiga se autoavaliar são essenciais. Se isso não estiver claro, simplesmente não funciona.

Aqui, claramente, ele está tentando chegar perto das 1.500 linhas. Observem: ele continua cortando para se aproximar da meta. Ele persiste, testando até conseguir atingir aquele valor. Finalmente, ele terminou e informou que gerou o documento para a gente. Basicamente, é isso.

Aqui está o documento gerado, as guidelines para PHP. Espero que tenham gostado. Obviamente, vocês terão acesso a todo esse material, a todo esse conteúdo, e principalmente ao comando. Assim, poderão adaptar ou ajustar dentro do projeto de vocês, ou nos novos projetos que forem fazer daqui para frente.

## Transcrição

00:01

Bom, pessoal, então estamos aqui. Estou dando um exemplo utilizando o Cloud Code, tá? Mas, novamente, pessoal, comando é comando, prompt é prompt. Então, nesse nosso caso, se você estivesse utilizando outros agentes de A, você teria basicamente o mesmo resultado, tá? Então, basicamente, como é que isso aqui vai funcionar?

00:20

Eu vou digitar o meu comando, ou seja, vou colocar aqui, barra, guidelines generate, aqui para mim, que é o nome do meu comando. E aí, o que eu vou fazer? Eu vou passar o nome da linguagem. Então, vamos imaginar que eu vou colocar a linguagem aqui, php, vou passar aqui, menos menos framework, é igual a Laravel, vou passar aqui para mim, banco de dados, eu vou falar que é o Postgres, vou falar

00:46

Aqui para mim, o que mais que nós temos que seria interessante a gente poder até colocar no mundo do PHP? Testing, eu vou colocar aqui PHP Unit. E aqui eu posso até ir mais longe, eu posso colocar front-end, por exemplo. Front-end, eu vou colocar React.

01:06

Ou eu posso colocar, sei lá, nextjs. Quando eu faço esses tipos de coisa, ainda assim, o comando vai funcionar. Por que eu estou dizendo isso? Porque esses parâmetros, eles simplesmente vão ser extraídos pela IA e vai fazer com que tudo isso acabe se encaixando. Então, vale a pena você explorar e realmente ser criativo e passar, basicamente, aquilo que faz sentido para você conseguir trabalhar.

01:35

Imagina que eu vou trabalhar com a parte de autenticação no Java. Então, qual o pacote que eu vou passar da parte do Spring? Então, eu posso ir colocando aqui para trazer e dar mais clareza ali nos guidelines. Mas, de forma geral, é isso. Eu dou um Enter.

01:51

e ele vai começar a fazer essa execução. E aí, conforme essa execução vai acontecendo, ele vai gerar aquele arquivo final que eu acabei mostrando para você. Uma coisa importante, vou deixar rodar aqui rapidamente, mas olha só que interessante.

02:08

Ele está trazendo aqui, se você perceber, fase 0. Então, eu vou fazer o parsing e entender a configuração da minha stack. Então, lembra que a gente tinha aquele espécie de JSON interno? Então, ele colocou a linguagem PHP, o framework Laravel, o banco de dados é o Postgres, o test é isso. Então, aqui ele já começa a trabalhar. E se você perceber,

02:32

Olha só que interessante, ele colocou uma nota, o front-end frameworks estão outside do PHP Scope. Então, é importante colocar, mas olha só que interessante. E ele pegou outros pontos que são interessantes, que fazem parte do mundo PHP e que eu não coloquei.

02:48

Ou seja, a parte de log, que é o monologue, que é o padrão do Laravel, de forma geral. Mas olha só o Composer. Então, se você olhar aqui, tudo esse auto-populated são aspectos importantes que qualquer linguagem de programação provavelmente vai ter que ter no meio de toda essa história. Então, eu gosto muito

03:08

desse aspecto da forma como ficou esse comando, porque mesmo que você não passe algo que normalmente é importante, ele tenta fazer a pesquisa e buscar o que normalmente é padrão no mercado e ele autopopula ali pra gente. Então, nesse aspecto, ele segue e aí ele vai pra parte de Research, onde ele sai fazendo uma busca em tudo quanto é coisa que a gente trabalhando aqui pra gente, tá? Então, é essa a ideia.

03:37

E aí, pessoal, não tem jeito. Ele vai entrar na outra fase de geração. E aí, quando ele vai fazer a geração, se você perceber, ele... Olha só o que ele está fazendo aqui. Geração fase 3.1. Ou seja, sessão de 1 a 8. Por quê? Porque ele não vai gerar tudo de uma vez. Porque se ele gera tudo de uma vez, a gente pode ter aquele problema de estressar, de fazer com que a memória...

04:05

tem um estouro de memória, ou trave, ou outras experiências que eu tive no passado, tá? Então, ele vai começar a fazer, vai gerar as sessões, as fundações, se você olhar, ele decidiu aqui quais são as sessões que ele vai adicionar, e o mais interessante, quais sessões que a gente tem que tá inclusa e não está, e o que vai entrar e o que não vai entrar. Então, por exemplo, ele não vai entrar como concorrência, ele não vai trazer a parte de...

04:33

teste de carga, ele não vai trazer a parte de benchmarks, ou seja, tudo que não é nativo da linguagem e que não tem uma biblioteca ou algo tão popular que é utilizado, ele está excluindo ali por padrão. Ou seja, o PHP não tem a parte nativa de concorrência. Obviamente que existem outros casos no caso do PHP que a gente consegue trabalhar de forma linda com isso,

04:57

Mas isso aqui não é uma aula de PHP, mas eu só queria que você entendesse como aquele prompt faz com que ele entenda o que ele vai precisar pesquisar de tudo que ele viu, o que ele vai colocar nas sessões e não vai colocar, como ele vai mapear o que vai entrar.

05:15

e como que ele vai gerar a stack final ali, ou seja, logo no começo, o que vai entrar, o que foi auto-populado, e aí, baseado nisso, ele vai começar a criar o arquivo. E aí, quando ele começa a criar o arquivo, vai demorar um bocado, mas ele vai sessão a sessão para fazer esse tipo de coisa.

05:38

Bom, pessoal, eu tinha dado uma pausa aqui, mas eu queria trazer uma coisa interessante pra vocês. Tá vendo aqui que ele tá começando a remover? Ele tá dando exemplos de código e tudo mais. Não sei se você percebeu que tem coisa que ele tá...

05:53

dizendo que está adicionando tudo em verde, mas conforme ele vai descendo aqui, ele está removendo do documento. Por que ele está fazendo isso? Porque ele bateu mais do que as 1.500 linhas, e agora, o que ele está fazendo? Ele está tentando, de alguma forma, resumir ou retirar pontos que são importantes

06:13

exatamente para quê? Para que o documento caiba dentro de 1.500 linhas. Então, agora ele está fazendo aquela revisão final e falando, olha, como é que eu posso mostrar um contexto inteiro de logs, de erro...

06:27

sem ter que fazer todo aquele código verboso e fora que ele revisa tudo realmente se o que ele tinha colocado antes tá fazendo sentido, tá? E se você perceber, ele tá sempre gravando e colocando isso dentro do arquivo. Então, acho que esse aspecto aí é uma das coisas bem importantes e independente de tá gerando design doc, tá, pessoal? Eu acho que um dos pontos mais importantes aí é

06:53

sempre, de alguma forma, deixe claro como você quer que a IA consiga fazer as validações. É a única forma, na minha opinião, de você conseguir deixar um agente rodando por muito tempo, tá? Ou seja, instruções extremamente claras e forma onde ele consegue realmente se auto-avaliar. Se isso não tiver claro, simplesmente não vai dar bom, tá? Simplesmente isso aí não vai dar bom.

07:22

E aqui, claramente, apareceu, deixa eu tentar chegando ainda perto das 1500 linhas. Olha aqui, deixa eu continuar cortando aqui para eu chegar perto das 1500 linhas. E ele está firme aqui para tentar bater a meta dele de 1500 linhas. Então, ele fica fazendo e fica testando até ele conseguir chegar naquele valor.

07:45

E, finalmente, ele terminou aqui, dizendo que acabou gerando o documento para a gente. Então, basicamente é isso, pessoal. Se você olhar, deve estar aqui o nosso documento que foi gerado.

08:01

em relação à nossa documentação das guidelines aqui do PHP, tá? Então, tá aqui ó, e eu espero que você tenha gostado. Obviamente, você vai ter acesso a todo esse material, a todo esse conteúdo, e principalmente ao comando, e aí você pode adaptar ou ajustar isso dentro do seu projeto ou dentro dos novos projetos que você for fazer daí pra frente, fechou?

## Resumo IA

**Resumo**  
A aula demonstra o uso de um comando do Claude Code para gerar guidelines de projeto, destacando que o comportamento esperado depende mais da estrutura do comando e do prompt do que da ferramenta de IA em si. O instrutor mostra a execução do comando `guidelines-generate` com parâmetros como linguagem, framework, banco de dados, testes e até front-end, explicando que essas informações são interpretadas pela IA para compor a stack do projeto e produzir um documento final coerente com o contexto informado. Durante a execução, a IA realiza uma fase inicial de parsing da configuração, identifica o que foi explicitamente informado e também autopopula itens considerados padrão do ecossistema, como Composer e Monolog no contexto PHP/Laravel. Em seguida, faz uma etapa de research para buscar referências e partir para a geração das seções do documento em fases, em vez de produzir tudo de uma vez, para evitar problemas como estouro de memória, travamentos e degradação da experiência. O instrutor enfatiza que a IA também decide o que incluir e o que excluir, deixando de fora tópicos como concorrência, testes de carga e benchmarks quando não são nativos da linguagem ou não têm ampla adoção. Por fim, a aula mostra a fase de revisão e compactação do conteúdo, em que o agente reduz trechos verbosos e exemplos excessivos para respeitar o limite de 1.500 linhas, mantendo contexto suficiente e atualizando o arquivo continuamente até concluir a geração das guidelines.

**Pontos de atenção**  
- O comando pode variar, mas a lógica é a mesma: comando e prompt precisam estar bem estruturados para qualquer agente de IA.  
- Parâmetros adicionais são bem-vindos e ajudam a IA a entender melhor o contexto do projeto.  
- A fase de parsing identifica linguagem, framework, banco de dados e testes antes de iniciar a geração.  
- Itens comuns do ecossistema podem ser autopopulados, mesmo que não tenham sido informados explicitamente.  
- O agente pode sinalizar componentes fora do escopo, como front-end frameworks em um contexto específico de PHP.  
- A geração é feita em etapas para evitar sobrecarga, travamento ou estouro de memória.  
- A IA também decide o que excluir por padrão, especialmente tópicos não nativos ou pouco relevantes para o stack informado.  
- É importante deixar claro como a IA deve validar o próprio conteúdo; autoavaliação e instruções claras são essenciais para manter o processo estável.  
- Ao ultrapassar o limite do documento, a IA passa a resumir e remover detalhes verbosos para caber na restrição de linhas.  
- O arquivo é atualizado continuamente durante o processo, então a revisão faz parte do fluxo e não apenas do final.