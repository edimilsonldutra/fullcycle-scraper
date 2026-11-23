Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16581)

## Resumo da aula

Retomando o loop Thought/Action/Observation já definido anteriormente, o ganho aqui está em transformá-lo em um prompt de depuração operacional. O prompt precisa fixar o papel do modelo como desenvolvedor back-end Go, delimitar o alvo do debug — o handler POST /products — e exigir uma saída em etapas até chegar a uma recomendação final de correção. Essa estrutura evita respostas genéricas porque força o modelo a inspecionar o fluxo real do código: decode do body, preparação da query, execução no banco e resposta HTTP.

Em debugging com IA, a restrição mais importante é impedir que o modelo use evidências que não existem no contexto. A instrução “do not fabricate information that is not provided in the context” reduz o risco de o raciocínio se apoiar em logs, traces ou comportamentos não fornecidos, o que contaminaria todo o diagnóstico. No caso de handlers com erro 500, isso é decisivo porque o modelo tende a inventar mensagens de erro plausíveis; ao proibir explicitamente logs inexistentes, o diagnóstico precisa se sustentar apenas no código disponível.

O handler apresentado recebe a requisição, faz o decode do JSON para uma struct Product, prepara um INSERT, executa a operação no banco e retorna HTTP 201 Created quando tudo funciona. Cada uma dessas etapas é um ponto potencial de falha, mas nem todas explicam um erro 500 recorrente. O raciocínio útil começa eliminando causas incompatíveis com o sintoma observado, como erro de parsing do body, que normalmente produziria 400 em vez de 500.

A primeira checagem relevante é separar falhas de entrada de falhas internas do servidor. Se o decode do JSON já retorna Bad Request quando o payload é inválido, essa etapa deixa de ser a principal suspeita para um 500 consistente. Esse filtro é valioso porque reduz o espaço de busca e desloca a investigação para a camada de persistência, onde erros de preparação ou execução de query são mais compatíveis com o sintoma.

O bug está no desalinhamento entre a struct Go e o tipo esperado pelo banco de dados para price. Quando price é declarado como string, mas o INSERT e o schema esperam um valor numérico como float64 ou decimal, a chamada de execução pode falhar por incompatibilidade de tipo. Esse é um erro típico de integração entre aplicação e banco: o código compila, o fluxo parece correto, mas a persistência quebra no momento em que os valores concretos são enviados.

A correção consiste em alterar price na struct Product de string para float64, alinhando o tipo da aplicação ao tipo esperado na persistência. Isso faz o decode do JSON produzir um valor numérico já compatível com a execução da query, em vez de empurrar uma string para uma coluna numérica. Se o banco usar precisão monetária mais rígida, outra alternativa seria modelar explicitamente um tipo compatível com a estratégia financeira adotada, mas o ponto central aqui é eliminar o mismatch.

A utilidade do ReAct não está apenas em acertar a resposta final, mas em mostrar por que certas hipóteses foram descartadas e por que outra se tornou mais provável. Quando a sequência passa por decode, preparação de statement e revisão dos argumentos do Exec, o desenvolvedor consegue auditar a trilha de decisão em vez de aceitar um palpite isolado. Isso torna a técnica especialmente útil para bugs de backend em que a causa real está em uma nuance de contrato entre camadas.

Ferramentas de IDE já ajudam a detectar erros, mas um prompt específico de debugging permite orientar a investigação segundo o contexto exato do problema. Ao informar endpoint, sintoma, trecho de código e restrições de evidência, o desenvolvedor controla melhor o tipo de análise produzida e consegue reutilizar esse padrão em outros bugs semelhantes. O valor prático está em transformar a IA em um apoio de depuração guiada, e não em um gerador de suposições soltas.

## Transcrição

00:01

Bom pessoal, seguinte, agora chegamos aqui com código na parte do React, tá? E isso aqui espero que seja já um prompt e algo que consiga te ajudar a corrigir bugs hoje. Obviamente é um prompt que ele não está totalmente

00:17

ajustado, porque é um exemplo, mas eu quero que isso possa abrir a sua mente hoje para você, talvez, ajudar a resolver problemas no dia a dia, tá? Então, um exemplo claro aqui de React para você, tá? Então, você é um desenvolvedor back-end Go, que está debugando uma API REST. Use o estilo de reasoning de React, alternando entre Thought, ou seja, a sua linha de pensamento, Action, um passo concreto que você tem que fazer ou checar,

00:46

ou que você tem que executar, e a cada ação escreva uma observação do que você conseguiu capturar com aquela ação que você fez. No final, conclua uma final answer com a sua recomendação de correção do código. Aí eu coloquei uma observação aqui para tentar evitar delírio, porque às vezes ela vai delirar mesmo, alucinar, e eu coloquei assim, do not fabricate an information that is not provided in the context, exemplo,

01:14

Se o contexto não está provendo logs, não use error logs na sua linha de pensamento. Aí eu coloquei aqui a context. Usuário reportou que no endpoint post barra products sempre está retornando erro 500.

01:32

Aqui está o código do handler do barra product. Isso aqui está em Go, galera. Você não precisa ser programador Go para entender. Mas, na realidade, aqui tem uma função que recebe um request, um response, ele pega um produto, transforma em JSON, insere no banco de dados, prepara para inserir no banco de dados, insere e executa no banco de dados e retorna um HTTP created, ou seja, um HTTP ali para mim.

01:59

E embaixo ele tem a struct, ou seja, a estrutura desse product aqui pra gente, onde ele traz pra mim id, nome, description, price e stock. Então, o que eu quero fazer é conseguir identificar aonde que tá o bug desse cara aqui.

02:17

pensando claramente passo a passo com as validações que ele pode fazer. Então, o que eu vou fazer? Eu vou executar aqui react e vamos ver o que vai rolar aqui nesse caso. E depois a gente pode trocar de modelo, dependendo se a resposta foi ruim ou não, ou qualquer coisa desse tipo, tá? Bom, tivemos a nossa primeira resposta aqui e vamos ver o que vai acontecer. Então, a linha de pensamento dele foi

02:41

O endpoint post-products está retornando o erro 500, o que indica que tem um internal server error. A causa comum para isso inclui problemas de operações no banco de dados ou condições inesperadas no servidor. A função de handler tenta fazer o decode do body, que ele vai transformar em JSON, preparar o SQL statement e executar isso. Vamos analisar cada passo. Ação.

03:07

Se ficasse o JSON decoding, pode estar causando um problema o erro que vai gerar, por exemplo, para um erro 400 e não 500. Observação, o JSON decoding step está correto retornando 400 para bad request, então isso não está causando o erro 500.

03:24

Ele gerou uma outra observação. Pensamento. O problema pode ser com a interação com o banco de dados especificamente em preparação à execução do SQL Query. Ação. Checar o SQL Statement Preparation para erros no Error Handler. Observação.

03:40

Aí ele colocou, se o prepare fails, os logs podem indicar que dá um fatal error, o que pode dar um crash no programa, isso não é ideal e pode contribuir para um erro 500. Mas isso não explica a consistência do HTTP 500 que fica rodando o tempo inteiro no servidor.

04:02

Aí, pensamento. Investigar o statement exec. Essa chamada pode estar falhando, causando o servidor retornar 500 com o problema do HTTP call, chamado aqui. Ação. Revisar os tipos e os valores passados no exec, garantindo que eles estão alinhados com o esquema do banco de dados. Observação. O product struct define price como uma string, mas o statement

04:31

normalmente está esperando o price como um float64 ou um decimal, matching the data, fazendo o match com o banco de dados. Então, o tipo, que é mismatched, normalmente pode causar uma execução no banco de dados. Pensamento. Convertendo, então, o price para o tipo correto pode resolver o problema. Ação. Modificar o produto

05:00

a struct product, mudando o price de string para float, garantindo que o decoding do JSON consiga fazer corretamente e ajustando o statement exec para esse tipo de formato.

05:16

Observação. Depois de mudar o price, o tipo do price, e testar novamente o endpoint, ele pode não mais retornar erros 500. Então, a final answer é mudar o tipo do campo de price que está em product de string para float64, alinhando com uma provável causa de quebra de expectativas e mismatch no banco de dados durante a execução.

05:46

Galera, você tem noção que com essa linha ele conseguiu resolver o problema, que é exatamente esse. Se você olhar aqui, o meu price está como string, tá? Na hora que eu vou fazer um insert aqui no meu banco de dados, ele está partindo do princípio que isso aqui poderia ser um inteiro ou um float. Então, ele pegou esse tipo de nuance. Vocês sacaram, galera, o poder que esse negócio tem

06:12

para você criar os seus próprios prompts para te ajudar a debugar esses tipos de coisa, ou até mesmo, você usa as suas IDEs, que já fazem esse tipo de verificação de erro e procuram, mas você sendo mais específico, ou você tendo conjuntos de prompts prontos, você consegue ter um controle maior, inclusive, nesse tipo de situação.

06:36

Eu vou quebrar agora esse vídeo para continuar para um outro exemplo que tem de React, que não tem a ver com programação, mas é importante a gente entender também. Beleza?

## Resumo IA

**Abreviações**  
- API: Application Programming Interface  
- REST: Representational State Transfer  
- JSON: JavaScript Object Notation  
- SQL: Structured Query Language  
- HTTP: Hypertext Transfer Protocol  
- 500: Internal Server Error  
- 400: Bad Request  
- 201 Created: código de status HTTP de recurso criado com sucesso  
- Go: linguagem de programação Go  
- ReAct: técnica de raciocínio que alterna entre *Thought* (pensamento), *Action* (ação) e *Observation* (observação)

**Resumo**  
A aula mostrou como transformar o loop ReAct em um prompt de depuração operacional para investigar um bug em uma API REST escrita em Go. O instrutor orientou a definir claramente o papel do modelo como desenvolvedor back-end Go, delimitar o alvo do debug ao endpoint `POST /products` e exigir uma resposta em etapas, com pensamentos, ações e observações, até chegar a uma recomendação final de correção. Também destacou uma restrição essencial: não inventar informações que não estejam no contexto, especialmente logs e erros não fornecidos, para evitar alucinações no diagnóstico.

No exemplo analisado, o handler recebe a requisição, faz o decode do body JSON em uma struct `Product`, prepara um `INSERT`, executa a query no banco e retorna `HTTP 201 Created` quando tudo dá certo. O raciocínio foi conduzido eliminando primeiro hipóteses incompatíveis com o sintoma: se o decode do JSON falha, o comportamento esperado seria `400 Bad Request`, não `500`. A investigação então se concentrou na camada de persistência, onde um erro de preparação ou execução do SQL seria mais compatível com um erro interno recorrente.

A causa encontrada foi um desalinhamento de tipo entre a struct da aplicação e o banco: o campo `price` estava definido como `string`, enquanto a coluna e a query esperavam um valor numérico, como `float64` ou um tipo decimal. Essa incompatibilidade fazia a execução do `INSERT` falhar, embora o código compilasse e o fluxo geral parecesse correto. A correção proposta foi alterar `price` de `string` para `float64` na struct `Product`, alinhando o decode do JSON e os argumentos do `Exec` ao tipo esperado pela persistência. O instrutor reforçou que o valor do ReAct está em tornar explícita a trilha de diagnóstico, ajudando a descartar hipóteses e a focar na causa mais provável com base no contexto real do código.

**Pontos de atenção**  
- Definir o contexto do prompt com precisão: papel do modelo, endpoint, linguagem e objetivo do debug.  
- Proibir explicitamente a fabricação de evidências inexistentes, como logs ou traces não fornecidos.  
- Separar falhas de entrada de falhas internas: erro de JSON inválido tende a gerar `400`, não `500`.  
- Analisar o fluxo real do handler por etapas: decode do body, preparação da query, execução no banco e resposta HTTP.  
- Suspeitar de incompatibilidade de tipos quando o código compila, mas a persistência falha em runtime.  
- Verificar o alinhamento entre a struct da aplicação e o schema do banco, especialmente em campos numéricos como `price`.  
- Não assumir que o problema está no decode se o sintoma é um `500` consistente.  
- Usar ReAct para justificar o descarte de hipóteses, não apenas para obter a resposta final.  
- Modelos de IA ajudam mais quando o prompt é específico e restrito ao contexto do bug.  
- IDEs e prompts de debugging se complementam: a IA pode orientar a análise, mas sem contexto suficiente ela tende a especular.