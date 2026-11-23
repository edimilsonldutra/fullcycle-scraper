Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16753)

## Resumo da aula

No vídeo anterior, nós conseguimos ter uma ideia geral dos prompts — no final das contas, tudo é prompt. Agora eu vou mostrar para você o programa, como ele funciona. Não quero me aprofundar na linguagem Python; você terá acesso ao repositório e poderá analisar com calma depois. Basicamente, o que fiz aqui foi criar uma chain para cada prompt. Tenho o draft, que pega o prompt, chama o LLM e traz o resultado para mim. Fiz isso para cada um, e agora temos a parte interessante.

Tenho a minha função que vai fazer a iteração, onde recebo a pergunta, o número máximo de iterações (porque não quero que ele fique infinitamente) e o quanto quero que ele considere o trabalho completo. Mas essa informação não vamos usar de forma tão intensa; vamos acompanhar as iterações e quando completamos.

Basicamente, a ideia é a seguinte. Primeiro passo: vou pegar o draft e gerar um draft baseado na pergunta do usuário. Esse draft já contém aqueles missing markers. Vou imprimir para podermos visualizar.

Depois disso, vou contar esses missings para saber quantos existem. Iniciei a quantidade de interações e o progresso como zero, e agora entro em um loop. No loop, na primeira iteração, vou pegar os gaps, ou seja, todas as informações faltantes. Verifico o seguinte: se não houver nenhum gap, significa que o trabalho terminou. Se não houver nenhum gap e eu tiver menos de duas interações, vou pedir para ele expandir. É basicamente isso que estou fazendo para evitar que ele execute tudo de uma vez. Quero algo mais expandido. Expandir significa gerar um novo draft para ter mais gaps faltantes e continuar as iterações.

Quando chegamos na situação onde não há mais gaps, mas apenas uma iteração foi realizada, gero mais gaps para a próxima etapa. Aqui ele trouxe o número da iteração e quais são os gaps que preciso responder agora.

O que farei agora? Vou executar o prompt, pegando o draft e, baseado nas partes que estão com missing, transformar isso em uma pergunta, já com a resposta. Se você observar, peguei o draft com as perguntas e fiz um loop, limitando a no máximo 10. No prompt depois mudei para no máximo 5, para não exagerar. Ele vai enumerar apenas para visualização — isso é um debug. Na realidade, estou gerando as perguntas que preciso.

Por último, o que vou fazer? Vou pegar a pergunta inicial, o draft que foi gerado, as perguntas que criei para resolver os gaps e o número da iteração atual. O fill chain consolida tudo: ele pega as perguntas com as respostas, o draft, a pergunta original e a iteração, e completa os buracos no draft, gerando um novo draft.

Em seguida, verifico se ainda existem gaps. Se houver, mostro o resultado e quantos faltam para concluir. Isso é apenas um debugging para visualização na tela. Não seria necessário todo esse código — eu poderia apenas chamar a função, verificar a iteração e fazer a expansão. O arquivo poderia ser cinco vezes menor. Grande parte das informações serve para manter o tracking e visualizar linha a linha o que está acontecendo.

Aqui está a execução principal. Coloquei a pergunta "explain about LangChain and LangGraph?" — a mesma do exemplo anterior, sem expansão. Ele fará o processo e pedi para trazer estatísticas de tamanho e outras informações.

Essa é a ideia. É complexo? Quando você entende o conceito, não é complexo. O objetivo é "fill in the blanks", tapar os buracos. Grande parte do código está “verboso” para facilitar o tracking, mas não é algo extremamente complexo.

Vamos executar o programa. Vou rodar o Python neste arquivo, e ele vai demorar um pouco porque chamaremos o modelo várias vezes. Obviamente, estamos pagando o custo por isso. Vou deixar rodando enquanto isso.

Ele está processando, mas vou começar do zero com vocês. A pergunta é: "explain about LangChain and LangGraph". Ele trouxe um draft inicial, provavelmente a mesma resposta do exemplo sem expansão: LangChain é um framework, etc. Quando precisamos de detalhes, ele inseriu missing markers: versão específica e data de release, especificações técnicas e parâmetros, métricas de performance benchmark. Ele encontrou cinco gaps de informações faltantes.

Solicitei que ele gerasse perguntas para responder a esses missing markers. Para "Missing Specific Version", ele respondeu que LangChain está na versão 0.12 — valor desatualizado, pois o modelo foi treinado há algum tempo. O importante é entender o fluxo. Para "Missing Technical Specification", ele trouxe a resposta correspondente. Ele itera por todas as perguntas geradas a partir dos dados faltantes.

Ele então gerou uma versão refinada do draft. Observem que, por exemplo, LangChain, na versão 0.12, foi lançado em 15 de 2023 — ele substituiu o missing marker pela resposta. Limitei a quantidade de caracteres para o texto não ficar muito extenso.

Nesta iteração, dos três gaps, ele conseguiu resolver apenas um, provavelmente o da versão. Restaram dois gaps. Ele pega as perguntas restantes, gera respostas e cruza com o draft novamente, verificando se consegue substituir as partes missing. Ele trouxe as informações e gerou outra versão refinada, conseguindo fechar os outros gaps.

Após três iterações, chegamos à versão final do documento. Agora, o documento tem muito mais informações e detalhes do que a versão sem expansão. Se eu pedir 10 missing points, o texto crescerá ainda mais, expandindo cada vez mais as informações.

Baseado na expansão, ele aumentou em quase 100% o tamanho original da resposta. Isso demonstra como, utilizando técnicas de prompt — pois no final, tudo é prompt — podemos encadear resultados: um prompt gera um resultado, que alimenta o próximo, e assim sucessivamente, até chegar à versão final de forma iterativa. Prompt é o que comanda, é o poder quando interagimos com IA, permitindo resultados fantásticos com esses detalhes.

No próximo vídeo, falaremos sobre como enriquecer as perguntas do usuário, diferente deste exemplo que focou em obter uma boa resposta.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente conseguiu ter uma ideia mais ou menos dos prompts, que no final das contas tudo é prompt. E agora eu vou mostrar para você o programa, como é que ele funciona. Eu não quero ir a fundo em relação à linguagem, ao Python, você vai ter acesso a esse repositório, você pode ver com calma depois. Mas, basicamente, o que eu fiz aqui foi criar um chain para cada prompt. Então, eu tenho o draft, que pega o prompt, que chama o llm,

00:30

e que traz o resultado pra mim. Então, eu fiz isso pra cada um, e agora que a gente tem a parte que é interessante.

00:37

É o seguinte, eu tenho a minha função que vai fazer a iteração, onde eu recebo a pergunta, o número máximo de iterações, porque eu não quero que ele fique infinitamente, e o quanto que eu quero que ele considere o trabalho completo. Mas essa informação aqui até que a gente não vai usar de uma forma tão forte, mas a gente vai ver as iterações e quando a gente conseguiu completar.

01:06

Então, basicamente, a ideia vai ser o seguinte. Vamos lá, passo 1. Eu vou pegar o draft e vou gerar um draft baseado na pergunta do usuário. Então, consegui agora com o draft. Esse draft aqui já tem aqueles missing markers ali pra gente. Então, eu vou até imprimir pra gente conseguir ver isso.

01:25

Depois disso, o que eu vou fazer? Eu vou, nesse caso aqui, contar esses missings para eu saber, inclusive, quantos eu tenho.

01:38

Beleza? No momento, eu iniciei a quantidade de interações e o progresso como zero, e agora eu entro num loop aqui. E o loop vai ser o seguinte, primeira interação, eu vou pegar os gaps que eu tenho, ou seja, eu vou pegar todas as informações que eu tenho faltando, e eu vou verificar o seguinte, se eu não tiver nenhum gap, significa que eu já terminei meu trabalho.

02:04

E se eu não tiver nenhum gap e eu tiver menos de duas interações, eu vou pedir para ele expandir. É basicamente isso que eu estou fazendo para ele não rodar numa vez só. Ou seja, eu quero ainda uma coisa mais expandida. E expandir o que significa? Gerar um novo draft

02:21

para ter mais gaps faltantes para a gente conseguir continuar as iterações. Basicamente, é isso que é feito aqui com a gente. Então, quando a gente cai nessa situação onde a gente não tem nenhum gap mais, mas foi só com uma iteração, eu gero mais gaps para eu conseguir para a próxima etapa aqui para mim. Então, aqui ele trouxe para mim o número da iteração e quais são os gaps que eu tenho

02:50

para responder agora. E agora, o que eu vou fazer? Basicamente, eu vou chegar e vou executar o prompt, onde eu vou pegar o draft, e baseado naquelas partes que estão com missing, eu vou...

03:05

tornar isso uma pergunta, já com a resposta dela aqui. Então, se você olhar aqui, o que eu fiz? Eu peguei o draft, onde eu tenho aqui minhas perguntas, e eu simplesmente fiz um loop aqui, pegando no máximo 10, mas no prompt depois eu mudei para ele trazer no máximo 5, para a gente não ficar muito.

03:23

e ele vai enumerar somente para eu conseguir ver isso aqui mostrado para a gente. Isso aqui é muito mais para a nossa visualização, é um debug essa parada aqui para a gente. Mas, na realidade, o que eu estou fazendo é gerando perguntas que eu estou precisando. E, por último, o que eu vou fazer? Eu vou pegar a pergunta inicial, o draft que ele queria, as perguntas que eu gerei,

03:49

para resolver aqueles meus gaps e a iteração que eu estou. Então, o que vai acontecer? Esse field chain, o que ele faz? Ele meio que consolida tudo.

04:03

No final das contas, ele vai pegar as perguntas com as respostas, ele vai pegar o draft, ele vai pegar a pergunta original, ele vai pegar a iteração que eu tenho, e ele vai completar os buracos ali com o nosso draft, pra gente ter esse nosso draft. Beleza? E daí, basicamente, o que eu faço é, eu verifico se...

04:25

Tem gaps ainda? Se tiver, eu mostro o resultado e quantos faltam pra gente concluir. Basicamente, é um debugging mesmo, galera. Isso aqui é realmente um debugging pra gente ver na tela aparecendo. Eu não precisaria nada disso. Eu precisaria somente chamar esse cara, somente chamar esse cara...

04:44

chamar e fazer a verificação da iteração e fazer expansão, ou seja, esse arquivo poderia ser, sei lá, cinco vezes menor no tamanho que está. Grande parte dessas informações que você está vendo aqui é muito mais para a gente manter o tracking e conseguir ver, linha a linha, o que está acontecendo ali para a gente. E aqui tem a execução principal aqui para a gente. Então, basicamente, eu coloquei explain,

05:12

About the length chain and length graph? Foi exatamente a mesma pergunta que eu fiz no exemplo passado, sem nenhuma expansão. E aí, ele vai fazer a mágica dele aqui, e eu pedi para trazer novamente estatísticas do tamanho e outras informações aqui para a gente.

05:29

Então, essa que é a ideia. É complexo? Assim, quando você entende a ideia, não é complexo, tá? Porque o que você quer é fill in the blanks, né? É simplesmente tapar os buracos, e grande parte desse código está bem verboso, é muito mais pra dar, por exemplo, pra você, e também muito mais pra gente conseguir trackear.

05:49

mas, de forma geral, não é algo extremamente complexo aí nesse nosso caso. Beleza? Então, eu vou botar esse cara aqui para rodar. E vamos lá. Então, eu vou dar aqui o Python, vou colocar aqui nesse camarada, e ele vai demorar um pouquinho para rodar. Na realidade, é porque a gente vai chamar o modelo diversas vezes. E, obviamente, a gente está pagando o preço de fazer isso. Então, olha só que interessante. Eu vou deixar ele rodando enquanto isso.

06:19

Ele está rodando, mas eu vou começar aqui do zero com você. Então, a pergunta é, explain about the lang chain and lang graph. E aqui ele trouxe um draft inicial. Esse draft inicial, provavelmente, é meio que a mesma resposta que aquele exemplo, sem nenhuma expansão, trouxe para a gente. Então, o lang chain é um framework, etc, etc, e tudo mais. Aí, o que acontece no meio da história?

06:43

Porém, quando a gente precisa trazer esses detalhes, daí ele colocou aqui, um, missing, a versão específica e a data de release, a data que foi lançado ali, o language em line graph. Daí eu coloquei, sendo que essa é a última versão que foi lançada e tudo mais. Então, perceba que isso aqui,

07:11

basicamente é o complemento, é o inicial desse restante dessa afirmação. Mesma coisa, technical specification e parâmetros, ou seja, os detalhes que estão por baixo da arquitetura. Outra parte missing, métricas de performance benchmark, outra parte missing. Então, ele trouxe aqui para mim vários pontos que estão missing, que estão ali no meu texto e que poderiam estar faltando.

07:38

Então, no final das contas aqui, ele encontrou cinco gaps de coisas que estão faltando. E aí, eu pedi pra ele gerar perguntas que respondam pra mim esses missing markers aqui pra gente. Então, a gente tem aqui...

07:55

Para a questão de Missing Specific Version e etc., aqui ele falou que a lang chain está na versão 0.12. E não está, porque o modelo está desatualizado, inclusive. O modelo foi treinado já faz um tempo. Mas o importante é a gente entender que ele trouxe as perguntas que a gente queria. Missing Technical Specification. Aí está aqui a resposta da Technical Specification, por exemplo.

08:22

E a gente vai iterando aqui por todas as perguntas que foram geradas baseados naqueles dados que estavam faltando. E agora ele gerou para mim uma versão refinada daquele meu draft. E agora se você olhar já o meu draft, você vai ver que, por exemplo, o LangChain, que está na sua versão 0.12, foi lançado em 15 de 2023. Por quê?

08:46

porque ele pegou aquele pedaço que estava faltando e agora substituiu com a resposta correta. E aqui eu limitei uma quantidade de caracteres para o texto não ficar muito gigante. Mas o que acontece? Ele conseguiu resolver nessa iteração, dos três gaps, ele conseguiu resolver um só. Ele conseguiu substituir somente, provavelmente, o da versão. Então, ele falou que tem mais dois caras que faltam ele preencher os buracos. E aí, o que ele faz? Ele pega as perguntas,

09:15

que a gente tinha, gerou a resposta dessas perguntas, e quando ele vai cruzar com o draft, ele vai ver, será que com a informação que eu tenho aqui, eu consigo substituir aquela parte em que está missing? E aí, o que vai acontecer? Ele trouxe aqui as informações, e ele trouxe agora aqui a versão refinada novamente, e agora ele falou que ele conseguiu

09:39

fechar os outros gaps. Então, agora, eu não tenho mais nenhuma informação daquelas perguntas que não estejam respondidas. E, agora, depois de ele ter refinado três iterações, aqui está a versão final do meu documento. E, agora, se você, de forma geral, vê,

09:59

Ele é um documento que tem muito mais informação e detalhes do que, necessariamente, o documento sem nenhuma expansão. Ou eu mesmo consigo, como eu posso dizer,

10:12

induzia o modelo a trazer cada vez mais perguntas. Se eu falo, olha, eu quero agora 10 missing points, eu quero que isso expanda, esse texto vai poder crescer, ele vai poder ir cada vez mais longe em relação a essas informações. Então, a gente consegue ver, e aqui eu trouxe... Ou seja, ele, baseado na expansão que ele fez, ele conseguiu aumentar em quase 100% do tamanho original da pergunta,

10:41

que ele traria ali. Então, isso aqui é uma ideia pra você ver como é que, utilizando técnicas de prompt, porque no final das contas, galera, tudo isso é prompt. É pegar um prompt, sair no resultado do outro, sair no resultado do outro, sair no resultado do outro, até a gente gerando a versão final de forma iterativa, tá? Então, novamente, galera, prompt é o que manda, é o poder quando a gente tá falando com IA nesse caso, então,

11:07

a gente consegue fazer coisas extremamente fantásticas com esses tipos de detalhes. Fechou? No próximo vídeo, a gente vai falar sobre como enriquecer as perguntas do usuário e não como ter uma boa resposta. Nesse nosso caso aqui, foi como ter uma boa resposta. Maravilha? Então, vamos nessa!

## Resumo IA

**Abreviações**
- **LLM**: *Large Language Model* (Modelo de Linguagem de Grande Porte).
- **LLM/llm**: referência ao modelo de linguagem chamado pelo programa para gerar respostas.
- **Python**: linguagem de programação usada na implementação do fluxo.

**Resumo**
A aula mostrou, na prática, como um fluxo iterativo baseado em prompts pode ser usado para enriquecer uma resposta até preencher lacunas de informação. O instrutor explicou que criou uma chain para cada etapa: uma chain inicial gera um draft a partir da pergunta do usuário, outra identifica os trechos faltantes marcados como *missing*, outra transforma esses gaps em perguntas respondíveis e, por fim, uma *fill chain* consolida pergunta original, draft, perguntas geradas, respostas e número da iteração para completar os buracos no texto.

O processo começa com a geração de um draft inicial sobre o tema solicitado. Em seguida, o sistema conta os *missings* e entra em um loop controlado por um número máximo de iterações, para evitar execução infinita. Se não houver gaps e ainda houver poucas iterações, o sistema força uma expansão para produzir mais lacunas e continuar o refinamento. Depois, cada lacuna é convertida em perguntas, as respostas são obtidas e o draft é reconstruído com essas informações. A cada rodada, o programa verifica se ainda restam gaps e, se necessário, repete o ciclo até chegar a uma versão final mais completa.

Como exemplo, foi usada a pergunta sobre LangChain e LangGraph. O primeiro draft trouxe uma resposta básica, mas com pontos faltantes como versão específica, data de release, especificações técnicas e métricas de benchmark. O sistema então gerou perguntas para cada lacuna, obteve respostas, substituiu os trechos missing e refinou o documento em múltiplas iterações. Ao final de três iterações, o texto ficou significativamente mais detalhado, com aumento de quase 100% em relação ao original. O instrutor enfatizou que grande parte do código é verbose apenas para facilitar o tracking e o debug, pois conceitualmente a ideia central é simples: usar prompts encadeados para “preencher os buracos” de forma iterativa.

**Pontos de atenção**
- Controlar o número máximo de iterações para evitar loops infinitos.
- Usar a expansão com critério, para não tentar resolver tudo em uma única passagem.
- Entender que os campos *missing* são apenas marcadores de lacunas a serem preenchidas.
- Separar bem as responsabilidades de cada chain: draft, detecção de gaps, geração de perguntas e preenchimento final.
- Considerar que a geração de respostas via LLM tem custo computacional e financeiro, pois o modelo é chamado várias vezes.
- Manter logs e *debugging* ajuda no rastreamento do fluxo, mas pode deixar o código excessivamente verboso.
- Não confiar cegamente na exatidão factual do modelo, especialmente em dados específicos como versões e datas, pois ele pode estar desatualizado.
- Limitar o tamanho das saídas quando necessário para evitar textos excessivamente longos.
- Validar após cada iteração se ainda existem gaps antes de prosseguir para a próxima etapa.
- A estratégia principal é iterativa: o resultado de um prompt alimenta o próximo, então a qualidade do fluxo depende da qualidade intermediária em cada etapa.