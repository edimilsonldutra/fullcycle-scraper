Módulo: Arquitetura na Era da IA\
Aula: [TTL, resposta stale e invalidação](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18338)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem? No vídeo anterior a gente falou sobre hit,

00:04

miss e cache aside. Ou seja,

00:06

a aplicação procura primeiro no cache, se encontrar uma resposta válida,

00:10

ela evita chamar a IA.

00:12

Se ela não encontrar, ela chama o modelo,

00:14

recebe a resposta e pode salvar aquilo para usar depois.

00:18

Agora entra uma pergunta importante. Por quanto tempo essa resposta continua válida?

00:24

E é aí que entram TTL,

00:27

resposta stale e invalidação. TTL significa Time to Live. Na prática,

00:33

é o tempo de vida daquele item no cache.

00:36

Você salva uma resposta e diz.

00:38

Essa resposta pode ser reutilizada por 5 minutos, 1 hora,

00:42

1 dia ou qualquer intervalo que faça sentido para aquele fluxo.

00:45

Em aplicações tradicionais, isso já é comum.

00:48

Mas em aplicações com IA, o TTL precisa ser pensado com um pouco mais de cuidado.

00:54

porque a resposta do modelo pode estar ligada a uma regra de negócio,

00:58

a uma versão de prompt,

01:00

a um contexto ou uma decisão que pode mudar.

01:03

Vamos continuar com o exemplo do analisador de tickets.

01:07

Se a aplicação classifica uma mensagem como billing,

01:10

talvez faça sentido reaproveitar essa classificação por algum tempo.

01:14

Se a mesma mensagem aparecer de novo poucos minutos depois,

01:18

provavelmente não tem motivo para eu chamar o modelo novamente.

01:22

Agora, se a regra de classificação mudou,

01:25

se o prompt foi ajustado ou se a forma de tratar tickets de cobrança mudou,

01:31

aquele cache pode não ser mais confiável. E esse aí é o ponto central.

01:36

O cache não expira só porque o tempo passou.

01:39

Às vezes ele precisa ser invalidado porque o contexto mudou.

01:43

E aí a ideia de resposta stale.

01:46

Uma resposta stale é uma resposta antiga.

01:50

Ela pode estar tecnicamente disponível no cache,

01:53

mas talvez não represente mais a melhor resposta para aquele momento atual.

02:00

Em alguns fluxos isso pode ser até aceitável, em outros não.

02:04

Por exemplo, se eu estou gerando uma sugestão genérica de categoria para um ticket,

02:08

talvez uma resposta um pouco antiga ainda seja aceitável.

02:12

Mas se eu estou tomando uma decisão sensível quando uma regra recém

02:16

-alterada ou eu estou lidando com algo que depende de alguma informação atualizada,

02:22

reutilizar uma resposta antiga pode ser um grande problema.

02:25

Então a pergunta não é simplesmente o cash expirou ou não expirou.

02:29

A pergunta melhor é... Essa resposta ainda pode ser usada com segurança?

02:34

A invalidação é justamente o mecanismo

02:40

para tirar uma resposta do jogo.

02:42

Pode ser por um tempo, usando o TTL, pode ser de forma manual,

02:46

quando alguém muda alguma regra, pode ser por versão,

02:50

quando o prompt muda, e pode ser por tipo de análise,

02:53

quando aquele fluxo não aceita a reutilização depois de um determinado período.

02:59

Por isso...

03:00

Mais pra frente, quando a gente for falar de fingerprint,

03:03

a gente vai incluir informações como a versão do prompt, a versão das regras,

03:08

na chave do cache. Assim, quando o prompt muda,

03:12

A aplicação, naturalmente, para de reutilizar as respostas antigas daquele contexto.

03:18

Então, guarda essa ideia.

03:20

TTL é uma forma simples de controlar o tempo de vida.

03:23

Resposta STALE é um alerta de que algo pode estar antigo.

03:28

Invalidação é a decisão de não usar mais aquele cache. E na próxima aula,

03:33

a gente vai sair um pouco da teoria e ver

03:35

aí o nosso analisador de tickets ainda sem cache,

03:38

justamente para medir o comportamento inicial antes de a gente começar a otimizar.

## Resumo IA

[RESUMO_IA]