Módulo: Protocolos de Comunicação\
Aula: [Docker MCP Toolkit](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18608)

## Resumo da aula

Containerizar um servidor MCP significa transformar um processo local em um serviço isolado, reproduzível e controlável. Retomando o mesmo servidor MCP, a preocupação deixa de ser apenas “executa corretamente” e passa a incluir rastreabilidade, contenção e previsibilidade operacional. Isso importa porque o servidor pode acessar APIs, file system, banco de dados e credenciais, tornando-se parte da superfície real de risco. O container funciona como barreira de execução, reduzindo acesso implícito ao host e padronizando o ambiente entre notebook, CI/CD e produção.

O Docker Catalog centraliza servidores MCP prontos para uso com evidências de confiança operacional. Provenance é a prova criptográfica de origem da imagem: indica quem a gerou, em qual pipeline e sem quais alterações intermediárias ela chegou ao artefato final. SBOM é o inventário completo dos componentes da imagem, incluindo dependências diretas, transitivas e licenças. Juntos, esses dois mecanismos permitem responder rapidamente se uma imagem é confiável e se foi afetada por uma CVE sem depender de inspeção manual do código.

O Docker MCP Desktop Toolkit atende ao ciclo local de desenvolvimento, onboarding e teste rápido de servidores do catálogo. Em produção, essa função muda para o Docker MCP Gateway, que opera como borda declarativa entre cliente, LLM e backend MCP. O gateway define por YAML quais servidores existem, como acessá-los por HTTP, quais tools podem passar e quais headers de segurança devem ser injetados. Essa separação evita levar para produção a ergonomia do desktop e substitui conveniência local por controle centralizado.

Multi-stage build separa a fase de compilação da fase de execução para reduzir tamanho e risco da imagem final. O estágio builder instala compiladores, resolve dependências e aproveita cache do BuildKit; o estágio runtime copia apenas o resultado necessário para rodar. Isso elimina logs temporários, caches e toolchains que não deveriam existir em produção. A consequência prática é uma imagem menor, mais rápida de distribuir e com menos superfície explorável.

Executar o processo como non-root impede que uma invasão no container comece já com privilégios máximos. A imagem cria um usuário dedicado, ajusta ownership dos arquivos da aplicação e declara esse usuário como padrão de execução. Se ocorrer um RCE, o atacante fica limitado a um contexto sem privilégios administrativos dentro do container. Essa medida não substitui isolamento adicional, mas reduz fortemente o impacto de falhas exploráveis.

Um container em execução não é necessariamente um serviço saudável. O health check consulta uma rota como /healthz para verificar periodicamente se a aplicação continua respondendo de forma útil, e não apenas se o processo ainda existe. Quando a verificação falha, o orquestrador pode marcar a instância como unhealthy e reiniciá-la automaticamente. Isso evita o estado enganoso de serviço “vivo”, porém travado, sem capacidade de atender requisições.

Secrets management em produção evita credenciais estáticas dentro do container do backend. Variáveis de ambiente locais são práticas frágeis porque podem ser extraídas por inspeção do processo ou do sistema /proc em caso de intrusão. O desenho mais seguro desloca o segredo para a borda: o gateway conhece o token de produção, injeta o header HTTP e o backend valida esse header por middleware. Assim, o segredo não precisa circular no cliente LLM nem permanecer exposto no runtime interno do servidor MCP.

STDIO funciona bem no ambiente local, mas não escala para deploy distribuído em containers. A migração para HTTP transforma o servidor MCP em um serviço roteável por rede, compatível com proxy reverso, balanceamento, observabilidade e políticas de borda. No ecossistema Python, isso aparece ao expor a aplicação por mcp.streamable_http_app. A mudança de transporte não é cosmética: ela viabiliza a operação segura em produção.

Retomando o mesmo servidor MCP, nem toda tool implementada deve ficar exposta à LLM. A allowlist no gateway declara explicitamente quais ferramentas estão autorizadas a atravessar a borda, bloqueando enumeração ou invocação de capacidades ocultas antes de qualquer chamada ao backend. Isso complementa o privilégio mínimo já visto na camada lógica com uma contenção operacional na borda. O resultado é menos superfície exposta e menor custo de processamento para requisições indevidas.

Defesa em profundidade combina várias restrições independentes para que a falha de uma camada não comprometa o sistema inteiro. No runtime do container, isso inclui cap_drop, file system somente leitura, tmpfs para escrita temporária, rede isolada e limites de CPU e memória. Cada controle remove uma classe de ação que o processo não deveria executar, como alterar relógio do sistema, persistir backdoors em disco ou degradar a máquina host por loop recursivo. Em conjunto, essas barreiras transformam o container em um ambiente mínimo e hostil a abuso.

Defaults seguros existem para reduzir erro operacional antes mesmo de qualquer customização. Limite de memória, isolamento de file system, exigência de imagens assinadas e profiles declarativos diminuem risco de exaustão de recursos, vazamento de dados locais, execução de binários não confiáveis e drift de configuração entre máquinas. Esses defaults não substituem revisão de arquitetura, mas elevam o piso de segurança do ecossistema. Em produção, o valor do padrão seguro está em remover permissões implícitas.

Uma revisão madura de imagens e deploys procura sinais simples de risco alto. Rodar como root sem justificativa, hardcode de secrets, COPY indiscriminado sem .dockerignore e ausência de health check são antipadrões porque ampliam privilégio, vazam dados, aumentam a imagem e escondem falhas reais de disponibilidade. Retomando o servidor MCP do capítulo, esses pontos definem se ele está apenas empacotado ou realmente pronto para produção. O checklist operacional existe para impedir que conveniência de desenvolvimento vire fragilidade em ambiente real.

A validação operacional do servidor MCP precisa produzir evidências observáveis. A imagem deve provar origem e composição por provenance e SBOM; o runtime deve mostrar execução non-root, health check ativo e restrições de file system, rede e capabilities; a borda deve comprovar allowlist, injeção de headers e bloqueio de acesso direto ao backend. A migração para HTTP também precisa ser verificável por roteamento e monitoração compatíveis com gateway. Esse conjunto de evidências confirma que o servidor deixou de ser um processo local e passou a operar como serviço seguro e reproduzível.

## Transcrição

00:01

Pessoal, essa aula coloca a gente num lugar bem específico, produção e segurança.

00:05

Então não é uma aula sobre Docker de forma genérica.

00:09

Não é como subir um container qualquer,

00:11

é Docker aplicado ao contexto de MCP,

00:14

onde a gente precisa empacotar servidor, controlar secrets e isolar processos.

00:20

Três expressões praticamente definem a trilha inteira.

00:26

Empacotamento, gerenciamento de secrets e isolamento de processos.

00:32

E guarda essa ideia aqui desde o começo, pessoal. Em ambiente MCP,

00:36

o servidor deixa de ser só um script de conversa com o host.

00:39

Ele passa a ser uma superfície operacional.

00:43

Ele chama a API, ele acessa o file system, ele conversa com serviços internos,

00:48

às vezes lê banco, às vezes manipula credenciais, enfim.

00:51

A gente não tem controle. Então, a pergunta muda. Não é mais só funciona.

00:57

A pergunta passa a ser, funciona de forma rastreável,

01:00

editável e segura o suficiente para a produção?

01:03

Então, o Docker aqui não entra como luxo de DevOps,

01:07

ele entra como fronteira operacional. Então, vamos lá.

01:13

A gente vai olhar os pontos que nós vamos passar aqui, é o seguinte,

01:17

pessoal. Primeiro, nós vamos detalhar as três peças do ecossistema.

01:21

destacando a diferença crucial entre o toolkit focado em

01:24

desenvolvimento local e o Docker focado em produção e orquestração.

01:30

Seguiremos com a engenharia da imagem, ou seja,

01:33

como estruturar um Dockerfile com multistage,

01:35

build e usuário no root para reduzir drasticamente a superfície de ataque.

01:42

E depois trataremos o gerenciamento de secrets,

01:46

comparando o paradigma headers HTTP com os

01:50

inseguros de variáveis de ambiente locais no container.

01:57

Depois nós veremos como o gateway

01:59

aplica regras de toAlloyList na borda,

02:04

para bloquear chamadas antes de bater no backend e,

02:07

obviamente, a mudança de transporte do STDIO para HTTP.

02:13

Bem, por fim, falaremos sobre os mecanismos de sandboxing no Compose, tá?

02:18

E revisaremos os principais antepadrões

02:24

operacionais que você deve evitar. Beleza.

02:28

Então, contêiner em ambiente MCP, pessoal, como eu disse lá atrás,

02:31

não é luxo ou capricho de DevOps. É uma barreira de contenção, tá?

02:35

Por que isso é tão crítico aqui?

02:38

Porque a IA, pessoal, ela opera as ferramentas de forma autônoma. Ou seja,

02:41

se a IA gerar um plano de execução inesperado ou

02:44

for induzida a um ataque de prompt injection,

02:46

a ferramenta pode receber inputs maliciosos. Primeiro ponto, então,

02:52

o que a gente tem que fazer? Isolamento.

02:54

O container encapsula a execução em namespaces de rede,

02:57

processos e sistemas de arquivo.

03:01

Se o atacante explora uma vulnerabilidade no seu servidor MCP,

03:04

ele estará isolado dentro daquele container.

03:06

Sem acesso direto aos processos ou arquivos do host.

03:13

Segundo ponto, reprodutibilidade.

03:15

O código que roda no seu notebook usa a exata mesma imagem,

03:19

dependências e SEO do CICD e nos contêineres de produção.

03:23

Isso previne bugs silenciosos causados por divergências de pacotes.

03:28

Terceiro, file systems e redes restritos. Por padrão,

03:32

o container não enxerga o disco local nem a rede interna do seu servidor.

03:36

A menos que você monte volumes,

03:37

eu configuro o bridge explicitamente.

03:39

A containerização remove a permissão implícita de acesso aos recursos locais.

03:46

Gente, o Docker Catalog é o catálogo oficial que

03:50

centraliza e qualifica servidores MCP prontos para produção.

03:54

Quando usamos código de terceiros,

03:57

a pergunta mais importante não é também se funciona.

04:00

E sim, consigo confiar na procedência desse binário?

04:03

Aqui entram dois conceitos de segurança de cadetes de suprimentos que o catálogo expõe.

04:07

Primeiro, a procedência. É a prova criptográfica,

04:11

é a procedência, que é o provenance.

04:14

É a prova criptográfica de origem. Ele garante quem gerou a imagem,

04:19

em qual pipeline do GitHub e DOC ela foi

04:22

compilada e que nenhuma alteração intermediária foi feita.

04:25

Segundo é o SBOM, que é o Software Bill of Materials.

04:29

É a lista de ingredientes da imagem.

04:31

O SBOM mapeia todas as bibliotecas Python, Node instaladas,

04:35

dependências transitivas e suas licenças.

04:37

Se uma vulnerabilidade grave, as famosas SVS,

04:41

ou divulgada em uma biblioteca específica,

04:43

o SBOM permite cruzar instantaneamente e descobrir se os

04:46

seus servidores MCP em execução estão usando a versão vulnerável.

04:51

Sem precisar, no final, ler código ou planilhas. Em ambientes corporativos,

04:57

a rastreabilidade baseada em SBOM é indispensável para conformidade,

05:01

como o SOC 2 e ISO 27001.

05:09

Agora, precisamos fazer a distinção clara entre o ambiente

05:12

de desenvolvimento e o ambiente de produção.

05:13

E o ecossistema Docker resolve ambos.

05:16

O Docker MCP Desktop Toolkit, pessoal, ele é uma ferramenta local.

05:23

Ele vive no Docker Desktop, permitindo gerenciar perfis, profiles.

05:28

Você escolhe servidores do catálogo,

05:30

clica em rodar e ele altera as configurações do seu cliente local,

05:34

de forma transparente.

05:37

É focado em um onboarding rápido de engenheiros e produtividade de desenvolvimento. Já em produção,

05:42

a conversa muda de figura. Não temos uma interface de desktop,

05:46

nós rodamos serviços distribuídos em nuvem.

05:48

E aí entra o Docker MCP Gateway. O Gateway atua como a borda da IA.

05:54

Ele é o proxy reverso que fica entre o cliente, a LLM, a aplicação que consome,

05:59

e seu backend de ferramentas, o MCP financeiro,

06:02

por exemplo, que a gente tem feito.

06:04

Ele é configurado via arquivo declarativo, que é o ponto YAML,

06:10

onde declaramos quais servidores existem,

06:16

como se conectar a eles via HTTP,

06:19

quais tools estão autorizadas a passar e quais

06:21

cabeçalhos de segurança devem ser injetados,

06:23

por exemplo. Isso garante uma função uniforme.

06:26

As imagens e comportamentos testados no toolkit local são expostos.

06:29

E protegidos de forma centralizada pelo Gator na nuvem.

06:33

Agora vamos analisar o esqueleto seguro de Docker

06:35

file que implementamos para o nosso servidor.

06:38

Ele usa a melhor prática de multi-stage build. No stage 1, que é o builder,

06:44

nós instalamos as ferramentas necessárias e compilamos as dependências.

06:48

Usamos o cache mount do BuildKit,

06:51

o que significa que o cache do PIP persiste entre

06:55

builds na máquina do desenvolvedor ou no Continuous Integration,

06:58

acelerando muito as compilações subsequentes. E no stage 2, que é o runtime,

07:02

nós começamos com uma imagem limpa.

07:04

Nós apenas copiamos o resultado compilado do builder. Nenhum compilador,

07:09

arquivo de log temporário ou cache do pip entra aqui.

07:12

Isso resulta em uma imagem final extremamente pequena.

07:15

E aqui mora o coração de segurança da imagem, pessoal. Olha só.

07:19

User non-root. Ou seja, criamos um usuário do sistema, nesse caso aqui,

07:24

que é o usuário app. A gente fez até aqui,

07:27

groupadd, menos r, app. E comercial, né? E dois is comerciais.

07:33

User ID, menos R, menos G. App,

07:35

menos U, é o UID do app. Ou seja, a gente...

07:39

Toda essa linha de comando aqui, pessoal, para quê?

07:42

Serve para a gente criar um usuário no root.

07:45

Tão simples quanto isso. Primeiro passo, pessoal, criar um usuário no root.

07:50

Depois a gente faz um drop privileges. Ou seja,

07:52

nós alteramos o dono dos arquivos da aplicação.

07:55

A gente usou o chown, né? Que é o change owner.

07:59

E declaramos userApp, que é o usuário no root que a gente criou ali em cima.

08:03

Pessoal, isso aqui é só um exemplo, tá?

08:06

Inclusive, pessoal, já um spoiler, nós vamos usar esse exemplo no Lab, tá? Esse mesmo exemplo.

08:11

Mas, enfim, o nome do usuário no root pode ser o que vocês entenderem,

08:16

né? Ou seja, o importante é seguir esses dois passos, tá? Ou seja,

08:19

se o container rodar como root padrão, que é a vulnerabilidade muito comum,

08:24

inclusive, e sofrer um ataque de execução remota de código, um RSE,

08:28

Por exemplo, o atacante ganha acesso de root ao container,

08:32

facilitando a quebra de isolamento para invadir o host. Quando no root,

08:36

o atacante fica restrito a usuários sem privilégios. E para fechar,

08:40

a gente faz um health check nativo.

08:42

O orquestrador monitora a rota healthz, que é o health de autorização,

08:47

periodicamente. Se a thread travar ou o banco de dados cair,

08:51

o container é marcado como unhealth e reiniciado automaticamente,

08:55

evitando o cenário do container vivo, mas inoperante.

09:01

Secrets Management em produção exige que

09:03

abandonemos práticas frágeis de desenvolvimento.

09:06

O maior antipatron em containers é injetar credenciais estáticas de banco de

09:11

dados ou APIs diretamente como variáveis de ambiente no container do back-end.

09:15

Se o container sofrer uma intrusão,

09:17

o invasor executa o comando simples como env, olé,

09:22

o sistema /proc e rouba todas as chaves.

09:25

A abordagem moderna de borda de IA resolve isso de uma forma elegante,

09:29

através de autenticação baseada em headers HTTP.

09:32

O token seguro de produção, que é o BEAR token.

09:36

É conhecido e gerenciado de forma segura pelo Gator.

09:40

Nas aquisições enviadas ao servidor MCP remoto,

09:44

no caso do nosso aqui que a gente vai fazer com o MCP financeiro,

09:46

o Gator injeta de forma transparente o cabeçalho.

09:50

No servidor back-end, nós implementamos o middleware.

09:54

É uma possibilidade, tá? A gente implementa, tipicamente,

09:59

a gente implementa o middleware HTTP,

10:01

que é um ALF middleware, que valida se esse token está presente e correto.

10:05

Qualquer tentativa de requisição que não passe pelo Gator ou use credenciais falsas,

10:10

fale instantaneamente com o código 4401 notarized. Pessoal,

10:13

isso aqui é só um exemplo, uma possibilidade de como...

10:16

de boa prática, tá? Ou seja, as rotas publicadas como barra health z,

10:23

que são os probes, e metrics, que a gente está usando Prometheus, passam sem toque,

10:28

mantendo a monitoração viva. Mas os endpoints MCPs estão completamente protegidos.

10:33

O segredo sensível nunca toca as variáveis de ambiente locais do

10:37

back-end e nunca é exposto ao cliente LLM.

10:41

Agora aqui, pessoal,

10:43

nós consolidamos o comportamento operacional do Docker MCP Gator na borda,

10:48

que a gente vai...

10:50

Testar no laboratório com as métricas de conformidade

10:54

que a gente sabe que é importante.

10:56

Primeiro, falemos do tool, allow e list.

11:00

Um servidor MCP pode implementar dezenas de ferramentas.

11:03

Algumas delas podem ser para fins de auditoria,

11:06

outras críticas e algumas administrativas de risco elevado.

11:09

Em vez de expor a API inteira do servidor diretamente ao LLM,

11:13

o gateway atua como filtro declarativo.

11:18

No arquivo de catálogo, pessoal, nós declaramos,

11:21

a gente pode declarar tipo uma rede de tools,

11:24

apenas com o que está aprovado para ir acessar.

11:28

Qualquer tentativa do LLM de enumerar ou disparar ferramentas

11:31

ocultas é rejeitada imediatamente pelo próprio GitHub,

11:34

sem sequer onerar o back-end.

11:40

O handshake HTTP end-to-end. Em ambiente local,

11:43

usamos o transporte via STDIO, entrada e saída padrão de texto.

11:47

Mas esse modelo não está... não escala para orquestradores de containers, pessoal.

11:51

Então, super importante a gente fazer o handshake para HTTP.

11:55

Para rodar em produção, mudamos o transporte do Python,

11:59

chamando mcp.streamable_http_app.

12:03

O servidor passa a responder via rede sobre HTTP com o servidor

12:12

usando streamable. Então, ou seja,

12:16

essa mudança de transporte viabiliza o deploy em containers isolados,

12:20

permitindo roteamento seguro por rede,

12:23

monitoração de pacotes e uso de balanceadores.

12:32

Agora, pessoal,

12:33

a segurança em produção funciona sob o conceito de defesa em profundidade.

12:38

Não confiamos apenas no código Python do servidor MCP, pessoal.

12:42

Nós configuramos uma aba do Docker para retirar recursos

12:46

e capabilities que o processo não precisa.

12:48

No Linux... Mesmo usuários no root podem retirar capacidades,

12:53

capabilities do kernel. Com a declarativa "-cap -drop=" no docker,

12:58

nós desabilitamos todas as chamadas administrativas por padrão.

13:02

Se o servidor precisar apenas ler e processar requisições,

13:05

ele não tem o direito de alterar o relógio do sistema,

13:07

gerenciar adaptadores de rede ou interceptar pacotes.

13:10

Outra barreira fortíssima é o file system read -only, que é o "-read -only".

13:15

O sistema de arquivos do container é montado como leitura.

13:18

O processo não pode criar novos arquivos ou alterar códigos existentes.

13:22

Para passas temporárias essenciais, notamos o volume e memória,

13:25

que é o "-tmpfs",

13:31

que é de Temporary File System, barra tempo,

13:34

que é o arquivo, a pasta que a gente quer fazer.

13:35

Se o atacante conseguir explorar o processo, ele é incapaz de salvar backdoors,

13:41

baixar escritos maliciosos ou gravar arquivos executáveis.

13:45

A rede isolada garante que o container backend só fale com quem precisa,

13:49

que no caso é o gateway, dentro de uma rede virtual bridge isolada do docking.

13:54

Por fim, pessoal, limitamos recursos.

13:56

Se o LLM entrar em um loop recursivo invocando a mesma ferramenta repetidamente,

14:01

ou se houver um vazamento de memória,

14:03

as diretivas de limitação de CPU e memória impedem que

14:07

o servidor MCP degrade a máquina roxa inteira,

14:10

agindo como proteção contra a negação de serviço, que é o Deny of Service, é o DOS.

14:17

Bem, pessoal,

14:19

o ecossistema Docker...

14:22

ele opera sob o princípio de defaults conservadores e seguros para o padrão.

14:26

O primeiro default relevante do toolkit do Gateway é o limite de memória.

14:31

Definir 2 GB de memória máxima previne que loops recursivos de IA

14:34

ou processamentos pesados de prompts consumam toda a RAM da máquina host.

14:39

Esse guard -rei operacional acaba forçando o desenvolvedor a

14:42

estruturar o servidor MCP com paginação e streaming,

14:45

melhorando a arquitetura global.

14:47

O segundo é o isolamento padrão de arquivos. Por default,

14:50

o servidor MCP centralizado tem acesso zero ao file

14:52

system local do desenvolvedor ou da máquina servidora.

14:56

Apenas diretórios declarados ativamente e montados sob

14:59

demanda podem ser lidos pelo IA,

15:01

reduzindo o vazamento de credenciais locais ou de código -fonte sensíveis.

15:04

O terceiro é a obrigatoriedade de mais assinadas,

15:07

garantindo que o container só execute binários confiáveis do catálogo.

15:11

Por fim, os profiles declarativos evitam o chamado drift de configuração.

15:16

entre máquinas do time.

15:17

O default seguro não visa bloquear a produtividade,

15:22

mas sim remover a possibilidade de falhas ou acessos perigosos dentais.

15:27

Bem, para

15:29

fechar, pessoal, a parte técnica,

15:31

esta é a régua real de revisão de pull requests em engenharia madura.

15:35

Esses quatro pontos são mandatórios em qualquer code review. Primeiro,

15:40

use root. Imagem padrão sem definição de use executa como root.

15:46

A menos que haja justificativa técnica extrema,

15:48

a imagem deve rodar com o drop de privilégios.

15:51

Secrets no docfile .com.br Chaves estáticas

15:58

ou tokens hardcoded nunca devem subir para repositórios.

16:01

Integre o GitLix ou ferramentas de scan de segredos nos hooks de pré-commit do Git.

16:09

Copy sem controle.

16:11

Evite copy indiscriminado sem

16:13

ter um .dockerignore correspondente.

16:18

Isso infla o tamanho das imagens copiando pastas .git,

16:21

pacotes locais .venv e arquivos de ambientes sensíveis,

16:25

o que aumenta o tempo de deploy e vaza dados.

16:27

Sem probes de health check. Sem monitoração de rota ativa,

16:31

você fica cego para falhas em cascata de threads ou deadlocks internos do servidor.

16:37

Pessoal, no laboratório prático que vamos realizar na sequência,

16:39

vocês verão cada um desses conceitos transformando-se em

16:42

comandos reais de auditoria e validação. Bem,

16:46

resumindo a tese operacional que construímos nesta aula,

16:49

containerizar servidores MCP não é apenas um empacotamento estético,

16:53

é a forma que temos de desenhar uma

16:55

barreira rígida em torno da inteligência artificial.

16:58

E lembre-se, o Docker MCP Gator centraliza o long list,

17:02

protege back-end e descansa. O Docker de produção deve ser multistage,

17:07

não multi, monitorado ativamente. O gerenciamento de segredos é movido para a borda,

17:12

comunicando-se via HTTP headers com validação de middleware,

17:16

prevenindo vazamento de variáveis locais.

17:18

A defesa em profundidade limita CPU,

17:21

memória e capacidade de queda do processo de execução.

17:24

Esses conceitos formam a fundação do laboratório prático que vamos fazer.

17:30

Daqui a pouco vamos colocar a mão na massa e ver isso acontecer.

## Resumo IA

[RESUMO_IA]