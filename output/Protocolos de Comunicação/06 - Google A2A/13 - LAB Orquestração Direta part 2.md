Módulo: Protocolos de Comunicação\
Aula: [LAB Orquestração Direta part 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18927)

## Resumo da aula

O agente de logística recebe um invoke_llm com prompt ancorado em um knowledge explícito. Esse grounding restringe a geração a rotas verificadas, em vez de deixar o modelo responder com conhecimento genérico. No laboratório, a base aparece hardcoded, mas a função arquitetural é a mesma de um RAG simples: injetar fatos recuperados antes da geração. Isso importa porque a resposta da logística alimenta a consolidação feita pelo estoque, então uma saída alucinada contaminaria toda a cascata.

Retomando a orquestração direta já estabelecida, a virada concreta acontece no import do helper chamar_agente. Essa função encapsula a burocracia do cliente A2A — discovery, envio de mensagem, polling e extração da resposta — para que o agente chamador não replique esse fluxo em cada integração. O efeito prático é separar a lógica de negócio da mecânica protocolar: o estoque decide quando consultar logística, mas não precisa reimplementar o ciclo completo da chamada. Uma alternativa seria instanciar o client A2A diretamente no executor, com mais controle e mais boilerplate.

O ponto mais importante do código é a chamada ao agente de logística passando o fornecedor. É nessa linha que o StockAgent, que começou atendendo o GenUI como servidor A2A, assume temporariamente o papel de cliente A2A de outro agente. Cliente e servidor, portanto, não são tipos fixos do processo; são papéis operacionais exercidos em momentos diferentes da mesma Task. Essa mudança de papel é o núcleo da orquestração direta implementada no laboratório.

Os status updates ao redor da chamada existem para preservar observabilidade durante a delegação. Antes de consultar logística, o estoque publica progresso para indicar que entrou em uma etapa dependente de outro agente; depois, publica novo update para sinalizar retomada e continuidade da consolidação. Isso evita a percepção de travamento na interface e mantém o lifecycle da Task inteligível para quem acompanha a execução. Se esses updates forem omitidos, a chamada lateral continua funcionando, mas o consumidor perde contexto operacional sobre o que está acontecendo.

A execução local do laboratório exige três processos separados: servidor do agente de logística, servidor do agente de estoque e aplicação de interface. Essa separação deixa visível a topologia real da cascata, porque cada papel roda de forma independente e pode ser inspecionado isoladamente em terminal próprio. Em troubleshooting, isso ajuda a distinguir falha de inicialização, erro na chamada A2A e problema de interface. Em produção, esses processos podem até ser distribuídos em hosts diferentes, mas a relação lógica entre eles permanece a mesma.

O GenUI enxerga somente o agente de estoque exposto na porta configurada. Isso significa que a logística não faz parte do contrato visível para a interface; ela é uma dependência interna resolvida pelo próprio estoque durante o processamento. Essa escolha reduz acoplamento no cliente e concentra a decisão de delegação no especialista que entende quando dados logísticos são necessários. Se amanhã a logística mudar de endpoint ou for substituída, o GenUI continua estável desde que o estoque preserve seu contrato.

Um mesmo agente pode alternar entre A2A server e A2A client sem quebrar a semântica do protocolo, desde que mantenha corretamente o lifecycle da Task que está atendendo. No laboratório, o estoque recebe a solicitação, delega parte do trabalho e depois consolida a resposta final para o consumidor original. Essa composição é valiosa porque aproxima a decisão de chamar outro agente do contexto de negócio que realmente sabe quando a dependência externa faz sentido. O resultado é uma arquitetura menos centralizada e mais aderente ao domínio.

Ao subir os três processos e enviar um pedido como “verifique a reposição da LG”, o comportamento esperado é a interface falar apenas com o estoque, enquanto o estoque consulta logística nos bastidores. O usuário não precisa conhecer a existência do segundo agente para receber uma resposta consolidada. Quando algo falha nesse fluxo, a inspeção deve começar pela ordem de subida dos serviços, pelas portas configuradas e pelo ponto exato em que o helper chamar_agente é invocado. Esse tipo de teste valida não só a lógica de negócio, mas também a transição real de papéis entre server e client.

## Transcrição

00:00

Olá pessoal, chegamos ao laboratório mais importante deste módulo. Até agora,

00:04

nossos clientes conversavam com um único agente por vez.

00:08

Mas no mundo real, se temos em produção,

00:10

precisamos de agentes conversando entre si, de forma autônoma ou semi -autônoma.

00:15

Tem um maestro, um coordenador central. Então,

00:18

nós vamos construir aqui um agente que atua ao mesmo tempo,

00:20

como servidor e cliente A2A.

00:22

Então, pensem no e -commerce, o usuário digita, verifique a reposição de Samsung.

00:28

Nosso front -end em Strelitz só conhece o agente de estoque.

00:31

É aqui que entra o workflow 100 % agente.

00:33

O próprio estoque entende que precisa de dados

00:36

de transporte para fechar o relatório.

00:38

De forma totalmente autônoma,

00:40

ele dispara uma chamada gateway para o agente de logística,

00:42

coleta as informações e monta a resposta final.

00:46

Para o cliente, tudo é mágico e transparente. Então,

00:49

vamos só dar uma olhada aqui no agente de logística.

00:55

Dá uma olhada no agente logístico. Ele roda na porta 9001.

00:58

O código dele já está pronto, pessoal.

00:59

Vocês não precisariam ter editado nesse laboratório.

01:04

Mas vamos dar uma olhada aqui. Vamos dar uma olhada na classe logística agent. Logística agent. Olha só.

01:28

Bem, aqui tem o invoke LLM. Tá bom? O invoco LLM, pessoal,

01:33

ele tem até um prompt. Eu vou ser analista de logística,

01:36

de e -commerce, usar apenas informações do contexto, tá? Então, neste caso aqui,

01:40

pessoal, reparem que a gente está fazendo um ground, tá? O que é o ground?

01:46

Nosso prompt injeta uma base de conhecimento com rotas verificadas. Neste caso aqui,

01:51

eu fiz uma rota hardcoded, tá, pessoal? Mas, tipicamente,

01:56

isso é uma pesquisa em banco, alguma coisa nesse sentido, tá?

02:00

Então, o modelo fica estritamente amarrado a este contexto.

02:04

Isso aqui é o equivalente ao que os sistemas de RAG fazem.

02:08

Quando a gente vai implementar o sistema de RAG, basicamente,

02:11

o RAG entrega para o agente informações que são fatos,

02:14

que a gente está entregando factualidade. Então,

02:16

se você perguntar de um fornecedor que não está lá,

02:19

ele não vai dar uma resposta genérica.

02:21

Isso é o que a gente chama de incontext learning. De longe,

02:24

a técnica mais simples e eficaz para blindar seus agentes contra alucinações.

02:30

E aqui está o Knowledge.

02:32

Agora, vamos para o nosso agente de estoque, tá? Bem,

02:40

aqui está a estrela da nossa aula, né, pessoal? Que é o agente de estoque, tá?

02:46

Ele é o nosso orquestrador, beleza? Que é o Stock Agent. Ele é o nosso orquestrador.

02:51

No Lab, esse arquivo tinha alguns chudos, né? Mas aqui, obviamente, aqui a ideia,

02:58

eu já trouxe os gabaritos. Vamos ver exatamente o que vocês deveriam ter feito.

03:04

o destaque vamos vamos primeiro aqui no importe vamos lá ó

03:09

é que que que a gente fez cara a gente a

03:12

gente fez o importe do

03:15

equipe cliente tá bom é chamar

03:21

a gente vamos ver aqui ó vamos colocar aqui vou pegar pera aí tinha

03:44

esquecido pessoal de fazer eu falei isso aqui agora tá aqui

03:52

então primeira coisa que a gente deveria ter feito cadê aqui

03:59

Aqui, ó. É o A2A client chamar a gente, tá?

04:03

Copiei o gabarito e colei aqui, tá? Então,

04:06

o grande segredo da orquestração direta é esse import,

04:08

que é o nosso helper A2A, tá bom? Esse cara aqui, ó.

04:12

Toda a burocracia do protocolo, né? Vamos dar uma olhada nele?

04:15

Toda a burocracia do protocolo, discovery, tá?

04:20

Message, pull, extração, tudo,

04:23

ela está escondida dentro dessa única função aqui, tá, pessoal? E...

04:29

Depois, olha só, vamos dar uma olhada aqui na parte dos fatos,

04:34

tá? Que é o chamar agente. Vamos colocar aqui, ó. Ó,

04:41

chamar o agente de logística passando o fornecedor. Então,

04:45

eu quero chamar o agente de logística,

04:47

né? E eu vou passar o fornecedor, tá?

04:52

Olha, até sugeri, olha que legal.

05:01

Mas não era isso que eu queria, não.

05:02

Era só para mostrar para vocês a ideia funcionando.

05:06

Mas o ponto é o seguinte, ó.

05:08

Aqui está a linha mágica. Com ela,

05:10

o estoque que nasceu como servidor invoca um helper class, que é o chamar a gente. E

05:18

no final,

05:23

vira cliente do agente de logística.

05:26

E note que antes e depois da chamada, nós enviamos atualizações de status.

05:30

Então, olha só. Antes e depois, a gente envia atualizações de status. Beleza?

05:40

E isso garante que a tela do usuário não

05:42

fique congelada enquanto os agentes conversam nos bastidores.

05:45

Então, o que nós vamos fazer agora? Nós vamos testar.

05:49

Então, eu vou abrir um terminal aqui.

05:52

Na verdade, três terminais.

05:55

Vou abrir mais um terminal.

05:59

Deixa eu colocar todos no mesmo. Beleza.

06:13

Vou fazer a mesma coisa nos outros. Vou abrir mais um. Vou abrir mais um.

06:27

O que eu fiz, pessoal? Eu abri três terminais.

06:30

dentro da parte de Lab e ativei o Envy. Então,

06:39

no primeiro eu quero fazer isso aqui.

06:41

No primeiro eu quero inicializar o agente de logística.

06:47

No segundo eu vou inicializar o agente de estoque.

06:54

E no terceiro eu vou inicializar a nossa aplicação.

07:03

Vocês não viram, mas ela abriu aqui em uma outra tela. Vou mostrar aqui para vocês.

07:12

E ele falou que o servidor de estoque está online.

07:17

Agora... Olha só a nossa interface, pessoal.

07:19

O Steelit está rodando com o agente de GenUI. Depois eu explico melhor.

07:23

Ele tem a própria LLM para interpretar seu pedido

07:26

e decidir se aciona a ferramenta de estoque.

07:29

Então, detalhe importante. Ele só enxerga estoque na porta 9002, tá? Tá aqui, ó.

07:35

Então, para o GenUI, o agente de logística simplesmente não existe, tá?

07:39

Então, vamos digitar aqui, ó. Verifique a reposição da LG.

07:56

Deu um erro aqui, pessoal? Eu vou corrigir e eu volto, tá bom?

## Resumo IA

[RESUMO_IA]