Módulo: Protocolos de Comunicação\
Aula: [LAB: Deploy e Gateway parte 1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18609)

## Resumo da aula

A topologia mínima de produção coloca o servidor MCP atrás do Docker MCP Gateway e adiciona a trilha de telemetria com OTel Collector, Prometheus, Tempo e Grafana. Essa composição existe para separar backend e internet, aplicar políticas na borda e produzir evidências observáveis do comportamento do sistema. Retomando o servidor MCP já construído anteriormente, ele continua sendo o mesmo serviço; a mudança nova é o caminho operacional pelo qual ele passa a ser exposto e auditado.

Produção deixa de ser “o processo sobe” e passa a ser “o sistema prova propriedades operacionais sob teste”. As evidências centrais aqui são objetivas: whoami retorna um usuário não privilegiado, o gateway responde 429 sob carga, métricas não ficam expostas publicamente, o handshake MCP funciona ponta a ponta e hosts inválidos são bloqueados por DNS Rebind protection. Esse modelo importa porque segurança operacional só é confiável quando pode ser confirmada por comando, resposta HTTP ou telemetria.

Antes de subir a topologia, o ambiente precisa eliminar causas triviais de falha: Docker Desktop e Docker Compose funcionando, porta 8080 livre, diretório correto do projeto e utilitários como curl e jq instalados. Esses checks não são burocracia; eles reduzem falsos negativos durante os testes e evitam gastar tempo depurando infraestrutura em vez de validar o comportamento do deploy. Quando um pré-requisito falha, a correção deve acontecer antes da execução do restante do fluxo.

O primeiro check operacional é docker compose ps, porque a topologia precisa atingir um estado estável antes de qualquer validação funcional. Esse comando confirma se MCP Financeiro, Gateway e componentes de telemetria estão de pé e ajuda a separar falha de boot de falha de roteamento. Se o problema estiver no serviço MCP, a investigação começa nos logs do backend; se estiver na borda de IA, o foco muda para o Gateway.

O Dockerfile de produção precisa materializar privilégio mínimo no runtime, e a prova prática disso é o container executar como usuário app, não como root. O check docker exec mcp-financeiro whoami deve retornar app; qualquer outro resultado invalida a premissa de isolamento esperada. Retomando a execução non-root já vista antes, o avanço aqui é tratá-la como evidência auditável de prontidão, e não como detalhe de configuração.

O mcp-catalog.yaml define exatamente quais servidores, rotas e tools o gateway pode expor, transformando a borda em um filtro declarativo de capacidades. Sem essa allowlist, um cliente JSON-RPC com bug ou comportamento indevido pode enumerar e alcançar funções internas que jamais deveriam estar publicamente acessíveis. O ponto novo não é a existência da allowlist, já conhecida, mas a validação operacional dela por teste e por logs do gateway.

Chaves de LLM e credenciais transacionais não devem circular livremente no ambiente downstream do container quando o backend não precisa conhecê-las diretamente. O gateway concentra esse acesso na borda e reduz o espalhamento de segredos, o que pode ser verificado com inspeções simples como env dentro do container. A consequência prática é clara: se um segredo aparece onde não deveria, o problema não é teórico, é um vazamento operacional concreto.

Ao sair de STDIO e entrar em HTTP, o servidor MCP passa a depender de proxy, cabeçalhos, roteamento e contrato de transporte para continuar funcional em produção. O handshake via Streamable HTTP é a prova mínima de que a infraestrutura inteira, e não apenas o processo local, consegue entregar o protocolo corretamente. Se a inicialização falhar, a investigação deve mirar protocolo, proxy e Host header antes de culpar a lógica da tool.

O smoke test valida o caminho crítico mínimo do deploy: gateway, proteção de métricas, handshake MCP, tools/list, tools/call em sucesso, tools/call com erro controlado e burst final de requisições. O uso de set -e -o pipefail faz o script abortar na primeira falha real, preservando a causa original do erro e encurtando o diagnóstico. Esse desenho é importante porque um teste de prontidão não deve mascarar falhas em etapas anteriores nem continuar executando sobre um estado já inválido.

O burst final não existe para medir performance geral; ele existe para provar que a borda reage corretamente sob pressão e devolve 429 quando o limite configurado é atingido. Essa resposta é uma evidência operacional de que o rate limit está ativo e de que ataques de enumeração ou abuso não chegam livremente ao backend. Se o burst não produzir o comportamento esperado, a falha está na política de borda, não na business logic da tool.

DNS Rebind protection impede que um host aparentemente legítimo seja resolvido de forma maliciosa para alcançar destinos indevidos através da borda. No contexto do laboratório, a validação não é conceitual: hosts inválidos precisam ser bloqueados de forma observável. Isso importa porque, em um gateway exposto, confiar apenas no nome solicitado sem validar a política de host abre espaço para desvio de tráfego e quebra do perímetro esperado.

A telemetria do fluxo conecta execução funcional e rastreabilidade operacional por meio de spans, traces e visualização centralizada. Quando o smoke test roda, cada etapa relevante pode aparecer no Grafana e no Tempo, permitindo enxergar o caminho de execução e localizar rapidamente o ponto de falha. Retomando a observabilidade já conhecida, a camada nova aqui é usá-la como prova de deploy saudável e como mecanismo imediato de troubleshooting.

A leitura correta do ponto de quebra acelera a correção: falha em métricas aponta para a borda, falha em initialize sugere problema de proxy ou cabeçalho, falha em tools/call concentra a análise na tool, e falha no burst desloca o foco para rate limit. Esse encadeamento transforma o laboratório em checklist executável, não em tentativa e erro. Um deploy pronto para produção é aquele em que cada falha possível já tem um ponto inicial claro de investigação.

## Transcrição

00:01

Pessoal, vamos para mais um laboratório. Então, olha só.

00:05

A primeira coisa que você precisa entender é

00:08

que nós estamos aqui não apenas para fazer deploy,

00:13

tá? Nós estamos aqui para construir uma borda de API profissional. Então,

00:17

muita gente acha que para a produção é dar um Docker build,

00:21

abrir a porta e torcer para o melhor,

00:23

né? Cruzar os dedos. Mas quando você expõe o servidor MCP,

00:27

que tem acesso ao banco de dados,

00:30

Chaves de autenticação, PNI, contêiner solto na rede,

00:34

é um convite para o desastre, pessoal.

00:38

Nós vamos tratar a produção como um conjunto de decisões arquiteturais.

00:42

Nós vamos pegar o nosso servidor MCP e

00:45

orquestrá-lo através de uma borda inteligente,

00:47

que é o Docker MCP Gateway.

00:49

O seu back-end não conversa mais direto com a internet.

00:52

É o Gateway que vai fazer o papel de leão de chácara.

00:55

Ele bloqueia acessos indevidos via to-allow list.

00:59

Isola as suas credenciais e despacha toda a

01:02

telemetria da operação para os coletores.

01:05

E nós não vamos ficar na teoria.

01:08

Por exemplo, se um tech lead perguntar, isso é seguro de verdade?

01:12

Eu não vou responder, acho que sim.

01:14

Nós vamos rodar scripts provando que o usuário do container é non-root,

01:20

ele não é um usuário root, em outras palavras,

01:26

que as chaves não vazam.

01:28

E que ataques de enumeração morrem na borda, tá?

01:31

Muito antes de encostar no seu código. Então, guarde essa frase.

01:36

Produção não é sobre fazer o código rodar.

01:38

É sobre fazer o código rodar com isolamento, controle e evidências operacionais.

01:45

Então, pensando aqui nas etapas, olha.

01:47

A primeira é o setup e o Dockerfile non-root,

01:54

tá? A palavra importante aqui é auditar.

01:57

O arquivo precisa garantir privilégios mínimos, tá bom?

02:01

A segunda é o To Allow List.

02:05

O MCP Gateway atua como leão de chácara de ar. Ele diz quais rotas,

02:10

tools e permissões o seu servidor pode expor para os clientes de LLM.

02:14

Então, você configura o

02:15

mcp-catalog e valida, tá?

02:22

Agora, a terceira estação foca no Secrets Management.

02:27

Então, passar API Key em um ambiente aberto de contêiner é perigoso. Então,

02:31

o MCP Gateway ajuda a gerir e isolar esses segredos no runtime exposto.

02:36

E a quarta estação consolida o transporte end-to-end e a telemetria. Então, olha só,

02:45

o Handshake MCP via Streamable HTTP garante que o produto se comunica ponta a ponta.

02:52

End-to-end. E ao injetarmos o erro intencional,

02:55

a observabilidade prova que o caos é

02:58

rastreado e resolvido instantaneamente no Grafana. Bem,

03:05

então a pergunta que move esse laboratório é,

03:10

eu sei construir um servidor MCP,

03:13

eu sei rodar MCP Dev, mas como isso vai para a produção em escala?

03:18

Em desenvolvimento local, o foco é, a ferramenta funciona?

03:22

Em produção, a pergunta vira. Consigo operar isso com segurança,

03:25

controle de tools e rastreabilidade?

03:27

A gente não está trocando o servidor MCP do módulo 3,

03:32

pessoal, por outra coisa. O servidor continua sendo o mesmo.

03:35

O que muda é que agora ele passa a rodar através de um gateway específico para IA,

03:39

que é o Docker MCP Gateway.

03:41

Então o laboratório organiza essas cinco práticas auditáveis.

03:44

A primeira é usuário no root no container,

03:47

para evitar que processos comprometidos façam estragos no host.

03:52

A segunda é o True Allow List.

03:54

Uma True MCP pode disparar LLM, banco ou API externa.

03:59

Expor tudo é um risco enorme.

04:01

A regra deve autorizar explicitamente o que passa. A terceira é Secrets Management,

04:07

ou seja, isolar chaves críticas. A quarta é o MCP Handshake End-to-End, ou seja,

04:12

provar que o streamable HTTP cruza a infraestrutura e entrega o contrato do protocolo.

04:18

E a quinta é a telemetria hotel,

04:21

que no final do dia, pessoal,

04:22

a gente vai fazer junto com a quarta. Ou seja, porque se quebrar,

04:27

você não quer procurar logs em texto no terminal,

04:29

quer ver o trace ID vermelho no dashboard.

04:34

Então, de novo, aqui não estamos falando de recomendações,

04:39

estamos falando de evidências verificáveis.

04:42

Ou o container roda como usuário não privilegiado ou não roda.

04:46

Ou o gateway devolve 429 sob carga ou não.

04:51

Ou as métricas estão isoladas da internet ou não.

04:54

Ou o handshake MCP continua funcionando para ponto ou não.

04:57

Ou a proteção contra DNS Rebind bloqueia hosts inválidos ou não.

05:02

Ou seja, repare que todas as evidências podem ser comprovadas por comandos,

05:06

respostas HTTP ou comportamento observável.

05:09

Essa é a diferença entre dizer que algo está seguro e demonstrar que está seguro.

05:14

Então, ao longo do laboratório,

05:15

nós vamos validar cada uma dessas evidências individualmente. Então,

05:22

guarde essa ideia simples, pessoal. Em produção,

05:24

segurança não é uma opinião, é uma evidência.

05:30

Tem pré-requisitos. Então, o objetivo desse slide não é ensinar Docker, pessoal,

05:36

nem rede, ou menos ferramentas. É eliminar causas comuns de erro antes da execução.

05:42

Primeiro, confirme que o Docker Desktop e o Docker Compose estão funcionando.

05:46

Depois, verifique se as portas necessárias estão livres,

05:48

principalmente a 8080 usada pelo Gateway. Em seguida,

05:51

confirme que você está no diretório correto do laboratório. E, por fim,

05:55

valide que as ferramentas de apoio estão instaladas, especialmente o Curl e o JQ,

05:59

que a gente vai usar durante os testes.

06:03

Se algumas dessas verificações falharem, vale resolver agora.

06:06

É muito fácil corrigir o ambiente nesse momento do

06:08

que interromper o laboratório no meio da execução.

06:11

Então é, menos tempo debugando infraestrutura,

06:13

mais tempo validando as evidências do laboratório, tá, galera?

06:17

Bem, a etapa zero. Subimos a pequena topologia de produção.

06:22

MCP financeiro, MCP Gateway, Hotel Collector, Prometheus, Tempo e Grafana.

06:28

Vocês vão ver que tem alguns termos que estão aqui,

06:31

Pessoal, que são termos de mercado.

06:32

Sugiro vocês darem uma pausa aqui,

06:35

façam uma pesquisa rápida, só para vocês contextualizarem,

06:40

mas não precisam se preocupar. O código está pronto, ele está rodando,

06:43

vocês vão ter pontos específicos que vocês precisam editar no laboratório,

06:46

que o objetivo aqui não é ensinar essas ferramentas,

06:49

é você saber que elas existem e como usá-las, tá? No final é isso.

06:53

Então, o primeiro check é doc.compose.ps, tá?

06:57

E preste atenção que o estado da arquitetura tem que estar estável, tá?

07:01

A comunicação é feita via HTTP, a borda agora entende os pacotes do MCP.

07:06

No anterior, lembra, a gente estava usando STDIO, fica a dica aqui,

07:10

tá? Se o problema for boot, olhe os logs do MCP Financeiro.

07:14

Se for na orquestração de IA, olhe o MCP Gateway.

07:19

A etapa 1 garante que você entenda o conceito de menor privilégio.

07:22

O Dockerfile cria o usuário e executa a user app.

07:26

E a auditoria ao vivo acontece via docker exec mcp financeiro whoin.

07:32

Que precisa... Who am I? Desculpa,

07:38

pessoal. Que precisa retornar app.

07:41

Para a Tech Lead, esse tipo de validação é a referência oficial.

07:45

Dockerfile de produção não define só build, define fronteira de segurança.

07:51

Na etapa 2, agora chegamos a uma das maiores inovações de usar o Docker MCP Gator,

07:56

que é gerenciar as ferramentas da borda.

07:58

Através do mcp-catalog.ialm,

08:03

nós instruímos o gateway sobre exatamente quais servidores

08:08

e quais rotas ele vai orquestrar. Sem a low-list,

08:10

qualquer cliente conectado via JSON-RPC tem total capacidade de

08:14

explorar o catálogo inteiro do seu backend. Com ele,

08:17

um bug de cliente não expõe todas as suas funções internas de IA.

08:21

A gente não decora o IAM, tá, pessoal?

08:23

A gente usa o teste para provar.

08:26

E os logs mostram se o to-alone list está sendo respeitado.

08:32

A etapa 3, pessoal, é importante a gente ter foco aqui com o seguinte.

08:37

Em segurança defensiva, credenciais abertas são... bombas relógio. Em MCP,

08:42

não lidamos com as chaves de LLM APIs transacionais. O objetivo aqui é isolar.

08:47

As variáveis sensíveis, como a API que dá Antropic, que eu tenho usado somente aqui,

08:53

que eu sugiro que vocês façam isso,

08:55

elas não ficam soltas. Elas devem estar no local apropriado.

08:58

E o Gateway ajuda a orquestrar o acesso sem

09:01

vazar tudo no ambiente de container downstream,

09:03

se não for necessário. Nessa métrica,

09:06

a gente garante que executar um simples ENV no container

09:09

não espalha os segredos de arquitetura por toda parte.

09:16

Agora chegamos ao teste fim a fim. Até aqui validamos componentes isolados.

09:21

Container, gateway, rate limit, proteção de métricas.

09:25

Agora precisamos provar que o sistema continua

09:28

funcionando depois de todas as camadas.

09:30

O smoke test existe para isso.

09:33

Ele não tenta validar todas as funcionalidades.

09:35

Ele valida o caminho crítico mínimo da aplicação.

09:38

O teste roda. O teste roda via o seguinte comando,

09:44

Bash testes barra smoke.sh.

09:48

Repara na sequência. Primeiro o Gator,

09:51

depois a proteção de métricas, depois o Handshake MCP,

09:54

depois o tools barra list, depois o tools barra call e cenário de sucesso,

09:58

depois o tools barra call e cenário de erro controlado. E por fim,

10:03

um burst de requisições para validar o comportamento sob pressão.

10:06

Cada etapa depende de deterioro. Por isso, o script usa set -e -o pipefail.

10:11

Na primeira falha, ele para imediatamente. Isso reduz muito o tempo de diagnóstico.

10:16

Se falhar em métricas, eu investigo o getter. Se falhar em initialize,

10:20

eu investigo o proxy, protocolo e host header.

10:23

Se falhar em tools barra call, eu investigo a tool.

10:26

Se falhar no burst, eu investigo o rate limit.

10:29

O esperado é simples, tá, pessoal? Sete validações concluídas com sucesso.

10:33

E existe um bônus interessante.

10:35

Cada execução gera spans que aparecem no Grafana a tempo.

10:39

Isso conecta a validação funcional com a observabilidade.

10:43

Você não apenas sabe o que o fluxo executou,

10:46

você consegue enxergar o caminho de execução.

10:49

E aqui acontece a primeira mudança de modelo mental da aula.

10:52

Antes o MCP rodava totalmente via STDIO. Agora ele roda em HTTP,

10:57

através de um Gator, com rate limit, isolamento de métricas e observabilidade.

11:01

Isso introduz preocupações reais de produção. Rede, proxy, cabeçalhos, status codes,

11:06

telemetria. Então, guarda essa ideia. Smoke test bom não tenta provar tudo.

11:11

Ele prova o suficiente para impedir deploy às cegas.

11:19

Então, pessoal, aqui é quando o nosso laboratório vira exercício.

11:25

Vocês vão ler isso aqui.

11:26

Eu vou dar pausa aqui no vídeo e eu continuo depois.

11:30

Eu volto aqui para a gente repassar o laboratório.

## Resumo IA

[RESUMO_IA]