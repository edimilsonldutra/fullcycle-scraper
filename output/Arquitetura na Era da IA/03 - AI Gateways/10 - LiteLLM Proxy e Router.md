Módulo: Arquitetura na Era da IA\
Aula: [LiteLLM Proxy e Router](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18294)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, no vídeo anterior a gente falou mais sobre o proxy do LiteLLM,

00:07

a gente trouxe algumas características interessantes em relação às keys,

00:12

a budgets, limites e etc.

00:14

Mas também existe aí uma peça central no meio de tudo isso que é chamado do router.

00:20

O router ele...

00:22

ele é quem decide como aquela chamada vai ser executada.

00:25

Mas antes de a gente falar dele em detalhe,

00:27

a gente precisa entender que o LiteLLM separa o que

00:31

a aplicação pede do que será chamado de verdade.

00:34

A aplicação pode pedir, sei lá, um nome lógico como,

00:38

sei lá, chat rápido ou strong chat, o classificador barato,

00:43

sei lá, classificação, extrator de documento.

00:47

Então, esses nomes não precisam ser o nome real do modelo no provider.

00:51

Por trás, no arquivo de configuração do proxy,

00:54

você define quais modelos reais atendem àqueles nomes.

00:58

Então aqui que entram dois conceitos, model group e deployment.

01:03

O model group é o nome lógico que a aplicação enxerga.

01:06

O deployment é a configuração concreta que o LLM,

01:11

que o LiteLLM usa para chamar um provider real.

01:15

Por exemplo... Um grupo, sei lá,

01:17

chat rápido pode apontar para um deployment

01:20

utilizando o GPT 5.4 ou 5.5.

01:25

O outro ali pode estar usando o Gemini 3.5

01:29

e o outro usando algum outro modelo equivalente.

01:32

Então, já esse grupo chat forte, ele pode apontar ali para o GPT 5.5.

01:38

Então... Essa separação é mega poderosa,

01:41

porque a aplicação deixa de conhecer o provider e o modelo físico e ela,

01:46

no final das contas, ela pede uma capacidade.

01:49

E quem decide essa execução... É a chamada do gateway.

01:53

Então, depois que o router, no final das contas, escolhe o deployment,

01:57

ele chama internamente cada camada de tradução do LiteLLM,

02:02

envia a requisição para o provider real, recebe a resposta,

02:05

normaliza o retorno e devolve ali à aplicação.

02:10

E depois que a resposta volta, ainda tem um pós-processamento.

02:14

O LiteLLM pode atualizar o uso de tokens,

02:18

ele pode mudar os custos, as métricas, os logs,

02:22

o consumo por chave do usuário, tempo e modelo. Então,

02:25

parte desse processamento pode acontecer de forma assíncrona, inclusive,

02:30

para não prender toda a requisição ali no banco de dados.

02:34

Então, o fluxo completo fica assim.

02:36

A aplicação chama o proxy, o proxy valida a chave virtual.

02:40

aplica o budget e o rate limit,

02:43

encaminha para o router,

02:44

esse router escolhe o deployment e o LiteLLM traduz a chamada para o provider,

02:50

recebe a resposta, normaliza o retorno e registra ali o uso. Então,

02:56

no próximo vídeo a gente vai entender um pouco

02:58

mais sobre esses aspectos aí de forma geral.

03:02

Mas o interessante é você entender que quando você está usando um proxy,

03:06

eu não preciso saber qual modelo eu vou precisar.

03:10

Eu preciso saber qual é o tipo de capacidade que eu preciso.

03:14

Eu preciso de algo que me torne rápido com esforço mediano?

03:19

Então eu posso dar um apelido para aquilo.

03:21

E quando eu faço a chamada para aquele apelido,

03:24

vamos dizer, no final das contas ele está me...

03:28

fazendo um apontamento para um deployment que tem

03:31

realmente ali as configurações de qual modelo,

03:34

qual provedor que eu vou utilizar.

03:36

Isso aí funciona muito bem mesmo na hora que a gente está trabalhando com isso. Beleza?

## Resumo IA

[RESUMO_IA]