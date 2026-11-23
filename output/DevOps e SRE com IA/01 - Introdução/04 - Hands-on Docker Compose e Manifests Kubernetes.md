Módulo: DevOps e SRE com IA\
Aula: [Hands-on: Docker Compose e Manifests Kubernetes](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18502)

## Resumo da aula



## Transcrição

00:00

Vou abrir o Docker Compose, vou fechar aqui o prompt,

00:02

que a gente não está precisando dele mais agora.

00:04

E, basicamente, o que a gente tem? Os serviços, vou minimizar aqui,

00:08

para a gente conseguir ter uma visualização melhor.

00:11

A gente tem os serviços, que é o que vai subir,

00:13

todos os services que vão subir. O primeiro é o app,

00:17

que a gente tem um build do contexto ponto, que é o local, e o Dockerfile,

00:22

que é o que a gente gerou na primeira etapa.

00:25

Aqui é o nome do container e as portas que ele será exposto.

00:28

Algumas variáveis de ambiente, como o endereço do banco de dados,

00:31

a senha, o usuário, etc. Aqui está exposto o pessoal,

00:35

mas a gente consegue, como é ambiente de dev,

00:39

a gente consegue ter, não tem esse problema.

00:42

Aqui já tem até uma variável do OpenTelemetry que a gente vai usar lá para frente,

00:46

mas já está mostrando aqui.

00:49

E aqui um DependsOn, ou seja, para esse app subir,

00:54

a gente vai depender do Postgres e do Redis subir primeiro.

00:57

Legal? E aqui um health check. Então,

01:00

o ponto é esse.

01:01

A gente gera o Docker Compose e passa validando

01:05

cada uma das coisas que estão acontecendo.

01:08

Não precisa ser assim muito no detalhe,

01:10

é só você ver alguma coisa diferente mesmo e vale a pena você mexer,

01:14

você mexe. Ok? Docker Compose pronto. Então,

01:17

a gente consegue aqui fazer a subida desse serviço. Então, vamos lá.

01:23

Vamos subir ele aqui. Puxar um pouquinho a tela aqui, vamos dar um docker compose,

01:30

traço compose,

01:32

up, menos d,

01:36

ele vai pegar o arquivo desta pasta e vai rodar,

01:40

que é o arquivo docker compose e emu que a gente está com ele aberto aqui. Então vamos rodar,

01:45

ele vai fazer a criação, notem que...

01:49

a parte que está rodando, que ele ainda está subindo,

01:51

o banco de dados e o Redis, assim que ambos estiverem prontos,

01:55

o app vai ser deployado também.

01:58

Ok, o app está aqui, o container do app está criado, o Postgres e o Redis estão de pé,

02:05

demorou 11 segundos aqui para fazer,

02:07

e para verificar a gente pode dar um docker compose

02:16

ps,

02:19

onde a gente consegue ver todos os serviços que estão rodando lá.

02:24

No nosso caso, a gente tem o App API Dev,

02:28

App Postgre Dev e App Redis Dev. E, basicamente, o nosso aplicativo está aqui.

02:35

Se a gente vier aqui no Docker Desktop,

02:38

a gente consegue ver o nosso aplicativo rodando aqui em container,

02:42

que é esse app. A gente tem o container aqui também.

02:45

Se quiser ver o log do container, pode clicar aqui,

02:48

que dá para ver, inspecionar quais foram os dados que entraram nele.

02:52

A gente tem aqui várias coisas,

02:53

a gente consegue entrar dentro do container, dar alguns comandos.

02:57

Então a gente consegue fazer várias coisas aqui com o Docker Desktop. É bem interessante.

03:01

Se a gente vier aqui na API Dev,

03:04

A gente consegue ver aquele mesmo log quando a gente executou localmente.

03:08

Então, o log, quando ela faz a parte ali do banco de dados,

03:11

os logs aqui, de quando ele sobe e tudo certinho.

03:15

A gente vai dar uma verificada aqui no banco de dados agora,

03:18

ver se está rodando certinho. Vamos dar um reload aqui. Refresh.

03:22

Temos o banco de dados e já temos as colunas aqui prontas.

03:25

Se a gente dá um SELECT aqui, asterisco, não temos nada.

03:29

Então, continue, não temos nada, a tabela está vazia.

03:32

Agora, a gente pode fazer o teste lá pelo Postman mesmo.

03:35

A gente vai chamar aqui um /health, ver se o serviço está de pé.

03:39

A gente consegue ver que retornou um health aqui,

03:41

só que agora ele está rodando todo em Docker.

03:44

Então, a gente consegue fazer um envio aqui. Zero itens, não tem nada aqui na lista.

03:49

E aqui a gente consegue inserir algum item lá dentro.

03:52

Vamos inserir. Se a gente fizer aqui de novo,

03:55

a gente já tem o item inserido lá dentro da lista.

04:00

Dentro do nosso serviço, o item foi inserido lá.

04:04

Se a gente vier no banco de dados novamente,

04:06

a gente vai conseguir ver que o item está aqui disponível para uso.

04:11

Com status de ativo e assim por diante. Legal?

04:16

Quando a gente faz o Docker Compose, ele vai subir a aplicação,

04:20

vai subir todas as aplicações que precisam,

04:24

que são dependências para essa aplicação, como o Postgres e o Redis.

04:30

Isso é ideal para a gente conseguir fazer alguns testes locais,

04:33

validar como está funcionando, se está tudo certo, etc.

04:37

Porque isso aqui já é um sabor do que a gente vai ter dentro do Kubernetes,

04:42

que é justamente essa criação com vários artefatos.

04:46

Então, a gente vai ter criação de Postgres, de Redis, da própria API em si,

04:50

vai conseguir verificar os health check e assim por diante.

04:54

Legal? Então, criado isso, próxima etapa agora,

04:58

a gente vai conseguir criar a parte do... Esqueci de passar o slide,

05:04

né, pessoal? Aqui, o Docker Compose no ambiente dev,

05:07

a API aqui, FastAPI,

05:09

o Postgres 16 com o volume e o Redis aqui, set com persistência.

05:14

E por que a gente vai gerar via prompt, um dos motivos que eu comentei lá.

05:18

Consistência com o Dockerfile de produção,

05:20

variáveis de ambientes sincronizados, health check espelhados,

05:23

e o dev setup nunca diverge de produção. Então, a gente vai ter isso aqui.

05:30

Dentro dessa pastinha aqui, junto com o material,

05:32

a gente vai ter o prompt para gerar esse Docker Compose. Combinado?

05:38

Próxima etapa aqui, a gente vai gerar os manifestos Kubernetes.

05:42

Então, a gente vai gerar... O manifesto de deploy, manifesto de serviço,

05:46

o namespace que vai comportar essa aplicação.

05:50

A gente vai gerar todos os tipos de

05:55

objetos específicos dentro do Kubernetes para comportar essa aplicação.

05:59

Então, deployment, que tem a réplica, as probes, as resources, as envs. O service,

06:05

que é um ClusterIP que vai mapear a porta do serviço.

06:07

O HPA, que é onde a gente vai fazer o autoscale.

06:13

Controlar o autoscale se a aplicação estiver sendo muito usada,

06:17

de acordo com o que foi definido.

06:19

Ele faz o scale automático horizontal para você. Então,

06:24

Ele cria novos pods horizontais. E aqui o Network Policy com ingress, roles e etc.

06:30

Então, a nossa próxima etapa é fazer a criação dos objetos Kubernetes. Ok?

06:37

Então, vamos lá, pessoal. Vamos criar aqui os nossos manifestos Kubernetes.

06:43

Com a mesma tela do OpenCode aberto aqui, a gente pode fazer essa criação.

06:48

Isso, a criação desse Kubernetes só depois da validação do OK, Compose,

06:52

e agora a gente vai simular o ambiente de produção aqui.

06:56

Então, a primeira coisa que a gente vai fazer é mostrar o prompt aqui para vocês. Vamos

07:04

abrir aqui o prompt que a gente

07:06

vai usar para criar os nossos manifestos Kubernetes.

07:13

Eu vou fechar o Docker Compose, que a gente não vai precisar usar ele mais.

07:16

E primeira coisa, vamos gerar.

07:19

Manifesto Kubernetes no ambiente YAML para a seguinte aplicação, FastAPI.

07:25

Vai seguir basicamente a mesma coisa que a gente usou

07:28

lá no título para criar o Docker Compose,

07:32

porém com alguns detalhes.

07:33

E suas dependências aqui, está falando português do Reds, que a gente usa.

07:37

Os SLOs devem informar, configuração, resource, props e HPA.

07:42

Todos os recursos namespace demo app MBA.

07:45

Então, a gente tem aqui um namespace específico que

07:49

a gente está desenvolvendo para essa aplicação.

07:52

Ok? Então,

07:53

aqui é um contexto da aplicação, onde a gente mostra o nome,

07:56

o Dockerfile, a imagem Docker que vai ser usada,

08:00

que está aqui, que é aquela imagem que a gente gerou lá na primeira parte,

08:04

quando a gente gerou o Dockerfile,

08:06

os SLOs de produção, que vão ser usados aqui para definir. Quais que são os HPAs,

08:12

qual que é a definição do HPA, as dependências,

08:15

que é o Postgres, o Redis e o ConfigMap,

08:18

então a gente tem essas dependências aqui, e as regras dos manifestos,

08:24

de cada um dos manifestos do Kubernetes.

08:26

Então, primeiro a gente tem o namespace,

08:28

o Postgres StatefulSet, o que é o StatefulSet?

08:32

É a persistência do dado, então ele vai criar,

08:34

além do container Postgres, ele vai criar um disco,

08:40

e esse disco vai persistir o dado. Então, normalmente, pods são stateless.

08:46

Se ele for reiniciado, ele perde os dados. Entendeu? Então,

08:50

esse Stateful é basicamente para quando o Post reiniciar,

08:54

ele não perder as informações dele e continuar de onde parou.

08:57

Como se fosse um Post que está instalado dentro de uma máquina comum.

09:01

Só que aqui ele está rodando em pod. Ok? Heads,

09:03

a mesma coisa. Stateful, para ele não perder.

09:06

A referência dele e reverter o banco de dados dele ali. O deployment,

09:11

onde a gente fala qual que é o nome do app,

09:13

qual que é o tipo dele, que é o back-end, qual que é o namespace,

09:17

quantidade de réplicas, a porta que o container vai rodar e assim por diante.

09:23

E aqui um service YAML,

09:25

que é onde o service vai apontar para os deployments.

09:29

Então, o service vai fazer o controle tipo assim.

09:32

O pod X está com consumo muito alto,

09:36

Então eu vou distribuir para o pod Y. Tem dois pods,

09:39

Então ele vai distribuir a parte de orquestrar mesmo e fazer

09:46

A distribuição de carga entre os dois pods que estão ativos ali,

09:51

Ou mais. O HPA, que é o Horizontal Pod Autoscaler,

09:55

Se os dois estão muito ocupados, a gente conseguiu ver ali.

09:59

E que ele está sendo muito utilizado por ambos,

10:03

Ele vai fazer automaticamente a escala desses pods na horizontal.

10:07

Vai criar pods irmãos daquele ali que vai responder para o service do mesmo jeito.

10:12

Network policy,

10:13

A gente vai definir algumas coisas aqui de ingress

10:16

E egress para a gente sair da internet,

10:18

Sair para a internet e a entrada para dentro do pod.

10:21

Quem está de fora do ambiente pode entrar no pod. Um ConfigMap,

10:26

Com as duas variáveis não sensíveis do ambiente,

10:30

E os Secrets com as variáveis sensíveis do ambiente,

10:33

Como por exemplo Postgres User e a senha.

10:36

Aqui só uma ordem que a gente precisa

10:39

Aplicar esses manifestos de

10:45

De acordo com o K3D,

10:47

Ok? O que a gente precisa aplicar desse jeito.

10:50

O formato de saída aqui a gente explica para ele que ele vai criar alguns

10:54

Arquivos, que cada um dos arquivos vai ser um K8s / o nome do arquivo.

10:58

Então ele vai criar aqui do ladinho uma pasta que chama K8s para mim.

11:02

Então vamos lá, vamos rodar essa criação aqui dos manifestos Kubernetes.

11:08

Ok? Dá um Enter aqui.

11:10

Então agora ele está iniciando a criação do manifesto Kubernetes.

11:14

Vocês vão notar que aqui ele vai gerar uma pastinha que vai chamar K8s.

11:21

Está fazendo

11:24

A criação. Primeiro está criando aqui o namespace.

11:28

Já criou a pastinha k8s e o namespace aqui. yaml já está sendo preenchido.

11:34

Está criando o ConfigMap agora.

11:37

ConfigMap criado. Namespace criado.

11:41

Secret ck pode ser criado. Que a gente tem aqui o Postgres e PostgresPassword.

11:46

Vamos continuar olhando aqui. Qual que vai ser o próximo.

## Resumo IA

[RESUMO_IA]