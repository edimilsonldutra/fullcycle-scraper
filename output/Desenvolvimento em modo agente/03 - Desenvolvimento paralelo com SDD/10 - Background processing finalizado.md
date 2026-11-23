Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17799)

## Resumo da aula

Um pipeline de background processing só está validado de verdade quando executa contra os serviços externos reais que fazem parte do fluxo. Testes com OpenAI fake continuam úteis para integração controlada e repetível, mas não provam que autenticação, chamadas remotas, latência, payloads reais e efeitos persistidos estão funcionando em produção simulada. Quando o agente declara que “testou tudo”, a pergunta decisiva é objetiva: ele rodou o pipeline com a API key real, enfileirou um job real e processou um vídeo real? Sem isso, a validação ficou incompleta.

Ao receber acesso a APIs que geram custo, o agente tende a preferir caminhos mais baratos, como mocks, fakes ou scripts parciais. Esse comportamento reduz risco e consumo, mas pode mascarar a ausência da única evidência que realmente importa: a execução real do fluxo. Por isso, a instrução precisa ser explícita: usar a chave fornecida, executar a integração real e retornar artefatos verificáveis, como trechos da transcrição e o resumo produzido a partir do vídeo de exemplo.

Retomando o cenário do pipeline de vídeo já definido anteriormente, a confirmação não deve ser apenas textual; ela precisa vir acompanhada de saídas concretas do sistema. Um resultado confiável inclui status do job como completed, idioma detectado, quantidade de segmentos transcritos e um trecho do conteúdo persistido no banco. Esse tipo de evidência reduz ambiguidade porque demonstra que o processamento em background saiu do plano abstrato e percorreu o fluxo completo.

Um script standalone pode ser útil para depuração localizada, mas ele não substitui a execução do sistema completo quando o objetivo é validar comportamento end-to-end. Em background processing, diferenças de bootstrap, configuração, filas, servidor web e ambiente da worktree podem alterar o resultado final. Exigir que o agente suba o sistema inteiro força a validação das mesmas peças que participarão do uso real, inclusive portas, sessão de execução e integração entre componentes.

No fluxo paralelo já estabelecido no capítulo, a worktree funciona como unidade isolada de implementação e teste. Para executar o pipeline nessa worktree, o agente precisou preparar uma bootstrap session e garantir que dependências como node_modules, .env e .env.local estivessem coerentes com aquele contexto. Esse preparo importa porque falhas de ambiente podem parecer bugs de aplicação quando, na verdade, o processo nem chegou a reproduzir corretamente o runtime esperado.

Quando o transcribe falhou durante a execução real, apareceu exatamente o tipo de problema que testes com provider fake costumam esconder. O fluxo parecia correto no papel e nos testes, mas a integração concreta revelou uma lacuna relacionada ao tratamento de idioma. Esse é o valor do smoke test real: ele não apenas confirma sucesso, mas também expõe incompatibilidades de contrato, parâmetros ausentes e diferenças entre o comportamento simulado e o comportamento efetivo do serviço externo.

O bug encontrado no meio da execução levou a um ajuste adicional para retornar a língua de forma normalizada, e não apenas o código ISO. Esse tipo de correção incremental é esperado em validações end-to-end porque o sistema passa a lidar com dados reais, não apenas com fixtures controladas. O importante é que a correção seja incorporada ao histórico com um commit explícito, preservando rastreabilidade entre falha observada, hipótese de causa e ajuste aplicado.

A feature só pode ser considerada concluída quando o fluxo real executa de ponta a ponta e produz os artefatos esperados. No caso descrito, isso incluiu upload do vídeo, processamento em background, transcrição persistida, resumo gerado, tópicos extraídos e event log disponível para consumo posterior via SSE pela outra funcionalidade. A conclusão deixa de ser uma declaração subjetiva do agente e passa a ser uma condição verificável do sistema.

Os commits em stages, já definidos anteriormente no processo de implementação, funcionam aqui como trilha de progresso e de depuração. Quando o último commit registra o bug encontrado no smoke real e sua correção, a pull request passa a contar a história técnica da feature: implementação inicial, validações intermediárias e ajuste final descoberto em integração real. Isso facilita auditoria, revisão posterior e entendimento do que mudou por causa da execução contra a OpenAI de verdade.

Depois do merge, manter a worktree aberta deixa de trazer valor e passa a consumir espaço mental e operacional. Remover a worktree após delete branch reduz acúmulo de contexto morto e sinaliza que aquela linha de trabalho já foi integrada ao branch principal. Em desenvolvimento paralelo, esse fechamento disciplinado evita confusão entre ambientes ativos, branches já finalificados e sessões que ainda estão em andamento.

## Transcrição

00:00

Bom, pessoal, voltando aqui agora, ele falou que passou e etc.

00:05

Se colocar o PNI fake ali, ele substitui as chamadas reais e todo mundo.

00:10

Mas eu vou fazer uma pergunta básica aqui para ele. E dependendo dessa pergunta,

00:15

da forma como ele responder, eu vou ficar mais cético, cético ou não.

00:21

Eu vou fazer uma pergunta básica.

00:23

Mas você chegou a fazer uma transcrição real?

00:29

Você? Rodou o pipeline usando

00:34

a API key da OpenAI?

00:40

Vou fazer aquela pergunta básica ali para ele. Você rodou ou não?

00:44

Aí ele falou que passou. Aí, olha só que interessante que ele colocou. Não.

00:50

Fui transparente no final, mas reforçando que nenhuma chamada real aconteceu.

00:55

O que rodou é que foram todos os testes de integração com OpenAI fake.

00:59

Nunca subi o dev server, nunca enfileirei um job real usando o vídeo sample.

01:04

Olha só que interessante, galera. O que isso significa,

01:08

por mais que a gente queira trabalhar ali com tudo

01:12

aquilo que eu falei em relação à harness?

01:14

Esse tipo de coisa que nós temos que tomar cuidado.

01:17

Ele fala que fez tudo, que testou tudo,

01:19

mas no final ele não fez o teste de integração em relação ao pipeline.

01:25

Ou seja, no papel está tudo bonito, no teste está tudo bonito,

01:28

e etc. Mas ele não usou a minha chave da OpenAI.

01:32

Tem alguns pontos aqui importantes que eu poderia ter sido mais explícito.

01:36

Por exemplo, ao fazer o teste, quando eu te der a chave da OpenAI,

01:42

faça testes reais com a OpenAI.

01:44

Obviamente que esses modelos, e o que eu já senti de várias formas,

01:48

é toda vez que ele vai fazer chamadas externas,

01:50

algo que vai consumir, não digo nem token, mas API externas,

01:55

eles tendem a não querer fazer as chamadas reais e etc.

01:58

Isso já aconteceu várias vezes.

02:00

Mas eu vou fazer o seguinte, eu vou colocar aqui,

02:04

ele está colocando, isso vai gerar custo para você.

02:07

Mas é a única forma de validar. Eu falo assim,

02:09

eu vou colocar, eu quero que você valide.

02:14

executando e me mostre que funcionou.

02:19

Inclusive, trazendo o

02:22

texto sumarizado do vídeo exemplo.

02:28

Então, vou colocar aqui para ele e vamos ver o que vai rolar nesse caso. Então,

02:34

vamos deixar ele aqui pensando. Mas, de fato,

02:38

acontece e é muito comum. Ele fala que termina uma tarefa,

02:42

ele diz que terminou, mas no final ele fala,

02:44

olha, eu não fui tão transparente com você.

02:46

Eu até falei que roda com uma variável fake ali,

02:52

mas eu não fui muito transparente ali com você. Então,

02:55

agora ele falou que vai rodar um smoke até ser end-to-end real. Então,

03:00

primeiro ele vai ver o tamanho da fixture para preparar um script

03:03

standalone que carrega o código do repositório sem precisar subir o Next inteiro.

03:07

Por que ele está fazendo isso? Porque ele roda como um processo em background.

03:13

Eu vou deixar ele fazer isso,

03:14

mas eu vou depois... Na realidade,

03:17

eu já vou pedir para ele fazer diferente aqui, tá?

03:21

Eu quero que você suba o sistema inteiro para

03:28

Ser algo real, tá?

03:32

Estou colocando aqui forte para ele, tá? Então...

03:37

Ele fica tendendo a não querer trabalhar.

03:40

Então agora ele vai ter que olhar as portas, né? Porta 3001 está ocupada,

03:44

Vou usar 3002.

03:46

Pelo menos ele pegou aquela ideia do que a

03:50

Gente tinha colocado naquela hora ali para a gente, tá?

03:56

E deixa ele voltar rodando. Eu até abri aqui o meu .env e o .local.

04:00

Eu dei um pause só para você não ver a minha

04:02

Chave da OpenAI para ver se estava aqui bonitinho.

04:05

E agora ele está...

04:08

Colocando e organizando uma Bootstrap Session para

04:14

Ele conseguir realmente fazer a parada funcionar.

04:19

Então olha só que interessante,

04:21

Ele vai precisar de um script para rodar

04:23

Dentro da Worktree para fazer o NodeModules funcionar.

04:28

Então vamos lá, botar esse cara ali para rodar.

04:32

Criou a sessão, agora ele vai fazer o upload.

04:35

Porque ele é um background processing, então ele não consegue arrastar, nesse caso,

04:40

O vídeo para fazer o upload, mas ele quer testar o quê?

04:44

A parte que ele roda em background, porque ele é um pipeline,

04:47

Né? Então aqui, ó, ele está fazendo a execução,

04:51

Falhou o transcribe e agora a gente já cai naquele problema. Opa,

04:56

Tinha algum erro ou alguma coisa aqui que estava faltando,

05:00

Né? Então vamos ver o que está rolando aqui.

05:04

Existem algumas coisas que são mais difíceis para eles testarem, porque,

05:07

Por exemplo, ele tem que fazer um upload de um vídeo,

05:09

Ou às vezes ele tem que simular algo muito interno num browser,

05:12

Tá? Mas, de qualquer forma, ele já viu aqui que tem log,

05:15

Que tem algum problema aqui para a gente, tá? Então,

05:18

Ele já encontrou problema. A gente tinha bug e, provavelmente,

05:23

De alguma forma ali ele precisava saber o idioma ou alguma coisa desse tipo.

05:28

Mas, eu não estou querendo focar nesses detalhes,

05:30

Eu quero ver o negócio funcionar. O retry aceitou o transcribing,

05:34

Agora ele vai acompanhar de novo para ver se está rodando ali o pipeline. Então vamos lá,

05:42

Aguardando um pouquinho, vou

05:47

Dar um pause e a gente volta somente para a

05:49

Gente não ficar um tempão aqui nesse vídeo.

05:53

E aí ele percebeu, só para você saber o que aconteceu aqui,

05:56

Ele não tinha reiniciado o servidor, ele reiniciou,

05:59

E daí eu acho que carregaram as coisas,

06:01

E ele falou, olha, o pipeline real funcionou de ponta a ponta,

06:04

Limpando o script temporário que ele criou. Para ele fazer o teste,

06:08

Mas ele colocou aqui, rodou o vídeo, o job deu como completed,

06:14

E aqui ele trouxe,

06:17

Falando que detectou um português com 33 segmentos,

06:21

E aqui ele trouxe um pedaço do texto que estava no banco de dados,

06:26

Que foi realmente transcrito. Então, ele falou que foi descoberto,

06:31

Ele fez um commit do Smoke.

06:33

Aqui para retornar a língua e não somente o ISO,

06:36

Então ele descobriu que provavelmente ali ele tinha que passar

06:38

Um parâmetro do idioma que estava sendo falado,

06:41

E aqui ele falou, Smoke End-to-End Real Concluído,

06:45

Fluxo executado contra o OpenAI de verdade, com Whisper GPT 4.1 Nano,

06:50

Com OpenAI Fake igual a zero, Dev Server rodando na porta 3002,

06:55

Usou o vídeo de verdade para rodar com o tamanho do vídeo,

06:59

Via POST, então ele trouxe essa parte aqui, e aqui ele trouxe...

07:02

O que eu pedi para ele. Os primeiros segmentos que ele encontrou,

07:06

O resumo que foi trazido do vídeo, os tópicos,

07:09

E ele colocou um Event Log que a função 11, a funcionalidade 11,

07:15

Vai consumir via SSE essas transcrições gravadas,

07:20

Incluindo peios intermediários,

07:22

Caso ele faça retry manual e etc.

07:26

Então ele fez um commit extra para normalizar.

07:30

A língua. Então, basicamente, o bug que ele encontrou,

07:33

Provavelmente, no meio desse processo,

07:35

Foi em relação a essa parte da língua ali que ele colocou.

07:40

Mas, de forma geral, ele terminou ali o processo dessa feature aqui pra gente.

07:47

O que eu vou fazer aqui nesse caso?

07:50

Eu vou dar um... Eu

07:55

Vou chegar aqui e vou dar um git commit push PR de cara.

08:01

Para ele fazer a pull request. Galera, perceba,

08:04

Eu não estou fazendo a revisão de código,

08:05

Eu não estou me preocupando com a qualidade de código,

08:09

Principalmente aqui nesse capítulo, nessa parte do curso, tá?

08:15

Nosso ponto aqui é instrução. Por quê? Porque as qualidades,

08:19

Guidelines, tudo isso entra na parte de harness, tá? Então,

08:23

Nosso ponto principal agora aqui é fazer com que as tarefas

08:26

Sejam executadas com os agentes rodando em paralelo aqui para mim.

08:31

Então, ele gerou aqui a pull request, foi criada aqui para mim.

08:37

Vou abrir a minha pull request.

08:39

Então, ele fala o que ele fez, adicionar o pipeline de processamento em background,

08:43

Colocou ali, mandar... ele criou um endpoint de retrial dos eventos, dos hooks,

08:50

E ele mostrou o plano de teste que ele fez e o que ele fez,

08:55

E aqui agora ele colocou o End-to-End Smoke Teste Real com um vídeo tal.

08:59

Antes ele não tinha feito isso, e depois ele conseguiu colocar.

09:04

E aqui foram os commits que ele fez, lembra? O Stage 1, 2,

09:07

3, 4, 5, e o último commit foi esse último bug que ele encontrou.

09:13

Mas perceba que ele fez realmente um commit,

09:17

Por parte do plano que tinha sido colocado ali para a gente.

09:22

A gente não vai ter conflito nesse caso,

09:24

Porque está sendo a primeira tarefa que está sendo desenvolvida. Então,

09:30

A gente não tem conflito nesse momento ali com o main. Então, vou dar aqui para mim,

09:36

Vou dar aqui um delete branch, para nem ficar lá no online.

09:42

E agora, aqui no caso do Cloud, o que vai acontecer?

09:46

Se você olhar em relação aos WorkTrees, eu tenho três WorkTrees,

09:49

Essa aqui é a WorkTree que está pronta, né?

09:52

E o que eu posso fazer aqui? Isso aqui, dicas,

09:56

Não sei se isso vai perdurar por muito tempo no Cloud Code especificamente.

10:01

Mas quando você sai da sessão do Cloud Code,

10:03

vou dar um Ctrl+C duas vezes,

10:05

ele vai perguntar aqui para mim, você quer manter a Work Tree?

10:09

Ou você quer remover a work tree falando que tudo vai ser perdido.

10:13

Eu quero remover porque eu já fiz o merge.

10:15

Então eu não estou preocupado com isso.

10:17

Eu vou dar um remove work tree aqui para mim.

10:19

E pum.

10:21

Ele tem que jogar fora esses arquivos todos ali que ele criou. Aqui para mim.

10:29

Então em tese, galera.

10:31

A gente já tem uma das features que a gente precisava da Wave 3 pronta.

10:36

Então a gente vai precisar agora.

10:38

Verificar a feature 07 e a feature 12.

10:41

Isso a gente vai ver no próximo vídeo para ver se ele já terminou,

10:43

qual que é o status das coisas.

10:46

Aparentemente aqui ele deve estar trabalhando porque dá para ver pela

10:50

corzinha que tem coisa aqui que não está comitada.

10:53

A gente vai dar uma olhada e a gente vê isso no nosso próximo vídeo.

## Resumo IA

**Abreviações**
*   API: Application Programming Interface
*   Dev Server: Servidor de Desenvolvimento
*   ISO: International Organization for Standardization
*   PR: Pull Request
*   SSE: Server-Sent Events

**Resumo**
O principal objetivo desta aula é demonstrar a importância crítica da validação de pipelines de processamento em background contra serviços externos reais, em contraste com testes baseados em mocks ou fakes. A aula enfatiza que, embora testes com provedores falsos sejam úteis para integração controlada, eles não comprovam o funcionamento de autenticação, chamadas remotas, latência, payloads reais e efeitos persistidos em um ambiente de produção simulado. O instrutor inicia a aula questionando a validade de um relatório de conclusão que se baseou apenas em testes com "OpenAI fake", sem executar o pipeline com a API key real, enfileirar um job real ou processar um vídeo verdadeiro.

Para forçar a validação real, o instrutor exige que o agente (simulado) utilize a chave de API fornecida para realizar integrações autênticas, retornando artefatos verificáveis como trechos de transcrição e resumos gerados a partir de um vídeo de exemplo. Inicialmente, o agente tenta otimizar custos e tempo com um script standalone, mas é instruído a "subir o sistema inteiro" (o dev server) para garantir que todas as partes do sistema, incluindo portas, configuração e a integração entre componentes, sejam validadas em um ambiente o mais próximo possível do real.

O fluxo de validação envolve a preparação de uma "bootstrap session" na worktree isolada, garantindo a coerência de dependências como `node_modules` e arquivos `.env`. Durante a execução do pipeline real, um bug relacionado ao tratamento do idioma na transcrição é descoberto, provando o valor do "smoke test real" em expor incompatibilidades de contrato e diferenças entre o comportamento simulado e o efetivo. Após a correção do bug, o pipeline é executado com sucesso de ponta a ponta, produzindo os artefatos esperados: upload de vídeo, job status "completed", idioma detectado, quantidade de segmentos transcritos, trecho do conteúdo persistido, resumo gerado, tópicos extraídos e um event log para consumo via SSE. A feature é considerada concluída apenas com a produção desses resultados verificáveis. A aula finaliza com a criação de uma Pull Request (PR) que documenta a história técnica da feature através de commits em stages, incluindo a correção do bug descoberto na integração real, e a remoção disciplinada da worktree após o merge para evitar acúmulo de contexto morto.

**Pontos de atenção**
*   **Validação Real vs. Testes Fakes**: A validação genuína de um pipeline de background processing só ocorre ao executá-lo contra serviços externos reais. Testes com fakes são úteis para integração controlada e repetível, mas não validam autenticação, chamadas remotas, latência, payloads e persistência em um ambiente simulado de produção.
*   **Evidência Concreta**: A única evidência que realmente importa é a execução real do fluxo. Declarações como "testei tudo" devem ser corroboradas por artefatos verificáveis do sistema, como status do job, idioma detectado, quantidade de segmentos, trechos de conteúdo persistido, resumos e logs de eventos.
*   **Custo e Comportamento do Agente**: Agentes (ou desenvolvedores) tendem a evitar chamadas a APIs que geram custo, optando por mocks ou fakes. Essa prática, embora reduza riscos e consumo, pode mascarar a ausência da validação mais importante.
*   **Sistema Completo vs. Scripts Standalone**: Scripts standalone são bons para depuração localizada, mas não substituem a execução do sistema completo para validação end-to-end. Diferenças em bootstrap, configuração, filas, servidor web e ambiente da worktree podem alterar o resultado final.
*   **Erros de Ambiente**: Falhas de ambiente (ex: configuração de portas, `.env`, `node_modules`, sessão de bootstrap) podem ser confundidas com bugs de aplicação, mas, na verdade, impedem a correta reprodução do runtime esperado.
*   **Valor do Smoke Test Real**: O smoke test real não apenas confirma o sucesso, mas é crucial para expor incompatibilidades de contrato, parâmetros ausentes e diferenças entre o comportamento simulado e o comportamento efetivo de serviços externos.
*   **Correções Incrementais e Rastreabilidade**: É esperado encontrar e corrigir bugs (como problemas de tratamento de idioma) durante validações end-to-end com dados reais. Essas correções devem ser incorporadas ao histórico com commits explícitos para preservar a rastreabilidade entre a falha, a hipótese de causa e o ajuste aplicado.
*   **Definição de Conclusão de Feature**: Uma feature só pode ser considerada concluída quando o fluxo real executa de ponta a ponta e produz todos os artefatos esperados, transformando a conclusão de uma declaração subjetiva em uma condição verificável do sistema.
*   **Gestão de Commits e Pull Requests**: A utilização de commits em stages (etapas) e a documentação na Pull Request (PR) contam a história técnica da feature, desde a implementação inicial até as validações intermediárias e os ajustes finais descobertos em integração real, facilitando auditoria e revisão.
*   **Limpeza de Worktrees**: Após o merge e exclusão do branch, remover a worktree é uma boa prática para evitar acúmulo de contexto morto, liberar espaço e sinalizar a integração completa da linha de trabalho, prevenindo confusão em ambientes de desenvolvimento paralelo.