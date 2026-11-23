Módulo: Arquitetura na Era da IA\
Aula: [Checklist de produção para observabilidade com IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18763)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente falou sobre a operação de agentes e tool calling.

00:06

A ideia principal foi entender que quanto mais

00:08

autonomia de IA ganha dentro da aplicação,

00:10

mais importante fica observar e governar cada etapa do fluxo.

00:14

Agora, para a gente fechar esse módulo,

00:16

eu queria transformar tudo isso que eu acabei falando numa checklist mental

00:20

para você pensar em softwares que você pode vir a colocar em produção.

00:28

Então é o seguinte...

00:29

Quando uma feature com IA está pronta para ir para a produção,

00:33

a pergunta não deve ser apenas,

00:35

funcionou no meu ambiente? Essa é só a primeira parte.

00:39

A pergunta mais importante é, se isso der problema em produção,

00:43

eu consigo entender o que aconteceu? Então esse aí é o ponto de partida.

00:47

A primeira coisa que eu preciso ter é rastreabilidade.

00:50

Toda execução importante precisa ter um request ID,

00:54

um trace ou alguma forma de correlação.

00:57

Sem isso, quando o usuário disser que recebeu uma resposta estranha,

01:00

você não consegue reconstruir o caminho e você fica aí tentando adivinhar,

01:05

olhando ali para um monte de log solto. Depois,

01:07

eu preciso saber qual fluxo foi executado.

01:10

Foi uma chamada direta ao modelo? Foi um reg, foi uma tool calling,

01:14

foi um agente, teve cache, teve fallback, teve re-ranking.

01:18

A aplicação pediu esclarecimento, ela recusou uma resposta. Então,

01:22

esses sinais ajudam a entender não só o resultado,

01:26

mas o caminho que levou até aquele resultado.

01:29

E a próxima pergunta é, eu sei qual modelo respondeu? Isso parece bem básico,

01:35

mas é fundamental. Se você troca de modelo, muda o custo,

01:38

o latência, o formato da resposta e até o comportamento. Então, o modelo usado,

01:43

o provider, a versão de prompt e a configuração principal da chamada,

01:46

ali elas precisam estar observáveis. Não necessariamente com o prompt ali completo,

01:52

mas com os metadados suficientes para você conseguir investigar. E depois vem...

01:57

Tokens e custo. Se você não sabe quantos tokens entraram,

02:01

quantos tokens saíram e quanto foi o custo aproximado daquela execução,

02:07

você não tem controle real sobre a operação. Em sistemas com IA,

02:11

custo não é só uma métrica financeira. O custo mostra a arquitetura.

02:16

Contexto grande demais, agente com muitos passos,

02:19

tool calling repetidos e resposta longa demais aparecem primeiro ali no consumo.

02:24

E a próxima parte é...

02:27

Latência por etapa. Não basta saber que a requisição demorou 5 segundos.

02:32

Onde ela demorou? No retrieval? No re-ranking? Na ferramenta externa?

02:36

Na chamada ao modelo? No banco?

02:38

No agente repetindo um monte de passos sem quebrar o fluxo em etapas?

02:42

Você não enxerga e você tem apenas o tempo total,

02:46

mas você não entende na realidade o gargalo, tá?

02:49

E agora vem uma pergunta crítica. Eu estou capturando os dados demais?

02:56

Observabilidade não pode virar vazamento. Em desenvolvimento,

03:00

talvez faça sentido capturar a pergunta,

03:02

a resposta com um evento de debug,

03:04

se isso estiver explicitamente habilitado. Mas em produção,

03:07

A regra precisa ser mais restrita. Prompt completo,

03:11

Contexto completo, chunkings, documentos internos,

03:13

Resposta inteira e dados sensíveis não devem ir para a

03:16

Ferramenta de observabilidade sem uma política muito clara.

03:20

Outro ponto. Os dados enviados têm cardinalidade controlada?

03:25

Atributos como feature, modelo, tenant e status são úteis.

03:29

Já pergunta inteira, e-mail, resposta completa,

03:33

O conteúdo de um chunk ou um atributo que pode explodir a cardinalidade pode,

03:39

No final das contas, aumentar o custo e dificultar,

03:42

No final das contas, a análise também.

03:44

Então, o ideal é manter IDs, contagens, flags,

03:47

Nomes controlados, tempos, hashes, quando fizer sentido.

03:51

E depois disso vem governança. A aplicação tem a low list de modelos,

03:56

Ela tem limite de output tokens,

03:58

Ela tem budget por tenant ou por feature, tem limite de passos por agentes,

04:02

Tem timeout para ferramentas, tem regra para fallback,

04:05

Tem degraded mode. Se uma feature passar do orçamento,

04:09

Ela bloqueia, reduz o modelo,

04:11

Pede confirmação ou continua gastando demais sem controle?

04:14

Então, esse ponto separa observabilidade de governança.

04:18

Observabilidade mostra o que aconteceu,

04:20

Governança define o que pode acontecer.

04:23

E também eu preciso pensar em... Retenção e acesso.

04:29

Quem pode ver os traces? Por quanto tempo eles ficam guardados?

04:32

O ambiente de desenvolvimento pode ter mais detalhes que produção?

04:35

Staging precisa simular a produção?

04:37

Traces com erros ficam por mais tempo? Chamadas normais podem ser amostradas?

04:43

Esses detalhes, eles parecem operacionais, mas impactam no custo,

04:47

Na segurança e inclusive nessa parte de auditoria. E por fim,

04:51

Eu preciso conseguir responder uma pergunta simples. Por que que essa resposta...

04:56

Foi gerada. Não no sentido de expor o raciocínio interno do modelo,

05:00

Mas no sentido operacional. Qual foi a pergunta? Qual fluxo rodou?

05:05

Qual modelo respondeu? Qual contexto foi usado?

05:07

Quais ferramentas foram chamadas? Quais fontes sustentaram a resposta?

05:11

Quais limites foram aplicados? O sistema recusou ou respondeu?

05:15

Quanto custou? Quanto demorou? Então, se eu não consigo responder isso,

05:20

A feature ainda está muito frágil para ir para a produção.

05:24

Então, fechando esse módulo,

05:26

A ideia principal é que a observabilidade em sistemas com IA não é só log,

05:31

Métrica ou trace. É a capacidade de investigar comportamento,

05:34

Custo, latência, contexto, decisões e limites operacionais.

05:39

A IA traz novas possibilidades para dentro das aplicações,

05:43

Mas também traz novas formas de falha. E quanto mais importante for a feature,

05:50

Mais importante é que ela seja observável, auditável e governável desde o início.

05:58

Essa pegada, espero que você tenha tido essa ideia geral sobre observabilidade e, obviamente,

06:04

Quando você estiver nos seus sistemas com integrações ou

06:07

Com seus agentes ou com seus regs,

06:09

Etc., pense nesses pontos.

06:11

Esse módulo não veio para tentar ensinar uma montanha de ferramentas,

06:15

Mas veio para tentar abrir a sua mente na

06:17

quantidade de coisas que vão poder seguir na sua...

06:24

no seu meio profissional, nos seus projetos,

06:26

nas arquiteturas dos sistemas que você projetar,

06:28

como uma espécie de uma checklist realmente para

06:31

que você não deixe passar essas informações.

06:34

Porque o que mais acontece é realmente problemas acontecendo

06:39

em produção e você não consegue entender o que aconteceu.

06:44

E às vezes, dependendo da empresa,

06:46

dependendo do tipo de sistema que você rodou, isso pode ser muito tarde.

06:51

tarde em questões financeiras, em relações a dados,

06:54

a sensíveis e tudo mais. Então,

06:57

tome muito cuidado e saiba que observabilidade é super importante e governança,

07:02

apesar de parecer um nome burocrático e tudo mais,

07:06

saiba que cada vez está sendo mais importante porque errar,

07:10

qualquer um erra. Agora, se você conseguir trabalhar intencionalmente,

07:16

para evitar que esse erro aconteça por uma trava sua do sistema,

07:19

aí a coisa começa a ir para um outro nível. Fechou? Um grande abraço e é isso aí.

## Resumo IA

[RESUMO_IA]