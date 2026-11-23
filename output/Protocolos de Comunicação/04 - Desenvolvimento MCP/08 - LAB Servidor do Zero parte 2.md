Módulo: Protocolos de Comunicação\
Aula: [LAB: Servidor do Zero parte 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18605)

## Resumo da aula

Encapsular a query de cancelamentos em um resource transforma a leitura do banco em uma visão segura e controlada do estado. Em vez de expor acesso arbitrário ao SQL, o servidor publica um JSON já preparado com os dados que o agente precisa consumir. Isso funciona como uma “foto” do estado atual dos cancelamentos: a consulta real continua no back-end, mas o contrato exposto ao agente é apenas a leitura idempotente resultante.

Uma tool genérica que recebe uma string com select mistura capability de negócio com execução arbitrária de banco, o que degrada segurança e governança. O problema não é apenas SQL injection; também há perda de previsibilidade contratual, porque o agente passaria a decidir consultas fora do domínio modelado. Em um servidor MCP, a leitura precisa nascer delimitada pelo contrato, não improvisada por texto livre.

Retomando o servidor financeiro, o prompt não serve para substituir regra de negócio, mas para enquadrar a intenção do agente como análise de retenção. Ao instruir “você é analista financeiro sênior de retenção”, o servidor delimita objetivo, critério e tipo de ação esperada. Esse enquadramento aumenta a chance de o modelo primeiro ler os cancelamentos, depois propor ações e só então tentar a operação de bônus.

O modelo não precisa receber explicitamente o nome da tool no prompt para escolhê-la corretamente. A decisão emerge da descrição semântica formada pela docstring, pela assinatura da função e pelos type hints, que já foram introduzidos anteriormente como base do contrato no FastMCP. Aqui, a camada nova é perceber que esses elementos não servem apenas para validação e documentação: eles orientam o LLM a mapear intenção textual para capability executável.

A rejeição operacional precisa sair como erro tipado e contextualizado, não como texto genérico. Quando o pedido não existe, quando o pedido não foi cancelado ou quando o bônus ultrapassa 20% do valor do pedido, a resposta correta é MCPError com -32602 (invalid params), porque a tentativa viola condições previsíveis do contrato. Isso permite que o agente interprete a falha como restrição de uso e ajuste a próxima ação sem tratar o caso como instabilidade do servidor.

A execução começa com um pedido amplo de análise das perdas financeiras, e o agente responde lendo o resource de cancelamentos e organizando um diagnóstico. O resultado inclui resumo executivo, detalhamento por cancelamento, causas como logística e preço, além de sugestões de retenção como bônus ou gift card. Esse comportamento mostra que o resource fornece contexto suficiente para uma análise útil antes de qualquer tentativa de ação.

Quando o agente recebe a instrução para reter o cliente do pedido 2 com R$ 150,00, ele cruza o valor solicitado com o estado lido anteriormente. Como o pedido vale R$ 350,00, o limite de 20% é R$ 70,00, então a operação deve ser negada. O caso é importante porque evidencia a combinação entre leitura prévia, regra de negócio e erro tipado: o agente não “inventa” a política, ele reage ao contrato do servidor.

Depois da negativa, a resposta sugere o valor máximo permitido e conduz a interação para uma alternativa válida. Ao reenviar a instrução com R$ 70,00, a operação passa a respeitar a política e se torna executável. Esse ajuste é a camada observável de governança: o erro não encerra o fluxo, ele orienta a correção automática ou assistida.

Testar um ID inexistente ou um pedido fora da lista de cancelados verifica se o servidor protege a capability contra uso fora do domínio. A mensagem informa que o pedido não aparece entre os cancelamentos registrados, o que corresponde à rejeição por parâmetro inválido no contexto daquela operação. A utilidade desse teste está em provar que a tool não aceita qualquer identificador só porque o formato numérico parece correto.

Quando a solicitação usa um valor baixo, como R$ 10,00, o agente reconhece que a quantia está dentro do teto permitido e produz um resumo financeiro da retenção. A resposta passa a discutir investimento, recuperação potencial e compra futura, porque a barreira de política já foi satisfeita. O fluxo completo fica claro: ler estado, interpretar intenção, tentar ação, receber restrição quando necessário e convergir para uma execução válida.

## Transcrição

00:02

Oi pessoal, tudo bem? Vamos agora passar pelo gabarito, tá?

00:07

Então, vamos lá. Obviamente,

00:10

a ideia aqui era que vocês complementassem o server.py, complementassem aqui,

00:16

e no final a gente ia ter um cenário mais realista,

00:23

né? Então, vamos lá.

00:25

Vamos ponto a ponto. Primeiro, pessoal, vamos ver aqui...

00:30

as primitivas por primitivas, tá?

00:33

Então, a primeira primitiva é a de resources, tá bom? Então, vamos lá.

00:37

Então, olha que interessante, pessoal.

00:38

A sacada aqui era que a primitiva de resources encapsulasse a query cancelamentos, tá?

00:44

A query cancelamentos é que, de fato,

00:46

vai fazer uma execução do banco de dados, vai fazer o select no banco.

00:50

Lembrem disso, tá? Aqui, a ideia, pessoal,

00:52

é que a gente não gere uma tool, uma função genérica,

00:58

que recebe um select, desculpa,

01:01

um parâmetro que é uma string que executa o select no banco, né?

01:03

Isso é péssima prática de programação, inclusive, questões de segurança,

01:08

que pode envolver SQL injection e tudo mais, tá? Então,

01:12

aqui é tão simples quanto o seguinte, a gente vai expor dados independentes,

01:15

tá? A gente vai pegar uma foto de como está o resultado,

01:19

que é o JSON da query cancelamento, você vai entregar pro agente, tá?

01:26

Esse é o primeiro ponto. O segundo ponto, pessoal,

01:30

é a ideia de que a gente precisa fazer o prompt para o analista,

01:35

ou seja, para que ele lide, para que ele resolva o problema como analista. Então,

01:39

você é analista financeiro sênior de retenção do nosso e-commerce,

01:43

propõe ações para conter essas perdas e avalie se

01:47

devemos emitir um bônus financeiro para reter algum cliente específico.

01:51

A ideia é que, ao colocar esse ponto aqui,

01:54

é o agente identifique que ele tem que chamar esta sua aqui debaixo, vocês podem

02:00

ver que não tá escrito o nome da sua aqui, tá? Falando basicamente essa

02:04

informação, como é que o LM ela vai ferir isso, tá? Ela vai ferir isso

02:09

baseado no docstring que tá aqui dentro ou mesmo assinatura do método. Ou seja,

02:14

informações que estão aqui nos type hints, nas descrições dos type hints,

02:20

mas o docstring é que vai gerar esse contexto semântico para o

02:26

modelo decidir que essa tool é a que tem que ser executada.

02:31

E aqui de novo, pessoal, dentro aqui, o que a gente fez?

02:34

A gente usou o MCPerError aqui em vários momentos para garantir que,

02:39

de fato, você não vai passar simplesmente um erro,

02:42

você vai passar um erro com contexto,

02:44

tá? Você vai passar o código,

02:47

que inclusive é o código do JSON-RPC,

02:51

que é o "-32602",

02:54

que é o invalid params, tá? Que a gente já viu isso aqui antes, beleza?

03:01

Mas com que contexto? Nesse caso, se passou um pedido,

03:05

um número de pedido que não é pedido,

03:07

o parâmetro é válido? Por quê? Porque o pedido não existe.

03:09

Se passou um pedido que não foi cancelado, por que o parâmetro é válido?

03:14

Porque essa operação é negada. Ele só faz sentido para pedidos que foram cancelados.

03:20

E se o valor for maior do que 20% do valor do pedido?

03:25

Também está errado, porque existe essa regra de negócio, dessa política.

03:30

Vamos ver como é que vai ser na prática, pessoal. Então,

03:33

eu pus aqui o estrelite para rodar. Está aqui.

03:38

Está aqui. Então, vamos fazer aqui. Faça uma análise financeira.

03:46

Só lembrar aqui como é que eu tinha pensado.

03:50

Faça uma análise das perdas financeiras.

03:53

Das perdas financeiras.

04:00

Faça uma análise de perdas financeiras aqui. Então, ó.

04:26

Resumo executivo. Detalhamento por cancelamento. Parará, parará, parará.

04:30

Análise por causa aí. Problema logístico.

04:32

Problema de preço. Equilíbrio estratégico. Otimizar.

04:35

Parará retenção de cliente. Prioridade média.

04:38

Oferecer bônus gift card para reter clientes insatisfeitos.

04:41

Programa de fidelização. Ó.

04:42

Gostaria que eu metisse reembolso bonificado para

04:45

tentar reter algum desses clientes?

04:47

Posso oferecer gift card de até 20 %

04:49

do valor do pedido para recuperar relacionamentos. Então, olha que legal.

04:53

Né? E vamos ver aqui, ó. É

04:56

então tente reter o cliente, vão pedir para reter

05:00

o cliente do pedido dois, tá? Então, bora

05:03

ver aqui, ó. Tente reter o cliente do pedido

05:06

dois, ó. Tente reter o cliente do pedido aí.

05:13

De dois, vamos colocar aqui um valor que não

05:17

representa, ó, é no

05:20

valor de 150 reais. Vamos ver.

05:32

Olha que interessante, pessoal.

05:35

Aqui, ele tinha lido MCP de recursos. Olha só.

05:42

Análise. Valor pedido, 350. Limite de bônus,

05:45

70 reais. Valor solicitado, 150. Operação negada.

05:48

O valor do bônus de 150 reais ultrapassa o limite de 20

05:54

do valor do pedido, que daria R$ 70,00. Isso viola a regra financeira.

06:01

Oferecer máximo permitido, R$ 70,00, em gift card e oferecer um valor intermediário.

06:05

Vou colocar aqui. Então, ofereça R$ 70,00.

06:13

Vamos até colocar aqui. Para,

06:21

ofereça R$ 70,00. Vamos ver. Beleza.

06:37

Agora, o que eu quero fazer aqui, pessoal? Eu quero tentar...

06:41

Fazer o seguinte, eu quero colocar um ID, assim, ó.

06:47

Aqui, letra B do cancelamento, aqui, ó. Agora,

06:51

retenha o cliente do pedido de ID 10.

07:04

Pessoal, o teste tá vindo atrasado aqui, tá?

07:07

Ele tá sempre vindo depois, né? Depois do próximo... Então, assim,

07:10

isso aqui é só para mostrar que ele fez o pedido aqui, ó.

07:14

Agora, vamos ver aqui, ó. Infelizmente,

07:15

com base na análise anterior que eu realizei...

07:17

O pedido ID 10 não aparece na lista de pedidos cancelados que temos.

07:22

Vou colocar aqui.

07:47

Deixa eu

07:53

pegar um que não está cancelado. Deixa eu ver aqui.

08:01

Aqui são só os que estão.

08:04

2, 3, 4. E

08:10

O pedido de ID 4. Vamos ver.

08:21

Com base na análise que fizemos anteriormente,

08:22

Pedidos de 24 também não aparecem na lista.

08:24

Pedidos cancelados que temos registrados no sistema. Excelente, pessoal.

08:28

Está super robusto. Então, vamos colocar aqui.

08:33

Eu quero daqui.

08:37

Ofereça R$10,00.

08:48

Vocês viram, pessoal, a facilidade do Estrelite cá entre nós? É muito fácil.

08:54

Então, aqui. O valor de R$10,00 é que dá 11% dentro do limite.

08:59

Resumo financeiro, investimento de retenção.

09:02

Valor recuperado, possível compra futura.

09:05

Aqui, inclusive, ele já deu um resumo de todos. Pessoal, sensacional. É isso aí.

09:13

Até a próxima.

## Resumo IA

[RESUMO_IA]