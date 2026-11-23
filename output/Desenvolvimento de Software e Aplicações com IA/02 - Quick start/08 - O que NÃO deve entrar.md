Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17396)

## Resumo da aula

O arquivo de inicialização do agente deve conter apenas informação que muda a decisão do agente e que ele não consegue obter com segurança por conta própria. Se o conteúdo é dedutível pela estrutura do repositório, pelo código existente ou por convenções já visíveis, ele tende a ser redundante. A exclusão não é estética; ela reduz ruído, custo de tokens e manutenção desnecessária. O arquivo fica melhor quando funciona como filtro de decisão, não como espelho do repositório.

Nomes de arquivos, funções, classes e outros elementos estruturais normalmente não precisam ser fixados no arquivo. Modelos atuais conseguem navegar pela árvore de diretórios, reconhecer padrões de nomenclatura e localizar os pontos mais prováveis de interesse sem receber esse inventário pronto. Quando essa informação já é recuperável pelo próprio agente, repeti-la no contexto inicial consome espaço sem aumentar muito a precisão. O ganho real aparece apenas quando há algo não óbvio naquele ponto do projeto.

Frases como “use boas práticas” ou “não escreva código inseguro” são amplas demais para orientar comportamento concreto. O agente já tende a seguir os padrões que encontra no código e, sem especificidade local, esse tipo de instrução pouco altera a execução. Se houver uma preferência real da equipe, ela precisa ser expressa de forma mais específica, como uma convenção técnica ou restrição verificável. Regra vaga ocupa contexto, mas não reduz ambiguidade.

Informação volátil é um mau candidato para o arquivo de inicialização porque envelhece rápido. Quando você fixa nomes de arquivos, funções ou classes que mudam com frequência, o arquivo passa a carregar instruções potencialmente incorretas. Isso é pior do que omissão, porque o agente pode confiar em um caminho errado e tomar decisões baseadas em contexto falso. O critério aqui é simples: quanto maior a chance de mudança, menor a chance de esse dado merecer contexto pré-carregado.

Documentação longa de API, bibliotecas ou detalhes amplos do sistema raramente deve entrar diretamente no arquivo principal. Além de aumentar o custo de tokens, esse volume pode não ser relevante para a tarefa atual e competir com instruções mais acionáveis. Retomando a estratégia de importação de arquivos de referência, detalhes estáveis e extensos pertencem melhor a documentos separados, consultados quando necessário. O arquivo principal deve permanecer curto o suficiente para priorizar o que afeta a primeira decisão.

Um bom teste de poda é perguntar se o conteúdo muda com frequência, se é grande demais ou se já se explica sozinho pelo código e pela estrutura do projeto. Se a resposta for sim, a tendência é remover. Isso inclui conhecimento cotidiano de desenvolvimento que não representa uma regra local importante. O objetivo não é empobrecer o arquivo, mas preservar apenas o que realmente orienta ação em vez de repetir o óbvio.

A regra de não listar arquivos tem exceções legítimas. Alguns projetos possuem arquivos marcantes: pontos específicos que concentram uma pegadinha conhecida pelo time, um comportamento vital ou uma armadilha recorrente que o agente dificilmente inferirá apenas lendo a estrutura. Nesses casos, mencionar o arquivo no cloud.md faz sentido porque a informação não está ali para catalogar o repositório, mas para evitar erro recorrente. A exceção se justifica quando aquele arquivo altera risco, não quando apenas existe.

Listar muitos nomes de arquivos ou funções transforma o arquivo em inventário frágil. Destacar um único arquivo crítico, por outro lado, é uma intervenção cirúrgica: você aponta um lugar cujo impacto operacional é desproporcional ao seu tamanho. A diferença está no motivo da inclusão. Se o dado entra porque é vital e não dedutível, ele merece estar ali; se entra apenas porque existe, provavelmente deve sair.

A estrutura exata do cloud.md não precisa seguir um modelo rígido de tópicos numerados ou seções padronizadas. O que precisa permanecer estável é o raciocínio de seleção: incluir o que orienta decisões e excluir o que o agente já consegue descobrir, o que muda demais ou o que é genérico demais. Esse critério produz arquivos diferentes entre projetos, mas com a mesma qualidade operacional. A consistência vem da lógica de poda, não do formato visual.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]