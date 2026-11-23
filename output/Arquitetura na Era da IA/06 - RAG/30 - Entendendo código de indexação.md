Módulo: Arquitetura na Era da IA\
Aula: [Entendendo código de indexação](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18451)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, no vídeo anterior a gente falou sobre essa

00:05

reindexação e eu queria mostrar rapidamente aqui,

00:07

porque também não é nenhum bicho de sete cabeças.

00:11

Basicamente, se eu for no manifest.py, o que esse cara fez?

00:15

Ele tem o nome do nosso pipeline,

00:16

porque eu posso ter vários pipelines,

00:18

cada pipeline pode ter uma estratégia, tipos de documentos diferentes,

00:21

então vai depender muito de como quer trabalhar.

00:24

Eu defini aqui onde vai ficar gravado o arquivo de manifesto.

00:29

E aqui eu tenho uma função chamada DocumentHash,

00:32

que ele vai dar um

00:33

SHA 256 em

00:38

cima do documento,

00:41

ou seja, ele vai ser um documento único. Ele vai carregar o manifesto, ou seja,

00:45

ele vai basicamente ler esse cara.

00:49

Aqui eu tenho a função onde eu salvo esse manifesto.

00:54

Então, basicamente, esse arquivo apenas faz o hash.

00:57

E ele faz o carregamento do manifesto e ele salva o manifesto.

01:01

Basicamente é isso. Agora, o que muda realmente é aqui.

01:06

O nosso arquivo de ingestão, ele continua o mesmo, quase o mesmo. Então,

01:10

eu até ocultei aqui as funções que não mudaram, que a gente estava acostumado.

01:14

Mas agora, essa função do chunk document, ela mudou.

01:18

Por que eu estou dizendo isso? A gente está fazendo o splitter,

01:22

a gente está selecionando as seções. Na hora que a gente vai para cada documento,

01:26

Olha só que interessante agora.

01:28

Eu tenho os metadados que eu estou acostumado,

01:32

mas uma das coisas que você vai

01:36

perceber é que eu também agora adicionei um

01:43

document hash no meu metadado.

01:46

E na hora que eu faço isso, eu tenho o hash, inclusive,

01:49

do meu chunk ID. Lembra que o meu chunk ID, quando eu mostrei para vocês,

01:55

ele começa... com os caracteres iniciais do nosso hash, ou seja,

01:59

estou fazendo a relação do Chunk ID com o hash do nosso documento aqui também.

02:04

Então, isso aí é um ponto importantíssimo que a gente acaba trabalhando. Então,

02:09

esse é o ponto principal que a gente fez a mudança.

02:14

Então, quando a gente vai gerar os documentos, os Chunk IDs,

02:17

a gente está gerando esse hash. E na indexação, o que acontece?

02:24

Basicamente... A gente vai carregar os chunks, fazer toda a verificação,

02:30

ler os metadados e etc. Algo que a gente já fazia antes.

02:35

Fazer agrupamento por source file,

02:38

isso aqui a gente já meio que fazia também para ser os tipos de arquivo.

02:43

Mas agora aqui eu tenho alguns pontos importantes, que é o classify source. Ou seja,

02:49

eu tenho meus documentos e eu tenho os documentos indexados.

02:53

E aqui eu vou verificar.

02:55

Baseado nessas listas, quais foram novos, ou seja,

02:58

que estão agora aqui e que não estão no meu manifesto,

03:03

quais que foram mudados e aqui. Então,

03:05

ele está carregando esses caras aqui e esse ele vai fazer um loop, basicamente,

03:10

ou seja, ele vai entrar e vai bater os documentos que existem.

03:13

Se tem documento novo, ele dá um append.

03:16

Se o documento que já existia, o hash estiver diferente,

03:20

ele sabe que ele vai ter que fazer uma mudança. Se tiver tudo igual,

03:25

basicamente ele vai estar com o monchanger e se ele tiver sumido,

03:30

ele vai botar todos os arquivos que foram removidos aqui para mim.

03:34

Aqui verifica a tabela se existe, conecta com o banco de dados,

03:38

isso a gente já fazia antes. E aqui a gente tem o nosso manifest entry.

03:43

O que esse cara faz no final das contas?

03:45

Tudo que está no nosso manifesto, a gente precisa retornar.

03:49

O hash do documento, o título, o tenant, o produto, a versão,

03:52

o status e os IDs dos chunks que eu estou percorrendo. E esses IDs dos chunks,

03:57

eu já mudei eles, basicamente,

03:59

utilizando o hash

04:01

do documento principal. Então,

04:08

o chunk ID agora tem aquele hash do documento principal para trabalhar. E aqui,

04:13

para... particionar os dados. Basicamente, não mudou nada do que a gente fez.

04:19

O único ponto agora é que, na hora que a gente vai fazer a execução,

04:23

eu carrego o manifesto de tudo que eu já tenho e eu tenho um rebuild.

04:30

Rebuild, o que ele vai fazer? Ele vai, primeiro,

04:33

verificar se a tabela não existe ou se ele não tem nenhuma fonte de indexação.

04:39

Se não tiver a fonte de indexação, vai ser o quê?

04:43

Em branco. E aí, a gente vai rodar esse classify sources,

04:47

onde a gente consegue mostrar o resultado e, então,

04:51

simplesmente fazer o processo de reindexação.

04:55

Eu tenho um --force como argumento,

04:57

caso eu queira forçar a reindexação de todos, tá? Mas, de forma geral,

05:01

o que ele está fazendo é pegar cada documento e gerar a indexação,

05:06

colocando, inclusive,

05:07

no manifesto que a gente precisa, né? Uma vez que ele tem toda essa indexação,

05:12

joga no embedding, conecta no banco de dados e salva.

05:15

E aqui no final,

05:17

eu tenho um save manifest de todos os documentos

05:19

que eles passaram por esse processo aqui.

05:22

Então, é uma lógica simples,

05:24

obviamente ela está de uma forma bem if-else,

05:28

de uma forma que eu fiz de uma forma para ficar didático,

05:31

aqui passo a passo, mas a ideia simplesmente é,

05:35

se o negócio deletou, ele vai sair. Então, no final das contas,

05:39

a mensagem importante desse código é salvar os dados, bater com o manifesto,

05:45

salvar os dados do manifesto atualizado e depois fazer

05:48

um report pequeno aqui para a gente.

05:50

Então, essa que é a ideia, ou seja,

05:52

o nosso processo de indexação agora mudou.

05:56

Ele bate um manifesto, verifica mudanças, se tiver mudança,

06:00

ele faz as atualizações e depois salva novamente o manifesto com as mudanças,

06:05

caso necessário. Fechou?

06:06

Então, essa que é a ideia de como que a

06:09

gente trabalha com esse processo de indexação para que

06:12

a gente consiga manter um pipeline ativo para que a

06:16

gente não fique se preocupando em duplicação de dados,

06:18

manter dados desatualizados e coisas desse tipo aí.

## Resumo IA

[RESUMO_IA]