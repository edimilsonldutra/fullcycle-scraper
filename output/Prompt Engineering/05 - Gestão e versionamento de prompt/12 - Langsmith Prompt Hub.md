Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16726)

## Resumo da aula

O Prompt Hub do LangSmith funciona como uma vitrine e um repositório remoto de prompts, com uma experiência próxima à de um GitHub voltado a artefatos de prompt. Ele centraliza publicação, descoberta, documentação, histórico e download, o que permite que um prompt exista fora do repositório da aplicação sem deixar de ser consumível em runtime. Retomando a gestão remota já estabelecida, a novidade aqui é a interface de hub: o prompt passa a viver em um catálogo navegável, com identidade própria e possibilidade de reutilização por outras pessoas e projetos.

Chat prompt e string prompt representam dois formatos diferentes de artefato dentro do hub. O chat prompt organiza a instrução em mensagens, normalmente incluindo papéis como system e user, o que o torna adequado para fluxos conversacionais e para prompts que dependem explicitamente dessa estrutura. Já o string prompt é o conteúdo textual direto do prompt, tratado como uma única instrução; é o formato mais próximo daquele prompt simples que já vinha sendo usado no exemplo anterior.

Cada prompt pode trazer um README com instruções de uso, contexto e orientação de integração. Isso transforma o prompt em um artefato publicável e compreensível por terceiros, porque não basta disponibilizar o texto: é preciso explicar como usar, quais entradas esperar e qual problema ele resolve. Quando um prompt remoto tem documentação acoplada, a descoberta e o reuso deixam de depender de conhecimento tácito da equipe que o criou.

O hub não serve apenas para navegação manual; ele também expõe um caminho de consumo programático por SDK. Retomando o uso de SDK já visto como ponte entre gestão externa e aplicação, o ponto novo é que o prompt pode ser baixado diretamente do hub, em vez de ser lido de um arquivo local versionado no projeto. Em sistemas de maior escala, esse consumo remoto costuma ser combinado com cache para evitar chamadas de API contínuas a cada execução.

O histórico de commits aparece no hub como parte do ciclo de vida do prompt publicado. Essa visualização aproxima o prompt de um artefato de software convencional: mudanças ficam registradas, podem ser inspecionadas e ajudam a entender evolução e manutenção. Aqui, o valor prático não está em redefinir commits, mas em perceber que o repositório remoto expõe esse histórico como parte da governança do prompt.

Prompt tags são metadados usados para classificar e localizar prompts dentro do LangSmith. Elas melhoram busca e descoberta no hub, especialmente quando o acervo cresce e passa a conter muitos prompts publicados por equipes diferentes. Essas tags não devem ser confundidas com mecanismos de versionamento ou com tags associadas a commits, porque sua função principal aqui é indexação e organização para pesquisa.

O fork permite partir de um prompt existente no hub e criar uma derivação própria para adaptação ou experimentação. Isso é útil quando um prompt público resolve parte do problema, mas precisa de ajustes para o contexto específico da sua aplicação, sem alterar o original. O modelo incentiva reaproveitamento com isolamento: você herda uma base útil, mas mantém autonomia para evoluir sua variante.

O Prompt Hub suporta repositórios públicos e privados, reproduzindo uma distinção operacional essencial. Repositórios públicos favorecem compartilhamento, descoberta e reutilização por qualquer pessoa com acesso ao hub; repositórios privados restringem visibilidade e consumo, o que é necessário quando o prompt faz parte do comportamento interno de uma aplicação. Nesse cenário, o acesso programático normalmente depende de autenticação por API key, de modo que apenas clientes autorizados consigam carregar o artefato remoto.

Retomando o prompt que antes vivia no projeto local, ele agora ganha uma camada de publicação: passa a ter página própria, documentação, histórico, tipo declarado e possibilidade de download. O desenvolvedor pode navegar pelo hub, identificar se o artefato é chat prompt ou string prompt, ler o README, inspecionar commits, aplicar filtros por prompt tags e decidir entre consumir, fazer fork ou manter uma versão privada. Essa camada não substitui os princípios anteriores de organização e integração; ela desloca o ponto de gestão para uma plataforma remota com descoberta e governança mais visíveis.

## Transcrição

00:01

Bom, pessoal, como eu falei para vocês, nós temos opções que vão fazer essa gestão de prompts para a gente, onde os prompts não necessariamente vão precisar ficar dentro do nosso projeto, dentro do nosso código-fonte, dentro do nosso Git, mas, eventualmente, se você for rodar em larga escala, você vai precisar de fazer um cache, você não vai ficar fazendo chamada de API o tempo inteiro.

00:26

O lance é o seguinte, se você olhar aqui, depois você pode buscar facilmente no Google, etc., mas é o hub.langsmith. Basicamente, aqui ele é um repositório de prompts. Agora, nem apenas mais só de prompts, agora ele já tem outras coisas também. Antigamente era somente para prompts, mas a ideia aqui é que a gente tenha como se fosse um GitHub.

00:52

Legal? Mas é um GitHub onde diversas pessoas podem publicar seus prompts e você poder utilizar esses prompts da forma que você quiser dentro dos seus projetos. Então, você vai perceber de diversas formas aqui que tem... Vou colocar os mais vistos aqui, por exemplo. Você vai perceber que eu consigo olhar diversos prompts

01:22

Por exemplo, esse reg prompt aqui, tem curtida, tem visualização, tem downloads, olha isso aqui galera, 27.6 milhões de downloads esse tipo de prompt, tá? Ele fala qual é o tipo de prompt, porque tem chat prompt, ou seja, que tem instruções do sistema e tudo mais, e tem string prompt, que na realidade é uma, basicamente,

01:43

uma chamada, o conteúdo todo de um prompt que você vai colocar. Então, tem conversação e também tem somente o prompt. O que a gente tem lá, que eu mostrei pra você, é apenas o prompt que a gente trabalha. Beleza? Então, o que acontece aqui? Se eu chego aqui, ele está falando que é um prompt pra gente fazer reg, tá? E aqui, você vai perceber que ele tem

02:04

O README, onde você tem um tutorial da utilização. Aqui tem, basicamente, como é que funciona o prompt básico, ou seja, pergunta, resposta e o contexto. E aqui você tem como que você consegue baixar esse prompt utilizando um SDK para você trabalhar. Então, ele mostra como que você importa, como que você chama e como que as coisas funcionam.

02:31

Aqui também você vai perceber que ele vai mostrar para vocês os commits que tiveram em relação a esse prompt, e a gente tem algo também chamado de prompt tags, que ajuda a gente a buscar. Mas existe uma confusão muito clara em relação a essas prompts tags com as tags dos seus commits, e isso eu vou garantir para você que eu vou salvar um belo de um tempo de pesquisa e bater a cabeça na hora que você for fazer a gestão dos seus prompts. Pode ter certeza que eu vou te mostrar.

02:59

Então, se você perceber, eu tenho aqui a documentação, eu tenho a lista dos meus commits, basicamente um GitHub de prompts que eu posso usar, baixar e tudo mais. Beleza? Posso fazer fork da forma como eu queira trabalhar. Maravilha?

03:17

Outro ponto importante é que nesse hub de prompts da lang.smith, da mesma forma como o GitHub tem repositórios públicos, nesse hub ele também tem repositórios públicos, mas ele também tem repositórios privados.

03:36

Então, eu posso, utilizando o LanguageMix como desenvolvedor ou em planos pagos, etc., você pode ter os seus prompts que não ficam públicos, e aí somente a sua aplicação vai conseguir chamar.

03:51

E você vai perceber que vai precisar também de uma API key. Maravilha? Então, no próximo vídeo, eu vou mostrar um pouco para vocês como é que funciona essa interface do Langsmith. A gente vai dar uma navegadinha. Foco total aqui apenas na parte de gestão de prompt.

04:08

porque o Langsmith tem muita coisa bacana, é uma plataforma bem grande, bem completa, e a gente vai utilizar esse cara aí pra fazer algumas coisas, inclusive, aí no futuro. Fechou? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **README**: *Read Me* — arquivo de documentação com instruções de uso, contexto e orientação de integração.  
- **SDK**: *Software Development Kit* — kit de desenvolvimento usado para consumir o prompt programaticamente.  
- **API**: *Application Programming Interface* — interface usada para chamadas de acesso ao serviço remoto.  
- **API Key**: chave de autenticação para autorizar o consumo de recursos privados.  
- **Git**: sistema de controle de versão usado como referência para histórico e organização de artefatos.  
- **GitHub**: plataforma de repositório e colaboração usada como analogia para o Prompt Hub.  
- **LangSmith**: plataforma do ecossistema LangChain usada para gestão e consumo de prompts.  

**Resumo**  
A aula apresentou o Prompt Hub do LangSmith como uma plataforma centralizada para publicar, descobrir, documentar, versionar e consumir prompts remotamente, de forma semelhante a um GitHub de artefatos de prompt. O instrutor explicou que, em vez de manter o prompt somente dentro do código-fonte ou do repositório local da aplicação, ele pode viver no hub e ser baixado em runtime, o que facilita reutilização, compartilhamento e governança. Também foi destacado que, em cenários de escala, esse consumo remoto deve ser combinado com cache para evitar chamadas de API constantes.

Foram abordados dois formatos de artefato disponíveis no hub: **chat prompt**, estruturado em mensagens com papéis como system e user, mais adequado para fluxos conversacionais; e **string prompt**, que representa o conteúdo textual direto em uma única instrução. O instrutor mostrou que cada prompt pode ter um **README** com explicações de uso, entradas esperadas, contexto e integração, tornando o artefato compreensível por terceiros e reduzindo dependência de conhecimento tácito.

A aula também mostrou que o hub oferece consumo programático por **SDK**, além da navegação manual. O prompt pode ser baixado diretamente da plataforma, e sua página exibe histórico de commits, o que ajuda a acompanhar evolução e manutenção. Outro recurso mencionado foram as **prompt tags**, metadados para classificar e localizar prompts dentro do catálogo, facilitando busca e descoberta em acervos maiores. Por fim, foi explicado que é possível fazer **fork** de um prompt existente para criar uma derivação própria, e que o Prompt Hub suporta repositórios públicos e privados, com acesso controlado por autenticação via **API key** quando o conteúdo não deve ficar visível para todos.

**Pontos de atenção**  
- Em uso em larga escala, evitar buscar o prompt remotamente a cada execução; considerar **cache** para reduzir chamadas de API.  
- Não confundir **prompt tags** com tags de commit: elas servem para indexação e busca no hub, não para versionamento de código.  
- Ler o **README** antes de consumir ou reutilizar um prompt, para entender entradas esperadas, contexto e forma correta de integração.  
- Identificar corretamente o tipo de artefato: **chat prompt** e **string prompt** têm estruturas e usos diferentes.  
- Aproveitar o histórico de commits para rastrear mudanças e evolução do prompt, especialmente em ambientes colaborativos.  
- Usar **fork** quando precisar adaptar um prompt público sem alterar o original.  
- Considerar a diferença entre repositórios públicos e privados; prompts privados exigem controle de acesso e **API key**.  
- Tratar o Prompt Hub como uma camada de governança e distribuição, não como substituto da disciplina de organização e integração do prompt na aplicação.