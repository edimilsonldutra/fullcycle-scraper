Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17530)

## Resumo da aula

A skill MCP Builder pode ser disponibilizada no Cloud Code apenas copiando sua pasta para o diretório de skills da ferramenta. Retomando o front matter já visto anteriormente, o carregamento inicial consome poucos tokens porque o agente lê primeiro só a descrição e decide aprofundar apenas quando a tarefa exige. Esse comportamento preserva janela de contexto e permite manter skills instaladas sem pagar o custo completo de todas elas o tempo todo.

Um one-shot prompt bem específico consegue acionar automaticamente a skill correta quando a intenção da tarefa está clara. Aqui, o pedido descreve um servidor MCP em TypeScript para uma pasta guides-mcp, com guias de linguagens e boas práticas, além de tools para listar guias, consultar conteúdo e responder perguntas baseadas nesses arquivos. A precisão do prompt importa porque é ela que sinaliza ao agente que o problema pertence ao domínio coberto pela skill.

O modo planning por si só já organiza etapas, mas a skill adiciona estrutura especializada ao plano. Em vez de produzir um roteiro genérico, o agente passa a considerar organização de diretórios, uso do SDK, padrões esperados de implementação e critérios de validação próprios de um servidor MCP. O ganho não está apenas em “planejar”, mas em planejar segundo um padrão técnico reutilizável.

O servidor foi planejado com três tools centrais: uma para listar guias disponíveis, outra para obter o conteúdo de um guia e outra para consultar esse conteúdo. Esse desenho separa descoberta, leitura e consulta semântica, o que reduz ambiguidade na interface do servidor. Em um MCP orientado a conteúdo, essa divisão facilita tanto a implementação quanto o consumo pelas aplicações clientes.

Lembra do carregamento on-demand de referências já discutido? Aqui ele aparece de forma concreta: o agente não se limitou ao skill.md, mas também incorporou instruções dos arquivos auxiliares da skill. Isso fica evidente quando o plano inclui detalhes de evaluation e critérios de qualidade que não estavam apenas na descrição principal.

A evaluation não entra como etapa opcional no fim; ela faz parte da definição do que significa “servidor pronto”. O plano inclui um evaluation.xml, perguntas de teste e restrições como execução não destrutiva e validação read-only. Esse acoplamento entre implementação e avaliação reduz a chance de aceitar um servidor que compila, mas não responde corretamente aos cenários esperados.

Um modelo mais rápido e mais barato pode entregar resultado útil quando recebe uma skill bem construída. A skill funciona como uma estrutura operacional que compensa parte da limitação do modelo, guiando decisões de arquitetura, implementação e teste. Isso não elimina revisão posterior, mas desloca parte da inteligência do processo para um artefato reutilizável.

Mesmo usando cerca de metade da janela de contexto, o processo conseguiu carregar a skill, implementar o servidor e executar validações. O custo observado não veio só da skill ou do código gerado, mas também da tendência do agente de produzir documentação e sumários em excesso. Esse padrão mostra que otimizar instruções de projeto, como em CLOUD.md, também é uma forma de controlar consumo de tokens.

Uma skill bem escrita captura padrões de desenvolvimento que normalmente ficam dispersos em documentação, memória da equipe ou preferência individual. Quando esses padrões viram skill, até modelos menos sofisticados conseguem iniciar projetos e manter consistência com mais velocidade. O efeito prático é transformar conhecimento operacional recorrente em um mecanismo acionável pelo agente.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]