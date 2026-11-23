Módulo: Arquitetura na Era da IA\
Aula: [Por que RAG simples falha](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18440)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente evoluiu no nosso chat com o Reg para retornar... uma resposta,

00:07

fonte das informações,

00:09

e a gente também fez um sistema simples de debug para a gente conseguir ver.

00:15

Isso já colocou a gente num ponto bem melhor do que simplesmente

00:18

perguntar para o modelo e torcer para ele responder certo.

00:21

Agora a aplicação busca contexto, monta o prompt,

00:24

responde com base nos chunks e mostra de onde aquela resposta veio.

00:28

Mas agora vem uma parte importante. Mesmo com tudo isso funcionando,

00:32

o Reg ainda pode falhar.

00:34

E esse seja uma das coisas mais importantes para entender.

00:37

O Reg funcionar em uma demo não significa que ele está pronto para a produção.

00:42

Muitas vezes a aplicação responde, mostra a fonte, parece que tudo está certo,

00:46

mas o problema está escondido em alguma etapa anterior do pipeline.

00:50

O Reg simples costuma seguir aquele fluxo básico.

00:53

Pega o documento, quebra em chunks,

00:55

gera embed, salva no banco, busca os chunks mais parecidos,

00:59

manda para o modelo. E esse fluxo é bom para aprender.

01:02

Ele é ótimo para a gente construir a primeira... Mas no mundo real,

01:06

ele começa a mostrar um monte de limite rapidamente.

01:09

Um primeiro problema é chunk sem contexto.

01:12

Às vezes o trecho recuperado tem uma frase correta,

01:15

mas perdeu a informação que explicava aquela frase. Por exemplo,

01:19

o chunk diz que o tempo de resposta é de 30 minutos,

01:21

mas não diz se isso vale para o P1 ou para o P2 ou plano enterprise,

01:26

plano individual ou horário comercial. O modelo recebe um pedaço verdadeiro,

01:31

mas incompleto. E o pedaço verdadeiro, quando está fora de contexto,

01:35

pode gerar uma resposta errada.

01:37

Outro problema é que a busca vetorial pode falhar com termos exatos.

01:42

Embeddings são muito bons para a similaridade semântica.

01:45

Eles ajudam quando a pergunta usa palavras diferentes, mas tem o mesmo sentido.

01:50

Só que em muitos sistemas reais existem siglas, códigos, nomes de produto, versões,

01:55

identificadores e termos bem específicos. Como coisas como P1, SOC2, FC...

02:02

AI Cloud, versão tal, endpoint X, plano enterprise. Às vezes,

02:07

uma busca puramente semântica pode não dar o peso correto para esse tipo de termo.

02:13

Ele entende o assunto em geral, mas perde o detalhe exato.

02:17

Em Reg, perder o detalhe exato pode mudar a resposta.

02:21

Também existe o problema de documentos conflitantes.

02:24

Imagina que você tem uma política antiga e uma política nova.

02:27

As duas estão falando do mesmo assunto.

02:30

Se o pipeline não usa bem os metadados, a versão, o status,

02:33

o retrieval pode trazer as duas.

02:35

Aí o modelo recebe os dois contextos com regras diferentes

02:38

e tenta montar uma resposta no meio ali daquilo.

02:41

E o resultado pode parecer até razoável,

02:43

mas não vai representar necessariamente a regra oficial.

02:47

Um outro erro comum é o documento antigo vencer o documento novo.

02:51

Isso acontece porque o banco vetorial não sabe sozinho o que é mais atual,

02:56

o que está aprovado, o que está válido. Então,

02:58

ele só sabe calcular a proximidade.

03:00

Se o documento antigo estiver mais parecido semanticamente com o novo,

03:05

ele pode trazer essa resposta antes. Por isso, a versão,

03:09

os estágios e os filtros são muito importantes para trabalhar com confiabilidade.

03:14

E a gente também tem o caso da pergunta ambígua, tá?

03:18

O usuário pergunta como. Como funciona o suporte do plano da empresa?

03:23

Só que o plano da empresa pode significar o plano Enterprise,

03:27

o plano corporativo, contrato customizado ou qualquer outra coisa.

03:32

Se a aplicação não tiver contexto adicional do usuário

03:35

ou não fizer uma pergunta de esclarecimento,

03:38

ele pode buscar o documento errado e responder como se tivesse certo, tá?

03:42

E também, um outro ponto é que o retrieval pode trazer o contexto certo,

03:48

mas o modelo não usar direito. Isso acontece, por quê?

03:53

Porque às vezes o chunk correto está no prompt,

03:55

mas ele vem junto com outros chunks mais genéricos ou parecidos.

03:59

Então o modelo pode dar mais atenção ao trecho errado,

04:03

misturar informações ou responder de forma incompleta. Então não basta dizer,

04:08

o chunk certo apareceu no top key. A pergunta é,

04:12

ele apareceu em uma posição boa? Ele foi enviado de forma clara?

04:16

O prompt direcionou bem o uso daquele contexto?

04:19

E ainda existe um erro mais sutil. A fonte não sustenta a resposta.

04:25

A aplicação pode mostrar uma fonte,

04:27

mas aquela fonte só tem a relação com o tema ali,

04:31

sem realmente provar que aquilo tem uma conclusão da resposta.

04:35

Então, ou seja, ela tem relação, mas aquela...

04:38

Fonte, ela não fala assim, olha, a resposta é essa. 1 mais 1 é igual a 2.

04:43

Então, esse é um cuidado muito importante,

04:45

porque a fonte não pode ser apenas o documento parecido.

04:48

Ela deve ser o trecho que sustenta aquilo que foi dito. Então,

04:52

quando a gente fala que um REG simples falha, não é porque o REG é ruim.

04:55

É porque o REG é um pipeline com várias

04:57

decisões e cada decisão pode introduzir erro.

05:01

Pode falhar na ingestão, no chunking.

05:03

Nos metadados, na busca, na montagem do contexto, na geração,

05:08

falha no prompt, em tudo quanto é lugar.

05:10

E é por isso que um debug é tão importante no RAG,

05:13

porque a gente precisa conseguir olhar para a pergunta original,

05:16

para os filtros aplicados, para os chunks retornados,

05:20

para os scores, para o contexto enviado ao modelo e também para a resposta final.

05:24

Na próxima prática, na parte de prática que a gente vai fazer,

05:27

a gente vai pegar uma busca ruim de propósito e melhorar esse fluxo.

05:32

A ideia não é...

05:33

criar um REG perfeito,

05:34

mas mostrar como sair de um REG ingênuo e começar

05:38

a pensar em relevância com o texto do chunk,

05:41

metadados e busca ali mais controlada, fechou?

## Resumo IA

[RESUMO_IA]