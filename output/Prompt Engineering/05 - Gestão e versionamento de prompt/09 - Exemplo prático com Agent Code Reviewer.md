Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16723)

## Resumo da aula

prompt_registry.py concentra o acesso ao registry.yaml e transforma o índice de prompts em uma API de uso dentro da aplicação. Em vez de espalhar caminhos de arquivos e leitura de metadados pelo código, a aplicação consulta um ponto único, como registry.getPrompt(id). Isso reduz acoplamento com a estrutura física da pasta prompts e cria uma fronteira clara entre o código executável e os artefatos versionados. Retomando o registry já definido anteriormente, a novidade aqui é seu uso como dependência real de runtime.

Uma dataclass para o request do prompt modela explicitamente todas as entradas esperadas pela execução, como diff, linguagem, rules, security_level e review_focus. Esse objeto funciona como contrato entre o código da aplicação e o prompt estruturado, evitando passar um dicionário solto sem semântica clara. A vantagem prática é validação conceitual mais simples, melhor legibilidade e menor risco de esquecer ou nomear incorretamente uma variável. O mesmo raciocínio se estende ao output da LLM: quanto mais o comportamento do prompt entra no software, mais importante se torna modelar entrada e saída como dados de aplicação.

loadPrompt faz a ponte entre o arquivo YAML versionado e um template executável compatível com LangChain. A função recebe o caminho físico do prompt, faz o parse do arquivo e devolve um PromptTemplate, pronto para interpolar as variáveis declaradas anteriormente no prompt.yml. Isso elimina a necessidade de montar manualmente o template em código e preserva o prompt como artefato externo, versionado e carregável em runtime. Se o arquivo estiver malformado ou incompatível com o contrato esperado, a falha aparece no carregamento, o que facilita diagnóstico.

O chain encadeia três etapas: template, modelo e parser de saída. Primeiro, o PromptTemplate recebe os valores concretos do request; depois, a LLM executa a inferência; por fim, o parser converte a resposta para um formato consumível pela aplicação. Essa composição deixa o fluxo explícito e separa responsabilidades: o prompt monta a instrução, a LLM gera a resposta e o parser trata a saída. Em implementações simples, o parser pode apenas retornar texto; em cenários mais controlados, ele pode preparar a base para saídas estruturadas.

A chamada com invoke exige que as variáveis do template sejam entregues no formato esperado pela biblioteca, normalmente um dicionário chave-valor. Por isso, o objeto tipado do request é convertido antes da execução, preservando a ergonomia de modelagem no código e a compatibilidade com a interface do chain. Essa etapa parece trivial, mas é onde surgem muitos erros de integração: nomes divergentes entre atributos e placeholders, campos ausentes ou valores montados no formato errado. O request tipado reduz esse risco, mas não elimina a necessidade de consistência com o contrato do prompt.

No agente Code Reviewer, o campo principal do request é o diff, porque a revisão depende do trecho alterado, e os demais atributos refinam o comportamento esperado da análise. Linguagem, regras do repositório, foco da revisão e nível de segurança não são detalhes acessórios; eles condicionam o tipo de crítica que a LLM deve produzir. O exemplo mostra a evolução direta do prompt já estruturado: aquilo que antes era apenas um artefato versionado agora participa do fluxo real da aplicação. O resultado final da Code Review passa a ser consequência de um pipeline reproduzível, não de um prompt colado manualmente.

Quando o script é executado, o fluxo completo fica visível: localizar o prompt no registry, obter seu caminho, carregar o YAML como template, instanciar a LLM, montar o chain e chamar invoke com os dados do request. Esse encadeamento é a primeira integração operacional do sistema de prompts com o código da aplicação. A principal decisão técnica aqui é manter o prompt fora do código-fonte e carregá-lo dinamicamente, o que preserva versionamento, rastreabilidade e possibilidade de troca sem reescrever a lógica de execução. O script do agente demonstra exatamente essa passagem do artefato estruturado para comportamento executável.

## Transcrição

00:01

Bom, pessoal, agora que a gente falou um pouco de a estrutura, de como que eu coloquei os arquivos, o meu YAML aqui, no caso, dos meus prompts, eu quero também trazer aqui para vocês algumas formas em relação a código, de como que eu posso utilizar isso aí para a gente. E o que eu tenho aqui somente como exemplo que eu preparei para mostrar isso aqui funcionando?

00:30

Então, se você olhar, eu tenho um prompt underline registry.py, um arquivo que foi criado exatamente para conseguir carregar aquele registry.yaml, para conseguir trazer o caminho do prompt, para trazer os metadados do prompt, para conseguir ler. Então, basicamente, é um arquivo que serve realmente para pegar essas informações.

00:55

mas não apenas para pegar essas informações também. Esse nosso arquivo também vai nos ajudar a fazer o quê?

01:08

vai nos ajudar a estruturar a forma de como que a gente vai trabalhar com as variáveis dentro da nossa aplicação. Então, eu criei uma classe muito clara aqui, poderia estar trabalhando ali com Data Class, com PyIdentic e etc. Cada vez isso vai ser mais importante, ter um modelo de dados do seu prompt, modelo de dados de como que você, inclusive, vai pegar os resultados

01:34

da sua LLM, tá? Então, isso aí é extremamente importante. Mas, deixa eu mostrar aqui pra vocês um cara desse sendo utilizado, tá? Então, o que acontece, o que eu fiz aqui, né? Foi o seguinte...

01:49

Eu criei uma classe no formato aqui de data class, então basicamente eu tenho esses atributos que eu posso trabalhar, então coloquei aqui todos os inputs que o meu prompt precisa, criei aqui meu objeto,

02:05

E nesse meu objeto eu tenho, o meu primeiro parâmetro é o diff, porque é um CodeReview, a linguagem é Python, as rules do meu repositório, security level, review focus, etc. Então, está aqui o meu objeto em relação ao request. Nesse caso agora, o que eu faço simplesmente? Eu tenho uma variável prompt, que eu dou um registry.getPrompt e passo o id do meu prompt.

02:31

Na hora que eu fizer isso, o que eu vou fazer aqui no final das contas? Eu vou utilizar um cara chamado loadPrompt, que nesse caso está aqui no meu langChain. E esse meu loadPrompt, o que ele vai fazer? Ele vai pegar o caminho do meu prompt,

02:52

que está em EML, ele vai conseguir parciar esse caminho e, no final das contas, ele vai gerar o quê pra gente? O nosso querido prompt template. Ou seja, eu tenho o meu template do tipo do lang chain que a gente precisa, bonitinho, pra eu conseguir trabalhar. E agora, o que eu posso fazer? Tenho o meu LLM,

03:13

onde eu inicio, carrego aqui, nesse caso eu estou utilizando o GPT4 ou poderia estar com o GPT5, o GPT6 não interessa, é somente um modelo de exemplo. E agora, o que eu fiz aqui? Eu simplesmente fiz um chain, ou seja, eu peguei o meu prompt template, chamando LLM e depois gerando isso aí parciado como um output.

03:36

E aí, com isso, o que eu fiz? Estou dando um invoke e aqui eu estou transformando, na realidade, aquele meu modelo num dicionário, onde todas essas minhas variáveis aqui de request vão ser passadas aqui e invocadas pela minha LLM. E aqui eu vou ter o meu resultado. Então, basicamente, vamos rodar, vou dar um Python, a src, agent, code reviewer, vou dar um enter aqui para mim,

04:06

E agora sim, ele vai chamar a minha LLM. Então, nesse caso aqui, eu estou realmente rodando o script, chamando a minha LLM e tudo de boas, mas aqui utilizando aquele meu template. Legal? Então, ele foi, pegou o registry, pegou o caminho do meu registro, o que depois ele fez? Ele carregou, aí baseado nas variáveis que eu acabei passando na minha request, ele simplesmente processou e mandou para a gente conseguir trabalhar.

04:34

Beleza? Então aqui a gente tem o meu resultado da minha Code Review.

## Resumo IA

**Abreviações**  
- **YAML**: *YAML Ain't Markup Language* — formato de serialização de dados legível para humanos, usado para arquivos de configuração e definição de prompts.  
- **LLM**: *Large Language Model* — modelo de linguagem de grande porte, usado para gerar respostas a partir de prompts.  
- **API**: *Application Programming Interface* — interface de programação que expõe funções e estruturas de acesso a um recurso ou serviço.  
- **LangChain**: biblioteca/framework para orquestrar aplicações com LLMs, incluindo prompts, chains e parsers.  
- **GPT**: *Generative Pre-trained Transformer* — família de modelos de linguagem generativa da OpenAI.  

**Resumo**  
A aula mostrou como transformar o registry de prompts em uma dependência real de execução da aplicação. O arquivo `prompt_registry.py` foi apresentado como a camada responsável por centralizar o acesso ao `registry.yaml`, evitando que o restante do código precise conhecer caminhos físicos, leitura de metadados ou detalhes da estrutura da pasta de prompts. Com isso, a aplicação passa a consultar o prompt por identificador, por exemplo via `registry.getPrompt(id)`, criando uma fronteira clara entre o código executável e os artefatos versionados.

Em seguida, o instrutor explicou a importância de modelar os dados de entrada do prompt com uma estrutura tipada, como uma `dataclass`. Esse request reúne todos os campos necessários para a execução, como `diff`, `language`, `rules`, `security_level` e `review_focus`, funcionando como contrato entre a aplicação e o prompt. A ideia é reduzir o uso de dicionários soltos, melhorar a legibilidade e diminuir erros por campos ausentes ou nomes inconsistentes. O mesmo raciocínio foi estendido à saída da LLM: quanto mais o prompt influencia o comportamento do software, mais importante se torna tratar entrada e saída como dados de aplicação.

Depois, foi detalhado o papel de `loadPrompt`, que faz a ponte entre o YAML versionado e um `PromptTemplate` compatível com LangChain. A função recebe o caminho do prompt, faz o parse do arquivo e devolve um template pronto para interpolar as variáveis declaradas no prompt. Isso elimina a montagem manual do template em código e mantém o prompt como artefato externo, carregado em runtime. Se houver problema no arquivo ou incompatibilidade com o contrato esperado, a falha aparece já no carregamento, facilitando o diagnóstico.

Na sequência, o fluxo de execução foi organizado como um chain com três etapas: template, modelo e parser de saída. Primeiro, o `PromptTemplate` recebe os valores concretos do request; depois, a LLM executa a inferência; por fim, o parser converte a resposta para um formato consumível pela aplicação. O instrutor destacou que essa composição deixa explícita a responsabilidade de cada etapa: o prompt monta a instrução, a LLM gera a resposta e o parser trata o resultado. Em cenários mais controlados, esse parser pode ser usado para estruturar melhor a saída, não apenas devolver texto cru.

Também foi mostrado como a chamada `invoke` exige que as variáveis sejam entregues no formato esperado pela biblioteca, normalmente um dicionário chave-valor. Por isso, o objeto tipado do request é convertido antes da execução, mantendo a ergonomia de modelagem no código e a compatibilidade com a interface do chain. O exemplo de uso no agente de Code Reviewer destacou que o campo central do request é o `diff`, já que a revisão depende do trecho alterado, enquanto os demais atributos refinam o comportamento da análise. O fluxo final executado foi: localizar o prompt no registry, obter o caminho, carregar o YAML como template, instanciar a LLM, montar o chain e chamar `invoke` com os dados do request. O resultado é uma pipeline reproduzível de code review, com prompt versionado fora do código e carregado dinamicamente em tempo de execução.

**Pontos de atenção**  
- Centralizar o acesso aos prompts no registry para evitar acoplamento com caminhos físicos e detalhes da pasta.  
- Manter o prompt como artefato versionado e carregá-lo em runtime, em vez de colá-lo no código-fonte.  
- Modelar a entrada do prompt com uma estrutura tipada, como `dataclass`, para evitar dicionários soltos e inconsistências de nomes.  
- Garantir que os nomes dos atributos do request coincidam exatamente com os placeholders do template.  
- Tratar `diff`, linguagem, regras, nível de segurança e foco da revisão como partes do contrato funcional do prompt, não como detalhes opcionais.  
- Validar o YAML e o contrato do template no carregamento, para que erros apareçam cedo e sejam mais fáceis de diagnosticar.  
- Converter o objeto tipado para o formato esperado por `invoke` antes da chamada da LLM.  
- Separar claramente as responsabilidades do chain: template monta a instrução, LLM gera a resposta, parser trata a saída.  
- Considerar o parser como ponto de evolução para saídas estruturadas, e não apenas como retorno de texto simples.  
- No fluxo de Code Review, dar atenção especial ao `diff`, pois ele é a base da análise da LLM.