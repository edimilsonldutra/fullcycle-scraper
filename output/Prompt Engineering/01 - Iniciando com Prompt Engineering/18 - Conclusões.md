Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16584)

## Resumo da aula

Prompt Engineering deixa de ser improviso quando a escolha da técnica passa a seguir critérios explícitos. Antes de escrever o prompt, defina o contexto da tarefa, o formato de saída desejado, o nível de detalhamento necessário e o quanto o processo precisa ser auditável. Técnicas diferentes podem resolver problemas parecidos, mas com custos, rastreabilidade e qualidade de resposta muito distintos. A decisão correta não é “qual técnica é mais sofisticada”, e sim “qual técnica atende melhor esta tarefa com o menor overhead aceitável”.

A qualidade do prompt depende primeiro da clareza sobre a saída esperada. Isso inclui estrutura, nível de precisão, compatibilidade com etapas posteriores e utilidade operacional do resultado. Quando a resposta será consumida por outro modelo, parser, agente ou sistema, o formato deixa de ser detalhe e vira contrato. Um prompt mal especificado costuma falhar menos por falta de inteligência do modelo e mais por indefinição do que deveria ser produzido.

Nem toda tarefa precisa expor raciocínio intermediário ou usar técnicas mais pesadas de deliberação. Retomando as técnicas já vistas, pedir passo a passo sem necessidade aumenta consumo de tokens, latência e complexidade operacional, especialmente em sistemas. O uso de raciocínio estruturado faz sentido quando há necessidade de auditabilidade, depuração, comparação entre alternativas ou redução de erro em tarefas complexas. Em tarefas simples, esse custo adicional tende a ser desperdício.

Explorar alternativas não é um luxo; é uma forma de reduzir decisões precipitadas e ampliar cobertura de solução. Quando o problema admite múltiplos caminhos, vale acionar técnicas já estudadas para comparar opções, reverificar respostas ou expandir possibilidades antes de concluir. Tree of Thought ajuda quando a meta é abrir caminhos concorrentes de raciocínio, e self-consistency ajuda a checar estabilidade entre respostas possíveis. O ganho aparece menos na primeira resposta e mais na qualidade da decisão final.

Auditabilidade não exige sempre a mesma estratégia. Em alguns casos, basta uma saída estruturada e verificável; em outros, compensa usar uma técnica que exponha etapas intermediárias ou permita revisão de hipóteses. Retomando o uso de ReAct em troubleshooting e análise, o valor está em tornar a sequência de investigação revisável quando a confiança importa mais do que a brevidade. A técnica escolhida deve refletir o quanto você precisa inspecionar o caminho, e não apenas o resultado.

A utilidade prática das técnicas aparece com força em três frentes: documentação, debugging e agentes. Retomando o esqueleto documental já trabalhado, estruturar antes de expandir melhora a qualidade de artefatos técnicos e facilita revisão. No debugging, prompts intencionais ajudam a restringir hipóteses, evitar alucinação e orientar inspeção do problema. Em agentes, a escolha do prompt afeta diretamente como o sistema decide, integra ferramentas, controla custo e evita comportamento desgovernado.

Escrever bons prompts dá trabalho porque exige projetar a interação, não apenas digitar um pedido. Isso inclui decidir o esqueleto da documentação, definir o formato de resposta para integração com outro modelo e revisar saídas ruins para ajustar o prompt seguinte. Esse esforço é parte do processo de engenharia: observar erro, refinar instrução, testar novamente e estabilizar comportamento. A alternativa é aceitar respostas inconsistentes e tratar falhas do modelo como inevitáveis, quando muitas delas são falhas de especificação.

Um prompt útil não é texto descartável; ele pode virar ativo reutilizável de trabalho. Quando você cria prompts para descobrir bugs, gerar documentação ou explorar decisões técnicas, está construindo ferramentas cognitivas que podem ser revisitadas, versionadas e refinadas. Isso aproxima Prompt Engineering de práticas normais de desenvolvimento, como debugging, documentação e melhoria contínua. O ganho acumulado vem da iteração consciente, não de uma única formulação perfeita.

Técnicas mais elaboradas valem mais em tarefas complexas, ambíguas ou de alto impacto. Se a tarefa é simples, o custo adicional de estrutura, tokens e manutenção pode não compensar. Quando a tarefa envolve precisão, integração entre etapas, risco de alucinação ou necessidade de justificativa revisável, a sofisticação deixa de ser excesso e passa a ser controle. Escolher bem significa aplicar o mínimo de complexidade capaz de produzir o máximo de confiabilidade necessário.

A diferença entre usar IA de forma casual e usar IA como ferramenta de engenharia está na intencionalidade. Prompt bem feito melhora resposta, reduz erro e aumenta utilidade principalmente em tarefas difíceis, onde improviso costuma falhar. A disciplina prática é simples: parar antes de pedir, decidir o que precisa sair, escolher a técnica adequada e refinar com base no erro observado. Esse hábito muda como se programa, como se documenta, como se depura e como se constroem fluxos com agentes.

## Transcrição

00:00

Bom, pessoal, depois dessa jornada nos tipos de prompts que a gente tem, e existem mais, e a gente vai acabar topando com eles aqui no curso, eu queria apenas, vamos dizer, concluir esse capítulo dizendo o seguinte, a partir de hoje, todas as vezes que você for criar um prompt, tente realmente entender

00:26

Qual é o contexto em que você está? Para que esse prompt vai servir? Como você quer a saída desse prompt? Como você quer poder auditar o que ele está pensando? Como você, por exemplo, quer explorar opções?

00:43

porque a gente tem muitas variações. E, às vezes, eu posso usar um ou outro tipo de prompt para fazer tarefas similares. O que vai mudar muito é o nível de detalhamento que eu vou querer. Então, principalmente quando a gente começa a cair de prompts de chain of dots para baixo, ignorando zero shot, one shot, few shot, etc.,

01:08

tudo começa a ficar mais complexo porque geram, de uma forma e outra, linhas de pensamento ou formas que a IA começa a se reutilizar para conseguir dar as respostas. Então, o primeiro ponto que eu queria trazer aqui para você é o seguinte, tenha clareza do que você quer como saída. Verifique se há

01:39

a real necessidade da IA pensar passo a passo, porque a gente vicia nisso e, de repente, a gente começa a utilizar isso para sistemas e sistemas gastam tokens. Abuse na exploração de alternativas

02:05

em qualquer tipo de coisa, na hora que você estiver trabalhando, na hora que você estiver desenvolvendo. Obviamente que, novamente, em aplicações de alta escala, raramente você vai trabalhar dessa forma. Então, se você tem clareza do que você quer, se você realmente

02:25

está ali com aquela preocupação de auditar o resultado. Então, não necessariamente eu preciso pedir passo a passo. Eu preciso saber, até o que eu não sei, cara, eu quero abusar na exploração de como que isso pode acontecer. E aí eu posso trabalhar com Tree of Thoughts, eu posso trabalhar eventualmente com React, tá? Eu posso reverificar, tá? Reverificar. Reverificar.

02:55

respostas com self-consistency, por exemplo, a gente pode gerar muita documentação. A gente pode buscar e resolver muitos bugs.

03:13

Assim, as opções são quase que ilimitadas, uma vez que você tem tantas alternativas de prompt. Então, o que eu não quero é que você tenha assistido esse vídeo até aqui e que hoje ou amanhã você continue produzindo os seus prompts da forma como você sempre produziu. Dá trabalho.

03:37

ser intencional em qualquer coisa. Dá trabalho de você pensar em como que você quer o esqueleto da documentação que você quer que ele gere. Dá trabalho de conseguir definir como que ele vai responder a resposta que você está esperando para essa resposta ser compatível com a chamada de um outro modelo.

04:00

Dá trabalho quando a IA gera um monte de código ruim para você, e você ter que entender o que de ruim ela gerou, para que no seu prompt você consiga ajustar para ela não cometer esse erro. Por exemplo, com o fill shot. Nunca faça isso mais, ou qualquer coisa parecida. Entenda que todos esses tipos de prompt podem mudar o jogo de como você programa,

04:30

de como você integra e desenvolve agentes e como você usa IA no seu GPT, no seu Cloud, no seu Gemini, ali na interface mesmo, tirando dúvidas do dia-a-dia ali no seu celular. Muda completamente. E a última coisa que eu iria pedir muito para você é que toda vez que você sentir preguiça,

04:57

Tire isso da sua cabeça. Sem preguiça. Quanto mais você usar

05:07

e abusar de promptes bem feitos, melhor vai ser a sua resposta, melhor vai ser o resultado. Principalmente quando você vai fazer tarefas complexas. Se você for fazer tarefas que são realmente bem simples, não tem tanto sentido, mas são coisas mais complexas, meu, agora você tem recurso, agora você tem ferramento suficiente para que você realmente consiga...

05:35

ter munição, vamos dizer assim, para ter respostas mais precisas, para evitar alucinações, minimizar, como a gente pode ver, ia, delira, alucina, cria linhas de raciocínio errado, mas sem dúvidas, trabalhando de forma intencional, você vai, a partir de agora, estar em um outro nível, você vai estar em um outro nível no novo jogo.

05:58

Agora, o seguinte, nós terminamos a nossa primeira etapa aqui, porque eu precisava que você entendesse realmente de criar prompts.

06:07

ver a utilização desses prompts, entender bem esses prompts, para quando a gente falar, a gente está na mesma língua, para você começar a utilizar hoje, e eu provoco você para você criar um prompt para você conseguir descobrir bugs, um prompt para você conseguir gerar documentação, um prompt para você, por exemplo, fazer exploração de alternativas de qualquer coisa,

06:33

de decisões técnicas que você vai tomar, tá? Então, eu provoco que você crie esses prompts, brinquem, tá? Use os exemplos que eu acabei de trabalhar, você tem acesso ao repositório disso, exatamente para você entender e revisitar tudo isso que eu acabei falando. Fechou? Então, um grande abraço e é isso que a gente tinha para ver nesse capítulo, foi bastante coisa, bastante informação. Prompt é muita leitura, eu sei disso, mas eu espero que você tenha

07:01

entendido e visto o valor nisso que a gente acabou de ver. Um grande abraço e até mais!

## Resumo IA

**Abreviações**  
- IA: Inteligência Artificial  
- GPT: Generative Pre-trained Transformer  
- API: Application Programming Interface  
- React: técnica de prompting para execução, observação e atuação com ciclos de raciocínio e ferramentas  
- Tree of Thoughts: Árvore de Pensamentos  
- Self-consistency: consistência própria / verificação por múltiplas respostas  
- Zero-shot: sem exemplos  
- One-shot: com um exemplo  
- Few-shot: com poucos exemplos  

**Resumo**  
A aula conclui o capítulo de Prompt Engineering reforçando que a escolha da técnica não deve ser improvisada, mas orientada por critérios claros: contexto da tarefa, objetivo do prompt, formato da saída, necessidade de auditoria e nível de detalhamento desejado. O instrutor enfatiza que prompts diferentes podem resolver problemas parecidos, porém com custos, rastreabilidade e qualidade muito distintos, então a melhor decisão é sempre a que entrega o resultado necessário com o menor overhead aceitável.

O ponto central da aula é a clareza sobre a saída esperada. Quando a resposta será consumida por outro modelo, parser, agente ou sistema, o formato passa a ser um contrato e não apenas um detalhe. O instrutor alerta que muitos erros atribuídos à “inteligência” do modelo, na verdade, nascem de especificação ruim do que deve ser produzido. Também destaca que nem toda tarefa exige raciocínio passo a passo: pedir deliberação intermediária sem necessidade aumenta consumo de tokens, latência e complexidade operacional.

A aula retoma técnicas já vistas, como Tree of Thoughts, self-consistency e React, mostrando quando cada uma faz mais sentido. Tree of Thoughts é útil para explorar caminhos concorrentes, self-consistency para comparar estabilidade entre respostas, e React para investigações revisáveis em troubleshooting e análise, especialmente quando auditabilidade importa mais do que brevidade. O instrutor relaciona essas técnicas a três usos práticos principais: documentação, debugging e agentes. Em documentação, estruturar antes de expandir melhora a qualidade do artefato; em debugging, prompts intencionais ajudam a restringir hipóteses e evitar alucinações; em agentes, o prompt influencia decisão, uso de ferramentas, custo e comportamento geral do sistema.

Ao final, a aula reforça que escrever bons prompts é um trabalho de engenharia: observar erros, refinar instruções, testar novamente e estabilizar o comportamento. O instrutor incentiva a criação de prompts reutilizáveis para descobrir bugs, gerar documentação e explorar decisões técnicas, tratando esses prompts como ativos que podem ser versionados e melhorados. A disciplina proposta é simples: parar antes de pedir, decidir o que precisa sair, escolher a técnica adequada e iterar com base no erro observado.

**Pontos de atenção**  
- Defina antes de tudo o contexto, o objetivo e o formato da saída esperada.  
- Quando a resposta for integrada a outro modelo, sistema ou parser, o formato é um contrato.  
- Não assuma que “mais sofisticado” é melhor; escolha a técnica com menor overhead aceitável.  
- Evite pedir raciocínio passo a passo sem necessidade: isso aumenta tokens, latência e complexidade.  
- Use técnicas mais pesadas de deliberação apenas quando houver necessidade real de auditoria, depuração, comparação de alternativas ou redução de erro.  
- Explore alternativas quando o problema permitir múltiplos caminhos; isso reduz decisões precipitadas.  
- Tree of Thoughts é mais útil para abrir caminhos concorrentes; self-consistency para checar estabilidade entre respostas.  
- React é especialmente útil em troubleshooting e análise quando a sequência de investigação precisa ser revisável.  
- Em sistemas de alta escala, abordagens muito verbosas ou deliberativas tendem a ser pouco viáveis.  
- Em documentação, comece pelo esqueleto e só depois expanda o conteúdo.  
- Em debugging, revise os erros gerados pela IA para ajustar o prompt e restringir falhas futuras.  
- Em agentes, o prompt impacta diretamente custo, integração com ferramentas e controle de comportamento.  
- Prompts bons exigem iteração: observar erro, refinar instrução, testar de novo e estabilizar.  
- Não trate prompt como texto descartável; ele pode virar um ativo reutilizável e versionável.  
- Para tarefas simples, complexidade extra pode não compensar; reserve técnicas elaboradas para tarefas complexas, ambíguas ou de alto impacto.