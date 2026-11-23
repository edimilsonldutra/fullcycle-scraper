Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17801)

## Resumo da aula

Em desenvolvimento paralelo com worktree, a implementação pode estar correta e ainda assim falhar na integração com a main. O ponto crítico não é apenas “funciona no branch”, mas “continua funcionando depois de incorporar mudanças concorrentes”. Por isso, a checagem de conflitos deve acontecer antes da criação da pull request, junto com uma nova validação dos critérios de aceitação. Essa etapa reduz o risco de abrir uma PR que já nasce inconsistente com o estado atual do repositório.

Conflito não surge apenas quando duas mudanças removem ou alteram a mesma linha; ele também aparece quando duas features adicionam estruturas diferentes no mesmo ponto do código. Retomando o cenário de integração entre features, uma branch adicionou colunas de preferência enquanto outra incluiu VideoEvents e helpers de repositório. Nesse caso, resolver o conflito significa preservar as duas intenções de negócio, não escolher arbitrariamente uma delas. Em arquivos estruturais como o schema do Prisma, isso exige revisar o resultado final para garantir que o modelo consolidado continue coerente.

Resolver conflito corretamente não é só apagar marcadores de merge; é manter comportamentos que já haviam sido incorporados por outra feature. Quando elementos como getViewWithPipelineRelations são preservados, a resolução respeita integrações anteriores e evita regressões silenciosas. Isso é especialmente importante em pontos compartilhados, como tabelas, schemas e funções de acesso a dados. O merge só está correto quando o branch resultante continua representando a soma das capacidades das duas linhas de trabalho.

Depois de consolidar mudanças estruturais, o projeto pode passar a exigir dependências que antes não existiam naquele branch. Foi o que ocorreu com pacotes ligados a Postgres e OpenAI, trazidos pela integração com a feature de background processing. Esse efeito é normal em merges entre features que evoluíram em paralelo, porque o branch local herda novos requisitos de build, runtime e geração de artefatos. Por isso, a resolução de conflitos inclui regenerar arquivos derivados e instalar dependências recém-introduzidas.

O merge precisa ser seguido por validações objetivas, como type check, geração de artefatos e testes pós-merge. Essa revalidação confirma que a união das branches continua compilando, que o banco suporta as novas tabelas e que o sistema não quebrou em pontos não cobertos pela inspeção manual. Lembra da política de verificação final já estabelecida: aqui ela é aplicada ao estado integrado, não ao branch isolado. Um branch aprovado antes do merge pode falhar depois dele, então a validação precisa ser refeita.

Critério de aceitação não é propriedade da implementação isolada; ele precisa continuar válido depois da integração com a main. Por isso, abrir a aplicação no browser e reexecutar o fluxo funcional continua sendo necessário mesmo após testes automatizados limpos. O objetivo é confirmar que a UI renderiza, que as rotas continuam operacionais e que o comportamento esperado ainda aparece no sistema consolidado. Em desenvolvimento paralelo, a evidência relevante é sempre a do branch já reconciliado com o restante do projeto.

Uma execução com status failed nem sempre indica defeito de implementação; ela pode representar um comportamento correto diante de uma pré-condição ausente. Quando o pipeline tenta processar sem OpenAI API key, a falha é esperada porque o branch mergeado não recebeu essa configuração. A interpretação correta aqui depende do contexto operacional: o sistema falhou por falta de credencial, não por regressão lógica introduzida no merge. Registrar isso evita confundir limitação de ambiente com bug de código.

A pull request gerada após o merge resolvido precisa refletir o estado final já reconciliado com a main. Isso inclui escopo da mudança, impactos em persistência, server-side, UI, rotas, testes executados, conflitos resolvidos e commits produzidos no processo. Esse registro transforma a PR em trilha auditável da integração, não apenas da implementação original. Só depois dessa consolidação faz sentido fazer merge na main e remover a branch.

## Transcrição

00:01

Bom, pessoal, o seguinte, ele implementou e realmente, cara,

00:05

ele conseguiu fazer, fez o upload, mostrou o vídeo aparecendo,

00:08

pegou o thumbnail e tudo mais. Mas agora, o que eu quero é,

00:13

se eu for criar uma pull request,

00:15

eu provavelmente, eu acredito de uma forma bem forte, que possa ser que eu tenha,

00:21

que eu possa ter conflitos. Então, eu vou colocar o seguinte,

00:25

verifique se tem conflitos com o main.

00:30

Antes de eu criar a PR.

00:35

Caso tenha, corrija e

00:40

garanta que

00:43

os critérios de aceitação estejam funcionando.

00:48

Vou colocar aqui para mim. Lembrando, pessoal,

00:51

poderia estar criando uma nova sessão aqui e seria super recomendável, inclusive,

00:56

principalmente por conta de janela de contexto.

00:58

Eu estou com uma janela de contexto enorme aqui,

01:00

então estou trabalhando dentro da mesma sessão.

01:03

A gente vai focar muito mais em compactação,

01:07

janela de contexto e coisas desse tipo na parte de harness,

01:10

que ali a gente vai ter que ser muito mais estrito em diversas partes.

01:14

Então vou dar um enter aqui para mim e

01:17

vamos ver esse pensamento dele,

01:20

onde ele vai verificar se tem conflito em relação ao main. Então,

01:26

apesar de que um tem a parte de background,

01:30

o outro é em relação a...

01:34

Library. Não sei quantos arquivos esses caras compartilham

01:37

em comum pra eles encontrarem conflitos, né?

01:40

Mas eu acredito que vai ter conflito porque ele fez uma correção

01:43

de uma feature 2 ali em relação à parte de cookies,

01:47

né? Então,

01:48

ele tá pensando aqui, rodando, e agora ele vai começar a comparar o branch ali,

01:54

o orange man com o branch que a gente tá dentro

01:58

dessa nossa work tree aqui e verificar se ele encontrou algum conflito.

02:05

E olha aqui, ele andou, dois conflitos,

02:08

são ambos de adições paralelas, eu adicionei colunas de preferência,

02:12

e a Feature Set adicionou Video Events com Helpers de repositório,

02:18

eu vou resolver mantendo as duas adições.

02:21

Então agora ele vai mexer no esquema do Prisma aqui para a gente.

02:25

Então vamos lá que agora dá -lhe ele resolver conflitos,

02:30

se você olhar aqui eu não consigo nem criar uma PR mais aqui para a gente.

02:34

Então, o repositório está preservado e

02:38

a parte do getViewWithPipelineRelations também está preservada.

02:43

Ou seja, ele manteve daquela feature de background,

02:46

porque provavelmente teve alteração dentro de uma mesma tabela,

02:53

dentro de um mesmo esquema,

02:54

provavelmente ali. Então, ele está verificando se tem mais conflito e etc.

03:00

E vamos lá, vamos aguardar esse cara trabalhar.

03:07

Bom... Ele arrumou o conflito aqui e agora falou que

03:11

não tem mais conflito e agora ele vai,

03:14

como se diz, verificar, está gerando os arquivos de novo e

03:21

ele falou que foi adicionado também as dependências

03:24

Do Postgres e da OpenAI que ele precisa instalar, ou seja, que ele não tinha antes.

03:31

Provavelmente agora ele tem que fazer novas

03:33

instalações para pacotes que não existiam.

03:36

Na video library porque o background,

03:39

Aquela feature background provavelmente instalou a lib

03:43

da OpenAI para conseguir trabalhar,

03:45

Então agora ele está fazendo essas instalações, vamos aguardando aí galera, e

03:53

Agora ele falou que o type check está limpo e que está tudo ok que o banco

03:58

de dados agora está pronto para entrar novas tabelas e agora ele vai rodar ali os

04:04

testes post-merge, ou seja, porque ele já fez, vamos dizer ali,

04:09

um merge em tudo que ele tinha feito para que

04:11

ele possa testar aí no meio da história.

04:16

E agora ele falou que vai fazer o restante dos testes, só para você saber,

04:21

eu estou dando pausa e continuando para a gente não ficar um tempão esperando,

04:24

mas ele abriu a aplicação agora,

04:26

entrou lá no browser e ele está verificando se

04:29

os critérios de aceitação ainda ali funcionam.

04:35

Aparentemente, a aplicação entrou e ele está verificando

04:39

se aqueles critérios de aceitação ainda estão passando.

04:42

Então, é interessante porque ele tinha rodado internamente e agora tudo renderizou.

04:49

E o vídeo agora mostra o status failed porque

04:52

o pipeline 07 mergeado tentou processar sem a OpenAI key,

04:57

comportamento correto, porque...

05:01

Esse branch específico, na hora que ele deu o merge,

05:04

ele realmente não tem a API key da OpenAI.

05:08

Então, esse aí é um ponto importante para a gente colocar,

05:12

mas ele não teria mesmo, porque eu não coloquei,

05:15

ele acabou de fazer o merge. Então, esse aí é um ponto importante. Então,

05:19

esse aí é uma coisa que impede para que ele continue trabalhando.

05:25

Mas ele colocou quais os conflitos que ele encontrou e...

05:29

as dependências, o que ele fez e tudo mais,

05:31

e beleza. Então, bom, ele rolou essa parada,

05:37

então eu vou aqui e vou pedir para ele dar um create, uma pull request para mim, vai

05:49

verificar se tem coisa que não está comitada, está

06:07

verificando, e

06:10

finalmente ele gerou a pull request, então eu vou clicar aqui,

06:13

apareceu a minha pull request, com escopo, persistência, server side,

06:19

a UI, as rotas, os testes que ele fez,

06:23

mudanças que ele teve, ele falou aquela parada do cookie,

06:27

o merge que ele teve que fazer ali com a

06:30

main para conseguir resolver os conflitos e o plano de teste,

06:35

aqui caso eu vá fazer isso aí manual,

06:37

trouxe os commits e eu vou dar um merge aqui para a nossa main e

06:44

eu vou dar aqui um delete branch agora aqui, beleza? Feito isso aqui,

06:51

essa etapa aqui está concluída.

06:57

Próximo vídeo a gente vê como é que fica

06:59

o nosso outro processo do painel de administração do usuário. Vamos nessa.

## Resumo IA

**Abreviações**
*   **PR**: Pull Request
*   **UI**: User Interface
*   **API**: Application Programming Interface

**Resumo**
O objetivo central da aula é reforçar a importância da verificação de conflitos e da revalidação rigorosa em cenários de desenvolvimento paralelo com `worktree`, tanto antes da criação de uma Pull Request (PR) quanto após a resolução de conflitos. A premissa é que o sucesso de uma feature não se limita ao seu funcionamento em um branch isolado, mas à sua capacidade de integrar-se e manter a funcionalidade após incorporar mudanças concorrentes da `main`.

A aula abordou a resolução de conflitos, destacando que esta não significa apenas remover marcadores de merge, mas sim preservar as intenções de negócio de todas as features, como exemplificado pela integração de colunas de preferência e elementos como `VideoEvents` e helpers de repositório. Nesses casos, a revisão de arquivos estruturais, como o schema do Prisma, é crucial para garantir a coerência do modelo consolidado. Foi enfatizado que merges podem introduzir novas dependências (ex: pacotes para Postgres e OpenAI) e requisitos de build/runtime, exigindo a instalação dessas dependências e a regeneração de arquivos derivados.

O fluxo explicado pelo instrutor detalha os seguintes passos: (1) Verificar e corrigir conflitos com a `main` *antes* de criar a PR; (2) Garantir que os critérios de aceitação continuam válidos após a resolução dos conflitos; (3) Realizar validações objetivas pós-merge, incluindo `type check`, geração de artefatos e testes automatizados; (4) Executar uma revalidação funcional abrindo a aplicação no browser para confirmar UI, rotas e comportamento esperado no sistema consolidado; (5) Interpretar corretamente falhas, distinguindo entre limitações de ambiente (e.g., falta de OpenAI API key) e bugs de código; e (6) Gerar uma PR abrangente que documente o estado final reconciliado, incluindo escopo, impactos, testes, conflitos resolvidos e commits, antes de fazer o merge na `main` e excluir o branch.

**Pontos de atenção**
*   **Validação Pré-PR Essencial:** Sempre verifique a existência de conflitos com a `main` e revalide *todos* os critérios de aceitação *antes* de criar uma Pull Request. Isso é crítico para evitar submeter uma PR que já nasce inconsistente com o estado atual do repositório.
*   **Resolução de Conflitos Abrangente:** A resolução de conflitos deve preservar *ambas* as intenções de negócio das features concorrentes, e não escolher arbitrariamente uma delas. Isso é vital para arquivos estruturais, como schemas de banco de dados e funções de acesso a dados compartilhadas.
*   **Preservar Comportamentos Integrados:** Não basta apenas apagar marcadores de merge. Garanta que elementos e comportamentos já incorporados por outras features (e.g., `getViewWithPipelineRelations`) sejam mantidos para evitar regressões silenciosas no sistema consolidado.
*   **Expectativa de Novas Dependências Pós-Merge:** É normal que o merge de features em paralelo introduza novas dependências (e.g., pacotes de Postgres, OpenAI) e requisitos de build ou runtime. A resolução de conflitos inclui a instalação dessas dependências recém-introduzidas e a regeneração de arquivos derivados.
*   **Revalidação Pós-Merge Obrigatória:** Um branch aprovado isoladamente pode falhar após o merge. É mandatório realizar validações objetivas (type check, geração de artefatos, testes pós-merge) no estado integrado para confirmar que o sistema continua compilando e funcionando.
*   **Testes Funcionais Manuais Críticos:** Mesmo após testes automatizados passarem, abra a aplicação no browser e reexecute o fluxo funcional. Isso confirma que a UI renderiza, as rotas estão operacionais e os critérios de aceitação permanecem válidos no sistema reconciliado.
*   **Contextualização de Falhas:** Uma falha (e.g., `status failed`) nem sempre indica um defeito de implementação. Pode ser um comportamento correto diante de uma pré-condição ausente (ex: falta de uma API key). Documente o contexto para evitar confundir limitações de ambiente com bugs de código.
*   **PR como Trilha Auditável da Integração:** A Pull Request final deve ser um registro completo e auditable da *integração*, não apenas da implementação original. Inclua escopo, impactos (persistência, server-side, UI, rotas), todos os testes executados, detalhes dos conflitos resolvidos e os commits gerados durante o processo.