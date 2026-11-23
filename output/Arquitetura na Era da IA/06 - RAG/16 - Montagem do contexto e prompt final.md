Módulo: Arquitetura na Era da IA\
Aula: [Montagem do contexto e prompt final](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18437)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem? No vídeo anterior a gente testou o retrieval isolado.

00:06

A gente fez uma pergunta,

00:07

buscou os chunks do Postgres com o PgVector e olhou o que voltou.

00:12

Antes de chamar o modelo,

00:13

a gente acabou no final das contas fazendo isso. Perceba,

00:16

a gente não chamou o modelo de A.

00:18

Para não dizer que a gente não chamou,

00:21

a gente utiliza um modelo de embedding para transformar a mensagem ali em um vetor.

00:26

Agora, isso foi importante para a gente,

00:28

porque agora a gente sabe separar uma coisa da outra.

00:31

Uma coisa é encontrar candidatos de contexto,

00:34

outra coisa é transformar esses candidatos em uma resposta final.

00:39

E agora entra uma etapa muito importante e que muita gente trata como um detalhe,

00:45

mas que na prática faz muita diferença,

00:49

que é a montagem do contexto e o prompt final.

00:52

Depois que o retrieval retorna os chunks,

00:56

a aplicação ainda precisa decidir como esses trechos

00:59

vão ser entregues para o modelo.

01:01

E aqui mora um ponto muito importante.

01:04

Montar um contexto não é simplesmente concatenar texto e jogar dentro do prompt.

01:10

Se a gente faz isso de qualquer jeito, o modelo pode receber trechos fora de ordem,

01:15

informações duplicadas, metadados perdidos,

01:18

fontes sem identificação ou até contexto demais.

01:21

E quando isso acontece,

01:23

o problema não está mais na busca.

01:25

O problema está em como a aplicação entregou evidência para o modelo.

01:30

Então dá para pensar nessa etapa como uma camada de preparação.

01:34

O retrieval encontrou as possíveis evidências ali para a gente.

01:38

A montagem do contexto organiza essas evidências para

01:42

que o modelo consiga usar isso melhor.

01:45

Uma boa montagem de contexto normalmente precisa preservar algumas informações.

01:50

O conteúdo do chunk,

01:53

obviamente, claro, mas também o documento de origem, o título, a sessão,

01:59

a versão e qualquer outro metadado importante para rastreabilidade.

02:04

Porque no final, quando o modelo responder,

02:06

a aplicação precisa saber de onde... Aquela resposta veio.

02:10

Se eu mando para o modelo apenas o texto bruto,

02:12

eu posso até conseguir uma resposta boa,

02:14

mas eu perco parte da rastreabilidade.

02:17

Já se eu mando o contexto de uma forma mais estruturada,

02:20

com cada trecho identificado,

02:22

fica mais fácil pedir para o modelo citar a fonte e

02:25

também fica mais fácil em debugar tudo isso aí depois.

02:29

Um outro cuidado é delimitar bem cada trecho.

02:32

O modelo precisa entender onde começa e onde termina cada parte do contexto.

02:38

Isso evita misturar informação. Por quê? Um trecho pode vir do documento de SLA,

02:44

um outro trecho pode vir da política comercial, o outro do plano enterprise.

02:48

Se tudo virar... um blocão de texto sem separação,

02:52

a resposta pode misturar as regras de documentos diferentes.

02:55

A gente também precisa pensar na ordem.

02:59

Nem sempre a ordem retornada pela busca é a

03:02

melhor ordem para a gente fazer o prompt.

03:04

Às vezes faz sentido manter a ordem de relevância,

03:07

às vezes faz sentido agrupar por documento,

03:11

às vezes faz sentido colocar primeiro a fonte mais

03:13

específica e depois uma fonte mais geral.

03:16

O ponto é que a aplicação precisa ter uma estratégia, mesmo que simples.

03:21

E tem também o limite de contexto. Só porque o Retrieval trouxe 5 ou 10 chunks,

03:27

não significa que tudo precisa ir para o modelo.

03:30

Cada chunk vira token. Isso aumenta o custo,

03:34

aumenta a latência e pode atrapalhar na resposta.

03:36

Então, a montagem do contexto também é uma camada de seleção.

03:41

Ela decide, no final das contas, o que entra e o que vai ficar de fora. Além disso,

03:46

o prompt final precisa ter instruções claras e ele precisa

03:50

dizer para o modelo responder com base no contexto fornecido.

03:54

Ele precisa dizer, também, para não inventar,

03:57

quando a informação não estiver ali. Ele precisa dizer para a resposta, por exemplo,

04:02

responder em português. E se for o padrão da aplicação, por exemplo,

04:06

se a aplicação for em inglês, responda em inglês. Ou seja,

04:09

a gente precisa orientar o formato da resposta.

04:12

E obviamente que eu não estou nem falando ainda aqui,

04:14

por exemplo, de segurança, de prompt injection ou qualquer coisa desse tipo.

04:19

Eu estou falando aqui simplesmente em setar algumas boundaries, setar algumas...

04:27

delimitações para fazer com que o modelo fique e

04:31

responda somente dentro daquele contexto que a gente está trabalhando.

04:34

Agora, um prompt final simples pode ter quatro partes. Primeiro,

04:39

a instrução do sistema,

04:40

dizer qual é o papel do assistente e quais regras ele deve seguir.

04:45

Depois, o contexto recuperado, com os trechos organizados e identificados.

04:51

Depois... a pergunta do usuário. E, por último,

04:54

a orientação de saída. Por exemplo, responda de forma objetiva,

04:58

use apenas esse contexto. Se não houver informação suficiente,

05:03

diga que não encontrou informação e tudo mais.

05:05

Isso é importante porque um prompt bom não é somente responder quando sabe.

05:12

Um prompt bom, ele também sabe responder quando o contexto não sustenta a resposta.

05:17

E essa talvez seja uma das diferenças mais

05:20

importantes entre um protótipo e uma arquitetura mais confiável.

05:24

No protótipo, a gente fica feliz quando o modelo responde. Numa aplicação real,

05:28

a gente também precisa ficar feliz quando ela se recusa a responder corretamente. Por quê?

05:34

Porque uma recusa... Correta é melhor do que uma resposta inventada com confiança.

05:40

Então, nessa etapa,

05:41

a aplicação começa a criar um contrato com o modelo.

05:44

Ela diz, aqui estão os trechos que você pode usar,

05:48

aqui está a pergunta, aqui está o formato esperado.

05:52

E se a resposta não estiver nesses trechos,

05:54

não invente. Claro que isso não é garantia absoluta. O modelo ainda pode errar.

05:59

Mas essa estrutura reduz bastante o risco e melhora a previsibilidade do sistema. No próximo vídeo,

06:05

a gente vai colocar isso na prática,

06:07

a gente vai pegar alguns chunks retornados pelo retrieval,

06:11

montar um contexto organizado.

06:13

Criar um prompt final e gerar ali uma resposta com o reg.

06:17

A partir daí, o nosso chat,

06:19

ele deixa de ser apenas uma busca de chunks e começa

06:22

a responder de verdade com base na nossa base de dados interna. Então vamos nessa.

## Resumo IA

[RESUMO_IA]