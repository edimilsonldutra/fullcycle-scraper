Módulo: Arquitetura na Era da IA\
Aula: [Gerando Gráfico de Acompanhamento](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18117)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, no vídeo anterior eu falei para vocês de acoplamento eferente, aferente,

00:06

a gente viu esses números aqui e é muito bonito ver números,

00:09

mas e no dia a dia? O que eu vou fazer agora aqui?

00:12

Então eu preciso entender um pouco melhor,

00:15

lembra que eu falei para vocês em relação à main sequence e etc,

00:19

onde a gente tem uma linha... que, basicamente,

00:22

quanto mais perto a gente estiver dela,

00:24

mas a gente tem um equilíbrio ali entre acoplamento e abstração, né? Então,

00:29

isso aí é muito útil pra gente ver. E eu tenho,

00:33

e fiz um script aqui também, que pode, normalmente,

00:37

também virar uma skill. E lembrando, né?

00:39

Cada linguagem de programação, o script, na realidade,

00:42

ele acaba sendo diferente, né?

00:44

A não ser que você peça pra IA fazer isso de uma forma...

00:50

sem ser determinística, ela vai conseguir fazer isso,

00:54

mas vai gastar token pra caramba porque ela vai abrir todos os arquivos.

00:57

Então eu recomendo que você faça isso de forma determinística, através de scripts.

01:02

Você vai pedir pra IA gerar pra você o script pra ficar

01:06

mais fácil e você pode ter uma skill que você pode pedir,

01:11

olha, eu quero o gráfico de...

01:14

de acoplamentos e eu quero que você compare a melhoria desse gráfico com

01:19

o da semana passada de acordo com as mudanças que eu tive no Git.

01:23

E aí a gente consegue ter a IA nos ajudando nesse processo,

01:26

tá? Mas é muito claro que dependendo da linguagem é a forma de você verificar,

01:31

tá? Não recomendo que você peça para a IA sair olhando tudo.

01:35

Você pode, mas você vai gastar mais token e vai demorar mais.

01:38

A gente tem formas de trabalhar com script determinístico para resolver. Então,

01:42

eu estou trabalhando dessa forma. Se você já trabalha dessa forma,

01:46

utilizando o próprio LLM, ela avalia e etc., vai funcionar também.

01:50

Mas é importante que você saiba que, dependendo da história,

01:55

trabalhar de forma determinística acaba sendo mais fácil.

01:58

E você pode usar da IA para fazer essa geração de script.

02:03

Esse script que você está vendo aqui,

02:05

eu pedi para a IA gerar para mim. Beleza? Então, basicamente,

02:08

foi isso. Bom, chega de conversa. Vamos olhar esse gráfico, tá?

02:13

Eu vou passar uma introdução e depois a gente entra com

02:16

ele um pouco mais a fundo ali pra gente, tá?

02:19

Eu peguei esse gráfico e eu coloquei aqui no

02:21

meu navegador pra ficar um pouquinho melhor,

02:23

tá? Então, basicamente, tá? É um mapa de acoplamento dos nossos módulos.

02:28

Cada ponto é um módulo do sistema. E daí, módulo...

02:33

Vai depender muito de como você quer trabalhar.

02:36

Ou se um módulo para você pode ser uma classe.

02:38

Então, um módulo, componente, depende muito de como a semântica que você utiliza.

02:43

E aqui, a gente combina, no final das contas, duas medidas.

02:47

Num eixo, a gente tem, no eixo vertical,

02:50

a gente tem, basicamente,

02:54

a parte de abstração. Então, o A nosso, que é a abstração.

03:00

Aqui vai para algo concreto e para cima algo mais abstrato.

03:06

Então, basicamente assim,

03:08

A gente vai nesse cara. Então,

03:10

Esse eixo aqui, vertical, é sobre abstração.

03:16

Já no caso, no eixo horizontal, a gente tem instabilidade,

03:23

que a gente vai de estável para instável. Então,

03:26

quanto mais estável a gente está desse lado,

03:29

quanto mais instável a gente está desse lado aqui. Ou seja,

03:33

a instabilidade vai do estável para o instável,

03:36

a abstração vai do concreto para o abstrato.

03:39

E se você olhar aqui no nosso gráfico,

03:42

a gente tem essa linha que é gerada aqui para a gente.

03:46

Essa linha é a famosa Main Sequence,

03:48

que no final das contas é um gráfico plotado usando a

03:52

fórmula de A mais I é igual a 1.

03:55

Basicamente é isso. E esses pontos que a gente está vendo aqui,

03:59

e eu vou trazer para vocês aqui no próximo vídeo com um pouco mais de calma,

04:03

para esse vídeo não ficar gigante,

04:04

é onde a gente tem aqui as nossas classes, os nossos componentes,

04:08

e a gente começa a entender de onde está cada componente e

04:13

o que a gente pode fazer no meio de tudo isso para...

04:18

a gente melhorar o nosso sistema ou entender o nível de

04:21

acoplamento que ele tem para criar um plano de refatoração,

04:23

para a gente, inclusive,

04:25

ter uma noção do que está acontecendo e, o mais interessante,

04:29

colocar isso na prática tentando mudar essas bolinhas de lugar. Então,

04:33

vamos fazer isso aí no próximo vídeo e entender um pouquinho melhor.

## Resumo IA

[RESUMO_IA]