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
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Escala)
- **IA** — Inteligência Artificial

**Resumo**
A aula revisa fundamentos de Prompt Engineering com foco em seu impacto prático em aplicações que utilizam LLMs em produção. O instrutor destaca que prompt não é apenas uma instrução textual ao modelo, mas um elemento de design que afeta diretamente comportamento operacional, velocidade, custo e utilidade das respostas. A ideia central é que, ao entender minimamente como o modelo funciona, as decisões de implementação passam a ser mais conscientes e eficientes, tanto em ferramentas internas de produtividade quanto em sistemas mais complexos, como agentes de IA.

Também é explicado que cada escolha de contexto e formato do prompt tem consequência real no funcionamento da aplicação. Prompts maiores ou mal estruturados tendem a aumentar latência e custo, enquanto prompts mais enxutos e orientados ao objetivo favorecem eficiência. Nesse cenário, a qualidade da resposta precisa ser equilibrada com restrições de engenharia, especialmente tempo de resposta e custo operacional.

A aula introduz ainda conceitos que servirão de base para os próximos conteúdos, começando pela janela de contexto, que é o espaço limitado que o modelo possui para processar instruções, histórico e dados de entrada em uma única chamada. Como esse espaço é medido em tokens, a administração desse orçamento é essencial para evitar degradação da resposta ou aumento desnecessário de custo. Por fim, o instrutor menciona caching e batch prompting como técnicas importantes para reduzir desperdício e melhorar escalabilidade: caching reaproveita respostas ou partes de contexto já processadas, e batch prompting permite agrupar trabalho para usar melhor as chamadas ao modelo. Esses conceitos formam a base para discutir otimização de contexto e tornam o Prompt Engineering uma prática orientada por restrições reais de produção.

**Pontos de atenção**
- Prompt Engineering vai além de “escrever boas instruções”; ele afeta diretamente desempenho, custo e escalabilidade da aplicação.
- O tamanho e a estrutura do prompt impactam a latência: prompts longos ou mal organizados tendem a tornar a resposta mais lenta e cara.
- A qualidade da resposta não deve ser avaliada isoladamente; é necessário equilibrá-la com custo e tempo de resposta.
- A janela de contexto é limitada e precisa ser gerenciada com cuidado, pois tudo o que é enviado consome tokens.
- Cada token conta: histórico excessivo, documentos desnecessários e contexto mal selecionado podem desperdiçar orçamento e degradar a eficiência.
- Caching é uma técnica de otimização, não um substituto para um prompt bem projetado.
- Batch prompting pode melhorar eficiência em cenários de alto volume, mas deve ser planejado para não prejudicar a utilidade da resposta.
- Em produção, essas decisões são restrições de engenharia e devem orientar o desenho da solução desde o início.