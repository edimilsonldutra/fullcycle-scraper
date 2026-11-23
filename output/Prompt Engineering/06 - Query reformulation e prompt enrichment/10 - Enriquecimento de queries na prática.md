Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16754)

## Resumo da aula

No vídeo anterior, falamos sobre como enriquecer respostas utilizando um loop iterativo para preencher lacunas. Agora quero abordar algo extremamente importante, que é o foco deste capítulo: como enriquecer perguntas. Ao enriquecer perguntas, conseguimos obter respostas melhores.

Não se apegue ao código Python em si. Procurei organizar o exemplo de forma estruturada, pois dependendo da abordagem pode ficar complicado. Por isso, quero que você entenda bem os detalhes. Separei em classes para tornar mais compreensível — normalmente eu faria funções chamando uma à outra, mas aqui optei por mais organização.

A ideia central é como enriquecer uma pergunta relacionada à correção de uma pull request. Defini algumas informações obrigatórias para reformular a pergunta. Se esses dados não estiverem disponíveis, o sistema deve perguntar ao usuário até obtê-los, para então gerar a pergunta final enriquecida. Com essas informações, podemos consultar um banco de dados, chamar a LLM ou executar alguma ferramenta.

Neste exemplo, defini como informações obrigatórias: ID da pull request, repositório, branch, preocupações (concerns), guia de estilo e requisitos de teste. Conforme desenvolvemos aplicações com LLM, será cada vez mais comum criar classes com Pydantic ou Data Classes para estruturar as respostas em modelos de dados, em vez de trabalhar apenas com linguagem natural.

Criei um modelo base que indica se a pergunta é complexa, se requer subqueries (perguntas menores), um campo de clarifications (perguntas ainda necessárias) e entidades capturadas a partir do interesse do usuário. Por exemplo, se o usuário menciona "minha PR é a PR ID 10", a entidade capturada seria "PR ID 10".

O motor de funcionamento para enriquecer a pergunta funciona assim: chamo o modelo com um prompt que define a tarefa. O prompt instrui o assistente a identificar informações faltantes para gerar perguntas de clarificação. Ele deve continuar perguntando até obter todas as seis informações obrigatórias. A resposta deve ser em JSON, indicando se há subqueries, as clarificações necessárias e as entidades identificadas.

O JSON permite estruturar a resposta e popular o modelo de dados. Em seguida, utilizo outra chain para reescrever tudo em linguagem natural, de forma organizada, concisa e clara, combinando a pergunta original com o contexto obtido.

Por fim, temos o método principal que executa o enriquecimento e gera a resposta final em linguagem natural, com todas as informações coletadas, resultando em uma pergunta bem formulada.

Na prática, haverá uma interação com o usuário: o sistema pergunta, o usuário responde, e o loop continua até que todas as clarificações sejam obtidas. Só então a pergunta final enriquecida é gerada.

Você terá acesso ao código fonte para analisar passo a passo. Meu objetivo não é o código em si, mas sim o conceito de como enriquecer perguntas. Sei que pode parecer confuso, especialmente com o formato JSON, mas a execução tornará tudo mais claro.

Vou executar o programa. Vou rodar "python query_enrichment.py". Ele perguntará: "Qual é a sua pergunta?" Vou responder em português: "revise a minha pull request". Então, essa é a minha pergunta inicial.

Agora vamos ver o que acontece. Preste atenção. Este arquivo está extenso principalmente devido ao debug. Observem: aqui temos o round 1, onde preciso enriquecer o output. A pergunta é complexa? Sim, porque se não fosse, ele não expandiria as perguntas. Aqui estão as subperguntas geradas: identificar o ID da PR, determinar o repositório, descobrir o branch, clarificar concerns, verificar o style guide e especificar os requirements.

Esse é o JSON atual com as perguntas que preciso responder. Para cada uma, preciso obter as informações: PR ID, nome do repositório, branch, etc. Quando todas essas clarificações forem resolvidas, terei a pergunta final enriquecida. As entidades ainda estão vazias.

Ele pede clarificações: "Qual é o ID da sua Pull Request?" Vou responder "1". Em seguida: "Qual é o ID do seu repositório?" Vou me negar a responder por enquanto para ver o comportamento.

Ele informa que no primeiro round conseguiu o PR ID. Agora, a pergunta sobre o ID da pull request não aparece mais, e a entidade PR ID agora é 1. Ele então pergunta: "Qual é o nome do seu repositório?" Vou responder "iagem". Depois: "Qual é o branch?" Vou responder "teste". Ainda deixo algumas respostas pendentes.

Agora ele tem as informações: nome do repositório, branch name e PR ID. Restam três pontos a clarificar. Observem como as perguntas estão evoluindo: "Revise a pull request com ID 1 no repositório iagem, no branch test." As subqueries já estão mudando porque já tenho dados suficientes para construir uma pergunta melhor.

Continuo: para concerns, vou responder "golang style to be used" — minha preocupação é não seguir o estilo Go. Para test requirements, vou responder "atingir 80% de cobertura".

Agora ele tem todas as entidades e não há mais nada a esclarecer. Vejam como ficou a pergunta final: "Você poderia revisar minha pull request com ID 1 no repositório iagem, no branch test, garantindo que siga o style guide Go e atinja os requirements de 80% de cobertura de testes."

Perceberam? Saímos de uma pergunta extremamente aberta — "revise minha pull request" — para uma pergunta muito mais completa, simplesmente enriquecendo a estrutura com o que considero importante.

Muitas vezes, quando um usuário faz uma pergunta vaga em um chat, podemos cair nesse loop interativo. Após responder todos os requisitos, enviamos a pergunta enriquecida para a LLM, que executará a operação.

Existem outras formas de enriquecimento. Se tivéssemos contexto anterior — como qual PR o usuário estava mexendo, qual branch, qual projeto — muitas informações já viriam preenchidas, e a query, apesar de vaga, já estaria melhor do que apenas a pergunta original.

O importante é entender que existem diversas técnicas para garantir perguntas cada vez mais completas para a LLM. Este é apenas um exemplo, com múltiplas chamadas e iterações, mas espero que tenha ficado claro como criar técnicas interessantes baseadas nos dados disponíveis e no que considero obrigatório ou não.

Aqui, fui respondendo conforme o sistema perguntava. Mas, na prática, quando um usuário faz uma pergunta vaga, podemos ter prompts que reformulem a pergunta com base no perfil do usuário, no último código que ele mexeu, na função que ele exerce, nos guias da empresa, etc. A pergunta reformulada pode ser gerada a partir de dados do banco, chamadas de ferramenta ou perguntas diretas ao usuário, como fizemos.

É muito melhor enviar uma pergunta completa como essa do que mandar para o sistema "corrija uma PR" sem saber sequer o ID da PR. Quando você internaliza essa ideia, passa a obter respostas cada vez mais completas.

O interessante é que, se eu fizer uma pergunta como "revise minha PR que está no repositório iagem, no branch X, e tome cuidado para não esquecer de seguir o estilo oficial de programação em Go", ele já captura algumas informações: repositório iagem, branch X. O PR ID e os concerns ele não pegou, mas já temos uma base. Com ajustes no prompt, provavelmente conseguiria capturar mais entidades e gerar uma pergunta final ainda mais rica.

Isso mostra que não precisamos começar do zero. Quando o sistema roda, podemos capturar entidades, entender o contexto e trazer apenas as informações que realmente importam, reformulando a pergunta de forma gramaticalmente correta e bem estruturada com os dados obtidos do usuário.

Este é um exemplo simples de como utilizar essas técnicas. Não tem como falar de prompt sem abordar enriquecimento de query e melhoria de respostas.

## Transcrição

00:01

Bom, pessoal, no nosso vídeo anterior, a gente falou sobre como eu consigo enriquecer respostas de forma geral, utilizando um loop iterativo para a gente ir preenchendo os buracos.

00:14

Agora, eu quero trazer aqui pra você uma das coisas que são muito e muito realmente importantes, que é muito do que se trata, inclusive, esse nosso capítulo, que é como que eu consigo enriquecer perguntas. Uma vez que eu consigo enriquecer perguntas, eu consigo ter respostas melhores, tá?

00:33

Novamente, não se apegue ao Python como fez, eu tentei aqui trabalhar de uma forma organizada porque pode ser um pouquinho complicado dependendo de como que você aborda cada situação, tá? Por isso que eu queria que você entendesse bem nos detalhes, eu acabei separando em classes, normalmente com exemplos eu só faço uma função chamando uma atrás da outra, mas aqui eu queria deixar um pouco mais organizado para fazer mais sentido para você, tá?

01:01

Então, basicamente, a nossa ideia aqui é como eu consigo, por exemplo, enriquecer uma pergunta que tivesse a ver com alguém corrigir uma pull request minha. Então, essa que é a ideia inicial.

01:17

Então, o que acontece? Basicamente, aqui eu coloquei variáveis somente para a gente trabalhar. E agora aqui que é o ponto importante. Eu criei algumas informações que eu vou considerar obrigatórias para que eu consiga reformular a sua pergunta. E nem que isso faça com que eu tenha que te perguntar de volta

01:43

a informação para eu conseguir gerar a pergunta final melhor. Então, a ideia é, se eu não tenho os dados que eu preciso, eu vou ficar perguntando para você para eu conseguir gerar a resposta final, e uma vez que eu gerar a resposta final, eu tenho as informações para eu fazer a consulta no banco, chamar a LLM, não interessa, ou chamar uma tool, etc. Então, nesse caso, eu falei que é importante eu saber o ID da minha pull request,

02:11

o repositório, o branch, as minhas preocupações, os concerns, o guia de estilo e test requirements. Então, essas são informações que, para mim, eu estou determinando que são importantes. E, galera, uma coisa que eu quero que você entenda sempre é que conforme a gente for avançando e desenvolvendo aplicações

02:31

principalmente trabalhando com LLM, cada vez mais vai ser comum você criar classes, você trabalhar com, por exemplo, com o Pydent, que por exemplo, dá vida, mesmo com o Data Class, para você conseguir pegar a resposta do LLM e trazer ela no formato de modelo de dados, e não utilizar somente essas informações em linguagem natural. Então, o que acontece aqui? Então, basicamente, aqui eu tenho um base model que eu falo se a pergunta é complexa,

02:58

Se eu preciso fazer subqueries, ou seja, fazer perguntas menores para conseguir receber a resposta que eu preciso, eu tenho um campo chamado de clarifications, ou seja, quais perguntas que eu preciso ter ainda,

03:15

para que eu consiga gerar minha pergunta enriquecida, tá? E aqui, entidades, ou seja, são as entidades que eu acabo capturando baseado no interesse do usuário. Por exemplo, se o cara fala assim, olha, a minha PR é a minha PR ID 10, beleza, então aqui como entidade eu vou ter PR 2.10, tipo isso, tá? E aqui, o que eu vou ter aqui no final das contas, tá?

03:43

Aqui que a gente começa a ter, basicamente, um motor de funcionamento de como que eu enriqueço a minha pergunta. Então, basicamente, eu vou chamar o modelo, vou falar que eu preciso de um chain, a gente já vai olhar que a gente está trabalhando com lang chain aqui. Mas, basicamente, o que a gente está fazendo é o seguinte, eu estou pegando,

04:07

e estou juntando aqui pra mim a pergunta do cara, certo? E com as informações que eu obrigatoriamente preciso saber, tá? Então, olha só como é que fica o meu prompt aqui no meu caso.

04:23

Você é um assistente especializado em refinar perguntas de software development. A sua tarefa é identificar informações que estão faltando para gerar perguntas que gerem clarificação, vamos dizer assim. Você pode

04:46

perguntar dos seis requirements de informações que podem estar faltando, tá? Não pare de fazer essas perguntas antes de eu ter todas essas minhas respostas respondidas, vamos dizer assim. E aqui tem as minhas perguntas, que é qual o ID do meu AMPR, o meu repositório, o nome do meu branch, e as outras informações da pull request. E daí, eu estou pedindo aqui para ele responder da seguinte forma, no formato de JSON.

05:15

É complexo? É um booleando. Se tem subqueries, eu trago aqui a subquerie. Clarificações, eu trago quais são as informações que eu preciso deixar mais claras e quais são as minhas entidades. Então, aqui, eu tenho algumas regras para deixar as coisas mais claras. Você precisa incluir as questões, tá?

05:38

que não estão necessariamente explicitamente mencionadas na pergunta. Então, basicamente, eu quero, na parte de clarificação,

05:50

mostrar exatamente o que eu ainda preciso saber, porque eu vou ter que voltar a perguntar para o usuário. É basicamente isso. Então, se você tem o ID de uma PR, o repositório, o branch, você ainda tem que perguntar o restante das outras perguntas. Não adianta eu ter apenas algumas respostas. Eu tenho que ter as seis perguntas obrigatórias para que eu tenha a minha pergunta final. Então,

06:18

Aqui é dado o exemplo, e no final das contas, como ele responde em JSON, o que eu estou fazendo aqui é para ele pegar o output no formato JSON e enriquecer aquele meu modelo.

06:29

Beleza? Então, uma vez que eu tenho esse cara aqui, eu faço, pego meu prompt, mando pra LLM e o meu parser, aqui no final das contas, vai ter o meu objeto ali populado. Aqui a gente tem, novamente, também uma outra chamada de uma chain, que no final das contas vai ser, reescreva isso

06:52

em linguagem natural, de uma forma bem organizada, concisa e clara. E aqui a gente vai pegar a pergunta original, pegar todo aquele contexto, e aí a gente vai ter a resposta.

07:06

E aqui, por fim, a gente tem o nosso método, que é o método, vamos dizer, principal, no final das contas, que ele traz o que a gente precisa enriquecer. E, por último, acredito que é por último, mas é por último mesmo, o que a gente tem é a gente gerar

07:26

a resposta final, no conteúdo original, com aquelas informações que a gente tem em linguagem natural para parecer uma pergunta bonitinha com o que a gente tem. Então, como é que vai funcionar aqui no final das contas? Aqui é somente

07:41

a sessão, ou seja, a forma de como eu vou interagir com o usuário. Então, ele vai mostrar a pergunta, depois ele vai pegar a resposta, e vai ficar naquele loop onde eu vou trabalhar eu mesmo digitando aqui no teclado. Então, é basicamente isso. Eu vou mostrar aqui para vocês.

07:58

Basicamente, tudo isso agora aqui que você está vendo é um loop que ele fica rechamando aquela função até ele ter clarificado tudo que estava faltando para ele gerar a minha pergunta final. Então, é basicamente isso que ele acaba trabalhando.

08:15

Você vai ter, obviamente, todo o tempo do mundo para olhar passo a passo esse código fonte. O meu ponto aqui não é no código, mas sim para você entender a ideia de como que eu consigo enriquecer. Eu sei que pode estar parecendo um pouco confuso, principalmente naquele formato de JSON, mas eu acho que agora, na hora que eu rodar, as coisas vão fazer mais sentido para você.

08:38

Então, deixa eu chamar, eu vou colocar aqui, Python, Query Enrichment aqui, e agora vai perguntar o seguinte, qual que é a sua pergunta? E eu vou colocar assim, revise a minha PR, a minha Pull Request, estou até escrevendo em português. Então, essa é a minha pergunta inicial. Agora, o que vai acontecer aqui para mim? Olha só que interessante, galera. Preste bem atenção.

09:07

Por isso que esse documento está gigante, esse arquivo, mas muito mais por conta de debug. Olha só, aqui ele pegou que é o nosso round 1, então eu preciso enriquecer o meu output. Então, é uma pergunta complexa? Sim, porque se não for complexa, ele acaba não expandindo mais as perguntas, tá? Mas, basicamente, aqui, quais são as sub-perguntas que ele tem?

09:32

Então, eu preciso identificar o ID da PR, determinar o repositório, descobrir qual é o branch, clarificar concerns, verificar o style guide, especificar os requirements para mim. Então, aqui, basicamente, é como está nesse momento esse meu JSON.

09:57

Então, baseado nessas perguntas que eu tenho, o que eu preciso ter claro para responder essas perguntas? Ou seja, aqui são as minhas perguntas e aqui é o que eu preciso saber para responder essas perguntas. Então, o que eu preciso saber? Qual é o meu PRID? Qual é o nome do meu repositório? Qual é o branch? Qual é isso?

10:18

Quando eu resolver todas essas clarificações, se é que existe ou não existe essa palavra, eu acho, significa que eu vou resolver todas as sub-perguntas. E, se eu resolver todas as sub-perguntas, eu vou ter a minha pergunta final enriquecida, tá? E as entidades estão em branco. Então, aqui, se você olhar, por favor, me dê algumas clarificações. Qual é a UID da sua Pull Request? Eu vou colocar 1, tá?

10:43

E agora ele pergunta, qual é a ID do seu repositório? Eu vou me negar a responder por enquanto. Vamos ver o que ele vai fazer. Então, ele falou o seguinte, olha, a informação que eu consegui pegar no primeiro round foi o PRID. Então, se você olhar agora, eu não tenho mais a pergunta que é falada sobre qual é a ID da minha pull request, tá? E eu não tenho mais a minha clarificação da minha pull request aqui. Mas eu tenho a minha entidade, que é a minha PRID, agora é 1.

11:13

E agora ele vai perguntar mais coisas. Qual é o nome do seu repositório? Eu vou chamar Iagem, por exemplo. Vou dar um Enter. Qual é o branch? Eu vou chamar o branch de teste. Vou dar um Enter agora aqui de novo, não vou responder. E ele falou, olha, agora eu consegui essas informações.

11:28

Agora que eu tenho essas informações, olhe as minhas entidades, o nome do repositório, o branch name, o PRID, e agora eu só tenho mais três pontos que eu preciso clarificar. E se você olhar aqui, olhe como estão ficando as minhas perguntas. Revise a pull request com o id1, um dagen repository, ou um detest branch. Você consegue perceber que as minhas subqueries já estão mudando?

11:54

porque eu já tenho dados suficientes para ir criando uma pergunta melhor. Então, vamos lá agora. Concerns eu vou chamar... GoLangStyle. Vou colocar aqui.

12:11

Bom, qual que era o meu concern, né? O golang style era um concern. Vou colocar golang style to be used. Minha preocupação é não seguir o gol style e agora eu estou falando que ele tem que seguir isso, tá? Bom, tudo bem. Quais são os test requirements? Eu vou colocar atingir 80% de cobertura.

12:39

Vou dar um enter agora aqui pra mim, agora ele falou, olha as informações que eu tenho nesse round. Agora, se você perceber, olha só que legal, galera. Ele conseguiu pegar todas as entidades, ele não tinha mais nada pra esclarecer, e agora, olha só como é que ficou a minha pergunta final.

12:58

Nesse meu caso. Você poderia revisar minha pull request com a ID 1 no repositório e a gen, no branch test, garantindo que ele vá seguir o style, o Go style guide, e também tiver e ter os requirements de 80% de test coverage.

13:17

Galera, eu não sei se vocês perceberam, mas eu consegui sair de uma pergunta extremamente aberta, ou seja, faça essa minha pull request, ao ponto de eu ter uma pergunta extremamente, vamos dizer ali, mais completa,

13:35

Simplesmente porque eu fui enriquecendo a minha estrutura daquilo que eu achava importante. Obviamente, tá, pessoal? Muitas vezes, quando o usuário mandar uma pergunta num chat ou qualquer coisa desse tipo, você pode cair nesse loop interativo, para quando ele terminar de responder todos os requisitos, você manda essa pergunta para a LLM, e a LLM vai fazer o quê? Vai executar essa operação.

14:03

Agora, também existem outras formas de você poder enriquecer. Por exemplo, ele faz essa pergunta muito vaga, mas se você tivesse no contexto anterior qual APR que o cara estava mexendo ou qual era o branch, qual era o projeto ou outras informações, muitas dessas informações já poderiam estar vindo completas e a minha query, apesar de vaga, já estaria um pouco melhor do que naturalmente

14:31

ela estaria somente com a pergunta do usuário final. Então, o que eu quero trazer aqui, e que você entenda principalmente, é que existem diversas técnicas, diversas maneiras de você conseguir garantir que você vai fazer uma pergunta para a LLM,

14:51

de uma forma cada vez mais completa. Obviamente, galera, da forma como eu trouxe aqui é um exemplo. Eu estou repetindo diversas chamadas e tudo mais para ter a minha pergunta mais completa. Mas eu espero que você tenha entendido o objetivo desse exemplo.

15:10

Ver como que eu consigo criar técnicas interessantes baseadas nos dados que eu tenho, no que eu considero obrigatório, do que eu não considero obrigatório, para que eu consiga reformular essa pergunta. E, obviamente, aqui eu fiquei respondendo conforme o sistema foi perguntando para mim.

15:28

Mas, muitas vezes, o que acontece quando o usuário faz uma pergunta muito vaga, você pode ter prompts falando, olha, baseado nessa pergunta, e baseado no perfil do cara que a gente tem no banco, baseado no último código que ele mexeu, baseado na função que ele tem, baseado no guia que a gente está acostumado, reformule essa pergunta dessa forma. E aí, a gente tem a pergunta reformulada.

15:52

Então, obviamente, se o usuário faz uma pergunta vaga, obviamente que para reformular a pergunta você tem que ter dados. Esses dados podem vir do seu banco de dados, esses dados podem vir de uma chamada de ferramenta, esses dados podem vir de perguntas que você refez para o usuário, que nem eu fiz aqui, para você ter a pergunta final antes de mandar para a DLM.

16:14

muito melhor mandar uma pergunta muito mais completa como essa do que mandar para o sistema corrigir uma PR que ele nem sabe qual é a UID da PR e como que o agente iria corrigir. Entendeu? Então, é essa a ideia. Quando você colocar isso na sua mente, você vai perceber que você vai ter cada vez respostas cada vez mais completas. O mais interessante de tudo isso é que, por exemplo, se eu coloco aqui,

16:42

revise minha PR, que está no repositório Iagem, no branch X, e tome cuidado para não esquecer de seguir o estilo oficial de programar na linguagem Go.

17:11

Quando eu faço esses tipos de pergunta, ele já consegue pegar algumas coisas, ainda mais porque eu peguei a... Como se diz, eu escrevi ainda em português, tá? Mas olha só, ele já entendeu que o repositório é a gen, ele entendeu que o branch é x, né? O prid e o concern etc. ele acabou não pegando. Com certeza, aqui ó,

17:38

Aqui é, tenha certeza que você pegou o style do Go, o branch X. Então, se você perguntar, você já vê que ele já trouxe a informação já um pouco mais enriquecida. Ele não pegou a minha PR1 e etc., mas com certeza, se eu ajusto o meu prompt, eu consigo perguntar de uma forma mais específica,

17:57

Provavelmente, muitas dessas perguntas aqui, essas entidades, já vão vir mais prontas para ele gerar a minha pergunta final. Então, isso aí é uma coisa interessante, porque você não precisa começar do zero. Quando isso roda no seu sistema,

18:13

Você vai conseguir pegar as entidades, você vai entender aquele contexto e vai trazer ou perguntar somente informações que você acha interessante, ou você reformula a pergunta de uma forma mais bonitinha, gramaticalmente correta, escrito certinho, com as informações que você conseguiu pegar do usuário final. Então, está aqui mais um exemplo bem simples de como você pode utilizar.

18:38

Fechou, galera? Então, era isso que eu queria trazer. Esse capítulo é importante. Não tem como a gente falar de prompt sem falar de enriquecimento de query e também de melhoramento das respostas e tudo mais. Fechou? Então, é isso aí, meu povo. Até mais!

## Resumo IA

**Abreviações**
- **LLM**: *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **PR / Pull Request**: Solicitação de *pull request* (proposta de alteração em um repositório de código)
- **PR ID / PRID**: Identificador da *Pull Request*
- **JSON**: *JavaScript Object Notation* (formato de dados textual estruturado)
- **Pydantic**: biblioteca Python para validação e modelagem de dados
- **Data Class**: classe de dados (estrutura para representar dados de forma tipada e organizada)
- **Branch**: ramificação do código-fonte em um repositório
- **Go / Golang**: linguagem de programação Go

**Resumo**
A aula apresenta o conceito de enriquecimento de perguntas, complementando o conteúdo anterior sobre enriquecimento de respostas. O instrutor explica que, ao receber uma pergunta vaga — como “revise minha pull request” — o sistema pode conduzir um loop interativo para coletar as informações consideradas obrigatórias antes de formar a consulta final. No exemplo, os dados essenciais definidos foram: ID da pull request, repositório, branch, concerns, style guide e test requirements.

Para estruturar esse processo, o instrutor usa classes e um modelo de dados, destacando que em aplicações com LLMs é comum representar saídas com Pydantic ou Data Classes em vez de depender apenas de texto livre. O fluxo começa com um prompt que faz o assistente identificar o que está faltando, gerar perguntas de clarificação e responder em JSON com campos como: se a pergunta é complexa, se há subqueries, quais clarifications ainda são necessárias e quais entidades já foram capturadas.

Em seguida, uma segunda chain reescreve o conteúdo em linguagem natural, de forma organizada, clara e concisa, combinando a pergunta original com o contexto obtido. O método principal coordena esse processo e mantém o loop de interação com o usuário: o sistema pergunta, o usuário responde, o modelo atualiza o estado e continua até completar todas as informações obrigatórias. Só então é gerada a pergunta final enriquecida, pronta para ser enviada à LLM, a uma consulta ao banco de dados ou a uma tool.

O instrutor demonstra a execução com o exemplo “revise a minha pull request”, mostrando como o sistema identifica a falta de dados, solicita o PR ID, repositório, branch, concerns e requisitos de teste, e vai refinando a pergunta a cada rodada. Ao final, a consulta se transforma em uma solicitação muito mais precisa, como revisar uma PR específica em um repositório e branch determinados, respeitando o style guide Go e uma meta de cobertura de testes. A aula também reforça que esse enriquecimento pode vir não só de perguntas diretas ao usuário, mas também de contexto prévio, banco de dados, perfil do usuário e informações de uso anterior.

**Pontos de atenção**
- Não tratar o exemplo como foco em Python; o objetivo é entender a técnica de enriquecimento de perguntas.
- Definir claramente quais informações são obrigatórias antes de formular a pergunta final.
- Usar um formato estruturado, como JSON, para facilitar a extração e a atualização do estado da conversa.
- Capturar entidades desde o início para reaproveitar o que o usuário já informou e evitar perguntas repetidas.
- Manter o loop de clarificação até que todas as informações essenciais tenham sido obtidas.
- Reescrever a pergunta final em linguagem natural para deixá-la clara, completa e bem formulada.
- Aproveitar contexto externo quando disponível, como dados de banco, perfil do usuário, último código alterado ou projeto atual, em vez de depender apenas da entrada inicial.
- Ajustar o prompt para melhorar a captura de entidades e reduzir lacunas na coleta de informações.
- Entender que perguntas vagas como “corrija uma PR” são insuficientes para uma boa execução por uma LLM.
- Considerar o enriquecimento de perguntas como parte central de sistemas com prompts, especialmente quando o objetivo é obter respostas melhores e mais precisas.