Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16390)

## Resumo da aula

Janela de contexto é a quantidade máxima de tokens que o modelo consegue considerar ao mesmo tempo para produzir a próxima saída. Como o processo autoregressivo usa tokens anteriores para prever os próximos, essa janela define o alcance efetivo da informação disponível durante a inferência. Na prática, ela limita o tamanho combinado de instruções, histórico, documentos e resposta. Modelos com janelas maiores conseguem operar sobre entradas mais longas, mas isso não elimina os problemas de qualidade.

Uma janela maior tende a melhorar a coerência porque o modelo consegue enxergar mais partes relevantes do contexto de uma só vez. Isso ajuda em tarefas como leitura de documentos extensos, integração de múltiplas fontes e respostas que dependem de dependências espalhadas ao longo do texto. Ainda assim, “caber na janela” não significa que todas as partes receberão a mesma atenção. O ganho é de capacidade de alcance, não de uniformidade de processamento.

Quando a entrada contém muitos tokens, a relevância das informações pode se diluir e o modelo passa a distribuir sua atenção de forma menos precisa. Retomando o mecanismo de atenção já discutido, o problema aqui não é a existência da atenção, mas sua limitação prática diante de contexto excessivo. O efeito mais comum é uma resposta mais genérica, com perda de detalhes ou descumprimento parcial de instruções específicas. Quanto mais informação concorrendo por atenção, maior a chance de trechos importantes receberem pouco peso.

Em modelos autoregressivos, existe uma tendência de os tokens mais recentes influenciarem mais a geração. Isso faz com que instruções colocadas no final do prompt frequentemente tenham mais peso do que informações equivalentes no início. A consequência prática é simples: em prompts muito longos, requisitos críticos devem aparecer perto do final ou ser reforçados explicitamente. Caso contrário, o modelo pode “esquecer” partes importantes do começo mesmo sem ultrapassar a janela.

Aumentar a janela de contexto encarece a inferência porque o mecanismo de atenção precisa processar mais relações entre tokens. O custo e o tempo de processamento crescem de forma quadrática em arquiteturas tradicionais de atenção, o que torna prompts longos significativamente mais caros e lentos. Existe, portanto, um trade-off direto entre alcance contextual e eficiência operacional. Janela grande melhora cobertura, mas cobra em latência e custo.

Considere um PDF de 200 páginas enviado com a instrução: resumir a cláusula de confidencialidade da página 13. Mesmo que todo o documento caiba na janela, o modelo pode responder de forma vaga ou misturar informações de outras partes porque o foco se dispersa ao longo do documento inteiro. O problema não é apenas capacidade de leitura, mas priorização interna daquilo que realmente importa. Em outras palavras, o modelo viu tudo, mas não necessariamente concentrou atenção no trecho certo.

Chunking divide o documento em partes lógicas, como capítulos, seções ou blocos menores, para reduzir a competição entre informações dentro do prompt. Isso melhora a precisão porque cada chamada trabalha com menos tokens e com contexto mais concentrado. Outra estratégia complementar é usar um sistema externo para recuperar apenas os trechos relevantes antes de enviar ao modelo. Em vez de pedir que a LLM encontre e resolva tudo sozinha, o pipeline separa busca e geração.

Resumos hierárquicos reduzem documentos longos em etapas sucessivas. Primeiro, resume-se cada parte; depois, usa-se esses resumos intermediários para produzir uma síntese mais específica ou executar outra tarefa. Esse método preserva cobertura sem exigir que todo o conteúdo bruto permaneça simultaneamente no contexto. Ele é útil quando o documento é grande demais ou quando a tarefa final depende de visão global, mas não de cada detalhe original.

Instruções de foco podem ser escritas de forma mais explícita para orientar a atenção do modelo dentro de um contexto longo. Em vez de apenas pedir “resuma a página 13”, vale restringir o escopo com comandos como ignorar a segunda metade do documento ou desconsiderar os últimos mil tokens. Isso não substitui um bom pré-processamento, mas ajuda a reduzir ambiguidade e a concentrar a geração no trecho desejado. É uma forma de cortar contexto via prompt quando o corte externo não foi feito.

## Transcrição

00:00

Fala galera, beleza? Quero falar com vocês de mais um item que a gente precisa ter atenção, tá? Como eu falei, as LLMs tem alguns pontos que a gente precisa evoluir ainda e dentro desses pontos tem um carinha que a gente chama de janela de contexto. Limitação ou janela de contexto? Melhor ainda, eu já vou falar do problema. Então tem a coisa que chama janela de contexto e ela tem uma limitação, tá bom? O que significa janela de contexto? Vamos lá, deixa eu contextualizar vocês então.

00:28

Imagina que você tem uma LLM ali, por exemplo, chatGPT 3.5 ou 4. Como que vai funcionar? A gente já falou disso durante várias partes do nosso curso aqui. Eu pego um token e vou prever o próximo, certo? Então, um grupo de token eu uso para prever o próximo token. Beleza? Então, com base nesse contexto,

00:49

eu vou entender os tokens anteriores e vou tentar evoluir para os próximos tokens, fechou? Então, esse contexto é limitado por um número máximo de tokens que você tem. Então, quando você joga um prompt para ele, ele vai olhar o prompt e ele vai ter uma limitação do que ele consegue enxergar.

01:08

de tokens. Então, quando você pega essa janela de contexto, é o que você consegue considerar de uma vez só, uma tacada só. E esse limite é chamado de janela de contexto, tá bom? Qual é a janela de contexto, por exemplo, do GPT 3.5? São 4.100 tokens, mais ou menos. É aproximado aqui, tá gente? Então, é mais ou menos 4.100 tokens.

01:32

Cara, é bastante. Se você olhar o GPT-4, 8 mil tokens, também é bastante. O GPT-4 Turbo, esse já é gigantesco, 128 mil tokens. Olha o tamanho da encrenca aqui. Se você olhar o Claude 3, da Anthropic, ele já tá batendo ali 200 mil tokens, mais ou menos. Então ele tá indo muito bem também. Gigante.

01:54

Qual que é o ponto que a gente tem aqui pra olhar? Quanto maior é a janela, tá bom? Mais o modelo consegue manter coerência. Fechou? Então, quanto for maior essa janela, mais coerência ele vai ter, porque ele vai conseguir enxergar mais. Tanto mais ele consegue raciocinar sobre um documento longo, pra integrar ali várias fontes de informação, pra ele conseguir produzir o que você tá pedindo pra ele. Fechou? Mas mesmo assim, você tem um problema acontecendo. Mesmo com essa janela grande,

02:24

A qualidade não vai ser uniforme. Então, imagina que você pegou o Claude com 200 mil tokens, ele vai ter uma janela gigante, só que ele não tem uma uniformidade em toda a extensão dos 200 mil tokens. O que ele faz? Ele tem três principais limitações. Vamos para a primeira? A primeira é a diluição de relevância, que a gente chama. Essa diluição de relevância significa o seguinte, quando tem muito token, eu vou ter dificuldade de manter o foco. Então, essa LLM vai ter um pouco mais de dificuldade de manter o foco.

02:52

Então, lembra aquilo que a gente falou, que a gente tem um mecanismo de atenção? Eu expliquei ele para vocês lá no começo da nossa conversa. Então você tem esse mecanismo de atenção. Ele não é perfeito, ele vai ter falhas. Quanto maior o problema para ele manter a atenção, pior é, é mais difícil

03:12

é você manter a atenção, porque você tem muita informação. Então, como qualquer coisa, se tem muito, você vai precisar de mais acurácia para conseguir manter a atenção. Então, esse modelo de atenção seletiva pode gerar, por exemplo, uma resposta um pouco mais genérica, se você tiver um prompt com uma tokenização muito grande, uma coisa muito grande de quantidade de tokens, você pode ter uma resposta mais genérica,

03:38

Você pode ignorar algumas das instruções que você mandou. Então pense o seguinte, tinha uma porrada de instrução, 200 mil tokens, é instrução pra cacete. E daí nessas 200 mil tokens, você pode perder alguns detalhes importantes ali. Por quê? O que ele vai fazer? Pode dar menos peso pra parte desse seu texto, porque na hora de manter a atenção ele vai decidir por outros lugares e algumas partes ele vai ser seletivo, pense assim.

04:05

E daí com isso você pode também ter um pouco de perda de coerência para trechos mais longos, que é a parte mais difícil da generativa, certo? O que mais você pode ter? Perda de foco, ou no final ou no começo. O que acontece? Quando a gente está falando, por exemplo, de modelos que são autoregressivos, eles tendem a dar mais foco para o final do contexto.

04:26

Então, ele vai pegar e vai ver todo o seu contexto. O finalzinho, ele vai dando mais foco. Então, os últimos tokens vão ter mais peso. Essa é a tendência. O que pode acontecer? Você pode, então, perder um pouco das informações do início do prompt. Aí, minha dica, se você for ter que usar um prompt tão grande assim, deixe as coisas mais críticas para o final. Se você deixar elas para o começo, possivelmente, você pode perder um pouquinho dessa acurácia, tá bom?

04:52

tem uma outra coisa aqui que é o custo computacional também que é uma limitação fala pô então vou trabalhar só com gpt-4 128 mil tokens tô tranquilo tá mais ou menos porque tem um negocinho que é complicado e o gpt-4 por exemplo ele cresce o custo e o tempo de processamento é

05:15

Quadraticamente, ou seja, ele vai elevar o seu custo de processamento e o seu tempo de processamento, ele vai elevar isso e vai

05:30

aumentar demais o custo vai ser muito difícil de você pagar a conta no final do dia então o mecanismo de atenção dele acaba sendo mais caro e daí vai ser muito é mais complexo então é mais lento só que em compensação ele vai conseguir olhar um grupo maior de coisas etc ele acaba te trazendo uma informação melhorada mas ele tem essas contrapartidas beleza é não ter almoço grátis

05:52

Então imagina o seguinte, vamos fazer aqui um caso, você tem lá um pdf, 200 páginas, aí você vai mandar pra LLM e vai falar o seguinte, resume pra mim os principais pontos da cláusula de confidencialidade da página 13.

06:13

Então você vai mandar isso pra ele. Bom, você deu claramente o que você quer, com a cláusula e com a página. Por mais que o modelo consiga ver as 200 páginas, ou seja, o monte de tokens, imagina que dentro dessas 200 páginas tem 128 tokens, cravado, e você tá usando o modelo do GPT-4 Turbo.

06:32

nem do modelo de GPT-4 Turbo, então coube, beleza? Ele olhou lá as 200 páginas, mas ele pode trazer uma resposta mais vaga porque ele diminuiu o foco, certo? Conforme eu falei, ele não foi só na página 13, ele diminuiu, ele diluiu o foco dele aqui. Então ele vai ter mais dificuldade, ou ele pode ignorar sua instrução, inclusive, de ir só na página 13, porque ele pode, ou de ir só nessa cláusula, porque ele

06:55

Perdeu tanto foco que ele não vai pegar essa informação e conseguir levar tão bem, entendeu? Então aqui você tem essa certa limitação. E como que você pode fazer pra contornar isso? Tem algumas estratégias de prompt que podem te ajudar, tá bom?

07:09

Tem um negócio chamada chunking intelligence. Você pode usar esse negócio para dividir, por exemplo, um documento em algumas partes lógicas. Dividir em capítulos, em seções, etc. Você consegue quebrar isso e dar mais foco, dar mais atenção para esses pedaços. Você pode também usar um sistema, por exemplo, externo para você buscar só trechos relevantes. Então, você separa os trabalhos. Você primeiro recorta, depois dá para ele fazer a ação. Entendeu? Basicamente isso. Fatia o bolo, entrega para ele com menos tokens para ele não ter que fazer

07:39

dividir tanta atenção dele. Você pode também, por exemplo, enviar os trechos em um modelo de prompt mais curto e direcionado. Você pode copiar mesmo, cortar e mandar mais direcionado, ao invés de mandar 200 páginas de pdf. Ou seja, você dá mais mastigadinho pra ele. Você pode fazer isso de forma manual, você pode fazer de forma automática, como eu falei, tem um sistema que vai quebrar isso e jogar pra ele, ou você pode quebrar por capítulos e sessões e focar

08:04

só em alguns capítulos e seções, que ainda assim você perde um pouco do seu modelo de atenção, ainda vai ficar mais difícil, não é a melhor prática, mas ajuda. Tem outra coisa que você pode fazer também, que são os resumos hierárquicos. Você pode fazer o quê? Resumir por partes. Então, por exemplo, você pode pegar um capítulo, resumir, e depois, em cima desse resumo, você trabalha o que você precisa fazer.

08:25

tem outra coisa que você pode fazer também que são prompts mais explícitos com instrução de foco isso a gente faz pouco então ao invés de você dar uma instrução de foco ali do tipo do que a gente deu de olha página 13 é uma certa instrução de foco certo mas ela não está explícita é um jeito de você deixar isso explícito é falar por exemplo ignora os mil tokens finais que eu sei que a página 13 está no meio do documento por exemplo é

08:51

Fala, ignora da metade para frente, ignora mil tokens do final ali e foca só no conteúdo da página 13 para resumir para mim a cláusula que eu te pedi. Então, você consegue focar um pouco a atenção dele pedindo para ele ignorar um trecho. Ou seja, ao invés de você cortar na mão, você corta com prompt para ele. Fala, cara, pode cortar daqui para lá que você não vai precisar usar. Então, é um jeito que você tem para resolver isso, tá bom? Daqui a pouco a gente volta para a próxima aula.

## Resumo IA

**Resumo**  
A aula explicou o conceito de janela de contexto em LLMs, isto é, a quantidade máxima de tokens que o modelo consegue considerar simultaneamente para gerar a próxima saída. O instrutor retomou o funcionamento autoregressivo, em que os tokens anteriores servem de base para prever os próximos, e destacou que essa janela limita o quanto de instruções, histórico, documentos e resposta podem ser considerados de uma vez. Foram citados exemplos de tamanhos de janela em diferentes modelos, como GPT-3.5, GPT-4, GPT-4 Turbo e Claude 3, para mostrar que modelos maiores conseguem lidar com entradas mais extensas.

Também foi discutido que uma janela maior não garante qualidade uniforme em todo o contexto. O instrutor apontou a diluição de relevância como principal problema: quanto mais tokens entram no prompt, mais difícil fica para o modelo manter foco e atenção em trechos específicos, o que pode resultar em respostas genéricas, perda de detalhes e descumprimento parcial de instruções. Outro ponto importante foi a tendência dos modelos autoregressivos de darem mais peso aos tokens mais recentes, fazendo com que instruções no final do prompt sejam frequentemente mais influentes do que as colocadas no início.

A aula ainda abordou o custo computacional de contextos longos. Como o mecanismo de atenção precisa processar mais relações entre tokens, o tempo e o custo de inferência crescem bastante, tornando prompts muito longos mais caros e lentos. Para exemplificar o problema, foi apresentado o caso de um PDF com 200 páginas em que o usuário pede o resumo de uma cláusula específica da página 13: mesmo cabendo na janela, o modelo pode responder de forma vaga ou dispersa por não concentrar atenção no trecho correto.

Por fim, o instrutor apresentou estratégias para contornar essas limitações: chunking, que divide documentos em partes lógicas; uso de sistemas externos para recuperar apenas trechos relevantes antes da geração; prompts mais curtos e direcionados; resumos hierárquicos, que condensam partes do documento em etapas sucessivas; e instruções de foco explícitas, como pedir para ignorar certas partes do texto e concentrar a análise em um trecho específico.  

**Pontos de atenção**  
- Janela de contexto maior aumenta a capacidade de leitura, mas não resolve automaticamente problemas de qualidade.  
- “Caber na janela” não significa que o modelo tratará todas as partes do contexto com o mesmo peso.  
- Contextos muito grandes tendem a causar diluição de relevância, com perda de foco e de detalhes importantes.  
- Em modelos autoregressivos, os tokens mais recentes costumam ter mais influência; instruções críticas devem aparecer mais ao final ou ser reforçadas.  
- Prompts longos podem gerar respostas mais genéricas e até ignorar parte das instruções originais.  
- O custo e a latência crescem significativamente com o aumento da janela de contexto, tornando a solução mais cara e lenta.  
- Enviar documentos enormes sem pré-processamento pode fazer o modelo “ver tudo”, mas não priorizar o trecho certo.  
- Chunking e recuperação externa ajudam a concentrar a atenção, sendo preferíveis a enviar todo o documento bruto.  
- Resumos hierárquicos são úteis quando o documento é grande demais, mas podem sacrificar detalhes finos do texto original.  
- Instruções de foco explícitas ajudam, mas não substituem uma boa estratégia de recorte e seleção de contexto.