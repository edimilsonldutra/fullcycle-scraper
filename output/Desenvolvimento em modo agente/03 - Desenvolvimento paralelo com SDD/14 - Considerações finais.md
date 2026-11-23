Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17802)

## Resumo da aula

Quando uma branch ainda não foi consumida por outras pessoas, rebase tende a ser a opção mais simples para integrar mudanças recentes da main ou de features já concluídas. Ele reaplica os commits da feature sobre a base mais atual, deixando o histórico mais linear e reduzindo o ruído de merges intermediários. Aqui, a escolha faz sentido porque as features 04 e 07 já estavam integradas e não havia risco de reescrever commits compartilhados com terceiros.

Desenvolvimento paralelo acelera entrega, mas aumenta a frequência de conflitos porque várias branches evoluem sobre os mesmos arquivos e contratos. Isso não é um defeito do processo; é uma consequência natural de elevar o throughput do time ou dos agentes. O ponto operacional importante é assumir que conflito faz parte do fluxo e tratá-lo como etapa prevista da integração, não como exceção.

Retomando as integrações já discutidas, os conflitos finais apareceram em áreas sensíveis como Prisma e setup de testes E2E. Esses pontos concentram colisões porque várias features podem alterar schema, arquivos gerados, preferências persistidas ou infraestrutura de teste ao mesmo tempo. Já arquivos que não tiveram sobreposição real, como storage.ts, podem passar por auto-merge limpo sem intervenção manual.

Depois de resolver conflitos em Prisma, não basta ajustar o texto dos arquivos versionados; é necessário regenerar os artefatos derivados e reexecutar migrações quando aplicável. Isso garante que o estado do código gerado volte a refletir o schema consolidado após a integração. Sem essa etapa, a branch pode compilar localmente de forma inconsistente ou falhar em testes e validações posteriores.

Resolver conflito não encerra o trabalho; a integração só fica confiável depois de rodar novamente os testes relevantes. O rebase pode introduzir incompatibilidades sutis entre mudanças que, isoladamente, estavam corretas. Por isso, repetir testes após a atualização da base é a verificação mínima para confirmar que a feature continua válida no estado atual do projeto.

O painel administrativo não chegou apenas com código funcional; ele também revelou desvios e problemas reais do ecossistema, como bugs, wrappers adicionados, banner de concorrência, uso de getSession, preservação de launch.json versionado e correção de configuração do Playwright para usar APP_PORT em vez de fixar a porta 3000. Esse tipo de achado é valioso porque mostra que a implementação de uma feature frequentemente expõe fragilidades transversais do projeto. Em desenvolvimento orientado por especificação, esses desvios precisam aparecer explicitamente na pull request para que a integração seja auditável.

A pull request consolida o plano executado, os desvios assumidos, o rebase realizado e o estado final validado da feature. Ela não serve apenas para pedir merge; funciona como registro operacional do que foi implementado e do que precisou ser ajustado para integrar com o restante do sistema. Depois do merge, deletar a branch encerra o ciclo e evita manter work in progress já incorporado à linha principal.

A especificação acelera geração de código e permite executar várias features em paralelo, mas não elimina a necessidade de governança sobre a IA. Quando o mesmo agente implementa e testa o próprio trabalho, a validação perde independência e tende a ser menos confiável. O próximo nível de maturidade é combinar especificação, código e harness externo para controlar melhor contexto, revisão cruzada e qualidade da entrega.

## Transcrição

00:00

Bom, pessoal, e agora voltamos aqui à nossa última feature que

00:05

a gente pediu para ele entregar em paralelo,

00:07

que é o painel administrativo.

00:09

Ele fez, testou aqui, trouxe e fez,

00:13

mostrou para a gente os critérios de aceitação, cross-feature integration,

00:18

desvios que ele fez, ele adicionou wrappers,

00:22

banner de concorrência pela página,

00:25

encontrou três bugs, inclusive viu aquela história do get session.

00:29

Provavelmente a gente vai ter que ajustar essa parte de conflito.

00:32

Viu que o launch.json tava versionado, não mexeu.

00:36

Achou alguma coisa, se eu não me engano, no Playwright,

00:39

onde ele tava forçado à porta 3000, ele mandou pegar da porta app port,

00:46

por padrão. Então, em tese, ele terminou aqui.

00:49

Mas agora eu vou fazer a mesma coisa, né?

00:52

Verifique conflitos com o main para fazermos o que aqui. Origin,

01:04

para criarmos uma pull request.

01:11

E agora, vamos lá, porque provavelmente lá vem conflito aí,

01:16

galera. Então, isso aí é algo que,

01:19

como que eu posso dizer? Conflito existe e sempre existiu,

01:22

e eu acredito que você sempre passou por isso.

01:25

O que eu percebo agora é que, como a gente entrega muito, muito mais rápido,

01:30

e a gente faz muita coisa em paralelo, cada vez mais os conflitos vão aparecendo.

01:35

Então, isso aí é um ponto importante.

01:38

Agora, vamos deixar ele rodar aqui.

01:40

Ele vai tentar fazer um merge com o main e vai

01:42

tentar pegar ali os principais conflitos e eu acho que

01:45

a gente vai passar mais ou menos por todo aquele

01:47

processo que a gente passou antes ali com a feature anterior.

01:53

Ele falou que encontrou dois conflitos ali.

01:57

Um conflito é do Prisma, conteúdo...

02:00

em relação à preferência de visualização da biblioteca,

02:03

com o Last Login, E2Z Global Setup, onde

02:10

ele criou uma parte para testes E2Z,

02:13

e Auto Merge Limpo sem intervenção do Storage.ts,

02:16

que vem também dos outros contextos, nenhum toca nos caminhos,

02:20

próximos passos, opções aqui, vou colocar,

02:25

corrija os conflitos para darmos...

02:31

Merge. Eu vou botar para ele fazer merge mesmo, ao invés dele querer fazer rebase.

02:37

Ele poderia ter feito um rebase que já estaria resolvido.

02:43

Mas pensando bem, galera, o seguinte,

02:45

nunca ninguém deu pull ou usou esse meu

02:50

branch que eu estou utilizando antes de mim.

02:55

Concordam comigo? E como a feature 04 e 07 já estão implementadas,

03:01

é muito melhor eu partir do princípio que eu

03:04

estou fazendo o rebase em cima dessas features,

03:08

ou do que, como se eu tivesse partido do bem. Então,

03:12

é melhor eu fazer o rebase, fica muito mais fácil,

03:15

a não ser que eu tivesse um risco de outras pessoas,

03:18

que nesse momento eu sei que eu não tenho,

03:19

terem utilizado o meu branch.

03:21

Porque daí teria que sair reescrevendo os commits. Então, na realidade,

03:24

Eu vou falar o seguinte, vou pedir para ele assim, faça o rebase aqui para mim.

03:31

E depois, vou colocar, faço o rebase. Vamos lá.

03:50

Então, agora ele vai pegar o conflito ali do rebase para conseguir fazer o ajuste.

04:01

Prontinho, ele fez o rebase e ele está falando que a

04:04

minha Ocurrity está limpa e que o meu Prisma,

04:08

que ele está fazendo a geração dos arquivos do Prisma novamente,

04:10

rodando as migrações e provavelmente vai rodar os testes novamente,

04:14

que foi aquilo que eu pedi lá naquele Cloud MD.

04:17

Mas assim fica muito mais linear os

04:20

nossos merges na main com o rebase. Então,

04:25

nesse caso, faz mais sentido para a gente.

04:27

Então, vamos aguardar esse cara fazer isso.

04:31

E agora, ele falou que fez o rebase, rodou os testes aqui,

04:36

fez os testes que ele queria. E agora,

04:38

eu vou dar um commit com o push .pr para ele fazer

04:44

o push para mim e gerar a pull request que eu estou querendo.

04:48

E vamos lá, galera.

04:50

Temos três features que a gente conseguiu fazer ali de forma paralela.

04:54

Eu não sei se vocês perceberam,

04:55

mas como que a gente chega com um nível de, como que eu posso dizer,

05:02

com um poder muito maior nesses aspectos quando nós estamos,

05:06

como que eu posso dizer, rodando as coisas em paralelo.

05:11

A gente poupa muito tempo e tudo isso baseado em uma especificação.

05:17

Mas é aquilo que eu te falei, não tem mágica, você vai ter conflito,

05:21

vai encontrar erro, você vai ter que continuar testando e etc.

05:25

Obviamente, o nosso objetivo aqui nesse curso não é que você...

05:30

a gente desenvolva um software e a gente fique vendo os detalhes de implementação,

05:36

da qualidade, isso acaba entrando numa outra seara.

05:40

Nosso principal ponto nesses capítulos aqui é entender

05:43

como fazer uma especificação gerar código.

05:46

Depois a gente vai entender como que com uma especificação e

05:50

com código e com harness que não seja apenas do nosso agente,

05:54

sei lá, do Cloud Code,

05:56

do Codex e etc., a gente consiga, de forma geral,

06:00

colocar essas rédeas aí na nossa IA.

06:07

Conseguir controlar melhor a janela de contexto,

06:09

fazer um agente revisar o trabalho do outro,

06:12

porque o próprio agente que desenvolveu está fazendo o próprio teste.

06:16

Isso aí é algo que não funciona na maioria das vezes,

06:20

como posso dizer, não é algo tão confiável aí nesses casos.

06:24

Então ele criou aqui a minha pull request,

06:29

botou tudo o que ele fez, o plano, falou que inclusive fez o rebase e etc.

06:34

E eu vou dar um merge na minha pull request, vou

06:40

dar um delete aqui no meu branch. E aí galera,

06:44

finalmente a gente terminou essa Wave

06:49

3 do desenvolvimento das nossas features. Então,

06:54

no próximo vídeo eu quero trazer alguns

06:58

outros esclarecimentos que eu acredito que são importantes.

## Resumo IA

**Abreviações**
*   **E2E**: End-to-End (testes de ponta a ponta)
*   **PR**: Pull Request (solicitação de incorporação de código)
*   **IA**: Inteligência Artificial

**Resumo**
Esta aula teve como objetivo demonstrar o processo de integração de uma nova feature, o "painel administrativo", desenvolvida em paralelo. O instrutor enfatizou a importância de encarar os conflitos de código como uma etapa natural do fluxo de desenvolvimento, e não como uma exceção, especialmente em contextos de alta velocidade e desenvolvimento paralelo. Foi explicada a escolha estratégica de realizar um rebase em vez de um merge para integrar as mudanças da main, dada a característica de que a branch de feature não havia sido consumida por outras pessoas e que features anteriores (04 e 07) já estavam integradas, o que resulta em um histórico mais linear. Os conflitos encontrados ocorreram em áreas sensíveis como o esquema do Prisma e a configuração de testes E2E (Playwright), enquanto arquivos como `storage.ts` foram auto-mesclados. Após a resolução dos conflitos, o fluxo detalhou a necessidade de regenerar artefatos derivados do Prisma e reexecutar as migrações e todos os testes relevantes para garantir a consistência e a validade da feature no estado atualizado do projeto. A aula também destacou que a implementação de features frequentemente revela desvios e problemas transversais no projeto, como bugs ou configurações inconsistentes (ex: `launch.json` versionado, Playwright usando porta fixa). Por fim, o instrutor demonstrou a criação de uma Pull Request, enfatizando seu papel como um registro operacional auditável das implementações, desvios e validações, finalizando o ciclo com o merge e a exclusão da branch. A importância da governança sobre a IA no processo de desenvolvimento foi mencionada, ressaltando que a validação do código não deve ser realizada apenas pelo agente que o desenvolveu.

**Pontos de atenção**
*   **Conflitos como parte do fluxo**: Assuma que conflitos são uma consequência natural do desenvolvimento paralelo e de times de alto throughput, tratando-os como uma etapa prevista da integração, não como uma exceção ou defeito.
*   **Resolução de conflitos no Prisma**: Após ajustar o texto dos arquivos versionados no Prisma, é crucial regenerar os artefatos derivados e reexecutar migrações, se aplicável, para garantir que o código gerado reflita o esquema consolidado.
*   **Reexecução de testes pós-integração**: Resolver conflitos ou realizar um rebase não encerra o trabalho. É fundamental rodar novamente os testes relevantes para verificar que a feature continua válida e que o rebase não introduziu incompatibilidades sutis.
*   **Descoberta de problemas transversais**: A implementação de uma nova feature frequentemente expõe fragilidades, bugs, desvios e problemas de configuração em outras áreas do projeto, o que é um achado valioso.
*   **Documentação explícita de desvios**: Em desenvolvimento orientado por especificação, qualquer desvio ou problema encontrado durante a implementação deve ser documentado explicitamente na Pull Request para garantir a auditabilidade da integração.
*   **Propósito da Pull Request (PR)**: A PR vai além de apenas solicitar um merge; ela serve como um registro operacional do que foi implementado, dos ajustes realizados, do rebase efetuado e do estado final validado da feature.
*   **Deleção de branches após o merge**: Deletar a branch de feature após o merge encerra o ciclo de desenvolvimento, evitando a manutenção de "work in progress" já incorporado à linha principal.
*   **Governança e validação de IA**: Embora a especificação acelere a geração de código e o desenvolvimento paralelo, é essencial ter governança sobre a IA. A validação perde independência e confiabilidade quando o mesmo agente que implementa o código também é o único a testá-lo, sendo preferível a revisão cruzada e o uso de harness externo.