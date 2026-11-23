Módulo: Protocolos de Comunicação\
Aula: [JSON-RPC 2.0: O Wire Format](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18587)

## Resumo da aula

Wire format é a mensagem real que trafega entre sistemas, independentemente do SDK, da linguagem ou da representação interna no código. Ele importa porque a integração só é verificável no ponto em que ambos os lados concordam sobre o que foi efetivamente enviado e recebido. Retomando a motivação de padronização já vista, o desacoplamento só se sustenta quando o acordo entre sistemas existe no nível da mensagem, não apenas no nível da biblioteca.

JSON-RPC 2.0 oferece baixo atrito porque seu contrato é pequeno, legível e não depende de uma toolchain pesada para começar. Ele também separa mensagem de transporte, o que permite manter o mesmo formato conceitual sobre diferentes canais sem reescrever a conversa. Em cenários com LLMs, a clareza semântica do JSON ajuda a distinguir intenção, dados e resultado com menos ambiguidade.

Uma mensagem JSON-RPC 2.0 é lida por quatro campos centrais: jsonrpc, method, params e id. jsonrpc fixa a versão do protocolo; method identifica a operação; params carrega os dados necessários; id marca chamadas que esperam resposta. Essa leitura operacional transforma um payload em algo inspecionável: versão, ação, argumentos e controle de correlação.

Request é a mensagem que pede a execução de uma operação e, por isso, abre uma pendência na conversa. Retomando o cenário do assistente no e-commerce, uma chamada como tools/call com o nome da tool consultar_pedido e um pedido_id expressa exatamente isso: qual capacidade deve ser acionada e com quais argumentos. A presença de id indica que existe expectativa de resposta associada àquela chamada.

Response fecha uma pendência aberta por um request e sempre traz exatamente um desfecho estruturado: result ou error. result representa sucesso utilizável pela aplicação ou pelo modelo; error representa falha tratável, com estrutura própria. Essa separação evita confundir entrega da mensagem com sucesso da operação, especialmente quando o transporte é HTTP e o status da camada de transporte não reflete o desfecho lógico da chamada.

Notification é uma mensagem que sinaliza algo no fluxo sem abrir nova pendência e sem exigir resposta. Por isso, ela não possui id: a ausência desse campo é parte do significado, não um defeito do payload. Em fluxos operacionais, notifications servem para progresso, inicialização, cancelamento ou mudança de estado que precisa ser comunicada, mas não confirmada por uma response.

O id é o mecanismo que liga uma response ao request correto, mesmo quando várias operações estão em andamento ao mesmo tempo. Ele existe para remover a dependência de ordem: a terceira chamada pode responder antes da primeira sem quebrar a conversa. Isso é essencial para interpretar logs e inspeções no MCP Inspector, porque a leitura correta depende de correlacionar mensagens por identificador, não por posição temporal.

Multiplexação ocorre quando várias conversas lógicas compartilham o mesmo canal de comunicação. Em JSON-RPC, isso funciona porque cada request tem seu próprio id, e cada response devolve esse identificador para fechar a pendência certa. O efeito prático é permitir paralelismo sem exigir um canal separado por operação.

Os códigos -32700, -32600, -32601, -32602 e -32603 classificam falhas recorrentes de forma previsível: parse inválido, request inválido, método inexistente, parâmetros inválidos e erro interno. Essa padronização reduz o custo de diagnóstico porque transforma “deu erro” em uma hipótese operacional concreta sobre onde investigar. Em vez de depender apenas da mensagem textual, o consumidor usa error.code para distinguir falha de sintaxe, de contrato, de roteamento ou de execução.

REST encaixa melhor quando a integração é orientada a recursos e operações de CRUD; quando a conversa exige progresso, mensagens bidirecionais e múltiplas pendências, ele tende a precisar de convenções adicionais. gRPC oferece performance, streaming e contratos fortes, mas cobra isso com mais peso operacional e menor legibilidade direta do payload. JSON-RPC ocupa o meio-termo adequado para o MCP: conversa estruturada, interoperabilidade, correlação explícita e baixo atrito para inspeção humana e consumo por sistemas com LLM.

JSON-RPC 2.0 funciona como o wire format do MCP porque fornece uma unidade mínima de comunicação simples, verificável e padronizada. É nesse nível que requests de tools, responses de execução, notifications de estado e erros passam a ser observáveis de forma uniforme. Entender essa camada é o pré-requisito para ler logs, interpretar o Inspector e depurar chamadas nas etapas práticas.

## Transcrição

00:01

Oi pessoal, tudo bem?

00:03

Hoje a gente vai fazer um mergulho em uma camada que normalmente fica escondida.

00:08

Quando você usa uma ferramenta, um SDK ou uma integração pronta,

00:12

parece que a comunicação acontece por métodos,

00:15

objetos e funções, não é o que a gente enxerga. Você chama a função,

00:18

recebe uma resposta e segue o fluxo. Mas por baixo disso existe outra coisa,

00:23

existe uma mensagem real trafegando entre os dois lados.

00:26

E essa é a mensagem que a gente vai estudar hoje.

00:28

O tema da aula é JSON-RPC 2.0 como wireformat. Ou seja,

00:33

o formato da conversa que está dentro do fio.

00:36

A proposta aqui não é decorar uma especificação inteira.

00:40

Também não é transformar o JSON-RPC em um assunto maior do que ele precisa ser.

00:43

A proposta é prática.

00:45

Quando você olhar para uma mensagem de JSON-RPC,

00:47

você deve conseguir entender qual papel ela cumpre na conversa.

00:52

Então, pensa nessa aula como uma base de leitura.

00:55

Antes de discutir arquiteturas maiores,

00:56

a gente vai aprender a ler a unidade mínima da conversa.

00:59

Então, hoje a gente não começa pela arquitetura inteira,

01:01

a gente começa pela mensagem, ok?

01:05

Então, a agenda aqui, pessoal, não é uma lista de assuntos isolados,

01:10

tá? Ela é uma escadinha, vocês vão perceber, tá?

01:13

Cada parte prepara para a próxima, ou seja,

01:15

a gente começa pela espinha dorsal, o wire format em si, tá?

01:19

Depois a gente... Abre a mensagem. A ideia é entender como ela organiza a conversa. Depois disso,

01:26

a gente entra no ponto em que várias

01:27

operações podem estar acontecendo ao mesmo tempo.

01:29

Aqui o foco é entender como a conversa continua organizada,

01:32

mesmo quando as coisas não acontecem em uma fila perfeita. E por fim,

01:37

a gente fecha com erros, porque uma integração não é boa só quando tudo dá certo.

01:41

Ela também precisa ser clara quando algo falha. Então o caminho é esse.

01:45

Primeiro a gente entende o fio. Depois a mensagem,

01:48

depois a gente fala dos papéis da conversa,

01:50

depois a coordenação dessa conversa e por fim a falha.

01:54

Com esse mapa dá para entrar no primeiro ponto sem

01:57

tentar resolver a aula inteira de uma vez. Bem,

02:01

começando pelo termo principal dessa primeira parte, que é o wire format.

02:05

O wire format é o formato real da comunicação entre dois sistemas.

02:09

Não é SDK, não é classe de método.

02:12

Desculpa, não é classe no código, não é o objeto que aparece bonito do debugger,

02:16

é a mensagem como ela trafega.

02:20

É o que está no fio.

02:22

Isso muda um pouco a forma como a gente olha para a integração.

02:25

Quando tudo funciona,

02:27

ninguém pensa nesse nível. Você chama uma função,

02:29

a biblioteca monta o que precisa montar,

02:33

o servidor responde e a aplicação segue.

02:35

Mas quando dá problema, a abstração começa a perder força.

02:39

Aí você precisa perguntar o que realmente foi enviado.

02:42

Imagina uma situação comum, tá? O cliente foi escrito em TypeScript.

02:46

O servidor está em Python. Cada lado usa uma biblioteca diferente.

02:50

O time do client olha para o código e diz, daqui saiu certo, né?

02:54

O time do server olha para o log e diz,

02:56

aqui não chegou como esperado, né? Nesse momento,

03:01

a pergunta que importa não é mais, o SDK deveria ter feito o quê? A pergunta é,

03:05

qual mensagem passou de verdade? Então, essa é a função do wire format, tá?

03:10

Ele é o contrato verificável entre os sistemas.

03:13

Se os dois lados concordaram no wire,

03:16

eles conseguem conversar mesmo usando linguagens diferentes,

03:20

bibliotecas diferentes e ambientes diferentes.

03:22

Então, SDK é conveniência local.

03:24

O wire é acordo entre sistemas.

03:27

E no contexto de IA, isso ganha mais peso,

03:29

porque a mensagem não serve só para duas bibliotecas conversarem.

03:33

Ela também pode virar contexto para um sistema ou

03:36

modelo que precisa interpretar a intenção e o resultado.

03:39

Então, quanto mais explícito é o wire, menor a ambiguidade da conversa.

03:43

É por isso que a observabilidade real passa por esse nível.

03:48

Logs de payload, traces,

03:49

proxies e ferramentas de captura tentam responder cada

03:53

um do seu jeito a mesma pergunta. O que passou no fio?

03:56

Então, guarda essa ideia. O wire format não é um detalhe interno.

04:00

É o ponto onde a integração fica verificável.

04:03

Agora que a gente entendeu o papel do wire format,

04:05

dá para fazer a próxima pergunta. Por que escolher JSON-RPC?

04:09

para ocupar esse papel.

04:13

E, de novo, por que usar um protocolo definido em 2010, inclusive?

04:18

Então, a pergunta é boa, porque o contexto que envolve A e tal parece muito moderno.

04:25

A gente está aqui falando de A, de agente, de MCP.

04:29

Então, seria esperado ver um protocolo mais recente ou mais sofisticado.

04:33

Mas a escolha de protocolo não deveria começar pela data de criação.

04:37

Deveria começar pelo encaixe.

04:39

Qual problema precisa ser resolvido,

04:40

quais propriedades importam e quais custos a gente aceita pagar.

04:44

A indústria tinha várias opções, REST, gRPC, GraphQL,

04:50

OpenAPI, ProfitBuff, enfim.

04:54

Então o JSON-RPC não entra por falta de alternativa.

04:57

Ele entra porque algumas características combinam bem com esse tipo de comunicação.

05:02

A primeira é baixo atrito.

05:04

O contrato não exige um ecossistema pesado para ser entendido.

05:08

Isso ajuda quando você quer interoperabilidade entre linguagens,

05:11

ferramentas e ambientes diferentes.

05:13

A segunda é que a comunicação não precisa ficar presa num modelo clássico de client,

05:18

pede, serve e responde.

05:19

O tempo todo. Ou seja, em protocolos de integração com ferramentas,

05:24

às vezes o server também precisa sinalizar eventos,

05:28

progresso ou mudança de estado. A conversa pode ter mais movimento, mais dinamismo.

05:34

A terceira é separar a mensagem do transporte.

05:36

A mesma ideia de que mensagem pode trafegar por caminhos diferentes.

05:43

Isso é saudável em arquitetura.

05:45

porque o transporte pode mudar sem obrigar a

05:49

reescrever o contrato conceitual da conversa.

05:51

E a quarta é a semântica do JSON. JSON organiza informação em pares de chave -valor.

05:58

Isso cria um formato que é legível,

06:00

parciável e semanticamente previsível. Em sistemas com LLM,

06:04

essa previsibilidade importa porque reduz a chance de misturar instrução,

06:09

dado e resposta.

06:10

Claro, JSON -RPC não resolve todos os problemas.

06:13

Ele não é a opção mais performática.

06:15

Não entrega a mesma força de esquema de protobuf.

06:20

Ele não substitui sozinho decisões de streaming,

06:23

por exemplo. Mas arquitetura é troca. E neste caso, as trocas fazem sentido.

06:28

A escolha não é o protocolo mais novo.

06:30

É o protocolo com atrito certo para o problema.

06:35

Agora que entendemos o porquê, vamos olhar para a mensagem em si, pessoal.

06:39

Bem, vamos abrir a mensagem de ISO -RPC?

06:42

Aqui, o objetivo é a gente ganhar a leitura da mensagem.

06:48

A leitura é como a gente entende a mensagem.

06:51

Então, quando você encontrar uma mensagem no log,

06:54

no trace ou em uma documentação,

06:56

você precisa conseguir identificar rapidamente o que cada parte está fazendo.

07:00

Então, o primeiro campo é o JSON -RPC.

07:02

Ele indica a versão do protocolo. Na prática, aqui estamos falando de 2 .0.

07:06

Então, esse campo parece burocrático, mas ele estabelece a regra do jogo.

07:11

Antes de interpretar a mensagem,

07:12

o outro lado precisa saber qual contrato está sendo usado. Depois vem método.

07:18

Este é o nome da operação. Ele responde a pergunta.

07:22

O que essa mensagem quer acionar?

07:24

Em MCP, você pode encontrar nomes como tools barra call,

07:29

resources barra list, initialize ou notifications barra initialize.

07:34

Não vamos entrar em cada um agora, mas o importante é saber que o método...

07:39

carrega a intenção operacional.

07:42

Aí depois vem parâmetros. Esse aqui é meio óbvio.

07:45

Aqui ficam os dados necessários para executar aquela operação.

07:49

Se o método diz o que precisa acontecer,

07:51

parâmetros traz as informações para isso acontecer.

07:55

É aqui que muita integração quebra. Não porque o método não existe.

08:02

mas porque os dados vierem em formato inesperado,

08:04

por exemplo. O campo faltou, um tipo veio diferente,

08:07

um objeto veio com estrutura errada.

08:10

E por fim, pessoal, nós temos o ID. Nesse slide, guarda só a ideia básica.

08:16

Aqui a gente só vai guardar a ideia básica.

08:18

O ID identifica uma chamada quando existe expectativa de resposta.

08:22

A explicação completa da correlação fica mais para frente.

08:25

Agora, olha para esses campos com uma leitura operacional. Method é intenção.

08:32

Params são dados. Id é controle da conversa.

08:36

Essa estrutura ajuda sistemas tradicionais e modelos

08:40

a não tratarem tudo como um texto indiferenciado.

08:43

Mas, em compensação, ela não elimina erro, mas ela reduz a ambiguidade.

08:48

Então, a leitura prática é qual a versão do protocolo,

08:51

Qual a operação, com quais dados existe chamada identificada. Então,

08:55

Essas perguntas transformam o JSON aparentemente técnico em uma conversa legível.

09:00

Agora que vimos a estrutura,

09:02

Vamos ver como essa estrutura aparece em uma mensagem que pede alguma coisa.

09:06

Bem, vamos

09:09

Entrar nos três papéis da conversa. E para não ficar abstrato,

09:14

Vamos usar um case simples que vai acompanhar os próximos slides.

09:17

Então, imagina um assistente dentro de um e-commerce.

09:20

O usuário pergunta, qual o status do meu pedido? O modelo não sabe isso sozinho.

09:25

Ele precisa acionar uma capacidade externa.

09:27

Pode ser uma tool chamada consultar pedido, por exemplo.

09:31

Essa tool consulta o sistema interno da loja e devolve o status.

09:35

O primeiro ato dessa conversa é o request.

09:37

Request é a mensagem de quem está pedindo alguma coisa.

09:42

A gente pode perceber que tem um exemplo como consultar CPF,

09:48

Para acompanhar a narrativa. Pense no...

09:52

Para acompanhar a narrativa,

09:54

Pense no mesmo padrão aplicado a uma tool consultar pedido,

09:57

A mesma coisa, tá? Então, o método é tools/call,

10:01

Ou seja, a mensagem está pedindo a execução de uma ferramenta.

10:03

Dentro de parênteses aparece o nome da ferramenta

10:06

e os argumentos necessários para essa chamada,

10:08

Tá? No nosso case,

10:09

Seria algo como quero chamar a tool consultar

10:12

pedido com o argumento pedido_id,

10:15

Tá? O ponto importante aqui não é decorar esse exemplo específico,

10:19

É entender o formato mental do request.

10:22

Ela diz, esta é a chamada, esta é a operação, estes são os dados.

10:27

A request tem uma expectativa clara. Quem mandou espera uma resposta.

10:31

Então, quando você vê uma request, pense, isso abriu uma pendência.

10:35

Repara também que existe um ID no exemplo.

10:37

Por enquanto, basta notar que ele acompanha a chamada.

10:40

A gente vai tratar com calma mais para frente,

10:42

Como eu já tinha falado antes. Então, aqui o foco é mais direto. Request é pedido.

10:47

No nosso case, é o assistente dizendo ao server, consulta esse pedido para mim.

10:52

Se request é a pendência, o próximo passo natural é entender como aparece a resposta.

10:57

Vamos lá? Bem, response, que é o segundo ato. Se request é a pendência,

11:03

Response fecha essa pendência.

11:04

Vamos continuar com o case de e-commerce. O assistente pediu,

11:08

consulta o pedido 1, 2, 3. Agora o server precisa voltar dizendo o que aconteceu.

11:12

Existem dois caminhos. Ou a consulta deu certo ou a consulta falhou. Em JSON-RPC,

11:18

Isso aparece de forma muito clara.

11:20

A response tem exatamente um dos campos, result ou error.

11:25

Nunca os dois. Então, se veio result, a operação reproduziu uma resposta válida.

11:30

No nosso case, poderia ser pedido encontrado,

11:33

Status enviado, previsão de entrega amanhã.

11:37

Se veio error, a operação falhou de forma estruturada.

11:40

Por exemplo... Pedido não encontrado,

11:42

Parâmetro inválido, usuário sem permissão ou falha interna do servidor.

11:46

Esse ponto é fundamental,

11:48

Porque JSON-RPC separa duas coisas que muita gente mistura.

11:52

O transporte da mensagem e o resultado da operação.

11:55

Quando o JSON-RPC trafega sobre HTTP,

11:58

é possível que o HTTP diga a mensagem foi entregue,

12:01

mas o corpo da mensagem diga, porém, a operação falhou.

12:06

Então o HTTP 200 não significa necessariamente o sucesso da operação.

12:10

Ele pode significar apenas que a comunicação aconteceu.

12:13

A verdade operacional está no JSON-RPC.

12:17

Para um modelo usando ferramentas, essa diferença é essencial, pessoal.

12:21

Result é algo que pode ser usado. Error é algo que precisa ser tratado. Então,

12:26

de novo, ainda vamos falar dos códigos de erro mais para frente.

12:32

Mas, por enquanto, o essencial é a resposta e a declaração do desfecho.

12:36

Sucesso em result, falha em error.

12:40

Agora, falta o terceiro tipo de mensagem, aquela que não pede e não responde nada,

12:44

apenas sinaliza, que é o notification, nosso terceiro ato.

12:49

Ela não está pedindo uma resposta, ela não está fechando o request anterior,

12:53

ela não está sinalizando que algo aconteceu.

12:56

Vamos continuar com o mesmo case.

12:59

O assistente pediu a consulta de um pedido. O server começou a processar.

13:03

Talvez a consulta dependa de um sistema externo de logística,

13:06

por exemplo. Talvez demore alguns segundos,

13:08

inclusive. Durante esse processo, o server pode querer sinalizar progresso.

13:12

Algo como consulta iniciada,

13:14

buscando dados da transportadora, status atualizado. Isso não é uma nova pergunta.

13:20

Também não é necessariamente a resposta final. É um aviso dentro do fluxo.

13:25

Por isso a notification não tem ID.

13:27

Essa é a regra de palavra. Notification não tem ID.

13:29

E aqui é importante não interpretar essa ausência como erro.

13:33

Neste caso, ausência é o próprio significado.

13:37

Então, a mensagem está dizendo, registre este evento,

13:41

mas não abra uma nova pendência.

13:43

No exemplo do slide, temos notifications / initialized.

13:47

Esse tipo de mensagem pode aparecer para sinalizar

13:50

uma etapa do fluxo de inicialização.

13:52

Quando a lógica é a mesma para progresso,

13:55

cancelamento ou mensagens estruturadas. Desculpa,

13:58

mas a lógica é a mesma para progresso, cancelamento ou mensagens estruturadas.

14:03

No caso do e-commerce... Request é o assistente pedindo a consulta do pedido.

14:08

Response é o server devolvendo o status ou um erro.

14:11

Notification é o server avisando algo no meio do caminho sem pedir resposta.

14:16

Essa distinção é útil quando você está lendo logs. Se você vê uma notification,

14:21

não deve procurar automaticamente uma resposta correspondente.

14:24

Ela pode não existir e isso pode estar correto.

14:27

Então a leitura prática é, tem expectativa de retorno? Se não tem,

14:32

provavelmente estamos diante de uma sinalização de evento.

14:34

Agora que os três papéis estão claros, podemos entrar no problema diferente.

14:38

O que acontece quando várias chamadas estão acontecendo ao mesmo tempo?

14:42

Bem, os IDs e o paralelismo. Então, agora sim, vamos falar do ID.

14:48

Até aqui, ele apareceu como parte da mensagem.

14:51

Mas o valor dele fica mais claro quando existe paralelismo. No caso do pedido,

14:57

A gente estava olhando para uma chamada. Agora,

14:59

Imagine o assistente fazendo mais de uma coisa ao mesmo tempo.

15:02

Ele consulta o status do pedido, consulta o cupom e consulta o prazo da entrega.

15:08

Essas três operações podem ser disparadas em sequência.

15:11

Um com ID 1, outro 2, outro 3.

15:14

O client não precisa esperar a primeira terminar para mandar a segunda.

15:18

E o server não precisa responder na mesma ordem que recebeu.

15:21

Uma operação pode ser rápida, outra pode depender de uma API externa,

15:25

outra pode ter latência maior.

15:28

Então, as respostas podem voltar fora de ordem, inclusive.

15:31

Ou seja, primeiro pode vir o ID 3,

15:33

depois o que tem o ID 1 e depois o ID 2. Isso não é um problema,

15:38

pessoal. O protocolo não exige que a ordem da resposta seja igual à ordem de envio.

15:44

O que ele precisa é garantir que cada resposta possa ser associada à chamada certa.

15:50

Essa é a grande mensagem desse slide. Então, esse é o papel do ID.

15:55

Esse é o mecanismo de correlação.

15:57

A resposta não precisa ser a primeira, segunda ou terceira.

16:00

Ela precisa carregar a identificação correta. Com isso,

16:03

o client não depende de ordem.

16:05

Ele olha para o identificador e sabe a qual operação aquela resposta pertence.

16:10

Então, desculpa, esse é o ponto que destrava o paralelismo.

16:15

Várias operações podem estar em andamento no mesmo canal lógico.

16:19

Cada uma tem seu próprio identificador e cada

16:22

resposta encontra a sua chamada original.

16:26

É isso que o slide chama de multiplexação.

16:29

Várias conversas lógicas compartilhando o mesmo caminho de comunicação.

16:33

No modelo REST tradicional,

16:35

a correlação costuma ficar amarrada ao ciclo de cada request HTTP.

16:39

No JSON-RPC, a correlação aparece dentro da própria mensagem,

16:43

que é genial. Por isso, o ID não é detalhe decorativo,

16:46

ele é coordenação mesmo. Ele tira a ordem da jogada.

16:51

Agora que entendemos a conversa, falta a gente olhar um ponto operacional.

16:56

E se a comunicação falha?

16:58

Bem, então, sem gerar trigger em ninguém aqui, gatilho, né, pessoal?

17:03

Agora vamos falar de erro, tá? É importante falar de erro também, né?

17:07

Uma integração boa, ela não é clara só quando dá certo, né?

17:11

Ela também precisa ser clara quando falha. Em JSON ou RPC,

17:15

quando uma operação falha, o erro vem estruturado.

17:17

E uma das partes mais importantes é o erro .code,

17:20

tá? Esse código classifica o tipo de problema.

17:24

Ele ajuda você a sair do diagnóstico genérico.

17:27

Deu erro para uma pergunta melhor. Que tipo de erro foi?

17:31

O primeiro código padrão é o -32.700, que é o parcerro.

17:38

Aqui o problema é que o JSON vem em vale.

17:42

Vocês vão ver o quanto isso é frequente.

17:46

A mensagem nem conseguiu ser interpretada corretamente, inclusive.

17:50

Depois, outro super famoso é o -32.600, que é o invalid request. Nesse caso,

17:56

o JSON pode até ser válido,

17:58

mas a estrutura não respeita o formato esperado pelo protocolo.

18:02

Depois, a gente tem aqui o -32.601.

18:07

É o método not found.

18:10

A operação chamada não existe ou não está disponível naquele servidor.

18:16

Tem outra aqui que acontece bastante, que é o "-32.602" ,

18:21

que é inválido de parâmetro.

18:22

Esse é muito comum. O método existe,

18:25

mas os parâmetros não vieram como o servidor esperava. Ou faltou campo,

18:29

ou veio o tipo errado, ou o esquema não bateu,

18:32

e aí você pode ter criado e adicionado os campos fora de ordem,

18:36

inclusive, o que dá um falso negativo de que faltou campo.

18:42

Bem, outro importante que acontece bastante é o "-32603", que é o Internal Error.

18:49

Aqui o servidor entendeu a request, mas falhou ao processar. Além desse,

18:54

existe uma faixa reservada para erros definidos para a implementação.

18:57

Isso permite que o servidor comunique casos específicos,

18:59

sem quebrar a lógica geral do protocolo.

19:01

A vantagem dessa padronização é operacional. O erro deixa de ser só uma frase.

19:07

Ele vira uma pista. Você consegue decidir onde investigar.

19:11

Formato do JSON, estrutura da request,

19:14

nome do método, parâmetros ou falha interna do servidor. Então a regra prática é,

19:19

quando vier erro, não leia só a mensagem textual, olhe o código.

19:24

Com esses elementos na mão, dá para voltar a uma pergunta mais arquitetural.

19:30

Por que usar esse modelo em vez de alternativas como REST ou de RPC?

19:40

A resposta começa com o cuidado.

19:44

REST não é ruim, por exemplo, quando a gente está falando por que não REST. REST não é ruim.

19:50

REST é excelente quando o problema combina com

19:53

recursos bem definidos e operações de CRUD, por exemplo.

19:57

Usuários, pedidos, produtos, documentos, ou seja, buscar,

20:01

criar, atualizar, remover. Ou seja,

20:03

para esse tipo de cenário, o REST encaixa muito bem.

20:06

O problema é que MCP tem uma dinâmica diferente.

20:09

Não é apenas buscar ou alterar recursos.

20:11

Essa coordenação entre client e server, modelo e capacidade,

20:15

existe coordenação entre client e server, modelo e capacidades externas.

20:20

Quando a conversa precisa envolver progresso, cancelamento,

20:24

múltiplas operações e mensagens nos dois sentidos,

20:27

o last pull começa a pedir complementos. Pulling,

20:30

WebSocket, endpoints auxiliares, convenções paralelas, enfim.

20:35

Essas soluções podem funcionar, mas elas espalham a conversa.

20:40

E quanto mais lugares carregam o pedaço da conversa,

20:45

mais difícil fica operar e depurar em conjunto.

20:48

Agora, do outro lado, nós temos o gRPC. gRPC é forte. Ele tem performance,

20:55

tem streaming, tem Protobuf, tem contratos bem definidos.

20:58

E em muitos ambientes internos,

21:01

isso é excelente. Mas ele também traz custo. Toolchain, geração de código,

21:06

formato binário, curva de entrada maior.

21:08

Para comunicação entre serviços tradicionais,

21:11

esse custo pode valer a pena. Mas quando o ecossistema envolve LLMs,

21:15

ferramentas, prompts e agentes, entra outro fator, clareza semântica.

21:19

Então JSON é texto estruturado.

21:23

Isso não quer dizer que JSON faz LLM raciocinar magicamente melhor.

21:27

Quer dizer que ele oferece marcadores explícitos.

21:31

Quando o modelo vê uma estrutura com método, parâmetros, result e erro,

21:35

ele recebe pistas claras sobre o papel de cada parte da mensagem.

21:39

Isso ajuda a separar intenção, argumentos, resultados,

21:42

falha e estado da conversa, não só para a gente,

21:44

mas para os modelos também. Ou seja,

21:46

essa separação importa porque LLMs trabalham com contexto, assim como a gente.

21:51

E contexto ambíguo aumenta a chance de interpretação errada.

21:54

Um payload binário pode ser excelente para a performance entre máquinas,

21:59

mas ele é naturalmente... inspecionável,

22:06

mas ele não é naturalmente inspecionável por uma pessoa,

22:10

nem naturalmente legível dentro de uma cadeia textual de reasoning.

22:14

Então o JSON-RPC entra como uma escolha de equilíbrio.

22:18

Ele usa JSON, permite mensagens em dois sentidos,

22:20

tem correlação por ID e não exige um 2-chain pesado para começar.

22:26

Isso não significa que ele seja melhor em abstrato.

22:30

Essa comparação não é um campeonato, tá? É uma avaliação de encaixe,

22:35

beleza? Então, REST encaixa muito bem com APIs orientadas a recursos.

22:41

JNPC encaixa muito bem quando performance,

22:43

streaming e contratos fortes justificam o peso.

22:47

JNPC encaixa bem quando a prioridade é conversa estruturada, interoperabilidade,

22:53

baixo atrito operacional e clareza semântica para sistemas com LLM.

22:57

Para esse problema, ele coloca o peso no lugar certo. Bem,

23:04

aqui, a tese dessa aula, ou seja, o JSON-RPC é o padrão de formato do MCP.

23:09

Quatro campos por mensagem, três atos, códigos de erro padronizados,

23:14

e é o protocolo que carrega todas as primitivas do MCP.

23:18

Tudo isso, só, só, pronto, diz e sempre.

23:20

A nossa próxima aula, sobre calling versus MCP versus A2A, a gente se vê por lá.

## Resumo IA

[RESUMO_IA]