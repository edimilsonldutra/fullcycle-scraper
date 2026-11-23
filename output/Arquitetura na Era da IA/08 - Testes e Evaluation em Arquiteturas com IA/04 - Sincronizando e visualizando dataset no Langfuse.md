Módulo: Arquitetura na Era da IA\
Aula: [Sincronizando e visualizando dataset no Langfuse](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18783)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior eu mostrei para vocês a estrutura do nosso dataset e tudo mais,

00:06

e aqui eu só queria mostrar na realidade a integração entre o Aço,

00:10

a sincronização com o LangFuse. Então se você olhar aqui,

00:13

eu tenho o nome do meu dataset, a descrição,

00:15

eu tenho o caminho onde ficam os meus arquivos,

00:18

os meus casos aqui,

00:20

aqui basicamente o modelo de como fica o

00:24

meu data model com todos os meus campos.

00:27

Ele vai carregar, beleza, load cases, ele vai validar o dataset,

00:31

que foi o que a gente acabou fazendo,

00:33

mas aqui nesse vídeo eu queria falar mais sobre esse cara,

00:36

que é o nosso sync dataset.

00:37

Esse sync dataset, o que ele vai fazer? Ele vai fazer a autenticação lá no Langfuse,

00:43

inclusive se ele não conseguir, ele vai dar um erro,

00:45

e aqui ele vai rodar um create dataset.

00:48

Nesse create dataset, a gente tem um loop. E para cada item daquele JSON,

00:54

ele vai passar lá o dataset name,

00:56

o ID daquele case, a pergunta e a resposta esperada.

01:02

Isso aqui é um ponto importante, tá? Por quê?

01:05

Porque a gente vai pegar aquelas informações e quando

01:09

a gente coloca ali como resposta esperada,

01:12

quando nós formos rodar qualquer teste ou experimento em relação àquele dataset,

01:18

eu tenho isso aí como ponto da verdade.

01:21

Ou seja, qualquer coisa que a IA responder, ela tem que,

01:24

de forma geral, bater com o que eu estou esperando.

01:26

Então, é uma forma de eu fazer aqueles meus testes semânticos. Então,

01:30

quando eu for rodar qualquer coisa contra a IA, o meu ponto de referência,

01:33

no final das contas, vai ser esse caso onde eu tenho essa expected output.

01:40

E eu tenho aqui tags com os meus metadados,

01:42

normalmente, caso ele produza. Então, depois disso, eu dou um flush.

01:46

E tudo mais, se eu tenho validate only,

01:48

ele não vai fazer o sync ali para a gente. Então,

01:51

se eu chegar aqui e rodar... Cadê o meu camarada? Evolve o dataset, o

01:59

que vai acontecer? Olha só,

02:00

ele fez a validação e agora ele pegou o nome do

02:04

dataset e fez o sync lá com o meu Langfuse. Então,

02:08

se eu acessar o meu Langfuse de forma geral...

02:15

eu tenho aquele meu projeto que eu tinha antes, que é

02:18

o FCIA e o FCIA RAG, mas se você olhar aqui,

02:24

no menu aqui do Langfuse, o Langfuse é muito grande, né?

02:28

Mas normalmente, sei lá, em módulos, em momentos anteriores,

02:32

a gente pode ter falado de prompts ou qualquer coisa desse tipo,

02:34

ou da parte de tracing, mas aqui a gente está focado principalmente em avaliação.

02:38

Se eu for em datasets, você vai ver que ele está vazio.

02:41

Eu posso criar manualmente ou posso fazer isso via API.

02:45

Então, na hora que eu faço isso via API, deixa eu dar uma atualizada agora aqui,

02:49

ele vai trazer aquilo que a gente subiu. Um ponto importante é a independência.

02:54

O que isso significa no final das contas?

02:56

Eu posso rodar isso quantas vezes quiser.

02:58

Ele não vai duplicar. Ele vai alterar os dados existentes.

03:02

Isso é importante para você manter o seu dataset consistente. Ele pode ir crescendo,

03:06

você pode adicionar casos, mas você não destrói nada aqui em cima.

03:10

E aí, quando eu clico nesse dataset, eu vou ver aqui os meus itens.

03:16

Então, eu tenho o ID do meu item.

03:20

Uma dica que eu dou,

03:22

você pode usar normalmente os IDs com prefixos

03:26

referentes à intenção do que você tem naquele momento.

03:31

Então, por exemplo, eu tenho ambíguo, ou seja, são perguntas ambíguas.

03:34

As perguntas negativas, a pergunta, nesse caso, sobre as empresas,

03:40

pergunta sobre o produto. Então, a parte sobre billing, sobre plano,

03:44

sobre SLA e tudo mais. Então, você acaba separando. E nesse caso aqui,

03:49

você vai perceber que eu tenho input e o expected output.

03:54

Então, se eu entro nesse cara aqui, vamos lá,

03:57

o que eu tenho? A pergunta e o output que eu espero,

04:01

por exemplo, da minha IA seja essa.

04:02

E os metadados são esses caras aqui que eu estou trazendo. Metadados, no caso,

04:07

são tags que são importantes aqui para mim que eu vou trabalhar.

04:12

Então, no final das contas aqui, eu tenho tudo isso.

04:16

Colocado bonitinho aqui para mim nesse meu dataset. E aí,

04:20

uma vez que eu tenho isso registrado, aí que a coisa começa a fazer mais sentido,

04:25

porque a gente tem essas informações para trabalhar.

04:28

Inclusive, a dica que eu dou é assim, quando a gente está desenvolvendo,

04:34

a gente está muito acostumado a trabalhar e sair desenvolvendo, programando.

04:40

Utilizando IA hoje em dia e tudo mais. Mas o grande ponto aqui,

04:44

que você sempre tem que pensar, é o seguinte.

04:46

Uma das coisas mais importantes para que tudo isso funcione é até...

04:50

muito bem feitos, tá? Então,

04:53

e ter esses datasets muito bem feitos é algo complexo, ainda mais quando você tem,

04:59

sei lá, um agente que faz muita coisa, né?

05:02

Ou um agente responde coisas extremamente variadas,

05:06

mas mesmo que seja no mesmo escopo. Então,

05:08

criar esses datasets é tão importante quanto você

05:12

programar e rodar os testes em cima,

05:15

tá? Então, eu tenho esse dataset com esses itens, mas assim,

05:20

eles estão consistentes,

05:22

eu fiz bastante verificações para fazer sentido na hora da

05:25

gente rodar as aulas aqui do nosso curso,

05:29

mas saiba que no dia a dia,

05:31

esses datasets, eles podem ser bem grandes, eles podem ter muita informação,

05:36

tem que ser feita de uma forma extremamente intencional, então assim,

05:40

não ignorem isso, porque um dataset mal feito faz com que...

05:45

todo o resto acabe desencadeando. E eu vou te dizer,

05:48

na maioria dos casos que eu peguei aqui e que eu pego nos meus projetos,

05:52

às vezes eu gasto 80% do tempo criando ou tendo um dataset muito bom,

05:58

então tem que falar com gente da área de produto, tem que entender, sei lá,

06:01

com alguém na área de vendas, pegar o histórico de um CRM e ver como é que, sei lá,

06:07

a sua equipe de suporte estava respondendo e aí como que você quer trabalhar,

06:12

por exemplo. Então, isso aí.

06:14

é um ponto extremamente importante e eu espero que você leve isso em consideração.

06:19

Tá? Eu faço questão de frisar,

06:21

qualidade do dataset, ele é tudo basicamente quando a

06:25

gente vai trabalhar com esses tipos de testes,

06:27

evaluation e etc, beleza? Então tá aqui nosso dataset,

06:32

vamos seguir aí com os próximos passos.

## Resumo IA

[RESUMO_IA]