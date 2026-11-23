Módulo: Arquitetura na Era da IA\
Aula: [Entendendo a integração do cache semântico no fluxo principal](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18352)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente viu como avaliar os

00:05

candidatos do cache semântico utilizando o Threshold.

00:08

A aplicação já conseguia pegar uma nova mensagem, gerar um embedding,

00:13

buscar respostas parecidas no PG Vector e dizer se o

00:17

melhor candidato passava ou não com um corte mínimo de similaridade.

00:22

Agora... Antes de partir para o código da nossa próxima aula, vamos dizer assim,

00:26

eu quero organizar o fluxo completo que a gente vai implementar,

00:31

porque essa parte pode ficar um pouco confusa se a gente olhar direto para o código. Até agora,

00:36

o cache semântico estava separado do endpoint principal.

00:40

A gente tinha endpoints próprios para criar itens manualmente,

00:44

buscar similares e avaliar os candidatos que a gente tem.

00:48

Então, isso foi de propósito, apenas para exemplificar.

00:52

Primeiro, a gente queria entender cada peça isolada, gerar o embedding,

00:56

salvar no PG Vector, buscar por similaridade e aplicar o threshold. Ver falso positivo,

01:02

caso a gente tenha essas mudanças, esses números do threshold.

01:07

Só que agora as peças vão começar a entrar

01:10

no fluxo real do nosso analisador de tickets.

01:13

Por quê? O endpoint principal continua sendo o mesmo.

01:17

barra tickets, barra analyze.

01:19

A diferença é que agora ele não vai mais pensar só no cache exato e na IA.

01:26

Ele vai ter uma etapa intermediária. O fluxo passa a ser assim.

01:31

Primeiro, a aplicação tenta o cache exato em memória.

01:34

Se a mensagem já foi enviada antes com o mesmo fingerprint,

01:38

a resposta vem do cache exato e acabou.

01:42

A aplicação não precisa mais gerar embedding, ela não precisa consultar o PG Vector,

01:47

ela não precisa chamar IA. Se não houver cache exato,

01:51

aí sim a aplicação tenta o cache semântico. Nesse momento,

01:55

ela gera o embedding da nova mensagem,

01:58

consulta o PG Vector, busca candidatos parecidos,

02:02

aplica o threshold e decide se algum resultado

02:05

é seguro o suficiente para ser reaproveitado.

02:09

Se encontrar um candidato bom, a resposta vem do cache semântico,

02:13

ou seja, a aplicação reutiliza a resposta que já estava no banco.

02:18

Nesse caso, o modelo de chat também não é chamado.

02:22

Isso é importante por quê? Porque o embedding é gerado para buscar,

02:26

mas a IA que classifica o ticket não roda de novo.

02:31

Agora, se não houver candidato,

02:34

ou se o melhor candidato estiver abaixo do threshold,

02:39

aí a aplicação segue o fluxo normal e chama IA.

02:43

Essa resposta vai continuar sendo salva no cache exato,

02:46

em memória, já como que isso acontece antes. Mas tem um detalhe importante.

02:52

Nessa prática,

02:53

a gente ainda não vai salvar automaticamente esse novo resultado no PG Vector.

03:00

Esse fechamento do ciclo vai ficar para o próximo vídeo, para a parte seguinte,

03:04

que é como a gente consegue integrar a leitura

03:08

do cache semântico no fluxo principal e a escrita automática,

03:12

então ela vem depois. Então, para deixar bem claro,

03:15

o que a gente vai implementar agora é isso,

03:18

cache exato primeiro, cache semântico depois e IA por último.

03:22

O que a gente não vai implementar agora...

03:25

A gente não vai fazer RAG, não vai buscar documentos,

03:28

a gente não vai fazer chunking,

03:30

a gente não vai fazer re-ranking. Por enquanto,

03:32

o objetivo é só um. Quando o cache exato não resolver,

03:35

a aplicação deve verificar se existe uma resposta semanticamente

03:39

parecida no PG Vector antes de chamar IA.

03:42

Isso ajuda a gente a enxergar essas diferenças.

03:45

Então, vamos seguir nessa pegada.

03:49

Porque vai ajudar bastante a forma de como que

03:52

você vai ver a aplicação de forma geral.

03:57

Então, vamos nessa!

## Resumo IA

[RESUMO_IA]