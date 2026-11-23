Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16600)

## Resumo da aula

Truncamento é o corte direto de partes do contexto para que a entrada caiba no limite disponível. Ele não reorganiza nem reinterpreta o conteúdo: apenas remove trechos. Essa técnica surge quando o histórico, as instruções e os dados enviados juntos excedem o espaço útil da chamada. Como a janela é finita, truncar é uma forma operacional simples de decidir o que fica e o que sai.

Retomando o cenário da aplicação, o sistema precisa continuar enviando conversa e instruções sem ultrapassar o limite de tokens já discutido. Quando o contexto cresce demais, alguma parte precisa ser descartada, e truncamento é a resposta mais direta para isso. A vantagem é simplicidade de implementação e previsibilidade de custo. O problema é que simplicidade não preserva significado automaticamente.

O caso mais comum é remover mensagens mais antigas para preservar o que acabou de acontecer na conversa. Ainda assim, truncamento não significa obrigatoriamente apagar o início do histórico. Se o prompt começa com instruções críticas, políticas de comportamento ou restrições que não podem sumir, esses trechos podem ser preservados de forma fixa enquanto o corte acontece em outra região. Isso transforma truncamento em estratégia de seleção, não apenas em descarte cronológico.

Alguns sistemas reservam uma faixa inicial do prompt que nunca é removida, como os primeiros mil tokens de instruções essenciais. O restante do espaço é disputado pelo histórico variável, que pode ser encurtado conforme a conversa cresce. Essa abordagem protege regras fundamentais do sistema, mesmo quando o histórico precisa ser comprimido à força. O efeito prático é manter estabilidade comportamental, ainda que parte da conversa seja sacrificada.

Truncamento pode remover mensagens inteiras ou cortar no meio de um bloco de texto, dependendo da implementação. Quando isso acontece, o modelo passa a enxergar apenas o trecho remanescente e perde a cadeia causal anterior. Se uma decisão atual dependia de contexto que ficou para trás, a resposta pode parecer incoerente, repetitiva ou sem noção do estado da interação. A perda de contexto é o principal trade-off dessa técnica.

Cortar contexto resolve o problema de caber na janela, mas não resolve automaticamente o problema de manter relevância. Em tarefas nas quais o histórico antigo contém dependências importantes, truncar pode degradar a resposta de forma significativa. Por isso, a escolha do ponto de corte precisa acompanhar o objetivo da aplicação e o tipo de informação que não pode ser perdido. Nas próximas estratégias, como sumarização e Sliding Window, a comparação central será exatamente entre simplicidade de corte e preservação de contexto.

## Transcrição

00:01

Bom, pessoal, agora a gente vai começar a entrar em aspectos que envolvem ali, mas, assim, muito diretamente a parte de Pronto Engineering, tá? E isso aí acabam virando como se fossem técnicas e algo muito comum que você vai ver o tempo todo

00:19

na hora de você desenvolver um software trabalhando com inteligência artificial, que são técnicas, uma delas é chamada de truncamento, o truncate, no final das contas. Basicamente, um truncamento vai remover parte menos relevante do contexto quando ele fica muito grande. E por que ele faz isso? Para a gente não encher a nossa janela de contexto e perder informação.

00:43

O grande ponto aqui de quando a gente trabalha com truncamento, a gente, no final das contas, está truncando, ou seja, a gente está cortando mensagem. E, normalmente, as mensagens que a gente corta são as mensagens mais antigas no início da conversa, tá? Então, basicamente, quando a gente fala em truncamento, a gente está falando em tentar cortar pedaços

01:07

de mensagens para ela caber na janela. O que normalmente acontece é que é cortada a mensagem mais nova para não perder dados recentes, mas isso não necessariamente é verdade. Por que eu estou dizendo? Vamos imaginar que eu tenho algumas instruções iniciais que são extremamente importantes.

01:28

E eu não posso perder isso de forma alguma. Então, eu posso, sim, querer fazer o truncamento do meu prompt, por exemplo, mas eu consigo garantir que aquele início, os mil primeiros tokens, por exemplo, eu sempre vou ter. E depois eu vou fazer um truncamento jogando fora o mais antigo para o mais novo, mas aquele início eu sempre mantenho. Então, lembre-se, pessoal, truncamento é cortar mensagem

01:58

para evitar ela ficar muito grande. É realmente cortar a mensagem. Agora, aonde você vai cortar vai depender da estratégia que você vai ter. Existem estratégias, depois a gente vai falar em seguida também ali de Sliding Window, por exemplo, que é um tipo de truncamento, mas lembre-se, truncar é cortar. Quando você corta, você pode cortar uma mensagem no meio do tipo, imagina que eu tenho aqui,

02:27

Eu vou cortar a partir daqui.

02:30

Então, quando o meu modelo vê, ele vai ver aqui, do início da conversa, mas ele perdeu, normalmente corta mensagens antigas. Ou seja, a partir daqui, ele perdeu completamente o contexto e pode acontecer que, a partir de agora, ele não tenha mais ideia do que está acontecendo porque ele perdeu esse início aqui, truncamento, remove parts, ele começa a olhar a partir daqui. Então, não necessariamente truncar é a melhor opção, tá?

03:00

E também, não necessariamente, truncar significa que você vai cortar o início da mensagem. Isso vai depender da estratégia que você vai ter na hora que você for criar seu prompt e conforme vai tendo as interações com o modelo.

03:19

Esse aí é um ponto importante que eu queria trazer aqui para vocês, porque tem muita gente que pensa que truncar é só jogar a mensagem antiga fora, ou truncar é colocar três pontinhos, ou qualquer coisa desse tipo. Não! Truncar você pode ter estratégias diferentes para você utilizar. O que eu estou querendo passar aqui, na realidade,

03:42

esses termos para a gente poder falar a mesma língua, porque quando a gente vai para a prática, eu vou começar a falar de truncamento, a gente vai falar de sumarização, esse tipo de coisa, e você precisa ter isso bem claro, bem ali sharp na sua cabeça, para você não ter problema de não conseguir acompanhar o curso ou ficar com dúvida no meio aí do processo, beleza? Próximo vídeo, a gente vai falar aqui de sumarização. Vamos nessa!

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **Prompt Engineering** — Engenharia de Prompt

**Resumo**
A aula apresentou a técnica de truncamento no contexto de aplicações com inteligência artificial e engenharia de prompt. O instrutor explicou que truncar significa cortar partes do contexto para que a entrada caiba no limite disponível da janela de contexto, sem reorganizar ou reinterpretar o conteúdo. Esse corte costuma ser aplicado quando histórico, instruções e dados juntos excedem o limite de tokens, sendo uma solução simples, previsível e comum na prática de desenvolvimento de software com IA.

Foi destacado que, em geral, o truncamento remove mensagens mais antigas para preservar o conteúdo recente, mas isso não é uma regra fixa. Dependendo da estratégia do sistema, trechos iniciais críticos, como instruções essenciais ou políticas de comportamento, podem ser preservados enquanto outras partes são removidas. O instrutor citou como exemplo a reserva de uma faixa inicial do prompt que nunca é truncada, mantendo regras fundamentais mesmo quando o restante do histórico precisa ser reduzido.

Também foi explicado que o truncamento pode ocorrer de formas diferentes: removendo mensagens inteiras ou cortando partes no meio de um bloco de texto. Em ambos os casos, o modelo passa a enxergar apenas o trecho remanescente, perdendo o encadeamento causal anterior. Isso pode gerar respostas incoerentes, repetitivas ou desconectadas do estado atual da conversa. A aula encerrou indicando que, nas próximas estratégias, como sumarização e Sliding Window, a comparação central será entre simplicidade de corte e preservação de contexto.

**Pontos de atenção**
- Truncamento não é apenas “apagar mensagens antigas”; é uma estratégia de corte de contexto.
- O ponto de corte depende da estratégia da aplicação e do que precisa ser preservado.
- Instruções iniciais críticas podem e, em alguns casos, devem ser mantidas fixas.
- Cortar o contexto resolve o problema de caber na janela, mas pode degradar a qualidade da პასუხa.
- Truncar pode remover mensagens inteiras ou cortar no meio de um bloco, dependendo da implementação.
- A perda de contexto pode gerar respostas incoerentes, repetitivas ou sem noção do estado da conversa.
- Em tarefas com dependências históricas importantes, truncamento pode não ser a melhor opção.
- É importante entender bem o conceito para acompanhar estratégias futuras, como sumarização e Sliding Window.