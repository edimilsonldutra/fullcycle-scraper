Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17800)

## Resumo da aula

Uma implementação orientada por critérios de aceitação precisa terminar com evidências verificáveis, não apenas com código alterado. Aqui, a Video Library foi concluída com commits, branch isolada em WorkTree, lista explícita de critérios atendidos, testes executados e registro de desvios. Esse formato transforma o relatório final em artefato técnico de revisão, porque permite validar o que foi entregue, o que mudou em relação ao plano e quais limitações ainda permanecem. Em desenvolvimento paralelo, esse nível de rastreabilidade reduz ambiguidade na integração entre features.

Um desvio não é necessariamente erro; ele pode ser uma adaptação legítima ao comportamento real do framework ou da base existente. O ajuste em submitLibraryPreference na server action, motivado por uma mudança específica do Next 16, mostra esse caso: a implementação preserva o objetivo funcional, mas altera a forma técnica de realizá-lo. O ponto importante é registrar o desvio de modo explícito para que revisão, manutenção e merge não assumam incorretamente que o plano original foi seguido literalmente. Sem esse registro, a diferença entre decisão arquitetural e regressão fica opaca.

Retomando o uso de smoke checks e validação automatizada já estabelecido, o problema novo aqui está na fragilidade do ambiente quando browser, sessão e cookies precisam ser limpos corretamente. O acesso a /app falhou não por ausência da feature principal, mas porque o navegador não conseguiu contornar um estado de autenticação herdado, o que foi classificado como soft fail. Essa classificação importa porque separa falha de ambiente ou automação de falha real de implementação. Em vez de bloquear a entrega inteira, o processo registra a limitação e segue com validações que ainda são confiáveis.

A WorkTree, já definida anteriormente como base do desenvolvimento paralelo, aparece aqui como condição prática para rodar a feature de forma independente. O agente gera Prisma Client, sobe o sistema e valida a Video Library sem interferir diretamente nas outras frentes em andamento. Esse isolamento não serve apenas para organização de branches; ele também preserva contexto de execução, dependências locais e estado da feature durante testes. Quando múltiplos agentes trabalham ao mesmo tempo, esse encapsulamento reduz efeitos colaterais difíceis de diagnosticar.

A necessidade de regenerar o Prisma Client após refazer partes do ambiente decorre da combinação entre versões do Next e do Prisma usada no projeto. Isso significa que o estado gerado do cliente não pode ser tratado como permanente durante o ciclo de execução local. Em termos operacionais, a validação da feature depende de reconhecer esse passo como parte do bootstrap técnico, não como detalhe incidental. Ignorar isso produz falhas que parecem ser de negócio, mas na verdade são de sincronização entre código gerado e runtime.

O Playwright foi usado para navegar pela aplicação, criar conta, autenticar, entrar em /app e verificar o comportamento visível da biblioteca. Esse fluxo valida a feature do ponto de vista do usuário: presença da drop zone, renderização da página, listagem de vídeos, modos de visualização e persistência após refresh. A vantagem desse tipo de teste é confirmar integração entre front-end, autenticação e estado da interface em uma única execução. A limitação observada aqui foi o manejo de cookies no ambiente atual, razão pela qual o uso do Playwright CLI foi apontado como alternativa mais estável.

A biblioteca implementada expõe um fluxo de uso claro: registrar usuário, acessar /app, enviar um vídeo e visualizar cards com thumbnail, ações de open, rename e edit description. O header e a drop zone permanecem visíveis, o que reforça a capacidade de adicionar novos vídeos sem perder contexto da listagem atual. A presença de grid, list e seção de vídeos recentes indica que a feature não se limita ao upload; ela organiza e apresenta o acervo de forma navegável. Esse conjunto atende tanto descoberta quanto manutenção do conteúdo enviado.

A extração ou geração de thumbnail é parte central da experiência da biblioteca porque transforma um arquivo bruto em item visualmente identificável. Houve inclusive criação de SVG como artefato auxiliar, mostrando que a implementação precisou produzir representação gráfica para suportar a interface. Isso importa porque bibliotecas de mídia dependem de pistas visuais para navegação rápida, especialmente quando o usuário gerencia múltiplos vídeos. Sem thumbnail, a listagem existe tecnicamente, mas perde grande parte da usabilidade.

Uma biblioteca de vídeos só é confiável se o estado persistir além da renderização inicial. Por isso, o refresh após alternância entre grid, list e vídeos recentes não é detalhe cosmético; ele verifica se preferências e dados continuam consistentes depois de nova carga da página. O teste confirma que a interface não está apenas simulando estado em memória temporária. Em aplicações reais, essa persistência é o que diferencia uma demo visual de uma feature utilizável.

Retomando a dependência com Background Processing já mapeada no capítulo, o upload aqui chega até o ponto em que a Video Library consegue receber o arquivo, extrair thumbnail e exibir o item com status de validação. A transição além dessa etapa não ocorre porque o processamento assíncrono ainda não está disponível. Isso demonstra uma integração parcial correta: a feature consumidora entrega tudo o que está sob sua responsabilidade e explicita o limite imposto pela dependência ausente. O resultado é um sistema funcional até a fronteira do pipeline, sem mascarar o que ainda falta integrar.

## Transcrição

00:00

Bom, pessoal, somente para colocar então,

00:04

Voltamos aqui nos processos de desenvolvimento. Se a gente olhar aqui,

00:08

a gente tem a tarefa 12 que ele está desenvolvendo aqui ainda,

00:12

que é implementando o painel de administração.

00:15

E aqui a gente está vendo ele fazer a

00:17

navegação e provavelmente testando as coisas aqui,

00:22

barra admin, barra users. Aqui ele está trazendo usuários, 50 por página.

00:28

E ele está trabalhando aqui, fez logout, ele vai verificar.

00:32

Eu tinha olhado aqui em alguns momentos onde ele

00:36

estava sofrendo um pouco para trabalhar com o browser aqui.

00:40

Isso pode ter sido coisas referentes, inclusive, ao Cloud Desktop.

00:44

Eu senti que ele estava, como que eu posso dizer,

00:48

com problemas de sessões e cookies na hora de limpar a sessão e coisas desse tipo.

00:52

Mas ele está ali.

00:55

Ele fez o logout e relogou aqui com admin

00:57

.e2e.local e ele está desenvolvendo aqui essa parte aqui.

01:03

Vamos ver o que ele trabalha, o que ele está fazendo.

01:07

Vou olhar aqui seções, logs de seção.

01:09

Está aqui aparecendo os logs do que ele estava

01:12

fazendo e aparentemente esse cara aqui está rodando.

01:16

Vamos para o outro cara aqui que é a implementação da Video Library.

01:19

Esse cara aqui, o que acontece? Ele...

01:24

fez o relatório e aparentemente ele terminou. Então,

01:27

vamos olhar aqui o que ele colocou.

01:30

Feature Video Library, ele fez quatro commits,

01:33

aqui está o branch que ele criou,

01:36

está com esse nome esquisito porque eu não pude dar nome ao WorkTree,

01:39

limitação aqui provavelmente no caso aqui do Cloud Desktop, mas o que acontece?

01:44

Ele mostra todos os critérios de aceitação que ele fez,

01:47

inclusive colocando quais são os testes.

01:50

Cross Feature Integration, ou seja,

01:53

O metadata com o thumbnail conseguiu fazer o render e etc.

01:59

Os vídeos puderam ser pegos ali do status do reset.

02:05

E aqui, deviations,

02:07

ele colocou aqui que ele adicionou single

02:11

argumento em relação à submit library preference. Server action,

02:15

basicamente, ele mudou porque alguma mudança específica em

02:20

relação ao Next 16 aqui no caso.

02:22

Soft fails é quando ele acessou o barra app para fazer um smoke check

02:27

o browser ali ele não conseguiu fazer

02:31

o bypass do baseado na feature 02

02:36

com o cookie ele não conseguiu fazer a limpeza do cookie, eu acho que foi

02:39

isso então que eu vi ele apanhando uma hora para ele fazer isso,

02:41

provavelmente deve ser difícil dentro desse ambiente que ele está trabalhando,

02:45

por isso que eu gosto muito de usar o Playwright CLI, a gente evita

02:51

alguns desses tipos de problema em relação à persistência de cookie e tudo mais. Notas de ambiente.

02:58

Toda vez que é refeito as coisas, ele tem que...

03:02

O ponto Prisma tem que ser refeito. Na realidade,

03:06

é algo referente ao Next e ao Prisma dessas versões, tá? Então,

03:10

ele trouxe aqui as fases que ele fez, os status e... a parada aqui rolando.

03:17

Que ele utilizou o Playwright, né?

03:19

Provavelmente ele trabalha com o Playwright quando ele mostra ali no browser, ali pra você,

03:24

Essa parada aqui quando eu coloco o preview. É uma coisa interessante que ele traz,

03:29

Quando ele mesmo criou um SVG, né?

03:33

Pra conseguir, como que eu posso dizer?

03:36

Colocar ali como thumbnail e coisas desse tipo.

03:39

Então aqui normalmente ele traz alguns artefatos que ele acabou colocando.

03:43

Então eu vou colocar aqui pra ele.

03:45

Rode o sistema pra eu verificar como ficou.

03:54

Vou dar um Enter aqui.

03:55

Ou seja, eu estou tentando fazer um teste básico pra eu conseguir olhar.

04:00

Perceba que ele ainda está trabalhando naquela feature ali pra gente.

04:04

Então, está gerando o Prisma Client de novo, que ele precisa.

04:08

E o importante de tudo isso, galera, é que ele está rodando dentro de uma WorkTree.

04:13

Então, isso aí é um ponto importante.

04:15

Aqui provavelmente novamente chega naquela parada dos

04:19

cookies, ele realmente está apanhando

04:21

Com os cookies, eventualmente eu mesmo

04:24

vou querer fazer o teste manual pra

04:29

inclusive ver isso aqui, provavelmente, é limitação.

04:32

Isso estava acontecendo em outras sessões.

04:34

Aqui também vamos ver se está

04:38

rodando aqui, aqui ele está colocando que

04:43

Como que eu testo? Eu abro o servidor nessa página, entro no register,

04:48

coloco um e-mail e senha, vai cair na página app, arrasto um vídeo,

04:53

pode ser o sample vídeo teste pra popular a biblioteca,

04:57

cada card vai mostrar um thumbnail,

04:59

onde eu tenho a opção de rename, descrição, no header da biblioteca e tudo mais.

05:05

E me avisa quando terminar. E eu vou colocar aqui pra ele.

05:10

Por que você não testa? Está dando erro? Qual erro?

05:21

Basicamente, provavelmente, tem rolo aqui com o Playwright.

05:25

Outra coisa que... Bom, pronto, vou testar de verdade.

05:29

E aqui ele está emperrado realmente com essa história do cookie aqui pra gente.

05:35

Uma outra coisa que eu não tô discutindo nesse momento com vocês,

05:38

e a gente vai falar isso na parte de Harness,

05:39

é a janela de contexto, compactação, que a gente sabe que é extremamente importante,

05:44

principalmente quando ele fica no loop e você tem,

05:47

sei lá, 200 mil tokens apenas pra trabalhar,

05:49

então isso é um ponto importante e que muda completamente o jogo,

05:54

e por isso que na parte de Harness a gente tem que conseguir limitar a

05:57

quantidade de coisas que ele vai fazer por step

05:59

pra gente validar esses tipos de coisa, tá?

06:02

Ele está falando que ele está com erro de navegador ali pra ele mesmo. Então,

06:06

agora ele deve ter ajustado.

06:08

Vamos ver esse cara navegar agora aqui pra ver se essa parada funciona.

06:14

Vou deixar ele criando a conta.

06:15

Vou dar uns pauses aqui somente pra gente não ficar perdendo tempo. Olha aqui então.

06:22

Ele falou que ele não estava conseguindo por conta

06:24

de uma bug que ele considerou pré-existente.

06:27

Provavelmente foi em relação à sessão quando redireciona pra pegar o cookie.

06:33

Ele falou que reajustou.

06:35

E redirecionou ali de verdade para a aplicação. Então,

06:39

Ele colocou tudo funcionando, a página renderizou, a library funcionou,

06:43

O drop zone está ali com o header da página, e eu tenho aqui os meus vídeos aqui.

06:49

Agora ele falou que vai testar a grid, com o list,

06:53

Os vídeos recentes, etc. E ele falou que persistiu,

06:57

Ele vai dar um refresh para verificar se essa persistência aqui funcionou.

07:04

E etc. Então, vamos ver como é que funciona essa parada aí.

07:10

E agora chegou a hora, galera.

07:12

Ele falou que vai fazer o upload pra ver se o vídeo vai aparecer ali.

07:17

Mas lembrando que a gente sabe que não tem o background

07:19

Processing ainda pra processar o vídeo e acontecer todas aquelas coisas ali.

07:24

Mas ele falou que vai fazer o upload aqui pra gente e provavelmente ele vai fazer

07:29

O upload por baixo dos panos porque ele não

07:31

Consegue pegar o mouse e arrastar alguma coisa, tá?

07:34

Então, ele falou que o vídeo foi carregado com sucesso, o thumbnail extraído,

07:38

E agora está aqui na parte de validando, e realmente está aqui,

07:43

Validando, mas ele não vai conseguir passar provavelmente dessa etapa,

07:47

Pelo fato de a gente não ter a tarefa em background.

07:50

Então, apareceu ali, lista de view ativa, laranja, o vídeo demo que apareceu,

07:56

Que ele colocou, a thumbnail ele pegou do vídeo.

07:58

O badge de validação está aparecendo,

08:01

O drop zone sempre está visível para eu poder colocar vídeo,

08:04

Isso foi uma especificação nossa,

08:06

Eu poderia ter pedido. E agora ele está abrindo ali, open,

08:09

Rename e edit description, caso ele queira trabalhar. Basicamente,

08:14

Ele está passando ali pelos testes de aceitação, tudo que tinha pedido, basicamente,

08:21

Aqui fez, e ele corrigiu um bug que estava pré-existente,

08:24

Que estava fazendo... um problema de cookie de sessão que aconteceu ali.

08:29

Se eu quiser testar, eu posso testar daqui pra frente.

08:32

Galera, legal. Próximo vídeo a gente vai tentar falar sobre conflitos.

08:37

Vamos ver se vai ter conflito no meio dessa história. Vamos nessa.

## Resumo IA

**Abreviações**

*   **CLI**: Command Line Interface (Interface de Linha de Comando).
*   **e2e**: End-to-End (De ponta a ponta), frequentemente usado em testes para indicar que o sistema completo está sendo testado.
*   **SVG**: Scalable Vector Graphics (Gráficos Vetoriais Escaláveis).
*   **WorkTree**: Recurso do Git que permite ter várias cópias de trabalho de um repositório em diferentes diretórios, cada uma associada a um branch distinto.

**Resumo**

A aula teve como objetivo demonstrar a implementação de uma funcionalidade, a "Video Library", guiada por critérios de aceitação e culminando em evidências verificáveis. O foco foi apresentar como uma tarefa de desenvolvimento é concluída, não apenas com mudanças no código, mas com um conjunto de artefatos técnicos que garantem rastreabilidade e facilitam a revisão.

O instrutor analisou o relatório de conclusão da `Video Library`, que detalhava quatro *commits*, o uso de um branch isolado via WorkTree (apesar de uma limitação de nomeação no ambiente Cloud Desktop), uma lista explícita de critérios de aceitação atendidos (incluindo a integração de metadados com *thumbnail* e a recuperação de status de vídeos), e os testes executados. Foram destacados "desvios", como a alteração em `submitLibraryPreference` na *server action*, justificada por uma mudança específica do Next 16. Esse registro sublinhou a importância de documentar adaptações legítimas para diferenciar de regressões. Também foram identificados "soft fails" durante um *smoke check* na rota `/app`, causados por dificuldades na limpeza de cookies do navegador, não por falha da própria feature. Para contornar esse tipo de problema, o uso do Playwright CLI foi sugerido como uma alternativa mais estável para lidar com a persistência de estado do navegador.

O fluxo de validação da `Video Library` incluiu a regeneração do Prisma Client (um passo reconhecido como essencial devido à interação entre as versões de Next e Prisma), a execução da feature em um ambiente isolado (WorkTree) e a utilização do Playwright para simular a interação do usuário. Este teste abrangia o registro de uma conta, autenticação, acesso a `/app`, o *upload* simulado de um vídeo (o agente executou o *upload* sem *drag-and-drop*), e a verificação de elementos da interface como a *drop zone*, a renderização da página, a listagem de vídeos com *thumbnail*, os modos de visualização (grid, list, vídeos recentes) e a persistência do estado após um *refresh* da página. A criação de um SVG para o *thumbnail* foi apontada como um artefato auxiliar crucial para a usabilidade.

Foi ressaltado que, embora o vídeo fosse carregado com sucesso e o *thumbnail* extraído, o processamento parava no status "validando". Isso ocorria porque o Background Processing, uma dependência assíncrona, ainda não estava implementado. Este cenário demonstrou uma integração parcial correta, onde a feature `Video Library` cumpria sua parte e explicitava a fronteira imposta pela dependência ausente, resultando em um sistema funcional até o ponto de integração.

**Pontos de atenção**

*   **Evidência Verificável na Entrega**: A conclusão de uma feature deve ser acompanhada de evidências verificáveis (commits, branch isolada, lista de critérios atendidos, testes executados e registro de desvios), não apenas código alterado, para facilitar a revisão e garantir a rastreabilidade.
*   **Registro Explícito de Desvios**: Documentar formalmente as adaptações legítimas (mudanças no plano original devido a comportamentos de framework ou base de código existente) é fundamental para diferenciar decisões arquiteturais de possíveis regressões durante revisões e manutenção.
*   **Classificação de Falhas (Soft Fails)**: Identificar e classificar corretamente falhas de ambiente ou automação (soft fails) em contraste com falhas reais de implementação. Isso permite que o processo de entrega continue com validações confiáveis, evitando bloqueios desnecessários.
*   **Isolamento com WorkTree**: Utilizar WorkTree para isolar o desenvolvimento e teste de features. Essa prática não apenas organiza os branches, mas também preserva o contexto de execução, dependências locais e estado da feature, minimizando efeitos colaterais em cenários de desenvolvimento paralelo.
*   **Regeneração de Artefatos Gerados**: Reconhecer a regeneração de artefatos gerados, como o Prisma Client, como um passo inerente ao *bootstrap* técnico, especialmente em projetos com combinações específicas de versões de frameworks (e.g., Next e Prisma). Ignorar isso pode causar falhas que aparentam ser de negócio, mas são de sincronização de ambiente.
*   **Estabilidade em Testes de Navegador**: O gerenciamento de sessões e cookies é um desafio comum em automação de testes de navegador. Ferramentas como o Playwright CLI podem oferecer maior estabilidade ao lidar com a persistência de cookies, tornando os testes mais confiáveis.
*   **Importância dos Artefatos Visuais**: Em bibliotecas de mídia, a extração ou geração de *thumbnails* e outras representações gráficas são cruciais para a usabilidade e navegação rápida, transformando arquivos brutos em itens visualmente identificáveis.
*   **Persistência de Estado**: Validar rigorosamente a persistência do estado da aplicação (e.g., preferências de visualização, dados) após um *refresh* da página. Isso garante que a interface não está apenas simulando um estado temporário em memória, mas oferece uma experiência utilizável e robusta.
*   **Integração Parcial e Fronteiras Explícitas**: Ao integrar com dependências que ainda não estão totalmente prontas, a feature consumidora deve entregar o que é sua responsabilidade e explicitar claramente os limites impostos pela dependência ausente, sem mascarar o que ainda precisa ser integrado.