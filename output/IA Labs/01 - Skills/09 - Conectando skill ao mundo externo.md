Módulo: IA Labs\
Aula: [Conectando skill ao mundo externo](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18275)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal. Então, dando continuidade aqui, vamos imaginar o seguinte.

00:04

Agora que a gente tem nosso Pendency Create aqui com um script,

00:10

vamos imaginar que eu quero agora adicionar a minha questão de referências, tá?

00:15

E fazer com que eu extraia aquela política e

00:19

faça com que aquela política seja jogada em uma referência.

00:22

O que eu tenho que fazer? Eu vou pedir,

00:25

então, para alterar a minha esquina. Na prática,

00:30

Vai ser dessa forma.

00:32

Analise passo a passo a

00:35

skill existente chamada Tenancy Page.

00:43

Atualmente a política, vou

00:48

dar uma olhada aqui, como está sendo o nome de classificação. Está

00:55

dentro do skill .md.

00:59

Seguindo as práticas,

01:03

faça

01:06

referência, crie diretório.

01:10

reference que

01:13

gere um arquivo específico de referência. Após isso,

01:20

atualize skill .md contendo essa referência e

01:28

vamos ver o que vai acontecer.

01:30

Então, a partir de agora, o que nós estamos fazendo aqui? Nós estamos usando

01:36

e abusando o lado progressive disclosure.

01:40

Então, vamos ver o que vai ser aqui. O resultado.

01:46

Vou mover as minhas classificações lá para dentro de reference.

01:51

Aparentemente, vai dar certinho. Já está criando aqui.

01:54

Perfeito. Vamos só verificar se ele vai fazer a referência dentro do nosso skill.

02:01

Porque, afinal de contas, se eu tiro daqui,

02:04

eu tenho que fazer o update do meu skill .md linkando com a minha referência.

02:08

Vamos dar uma olhada aqui.

02:11

Show de bola.

02:14

E vamos ver.

02:17

Qual foi o resultado? Temos aqui. Reference. Perfeito.

02:23

E aqui. Deixa eu ver. Se a gente tem.

02:27

O nosso link. E temos sim. Está aqui. Reference.

02:31

Classification. Policy. Perfeito.

02:35

O que a gente vai fazer? Vamos rodar.

02:40

E ver. A nossa skill rodando. Para a gente ver. Qual vai ser. O resultado atual.

02:47

Está aí. Nosso resultado. E conforme a gente pode perceber,

02:52

Está bem coerente com aquilo que já havíamos visto, né?

02:56

Vamos só ver o que vai ter aqui de baixo e também das nossas recomendações.

03:03

Tô de bola. Perfeito, pessoal. Então, até aqui, tudo certo.

03:06

O que a gente vai fazer a partir de agora?

03:08

Agora que nós temos aqui uma skill N3 com referência,

03:12

script e o nosso skill .md, nós vamos adicionar algo um pouco a mais, tá?

03:18

Bom, como agora... Eu já tenho o processo de classificação acontecendo.

03:23

Eu tenho que jogar isso aqui para algum lugar.

03:27

Afinal de contas, só classificar não faz muito sentido.

03:30

Preciso ter, de fato, uma ação para isso depois ser ajustado e tudo mais.

03:36

Então, o que a gente vai fazer? Eu vou vir aqui no Git.

03:41

Gerei este repositório.

03:45

Para esta demo, vou utilizar o GitHub CLI.

03:50

Podemos utilizar GitHub CLI,

03:53

podemos utilizar API do GitHub via Personal Token,

03:56

ou se você preferir também, podemos utilizar o próprio MCP do GitHub,

04:00

que através de Docker ou da própria instalação a gente consegue fazer o uso.

04:06

No meu caso, vou utilizar o CLI,

04:09

que acaba sendo algo que todo mundo já tem na

04:12

sua máquina e acaba sendo mais fácil de demonstrar para vocês.

04:17

Mas fiquem à vontade para escolher aquilo que... melhor,

04:20

com vocês. Então, o que eu vou fazer?

04:22

Como eu disse, criei um repositório,

04:24

vou agora botar essas informações dentro do meu repositório,

04:29

aquele projetinho e tudo mais, junto, inclusive, com o Cloud Skills,

04:33

e vamos rodar. Após isso, pego o relatório,

04:38

abro uma nova issue.

04:41

E, obviamente, quem vai fazer tudo isso vai ser a nossa skill.

04:48

Beleza? Então,

04:50

Vamos lá. Voltando aqui para o nosso VS Code, a gente vai fazer o seguinte.

04:55

Agora, faça a

04:59

seguinte alteração na skill.

05:06

Após o processo de classificação e

05:13

recomendação, utilize a

05:20

ferramenta GH GitHub CLI para...

05:29

Criar uma nova ficha contendo

05:33

todas as informações e recomendações.

05:38

O ponto importante aqui é que eu já estou logado no meu GitHub.

05:43

Então, a única coisa que eu preciso fazer aqui é, primeiro,

05:47

garantir que eu esteja logado, já com tudo certinho, e depois,

05:51

obviamente, jogar o meu projeto para o meu repositório remoto.

05:57

Que ainda não aconteceu. E a gente vai fazer isso logo mais. Então

06:02

dando continuidade aqui.

06:05

Pontos de atenção.

06:09

Relacionado a.

06:11

Idpotência. Ou dedup. Se a issue. Já existir.

06:21

Apenas atualize -a. E

06:28

se não existir. Será necessário. A criação.

06:35

Adicione isso como.

06:37

um novo passo da nossa skill.

06:42

Vamos ver o que vai acontecer.

06:46

Retornando aqui, pessoal, vamos dar uma olhada no que aconteceu.

06:50

Como vocês podem perceber, novamente, foi gerado aqui o

06:56

nosso skills.md, na verdade, atualizado.

07:00

E a gente pode ver que foi surgido mais um passo,

07:07

que é o passo 4.

07:09

E aí o que acontece? Primeiro ele faz aqui o processo de pré-checagem,

07:12

depois verifica se existe a issue, monta o corpo,

07:19

cria ou atualiza e confirma no chat.

07:23

Note que como eu não pedi nada referente à criação de scripts e tudo mais,

07:28

o que aconteceu? Ele veio para dentro da skill.

07:32

E aqui a gente já começa a falar um pouco de boas práticas, né?

07:37

E uma dessas boas práticas é tentar manter...

07:39

no skill .md o mais clean possível, o mais linear possível.

07:44

Quando eu digo linear, estou me referindo a, por exemplo,

07:48

aqui já tem a presença de bash, de gh

07:54

-cli, enfim, tem bastante coisa.

07:58

Tinha a parte de classificação, que agora a gente removeu,

08:01

jogou para as nossas referências. Então, com o tempo,

08:05

a gente vai vendo a necessidade também de refatorar as nossas skills mediante

08:10

o projeto que está evoluindo a todo momento, beleza?

08:14

Então, vamos lá. Primeira coisa, vamos dar um reload na

08:20

skill aqui bem rapidamente e vamos fazer um dependence create,

08:25

tá? Em contrapartida, no momento em que ele estava rodando aqui,

08:30

eu vou mostrar para vocês o meu browser,

08:32

que eu já fiz o meu commit lá para dentro do repositório, tá?

08:38

Retornando aqui no VS Code, vamos dar uma olhada de como que está indo.

08:42

Bom, temos aqui o resultado, tá? E aí tivemos de novo o mesmo resultado,

08:48

porém no momento da issue falou que não foi publicado. Isso porque, olha só,

08:53

temos aqui um programinha com o GitHub. E o que eu vou fazer?

08:57

Peguei lá a minha URL e já coloquei aqui

09:01

para que a gente consiga passar a nossa origem remota.

09:06

E aí, olha só, Já entramos, inclusive, na parte ali do dia a dia,

09:11

do processo de debugging, né? Então,

09:13

vimos que a skill foi feita, foi elaborada, porém,

09:16

caímos num pequeno erro.

09:17

Temos que corrigir e aí a gente vai utilizando os nossos artifícios,

09:22

tá? Nesse caso, apenas de demo,

09:25

vou passar o meu URL, beleza?

09:31

Criei o repositório,

09:34

já coloquei as informações lá e agora ele automaticamente...

09:39

Vai fazer a criação da minha issue. Vamos lá. Aguardando.

09:48

Bom, retornando aqui. E agora a issue foi criada com sucesso.

09:53

Só que se vocês repararem. Logo aqui em cima.

09:56

Vamos ver onde que está. Olha só.

09:59

Ela foi criada via std. Não foi via skills.

10:04

Mas apenas a cargo de demonstração. Se a gente vir aqui na issue.

10:09

A gente tem aqui a nossa triagem de acordo com aquilo que a gente viu ali no chat.

10:15

Para ser resolvido isso de uma vez por todas,

10:19

o que a gente tem que fazer? A gente tem que adicionar o seguinte.

10:24

Adicione na

10:26

skill uma

10:28

verificação. Deixa eu colocar qual o nome da skill.

10:36

Se não

10:40

existir a

10:42

origem remota, qual é a URL do GitHub?

10:49

Pergunte ao usuário. Utilize.

10:54

Ask tool. Antes

10:58

de. Realizar. O processo.

11:02

De criação. Da issue.

11:05

Garantindo sempre. Que. O repositório remoto. Exista.

11:13

Vamos ver. Qual que vai ser o resultado.

11:16

Show de bola. Aparentemente. Tudo certo. Para a gente fazer. O teste.

11:22

Vamos fazer o seguinte. Pessoal. Vou voltar aqui no meu browser. Vou.

11:29

Fechar. Esse carinha aqui.

11:32

E após isso, a gente vai voltar no VS Code e vamos rodar novamente. Só que,

11:39

para rodar novamente, eu vou aqui no outro Cloud meu,

11:44

no qual eu fiz o seguinte.

11:46

Eu peguei somente a minha skill, juntamente com o projeto,

11:50

e separei em um novo diretório,

11:54

naveguei até ele e agora abri a minha sessão de Cloud.

11:58

Com isso feito, vou gerar novamente.

12:02

E aí, como vocês podem perceber agora,

12:04

ele já me deu o resultado e já está publicando lá no GitHub.

12:09

Então, ele verificou, fez aquela verificação que a gente pediu,

12:13

viu que realmente existe,

12:14

viu que não tem nenhuma I.S.,

12:16

porque a gente deletou e agora vai publicar. Dessa forma, o que a gente fez?

12:21

A gente conseguiu incluir mais uma questão dentro

12:25

daquela própria skill que nós começamos.

12:27

Inicialmente, fazia muita coisa, depois... Passamos a fazer o script,

12:31

agora temos a referência e agora a gente tem o nosso contato aí com o mundo externo, né?

12:38

Para mostrar para vocês que também a gente consegue fazer desta forma, tá? Então,

12:44

voltando aqui, só para vocês darem uma olhada,

12:48

temos aqui novamente a nossa publicação, beleza?

12:54

Show de bola então, pessoal!

## Resumo IA

[RESUMO_IA]