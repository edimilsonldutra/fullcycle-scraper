Módulo: Protocolos de Comunicação\
Aula: [LAB: Servidor do Zero parte 1](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18604)

## Resumo da aula

O primeiro servidor MCP de um time tende a virar referência informal para os próximos. Por isso, a qualidade do template inicial importa mais do que a ergonomia superficial do decorator. Um servidor saudável nasce quando segurança, semântica de erro, logs e testes já aparecem no primeiro pull request. Essa disciplina evita que o padrão replicado pelo time normalize falhas operacionais difíceis de corrigir depois.

Finance Admin é um servidor pequeno, mas com responsabilidade de negócio explícita: operar sobre dados financeiros reais e rejeitar ações fora da política da empresa. O objetivo não é construir um produto completo, e sim um recorte suficiente para exercitar integração com banco, modelagem semântica de capabilities e guardrails de reembolso. Esse tipo de escopo é útil porque aproxima o laboratório de um serviço corporativo sem diluir o foco em detalhes periféricos.

Linhas de código medem custo de autoria e ajudam a avaliar a DevEx do FastMCP em um servidor útil, não apenas em um exemplo mínimo. Tempo até a primeira tool conectada ao Streamlit mede atrito de setup, que em times reais costuma se converter em manutenção lenta e onboarding ruim. Cobertura mínima, latência baixa e proporção de erros tipados completam o quadro porque mostram se o servidor é operável, testável e semanticamente previsível.

O script verify_lab.sh concentra a validação do ambiente antes de qualquer depuração de protocolo. Ele existe para separar falhas de infraestrutura — como container indisponível, banco vazio ou testes quebrados — de falhas do servidor MCP em si. Essa ordem reduz ruído operacional: primeiro Docker e dados, depois servidor e integração. Em produção, inverter essa sequência faz o time perder tempo investigando protocolo quando o problema ainda está na base do ambiente.

Retomando o uso de FastMCP já estabelecido, a tool não deve misturar contrato de protocolo, regra financeira e persistência no mesmo bloco. O servidor importa funções de domínio como buscar_pedido e registrar_reembolso_bonificado, enquanto a camada MCP fica responsável por expor capability, validar entrada e traduzir falhas para o protocolo. Essa divisão reduz acoplamento e permite testar a regra de negócio com muito mais precisão. Quando tudo fica dentro do handler, a manutenção degrada rapidamente.

A regra central do domínio é simples e rígida: o bônus de retenção não pode ultrapassar 20% do valor do pedido. Essa trava existe para impedir que o agente transforme uma capability legítima em um canal de perda financeira. O ponto importante não é apenas barrar o valor excessivo, mas barrá-lo de forma semanticamente interpretável. A política da empresa vira código executável e auditável, em vez de depender de instrução textual solta para o modelo.

Quando o valor pedido viola a política de 20%, a rejeição correta é um MCPError com invalid params, e não um raise genérico. Esse erro comunica ao host e ao agente que a falha era previsível, ligada ao contrato de entrada e à política operacional, não a uma pane interna. O efeito prático é decisivo: o agente consegue reinterpretar a situação, responder com clareza ao usuário e evitar comportamento errático. Em servidores financeiros, erro tipado é parte da regra de negócio, não apenas detalhe de implementação.

O resource cancelamentos/motivos publica leitura controlada sobre perdas financeiras sem abrir espaço para consultas arbitrárias. Em vez de deixar o agente “pesquisar” no banco por meio de uma tool genérica, o servidor entrega um estado já empacotado, estático e seguro. Isso reduz superfície de risco e mantém a semântica correta: leitura idempotente continua sendo resource, não ação disfarçada. A modelagem protege o banco e simplifica o raciocínio do agente.

O prompt financeiro não executa nada; ele enquadra a intenção do agente antes da execução. Ao embutir persona, objetivo analítico e diretriz de quando usar a tool de bônus, o servidor transforma política interna em orientação operacional reutilizável. Esse desenho reduz improviso do modelo e melhora consistência entre diferentes execuções. Retomando a distinção já conhecida, a tool age, o resource informa e o prompt orienta.

A integração com Streamlit materializa o servidor em uma interface real, enquanto o agente consome o catálogo MCP via LangChain. O fluxo relevante é observar leitura do resource, decisão guiada pelo prompt e tentativa de ação pela tool, tudo visível por logs e comportamento da interface. Quando o agente tenta oferecer R$ 150 em um pedido de R$ 350, o servidor bloqueia a operação porque o limite permitido é R$ 70. O valor pedagógico dessa integração está em mostrar que o guardrail continua valendo mesmo quando a decisão parte de um sistema agêntico.

Em ambiente corporativo, a confirmação final da segurança não vem do chat, mas dos testes automatizados. O servidor precisa provar que entradas maliciosas ou fora da política geram exatamente o erro esperado, sem tocar indevidamente o banco. Cobertura alta não é vaidade numérica nesse contexto; ela funciona como evidência de que a regra financeira continua protegida durante a evolução do código. Quando a tool é a parte determinística do agente, é nela que a suíte de testes precisa ser mais rigorosa.

## Transcrição

00:01

Pessoal, essa aula marca uma mudança importante no curso do

00:06

ponto de vista de que até agora vocês me viram fazendo.

00:09

Então, vocês entenderam o que é o MCP,

00:14

a gente fez várias implementações,

00:18

tanto em TypeScript quanto em Python,

00:22

só que agora vocês vão construir o servidor MCP do zero.

00:27

E ele vai continuar no mesmo esquema de usar o banco de dados real, que é o PostgreSQL,

00:31

validar regras de negócios financeiras e travar ações não permitidas usando MCPR, por exemplo.

00:39

Então, a ideia aqui é que vocês tentem experimentar

00:42

o mais próximo possível de algo real,

00:46

do ponto de vista, pelo menos,

00:48

de conceitos e de semântica das primitivas do MCP.

00:58

O roteiro é quebrado em partes pequenas, como nas outras vezes. Ou seja,

01:02

etapa 0 é subir a infraestrutura do banco de dados,

01:04

relacionar e rodar o script de verificação.

01:08

Essas informações, pessoal, vocês conseguem lá no Readme. Depois,

01:13

etapa 1 e 2, que é o esqueleto do servidor.

01:16

Um resource para expor dados de cancelamento de forma segura

01:20

e um prompt para guiar o agente financeiro.

01:23

Na etapa 3 entra a ação de fato, então vamos criar a ferramenta de

01:27

reembolso com validações estritas de negócio, então o

01:30

nosso agente ele não pode simplesmente gastar

01:34

dinheiro ilimitado, então na etapa 4 nós conectamos tudo no ambiente real, né? E

01:40

aí eu vou usar aqui, pessoal, uma tecnologia que chama Streamlit, super fácil de usar,

01:44

Já vou deixar tudo pronto ali para vocês, tá? Inclusive o passo a passo. De novo,

01:49

como a gente no hands-on passado introduziu o tema do LangChain super rápido,

01:54

eu acho que o Streamlit também é uma tecnologia super fácil de vocês usarem, tá?

01:58

De novo, se vocês tiverem curiosidade, dê pausa aqui no vídeo,

02:02

dá uma pesquisada do que é o Streamlit em Python, tá?

02:05

Vocês vão entender que é quase como se fosse uma forma de gerar um front-end em Python,

02:09

tá? Mas enfim, vamos lá então. Bem...

02:15

Aqui, a tese... Então, olha só. A gente precisa desacelerar um pouco.

02:20

Agora, nesse slide aqui. A fase principal é essa.

02:24

Disciplina de protocolo. Então, o template,

02:26

imagina que é o primeiro pull request que vocês vão fazer dentro do time de vocês,

02:32

que no final do dia, a partir do momento que vocês sobem o primeiro servidor,

02:36

isso meio que vira uma convenção do time.

02:38

O que significa na prática? Que o primeiro servidor MCP que o time constrói...

02:42

quase sempre vira referência, tá? Isso é humano, tá?

02:45

Então, mesmo sem decisão formal, beleza? Então,

02:48

o padrão nasce no primeiro pull request e depois começa a ser replicado e,

02:52

obviamente, refinado, melhorado, enfim.

02:54

E a tese aparece aqui de forma bem direta, ó.

02:57

Servidor do zero em produção tem disciplina de protocolo.

03:00

Não é o decorador que faz o servidor bom,

03:02

é como você garante segurança, trata erro e gera log, tá?

03:07

O decorador é importante, eu tenho dúvida, tá, gente?

03:10

Ele expõe a ferramenta, Ele expõe a sua, é visível, fácil de demonstrar, claro, no código.

03:16

Mas produção normalmente não quebra por causa do decorador.

03:19

Ele quebra quando um erro de negócio, como um bônus financeiro muito alto,

03:23

Passa batido. Então, quando o erro vira texto solto no console, por exemplo,

03:27

quando falta log para entender o que o agente tentou fazer,

03:31

ou quando o host recebe uma falha sem semântica clara, aí que tem um problema.

03:36

Então é o seguinte, pessoal, vamos dar uma olhada aqui.

03:39

Esse é o vocabulário de produção que o Lab vai aplicar.

03:42

Type hints virando esquema do FastMCP.

03:46

MCP é erro tipado,

03:49

atuando como trava de segurança financeira no lugar de um raising genérico.

03:53

Logs estruturados e cobertura mínima de testes como guardrail.

03:57

De novo, pessoal, eu vou entregar muito código para vocês,

04:02

para vocês não começarem do zero, porque o foco de fato...

04:05

é vocês irem preenchendo os

04:07

gaps da implementação para poder ficar

04:13

cada vez mais familiarizado com todos os pontos que eu trouxe aqui.

04:19

Então vamos lá.

04:22

Vamos pensar como seria uma revisão, por exemplo, do pull request.

04:29

Se eu vejo uma tool que emite dinheiro sem travas claras no protocolo,

04:33

eu não estou olhando só estilo.

04:35

Estou olhando para um risco real na empresa.

04:37

Se eu vejo um velho erro genérico em vez de um MCP de erro,

04:40

de inválido de parâmetros,

04:42

por exemplo, que vocês viram, eu estou olhando a experiência do host e do modelo,

04:46

que vai ficar confuso ao receber aquela falha.

04:53

Pode aplicar essas exatas substituições no seu arquivo

04:56

e a narrativa dos próximos slides,

04:58

vocês vão ver que ficará perfeitamente casada com a nossa tool de reembolso.

05:03

de fato no Lab quando vocês estiverem desenvolvendo.

05:08

Bem, agora a gente transforma a tese da aula em objetivo mensurado.

05:15

Repara só, pessoal.

05:17

O que você vai construir é um servidor MCP chamado Finance Admin. Ele expõe tools,

05:23

resources, prompts e usa o vocabulário de produção que a gente acabou de discutir.

05:27

MCP erros e logs estruturados, operando em cima de um PostgreSQL real.

05:32

por exemplo, e no final esse escopo importa, óbvio,

05:37

a gente não está construindo um produto inteiro, isso é claro,

05:41

a gente está construindo um servidor pequeno o suficiente para caber no lab,

05:44

mas focado o suficiente para exercitar problemas

05:46

reais de integração de regras de negócios estritas.

05:53

Então, olha só pessoal, vou pegar aqui as métricas que vocês precisam ter em mente.

05:59

pontos que vocês precisam ter em mente, que é importante validar. Então,

06:02

a primeira é a linha de código. Parece simples,

06:08

mas mede o DevEx, o Developer Experience.

06:11

Então, quanto código realmente é necessário para expor um

06:15

server útil e seguro usando o FastMCP?

06:17

A segunda é o tempo até a primeira sua aparecer e conectar nesse lead.

06:22

Isso mede a tria inicial. Em time real,

06:24

setup complicado normalmente vira o turnaround ruim depois.

06:28

A terceira, pessoal, métrica é a cobertura de teste.

06:32

O alvo aqui é ser maior ou igual a 80%.

06:34

A cobertura aqui não é fetiche de número, é guarda-rail de fato.

06:39

Se a gente lida com o reembolso financeiro,

06:41

o código não pode evoluir sem teste. E lembra, pessoal,

06:44

as tools é a parte determinística de um agente. Lembra disso.

06:50

A parte não determinística é LLM. Então, nós devemos testar...

06:56

e fazer testes bem robustos em cima das tools. Bem,

07:03

se a gente repara nesse campo de menos de 10 mil segundos que eu trouxe aqui, pessoal,

07:10

se a validação financeira da tool for lenta,

07:13

o Strelitz vai travar e a percepção que o modelo,

07:15

que o LLM no caso, tem do seu servidor muda imediatamente.

07:19

E a quinta métrica talvez seja a mais importante para a segurança de protocolo.

07:23

Erros chipados versus erros genéricos.

07:27

Quantos RAID de Python puro você converteu em um MC Peregrine em Vale de Paranhos?

07:32

Focado em política da empresa. Porque no fim,

07:34

não basta o server funcionar no caminho feliz.

07:37

E produção o que importa é como ele rejeita com clareza aquilo que não é permitido. Então vamos lá.

07:48

Aqui parece meio burocrático, pessoal,

07:50

mas a gente já falou isso várias vezes. Um laboratório técnico evita...

07:55

Mas em laboratório técnico você evita metade dos problemas.

07:58

São quatro frentes, pessoal. É simples, de novo.

08:02

Todos esses pontos que estão aqui, pessoal,

08:04

são basicamente as mesmas questões dos outros laboratórios.

08:08

Obviamente, a gente... Inclusive, dos rendes ontem.

08:15

Então, se não tem muito mistério,

08:16

vocês não vão ver aqui nada super mega novo, a não ser, de novo, o estrilite.

08:21

Então, enfim, pessoal. Só, de novo, se tiver curiosidade, dá uma olhada lá.

08:27

Para, dá pausa, entende o que é estrilite. Mas,

08:29

de novo, gente. Super fácil, super simples.

08:32

Aqui é mais para ter uma UI melhor do que um simples console.

08:38

A ideia aqui é simplesmente essa.

08:40

Bem, agora indo para a etapa zero, de novo, vamos lá.

08:45

Antes de construir o CVMCP,

08:46

a gente precisa garantir que as dependências estão saudáveis,

08:49

o banco relacional postigris funciona como a fonte

08:51

de dados do nosso setor financeiro.

08:53

E vale fixar uma coisa importante, você não precisa escrever a estrutura do banco.

08:57

Ela já está pronta no repo. E isso define a fronteira do lab.

09:01

A gente não está aprendendo o doc, o postgres agora, pessoal.

09:04

A gente está usando eles como dependência externa.

09:07

E essa é uma situação muito comum em produção.

09:09

O servidor MCP normalmente nasce no meio de sistemas pesados que já existem. Então,

09:14

olha o comando inicial. Nós simplificamos tudo em um único script.

09:18

Só para facilitar para vocês.

09:19

Verify underscore lab ponto sh.

09:23

Sugestão, pessoal, que é o shell script.

09:26

Sugestão... Dá uma olhada nele. Vê, assim, na verdade, deveria...

09:30

Agora que vocês estão começando a acostumar, tá?

09:32

Dá uma olhada nos comandos. Vê o que aparece lá. Vê o que dá para fazer.

09:35

Aliás, vê o que ele está fazendo, tá? E vê o que vocês não entenderam.

09:41

Dá uma pausa. Dá uma pesquisada, tá? De novo, nada complexo, tá?

09:46

Bem... O que

09:50

mais aqui, pessoal? O que é novidade? No final,

09:53

O resto é a mesma coisa, tá? Então...

09:58

Deixa eu ver que vale a pena aqui também. Olha lá. É importante.

10:04

Garantir que os testes do ambiente passem antes de ligar o MCP evita um erro brutal,

10:08

que é começar a debugar protocolo quando a infraestrutura ainda nem está válida.

10:13

Então, em ambiente real, isso acontece direto. Então,

10:17

o time acha que o problema está no MCP,

10:19

no SDK ou no Roche. No fim,

10:20

era um banco vazio ou um container Docker que não subiu. Então,

10:24

a expectativa aqui é objetiva. Docker está rodando,

10:27

banco populado e testes passando verde.

10:29

E se eu estivesse debugando esse lab em produção agora,

10:32

eu seguiria exatamente nessa ordem,

10:35

status do container, tabelas populadas e só depois o servidor MCP, tá?

10:41

Bem, não debugue protocolo, pessoal, antes de validar a infraestrutura, tá?

10:46

Esse aqui que é a grande mensagem desse slide.

10:49

Beleza. Aqui começa a construção do MCP Server de verdade, tá?

10:53

Repara nesse código aqui, tá, gente? A primeira linha importa o Fashion CP,

10:57

como a gente já viu no hands-on. Ela é pequena,

11:01

mas define bastante coisa. O SDK escolhido,

11:03

o estilo do servidor e a forma como as tools vão ser declaradas.

11:07

A gente está usando Python,

11:08

Decorators e Tapirins para transformar função de contrato de protocolo.

11:13

Função de contrato de protocolo.

11:16

De novo, não é novidade, é só para reforçar aqui.

11:19

Logo depois do código, importa buscar pedido e registrar reembolso bonificado.

11:24

Esse detalhe importa.

11:25

A TUR não implementa acesso direto a banco de dados nem update ali dentro.

11:29

Ela delega para funções de domínio. Isso parece simples,

11:32

mas melhora a manutenção. Quando regra de negócio,

11:35

protocolo e persistência ficam misturados,

11:38

o servidor cresce rápido e fica impossível de manter.

11:42

Na sequência, a gente cria a instância com o nome... é, é, financeadmin.

11:47

Repara nesse nome. Ele vai aparecer no host. Em ambiente real,

11:51

quando existem vários servidores conectados no mesmo cliente,

11:54

o nome genérico vira atrito, tá?

11:56

Então, o problema não é técnico, é cognitivo, tá, gente? É semântico, tá?

12:00

E aí vem o decorator de tool, tá? Ele expõe a função como tool para o host,

12:04

mas volta para a tese da aula.

12:06

O decorator não é o que faz o servidor ser bom.

12:09

Ela só torna a função visível. O que realmente importa aparece dentro da função.

12:14

A emitir reembolso bonificado, a função é emitir reembolso bonificado,

12:20

recebe o ID e valor do bônus. Repara nos type hints, pessoal, int e float.

12:26

O SDK usa isso para gerar esquema.

12:29

E a validação da trava de retenção financeira, os 20% de limite,

12:34

é o ponto mais importante do slide. Se o LLM tentar dar bônus maior que 20%,

12:40

o código levanta um MCP Error tipado com parâmetro inválido,

12:43

e uma mensagem detalhada de política de empresa.

12:46

Isso é diferente de deixar um

12:47

velho erro genérico escapar sem semântica. Lembrei disso.

12:55

Em produção, esse detalhe muda e implementa a interpretação do LLM. De novo,

13:01

A IA, que é a inteligência artificial,

13:03

ela tem as mesmas dificuldades semânticas que nós temos ao ler um texto.

13:08

Ou seja, porque ela recebe um texto,

13:09

ela precisa interpretar aquele texto. Então,

13:12

quanto melhor o contexto, quanto mais semanticamente correto,

13:16

melhor a interpretação, mais correto vai ser... Aliás,

13:21

vou colocar cheio de aspas aqui.

13:24

Mais determinística será a resposta. Quando eu digo mais determinística,

13:28

porque por natureza é não determinística. Mas, no final,

13:30

a gente aumenta a probabilidade de, pelo menos,

13:34

não ouvir uma resposta que a gente não queira,

13:36

ou de tomar uma ação que a gente não queira, que,

13:38

no final... É a velha desculpa de a IA alucinou.

13:41

Muitas vezes a IA não alucinou.

13:42

É a gente que não criou essas travas semânticas, tá bom? Bem,

13:46

vamos lá. Então, se mandarmos o MCPR explicando a política,

13:51

a gente se corrige no chat e responde educadamente

13:55

ao gerente que o valor não foi aprovado.

13:57

Então, o principal aqui é isso.

13:58

A primeira tu já nasce com segurança e protocolo explícito.

14:01

Se eu estivesse revisando esse PR,

14:03

pessoal, minha pergunta seria simples, tá?

14:05

Toda entrada inválida que gera perda financeira vira

14:09

erro de protocolo interpretável pelo agente?

14:11

Gente, toda vez que eu falar agente,

14:13

pensem em LLM, mais tools, mais memória, tá? Então assim,

14:18

do agente de A Generativa, sim, sim, o servidor nasceu saudável.

14:23

Tá bom. Etapa 2. Servidor ganha contexto passivo e direção ativa.

14:29

O ponto de partida é o decorreto de resource.

14:32

Repare na URI estáticas, cancelamentos, barra motivos.

14:36

Aqui existe uma distinção importantíssima do modelo MCP.

14:40

Tool normalmente representa intenção ou ação,

14:43

como emitir um reembolso ou alterar um saldo,

14:46

que só se representa em estado consumível.

14:50

A grande sacada de segurança aqui é,

14:53

em vez de criar uma tool genérica de buscar dados onde

14:56

a IA poderia tentar injetar queries perigosas no banco,

14:59

a gente pacota os dados de perdas financeiras no nosso back-end,

15:04

e exporta de forma limpa,

15:06

estática e 100% segura. O agente não pesquisa, ele consome o estado embalado.

15:11

Bem, depois entra a segunda novidade do slide, que é o prompt.

15:15

O prompt não é a execução, de novo, a mesma coisa.

15:17

O prompt é a voz do engenheiro dizendo para o LLM

15:20

como ele deve agir no momento que entrar no servidor.

15:23

Repare que a função analisa perdas financeiras e embute a persona analista financeira.

15:28

A tarefa de calcular receitas perdidas e a diretriz...

15:32

E a diretriz clara de quando usar a tool de bônus.

15:35

Então aqui a distinção didática do slide fica perfeitamente clara.

15:39

Se eu quero executar uma ação arriscada no sistema, eu exponho uma tool protegida.

15:44

Se eu quero fornecer massa de dados do banco de forma isolada, eu uso o resource.

15:51

Se eu quero guiar o raciocínio inicial da IA com regras da empresa, eu uso o prompt.

15:57

Então, guarda essa frase porque ela organiza a arquitetura cognitiva do MCP.

16:02

Se só se alimenta o agente,

16:03

tu fornece os braços e o prompt serve como cérebro operacional inicial,

16:09

como memória operacional inicial desse agente.

16:18

Bem, essa é a etapa em que o servidor prova o seu valor em produção.

16:23

Até aqui, o servidor existia apenas como código local.

16:26

Agora ele passa a existir como uma ferramenta disponível para aplicação real.

16:30

Construída em Streamlit, tá?

16:31

Que poderia ser qualquer outra tecnologia para desenvolvimento

16:37

de geral e uso de interface mais amigável,

16:39

né? Do que simplesmente o console.

16:42

E orquestrada pelo Legchain, tá? De novo, Legchain, gente,

16:45

é o principal SDK para desenvolvimento de IA que nós temos no mercado, tá?

16:54

Repara no fluxo aqui, pessoal.

16:56

Você sobe a interface com Streamlit, tão simples quanto.

17:02

O LinkedIn se conecta no seu servidor MCP, descobre os resources,

17:06

descobre o prompt e descobre a ferramenta de emissão de dinheiro.

17:09

Aí vem o primeiro input da prova de fogo, pasta análise de perdas financeiras.

17:14

O que você deve observar não é apenas a tela do chat,

17:17

é a barra lateral de logs.

17:18

Você vai ver exatamente o momento em que a gente

17:21

consome passivamente o resource cancelamentos barra motivos e categoriza as perdas.

17:26

Tudo ocorrendo com zero risco de exposição do banco.

17:30

Mas daí vem o teste de estresse financeiro. O input pede.

17:34

Tente reter o cliente do pedido 2 oferecendo um reembolso de R$150.

17:39

O pedido 2 era de R$350. 70% disso seria apenas R$70.

17:45

A IA, nesse caso aqui, ela tentou extrapolar a cota. E é ali que o MCP Pereira,

17:50

o que nós escrevemos, brilha. Porque o servidor bate na trava,

17:55

bloqueia a execução do banco e devolve um erro.

17:58

de protocolo inválido de parâmetro para o language chain.

18:01

E o que acontece a seguir é a magia do sistema agêntico, tá?

18:06

Seguro. Aí ela não quebra.

18:07

Ela não cospe um log de erro sujo para o usuário da interface.

18:10

A gente lê a mensagem detalhada do MCP Pereira.

18:13

O agente lê a mensagem detalhada do MCP Pereira,

18:17

entende a política restritiva da empresa e responde de forma educada no chat. Infelizmente,

18:22

não posso oferecer esse valor, pois fere a política de limite de 20%.

18:26

Então, guarda a ideia central dessa etapa, pessoal.

18:29

Um servidor sem travas de negócio é uma arma apontada para o banco de dados.

18:32

É aqui, lidando perfeitamente com MCPRR, uma interface real,

18:36

que o nosso servidor deixa de ser só uma demo teórica e

18:40

passa a ser uma arquitetura confiável dentro do mundo corporativo.

18:45

Beleza, então aqui, agora, a gente entra na consolidação final, pessoal.

18:49

Até que nós focamos a interface interativa com o Streamlit e o Agente.

18:53

Mas em um ambiente corporativo,

18:54

a verdade absoluta não mora no chat. Ela mora nos testes automatizados. Então,

18:59

o ponto central desse slide é o script de validação,

19:01

que é o script --verify --labs .sh.

19:05

Repara o que ele faz. Ele testa exaustivamente as travas do servidor.

19:09

O MCP deixa de ser apenas uma mágica de IA e

19:12

passa a ser um componente de back-end testável,

19:15

previsível e confiável. E olha o detalhe da cobertura de testes.

19:18

Em ambiente real, muitos problemas sérios nascem quando a regra de negócio...

19:22

do back-end muda e o agente começa

19:24

a cometer erros financeiros sem ninguém perceber. Por isso,

19:28

a sequência de validação é rigorosa.

19:30

A gente roda os testes que batem diretamente na TUR,

19:33

emitir reembolso bonificado. O teste injeta parâmetros maliciosos,

19:36

tentando dar um bônus de retenção muito maior do que a cota que o pedido permite.

19:43

Então, quando o teste recebe o nosso MCP-R de volta e dá PES, a gente...

19:49

tem a prova definitiva de que a segurança da tua funciona de forma isolada.

19:52

O que você deve observar na tela não é só a palavra verde,

19:55

é garantia de comportamento.

19:57

Repare na coluna da direita, pessoal.

19:59

Você deve focar que a cobertura de testes atinge 92%.

20:02

Isso é extremamente importante,

20:04

porque a confiança do sistema agêntico não vem de fé no LLM, tá? Vem de guardrails,

20:09

matematicamente comprovados no servidor. Então,

20:13

essa etapa fecha o end-to-end corporativo de verdade.

20:16

Não é só ver o agente responder de forma educada na interface web.

20:19

É garantir que, por trás dos panos,

20:21

as políticas financeiras estão blindadas por código automatizado

20:24

que roda em qualquer ambiente de pipeline de ICD.

20:29

Então, guarda isso aqui, pessoal.

20:31

Demonstração de agrado ao cliente.

20:33

Mas teste automatizado de ponta a ponta é o que não deixa a empresa falir.

20:37

Eu adoro essa frase.

20:39

Bem, é nesse momento aqui que vocês vão dar a pausa.

20:44

Vão abrir a IDE e sigam

20:49

o Readme, voltem aqui no vídeo, tentem tirar as dúvidas de vocês,

20:55

comece o desenvolvimento e daqui a pouco eu volto para a gente repassar a solução, tá bom?

## Resumo IA

[RESUMO_IA]