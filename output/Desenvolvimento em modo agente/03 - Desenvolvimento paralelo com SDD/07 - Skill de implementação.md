Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17796)

## Resumo da aula

A skill implement padroniza a forma de pedir implementação para um agente sem engessar o processo. Ela recebe o ID da feature, o folder de trabalho e overrides opcionais, que permitem alterar o comportamento padrão para casos específicos. Esse desenho é importante em desenvolvimento paralelo porque reduz ambiguidade entre execuções diferentes e mantém um contrato mínimo de entrada. A flexibilidade fica nos overrides; a consistência fica na estrutura fixa da skill.

Overrides são instruções adicionais que sobrescrevem partes do comportamento padrão da skill. Eles existem para acomodar necessidades locais sem obrigar a criação de um novo comando para cada variação, como pedir uma credencial durante a execução ou mudar a forma de testar uma feature específica. Isso evita que o prompt vire um artefato rígido e pouco reutilizável. Em vez de multiplicar comandos, mantém-se uma base comum com pontos controlados de customização.

Retomando o fluxo de features já definido no capítulo, a implementação começa lendo spec.md, plan.md e prd. Esses arquivos fornecem o contexto funcional, o plano de execução e o enquadramento da feature dentro do sistema, para que o agente não implemente apenas por inferência local do código. A skill também aplica os overrides nessa etapa, o que significa que a interpretação da feature já nasce ajustada às restrições do caso atual. O resultado é uma preparação orientada por documentação antes de qualquer alteração no código.

O Preflight Dependency Check verifica dependências da feature em relação ao que já existe no sistema e às outras features ao redor. Como o capítulo já estabeleceu grafo de dependências, provides e consumes, o ponto novo aqui é usar esse contexto como checagem operacional antes de codificar. Isso aumenta a awareness do agente sobre o ambiente real de execução e reduz implementações que ignoram pré-requisitos. A verificação funciona como uma barreira contra trabalho inconsistente com o estado atual do projeto.

A execução da skill segue um loop: implementar, validar e decidir o próximo passo. A validação inclui o que o ambiente disponibiliza, como linter, type check e testes, sem acoplamento a uma stack única. Se a validação falha, o agente volta a implementar; se passa, ele consolida o progresso e segue para a próxima fase. Esse ciclo transforma qualidade em parte do fluxo de desenvolvimento, não em uma revisão tardia.

Cada grupo de fases concluído deve gerar um commit, em vez de concentrar toda a implementação em uma única alteração grande. Isso preserva o tracking do que funcionou, facilita rollback quando a fase seguinte degrada o resultado e cria marcos intermediários de progresso. Há ainda um efeito importante para agentes: o histórico do Git e os diffs passam a funcionar como memória operacional do que já foi feito. Quando o sistema ainda não mantém estado explícito, o repositório versionado vira a principal fonte de estado recuperável.

Lembra da discussão anterior sobre compartilhamento de estado entre agentes? Aqui, enquanto não existe um mecanismo adicional de estado, o Git cumpre esse papel de forma prática. O agente pode inspecionar commits e diffs para inferir decisões recentes, entender o ponto atual da feature e evitar retrabalho cego. Isso explica por que commits automáticos e lógicos aumentam segurança em vez de apenas poluir o histórico. O versionamento deixa de ser só rastreabilidade humana e passa a ser insumo de execução para o próprio agente.

Depois da implementação, a skill força uma verificação final mais ampla: rodar a suíte inteira de testes e rechecagem dos critérios de aceitação. Essa etapa existe porque passar em validações parciais durante o loop não garante conformidade global da feature. A suíte completa captura regressões fora do escopo imediato da fase atual, e os critérios de aceitação confirmam aderência ao que foi especificado. O fechamento da implementação depende tanto de corretude técnica quanto de alinhamento com o contrato funcional.

O relatório final deve registrar o que foi concluído, o que não foi concluído e quais desvios ocorreram em relação à especificação. Desvio não é apenas erro; é qualquer implementação que atende parcialmente ao objetivo, mas por um caminho diferente do previsto. Tornar esses desvios explícitos é essencial porque pequenas exceções acumuladas degradam a arquitetura ao longo do tempo. Sem esse registro, o sistema se afasta da organização original de forma silenciosa.

Hard fail ocorre quando a execução é bloqueada por uma impossibilidade real, como ausência de chave da OpenAI ou incapacidade de conexão com um CRM externo. Nesses casos, o agente não falha por incompetência de implementação, mas por falta de informação, acesso ou ferramenta necessária para qualquer desenvolvedor concluir a tarefa. Soft fail é diferente: houve impedimento em parte do processo, como uma forma específica de teste que não pôde ser executada, mas a feature ainda conseguiu ser desenvolvida de algum modo. A distinção importa porque separa bloqueios estruturais de limitações contingentes e melhora a qualidade do relatório final.

## Transcrição

00:00

Bom, pessoal, como eu falei para vocês,

00:03

para a gente não começar agora a, não vamos dizer assim,

00:08

avacalhar no nosso prompt,

00:10

para pedir para o nosso agente fazer alguma coisa para a gente,

00:13

principalmente para trabalhar em paralelo,

00:15

eu preciso de pelo menos um mínimo de padronização da forma como eu vou pedir.

00:20

E também um pouco de,

00:22

como que eu posso dizer,

00:24

organização e passos que são importantes na hora que ele vai desenvolver.

00:30

É uma skill muito simples,

00:33

mas ela tem alguns aspectos ali importantes para que você

00:37

consiga ter em mente que a gente fez de forma intencional,

00:42

baseado, vamos dizer, nesse, entre aspas, framework que nós temos.

00:46

Então, ela é chamada de implement, ela vai ser rodada,

00:50

a gente pode rodar ela como um slash command,

00:53

dependendo da plataforma, ou você pode escrever em linguagem natural.

00:57

O grande ponto que ela precisa é o seguinte,

01:00

Ela precisa saber qual é o ID da feature que eu estou desenvolvendo,

01:03

qual é o folder, obviamente, e alguns,

01:07

como eu posso dizer, overrides opcionais. O que significa?

01:13

Significa que eu quis deixar essa feature,

01:15

essa skill, o mais livre possível. Por quê?

01:20

Quando você cria um comando, mais que o nome que você queira chamar,

01:23

um prompt que você vai pegar, copiar e colar,

01:26

muitas vezes isso acaba sendo engessado. Então,

01:30

quando eu coloco overrides opcionais,

01:33

significa que eu posso dar instruções

01:35

adicionais que podem sobrescrever o comportamento padrão. Por exemplo,

01:42

na hora que ele for desenvolver,

01:44

eu quero que ele pare e me pergunte a chave da OpenAI.

01:48

Ah, eu quero que nessa feature, na hora que ele for implementar,

01:51

ele faça os testes de uma outra forma. Então, eu posso pedir algo a mais.

01:57

Então, o que acontece?

01:59

Tem o passo 1 a passo 3, porque você vai ter acesso a esse prompt de qualquer forma,

02:04

a essa skill, mas para a gente não ficar lendo muito aqui,

02:07

depois a gente vai dar uma passada por ela. Mas, basicamente,

02:10

do passo 1 ao 3, ele vai resolver o quê?

02:12

Ele vai falar que... Você vai precisar procurar um arquivo spec.md, um pleno.md,

02:18

ler o arquivo prd,

02:20

entender o contexto do sistema ali e aplicar os overrides, ou seja,

02:25

tudo aquilo que eu falei para ele substituir e poder

02:30

mudar o comportamento na hora que eu queira.

02:33

Aí, o que acontece?

02:35

Tem o outro ponto aqui que é chamado de Preflight, Dependency Check.

02:39

Ele vai olhar ali baseado em todas as dependências que essa feature tem em volta de

02:44

tudo que já foi criado e de todas as

02:46

outras features que existem e coisas desse tipo.

02:48

Então, isso para ele é importante,

02:50

ele ter um pouco mais de awareness do ambiente que ele está rodando.

02:54

E aí, a gente entra na parte realmente de execução.

02:57

Como é que vai funcionar essa fase de execução aqui?

03:01

Vai ser um loop. Então, vai ser assim,

03:02

ele vai implementar o código, aí ele vai cair para a parte de validação.

03:07

Ou seja, ele vai rodar linter,

03:09

type check, vai rodar os testes, ou seja,

03:12

o que nesse caso o nosso ambiente tem para ele conseguir testar.

03:15

Eu não fui um cara extremamente específico porque

03:17

eu não fiquei focando apenas na stack.

03:19

E daí, se der tudo certo,

03:21

ele vai fazer o commit e vai voltar para uma nova fase aqui.

03:27

Obviamente, se não der certo, ele vai implementar novamente.

03:31

Eu não quis deixar esse... esse diagrama cheio de ramificações. Se não der certo,

03:37

volta para essa fase. Se isso, se naquilo e etc.

03:39

Eu não quis deixar isso dessa forma. Mas a ideia é o seguinte,

03:44

que cada fase do desenvolvimento, lembra? A gente tem no nosso plano fase 1,

03:50

o stage 1, que tem ali a parte 1, 2, 3, 4.

03:56

Cada grupo de fases que ele terminar vai ser um commit.

03:59

Isso é muito importante. Por quê?

04:02

Porque muitas vezes ele consegue fazer com muito sucesso uma determinada fase e daí,

04:09

quando ele vai para a próxima,

04:10

aí ela pode fazer besteira.

04:12

E aí você acaba perdendo o tracking do que foi feito

04:15

e também perdendo aquilo que ela fez de bom.

04:19

Uma das coisas que os modelos hoje em dia são cada vez melhores é

04:23

que eles conseguem olhar o histórico do Git para entender o que foi feito.

04:27

E não só olhar a descrição do que está no repositório do Git,

04:31

ele consegue também olhar os diffs para entender o que já

04:35

foi feito e do que ele precisa modificar baseado nas últimas alterações.

04:40

Então, tem muita gente que tem aflição de

04:43

pedir para o agente ficar comitando automaticamente,

04:47

mas na realidade,

04:48

essa é a maior parte de segurança que você tem.

04:52

Na hora que você for trabalhar, porque quanto mais entre as suas commits lógicas,

04:56

obviamente, que ele for fazer, isso vai ajudar tanto você,

05:01

vai dar segurança de caso faça alguma besteira, você consegue voltar,

05:04

mas vai ajudar o agente a entender o estado anterior na hora que ele for trabalhar,

05:09

principalmente quando a gente for falar de estado do nosso projeto.

05:13

Não sei se você percebeu, mas até agora a gente não mantém o estado,

05:16

né? Ou seja, a gente fala para executar uma feature...

05:19

mas a gente não está ali falando especificamente o que ele já fez,

05:23

o que ele não fez. Então, lembre-se disso,

05:26

que nesse momento a gente não está trabalhando com estado,

05:29

o maior estado que ele tem nesse momento é o Git.

05:31

Depois que ele terminar a implementação, eu forço ele a fazer uma verificação final.

05:36

Qual é essa verificação final?

05:38

Rodar a suíte inteira de testes e fazer uma rechecagem nos critérios de aceitação.

05:45

E depois disso, ele vai trazer para mim um relatório final.

05:48

Esse relatório final aqui, pra mim, ele é importante em alguns aspectos, tá?

05:53

Nesse relatório final, eu vou pedir para ele trazer o que ele conseguiu fazer,

05:57

o que ele não conseguiu fazer, os desvios que ele teve no meio do processo.

06:04

Como assim desvio? Às vezes a especificação pedia pra ele fazer alguma coisa, e ele fez,

06:09

mas ele fez de uma forma um pouco diferente.

06:11

Então ele vai colocar o que ele fez de forma diferente.

06:14

É importante a gente entender esses desvios,

06:16

porque são esses tipos de desvio que ao longo do tempo vão fazendo com que a

06:22

arquitetura do seu software vá se degradando pelo fato

06:26

de que hoje desviou um pouquinho aqui, depois ali,

06:29

e depois perto da arquitetura original, das suas instruções originais,

06:33

de como você tinha organizado o sistema,

06:35

você vai ver que o seu sistema cada vez está

06:36

indo muito mais longe em relação a isso.

06:39

Então, pedir para ele trazer essas informações é importante.

06:44

Tem uma outra coisa aqui também que é interessante você entender.

06:48

São conceitos de hard e soft fail, tá?

06:55

Então eu vou colocar aqui pra você, ó. Hard fail, tá? E soft fail.

07:03

Quais são esses conceitos aqui de soft e hard fail?

07:08

O hard fail é quando ele realmente não

07:11

consegue fazer algo pelo fato de ele não...

07:15

ter a informação, ou ele não ter ferramenta,

07:19

ou ele não conseguir realmente trabalhar com aquilo. Vou dar um exemplo.

07:23

Imagina que eu estou pedindo para ele fazer os testes

07:27

com a OpenAI e ele não tem a chave.

07:30

Ou seja, isso pode ser um hard fail. Ah,

07:33

eu preciso que ele se conecte com o meu CRM e ele não consegue se conectar. É um hard fail,

07:38

porque não tem como ele conseguir fazer como se qualquer

07:42

outro melhor desenvolvedor do mundo também não conseguisse. Então,

07:45

é importante a gente saber esse hard fail. Agora, o soft fail, ele,

07:50

na realidade, é eu não consegui fazer, mas existiu uma possibilidade.

07:54

Eu tentei testar daquela forma e eu não

07:57

consegui testar daquele jeito por algum impedimento.

08:00

Mas a feature foi desenvolvida de alguma forma. Então,

08:03

isso aí é importante. E no próximo vídeo,

08:06

eu vou mostrar para vocês como que nós criamos e estruturamos esse prompt. Então, vamos nessa.

## Resumo IA

**Abreviações**
*   **ID**: Identificador
*   **CRM**: Customer Relationship Management

**Resumo**
A aula apresenta a skill `implement`, projetada para padronizar o processo de solicitação de implementação a um agente de desenvolvimento de software, garantindo flexibilidade e consistência, essencial para o trabalho paralelo. A skill recebe um identificador (ID) da feature, o folder de trabalho e `overrides` opcionais. Estes `overrides` são instruções adicionais que permitem sobrescrever o comportamento padrão da skill, adaptando-a a necessidades específicas sem a criação de novos comandos, como solicitar credenciais ou alterar a forma de testar uma feature.

O fluxo de implementação inicia com a leitura de arquivos de documentação (`spec.md`, `plan.md`, `prd`), que fornecem o contexto funcional, o plano de execução e o enquadramento da feature no sistema. Os `overrides` são aplicados nesta etapa, ajustando a interpretação da feature às restrições do caso atual. Segue-se um "Preflight Dependency Check", que verifica as dependências da feature com o sistema existente e outras features, aumentando a consciência do agente sobre o ambiente e prevenindo implementações inconsistentes.

A execução principal ocorre em um loop de "implementar, validar e decidir o próximo passo". A validação inclui ferramentas como linter, type check e testes, sem acoplamento a uma stack tecnológica específica. Se a validação falha, o agente re-implementa; se passa, o progresso é consolidado através de um commit. É crucial que cada grupo de fases concluído gere um commit, pois isso facilita o rastreamento, possibilita rollbacks e utiliza o histórico e os diffs do Git como memória operacional para o agente, funcionando como principal fonte de estado recuperável na ausência de um mecanismo de estado explícito.

Após a implementação, uma verificação final mais abrangente é realizada, incluindo a execução da suíte completa de testes e a rechecagem dos critérios de aceitação, garantindo a conformidade global da feature. Finalmente, um relatório detalhado é gerado, registrando o que foi concluído, o que não foi e quaisquer "desvios" da especificação original. O relatório também distingue entre "Hard Fail" (bloqueios estruturais por falta de informação, acesso ou ferramenta) e "Soft Fail" (impedimentos parciais superados de alguma forma), o que ajuda a diferenciar causas de falha e melhora a qualidade do feedback.

**Pontos de atenção**
*   **Balancear Padronização e Flexibilidade**: A skill `implement` oferece uma estrutura consistente para pedidos, mas os `overrides` são essenciais para permitir customização sem engessar o processo ou a criação excessiva de prompts.
*   **Priorizar Documentação**: É fundamental que o agente leia `spec.md`, `plan.md` e `prd` para obter contexto funcional e de sistema, evitando implementações baseadas apenas em inferências locais do código.
*   **Verificação de Dependências**: O "Preflight Dependency Check" é um passo crítico para que o agente tenha "awareness" do ambiente e evite criar implementações inconsistentes com o estado atual do projeto.
*   **Integração Contínua da Qualidade**: O ciclo "implementar, validar, decidir" garante que a qualidade seja parte inerente do fluxo de desenvolvimento, e não uma etapa tardia de revisão.
*   **Commits Lógicos e Frequentes**: Gerar commits para cada grupo de fases concluído é uma boa prática que preserva o histórico, facilita rollbacks, marca o progresso e, principalmente, serve como memória operacional para o agente, que pode inspecionar commits e diffs.
*   **Git como Fonte de Estado**: Na ausência de um mecanismo de estado explícito para agentes, o repositório Git se torna a principal fonte de estado recuperável, permitindo ao agente inferir decisões e evitar retrabalho. Commits automáticos e lógicos aumentam a segurança operacional.
*   **Verificação Final Abrangente**: A execução da suíte completa de testes e a rechecagem dos critérios de aceitação após a implementação são cruciais para garantir a conformidade global da feature e capturar regressões que validações parciais poderiam ter perdido.
*   **Monitoramento de Desvios**: Registrar e tornar explícitos os "desvios" da especificação original, mesmo que a feature funcione, é vital para prevenir a degradação arquitetural silenciosa ao longo do tempo.
*   **Diferenciação de Falhas**: A distinção entre "Hard Fail" (bloqueios estruturais insuperáveis, como ausência de chaves de API) e "Soft Fail" (impedimentos parciais que foram contornados) no relatório final fornece clareza sobre a natureza dos problemas e melhora a análise de desempenho do agente.