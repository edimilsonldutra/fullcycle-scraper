Módulo: Arquitetura na Era da IA\
Aula: [Entendendo o código do Rerank](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18447)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente viu a parte de re-rank funcionando.

00:05

E aqui eu tenho o meu re-rank.py, somente para você ver como é que a gente fez.

00:11

Se você olhar aqui,

00:12

eu estou falando que o meu re-rank vai pegar os quatro melhores aqui.

00:16

E aqui eu tenho o prompt. Você é um retrieval de re-rank,

00:20

você vai analisar os candidatos, você vai selecionar os... Os top 4 aqui,

00:25

vai escolher os chunks que ajudam na resposta direta, prefiro os chunks,

00:29

a gente já leu isso aqui antes.

00:30

E aqui estão os candidatos que basicamente vêm da busca vetorial.

00:35

E aqui tem o prompt onde eu grudo o prompt do re-rank,

00:38

ou seja, eu pego o prompt do sistema, coloco a pergunta do humano,

00:43

coloco a pergunta normalizada e coloco os termos exatos

00:47

para montar o prompt aqui para mim.

00:49

E no final das contas,

00:51

o Rerank Result é simplesmente os chunks

00:55

IDs que a gente tem para trabalhar.

00:58

Por quê? Porque ele já tem os chunks no final das contas.

01:01

Então, se você olhar,

01:03

ele vai selecionar os documentos por ID para pegar todos esses documentos.

01:07

Aqui é como eu formo os candidatos.

01:10

para eu ter os dados que eu queria, para a gente conseguir mostrar e fazer o append,

01:14

inclusive aqui. Então, basicamente, eu pego o chunk, o source, o title,

01:19

se tiver sessão, eu pego sessão, versão, que é o que a gente usa para conseguir,

01:22

inclusive, exibir, certo?

01:25

E aqui eu estou fazendo o re-rank dos documentos selecionados.

01:28

Basicamente é, eu vou pegar todos os documentos, certo?

01:32

E vou chamar, selecione os documentos por ID,

01:35

passando a lista, baseado nos chunks que eu tenho.

01:38

e pegar somente os quatro que eu queria aqui,

01:41

o re-rank top N que a gente tinha.

01:43

E aqui embaixo é somente a informação para a gente ter o debug.

01:46

No reg chat aqui, o que mudou agora?

01:49

Antes nós tínhamos o quê? O planner e o answer. Agora a gente tem o re-ranker aqui.

01:55

E o re-ranker, o que ele vai fazer? Eu tenho o cara que vai fazer o query plan,

02:00

que nem a gente fez. Aí a gente tem a busca, se não tiver resultados.

02:05

E agora aqui... eu faço um if se tem re-rank,

02:08

porque eu coloquei aquele menos menos no re-rank,

02:10

né? Mas basicamente o que ele faz? Ele pega o prompt, né?

02:15

Pronto ali, né? E monta aquele prompt baseado nas variáveis que a gente tem.

02:19

E se tiver show prompt, ele exibe, né? E aí ele dá um invoke aqui. E nesse momento,

02:25

é o momento que a resposta que eu tenho aqui é a resposta que vem do modelo.

02:29

E aí eu passo esses resultados aqui, né? aqui para dentro,

02:34

selecionando o quê? Os documentos re-ranqueados.

02:39

E aí, uma vez que eu tenho os documentos re-ranqueados, o que eu vou fazer?

02:43

Eu vou pegar o meu prompt, que realmente vai para o modelo agora,

02:47

que é o prompt de resposta,

02:49

e montar esse prompt de resposta baseado apenas

02:52

nos documentos que foram re-ranqueados.

02:55

Certo? E depois disso, eu exibo para o cliente final.

02:59

Então, basicamente, é isso que o Rerank faz.

03:02

Ele coloca uma camada no meio entre esses caras. No próximo vídeo,

03:08

eu quero falar alguns pontos importantes também sobre o Rerank.

03:12

Porque se você olhar aqui,

03:14

eu estou falando especificamente de utilizar o

03:21

Rerank fazendo uma outra chamada no modelo.

03:24

Então, se você perceber aqui,

03:26

eu estou fazendo três chamadas no modelo para cada pergunta que alguém fizer.

03:30

Ou seja, é bastante chamada. Dependendo da situação,

03:33

vale a pena. Dependendo da situação, pode não valer.

03:36

Mas o ponto importante é que existem trade-offs e,

03:40

eventualmente, a gente tem outros tipos de re-

03:42

-rank que eu queria comentar sobre eles.

03:44

A gente não vai ficar olhando um por um. De forma geral,

03:47

mas eu queria apenas comentar pra que você consiga entender

03:51

um pouco mais como é que esses caras funcionam,

03:53

pra você não achar que o re-rank é apenas feito chamando o modelo,

03:57

fechou? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]