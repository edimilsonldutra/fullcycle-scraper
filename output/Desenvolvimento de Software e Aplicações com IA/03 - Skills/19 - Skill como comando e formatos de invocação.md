Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17547)

## Resumo da aula

Uma skill pode ser invocada não apenas por trigger semântico, mas também como slash command. No Cloud Code, isso transforma a skill em uma interface explícita de execução: em vez de esperar o modelo decidir usá-la, o usuário chama diretamente pelo nome. Essa convergência reduz a separação entre “comando” e “skill”, porque a mesma definição passa a servir tanto para automação contextual quanto para execução manual. Na prática, comandos tendem a virar skills reutilizáveis, enquanto comandos isolados ficam mais úteis apenas para casos muito específicos.

Retomando o front matter já definido anteriormente, ele continua orientando a ativação automática pelo modelo. A diferença aqui é que a mesma skill pode ter dois caminhos de entrada: o modelo pode carregá-la durante a conversa, ou o usuário pode chamá-la explicitamente com /nome-da-skill. Essa distinção importa porque cada modo de invocação atende um objetivo diferente: automação contextual no primeiro caso, controle operacional direto no segundo. Escolher entre os dois não muda o conteúdo da skill, mas muda quem tem permissão para iniciá-la.

A opção user invocable controla se a skill pode aparecer e ser executada como slash command. Quando essa opção é desabilitada, a skill deixa de estar disponível para chamada direta pelo usuário, mesmo que continue existindo e possa ser usada internamente pelo sistema. Isso é útil quando a skill foi projetada para ser acionada apenas no fluxo automático do modelo, sem exposição como comando público. O efeito prático é restringir o acesso manual e evitar uso indevido ou execução fora do contexto esperado.

Disable Model Invocation faz o inverso: impede que o modelo carregue a skill automaticamente durante a conversa. Nesse cenário, a skill continua podendo ser usada manualmente, desde que a invocação pelo usuário esteja habilitada. Essa configuração é adequada quando a skill deve funcionar como ferramenta explícita, acionada sob decisão humana, e não como parte da autonomia do modelo. O resultado é uma separação clara entre automação e comando manual.

As duas opções podem ser combinadas para definir exatamente quem pode iniciar a skill. Se user invocable estiver desabilitado, o usuário não chama por slash command; se Disable Model Invocation estiver ativo, o modelo não chama automaticamente. Isso cria uma matriz simples de controle: somente o modelo, somente o usuário, ambos ou nenhum, dependendo da configuração. Em ambientes com múltiplos usuários e skills sensíveis, esse controle evita exposição desnecessária e ajuda a impor o fluxo correto de uso.

Quando a skill é executada como comando, ela pode receber argumentos, funcionando de forma parecida com parâmetros de linha de comando. Esses valores permitem especializar a execução sem alterar a definição da skill, por exemplo informando caminhos, nomes ou opções de operação. A passagem de argumentos torna a skill mais operacional e previsível, porque o comportamento pode ser ajustado por entrada explícita do usuário. Isso aproxima o uso de skills do modelo mental já conhecido de CLIs e scripts.

Os argumentos podem ser interpretados por posição. Se o usuário passar A B C, o índice 0 corresponde a A, o índice 1 a B e o índice 2 a C. Esse mapeamento posicional é simples, mas exige consistência entre a forma de chamar o comando e a forma como a skill consome esses valores. Quando a ordem é bem definida, os argumentos passam a funcionar como variáveis de entrada para a execução.

argument hint e type hint servem para explicitar como os argumentos devem ser fornecidos. Eles não mudam a lógica da skill, mas melhoram a usabilidade ao orientar o preenchimento e facilitar sugestões da interface. Em ferramentas como o Cloud Code, isso reduz ambiguidade na chamada do comando e ajuda o usuário a fornecer entradas no formato esperado. O ganho principal é ergonomia operacional, não mudança semântica da skill.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]