Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16403)

## Resumo da aula

Zero-shot prompting usa apenas a instrução da tarefa, sem exemplos prévios de entrada e saída. Essa estratégia funciona bem quando o modelo já responde bem ao tipo de tarefa pedido e quando o custo de tokens precisa ficar baixo. O ganho principal é velocidade de formulação, mas a saída tende a depender fortemente da clareza do enunciado. Se a instrução estiver ambígua, a resposta pode vir vaga, fora do formato esperado ou com baixa precisão.

Zero-shot é adequado quando não há necessidade de alto controle sobre a estrutura da resposta ou quando a tarefa já é muito conhecida pelo modelo, como classificações simples. No exemplo de sentimento, pedir “classifique o sentimento da frase: estou muito feliz com o produto que acabei de comprar” costuma ser suficiente porque muitos modelos já foram expostos a esse padrão. Também serve quando o próprio solicitante ainda está explorando o que quer obter e aceita respostas mais abertas. O custo menor vem justamente da ausência de exemplos adicionais no prompt.

Few-shot prompting adiciona exemplos de input e output antes da solicitação real para induzir o padrão desejado. Em vez de apenas dizer o que fazer, você demonstra como a tarefa deve ser resolvida, o que aumenta o controle sobre estilo, formato e critério de resposta. Essa técnica reduz ambiguidades e costuma ajudar em tarefas mais contextualizadas ou sujeitas a alucinação. O preço desse controle é maior consumo de tokens e maior esforço para selecionar exemplos representativos.

A lógica do few-shot é mostrar pares consistentes antes da consulta final. Em classificação de sentimentos, você pode fornecer frases rotuladas como positivo, negativo e neutro e só depois enviar uma quarta frase para o modelo classificar. Retomando esse cenário, a nova camada não está na tarefa em si, mas na formulação da instrução: o modelo passa a inferir o critério a partir dos exemplos, não apenas do comando. Se os exemplos forem mal escolhidos, o modelo aprende um padrão ruim e a qualidade da saída cai.

Chain-of-thought prompting, ou CoT, pede que o modelo explicite o raciocínio passo a passo antes de chegar à resposta final. Essa estratégia é útil quando a tarefa exige encadeamento lógico, múltiplas etapas, cálculo ou depuração de erros de raciocínio. Como o aluno já conhece a ideia geral de controle de saída, o ponto novo aqui é que o controle passa a incidir sobre o processo intermediário, não apenas sobre o formato final. Isso aumenta a capacidade de inspecionar desvios e corrigir o caminho seguido pelo modelo.

Ao forçar uma decomposição em etapas, o CoT tende a melhorar a precisão em problemas mais complexos e facilita identificar onde o modelo errou. No exemplo das maçãs, pedir “pense passo a passo” faz o modelo explicitar a soma antes de responder que João tem 5 maçãs. Essa transparência ajuda na depuração, mas não é gratuita: a resposta fica mais longa, mais cara em API e frequentemente exige um segundo prompt para condensar o resultado em algo utilizável. Além disso, a confiabilidade do raciocínio exposto depende do modelo, então o passo a passo também precisa ser validado.

Role-based prompting instrui o modelo a responder como se ocupasse um papel específico, como advogado, médico, cientista de dados ou uma persona alinhada à empresa. O objetivo não é apenas mudar o tom, mas induzir vocabulário, profundidade, enquadramento e prioridades compatíveis com um domínio. Isso é especialmente útil quando a resposta precisa parecer profissionalmente situada, como no primeiro contato de um escritório de advocacia. A técnica melhora coerência contextual, mas restringe a amplitude da resposta ao papel definido.

Uma persona bem definida aumenta a precisão da resposta porque reduz a liberdade interpretativa do modelo em domínios específicos. Pedir “você é um advogado trabalhista experiente; explique de forma clara os direitos de um trabalhador segundo a CLT” orienta não só o conteúdo, mas também o registro linguístico esperado. Em contrapartida, personas exigem iteração para ajuste fino e consomem mais tokens, já que a instrução precisa carregar identidade, contexto e limites de atuação. Se o papel estiver mal especificado, o modelo pode ficar artificial ou excessivamente estreito.

Instruction tuning via prompt consiste em formular comandos altamente explícitos sobre conteúdo, estilo, restrições e tamanho da resposta, sem alterar os pesos do modelo. Em vez de apenas pedir um tema, você define exatamente o que quer, como quer e em que extensão quer a saída. Um pedido como “explique inflação em linguagem simples, com até três parágrafos curtos” já embute objetivo, nível de linguagem e formato. Essa técnica se aproxima do comportamento de modelos afinados para seguir instruções, mas depende de alta precisão na escrita do prompt.

A escolha entre zero-shot, few-shot, CoT, role-based e instruction tuning via prompt depende do trade-off entre custo, controle e precisão. Zero-shot favorece rapidez e economia; few-shot melhora aderência por demonstração; CoT aumenta inspeção do raciocínio; role-based alinha a resposta a um domínio; instruction tuning via prompt padroniza saídas com comandos detalhados. A mesma tarefa pode produzir respostas muito diferentes conforme a estrutura da instrução usada. Prompting eficaz, portanto, não é uma única técnica, mas a seleção deliberada da estratégia mais adequada ao tipo de problema.

## Transcrição

00:02

pessoal então vou passar com vocês agora algumas das estratégias que a gente tem para fazer um prompt bem feito e de cada uma dessas estratégias é para um tipo de situação tá bom para vocês entenderem que formatos a gente pode seguir para conseguir o melhor resultado que a gente quer quando a gente está promptando beleza

00:22

então aqui para a gente conhecer o conceito de cada uma delas vamos falar primeiro do zero shot prompt esse cara é o mais comum que a gente vê no dia a dia é basicamente um tiro onde a gente está tentando acertar ali uma uma resposta tá você então vai dar uma instrução simples e direta sem exemplo anterior sem nada muito elaborado para o seu

00:45

para o seu Transformer. Então, quando você mandar essa pergunta, ele simplesmente vai responder assim por diante. É como se eu pedisse alguma coisa para uma pessoa, mas sem mostrar nenhum exemplo, sem mostrar como deve ser feito e assim por diante. É só um pedido aberto. Então, as vantagens disso é que é simples e direto. É muito mais fácil de promptar, muito mais rápido, muito mais simples para quem está promptando.

01:08

é bom para quando você tem um modelo que já desempenha alguma tarefa muito bem. Então, se você tiver um modelo que já está preparado para certa tarefa, esse tipo de estratégia pode ser uma estratégia interessante. Ele vai ser econômico em tokens, por exemplo, e você vai ter uma resposta não tão profunda. Quais são as desvantagens então que você vai ter aqui? A resposta pode ser vaga,

01:32

não tão profundo como acabei de falar, pode ser fora do padrão ou do formato que você deseja, e vai depender fortemente da clareza da instrução que você está mandando. Se você não tiver uma clareza muito grande, dificilmente você vai ter um resultado interessante. Então, esse tipo de estratégia normalmente é quando você não precisa de tanta precisão na saída, ou até quando você não tem tanto domínio do que você quer que saia. Para atividades, por exemplo, mais criativas, etc., às vezes é interessante.

02:01

Então, um exemplo pra vocês. Classifique o sentimento da frase... Estou muito feliz com o produto tal que eu acabei de comprar. Esse tipo de estratégia tem já vários... Várias transformers, várias LLMs que são preparadas pra isso. Você não precisa fazer um prompt muito diferenciado, que elas já estão prontas pra fazer esse tipo de estrutura. Então, você não precisa gastar tanto tempo.

02:25

dando tanta orientação porque ela já está preparada para isso eu poderia usar o mesmo tipo de coisa para algum tipo de pedido que eu não tenho tanto domínio do tipo a me deu um exemplo de um zero short prompting é para eu colocar nessa aula mas ele poderia dar um exemplo aleatório aqui e eu vou usar esse exemplo então puts eu não preciso ter um exemplo tão claro que ainda não sei muito bem o que eu quero poderia ser também um exemplo de zero prompting

02:50

é zero short prompting tá que pode ajudar vocês no dia a dia vamos pro segundo carinha aqui segundo carinha chama view short prompting esse cara ele vai ter qual estratégia nele você já vai começar a incluir exemplos de entrada e de saída de prompt que são os inputs e outputs que a gente tem então basicamente você vai treinando novamente essa esse LLM ou esse

03:15

ou esse Transformer que seja, para ele conseguir compreender qual é o estilo que você precisa, quais são os mecanismos que você precisa antes de fazer a sua pergunta real. Então, o modelo aprende com você o padrão que você espera, seguindo com base exemplos, nada melhor do que você dar exemplos. Imagina que você está ensinando alguém a fazer algo, seria algo parecido com isso. Você vai dar alguns exemplos e fala... Olha, dado essa pergunta, responda isso. Dado essa pergunta, responda aquilo. Dado essa pergunta, não responda isso.

03:44

e daí com o tempo ele vai começar a ficar mais afinado para o que você precisa, beleza? Então, quais são as vantagens que a gente tem aqui? Você vai ter mais controle sobre o formato e estilo de resposta, porque você foi direcionando ele para o que você quer, você reduz a alucinação e você tem ali, por exemplo,

04:03

uma maior facilidade para tarefas que são ambíguas ou muito contextualizadas, tá bom? Então tem essas vantagens aqui pra você. Quais são as desvantagens que você vai ter nesse tipo de estratégia? Você vai gastar mais token?

04:18

Então, você ocupa mais token ali de entrada e você tem que ter mais tempo para selecionar bons exemplos. Se der mal os exemplos, você vai acabar promptando errado, você vai gerar uma saída pior do que poderia. Então, você tem que ter ali uma categorização dos exemplos que você vai dar para não fazer nenhuma besteira. Vamos pensar em alguns exemplos aqui para vocês.

04:41

Imagina que você tá preparando uma classificação de sentimentos seguindo a lógica do que a gente tava falando anteriormente. Então você vai lá e fala pra ele assim ó, classifique os sentimentos das frases abaixo. E já passa pra ele a entrada e a saída. Então vamos lá, você dá a primeira entrada que é a seguinte frase. Esse produto é excelente e superou minhas expectativas. Qual o sentimento disso? Positivo.

05:03

Então você vai colocar lá a frase, o exemplo, qual o sentimento? Positivo. Segunda frase, o atendimento foi lento e os funcionários foram rudes. Sentimento? Negativo. Então você já passa isso pra eles, tá entendendo? Você não vai perguntar, você vai mandar a frase, qual o sentimento? Um, da primeira frase é positivo, da segunda frase que eu dei de exemplo é negativo. Da terceira frase, recebi um produto conforme descrito, nada além do esperado.

05:30

Bom, não é nem positivo nem negativo, é meio neutro. Então, você vai colocar isso como neutro. Imagina que eu dei três exemplos. Eu podia fazer 40 exemplos aqui. Quanto mais exemplos eu der, melhor. Mas imagina que eu dei três exemplos, já dá pra começar a brincadeira aqui desse tipo de estratégia. Dado esses três exemplos, aí eu faço a pergunta dando a quarta frase pra ele. Achei o preço justo, mas o prazo de entrega podia ser melhor. E deixo ele analisar esse sentimento pra ver se ele vai trazer pra mim.

05:58

que é positivo, se é negativo ou se é neutro, dado que eu acabei de explicar pra ele que é o conceito que eu compreendo, beleza? Então ele teve os exemplos pra conseguir seguir e chegar possivelmente numa estratégia um pouco melhor. Tá bom? Vamos então pra terceira estratégia que a gente tem de Prompt Engineering. A terceira dela chama Chain of Tough Prompting.

06:21

que é COT, C-O-T. Quando você vê essa sigla, então você está falando dessa estratégia de prompt. O que ela tem de diferente? Você pede para o modelo explicar o raciocínio passo a passo antes de te responder. Então, você pede para ele te contar o que ele pensou. Basicamente assim, olha... Antes de sair fazendo, me explica o que você pensou e daí a gente segue.

06:45

Eu uso isso muitas vezes quando eu pego algum modelo alucinando. Isso acontece, tá? Então, as vezes eu pego um modelo alucinando e falo, me explica passo a passo o que você tá fazendo. Daí eu vejo lá o passo a passo e falo, puta, aqui você tá errando. Organiza dessa forma e daí manda o prompt pra ele organizar aquele pedaço e fala, agora faz de novo.

07:02

Aí ele mostra de novo e eu falo, putz, agora você foi no caminho certo. E daí eu deixo ele fazer a execução. Isso é um exemplo, tá? Então, você pode usar essa técnica quando você precisa ter ali um controle maior do raciocínio passo a passo desse tipo de prompt, desse tipo de resultado que a sua LLM vai te trazer.

07:19

Então, o que é legal desse carinha aqui? Lembra que eu falei para vocês que para uma LLM, para um Transformer, uma das coisas mais difíceis é seguir uma lógica, porque ele não compreende lógica, ele compreende sequenciamento de texto. Então, para ele é muito difícil, tem estratégias que são colocadas por trás para ele que ele consiga, mas é doído para ele, é igual para a gente ir na academia, brincadeira, às vezes você gosta pra caramba, mas para mim é difícil, é doído.

07:46

Então, assim, você fala... Putz, eu preciso fazer isso. Tá bom, eu gosto? Não. Sou bom? Não. Mas eu tenho estratégias para fazer isso acontecer. Então, o Prompt pensa que ele vai te ajudar nesse tipo de coisa. Então, quando você faz um code aqui, você consegue direcionar para o seu Transformer ser melhor nesse tipo de estratégia. Ele vai conseguir ter uma melhora quando você fizer pedidos que dependem de um encadeamento lógico.

08:13

e a maior parte das lógicas elas são encadeadas, né? Então aqui você consegue ter um melhor resultado. Então quando você tem algum tipo de raciocínio multi-etapa, alguma coisa um pouco mais complicada, vai ajudar bastante você fazer esse tipo de estratégia. Tem vários papers inclusive que defendem o uso desse tipo de estratégia quando você precisa de cálculo, raciocínio multi-etapa, lógica de programação e assim por diante, beleza? Quais são as vantagens?

08:39

Quando você tem tarefa complexa, vai ser mais preciso, menos chance de erro. Você vai ter mais transparência na resposta que foi gerada, mas ó, essa transparência vai depender muito do modelo que você tá usando. Dependendo, por exemplo, o ChatGPT, ele teve há um tempo atrás uma atualização que ele mentia quando você fazia esse tipo de pergunta e ele não tinha resposta. Imagina que ele tava fazendo ali o chain dele, tava fazendo a corrente de pensamento e no meio dessa corrente ele colocava algumas coisas lá que ele

09:09

tava mentindo era só pra não falar que eu inventei ele dava umas mentidas e depois de um tempo teve algumas atualizações que melhoraram isso e hoje em dia eu não pego mais isso acontecendo então tem que olhar também se ali no meio do caminho ele não vai colocar nenhuma groselha então por isso que é importante a gente tá sempre ali próximo entendendo que ele tá gerando de resultado tá mas hoje em dia tá funcionando muito bem

09:32

Sendo bem honesto, fica aqui o meu feedback positivo pra todas as LLMs que eu tenho usado. Quando eu uso esse tipo de estratégia, tem respondido super bem. Então vamos lá. Vai ser mais transparente, você vai saber como a resposta foi gerada, o que é ótimo. Facilita uma depuração, foi o que eu falei pra vocês agora, e refinamento, quando você pega qualquer desvio.

09:56

Você consegue dar um tapinho e falar... Opa, para cá não, muda que aqui você está pensando errado. Quais são as desvantagens? A resposta é mais longa... Lógico, você demora mais tempo para organizar isso, a resposta vai ficar muito cheia de sujeira, porque você vai estar perguntando um monte de coisa, está te contando como ele está fazendo e fazendo. Então, fica uma resposta maior, mais longa e cheia de sujeira e depois você vai ter que fazer possivelmente um outro prompt mais simples para deixar isso mais organizado para você poder utilizar.

10:24

Outra coisa também é que quando você tá usando API ali o custo tende a ficar mais alto, você vai deixar bem caro esse tipo de estratégia. Então pra quem tá usando isso diretamente como chamada de API e utilização aí no dia a dia no seu tipo de trabalho que você precisa fazer, muito cuidado porque fica assim muito caro.

10:42

Vou dar um exemplo pra vocês, tá bom? Imagina que tem uma pergunta que é o seguinte, se João tem 3 maçãs e ganha 2, quantas maçãs ele tem agora? Pra gente parece simples, mas pra uma LLM é mais chato de pensar nisso. Elas conseguem, mas é mais chato. Quando você faz isso via prompt usando cot, você vai falar pra ela o seguinte, vamos pensar passo a passo.

11:06

como que você resolveria esse problema aqui. Então, você vai mandar pra ela assim ó, pergunta, se João tem três maçãs e ganhar mais duas, quantas ele tem agora? Utilize um chain of prompting pra me dar a resposta disso. Me conte passo a passo o que você tá fazendo. E daí ela vai te contar.

11:24

Vamos pensar um passo a passo então sobre este assunto. João começou com 3 maçãs, ele ganhou mais 2, então 3 mais 2 é igual a 5. A resposta é 5. Essa possivelmente vai ser a saída. A entrada aqui que eu coloquei para vocês é tão simples quanto dar a pergunta e ou pedir estrategicamente que ela te responda usando o cote,

11:43

Ou você falar pra ela, ó... Me responda contando passo a passo do que você fez pra chegar nessa solução. E daí ela vai te dar o passo a passo e você vai conseguir compreender. Você pode fazer isso de forma muito mais requintada, dependendo do que você precisa. Mas pra uma pergunta tão simples quanto essa, desse jeito já é o suficiente. E daí aqui você vai ter uma resposta estruturada ali do que você tá precisando, tá bom? Vamos lá pra mais um. Hold-based prompting. Esse carinha aqui também...

12:12

É uma coisa que eu gosto muito de usar, muito, muito, muito.

12:17

Você pode instruir o modelo, então, para assumir um papel. Você cria uma persona. Você fala, a partir de agora, você vai pensar deste jeito. Ou seja, eu posso virar e falar assim, a partir de agora você vai pensar como um advogado, ou como um médico, ou como um cientista de dados, ou como um professor, ou até falar, pensar igual a mim. Isso vai influenciar o tom, o vocabulário, profundidade e tudo que ele vai fazer. Então, você pode falar, por exemplo, imagina que eu quero pegar o tom de alguém que eu conheço aqui.

12:47

Eu quero pegar o tom de um ator, ou alguém conhecido, ou um jornalista e tal. Eu posso falar pra ele ler tudo que tem na web sobre esse ator, sobre esse jornalista, ver quais são os tons, por exemplo, de artigos, etc, que ele conversa, que ele cria conteúdo.

13:03

E com base nisso, eu posso pedir pra ele assumir este papel. A partir de agora ele é esta persona. Então possivelmente ele vai dar respostas muito direcionadas pra esse tipo de estratégia, esse tipo de papel. Então aqui eu falei brincando de você pegar um ator, mas você pode colocar, por exemplo, um advogado, um médico, foi como eu falei. Depende do que você precisa responder, imagina que você precisa fazer uma I.A.

13:23

que vai responder alguns questionamentos médicos iniciais ali, de advocacia iniciais ali. Por exemplo, você é de um escritório de advocacia e você precisa responder o primeiro contato de um cliente. Se você já deixar ele preparado para responder como um advogado, possivelmente ele já vai mostrar para o cliente que ele está dentro de um escritório, já começa a entender essa correlação e ter maior facilidade no comportamento dele, tá bom?

13:48

Então, as vantagens é que você vai ter uma maior precisão e coerência, ainda mais quando você está falando de domínios específicos, como eu falei para vocês. Você vai ter maior facilidade para usar o modelo em contexto profissional, igual eu falei agora. Imagina que eu falei sobre um médico, mas você pode falar para ele assumir um papel de alguém que segue as diretrizes da sua empresa, da sua organização. Então, por exemplo, se é uma empresa que preza pelo...

14:15

pelo bem-estar e etc. Putz, já deixei isso lá já preparado para ele assumir esse tipo de papel, beleza?

14:23

Quais são as desvantagens? As desvantagens é que essa capacidade do modelo de incorporar o papel, ele vai nichar nesse papel, então ele não vai abrir muito quando vier alguma coisa mais expansiva, a não ser que você dê essa informação, esse direcionamento pra ele. Pode existir... Pode não, vai exigir muito teste pra você conseguir ajustar essa persona corretamente, porque ele não pega logo de cara, você precisa ir organizando até ele pegar.

14:51

E também é um pouquinho caro pra você fazer, você gasta bastante pra transformar essa persona, tá bom? Então vou dar um exemplo, você é um advogado trabalhista, experiente, explique de uma forma clara os direitos de um estagiário segundo a CLT.

15:09

ou dos direitos de um trabalhador segundo a CLT. Então aqui você está falando para ele o que ele é, você já deixa claro e pede para ele explicar, ele vai explicar possivelmente em um tom mais jurídico aqui. Beleza? Então essa é uma outra forma de você gerar esse prompt. Tem mais uma gente.

15:27

um Instruction Tunning Prompt. Você pode fazer isso via Prompt e você pode fazer isso via Instruction do GPT também. Então, deixa eu explicar isso melhor. Esse tipo de estratégia, ele pode usar um negócio do GPT que chama Instruct GPT, que você pode fazer também.

15:45

ou você pode fazer isso direto pelo Instruction Tunning no Prompt Engineering. Então, você pode usar a mesma estratégia que você estaria no Instruct GPT, só que direto promptando. Então, aqui é a mesma coisa que a gente fala de treinamento supervisionado, que a gente falou lá atrás, só que aqui a gente está falando de prompts que foram moldados para conseguir fazer esse tipo de

16:08

de comportamento por modelos claros e definidos ali. Então, por exemplo, eu posso definir essa estratégia pra ganhar algumas vantagens aqui pra gente. Você vai ter um estilo mais direto, é fácil de padronizar e assim por diante. Ele vai funcionar bem em modelos que já foram afinados com esse tipo de entrada, como o GPT, por exemplo, que ele já foi afinado desse jeito. Mas você precisa de uma precisão de comando muito boa. Isso é pra quem prompta muito bem, tá? E alguns modelos, eles podem responder melhor

16:37

a esse estilo do que outros modelos. Por exemplo, o GPT responde super bem a esse tipo de estratégia. Tô tentando lembrar de algum modelo que não responde. O DeepSeek também responde. Deixa eu ver algum que pode não responder bem. Eu não lembro se o Manos tem respondido bem. As últimas vezes que eu tentei desse jeito no Manos, se eu não me engano, ele não é tão bom quanto o GPT e quanto o DeepSeek.

17:02

mas eu não sei se é por conta da versão que eu usei. Vale a gente conferir um pouco quando for fazer, quais são os modelos que mandam melhor nesse Struction Tunning, mas alguns deles podem ir melhor do que outros. Eu nunca peguei um problema claro acontecendo, e a maior parte dos modelos de geração de textual manda bem nisso.

17:26

Então, por exemplo, você pode falar pra ele explicar o conceito de inflação em uma linguagem simples, com até três parágrafos curtos. Ou seja, você tá vendo que eu já falei pra ele tudo que eu quero? Eu quero... Qual a informação que eu quero, qual o estilo de linguagem que eu quero e qual o tamanho que ele tem que fazer. Então, aqui eu já dei uma direção geral. Lógico, de uma coisa muito tonta. Normalmente, pra fazer um prompt,

17:51

Tão detalhado, vou te falar que eu já tenho prompts no livro que eu escrevi sobre A, que são de mais ou menos 3 a 4 páginas de prompt nesse tipo de estratégia de instruction planning, que é muito mais detalhado pra você conseguir fazer, tá bom? Aqui eu fiz um exemplo simples.

18:09

Mas quando você for fazer esse tipo de estratégia legal, você detalha muito bem o que você precisa. Fechou? Essas são as estratégias que a gente tem. Cada uma delas vai ter seus prós e contras. E você precisa pensar quando você for usar no dia a dia qual vai fazer mais sentido para cada tipo de aplicação que você for puxar aí no seu dia a dia. Beleza?

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)  
- **CLT** — Consolidação das Leis do Trabalho  
- **CoT** — *Chain-of-Thought* (cadeia de raciocínio)  

**Resumo**  
A aula apresentou estratégias de *prompt engineering* para obter melhores resultados em modelos de linguagem, mostrando que a escolha da técnica depende do nível de controle, custo e precisão desejados. No **zero-shot prompting**, o modelo recebe apenas a instrução da tarefa, sem exemplos, o que torna o processo mais rápido, simples e econômico em tokens, mas também mais sensível à clareza do enunciado e com maior chance de respostas vagas ou fora do formato esperado. No **few-shot prompting**, o instrutor demonstrou como incluir exemplos de entrada e saída para ensinar o padrão desejado ao modelo, aumentando o controle sobre estilo, formato e critério de resposta, embora com maior consumo de tokens e necessidade de selecionar bons exemplos.

Em seguida, foi explicado o **chain-of-thought prompting (CoT)**, em que o modelo é solicitado a explicitar o raciocínio passo a passo antes da resposta final. Essa abordagem foi associada a tarefas mais complexas, com múltiplas etapas, cálculo ou depuração de erros, pois melhora a transparência e facilita identificar onde o modelo se desviou. Também foi abordado o **role-based prompting**, que consiste em atribuir uma persona ou papel ao modelo, como advogado, médico ou cientista de dados, para orientar tom, vocabulário, profundidade e prioridades da resposta. Por fim, foi apresentada a ideia de **instruction tuning via prompt**, em que o comando é escrito de forma altamente explícita, definindo conteúdo, estilo, restrições e tamanho da saída, sem alterar os pesos do modelo. A aula concluiu reforçando que não existe uma técnica única ideal: a melhor escolha depende do equilíbrio entre economia, controle e qualidade exigido pela aplicação.

**Pontos de atenção**  
- No **zero-shot**, a qualidade depende muito da clareza da instrução; se o pedido estiver ambíguo, a resposta tende a ficar vaga ou fora do formato desejado.  
- O **zero-shot** é mais indicado para tarefas simples, conhecidas pelo modelo ou quando não há exigência forte de estrutura.  
- No **few-shot**, a escolha dos exemplos é crítica: exemplos ruins induzem padrões ruins e pioram a saída.  
- O **few-shot** consome mais tokens e exige mais tempo para selecionar exemplos representativos.  
- O **CoT** aumenta a transparência, mas também deixa a resposta mais longa e mais cara, especialmente em chamadas de API.  
- O raciocínio passo a passo do **CoT** não deve ser aceito cegamente; é importante validar se o modelo não “inventa” etapas ou justificativas.  
- Em tarefas simples, o **CoT** pode ser excessivo; vale usar quando houver raciocínio multi-etapa, cálculo ou lógica mais complexa.  
- No **role-based prompting**, uma persona mal definida pode deixar a resposta artificial, estreita ou pouco útil.  
- A personalização por papel geralmente exige iteração e testes para ajustar o comportamento do modelo.  
- No **instruction tuning via prompt**, a precisão do comando precisa ser alta; quanto mais detalhado o objetivo, estilo e restrições, melhor tende a ser o resultado.  
- Modelos diferentes podem reagir melhor ou pior ao mesmo estilo de prompt; é importante testar a técnica no modelo específico da aplicação.  
- A técnica ideal depende do trade-off entre custo, controle e precisão, então a escolha deve ser feita caso a caso.