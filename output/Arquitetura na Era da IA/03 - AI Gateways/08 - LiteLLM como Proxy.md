Módulo: Arquitetura na Era da IA\
Aula: [LiteLLM como Proxy](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18292)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

Até aqui a gente viu o LiteLLM com uma camada de compatibilidade.

00:07

Agora a gente vai mudar o desenho da arquitetura e entender

00:11

o que acontece quando a gente usa o LiteLLM no modo proxy.

00:15

No modo SDK, a aplicação chama o LiteLLM dentro do próprio código, ou seja,

00:21

a biblioteca está instalada na aplicação e é chamada a partir dali.

00:25

No modo proxy, isso muda.

00:27

O LiteLLM passa a rodar como um serviço separado e a aplicação,

00:32

no final das contas, não chama mais uma biblioteca local.

00:35

Ela faz uma requisição HTTP para o LiteLLM proxy

00:39

e o proxy encaminha a chamada para o provider configurado.

00:43

Então, esse fluxo passa a ser... A aplicação chama o LiteLLM proxy,

00:48

o LiteLLM proxy chama o provider,

00:51

o provider responde para o proxy,

00:53

o proxy devolve a resposta para a aplicação e esse é o ponto principal. LiteLLM,

00:59

ele deixa de ser apenas uma dependência da aplicação e

01:03

passa a ser uma peça no caminho da requisição.

01:06

E quando uma peça fica no caminho da requisição,

01:09

ela pode começar a concentrar responsabilidades.

01:13

Ela pode esconder as chaves reais dos providers,

01:16

pode expor o nome dos modelos mais controlados,

01:18

pode padronizar a forma como diferentes aplicações acessam a IA,

01:23

ela pode registrar a forma de utilização, os limites, o roteamento.

01:28

Centralizar a configuração. Então, a ideia aqui, na realidade,

01:32

é nesse vídeo eu quero focar mais nessa mudança,

01:35

na realidade, de topologia. Porque esse aqui que é o nosso salto arquitetural.

01:40

Antes, cada aplicação podia carregar a sua própria lógica de

01:43

integração e agora várias aplicações podem chamar o mesmo ponto central.

01:48

Então, eu posso ter uma API na área de suporte,

01:51

uma área de pagamentos e todos esses caras,

01:54

sistemas... separados podem chamar o mesmo proxy. E na realidade,

02:00

às vezes, ele nem precisa saber qual é o provider que está por trás.

02:04

Ele chama esse proxy e o proxy toma conta de todo o resto.

02:08

Então, a grande sacada em tudo isso é

02:12

que reduz pra caramba o nosso impacto no código.

02:16

Mas o mais importante não é só reduzir código.

02:18

O mais importante é que a arquitetura possa ter

02:21

uma fronteira central para chamadas da IA.

02:25

Só que essa fronteira ainda precisa ser entendida por dentro,

02:29

tá? Quando uma requisição chega no LiteLLM Proxy, ela precisa ser autenticada.

02:34

O proxy precisa validar a chave,

02:36

entender qual modelo foi pedido, verificar permissões,

02:40

aplicar limites e depois decidir para onde vai mandar essa chamada.

02:44

A gente não vai entrar em todos esses detalhes agora,

02:47

mas o objetivo desse vídeo era apenas o quê?

02:50

Fixar esse novo desenho.

02:52

Que o LiteLLM como SDK roda dentro da aplicação e o

02:56

proxy roda fora da aplicação e passa a ser chamado como HTTP.

03:00

Então, no próximo vídeo a gente vai abrir um pouco melhor esse

03:02

fluxo para entender como é que funciona todas as requisições.

## Resumo IA

[RESUMO_IA]