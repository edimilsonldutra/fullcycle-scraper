Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16939)

## Resumo da aula

Otimizar prompt com evidência exige tratar a mudança como uma nova versão do mesmo artefato, não como um experimento informal. Aqui, o prompt A evolui de Security Expert V1 para Security Expert V2, ampliando o escopo de análise: em vez de olhar apenas segurança, a nova versão também considera performance. Essa mudança altera a política de inspeção do modelo e, por isso, pode deslocar o placar pairwise mesmo sem mudar mais nada no pipeline.

Commits do prompt funcionam como trilha de auditoria do experimento. Eles permitem comparar a versão anterior com a atual e responder exatamente o que mudou entre uma execução e outra. Quando o prompt é alterado no LangSmith, a comparação deixa de ser “prompt antigo versus prompt novo criado manualmente” e passa a ser “versão anterior versus versão atual do mesmo artefato”, o que melhora rastreabilidade e reduz ambiguidade.

Uma comparação entre versões só é tecnicamente válida quando o restante do experimento permanece constante. Retomando o cenário pairwise já conhecido, o script continua o mesmo, o dataset continua o mesmo e o juiz continua o mesmo; a única variável alterada é o prompt. Esse isolamento é o que permite atribuir a mudança no resultado à nova instrução, e não a diferenças de implementação, dados ou critério de julgamento.

Manter o dataset constante garante que as duas versões enfrentem exatamente os mesmos casos. Manter o juiz constante preserva a mesma régua de decisão entre as execuções, evitando que uma mudança no avaliador contamine a leitura do placar. Sem esses dois controles, a comparação entre versões perde valor experimental, porque o resultado passa a misturar múltiplas causas.

Quando apenas o prompt muda, a validação correta é rerodar exatamente o mesmo script. Isso preserva o pipeline operacional e transforma a execução em um teste de hipótese simples: “a nova versão do prompt vence mais do que a anterior?”. A referência breve ao pairwise basta aqui: as duas saídas continuam sendo comparadas caso a caso sob a mesma estrutura já estabelecida.

O placar muda de um cenário equilibrado, 5,5 vs 4,5, para uma vantagem mais clara, 8 vs 2. Essa diferença sugere que a nova versão do prompt A passou a produzir respostas que o juiz prefere com mais frequência sob o mesmo critério. O ponto central não é apenas “ganhou”, mas “ganhou mais depois da alteração controlada”, o que transforma refinamento de prompt em evidência mensurável.

Uma vitória maior não prova que o prompt ficou universalmente melhor em qualquer contexto; ela prova que, sob aquele dataset, aquele juiz e aquele critério, a nova versão teve desempenho superior. Essa leitura é mais robusta do que uma impressão subjetiva, porque está ancorada em comparação controlada. Em engenharia de prompts, melhoria útil é melhoria reproduzível nas mesmas condições de teste.

Melhorar qualidade não encerra a decisão técnica. Um prompt mais elaborado pode consumir mais tokens, aumentar latência e elevar custo por execução, então o ganho no placar precisa ser lido junto com o custo operacional. A escolha correta depende do contexto: em alguns casos, uma versão menos precisa, mas significativamente mais barata, entrega melhor relação custo-benefício do que a vencedora absoluta.

Retomando o experimento já montado no LangSmith, o fluxo fica simples: atualizar o prompt versionado, manter dataset, script e juiz inalterados, rerodar A e B e comparar o novo placar agregado. Em seguida, inspecionar tokens e custo para verificar se a melhoria compensa financeiramente. Esse processo transforma iteração de prompt em ciclo auditável de hipótese, execução e decisão.

## Transcrição

00:01

Bom pessoal, no vídeo anterior a gente teve essa pegada aqui, o prompt A ganhou do prompt B, baseado com os critérios que a gente passou para o nosso juiz, legal? Agora, o que eu vou fazer? Eu vou executar novamente esse cara, mas olha só o que eu vou fazer, eu vou dar um update

00:20

prompt v2 e vou dar um enter aqui para o nosso prompt ele ser alterado. O que acontece? Esse nosso prompt v2, o que ele tem aqui? Antes eu tinha o security expert v1

00:38

E agora, o que eu tenho? Eu tenho o Security Expert V2. E o Security Expert V2 também consegue verificar vulnerabilidade de segurança e problemas de performance. Ou seja, analise o código, e aí eu trouxe instruções para ele verificar a segurança.

00:57

E também falei em relação à parte de performance. Então, agora ele está com um viés de dois aspectos, segurança e performance. Um, antes ele era só segurança, depois ele era só performance.

01:12

o outro é só performance. Agora, esse terceiro é segurança e performance. E lembre-se, eu não criei um novo prompt, eu alterei o prompt que a gente tinha lá no Langsmith. Então, esse é um ponto importante somente para você saber. E vamos ver se o resultado tem alguma mudança, um pouco de diferença agora. Como que eu vou fazer agora?

01:36

Eu só mudei o prompt, então eu vou rodar exatamente o mesmo script que eu fiz aquela vez. E nós vamos aguardar agora, tem que aguardar mais aquele pontinho aqui. Enquanto a gente está aguardando ele rodando aqui, eu quero mostrar aqui para vocês o nosso prompt.

01:56

E olha só, aqui tem o prompt que tem dois commits, se você olhar, tá vendo? Então, esse cara aqui é o prompt mais novo que a gente tem. Ou seja, a gente fez modificação nesse nosso prompt e a versão dele antes era assim.

02:18

E agora, a versão atual é assim. Então, essa mudança de prompt em tese, de alguma forma, vai fazer o resultado do nosso experimento mudar. Em tese, a gente tem que ganhar, o A tem que ganhar com uma vantagem maior ainda do que com o B aqui nesse nosso caso. Então, somente para a gente lembrar qual que é o nosso ponto, a gente está realmente

02:46

fazendo e fazendo essa verificação. Deixa eu ver se ele já rodou. Ainda não rodou, ele está fazendo a evaluação do pairwise B, ou seja, ele está aqui no nosso prompt B ainda, e aí ele vai fazer ainda a verificação do juiz, fazendo a comparação dos dois agora aqui. Essa aí, o que acaba sendo

03:14

mais rápida, porque ele vai rodar apenas duas vezes. Ele não precisa rodar o dataset inteiro mais. Então, agora a gente já tem a nossa comparação. Vamos voltar agora aqui no nosso ParallelWise, e agora a gente tem quatro experimentos. O primeiro experimento foi da primeira à segunda vez, e o segundo experimento roda o A e B de novo, mas o interessante

03:41

é que a gente vai ver a comparação agora desses caras. Então, olha só que interessante, pessoal. Quando eu melhorei o prompt ainda da versão A, ele saiu de 5,5 para 8, versus 2, onde aqui era 5,5, 4,5, estava muito parecido, mas agora as coisas já mudaram um pouco mais de figura, tá? Então, isso aí é algo realmente super importante, pessoal.

04:10

porque a melhor forma de você comparar prompt é colocar realmente um do lado do outro com a mesma entrada e também existem outros aspectos também que a gente tem que verificar. Quantos tokens esse prompt gastou? Quanto custou tudo isso? Será que esse ganho de performance no final das contas, esse ganho dessa melhoria, valeu a pena em relação à parte financeira? Até que ponto eu posso ter um prompt que

04:37

ele, apesar de não ser tão preciso, resolve um problema e isso fica muito mais barato para mim. Então, a gente tem esses aspectos aqui também. Beleza?

## Resumo IA

**Abreviações**
- **V1** — Version 1 (Versão 1)
- **V2** — Version 2 (Versão 2)
- **A/B** — Versão A e Versão B do experimento comparativo
- **pairwise** — Comparação par a par entre duas saídas/versões
- **LangSmith** — Ferramenta/plataforma da LangChain para observabilidade, avaliação e versionamento de prompts e experimentos

**Resumo**
A aula mostrou como otimizar prompts com evidência, tratando cada alteração como uma nova versão do mesmo artefato, e não como um teste informal. O instrutor partiu do cenário em que o prompt **Security Expert V1** foi atualizado para **Security Expert V2**, ampliando o escopo de análise de segurança para incluir também performance. A ideia central é que essa mudança de instrução pode alterar o comportamento do modelo e, consequentemente, o resultado do experimento pairwise, mesmo sem modificar o restante do pipeline.

Foi destacado que os **commits do prompt** no LangSmith funcionam como trilha de auditoria, permitindo comparar claramente a versão anterior com a atual e entender exatamente o que mudou. Para que a comparação tenha validade técnica, o restante do experimento precisa permanecer constante: mesmo script, mesmo dataset e mesmo juiz. Com isso, o teste passa a isolar a variável “prompt”, permitindo atribuir a mudança no placar à nova instrução, e não a diferenças nos dados, na implementação ou no critério de avaliação.

No fluxo prático, o instrutor explicou que, ao alterar apenas o prompt versionado, deve-se rerodar exatamente o mesmo script. A comparação pairwise então é refeita sob as mesmas condições, e o novo placar agregado mostra a evolução do prompt A de um resultado equilibrado para uma vitória mais clara. O ponto enfatizado é que a melhoria precisa ser interpretada de forma controlada: ela vale para aquele dataset, aquele juiz e aquele critério, não como garantia universal. Por fim, a aula reforçou que a decisão técnica não deve considerar só a qualidade da resposta, mas também o custo operacional, incluindo tokens consumidos, latência e custo financeiro, já que um prompt mais sofisticado pode ser melhor em desempenho e pior em custo-benefício.

**Pontos de atenção**
- Tratar atualização de prompt como **nova versão versionada**, não como experimento solto.
- Usar **commits** ou histórico no LangSmith para rastrear exatamente o que mudou entre execuções.
- Manter **dataset, script e juiz constantes**; qualquer variação nesses elementos invalida a comparação direta.
- Atribuir a diferença de resultado **somente à mudança do prompt** quando o restante do pipeline foi preservado.
- Entender que melhoria no placar é **contextual**: vale para aquele conjunto de testes, não para qualquer cenário.
- Não olhar apenas para acurácia/placar; medir também **tokens, latência e custo**.
- Considerar que um prompt mais “forte” pode ser **mais caro** e, em alguns contextos, uma versão mais barata pode ter melhor relação custo-benefício.
- Reexecutar o **mesmo script** para garantir reprodutibilidade e comparar versões de forma justa.
- Interpretar o resultado pairwise como **evidência experimental controlada**, não como prova absoluta de superioridade universal.