Módulo: Arquitetura na Era da IA\
Aula: [Reescrevendo Planejamento](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18120)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, no vídeo anterior a gente caiu nessa situação,

00:03

a gente criou um plano e etc.

00:05

Mas como eu falei para vocês, a gente precisa de uma rede de segurança.

00:09

Então o que eu vou falar é o seguinte, aqui para o meu Cloud no modo planejamento.

00:14

Uma vez que você tem

00:19

de forma determinística a cobertura nesse

00:26

plano, quero

00:28

adicionar uma das etapas...

00:32

mais importantes que não colocamos que

00:37

é uma rede de segurança de testes para

00:44

os componentes dessa

00:49

forma teremos

00:54

menos medo de refatorar ok?

00:59

de refatorar então eu vou

01:04

colocar assim, logo avalie profundamente

01:10

os testes atuais, com

01:23

um plano de criar os

01:28

testes que realmente importam para o negócio, ou seja,

01:35

que trabalham e mudam o comportamento do sistema,

01:43

incluindo integrações e

01:49

regras de negócio.

01:52

E remova testes óbvios e

01:56

rasos que não agregam valor, tá?

02:05

Agora tem um ponto aqui, tá, pessoal?

02:07

Isso aqui é uma observação importantíssima nesse prompt, tá?

02:12

Tome muito cuidado pra você fazer o que eu tô fazendo aqui, tá? Que é

02:18

definir quais são os testes que são importantes pro

02:21

negócio e pedir pra ele remover teste. Galera...

02:25

Eu recomendo que,

02:26

principalmente se você estiver num sistema grande ou qualquer coisa desse tipo,

02:29

não faça necessariamente um prompt raso dessa forma.

02:32

Eu estou colocando aqui muito mais por questão de tempo.

02:35

Nosso aspecto aqui não é criar o melhor código do mundo,

02:38

tá? Mas você tem que tomar muito cuidado e

02:41

ter uma definição muito clara do seu projeto,

02:44

da sua equipe, da estratégia que vocês têm de teste, principalmente,

02:49

para dizer... O que é um teste importante ou o que é um teste que não?

02:53

Qual teste que é redundante eu posso remover? Qual teste eu devo criar?

02:58

Somente para você fazer um negócio desse e o sistema sair removendo um monte

03:02

de testes que às vezes eram importantes e às vezes ele criar até testes demais.

03:07

No nosso caso aqui eu escrevi de forma simplificada

03:09

porque é um exemplo pequeno e tudo mais.

03:12

Mas, novamente,

03:13

tome muito cuidado na hora de você fazer a refatoração

03:16

e na hora de fazer a criação de testes.

03:20

E vou colocar,

03:21

se tiver que fazer alguma

03:26

modificação em arquivos para refatoração,

03:32

utilize TDD,

03:35

que é Test Driven Development. Ou seja,

03:37

Ele escreve o teste primeiro e depois faz o teste não passar,

03:42

faz a alteração do código e depois disso faz o teste passar.

03:46

Ou seja, não sei se você tem conhecimento de TDD.

03:50

Mas eu super recomendo.

03:51

E uma das formas que eu vejo que é uma das formas mais

03:53

seguras hoje em dia de trabalhar com IA é também utilizando TDD,

03:57

porque você consegue focar bastante no negócio. Então, vai uma dica boa.

04:02

Faça alguns testes utilizando o Test Driven Development.

04:05

Tudo que eu tenho feito ultimamente,

04:07

utiliza. E eu tenho tido, assim, muitos bons resultados, tá?

04:11

Não é regra e não é algo que você possa falar

04:14

Wesley está falando para todo mundo só usar TDD.

04:17

Não. O que eu estou dizendo é que TDD está sendo

04:20

muito efetivo para muitos tipos de projetos que eu desenvolvo, tá? Então,

04:24

vou dar um Enter aqui para ver a nossa iteração. Perceba, galera,

04:28

estou fazendo isso da forma mais simples possível e manual,

04:31

porque o meu objetivo aqui não é te dar uma skill pronta

04:35

para você dar um Enter e resolver os seus problemas dos seus testes.

04:38

Não, o que eu quero aqui é que você entenda realmente,

04:41

de fato, em nível mais arquitetural, em nível mais baixo nível, né?

04:47

Como você deve se preocupar com os componentes do seu sistema?

04:50

Aí, se em algum momento você quiser automatizar,

04:53

você criar skills, fazer um monte de coisa, fica na liberdade.

04:57

Mas o que eu quero trazer agora aqui para você são questões...

05:03

mais arquiteturais, um pouquinho mais de baixo nível,

05:06

e por isso que eu acredito que seja importante eu fazer manual,

05:10

mesmo que eu não tenha um prompt preciso,

05:12

eu poderia estar copiando e colando,

05:14

mas eu estou iterando aqui e fazendo esse processo junto com vocês,

05:17

e o interessante é que durante esse processo eu não sei o que vai acontecer.

05:24

A gente tá fazendo isso em conjunto, né?

05:25

Eu tô gravando essa aula de forma não determinística,

05:29

não consigo forçar o resultado dessa aula aqui pra gente, então vamos aguardar.

05:34

Bom, pessoal, ele gerou a parte aqui, a gente vai ler junto,

05:38

eu não li, tô fazendo isso com vocês aqui, tá?

05:41

Uma coisa que ele falou é que ele encontrou um ponto crítico do SIDS.

05:46

Não são idempotentes.

05:48

Eu não sei se você sabe o que é idempotência,

05:51

mas basicamente é algo que prevê algum tipo de duplicação.

05:55

Imagina que eu rodo duas vezes o sistema para preencher meu

05:59

banco de dados e ele vai duplicar os dados.

06:01

Idempotência é quando você consegue perceber que aquela informação já está lá,

06:05

logo, ela não precisa ser mexida. Como a gente está trabalhando com,

06:09

entre aspas, um banco de dados em array aqui, etc.

06:13

Ele fala que não está sendo idempotente,

06:15

logo, ele vai ter que ter um helper para fazer um reset e um recede ali por testes. Se ele vai criar um teste,

06:22

ele tem que conseguir zerar a base e criar de novo. Aí ele colocou aqui,

06:26

plano atualizado, nova parte C, rede de segurança com os testes, o coração do plano.

06:31

C0, isolamento, descobrir que os seeds não são idempotentes.

06:35

Ele colocou aqui a solução, limpeza, remover 18 testes rasos.

06:40

Testes que importam desconto real,

06:42

A regra se é elegível, estoque, multa e etc., etc., etc.

06:48

Abordagem por tipo de mudança. A rede de segurança usa a caracterização,

06:52

Trava o comportamento atual, passa a ver.

06:54

Ou seja, ele está falando o importante. A refaturação piloto,

06:58

A parte D usa TDD para ele fazer a refaturação.

07:01

O detalhe que corrigi é que o skip original acertava a ordem por status,

07:05

Mas o create order lança falha. Então,

07:08

Ele trouxe alguns pontos aqui. Agora, olha só que interessante.

07:13

Ele está perguntando se eu quero que... Se eu tenho alguma ressalva,

07:18

Ordem ou coisa desse tipo, tá?

07:21

Ele manteve o plano e esse piloto não derruba o Order Service ainda e etc.

07:26

A prova de que a linha se sustenta

07:29

É ser criado mais três testes críticos verdes,

07:34

Cobertura nova e dar um npm start inalterado. Agora, galera,

07:38

Eu vou passar uma dica para você, tá?

07:40

Uma dica com todo o coração do meu carinho. O que eu faço, eu vou falar o seguinte.

07:44

Reanalise,

07:47

Reanalise todo o plano. E

07:52

Principalmente na parte

07:56

De testes automatizados,

08:03

Busque por edge cases

08:06

E pontos cegos que

08:11

Eventualmente não seriam testados.

08:20

Galera, sempre quando você fizer um módulo de planejamento,

08:24

Independente da ferramenta, tá?

08:26

Se você quiser ter uma chance maior de sucesso ali na IA,

08:32

Quando ela gerar um plano, escreve assim pra ela.

08:36

Analise seu plano e busque por edge cases ou qualquer coisa que

08:41

Possa fazer com que o resultado esperado não funcione da melhor forma possível.

08:46

Algo desse tipo.

08:47

E estou falando isso de forma manual aqui, tá?

08:50

Perceba que tudo que eu estou fazendo é manual

08:52

E eu quero que você tenha essa experiência.

08:55

Eu sei que a gente já veio de módulos de SDD, né?

08:59

Módulos de Harness, Engineer, muita coisa roda automático de implementações,

09:04

Mas para você criar toda essa linha de proteção e etc.,

09:09

Você tem que ter fundamento e por isso que eu estou

09:11

Fazendo as coisas aqui de uma forma mais manual.

09:15

Aqui pra gente tá então basicamente essa é a pegada

09:20

Vamos aguardar agora que a IA terminar e assim que

09:27

Ela terminar a gente volta no próximo vídeo porque eu não

09:30

Quero deixar esse vídeo gigante aqui pra gente, vamos nessa

## Resumo IA

[RESUMO_IA]