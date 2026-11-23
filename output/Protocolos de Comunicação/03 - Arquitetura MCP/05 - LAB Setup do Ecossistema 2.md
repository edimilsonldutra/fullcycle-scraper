Módulo: Protocolos de Comunicação\
Aula: [LAB: Setup do Ecossistema 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18596)

## Resumo da aula

A validação ponta a ponta depende de infraestrutura real, não de mocks isolados. Por isso, o fluxo começa com Docker Desktop ativo, credenciais de modelo em .env e um GitHub Personal Access Token já configurado. O seed operacional do Postgres cria um cenário verificável com 10 clientes, 30 pedidos e um subconjunto de pedidos com falha, o que permite testar correlação entre sistemas com um resultado esperado. A ausência inicial de issues sobre pedidos no GitHub não é um erro do experimento; ela define um caso legítimo de não interseção.

O banco PostgreSQL rodando em container não é, por si só, um server MCP. Ele continua sendo apenas a infraestrutura de dados; a superfície MCP surge quando um server específico encapsula esse banco e publica resources e tools sobre ele. Essa separação importa porque o recurso consultado pertence ao domínio, enquanto o server é a camada de protocolo que traduz esse domínio para contratos consumíveis pelo client. Na prática, isso evita confundir “onde os dados vivem” com “como as capacidades são expostas”.

No primeiro client customizado, o server MCP do Postgres é iniciado por npx, baixado dinamicamente como um processo Node local. O ponto central não é Node em si, mas o fato de o client Python conversar com esse processo via stdio, sem depender de HTTP, SDK proprietário ou embedding manual de integração. Retomando o cenário de pedidos com falha, isso permite consultar o schema e executar queries reais no banco sem acoplar o host ao driver interno do server. O Inspector, já conhecido, entra aqui apenas como prova de contrato antes da execução via Python.

Inspecionar resources e tools antes de rodar o client reduz ambiguidade de diagnóstico. Se o schema das tabelas clientes e pedidos aparece corretamente e a tool de query responde no Inspector, o problema deixa de ser “o server não sobe” e passa a ser “como o client ou o agente estão usando esse contrato”. Esse passo é especialmente útil em laboratório multi-etapas, porque separa falha de transporte, falha de contrato e falha de raciocínio do agente. O resultado simples de contar 10 clientes confirma que a cadeia Postgres → server MCP → client Python está íntegra.

O mesmo transporte stdio funciona tanto para um server iniciado por npx quanto para um server empacotado em Docker. Essa independência entre empacotamento e transporte é um dos pontos mais operacionais do ecossistema: o host não precisa saber se o processo remoto é um binário local, um script Node ou um container. No caso do GitHub MCP, a troca de npx por docker -i altera o modo de empacotar e distribuir o server, mas não altera a forma como o client conversa com ele. Isso preserva a interface de integração mesmo quando a estratégia de runtime muda.

O salto arquitetural ocorre quando um único client conecta simultaneamente Postgres e GitHub MCP. Lembra do fanout já estabelecido: aqui ele deixa de ser apenas conceito e vira orquestração concreta, com uma pergunta que exige leitura em dois domínios e síntese posterior. O client multi-servidor não funde os sistemas entre si; ele mantém dois contratos independentes e delega ao agente a composição da resposta. Essa abordagem reduz glue code manual, mas transfere parte do risco para a qualidade da navegação e das chamadas feitas pelo agente.

Ter schema exposto e tool funcional não garante que o agente gerará SQL correto. No experimento, o agente tentou colunas inexistentes como p.numero_pedido e p.data_pedido, o que mostra um limite importante: contrato reduz erro, mas não elimina inferência equivocada. Esse tipo de falha é valioso porque revela a diferença entre “capacidade disponível” e “uso correto da capacidade”. Em produção, isso pede mitigação com prompts mais restritivos, exemplos de query, validação intermediária ou camadas adicionais de proteção no server.

Quando o cruzamento entre issues abertas e pedidos com falha não encontra correspondência, o sistema ainda produziu uma resposta correta. Esse caso é importante porque evita a expectativa errada de que integração multi-servidor sempre precisa retornar uma correlação positiva para “dar certo”. Retomando o cenário original, descobrir sete falhas no banco e zero tickets relacionados no repositório é uma conclusão operacional útil: existe problema no domínio de pedidos, mas ele não foi reportado naquele sistema externo. A ausência de interseção, portanto, é evidência, não vazio semântico.

Para produzir uma interseção real, foi criado um seed do GitHub que gera um repositório fake e três issues citando pedidos com falha. Esse seed não depende obrigatoriamente do server MCP; ele pode chamar a API do GitHub diretamente, desde que prepare o estado externo necessário para o experimento. A ideia central é tornar o laboratório reproduzível: o aluno deixa de depender do acaso do mundo real e passa a trabalhar com um cenário controlado, no qual a correlação esperada pode ser conferida. Seed operacional, aqui, é preparação de ambiente para teste de integração, não apenas carga inicial de banco.

Delegar ao agente a criação de scripts, repositórios e issues acelera a montagem do experimento, mas isso não transforma o processo em automação irrestrita. O uso produtivo de vibe coding exige escopo pequeno, credenciais controladas e capacidade de revisar o que o agente decidiu fazer, inclusive quando ele escolhe chamar a API diretamente em vez de reutilizar um server existente. O ganho está na velocidade de execução de tarefas mecânicas; o limite aparece quando a decisão do agente afeta segurança, custo ou consistência do ambiente. Sem esses freios, a conveniência vira risco operacional.

Depois de semear o repositório fake, a mesma orquestração multi-servidor passa a encontrar três issues abertas e correlacioná-las com pedidos realmente marcados como falha na base. O resultado final confirma os pedidos 2, 14 e 28 como presentes nos dois lados e ainda identifica quatro falhas adicionais não mencionadas nas issues. Esse desfecho mostra a utilidade prática da composição entre servers: a resposta relevante não está isolada nem no banco nem no GitHub, mas no cruzamento governado entre ambos. O valor do MCP aparece justamente quando a integração deixa de ser adapter artesanal e vira fluxo verificável de protocolo.

## Transcrição

00:00

Vamos lá pessoal, vamos agora no nosso walkthrough do laboratório,

00:06

do laboratório 13.

00:08

Então, vamos começar aqui. Importante, pessoal,

00:14

garanta que o Docker Desktop está rodando e que você possui um .env,

00:20

ou seja, ou com a API da Anthropic ou com a API da OpenAI, tá bom?

00:26

Com uma, desculpa, com uma API Key da Anthropic ou com uma API Key da OpenAI, tá?

00:32

E, obviamente, ter configurado lá o seu GitHub Personal Access Token,

00:37

tá? Essas informações, pessoal,

00:38

elas estão disponíveis aqui no README, tá? Então,

00:42

fique super à vontade depois e, na verdade,

00:45

fortemente que vocês acessem aqui e peguem as

00:50

informações necessárias para vocês poderem rodar o Lab, tá bom? Bem...

00:57

Vamos começar aqui, deixa eu só dar o CD aqui para o

01:05

diretório correto, estamos no diretório correto,

01:08

então vamos lá. Primeira coisa, pessoal,

01:10

para testar o MCP de verdade, nós precisamos de infraestrutura real,

01:14

então vamos começar subindo o banco de dados PostgreSQL no Docker,

01:18

e populando ele com dados do nosso negócio, nosso sistema fictício.

01:24

Então, só para vocês terem uma ideia,

01:27

e nós vamos abrir aqui, tá? O que seria o CID, tá bom? Aqui para

01:32

você, tá? Então, nossa carga inicial ela tem 10 clientes e 30 pedidos de e-commerce,

01:38

tá? Também tem os clientes, aqui, tem 10 clientes e 30 pedidos de e-commerce,

01:42

tá? Alguns desses pedidos falharam, tá? Estão com status

01:46

de falha. Para nossa simulação final ser realista,

01:49

o nosso repositório no GitHub deve ter zero issues tratando problemas com pedidos.

01:54

Nossa conclusão de sucesso ao final da aula será descobrir que X pedidos falharam,

02:00

mas nenhum ticket foi aberto. Vamos

02:04

lá. Vamos agora subir o Docker e popular com o CID. Vamos

02:14

subir o Docker.

02:17

Beleza, então ele subiu, tá?

02:18

Agora a gente aqui tem um banco de dados. Opa, opa, opa.

02:23

Temos aqui o nosso pôster que está funcionando, tá? 11 segundos atrás, beleza?

02:29

Bem, agora a gente vai instalar as dependências do Python que

02:36

a gente vai precisar usar para poder rodar o nosso cliente, tá bom? Então...

02:43

Beleza, então agora o que a gente vai fazer, pessoal?

02:45

Nós vamos configurar o PostgreSQL MCP no nosso host,

02:48

que é no nosso cliente personalizado, tá?

02:53

Então, para isso, pessoal, como agora nós temos o banco de dados rodando,

02:57

mas ele é apenas um banco comum no Docker, tá?

03:02

Então, como que conectamos um agente de A nele?

03:05

A gente usa um servidor MCP. Então, vamos olhar o nosso primeiro orquestrador aqui,

03:10

pessoal, que é esse Custom Client 1 Postgres, tá? Então,

03:16

aqui é o seguinte. Então, o que ele vai fazer?

03:19

Ele vai... Antes de... Deixa eu ir aqui para baixo, para as configurações.

03:25

Desculpa, aqui no main, tá? Então, vamos lá.

03:29

Veja o comando aqui, pessoal.

03:31

NPX com esses argumentos. Então, repare que o servidor MCP não está no Docker.

03:37

Ele é um script Node baixado dinamicamente que conecta no nosso banco de dados.

03:41

Então, ele se comunica de volta com o nosso código cliente pela saída padrão STDIO.

03:47

Então, inspecione.

03:50

Vamos agora. Para provar a capacidade do servidor, nós podemos usar o Spectre MCP.

03:56

Então assim, primeiro vamos rodar o Spectre MCP aqui para ver,

04:03

para garantir que ele está funcionando bonitinho, tá?

04:06

Que o MCP server está funcionando.

04:10

Então vamos pegar aqui, ele abriu aqui outra tela, gente,

04:16

que eu tenho aqui aberta. Deixa eu colar aqui, para

04:24

ter certeza que eu peguei certo.

04:34

Beleza, vamos conectar. Conector.

04:38

Vamos ver a lista de resources.

04:40

Lembra que eu falei para vocês? Nós temos dois resources.

04:43

Ele tem o resource do esquema da tabela

04:49

Clientes e o resource do esquema da tabela Pedidos.

04:53

E no caso aqui, nós temos uma tool só,

04:56

que é a tool de query. Select asterisco com clientes.

05:04

Tá vendo? Mandei listar todos os pedidos. Então,

05:07

eu estou acessando o banco de dados através de um MCP Server, tá bom?

05:13

Ou seja, é que ele está simulando o meu client, o meu host.

05:16

Na verdade, o meu client, tá? Que é o MCP Spectre. Beleza. Voltando aqui na IDE.

05:24

Eu vou abrir mais uma janelinha aqui, pessoal. QCD. Beleza.

05:35

Vamos voltar aqui no meu roteirinho, tá? Então, olha só.

05:38

Então, a gente viu executando, tá? Só que assim,

05:41

então agora, a execução do orquestrador,

05:43

tá? Então, o que a gente vai fazer? Nós vamos executar o orquestrador Postgres.

05:50

Ah, aqui, ó. Fecha o Spectre e vamos rodar isso via Python. Então,

05:54

vamos rodar via Python, tá bom? Aqui, eu tinha anotado aqui,

05:56

vamos lá. Então, para eu lembrar, tá? De fechar o Spectre, tá?

05:59

Já está aqui, está fechado aqui, tá? Vou fechar aqui o Spectre.

06:04

Vou derrubar ele aqui também. Pode ser. Não tem problema não.

06:08

E vamos fazer esse negócio funcionar. Então, vamos rodar aqui o client.

06:13

Olha lá. Então, olha só.

06:15

O que ele está fazendo, pessoal? O que o client 1 está fazendo? Ele vai pesquisar.

06:20

Vamos ver o que ele vai fazer. Consulte o banco de dados.

06:23

Quantos clientes nós temos cadastrados na tabela cliente?

06:26

Então, olha só. Essa aqui é a pergunta.

06:29

Resultado, 10 clientes. Então, perfeito.

06:32

Então, o que a gente fez?

06:34

Nós subimos o banco de dados no Docker,

06:41

ou seja, o nosso banco de dados roda no Docker.

06:44

Não o MCP7 roda no Docker, tá? O banco de dados roda no Docker.

06:49

O MCP7, ele é rodado,

06:53

ele é executado localmente via comando NPX.

06:57

É como se ele instalasse aqui localmente e

06:59

a gente consegue executar via STD ou padrão, tá bom?

07:04

Agora o que a gente vai fazer? Agora o protocolo é universal.

07:08

Se acabamos de usar um servidor Node,

07:11

agora nós vamos plugar um servidor do GitHub. E detalhe, empacotado diferentemente.

07:19

Então vamos abrir aqui, só para vocês verem,

07:21

o client conectando no GitHub.

07:27

Nesse caso aqui, vamos dar uma olhada.

07:39

O transporte continua sendo stdio só que a gente só que a gente vai só que

07:44

A gente vai usar o comando Docker, tá? O comando Docker então seja então olha.

07:49

Só dessa vez a configuração ela não usa npx, mas sim Docker -i, tá? É o

07:55

servidor MCP do GitHub vive dentro de um container.

07:58

isolado, tá? Graças ao transporte universal por STDIN.

08:02

O nosso host em Python não faz ideia,

08:04

nem se importa se o servidor está no container ou se é binário local.

08:08

Então, vamos fazer a execução do orquestrador GitHub.

08:12

Olha só. Vamos rodar essa etapa.

08:15

Nós estamos inspecionando agora o GitHub e mandando

08:19

o LLM listar três repositórios mais populares do protocolo.

08:29

Olha lá. Quais são os três repositórios mais populares do Model Context Protocol?

08:35

Então, olha só. O primeiro é o Servers com 86 mil estrelas.

08:40

O segundo é o Python SDK com 23 mil estrelas.

08:43

E depois o TypeScript SDK com 12 mil estrelas, tá? Só de curiosidade,

08:49

pessoal, nós vamos usar esses dois aqui muito no próximo módulo, tá?

08:54

Agora, o que a gente vai fazer? A gente vai fazer uma tarefa combinada, tá?

08:58

Ou seja, nós chegamos no momento a raça. Ou seja, vamos combinar dois mundos, tá?

09:02

E nós vamos abrir, vamos abrir aqui o Custom o três, tá? Que esse cara aqui, ó, é

09:09

que é que de novo, tá, gente? Ele tá simulando o quê? Um Cloud Code, o Caldo

09:14

Desktop e faz que a gente só, que eu tô mostrando aqui por baixo do capô, que é muito

09:18

mais interessante para a gente, tá? É ao invés

09:21

de simplesmente usar um cara pronto, tá bom? Então, vamos

09:25

ver aqui, parar aqui, que ele vai fazer, tá? Ó.

09:28

Ele vai conectar, ele vai conectar tanto com POST

09:33

quanto com o GitHub, dessa vez, tá?

09:35

Um cliente conectando com os dois MCP servers ao mesmo tempo, tá?

09:38

E vamos

09:42

dar o seguinte: missão impossível para a gente.

09:45

Verifique se há issues abertas no nosso repo mencionando pedidos, tá?

09:51

Depois, cruze com a nossa tabela de pedidos do banco

09:54

de dados e veja quantos pedidos têm falha,

09:57

tá bom? Então, vamos executar aqui, cara.

10:21

Obviamente, não vai ter, pessoal. A gente sabe que não vai ter.

10:25

Porque não tem lá. Vamos ver lá.

10:28

Verifique se há issues abertas. Ele está usando o search.

10:32

Está fazendo uma query. Tem um erro na ferramenta.

10:36

P número pedido não existe.

10:39

P data de pedido também não existe.

10:43

E aqui ele está mostrando. Está vendo?

10:46

O Cloud decidiu usar a ferramenta search issues. Depois, a ferramenta query.

10:50

Vamos ver, ele ainda está fazendo aqui. Vamos ver.

10:57

Olha só. Cruzamento de dados. Então, olha só.

11:00

Encontrei sete pedidos com status de falha associados aos seguintes clientes.

11:04

Todos esses pedidos aqui.

11:06

Não há correspondência entre as issues abertas no GitHub e

11:09

os pedidos com falha no banco de dados.

11:11

Isso significa que nenhum desses pedidos falharam.

11:16

Falhados foi reportado com isso no repositório

11:19

de servidores do Model Context Protocol. Obviamente, que não.

11:23

A gente podia até melhorar esse exemplo.

11:27

Eu posso ver se eu melhoro para a próxima turma.

11:29

Mas no final do dia, pessoal, não tem como achar fazer essa transição aqui.

11:33

Na verdade, olha o que eu vou fazer.

11:36

Eu vou sair do script aqui um pouquinho.

11:40

Eu vou sair desse tipo de aqui porque aqui não vai

11:42

não vai, a gente não vai conseguir sair do outro

11:45

lado, né? Mas olha só que legal, e se eu simular

11:50

né? É, e pedir para criar um repositório, né? Aí, olha

11:55

olha que legal, pessoal, eu vou pedir para criar um

11:58

repositório, é no banco, tá? No meu chave, tá aqui

12:05

que eu passei, tá? No meu, aqui estou aqui, e esse repositório

12:08

repositório que simula os pedidos, tá? Então, é o seguinte,

12:11

para que

12:18

exemplo do

12:26

combinado fique

12:31

mais realista,

12:35

preciso que crie um repositório fake

12:41

e que crie issues nesse repositório,

12:48

citando que crie três issues,

12:52

citando pedidos e

12:57

clientes, pedidos que falharam.

13:07

citando pedidos que falharam.

13:12

Porque nunca vamos achar um

13:19

cruzamento usando

13:23

o Model

13:27

Context Protocol, o

13:32

repo do Model Context Protocol.

13:39

Não é preciso que crie um repositório fake chamado e

13:47

-commerce, e

13:51

que crie três issues nesse repositório.

13:56

Vamos ver se ele vai conseguir nos ajudar.

14:05

Pessoal, não sei se... Obviamente,

14:07

alguns de vocês devem ter experiência usando uma ideia semelhante,

14:11

tá? Como essa aqui que eu estou usando agora, tá?

14:15

E curiosidade para vocês aqui, o anti-gravity, tá?

14:19

Ele se conecta à conta do próprio... do próprio...

14:23

do meu próprio Gmail e da minha conta, tá? Então, vamos ver aqui,

14:26

ó. Escrevi um plano de implementação detalhado, exatamente como vamos criar.

14:31

Então, olha o plano que ele criou, gente, objetivo,

14:34

né? Tornar o momento errado a tarefa combinada mais realista,

14:37

né? Ele vai usar meu access token,

14:41

ele vai criar um repo, ele vai criar aqui tudo lá dentro,

14:45

vamos ver se vai funcionar.

14:47

Bem, vamos

14:51

ver o agente aí trabalhando, tá? E só uma curiosidade para vocês,

14:56

tá? Eu já havia cadastrado meu access token aqui diretamente também.

15:00

Para que ele possa usar o meu repositório, tá bom?

15:13

Só que nesse caso aqui está sendo mais inteligente, tá?

15:17

Ele está criando um Python para poder fazer isso.

15:20

Né? Para, obviamente, usar o MCP server que a gente usou, que a gente criou. Interessante.

15:53

Lembrar de atualizar o limpar.

16:02

Script de limpeza. Está vendo?

16:17

Eu uso o meu Isaac Babs, que é o meu usuário, tá? Então

16:37

enquanto ele faz ali, pessoal, vamos ver o que que ele fez aqui ó

16:40

ele criou um script que é seed

16:42

do GitHub, tá? Que obviamente ele pega

16:48

aqui o meu access token, tá bom? Deixa eu ver se ele usou o

16:52

MCP server, se ele executou diretamente. Ah, não, ele chamou direto a API do GitHub, tá?

17:00

É como é como ele fez lá no caso do CID do Postgres, né?

17:06

É que ele fez um CID do

17:09

GitHub para poder executar, então vamos lá, aí

17:16

o seguinte, tá? Então, então, como é que vai ficar agora? O seguinte, ó, então

17:26

a gente já configurou, então vou fechar aqui

17:31

Tá? A gente já configurou, né? Vamos, a gente já

17:36

Então, o protocolo, beleza. Onde é que eu estou aqui? Então, assim, a

17:42

gente viu o GitHub pedindo. Vamos ver aqui,

17:49

deixa eu ver aqui, cadê o CID,

17:57

cadê o CID? Ah,

18:01

Boa, olha só,

18:03

deixa eu executar o comando aqui que vai...

18:07

Criar o repo temporário lá, tá, pessoal? Vamos cruzar os dedos.

18:12

Vamos ver se vai funcionar.

18:18

Caramba, criou mesmo, tá? Que legal.

18:23

Criou tudo lá, né?

18:26

Criando estes falsos, parará, beleza.

18:29

Vamos ver aqui agora.

18:31

Aliás, deixa eu... Não, pode ser aqui.

18:34

Beleza, então agora... Olha o que eu vou fazer. Eu vou fazer o combinado.

18:39

Já vou executar aqui o combinado. Tudo junto.

18:59

Pessoal, esse aqui é um bônus aqui para vocês.

19:07

De como fazer vibe coding, tá? Nesse caso aqui específico, tá? De novo,

19:13

a gente está aqui em um ambiente produtivo e, obviamente, pessoal,

19:18

eu tenho cuidado de colocar várias skills para controlar.

19:25

Neste caso específico, pessoal, como é algo super simples, tá?

19:31

Eu permiti que ele...

19:35

que ele fizesse aqui desde o início. Então, pessoal, olha só. Olha que legal.

19:40

Olha que legal, gente. Ixos abertos mencionando pedido.

19:43

Encontrei três Ixos abertos no repositório Isaac e-commerce.

19:47

E ele correlacionou os pedidos, pedidos com status de falha encontrados. Conclusão,

19:54

todos os três pedidos mencionados na Ixos abertos estão realmente

19:56

com status de falha na base de dados,

19:58

confirmando que dois pedidos da Ana confirmando falha,

20:01

14 pedidos... Desculpa,

20:04

pedido 14 da Gabriela confirmado falha e pedido 28 do confirmado falha. Além disso,

20:08

há quatro pedidos adicionais com status falha que

20:12

não foram mencionados na issues abertas, tá?

20:14

Que também precisam de atenção.

20:16

Pessoal, sensacional ou não é? Com essa aqui eu fecho o nosso treinamento de hoje,

20:22

Tá bom, pessoal? O nosso lab.

20:23

A gente se vê na próxima. Não, não, não, não, não.

20:27

Preciso fechar. Não, tá certo. Não tem mais nenhum outro slide lá.

20:30

Perdão, não tem mais nenhum outro slide lá,

20:32

Então a gente fechou aqui mesmo. Valeu, pessoal!

## Resumo IA

[RESUMO_IA]