Módulo: Arquitetura na Era da IA\
Aula: [Como OpenAI, Anthropic e Gemini tratam prompt caching](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18358)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:03

No vídeo anterior a gente separou cache de aplicação e cache de provedor.

00:07

Agora a gente vai olhar para como isso aparece em alguns provedores,

00:11

porque aqui existe uma diferença importante. A ideia é parecida,

00:15

mas a forma de utilizar ela não é igual.

00:18

Então quando a gente fala de prompt caching no provedor,

00:22

não estamos falando de reaproveitar a resposta final da aplicação.

00:28

A gente está falando em reaproveitar partes repetidas do

00:31

prompt que continuam sendo enviadas para o modelo.

00:34

Normalmente isso faz mais sentido quando existe um

00:37

prefixo grande e estável como instruções,

00:40

regras, exemplos, esquemas,

00:42

ferramentas ou um contexto mais fixo.

00:44

E depois sim a gente tem a parte variável ali no final.

00:49

Na OpenAI, o funcionamento é mais automático.

00:52

A documentação atual diz que o prompt caching é habilitado

00:58

automaticamente para prompts com pelo menos 1024 tokens ali ou mais.

01:05

E que o cache hit depende de match exato de prefixo. Por isso,

01:10

a recomendação prática é colocar o conteúdo estático no

01:14

começo do prompt e o conteúdo variável no final.

01:17

A resposta também pode trazer tokens cacheados dentro do uso,

01:23

o que permite observar quando parte da entrada foi reaproveitada.

01:28

Então, no caso da OpenAI,

01:30

o raciocínio arquitetural é eu não preciso criar um

01:33

recurso explícito de cache para começar a reaproveitar isso,

01:37

mas eu preciso organizar o meu prompt para que eu

01:44

tenha ali no início dele

01:47

tudo que é fixo. Por quê? Se eu fico mudando o começo do prompt toda hora,

01:52

se eu coloco informação variável antes dessas instruções fixas,

01:56

ou se eu altero pequenas partes do prefixo, eu reduzo a chance de cache hit.

02:02

Já na Anthropic, o controle é mais explícito. O Cloud permite usar o...

02:08

cache-control para indicar pontos do prompt que podem ser cacheados

02:14

com TTL padrão de 5 minutos e uma opção de 1 hora.

02:18

A documentação também fala sobre a possibilidade de misturar TTLs desde

02:24

que entradas com TTL maior apareçam antes das de TTL menor.

02:30

Isso muda o estilo de uso, porque ao invés de você apenas...

02:35

depender do provedor reconhecer automaticamente o seu prefixo repetido,

02:40

você consegue marcar blocos específicos como cacheáveis.

02:44

E isso pode ser muito útil quando você tem um system prompt grande,

02:49

documentos estáticos,

02:50

exemplos longos ou instruções compartilhadas por várias chamadas.

02:55

Mas também exige cuidado de implementação, porque agora você precisa pensar...

03:00

onde estão os blocos estáveis e onde começa a parte variável. Já no Gemini,

03:07

existem duas ideias importantes. A documentação fala de caching implícito,

03:12

habilitado por padrão em modelos como Gemini 2.5 ou os mais novos,

03:17

com caches mínimos de tokens por modelo.

03:20

E também existem os cachings explícitos, por conteúdo cacheado,

03:27

onde você cria um conteúdo cacheado com um modelo,

03:30

um conteúdo e TTL. Se o TTL não for informado,

03:35

a documentação indica que o padrão é de uma hora.

03:37

Então, o Gemini acaba tendo um desenho interessante.

03:41

Em alguns casos, você pode se beneficiar do caching implícito,

03:44

sem fazer nada de especial,

03:46

além de estruturar bem a entrada. Em outros,

03:49

você pode fazer sentido criar explicitamente um conteúdo cacheado.

03:54

Principalmente quando existe um contexto grande que

03:57

será reutilizado em várias chamadas. Agora,

04:00

o ponto principal dessa aula não é decorar a API de cada provider.

04:04

Isso muda e você sempre precisa conferir a documentação atual.

04:08

O ponto principal é entender o padrão arquitetural.

04:12

OpenAI... tende a ser mais automático.

04:15

Anthropic dá mais controle com breakpoints e cache control.

04:18

E o Gemini combina caching implícito e caching explícito com cached contents.

04:24

Mas, em todos os casos,

04:26

existe uma ideia comum. Quanto mais estável for o começo do prompt,

04:30

maior a chance de reuso.

04:33

Isso influencia a forma de como a gente monta os prompts em aplicações reais.

04:38

Se você tem instruções fixas, regras de formato,

04:41

exemplos, esquemas, fortes e ferramentas,

04:43

faz sentido manter essas partes muito estáveis no começo.

04:48

A parte variável, como mensagem do usuário, os dados específicos daquela requisição,

04:53

ou qualquer coisa que muda da chamada,

04:56

você tenta deixar o máximo possível depois.

04:58

Não porque isso deixa o prompt mais bonito,

05:01

inclusive, mas porque isso pode afetar o custo e a latência.

05:04

Tome cuidado com uma conclusão errada.

05:07

Provider caching não remove a necessidade de caching na aplicação.

05:11

Se a resposta já foi calculada e continua válida,

05:14

melhor caminho pode ser nem chamar o provider.

05:18

Foi isso que a gente fez, inclusive, anteriormente. Então,

05:21

na prática, a pergunta aí é dupla, né? Primeiro,

05:24

se eu consigo evitar a chamada inteira usando o cache da aplicação?

05:27

E se eu não consigo? A segunda pergunta é,

05:30

eu consigo estruturar essa chamada de um jeito que

05:33

o provider reaproveite a parte estática do prompt?

05:36

Essa é a visão que eu queria que você levasse para você.

05:40

Não é escolher entre um cache da aplicação e um cache de provider.

05:43

É conseguir entender que eles estão nas camadas diferentes.

05:46

E um ponto muito importante que eu queria

05:49

trazer e que não é necessariamente técnico,

05:51

é a parte de economia.

05:54

Toda vez que você trabalha com cache de provider,

05:57

o desconto que você tem na utilização desse cache é muito grande.

06:04

Muito grande mesmo.

06:05

Muitas vezes você tem ali um desconto de 90%

06:08

somente pelo fato de você ter cacheado essas informações,

06:13

tá? Eventualmente no Gemini eu falo,

06:15

eu quero que esse documento, esse dado, ele fique cacheado.

06:19

Então, ele gera uma referência ali pra você e

06:21

toda vez que você precisar usar aquele dado,

06:24

Você passa por referência e ele sabe de qual conteúdo cacheado você

06:28

Tá falando e aí você consegue também ter essa economia,

06:30

Velocidade e tudo mais. Então, lembre... galera, a arquitetura nesse caso,

06:36

Em relação a essas camadas de provider, elas vão muito além,

06:40

Mas muito além apenas de simplesmente dizer que eu cachei isso aí, fecha muito,

06:46

Muito, muito faz com que uma,

06:48

Como que eu posso dizer, uma conta feche ou não na utilização da

06:52

IA aí na sua empresa, porque pode ficar muito caro utilizar a IA,

06:56

Então, se você conseguir combinar o cache da sua aplicação, o cache semântico,

07:00

O cache exato e também

07:02

Conseguir organizar muito bem os seus prompts e tudo mais, o que vai acontecer?

07:08

Vai fazer com que você entre num mundo onde você vai gastar o menor possível,

07:12

Tá? E também, ao mesmo tempo, vai tentar fazer,

07:15

Chamar ao menor possível também o modelo.

07:18

O ponto é que trabalhar com o cache no provider de

07:21

Forma correta vai gerar uma economia muito grande para a sua aplicação.

07:26

Então, fique de olho nisso. A sua empresa agradece.

## Resumo IA

[RESUMO_IA]