Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16745)

## Resumo da aula

Neste capítulo vamos entrar em um assunto muito importante e que, às vezes, acaba sendo subestimado quando trabalhamos com inteligência artificial. Vamos falar sobre Query Reformulation e Prompt Enrichment. O que isso significa? Muitas vezes gastamos muito dinheiro trabalhando com IA por um único motivo: o usuário final chega e faz uma pergunta mal formulada. Vamos imaginar que o usuário final cria um prompt mal estruturado.

Quando isso acontece, você recebe informações que não são claras o suficiente ou que não contêm todo o material necessário. Isso faz com que o usuário continue iterando com o sistema e, no final das contas, ele acaba gastando muitos tokens. Existe ainda um problema que pode ser pior: o usuário não fica satisfeito com a resposta que recebeu e continua culpando o sistema.

Então, o nosso objetivo aqui é pensar da seguinte forma: como podemos ajudar esse usuário a obter respostas melhores da IA, mesmo sabendo que ele fará perguntas, entre aspas, erradas ou incompletas. Os dois aspectos que quero apresentar hoje estão relacionados a como reformular perguntas, principalmente quando precisamos buscá-las em ambientes externos, trazendo as informações mais relevantes.

Ao mesmo tempo, veremos como aplicar técnicas para melhorar o prompt e, assim, obter respostas mais qualificadas. Esse será exatamente o objetivo que vamos tratar aqui hoje. Também apresentarei alguns exemplos práticos com código para que você consiga entender melhor essa diferença. Então, vamos começar. No próximo vídeo, vamos iniciar a discussão desses aspectos.

## Transcrição

00:00

Bom, pessoal, nesse capítulo a gente vai entrar num assunto, mas ele é muito, muito importante e, às vezes, ele acaba sendo subestimado quando a gente vai trabalhar com inteligência artificial. Então, a gente vai falar hoje sobre Query, Reformulation e Prompt Enrichment. O que isso significa? Muitas vezes, a gente gasta muito dinheiro trabalhando com IA por um único motivo.

00:30

o usuário final chega e faz uma pergunta, uma pergunta, vamos dizer assim, mal feita. Vamos imaginar que o usuário final faz um prompt mal feito. E quando você tem um prompt mal feito, você vai receber informações não claras o suficiente, ou com todo o material que você precisa, e isso vai fazer com que o usuário continue e continue iterando,

00:54

com o seu sistema e, no final das contas, ele acaba gastando, inclusive, muitos tokens ou, até mesmo, um problema que, às vezes, acaba sendo pior. Ele não fica contente com a resposta que ele recebeu e ele vai continuar culpando o seu sistema. Então, o nosso objetivo agora aqui é pensar da seguinte forma, como que eu consigo fazer algo

01:19

para ajudar esse usuário a conseguir pegar respostas melhor da IA, mesmo sabendo que ele vai fazer perguntas, entre aspas, erradas ou incompletas. Então, os dois aspectos que eu quero trazer aqui hoje para você é em relação a como eu consigo reformular

01:44

perguntas, e principalmente para que a gente consiga buscar essas perguntas em ambientes externos e conseguir, vamos dizer assim, trazer as informações mais relevantes, mas, ao mesmo tempo, como que eu consigo trabalhar com técnicas para fazer com que o meu prompt melhore, para eu trazer respostas melhores. Então, o nosso objetivo, que a gente vai tratar aqui,

02:09

Hoje vai ser exatamente esse. Eu também vou te dar alguns exemplos práticos ali, com código, para que você consiga entender um pouco essa diferença. Fechou? Então, vamos nessa. No próximo vídeo, a gente vai começar a falar desses aspectos.

## Resumo IA

**Resumo**  
A aula apresenta dois temas centrais no uso de inteligência artificial em aplicações com interação textual: **Query Reformulation** e **Prompt Enrichment**. O instrutor destaca que um dos principais problemas em sistemas baseados em IA é o usuário final formular perguntas mal estruturadas, incompletas ou pouco claras, o que gera respostas insuficientes, aumenta a necessidade de iterações e, consequentemente, eleva o consumo de tokens e o custo da operação. Além disso, uma resposta insatisfatória pode levar o usuário a atribuir a falha ao sistema, mesmo quando a origem do problema está na formulação do pedido.

O objetivo da aula é mostrar como melhorar a qualidade da resposta da IA mesmo quando a entrada do usuário não é ideal. Para isso, a aula introduz a ideia de reformular consultas, especialmente quando é necessário buscar informações em ambientes externos, priorizando a recuperação dos dados mais relevantes. Em paralelo, explora técnicas de enriquecimento de prompt para tornar a solicitação mais completa e gerar respostas mais qualificadas. O instrutor também indica que trará exemplos práticos com código para evidenciar a diferença entre esses dois conceitos e como aplicá-los na construção de soluções mais eficientes.

**Pontos de atenção**  
- Prompt mal formulado pode gerar respostas vagas, incompletas ou pouco úteis.  
- Entradas ruins tendem a aumentar a quantidade de iterações e o consumo de tokens.  
- O custo de uso da IA pode crescer significativamente quando o sistema precisa “adivinhar” a intenção do usuário.  
- Uma resposta insatisfatória pode ser interpretada como falha do sistema, impactando a percepção do usuário.  
- **Query Reformulation** é especialmente relevante quando há necessidade de buscar informações em fontes externas; reformular bem a consulta melhora a relevância do retorno.  
- **Prompt Enrichment** ajuda a complementar a solicitação original para aumentar a qualidade da resposta.  
- O foco não é apenas “corrigir o usuário”, mas projetar o sistema para lidar melhor com perguntas erradas ou incompletas.  
- Exemplos práticos com código são importantes para entender a aplicação real dessas técnicas e evitar confusão entre os dois conceitos.