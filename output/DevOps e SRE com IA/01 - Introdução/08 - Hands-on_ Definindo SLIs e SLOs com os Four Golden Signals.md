Módulo: DevOps e SRE com IA\
Aula: [Hands-on_ Definindo SLIs e SLOs com os Four Golden Signals](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/295/conteudos?capitulo=295&conteudo=18520)

## Resumo da aula



## Transcrição

00:00

Estimativa de custo, que era o último que a gente tinha falado.

00:03

Baseado no cálculo, GCP é 2, AWS M6 e assim por diante.

00:08

Ele fez uma estimativa bacana de custo aqui.

00:11

Nenhum orçamento de time documentado. Impossível comparar. Então,

00:15

ele não conseguiu fazer nenhuma comparação. Então,

00:17

vamos lá. Vamos validar. Temos as cinco categorias.

00:21

No final, a gente tem o veredito.

00:24

Então, brocas críticas, ele fala aqui de várias coisas sobre o veredito.

00:30

Condições para ready, estiver pronto para produção,

00:32

ele tem que arrumar tudo isso aqui, documentar o budget,

00:36

documentar a SLO e assim por diante.

00:40

Então, checklist completo e aqui algumas coisas que ele validou.

00:44

Qualquer outra coisa aqui, itens de segurança,

00:46

menciona o non-route, vamos lá, vamos validar o item de segurança ali em cima.

00:52

Menciona o...

00:54

No root, está escrito aqui, no root, está escrito,

00:57

porque a nossa imagem tem o no root lá para ele

01:00

não rodar o container com o root lá dentro.

01:03

Então a gente tem o network policy,

01:05

está aqui aplicada, bonitinho, e o trivia,

01:09

que é a parte aqui de imagem escaneada. Nenhum papilhagem de CSD,

01:13

porque a gente não construiu ainda,

01:15

então algumas coisas ele deu pau aqui para a gente, legal?

01:21

Itens de recursos, vamos ver se ele menciona aqui nos recursos o HPA,

01:25

CPU Request Limit está aqui, Memory Request Limit,

01:29

e o HPA. Está com exclamação e está com interrogação aqui,

01:33

porque não escala a latência de P99.

01:37

Então, provavelmente foi alguma coisa que ele...

01:40

construiu um pouco errado lá. Então,

01:44

por isso que é sempre bom a gente sempre rever o que ele constrói,

01:47

porque algumas coisas podem não bater.

01:50

E a estimativa de custos de itens corretos, mesmos aproximados.

01:55

Então, ele criou para mim a estimativa de custo aqui, mais ou menos.

01:59

Claro que ele não tem nenhum orçamento para seguir,

02:01

etc. Mas ele criou aqui uma estimativa de custo usando a AWS e usando o GCP.

02:07

Ok? On demand e...

02:10

Então está criado aqui um custo mais ou menos que a gente vai gastar. Legal.

02:15

Aqui tem um resumo do que ele criou. Segurança, recursos,

02:19

observabilidade, custo total e a porcentagem que está atendendo.

02:22

Então a gente tem um resumo aqui executivo que a gente pode mostrar para o pessoal,

02:25

para a equipe, etc. Então o checklist completo acima,

02:29

score 10 de 25, 40% not ready.

02:33

Então ele falou que a aplicação não está pronta para o ambiente de produção. Legal.

02:40

Então, assim funciona uma skill. Então, toda vez que você mudar a sua aplicação,

02:45

você pode dar um comando /skill que ela vai conseguir avaliar para você tudo do

02:51

seu código para te falar se está pronto para

02:53

produção ou não está pronto para produção.

02:55

Então, o checklist aqui é super importante para

02:59

validar todas as etapas do que a gente constrói.

03:03

Então, isso é uma das possibilidades que a gente tem de skill.

03:08

A outra possibilidade que a gente tem de skill é a parte de SLI e SLO mapping.

03:13

Bacana? Então, o que é o SLI e o SLO mapping aqui na nossa parte de skill?

03:20

O que a gente vai ter aqui na parte de SLI? Então,

03:25

vai ter uma descrição de input de serviço,

03:27

vai ter um tipo de workload, que é API, Bash, etc.

03:31

O output vai ser o SLI com os Golden Scenarios que a gente falou lá atrás,

03:36

que é o Latency, Traffic, Error e Saturation, SLO, percentuais com justificativa,

03:43

um Error Budget derivado e os alertas de Thresholds sugeridos aqui.

03:47

Então, a gente vai criar mais uma skill aqui para a

03:51

gente conseguir fazer a geração desse SLI e SLO mapping aqui.

03:58

Como sempre, eu tenho aqui já a skill construída,

04:01

vamos trazê-la aqui para o nosso contexto.

04:04

Vamos puxar ela aqui, jogar aqui para dentro do nosso serviço, dentro

04:11

de skills, e aqui a gente tem a skill de SLI e SLO.

04:16

Aqui as definições dela, vamos puxar um pouquinho.

04:19

O que a gente tem de definição aqui?

04:20

Vou fechar essa tela, vai ficar mais fácil. Isso.

04:23

Você é o SLI responsável por definir SLI e SLO para serviços em produção.

04:29

Dada a descrição do serviço, mapeio para Golden Sign-ons e assim por diante.

04:35

E aqui é uma descrição do serviço e as instruções do que ele deve preencher.

04:42

SLO, SLO e assim por diante. Cálculo de erro budget,

04:48

alerta de thresholds e

04:53

aqui os formatos de saída. Definir também.

05:00

Derivação dos erros do budget, os alertas, etc.

05:04

Alerts, thresholds detalhados e recomendação de instrumentação.

05:08

Então, ele vai conseguir te mostrar até as partes de monitoramento, tá?

05:12

Se você colocar essa skill aqui até em outros serviços,

05:15

você consegue reutilizar e tem como no OpenCode,

05:19

por exemplo, você consegue colocar ela de maneira global.

05:21

Eu estou colocando aqui dentro do serviço para

05:23

facilitar e a gente ter a visualização.

05:25

Mas tem como você colocar ela de maneira global,

05:27

onde você pode usar ela em qualquer projeto seu. Então, usando um projeto,

05:32

ele vai lá e gera para você toda aquela parte de skill.

05:35

Basta você abrir o OpenCode dentro daquele projeto. Aqui para baixo,

05:39

a gente tem aqui um exemplo desse carinha preenchido com essa descrição do serviço. Então,

05:45

API REST 3.11 com FastAPI, 3 endpoints, bancos de dados,

05:49

postings e assim por diante, toda a descrição que a gente já falou.

05:52

E aqui a gente já tem a nossa skill definida.

05:55

Salvei a nossa skill. Vou fechar. Vou fechar aqui.

05:58

E aqui eu vou basicamente fazer aquele mesmo esquema.

06:02

Vou fechar o OpenCode e abrir ele de novo dentro do repositório. Ok? Downbar Skills.

06:09

E agora a gente já tem aqui o SLI e o SLO Map.

06:13

Então, vamos rodar ele aqui e vamos ver o resultado. Isso.

06:21

Aqui ele já manda todo o prompt e agora ele já começa a construir

06:25

toda a parte de SLI e SLO mapping que está definido dentro daquela skill.

06:31

E o bacana é, a gente consegue utilizar em qualquer projeto,

06:35

qualquer pessoa pode conseguir utilizar e

06:37

pode reutilizar em outros projetos qualquer,

06:42

sempre seguindo as mesmas diretrizes.

06:45

Se você é um DevOps, você consegue definir.

06:48

Colocar isso dentro do software que você usa como padrão

06:51

para desenvolvimento com AI dentro da sua empresa e usar globalmente.

06:56

Legal? Então,

06:58

o que a gente tem aqui, pessoal? A tela de resumo com latência,

07:02

burn rate e assim por diante. A gente tem o tráfego.

07:06

Tem várias coisas aqui que a gente pode avaliar.

07:10

Vou pegar a listinha aqui para a gente avaliar.

07:13

Então, basicamente, a gente vai ter uma tabela com quatro linhas aqui. A gente tem...

07:19

com o For Golden Signals, que a gente tem um P99 de latência,

07:25

que está definido. Serial Target,

07:27

Alerta Threshold e o Error Budget

07:29

aqui de 43,2 minutos mensal.

07:35

E o Error Budget Diário,

07:38

a gente pode ter no máximo 86,4 segundos de indisponibilidade.

07:44

O Tráfego, aqui a gente tem

07:48

Toda a parte aqui de requests por segundo.

07:50

O drop aqui de 5 minutos e assim por diante. Ele gera bonitinho aqui.

07:54

Os erros em HTTP 500 rate. Ele não pode ser maior do que 0,1%.

08:01

E tem um rate de 0,5 minutos.

08:07

CPU utilization e assim por diante que mostra toda a parte aqui da tabela.

08:11

O SLO de disponibilidade de 99% com erro budget de 43 minutos.

08:16

Está aqui. Está disponível aqui,

08:18

alerta de host born com rates de 14,46,

08:23

está tudo aqui, o budget mensal, todas as partes escritas aqui para esse serviço,

08:30

o alerta de host, warning e critical, 50% do budget consumido,

08:35

ele vai ter um born rate aqui de 14,4x e janela de 5 minutos,

08:41

se mantido por 5 minutos. Consume metade do budget mensal.

08:44

Então, tem algumas regras aqui que vão definir

08:47

a parte do nosso budget mensal para esse serviço,

08:52

quanto que ele pode parar por mês.

08:54

Então, basicamente, a gente tem todas as partes aqui,

08:57

tudo feito por AI, tudo feito com a generative AI,

09:00

que facilita bastante a nossa vida para desenhar,

09:05

fazer um documento desse que é bem complexo no nosso dia a dia de DevOps.

09:12

Assim, a gente finaliza a parte aqui de skills. Bacana? Então,

09:16

falando um pouco aqui do nosso hands-on que a gente passou,

09:20

a gente passou aqui por várias partes, né?

09:24

A gente criou a aplicação Unicornic App Main

09:29

.app que a gente criou lá no começo, já está criado na real,

09:33

né? Já está tudo definido e a gente fez a geração do Dockerfile para ela.

09:37

A gente inspecionou a aplicação, fizemos tudo, geramos o Dockerfile,

09:42

que é aquele prompt de Dockerfile.md,

09:47

validamos, fizemos o build e testamos.

09:49

Geramos o Docker Compose, subimos o Docker Compose dentro da nossa máquina local,

09:55

isso rodou lá, funcionou perfeitamente.

09:59

Geramos o K8s Manifest,

10:01

a gente fez a geração dos manifestos do Kubernetes e

10:05

aplicamos dentro do nosso K3d para fazer a validação do serviço.

10:12

Fizemos alguns prompts com o Rambook,

10:15

a gente usou o prompt para gerar um Rambook de

10:18

recuperação do serviço e fazemos os testes aqui.

10:21

Faltou a parte de docs também, a gente gerou a doc.

10:25

Faltou aqui, come bola, a parte de dock.

10:29

Geramos também as docks completas do serviço e fizemos duas skills aí

10:34

que podem ser reutilizadas em vários outros serviços por toda a equipe.

10:41

Então, para cada passo, se você perder algum passo,

10:44

volta, termina, vai fazendo esses labs hands -on aí,

10:48

que é muito importante para você entender todo o processo.

10:51

Legal? Um fluxo aqui do que a gente gerou.

10:56

desde o início dessa aula,

11:00

a gente conseguiu acompanhar os apps mais SLA,

11:04

vimos um pouco de prompt, vimos o LLM funcionando aqui com o OpenCode Go,

11:10

que é a licença do OpenCode para você usar vários modelos bacanas.

11:15

Então a gente conseguiu gerar vários artefatos,

11:18

validamos a geração dos artefatos e validamos até a execução dele. Legal?

11:24

Então, essa parte bacana que o LLM ajudou

11:27

a gente bastante na geração desses artefatos.

11:34

Seguindo aqui, sempre valide. A mensagem sempre é essa.

11:37

Desde o início eu sempre falo isso, sempre valide. Então, gera o doc file,

11:42

valida. Gera os manifestos Kubernetes, valida.

11:46

Gera os handbooks, leia tudo e valida.

11:49

Ele vai gerar um rascunho qualificado, que é chamado.

11:53

que não é a informação final, não é o serviço final que vai estar ali,

11:58

mas é boa parte das coisas montadas.

12:01

Então, sempre valido. O LLM pode alucinar,

12:04

pode entregar coisas que não estão de acordo com o seu ambiente,

12:09

de acordo com a sua empresa, com as suas regras de negócio, etc. Então,

12:15

sempre tente pegar as suas regras de negócio,

12:17

trazer para dentro do contexto do LLM e sempre valide.

12:22

todas as partes que você for gerar usando o LLM. Combinado?

12:27

E um resumo aqui do módulo 1. Já falei lá,

12:31

mas vamos falar um pouquinho de novo aqui.

12:33

Fizemos alinhamento aqui do que é DevOps e SRE. Legal. Geramos alguns Docs Files. Alguns não, né?

12:41

Geramos um Doc File para o nosso projeto que a gente já tinha definido.

12:44

Geramos um Doc Compose para esse mesmo projeto.

12:47

Geramos um K8S Manifest. que é um Kubernetes manifesto aqui para o projeto.

12:52

E todos esses aqui a gente conseguiu colocar para rodar.

12:56

Então a gente gerou e ainda mostrou ele rodando.

12:59

Bacana? Geramos um runbook e geramos um docdesign.

13:03

Esses dois carinhas vão ser super importantes para o projeto lá no final,

13:07

porque a gente vai fazer consulta neles para fazer a validação de algumas coisas.

13:12

Então validar se o serviço está de pé, se ele caiu, etc. A gente vai...

13:17

consultar esses serviços.

13:18

E a gente construiu 12 skills aqui que a gente pode reutilizar,

13:22

não só nesse projeto, mas em outros projetos também.

13:26

Então, no próximo módulo, a gente vai começar a falar um pouco de CI e CD.

13:30

Então, a gente vai automatizar tudo isso que a gente fez manualmente,

13:33

de gerar o Dockerfile, gerar a imagem, subir os arquivos dentro do Kubernetes,

13:40

etc. A gente vai automatizar isso numa esteira de CI e CD.

13:44

Com as ações do GitHub e Agents .GI.

13:49

A gente vai ter um orquestrador de segurança,

13:53

a gente vai passar esse cara por um filtro de segurança lá dentro da nossa pipeline.

13:58

A gente vai fazer um code review assistido usando o OpenCode também,

14:02

alternativo para o OpenCode Copilot.

14:05

A gente vai fazer um prompt version usando o LLMs Duddy.

14:09

Então a gente vai conseguir versionar os nossos prompts agora. Então,

14:13

a gente tem vários prompts aqui que estão soltos.

14:15

Então, a gente vai conseguir versioná-los.

14:17

A gente vai conseguir criar eles e versionar. Então,

14:20

a gente vai ter um supply chain security que a gente vai

14:23

conseguir fazer a validação de segurança de todas as partes aqui. Ok, pessoal?

14:29

Então, é isso. Foi uma aula bem grandinha aí. A gente falou bastante coisa.

14:34

Eu acho que a gente entendeu muita coisa aí do que é um pouco do DevOps,

14:40

um pouco de SRE.

14:41

E a gente segue aí para o módulo 2 de CI e CD,

14:45

para a gente falar um pouco mais de pipeline.

14:48

Um abraço para todos, fiquem em paz e façam o teste,

14:53

se der errado, mate de novo o serviço,

14:56

sobe de novo e continuem testando aí, pessoal.

15:00

Muito obrigado e tenham uma boa noite, um bom dia ou uma boa tarde.

## Resumo IA

[RESUMO_IA]