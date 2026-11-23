Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16697)

## Resumo da aula

A análise em nível de componente desce uma camada em relação ao relatório arquitetural: em vez de mapear a forma geral do sistema, ela explica como cada componente funciona por dentro. O ponto de partida continua sendo a lista de componentes já identificada anteriormente, mas agora cada item vira alvo de um prompt especializado e de um relatório próprio. Essa mudança de granularidade permite sair de “quais partes existem” para “quais regras, fluxos e integrações cada parte executa”.

Um agente de análise de componentes precisa ler código, mas também inferir comportamento funcional e de negócio a partir da implementação. Por isso, o escopo inclui extração de regras de negócio, lógicas de validação, use cases, regras de domínio, algoritmos e data flow. O resultado esperado não é apenas um inventário técnico do diretório, e sim uma compreensão operacional do componente como unidade funcional do sistema.

Retomando o mapeamento arquitetural, a leitura seletiva continua válida, mas o recorte menor permite ser mais agressivo na inspeção dos arquivos daquele componente. Como o volume de código é menor do que o projeto inteiro, o prompt pode exigir cobertura mais profunda de implementações, interfaces, testes, configurações, fixtures, mocks, imports e declarações. Esse ajuste melhora a densidade do diagnóstico sem tentar ler toda a codebase com o mesmo nível de detalhe.

Nem todo componente tem o mesmo tamanho ou a mesma coesão interna, então um único prompt por componente nem sempre produz o melhor relatório. Quando um componente é grande demais, o caminho correto é quebrá-lo em subcomponentes e aplicar novos prompts em um nível mais baixo. A análise, portanto, é hierárquica: alto nível para localizar fronteiras, baixo nível para explicar comportamento interno.

Extrair regras de negócio significa identificar decisões que controlam o comportamento do componente, como validações, restrições, critérios de processamento e condições de domínio. Essas regras precisam aparecer separadamente porque um mesmo componente pode concentrar várias decisões relevantes, e um resumo único tende a esconder diferenças importantes entre elas. Uma tabela com tipo da regra, descrição, arquivo e linha transforma lógica implícita em artefato auditável.

Listar regras não basta quando o objetivo é entender a aplicação; cada regra também precisa de uma explicação textual própria. O detalhamento útil inclui nome da regra, visão geral, descrição expandida e um workflow básico do seu funcionamento, para mostrar em que ponto ela entra e quais efeitos produz. Esse formato ajuda a distinguir regra de negócio de simples detalhe de implementação.

O data flow descreve o caminho percorrido por uma solicitação ou dado dentro do componente, desde a entrada até a resposta ou efeito colateral. Um fluxo como controller -> validação -> processamento -> Stripe -> banco -> mensageria -> Response Builder mostra ordem, dependências e pontos de decisão sem exigir leitura direta do código. Esse mapa é valioso porque revela onde a lógica realmente acontece e onde estão os acoplamentos mais sensíveis.

A análise profunda do componente precisa distinguir dependências internas, dependências externas e integrações efetivas, porque esses grupos têm impactos diferentes na evolução do sistema. Dependências internas mostram como o componente se organiza; externas revelam sensibilidade a outros módulos; integrações expõem contato com serviços, APIs ou infraestrutura. Coesão, acoplamento, relações aferentes e eferentes e limites arquiteturais entram aqui como critérios para julgar se o componente está bem delimitado ou se acumula responsabilidades demais.

Endpoints só devem aparecer quando o componente realmente os expõe. O prompt precisa deixar isso explícito para evitar seções inventadas e para adaptar o formato ao tipo de interface, como REST, GraphQL ou gRPC. Quando o endpoint é REST, uma estrutura com rota, método e descrição já fornece um inventário operacional suficiente para conectar interface externa e lógica interna.

A cobertura de testes do componente não é apenas uma contagem de arquivos de teste; ela indica quais comportamentos críticos estão protegidos e quais áreas permanecem frágeis. Quando essa leitura é combinada com tratamento de erro, segurança, resiliência, dívidas técnicas e code smells, o relatório deixa de ser descritivo e passa a apontar risco operacional real. Isso é especialmente útil para priorizar investigação ou modernização sem misturar diagnóstico com refatoração imediata.

Os inputs do prompt incluem o componente, seus diretórios e os caminhos já identificados no relatório arquitetural, além de artefatos como implementações, interfaces, documentação, testes e configurações. O output precisa consolidar sumário executivo, fluxo de dados, regras de negócio, dependências, endpoints, integrações, patterns, riscos e testes em um relatório estruturado. Retomando o uso de critérios, ambiguidades, instruções negativas e tratamento de erro já definidos antes, o diferencial aqui é aplicar essas peças para produzir um retrato profundo e específico de cada componente.

Quando o prompt acumula muitas instruções, um workflow resumido no final funciona como trilho de execução para a IA. Ele não substitui a especificação detalhada, mas reforça a ordem esperada: ler o escopo, mapear estrutura, extrair regras, reconstruir fluxo, identificar dependências, listar endpoints, avaliar testes e salvar o relatório. Em tarefas longas ou densas, esse resumo reduz a chance de o agente ignorar etapas importantes.

## Transcrição

00:01

Bom, pessoal, da mesma forma que a gente fez isso para a arquitetura do sistema, eu quero mostrar novamente o mesmo prompt. Galera, isso aqui é uma disciplina de Prompt Engineering. Eu não posso deixar de falar dos prompts. Eu sei que a gente já entendeu essa estrutura básica, mas eu quero trazer e tentar explicar cada vez mais exemplos que eu puder.

00:23

para que você consiga otimizar o seu tempo e ter até um pouco mais de insights para você fazer os seus próprios agentes, seus próprios prompts aqui, tá? Então, somente para você entender, novamente, o cara Persona e Scopo é basicamente a mesma coisa, onde ele faz análise de código e aqui também, inclusive, lógicas de negócio, extração de lógicas de negócio.

00:47

perceba bem o que eu coloquei aqui, extração de lógicas de negócio. Então, o objetivo dele é fazer uma compreensão em nível de componente, porque antes a gente teve uma compreensão em nível de arquitetura geral do sistema, e naquele documento nós tivemos a listagem dos componentes do sistema. Então, a nossa ideia aqui é que esse prompt pegue cada componente

01:14

que existe listado naquele relatório de arquitetura e gere um relatório específico para cada componente. Então, aqui o que eu estou pedindo? Mapear completamente a estrutura e a organização desses componentes.

01:30

extrair os documentos e todas as regras de negócio, lógicas de validação, use cases e regras de domínio, analisar implementações, algoritmos e data flow, ou seja, o fluxo de dados daquele componente, identificar as dependências internas e externas e as integrações,

01:55

documentar e entender os design patterns, as decisões arquiteturais e os atributos de qualidade. Isso aqui, no final das contas, é o que define, inclusive, o que é a arquitetura. E entender o acoplamento de cada componente, a coesão e os seus limites arquiteturais.

02:14

entender pontos de segurança, como que ele está vendo erros, padrões de resiliência, identificar dívidas técnicas e codes MELs aqui pra gente, tá? Então, esse é o objetivo principal. Se você perceber, agora eu estou sendo um pouco mais detalhista em relação ao que ele vai ler na quantidade de arquivos. Provavelmente, ele vai

02:38

Como eu estou analisando especificamente um componente apenas, eu posso ser mais preciso e falar para ele ser um pouco mais agressivo na leitura dos arquivos que estão dentro desse componente, porque, com certeza, são menos arquivos do que tem no projeto como um todo, como a gente fez na arquitetura. Mas, novamente, depende do nível que você quer olhar. Por exemplo, se você tem na sua empresa um componente muito grande, provavelmente você poderia rodar um...

03:06

um outro prompt ou uma outra chamada para ele gerar subcomponentes para você ter um relatório mais preciso do que isso acontece. Então, você pode ir do alto nível e ir baixando nível, e cada nível que você vai baixando, você pode ter um prompt diferente. Tudo isso vai depender do tamanho do projeto. Novamente, não tem uma regra geral que vai funcionar para todo mundo, tá? Então, provavelmente, esse prompt que eu estou utilizando aqui para você, dependendo da situação,

03:31

não pode trazer tanta informação da forma como você queria. Ou, às vezes, pode trazer até mais informação do que você gostaria. Por isso que é importante você ter autonomia para você conseguir trabalhar nos seus prompts e não ficar dependendo, obviamente, somente dos prompts que eu trago aqui no curso para você. Legal?

03:47

E aqui são os inputs. O input é o componente, os serviços, os diretórios onde estão identificados no report de arquitetura, porque lá tem os caminhos, os arquivos e as implementações, as interfaces, os testes, as documentações, os arquivos de configuração, os arquivos de testes, desde fixtures, desde mocks,

04:08

dependências, declarações, os imports, e opcional, ele pode olhar o arquivo de arquitetura e ver quais são os componentes mais críticos, para entender um pouco melhor, e outras análises que o usuário pode trazer. Outros pontos, output, novamente, é aquela parte que dá trabalho. Então, sumar executivo, a data flow, ou seja, como que esse componente funciona em relação a passo a passo. Então, receber um

04:37

uma solicitação num controller, foi para uma validação, caiu na regra de negócios da parte de processamento, chamou o Stripe, depois persistiu no banco de dados, mandou uma mensagem e retornou ali para um Response Builder, por exemplo. Entendeu? Então, a ideia é somente para a gente ter uma ideia de como o fluxo dos dados acontece dentro daquele componente. Outra coisa que eu pedi aqui para ele é para ele extrair as regras de negócio de forma quebrada

05:05

para cada regra de negócio que ele encontrar no sistema. Por que isso é importante? Porque, às vezes, quando eu vou ver um componente, cada componente tem sua regra de negócio. E um componente pode ter diversas regras de negócio. Então, para eu fazer análise e entender um pouco melhor a aplicação que eu estou analisando, provavelmente ter uma ideia de um resumo básico das regras de negócio que aquele componente faz acaba sendo relevante, pelo menos na minha opinião. Aí vai depender de cada um. Então, a minha ideia aqui foi

05:34

o overview das regras de negócio. Então, basicamente, o que eu trouxe, eu criei uma tabelinha Markdown falando qual o tipo de regra, por exemplo, uma validação, qual que é uma descrição dessa regra, por exemplo, o pagamento mínimo tem que ser de um dólar e aonde está esse arquivo e a linha dessa regra de negócio.

05:51

E eu fiz isso, tá? E, depois disso, eu pedi, inclusive, para ele gerar aqui para mim um detalhamento de cada regra de negócio. Então, eu coloquei regra de negócio, o nome da regra, uma visão geral da regra de negócio, a descrição mais detalhada dessa regra de negócio, e pedi para ele trazer um workflow básico de como que funciona essa regra de negócio.

06:13

Então, perceba, galera, que eu estou usando aqui XML, ou uma forma como se fosse um placeholder, para ele entender que aqui é onde ele vai escrever, porque eu estou colocando uma definição em markdown aqui para ele, então ele pode confundir. Então, eu tento deixar isso da forma mais clara possível ali para a gente. E, na descrição, eu estou falando, olha...

06:34

Use pelo menos três parágrafos, traga o máximo de detalhes possível, de uma forma fácil de entender como que as regras de negócio funcionam para cada componente. E aqui eu pedi para ele trazer também a estrutura de componentes, análise de dependências, parecido como a gente fez, mas agora de mais baixo nível.

06:52

componentes aferentes e referentes, como eu tinha falado, os endpoints, caso existam endpoints. Nem todo componente tem endpoints, mas se esse componente tiver um endpoint, ele vai trazer. E eu falei que um endpoint pode ser considerado, por exemplo, um REST, um GraphQL, pode ser um gRPC, e...

07:10

Se esse componente não expor nenhum endpoint, não inclui essa sessão. E eu coloquei aqui uma regra mais específica. Se o componente for REST, use o formato abaixo. E daí eu coloquei endpoint, o método e a descrição ali pra gente. Depois, pedir pra ele trazer o ponto de integração, os patterns que estão sendo utilizados, os riscos técnicos, análise de cobertura de testes, pedir pra ele salvar o report,

07:33

e fiz o final step e trouxe novamente outros critérios que eu acabo entendendo que são importantes para ele decidir e trabalhar ali pra gente, tá? Também análise de ambiguidades, instruções negativas, como ele trabalha com o erro, e novamente aqui, galera, olha só, workflow, que é como se fosse um resumo de tudo que eu coloquei lá em cima,

07:55

para que a IA possa seguir esse passo a passo. Então, esse Workflow é um resumo. Ele é interessante muitas vezes quando você tem muita informação e muita instrução. Eu gosto de colocar esse Workflow. Se você olhar aqui no formato de Prompts, eu não estou colocando aqui o Workflow, mas eu vou até adicionar, eu vou deixar como opcional o Workflow.

08:16

opcional, porque vai depender do tipo de tarefa que você vai fazer. Se ela é muito complexa, se ela é muito longa ou coisas desse tipo, você pode colocar um workflow ou não. Então, galera, isso aqui foi mais um exemplo de como eu utilizei esse tipo de prompt para ele fazer uma análise interna de componentes de uma aplicação. Fechou? Daqui para frente, a gente vai ver outros tipos de componentes que vão ser importantes para a gente também.

## Resumo IA

**Abreviações**

- **IA** — Inteligência Artificial
- **REST** — Representational State Transfer
- **GraphQL** — Graph Query Language
- **gRPC** — Google Remote Procedure Call
- **XML** — Extensible Markup Language
- **Markdown** — linguagem de marcação para formatação de texto

**Resumo**

A aula apresentou um prompt voltado para análise em nível de componente, aprofundando o trabalho que antes havia sido feito em nível de arquitetura do sistema. A ideia central é usar a lista de componentes já identificada no relatório arquitetural como ponto de partida para gerar, para cada item, um relatório próprio e mais detalhado, capaz de explicar não só a estrutura interna, mas também o comportamento funcional e de negócio daquele componente.

O instrutor destacou que o agente de análise precisa ir além da leitura de código, inferindo regras de negócio, lógicas de validação, use cases, regras de domínio, algoritmos e fluxo de dados. Com isso, o resultado deixa de ser um inventário técnico de arquivos e passa a ser uma compreensão operacional do componente como unidade funcional. A análise é apresentada como hierárquica: primeiro se localizam fronteiras em alto nível e, quando necessário, o componente é quebrado em subcomponentes para uma leitura ainda mais profunda.

Também foram detalhados os principais itens de entrada do prompt, como o componente, seus diretórios, caminhos já identificados no relatório de arquitetura e artefatos como implementações, interfaces, testes, documentações, configurações, fixtures, mocks, imports e declarações. Do lado da saída, o relatório deve consolidar sumário executivo, fluxo de dados, regras de negócio, dependências, endpoints, integrações, design patterns, riscos e cobertura de testes.

A aula explicou ainda como estruturar a extração das regras de negócio, recomendando separá-las em uma tabela com tipo, descrição, arquivo e linha, e depois detalhá-las individualmente com nome, visão geral, descrição expandida e workflow básico. O instrutor reforçou a importância de explicitar o data flow do componente, mostrando o caminho percorrido por uma solicitação desde a entrada, passando por validação, processamento, integrações externas, persistência e retorno.

Outro ponto abordado foi a diferenciação entre dependências internas, externas e integrações efetivas, além da análise de coesão, acoplamento e limites arquiteturais. O prompt também prevê tratamento condicional para endpoints: eles só devem aparecer se realmente existirem, e, no caso de REST, podem ser descritos por rota, método e descrição. Por fim, a aula enfatizou o uso de um workflow resumido no final do prompt como guia de execução para a IA, especialmente útil quando há muitas instruções e o processo é longo ou complexo.

**Pontos de atenção**

- A análise em nível de componente deve ser mais profunda que a análise arquitetural, mas sem perder o vínculo com os componentes já mapeados anteriormente.
- Nem todo componente tem o mesmo tamanho ou a mesma coesão; em casos grandes, pode ser necessário dividir em subcomponentes e rodar novos prompts.
- O prompt deve incentivar a leitura agressiva dos arquivos do componente, aproveitando que o escopo é menor que o do projeto inteiro.
- Regras de negócio não devem ser tratadas como um bloco único; o ideal é separá-las por tipo e detalhá-las individualmente.
- O data flow é essencial para entender onde a lógica realmente acontece e quais são os pontos de acoplamento mais sensíveis.
- É importante distinguir dependências internas, dependências externas e integrações reais, pois cada uma impacta o sistema de forma diferente.
- Endpoints só devem ser listados quando o componente realmente os expõe; se não houver endpoints, essa seção deve ser omitida.
- A estrutura de saída precisa ser adaptável ao tipo de interface do componente, como REST, GraphQL ou gRPC.
- A cobertura de testes não deve ser vista apenas como contagem de arquivos, mas como indicação de comportamentos críticos protegidos.
- Segurança, tratamento de erros, resiliência, dívidas técnicas e code smells devem ser considerados como riscos operacionais, não apenas como observações técnicas.
- O uso de placeholders ou marcação bem clara evita confusão entre instruções do prompt e campos que a IA deve preencher.
- Um workflow resumido no final ajuda a IA a seguir a ordem correta das etapas, especialmente quando o prompt contém muitas instruções.
- O instrutor reforçou que não existe um prompt universal: é preciso ajustar o nível de detalhe conforme o tamanho do projeto e o objetivo da análise.