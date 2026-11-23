Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16730)

## Resumo da aula

O langsmith_client representa a etapa em que a aplicação consome um prompt remoto em vez de depender de um arquivo local. Retomando o prompt agent-pull-request-creator, o fluxo passa por identificar o prompt, fazer o pull via SDK e usar o artefato retornado na composição com o modelo. O efeito prático é que o texto do prompt deixa de ser responsabilidade direta do código da aplicação, embora continue sendo parte do comportamento executado. Isso separa autoria e governança do prompt da integração em runtime.

Depois do pull, o prompt já pode ser encadeado com o modelo e executado com invoke, recebendo o dicionário de entradas esperado. O ponto importante não é a sintaxe específica da linguagem, mas o contrato operacional: a aplicação baixa um artefato remoto, injeta os inputs e executa o LLM com aquele estado do prompt. Isso permite que o software use um prompt mantido por outra pessoa ou equipe, desde que o ID e a referência de versão sejam estáveis.

Quando nenhuma versão específica é informada no consumo, o SDK resolve o prompt para o estado mais recente disponível. Esse comportamento é conveniente para desenvolvimento rápido, mas é arriscado quando a aplicação precisa de reprodutibilidade, rollback ou promoção controlada entre ambientes. Em produção, depender implicitamente da última revisão significa aceitar mudança de comportamento sem fixação explícita do estado consumido.

Prompt tags, já usadas anteriormente no push, continuam sendo apenas metadados de catalogação e busca. Acrescentar algo como :1.0.0 no consumo não funciona se essa informação foi criada como prompt tag, porque ela não aponta para um commit executável. O erro de “commit não encontrado” expõe exatamente essa diferença: a aplicação não baixa “a tag textual do prompt”; ela baixa um estado versionado identificado por commit.

Commit tag é o rótulo associado a um commit específico do histórico e é esse rótulo que o SDK usa para resolver qual revisão baixar. Se nenhuma commit tag existir, a alternativa é referenciar diretamente o hash do commit, que é o identificador real daquele estado. A consequência é direta: prompt tag organiza o catálogo, enquanto commit tag controla qual versão entra em execução.

Como a plataforma restringe o uso de pontos, a convenção de nome precisa ser adaptada para strings como v1-0-0, dev ou prod. Essa limitação não muda o mecanismo de versionamento; ela apenas afeta a forma de nomear referências legíveis para humanos. O valor dessas tags está em traduzir o histórico técnico de commits para referências operacionais que a aplicação consegue consumir com clareza.

Associar dev a um commit antigo e prod ao commit mais recente cria uma camada simples de promoção entre estados do prompt. A aplicação pode apontar para dev durante experimentação e para prod em runtime estável, sem alterar o conteúdo do prompt no código. O mesmo mecanismo serve para rollback: basta reposicionar a commit tag para outro commit válido, em vez de editar a aplicação.

O fluxo correto é: publicar o prompt, consultar o histórico de commits, criar uma commit tag no commit desejado e consumir o prompt remoto usando o ID mais essa referência operacional. Se o desenvolvedor tentar usar uma prompt tag como se fosse versão, o SDK não encontrará o commit correspondente. Quando a referência está correta, o pull baixa o estado exato do prompt e o restante do pipeline executa normalmente com o modelo.

Consumir prompt remoto em toda execução adiciona chamadas de API desnecessárias e aumenta latência, custo e dependência da disponibilidade da plataforma. Por isso, o padrão recomendado é baixar o prompt e armazená-lo em cache, renovando esse cache conforme a estratégia de atualização da aplicação. O cache não substitui o versionamento; ele reduz o custo operacional de consultar repetidamente uma versão que já foi resolvida.

O ponto decisivo não é o código do exemplo, porque a mesma lógica pode ser implementada em qualquer linguagem. O que precisa ficar fixo é a distinção entre metadado de organização e referência real de execução: prompt tag classifica, commit tag versiona operacionalmente. Sem essa separação conceitual, o consumo remoto parece funcionar até o momento em que a aplicação precisa escolher exatamente qual revisão do prompt deve rodar.

## Transcrição

00:01

Bom, pessoal, agora a gente percebeu que nós temos o nosso prompt todo bonitão aqui, mas vamos imaginar que eu quisesse utilizar agora esse prompt. Como é que funcionaria, galera? Então, vamos lá. Eu, além de ter criado um arquivo chamado lang.smith.push, eu criei um chamado lang.smith.client, tá? E agora a coisa fica um pouco interessante aqui pra gente, tá?

00:28

O que acontece é o seguinte, se você perceber, olha só o que eu estou fazendo.

00:35

Fiz o meu client, falei que o meu prompt é pull prompt e passei o nome dele, que é agent pull request creator, que é o prompt que a gente está trabalhando. Estou chamando aqui OpenAI, aqui para mim. Estou aqui fazendo meu change prompt e depois chamando o meu modelo. E aqui estou fazendo o invoke desse meu prompt, passando todo o meu dicionário das informações que ele precisa para rodar.

01:05

ponto o conteúdo do meu prompt. Então, isso significa que, no final das contas, quando eu dei um pull prompt, ele já carregou esse prompt para mim, baixando, fazendo uma chamada lá no nosso prompt hub, lá no langsmith. Então, vamos fazer esse cara aqui funcionar. Então, vamos lá. Eu vou dar um python src langsmith client.py

01:39

Vamos aguardar um pouquinho, porque ele não só baixou, como ele também executou o LLM, e você viu que funcionou de boas. Ou seja, eu consegui baixar o prompt vindo lá do lang.smith.

01:54

Então, se você perceber, agora eu, como desenvolvedor, não me importo mais em relação ao prompt. O que eu me importo é que eu vou dar um pulo no prompt e quem estiver lá mexendo no Langsmith, por exemplo, vai ser responsável pela qualidade daquele prompt. É basicamente isso que acaba acontecendo. Ou seja, a gente consegue isolar as responsabilidades agora. Agora, uma das coisas que eu não sei se você percebeu é que

02:21

Eu estou utilizando esse prompt e ele está pegando, nesse nosso caso aqui, a nossa última versão, que é essa versão que está aqui. Tem três pontinhos aqui, se eu não me engano. Se eu for nesse commit aqui, se eu não me engano, não tem os três pontinhos. Eu acho que era essa a diferença que eu fiz.

02:39

Agora, se você olhar, lembra que naquele prompt eu tinha colocado a versão 1.0.0? Então, vamos fazer o seguinte, eu vou chegar agora aqui e vou colocar agora, dois pontos, 1.0.0, para eu pegar aquela minha primeira versão da tag que eu tinha colocado. Vou executar agora aqui, olha só que interessante, vamos lá. E deu erro para mim, porque ele falou que não encontrou esse commit. Por que ele não encontrou esse commit? Porque

03:09

ou o langsmith, ele utiliza o hash como identificador do prompt. O que eu estou querendo dizer é que se você for aqui, esse cara aqui, tanto faz, isso aqui é pra você, pra você buscar, pra ficar, se organizar, mas isso não tem nenhuma relação

03:35

com o pool que você vai dar nesse prompt aqui. Não tem absoluta nenhuma relação. E você deve estar pensando, então, ok, eu tenho o meu prompt com duas versões e eu quero usar a versão antiga. Como é que eu faço para fazer isso? Então, a resposta para isso é que, pelo menos até o momento dessa gravação, isso é feito de forma manual. Como assim de forma manual?

04:02

eu posso entrar no meu prompt, beleza? Eu posso ver aqui o meu histórico de commits, e se você perceber aqui ó, aqui eu consigo fazer uma tag, mas é um commit tag. Então entenda que existe prompt tag, que é o que você criou, e tem o commit tag, tá? O commit tag é a tag que ele vai utilizar

04:24

pra fazer o download do prompt. Se você deixar ela vazia, você vai ter que passar a string, o hash do string do post pra você conseguir baixar. Ou você pode chegar e fazer o seguinte, eu posso colocar aqui pra mim um commit tag, eu posso colocar, por exemplo, latest.

04:43

A lei tece por padrão, ela já existe, mas eu posso colocar 1.0.1 ou posso colocar V na frente, da forma como você queira colocar. Mas, uma coisa interessante aqui nessas prompt tags é que, primeira coisa, ela não vai deixar você fazer pontos aqui dentro,

05:03

e ela vai também forçar com que, de alguma forma, você também possa trabalhar com strings para conseguir ficar de uma forma um pouco mais organizada. Então, eu posso colocar v1.0.1, dessa forma, ou eu posso colocar, por exemplo, prod. Ou seja, eu sei que esse cara está em produção. Eu posso colocar esse cara aqui como deve que ele está, esse prompt, em desenvolvimento.

05:31

Legal? Eu posso colocar o versionamento dele, posso colocar também a versão 1.1, não sei o quê, não sei o quê. Eu posso escolher como eu organizo. Agora, a grande questão aqui é que o que você vai perceber é que essa tag vai ter relação direta agora com o seu prompt. E, na prática, isso significa o quê? Se eu chegar aqui agora e colocar dev,

06:01

ele vai conseguir fazer o download da versão do meu primeiro commit.

06:09

Se eu colocar prod, ele vai pegar do último commit. Se eu quiser colocar a versão 1, não sei o quê, eu posso colocar, só não posso usar ponto. Então, eu posso colocar 1, v1, traço 0, traço 0. Isso aqui ele vai me deixar colocar. Acho bem chato ele não permitir colocar com pontos aqui, mas paciência. Mas, eu acho que agora começa a fazer um pouco mais de sentido como que você consegue gerenciar. Porque, nesse momento,

06:39

Usando o SDK, eu consigo baixar o prompt que está no Langsmith, que outra pessoa criou, e eu tenho apenas o ID desse prompt, a versão do prompt que eu vou utilizar, e a partir daí eu consigo trabalhar com o meu software. Considerações importantes, tá? Se você for utilizar essa abordagem usando o Langsmith, usando o Prompt Layer, usando qualquer Langfuse, independente do cara que você vai utilizar,

07:05

Recomendo sempre é baixe esse prompt, guarde ele num cache, porque senão toda hora você vai ter que ficar fazendo chamadas de API. Apenas uma dica aí pra você se lembrar, porque senão não faz sentido a gente ficar baixando esse cara toda hora aí.

07:22

Agora, o ponto mais importante de tudo isso aqui não é o código que eu mostrei, porque o código é um detalhe independente da linguagem de programação. O que eu acho aqui importante em relação é a gente entender esse conceito. Então, vamos empacotar essas nossas ideias com uma conclusão.

## Resumo IA

**Abreviações**  
- **SDK** — *Software Development Kit*  
- **LLM** — *Large Language Model*  
- **API** — *Application Programming Interface*  
- **ID** — *Identificador*  

**Resumo**  
A aula apresentou o consumo de prompts remotos com o `langsmith_client`, mostrando que a aplicação deixa de depender de um arquivo local e passa a baixar o prompt diretamente do LangSmith via SDK. O instrutor retomou o prompt `agent-pull-request-creator` e explicou o fluxo em que o prompt é identificado, feito o *pull* e então encadeado com o modelo para execução por meio de `invoke`, recebendo um dicionário com os inputs necessários. A ideia central é separar a autoria e a governança do prompt da integração em tempo de execução, permitindo que outra pessoa ou equipe mantenha o prompt enquanto a aplicação apenas consome uma referência estável.

Também foi explicado o comportamento de resolução de versão: quando nenhuma versão explícita é informada, o SDK baixa o estado mais recente do prompt. Isso é conveniente para testes e desenvolvimento, mas perigoso em produção, porque permite mudanças de comportamento sem controle explícito da revisão consumida. O instrutor diferenciou claramente *prompt tag* de *commit tag*: a *prompt tag* serve para catalogação e busca, enquanto a *commit tag* é a referência usada para baixar efetivamente a revisão do prompt. Se não houver *commit tag*, é possível usar o hash do commit diretamente, que é o identificador real do estado versionado. O exemplo também mostrou que a plataforma não aceita pontos em certas tags, exigindo convenções como `v1-0-0`, `dev` ou `prod`. Por fim, foi reforçado que o fluxo correto envolve publicar o prompt, consultar o histórico de commits, associar uma *commit tag* ao commit desejado e consumir o prompt remoto com o ID e a referência operacional correta. O uso de cache foi recomendado para evitar chamadas de API a cada execução, reduzindo latência, custo e dependência da disponibilidade da plataforma.

**Pontos de atenção**  
- Não confundir **prompt tag** com **commit tag**: a primeira organiza e ajuda na busca; a segunda define a versão executável.  
- Usar uma **prompt tag** como se fosse versão de execução causa erro de “commit não encontrado”.  
- Se nenhuma versão for informada, o SDK resolve para a **última revisão disponível**, o que pode ser arriscado em produção.  
- Em produção, é importante **fixar explicitamente a revisão** consumida para garantir reprodutibilidade, rollback e promoção controlada.  
- Quando não houver *commit tag*, deve-se usar o **hash do commit** correspondente ao estado desejado.  
- A nomenclatura das tags precisa respeitar as **restrições da plataforma**, como a não aceitação de pontos.  
- Tags como `dev` e `prod` podem ser usadas para representar **ambientes ou estados operacionais** e facilitar promoção/rollback.  
- Consumir o prompt remoto em toda execução aumenta **latência, custo e dependência de disponibilidade**; por isso, é melhor **baixar e cachear** o prompt.  
- O importante é entender o **contrato operacional** do fluxo, não a sintaxe de uma linguagem específica.  
- A separação entre quem **edita/governa** o prompt e quem **executa** a aplicação é uma boa prática central da abordagem.