Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16747)

## Resumo da aula

Então vamos entender agora, rapidamente, o fluxo bem básico que acontece nesse processo. Caso você não tenha captado totalmente a ideia do que eu acabei de explicar, isso aqui ajuda a tangibilizar um pouco melhor. Vamos imaginar que o usuário faz uma solicitação para a LLM, mas essa solicitação não vai diretamente para a LLM que dará a resposta final.

Ela primeiro vai para uma LLM responsável por enriquecer a solicitação. Uma vez que essa solicitação foi enriquecida, ela será enviada para o modelo que realmente vai responder à pergunta. Depois disso, a resposta final é retornada novamente para o usuário. Esse é apenas um fluxo básico para facilitar o entendimento.

Agora, por que estou falando de dois LLMs aqui? Porque, normalmente, quem enriquece a pergunta é um modelo menor, mais barato e mais rápido, utilizado apenas para realizar esse tipo de processamento. Já o modelo que vai gerar a resposta final costuma ser um modelo mais robusto, que precisa ter acesso a mais dados ou a informações externas.

Então temos essas duas etapas principais que formam esse fluxo. Um ponto importante para você entender é que, dependendo da situação, existem casos em que é possível armazenar em cache perguntas que são frequentemente feitas pelos usuários. Muitas pessoas fazem isso para economizar custos, o que pode fazer bastante sentido dependendo do contexto.

Nesse caso, a reformulação pode ser baseada em palavras-chave. Quando você percebe que o usuário fez determinadas perguntas contendo algumas palavras-chave específicas, você pode buscar essas informações em um cache. Se essas palavras existirem, é possível concatenar algum contexto baseado nelas e gerar uma instrução mais completa para a IA.

Dessa forma, você elimina a necessidade de chamar um modelo para fazer o enriquecimento. Obviamente, o resultado não será tão refinado quanto quando utilizamos um LLM para enriquecer a pergunta, mas você economiza bastante em custo e tempo de processamento. Por isso, tudo depende do contexto em que você está trabalhando.

Sempre que eu vou criar qualquer coisa utilizando IA, a primeira coisa em que penso é quantas chamadas eu vou fazer ao modelo. Quanto mais chamadas forem feitas, mais caro o processo ficará e também mais lento ele será. No desenvolvimento tradicional de APIs, estamos acostumados com respostas em 10, 20, 50 ou 150 milissegundos.

No entanto, quando trabalhamos com IA, somente a etapa de enriquecimento já pode levar três, quatro ou cinco segundos. A geração da resposta final pode levar até 60 segundos. Ou seja, a arquitetura e a forma de trabalhar mudam completamente quando utilizamos IA.

Quanto menos camadas você tiver nesse processo, melhor, porque o sistema tende a ficar mais rápido e mais barato. Isso significa que você não precisa necessariamente utilizar um LLM para fazer enriquecimento em todos os casos. Também não precisa chamar um LLM sempre que tiver perguntas frequentes.

Você pode capturar determinados padrões de pergunta ou palavras-chave e buscar respostas em um cache já preparado, retornando esse resultado diretamente em vez de processar tudo novamente. Essa é uma das estratégias mais importantes para evitar uma abordagem ingênua de chamar o modelo a todo momento.

Toda vez que você chama um modelo, existe mais latência e mais custo. Por isso, é importante pensar cuidadosamente na arquitetura da solução. O enriquecimento é importante porque muitas vezes ele ajuda o usuário a fazer apenas uma pergunta para obter a resposta correta.

Se o usuário precisar perguntar novamente, isso significa mais tokens e mais custo. Muitas vezes vale mais a pena investir no enriquecimento da pergunta para garantir que a resposta seja adequada logo na primeira tentativa. E quando falo usuário, isso pode ser outra IA, uma integração entre sistemas ou qualquer outro tipo de consumidor da API.

O que precisamos, muitas vezes, são informações suficientes para responder corretamente. Quando não temos essas informações, precisamos repetir a busca ou executar um retry, e isso acaba gerando mais consumo de tokens e mais custo. Por isso, esse processo costuma ser subestimado.

Também é importante entender que não existe apenas esse tipo de interceptação. Existem interceptações de segurança, interceptações antes da execução de uma ferramenta, depois da execução de uma ferramenta, antes de chamar o modelo e depois de chamar o modelo. Ou seja, não é algo simples, mas tudo começa com esse tipo de abordagem.

## Transcrição

00:01

Bom, pessoal, então vamos entender agora aqui, rapidamente, o fluxo bem básico que acontece nesse processo. Então, somente caso você não tenha pegado a ideia, inclusive o que eu acabei de passar, eu acho que isso aqui consegue tangibilizar um pouquinho mais. Então, vamos imaginar que o user faz uma solicitação para a LLM, mas essa solicitação não cai para a LLM, que vai dar a resposta final.

00:29

Ela cai pra uma LLM que vai enriquecer a solicitação dele. Uma vez que essa solicitação foi enriquecida, essa solicitação vai ser enviada pro LLM, pro modelo que realmente vai responder a pergunta. E daí...

00:44

você vai passar a pergunta de novo para o usuário. Obviamente que isso é um fluxo básico. Agora, por que eu estou falando de dois LLMs aqui? Eu estou falando de dois porque, normalmente, quem enriquece a pergunta é um modelo, normalmente menor, mais barato, mais rápido, para conseguir fazer esse tipo de coisa.

01:04

E, normalmente, o modelo para fazer esse tipo de solicitação é um modelo que você realmente precisa ter mais dados e ser mais bem treinado, ou com informações de acesso externo e tudo mais. Então, a gente tem essas duas etapas principais que fazem com que a gente tenha esse fluxo. Agora, um ponto importante aqui para você entender,

01:27

é que, dependendo da situação, há casos que você pode cachear perguntas que são normalmente feitas pelo usuário. Tem muita gente que, para economizar, e faz todo sentido dependendo do contexto,

01:45

Essa reformulação pode ser baseada, por exemplo, em palavras-chave. Então, quando você percebe que o usuário fez determinadas perguntas com algumas palavras-chave que tem naquela instrução que ele manda, o que você pode fazer? Você pode buscar em algum cache. Quando essas palavras existem, você pode concatenar algo ali dentro

02:12

baseado naquelas palavras-chave e colocar alguns contextos para tentar gerar mais informação para a IA, e daí você elimina a chamada de um modelo, mas, obviamente, você não vai ter um enriquecimento tão mais bem feito do que passando essa informação para o LLM. Por outro lado, você economiza muito.

02:37

Então, realmente vai depender do contexto que você está. Então, toda vez que eu vou criar qualquer coisa com o IA, a primeira coisa que eu preciso pensar é quantas chamadas eu vou fazer no modelo. Porque quanto mais chamada eu fizer, mais caro vai ficar, mas também mais lento vai ficar.

02:56

A gente está muito acostumado, no dia a dia, a desenvolver APIs onde a gente tem requisições que se resolvem em 20 milissegundos, em 10 milissegundos, 50, 150 milissegundos, não interessa. E muitas vezes, somente para esse enriquecimento aqui, a gente já tem 3, 4, 5 segundos. Para gerar a resposta final, a gente tem 60 segundos. Então,

03:21

É uma arquitetura e é uma forma tão diferente de trabalhar quando você está utilizando IA nos dias de hoje que o jogo muda, né? Então, quanto menos camadas você tiver, é melhor porque vai ser mais rápido e mais barato ali no final das contas. Então, não necessariamente você precisa para enriquecimento sempre um LLM. Não necessariamente você precisa

03:45

sempre chamar LLM se você está fazendo perguntas e respostas frequentes. Você pode simplesmente capturar aquelas palavras ou aquele tipo de pergunta e buscar num cache pronto e trazer esse tipo de resultado ao invés de processar tudo novamente. Então, eu acho que isso é uma das coisas mais importantes que você pode fazer para não

04:11

ter uma atitude, vamos dizer assim, ingênua de querer fazer chamada para o modelo a todo momento. Toda vez que você chamar, é mais latência e mais custo. Então, pense sempre bem como trabalhar, e por isso que enriquecimento é importante, porque muitas vezes o enriquecimento vai fazer o usuário perguntar apenas uma vez.

04:33

Se o usuário tiver que perguntar mais outra vez, é mais dinheiro, é mais token. Então, eu prefiro, às vezes, investir no enriquecimento para garantir que eu tenha o trabalho feito. E quando eu falo usuário, pode ser outra IA perguntando, pode ser integrações de sistemas, não interessa. O que a gente precisa, muitas vezes, são informações, e se a gente não tem informação suficiente, a gente vai ter que refazer essa busca, a gente vai ter que fazer um retry.

04:59

E aí, nesse caso, a gente vai gastando, gastando, gastando. Então, esse processo acaba sendo sempre muito subestimado porque a gente tem que interceptar, tá? E você vai perceber que a gente não tem somente esses tipos de interceptação. A gente tem interceptações de segurança, a gente tem interceptações antes de executar uma ferramenta, depois de uma ferramenta, antes de chamar o modelo, depois de chamar o modelo.

05:26

Então, não é simples, mas começa por aqui, nesse tipo de aspecto. Beleza? Então, vamos nessa!

## Resumo IA

**Resumo**  
A aula apresenta um fluxo básico de processamento com IA em que a solicitação do usuário não é enviada diretamente ao modelo que gera a resposta final. Primeiro, ela passa por uma LLM de enriquecimento, geralmente menor, mais barata e mais rápida, cuja função é complementar ou reformular a pergunta para torná-la mais adequada ao modelo principal. Em seguida, a solicitação enriquecida é encaminhada para a LLM responsável por produzir a resposta final e, depois, o resultado retorna ao usuário. O instrutor destaca que esse desenho arquitetural é comum quando se precisa lidar com modelos mais robustos, que podem depender de mais dados ou de informações externas.

Também é abordada uma estratégia de otimização baseada em cache. Em cenários com perguntas frequentes ou padrões identificáveis por palavras-chave, é possível buscar respostas ou contextos previamente preparados em cache, concatenar informações relevantes e montar uma instrução mais completa sem precisar chamar uma LLM para enriquecimento. Isso reduz custo e tempo de processamento, embora com menor refinamento em relação ao uso de um modelo dedicado para enriquecer a solicitação. A aula reforça que, em projetos com IA, a principal preocupação arquitetural é o número de chamadas ao modelo, pois cada chamada aumenta latência, custo e consumo de tokens. O instrutor compara esse comportamento com APIs tradicionais, que costumam responder em milissegundos, enquanto fluxos com IA podem levar vários segundos no enriquecimento e até dezenas de segundos na geração final.

Por fim, a aula enfatiza que menos camadas na solução tendem a significar mais desempenho e menos custo, e que não é obrigatório usar LLMs em todos os casos de enriquecimento ou de perguntas recorrentes. A ideia é evitar uma abordagem ingênua de chamar o modelo a todo momento, preferindo interceptações inteligentes, uso de cache e tratamento de padrões quando fizer sentido. O enriquecimento é apresentado como uma prática que pode evitar retrabalho, novas perguntas, retries e consumo adicional de tokens, melhorando a chance de obter a resposta correta já na primeira tentativa. O instrutor também menciona que esse tipo de interceptação é apenas um dos vários pontos possíveis em uma arquitetura com IA, que pode incluir interceptações de segurança, antes e depois da execução de ferramentas e antes e depois de chamadas ao modelo.

**Pontos de atenção**  
- Cada chamada a um modelo aumenta custo e latência; isso precisa ser considerado na arquitetura.  
- Fluxos com IA têm tempos de resposta muito diferentes de APIs tradicionais; não assumir comportamento de milissegundos.  
- A etapa de enriquecimento pode ser cara em tempo e pode chegar a vários segundos.  
- A geração da resposta final pode ser ainda mais lenta, chegando a dezenas de segundos.  
- Usar uma LLM para enriquecer todas as perguntas pode ser desnecessário em cenários com perguntas recorrentes.  
- Cache por palavras-chave e padrões pode reduzir custo, mas tende a entregar enriquecimento menos refinado.  
- Quanto menos camadas no fluxo, melhor tendem a ser desempenho e custo.  
- Evitar uma estratégia ingênua de chamar o modelo sempre; pensar em interceptação e roteamento inteligente.  
- Investir em enriquecimento pode valer a pena se isso reduzir retrabalho, novas perguntas e retries.  
- Falta de informação suficiente leva a reprocessamento, mais consumo de tokens e maior custo.  
- O usuário pode ser uma pessoa, outra IA ou uma integração entre sistemas; a arquitetura deve considerar todos esses consumidores.  
- Existem vários tipos de interceptação além do enriquecimento: segurança, pré e pós-ferramenta, pré e pós-modelo.