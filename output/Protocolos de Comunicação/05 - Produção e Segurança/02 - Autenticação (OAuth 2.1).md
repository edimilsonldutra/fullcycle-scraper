Módulo: Protocolos de Comunicação\
Aula: [Autenticação (OAuth 2.1)](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18626)

## Resumo da aula

API key estática falha em ambientes corporativos porque autentica apenas um segredo compartilhado, não a identidade real de quem está acionando a operação. Em um servidor MCP, isso impede distinguir usuário, host e agente, o que enfraquece governança, revogação e rastreabilidade. Retomando o cenário do agente com acesso a operações reais, uma chave colada no código não permite provar se a ação partiu de um usuário autorizado, de um host homologado ou de um fluxo indevido. Sem essa separação, o controle de acesso vira um segredo distribuído em vez de uma política verificável.

Em MCP, a identidade relevante é composta porque a ação não nasce apenas de um ator isolado. O sistema precisa considerar quem iniciou a conversa, qual host intermediou a requisição e qual agente executou a chamada em nome desse contexto. Essa composição existe porque o host atua em nome do usuário ao conversar com o servidor MCP, e o agente herda limites dessa mediação. O efeito prático é que autorização deixa de responder apenas “quem é você?” e passa a responder “quem é você, por meio de qual host, executando qual capacidade?”.

OAuth 2.1 fornece um fluxo padronizado para delegar acesso sem expor credenciais do usuário ao servidor de destino. Ele consolida correções importantes sobre o OAuth 2.0, incluindo a remoção de práticas inseguras como Implicit Grant e a adoção de PKCE no fluxo de autorização. Isso importa em MCP porque o host precisa obter autorização para falar com o servidor em nome do usuário, sem transformar senha em credencial de integração. A identidade como última fronteira vira, aqui, um protocolo governável e revogável.

O Identity Provider corporativo, como Keycloak ou Entra ID, centraliza autenticação e emissão de credenciais de acesso. O usuário se autentica nesse provedor, e o host recebe um Access Token que representa uma autorização concedida dentro das políticas da organização. Essa centralização permite aplicar regras uniformes de login, expiração, revogação e conformidade sem duplicar lógica em cada servidor MCP. O servidor de negócio deixa de autenticar senha diretamente e passa a confiar em uma autoridade de identidade especializada.

Depois da autenticação, o host recebe um Access Token de acesso restrito e o envia nas requisições ao servidor MCP, tipicamente no cabeçalho HTTP. Esse token não é apenas um passe genérico; ele carrega a autorização concedida para aquela combinação de contexto. Retomando o cenário do marketplace, a chamada do agente de busca de SKUs passa a ocorrer em nome de um usuário autenticado, via host autorizado, com token curto e escopo restrito. Isso transforma uma chamada técnica em uma ação governada por identidade.

O servidor MCP não valida a senha do usuário; ele valida o token recebido. Essa validação pode ocorrer por introspecção junto ao autorizador ou pela verificação da assinatura criptográfica de um JWT, dependendo da arquitetura adotada. Ao fazer isso, o servidor descobre se o token é legítimo, a quem pertence, por qual emissor foi gerado e quais scopes estão autorizados. A decisão de acesso passa a ser baseada em evidência criptográfica ou em consulta confiável, não em confiança implícita no cliente.

Scopes definem o conjunto exato de ações permitidas por um token. Eles existem para materializar privilégio mínimo em termos operacionais: o token não libera “acesso ao sistema”, mas capacidades específicas como leitura de um recurso determinado. No exemplo apresentado, um token com read_statement não autoriza escrita, criação de cartão ou acesso a dados fora daquele domínio. Se a IA tentar executar uma ação além do escopo, o backend rejeita a transação imediatamente.

Access Token deve ter vida curta para reduzir o impacto de vazamento, replay e uso indevido prolongado. Quando uma tarefa do agente dura mais do que a validade do token, o client precisa renovar o acesso em background usando um Refresh Token, sem interromper a operação. Esse desenho preserva segurança e continuidade ao mesmo tempo: o token usado na chamada expira rápido, mas a sessão autorizada pode ser mantida sob regras controladas. Em produção, isso é essencial para fluxos longos de análise ou automação.

Rotação de chaves reduz o risco acumulado de comprometimento criptográfico ao trocar periodicamente os materiais usados para assinar ou validar tokens. Ela é especialmente importante quando o ecossistema depende de JWT e de validação distribuída entre múltiplos serviços. O objetivo não é apenas “ter criptografia”, mas manter a confiança operacional mesmo diante de incidentes, revogações ou mudanças de infraestrutura. Credenciais em texto aberto e tokens eternos quebram exatamente essa premissa.

Cada validação de token precisa deixar rastro suficiente para ligar a transação do agente à sessão autorizada que a originou. Isso permite correlacionar o clique do usuário, a execução intermediada pelo host e a decisão final do backend, reforçando a auditoria já exigida em produção. Governança de acesso, nesse contexto, significa que permissões podem ser concedidas, limitadas, rastreadas e revogadas com precisão. Só depois de saber quem pode fazer o quê o isolamento operacional com containers e gateway passa a ter valor completo.

## Transcrição

00:00

Fala galera, beleza? Então vamos voltar agora para entender.

00:04

Como a gente começa a identificar os nossos agentes,

00:08

como a gente faz aquele cara crachá,

00:10

as IAs que estão atuando no nosso sistema.

00:12

Então a gente vai falar um pouquinho sobre

00:13

a identidade de IAs no ambiente corporativo, tá?

00:16

Então a gente vai falar um pouquinho da autenticação com o OAuth 2.1, tá?

00:21

Então na aula passada a gente falou um pouquinho das trancas nas portas,

00:24

certo? Como é que a gente faz para a

00:26

gente blindar o nosso fluxo semântico de ataques,

00:29

de prompt injection e de tail poisoning.

00:32

Beleza, da hora, a gente conseguiu então dar um passo super importante.

00:35

Mas agora vem a pergunta que a gente tem que se fazer o tempo todo.

00:39

Qualquer arquiteto que atua em ambiente corporativo vai pensar,

00:43

como eu sei quem está usando as tools que eu liberei?

00:47

Quem está usando essa ferramenta?

00:48

Como que eu consigo garantir o controle do ambiente,

00:51

saber quem está fazendo o quê? Então quando a gente está olhando para isso,

00:54

a gente precisa conseguir saber qual a identidade

00:57

de cada um dos agentes que estão...

00:58

dentro do nosso sistema. Tanto os agentes pessoais, ou seja,

01:01

as pessoas mesmo ali que estão agindo e interagindo com o nosso sistema,

01:05

quanto os agentes de inteligência artificial.

01:07

Não muda muito quando a gente está falando nesse tipo de... de situação,

01:11

a gente precisa saber também quais são os agentes de AI que estão mexendo.

01:15

Deixa eu explicar melhor para vocês, para vocês entenderem.

01:17

Eu vou dar aqui um case prático do dia a dia que eu

01:20

vejo acontecendo em algumas das organizações com as quais eu atuo.

01:23

Imagina que você tem lá o seu ambiente de marketplace,

01:26

onde você está fazendo a venda de produtos. Eu vou usar marketplace como exemplo,

01:30

para não dar exemplo da minha empresa em específico,

01:33

porque não é legal dar o exemplo direto da minha empresa,

01:36

que nem sempre a gente pode abrir.

01:38

Então vamos fingir que aqui é um marketplace.

01:40

Então no marketplace você tem lá toda a parte de produtos,

01:43

onde você consegue buscar ali os SKUs,

01:46

os itens que você tem de venda e assim por diante.

01:48

O agente de busca de SKUs, por exemplo, não poderia...

01:54

acessar os dados e as informações de RH da empresa. Ou seja,

01:57

ele não pode ir lá e buscar informações sobre salário de cliente e assim por diante.

02:02

Ou ele não pode ir lá e deletar produtos

02:04

ou dar produtos sem deixar sua identificação.

02:07

Você precisa ter um rastro de quem está fazendo o quê e o que cada um pode fazer. Então,

02:11

aqui eu falei de dois assuntos que são super importantes.

02:14

Um deles é quem faz o quê e o outro é como eu identifico quem é quem.

02:18

Porque se eu não conseguir identificar quem é quem,

02:20

eu não consigo colocar as barras, as barreiras de quem pode fazer o quê.

02:24

Certo, galera? Então, voltando ao que a gente está falando.

02:27

No mundo real, ali dentro de grandes empresas, por exemplo,

02:30

a gente não pode só expor ali um servidor MCP.

02:34

Que vai aceitar qualquer conexão de qualquer lugar,

02:36

com uma chave de API estática.

02:38

Então, o cara pode colocar lá no código,

02:40

grudar a sua chave, mas isso vai deixar a nossa governança...

02:46

extremamente vulnerável, é um suicídio. Então,

02:48

quando a gente está falando de uso de IA,

02:50

a gente precisa entender que se a IA decidir

02:53

invocar uma tool para aprovar o crédito, por exemplo,

02:56

ou para consultar algum dado sensível de cliente, o sistema precisa de um crachá,

03:00

precisa saber se ela pode entrar naquele local,

03:02

precisa responder três perguntas fundamentais.

03:06

Quem é o usuário que iniciou a conversa?

03:08

Qual é o host que está intermediando a requisição?

03:11

E quais são os limites exatos de direito que essa combinação possui? Ou seja,

03:17

você está identificando quem está chegando e está sabendo

03:21

o que essa combinação de chave libera de acesso.

03:24

Então, no final das contas, é aquela bela e boa liberação de acesso,

03:28

como eu acabei de mostrar para vocês. O acesso ali de uma...

03:34

Um agente que está na parte, por exemplo,

03:36

de vendas de produtos no marketplace não pode ir

03:39

lá e buscar dados financeiros da empresa.

03:41

Ou ele não pode ir lá e fazer, por exemplo,

03:43

a criação de um novo cartão de crédito para um cliente.

03:46

E assim por diante. Você conseguir identificar e dar os acessos necessários e...

03:52

apenas os necessários, é extremamente importante.

03:55

Então, para resolver isso de forma padronizada,

03:57

sem a gente ter que reinventar a roda,

03:59

a gente vai trazer para o ecossistema agente o padrão de ouro de mercado,

04:02

o Alt 2.0,

04:04

ou seja, a gente não vai inventar nada. Hoje a gente vai entender, então,

04:07

como é que a gente adapta o fluxo de autorização que a identidade

04:11

do cliente e o controle de token assegurem de forma segura entre o host,

04:15

o client e o server. Vamos mostrar isso nas próximas aulas. Beleza, galera? Até já, já.

04:23

Então, vamos lá, pessoal. E como é que é a mecânica dessa brincadeira aqui, tá?

04:27

Vamos entender junto aqui. Não é nada de outro mundo,

04:30

porque a gente está reaproveitando o que a gente conseguiu do Alt 2.1 ali,

04:33

mas é importante a gente falar um pouquinho para vocês entenderem,

04:37

tá? Então, no Alt 2.1, o que a gente resolveu? Quem lembra lá? Então,

04:41

a gente resolveu ali alguns problemas que a gente tinha do 2.0.

04:45

A gente tinha algumas coisas que eram meio inseguras ali

04:48

no 2.0 que a gente conseguiu resolver.

04:50

Então, por exemplo, a parte de Implicit Grant a gente resolveu.

04:53

A gente resolveu ali as melhores práticas com o uso de ProfKey

04:57

para Code Exchange para proteger a troca ali de código por token.

05:02

Mesmo quando a gente estava falando de cliente confidencial, certo?

05:05

Quando a gente está trazendo para o contexto de MCP,

05:07

a gente traz uma camada extra ali de complexidade.

05:09

A gente começa a ter que gerenciar uma outra brincadeira ali no meio do caminho. Pensa comigo.

05:15

O usuário final ali não está interagindo diretamente,

05:18

ele está interagindo com a interface que é o host.

05:21

E o host vai precisar de autorização para poder falar com o MCP server,

05:25

mas em nome do usuário.

05:27

Como é que a gente vai fazer isso? O fluxo,

05:29

então, ele tem que começar com o seguinte,

05:30

o host vai solicitar uma autorização,

05:32

o usuário se autentica ali via Identity Provider da empresa,

05:36

que pode ser um Keycloak ou uma entrada de ID ali. Uma vez autenticado,

05:41

o host vai receber um Access Token, certo?

05:44

E ele vai ter esse access token de acesso restrito.

05:47

E quando o host delega uma ação para o cliente MCP,

05:51

esse token de acesso você vai injetar ele no cabeçalho de transporte de conexão.

05:56

Então, nas requisições HTTP, você vai jogá-lo para dentro.

05:59

O grande pulo do gato é que a identificação do cliente

06:02

do servidor MCP não valida a senha do usuário.

06:04

Ele recebe o token e faz a introspecção

06:07

ou vai validar a assinatura de criptografia desse JWT, certo?

06:13

Através disso, o servidor vai descobrir instantaneamente os scopes

06:17

daquela requisição, daí com isso, ele consegue validar esse token

06:21

que aqui pertence ao Nathan, ele veio através de um host homologado

06:24

da empresa e possui um escopo de read statement,

06:27

por exemplo, se a IA tentar inventar uma ação

06:31

descrita que o token de usuário não suporta, por exemplo,

06:33

o backend vai rejeitar a transação na hora,

06:35

porque ele sabe que aquela troca não funciona. O protocolo, então,

06:39

começa a ser o guardião ali da governança. Então, ou seja,

06:42

você trouxe para a parte de protocolo de comunicação e de troca de

06:46

token essa resolução para não ter acesso a coisas que não deveriam ter.

06:51

Beleza? Aí, para fechar a nossa implementação aqui,

06:54

com a maturidade que a gente precisa ter...

06:56

A gente precisa falar sobre a gestão do ciclo de vida do token.

06:58

Não pode ser um token eterno que não tenha um ciclo de vida bem regularizado.

07:04

Quando a gente está falando ali em ambiente de produção,

07:05

a gente trabalha com o conceito de token de vida curta, certo?

07:08

Um access token,

07:10

ele não deve durar mais do que alguns minutos ou, no máximo, poucas horas,

07:14

mas vamos focar em alguns minutos.

07:16

O que significa que essa arquitetura ali, o MCP client,

07:20

precisa ser inteligente para gerenciar o refresh de token.

07:24

Se o agente de A está engajado em uma tarefa complexa de análise de dados,

07:28

que dura, por exemplo, 20 minutos,

07:30

e o token expira no meio do processo,

07:32

o client precisa ser capaz de ir até o autorizador do servidor,

07:36

em background, renovar o access token usando o refresh token,

07:40

seguro com a rotação de chaves e continuar a operação sem

07:43

quebrar a experiência do usuário e sem expor credenciais de texto aberto,

07:47

pelo amor de Deus. Além disso,

07:50

a gente precisa pensar como liderança

07:53

Como que a gente vai fazer a auditoria disso?

07:55

Cada validação de token precisa gerar um rastro, certo?

07:59

Que a gente consiga atrelar o ID da transação da IA ao ID da sessão do ALF.

08:05

Se amanhã houver uma auditoria de conformidade, uma investigação de segurança,

08:09

alguma coisa assim, a gente consegue mapear a linha exata.

08:12

Desde o clique do usuário, passando pelo pensamento do modelo,

08:14

até a validação de token lá no back-end.

08:17

Dominar esse fluxo aqui dentro do ecossistema é o que

08:20

vai fazer as nossas ferramentas ali que eram...

08:22

uma agente que é isolada, uma malha de serviço que se integra,

08:27

tá? Que seja uma coisa mais robusta.

08:28

A gente consegue trazer segurança pronta para

08:31

passar por qualquer comitê de conformidade,

08:32

certo? Então, basicamente,

08:34

a gente conseguiu descobrir aqui,

08:36

desenhar um fluxo semântico que está protegido pela identidade do usuário,

08:40

que está controlada,

08:41

e agora a gente precisa começar a olhar um pouquinho

08:44

mais uma outra parte do desafio de infraestrutura,

08:46

como a gente empacota tudo isso de forma isolada e imutável.

08:50

A gente vai falar um pouquinho depois do Docker MCP Toolkit

08:52

para a gente conseguir fazer isso nas próximas aulas, beleza?

## Resumo IA

[RESUMO_IA]