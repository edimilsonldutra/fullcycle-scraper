Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17789)

## Resumo da aula

Uma feature bloqueante é aquela que libera várias outras do backlog porque fornece uma capacidade base do sistema. Aqui, o upload de vídeo cumpre esse papel: sem ele, fluxos posteriores como cadastro completo do vídeo, categorização, tags e transcrição não conseguem avançar de forma útil. Retomando o fluxo já estabelecido com PRD, branch e pull request, o ponto novo é identificar que nem toda feature tem o mesmo valor estrutural; algumas existem para destravar o restante do grafo.

A validação não ficou restrita ao diff ou ao build: o comportamento foi testado diretamente na interface por meio da drop zone de upload. Para isso, um arquivo de amostra foi deixado disponível em uma pasta como Video Sample, permitindo que o agente ou o operador executasse testes com browser tools e confirmasse que o envio do arquivo realmente funcionava. Esse tipo de artefato reduz ambiguidade operacional e torna a verificação de uma feature multimodal mais previsível.

Depois que a feature foi implementada e validada, o fluxo segue com merge da pull request, remoção da branch e atualização da main com git checkout main e pull. Isso importa porque o desenvolvimento paralelo precisa partir de uma base consolidada; ramificações simultâneas sobre uma fundação instável multiplicam conflitos e retrabalho. Em projetos guiados por agentes, estabilizar a linha principal antes de abrir novas frentes é uma decisão de coordenação, não apenas de Git.

Retomando o PRD já usado nas etapas anteriores, o avanço aqui é tratar as features como nós de um grafo de dependência, e não como uma lista linear de tarefas. A prioridade ajuda a sugerir ordem, mas a dependência define viabilidade: uma feature pode até parecer importante, porém continua inviável até que outra prepare os contratos, fluxos ou recursos necessários. Esse modelo explica por que features aparentemente separadas conseguem se integrar depois sem “gambiarras”: elas já foram especificadas com pontos de encaixe.

Waves são agrupamentos de features que podem ser desenvolvidas na mesma rodada porque não dependem entre si de forma bloqueante. Se a Wave 1 contém as Features 1 e 2, ambas podem avançar em paralelo; se a Feature 3 depende das anteriores, ela entra na Wave 2. Essa organização transforma o PRD em instrumento de planejamento operacional, porque indica onde paralelizar com segurança e onde a sequência é obrigatória.

A feature de upload não é apenas mais uma entrega visível; ela prepara o terreno para capacidades posteriores do produto. Sem upload, não há vídeo persistido para categorizar, etiquetar ou enviar ao pipeline de processamento com OpenAI e Whisper para transcrição. Em termos de arquitetura de produto, isso caracteriza uma dependência funcional forte: as features seguintes consomem um recurso que ainda não existe até essa etapa ser concluída.

Quando uma feature “prepara o terreno” para outra, isso significa que ela entrega interfaces, fluxos e comportamentos esperados pelas próximas implementações. O resultado desejado é permitir CRUD e integração entre partes do sistema sem costuras manuais feitas depois. Nem sempre isso elimina ajustes posteriores, mas reduz drasticamente o trabalho de reconciliação porque a compatibilidade já foi pensada na especificação.

Desenvolvimento paralelo não é simplesmente abrir várias branches ao mesmo tempo; é escolher frentes independentes com base no grafo de dependência. Quando essa análise é feita cedo no PRD, fica possível distribuir trabalho entre agentes ou pessoas sem criar bloqueios artificiais. O ganho real não é só velocidade, mas previsibilidade: cada frente sabe o que já está pronto, o que ainda bloqueia e qual fundação precisa existir antes do próximo passo.

## Transcrição

00:00

Bom, pessoal, voltando aqui, somente para vocês saberem, foi terminado, basicamente,

00:07

a nossa feature trace, que era para a gente fazer o upload do vídeo.

00:12

Então, basicamente, o que eu fiz foi pegar,

00:16

gerar a feature trace e pedir para essa feature trace ser executada. Então,

00:22

se você olhar aqui, eu tenho a feature trace,

00:25

vídeo upload, com as especificações, com toda aquela história.

00:29

Que a gente já viu e que a gente está acostumado, que a gente foi seguindo,

00:33

tá? Além disso, o que eu fiz, eu já gerei a pull request aqui.

00:40

Somente para você saber, eu fiz tudo através aqui do Cloud Desktop,

00:46

nesse nosso caso, tá?

00:47

Mas eu também fiz testes aqui,

00:50

onde eu mesmo posso fazer o drop na drop zone do vídeo,

00:54

né? Eu coloquei um vídeo de exemplo para que ele pudesse testar, né? via tools,

01:00

via internal tools deles, browser tools, ou seja,

01:04

eu criei uma pastinha aqui chamada Video Sample,

01:07

onde tem um vídeo de teste aqui, onde ele pode fazer os testes,

01:12

mas eu também fiz alguns testes aqui para garantir

01:14

que o vídeo estava sendo feito o upload.

01:17

Beleza? Agora, o que vai restar aqui para a gente?

01:21

A primeira coisa que eu vou fazer é entrar e fazer o merge do meu pull request.

01:30

Vou deletar o branch, vou

01:33

voltar aqui no meu cursor, vou colocar um git checkout main,

01:39

vou pedir para ele dar um pull aqui para mim, e

01:44

basicamente o que vai acontecer vai ser o seguinte,

01:51

nós vamos entrar em uma nova fase,

01:54

e nessa nova fase agora a gente vai falar sobre o desenvolvimento paralelo.

01:59

E isso é uma das coisas mais importantes que a gente

02:04

pode ver da forma como a gente acaba trabalhando e provavelmente

02:09

é assim que você vai começar a trabalhar daqui para frente ou

02:12

se é que você já não está trabalhando dessa forma,

02:15

tá? Então, o que acontece aqui é o seguinte,

02:18

pessoal. Eu vou novamente botar o nosso PRD para visualização e eu vou voltar,

02:24

inclusive, para o nosso Scaled Draw.

02:26

Para mostrar um pouquinho mais de forma profunda como que isso aí acaba funcionando,

02:33

principalmente pelo relacionamento das features, que foi o que eu falei para você.

02:37

Somente para você saber, as três features que a gente desenvolveu até agora,

02:42

todas elas conseguem se falar sem eu ter que ficar

02:45

fazendo um monte de arranjos e gambiarra para grudar essas features.

02:50

Isso sempre vai funcionar?

02:52

Provavelmente não. Eventualmente, você sempre vai ter que fazer alguns ajustes.

02:56

Mas aqui nós temos esse gráfico de dependência das features,

02:59

tá? Então, feature 1, feature 2, 3,

03:01

tem a prioridade que ela faz, ou seja,

03:04

a gente criou no prompt e tem toda uma parte de prioridade,

03:07

o que ele acha que tem que ser feito primeiro ou não.

03:09

Mas quando a gente começa a olhar aqui,

03:12

a gente consegue ver que existe todo um gráfico de dependência,

03:16

tá? E por isso que eu separei esses gráficos aqui em waves.

03:21

Waves é... como se fosse rodadas. Então, a Wave 1,

03:24

eu posso fazer a Feature 1 e Feature 2.

03:26

Já na Wave 2, eu posso fazer só a Feature 3.

03:29

Por isso que eu fiz essa Feature 3, sem ficar mostrando aqui para vocês,

03:32

porque existem muitas Features que dependem da Feature 3,

03:36

que é exatamente a Feature de Upload. Então,

03:39

eu não consigo cadastrar um vídeo e fazer o Upload dele, eu não consigo categorizar,

03:43

eu não consigo fazer Tag, eu não consigo fazer o processamento ali com a...

03:48

com a OpenAI, com o Whisper para ele fazer transcrição e tudo mais. Então,

03:53

o nosso objetivo agora é eu conseguir explicar para você a lógica desse PRD,

04:00

mas por que eu estou querendo dizer a lógica desse PRD?

04:03

Eu não estou dizendo que você vai ter que usar esse PRD.

04:05

Eu quero que você entenda a lógica de como essa construção de dependências

04:10

foi gerada ao ponto de fazer com que uma feature deixe a outra saber

04:17

que ela preparou o terreno para ela, para que isso possa,

04:20

vamos dizer, fazer esse CRUD, essa integração entre features. Então, no próximo vídeo,

04:27

eu vou trazer aqui para vocês exatamente como é que isso aí vai funcionar. Vamos nessa!

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirements Document
*   **PR**: Pull Request
*   **CRUD**: Create, Read, Update, Delete

**Resumo**
A aula teve como objetivo principal demonstrar a conclusão da "feature trace" de upload de vídeo, uma feature bloqueante que libera diversas outras funcionalidades do backlog. Foi revisitado o fluxo de desenvolvimento que inclui a especificação no PRD, criação de branch e submissão de pull request. O ponto central da aula foi a introdução do conceito de que nem todas as features possuem o mesmo valor estrutural, sendo algumas essenciais para destravar o restante do grafo de dependências do sistema.

A validação da feature de upload não se restringiu à análise de `diff` ou ao `build`, mas incluiu testes diretos na interface, utilizando uma "drop zone" para o envio de arquivos. Para facilitar esse processo, um arquivo de vídeo de amostra foi disponibilizado em uma pasta "Video Sample", permitindo que o operador realizasse testes com "browser tools" e confirmasse a funcionalidade.

Após a implementação e validação, o fluxo seguiu com o merge da pull request, a remoção da branch e a atualização da branch `main` com os comandos `git checkout main` e `git pull`. Esta etapa é crucial para garantir que o desenvolvimento paralelo parta de uma base consolidada, evitando conflitos e retrabalho.

A aula aprofundou na visão de que as features devem ser tratadas como nós de um grafo de dependência, e não como uma lista linear. A prioridade pode sugerir a ordem, mas a dependência define a viabilidade, explicando como features aparentemente separadas se integram sem "gambiarras" se forem especificadas com "pontos de encaixe". Foi apresentado o conceito de "Waves" (rodadas), que são agrupamentos de features que podem ser desenvolvidas em paralelo por não possuírem dependências bloqueantes entre si. O PRD, nesse contexto, torna-se um instrumento de planejamento operacional que indica onde a paralelização é segura e onde a sequência é obrigatória. A feature de upload de vídeo, por exemplo, prepara o terreno para capacidades futuras como cadastro completo, categorização, tags e processamento com ferramentas como OpenAI e Whisper para transcrição. A lógica por trás da construção dessas dependências no PRD foi destacada como essencial para permitir o CRUD e a integração entre as partes do sistema.

**Pontos de atenção**
*   **Identificação de Features Bloqueantes:** É crucial identificar features que funcionam como capacidades base do sistema, pois elas destravam o desenvolvimento de muitas outras. O upload de vídeo é um exemplo claro, pois sem ele, funcionalidades como categorização, tags e transcrição são inviáveis.
*   **Validação Multimodal:** A validação de features não deve se limitar a análises de código (`diff`) ou compilação (`build`). Testar o comportamento diretamente na interface do usuário (ex: "drop zone") com arquivos de amostra (ex: "Video Sample") reduz ambiguidades e torna a verificação mais previsível.
*   **Estabilização da Linha Principal (`main`):** Antes de abrir novas frentes de desenvolvimento ou ramificações paralelas, é fundamental estabilizar a linha principal do código. Ramificações simultâneas sobre uma fundação instável multiplicam conflitos e retrabalho. O fluxo de `merge PR`, `delete branch`, `git checkout main` e `git pull` é essencial para isso.
*   **Features como Grafo de Dependência:** Tratar as features como nós de um grafo de dependência, e não como uma lista linear de tarefas, permite um planejamento mais eficaz. A viabilidade de uma feature é definida por suas dependências, mesmo que sua prioridade pareça alta.
*   **"Preparar o Terreno":** Uma boa prática é que features "preparem o terreno" para outras, entregando interfaces, fluxos e comportamentos esperados pelas próximas implementações. Isso reduz drasticamente o trabalho de reconciliação posterior e a necessidade de "gambiarras".
*   **Desenvolvimento Paralelo Inteligente:** Desenvolvimento paralelo não é simplesmente abrir várias branches ao mesmo tempo. É escolher frentes de trabalho independentes com base em uma análise do grafo de dependência, realizada cedo no PRD. Isso permite distribuir o trabalho entre equipes ou agentes sem criar bloqueios artificiais, aumentando a velocidade e a previsibilidade.
*   **Utilização de Waves:** Agrupar features em "Waves" (rodadas de desenvolvimento) que podem avançar em paralelo, pois não possuem dependências bloqueantes entre si, transforma o PRD em uma ferramenta de planejamento operacional eficaz.