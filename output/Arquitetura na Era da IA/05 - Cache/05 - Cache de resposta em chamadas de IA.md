Módulo: Arquitetura na Era da IA\
Aula: [Cache de resposta em chamadas de IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18340)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, no vídeo anterior a gente viu o analisador de tickets funcionando ainda sem cache, cada requisição,

00:08

mesmo que a mensagem fosse igual, a aplicação chamava a IA novamente.

00:12

Isso foi importante porque agora a gente tem uma base,

00:15

a gente sabe como é que o fluxo se

00:17

comporta quando não existe nenhuma otimização no meio.

00:20

Agora a gente vai dar o primeiro passo real de cache nesse projeto,

00:24

que é o cache de resposta. A ideia aqui é simples.

00:28

Mas tem um detalhe aí bem importante.

00:30

A gente não está cacheando qualquer coisa interna do modelo.

00:34

A gente não está cacheando token, embedding, contexto ou pedaço de prompt.

00:40

Isso a gente vai ver mais para frente. Nesse momento,

00:43

a gente está cacheando o resultado final da chamada.

00:47

No nosso caso, o resultado é a classificação do ticket.

00:51

A aplicação recebe uma mensagem.

00:54

Chama o modelo e o modelo retorna algo como categoria,

00:58

confiança e motivo. Se uma próxima requisição chegar com a mesma mensagem,

01:03

dentro das mesmas condições,

01:05

talvez a aplicação não precise chamar o modelo novamente.

01:09

Ela pode devolver a resposta que já foi calculada antes.

01:12

E esse é o cache da resposta. E aqui vale perceber uma coisa.

01:17

Em aplicações com IA, a resposta final normalmente custa mais caro do que parece.

01:24

Ela envolve montar o prompt, enviar o provedor,

01:26

esperar a inferência, consumir tokens, lidar com rede,

01:30

timeout, retry, rate limit e depois validar se o retorno veio no formato esperado.

01:35

Quando a gente retorna uma resposta do cache,

01:38

a gente está pulando todo esse caminho.

01:40

Então, no nosso endpoint, o fluxo começa a mudar.

01:45

Antes era a requisição chega, a aplicação chama IA e devolve a resposta.

01:49

Agora ela passa a ser a requisição chega,

01:51

a aplicação gera uma chave de cache,

01:53

procura se já existe uma resposta e só chama a IA se não encontrar nada válido. Se encontrar,

02:00

a resposta vem do cache. Se não encontrar,

02:02

chama o modelo, salva o resultado e devolve.

02:05

Só que a parte mais importante aqui não é o mecanismo, tá?

02:09

É o critério. Porque a pergunta não é apenas eu tenho algo salvo. A pergunta é...

02:14

O que está salvo ainda representa corretamente essa requisição? Então,

02:19

nessa primeira versão, a gente vai começar de forma simples.

02:22

A gente vai usar uma chave baseada na mensagem normalizada.

02:26

Por exemplo, remover os espaços extras,

02:28

deixar o texto num formato previsível e usar isso como base para procurar no cache.

02:33

Isso já vai ser o suficiente para demonstrar o primeiro ganho.

02:36

Duas chamadas iguais não precisam chamar a IA duas vezes. Mas isso ainda...

02:41

Não é o desenho completo. Se amanhã o prompt mudar,

02:45

uma resposta antiga não pode representar o mesmo comportamento atual da aplicação.

02:51

Então, se a regra de classificação mudar,

02:54

a resposta antiga também pode ficar inválida. Se eu mudar um modelo mais simples,

02:58

um modelo mais robusto, talvez eu também acabe tendo resultados misturados. E é por isso que,

03:05

depois dessa primeira prática, a gente vai evoluir para fingerprint.

03:10

A chave, sim, de cache vai começar a considerar a versão do prompt,

03:14

versões de regras e etc. Então, nessa etapa, o objetivo é bem direto.

03:18

A gente vai fazer o nosso endpoint, chamar a IA,

03:22

quando a mesma mensagem já foi analisada antes.

03:27

Fechou? E esse é o comportamento que a gente espera enxergar agora,

03:32

logo no nosso próximo vídeo. E no nosso próximo vídeo prático, inclusive,

03:36

a gente vai implementar isso no projeto, ainda sem banco, sem Redis, sem Embedding,

03:42

sem PG Vector,

03:44

só o primeiro cache exato em memória para deixar o fluxo

03:49

claro antes de evoluir para qualquer solução um pouco mais completa. Beleza?

## Resumo IA

[RESUMO_IA]