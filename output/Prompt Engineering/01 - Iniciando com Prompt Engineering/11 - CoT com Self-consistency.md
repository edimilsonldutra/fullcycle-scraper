Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16577)

## Resumo da aula

Self-consistency é uma estratégia em que o modelo gera vários caminhos de raciocínio para a mesma pergunta e, ao final, escolhe a resposta que aparece com maior consistência entre eles. A técnica se apoia no Chain of Thought já conhecido, mas adiciona uma camada de robustez: em vez de confiar em uma única decomposição do problema, compara várias. Isso importa quando uma execução isolada pode conter um erro local de interpretação, cálculo ou inferência. O ganho esperado não é “pensar mais”, e sim reduzir a dependência de um único caminho possivelmente defeituoso.

A resposta final é escolhida por convergência entre os caminhos gerados, normalmente por maioria ou por agrupamento das conclusões equivalentes. Quando dois ou mais raciocínios chegam ao mesmo resultado e um terceiro diverge, a resposta divergente pode ser tratada como menos confiável. Esse mecanismo funciona como uma votação entre hipóteses produzidas pelo próprio modelo. Ele é útil em decisões técnicas, cálculos, interpretação de texto e questões de múltipla escolha, desde que o custo extra compense.

Outlier, nesse contexto, é um caminho de raciocínio cuja conclusão foge do padrão dominante entre as demais execuções. Ignorar outliers evita que uma resposta espúria, gerada por um desvio pontual, tenha o mesmo peso de respostas que convergiram entre si. Isso fica ainda mais relevante quando o prompt pede muitos caminhos, como 10 ou 20, porque a dispersão tende a aumentar. O critério, porém, depende de haver convergência suficiente; se todas as respostas divergirem, o sistema deveria assumir incerteza em vez de forçar uma conclusão.

Self-consistency aumenta custo de tokens e latência porque a mesma tarefa é resolvida várias vezes antes da consolidação final. Em tarefas simples, esse overhead costuma gerar pouco valor, já que uma única resposta direta tende a ser suficiente. A técnica também não garante correção: se o modelo errar de forma parecida em múltiplos caminhos, a votação apenas consolida o erro. Por isso, consistência é um sinal de estabilidade, não uma prova de verdade.

Retomando o cenário do endpoint que busca usuários e, em seguida, busca posts dentro de um loop, o ponto novo não é redefinir N+1, mas usar múltiplos raciocínios para validar a contagem de queries. O prompt pede três linhas de raciocínio passo a passo e, ao final, solicita um sumário com a resposta mais consistente, ignorando outliers. A estrutura prática é: gerar caminhos independentes, comparar as conclusões e escolher a maioria. Opcionalmente, o prompt ainda pode declarar que, se todas as respostas forem diferentes, a saída deve assumir que não há resposta consistente.

No experimento, um dos caminhos identificou corretamente N+1, enquanto outros caminhos erraram ao esquecer a query inicial ou ao imaginar uma otimização que não existia no código mostrado. Quando a maioria dos caminhos convergiu para N, o sistema escolheu N, mesmo sendo a resposta errada. Isso mostra o ponto pedagógico central da técnica: ela melhora robustez contra desvios isolados, mas não corrige um viés dominante do modelo. Se o erro for consistente, a consolidação também será.

Usando o mesmo prompt, modelos diferentes podem produzir distribuições diferentes de caminhos e, por consequência, resultados finais diferentes. No caso testado, o GPT-3.5 Turbo variou entre execuções e chegou a consolidar a resposta errada por maioria, enquanto o GPT-4o convergiu repetidamente para N+1. A técnica, portanto, não elimina a influência do modelo base; ela apenas organiza melhor a decisão a partir das saídas que esse modelo consegue gerar. Isso reforça a necessidade de avaliar qualidade, custo e estabilidade em conjunto.

Self-consistency vale a pena quando o custo de uma resposta errada é relevante e existe benefício em comparar múltiplos caminhos antes de decidir. Ele é especialmente útil em problemas com ambiguidade local, etapas de cálculo ou análise técnica em que um único raciocínio pode falhar por descuido. Em contrapartida, não faz sentido transformá-lo em padrão para toda requisição, porque o ganho depende da natureza da tarefa. A escolha deve ser intencional: mais robustez em troca de mais processamento.

## Transcrição

00:01

Agora, pessoal, eu quero falar com vocês de um cara que é colocado em conjunto com o Chain of Thought, que acaba sendo um mecanismo, na realidade, chamado self-consistency, ou seja, a autoconsistência. Para que serve esse cara?

00:16

Muitas vezes eu posso pedir para o modelo raciocinar, e com o raciocínio que ele dá, pode ser um raciocínio errado, e ele me dá uma resposta errada. Para eu tentar garantir mais consistência nas minhas respostas, o que eu posso fazer? Eu posso pedir para ele fazer isso várias vezes, e ele escolher qual é a resposta mais consistente do que ele mesmo gerou.

00:38

Ou seja, ele pode confirmar cálculo, ele pode validar hipóteses diferentes, ele pode classificar sentimento, ele pode revisar a interpretação de um mesmo texto, ele pode decidir melhor em uma opção múltipla escolha, né? E quais são limitações? Gasta mais token, pode ser mais lento, nem sempre ele vai convergir para a resposta correta, em tarefas fáceis ele não vai agregar muito valor e ele pode repetir respostas redundantes. Então, isso aí é uma parada muito louca. Eu vou dar um exemplo. Imagina que você tem uma prova, né? E...

01:07

e você passa para a A responder, a questão A, B, C ou D, e ela lê as respostas. E daí ela dá A, e tem uma hora que você pergunta e ela escolhe a B. O que você pode fazer? Você pode usar um prompt de self-consistency com chain of thoughts, onde ela elabora a linha de raciocínio,

01:23

diversas vezes, e daí ela meio que soma o que teve mais consistente na linha de raciocínio dela e fala qual que é a resposta. Ou seja, ela pensa várias vezes na mesma resposta e, se tiver respostas diferentes, ela escolhe a maioria. Mais ou menos desse tipo, falando grosseiramente falando.

01:39

Então, deixa eu trazer aqui pra você essa parte aqui de self-consistency, porque é bem importante e é muito útil, principalmente quando você está na dúvida de tomar alguma decisão técnica, ou de fazer um cálculo, ou fazer um algoritmo, ou até mesmo...

01:57

fazer uma prova ou propor um documento ou qualquer coisa desse tipo. Então, olha só, eu tenho uma única mensagem aqui que é a seguinte. A questão é, num endpoint de uma API que retorna uma lista de usuários com os seus posts, o desenvolvedor escreveu.

02:16

users dbFetchAllUsers, e daí ele dá um for, e para cada usuário ele faz a busca dos posts, tá? E aí a pergunta para ele é...

02:29

Quantas queries no banco de dados foram executadas para N users? Por que eu fiz essa pergunta, na realidade? Porque ela é uma pergunta clássica para quem está começando a programar ou para quem já detonou muito banco de dados por aí, que é o problema do N mais 1.

02:50

Ou seja, existem várias formas de você consultar bastante coisa sem iterar por cada loop para cada usuário. Mas nesse caso aqui, o que acontece é o seguinte, quando ele faz essa validação,

03:08

a gente sempre tem algumas coisas interessantes. Por exemplo, ele sempre vai ter n mais 1, ou seja, a primeira consulta principal para pegar a lista dos usuários e uma consulta para o usuário. Então, eu sempre vou ter um número de n mais uma consulta, tá? Então, aqui o meu prompt, que é o mais importante, não é eu ensinar para você o que é n mais 1. Se você é desenvolvedor, você sabe o que é n mais 1. Mas, a minha pergunta aqui para ele está o seguinte, olha, gere três

03:37

Linhas de raciocínio diferentes passo a passo. Ao final, sumarize as respostas e escolha a resposta mais consistente, ignorando outliers, ou seja, aquela resposta espúria. Por quê? Porque às vezes eu posso pedir mais de três, por exemplo. Posso pedir dez, vinte. Ou seja, aquelas que são muito diferentes, ele ignora.

04:00

E eu coloquei um if aqui no final, mas eu vou admitir que eu consegui reproduzir esse if pouquíssimas vezes aqui no meu teste, mas eu vou deixar aqui pra você. Eu coloquei o seguinte, se as três respostas forem diferentes,

04:15

apenas responda, eu não consigo encontrar uma resposta consistente, beleza? Então, é basicamente isso que eu vou fazer, e a gente vai testar em modelos diferentes aqui também, tá? E vamos ver como é que saem as respostas, para ver como é que estão, para ver se a IA já vai fazer aquele seu algoritmo de N mais 1, você se enrolar com ele na hora de você desenvolver o programa, tá? Então, vou colocar aqui, ó, Python,

04:43

Aqui, 1, 3.1, né? Aqui, self-consistency. Então, eu vou rodar esse cara aqui.

04:51

E, galera, eu fico empolgado mesmo porque pode parecer umas coisas malucas, mas isso muda completamente a forma de como a gente programa e como a gente entrega a software, tá? Então, vamos lá. Aqui está meu prompt que eu fiz e aqui tem as respostas. Primeiro passo, né? Porque eu falei para ele pensar em path, né? Primeiro passo. Para cada usuário na lista de usuários, o código é executado uma query buscando por usuário. Logo, né?

05:19

Para N usuários, eu tenho N queries para ser executada. Ou seja, ele já errou aqui, porque ele esqueceu de somar, de contar a query onde eu dou users. Ou seja, ele só fez N, não teve o N mais 1. Segunda linha de raciocínio. O código, primeiro, busca todos os usuários no banco de dados com o dbFindUsers, o que vai resultar numa query. Depois, cada usuário é feito a uma busca por ID.

05:49

Então, para N usuários, o total de queries pode ser N mais 1.

05:54

E o terceiro caminho é, dependendo da implementação do dbFindUsers e o dbFindByUserId, essas funções podem otimizar e fazer uma única query que vai pegar todos os dados necessários. Nesse caso, independente do número de usuários, o código pode potencialmente executar duas queries, uma para pegar todas e outra para trazer todos os IDs.

06:22

Cara, ele viajou aqui, né? Porque eu tô num loop ali, na realidade, no meio da história, né? Então, o sumário, a resposta mais consistente...

06:30

Para isso, é de N users que o código vai ser usado nqueries, e esse reasoning é baseado no fato que cada usuário separado vai dar e etc., ele vai trazer como N users. Então, olha só que interessante, galera. O cara errou feio. Ele gerou a hipótese correta, ele gerou três diferentes, ele não seguiu o meu if e respondeu errado para mim.

06:54

Paciência, GPT 3.5 Turbo. Vou rodar de novo esse modelo para ver o que ele retorna aqui de novo, tá? Então, ó, vamos lá, só vou bater o olho aqui. PF número 1, ele deu N mais 1.

07:07

PATH número 2, ele deu n mais 1. PATH número 3, ele deu n mais 1. A resposta mais consistente, baseada nas três, é n mais 1. Então, perceba que eu executei o mesmo prompt duas vezes e agora ele acertou as três. Vamos ver se ele erra aqui para a gente.

07:25

A primeira aqui, ele falou que é N, errou. A segunda, ele falou que é N. E a terceira, ele falou que é N mais 1. Baseado no que ele acabou colocando, ele falou que é N, porque teve duas N e uma N mais 1. Ou seja, o 3.5, ele está sendo consistente. Se concordar comigo, ele está sendo. Ele está pegando a que trouxe mais consistência, mas que, infelizmente, é a resposta errada.

07:52

Mas isso aqui é self-consistency, você pode rodar várias vezes. Vamos testar aqui no GPT-4O, aqui pra gente ver o que ele traz aqui pra gente, tá? Só por curiosidade, mas eu acho que vocês entenderam a ideia principal do self-consistency, né? Você pede pra esses caminhos ali pra ele. Então, vamos lá.

08:14

Caminho número 1, ele gera toda a linha de raciocínio, e ele dá que dá N mais 1. A segunda, ele traz que dá N mais 1 também. A terceira, ele traz que dá N mais 1, e aí ele acertou. Vou rodar de novo só para ver se ele dá alguma deliradinha aqui ou não, mas eu acho que ele vai acertar o 4o mais inteligente do que o 3.5, aparentemente. Vamos ver se ele vai errar ou não.

08:41

Aqui, ele trouxe N mais 1 no primeiro caminho, segundo caminho N mais 1, terceiro caminho N mais 1. Então, agora ele está acertando aqui pra gente. Independente se ele acertou ou não, galera, o que eu queria que você entendesse é que esse cara aqui é o que faz gerar o self-consistency ali pra gente. Beleza? Então, estamos vistos aí, self-consistency aí na prática. Deu pra gente sentir também como modelos mudam o resultado pra gente.

## Resumo IA

**Abreviações**
- **CoT** — *Chain of Thought* (cadeia de raciocínio)
- **N+1** — padrão de problema em que uma consulta inicial é seguida por mais N consultas individuais, totalizando **N + 1** queries
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **GPT** — *Generative Pre-trained Transformer* (Transformador Generativo Pré-treinado)
- **Turbo** — variante/modelo otimizado para maior velocidade e menor custo, citado como **GPT-3.5 Turbo**
- **GPT-4o** — versão do modelo **GPT-4 Omni**
- **Python** — linguagem de programação Python

**Resumo**
A aula apresentou a técnica de **self-consistency**, usada em conjunto com **Chain of Thought**, para aumentar a robustez das respostas de modelos de linguagem. A ideia central é fazer o modelo gerar vários caminhos de raciocínio para a mesma questão e, ao final, consolidar a resposta mais consistente entre eles, normalmente por maioria. O instrutor destacou que essa abordagem não serve para “pensar mais”, mas para reduzir a dependência de um único raciocínio, que pode conter erro local de interpretação, cálculo ou inferência.

Foram explicados os principais usos da técnica, como validação de cálculos, classificação de sentimento, revisão de texto, decisões em múltipla escolha e problemas técnicos em geral. Também foram apontadas limitações importantes: maior consumo de tokens, maior latência, possibilidade de respostas redundantes e o fato de que a técnica não garante correção, apenas estabilidade estatística entre os caminhos gerados. O instrutor reforçou que consistência não é prova de verdade; se o modelo errar de forma semelhante em vários caminhos, o erro pode ser consolidado como resposta final.

Na parte prática, foi mostrado um exemplo envolvendo um endpoint de API que busca usuários e, dentro de um loop, busca os posts de cada usuário, com o objetivo de identificar quantas queries no banco seriam executadas para N usuários. O prompt pedia três linhas de raciocínio independentes e, ao final, um sumário com a resposta mais consistente, ignorando outliers. O exemplo foi usado para discutir o problema clássico de **N+1 queries** e para demonstrar como a consolidação por maioria funciona na prática. Em testes com modelos diferentes, o instrutor observou que o GPT-3.5 Turbo podia convergir para a resposta errada por maioria, enquanto o GPT-4o tendia a convergir corretamente para N+1, reforçando que a técnica depende da qualidade do modelo base.

**Pontos de atenção**
- Self-consistency **aumenta custo** de tokens e **latência**, pois a mesma tarefa é resolvida várias vezes.
- A técnica **não garante correção**; se o modelo estiver enviesado, a maioria pode consolidar uma resposta errada.
- Em tarefas simples, o overhead geralmente **não compensa**.
- É importante **ignorar outliers**, mas somente quando existe convergência suficiente entre os caminhos.
- Se todas as respostas divergirem, o comportamento mais seguro é **assumir incerteza** em vez de forçar uma conclusão.
- O resultado depende fortemente do **modelo base**; modelos diferentes podem apresentar distribuições diferentes de raciocínios e conclusões.
- A abordagem é mais indicada quando o custo de errar é alto e há valor real em **comparar múltiplos caminhos** antes de decidir.
- O uso de self-consistency deve ser **intencional e seletivo**, não como padrão para toda requisição.
- Em exemplos técnicos, é preciso cuidar para não deixar o modelo **“viajar”** em hipóteses de otimização inexistentes ou fora do contexto do código.
- A técnica melhora a robustez contra erros isolados, mas **não corrige erros dominantes** do modelo.