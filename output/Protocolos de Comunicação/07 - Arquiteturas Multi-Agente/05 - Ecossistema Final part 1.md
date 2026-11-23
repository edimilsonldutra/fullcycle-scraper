Módulo: Protocolos de Comunicação\
Aula: [Ecossistema Final part 1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18933)

## Resumo da aula

O Resolution Center passa a operar como um sistema completo de atendimento ao cliente quando UI, orquestração, agentes remotos, legado e observabilidade são conectados em um único fluxo. O problema de negócio é simples de formular — um pedido atrasado —, mas a resposta exige coordenação entre fontes heterogêneas e responsabilidades separadas. Um agente isolado não resolve isso com segurança nem com previsibilidade operacional. A arquitetura integrada existe para distribuir execução, centralizar coordenação e preservar evolução futura sem acoplamento indevido.

A UI em Streamlit funciona como a fronteira de interação humana do sistema e deve conhecer apenas HTTP REST. Essa restrição é deliberada: a interface envia uma requisição, recebe um resultado e permanece desacoplada de protocolos internos como MCP e A2A. Quando a UI sabe demais sobre banco, agentes ou contratos internos, ela deixa de ser cliente da aplicação e passa a participar da infraestrutura. Em produção, isso torna qualquer troca de backend mais cara e mais arriscada.

Usar HTTP REST na UI não é apenas uma escolha de transporte; é uma forma de encapsular o ecossistema atrás de uma interface estável. A camada visual não precisa saber se o orquestrador consultou um banco via MCP, disparou agentes via A2A ou executou fan-out paralelo. Esse isolamento reduz vazamento de detalhes técnicos para o front-end e impede que decisões internas contaminem a experiência externa. O contrato da UI deve ser orientado ao caso de uso, não à topologia da arquitetura.

Vazamento de protocolo ocorre quando uma camada passa a depender de detalhes que pertencem a outra, como uma UI conhecer a string de conexão do Postgres ou o orquestrador acessar o banco diretamente sem passar pelo MCP. O problema não é apenas estético: a troca de uma implementação interna passa a quebrar consumidores que nunca deveriam ter conhecido esse detalhe. Encapsulamento, aqui, significa cegueira controlada entre camadas. Cada parte sabe apenas o contrato necessário para cooperar, não o mecanismo interno da outra.

Retomando o LangGraph já estabelecido, o histórico de estado pode ser exposto na UI para transformar execução em auditoria visível. Em vez de mostrar apenas a resposta final, a interface também revela a trajetória do atendimento, o que ajuda operadores a entenderem como a decisão foi construída. Isso é especialmente útil em fluxos com memória e múltiplas integrações, porque reduz opacidade sem exigir acesso direto a logs internos. A UI deixa de ser só um canal de entrada e saída e passa a ser também uma janela de inspeção do processo.

Observabilidade embutida significa incorporar a visualização operacional no próprio ambiente de uso, por exemplo com um iframe do Arise Phoenix na mesma janela da aplicação. O operador acompanha o fluxo funcional enquanto o engenheiro inspeciona traces e spans sem trocar de contexto. Essa proximidade encurta o caminho entre sintoma e diagnóstico, o que é valioso em sistemas distribuídos com múltiplos pontos de falha. OpenTelemetry continua sendo a base da instrumentação; o Phoenix entra como superfície de análise integrada.

A separação entre coordenação e execução fica explícita quando o LangGraph decide o fluxo, mas não realiza o trabalho especializado de domínio. O orquestrador classifica o problema, escolhe integrações, dispara consultas e consolida resultados; já estoque, logística e banco respondem por suas próprias capacidades. Essa divisão evita que a lógica central vire um monólito cognitivo que sabe demais e faz demais. Em ecossistemas multiagente, escalar com segurança depende mais dessa fronteira do que da sofisticação isolada de qualquer componente.

O critique node é o ponto em que respostas parciais deixam de ser apenas saídas independentes e passam a compor uma decisão final validada. Ele recebe resultados de múltiplas fontes, verifica consistência, resolve tensões entre evidências e produz a estrutura final que seguirá para a UI. Esse nó é especialmente importante quando há LLM no fluxo, porque a síntese precisa ser governada e não apenas concatenada. Sem uma etapa explícita de crítica, o sistema corre o risco de devolver respostas plausíveis, porém incoerentes entre si.

Lembra da separação entre orquestrador local e agente remoto: aqui ela aparece na forma quase final do ecossistema. Estoque e logística não são funções internas do grafo, mas APIs autônomas em outros processos, cada uma com sua própria lógica e possivelmente seu próprio LLM. O orquestrador envia contexto e espera um JSON de resposta, sem microgerenciar a implementação remota. Esse desenho preserva especialização, independência de deploy e evolução isolada dos serviços.

O MCP atua aqui como blindagem do banco legado, impedindo que a LLM trate o PostgreSQL como um espaço livre para inventar schema ou emitir SQL destrutivo. Em vez de gerar consultas arbitrárias, o agente invoca uma tool controlada, como db_query, cujo servidor traduz a intenção para acesso seguro via SQLAlchemy. O banco continua acessível ao ecossistema, mas por uma superfície estreita e governada. Essa mediação reduz risco operacional e transforma o legado em capacidade consumível sem expor sua estrutura interna.

No fluxo integrado, o cliente informa na UI que o pedido atrasou, o planner identifica a natureza do caso e aciona o investigador para consultar o dossiê financeiro via MCP. Em seguida, o orquestrador faz fan-out para estoque e logística, consolidando evidências paralelas sobre disponibilidade e transporte. O critique node valida o conjunto e produz um JSON final, que a UI converte em resposta empática para o cliente. O resultado é um atendimento ponta a ponta em que cada camada cumpre um papel específico sem invadir a responsabilidade da outra.

Quando uma execução falha, a pergunta operacional não é apenas “deu erro?”, mas “em qual nó, integração ou serviço a falha surgiu?”. Com traces distribuídos visíveis no Phoenix, fica possível localizar se a latência veio do MCP, se um agente A2A retornou erro ou se o gargalo apareceu na própria orquestração. Essa capacidade separa protótipo de sistema operável, porque reduz tempo de diagnóstico e sustenta manutenção contínua. Modularidade, observabilidade e distribuição formam o tripé que permite ao sistema degradar sem colapsar.

## Transcrição

00:01

Oi pessoal, bem-vindos ao ápice da nossa jornada.

00:04

Hoje não é dia de teoria, é dia de construir, tá?

00:08

Nas últimas aulas vimos blocos isolados.

00:10

Hoje vamos orquestrar o caos e conectar absolutamente

00:13

tudo em um ecossistema de resolução,

00:15

que é o Resolution Center,

00:17

tá? Em apenas alguns minutos, tá? Ou seja,

00:20

apertem o cinto porque nós vamos construir aqui a nível de produção, tá, galera?

00:26

Qual é a nossa meta?

00:27

A gente vai rodar um lab que simula o coração de

00:30

um painel de atendimento ao cliente de um grande varejista.

00:33

O cliente vai reclamar de um pedido atrasado, em vez de um

00:36

humano caçar telas e bancos

00:45

de dados. Desculpa, nosso ecossistema vai de forma autônoma entender o problema,

00:48

cruzar dados financeiros do banco local com armazéns logísticos remotos.

00:53

Criar a própria resposta e devolver algo pronto.

00:56

E tudo isso amarrado com observabilidade.

01:00

Então, por que vamos fazer isso aqui tudo junto, pessoal,

01:03

que vocês estão vendo na tela? Porque no mundo real, um agente sozinho,

01:06

o mais inteligente que seja, não resolve problemas complexos.

01:09

As empresas possuem silos de dados, banco financeiro, ERP de logística,

01:13

API do fornecedor. E esse projeto existe para provar que a união,

01:17

o LengGraph, como maestro, MCP como banco de dados legado,

01:21

e o A2A para serviços de terceiros é o estado

01:23

da arte da engenharia de software de IA atual.

01:27

Aqui está um raio-x da nossa arquitetura.

01:30

Primeiro, a UI. Nosso front-end premium é em Streamlit. A UI só conhece HTTP REST.

01:36

Ele envia o post e espera o resultado. Não sabe nada de A2A nem de MCP.

01:42

Segundo, o LengGraph, nosso orquestrador cognitivo, é a nossa máquina de estados.

01:47

Terceiro e quarto, a infraestrutura é distribuída.

01:50

Ele dispara chamadas para agentes remotos de estoque e logística via

01:54

protocolo H2A e acessa o banco de dados via MCP local.

01:58

E aqui vai a provocação mental.

02:00

Se a UI soubesse a string de conexão do Postgres ou

02:03

se o LengGraph batesse direto no banco burlão do MCP,

02:06

vocês estariam vazando o protocolo.

02:09

Isso quebra o encapsulamento. Se o banco mudar amanhã, é que o sistema desmorona.

02:14

Cada camada tem que ser cega o suficiente para a implementação da outra.

02:21

Bem, é a camada 1. Vamos agora um por um, tá?

02:24

Que é o Front-End Premium, né? Que eu chamei, que é o Streamlit,

02:27

né? Então, esqueça aqueles terminais pretos, ó. Tem três coisas para gravar aqui.

02:31

Primeiro, rica interatividade. O cliente interage com algo visualmente impecável.

02:35

Segundo, a máquina do tempo. Olha esse código, pessoal.

02:38

O Streamlit puxa o histórico de estado do LengGraph e printa na tela.

02:43

É auditoria nativa e transparente.

02:45

Terceiro, observabilidade embutida.

02:47

Nós subimos um iframe do Arise Phoenix na mesma janela.

02:51

O operador vê o fluxo e o engenheiro vê o trace.

02:56

Agora na camada 2. Por que usar o LengGraph e não apenas um monte de if-else,

02:59

pessoal? Porque isso aqui é uma máquina de estado autônoma.

03:02

Olha o roteamento. O planner decide se o problema é de banco, ou seja, MCP,

03:07

ou de logística, que aí ele vai usar o E2A. Olha o paralelismo.

03:11

Ele faz o fanout. Ele chama o estoque e logística ao mesmo tempo.

03:15

Se cada um leva 2 segundos, não levamos 4, levamos 2.

03:18

E o critique é o nó que junta tudo, valida e manda para o i.

03:22

Isso aqui também, gente, o critique é um dos pontos-chave da gente usar LLM aqui. Camada 3.

03:28

Vocês acham que logística é só a funçãozinha calcular frete dentro do orquestrador?

03:33

Errado. Elas são APIs autônomas, rodando em outras portas. Então,

03:38

cada um tem seu próprio LLM. O orquestrador manda o contexto e fala.

03:41

Resolve. Ele não microgerencia como o agente de logística faz o trabalho.

03:47

Ele só quer o JSON da resposta final, descentralização real.

03:52

Agora tem o legado.

03:53

Como conectar uma LLM a um PostgreSQL sem ela inventar

03:56

tabelas que não existem ou fazer um drop table?

03:58

Nós isolamos o banco com o MCP.

04:00

O agente não manda string SQL, ele invoca a tua DB query.

04:05

O nosso servidor roda o SQLAlchemy por baixo dos panos.

04:09

Puxa a tupla...

04:12

Academy, gente, desculpa. Roda o SQLAlchemy por baixo dos panos.

04:18

Puxa a tupla e devolve o texto seguro para a LLM analisar.

04:21

O MCP é a sua camada de blindagem contra alucinações destrutivas.

04:27

Bora resumir a orquestra inteira em menos de 3 segundos de latência.

04:32

O cliente grita na Wi-Fi. O pedido atrasou.

04:34

O Planner captura a intenção e chama o investigador.

04:37

O investigador vira para o MCP e puxa o dossiê financeiro. Ah, foi pago.

04:42

Fan out agora. O Planner atira para estoque e logística simultaneamente.

04:46

E o Critique pega tudo.

04:48

Temos o produto na fila X e o frete está normal. E cospe o JSON final.

04:52

A UI renderiza uma resposta empática. Tudo isso perfeitamente rastreável no gráfico.

04:58

Isso é o que o sistema falha. De quem é a culpa?

05:00

Onde estourou? Sem isso aqui, pessoal,

05:03

vocês perdem semanas debugando. Com o OpenTelemetry mais o Arise Phoenix,

05:08

nós vemos a árvore de Spans.

05:11

E o Phoenix desenha exatamente em qual nó do Langraph a chamada para o MCP demorou.

05:16

Ou qual API remota o A2A retornou erro.

05:20

Instrumentação não é luxo, tá?

05:22

É o que separa o seu protótipo de brincadeira de uma arquitetura cooperativa séria.

05:27

E com isso, vamos para a IDE, pessoal.

05:30

Reproduzir na própria máquina a base do que roda

05:33

nas maiores empresas tecnológicas do mundo hoje.

05:35

A frase que vocês têm que levar é que o sistema bom é modular,

05:38

observável e distribuído. Se a gente cai, o sistema sofre, mas não desmorona. Então, vamos lá.

## Resumo IA

[RESUMO_IA]