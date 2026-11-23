Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16402)

## Resumo da aula

Escolher como usar uma LLM é uma decisão de engenharia, não apenas de uso da ferramenta. O objetivo é maximizar impacto com o menor custo possível, sem perder eficiência operacional nem controle sobre a saída. Esse trade-off importa especialmente em aplicações reais, nas quais resposta inconsistente, gasto excessivo e baixa previsibilidade afetam produto, operação e negócio. Conhecer a arquitetura do modelo ajuda, mas a decisão mais valiosa costuma ser escolher a estratégia de uso adequada.

Prompt engineering é a formulação deliberada de instruções textuais específicas para induzir a LLM a produzir uma saída mais alinhada ao objetivo. Não se trata apenas de “saber escrever”, mas de especificar contexto, formato, restrições e intenção com clareza suficiente para reduzir ambiguidade. Um prompt genérico como “me ajude com o resumo” tende a gerar uma resposta aceitável, porém pouco otimizada; ao explicitar limite de linhas, linguagem e foco, a saída fica mais direcionada. O ganho vem de transformar um pedido aberto em uma instrução operacional.

Entre prompting, RAG e fine-tuning, o prompt engineering costuma ser a estratégia de menor custo e menor tempo de implementação no curto prazo. Ele melhora o comportamento da LLM sem alterar arquitetura, pesos ou pipeline de treinamento, o que evita esforço alto de infraestrutura, dados e equipe especializada. Isso o torna a primeira opção quando o problema pode ser resolvido por melhor instrução, e não por adaptação estrutural do modelo. Em termos práticos, é a forma mais barata de aumentar aderência da resposta antes de considerar intervenções mais pesadas.

Uma LLM responde melhor quando a instrução define com precisão o que deve ser produzido. Pedir “escreva um parágrafo sobre o clima” abre espaço para respostas amplas e pouco úteis; pedir um parágrafo informativo, em linguagem jornalística, sobre o impacto do El Niño no Brasil em 2023 restringe tema, estilo e escopo. Esse controle reduz variabilidade desnecessária e aumenta a chance de a resposta servir diretamente ao caso de uso. Retomando os parâmetros de geração já vistos, eles ajustam o comportamento probabilístico; o prompt define a direção semântica e operacional da saída.

Prompts bem estruturados aumentam a precisão porque diminuem a liberdade interpretativa do modelo. Isso é decisivo em cenários como geração de código, respostas a clientes ou tarefas em que erro e inconsistência têm custo alto. Como a mesma pergunta pode produzir respostas diferentes em execuções distintas, instruções mais claras ajudam a estabilizar o comportamento observado. Precisão, nesse contexto, não significa perfeição, mas maior aderência ao resultado esperado.

Prompting também é uma decisão econômica, porque tokens consumidos viram custo direto em APIs pagas e custo indireto em ciclos de tentativa e erro. Perguntas abertas frequentemente exigem mais interações para corrigir rumo, enquanto instruções mais específicas reduzem retrabalho e desperdício. Isso vale tanto para uso pessoal com limites de créditos quanto para sistemas corporativos em escala, nos quais pequenas ineficiências se multiplicam rapidamente. Um prompt melhor não apenas melhora a resposta; ele reduz o custo total para chegar nela.

Quando o prompt é tratado como artefato de engenharia, ele pode ser comparado, versionado e testado. Isso permite executar testes A/B de estilo, tom, nível de detalhe e grau de restrição para descobrir qual instrução produz a resposta mais útil ao usuário. O benefício não é só qualidade textual, mas previsibilidade de comportamento em fluxos automatizados. Quanto mais explícita a instrução, mais fácil fica reproduzir, avaliar e ajustar o resultado.

Fine-tuning entra quando apenas instruções não bastam e há necessidade de adaptação mais profunda do comportamento do modelo. O custo e a complexidade são maiores porque essa estratégia envolve mexer no processo de treinamento, exigindo mais tempo, recursos e capacidade técnica. Por isso, a decisão racional costuma começar por prompt engineering e só avançar para fine-tuning quando o ganho esperado justificar o investimento. RAG também participa desse panorama como estratégia complementar de recuperação de contexto, já conhecida, e será útil quando o problema exigir acesso a informação externa ao prompt.

## Transcrição

00:00

Pessoal, estamos chegando no último módulo aqui do nosso curso. Eu espero que vocês tenham gostado bastante. A gente tem mais um pouquinho de conteúdo pra passar. Só pra finalizar, pra vocês ficarem craques quando a gente tá falando aqui sobre toda a estratégia de uma LLM e de como funciona uma IA. Trazer pra vocês os fundamentos reais. Eu espero que vocês tenham gostado bastante. Vamos finalizar agora com chave de ouro, falando de três grandes temas que eu vou trazer pra vocês.

00:28

A primeira coisa que eu queria conversar com vocês é o seguinte, já entendemos como tudo funciona, já entendemos basicamente tudo que esse treinamento queria passar pra vocês, que é como funciona e como foi criado, como foi evoluído e qual que é a estrutura principal e o core de uma LLM, de um transformer e assim por diante, pra você conseguir entender como isso funciona, porque daí no seu dia a dia você vai ter mais autonomia,

00:54

Você vai saber melhor como as coisas funcionam por trás e você possivelmente vai tomar decisões melhores. Então essa é a nossa ideia. Pra finalizar, eu queria passar por algumas coisas que a gente não pode deixar de fora. A gente não falou até agora de prompt e a maior parte dos cursos de A só falam de prompt.

01:10

O que a gente não quer é ensinar você a promptar no detalhe, não é a ideia desse treinamento. Mas eu quero te passar quais são as estratégias de prompt, quais são as estratégias que você pode usar pra promptar bem. E daí, dali pra frente, você vai evoluindo conforme você for usando IA. A gente vai fazer então aqui alguns cases pra vocês entenderem quais são os tipos de estratégia e vou passar por principalmente três tipos de estratégia de prompt pra vocês.

01:37

depois eu vou falar um pouquinho também sobre as estratégias de reggae pra vocês recuperação aumentada e geração eu vou falar então dessa estratégia também e depois eu vou encerrar perdão

01:51

falando um pouquinho mais de Fine Tuning mais alguns detalhes de Fine Tuning só pra vocês ficarem com o resto do que a gente tem de detalhezinhos de encerramento aqui do nosso treinamento, tá bom? Então esse módulo a gente vai pegar nesses três principais pontos, tá bom? Mais do que pra você aprender a dominar a ferramenta como a gente tem falado até agora eu quero te mostrar como que você usa e toma as melhores decisões sobre eficiência

02:18

custo e controle do que você tá gerando, porque aqui eu tô falando não só com quem vai promptar ali no dia a dia, mas também com quem vai criar aplicações que vão usar esse tipo de estratégia, com quem vai precisar criar negócios que vão usar uma estratégia desse tipo, e pra isso você precisa pensar em tudo isso, em custo, em eficiência, e você precisa pensar se o seu resultado vai ser o melhor resultado possível

02:41

dado tudo isso que a gente tem falado, beleza? Então, como você vai gerar o máximo impacto com o menor custo e com a melhor eficiência, fechou?

02:50

Então, vamos falar primeiro aqui de Prompt Engineering. Quando a gente está falando da parte de prompt, gente, não é nada mais, nada menos do que criar instruções textuais específicas. Isso mesmo! Você deve estar pensando... Poxa, você está falando que eu tenho que aprender a escrever. Sim! Muita gente sabe escrever, mas não consegue dar instruções claras, eficazes para os modelos de LLM. E eu vou falar a real. Quando eu comecei a estudar IA, eu achava que eu sabia promptar.

03:18

E depois de 9 meses estudando IA, quando eu comecei a aprofundar realmente, aí eu vi que o buraco é mais embaixo. Quando você precisa promptar bem, quando você precisa promptar para dar um resultado que você não pode falhar, é muito complicado, você precisa dominar muito.

03:35

é o que você tá gerando, tá bom? O óbvio precisa ser dito, sabe quando a gente fala isso? É mais ou menos isso quando a gente tá falando de um prompt de A. E tem várias estratégias, inclusive eu tenho estratégias próprias que eu fui desenvolvendo ao longo do meu treinamento, dos cursos que eu fui fazendo e do meu aprendizado, que eu já tô nessa jornada faz bastante tempo.

03:55

Então conforme eu fui evoluindo, eu fui criando estratégias próprias de prompt que fazem eles serem cada vez mais eficientes, inclusive diminuem o meu custo operacional de criação de prompt também. Então tem várias coisas que a gente pode fazer aqui. Não é a ideia desse curso explicar tudo sobre prompt pra vocês, mas explicar como a banda toca, como a coisa funciona pra você conseguir usar. Beleza? Vamos lá!

04:17

Então, basicamente, quando a gente tá falando de prompt, o que eu tô querendo no final do dia? Pensa o seguinte, você tem lá uma LLM e você pode deixar ela mais propensa ao que você precisa gerar, beleza? E isso, você tem as estratégias que eu acabei de falar pra vocês. Você pode usar tanto o Prompt Engineering, como o Fine Tuning, como, por exemplo, o Reg. Quando você tá falando

04:39

dessas três formas de fazer a coisa, a mais barata, querendo ou não, pra você de construção de tiro curto é o Prompt Engineering, porque aqui você vai influenciar ou controlar o comportamento dessa LLM, dessa estratégia de implementação

04:59

sem precisar mudar sua arquitetura, seus pesos e tudo aquilo que a gente falou até agora. Então, é uma forma de você conseguir um resultado melhorado, um resultado amplificado, porque você precisa, sem precisar mexer em toda a estrutura de Transformers. Então, é basicamente disso que você tem que ter na cabeça quando você estiver montando a sua estratégia de pra que lado correr, tá bom? Então, na prática, o que você precisa é

05:21

trabalhar um pedido que podia ser muitas vezes genérico, por exemplo, me ajude com o resumo. Isso é um pedido genérico, eu podia falar assim, olha, tá aqui um texto, me ajude resumindo esse texto.

05:34

Tá bom, então eu dei um texto e pedi um resumo. Você viu que é uma instrução básica, ele vai fazer, a sua LLM possivelmente vai fazer, se você jogar pro chat de APT, pro de Psyche, com Gemini, ele vai gerar, vai gerar possivelmente algo interessante, mas ele não vai gerar maximizando a performance do modelo.

05:52

Eu poderia, por exemplo, gerar algo um pouquinho melhor falando coisas do tipo, resuma o texto abaixo em até cinco linhas, com uma linguagem simples, destacando os principais argumentos apresentados. Essa é uma outra forma de promptar.

06:08

Então, aqui você já colocou muito mais informações. Dá pra fazer muito mais do que isso. Depende de onde você quer chegar. Então, possivelmente você precisa estruturar o seu prompt pra ser a melhor instrução possível pra basicamente nichar o pensamento da sua LLM. Pra isso que você vai usar o Prompt Engineering, beleza? Então, basicamente é uma arte de você formular os melhores direcionamentos

06:37

em linguagem natural e usando muito a sua criatividade para conseguir fazer isso no dia a dia. Então, é basicamente isso que é Prompt Engineering, beleza? E por que ele é tão importante?

06:53

Passo 1. Você consegue ganhar eficiência sem ter que retreinar. Lembra que a gente falou? Putz, pra treinar de novo um modelo é super caro. Pra treinar de novo um modelo, você tem que ter capacidade dentro do seu time pra fazer isso. Você vai ter que ter pessoas que consigam trabalhar esse treinamento. Dificilmente você sozinho vai pegar um modelo e vai sair treinando. Se você for fazer isso também, vai dar um baita de um trabalho, não é tão simples. Vai demorar.

07:16

Então, vai tempo, vai dinheiro, vai muita coisa aqui pra você conseguir fazer. Enquanto que um modelo de Prompt, você vai fazer isso com basicamente um Prompt bem escrito. Então, se você quiser mudar um Transformer, se você quiser treinar ele de novo, você vai gastar pra caramba. Se você colocar um Prompt bem feitinho, você consegue fazer isso um pouco mais barato e você consegue fazer de forma mais simplificada pra conseguir entregar o que você precisa, tá bom? Então, por exemplo,

07:46

Se eu pegar uma frase sem prompt em Genuine, por exemplo, escreva um parágrafo sobre o clima. Vai me dar uma resposta genérica, ele pode falar qualquer coisa sobre o clima. Agora imagina que eu preciso disso numa solução real, que eu tô usando no dia a dia. Se eu mandar um prompt desse, vai vir uma coisa genérica, pode vir qualquer tralha.

08:06

Agora, com prompting genuino, eu posso falar, escreva um parágrafo informativo em linguagem jornalística explicando o impacto do El Nino no clima do Brasil em 2023. Olha que coisa mais nichada, aqui eu consigo dar claramente o que eu preciso pra essa LLM me trazer o melhor resultado possível. Então, é mais ou menos disso que a gente tá falando, beleza?

08:26

Tem uma outra coisa também que é super importante. Então, a primeira coisa é eficiência sem precisar ser retreinado. Você vai gerar uma resposta muito melhor sem precisar gastar tanto com o treinamento novo da sua LLM. Agora, quando eu tô falando do segundo pilar aqui que a gente precisa pensar, é porque isso também aumenta a precisão.

08:46

Então, se você precisa de uma resposta precisa e você não dá uma instrução clara, você não vai ter essa resposta precisa, parece meio óbvio. Então, aqui quando você escreve prompt bem estruturado, a precisão possivelmente vai ser muito maior. Lembrando que se você fizer a mesma pergunta, e eu já fiz isso várias vezes para várias LLMs, a mesma pergunta 10 vezes, as respostas vêm 10 vezes diferentes. Muito difícil de ela vir 10 vezes igual ou muito parecida, ela dá uma mexida legal.

09:16

E daí vai depender de qual tipo de modelo, depois a gente até faz um teste sobre isso, qual tipo de modelo que você tá usando, vai ser mais ou menos desorganizado a coisa. Então, aqui quando a gente tá falando de tarefas críticas, que você precisa, por exemplo, geração de código, diagnóstico ou então resposta a clientes, não dá pra você ficar gerando algo que não vai ter precisão. Você precisa ter certa precisão, você não pode ficar brincando com isso.

09:43

Então, aqui é super importante também. Outro motivo pra ser importante é essa ideia de Promoting Engineering. Terceiro motivo.

09:51

economia de token. Então, quando você faz uma pergunta muito aberta, vai gastar muito token para conseguir moldar esta resposta, enquanto que se você fizer uma pergunta mais instrutiva, mais nichada, mais organizada, você consegue diminuir o custo disso, gastar menos tokens e com isso reduz muito o custo das APIs pagas, por exemplo, que você pode estar usando, ou até quando você está fazendo para seu uso próprio dentro de casa aqui, por exemplo, fazendo algum tipo de

10:21

de pesquisa e situações assim por diante, você não gasta tanto operacionalmente ali. Aí você vai me falar, poxa Natan, se você já paga o GPT, você pode ficar fazendo um monte de perguntas ali? Pode, tá bom? Se você paga o GPT, você pode. Mas por exemplo, se você estiver usando o Manos de graça,

10:39

Você tem um certo número de tokens que você pode usar. Chega uma hora que acaba. Se você estiver usando, por exemplo, para a geração de vídeo um VO3. Você tem, se eu não me engano, ali mil créditos para usar durante um mês. Acho que é mais ou menos isso. A cada mês ele te dá mais mil créditos, se eu não me engano.

10:55

Então, pra gerar um vídeo do Viu3, você vai gastar 100 créditos, você consegue gerar 10. Se você ficar promptando de qualquer jeito, você vai gerar 3 vídeos ali e o resto vai ser tudo descartado. Você não vai conseguir fazer isso de forma eficiente. Então, quando você tem limitação de custo, é super importante você pensar nisso. E aqui eu tô falando pra uso pessoal. Quando você tá falando do uso empresarial, se você não promptar certo, o custo vai subindo exponencialmente. Você precisa dar um jeito de nichar aquela resposta, beleza?

11:24

E outra coisa é que vai facilitar o seu controle e o teste do que você está gerando, porque você vai conseguir compreender o que está tendo de sair de fazer testes AB, por exemplo, de estilos de prompt para responder para o usuário. Seja mais simpático, seja menos simpático, responda mais aberto, responda mais nichado e assim por diante você consegue automatizar os fluxos com consistência.

11:45

Basicamente, são esses os pontos principais que eu queria que vocês tivessem na cabeça de quando a gente tá falando de estratégia de Prompt Engineering. Não é só simplesmente escrever um texto. Você precisa pensar em tudo isso que eu falei pra vocês, beleza? Agora, na sequência, eu vou aprofundar um pouquinho com vocês sobre como a gente faz isso em algumas estratégias reais de Prompt Engineering, beleza?

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **IA** — Inteligência Artificial  
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)  
- **A/B** — teste comparativo entre duas variações para avaliar qual performa melhor  
- **GPT** — *Generative Pre-trained Transformer* (Transformador Generativo Pré-Treinado)  
- **RAG** — *Retrieval-Augmented Generation* (Recuperação Aumentada com Geração)  
- **VO3** — ferramenta/modelo citado para geração de vídeo  

**Resumo**  
A aula encerra o módulo reforçando que escolher como usar uma LLM é uma decisão de engenharia, orientada por impacto, custo, eficiência e controle da saída. O instrutor destaca que, para aplicações reais, não basta conhecer a estrutura do modelo; é preciso decidir qual estratégia oferece melhor resultado com menor investimento operacional. Dentro desse contexto, ele introduz três abordagens principais: prompt engineering, RAG e fine-tuning, explicando que o módulo vai focar especialmente em como tomar boas decisões entre elas.

O principal tema da aula é o prompt engineering, definido como a criação deliberada de instruções textuais específicas para guiar a LLM com mais precisão. O instrutor mostra que um prompt genérico tende a produzir respostas aceitáveis, mas pouco otimizadas, enquanto um prompt bem formulado delimita melhor contexto, objetivo, formato, estilo e restrições. Com isso, a LLM fica mais “nichada” para a tarefa, respondendo de maneira mais alinhada ao caso de uso. A ideia central é transformar um pedido aberto em uma instrução operacional, capaz de melhorar a qualidade da saída sem alterar arquitetura, pesos ou treinamento do modelo.

A aula compara prompt engineering com fine-tuning e RAG, destacando que o prompt é a alternativa mais barata, rápida e simples para curto prazo. O fine-tuning aparece como uma solução mais profunda, porém mais cara e complexa, indicada quando só a instrução não resolve o problema. Já o RAG é citado como estratégia complementar para quando a aplicação precisa acessar informação externa ao prompt. O instrutor enfatiza que, antes de recorrer a intervenções mais pesadas, vale tentar extrair mais valor da própria formulação da instrução.

Ao longo da explicação, o instrutor usa exemplos práticos para mostrar como prompts mais específicos geram respostas melhores. Ele contrasta pedidos vagos, como “escreva um parágrafo sobre o clima”, com instruções mais detalhadas, como pedir um parágrafo informativo, em linguagem jornalística, sobre o impacto do El Niño no Brasil em 2023. Esse refinamento reduz ambiguidade, diminui variabilidade e aumenta a chance de a resposta ser útil diretamente no fluxo de trabalho. A aula também relaciona isso aos parâmetros de geração, reforçando que eles ajustam o comportamento probabilístico, enquanto o prompt define a direção semântica da saída.

Por fim, a aula mostra que prompt engineering também é uma decisão econômica e operacional. Prompts melhores reduzem o consumo de tokens, diminuem retrabalho, facilitam testes A/B, permitem versionamento e aumentam a previsibilidade em fluxos automatizados. Em cenários com APIs pagas, limites de créditos ou geração em escala, a diferença entre um prompt aberto e um prompt bem estruturado impacta diretamente custo e eficiência. O instrutor conclui que escrever prompt não é apenas “escrever bem”, mas formular instruções claras o suficiente para melhorar qualidade, estabilidade e controle do comportamento da LLM.

**Pontos de atenção**  
- Escolher a estratégia de uso da LLM é uma decisão de engenharia, não apenas de ferramenta.  
- Prompt engineering é a opção mais barata e rápida no curto prazo, mas não substitui fine-tuning quando é necessária adaptação profunda.  
- Prompts genéricos tendem a produzir respostas amplas, inconsistentes e pouco úteis para aplicações reais.  
- Quanto mais clara e específica a instrução, menor a ambiguidade e maior a aderência ao objetivo.  
- Em tarefas críticas, como geração de código, suporte ao cliente e diagnóstico, precisão e consistência são essenciais.  
- A mesma pergunta pode gerar respostas diferentes em execuções distintas; por isso, prompts bem estruturados ajudam a estabilizar o comportamento.  
- Prompting mal feito aumenta custo indireto com retrabalho e custo direto com consumo de tokens.  
- Em ambientes com APIs pagas ou créditos limitados, a economia de tokens é fator decisivo.  
- Prompts devem ser tratados como artefatos de engenharia: testáveis, comparáveis, versionáveis e passíveis de testes A/B.  
- Melhorar o prompt pode evitar retraining desnecessário, poupando tempo, dinheiro e infraestrutura.  
- Quando a informação precisa vir de fontes externas ao prompt, RAG pode ser mais adequado que apenas reformular instruções.