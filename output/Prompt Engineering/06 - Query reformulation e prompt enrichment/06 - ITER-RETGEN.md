Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16750)

## Resumo da aula

Antes de partirmos para a prática e eu mostrar alguns exemplos interessantes, quero falar sobre uma técnica chamada Iter-RetGen. Basicamente, esta é uma técnica extremamente interessante que você pode usar para expandir o contexto da pergunta do usuário. É uma técnica bem utilizada, e vou mostrar isso na prática. Acredito que vale a pena entender este tipo de exemplo.

A ideia é ter um loop iterativo que alterna entre geração e recuperação. Ou seja, eu gero um rascunho e, depois, uso esse rascunho para buscar, de forma mais específica, as informações que vão me ajudar.

O passo a passo funciona assim:

Primeiramente, eu gero um rascunho com Missing Markers. Missing Markers são como lacunas dentro do texto. Vamos imaginar que eu vou fazer uma pergunta sobre a linguagem Python. Eu posso colocar: "A última versão da linguagem Python é [MISSING]". Em vez de colocar a versão, coloco um marcador indicando que está faltando. Depois, posso colocar: "Python foi criado por [MISSING]".

Quando eu gero esse documento com partes faltando, posso avançar para a próxima etapa: gerar perguntas baseadas no contexto do que está faltando. A partir dessas perguntas, posso buscar respostas e, com essas respostas, substituir os marcadores pelas informações corretas ou expandidas.

Sei que pode parecer confuso, mas vai fazer sentido. Basicamente, eu gero um rascunho com marcadores indicando informações faltantes. Depois, pego essas informações faltantes e as transformo em perguntas para realizar uma busca. Com a lista de perguntas, faço a pesquisa e obtenho as respostas. Com essas respostas, reescrevo o rascunho inicial e verifico se ainda há algo pendente. Se houver, repito o processo: faço novas perguntas, busco respostas e, ao obtê-las, gero a versão final, substituindo as partes importantes que precisavam ser expandidas.

A ideia principal é criar um rascunho com pedaços de informação faltando, gerar perguntas para obter essas informações e, com as respostas, substituir as lacunas. Isso é muito interessante porque, às vezes, temos uma pergunta extremamente vaga e queremos uma resposta extremamente completa, o que é difícil para a IA fazer. Com este loop, a quantidade de informação relevante que você pode trazer é impressionante.

Separo isso em quatro categorias: Draft, Query, Fill e Expansion. O processo funciona assim:

Tenho o input do usuário, que pode ser uma pergunta aberta ou ruim.

Pego essa pergunta e gero um draft de resposta, mas neste draft o prompt será provocativo, instruindo a verificar especialidades, trazer informações específicas, e onde não houver certeza, substituir por [MISSING].

Em seguida, tudo que está marcado como [MISSING] é usado para gerar perguntas.

Com as perguntas, faço uma busca, obtenho as respostas e gero a resposta completa para o usuário final.

Se houver pouca interação, ou seja, se apenas algumas perguntas foram geradas, posso fazer uma expansão adicional, criando mais Missing Markers, gerando mais perguntas, obtendo mais informações e produzindo uma resposta final ainda mais completa.

Essa é a ideia principal ao trabalhar com Iter-RetGen. Nos próximos vídeos, veremos exemplos práticos de código para entender como criar esse tipo de comportamento na IA.

## Transcrição

00:01

E agora, pessoal, antes da gente ir pra prática e eu mostrar alguns exemplos interessantes pra você, eu quero falar de esse camarada que é chamado de Iter.

00:11

RetGen. Basicamente, essa é uma técnica extremamente interessante e que você pode usar muito para conseguir expandir o contexto da pergunta do usuário. É uma técnica bem utilizada mesmo, e eu vou mostrar, inclusive, isso na prática para você. Eu acho que esse tipo de exemplo vale a pena você entender. Então, qual que é a ideia aqui? É a gente ter um loop iterativo que alterna entre a geração e recuperação.

00:41

O que significa? Eu vou gerar um rascunho e, depois, eu uso esse rascunho para buscar, de forma mais específica, as informações que vão me ajudar. Então, como é que funciona esse passo a passo aqui?

00:54

Primeiramente, eu vou gerar um rascunho com Missing Markers. O que isso significa? O que é um Missing Markers? É como se fossem lacunas dentro do meu texto. Então, vamos imaginar o seguinte. Imagina que eu vou fazer uma pergunta sobre a linguagem Python. Eu posso colocar, a última

01:16

a versão da linguagem Python, e aqui, ao invés de eu colocar a versão, eu coloco aqui, Missing, por exemplo, está faltando, tá? Sendo que, daí eu coloco aqui, sendo que o Python foi criado por

01:41

E aqui eu tenho Missing. E aí, o que acontece? Quando eu gero esse documento com essas partes faltando, o que eu posso fazer? Eu posso ir para uma etapa e fazer o seguinte. Gere perguntas para mim baseadas no contexto

02:04

do que está faltando, ou o que está no missing. E aí eu vou ter diversas perguntas que eu vou gerar. E a ideia dessas perguntas é eu responder essas perguntas e com a resposta dessa pergunta eu

02:21

trocar ou substituir esse cara aqui pela resposta correta ou que eu expandi, tá? Eu sei que pode parecer um pouco confuso, mas vai fazer sentido aqui pra você. Então, basicamente, eu vou gerar um rascunho onde vai ter, né, marcadores ali pra mim falando que eu tenho informações faltando.

02:39

Aí, o que eu vou fazer? Eu vou pegar essas informações faltando e vou fazer isso como uma pergunta, para que isso vire uma busca para mim. Aí, uma vez que eu tenho essa lista dessas perguntas que estão faltando, eu vou fazer a pesquisa realmente das respostas dessas buscas. E agora que eu tenho essas respostas dessa busca, o que eu vou fazer? Eu vou reescrever a resposta do meu rascunho inicial,

03:09

E vou verificar se tem mais alguma coisa pendente. Se tiver pendente, eu faço a busca de novo, tento fazer a pergunta, tento conseguir a resposta. Se eu conseguir a resposta, eu gero a minha versão final, substituindo aquelas partes

03:26

que são importantes ou que eu poderia expandir ou não. Então, a ideia principal é criar um rascunho com pedaços de informação faltando, você fazer perguntas para conseguir a resposta dessas informações faltando. Quando você tem essas respostas, você pega aquele rascunho e substitui aquelas partes faltando pelas respostas que você conseguiu. Então, isso aí é muito interessante porque, às vezes, a gente tem uma pergunta extremamente vaga

03:55

e a gente quer uma resposta extremamente completa.

04:00

E isso é muito difícil para IA fazer. Com esse loop aqui, é impressionante a quantidade de informação relevante que você pode trazer em relação a isso. Então, basicamente, eu separo isso por quatro partes, quatro categorias. Um é chamado de Draft, outro Query, outro Fill e outro Expansion. Então, a ideia é a seguinte. Eu tenho aqui o input do usuário, onde ele faz uma pergunta

04:29

aberta, ou uma pergunta ruim. E o que eu faço aqui? Eu pego essa pergunta e gero um draft de uma resposta, mas nesse draft, o meu prompt vai ser provocativo. E essa provocação vai ser, verifique se isso tem alguma especialidade, traga isso, traga aquilo e etc. E o que você não tiver certeza, substitua por missing. Basicamente isso.

04:57

E aí, o que ele faz? Ele pega tudo que está com Missing e gera perguntas disso aí. E agora que eu tenho as perguntas, eu faço uma busca, pego as respostas e gero a resposta completa para o usuário final. Se você quiser, eu fiz isso, caso eu tenha pouca interação, ou seja, ele gerou apenas duas perguntinhas, uma perguntinha faltante ali, eu posso fazer mais uma expansão ainda,

05:24

para que ele tenha mais Missing Markers, para ele fazer mais perguntas, para ter mais informação, para gerar a resposta final ainda mais completa. Então, essa que é a ideia principal quando a gente está trabalhando com esse camarada aqui. Então, nos próximos vídeos, a gente vai ver um pouco mais de código para você entender como que a gente consegue criar esse tipo de comportamento na IA.

## Resumo IA

**Abreviações**  
- **Iter-RetGen**: *Iterative Retrieval Generation* (geração iterativa com recuperação).

**Resumo**  
A aula apresentou a técnica Iter-RetGen, um fluxo iterativo usado para expandir o contexto de uma resposta a partir de perguntas do usuário. A proposta central é alternar entre geração e recuperação: primeiro, o modelo cria um rascunho de resposta com lacunas explícitas, chamadas de **Missing Markers**; depois, essas lacunas são convertidas em perguntas específicas; em seguida, realiza-se a busca pelas respostas; por fim, o rascunho é reescrito com as informações recuperadas. O instrutor destacou que essa abordagem é especialmente útil quando a pergunta inicial é vaga ou incompleta e, mesmo assim, deseja-se produzir uma resposta mais completa e relevante.

O fluxo foi dividido em quatro etapas: **Draft**, **Query**, **Fill** e **Expansion**. Em **Draft**, a entrada do usuário é usada para gerar uma resposta provisória, com instruções no prompt para que o modelo identifique especialidades, detalhe o que for possível e marque incertezas como `[MISSING]`. Em **Query**, cada item marcado como faltante é transformado em perguntas. Em **Fill**, essas perguntas são pesquisadas e respondidas, permitindo substituir os marcadores pelo conteúdo correto. Por fim, em **Expansion**, caso ainda haja pouca informação ou poucas interações geradas, o processo pode ser repetido para criar novos marcadores, novas perguntas e uma resposta final ainda mais rica. O objetivo é aumentar progressivamente a qualidade da saída da IA por meio de um loop de refinamento e busca direcionada.

**Pontos de atenção**  
- O método é mais útil quando a entrada do usuário é vaga, ampla ou mal formulada.  
- Os **Missing Markers** devem ser usados de forma explícita para sinalizar lacunas que precisam ser recuperadas.  
- As perguntas geradas a partir do rascunho devem ser específicas e guiadas pelo contexto do que está faltando.  
- Depois de preencher as lacunas, é importante revisar se ainda restou informação pendente antes de finalizar.  
- O processo pode ser repetido em ciclos de **expansão** para enriquecer ainda mais a resposta.  
- O uso do prompt deve ser provocativo e orientado a extrair detalhes, especialidades e informações que o modelo não tenha certeza.  
- A técnica busca equilibrar resposta ampla com precisão, evitando que a IA invente informação quando houver incerteza.