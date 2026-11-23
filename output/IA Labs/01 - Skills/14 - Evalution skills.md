Módulo: IA Labs\
Aula: [Evalution skills](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18280)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, então vamos dar continuidade aqui e agora a gente vai falar sobre um tema que

00:04

é bem legal também e que acaba aí fechando a parte de skill de forma geral,

00:10

que é o processo de evaluation, de avaliação,

00:14

se a nossa skill está performando da forma que deveria,

00:18

pontos aí que a gente pode melhorar e principalmente

00:23

se ela está trigando na hora.

00:25

que ela deve ser trigada, ou seja,

00:28

está executando quando realmente deveria ser executada.

00:32

Então, vocês podem reparar que,

00:34

assim como o código que eu falei lá no começo,

00:38

que a skill passou a ser código a partir de agora,

00:41

a gente vai precisar, de tempos em tempos, retornar a skill e dar manutenção nela,

00:48

fazer testes, entender se realmente...

00:52

A skill que a gente criou no passado ainda é válida,

00:55

está funcional da forma que deveria ser, tá? E pensando nisso,

00:58

foi criado um carinha que se chama Skill Creator,

01:01

tá? Esse Skill Creator é da própria Anthropic, ok? Ela é padrão aberto,

01:07

então roda em qualquer tipo ali de skill, né? Basicamente,

01:10

é uma skill que foi feita para avaliação da skill,

01:15

então envolve ali processos determinísticos também,

01:18

e a gente vai utilizar essa ferramenta.

01:21

para que a gente consiga realizar esse processo de avaliação. Antes disso, galera,

01:27

queria só mostrar para vocês aqui como é que faz o processo de instalação,

01:30

caso você nunca tenha realizado esse processo. Então,

01:34

estou aqui no meu skills .sh, ok? É o nosso site,

01:38

inclusive, vai estar disponível aí para vocês.

01:40

E também tem o GitHub, que é da própria Anthropic.

01:43

Lá na pastinha Skills, temos o Skill Creator, tá?

01:47

Como é que faz para utilizar esse carinha? Você pode fazer de duas formas.

01:51

O primeiro é através do próprio Cloud Code,

01:54

que eu já mostro para vocês como vocês conseguem colocar dentro do

01:57

projeto de vocês ou instalar de forma global também via plugins.

02:01

Ou se você preferir, você pode vir aqui, clicar no Skill Creator.

02:06

Obviamente, vai ter que fazer uma pesquisa aqui, né? E copiar e colar.

02:11

E aí a gente já tem o nosso processo de instalação rolando, tá? Vou voltar.

02:16

Lá no nosso Visual Studio Code, eu vou mostrar aqui também via plugins.

02:20

Então, barra plugins, a gente consegue fazer um search aqui,

02:25

skill creator, e a gente tem aí a possibilidade de instalação por aqui também.

02:31

Se você preferir, da forma que eu apresentei, abra um novo terminal,

02:37

vá até a sua pasta do projeto

02:42

e cole o que a gente copiou lá.

02:47

Basicamente, o que vai acontecer é,

02:48

vou selecionar qual tipo de CLI que eu estou trabalhando, vou pressionar um Enter,

02:55

vou dizer que eu quero instalar no meu projeto, tá?

02:58

E vou dizer que eu quero copiar para o meu Agents.

03:03

Então, o que aconteceu aqui?

03:04

Ele gerou o meu Skill Creator e gerou também um

03:08

link simbólico para o uso dentro do Cloud Code,

03:11

perfeito? Como vocês podem perceber aqui,

03:13

como eu disse, ele... É uma skill que tem diversas coisas dentro dela, né?

03:18

Então, a gente tem presença de agents, a gente tem presença de assets, eval viewer,

03:24

referências, scripts. É, de fato, uma camada,

03:29

uma skill, né? De nível 3 aí.

03:33

E, claro, né? A gente vai ter o nosso skill.md,

03:36

que vocês também podem dar uma olhada aí, entender como é que foi feito e tudo mais.

03:40

Recomendo bastante, inclusive. Ok? Bom, partindo desse pressuposto,

03:46

Agora, vou só reiniciar aqui o meu Cloud Code. E vamos nessa.

03:52

Para esse exemplo nosso ser extremamente didático, o que eu vou fazer aqui?

03:57

Eu vou criar o seguinte: Query Optimizer.

04:03

Vamos colocar aqui um badge.

04:05

Vou gerar um skill.md. Ok?

04:12

Basicamente, eu tenho aqui um conteúdo. Ok?

04:19

Eu vou copiar. E aí a gente conversa sobre isso.

04:24

Mas é para ser realmente muito ruim.

04:30

Bad Query Optimizer.

04:35

E aqui eu vou ter basicamente como usar.

04:38

E como vocês podem analisar aqui. Não tem nada de muito diferente.

04:43

Basicamente eu gerei uma skill aqui. Super simplificada.

04:47

Para que a gente rode o nosso eval. E a gente consiga reparar ali.

04:52

O que vai dar de resultado.

04:55

E aí um outro ponto. Que é interessante. E agora já executando de fato.

05:01

Iniciando a parte da execução. Do nosso processo.

05:04

De avaliação de testes. Poderia dizer.

05:07

É que quando a gente vai trabalhar com o eval.

05:09

A gente precisa adicionar. Um arquivo aqui dentro.

05:16

Que é o que? A parte de evals.

05:20

Então. Vou gerar aqui.

05:24

eval.json.

05:26

Sua cargo aí de curiosidade, né? Isso também faz parte,

05:30

tá? De boas práticas de skill. Então,

05:34

esses nomes aqui devem permanecer da forma que foi escrito aqui. E aí, eu tenho

05:41

basicamente alguns dados aqui que a gente vai utilizar de teste. Então,

05:46

qual é o princípio base para que a gente

05:48

consiga trabalhar com esse processo de benchmark,

05:51

de teste de... avaliação, da forma que você achar melhor o nome.

05:56

Primeiro, eu tenho que ter uma skill. Segundo,

05:59

eu tenho que ter um dataset e esse dataset vai conter itens, entre aspas,

06:04

bons e itens, entre aspas, ruins,

06:07

para que a gente consiga realizar a nossa avaliação.

06:10

E baseado nisso,

06:12

a gente vai rodar o skill creator que vai fazer esse

06:15

processo de avaliação e então vai identificar o que deveria acontecer.

06:22

e o que não aconteceu. Além disso,

06:25

a gente também tem algumas formas de trabalhar esse processo de avaliação,

06:31

que é verificando a nível de trigger,

06:37

ou seja, se a skill foi chamada quando ela deveria ser chamada,

06:42

e também verificando a qualidade do resultado,

06:46

se o resultado produzido era aquilo que foi esperado ou não.

06:51

Nesse nosso caso, a gente está iniciando aqui, primeiramente,

06:55

pela parte de trigger.

06:58

Como vocês conseguem reparar aqui no nosso pequeno dataset.

07:03

Temos aqui nove itens apenas,

07:05

É claro que isso em uma skill real,

07:08

E no dia a dia a gente vai ter muitos datasets com vários dados

07:13

Para que a gente garanta que realmente o

07:16

Negócio está funcionando do jeito que deveria. Então,

07:18

Aqui a gente vai avaliar o nosso Shoot Trigger. Como vocês podem perceber,

07:23

Temos alguns aqui que são true e outros que são false,

07:26

Beleza? Feito isso, feito esse setup breve aí,

07:30

O que vai acontecer a partir de agora?

07:34

Bom, deixa

07:36

Eu navegar para

07:40

Dentro do nosso Eval Specs e aí iniciar meu Cloud Code.

07:44

E agora o que a gente vai fazer é chamar o Skill Creator e pedir...

07:52

Para que ele rode o processo aqui de avaliação. E baseado nisso,

07:57

A gente vai entender qual vai ser o resultado.

08:00

Bom, e aqui eu posso, desde chamar via slash command,

08:03

Eu também posso pedir a descrição, né? Como, por exemplo,

08:06

Gere o teste de disparo ou de trigger da nossa skill Bad Query Optimizer,

08:12

Tá? Mas no meu caso aqui,

08:14

Como a gente está trabalhando com foco em mostrar isso, né?

08:19

Eu vou literalmente digitar este cara aqui e vou pedir para testar a

08:25

Nível de Trigger, Skill,

08:29

Bad, Query, Optimizer.

08:32

Vamos rodar aí e vamos entender o que vai acontecer.

08:37

Quando eu faço isso aqui, entre os panos, o que está acontecendo aqui?

08:41

Ele está indo até o nosso QCreator e aqui vocês podem perceber

08:45

Que ele vai começar a rodar vários itens que pertencem aqui ao script.

08:52

Então, basicamente, esse carinha aqui, como que a gente pode ver,

08:55

É um monte de scripts Python que

08:58

Vai avaliar esse processo de trigger ou não, tá?

09:05

Por meio aqui de determinados algoritmos, tá?

09:08

Não vou entrar exatamente como tudo funciona e tudo mais,

09:13

Mas basicamente ele vai utilizar os scripts e ao

09:16

Final de tudo vai conseguir produzir o nosso resultado.

09:20

Vamos ver aqui o que está acontecendo. Ok. Vamos

09:29

Continuar aguardando e vamos ver o que vai acontecer. Bom,

09:38

Já está rodando. Agora a gente tem que entender qual vai ser o resultado. Vamos

09:45

Dar uma olhada aqui no

09:48

Nosso baseline. Beleza.

09:56

Aqui, já começou a aparecer. Então, o que a gente tem aqui?

10:00

Veja bem que a gente tem o nosso

10:03

Skill, que nós montamos, tá? E aí, o que ele fez? Ele fez uma cópia, vamos dizer assim,

10:09

Basicamente criou um workspace e aqui ele está rodando todas as informações.

10:15

Então, ele pega os dados que estão aqui, faz a leitura,

10:18

Gera essa minha pasta e começa a trazer as informações para um workspace específico, tá?

10:26

E se a gente reparar, já temos aqui o próximo passo, né?

10:29

Mas antes do próximo passo, vamos dar uma olhada aqui.

10:32

Do que ocorreu. Bom, baseline foi finalizado e o resultado é bem revelador. Então, vamos lá.

10:41

Seu query Talenta. Otimize para mim. Seu query Talenta. Otimize para mim. Sim. Ok.

10:48

Falhou. Melhore a performance desse select.

10:50

Falhou. Essa consulta demora alguns segundos. Deixe mais rápida.

10:54

Falhou. Sugere índice para acelerar

10:58

a query. Também falhou. Explique. Passou.

11:04

Então, aqui nos casos que não deveriam passar. Beleza. Aparentemente,

11:07

nos casos que não deveriam travar, está tudo certo.

11:11

O problema está sendo mais aqui no que não deveria disparar. Então,

11:16

a gente tem aqui um score de 4 para 8.

11:21

Inclusive, ele faz aqui um diagnóstico que ele previa,

11:25

over-trigging, mas na verdade é under-trigging.

11:28

Então, ele me oferece alguns próximos passos. Isso que é o mais interessante.

11:34

O que está acontecendo aqui? Depois que ele percebe que algo está errado,

11:39

através desses logs que eu havia falado com vocês,

11:42

o que ele vai fazer? Ele vai já te dar algumas opções de otimização e tudo mais.

11:49

Então, eu vou fazer o seguinte.

11:53

Até para a gente não estender muito, vamos parar por aqui. Vou colocar aqui no item 5,

11:58

parar por aqui e me dar o relatório com o diagnóstico.

12:05

Vamos ver aí qual vai ser o relatório produzido.

12:10

De bola, temos aqui o

12:13

resultado. Então, basicamente,

12:15

ele fez aqui um pequeno levantamento de tudo o que aconteceu.

12:19

E aí eu já tenho um relatório.

12:22

Poderia ter pedido também para ele gerar HTML, não tem nenhum tipo de problema.

12:27

Quando acontece da nossa skill ser extremamente ruim,

12:30

como foi o que aconteceu agora,

12:34

geralmente ele nem vai te dar a opção do HTML,

12:37

mas por padrão ele vai utilizar o HTML para demonstrar os resultados.

12:42

Então, o que a gente vai fazer?

12:43

Eu vou dar um novo comando e a gente vai rodar de novo a mesma coisa,

12:49

porém agora a gente vai entender o processo de otimização. Por quê?

12:54

Porque isso aqui é muito interessante e é isso que o processo de manutenção

12:59

de uma skill vai prever daqui para frente nos seus projetos e tudo mais.

13:05

Vamos aguardar aí e a gente vai entender um pouquinho melhor. E olha aí, pessoal.

13:10

Eu já fui aqui pedido para selecionar qual é

13:15

o meu próximo passo baseado na baseline já existente.

13:18

Então, o que eu quero aqui? Como eu disse para vocês,

13:21

o Skill Creator tem essa facilidade.

13:26

Facilidade no sentido de que ela te dá as opções do que você precisa fazer.

13:33

Então, nesse caso aqui em específico,

13:35

no qual a nossa skill nem chegou a disparar quando ela deveria disparar,

13:42

o que ele já está me ofertando aqui?

13:44

Tem duas opções basicamente. Ou eu expando e meço novamente,

13:49

ou eu já começo um processo de loop contínuo

13:54

para que a gente consiga melhorar a nossa skill.

13:58

E essa é a questão que é muito bacana.

14:02

Basicamente, isso aqui a gente consegue fazer

14:05

aquele conceito de autocorreção de forma automática.

14:10

O próprio Skill Creator traz esse processo,

14:14

esse looping acontecendo. Então, vamos explorar aqui o item 2 e,

14:19

se necessário, a gente roda de novo.

14:21

Bom, temos aqui o nosso resultado. O que ele fez aqui,

14:24

galera? Basicamente, ele gerou um novo dataset.

14:28

E também, se a gente reparar no browser, ele abriu aqui para mim,

14:32

no qual ele está me pedindo para fazer uma revisão,

14:36

se faz sentido ou não. Não vou me atentar a isso aqui,

14:40

mas óbvio, no caso da realidade,

14:43

é muito importante que a gente dê uma olhada e

14:47

consiga saber se faz sentido aquilo que foi proposto ou não.

14:53

Com isso, o que a gente vai fazer aqui? A gente vai dar continuidade dizendo...

14:59

E pode rodar. E aí, o que vai acontecer? Agora,

15:03

ele vai pegar esse nosso eval de trigger criado

15:07

por ele e vai começar o processo de otimização.

15:12

Vamos lá ver o que vai acontecer a partir de agora, tá?

15:17

Bom, enquanto ele está rodando aqui, como ele mesmo avisou,

15:21

já está rodando em background. Então, se a gente aperta para baixo aqui,

15:24

a gente consegue ver o que está acontecendo, né? E aí,

15:29

a gente... Só aguarda e depois ele vai compilar todo o resultado.

15:35

E aí a gente tem aqui o resultado. Então, veja bem,

15:39

galera. Vamos dar uma analisada aqui no que ocorreu.

15:46

Bola, criou ali a atualização do meu resultado.

15:51

E o resultado ainda permanece em 0%,

15:54

mesmo com o eval, com o dataset que ele mesmo criou.

16:00

E aí a gente tem a causa raiz. Olha só,

16:03

já conseguiu identificar a causa raiz. E, obviamente,

16:07

quando identificou a causa raiz, o que foi pedido?

16:10

Pedido para que a gente reescreva a nossa description.

16:13

Então, a gente tem duas formas aqui de se trabalhar. Ou peço para ele já fazer isso,

16:20

ou posso vir aqui de novo, mais uma vez, simplesmente

16:25

rodar novamente.

16:28

Vamos ver aí qual vai ser. O resultado. Então,

16:31

eu estou explorando aqui junto com vocês,

16:33

né? E a gente vai fazer esse processo de otimização.

16:37

Primeiramente, a gente vai trabalhar ali a nível de description, tá?

16:41

Que é o que a gente está fazendo neste momento.

16:44

Novamente, paramos ali no processo de escolha, né?

16:48

No qual ele tentou mais uma vez e,

16:51

de novo, caiu no mesmo problema. Descrição genérica. Agora, o que a gente vai fazer?

17:00

De melhoria dessa skill, tá bom? Então,

17:03

qual que é o escopo real que o Bad Query deve cobrir, né? Primeiro ponto.

17:10

Só otimização, performance, leitura, tudo para banco de dados.

17:15

E aí, neste caso, o que a gente tem que parar e analisar,

17:18

galera? Lembra lá das aulas iniciais.

17:21

Skill, o que é uma skill, como eu crio uma skill, isso deve ser uma skill ou não.

17:28

Então, agora a gente vai... Utilizar tudo aquilo. Porém de uma outra forma.

17:32

Para a gente otimizar isso aqui. Com a ajuda da Skill Creator.

17:36

Neste caso. Vamos focar aqui só no processo de otimização.

17:41

Para a nossa demo. Então, vamos lá. Vamos aguardar aí.

17:45

Escolheu. E agora vamos entender o que ele vai fazer.

17:47

Temos aqui o resultado. E aí o que ele falou para a gente. Foi o seguinte.

17:54

Montou. O dataset expandido. Manteve os outros originais.

17:58

Temos aqui o que deve disparar. E o que não deve disparar. E aí.

18:04

Vamos rodar. Vamos disparar o loop de otimização.

18:10

E aí vamos ver o que vai acontecer.

18:13

Então o que está acontecendo aqui? Ele novamente gerou.

18:17

O nosso dataset ali. Agora expandido.

18:21

E agora começamos o loop de

18:27

atualização ali para acompanhar como é que tá sendo. Otimização.

18:32

E aí a gente vai entender aí como é que vai ser o resultado.

18:36

Estamos aguardando finalizar. Tudo está rodando em subagentes, tá?

18:41

A gente pode dar uma olhadinha aqui,

18:44

clicando um pouquinho abaixo, né? Na verdade, setinha para baixo.

18:49

Basta aguardar aí o resultado.

18:52

Voltando aqui, pessoal, enquanto tá executando, olha só que interessante,

18:55

né? Como eu disse, é um looping. Então, ele

18:59

iniciou, conseguiu algumas confirmações a partir da primeira iteração,

19:05

foi para a segunda,

19:06

está na terceira e vamos chegar provavelmente até na quinta.

19:11

Então, vamos aguardar para a gente conseguir saber até

19:15

que ponto a gente vai conseguir otimizar isso aqui.

19:19

Bom, galera, voltamos aqui e olha só,

19:21

vamos encontrar aqui os nossos achados, né? Então,

19:25

rodou cinco interações e a gente tem aqui

19:27

os resultados do teste de trigger especificamente,

19:30

tá? Vamos lá. Vamos

19:34

analisar aqui qual foi a melhor descrição.

19:39

E a melhor descrição pelo loop foi a original.

19:43

E olha só que interessante, né? E por que disso?

19:45

Porque nenhuma candidatura bateu o baseline no teste. Todas empataram,

19:49

basicamente, 50% de acurácia, né? Então, olha só,

19:55

com base na decisão acima, o que ele nos deu.

20:02

O gargalo não é a descrição.

20:04

Pelo menos, não por enquanto, né?

20:07

E ele achava que era. Então, o que é o gargalo? É a skill.

20:12

Depois que ele investiu aqui 5 itens, ou melhor, 5 iterações,

20:17

refinando o texto da descrição, basicamente ficou no mesmo local. E aí,

20:23

o que ele está me pedindo para fazer

20:27

com base no processo que ele fez acima de looping?

20:33

Vamos fazer aqui. Escreva o

20:39

conteúdo

20:42

da skill de acordo com

20:46

os achados na

20:49

investigação dos

20:55

testes.

20:57

Vamos ver aí o que vai acontecer. Então,

21:01

temos aqui o resultado. Ele falou que já sobrescreveu a skill,

21:06

aplicando ali as alterações. E agora a gente tem um corpo com uma metodologia,

21:11

um catálogo de antepadrões. E agora temos um próximo passo,

21:15

que é rodar novamente o teste. Então, vamos pedir.

21:19

Para ele rodar o teste. Enquanto ele roda,

21:21

a gente vai dar uma olhadinha aqui no que ele fez.

21:24

Então, a nível de skill, olha só. A gente saiu daquela skill simplista.

21:30

Na verdade, uma skill péssima. Que foi criada com essa intenção.

21:34

E agora a gente tem algo muito mais concreto.

21:40

Fluxo de trabalho muito mais definido. Então, tendo a query.

21:44

Leia o plano de execução.

21:49

Diagnostic O, baseado no checklist de antepadrões.

21:54

Proponha a correção.

21:56

Confirme, medindo novamente.

21:58

E siga determinados princípios. Caso você precise de referência de antepadrões, o que ele fez?

22:04

Ele adicionou um template de referências.

22:07

E aqui a gente tem todo um template indicando o que é bom,

22:11

o que é ruim. E aí, galera,

22:13

o que a gente vai fazer agora? Vamos fazer o seguinte, então.

22:16

Eu vou pegar esse carinha aqui. E vou deletar,

22:18

tá? E aí, vamos abrir um novo terminal. Vamos

22:28

para dentro de eval specs. Agora com a nossa skill reescrita,

22:33

né? E vamos rodar a nossa skill creator.

22:37

E vamos fazer aqui nosso

22:41

bad query optimizer. Esse é o nome, não é isso? Exatamente.

22:47

Prontinho. Agora... Repare que eu só chamei dessa vez,

22:51

não passei nenhum tipo de descrição e tudo mais. O que vai acontecer aqui?

22:55

Vai gerar alguns datasets para mim e após isso ela

22:58

vai começar a fazer o processo de eval.

23:02

Vamos pedir agora para rodar aqui o eval e iterar.

23:07

Não precisamos mais mexer na parte de descrição porque

23:11

a skill foi refeita e vamos acompanhar aí o resultado.

23:16

Então mais uma vez está sendo criado aqui. O nosso workspace. Está gerando.

23:25

Basicamente. Algumas iterações. Que ela vai testar. Agora já está testando. A

23:31

skill em si. A gente pode. Dar

23:36

uma olhada aqui. Foi gerado alguns itens.

23:39

Inclusive. De eval. Está fazendo agora. Teste.

23:46

Vamos deixar. Os agentes rolando aí.

23:49

Sete agentes. Finalizados. Com sucesso.

23:53

Vamos esperar aí agora o resultado final para a gente entender como

23:58

que a gente se saiu aí com a nova skill.

24:01

Bom, após seis minutos, temos aqui o resultado. Então, vamos dar uma olhada, né?

24:07

O que aconteceu aqui, galera? Então,

24:08

ele fez algumas escritas dentro do nosso workspace,

24:12

tá? E finalmente conseguiu gerar o resultado agora final,

24:16

baseado naquilo que a gente reescreveu, tá? E aí, se a gente...

24:23

Dá uma olhada. Ele até gera um HTML, conforme eu havia dito para vocês,

24:27

né? E já deixa disponível aqui neste endereço na porta 31.17.

24:34

Logo mais a gente vai dar uma olhada nele. Mas,

24:36

basicamente, ele também fala aqui o que aconteceu,

24:40

né? Então, baseado nos evals aqui que ele criou de input e tudo mais,

24:44

ele teve esses resultados de baseline, né?

24:49

Então... Temos aqui o relatório, paginação,

24:52

subquery e o pass rate em cada um dos itens. E por fim,

24:58

ele dá aqui um overview geral, além do relatório em HTML.

25:04

Mas tem um ponto que eu acho que é bem importante aqui,

25:06

Que é que ele também te deixa livre

25:11

para você discorrer sobre aquilo que você quer saber.

25:15

Então, ele até fala aqui, se você quer saber se...

25:19

A skill está realmente funcionando como deveria e tudo mais.

25:22

Só você me perguntar. Então, vamos fazer essa pergunta para ele. Em resumo,

25:28

A skill está funcionando conforme deveria funcionar.

25:34

Faz sentido ter essa skill?

25:41

O que mais a gente pode perguntar aqui?

25:46

Ah, uma coisa, né? Dado os

25:52

inputs e

25:54

a baseline,

26:00

O resultado foi ruim.

26:04

Médio, bom, excelente.

26:08

E podemos fazer para melhorar. Vamos ver aí o que vai acontecer.

26:14

Enquanto ele está processando, o que a gente vai fazer? Vamos lá no browser.

26:18

Vamos dar uma olhadinha aqui. E aqui a gente tem o nosso resultado.

26:22

Então, nós temos aqui o output.

26:25

Acessando nosso localhost. Vocês podem...

26:31

acessando aqui o localhost 3117, vocês podem dar uma olhada, tá? Vamos aqui no output,

26:37

basicamente eu consigo passar item a item daquilo que foi testado,

26:41

tá? Dou meu feedback se necessário,

26:44

tenho aqui o next que eu vou passando as interações e entendendo

26:49

aquilo que foi feito e qual o resultado daquilo que foi feito,

26:53

né? Aqui tem o prompt e aqui é o answer. Então sempre vai ser primeiro,

27:00

com a skill e

27:02

depois sem skill.

27:06

Obviamente, as mesmas perguntas para a gente fazer essa comparação.

27:09

Da mesma forma que a gente tem o benchmark e faz

27:13

o breakdown ali do número de evals que aconteceu.

27:16

E aqui a gente consegue ver o pass rate e tudo mais, consegue ver o delta,

27:21

que é a diferença ali entre os dois e entender o que foi feito,

27:27

como foi feito, o que passou, o que não passou.

27:30

E baseado nisso, a gente consegue tomar as ações. Bom,

27:33

vamos voltar lá no nosso Visual Studio Code e

27:36

vamos ver aqui o que ele nos deu de resultado.

27:42

Então, resumo. A skill está funcionando como deveria. Sim,

27:45

ela faz exatamente o que o MD promete, conduz o diagnóstico por evidência.

27:52

Nenhum dos runs com a skill alucinou,

27:54

ignorou o explain ou chutou índice no escuro.

27:58

Então, tecnicamente, está funcionando aqui.

28:01

Faz sentido ter essa skill? E aí, como eu já esperava,

28:06

aqui ele vai falar que o benefício é menor do que parece.

28:12

O ops por sozinho, o próprio modelo que eu estou utilizando aqui,

28:16

já seria capaz de executar aquilo que foi executado pela skill.

28:22

Então, ele fez até uma comparação. Acertou 88% aqui,

28:26

se comparado com o acerto de 100% da skill. Então,

28:30

ou seja... Não ensina exatamente o modelo a otimizar,

28:34

porque ele já está treinado para isso.

28:36

Mas serve para garantir a consistência do nosso troubleshooting,

28:40

do método passo a passo.

28:42

Em relação à qualidade de resultado, bom, não excelente.

28:47

Bom porque cumpre o objetivo e é confiável.

28:49

E não é excelente porque o delta sobre a baseline é estreito.

28:52

Conforme a gente pode ver, 88 para 100 não é uma diferença tão grande.

28:57

Problema fundo dos testes, três inputs são fáceis demais,

29:00

cada um tem um X-Play limpo,

29:02

com gargalo escrito quase na cara. Enfim,

29:06

aqui ele faz a próxima etapa da otimização.

29:11

E aí, novamente, aqui é o momento em que a gente tem que parar,

29:14

analisar o que de fato a gente está construindo, como a gente está construindo,

29:18

fazer todo aquele trabalho mental que a gente já comentou e começar a analisar.

29:25

Se a gente está indo para a direção que a gente quer ou não.

29:29

Beleza, pessoal? Mas isso a gente vai continuando aí na nossa próxima aula.

## Resumo IA

[RESUMO_IA]