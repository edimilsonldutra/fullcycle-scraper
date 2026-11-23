Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17788)

## Resumo da aula

Encerrar uma feature não termina no código implementado; é preciso consolidar o estado do repositório com commit, push, abertura da pull request, merge e limpeza controlada do branch. Esse fechamento cria um ponto estável antes da próxima etapa e reduz o risco de carregar mudanças intermediárias para o fluxo seguinte. A limpeza, porém, exige precisão: remover “o outro branch local” de forma genérica é perigoso quando existem múltiplos branches ativos no repositório. O procedimento seguro é voltar para main, executar pull, confirmar que o merge foi concluído e deletar explicitamente apenas o branch correto.

Quando a sessão do agente é reiniciada ou limpa, parte do contexto operacional pode se perder, mesmo que ações anteriores tenham sido executadas. Isso afeta especialmente o registro do test plan, porque o sistema pode passar a reportar que nada foi rodado, apesar de a execução ter ocorrido em uma sessão anterior. A consequência prática é que o histórico visível da automação nem sempre representa todo o trabalho já feito. Por isso, ao revisar uma PR, é importante distinguir ausência de evidência na sessão atual de ausência real de validação.

Retomando o uso de Playwright e E2E já visto antes, nem todo artefato gerado pelo agente deve permanecer no branch. Se o agente cria uma pasta E2E e testes automatizados sem que isso faça parte do objetivo imediato da entrega, esses arquivos aumentam escopo, ruído de diff e custo de revisão. Remover esse conteúdo é uma decisão de controle de fronteira da feature, não de rejeição à automação. Em SDD, manter apenas o que pertence ao objetivo atual melhora previsibilidade e facilita composições futuras.

A feature 3, de video upload, é tratada como uma feature central porque habilita capacidades que destravam etapas posteriores do produto. Mesmo depois de concluir as features 1 e 2, ela não entra apenas como mais uma entrega sequencial; ela funciona como dependência para uma nova fase de execução. Quando uma feature tem esse papel estrutural, faz sentido implementá-la isoladamente para estabilizar contratos, fluxos e dependências antes de paralelizar o restante. Isso reduz bloqueios cruzados entre branches futuros.

A leitura das dependências no PRD define quando uma feature pode ser desenvolvida sozinha e quando várias podem avançar em paralelo. Aqui, a estratégia é concluir a feature 3 primeiro para que a Wave 3 possa ser executada com múltiplas frentes simultâneas. Desenvolvimento paralelo só funciona bem quando as dependências anteriores já foram resolvidas e o ponto de integração está claro. Em outras palavras, SDD não serve apenas para implementar uma feature com agente; serve para reorganizar o fluxo de entrega em unidades independentes e paralelizáveis.

Até aqui, o fluxo vinha do desenvolvimento de uma feature por vez, com branch, validação e PR. O avanço novo está em usar a especificação não apenas para orientar uma implementação isolada, mas para preparar um pipeline de execução paralela entre features. Isso muda o papel da especificação: ela deixa de ser só instrução de construção e passa a ser mecanismo de coordenação entre frentes de trabalho. O ganho esperado é throughput maior sem perder controle de escopo e dependências.

## Transcrição

00:00

Bom, pessoal, voltando no nosso projeto aqui, olha só, eu vi que o Cursor,

00:06

Naquela hora, ele criou uma pasta 2E, né?

00:09

E ele criou vários testes chamando e tentando

00:14

Fazer a pegada para rodar com o Playwright,

00:17

Tá? Eu vou apagar esse cara aqui porque não é o meu objetivo.

00:20

E o que eu vou fazer agora aqui vai ser, eu vou dar um commit, push PR, para

00:28

Ele subir o...

00:31

Essas nossas alterações e também pra que a gente consiga fazer o pull request,

00:38

Jogar isso aí pra mim,

00:39

Pra gente ir pra nossa terceira feature, tá? Então,

00:43

Vamos nessa, vamos ver esse cara fazendo isso.

00:51

Bom, ele gerou a nossa pull request aqui.

00:54

Então, deixa eu pedir pra esse cara abrir. Apareceu.

01:01

Como na sessão atual que eu estava, né?

01:07

Eu apaguei a pasta E2Z e ele não tinha rodado aqueles planos de teste,

01:12

Né? Porque eu mudei de sessão, eu tinha dado um clear.

01:15

Ele está dizendo que eu não fiz nada no test plan, mas ele tinha rodado,

01:19

A gente sabe disso. Vou rodar esse cara aqui,

01:22

Estou dando merge, deletando aqui meu branch, tá?

01:28

Vou pedir aqui para ele voltar para o git checkout main e

01:35

Eu vou colocar pedir para ele dar um pull.

01:40

Aqui para mim, já está up to date,

01:44

Remova o outro branch local.

01:49

Que perigo escrever dessa forma, né?

01:51

Se você tiver vários outros branches locais,

01:54

Que nesse caso é o branch do Authentication System ali para a gente,

01:59

Né? Então, tomar cuidado com isso aí, mas beleza,

02:02

Ele deletou e eu só tenho a PR2 com o branch remoto, né? Está lá intacto.

02:10

Agora, a questão é o seguinte, galera.

02:13

Terminamos mais uma fase. Agora,

02:15

O que a gente tem ali no meio de toda essa história aqui, tá?

02:22

Que é o seguinte.

02:24

Uma das coisas... Opa, espera um pouquinho.

02:28

A minha pull request que eu fiz e eu pedi pra ele deletar o branch,

02:32

Deixa eu só ver, eu acho que eu fiz uma besteira.

02:35

Não, não fiz besteira, não. Era um atualizar aqui,

02:38

Porque tinha subido a minha especificação.

02:41

Então, galera, só pra gente entender qual que vai ser o nosso próximo plano aqui.

02:47

Eu vou fazer a geração, tá? Da feature número 3.

02:50

E se você olhar a feature número 3, tá?

02:54

Deixa eu abrir o nosso PRD.

02:56

Somente pra você entender que pé que a gente tá do nosso projeto aqui. Deixa eu abrir aqui.

03:06

A gente fez a feature 1, 2.

03:10

E a gente tem aqui a nossa feature 3, que é o vídeo upload, tá?

03:14

Essa feature é uma das features, obviamente, principais,

03:17

Porque a gente vai poder fazer o upload ali do nosso vídeo.

03:22

Deixa eu... Caramba, ela tá... A feature pra caramba aqui.

03:27

Vamos lá. Aqui as dependências. Aqui que eu queria chegar.

03:31

Então, o que acontece aqui?

03:33

Eu fiz a feature 2, fiz a feature 1.

03:36

Aí eu tenho a feature 3, que ela tem que ser feita isolada. Então, a gente vai...

03:40

Eu vou desenvolver essa feature aqui, eu não vou ficar gastando tempo, o seu tempo,

03:43

vendo eu desenvolver uma nova feature. Ou seja,

03:46

eu vou pegar, vou pedir para ela desenvolver,

03:47

para essa feature ficar pronta. Porque quando a gente chegar aqui, nessa Wave 3 aqui,

03:54

a gente vai poder fazer esses caras de forma simultânea.

03:57

E é esse que é o objetivo que eu queria trazer aqui.

04:00

Para você sair do ponto de desenvolver uma feature,

04:03

e fazer com que a gente consiga trabalhar em desenvolvimento paralelo,

04:07

basicamente... ali utilizando a SDD, fechou?

04:13

Então deixa eu parar o vídeo, fazer a feature número 3, e daí a gente volta aí.

## Resumo IA

**Abreviações**
*   PR: Pull Request
*   E2E: End-to-End (teste)
*   SDD: Specification-Driven Development
*   PRD: Product Requirements Document

**Resumo**
A aula aborda a etapa final do ciclo de desenvolvimento de uma feature, enfatizando que o processo não se encerra na implementação do código. O objetivo principal é consolidar o estado do repositório através de `commit`, `push`, abertura de `Pull Request` (PR), `merge` e a limpeza controlada do branch. Essa sequência visa criar um ponto estável no projeto e minimizar o risco de introduzir mudanças intermediárias em fases subsequentes.

Durante a demonstração, o instrutor removeu artefatos (como a pasta `E2E` e testes do Playwright) gerados por um agente (Cursor) que não faziam parte do escopo imediato da feature, destacando a importância de controlar o conteúdo para evitar ruído e aumento de escopo. Foi discutido como a reinicialização ou limpeza de uma sessão de agente pode resultar na perda de contexto operacional, afetando o registro do `test plan` e levando a relatórios que indicam que nada foi executado, mesmo que a validação tenha ocorrido.

A aula também marcou a transição do desenvolvimento de features isoladas para a preparação de um pipeline de execução paralela. A Feature 3 (upload de vídeo) foi identificada como uma feature "central" ou "estrutural", que precisa ser implementada isoladamente para estabilizar contratos, fluxos e dependências, destravando etapas futuras do produto. O Product Requirements Document (PRD) é usado para definir as dependências e estratégias de desenvolvimento, permitindo que a "Wave 3" do projeto seja executada com múltiplas frentes simultâneas. O instrutor ressalta que o Specification-Driven Development (SDD) é fundamental para organizar o fluxo de entrega em unidades independentes e paralelizáveis, transformando a especificação de uma simples instrução de construção em um mecanismo de coordenação entre as equipes.

**Pontos de atenção**
*   **Limpeza segura de branches**: Remover branches locais de forma genérica é perigoso se houver múltiplos branches ativos. O procedimento correto envolve voltar para a branch `main`, executar um `pull`, confirmar que o `merge` foi concluído e, em seguida, deletar explicitamente apenas o branch correto.
*   **Contexto de sessão do agente**: Tenha em mente que a reinicialização ou limpeza da sessão de um agente pode causar a perda de contexto operacional, levando a um registro impreciso do `test plan`. Ao revisar uma PR, é crucial distinguir entre a ausência de evidência na sessão atual e a ausência real de validação.
*   **Controle de artefatos indesejados**: Evite manter artefatos gerados automaticamente por agentes (como pastas `E2E` ou testes automatizados) se não forem parte do objetivo imediato da feature. Isso é uma boa prática para controle de fronteira da feature, minimizando aumento de escopo, ruído de `diff` e custo de revisão.
*   **Priorização de features estruturais**: Features que habilitam capacidades críticas ou destravam etapas posteriores do produto devem ser implementadas isoladamente primeiro. Isso ajuda a estabilizar contratos, fluxos e dependências, reduzindo bloqueios cruzados entre branches futuros e facilitando a paralelização posterior.
*   **Pré-requisitos para desenvolvimento paralelo**: O desenvolvimento paralelo de features só é eficaz quando as dependências anteriores foram resolvidas e o ponto de integração está claramente definido.
*   **Papel da especificação**: A especificação (PRD) não deve ser apenas uma instrução para a implementação individual de uma feature, mas também um mecanismo de coordenação para preparar um pipeline de execução paralela entre diferentes frentes de trabalho. Isso visa aumentar o `throughput` (vazão) sem perder o controle de escopo e dependências.