Módulo: Arquitetura na Era da IA\
Aula: [Quando uma chamada síncrona ainda faz sentido](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18312)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? No vídeo anterior,

00:03

a gente começou a falar sobre o problema de execução em aplicações com IA.

00:08

A ideia principal era entender que uma chamada para IA,

00:11

ela não entra sempre no software do mesmo jeito.

00:14

Às vezes o usuário pode esperar a resposta na hora,

00:17

às vezes faz sentido ele acompanhar a resposta,

00:19

às vezes isso aí também faz sentido virar um job em background.

00:24

Agora, a gente vai pelo caso mais simples, que é a chamada síncrona.

00:29

E a chamada síncrona é basicamente o fluxo que a

00:32

gente já está acostumada a fazer em aplicações web.

00:36

O usuário faz uma ação, a aplicação recebe a requisição, o back-end chama a IA,

00:41

espera a resposta completa e depois devolve alguma coisa para o usuário.

00:46

Então imagina um endpoint bem simples, por exemplo,

00:49

um POST para analisar um ticket de suporte.

00:52

O usuário manda uma mensagem dizendo,

00:54

fui cobrado duas vezes e preciso de ajuda com meu pagamento.

00:58

A aplicação recebe essa mensagem, chama a IA e pede para ela devolver uma categoria,

01:04

uma prioridade e um pequeno resumo daquele ticket.

01:07

A resposta poderia ser alguma coisa como categoria billing,

01:11

prioridade alta e um resumo dizendo que o cliente relata uma cobrança duplicada.

01:17

Nesse caso,

01:18

talvez faça sentido usar uma chamada assíncrona. Por quê?

01:21

Porque a entrada é pequena, a saída também é pequena,

01:25

a tarefa é bem objetiva e o usuário provavelmente

01:28

espera uma resposta ali quase que imediata.

01:31

Então, não tem muita coisa acontecendo aí.

01:34

A IA não precisa analisar um documento gigante,

01:37

não precisa gerar um relatório, ela não precisa processar centenas de registros.

01:41

Ela só precisa olhar para um texto curto e devolver uma estrutura simples.

01:46

Então, a chamada síncrona não é errada.

01:49

O problema é quando a gente começa a usar a chamada síncrona para tudo.

01:56

E isso é muito comum. Como que é o caminho,

02:01

vamos dizer assim, mais simples de implementar?

02:04

A gente tende a ter essa tendência de fazer toda a

02:07

feature cunhar da forma como a gente sempre desenvolveu.

02:10

Então esse é o grande ponto e a gente tem esse problema.

02:14

Agora, uma coisa é esperar dois segundos para uma classificação curta.

02:19

Outra coisa é esperar 20,

02:21

30, 40 segundos para gerar uma análise maior. A aplicação fica segurando a conexão,

02:27

o usuário fica olhando para a tela sem saber

02:29

o que está acontecendo e qualquer instabilidade...

02:32

pode virar ali uma experiência mega ruim.

02:35

E tem um outro ponto importante também. Quando a chamada é síncrona,

02:39

normalmente a requisição inteira depende da resposta da IA. Então, se a IA demora,

02:46

tudo vai demorar. Se a IA falha, a requisição vai falhar. Se estoura um timeout,

02:52

o usuário pode achar que nada aconteceu e vai ter que clicar ali de novo.

02:56

E a aplicação pode disparar a mesma tarefa mais de uma vez.

03:00

Então, quando a gente fala de arquitetura com IA,

03:02

a pergunta não é se a chamada síncrona é boa ou ruim. A pergunta é,

03:07

essa tarefa é pequena o suficiente para justificar esse fluxo?

03:11

Se for uma classificação curta,

03:13

uma extração simples, uma validação rápida, talvez ali,

03:16

beleza, faz sentido. Você chamar IA,

03:18

vai esperar uma resposta e vai devolver um JSON.

03:21

Agora, se a tarefa começar a ficar longa,

03:23

se a resposta é muito grande, no final das contas,

03:26

aí a gente já tem que utilizar outras estratégias.

03:29

ou outras estratégias. Então, uma regra prática para você em relação a tudo isso. Pensar assim,

03:37

se o usuário precisa da resposta agora para continuar usando aquela tela,

03:42

e se essa resposta tende a voltar rápido,

03:46

o síncrono vai funcionar muito bem.

03:50

Mas se a resposta demora o suficiente para deixar o usuário inseguro,

03:54

ou se existe um risco de timeout,

03:56

ou se a tarefa envolve várias etapas,

03:59

a gente tem que parar e pensar provavelmente em outro fluxo. E no próximo vídeo,

04:04

a gente vai olhar para o streaming. Ele não elimina o tempo total da chamada,

04:10

mas ele muda bastante a percepção do usuário. Beleza? Então, vamos nessa.

## Resumo IA

[RESUMO_IA]