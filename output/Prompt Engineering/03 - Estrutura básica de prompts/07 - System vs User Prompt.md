Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16616)

## Resumo da aula

System Prompt é a camada que define as regras permanentes da interação. Ele estabelece comportamento do modelo, tom de resposta e restrições gerais, funcionando como um manual de instrução do agente. Retomando a ideia de limites de comportamento já vista antes, a diferença aqui é de posicionamento: essas regras ficam na camada global da conversa, não no pedido pontual. Por isso, o System Prompt tende a mudar pouco e serve como base estável para múltiplas interações.

User Prompt é a instrução variável que descreve o que o usuário quer naquele momento. Esse usuário pode ser uma pessoa, outro software ou até outro agente de IA, desde que esteja enviando a solicitação operacional da vez. A função dessa camada não é redefinir a identidade do agente, mas acionar uma tarefa concreta dentro das regras já estabelecidas. Em termos práticos, o User Prompt carrega a intenção imediata; o System Prompt define como essa intenção deve ser executada.

Muitos modelos tratam o System Prompt com prioridade maior do que o User Prompt. Isso significa que, em condições normais, o pedido específico é interpretado à luz das regras globais já definidas, em vez de substituí-las livremente. Essa hierarquia existe para dar consistência ao comportamento do modelo ao longo da conversa. Sem ela, cada nova mensagem poderia reconfigurar completamente o agente e reduzir previsibilidade.

O comportamento do modelo resulta da combinação entre instruções globais e pedidos locais, mas essa combinação não é mecanicamente garantida. Mesmo com uma separação clara entre System e User, a execução continua sujeita à natureza probabilística do modelo, algo já discutido anteriormente. Isso explica por que a arquitetura do prompt melhora consistência sem garantir obediência absoluta. A utilidade da separação está em reduzir ambiguidade e tornar o desvio mais controlável.

Jailbreak é a tentativa de fazer o modelo abandonar ou contornar instruções que deveriam permanecer válidas, como regras de comportamento definidas no System Prompt. Um exemplo típico é ordenar explicitamente que o modelo ignore suas instruções anteriores e passe a responder de outra forma. O ponto central não é o comando em si, mas o fato de ele atacar a hierarquia entre camadas. Quando isso funciona, o pedido local deixa de operar dentro da política global e passa a corroer essa política.

Prompt Injection é uma forma de induzir o modelo a reinterpretar ou ignorar instruções por meio de conteúdo inserido na interação. Diferentemente de uma configuração legítima do agente, a injeção tenta introduzir comandos concorrentes que desviam o comportamento esperado ao longo do fluxo. Isso contextualiza por que separar System e User é necessário, mas insuficiente como defesa completa. A estrutura ajuda a organizar autoridade, porém ainda existe fragilidade quando entradas maliciosas tentam reescrever essa autoridade.

A distinção operacional é simples: coloque no System Prompt o que deve valer de forma ampla e duradoura; coloque no User Prompt o que muda conforme a tarefa. Regras de comportamento, tom e restrições gerais pertencem à camada global, enquanto perguntas, tarefas e solicitações do momento pertencem à camada específica. Essa separação prepara a próxima etapa de estruturação do prompt, na qual seções internas podem ser organizadas dentro de cada camada. Primeiro define-se quem o agente é e como deve agir; depois define-se o que ele precisa fazer agora.

## Transcrição

00:01

Bom, pessoal, agora que a gente passou um pouquinho por essas guidelines, somente para você sentir um pouco mais o quão profundo é toda essa parte de Prompt Engineering, não é só os tipos de prompt, mas como ele afeta a vida e o ciclo de vida do software, é importante que a gente consiga revisitar alguns conceitos para que a gente entre numa linha de raciocínio aqui,

00:27

para eu mostrar uma forma sugerida para você ter como base, para você começar a estruturar os seus próprios prompts, tá? Então, a primeira coisa que eu quero falar aqui para vocês, talvez você já saiba, talvez você não saiba, mas é o seguinte, a gente tem alguns tipos de prompt, tá? Então, quando eu digo tipos de prompt é quando a gente vai iniciar uma nova conversa, um novo chat, uma nova interação com a inteligência artificial,

00:53

A gente tem duas coisas aqui. Uma coisa chamada System Prompt e outra coisa chamada User Prompt. Em alguns aspectos chamam de Human, no meio da história. Mas o que acontece é o seguinte. O que é o System Prompt? O System Prompt normalmente vai definir a regra do jogo.

01:13

Ele vai definir o comportamento da IA, o tom que ela vai responder, as restrições que a gente quer impor para o modelo. Ele deve ser como se fosse um manual de instrução permanente para que ela conversa. Geralmente, esse system prompt não muda muito.

01:31

porque ele é a instrução inicial. E um ponto importante é que muitos modelos tendem a ler esse system prompt de uma forma mais prioritária do que está no user, ou seja,

01:47

O System Prompt gera uma regra como se fosse global e ele fala assim, cara, essas são as minhas instruções, é assim que eu vou trabalhar e, ao longo da conversa, dependendo da forma como você interage com a IA, você começa a conseguir quebrar esse System Prompt.

02:06

falando, por exemplo, ignore o System Prompt. Ignore algumas instruções de comportamento que você tem e comece a se comportar dessa forma, uma tentativa de jailbreak, por exemplo. Mas, de forma geral, é importante que você tenha o System Prompt.

02:23

Segundo ponto aqui, nós temos o user prompt. O user prompt, no final das contas, é quando o usuário, e esse usuário pode ser um humano, ou pode ser um outro software, ou pode ser um outro agente de A, que ele vai pedir, fazer uma pergunta, vai pedir para realizar uma tarefa ou qualquer coisa desse tipo, tá?

02:42

E o user prompt pode mudar a cada interação. Então, da mesma forma que o system prompt se mantém fixo na maioria das vezes, o user prompt tende a mudar porque ele vai trabalhando com as interações. Então, a ideia do user prompt basicamente especifica

03:05

sendo a descrição do que o usuário quer naquele momento, já respeitando as regras do System Prompt.

03:14

Então, toda hora que você pensar em System Prompt versus User Prompt, você tem que ter uma nota mental. System é a configuração global da conversa. User, pedido específico que você quer que o modelo execute. Normalmente, o modelo vai executar o que você quer, mas utilizando as regras e as instruções e comportamentos que você definiu no System Prompt.

03:42

Tudo isso é na teoria, porque quando a gente começa a falar de aspectos como Prompt Injection, existem diversas formas que você tenta dar um trick, que você tenta meio que enganar um pouco o modelo para ele ir ignorando e mudando ao longo do tempo e perdendo essa essência aí do System Prompt, tá? Então, isso aí é um ponto mais do que importante para você ter em mente. Aí, fechou?

## Resumo IA

**Abreviações**  
- IA — Inteligência Artificial  
- Prompt Engineering — Engenharia de Prompts  
- System Prompt — Prompt de sistema  
- User Prompt — Prompt do usuário  
- Human — Humano  
- Jailbreak — tentativa de contornar ou burlar instruções e restrições do modelo  
- Prompt Injection — injeção de prompt  

**Resumo**  
A aula apresentou uma visão inicial sobre como estruturar prompts em interações com inteligência artificial, destacando que o Prompt Engineering vai além de apenas “escrever comandos” e influencia diretamente o comportamento do modelo ao longo do ciclo de uso. O instrutor explicou que, em uma nova conversa, existem duas camadas principais: o System Prompt e o User Prompt. O System Prompt funciona como a camada global e permanente da interação, definindo a regra do jogo, isto é, o comportamento esperado da IA, o tom das respostas e as restrições gerais. Ele tende a mudar pouco e serve como base estável para orientar a conversa inteira.

Em seguida, foi explicado que o User Prompt é a instrução variável, isto é, o pedido específico feito naquele momento por um humano, por outro software ou até por outro agente de IA. Diferentemente do System Prompt, o User Prompt muda a cada interação e contém a tarefa ou solicitação imediata, sempre respeitando as regras já definidas na camada global. O instrutor reforçou a hierarquia entre essas camadas, observando que muitos modelos priorizam o System Prompt, o que ajuda a manter consistência e previsibilidade no comportamento da IA.

A aula também abordou a limitação dessa arquitetura: embora a separação entre System e User melhore a organização e reduza ambiguidades, ela não garante obediência absoluta, pois o modelo ainda opera de forma probabilística. Nesse contexto, foram citados dois riscos importantes: Jailbreak, quando alguém tenta fazer o modelo ignorar instruções anteriores ou contornar restrições do System Prompt, e Prompt Injection, quando conteúdos inseridos na interação tentam induzir o modelo a reinterpretar ou abandonar instruções válidas. Por fim, o instrutor resumiu a regra prática: colocar no System Prompt o que deve ser amplo e duradouro, e no User Prompt o que é específico da tarefa atual, preparando a base para etapas futuras de organização interna do prompt.

**Pontos de atenção**  
- O System Prompt deve concentrar regras permanentes, comportamento, tom e restrições gerais.  
- O User Prompt deve conter apenas a solicitação pontual, sem tentar redefinir a identidade do agente.  
- O System Prompt costuma ter prioridade sobre o User Prompt, mas isso não é uma garantia absoluta de cumprimento.  
- A resposta do modelo continua sujeita ao comportamento probabilístico; a estrutura do prompt aumenta consistência, mas não elimina falhas.  
- Jailbreak é uma tentativa de fazer o modelo ignorar suas instruções base; é um risco direto à hierarquia entre camadas.  
- Prompt Injection é uma forma de inserir comandos concorrentes para desviar o comportamento esperado.  
- Separar System e User ajuda na organização e segurança, mas não é defesa completa contra entradas maliciosas.  
- Pensar sempre em “global vs. específico” facilita a construção correta dos prompts.  
- Primeiro define-se quem o agente é e como deve agir; depois define-se o que ele precisa fazer naquele momento.