Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17889)

## Resumo da aula

Guardrails e constraints são mecanismos que reforçam, de forma explícita, como o sistema deve evoluir durante a execução por agentes. Eles existem porque, mesmo com uma arquitetura bem definida, a geração contínua de código tende a introduzir desvios graduais de padrão, dependência e organização. Retomando o ambiente e os princípios já estabelecidos, o ponto novo aqui é transformar essas regras em verificações objetivas que impedem deriva arquitetural antes que ela se acumule.

Uma arquitetura em camadas já embute restrições verificáveis: service não deve importar UI, type não deve depender de outras camadas e config pode ter leitura mais ampla. Essas relações não precisam ficar apenas como convenção escrita ou expectativa no prompt. Quando a regra é estrutural e observável no código, ela pode ser convertida em uma checagem binária: permitido ou proibido.

Linters customizados são programas que analisam o código gerado para detectar violações específicas do projeto, como quebra de hierarquia entre módulos. Em vez de pedir ao modelo que “julgue” se algo parece correto, o linter executa uma regra formal e retorna um resultado inequívoco. Isso reduz ambiguidade, aumenta previsibilidade e desloca parte do controle de qualidade do campo probabilístico para o mecânico.

O enforcement só produz efeito consistente quando a verificação é obrigatória no fluxo de trabalho. Por isso, essas checagens devem rodar antes de commits, ao final de uma tarefa ou em hooks que o agente seja forçado a executar. Se houver violação, o sistema pode sinalizar diretamente ao agente onde a regra foi quebrada, criando um ciclo de correção guiado por feedback objetivo.

Nem toda validação precisa de modelo. Se a regra pode ser expressa como “sim ou não”, como impedir regra de negócio em controller ou bloquear chamadas diretas de controller para repositório, um software determinístico é mais barato, mais rápido e mais confiável. O uso de IA continua válido para casos ambíguos, mas regras preto no branco devem ser capturadas por mecanismos formais sempre que possível.

Enforcement mecânico reduz consumo de tokens porque evita delegar ao modelo verificações que um script resolve com custo muito menor. O ganho principal, porém, não é apenas financeiro: ele aumenta a confiança de que certas invariantes do sistema serão respeitadas ao pé da letra. Quanto mais regras relevantes forem convertidas em validações determinísticas, mais o agente passa a operar dentro de limites definidos por engenharia, e não apenas por instrução textual.

## Transcrição

00:00

Bom, pessoal, e agora a gente entra numa parte que é uma das partes que eu acho mais importantes,

00:07

inclusive, sobre Harness Engineering,

00:09

que é quando a gente está falando de Guardrails e Constraints. Ou seja,

00:14

são pontos onde a gente consegue reforçar como

00:19

que a gente quer que o nosso sistema funcione.

00:22

E o porquê que eu estou dizendo isso?

00:24

Novamente, a gente já comentou, conforme o software vai sendo desenvolvido,

00:28

a gente, aos poucos, a gente vai tendo desvios.

00:32

A IA pode começar aos pouquinhos e mudando a forma,

00:37

o padrão, a arquitetura da sua aplicação e etc.

00:41

Então, o que acontece?

00:43

Muitas vezes, a gente tem uma arquitetura clara do nosso sistema.

00:47

Ah, eu tenho o tipo, eu tenho a parte de configuração, eu tenho o repositório,

00:52

que daí tem o service, que vai para um runtime, que depois vai para uma UI.

00:57

Se eu tenho esse padrão, eu tenho algumas coisas claras ali. Por exemplo,

01:02

a minha UI jamais pode importar um service diretamente.

01:05

Quer dizer, ela pode importar um service,

01:07

mas o service não pode importar a UI. Uma config pode ser lida por qualquer camada.

01:12

Um type não depende de nada. Se você perceber, no nosso software existem padrões.

01:19

Uma vez que você entende esses padrões,

01:21

você pode fazer algumas coisas e isso aí é super importante.

01:26

A primeira coisa que eu recomendo que você faça é criar linters customizados. O que significa?

01:34

Você pode fazer um programa que, e a gente vai ver isso inclusive,

01:40

que vai rodar em cima de todo o código que

01:43

foi gerado e vai verificar se existe alguma quebra de hierarquia,

01:47

por exemplo. Se houver essa quebra de hierarquia,

01:50

esse linter pode simplesmente avisar o...

01:56

o próprio agente falando, olha, você quebrou aqui,

02:01

isso aqui não deveria estar sendo feito dessa forma. Então,

02:05

esse tipo de coisa é super importante.

02:07

E o mais interessante é que esses tipos de linter,

02:10

por exemplo, ou ferramentas e etc., você não precisa usar IA para validar.

02:16

Pode ser algo realmente determinístico,

02:18

sim ou não. Ou seja... É um software que roda, toda vez antes de dar um commit,

02:23

ou toda vez que a IA fala que ela terminou uma tarefa,

02:27

simplesmente você força ela a executar,

02:30

você bota um hook, você faz alguma coisa para que aquele software seja executado.

02:36

Quando isso acontece,

02:37

você consegue garantir consistência no seu sistema

02:40

e você vai evitar esses tipos de desvio.

02:44

Então pense nesse caso ali, como que eu consigo fazer um enforcement mecânico?

02:50

Entendeu? E não necessariamente apenas de forma probabilística.

02:54

Muita gente com IA utiliza muito o modelo para fazer

02:58

essas análises e não tem nada de errado.

03:00

Mas existem algumas coisas que podem ser preto no branco dentro

03:03

da sua aplicação que vai fazer você economizar token,

03:06

vai ser mais rápido e você vai garantindo e tendo

03:10

cada vez mais certeza que algumas regras que você consegue,

03:14

que você quer, elas sejam cumpridas ali ao pé da letra.

03:19

Ou seja, você não tem ambiguidade, é regra binária. Então,

03:23

Não tem como você colocar uma regra de negócio no seu

03:29

controller ou fazer o seu controller chamar o seu repositório diretamente.

03:34

Não, você pode fazer softwares ali que façam essas validações. Então,

03:39

esses guardrails, essas constraints, elas vão permitir com que você evite...

03:46

alguns desvios que às vezes eles são os desvios

03:49

grosseiros e a gente acaba deixando passar.

03:52

Então o linter é apenas uma das coisas que você pode fazer.

03:58

Agora pense hoje no seu sistema o que você acha que

04:02

a IA está fazendo de errado e que você pode melhorar.

04:05

Mas essa melhora não é apenas no prompt.

04:09

É em, sei lá, que script você pode fazer que consegue validar.

04:14

Se a IA não fez besteira em determinada parte do seu software. Então,

04:18

quanto mais determinístico você for eventualmente,

04:23

mais claro vai ser se você está fazendo com que

04:28

o agente seja guiado por você da melhor forma possível. Fechou?

## Resumo IA

**Abreviações**
*   IA: Inteligência Artificial

**Resumo**
O objetivo desta aula é apresentar os conceitos de Guardrails e Constraints como mecanismos fundamentais no Harness Engineering. Eles servem para reforçar, de forma explícita e obrigatória, como o sistema deve evoluir durante a execução por agentes, evitando o desvio arquitetural gradual que a geração contínua de código pode introduzir, mesmo em arquiteturas bem definidas.

A aula destacou que as regras arquiteturais, como as de uma arquitetura em camadas (ex: service não deve importar UI, type não deve depender de outras camadas, config pode ter leitura ampla), podem e devem ser transformadas de meras convenções ou expectativas de prompt em verificações objetivas e binárias (permitido ou proibido). Para isso, a ferramenta principal abordada são os linters customizados — programas determinísticos que analisam o código gerado para detectar violações específicas do projeto, como quebras de hierarquia.

O instrutor explicou que o enforcement dessas regras só é eficaz quando a verificação é obrigatória no fluxo de trabalho. As checagens devem rodar antes de commits, ao final de uma tarefa ou por meio de hooks que forcem o agente a executá-las. Em caso de violação, o sistema deve sinalizar diretamente ao agente o ponto da quebra, criando um ciclo de correção guiado por feedback objetivo. A priorização de validações determinísticas para regras "preto no branco" é enfatizada, pois são mais baratas, rápidas, confiáveis e economizam tokens em comparação com a delegação dessas verificações a modelos de IA.

**Pontos de atenção**
*   **Desvio Arquitetural é Constante:** Mesmo com uma arquitetura bem definida, a geração contínua de código por agentes pode introduzir desvios graduais de padrão, dependência e organização.
*   **Evitar Ambiguidades:** Não dependa apenas de convenções escritas ou expectativas no prompt; transforme regras estruturais e observáveis no código em checagens binárias (permitido ou proibido) para reduzir ambiguidade e aumentar a previsibilidade.
*   **Obrigatoriedade da Verificação:** O enforcement das regras só produz efeito consistente se a verificação for obrigatória no fluxo de trabalho (ex: antes de commits, ao final de uma tarefa, via hooks).
*   **Priorizar Validações Determinísticas:** Para regras "preto no branco" que podem ser expressas como "sim ou não" (ex: impedir regra de negócio em controller, bloquear chamadas diretas de controller para repositório), utilize software determinístico como linters customizados. Isso é mais barato, rápido e confiável do que delegar a validação a modelos de IA, além de economizar tokens.
*   **Feedback Objetivo ao Agente:** Em caso de violação, o sistema deve sinalizar diretamente ao agente onde a regra foi quebrada, criando um ciclo de correção guiado por feedback objetivo.
*   **Confiança nas Invariantes:** Quanto mais regras relevantes forem convertidas em validações determinísticas, maior a confiança de que certas invariantes do sistema serão respeitadas ao pé da letra, fazendo o agente operar dentro de limites definidos por engenharia e não apenas por instrução textual.
*   **Além do Prompt:** A melhoria no comportamento da IA não se resume apenas a prompts melhores, mas também à criação de scripts e ferramentas que validem e corrijam o código gerado mecanicamente.