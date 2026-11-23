Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16619)

## Resumo da aula

Uma estrutura reutilizável de prompt organiza a instrução em blocos previsíveis, em vez de depender de um pedido solto e genérico. Isso reduz variações desnecessárias na interpretação do modelo e facilita reaproveitar o mesmo formato em tarefas diferentes. O ganho principal não é “ter um template bonito”, mas transformar uma necessidade difusa em uma solicitação mais operacional e verificável.

Auditar dependências de bibliotecas significa verificar se um projeto usa versões atualizadas, componentes depreciados ou pacotes com falhas de segurança conhecidas. Esse é um problema real de engenharia porque afeta manutenção, risco operacional e exposição a vulnerabilidades. Um prompt estruturado ajuda porque delimita exatamente o que deve ser inspecionado e qual tipo de resposta é esperado da análise.

Ambiguidade em prompts operacionais surge quando a instrução permite múltiplas interpretações sobre tarefa, critério ou formato de resposta. Em um cenário como auditoria de dependências, um pedido genérico pode produzir uma resposta superficial, incompleta ou inconsistente entre execuções. Estruturar o prompt é uma forma de restringir liberdade onde a previsibilidade importa.

A mesma lógica de estruturação pode ser usada fora da análise de código, desde que exista uma tarefa com instruções, limites e resultado esperado bem definidos. Um agente corporativo que recebe orientações para executar uma atividade interna também depende de clareza sobre o que fazer e como responder. O valor da estrutura está menos no domínio e mais na capacidade de explicitar intenção, contexto e restrições.

Nenhuma estrutura única de prompt resolve todos os problemas de uma empresa ou de um sistema baseado em agentes. Cada contexto impõe exigências próprias de entrada, saída, risco, autonomia e validação, então o formato precisa ser adaptado. A estrutura base funciona como ponto de partida confiável, não como receita universal.

Persona, escopo, objetivo, entrada, saída, critérios, ambiguidade e instruções negativas formam os blocos que tornam o prompt mais controlável. Cada bloco reduz um tipo específico de incerteza: quem executa, o que está dentro do limite, qual resultado deve ser produzido, com quais dados e sob quais restrições. Esses elementos servem como gramática operacional para agentes que precisam agir de modo consistente.

## Transcrição

00:01

Bom, pessoal, agora que a gente entendeu uma estrutura básica para que a gente consiga criar um prompt de uma forma um pouco mais organizada, eu vou mostrar para você um prompt que eu uso para verificar dependências de bibliotecas no meu projeto.

00:17

Muitas vezes eu quero saber se estou usando últimas versões, se estou usando bibliotecas depreciadas ou com falhas de segurança e etc. Então, eu utilizo essa mesma estrutura de prompt, mas para fazer essa varredura de dependências nos meus projetos.

00:33

Agora, eu tenho um ponto bem importante que eu quero falar aqui para você, que é o seguinte, eu estou utilizando essa estrutura para esse tipo de prompt para verificar a vulnerabilidade, mas eu estou mostrando esse exemplo porque é algo mais mundo real, dia a dia, de nós desenvolvedores.

00:52

Por outro lado, isso não impede que você use essa mesma estrutura em outro contexto que não seja o contexto de desenvolvimento. Por exemplo, imagina que você está integrando uma aplicação de inteligência artificial na sua empresa e você precisa passar instruções claras para o agente que você está desenvolvendo.

01:12

Então, eventualmente, você pode utilizar essa estrutura. E por que eu digo eventualmente? Como eu disse, não é uma única estrutura de prompt que vai resolver todos os problemas da sua vida, da empresa que você trabalha e tudo mais. Mas isso aqui é um bom começo e agora eu vou começar a mostrar na prática para que a gente consiga fazer um depara ali em relação ao que eu criei, tá? Então, no próximo vídeo agora aqui, a gente vai começar

01:39

analisar a persona, escopo, objetivo, entrada, saída, critério, ambiguidade, instruções negativas e etc. Vamos nessa!

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial

**Resumo**  
A aula apresenta o uso de uma estrutura reutilizável de prompt para tornar instruções mais organizadas, previsíveis e verificáveis, em vez de depender de pedidos genéricos e ambíguos. O instrutor usa como exemplo um prompt que ele aplica para auditar dependências de bibliotecas em projetos, verificando se há versões desatualizadas, bibliotecas depreciadas ou pacotes com falhas de segurança conhecidas. A ideia central é que um prompt estruturado reduz variações na interpretação do modelo e ajuda a delimitar com clareza o que deve ser analisado, qual formato de resposta é esperado e quais restrições devem ser respeitadas.  

Também é destacado que essa abordagem não se limita ao desenvolvimento de software: ela pode ser aplicada em outros contextos, como na criação de agentes de IA para tarefas internas em empresas, desde que exista uma atividade com instruções, limites e resultado esperado bem definidos. O instrutor reforça que não existe uma estrutura única capaz de resolver todos os cenários; por isso, o formato do prompt deve ser adaptado conforme o contexto, o risco, a autonomia necessária e o tipo de validação. Por fim, ele antecipa que a estrutura será decomposta em blocos como persona, escopo, objetivo, entrada, saída, critérios, ambiguidade e instruções negativas, que funcionam como uma gramática operacional para aumentar a consistência das respostas.

**Pontos de atenção**  
- Prompts genéricos podem gerar respostas superficiais, incompletas ou inconsistentes.  
- A ambiguidade em instruções operacionais compromete a previsibilidade da análise.  
- Estruturar o prompt não é apenas “deixá-lo bonito”; o objetivo é torná-lo operacional e verificável.  
- A mesma estrutura não resolve todos os casos: ela deve ser adaptada ao contexto, risco e validação necessários.  
- Em auditoria de dependências, é importante delimitar claramente o que será inspecionado e qual tipo de saída é esperado.  
- Os blocos do prompt ajudam a reduzir incertezas específicas: quem executa, o que está no escopo, com quais dados, qual resultado e sob quais restrições.  
- Instruções negativas são relevantes para evitar interpretações indesejadas e respostas fora do esperado.  
- A estrutura serve como ponto de partida confiável, não como receita universal.