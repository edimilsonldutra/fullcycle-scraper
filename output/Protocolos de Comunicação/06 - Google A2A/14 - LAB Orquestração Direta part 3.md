Módulo: Protocolos de Comunicação\
Aula: [LAB Orquestração Direta part 3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18928)

## Resumo da aula

Retomando a topologia GenUI → estoque → logística, o ponto decisivo aqui é que o usuário conversa com uma única interface e não precisa conhecer a malha interna de agentes. O GenUI chama apenas o agente de estoque, e a dependência com logística permanece encapsulada dentro do domínio de estoque. Isso reduz acoplamento na experiência de uso e preserva uma fronteira clara: o cliente consome uma capacidade de negócio, não a estrutura interna que a implementa.

O fechamento do fluxo valida a aplicação concreta da orquestração direta já estabelecida: o estoque recebe a requisição como servidor A2A e, durante a mesma execução, assume o papel de cliente ao consultar logística. O valor arquitetural está em manter a decisão de delegação no agente que entende o domínio, em vez de empurrá-la para a interface. Quando o estoque consolida a resposta final, ele transforma colaboração lateral entre especialistas em uma resposta única e coerente para quem iniciou a solicitação.

GenUI, ou Generative User Interface, é uma camada de interface que não apenas coleta texto do usuário, mas interpreta intenção com uma LLM própria e decide qual capacidade do sistema deve ser acionada. Isso desloca parte da inteligência para o front-end, permitindo que a interface atue como ponto de entrada semântico em vez de mero formulário ou chat passivo. Nesse arranjo, a interface não executa a lógica de estoque nem de logística; ela decide para onde enviar a solicitação com base na intenção detectada.

Quando a interface interpreta o pedido e conclui que a intenção é consultar reposição, ela aciona o estoque diretamente. Essa escolha é importante porque evita expor logística como opção de uso geral para o cliente final, mesmo quando a resposta depende dela internamente. O resultado é um fluxo mais robusto: a interface conhece menos detalhes operacionais, e o domínio de estoque controla quando a colaboração com logística é necessária.

A próxima camada natural dessa arquitetura é fazer o GenUI consumir Agent Cards e lidar com múltiplos agentes e ferramentas como MCP. Isso amplia a capacidade de descoberta e seleção dinâmica sem alterar a base já construída, porque a fundação continua sendo a interoperabilidade A2A entre especialistas. A diferença é que a interface deixa de depender de integrações fixas e passa a operar como uma camada inteligente capaz de escolher capacidades disponíveis no ecossistema.

Um sistema simples já pode sinalizar prontidão arquitetural quando a colaboração entre agentes acontece de forma invisível, rastreável e consistente para o usuário. Aqui, a robustez não vem de uma interface sofisticada isoladamente, mas da combinação entre entrada inteligente no GenUI e delegação interna controlada no estoque. Esse fechamento confirma que o padrão não serve apenas para demonstração local: ele já se comporta como uma solução plausível para cenários reais.

## Transcrição

00:01

Pessoal, erro corrigido. Vamos voltar aqui. Verifique a reposição da LG. A

00:15

posição dos produtos LG está refeita na alfândega.

00:18

Olha que interessante, pessoal.

00:21

Eu quero mostrar para vocês uma coisa que é muito interessante.

00:23

Aqui, se vocês forem ver,

00:25

tanto o... Olha, esse aqui é o agente de logística.

00:30

O agente de logística foi

00:32

acionado pelo agente de estoque. Então,

00:40

nós fizemos aqui um workflow semelhante.

00:43

Então, pessoal, para a gente fechar,

00:45

hoje nós construímos o padrão básico de orquestração direta, que é um workflow semelhante.

00:51

Um agente operando como servidor e cliente ao mesmo tempo.

00:53

Ou seja, o estoque recebe a requisição,

00:55

ele aciona o agente de logística via E2A e consolida o resultado.

01:00

Na verdade, o agente cliente, que é o GenUI,

01:03

ele aciona o agente de estoque, que não sabe da existência,

01:07

o agente de cliente não sabe da existência do agente de logística,

01:10

e o agente de estoque é que interage com a logística, tá?

01:14

Ou seja, a frase que vocês devem levar para o time é o seguinte,

01:19

orquestração direta é quando o agente vira cliente do outro,

01:22

e fim de papo, sem intermediários.

01:24

E vocês repararam um salto tecnológico, né?

01:27

Nossa interface já nasceu semelhante. Então, como eu disse,

01:30

eu até chamei de GenUI, mas eu não expliquei,

01:32

que é o Generative User Interface, tá?

01:34

É um conceito interessante, ó. Ele tem seu LLM próprio,

01:38

ele interpreta a intenção do usuário e decide chamar o estoque. Nos próximos lives,

01:42

vamos colocar cereja no bolo fazendo essa interface assumir agent cards,

01:46

consumir agent cards múltiplos e até mesmo ferramentas MCP,

01:49

tá? A inteligência finalmente subiu para o front-end, tá? Mas lembre-se,

01:53

a fundação de tudo é que essa é a orquestração 8-way robusta que acabamos de fazer.

01:57

Ou seja, é... Pessoal,

02:00

um grande avanço significativo aqui nos nossos labs e vocês viram um

02:04

sistema simples que remete a uma

02:07

solução que poderia facilmente estar em produção. Obrigado.

## Resumo IA

[RESUMO_IA]