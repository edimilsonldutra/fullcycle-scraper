Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16596)

## Resumo da aula

Prompt Engineering não se limita a escrever instruções para um modelo; ele influencia o comportamento operacional de aplicações que usam LLMs em produção. Entender minimamente como o modelo funciona muda decisões de implementação, porque o desenho do prompt afeta velocidade, custo e utilidade da resposta. Isso vale tanto para ferramentas internas que aumentam produtividade quanto para sistemas mais complexos, como agentes de IA. Um prompt bem projetado deixa de ser tentativa e erro e passa a ser parte do design do sistema.

Quando uma aplicação envia prompts a um modelo, cada escolha de contexto e formato tem consequência prática. Um prompt maior ou mal estruturado pode aumentar o tempo de resposta e elevar o custo de operação, enquanto um prompt mais enxuto e orientado ao objetivo tende a melhorar eficiência. Por isso, qualidade de resposta não pode ser analisada isoladamente: ela precisa ser equilibrada com latência e custo. Em produção, esse equilíbrio é uma restrição de engenharia, não um detalhe secundário.

Janela de contexto é o espaço disponível para o modelo processar instruções, histórico e dados de entrada em uma única chamada. Esse espaço é limitado por tokens, então cada palavra, trecho de histórico ou documento incluído consome parte de um orçamento finito. Quando esse limite é mal administrado, a aplicação perde eficiência e pode degradar a resposta ou exigir chamadas mais caras. Por isso, compreender contexto e tokens é base para qualquer estratégia séria de Prompt Engineering.

Caching e batch prompting aparecem como técnicas importantes para reduzir desperdício operacional em sistemas baseados em LLM. Caching evita recomputar respostas ou partes de contexto que já foram processadas, enquanto batch prompting busca aproveitar melhor chamadas agrupando trabalho de forma eficiente. Essas técnicas não substituem um bom desenho de prompt, mas ampliam a capacidade de escalar com menor custo e melhor desempenho. Elas se tornam especialmente relevantes quando a aplicação faz muitas chamadas repetidas ou em alto volume.

Janela de contexto, limite de tokens, caching e batch prompting formam um conjunto de conceitos que orienta decisões posteriores de implementação. Eles servem como base para discutir técnicas mais específicas de gerenciamento e otimização de contexto ao longo do capítulo. Sem esse enquadramento, Prompt Engineering vira apenas ajuste textual; com ele, passa a ser uma prática orientada por restrições reais de operação.

## Transcrição

00:01

Bom, pessoal, seguinte, agora eu quero revisitar com você alguns pontos que vão se encaixar quando a gente está falando em Prompt Engineering. Então, somente para a gente alinhar as expectativas aqui, eu não quero me aprofundar muito nesse aspecto que eu quero trazer aqui para vocês, principalmente porque numa disciplina, por exemplo, como arquitetura, na era da IA,

00:25

a gente pode ver todos esses aspectos de uma forma muito mais fundamentada. Por outro lado, quando a gente está falando em Prompt Engineering, nós temos que entender alguns aspectos básicos de como o modelo funciona, porque uma vez que a gente entende isso, independente se a gente vai trabalhar desenvolvendo aplicações no dia a dia para ajudar

00:48

a nossa velocidade e produtividade, ou se a gente for criar agentes de A, entender isso vai mudar completamente, porque isso vai fazer com que a sua aplicação fique mais rápida ou fique mais lenta, que tudo fique muito mais custoso, menos custoso. Então, é importantíssimo a gente voltar e revisitar

01:07

de forma geral, esses tipos de assuntos. E agora, eu quero tratar com você assuntos que vão focar tanto em janelas de contexto, limite de tokens, a gente vai falar sobre caching, a gente vai falar sobre batch prompting e diversos aspectos que vão realmente fazer diferença na hora que você for montar o seu prompt de forma geral. Fechou? Então, vamos nessa. Até o nosso próximo vídeo para a gente começar e entrar nesse assunto.

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **IA** — Inteligência Artificial  

**Resumo**  
A aula revisita fundamentos importantes de Prompt Engineering com foco em aplicações práticas. O instrutor destaca que, ao entender minimamente como um modelo de linguagem funciona, as decisões de implementação mudam significativamente, tanto em ferramentas internas de produtividade quanto em sistemas mais complexos, como agentes de IA. O ponto central é que o prompt não deve ser visto apenas como texto de instrução, mas como parte do design operacional da aplicação, pois influencia diretamente velocidade, custo e utilidade da resposta.

Também é explicado que, em produção, o equilíbrio entre qualidade da resposta, latência e custo é uma restrição real de engenharia. Prompts maiores ou mal estruturados tendem a consumir mais tempo de resposta e aumentar custos, enquanto prompts mais objetivos podem melhorar a eficiência. Nesse contexto, o instrutor introduz conceitos que serão explorados ao longo do capítulo, como janela de contexto, limite de tokens, caching e batch prompting, todos fundamentais para administrar melhor os recursos do modelo. A aula prepara o terreno para discussões mais técnicas sobre otimização e gerenciamento de contexto, reforçando que Prompt Engineering vai além de tentativa e erro e passa a ser uma prática orientada por restrições concretas de operação.

**Pontos de atenção**  
- Entender o funcionamento básico do modelo é essencial para tomar boas decisões de implementação.  
- O desenho do prompt afeta diretamente **velocidade**, **custo** e **qualidade útil** da resposta.  
- Em produção, a qualidade da resposta deve ser equilibrada com **latência** e **custo operacional**.  
- Prompts grandes ou mal estruturados podem deixar a aplicação mais lenta e cara.  
- A **janela de contexto** é limitada e deve ser usada com cuidado, pois todo texto incluído consome tokens.  
- O gerenciamento inadequado de **tokens** pode degradar a resposta e aumentar o custo das chamadas.  
- **Caching** ajuda a evitar recomputação de conteúdo já processado, reduzindo desperdício.  
- **Batch prompting** pode melhorar eficiência ao agrupar trabalho em chamadas mais bem aproveitadas.  
- Essas técnicas não substituem um bom prompt; elas complementam um bom desenho para escalar melhor.  
- Prompt Engineering não deve ser tratado como ajuste textual isolado, mas como parte do projeto do sistema.