Módulo: Arquitetura na Era da IA\
Aula: [LiteLLM na prática](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18291)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, quando a gente começou com os nossos exemplos,

00:03

a gente fez um experimento de trabalhar direto com o SDK da OpenAI,

00:07

depois a gente adicionou o Anthropic e a gente

00:10

viu a aplicação começar a virar meio bagunçada,

00:12

cheia de if e etc.

00:14

E agora... que a gente entende um pouco melhor sobre o LightLLM,

00:19

eu só queria dar um exemplo bem simples só

00:21

para constar de como que isso acaba ficando.

00:23

Então eu estou pedindo aqui para ele não usar frameworks,

00:26

não usar o LightLLM proxy, porque existe o proxy do LightLLM,

00:31

mas para ele trabalhar com o LightLLM aqui direto para a gente.

00:35

Então basicamente é isso que é o prompt, eu vou pedir para ele implementar agora.

00:40

Implemente arroba o prompt 0... O 3 aqui pra mim.

00:46

Vamos botar esse cara aqui pra funcionar.

00:51

E prontinho, ele implementou aqui pra gente.

00:55

Deixa eu diminuir um pouco o zoom disso aqui, galera,

00:57

para vocês conseguirem ver melhor. Mas aqui agora é o código atual, né? Então,

01:02

eu tirei aqui basicamente aquelas

01:04

implementações do OpenAI e da Anthropic,

01:11

coloquei apenas do LightLLM, né?

01:14

ele pega o padrão, ele só deixa um provider e etc.

01:18

para garantir que esses dados das variáveis de ambiente têm o prompt. E agora,

01:22

o que acontece é o seguinte,

01:25

ele está aqui nesse nosso caso fazendo um if sobre OpenAI e Anthropic por um motivo,

01:32

porque eu só tenho a chave dos dois.

01:34

Ou seja, aqui ele está validando as chaves se eu tenho.

01:37

É basicamente isso que acontece. Mas,

01:39

uma das coisas aqui bem interessantes também é,

01:44

ele está fazendo uma outra validação, que é o input do modelo.

01:49

Então aqui basicamente é validação do que esse cara está trabalhando.

01:52

Eu não precisaria ter absolutamente nada disso caso eu quisesse.

01:58

E eu estou dizendo isso por quê? Porque parece que o código nosso está gigante,

02:02

mas na realidade metade desse nosso código aqui é validação da

02:06

forma como que as coisas estão vindo aqui para a gente.

02:10

Mas é aqui que a coisa acaba ficando legal. Por quê? Olha só,

02:16

eu estou dando response completion, estou passando qual é o modelo, né?

02:20

E aqui eu tenho a pergunta e o resultado.

02:23

Posso passar temperatura, max tokens e acabou.

02:26

Ou seja, eu não estou mais agora preocupado,

02:31

na realidade, de ter

02:35

que ficar usando um SDK para cada coisa. Basicamente, o que eu fiz é,

02:40

eu escolho qual modelo que eu quero trabalhar e ele roda isso aqui para mim. Eu acho que,

02:44

não sei se ele instalou a

02:48

dependência do pip

02:52

install -r requirements.txt, a

02:59

dependência do LightLLM. Vamos lá.

03:11

E agora eu acho que vai.

03:15

Pronto. Então, se você perceber agora, o que acontece?

03:18

Eu estou fazendo a mesma coisa que antes, mas com o LightLLM,

03:23

agora eu não tenho que mais me preocupar com aquilo que eu estava antes.

03:27

Tá? Então, aqui tem a questão, o System Prompt.

03:30

Se eu quiser aqui, diminuir o meu código, aqui eu posso tirar essa validação,

03:37

eu acredito, eu acredito também que eu posso tirar esse cara aqui.

03:44

E aqui... Se eu quiser, modo input, esse

03:49

cara aqui, eu posso tirar esse cara aqui também, eu acredito.

03:55

Se eu quiser dar um build, se tiver modo input, o modo input é esse,

03:59

se não, ele coloca o provider ou esse. Então, eu vou colocar o modelo dessa

04:06

forma aqui e eu acho que vai rodar. E aqui o nosso try.

04:09

Vamos ver se esse cara funciona ou se eu removi coisa demais.

04:12

Aí vai funcionar. Então, se você perceber... O que acontece?

04:16

Eu tenho meu programa extremamente simples,

04:18

é só eu trocar minha variável de ambiente, mas agora,

04:21

se eu quiser adicionar o Gemini, se eu quiser adicionar quem eu quiser,

04:24

eu simplesmente mudo o modelo,

04:26

mas a minha interface é exatamente a mesma.

04:29

E é essa facilidade que o Lite LLM traz aqui para a gente.

04:33

Então, isso aqui mudou o jogo aqui para mim.

04:37

Essa única chamada, ela consegue suportar todos os modelos.

04:41

Mas novamente, não existe bala de prata,

04:44

nem todo modelo é igual, não pode ser tratado igual. O que esse cara faz,

04:49

ele tenta ao máximo padronizar a entrada e a saída.

04:53

Mas essa que é a ideia de a gente trabalhar, por exemplo, com o Lite LLM.

## Resumo IA

[RESUMO_IA]