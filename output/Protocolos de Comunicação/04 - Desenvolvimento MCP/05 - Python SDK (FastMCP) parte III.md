Módulo: Protocolos de Comunicação\
Aula: [Python SDK (FastMCP) parte III](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18602)

## Resumo da aula

O fluxo começa pela leitura do pedido via resource, porque é esse estado persistido que determina o que o agente pode concluir e quais ações ainda fazem sentido. Retomando o cenário de pedidos, a decisão não nasce de texto livre do usuário, mas dos dados estruturados do pedido: status, previsão de entrega, CEP e histórico operacional. Isso evita respostas especulativas e reduz o risco de o agente agir com base em contexto incompleto ou desatualizado.

O resource funciona aqui como ponto de entrada operacional do agente: ele lê o pedido 8, identifica que há atraso e extrai o CEP para aprofundar a análise. A leitura inicial organiza o restante da execução, porque os próximos passos deixam de ser genéricos e passam a ser condicionados pelo conteúdo retornado. Em vez de chamar capacidades aleatórias, o agente encadeia consultas a partir do estado observado.

A consulta externa de CEP adiciona contexto que não estava originalmente no pedido exposto ao agente, como rua e dados de localização. Esse enriquecimento existe porque certas decisões e comunicações exigem mais do que o estado interno do sistema; elas dependem de informação complementar obtida fora do banco principal. O ponto importante não é apenas “consultar uma API”, mas transformar um identificador já presente no pedido em contexto útil para análise e resposta.

A elegibilidade para frete prioritário não é inferida por linguagem natural; ela é concluída a partir de campos verificáveis, como atraso e estado atual do pedido. Quando o agente lê datas, compara previsão com data corrente e combina isso com o status operacional, a decisão se torna auditável e reproduzível. Esse padrão é essencial em fluxos de negócio, porque permite justificar por que uma ação foi sugerida, executada ou bloqueada.

Verificar se o frete prioritário já estava ativo impede ação duplicada e mantém o servidor idempotente do ponto de vista operacional do agente. No exemplo, o pedido qualifica para frete prioritário, mas a resposta informa que o upgrade já havia sido realizado em operação anterior. Essa checagem transforma o estado do pedido em mecanismo de proteção contra redundância, evitando repetir efeitos colaterais desnecessários.

Lembra das primitivas já estabelecidas? Aqui elas cooperam em sequência: o resource lê o pedido, a consulta externa enriquece o contexto e o prompt governa a forma da comunicação final. O valor arquitetural dessa composição está em separar aquisição de dados, decisão operacional e linguagem de saída, sem misturar tudo em uma única capability opaca.

A comunicação ao cliente não é gerada apenas com base em fatos; ela também precisa obedecer a diretrizes de tom, estrutura e identidade da empresa. Por isso, o agente usa um template parametrizado para redigir o e-mail do pedido 2, preenchendo nome, situação do pedido e elementos institucionais como assinatura e oferta. Governança de linguagem significa limitar a variabilidade do texto final para preservar consistência de atendimento, mesmo quando a redação é automatizada.

O agente atua como coordenador do fluxo, não como fonte primária da verdade do negócio. Ele consulta o resource correto, decide quando chamar a API externa, verifica o estado atual e só então produz a comunicação adequada. LangChain entra como camada de orquestração dessa sequência, conectando capacidades MCP sem deslocar regras de negócio para fora do servidor.

No pedido 8, a execução segue uma cadeia clara: ler o pedido, detectar atraso, extrair o CEP, consultar a API externa, obter a rua, verificar elegibilidade para frete prioritário e confirmar se a ação já havia sido aplicada. O resultado não é apenas uma resposta textual; é uma síntese de estado, contexto enriquecido e decisão operacional. No pedido 2, o fluxo muda de objetivo: o agente lê o estado atualizado e usa o prompt de comunicação para gerar um e-mail amigável informando o reembolso com linguagem alinhada à política da empresa.

## Transcrição

00:00

Bom, pessoal, descobri. Tinha um probleminha aqui no nosso banco de dados.

00:06

Mas problema resolvido.

00:09

Vamos agora voltar ao ponto que a gente estava.

00:13

Vamos lá. Na verdade, agora eu quero conversar. Eu quero fazer esse pedido aqui.

00:17

Gera um e-mail para o cliente do pedido 2.

00:23

Desculpa. Não, eu não quero esse aqui agora, não. Eu quero o seguinte. Desculpa.

00:33

A gente precisa ver o do CEP sendo executado.

00:40

Então, aqui é aquele, consulta o status do pedido 8,

00:42

se ele estiver atrasado, verifica o CEP dele,

00:44

me diga a rua e se ele qualifica para um FET prioritário. Então, vamos lá.

00:50

Olha o que ele fez aqui.

00:51

Ele executou o recurso com o pedido 8, tá bom?

00:56

Depois, ele fez a consulta do CEP, passando o CEP, coisa que a gente não tinha antes,

01:00

processou aqui, deu ok, perfeito.

01:04

Aqui estão as informações solicitadas para o pedido 8,

01:06

a análise que eu pego do pedido: status de atraso,

01:09

data de previsão de entrega 1 do 6,

01:11

data atual 2 do 6, status atrasado.

01:15

Informações de localização do CEP. Aqui tem as informações,

01:18

tudo bonitinho. Resultado final,

01:21

pedido 8 qualifica para FET prioritário e

01:23

já foi upgradeado com sucesso na operação anterior.

01:29

Então, aqui é o resumo dessa informação.

01:32

Então, de novo, gente, a gente leu o recurso do pedido, identificou o CEP,

01:36

chamou a PI externa de CEP para pegar o endereço

01:39

e confirmou que o frete prioritário já estava ativo.

01:42

Agora eu vou pedir para ele gerar uma comunicação

01:45

formal personalizada baseada no status desse pedido, tá?

01:49

Então, vamos aqui.

02:00

Já o e-mail para o cliente do pedido 2,

02:02

contou a amigável explicando que ele foi reembolsado. Vamos

02:08

lá, e-mail para o cliente 2. Para Ana.

02:12

Seu reembolso foi processado com sucesso. Ana Silva,

02:16

esperamos que esteja bem. Estamos entrando em contato para informar.

02:20

Ou seja, ele usou aquela template do pedido 2,

02:23

pegou as informações do pedido 2, inseriu aqui.

02:26

Então, o que mudou?

02:28

Saímos... Aliás, sabemos que isso pode ser frustrante.

02:32

Ou seja, de novo, ele usou a template.

02:35

Acho que é importante, ele usou aquela template lá de geração de e-mails,

02:40

até falou aqui, suporte, loja, arroba,

02:43

até o DDD 31, parará, equipe de atendimento ao cliente,

02:47

sua loja de e-commerce, aproveite um desconto especial de 15%. Pessoal,

02:50

o agente buscou o status atualizado do pedido via recurso e redigiu

02:55

a mensagem de pós-atendimento perfeitamente alinhada com as diretrizes da empresa,

02:58

tá, pessoal? Basicamente... os nossos prompts lá.

03:01

Essa flexibilidade prova o poder de ter o

03:04

Langchain orquestrando o servidor MCP completo,

03:06

tools, sources e prompts.

03:07

Com isso, nós finalizamos o nosso laboratório e nos vemos no próximo módulo. Fechado? Valeu!

## Resumo IA

[RESUMO_IA]