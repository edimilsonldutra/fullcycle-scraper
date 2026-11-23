Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16937)

## Resumo da aula

Retomando a comparação pairwise já estabelecida, o experimento agora ganha uma forma concreta: o mesmo código é avaliado por dois prompts concorrentes e uma terceira entidade decide qual resposta é melhor. O objetivo não é medir acerto contra ground truth absoluto, mas comparar duas perspectivas de análise sobre a mesma entrada. Isso permite testar hipóteses de melhoria mesmo quando a qualidade depende de julgamento relativo. O LangSmith entra como ambiente para registrar prompts, dataset, execuções e decisões do juiz.

Prompt A e prompt B são apenas rótulos das duas variantes comparadas dentro do experimento controlado. Isso não equivale a teste A/B de produção, porque aqui não há tráfego real de usuários nem métrica de negócio observada em ambiente produtivo. A evidência produzida é comparativa e técnica: qual saída parece melhor segundo um critério explícito. Essa distinção evita interpretar um experimento de avaliação offline como validação de impacto em produto.

Os dois prompts não competem por estilo, mas por política de revisão. Um deles prioriza performance e procura sinais como N+1, memory leak, blocking e missing timeouts; o outro prioriza segurança e valida findings sob a ótica de vulnerabilidades. Como ambos recebem o mesmo código, a diferença observada vem da instrução embutida no prompt, não da entrada. O experimento isola exatamente esse efeito: como perspectivas distintas mudam o code review produzido.

LLM as a judge é o uso de um modelo adicional como árbitro da comparação entre duas saídas. Em vez de pedir ao mesmo prompt que se autoavalie, o experimento define um juiz separado, com papel explícito de técnico imparcial. Esse juiz recebe o código-fonte original, a resposta A e a resposta B, e decide qual revisão é superior segundo as regras fornecidas. A qualidade do experimento depende de o juiz ter instruções claras, auditáveis e alinhadas ao objetivo da comparação.

O juiz não deve escolher com base em preferência vaga; ele precisa operar com critérios explícitos. Neste cenário, ele compara dois code reviews olhando o código real, o impacto dos problemas apontados e a natureza dos findings. Se identificar vulnerabilidades críticas reais, escolhe A; se identificar problemas críticos reais de performance, escolhe B. Quando os dois lados encontram problemas de peso equivalente, o resultado correto não é forçar um vencedor, mas registrar empate.

Tie é um resultado legítimo da avaliação pairwise, não um erro do processo. Ele representa a situação em que as duas respostas têm mérito equivalente segundo o critério adotado, ou em que nenhuma supera claramente a outra. Permitir empate evita introduzir ruído ao obrigar o juiz a escolher artificialmente entre alternativas indistinguíveis. Em experimentos iterativos, a frequência de tie também informa se as mudanças de prompt estão realmente produzindo diferença perceptível.

updatePrompt não é apenas uma nova versão textual do prompt; ele representa uma hipótese de melhoria. Primeiro compara-se A contra B na configuração atual; depois altera-se um dos prompts e executa-se novamente o mesmo desenho experimental. Se a distribuição de vitórias mudar a favor da versão atualizada, há evidência de que a modificação deslocou a qualidade relativa da saída. Esse ciclo transforma edição de prompt em iteração controlada, e não em tentativa aleatória.

A execução segue uma ordem simples: subir o dataset, criar os prompts, rodar as duas variantes sobre as mesmas entradas e enviar as saídas ao juiz. O dataset continua sendo a base comum da comparação, como já visto anteriormente, mas agora ele alimenta duas gerações concorrentes em vez de uma comparação contra ground truth. O juiz recebe três entradas por caso: código-fonte, resposta A e resposta B. O resultado de cada item é uma decisão entre A, B ou tie, que depois pode ser agregada para orientar a próxima iteração de prompt.

## Transcrição

00:01

Bom pessoal, no vídeo anterior a gente acabou falando isso de pairwise evaluator e evaluation. Então vamos que nós temos um exemplo aqui bem tranquilo para conseguir mostrar aqui para vocês. Então eu vou aqui nesse meu terceiro exemplo que é chamado de pairwise e esse exemplo basicamente é o seguinte.

00:19

eu vou criar dois prompts. Eu poderia rodar os prompts na minha máquina, mas aqui eu vou mostrar para vocês que você também é capaz de criar prompts lá no Langsmith. E nós temos um dataset também, eu tenho alguns helpers, que são algumas funções que me ajudam com o script, depois você pode olhar com calma. Eu tenho um arquivo run, que vai executar o processo, mas uma coisa interessante que você vai ver é que eu tenho um update prompt versão 2.

00:49

Por que eu estou dizendo isso? Porque a nossa ideia vai ser o seguinte, eu vou carregar dois prompts no Langsmith, vou rodar o nosso evaluation, aí a gente vai fazer a comparação desses dois prompts, ou quem ganhou basicamente isso, qual opção que ganhou, A ou B, beleza? Depois disso, a gente vai fazer uma atualização,

01:13

em um dos prompts, e daí a gente vai ver quem ganhou com essa mudança. Então, a ideia é fazer um A, B, depois que a gente fez isso, a gente altera o prompt, roda novamente, e daí a gente consegue perceber se a mudança de prompt teve melhora ali pra gente, tá? E quando eu tô falando em A, B, é prompt A, prompt B. Eu não estou falando que é um teste A, B. Normalmente, teste A, B são testes que a gente faz em produção.

01:39

Beleza? Então, a primeira coisa que eu vou fazer aqui é eu tenho que fazer o upload do nosso dataset. Vamos ver se tudo vai funcionar. Então, aqui tem o pairwise upload dataset. Ele vai subir aqui o nosso dataset.

01:59

Subi 10 datasets aqui de exemplo. Agora eu vou executar para a gente criar os nossos prompts. Então, aqui, Python 3 createPrompt. Vou criar os meus dois prompts que eu estou querendo. Então, se você olhar aqui o nosso

02:22

e eu quero trazer o contexto aqui pra vocês é o seguinte eu tenho um data set e esse prompt que eu tenho ele funciona da seguinte forma tá um prompt ele é focado em performance então ele vai receber o código

02:43

e ele vai analisar esse código de forma geral, focado muito mais identificando pontos de performance. Então, ele vai olhar problemas de N mais 1, problema de memory leak, blocking, missing timeouts, etc. Então, se você olhar a análise desse camarada, ele é muito mais focado em performance.

03:06

eu tenho meu segundo prompt, que foca um pouco mais em segurança. Então, se você olhar, esse prompt vai começar a fazer validações nos findings dele, baseado na perspectiva de segurança. Então, se você perceber, são dois prompts diferentes, que têm foco em coisas diferentes, para a gente fazer a execução. Mas quem vai verificar essa...

03:35

essa execução? O nosso juiz. A gente está usando LLM as a judge. Então, se você olhar aqui, eu tenho um pairwise judge. E o que eu estou falando aqui nesse nosso caso, nesse nosso prompt? Que eu tenho três entradas aqui. Eu tenho o código fonte, que eu vou passar para ele no meu dataset, eu tenho a resposta A, eu tenho a resposta B aqui para mim.

04:00

E aqui, olha só como é que está o meu prompt. Eu estou falando, olha, você é um técnico imparcial que vai fazer a verificação de dois CodeReviews. E eu vou passar o CodeReview, o código que vai ser analisado. O CodeReview do Security Expert, que é a nossa resposta 1.

04:20

E a gente tem o do Performance Expert, que é a resposta B, e aqui eu tenho a tarefa. Você vai fazer a verificação objetiva, você vai olhar o código real, vai verificar o impacto, você tem regras, etc. Depois você olhar. E se você perceber, se você achar

04:38

pontos críticos realmente de vulnerabilidade, escolho A. Se você achar pontos críticos reais de performance, escolho B. Se os dois forem encontrados igualmente, você vai fazer um tie, ou seja, você vai dar um empate para esses dois caras, e aí a resposta vai poder ser A, B ou empate, aqui nesse nosso caso, porque pode empatar eventualmente.

04:59

Então, esse é o juiz que vai executar isso, tá? Então, esse aí que é o nosso ponto agora mais importante. Então, a gente vai passar um código, vai ter code review, e aí a gente vai ver quem vai ganhar aqui nesse nosso ponto. Beleza? Então, próximo vídeo, só pra esse vídeo não ficar muito grande, eu vou executar esses caras e daí a gente faz essa discussão. Vamos nessa!

## Resumo IA

**Abreviações**  
- **A/B**: duas variantes comparadas em um experimento; no contexto da aula, são os dois prompts concorrentes, não um teste A/B de produção.  
- **N+1**: padrão de consulta ineficiente em que uma consulta inicial gera várias outras consultas adicionais.  
- **LLM**: *Large Language Model* (Modelo de Linguagem de Grande Porte).  
- **LLM as a judge**: uso de um modelo de linguagem como juiz/árbitro para comparar saídas de outros modelos ou prompts.  
- **CodeReview**: revisão de código.  
- **ground truth**: referência verdadeira/definitiva usada como base de comparação em avaliação.

**Resumo**  
A aula apresenta um experimento de avaliação pairwise em que o mesmo código-fonte é analisado por dois prompts diferentes e, em seguida, uma terceira entidade — o juiz — decide qual revisão é melhor. O foco não é medir acerto absoluto contra uma resposta correta de referência, mas comparar duas perspectivas de análise sobre a mesma entrada para testar hipóteses de melhoria de prompt. O fluxo é organizado no LangSmith, que serve para registrar dataset, prompts, execuções e o resultado da decisão.

Os dois prompts são versões com objetivos distintos: um é orientado a performance e procura problemas como N+1, memory leak, blocking e timeouts ausentes; o outro é orientado a segurança e valida findings sob a ótica de vulnerabilidades. A ideia não é comparar estilo de escrita, mas o efeito de instruções diferentes sobre a qualidade do code review produzido. Assim, o experimento isola a mudança de prompt como variável principal.

Para decidir entre as respostas, a aula usa o conceito de LLM as a judge. O juiz recebe três elementos por caso — código-fonte, resposta A e resposta B — e faz uma verificação objetiva com critérios explícitos. Se identificar vulnerabilidades críticas reais, escolhe A; se identificar problemas críticos reais de performance, escolhe B; se ambas as respostas tiverem mérito equivalente, o resultado pode ser empate. Esse empate é tratado como resultado válido, não como falha do processo.

A execução descrita segue uma sequência prática: subir o dataset, criar os dois prompts no LangSmith, rodar as duas variantes sobre as mesmas entradas e enviar as saídas ao juiz. Depois, o resultado de cada item pode ser agregado para orientar uma nova iteração. A aula também destaca o uso de `updatePrompt` como forma de representar uma hipótese de melhoria: após comparar A e B, altera-se um dos prompts e repete-se o experimento para verificar se a distribuição de vitórias muda a favor da versão atualizada.

**Pontos de atenção**  
- Não confundir **prompt A/B** com **teste A/B de produção**; aqui a comparação é offline e técnica.  
- O experimento não mede **ground truth absoluto**, mas sim julgamento relativo entre duas saídas.  
- O juiz precisa de **critérios claros, auditáveis e objetivos**; preferência vaga compromete a avaliação.  
- O juiz deve analisar o **código real** e o **impacto dos problemas encontrados**, não apenas a forma do texto.  
- O resultado **tie/empate** é válido e deve ser aceito quando as respostas tiverem mérito equivalente.  
- Forçar um vencedor em casos equivalentes adiciona ruído e piora a qualidade da avaliação.  
- Os dois prompts devem ser avaliados com a **mesma entrada/dataset**, para isolar o efeito da instrução.  
- Cada prompt representa uma **política de revisão** diferente: um prioriza performance, o outro segurança.  
- `updatePrompt` deve ser tratado como **hipótese de melhoria**, não como edição aleatória.  
- Observar a **frequência de empates** também é útil, pois pode indicar pouca diferença real entre as versões.  
- O uso do LangSmith ajuda a manter o processo **reprodutível e rastreável**, o que é essencial para iteração controlada.