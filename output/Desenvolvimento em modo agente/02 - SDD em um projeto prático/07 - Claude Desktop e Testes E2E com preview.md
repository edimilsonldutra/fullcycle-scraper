Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17785)

## Resumo da aula

O fluxo de desenvolvimento assistido por IA deixa de ficar restrito à IDE quando o trabalho passa a envolver múltiplas sessões, múltiplos agentes e revisão contínua de pull requests. Nesse cenário, a unidade operacional deixa de ser apenas o editor de código e passa a ser a sessão associada a um repositório, um branch e um objetivo explícito. Ferramentas como Cloud Desktop, Codex App e soluções equivalentes existem para centralizar essa orquestração. O valor prático está em acompanhar execução, contexto e saída do agente sem depender do ambiente tradicional de edição.

Uma sessão útil precisa nascer já ancorada no ambiente correto: repositório, branch e, quando aplicável, estratégia de trabalho paralelo como WorkTree, referenciada anteriormente. Quando a sessão já sabe para qual branch está apontando, ela reduz erro operacional em tarefas como geração de diff, preparação de mudanças e futura abertura de pull request. Isso transforma o agente em um executor contextualizado, não em um terminal genérico. Em projetos com várias features em andamento, esse vínculo com o branch é parte da rastreabilidade.

O preview é a camada que torna visível o comportamento do sistema enquanto o agente executa ações no navegador. Nesse caso, o setup cria um arquivo .cloud/launch.json, usado para definir como o ambiente deve ser iniciado e exibido. A consequência é simples: sempre que o sistema for testado, a interface pode ser acompanhada em tempo real. Isso reduz a distância entre automação e inspeção humana, especialmente quando se quer confirmar navegação, renderização e efeitos de interação.

Retomando as features já especificadas, o agente não navega aleatoriamente: ele usa documentação, histórias de usuário e critérios de aceitação como roteiro de execução. Quando recebe uma instrução como subir o sistema e navegar pelas features 01 e 02, ele interpreta a especificação e transforma cada critério em ação observável. Carregar a página, abrir registro, validar login e testar senha fraca deixam de ser passos implícitos e viram checkpoints verificáveis. A qualidade do teste depende diretamente da qualidade dessa especificação.

O mecanismo de automação pode estar encapsulado pela plataforma, mas o comportamento observado é o de um teste end-to-end dirigido por navegador, frequentemente com Playwright por baixo dos panos, como já referenciado antes. A diferença nova aqui é a visibilidade operacional: além de o teste rodar, é possível assistir ao agente executando cada etapa. Isso ajuda a confirmar se o fluxo seguido corresponde ao esperado e se a interpretação dos critérios está correta. Em vez de apenas receber um relatório final, você acompanha a execução enquanto ela acontece.

Nem todo erro visual ou redirecionamento indica defeito da implementação atual. Quando o registro funciona e depois redireciona para 404, isso pode ser compatível com o critério de aceitação se a próxima tela depender de uma feature ainda não entregue. A leitura correta do resultado exige entender a costura entre features, já tratada anteriormente, para não classificar como bug algo que é apenas ausência planejada de uma etapa futura. Teste automatizado útil não é só execução; é interpretação contextual do comportamento.

Alguns cenários E2E exigem manipulação explícita de sessão para que o próximo caso seja válido. Para testar e-mail duplicado após um registro bem-sucedido, o agente precisa limpar a sessão, voltar ao estado correto da aplicação e só então repetir a ação com os dados apropriados. Esse detalhe mostra que testes baseados em histórias de usuário não são independentes por acaso; eles precisam de pré-condições controladas. Sem esse cuidado, o teste falha pelo estado residual da aplicação, não pela regra de negócio.

A plataforma não expõe apenas a interface; ela também permite observar logs produzidos durante a execução. Isso é decisivo quando o agente encontra um problema como sessão deletada com cookie stale em getSession, porque o erro deixa de ser um sintoma visual isolado e passa a ter evidência técnica correlacionada. O agente pode então iterar entre ação no navegador e leitura de logs até localizar a causa provável. Esse ciclo aproxima depuração e validação funcional no mesmo fluxo.

Guidance continua sendo o fator que separa um agente superficial de um agente realmente útil. Se a instrução não explicita que ele deve testar, ele tende a fazer apenas um smoke test: subir a aplicação, verificar rapidamente e encerrar. Quando o prompt manda validar use cases e histórias de usuário, o comportamento muda para uma exploração orientada por critérios. O agente não decide sozinho a profundidade correta; essa profundidade é projetada por quem define o guidance.

Ver o agente trabalhando em tempo real é valioso, mas isso não implica acompanhar cada clique manualmente. À medida que o fluxo amadurece, a tendência é confiar mais na instrumentação, nos logs, nos critérios de aceitação e no resultado consolidado do que na observação contínua da execução. O preview serve como mecanismo de inspeção e diagnóstico, não como requisito permanente de supervisão humana. O ganho real está em poder intervir quando necessário, sem transformar cada execução em acompanhamento manual.

## Transcrição

00:01

Bom pessoal, o seguinte, o que eu quero trazer e mostrar aqui para vocês?

00:06

Uma das grandes tendências que a gente tem daqui para frente,

00:10

não tenho dúvida alguma,

00:11

é que cada vez mais nós não vamos mais ficar na nossa ideia.

00:14

A gente vai ficar gerenciando um monte de sessão, um monte de agentes,

00:17

orquestrando agentes e a gente vai provavelmente trabalhar muito com pull requests. E, eventualmente,

00:24

muitas das pull requests já vão passar e já vão

00:26

direto para a produção sem mesmo contato humano.

00:30

Esse, assim, vai acontecer.

00:33

No momento que você está olhando essa tela,

00:38

pode ter mudado. Isso aqui é o Cloud Desktop.

00:42

Existe o Codex App. Existem diversas aplicações. O cursor tem isso também.

00:47

Então, basicamente, é uma das ferramentas que você pode usar.

00:51

sem ser necessariamente uma IDE,

00:54

mas que você consiga gerenciar as sessões ali. O que acontece?

01:00

Se você olhar aqui, você tem uma espinha dorsal,

01:06

lembra quando eu falei para vocês do desenvolvimento com IA,

01:09

um dos pontos é ambiente, e nesse caso é um ambiente local,

01:12

poderia estar sendo um ambiente remoto lá na...

01:17

utilizando, sei lá, a nuvem da Anthropic, coisas desse tipo. Qual é a pasta,

01:23

né? Que é o meu repositório. Qual é o branch?

01:26

Eu vou aqui no meu branch F02 Authentication System.

01:30

E eu não vou trabalhar com o WorkTree agora, aqui nesse momento.

01:33

Isso aí vai chegar na parte onde a gente vai trabalhar em paralelo, tá?

01:36

E eu vou iniciar uma sessão aqui boba somente para

01:39

eu poder mostrar um negócio aqui para vocês.

01:41

Então, eu vou dar um ai aqui para mim.

01:44

Ele vai iniciar a minha sessão.

01:47

Ele já sabe o branch para onde ele está

01:51

apontando caso eu for fazer uma pull request.

01:54

Esse aí é um ponto interessante.

01:57

E ele perguntou o que você quer trabalhar ou alguma coisa desse tipo.

02:02

Mas se eu abrir aqui essa aba,

02:05

você vai perceber que eu tenho algumas coisas interessantes. Eu tenho o diff.

02:10

Então, aqui eu consigo visualizar o diff de tudo que foi modificado.

02:16

Então, ok, é útil para mim,

02:17

para algumas coisas. Quando tem muito arquivo,

02:19

esse diff fica cada vez mais difícil de eu conseguir trabalhar.

02:24

Mas ele tem uma coisa que é bem bacana, que é o quê? O preview.

02:29

Quando eu vou aqui no preview, deixa eu fechar o meu diff aqui.

02:33

Quando eu vou aqui no meu preview, eu consigo fazer o setup desse preview.

02:40

E esse setup do meu preview, o que está falando para ele fazer?

02:44

Ele cria um arquivo dentro da minha pasta .cloud, chamado launch.json, tá?

02:49

E esse arquivo que ele cria,

02:52

ele vai fazer com que toda vez que eu quiser testar o meu sistema ou alguma coisa,

02:57

eu consiga ver o preview em tempo real do que está acontecendo,

03:01

tá? Muitas outras ferramentas já fazem isso, inclusive, tá?

03:04

Mas eu só estou querendo trazer isso como uma forma que,

03:08

às vezes, acaba sendo um pouco mais simples de você não estar na IDE,

03:13

e eventualmente rodar tudo isso aí. Então,

03:18

Eu vou chegar aqui para o meu...

03:20

Eu posso colocar assim, subir o sistema para

03:26

Eu poder... Subir o sistema e

03:31

Navegue pelos

03:34

Critérios de

03:39

Aceitação das features 01 e 02.

03:47

Vou...

03:49

Dá um Enter aqui e vamos ver se ele faz essa parada aqui para a gente.

03:55

Então, ele vai ler as documentações, está

04:04

lendo as especificações e olha só agora aqui.

04:07

Agora, ele já abriu o preview aqui para mim.

04:11

Mas o mais legal agora aqui é que não é só a questão de ele abrir o preview.

04:16

É uma questão agora que ele vai entender as especificações das features,

04:23

os critérios de aceitação que foram colocados.

04:25

E ele vai poder entender para ver como que ele vai

04:29

fazer o progresso disso para ver se essas features acabam funcionando.

04:36

Então, eventualmente, na forma de como você pede para ele implementar,

04:40

essas coisas podem acabar funcionando. Então,

04:46

olha só, agora eu consigo ver ele navegando. Então,

04:48

Criar conta, aí provavelmente ele vai preencher.

04:53

Ali para mim, eu consigo ver ele fazendo as interações,

04:56

ou seja, critério de aceitação 1,

04:58

Carregar a página, e ele analisou a página para ver se renderizou certo,

05:02

e o critério 2 é ir para a página de registro,

05:06

e daí tem a parte provavelmente da parte de login, e

05:14

aí ele vai fazer as validações aqui.

05:16

Deixa eu ver se eu consigo inclusive aumentar o zoom

05:18

dessa parte só para você conseguir ver melhor.

05:24

E aqui ele navega pelos critérios.

05:27

Agora ele vai testar senha fraca. Ou seja,

05:32

Lembra todos aqueles critérios baseados naquelas histórias

05:35

de usuário que a gente fez?

05:36

Então, elas acabam entrando aí. Por isso que ele sabe quais detalhes, nesse momento,

05:42

ele vai precisar testar. E aqui, nesse momento,

05:45

a gente consegue ver ele testando esses tipos de coisa,

05:48

tá? Então, isso aqui é apenas uma forma, inclusive, de jeito de falar.

05:54

Cada vez mais, mesmo quando nós vamos passar pelo processo de desenvolvimento,

06:00

independente se a gente está conduzindo o agente,

06:02

ou se o agente está fazendo isso em uma pipeline de CI e CD,

06:09

usando um Playwright por baixo dos panos,

06:12

a gente sabe que cada vez mais está ficando fácil de desenvolver,

06:17

porque a gente consegue ver e gerenciar as sessões

06:20

vendo o que o agente está trabalhando.

06:22

E aqui ele falou que o registro funcionou, mas redirecionou para 404,

06:26

porque isso faz parte do critério de aceitação,

06:30

por conta que tem uma outra feature que vai ser utilizada.

06:35

Uma coisa interessante é que eu consigo ver os logs aqui,

06:38

e ele também consegue ver e ter acesso aos logs do que acaba colocando aqui.

06:42

Então, ele vai entrando, vai andando pelos critérios e tudo mais. Então,

06:49

era basicamente... Esse detalhe que eu queria trazer aqui para vocês.

06:54

E por isso que eu saí do meu cursor e entrei aqui no meu Cloud Desktop,

06:58

Tá? Mas a gente poderia fazer algo extremamente parecido,

07:02

Por exemplo, utilizando o Codex, tá? Então,

07:05

Isso aí é um dos pontos que valem a pena você ficar ligado, tá?

07:12

Aqui ele está, precisa de um logout para testar o registro do e-mail,

07:17

Então ele está limpando a sessão.

07:19

Para ele poder voltar para a página, para daí que ele volta para a página,

07:23

Ele pode testar o teste de e-mail duplicado.

07:28

Então perceba que ele vai ficar iterando até que todos

07:31

Aqueles testes de aceitação estão rodando e esses testes

07:34

De integração end-to-end ele consegue fazer e nessas

07:38

Plataformas a gente consegue ver isso em tempo real.

07:42

Por outro lado, eu vou deixar claro para vocês, cada dia mais que passa eu fico...

07:49

Não fico mais de babadear. Então,

07:52

Raramente eu vou ficar olhando e vendo como as coisas estão fazendo.

07:57

Ele botou um duplicate mail e agora limpou a sessão.

08:01

Ele pegou um erro ali de alguma coisa. Ah,

08:04

Por conta de sessão da forma que ele estava tentando limpar a sessão,

08:08

Eu acho. Não sei como é que ele está fazendo.

08:14

Encontrei um bug. Ao deletar a sessão,

08:16

O cookie ficou stale do get session. Ele vai tentar limpar.

08:20

Ali com o Next.js e rodando. Então, cara,

08:25

Essas coisas assim fazem muita diferença e normalmente é guidance de novo. O que isso significa?

08:34

Significa que se você não instrui o agente a testar,

08:38

Ele não vai testar. Se você não instrui o agente o que testar,

08:42

Ele necessariamente vai fazer um smoke test, vai subir, vai dar uma olhada e acabou.

08:49

Mas você também pode fazer com que o agente teste todos os seus use cases,

08:55

As suas histórias de usuário,

08:56

Para garantir como é que isso aí acaba funcionando. Então, esse aí é um outro ponto.

09:03

Bug, esse tipo de coisa que ele vai resolver, eu não estou preocupado.

09:06

O meu maior ponto aqui é ver como é que

09:09

Esse cara iria trabalhar e mostrar aqui para vocês.

09:13

Provavelmente, ele parou agora para limpar a sessão e vai iniciar de novo.

09:18

Agora aqui para ele terminar os testes, tá?

09:22

Provavelmente o que ele considerou um bug é o que

09:25

O Next.js está dizendo aqui para ele,

09:28

Ó. Então ele está com essa parte aqui e ele vai tentar ficar resolvendo esse bug.

09:33

Então esses tipos de coisa ali são extremamente importantes

09:36

E é legal você saber que existe,

09:39

Eu não sei se você está trabalhando dessa forma,

09:41

Mas eu só queria trazer uma forma alternativa aí para você dar uma olhada.

## Resumo IA

**Abreviações**
*   **IDE**: Integrated Development Environment
*   **PR**: Pull Request
*   **IA**: Inteligência Artificial
*   **CI/CD**: Integração Contínua / Entrega Contínua
*   **E2E**: End-to-End (ponta a ponta)

**Resumo**
A aula aborda a evolução do fluxo de desenvolvimento assistido por IA, que se estende para além do ambiente da IDE tradicional, focando na orquestração de múltiplas sessões e agentes, e na revisão contínua de pull requests. Nesse novo paradigma, a unidade operacional deixa de ser apenas o editor de código e passa a ser a "sessão", que está intrinsecamente ligada a um repositório, um branch específico e um objetivo explícito. Ferramentas como Cloud Desktop, Codex App e Cursor são apresentadas como soluções para centralizar essa orquestração, permitindo acompanhar a execução, contexto e saída do agente sem depender de um ambiente de edição tradicional.

Uma sessão eficaz é iniciada já ancorada no ambiente correto (repositório, branch e, se aplicável, WorkTree), o que minimiza erros operacionais em tarefas como geração de *diffs*, preparação de mudanças e abertura de PRs, transformando o agente em um executor contextualizado. A camada de "preview" é crucial, configurada via um arquivo `.cloud/launch.json`, que permite visualizar o comportamento do sistema em tempo real enquanto o agente executa ações, como testes de navegação, renderização e interação. Isso reduz a lacuna entre automação e inspeção humana.

O instrutor demonstra como o agente, guiado por documentação, histórias de usuário e critérios de aceitação, não navega aleatoriamente. Ao receber instruções como "subir o sistema e navegar pelas features 01 e 02", ele interpreta as especificações e transforma cada critério em ações observáveis e verificáveis, como carregar uma página, registrar, validar login ou testar senhas fracas. O mecanismo de automação, frequentemente utilizando Playwright por baixo dos panos para testes E2E, oferece visibilidade operacional, permitindo que o usuário acompanhe cada etapa da execução do agente.

A plataforma também permite observar *logs* produzidos durante a execução, o que é decisivo para correlacionar sintomas visuais com evidências técnicas, como um erro de cookie *stale* em `getSession`. A "guidance" (orientação explícita) é destacada como um fator crítico: se o agente não é instruído a testar, ele fará apenas um *smoke test*; se for instruído a validar *use cases* e histórias de usuário, sua exploração será orientada por critérios, determinando a profundidade do teste. Embora o preview seja valioso para inspeção e diagnóstico, a tendência é confiar mais na instrumentação, *logs* e resultados consolidados à medida que o fluxo amadurece, sem a necessidade de supervisão manual contínua.

**Pontos de atenção**
*   **Ancoragem de Sessão:** A sessão de trabalho deve nascer já vinculada ao ambiente correto (repositório, branch e, se aplicável, WorkTree) para garantir contexto, reduzir erros operacionais e facilitar a rastreabilidade em projetos com múltiplas *features*.
*   **Qualidade da Especificação:** A eficácia dos testes automatizados e o comportamento do agente são diretamente proporcionais à clareza e qualidade da documentação, histórias de usuário e critérios de aceitação fornecidos. Sem isso, o agente não saberá a profundidade de teste necessária.
*   **Interpretação Contextual dos Resultados:** Um erro visual ou redirecionamento (ex: 404) nem sempre indica um defeito. É crucial entender a "costura entre *features*" e o planejamento do projeto para evitar classificar como *bug* algo que é apenas uma ausência planejada de uma etapa futura.
*   **Manipulação Explícita de Sessão em E2E:** Para que os casos de teste E2E sejam válidos e independentes, é essencial que o agente manipule explicitamente a sessão (limpar, voltar ao estado correto) antes de cada novo teste, evitando falhas causadas por estados residuais da aplicação.
*   **Importância do *Guidance***: O agente não decide sozinho a profundidade dos testes. A instrução (ou *guidance*) explícita por parte do desenvolvedor é o que diferencia um *smoke test* superficial de uma exploração orientada por critérios, garantindo que *use cases* e histórias de usuário sejam validados.
*   **Logs como Ferramenta de Diagnóstico:** O acesso e a capacidade do agente de observar *logs* durante a execução são decisivos para correlacionar problemas visuais com evidências técnicas (ex: *cookie stale*), facilitando a depuração e validação funcional.
*   **Preview para Inspeção, Não Supervisão Contínua:** Embora o *preview* em tempo real seja valioso para inspeção e diagnóstico de problemas, o objetivo final é confiar na instrumentação e nos resultados consolidados. O *preview* serve como um mecanismo de intervenção quando necessário, não como um requisito permanente de acompanhamento manual.