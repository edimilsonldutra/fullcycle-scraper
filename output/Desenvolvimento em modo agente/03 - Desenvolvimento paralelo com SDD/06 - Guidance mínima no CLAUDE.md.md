Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17795)

## Resumo da aula

Uma guidance mínima em CLAUDE.md antecipa conflitos previsíveis do desenvolvimento paralelo sem transformar o fluxo em um processo excessivamente prescritivo. A ideia não é documentar tudo, mas fixar decisões operacionais que o agente dificilmente inferiria sozinho com segurança. Isso reduz ambiguidade em pontos sensíveis como portas, banco de dados, arquivos locais e execução de testes. Quando essas regras ficam explícitas, o agente pode focar na feature sem desperdiçar iterações corrigindo infraestrutura local.

Em um setup com várias features rodando ao mesmo tempo, a porta 3000 pode ser reservada para a aplicação principal executada a partir do main, enquanto as demais execuções usam portas a partir da 3001. Essa convenção evita colisão entre a instância de referência e os ambientes temporários de desenvolvimento. A escolha do número é arbitrária; o valor real importa menos do que a consistência da regra. O CLAUDE.md precisa apenas declarar a convenção para que cada execução derivada escolha a próxima porta disponível sem disputar a porta principal.

Retomando o cenário de execução paralela, o container de Postgres continua único na porta 5432, mas cada feature recebe seu próprio banco de dados dentro desse mesmo servidor. O isolamento deixa de depender de múltiplos containers e passa a depender de nomes de database distintos, como VideoMaxCloud-funcionalidade-02-alt. Isso impede que migrações de uma feature contaminem o estado de outra durante o desenvolvimento simultâneo. A regra crítica é simples: cada agente só pode migrar o banco que ele mesmo criou.

Permitir limpeza automática sem restrição é perigoso em ambientes compartilhados, porque o agente pode apagar recursos que não pertencem à sessão atual. Por isso, a remoção deve ser limitada a databases e schemas criados com um prefixo controlado, como VideoMaxCloud-*. Essa convenção transforma naming em mecanismo de segurança operacional. Tudo que não seguir o prefixo da sessão deve ser tratado como patrimônio do usuário e preservado.

O arquivo .env.local concentra os ajustes específicos de cada execução paralela: porta da aplicação, nome do banco e URL de conexão. O fluxo mínimo consiste em copiar .env.example para .env.local antes de iniciar o ambiente e então sobrescrever os valores variáveis da sessão. Isso mantém o template versionado intacto e desloca a customização para um arquivo local. Em projetos mais maduros, scripts de bootstrap podem encapsular esse passo, mas a regra continua a mesma.

Quando o fluxo usa Claude Desktop, o launch.json na pasta .claude precisa refletir a mesma porta configurada no .env.local. Se os dois arquivos divergirem, o preview aponta para uma instância errada ou simplesmente falha. Como esse arquivo é específico do ambiente local, ele não deve ser commitado e normalmente já fica coberto pelo .gitignore. A utilidade dele é operacional, não colaborativa.

A skill next.js.bestpractice funciona como guidance complementar para um framework que evolui rapidamente, como o Next 16. O ponto importante não é redefinir o framework, mas reduzir contradições entre o comportamento esperado do agente e as práticas atuais da stack. Como o próprio ecossistema já usa mecanismos de Progressive Disclosure, a skill serve para alinhar a execução com essas novidades sem exigir prompts longos. Guidance mínima não significa ausência de contexto técnico; significa contexto suficiente e bem escolhido.

Os testes unitários continuam sendo executados com Vitest, mas critérios de aceitação que exigem navegação, interação com DOM, formulários, cliques ou submit deixam de ser apenas lógica local e passam a exigir teste E2E de front-end. O gatilho prático é a necessidade de navegar pela interface. Essa regra existe porque um agente pode implementar código sem sequer subir o servidor, o que mascara falhas reais de integração visual e comportamental. Ao vincular o tipo de teste ao critério de aceitação, a validação deixa de ser opcional.

Se o ambiente suportar preview via launch.json, o teste pode usar esse fluxo diretamente. Fora desse contexto, a alternativa é carregar a skill do Playwright CLI e executar em headless mode, no qual o browser roda sem interface gráfica visível. O importante não é a ferramenta de entrada, mas garantir que a navegação realmente aconteça em um ambiente funcional. Antes de qualquer teste, banco existente, migrações aplicadas e servidor na porta correta são pré-condições obrigatórias.

Retomando a plataforma de vídeo já usada no capítulo, fluxos de upload precisam de um arquivo concreto para teste, não apenas de mocks abstratos. Um sample como sample/videoteste.mkv permite validar o caminho completo de seleção, envio e processamento inicial do arquivo. Isso torna o teste reproduzível e reduz improvisações do agente ao gerar entradas artificiais. Em cenários com mídia, fixture de arquivo é parte da infraestrutura de teste.

Conflito resolvido não significa feature validada. Sempre que houver merge ou ajuste manual em áreas afetadas, os testes correspondentes precisam ser executados novamente, porque a integração pode ter quebrado comportamentos já aceitos. Se o conflito atingir um critério que depende de interação de front-end, o E2E também volta a ser obrigatório antes de encerrar o trabalho. Essa regra transforma o merge em evento de revalidação, não em etapa puramente textual.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior eu falei para vocês como a gente tem que tomar cuidado na

00:05

realidade e na hora que a gente for trabalhar

00:07

com várias coisas rodando ao mesmo tempo.

00:09

Então, o que acontece? A partir desse momento,

00:12

a gente vai precisar ter um pouco mais de cuidado, por exemplo, com banco de dados,

00:17

com portas, com variáveis de ambiente,

00:20

com Git Ignore e também com o processo de testabilidade.

00:24

Então, o que eu fiz aqui?

00:27

Dentro do meu Cloud MD, perceba,

00:29

eu estou tentando deixar ele aqui o mínimo possível

00:31

para a gente focar simplesmente no desenvolvimento.

00:35

Eu não estou querendo aqui passar por um processo tão iterativo de construção,

00:42

mas eu já tenho uma antecipação de coisas que

00:45

para mim são comuns que vão acontecer claramente.

00:48

Então, o que são uma dessas coisas? Primeira coisa,

00:52

Next.js porta.

00:54

Então, o que eu falo? Normalmente a porta 3000 está em uso.

00:59

E por que eu estou dizendo isso? Normalmente,

01:02

quando eu quero testar a minha aplicação ali no main,

01:05

eu vou utilizar a minha porta 3000. Então,

01:08

o que eu estou querendo dizer é que toda vez que

01:11

ele for querer fazer o desenvolvimento de uma feature,

01:14

para ele pegar a próxima porta a partir da 3001,

01:19

porque a 3000 eu estou reservando, vamos dizer assim, para o meu...

01:26

para o meu Next.js, que eu vou rodar no main,

01:28

que é como se fosse o que estivesse em produção. Então,

01:31

isso foi uma decisão arbitrária que eu tomei aqui nesse curso,

01:34

isso não significa que você vai ter que fazer isso no seu projeto.

01:37

Outra coisa é o seguinte, eu estou falando que o Postgres vai usar a porta 5432,

01:43

e o Postgres está rodando para mim num Docker. Então,

01:46

eu tenho um Docker com Post, que ele sobe o Postgres na minha máquina aqui.

01:50

Mas, novamente, eu só tenho uma porta 5432. Então,

01:53

todo o desenvolvimento aqui do software vai ter que rodar em cima dessa mesma porta.

01:58

Então, o que eu estou falando? Estou falando o seguinte, olha,

02:01

você vai rodar aqui na porta 5432 e você

02:05

vai reutilizar o Possible Container que já está rodando.

02:09

Se não estiver rodando,

02:10

você vai iniciar usando nesse repositório

02:15

e subindo aqui o Docker Compose YAML.

02:19

Outra coisa interessante que eu coloquei aqui é Perception Database.

02:23

Então, o que eu falei? Dentro do container,

02:26

você vai criar um banco de dados nomeado no formato Video, Max,

02:31

Cloud e uma Slug. Aqui, por exemplo, Video, Max, Cloud, funcionalidade 02, Alt.

02:37

E o que eu estou colocando aqui para ele é para ele nunca

02:40

rodar nenhuma migração em cima de outros bancos de dados que não são dele. Por quê?

02:47

Porque eu não quero ter um único banco de dados e

02:50

na hora que eu estou desenvolvendo em paralelo,

02:52

um banco de dados atrapalha o desenvolvimento

02:54

da outra feature que está sendo desenvolvida.

02:59

Eu preciso isolar esses caras.

03:00

Então, eu estou pedindo para ele criar um banco

03:01

de dados para cada feature naquele momento.

03:06

Aí eu coloquei aqui, Data Removal.

03:08

Você vai apenas poder remover databases e esquemas que você criou nessa sessão.

03:14

aqueles que começam com VideoMax Cloud e ali algum prefixo.

03:18

Qualquer outro banco de dados que o usuário tiver nessa sessão.

03:23

Aí a gente tem um outro ponto, que é o .env .local. Antes de iniciar o ambiente,

03:30

copie o .env .example para .env .local e faça a

03:37

alteração da porta e o nome do banco de dados,

03:41

a URL do banco de dados.

03:43

Esse aqui é um ponto importante que eu já estou ensinando ele aqui.

03:47

Outra coisa também que eu já queria dizer, pessoal,

03:49

muito do que está nessa instrução aqui pode ser reduzido basicamente por uma,

03:56

duas ou três linhas,

03:57

uma vez que você tem alguns scripts de inicialização.

04:00

A gente já falou no passado sobre scripts de inicialização.

04:03

Como nós não estamos focando nisso,

04:06

nesse capítulo ou nessa parte especificamente de SDD, Então,

04:11

eu estou fazendo isso de forma mais manual e eu

04:13

estou guiando o agente ali passo a passo.

04:16

Mas eu poderia criar um script que eu dou um init,

04:18

ele já faz tudo automático ali para mim, certo?

04:21

E o .env, .local, então ele vai copiar e vai alterar a porta aqui.

04:26

Outra coisa que eu tenho, e nesse caso, é específico do cloud, tá?

04:31

Que é o arquivo lanch .json. Esse arquivo aqui,

04:34

ele é criado na pasta, nesse caso, .cloud, tá?

04:40

E esse arquivo é um arquivo

04:42

que simplesmente o cloud cria para mim,

04:48

para eu rodar aquele preview no cloud desktop.

04:51

Então, isso, nesse caso aqui, é focado somente se eu for usar aquele ambiente.

04:59

Somente por isso que essa linha existe aqui para mim,

05:03

porque ele só vai trabalhar aqui nesse aspecto. Então,

05:07

eu vou falar o que aqui para ele.

05:09

Se você criar um launch .json,

05:12

você tem que usar a mesma porta que você está usando no .env .local.

05:16

E eu falei para ele nunca comitar o launch .json,

05:19

porque ele também já está no .gitignore. Beleza? Então,

05:23

esse é um ponto para configurar o minimamente do ambiente para

05:27

eu poder rodar esses caras em paralelo e etc.

05:31

Outra coisa que eu coloquei aqui também é carregue

05:34

a skill next .js .bestpractice e lembrando também, tá?

05:39

no momento que a gente está desenvolvendo, está no Next 16,

05:42

e o Next 16, quando a gente cria...

05:45

ele até gera um arquivo falando, olha, esse é o Next que você não conhece,

05:50

então você pode ler a documentação em tal lugar.

05:52

Então ele trabalha ali com o Progressive Disclosure para

05:55

conseguir carregar as novidades para a gente conseguir.

05:58

Então o próprio Next .js é como se ele já tivesse feito isso,

06:02

a gente pode depois colocar essa linha,

06:04

mas como eu estou trabalhando já com essa skill,

06:07

Eu quero evitar muita contradição e etc.

06:10

E aqui é a parte de teste. Então,

06:13

Em relação a teste, eu estou colocando o seguinte, olha,

06:16

Os testes que você vai rodar, você vai rodar os unit tests ali com o iTest,

06:20

Os testes E2E, end-to-end, front-end testes, eles precisam,

06:27

Quando eles estiverem no critério de

06:33

Aceitação e eles precisarem de navegação,

06:36

DOM, formulários ou qualquer comportamento visual, comportamento visual,

06:43

Qualquer coisa que tenha, o usuário pode clicar, ele pode ser,

06:47

Ele pode dar um submit, ele pode navegar,

06:49

O critério é navegar. Então,

06:56

Esse aqui é um ponto.

06:57

Toda vez que nós tivermos que fazer isso,

07:00

Isso aqui, na realidade,

07:02

Vai ser considerado para a gente um teste de front-end E2E.

07:07

Então, a gente obriga, nesse caso, o agente a fazer esse teste. Porque o que acontece?

07:13

Eu acho que você já viu em sessões anteriores,

07:16

Ele desenvolveu o sistema sem ao menos iniciar o servidor.

07:20

Então, quando eu estou falando para ele,

07:22

Quando ele olha os critérios de aceitação e percebe

07:24

Que nesse critério de aceitação ele vai precisar navegar,

07:29

Então esse tipo de coisa vai forçar com que ele utilize o ambiente.

07:35

E aqui eu estou falando como que você roda esse ambiente.

07:38

Então, eu estou colocando assim, como rodar o teste Z2Z? Então,

07:42

Se você tentar utilizar o Launch.json com o Preview Start,

07:46

Novamente, nesse caso, é específico para aquela interface do Cloud Desktop.

07:52

Você pode utilizar com o Preview Start. O que acontece?

07:56

Não necessariamente a gente vai estar naquele ambiente,

07:59

Muitas vezes a gente vai estar aqui na IDE.

08:01

Se isso aqui falhar, você vai carregar o Playwright CLI, a skill,

08:06

E vai rodar em Headless Mode. O que é Headless Mode? Basicamente,

08:10

É quando o browser não vai precisar abrir ali na nossa frente. Então,

08:15

Somente pelo fato disso acontecer, ele vai conseguir fazer os testes ali também.

08:20

Outra coisa que eu coloquei é, antes de rodar qualquer teste,

08:24

Tenha certeza que o banco de dados existe e que as

08:29

Migrações foram aplicadas e que o servidor está rodando na porta correta.

08:35

E o que eu falei aqui também para ele é, como a gente tem uma plataforma de vídeo,

08:41

Ele vai precisar ter um vídeo de exemplo para que ele

08:45

Consiga fazer o upload e fazer o teste ali para a gente. Então, nesse caso aqui,

08:50

Eu coloquei, olha, tem um vídeo de exemplo,

08:53

Se você precisar de um vídeo para qualquer tipo de teste ou simulação,

08:57

Use o vídeo sample / videoteste.mkv, que eu criei um arquivinho aqui,

09:03

Ó, vídeo sample, que está esse cara aqui para ele poder usar.

09:06

E aqui na parte de Git é,

09:09

Sempre que você resolver um merge ou trabalhar com conflitos,

09:14

Você vai ter que rodar novamente os testes que foram afetados naquela área.

09:18

Se algum critério de aceitação for impactado por esse

09:22

Conflito e precisar de qualquer interação com front-end,

09:27

Você vai ter que também rodar o teste E2E antes de terminar.

09:31

Isso aqui é apenas um reforço do tipo. Eu sei que vai ter conflito.

09:35

Eu vou pedir para ele resolver conflitos,

09:37

provavelmente na hora que ele terminar a tarefa,

09:39

eu vou pedir para ele, veja, olha,

09:41

tenta ver o que tem no main para você fazer um

09:44

merge antes de eu gerar a minha pull request.

09:47

Então, quando eu pedir para fazer isso,

09:48

ele já sabe que ele vai ter que rodar os testes novamente.

09:52

É um mínimo que eu coloquei aqui.

09:56

Novamente, dá para a gente reduzir bastante esse CloudMD com alguns desses...

10:02

Com alguns desses tweaks que a gente pode fazer e etc.

10:06

Mas eu estou deixando de uma forma mais explícita aqui para você.

10:09

Então isso é uma parte do que eu queria mostrar.

10:13

Agora a outra parte vai no próximo vídeo que eu

10:16

vou mostrar aqui para vocês na parte de implementação.

10:19

Como é que a gente vai fazer.

## Resumo IA

**Abreviações**
*   **CLAUDE.md:** Documento de orientação mínima para o agente de desenvolvimento.
*   **.env.local:** Arquivo de variáveis de ambiente local.
*   **E2E:** End-to-End (Teste de ponta a ponta).
*   **DOM:** Document Object Model.
*   **CLI:** Command Line Interface (Interface de linha de comando).
*   **YAML:** YAML Ain't Markup Language (linguagem de marcação de dados recursiva, usada em Docker Compose).
*   **SDD:** Software Design and Development (disciplina ou processo de desenvolvimento de software, contexto do capítulo do curso).
*   **IDE:** Integrated Development Environment (Ambiente de Desenvolvimento Integrado).
*   **PR:** Pull Request (Requisição de Pull).

**Resumo**
O objetivo da aula é fornecer uma orientação mínima em um documento `CLAUDE.md` para antecipar e mitigar conflitos previsíveis no desenvolvimento paralelo, sem impor um processo excessivamente prescritivo. A ideia é fixar decisões operacionais que o agente de desenvolvimento dificilmente inferiria com segurança sozinho, como configurações de portas, bancos de dados, arquivos locais e execução de testes, permitindo que o agente foque na feature sem desperdiçar iterações corrigindo a infraestrutura local.

Os conceitos e ferramentas abordados incluem:
Em um cenário de desenvolvimento paralelo, a porta 3000 é reservada para a aplicação principal executada a partir do `main`, enquanto as demais execuções de features utilizam portas a partir da 3001 para evitar colisões. O servidor de banco de dados Postgres permanece único na porta 5432 (rodando em Docker), mas cada feature recebe seu próprio banco de dados isolado por nomes distintos (ex: `VideoMaxCloud-funcionalidade-02-alt`), prevenindo contaminação de migrações. A remoção de dados é restrita a bancos e schemas criados com um prefixo controlado (`VideoMaxCloud-*`) para garantir segurança operacional.

A configuração de ambiente local é centralizada no arquivo `.env.local`, que concentra ajustes específicos como a porta da aplicação, nome do banco e URL de conexão. O fluxo de setup envolve copiar `.env.example` para `.env.local` e sobrescrever os valores variáveis. Para usuários do Claude Desktop, o arquivo `launch.json` (na pasta `.claude`) deve refletir a mesma porta configurada no `.env.local`; este arquivo é local e não deve ser versionado. A skill `next.js.bestpractice` é utilizada para alinhar o agente com as práticas mais recentes de frameworks como Next.js 16, complementando a orientação mínima.

A estratégia de teste distingue entre testes unitários (executados com Vitest) e testes End-to-End (E2E) de front-end. Testes E2E são obrigatórios sempre que os critérios de aceitação exigem navegação, interação com o DOM, formulários, cliques ou qualquer comportamento visual. Essa regra força o agente a garantir que o servidor esteja ativo e funcional. Os testes E2E podem ser executados via `launch.json` (no preview do Claude Desktop) ou utilizando o Playwright CLI em modo headless. Pré-condições essenciais para qualquer teste incluem a existência do banco de dados, migrações aplicadas e o servidor rodando na porta correta. Para cenários com upload de mídia, arquivos de exemplo concretos (ex: `sample/videoteste.mkv`) são necessários como fixtures de teste. Por fim, sempre que conflitos Git são resolvidos ou merges são realizados, os testes afetados devem ser reexecutados (incluindo E2E se o front-end for impactado) para revalidar a integração. O instrutor ressalta que muitos desses passos manuais poderiam ser automatizados com scripts de bootstrap em projetos mais maduros.

**Pontos de atenção**
*   **Guidance Mínima vs. Prescrição:** A `CLAUDE.md` deve focar em resolver ambiguidades em pontos sensíveis e antecipar conflitos previsíveis, sem se tornar um documento excessivamente prescritivo ou um manual completo.
*   **Colisão de Portas:** Evite conflitos reservando a porta 3000 para a instância principal da aplicação (branch `main`) e utilizando portas a partir de 3001 para as execuções de features em desenvolvimento paralelo. A consistência da regra é mais crucial do que o número específico da porta.
*   **Isolamento de Banco de Dados:** Para o desenvolvimento paralelo, mantenha um único container de Postgres, mas crie um banco de dados distinto para cada feature (ex: `VideoMaxCloud-funcionalidade-02-alt`). Isso impede que as migrações de uma feature contaminem o estado de outra.
*   **Controle de Migrações:** O agente deve ter permissão para migrar apenas o banco de dados que ele mesmo criou, reforçando o isolamento.
*   **Remoção Segura de Dados:** Limite a limpeza automática de bancos de dados e schemas apenas àqueles que seguem um prefixo controlado (ex: `VideoMaxCloud-*`). Recursos sem esse prefixo devem ser tratados como patrimônio do usuário e preservados.
*   **Configuração Local (`.env.local`):** Sempre copie o `.env.example` para `.env.local` antes de iniciar o ambiente e personalize as variáveis locais (porta da aplicação, nome do banco, URL de conexão). O `.env.example` deve permanecer intacto e versionado.
*   **Sincronia `launch.json` (Claude Desktop):** Se estiver usando Claude Desktop, a porta configurada no `launch.json` (na pasta `.claude`) *deve* ser idêntica à porta definida no `.env.local`. Este arquivo é específico do ambiente local e não deve ser commitado.
*   **Gatilho para Testes E2E:** Qualquer critério de aceitação que exija navegação na interface, interação com o DOM, formulários, cliques ou qualquer comportamento visual implica na obrigatoriedade de testes E2E de front-end. Isso força o agente a verificar a integração em um ambiente funcional.
*   **Pré-condições para Testes:** Antes de executar qualquer teste (unitário ou E2E), assegure-se de que o banco de dados exista, todas as migrações foram aplicadas e o servidor da aplicação está rodando na porta correta.
*   **Fixtures para Testes de Mídia:** Em testes envolvendo upload ou manipulação de mídia, use arquivos de exemplo concretos (ex: `sample/videoteste.mkv`) como fixtures para garantir que os testes sejam reproduzíveis e válidos.
*   **Revalidação Pós-Conflito/Merge:** A resolução de conflitos no Git ou a realização de um merge é um evento de revalidação. Após qualquer ajuste manual em áreas afetadas, todos os testes correspondentes (incluindo E2E se a interação de front-end for impactada) devem ser executados novamente.
*   **Automação de Setup:** Embora a aula mostre um fluxo manual, scripts de bootstrap podem encapsular e automatizar o setup do ambiente (como a cópia de `.env.local` e a configuração de portas), tornando o processo mais eficiente em projetos maduros.
*   **Nomenclatura como Segurança:** Utilizar prefixos controlados para nomes de bancos de dados e schemas (`VideoMaxCloud-*`) serve como um mecanismo de segurança para gerenciar a remoção de recursos de forma segura.