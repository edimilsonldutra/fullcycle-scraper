Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16610)

## Resumo da aula

Prompt não é improviso textual; é um artefato projetado para induzir um comportamento específico do modelo. Isso importa porque a qualidade da resposta depende menos de “escrever bonito” e mais de explicitar intenção, contexto e formato esperado. Quando o prompt é tratado como projeto, ele passa a ser ajustado conforme o caso de uso, em vez de reaproveitado como uma fórmula universal.

Nenhuma estratégia de prompting resolve todos os problemas com o melhor resultado em qualquer cenário. Um workflow de desenvolvimento, um agente que atende cliente, uma exploração para decidir arquitetura e a geração de um documento exigem estruturas diferentes porque pedem raciocínios, restrições e saídas distintas. A consequência prática é simples: escolher a estrutura do prompt faz parte da solução, não é um detalhe de implementação.

A estrutura adequada nasce do objetivo operacional do prompt. Se a tarefa é apoiar um workflow de desenvolvimento, a organização tende a privilegiar etapas, critérios e continuidade entre interações; se a tarefa é responder ao cliente final, o foco muda para robustez, interpretação de entradas variadas e consistência de resposta. Quando o objetivo é explorar alternativas de arquitetura, o prompt precisa abrir espaço para comparação e análise; quando a meta é gerar um documento, a prioridade passa a ser formato, seções e completude.

Separar o prompt em partes e seções reduz a mistura de intenções dentro do mesmo pedido. Em vez de concentrar tudo em um bloco único, a estrutura pode distinguir objetivo, contexto, tarefa e saída esperada, o que torna a instrução mais legível tanto para quem escreve quanto para o modelo. Essa organização não é um template fixo, mas uma forma de tornar explícito o que antes estava implícito e ambíguo.

Ambiguidade surge quando o prompt mistura exploração, análise e geração sem dizer qual delas tem prioridade. Ao reorganizar o mesmo pedido em seções, fica mais claro o que o modelo deve fazer, com base em qual contexto e em que formato deve responder. O efeito esperado é maior previsibilidade: a resposta tende a variar menos de forma indesejada e a ficar mais alinhada ao resultado que o caso de uso realmente pede.

Observar prompts prontos ajuda a identificar padrões recorrentes de estruturação. Esse reconhecimento não serve para copiar cegamente um formato, mas para perceber como diferentes tipos de problema pedem diferentes arranjos de instruções. Com o tempo, esse repertório permite diagnosticar prompts confusos e reorganizá-los de forma mais intencional.

## Transcrição

00:01

Bom, pessoal, agora chegou a hora de a gente falar sobre estruturação de prompts e estratégias de utilização. A primeira coisa que eu já quero começar deixando claro aqui pra você, tá? Independente da estratégia que você vá utilizar pra estruturar os seus prompts,

00:16

Essas estratégias não conseguem ser coringas, ou seja, uma estratégia vai fazer com que você consiga resolver todos os seus problemas da sua vida com prompts e você sempre vai ter o melhor resultado. Entenda que quando você quer trabalhar com um processo de workflow de desenvolvimento, provavelmente você vai usar um tipo de estrutura. Se você precisa desenvolver um agente que precisa, vamos dizer assim, processar qualquer tipo de informação para responder ao cliente final, você vai ter uma outra estrutura.

00:46

Se você quiser fazer uma exploração e entender melhores estratégias para chegar na arquitetura do software que você quer, novamente, é um outro tipo de prompt. Eu preciso gerar um documento, outro tipo de prompt também.

01:02

Então, o ponto principal desse capítulo aqui é que você entenda que essas estratégias para a gente estruturar prompts vão dar algumas bases para a gente. Porém, o que eu vou trazer aqui para vocês é uma base inicial para que você entenda

01:21

como que você pode estruturar os seus prompts, não necessariamente da forma como eu vou mostrar, mas ele pelo menos consegue abrir um pouco mais a sua mente de partes e sessões no processo de estruturação. Então, esse aí é o nosso principal objetivo e eu vou trazer aqui alguns exemplos e a gente também vai praticar bastante em relação a isso e nós vamos ver alguns prompts

01:47

prontos para que você consiga identificar esses tipos de padrão. Maravilha? Então, vamos nessa, pessoal, porque a gente vai falar sobre estruturação de prompts agora.

## Resumo IA

**Abreviações**
- **workflow**: fluxo de trabalho
- **prompt**: instrução ou comando textual dado ao modelo de IA

**Resumo**
A aula apresentou a ideia de que prompt não deve ser tratado como improviso textual, mas como um artefato projetado para induzir um comportamento específico do modelo. O instrutor reforçou que a qualidade da resposta depende menos de “escrever bonito” e mais de explicitar intenção, contexto e formato esperado. A principal mensagem foi que não existe uma única estratégia de prompting que funcione como solução universal para todos os cenários.

Foi explicado que diferentes objetivos exigem diferentes estruturas de prompt. Um workflow de desenvolvimento, um agente voltado ao atendimento do cliente, uma exploração para decisões de arquitetura e a geração de documentos pedem raciocínios, restrições e saídas distintas. Por isso, escolher a estrutura do prompt faz parte da solução e não é apenas um detalhe de implementação.

A aula também destacou que a estrutura adequada nasce do objetivo operacional da tarefa. Quando o foco é apoiar um workflow de desenvolvimento, o prompt tende a organizar etapas, critérios e continuidade entre interações. Quando o objetivo é responder ao cliente final, a ênfase vai para robustez, interpretação de entradas variadas e consistência. Para exploração de arquitetura, o prompt precisa permitir comparação e análise; para geração de documentos, deve priorizar formato, seções e completude.

O instrutor explicou que separar o prompt em partes e seções ajuda a reduzir a mistura de intenções dentro do mesmo pedido. Em vez de concentrar tudo em um único bloco, a estrutura pode distinguir objetivo, contexto, tarefa e saída esperada, tornando a instrução mais clara tanto para quem escreve quanto para o modelo. Essa organização foi apresentada como uma forma de explicitar o que estava implícito ou ambíguo.

Por fim, foi ressaltado que prompts ambíguos costumam misturar exploração, análise e geração sem definir qual delas tem prioridade. Ao reorganizar o pedido em seções, o modelo entende melhor o que fazer, com base em qual contexto e em que formato responder. O resultado esperado é maior previsibilidade e alinhamento com o caso de uso. Também foi mencionado que observar prompts prontos ajuda a reconhecer padrões de estruturação e a desenvolver repertório para diagnosticar e reorganizar prompts confusos de maneira mais intencional.

**Pontos de atenção**
- Não tratar nenhuma estratégia de prompt como “coringa” para todos os problemas.
- Escolher a estrutura do prompt de acordo com o objetivo operacional da tarefa.
- Evitar misturar no mesmo pedido exploração, análise e geração sem definir prioridade.
- Separar claramente objetivo, contexto, tarefa e saída esperada.
- Para workflows de desenvolvimento, priorizar etapas, critérios e continuidade entre interações.
- Para agentes voltados ao cliente final, priorizar robustez, interpretação de entradas variadas e consistência.
- Para exploração de arquitetura, deixar espaço para comparação e análise.
- Para geração de documentos, especificar formato, seções e completude.
- Usar exemplos de prompts prontos como referência de padrões, sem copiar de forma cega.
- Reorganizar prompts confusos de forma intencional para aumentar previsibilidade e reduzir ambiguidades.