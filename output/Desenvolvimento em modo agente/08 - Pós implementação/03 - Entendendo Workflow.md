Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17985)

## Resumo da aula



## Transcrição

00:00

Então pessoal,

00:02

olha aqui somente para ficar um pouco mais fácil de você

00:05

entender a ideia aqui dessa skill com um orquestrador no meio.

00:09

Hoje em dia você já pode, por exemplo, no caso de um Cloud Code,

00:13

por exemplo, pedir para ele criar a orquestração de alguma coisa. Mas nesse caso,

00:18

a gente está fazendo de algo extremamente específico e com o contrato no meio. Então,

00:23

eu acho que essa que é a grande diferença aqui desse nosso workflow. Mas, novamente,

00:28

o que eu quero trazer para você é...

00:31

a clareza em relação à parte de orquestração. Então, nesse nosso caso,

00:35

a gente tem aqui uma skill que ela é chamada de Implement Evaluate.

00:39

Então, basicamente, o que ela acaba fazendo aqui para a gente?

00:43

Eu tenho um agente aqui,

00:45

orquestrador, que ele vai planejar todo o ciclo que ele vai fazer,

00:49

ele vai delegar para os subagentes,

00:50

vai agregar o resultado dos subagentes e vai decidir os próximos passos.

00:54

Então, o que vai acontecer no meio dessa história?

00:57

A gente vai precisar de artefatos. Então, eu continuo com o contract .md,

01:01

o spec .md, o plan .md, e a gente tem esse cara aqui,

01:05

que é o nosso prdprogress .json. Esse cara, ele vai mostrar o quê?

01:10

Em qual momento que eu estou naquela etapa.

01:15

Porém, o que acontece?

01:17

Em relação ao agente, ele vai entender, de forma geral, tudo.

01:24

que acontece e tudo o que tem que mudar e o

01:27

que vai ser mudado no meio de toda essa história.

01:30

Então, aí eu tenho os meus fluxos. Primeira coisa,

01:34

eu peço aqui para ele executar, então ele roda o nosso implement feature ali,

01:40

então ele vai implementar a mudança,

01:42

ele vai gerar e atualizar os testes e ele vai respeitar

01:45

o contract .md e vai gerar os artefatos ali para mim.

01:49

E com isso, o que vai acontecer? Uma vez que eu pego tudo isso,

01:54

o meu orquestrador vai pegar isso aqui

01:58

e mandar para avaliação todos esses artefatos.

02:02

E o meu evaluator vai fazer essa verificação e assim que ele terminar,

02:06

ele vai retornar aqui para o meu orquestrador. Se encontrar algum problema,

02:10

ele pede a solicitação para o meu fixrunner,

02:12

que é um subagente, que vai fazer o quê? Vai verificar...

02:16

problemas de bugs e etc. O cara mais expert, vamos ver,

02:20

o prompt dele é um pouco mais forte para a resolução de bugs.

02:24

E ele prepara uma nova versão e retorna para o

02:28

orquestrador e vai para o evaluator de novo.

02:31

Então aqui é um ciclo que acaba ficando e eu

02:34

tenho uma quantidade de retries que eu posso colocar.

02:37

Se aprovou, beleza, ele cai aqui para um resultado final que está concluído.

02:43

Caso não... Ele vai ficar nesse ciclo até morrer o processo.

02:47

Então, essa que é a ideia.

02:48

Agora, somente para você ter um zoom um pouco melhor em relação ao evaluator,

02:52

basicamente funciona da seguinte forma. O evaluator vai poder seguir e falar, olha,

02:58

está tudo ok. Ou ele pode falar que foi fail, ou seja,

03:02

falhou o processo, e vai encerrar e vai falar,

03:04

olha, pode voltar que realmente falhou.

03:06

Ele pode trazer, dizer que está pending, ou seja, olha...

03:11

Vai ter que ter uma reavaliação e normalmente o pending vai trazer, por exemplo,

03:15

que é porque eu tenho uma validação manual que eu tenho que fazer.

03:20

Então ele vai retornar um pending,

03:21

mas não necessariamente que falhou. E aqui ele traz um abortado.

03:27

O abortado encerra completamente o processo,

03:31

porque a partir de um abortado ele vai chamar... Um Fixed Runner.

03:36

Isso aí vai ser mandado pro Fixed Runner pra ele corrigir e trazer ali de volta, tá? Então,

03:42

a grande sacada no meio dessa história do Evaluator é que ele

03:45

acaba tendo esses status que vão ficando mais fáceis pra gente entender.

03:51

Então tá tudo certo, ou ele falhou... Beleza?

03:54

E ou ele aborta porque ele também não consegue. Uma abortagem, por exemplo,

03:58

pode ser que eu preciso de algo para conseguir testar e eu não consigo testar.

04:02

Eu tenho que levantar o ambiente, mas nem levantei o ambiente.

04:05

Então ele já aborta ali naquele momento também.

04:07

Então podem ter diversas situações onde ele vai falhar,

04:11

ou seja, a feature não bateu de acordo com o que especificava,

04:14

ou ele pode abortar quando ele pode ter alguns hard fails e coisas desse tipo, tá?

04:19

E no meio dessa história eu tenho um arquivo.

04:23

de saída. Deixa eu voltar aqui só nesse anterior,

04:26

que é um arquivo de orquestração, que ele vai falar qual que é o run ID, ou seja,

04:32

porque eu posso fazer vários ciclos,

04:34

eu posso mandar ele rodar várias vezes a mesma feature.

04:36

Então ele tem o arquivo de orquestração,

04:39

o report de avaliação, ou seja... Toda a documentação,

04:43

o porquê que aquilo foi reportado, ou seja,

04:46

tudo que ele fez em relação aos testes e como que ele avaliou.

04:50

E ele tem um orchestrate ali, .loc, para não ficar rodando coisas simultâneas.

04:55

Evitar problemas ali de concorrência é uma forma de minimizar.

04:58

E aí, no final da história, o que acontece?

05:02

Eu tenho... Deixa eu ver se eu consigo aumentar o zoom aqui para você.

05:06

Eu tenho um journal.

05:08

Persistido, ou seja, eu tenho tudo o que aconteceu no meu orquestrador,

05:11

o que foi feito, o que rodou.

05:13

Eu tenho um eval report, ou seja, tudo o que aconteceu e como que ele avaliou.

05:20

Inclusive, ele gera para a gente artefatos como os screenshots,

05:24

caso eu precise, caso eu queira,

05:26

mas por padrão ele já traz screenshots quando eu estou usando, por exemplo, o Playwright,

05:30

porque ele consegue provar que a cada momento ele foi utilizando aquela imagem como

05:36

base para conseguir sustentar aquele report que ele está trazendo ali para a gente.

05:41

Então isso aí são interessantes. Depois disso, ele já pode criar uma PR no GitHub,

05:47

E aqui tem o tracking de iniciado, falhou, update,

05:53

os cycles e os soft fails. Ou seja,

05:55

basicamente é a forma de como que o

05:59

orquestrador organiza os status e aquele nosso tracking,

06:04

que é aquele prdprogress.json,

06:07

que basicamente são essas colunas que ele acaba tendo. Então,

06:11

com isso, de forma geral, a gente acaba tendo uma árvore de arquivos.

06:16

que acaba ficando bem simples de forma geral e é um workflow, tá?

06:21

E novamente, tá? Eu criei isso aqui pra gente dar esses exemplos.

06:25

Cada dia a gente vai ver, por exemplo, o Cloud Code que agora ele cria workflows,

06:29

mas é muito mais pra trabalhar de uma forma multiagente e pra criar.

06:34

Muita interação entre agentes, você tem criadores de especificações também já hoje,

06:40

coisas muito parecidas com o que a gente colocou de forma automática.

06:44

Qual que é a grande vantagem e o porquê importante

06:47

de você aprender isso que eu estou te mostrando?

06:49

Porque quando você entende o racional do que está por

06:52

trás e como que isso aqui foi feito,

06:54

te dá mais bagagem para você não depender apenas de ferramentas prontas,

06:59

tá? E um ponto importante é... O contract.md,

07:03

ele muda muito o jogo em relação a tudo isso,

07:07

tá? Hoje em dia, você já consegue, por exemplo,

07:10

ter plugins que conseguem fazer a implementação e testar.

07:16

Mas esse teste não tem um contrato dessa forma como a gente colocou.

07:21

Você entende? Então,

07:22

tudo pode parecer igual até não ser, entendeu? Ou seja, ah,

07:27

esse cara implementa, o outro avalia. Mas como ele avalia?

07:31

Baseado em que ele avaliou? Em quais requisitos ele avaliou?

07:35

De onde vieram os critérios de aceitação? Você entende a diferença, galera?

07:40

E eu acho que isso que vai fazer uma

07:42

diferença gigante na sua carreira como desenvolvedor,

07:45

arquiteto e tudo mais.

07:47

Que é o nível de profundidade que

07:50

você consegue entrar em relação a planejar,

07:54

criar, pedir para desenvolver, testar.

07:57

Porque de forma geral é muito claro, implementar e testar, é o que aconteceu sempre.

08:02

Mas como testar? Hoje em dia isso não é trivial.

08:07

E a parte de harness é importante por quê?

08:09

Porque cada projeto eventualmente é testado de uma forma diferente.

08:13

Então não vai ter uma bola de prata que vai

08:16

dar um comando e vai resolver a sua vida.

08:18

Por isso que um contract.md ou algo parecido vai te ajudar nesses aspectos.

08:24

E novamente, esse workflow, esse fluxo, essa skill aqui que eu criei,

08:29

ela também não é bala de prata para todos os seus projetos.

08:32

Inclusive, esse projeto mesmo que a gente faz,

08:34

você vai perceber que a gente tem que parar

08:36

entre uma feature e outra para reavaliar,

08:40

ver se ele precisa de dados de input,

08:42

de assets estáticos que ele precisa trabalhar. Por quê?

08:47

Não existe mágica. O que existe é você ajustando o processo ao longo do tempo,

08:52

tá? E quando você começa a entender isso,

08:54

a mentalidade acaba trabalhando. A gente tem alguns perfis de desenvolvedores.

09:00

Tem aquele desenvolvedor que acha que pode desenvolver tudo num one shot e acabou.

09:05

E tem aquele desenvolvedor que é o cara que faz a babada de IA. Ele não programa...

09:10

Basicamente, a IA não programa. A IA vira um autocomplete ali pra ele.

09:17

Certo? A nossa ideia é a gente achar o momento onde grande

09:21

parte do desenvolvimento da IA vai fazer por horas e vai ficar programando,

09:24

mas a gente vai gastar tempo, sim, em melhorar o processo da IA.

09:28

E é por isso que essa parte de harness é tão importante. Fechou?

09:32

Então é isso aí, galera. Um grande abraço e vamos nessa.

## Resumo IA

**Abreviações**
*   **ID**: Identifier
*   **PR**: Pull Request (no contexto do GitHub)
*   **IA**: Inteligência Artificial
*   **.md**: Formato de arquivo Markdown
*   **.json**: Formato de arquivo JavaScript Object Notation

**Resumo**
A aula tem como objetivo principal trazer clareza sobre o conceito de orquestração, apresentando uma "skill" específica chamada "Implement Evaluate". Esta skill demonstra um workflow multiagente para automatizar a implementação e avaliação de features, com um forte foco em um "contrato" explícito.

O fluxo inicia com um **orquestrador** que planeja o ciclo, delega tarefas a subagentes, agrega seus resultados e decide os próximos passos. Para isso, utiliza artefatos de entrada como `contract.md`, `spec.md`, `plan.md` e um `prdprogress.json` para rastrear o progresso.

O **fluxo de execução** envolve:
1.  **Implementação da Feature:** Um agente executa a `implement feature`, que realiza a mudança, gera/atualiza testes e respeita o `contract.md`, gerando artefatos.
2.  **Avaliação:** O orquestrador envia os artefatos para um agente `evaluator`, que os verifica. O `evaluator` pode retornar os seguintes status:
    *   `ok`: Aprovado, o processo segue para conclusão.
    *   `fail`: Falha, encerra o processo ou solicita correção.
    *   `pending`: Requer reavaliação, geralmente devido a validação manual.
    *   `abortado`: Encerra completamente o processo devido a falhas críticas (ex: ambiente de teste não levantado, hard fails).
3.  **Correção:** Se o `evaluator` retornar `fail` ou `abortado`, ele solicita a intervenção de um subagente `fixrunner`. O `fixrunner` é um especialista em resolução de bugs com um "prompt" mais forte para essa finalidade, que prepara uma nova versão.
4.  **Ciclo Iterativo:** O `fixrunner` retorna a nova versão ao orquestrador, que a envia novamente ao `evaluator`, formando um ciclo com uma quantidade configurável de `retries`. O processo continua até ser aprovado (`ok`) ou esgotar as tentativas.

Ao final, se aprovado, o processo é concluído. O workflow gera diversos **artefatos de saída**, incluindo: um arquivo de orquestração (com `run ID` para rastrear ciclos), um report de avaliação (documentação, testes, como foi avaliado, screenshots via Playwright), um arquivo de lock (`orchestrate.loc`) para evitar concorrência, um journal persistido do orquestrador e, finalmente, pode criar uma Pull Request (PR) no GitHub. O `prdprogress.json` é atualizado para rastrear os status (iniciado, falhou, update, cycles, soft fails).

A aula conclui destacando que, embora ferramentas como Cloud Code possam criar workflows, o valor está em entender o racional por trás para não depender apenas de soluções prontas e em ajustar o processo continuamente, reconhecendo que não existem "balas de prata".

**Pontos de atenção**
*   **Diferença do Contrato:** A grande diferença deste workflow é a inclusão de um `contract.md`, que especifica os critérios de aceitação e como a avaliação deve ser feita, diferindo de soluções genéricas que podem apenas implementar e testar sem um contrato claro.
*   **Compreensão do Racional:** É fundamental entender o "porquê" e o "como" o workflow foi construído para obter mais bagagem e não depender exclusivamente de ferramentas prontas.
*   **Não é "Bala de Prata":** Este workflow, ou qualquer outro, não é uma solução universal para todos os projetos. É comum precisar de intervenção manual para reavaliar, fornecer dados de input ou assets estáticos entre features.
*   **Ajuste Contínuo do Processo:** Não existe mágica no desenvolvimento. O sucesso reside em ajustar o processo continuamente ao longo do tempo.
*   **Papel da IA no Desenvolvimento:** A Inteligência Artificial deve ser vista como uma ferramenta que pode automatizar grande parte do desenvolvimento por horas, mas os desenvolvedores ainda precisarão gastar tempo melhorando e ajustando o processo da IA, não apenas usando-a como um "autocomplete".
*   **Importância do Harness:** Cada projeto pode ser testado de forma diferente. Um "harness" (como o `contract.md`) é crucial para guiar os testes, pois não existe um comando único que resolva todos os problemas de teste.
*   **Controle de Concorrência:** O uso do arquivo `orchestrate.loc` é uma boa prática para evitar que várias instâncias rodem simultaneamente, minimizando problemas de concorrência.
*   **Múltiplos Status de Avaliação:** O `evaluator` fornece status detalhados (`ok`, `fail`, `pending`, `abortado`) que ajudam a entender o motivo de uma falha e a direcionar as próximas ações, seja para correção automática, validação manual ou encerramento por problemas críticos.