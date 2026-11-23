Módulo: Arquitetura na Era da IA\
Aula: [O que RAG não resolve](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18405)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? No vídeo anterior a gente entendeu o que é RAG.

00:05

A gente viu que a ideia principal é recuperar informações externas,

00:09

colocar esse contexto na entrada do modelo e deixar

00:12

o modelo gerar uma resposta baseada naquele conteúdo.

00:15

Agora, antes de começar a implementar isso,

00:18

a gente precisa entender um ponto muito importante.

00:21

RAG não resolve qualquer problema. E esse cuidado é fundamental,

00:26

porque quando uma tecnologia começa a ficar popular,

00:29

a tendência é tentar usar ela em tudo.

00:32

A pessoa vê um problema envolvendo pergunta, resposta,

00:35

documento, dado, informação e já pensa,

00:37

vou colocar um RAG aqui.

00:39

Só que nem todo problema de informação é um problema de RAG.

00:44

RAG faz muito sentido quando a resposta

00:47

depende de conhecimento externo em formato de documento, política,

00:53

PAC, manual, contrato, documentação, artigo ou base interna. Ou seja,

00:58

quando existe uma fonte textual que precisa ser

01:01

recuperada para ajudar o modelo a responder.

01:04

Agora, se a resposta depende do estado atual de um sistema,

01:08

talvez RAG não seja a melhor solução. Por exemplo,

01:12

se o usuário pergunta qual foi o último pagamento do aluno João,

01:16

isso não deveria ser respondido buscando em um documento.

01:20

Isso provavelmente deveria vir de um banco de dados,

01:23

de uma API ou de alguma ferramenta que consulta o sistema financeiro.

01:27

A resposta depende de um dado transacional,

01:30

ao vivo, vamos dizer assim, que acaba mudando ali o tempo todo.

01:34

Outro exemplo é, cancele a matrícula desse aluno.

01:38

Isso também não é RAG.

01:39

Aqui a gente não está falando de recuperar conhecimento para responder.

01:43

A gente está falando de executar uma ação dentro do sistema.

01:47

Isso entra muito mais em workflow, tool calling, automação,

01:52

regras de negócio e autorização. Agora, se a pergunta for...

01:57

Qual é a política de cancelamento para alunos do plano Enterprise?

02:00

Aí sim... Começa a fazer mais sentido pensar em RAG,

02:04

porque a resposta provavelmente está em algum documento interno,

02:08

em alguma política comercial ou em alguma base de conhecimento.

02:12

Então, uma primeira separação importante é essa.

02:15

RAG é para recuperar conhecimento, não é para substituir banco de dados,

02:20

não é para consultar qualquer dado ao vivo,

02:23

ali vindo da aplicação, e também não é para executar alguma ação no sistema.

02:29

Um outro ponto importante,

02:31

É, RAG não garante verdade. Isso parece contraditório no começo,

02:37

porque a gente usa RAG justamente para melhorar a resposta.

02:40

Mas melhorar não significa garantir. Se o documento estiver errado,

02:45

o RAG pode trazer uma resposta errada.

02:47

Se o documento estiver antigo, a resposta pode estar desatualizada.

02:51

Se a busca recuperar o trecho errado, o modelo pode gerar uma resposta até bonita,

02:56

bem escrita, mas baseada... num contexto errado.

03:00

Então o RAG não elimina a alucinação automaticamente.

03:03

Ele reduz o risco quando o contexto é certo,

03:07

É recuperado e usado ali corretamente.

03:11

Mas se o pipeline falha, a resposta também pode falhar. E aqui entra um outro ponto.

03:16

RAG não conserta uma base ruim.

03:19

Se os documentos estão bagunçados, duplicados, contraditórios,

03:23

sem versão, sem metadados, sem dono e sem processo de atualização,

03:27

o problema não desaparece só porque a gente colocou

03:30

embeddings em um banco vetorial ali no meio.

03:33

Às vezes ele fica até mais perigoso porque a resposta final parece inteligente,

03:39

mas por trás está usando uma base desorganizada.

03:42

Reg também não resolve permissão sozinho.

03:46

Se o usuário pode acessar um documento de um produto,

03:48

de um tenant ou de um plano específico,

03:51

essa permissão precisa ser aplicada antes do contexto chegar ao modelo.

03:57

Não adianta recuperar um documento privado,

03:59

colocar no prompt e pedir para o modelo não usar aquilo.

04:02

O controle precisa estar na arquitetura da aplicação,

04:05

não só na instrução do prompt. E tem mais um limite importante.

04:09

Custo. RAG não é de graça. Existe um custo para gerar embeddings,

04:14

custo para armazenar vetores, custo para fazer busca,

04:17

custo de infraestrutura e principalmente de tokens na hora

04:21

de montar o contexto para o modelo.

04:23

Quando a aplicação recupera vários chunks e coloca tudo dentro do prompt,

04:28

esses trechos viram input tokens. E quanto mais contexto você manda,

04:32

maior pode ser o custo e maior também pode ser a latência. Então o RAG,

04:38

só porque parece moderno ou qualquer coisa desse tipo,

04:42

pode deixar a aplicação mais cara, mais lenta,

04:45

mais complexa, sem melhorar a qualidade da resposta.

04:49

Às vezes a base é pequena e cabe no contexto do modelo.

04:53

Às vezes cache resolve. Às vezes uma consulta SQL vai resolver.

04:57

Muitas vezes uma chamada de API é melhor.

05:00

O ponto é que RAG precisa entrar porque existe

05:03

um problema real de recuperação de conhecimento,

05:06

não porque virou um padrão ou é alguma coisa

05:09

que todo mundo acaba utilizando de forma geral. Na prática,

05:14

um RAG bem desenhado pode ajudar a controlar custos porque

05:18

evita mandar documentos enormes e permite recuperar apenas o que importa.

05:23

Mas um RAG mal desenhado pode fazer o contrário, buscar contexto demais,

05:27

mandar token demais e ainda assim responder mais.

05:29

Então, a mensagem principal dessa aula é, RAG é uma peça importante,

05:35

mas ela não é arquitetura inteira.

05:38

Ela resolve muito bem o problema de recuperar

05:41

contexto relevante em uma base de conhecimento.

05:43

Mas ela não substitui um banco de dados, não substitui API,

05:47

não substitui as suas regras de negócio, autorização, ações, etc.

05:52

Ou seja, antes de implementar RAG,

05:55

a gente precisa saber quando ele faz sentido e quando ele não faz.

05:59

Porque usar RAG apenas para poder aumentar custo,

06:02

latência e deixar o seu sistema mais complexo, sem dúvidas,

06:06

não vai valer a pena. No próximo vídeo...

06:08

a gente vai comparar o RAG com outras estratégias como Long Context,

06:12

Cache, SQL, API, Socket Calling e Fine Tuning.

06:16

Isso vai ajudar a posicionar melhor cada solução dentro da arquitetura.

## Resumo IA

[RESUMO_IA]