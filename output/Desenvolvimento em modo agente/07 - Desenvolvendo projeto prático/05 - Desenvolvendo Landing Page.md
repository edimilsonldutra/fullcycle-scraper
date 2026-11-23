Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17980)

## Resumo da aula

A implementação da feature é guiada por três artefatos complementares: spec.md, plan.md e contract.md. Retomando o fluxo já estabelecido, o spec.md define o que precisa ser entregue e o plan.md organiza as etapas; o ponto novo aqui é que o agente implementador usa esses arquivos como fonte operacional para executar a feature. O contract.md deixa de ser apenas um documento de validação e passa a atuar como restrição ativa durante a implementação. Isso reduz ambiguidade e impede que a entrega seja considerada pronta sem cumprir os critérios verificáveis.

O contrato funciona como o critério que governa a implementação e a validação da própria feature. Se a implementação não satisfaz o contrato, o agente não consegue confirmar que o resultado está correto, porque a verificação final depende exatamente dessas condições. Por isso, o contrato não é acessório: ele define o que precisa existir, o que deve ser testado e quais evidências tornam a entrega aceitável. Em fluxo com múltiplos agentes, isso também garante que outro agente consiga revisar ou validar o resultado sem reconstruir contexto manualmente.

Quando o contrato exige insumos específicos, o agente precisa materializá-los no ambiente antes de validar a feature. Se um teste depende de uma imagem, por exemplo, essa imagem precisa existir tanto para a execução local do agente implementador quanto para a validação posterior por outro agente. Essa preparação evita falsos negativos causados por ambiente incompleto e torna a entrega reproduzível. O valor prático está em transformar dependências implícitas em artefatos explícitos e disponíveis.

A implementação não é verificada apenas de forma genérica; cada critério de aceitação é confrontado com a entrega produzida. O contrato também orienta quais camadas do sistema entram na validação, como API, serviço, worker, CLI ou UI, conforme a natureza da feature. Isso permite separar testes e responsabilidades por camada, em vez de tratar toda feature como um bloco único. No caso da landing page, a ênfase recai mais sobre UI, mas o mesmo mecanismo escala para features com arquitetura mais complexa.

Antes de delegar a implementação, o repositório precisa estar em um estado minimamente organizado. O fluxo mostrado inclui criar commits iniciais descritivos e depois abrir uma branch específica para a feature, como f01-landing-page. Essa separação facilita rastreabilidade, isola mudanças e prepara o terreno para evolução incremental da feature. Mesmo em um experimento rápido, estruturar o histórico desde o início melhora controle e revisão.

A execução da skill de implementação pode receber a feature por identificador, como F01, ou por referência direta à pasta correspondente. Além disso, é possível reforçar o contexto com artefatos adicionais, como páginas de system design ou referências específicas da landing page do VideoMax. Esse reforço não substitui a automação do fluxo, mas aumenta a precisão quando o agente precisa alinhar implementação visual ou estrutural com uma fonte concreta. Em tarefas práticas, redundância controlada no prompt costuma ser mais útil do que depender de inferência excessiva.

O processo de implementação passa por uma checagem inicial de dependências (pre-flight), pela execução das fases previstas no plano (Stage 1, Stage 2, Stage 3) e por uma verificação final. Essa etapa final consulta os gates definidos e executa testes, incluindo Playwright quando o contrato exige validação de interface. A sequência importa porque primeiro o agente garante que consegue rodar, depois implementa por etapas e só então valida o resultado completo. Isso aproxima o fluxo automatizado de um pipeline disciplinado de entrega.

A validação final pode revelar desvios de implementação, como ícone invertido ou cor incorreta, antes de concluir a feature. Quando a entrega atende ao nível esperado, o status correspondente no arquivo de tracking, como PRDProgress, é atualizado para Implemented. Retomando o tracking já definido anteriormente, a novidade aqui é o fechamento do ciclo: a feature sai do planejamento e entra formalmente no estado de implementada. Esse vínculo entre execução e tracking permite que o projeto avance com estado observável e consistente.

## Transcrição

00:00

Bom, pessoal, agora que a gente passou pelo camarada que vai escrever,

00:06

que escreveu a feature para a gente e que criou o contrato,

00:10

a gente tem que passar pelo camarada que vai implementar essa feature. Então,

00:14

se a gente for aqui nesse camarada,

00:17

e deixa eu abrir aqui, ele implementa a feature.

00:23

Esse cara aqui é uma skill que ele vai fazer o quê?

00:26

Ele vai implementar a feature ali para a gente.

00:30

E o grande ponto de tudo isso é o seguinte,

00:33

ele vai ser guiado para fazer a implementação lendo o spec.md,

00:39

o plan.md e o contract.md.

00:41

E um dos pontos aqui importantes em relação à execução dos steps é,

00:47

ele vai ver qual é a feature,

00:49

em qual pasta que ele vai buscar e etc. Mas, uma vez que ele carregue o controle,

00:54

você vai perceber que o tempo todo aqui vai ter um contract.md.

00:59

E a ideia desse contract.md,

01:01

no final das contas, vai ser o quê? No seguinte, no final do dia,

01:05

você vai ter que usar o plano, usar as especificações que eu fiz,

01:10

mas eu preciso garantir que você cumpra o contrato.

01:14

Porque se você não cumprir o contrato,

01:16

você mesmo não vai conseguir validar se aquilo que você está fazendo está certo.

01:20

Então, essa aqui é a ideia.

01:22

Se você olhar, ele vai olhar os pré-requisitos do contrato.

01:25

Por quê? Porque se esse contrato...

01:28

precisar de algum pré-requisito,

01:30

ele vai ter que criar esse pré-requisito desse ambiente,

01:34

por quê? Para ele mesmo rodar,

01:36

mas para quando outro agente for avaliar o resultado,

01:40

esses pré-requisitos já existam para que esse outro agente consiga utilizar. Por exemplo,

01:46

eu preciso de uma imagem, então ele tem que garantir que ele vai ter uma imagem ali,

01:50

porque se ele não tiver uma imagem...

01:52

ele não vai conseguir testar,

01:54

mas o outro cara que está de fora talvez também não consiga testar.

01:57

Então ele sempre vai tentar gerar o material necessário

02:01

para que quem for testar isso aqui,

02:04

inclusive ele, tenha todas as partes necessárias aqui.

02:07

Então aqui basicamente ele traz tudo isso e vai...

02:12

bater cada critério de aceitação para ver se ele acabou passando.

02:16

E daí tem diversas formas que ele vai trabalhar e diversas camadas.

02:22

Ele pode ver a camada de API, a camada de serviço,

02:26

a camada de worker, a camada de CLI. Ou seja, basicamente no contrato,

02:31

ele vai verificando quais são as camadas que existem no seu sistema.

02:36

E ele separa os testes e as camadas conforme cada feature,

02:40

né? Na feature que a gente viu,

02:41

tinha ali mais a parte de UI,

02:43

mas você vai perceber que conforme vai passando as coisas,

02:46

a gente começa entrando em aspectos ali mais complexos no meio de toda a história,

02:52

fechou? Então, essa que é a ideia principal aí. Lembrando que o nosso projeto,

02:57

ele é um projeto onde eu posso fazer upload de vídeos...

03:00

onde ele faz a transcrição do vídeo,

03:02

onde eu consigo clicar no meu vídeo,

03:04

Onde eu consigo ver o resumo e coisas desse tipo.

03:07

Então, essa que é a ideia do meu Videomax

03:09

para que eu consiga subir essas minhas informações.

03:13

Então, aqui está o meu camarada que faz a implementação no meio de tudo isso.

03:20

Como que eu rodo para ele implementar isso? Então, eu vou aqui no meu Cloud.md,

03:27

meu Cloud.md não, eu vou aqui nesse cara.

03:29

E eu vou digitar aqui nesse

03:32

caso para ele implementar essa feature. Pessoal,

03:37

só para vocês saberem, ninguém fica com preconceito aqui para mim.

03:41

Esse cara inicial, tá? Eu vou fazer tudo no main, tá?

03:46

Na realidade, eu vou até pedir para ele mudar de branch,

03:48

mas eu vou dar aqui para ele, para mim, primeiro para ele fazer um commit aqui para mim.

03:54

Para ele commitar todas as features aqui para mim. Deixa eu ver.

03:58

Aqui ele não tem nenhum... ele nunca deu um git init, então eu vou colocar faça

04:06

o primeiro commit descritivo desse

04:13

das

04:16

features e scar folding separados estou pedindo aqui apenas

04:23

para ele criar aqui para mim dois commits para

04:26

ele conseguir botar todo esse cara aqui e vamos lá

04:31

para ele conseguir trabalhar em cima de tudo isso

04:34

Bora. Ele está comitando todos os caras.

04:38

E depois, em cima disso, eu vou pedir para ele criar uma nova branch.

04:43

Depois, a gente vai na branch e coloca uma branch de landing page.

04:46

Feature 01, landing page, para ele conseguir trabalhar.

04:49

E esses bugs aqui são os bugs malucos aqui do Cloud.

04:53

Mas não tem problema.

04:54

Vamos nessa aqui para ele fazer esses nossos commits iniciais aqui para a gente.

05:01

Bom, pessoal, ele terminou os meus commits aqui. Então, o que eu vou fazer é...

05:06

Eu vou rodar aqui um git checkout -b f01-landing-page.

05:13

Somente para quem quiser saber,

05:15

quando eu coloco uma exclamação aqui no Cloud e digito um comando bash,

05:18

ele executa, mas joga esse comando ali para o Cloud, ali para a gente.

05:23

E agora, o que eu vou fazer? Eu vou rodar um implement feature. Então,

05:26

eu vou dar aqui um /implement-feature. Eu vou colocar o meu PRD, só

05:32

para ele saber. E eu posso colocar... um F01, ou eu posso apontar,

05:37

inclusive, para a pasta da minha feature, que eu, às vezes,

05:41

eu prefiro mais. F01 aqui em relação à minha landing page.

05:45

Se eu quiser reforçar ainda mais,

05:47

eu posso ainda até colocar siga a siga

05:54

a página a

05:58

landing page

06:00

de arroba, eu posso passar o meu das minhas pages, dos meus system design.

06:07

a VideoMax page eu posso reforçar e etc.

06:11

Galera, uma das coisas que eu já desencanei na minha vida

06:13

em relação com o IA é não custa reforçar.

06:16

Eu sei que comandos funcionam de uma forma extremamente forte.

06:19

Eu sei que as skills estão bem.

06:20

Mas, cara, não custa às vezes escrever um pouco mais de linha,

06:24

a não ser que você queira fazer algo extremamente automatizado.

06:26

Isso funciona? Funciona. Mas se eu estou aqui nesse momento,

06:30

Não custa nada eu fazer isso e dar um Enter.

06:32

Então, agora, o que ele vai começar a fazer?

06:35

Ele vai começar a fazer a implementação dessa minha feature número 1,

06:39

Beleza? E depois, né,

06:41

de algum tempo aí rodando isso aí,

06:43

a gente vai ver como é que ficou o resultado aí dessa feature.

06:47

Então, eu vou esperar ele terminar isso aqui pra gente

06:50

conseguir ver o resultado e a gente já volta.

06:53

Se você verificar aqui, ó. Ele está dando um pré-flight, ou seja,

06:57

ele verifica tudo que ele tem de dependências para ver se ele consegue subir.

07:01

E depois ele bota as fases que ele encontrou no plano.

07:04

Stage 1, Stage 2, Stage 3. E depois a final verification,

07:08

que ele vai ver os gates mais o Playwright,

07:10

que é porque ele vai estar olhando o contrato.

07:13

Aqui ele terminou as três fases e agora ele está na final verification.

07:18

Que é provavelmente quando ele já está iniciando o ambiente aqui, né?

07:22

E provavelmente vai começar a fazer os testes ali com o Playwright.

07:26

Vamos ver como é que ele vai se sair.

07:29

E bom, pessoal, ele finalmente terminou aqui.

07:32

Ele passou pelo processo de revisão dele e começou

07:35

a perceber que ele tinha feito ícone invertido,

07:38

com cor diferente e tudo mais.

07:40

E eu acessei aqui e aparentemente está razoável. Eu não vou...

07:46

Clicar aqui para dizer que tem que estar pixel perfect,

07:49

mas de forma geral ele fez a nossa tarefa aqui número 1,

07:54

a nossa feature número 1. Então, se em tese eu olhar para cá, onde que está?

08:01

Docs, PRD Progress aqui para mim.

08:05

Se a gente olhar aqui, está como Implemented. Então,

08:08

em tese agora, isso aqui foi implementado e...

08:12

terminamos uma etapa aqui com o nosso camarada da nossa primeira tarefa, tá? Então,

08:17

eu acho que esse aí é um ponto importante que a gente tem que levar em consideração.

08:23

Agora, o ponto é o que a gente faz daqui pra frente em relação a isso.

08:28

Então, isso a gente vai ver no nosso próximo vídeo.

## Resumo IA

**Abreviações**
*   **API**: Application Programming Interface
*   **CLI**: Command Line Interface
*   **IA**: Inteligência Artificial
*   **MD**: Markdown
*   **PRD**: Product Requirement Document (implícito no "PRDProgress")
*   **UI**: User Interface

**Resumo**
A aula focou na fase de implementação de uma feature, onde um "agente implementador" utiliza três artefatos principais: `spec.md`, `plan.md` e `contract.md`. O `spec.md` detalha o que precisa ser entregue, o `plan.md` organiza as etapas da implementação, e o `contract.md` atua como uma restrição ativa e um critério de validação, definindo o que deve existir, ser testado e as evidências que tornam a entrega aceitável.

O fluxo de implementação detalhado inclui a preparação do ambiente, onde o agente materializa insumos específicos (como imagens para testes) exigidos pelo contrato para garantir a reprodutibilidade. O contrato também orienta a validação por camadas do sistema (API, serviço, worker, CLI ou UI), permitindo testes mais segmentados. Antes de delegar a implementação, o repositório deve ser organizado com commits iniciais descritivos e uma branch específica para a feature.

A execução da implementação é feita através de uma "skill" que recebe a feature por identificador ou referência à pasta, podendo ter o contexto reforçado com artefatos adicionais. O processo segue uma sequência disciplinada: uma checagem inicial de dependências (`pre-flight`), a execução das fases definidas no plano (`Stage 1, 2, 3`) e uma verificação final que consulta "gates" e executa testes (como o Playwright para UI). Ao final, o arquivo de tracking `PRDProgress` é atualizado para "Implemented", formalizando a conclusão da feature e tornando o estado do projeto observável.

**Pontos de atenção**
*   **O Contrato como Restrição Ativa**: O `contract.md` não é apenas um documento de validação passivo, mas uma restrição ativa que governa a implementação e a validação. Sua ausência ou não cumprimento impede o agente de confirmar a correção do resultado.
*   **Materialização de Dependências**: É crucial que o agente materialize todos os insumos específicos (ex: imagens) exigidos pelo contrato no ambiente de execução. Isso evita "falsos negativos" e garante que a entrega seja reproduzível tanto para o implementador quanto para outros agentes de validação.
*   **Validação por Camada**: Utilize o contrato para orientar a validação em camadas específicas do sistema (API, serviço, worker, CLI, UI). Isso permite separar testes e responsabilidades, evitando tratar a feature como um bloco único e monolítico.
*   **Organização do Repositório**: Antes de iniciar a implementação, garanta que o repositório esteja minimamente organizado com commits iniciais descritivos e uma branch específica para a feature (ex: `f01-landing-page`). Isso facilita a rastreabilidade, isola as mudanças e prepara o terreno para revisões e evolução incremental.
*   **Reforço de Contexto para IA**: Ao interagir com agentes de IA, "redundância controlada no prompt costuma ser mais útil do que depender de inferência excessiva". Não hesite em reforçar o contexto com artefatos adicionais ou referências específicas para aumentar a precisão da implementação.
*   **Fluxo de Implementação Disciplinado**: O processo segue um pipeline claro (pré-flight -> stages do plano -> verificação final). Essa sequência garante que as dependências sejam checadas primeiro, o trabalho seja executado em etapas e o resultado final seja validado de forma sistemática.
*   **Atualização Consistente do Tracking**: A atualização do `PRDProgress` para "Implemented" após a conclusão da feature é essencial para vincular a execução ao tracking, mantendo o estado do projeto observável e consistente.