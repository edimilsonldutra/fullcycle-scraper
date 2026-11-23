Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17791)

## Resumo da aula

Uma integração entre features precisa ser tratada como um contrato explícito entre quem provê e quem consome dados. No exemplo, Video Upload Feature provê path e metadados, enquanto Background Processing Feature consome essas saídas para continuar o fluxo. Esse contrato importa porque a ligação entre features não pode ficar implícita em código disperso ou apenas no entendimento da equipe. Quando o contrato fica visível, a dependência entre as partes deixa de ser informal e passa a orientar implementação e validação.

O grafo de dependências surge diretamente da relação entre provides e consumes. Se Video Upload expõe um file path e a feature de background usa esse file path, então Background Processing depende de Video Upload. Essa leitura do grafo não é conceitual apenas: ela mostra quais features precisam conversar corretamente para que o sistema funcione. Retomando o cenário de upload de vídeo, o consumidor revela onde existe acoplamento funcional entre duas partes do produto.

A regra central é simples: toda feature que consome algo de outra precisa de um teste que comprove esse handoff. O teste não valida só a existência do dado; ele valida que o dado realmente sai da feature provedora e chega ao destino esperado na feature consumidora. Por isso, os testes de integração entre features são derivados dos consumes, e não apenas da lista de componentes existentes. O consumidor é o sinal de que existe uma fronteira que precisa ser verificada.

Quando Background Processing consome os dados produzidos por Video Upload, esse consumo vira critério de aceitação da integração. Um exemplo direto é um teste E2E como The Video Uploaded Actually Reaches the Processing Pipeline. Esse tipo de teste confirma que o vídeo enviado realmente alcança a pipeline de processamento, em vez de parar em algum ponto intermediário. O valor do teste está em provar o fluxo completo entre origem e destino, não apenas chamadas isoladas.

Sempre que uma feature for conectada a outra, identifique primeiro quem consome e depois exija um teste que garanta a comunicação entre elas. Essa regra parece óbvia, mas costuma ser esquecida quando o time está escrevendo PRD, documentação ou frameworks de suporte. O resultado desse esquecimento é uma arquitetura que aparenta estar integrada, mas falha justamente nos pontos de passagem entre features. Formalizar essa regra reduz incerteza e aumenta a confiança de que as features realmente estão se falando.

## Transcrição

00:00

Agora que você entendeu o básico, vamos dizer assim,

00:04

de como que essas gerações, essas áreas são geradas,

00:07

principalmente com essas integrações, eu tenho mais um exemplo aqui,

00:11

que é o contrato entre as features,

00:13

que é aquilo que eu estava falando para você,

00:15

mas eu resolvi dar um exemplo um pouco mais claro para

00:19

ficar um pouquinho mais fácil de você conseguir entender. Então, olha só.

00:24

Depois eu leio o texto ali.

00:27

Eu tenho uma feature, por exemplo, de upload.

00:30

Tá? Video Upload Feature. O que ela provê?

00:33

Ela provê o path e os metadados para alguém.

00:38

Beleza? Eu tenho uma outra feature chamada Background Processing Feature,

00:43

que ela vai fazer o quê?

00:45

Ela vai consumir o upload, vídeo, file, metadata que essa feature fez.

00:51

Ok? E com isso, eu tenho a geração do meu grafo da seguinte forma.

00:57

Eu estou falando que o Processing... has a dependencies on video upload.

01:03

Em cross-feature de integration test,

01:05

eu tenho que o upload do vídeo

01:07

atualmente tem que alcançar a pipeline de processamento.

01:14

Então, essa que é a ideia importante,

01:17

porque quando eu tenho duas features, elas se integram,

01:21

eu tenho como a dependência é gerada e eu tenho como que eu testo essa integração. Então,

01:28

eu tenho o teste de integração entre features e eu tenho a dependência

01:32

que eu tenho que estar ciente que essas features se integram.

01:35

Então, é basicamente isso que eu acabei de falar. Dentro da feature video upload,

01:39

tem um provides que vai retornar o file path.

01:41

A feature background vai consumir o file path.

01:44

Isso é exatamente o grafo de dependências.

01:47

Os testes de integração são criados a partir dos consumes.

01:50

Pelo fato do processing...

01:54

do cara que vai processar, nessa fase de processar,

01:56

vai consumir os dados do video upload e vai entrar como critério de aceitação.

02:01

E esses critérios podem ser um teste E2E,

02:04

que é o The Video Uploaded Actually Reaches the Processing Pipeline.

02:08

Então, esse teste garante o handoff entre duas features. Logo,

02:14

todo consumidor acaba criando um teste desse tipo.

02:18

Então, qual que é a regra que eu estou estabelecendo aqui no meu racional?

02:24

que qualquer cara, qualquer feature que consome algo,

02:28

precisa de um teste garantindo que

02:33

ela consegue chegar até o destino final.

02:38

Ok? Então, isso é importante. Então, eu preciso ter esse racional.

02:43

Se tudo que consome vai criar um teste de integração,

02:48

isso vai me ajudar...

02:50

a me dar mais tranquilidade de que as minhas features estão falando. Então,

02:54

esse tipo de contrato é importante para que a gente tenha esse racional. Então,

03:00

se eu tivesse que gerar em traços uma regra na sua cabeça agora,

03:03

seria toda vez que eu quero grudar uma feature na outra,

03:07

eu vejo qual feature que consome a outra e falo

03:10

que eu tenho que ter um teste para garantir...

03:13

que essa feature está conseguindo conversar com outra que ela consome,

03:16

Que é algo óbvio, né?

03:18

Mas na hora de a gente criar um PRD,

03:20

um documento, um framework ou qualquer coisa desse tipo,

03:22

às vezes isso fica para trás e aí que as coisas acabam não se encaixando mais,

03:28

Tá? Então esse aí é um ponto, tá?

03:31

E aqui está um exemplo do projeto atual

03:36

que eu vou mostrar para vocês no próximo vídeo.

## Resumo IA

**Abreviações**
*   **E2E**: End-to-End (De ponta a ponta)
*   **PRD**: Product Requirements Document (Documento de Requisitos de Produto)

**Resumo**
A aula enfatiza a necessidade de tratar a integração entre features como um contrato explícito entre quem provê e quem consome dados, evitando ligações implícitas em código ou no entendimento da equipe. O objetivo é estabelecer que a visibilidade desse contrato orienta a implementação e a validação, gerando um grafo de dependências claro. Utilizando o exemplo de uma "Video Upload Feature" que provê um path e metadados, e uma "Background Processing Feature" que os consome, o instrutor demonstra como essa relação cria uma dependência direta. O conceito central é que toda feature que consome dados de outra deve ter um teste de integração que comprove o "handoff" (a passagem dos dados). Esses testes, derivados dos "consumes", validam não apenas a existência, mas a chegada efetiva dos dados ao destino, garantindo o fluxo completo entre as features. Um teste E2E como "The Video Uploaded Actually Reaches the Processing Pipeline" é apresentado como exemplo de critério de aceitação, provando a comunicação integral.

**Pontos de atenção**
*   A integração entre features deve ser tratada como um **contrato explícito**, e não como algo implícito em código disperso ou no entendimento da equipe.
*   A visibilidade do contrato de integração transforma as dependências informais em guias claros para implementação e validação.
*   O **grafo de dependências** surge diretamente da relação entre quem "provê" e quem "consome" dados.
*   **Toda feature que consome algo de outra precisa de um teste** que comprove o "handoff" (a passagem de dados) entre elas.
*   Os testes de integração devem validar não apenas a existência do dado, mas que ele **realmente sai da feature provedora e chega ao destino esperado** na feature consumidora, provando o fluxo completo.
*   Os testes de integração são derivados dos "consumes", pois o consumidor é o indicador de uma fronteira que exige verificação.
*   A regra de identificar o consumidor e exigir um teste para garantir a comunicação é crucial, mas **frequentemente esquecida** durante a criação de PRDs, documentação ou frameworks de suporte.
*   O esquecimento dessa regra resulta em arquiteturas que aparentam estar integradas, mas falham justamente nos pontos de passagem entre features.
*   Formalizar a exigência de testes para cada ponto de consumo **reduz a incerteza e aumenta a confiança** de que as features realmente estão se comunicando de forma eficaz.