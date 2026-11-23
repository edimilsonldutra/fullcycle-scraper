Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17768)

## Resumo da aula

SDD já foi apresentado como uma abordagem em que a especificação orienta a geração e a validação do software. O ponto novo aqui é que nem toda instrução dada ao agente descreve o produto; parte delas descreve o processo de desenvolvimento. Quando a especificação diz o que o sistema deve fazer, ela está no núcleo do SDD. Quando passa a dizer como o agente deve se comportar durante a execução, surge uma fronteira semântica menos nítida.

Especificar arquitetura, endpoints, layout e padrões de teste ainda pode ser entendido como detalhamento do produto e de sua implementação. Já instruções como “ao finalizar uma tarefa, execute a suíte de testes e faça um commit” operam em outra camada: elas controlam o fluxo de trabalho do agente. Isso continua sendo uma forma de especificação, mas não necessariamente uma especificação do produto. A distinção importa porque mistura duas fontes de verdade diferentes: a do sistema entregue e a do ambiente que conduz sua construção.

Retomando o conceito de harness já introduzido, ele representa o ecossistema fornecido ao agente para executar o trabalho: regras operacionais, automações, restrições e comportamentos esperados. Esse ambiente não descreve diretamente o domínio do software, mas condiciona como o agente produz mudanças no projeto. Por isso, o harness funciona como uma camada de controle sobre a execução, enquanto a documentação do projeto continua sendo a referência principal do que deve ser construído.

A fronteira fica nebulosa quando uma instrução operacional depende de conhecimento do produto. Mandar o agente rodar testes é claramente um comportamento de processo; exigir que ele verifique se os testes cobrem os critérios de aceitação já exige uma especificação de validação alinhada ao produto. Nesse ponto, o harness sozinho não basta, porque ele precisa de artefatos que expliquem como testar e o que significa aceitar a entrega. A validação passa a conectar comportamento do agente e semântica da especificação.

Na prática, a separação rígida entre documentação do produto e comportamento do agente tende a não se sustentar. O projeto acaba reunindo especificações sobre o que será feito, como será feito e em que ambiente o trabalho ocorrerá, incluindo documentos como ADRs e demais artefatos acumulados ao longo do tempo. Isso não elimina a diferença conceitual entre as camadas, mas mostra que elas cooperam para viabilizar desenvolvimento assistido por agentes. O ganho está menos em isolar perfeitamente cada parte e mais em entender qual papel cada uma exerce.

Para observar os limites do SDD com clareza, vale começar com o agente sem instruções adicionais de ambiente. Essa configuração expõe o quanto a documentação, sozinha, consegue orientar a implementação e onde começam a surgir falhas de execução, validação e controle. A partir desses problemas, fica mais fácil decidir quais comportamentos devem migrar para o harness. Assim, os controles sobre o agente aparecem como resposta a limitações observadas, e não como premissas arbitrárias.

## Transcrição

00:00

Bom, pessoal, a gente estava falando de alguns pontos importantes,

00:04

principalmente entendendo que SDD não é mágica e também que não é

00:10

porque eu tenho uma especificação que eu vou conseguir sair gerando um código.

00:14

Então, eu quero que você entenda a linha de raciocínio que eu estou tomando aqui,

00:19

porque é uma zona cinzenta.

00:23

Então, o que acontece?

00:26

Normalmente, uma especificação, em geral, ela define o que a gente tem que fazer.

00:34

Eu especifico o que tem que ser feito.

00:37

Porém, para a gente é fácil inferir

00:40

e a gente pode também especificar como fazer.

00:44

Concorda comigo? Ou seja,

00:46

o que eu tenho que fazer está claramente ali na minha especificação.

00:50

O como fazer é uma outra história,

00:53

mas isso não significa que isso também não pode ser especificado.

00:59

Entendeu? Então, a grande sacada aqui é,

01:02

qual que é o limite que nós temos do como fazer?

01:07

Eu posso especificar um produto, uma arquitetura, um endpoint,

01:10

um layout, os padrões de teste? Ok.

01:14

Mas eu posso especificar que, ao finalizar uma tarefa,

01:18

a suíte de teste deve ser executada e um commit realizado?

01:22

Eu posso. Mas eu não sei se você consegue perceber, uma coisa é o que o sistema,

01:29

tem o que vai ser feito ali no sistema. A outra coisa,

01:34

ela trabalha muito mais sobre o comportamento

01:37

do processo de desenvolvimento desse sistema,

01:41

que em si é um tipo de especificação. Mas semanticamente falando,

01:47

esse tipo de especificação não tem necessariamente

01:51

relação direta com o produto em si.

01:58

Sobre os detalhes do produto.

02:00

Eles têm muito mais em relação a comportamentos e ambientes agentes,

02:06

que vão ajudar a gente a construir aquele produto baseado naquela especificação.

02:12

E a grande questão aqui é, se eu especifico que para IA,

02:16

quando finalizar uma tarefa, rodar o teste... Isso é spec-driven. Então,

02:21

por isso que eu estou dizendo aqui que existe uma zona cinzenta

02:25

e eu queria trazer isso aqui para que você refletisse também.

02:29

Vamos imaginar que eu tenho aqui o meu projeto, com as documentações,

02:32

com as especificações, com as architecture decision records,

02:36

os documentos todos que você vai gerando ao longo do tempo,

02:40

por exemplo, para trabalhar com spec-driven.

02:43

Por outro lado, eu tenho o ambiente, o comportamento do agente aqui,

02:49

algo que a gente chama de harness, ou seja, todo o ambiente,

02:53

todo o ecossistema que a gente vai dar para que o agente consiga

02:57

fazer a execução do que a gente tem aqui nessa especificação do nosso projeto.

03:05

O ponto aqui, quando a gente está falando de SDD, é até

03:10

que ponto esse

03:13

projeto ou essa especificação

03:17

colabora com o agente ou...

03:21

até que ponto esse comportamento do agente

03:25

aqui também pode estar aqui dentro dessas documentações.

03:30

Entendeu? Ou seja,

03:32

pedir para fazer um comitê no desenvolvimento com

03:35

Certeza pode ser um comportamento do agente,

03:38

mas eventualmente fazer um teste e verificar se

03:42

esse teste bate com os critérios de aceitação,

03:45

aí a coisa já fica diferente. Por quê? Testar é uma coisa.

03:50

mas o teste bate com o critério de aceitação. Então,

03:54

será que eu não teria que ter uma especificação de como

03:56

testar aqui para ele bater com os critérios de aceitação?

04:00

Então, essas coisas ficam nebulosas.

04:03

O grande ponto aqui é como eu separo isso.

04:08

Então, o fato importante é que, na prática, na minha opinião,

04:13

você não vai separar. Você vai tratar o seu projeto como um todo.

04:19

Ou seja, o seu projeto vai ter especificação do que vai ser feito,

04:22

como vai ser feito e sobre o ambiente e como a gente vai trabalhar.

04:26

Mas é importante para a gente entender, falando especificamente de SDD,

04:33

que nós vamos tratar, principalmente aqui nesse capítulo,

04:38

dessa parte.

04:39

Como que eu consigo gerar essas documentações para

04:43

eu pedir para o agente desenvolver.

04:46

E para a gente conseguir fazer isso da forma mais pura,

04:49

a gente vai fazer isso com o agente,

04:54

vamos dizer, pelado.

04:56

Como se o agente não tivesse nenhuma instrução sobre

04:59

o ambiente em que ele está desenvolvendo.

05:01

E ao longo do tempo a gente vai começar a perceber quais são os problemas

05:05

que a gente vai tendo e os controles que nós poderemos ter em relação ao agente.

05:10

Beleza? Então vamos lá no próximo vídeo para a gente

05:13

entender como é que vai funcionar essa nossa dinâmica.

## Resumo IA

**Abreviações**
*   **SDD**: Spec-Driven Development
*   **ADRs**: Architecture Decision Records

**Resumo**
A aula abordou a distinção crucial entre a especificação do produto ("o que" o sistema deve fazer) e a especificação do processo de desenvolvimento ("como" o agente deve se comportar) no contexto do Spec-Driven Development (SDD). O objetivo foi explorar a "zona cinzenta" onde essas duas formas de especificação se encontram e se complementam.

Foram detalhados conceitos como a especificação de produto (que inclui arquitetura, endpoints, layout e padrões de teste) e a especificação de processo (que envolve instruções para o fluxo de trabalho do agente, como "executar a suíte de testes e fazer um commit ao finalizar uma tarefa"). O instrutor enfatizou que, embora ambas sejam formas de especificação, a segunda não descreve o produto diretamente, mas sim o ambiente e o comportamento do agente que o constrói.

Foi introduzido o conceito de *harness*, que representa o ecossistema fornecido ao agente, englobando regras operacionais, automações e comportamentos esperados. O *harness* atua como uma camada de controle sobre a execução, enquanto a documentação do projeto (incluindo ADRs) continua sendo a referência principal do que deve ser construído. A complexidade surge quando instruções operacionais dependem de conhecimento do produto, exigindo que o *harness* se conecte a artefatos que detalham como testar e validar o produto.

A aula concluiu que, embora a separação conceitual seja importante, na prática, os projetos tendem a reunir especificações de "o que será feito", "como será feito" e "em que ambiente o trabalho ocorrerá". O instrutor propôs uma abordagem prática: iniciar o agente sem instruções adicionais de ambiente ("agente pelado") para identificar onde a documentação do produto, sozinha, é insuficiente para guiar a implementação e validação. As falhas observadas servirão de base para decidir quais comportamentos devem ser migrados para o *harness*, adicionando controles de forma reativa e estratégica.

**Pontos de atenção**
*   **SDD não é mágica:** Não basta ter uma especificação para garantir a geração automática de código; a compreensão da sua aplicação é fundamental.
*   **Distinção entre "o que" e "como":** É essencial diferenciar a especificação do produto (o que o sistema deve fazer) da especificação do comportamento do agente (como o processo de desenvolvimento deve ocorrer), pois elas representam duas fontes de verdade distintas.
*   **O papel do *harness*:** O *harness* é um ambiente de controle para o agente, definindo regras e automações, mas não é a especificação do produto em si. A documentação do projeto permanece como a fonte primária do que precisa ser construído.
*   **Validação dependente do produto:** Quando o comportamento do agente (ex: rodar testes) precisa verificar critérios de aceitação do produto, a fronteira se torna nebulosa. Nesses casos, o *harness* necessita de artefatos que expliquem como testar e validar o produto, conectando comportamento do agente e semântica da especificação.
*   **Integração prática das especificações:** Na prática, a separação rígida entre especificações de produto e processo é difícil de manter. Os projetos acabam acumulando ambas as formas de especificação (incluindo ADRs), e o valor reside em entender o papel de cada uma, e não em isolá-las perfeitamente.
*   **Boas práticas para adicionar controles:** Comece com um agente com poucas ou nenhuma instrução ambiental ("agente pelado") para identificar as falhas da documentação do produto na orientação da implementação, validação e controle. Adicione controles ao *harness* de forma incremental e estratégica, como resposta a problemas observados, e não como premissas arbitrárias.