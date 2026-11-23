Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16612)

## Resumo da aula

Uma resposta ruim da IA não deve encerrar o processo com frustração; ela deve iniciar um diagnóstico. Em vez de apenas concluir que “o código ficou um lixo”, o passo útil é fazer um Code Review da saída e mapear falhas concretas: uso de bibliotecas antigas, arquivos grandes demais, funções desnecessárias, abandono de implementação no meio do caminho e quebra de padrões do projeto. Esse mapeamento transforma erro difuso em problema observável e corrigível. O valor está em converter reclamação em especificação.

Tratar a IA como um funcionário no primeiro dia ajuda a ajustar expectativa e método. Um funcionário novo erra porque ainda não conhece regras locais, convenções do time, versões corretas de dependências e limites de escopo; com a IA acontece o mesmo em cada novo chat. Essa metáfora existe para deslocar o foco de “a ferramenta falhou” para “o processo de instrução ainda está incompleto”. O efeito prático é passar a treinar o sistema com regras explícitas, em vez de esperar alinhamento implícito.

Cada erro recorrente pode virar uma instrução permanente. Se a IA importou um pacote obsoleto, registre a regra correta, mostre o import errado e o import certo e acrescente a exigência de consultar a documentação antes de escolher bibliotecas daquela família. Se ela cria funções desnecessárias, adicione uma verificação obrigatória para revisar redundância após cada implementação. Documentar assim reduz repetição de falhas e cria memória operacional fora do modelo.

Guidelines são regras curtas e acionáveis que orientam comportamento recorrente do modelo. Elas podem limitar tamanho de arquivo, exigir funções limpas, pedir reaproveitamento de código existente ou obrigar retomada de contexto após interrupção. Diferentemente de uma correção pontual no chat, uma guideline é escrita para ser reutilizada em execuções futuras. Isso transforma aprendizado local em padrão de trabalho.

Few-shot é a técnica de fornecer poucos exemplos para induzir o padrão desejado. No caso discutido, isso aparece quando se mostra explicitamente um import incorreto e outro correto, ou quando se exemplifica a forma esperada de saída. O modelo não recebe apenas uma regra abstrata; ele passa a ter pares concretos de comparação para imitar. Isso é especialmente útil quando a diferença entre certo e errado depende de convenções específicas do projeto ou da stack.

Quando o prompt inclui instruções como “após criar qualquer função, revise se ela realmente é necessária”, ele força uma sequência de raciocínio operacional. Aqui, chain of thought importa menos como explicação interna do modelo e mais como estrutura de passos: implementar, revisar, comparar com o que já existe e só então manter a solução. Esse encadeamento reduz respostas impulsivas e aumenta autocorreção. Em engenharia de software, isso serve para conter proliferação de código desnecessário.

Skeleton of thoughts é uma forma de orientar a estrutura do pensamento ou da resposta por meio de um esqueleto explícito. Quando você combina exemplos com uma forma mais específica de saída, está delimitando não só o conteúdo, mas a organização da resposta. Isso ajuda quando a IA até entende a tarefa, mas entrega em um formato confuso ou difícil de revisar. O ganho principal é previsibilidade estrutural.

Retomando a ideia de prompt como artefato projetado, a base de conhecimento criada a partir desses erros também precisa de organização. Conforme guidelines, exemplos e restrições crescem, um arquivo desestruturado passa a gerar mais ambiguidade em vez de mais controle. O mesmo cuidado usado para manter testes automatizados legíveis vale aqui: clareza, separação de responsabilidades e manutenção ao longo do tempo. Mais informação só ajuda quando está organizada.

Os limites de comportamento, já estabelecidos anteriormente, ganham aqui uma função de treinamento acumulativo. Se a IA abandona um arquivo ao ser interrompida, a instrução não deve apenas corrigir o erro atual, mas definir a regra futura: terminar o arquivo atual antes de mudar de direção, ou corrigir e depois retomar exatamente do ponto onde parou. Esse tipo de limite reduz bugs introduzidos pelo próprio fluxo conversacional. O objetivo deixa de ser só responder melhor e passa a ser operar melhor dentro do workflow.

Quando erros documentados viram guidelines, exemplos e restrições reutilizáveis, o conjunto deixa de ser improviso e vira ativo do projeto. Esse ativo reduz dependência de memória individual, acelera onboarding de novos chats e melhora consistência entre tarefas de desenvolvimento, agentes e geração de documentos. Ele não elimina falhas, porque modelos continuam probabilísticos, mas diminui reincidência e encurta o caminho até uma saída útil. O ganho acumulado aparece com o tempo, não em uma única interação.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior, eu passei aqui para você uma situação comum que pode acontecer com você no dia de desenvolvimento, principalmente quando você está desenvolvendo em equipe. Esse tempo atrás, eu tive o prazer de conversar com algumas pessoas, alguns desenvolvedores, e eu acabo percebendo que tem muitos desenvolvedores que realmente possuem uma frustração muito grande com a OEA.

00:29

E eu não vou tirar a legitimidade disso, porque, em tese, ele está pedindo algo e a IA não está fazendo da forma como ele espera. Então, a gente tem um problema de expectativa aí, tá? Mas, chega um momento do seu trabalho, do seu dia a dia, com o seu estresse, que você acaba falando a seguinte coisa. Eu vou escrever assim, ó... O código que a IA

00:58

gerou para mim é um lixo. Eu estou simplesmente parafraseando o que esse meu camarada, colega de profissão falou aqui para mim.

01:13

E por que ele falou isso? Porque é o seguinte, a tecnologia que ele estava utilizando, ela tinha muitas versões, tinha muita confusão de versão, e as coisas começavam a sair do controle, porque, ora, ela pegava algo numa versão mais nova,

01:30

algo na versão mais antiga, era uma aplicação front-end, então tinha muitas mudanças sensíveis, ainda mais em interface, e o resultado final que ele falou é que o código que a IA gerou para mim é um lixo, tá? Ok, tudo bem, né? Beleza, vamos partir do princípio que é um lixo. E daí ele falou que tentou várias vezes e o código continuava a ser um lixo.

01:57

E a minha resposta pra ele, na realidade, a minha resposta pra ele foi uma outra pergunta. E eu quero que você faça essa pergunta pra você toda vez que você for inserir um prompt na hora de você desenvolver uma aplicação. Ok, temos um diagnóstico. O código da IA realmente é um lixo.

02:22

Vamos partir desse princípio que o código realmente é um lixo. Agora, o que eu preciso de você é o seguinte. Vamos fazer um Code Review de um lixo. Code Review de um lixo. E uma vez que eu vou fazer um Code Review de um lixo, eu vou mapear o seguinte. Olha, ele fez uma função totalmente

02:50

com bibliotecas antigas, ele criou arquivos muito grandes, ele também gerou funções desnecessárias, ele também, a Iá também fez o que no meio dessa história? Iniciou o trabalho

03:20

em um arquivo, e quando ela foi interrompida pela gente para uma instrução, para corrigir o caminho, vamos dizer assim, ou seja, às vezes a gente está desenvolvendo com o IA, você vê que ela está fazendo besteira, você escreve lá no chat, olha, não faz assim, é dessa forma. Aí o que a IA fez?

03:44

Ela iniciou o trabalho em um arquivo que, quando ela foi interrompida, ela foi interrompida, ela, adivinha o que ela fez nesse caso, quando ela foi interrompida? Ela voltou a ajustar o que você pediu e largou o arquivo que você estava usando pela metade, tá?

04:09

Ou seja, ela gerou, no final das contas, um bug e deixou você ali na mão. Então, vamos imaginar que ela gerou todos esses problemas ali ainda.

04:21

ali pra mim. Fora isso, ela mudou alguns padrões nos seus arquivos e, no final das contas, deu tudo errado. Então, uma vez que você chega a essa conclusão, você pode ter dois posicionamentos. Um posicionamento é voltar a xingar e aí falou que é um lixo e fazer do seu jeito e, sei lá, tentar de novo, gastar seu tempo e os seus resultados não melhoram.

04:45

A segunda forma que você pode resolver realmente é vamos fingir que a Yá aqui não é uma Yá. Vamos fingir que ela é um colega seu de trabalho e que você tem um carinho enorme com essa pessoa e ela realmente está fazendo o melhor dela. Vamos partir desse princípio.

05:05

E o que você vai perceber aqui nesse momento? Quando você for fazer esse Code Review, você vai perceber o seguinte, que ela utilizou uma função antiga. Então, você vai mapear o seguinte. Olha, você usou o pacote X, mas você deveria ter usado o pacote Y.

05:38

from x import y e daí você coloca errado e depois você coloca um outro exemplo from x import j e aqui é certo e depois tá explica que todas as vezes que ela for fazer algo parecido ela vai ter que

06:08

fazer essa correlação para nunca mais, nessa situação, isso acontecer. Mas, além disso, você pode passar uma instrução adicional que será o seguinte. Antes de importar um pacote dessa família ou dessa versão, pesquise as documentações,

06:38

na web, no Context 7, não interessa, tá? E garanta que você está utilizando a última versão. Ok? Isso aqui vai resolver 100% o problema que vai acontecer. Será que ela nunca mais vai importar uma versão antiga? Talvez ela vá implementar. O problema, nesse caso, é que agora você tem uma informação adicional

07:05

que ela tinha. E, provavelmente, esse erro aqui que ela cometeu, ela não vai cometer mais. Ou, se ela vier a cometer, você pode restringir ainda mais. Ela criou arquivos muito grandes. Então, você pode colocar ali Guidelines. Não crie arquivos com mais de 100 linhas. Tente

07:34

a trabalhar com funções limpas e, se necessário, crie arquivos e interfaces para melhorar a compreensão. Estou dando um exemplo aqui. Então, coloquei mais essa guideline, aí ela gerou funções desnecessárias. Opa, se ela gerou funções desnecessárias, eu posso chegar e falar assim para ela, após criar

08:03

qualquer função, revisite e veja se realmente ela é necessária ou se não existe algo similar.

08:21

já implementado. Então, se você perceber, o que eu estou fazendo? Eu estou criando mais uma guideline aqui para ela trabalhar. Aí, a gente tem uma situação que é grave, que é o seguinte. Todas as vezes que eu passar uma instrução para fazer um ajuste em determinada tarefa,

08:52

Aqui eu posso escolher, termine a implementação do arquivo atual e depois siga as minhas instruções. Hoje em dia já tem IDS que coloca todas as suas mensagens numa fila para evitar esse tipo de coisa, mas ainda assim pode acontecer.

09:16

Ou você pode falar aqui para ela o seguinte, olha só, você está fazendo isso no caminho errado, então corrija isso e não esqueça de voltar e continuar de onde você parou. Então, isso também já vai fazer com que isso acabe melhorando. Então, perceba, galera,

09:38

que a grande questão aqui é que, ao longo do tempo, você vai começar a estruturar os seus prompts com uma base de conhecimento, guidelines, exemplos e coisas desse tipo, que vão fazer com que aquele código lixo, pelo menos naquele contexto, esse problema vai ser minimizado.

10:01

E a recomendação que eu dou para você é que todas as vezes que a IA não gerou algo que te agrade, você documente para ela ao invés de passar raiva. Pense que ela é um novo funcionário, que ela não conhece direito a empresa, ela está no primeiro dia dela. Cada chat que você iniciar,

10:21

é um funcionário que acabou de chegar na empresa. Então, partindo desse princípio, o que vai acontecer é que, ao longo do projeto, isso aqui vai se tornar um ativo e vai fazer com que a IA não caia em tantas mais pegadinhas que a gente acaba trabalhando. Uma coisa que você vai perceber é que, muitas vezes, você vai perceber que, por exemplo, isso aqui, aqui no meio dessa história,

10:50

é um, por exemplo, um FillShotPrompt, por exemplo. Por que é um FillShot? Porque eu estou dando alguns exemplos aqui para ela. Então, toda vez que eu vou dar um exemplo aqui para ela, ela vai ter

11:07

como copiar e transpor aquilo que ela pensava que era para um outro trabalho. Todas as vezes que eu gerar esses tipos de guidelines, eu tenho um outro formato de prompt. Por exemplo, após criar qualquer função, revisite se realmente ela foi necessária. Então, o que ela está fazendo? Ela está gerando uma linha de pensamento para ela

11:35

encadear um próximo passo. Então, isso aqui, para a gente, pode ser também um chain of thought. Uma outra coisa que a gente pode falar aqui também, é que toda vez que você dá um few shot e traz, como exemplo, a saída aqui que a gente acaba escolhendo, no final das contas, a gente poderia dizer

12:03

que poderia ser uma espécie de um skeleton of thoughts, porque você está sendo um pouco mais específico de como você quer a saída. Então, se você perceber, até mesmo nesses exemplos que acontecem para a gente no dia a dia, a gente está utilizando diversas técnicas de prompt. O grande problema é que, se você começa a criar os seus arquivos e os seus prompts de formas desestruturadas, assim, no seu processo de trabalho,

12:33

vai ficar um pouco de bagunça até mesmo para você manter esse arquivo. Vamos imaginar, pessoal, que você está criando um teste automatizado.

12:43

Meus, os testes automatizados têm que estar muito claros. Eles têm que estar bem feitos. Eu tenho que poder olhar o meu teste automatizado e garantir que eu estou entendendo o que ele está fazendo, porque ele vai crescer ao longo do tempo. E você saiba que os seus prompts ou os seus arquivos, a sua base de conhecimento que você vai passar para lá, vai crescer ao longo do tempo. Então, se você não tiver uma estrutura clara,

13:08

para fazer esses tipos de coisa e, intencionalmente, entender o tipo de prompt que você precisa, simplesmente, você vai gerar um arquivo insustentável, vai gerar mais ambiguidade, porque, às vezes, mais informação gera mais ambiguidade e aí ela começa a fazer coisas piores do que você estava mandando menos informação. Então, qual é o meu objetivo aqui nesses dois exemplos que eu trouxe aqui para você?

13:34

é que todas as vezes que a IA gerar algo que você não espera, é porque você não define os limites e o comportamento, e toda vez que ela gerar algo que é muito ruim,

13:48

Tente abstrair que ela é um funcionário, e como funcionário, ela chegou no dia 1 e ela fez do jeito que ela imaginava, e você vai ter que treinar esse seu funcionário. O grande ponto é que esse seu funcionário, no dia seguinte,

14:05

Quando você iniciar um novo chat, ou seja, chegou um funcionário ainda mais novo na sua empresa, o que você vai fazer? Ele já vai ter essas regras e esses erros vão ser minimizados. Eu nunca vou falar que esses erros nunca mais vão aparecer.

14:20

porque não é assim que a coisa funciona, mas você vai ter uma minimização. Agora, imagine ao longo dos anos, ao longo dos tempos, como que esses tipos de coisa vão poder melhorar aí para você. Então, eu só queria trazer isso um pouco mais para a nossa realidade antes de eu começar a falar especificamente de como você pode estruturar um prompt para que você realmente entenda que...

14:50

Existem formas que não é só ficar escrevendo dessa forma ou passar instruções pra IA no chat dessa forma. Existem formas bem inteligentes e essas formas não são apenas para o nosso workflow de desenvolvimento, tá? Isso aqui é um dos pontos importantes.

15:08

Eu tenho, sim, processos de workflow de desenvolvimento, mas eu tenho agentes que precisam processar informação para um cliente final, eu quero explorar e pegar novas possibilidades, eu quero fazer geração de documentos, eu quero fazer muita coisa com o IA. Então, o que acontece aqui é o seguinte, se eu não tiver uma estrutura clara, simplesmente eu não vou conseguir o meu resultado.

15:28

E, novamente, nenhuma estratégia de estruturação vai resolver todos os seus problemas. A gente vai ver diversas estratégias na nossa frente, a gente vai testar, a gente vai escrever prompt e a gente vai brincar bastante. E eu espero que você consiga sair utilizando isso no seu trabalho o quanto antes. Fechou? Então, vamos nessa!

## Resumo IA

**Abreviações**
- IA — Inteligência Artificial
- Code Review — Revisão de código
- prompt — instrução ou comando textual dado ao modelo
- guidelines — diretrizes/regras orientativas
- few-shot — técnica de prompting com poucos exemplos
- chain of thought — encadeamento de raciocínio em etapas
- skeleton of thoughts — esqueleto de pensamento; estrutura base da resposta

**Resumo**
A aula explica como lidar com respostas ruins da IA no desenvolvimento de software sem cair na frustração, transformando a falha em diagnóstico. Em vez de simplesmente concluir que o código “é um lixo”, o instrutor propõe fazer um Code Review da saída gerada para identificar problemas concretos, como uso de bibliotecas antigas, arquivos grandes demais, funções desnecessárias, interrupção de implementação no meio do caminho e quebra de padrões do projeto.

Para isso, a aula usa a metáfora de tratar a IA como um funcionário no primeiro dia: ela ainda não conhece as convenções, regras e limites do time, então precisa ser treinada com instruções explícitas. A partir dos erros observados, o conteúdo orienta a documentar correções como regras reutilizáveis, criando uma base de conhecimento com guidelines, exemplos e restrições. Assim, cada falha recorrente deixa de ser apenas uma correção pontual e passa a virar instrução permanente para interações futuras.

O instrutor mostra como isso se relaciona com técnicas de prompting. Quando são dados exemplos de import errado e import certo, há uso de few-shot para induzir o padrão desejado. Quando se pede para revisar se uma função é realmente necessária após criá-la, há uma sequência de raciocínio operacional associada ao chain of thought. Quando a saída é guiada por uma forma mais específica e estruturada, isso se aproxima de skeleton of thoughts. O objetivo é tornar o comportamento da IA mais previsível, autocorrigível e aderente ao workflow.

A aula também destaca a importância de organização: à medida que as regras, exemplos e restrições crescem, os prompts e arquivos de conhecimento precisam permanecer claros e sustentáveis, do mesmo modo que testes automatizados bem escritos. O fluxo proposto é observar o erro, mapear o problema, transformar a falha em guideline, adicionar exemplos concretos, impor limites de comportamento e reutilizar esse material para reduzir reincidência em novos chats e novos contextos de trabalho.

**Pontos de atenção**
- Não encerrar o processo com frustração; use a resposta ruim como ponto de partida para diagnóstico.
- Fazer Code Review da saída da IA e identificar falhas concretas, em vez de avaliar de forma genérica.
- Registrar erros recorrentes como regras permanentes, para evitar repetição em novos chats.
- Sempre conferir versões e documentação antes de aceitar bibliotecas ou pacotes sugeridos pela IA.
- Adicionar guidelines para limitar tamanho de arquivos, evitar funções desnecessárias e estimular código limpo e reaproveitável.
- Exigir que a IA revise redundâncias após implementar uma função.
- Definir o comportamento quando houver interrupção: terminar o arquivo atual ou retomar exatamente do ponto onde parou.
- Evitar arquivos de base de conhecimento ou prompts desestruturados, pois isso aumenta ambiguidade.
- Manter prompts e regras claros e sustentáveis, como se fossem testes automatizados bem documentados.
- Entender que as técnicas ajudam, mas não eliminam totalmente os erros; o ganho é reduzir reincidência e aumentar consistência.