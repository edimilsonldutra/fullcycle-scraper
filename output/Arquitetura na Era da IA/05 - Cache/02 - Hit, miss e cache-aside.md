Módulo: Arquitetura na Era da IA\
Aula: [Hit, miss e cache-aside](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18337)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente começou a organizar a

00:05

ideia de cache em aplicações com o IA.

00:07

A gente viu que o ponto, ele não é simplesmente deixar a aplicação mais rápida,

00:12

mas entender quando que uma chamada para um

00:15

modelo realmente precisa acontecer de novo. Agora,

00:19

a gente vai para a primeira peça prática desse raciocínio,

00:23

que é o hit, miss e o padrão cache aside.

00:28

E eu não quero transformar isso aqui numa aula básica de cache,

00:31

porque provavelmente você já possa ter uma ideia geral sobre isso,

00:35

dependendo de quanto tempo você trabalha aí na área.

00:38

Mas vale alinhar o conceito dentro do fluxo com o IA,

00:41

porque aqui o impacto é um pouco diferente.

00:44

Quando uma aplicação recebe uma requisição,

00:46

ela pode procurar primeiro se já existe uma resposta aproveitável no cache.

00:51

Se existe, nós temos um cache hit.

00:54

A aplicação retorna a resposta e não chama o modelo. Isso aí é importante.

01:00

O ganho não é só em alguns milissegundos a menos.

01:04

A gente evitou tokens, evitou latência de inferência,

01:08

a gente evitou dependência do provedor naquele

01:10

momento e reduziu uma chamada externa.

01:13

Agora, se a resposta não existe no cache, temos um cache miss.

01:18

Aí a aplicação segue o fluxo normal, chama o modelo.

01:22

Recebe a resposta, valida o resultado e se fizer sentido,

01:26

salva aquela resposta no cache para uma próxima vez.

01:30

Esse desenho é o que normalmente chamamos de cache aside.

01:35

A aplicação olha para o cache,

01:37

se encontrou, usa. Se não encontrou,

01:39

busca na fonte original e daí a gente grava no cache.

01:44

Trazendo para o nosso exemplo de analisador de tickets,

01:48

o fluxo ficaria mais ou menos assim.

01:50

O usuário envia uma mensagem. Antes de chamar IA,

01:53

a aplicação gera uma chave de cache para aquela entrada.

01:56

Se encontrar uma resposta válida, retorna. Se não encontrar, chama o modelo,

02:01

recebe a classificação do ticket, salva o resultado e devolve para o usuário.

02:07

Aparentemente é simples, só que aqui começa a parte arquitetural.

02:12

Em uma aplicação com IA,

02:14

o cache hit pode não ser apenas achei alguma coisa com o mesmo texto,

02:22

uma resposta que ainda faz sentido para esse fluxo. Por isso,

02:26

mesmo antes de falar de fingerprint com mais detalhes,

02:30

a gente já precisa ter essa preocupação na cabeça.

02:34

O cache hit precisa ser confiável.

02:37

Se ele não for confiável, ele vira uma otimização,

02:41

vamos dizer assim, muito perigosa. E o miss também não é só a ausência de dado.

02:47

Às vezes o dado existe, mas ele não deve ser usado.

02:51

Talvez o prompt mudou, talvez a regra mudou,

02:54

a resposta anterior, sei lá, ela tenha vindo ali com um nível de confiança baixo,

03:00

talvez aquele tipo de análise não possa mais ser utilizado. Então, na prática,

03:05

a aplicação pode tratar isso como um miss, mesmo tendo algo armazenado.

03:10

E esse ponto é importante porque muita gente

03:13

Pense em cache apenas como armazenamento,

03:16

mas em sistemas como o IA, cache também é uma decisão.

03:21

A aplicação precisa decidir se aquela resposta pode ser reutilizada

03:25

ou se é melhor chamar o modelo novamente. Então,

03:28

nesse primeiro momento, a gente tem que pensar na seguinte estrutura básica.

03:34

No hit, eu evito a chamada para IA.

03:38

No miss, eu chamo a IA e posso salvar o resultado. E no cache aside,

03:43

quem controla esse fluxo é a própria aplicação. Aí no próximo vídeo,

03:47

a gente vai completar essa base falando sobre TTL.

03:50

Respostas, stale e invalidação.

03:54

Porque encontrar algo no cache é só uma parte da história.

03:57

A outra parte é saber por quanto tempo aquilo ainda vai continuar confiável.

## Resumo IA

[RESUMO_IA]