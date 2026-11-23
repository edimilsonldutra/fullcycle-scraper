Módulo: DevOps e SRE com IA\
Aula: [CleanUp (Removendo as faults)](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18547)

## Resumo da aula



## Transcrição

00:00

Passando aqui para a nossa última demo, eu não vou cortar entre essas duas,

00:03

porque essa aqui é bem rápida,

00:05

então a gente vai fazer um clean up aqui,

00:07

fazer remover todos os problemas que estão no nosso ambiente,

00:10

restaurar todos os faltos injetados, tudo que a gente injetou,

00:14

a gente vai remover, apesar que já está tudo funcionando normalmente lá,

00:20

mas vamos ver o que ele vai fazer aqui quando a gente pedir para ele remover.

00:24

Falta injector, restaura o deploy original.

00:29

K8S verifica o suporte saudável e o prompt confere o SLO normal.

00:33

O audit completo, todo o ciclo registrado no LingFuse,

00:37

timestamp de cada ação e decisão, quem aprovou, quem rejeitou,

00:40

quem ativou e assim por diante, ações executadas e resultados,

00:44

pós -mortem gerado dentro do Trace.

00:46

Então a gente consegue ter toda essa auditoria completa do que aconteceu.

00:52

Então a primeira coisa que a gente vai fazer...

00:54

Vamos voltar aqui no nosso chat,

00:56

vamos manter nesse chat aqui e voltar ele para o SRE troubleshoot aqui.

01:06

Primeira coisa, vamos pedir para ele remover. Então,

01:09

remova todas as

01:12

faults injetadas no

01:18

app API e verifique que

01:24

o deploy...

01:29

Deployment está em estado normal.

01:35

Vamos esperar aqui para ele fazer a resposta para a gente.

01:42

Vou remover todas as falhas injetadas.

01:44

Ele está olhando aqui. Ele pediu para remover todas.

01:52

Status Restored. Ele voltou para todas as falhas removidas.

01:56

Deployment restaurado em estado normal.

01:58

Um patch aplicado.

02:01

Então aqui ele fez uma tool call para verificar

02:03

como está o estado do nosso ambiente. Ver se está ok.

02:10

Agora ele vai verificar o estado, a saúde dos pods e assim por diante.

02:16

E vai mostrar o audit log completo que a

02:18

gente já conseguiu ver lá na parte anterior.

02:20

Então aqui estão as réplicas, tudo que está rodando,

02:23

tudo bonitinho, pode a conclusão.

02:25

Então agora a gente está tudo no estado normal e operacional.

02:29

Essa última demo aqui é bem simples,

02:30

só pedir para ele remover tudo que a gente consegue pedir também,

02:33

a gente tem essa possibilidade e a gente consegue fazer N outras coisas aqui.

02:37

Basta usar a criatividade e usar a necessidade,

02:43

fazer a necessidade que você tem,

02:45

que você consegue criar diversas MCPs que vão te

02:49

ajudar na operação do seu ambiente no dia a dia.

02:53

Inclusive MCPs que você pode usar para...

02:56

Fazer aquele deploy automático que a gente fez lá,

02:58

eu precisava fazer um git add, precisava fazer um git checkout, etc.

03:02

A gente tem a possibilidade de criar MCPs que fazem isso automaticamente,

03:06

né? Em conjunto com um LLMI,

03:10

ok? Então aqui, no final, a gente tem a entrega do nosso projeto.

03:14

Um repositório, um GitHub progressivo, do módulo 1 até o 5,

03:18

com vários regions aqui executáveis.

03:22

Quatro MCPs configurados, o OpenMBA funcional com modelo e Keynote Base, o LangFuse,

03:28

AuditLog, Key, OnChase, na execução real, o Rascunho de pós-morte gerado,

03:34

o pós-morte generator, demo gravada, a gente criou a demo aqui,

03:38

mostrando o ciclo completo do OpenMBA. Legal?

03:43

Alguns critérios aqui de avaliação, funcionalidade end-to-end,

03:48

governança, clareza do README e reprodutibilidade.

03:53

Acredito que vocês vão conseguir

03:55

fazer o README bem construído aí,

04:01

para o pessoal conseguir reproduzir isso. E a qualidade do pós-morte ali.

04:07

A gente consegue atingir isso aí também.

04:09

O que demonstramos aqui, né? Da nossa arquitetura, fizemos as quatro demos aqui,

04:16

criamos governança para administrar os nossos

04:21

sistemas e tivemos a oportunidade de

04:25

conseguir fazer ações dentro de um cluster

04:28

Kubernetes simplesmente com linguagem natural,

04:31

mandando mensagens para um chat e esse chat fazendo a

04:34

operação para você e te dando o retorno.

04:37

Isso é bem interessante para ajudar o dia a dia de trabalho nosso

04:40

para diminuir a nossa carga de trabalho

04:44

de SRE e de outras atividades também,

04:48

se for necessário, a gente consegue diminuir também. Beleza,

04:51

pessoal? Então vou encerrar essa parte por aqui.

04:55

Volto no próximo vídeo para a gente fazer o encerramento, para ter um papo,

05:00

falar um pouco sobre o que foi o curso, o que a gente fez até aqui.

05:04

Propor esse desafio para vocês aí de fazer

05:07

toda essa arquitetura internamente aí no computador de vocês, tá?

05:14

Então, é isso aí. Um abraço. Até a próxima.

## Resumo IA

[RESUMO_IA]