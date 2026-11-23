Módulo: IA Labs\
Aula: [Best practice - skills](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18276)

## Resumo da aula



## Transcrição

00:00

Bom pessoal, então vamos dar continuidade aqui e dessa vez a gente vai falar um

00:04

pouco sobre boas práticas quando nós estamos trabalhando

00:07

aí na criação das nossas skills,

00:09

tá? Até então a gente falou um pouco sobre boas práticas,

00:12

porém foi bem específico ali em algumas partes do Front Matter, tá?

00:16

E nessa aula eu queria focar exatamente a nível da skill de forma geral,

00:21

porque também existem alguns pontos que a gente precisa ter atenção

00:24

no momento que a gente vai trabalhar neste processo de criação. Então, vamos nessa.

00:31

Primeira coisa que é importante a gente entender é que existem aqui seis itens. Inclusive,

00:37

já criei aqui um novo arquivo.

00:39

Vou abrir ali na preview para ficar mais fácil

00:41

a gente conversar sobre cada item desse.

00:44

Alguns vão acabar sendo repetitivos. Por quê?

00:47

Porque a gente já começou a falar sobre isso,

00:49

mas é válido para a gente revisar e dar mais ênfase.

00:52

Então, a primeira coisa é em relação à nossa description.

00:55

que tem a necessidade de ser específica e ter os nossos gatilhos concretos, como,

01:01

por exemplo, o do not use e também o must use e coisas relacionadas.

01:06

E, obviamente, se algo for vago,

01:09

ele vai ou não disparar ou disparar demais sem a necessidade.

01:15

A partir disso, nós temos o ponto 2, que é uma skill é igual a uma responsabilidade.

01:21

E aqui é um ponto que eu gostaria de tocar.

01:24

E entrar um pouco mais dentro disso aqui,

01:27

porque essa questão pode causar algumas dúvidas.

01:31

Aqui nós estamos falando de responsabilidade.

01:34

Existem projetos que uma responsabilidade pode ser mais de uma habilidade.

01:41

E por que eu estou falando isso? Porque skills é habilidade. Então,

01:47

muitas vezes nós pensamos que eu tenho que tratar isso aqui de forma muito granular.

01:54

E aí, a gente tem que ter esse discernimento que, às vezes,

01:59

o meu granular é diferente em um projeto que é diferente do outro projeto,

02:05

ou que é diferente da granularidade lá do seu amiguinho,

02:10

do seu companheiro de trabalho. Então,

02:12

como é algo muito particular essa questão de granularidade,

02:16

a gente deve primeiro fazer a nossa triagem mental.

02:21

E entender o que de fato é uma responsabilidade.

02:26

Mesmo que envolva duas habilidades.

02:29

Porque a partir disso a gente consegue trabalhar com skills,

02:32

sub -skills e coisas nesse sentido.

02:34

Inclusive é algo que a gente vai falar daqui a pouco sobre isso.

02:39

Item 3. De boas práticas.

02:42

A gente precisa já tentar ao máximo que nós

02:45

conseguirmos empurrar o peso de toda a nossa skill.

02:50

para dentro dos itens de nível 3,

02:53

que seria a parte de referências e scripts. Ou seja,

02:58

com isso a gente garante que o nosso corpo da skill fique curto,

03:03

fique imperativo, tenha um checklist ali, critérios de aceite,

03:08

né? E caso a gente tenha algum tipo de convenção,

03:13

spec, coisas nesse sentido, a gente vai...

03:17

acabar colocando dentro dos itens de nível 3,

03:20

como referência, scripts e coisas nesse sentido.

03:23

O item 4 aqui é muito importante também,

03:26

que é acerca de quando priorizar

03:29

o uso de scripts e prosa,

03:33

que é basicamente a nossa instrução markdown.

03:38

E a análise que a gente deve tomar é o seguinte,

03:40

se por acaso eu tenho algo que precisa ser determinístico,

03:46

é muito provável que ele vai virar um

03:49

script dentro daquele bundle que nós estamos criando.

03:53

Por quê? Porque isso garante um resultado consistente. Então,

03:56

toda vez que a gente for criar uma skill,

03:58

ponto importante são esses dois itens. Primeiro,

04:01

eu faço a minha skill da forma que eu acho que ela deve ser. testo ela,

04:06

mas depois eu já vou tentando jogá -la para o nível 3,

04:10

separando ali as minhas referências,

04:12

aquilo que pode virar referência,

04:14

vou verificando se existe a necessidade da inclusão de scripts internados locais,

04:19

se sim, já aparto também e tento sempre visar o meu corpo o menor possível, tá?

04:26

Finalizando, nós temos os itens de segurança, ou seja,

04:29

se você estiver executando ou utilizando qualquer tipo de skill,

04:36

Alheia, isso serve tanto para skills que você baixa e acha na internet,

04:40

como também scripts de terceiro que você vai utilizar dentro da sua skill.

04:45

É muito importante que a gente inspecione antes de

04:47

trabalhar a instalação ou qualquer coisa nesse sentido.

04:51

E, óbvio, em questões de segurança,

04:53

a gente tenta sempre trabalhar com allowed tools, porque dessa forma,

04:57

mesmo que existam determinados scripts que sejam maliciosos,

05:01

a gente consegue, através do allowed tool,

05:03

Dizer somente aquelas ferramentas estarão permitidas nessa skill. Logo,

05:09

é uma camada a mais de segurança.

05:11

Para finalizar, a parte de versionamento dentro do nosso projeto.

05:17

Por padrão, assim como o nosso código,

05:19

a gente tende a versionar a nossa skill via Git. E toda vez que existe uma mudança,

05:26

o que acontece? A gente faz essa mudança via PR.

05:30

E tentamos sempre manter essa consistência

05:33

exatamente como nós trabalhamos no código.

05:37

Vida e regra, pessoal. O negócio aqui é o seguinte.

05:40

Trate as suas skills como código. E aí vai funcionar muito bem.

05:46

E agora, para a gente finalizar aqui,

05:50

eu queria passar na prática com vocês alguns itens

05:54

desse aqui para que a gente consiga entender melhor.

05:57

O primeiro deles a gente vai aqui dentro do nosso exemplo,

06:02

que é uma skill chamada Dev Helper.

06:06

Já fiz isso aqui pensando

06:08

no fato de trazer más práticas,

06:13

mas isso aqui inclusive é bem comum de se acontecer no dia a dia.

06:19

Vou fechar aqui a minha barrinha de

06:21

navegação e vamos abrir no nosso editor. Então veja só.

06:28

Dev Helper, qual que é a minha descrição? Muito vaga, né? Ou seja,

06:32

ajuda com código, ajuda com revisão, testes e outras coisas do dia a dia.

06:37

Eu acho que está mais do que claro que basicamente o que foi pedido aqui,

06:41

Se eu peço o Cloud para revisar, se eu peço o Cloud para implementar algo,

06:47

para testar alguma coisa,

06:48

a possibilidade dessa skill aqui ser triggada é muito grande, né?

06:52

E aí o que vai acontecer? Basicamente, eu tenho aqui o corpo da minha skill.

06:57

Repare que ela nem é tão grande assim, certo?

07:00

Só que o primeiro ponto é que

07:03

tem muitas coisas dentro de apenas um local,

07:07

ou seja, ela tem que revisar código, ela tem que gerar teste,

07:10

ela tem que gerar scaffolding, é muita coisa.

07:15

O ideal neste caso aqui é o que?

07:17

A gente começar a fazer essa separação de tal forma que...

07:21

A parte de geração de scaffolding seja uma coisa,

07:24

a parte de geração de teste seja outra coisa,

07:26

a parte da revisão de código seja um outro local.

07:31

E aí a gente começa a navegar em mares um pouquinho mais escuros,

07:36

no qual a gente pode fazer que dentro dessa nossa skill,

07:41

por exemplo, de revisão de código,

07:42

a gente tenha a partir dela várias outras sub-skills.

07:48

No qual existem as convenções específicas de cada camada.

07:53

E aí eu faço uma skill chamar uma outra skill

07:57

que verifica as convenções para então conseguir gerar o nosso resultado.

08:03

Testes, as mesmas coisas. A gente tem muita convenção de teste.

08:07

Eu poderia ter skills,

08:09

a depender da granularidade que a gente está trabalhando,

08:13

específicas para Unity Test, Integration Test,

08:17

end-to-end test,

08:18

vai depender muito de como realmente eu quero trabalhar e abordar isso aqui.

08:23

Da mesma forma que o meu scaffold trabalha-se da mesma forma.

08:28

Veja bem, eu tenho novos serviços,

08:31

mas eu posso ter novos repositórios, novos serviços, novos controladores,

08:35

novos testes, novos adapters e coisas nesse sentido.

08:40

Só que, para cada um desses carinhas aqui, eu tenho as minhas próprias convenções.

08:47

Eu tenho as convenções do meu framework que

08:51

estão ainda acima das minhas próprias convenções.

08:54

Então, repare que neste caso aqui,

08:58

a gente acaba agrupando

09:02

uma responsabilidade que não

09:05

faz nem sentido estar em somente uma skill.

09:09

Inclusive, se você quiser fazer um teste,

09:12

a gente pode fazer algo mais ou menos nesse sentido aqui.

09:18

Deixa eu só pegar o nome dela aqui.

09:21

Vamos neste Cloud aqui. E vamos fazer o seguinte. Vá dentro da skill.

09:27

Dev Helper. Após isso.

09:32

Verifique em quais pedidos. Do dia a dia. Por exemplo.

09:37

Essa skill. Dispararia. indevidamente.

09:46

Me fale o motivo. E ao final. Exiba uma tabela.

09:53

Vamos ver o que vai acontecer aqui.

09:56

Bom, continuando. Vamos dar uma olhada aqui o que aquela me trouxe.

10:00

Temos um problema central.

10:04

Então, o que está faltando aqui? Está faltando os nossos 'do not use'.

10:09

Acaba indo para sobreposições de skills um pouco mais especializadas,

10:14

que é aquilo que a gente havia falado sobre

10:16

a granularidade que a gente quer trabalhar.

10:19

E aí, a gente tem aqui alguns pedidos. Então, me ajude a debugar esse erro.

10:26

Provavelmente daria ali um falso positivo, refatorar uma função,

10:30

escrever mensagem, olha só, fazer revisão.

10:34

Tudo isso ele poderia disparar. Inclusive, ele faz um resumo dos 12 itens pedidos aqui,

10:41

somente dois que realmente fazem parte ali do que ela deveria fazer.

10:47

E aqui eu pedi o porquê de cada coisa, né?

10:50

Conforme a gente já havia dito ali nas nossas best practices,

10:54

descrição, muito abrangente.

10:57

Skill faz um monte de coisa e não faz nenhuma muito bem.

11:00

E tem aqui um item coringa, que é outras coisas do dia a dia de dev.

11:06

Então, repare que até o próprio Cloud basicamente

11:09

consegue entender aquilo que foi feito errado.

11:12

E claro, você,

11:13

enquanto desenvolvedor que está ali trabalhando com as suas skills,

11:16

pode utilizar a ferramenta para ajudar no processo de criação.

11:21

Voltando aqui, agora a gente vai falar da parte boa.

11:25

Da coisa, né? Afinal de contas, mostrei a parte ruim,

11:29

temos que mostrar também a parte boa. E aí aqui, galera, basicamente,

11:34

eu compartilhei essa ideia de testes, tá?

11:39

E criei um test generation.

11:43

Então, na nossa skill aqui, veja bem,

11:46

que eu já tenho uma descrição muito mais desenvolvida,

11:49

tenho aqui os meus allowed tools, tá? E baseado nisso,

11:54

eu tenho de novo,

11:55

a presença dos meus passos a passo. Tenho a execução de

11:58

um script. Vamos ver o que esse carinha aqui vai fazer. Então, test generator,

12:04

primeiro passo: temos que achar os itens que estão sem testes. Para isso,

12:10

temos aqui o script, que é um bash, que vai

12:14

fazer uma busca determinística por itens relacionados a .test e

12:20

.spec. Depois que ele tem essa lista, tenho a minha

12:25

pequena convenção de time. Nota que ainda são itens bem pequenos,

12:30

então, por isso, isso está dentro do corpo da skill. Conforme isso aqui cresce,

12:36

obviamente, o que vai acontecer? Vai a todo momento gerar novos itens,

12:42

novos dados e há a necessidade de jogar dentro

12:46

de uma referência específica e linkar aqui dentro.

12:49

E passo 3,

12:51

baseando-se nos critérios que ele encontrou aqui,

12:55

mais os critérios de boas práticas da convenção do time, eu vou, então,

13:00

começar a criar o código-fonte do arquivo de fato, tá? Então,

13:07

vamos lá. Vamos fazer aqui o seguinte. Vou navegar para o good.

13:11

Vou executar aqui a minha skill, né? Mas, inclusive,

13:16

deixa eu alterar aqui na aula também, porque está incorreto, né?

13:23

Aí, eu vou fazer um reload das skills.

13:27

Vamos ver se ela aparece aqui. Show de bola.

13:30

Então, vamos testar dessa forma aqui mesmo, tá?

13:33

Já vou invocar de forma direta. Óbvio,

13:35

poderia também disparar ali pela minha descrição,

13:39

Mas neste caso, apenas para demo,

13:42

Fica mais simples a gente fazer desse jeito. Então, aguardando.

13:46

E olha só, já temos testes aqui sendo produzidos, tá? Então, ela já conseguiu rodar.

13:53

O script, identificar que esses carinhas aqui estavam sem

13:58

itens de teste.

14:01

Baseado nisso, ele

14:04

já conseguiu escrever os nossos testes.

14:06

Vamos dar uma olhada como é que ficou? Então,

14:07

a gente tem aqui total carrinho e aplicar cupom.

14:09

Se a gente der uma olhada aqui, temos o total carrinho, temos

14:15

o item aqui de teste zero, quando o carrinho está vazio,

14:21

quando os itens forem nulos,

14:24

somar o preço, muito bom, e também somar as quantidades.

14:30

E se a gente vem agora no aplicar cupom, aqui,

14:35

quando a gente tem nenhum tipo de alteração,

14:39

nesse caso aqui, o total 100, alteração de percentual,

14:44

aplicar de fato o percentual e zerar quando é 100%. Então,

14:50

batendo exatamente com aquilo que nós criamos de código.

14:55

Usuário, temos buscar, salvar e o render.

14:58

Então, vamos dar uma olhada aqui.

15:02

Consultou. Olha só que interessante.

15:04

Como aqui eu estou trabalhando com o banco de dados,

15:08

ele já fez o meu mock, né? Então,

15:10

ele já está utilizando, de certa forma, boas práticas, óbvio.

15:15

E dentro da skill,

15:16

eu poderia desenvolver essas boas práticas de forma muito mais assertiva,

15:20

mas só para a gente conseguir entender o nível de boa prática,

15:26

Aqui já está bem bacana.

15:28

Depois, montou

15:31

a query. Vamos ver aqui no salvar usuário.

15:34

Mais uma vez, trabalhando com mock. Muito bacana.

15:39

Aqui também, trabalhando com mock a nível de erro. E o render card,

15:44

também trabalhando com mock. Ou seja,

15:48

tudo bem legal e bem funcional. E a questão principal.

15:55

Estamos utilizando aqui exatamente aquilo.

15:58

que foi convenção dentro da nossa skill. Então,

16:02

o contraste daquilo que eu havia passado para vocês é,

16:06

de um lado, a gente tem uma skill totalmente desorganizada,

16:11

que não segue nenhum nível que a gente havia conversado, e de outro,

16:16

a gente tem um resultado já alinhado com as nossas expectativas.

16:22

Parece, num primeiro momento, algo muito simplista, mas...

16:28

Seguir esse passo a passo mental que a gente vem

16:31

criando desde o início do nosso bate-papo,

16:34

vai te trazer isso com o tempo,

16:37

né? Uma facilidade enorme de criação,

16:40

de exploração dessas ideias que podem virar skills,

16:43

beleza? Então, é isso aí, galera.

## Resumo IA

[RESUMO_IA]