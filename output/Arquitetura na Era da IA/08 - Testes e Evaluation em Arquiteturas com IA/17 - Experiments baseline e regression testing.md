Módulo: Arquitetura na Era da IA\
Aula: [Experiments baseline e regression testing](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18796)

## Resumo da aula



## Transcrição

00:00

Olá pessoal, tudo bem? No vídeo anterior,

00:03

a gente criou um juiz com uma saída estruturada para

00:06

avaliar a resposta final do nosso Knowledge Chat. Com isso,

00:11

além dos testes determinísticos de avaliação por

00:15

componente e das métricas com ratas,

00:17

a gente passou também a ter uma avaliação baseada em rubricas.

00:22

Agora, a gente precisa dar um passo muito importante.

00:26

Parar de olhar uma execução isolada e começar a comparar versões.

00:30

Porque uma avaliação rodada uma vez responde uma pergunta limitada.

00:36

Como o sistema está se comportando agora?

00:38

Isso é útil, mas em arquitetura, normalmente a pergunta mais importante é outra.

00:44

O sistema melhorou ou piorou depois da mudança? Essa é a ideia do experimento.

00:49

Um experimento é uma execução organizada de avaliação

00:53

contra uma versão específica do sistema.

00:55

Pode ser uma versão de prompt, uma versão do modelo,

00:58

uma versão do pipeline, uma configuração de re-ranking,

01:01

outra sem re-ranking, um chunking diferente,

01:05

ou com threshold diferente e assim por diante.

01:07

Então, quando a gente roda o dataset contra uma versão do Knowledge Chat,

01:12

a gente gera as respostas, calcula os scores e salva os resultados.

01:17

Isso vira, no final das contas, um experimento.

01:20

Mas esse experimento só ganha força quando a gente compara um com o outro.

01:25

E é aqui que entra a baseline.

01:28

O baseline é a versão de referência,

01:30

é o comportamento atual que você considera como ponto de comparação.

01:35

Não significa que ele é perfeito, significa apenas,

01:39

a partir daqui eu quero saber se as próximas mudanças melhoram ou pioram. Por exemplo,

01:45

imagina que hoje o pipeline está usando o query planner, retrieval,

01:49

re-ranking e o prompt final. Esse é o baseline.

01:52

Amanhã você altera o prompt do planner.

01:54

Depois roda o mesmo dataset de novo. Se os discord melhorarem,

01:58

ótimo. Se ele piorar, você detectou no final das contas uma regressão.

02:04

E regressão é justamente isso.

02:07

Uma mudança que piora o comportamento que antes estava melhor.

02:11

Em sistemas tradicionais,

02:13

a gente está acostumado a falar de regressão quando

02:15

um teste que passava começa a falhar.

02:17

Em sistemas com IA, isso continua existindo,

02:20

mas fica mais sutil. Às vezes, nada quebra tecnicamente.

02:24

A API continua respondendo, o JSON continua válido,

02:27

o modelo continua gerando texto, mas a qualidade piora.

02:31

A fonte correta aparece menos. A taxa de recuso aumenta.

02:35

O juiz começa a dar nota menor para o groundedness.

02:38

A resposta fica mais longa e mais cara.

02:41

O retrieval passa a trazer mais ruído. Então, tudo isso é regressão.

02:46

E se você não compara versões com o dataset estável,

02:50

você não percebe. Um ponto importante,

02:52

nem toda mudança melhora todas as métricas ao mesmo tempo. Você pode trocar...

02:58

para um modelo mais barato e reduzir o custo,

03:00

mas perder um pouco de completude.

03:02

Você pode aumentar o top K e melhorar o recall, mas aumentar tokens e latência.

03:08

Pode ligar o re-ranking e melhorar a fonte,

03:11

mas aumentar custo. Então pode deixar um prompt mais restritivo,

03:15

reduzir a alucinação, mas aumentar as recusas.

03:18

Então o experimento não é só procurar uma nota mágica, tá?

03:22

É entender trade-offs. Em arquitetura isso é fundamental, porque qualidade,

03:26

custo, latência, quase sempre eles brigam ali entre si.

03:30

A versão melhor não necessariamente é a que tem a

03:34

melhor resposta ou maior score em uma única métrica.

03:37

A versão melhor é a que atende ao

03:40

objetivo da aplicação dentro das restrições definidas.

03:44

Por isso, quando a gente compara experiments,

03:46

a gente precisa olhar para várias dimensões.

03:49

A taxa de contratos válidos continua alta.

03:53

As fontes aceitas aparecem. A resposta está fundamentada.

03:58

O custo por causa... o caso aumentou, a latência piorou,

04:02

a recusa está correta, o comportamento em casos ambíguos melhorou,

04:07

os casos negativos continuam sendo recusados e no caso de agentes,

04:12

mais para frente a gente também vai olhar para ferramentas chamadas,

04:16

argumentos e também trajetória.

04:20

Outro ponto importante é manter o dataset estável.

04:24

Se cada experimento você muda os casos,

04:26

fica difícil saber se o sistema melhorou ou se você apenas mudou a prova.

04:31

Claro que o dataset deve evoluir com o tempo,

04:33

principalmente a partir de bugs reais e feedback de produção.

04:37

Mas para comparar uma mudança específica,

04:40

o ideal é rodar sempre contra o mesmo dataset,

04:43

certo? Então isso dá muito mais confiança.

04:46

A prática que vem depois de a gente seguir exatamente essa ideia.

04:52

Vamos dizer que a gente vai comparar versões do nosso Knowledge Chat, por exemplo,

04:56

uma execução com re-ranking e outra sem re-ranking.

04:59

Uma versão com prompt atual e outra com prompt alterado.

05:02

O ponto não é provar que uma é sempre melhor,

05:04

o ponto é mostrar como que a gente mede a diferença. E daí,

05:08

a partir daí, a avaliação começa a virar uma ferramenta de decisão arquitetural.

05:13

Você deixa de falar, eu acho que ficou melhor,

05:16

e começa a falhar. Falar, quer dizer. Nesse dataset,

05:20

essa versão melhorou o source hit,

05:23

piorou a latência e manteve o groundedness estável.

05:26

Então, essa conversa aí, ela começa a ficar muito...

05:29

Então a mensagem principal dessa aula é,

05:32

avaliação não serve apenas para medir uma versão, ela serve para comparar versões,

05:37

detectar regressões e tomar decisões com mais evidência. Fechou?

## Resumo IA

[RESUMO_IA]