Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17881)

## Resumo da aula

Harness Engineering é a disciplina de projetar e operar o ambiente em que o agente trabalha. Retomando o conceito de harness já estabelecido, o foco aqui não é definir o que ele é, mas como construí-lo de forma sistemática para reduzir erros recorrentes e sustentar execução autônoma. A lógica central é iterativa: quando o agente falha de um jeito previsível, o ambiente é ajustado para impedir que a mesma falha volte a ocorrer. Isso transforma improviso em engenharia.

Prompt Engineering trata da forma de comunicação com o agente. Ele organiza como a instrução é formulada, quais técnicas de prompting são usadas e como a pergunta influencia a qualidade da resposta. Chain-of-thought e few-shot entram nessa camada porque alteram a estrutura da interação, não o ambiente de execução. O objetivo é melhorar a troca de informação entre humano, agente e demais componentes com os quais ele interage.

Context Engineering define o que o agente pode ver para executar a tarefa. Isso inclui dados, documentos, histórico e o controle da janela de contexto: o que entra, o que sai e quanto da tarefa cabe naquele espaço. Em sessões de codificação, essa decisão afeta diretamente o tamanho adequado da tarefa e a quantidade de informação fornecida. O critério não é “dar o máximo possível”, mas fornecer o mínimo necessário para que o agente trabalhe bem.

Harness Engineering engloba o que será pedido ao agente, o contexto que será disponibilizado e o ambiente em que ele vai operar. A diferença é de escopo: prompt cuida da instrução, contexto cuida da visibilidade, e harness cuida das condições operacionais que tornam a execução confiável por longos períodos. Por isso, harness não substitui as outras camadas; ele as envolve e coordena. Essa distinção evita tratar termos diferentes como se fossem sinônimos.

Quando o agente precisa programar de forma autônoma por horas, prompt e contexto isoladamente deixam de ser suficientes. O ambiente passa a precisar de ferramentas, validações, arquitetura bem definida, restrições e guidance operacional. Retomando o harness genérico visto antes, a novidade aqui é o uso dessa estrutura como disciplina de design para sustentar autonomia contínua. O resultado esperado não é apenas uma boa resposta pontual, mas um fluxo de trabalho estável.

Projetar um harness significa decidir quais ferramentas o agente pode usar, quais validações bloqueiam saídas ruins, quais consultas contextuais são permitidas e como o agente será guiado passo a passo. Essas decisões formam um sistema de suporte ao comportamento do modelo, em vez de depender apenas da capacidade bruta dele. Quando bem desenhado, o ambiente melhora previsibilidade, reduz retrabalho e torna o agente mais útil em cenários reais de desenvolvimento. A engenharia está justamente nessa composição deliberada do ambiente.

## Transcrição

00:01

Bom, pessoal, eu sei que eu tinha dado uma base e falei um pouquinho sobre o que é Harness,

00:08

Agent Harness, Harness de propósito geral, Harness do usuário,

00:12

mas eu queria agora dar um zoom um pouco maior sobre esse

00:18

conceito para conseguir trazer um pouco mais de clareza aqui para você,

00:22

principalmente aonde... essa história da engenharia do Harness,

00:28

ele acaba funcionando.

00:30

Como que a gente começou a ouvir esse termo?

00:33

Existe o camarada que criou a HashiCorp,

00:38

que faz o Terraform. Então,

00:40

o que acontece? Ele criou um artigo que eu vou recomendar,

00:44

obviamente você lê, está aqui inclusive, e ele coloca My AI Adoption Journey.

00:49

Então, é um artigo que ele começou a colocar,

00:51

como que ele começou a programar utilizando IA, etc., um cara super genial,

00:55

e ele começou a perceber que ele começou a colocar assim,

00:59

toda vez que você encontra um agente cometendo um erro,

01:03

você dedica tempo de criar uma solução para que o agente nunca,

01:08

cometa esse erro novamente.

01:10

E daí ele colocou falando como se

01:13

você estivesse criando a engenharia do Harness,

01:18

ou seja, engenharia do Harness.

01:20

Ele até coloca no artigo que ele nem sabe se esse

01:23

termo existe ou se ele que está criando alguma coisa,

01:26

mas é como que ele acaba vendo. Então,

01:29

essas ideias podem parecer óbvias e é tudo aquilo que a gente está falando,

01:34

mas... Quando a gente entende o que é Agent Harness,

01:38

que é o que eu falei em todos esses vídeos atrás,

01:42

a gente tem que pensar agora o que é o Harness Engineering.

01:47

Como é que a gente consegue ter uma visão mais global de engenharia do Harness?

01:53

Então, quando a gente pensa em Harness Engineering,

01:56

a gente está pensando no processo de design,

02:00

de execução do ambiente em que os agentes vão... Então,

02:06

o Harness Engineering, ele é como que nós vamos construir,

02:11

como que nós vamos desenhar o ambiente.

02:14

A gente sabe o que é Harness, mas como que eu crio isso?

02:20

Qual que é o processo que eu utilizo?

02:23

Qual é a disciplina que eu utilizo para ter esse ambiente favorável?

02:28

Então, o Harness Engineering, a gente vai conseguir...

02:31

na realidade, definir quais as ferramentas,

02:33

quais são os processos de validação,

02:35

quais são as consultas de informações contextuais que o agente vai ter,

02:42

quais são as restrições, guidance, como que você vai falar pro agente,

02:46

como que você vai guiar o agente passo a passo.

02:49

E eu acho que uma forma muito bacana que eu vi no artigo,

02:52

tô deixando todas as fontes aí pra vocês, sempre, tá?

02:57

Basicamente isso aqui, deixa eu...

03:00

Deixa eu diminuir o zoom para ficar um pouco melhor aqui para você.

03:03

Cara, eu acho que essa imagem diz muita coisa sobre o que a gente está falando. O que acontece?

03:10

Eu tenho aqui uma bola chamada Prompt Engineering.

03:14

Então, toda vez que a gente fala, e a gente já falou muito sobre o Prompt Engineer,

03:19

é o que eu digo para o agente. Ou seja,

03:23

É a minha forma de comunicação. Eu estou falando em chain of thoughts,

03:26

eu estou falando em few shots,

03:28

eu estou falando em todas as formas e técnicas que eu tenho de Prompt Engineer.

03:32

Então, nesse caso, o Prompt Engineer,

03:35

ele está muito ali focado no quê? Em trocar informação.

03:39

Como que eu pergunto melhor e como que eu

03:42

posso ter uma qualidade melhor da minha resposta.

03:45

É ali que a gente acaba tendo a grande vantagem e que é o

03:50

que muda completamente uma forma de como

03:53

que um agente consegue se comunicar com outro,

03:59

ou com um humano, ou com um próprio Highness, etc. Ou seja,

04:05

quanto melhor a gente pergunta, melhor a gente tem a resposta. Basicamente é isso.

04:10

Também nós tivemos muito esse conceito de context engineer.

04:14

O que o context engineer fala,

04:16

basicamente, é o que eu posso dar de contexto para a gente, ou seja,

04:21

o que o nosso agente pode ver, o que eu falo para ele e o que ele pode ver,

04:28

ou seja, quais são os dados, quais são os documentos.

04:33

E, nesse caso, eu tenho um foco muito mais na minha janela de contexto,

04:37

no histórico, no que entra, no que sai. Então,

04:40

quando eu estou dentro de uma sessão de codificação ali do meu agente,

04:43

eu tenho que ter uma noção de qual está sendo o tamanho da minha janela de contexto.

04:48

Baseado nisso, o quanto de dado eu vou dar para o meu agente,

04:51

o quanto ele vai ler, qual o tamanho da tarefa, por exemplo,

04:55

que eu vou colocar para que ele tenha histórico suficiente para que ele consiga, na realidade,

05:01

desenvolver aquilo que eu preciso. Ou seja,

05:04

quando eu estou falando de context engineer,

05:05

é qual é o nível de contexto que eu quero dar.

05:09

Que seja o mínimo necessário para que ele consiga fazer bem a tarefa dele. Ok?

05:15

E a gente tem, então, o Harness Engineering, que engloba o que eu vou pedir,

05:22

com a informação que eu vou passar,

05:24

mas com o ambiente que ele vai operar.

05:27

Ou seja, quando eu estou falando em Harness Engineering,

05:31

eu estou falando do agente desenvolvendo de forma autônoma,

05:36

por horas, principalmente.

05:37

Então, para isso, eu tenho que ter ferramenta, eu tenho que ter validação,

05:41

eu tenho que ter uma arquitetura muito bem feita,

05:43

eu tenho que ter restrições que eu vou passar para o agente.

05:46

Então, o Harness, ele acaba estando em volta do que a gente pode,

05:52

do que a gente fala para o agente,

05:55

daquilo que o agente tem acesso, e ele foca no quê?

05:59

Como que eu faço esse cara poder sair programando, por exemplo,

06:03

de forma autônoma por muitas horas, baseado no ambiente que eu dou para ele.

06:07

Se no meu ambiente eu consigo fazer com que a gente troque informação,

06:12

que eu consiga dar a informação necessária e ainda criar ferramentas,

06:17

validações e todos esses processos, eu consigo fazer a minha construção,

06:24

o design do meu Harness Engineering.

06:26

Mas é importante aqui, nesse caso, você conseguir visualizar...

06:32

no final das contas, onde cada coisa acaba se encontrando.

06:37

Porque a gente começa a escutar cada dia mais termos e parece que esses termos

06:41

acabam não mais se encaixando e não mais funcionando.

06:45

Ou eles acabam se tornando um só. Nesse caso,

06:49

Eu acredito que não. Eu acho que tem objetivos muito claros e eu acho que,

06:54

olhando essa imagem, eu acho que fica mais fácil.

06:57

De você conseguir se entender no mundo desses montes de termos

07:02

que cada dia a gente vai tendo e vai surgindo.

## Resumo IA

**Abreviações**
*   **IA**: Inteligência Artificial
*   **AI**: Artificial Intelligence (mencionado no contexto de "My AI Adoption Journey")

**Resumo**
A aula tem como objetivo principal aprofundar o conceito de Harness Engineering, diferenciando-o de Prompt Engineering e Context Engineering, e apresentando-o como uma disciplina essencial para o design e operação de ambientes onde agentes de software podem trabalhar de forma autônoma e sustentável.

**Harness Engineering** é definido como a disciplina de projetar e operar o ambiente no qual o agente atua. Sua lógica é iterativa: ao identificar um erro previsível do agente, o ambiente é ajustado para impedir a recorrência da falha, transformando improviso em engenharia. Para sustentar a autonomia contínua de um agente por longos períodos, como em sessões de programação de horas, o Harness Engineering engloba a definição de ferramentas, processos de validação, consultas de informações contextuais permitidas, restrições e orientações (guidance) passo a passo para o agente.

**Prompt Engineering** foca na forma de comunicação com o agente, organizando a formulação da instrução e o uso de técnicas como Chain-of-Thought e Few-Shot. Seu objetivo é melhorar a troca de informações entre humano, agente e outros componentes, visando otimizar a qualidade da resposta.

**Context Engineering** define o que o agente pode "ver" ou ter acesso para executar a tarefa, incluindo dados, documentos e histórico. Ele controla a janela de contexto – o que entra, o que sai e quanto da tarefa cabe naquele espaço – com o critério de fornecer o mínimo de informação necessária, e não o máximo possível, para que o agente trabalhe eficientemente.

O instrutor explica que o Harness Engineering engloba o que será pedido ao agente (Prompt Engineering), o contexto que será disponibilizado (Context Engineering) e o ambiente em que ele vai operar. Não substitui as outras camadas, mas as envolve e coordena, lidando com as condições operacionais que tornam a execução confiável e estável por longos períodos. A engenharia do Harness está na composição deliberada do ambiente para apoiar o comportamento do modelo, visando previsibilidade e redução de retrabalho.

**Pontos de atenção**
*   **Abordagem Iterativa:** Em Harness Engineering, a cada falha previsível do agente, o ambiente deve ser ajustado para que o erro não se repita, transformando improviso em uma prática de engenharia.
*   **Objetivo do Prompt Engineering:** Concentrar-se em como formular a instrução e usar técnicas de prompting para otimizar a comunicação e a qualidade da resposta do agente.
*   **Princípio do Context Engineering:** Fornecer apenas o *mínimo necessário* de contexto para a tarefa, em vez de sobrecarregar o agente com o máximo de informação possível, controlando a janela de contexto de forma eficiente.
*   **Distinção de Escopo:** Harness Engineering engloba e coordena Prompt Engineering e Context Engineering. Ele não os substitui, mas cuida das condições operacionais para a execução autônoma contínua, enquanto Prompt foca na instrução e Contexto na visibilidade.
*   **Necessidade para Autonomia Duradoura:** Prompt e Context Engineering isoladamente são insuficientes quando o agente precisa programar de forma autônoma por horas, tornando o Harness Engineering (com suas ferramentas, validações e arquitetura) indispensável.
*   **Resultados Esperados:** O objetivo do Harness Engineering é alcançar um fluxo de trabalho estável, aumentar a previsibilidade, reduzir o retrabalho e tornar o agente mais útil em cenários reais de desenvolvimento, e não apenas obter uma boa resposta pontual.
*   **Evitar Confusão de Termos:** É fundamental entender as diferenças e interconexões entre Harness Engineering, Prompt Engineering e Context Engineering para evitar tratá-los como sinônimos e garantir o uso correto de cada disciplina.