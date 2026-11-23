Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16579)

## Resumo da aula

Skeleton of Thought separa a geração em duas fases: primeiro o modelo produz um esqueleto de tópicos ou seções, depois expande cada parte com detalhes. Essa técnica funciona como um template intermediário que organiza a resposta antes da redação final. O ganho principal não é explorar alternativas, como em Tree of Thought, mas impor estrutura hierárquica à solução. Isso é especialmente útil quando a qualidade da resposta depende mais de organização do que de criatividade livre.

O esqueleto é um artefato de planejamento: ele define quais blocos existirão, em que ordem aparecerão e qual escopo cada bloco deve cobrir. Se esse artefato vier mal definido, a expansão herdará a falha e produzirá uma resposta confusa, incompleta ou redundante. Por isso, nomes de seções ambíguos e tópicos mal recortados tendem a contaminar a etapa seguinte. A técnica exige controlar explicitamente que o modelo não pule direto para os detalhes antes de consolidar a estrutura.

A forma mais explícita de usar a técnica é pedir primeiro o esqueleto e, em seguida, a expansão de cada item. Isso aumenta consumo de tokens, porque a estrutura aparece no contexto antes da resposta final, mas também melhora a coerência local da continuação. Em muitos casos, o esqueleto nem precisa ser exibido ao usuário final; ele pode existir apenas como etapa de geração. Ainda assim, quando o modelo “vê” a própria estrutura anterior, tende a manter melhor a sequência e a cobertura dos tópicos.

Documentação se beneficia muito dessa abordagem porque normalmente falha mais por desorganização do que por falta de conteúdo. Em vez de pedir um texto corrido sobre otimização de query SQL, peça 3 a 5 bullet points e só depois a expansão com exemplos. O resultado tende a separar melhor temas como indexação, SELECT *, JOINs, reescrita de query e plano de execução. Essa ordem transforma uma resposta genérica em uma explicação navegável e mais fácil de revisar.

ADR funciona muito bem com Skeleton of Thought porque já possui uma forma semiestruturada. Retomando o uso de documentação com IA, a novidade aqui é tratar as seções da ADR como o esqueleto obrigatório da resposta: Contexto, Decisão, Alternativas, Consequências e Referências. Primeiro o modelo lista apenas os headers; depois preenche cada seção com o conteúdo da decisão, como a escolha de PostgreSQL em vez de MongoDB. Isso reduz o risco de uma ADR virar texto opinativo solto e força o modelo a produzir um registro técnico legível.

No planejamento de uma API REST em Go, o esqueleto organiza a implementação antes do código. Em vez de pedir “crie um CRUD de produtos”, a instrução define os blocos esperados: structs, framework HTTP, rotas, handlers, validação, camada de banco, tratamento de erro e estrutura de pastas. Depois da estrutura aprovada, cada item é expandido com exemplos de código e boas práticas idiomáticas. Esse fluxo transforma geração de código em planejamento guiado, o que reduz lacunas entre design, implementação e organização do projeto.

Um prompt eficaz delimita papel, tarefa e sequência de geração. Ao instruir um Senior Backend Engineer a responder em dois passos, o modelo primeiro produz bullets como indexação, evitar SELECT *, otimizar JOINs, reestruturar queries e analisar o plano de execução; depois detalha cada item com explicações e exemplos. O valor da técnica está em impedir que todos esses pontos apareçam misturados em um único bloco de texto. A resposta final fica mais auditável e mais fácil de transformar em checklist de revisão.

Ao pedir uma ADR em duas fases, a primeira saída contém apenas a espinha dorsal do documento. Na expansão, cada seção passa a carregar o conteúdo decisório: contexto do sistema, justificativa da escolha, alternativas consideradas, efeitos positivos e negativos e referências usadas. Mesmo com pouco contexto, a estrutura já força uma resposta mais profissional do que um parágrafo livre comparando bancos. O esqueleto, nesse caso, não é só formatação; ele define o tipo de raciocínio documental esperado.

Retomando a ideia de planejamento antes da implementação, o CRUD em Go mostra o esqueleto como mapa técnico do projeto. A primeira fase lista etapas como modelagem com structs, uso de go-chi ou net/http, definição de rotas, handlers, validação com go-playground, acesso a PostgreSQL, error handling e organização em pacotes. A segunda fase expande cada bloco com trechos de código e decisões idiomáticas de Go. O resultado não é apenas “código gerado”, mas uma solução organizada que pode ser revisada, ajustada e usada como plano de execução.

Chain of Thought e Tree of Thought continuam úteis como apoio para explorar raciocínio e alternativas, mas aqui o foco muda para organização da resposta. Depois de explorar possibilidades, o esqueleto consolida a solução em uma sequência implementável. Essa combinação é valiosa quando a aplicação precisa sair da fase de análise e entrar na fase de documentação, design ou implementação. O modelo deixa de apenas pensar sobre o problema e passa a estruturar a entrega.

Skeleton of Thought não corrige falta de contexto nem substitui julgamento técnico. Se o esqueleto inicial estiver errado, incompleto ou ambíguo, a expansão apenas amplifica esse erro. Também há custo adicional de tokens e o risco de o modelo ignorar a separação entre fases e detalhar cedo demais. O uso vale mais a pena quando estrutura, legibilidade e planejamento são mais importantes do que respostas curtas e imediatas.

## Transcrição

00:01

Bom, pessoal, e agora a gente vai pro nosso próximo camarada aqui, tá? Um outro tipo de prompt. Dá pra perceber que a gente tem muito, né, pessoal?

00:11

mas eu acho que quanto mais você pratica, vai sendo natural, até a forma de como você escolhe, até a forma de como você escreve, começa a ser meio que fluente na hora que você trabalha e naturalmente você sabe qual tipo de prompt que você está utilizando. Então, o Skeleton of Thought, ele primeiro cria um esqueleto de tópicos e depois expande cada um.

00:32

Basicamente, ele trabalha como templates para a gente. Então, quando que eu utilizo? Quando eu quero estruturar uma redação antes de eu escrever. Quando eu quero criar uma ADR, uma Architecture Decision Record. Quando eu preciso planejar endpoint de uma API antes de sair codificando. Quando eu quero organizar um artigo em sessões e depois detalhar. Quando eu quero fazer uma checklist de alguns requisitos antes de analisar tudo. Então, qual que é a limitação?

00:58

Um esqueleto ruim leva a uma expansão ruim. Por que uma expansão? Porque cada tópico que ele coloca ali no esqueleto, ele vai expandir para trazer a resposta, tá? Ele pode perder o contexto entre etapas, tá? Isso aí é um problema, porque ele pode misturar uma etapa com a outra...

01:14

principalmente se a seção que você está pedindo para ele criar tem um nome um pouco ambíguo, tá? Pode confundir um pouco com outro. Vai ser mais tokens, obviamente, né? Exige um controle para ele não pular direto para os detalhes, ou seja, às vezes ele sai detalhando e ele não segue necessariamente aquele esqueleto como você pré-definiu.

01:34

E a saída nesse caso vem em duas fases. O que significa? Primeiro você mostra o esqueleto e depois você traz o resultado. Por outro lado, não necessariamente você precisa imprimir o esqueleto.

01:49

No prompt, você pode pedir apenas o resultado. Quando você imprime o esqueleto, fica mais claro para a IA o próximo token do esqueleto que ele tem anterior, então ele tende a ter uma resposta melhor, mas não necessariamente você precisa trazer o esqueleto antes de trabalhar. Você consegue ter resultados muito bons sem trazer o esqueleto, mas o esqueleto é essencial no ponto da própria IA

02:17

vê o que ela já trouxe do esqueleto passado, ou seja, para ela calcular o next token no final das contas. Então, ela vê o que ela escreveu antes, ajuda ela a ver o que ela vai trazer depois. Se você não trouxe o esqueleto, ela perde esses tokens do esqueleto e não necessariamente ela pode trazer a melhor resposta do mundo.

02:38

Mas eu vou ser honesto com vocês, galera. Na maioria das vezes, quando eu vou trabalhar com isso, eu não trago o esqueleto antes, tá? Somente para vocês saberem, na maioria das vezes eu não faço isso. E eu vou mostrar como é que a gente pode trabalhar agora com o Skeleton of Thought. E eu adoro isso para a gente trabalhar com documentação, cara. Documentação e Skeleton of Thought ajuda demais, tá? Então, o lance é o seguinte. Esse aqui vai ser o exemplo que eu criei.

03:04

E vamos ver aqui como é que a gente tem. Seguinte, você é um Sênior Backend Engineer, um Júnior Developer perguntou como que você pode otimizar uma Query SQL para performar melhor. Siga o seguinte esqueleto de pensamento, o Skeleton of Thought, do seguinte approach. Passo 1, gere somente o esqueleto

03:28

com a sua resposta de 3 a 5 bullet points, certo? Passo 2. Expanda cada bullet point de uma forma clara e detalhada, explicando com exemplos.

03:44

tenha certeza que a resposta final vai ser estruturada de uma forma simples de seguir. Essa é uma forma de você trabalhar com o Skeleton of Thought. Por quê? Porque eu pedi para ele gerar como esqueleto antes para mim os meus bullet points. E depois ele vai explicar esses bullet points que ele gerou no esqueleto

04:02

expandindo isso. Então, isso é uma forma de Skeleton of Thought, tá? Agora aqui, mensagem 2. Você é um arquiteto de software, você quer produzir um Architecture Decision Record, ou seja, uma ADR, para escolher o Postgres ao invés do MongoDB, tá? Siga o seguinte esqueleto.

04:21

Primeiro, gere somente o esqueleto da ADR com as suas sessões, com os headers da ADR, sem nenhuma explicação. Segundo, use os padrões de ADR com as cinco sessões, contexto, decisão, alternativas, considerações, consequências e referências.

04:42

Passo 2. Depois de mostrar esse esqueleto, expanda cada seção detalhando claramente o conteúdo. Mantenha como final uma ADR profissional, estruturada e fácil de ler. Ou seja, eu estou botando como ele poderia trabalhar com o Skeleton of Thought seguindo uma ADR. E aqui por último, você é um desenvolvedor sênior em Go

05:04

você quer me ajudar a criar uma API REST para gerenciar produtos, uma API de produtos, gerenciamento de produtos em Go. Para isso, siga o seguinte esqueleto. Primeiro, gere o esqueleto com uma solução entre seis a oito bullet points. Esse esqueleto deve cobrir o modelo de dados definido em Go com as structs, a escolha do framework HTTP,

05:32

Routing, Handlers, Validation, Database Layer, Error Handling, estrutura de projetos, e ainda não expanda. Perceba que eu só pedi para ele gerar o esqueleto.

05:46

Passo 2. Expanda cada bullet point de forma clara e detalhada com exemplos e com boas práticas de Go. Inclua exemplos de código, como as structs, os handlers e as rotas, considerando os pacotes como o Go-Chi, o nethttp, aqui a gente está falando de Go, né? Como fazer o error handling em Go, idiomático, como organizar o projeto em pacotes e tudo mais, tá? Use uma forma concisa e profissional de linguagem.

06:15

A API precisa ser implementada com as operações de CRUD para os produtos com os campos ID, Nome, Descrição, Price e Stock. Então, aqui está três exemplos com nível de complexidade diferentes usando o esqueleto de pensamento que a gente colocou aqui para a gente. Então, eu vou fazer o seguinte, galera. Eu já vou botar os três de uma vez e depois a gente olha um a um.

06:41

Porque daí fica mais fácil, ao invés de ficar fazendo uma execução para cada coisa. Então, vamos lá. Python, 1, 5, aqui, Skeleton of Thought, aqui para a gente. E mandei colocar com GPT-4o, tá? Vamos lá.

07:01

Vai demorar um pouquinho, porque tem bastante coisa para escrever, porque são três chamadas, e cada chamada é longa, de forma geral. Então, vamos aguardar um pouquinho esse cara sair. Prontinho! Então, vamos lá em cima agora, porque são bastante coisas aqui que a gente colocou. A gente está aqui... Vamos ver em qual momento que a gente está. Aqui...

07:32

é a resposta do Skeleton of Thought. Aqui. Beleza. Show de bola. Então, primeiro ponto, o Senior Backend Engineer para otimizar queries SQL, fazer o esqueleto e etc. Foi o que a gente leu. Então, passo 1, Skeleton of Thought.

07:48

indexação, fazer avoiding SELECTs, otimizar joins, reorganizar, reestruturar queries e analisar o plano de execução de query. E aqui passa o 2, a explanação, a explicação expandida. Então, a parte de indexing, que é o primeiro bullet point, ele trouxe a explicação. A indexação, nesse jeito, e aqui ele trouxe um exemplo da indexação.

08:19

a evitar SELECTs. Usando o select asterisco de todas as colunas pode gerar isso. Exemplo. Joins, mesma coisa. Queries, mesma coisa. Analyzing, mesma coisa. Então, se você perceber, ele gerou essa estrutura e agora ele responde expandindo essa estrutura aqui pra gente.

08:38

Agora a gente tem o segundo, você é um software arquiteto, eu quero que você faça uma ADR, um Architecture Decision Record, ele pedir primeiro o esqueleto com os headers, baseado nas seções, e aqui está a resposta. Então, primeiro passo, skeleton, contexto, decisão, alternativas consideradas, consequências e referências.

08:58

Aí, agora, ele vai expandir a decisão. Contexto. No desenvolvimento de uma nova aplicação, você precisa de soluções de banco de dados, são complexas, integridade, etc. Nosso time está decidindo pelo PostgreSQL, que é um banco de dados relacional, e o MongoDB, com flexibilidade no SQL, etc. Decisão. A gente escolheu o PostgreSQL por conta que ele foi um...

09:23

um ecossistema mais maduro, tem etc, não que o Mongo não tenha também, e etc e tal. Alternativas consideradas, ele trouxe o Mongo, o MySQL e o SQLite, consequências positivas e consequências negativas, e as referências dessas informações que foram trazidas ali para tomar essa decisão. E ele coloca, essa é uma ADR, informando as decisões dos bancos de dados de escalabilidade, etc.

09:53

Então, olha só como ele criou uma ADR bem estruturada, de forma geral, independente se eu concordo com ela aqui ou não, a gente deu pouco contexto, mas a ideia é que você consiga ver o poder que está na sua mão somente de você conseguir fazer esses ajustes no prompt. E, por último, é o mais difícil, que é ajudar eu criar um esqueleto de pensamento para me ajudar a desenvolver

10:19

um gerenciamento, um CRUD, de produtos em Go, tá? Então, eu pedi pra ele seguir, né, expandir os bullet points, e aqui tá a API, tem que implementar, eu falo os campos da API. Então, olha só, ele separou em oito etapas.

10:33

modelagem e definição das structs no Go, escolha do framework HTTP, fazer a parte de rota, depois criar os handlers, depois fazer as validações, depois a parte de banco de dados, depois validação de erro e depois a estrutura do projeto.

10:51

E aqui, a detalhação. Então, aí ele trouxe aqui o detalhamento. Ele trouxe aqui a definição das structs, definir o data model do produto e etc. Daí ele trouxe o exemplo do código de como é que é uma struct aqui em Go.

11:06

HTTP, usar o Go-Chi (Chi). Ele mostrou como é o import do Go-Chi para você trabalhar com isso. Roteamento, define as rotas. Ele pega o Go-Chi e coloca aqui para mim as rotas do CRUD de como vai ser implementado no Go. Handlers, como vai ser as funções que vão ser executadas no meu produto.

11:27

4. Validação. Ele trouxe ali uma biblioteca de validação do Go Playground aqui e mostrar como é que valida uma struct. Beleza. Database Layer. Usar um SQL Banco de Dados como um PostgreSQL aqui da vida, criar um pacote. Daí ele deu um exemplo de importando o pacote SQL, fazendo a inicialização do banco de dados com PostgreSQL, definindo as funções do banco de dados.

11:51

Aí, Error Handling, né? Fazer erros, tratar os erros dentro, provavelmente, dos meus controllers, dos meus handlers aqui pra mim. E a estrutura do projeto, como que ele organizou as pastas aqui pra mim, como é que ele fez. Galera...

12:08

Isso te lembra alguma coisa na hora que você vai tentar pedir pra IA desenvolver algum software pra você, em relação à produtividade? Na hora de você pedir pra ela gerar contexto ou pra você instruir ela passo a passo de como que ela deve seguir com o processo de desenvolvimento do seu software?

12:25

Imagina o quão rico é você explorar linhas de pensamento com Chain of Thoughts e com Tree of Thoughts, depois, baseado nisso, você criar um esqueleto dos passos que ela pode utilizar para resolver esse problema e ela gerar essas sugestões, você pode argumentar, ajustar e usar isso como um plano de ação para ela sair implementando isso ali na sua ideia, por exemplo.

12:52

Você entende como é rico. E esses prompts, se você perceber, eles não são grandes. Concorda comigo? Não são prompts malucos e grandes. São prompts que, intencionalmente, eles conseguem gerar esses resultados que, na minha opinião, são fantásticos e que mudam o jogo na hora que você vai programar.

13:10

Eu espero, eu realmente, do meu coração, eu espero que você esteja assistindo isso e pensando como que você pode implementar isso hoje no seu dia a dia, na hora que você estiver trabalhando e programando. Então, vimos agora aqui, Skeleton of Thought.

## Resumo IA

**Abreviações**
- **ADR** — *Architecture Decision Record* (Registro de Decisão de Arquitetura)
- **SQL** — *Structured Query Language* (Linguagem de Consulta Estruturada)
- **CRUD** — *Create, Read, Update, Delete* (Criar, Ler, Atualizar, Excluir)
- **HTTP** — *Hypertext Transfer Protocol* (Protocolo de Transferência de Hipertexto)
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **Go-Chi / Chi** — framework leve de roteamento HTTP para Go
- **JWT** — não mencionado na aula
- **MongoDB** — banco de dados NoSQL orientado a documentos
- **PostgreSQL** — sistema gerenciador de banco de dados relacional

**Resumo**
A aula apresentou a técnica **Skeleton of Thought**, um padrão de prompt em duas fases no qual o modelo primeiro cria um esqueleto estruturado de tópicos ou seções e depois expande cada parte com detalhes. O objetivo principal não é explorar múltiplas alternativas, como em Tree of Thought, mas impor organização hierárquica à resposta, tornando o conteúdo mais coerente, auditável e fácil de revisar. O instrutor destacou que essa abordagem funciona muito bem quando a qualidade da saída depende mais de estrutura e legibilidade do que de criatividade.

Foi explicado que o esqueleto atua como um artefato de planejamento: ele define a ordem dos blocos, o escopo de cada seção e a cobertura esperada. Se esse esqueleto vier mal definido, a expansão tende a herdar os mesmos problemas, produzindo respostas confusas, incompletas ou redundantes. Também foi ressaltado que nomes ambíguos de seções e tópicos mal recortados podem contaminar a etapa seguinte, além de exigir controle para que o modelo não pule direto aos detalhes antes de consolidar a estrutura.

A técnica foi demonstrada em contextos práticos de documentação e desenvolvimento de software. Em documentação, o instrutor mostrou como pedir primeiro 3 a 5 bullet points e depois expandi-los, evitando respostas genéricas sobre temas como otimização de SQL e separando melhor itens como indexação, SELECT *, JOINs, reescrita de queries e análise de plano de execução. Em arquitetura, foi apresentada a construção de uma ADR com headers obrigatórios — contexto, decisão, alternativas, consequências e referências — para evitar textos opinativos soltos e gerar um registro técnico mais profissional.

Outro exemplo foi o planejamento de uma API REST em Go para gerenciamento de produtos. Em vez de pedir “crie um CRUD”, o prompt orienta o modelo a primeiro gerar o esqueleto com blocos como modelagem com structs, escolha do framework HTTP, rotas, handlers, validação, camada de banco, tratamento de erros e estrutura do projeto. Depois, cada item é expandido com exemplos de código e boas práticas idiomáticas. O fluxo apresentado transforma a geração em planejamento guiado, aproximando design, implementação e organização do projeto.

O instrutor também comparou essa abordagem com Chain of Thought e Tree of Thought: essas técnicas continuam úteis para explorar raciocínio e alternativas, mas aqui o foco muda para consolidar a solução em uma sequência implementável. Skeleton of Thought é especialmente útil quando a entrega precisa sair da fase de análise e entrar na fase de documentação, design ou implementação, deixando a resposta mais navegável e fácil de transformar em checklist ou plano de ação.

**Pontos de atenção**
- Um **esqueleto mal definido** gera uma expansão igualmente ruim.
- **Seções com nomes ambíguos** podem confundir o modelo e misturar tópicos.
- Há risco de o modelo **perder contexto entre as fases**.
- A técnica costuma **consumir mais tokens** do que uma resposta direta.
- É importante controlar para o modelo **não pular direto para os detalhes** antes de fechar a estrutura.
- O esqueleto pode existir **sem ser exibido ao usuário final**, mas mostrÁ-lo ao modelo tende a melhorar a coerência da resposta.
- **Skeleton of Thought não substitui julgamento técnico** nem corrige falta de contexto.
- Funciona melhor quando **estrutura, legibilidade e planejamento** são mais importantes do que concisão extrema.
- Em documentação e arquitetura, prefira **headers e tópicos bem recortados** para evitar respostas genéricas.
- Em prompts de código, deixar explícitos **papel, tarefa e sequência de geração** melhora muito a qualidade da saída.