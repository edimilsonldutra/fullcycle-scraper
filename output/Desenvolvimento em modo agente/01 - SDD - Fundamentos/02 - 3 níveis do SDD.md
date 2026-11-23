Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17766)

## Resumo da aula

Spec-Driven Development usa a especificação como referência principal para gerar e validar software. Retomando a base já estabelecida de SDD, o ponto novo aqui é o papel da especificação como contrato explícito entre produto e desenvolvimento: ela descreve o comportamento desejado e orienta tanto a implementação quanto os testes. Em ambientes com IA, isso ganha peso porque o modelo precisa de restrições, contexto e critérios claros para produzir código aderente ao que foi pedido.

Spec First é o nível em que a especificação vem antes do código, mas não passa a fazer parte da manutenção contínua do projeto. Ela serve bem para protótipos, tarefas isoladas e criação de features pontuais, especialmente quando a geração da especificação já é parcialmente automatizada. O ganho está em planejar melhor a entrega e usar a IA com mais precisão naquela tarefa específica, sem assumir o custo de manter esse artefato vivo depois.

Quando a especificação é ancorada, ela evolui junto com o código e é validada pelos testes. Em vez de existir apenas no início de uma feature, ela compõe um histórico persistente do sistema: feature por feature, dependência por dependência, formando uma linha do tempo que ajuda a IA a entender o contexto acumulado do projeto. Esse modelo é mais útil para sistemas que continuam crescendo, porque a clareza histórica melhora a consistência das próximas gerações.

Manter documentação sempre coerente é difícil porque projetos mudam de direção, decisões são revistas e textos antigos podem entrar em conflito com o estado atual do sistema. Por isso, exigir documentação totalmente livre de ambiguidades tende a ser irrealista. Ainda assim, preservar o encadeamento das decisões e das features já construídas já produz valor suficiente para orientar evolução, testes e geração assistida por IA.

A necessidade de detalhamento extremo não é fixa; ela depende da capacidade de inferência dos modelos usados. À medida que os modelos ficam mais competentes, parte do contexto pode ser inferida sem que cada detalhe esteja explicitado na documentação. Isso não elimina a especificação, mas muda o ponto ótimo entre esforço de documentação e qualidade da geração.

Spec as Source é o nível em que a especificação se torna o único lugar de edição, e o código derivado dela não deve ser alterado manualmente. Se uma regra de negócio muda, a alteração acontece na especificação e o código é regenerado a partir dela. Esse modelo maximiza consistência entre intenção e implementação, mas exige um pipeline confiável e uma disciplina operacional maior do que a maioria dos times ainda consegue sustentar plenamente.

Na prática, o cenário atual já se aproxima parcialmente de Spec as Source, porque boa parte da codificação manual tende a desaparecer, embora ajustes periféricos ainda ocorram. Configurações, organização de ambiente e pequenas intervenções continuam existindo mesmo quando a lógica principal já é gerada. Por isso, o nível mais alto deve ser entendido mais como direção de maturidade do que como regra absoluta aplicada ao pé da letra.

## Transcrição

00:00

Bom, pessoal, agora que a gente tem algumas expectativas aqui mais alinhadas

00:05

de como que vai funcionar aqui o nosso processo,

00:07

vamos falar especificamente de uma forma um pouco

00:10

mais profunda sobre Spec-Driven Development,

00:13

tá? Então, conceito básico para quem nunca ouviu falar, tá? E lembrando, tá?

00:19

Esses termos, ao longo do tempo, eles podem mudar, principalmente nessa era da IA,

00:24

que cada dia novos termos vão aparecendo. Mas eu acredito que,

00:28

independente de termo, o conceito acaba se tornando o mesmo,

00:32

porque você sempre vai precisar ter uma especificação

00:35

para desenvolver algo de uma forma geral,

00:37

certo? Então, o que acontece?

00:39

Quando a gente está falando do Spec-Driven Development,

00:42

nós temos alguns pontos que são importantes, que é o quê?

00:46

A ideia é que...

00:48

a fonte da verdade para que o código seja gerado é o quê?

00:53

A própria especificação.

00:56

Então, quando eu quero, na realidade, validar o meu software,

01:01

eu vou validar o meu software baseado na especificação que ele foi gerado.

01:05

Então, normalmente, o que acontece?

01:09

A gente sabe que a gente tem que especificar,

01:11

independente do tipo de software que a gente vai fazer,

01:14

mas como a gente vai trabalhar com IA? O que normalmente a gente vai precisar?

01:19

Ter mais restrições, ter mais contexto e também fazer com que,

01:23

muitas vezes, o código gerado tenha que refletir exatamente. Ou seja,

01:30

é como se o nosso teste automatizado fosse feito contra a nossa especificação.

01:37

Então... O ponto importante aqui é que as equipes,

01:41

independente se é área de produto, junto com a área de desenvolvimento,

01:45

elas vão escrever um contrato claro do comportamento desejado e

01:49

eles vão usar esse contrato para orientar e fazer as implementações,

01:54

inclusive testar a aplicação. Então, essa aqui é a ideia principal do Spec-Driven.

02:00

Eu tenho uma especificação, baseado naquela especificação,

02:03

a gente tem um código. Basicamente é isso, tá? A grosso modo. O ponto é o seguinte,

02:09

existem alguns artigos,

02:11

eu vou compartilhar diversos artigos com vocês ao longo dos próximos capítulos,

02:16

porque são muito material e você precisa ler,

02:19

mas no blog do Martin Fowler,

02:23

eles fizeram uma publicação especificamente da evolução do Spec-Driven Development,

02:30

quando isso começou a ser gerado.

02:35

Qual que eles colocaram assim como se fossem níveis de maturidade? E honestamente,

02:40

eu não sei se em algum momento a gente vai chegar nesse nível de maturidade,

02:44

honestamente, mas o fato é,

02:47

o primeiro ponto que a gente tem que pensar é que nós temos Spec First, ou seja,

02:52

a gente especifica, a especificação é criada antes do código,

02:57

mas não necessariamente ela é mantida.

03:01

Ou seja, ela é utilizada para protótipos e tarefas isoladas.

03:06

Então, vamos imaginar que eu quero criar uma feature,

03:08

vamos imaginar que eu quero criar um pedaço de um sistema.

03:11

Então, o que eu faço? Eu gero uma especificação,

03:13

baseado naquela especificação, o que acontece no meio dessa história,

03:17

eu desenvolvo o código e eu resolvo aquela tarefa.

03:20

Muito parecido com o que o Luiz Carlos colocou,

03:25

que você planeja, você implementa e etc. É parecido.

03:29

A grande diferença aqui nesse caso é que normalmente o nível de especificação é

03:34

um pouco maior e normalmente o processo de

03:37

geração da especificação é mais automatizado.

03:41

Mas o ponto é que a especificação first deixa claro,

03:45

mas ela não faz parte da vida

03:49

do projeto. Ela trabalha ali de uma forma pontual.

03:52

Eu tenho um projeto ou vou começar algo do zero,

03:55

eu crio algo para fazer uma implementação e

03:58

aí eu gero uma feature baseada em uma especificação.

04:02

Isso aqui é muito comum de acontecer.

04:06

Às vezes você tem um sistema, quer desenvolver uma feature,

04:08

você consegue gerar a especificação dessa feature,

04:10

medir para a IA gerar e você não vai manter isso ao longo do tempo.

04:15

Agora... Aqui a coisa começa a ficar mais interessante,

04:19

que na realidade é o nível que provavelmente nós vamos chegar aqui nesse capítulo, que é o quê?

04:26

A especificação é ancorada, ou seja, ela é mantida junto com o código,

04:33

validada com os testes, ou seja,

04:36

o sistema que evolui ao longo do tempo é mantido junto com o código. Significa o quê?

04:44

Que eu posso ter um sistema inteiro que eu quero criar e ao longo da vida desse

04:49

sistema eu vou tendo essas especificações e que a

04:54

passo a passo ele vai construindo feature por feature,

04:58

mas vamos dizer, a documentação, aquele bundle de documentação,

05:03

ele é persistido ao longo do tempo.

05:06

Existem diversos desafios para a gente chegar nesses

05:09

aspectos porque os projetos eles desviam.

05:13

As decisões acabam mudando e as documentações, ao longo do tempo,

05:17

elas começam e podem ficar contraditórias.

05:20

Então manter essas documentações extremamente sem ambiguidades é algo que,

05:24

na minha opinião, é quase que impossível. Por outro lado,

05:28

somente de você ter a linha do tempo do que foi construído desde o início,

05:32

feature 1, feature 2, feature 3,

05:34

e vai seguindo os gráficos das dependências dessas features,

05:38

as coisas vão ficando muito claras.

05:40

E quanto mais clareza a IA tem, mais esperta ela vai ficar em relação a entender,

05:48

a linha do tempo ali do projeto. Obviamente que a gente vai falar disso também,

05:52

que cada dia mais os nossos modelos estão ficando mais inteligentes e muitas vezes

05:57

a gente não precisa chegar num nível

06:02

de granularidade tão grande em determinada documentação,

06:05

porque ele vai ter um poder tão grande de

06:08

inferência que ele vai conseguir desenvolver mesmo assim.

06:10

Mas o ponto é que a gente vai fazer com que a especificação ela...

06:15

fique ali atrelada ao longo do projeto, tá?

06:18

E aqui é um nível mais hard, como que eu posso dizer para você,

06:23

que é chamado Spec as Source.

06:26

Isso significa que a especificação é o único local onde você vai editar.

06:32

O código que é gerado a partir dela nunca vai ser modificado na mão.

06:37

Ou seja, basicamente, eu fiz uma especificação,

06:41

rodo o software gerado e eu não faço... ajuste nenhum.

06:44

Na realidade, eles colocam até exemplos do tipo código gerado automaticamente,

06:49

não modifique. É basicamente isso que acontece.

06:53

Como que eu, pessoalmente, encaro isso? Nós vamos chegar lá,

06:59

e a gente chega lá, hoje eu já não programo mais,

07:03

eu já não coloco mais a mão no código, mas eventuais ajustes eu acabo fazendo.

07:10

Organizar a variável de ambiente, fazer um negócio para lá,

07:13

fazer um negócio para cá. Mas realmente, codificar em si,

07:16

chegar e falar if, colocar a mão no código, etc., isso eu já não faço mais. Então,

07:21

se a gente coloca isso como spec é source, depende muito do nível de interpretação.

07:27

Eu acredito que o nível de interpretação que eles colocam aqui é

07:31

o aspecto de que realmente eu tenho ali um monte de especificação,

07:36

don't enter, gera o código. Quero mudar, mudei a especificação,

07:39

foi lá, mudou o código. Mais ou menos isso ali.

07:42

É como se fosse um editor de especificação cuspindo o código.

07:45

A gente está um pouco nesse momento, porém,

07:48

eu acho que chegar a isso de forma completamente

07:50

plena vai demorar ou não vai ser assim algo tão...

07:57

ao pé da letra como eles colocaram.

07:59

Mas faz muito sentido porque hoje você já não programa mais.

08:04

Desenvolver em si, colocar a mão no código é algo que cada vez menos,

08:11

cada vez mais, cada vez menos a gente vai fazer.

08:14

Legal? Para esse vídeo não ficar muito grande,

08:16

eu vou cortar aqui e a gente continua aí.

## Resumo IA

**Abreviações**
*   **SDD**: Spec-Driven Development
*   **IA**: Inteligência Artificial

**Resumo**
A aula teve como objetivo aprofundar o conceito de Spec-Driven Development (SDD), enfatizando seu papel crucial na era da Inteligência Artificial. SDD baseia-se na especificação como a referência principal, a "fonte da verdade", para a geração e validação de software. Essa especificação atua como um contrato explícito entre as equipes de produto e desenvolvimento, descrevendo o comportamento desejado e orientando tanto a implementação quanto os testes. Em ambientes com IA, a especificação ganha ainda mais peso ao fornecer as restrições, o contexto e os critérios claros que os modelos de IA precisam para produzir código aderente às demandas.

O instrutor apresentou diferentes níveis de maturidade do SDD, inspirados em uma evolução:
*   **Spec First**: Neste nível, a especificação é criada antes do código, mas não é mantida ativamente ao longo do tempo. É ideal para protótipos, tarefas isoladas e a criação de funcionalidades pontuais, especialmente quando a geração da especificação já é parcialmente automatizada. Seu benefício está no melhor planejamento da entrega e no uso mais preciso da IA para aquela tarefa específica, sem o custo de manutenção contínua do artefato.
*   **Especificação Ancorada**: Aqui, a especificação evolui junto com o código e é validada pelos testes. Em vez de ser um documento inicial único, ela se torna um histórico persistente do sistema, registrando feature por feature e dependência por dependência. Essa linha do tempo acumulada é valiosa para a IA, que consegue entender o contexto do projeto, resultando em maior consistência nas gerações futuras de sistemas que continuam crescendo.
*   **Spec as Source**: Representa o nível mais elevado de maturidade, onde a especificação se torna o único local de edição. O código derivado dela não deve ser alterado manualmente; qualquer mudança de regra de negócio acontece na especificação, e o código é regenerado. Este modelo maximiza a consistência entre a intenção e a implementação, mas exige um pipeline de geração confiável e uma disciplina operacional que poucos times conseguem sustentar plenamente hoje.

Na prática, embora o cenário atual já se aproxime de "Spec as Source" devido à crescente automação da codificação, ajustes periféricos (como configurações de ambiente) ainda podem ocorrer manualmente, indicando que este nível é mais uma direção de maturidade do que uma regra absoluta.

**Pontos de atenção**
*   **Evolução da Terminologia**: Termos como "Spec-Driven Development" podem mudar com o tempo, especialmente na era da IA, mas o conceito fundamental de usar uma especificação para desenvolver software permanece constante.
*   **Exigências da IA**: Ao trabalhar com IA para geração de código, é crucial que as especificações contenham mais restrições, contexto e critérios claros para garantir que o código gerado reflita exatamente o que foi solicitado.
*   **Especificação como Contrato**: A especificação deve ser vista como um contrato claro entre as equipes de produto e desenvolvimento, orientando não apenas a implementação, mas também os testes.
*   **Manutenção de Documentação**: Manter a documentação de projetos em evolução sempre coerente é um desafio. Projetos mudam, decisões são revistas, e documentos antigos podem se tornar contraditórios. Atingir uma documentação totalmente livre de ambiguidades é irrealista.
*   **Valor do Histórico Persistente**: Mesmo com as dificuldades de manter a documentação perfeita, preservar o encadeamento das decisões e das features construídas (como em "Especificação Ancorada") já agrega valor suficiente para guiar a evolução, os testes e a geração assistida por IA.
*   **Nível de Detalhamento Flexível**: A necessidade de detalhamento extremo na especificação não é fixa; ela depende da capacidade de inferência dos modelos de IA. À medida que os modelos se tornam mais inteligentes, parte do contexto pode ser inferida, alterando o ponto ótimo entre esforço de documentação e qualidade da geração.
*   **Desafios do "Spec as Source"**: Embora maximize a consistência, o modelo "Spec as Source" exige um pipeline extremamente confiável e uma disciplina operacional muito alta, que a maioria das equipes ainda não consegue sustentar plenamente.
*   **Realidade do "Spec as Source"**: O nível mais alto de "Spec as Source" deve ser encarado como uma direção de maturidade. Embora a codificação manual de lógica principal tenda a diminuir, ajustes periféricos e configurações ainda podem exigir intervenção humana, mesmo em cenários altamente automatizados.