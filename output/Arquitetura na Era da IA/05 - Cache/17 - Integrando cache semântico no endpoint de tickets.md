Módulo: Arquitetura na Era da IA\
Aula: [Integrando cache semântico no endpoint de tickets](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18353)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, seguinte, agora a gente está juntando os pontos,

00:06

porque antes a gente tinha o nosso cache para analisar os

00:09

tickets e a gente tinha toda essa história de o cache semântico,

00:14

as buscas que a gente fez em endpoints separados para

00:17

a gente entender bem como é que isso funcionava. Agora,

00:20

o que a gente vai fazer? A gente vai pegar o que a gente... tem agora de busca,

00:24

cache semântico e tudo mais,

00:26

e a gente vai colocar nesse endpoint do tickets / analyze.

00:30

E isso vai funcionar que nem uma cascata. Então,

00:33

o que acontece aqui? O que vai acontecer? Quando entrar uma pergunta,

00:38

entrar uma requisição aqui para a gente,

00:40

a gente vai ter três camadas aqui. Primeira camada, cache exato. Ou seja,

00:45

ele vai pegar e verificar se essa mensagem que

00:47

foi enviada é idêntica a uma mensagem anterior,

00:51

e que já foi respondida. Ou seja, o fingerprint é idêntico. Quando isso acontece,

00:56

ele já vai retornar o cache de volta. A gente tem uma segunda camada.

01:01

Caso não tenha esse cara aqui, a gente vai usar o cache semântico.

01:06

A gente vai ver a mensagem que ela é parecida o bastante e que

01:10

tem um threshold no pgVector acima do valor que a gente quer, que é o 0.9.

01:15

E caso a gente não tenha nenhum candidato a ser aceito aqui nesse cache semântico, o que acontece?

01:22

Nenhum cara serviu, então eu vou chamar a IA e vou guardar,

01:26

chamar o modelo e guardar o resultado. Esse guardar o resultado,

01:30

eu estou guardando de memória, eu não estou salvando ainda no banco de dados,

01:35

mas somente para você saber. Então, como é que funciona aqui?

01:39

Construir minha fingerprint, tudo o que a gente tinha feito antes. Então,

01:42

o passo 1 aqui é verificar se isso aqui já existe no cache exato,

01:47

ou seja, se o fingerprint é o mesmo. Então,

01:49

ele vai verificar se está no cache, se tiver,

01:51

eu vou falar aqui o source dele,

01:54

perceba bem o nome que eu estou colocando aqui, source exato cache, ou seja,

02:00

isso já existia na memória,

02:01

o fingerprint bateu e eu retornei esse cara aqui para mim.

02:05

Beleza? Então, isso aqui acabou.

02:08

Agora, a partir daqui...

02:10

a gente sempre vai garantir que vai ser um cache miss exato. Ou seja,

02:14

não tenho mais aquele cache exato porque a gente já saiu desse return agora aqui.

02:20

Então, o passo dois nosso aqui é o nosso cache semântico. Ou seja,

02:23

a gente vai fazer a busca no Postgres e a gente vai ver o

02:26

threshold para ver se ele tem o mínimo de similaridade que a gente está querendo.

02:31

Então, o que eu vou fazer? Um,

02:33

gerar um embedding das mensagens e buscar os

02:37

candidatos e avaliar o melhor deles contra o threshold,

02:40

beleza? Então, aqui eu vou fazer a minha avaliação,

02:43

onde eu passo a minha fingerprint e o threshold, e eu vou pegar o melhor,

02:47

o cara que tem a maior, a maior similaridade comigo.

02:53

E agora aqui... Qual que é a pergunta?

02:55

Se há um hit semântico e se o candidato for aceito,

02:58

o response JSON vai ser salvo e ele é válido.

03:02

Um item corrompido no banco pode derrubar a API.

03:06

Depois a gente trata isso como miss. Então, o que acontece?

03:09

Ele vai verificar se o cara que ele encontrou está aceito.

03:16

Tem aquela decisão se ele está aceito como cache.

03:20

Se for, o que ele vai fazer?

03:21

Ele vai pegar essa resposta desse melhor cara que

03:26

aconteceu e vai trazer a gente aqui,

03:29

vai preencher o nosso ticket de análise com aquela resposta lá preenchida.

03:33

Caso contrário, que tem algum erro,

03:37

ele vai dar que a decisão é rejected e falou que o

03:39

best match aqui é inválido ou teve algum problema com semantic miss.

03:45

E aqui, basicamente, é o bloco do cache da resposta,

03:50

que é exatamente o mesmo caminho que a gente dá um hit no cache semântico.

03:56

Então, basicamente,

03:57

eu trago se teve uma tentativa,

04:02

se ele deu o hit ou se não conseguiu dar o hit,

04:07

a decisão, se foi accepted ou não, o motivo.

04:11

O threshold que foi utilizado e aqui a similaridade, a distância,

04:16

o ID do cara e o input do texto que acabou trazendo.

04:20

Então, aqui é o bloco que a gente vai trazer no caso do cache semântico.

04:25

E agora aqui, basicamente, o candidato foi aceito e é válido. Então,

04:30

eu vou reaproveitar a resposta que foi salva sem chamar a IA.

04:34

Então, nesse momento é, eu tive o semantic result, ele não é em branco?

04:40

O que eu vou fazer? Eu dei um cache hit, certo?

04:44

Mas o cache hit que eu dei foi um semantic cache. Ele não foi exato,

04:48

porque eu fiz a busca no banco de dados, vi os candidatos,

04:52

peguei o meu best match, vi que esse cara passou do threshold,

04:55

ele passou do threshold, então peguei a informação dele, vi que eu tive a resposta,

05:02

e aí eu vou retornar esse cara aqui. A IA foi chamada? Não foi chamada,

05:08

porque a gente fez busca no banco de dados.

05:10

E a gente retorna ali a nossa requisição.

05:13

Agora, o que acontece?

05:14

A gente tem a situação que no cache semântico a coisa também não deu certo.

05:20

Ou seja, ele não encontrou nenhum cara no cache semântico.

05:23

Então, o que vai acontecer? Eu vou chamar a IA aqui para mim,

05:27

certo? Então, eu estou dando um invoke ali com o LangChain.

05:30

Somei uma chamada e vou guardar essa chamada no meu cache local.

05:37

Eu não estou salvando ainda no banco de dados. Preste atenção,

05:40

galera. Então, eu estou salvando ele, a fingerprint dele,

05:44

ali na minha memória. Não estou salvando no banco de dados ainda.

05:48

De qualquer forma, ele vai dar um cache miss.

05:50

E você vai perceber, então, que como ele deu um cache miss,

05:55

ele vai trazer o resultado,

05:57

mas teve que chamar a IA aqui para a gente.

05:59

E aí você vai ver que o source é AI model. Então, eu tenho três sources.

06:04

AI model, quando eu tive que chamar a IA. Eu tenho semantic cache,

06:07

quando eu tive que fazer a busca no banco de dados e consegui,

06:12

e eu tenho o exec cache,

06:15

que é quando ele pegou da memória o fingerprint

06:17

e bateu exatamente como é que ali funcionou.

06:21

Então, o que acontece? Se eu chegar agora aqui no meu teste .http,

06:24

eu posso ter os meus pontos aqui.

06:29

Deixa eu dar um Enter aqui, vamos lá. Tenho dúvidas sobre cobrança, pode me ajudar?

06:34

Então, mandei aqui uma request aqui para esse cara, e ele deu um cache miss,

06:39

a IA foi chamada. Ou seja, semantic cache foi rejeitado,

06:43

a similaridade deu 0.4, o threshold é 0.9, chamou a IA sim,

06:49

teve uma chamada da IA, e a categoria foi billing aqui para mim.

06:54

Agora eu vou fazer uma segunda chamada,

06:57

e nesse caso tem que retornar como exec cache. Então,

07:00

porque a pergunta é exatamente a mesma.

07:02

Então eu vou dar um Send Request, e aqui, olha só.

07:06

Cache exato, a IA não foi chamada, tenho dúvidas,

07:09

não chamou a IA, então ele bateu direto. Por quê?

07:13

Porque a primeira vez ele chamou a IA,

07:14

e depois disso ele guardou essa chave ali para a gente.

07:20

Aí nós temos a outra situação, que eu vou incluir o embedding ali no banco de dados.

07:27

Aqui eu consigo olhar meu config, eu consigo ver que tem o meu banco de dados,

07:31

consigo ver que o meu status no meu banco de dados está tudo ok.

07:36

E agora aqui eu posso criar os itens semânticos aqui, né?

07:40

Que é como que eu cancelo a minha assinatura.

07:43

Eu tenho um cara que eu vou criar um outro

07:45

cara manual que é quero cancelar meu plano.

07:47

Está aqui também. E eu vou criar uma busca.

07:52

Aqui eu tenho aquela minha busca do cache semântico, né?

07:55

que a gente fez ali no passado, mas agora, o que acontece?

08:01

É o seguinte, quando a gente vai fazer as nossas análises dos tickets,

08:06

olha só o que vai acontecer. Eu tenho aqui, preciso cancelar o meu plano. Então,

08:13

eu vou dar um Send Request, e olha só, semantic hit e a não chamada.

08:19

O que isso significa? Ele não tinha o fingerprint na memória, mas ele...

08:25

conseguiu buscar no banco de dados,

08:27

viu que a similaridade era de 0.94, ou seja, foi aceito,

08:32

a IA não foi chamada e eu tive o cache hit. Mas o cache hit não foi na memória,

08:38

foi por similaridade ou foi por busca semântica ali no nosso caso.

08:43

Se eu coloco aqui, preciso cancelar meu plano agora aqui,

08:46

mas olha só o que eu vou fazer.

08:48

Está vendo o threshold que eu vou colocar? Eu vou colocar de 0.99.

08:53

Então, o threshold é ali altíssimo agora.

08:55

E agora eu vou mandar a mesma pergunta. Preciso cancelar meu plano.

09:00

Olha o que vai acontecer.

09:02

Ele deu um cache miss na chamada. Por quê? Porque o cara,

09:06

o semantic cache, deu como rejeitado. Porque a similaridade dele era 0.94.

09:13

E o threshold que eu tinha colocado aqui era 0.99. Então,

09:17

ele teve que chamar de novo a IA para trazer a resposta ali que eu estava querendo.

09:23

Então, essa aí é a grande diferença, galera.

09:27

Você viu que conforme eu mudo a régua,

09:29

ele vai trazer ou não a resposta ou ele teve que chamar a IA ou não.

09:34

Agora, uma coisa somente para lembrar para você é que

09:37

no momento que eu fiz essa busca agora aqui...

09:40

Eu não salvei isso no banco de dados, esse resultado no banco de dados.

09:44

Só estou salvando ali na memória. Então,

09:47

lembrando as camadas que eu tenho. Eu tenho a memória,

09:49

nesse nosso caso, eu tenho a IA, a chamada,

09:55

E eu tenho a semente que também.

09:57

Nesse caso, ele chamou a IA,

10:00

mas o semantic cache não foi, como se diz...

10:06

gravado no banco de dados ainda,

10:08

A gente vai fazer isso nos nossos próximos vídeos. Vamos nessa!

## Resumo IA

[RESUMO_IA]