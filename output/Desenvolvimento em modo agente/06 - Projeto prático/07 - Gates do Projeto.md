Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17970)

## Resumo da aula

Gate determinístico é uma verificação automática que produz um resultado objetivo e repetível: passou ou falhou. Ele existe para validar regras que não dependem de interpretação do LLM nem de julgamento humano sobre “qualidade percebida” do código. Em um fluxo com agentes, isso cria uma fronteira operacional clara: alterações no projeto só são aceitas quando respeitam requisitos mínimos verificáveis por script.

O projeto precisa reagir às mudanças que recebe, porque gerar código, alterar arquivos e implementar funcionalidades aumenta o risco de regressão estrutural e comportamental. Os gates funcionam como mecanismos internos de validação que confirmam se a alteração ainda respeita contratos, limites arquiteturais e critérios de qualidade. Essa camada não substitui revisão humana, mas reduz o espaço de erro objetivo e evita gastar tokens tentando redescobrir problemas que já podem ser detectados localmente.

Retomando o uso de scripts no harness, o TSC entra como a verificação mais básica da cadeia. Ele valida o código do ponto de vista de tipos sem exigir build completo, detectando incompatibilidades entre interfaces, implementações e contratos entre camadas. Quando esse gate falha, o problema já está suficientemente concreto para correção imediata, sem depender de análise subjetiva.

O ESLint não serve apenas para estilo; aqui ele é configurado como mecanismo disciplinador de consistência. Ao tratar warning como falha, o projeto impede pequenos desvios que, acumulados, degradam a base de código e confundem o agente sobre o padrão esperado. Essa rigidez é útil em ambientes assistidos por IA porque transforma convenções em restrições executáveis.

Lembra das regras de dependência entre domínio, aplicação, mundo externo e composition root já definidas anteriormente? O Dependency Cruiser aplica essas regras no nível das importações, verificando se uma camada passou a depender de outra de forma indevida. Isso cobre um tipo de quebra que frequentemente não aparece na compilação: o sistema continua funcionando, mas a arquitetura já foi violada.

Nem toda regra arquitetural pode ser expressa apenas como “quem importa quem”. Um script customizado como Check Architecture, escrito em TypeScript, permite validar restrições particulares do projeto, como limitar o uso de process.env a env.ts, concentrar o composition root em main.ts ou proibir try-catch direto em handlers. Esse tipo de gate captura convenções locais que ferramentas genéricas não conhecem.

Compilação, lint e arquitetura validam estrutura; testes validam comportamento. Eles confirmam que o que já existia continua funcionando e que a implementação nova atende ao que foi definido, mesmo quando o restante da cadeia estrutural está verde. Em fluxos com agentes, isso evita aceitar código formalmente correto, mas funcionalmente errado.

O Knip procura resíduos comuns de iteração: exports não usados, arquivos órfãos, dependências obsoletas e tipos sem referência. Esse problema tende a crescer quando o agente explora uma abordagem, abandona parte dela e deixa sobras no repositório. Transformar esse diagnóstico em gate mantém a base mais enxuta e reduz ruído para futuras gerações de código.

Em vez de exigir que cada verificação seja executada manualmente, o projeto centraliza a sequência em um script como runGate.mjs. Esse ponto único de entrada padroniza a ordem de execução, simplifica a rotina do desenvolvedor e torna o processo explícito para o harness. A centralização também facilita plugar o mesmo fluxo em automações locais, CI e execução pelo agente.

Quando o agente implementa uma feature e executa os gates, a falha deixa de ser abstrata e vira um erro concreto retornado por uma ferramenta específica. Esse retorno orienta a próxima correção com muito mais precisão do que um prompt genérico pedindo “melhore o código”. O gate, portanto, não apenas bloqueia; ele fecha um ciclo de feedback determinístico que ajuda o agente a convergir com menos custo.

## Transcrição

00:00

Bom, pessoal, e antes de a gente seguir, eu quero falar sobre gates, né?

00:05

E a primeira camada onde a gente vai

00:08

colocar esses gates no nosso projeto aí do Videomax,

00:12

tá? Primeiro ponto que eu já falei pra vocês,

00:15

gates, nesses casos, eles são determinísticos, tá? Então,

00:19

a ideia aqui é a gente conseguir, de forma geral,

00:23

de forma bem objetiva, saber que, ao executar... um script no nosso projeto,

00:29

a gente consegue garantir que algumas falhas ele não vai corrigir. Então,

00:35

vamos pensar que daqui para frente a gente está falando sempre uma palavra-chave, que é...

00:40

Ou seja, resolver um problema que dá para resolver de forma objetiva,

00:45

sem depender ali do LLM.

00:47

Então, não é uma análise subjetiva, tipo, acho que o código ficou bom.

00:51

Parece que está dentro do padrão.

00:53

O gate precisa rodar e desenvolver um resultado claro. Ou seja,

00:57

ou passou ou falhou. E isso é muito importante no cenário,

01:00

porque a gente vai mexer no projeto,

01:03

a gente vai criar código, a gente vai alterar arquivo,

01:06

a gente vai implementar um monte de funcionalidade. E só que, depois disso,

01:11

o próprio projeto precisa ter alguns mecanismos para dizer se

01:16

aquela alteração ainda respeita aqueles requisitos mínimos que a gente espera.

01:21

Então, no nosso caso do Videomax,

01:23

a gente vai trabalhar com gates determinísticos. Então, na realidade...

01:28

a gente não vai depender de opinião nenhuma. Ou seja,

01:31

os gates sempre vão rodar ali do mesmo jeito.

01:34

Então, a gente tem coisas do tipo, se o TypeScript não compila,

01:38

falhou. Se o lint não encontrou, se ele teve um warning ali no lint,

01:42

por exemplo, ele falhou.

01:44

Se uma camada acessou uma dependência que não deveria, vai falhar.

01:48

Se um script arquitetural encontrou uma regra quebrada, também.

01:51

Se os testes não passarem, vai falhar.

01:53

Se encontrou um código morto ali que não está servindo para nada no projeto,

01:57

ninguém está importando ele, ele não está importando ninguém,

01:59

também a gente pode falhar ou a gente pode colocar isso como uma

02:03

melhoria e daí vai depender muito de como que a gente quer trabalhar. Então,

02:09

Falando especificamente dos gates do Videomax,

02:12

a gente vai ter o nosso primeiro gate, que é o famoso TSC.

02:16

A ideia aqui é rodar verificação de tipo sem a necessidade de fazer um build,

02:21

ou seja, a gente quer saber se o código compila do ponto de vista dos tipos,

02:25

sem nenhum erro de contrato, se alguma camada está quebrada,

02:28

se alguma interface deixou de bater ali com a implementação.

02:31

Então esse é o gate mais básico de todo mundo.

02:34

Opa, todo mundo já faz TSC, não tem problema.

02:37

Faz parte de um gate, legal?

02:39

Outro ponto aqui é o ESLint, tá? Aqui a gente entra com o estilo,

02:44

a qualidade e a consistência do código, mas no nosso caso,

02:47

o ponto mais importante é que ele vai rodar com tolerância zero ao warnings, ou seja,

02:53

não é aquela ideia de, ah, tem uns warnings e depois a gente vê.

02:56

Não, aqui a gente consegue fazer quebrar o gate.

02:58

Isso aí é importante para que os projetos ali com os agentes,

03:02

né, eles comecem a saber que quando... tem um warning,

03:07

Ele vai começando aos poucos a ter desvios e quando a gente vê o projeto,

03:11

ele já descambou,

03:13

né? Então a ideia é a gente conseguir seguir de

03:16

forma bem estrita ali no meio do caso, tá?

03:19

Terceiro gate que nós vamos ter aí,

03:21

Dependency Cruiser, tá? Basicamente é o Dep Cruiser.

03:25

Esse é um dos caras mais importantes na nossa arquitetura,

03:27

na realidade, pelo menos na minha opinião.

03:29

Como o nosso back-end está seguindo muito a Clean Architecture,

03:32

a gente precisa proteger as fronteiras, vamos dizer assim, entre as camadas.

03:37

Ou seja, o domínio não pode depender da infraestrutura.

03:39

O use case não deve importar o detalhe externo de forma indevida.

03:43

A camada de infra não pode começar a vazar para onde ela não deveria. Então,

03:48

esse tipo de problema muitas vezes não aparece como erro de compilação.

03:52

O código pode estar até compilando e funcionando,

03:55

mas a arquitetura já foi quebrada. Por isso,

03:58

esse Dependency Cruiser vai ajudar a gente como uma

04:01

espécie de guardião das dependências entre os módulos.

04:04

Então, ele vai verificar se as importações estão

04:07

respeitando as regras que a gente definiu. Então,

04:11

se alguém ou a gente tentar fazer uma camada depender de outra de forma errada,

04:16

esse gate vai apontar ali logo o problema.

04:19

O quarto gate é um gate customizado de arquitetura, tá? Então, esse aí,

04:24

ele é um script próprio do próprio projeto que ele é feito em TypeScript,

04:29

tá? Ele vai se chamar ali Check Architecture.

04:31

E por que a gente precisa desse script customizado?

04:35

Já que a gente tem, vamos dizer ali, o Dependency Cruiser, né? Na realidade,

04:39

é porque já existem regras que são muito específicas para o nosso projeto.

04:44

Algumas regras, elas não são apenas de quem importa quem.

04:47

Às vezes a gente vai querer garantir que o process .env,

04:51

por exemplo, só seja usado em um arquivo específico,

04:54

como o env.ts.

04:56

Ou a gente quer garantir que o composition

04:58

root esteja concentrado em um lugar específico,

05:02

como o main.ts.

05:03

Ou ainda a gente quer impedir que certos padrões, como handlers,

05:08

tenham try-catch diretamente quando isso devia ser, por exemplo,

05:13

tratado de outra forma no projeto. Essas regras são particulares do projeto. Então,

05:19

isso aí só faz sentido a gente ter um script nosso.

05:22

E isso eu recomendo, inclusive, para você nos seus projetos.

05:25

Comece a perceber peculiaridades que o projeto que você tem,

05:29

que você gostaria de reforçar essas regras e

05:32

não algum script um pouco mais genérico.

05:35

A gente também tem o quinto gate aqui,

05:37

que são os testes automatizados, e a ideia é simples,

05:40

depois que o agente implementa uma coisa,

05:42

o projeto precisa conseguir validar o comportamento,

05:45

não apenas o lint e a arquitetura.

05:47

Os testes entram para verificar se o que já existia continua funcionando,

05:53

se as partes novas têm algum nível de cobertura dentro do que foi definido.

05:57

Esse gate também é importante porque muitos

06:00

problemas não aparecem somente na parte estrutural.

06:04

Às vezes a arquitetura está certa, o código compila,

06:07

o link passa, mas o comportamento está errado,

06:09

então o teste vai ajudar bastante com isso. A gente tem também o sexto gate ali,

06:13

que é o NIP. O NIP vai procurar código morto no projeto. Então isso inclui o quê?

06:18

export que não foi utilizado, arquivos que ficam sobrando,

06:22

dependências que não estão sendo mais usadas, os tipos que foram criados,

06:26

mas não são referenciados por ninguém.

06:28

Esse gate é bem útil no fluxo. Onde que os agentes,

06:32

né, eles começam a tentar desenvolver em determinada abordagem,

06:36

eles criam alguns arquivos,

06:38

depois as coisas mudam de caminho e a gente começa a ficar

06:42

com aquele monte de resto de código morto no projeto.

06:44

Não sei se você já passou por isso, eu já passei e mesmo assim,

06:47

às vezes, a gente acaba pegando um monte desses tipos de código ainda,

06:51

principalmente nesses dias de hoje, tá? Então,

06:54

o NIP vem aí para ajudar e deixar o nosso projeto mais enxuto.

06:58

Então, se você perceber, esses gates têm naturezas diferentes.

07:03

Alguns olham para compilação, outros olham para código, outros olham para arquitetura,

07:07

outros olham para comportamento, outros olham para código morto.

07:11

E quando você pega essa combinação,

07:13

a gente começa a ter uma camada interessante de proteção.

07:16

E para não deixar isso espalhado, o que a gente faz?

07:19

A gente acaba tendo um script único,

07:21

que quando a gente executa lá, sei lá, um runGate .mjs, o que vai acontecer?

07:27

Ele simplesmente vai rodar tudo isso. Então,

07:31

é uma função que acaba orquestrando todos esses gates em sequência.

07:36

Então, ao invés de eu depender de...

07:38

lembrar todos os comandos, a gente ter um ponto, a ideia é você ter,

07:43

no final das contas, um ponto único de entrada.

07:46

Então, rodou o run gates, ele executa tudo na ordem que a gente colocou.

07:50

E para a gente, como desenvolvedor,

07:51

facilita bastante a rotina, e para a gente,

07:54

deixa esse processo completamente mais explícito.

07:56

E é aqui que entra um detalhe mega relevante para

07:59

o fluxo que a gente vai construir depois.

08:01

Porque esses gates, eles também podem ser usados pelos agentes como feedback.

08:06

Por exemplo, eu implemento uma feature com o RunGate,

08:09

ele falha e ele passa a ter um erro concreto para corrigir.

08:12

Então, basicamente, olha,

08:14

deu erro aqui. Quando ele vê que deu erro,

08:17

ele sabe qual o erro que o gate retornou e ele já consegue,

08:21

baseado nesse erro, corrigir a aplicação. Então, isso aí é importante,

08:25

porque os gates, eles não só bloqueiam, os gates,

08:29

o que eles fazem, eles também dão feedbacks ali pelo agente.

08:32

Então, isso aí também é importante pra gente trabalhar, tá?

08:36

Obviamente... que isso aí não vai resolver tudo, tá?

08:40

Não vai substituir a gente revisar código ou coisas desse tipo.

08:43

Muitas vezes substitui, tá? Mas, de forma geral,

08:46

É uma camada fundamental para harness,

08:49

Tá? Então, eu acredito que muitos de vocês,

08:53

Talvez na hora que estejam vendo esse vídeo,

08:54

Já têm alguns gates e etc., mas saiba que isso aí é harness puro.

09:00

Porque você realmente vai tentar manter o agente dentro daquele

09:04

quadradinho para que quando um código seja gerado,

09:06

Algumas decisões mínimas você vai conseguir ter e de forma novamente determinística.

09:12

Você evita gastar um monte de tokens e ainda assim você

09:17

garante que algumas regras claras aí não estão sendo ali quebradas.

09:21

Fechou? Então vamos nessa aí para o nosso próximo vídeo.

## Resumo IA

**Abreviações**
*   **CI**: Continuous Integration
*   **LLM**: Large Language Model
*   **TSC**: TypeScript Compiler

**Resumo**
O objetivo desta aula é apresentar os "gates determinísticos" como mecanismos de verificação automática que produzem resultados objetivos e repetíveis (passou ou falhou). Esses gates são essenciais para validar regras que não dependem da interpretação de um LLM ou de julgamento humano subjetivo, estabelecendo uma fronteira operacional clara onde alterações no projeto só são aceitas se respeitarem requisitos mínimos verificáveis por script.

O instrutor explicou que, em um fluxo de desenvolvimento assistido por agentes de IA, gerar e alterar código aumenta o risco de regressão estrutural e comportamental. Os gates atuam como mecanismos internos de validação para confirmar se as alterações mantêm contratos, limites arquiteturais e critérios de qualidade. Essa camada de validação complementa a revisão humana, minimizando erros objetivos e otimizando o uso de tokens por evitar que agentes tentem redescobrir problemas já detectáveis localmente.

Foram abordados diversos gates específicos e suas funções:
*   **TSC (TypeScript Compiler)**: O gate mais básico, que valida o código do ponto de vista de tipos, detectando incompatibilidades entre interfaces, implementações e contratos sem a necessidade de um build completo. Uma falha aqui indica um problema concreto para correção imediata.
*   **ESLint**: Configurado para atuar como um mecanismo disciplinador de consistência. Ao tratar warnings como falhas, o projeto impede pequenos desvios que, acumulados, degradam a base de código e podem confundir o agente sobre o padrão esperado, transformando convenções em restrições executáveis.
*   **Dependency Cruiser**: Aplica regras de dependência arquitetural (como entre domínio, aplicação e infraestrutura) no nível das importações, verificando se uma camada depende indevidamente de outra. Ele captura violações arquiteturais que podem não ser detectadas por erros de compilação.
*   **Check Architecture (Script Customizado)**: Um script customizado em TypeScript que valida restrições arquiteturais muito específicas do projeto, como limitar o uso de `process.env` a `env.ts`, concentrar o *composition root* em `main.ts` ou proibir `try-catch` direto em *handlers*, cobrindo convenções locais que ferramentas genéricas não conhecem.
*   **Testes Automatizados**: Validam o comportamento do sistema. Confirmam que o que já existia continua funcionando e que as novas implementações atendem às definições, prevenindo que código formalmente correto seja funcionalmente errado.
*   **Knip**: Procura por resíduos comuns de iteração de código, como exports não utilizados, arquivos órfãos, dependências obsoletas e tipos sem referência. Essencial para manter a base de código enxuta e reduzir ruído, especialmente quando agentes exploram e abandonam abordagens, deixando "código morto".

O fluxo explicado envolve a centralização da execução de todos esses gates em um único script, como `runGate.mjs`. Esse ponto de entrada padroniza a ordem de execução, simplifica a rotina do desenvolvedor e torna o processo explícito para o *harness* e automações locais ou de CI. Quando um agente implementa uma *feature* e os gates falham, o erro concreto retornado por uma ferramenta específica oferece um feedback muito mais preciso do que um prompt genérico, orientando a correção e fechando um ciclo de feedback determinístico que ajuda o agente a convergir com menor custo.

**Pontos de atenção**
*   **Natureza Determinística dos Gates**: Os gates devem produzir resultados objetivos e repetíveis (passou/falhou), sem depender de interpretação subjetiva de LLMs ou de julgamento humano sobre qualidade percebida.
*   **Tolerância Zero para Warnings**: Configure ferramentas como ESLint para tratar warnings como falhas, garantindo a consistência do código e prevenindo pequenos desvios que podem degradar a base ao longo do tempo. Essa rigidez é crucial em ambientes assistidos por IA.
*   **Proteção Arquitetural Aprofundada**: Utilize ferramentas como Dependency Cruiser para proteger as fronteiras entre as camadas arquiteturais. Muitas violações arquiteturais não geram erros de compilação, mas comprometem a estrutura do sistema.
*   **Customização para Regras Específicas**: Ferramentas genéricas não cobrem todas as particularidades de um projeto. Desenvolva scripts customizados (e.g., em TypeScript) para validar restrições arquiteturais e convenções únicas do seu projeto.
*   **Validação Comportamental Essencial**: Não se limite a validações estruturais (compilação, lint, arquitetura). Testes automatizados são fundamentais para garantir que o comportamento do código esteja correto, evitando que código formalmente válido seja funcionalmente incorreto.
*   **Gestão de Código Morto**: Implemente gates como o Knip para identificar e remover exports não utilizados, arquivos órfãos, dependências obsoletas e tipos sem referência. Isso é especialmente importante em fluxos com agentes de IA, que podem gerar e abandonar partes de código.
*   **Centralização da Execução dos Gates**: Utilize um único script (e.g., `runGate.mjs`) para orquestrar e sequenciar a execução de todos os gates. Isso padroniza o processo, simplifica o trabalho do desenvolvedor e facilita a integração em *harness*, CI e automações locais.
*   **Feedback Concreto para Agentes**: Os gates funcionam não apenas como bloqueadores, mas também como mecanismos de feedback determinísticos. Erros concretos de ferramentas específicas orientam o agente de IA com muito mais precisão do que *prompts* genéricos, reduzindo o custo de convergência.
*   **Complementaridade à Revisão Humana**: Os gates não substituem a revisão humana, mas reduzem drasticamente o espaço para erros objetivos e evitam o gasto de tokens em problemas que podem ser detectados localmente, liberando a revisão humana para questões de maior complexidade e design.