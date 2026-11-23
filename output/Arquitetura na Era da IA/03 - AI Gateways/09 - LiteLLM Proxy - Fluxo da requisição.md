Módulo: Arquitetura na Era da IA\
Aula: [LiteLLM Proxy - Fluxo da requisição](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18293)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? Aí nos vídeos anteriores,

00:03

a gente acabou vendo que o Lite LLM Proxy,

00:06

ele muda o desenho da arquitetura e ele deixa de ser apenas

00:10

uma biblioteca dentro da aplicação e passa a ser um serviço separado, né? Agora,

00:15

vamos olhar para o fluxo de uma requisição por dentro. Imagina que uma aplicação,

00:19

ele precisa chamar um modelo. Em vez de chamar diretamente o provider,

00:23

ele envia uma requisição HTTP para o Lite LLM Proxy.

00:27

Essa requisição normalmente vai como um Bearer Token,

00:32

como autorização, né? Só que esse token, ele não precisa ser a chave real da OpenAI,

00:38

da Anthropic, da Google, da AWS ou de qualquer outro provider.

00:42

Ele pode ser uma chave virtual criada pelo próprio LiteLLM.

00:47

Então, esse conceito, ele é muito importante, por quê?

00:51

A Virtual Key funciona como uma chave de acesso emitida pela Gateway.

00:56

A aplicação usa essa chave para chamar o LiteLLM

01:00

Proxy e o proxy por trás das credenciais reais usando...

01:05

usando pelos providers. Então,

01:07

a aplicação não precisa agora carregar a chave real do provider,

01:11

ela carrega uma chave controlada pelo Lite LLM. E isso já muda bastante a segurança,

01:16

a parte de governança,

01:17

porque agora você pode criar uma chave para uma aplicação específica,

01:21

outra para um outro time, outra para um outro ambiente,

01:24

outra para um outro serviço interno, outra para um agente, etc.

01:28

Então, quando a requisição chega no Lite LLM Proxy, ele valida essa Virtual Key.

01:34

Ele verifica se essa aba existe, se ela está ativa, se está dentro do budget,

01:38

ou seja, do orçamento, se pode acessar aquele modelo,

01:41

se não ultrapassou nenhum dos limites configurados e tudo mais.

01:44

Então, essa verificação,

01:46

inclusive, ela pode usar cache em memória, pode usar um Redis,

01:49

um banco de dados, depende da configuração.

01:52

Em produção isso importa porque você não vai querer transformar cada requisição

01:56

em uma sequência pesada de leitura no banco de dados.

01:59

E depois da chave entram os rate limits.

02:03

Aqui... a gente já está falando de limites como

02:06

requests por minuto e tokens por minuto. Então,

02:09

esses limites podem existir em níveis diferentes.

02:13

Pode existir limite global do servidor, um limite por Virtual Key,

02:17

um limite por usuário ou um limite por time, por exemplo.

02:21

Isso é importante porque a IA tem uma

02:23

característica diferente de muitas chamadas tradicionais.

02:26

Quando você chama uma API comum,

02:28

normalmente você se preocupa com latência, throughput e disponibilidade.

02:32

Com IA, além disso, você passa a se preocupar com custo,

02:35

com token, com cota de providers,

02:37

com risco que uma feature tem de consumir muito mais do que ela deveria. Então,

02:42

o rate limit e o budget, eles não são detalhes operacionais soltos.

02:45

Eles viram parte da arquitetura e de controle.

02:48

Depois que o proxy valida essa chave, o budget, os limites e as requisições,

02:54

elas acabam chegando ali nos endpoints internos do Lite LLM Proxy,

03:00

e esses endpoints podem ser compatíveis com as chamadas como chat completions,

03:05

embeddings, responses e outros recursos aí suportados. Então, a partir daí,

03:12

A requisição é encaminhada para uma peça central,

03:15

que é o famoso router, ok? E no final das contas,

03:19

No próximo vídeo a gente continua para você entender

03:22

como é que esse esquema de roteamento funciona.

## Resumo IA

[RESUMO_IA]