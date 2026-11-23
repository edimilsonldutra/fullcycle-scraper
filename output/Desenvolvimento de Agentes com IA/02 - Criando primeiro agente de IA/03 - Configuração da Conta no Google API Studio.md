Módulo: Desenvolvimento de Agentes com IA\
Aula: [Configuração da Conta no Google API Studio](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/290/conteudos?capitulo=290&conteudo=18094)

## Resumo da aula



## Transcrição

00:00

Nesta aula, nós vamos configurar uma conta do Google para que nós possamos usar

00:04

os modelos do Gemini para ser a base dos nossos exemplos práticos.

00:11

Nós vamos utilizar isso durante todo o curso.

00:13

Mas você pode utilizar os seus modelos também.

00:16

Se você tem algum budget ali na Anthropic, na OpenAI,

00:22

esteja à vontade para utilizar. Mas o Gemini já disponibiliza modelos...

00:27

de forma gratuita. Tem um free tier tanto para uso desses modelos,

00:30

para o Gemini CLI e para outras coisas também.

00:34

Essa parte que eu estou logado com a minha conta é o AI Studio,

00:39

que equivale ao Cloud AI ou ao ChatGPT,

00:42

em que você consegue fazer os seus prompts, mas de uma forma mais especializada,

00:48

porque aqui dá para trabalhar com quantificação,

00:51

geração de imagem e outras coisas. Você consegue acompanhar...

00:55

o uso da sua conta, quantos tokens estão sendo utilizados,

00:59

qual é o gasto, se você está cometendo erros,

01:03

enfim, você tem vários relatórios e

01:07

diagramas para informar o que está acontecendo.

01:12

Então basta que você tenha a sua conta do Google,

01:15

não é necessário fazer mais nada, é só acessar o ai.google.com.

01:20

Aqui em Dashboard, nós vamos ter acesso às chaves de API.

01:27

Os projetos, uso, limite de taxa, gasto,

01:31

faturamento e mais um monte de outras coisas.

01:33

Você gerencia tudo aqui. Para acessar os modelos do Gemini,

01:36

é necessário ter um projeto.

01:38

Em cima do projeto que nós temos o faturamento,

01:40

quais modelos foram utilizados, os erros que aconteceram,

01:45

enfim. Então, se não aparecer um projeto para você, já crie um projeto novo.

01:50

Dependendo do nível da sua conta,

01:51

também vão ter restrições do número de projetos a serem utilizados,

01:55

exatamente porque é caro para a gente,

01:57

mas para quem está provendo a infraestrutura também. Então,

02:00

eu vou utilizar essa conta que aqui está.

02:04

Em limite de taxa,

02:05

nós conseguimos entender um pouco como funciona o free tier do Google,

02:10

porque nós temos ali o Admin ICLAI,

02:12

que tem até um certo ponto gratuito,

02:14

o uso dos modelos aqui até um certo ponto é gratuito também.

02:17

A minha conta é nível 1, que é o primeiro nível de pagamento depois do free tier.

02:23

Então eu criei ali uma conta de faturamento e coloquei o meu cartão

02:27

de crédito para que eu pudesse usar modelos que não são somente os gratuitos.

02:34

Nós temos os modelos Flash da

02:37

versão 2 e 3 que são gratuitos.

02:40

Então qualquer um desses modelos Flash você não vai ser cobrado.

02:44

Mas nós vamos ter limitações em

02:48

quantas requests por minuto podem ser feitas e também no número de tokens.

02:53

Na verdade, essa tela está um pouco maior,

02:55

dá para reduzir um pouco mais aqui e eu tenho outras informações.

03:03

Ao colocar a comparação com o nível gratuito,

03:06

então veja que a minha

03:08

conta permite mil requests por minuto.

03:13

Enquanto no gratuito ele vai permitir apenas cinco.

03:20

Então você não vai poder fazer mais que cinco chamadas por minuto.

03:24

Com os modelos Flash nós já conseguimos testar e estudar muito bem,

03:30

mas se você quiser mais variedade e aprofundar mais,

03:35

eu recomendo que você suba para o nível 1, que vai te dar uma vazão melhor.

03:41

E aí você pode continuar utilizando os modelos Flash nos momentos oportunos,

03:45

porque são os mais baratos,

03:47

eles vão ter um custo por milhão de tokens na casa de centavos de dólar.

03:54

É um momento novo que nós estamos vivendo,

03:57

então é preciso organizar muito bem o ambiente que nós vamos utilizar.

04:03

Na parte de gasto,

04:05

nós conseguimos ver o gasto mensal e definir um custo máximo.

04:10

Assim você não tem surpresas. Isso já aconteceu comigo.

04:13

Eu rodei uma bateria de testes com os agentes e na

04:17

verdade estava com o modelo Pro e aí depois ele acabou.

04:22

Elevando o custo, mas como eu tinha definido uma trava,

04:25

não passou daquilo, eu fui lá e fiz a correção.

04:28

Então isso é muito comum. Então é importante colocar essas travas,

04:32

essa segurança, para que a gente não tenha surpresas depois.

04:36

Então a questão é que nós podemos utilizar de forma gratuita,

04:41

eu vou sempre mostrar os exemplos permitindo que você rode dessa forma.

04:47

Mas aqui já vai também uma dica em relação a essa questão de custo cunhar.

04:51

Eu vejo muitos profissionais de tecnologia querendo

04:55

não gastar nada, se apegando à forma antes de trabalhar,

05:00

que você trabalhava com mais ou menos custo 0,800 para tudo.

05:04

É um momento novo que nós estamos vivendo.

05:06

Se você quer de fato testar essas ferramentas, e não só aqui o Gemini CLI,

05:11

outros serviços também que envolvem a inteligência artificial do Google,

05:15

você vai ter que gastar alguma coisa.

05:17

O ponto é que tem que ser dentro da sua realidade,

05:21

conforme o que você vê que é bom para você.

05:26

Mas nós não devemos ter medo de ter esses gastos,

05:29

porque vai ser com o acesso a

05:33

outras ferramentas que nós vamos conseguir estudar,

05:36

entender mais e evoluir.

05:39

Então fica a dica sobre isso. Mas nós vamos utilizar sempre os modelos Flash.

05:46

Para que nós possamos desempenhar o nosso trabalho. Então,

05:49

voltando aqui para a parte do projeto,

05:52

eu tenho essa chave de API que eu posso colar e colocar lá no meu arquivo de .env.

05:59

Então, nós vamos criar aqui um .env example com

06:05

uma

06:07

Google API Key com o valor que eu vou colar aqui depois e

06:14

um .env,

06:17

que não vai estar no controle de versão.

06:19

Então eu vou colocar o .env para ser ignorado,

06:23

senão eu acabo colocando no repositório que vai ficar acessível para vocês.

06:28

Então você vai pegar aquele token e colocar exatamente aqui.

06:33

E com essa configuração feita,

06:35

agora nós vamos partir para a configuração do SDK.

## Resumo IA

[RESUMO_IA]