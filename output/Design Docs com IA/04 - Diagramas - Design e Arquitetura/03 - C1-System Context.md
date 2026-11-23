Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17072)

## Resumo da aula

C1, no modelo C4, é a visão de contexto: ele mostra o sistema a partir de fora, no ambiente em que opera. O foco não está na estrutura interna, mas em responder quem usa o sistema, com quais outros sistemas ele se integra e qual papel ele cumpre no ecossistema. Esse nível é útil quando vários times precisam alinhar rapidamente fronteiras, responsabilidades e dependências sem abrir detalhes de implementação.

A granularidade do C1 é deliberadamente alta. Em ecossistemas com muitos microserviços, essa escolha reduz ruído e destaca apenas relações arquiteturalmente relevantes: consumidores, atores e integrações externas. Retomando a leitura progressiva do mesmo sistema, aqui o objetivo ainda não é abrir containers ou componentes, mas fixar o recorte correto do que será aprofundado depois.

O caso do Rate Limiter é menos óbvio porque o sistema central não é um serviço isolado, mas um SDK embutido em outros serviços. Mesmo assim, ele pode ser tratado como o sistema do diagrama quando a intenção é documentar seu contexto operacional: quem o utiliza, quem o configura e de quais dependências externas ele precisa. Isso evita que a biblioteca desapareça visualmente dentro dos microserviços consumidores e permite explicitar seu papel arquitetural.

O System Boundary delimita o que pertence ao sistema sendo documentado e o que está fora dele. No diagrama, essa fronteira separa o que é desenvolvido e mantido como Rate Limiter das pessoas e sistemas que interagem com ele. Sem essa marcação, o leitor pode confundir o SDK com a plataforma inteira de microserviços ou interpretar dependências externas como partes internas da solução.

No contexto do Rate Limiter, o usuário final aparece porque interage com os Endpoints HTTP protegidos pelo middleware. O desenvolvedor também entra como ator relevante, porque integra, mantém e configura o SDK nos serviços consumidores. Essa inclusão faz sentido quando o sistema central é uma biblioteca embutida, já que parte importante do seu uso acontece por integração técnica, não por interface direta de negócio.

Os microserviços da plataforma são consumidores diretos da biblioteca de Rate Limiting embutida. Eles usam o SDK para tomar decisões de Allow/Deny nas requisições HTTP e para padronizar a observabilidade associada a esse controle. No C1, esses serviços aparecem como sistemas ao redor do Rate Limiter, não como detalhamento interno dele.

Um sistema de Rate Limiting distribuído precisa manter contadores por chave, como IP, usuário ou outro identificador. Quando várias instâncias do mesmo serviço estão rodando, esses contadores não podem ficar apenas em memória local, porque cada instância veria um estado diferente. Por isso, o diagrama mostra um armazenamento compartilhado de estado como dependência externa opcional para sustentar a limitação de forma consistente.

A exportação de métricas e traces também aparece no contexto porque o Rate Limiter não opera isoladamente: ele precisa alimentar a camada de observabilidade do ecossistema. Essa integração externa permite acompanhar volume de requisições, decisões de bloqueio e comportamento operacional do mecanismo. Em um C1, isso importa menos pelo detalhe técnico da instrumentação e mais por deixar explícito que observabilidade faz parte do contrato arquitetural do sistema.

Em sistemas tradicionais, o nome do serviço costuma bastar para comunicar sua função. Já em uma biblioteca embutida, uma anotação curta de propósito pode ser valiosa para esclarecer rapidamente o que ela faz: limitar por chave, IP ou plano, tomar decisões locais, usar estado compartilhado opcional e padronizar observabilidade. Essa anotação não é obrigatória, mas ajuda quando o elemento central do diagrama não é um processo independente e poderia parecer genérico demais.

O recorte final do C1 do Rate Limiter fica assim: no centro, a biblioteca/SDK; ao redor, usuário final, desenvolvedor, microserviços consumidores, storage compartilhado e sistema de observabilidade. Esse desenho responde onde o Rate Limiter vive, quem o usa, quem o configura e de quais sistemas externos depende. A estrutura interna ainda permanece fechada; essa abertura fica para o próximo nível, quando o mesmo sistema for detalhado em C2.

## Transcrição

00:01

Bom, pessoal, agora que nós fomos propriamente, vamos dizer assim, introduzidos a esse mundo do diagrama C4, eu queria trazer aqui para vocês um resumo para que você consiga entender a ideia, mas também para que você consiga visualizar um tipo de diagrama, tá? E que para que nós possamos estar sempre na mesma página e a gente não ficar trocando de exemplos, de domínio de exemplos, tá?

00:29

Eu estou seguindo sempre aqui a linha daquele projeto que a gente fez do Rate Limiter, tá? Então, a nossa ideia aqui é sempre utilizar ele como um estudo de caso, vamos dizer assim, para que nós possamos trabalhar, beleza? Então, vamos lá, pessoal. C1.

00:45

Então, aqui é o nosso primeiro tipo de diagrama, ou seja, C1 significa System Context. E a ideia aqui é que você consiga ter uma visão externa, uma visão muito mais em alto nível. Então, o C1 vai definir o sistema no ambiente que ele opera.

01:05

Ele vai identificar os usuários, os consumidores e as integrações externas. Ele é muito bom para alinhamento entre diferentes times, como desenvolvimento, produto, segurança e etc. É interessante porque esse diagrama é bem de alto nível.

01:21

E o interessante disso é que quando você está num ecossistema muito grande, onde você tem ali milhares de microserviços e sistemas se comunicando, esse tipo de diagrama, apesar de ele ser extremamente alto nível, ele consegue deixar claramente uma visão de com quem esse sistema conversa.

01:42

Quem esse sistema... Com quem esse sistema fala? Quem usa esse sistema? Quem esse sistema usa? Qual que é a ideia desse camarada? Então, isso aqui é um exemplo do nosso sistema de Rate Limiter. Eu coloquei aqui, se você perceber aqui como C1, que é o System Context, e eu coloquei aqui uma plataforma de microserviços. Vamos imaginar que nós temos

02:10

diversos microserviços dentro de uma plataforma. Então, nesse momento, somente para facilitar, eu estou chamando isso de system, ou seja, é o sistema e, nesse caso, como a gente está trabalhando, vamos dizer, com o SDK de um rate limiter, as coisas acabam ficando um pouco mais ainda

02:30

interessantes, porque a gente pode estar falando de diversos sistemas ao mesmo tempo que vão utilizar o Rate Limiter, tá? Então, aqui, o que acontece? Vamos imaginar que eu tenho o usuário final que está interagindo com Endpoints HTTP, tá? Porque, principalmente, o nosso Rate Limiter está funcionando, ele vai funcionar somente como Middleware HTTP, beleza? Eu tenho também o desenvolvedor que vai falar com esse sistema, mas nesse ponto, que é manter e integrar o serviço.

02:59

E por que eu estou colocando o desenvolvedor como um stakeholder? Porque, especificamente no caso do Rate Limiter, ele vai interagir com o quê? Criando esse SDK, mantendo esse SDK, configurando esse SDK. Então, por isso que eu acabei colocando nesse nível de granularidade. Mas, normalmente, a gente coloca mais sistemas caras externos falando. Se você perceber aqui, eu tenho essas linhas

03:25

tracejadas, onde define aonde está o escopo do que eu desenvolvo. E atrás, em volta, mostra quem interage com quem. Beleza? Então, nesse nosso caso, eu tenho usuário final e eu coloquei o desenvolvedor aqui para...

03:41

para integrar os serviços, e aqui tem microserviços da plataforma, são serviços com biblioteca de Rate Limiting embutida para decidir Allow barra Deny e padronizar observabilidade. Então, o que acontece se você olhar aqui? Esse nosso sistema vai utilizar um armazenamento compartilhado de estado,

04:03

para o back-end, opcionalmente, para ele ter essa limitação. O que isso significa, pessoal? Que quando eu tenho um sistema de rate limiting, eu quero manter o estado, ou seja, eu quero continuar contando quantas pessoas ou quantos

04:21

quantas vezes um determinado IP ou um usuário está acessando aquele meu sistema, e para que eu consiga fazer isso de forma distribuída, ou seja, imagina que eu tenho um sistema com diversas instâncias rodando exatamente o mesmo sistema, como é que eu consigo fazer o rate limiting de todos esses caras? Fazendo com que eu acesse uma base compartilhada, onde nós vamos ter os contadores para ver quantas, quantas requisições já foram feitas por determinado usuário.

04:51

Isso aqui é uma coisa, ou seja, ele mantém os contadores por uma chave. O outro ponto aqui é exportar métricas e traces, ou seja, eu tenho um sistema que vai trabalhar com a parte de observabilidade para a gente pegar as métricas e os traces.

05:06

Aqui, tá? É importante você conseguir ver que eu acabei colocando uma anotação, tá? Essa anotação, muitas pessoas falariam que não vale a pena colocar no C1 e outras pessoas talvez falassem que seria interessante. Eu coloquei explicitamente essa anotação, por quê?

05:28

Porque como isso é um sistema que está embutido em um outro sistema, eu queria deixar claro aqui que a ideia desse Rate Limiting é eu conseguir garantir o limite por chave, por IP, por plano, as decisões locais com estado compartilhado opcional e a observabilidade padronizada entre os serviços. E por que eu estou falando especificamente disso?

05:51

porque é o propósito do sistema, tá? E o porquê que eu estou dizendo que é o propósito? Para que quem olhe esse nosso sistema entenda do que a gente está falando nesse caso especificamente, porque a gente está falando de um SDK, tá? Ou seja,

06:08

é uma biblioteca, no final, o que a gente está desenvolvendo, né? Então, não é algo tão comum que a gente acaba colocando, ah, eu tenho um microserviço A, que fala com o B, que fala com o C. Não! Nesse caso, a nossa biblioteca está embedada dentro de um serviço. Então, isso aqui é uma anotação, não é obrigatório, mas vale a pena a gente entender como é que funciona isso aqui, de forma geral, tá? Agora,

06:33

Como que vai funcionar a nossa dinâmica aqui, tá? Somente para que você consiga entender um pouquinho melhor de como que a gente vai seguir. Eu vou mostrar aqui para vocês os quatro C's, tá? E depois que a gente olhar esses quatro C's, a gente vai para o código. E aí eu vou mostrar para você qual é o código que gera esses diagramas, tá? Mas, ao mesmo tempo, eu vou mostrar para vocês como que

07:01

A inteligência artificial é capaz de também fazer essa geração desse diagrama para você. Beleza? Então vamos nessa porque a gente tem o C2 para a gente ver em seguida.

## Resumo IA

**Abreviações**
- **C1** — *System Context* (Contexto do Sistema)
- **C4** — *C4 Model* (Modelo C4)
- **SDK** — *Software Development Kit* (Kit de Desenvolvimento de Software)
- **HTTP** — *Hypertext Transfer Protocol* (Protocolo de Transferência de Hipertexto)
- **IP** — *Internet Protocol* (Protocolo de Internet)

**Resumo**
A aula apresentou o nível C1 do modelo C4, chamado *System Context*, com foco em mostrar o sistema de forma externa, no ambiente em que ele opera. O instrutor explicou que, nesse nível, o objetivo não é detalhar estrutura interna, mas identificar usuários, consumidores, integrações externas e o papel do sistema no ecossistema, favorecendo o alinhamento entre times em cenários com muitos microserviços.

Como estudo de caso, foi usado o Rate Limiter. O instrutor destacou que, mesmo sendo uma biblioteca/SDK embutida em outros serviços, ele pode ser tratado como o sistema central do diagrama quando a intenção é documentar seu contexto operacional. Para isso, a fronteira do sistema (*System Boundary*) separa o que faz parte do Rate Limiter do que está fora dele, evitando confusão entre a biblioteca e a plataforma de microserviços em que ela está inserida.

No diagrama de contexto, aparecem o usuário final, que interage com endpoints HTTP protegidos por middleware, e o desenvolvedor, que integra, mantém e configura o SDK. Também aparecem os microserviços consumidores da plataforma, que usam a biblioteca para tomar decisões de *Allow/Deny* nas requisições e padronizar a observabilidade. Além disso, foi explicado que um sistema de rate limiting distribuído precisa de armazenamento compartilhado de estado para manter contadores por chave, como IP ou usuário, já que várias instâncias não podem depender apenas de memória local.

A observabilidade também foi colocada como parte do contexto, por meio da exportação de métricas e traces, deixando claro que esse aspecto faz parte do contrato arquitetural do sistema. O instrutor comentou ainda que uma anotação curta de propósito pode ser útil nesse tipo de diagrama, especialmente quando o sistema central é uma biblioteca embutida e poderia parecer genérico demais. Ao final, ele resumiu o recorte do C1 como a biblioteca/SDK no centro, cercada por usuário final, desenvolvedor, microserviços consumidores, armazenamento compartilhado e sistema de observabilidade, preparando a transição para o próximo nível, o C2.

**Pontos de atenção**
- O C1 deve permanecer em alto nível; não é o momento de abrir containers, componentes ou detalhes internos.
- Em ecossistemas com muitos microserviços, o diagrama deve reduzir ruído e destacar apenas relações arquiteturalmente relevantes.
- A *System Boundary* é essencial para não confundir o sistema documentado com a plataforma inteira ou com dependências externas.
- No caso de bibliotecas/SDKs embutidos, pode ser necessário representá-los como sistema central para não “sumirem” dentro dos consumidores.
- O desenvolvedor pode aparecer como ator relevante quando sua interação com o sistema envolve integração, manutenção e configuração do SDK.
- Para rate limiting distribuído, não se deve depender apenas de memória local; é preciso estado compartilhado para manter consistência entre instâncias.
- Os contadores devem ser mantidos por chave, como IP, usuário ou plano, para que a limitação faça sentido operacionalmente.
- Observabilidade não é detalhe periférico: métricas e traces fazem parte do contexto arquitetural do sistema.
- Anotações de propósito no C1 não são obrigatórias, mas ajudam quando o sistema central é uma biblioteca embutida e o objetivo precisa ficar explícito.
- O C1 serve para fixar o recorte correto antes de avançar para níveis mais detalhados, como o C2.