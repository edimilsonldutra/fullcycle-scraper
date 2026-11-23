Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16568)

## Resumo da aula

Prompt Engineering, retomando a ideia já estabelecida de prompt como artefato de engenharia, ganha valor real quando deixa de ser texto improvisado e passa a ser instrução construída com intenção. A qualidade da resposta de um sistema generativo depende diretamente de como a tarefa é formulada, do contexto fornecido e do nível de precisão pedido. Por isso, escrever um bom prompt não é apenas “saber perguntar”, mas projetar uma entrada capaz de induzir comportamento útil, específico e tecnicamente adequado. A dimensão criativa entra justamente na escolha da forma de instruir o modelo para obter o resultado esperado sem perder controle.

O uso ingênuo de IA costuma produzir respostas superficiais, genéricas ou desalinhadas com a necessidade do desenvolvedor. Quando a instrução é vaga, o modelo preenche lacunas por conta própria e tende a devolver algo plausível, mas pouco acionável. O uso intencional reduz esse problema ao explicitar objetivo, escopo, profundidade e critério de saída, o que aumenta a chance de obter respostas mais úteis e consistentes. Em termos práticos, a diferença entre “funciona mal” e “muda completamente” muitas vezes está menos no modelo e mais na qualidade da instrução.

No fluxo de desenvolvimento, Prompt Engineering serve para apoiar tanto criação quanto manutenção de software. Isso inclui acelerar tarefas repetitivas, obter soluções rápidas para dúvidas pontuais e estruturar apoio em problemas mais complexos que exigem linha de raciocínio bem guiada. A utilidade não se limita à escrita de código: ela atravessa o ciclo completo de engenharia de software, do trabalho preparatório até atividades ligadas à confiabilidade antes de colocar o sistema em produção. O efeito principal é aumento de produtividade com mais direcionamento e menos tentativa aleatória.

A documentação com IA, já introduzida anteriormente, se torna mais útil quando o prompt explicita finalidade e recorte técnico do artefato. Em desenvolvimento de software, isso vale para design docs, resumos de decisões e explicações sobre partes do sistema que precisam ser mantidas ao longo do tempo. Um prompt bem construído ajuda a IA a produzir documentação mais alinhada ao domínio, ao nível de detalhe esperado e ao público que vai consumir aquele texto. Isso reduz retrabalho e melhora a capacidade da equipe de manter contexto compartilhado.

Prompt Engineering também atua como ferramenta operacional em atividades cotidianas de equipe. Em code review, a instrução pode direcionar a IA para avaliar legibilidade, risco, aderência a padrões e possíveis regressões, em vez de gerar comentários genéricos. Na escrita de commits, prompts melhores ajudam a transformar mudanças de código em mensagens mais claras e úteis para histórico e rastreabilidade. Em brainstorming, a qualidade da instrução define se a IA vai apenas listar ideias óbvias ou propor alternativas realmente relevantes para o problema técnico em questão.

Retomando a noção já conhecida de agentes, o ponto novo aqui é que sua utilidade prática depende da capacidade de “pilotá-los” com instruções melhores. Um agente de codificação não se torna eficaz apenas por existir; ele precisa receber objetivo, limites, contexto do repositório e expectativa de saída de forma suficientemente clara. Prompt Engineering é o mecanismo que transforma esse agente em apoio produtivo para implementar, revisar ou explorar soluções, em vez de um sistema que age de maneira errática. Quanto mais complexo o fluxo, maior a necessidade de instruções bem desenhadas.

Desenvolver software envolve etapas diferentes, com necessidades diferentes, e o prompt precisa acompanhar essa variação. A mesma prática que ajuda a gerar documentação também pode apoiar revisão de código, manutenção, exploração de alternativas e preparação para entrega com mais confiabilidade. Isso mostra que Prompt Engineering não é uma habilidade isolada para conversar com chatbot, mas uma prática transversal ao processo completo de engenharia de software. Seu valor está em conectar intenção, contexto e resultado ao longo do trabalho diário do desenvolvedor.

## Transcrição

00:01

Bom, pessoal, então o primeiro ponto que eu quero trazer aqui já pra gente começar com tudo é o que que é Prompt Engineering, né? Eu tenho que admitir pra você que quando eu comecei a estudar bastante sobre inteligência artificial, quando eu vi esse termo, eu já tinha pensado na hora, agora inventaram uma nova profissão.

00:21

Agora inventaram mais uma palavra, hype, para colocar em toda essa história de tecnologia, que é uma sopa de letrinhas. Mas, conforme eu fui tendo resultados muito ruins com o IA na hora que eu desenvolvia a software, na hora que eu estava utilizando agentes de IA para codificar, até mesmo quando eu fazia perguntas para o chat de GPT, eu sentia que as coisas eram superficiais e as coisas não funcionavam muito bem.

00:46

Até que um dia eu decidi realmente estudar a fundo o Prompt Engineering, e eu comecei a perceber que isso muda completamente. É a mesma coisa de você pegar um adolescente e perguntar alguma coisa pra ele, e você pegar um pós-doutor e perguntar a mesma coisa pra ele.

01:06

o nível de como que você trabalha com o IA, ele consegue ser, assim, tão distante da quantidade e da qualidade da informação que ele vai poder retornar pra você, tá? Então, quando a gente tá falando em Prompt Engineering, a gente tá falando que os sistemas de IA generativa, eles são projetados pra produzir respostas específicas com base na qualidade dos prompts fornecidos, tá? Então,

01:31

O que a gente tem aqui é que Prompt Engineering permite que esses modelos compreendam melhor as instruções e consigam trabalhar com uma ampla gama de demandas, desde comandos simples até questões altamente técnicas. Eu tirei esse coach aqui do site da IBM e eu acho que ele representa muito a contextualização.

01:53

Ou seja, a coisa básica, o sistema de A precisa produzir resposta específica, ele precisa ter qualidade nas respostas, a gente precisa saber perguntar, e tudo isso depende do prompt. Então, o prompt engineering, na realidade, é a forma de você construir instruções de uma forma

02:15

Vamos dizer assim, inclusive, muito criativa para você conseguir ter o seu resultado esperado. Agora, uma das coisas que eu quero sempre tentar deixar bem claro aqui para a gente é, eu sempre vou tentar contextualizar muito do que a gente está vendo no mundo, na nossa bolha de desenvolvimento de software. Por quê? Porque fica mais fácil a gente falar a mesma língua, a gente está no mesmo domínio, no mesmo

02:43

no mesmo ambiente de complexidade nos dias de hoje, tá? Então, se você for falar de Prompt Engineer pra quem tá trabalhando na área de Marketing, provavelmente a forma de ensinar e a forma dos exemplos serão completamente diferentes do que a gente vai tá aprendendo aqui, tá? Então, eu tô tentando fazer isso o mais focado possível pra ajudar, tá? Então...

03:05

Pensando nessa linha de raciocínio, como o Prompt Engineer vai poder nos ajudar ali em processo de desenvolvimento. Então, processo de desenvolvimento, o Prompt Engineer vai ajudar você a desenvolver software e manter o software que você tem. Ele vai ajudar você a automatizar tarefas repetitivas.

03:24

Ele vai ajudar você a ter soluções rápidas para aquilo que você está buscando. Ele vai conseguir te auxiliar em processos complexos de desenvolvimento, onde você realmente precisa de uma linha de raciocínio para conseguir tirar essas informações. Ele vai conseguir também ajudar você a gerar documentação.

03:41

trabalhar com design docs, a gente falou um pouquinho sobre isso, vai ajudar você a fazer code review, ele vai ajudar você a fazer brainstorming, vai ajudar você a fazer commit, ele vai ajudar a você pilotar o seu agente de A de codificação da melhor maneira possível. Então, quando a gente está falando de Prompt Engineering para processo de desenvolvimento de software,

04:01

ele vai te ajudar na sua produtividade e forma geral. E, como desenvolver software, a gente tem diversas etapas, principalmente quando a gente está falando engenharia de software, ou seja, a gente está falando do processo completo, desde uma documentação até o nível de confiabilidade quando o software vai para o ar,

04:23

O grande ponto é que a parte de Prompt Engineer vai ser essencial para cada uma dessas etapas quando a gente está falando em engenharia de software. Então, esse aí é um dos pontos importantes.

04:37

Então, Prompt Engineer vai te ajudar diariamente nesse tipo de coisa. Porém, por outro lado, a gente tem outros Prismas que também o Prompt Engineer vai fazer parte do seu dia-a-dia, tá? Somente pra esse vídeo ele não ficar muito enorme, eu vou parar aqui e a gente continua com outros aspectos então.

## Resumo IA

**Abreviações**  
- IA — Inteligência Artificial  
- AI — Inteligência Artificial  
- GPT — Generative Pre-trained Transformer  
- code review — revisão de código  
- brainstorming — tempestade de ideias  
- commit — registro de alteração no repositório  
- design doc(s) — documentação de design / documento de arquitetura e decisões  

**Resumo**  
A aula explicou que Prompt Engineering é a prática de construir instruções para sistemas de IA generativa de forma intencional, precisa e contextualizada, em vez de usar perguntas improvisadas e vagas. O instrutor destacou que a qualidade da resposta depende diretamente da qualidade do prompt: quanto mais claro forem objetivo, escopo, profundidade e tipo de saída esperado, mais útil e consistente será o resultado. A ideia central foi mostrar que a diferença entre respostas superficiais e respostas realmente acionáveis muitas vezes está mais na formulação da instrução do que no modelo em si.

O conteúdo foi contextualizado para desenvolvimento de software, reforçando que Prompt Engineering é uma habilidade transversal ao ciclo de engenharia. Ele pode ser usado para automatizar tarefas repetitivas, obter respostas rápidas para dúvidas técnicas, apoiar raciocínios mais complexos, gerar documentação, elaborar design docs, auxiliar em code review, brainstorming e escrita de commits, além de ajudar a “pilotar” agentes de codificação com mais precisão. O instrutor também ressaltou que essa prática melhora a produtividade e contribui para a manutenção do software e para a confiabilidade antes da entrega em produção.

**Pontos de atenção**  
- Prompt vago tende a gerar respostas genéricas, superficiais ou desalinhadas com a necessidade real.  
- A IA costuma preencher lacunas sozinha quando a instrução é incompleta, o que pode produzir saídas plausíveis, porém pouco úteis.  
- É importante explicitar objetivo, contexto, escopo, nível de detalhe e critério de saída no prompt.  
- Prompt Engineering não é só “saber perguntar”; é projetar instruções com intenção e controle.  
- A forma de instruir precisa considerar o domínio: exemplos e estratégias para desenvolvimento de software são diferentes de áreas como marketing.  
- Em code review, prompts genéricos levam a comentários genéricos; a instrução deve direcionar para legibilidade, risco, padrões e regressões.  
- Para agentes de codificação, não basta existir a ferramenta: é necessário fornecer contexto do repositório, limites e expectativa de resultado.  
- A prática deve acompanhar as diferentes etapas da engenharia de software, desde documentação até confiabilidade em produção.  
- O ganho de produtividade vem do uso intencional do prompt, não de tentativas aleatórias.