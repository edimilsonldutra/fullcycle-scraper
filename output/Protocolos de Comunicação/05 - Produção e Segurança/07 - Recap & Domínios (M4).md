Módulo: Protocolos de Comunicação\
Aula: [Recap & Domínios (M4)](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18612)

## Resumo da aula

Segurança em MCP se organiza em três camadas porque os riscos não são do mesmo tipo. Transporte decide quem pode entrar e sob quais credenciais; runtime limita o dano possível depois da entrada; conteúdo controla o que o modelo passa a tratar como instrução. Retomando o cenário do servidor MCP em produção, esse mapa evita a falsa sensação de que um único controle, como Docker ou autenticação, resolve o sistema inteiro.

A camada de transporte usa OAuth 2.1, TLS, PKCE e scopes para impedir interceptação, abuso de token e falsificação de identidade do host. A camada de runtime reaproveita o isolamento já visto com Docker MCP, mas o ponto novo aqui é a síntese: non-root, sandboxing e secrets fora do código não decidem acesso, e sim contenção de impacto. A camada de conteúdo existe porque, em sistemas com LLM, dado externo pode ser reinterpretado como comando; por isso sanitização, esquemas estritos e fencing de output protegem a fronteira semântica.

As vulnerabilidades mais relevantes do OWASP for LLM no contexto de MCP são LLM01, LLM06 e LLM05 porque atravessam a cadeia completa entre texto, ferramenta e ação. O risco central não é apenas o modelo errar, mas o modelo receber instruções disfarçadas de dados, operar ferramentas com poder real e produzir saídas que outro sistema executa sem validação. Essa leitura muda a análise arquitetural: o problema deixa de ser “qual prompt entrou” e passa a ser “qual fluxo operacional foi acionado”.

LLM01, Prompt Injection, ganha peso extra em MCP porque o ataque pode ser indireto. Uma tool, uma página externa, um arquivo ou uma API devolve texto que entra no contexto do modelo e tenta se comportar como instrução. O controle correto não é “confiar no texto porque veio de uma integração”, e sim tratar texto externo como dado não autoritativo.

LLM06, Excessive Agency, aparece quando a LLM tem acesso a tools que criam tickets, alteram recursos, chamam APIs de cobrança ou executam ações destrutivas. O problema se divide em functionality, permissions e autonomy: o que a tool faz, com quais permissões e com quanta liberdade de execução. Se o custo do erro é alto, a arquitetura precisa inserir human in the loop em vez de automatizar a cadeia inteira.

LLM05, Output Handling, descreve o momento em que a saída do modelo vira entrada de outro sistema. Quando o output é usado para montar SQL, compor comandos de shell, renderizar HTML ou chamar APIs sem validação, o sistema reabre classes clássicas de falha por um caminho novo. O LLM não substitui a segurança tradicional; ele desloca o ponto em que ela precisa ser aplicada.

Retomando o mesmo cenário de servidor MCP em produção, imagine uma tool que lê uma página externa e entrega o texto ao modelo para resumo. Se a página contém uma instrução escondida para ignorar políticas e chamar outra tool, o incidente começa como LLM01. Se a tool seguinte tem permissões amplas demais para alterar algo real, o problema evolui para LLM06; se a resposta final é consumida por um sistema que executa comandos ou monta SQL sem validação, ele fecha em LLM05.

Esse encadeamento produz um checklist mental útil para troubleshooting. A primeira pergunta é de onde veio o conteúdo interpretado pelo modelo; a segunda é qual ferramenta estava disponível e com qual permissão; a terceira é quem consumiu a saída depois. Esse trio localiza a falha na camada semântica, na camada de agência ou no consumo downstream.

PKCE existe para impedir que o authorization code, se interceptado, seja suficiente para obter um access token. Sem PKCE, um atacante que observe esse code em redirect URI malicioso, log de proxy, histórico ou outro ponto de exposição pode trocá-lo pelo token e assumir a autorização. O code não é o token final, mas é um bilhete transitório poderoso; por isso ele não pode circular desacoplado do cliente legítimo.

Com PKCE, o authorization code só pode ser trocado quando acompanhado do code verifier original gerado no início do fluxo. O authorization server compara o verifier apresentado com o desafio derivado anteriormente e confirma que quem conclui a troca é o mesmo cliente que a iniciou. A proteção real, portanto, não é “mais segurança em geral”, mas defesa contra roubo ou replay do authorization code.

No contexto de MCP, essa exigência não é opcional porque OAuth 2.1 tornou PKCE obrigatório para clients public e confidential, e o protocolo herda essa postura. O detalhe operacional importante é a geração do verifier com RNG criptograficamente seguro, como secrets.token_urlsafe; um valor previsível enfraquece exatamente o mecanismo que deveria amarrar início e fim do fluxo. Revisão séria de autenticação verifica uso efetivo de PKCE, armazenamento correto do verifier e qualidade criptográfica da geração.

Secrets fora do código significam que credenciais de produção não devem ser embutidas em fonte, imagem ou configuração versionada. Em MCP, isso importa porque a cadeia inclui modelo, gateway, backend e ferramentas, ampliando os pontos de exposição acidental. A prática correta é manter o segredo na borda ou em mecanismo dedicado de secret management, reduzindo o alcance de vazamento e evitando que o backend ou a LLM carreguem credenciais desnecessárias.

Prontidão operacional não se prova com “o container subiu”, mas com evidências observáveis. O piso mínimo consolidado aqui tem cinco métricas: processo rodando como non-root, gateway limitado em vez de permissivo, endpoints públicos estritamente controlados, health check medindo saúde real e smoke test exercitando uma chamada MCP de verdade. Cada uma responde a uma pergunta diferente sobre contenção, exposição, recuperabilidade e validade do deploy.

A ordem dessas métricas também serve como roteiro de diagnóstico. Primeiro confirme o usuário de runtime; depois verifique se a borda está filtrando o que deve expor; em seguida revise quais rotas estão públicas; só então avalie se o health check detecta degradação real e se o smoke test percorre o caminho crítico completo. Produção começa quando o sistema consegue provar que está saudável, limitado e recuperável.

AIOps, neste contexto, não é uma ferramenta específica nem automação mágica. O termo descreve maturidade operacional aplicada a servidores de IA: empacotar corretamente, impor limites, medir comportamento, validar saúde e testar o fluxo fim a fim com evidência observável. A operação segura surge da disciplina de checks e controles, não do uso isolado de uma plataforma.

MCP foi tratado como eixo vertical porque conecta um host a ferramentas e recursos por meio de servidores especializados. A2A desloca o problema para o eixo horizontal, no qual agentes descobrem capacidades uns dos outros, coordenam trabalho e negociam tarefas. Essa distinção importa porque não faz sentido conectar agentes entre si antes de dominar a operação responsável do servidor de ferramentas que sustenta essas interações.

## Transcrição

00:01

Pessoal, vamos lá.

00:04

O grande

00:06

ponto dessa revisão, pessoal,

00:09

é que a gente está aqui num momento super interessante,

00:14

em que a gente está focando produção e segurança, né?

00:20

E a gente sai aqui de um mundo onde o servidor MCP,

00:26

ele passa, né?

00:32

do laboratório, ou seja,

00:34

da exploração e entra em produção.

00:36

E quando isso acontece, a gente muda a pergunta.

00:39

A gente não só pergunta se funciona.

00:43

Agora a gente quer saber se funciona de forma segura, observável e controlável.

00:48

Porque produção não perdoa a ambiguidade. Ou seja,

00:51

se você não entende exatamente o que cada camada protege,

00:53

depois fica muito difícil saber onde procurar quando o sistema dá erro.

00:59

Então, é o esquema da... Mostra a pergunta, vocês param um pouquinho, pensam,

01:04

eu mostro a resposta e a gente discute, tá bom? Mesmo esquema das outras. Então, vamos lá.

01:10

Focando aqui nas três camadas de defesa. Então, aqui é o seguinte.

01:18

Quais são as três camadas de defesa de um servidor MCP? E o que cada uma protege?

01:26

Bem, vamos lá.

01:30

A resposta, ou seja...

01:35

três camadas, né? Obviamente, três ataques diferentes, né? Então, vamos lá.

01:41

Então, segurança MCP não é só proteção única. Não existe colocar OAF e pronto,

01:47

tá? Não existe ROD e container e pronto. Ou seja,

01:50

cada camada reduz um tipo diferente de risco.

01:53

Então, a primeira camada é o transporte,

01:55

que é o OAF 2.1. Ou seja, aqui entram TLS,

02:00

PKCE, Scopes. O objetivo é impedir interceptação,

02:04

abuso de token ou alguém se passando por Roche legítimo.

02:08

E repara numa confusão comum. Está seguro porque roda em Docker.

02:15

Docker não resolve transporte, pessoal. Docker não autentica o Roche.

02:19

Docker não controla o escopo de acesso. A segunda camada é Runtime.

02:23

No caso, o que a gente desenvolveu foi o Docker MCP.

02:27

E aqui entram... sandboxing, processo no root e secrets fora do código.

02:34

Agora o problema muda,

02:36

não é mais quem entra, é o que consegue acontecer dentro do ambiente.

02:43

Ou seja, tu vulnerável, permissão excessiva, acesso indevido a file system.

02:48

Normalmente é aqui que incidentes operacionais começam a escalar. Então,

02:53

o runtime existe para limitar dano. A terceira camada é conteúdo.

02:58

Então vamos lá, sanitizar.

03:01

esquemas estritos e fence de output. Ou seja,

03:04

porque em sistemas com LLM o problema não é só receber dado.

03:07

É o modelo interpretar aquele dado como instrução.

03:11

Uma ferramenta pode devolver conteúdo malicioso, uma página pode induzir comportamento,

03:15

um output pode contaminar o fluxo seguinte. Ou seja,

03:19

transporte não resolve isso, runtime sozinho também não.

03:22

E a frase final que resume muito bem esse trade-off.

03:28

As três custam...

03:30

As três custam pouco juntas. Agora, ficam caras quando falta uma.

03:34

Então, vamos guardar esse mapa mental aqui. Transporte decide quem entra,

03:39

Runtime limita o que acontece dentro e o conteúdo controla o que vira instrução.

03:47

Bem, como vocês podem ver, pessoal, eu já trouxe a pergunta e a resposta.

03:53

Mas vamos continuar mesmo assim. Vamos lá.

03:56

A segunda pergunta aproxima o módulo de uma taxonomia externa.

04:01

Que é o OASP for LLM,

04:04

ou seja, OASP para LLM. Ou seja, a pergunta é,

04:07

Das 10 vulnerabilidades do OASP for LLM de 2025,

04:11

quais três importam mais no MCP e por quê? Então, antes da resposta,

04:16

pessoal, a gente precisa focar no contexto do MCP.

04:20

O que muda quando o LLM não está só gerando o texto, mas coordenando as ferramentas?

04:25

Pensa nisso por um segundo. Então, olha só,

04:27

MCP conecta modelo, host, servidor e ferramentas.

04:30

Então, as vulnerabilidades mais importantes tendem a

04:32

ser aquelas que atravessam essa fronteira.

04:35

Instrução entrando como dado,

04:37

agência excessiva e output usado sem tratamento. Então,

04:41

as respostas são três. É o LLM01, o 06 e o 05.

04:45

A ordem importa menos do que a lógica.

04:47

A pergunta não está pedindo para decorar códigos.

04:50

Ela está pedindo para entender por que essas três aparecem com força no MCP.

04:56

Então, a primeira é o LLM0.1, que é o Prompt Injection.

05:00

E o detalhe que importa, direto e indireto. Ou seja, esse I é fundamental.

05:07

Prompt injection direto é quando o usuário tenta manipular o modelo explicitamente.

05:12

Indireto é mais sutil. O modelo lê conteúdo ouvido de uma ferramenta,

05:15

de um arquivo, de uma página,

05:17

de uma API e aquele conteúdo tenta se comportar como instrução. Ou seja,

05:22

o MCP amplifica esse risco porque ferramentas externas devolvem

05:25

dados que entram no contexto do LLM.

05:27

E o LLM, por natureza,

05:29

trabalha... lendo o texto e inferindo intenção. Ou seja,

05:33

então o dado precisa ser tratado como dado, não como autoridade.

05:37

A segunda é o LLM06, que é o Acessive Agency. Ou seja,

05:42

aqui o problema não é só o modelo falar algo errado.

05:45

O problema é o modelo ter ferramentas com ações reais,

05:49

criar ticket, mandar mensagem, consultar banco,

05:52

alterar recurso, deletar arquivo, acionar pipeline,

05:56

chamar API de cobrança. Ou seja... Essa vulnerabilidade tem três subcategorias.

06:01

Functionality, Permissions e Autonomy. Ou seja, o que a ferramenta pode fazer,

06:06

com que permissão e com quanta autonomia.

06:10

Ações destrutivas exigem human in the loop.

06:15

Essa frase é uma regra prática. Se o custo do erro é alto,

06:18

não deixa a cadeia totalmente autônoma só porque tecnicamente dá para deixar.

06:25

A terceira é o LLM05, que é o Output Handling.

06:29

Essa vulnerabilidade é muito concreta em arquitetura.

06:32

Output do LLM vira input downstream, ou seja,

06:35

isso significa que a resposta do modelo pode virar query SQL,

06:39

argumento de shell, HTML renderizado, payload para API, comando de automação.

06:45

Se você trata o output como confiável,

06:48

você importa classes tradicionais de falha, SQL injection, shell exec,

06:55

XSS, ou seja, o ponto é que o LLM não elimina a segurança clássica.

06:59

Ele reintroduz segurança clássica por um caminho novo.

07:03

E repara no que não aparece aqui como resposta principal,

07:06

pessoal. Não é só modelo alucinando.

07:09

Alucinação é importante. Mas em MCP,

07:11

o risco arquitetural mais forte está no acoplamento entre texto,

07:15

ferramenta e ação. O modelo pode ler instrução escondida,

07:18

pode ter permissão de mais e pode produzir

07:21

saída que outro sistema executa sem validação.

07:25

Agora, se eu estivesse debugando um incidente de MCP,

07:29

eu faria três perguntas inspiradas nessa resposta.

07:32

Primeira, de onde veio o conteúdo que o modelo interpretou? Segunda,

07:37

que ferramenta estava disponível e com qual permissão? Terceira,

07:41

quem consumiu a saída do modelo depois?

07:43

Essas perguntas ajudam a localizar se o problema foi prompt injection,

07:47

agency ou output handling.

07:49

Vamos pegar um exemplo simples, pessoal.

07:51

Uma tool lê uma página externa e devolve o texto para o modelo resumir.

07:55

No meio da página existe uma instrução maliciosa dizendo

07:58

para ignorar políticas e chamar outra tool.

08:00

Se o modelo obedece, estamos em LLM01.

08:04

Se a outra tool tem permissão ampla demais para alterar algo real, LLM06.

08:09

Se a saída final é enviada...

08:12

para um sistema que executa comandos ou monta SQL sem validação, LLM05.

08:17

Então, um incidente atravessa as três.

08:20

Guarda essa frase, pessoal. Em MCP, texto não é só texto. Texto pode virar ação.

08:25

Esse é o argumento que você leva para uma conversa de arquitetura

08:28

quando alguém diz que segurança de LLM é só filtrar prompt.

08:33

Se a sua resposta mental criou prompt injection indireto,

08:36

permissões de tool e validação do output,

08:38

você está no eixo certo. Se você ficou só em nome de vulnerabilidade,

08:42

volta na camada consequência operacional, pessoal.

08:46

O domínio aqui é entender por que MCP muda o peso relativo entre riscos, tá?

08:53

Vamos lá. Aqui também, né? Pus a pergunta e já entreguei a resposta.

08:57

Vamos seguir, vamos lá. A terceira pergunta, pessoal, ela é mais específica, né?

09:02

Mas ela trata uma coisa muito importante.

09:04

Você entende OAF como um mecanismo de segurança?

09:07

Ou só como uma palavra que aparece em autenticação?

09:10

A pergunta é, por que PKCE é obrigatório no MCP? Ou, mais afiado,

09:16

qual ataque o PKCE evita e por que o MCP exige e não só recomenda?

09:23

Antes da resposta, pessoal, tenta formular assim.

09:25

Qual é o objetivo que o atacante tenta roubar?

09:29

E por que esse objetivo sozinho não deveria bastar?

09:33

A palavra central é Authorization Code.

09:37

PKCE existe para reduzir o risco de interpretação desse code no fluxo OAF.

09:44

Sem PKCE, se alguém intercepta o code e consegue trocá-lo por token,

09:49

o estrago pode ser completo. Com PKCE, o code sozinho não basta.

09:55

A resposta curta é anti-interceptação de authorization code.

10:00

Vamos ver como funciona. Primeiro...

10:04

O case sem PKCE, um atacante intercepta o code por um redirect URI malicioso, um log de proxy,

10:11

um histórico ou algum ponto onde esse código

10:15

Aparece indevidamente e troca por um access token.

10:19

Repare que o code, nesse caso, vira uma credencial transitória poderosa.

10:24

Ele não é o token final, mas é o bilhete que permite chegar ao token.

10:28

Se alguém pega esse bilhete e consegue usar,

10:30

você perdeu a propriedade de segurança do fluxo. Agora o contraste, pessoal.

10:35

Com o PKCE, vamos ver. O code sozinho não vale.

10:40

Ele tem que vir com o code verifier original.

10:44

E esse code verifier foi criado no início do fluxo pelo cliente legítimo.

10:49

O authorization server recebe primeiro o desafio derivado dele e depois

10:53

confere se quem está trocando o code consegue apresentar o verifier correto.

10:59

Então o atacante pode até ver o code,

11:01

mas não consegue completar a troca se não tiver o segredo correspondente.

11:07

Então esse é um bom momento para o reframe.

11:10

PKCE não é mais uma opção de configuração OAF,

11:13

PKCE é uma marra entre quem iniciou o fluxo e quem tenta concluir o fluxo.

11:19

O problema aqui não é autenticar o usuário de novo,

11:22

é provar que o cliente que recebeu o code é o mesmo que começou a dança.

11:29

E por que MCP exige?

11:31

Porque o ARF 2.1 tornou o PKCE obrigatório

11:34

para todos os clients confidential e public.

11:38

E MCP herdou, tá? Então, o detalhe aqui é que por muito tempo,

11:43

muita gente associou o PKCE principalmente a public clients,

11:47

tá? Como mobile ou SPA.

11:51

Onde há um segredo de cliente confiável, tá?

11:54

Mas o movimento moderno é tratar PKCE como...

11:58

uma proteção geral contra interceptação de authorization code,

12:03

não como um luxo opcional. E tem um bônus que aparece pequeno, mas é muito prático.

12:08

Code Verifier deve ser gerado por um RNG criptograficamente seguro,

12:14

algo como Secrets.token, Adelaide e URL Safe.

12:19

Nunca um addon comum. Se o Verifier é previsível,

12:23

você enfraquece justamente o mecanismo que deveria proteger a troca.

12:27

Em segurança, pessoal,

12:29

aleatoriedade ruim costuma aparecer funcionalidade até alguém explorar.

12:35

O sistema passa nos testes felizes,

12:37

mas falha no modelo de ameaça.

12:40

Se eu estivesse revisando o código de autenticação no server MCP,

12:44

eu procuraria três coisas.

12:45

Primeiro, o fluxo usa o PKCE mesmo? Segundo,

12:48

o Code Verifier é armazenado de forma correta entre o início e o callback?

12:53

Terceiro, ele foi gerado com forte criptografia?

12:56

com fonte criptograficamente segura,

12:58

eu não aceitaria funcionar no login como prova suficiente.

13:03

Login funcionar é o caso feliz.

13:05

Segurança pergunta o que acontece quando o code

13:07

é observado por alguém que não deveria. Então, guarda essa frase.

13:12

No off moderno, o code não pode ser uma chave solta.

13:16

Ele precisa estar preso ao cliente que começou o fluxo.

13:21

Se você respondeu mentalmente PKCE evita roubo ou replay do authorization code, está no eixo certo.

13:27

Se você respondeu PKCE melhora a segurança, mas não soube dizer qual o ataque,

13:31

volta à aula de OAF. Em arquitetura, pessoal,

13:34

Dizer melhora a segurança é vago demais.

13:38

O que convence é apontar ameaça, mecanismo e consequência.

13:43

Bem, quarta pergunta.

13:47

Então, agora a gente chega na pergunta mais operacional da aula.

13:50

Quais são as cinco métricas que o Lab 20 ensinou para

13:54

dizer se o servidor MCP está pronto para produção?

13:57

Então, antes da resposta, pessoal, pensa como alguém que vai aprovar um deploy.

14:02

Você não quer opinião, você quer cheques observáveis.

14:06

Ou o que eu consigo testar, o que eu consigo verificar,

14:10

o que falta de forma visível,

14:12

tentar listar mentalmente, usuário no root, rate limit,

14:16

send points protegidos, health check, smoke test,

14:19

enfim, enfim, ou seja, esses cinco não cobrem tudo que existe em produção,

14:23

mas são um piso muito bom para concluir, subiu, é,

14:27

é, é, é, subiu com está pronto, tá?

14:33

Então, ó, é, pessoal,

14:38

Se eu estivesse debugando um deploy que subiu, mas não funciona,

14:42

eu seguiria a ordem desses cinco. Ou seja,

14:45

primeiro, com que usuário o processo está rodando? Segundo,

14:49

o gateway está limitado ou deixando tudo passar?

14:51

Terceiro, o que está exposto publicamente? Quarto,

14:54

o health check mede saúde real ou só processo vivo?

14:58

E quinto, o smoke test faz uma chamada MCP de verdade ou só bate na raiz?

15:04

Então, guarda essa frase, pessoal.

15:05

Produção começa quando o sistema consegue provar que está saudável,

15:09

limitado e recuperável, tá?

15:15

Bem, então, pessoal, agora a gente chega no fechamento conceitual do módulo, tá?

15:22

Então, ou seja, aqui, gente, o termo AIOps, por exemplo, pode ser usado...

15:28

é de muitos jeitos no mercado mas aqui neste modo ele está

15:32

muito concreto tá operar um servidor MCP com segurança e

15:35

pacotamento, gato e métricas limites, health check e teste fim a

15:39

fim, tá? Não é magia operacional, é disciplina, tá? Então, é

15:45

é, ó.

15:48

E o próximo passo, tá, gente? O módulo que é o módulo A to A, que é o A to A,

15:53

tá? Que é outro eixo, outra história. Então, o foco muda para o eixo horizontal.

15:57

Essa distinção é importante, ó. MCP, nesse módulo, foi tratado como eixo vertical.

16:02

Um host conectando ferramentas e recursos por meio de servidores. A to A,

16:07

pessoal, vai deslocar a conversa para a gente conversando entre si,

16:11

coordenando o trabalho, descobrindo capacidades e negociando tarefas.

16:16

Não vamos ensinar A to A aqui ainda,

16:18

tá? Isso é só um aviso de mudança de eixo.

16:21

Mas ele fecha o módulo, mas a gente vai fechar o módulo dizendo,

16:26

antes de conectar agentes entre si,

16:28

você precisa saber operar o servidor de ferramenta com responsabilidade.

16:32

Então, gente,

16:34

o reframe final é tão simples quanto.

16:37

AIOps aqui não é ferramenta, é maturidade operacional aplicada a servidores de IA.

16:42

E saber defender, pacotar e operar. Tá bom?

## Resumo IA

[RESUMO_IA]