Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16728)

## Resumo da aula

Criar prompts pela interface do LangSmith começa com um pré-requisito operacional simples: gerar uma API key em Settings > API Keys e armazená-la nas variáveis de ambiente. Essa chave não serve para editar o prompt na tela, mas viabiliza reproduzir fluxos e preparar a integração posterior com a aplicação. Retomando a gestão remota já vista, a interface passa a ser o ponto de autoria, enquanto o consumo programático fica para a etapa seguinte.

A criação de um prompt começa pela escolha entre chat prompt e prompt baseado em instruções. No formato de chat, a interface organiza mensagens por papel, como system e human, além de permitir adicionar mensagens extras, ferramentas e esquema de saída. No formato de instruções, o prompt vira um template textual único, mais adequado quando o comportamento pode ser expresso como uma string parametrizada sem estrutura conversacional.

O prompt de instruções aparece como um StringPromptTemplate com duas partes visíveis: o template e as variáveis de entrada. Essa separação é importante porque a interface deixa explícito o contrato do prompt sem exigir edição em arquivo local. Em vez de alterar YAML ou código, a autoria acontece diretamente no formulário, o que reduz atrito para ajustes rápidos e para colaboração com pessoas fora do time de desenvolvimento.

O playground é o ambiente de teste imediato do prompt antes do salvamento. Ao definir um template como quanto é x mais y?, a interface expõe os inputs correspondentes, permite preencher valores como 2 e 3 e executar o prompt na hora. Esse ciclo curto de editar, preencher entradas e rodar evita publicar um artefato sem validação básica de comportamento.

A execução no playground depende da escolha de um modelo compatível com o tipo de teste desejado. No exemplo, a troca para GPT-4o mini foi necessária para rodar o fluxo pretendido, mostrando que o resultado do playground não depende apenas do texto do prompt, mas também da configuração do modelo. Quando um teste falha ou não executa como esperado, uma das primeiras verificações deve ser justamente o modelo selecionado.

A interface não mostra apenas a resposta final; ela também expõe sinais operacionais da execução. Depois do teste, ficam visíveis o tempo de processamento, o status da execução, a contagem de input tokens, a contagem de output tokens e o custo estimado daquela chamada. Esses dados transformam o playground em uma ferramenta de ajuste técnico, porque permitem avaliar não só qualidade da resposta, mas também impacto financeiro e eficiência.

Além de executar o prompt, o playground funciona como área de experimentação controlada. É nele que se testa uma pequena mudança no template, se compara o efeito de inputs diferentes e se observa se o custo cresce sem ganho proporcional de resultado. Essa etapa é especialmente útil quando o prompt ainda está sendo refinado por produto, operação ou prompt engineering, sem necessidade de alterar o repositório da aplicação.

Depois de validar o comportamento, o prompt pode ser salvo com um nome, como a soma, e passa a aparecer na listagem de prompts da plataforma. A interface registra o tipo do artefato, exibe informações como último commit e mantém o prompt organizado no hub, sem exigir que o autor preencha toda a estrutura manualmente. O salvamento transforma um experimento temporário do playground em um artefato persistente e reutilizável.

O prompt salvo nesse fluxo pode permanecer privado, o que é coerente com prompts que fazem parte do comportamento interno de uma aplicação. Lembra da gestão remota já estabelecida: aqui ela ganha a camada operacional de autoria, em que uma pessoa de produto ou outra função da empresa consegue criar e ajustar o prompt sem mexer no Git do software. O desenvolvedor continua responsável pela integração em runtime, mas a edição do conteúdo deixa de depender exclusivamente do repositório da aplicação.

Esse fluxo não substitui a organização local de prompts já vista anteriormente; ele oferece uma alternativa de autoria e governança fora do código. Em muitos projetos, prompts continuarão em pastas versionadas no repositório, mas a interface do LangSmith atende cenários em que a edição precisa ser mais acessível e menos acoplada ao ciclo de desenvolvimento. O ponto central é separar onde o prompt é criado e ajustado de onde ele será consumido pela aplicação.

## Transcrição

00:01

Bom, pessoal, seguinte, uma vez que você entrou no site da LangChain, fez o sign-up, você teve acesso a entrar nessa ferramenta na aplicação do LangSmith. Então, pelo menos até o momento dessa gravação, a interface é assim, pode mudar, coisas assim, mas eu acredito que os conceitos acabam sendo os mesmos.

00:25

Então, quando você entra, uma das coisas que eles usam muito para o Langsmith é a parte de observabilidade. Eu não vou nem passar perto dela aqui, se você olhar aqui eu tenho alguns projetos, mas eles têm muita coisa baseada em relação a observabilidade e evaluation.

00:43

e outros aspectos importantes. Então, aqui, nesse nosso caso, o que eu recomendo que você faça assim que você entrar, inclusive para você conseguir, caso você queira reproduzir os exemplos que eu vou te mostrar daqui a pouco, tá? Você vai ter que criar uma chave de API, tá? Então, provavelmente, você vai em Settings, API Keys, e você cria uma chave de API para você poder utilizar e você vai colocar nas suas variáveis de ambiente, tá? Somente para

01:12

deixar claro aqui pra você. E o ponto principal onde eu quero trabalhar aqui pra vocês é a parte de prompts, que é a parte que nos interessa nesse contexto, tá? Então, se você perceber aqui, você vai ver que eu tenho aqui uma tela onde eu tenho

01:29

diversas opções e eu não tenho nenhum prompt aqui cadastrado. Então, o que acontece é o seguinte, eu posso criar um novo prompt ou no formato de chat ou no formato de instruções, ou seja,

01:45

depende de como você quer trabalhar e brincar com esse cara. Então, vou dar um Create Prompt aqui normalmente. Então, se você perceber, aqui eu estou em um formato de chat. Então, o que acontece? Eu tenho aqui, nesse caso, o System Prompt.

02:01

Aí eu tenho o humano escrevendo, aí eu posso adicionar mensagem, eu posso falar qual a ferramenta que ele tem, eu posso escolher o esquema de output que esse prompt vai trabalhar. Então, basicamente, quando eu trabalho nesse processo, eu tenho um tipo de prompt. Se eu voltar aqui para mim, para prompts,

02:22

e eu chegar e criar instruções, prompts baseados em instruções, você vai perceber aqui que eu tenho o meu template onde eu tenho as minhas instruções. E que se você fizer qualquer tipo de relação, olha só que interessante aqui,

02:44

Eu tenho as minhas variáveis de entrada e eu tenho o meu template. Então, isso aqui é um PromptStringTemplate, porque ele trabalha dessa forma. Ele não é baseado em uma conversa. Agora, uma coisa interessante que você tem é... Existem algumas coisas interessantes, que eu posso colocar assim, por exemplo. O que é... Quanto é... Eu posso colocar pis mais y.

03:12

Somente de eu fazer isso aqui, ou seja, esse é o meu prompt, legal? Quanto que é x mais y? E aqui eu tenho os inputs, inclusive, para eu fazer a execução aqui desse prompt. Eu posso colocar 2 e 3 e eu posso dar um start aqui. Ele vai rodar. Na realidade, inclusive, eu tenho que escolher um outro...

03:37

como se diz, o outro modelo para eu rodar streaming, somente para você saber, eu teria que usar um outro modelo aqui do meu modelo, porque o GPT-5 trabalha com streaming, deixa eu pegar aqui, vou pegar o GPT-4O mini aqui para mim. Beleza? Então vou deixar aqui dessa forma essa configuração, e agora vamos rodar somente para ver.

04:04

E aqui eu tenho 2 mais 3 é igual a 5. Então, basicamente, eu tive, na realidade, a execução aqui do meu prompt. E uma das coisas interessantes é que tudo que eu fiz aqui de input, ele pegou o tempo, ele pegou se essa execução acabou, ele trouxe aqui pra mim quanto que eu gastei de input token e output token, e ele consegue trazer ainda pra mim quanto que foi o meu custo

04:30

para rodar esse tipo de teste, somente para que você consiga ter uma ideia do nível de coisa interessante. E, baseado nisso, eu consigo, inclusive, fazer anotações e tudo mais. Vou mostrar para vocês isso um pouco depois. Mas eu acredito que deu para você, caso você nunca tenha visto alguma ferramenta desse tipo, entender o poder que a gente acaba tendo sobre poder testar e fazer evaluation de prompts.

04:55

que é uma outra área aqui, inclusive, você sobe datasets, bota os diversos prompts, ele vai rodar e vai trazer os resultados. Então, tem muita coisa interessante, mas olha só que coisa importante. Eu consigo, aqui nesse meu playground, trabalhar. Agora, se eu chegar agora aqui e dar um salvar, ele vai falar pra mim qual o nome que eu quero dar pra esse prompt. E eu vou colocar aqui, por exemplo,

05:21

a soma, sei lá, eu não estou com a mente mais criativa do mundo hoje, mas se você olhar aqui, eu posso visualizar o meu prompt, que ele até colocou agora aqui, no prompt hub. Então, se eu chegar aqui em prompts agora,

05:39

ele vai trazer aqui pra mim o prompt que eu tenho. E ele vai falar que é um StringPromptTemplate, vai falar a data de utilização, vai colocar o último commit e tudo mais. E tá ótimo, sem erro nenhum. Então, eu não preciso colocar algumas informações, eu posso organizar aqui na interface deles.

06:01

Beleza? Então, com isso, se você perceber, eu já tenho a minha forma de trabalhar com o prompt e esse cara aqui é privado. Agora, você deve estar pensando, ok Wesley, e o que isso tem a ver com o meu software? E aqui que é o grande ponto. Normalmente, quem vai trabalhar nesse processo aqui de mexer, gerenciar esses prompts, não necessariamente vai ser o desenvolvedor.

06:27

pode ser outra pessoa completamente diferente com outra função na empresa. E cada dia isso vai ser mais comum. E é por isso que essas plataformas geram essa flexibilidade, porque senão você teria que ficar dando acesso a Git e coisas desse tipo para um profissional que não tem esse foco. Às vezes é uma pessoa de produto, uma pessoa que está em outra área e está mexendo nos prompts ali da aplicação.

06:50

Isso não significa que você precisa usar essa ferramenta. Em muitos casos, você vai conseguir rodar da forma como eu te mostrei, organizando as pastas. Na maioria dos projetos, hoje em dia, você vai ver mais ou menos daquela forma, mas você tem essa opção de trabalhar aqui com o LangSmith. No próximo vídeo, eu vou mostrar para você como você consegue fazer com que a sua aplicação se integre com o LangSmith. Então, vamos nessa.

## Resumo IA

**Abreviações**  
- **API** — Application Programming Interface (Interface de Programação de Aplicações)  
- **API key** — Chave de API  
- **Git** — Sistema de controle de versão distribuído  
- **GPT-4o mini** — Modelo da família GPT-4o, versão mini  
- **LLM** — Large Language Model (Modelo de Linguagem de Grande Porte)  
- **LangChain** — Framework para aplicações com modelos de linguagem  
- **LangSmith** — Plataforma da LangChain para observabilidade, avaliação e gerenciamento de prompts  
- **Output** — Saída  
- **Prompt String Template** — Modelo de prompt em formato de string, baseado em texto parametrizado  
- **System Prompt** — Instrução de sistema  
- **YAML** — YAML Ain’t Markup Language (formato de serialização de dados legível por humanos)  

**Resumo**  
A aula apresentou o fluxo de criação e teste de prompts na interface do LangSmith, começando pelo pré-requisito operacional de gerar uma API key em Settings > API Keys e configurá-la nas variáveis de ambiente para viabilizar a reprodução dos exemplos e a integração posterior com a aplicação. O instrutor destacou que o foco da interface aqui é a autoria e o gerenciamento dos prompts, enquanto o consumo programático fica para uma etapa seguinte. Em seguida, mostrou a diferença entre criar um prompt no formato de chat e no formato de instruções: no chat, o prompt é estruturado por mensagens com papéis como system e human, podendo incluir mensagens adicionais, ferramentas e esquema de saída; já no formato de instruções, o conteúdo é tratado como um template textual único, mais adequado quando o comportamento desejado pode ser expresso como uma string parametrizada.

No caso dos prompts por instruções, a interface deixa visível a separação entre template e variáveis de entrada, caracterizando um StringPromptTemplate. O instrutor demonstrou que é possível editar o texto diretamente na interface, sem precisar alterar arquivos locais, YAML ou código, o que facilita ajustes rápidos e colaboração com pessoas fora do time de desenvolvimento. O playground foi apresentado como ambiente de teste imediato: ao definir um template como “quanto é x mais y?”, a interface gera os campos de entrada correspondentes, permite preencher valores e executar o prompt na hora, fechando um ciclo curto de edição, validação e ajuste. Também foi ressaltado que o resultado depende não só do texto do prompt, mas do modelo escolhido; por isso, em um dos testes foi necessário trocar para GPT-4o mini para que a execução funcionasse conforme esperado.

Além da resposta final, o playground exibe informações operacionais importantes da execução, como tempo de processamento, status, contagem de tokens de entrada e saída e custo estimado da chamada. Isso transforma o ambiente em uma ferramenta de experimentação e avaliação técnica, útil para comparar pequenas mudanças no prompt, observar impacto em qualidade e custo e validar comportamento antes de publicar um artefato. Após a validação, o prompt pode ser salvo com um nome e passa a aparecer no prompt hub da plataforma, com tipo de artefato, data de utilização e último commit, permanecendo como um item privado e reutilizável. O instrutor concluiu relacionando esse fluxo ao contexto de produto e operação: a autoria pode ficar com outras funções além do desenvolvimento, sem exigir acesso direto ao Git, enquanto a organização local de prompts continua sendo uma alternativa válida em muitos projetos.

**Pontos de atenção**  
- A criação da **API key** em **Settings > API Keys** e sua configuração nas variáveis de ambiente é necessária para reproduzir os exemplos e preparar a integração futura.  
- A interface do LangSmith pode mudar visualmente com o tempo, mas os conceitos centrais tendem a permanecer os mesmos.  
- É importante escolher corretamente entre **prompt de chat** e **prompt de instruções** conforme o tipo de comportamento que se quer modelar.  
- Em prompts de instruções, observar a separação entre **template** e **variáveis de entrada** ajuda a entender o contrato do prompt.  
- O **playground** deve ser usado para testar antes de salvar; ele evita publicar prompts sem validação básica.  
- O comportamento do teste depende também do **modelo selecionado**; se a execução falhar, a primeira verificação deve ser o modelo configurado.  
- Monitorar **tempo, tokens e custo** é essencial para avaliar não só a qualidade, mas também a eficiência e o impacto financeiro do prompt.  
- Pequenas mudanças no template podem alterar bastante o resultado, então comparar versões no playground é uma boa prática.  
- O prompt salvo pode ficar **privado**, o que faz sentido para comportamentos internos de aplicação.  
- A gestão de prompts não precisa ficar restrita ao desenvolvedor; a interface permite autoria por outras áreas, como produto ou operação, reduzindo dependência do Git.  
- O fluxo apresentado não substitui a organização local de prompts no repositório; ele funciona como uma alternativa de autoria e governança fora do código.