Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16935)

## Resumo da aula

Summary Evaluator agrega os resultados de vários registros em uma métrica consolidada do experimento, em vez de expor apenas avaliações isoladas por item. Isso é útil quando a decisão depende do comportamento global do prompt sobre o dataset, como no code review com precision, recall e F1. No LangSmith, essa abordagem permite ler rapidamente o perfil de cada política de prompt sem inspecionar manualmente os 10 exemplos. O valor agregado não substitui auditoria detalhada, mas acelera a comparação operacional entre variantes.

Retomando o cenário de code review em Go, a variável experimental continua sendo o prompt: conservador, agressivo ou balanceado. O script carrega o prompt escolhido, reutiliza uma função compartilhada para conectar inputs, LLM e integração com OpenAI via LangSmith, e extrai do ground truth os expectedFindings com tipo e severidade. Esses dados alimentam extractExpected e a função de cálculo de PrecisionRecallF1, que consolida os acertos e erros do experimento. A execução é disparada com evaluate, que roda o modelo sobre o dataset e registra os resultados no LangSmith.

No experimento conservador, a leitura agregada mostrou precision muito alta, recall muito baixo e F1 baixo. Esse padrão indica um sistema seletivo: ele evita emitir alertas errados, mas deixa passar muitos bugs reais. Operacionalmente, isso faz sentido quando o custo de investigar falsos positivos é alto, mas se torna inadequado quando cobertura é prioridade. O ponto principal não é o número isolado, e sim o formato do comportamento que ele revela.

No experimento agressivo, o código permanece igual e apenas o prompt muda, o que isola a causa da diferença nas métricas. O resultado observado foi o inverso do conservador: precision baixa, recall mais alto e F1 ainda baixo. Isso mostra uma política mais permissiva, que recupera mais casos reais ao custo de introduzir mais ruído. A comparação lado a lado deixa explícito o trade-off já conhecido entre cobertura e confiabilidade dos alertas.

O prompt balanceado produziu um F1 significativamente maior do que os outros dois, porque reduziu o desequilíbrio entre precision e recall. Ele não maximizou nenhuma métrica isoladamente, mas entregou uma combinação mais útil para comparação global. Quando o objetivo é escolher uma política geral de revisão, esse tipo de resultado costuma ser mais valioso do que extremos com uma métrica excelente e outra muito degradada. O F1, aqui, funciona como critério de ordenação prática entre políticas concorrentes.

Resultados com LLMs não são perfeitamente estáveis, mesmo quando a estrutura do experimento parece idêntica. Mudanças de momento de execução, versão de modelo ou pequenas variações internas de geração podem deslocar as métricas observadas. Por isso, um único run não deve ser tratado como verdade definitiva sobre a qualidade do prompt. A leitura correta é probabilística: o experimento sugere tendência, não certeza absoluta.

Confiabilidade experimental exige repetir o mesmo experimento mais de uma vez e usar datasets maiores. Repetição ajuda a distinguir padrão consistente de flutuação ocasional do modelo, enquanto mais exemplos reduzem a influência desproporcional de casos individuais sobre a média agregada. Com apenas 10 registros, pequenas mudanças já alteram bastante precision, recall e F1. A decisão de produto fica mais segura quando o comportamento se mantém sob repetição e em amostras mais amplas.

A interface do LangSmith permite acompanhar iterações, execuções e métricas resumidas do experimento sem entrar registro por registro. Isso acelera a comparação entre versões como conservative, aggressive e balanced, especialmente quando o objetivo é decidir qual política seguir. Ainda assim, a leitura agregada só é confiável porque o dataset, o ground truth e o pipeline de extração permanecem constantes entre os testes. Sem esse controle, diferenças numéricas poderiam refletir mudança nos dados, e não no prompt.

## Transcrição

00:00

Bom, pessoal, agora que a gente entendeu um pouco das métricas, a gente vai começar a executar as coisas, tá? Somente pra você ver.

00:09

Tenho três arquivos. Um arquivo que usa a parte mais conservadora, o mais agressivo, e o outro mais balanceado. Então, esse foi o nosso objetivo, usar aqueles prompts. Somente para passar rapidamente aqui pelo script, depois você pode ver com calma. Mas, basicamente, o que eu faço é... Eu carrego o prompt que eu quero, nesse caso, que é o mais conservador,

00:32

Eu tenho essa função aqui que ela está compartilhada num pacote shared, que basicamente ela pega o prompt, pega os inputs que a gente vai passar, a gente pega a conexão com o LLM e tem um wrap em volta da OpenAI com o Langsmith, e aqui é o código do JSON que ele vai olhar, a chave do JSON que ele vai olhar, que é basicamente essa chave aqui.

01:01

E aí a gente vai fazer, no final das contas, uma extração que a gente vai pegar todos os exemplos que existem do nosso Ground Truth para garantir que a gente possa fazer aquela comparação, ou seja,

01:16

esse expected findings, tá vendo? A gente inicializa ele com nada, e depois a gente começa a colocar o tipo e o grau de severidade, vamos dizer assim, né? E uma vez que a gente tem esse findings, a gente utiliza esse findings aonde, inclusive? A gente acaba

01:36

tendo essa função, que é o ExtractExpect, que a gente vai usar para calcular o PrecisionRecallUF1, que é exatamente aquela função que eu mostrei para vocês que tem a fórmula. E agora, no final das contas, o que vai acontecer? Eu vou dar um Evaluate, ou seja, chamando o LangSmith,

01:53

pedindo para ele rodar a minha análise, ou seja, isso aqui vai fazer a chamada do meu LLM, e se você olhar aqui, ele está executando o prompt com aqueles parâmetros que eu falei. Se você olhar agora aqui também, tem Evaluators. E se você olhar, o Evaluators está em branco. Mas por que está em branco? Porque nesse nosso caso, a gente está usando o Summary Evaluators. Eu não sei se você lembra, mas quando a gente estava falando de tipos,

02:20

de evaluators, a gente falou LLMS Judge, a gente falou Code Evaluator, a gente falou de pairwise e a gente falou de Summary Evaluator, que é quando eu pego diversos registros e agrego uma métrica só ali no nosso caso, coloquei um prefixo concorrente para ele fazer um pouco mais rápido, e aqui, no final das contas, a gente vai fazer a execução. Acredito que o dataset já fiz o upload, então eu vou dar aqui um 2 precision e vou colocar um conservative precision.py.

02:51

e vamos botar esse cara aqui para ser executado a gente vai ter que...

02:56

aguardar um pouquinho, mas enquanto isso dá pra gente ir entrando aqui no nosso Langsmith, tá? No nosso Langsmith, deixa ele carregar, vou aumentar aqui a tela, você vai perceber que eu tenho aqui pra gente agora um dataset, e dentro desse dataset que a gente tem, a gente tem aquele Evaluation Precision, que é o dataset que a gente tem.

03:21

E agora, se você olhar, eu tenho o quê nesse nosso caso? Eu tenho o experimento que eu fiz, que é conservador. Deixa eu voltar aqui para ficar melhor. Eu tenho a quantidade de repetições, eu tenho F1 de 0,22.

03:38

uma precisão extremamente alta, mas o recall extremamente baixo. O que significa? Que provavelmente aqui a gente focou muito em precisão. Ou seja, a gente pegou praticamente todos os bugs que tinham, mas junto com isso a gente trouxe um monte de bug que não era bug. Então, esse aí foi o nosso problema em relação a medir a precisão. Então, perceba aqui, pessoal, que eu não preciso ficar necessariamente entrando

04:05

registro por registro, eu consegui pegar isso de uma forma resumida, ou seja, esse 0.22, esse 1 e esse 0.13, ele é o resultado do resumo de todos os 10 exemplos do nosso dataset. Então, essa que é a nossa ideia aqui. Da mesma forma que a gente tem isso, eu tenho o aggressive, que ele vai fazer exatamente o que a gente fez, o código é exatamente o mesmo, a única coisa que vai mudar é o prompt novamente. Então, eu vou botar aqui para rodar,

04:35

o nosso exemplo 2, que ele é o mais agressivo aqui. Então, vamos botar esse cara aqui para rolar. Bom, a gente só tem 10 registros no dataset, então provavelmente a execução dele vai ser mais rápida aqui. Vamos entrar aqui no nosso langsmith para que a gente consiga ir olhando como que ele vai se comportando esse nosso camarada aqui para a gente.

04:58

Então, já dá para perceber que ele está subindo aqui a parte de Aggressive, aqui para a gente ver, e agora a gente tem que aguardar os cálculos sendo feitos. Então, a gente vai aguardar mais alguns segundinhos até o resultado. Deixa eu só olhar aqui novamente. Então, a gente passou pela sétima iteração, a gente tem que passar por dez iterações para que ele consiga olhar todos os dados do nosso dataset, aqui nesse nosso caso.

05:26

Beleza? Então, gerou aqui. Vamos ver como está aqui no nosso LangSmith. Então, olha só aqui. Vamos verificar. Vamos aguardar ele carregar mais um pouco. Vamos ver se ele...

05:40

Se ele ainda vai atualizar, deixa eu dar um F5, mas aqui a gente já consegue ver um resultado claro na realidade, tá? Se você olhar, o nosso F1 é baixo, a nossa precisão aqui está muito baixa. Perceba que nesse exemplo mais conservador, ou seja, onde ele tinha que achar tudo que era de previsão, ele acertou todas. Em relação à precisão agora aqui, ele caiu muito essa nossa taxa de precisão.

06:06

Por outro lado, o recall dele foi maior. Então, se você olhar aqui, precisão alta. Se você olhar aqui, recall baixo. Se você olhar aqui, precisão baixa e o recall aqui mais alto. E o mais interessante de tudo aqui, nesse caso, é que eu tenho o F1, que é o equilíbrio dos dois. Esses dois estão equilibrados, por outro lado,

06:27

a prioridade e a forma como eles estão balanceados são de uma forma um pouco mais contrária, um focado mais em precisão e outro mais focado em relação à parte de recall. Agora, o que eu vou fazer? Eu vou executar o nosso último aqui, que em tese ele vai estar mais balanceado. E lembrando, pessoal, quando a gente está falando com o IA,

06:51

Tudo que eu estou colocando aqui vai depender do momento, do modelo, de tudo que a gente está fazendo. Então, provavelmente, em outros momentos eu consegui executar, os resultados foram um pouco diferentes. Tem casos que os executados...

07:06

Os casos executados são mais parecidos. E por isso que, muitas vezes, é super importante que você repita mais vezes o mesmo experimento, porque daí você consegue ter um pouquinho mais apurado em relação a isso. Vamos ver agora esse cara aqui, o balanceado. Olha só que interessante, pessoal. O resultado desse cara já foi diferente. Se você perceber, o nosso F1 aqui praticamente foi o dobro do F1 dos outros. Por quê?

07:35

ele balanceou um pouco mais de precisão, ou seja, enquanto aqui tinha 1 de precisão e aqui tinha 0.1, aqui foi 0.64. Enquanto que aqui tinha um recall de 0.38, o recall aqui foi de 0.29.

07:52

Então, você começa a perceber que teve um balanço um pouco maior. Se você olhar aqui, a precisão está muito maior do que necessariamente o recall. Mas, de qualquer forma, quando a gente olha, a gente consegue perceber claramente o balanço que a gente acabou tendo entre F1 e também entre recall e precision aqui para a gente.

08:18

Vale a pena executar várias vezes e outra coisa, né? É super importante pegar um dataset grande, porque um dataset maior você consegue explorar muito mais opções, tá? Mas a ideia era gerar três prompts para vocês verem como que o prompt consegue mudar claramente o que é precisão, o que é recall e, naturalmente, acaba mudando bastante em relação ao F1.

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model*  
- **JSON** — *JavaScript Object Notation*  
- **F1** — Métrica F1, média harmônica entre precisão e recall  
- **Precision** — Precisão  
- **Recall** — Revocação ou sensibilidade  
- **Evaluate** — Avaliação/execução de um experimento no LangSmith  
- **LangSmith** — Plataforma de observabilidade e avaliação de aplicações com LLMs  
- **OpenAI** — Empresa e API/modelos de IA usados na integração mencionada  
- **Ground Truth** — Conjunto de respostas esperadas usadas como referência  

**Resumo**  
A aula demonstrou como usar o LangSmith para executar e comparar experimentos de avaliação em um cenário de code review em Go, variando apenas o prompt entre três políticas: conservadora, agressiva e balanceada. O instrutor explicou que o objetivo não era olhar resultados isolados, mas consolidar os registros do dataset em métricas agregadas por meio de um Summary Evaluator, permitindo uma comparação prática do comportamento global de cada prompt. O fluxo do script consiste em carregar o prompt escolhido, reutilizar uma função compartilhada para conectar inputs, LLM e integração com OpenAI via LangSmith, extrair do ground truth os *expected findings* com tipo e severidade, passar esses dados para a extração e depois calcular Precision, Recall e F1. Em seguida, a função `evaluate` dispara a execução do modelo sobre o dataset e registra os resultados no LangSmith.

Na comparação dos experimentos, o prompt conservador apresentou precisão muito alta, mas recall muito baixo, indicando um comportamento seletivo: evita falsos positivos, porém perde muitos casos reais. Já o prompt agressivo mostrou o inverso, com precisão baixa e recall mais alto, recuperando mais bugs reais ao custo de maior ruído. O prompt balanceado foi o que obteve melhor F1, porque equilibrou melhor precisão e recall, sendo mais útil para decisão global do que extremos com uma métrica isolada excelente e outra muito degradada. O instrutor também destacou que resultados com LLMs não são totalmente estáveis, pois podem variar conforme momento de execução, versão do modelo e pequenas diferenças internas de geração, então um único run não deve ser tratado como verdade definitiva. Por isso, recomendou repetir experimentos e usar datasets maiores para obter conclusões mais confiáveis. Ao final, reforçou que a leitura agregada no LangSmith acelera a comparação entre variantes, mas só é válida quando dataset, ground truth e pipeline de extração permanecem constantes.

**Pontos de atenção**  
- O **Summary Evaluator** agrega resultados e acelera a leitura, mas **não substitui auditoria detalhada** dos exemplos individuais.  
- O **prompt é a variável experimental principal**; o restante do pipeline deve permanecer igual para isolar corretamente a causa das diferenças.  
- **Precisão alta com recall baixo** indica um modelo conservador: poucos falsos positivos, mas muitos casos reais perdidos.  
- **Recall alto com precisão baixa** indica um modelo agressivo: mais cobertura, porém com mais ruído.  
- **F1** é útil para comparar políticas globais porque equilibra precisão e recall, mas não deve ser interpretado isoladamente sem entender o trade-off.  
- Resultados com LLMs **não são perfeitamente estáveis**; um único experimento pode refletir flutuação momentânea e não o comportamento real do prompt.  
- É importante **repetir o mesmo experimento várias vezes** para verificar consistência.  
- **Datasets pequenos** tornam as métricas mais sensíveis a pequenas variações; amostras maiores dão conclusões mais confiáveis.  
- Manter **dataset, ground truth e extração constantes** é essencial para que a comparação entre prompts seja válida.  
- A leitura no LangSmith fica mais útil quando se observa o **perfil agregado do experimento**, e não apenas valores pontuais de um run.