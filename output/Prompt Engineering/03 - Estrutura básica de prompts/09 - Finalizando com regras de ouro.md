Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16618)

## Resumo da aula

Regras de ouro em prompting funcionam como um checklist curto para validar a estrutura antes da execução. A utilidade desse checklist não está em impor um template rígido, mas em evitar omissões que aumentam ambiguidade, erro e variação indesejada na resposta. Se um item importante não aparece no prompt, essa ausência precisa ser intencional e justificada pelo caso de uso. O valor prático está em transformar estrutura em hábito de revisão, não em decorar uma fórmula fixa.

A revisão final deve verificar se o prompt cobre os blocos essenciais já estabelecidos: persona e escopo, objetivo, entradas separadas e mínimas, formato de saída, critérios, tratamento de ambiguidades e erros e proibições necessárias. Retomando a estrutura anterior, a pergunta correta não é “meu prompt está bonito?”, mas “cada parte necessária para controlar o comportamento do modelo está explícita?”. Esse tipo de checagem reduz improviso do modelo e torna a resposta mais auditável. Quando o prompt falha, normalmente a falha aparece justamente em um desses pontos ausentes ou mal definidos.

Proibições não são detalhe cosmético; elas delimitam o espaço de ação do modelo. Dizer o que não pode acontecer evita que a resposta viole formato, extrapole escopo ou introduza conteúdo que atrapalha consumo automático e revisão humana. Em prompts estruturados, restrições negativas funcionam como contenção de comportamento, especialmente quando o modelo tende a completar lacunas por inferência excessiva. Elas devem existir quando há risco real de desvio, não como lista arbitrária de comandos.

A estrutura é estável como referência, mas a implementação muda conforme o contexto operacional. Um prompt para processamento em batch, por exemplo, pode exigir entradas maiores, organização diferente dos dados e um formato de saída menos simples do que o usado em um caso pontual. Isso significa que “mínimo” e “adequado” são decisões relativas à tarefa, ao volume e ao modo de execução. O checklist continua válido, mas cada item precisa ser calibrado para o cenário real.

A pergunta central antes de rodar um prompt é sempre a mesma: o que entra, o que sai, o que é permitido, o que é proibido e como o agente reconhece o contexto logo no início. Essa heurística consolida a estrutura já conhecida em uma nota mental reutilizável. Retomando o exemplo estruturado anterior, a camada nova não é criar outra seção, mas revisar se todas as seções essenciais estão cobertas antes de executar. Esse hábito acelera construção, melhora consistência e reduz retrabalho em prompts reutilizados.

## Transcrição

00:01

Então, pessoal, só para a gente concluir o nosso raciocínio do que a gente viu dessa estruturação anterior.

00:07

Notas mentais, eu chamo isso de regras de ouro, quando você vai estruturar qualquer tipo de prompt, são coisas que você tem que pensar e que, normalmente, tem que ter no seu prompt. Se não tiver, tem que ter uma justificativa muito clara para não ter. Mas, normalmente, você vai ver coisas parecidas com essa. Então, antes de rodar um prompt, revise se ele define em persona o escopo,

00:33

Se ele tem um objetivo direto, se ele fornece entradas separadas e mínimas, se ele define um formato de saída, se ele lista critérios claros do que deve ser feito, se ele trata ambiguidade e erros e se ele inclui proibições necessárias.

00:52

Uma vez que você tiver isso como nota mental, eu acredito que você pode criar qualquer tipo de prompt, tá? Mas, obviamente, eles vão ter que ser adaptados. Ou seja, às vezes eu quero criar um prompt que vai trabalhar em batch. Então, as entradas separadas e mínimas não são tão mínimas. O formato de saída, às vezes, não é tão simples como apenas trazer um teste.

01:16

Entende? Então, o ponto principal aqui é que você sempre tem que pensar no conceito. O que eu quero ter de entrada, o que eu quero ter saído, o que pode, o que não pode, e como que eu consigo especializar esse meu agente para que ele entenda de cara o contexto que você está trabalhando, tá? Então, pense nessas regras de ouro, tome em nota, coloque uma notinha, toda hora que você for criar um prompt, tenta começar por isso. É um bom começo aí para você. Fechou?

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **batch** — Processamento em lote  

**Resumo**  
A aula conclui a discussão sobre estruturação de prompts apresentando “regras de ouro” como uma nota mental e um checklist de revisão antes da execução. O instrutor enfatiza que o objetivo não é seguir um template rígido, mas garantir que nenhum elemento essencial fique de fora sem uma justificativa clara, reduzindo ambiguidades, erros e variações indesejadas na resposta do modelo. A revisão deve verificar se o prompt explicita persona e escopo, objetivo direto, entradas separadas e mínimas, formato de saída, critérios do que deve ser feito, tratamento de ambiguidades e erros, além de proibições necessárias. Também é reforçado que restrições negativas são importantes para limitar o comportamento do modelo e evitar desvios de formato, escopo ou conteúdo. Por fim, a aula destaca que a estrutura geral é estável, mas a implementação precisa ser adaptada ao contexto operacional, como em cenários de processamento em lote, em que entradas e saídas podem ser mais complexas. A heurística central proposta é sempre revisar o que entra, o que sai, o que é permitido, o que é proibido e como o contexto é reconhecido logo no início, transformando esse raciocínio em hábito para acelerar a criação de prompts e reduzir retrabalho.

**Pontos de atenção**  
- O checklist não deve ser usado como template rígido; ele serve para revisão crítica.  
- Se um item essencial não estiver no prompt, a ausência precisa ser intencional e justificada.  
- Verificar explicitamente: persona, escopo, objetivo, entradas, formato de saída, critérios, ambiguidades/erros e proibições.  
- A pergunta correta não é se o prompt “está bonito”, mas se controla o comportamento do modelo de forma explícita.  
- Proibições são importantes para evitar extrapolação de escopo, quebra de formato e conteúdo indesejado.  
- Restrições negativas devem ser usadas quando houver risco real de desvio, não como lista decorativa.  
- O conceito de “mínimo” e “adequado” varia conforme tarefa, volume e modo de execução.  
- Em prompts para batch, entradas e formato de saída podem exigir mais estrutura do que em casos pontuais.  
- O ideal é sempre confirmar: o que entra, o que sai, o que pode, o que não pode e como o contexto é identificado.  
- O hábito de revisão melhora consistência, auditabilidade e reduz retrabalho em prompts reutilizados.