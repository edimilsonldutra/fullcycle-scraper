Módulo: IA Labs\
Aula: [Orquestração com script deterministico](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/294/conteudos?capitulo=294&conteudo=18278)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, então, dando continuidade aqui, o que a gente vai fazer agora?

00:03

Vamos mexer um pouquinho mais nessa parte aqui da granularidade e

00:07

a gente vai adicionar agora um script determinístico dentro das nossas skills.

00:14

Para quê? Para que ela consiga executar uma autocorreção.

00:18

Então, a ideia aqui é o seguinte,

00:20

galera. Deixa eu fazer aqui um new. Vou fechar esse carinha,

00:24

porque a gente não vai utilizar. E, por enquanto,

00:26

vamos deixar... somente um único Cloud aberto.

00:31

Qual vai ser aqui a ideia principal do nosso script determinístico?

00:36

Vai ser limitar as nossas camadas, camadas essas, a nível de arquitetura,

00:43

do qual, se você reparar bem,

00:46

vamos iniciar desde aqui, da construção da nossa rota,

00:51

o que acontece? Nós temos a rota sendo definida,

00:54

então a gente acessa a rota da rota. A gente vai chamar o que?

00:58

Nós vamos chamar o nosso caso de uso, que é o nosso CreateService.

01:04

Então, se a gente vem aqui, nós vamos para dentro do serviço.

01:08

E dentro do serviço, a gente vai ter, por sua vez,

01:12

o domínio, bem como o produto repository e as minhas dependências. Então,

01:19

se você reparar bem, existe uma sequência e um padrão muito claro.

01:25

de como está sendo organizado a entrada e a saída desse dado.

01:30

Então, chegando aqui, ele vai acessar o domínio, criar

01:36

o que tiver que criar, neste caso aqui, criar um novo produto,

01:39

vai pegar este carinha aqui e vai mandar para dentro do repositório.

01:44

Então, como a gente bem sabe,

01:46

o serviço vai orquestrar tanto a camada de

01:48

domínio como também a camada de repositório.

01:51

E, como eu disse, existe um flow das nossas informações rolando. O ponto é,

01:58

quando a gente está trabalhando a nível de inteligência artificial,

02:03

a gente acaba tendo alguns problemas porque ela não é determinística. Então,

02:08

a gente vai adicionar essa trava determinística via

02:12

script a nível arquitetural para manter este flow corretamente.

02:17

No caso,

02:19

na prática, o que vai acontecer?

02:20

Como eu passei aqui para vocês, e da mesma forma que

02:25

Nós temos este caminho que eu acabei de percorrer,

02:29

ele também é o mesmo caminho de volta. Isso quer dizer que o

02:34

nosso domínio, você nunca vai vê-lo, por exemplo, dentro de uma rota.

02:38

Você nunca vai vê-lo dentro da construção das nossas rotas.

02:43

Por quê? Porque isso é uma quebra arquitetural que nós temos.

02:47

Então, a ideia é garantir através...

02:51

deste determinismo via script que isso nunca aconteça.

02:57

E se caso acontecer,

02:58

a gente vai meio que fazer aqui uma proposta de self-correction,

03:03

beleza? Então, vamos nessa.

03:06

Vou fazer o seguinte, vamos fechar todos esses itens,

03:10

voltar aqui no meu Cloud Code e vamos iniciar então uma nova sessão,

03:14

tá? Bom, eu vou pedir para que a gente consiga criar um script.

03:20

Vou colocar aqui script barra

03:24

check layers, por exemplo. Vou falar que esse aqui é um script.

03:31

Esse é um script. Será

03:36

Utilizado via ESLint.

03:39

Verifique se o projeto já conta com o ESLint.

03:45

Caso não, instale

03:48

e configure para receber.

03:55

Regras customizadas e também configure

03:59

comando em scripts no package.json do projeto, show

04:07

de bola, continuando aqui vou

04:11

falar que esse script

04:13

vai resolver a camada em cada

04:24

arquivo pelo path.

04:31

Vamos especificar aqui os paths existentes, repository, temos o adapter,

04:36

temos o shareage.

04:40

Também resolve os imports relativos

04:47

também e

04:49

barra as fronteiras proibidas.

04:54

Essas fronteiras serão definidas

05:00

dentro do script em questão. E aqui, galera,

05:04

obviamente não vou fazer um prompt muito grande que

05:09

vai ter todas as regras e tudo mais.

05:11

Eu vou apenas demonstrar uma das regras e aí vocês

05:14

fiquem à vontade para adicionar quando se sentirem à vontade.

05:18

Então, vou colocar aqui uma regra, por exemplo. Regra

05:24

principal.

05:26

Uma rota não pode

05:28

importar nada de src/domain.

05:35

Um domínio não

05:38

importa nada para fora,

05:42

exceto a dependência Zod que faz

05:50

parte. Uma

05:54

rota não importa repositório. Vou

06:02

botar aqui também. Vou

06:05

encolher um pouco as regras e vamos colocar assim, de forma geral, as

06:12

dependências.

06:14

Sempre apontam para dentro,

06:17

seguindo ali uma ideia de clean architecture. Então,

06:22

caso

06:25

exista alguma violação, por exemplo,

06:30

execute exit 2 mais

06:36

o erro em questão, um

06:40

bloco por violação com

06:45

a regra exposta e claro,

06:49

arquivo e a linha. O import.

06:55

Ofensor. O porquê.

07:03

Mais o que a gente pode colocar aqui. O porquê que viola. Neste caso. E como

07:10

consertar.

07:14

Mais o que eu vou fazer aqui. Isso.

07:19

Servirá para.

07:20

Um agente. Se auto. Corrigir.

07:27

Vou definir também. Adicione. Na verdade.

07:36

Já havia colocado aqui em cima, certo?

07:39

Só dar uma olhada. Sim, já está ali para adicionar.

07:43

Então, não preciso colocar aqui.

07:47

E tenho que colocar agora onde

07:51

vai ser feita a nossa edição.

07:55

Então, o que vai acontecer aqui?

07:56

A gente vai pedir para editar a nossa skill. Deixa eu abrir aqui.

08:04

De feature.

08:07

Tá? Então, editar skill

08:10

.md adicionando uma

08:14

nova etapa, passo 5 ou 6,

08:20

deixa eu ver, passo

08:24

5, efetivamente, que é o gate de arquitetura, tá?

08:31

Deve ser rodado sempre, deve ser rodado sempre

08:36

ao final da pipeline,

08:40

Tá? Vou colocar aqui

08:44

Com autocorreção. Também. Uma

08:47

coisa que eu notei aqui. É que eu coloquei para editar a skill.

08:51

Mas eu não disse qual que é a skill. Que é implement feature. Agora sim.

08:58

E aí. O que a gente pode colocar aqui. Em relação a esse passo.

09:05

Vamos deixar. O seguinte.

09:11

Depois que.

09:13

Essas camadas. Passarem.

09:19

Depois que todas as camadas forem implementadas e passarem

09:25

no teste, pode ir ao Bash,

09:31

npm run check layers, por exemplo.

09:42

Posso colocar aqui, se

09:46

houver algum erro, layer, std, error,

09:56

autocorrija, cada... violação,

10:05

delegando para a sub-skill correta,

10:10

referente à camada ofensora.

10:19

Repita o processo. Vamos colocar aqui meio que um max retry. Na

10:27

verdade, para esse exemplo,

10:28

eu vou colocar que ele repita o processo até que o exit seja zero. E aí,

10:37

eu posso colocar o seguinte, se as

10:45

tentativas passarem de 10, conforme ao

10:51

usuário, e utilize a tool ask

10:55

user question.

11:02

Defina que a tool, que a feature na verdade,

11:06

só está pronta com o gate verde. Vou

11:14

rodar aqui e ver.

11:19

Qual que vai ser o resultado, galera?

11:21

Bom, pessoal. Vamos ver aqui, então, como é que foi o resultado,

11:25

né? Foi mais ou menos aí quase oito minutos.

11:28

Vamos ver o que aconteceu.

11:30

Então, temos aqui o script criado. Beleza. Vamos

11:39

analisar aqui o que ele fez em relação às telhas. Beleza. Conseguiu gerar. Bacana.

11:57

Inclusive, já até gerou aqui um belo resumo.

12:01

Então, já está sendo resolvido. As camadas via path.

12:04

ESLint foi curado. E também temos regras customizadas.

12:09

Que é aquela regra que a gente fez. E a skill foi adicionada.

12:14

Deixa eu dar uma olhada. Na skill.

12:18

Para a gente entender o que aconteceu.

12:22

Passo 5. Vamos fazer aqui um Open Preview.

12:25

Para a gente ver. Passo 5.

12:31

Loop de autocorreção. Show de bola.

12:35

Muito bacana.

12:37

Para a gente dar continuidade, até antes de testar, o que eu vou fazer?

12:41

Ele recomendou aqui que a gente faça um audit fix.

12:45

Existem algumas vulnerabilidades,

12:47

mas isso neste momento para a gente não importa tanto.

12:51

A gente vai fazer o seguinte.

12:53

Adicione o projeto

12:56

granularidade ao

13:01

arquivo.

13:04

Cloud.md e Agents.md.

13:09

O que vai rolar aqui, pessoal? Como eu disse para vocês,

13:12

o Cloud MD é específico do Cloud Code, mas vocês podem utilizar o Agents.md.

13:18

Inclusive, se você quiser utilizar o Agents só fazendo uma referência ao Cloud MD,

13:24

não tem nenhum tipo de problema.

13:25

Ele consegue ler sem problema. E como eu também havia falado para vocês,

13:29

esses arquivos em questão, o que eles fazem? Eles são lidos.

13:33

a todo momento. São obrigatoriamente lidos. Então,

13:37

o que eu vou pedir aqui para criar neste momento?

13:41

Criar este arquivo e vou adicionar uma regrinha.

13:46

Algo nesse sentido.

13:49

Ao concluir qualquer feature

13:55

ou ao terminar de

13:59

editar. Qualquer tipo de arquivo está dentro da pasta.

14:05

src, o

14:08

último passo

14:10

obrigatório de

14:18

dizer se a tarefa foi realmente finalizada ou não,

14:25

é rodar o page determinístico.

14:30

Vamos pegar aqui qual foi o nome do package.json que ele colocou,

14:35

check layers, e

14:41

a gente vai pedir para ele rodar o nosso check layers. Via Bash.

14:46

Vamos ver. Como é que vai ser a saída.

14:50

Bom. Já está aqui.

14:53

Criando o nosso CloudMD. De bola.

15:00

Vamos ver se ele cria o Agents.md.

15:07

Ok. O

15:12

Agents.md. É apenas. Um link. Para. O Cloud.md.

15:19

Além disso. Adicione também. Os comandos. No

15:27

Cloud.md.

15:29

para trabalhar com a aplicação e

15:34

também uma

15:36

breve informação sobre a arquitetura.

15:40

Vamos até adicionar aqui um pouquinho mais de informação no nosso arquivo,

15:45

até para nos ajudar a gastar menos tokens, perfeito?

15:50

Fica, inclusive, a dica para vocês, né? É ideal sempre ter esses arquivos.

15:56

No nosso caso aqui, como a gente está em um ambiente super controlado,

15:59

não precisa, tá?

16:02

Já que já estamos trabalhando,

16:03

é importante que a gente faça assim. Então, aí, gente,

16:09

isso agora está apenas referenciando. Inclusive,

16:11

posso até tirar tudo aqui e deixar realmente só o link,

16:14

tá? E aí, como vocês podem perceber, eu tenho aqui agora algumas informações.

16:18

Deixa eu abrir no preview para vocês.

16:21

E tem exatamente aquilo que a gente havia pedido, né? Então,

16:25

os comandos aqui de como funciona,

16:27

um pouquinho da arquitetura, as camadas e tudo mais,

16:29

e o nosso gate de arquitetura, tá?

16:32

Vou fazer apenas uma alteração para reforçar mais ainda.

16:36

Na verdade, nem vai precisar, né? Que já está aqui como obrigatório, né? Bom, vamos lá.

16:45

Uma última coisinha que talvez tenha ficado um pouco de dúvida e eu

16:50

vou esclarecer neste momento em relação ao exit 0 e ao exit 2,

16:55

né? Então, basicamente, o exit 0 é quando deu tudo certo e podemos classificar aí.

17:02

Como algo pronto.

17:04

E o exit 2 é o gate vermelho. Ou seja, algo deu errado.

17:07

Então, a gente precisa trabalhar ali na autocorreção. Bom,

17:10

e agora a gente precisa testar isso. Então, vou fazer o seguinte.

17:16

Vou até pedir para o próprio Cloud aqui testar isso para mim.

17:21

Vamos testar a pipeline.

17:25

Aliás, não vou testar a pipeline por completo.

17:27

Vamos testar somente a nível de edição.

17:32

Verificar se

17:35

o gate

17:38

está funcional ou não a partir de agora.

17:42

Faça uma edição na

17:47

SRC em algum arquivo que

17:53

esteja fora das barreiras arquiteturais

17:59

impostas e vamos ver o comportamento.

18:04

Vamos ver aí o que vai acontecer. Acontecer a partir de agora.

18:09

Bom, estamos aí. Vamos ver o que vai acontecer. Já está introduzindo.

18:18

E olha só, o gate está funcional. Detectou as duas violações.

18:22

Tivemos ali nosso exit 2, ou seja, gate vermelho.

18:28

E o comportamento observado foi: temos um bloco aqui.

18:32

Já mostrou exatamente as camadas, exatamente como eu havia pedido. O local.

18:39

E isso ocorreu. Então,

18:41

cada bloco ali trouxe exatamente aquilo que desejava — e

18:45

automaticamente já passou — para uma alta correção.

18:53

E agora nós temos aqui o teste concluído.

18:59

E somente se, caso, tenha ficado algum tipo de

19:02

dúvida se a LLM rodou ou não os nossos scripts,

19:08

a gente pode ver aqui.

19:10

No nosso shell command.

19:14

Que o check layer.

19:15

Agora está certinho. Então, exit zero.

19:19

E se a gente for um pouco mais acima,

19:22

nós temos aqui. Olha só. Após o processo de edição. O que aconteceu.

19:29

Rodou automaticamente o nosso Check Layer.

19:33

E aí, olha só.

19:35

O prompt que foi passado para o processo de autocorreção no princípio.

19:42

As dependências apontam para dentro, e aí eu dou aqui as camadas,

19:46

como que é o flow dos nossos dados.

19:49

Temos aqui o erro que ocorreu, tipo de erro,

19:54

a regra, o arquivo, o import, a direção, o

20:01

por que disso, como consertar,

20:05

e a camada que foi afetada juntamente com a subskill. Aqui, neste caso,

20:11

Foi tudo dentro da rota, porque foi algo programado.

20:14

E aí, com isso aqui, o que aconteceu?

20:16

A própria LLM já disparou o processo de self-correction,

20:21

de autocorreção, melhor dizendo.

20:24

É claro que este exemplo que a gente fez agora é algo muito sucinto.

20:30

O ideal é que a gente permaneça utilizando,

20:32

gere novas features e tudo mais,

20:34

para validar integralmente se tudo está ocorrendo como deveria ser.

20:40

A nível de demonstração. Para que vocês consigam expandir a mente de vocês.

20:44

E entender até onde a gente consegue chegar.

20:47

E a gente consegue ir muito mais longe do que isso.

20:49

Eu acho que é um excelente começo. Para que vocês consigam despertar o imaginário.

20:56

E começar a criar coisas novas. Beleza? Então é isso aí.

## Resumo IA

[RESUMO_IA]