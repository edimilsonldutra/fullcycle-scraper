Módulo: Arquitetura na Era da IA\
Aula: [Avaliando resposta final](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18790)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente olhou para avaliação por componente,

00:05

a ideia foi separar o pipeline em partes para

00:08

a gente entender onde que uma falha nasce,

00:10

no planner, no retrieval,

00:12

no re-ranking ou em alguma etapa anterior à geração.

00:15

Agora a gente vai olhar para o outro lado,

00:18

a resposta final que chega para o usuário.

00:21

Esse ponto é importante porque no final das contas o usuário não vê o planner,

00:25

ele não vê o score, do retrieval ele não vê nada.

00:28

Ele nem quer saber quantos chunks foram recuperados.

00:31

O usuário vê a resposta. Então,

00:33

mesmo com componentes internos estejam funcionando bem,

00:35

a resposta final ainda precisa ser avaliada.

00:38

Só que avaliar a resposta final em sistemas com IA é mais difícil do que parece.

00:43

Numa aplicação tradicional, muitas vezes eu consigo fazer um acerto direto.

00:46

A saída deveria ser exatamente essa.

00:50

Mas em uma resposta gerada por um LLM,

00:54

duas respostas diferentes podem estar corretas. Uma pode ser mais curta,

00:59

a outra pode ser mais explicativa,

01:00

uma pode usar palavras diferentes e ainda responder

01:03

exatamente o que o usuário perguntou.

01:06

Então a pergunta não é apenas, a resposta é igual à esperada?

01:10

E a pergunta passa a ser, a resposta cumpre o papel dela? E para responder isso,

01:15

a gente precisa olhar para algumas dimensões. A primeira é relevância.

01:20

A resposta realmente responde à pergunta do usuário?

01:23

Parece óbvio, mas é um dos erros mais comuns.

01:26

Às vezes o modelo responde algo relacionado ao tema,

01:29

mas não responde exatamente à pergunta.

01:32

O usuário pergunta sobre o tempo de resposta para a

01:36

P1 no Enterprise e a

01:38

resposta fala de gerenciamento sobre suporte,

01:43

canais de atendimento e SLA.

01:46

Então, está no assunto, mas não resolveu a dúvida.

01:49

Agora a gente tem a segunda dimensão, que é a completude.

01:53

A resposta traz o suficiente para o usuário entender o ponto principal?

01:58

Ela não precisa explicar o documento inteiro,

02:00

mas ela precisa cobrir o que a pergunta exige.

02:04

Se a pergunta envolve P1 no Enterprise,

02:07

talvez não basta dizer SLA, sei lá, reduzido.

02:11

A resposta precisa trazer o tempo da resposta e talvez mencionar 24 por 7,

02:16

se isso for parte relevante ali da regra.

02:19

E aí a gente tem também a terceira dimensão,

02:22

que é o groundedness, ou a fundamentação. A pergunta aqui é...

02:28

A resposta está sustentada pelo contexto que o sistema recebeu? Em reg,

02:33

isso é essencial. A resposta pode estar bem escrita, pode parecer correta,

02:38

mas se ela trouxe uma informação que não estava no contexto,

02:42

a gente tem um problema. Ela pode estar usando o conhecimento geral do modelo,

02:47

suposição ou preenchendo lacuna com algo ali plausível.

02:52

E isso é exatamente o tipo de erro que avaliação precisa pegar.

02:57

A quarta dimensão é a atribuição de fonte.

03:00

Não basta ter uma lista de fontes no final.

03:03

A fonte precisa sustentar aquilo que foi dito.

03:06

Se a resposta fala sobre crédito de SLA,

03:09

a fonte precisa ter um trecho que realmente trate de créditos de SLA.

03:14

Se a fonte é apenas um documento genericamente relacionado a suporte,

03:18

isso pode ser que isso não seja o suficiente.

03:22

Então, uma boa avaliação não olha só se existe fonte.

03:26

Ela pergunta se a fonte é adequada.

03:28

A quinta dimensão é a recusa correta. Um sistema com IA não deve responder tudo.

03:35

Se a informação não está na base,

03:37

se a pergunta depende de um dado transacional que o RAG não possui,

03:41

ou se faltam detalhes importantes,

03:43

o sistema precisa saber que não tem informação suficiente ou pedir esclarecimento.

03:48

Então, isso também é qualidade.

03:52

Então, às vezes, a melhor resposta... é não responder ainda.

03:56

Então isso é muito difícil para alguns times aceitarem,

03:59

porque a tendência é medir qualidade apenas como o sistema respondeu.

04:04

Em sistemas com IA,

04:05

uma recusa correta pode ser muito melhor do que uma resposta confiante e errada.

04:10

E aí a gente tem a sexta dimensão,

04:13

que é... Clareza, tá? Mesmo quando a resposta está correta e fundamentada,

04:18

ela precisa ser compreensível,

04:20

ou seja, uma resposta pode ser tecnicamente certa, mas confusa, longa demais,

04:26

cheia de termos desnecessários ou com uma estrutura ruim.

04:30

Então, em algumas aplicações isso importa muito.

04:33

Por exemplo, um assistente de suporte precisa responder com objetividade.

04:38

Um assistente interno de analista, sei lá, talvez ele possa trazer mais detalhes.

04:43

O critério depende sempre do quê? Do produto. Então,

04:47

quando avaliamos a resposta final, a gente não está avaliando apenas o texto bonito.

04:52

A gente está avaliando se a resposta é relevante,

04:56

completa, que ela é fundamentada, rastreável,

04:59

segura dentro do escopo e clara para o usuário também.

05:02

E isso é um ponto importante para a gente não misturar as coisas.

05:06

Na aula de componentes,

05:07

a gente queria saber se o pipeline encontrou e selecionou o contexto certo.

05:12

Agora, a pergunta é outra. Dado o contexto selecionado,

05:15

o sistema gerou uma boa resposta?

05:18

Essas duas avaliações se complementam. Se a resposta final falha,

05:22

mas o contexto estava errado,

05:24

o problema provavelmente não está no modelo final e está antes.

05:28

Se o contexto estava certo e a resposta final falhou,

05:31

aí talvez o problema esteja ali no prompt, no modelo,

05:34

na rubrica de resposta ou no formato aí esperado.

05:38

Então essa separação evita ali muito chute.

05:42

E no nosso projeto, a nossa próxima etapa, a prática,

05:45

vai começar a medir essas dimensões usando ferramentas específicas.

05:50

A gente vai sair dos checks simples, né?

05:53

Tem fonte ou não tem fonte?

05:55

E começar a olhar para as métricas mais ligadas à

05:58

Qualidade das respostas e o uso correto do contexto.

06:02

Então, guarda essa ideia.

06:03

Avaliar a resposta final não é comparar texto com texto.

06:08

É verificar se a resposta cumpre a intenção do usuário e

06:11

se permanece fiel às evidências que a aplicação entregou ao modelo.

06:15

E aí, nos próximos vídeos,

06:17

a gente vai ver essas métricas com RAG e etc. Então, vamos nessa!

## Resumo IA

[RESUMO_IA]