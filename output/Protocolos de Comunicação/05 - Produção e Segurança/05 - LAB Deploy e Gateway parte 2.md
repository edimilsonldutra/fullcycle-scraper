Módulo: Protocolos de Comunicação\
Aula: [LAB: Deploy e Gateway parte 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18610)

## Resumo da aula

O Dockerfile implementa a defesa operacional em duas camadas: um estágio de build e um estágio final de runtime. O multi-stage build, já conhecido, aparece aqui como mecanismo concreto para deixar a imagem final apenas com código e dependências necessárias, sem compiladores nem ferramentas de construção. Isso reduz superfície de ataque e evita carregar artefatos inúteis para produção. O ponto novo nesta configuração é como essa limpeza se combina com as regras de execução do processo.

A criação do usuário app, seguida de chown em /app e só depois USER app, não é detalhe cosmético; é uma dependência de ordem. Se o container trocar para non-root antes de ajustar ownership, o processo perde acesso aos próprios arquivos e falha com erro de permissão. Se mantiver root até o fim, o serviço funciona, mas perde uma barreira importante contra escalada após comprometimento. A sequência correta prova que segurança e funcionalidade precisam ser montadas juntas, não em etapas independentes.

Retomando a exigência de evidência operacional, docker exec ... whoami transforma a configuração do Dockerfile em prova observável. O resultado esperado é app, não root, porque o objetivo não é declarar privilégio mínimo, e sim demonstrar que ele está ativo no runtime real. Esse teste é simples, mas elimina a falsa sensação de segurança causada por arquivos corretos e containers executando com configuração diferente da esperada.

O YAML do gateway define a borda efetiva da IA, e o bloco tools é onde a restrição vira política executável. Em vez de publicar tudo o que o backend sabe fazer, a configuração expõe apenas emitir_reembolso_bonificado, alinhando a superfície acessível ao caso de uso aprovado. A allowlist já foi estabelecida anteriormente; o avanço aqui é enxergar exatamente onde ela mora no arquivo e como uma linha de configuração muda o que a LLM consegue ou não invocar.

O Authorization configurado em headers injeta um barrier token na requisição antes que ela saia do gateway. Esse token funciona como uma credencial de barreira entre borda e backend: a LLM usa a tool exposta, mas não recebe o segredo que autentica o tráfego interno. Isso existe para separar capacidade de uso da tool de posse da credencial operacional. Em produção, o segredo deve viver na borda e ser repassado ao backend apenas no tráfego autorizado.

A classe AuthMiddleware implementa a contraparte do segredo injetado pelo gateway. Ela intercepta as requisições, lê o header Authorization e compara o valor recebido com o barrier token esperado; se o token estiver ausente ou incorreto, a resposta deve ser 401. O valor dessa abordagem está na sincronização explícita entre borda e backend: um lado injeta, o outro valida. Há alternativas mais robustas, como validação por JWT ou integração com um provedor de identidade, mas o middleware simples já demonstra a mecânica essencial da defesa.

Nem toda rota deve exigir o mesmo tratamento de autenticação. O middleware libera /healthz e /metrics sem validação do barrier token para preservar health checks e observabilidade, enquanto mantém o tráfego MCP protegido. Essa exceção precisa ser deliberada e restrita, porque abrir rotas demais transforma conveniência operacional em bypass de segurança. O critério correto é liberar apenas endpoints de suporte que não executam ações de negócio.

Retomando a migração de STDIO para HTTP, o servidor passa a ser empacotado como uma aplicação Starlette usando transporte streamable HTTP. Isso permite que o gateway converse com o backend pela rede, em vez de depender de um processo preso ao terminal local. A mudança não é apenas de protocolo; ela habilita a aplicação das políticas de borda, autenticação por header e inspeção operacional no caminho real de produção.

O caminho feliz confirma que as camadas estão alinhadas quando um pedido de reembolso percorre interface, gateway e servidor remoto até consultar o banco interno e retornar resultado. O tracing inline foi deixado visível para mostrar a sequência de chamadas e facilitar a leitura do fluxo. Esse tipo de teste não prova robustez sozinho, mas verifica se a configuração do gateway, o middleware e o transporte HTTP estão coerentes entre si antes de partir para falhas induzidas.

A injeção de caos começa ao forçar uma exceção dentro de emitir_reembolso_bonificado e reexecutar o serviço para observar a reação do sistema. O objetivo não é “quebrar por quebrar”, e sim validar se a arquitetura expõe erro de forma detectável para quem opera e para quem consome. Quando o comportamento não corresponde ao esperado, como ocorreu no experimento mostrado, o teste continua útil porque revela descompasso entre hipótese e execução real. Caos controlado serve exatamente para isso: encontrar pontos cegos antes que a falha apareça em produção.

## Transcrição

00:00

Pessoal, tudo bem? Então agora nós vamos para o gabarito do Laboratório 23. Ou seja,

00:08

chegou o momento que a gente vai revisar o laboratório.

00:13

E a nossa missão, só para lembrar,

00:15

era tirar o servidor MCP do ambiente local,

00:17

que é o STDIO, e colocar numa arquitetura realista de produção.

00:21

E a gente tem que prestar atenção em uma coisa,

00:24

que não basta simplesmente rodar em um container.

00:27

Produção exige um gateway especializado,

00:30

e no caso aqui nós estamos usando o Docker MCP

00:33

Gateway que tenha controle rigoroso de todas expostas,

00:36

isolamento e rastreabilidade total.

00:39

E o desafio de vocês era implementar as métricas de segurança de forma end-to-end, tá?

00:45

Bem, então vamos ver como vocês deveriam ter

00:48

implementado essas defesas direto nas camadas de infraestrutura.

00:52

Vamos primeiro abrir o arquivo DOCX, tá?

00:56

Então, pessoal, olha só.

01:00

Notem que no topo do arquivo nós começamos definindo o multistage build.

01:05

E esse multistage build, pessoal,

01:08

ele é importante porque a gente vai separar muito

01:13

claro a parte de compilação e subida da aplicação.

01:20

das dependências e suas dependências, tá?

01:24

E da definição que a gente vai ter aqui sobre responsabilidades e acesso,

01:28

desculpa, autorização e acesso de usuário,

01:32

tá? Que seria referente à lógica 1, tá? Então, vamos lá.

01:36

Então, no primeiro estágio, que eu chamei de builder, tá?

01:40

Nós estamos instalando as dependências fazendo o cache

01:43

do PIP para acelerar os builds,

01:45

tá? Então, já a partir da linha 34,

01:50

a gente tem o runtime, tá? E no caso seguinte,

01:54

nós copiamos apenas o código da aplicação e as dependências já instaladas,

01:58

deixando a imagem realmente mínima e livre de compiladores

02:02

ou ferramentas de build desnecessárias em produção,

02:04

tá? Até para evitar maiores problemas e ataques, tá bom? Beleza? Então, né?

02:11

Então vamos lá. Primeira parte, build. Segunda parte,

02:15

é o que nós vamos subir, tá?

02:21

E descendo para a primeira métrica, pessoal,

02:24

não sei se vocês lembram que é a métrica do no root,

02:26

né? Da gente tirar o usuário root, tá? Então,

02:28

vejam mudar o usuário root. Vejam que nós criamos um usuário app, tá?

02:33

A gente criou um usuário app, tá bom? Que esse cara aqui, beleza?

02:39

E logo na inicialização, a gente altera o dono da pasta /app, tá?

02:45

A gente altera o dono da pasta /app,

02:49

com o chown, tá? A gente vai usar o chown aqui, tá vendo?

02:55

Para ser esse usuário. Ou seja, o dono da pasta /app,

03:01

que é a pasta do aplicativo,

03:04

é o usuário app que a gente criou lá em cima, tá bom?

03:08

Bem, a

03:10

gente trava a execução usando a diretiva user app no final do arquivo DOCX,

03:15

tá? Então, a gente travou aqui usando o usuário app, user app.

03:20

O chown, pessoal, que é o change owner, tá? Então, isso aqui

03:23

serve não sei se todo mundo conhece né exatamente para mudar o

03:27

que vai ser o dono da pasta tá que vai ter acesso que

03:31

vai ter acesso a pasta então preste atenção nesse detalhe pessoal

03:34

de forma simples tá como a diretiva user manda o container derrubar

03:38

os privilégios de root se a gente não fizesse esse tchom tá

03:42

se a gente não fizesse esse tchom aqui antes O nosso programa

03:45

daria um erro de permissão negada ao tentar ler os próprios arquivos,

03:49

pois eles ainda pertenceriam ao root. Então,

03:52

o processo comprometido rodando como root em container

03:55

é um risco inaceitável em produção.

03:58

É por isso que foi feito nessa ordem, inclusive.

04:03

Então, só para a gente ver se está certo, inclusive o seguinte... Então,

04:08

para a gente validar isso aqui, se a nossa defesa funcionou,

04:12

a gente não precisa só acreditar no código, tá,

04:14

gente? A gente pode executar o WhoAm I,

04:17

tá? Aqui, em cima aqui do nosso aplicativo para ver, ó. Beleza, ó.

04:23

WhoAm I, ou seja, você vai ver que a resposta é app,

04:27

tá? O atacante invadir esse processo,

04:29

ele não terá permissões de root para escalar ataques na máquina host,

04:32

tá? Então... Essa aqui, gente, é a validação, a nossa primeira validação,

04:38

a métrica 1 lá, que é do usuário root, tá?

04:41

Agora, pessoal, a gente vai para um... Ou seja,

04:44

então subimos, tá? Subiu, definiu, mudou o root,

04:47

tá? Está tudo certinho. Agora nós vamos para a parte do catálogo MCP.

04:55

Gente, vocês vão reparar que o quanto o arquivo

04:59

pequeno como esse é super importante dentro do contexto aqui, tá?

05:04

Então, vamos lá. Então, no docmcpGator, nós definimos a borda da IA.

05:09

Então, lembra disso, pessoal. O Gator,

05:10

ele define a borda da IA, tá? Então,

05:13

aqui a gente vai aplicar aquela validação 2, a métrica 2,

05:16

que é a tua low enlist. Ou seja,

05:19

em vez de expor tudo que o back -end faz, repare no bloco tools,

05:23

tá, gente? Que está aqui, ó. O bloco tools,

05:26

a gente só vai colocar aqui, nós determinamos exatamente nesse lugar.

05:32

Quais ferramentas o cliente LLM pode acessar?

05:35

Nesse caso aqui,

05:36

a gente falou que ele só pode acessar o emitir reembolso bonificado.

05:40

Agora, olha só que legal, pessoal.

05:43

Além disso, olha a métrica 3, que é de Secrets Management,

05:46

tá? Olha só, nós configuramos um cabeçalho HTTP, tá?

05:53

Usando headers, tá?

05:54

Que é o headers, chamado authorization, tá?

05:59

E nós vamos injetando o nosso token barrier de produção.

06:02

O token barrier que eu inventei aqui, tá?

06:05

Só lembra uma coisa.

06:06

Nós vamos precisar saber esse token barrier lá no servidor HTTP,

06:10

tá? Beleza? Então, vamos lá.

06:13

Então, o nosso servidor financeiro, ele valida esse token,

06:16

por isso que a gente vai precisar dele lá,

06:17

via middleware no Python.

06:19

E já recebe a requisição autenticada quando processar

06:22

os estornos na adquirente de cartão.

06:25

A IA nunca vê esse segredo, tá, pessoal?

06:27

Ele não fica solto em variáveis locais, tá bom?

06:31

Então, vamos lá. Então, para a gente dar continuidade à métrica 3,

06:34

vamos dar uma olhada como é que a gente

06:36

implementa essa métrica 3 aqui no nosso servidor, tá?

06:39

Então, olha só, pessoal.

06:42

Parará, parará.

06:44

Depois vocês dão uma olhadinha aqui como é que ficou.

06:47

Opa, fui muito... Deixa eu achar aqui o nosso token, só para... Então, vamos lá. Agora aqui...

07:03

Olha só, olha só você então aqui na métrica

07:07

continuando a métrica 3, a gente deve implementar a validação

07:10

de barrier token, então, no arquivo, na classe ALF

07:14

middleware, tá? Essa aqui, cara, essa classe ALF middleware aqui

07:19

ela deve interceptar as requisições,

07:23

deixando o barra healthz,

07:26

que é o health authorization,

07:28

e metrics passarem sem autenticação.

07:34

Deve interceptar, deixando esses caras passarem sem autenticação,

07:38

mas bloqueando todo o tráfego MCP com 401,

07:41

se o token estiver ausente ou incorreto. Ou seja, se não vier esse token, pessoal,

07:48

Olha só, gente, aqui ele capturando dentro do header,

07:53

capturando dentro dos headers,

07:58

este header que a gente definiu lá,

08:00

e aqui o nosso token. Então, de novo, pessoal, olha só.

08:05

Dessa forma, as duas pontas ficam perfeitamente sincronizadas. Ou seja,

08:10

a borda vai injetar isso aqui

08:16

de forma transparente para a LLM.

08:19

E o servidor vai capturar e vai saber, cara,

08:22

peraí, tem aqui um token? Gente, obviamente,

08:24

existem várias formas de implementar isso aqui. Isso aqui é só para...

08:27

Isso aqui é um... A gente está interceptando e capturando antes,

08:32

tá? Obviamente, está longe de ser a melhor forma,

08:36

mas é uma forma viável e funcional para a gente, tá? Bem,

08:43

então assim, então... E a outra coisa, gente, é com relação ao transporte, tá?

08:49

Lembrem disso, pessoal, olha só.

08:51

Para rodar em containers, não faz sentido manter o STDIO.

08:54

Então, aquele que roda atrelado ao terminal local.

08:57

A gente precisa alterar a infraestrutura chamando o MCP streamer HTTP.

09:03

Então, aqui, pessoal, vamos ver aqui.

09:10

Então, a gente precisa chamar o MCP streamer HTTP.

09:14

Isso empacota o servidor MCP em uma API Starlette que fala HTTP na rede.

09:21

É assim, gente, nosso API tu conversa com o Becky,

09:24

Becky devia rede de forma transparente, então, pra gente

09:27

ver o fluxo completo, tá funcionando do caminho feliz, a gente

09:30

vai subir a aplicação e vai testar, tá bom? Tem

09:35

só um erro aqui, tá, pessoal, que eu acabei de

09:38

perceber. Eu vou alterar para ficar bonitinho para vocês,

09:40

por isso que eu dei até uma travada aqui quando

09:42

Eu tava explicando que é sobre aqui ó esse

09:49

Cara aqui esse cara aqui é métrica 3, beleza

09:55

Que a gente tem a métrica

09:58

Olha só aqui a métrica 3, pessoal.

10:11

É... Vou

10:51

mudar isso aqui dentro do gabarito.

10:55

Deixa eu já corrigir, pessoal. Que aí vai bonitinho pra vocês.

11:24

Opa, não é esse não. É

11:31

esse aqui. Não

11:41

É porque misturei os dois, por isso que tava errado. Entendi.

11:45

Entendi. Na

11:48

Verdade é o seguinte, então, pessoal.

12:26

Tá vendo, pessoal? É assim também, né? A gente erra também, né? Então

12:34

agora as coisas estão no lugar certo. E

12:49

agora vamos voltar aqui, pessoal, vamos rodar agora

12:52

o nosso aplicativo Estrelite, tá? Vamos ver, vamos

12:59

colocar aqui ó, emitir o reembolso de dois reais, emitir

13:06

o reembolso por pedido 2 que tá aqui ó, emitir um reembolso por

13:15

pedido 2 no valor de 50 reais.

13:27

Olha o tracing inline aqui, pessoal. Obviamente, pessoal,

13:30

eu fiz de forma a vocês poderem ver a chamada das funções,

13:33

né? Que tá chamando bonitinho, né?

13:35

Tem aqui o resultado da ferramenta, né? Gente, isso aqui é pra ser didático,

13:39

tá? Tá longe de ser algo real, tá? Então, ó.

13:45

Então, o pedido foi até a interface do Gator. Ele bateu no MCP Server remoto.

13:49

Ele autenticou. Ele consultou o banco de dados interno. Tudo ficou maravilhoso.

13:54

Agora, pessoal, a prova de fogo. Nós vamos injetar o caos.

13:58

É isso aí. A nossa arquitetura está de pé.

14:01

Mas será que ela nos avisa quando as coisas dão errado?

14:04

Ou quando estamos sendo atacados?

14:06

Vamos unir a visão do usuário com a visão de engenharia.

14:10

Agora é o seguinte, pessoal. Eu vou gerar um

14:13

pequeno caos aqui.

14:15

O princípio, a gente já acabou, tá, gente? O lab.

14:18

Mas eu quero mostrar para vocês isso aqui, que interessante. Vamos aqui, ó.

14:21

Eu vou na função emitir reembolso bonificado aqui, ó. Servidor.

14:27

Vou aqui na funçãozinha, emitir reembolso bonificado. E o que eu vou fazer, pessoal?

14:33

Eu vou gerar

14:35

uma exceção, tá? Vou gerar uma exceção. Bum!

14:45

Vou colocar as informações aqui. Bom.

14:48

Vou gerar uma exceção, tá? E

14:54

eu vou subir o Docker de novo, tá? Eu vou subir o Docker de novo, deixa

15:02

aqui para

15:05

subir o Docker. Eu não preciso derrubar o Streamlit, só preciso subir

15:10

aqui de novo. Só preciso fazer duas coisas aqui antes. Tudo é

15:27

preguiça, pessoal, de digitar. Estou

15:37

subindo, subir. Beleza, pessoal.

15:39

Agora vai ser o seguinte. Agora a gente vai pedir o mesmo reembolso de novo.

15:44

Nós vamos pedir o mesmo reembolso.

15:45

Vocês podem ver que eu não derrubei o Streamlit. Mas eu vou pedir o mesmo reembolso.

15:56

Olha só que interessante, pessoal. Opa.

16:13

Deixa eu ver se eu esqueci alguma coisa, pessoal.

16:16

Uma coisa

16:23

aqui. Deixa eu ver. Ele

16:40

não está dando erro. É

16:43

o seguinte. Eu

16:57

vou derrubar o dock. Deixa

17:05

eu roubar o Docker do MCP Financeiro aqui, pessoal. Deu

17:11

o Dockerzinho do MCP Financeiro. São vários. Vamos ver aqui.

17:27

Simplesmente apaguei. Só para ver se a gente apagou mesmo. Vamos ver aqui.

17:34

Deveria dar um erro agora. Não é possível.

17:37

Beleza. Falhou, pessoal. Não tem. Não achou. Não achou. Então aqui agora.

17:43

O que eu vou fazer? Eu vou subir o servidor de novo. Beleza. Subiu.

17:54

Agora eu vou fazer o mesmo pedido.

17:59

Tem que vir outro tipo de erro, tá? Na verdade. Que coisa.

18:13

Pessoal, eu vou dar uma pausa aqui no vídeo e entender o que aconteceu e volto, tá?

18:17

Né? Vamos ver.

## Resumo IA

[RESUMO_IA]