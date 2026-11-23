Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16611)

## Resumo da aula

Um prompt mal delimitado pode transformar uma correção simples em uma alteração ampla demais. No cenário de desenvolvimento, isso acontece quando o modelo corrige o bug pedido, mas também refatora funções, reescreve testes, adiciona documentação e aplica padrões em arquivos que não faziam parte do objetivo original. O resultado pode até parecer tecnicamente melhor, mas operacionalmente piora o fluxo da equipe. Uma PR que deveria validar uma troca de > por >= passa a exigir revisão extensa e muda o custo do code review.

O problema central não é apenas a qualidade do código gerado, mas o desvio de escopo dentro do processo de entrega. Quando a mudança se espalha por vários arquivos, o revisor deixa de avaliar uma correção pontual e passa a revisar uma refatoração implícita, o que aumenta tempo, atrito e risco percebido. Isso pode atrasar a entrada de um bugfix urgente em produção, mesmo sem introdução de defeitos novos. Em times reais, previsibilidade de revisão importa tanto quanto a correção em si.

A ambiguidade já foi tratada anteriormente; aqui, ela aparece como falha operacional. Um pedido como “valide a função, entenda o problema e faça a correção” informa intenção, mas não impõe fronteiras suficientes sobre até onde o modelo pode ir. Como o modelo tenta ser útil, ele interpreta espaço aberto como permissão para melhorar o contexto ao redor. Em desenvolvimento, essa liberdade costuma virar alteração colateral.

Barreira de comportamento é a parte do prompt que restringe explicitamente o que o modelo pode e não pode fazer. Ela existe para conter a proatividade excessiva entre versões e famílias de modelos, já que o comportamento muda com o tempo mesmo quando o pedido parece “claro”. Em vez de confiar que o modelo vai inferir o limite correto, o prompt precisa declarar algo como: corrigir apenas o bug, não refatorar, não alterar arquivos fora do escopo, não reescrever testes além do necessário. Essa barreira reduz desvios e torna o resultado mais estável para o workflow de engenharia.

Limitar o prompt significa definir o escopo de atuação antes da execução, não corrigir o excesso depois. Esses limites podem envolver quantidade de arquivos, tipo de mudança permitida, proibição de melhorias oportunistas e foco exclusivo na causa do bug. Retomando o cenário da correção simples, o objetivo não é “melhorar o módulo”, mas resolver uma condição errada sem expandir a intervenção. Quanto mais explícito for esse recorte, menor a chance de a PR crescer sem necessidade.

Definir a saída final impede que o modelo invente a forma de entrega. Em um caso de desenvolvimento, isso pode significar pedir exatamente o patch mínimo, a lista de arquivos alterados, a justificativa da mudança e nada além disso. Sem essa definição, o modelo escolhe sozinho como responder e pode embutir mudanças extras porque considera isso útil. Saída especificada funciona como contrato de entrega e complementa os limites de comportamento.

Mudanças de versão alteram o grau de iniciativa do modelo, mesmo quando o prompt permanece igual. Um modelo mais “centrado” pode executar só o pedido, enquanto outro mais agressivo tenta otimizar o código inteiro ao redor do bug. Por isso, um prompt que parecia suficiente em uma versão pode falhar em outra. Estruturação intencional serve justamente para reduzir essa dependência do temperamento do modelo.

Como o caso de uso já determina a estrutura do prompt, correção de bug exige uma composição orientada a controle de escopo e previsibilidade de revisão. O prompt precisa separar com clareza o problema, os limites de atuação e o formato da resposta, porque o custo de uma resposta “boa demais” pode ser alto no pipeline de entrega. Em desenvolvimento, utilidade não é maximizar mudanças positivas; é produzir a menor alteração correta para o objetivo atual. Essa lógica prepara o terreno para guidelines mais formais de construção de prompts.

Comece descrevendo o bug de forma objetiva e localizável: qual função está errada, qual condição falha e qual comportamento esperado deve surgir após a correção. Em seguida, imponha a barreira de comportamento: alterar apenas o necessário para corrigir o bug, sem refatorar, sem reorganizar código, sem expandir documentação e sem modificar arquivos fora do escopo definido. Depois, declare a saída esperada: patch mínimo, arquivos alterados e explicação curta da correção. Essa combinação conecta teoria e prática porque transforma um pedido aberto em uma instrução operacional revisável.

Uma PR pequena não é só uma preferência estética; ela preserva a capacidade de revisão rápida e reduz o custo cognitivo do time. Quando o modelo trabalha com limites e saída definida, a chance de gerar mudanças laterais diminui, e o code review volta a refletir o objetivo original da tarefa. Isso não elimina completamente o comportamento probabilístico da IA, mas melhora bastante a previsibilidade entre execuções e entre versões de modelo. Em ambientes de engenharia, esse ganho de previsibilidade vale mais do que uma refatoração não solicitada.

## Transcrição

00:01

Bom, pessoal, agora que a gente teve uma ideia do que a gente vai falar agora, eu queria trazer um caso bem simples de coisas que podem atrapalhar muito o desenvolvimento de um software, e isso pode ser exatamente por um único motivo. Prompts.

00:17

incompletos ou prompts que não tenham uma clareza muito grande e que geram ambiguidade muito grande. E eu vou falar um exemplo bem claro que acontece. E se já aconteceu com você, eu acho que você já deve ter sentido na pele. Se não aconteceu, eu acho que já serve para você como uma dica do que não fazer, por exemplo, quando você vai desenvolver. Então, vamos imaginar o que acontece no processo de desenvolvimento de software comum.

00:44

Basicamente, eu tenho o meu software com um monte de linha de código, e daí alguém vai pedir, por exemplo, para eu resolver um bug aqui. Então, eu tenho um bug que eu quero resolver, e beleza, alguém passa esse bug para mim e acabou caindo. Aí, o que eu vou fazer uma vez que esse bug chega aqui para mim? Eu vou entender todo o processo e tudo mais, e eu vou fazer o desenvolvimento. E, nesse momento, o que eu vou fazer? Eu vou fazer o desenvolvimento do meu bug usando o IA,

01:11

mas todas as minhas ferramentas de IDE e tudo mais, todo o meu conhecimento como desenvolvedor, eu sou um ótimo desenvolvedor, então tá uma maravilha. E daí, uma vez que eu fiz tudo isso, eu vou gerar a minha pull request. Então, a minha pull request vai ser gerada e por, naturalmente, vai passar por quê? Por um code review. Beleza?

01:35

Agora, vamos imaginar que quem vai fazer esse Code Review aqui? Vai ser algum outro desenvolvedor. O bug que você tinha que consertar, o que acontece? Ele era uma função simples que estava com problema. Então, você tinha uma função muito simples que, no final das contas, vamos imaginar que era um maior igual que teria que ser mudado.

01:58

estava maior e você tinha que colocar o maior igual. Mas o que acontece? Como você mandou a instrução ali pra lá, o que ela fez? Ela fez muita coisa legal, adivinha só. Ela corrigiu o bug, ou seja, ela fez a correção do bug e você ficou muito feliz porque os testes estavam passando. Aí ela deu uma melhorada

02:21

nos testes para ficar um pouco mais claro, né? Esses testes. E aí, naquele arquivo ainda, ela percebeu que algumas partes não estavam tão bem documentadas. Então, o que ela fez? Ela também documentou um pouquinho, né? Ela fez a documentação. Documentou. Legal? Maravilha! Outra coisa que ela percebeu é que

02:46

Ali não estava usando tão bem os princípios, por exemplo, do Clean Code. Então, adivinha o que ela fez ainda? Ela pegou algumas funções e ela extraiu...

03:02

para funções menores, usando boas práticas, e daí ela estava dentro daquele módulo e começou a perceber que esse padrão que ela utilizou das boas práticas também poderiam ser feitos. Então, nesse momento, ficou top. Imagina você chegando em uma empresa

03:24

Primeiro dia de trabalho, o cara fala pra você corrigir um bug, e você não só corrige o seu bug, você é proativo. Você melhora o código, você documenta, você usa clean code, você extrai as funções, deixa as variáveis, tudo cada vez mais limpo.

03:39

Ou seja, o seu código está muito bem ilustrado. Agora, adivinha só o que vai acontecer quando esse cara aqui, que vai trabalhar aqui na parte do Code Review, ao invés de revisar uma linha de código, ele vai revisar, por exemplo, 500 linhas em, por exemplo,

04:09

cinco arquivos, ou seja,

04:14

Você pediu para a IA fazer uma coisa, ela fez, melhorou tudo o que ela precisava melhorar, não introduziu nenhum bug, mas o processo de desenvolvimento aqui, o workflow da sua equipe foi completamente modificado e enrolado, porque esse cara que ia gastar 5 minutos para fazer o code review do seu bug, esse cara aqui pode querer gastar o dia inteiro,

04:41

Esse cara vai ficar maluco. Por quê? Porque você simplesmente... Não é que você foi proativo. A sua I.A. foi proativa demais. E, nesse momento de proatividade, você se segurou ali por conta dos testes e realmente ficou melhor o código. Mas o objetivo inicial, na realidade, era fazer a correção de um bug.

05:04

não era refatorar código, não era melhorar código, porque toda vez que você sai mexendo em um monte de arquivo ao mesmo tempo, e isso aí ela faz, o que acontece? Você vai prejudicar a pessoa lá da ponta. E, às vezes, a necessidade de simplesmente coger um bug urgente

05:23

Não vai poder ir para a produção porque esse Code Review não ficou mais referente apenas àquele bug. Esse Code Review começou a virar um Code Review de refatoração de código e você perdeu o propósito.

05:37

Por que isso acontece? Muitas vezes a gente faz isso sem perceber. Eu, utilizando inteligência artificial, já percebi que algumas vezes eu estava querendo adicionar uma feature, ou melhorar alguma coisa, ou corrigir alguma coisa, e na realidade a correção era em um, em dois arquivos, e quando eu vi tinha dez arquivos modificados, e depois eu fiquei pensando, cara, que loucura a quantidade de arquivos que eu mesmo vou ter que revisar na hora de eu trabalhar.

06:06

Eu comecei a pensar, cara, será que isso é um problema do modelo? E, realmente, não digo que era um problema do modelo, tá? Mas isso aconteceu sabe quando? Quando eu estava usando o modelo do Cloud Sonnet.

06:22

E nessa época, a versão do Cloud Sonnet era 3. Eu não sei até que ponto o quanto você já trabalhou com o IA e o quanto você já utilizou, por exemplo, esse modelo do Cloud Sonnet 3. E ele estava sendo um modelo muito bom, porque ele fazia muita coisa legal e ele era bem centrado, vamos dizer assim. Você pedia para ele fazer uma coisa, ele fazia essa coisa.

06:46

Na mesma época, passou um tempinho, o que aconteceu? Lançou o Cloud Sonnet 4, tá? E o Cloud Sonnet 4 começou a parecer um desenvolvedor desenfreado que simplesmente saía fazendo as coisas pra você sem você mandar. O cara virou uma máquina de ser proativo.

07:09

E daí, apesar de ele resolver muitos problemas, esse cara aqui, vamos dizer, ele era muito arisco, né? Vamos imaginar que você tem um cavalo, um cavalo bem bonitinho ali, que você vai andando com ele e, de repente, você senta no outro cavalo e esse cara te joga pra cima. O Cláudio Sonnett foi um susto pra mim, tá? E esse susto, ele foi muito grande porque ele realmente saiu fazendo coisas que eu não queria. Mas, eu comecei a pensar, cara,

07:36

sempre vão haver novos modelos. Sempre vão haver novos modelos. Durante esse processo, lançou o Cloud Sonnet, o 4.1, o Opus, o GPT-5, o GPT-4.1 Mini, um monte de coisa, o Gemini, e os modelos não param de nascer. E o problema é que nós temos o seguinte, tá?

08:00

o comportamento do modelo sempre vai ser alterado conforme as versões. Então, quando eu tenho um comportamento, esse comportamento aqui, a gente não vai conseguir, na realidade, segurá-lo muito se você trabalhar de formas um pouco inocentes. Por exemplo, eu tenho um problema nessa feature e ela está fazendo um cálculo errado. Eu gostaria que você validasse essa função e tentasse entender o problema e fazer a correção para mim.

08:29

Muitas vezes a gente trabalha dessa forma e parece que está tudo ok, porque você realmente está especificando as coisas. O problema é que a falha desse tipo de coisa é que o prompt que a gente está usando, ou até mesmo o prompt que eu acabei de falar para você, ele não gera, na realidade, uma barreira

08:52

de comportamento. O que isso significa? O seu prompt não coloca limites naquilo que você quer que ele desenvolva. Então, toda vez que você vai estruturar um prompt, você tem que ter de cara quais são os limites que você vai deixar esse prompt trabalhar. Se você não limitar especificamente, pode ser

09:18

que você pegue o Cloud Sonnet em outras versões ou algum outro modelo e ele saia parecendo um estagiário irresponsável, saindo fazendo mudanças em 500 linhas de código. Uma vez que você também seta esses limites, uma outra coisa que você, na realidade, tem que conseguir fazer, adivinha o que é no final das contas.

09:44

resultado final. O que significa? Você tem que especificar a saída final. Se você não especifica como você quer a saída, ele vai gerar a saída da cabeça dele. Então, uma vez que você coloca limites e que você especifica uma saída, ou seja, o que você quer no final do dia,

10:10

ele tende a te respeitar mais. Significa que ele não pode querer sair mudando arquivos a mais? Meu, e há trabalho de forma probabilística, você nunca vai conseguir garantir absolutamente nada com a inteligência artificial. Porém, fazendo esses tipos de coisa, você vai conseguir trabalhar bastante, tá? E vai conseguir ter muitos resultados ali bem interessantes.

10:34

Eu, no próximo vídeo, vou dar mais um exemplo de coisas parecidas que podem acontecer com você no dia a dia, e depois, em seguida, eu vou caminhar para os conceitos e depois a gente vai para a prática. Eu vou te mostrar alguns prompts que eu tenho, vou liberar para vocês, quero que vocês façam testes e tudo mais. Fechou? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **IDE** — Ambiente de Desenvolvimento Integrado  
- **PR** — Pull Request  
- **Code Review** — Revisão de código  
- **Clean Code** — conjunto de boas práticas para escrita de código limpo e legível  
- **GPT** — Generative Pre-trained Transformer  
- **Opus** — nome de uma variante/modelo da família Claude  
- **Gemini** — família de modelos de IA do Google  

**Resumo**  
A aula mostrou como prompts incompletos ou mal delimitados podem prejudicar o desenvolvimento de software ao ampliar indevidamente o escopo de uma correção simples. O instrutor usou o exemplo de um bug pontual em uma função, como a troca de uma condição `>` por `>=`, para ilustrar que uma solicitação aberta à IA pode gerar não só o bugfix, mas também refatorações, reescrita de testes, melhorias de documentação e alterações em vários arquivos. Embora essas mudanças possam parecer positivas isoladamente, elas aumentam o custo de revisão, alteram o fluxo do time e podem atrasar a liberação de correções urgentes em produção.

O ponto central da aula foi que o problema não está apenas na qualidade da resposta gerada, mas no desvio de escopo dentro do processo de entrega. Para evitar isso, o instrutor explicou o conceito de barreira de comportamento, isto é, a parte do prompt que define explicitamente o que o modelo pode e não pode fazer. Essa barreira deve restringir a atuação da IA ao necessário para corrigir o bug, proibindo refatorações, mudanças fora do escopo, expansões de documentação e alterações colaterais. Além disso, foi enfatizado que o prompt também precisa definir a saída final esperada, como um patch mínimo, a lista de arquivos alterados e uma justificativa curta.

A aula também destacou que o comportamento da IA muda entre versões e modelos, o que torna perigoso confiar apenas em prompts vagos, mesmo quando parecem suficientes em um modelo específico. O instrutor comparou diferentes versões de modelos, observando que alguns são mais centrados e outros mais proativos, o que reforça a necessidade de estruturar prompts com limites claros e previsibilidade operacional. No fluxo proposto, primeiro descreve-se o bug de forma objetiva e localizável, depois impõem-se limites de atuação e, por fim, define-se exatamente como a resposta deve ser entregue. A ideia é transformar um pedido aberto em uma instrução operacional revisável, preservando a capacidade de revisão rápida e reduzindo o custo cognitivo do time.

**Pontos de atenção**  
- Um prompt “aberto demais” pode fazer a IA ir muito além da correção solicitada.  
- Correção de bug não deve virar refatoração implícita.  
- Alterar muitos arquivos para resolver um problema pequeno aumenta o custo do code review.  
- Melhorias oportunistas, como reescrever testes, documentar ou aplicar Clean Code fora do necessário, podem piorar o fluxo de entrega.  
- A proatividade excessiva do modelo pode ser útil tecnicamente, mas prejudicial operacionalmente.  
- Em times reais, previsibilidade de revisão é tão importante quanto a correção do código.  
- O prompt deve conter barreiras explícitas de comportamento: corrigir apenas o bug, sem refatorar, sem reorganizar, sem expandir o escopo.  
- É importante limitar quantidade de arquivos, tipo de mudança e áreas permitidas de atuação.  
- Definir a saída final evita que a IA escolha sozinha o formato da entrega e acrescente conteúdo desnecessário.  
- Não se deve confiar que um prompt que funciona em uma versão do modelo continuará funcionando em outra.  
- O comportamento da IA é probabilístico; por isso, o objetivo é reduzir desvios, não garantir controle absoluto.  
- O ideal em correção de bug é produzir a menor alteração correta possível.