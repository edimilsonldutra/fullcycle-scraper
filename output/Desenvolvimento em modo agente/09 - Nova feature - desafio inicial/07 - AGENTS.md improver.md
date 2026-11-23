Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17995)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, uma outra coisa aqui interessante, somente para a gente lembrar,

00:05

ele implementou a feature número 3,

00:07

e aqui nessa feature número 3, ele tem aqui o EVOL,

00:12

o processo de EVOL, e aqui ele tem basicamente os screenshots.

00:15

Então, se eu clicar aqui,

00:17

ele tem cada screenshot de cada parte dos testes e dos itens,

00:22

dos critérios de aceitação que ele precisava cumprir. Então,

00:27

é interessante porque ele gera esses artefatos,

00:30

obviamente, caso você queira.

00:31

E aqui ele tem o relatório dele de como que foi feito e etc.

00:36

O que foi feito, avaliado e etc. Os quality gates,

00:40

o que passou, persistent state e etc.

00:42

Com certeza foi importante aquele state que a gente passou dos arquivos,

00:47

como se diz,

00:49

daquele script para ele conseguir passar. Porque se você olhar aqui,

00:53

ele conseguiu passar no teste...

00:57

De... deixa eu ver, tem um teste rejeitado. Cadê? Aqui, ó.

01:07

Aqui, ó. O tamanho do arquivo.

01:09

Então ele conseguiu pegar esse teste aqui na interface gráfica.

01:13

Então não foi só no back-end. Então pra gente isso é importante, tá?

01:17

Agora, tem alguns pontos interessantes no meio dessa história, galera, que é o seguinte.

01:22

Deixa eu... eu tô fechando um monte de arquivo aqui que ficou aberto.

01:26

Mas eu acho que o ponto mais importante de toda essa história aqui é o seguinte,

01:32

o que a gente pôde aprender com o que aconteceu?

01:36

Então, uma dica que eu dou, que você pode fazer de uma forma mais simples é,

01:41

acabou qual da sessão que você acha que é importante,

01:44

ou quando você está ali e você está vendo a Iá apanhar,

01:47

ou você para a sessão e pergunta, por que você está sofrendo nesse momento?

01:52

E ela pode falar o problema e você ajuda e depois pede para ela colocar no Cloud MD.

01:57

No nosso caso aqui, existe um plugin da Anthropic nesse caso,

02:03

quem está usando o Cloud Code, mas é um plugin auxiliar,

02:08

tá? Isso que eu estou dizendo.

02:10

O importante é você entender o que você tem que fazer.

02:12

Por isso que eu estou dizendo, eu não quero ficar aqui só preso à ferramenta,

02:15

que eu estou usando uma ferramenta, eu vou usar os recursos que ela tem.

02:18

Mas se eu for aqui em plugins, existe um plugin aqui,

02:20

se você olhar aqui que está instalado, que é, deixa

02:28

eu achar aqui, tem

02:32

o Superpowers, que é interessante, mas eu queria achar o do nosso camarada, o

02:40

do aqui, Cloud MD Management. Então você pode instalar esse plugin aqui,

02:44

ele é interessante e eu queria mostrar.

02:47

Aqui nesse caso, o que pode acontecer no nosso caso Cloud MD Management?

02:52

Vou colocar Cloud MD Improver, ele tem aqui,

02:54

e ele tem uma revisão aqui nesse cara, tá?

02:58

Então esse cara, ele atualiza o seu Cloud MD,

03:01

aprendendo a partir dessa sessão, tá? Então nesse nosso caso,

03:07

essa nossa sessão está vazia, então ele não vai aprender nada, tá?

03:10

Mas eu vou colocar nesse caso aqui o Improver,

03:13

somente para ver o que ele traz aqui para a gente.

03:16

Então lembra que eu falei, pergunta pra ele o que ele aprendeu nessa sessão?

03:20

Nesse caso aqui, a Anthropic ela fez um basicamente, é um prompt provavelmente,

03:26

que ela roda e na hora que ela roda ela

03:30

tenta entender o que ela aprendeu que poderia...

03:33

ser utilizado para bugs futuros.

03:35

Mas você pode fazer isso de forma manual ou criar uma skill para fazer isso.

03:38

Existem diversas skills.

03:40

Então, o grande ponto que eu quero que você entenda são os conceitos.

03:45

Nesse momento, o que ela está fazendo aqui? Ela está analisando o meu código,

03:49

analisando o CloudMD, né? E aí, baseado nisso,

03:54

ela vai ver o que tem de erro ou melhoria que eu poderia colocar.

03:58

Agora tem um ponto importante que eu quero dizer aqui para vocês.

04:01

Eu já testei bastante esses caras,

04:02

diversos na realidade, e você não tem que fazer isso de forma cega, tá?

04:08

Não é porque ela está sugerindo aquilo que você tem

04:11

que necessariamente concordar com aquilo que ela está falando,

04:14

tá? Então, seja muito criterioso, porque esses caras,

04:20

às vezes, eles tendem a ser muito verbosos.

04:23

e deixar o arquivo muito grande. O nosso arquivo já está meio que grande,

04:27

entendeu? Então, nesse aspecto, a gente tem que tomar ali cuidado.

04:32

Então, ela trouxe aqui, ela gerou um score,

04:36

está falando que o nosso código aqui está com grade B agora,

04:39

com vários problemas, provavelmente scores e etc.

04:44

Então, aqui ela gerou critérios e o score do que está ruim e o que está bom.

04:49

Primeira coisa que ela falou que está ruim,

04:51

os comandos workflow. O init stop gates está documentado.

04:53

Está missing o run gates shortcut, que é npm run gates,

04:59

ok. E o npm test não está colocado.

05:04

E aí eu já tenho, como que eu posso dizer?

05:08

Eu já tenho ali a minha questão.

05:11

Cara, será que eu preciso colocar um npm test no meio da história?

05:15

O log file locations é interessante. E o health endpoint.

05:20

Eu não acho interessante a gente ter no cloud,

05:23

no momento que a gente está do nosso projeto,

05:25

inclusive. Entendeu? Então, isso aí, para mim,

05:28

não é importante. Então, esse cara. Arquitetura. Mono repo, back-end, etc.

05:34

Deixa eu ver aqui, então, o que ela trouxe e as recomendações.

05:39

Tem erro de typo aqui, provavelmente.

05:41

ESLint, na realidade.

05:45

Opcional, colocar o run gates para conveniência.

05:48

E aqui ela traz meio que como se fosse um diff, né?

05:51

Então, você pode usar o Run Gates para rodar todos de uma vez.

05:57

E ela fez o ajuste aqui do ESLint, beleza?

06:00

E também adicionou um cara que

06:05

eu tinha esquecido em relação ao Quality Check aqui.

06:09

Ela botou o TSC, o ESLint, o Deep Cruise aqui para a gente.

06:14

Beleza, isso aqui é um ajuste. Edit B.

06:17

Aqui ó, make the full part discoverable after login online.

06:21

Então ela coloca assim ó,

06:22

ports allocated dynamically, web from 3000, backend from 4000,

06:26

find a new live URLs com init.sh, ready, output.

06:32

Então, aí que é o grande ponto, galera,

06:34

Tá vendo? Ele deixou realmente o mais descritivo isso aqui, se você perceber.

06:39

Mas, eu não acho, honestamente,

06:44

que eu preciso colocar tudo isso. Se você perceber,

06:47

a gente não teve esse problema. Então, se eu não tive esse problema,

06:50

somente com os dados que eu coloquei foram suficientes,

06:52

então eu estou feliz, eu não vou colocar.

06:54

Sobre os logs, eu acho interessante colocar.

06:58

Eu acabei não colocando. Isso aqui é algo interessante.

07:03

Então, eu vou aqui no meu agents.md e

07:08

aqui a gente tem a parte dos logs que ele tinha falado aqui,

07:14

né? Então, em relação à parte de logs.

07:20

Logs nesse cara aqui.

07:23

Outra coisa, o nosso erro de typo, né? Tava R list,

07:29

né? E é o seguinte, o must use wrapper, etc.

07:34

Esse cara aqui e o must use esse

07:42

cara aqui pra gente, tá?

07:45

Wesley, por que você não tá fazendo isso junto com o IA? Eu poderia estar fazendo, tá?

07:48

É que eu tô querendo explicar e a gente ler e fazer isso junto aqui.

07:54

Então, ele trouxe essas recomendações.

07:57

E aqui tem outras melhorias que ele está trazendo. O wrong gate. Vamos olhar aqui.

08:10

Aqui, recomendações.

08:16

É isso aqui. Não teve muita recomendação forte.

08:21

Se você olhar bem aqui, grande parte do GIF dele que ele colocou,

08:25

a parte do log, a parte das portas, a parte do gate que eu ajustei.

08:33

Foi mais nesse foco aqui que ele acabou colocando. Então, assim,

08:36

eu tô contente por enquanto com o nosso camarada. Ele tá dando uma nota razoável.

08:42

Eu não concordo com tudo que ele colocou e por isso que eu vou seguir.

08:45

Provavelmente eu vou manter uma nota mais baixa ali com ele.

08:48

Mas ali tem, basicamente, pra gente ter uma noção de como que isso funciona.

08:54

Mas eu acho que o ponto principal aqui, galera, é eu trazer sempre pra você.

08:59

A cada iteração, a cada feature, a cada coisa que acontecer,

09:01

revisa esse cara. Esse cara, ele é o guia, ele, vamos dizer,

09:07

é o treinador do próximo funcionário que vai entrar

09:11

em relação à parte de IA ali na sua empresa.

09:14

Ou seja, o próximo agente, a próxima iteração que a gente acontecer,

09:17

esse cara, ele vai aprendendo. Então, esses tipos de plugin ajudam bastante,

09:22

tá? Mas lembre-se, né? Toda vez que você estiver desenvolvendo...

09:27

Dá para aprender no meio de todas essas sessões e tudo mais.

09:32

Beleza? Então, somente para lembrar,

09:34

fazendo atualizações aí do nosso cloud. E como eu sou uma pessoa extremamente,

09:39

extremamente, como que eu posso dizer, by the book,

09:47

eu estou fazendo o commit direto na main aqui. Olha que maravilha. Sem pull request.

09:52

Mas... Dá para você entender, né, galera? Colocando aqui mesmo, não tem problema.

09:56

Nossos próximos passos daí seriam a gente ir para as outras features,

10:01

para a gente fazer ali e começar a rodar isso em paralelo.

10:04

Mas daí é uma próxima etapa,

10:06

porque a gente vai falar de um outro processo

10:09

de orquestração de features sendo desenvolvidas simultaneamente ali por subagentes.

10:14

Fechou? Então é isso por esse capítulo, galera. Um abraço.

## Resumo IA

**Abreviações**
*   **EVOL**: Processo de Avaliação (relacionado à implementação de features, testes e geração de artefatos).
*   **IA**: Inteligência Artificial.
*   **Cloud MD**: Cloud Markdown (documentação ou arquivo de configuração, geralmente em formato Markdown, mantido e atualizado em ambiente de nuvem).
*   **npm**: Node Package Manager.
*   **ESLint**: ECMA Script Linter.
*   **TSC**: TypeScript Compiler.
*   **Diff**: Diferença (representação de mudanças entre arquivos).

**Resumo**
A aula revisa a implementação da Feature 3, destacando o processo de EVOL com a geração de artefatos como screenshots e relatórios de testes que comprovam o cumprimento dos critérios de aceitação. É ressaltada a importância de scripts de estado persistente para garantir a passagem de testes, tanto de back-end quanto de interface gráfica.

O foco principal da aula, no entanto, é a integração e o uso crítico de ferramentas de Inteligência Artificial para aprimorar o processo de desenvolvimento e a documentação. O instrutor demonstra como plugins de IA, como o "Cloud MD Improver" (da Anthropic, integrado ao Cloud Code), podem analisar sessões de desenvolvimento e o código-fonte para automaticamente atualizar um arquivo "Cloud MD" (que serve como documentação viva do projeto), aprendendo com as interações e sugerindo melhorias para prevenir bugs futuros.

Durante a demonstração, a IA analisa o projeto, atribui uma nota (ex: Grade B) e gera recomendações. Essas sugestões incluem a adição de comandos de workflow (como `npm run gates` ou `npm test`), documentação de localizações de logs, configurações de portas e inclusão de ferramentas de qualidade de código (como `TSC`, `ESLint`, `Deep Cruise`). O instrutor, então, exemplifica a revisão manual dessas sugestões, aceitando as que agregam valor real ao projeto (como correções de typos e adição de checks de qualidade) e rejeitando outras que considera desnecessariamente verbosas ou não alinhadas com as necessidades atuais do projeto (como a documentação de um health endpoint ou detalhes excessivos de portas se não houve problema). O fluxo explicado enfatiza a iteração contínua e a manutenção do Cloud MD como um guia essencial e uma ferramenta de treinamento para futuros agentes de IA ou novos membros da equipe.

**Pontos de atenção**
*   **Compreensão Conceitual vs. Ferramenta**: O mais importante é entender o conceito do que se precisa fazer, e não se prender apenas à ferramenta específica utilizada. As ferramentas são meios para atingir um fim.
*   **Revisão Crítica das Sugestões da IA**: Não se deve aceitar as sugestões da IA de forma cega. É fundamental ser criterioso, pois as IAs podem gerar recomendações excessivamente verbosas ou que não se aplicam à realidade do projeto, tornando a documentação desnecessariamente grande e complexa.
*   **Cloud MD como Guia e Treinador Vivo**: O arquivo Cloud MD (ou documentação equivalente) deve ser constantemente revisado e atualizado a cada iteração ou nova feature. Ele serve como um guia essencial para o projeto e funciona como um "treinador" para o próximo agente de IA ou novo desenvolvedor que integrar a equipe, permitindo o aprendizado contínuo.
*   **Importância do Estado Persistente**: A utilização de scripts para manter e restaurar o estado persistente do ambiente é crucial para garantir que os testes (inclusive de interface gráfica) possam ser executados e passados com sucesso.
*   **Intervenção Humana na Dificuldade da IA**: Se a IA estiver com dificuldades durante uma sessão de desenvolvimento, é uma boa prática pausar, perguntar à ela o motivo do problema e, com base na resposta, ajudar a solucionar e registrar o aprendizado no Cloud MD.