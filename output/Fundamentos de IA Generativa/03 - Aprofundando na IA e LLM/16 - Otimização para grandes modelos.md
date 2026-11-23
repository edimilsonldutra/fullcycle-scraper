Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16387)

## Resumo da aula

LoRA é uma técnica de fine-tuning eficiente que evita atualizar todos os pesos de uma LLM. Em vez disso, os pesos originais ficam congelados e o treinamento recai sobre camadas adicionais de baixa dimensão, chamadas de low-rank. Isso reduz custo computacional, uso de memória e risco de sobreajuste, mantendo a capacidade de especializar o modelo para um domínio específico. Retomando o cenário de especialização já discutido, um Llama 2 pode ser adaptado para atendimento jurídico em português sem o custo de refazer o ajuste completo do modelo.

Quantização reduz o tamanho e o custo operacional de um modelo ao representar seus pesos com formatos numéricos mais leves, como INT8 ou INT4, em vez de representações mais pesadas. O ganho principal aparece em memória e velocidade de execução, o que viabiliza rodar modelos em hardware mais modesto. Essa redução cobra um preço: parte da precisão se perde, então a escolha do nível de quantização é sempre um compromisso entre qualidade e eficiência. Um Mistral 7B quantizado para INT4, por exemplo, pode cair de algo como 13 GB para cerca de 4 GB e passar a rodar localmente em ferramentas como Ollama ou LM Studio.

Mixture of Experts, ou MoE, organiza um modelo grande em vários especialistas internos e ativa apenas alguns deles para cada entrada. Em vez de mobilizar toda a rede a cada inferência, um componente roteador decide quais experts são mais adequados para processar aquela solicitação. Isso permite aumentar a escala total do modelo sem pagar o custo completo de ativação em todas as requisições. No caso do Switch Transformer, a ideia é justamente essa: mesmo com um número gigantesco de parâmetros, apenas uma fração dos especialistas entra em ação por entrada.

P-Tuning e Prefix Tuning adaptam o comportamento da LLM sem modificar seus pesos internos. A estratégia consiste em injetar contexto aprendido na entrada, seja como vetores que orientam o processamento, seja como tokens pré-treinados posicionados no início da sequência. O efeito prático é semelhante ao de fornecer instruções persistentes que moldam a resposta do modelo para uma tarefa específica. Retomando a noção de engenharia de prompt já conhecida, aqui ela deixa de ser apenas texto manual e passa a incorporar estruturas aprendidas para guiar o modelo de forma mais estável.

Essas técnicas resolvem problemas diferentes dentro da otimização de grandes modelos. LoRA ataca o custo do ajuste fino, quantização ataca o custo de memória e inferência, MoE melhora a eficiência estrutural em modelos muito grandes, e P-Tuning evita alterar pesos ao especializar comportamento. A escolha depende do gargalo dominante: orçamento de treinamento, limitação de hardware, escala do modelo ou necessidade de adaptação leve. Em ambientes reais, essas abordagens podem ser combinadas para equilibrar desempenho, custo e viabilidade operacional.

## Transcrição

00:00

Fala galera, beleza? Eu queria repassar com vocês um item importante aqui, tá? Eu vou tentar passar rapidamente, mas só pra gente ter isso na nossa mente. Já comentei um pouquinho com vocês sobre as técnicas de otimização de fine tuning que a gente tem pra grandes modelos. Acabei de falar pra vocês, eu só queria repassar alguns pedacinhos disso pra gente ter isso muito claro na cabeça. Primeira coisa que eu vou falar com vocês então é o LoRA, tá bom?

00:26

Low-Rank Adaptation. Esse LoRA, o que ele tem como contexto? Imagina o seguinte, você tem as LLMs crescendo muito, a gente tem muito dado, muito token sendo utilizado, então a gente começou a ter LLMs muito complexas na sua estruturação de dados e criação neural. Essa coisa ficou gigante, beleza? Muito caro pra fazer.

00:48

Depois veio a ideia dos fine-tunings que a gente pode ter para uma empresa e assim por diante. Quando a gente fala do fine-tuning, isso trouxe junto aquele problema que a gente acabou de conversar, poder computacional, custo e etc. O LoRA veio para tentar resolver isso. É uma técnica de otimização para tentar resolver isso e deixar isso mais simples, tá bom? Então, imagina que antes você precisava de grandes modelos para conseguir executar o fine-tuning também,

01:13

nos modelos que você já tinha ali de LLMs e aqui você consegue fazer o fine-tuning sem ser completo o fine-tuning que a gente falou usando esse tipo de estratégia para fazer ele parcial. Então, o LoRA vai permitir que você congele ali os pesos originais que você tem, tá bom? E vai adicionar algumas camadas mais leves de informação de baixa complexidade. Essas camadas vão chamar Low Rank.

01:38

essas camadas são mais importantes que a gente tem ali no Lora, tá bom? Porque isso faz com que a gente consiga...

01:45

conduzir um fine tuning sem ser completo e que seja importante consiga gerar certo resultado também. Então a gente vai treinar só essa camada de low rank, você não treina toda a camada de dados novamente, toda a camada que a gente já tinha ali de variáveis para fazer tudo de novo. Então fica mais barato e mais rápido de fazer. Com isso você vai diminuir tempo, uso de memória, você vai

02:10

diminuir risco de sobre ajustes e assim por diante. Então é uma técnica que você consegue usar que é bem eficiente para especializar uma LLM. Então eu vou dar um exemplo, a gente já falou disso, é que eu vou tocar em mais alguns exemplos de técnicas de otimização, mas o exemplo do Lora é, por exemplo, você pegar um llama da vida, o llama 2, e preparar ele para atendimento jurídico em português, por exemplo.

02:33

Você vai ter que testar e treinar ele, fazer um fine tuning em cima dele. Esse fine tuning completo seria extremamente caro para uma empresa, por exemplo, brasileira que não vai ter essa grana toda para refazer um llama dois da vida. Então, você precisa ter ali um poder, uma forma, uma estratégia de fazer isso para deixar ele preparado para a sua empresa, sua organização começar a usar, tá bom?

02:54

Então aqui você consegue fazer esse modelo especializado, treinado de forma um pouco mais rápida e mais barata. Bem mais barato do que um modelo de tuning completo, mas você ainda acaba gastando um pouquinho de dinheiro para conseguir fazer isso, então também não ache que você vai sair e vai fazer isso super barato, não. Tem um pouco de dinheiro gasto, mas fica muito mais simplificado.

03:13

Vamos para o segundo cenário, eu vou trazer para vocês, acho que 4 estratégias de otimização de grandes modelos de finetuning. A segunda que eu vou trazer para vocês é a quantização, vou falar de INT4 e INT8.

03:30

Aqui qual que é o contexto? Imagina que você tem uma LLM que vai usar um grande uso de GPU e de memória. Então como você não consegue rodar isso em máquina pessoal, você vai precisar de recursos limitados. Então você vai precisar de algum tipo de organização para conseguir fazer esta utilização.

03:52

A quantização vai compactar os modelos, mas ainda assim mantendo uma boa performance. É como se você zippasse o seu modelo pra você conseguir fazer esse processamento melhorado. Lógico que o zip é pra só guardar, mas imagina que você tá compactando isso pra no processamento você usar menos GPU e menos memória, tá bom?

04:17

Então ela vai converter ali os pesos dos modelos em ponto flutuante. É um pouquinho mais complicado, não vou entrar no detalhe disso, porque senão vai ficar uma aula muito complexa e muito longa. Eu acho que aqui a ideia é a gente passar fundamentos, então eu não vou entrar com o detalhe do detalhe, mas você vai transformar isso em ponto flutuante. Esse ponto flutuante vai ser o FP32 ou o FP16 da vida. E daí pra você conseguir fazer isso, quando você faz isso na verdade, você consegue então

04:43

ter uma representação mais leve, tá bom? Então você vai ter o INT8 e INT4 que eu falei ali pra vocês. Com isso você vai reduzir o uso de memória, vai acelerar o processamento e execução e você vai ter uma perda minimizada de precisão ali. Você consegue deixar isso com uma perda minimizada. Ou seja, você tá usando cálculo e matemática a seu favor pra deixar o modelo mais leve pra processamento. No fim das contas é isso, tá bom? E daí com isso você consegue rodar

05:09

modelo em cpu por exemplo ou em gpu de pequeno porte localmente você não precisa ir para uma gpu fora para você sair em um lugar fora do que você tem de ambiente normalmente então aqui é um jeito de você fazer isso é uma forma de otimização que chama quantização beleza então vou dar um exemplo prático para você aqui imagina que você quer pegar ou sei lá

05:31

O Llama ou Mistral, vou pegar o Mistral pra gente mudar um pouquinho. Você tem lá o Mistral 7B e você quer processar ele no seu notebook comum, você quer fazer alguma mudança aqui no notebook comum. Se você quantizar o modelo pra INT4 por exemplo, você vai deixar ele com vai, uns 4GB em vez de 13GB.

05:49

e daí olha ficou bem menor, tá vendo que é como se fosse um zip ele vai ficar bem menor e daí com isso você vai conseguir executar ele por exemplo em alguma ferramenta do tipo Ollama ou LM Studio você consegue jogar ele dentro da sua máquina e usando o processamento mais simplificado e vai ter uma qualidade aceitável nossa vai ser a puta qualidade não, não vai, vai ficar pioradinho mas você consegue fazer isso, isso é pra quem

06:17

tem restrição computacional ou precisa resolver esse tipo de problema em máquina local. Você vai achar o meio termo aqui, o melhor dos caminhos com que você tem de opção aqui, tá bom? Então, a quantização é bem importante, pode ser utilizada, mas você vai sim perder qualidade e etc, tá bom?

06:36

O terceiro modelo de que você tem de otimização chama a Mixture of Experts, o MoE (Mixture of Experts). Esse carinha aqui ele tem um contexto um pouquinho diferente também. Quando você vai treinar um modelo muito grande, você vai começando a ver que nem todas as partes elas vão precisar ser ativadas para todas as entradas.

06:59

Então você consegue separar um pouquinho a coisa, você vai especializar internamente o modelo e com isso você vai ter cada uma das partes responsáveis por parte do conhecimento.

07:12

Vamos ver se eu consigo explicar isso um pouco mais fácil para vocês. Imagina que você vai pegar o seu modelo e vai dividir em múltiplos experts, tá bom? Submodelos. Você quebrou ele e meio que modularizou ou criou micro modelos, tá bom? Então você gerou experts dentro do seu modelo. Com isso você vai ter uma rede roteadora como se fosse alguma estratégia de

07:34

de roteamento, de carga e de balanceamento, para quem conhece. E com isso você vai decidir quais dessas você vai ativar para cada entrada que você tem. Então, você teve uma entrada, você tem um roteador que ele vai decidir os experts e com base na entrada ele vai falar, esse expert tem que ser usado, esse expert, aquele expert, aquele expert. Com isso, você vai ter essas bases de modelo quebrada e você vai ter os experts sendo usados. Como você está numa base expert, você não vai ter que fazer isso para o modelo inteiro, você faz só para aquele trecho. E daí, com isso...

08:04

só essa parte do modelo vai ser impactada e vai ter sua inferência ali. E daí reduz o custo, óbvio, porque você tá limitando ali e vai permitir uma escala um pouco maior. Então eu vou dar um outro exemplo aqui, tá bom? Tô tentando abrir aqui o leque de ferramentas pra vocês também terem isso na cabeça, tá? Imagina que você pode usar, por exemplo, o Google Switch Transformer, tá? Ele tem mais de um trilhão ali de parâmetros, mas você pode fazer o seguinte,

08:34

você só ativa dois dos 64 especialistas ali, você quebrou ali em 64 especialistas, você vai ativar só dois dos 64, e daí com base nisso você vai ter uma resposta mais inteligente, só que com baixo custo, porque você inferiu por onde tem que ser essa resposta. E daí com isso você vai ter, por exemplo, uma aplicação de tradução ou geração de texto técnico um pouco mais facilitada ali, você consegue usar isso de uma forma mais estratégica.

09:04

Beleza? Esse é o terceiro. Vamos falar do quarto? O quarto é o P-Tuning ou Prefix Tuning. Depende de onde você vai ler ali, tá? Qual que é o contexto desse carinha? Imagina que você tem ali uma LLM que você precisa de tarefas específicas sem alterar o peso dessas tarefas.

09:30

Então, o que a gente muda aqui, tá? Você pensa que você vai ter uma técnica onde você insere condições ou contextos aprendidos nessas entradas, só que de uma forma mais leve e eficiente. Ou seja, você vai adaptar o comportamento sem modificar o modelo original. Então, tudo isso que a gente falou até agora, você estava pegando,

09:53

a maior parte do que a gente falou até agora, você estava pegando o modelo original e fazendo um fine-tuning nesse modelo original. Quando a gente tem o Prefix Tuning, você vai fazer o que? Você vai pegar o P-tuning ali, vai mostrar pra ele alguns vetores de entrada, ou seja, alguns prompts que vão orientar esse modelo sem alterar os seus pesos. Ou seja, é como se fosse um sidecar, pra quem conhece de desenvolvimento, é como se fosse um sidecar que tá ali do lado do seu...

10:22

do seu modelo de processamento, seu modelo de IA, e ele vai contando para onde que essa coisa deveria ir. Não sei se ficou muito claro para todo mundo, então vou tentar de um outro jeito. Imagina o seguinte, imagina que eu sou a máquina que tem todo o poder de processamento, e eu manjo pra caramba, eu sou a puta, eu sei tudo.

10:41

Quando chega um pedido pra mim, tem uma pessoa que fala assim, ó Natan, esse contexto aí é um contexto de jurídico, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá, blá

11:03

e daí com isso eu não alterei a minha forma de pensamento, eu me adequei ao que essa pessoa está me falando. Então é como se eu fosse num jantar muito elegante e usasse os talheres das melhores formas com etiqueta. Eu não mudei o meu jeito de comer no meu dia a dia, mas eu me adequei dado aquela etiqueta que me foi trazida. Tentei dar alguns exemplos dos mais malucos possíveis para tentar facilitar nossa compreensão aqui. Mas o que eu estou falando é, eu vou ter uma lista, ou seja, uma...

11:33

uma receitinha de bolo pré-pronta que vai me falar como que eu deveria agir dado a entrada então não muda o meu parâmetro mas faz um filtro de entrada me adequando pra fazer aquilo tá bom e aqui isso é pro p-tuning o Prefix Tuning ele vai fazer coisa parecida você vai ter os tokens treinados

11:54

no início de uma sequência, ou seja, você vai ter isso pré-aprendido também, que vai direcionar o modelo de saída. Ele é parecido também, só que você consegue fazer isso em vez de por prompt, você faz por tokens pré-treinados. Então, os tokens já estão preparados ali para no início da sequência serem colocados como tokens pré-aprendidos.

12:13

Então é um outro jeitinho de fazer isso. Os dois conseguem fazer um LLM se especializar usando engenharia de prompt em vez de usar finetuning propriamente dito. Olha que engraçado, você está usando a seu favor o próprio

12:29

a própria engenharia de prompt para conseguir chegar do outro lado fazendo uma organização e um tuning melhorado, tá bom? Então, com isso você não precisa mudar nada, você tem vetores adicionais que vão fazer você conseguir contextualizar, tá bom? Então, basicamente são esses quatro que a gente tem aqui para conversar e já já a gente volta para ir para o próximo assunto. Espero que você esteja gostando. Até já, um abraço.

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **LoRA** — *Low-Rank Adaptation* (Adaptação de Baixa Dimensão)
- **MoE** — *Mixture of Experts* (Mistura de Especialistas)
- **P-Tuning** — *Prompt Tuning* / *Prefix Tuning* (Tuning por Prompt / Tuning por Prefixo)
- **INT8** — Inteiro de 8 bits
- **INT4** — Inteiro de 4 bits
- **FP32** — *Floating Point 32-bit* (Ponto Flutuante de 32 bits)
- **FP16** — *Floating Point 16-bit* (Ponto Flutuante de 16 bits)
- **GPU** — *Graphics Processing Unit* (Unidade de Processamento Gráfico)
- **CPU** — *Central Processing Unit* (Unidade Central de Processamento)

**Resumo**
A aula apresentou técnicas de otimização e especialização de grandes modelos de linguagem, com foco em reduzir custo, memória e complexidade operacional sem perder completamente a utilidade do modelo. O instrutor começou com **LoRA**, explicando que, em vez de atualizar todos os pesos de uma LLM, os pesos originais ficam congelados e o treinamento acontece em camadas adicionais de baixa dimensão, o que torna o fine-tuning mais barato e rápido. O exemplo dado foi a adaptação de um **Llama 2** para atendimento jurídico em português, mostrando como especializar um modelo para um domínio específico sem arcar com o custo de um ajuste completo.

Em seguida, foi apresentada a **quantização**, técnica que reduz o tamanho do modelo ao representar seus pesos com formatos mais leves, como **INT8** e **INT4**, em vez de representações mais pesadas como **FP32** e **FP16**. O objetivo é diminuir uso de memória e acelerar a inferência, permitindo rodar modelos em hardware mais modesto, como CPU ou GPU de pequeno porte. O instrutor ilustrou com o caso de um **Mistral 7B**, que pode reduzir significativamente de tamanho ao ser quantizado, podendo ser executado localmente em ferramentas como **Ollama** ou **LM Studio**, embora com alguma perda de precisão.

Depois, a aula abordou **Mixture of Experts (MoE)**, explicando que um modelo é dividido em vários especialistas internos e que, para cada entrada, apenas alguns deles são ativados por um roteador. Isso permite escalar o número total de parâmetros sem acionar toda a rede a cada inferência. O exemplo citado foi o **Switch Transformer**, em que apenas uma pequena fração dos especialistas é usada por requisição, reduzindo custo computacional e permitindo aplicações mais eficientes em tarefas como tradução e geração técnica.

Por fim, o instrutor explicou **P-Tuning** e **Prefix Tuning** como formas de adaptar o comportamento de uma LLM sem alterar seus pesos internos. A ideia é inserir contexto aprendido na entrada, seja por vetores, prompts ou tokens pré-treinados no início da sequência, funcionando como uma orientação persistente para a tarefa desejada. A analogia usada foi a de um “sidecar” ou de uma instrução de etiqueta que direciona o comportamento sem mudar o modelo base. A aula encerrou reforçando que cada técnica resolve um tipo de gargalo diferente: **LoRA** para custo de fine-tuning, **quantização** para memória e inferência, **MoE** para escala estrutural e **P-Tuning/Prefix Tuning** para adaptação leve sem mexer nos pesos.

**Pontos de atenção**
- **LoRA não é fine-tuning completo**: os pesos originais ficam congelados; apenas as camadas de baixa dimensão são treinadas.
- **Há economia, mas não custo zero**: LoRA reduz muito o gasto, porém ainda exige treinamento e recursos computacionais.
- **Quantização envolve trade-off**: quanto mais agressiva a redução para INT8/INT4, maior o risco de perda de qualidade.
- **Modelos quantizados podem ficar piores em precisão**: a vantagem é viabilizar execução local, não necessariamente manter a mesma performance do modelo original.
- **Ferramentas locais são alvo da quantização**: o objetivo é permitir rodar em máquinas comuns, CPU ou GPU limitada, como em Ollama e LM Studio.
- **MoE ativa apenas parte do modelo por entrada**: é importante entender que nem todos os parâmetros são usados a cada inferência.
- **Roteador é componente crítico no MoE**: a qualidade da decisão sobre quais experts ativar influencia diretamente a resposta.
- **P-Tuning e Prefix Tuning não alteram os pesos do modelo**: a adaptação ocorre por contexto aprendido na entrada.
- **Engenharia de prompt é usada de forma mais estruturada**: nesses métodos, ela deixa de ser manual e passa a incorporar elementos treinados.
- **Escolha da técnica depende do gargalo principal**: custo de treinamento, limitação de hardware, necessidade de escala ou adaptação leve.
- **As abordagens podem ser combinadas**: em cenários reais, é comum usar mais de uma técnica para equilibrar desempenho e viabilidade.