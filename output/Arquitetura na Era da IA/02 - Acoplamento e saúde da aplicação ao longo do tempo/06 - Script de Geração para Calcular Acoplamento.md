Módulo: Arquitetura na Era da IA\
Aula: [Script de Geração para Calcular Acoplamento](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18116)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, no vídeo anterior eu falei para vocês,

00:04

mostrei aqui para vocês um código de um sistema,

00:06

provavelmente tem um monte de coisa errada com esse sistema,

00:09

tem coisas que estão ok no sistema,

00:11

mas o ponto é como que eu, um desenvolvedor,

00:15

um arquiteto de software, consigo entender essas coisas melhor.

00:18

Então, primeira coisa,

00:20

aqui vai depender muito da linguagem de programação que você está utilizando,

00:23

das ferramentas que tem.

00:24

Eu estou utilizando o TypeScript e o TypeScript tem um cara chamado Mad,

00:29

onde ele consegue trazer para a gente as dependências de um sistema.

00:34

Ele consegue gerar um gráfico de dependências.

00:36

Quer ver? Eu gerei esse cara aqui. Você vai ter acesso a esse projeto,

00:41

então vai ficar mais fácil de você olhar. Então,

00:44

eu consigo ter acesso a um gráfico desse jeito.

00:48

Mas o problema é que, se eu olho isso, poxa,

00:53

é legal, mas parece que não faz sentido para mim.

00:55

Que decisão arquitetural que eu consigo ter olhando para isso aqui?

01:00

É muita informação.

01:02

Então, acaba sendo insano. Mas eu consigo usar esse cara e etc.,

01:08

e as informações dele para conseguir, eventualmente...

01:13

fazer uma conta simples de acoplamento aferente e eferente para

01:18

a gente começar a entender aquilo que eu trouxe para vocês,

01:21

tá? Então, vamos lá.

01:23

Eu tenho aqui um script que se eu der Node Scripts,

01:29

eu acho que é Coupling, aqui,

01:32

ele vai trazer algo, mas relaxa que a gente vai ver isso em gráfico, tá?

01:37

Mas eu preciso trazer para vocês aqui para você

01:39

entender de onde vieram as coisas do gráfico.

01:41

Então, se você olhar aqui, eu tenho CA aferente,

01:45

tá? Ou seja, quantos módulos importam esse aqui,

01:48

né? Quanto maior, mais dependem deles, é mais rígido. Quanto menor, né?

01:54

Ele depende de muitos, então ele é mais frágil. E a instabilidade,

01:59

né? É a fórmula que eu falei pra você.

02:00

CE dividido por C mais A. Quanto, se for zero, mais estável. Se for um,

02:05

mais perto de um, mais instável. Então, ele trouxe aqui, ó,

02:09

os tops caras eferentes. Então, se você olhar aqui, por exemplo, Order Service,

02:15

o acoplamento aferente dele é 3. Ou seja,

02:20

quantos módulos importam o Order Service?

02:23

Agora, se eu olhar aqui, o CE, que é o acoplamento eferente,

02:28

é 15. Ou seja, tem 15 caras importando ele.

02:35

Então, quer dizer, que ele importa, na realidade.

02:40

Então... O nível de instabilidade dele é 0,83. É alto. Por quê?

02:47

Porque ele depende de muita gente.

02:49

E se alguém desses 15 caras mudar, ele pode quebrar.

02:54

Se eu olhar aqui o server.ts,

02:58

o acoplamento aferente dele é zero. Ou seja,

03:03

ninguém depende dele. E ele depende de... Vários caras.

03:09

Isso aqui é uma classe Deus, praticamente,

03:11

né? Tudo está sendo chamado para ela. Faz sentido?

03:15

Ele é o service, ele é o server, ou seja,

03:18

ele executa, ele tem os handlers, ele tem o controle,

03:22

importa tudo, importa banco de dados e etc.

03:24

Ou seja, é uma classe deus, né?

03:26

Mas extremamente frágil ali também. Então, quando você olha aqui,

03:30

você começa a ver, né? Aferente, eferente e o grau de instabilidade,

03:34

tá? Mas nesse caso, é os tops eferentes.

03:37

E aqui eu tenho os tops aferentes, onde todo mundo depende dele.

03:41

Então, se você olhar aqui, eu tenho os caras aferentes,

03:44

que todo mundo depende dele. E nesse caso,

03:47

a instabilidade dele começa a ser mais próxima a zero.

03:50

E daí vai subindo aqui para a gente.

03:52

Aqui também, eu pedi para ele trazer dependências circulares.

03:56

Ou seja, imagina que eu tenho aqui um inventory service,

04:02

que importa ali o notification.

04:06

O notification importa o previous order count,

04:11

que importa o order service,

04:14

que importa o inventory service de novo. Ou seja,

04:18

eu tenho um ciclo aqui que esse cara está

04:22

sendo chamado de novo dentro desse mesmo fluxo.

04:25

Então, isso é uma dependência circular.

04:27

Isso aí acaba sendo muito ruim em muitos aspectos.

04:31

Então, ele tem aqui quatro dependências.

04:35

circulares, tá? Então isso aqui eu queria trazer e mostrar pra vocês primeiramente,

04:39

pra eu mostrar a conta clara em relação

04:43

a acoplamento aferente e eferente pra ficar mais tangível,

04:47

né? Essa parte aqui pra vocês,

04:50

tá? No próximo vídeo a gente já vai olhar isso de uma forma um pouco diferente

04:56

e eu acho que vai começar a fazer mais sentido prático pra você no dia a dia. Vamos nessa!

## Resumo IA

[RESUMO_IA]