Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17991)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, como é que eu falei no vídeo anterior?

00:03

Nós temos essa situação em relação a vídeos,

00:05

né? Então, o que eu quero fazer aqui? Eu quero, na realidade,

00:10

facilitar a minha vida e ajudar aqui a desenvolver essa feature.

00:16

E essa feature, na realidade,

00:18

ela vai me ajudar durante todo o processo,

00:22

porque o upload de vídeo vai ser utilizado em tudo quanto é lugar.

00:25

Entendeu? Então, isso é como se fossem, vamos dizer,

00:28

testes automatizados. Então, o que eu posso fazer?

00:31

Eu posso colocar em modo planejamento,

00:32

posso utilizar outros plugins aqui interessantes,

00:37

mas o que eu vou fazer é o seguinte,

00:39

eu vou colocar de uma forma bem simples aqui para IA,

00:42

em modo planejamento aqui mesmo, eu vou colocar o seguinte,

00:45

no meu arroba contract.md aqui,

00:51

preciso...

00:56

de inputs estáticos conforme o documento

01:05

preciso que

01:08

você gere esses

01:11

arquivos

01:15

incluindo o thumbnail, porém o

01:23

arquivo de 2 gigas, preciso

01:31

ter um script que

01:34

será utilizado para fazer

01:39

a geração sob

01:44

demanda, pois

01:46

ele não ficará no

01:49

meu controle de versão. Os outros scripts eu posso, porque os arquivos são pequenos, no meu controle de versão.

02:02

Logo, preciso da geração desse

02:10

script avulso.

02:16

E vou dar um enter aqui para mim,

02:19

na realidade, ele tirou do meu modo planejamento, né? Deixa eu colocar aqui.

02:23

E uma coisa que é importante, por que eu estou falando isso, galera?

02:27

Porque provavelmente esse script vai acabar caindo no meu agents.md para ele

02:33

saber que toda vez que ele precisar testar um arquivo acima de 2GB,

02:37

para ele executar aquele script, porque esse script vai gerar um arquivo e aí,

02:42

baseado nesse arquivo, ele vai conseguir fazer o teste dele.

02:46

E ele não precisa gerar esse arquivo o tempo todo.

02:49

Então, esse aí é um ponto importante para a gente trabalhar.

02:54

Ou até mesmo os próprios arquivos de vídeo,

02:57

de sample e etc, podem ser gerados somente on demand.

03:00

Mas, como é um arquivo de 250 KB e etc, um arquivo pequeno,

03:04

eu acho que não tem problema desses caras estarem comitados ali no ambiente.

03:08

Mas o arquivo de 2 GB, sem dúvidas,

03:11

a gente tem que pensar ali no caso de como resolver esse tipo de coisa.

03:15

Então, esse aí é um ponto importante para a gente.

03:19

Deixa ele pensar como é que ele vai fazer,

03:21

porque eu poderia aqui, nesse momento, também pegar e fazer um

03:24

drop de um vídeo ali numa pasta e tudo mais,

03:27

mas eu só estou querendo brincar aqui com as

03:29

Possibilidades aqui com a IA para a gente.

03:31

Eu poderia pegar esses arquivos colocados dessa forma e beleza, mas não,

03:35

vamos ver como é que ela se sai aqui nesses aspectos aqui também.

03:39

Deixa ela pensar bem como que ela pode trabalhar.

03:43

E aqui ela trouxe as perguntas para mim.

03:46

Primeiro, thumbnail, o que significa incluindo thumbnail?

03:50

É o Placeholder Bundle JPEG, né?

03:53

É basicamente o que ela vai precisar de um thumbnail.

03:56

Apenas a referência, é isso mesmo. Eu não quero um thumbnail de exemplo.

04:00

Agora eu quero ver como é que ela vai fazer o script de 2 GB,

04:03

tá? Esse script de 2 GB,

04:05

eu utilizaria um Data Duplicator e não criaria o vídeo em si, tá?

04:09

Mas vamos ver como é que o nosso querido Claudio vai trabalhar.

04:14

Aqui, um script avulso de geração de arquivos de 2 GB,

04:19

oversize -video .mp4, fora do controle de versão,

04:22

deve ser de que tipo? Um shell script DD sparse,

04:26

onde eu tenho generation, oversize e fixture,

04:30

usando o DD com o SIC para criar um arquivo esparso de 0 bytes em disco,

04:36

tamanho reportado, ou um TypeScript que segue essa mesma convenção.

04:43

Para criar um arquivo esparso. Bom, rapidinho, somente para você não ficar perdido, eu não sei se você já tem,

04:49

já usou ou já trabalhou alguma coisa com o DD, tá? Mas, basicamente, DD significa,

04:54

eu acredito que é Data Duplicator. É um comando que, basicamente,

04:59

você consegue pegar um dado de uma origem e um dado de um destino,

05:04

tá? E aí você consegue contar, inclusive, né?

05:10

Contar... ou dar um seek nesse caso,

05:13

para ver em qual posição que aquela informação está.

05:19

Eu vou dar um exemplo rápido e simples aqui para vocês,

05:22

que é o seguinte,

05:23

se eu chegar aqui e dar um ls -la aqui,

05:30

se você olhar aqui, eu tenho o tamanho dos meus arquivos, está vendo?

05:35

Isso aqui é o apparent size, ou seja, o tamanho aparente do meu arquivo.

05:40

Se eu der um do aqui na frente, tá? Aqui para mim.

05:45

Sei lá, vou dar um do no meu package.json aqui para mim.

05:52

Ele vai trazer um tamanho. Se eu colocar, dar um ls aqui nesse cara,

05:57

menos la, né? Deixa eu colocar aqui, menos la.

06:03

Ele vai trazer esse cara aqui para mim também.

06:06

Então, o que eu estou querendo dizer com isso?

06:09

Estou dizendo o seguinte, opa, os números não estão batendo. Ah, é do menos h, né? Menos H.

06:18

Aqui, ó. 416 KB. E se eu der um ls -l,

06:22

ele vai trazer um fluxo de ls -la, né?

06:25

Ele vai ter que trazer também pra mim esse cara

06:28

aqui parecido também pra mim em relação a tamanho.

06:32

O que que, no final das contas, galera, isso aqui significa ali pra mim?

06:39

Então, olha que legal. Aqui a gente parece que tem algo invertido.

06:43

Por quê? Quando eu dou um ls aqui... Basicamente,

06:48

ele conta byte a byte do tamanho do meu arquivo. Quando eu dou um do aqui,

06:54

ele vê o quanto que ele está alocando em file system nos blocos meus.

06:59

E aqui, nesse caso, ele deve estar fazendo algum arredondamento de bloco, por isso que os dados,

07:05

os números, não vão bater um ls com um do, no final das contas.

07:09

Porque file system... é diferente de contar byte a byte.

07:12

No file system, ele vai contar por blocos.

07:14

Mas a grande questão aqui é que quando eu uso um DD,

07:17

eu consigo fazer um DD trabalhando com zero,

07:21

um /dev/null e /dev/zero. O que isso significa?

07:23

Ele vai pegar como se fosse um monte de zeros e

07:26

gerar um arquivo de tamanho aparente de 2 GB,

07:30

porém ele não vai ocupar nada em disco para mim. Ou seja,

07:35

eu não vou gastar espaço em disco, tamanho de arquivo em disco.

07:40

Ou seja, eu vou gerar um arquivo fake que não vai ocupar em disco,

07:43

mas quando eu for olhar no header dele, ele vai constar para mim ali 2 GB.

07:48

Então isso aí vai me ajudar bastante porque eu

07:51

não vou precisar colocar em controle de versão.

07:52

Então é uma boa, tá?

07:54

A única coisa que a gente tem que tomar cuidado aí nesse

07:56

caso é que quando ele for fazer o upload de verdade,

07:59

apesar de que ele não vai ter o arquivo alocado em disco,

08:06

ele vai ter que fazer a transferência do arquivo,

08:09

para bater o metadado e ele ver o tamanho.

08:12

E esses dados, ele vai ter que ser transferidos como stream ali.

08:17

Então, isso aí a gente só tem que tomar cuidado,

08:19

mas eu acho que essa ideia funciona bem, trabalhar com o DD aqui nesse caso,

08:24

porque ele vai conseguir trabalhar. Vai ser alguma coisa meio que DD,

08:27

if, /dev/null, /dev/zero.

08:33

Daí para o tamanho, ele tem o input, o output, o count, daí o seek,

08:37

ele bota lá para o final, mas daí isso aí é detalhe,

08:40

eu não quero chegar nesse ponto aqui,

08:42

a nossa intenção aqui não é aprender a desenvolver plataforma de vídeo,

08:46

é entender um pouco mais sobre Harness.

08:48

Então eu vou trabalhar aqui nessa pegada, aqui no script de 2 GB,

08:52

aqui para ele conseguir trabalhar, porque é uma solução,

08:56

vamos dizer, em tese que pode funcionar.

08:59

Para fazer com que a gente não tenha que ficar comitando esses tipos de coisa,

09:03

mas é importante ter esses scripts para eles

09:05

gerarem esses arquivos estáticos que vão nos ajudar. Então,

09:11

isso aí é interessante para a gente saber ali também como que a gente pode fazer, tá?

09:17

E enquanto que ele vai fazer isso, inclusive, depois, na hora que ele for fazer isso,

09:21

eu vou fazer um

09:22

commit dessa especificação no main. Mas,

09:30

esse script, esse tipo de coisa, eu vou fazer só no branch da feature 03.

09:36

Então, aqui, ele

09:39

trouxe, né? Committed features, gerar um sample.

09:45

Aqui, ele está gerando um FFmpeg, criando um arquivo da duração.

09:50

Um unsupported, ele vai gerar um bad code.

09:53

E o .gitignore, no oversized vídeo.

09:59

E o committed placeholder, e aqui o generate oversize aqui pra gente,

10:06

que é um script, ele vai criar um arquivo esparso, usando o dd e seek,

10:12

if /dev/null, off o output, bs igual a 1, count,

10:17

dando um seek de ali um byte em cima de 2 gigas,

10:20

aí ele vai trabalhar, então ele vai criar e vai fazer beleza aqui pra mim,

10:25

beleza, eu vou fazer o seguinte, eu vou dar um enter aqui,

10:28

E vou pedir para ele fazer essa implementação.

10:31

Então, galera, não sei se vocês percebem,

10:34

mas, assim, você tem que entender, de forma geral, de desenvolvimento.

10:41

Você tem que ter alguma base.

10:44

Dependendo do tipo de software que você vai desenvolver.

10:47

Se você nunca trabalhou com vídeo,

10:48

ou se você nunca trabalhou com esse tipo de domínio,

10:50

não vai ser a IA que vai fazer a mágica.

10:52

Ou ela pode até fazer,

10:54

mas o problema é quando você não tem ideia do que ela está fazendo.

10:57

Então, esses tipos de coisa têm que

10:59

ajudar a gente a entender o quanto que,

11:05

em alguns momentos, antes de eu desenvolver uma feature,

11:08

antes de analisar uma coisa,

11:09

eu tenho que ter base.

11:12

Por isso que simplesmente sair gerando a Task Writer, Implementer e etc.,

11:18

pode funcionar muitas vezes dependendo do tipo de feature.

11:21

Você vai gerar um bando de CRUD ali, nossa, isso aí vai ser fácil.

11:24

O grande ponto ali mesmo é quando você tem esse tipo de desafio.

11:28

Então, se isso não está documentado, se isso não está claro,

11:31

isso aí pode gerar uma consequência bem grande ali para o projeto.

11:37

Então, é basicamente isso. Então, aqui ele fez as fixtures estáticas, versionadas,

11:42

que até se passa features, combinei o versionado,

11:46

script avulso, generate oversize feature,

11:50

aqui para mim gera sob demanda e etc. Para materializar,

11:53

eu rodo o script aqui para a gente.

11:56

E ele não vai guardar nada no disco. Então, eu vou colocar, rode o

12:03

script oversize aqui para mim.

12:08

Vou pedir para ele executar.

12:19

E vamos lá, ó. O script detectou o arquivo que já existia, ele já tinha rodado, né?

12:23

E ele colocou onde mesmo? Ele colocou em back-end,

12:28

né? App, back-end, scripts,

12:32

generate, aqui, oversize, aqui foi o script que ele criou, e os testes, pictures,

12:39

e aqui o oversize-video.mp4, tá? Então,

12:43

esse cara aqui que é o interessante de a gente tentar...

12:46

Entender. Quer ver? Vamos olhar aqui, principalmente pela curiosidade.

12:50

Se eu colocar um do menos H,

12:54

do menos H, apps, back-end, fixtures. Opa, tá difícil. Fixtures,

13:06

testes, fixtures,

13:09

oversize, vídeo.mp4.

13:14

Olha só, tá zero bytes em disco. Mas se eu der um ls menos...

13:24

Olha só o tamanho do vídeo que ele tá trazendo aqui pra mim,

13:28

né? Se colocar o "-lh", dá

13:31

pra gente ver, ó. Tamanho de 2 GB aqui pra mim no vídeo. Então, isso aqui, galera,

13:37

é interessante pra gente ver,

13:38

porque a gente pode rodar esse tipo de script pra gente conseguir trabalhar.

13:43

Então, vamos pro que importa agora aqui pra gente, tá?

13:48

Primeira coisa que eu vou fazer, eu vou dar um commit.

13:52

Somente nas minhas documentações aqui para mim.

13:57

Para que eu tenha a feature 3 colocada.

14:01

E estou dando um commit direto no main.

14:02

Eu não vou gerar por request aqui.

14:04

Espero que você esteja entendendo o meu objetivo aqui. Não

14:11

quero gerar commit... Deixa

14:15

eu colocar aqui no... Somente no docs.

14:22

Ele estava querendo adicionar os outros caras ainda.

14:24

Os outros caras eu vou adicionar no outro branch.

14:27

que eu vou criar, tá? Então, isso aí é um ponto importante.

14:34

Será que ele já comitou? Não é possível. Deixa eu olhar aqui. Barra docs.

14:37

Cara, não tá comitado, tá?

14:41

Cara, eu acho que já tá comitado.

14:44

E o apps backend features não. Beleza.

14:47

Ótimo. Então, o que eu vou fazer agora? Eu vou dar um

14:51

git checkout -b. Eu

14:57

vou dar um git checkout -b. Eu vou colocar aqui, ó, feature 03 aqui pra mim.

15:03

E agora eu vou dar um commit aqui para mim,

15:08

para ele fazer o commit desse restante das coisas aqui para mim.

15:14

Outra coisa aqui que está me incomodando... Será que ele comitou os testes? Cara,

15:20

ele comitou os testes e a fixture para mim lá no main naquela primeira vez.

15:24

Mas beleza, eu vou fechar o olho aqui, tá, galera?

15:28

Uma coisa que está me incomodando é o gitignore.

15:34

no Playwright CLI, tá?

15:40

Maravilha, então ele tá adicionando e tem mais uma

15:43

coisa aqui que pra mim é importante agora,

15:45

tá? Que é o Cloud MD.

15:46

Vou colocar adicione de forma

15:50

curta no cloud.md. Vou

15:55

colocar agents.md pra ele não ficar procurando link simbólico.

15:58

Agents.md. O

16:00

script de geração de vídeo

16:09

oversized. Oversized.

16:20

Por quê? Porque eu quero agora que o meu agente,

16:23

na hora que ele for fazer os testes,

16:24

ele também saiba que esse script existe, né? Então,

16:27

isso aí, pra mim, é importante ele colocar.

16:30

Então, vamos ver onde que ele adicionou.

16:34

Pras testes, né? Então, ele colocou aqui,

16:36

2 gigas. Aqui, ó. 2 gigas, upload fixtures.

16:42

Tá, gitignore, generate on demand, barra. Generate Oversize a fixtures.sh.

16:50

Beleza. Então, a minha A, ela já sabe agora que eu consigo ter essa informação aqui,

16:56

caso ele precise trabalhar. Então,

16:58

isso aqui eu já estou feliz de estar colocado.

17:01

Eu vou comitar essa minha alteração aqui no cloud.md.

17:05

Não estou passando por PR, tá, galera?

17:08

Estou botando aqui e nem preciso PR, né?

17:10

Porque eu estou em um outro branch agora aqui para mim. Beleza?

17:14

Agora, o que eu vou fazer no próximo vídeo?

17:17

A gente vai iniciar o processo de desenvolvimento e a gente

17:20

vai ver como é que o agente vai se portando,

17:23

tá? Porque é aquela história. Não tem milagre, galera. Não tem milagre.

17:27

Simplesmente, o que a gente vai fazer é o passo a passo. Mas perceba,

17:31

tudo que a gente está fazendo e a gente está, vamos dizer,

17:34

gastando esse tempo agora, é pra quê?

17:36

É exatamente pra que quando a IA for desenvolver,

17:40

ela não fique perdida. Isso é harness, tá?

17:43

Ou seja... é o que eu preciso fornecer para ajudá-la ali.

17:48

E se estiver faltando algo, a gente vai perceber se ela cometer erro,

17:52

a gente vai entender qual que é esse erro e

17:54

daí a gente vai trabalhando daqui para frente.

17:57

Então, até o próximo vídeo.

## Resumo IA

**Abreviações**

*   **IA**: Inteligência Artificial
*   **KB**: Kilobytes
*   **GB**: Gigabytes
*   **DD**: Data Duplicator (comando Unix para manipulação de dados)
*   **LS -LA**: `ls -la` (comando Unix para listar conteúdo de diretórios com detalhes, incluindo tamanho aparente)
*   **DO -H**: `du -h` (comando Unix para mostrar uso de disco de arquivos/diretórios em formato legível por humanos)
*   **CRUD**: Create, Read, Update, Delete (operações básicas de persistência de dados)
*   **FFmpeg**: Ferramenta de linha de comando para manipulação de arquivos de áudio e vídeo
*   **PR**: Pull Request (mecanismo de revisão de código em sistemas de controle de versão como Git)
*   **BS**: Block Size (parâmetro do comando `dd`)
*   **IF**: Input File (parâmetro do comando `dd`)
*   **OF**: Output File (parâmetro do comando `dd`)
*   **CLI**: Command-Line Interface

**Resumo**

O objetivo principal desta aula é facilitar o desenvolvimento de uma feature de upload de vídeo, especificamente lidando com a necessidade de testar uploads de arquivos grandes (2GB) sem comitá-los no controle de versão. O instrutor demonstra como usar uma IA para auxiliar nesse processo, focando na criação de um "harness" eficaz para a IA.

Os conceitos abordados incluem a distinção entre tamanho aparente de arquivo (`ls`) e espaço real alocado em disco (`du`), e a importância de arquivos esparsos (sparse files) para simular grandes tamanhos de arquivo sem consumir espaço físico. A ferramenta `DD` (Data Duplicator) é explicada em detalhe como um comando Unix fundamental para criar esses arquivos esparsos, utilizando `if=/dev/zero` e o parâmetro `seek`.

O fluxo explicado pelo instrutor começa com a instrução à IA via `@contract.md` para gerar inputs estáticos para testes, incluindo thumbnails e um script para criar o arquivo de 2GB sob demanda. Após um diálogo com a IA sobre as opções do script, o instrutor opta por um shell script utilizando `DD`. Ele então valida a funcionalidade do script, demonstrando que o arquivo gerado de 2GB ocupa 0 bytes em disco. Em seguida, o instrutor gerencia o controle de versão, comitando a documentação no branch `main` e isolando o script e as fixtures em um novo branch (`feature-03`). Finalmente, ele atualiza o `agents.md` para que a IA tenha conhecimento do script de geração do arquivo oversized, garantindo que ela possa utilizá-lo em testes futuros. A aula conclui enfatizando a importância de fornecer um "harness" completo e claro para a IA, preparando o terreno para o desenvolvimento da feature no próximo vídeo.

**Pontos de atenção**

*   **Não comite arquivos grandes no controle de versão**: Arquivos como vídeos de 2GB devem ser gerados sob demanda para evitar inchar o repositório e dificultar o trabalho com branches.
*   **Utilize arquivos esparsos para testes**: Em vez de criar arquivos de teste gigantes que consomem espaço em disco, use ferramentas como `DD` com `if=/dev/zero` e `seek` para criar arquivos que reportam um tamanho grande, mas ocupam quase zero espaço físico.
*   **Diferença entre tamanho aparente e uso de disco**: Compreenda que `ls -la` mostra o "tamanho aparente" do arquivo (número de bytes), enquanto `du -h` mostra o "espaço alocado em disco" (que pode ser arredondado por blocos do sistema de arquivos). Arquivos esparsos são uma aplicação direta dessa diferença.
*   **Harness para IA é crucial**: A IA não faz mágica. É fundamental fornecer a ela o contexto, a documentação (`contract.md`, `agents.md`), os scripts e as informações necessárias para que ela possa desenvolver e testar funcionalidades de forma eficaz. Sem um "harness" adequado, a IA pode ficar perdida ou gerar soluções subótimas.
*   **Conhecimento de domínio é insubstituível**: Mesmo com a IA, o desenvolvedor precisa ter uma base de conhecimento sobre o domínio (neste caso, manipulação de vídeo, sistemas de arquivos, comandos Unix) para guiar, validar e corrigir as soluções propostas pela IA.
*   **Gerenciamento do controle de versão**: Tenha cuidado ao comitar. Documentações podem ir para o `main`, mas scripts de geração de dados e fixtures de teste relacionadas a features devem ser gerenciados em branches específicos, evitando comits indesejados no branch principal.
*   **Impacto de upload de arquivos esparsos**: Embora um arquivo esparso ocupe pouco espaço em disco localmente, a transferência real (upload) ainda exigirá o envio do tamanho aparente completo do arquivo (ex: 2GB), pois o sistema de destino precisará lidar com o metadado do tamanho. Este é um detalhe importante para cenários de upload.