Módulo: Protocolos de Comunicação\
Aula: [Multi-Turno e Input Required](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18623)

## Resumo da aula

Input required é a resposta correta quando o agente não pode concluir a execução com segurança ou precisão. Isso acontece em três situações centrais: campo faltante, ambiguidade de intenção e ação destrutiva. Nesses casos, o erro não está no formato da requisição, mas na insuficiência de contexto de negócio para continuar. O comportamento correto é pausar a mesma Task e pedir exatamente a informação que falta.

Campo faltante ocorre quando a requisição é estruturalmente válida, mas omite um dado indispensável para produzir uma resposta correta. Se o cliente pede 500 licenças sem informar a região fiscal, o agente não deve inferir um valor provável com base em padrão estatístico. A inferência silenciosa cria alucinação operacional, que é difícil de detectar e cara de corrigir. A pausa com pergunta precisa transforma incerteza implícita em coleta explícita de contexto.

Ambiguidade aparece quando há dados suficientes para agir, mas não para decidir qual ação específica executar. Um pedido como “enviar contrato” pode corresponder a vários contratos ativos do mesmo cliente, e o agente não deve escolher arbitrariamente. Nesse caso, a pergunta de desambiguação reduz risco de ação incorreta sem tratar a situação como falha técnica. O uso de textPart aqui serve para listar opções e solicitar uma escolha clara.

Ação destrutiva exige uma trava deliberada antes da execução, mesmo quando o agente entendeu o pedido. Comandos como “cancelar tudo” ou operações irreversíveis não devem ser executados sem confirmação explícita. Esse padrão implementa human-in-the-loop como controle arquitetural, não como detalhe de interface. A pausa em input required funciona como barreira de segurança contra excessive agency.

Retomando o lifecycle da Task já estabelecido, o caminho normal continua sendo submitted → working → estado terminal. A novidade é a ramificação para input required, que não representa falha, mas suspensão controlada da execução. Quando o cliente responde, a mesma Task retorna para working, preservando ID, contexto e histórico. O protocolo trata a conversa multi-turno como continuação da mesma unidade de trabalho, não como nova submissão.

HTTP 400 deve ser usado para erro de esquema: JSON malformado, tipo inválido ou campo obrigatório ausente no contrato de entrada. Input required deve ser usado quando a estrutura está correta, mas falta contexto de negócio ou existe ambiguidade operacional. Essa distinção evita misturar validação sintática com coleta de contexto. A regra prática é simples: erro de contrato falha a requisição; falta de contexto pausa a Task.

O fluxo começa lendo a mensagem mais recente do history e aplicando uma validação de negócio sobre o conteúdo. Se a validação detectar campos faltantes ou necessidade de confirmação, o agente anexa uma nova mensagem à própria Task, muda o status para input required e encerra o handler com return. Isso é importante porque o servidor não deve bloquear thread nem manter loop de espera. Quando a resposta chega, o handler é invocado novamente com o histórico acumulado e continua o processamento.

Lembra do history, já usado antes como registro conversacional? Aqui ele ganha papel operacional decisivo: cada turno é anexado à mesma Task e forma um log auditável e replayable. Isso elimina a necessidade de o cliente repetir o pedido original e permite depuração posterior com contexto completo. Em multi-turno, perder histórico significa perder a própria continuidade da execução.

A pausa precisa ser observável imediatamente pelo cliente, usando SSE ou webhook, já vistos anteriormente como canais de acompanhamento. O servidor muda o estado para input required e publica o evento sem depender de polling como mecanismo principal. Polling com status inventado, como needs_info, quebra a padronização do A2A e introduz dívida técnica desnecessária. A retomada correta acontece no mesmo protocolo e no mesmo wire.

Pergunta ruim aumenta o número de turnos e degrada a experiência do cliente. A formulação correta nomeia o campo faltante, faz uma pergunta por vez, oferece exemplo de formato e lista opções quando o domínio é finito. Também é necessário validar o que já foi informado antes de perguntar novamente. Uma boa pergunta reduz erro de retorno e evita poluir o history com ciclos de correção desnecessários.

Quando a resposta esperada do cliente precisa voltar como estrutura tipada, dataPart é mais adequado que textPart. Isso evita parsing frágil por regex e permite retomar a execução com dados já normalizados. Em fluxos multi-turno, a escolha entre texto livre e payload estruturado afeta diretamente robustez do handler. Use textPart para desambiguação textual e dataPart quando o retorno precisa ser consumido programaticamente.

A pausa deve ocorrer antes de qualquer ação irreversível, nunca depois. Ao entrar em input required, o servidor precisa notificar imediatamente o cliente pelo canal de acompanhamento configurado. Quando a conversa terminar, a Task ainda deve publicar um artifact, porque múltiplos turnos não eliminam a obrigação de entregar um resultado formal. O fluxo correto não inventa contexto, não reinicia a execução do zero e não substitui o protocolo por placeholders ad hoc.

## Transcrição

00:01

Pessoal, bem-vindos de volta ao nosso módulo de desenvolvimento A2A.

00:06

No mundo real,

00:08

o usuário geralmente pode mandar um prompt incompleto.

00:14

Ele pode faltar um parâmetro crítico ou pedir sem ambiguidade.

00:18

Ou seja, é não determinístico,

00:20

assim como a IA. Ou a gente está prestes a executar algo destrutivo,

00:25

por exemplo, sem uma confirmação. Então, pensa nesse cenário.

00:31

O que o sistema faz? Ele não pode alucinar uma resposta para tentar ser útil.

00:35

E você também não quer devolver um erro genérico na tela do cliente.

00:39

Então, como o próprio subtítulo diz,

00:44

aqui o agente precisa de mais dados para prosseguir.

00:48

Então, exatamente esse gap que a gente fecha hoje é o Multiturn Input Required.

00:53

Vamos para o próximo slide para entender onde esse padrão se encaixa melhor.

00:58

Antes, primeiro, vamos dar uma olhada como é que a aula está dividida. Então, olha só.

01:06

Primeiro, a gente começa pelos cenários, ou seja,

01:08

em que situações reais o agente precisa pausar e pedir mais dados.

01:12

Ou seja, vamos ver três casos que aparecem o tempo todo em produção.

01:16

Depois, a gente sobe para a máquina de estados. A pergunta aqui é,

01:19

como que essa pausa se traduz em transições formais?

01:23

E o que acontece com o ciclo de vida da TESC?

01:26

Quando a gente entra em Input Required e o que acontece quando o cliente responde? Ou seja,

01:31

é que existem de fato pontos que são críticos,

01:37

que precisam ser validados e no final do dia esse fluxo tem que ser fluido.

01:43

Na sequência, tem implementação prática. A gente vai abrir o Reader,

01:47

ver o código que valida, como é que pausa e retorna,

01:51

e entender como o History acumula o contexto entre

01:55

os turnos da conversa sem perder nada, que isso é super importante.

01:58

E, por último, o trade-off de boas práticas.

02:01

Por que a pergunta que eu mais recebo é por que não usar um HTTP 400 e pronto? Ou seja,

02:07

a gente vai comparar as alternativas e entender...

02:09

Quando cada um faz sentido e fechar em um checklist operacional

02:13

de como formular a pergunta certa para o cliente.

02:15

Então é isso, tá? Vamos lá.

02:19

Bem, então quando exatamente a gente deve pausar e pedir mais dados?

02:23

Vamos olhar os três cenários clássicos.

02:26

Cada coluna é um caso que vocês vão encontrar em produção.

02:29

Primeira à esquerda é o campo faltante.

02:31

O cliente pede 500 licenças,

02:36

mas omite a região fiscal.

02:40

E aqui vem a armadilha. Um agente mal projetado vai tentar resolver.

02:44

Vai alucinar São Paulo, porque é o padrão mais comum no dataset dele,

02:48

e vai devolver a cota errada com toda a confiança do mundo.

02:52

O agente correto não inventa.

02:55

Ele entra em Input Required e devolve uma pergunta precisa.

02:58

Qual região fiscal? Ou seja, parece óbvio,

03:01

mas em produção esse tipo de alucinação silenciosa é

03:04

um dos bugs mais caros de detectar.

03:07

Segundo cenário.

03:10

Ambiguidade. Ou seja, o cliente manda enviar contrato.

03:13

O agente consulta o banco e conta três contratos ativos com o mesmo cliente.

03:18

Qual dos três? Em vez de chutar ou falhar com o erro genérico,

03:22

ele envia um text part de desambiguação listando os

03:25

três e pedindo para o cliente escolher.

03:28

Repare que aqui o agente tem informação suficiente para agir.

03:31

Ele só não tem certeza de qual ação tomar.

03:34

É o caso que é bem diferente do anterior.

03:37

E o terceiro, à direita, que é o mais crítico,

03:40

a ação destrutiva. O cliente manda cancelar tudo.

03:44

E esse é um caso de segurança arquitetural. Ou seja,

03:49

o ASP tem uma categoria específica para isso.

03:52

Excessive Agents. Ou seja,

03:54

quando o agente tem poder demais e executa sem validação humana.

03:58

Aqui, a gente força o input required como trava de segurança,

04:02

exigindo confirmação explícita antes de qualquer operação irreversível.

04:06

É o clássico Hume in the loop.

04:09

Então, são três motivações diferentes.

04:12

Dado faltante, intenção ambígua e proteção contra ação destrutiva.

04:16

Agora, a pergunta é,

04:17

como a máquina de status lida com essa pausa? Bem,

04:21

agora vamos ver como esses cenários que a gente

04:24

acabou de discutir se traduzem em status formais.

04:27

Então, olha só o diagrama, pessoal.

04:29

Caminho feliz você já conhece. A task entra em submitted,

04:33

transiciona para o work e termina em um dos três estados finais,

04:37

que é completed, failed ou canceled. E isso não muda.

04:41

O que muda é essa ramificação putilhada ali embaixo. Repara,

04:45

quando a gente detecta um dos três cenários que a gente acabou de ver,

04:49

campo faltante, ambiguidade, ação destrutiva, ele não falha a task.

04:53

Ele transiciona para input required.

04:56

E olha a anotação do lado, olha.

04:58

O agente envia a pergunta via text e parte no history.

05:01

Ele não abre um canal separado, ele não cria uma task nova,

05:05

ele anexa a pergunta na mesma task e muda o estado.

05:08

Agora, a parte mais importante do diagrama, a seta de volta.

05:12

Quando o cliente responde, a task volta para o working. A mesma task,

05:17

mesmo ID, mesmo contexto, mesmo history. Só que agora com a informação que faltava.

05:22

A execução retoma de onde parou.

05:25

Lembra do taskUpdate, pessoal?

05:28

Lá a gente viu o método updateStatus com input required como uma das opções.

05:32

Agora vocês estão vendo onde ele se encaixa no fluxo completo.

05:36

E como que isso fica no código?

05:39

Vamos lá. Esse slide é o coração prático da aula.

05:42

Então, vamos percorrer o código linha a linha.

05:44

Primeiro a gente extrai o texto da última mensagem do history, taskHistory -1.

05:50

Sempre a mensagem mais recente do cliente.

05:54

Em seguida, joga uma função de validação de negócio. Olha o comentário ali,

05:59

o retorno é um dicionário com os campos que faltam. No exemplo, região 2.9.

06:05

Agora, vem o ponto-chave, o if faltando. Se a validação acusa algo incompleto,

06:11

o que a gente faz? Olha a sequência. Primeiro,

06:14

dá um append no history da task com a mensagem do agente.

06:17

Repare que a mensagem é precisa, no meio campo,

06:20

dá exemplo de formato. Não é um dado faltando genérico.

06:23

Isso conecta diretamente com o que a gente vai

06:25

ver mais para frente sobre qualidade da pergunta.

06:28

Depois, seta o status para input required.

06:31

E aí vem o detalhe arquitetural mais importante, o return. A execução para aqui.

06:36

A gente não fica segurando o thread, não fica em loop esperando.

06:40

O handler simplesmente sai.

06:42

O cliente vai ser notificado via HTTP,

06:49

possivelmente, ou webhook.

06:51

Exatamente como a gente vai implementar,

06:54

como a gente implementou na aula 31, na aula anterior.

07:00

E quando ele responde, o handler é invocado com o histórico já acumulado.

07:05

E ali embaixo, pessoal, separado visualmente, o caminho feliz.

07:09

Se ambos estão ok, a gente segue direto para o processamento completo.

07:13

Cabe aqui uma observação, tá?

07:15

Esse código é pseudo-código intencional, tá, pessoal? Em produção,

07:18

vocês usariam o TaskUpdater, que usa Update Status, New Agent Message, por aí vai.

07:24

A lógica é a mesma,

07:26

mas o Test Updater encapsula a emissão de eventos pelo Event Keyword.

07:31

Agora, o que acontece com o contexto dessa conversa entre turnos?

07:35

Como que nada se perde?

07:37

Bem, a gente acabou de ver como o Handler pausa. Agora, a pergunta é,

07:42

por que essa abordagem funciona sem perder informação?

07:45

São quatro propriedades. A gente vai percorrer cada uma.

07:49

É cada quadrante aqui.

07:53

Bem, vamos lá. Começando lá em cima. O histórico acumula. Ou seja, cada turno,

07:59

cliente, agente, cliente, agente, cliente, agente, é uma mensagem anexada ao array.

08:06

Aquele task.history.append que a gente viu

08:08

no código não é uma operação descartável.

08:11

Ele cria um log completo da conversa.

08:14

Auditável e, mais importante, replayável. Ou seja, a gente pode reexecutar.

08:19

Se você precisar debugar uma task que deu problema em produção,

08:22

o histórico é sua fonte de verdade.

08:26

Depois, sem perda de contexto.

08:28

O cliente não precisa reexplicar o pedido original na segunda mensagem.

08:32

A task carrega tudo via session ID e o histórico acumulado.

08:36

Quem já trabalhou com chatbots stateless sabe a dor

08:40

de forçar o usuário a repetir a informação.

08:42

Aqui isso não existe.

08:45

E agora, ali embaixo, o cliente é notificado.

08:48

Quando o Handler entra em input required,

08:50

o evento desce via HTTP stream, SSE,

08:55

Webhook. Exatamente sem pooling.

09:00

O cliente não fica perguntando, e aí,

09:03

tem novidade? Em loop, ele recebe o push e responde.

09:08

E depois, por fim, olha pessoal, resumo e continuação.

09:11

Uma conversa de cinco turnos vira uma task com history 5.

09:15

Não são cinco tasks separadas.

09:18

E no final, o artifact ainda fecha o ciclo em completed.

09:21

Aquela entrega final tangível que o TaskUpdater emite com addArtifact e complete.

09:29

Beleza, agora o modelo mental está montado, mas alguém pode perguntar,

09:32

Por que não resolver isso com o simples HTTP 400? Vamos comparar?

09:38

Então, essa é a pergunta que eu mais ouço em consultoria,

09:41

Tá? Por que não devolver um 400 e pronto?

09:44

Vamos comparar três alternativas.

09:46

Cada coluna é uma abordagem diferente para o mesmo problema.

09:49

Alternativa A, HTTP 400, Bad Request. O server devolve um erro síncrono,

09:56

O cliente lê a mensagem, corrige e reenvia do zero.

09:59

Repara no problema, reenvia do zero. Você perde o histórico inteiro.

10:03

Se o cliente já tinha passado três informações corretas e errou uma,

10:07

Ele precisa mandar tudo de novo. Para multiturno, isso não escala.

10:11

Mas, isso é importante, o 400 ainda tem seu lugar.

10:15

Ele serve para validação estrutural, de JSON mal formado,

10:19

Campo obrigatório faltando no esquema,

10:21

Tipo errado. Bem, isso é um erro de contrato, uma falta de contexto no negócio.

10:27

Agora vamos para B.

10:28

Pule em Simple Holder.

10:30

O server retorna 200 com status inventado do tipo needs info

10:34

E obriga o cliente a ficar perguntando em loop.

10:38

Vocês lembram

10:40

Que a gente fez um...

10:43

Decision Tree, pessoal, na aula passada. Olha, pooling era o último recurso,

10:48

Só para o cliente intermitente. Aqui é pior.

10:51

É pooling como mecanismo principal de interação.

10:54

Não é padrão 8-way,

10:55

Gera dívida técnica e a gente perde o SSE e o webhook de graça.

11:03

Existia antes da padronização. Não tem razão para usar hoje, pessoal.

11:08

Alternativa C. Essa aqui é oficial. Input required.

11:12

Server pausa a task. Cliente recebe via SSE Webhook.

11:17

History acumula. Mesmo wire,

11:20

Mesmo protocolo, mesmo cliente SDK.

11:22

Funciona igual para cliente web, mobile ou server.

11:26

Agora, olha a decision rule aqui embaixo.

11:28

Guarda essa regra porque ela resolve 90% das dúvidas em code review.

11:33

Erro de esquema, HTTP 400.

11:36

Falta de contexto na ambiguidade de negócio, input required.

11:39

Pule com o placeholder? Nunca, tá?

11:43

Então, a decisão de quando usar está clara.

11:47

Bem, a

11:49

Gente resolveu quando pausar e como pausar. Agora, falta o que perguntar.

11:54

Porque a engenharia mais limpa do mundo não salva um agente que faz perguntas ruins.

11:59

Olha a coluna da esquerda, a vermelha. Faltam dados. Ponto final.

12:03

Quem já integrou... Com APIs que devolvem mensagens assim,

12:06

Sabe a frustração que é, pessoal.

12:08

O cliente não sabe o que falta, não sabe o formato,

12:11

Não sabe quantos campos precisa preencher. Pede tudo de uma vez,

12:15

Sem exemplo, sem opção. O resultado? O cliente chuta,

12:19

Erra de novo e você entra no loop de input

12:21

Required que destrói a experiência e polui o histórico.

12:25

Agora, olha a coluna verde, pessoal, à direita. Repara na diferença.

12:28

Cada item é uma regra de design da pergunta.

12:31

Ó, nomeie o campo faltante. Qual região fiscal?

12:36

Não faltam dados, tá, pessoal?

12:42

Uma pergunta... Desculpa. Uma pergunta por turno.

12:47

Uma pergunta por turno.

12:49

Evita confusão de intenção. Dê exemplo do formato.

12:53

Exemplo, BR São Paulo. Lista opções quando o domínio é finito. Se são três regiões,

12:59

lista as três. E valida a prévia antes de pedir.

13:02

Checa o que você já fez antes de incomodar o cliente

13:06

com algo que ele já passou no turno anterior.

13:10

Vamos lembrar o exemplo do código nos slides anteriores.

13:15

Aquela mensagem, preciso, list, faltando, exemplo,

13:20

dois pontos, região igual São Paulo,

13:22

ela segue exatamente essas regras. Campo nomeado,

13:25

formato exemplificado e uma coisa por vez. Vamos lá.

13:32

Então, aqui é um checklist para vocês,

13:34

que vocês levam para o time, tá? Quatro regras operacionais.

13:38

Não vou ler cada uma, vocês conseguem ver, tá?

13:40

Mas vou destacar o que costuma dar errado na prática.

13:44

Segurança em camadas.

13:46

Pausa antes da ação destrutiva, parece óbvio,

13:49

mas o erro mais comum que eu vejo é o agente validar depois de executar.

13:53

O delete já rodou, aí vem a confirmação. O ASP chama isso de excessive ages.

14:00

Ou seja, a regra é simples. Se a operação é reversível,

14:02

o input required vem primeiro, sempre.

14:05

Ciclo de vida da task. Quando você espera JSON tipado de volta,

14:10

não texto livre, use data part no history em vez de text part.

14:14

Isso facilita o passing do lado do agente e evita aquela

14:18

ginástica de regex para extrair dados de uma string.

14:22

Agora, notificações.

14:23

Envie o evento SSE Webhook imediatamente ao entrar input required.

14:28

Um cliente travado esperando resposta porque o server mudou o estado,

14:31

mas não disparou notificação. É um bug clássico de timeout mascarado.

14:36

Silencioso e difícil de debugar. E o último, entrega de resultados.

14:42

Independente de quantos turnos a conversa teve,

14:44

sempre devolva um artifacto a terminar.

14:46

Task incompleta sem artifacto é uma função

14:50

que retorna void quando o chamador espera dados.

14:55

Fusta a integração e quebra a confiança do protocolo.

15:00

Bem, vamos fechar? Então vamos lá. O que vocês levam dessa aula?

15:04

Primeiro, três cenários que justificam o input required.

15:06

Campo faltante, ambiguidade e ação destrutiva.

15:09

Se o pedido cai em um desses casos,

15:11

a gente pausa. Não inventa, não falha, não ignora.

15:15

Máquina de estados. A task vai de um work para input required e volta para o work.

15:19

Mesma task, mesmo id, mesmo history, sem criar task nova, sem perder contexto.

15:25

Depois, a Decision Rule que resolve qualquer dúvida

15:29

em Code Review é Erro de esquema,

15:32

HTTP 400. Falta de contexto de código, Input Required.

15:36

Pule com o Placeholder, gente, nunca. A

15:40

qualidade da pergunta importa tanto quanto a engenharia. Campo nomeado,

15:44

uma pergunta por turno, com exemplo de formato.

15:48

E por fim, pessoal, sempre devolva um artifact ao fechar a task incompleta.

15:52

Sem entrega tangível, a integração perde confiança. Pessoal,

15:56

esse aqui é um dos slides mais importantes de tudo

15:59

que a gente viu de 8-way até agora.

16:00

Tá bom? E na próxima aula é o lab. Até mais.

## Resumo IA

[RESUMO_IA]