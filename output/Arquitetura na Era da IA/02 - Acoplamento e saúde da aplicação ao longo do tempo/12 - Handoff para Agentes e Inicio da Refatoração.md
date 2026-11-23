Módulo: Arquitetura na Era da IA\
Aula: [Handoff para Agentes e Inicio da Refatoração](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18122)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, o nosso agente aqui terminou e ele fez a instalação,

00:08

ele conseguiu verificar aqui também o nível de

00:13

cobertura em relação ao quanto que ele conseguiu trabalhar,

00:18

mas eu acho que o maior ponto importante aqui que ele deixou claro

00:21

aqui para a gente é essa nossa comparação de antes e depois.

00:25

Porque ele fez a implementação dessa rede de segurança

00:29

dos testes que a gente estava querendo,

00:31

né? Então, ele realizou a nossa tarefa A,

00:35

B e C aqui para a gente, mas ele não fez nenhuma refatoração,

00:39

né? Uma coisa interessante é que ele pegou edge cases,

00:42

que é o que eu tinha falado para vocês, né? E fez esse ajuste aqui.

00:46

A única coisa que ele fez uma ressalva, que ele vai ter que resolver depois,

00:49

é o teste que dá um skip em relação à parte de pagamento, tá?

00:54

Eu tenho algumas opções aqui, tá? Que eu posso fazer agora, tá?

01:00

Uma coisa eu poderia pedir pra ele já ir pra refatoração

01:04

ali do meu piloto e depois fazer a verificação,

01:07

tá? Mas eu vou querer

01:10

criar uma nova, uma nova, uma

01:16

nova janela, né? Uma nova sessão aqui pra mim. Tem,

01:20

tá? Só pra você saber, existe uma, uma

01:24

como que eu posso dizer, uma

01:27

skill que é chamada de handoff? Deixa eu ver se eu tô com ela aqui, ó.

01:31

Handoff. Eu acho que eu não tô com ela aqui.

01:33

Eu vou instalar essa skill aqui junto com você pra você ver.

01:39

Essa skill, tá?

01:41

E galera, só tô dando um exemplo, mais uma coisa que você pode aprender,

01:44

mas isso aqui não é obrigatório, tá? É muito mais algumas curiosidades.

01:49

Tem uma skill que chama handoff. Que é o mesmo cara que fez o Grilled Me.

01:52

Olha só, tem bastante gente, pelo menos nesse momento.

01:55

Eu vou copiar aqui e vou instalar essa skill aqui pra mim, tá?

01:59

O que que essa skill, ela faz no final das contas, tá?

02:05

Ela pega tudo que aconteceu naquela janela e faz,

02:09

e gera um arquivo aleatório,

02:12

onde nesse arquivo, tá? Tem tudo que aconteceu na sessão anterior,

02:18

como se fosse uma espécie, uma compactação,

02:20

mas pra você conseguir passar pro próximo agente,

02:23

tá? Então, a ideia ali no meio da história é,

02:27

eu quero passar o que aconteceu aqui para uma outra sessão, para um agente,

02:32

para não começar do zero. Como é que eu faço? Entendeu?

02:36

E aí, então, eu estou instalando aqui o handoff. Então,

02:41

essa skill ajuda bastante quando você não quer começar do zero totalmente,

02:45

você pode dar um handoff e aí você pode até focar, escolher o handoff,

02:50

passar mais detalhes ali. Então, eu vou dar um reload aqui, skills aqui para mim.

02:57

E agora eu vou dar um handoff aqui para mim.

03:02

Compactar a conversa para um outro agente poder conseguir trabalhar.

03:06

Então, eu vou colocar.

03:08

Ele pergunta, por que a última sessão vai ser utilizada?

03:12

Minha próxima sessão vai ser utilizada para fazer a...

03:16

Próxima sessão será

03:21

usada para fazer...

03:23

A refatoração

03:25

piloto conforme o

03:30

arroba plan.md.

03:33

E vou dar um enter agora aqui para mim. Então,

03:36

o que vai acontecer agora no meio da história?

03:39

Ele vai entender tudo o que aconteceu, porque ele tem isso no contexto.

03:42

Vai olhar também de novo o plan.md. E aí,

03:45

provavelmente, ele vai gerar um arquivo para mim,

03:48

temporário. E aí, nesse arquivo, ele vai trazer os detalhes.

03:53

que aconteceram nessa sessão, pra que na próxima eu não comece ela do zero,

03:58

tá? Então é basicamente isso que acontece.

04:00

Ele tá falando, inclusive,

04:02

que ele vai deixar o arquivo

04:03

na parte temporária do meu sistema operacional,

04:09

porque eu tô com bypass permission,

04:11

senão ele iria fazer dentro do meu container ou dentro ali do meu projeto,

04:15

tá? Então ele vai escrever agora esse documento, vamos aguardar um pouquinho aí.

04:23

Prontinho. Ele falou aqui do handoff que ele acabou de criar aqui pra mim.

04:28

Eu vou colocar aqui, traga o conteúdo gerado.

04:34

Só pra eu ver o handoff dele.

04:37

Obviamente que eu poderia dar um catch no caminho e eu mesmo pegar pelo terminal,

04:41

mas vamos colocar dessa forma mesmo aqui.

04:45

A gente já tá mexendo com a IA e eu

04:47

não tô nesse momento preocupado com os meus tokens, tá?

04:50

Nesse momento eu tô dando aula, tá, galera?

04:53

Token é algo que você sempre deve tentar economizar de forma geral, tá?

04:57

Então, vamos ver aqui o que ele vai colocar.

05:03

Bom, ele gerou aqui, ele trouxe aqui para mim o texto do Randolph.

05:09

Basicamente, é a compactação dele, né?

05:11

Próxima sessão, refatoração piloto, etapa D do Docs Plan.

05:15

Executar a fase D, especificação aqui,

05:17

princípio que rege tudo. Não esquecer,

05:20

rede de segurança trava o comportamento atual.

05:22

Estado atual, ele trouxe o estado atual,

05:25

arquivos novos e alterados, ele trouxe o plano de execução,

05:29

o RAID, ele vai trabalhar, por exemplo,

05:32

com o TDD, provavelmente, transformar o SKIP,

05:35

ele vai o GREEN, em relação a fazer passar o teste,

05:39

a verificação, depois o GREEN, armadilhas conhecidas,

05:44

que ele trouxe, as skills sugeridas, eu tenho o SUPERPOWERS,

05:49

aqui tem o Test Driven Development,

05:52

que é uma etapa explícita pra trabalhar com o TDD,

05:55

fazer os commits e etc, e etc, e etc. Comandos úteis. Então,

06:00

é isso que ele gerou naquele handoff, tá? Então, isso aí é interessante.

06:05

E o handoff, ele tá em qual arquivo que ele trouxe aqui pra gente?

06:08

Nesse caminho aqui, ó. Tá? Então, o que que eu vou fazer agora aqui nesse momento é,

06:14

eu vou dar um commit aqui pra mim, tá? Somente pra ele comitar a...

06:19

o que a gente criou aqui com plano e coisa desse tipo,

06:23

e ele também mexeu nos testes,

06:26

e ele também instalou, né,

06:28

A parte lá de cobertura de código também, mudou o package.json,

06:34

Então deixa ele fazer o commit ali pra gente.

06:38

Eu não tô trabalhando com múltiplos branches,

06:39

Mas pelo menos vamos comitar de uma parte pra outra

06:42

Só pra gente também não forçar a barra, tá?

06:46

Então, tá aqui feito. Agora o que eu vou fazer? Eu vou limpar essa seção, tá?

06:51

Então eu posso colocar baseado no end of e vou

06:57

passar o caminho do arquivo e no arroba plan.md,

07:02

Realize

07:04

a refatoração

07:11

aqui piloto.

07:17

Estou colocando assim um prompt extremamente simples, né?

07:24

Após refatorar, reanalyze.

07:33

Após refatorar,

07:35

Verifique sempre

07:39

todos os testes aqui pra mim.

07:46

Meu cloud.md provavelmente não está dizendo sempre quando você fizer, rode os testes novamente,

07:51

etc. Então, vamos botar esse cara pra rodar agora aqui e

07:56

vamos ver o que vai acontecer ali pra gente.

08:00

Agora a gente vai ter que esperar um pouco.

08:01

Agora um ponto importante é, ele vai ler... o arquivo,

08:05

vê o código relevante e ele vai chamar a skill que vai trabalhar

08:11

com o TDD pra ele fazer esse ciclo de TDD aqui nesse nosso aspecto.

08:16

Então ele já carregou a skill aqui que ele precisava,

08:18

está lendo os arquivos e o que eu vou fazer agora,

08:22

eu vou parar o vídeo aqui enquanto ele está mexendo,

08:24

Assim que ele terminar a gente começa no próximo vídeo só

08:27

pra ele não ficar gigante aqui pra gente. Então vamos nessa.

## Resumo IA

[RESUMO_IA]