Módulo: Arquitetura na Era da IA\
Aula: [Chunking, metadados e versionamento](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18413)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente começou o pipeline de ingestão.

00:05

A gente ainda não fez um reg de verdade.

00:07

A gente apenas leu os documentos na pasta Knowledge Base,

00:11

extraiu o front matter,

00:12

validou os metadados e garantiu que a base

00:15

está minimamente organizada para ser processada.

00:19

Agora entra uma etapa muito importante.

00:22

Transformar esses documentos em unidades menores de recuperação.

00:26

É aqui que aparece o chunking.

00:29

Quando a gente trabalha com REG,

00:31

normalmente o documento inteiro não vira uma única unidade de busca.

00:36

Um documento pode ter muitas sessões,

00:39

muitos assuntos diferentes, regras para planos diferentes,

00:42

detalhes de cobrança, SLA, segurança, integração, limites e assim por diante.

00:48

Se eu indexo o documento inteiro como um bloco só...

00:52

A busca pode ficar muito genérica, o sistema até encontra o documento certo,

00:57

mas talvez não encontre exatamente o trecho certo. Por outro lado,

01:02

se eu quebro demais o documento,

01:04

cada pedaço pode ficar pequeno demais e perder o sentido.

01:08

O chunk pode ter uma frase solta, uma regra sem título da sessão,

01:13

uma tabela sem contexto ou um trecho que sozinho acaba não explicando nada. Aí...

01:19

o sistema encontra um pedaço parecido,

01:21

mas o modelo não recebe a informação suficiente para responder bem.

01:26

Então, um chunking não é só um detalhe técnico,

01:30

é uma decisão arquitetural do REG.

01:33

Um chunk é uma unidade que vai disputar espaço na busca.

01:38

Quando o usuário fizer uma pergunta,

01:40

o sistema não vai procurar o documento mais bonito, ele vai procurar...

01:45

Os chunks mais relevantes. Então, se os chunks foram mal definidos,

01:50

o retrieval já vai começar errado. Imagine a gente criar um documento de SLA.

01:57

Ele pode ter uma sessão explicando P1, a outra explicando P2,

02:01

a outra falando de canais de suporte,

02:03

outra falando de créditos de SLA e outras falando de manutenção programada.

02:08

Se o usuário pergunta sobre incidente P1 no plano Enterprise,

02:12

o ideal é que a busca encontre justamente o trecho que fala de P1,

02:18

o plano Enterprise, o tempo de resposta. Agora, se o chunk misturar P1,

02:23

P2, P3, manutenção, crédito, SLA no mesmo bloco, a resposta pode ficar confusa.

02:28

Se o chunk tiver só o tempo de resposta de 30 minutos,

02:32

sem dizer que isso é parte do P1 Enterprise,

02:35

por exemplo, também fica ruim. Por isso,

02:38

quando a gente fala em chunking,

02:39

a pergunta não é apenas qual que é o tamanho que eu coloco.

02:43

A pergunta melhor é, esse pedaço ainda carrega sentido sozinho?

02:49

Muitas vezes, chunking por estrutura funciona melhor do que chunking puramente...

02:55

por número de caracteres. Se o documento está em Markdown, títulos,

03:00

subtítulos ajudam bastante. Um H2, um H3 pode indicar uma seção lógica.

03:06

A gente pode quebrar respeitando essas seções e, quando necessário,

03:11

dividir essas seções grandes em pedaços menores. Também existe a ideia de overlap,

03:18

que é repetir uma pequena parte do conteúdo entre os chunks vizinhos.

03:23

Isso ajuda quando uma informação importante fica

03:26

Exatamente na fronteira entre dois pedaços.

03:30

Mas o overlap demais aumenta o volume, custo de embedding,

03:34

armazenamento e pode gerar duplicidade na resposta. Então,

03:38

ele precisa ser usado também com cuidado. Agora, além do conteúdo do chunk,

03:44

a gente precisa falar dos metadados. A gente falou sobre isso.

03:48

Metadado é tudo aquilo que ajuda a aplicação a entender de

03:52

onde aquele chunk veio e quando ele deve ser ou não usado.

03:57

No nosso projeto, cada documento já tem informações como tenant, product, plan,

04:03

doctype, version, status e visibility. Quando a gente gerar os chunks,

04:09

esses metadados precisam acompanhar cada pedaço.

04:14

Não adianta o documento ter metadata se o chunk

04:18

perde essa informação no meio do pipeline.

04:21

Lá na frente, quando a gente for buscar no PG Vector,

04:24

a aplicação precisa conseguir filtrar, por exemplo,

04:28

apenas documentos publicados, apenas documentos para o produto correto,

04:33

apenas do tenant correto ou apenas de um determinado tipo.

04:37

Isso ainda é mais importante ali em sistemas, vamos dizer, reais.

04:42

Imagina recuperar um chunk de um documento em draft ou recuperar

04:46

uma regra antiga ou buscar uma informação de um outro tenant.

04:50

O problema não é só qualidade da resposta,

04:52

é inclusive segurança, governança e confiança.

04:55

E aqui entra então o versionamento. O documento muda, política muda,

05:02

SLA muda, preço muda, regras comerciais mudam.

05:06

Se a base muda e o índice vetorial continua com chunks antigos,

05:10

o reg pode responder com informação desatualizada.

05:13

E isso é um dos erros mais perigosos,

05:15

porque a resposta pode parecer correta, pode trazer fonte,

05:18

mas a fonte pode ser uma versão antiga.

05:20

Então a ingestão precisa carregar informações de versão.

05:25

E mais para frente, também precisa lidar com fingerprint ou hash de documento.

05:30

A ideia é simples.

05:32

Se o conteúdo mudou,

05:33

o sistema precisa saber que aquele conteúdo precisa ser reprocessado.

05:37

Chunks antigos precisam ser substituídos pelos novos. Nessa fase,

05:42

a gente ainda não vai implementar toda a indexação automática,

05:46

mas a gente já vai preparar a estrutura certa.

05:49

Cada chunk precisa ser um identificador. O arquivo de origem,

05:53

a seção, os metadados do documento e,

05:56

idealmente, alguma referência para a versão ou o hash daquele conteúdo.

06:01

Percebe que a gente ainda nem chamou o modelo, ainda nem gerou embedding,

06:06

mesmo assim, várias decisões importantes já começam a aparecer.

06:10

Esse é o ponto central do RAG.

06:12

A qualidade da resposta começa muito antes da pergunta do usuário.

06:18

Ela começa na forma de como a base foi escrita,

06:20

depois passa pela forma de como os documentos são carregados,

06:24

depois como são quebrados e depois metadados que acompanham cada trecho.

06:29

Só então aí a gente chega em embedding,

06:32

retrieval e geração. No próximo vídeo, a gente vai colocar isso na prática.

06:36

A gente vai evoluir o nosso pipeline para gerar chunks com metadados,

06:40

preservando a origem do documento.

06:42

A sessão e as informações necessárias para que mais

06:45

para frente o retrieval consiga trabalhar de forma mais controlada.

## Resumo IA

[RESUMO_IA]