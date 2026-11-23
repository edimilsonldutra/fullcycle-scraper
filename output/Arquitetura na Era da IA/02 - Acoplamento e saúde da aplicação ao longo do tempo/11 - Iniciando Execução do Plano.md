Módulo: Arquitetura na Era da IA\
Aula: [Iniciando Execução do Plano](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18121)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, voltando aqui,

00:03

ele terminou o processo e eu vi uma coisa bem interessante.

00:07

Primeira coisa, ele soltou três agentes, um para ver edge case de fluxo de pedido,

00:12

outro edge case na parte do preço, promoção,

00:14

frete e imposto e outros pontos cegos de infraestrutura de teste. Agora,

00:18

olha só que interessante, por isso que eu falei para vocês.

00:21

Os três agentes encontraram um conjunto enorme de

00:25

pontos cegos e muitos são exatamente os defeitos plantados. Por quê?

00:29

Porque eu falei aqui que a gente tem um curso

00:31

e tem erro ali dentro do nosso sistema.

00:35

Oversell com linha duplicada, três totais divergentes,

00:38

frete de e-mail diferente do frete cobrado, imposto fora do total,

00:43

round two aqui errando meio centavo. Então,

00:46

isso muda a natureza da rede de segurança. Ela precisa travar o comportamento atual.

00:52

inclusive os bugs, por caracterização,

00:55

para que qualquer refatoração que os altere seja sinalizada. Galera,

01:00

isso é uma coisa importante que eu quero que você tenha em mente, que é o seguinte,

01:04

mesmo que um teste, e você vai pedir para IA fazer os testes, etc.,

01:09

mesmo que você saiba que o software tem um bug,

01:12

pede para ele fazer o teste que não corrija esse bug.

01:18

mas que o teste mantenha esse bug do jeito que está. Por que eu estou dizendo isso?

01:23

Porque você quer manter o comportamento do software inalterado

01:27

enquanto você tem essa linha de teste.

01:29

Porque se a gente sair corrigindo o bug agora,

01:31

a gente desvia do nosso ponto principal.

01:34

E aqui ele reanalisou, aqui para a gente,

01:37

e ele falou que encontrou um conjunto enorme de pontos cegos. Então...

01:42

Olha como faz diferença você buscar por edge cases. Então,

01:46

fica aí a dúvida. Olha o que estava fora do plano.

01:49

Infraestrutura, e-mail, cobertura órfã, edge cases de negócio,

01:53

muitos são defeitos plantados. Aqui, o que o plano mudou?

01:57

A rede de segurança agora explicitamente caracterização.

02:00

Trava o comportamento atual, incluindo os bugs, etc.

02:03

Então, está aqui, né? Plano, cobertura determinística, rede de segurança de teste,

02:07

refatoração piloto. Esse aqui é o nosso plano aqui,

02:11

que ele separa por parte A, parte B,

02:13

parte C, e aqui ele bota limpeza, ou seja,

02:18

ele está trazendo de forma geral o plano,

02:20

ele está verificando os testes de comportamento baseado nos valores do SIDS.

02:25

Então ele está fazendo toda a coisa,

02:27

eu não vou olhar aqui com todos os detalhes do mundo, tá?

02:30

E aqui é uma das partes importantes, que é a refatoração piloto via TDD,

02:34

usando Dependency Inversion Principle,

02:36

utilizando o Payment Gateway no Order Service,

02:41

etc. A verificação aqui, a gente tem uma verificação End-to-End,

02:45

que ele pede para testar, e ele trouxe riscos, etc.

02:49

Agora, o que eu posso fazer aqui nesse momento?

02:53

Eu posso pedir para ele fazer a execução,

02:56

e ele vai sair executando isso.

02:58

Eu estou usando o Cloud Code e tem um milhão de janelas de contexto,

03:01

se eu quisesse eu desse um Enter,

03:02

provavelmente nessa janela ainda eu conseguiria resolver esse problema, tá?

03:08

Mas na realidade eu vou pedir para ele fazer algo diferente,

03:12

tá? Eu vou escrever aqui para ele, aqui ó,

03:16

faça com que esse

03:20

plano gere um documento

03:25

extremamente explicativo na pasta

03:36

docs barra plan

03:41

.md. Vou colocar uma coisa assim.

03:43

Faça com que esse plano gere um documento, etc.

03:48

A implementação não

03:53

deverá ser executada.

03:59

Basicamente o que eu fiz é, ao invés de pedir para ele fazer a implementação,

04:03

eu mudei a ideia falando que não, eu não quero que você implemente,

04:08

eu quero que você crie um documento e tenha os detalhes da implementação.

04:12

Por quê? Com esse documento eu consigo quebrar isso em fases,

04:16

eu consigo dar um clear na minha janela de contexto e fazendo isso por pedaços,

04:22

tá? Então somente para a gente trabalhar com clear,

04:26

com a janela de contexto mais tranquila.

04:28

Mas provavelmente do jeito que eu estava, se eu mandasse ele implementar,

04:31

ele iria implementar, mas eu quero ir devagar aqui para a gente.

04:35

Então ele trouxe aqui o plano aqui para a gente, fazendo

04:39

essa alteração, vamos só garantir que está tudo certo.

04:44

Plano, código didático, e -commerce e problemas,

04:46

switch passa, objetivo antes refatorar,

04:49

montar uma rede de segurança, parte 2, documentação expletiva,

04:52

primeira entrega aqui para a gente. Aí tem parte A, determinística e tal.

04:57

Então, primeiramente, eu vou colocar a parte yes, eu vou colocar aqui,

05:03

passa a parte inicial da documentação.

05:12

Eu vi que ele continuou com as partes do passo a passo ainda no plano.

05:17

Então, se eu der um Enter,

05:19

eu não quero que ele continue executando o plano. Então,

05:21

eu botei aqui para ele fazer somente a parte 1.

05:26

Bom, pessoal, ele falou que criou o documento.

05:29

Vou ver aqui junto com vocês o documento. E ele perguntou, inclusive,

05:32

ali se eu quero que ele inicie a implementação das outras fases, tá?

05:36

Então, eu vou botar aqui para a gente ver o documento.

05:40

Para ficar melhor, diagnóstico inicial, cobertura de testes,

05:43

uma rede de segurança ilusória,

05:45

os três comportamentos, os componentes mais críticos do acoplamento,

05:51

porque cada existe, é uma lógica pedagógica,

05:54

obviamente por conta que a gente estava trabalhando,

05:56

catálogo de edge case e pontos cegos,

06:00

caracterização de efeitos, dados sujos, rede de segurança de testes,

06:05

aqui para a gente.

06:08

A limpeza dos testes rasos.

06:11

Cinco, refatoração.

06:13

E verificação de como saber se deu certo aqui. Então,

06:16

a etapa zero ele já fez. Aqui a cobertura determinística. Baseline, tabela antes.

06:22

E a cobertura, como é que estava antes de métricas.

06:25

Para depois a gente provavelmente verificar e ver isso aí depois e tudo mais.

06:30

Então, ele fez isso. O que eu vou fazer agora aqui,

06:32

No final das contas, vai ser... Eu vou dar um...

06:37

Um clear pra gente iniciar, tá?

06:40

Essas tarefas aqui.

06:42

Então, o que que eu vou fazer aqui pra gente, tá?

06:48

Eu vou colocar, né?

06:51

Eu tenho uma parte que eu posso fazer execução

06:53

de planos independentes ou qualquer coisa desse tipo,

06:56

mas no final das contas, eu quero... Como que eu posso dizer?

07:03

Eu posso colocar aqui, ó. Baseado no...

07:07

arroba plan.md

07:11

crie,

07:15

implemente as

07:19

etapas A, B,

07:23

aqui

07:25

para mim, e depois C. Eu não quero fazer refatoração por enquanto. Utilize

07:33

subagentes.

07:38

Existem comandos para isso, tá, galera? Estou escrevendo...

07:42

manualmente aqui pra vocês, tá? Tem diversos skills,

07:45

tem o Superpowers que eu posso usar pra ele fazer desenvolvimento baseado em subagentes,

07:49

tudo mais. Utilize subagentes de forma paralela

07:54

paralela à medida do possível

07:59

para adiantar todo o processo.

08:05

Basicamente é isso que a gente tá colocando aqui.

08:11

E... Vou tirar aqui do modo plan. Vou botar direto aqui.

08:17

Vamos ver como é que ele vai rolar. Vou dar um enter.

08:21

E vamos nessa, galera. Vou deixar esse cara rodando.

08:26

E vou parar esse vídeo por aqui. Talvez para ele não ficar muito grande.

08:29

A gente volta depois da implementação.

## Resumo IA

[RESUMO_IA]