Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17982)

## Resumo da aula

O evaluator automatiza a validação de uma feature já implementada usando os artefatos do fluxo anterior. Em vez de depender apenas do ID da feature ou apenas do contrato, a execução aceita ambos porque a ferramenta consegue inferir o contrato correto a partir do PRD e da referência informada. Essa flexibilidade reduz atrito operacional sem quebrar o vínculo com a especificação que orienta a validação.

Retomando o uso de spec.md, plan.md e contract.md, o ponto novo aqui é a busca automática do contrato durante a avaliação. Quando a entrada é algo como feature F01, o processo localiza o contrato correspondente e usa esse artefato como base para verificar a entrega. Isso mantém a avaliação alinhada aos critérios formais sem exigir que o operador sempre informe o caminho exato do contrato.

A avaliação combina duas camadas complementares. Primeiro, os Quality Gates verificam aspectos objetivos do projeto, como os gates já configurados no fluxo; depois, o Playwright CLI executa validações de interface com captura de screenshots e comparação de resultados. A consequência prática é que a evidência final não depende só de logs textuais: ela inclui sinais observáveis da execução.

Um resultado indeterminate indica que a automação não encontrou falha objetiva, mas também não consegue afirmar conformidade total sem julgamento humano. Isso ocorre quando o critério depende de percepção visual ou outra análise subjetiva. Nessa situação, o sistema preserva a rastreabilidade marcando a pendência manual em vez de promover uma aprovação total artificial.

O eval report registra o que foi executado, o que passou, o que não passou e quais verificações exigem revisão manual. Esse relatório não serve apenas para consulta; ele funciona como evidência persistida da avaliação realizada. Em fluxos com múltiplos agentes ou revisões posteriores, esse artefato evita decisões baseadas apenas em memória ou interpretação informal.

Retomando o PRDProgress.json, implemented indica que a feature foi entregue do ponto de vista de implementação, mas ainda pode faltar confirmação final de avaliação. O status done só faz sentido quando a validação foi concluída e existe comprovação suficiente, inclusive após a etapa manual quando necessária. Essa separação impede que implementação e aceitação final sejam tratadas como a mesma coisa.

Quando a verificação termina, o tracking não deve guardar apenas um estado textual. O valor novo aqui é anexar ao item concluído o link para o report gerado, de modo que o status done venha acompanhado da evidência que o sustenta. Isso transforma o arquivo de progresso em um índice auditável de entregas, e não apenas em uma lista de marcações.

## Transcrição

00:00

Bom pessoal, a gente falou então no vídeo anterior sobre o evaluator,

00:06

a gente viu que a gente teve a implementação,

00:09

a gente tem uma skill especificamente apenas para fazer esse tipo de

00:13

análise e é o que a gente vai rodar agora.

00:15

Então eu vou dar um clear aqui para ele limpar e não contaminar nenhuma janela,

00:20

vou rodar aqui um evaluator, aqui que é o nosso plugin.

00:24

Vou passar aqui para ele qual que é o PRD e eu vou passar para

00:28

ele qual é a feature que eu quero que ele faça essa avaliação aqui para mim.

00:32

Que é essa feature aqui. Ou, na realidade, eu posso passar diretamente, inclusive,

00:38

o contrato que eu quero. A IA,

00:41

ela é bem inteligente para conseguir entender e inferir,

00:44

porque ela sabe que ela vai ter que procurar por um contrato,

00:47

tá? Então, vai depender muito de como você quer trabalhar,

00:51

etc. Eu não fico muito... preso a isso.

00:54

Mas quando eu falar a feature, eu posso passar só o ID da feature.

00:57

Eu poderia colocar apenas o PRD feature F01 e ele vai buscar, tá? De forma geral.

01:03

Perceba que ele vai buscar sempre ali o contrato conforme a gente precisa. Então,

01:08

vou dar um ENTER aqui e vai demorar uns minutinhos aí, obviamente, para ele rodar,

01:13

para ver como é que tudo está funcionando e daí a gente

01:16

aguarda aí o resultado para ver o que ele trouxe,

01:19

o que ele não trouxe ou pode ser que ele fale, poxa, olha...

01:22

Funcionou de primeira, vamos ver o que vai acontecer.

01:26

Se você ver agora, ele está rodando e ele subiu e ele está falando,

01:30

opa, deixa eu fazer,

01:32

rodar os Quality Gates agora aqui para mim. E agora ele já falou, olha,

01:35

os três Gates que eu coloquei aqui já rodaram aqui para mim.

01:39

E agora deixa eu subir o Playwright CLI,

01:41

provavelmente ele vai começar a tirar foto e vai fazer as comparações.

01:46

E então, pessoal, o que ele fez?

01:48

Ele gerou um relatório aqui para a gente, falando que ele seguiu.

01:54

Os critérios passaram, ou seja, tem os critérios de avaliação,

01:58

ou seja, os quatro foram passados,

02:00

nenhum falhou, e tem um que é indeterminado. O que é indeterminado?

02:04

Quando ele acha que eu tenho que ter uma verificação manual, ou seja,

02:08

uma verificação subjetiva aqui para a gente. E ele trouxe o screenshot,

02:12

caso eu queira... ver essa avaliação,

02:15

tá? Então, tudo que ele pode avaliar, ele coloca,

02:18

mas se ele achar que precisa de algo subjetivo,

02:21

ele deixa como pending, tá vendo aqui, e como pass,

02:25

mas de qualquer forma, ele não termina de marcar a tarefa como 100% concluída,

02:32

nesse meu caso, porque teve essa parte que é, vamos dizer, visual.

02:39

Aqui que ele coloca, então se eu olhar aqui o meu progress.json,

02:43

você vai ver que está implemented,

02:44

mas ele não marcou quando está completamente

02:48

terminado porque tem esse aspecto que está,

02:52

não é falhando, mas tem uma parte manual e aqui ele colocou o relatório dele,

02:58

então provavelmente ele deixou o screenshot,

03:00

caso eu queira olhar, e aqui eu tenho o eval report dele,

03:05

falando tudo o que ele fez, todos os detalhes

03:08

O que rodou, o que não passou e etc. Então,

03:11

Aqui está o relatório detalhado e é bom que ele deixa um artefato gravado.

03:16

Eu vou colocar, terminei de ver e está ok.

03:24

D1 completar no

03:30

VRD progress.

03:36

Eu estou falando para ele terminar ou completar.

03:38

Eu mesmo poderia entrar e mudar o campo.

03:40

Só quero colocar aqui. Ele está muito louco por conta do meu zoom alto aqui.

03:45

Mas ele vai provavelmente alterar o meu camarada aqui, ó.

03:49

Agora, landing page, ele coloca, olha só que interessante,

03:53

status done, e ele coloca,

03:55

né, o link pro report que ele gerou em relação a isso,

04:01

tá? Então não é somente que ele terminou,

04:04

ele terminou e tá aqui o que foi avaliado pra comprovar o que ele terminou.

04:09

Então isso aí é um ponto que eu acho que acaba sendo

04:12

bastante interessante pra gente ver aí durante todo o nosso fluxo,

04:16

tá? No próximo vídeo,

04:17

a gente vai fazer isso de uma forma um pouquinho diferente e eu

04:20

acho que ali que as coisas vão começar a ficar mais bacanas,

04:23

beleza? Vamos nessa!

## Resumo IA

**Abreviações**
*   **ID**: Identificador
*   **PRD**: Product Requirements Document (Documento de Requisitos de Produto)
*   **spec.md**: Specification Markdown file (Arquivo Markdown de Especificação)
*   **plan.md**: Plan Markdown file (Arquivo Markdown de Plano)
*   **contract.md**: Contract Markdown file (Arquivo Markdown de Contrato)
*   **CLI**: Command Line Interface (Interface de Linha de Comando)
*   **eval report**: Evaluation Report (Relatório de Avaliação)
*   **PRDProgress.json**: Product Requirements Document Progress JSON file (Arquivo JSON de Progresso do Documento de Requisitos de Produto)

**Resumo**
A aula aborda a automatização da validação de funcionalidades desenvolvidas por meio de uma ferramenta chamada "evaluator". O objetivo é demonstrar como essa ferramenta utiliza os artefatos de fluxos anteriores, como `spec.md`, `plan.md` e `contract.md`, para verificar a entrega de uma feature.

A principal inovação é a capacidade do evaluator de inferir o contrato correto mesmo que a entrada seja apenas o ID da feature (ex: `feature F01`) ou o `PRD`, eliminando a necessidade de informar o caminho exato do `contract.md`. Essa flexibilidade reduz o atrito operacional sem comprometer o alinhamento com a especificação.

A avaliação é realizada em duas camadas complementares:
1.  **Quality Gates**: Verificações objetivas já configuradas no fluxo do projeto.
2.  **Playwright CLI**: Execução de validações de interface do usuário, incluindo captura de screenshots e comparação de resultados, gerando evidências visuais além de logs textuais.

O processo gera um "eval report" que detalha o que foi executado, o que passou, o que falhou e o que é considerado "indeterminate". O status "indeterminate" ocorre quando a automação não encontra falhas objetivas, mas também não consegue afirmar conformidade total sem julgamento humano (ex: critérios visuais ou subjetivos), marcando uma pendência manual e preservando a rastreabilidade.

O `PRDProgress.json` é atualizado para refletir o progresso das features. O status `implemented` indica que a feature foi entregue do ponto de vista de codificação, mas a validação final pode estar pendente. O status `done` só é atribuído quando a validação está completa, incluindo as etapas manuais, e é acompanhado pelo link do "eval report" como evidência persistida, transformando o arquivo de progresso em um índice auditável de entregas.

**Pontos de atenção**
*   **Flexibilidade e inferência de contrato**: A capacidade do evaluator de inferir o `contract.md` a partir do `PRD` ou do ID da feature reduz o atrito operacional, mas a rastreabilidade e o vínculo com a especificação são mantidos.
*   **Validação em duas camadas**: A combinação de Quality Gates objetivos e validações de UI com Playwright CLI (incluindo screenshots) oferece um conjunto de evidências mais robusto e completo para a avaliação.
*   **Status "indeterminate"**: É crucial para não aprovar automaticamente critérios que dependem de percepção visual ou análise subjetiva. Isso garante que a rastreabilidade seja mantida e que a aprovação final seja consciente, não artificial.
*   **Relatório como artefato persistido**: O "eval report" não é apenas para consulta; ele serve como evidência gravada da avaliação, essencial para auditorias, revisões futuras e para evitar decisões baseadas apenas na memória.
*   **Distinção entre "implemented" e "done"**: É fundamental diferenciar o estado de "implementado" (código entregue) do estado de "concluído" (validação e aceitação final), que inclui etapas manuais se necessário.
*   **Tracking auditável**: Anexar o link do "eval report" ao status "done" no `PRDProgress.json` é uma boa prática para transformar o progresso em um índice auditável, fornecendo prova da validação realizada.