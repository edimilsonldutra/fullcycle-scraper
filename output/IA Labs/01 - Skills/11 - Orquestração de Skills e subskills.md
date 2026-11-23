Módulo: IA Labs\
Aula: [Orquestração de Skills e subskills](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18277)

## Resumo da aula



## Transcrição

00:00

Pessoal, dando continuidade aqui,

00:02

agora a gente vai falar sobre aquela percepção de granularidade,

00:05

sub-skills e como a gente consegue trabalhar neste sentido.

00:12

Para facilitar,

00:13

a gente vai pegar um caso de uso bem comum para o nosso dia a dia e a gente

00:17

vai criar aqui em conjunto para a gente começar

00:19

a entender como fazer essa orquestração utilizando somente as skills.

00:26

Qual vai ser o foco aqui da nossa criação? Basicamente,

00:29

agora a gente vai codificar um pouco e para isso a gente vai gerar

00:36

algumas skills que vão nos dar a

00:39

forma com que eu quero entregar aquele código.

00:43

Seja seguindo determinadas boas práticas,

00:46

seja criando convenções específicas sobre uma boa prática. Enfim,

00:53

a gente vai conseguir juntar e fazer com

00:56

que as skills se orquestrem daqui pra frente,

01:00

tá? Então, vamos lá. A nível de código mesmo,

01:03

de produto que a gente vai gerar aqui nessa demo,

01:06

não é o foco, tá? A gente pode pedir qualquer coisa.

01:10

O nosso foco aqui é, de fato,

01:11

entender essa camada aí de orquestração e como que a gente

01:14

vai fazer com que as skills se conversem entre si, beleza?

01:19

Primeira coisa, então, já tem aqui mais um diretório criado, tá? Não tem nada.

01:24

Vou gerar apenas um src aqui pra ficar fácil da gente trabalhar. Pois bem,

01:29

agora com essa separação, a gente vai fazer o seguinte.

01:32

Vamos implementar aqui, inicialmente, duas skills,

01:36

tá? Uma vai chamar a outra e ela vai ser uma orquestradora, perfeito? Então,

01:42

vamos lá. Primeira coisa que a gente tem que fazer aqui, pessoal, é o seguinte.

01:46

Crie uma

01:49

nova skill. Vou dar o nome aqui de implementing

01:53

feature, por exemplo, implement feature, que

01:59

será um orquestrador de

02:03

implementação de uma feature por completo. Essa

02:10

skill não vai escrever diretamente o

02:17

código, mas

02:20

sim delegar cada camada do

02:25

código a uma subskill específica.

02:31

E aqui, caso eu queira até padronizar a ordem que eu quero que isso aconteça,

02:37

eu também posso fazer isso.

02:39

Então, só a título de exemplo,

02:42

vamos aplicar aqui uma ordem na

02:47

camada do código utilizando uma subskill específica,

02:53

aplicando ordem, por exemplo, bottom to up.

02:59

Ou seja, vou implementar o meu domínio,

03:02

por exemplo. Depois, adapter, se existir.

03:07

Depois eu posso ter

03:09

serviços. Depois eu posso ter repositório. E no final,

03:13

eu tenho a implementação da minha rota.

03:16

Então, se você perceber bem o que eu estou pedindo aqui,

03:19

é basicamente uma arquitetura baseada em camadas.

03:23

Na qual eu tenho a minha camada de domínio,

03:26

Que vai ser responsável por toda a lógica de negócio.

03:30

Tenho adaptadores, caso venha a existir, servir como providers ali.

03:36

Depois eu tenho o meu serviço,

03:38

que vai orquestrar os repositórios juntamente com o domínio.

03:43

E por fim, eu tenho a rota sendo implementada, que vai chamar o meu serviço. Beleza?

03:49

Nada muito fora do que geralmente a gente está acostumado.

03:53

Ficou de bola? Então, vamos lá.

03:57

Vamos colocar aqui também o seguinte.

04:01

E para cada arquivo

04:04

será necessário a execução

04:08

do planejamento e também é a

04:15

execução primeiro

04:19

invocar a

04:23

subskill correspondente em camada

04:27

está sendo trabalhada a

04:32

subskill vai produzir o

04:36

arquivo garantindo testes daquele arquivo

04:44

Aplique referências, caso

04:50

exista, que

04:54

estão disponíveis dentro da pasta difference. Vou

05:04

pedir também para,

05:06

opa,

05:12

caso item de decisão fale, execute

05:19

o stop e pergunte ao usuário como vou seguir.

05:24

Easy task tool, por exemplo.

05:28

Vamos rodar aqui e ver o que ela vai produzir.

05:31

Depois a gente vai melhorando o resultado.

05:36

Bom, galera, vamos dar uma olhada aqui e vamos ver o que aconteceu, tá? Então,

05:40

nós temos aqui um mapa de camadas com a nossa subskill.

05:44

Então, toda vez que eu tiver...

05:46

Uma camada de domínio, temos aqui implementar domain, adapter, implementar adapter,

05:52

service repository, e também temos aqui o nosso route.

05:56

E por fim, também temos a parte de geração de teste, tá?

05:58

Quando o cloud, cada subskill, ela deve ser executada,

06:03

e o que fazer quando ela não existir?

06:05

Então já temos aqui, e a passagem de contexto também para a nossa subskill, beleza?

06:10

Posterior a isso, temos a nossa pipeline,

06:12

que é basicamente a definição de como isso vai...

06:16

funcionar na prática. Então, cada camada tem aqui o que se espera de

06:24

cada item e qual é o fluxo que deve ser seguido ou que, pelo menos,

06:28

deveria ser seguido. Lembrando que são itens não determinísticos.

06:31

Então, tudo começa do nosso domínio.

06:34

Adapter, se existir, vai para o nosso serviço,

06:36

vai para o nosso repositório até chegar lá na route.

06:40

Se a gente analisar isso aqui,

06:42

está invertido com a lógica que o usuário acessa a nossa aplicação.

06:45

Por quê? Ele vai... acessar pela minha route.

06:48

Depois ele vai para o nosso serviço,

06:50

baseado no controlador ou na rota que ele acessou,

06:54

o serviço então vai chamar os meus adapters.

06:56

Os repositórios, que vai chamar também o meu domínio quando necessário e tudo mais.

07:00

E aqui ele apontou algumas regras de fluxo. E óbvio,

07:04

caso tenha algum tipo de decisão a ser tomada,

07:07

o que tem que ser feito? Tem que parar e executar algumas verificações.

07:12

E agora, vamos ver o corpo. Da nossa skill de fato.

07:17

Então vamos lá. Bom. Aqui. Eu já tenho.

07:21

Uma descrição muito bem feita. Juntamente com a lowered tool.

07:24

E aqui eu tenho um orquestrador. Já estou dizendo aqui que ele não.

07:28

Escreve código. Primeiro ponto. Mapear a feature em camadas.

07:33

Carregar o contrato da camada. Seguindo aqui.

07:38

Vou fazer. Um ciclo. Por.

07:41

Arquivo. Ou seja. Invoca uma subskill.

07:45

Subskill. Produz o resultado, aplica as referências e executa a porta de decisão,

07:50

que é aquele nosso gatezinho de qualidade, beleza? E o fechamento nós temos aqui.

07:55

Show de bola. Bom, vamos dar continuidade nesse cara aqui,

07:59

colocando agora o seguinte, pessoal.

08:03

Primeira coisa que a gente deve fazer aqui é

08:06

o quê? Deixa eu abrir um novo Cloud.

08:11

Já gerei aqui o meu SRC.

08:14

E deixa eu dar uma olhada.

08:17

em como foi criado aqui a nossa descrição. Então, implemente a nossa feature x.

08:24

Beleza. Então, a primeira coisa que a gente vai fazer agora é o quê?

08:30

Com a minha skill orquestradora, eu vou

08:34

gerar, na verdade, vou gerar numa nova sessão mesmo,

08:38

porque daí a gente continua trabalhando na skill principal,

08:41

que é a orquestradora, dentro dessa sessão. Então,

08:44

a gente gera mesmo uma nova sessão, gerar uma nova skill para complementar.

08:51

Mais que a orquestradora. Implementar a feature.

08:58

Beleza. O

09:00

foco está na construção. Da pipeline.

09:07

Vou basicamente.

09:11

Vamos gerar.

09:14

Todas as skills. Mas o nosso foco vai ser só em uma.

09:17

E aí posteriormente. Vocês podem pegar essa implementação. E ir trabalhando melhor.

09:24

Em cada nível da pipeline. Mas o nosso foco aqui vai ser mais na camada de domínio.

09:28

Perfeito? Então o foco está na construção da pipeline.

09:31

Nas sub...

09:34

Presente. No...

09:41

Camadas .md Vamos

09:46

só verificar aqui.

09:49

Beleza. É isso mesmo. Tá? E na... Pipeline .md

09:55

Construir... Cada sub-skill. E...

10:04

Para... Cada item criado deve

10:14

-se primeiramente fazer um pré-check e load de informações de

10:20

convenções do projeto em si que

10:23

estará dentro da pasta chamada architecture.

10:36

Dessa forma.

10:38

Contendo os arquivos nesse padrão. Convention,

10:48

camada, .md.

10:51

Ao ler o arquivo de convenção,

10:55

aplique no processo de

10:59

implementação como fonte da verdade.

11:04

E aí, galera, o que eu fiz aqui? Basicamente,

11:07

o que eu estou criando neste caso aqui são as nossas

11:10

sub -skills que estão dentro da camada em si.

11:14

Só que note o seguinte.

11:17

Eu comecei a granularizar. Então eu tenho o meu orquestrador.

11:20

E agora eu vou ter múltiplas skills.

11:22

E o meu orquestrador vai tomar conta. E vai chamar.

11:25

Só que dentro ainda. Dessa minha sub skills. Eu estou dizendo que.

11:31

Antes da execução acontecer. Ele deve buscar.

11:34

Uma pasta chamada. Architecture.

11:39

Verificar se existe.

11:41

Arquivos de convenção específico. Desse projeto para aquela camada. E aí sim.

11:46

Leio isso, aplicar, caso exista, e aí produzir o código.

11:52

Então, veja que nessa minha subskill, eu poderia já, por padrão,

11:56

colocar critérios claros de como eu quero que ela funcione.

12:01

Por exemplo, uma subskill de domínio,

12:03

né? Poderia dizer, olha só, você vai utilizar domínio rico, você vai utilizar value,

12:09

object e tudo mais. E dentro dessa minha convenção, além de...

12:15

Toda essa questão de domínio rico, VO, como eu espero que ele seja construído,

12:21

eu vou dizer, olha só, além disso,

12:24

você vai seguir esse modelo aqui de convenção,

12:28

que é para o meu projeto. Pensa que estou seguindo um framework,

12:32

mas dentro do framework eu estou customizando a forma que eu gosto de trabalhar.

12:39

E aí o que a gente vai fazer? Vou gerar aqui a nossa pastinha de architecture. Beleza?

12:47

Então, executando aqui, vamos dar uma olhada no que vai acontecer.

12:53

Bom, galera, está sendo gerado aqui.

12:55

Vamos aguardar mais um momento aí e ainda não conseguimos terminar.

13:01

Enquanto isso, vamos só dar uma olhadinha aqui como é que está ficando.

13:05

Seguindo novamente aquelas mesmas convenções que a gente

13:07

já está trabalhando e vamos aguardar aí ela terminar.

13:13

Continuando aqui, pessoal, aparentemente tudo certo, tá? Então,

13:17

Vamos pegar de novo aqui a nossa skill de domínio,

13:20

que ela vai ser nosso ponto -chave de partida, tá?

13:23

Vamos verificar o que que tá ocorrendo aqui.

13:26

Inclusive, só a cargo aí de curiosidade, né?

13:30

Eu poderia botar aqui no meu front matter o disable model,

13:35

pra que eu não conseguisse chamar isso diretamente via slash command,

13:40

via barra, alguma coisa, tá?

13:43

E aí deixar realmente só a skill orquestradora. chamando essas sub -skills.

13:49

Mas, não é o nosso foco agora, tá?

13:51

Vamos focar aqui mais na parte da implementação de fato.

13:55

Então, passo zero, faz ali o nosso pre -checkout,

13:59

no qual eu tenho ali a pasta

14:03

já criada e vai buscar convention domain. Inclusive,

14:07

já até gerei esse carinha aqui pra ficar mais fácil pra gente,

14:11

depois mostro pra vocês. Depois, vou trabalhar.

14:14

Como fonte da verdade. A convenção que foi acabada de ler.

14:18

Vou implementar o domínio. E aí neste caso aqui.

14:22

Como eu disse. Não passei muitas informações.

14:25

Do que eu quero que seja implementado. Então ele inferiu.

14:30

Baseado no que foi colocado. Na minha feature de implementação. Lá em camadas.

14:35

Porque aqui se você reparar. A gente tem.

14:40

Que são entidades, value objects, regras de negócio e tudo mais. Ou seja,

14:45

a gente conclui que nós estamos trabalhando com o domínio rico aqui, beleza?

14:49

Então, baseado nisso, ele inferiu aqui algumas etapas chaves.

14:54

Depois, teste e temos também um portãozinho de decisão e

14:59

o que eu espero que aconteça após a minha finalização.

15:05

E aí, como eu disse para vocês,

15:07

isso aqui se repetiu em praticamente todos os itens, tá?

15:12

Caso eu quisesse...

15:13

E mais a fundo eu poderia colocar um checklist aqui dentro da minha própria skill,

15:19

tá? Com uma listinha de referências.

15:21

Fazer um script que verificaria

15:24

esse shape que eu desejo atingir,

15:29

né? A nível de implementação.

15:30

E também pediria pra minha skill realizar essa minha checagem.

15:36

Mas, nesse primeiro momento, vamos continuar da forma que tá aqui somente.

15:42

Com informações a nível de skill. Então,

15:45

mostrando para vocês aqui um pouco da convenção.

15:48

Eu simplesmente pedi para gerar aqui algumas informações.

15:55

Inclusive, coloquei também aqui algumas documentações que são a nível de biblioteca.

16:00

Depois a gente fala sobre isso.

16:02

E aqui eu tenho basicamente o que eu espero de convenção.

16:05

Então, tem aqui desde a forma de estruturar a nível de conteúdo,

16:10

de fato. Depois eu tenho como eu devo criar e

16:15

exemplos, tá? Como vai funcionar um value object,

16:20

repositório,

16:22

erros, o que é legal, o que é proibido e coisas nesse sentido.

16:29

E só pra referência aí de vocês, tá? Inclusive vou fazer uma breve alteração aqui.

16:35

Isso aqui eu peguei de um projeto que já está em uso. Então, de fato, é algo que...

16:43

Vocês podem utilizar aí no dia a dia, tá?

16:47

Caso vocês tenham, por exemplo, bibliotecas, galera, como o Zod,

16:52

ou qualquer outra biblioteca aí do dia a dia que vocês usam,

16:55

e querem colocar informações,

16:58

ou seja, o seu jeito de usar, as suas convenções,

17:01

você também pode criar dentro de Architecture ou qualquer outro local,

17:05

no caso aqui, Docs Convention, como você espera que o Zod seja utilizado, tá?

17:11

E aí... Para facilitar para a gente, o que eu vou fazer aqui?

17:15

Eu vou gerar uma pastinha docs e

17:19

vou gerar uma pastinha conventions, tá? E vou copiar esse

17:26

carinha para cá, que é o meu Zod, beleza?

17:30

Só para bater ali com as convenções que a gente tem,

17:32

eu já consigo chegar aqui. Show de bola?

17:36

Bom, seguindo isso, então, o que a gente pode fazer?

17:39

Vamos gerar mais uma seção do Cloud.

17:44

E agora eu vou fazer o seguinte. Quero implementar uma feature

17:51

de produto no

17:54

qual um produto possui

17:58

Os seguintes atributos. Name,

18:04

Description e

18:08

Price. O

18:11

Nome deve ser obrigatório juntamente com o preço. E

18:21

Não pode ser zero.

18:25

Definindo ali. Apenas algumas regrinhas de negócio básicas, tá?

18:29

E eu

18:36

consigo gerar um novo produto, consigo listar os

18:44

meus produtos existentes. Tudo

18:50

isso feito

18:54

em memória, utilizando array

18:59

list.

19:03

Vamos ver o que vai acontecer aqui.

19:07

O ponto importante, né, foi que eu acabei...

19:10

Não chamando a minha skill. Então vamos

19:18

só dar

19:21

uma nova seção aqui. Vou chamar a minha skill.

19:24

Que é implement feature.

19:31

E aí eu vou. Novamente passar aqui. As minhas informações.

19:35

E vamos ver aí o que vai acontecer. Olha só.

19:41

Ele já identificou que é um orquestrador que vai delegar alguma coisa.

19:47

Está lendo ali os meus arquivos de convenção.

19:50

E vamos ver o que vai sair.

19:53

Continuando aqui. Passo 1. Mapa de camadas. Então é uma feature de produto.

19:57

Contendo aqui as informações.

20:02

Domínio. Adapter no caso. Não vai precisar.

20:05

Temos aqui o meu service. Temos também o meu repository.

20:08

Que vai ser persistido em memória.

20:10

Exatamente da forma que eu falei para ele. Então. Ordem.

20:14

Bottom to up. Já chamou

20:19

a minha subskill. Conforme eu havia

20:22

previsto que ele iria fazer, ou seja,

20:23

iniciei pela implement feature e aqui agora ele já identificou que eu estou na

20:29

nível de camada de domínio e já começou

20:33

então a trabalhar na implementação do domínio.

20:36

Então, olha só o que aconteceu,

20:38

já bateu no meu portão de decisão.

20:40

E aí o que ele está perguntando aqui? Qual stack você prefere utilizar? Então,

20:45

vou usar aqui TypeScript, por exemplo, um scaffold mínimo,

20:50

porque a gente não tem nada, veja só. Dentro do meu SRC.

20:54

Camada de router, vamos colocar aqui o sim.

20:58

Expor via HTTP.

21:01

Utilize, por exemplo, o RONO, que é um framework bem simples de ser trabalhado.

21:07

E vamos ver o que vai acontecer se ele vai continuar,

21:11

de fato, o processo na pipeline.

21:12

Então, aparentemente, tudo que a gente está fazendo aqui está indo de acordo com o

21:19

que a gente imaginava que seria, né, pessoal?

21:22

Ó, já registrou as minhas decisões e agora já começou a trabalhar,

21:27

né? Fez ali um boilerplate muito simples de TypeScript e

21:31

agora provavelmente ele vai começar de fato a trabalhar nos itens do projeto em si, né?

21:37

Que é a parte de código, onde vai fazer domínio,

21:42

repositório e coisas nesse sentido. Vamos continuar ali aguardando.

21:47

Continuando aqui, olha só, já começou. A escrever, inclusive,

21:52

Ponto importante, né? Seguiu ali a parte de teste.

21:55

Vamos ver como é que está sendo feito aqui, ó. Criou o nosso erro.

21:59

Criou o nosso erro específico de produto.

22:02

Gerou o nosso value object, tá? Gerou o nosso produto. Gerou o nosso repositório.

22:10

Vamos ver aqui. Gerou também os nossos testes, seguindo exatamente a nossa pipeline.

22:15

Interessante. E olha só. Camada de domínio já passou com todos os nossos testes.

22:20

Vamos ver aqui o que vai ocorrer.

22:22

Já pediu a camada de serviço. Bacana.

22:25

As convenções de serviço, repositório e route não existem.

22:30

Bom, e aí nesse caso, pessoal, como não existe, o que eu vou fazer aqui?

22:32

Como eu já tenho esses arquivos prontos,

22:34

eu vou trazer isso para dentro do nosso projeto.

22:40

E aí a gente faz de conta.

22:45

Que nós temos tudo isso gerado. Ok. Então, vamos trazer.

22:50

Esses carinhas para cá. Está faltando o repositório.

22:53

Está faltando o adapter, né? Então, já tenho aqui o meu domínio, o service, route. Certinho.

23:04

Olha. Novamente, na pasta arquitetura, coloquei.

23:10

As convenções.

23:12

Vamos ver aí o que ele vai fazer. Já conseguiu.

23:17

Identificar a existência das minhas convenções, tá?

23:21

Lembrando que o nosso foco aqui tá somente na parte do domínio em específico,

23:25

mas vamos continuar aqui pra gente entender até onde ele

23:28

consegue chegar com essa pequena ideia que nós tivemos até então.

23:33

Bom, todas as convenções aqui foram carregadas, então,

23:37

e agora é bem provável que ele já dê o próximo passo aí da pipeline,

23:43

que é implementação dos nossos serviços, né? Vamos ver aí como é que vai ser.

23:47

O resultado. Enquanto ele está gerando aqui, pessoal,

23:49

vamos dar uma olhadinha aqui no nosso domínio,

23:51

o que ele produziu. Só para a gente ter uma ideia, então, Clash Domain Error,

23:55

os nossos Value Objects, beleza? Depois a gente passa mais a fundo.

24:00

Temos também a nossa interface e temos também o meu produto,

24:04

que aparentemente está bem bacana. Show! Vamos continuar lá.

24:10

Vamos voltar para cá. Vamos dar uma olhada no que está sendo produzido.

24:14

Ó, mais uma vez, fez o processo de teste, camada de serviço certinho.

24:20

De novo, seguindo a pipeline, fez a camada de repositório, bacana,

24:24

muito bom. Vamos ver aqui qual vai ser o resultado,

24:28

né? Já temos aqui as convenções de repositório

24:31

sendo aplicadas e o write acontecendo.

24:36

Perfeito que agora falta somente as rotas, né? Vamos olhar aqui.

24:41

Exatamente, falta somente os controladores ou as rotas ali.

24:46

Mais uma vez, nossa subskill sendo utilizada aí.

24:52

E aí o que a gente vai ver agora vai ser a criação das nossas rotas, né?

24:58

Então, vamos lá.

25:01

Continuando aqui, galera. Rota sendo aplicada, né?

25:06

Inclusive, aparentemente tudo certinho.

25:10

Vamos dar uma olhadinha aqui. Já gerou até o nosso main.ts.

25:13

Que é o nosso entry point. Gerando as rotas também.

25:16

E as minhas versões de teste. E agora. Trabalhando ali no script de start.

25:21

Para que a gente consiga analisar o resultado de fato.

25:24

Rodando nosso type check. Do TypeScript.

25:28

E vamos ver. Como que vai se sair aí.

25:32

Temos mais um resultado. 28 testes passando.

25:36

E também nosso type check. Está retornando.

25:42

Sem nenhum erro, agora está fazendo o nosso smoke test.

25:47

Só para a gente validar se realmente está funcionando ou não.

25:53

Fechamento, então, que é depois que acabou, devolveu essas informações,

25:57

O orquestrador basicamente vai me reportar o que aconteceu.

26:01

E aí a gente tem todo um resultado aqui.

26:05

Bom, o que a gente vai fazer antes de olhar qualquer coisa?

26:11

Aliás, nem precisamos de call out code neste caso.

26:14

Vamos só fazer aqui um src de granularidade

26:19

E vamos executar um npm run start.

26:23

A gente já tem aqui nosso resultado. Beleza. Então,

26:28

Nosso lista está totalmente funcional. Vamos voltar para cá e

26:37

Um curl para

26:40

Criar um produto. Só para eu ter mais facilmente como testar isso.

26:47

Vamos ver.

26:48

Se ele vai executar ou se vai me dar o comando de fato.

26:52

E aparentemente deu tudo certinho. Vou fazer só esse último teste.

26:57

Só para a gente entender aí.

27:01

Show de bola. Então deixa eu pegar aqui o meu curl.

27:06

Já está aqui.

27:09

Fazer um npm start.

27:11

E vamos

27:13

Ver aqui o nosso resultado.

27:19

Aparentemente tudo certo.

27:21

Vou fazer aqui um refresh.

27:25

Bacana, eu já tenho aqui realmente o nosso curl funcional. Vamos

27:32

Fazer um outro teste, só para a gente checar se nosso

27:39

Nome pode ir como nulo, algo nesse sentido.

27:43

Só para ver se a regrinha funcionou ou não.

27:45

E aí, como vocês puderam perceber, validation failed.

27:49

Ou seja, é sinal que realmente aquilo que foi proposto...

27:54

Com aquela pequena spec que a gente produziu diretamente no chat,

27:57

Foi atingido com sucesso.

28:00

Mas o ponto aqui, galera, nem é a aplicação em si, porque isso aqui é muito simples.

28:05

Não tem nada de tão complexo assim em uma aplicação dessa.

28:09

Eu quero mostrar para vocês o código produzido para a

28:13

Gente conseguir analisar e ver realmente a qualidade disso que gerou.

28:19

Então, vamos lá. Vamos primeiro aqui no domínio.

28:24

Que é nossa base principal. Se vocês repararem aqui, está extremamente bem feito,

28:31

Tá, galera? Ó, temos aqui nosso domínio. Temos aqui o create.

28:37

From row, beleza.

28:42

Perfeito. A única coisa que eu acrescentaria aqui,

28:45

Tá, é a autovalidação do meu domínio.

28:50

Que realmente não foi feito.

28:52

Provavelmente isso aqui deve estar em algum outro local.

28:55

Provavelmente dentro dos próprios Value Objects ou dentro do serviço.

29:01

Vamos dar uma olhada aqui para a gente entender se está aqui ou não.

29:06

Exatamente como eu imaginei.

29:08

O name e a autovalidação estão dentro do nosso

29:12

Value Objects porque a gente acabou trabalhando ali com dois Value Objects.

29:16

Então, neste caso, seguiu a implementação conforme eu faria também.

29:22

Vamos ver o price.

29:24

Mesma coisa também.

29:25

Se auto validando. Perfeito.

29:27

Agora aqui eu tenho no meu domínio somente a camada de interface do meu repositório.

29:33

E se eu for lá no meu serviço,

29:37

eu tenho aqui os meus casos de uso. Que aqui eu chamei de serviço.

29:41

Mas basicamente são casos de uso. Onde eu tenho aqui o meu execute.

29:45

E aí eu primeiro faço

29:48

a criação lá no meu domínio. E se der tudo certo, eu jogo para o meu repositório.

29:52

Inclusive já está logando aqui. Legal.

29:56

Temos o teste. Deixa eu pegar aqui o teste de create.

30:00

Trabalhando já da

30:03

forma que tem que ser. Ok.

30:07

Persiste. Description. Testando a ausência de dados.

30:12

Inclusive, já gerou evento também.

30:17

Vamos verificar aqui o nosso list.

30:20

Perfeito. Aqui não tem muita questão a ser analisada.

30:26

Poderíamos, caso...

30:28

Quiséssemos trabalhar também com o mock. Até para facilitar ainda mais.

30:34

Vamos olhar agora. A nossa rota.

30:39

Temos aqui o nosso esquema. Que é o DTO.

30:44

Temos aqui o nosso build.

30:46

Faço a minha rota.

30:50

Valido lá. Os inputs.

30:52

Baseado no meu DTO que eu estou recebendo do usuário.

30:55

Se der tudo certo, eu simplesmente devolvo que está inválido.

31:00

E aí, dando certo, eu chamo o meu.

31:02

Use case ali que é o meu serviço. E aí, sim, eu respondo.

31:05

Da mesma forma, a parte de listagem. Show de bola.

31:09

E aí, vamos ver o nosso repositório. Que é um repositório somente em memória.

31:13

Então, implementei lá aquela interface.

31:16

E criei aqui basicamente o novo array.

31:21

Contendo as informações ali.

31:24

Ótima implementação também.

31:26

Vamos ver o shared.

31:30

Um erro de aplicação.

31:33

Uma respostinha. E um logger.

31:37

Só para facilitar. Temos aqui o nosso resultado, se foi de ok ou erro.

31:41

E agora, vamos ver aqui no nosso entry point,

31:44

que é onde eu começo a empilhar as informações.

31:49

Então, tenho aqui a minha API sendo criada,

31:53

beleza. E o meu servidor, basicamente, é onde eu inicio o servidor Rono.

31:59

Show de bola. Bom, a implementação em si,

32:02

poderia dizer que está bem coerente com a realidade do dia a dia.

32:09

Muito boa se comparado com implementações

32:12

de projetos que rodam na atualidade.

32:16

Mas o ponto principal aqui é o entendimento

32:20

de como a gente conseguiu fazer essa pipeline acontecer.

32:25

E uma outra questão é como que a gente conseguiu fazer

32:29

com que ele gerasse um código que não é aquele macarrão.

32:34

E de fato,

32:35

código que pode ser utilizado em produção e tudo mais.

32:38

Isso tudo se deve, pessoal, primeiro,

32:40

à forma que a gente construiu as nossas skills, tá? E o tamanho de contexto, né?

32:46

As informações importantes de contexto que a gente

32:48

passou para a LLM para que ela conseguisse entender,

32:54

espelhar e trazer o resultado esperado.

32:57

E tudo isso a gente fez utilizando apenas arquivos MD,

33:02

apenas com inferência, tá? Não validamos nada de scripts e tudo mais.

33:06

Se a gente quisesse adicionar mais uma camada ainda de script,

33:09

que é determinístico para validar efetivamente aquilo que está sendo feito,

33:14

ficaria melhor ainda a nossa implementação.

33:17

Por quê? Caso acontecesse qualquer tipo de coisa que saísse daquele molde,

33:23

basicamente o que iria acontecer, o script iria falar, opa, saiu. Então,

33:27

automaticamente haveria... uma autocorreção, né?

33:32

Aquilo que a gente chama de self-healing.

33:33

E se vocês repararem bem, olha só.

33:36

É basicamente informações acerca de arquitetura,

33:41

padrões de projeto, design de código. Isso tudo aqui, galera, são fundamentos.

33:48

Fundamentos que você, enquanto engenheiro de software,

33:51

deve obrigatoriamente saber. E não só saber,

33:54

mas como utilizar, quando utilizar. É isso que diferencia, de fato,

33:59

uma pessoa que está aí acima da média, vamos dizer.

34:03

Então, se você reparar bem, a ideia da orquestração não é tão complexa assim.

34:09

Basta dar o devido contexto,

34:11

saber e entender dos fundamentos, como aplicar esses fundamentos e,

34:16

baseado nisso, a gente trabalhar no processo de orquestração. Fechado?

34:22

E, obviamente, uma informação que vale sempre relembrar é que...

34:27

O que a gente construiu aqui é só o início.

34:30

Vocês podem pegar isso aqui como base e a partir dela ir aprimorando cada vez mais.

34:35

Mas aqui está o ponto de partida. Por quê? Aplicamos os fundamentos,

34:39

aplicamos as documentações dos frameworks e aplicamos em cima

34:45

disso todas as convenções que

34:48

o desenvolvedor gostaria que tivesse.

34:52

E aí eu posso fazer isso por projeto, por time. E assim por diante.

34:56

Então, veja que a gente tem três camadas ali de customização.

35:00

Isso que é o mais interessante e o mais legal.

35:02

A gente consegue ir segregando e dando essa granularidade quando é necessário.

35:08

Fechado, pessoal? Então, é isso aí.

## Resumo IA

[RESUMO_IA]