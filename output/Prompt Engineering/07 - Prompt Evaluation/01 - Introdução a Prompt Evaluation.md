Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16856)

## Resumo da aula

Prompt evaluation é o processo de avaliar prompts com critérios explícitos, em vez de depender de impressão subjetiva. Dizer que um prompt é “bom” ou “ruim” não basta, porque essa classificação só faz sentido quando existe uma referência clara do que está sendo medido. Sem esse enquadramento, o ajuste de prompts vira tentativa e erro sem aprendizado acumulado. Tratar o prompt como algo mensurável transforma experimentação solta em engenharia reproduzível.

Um prompt só pode ser comparado de forma útil quando os critérios de análise estão definidos. Esses critérios existem porque diferentes prompts podem otimizar coisas diferentes: qualidade da saída, custo operacional ou experiência do usuário. Quando a equipe não explicita o que considera sucesso, duas pessoas podem olhar a mesma resposta e chegar a conclusões incompatíveis. A avaliação organiza essa decisão e reduz ambiguidade.

Testar prompts “na sorte” produz mudanças, mas não produz conhecimento confiável sobre por que um resultado melhorou ou piorou. Isso cria um ciclo de iteração sem memória técnica: a equipe tenta variações, observa impressões pontuais e perde a capacidade de repetir o que funcionou. Em sistemas reais, esse comportamento encarece manutenção e dificulta evolução consistente. Avaliar de forma estruturada evita que cada nova tentativa recomece do zero.

O prompt não é apenas texto de instrução; ele atua como um componente que altera o comportamento do sistema. Mudar esse componente pode modificar a resposta gerada, o consumo de recursos e a forma como o usuário percebe o produto. Por isso, o prompt precisa ser tratado com o mesmo rigor aplicado a outras partes que afetam resultado de negócio. Se ele influencia o sistema, ele também precisa ser observado, comparado e evoluído com método.

A avaliação de prompts importa porque o prompt afeta diretamente três dimensões centrais. A primeira é a qualidade da saída: respostas mais corretas, úteis e adequadas ao objetivo do sistema. A segunda é o custo, já que a formulação do prompt influencia processamento e, portanto, gasto operacional. A terceira é a experiência do usuário, porque a percepção de utilidade, clareza e consistência da IA depende fortemente de como o prompt orienta o modelo.

Comparar prompts é necessário porque pequenas mudanças podem gerar impactos relevantes no comportamento do sistema. Essa comparação não deve acontecer apenas uma vez, mas de forma contínua, já que o uso real revela efeitos que nem sempre aparecem em testes informais. Avaliação contínua cria uma base para decidir quando um prompt realmente melhorou o sistema e quando apenas pareceu melhor em um caso isolado. Esse é o ponto de partida para, nas próximas etapas, definir objetivos, métricas, evaluators e datasets de forma disciplinada.

## Transcrição

00:00

Bom, pessoal, agora a gente chegou aqui num capítulo realmente muito importante em relação a prompts, principalmente, que é a parte de prompt evaluation. Uma das coisas mais comuns de as pessoas perguntarem é, como eu sei se o meu prompt está bom ou se ele está ruim? E, normalmente, a resposta é dada no formato de pergunta.

00:23

Ok, quais critérios você utiliza, no final das contas, para definir isso? Então, simplesmente dizer que algo é bom ou é ruim às vezes pode ser fácil, às vezes pode ser difícil, mas o grande ponto é você tem que ter critérios claros. E o ponto é que quando a gente não estuda de forma coerente a parte de verificação, evaluation de prompt,

00:48

significa que muitas das coisas que a gente acaba fazendo são chutes, ou seja, a gente fica testando na sorte e a gente acaba não conseguindo entender e ter uma clareza de como eu faço esse tipo de análise. Então, nesse capítulo aqui, a gente tem bastante coisa para ver, muitos exemplos para seguir. Eu acredito que isso vai ser extremamente importante

01:15

para você agora que está trabalhando com prompts, para você na hora que for trabalhar com arquitetura utilizando IA, tem muita coisa aqui que realmente vai fazer diferença. Obviamente que o nível de profundidade que a gente vai trazer aqui vai estar muito mais focado, obviamente, no prompt em si e também vai ter muito focado nos resultados que esses prompts conseguem gerar. Então, o Prisma que a gente vai olhar agora para a parte de verificação de prompts,

01:44

É muito mais para a gente ter essa ideia geral. E você vai perceber que, mesmo falando que a gente vai ter uma ideia geral, você vai perceber como que o buraco é muito mais fundo na hora que a gente está falando sobre tudo isso. Porque, no final das contas, é o prompt que vai definir quanto você vai gastar.

02:01

e, no final do dia também, qual é a experiência que o usuário vai ter utilizando a inteligência artificial. Tudo está no prompt e você tem que conseguir medir. E, nesse capítulo, a gente vai conseguir fazer isso bem legal. Maravilha? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- IA: Inteligência Artificial

**Resumo**  
A aula introduz o conceito de *prompt evaluation* como o processo de avaliar prompts com critérios explícitos, em vez de depender de impressões subjetivas como “bom” ou “ruim”. O instrutor destaca que a avaliação só faz sentido quando há uma referência clara do que está sendo medido, pois sem critérios definidos a equipe cai em tentativa e erro, sem aprendizado acumulado nem capacidade de reproduzir resultados.  

Também é explicado que prompts não são apenas texto de instrução, mas componentes que influenciam diretamente o comportamento do sistema, afetando a qualidade da resposta, o custo operacional e a experiência do usuário. Por isso, mudanças em prompts devem ser tratadas com o mesmo rigor aplicado a outras partes do sistema que impactam resultados de negócio.  

A aula reforça que avaliar prompts de forma estruturada evita decisões inconsistentes entre pessoas diferentes e impede que cada nova iteração recomece do zero. O objetivo do capítulo é preparar a base para etapas posteriores, nas quais serão definidos objetivos, métricas, *evaluators* e *datasets* para uma prática mais disciplinada de validação e evolução de prompts.

**Pontos de atenção**  
- Não basta dizer que um prompt é “bom” ou “ruim”; é necessário definir critérios claros de avaliação.  
- Sem critérios explícitos, duas pessoas podem interpretar a mesma saída de formas diferentes.  
- Testar prompts “na sorte” gera ajustes sem entendimento real do que causou a melhora ou piora.  
- A ausência de avaliação estruturada leva a um ciclo de iteração sem memória técnica, dificultando manutenção e evolução.  
- O prompt deve ser tratado como componente do sistema, pois impacta comportamento, custo e experiência do usuário.  
- Pequenas alterações em prompts podem provocar efeitos relevantes; por isso, a comparação precisa ser contínua e sistemática.  
- A avaliação deve servir para decidir com base em evidências quando um prompt realmente melhorou o sistema.