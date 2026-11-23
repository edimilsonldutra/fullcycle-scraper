Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16404)

## Resumo da aula

RAG combina uma LLM com uma fonte externa de conhecimento para reduzir a dependência exclusiva do que ficou armazenado nos pesos do modelo. Uma LLM pura responde com base no que aprendeu no treinamento e, por isso, nasce defasada assim que o mundo muda. Atualizar o modelo por novo treinamento contínuo é caro e operacionalmente inviável em muitos cenários. A consequência prática é simples: sem recuperação externa, perguntas sobre fatos recentes ou dados internos da empresa tendem a gerar lacunas ou alucinações.

A fonte externa pode ser a web, mas o ganho mais valioso costuma aparecer quando ela é restrita a bases confiáveis e específicas. Documentos corporativos em S3, APIs internas, e-mails, chats, relatórios, FAQs de atendimento e bases acadêmicas são exemplos de repositórios que podem alimentar a recuperação. Isso permite responder com informação atualizada sem alterar os pesos da LLM. Também aumenta controle, porque a resposta passa a depender de fontes escolhidas pela aplicação, e não de um universo aberto e imprevisível.

A primeira camada do pipeline é a query, isto é, a pergunta textual enviada pelo usuário. Sozinha, essa entrada ainda não carrega o contexto factual necessário para responder perguntas recentes ou específicas de um domínio. Por isso, a query funciona como ponto de partida da recuperação, não como contexto suficiente para a geração final. Perguntas como “quais são as políticas de backup da empresa?” ou “o que diz a cláusula 7 do contrato?” exigem enriquecimento antes de chegar à LLM.

Retomando embeddings, a query deixa de ser tratada apenas como texto literal e passa a ser representada como vetor numérico. Esse vetor captura o significado da frase e viabiliza comparação semântica com a base indexada. O objetivo não é procurar coincidência exata de palavras, mas proximidade de sentido. Por isso, uma consulta como “acesso remoto seguro” pode recuperar conteúdo sobre “VPN corporativa” mesmo sem compartilhar os mesmos termos.

O retriever é o componente que usa o embedding da query para procurar, em uma base vetorial, os trechos mais semanticamente próximos. Para isso funcionar, os documentos já precisam ter sido previamente quebrados em partes e convertidos em embeddings. A recuperação compara vetores da consulta e dos trechos indexados e retorna os fragmentos mais relevantes. Esse passo substitui a lógica de palavra-chave por uma lógica de significado, o que melhora a recuperação em linguagem natural real.

Depois da recuperação, a aplicação monta um novo prompt contendo a pergunta original e os trechos encontrados. Esse é o ponto de integração entre busca e geração: a LLM não responde só com a memória do treinamento, mas com evidências recuperadas imediatamente antes da inferência. Se os trechos retornados incluem regras como uso obrigatório de VPN, registro por log e atualização de dispositivos móveis, essas informações entram no contexto fornecido ao modelo. A qualidade da resposta final depende diretamente da qualidade e da relevância desse contexto montado.

Com o prompt enriquecido, a LLM gera a resposta final de forma mais contextualizada. Ela continua sendo um modelo gerador, mas agora opera sobre evidências externas recuperadas para aquela pergunta específica. Isso reduz a chance de invenção e melhora aderência factual, especialmente quando a base consultada é recente e confiável. O valor do RAG não está em fazer a LLM “aprender em tempo real”, e sim em fazê-la responder com base em contexto recuperado em tempo real.

RAG é uma estratégia de arquitetura para equilibrar custo, atualização e previsibilidade sem recorrer a retreinamento constante. Retomando prompt engineering, o controle aumenta quando a recuperação é delimitada a fontes específicas, em vez de deixar a busca aberta na internet inteira. Restringir a consulta a sites, revistas, faculdades ou bases internas reduz ruído e melhora a confiabilidade operacional. Em sistemas reais, controlar de onde vem o contexto costuma ser tão importante quanto escolher qual LLM vai gerar a resposta.

## Transcrição

00:00

Bom, galera, vamos falar agora um pouquinho de RAG. Quando a gente tá falando do RAG, ou RAG, Retrieval Alignment Generation, a gente tá falando sobre uma outra estratégia quando a gente tá usando aqui as LLMs, os Transformers. Qual que é o grande ponto aqui? Quando a gente tá falando do RAG, conforme a gente já tinha falado anteriormente,

00:19

a gente está linkando uma LLM com uma fonte externa de informação, para conseguir trazer uma informação mais atualizada, mais realista, mais controlável para o nosso dia a dia. E por que isso é necessário? Pensa no seguinte, quando você prepara, treina a sua LLM, como a gente mostrou anteriormente, você está pegando um monte de Tolkien que você foi gerando, ou seja, um monte de palavras, frases e assim por diante, de livro, de artigo, de...

00:47

informação da internet, assim por diante, você jogou esse monte de token pra treinar a sua máquina. Beleza, treinou a LLM. Terminei de treinar a minha LLM, o que acontece? Eu tô com uma defasagem. Em D mais 1, em segundos depois, eu já não tenho as informações novas que estão chegando. Só tenho aquelas informações antigas que eu tinha acabado de fazer o treino da minha máquina.

01:08

Se eu falar o seguinte, cara, mas eu quero treinar e deixar ela sempre atualizada, extremamente caro, você não vai conseguir fazer isso possivelmente, vai ser muito caro pra fazer, você vai ter que parar toda hora pra fazer um novo treino de máquina, você nunca vai parar esse trabalho, ele vai ter que ser contínuo porque toda hora tá chegando informação nova, beleza?

01:24

Então, esse é um problema que a gente tem quando a gente tá falando de LLM pura, sem nada, sem nenhum tipo de estratégia. E daí você pega, por exemplo, o ChatGPT quando foi lançado, o ChatGPT no comecinho ali. O que ele fazia? Ele inventava. Se eu virasse pra ele e falasse assim, olha, eu preciso saber quanto foi o jogo do Palmeiras ontem. Nem sei se o Palmeiras jogou ontem, tá? Mas imagina que eu falasse assim, pô, preciso saber quanto foi o jogo do Palmeiras ontem. E o ChatGPT tava com a foto, sei lá, de um, dois anos pra trás, que foi quando ele foi treinado.

01:51

Ele não ia conseguir trazer pra mim, possivelmente ele ia inventar ou dar algum tipo de resposta meio macarrônica ali pra conseguir sair desse tipo de sinuca de bico. Então aqui a gente tem um problemão quando a gente tá falando das LLMs. Isso evoluiu, agora o Chat GPT, se você estiver usando uma versão paga, por exemplo, você vai ter lá um sistema de reggae já

02:11

implementado nele. Quando você faz uma pesquisa perguntando algo que é muito novo, alguma informação que é de ontem, por exemplo, ou de alguns minutos atrás, ele vai fazer o que? Ele vai abrir e vai buscar na internet, vai buscar na web, que é uma fonte de dados. Basicamente, essa é a estratégia. Ele não vai saber o que tem de novo após

02:30

o final do seu treinamento, mas ele consegue buscar dados em tempo real. Quando a gente consegue colocar ali uma aplicação de Reggie nele, ele vai conseguir buscar dados adicionais. Então o problema que a gente tem é, uma LLM pura ali, que a gente tinha, não acessava dados em tempo real.

02:48

não tem uma memória viva, não consegue ir aprendendo conforme as coisas vão acontecendo, pode alucinar quando ela é confrontada com um problema ou pergunta específica daquele momento, por exemplo, e dá uma informação meio mirabolante pra você.

03:04

Então, RAG vai ser uma técnica onde eu combino um modelo de geração, tipo um chat GPT da vida, com um mecanismo de busca de base de conhecimento externo. Então, você tem que juntar as duas coisas, não é só a sua geração de conteúdo de palavra a palavra com base em Token, mas você inclui um mecanismo de busca por similaridade e aí a gente vai falar um pouco disso. É um pouco diferente de uma busca comum, tá bom?

03:29

Vamos falar um pouco disso daqui a pouquinho. Então, ao invés de você lembrar, ao invés da LLM ter que lembrar tudo com base nos tokens, ela consulta, ela busca algumas informações novas antes de responder. E aí, quais são as fontes que você pode ter? Eu falei aqui da web, é um jeito, então você pode buscar na internet, pode buscar em bases, mas você pode nichar e colocar só de documentos da sua empresa, por exemplo. Pô, vou colocar lá, sei lá, no Bucket S3 um monte de documentos da minha empresa,

03:55

E lá eu vou jogar tudo quanto é informação para buscar quando eu tiver que pegar algum tipo de informação nova ou sei lá, você consegue gerar isso. Até em outras ferramentas internas da empresa, você consegue colocar algumas APIs e fazer essa busca lá também. Tem algumas estratégias que você pode colocar. Mas aqui o ponto é, você pode buscar dados de conhecimento exclusivos da sua empresa conforme eles vão sendo atualizados, você vai buscando as coisas mais novas. Então, por exemplo, imagina que você terminou de treinar a sua LLM mês passado e você está fazendo fechamento

04:25

contábil desse mês. Se você perguntar para ela sobre informações do fechamento desse mês, ela não vai saber. Então você consegue colocar ela linkada aos documentos da sua empresa para conseguir fazer atividades desse tipo, beleza? Outra coisa que você pode ter também é base de conhecimento específico de artigos científicos, de faculdades, etc. Você pode colocar busca em e-mail, em chat, em relatório. Você pode colocar, sei lá, plugado numa

04:51

num Teams da vida, numa outra ferramenta de mensageiria que você tem dentro da sua empresa. Pode colocar uma coisa que a galera acaba usando bastante é FAQ de atendimento. Então, por exemplo, seu time de atendimento já fez um baita de um trabalho ao longo dos anos de ir aprendendo e o atendimento, ele tá toda hora mudando, certo? Toda hora tem alguma reclamação nova. Então, entrou uma reclamação nova porque alguém fez um deploy errado em produção e tá gerando impacto, ele já vai estar atualizado porque ele vai conseguir buscar esse tipo de informação. Então, tem esses tipos de estratégia que podem te ajudar no dia a dia, beleza?

05:21

O que mais? Quando a gente está falando do REG, então ele é separado em 5 camadas, 5 camadas arquiteturais, tá? Eu vou simplificar elas para vocês entenderem, que é o ponto desta aula, para vocês entenderem um pouquinho mais das camadas arquiteturais, quando a gente está falando dessa estratégia. A primeira camada dela é a Query, que é a entrada do usuário.

05:42

A entrada do usuário é a pergunta que ele está fazendo, então a pergunta textual que a gente tem ali comum ali numa linha de prompt, então por exemplo, eu posso virar e falar quais são as políticas de backup da empresa, o que diz a cláusula 7 do contrato de prestação de serviços,

05:59

E assim por diante, são as perguntas que eu tô fazendo. Essa entrada, ela ainda não tem contexto suficiente, porque você tá dando pra ela só uma pergunta. Quando você tá falando de perguntas de coisas que aconteceram há pouco tempo, que não tem no treinamento dela, ela precisa ser enriquecida, então, com uma base de conhecimento. E daí que ela vai pros próximos pontos antes de ir pra geração do conteúdo SIM. Então, ela vai transformar isso numa query.

06:23

em um embedding. Lembra o que a gente falou? O que é um embedding? É uma representação vetorial daquela palavra ou daquele contexto que eu estou colocando. Então, você vai pegar os tokens, transformá-los em uma representação vetorial, que é um embedding, e com base nesse embedding, você vai buscar dentro da sua base de conhecimento que tem de proximidade nisso. Então, a query vai ser convertida em um vetor numérico. Ela vai deixar de ser uma palavra textual ou um token, tá?

06:51

E com isso, você vai conseguir fechar um vetorzinho pra ir buscar. Esse vetor vai representar o significado da frase, mais do que sua palavra. Então, pensa. Quando eu tenho uma frase, eu não vou buscar por proximidade daquelas palavras, palavra a palavra. Como eu faço, por exemplo, uma busca simplificada de alguma coisa, por similaridade de palavra. Conforme você vai digitando no campinho de busca, às vezes você vai buscando por similaridade de palavra, certo?

07:18

ou quando você busca na Netflix o filme, você está buscando por similaridade de palavra. Um embedding não, ele vai buscar por representação vetorial, então é por proximidade do significado da frase, mais do que da palavra. Então, por exemplo, imagina que você está buscando a frase acesso remoto seguro.

07:37

Ela pode ter um vetor de similaridade sobre VPN corporativa. Tá vendo que a VPN corporativa não tem a palavra acesso, não tem a palavra segura, não tem a palavra remoto, mas pela similaridade pode ser que seu embedding chegue nisso. Então, você está buscando similaridade e não a palavra em si.

07:56

Beleza? Então, isso é importante de você entender no modelo que a gente está construindo aqui de reg de utilização, onde a sua busca ela não é por palavra e sim por vetor e por similaridade usando o embedding. Beleza? Então, tudo isso que a gente aprendeu até agora, viu como é importante para a gente poder ter aqui a mesma linguagem? Senão, eu ia falar esse monte de palavras para você, você não ia entender bulhufas do que eu estava falando. Hoje, eu estou só com palavras extremamente atuais, né? Bulhufas, sinuca de bico, meu Deus, acordei um senhor.

08:26

vamos lá outra coisa importante que a gente tem então terceiro passo busca semântica na base vetorial retriever que a gente fala essa busca semântica vai ser o seguinte eu vou buscar então com base no vetor da query que eu gerei certo

08:41

na minha base vetorial de documentos. Então, meus documentos já foram transformados em vetor, eles já estão preparados para esse tipo de trabalho e daí eu vou lá e busco nesses documentos os dados que eu preciso para poder indexar essa busca. Então, pensa... Eu peguei um vetor aqui com base na pergunta, transformei ela num vetor. Os meus documentos eu já tinha processado, daí tinha várias frases lá, eu quebrei em vários pedaços.

09:05

E daí, essa quebra transformou eles em vetores. Tem tokens, vetores e embeddings. Então, tem um embedding de um lado e um do outro. Quando eu vou procurar a similaridade de cálculo aqui, matemática, eu vou começar a achar a similaridade e vou trazer quem é mais próximo daquilo. Então, basicamente é isso. Você vai conseguir, com o Retriever, buscar as partes que têm mais similaridade semântica à sua query, beleza? Ele vai buscar

09:31

todo o entendimento daquela pergunta que é a query e não mais só a palavra, tá bom? Então, isso é super importante, não é uma busca por palavra-chave gente, é uma busca por significado que é representado por um embedding que é nada mais do que seu token transformado em vetor junto com todas aquelas camadas que eu te falei de compreensão textual, tá bom? É muito complexo para a gente pensar, mas por trás é isso que está acontecendo. Então, vamos lá...

10:00

Qual que é o quarto passo? É a construção do prompt pra essa LLM. Agora sim, ele vai ter um prompt pra fazer. Depois que ele buscou tudo, ele tem os trechos recuperados, ele tem a sua pergunta inicial, tudo isso montado, isso adicionado ao prompt, aí agora ele vai trabalhar.

10:17

Agora ele vai pegar essa estrutura aqui, onde ele buscou na base de conhecimento as frases de exemplo ali, por exemplo, sei lá, política de acesso remoto, existe o uso de VPN, o acesso deve ser registrado por log, os dispositivos móveis precisam estar atualizados, sei lá, tá buscando frase a frase, de um monte de documento você gerou.

10:36

E ele achou esse multitário aqui. Na hora que ele vai fazer esse trabalho, ele junta isso na sua base de prompt. Então, você fez a pergunta, ele coloca isso na base de prompt do que ele tem de informação e daí sim ele começa a parte de geração, tá bom? Então, é com isso que ele consegue organizar.

10:53

tudo antes de responder. E daí ele vai pra quinta e última parte, a geração da resposta. Agora ele já tem todo o contexto, ele consegue gerar a resposta. Então ele vai pegar lá o prompt mais as evidências que ele gerou, pensa assim, e vai responder isso de forma mais contextualizada. Agora ele não vai ser mais um modelo que inventa, ele é um modelo que ele buscou as informações

11:15

organizou essas informações e com base nesses trechos reais, aí sim ele vai gerar a resposta que você precisa. Tá bom? Eu vou dar uma ideia de umas coisas que eu acabo fazendo quando eu tô promputando. Quando eu preciso de uma informação precisa e mais atual, eu nicho colo a base de conhecimento. Então, por exemplo, imagina que você precisa pegar

11:35

quais foram os últimos lançamentos dia da semana. Poxa, não vai ter na base de Token de processamento. E ele vai buscar na internet. Mas ele pode buscar em um monte de lugar maluco aí, certo? Então se eu jogar no chat de EPT, ele vai sair buscando. Blá, blá, blá. Uma porrada de lugar. O que que eu faço? Eu já nicho. Eu falo, olha, busca, mas busca nessa revista digital, nesta faculdade, neste site que eu preciso que você busque. Não busca aberto. Busca nestas fontes. Não use outras fontes que não estas.

12:05

porque daí eu já trago uma informação quente que eu sei que vai ser a melhor possível e que não vai ter nenhum tipo de falha ou alucinação ali no meio. Beleza? Então, estas são as formas de você trabalhar. Você pode trabalhar isso de várias maneiras, mas é um jeito de você organizar a entrega do seu resultado da LLM. Beleza?

## Resumo IA

**Abreviações**  
- **RAG** — *Retrieval Augmented Generation* (Geração Aumentada por Recuperação)  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **APIs** — *Application Programming Interfaces* (Interfaces de Programação de Aplicações)  
- **S3** — *Simple Storage Service*  
- **FAQ** — *Frequently Asked Questions* (Perguntas Frequentes)  
- **VPN** — *Virtual Private Network* (Rede Privada Virtual)  
- **Teams** — Microsoft Teams  

**Resumo**  
A aula apresentou RAG como uma estratégia de arquitetura que conecta uma LLM a uma fonte externa de conhecimento para reduzir a dependência exclusiva dos dados aprendidos no treinamento. O instrutor destacou que uma LLM pura fica defasada rapidamente, pois não acompanha informações novas após o treinamento, o que torna caro e pouco viável manter o modelo sempre atualizado por retreinamentos contínuos. Nesse cenário, sem recuperação externa, perguntas sobre fatos recentes ou dados internos tendem a gerar lacunas ou alucinações.

Foi explicado que a fonte externa de conhecimento pode ser a web, mas o maior valor do RAG aparece quando a busca é restrita a bases confiáveis e específicas, como documentos corporativos em S3, APIs internas, e-mails, chats, relatórios, FAQs de atendimento e bases acadêmicas. A ideia é permitir respostas mais atualizadas e controladas sem alterar os pesos da LLM, deixando a aplicação decidir de onde vem o contexto usado na geração.

O fluxo arquitetural foi detalhado em cinco etapas. Primeiro, a **query** é a pergunta do usuário, ainda sem contexto suficiente. Em seguida, essa query é convertida em **embedding**, ou seja, uma representação vetorial que captura o significado sem depender apenas das palavras exatas. Depois entra o **retriever**, que compara o embedding da query com os embeddings dos trechos já indexados em uma base vetorial e recupera os fragmentos semanticamente mais próximos. Na quarta etapa, a aplicação monta um prompt enriquecido com a pergunta original e os trechos recuperados. Por fim, a LLM usa esse contexto para gerar a resposta, agora mais factual, contextualizada e menos sujeita a invenções.

**Pontos de atenção**  
- LLM pura não tem memória viva: ela responde com base no treinamento e pode ficar rapidamente desatualizada.  
- Retreinamento contínuo para manter o modelo atualizado é caro e operacionalmente inviável em muitos cenários.  
- Sem recuperação externa, perguntas recentes ou específicas tendem a gerar respostas incorretas ou alucinações.  
- RAG não significa “aprender em tempo real”; significa recuperar contexto em tempo real para orientar a geração.  
- A qualidade da resposta final depende diretamente da qualidade, relevância e confiabilidade dos documentos recuperados.  
- A busca em RAG é semântica, não por palavra-chave: o foco é similaridade de significado via embeddings.  
- Os documentos precisam ser previamente quebrados em partes e indexados em uma base vetorial para que a recuperação funcione bem.  
- A query isolada não basta; ela precisa ser enriquecida com contexto antes de chegar à geração.  
- Controlar as fontes consultadas é essencial para reduzir ruído, melhorar previsibilidade e evitar respostas vindas de fontes abertas e imprevisíveis.  
- Restringir a busca a bases específicas da empresa, revistas, faculdades ou fontes confiáveis aumenta a chance de obter respostas corretas e operacionais.