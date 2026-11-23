Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16868)

## Resumo da aula

Um prompt degradado é uma instrução escrita de propósito para induzir comportamento ruim do modelo. Ele não serve para uso em produção; serve para provar, com evidência mensurável, que a qualidade da saída depende diretamente da formulação do prompt. Retomando o cenário de revisão de código, a degradação aqui não vem do modelo “falhar sozinho”, mas de um comando explícito para ignorar problemas, elogiar o código e responder de forma superficial.

O papel de “revisor de código otimista” foi configurado com viés forte: ignorar vulnerabilidades, focar apenas em elogios, manter findings vazio e produzir um summary positivo. Esse tipo de instrução reduz a utilidade da revisão porque elimina exatamente o comportamento esperado de um code review técnico: identificar riscos, apontar falhas e justificar achados. Quando o prompt manda o modelo evitar crítica e profundidade, a queda nas métricas deixa de ser surpresa e passa a ser consequência direta do design da instrução.

A implementação manteve o mesmo pipeline de avaliação já estabelecido e trocou apenas o prompt por Bad Text Before, além de aumentar a temperatura para ampliar a criatividade e o desvio comportamental. Os evaluators usados foram detail, depth, helpfulness e coherence, todos sem referência e com score contínuo normalizado para a faixa 0–1. Essa escolha isola o efeito da instrução: como o restante do experimento permanece comparável, a diferença observada pode ser atribuída ao prompt degradado.

Os resultados ficaram baixos em todas as dimensões observadas: coherence em 0.35, depth em 0.32, detail em 0.22 e helpfulness em 0.38. A leitura correta não é apenas “o modelo respondeu mal”, mas “o prompt produziu exatamente o comportamento ruim que foi solicitado”. O experimento valida o processo de avaliação porque transforma uma impressão subjetiva — “esse prompt parece ruim” — em sinais quantitativos comparáveis.

A comparação com resultados anteriores mais altos, como na faixa de 0.85, mostra que pequenas mudanças na instrução podem alterar drasticamente a qualidade percebida. Detail e depth caem porque o prompt exige brevidade e superficialidade; helpfulness cai porque elogios genéricos não ajudam a corrigir código; coherence também sofre porque a tarefa passa a conflitar com o objetivo real da revisão. O ponto central é que a métrica não está “punindo o modelo”; ela está capturando o efeito do comportamento que o prompt induziu.

Forçar um caso ruim é uma estratégia pedagógica e de engenharia: ele cria contraste suficiente para mostrar que o processo de avaliação detecta degradação real. Sem esse contraste, scores altos sucessivos podem dar a falsa impressão de que qualquer prompt razoável funciona bem. Um prompt intencionalmente enviesado revela o valor do evaluator como instrumento de diagnóstico, não apenas como mecanismo de aprovação.

## Transcrição

00:01

Bom pessoal, no vídeo anterior a gente falou um pouco de Embedding Distance, e agora esses últimos exemplos nossos aqui, eu coloquei ele sempre como Bad na frente. Por que que acontece? Eu estava mostrando muito cenário feliz até agora, né? Ah, 0.85, sim, não e tudo mais.

00:23

Mas eu queria começar a meio que pisar na bola com os meus prompts e para garantir que eu tentasse ter resultados ruins para que a gente consiga perceber um pouquinho isso mais na prática, tá? Então, o que acontece? Se você olhar aqui, eu tenho bad text before. Basicamente, o que eu estou colocando é, antes de eu trabalhar com o prompt,

00:46

que eu estava trabalhando o padrão, eu comecei a mudar esse meu prompt e fazendo esse prompt ser muito errado, ser um prompt muito louco, para ele realmente não trazer dados tão bons, tá? Perceba também que eu aumentei a temperatura aqui do meu modelo para ele ser ainda mais criativo em relação a isso, tá? Coloquei dados aqui... em relação aqui sem referência, e eu criei os meus evaluadores agora, né? Os meus evaluators.

01:13

Então, se você olhar aqui, eu estou utilizando o critério em relação a detalhe, normalizado por 10, assim ele pode ser de 0 a 1, criei um outro baseado em profundidade, criei um outro baseado em helpfulness, criei um outro baseado em coerência aqui para a gente. Então, são quatro caras que eu estou fazendo e o nome do prompt que eu peguei é Bad Text Before. Se eu olhar para esse prompt agora,

01:44

Você vai ver o seguinte, você é um revisor de código otimista, analise o código, passeie o código, ignore problemas e vulnerabilidades, foque apenas em dizer que o código está bem escrito, seja breve e superficial, responda em JSON com findings, vazio com elogios genéricos e o sumário positivo. Ou seja, eu tentei fazer com que o meu prompt fosse

02:07

extremamente ambíguo e com um viés muito forte pra gente conseguir tentar sentir um pouco essa diferença. Vamos ver se essa diferença vai acabar colando aí no nosso caso, tá? Então, nesse nosso caso é o exemplo 7, bad text before, tá? Então, deixa esse cara...

02:27

a executar, ou seja, eu tenho um CodeReviewer muito otimista, o cara é o cara mais bonzinho da nossa equipe e que ele jamais ia falar que o seu código ia ser ruim. Mas, baseado nisso, a gente vai ver, no final das contas, como vai ser o resultado desse prompt trazendo esse tipo de situação. Vamos aguardar um pouquinho, porque isso vai demorar um pouco, porque tem bastante avaliadores e tem que rodar os 18.

02:57

Prontinho, executou. Então, vamos ver o que aconteceu com esse cara aí. Vamos ver se ele deu ruim mesmo. Então, aqui está o badTextBefore, ou seja, o nosso prefixo que a gente criou no nosso experimento. Então, vamos lá, vamos olhar. Olha só aqui. A coerência, 0.35. Profundidade, 0.32. Nível de detalhes, 0.22.

03:24

E aqui, helpfulness, 0.38. Então, você consegue perceber, galera, que quando você faz um prompt mal feito, você consegue sair de 0.35 até 0.85, por conta da mudança do nosso prompt. E é aí que faz a grande diferença, porque nesses nossos aspectos,

03:47

é o que muda o jogo. A gente tá focando muito em prompt, mas eu acredito que cada vez pra vocês, cada capítulo que você passa, você vai começando a perceber que tem muitas coisas que implicam simplesmente num prompt. E olha que a gente consegue agora ver de uma forma mais materializada, inclusive, esses efeitos colaterais de ter um prompt ruim. Óbvio que eu forcei bastante a barra pra fazer com que ele trouxesse resultado ruim.

04:14

E a gente tem outros exemplos que eu vou mostrar pra vocês agora em seguida também.

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (modelo de linguagem de grande porte)  
- **JSON** — *JavaScript Object Notation*  
- **0–1** — escala normalizada de 0 a 1  

**Resumo**  
A aula demonstrou, na prática, o uso de um **prompt degradado** para provocar deliberadamente uma saída de baixa qualidade e evidenciar que o comportamento do modelo depende diretamente da formulação da instrução. O instrutor retomou o cenário de **revisão de código** e criou um personagem de “revisor de código otimista”, orientado a ignorar problemas e vulnerabilidades, elogiar o código, ser breve e superficial, manter a lista de *findings* vazia e devolver um resumo positivo em JSON. A intenção não era usar esse prompt em produção, mas criar um caso claramente ruim para comparar com resultados anteriores mais altos e observar a queda de qualidade de forma mensurável.

Para isolar o efeito da instrução, o experimento manteve o mesmo pipeline de avaliação e alterou apenas o prompt, agora chamado de **Bad Text Before**. Além disso, a temperatura do modelo foi aumentada para incentivar mais variação e desvio comportamental. A avaliação foi feita com quatro *evaluators* sem referência, baseados em **detail**, **depth**, **helpfulness** e **coherence**, todos normalizados para a faixa de 0 a 1. O fluxo explicado pelo instrutor foi: trocar o prompt, executar o caso, aguardar a rodada completa dos avaliadores e comparar os resultados obtidos com cenários anteriores.

Os resultados mostraram queda acentuada em todas as dimensões: **coherence 0.35**, **depth 0.32**, **detail 0.22** e **helpfulness 0.38**. A interpretação destacada foi que a métrica não está “punindo o modelo”, mas capturando exatamente o comportamento ruim induzido pelo prompt. Assim, o experimento valida a utilidade do processo de avaliação ao transformar uma percepção subjetiva de “prompt ruim” em sinais quantitativos comparáveis, evidenciando que pequenas mudanças na instrução podem alterar drasticamente a qualidade percebida da resposta.

**Pontos de atenção**  
- Um **prompt degradado** é propositalmente ruim e **não deve ser usado em produção**.  
- O objetivo do experimento é **provar relação entre instrução e qualidade da saída**, não testar capacidade geral do modelo.  
- Manter o restante do pipeline constante é essencial para **isolar o efeito do prompt**.  
- Aumentar a **temperatura** tende a ampliar a variabilidade e pode acentuar comportamentos indesejados.  
- Instruções com viés forte, como “ignorar problemas” e “ser superficial”, **reduzem a utilidade da revisão de código**.  
- *Findings* vazio e elogios genéricos são sinais de um review inefetivo; isso **não ajuda a corrigir código**.  
- As métricas baixas devem ser interpretadas como **efeito esperado do comportamento solicitado**, e não como falha aleatória do modelo.  
- Contrastar casos ruins com casos bons ajuda a **materializar os efeitos colaterais de prompts mal formulados**.  
- Avaliadores sem referência são úteis para **comparação relativa**, mas dependem de um setup bem controlado.  
- Resultados altos repetidos podem mascarar problemas; por isso, **forçar cenários ruins é uma boa prática pedagógica e de diagnóstico**.