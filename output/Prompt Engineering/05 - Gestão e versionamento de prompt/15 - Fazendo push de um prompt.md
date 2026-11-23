Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16729)

## Resumo da aula

Publicar um prompt no LangSmith por código conecta o repositório local ao hub remoto sem depender da interface. O fluxo central é simples: carregar o template local, instanciar o client autenticado por variáveis de ambiente e chamar push_prompt. Retomando o exemplo do agente de pull request, a novidade aqui não é o ID nem o template em si, mas o empacotamento desse artefato para publicação remota. Esse passo transforma o prompt local em um item versionado no hub com histórico de commits.

As variáveis de ambiente sustentam a autenticação e a configuração do client antes do push. Sem elas, o script não consegue se conectar à conta ou ao workspace corretos, então o problema não é apenas conveniência, mas viabilidade operacional. Como a autenticação já foi preparada anteriormente, o ponto novo aqui é que o script de publicação depende desse contexto para funcionar fora da interface. Em troubleshooting, falhas de push costumam começar por credenciais ausentes, inválidas ou carregadas no ambiente errado.

O script usa algo como registry.getPrompt para localizar um prompt no projeto e obter seu conteúdo antes do envio. Isso serve como fonte de entrada para o push, não como exigência arquitetural: o template também poderia vir de uma string em memória ou de outra origem. A escolha por carregar do registry é útil para reaproveitar a organização já existente no projeto e demonstrar que o mesmo artefato local pode ser promovido ao hub. Se houver sincronização entre local e remoto, a equipe precisa decidir explicitamente qual lado é a fonte da verdade.

A chamada push_prompt envia ao LangSmith pelo menos três elementos relevantes neste contexto: o ID do prompt, o template e as tags. O ID identifica o artefato remoto de forma única dentro do hub; na prática, ele funciona como um nome reservado que não pode colidir com outro prompt no mesmo espaço. O template é o conteúdo efetivo publicado, e as tags entram como metadados auxiliares, como versão textual, modelo associado e descrição. Separar esses papéis evita confundir identificação do artefato, conteúdo publicado e informação de catalogação.

Prompt tags servem para busca, filtro e organização, não para representar o mecanismo real de versionamento consumível. Colocar v1.0.0, model:gpt-5-nano ou uma descrição nas tags ajuda a catalogar o prompt, mas isso não transforma essas tags em identificadores de commit. Essa distinção é crítica porque a aparência de “versão” nas tags pode induzir a equipe a tratá-las como referência operacional estável. Elas são metadados úteis, mas não substituem o identificador real gerado pela plataforma.

O push gera um hash que representa o estado publicado do prompt naquele commit. Esse hash é o identificador efetivo da revisão criada no hub e é ele que diferencia uma publicação nova de uma tentativa de reenviar exatamente o mesmo conteúdo. Quando o mesmo prompt é enviado novamente sem alteração, o sistema detecta que o estado já existe e retorna erro em vez de criar um commit redundante. Em outras palavras, o versionamento real está ancorado no conteúdo publicado, não na tag textual que você anexou.

Executar o mesmo script duas vezes sem mudar o prompt falha porque o segundo envio produz o mesmo hash do primeiro. Isso mostra que o controle de commits não depende apenas do nome do prompt: o nome identifica o artefato lógico, mas o hash identifica o estado exato daquele artefato. Para gerar um novo commit, é necessário alterar o conteúdo publicado e então executar o push novamente. Mudar apenas a intenção sem mudar o template não cria uma nova revisão real.

Retomando o prompt de pull request creator, alterar o registro local de 1.0.0 para 1.0.1 e publicar novamente só produz um novo commit se o estado enviado for diferente. Quando isso acontece, o hub passa a exibir dois commits, o template publicado e as prompt tags associadas a cada envio. O histórico visível facilita inspeção e auditoria, mas a leitura correta continua sendo: tags ajudam a organizar, enquanto o commit é identificado pelo hash. Essa separação prepara o consumo remoto correto nas próximas etapas do fluxo.

Depois da publicação, o prompt aparece no hub com tipo, template, commits, autor e campos auxiliares como comentários. Essa visualização confirma que o push não apenas armazenou texto, mas registrou uma revisão navegável dentro da infraestrutura remota já usada para gestão de prompts. O valor prático disso está em permitir publicação programática sem perder histórico nem governança. O hub vira o ponto de consulta do estado publicado, enquanto o script vira o mecanismo de promoção desse estado.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente falou e a gente viu um prompt sendo criado aqui com o Langsmith. Agora, uma coisa interessante é que se esse prompt está aqui no Langsmith, como é que eu vou conseguir utilizar dentro da minha aplicação? Então, essa é a primeira pergunta e é por isso que o Langsmith tem SDK para que você consiga trabalhar. Então, o que eu vou mostrar agora aqui para você vai ser o seguinte, tá? Eu vou te mostrar

00:31

Dentro aqui da aplicação, eu criei dois arquivos. Um arquivo chamado lang.smith.push. O que esse arquivo faz aqui, galera? Somente para você entender aqui. A primeira coisa que você tem que se ligar é que existem algumas variáveis de ambiente que estão aqui. Legal? E é interessante que você tenha, principalmente aqui do lang.smith,

00:58

Mas, o mais interessante aqui desse punch é o seguinte, o que eu estou fazendo? Eu estou usando o meu registry.getPrompt, estou fazendo um prompt path, ou seja, estou carregando um prompt que está no meu repositório. Wesley, por que você está fazendo isso? Porque eu queria dar um exemplo apenas de a gente pegar e carregar esse prompt, mas, obviamente, não faz muito sentido eu ter esse prompt no meu computador,

01:28

no meu repositório se eu vou usar o Langsmith. Ou até pode fazer se eu fizer algum esquema de fazer sincronização, que é muito comum para você não ficar chamando externamente o Langsmith toda hora, na hora que você for carregar um prompt. Então, sim, eu posso fazer algo parecido. Mas, de forma geral, o objetivo aqui desse script não é a gente carregar o nosso prompt que está aqui, porque muitas vezes esse prompt não vai estar aqui.

01:56

ou ele vai e daí tem todo um outro esquema de sincronização que você pode escolher qual que é a fonte da verdade no final das contas, tá? Agora, o ponto interessante aqui é que eu peguei o client aqui do lang.smith e aqui eu tenho um push prompt, tá? E o que esse push prompt acaba fazendo no final das contas?

02:17

Eu estou colocando o ID do prompt, ou seja, o nome do prompt, e isso aqui é como se fosse um repositório no GitHub. Então, não pode ter um repositório com o mesmo nome. Basicamente é isso, tá? Outra coisa é o prompt template, que é o que eu carreguei, ou seja, o conteúdo do meu prompt. Ou seja, eu não precisava ter nada disso aqui, eu poderia apenas colar o conteúdo do meu prompt dentro de uma variável, e esse prompt template segue o padrão de um prompt template

02:47

que a gente está acostumado, baseado naquele padrão que ele está, inclusive, trabalhando ali com o YAML. Outra coisa interessante é a parte de tags, tá? Mas é aqui que você tem que entender uma coisa muito clara. Existe algo chamado prompt tags. O que são prompt tags? São tags que eu consigo colocar no meu prompt para utilizar como metadado de forma geral. E eu posso colocar quantas tags eu quiser. Nesse caso,

03:16

Eu estou pegando do meu registry, colocando a versão, colocando um V aqui na frente, coloquei model, e coloquei o model que esse prompt estava sendo utilizado, e coloquei uma description que está na descrição também ali do meu prompt. Então, basicamente, foi isso que eu fiz. Por outro lado, o que acontece?

03:39

Essas tags aqui, elas são prompt tags. Isso não significa que isso aqui é a versão do prompt. E eu já vou falar pra você o que isso significa, tá? Vamos imaginar que eu quero pegar esse meu prompt de pull request creator. Então, deixa eu chegar aqui. Prompt de pull request creator. Se você perceber aqui, eu tenho uma versão 1.0.

04:04

a .0, eu tenho uma versão 1.0.1. Se eu chegar aqui no meu registry, e eu vou colocar aqui que ele é 1.0.0, tá?

04:15

Vou colocar que é 1.0.0. O que ele vai fazer aqui para mim no final das contas? Deixa eu abrir aqui. Eu vou executar, então vamos lá. Eu vou dar um Python, src, como que é o nome do meu camarada? langsmith-push, e vou dar um Enter aqui para mim. Na hora que eu dei esse Enter agora, você vai perceber que ele

04:42

criou esse meu prompt lá no lang.smith e ele gerou, inclusive, aqui um hash. Então, se eu entrar agora aqui no lang.smith

04:53

você vai perceber que já apareceu aqui pra mim um agent por request creator, ele é um string prompt template, tem um commit, prompt tags 1.0.0, model gpt-5 nano, aqui pra mim. Se eu entrar nesse cara, o que vai acontecer? Eu vou ver o template do meu prompt. Você vai perceber que tem toda essa

05:19

essas informações aqui pra mim. Então, eu vejo as tags, eu vejo o type, eu vejo o commit, quem fez o commit, posso adicionar comentário, igualzinho como a gente viu lá no PromptHub, porque tá no Hub aqui mesmo. Beleza? Agora, existem alguns pontos que são importantes aqui e que eu já quero mostrar pra você. Se eu executar novamente esse mesmo programa, olha só o que vai acontecer.

05:47

ele vai dar erro. E por que ele vai dar erro? Porque esse prompt já existe lá. Mas como ele verifica se ele já existe? Somente por conta do nome? Não. Porque na hora que eu subo esse prompt, o que vai acontecer? Ele tem um hash.

06:04

E, por conta desse hash, significa que se eu subir duas vezes a mesma coisa com o mesmo hash, significa que eu estou subindo a mesma coisa. Ou seja, eu não posso subir o mesmo prompt com o mesmo hash. Ponto final. Então, quando eu quiser fazer o push, eu preciso ter, obviamente, o meu prompt alterado. Então, eu vou chegar agora aqui,

06:35

Vou aqui no meu registry, vou falar agora que nós estamos na versão 1.0.1, tá aqui bonitinho aqui pra mim, e eu vou executar agora aqui o meu push. E agora você viu que foi. Quando eu chego agora aqui, você vai perceber que ele tem dois commits,

07:02

Tem a última versão, teve aqui a minha primeira versão, tenho aqui prompt tags com a versão 1.0.1 e etc. Agora, o que isso na prática significa? Significa que a minha última versão desse prompt é essa, eu consigo ver o histórico e eu tenho essas versões com o meu prompt tag. Porém, existe uma pegadinha aqui.

07:28

Esse meu prompt tag é apenas metadados para eu conseguir buscar, para eu conseguir me organizar. Isso não significa que é uma tag específica do prompt para você utilizar. E eu vou mostrar isso para você no nosso próximo vídeo, na hora que eu vou mostrar como você consegue utilizar esse prompt dentro do seu programa. Então, vamos nessa!

## Resumo IA

**Abreviações**
- **SDK** — *Software Development Kit* (conjunto de ferramentas e bibliotecas para integração com uma plataforma).
- **ID** — *Identifier* (identificador único de um artefato).
- **YAML** — *YAML Ain’t Markup Language* (formato de serialização legível para configuração e dados).
- **Hub** — repositório/central remota de gestão e publicação de prompts no LangSmith.
- **PR** — *Pull Request* (solicitação de mesclagem de alterações em código; no contexto, usado em “pull request creator”).

**Resumo**
A aula mostrou como publicar um prompt no LangSmith por código, sem depender da interface web, usando o SDK da plataforma. O instrutor explicou o fluxo central: carregar um prompt local do repositório com `registry.getPrompt`, instanciar o client do LangSmith com base em variáveis de ambiente e enviar o artefato com `push_prompt`. O objetivo não foi criar um novo prompt do zero, mas promover um prompt já existente localmente para o hub remoto, preservando histórico e governança.

Também foi enfatizado que a autenticação e a configuração do ambiente são indispensáveis para o script funcionar corretamente. Sem as variáveis de ambiente corretas, o client não consegue se conectar à conta e ao workspace adequados, o que torna a publicação inviável. O instrutor comentou que o prompt local pode até ser usado como origem do conteúdo em cenários de sincronização, mas a decisão sobre qual ambiente é a “fonte da verdade” precisa ser explícita quando há cópia entre local e remoto.

Na chamada de publicação, o `push_prompt` recebe elementos essenciais: o ID do prompt, o template e as tags. O ID funciona como identificador único do artefato no hub, o template é o conteúdo efetivamente publicado e as tags atuam como metadados para catalogação, como versão textual, modelo usado e descrição. A aula destacou com força que tags não são o mecanismo real de versionamento: elas ajudam a organizar e filtrar, mas não substituem commits nem servem como identificador de revisão.

Outro ponto central foi o hash gerado pela publicação. Esse hash representa o estado exato do prompt publicado e é o que define uma revisão no hub. Se o mesmo script for executado novamente sem alterações no prompt, o sistema detecta que o conteúdo já existe com o mesmo hash e retorna erro, em vez de criar um commit redundante. Para gerar uma nova versão, é necessário alterar o conteúdo do prompt e então executar o push novamente.

Por fim, o instrutor demonstrou que, ao alterar a versão local de 1.0.0 para 1.0.1 e publicar outra vez, o hub passa a exibir dois commits, com histórico visível, autor e metadados associados. Isso confirma que a publicação programática mantém rastreabilidade e auditoria, ao mesmo tempo em que centraliza o estado publicado no hub remoto.

**Pontos de atenção**
- As variáveis de ambiente precisam estar corretas para autenticação; credenciais ausentes, inválidas ou carregadas no ambiente errado causam falha no push.
- `registry.getPrompt` foi usado como exemplo de fonte local, mas o prompt também poderia vir de outra origem; em cenários com sincronização, é necessário definir qual lado é a fonte da verdade.
- O `ID` do prompt é o identificador do artefato no hub e deve ser único; não pode haver colisão com outro prompt no mesmo espaço.
- As `prompt tags` são apenas metadados para busca, filtro e organização; não devem ser tratadas como versão operacional do prompt.
- Não confundir tags como `v1.0.0` com o commit/revisão real: o versionamento efetivo é determinado pelo hash do conteúdo publicado.
- Reexecutar o push sem alterar o prompt tende a falhar, porque o hash gerado será o mesmo e o sistema não cria commit redundante.
- Para publicar uma nova versão, é necessário mudar o conteúdo do prompt, não apenas a intenção de versioná-lo.
- O hub registra histórico, autor, template e comentários; essa visibilidade é útil para auditoria e governança.
- Separar claramente três coisas evita confusão: identificação do artefato, conteúdo do prompt e metadados de catalogação.