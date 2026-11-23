Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16398)

## Resumo da aula

Top-p já foi definido anteriormente; aqui o ponto central é observar que seu efeito costuma ser mais sutil do que o da temperatura. Em vez de produzir mudanças muito evidentes em estilo ou criatividade, ele refina o conjunto probabilístico de candidatos elegíveis para a próxima escolha. Por isso, a diferença entre duas execuções pode ser pequena e, em alguns casos, quase imperceptível. Essa característica exige testes mais controlados para que a comparação tenha valor técnico.

Retomando o exemplo de continuação de frase, o valor de top-p funciona como um corte por massa acumulada de probabilidade. Se os tokens mais prováveis somam 90% ao alcançar o terceiro candidato, o modelo passa a amostrar apenas dentro desse subconjunto e ignora o restante. Com top_p = 0.9, o conjunto pode incluir várias opções; com um valor mais baixo, como 0.6, o corte pode ficar tão restrito que sobra apenas o token dominante. O efeito prático é reduzir ou ampliar a variedade possível sem fixar uma quantidade rígida de candidatos.

O máximo de tokens, já visto antes, precisa estar configurado corretamente para não contaminar o teste. Se esse valor estiver em zero ou muito baixo, a execução falha ou a saída é truncada, e a comparação deixa de medir top-p para medir limitação de geração. Antes de comparar respostas, ajuste esse parâmetro para um valor suficiente para a tarefa. Sem esse cuidado, qualquer conclusão sobre top-p fica tecnicamente fraca.

Usar múltiplas mensagens no Playground é a forma mais prática de comparar saídas lado a lado sem perder a execução anterior. Ao criar uma nova mensagem, a resposta anterior permanece visível acima, o que facilita inspecionar diferenças de escolha lexical, continuidade e grau de variação. Esse procedimento é melhor do que sobrescrever a mesma execução, porque preserva o contexto da comparação. Quando o efeito é sutil, a inspeção visual simultânea passa a ser parte do método.

Mantenha o mesmo prompt e altere apenas o valor de top_p. Primeiro, execute com um valor mais restritivo, como 0.1, e confirme que o máximo de tokens não está impedindo a geração; depois rode novamente com um valor mais amplo, como 0.9, em uma nova mensagem. Compare as duas saídas observando se a continuação ficou mais fechada nas opções mais prováveis ou se ganhou alguma flexibilidade adicional. Se a diferença parecer pequena, isso não invalida o teste: faz parte do comportamento esperado desse parâmetro.

A comparação não deve buscar apenas mudanças grandes de conteúdo, porque top-p frequentemente atua em nuances. Observe se a resposta repete caminhos mais previsíveis, se escolhe palavras mais conservadoras ou se admite pequenas alternativas de formulação quando o limiar aumenta. Em muitos casos, a estrutura geral permanece parecida e a diferença aparece apenas na seleção de termos ou na abertura para variações locais. Ler o resultado com esse critério evita a falsa impressão de que o parâmetro “não fez nada”.

## Transcrição

00:01

Bom pessoal, deixa eu mostrar então para vocês um pouquinho como vai funcionar o Top P.

00:06

Vamos lá, vamos lembrar o que é o Top P antes de eu começar a mostrar para vocês. O Top P é uma evolução, posso dizer que ele é uma evolução do Top K, o jeito mais fácil de explicar, não o mais científico e o mais correto, mas é o jeito mais fácil de vocês entenderem para que serve o Top P. Top P então é como se fosse um Top K aperfeiçoado, o que ele vai fazer? Ele dá mais abertura para você conseguir evoluir as LLMs. O que ela vai ter por trás? Pensa que o Top P é como se fosse os Top principais

00:36

como é que eu posso dizer, são os top principais

00:42

probabilidades da próxima palavra acontecer, de ser aquela próxima palavra. Então, você abre uma janela de oportunidade aqui. Então, imagina o seguinte, imagina que você está construindo uma frase como a gente fez várias vezes aqui. Então, imagina que você tem lá uma frase do tipo, o cachorro latiu hoje cedo. O cachorro latiu hoje cedo. O cachorro latiu hoje cedo. Cinco palavrinhas aqui, certo? Você tem dentro desses cinco tokens, vamos imaginar que são cinco tokens,

01:08

você tem o modelo de probabilidade de cada um deles acontecer. Então, o cachorro latiu hoje e está cedo aqui no final. Então, onde normalmente deveria chegar é no cedo. Para uma LLM, ela vai chegar no modelo probabilístico que mostra isso. O TopP pode abrir ou fechar esse modelo probabilístico de uma forma mais abrangente ou menos abrangente. Como isso funciona? Imagina que a gente tem então

01:34

o cachorro latiu hoje cedo o cedo quero que ele descubra então vamos focar no cedo imagina que ele está o cachorro latiu hoje aí tem a palavra cedo pode ser a próxima palavra pode ser hoje na cozinha latiu hoje

01:55

muito hoje babá imagina que ele tem lá várias palavras que podem aparecer aqui junto com ser então tem várias palavras no modelo probabilístico deles algumas com mais probabilidade outras com menos de ser a palavra que você está procurando se você chegar e falar o seguinte olha

02:11

cedo tem uma probabilidade de 30% dentro deste grupo de palavras. Então, imagina que ele chegou em 10 palavras, das 10 palavras, cedo tem 30% de probabilidade. Ou melhor, tem 60% de probabilidade, tá bom? Para facilitar a nossa conta aqui e ficar mais rápida.

02:28

Então, CEDO tem 60% de probabilidade. NA tem 20% de probabilidade. Então, 60, 70, 80%. Tô somando aqui. E quando eu olho pra hoje, CEDO, NA e sei lá...

02:47

Cozinha, que possivelmente tem uma probabilidade baixa, vai ter sei lá, 10% de probabilidade. Tô colocando uma alta aqui só pra gente chegar na conta rápida, tá? Então você tem cedo com 60, na com 20 e cozinha com 10.

03:02

Se você fechar o seu modelo probabilístico em 90%, você está vendo que a soma aqui já deu 90? Então, 0,9 significa que você está pegando de 0% até 90% do modelo probabilístico que você quer pegar. Quando a soma disso bater 90,

03:20

Você pega aquele grupo de palavras e dentro dele você escolhe qual você quer usar. Então, você deixa isso aberto para a sua LLM trabalhar em cima deste contexto. Ou seja, aqui nesse contexto, imagina que ele tinha lá um grupo de 10 palavras, ele vai fechar só nas três primeiras e desprezar as demais para usar essas três primeiras, porque já bateu o peso dele de 90. Então, quando eu venho aqui e coloco topP 9, eu estou dizendo isso para ele. Se eu colocasse topP nesse cenário que eu dei, 60, ele vai pegar só a primeira palavra, só o cedo.

03:47

Então ele basicamente vai fechar mais ou menos isso. Isso é um jeito muito, muito, muito, muito simplificado de contar assunto para facilitar a vida de vocês. Mas é mais ou menos assim que o Top P vai funcionar. Beleza? Vamos ver ele funcionando na vida real? Então imagina que eu pego aqui um Top P de 0,1 para ele fechar na palavra mais próxima na geração. Vamos ver o que vai acontecer.

04:11

Ixi, olha lá. Aquele erro que eu falei pra vocês é isso aqui, ó. Ele deu o máximo de tokens. Aqui, ó. Deixei o máximo zero e não consegue rodar. Que bom que deu erro. Vou abrir ali o máximo de token pra um tanto legal. Eu vou deixar ele rodar. Depois que ele terminar de rodar, eu vou gerar um pra gente tentar comparar

04:38

com ele no máximo e a gente vê se ele vai gerar algum tipo de variação aqui que a gente consegue pegar. Nem sempre gera, tá? O Top P é mais sutil. Nas experiências que eu fiz até hoje, ele acaba sendo um pouquinho mais sutil. Vamos deixar ele com 1, que é o máximo. Não, vou deixar 0,9.

04:55

e dar um run aqui pra gente ver o que acontece. Eu cliquei aqui, vocês viram que eu cliquei em nova mensagem e eu vou colocar aqui outra e daí dentro de outra ele vai criar pra baixo, ele não vai jogar aquela de cima pra fora, tá? Isso é bom pra quando você quer fazer algum tipo de teste e comparativos, tá vendo? Então, ó, ele ficou de cima ali e agora tem um de baixo aqui pra gente testar. Vamos ver o que ele vai gerar de diferente.

05:31

Ó, algumas coisas importantes, você já vê que olha...

## Resumo IA

**Abreviações**  
- **Top P**: *Nucleus Sampling*; estratégia de amostragem que considera os tokens até atingir uma massa acumulada de probabilidade definida por um limiar.  
- **Top K**: estratégia de amostragem que restringe a escolha aos K tokens mais prováveis.  
- **LLM**: *Large Language Model*; modelo de linguagem de grande porte.

**Resumo**  
A aula explicou o funcionamento do Top P como um mecanismo de amostragem que controla a variedade das respostas de uma LLM por meio de um corte baseado em massa acumulada de probabilidade. O instrutor comparou o Top P ao Top K de forma didática, destacando que o Top P não fixa uma quantidade rígida de candidatos, mas seleciona dinamicamente os tokens mais prováveis até alcançar um limiar, como 0,9 ou 0,6. Foi usado o exemplo de continuação de frase para mostrar que, ao atingir o percentual configurado, o modelo passa a amostrar apenas dentro do subconjunto escolhido e descarta as alternativas restantes.

Também foi reforçado que o efeito do Top P costuma ser mais sutil do que o da temperatura, podendo gerar diferenças pequenas entre execuções. Por isso, a comparação precisa ser feita com cuidado, mantendo o mesmo prompt e alterando apenas o valor de Top P. O instrutor mostrou a importância de configurar corretamente o máximo de tokens, pois um valor inadequado pode truncar a saída ou impedir a geração, contaminando o teste e tornando inválida a análise do parâmetro.

Na demonstração prática, foi sugerido executar primeiro com um Top P mais restritivo, como 0,1, e depois com um valor mais amplo, como 0,9, utilizando novas mensagens no Playground para preservar as execuções anteriores e comparar os resultados lado a lado. O fluxo recomendado foi observar se a resposta fica mais conservadora, fechada nas opções mais prováveis, ou se ganha flexibilidade lexical e pequenas variações de formulação. O instrutor enfatizou que, mesmo quando a diferença parece pequena, isso é esperado e faz parte do comportamento do Top P.

**Pontos de atenção**  
- Configurar corretamente o **máximo de tokens** antes do teste; se estiver muito baixo ou em zero, a saída pode falhar ou ser truncada.  
- Comparar sempre **mantendo o mesmo prompt** e alterando apenas o valor de **Top P**.  
- Lembrar que o efeito do **Top P é sutil**; diferenças pequenas não significam ausência de impacto.  
- Não interpretar o resultado apenas por mudanças grandes de conteúdo; observar também **nuances lexicais** e pequenas variações locais.  
- Usar **novas mensagens no Playground** para comparar execuções lado a lado sem sobrescrever a anterior.  
- Testar com valores contrastantes, como **0,1** e **0,9**, para facilitar a percepção do comportamento.  
- Entender que o Top P trabalha por **massa acumulada de probabilidade**, e não por número fixo de opções.  
- Evitar concluir que o parâmetro “não fez nada” quando a estrutura geral da resposta permanecer parecida; isso pode ser esperado.