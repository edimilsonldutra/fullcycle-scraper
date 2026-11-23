Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17057)

## Resumo da aula

Feature Design Doc é o documento que desce do desenho arquitetural para a especificação operacional da feature. O HLD já definiu o terreno da solução; o FDD transforma esse contexto em comportamento detalhado, contratos reais e condições de implementação. Ele não chega ao nível de prescrever código linha por linha, mas também não fica apenas na organização macro do sistema. Seu papel é reduzir a ambiguidade entre arquitetura e execução.

O FDD se justifica quando a feature expõe API, altera contratos, adiciona configuração ou produz efeitos relevantes em segurança, performance e compatibilidade. Nesses casos, a implementação depende de definições que não cabem mais no nível arquitetural, mas ainda precisam ser compartilhadas antes do código. Se a mudança afeta integração entre partes do sistema, comportamento em runtime ou expectativas externas, o documento deixa de ser opcional e passa a ser instrumento de alinhamento técnico.

Um FDD responde como a feature se comporta em tempo de execução, quais interfaces expõe, como é configurada, de quais dependências precisa e como lida com erros, exceções e concorrência. Ele também define como validar que a implementação está correta, o que desloca a discussão de intenção para verificabilidade. Isso torna o documento útil não só para construir, mas para revisar, testar e aceitar a feature com critérios objetivos.

A fronteira do FDD é deliberada: ele detalha o suficiente para orientar implementação sem virar prescrição de padrão de codificação ou detalhe interno de classe. Essa posição intermediária importa porque muitos erros surgem justamente no espaço entre “a arquitetura permite” e “o código realmente faz”. O FDD fecha esse espaço ao explicitar contratos públicos, fluxos, erros e regras operacionais que o HLD apenas sinaliza em alto nível.

Contratos públicos são a parte do documento que define o que outras partes do sistema ou consumidores externos podem esperar da feature. Aqui entram assinaturas, endpoints, headers, exemplos de uso e semântica de resposta, porque integração depende de precisão, não de intenção genérica. Retomando o rate limiter já conhecido, o foco agora deixa de ser a topologia com Redis e middleware e passa a ser o comportamento exato da feature: quais headers ela retorna, em que condição responde 429 e qual contrato expõe para quem integra.

Erros e exceções precisam aparecer como comportamento especificado, não como detalhe deixado para o implementador decidir no meio do desenvolvimento. Fallbacks entram nessa mesma camada porque representam a resposta esperada quando dependências falham ou quando a feature não consegue operar no modo principal. No rate limiter, a decisão arquitetural de fallback open já existe; no FDD, ela precisa virar regra operacional clara, com condições de acionamento e efeito observável no comportamento da feature.

Configuração aparece no FDD no nível em que afeta uso real da feature: quais opções existem, como são fornecidas via código e quais combinações são válidas ou inválidas. Dependências também deixam de ser apenas componentes do desenho e passam a ser requisitos concretos para a feature funcionar, inclusive com impacto em integração e rollout. Compatibilidade precisa ser tratada explicitamente quando a mudança altera contratos, comportamento esperado ou forma de adoção por consumidores já existentes.

Critérios de aceite técnicos são centrais porque transformam o documento em referência verificável, não apenas descritiva. Eles definem as condições sob as quais a feature pode ser considerada correta, cobrindo comportamento, contratos, erros e restrições técnicas relevantes. Sem essa seção, o time até implementa algo plausível; com ela, o time implementa algo testável contra uma definição compartilhada.

Um FDD costuma reunir contexto e motivação técnica, objetivos, escopo e exclusões, fluxos detalhados, diagramas quando necessários, contratos públicos, erros, fallbacks, dependências, compatibilidade, critérios de aceite, riscos e mitigação. Essa composição mostra que o documento não serve apenas para descrever a feature, mas para cercar os pontos que mais geram divergência durante implementação. Observabilidade e riscos podem ser apenas referenciados a partir do que já foi estabelecido antes, desde que o documento deixe claro como essas preocupações afetam a operação específica da feature.

Um FDD bem escrito melhora a implementação assistida por IA porque fornece contexto operacional reutilizável em vez de depender de prompts vagos. Como o documento já explicita contratos, erros, configuração e critérios de aceite, a IA passa a gerar código e testes com menos espaço para interpretação arbitrária. O ganho principal não é “automatizar a feature”, mas reduzir a distância entre o que foi decidido e o que será implementado.

## Transcrição

00:00

Bom pessoal, e agora a gente vai para um dos documentos que eu acho bem importante, principalmente se você é desenvolvedor e é a pessoa que vai ler esse documento ou que vai criar esse documento, porque ele acaba sendo, eu acredito que é o documento mais

00:19

moderado que nós temos, ou seja, ele tem bastante informação, um pouco mais baixo nível, mas ele não vai tão baixo nível em relação à implementação. Então, de forma geral, ele traz realmente o que vai ser feito, não numa visão tão high level como a gente acabou de ver,

00:37

Ela é mais low-level, mas ele foca muito mais em funcionamento, detalhes, contratos de uma forma mais detalhadas, mas ainda assim ele não traz o detalhe de códigos extremamente específicos. Normalmente ele trabalha muito mais com interfaces e coisas desse tipo, tá?

00:56

Então, o nome desse documento é Feature Design Doc, ou seja, o design para você desenvolver qualquer feature, e quando eu falo feature, pode ser uma feature pequena do seu sistema ou pode ser de um produto novo que tenha uma razão de auto-existir, beleza? Então, seguinte, o Feature Design Doc

01:18

Ele é o como implementar uma feature específica no contexto definido pelo high-level design. Então, aqui vem os contratos públicos reais, o comportamento exato, fluxos detalhados, erros, semântica de headers, opções de configuração via código, critérios de aceites, e é um documento que habilita a implementação sem tanta ambiguidade, porque muitas vezes, quando a gente está numa visão muito alto nível,

01:48

a gente deixa muita coisa sem definição. Esse documento já traz algumas definições mais claras para a gente. Então, é importante você usar esse documento sempre que você vai fazer uma feature que vai expor uma API, que altera contratos, você adiciona opções de configuração, ela vai ter efeitos claros em segurança, em performance ou compatibilidade.

02:08

Então, normalmente, quando a gente tem esses tipos de detalhes, vale a pena você utilizar, tá? Normalmente, esse documento vai responder algumas perguntas como... Quais são os principais detalhes técnicos dessa feature? Como que essa feature se comporta em tempo de execução? Quais os contratos e as interfaces que ela expõe para a integração? Como que ela é configurada e quais as dependências que ela exige?

02:32

como que lida com erro, exceções, concorrência, como que a gente valida que a implementação está correta e atende os critérios técnicos, tá? Então, assim, é um documento que você consegue perceber que ele é mais técnico, ele responde mais perguntas, tá? Ou seja, ele vai um pouco mais abaixo nível do que o high-level design.

02:52

Ele não vai a tão baixo nível, falando que você vai usar esse padrão específico de codificação. Ele não faz isso. Mas ele dá claramente pontos importantes sobre aquilo que vai ser desenvolvido. Normalmente, o que você vai encontrar em um FDD? Lembrando, pessoal, que

03:12

Feature Design Doc, ou você pode encontrar outras siglas, mas que acabam representando exatamente a mesma coisa, tá? Então, normalmente, a gente vai ter contexto e motivação técnica, objetivos técnicos, escopos e exclusões, fluxo detalhados e diagramas, caso você precise, contratos públicos, assinaturas, endpoints, headers, exemplos,

03:35

Erros, exceções e fallbacks, observabilidade, dependência e compatibilidade, critérios de aceites técnicos, riscos e mitigação. Então, se você perceber, tem bastante coisa nesse tipo de documento e isso aí realmente

03:51

faz uma grande diferença na hora que você vai desenvolver qualquer coisa, tá? Eu acredito que quando eu mostrar agora o exemplo mais prático aí pra você desse documento feito, eu acho que vai ficar um pouco mais claro como é importante se todo projeto que você tivesse, você tivesse um documento desse realmente, tá? E o quão mais importante é agora que a gente tem IA, né?

04:15

como um documento desse não vai ajudar no nosso fluxo para desenvolvimento com inteligência artificial. Então, vamos nessa, que no próximo vídeo eu vou mostrar como é que fica esse documento.

## Resumo IA

**Abreviações**  
- **HLD** — *High-Level Design* (Projeto de Alto Nível)  
- **FDD** — *Feature Design Doc* (Documento de Design da Feature)  
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)  
- **IA** — Inteligência Artificial  

**Resumo**  
A aula apresentou o Feature Design Doc (FDD) como um documento intermediário entre o desenho arquitetural de alto nível e a implementação detalhada da feature. O instrutor explicou que, enquanto o HLD define o terreno da solução em nível macro, o FDD desce para um nível mais operacional, especificando comportamento exato, contratos públicos, fluxos, erros, configurações, dependências e critérios de aceite, sem chegar ao extremo de prescrever código linha por linha ou padrões internos de codificação.

Foi destacado que o FDD é especialmente importante quando a feature expõe uma API, altera contratos, adiciona opções de configuração ou gera impacto em segurança, performance e compatibilidade. Nesses casos, a arquitetura sozinha não basta, porque ainda existem definições que precisam ser compartilhadas antes da implementação. O documento ajuda a reduzir ambiguidades, alinhar expectativas entre equipes e permitir que a feature seja construída, revisada, testada e aceita com base em critérios objetivos.

A aula também detalhou as perguntas que o FDD deve responder: como a feature se comporta em tempo de execução, quais interfaces e contratos expõe, como é configurada, de quais dependências precisa, e como trata erros, exceções e concorrência. O instrutor reforçou que esse tipo de documento fecha o espaço entre “a arquitetura permite” e “o código realmente faz”, explicitando regras operacionais e condições observáveis, como no exemplo do rate limiter, em que não basta citar a solução com Redis e middleware, sendo necessário definir headers, resposta 429 e o comportamento de fallback.

Por fim, foram listados os componentes que normalmente compõem um FDD: contexto e motivação técnica, objetivos, escopo e exclusões, fluxos detalhados, diagramas, contratos públicos, erros, fallbacks, observabilidade, dependências, compatibilidade, critérios de aceite, riscos e mitigação. O instrutor concluiu ressaltando que um FDD bem escrito também melhora o uso de IA no desenvolvimento, porque fornece contexto operacional claro e reutilizável, reduzindo interpretações vagas e ajudando na geração de código e testes.

**Pontos de atenção**  
- O FDD deve ficar em um nível intermediário: mais detalhado que o HLD, mas sem virar especificação de código ou de implementação interna.  
- Use FDD quando a feature impactar API, contratos, configuração, segurança, performance ou compatibilidade.  
- Não deixe erros, exceções e fallbacks como decisão livre do implementador; eles precisam estar especificados.  
- Contratos públicos devem ser explícitos: assinaturas, endpoints, headers, exemplos e semântica de resposta.  
- Critérios de aceite técnicos são essenciais para tornar a feature verificável e testável.  
- Dependências e compatibilidade precisam ser tratadas de forma concreta, especialmente em integrações e rollout.  
- O documento deve reduzir ambiguidade entre arquitetura e execução; se ainda houver espaço para interpretação, ele está incompleto.  
- Riscos e mitigação devem ser considerados, assim como observabilidade quando ela afetar a operação da feature.  
- Um FDD bem estruturado melhora o desenvolvimento assistido por IA, pois fornece contexto claro e diminui respostas genéricas ou incorretas.