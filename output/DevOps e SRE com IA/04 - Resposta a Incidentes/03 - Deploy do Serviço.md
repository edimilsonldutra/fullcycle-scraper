Módulo: DevOps e SRE com IA\
Aula: [Deploy do Serviço](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18512)

## Resumo da aula



## Transcrição

00:00

Então, vamos começar aqui com o nosso deploy do serviço. Vou pegar aqui,

00:04

vamos no repositório do nosso App API, já está aqui.

00:08

Ok? A gente tem aqui um deployment, eu já tenho aqui o manifesto dele criado.

00:13

Esse manifesto eu vou disponibilizar para vocês aí,

00:15

para vocês conseguirem fazer isso também. Então,

00:19

temos aqui o nosso manifesto criado. O que a gente vai ter?

00:22

A gente está adicionando aqui algumas coisas,

00:25

que é uma imagem de policy aqui, está com o Never.

00:30

Antes, na verdade, esse mal de policy aqui já estava com o never,

00:34

só que a gente tirou um security context aqui.

00:37

Colocamos aqui algumas variáveis de ambiente, como, por exemplo,

00:41

o app name, o app env aqui.

00:43

Ajustamos aqui os requests.

00:45

O service aqui continua praticamente a mesma coisa. Então,

00:50

vamos salvar esse cara aqui para a gente fazer o ajuste dele.

00:57

Vamos também adicionar aqui a parte do alert -rules,

01:04

que é um arquivo. Vou puxar ele aqui. Vamos criar ele aqui,

01:08

na verdade. Ele se chama alert -rules e esse arquivo será consumido pelo Prometheus,

01:14

tá bom? alert -rules .imo. Tá aqui.

01:21

Vamos copiar o conteúdo dele que a gente tem aqui embaixo.

01:24

Será disponibilizado para vocês também.

01:26

E aqui a gente tem alguns alert roads que a

01:28

gente vai aplicar lá dentro do nosso Kubernetes,

01:31

do nosso serviço.

01:33

Dentro do nosso cluster lá dentro. Ok?

01:38

Vamos lá. Git checkout -b. Add. Ajuste. Deployment. Mais.

01:49

End, né? Vou colocar end.

01:52

alert roles, ok?

01:57

Então git add ponto, git commit menos m,

02:01

ajuste deployment mais alert roles.

02:08

Vamos dar um git branch aqui pra gente pegar o nome certinho da branch, copiar ele, ok?

02:17

Dar um git push origem da branch.

02:23

Feito isso, vamos aqui no nosso

02:27

no nosso código, olhar aqui as brands que foram criadas,

02:33

inclusive já até cliquei sem querer aqui na brand, vamos aqui,

02:36

brands criadas, a gente já tem aqui o ajuste deployment,

02:39

vamos aqui no pull request, vamos criar um novo pull request.

02:46

A gente vai pegar esse ajuste deployment e a last worlds,

02:53

vamos criar aqui um pull request.

02:57

Ok, pelo request criado,

02:59

deixa a parte aqui rodar de verificação lá do verificação de segurança, né?

03:05

Que é o nosso spec plan de segurança.

03:07

Vai verificar aqui o auto -abstrumentation também,

03:09

que é aquelas validações que a gente colocou lá.

03:12

Enquanto isso, vamos dar uma olhada aqui no nosso cluster.

03:15

Deixa eu dar uma verificada aqui. Está aqui no nosso iTerm, o nosso cluster.

03:22

Aqui em cima, na aba de K9S, temos aqui os nossos serviços sendo executados.

03:28

Vamos voltar aqui na nossa interface para ver.

03:31

Já fez aqui o comentário de segurança,

03:32

tudo certinho. Vamos fazer o pull request aqui.

03:36

Pull request não, vamos fazer o merge aqui para a main do nosso pull.

03:42

Feito, a gente vai iniciar aqui o deploy.

03:46

Vou dar um pause aqui no vídeo até esse deploy ser feito.

03:49

Assim que estiver pronto lá dentro do nosso cluster,

03:52

eu volto aqui para dar continuidade com vocês.

03:55

Ok, estou de volta aqui. Deploy concluído. A gente pode entrar aqui no deploy.

04:01

Conseguimos ver aqui que ele aplicou tudo certinho lá dentro.

04:07

Aplicou aqui o que a gente queria do MBA App Alerts.

04:12

A gente conseguiu aplicar aqui.

04:14

A gente conseguiu aplicar também o nosso deploy novo aqui.

04:18

O service. Tudo certinho aqui.

04:22

Vamos aqui no Kubernetes.

04:25

A gente no K9S, a gente consegue ver que os pods acabaram de iniciar aqui,

04:30

estão up e funcionando normalmente aqui

04:34

com o health check bem certinho.

04:37

Legal? Então, ok. Agora nós vamos para a segunda parte.

04:41

Vamos atualizar o nosso serviço do MCP do Kubernetes.

04:46

Legal? Então, hoje nosso MCP do Kubernetes... o nosso servidor de MCP Kubernetes,

04:53

ele simplesmente faz consultas. Está até aberto aqui já.

04:57

Então, a gente tem aquele YAML do Kubernetes,

04:59

esse serviço aqui consegue somente

05:02

fazer consultas lá dentro do Kubernetes.

05:09

Então, a gente vai alterar esse serviço e colocar um outro servidor,

05:14

um outro MCP Kubernetes, um STDIU Kubernetes.

05:18

que a gente consegue, além de fazer consultas,

05:21

a gente consegue também fazer rollouts,

05:29

fazer operações de write dentro do servidor, tá bom? Dentro do servidor Kubernetes.

05:35

Então, dessa maneira a gente consegue ter mais

05:38

facilidade de pedir para um pod reiniciar,

05:41

para um pod escalar, tudo usando MCP, tá? Então aqui é bem simples, a gente vai...

05:47

tirar esse servidor aqui que já existe.

05:49

A gente vai manter as mesmas configurações aqui, Kubernetes,

05:52

comando mpx, args, etc. E vamos trocar por esse cara aqui.

05:57

Ele se chama mcp -server -kubernetes.

06:06

Deixa eu ver se está certinho. Kubernetes.

06:09

Está certinho.

06:12

Só isso. mcp -server -kubernetes. Esse é o nosso...

06:16

servidor Kubernetes que a gente vai usar agora, que vai funcionar como stdio,

06:19

rodando em npx lá dentro, ok? Para esse cara,

06:23

a gente tem uma parte de env, igual a gente tem aqui embaixo no lockmcp.

06:28

Então vamos adicionar aqui um env, env,

06:32

dois pontos, abre chave, fecha chave, dá um tabzinho aqui,

06:38

tab em cima na real, um tab aqui,

06:41

e a gente, eu vou copiar aqui que vai ficar mais fácil, que é uma env,

06:47

que a gente vai precisar aqui de yellow non-destructive tools.

06:52

O que é esse yellow non-destructive tools?

06:55

Ele basicamente vai impedir que tools de delete,

07:01

tools que podem quebrar o seu cluster, podem destruir o seu cluster,

07:06

sejam ativadas.

07:07

Então a gente vai adicionar essa variável.

07:13

De ambiente para evitar que isso aconteça.

07:15

E por fim,

07:16

a gente está falando aqui de um serviço que vai precisar de alguns acessos a mais.

07:22

Esses acessos são de escrita.

07:25

A gente tem uma lista de roles novas aqui que a gente vai precisar colocar.

07:29

Vou copiar elas aqui. E essas roles vão servir para a parte de escrita.

07:35

A gente continua com a habilidade de leitura para o MCP,

07:38

mas essas roles aqui a gente vai ter a habilidade de escrita.

07:41

Então aqui é toda a parte de escrita.

07:45

E aqui, de leitura, desculpa, e aqui toda a parte de escrita.

07:49

Então a gente consegue fazer um kubectl rollout,

07:52

um kubectl scale para ele descalar pods, e um kubectl patch,

07:58

um kubectl apply,

07:59

e a gente tem várias possibilidades aqui de uso

08:02

dessa biblioteca que a

08:08

gente está usando para MCP,

08:09

tá bom? Para o Kubernetes especificamente.

08:12

Biblioteca da Comunidade, vocês pesquisarem no Google aí,

08:16

tranquilo, vocês vão conseguir achar,

08:17

e vai estar também no material que eu vou disponibilizar de referência,

08:21

para vocês conseguirem fazer essa configuração aí também no ambiente de vocês,

08:26

ok? Então vamos aplicar, do mesmo jeito que a gente já aplicou várias vezes aqui,

08:30

dar uma referência, kubectl k8s deploy .sh, ok? Vamos aplicar aqui.

08:39

Ele criou a imagem lá para mim, do MCP novo,

08:42

já importou lá para dentro do Kubernetes e já está fazendo a aplicação.

08:46

Ok, aplicado, a gente já tem o MCP operacional,

08:50

está aqui, óbvio que não, esse aqui é o serviço.

08:52

Vamos lá na nossa stack de observabilidade,

08:55

no nosso namespace de observabilidade, desculpa, do OpenABY, na verdade,

08:59

que o MCP está deployado lá dentro, e aqui a gente tem o MCP.

09:03

Lembrando que ele fez o deploy somente...

09:06

do objeto deploy, do tipo deploy. Ele não fez o rollout do serviço. Então,

09:11

vamos fazer o rollout do serviço,

09:13

que é simplesmente deletar, que ele vai reiniciar aqui.

09:15

E aqui ele já começou a baixar.

09:17

Iniciando configurações, conexão com o servidor Kubernetes. Então,

09:20

ele já começou aqui a conexão. Deixa ele iniciar.

09:23

Ok. Está aqui tudo certinho. Baixou.

09:28

Está reclamando aqui de uma versão antiga,

09:30

glob supported e algumas coisinhas a mais aqui.

09:33

Porém, iniciou tudo certinho. Iniciou o Kubernetes.

09:36

Conexão para Prometheus. Conectou certinho.

09:38

Conexão para Lock. Lock MCP. Run STD IO.

09:44

Tudo funcionando. 100% aqui.

09:46

Temos 3 servidores MCP ativos.

09:49

Utilizando o MCP para traduzir para o OpenRBI. Beleza?

09:56

Se vocês quiserem usar, por exemplo, lá no OpenCode. Basta você colocar.

10:02

dar uma pesquisada no Open Code ali e colocar

10:04

esse arquivo de configuração completo lá dentro,

10:07

que vocês já vão ter a habilidade de usar esses serviços usando o Open Code.

10:12

Usando o próprio Cloud Code,

10:15

o que vocês tiverem de interface conversacional para LLM.

10:21

Vamos verificar se o serviço subiu certinho com o Open Web UI.

10:25

Vamos aqui dentro do Open Web UI, vamos pegar o endereço do nosso MCP.

10:31

A gente vem aqui, painel do admin, configuração.

10:34

A gente tem aqui na parte de integrações,

10:37

Kubernetes, que a gente tinha criado na última aula. Ok?

10:42

Aqui no avançado a gente consegue o endereço completinho.

10:45

Vamos pegar aqui o endereço completinho e colar aqui na nossa aba.

10:49

Então vamos lá. Olha, deu problema.

10:52

Tivemos um problema aqui.

10:54

Porém, o problema é simples de resolver, tá? Se quer uma chamada interna,

10:58

como o servidor está dentro do mesmo cluster,

11:00

está dentro da mesma rede,

11:01

ele consegue fazer a chamada internamente do pod para o service lá dentro.

11:06

Como a gente está do lado de fora,

11:07

a gente está no localhost, a gente vai precisar criar, criar não,

11:11

a gente vai ter lá já criado o ponto ingress que a gente consegue chamar.

11:15

E o nosso ponto ingress se chama ponto test.

11:17

E a porta que ele responde é na 8080.

11:21

Ok, temos o nosso MCP. Aqui está ativo e operacional.

11:26

Então aqui, se a gente organizar o JSON bonitinho,

11:28

a gente consegue ver que ele consegue fazer um describe,

11:31

ele consegue fazer um apply,

11:33

ele consegue fazer um create, ele consegue fazer log e assim por diante.

11:38

Então, se vocês notarem, a gente já tem aqui a possibilidade de create,

11:43

que é uma operação de write,

11:46

e a gente tem a possibilidade de apply, que também é uma operação de write.

11:49

Legal? Temos aqui pronto o nosso MCP.

11:52

Então, finalizado essa parte do deploy novo que a gente fez, mais o MCP.

## Resumo IA

[RESUMO_IA]