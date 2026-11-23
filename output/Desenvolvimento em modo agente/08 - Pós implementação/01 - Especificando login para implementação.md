Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17983)

## Resumo da aula



## Transcrição

00:01

Bom, pessoal, no vídeo anterior, o que acontece?

00:04

Nós fizemos o quê? Nós geramos uma especificação,

00:08

depois a gente pediu para fazer uma implementação, e depois dessa implementação,

00:12

a gente pediu para ter uma avaliação, ou seja,

00:16

para ter uma avaliação para ver se tudo deu certo.

00:18

Agora, a nossa história vai ser um pouquinho mais,

00:21

entre aspas, automática. E o que é automática?

00:25

Eu vou gerar a feature normalmente com o Spec Writer.

00:28

Mas depois, a nossa intenção aqui vai ser utilizar uma outra skill,

00:33

que é o nosso Implement and Evaluate,

00:37

tá? Aí nesse caso, a gente tem uma espécie de um orquestrador,

00:41

não é bem um orquestrador,

00:42

mas basicamente a gente vai fazer a implementação e depois disso

00:47

vai chamar um outro agente para fazer a avaliação no mesmo ciclo.

00:51

Sem que eu tenha que iniciar novamente. Ou seja,

00:54

ele vai chamar um outro agente naquele momento de avaliação,

00:58

tá? Mas, para a gente começar todo esse processo,

01:01

o que eu tenho que fazer? Eu tenho que gerar a implementação,

01:04

gerar uma feature. Então, eu vou colocar aqui, barra, Spec Writer, tá?

01:11

Vou colocar o meu PRD e vou colocar aqui a minha feature 02, aqui para mim.

01:17

E aqui... ele vai ter que começar a fazer todo aquele processo de especificação,

01:22

demora um pouquinho, então vou dar um pause aqui somente para você saber,

01:26

e aí a gente volta em seguida.

01:29

E pronto, pessoal, depois de um tempinho, ele gerou aqui a nossa segunda etapa,

01:36

que é o sistema de autenticação. Então ele gerou aqui o spec,

01:40

o plan e o contract.md aqui.

01:43

Então se eu clicar agora aqui no meu querido F02, eu vou ver aqui.

01:49

A minha especificação, deixa eu jogar esse cara aqui de lado, vamos

01:54

ver, onde eu tenho a especificação do meu sistema de autenticação, né?

01:58

Ele tá falando de back-end agora, então eu vou ter a back-end domain user,

02:04

user ID como objeto velho, e-mail pra normalizar, password, ou seja,

02:10

agora aqui ele tá indo mais pra aquele lado TDD-like, né? Ou seja...

02:15

muito mais focado em TDD, não, DDD-like com Clean Architecture,

02:19

tá? Ele tá até restritivo demais,

02:21

né? Ou seja, fazer com que o User ID seja um objeto velho.

02:25

Normalmente eu não sou tão purista dessa forma,

02:27

mas o nosso ponto é que a gente pode ajustar a skill,

02:31

né? Então ele colocou aqui o que vai precisar.

02:33

Aqui tem o plano de ação, né? Então os pré-requisitos pra rodar.

02:39

E aí o estágio 1, estágio 2, estágio 3, ele vai até 7.

02:45

8, 9, as tarefas, né? Então estágio 4,

02:48

onde ele entra nas páginas web, basicamente, aqui, né?

02:52

Depois estágio 5 é a verificação dele. Então, tá aqui feito,

02:57

e agora a gente tem um ponto mais importante,

02:59

vamos dizer, né? Que são as novidades do que a gente tá falando aqui de Harness,

03:03

que é em relação à parte de, do contrato, né?

03:07

Então, aqui no contrato, eu tenho o meu...

03:12

Runtime Services, então, o que ele vai imaginar?

03:14

Que ele vai precisar de um Fastify Service,

03:16

ele vai precisar de um Next.js, ele vai precisar do Postgres, e para persistir,

03:22

Ele vai precisar de um usuário Alice, com User, com Name Alice, com e-mail esse.

03:27

Então, ele cria, se você perceber,

03:29

o que ele vai precisar como dado.

03:36

Para ele iniciar o processo de teste, inclusive. Então,

03:39

quando um evaluator for rodar esse cara,

03:42

ele também vai ver isso. Então,

03:43

aqui tem as partes de configuração de como isso aqui deve ser,

03:46

os gates de qualidade que vão ter que ser rodados, ou seja,

03:49

ele dá um run gates aqui realmente para a gente rodar.

03:53

E aqui, o que ele vai cobrir que está no PRD.

03:59

Então, basicamente, ele vai cobrir... HTTP API, ou seja,

04:04

ele vai ver toda a parte de HTTP de API,

04:07

ou seja, registrar, e-mails, a parte de login, depois

04:13

disso ele vai para a parte de logout,

04:15

depois com o usuário atual, com a sessão atual,

04:19

se ele consegue acessar, e depois a parte de UI,

04:23

onde vai ter a página de registro, a

04:27

página de login, a parte de logout, a parte de autenticação,

04:33

teste E2E, onde vai fazer o cara entrar, se inscrever, fazer

04:39

o login e fazer o logout.

04:41

Então esse aqui é o contrato que a gente vai

04:44

utilizar aqui nesse momento para fazer essa segunda feature aqui.

04:49

No próximo vídeo,

04:50

o que a gente vai fazer? A gente vai focar na implementação e avaliação.

04:55

E aí a gente vai ver com calma como é que esse cara funciona.

## Resumo IA

**Abreviações**
*   **PRD**: Product Requirements Document
*   **TDD**: Test-Driven Development
*   **DDD**: Domain-Driven Design
*   **API**: Application Programming Interface
*   **UI**: User Interface
*   **E2E**: End-to-End
*   **F02**: Feature 02 (Segunda Feature)

**Resumo**
Esta aula introduz um fluxo de desenvolvimento de software mais automatizado em comparação com o processo anterior de geração manual de especificação, implementação e avaliação. O objetivo principal é demonstrar o uso de uma nova "skill" chamada `Implement and Evaluate`, que funciona como um orquestrador para realizar a implementação e a avaliação em um único ciclo, sem a necessidade de intervenção manual para iniciar a fase de avaliação.

O fluxo explicado envolve os seguintes passos:
1.  **Geração da Feature**: Utiliza-se o `Spec Writer` para gerar a especificação de uma nova funcionalidade, neste caso, a "Feature 02: Sistema de Autenticação", a partir de um PRD.
2.  **Análise dos Artefatos Gerados**: Após a geração, são produzidos três arquivos principais:
    *   `spec`: Detalha a especificação do sistema de autenticação, incluindo conceitos de backend, domínio de usuário, User ID como Value Object, normalização de e-mail e password. A especificação segue uma abordagem DDD-like com Clean Architecture.
    *   `plan`: Apresenta o plano de ação com pré-requisitos e uma série de estágios (até 9), cobrindo tarefas desde o backend até a interface do usuário e verificação.
    *   `contract.md`: Destacado como o ponto mais importante e novidade ("Harness"). Este arquivo detalha o contrato da feature para implementação e avaliação automática. Ele inclui:
        *   `Runtime Services`: Serviços que serão necessários (ex: Fastify Service, Next.js, Postgres).
        *   `Data`: Dados necessários para iniciar os testes (ex: usuário Alice com nome e e-mail específicos).
        *   `Configuration`: Configurações essenciais para o ambiente.
        *   `Quality Gates`: Critérios de qualidade que serão executados.
        *   `PRD Coverage`: Quais aspectos do PRD a feature cobrirá e testará, incluindo a API HTTP (registro, login, logout, sessão), a UI (páginas de registro, login, logout, autenticação) e testes E2E (inscrição, login e logout completos).

O `contract.md` serve como um guia detalhado para o agente de avaliação, permitindo que ele configure o ambiente, injete dados e execute os testes definidos de forma autônoma. A próxima aula focará na utilização desse contrato para a fase de implementação e avaliação.

**Pontos de atenção**
*   **Purismo na Especificação**: O instrutor observa que a especificação gerada pode ser "restritiva demais", mencionando o exemplo de definir `User ID` como um objeto de valor (Value Object) quando ele pessoalmente não adota um purismo tão elevado.
*   **Ajuste da Skill**: É ressaltado que o comportamento da skill (neste caso, o `Spec Writer`) pode ser ajustado para adaptar o nível de purismo ou outros requisitos técnicos.
*   **Importância do Contrato (`contract.md`)**: O arquivo `contract.md` é apresentado como uma das grandes novidades da abordagem "Harness", sendo fundamental para a automação do processo de implementação e avaliação, pois ele informa ao avaliador tudo o que é necessário para rodar os testes e garantir a qualidade da feature.