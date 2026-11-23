Módulo: IA Labs\
Aula: [Skill com MCP](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18282)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, então vamos lá. Dando continuidade aqui,

00:02

agora a gente vai falar sobre como que a gente

00:04

pode criar uma skill que vai consumir um MCP. E aí,

00:09

a gente fazer com que as duas coisas se integrem para que a

00:13

gente consiga atingir um resultado esperado dentro

00:16

da skill que nós estamos trabalhando,

00:18

tá? E para exemplificar isso,

00:20

o que a gente vai fazer? A gente vai fazer o uso do MCP, do GitHub,

00:24

e vamos criar uma skill.

00:27

que vai fazer a triagem de issue que estão abertas ali em determinado repositório,

00:33

tá bom? Obviamente,

00:34

vou gerar aqui alguns dados fakes com o próprio MCP e a

00:40

partir desses dados aí a gente consegue ir trabalhando e tudo mais.

00:44

Acho que o primeiro ponto que tem que ficar muito

00:46

claro é em relação à diferença entre MCP e skill,

00:51

tá? E aí eu gosto sempre de falar o seguinte.

00:55

Quando nós falamos de skill,

00:56

eu estou me referindo a uma habilidade que eu

00:58

quero apartar e reutilizar sempre que necessário.

01:02

Quando eu falo de MCP,

01:04

a ideia do MCP é te dar uma porta para entrar em alguma coisa. Então, no nosso caso,

01:11

aqui é a porta do GitHub para que a gente consiga acessar os nossos dados,

01:16

fazer iterações externas com algum tipo de ferramenta. No nosso caso, o...

01:23

Mas pode ser um banco de dados ou qualquer outra ferramenta que dê o suporte ao MCP,

01:29

que a gente tenha acesso ao MCP. Então, basicamente,

01:32

a skill seria o como e o MCP seria a porta, o nosso acesso.

01:38

Se a gente olhar na ótica desse desafio que a gente está propondo,

01:43

a issue está aberta e pode mudar a toda hora.

01:49

Então, ela nunca...

01:51

vai entrar dentro de uma skill. Ela vai entrar via MCP,

01:56

em tempo de execução. Ou seja,

01:58

ao gerar uma nova issue ou fazer o update de uma nova issue,

02:03

tudo em tempo de execução,

02:04

a skill só irá carregar o procedimento necessário para te dar o resultado esperado.

02:10

No nosso caso aqui, como é uma triagem de issue,

02:13

ela vai carregar o procedimento de triagem e vai me

02:16

dar um relatório do que nós temos em aberto atualmente.

02:21

E para a gente conseguir fazer isso, eu vou utilizar o Docker. Então,

02:26

é muito importante que você tenha o Docker instalado aí na sua máquina, tá?

02:29

Caso você não tenha, super tranquilo de instalar.

02:32

Você pode acessar o próprio site do Docker, docker .com,

02:36

procurar aqui por download e realizar aqui o download

02:40

de acordo com o sistema que você está utilizando.

02:44

Pode também fazer a instalação via linha de comando, enfim,

02:47

da forma que ficar mais viável aí para você, tá?

02:51

Eu já tenho aqui o meu Docker, ok?

02:53

A primeira coisa que eu queria falar com vocês é que o próprio Docker,

02:56

ele já tem um catálogo de MCP Service, tá? Então,

03:00

ele age ali como um gateway que a gente pode utilizar,

03:03

mas para este exemplo em especial,

03:06

A gente não vai fazer o uso desse catálogo de MCP, ok?

03:10

A gente vai fazer a configuração passo a passo ali

03:13

Para vocês entenderem de fato como que utiliza-se um MCP, ok?

03:18

Mas apenas... A cargo aí de curiosidade. Para vocês saberem onde que fica.

03:23

Como é que vocês fazem também para utilizar.

03:25

Vocês podem vir aqui na parte de Settings.

03:28

E buscar por MCP. E aí você vai fazer o Enable.

03:33

Caso não esteja ativado. E vai aplicar. Com isso pronto.

03:37

O que a gente pode fazer? A gente pode vir aqui no MCP Toolkit.

03:40

E aí eu posso vir na parte de Catálogo.

03:43

E entender quais são os itens que eu posso utilizar.

03:47

Basta eu selecionar, colocar as minhas chaves quando há necessidade,

03:50

aí eu já tenho o MCP pronto para utilização diretamente no Docker.

03:56

Mas voltando lá no nosso VS Code, conforme eu disse,

03:59

a nossa ideia aqui é fazer algo um pouco mais passo a passo,

04:03

até para ficar mais claro aí com vocês como é

04:06

que vai funcionar todo esse processo de configuração.

04:10

Vamos lá, então. Primeira coisa que nós temos que fazer é gerar o seguinte,

04:14

gerar o nosso Docker Compose.

04:16

Bom, para gerar o nosso Docker Compose, eu posso pegar isso da internet pronto.

04:20

Tem um monte de exemplo na internet. Eu posso utilizar a LLM. No meu caso aqui,

04:24

eu vou utilizar a LLM.

04:26

E depois também mostro para vocês como é que ficou o resultado.

04:29

Então, gere um arquivo Docker

04:32

Compose com o MCP do GitHub.

04:41

Nomeei como gh-mcp.

04:50

Vou pedir para ele usar aqui o stdin open como true.

04:56

E vou também utilizar o Personal

05:03

Token na Zenv.

05:06

Vamos ver aqui como é que vai ser o

05:09

resultado deste nosso arquivo de Docker-Compose.

05:12

Provavelmente ele vai escrever bem rápido.

05:14

Exatamente como eu imaginei. Então a gente tem aqui o nosso docker-mcp.

05:21

Ok. Vou adicionar também.

05:26

Essa opção aqui. Porque a gente não está utilizando terminal.

05:28

Então vai vir um formato de pipeline. Temos aqui,

05:31

O nosso Personal Access. Que a gente vai,

05:35

Utilizar aí via Enviar.

05:37

Eu posso colocar também um comando. É. Definir aqui Stdio.

05:48

Colocar. Dessa forma. Aqui.

05:51

Show de bola. Depois a gente vai mexer um pouquinho mais nisso aqui. Mas por hora,

05:56

Creio que já vai funcionar. Vamos fazer aqui um teste.

06:01

Um Docker-Compose. Vamos fazer um up.

06:07

Opa, faltou a gente acessar aqui.

06:12

Vou nem colocar "-d". Eu quero ver realmente o que vai acontecer.

06:18

Beleza. Erro esperado, que foi a falta do nosso GitHub Token. Bom,

06:24

para gerar esse nosso GitHub Token é bem simples.

06:27

Vamos voltar aqui no nosso browser.

06:30

Primeiro ponto, você vai precisar ter uma conta no GitHub.

06:34

E aí você vai acessar o seguinte. Vai vir aqui no seu usuário,

06:39

Vai vir em Settings. E aí, quando você vir em Settings,

06:43

você vai descer lá embaixo em Developer Settings.

06:46

E aí você vai acessar o local onde você consegue realizar a criação.

06:51

No meu caso, vou utilizar aqui o Personal Access Token,

06:55

tá? Então já estou com ele aberto aqui,

06:57

vamos utilizar um find granted e aqui eu vou preencher. Então,

07:01

vou colocar aqui Docker, GitHub, MCP, expiration, vamos colocar sete dias só,

07:07

acesso a quais tipos de repositório,

07:10

vamos colocar acesso a todos os repositórios ou se

07:13

eu preferir também posso selecionar somente um repositório, tá?

07:15

E baseado nisso eu vou adicionar as minhas permissões.

07:19

Bom, permissionamento aqui é muito simples,

07:22

né? No nosso caso, a gente vai precisar somente da parte de issue.

07:25

E aí eu escolho se vai ser read only ou read e write.

07:30

Também vou só dar uma olhada aqui na parte do

07:36

repositório.

07:38

Não existe mais.

07:40

Antigamente a gente também tinha que dar acesso ao repositório em si.

07:44

Mas agora já está aqui em cima.

07:47

E eu já consigo ter acesso ao repositório em questão. Beleza.

07:52

Vou gerar esse token. E o que vai acontecer?

07:55

Vou lá no meu VS Code e vou criar aqui um arquivo .env.

08:00

Então, um .env com essa

08:06

informação. Vou jogar o meu token aqui e

08:10

aí a gente provavelmente vai conseguir conectar ao MCP.

08:14

Não vou mostrar essa parte para vocês porque o nosso token é de uso pessoal.

08:19

Então, façam aí e depois retornem na aula.

08:24

Bom, tudo configurado? Vamos fazer o seguinte.

08:27

Vou dar novamente. Vamos ver o que vai acontecer.

08:29

Foi recriado. E olha só. Tudo certo.

08:32

Aparentemente, nós temos aí o nosso container já funcional.

08:36

Se eu retorno aqui no Docker,

08:38

só para vocês darem uma olhada, eu já tenho aqui o meu MCP do GitHub funcionando.

08:45

Beleza? Configuração feita. O que a gente vai fazer agora, galera?

08:49

Vamos fazer com que o Cloud

08:51

Code consiga ler a existência desse MCP. Para isso,

08:57

a primeira coisa que eu vou fazer vai ser retornar no VS Code.

09:00

Já limpei aqui a minha sessão. Inclusive,

09:03

vou precisar sair dela para que a gente consiga adicionar um novo MCP.

09:08

Por quê? Se eu acesso o Cloud Code de novo,

09:12

tomei o MCP,

09:13

você vai perceber que a gente não tem o uso de nenhum tipo de MCP do GitHub.

09:19

Temos aqui alguns que eu já estava utilizando. Então,

09:21

o que nós temos que fazer? Adicionar um novo MCP. Para isso,

09:26

eu vou utilizar o comando chamado Cloud MCP, tá? Então, se eu der um list aqui,

09:31

o que ele vai fazer?

09:32

Ele vai listar todos os itens existentes aqui no MCP,

09:38

que foi adicionado na nossa lista de MCP. Se porventura eu quero adicionar um novo,

09:44

vai ser Cloud MCP Edge. Vou colocar GitHub. Vou definir o meu escopo, tá?

09:50

Vai ser escopo de projeto. E vou colocar aqui um Docker Compose Run.

09:54

que é o formato onde eu quero executar esse MCP server, beleza? Então,

10:01

deixa eu só colocar aqui algumas tags e temos o nome,

10:06

lembrar qual é o nome, GH

10:10

MCP, GH MCP. Então,

10:15

já tenho aqui esse cara adicionado. O que gerou?

10:18

Gerou um MCP.json. Então, se você reparar bem,

10:24

deixa eu até... listar novamente.

10:29

Agora eu tenho o meu GitHub, que foi nomeado ali por mim.

10:33

Temos aqui o tipo, temos o comando e temos a nossa environment.

10:38

Inclusive, aqui eu posso retirar.

10:41

Não tem tanta utilidade neste momento para a gente.

10:45

Bom, eu

10:46

volto para cá, dentro do Cloud Code, numa nova seção.

10:51

Agora eu tenho aqui o meu GitHub MCP.

10:55

A nível de projeto, tá? Scope sempre a nível de projeto.

10:58

Nós temos alguns outros MCPs que são níveis globais também.

11:02

E ele já está conectado juntamente com 41 tools aí que a gente pode utilizar.

11:08

A partir disso, o que a gente precisa fazer?

11:11

A gente precisa apenas trabalhar aí com a geração da skill.

11:15

No nosso caso aqui, o que eu vou fazer? Eu vou criar um ponto Cloud e Skills.

11:22

E eu já vou trazer essa minha skill.

11:26

Pronta para a gente. Issue. Category.

11:35

Deixa eu copiar ela aqui.

11:37

Ela é bem simples. Não tem nada de muito complexo. E aí eu explico ela para vocês.

11:47

Inclusive deixa eu até usar esse mesmo nome aqui.

11:49

Daí a gente já fica todo mundo na mesma página.

11:54

Deixa eu fazer o rename.

11:56

Perfeito. Bom, já tinha gerado. Essa é a skill.

12:01

Anteriormente. Diferenças que nós temos aqui. Nada muito diferente.

12:04

Daquilo que a gente já fez.

12:06

Diversas vezes aqui. O que a gente tem que notar. Primeira coisa.

12:12

Relacionado ao nosso front matter.

12:14

Continuamos utilizando ali. Aquela mesma metodologia.

12:17

Porém em allow tools. Note o seguinte.

12:20

Eu não estou utilizando ali os comandos bash. E sim os comandos de MCP.

12:25

E o que são esses comandos de MCP? Se você.

12:29

Relembrar que junto comigo nós temos 41 tools que estão disponíveis para uso. O

12:36

comando MCP são nada mais, nada menos que tools.

12:40

Então, list, issue, get, issue e search issue, ok? Então,

12:46

eu estou dizendo que a press skill deve utilizar somente essas tools, ok?

12:54

Faço, então, a minha instrução.

12:58

Ponto importantíssimo é...

13:01

Citar o uso do MCP para garantir que ele vai usar o MCP.

13:06

Por quê? Porque assim como a existência de um CLI do GitHub, a existência de API,

13:12

ele pode simplesmente escolher outras formas de acesso.

13:16

Mas com essa configuração que a gente já faz,

13:20

ele vai tender sempre a procurar o MCP de forma primária,

13:27

tendo em vista que é a nossa skill.

13:28

está pedindo isso e não está fazendo referência nenhuma

13:31

à API ou qualquer outro tipo de acesso.

13:35

Em relação a como fazer o uso de um MCP dentro da skill,

13:42

vocês podem perceber que é basicamente instrução. Use o GitHub MCP.

13:47

Não tem nada muito diferente daquilo que a gente já viu.

13:51

Instrução também para eu já subir agentes e coisas relacionadas ali.

13:56

Aos outros exemplos nos quais já trabalhamos, tá? E aí,

14:00

o passo 2 vai ser classificação da issue. Então, P1, P0, P2 e P3.

14:07

Quebra, produção, bug sério, bug de impacto e P3 simplesmente cosmético.

14:14

Depois eu vou fazer,

14:15

detectar aqui coisas que sejam em duplicidade e depois eu tenho um relatório.

14:21

Super simples, nada muito complexo, tá?

14:24

Com isso, o que a gente vai fazer? Primeira coisa, eu vou pedir para

14:30

ele gerar algumas issues para a gente e depois eu

14:33

vou pedir para usar a nossa skill para realizar essa triagem.

14:37

Então, gere algumas

14:40

issues

14:43

no repositório GitHub. Já vou passar aqui qual o repositório, que

14:50

é aquele que a gente estava já trabalhando para

14:56

gerar cada issue layer. A skill.

15:02

Como é o nome da skill.

15:05

Viagem. Issue. Do projeto.

15:11

Analise. As categorias. E baseando-se nelas. Gere.

15:18

Total. De 10. Issues.

15:23

Aí um ponto importante, né? Utilize. O.

15:28

MCP. Do GitHub.

15:31

Então. Estamos vendo aí também como. Trabalhar com o MCP. Dentro.

15:35

Do CLI. Vamos esperar. Entender o que vai acontecer.

15:39

Ele já conseguiu ler ali. A ideia da skill.

15:44

E agora já está utilizando. O MCP. Já estou aqui.

15:49

Utilizando as tools do MCP. Primeiro viu meu perfil. Depois listou ali.

15:55

Assiste. E vamos ver o que ele vai.

16:00

Gerar para a gente.

16:02

Aparentemente. Tudo gerado. Utilizando o MCP. Do GitHub.

16:08

Vamos dar uma olhada aqui

16:11

no nosso browser. Clicar aqui em issue.

16:15

E agora eu tenho diversos pontos aqui a serem analisados pela nossa skill.

16:22

Como eu não pedi para usar a skill, ele só gerou de fato.

16:27

Vamos retornar aqui. E agora o que eu vou fazer? Eu vou utilizar a

16:35

triagem de issues e vou passar...

16:39

o repositório aqui,

16:40

só para a gente ver qual vai ser o processo de triagem. Obviamente,

16:45

como a gente já pode perceber, ele está fazendo o que?

16:48

Utilizando o GitHub. E olha só que bacana.

16:52

Temos aqui o nosso resultado. Então, as prioridades já foram pré-definidas,

16:58

não temos nenhum tipo de label.

17:01

Eu tenho aí os próximos passos,

17:05

que é o meu relatório que foi pedido com os próximos passos.

17:08

Poderia, enfim, pedir aqui para ele já adicionar label,

17:12

definir essas prioridades e colocar descrição, label, autores e tudo mais.

17:18

Inclusive, poderia criar skills para automatizar todo esse processo,

17:23

juntamente com outros MCPs e tudo mais.

17:25

Mas, por ora, a ideia era mais mostrar para vocês como que a gente pode,

17:30

de uma skill, chamar um MCP, como que a gente pode configurar um MCP também.

17:36

E como que a gente faz essa interação aí de forma geral, beleza?

## Resumo IA

[RESUMO_IA]