Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16580)

## Resumo da aula

ReAct conecta raciocínio a execução observável. Em vez de apenas produzir uma resposta após pensar, o modelo alterna entre pensar sobre o problema, executar uma ação e incorporar o resultado dessa ação no próximo passo. Essa estrutura mudou o uso de LLMs porque aproxima o prompt de um ciclo operacional, não apenas de uma resposta textual. Por isso, a técnica aparece com frequência em agentes e frameworks que orquestram ferramentas externas.

O núcleo do ReAct é um loop de Thought/Action/Observation. O modelo primeiro formula um passo de raciocínio, depois escolhe uma ação concreta e, em seguida, recebe uma observação que representa o resultado dessa ação. A observação não encerra o processo; ela vira entrada para o próximo raciocínio, que pode gerar outra ação. O comportamento emergente é iterativo: o modelo avança por verificação sucessiva, não por uma única inferência linear como no Chain of Thought.

Agentes com IA usam esse loop para decidir o próximo passo com base no estado atual da tarefa. O agente deixa de ser apenas um gerador de texto e passa a operar como um controlador que escolhe quando consultar, buscar, executar ou interromper. Em frameworks como LangChain, o tipo de agente ReAct formaliza exatamente esse padrão. A utilidade prática está em permitir decisão e execução encadeadas dentro de um fluxo controlado.

O ganho mais importante do ReAct aparece quando o modelo tem acesso a ferramentas. Se a tarefa exige buscar repositórios públicos e existe uma integração com GitHub, a ação pode ser chamar essa ferramenta em vez de apenas descrever o que deveria ser feito. Isso transforma o raciocínio em operação verificável, porque o próximo passo depende do retorno real da ferramenta. Retomando a lógica de prompts analíticos já vista, a novidade aqui é que o modelo não só analisa: ele age sobre o ambiente disponível.

Um agente ReAct precisa de um critério explícito de parada. Sem esse controle, o loop pode continuar gerando novas ações e observações indefinidamente, elevando custo e latência sem ganho proporcional. O ponto de stop pode ser uma condição de sucesso, um limite de iterações, uma regra de confiança ou um orçamento de tokens. Esse mecanismo não é detalhe de implementação; ele é parte da segurança operacional do agente.

ReAct é especialmente útil quando a tarefa exige decidir e executar, não apenas responder. Isso inclui depuração de erros, busca de informação interna, automação de tarefas com decisão intermediária, troubleshooting de sistemas e integração com ferramentas externas. Nesses cenários, o valor está em permitir que cada passo seja guiado pelo resultado do passo anterior. A técnica também ajuda a localizar falhas em aplicações porque o processo fica mais inspecionável.

Como o loop produz múltiplos passos intermediários, ReAct tende a ser mais longo e mais verboso. Isso aumenta consumo de tokens e tempo de resposta, então o uso em alta escala costuma ser caro e lento. A técnica faz mais sentido em exploração, desenvolvimento, depuração e fluxos de maior valor por requisição. Em muitos casos, o próprio modelo já executa padrões semelhantes internamente, mas o prompt ainda pode forçar esse comportamento de forma mais explícita.

O principal risco operacional do ReAct é o modelo afirmar que executou uma ação que não executou ou inventar uma observação que nunca foi retornada por ferramenta alguma. Esse problema é grave porque quebra a confiabilidade do loop: o raciocínio seguinte passa a se apoiar em um estado falso. Embora esse tipo de alucinação não seja exclusivo do ReAct, ele se torna mais sensível aqui porque a técnica depende justamente da transição entre ação real e observação real. Em produção, isso exige validação externa das chamadas e das respostas recebidas.

Usar ReAct em produção é mais difícil do que usar prompts puramente analíticos. Além do prompt, é preciso controlar ferramentas, estados, critérios de parada, orçamento de execução e validação das observações. Isso torna a técnica poderosa, mas também mais arriscada em ambientes de alta escala. A escolha correta depende de quanto a aplicação realmente precisa de raciocínio acoplado a ação observável.

## Transcrição

00:01

Bom, pessoal, agora a gente vai para um outro tipo de prompt, tá? E esse prompt, eu não vou dizer que ele é complexo, a ideia dele é simples, mas ele mudou o jogo de como as LLMs funcionam. Por quê? Porque ele começou a meio que ser embutido nas próprias LLMs para elas tomarem determinadas ações baseadas em linhas de raciocínio e observações, tá?

00:26

Inclusive, por exemplo, você pode criar agentes React, que é o que a gente vai falar. Inclusive, por exemplo, num LangChain da vida, onde você vai criar um agente, você cria um tipo de agente chamado React, e é exatamente por conta desse tipo de técnica de prompt. Então, o que acontece? O React é reagir e agir. Basicamente, é reasoning e agir. Ou seja, ele vai raciocinar,

00:54

aí ele vai tomar uma ação, daí ele vai pegar a observação do que a ação dele resultou, tá? E depois, raciocinar em cima dessa observação, pra dar uma ação, pra gerar uma outra observação. Então, ele fica num loop ali, esse agente. Se você não tomar cuidado, ele não para nunca mesmo e vai gastar tokens. Tem até técnicas pra você colocar um ponto de stop,

01:21

para esse cara parar de processar, tá? E isso é muito, muito poderoso, galera, é muito poderoso. Principalmente se você está desenvolvendo agentes, dependendo da linha de raciocínio que você coloca, ele fala, olha, já que eu tenho que fazer isso, e eu tenho uma ferramenta assim, eu vou fazer uma chamada. Já que ele quer pegar os repositórios públicos, eu tenho uma ferramenta do GitHub, logo, a minha ação vai ser baixar os repositórios do GitHub,

01:46

Então, dá pra fazer muita coisa, é muito poderoso o React, tá? O ponto é que as pessoas usam muito pouco, mas, novamente, também você tem que tomar cuidado se for rodar em alta escala, tem muito token.

02:00

Ele demora, então, normalmente, você não vai rodar isso em alta escala. Você vai usar muito mais isso para exploração, para conseguir trabalhar no seu dia a dia para desenvolver coisas. Ou, muitas vezes, o seu próprio modelo já trabalha ali com React. Mas o fato é que, quando você trabalha com prompt, você consegue forçar essa linha de raciocínio. Então, quando que eu uso? Quero depurar erro, cara.

02:28

Eu quero criar um agente que busque informação interna. Eu quero automatizar uma tarefa que exige uma decisão e uma execução. Eu quero simular um troubleshooting de um sistema. Eu quero integrar um modelo com uma ferramenta externa. Então, tudo isso eu consigo fazer com React. Até para você resolver erro, corrigir erro, entender onde estão os erros da sua aplicação. Limitação.

02:52

É longo e é verboso. Escreve pra caramba. É difícil de controlar quando ele para. Às vezes ele simula a ação que não existe. Às vezes ele inventa a observação falsa. E ele é mais complexo pra usar em produção. Foi o que eu acabei de falar, porque é muita coisa, é muito lento e tem riscos e tudo mais. E quando eu digo produção, é alta escala, tá? É isso que você tem que tomar. Agora, essas limitações de pode simular a ação, pode fazer isso, pode fazer isso, todos os modelos podem, tá? Mas é importante ressaltar, porque isso é documentado em relação à parte do React.

03:22

Então, o que vamos fazer agora? No próximo vídeo, eu vou mostrar na prática o React para vocês funcionarem. E não é o React do framework JavaScript, é o React, esse tipo de prompt para a gente.

## Resumo IA

**Abreviações**
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)
- **LangChain** — framework para orquestração de aplicações com LLMs e ferramentas externas
- **React** — *Reasoning and Acting* (Raciocinar e Agir)

**Resumo**
A aula apresentou a técnica de prompt ReAct, explicando como ela combina raciocínio e ação observável em um ciclo iterativo. Em vez de gerar apenas uma resposta final após pensar, o modelo alterna entre formular um pensamento, executar uma ação concreta e incorporar a observação resultante para decidir o próximo passo. Esse fluxo foi descrito como o núcleo do padrão Thought/Action/Observation, que aproxima o comportamento do modelo de um agente capaz de operar sobre o ambiente, e não apenas de responder textualmente.

O instrutor destacou que essa abordagem é muito usada em agentes de IA e em frameworks como o LangChain, especialmente quando há integração com ferramentas externas. Nesse contexto, o modelo pode decidir consultar um repositório, buscar dados internos, executar uma automação ou chamar uma ferramenta como GitHub, em vez de apenas descrever o que faria. O valor do ReAct está justamente em transformar o raciocínio em operação verificável, permitindo que cada novo passo dependa do retorno real da ação anterior.

Também foi explicado que o ReAct precisa de um critério explícito de parada para não entrar em loop indefinido, o que aumentaria custo e latência. O método é especialmente útil em cenários como depuração de erros, troubleshooting, automação com decisão intermediária, busca de informação interna e integração com ferramentas externas. Por outro lado, o instrutor alertou que a técnica tende a ser longa, verbosa e cara em tokens, sendo menos adequada para alta escala e mais indicada para exploração, desenvolvimento e tarefas de maior valor por requisição.

**Pontos de atenção**
- Definir sempre um **critério de parada** do loop para evitar processamento infinito.
- Controlar **custo e latência**, pois o fluxo tende a consumir muitos tokens e ser mais lento.
- Evitar uso em **alta escala** quando houver alternativa mais simples, devido ao custo operacional.
- Validar externamente as **ações executadas** e as **observações recebidas** para não confiar em estados falsos.
- Ficar atento à possibilidade de o modelo **simular ações** ou **inventar observações** que não vieram de nenhuma ferramenta.
- Lembrar que o ReAct é mais útil quando há necessidade real de **decidir e executar**, não apenas responder.
- Em produção, gerenciar com cuidado **ferramentas, estado, orçamento de execução e validação**, pois a técnica é mais complexa de operar.
- Usar o ReAct principalmente em contextos de **exploração, depuração, troubleshooting e automação com ferramentas**, onde o ganho justifica a complexidade.