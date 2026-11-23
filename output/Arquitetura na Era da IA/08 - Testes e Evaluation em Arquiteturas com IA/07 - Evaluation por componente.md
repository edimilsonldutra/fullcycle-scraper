Módulo: Arquitetura na Era da IA\
Aula: [Evaluation por componente](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18786)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente criou testes determinísticos

00:05

para o contrato do nosso Knowledge Chat.

00:07

A ideia foi validar coisas objetivas, se a API responde no formato certo,

00:13

se o Resensor vem coerente, se as fontes aparecem quando deveriam aparecer,

00:17

se os casos de recusa não trazem fontes e

00:19

se as perguntas ambíguas seguem o fluxo correto.

00:22

Agora a gente vai dar um passo além.

00:25

Até aqui a gente olhou para o comportamento externo da aplicação.

00:29

O usuário faz a pergunta, a API responde, a gente valida o contrato da resposta.

00:34

Isso aí é importante,

00:35

mas ainda não explica onde o sistema errou quando alguma coisa falha.

00:40

Em sistemas com IA, principalmente em pipelines com várias etapas,

00:44

essa separação é fundamental.

00:45

Pensa no nosso Knowledge Chat. Quando uma pergunta entra,

00:49

ela não vai direto para o modelo final.

00:52

Primeiro passa pelo query planner, depois vem o retrieval,

00:55

depois pode vir o re -ranking,

00:57

depois a aplicação monta o contexto e só então...

01:01

chama o modelo para gerar a resposta. Então, se a resposta final veio ruim,

01:05

a falha pode ter acontecido em vários lugares.

01:08

O query planner pode ter entendido a pergunta de forma errada. Por exemplo,

01:12

a pergunta era sobre SLA, mas ele classificou como política comercial.

01:17

Nesse caso, os filtros podem levar o retrieval para os documentos errados.

01:21

Ou o planner pode ter deixado de identificar o plano.

01:25

A pergunta era sobre o enterprise, mas o plano ficou nulo, por exemplo. Então,

01:29

a busca... ela ficou mais ampla e pode trazer contextos do starter,

01:34

do plano pro, do plano enterprise misturado. Então,

01:37

a gente pode ter a mesma coisa com o retrieval,

01:42

a gente pode ter isso com o re -ranking e tudo mais, tá?

01:46

Você consegue perceber o problema? Se a gente avalia só a resposta final,

01:50

a gente sabe que falhou, mas a gente não sabe onde a gente falhou.

01:54

E é por isso que evaluation...

01:56

por componente também é importante.

01:58

Em vez de a gente tratar a aplicação como uma caixa preta,

02:01

a gente avalia cada parte do pipeline com critérios próprios. No query planner,

02:06

a gente pode avaliar se ele identificou o dock type esperado. No retrieval,

02:10

a gente pode avaliar se os documentos aceitos para

02:12

aquele caso apareceram entre os chunks recuperados. No re -ranking,

02:16

a gente pode avaliar se os chunks selecionados ainda preservam as fontes. Na geração final,

02:21

a gente pode avaliar se a resposta respeitou o contexto, trouxe fontes.

02:25

não inventou nada. Então, cada componente tem a sua responsabilidade.

02:29

E isso ajuda a gente bastante no dia a dia porque evita conserto no lugar errado.

02:34

Sem essa reparação, o time começa a trocar modelo, mudar prompt final,

02:38

aumentar o top key ou mexer nos chunkings sem

02:41

saber se esse era realmente o problema.

02:44

Então, a mensagem principal dessa aula é evaluation.

02:50

Boa não avalia apenas o output final.

02:53

Ela ajuda a localizar a falha dentro da arquitetura. Então, no próximo vídeo,

02:59

a gente vai começar a seguir com isso nessa linha para que

03:02

Você consiga ter mais clareza em relação a todos esses pontos. Então, vamos nessa!

## Resumo IA

[RESUMO_IA]