Módulo: Arquitetura na Era da IA\
Aula: [Instrumentando o pipeline com OpenTelemetry - PT2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18752)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente viu os tracings aparecendo,

00:06

mas olha só que interessante, tá?

00:08

Eu já vou forçando aqui com variável de ambiente

00:09

que fica ficando até mais fácil de a gente visualizar.

00:15

Eu vou mandar aqui que observability está enabled,

00:19

os traces exporter está como console, para aparecer no console,

00:23

mas eu estou colocando aqui o no re-rank para ele não fazer a etapa de re-ranking,

00:28

tá? E agora, o que acontece no meio da história?

00:32

Quando eu faço aquela minha pergunta, aqui,

00:35

qual é a SLA, o que vai acontecer?

00:38

Ele vai trazer tudo aquilo que eu já tinha colocado ali para a gente.

00:42

Porém, se você olhar,

00:44

você não vai ver mais o re-rank aqui. Por quê?

00:48

Porque ele pulou essa etapa e uma vez na hora que ele pula essa etapa,

00:52

simplesmente isso não vai ser, porque acabou não passando por isso.

00:58

Então, esse aí é um ponto. Por outro lado,

01:01

deixa eu dar um CTRL C aqui, eu posso,

01:04

nesse caso, passar,

01:06

por exemplo, uma mensagem

01:12

colocando, por exemplo, o token da OpenAI errado.

01:18

E aí, nesse caso,

01:20

o que acontece no final das contas quando eu vou trabalhar dessa forma?

01:25

Deixa eu dar um enter aqui para a gente. Então,

01:29

eu tenho o meu chat totalmente normal aqui para mim. Mas o que acontece?

01:35

Eu vou botar aquela minha pergunta base.

01:38

E a gente sabe que a gente está com o token da OpenAI errado.

01:42

E agora, espera um pouquinho. O que ele está dando aqui? Vamos lá. Vamos lá. Chat started.

01:52

Qual é o plano da OpenAI? Ele está falando que está inválido. Espera um pouquinho,

01:56

que eu acho que é por conta do espaçamento. Espera aí.

01:59

Aqui, observability. Ah não, está certo mesmo. Acho que é isso mesmo. Aqui.

02:08

Vamos lá. Eu quero mostrar para vocês o seguinte erro,

02:12

o seguinte problema. Olha aqui.

02:14

Quando ele cai no reg do pipeline em si, o que vai acontecer?

02:20

Você vai ver que eu tive aqui como status, error.

02:25

e a descrição que eu tive um problema de autenticação. E depois tudo deu errado,

02:29

porque a minha aplicação não está tratando bonitinho lá, olha,

02:32

se a OpenAI estiver errada, dá uma resposta bonita para o usuário.

02:35

Mas o ponto aqui que eu queria mostrar para vocês é

02:38

que quando nós temos uma etapa ali com um problema,

02:41

você vai perceber que isso aqui acaba se expandindo no meio da história,

02:46

porque ele precisou do query planning para fazer o planejamento,

02:49

eu tive um erro de API.

02:52

para tentar fazer o Pipeline Reg rodar,

02:55

que é o guarda-chuva principal, o que acontece?

03:00

Ele teve erro de autenticação ali também. Então, aqui a gente consegue,

03:05

de forma geral, mostrar que o quê? Que quando você também tem problemas,

03:11

você também acaba tendo esse tipo de informação,

03:16

porque você consegue acabar trabalhando.

03:20

Agora... Uma coisa que é interessante

03:23

é que se eu trabalhar com erro,

03:28

É importante que os meus erros estejam ali trabalhando tudo certinho.

03:33

O único ponto que nós temos que perceber no meio de

03:36

tudo isso é que nós temos que ser intencionais

03:40

para que a gente consiga adaptar a utilização dessas bibliotecas

03:44

dentro da nossa aplicação com o que a gente quer. Ou seja,

03:49

cada etapa da minha aplicação tem que ser

03:52

importante e intencionalmente marcada como um span,

03:55

como uma fatia que eu quero observar.

03:57

Às vezes você não quer observar de uma forma tão granular,

04:01

então você não precisa ficar criando um span para cada pedacinho do seu software.

04:04

Mas às vezes faz muito sentido e nesse ponto é

04:08

importante saber o que você vai querer medir. Fechou?

## Resumo IA

[RESUMO_IA]