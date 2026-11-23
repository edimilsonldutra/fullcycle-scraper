Módulo: Arquitetura na Era da IA\
Aula: [Quando transformar IA em processamento assíncrono](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18314)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente falou sobre streaming e sobre como ele

00:06

ajuda bastante quando a resposta pode aparecer em partes para o usuário.

00:11

Só que tem uma situação onde mesmo o streaming não resolve tão bem,

00:14

que é quando a tarefa é mais pesada,

00:17

é mais longa ou quando simplesmente não deveria ficar presa em uma requisição HTTP.

00:22

E é aqui que entra o processamento assíncrono. A ideia é simples.

00:25

Ao invés do usuário disparar uma ação e a aplicação ficar

00:28

esperando a IA terminar tudo para devolver uma resposta,

00:31

a aplicação cria uma tarefa,

00:34

devolve um identificador e continua ali processando em background.

00:38

Então, imagina o seguinte cenário.

00:40

O usuário quer gerar uma análise completa de vários tics de suporte.

00:44

a IA precisa ler cada ticket,

00:46

classificar, resumir, identificar a prioridade,

00:49

talvez sugerir uma ação para cada caso e,

00:51

no final, montar um resultado consolidado. Então, isso pode levar um tempo.

00:55

Se a gente tentar fazer tudo isso dentro da mesma requisição,

00:59

a chance de dar ruim é grande. Pode estourar timeout, pode falhar no meio,

01:04

o usuário pode fechar a tela, pode clicar mais de uma vez. Então,

01:07

a aplicação fica amarrada num fluxo que não

01:10

foi feito para esse tipo de processamento.

01:12

Então, nesse caso, faz muito mais sentido pensar num job.

01:16

O fluxo fica mais ou menos assim. O usuário faz um post para pedir análise.

01:21

A aplicação cria um job com status pendente,

01:24

salva essa informação em algum lugar e devolve um job ID. A partir daí,

01:29

um worker pega esse job, executa a chamada para IA,

01:33

processa o resultado e atualiza o status.

01:37

Depois, o usuário pode consultar esse job ID para saber se ele ainda...

01:43

Está processando se ele terminou ou se ele deu erro.

01:46

Quando terminar, a aplicação retorna o resultado final.

01:50

Percebe que a chamada da IA saiu do caminho principal da requisição?

01:55

O usuário não ficou preso esperando tudo terminar.

01:58

A aplicação também não precisou manter a conexão aberta até o fim do processamento.

02:03

Então isso é muito comum quando a gente fala de geração de relatório,

02:06

análise de documentos,

02:07

extração de PDF, enriquecimento de muitos registros e etc.

02:11

E um ponto importante aqui é que isso não é uma invenção por conta da IA.

02:16

A gente já usa processamento assíncrono há muito tempo no software.

02:19

O que muda é que a IA aumenta bastante a frequência desses casos,

02:24

porque muitas features deixam de ser operações rápidas e

02:27

elas passam a ser processos que demoram,

02:30

custam dinheiro e podem falhar de diferentes formas.

02:33

Por isso, a arquitetura precisa tratar...

02:36

essas tarefas aí com mais cuidado. Um job normalmente precisa ter estado,

02:41

ele pode começar como um pending, depois ir para processing,

02:45

depois ir para completed ou failed. Dependendo do caso, também pode salvar logs,

02:50

mensagens intermediárias ou algum resultado parcial.

02:54

E isso ajuda tanto na experiência do usuário...

02:57

quanto na operação do sistema. Se alguma coisa falha,

03:00

Se a aplicação sabe qual job falhou,

03:03

Se esse usuário volta depois e o resultado ainda está lá,

03:07

Se ele precisar tentar de novo,

03:08

Dá para ele clicar em retry ou a gente fazer qualquer tipo desse tipo de coisa.

03:14

Então, o assíncrono não é uma forma de rodar depois.

03:18

Na realidade, ele muda o desenho da feature. A IA,

03:21

ela deixa de ser uma resposta imediata e passa

03:24

a fazer parte de um fluxo de processamento.

03:26

Na prática agora, a pergunta que a gente precisa fazer é,

03:30

Essa tarefa precisa terminar dentro da requisição original? Se não precisa,

03:36

Talvez ela seja uma boa camada, uma boa candidata a virar um job.

03:42

E aí, no próximo vídeo, a gente vai continuar em cima disso,

03:45

Pensando nesses aspectos. Beleza? Um grande abraço e vamos nessa!

## Resumo IA

[RESUMO_IA]