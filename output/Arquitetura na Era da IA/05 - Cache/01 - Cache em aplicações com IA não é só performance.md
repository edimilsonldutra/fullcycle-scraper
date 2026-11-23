Módulo: Arquitetura na Era da IA\
Aula: [Cache em aplicações com IA não é só performance](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18336)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:03

Agora a gente vai entrar em um assunto que parece ser muito

00:06

conhecido para qualquer pessoa que já trabalha com desenvolvimento há algum tempo,

00:10

que é o cache. Só que aqui tem um ponto importante.

00:14

A gente não vai tratar cache simplesmente como aquela

00:17

técnica clássica para deixar uma aplicação mais rápida.

00:21

Isso todo mundo já sabe, ou pelo menos conceitualmente conhece.

00:25

A ideia aqui é entender o que muda...

00:29

quando a gente começa a colocar inteligência artificial no meio da aplicação.

00:34

Porque em aplicações tradicionais,

00:36

muitas vezes o cache aparece para evitar uma consulta no banco,

00:40

evita uma chamada para uma API externa,

00:43

ele reduz a carga para algum serviço ou até

00:46

melhora um tempo de resposta de uma tela.

00:50

Isso continua existindo,

00:51

só que quando a gente fala de IA, o cache começa a ganhar uma importância diferente.

00:57

Porque cada chamada para o modelo pode envolver latência, custo,

01:02

limite de uso, instabilidade, variação de resposta e,

01:06

dependendo do caso,

01:08

até o risco de retornar algo que não deveria ser mais reutilizado.

01:13

Então o problema deixa de ser apenas, como que eu deixo isso mais rápido?

01:17

E a pergunta passa a ser, essa chamada para IA realmente precisa acontecer de novo?

01:24

Essa mudança de pergunta é muito importante.

01:28

Vamos imaginar uma feature simples que analisa os nossos tickets de suporte.

01:32

O usuário manda uma mensagem dizendo que está com dúvida sobre cobrança.

01:37

A aplicação chama o modelo, o modelo classifica aquilo ali como billing,

01:41

retorna uma confiança ali sobre isso,

01:44

talvez até uma explicação curta, e o sistema segue o fluxo. E até aqui, tudo bem.

01:51

Mas se uma mensagem muito parecida entrar de novo, com a mesma versão do prompt,

01:57

com as mesmas regras de classificação, com o mesmo tipo de análise,

02:02

será que faz sentido eu pagar outra chamada para o modelo?

02:05

Será que faz sentido eu esperar de novo ali pela inferência?

02:09

Será que faz sentido eu consumir novamente token,

02:11

rede, provider, timeout, ter retry,

02:14

tudo isso para chegar em uma resposta que provavelmente a gente já tem?

02:18

Então, essa é a nossa primeira camada do raciocínio.

02:23

Cache em aplicações com IA, em parte,

02:26

ela é uma estratégia de performance,

02:28

mas ela também é uma estratégia de custo e também é uma estratégia de resiliência.

02:34

Se eu consigo evitar chamadas desnecessárias ao modelo,

02:38

eu reduzo latência, reduzo custo,

02:40

reduzo pressão em cima do provider e diminuo a chance

02:43

de uma instabilidade externa afetar a experiência do usuário.

02:47

Só que tem um outro lado. O cache também pode virar uma fonte de erro.

02:52

E é aqui que muita gente acaba simplificando demais.

02:57

Não basta eu pegar uma pergunta do usuário, jogar numa chave e pronto.

03:02

Porque a IA, vamos dizer assim, a resposta não depende só da pergunta.

03:07

Ela depende do prompt utilizado, da versão das regras, do modelo escolhido, dos parâmetros,

03:14

do contexto disponível naquele momento e o tipo de resposta que a aplicação espera.

03:20

Por exemplo, se eu tenho uma pergunta,

03:22

Quero cancelar a minha assinatura. Talvez, em um cenário simples, a resposta seja uma.

03:27

Mas se as regras de cancelamento mudaram ontem,

03:30

o cache de ontem pode já não servir mais.

03:33

Se o prompt foi ajustado para classificar melhor os casos de cobrança,

03:38

o cache antigo pode estar tecnicamente válido com o dado armazenado.

03:43

Mas ele é inválido como decisão atual da aplicação. Então,

03:47

quando a gente fala de cache nesse tipo de sistema,

03:50

a gente precisa pensar em identidade de contexto.

03:54

A resposta cacheada não é só uma resposta,

03:58

ela é uma resposta produzida em cima de uma versão específica de um prompt,

04:04

de regra, de modelo e de interpretação.

04:09

E esse é o motivo pelo qual o cache com IA pode ser muito mais arquitetural do que parece.

04:15

Não é só colocar no Redis no meio,

04:18

não é só salvar um JSON numa tabela,

04:20

não é só criar ali um TTL de 5 minutos e achar que o problema está resolvido.

04:25

Essas coisas podem fazer parte da solução, claro,

04:28

mas a decisão importante vem antes. O que exatamente eu estou reutilizando?

04:35

Em quais condições isso continua correto? Quando que eu devo invalidar?

04:40

Quando eu aceito uma resposta antiga? Quando eu prefiro chamar novamente o modelo?

04:45

E perceba que isso conversa diretamente com o que a gente viu antes,

04:49

porque primeiro a gente falou de gateway, proxy, fallback,

04:52

timeout, e de uma forma de a gente controlar mais a aplicação para chamar a IA.

04:59

Depois a gente falou como que a aplicação consegue se comportar enquanto

05:03

ela espera uma resposta de uma forma assíncrona com streaming ou com jobs.

05:07

E agora a gente dá mais um passo que ao

05:10

em vez de pensar apenas de como esperar melhor,

05:13

a gente vai pensar em quando não precisamos

05:16

esperar porque talvez aquela chamada possa ser evitada.

05:21

Só que essa decisão precisa ser feita com muito cuidado. Em alguns casos, o cache...

05:28

vamos dizer assim, o cache exato, ele vai resolver. A mesma entrada,

05:34

com o mesmo fingerprint, pode devolver a mesma resposta.

05:37

Mas, em outros casos, a entrada não é exatamente igual,

05:41

mas ela tem a mesma intenção.

05:43

E aí começa a aparecer a ideia de cache semântico,

05:47

que mais para frente a gente vai implementar utilizando embeddings, pgVector,

05:53

mas antes da gente chegar lá, a gente precisa organizar a base,

05:57

que é Hit, miss, TTL, invalidação, fingerprint,

06:02

versão de prompt e política de cache.

06:05

A ideia desse capítulo é a gente construir esse raciocínio aos poucos.

06:10

A gente vai começar pelo caso mais simples, uma aplicação que chama IA toda vez.

06:15

Depois a gente vai colocar um cache exato.

06:18

Depois a gente vai melhorar a chave de cache com fingerprint.

06:22

Depois a gente vai entender o embedding,

06:25

para entender como comparar o significado e não só aquele texto igual.

06:30

E mais para frente, nós vamos falar ali do cache,

06:33

como que ele acontece no próprio provedor,

06:36

porque a OpenAI, o Gemini, a Anthrop,

06:38

ele tem formas diferentes de reaproveitar partes do prompt.

06:42

Então, o ponto principal dessa primeira aula aqui é esse.

06:46

Cache em aplicação com IA não é apenas uma otimização.

06:50

É uma decisão de arquitetura sobre reutilização.

06:54

Quando bem aplicado, ele reduz custo, latência,

06:57

dependência externa. Quando mal aplicado,

06:59

ele pode devolver uma resposta velha,

07:02

fora de contexto ou simplesmente errada. Então, a partir daqui,

07:05

a gente vai montar essa base com calma e depois a gente vai

07:09

evoluir o projeto prático para a gente ver tudo isso funcionando no código.

## Resumo IA

[RESUMO_IA]