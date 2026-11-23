Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16570)

## Resumo da aula

Escrever um prompt melhor não significa sempre adicionar mais contexto. Informação em excesso pode introduzir ruído, ambiguidade ou restrições desnecessárias, o que piora a resposta em vez de melhorá-la. A qualidade da saída depende da relação entre objetivo, contexto útil e forma de instrução. Em Prompt Engineering, estrutura relevante costuma valer mais do que volume de texto.

Retomando a ideia de tipos e técnicas de prompts já apresentada, o ponto novo aqui é a justificativa para estudá-los como repertório técnico. Essas técnicas surgem porque tarefas diferentes exigem formas diferentes de orientar o modelo, e essa diferença já foi observada em papers, benchmarks e comparações entre modelos. Não se trata de escrever “mais bonito”, mas de escolher uma estrutura que induza o comportamento mais adequado para cada problema. Isso transforma o prompt em decisão experimental e não em improviso textual.

Técnicas de prompt ficam abstratas demais quando são ensinadas apenas por definição. Ao executar prompts em código ou em interfaces como ChatGPT no browser, fica possível observar variação de resposta, impacto de pequenas mudanças e comportamento do modelo sob condições controladas. Essa prática torna visível o que, de outro modo, pareceria apenas recomendação subjetiva. Para desenvolvedores, esse formato aproxima o estudo de prompts da lógica de teste, comparação e inspeção de comportamento.

Rodar o mesmo prompt com pequenas alterações permite discutir o que mudou na saída e inferir o que está acontecendo por baixo do capô do modelo. O objetivo não é abrir a implementação interna da IA, mas entender efeitos observáveis da instrução sobre qualidade, foco e consistência da resposta. Esse tipo de análise ajuda a construir intuição técnica sobre quando simplificar, quando estruturar mais e quando trocar de técnica. Sem esse ciclo de execução e comparação, o aprendizado tende a ficar superficial.

Os vários tipos de prompt formam um mapa de leitura para o restante do capítulo. Como esse repertório pode confundir quando aparece apenas como lista, a abordagem correta é estudar cada técnica em uso, comparando intenção, efeito e limite prático. A primeira técnica dessa sequência é o role prompt, que muitas pessoas já usam de forma automática, mas sem avaliar claramente o impacto dessa escolha. O avanço aqui é sair do uso intuitivo e passar a observar a técnica como mecanismo deliberado de controle da resposta.

## Transcrição

00:01

Bom, pessoal, agora uma das coisas que a gente tem que ter clareza agora, iniciando realmente com o Prompt Engineering, a gente tem que entender que escrever um prompt não é somente tentar dar o nível de informação mais detalhado possível. Inclusive, muitas vezes a gente vai perceber, e eu vou mostrar com exemplos aqui para você, que às vezes dá mais informação do que a IA precisa

00:27

pode gerar mais problema e comprometer ainda mais o resultado da sua resposta, tá? Então, por isso que quando a gente está falando de Prompt Engineering, nós temos diversos tipos ou técnicas de prompts, e essas técnicas e esses tipos não foram simplesmente criados à toa. Existem muitos papers que você vê ali

00:48

de diversos formatos, com estatísticas, com diversos benchmarks e comparações de tipos de prompts, e até mesmo nos benchmarks dos próprios modelos, como é que esses prompts conseguem fazer com que a IA trabalhe ou haja ali para a gente. Então, o nosso objetivo daqui para frente, nesse primeiro momento aqui da disciplina, é entender realmente esses tipos de prompt.

01:14

Mas, na hora que eu estava pensando como é que a gente vai entender, como é que eu vou mostrar, é só texto, ou eu só vou ficar explicando o que cada um, quando usar, com limitação, eu fiquei pensando muito em como fazer isso. E eu acho que a melhor forma de mostrar e ver essas coisas acontecendo

01:35

é realmente na prática e com código, ou também, muitas vezes, com o chat GPT aberto, com o browser aberto. Então, o que eu tenho um compromisso aqui de fazer com você, principalmente nessas partes de tipos de prompts, porque são vários tipos, você acaba ficando até um pouco perdido na hora que você tem esses tipos,

01:54

E se eu só falar, eu acho que vai ser muito difícil você tangibilizar, você ver a coisa acontecendo, ainda mais quando a gente está falando de código. Então, o que eu quero trazer aqui para você também vai ser as possibilidades que nós vamos ter de olhar código,

02:14

e ficar rodando um determinado prompt e discutir um pouco mais sobre esse prompt e como que isso está acontecendo um pouco ali por baixo do capô da inteligência artificial do modelo que a gente está rodando, beleza? Então, agora, no nosso próximo vídeo, somente para esse vídeo não ficar extremamente longo, nós vamos falar sobre o nosso primeiro tipo de prompt que eu acredito que você já

02:41

Deva ter feito ou já deva ter visto acontecer, e às vezes a gente fala de faz de forma automática, mas a gente não entende necessariamente o impacto que isso pode ter na realidade, tá? Então, vamos nessa. Próximo vídeo a gente vai começar a falar de role prompt.

## Resumo IA

**Resumo**  
A aula introduz um princípio central de Prompt Engineering: escrever um prompt melhor não significa, necessariamente, adicionar mais informação. O instrutor destaca que excesso de contexto pode gerar ruído, ambiguidades e restrições desnecessárias, prejudicando a qualidade da resposta. Em vez de focar no volume de texto, a ênfase deve estar na relação entre objetivo, contexto realmente útil e forma de instrução, entendendo que a estrutura do prompt costuma ser mais importante do que sua extensão.

Em seguida, a aula justifica o estudo dos tipos e técnicas de prompt como um repertório técnico, e não apenas como dicas de escrita. Essas técnicas existem porque diferentes tarefas exigem diferentes formas de orientar o modelo, algo que já foi observado em papers, benchmarks e comparações entre modelos. Assim, o prompt passa a ser visto como uma decisão experimental: a escolha de uma estrutura pode induzir comportamentos diferentes na IA, com impacto direto na resposta gerada.

O instrutor também explica que aprender prompts só por definição tende a tornar o conteúdo abstrato e pouco útil. Por isso, propõe um aprendizado prático, executando prompts em código ou em interfaces como o ChatGPT no navegador, para observar variações de resposta, efeitos de pequenas alterações e comportamento do modelo sob condições controladas. Esse método aproxima o estudo de prompts de uma lógica de teste, comparação e inspeção de comportamento, ajudando o desenvolvedor a construir intuição sobre quando simplificar, quando estruturar mais e quando trocar de técnica.

Por fim, a aula posiciona os vários tipos de prompt como um mapa de leitura para o restante do conteúdo. A estratégia pedagógica é estudar cada técnica em uso, comparando intenção, efeito e limitação prática. O primeiro tipo a ser abordado será o role prompt, apresentado como uma técnica já conhecida por muitos, mas que precisa ser compreendida de forma deliberada e não apenas intuitiva.

**Pontos de atenção**  
- Não assumir que mais contexto sempre melhora o resultado; informação em excesso pode piorar a saída.  
- Evitar prompts longos e detalhados sem necessidade, pois isso pode introduzir ruído e ambiguidade.  
- Priorizar a estrutura da instrução, alinhando objetivo, contexto útil e forma de pedir a tarefa.  
- Entender técnicas de prompt como escolhas técnicas, não como mera “escrita bonita” ou improviso textual.  
- Basear o aprendizado em experimentação prática, comparando respostas com pequenas variações no prompt.  
- Observar o comportamento do modelo de forma controlada para identificar impacto real de cada técnica.  
- Não estudar tipos de prompt apenas por definição; isso tende a deixar o conteúdo abstrato e superficial.  
- Tratar cada técnica como algo a ser analisado em intenção, efeito e limite prático.  
- Reconhecer que o uso intuitivo de técnicas como role prompt pode esconder impactos importantes na resposta.