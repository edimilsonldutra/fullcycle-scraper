Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17987)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, seguinte, aqui nós temos a nossa seed criada. Então,

00:05

o que eu vou pedir aqui para ele nesse momento?

00:09

Eu vou pedir, a primeira coisa que eu já vou fazer aqui,

00:12

eu vou criar um novo branch aqui para mim.

00:15

Não vou trabalhar com WorkTree, então eu vou colocar um asterisco,

00:18

vou colocar git checkout -b e

00:21

eu vou colocar seed aqui para mim.

00:27

Então, ele criou um novo branch aqui para mim chamado seed,

00:30

apenas para não ficar misturando muito com o main, tá?

00:33

E o que eu vou pedir para ele fazer aqui já de cara para mim é dar um commit. Estou usando o Cloud Code,

00:38

então eu vou dar um commit, commit, que é uma extensão.

00:42

E o que esse cara consegue fazer? Ele olha os padrões dos meus commits,

00:46

faz o diff aqui para mim e ele já vai gerar o commit com a ideia,

00:50

com a mensagem e tudo mais.

00:52

Beleza? Então, ele acabou de fazer... esse ajuste aqui para mim. Agora,

00:58

qual que é o meu grande ponto aqui nesse momento?

01:01

Vai depender muito do que eu quero fazer e o nível de

01:06

detalhe que eu quero passar e o nível de complexidade da task.

01:11

Por que eu estou dizendo isso? Quando a gente está trabalhando,

01:13

sei lá, com SDD, a gente vai fazer sempre...

01:16

aquela parte maior, onde o agente fica um tempão,

01:20

na realidade, trabalhando ali para a gente. Porém,

01:23

esses ajustes no meio do caminho são necessários para a gente conseguir

01:26

fazer com que o agente fique rodando um bom tempo.

01:29

Então, por exemplo, nesse tipo de coisa, eu poderia fazer o quê?

01:33

Eu posso criar um modo de planejamento aqui para mim

01:36

e posso chegar e falar aqui para ele, olha,

01:39

a partir de agora eu quero que você faça a implementação

01:43

do meu init quando eu passar por --seed.

01:45

Ele vai trabalhar.

01:47

Ou eu posso fazer o contrário. Quando ele entrar, ele der um init,

01:51

eu posso dar um "--ignore-seed", para ele não aplicar seed. Porque,

01:56

por padrão, eu quero com seed no meu processo de desenvolvimento.

01:59

Então, o que eu vou fazer aqui, nesse momento, galera?

02:03

Eu vou fazer o seguinte. Eu vou criar aqui,

02:08

eu poderia criar uma nova sessão, mas... Aqui nesse caso,

02:12

eu tô com uma janela de token grande, eu não tô me preocupando,

02:14

mas eu poderia e eu acho que não teria problema nenhum criar uma nova,

02:17

ou até criar uma nova sessão para a gente não ter rolo

02:23

aqui, tá? Então eu vou colocar aqui em modo de planejamento, tá?

02:28

Atualmente, tenho o meu arroba seed.ts,

02:36

o meu arroba seed, em qual página que ele tá?

02:41

Scripts... barra

02:43

seed aqui. E desejo

02:50

que

02:53

ele seja executado ao iniciar o ambiente. Ou

03:01

seja, na execução do

03:06

arroba init.sh.

03:10

Quero também criar uma flag que

03:18

quando passada

03:23

a seed não

03:26

será executada, que é o "-ignore -seed". E

03:33

vou dar um enter agora aqui no meu modo planejamento, ou seja, pessoal,

03:38

estou fazendo isso da forma mais simples,

03:40

porque você não precisa o tempo todo ficar...

03:47

criando especificação, criando isso, aquilo, dependendo do tipo de tarefa,

03:50

principalmente tarefas de ajuste de ambiente,

03:53

a não ser que seja uma tarefa muito grande,

03:55

aí sim eu vou criar uma spec, etc. Caso contrário,

03:58

eu vou usar os recursos fáceis que têm em DAIA. E aí vai depender,

04:02

se eu for fazer uma mudança num script que é bem importante como o init,

04:06

eu vou criar um módulo de planejamento aqui para ele

04:09

olhar aqui para mim e entender melhor esses aspectos.

04:12

Se for algo muito simples, como criar simplesmente uma seed,

04:16

o que eu fiz? Criei, pedi direto sem módulo de planejamento.

04:20

Aí depende muito do seu bom senso, do tamanho de tudo que vai acontecer.

04:25

Ele trouxe aqui para mim como que ele pretende fazer.

04:29

Aqui para mim, ele trouxe o problema do usuário,

04:32

quando ele roda, a SID já é depletente, as mudanças,

04:35

onde ele está basicamente colocando um IF, a função runSID para espelhar o Prisma,

04:42

e aparentemente chamar o runSID aqui nessa sequência.

04:45

Verificação, e eu vou dar um sim aqui para ele, tá?

04:48

Porque não é uma mudança aparentemente complexa aqui para mim.

04:52

Quando a gente cai em mudanças mais complexas,

04:54

eu vou passar algumas dicas que normalmente eu utilizo muito

04:57

quando eu vou trabalhar também em modo planejamento.

05:00

Então, ele já está adicionando isso aqui para mim. Maravilha.

05:12

Vamos aguardar.

05:16

E ele falou que implementou essas mudanças aqui para mim.

05:21

Agora, você quer que eu rode o script para confirmar? Eu vou colocar assim.

05:28

Pare e limpe o ambiente.

05:31

Depois... Suba

05:33

com acids,

05:37

derrube e suba sem acids.

05:43

Realmente para ele fazer esse teste aqui para mim.

05:45

Perceba, quando é coisa bem simples, galera,

05:47

não tem muito segredo.

05:50

Você não precisa ficar que nem um mágico querendo rodar um trilhão de coisas.

05:55

Você vai interagir com a IA.

05:57

E eu acho que isso não tem problema nenhum quando

05:59

você está trabalhando com a estrutura do harness,

06:02

de forma geral. Agora,

06:04

se você vai ficar de babá da IA no momento da implementação de coisas grandes,

06:09

principalmente, aí provavelmente tem algo meio que errado no meio da história.

06:14

Então é isso que você tem que tomar cuidado e entender essa

06:18

zona meio cinzenta de quando que

06:21

você usa a IA como um parceiro,

06:27

ou seja, eu estou interagindo, estou trabalhando aqui com ela.

06:31

mas ou quando ela vai rodar de forma autônoma mesmo,

06:35

por um bom tempo criando as features, que é o que a gente está fazendo.

06:38

Então ele falou que aplicou e etc. e tudo mais.

06:41

O ambiente está atualmente rodando e beleza.

06:44

Uma coisa que eu costumo fazer muito aqui nesses aspectos, galera,

06:48

eu não mostrei, eu acho, no ponto anterior, mas no caso,

06:53

Cloud Code falando, mas normalmente é prompt,

06:56

você pode usar isso em outros, eu gosto de rodar um simplify.

07:00

Quando você dá um barra simplify aqui, ele vai ver o diff das mudanças que houve,

07:04

e ele vai ver se consegue simplificar aquele script,

07:07

tirando pontos redundantes e coisas desse tipo,

07:10

para garantir que você evite aquele monte de AI slot,

07:15

aquele monte de código duplicado e coisas desse tipo.

07:18

Esse tipo de script, esse tipo de plugin ajuda pra caramba,

07:22

onde ele roda alguns agentes e fica verificando o reuso, ele fica verificando a...

07:30

reuso, qualidade e etc.

07:32

Ele acha aqui que provavelmente é muito pequena

07:36

essa diff para ficar rodando a gente,

07:38

então nesse caso aqui, ele só fez alguns ajustes aqui, pronto do resumo aplicado.

07:45

Tinha uma flag desconectada, a mão copiada do stop .sh que não tem helper.

07:52

Movi o loop de argumentos, as definições e troquei por uma flag,

07:56

reutilizando o helper e etc.

07:59

a avaliar de mantido e etc.

08:02

E agora eu vou pedir refaça os testes novamente.

08:09

Somente para garantir se esse meu Simplify não fez algum problema aqui para mim.

08:14

Então ele está parando o ambiente,

08:15

vai subir e vamos aguardar isso aqui.

08:18

Vou editar um pause aqui rápido no vídeo para você não ficar gastando muito tempo.

08:23

Beleza, então ele rodou aqui e falou que até

08:26

subiu o ambiente rodando, subido sem sigs.

08:30

Tem seeds na porta 40, 75 e tudo mais.

08:34

Agora, a gente tem o seguinte. O nosso script de init mudou,

08:37

né? Então, o que eu vou pedir aqui para ele fazer?

08:43

Atualize o cloud.md trazendo mais

08:50

esse novo parâmetro ali

08:57

para mim. Vamos ver e o meu cloud.md está aberto aqui.

09:01

Então, vamos ver. Para ele fazer essa atualização,

09:04

obviamente, né? Eu poderia simplesmente mudar uma linha aqui.

09:08

Aquela preguiça de AI ali para mim. Vamos lá.

09:20

Então, ele editou algo real. Bom,

09:22

aqui o cloud.md é um link simbólico na realidade, né?

09:29

Então, aqui deixa eu reabrir meu cloud.md.

09:33

Cadê meu cloud.md? É o agent.md na realidade, né?

09:38

Então, ele colocou 'use to start the project with running seeds'.

09:42

Agora, isso aí é um ponto importante e beleza, tá?

09:45

Agora, um ponto importante aqui também é o seguinte.

09:49

Uma vez que a gente tem isso e eu fiz essa melhora no Cloud.md,

09:53

o que eu vou fazer agora aqui? Eu vou dar um commit.

09:59

Vou criar mais um commit.

10:01

Normalmente, eu gosto de fazer pequenos commits no meio dessas

10:04

interações para eu poder voltar e aí entender,

10:06

inclusive... esses aspectos, commit criado e tudo mais.

10:10

Próximo vídeo, eu vou olhar e a gente vai dar uma revisada nesse cloud.md

10:15

Porque a gente já está no momento que a gente pode melhorar esse cara aí. Então, vamos nessa.

## Resumo IA

**Abreviações**

*   **AI / IA**: Inteligência Artificial
*   **diff**: Diferença (utilizado para comparar alterações em arquivos)
*   **Git**: Sistema de controle de versão distribuído
*   **init.sh**: Script de inicialização (arquivo de shell script)
*   **.md**: Formato de arquivo Markdown (utilizado para documentação)
*   **SDD**: Software Design Document (Documento de Projeto de Software) - inferido como uma fase de planejamento e especificação mais extensa.
*   **seed.ts**: Script de *seeding* (população inicial de dados) em TypeScript
*   **.sh**: Extensão para arquivos de *shell script*
*   **spec**: Especificação
*   **TS**: TypeScript (linguagem de programação)

---

**Resumo**

A aula aborda o processo de aprimoramento do script de inicialização de um ambiente de desenvolvimento para incluir a execução automática de um script de *seeding* (`seed.ts`), além da adição de uma *flag* para controlar essa funcionalidade. O objetivo é integrar a execução do `seed.ts` ao `init.sh` de forma padrão, oferecendo também o parâmetro `--ignore-seed` para desativar o *seeding* quando necessário.

O instrutor inicia criando um novo *branch* (`seed`) no Git para isolar as mudanças e realiza um *commit* inicial usando uma extensão do Cloud Code que padroniza mensagens de *commit*. Ele demonstra como interagir com uma ferramenta de IA (Cloud Code/DAIA) para desenvolver a funcionalidade. Para esta tarefa, que envolve uma modificação em um script crucial (`init.sh`), o instrutor opta por usar o "modo de planejamento" da IA, fornecendo uma descrição detalhada das mudanças desejadas: execução do `seed.ts` no `init.sh` por padrão e a criação da *flag* `--ignore-seed`.

Após a IA propor a solução, o instrutor a aprova e, em seguida, solicita testes abrangentes para verificar a correta execução do ambiente com e sem as *seeds*. Posteriormente, ele utiliza o comando `/simplify` (disponível na ferramenta de IA) para otimizar o código gerado, removendo redundâncias e melhorando a qualidade. Após a simplificação, novos testes são executados para garantir a estabilidade das alterações. Finalmente, a documentação do projeto (`cloud.md` ou `agent.md`) é atualizada para incluir a descrição do novo parâmetro `--ignore-seed`, e as mudanças são salvas em um *commit* focado.

---

**Pontos de atenção**

*   **Estratégia de Branching:** É uma boa prática criar *branches* separados (ex: `seed` branch) para desenvolver novas funcionalidades ou fazer ajustes significativos, evitando misturar o trabalho com o *branch* principal (`main`).
*   **Qualidade dos Commits:** Utilize ferramentas ou extensões que auxiliem na criação de *commits* padronizados e com mensagens claras, facilitando o histórico de mudanças e a colaboração.
*   **Interação com IA (Modo de Planejamento vs. Comando Direto):**
    *   Para tarefas simples e ajustes pequenos, a interação direta com a IA pode ser eficiente.
    *   Para tarefas mais complexas ou que envolvem scripts críticos (como `init.sh`), o "modo de planejamento" é recomendado. Ele permite detalhar o problema e os requisitos para a IA, resultando em soluções mais precisas e alinhadas.
    *   A escolha entre os modos deve ser feita com base na complexidade e no impacto da tarefa.
*   **IA como Parceira, não Babá:** Interaja com a IA como uma parceira, fornecendo orientações e validando seus resultados, especialmente em tarefas menores. Evite "micromanager" a IA em grandes implementações; confie em sua autonomia quando as instruções são claras.
*   **Simplificação e Refatoração de Código Gerado:** Sempre revise e utilize comandos como `/simplify` para otimizar o código gerado pela IA. Isso ajuda a remover redundâncias, garantir reuso e manter a qualidade do código.
*   **Testes Abrangentes:** Após implementar novas funcionalidades ou *flags*, execute testes completos para validar todos os cenários (ex: com e sem a *flag*), garantindo que a funcionalidade se comporta conforme o esperado. Lembre-se de retestar o código após qualquer otimização ou refatoração.
*   **Manutenção da Documentação:** Mantenha a documentação do projeto (ex: arquivos `.md`) atualizada com novos parâmetros, funcionalidades e mudanças na configuração do ambiente. Isso é crucial para a compreensão e manutenção futura do projeto.
*   **Commits Pequenos e Frequentes:** Prefira fazer *commits* pequenos e focados ao longo do desenvolvimento. Isso facilita o rastreamento das mudanças, o *rollback* se necessário e a compreensão do fluxo de trabalho.