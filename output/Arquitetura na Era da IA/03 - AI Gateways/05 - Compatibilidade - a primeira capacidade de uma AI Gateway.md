Módulo: Arquitetura na Era da IA\
Aula: [Compatibilidade - a primeira capacidade de uma AI Gateway](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18289)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem? No vídeo anterior a gente entendeu o conceito de AI Gateway,

00:06

a gente falou sobre fronteiras arquiteturais,

00:09

a gente falou inclusive também sobre como tudo isso

00:13

pode mexer no processo e na arquitetura da sua aplicação. Agora,

00:18

antes da gente entrar em uma ferramenta específica e etc,

00:22

eu queria separar uma capacidade importante dessa ideia, que é a compatibilidade.

00:30

Quando a gente fala em AI Gateway,

00:31

muita gente já pensa em um monte de coisa ao mesmo tempo.

00:35

Pensa em fallback, roteamento, controle de custo, dashboard,

00:39

um monte de providers,

00:41

chave por usuários, parte de aplicação e por aí vai. Tudo isso,

00:46

na realidade... pode fazer parte de uma gateway mais madura.

00:52

Mas nem sempre a evolução começa com todos esses recursos. Muitas vezes,

00:58

a primeira necessidade é muito, muito, muito mais direta, que é fazer uma aplicação,

01:05

conversar com diferentes modelos e providers sem ficar

01:09

presa ao formato específico de cada um.

01:11

Esse aí, então, é o papel da compatibilidade. Então,

01:15

a compatibilidade é a capacidade de a gente oferecer

01:18

uma interface mais uniforme para acessar providers diferentes.

01:21

A aplicação faz uma chamada em um formato mais padronizado,

01:26

uma camada intermediária entende o provider,

01:29

traduz a request, adapta os parâmetros,

01:32

envia a chamada para o destino correto e tenta

01:35

devolver uma resposta num formato mais consistente.

01:38

Então, nesse momento,

01:40

a gente não está falando ainda de política completa da arquitetura.

01:44

Nós não estamos aí decidindo se a resposta deve ser ali degradada.

01:48

A gente não está definindo...

01:50

Quando mandar para uma, sei lá, uma revisão humana,

01:53

a gente não está falando de um processo assíncrono e também a

01:57

gente não está discutindo toda a estratégia

01:59

de observabilidade e segurança da aplicação.

02:02

O que a gente está falando de um primeiro momento

02:04

é um passo que é padronizar o acesso.

02:07

E esse passo já muda bastante a arquitetura,

02:09

porque se a aplicação consegue acessar providers

02:12

diferentes para uma interface mais comum,

02:14

você ganha mais liberdade para testar modelos,

02:17

comparar custos, medir qualidade, trocar uma opção por outra e tudo mais.

02:21

Mas a gente tem que ter um cuidado importante com isso.

02:25

Compatibilidade não significa que todos os modelos são iguais.

02:29

Um modelo pode ter um suporte melhor a tool calling,

02:32

outro pode lidar melhor com JSON, outro pode ter uma janela de contexto maior,

02:37

outro pode ter um comportamento com streaming,

02:40

imagem, arquivos, embeddings ou reasoning. Então,

02:43

uma camada de compatibilidade não apaga essas diferenças,

02:48

ela só cria um ponto mais organizado para lidar com elas.

02:52

Então, essa distinção é realmente importante e é importante a gente destacar isso.

02:57

Porque antes de falar em um gateway, mesmo que manual,

03:00

com políticas específicas, ou de um gateway totalmente de mercado,

03:04

A gente precisa entender esse primeiro nível.

03:07

Como que eu reduzo a fricção de conversar com múltiplos providers?

03:12

E é exatamente aqui que ferramentas como o Lite LLM começam a aparecer. No próximo vídeo,

03:18

A gente vai posicionar o Lite LLM dentro dessa

03:22

evolução e entender por que ele é uma peça importante.

03:27

Para a compatibilidade,

03:28

Mas não representa também sozinho aqui toda aquela

03:31

maturidade arquitetural de um AI Gateway.

03:35

Então, vamos nessa.

## Resumo IA

[RESUMO_IA]