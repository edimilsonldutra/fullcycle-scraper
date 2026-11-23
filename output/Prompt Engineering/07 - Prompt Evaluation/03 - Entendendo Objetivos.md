Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16858)

## Resumo da aula

Objetivo de avaliação é a definição explícita do que deve ser medido em um prompt. Sem isso, métricas e comparações ficam soltas, porque a equipe não sabe se está julgando exatidão, utilidade, formato, segurança ou custo. No mercado, esses objetivos aparecem com nomes relativamente padronizados em ferramentas, APIs e documentações. Essa checklist funciona como vocabulário operacional para transformar “quero melhorar o prompt” em “quero medir exatamente esta propriedade”.

Correctness mede se a saída bate com uma referência considerada correta para aquele caso. A lógica é comparar a resposta gerada com um fato, gabarito ou exemplo de referência e verificar se o conteúdo está certo. Esse objetivo é apropriado quando existe uma resposta verificável, como fatos, cálculos, classificações ou campos esperados. Se a pergunta admite validação objetiva, correctness é o critério que ancora a avaliação.

Relevance mede se a resposta realmente atende à pergunta ou à solicitação feita. Uma saída pode até parecer bem formada, mas ainda assim falhar por responder outra coisa, desviar do pedido ou trazer conteúdo fora do escopo. No exemplo “qual é a capital do Brasil?”, uma resposta sobre outro país não é relevante para a tarefa. Esse objetivo existe para separar aderência ao pedido de outras dimensões de qualidade.

Faithfulness verifica se a resposta permanece fiel ao contexto fornecido e não inventa informações além do que deveria afirmar. Groundedness adiciona a ideia de base explícita: a resposta precisa estar sustentada por uma fonte, evidência ou contexto rastreável. Uma resposta pode ser fiel ao contexto sem necessariamente ser exata em sentido absoluto, porque fidelidade e exatidão não são a mesma coisa. Essa distinção é central quando a saída depende de documentos, contexto recuperado ou links usados como base da resposta.

Quando um sistema apresenta um link, documento ou trecho como suporte da resposta, esse artefato funciona como grounding. O ponto não é apenas dizer algo plausível, mas mostrar de onde aquilo veio. Retomando a lógica de comparação entre critérios, a mesma resposta pode parecer boa em tom e estrutura, mas falhar se não estiver ancorada na fonte esperada. Em sistemas com RAG, busca ou documentação interna, grounding vira um objetivo de primeira classe.

Conciseness mede se a resposta é direta e evita excesso de texto desnecessário. Respostas longas não são automaticamente melhores; em muitos casos, elas aumentam custo, tempo de leitura e ruído sem melhorar a decisão do usuário. Esse objetivo é útil quando o sistema precisa ser objetivo, como em assistentes operacionais, extração estruturada ou respostas rápidas. Concisão não significa omitir informação essencial, e sim entregar o necessário sem enrolação.

Helpfulness mede se a resposta foi realmente útil e clara para quem vai usá-la. Uma saída pode ser correta, relevante e curta, mas ainda assim não ajudar o usuário a agir, entender ou decidir. Por isso, utilidade não se reduz a exatidão nem a concisão: ela depende de a resposta fazer sentido no contexto de uso. Esse objetivo captura valor prático percebido, não apenas conformidade técnica.

Bias verifica se a resposta está enviesada de forma inadequada, especialmente em temas nos quais a formulação pode induzir preferência injustificada. Harmfulness cobre saídas potencialmente prejudiciais ao usuário ou a terceiros. Toxicity foca em conteúdo ofensivo, agressivo, degradante ou inadequado, incluindo insultos e linguagem abusiva. Esses objetivos são indispensáveis quando segurança e comportamento aceitável fazem parte da qualidade esperada do sistema.

Format adherence mede se a saída respeita o formato exigido pela aplicação consumidora. Isso inclui gerar JSON válido, obedecer a um schema, preencher campos esperados ou produzir texto compatível com uma regex. Esse objetivo é especialmente importante quando a resposta será processada por software, e não apenas lida por humanos. Uma saída semanticamente boa ainda pode falhar operacionalmente se vier no formato errado.

Efficiency trata do custo operacional do prompt em execução. Aqui entram latência, consumo de tokens, throughput e capacidade de sustentar requisições por segundo sob carga. Retomando o que já foi estabelecido sobre avaliação contínua, qualidade de saída não é a única variável relevante: um prompt pode melhorar a resposta e piorar drasticamente o custo. Eficiência vira objetivo quando a aplicação precisa equilibrar qualidade com viabilidade técnica e econômica.

Pairwise é a comparação direta entre duas versões de saída ou entre dois prompts executados sob a mesma base de teste. A técnica só faz sentido quando existe um critério de vitória definido antes: mais correto, mais útil, mais conciso, mais fiel ou qualquer outro objetivo explícito. Retomando a comparação entre prompts já conhecida, pairwise não substitui o objetivo; ele operacionaliza a decisão entre alternativas. Dizer que “o prompt A ganhou do prompt B” só é informativo quando se sabe em qual dimensão ele ganhou.

A mesma resposta pode receber julgamentos diferentes dependendo do objetivo escolhido. Uma saída pode ser correta, mas pouco relevante para o pedido específico; pode ser fiel ao contexto, mas longa demais; pode ser concisa, mas pouco útil; pode seguir o formato, mas ainda ser tóxica. Esse é o ponto central da definição de objetivos: qualidade não é uma propriedade única do prompt. Cada objetivo recorta uma dimensão distinta do comportamento que será medida depois por métricas e evaluators.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior eu falei sobre a gente tem que entender os objetivos, a gente tem que entender como, a gente tem que entender quem e vamos nessa pra gente seguir essa linha de caminho aqui, tá? Então, o negócio é o seguinte, se você perceber aqui, tá? Eu tenho uma lista

00:19

E essa lista nos ajuda a entender quais são os nossos principais objetivos para que, na hora que eu quiser fazer uma verificação de um prompt, eu possa ter na minha cabeça o que eu quero avaliar no final das contas.

00:40

Então, esses termos que eu estou utilizando aí são termos extremamente comuns no mercado, nas ferramentas, nos tutoriais, nos manuais, nas APIs e tudo mais, que são termos que vão realmente descrever o que você precisa definir. Então, o nosso primeiro termo que a gente tem aqui é o correctness. Basicamente, ele vai verificar

01:10

E a saída que você está esperando, está batendo com uma referência. O que isso significa? Que eu faço uma chamada, e para essa chamada, vamos imaginar que eu tenho um fato ou uma referência em relação a essa chamada. Ou seja, eu tenho um exemplo ali comigo do que, para mim, o que é certo. Então, o que significa?

01:31

Quando eu rodo algo no meu prompt, no final das contas, eu acabo comparando o resultado que foi executado pela LLM baseado na referência que eu tenho. E aí, quando há essa comparação, eu consigo saber

01:49

o qual é o nível de confiança daquela informação está realmente apurada. Então, se você quer saber se o seu resultado está certo ou não,

02:04

baseado em uma referência, você vai utilizar esse correctness. Beleza? Agora, outro ponto importante é relevance, ou seja, a relevância. Se a saída que a gente teve realmente responde à pergunta feita ou à solicitação.

02:23

Ou seja, qual é a capital do Brasil? Se responder França é a capital do Brasil, provavelmente a relevância ali é mínima. Por quê? Porque a resposta está errada, tá? Outros dois termos que são bem comuns de aparecer, e aí depende muito de...

02:41

literatura, depende muito de ferramenta, a gente tem diversas ferramentas no mercado, mas, normalmente, elas são bem parecidas, na realidade, é faithfulness ou groundedness. Basicamente, é pra gente verificar se o resultado, né, que a gente tem da nossa saída, ela se mantém fiel ao contexto que a gente tá esperando, e ela não alucina, ela não traz um monte de besteira.

03:07

Então, no final das contas, a gente tá falando ali de confiança, tá? Ou seja, o quanto que de fidelidade, né, esse tipo de resposta ela tem de acordo com o que eu espero, tá? Então, quando a gente fala de fidelidade ou faithfulness,

03:23

A gente está querendo dizer isso, mas ao mesmo tempo, quando a gente está falando de grounding, quando a gente está trabalhando com AI, a gente está querendo dizer o seguinte, esse resultado que saiu, ele realmente é baseado em algo, né?

03:42

tem algo por trás, ou seja, toda vez que a gente falar em grounding, a gente começa a pensar, cara, qual é a referência que eu tenho para ter o grounding disso, né? Então, ou seja, eu tenho aquela resposta e o grounding daquela resposta é determinado fato. Então, é basicamente isso que acontece. Eu vou dar um exemplo bem claro. Imagina que você está usando o Chapt GPT e você fez uma pergunta e ele respondeu, e às vezes, do lado da resposta, ele coloca um link, né?

04:08

Aquele link, basicamente, é onde ele está fazendo o grounding, ou seja, ele está falando que aquela informação que ele está trazendo está vindo a partir daquele link. Então, isso é grounding. Então, basicamente, quando eu vou pensar nos meus objetivos, eu quero saber se as informações que estão vindo realmente se mantêm fiéis. Agora, se você perceber,

04:31

Ser fiel ou ter base é diferente de ser algo exato, tá? Mas o importante é saber se isso se mantém fiel ao contexto, tá? Outro item que a gente tem que é extremamente importante é concise-ness, ou seja, se a saída que a gente tem daquela resposta é objetiva e ela não tem enrolação. Às vezes a gente faz uma pergunta e a gente recebe dez páginas de resposta. Provavelmente isso não é... não é...

04:59

não é o objetivo, não tem essa consciousness no final das contas. Então, é o quanto mais direto é a minha resposta e que ela acaba me atendendo. Legal? Outro ponto importante é um outro termo que a gente chama de helpfulness, ou seja, se aquele resultado realmente é útil e claro para o usuário.

05:19

Uma coisa é ser algo objetivo, outra coisa é fazer com que o usuário tenha entendido aquilo e falado, olha, isso aqui realmente fez sentido. Então, eu acabo mostrando e verificando quanto aquilo realmente foi bom como resultado final. E não somente se ele teve grounding, se ele teve relevância, ou se ele estava correto, ou se ele foi objetivo. Eu quero saber, no final das contas, se isso realmente foi útil.

05:47

A gente também tem alguns outros pontos, que é a parte de Harmfulness, Bias ou Toxicity. Basicamente, o que eu estou querendo verificar é se as saídas que estão sendo geradas, elas não têm algo a ver com...

06:01

algo que pode ser prejudicial a alguém, algo que não esteja enviesado, ou seja, algo que tenha uma opinião totalmente pessoal em algo que necessariamente não existe uma resposta certa ou errada. Vamos dizer um exemplo muito simples. Qual é o melhor político?

06:19

O que é melhor em relação a isso? Ou seja, dependendo de como a IA responde, a gente pode dizer que ela tem um bias, ou seja, que ela está enviesada para determinado tipo de assunto. Então, nós também temos, a gente consegue fazer algumas verificações para ver se ela está realmente muito enviesada. E a gente tem a parte de toxicidade também, que no final das contas, a gente vê se não é um conteúdo tóxico, um conteúdo que não faz sentido para o usuário, muitas vezes,

06:48

conteúdo que fala mal de outras pessoas, um conteúdo que tem palavrão e coisas desse tipo, tá? Outra coisa interessante também é o format adherence. Basicamente, ele está dizendo o seguinte, se a saída que eu tenho agora

07:03

ela faz sentido no formato que eu queria que ele trouxesse ali pra mim. Ou seja, eu queria um JSON válido, eu queria a estrutura tal do JSON, eu queria seguir aquele esquema, eu quero que aquele regex ele tente passar. Então, nesse caso, também é um objetivo. Outro ponto aqui também é efficiency, basicamente eficiência, ou seja,

07:25

como é que eu tenho as minhas métricas para a parte de latência, de custo, em relação a token, throughput, quantas requisições por segundo eu consigo aguentar. Então, isso também eu posso querer medir a eficiência do meu prompt.

07:42

E outro ponto importante aqui também é a parte de evaluation, né, comparação de evaluação, ou normalmente isso é chamado de pairwise. Você vai escutar bastante esse termo, tá? Ou pairwise preference, ou a mesma avaliações baseadas em pairwise.

07:59

Basicamente, elas tendem a fazer comparações de duas versões e bater esses dados e falar quem ganhou e quem não ganhou. E daí, novamente, ganhou baseado em qual critério? Esse aí é um dos pontos importantes para a gente. Então, somente para a gente ter exemplos de objetivos, vamos imaginar que eu tenho um prompt e eu quero garantir que ele está seguindo determinado formato.

08:25

Ok, isso é um objetivo. Eu quero que a saída seja fiel ao contexto que está sendo passado, ou seja, eu não quero que a A alucine. Eu quero que a resposta seja curta e direta. Eu quero comparar se o prompt A gera respostas mais corretas que o prompt B. Então, se você perceber, são objetivos que eu posso ter e, baseado nesses objetivos, você vai começar a perceber

08:49

que você pode percorrer esses níveis de objetivos que eu posso querer trabalhar. E como esses objetivos conseguem ser muito baseados nesses tipos de categoria, que já é algo bem, vamos dizer, difundido no mercado, acaba sendo já meio que padrão,

09:10

vai ficar cada vez mais simples, de forma geral, você agora começar a pensar no que você quer melhorar ou no que você quer medir em relação ao seu prompt. Então, aqui tem uma checklist de possíveis pontos que você gostaria, que você tem o objetivo de fazer essa verificação. Maravilha? Pessoal, é o seguinte, eu sei que esse vídeo ficou grande, então vamos para o próximo porque...

09:34

a gente tem um objetivo, e a gente tem que verificar quais métricas que fazem sentido para eu conseguir cumprir esses meus objetivos. Beleza? Então, vamos nessa!

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **AI** — *Artificial Intelligence* (Inteligência Artificial)
- **JSON** — *JavaScript Object Notation*
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **RAG** — *Retrieval-Augmented Generation* (Geração Aumentada por Recuperação)
- **regex** — *regular expression* (expressão regular)

**Resumo**
A aula apresentou a ideia de **objetivos de avaliação** como a definição explícita do que deve ser medido em um prompt. O instrutor enfatizou que, sem essa definição, métricas e comparações ficam vagas, pois não se sabe se a avaliação está considerando exatidão, utilidade, formato, segurança, custo ou outra dimensão. Para organizar essa análise, foi mostrada uma checklist de termos amplamente usados em ferramentas, APIs, documentação e avaliações de modelos.

Primeiro, foi explicado **correctness**, que verifica se a resposta gerada bate com uma referência considerada correta. Em seguida, **relevance** foi tratado como o critério que mede se a saída realmente responde à pergunta ou solicitação feita. Depois, o instrutor diferenciou **faithfulness** e **groundedness**: o primeiro avalia se a resposta permanece fiel ao contexto fornecido, sem alucinar; o segundo destaca se a resposta está sustentada por uma fonte, evidência ou base rastreável. Nesse ponto, foi explicado que links, documentos ou trechos usados como suporte funcionam como grounding, especialmente em cenários com documentos internos ou RAG.

A aula também cobriu **conciseness**, que mede se a resposta é direta e sem excesso desnecessário, e **helpfulness**, que avalia se a resposta é realmente útil e clara para o usuário no contexto de uso. Em seguida, foram abordados critérios ligados à segurança e comportamento: **bias**, para identificar enviesamentos inadequados; **harmfulness**, para detectar saídas potencialmente prejudiciais; e **toxicity**, para identificar conteúdo ofensivo, agressivo ou abusivo. Também foi apresentado **format adherence**, que verifica se a saída respeita o formato exigido pela aplicação, como JSON válido, schema ou padrão por regex.

Por fim, o instrutor explicou **efficiency**, relacionada a latência, custo em tokens, throughput e capacidade de atender requisições por segundo, e **pairwise**, que consiste em comparar duas versões de saída ou de prompt para decidir qual performa melhor em um critério previamente definido. A mensagem central foi que a qualidade de um prompt não é única: a mesma resposta pode ser boa em um aspecto e ruim em outro, então a avaliação precisa começar pela definição clara do objetivo que se quer medir.

**Pontos de atenção**
- Definir claramente **o que será medido** antes de escolher métricas ou comparar prompts.
- Não confundir **correção** com **relevância**: uma resposta pode estar certa, mas não responder ao que foi pedido.
- Diferenciar **faithfulness** de **groundedness**: fidelidade ao contexto não é o mesmo que exatidão absoluta, e grounding exige base explícita.
- Em sistemas com documentos, busca ou RAG, verificar se a resposta está realmente **ancorada na fonte esperada**.
- **Conciseness** não significa omitir informação essencial; o objetivo é evitar enrolação sem perder o necessário.
- **Helpfulness** vai além de correção e formato: a resposta precisa ser útil de fato para o usuário.
- Avaliar **bias, harmfulness e toxicity** quando o sistema puder gerar conteúdo enviesado, ofensivo ou prejudicial.
- **Format adherence** é crítico quando a saída será consumida por software; uma resposta semanticamente boa pode falhar se vier no formato errado.
- Considerar **efficiency** junto com qualidade, pois um prompt melhor pode aumentar custo, latência ou consumo de tokens.
- Em **pairwise**, o resultado só faz sentido se o critério de vitória estiver definido antes.
- Uma mesma resposta pode receber julgamentos diferentes dependendo do objetivo escolhido; por isso, a avaliação deve ser dimensionada por **dimensão específica** e não por uma noção genérica de “boa resposta”.