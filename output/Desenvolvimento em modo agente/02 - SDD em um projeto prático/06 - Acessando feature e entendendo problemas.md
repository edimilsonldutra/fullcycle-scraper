Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17784)

## Resumo da aula

Guidance mínimo pode ser suficiente para gerar arquivos, mas não garante que o agente execute a aplicação, valide o ambiente nem confirme que o fluxo realmente funciona. Quando o repositório só orienta o uso de uma skill genérica, como Next Best Practice, o agente tende a “digitar código” sem completar o ciclo operacional. O problema não está apenas na qualidade do modelo, mas na ausência de limites explícitos, critérios de comportamento e passos obrigatórios de validação.

A ausência de artefatos operacionais denuncia que a implementação não foi realmente exercitada. Se o agente pede para subir Docker Compose, copiar variáveis para .env.local, rodar migrações e iniciar o servidor, mas nada disso aparece no workspace ou no processo em execução, então ele não validou a aplicação localmente. Esse diagnóstico é importante porque código aparentemente correto pode falhar na primeira execução por dependências, configuração ou estado do ambiente.

Retomando o fluxo local já estabelecido, o gargalo novo aqui não é a feature de autenticação em si, mas a falta de automação ao redor do agente. Harness e scripts de inicialização encapsulam tarefas como subir containers, preparar .env.local, aplicar migrações, iniciar o servidor e liberar portas ocupadas. Sem isso, o agente improvisa comandos, entra em conflitos de processo e consome tokens resolvendo problemas repetitivos de infraestrutura local.

Quando já existe um servidor Next.js rodando em background, uma nova tentativa de subir a aplicação pode falhar mesmo que o código esteja correto. O agente então precisa detectar o conflito, identificar o processo anterior e encerrá-lo antes de reiniciar o ambiente. Esse tipo de recuperação operacional não deveria depender de tentativa e erro; ele deve estar codificado em scripts ou no harness para tornar a execução previsível.

Lembra do redirecionamento para /app, definido anteriormente como parte da costura entre features? Aqui ele deixa de ser apenas especificação e vira evidência de que a autenticação preparou corretamente a entrada da próxima feature. Ao criar uma conta e ser redirecionado para /app, o sistema confirma que cadastro, sessão e navegação mínima estão integrados do jeito esperado.

Ter rotas de register e login criadas não basta; o valor está em observar o comportamento real da aplicação com um usuário autenticado. Se o usuário já está logado, o acesso pode cair direto no destino protegido por causa do redirecionamento automático, o que também é um sinal útil de que a sessão está funcionando. A validação prática precisa considerar esse estado para não confundir ausência de tela com erro de implementação.

Quando o agente está bem domesticado por guidance e harness, a inspeção manual deixa de acontecer durante cada comando intermediário. O fluxo passa a privilegiar execução autônoma, geração de commits e abertura de pull request, concentrando a revisão humana no diff final. Isso só é viável quando o ambiente, os critérios de aceite e os mecanismos de validação já estão suficientemente estruturados para reduzir surpresas durante a implementação.

## Transcrição

00:01

Bom, pessoal, seguinte, tá?

00:03

Qual que é o grande problema que nós temos agora aqui, tá?

00:08

E esse é uma das coisas que mais

00:11

acontece quando você dá guidance zero pro agente.

00:16

Ou seja, quando você pede pra ele implementar uma coisa de forma superficial,

00:21

que nem eu fiz, tá? Mas também quando você não tem um monte de boundaries,

00:29

e critérios de como que o seu agente tem que se

00:33

comportar e quais são os limites do que ele tem que fazer.

00:37

Tanto que você está vendo que no meucloud.md só tem isso.

00:40

Só tem para ele usar o Next Best Practice. Mas o que acontece?

00:44

O meu agente pode ser muito bom.

00:46

O meu modelo pode ser muito bom. Mas se você perceber...

00:50

Ele pediu para rodar localmente, você roda o Docker Compose,

00:53

você copia esse cara para o env.local, roda o migrate,

00:57

dá um npm run dev test. O que significa quando ele está fazendo isso?

01:02

Quando eu olho para cá e não vejo nem que ele criou o .env.local,

01:06

significa que basicamente ele

01:11

nem executou a minha aplicação.

01:15

Ele só digitou código.

01:18

E esse tipo de coisa é muito ruim, entendeu? Então,

01:22

eu vou aqui, nesse momento, pedir para ele fazer isso aqui. Então,

01:32

faça você.

01:35

Pode localmente para eu acessar.

01:42

Eu estou com preguiça de ficar rodando esses comandos. Então,

01:45

ele está dando um docker com post-up -d.

01:49

Está subindo a aplicação. Ele está com o shell ativo.

01:54

Está aqui. Então, ele deve estar procurando agora o usuário e senha e tudo mais. Ele achou.

02:06

Duplicou o meu env.local.

02:09

Está rodando as migrações.

02:12

Vai iniciar o servidor em background.

02:16

E aqui, se você olhar,

02:18

já tem outro servidor em background que era do meu processo número 1, inclusive.

02:22

Vamos ver o que vai rolar nessa parada.

02:29

Falou que não deu para rodar. Provavelmente,

02:32

ele não está conseguindo rodar porque tem um Next rodando já no processo anterior. Olha ali.

02:38

Então ele vai matar o processo anterior e

02:41

vai rodar.

02:43

Está vendo que todos esses engasgos que ele está dando

02:46

e que a gente está gastando token à toa,

02:48

é porque falta de guidance, harness,

02:52

scripts que fazem inicialização, sobe e desce o ambiente,

02:56

gerencia portas e tudo mais isso aqui para a gente.

02:59

Então ele colocou aqui, tudo rodando, landing page, cadastro,

03:02

login e register aqui para mim,

03:04

colocou o banco de dados ali com as migrações aplicadas.

03:08

Então, eu vou chegar agora aqui, tá?

03:11

E vou olhar aqui na minha porta 3000 e vou botar esse cara para rodar agora,

03:17

tá? Então, voltamos aqui ao meu projeto.

03:20

Vou aqui criar uma nova conta. Caiu aqui para eu criar minha conta.

03:24

Então, eu vou colocar Wesley Silva.

03:31

Vou colocar www.com e

03:35

Vou colocar uma senha.

03:39

Se eu não me engano, tem que ter oito caracteres.

03:41

E uma letra maiúscula, né? Que eu pedi.

03:45

Vou colocar. Vou dar um create account aqui pra mim. E pronto.

03:49

Ele criou a minha account. Mas olha só que interessante.

03:54

Ele já me redirecionou pro barra app. E por que ele me redirecionou pro barra app?

03:59

Porque eu sei que ele provê pra minha feature trace.

04:05

Trace, né? Provê pra minha feature trace. Tô querendo falar trace em inglês.

04:12

O link que aquela feature vai ter que usar para entrar no meu dashboard aqui. Então, realmente,

04:20

ele conseguiu fazer essa minha preparação. Então,

04:23

esse ponto aqui é interessante de a gente conseguir ver.

04:27

E, provavelmente, a gente tem a página anterior,

04:30

que é a página de login que ele criou aqui também.

04:35

Tem o login que deve mandar para essa página.

04:39

É que eu já estou logado, né? Então,

04:41

por isso que ele já caiu direto, porque ele está me redirecionando.

04:45

O que eu vou pedir para ele fazer agora aqui é, vou colocar aqui, mate o processo.

04:53

O que eu quero mostrar agora aqui para vocês,

04:56

vou mostrar inclusive no nosso próximo vídeo,

04:59

para mostrar uma alternativa do que é a tendência,

05:04

e eu acredito que daqui para frente muita gente

05:07

já vai estar desenvolvendo nesse tipo de esquema,

05:10

principalmente...

05:13

Se você... Como que eu posso dizer?

05:17

Se você já conseguiu domar o seu agente.

05:21

Se você conseguiu organizar toda a parte de harness em volta dele.

05:25

Quando você faz isso, basicamente você já não vai mais olhar o código dele.

05:31

Você vai olhar o código dele na pull request apenas.

05:34

Porque ele já vai fazer os commits e a pull request em seguida.

05:38

Então, o que eu vou fazer? Eu vou...

05:41

Parar esse vídeo e eu vou mostrar uma outra

05:43

forma utilizando a própria plataforma da cloud aqui,

05:47

mas a gente pode fazer isso também utilizando o Codex App,

05:51

por exemplo, que tem esses tipos de recurso também.

## Resumo IA

**Abreviações**
*   **PR**: Pull Request

**Resumo**
A aula aborda a importância da automação e da validação operacional no desenvolvimento de software assistido por um agente de IA. O objetivo principal é demonstrar que, mesmo com um modelo de IA avançado, um "guidance" mínimo e a ausência de um "harness" (conjunto de ferramentas e scripts de automação) resultam em implementações incompletas, sem validação real do ambiente local e com alto consumo de recursos para resolver problemas repetitivos.

Os conceitos e ferramentas abordados incluem: a necessidade de ir além da mera geração de código, garantindo que o agente execute e valide a aplicação; o uso de ferramentas como Docker Compose para subir ambientes, arquivos `.env.local` para configuração e a aplicação de migrações de banco de dados. Foi demonstrado o fluxo de inicialização de um servidor Next.js e a gestão de conflitos de porta, onde o agente precisou identificar e encerrar um processo pré-existente antes de iniciar o novo. A feature de autenticação (cadastro e login) foi utilizada como exemplo para validar a integração e o comportamento esperado da aplicação, com o redirecionamento para a rota `/app` servindo como prova de que a sessão e a navegação mínima funcionam.

O fluxo explicado pelo instrutor começou com a identificação do problema: o agente gerou o código, mas não realizou a validação local, como a criação do `.env.local` ou a execução da aplicação. Em seguida, o instrutor solicitou que o agente executasse a aplicação localmente, o que levou o agente a orquestrar o ambiente (Docker Compose, migrações, servidor). Durante este processo, o agente encontrou e resolveu um conflito de porta. Finalmente, o instrutor validou a funcionalidade de autenticação, registrando um usuário e observando o redirecionamento para a página protegida, reforçando a ideia de que a validação prática do comportamento da aplicação é crucial. A aula concluiu discutindo como um agente bem "domesticado" por guidance e harness permite um fluxo de trabalho onde a revisão humana se concentra apenas no "diff" final de um pull request (PR), após a execução autônoma e geração de commits pelo agente.

**Pontos de atenção**
*   **Guidance Mínimo vs. Abrangente**: Um "guidance" superficial para o agente não garante a execução, validação do ambiente ou confirmação de que o fluxo funciona. A falta de limites explícitos, critérios de comportamento e passos obrigatórios de validação impede o agente de completar o ciclo operacional.
*   **Ausência de Artefatos Operacionais**: Se o agente descreve passos operacionais (subir Docker Compose, copiar `.env.local`, rodar migrações, iniciar servidor), mas esses artefatos não aparecem no workspace ou em processos em execução, isso denuncia que a implementação não foi realmente exercitada.
*   **Falha na Primeira Execução**: Código aparentemente correto pode falhar na primeira execução devido a dependências, configuração ou estado do ambiente, reforçando a necessidade de validação prática.
*   **Gargalo na Automação**: A falta de "harness" e scripts de inicialização (para subir containers, preparar `.env.local`, aplicar migrações, iniciar servidor, liberar portas) força o agente a improvisar comandos, entrar em conflitos de processo e consumir tokens resolvendo problemas repetitivos de infraestrutura local.
*   **Gerenciamento de Conflitos**: A recuperação operacional, como detectar e encerrar processos anteriores que ocupam portas, não deve depender de tentativa e erro do agente, mas sim estar codificada em scripts ou no "harness" para garantir execução previsível.
*   **Validação do Comportamento Real**: Ter rotas de `register` e `login` criadas não é suficiente. O valor reside em observar o comportamento real da aplicação com um usuário autenticado, incluindo redirecionamentos esperados (ex: para `/app`) e como o sistema lida com sessões já ativas.
*   **Estado da Sessão e Redirecionamento**: A validação prática deve considerar o estado da sessão. Um usuário já logado pode ser redirecionado automaticamente para um destino protegido, o que é um sinal de que a sessão está funcionando, e não um erro de implementação.
*   **Inspeção Manual vs. Execução Autônoma**: Quando o agente está bem domesticado por "guidance" e "harness", a inspeção manual durante cada comando intermediário diminui. O fluxo privilegia a execução autônoma, geração de commits e abertura de Pull Requests (PRs), concentrando a revisão humana no "diff" final. Isso exige um ambiente, critérios de aceite e mecanismos de validação bem estruturados.