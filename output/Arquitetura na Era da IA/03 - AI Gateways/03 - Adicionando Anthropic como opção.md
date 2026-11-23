Módulo: Arquitetura na Era da IA\
Aula: [Adicionando Anthropic como opção](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18287)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente viu, na realidade,

00:05

basicamente a implementação comum de uma chamada

00:10

e um chat completion chamado direto da OpenAI.

00:13

Agora a gente pode ter, na realidade, um segundo prompt que eu tenho aqui,

00:18

que é para fazer essa implementação no final das contas,

00:22

mas também com o modelo da Anthropic. Então, basicamente,

00:27

o que eu estou pedindo aqui é para adicionar

00:29

o modelo da Anthropic no meio dessa história.

00:32

Aqui não é 5.4, eu vou colocar aqui 4.1,

00:35

só para ele não gerar besteira. E, basicamente, é isso.

00:40

Então, eu vou pedir para ele implementar, implemente, arroba aqui o prompt 2,

00:44

e vamos ver esse cara trabalhar aqui.

00:49

Pra gente, tá? Então, a ideia principal agora, no final das contas,

00:53

é fazer com que ele coloque tanto o suporte pra OpenAI,

00:56

quanto o suporte aqui pra Anthropic, tá?

01:00

Então, vamos trabalhar aqui nessa,

01:05

vamos aguardar ele fazer a implementação, que de forma geral é simples, né?

01:10

Ele só tá adicionando ali no requirements o Anthropic e provavelmente vai

01:13

encher de if esse nosso main.py aqui pra gente.

01:19

Vamos lá, ele também criou as API Keys, AI Model, e

01:27

está mudando os nossos IFs aqui que a gente precisa. Está dando um instalar, e

01:35

eu acho que ele terminou de forma geral. Vamos ver aqui.

01:39

Então, basicamente, o que ele fez aqui, galera?

01:43

Ele está importando dois SDKs.

01:48

Pegou o provider, tem o mesmo system prompt e agora começa o if.

01:52

E agora que as coisas começam a trabalhar de uma forma meio que difícil,

01:56

porque se for OpenAI,

01:58

o grande ponto aqui é que ele vai

02:01

utilizar o SDK do OpenAI e perceba a assinatura,

02:07

client.chat.completions aqui para a gente. Agora,

02:11

se for utilizar o provider que é Anthropic, o que vai acontecer?

02:18

Na realidade, usar client.messages.create. Então,

02:21

a gente já começa a perceber que não há nenhuma

02:24

interface que deixe esses dois caras aqui parecidos de forma geral, tá? Então,

02:29

isso aí que a gente tem que acabar se tocando. Então, eu tenho aqui o meu ponto env,

02:35

por exemplo, onde eu tenho, tô falando provider Anthropic e o meu,

02:42

como se diz, o meu...

02:44

Meu cara aqui, o meu modelo é o CloudSonic 4.6.

02:48

E aqui, basicamente, eu consigo trocar, né? Então,

02:51

naquela hora eu estava rodando com o OpenAI,

02:53

agora aqui eu estou rodando com o Anthropic. Basicamente é isso.

02:57

Mas o aprendizado aqui não é você sair sabendo fazer uma chamada para IA,

03:02

né? Aqui, ele respondeu.

03:03

O ponto principal aqui é você entender o nível de perigo.

03:08

Eu não quero ficar chovendo no molhado, mas...

03:11

Eu acho que a principal aprendizagem aqui é, veja como que esses,

03:16

os SDKs, eles trabalham diferentes, têm recursos diferentes,

03:20

tá? E eu vou mais longe, tá? Se eu pegar aqui, o GPT 5.4 Mini,

03:26

ele mesmo entre si, 5.4 Mini.

03:33

Eu acho que é isso. Não preciso nem mudar aqui,

03:34

Se eu mudar as minhas variáveis de ambiente, né? Vou colocar aqui, OpenAI, GPT.

03:43

5.4-mini. Eu acho que é isso.

03:47

Olha só. Vamos ver aqui.

03:51

Olha o que aconteceu.

03:53

Esse modelo, que é da própria OpenAI, com o seu próprio SDK,

03:58

está dando erro para mim. Por quê? A versão de 5, ali para cima,

04:03

do 5.4, por exemplo, ele não tem o Max Token, basicamente.

04:07

Ele tem Max Completion Token, ao invés de Max Token. Então, dentro do próprio SDK,

04:13

ainda a gente já começa a ter os próprios problemas. Então,

04:15

a gente realmente precisa de uma interface que nos ajude,

04:18

inclusive, a evitar esse tipo de problema.

04:21

Fechou? Então, é isso, galera, que eu queria mostrar,

04:24

somente para a gente não ficar muito na teoria, e no próximo vídeo a gente continua.

## Resumo IA

[RESUMO_IA]