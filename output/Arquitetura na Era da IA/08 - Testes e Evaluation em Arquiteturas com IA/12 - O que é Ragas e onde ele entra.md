Módulo: Arquitetura na Era da IA\
Aula: [O que é Ragas e onde ele entra](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18791)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem?

00:02

No vídeo anterior a gente falou sobre avaliação da resposta final e a gente viu

00:05

em sistema de A que a gente não basta comparar o texto com o texto,

00:10

a resposta precisa ser relevante, completa,

00:13

fundamentada no contexto, clara, quando for o caso,

00:16

também precisar usar fontes que realmente sustentam o que foi dito. Agora,

00:21

antes de a gente ir para a prática,

00:22

a gente precisa entender onde entra uma ferramenta chamada RAGAS.

00:28

RAGAS é um framework de avaliação para aplicações com IA,

00:32

com foco muito forte em RAG.

00:34

A ideia dele é ajudar a transformar algumas

00:37

dimensões de qualidade em métricas mais executáveis.

00:41

Em vez de a gente ficar apenas lendo resposta por resposta

00:44

e dizendo essa ficou boa ou essa ficou ruim,

00:47

a ferramenta ajuda a gente a medir os

00:49

aspectos como qualidade do contexto recuperado,

00:52

fidelidade da resposta ao contexto e relevância da resposta para a pergunta.

00:57

A documentação, inclusive,

00:58

atual do RAGAS posiciona as suas métricas

01:01

como uma forma de medir objetivamente aplicações LLM,

01:07

incluindo... um RAG e workflows de agentes, tá?

01:11

Mas é importante entender o papel dele no nosso módulo.

01:14

RAGAS não substitui teste determinístico.

01:17

A gente já falou disso.

01:18

Se eu quero validar se a API retorna hasAnswer, sources, debug,

01:22

status code, esquema correto, eu não preciso de RAGAS,

01:25

tá? Isso é contrato de software.

01:27

Eu testo com PyTest, fake pipelines, test client e acertos objetivos. O RAGAS,

01:33

ele entra em outra camada. Ele ajuda...

01:36

Quando a pergunta passa a ser a resposta está bem fundamentada,

01:40

o contexto recuperado foi útil, a resposta está alinhada com a pergunta,

01:43

o sistema usou o contexto corretamente,

01:46

essas perguntas são mais difíceis de validar com um simples acerto.

01:50

Por exemplo, imagina um usuário que pergunta sobre SLA de P1 no Enterprise.

01:56

O sistema recupera alguns chunks, monta o contexto, gera a resposta.

02:00

A gente pode perguntar... Os chunks recuperados realmente eram úteis para responder?

02:04

A resposta ficou fiel ao contexto?

02:06

Ela respondeu a pergunta ou só falou genericamente sobre suporte?

02:10

É esse tipo de avaliação que começa a fazer sentido com o RAGAS.

02:14

Só que também tem um cuidado. Nem toda métrica serve para todo o dataset.

02:19

Algumas métricas precisam de uma resposta de referência.

02:22

Outras conseguem trabalhar usando pergunta,

02:25

resposta gerada e também contexto recuperado.

02:28

A documentação do RAGAS, por exemplo, diferenciava...

02:31

métricas que dependem de referência de métricas

02:34

que usam resposta gerada e os contextos recuperados.

02:38

Context Precision pode comparar contexto com uma resposta de referência.

02:44

Enquanto context e utilization avalia a utilidade do

02:48

contexto usando a resposta gerada quando não há referência.

02:53

E isso é muito importante para a nossa prática.

02:56

No nosso dataset, nós temos perguntas, termos obrigatórios, fontes aceitas,

03:01

tags e expectativa como should answer e should clarify.

03:05

Mas a gente ainda não criou uma resposta de referência completa.

03:10

Para cada caso. Então,

03:11

não faz sentido inventar uma resposta longa só para encaixar numa métrica.

03:16

A métrica precisa servir ao objetivo da avaliação e não ao contrário.

03:20

No nosso caso,

03:22

a gente vai utilizar a RAGAS para avaliar os casos respondíveis

03:26

onde o Knowledge Chat realmente produziu a resposta e teve contexto selecionado.

03:33

Casos negativos, onde o sistema deveria recusar, e casos ambíguos,

03:37

eles deveriam pedir, no caso, esclarecimento. Então,

03:42

eles não entram nessa avaliação com RAGAS agora.

03:45

Eles continuam sendo avaliados por outros mecanismos.

03:49

Então, repara como as camadas se complementam.

03:53

Teste de contrato garante que a API se comporta corretamente.

03:56

Evaluation por componente mostra se o Planner Retrieval e

03:59

o Reranking estão fazendo a parte deles.

04:02

RAGAS ajuda a olhar pela qualidade da resposta final em relação ao contexto usado.

04:08

E mais pra frente,

04:09

o LLMS Judge vai nos permitir criar uma rubrica própria

04:13

para critérios que talvez não estejam cobertos diretamente pelas métricas prontas.

04:19

Uma outra coisa importante é... RAGAS não é observabilidade.

04:24

O LangFuse ajuda a organizar datasets, experiments, traces e scores.

04:29

Agora, o RAGAS calcula métricas. Essas duas coisas podem trabalhar juntas,

04:35

mas elas não têm o mesmo papel.

04:38

Então, a pergunta arquitetural aqui é, qual ferramenta responde qual pergunta?

04:42

Se eu quero ver o trace de uma execução,

04:45

eu olho para ferramentas de observabilidade.

04:47

Se eu quero experimentos e scores, eu posso usar um LangFuse.

04:51

Se eu quero medir dimensões específicas de RAG, eu posso usar o RAGAS.

04:55

Se eu quero validar contrato, eu posso usar teste determinístico.

04:58

Se eu quero usar uma avaliação semântica customizada,

05:02

eu posso criar um judge com rubrica. No próximo vídeo,

05:05

a gente vai colocar isso na prática,

05:07

a gente vai rodar o nosso Knowledge Chat contra os casos respondíveis,

05:10

vamos dizer assim, do dataset,

05:12

coletar pergunta, resposta e também o contexto usado. Então,

05:17

aplicar métricas do RAGAS para começar a medir a qualidade da resposta final.

## Resumo IA

[RESUMO_IA]