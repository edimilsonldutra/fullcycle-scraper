Módulo: DevOps e SRE com IA\
Aula: [Ferramentas & Prática (Postmortem Generator)](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18513)

## Resumo da aula



## Transcrição

00:00

Temos aqui o nosso SRE Threshold pronto.

00:04

Próximo agent que a gente vai criar aqui é o PlusMortemGenerator.

00:08

O PlusMortemGenerator, mesma coisa. Novo agent, nome do modelo aqui,

00:15

Queen 3.5.

00:17

Nós vamos copiar o prompt dele aqui também.

00:23

Vai estar lá nos materiais para vocês conseguirem.

00:28

Conseguirem detalhar melhor, se vocês quiserem.

00:30

O que a gente vai precisar selecionar nele?

00:32

System Prompt e as tools Incident,

00:35

Prometheus e K8S. As tools Prometheus, Incident e Kubernetes.

00:43

A gente já tinha criado, tá bom?

00:46

Salvar e criar. Temos mais um agent pronto.

00:49

E por último, o SRE Health Monitor.

00:55

Vamos criar o novo agent aqui, chamado aqui de modelo, né?

00:59

Queen 3.5.

01:01

Copiar o nosso System Prompt e colar aqui.

01:05

Ok? Não vou parar, não vou explicar esse System Prompt. Dei uma olhada também nele.

01:10

E lá a gente vai selecionar a mesma coisa.

01:13

As tools K8S, Prometheus e Incidente.

01:17

Incidente, Prometheus e Kubernetes. Temos aqui.

01:24

Salvar e criar. Ok, temos os nossos agents prontos aqui.

01:28

Vamos fazer o teste de algum?

01:31

Vamos pegar esse Threshold, vamos perguntar, o que você pode fazer?

01:37

Ah, só um detalhe, antes da gente perguntar,

01:39

eu esqueci de habilitar nesses aqui a chamada Native,

01:44

para ele conseguir fazer o looping de função.

01:49

Então ele consegue fazer o looping automático lá e se resolver.

01:53

Então, pós-morta e direita, mesma coisa, eu não selecionei.

01:56

Vamos mostrar aqui os parâmetros avançados, chamada de função nativa.

02:01

Antes que a gente esqueça de fazer isso. Vamos aqui no Threshold,

02:05

que a gente tem várias funçõezinhas aqui que a gente pode usar.

02:09

Dar um novo chat aqui.

02:13

Threshold e perguntar, o que você pode fazer?

02:17

Ele vai detalhar para a gente aqui o que ele consegue fazer. Vamos esperar.

02:24

É bastante contexto.

02:26

Minha máquina aqui vai dar uma fritada agora

02:29

que eu estou rodando o modelo localmente.

02:31

Vamos ver como é que está lá dentro do nosso LM Studio.

02:36

Está rodando aqui loucamente.

02:41

Vamos voltar lá no OpenAI e ver.

02:44

Temos a resposta aqui. Como assistente de rede de Kubernetes,

02:47

pode ajudar você a diagnosticar,

02:48

resolver problemas com Kubernetes e assim por diante. Como trabalho.

02:52

Começo amplo, lista de pods, identifico o problema específico,

02:57

faço análise profunda, e assim por diante. Então,

03:01

temos aqui, inclusive, colocaram até uns textos em japonês aqui,

03:05

pode ser algum erro do nosso prompt aí,

03:09

ou da própria AI que colocou, tá bom? Então,

03:12

a gente consegue aqui ter todo um contexto e pedir

03:14

para ele fazer as coisas com esse trecho roteiro.

03:16

Beleza?

03:21

Na próxima aula, no módulo 5, a gente vai usar esse cara aqui de foto.

03:24

Legal? Por último, a gente vai criar alguns automations lá dentro do OpenRBI.

03:30

Só um ponto. Usem sempre a última versão do OpenRBI.

03:36

Porque esse automation está disponível na última versão.

03:39

E a gente vai usar ele aqui. Legal?

03:42

Então a gente vai criar um automation de half-check. Legal?

03:46

Vamos aqui dentro. A gente vai em user.

03:50

Automações. Essas automações a gente vai criar uma nova automação.

03:54

Aí eu já tenho aqui os parâmetros dessa automação.

03:57

Deixa eu pegar aqui para a gente fazer.

04:00

Automation. Aí a gente vai criar agora de Health Check.

04:03

Essa aqui vai se chamar Health Check.

04:07

Ela vai ter essa descrição aqui.

04:11

Temos essa descrição. Verifique o status, SLO, serviço, app, API, namespace.

04:17

O namespace está errado aqui na descrição.

04:19

Vamos arrumar o namespace. Vou

04:24

pegar aqui no Kubernetes. Namespace é demo app mba.

04:32

App API dentro da tela a cada 5 minutos e detectar problema,

04:38

diagnosticar, sugerir mitigação. Legal?

04:42

Basicamente, a gente vai ter aqui um model ID que a gente vai selecionar,

04:49

que vai ser o nosso SRE.

04:52

Trash Holder. Trash Holder aqui.

04:57

E a gente vai criar essa automação

05:03

aqui a cada 5 minutos. Então a gente tem aqui a cada hora.

05:09

Não é a cada hora não.

05:10

Personalizado. E a gente vai colocar aqui o textinho de 5 minutos aqui. Ok.

05:20

Feito isso.

05:22

A gente vai salvar a nossa automação. Vou

05:36

salvar aqui, que ela vai fazer a criação.

05:49

Aparentemente travou a criação aqui.

05:51

Não, não tinha travado não. Só demorou um pouquinho para criar.

05:55

Dei um pause aqui até criar e voltei.

05:58

Faltou só um ponto que a gente tinha que

06:00

colocar o prompt para ela conseguir fazer o procedimento aqui.

06:07

Então, aqui tem o detalhe, tá? Do que ela deve fazer.

06:12

As instruções, né? Tá escrito aqui instruções.

06:16

Número 2 aqui.

06:18

Número 3.

06:21

Temos aqui a número 4. Número 5.

06:27

Instrução número 5.

06:31

Essa é a 5. Não,

06:35

a 5 tá aqui. Essa aqui não é a 5, não. A 5 está aqui na frente, a instrução.

06:42

O número aqui a gente tem a 6, a

06:46

número 5 tá aqui, simplesmente esse que é o

06:50

próprio sistema, tá, gente, que a gente vai criar

06:53

e acabou. Temos seis instruções aqui para ela seguir.

06:58

Vamos salvar e a gente pode executar ela aqui.

07:02

Agora vamos fazer execução. Ó, execução iniciada. Que que

07:06

é essa execução? Tá, ela vai iniciar um novo chat.

07:10

Aqui para mim com toda a instrução lá

07:13

Colocou tudo certinho,

07:14

Agora ela vai fazer essa execução para mim de 5 em 5 minutos, tá bom?

07:22

Isso é bacana porque a gente consegue deixar esse cara rodando de 5

07:27

em 5 minutos para fazer um check para a gente do que está acontecendo.

07:33

Então ele está fazendo esse check aqui e fazendo a validação,

07:36

usando lá o Prometheus, usando os logs de dentro do Kubernetes.

07:42

Fazendo algumas ações lá para a gente conseguir pegar esse funcionamento.

07:46

Deixa ele terminar de rodar aqui e a gente já vê o que está acontecendo.

07:49

Vamos voltar aqui em automações. Eu vou desativá-la por enquanto,

07:54

tá? Para ela não ficar rodando aqui e consumindo recursos.

07:56

Mas enquanto isso, vamos criar as outras automações aqui.

08:00

Então a gente tem um SLO Monitor. Vamos criar uma nova automação.

08:05

Essa aqui é a descrição dela. Descrição não, o título dela, né? SLO Monitor.

08:12

A gente aqui vai ter uma descrição dela.

08:14

Então aqui a gente tem uma descrição. E

08:18

aqui a gente vai ter uma lista

08:23

de tarefas que ela deve fazer.

08:25

Naquele mesmo esquema de várias coisas ali de tarefa.

08:30

O que ela vai usar?

08:32

Ela vai usar também o SRE Trash Roller.

08:36

E ela vai executar personalizado de 15 em 15.

08:44

Vamos colocar aqui. Vamos

08:49

colocar aqui para executar de 15 em 15 minutos e criar.

08:53

Vou dar um pause aqui no vídeo até ela criar e já retorno.

## Resumo IA

[RESUMO_IA]