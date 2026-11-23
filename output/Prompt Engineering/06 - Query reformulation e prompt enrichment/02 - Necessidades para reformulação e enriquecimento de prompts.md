Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16746)

## Resumo da aula

Como eu falei no vídeo anterior, a nossa ideia aqui é entender quais são as estratégias que precisamos para trabalhar de uma forma melhor quando temos algumas situações com os usuários. No vídeo anterior eu mencionei uma situação que é muito comum, mas existem outros aspectos que também podem influenciar a forma como vamos trabalhar.

Então, o primeiro ponto é exatamente o que eu mencionei. O usuário faz uma consulta muito vaga ou ambígua, onde a IA não consegue lidar bem com isso e acaba não trazendo os resultados que queremos, completos e adequados. Vamos imaginar que o usuário escreve apenas: Python e LangChain. O que isso vai representar no final das contas quando você coloca isso em um LLM?

Eu poderia fazer uma reformulação dessa pergunta como algo do tipo: crie um guia completo explicando como trabalhar com LangChain utilizando Python, do básico ao avançado. Se você perceber, eu peguei Python e LangChain e tentei inferir o que o usuário estava querendo saber. Esse é um exemplo mais extrapolado, porque normalmente conseguimos receber um pouco mais de contexto.

Ainda assim, se você consegue entender a intenção do usuário, já é possível melhorar bastante esse tipo de situação. Outra situação que também acontece é quando temos falta de contexto relevante. Às vezes o usuário quer perguntar algo, mas sabe quando surge aquele clássico depende? Por exemplo, o que é melhor, Go ou Python? A resposta normalmente será depende, porque precisamos entender o contexto por trás.

Muitas vezes acontece a mesma coisa. O usuário não adiciona no prompt as informações ou os contextos importantes para que o modelo consiga responder de forma mais assertiva. Um exemplo seria: como criar uma API em Python? Apesar de parecer uma pergunta clara, ainda é algo genérico, porque não sabemos exatamente o motivo ou o contexto da criação dessa API.

Então podemos melhorar essa pergunta. Por exemplo: explique como desenvolver um CRUD em Golang e disponibilizar endpoints REST utilizando o framework Gin. Se você perceber, eu melhorei a pergunta. Ao falar de criação de API, já inseri o conceito de CRUD para indicar que a API terá todos os endpoints necessários.

Também especifiquei que a API utilizará REST, porque APIs podem ser criadas utilizando outros protocolos. Além disso, mencionei um framework muito comum utilizado nesse contexto. Ou seja, adicionar contexto ajuda muito para que a IA consiga trabalhar melhor, e você pode realizar esse tipo de reformulação.

Outra coisa interessante é alinhar o formato da resposta. Muitas vezes precisamos que a resposta venha em um determinado formato ou padrão. Nesse caso, também podemos interceptar a pergunta do usuário e reformulá-la para garantir que a resposta venha estruturada da forma desejada.

Por exemplo: explique as regras de negócio desse sistema. Uma reformulação possível seria: faça um resumo das regras de negócio, módulo a módulo desse sistema, e retorne o resultado utilizando Markdown no seguinte formato: regras de negócio, depois a regra X, e em seguida o conteúdo do resumo.

Se você perceber, o que eu fiz foi reformular a pergunta e, ao mesmo tempo, definir o formato da resposta. Com o tempo você vai perceber que, apesar de gostarmos muito de Markdown, trabalhar com JSON ou outras notações estruturadas que usamos para integração entre sistemas acaba sendo essencial. Isso acontece porque nem todo sistema que não trabalha com IA consegue entender Markdown, mas JSON, por exemplo, consegue.

Então, nós temos esses tipos de situação. Outro ponto importante também é conseguir minimizar riscos de respostas incorretas. Como assim? Às vezes acabamos induzindo a IA a responder de forma errada. Por exemplo: quem criou a linguagem Python em 2012? Aqui temos, na realidade, uma pergunta que pode dar um nó na cabeça da IA e muitas vezes fazê-la alucinar.

O que acontece nesse caso é que a pergunta já traz uma premissa incorreta, pois Python não foi criado em 2012. Então, para evitar esse tipo de ambiguidade, podemos reformular a pergunta para algo como: quem foi o criador da linguagem Python e em que ano ela foi lançada? Dessa forma conseguimos deixar a pergunta muito mais específica.

Também temos situações relacionadas à realização de buscas semânticas. Esse é um dos aspectos mais importantes. Muitas vezes as perguntas que queremos fazer não estão treinadas diretamente na IA. Elas precisam estar em um determinado banco de dados e, para fazer essa consulta, quanto mais informação tivermos, mais documentos relacionados àquela pergunta conseguiremos recuperar.

Nesse caso podemos fazer com que a pergunta ou a instrução inicial do usuário traga mais detalhes. Podemos corrigir erros de ortografia, expandir sinônimos e enriquecer o texto. Isso acontece porque normalmente esses tipos de pesquisa vão consultar um banco de dados tentando encontrar relevância nas informações presentes na pergunta.

Então, quando reformulamos a pergunta incluindo mais sinônimos, às vezes adicionando termos em inglês, utilizando os mesmos termos em português e corrigindo detalhes de escrita, aumentamos a chance de recuperar documentos muito mais relevantes. Imagine, por exemplo, que alguém escreve: esse código está certo em Go, ainda com a palavra “certo” escrita com S.

Nesse caso podemos reformular para algo como: revise o seguinte código na linguagem Go, identifique possíveis bugs, problemas de performance, segurança ou violações, e forneça sugestões de melhoria com exemplos. Se você perceber, nessa reformulação eu já mencionei que Go é uma linguagem, falei de bugs, performance, segurança e pedi exemplos.

Tudo isso faz com que, ao buscar informações em um banco de dados, a quantidade e a riqueza de palavras presentes no prompt aumentem, trazendo normalmente documentos muito mais relevantes. O último ponto que quero abordar neste vídeo, para não deixá-lo muito longo, é a personalização.

Ou seja, quando existe conhecimento sobre contexto, perfil, público e outros detalhes que podem ajudar no resultado da pergunta. Por exemplo: explique como desenvolver aplicações com IA e Python. Podemos reformular para algo como: explique como desenvolver aplicações com Python para quem nunca teve contato com a linguagem e, a cada exemplo, mostre um comparativo com TypeScript.

Por que inserir essas informações? Porque podemos imaginar que, nesse momento, temos dados sobre o usuário. Sabemos que ele nunca trabalhou com Python e sabemos que sua especialidade é TypeScript. Tendo essas informações, conseguimos reformular o prompt para direcionar a IA a fazer um paralelo entre Python e TypeScript.

Provavelmente você utiliza o ChatGPT ou algum outro sistema de IA no dia a dia. Se perceber, cada vez mais o tom da IA ao conversar com você muda. Ela passa a saber mais sobre sua rotina, entende onde você mora e quais linguagens de programação você costuma utilizar como exemplo.

Naturalmente, os resultados que você começa a receber da IA passam a refletir essas informações. Quando você pergunta sobre programação, normalmente as respostas passam a usar a linguagem que você mais consulta. Quando pergunta sobre localização, as respostas podem trazer informações relacionadas à cidade onde você mora.

Ou seja, a IA consegue personalizar as informações que vai retornar. Ela faz isso utilizando dados que possui em sua memória de longo prazo e, com isso, consegue reformular as perguntas para que você receba respostas extremamente personalizadas, muitas vezes até utilizando o nome da pessoa ou outras informações contextuais.

Então perceba que não se trata apenas de dar contexto para perguntas mal formuladas, mas também de adicionar contexto para personalizar a experiência do usuário. Esses são alguns pontos importantes para entendermos quando devemos reformular e enriquecer prompts.

## Transcrição

00:01

Bom, pessoal, como eu falei no vídeo anterior, a nossa ideia aqui é entender quais são as estratégias que a gente precisa para que a gente consiga trabalhar de uma melhor forma quando a gente tem algumas situações com os usuários. No vídeo anterior, eu falei uma situação que é muito comum, mas nós temos outros aspectos aí que também podem influenciar a forma como a gente vai trabalhar.

00:25

Então, o primeiro ponto aqui foi meio que o que eu falei, tá? O usuário faz uma consulta muito vágua, muito vaga ou ambígua, onde a IA não consegue lidar muito com isso e acaba não trazendo resultados que a gente quer, completos e tudo mais. Então, vamos imaginar que o usuário pergunta, escreve apenas assim, Python e LangChain.

00:48

o que isso vai representar no final das contas quando você colocar isso no LLM? Então, eu poderia fazer uma reformulação dessa pergunta como algo. Crie um guia completo explicando como trabalhar com lang chain, com Python,

01:04

do básico ao avançado. Então, se você perceber aqui, eu peguei, né, Python e LangChain e tentei inferir o que o usuário estava querendo saber. Então, isso aqui é um exemplo, assim, bem extrapolado, tá? Porque, normalmente,

01:21

a gente consegue receber um pouquinho mais de contexto. Mas, ainda assim, se você consegue entender a intenção do usuário, você consegue, pelo menos, melhorar bastante esse tipo de situação. Uma outra situação também que a gente tem aqui é quando a gente tem pauta de contexto relevante. Então, às vezes, o usuário quer perguntar algo, mas sabe quando a gente vai falar aquele bendito depende? O que é melhor, Go ou Python?

01:51

a minha resposta vai ser depende, eu preciso entender o contexto por trás. Então, muitas vezes acontece a mesma coisa. Então, o usuário não adiciona no prompt as informações, os contextos importantes para que o modelo consiga responder de forma mais assertiva. Então, um exemplo aqui. Como criar uma API em Python?

02:09

Bom, apesar de ser bem claro a criação de APIs em Python, pode ser algo realmente interessante, mas, ao mesmo tempo, genérico do porquê eu vou criar esse tipo de API. Então, muitas vezes... Eu coloquei Go aqui, mas era em Python. Explique como desenvolver um CRUD com Python. Deixa eu já arrumar aqui na frente de todo mundo.

02:38

e disponibilizar Endpoints REST utilizando o framework Golgi. Então vou fazer o seguinte, eu vou voltar aqui pra Golang e eu vou colocar aqui em Golang. Beleza? Então se você perceber aqui, eu melhorei a pergunta.

02:53

Falei que para criar uma API eu já coloquei um CRUD no meio para que a API fique com todos os endpoints, vamos dizer assim. Falei que vai trabalhar ali com REST porque eu posso fazer APIs em outros protocolos e ainda também formei um framework muito comum utilizado. Então, dar contexto ajuda muito para que a IA consiga trabalhar e você pode sim conseguir fazer esse tipo de reformulação.

03:22

A outra coisa interessante é em relação a alinhar formato. Então, muitas vezes, se eu preciso ter a resposta em um determinado formato, em um determinado padrão, eu ainda assim também posso interceptar a pergunta do usuário e conseguir reformular para que eu consiga receber a informação em um formato. Então, por exemplo, explique as regras de negócio desse sistema.

03:47

Então, a minha reformulação pode ser, faça um resumo das regras de negócio, módulo a módulo desse sistema, e retorne o resultado utilizando o markdown no formato. Regras de negócio, depois a regra X, e depois o conteúdo do resumo. Então, se você perceber, o que eu acabei de fazer foi reformular a pergunta, mas, ao mesmo tempo, conseguir definir, inclusive, um formato para que muitas vezes eu precise. Você vai perceber que, ao longo do tempo, mesmo a gente gostando muito de markdown,

04:17

Trabalhar com JSON, essas notações que nós estamos acostumados para fazer integração entre sistemas, vai ser mais do que essencial, porque nem todo sistema que não trabalha com IA consegue entender Markdown, mas JSON, por exemplo, consegue. Então, nós temos esses tipos de situação.

04:37

Outro ponto importante também é a gente conseguir minimizar riscos de respostas incorretas. Como assim? Às vezes, a gente acaba induzindo a IA a falar de forma errada para a gente. Por exemplo, quem criou a linguagem Python em 2012? Aqui, a gente tem, na realidade, uma pergunta que vai dar um nó na cabeça da IA, que muitas vezes pode fazê-la alucinar. O que eu estou falando aqui é

05:07

que Python foi criado em 2012 e não foi criado em 2012. Então, o que eu posso fazer nesse caso é, para evitar esse tipo de ambiguidade, eu posso colocar quem foi o criador da linguagem Python e em que ano ela foi lançada. Então, eu consigo deixar isso muito mais específico. E também a gente tem situações em

05:30

realizações de buscas semânticas. O que isso significa? E eu acho que esse é um dos aspectos mais importantes. O que acontece, pessoal, é que muitas vezes as perguntas que a gente quer fazer não estão treinadas na IA.

05:47

Elas precisam estar em um determinado banco de dados e, para eu fazer essa consulta no banco de dados, quanto mais informação eu tiver, mais documentos, vamos imaginar assim, relacionados àquela pergunta, a gente vai ter ali com a gente. Então, nesse caso, a gente pode fazer com que a pergunta ou a instrução inicial do usuário

06:12

a gente possa trazer mais detalhes, a gente pode corrigir erro de ortografia, a gente pode expandir sinônimos. Por quê? Porque normalmente esses tipos de pesquisa vão cair num banco de dados e eles vão tentar encontrar relevância naquela informação que você colocou. Então, quando você reformula aquela pergunta colocando mais sinônimos, às vezes colocando termos em inglês,

06:36

usando os mesmos termos em português, corrigindo detalhes, vai fazer com que eu consiga trazer documentos muito mais relevantes. Então, imagina que eu escrevo ali, esse código está certo em Go, e o certo ainda com S.

06:52

Então, eu poderia reformular para revise o seguinte código na linguagem Go, identifique possíveis bugs, problemas de performance, segurança ou violação, forneça sugestões de melhorias como exemplos. Então, se você perceber, eu...

07:07

Com essa reformulação, eu já falei que Go é uma linguagem, eu falei de bug, eu falei de performance, falei de segurança, pedi exemplos. Então, tudo isso vai fazer com que, se eu estiver buscando num banco de dados, a chance de... a quantidade de riquezas de palavras que eu acabei introduzindo no prompt vai trazer documentos realmente, normalmente melhores. E o último ponto que eu queria trazer aqui para esse vídeo não ficar gigante é personalização.

07:36

Ou seja, quando há conhecimento do contexto, perfil, público e detalhes importantes que possam ajudar no resultado da pergunta. Então, por exemplo, assim... Explique como desenvolver aplicações com IA e Python. Então, eu posso reformular para o seguinte... Explique como desenvolver aplicações com Python para quem nunca teve contato com a linguagem.

08:03

a cada exemplo mostre um comparativo com TypeScript. Por que eu coloquei para quem nunca teve contato com linguagem e comparativo com TypeScript? Porque vamos imaginar que, nesse momento, eu tenho informações do usuário. Então, eu sei que ele nunca trabalhou com Python e eu sei que a especialidade dele é TypeScript. Então, eu tendo essas informações, eu consigo reformular esse prompt para fazer com que eu já

08:33

Direcione a IA ao ponto de ela conseguir fazer um depara de Python para TypeScript e tudo mais. Eu acredito que você deva usar o chat GPT ou algum outro tipo de sistema de IA no dia a dia. E se você perceber, cada dia a mais você vê que o tom que a IA fala com você é diferente, ela sabe mais coisas da sua vida, ela entende, às vezes, onde você mora, linguagem de programação que normalmente você

09:00

dá exemplos e, naturalmente, os resultados que você começa a receber da IA normalmente são resultados que vêm da linguagem de programação que você mais pergunta, quando você pergunta de localização, normalmente vai ser algo que tem a ver com a cidade onde você mora, ou seja,

09:19

a IA consegue personalizar a informação que vai trazer, e ela consegue fazer isso através de informações que ela tem na memória dela a longo prazo, e vai fazer com que ela reformule a nossa pergunta para que a gente receba uma resposta extremamente personalizada, muitas vezes com o nome da pessoa e coisas desse tipo. Então, isso aí é extremamente interessante. Então, perceba que não é apenas

09:45

dar contexto para perguntas mal feitas, mas também é dar contexto para você conseguir personalizar a experiência aí do usuário. Beleza? Então, esses aí são alguns pontos importantes para a gente entender quando que a gente tem que reformular e enriquecer prompts aí para a gente. Beleza? Então, vamos aí para o nosso próximo vídeo.

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **LLM** — *Large Language Model* (Grande Modelo de Linguagem)  
- **CRUD** — *Create, Read, Update, Delete* (Criar, Ler, Atualizar, Excluir)  
- **REST** — *Representational State Transfer* (Transferência de Estado Representacional)  
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)  
- **Markdown** — linguagem de marcação leve para formatação de texto  
- **JSON** — *JavaScript Object Notation* (Notação de Objetos JavaScript)  
- **Go / Golang** — linguagem de programação Go  

**Resumo**  
A aula abordou estratégias para reformular e enriquecer prompts de usuários, com o objetivo de melhorar a qualidade das respostas geradas por IA e aumentar a relevância de buscas em bases de conhecimento. O instrutor destacou que consultas muito vagas ou ambíguas, como “Python e LangChain”, tendem a produzir respostas incompletas, e que uma boa prática é inferir a intenção do usuário e transformar a pergunta em algo mais específico, como um guia completo do básico ao avançado.  
Também foi explicado que a falta de contexto relevante prejudica a assertividade das respostas. Para resolver isso, o prompt pode ser enriquecido com informações como o tipo de aplicação, padrões esperados e tecnologias envolvidas, por exemplo, ao pedir o desenvolvimento de um CRUD em Golang com endpoints REST usando o framework Gin. Além disso, a aula mostrou como alinhar o formato da resposta, definindo explicitamente se a saída deve vir em Markdown, JSON ou outro padrão estruturado, especialmente em cenários de integração entre sistemas.  
Outro ponto importante foi a redução de riscos de respostas incorretas ou induzidas por premissas falsas. O exemplo usado foi uma pergunta equivocada sobre o ano de criação do Python, que pode levar a alucinações do modelo; a solução é reformular a questão de forma objetiva e correta. Em seguida, a aula tratou de buscas semânticas, explicando que quanto mais detalhes, sinônimos, correções ortográficas e termos equivalentes forem adicionados ao prompt, maior a chance de recuperar documentos mais relevantes em um banco de dados. Por fim, o instrutor mostrou que a personalização também é um motivo para enriquecer prompts: sabendo o perfil do usuário, seu nível de conhecimento e suas tecnologias de referência, a IA pode adaptar a resposta, por exemplo, comparando Python com TypeScript para alguém que está migrando entre essas linguagens.  

**Pontos de atenção**  
- Consultas vagas ou ambíguas reduzem muito a qualidade da resposta da IA.  
- Reformular o prompt exige inferir corretamente a intenção do usuário, evitando extrapolações excessivas.  
- Falta de contexto relevante torna perguntas aparentemente claras ainda assim genéricas e pouco acionáveis.  
- Ao pedir desenvolvimento de APIs, é importante especificar detalhes como CRUD, protocolo, framework e objetivo da solução.  
- Definir o formato da saída é essencial quando o resultado precisa ser consumido por outro sistema.  
- Markdown nem sempre é adequado para integração; JSON costuma ser mais compatível em fluxos entre sistemas.  
- Premissas incorretas no prompt podem induzir a IA a alucinar ou responder de forma errada.  
- Em buscas semânticas, enriquecer o texto com sinônimos, correções ortográficas e variações de termos aumenta a relevância dos documentos recuperados.  
- Incluir termos técnicos adicionais no prompt pode melhorar a recuperação, mas deve manter relação com a necessidade real.  
- Personalização depende de contexto sobre perfil, experiência e preferências do usuário.  
- O uso de informações pessoais ou de comportamento exige cuidado para manter a experiência útil sem perder a adequação ao contexto.