Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17521)

## Resumo da aula

Skills são capacidades adicionais fornecidas ao agente para executar tarefas de domínio específico, seguindo padrões do projeto, da empresa ou de uma função técnica particular. Isso inclui comportamentos como atuar como code reviewer, aplicar boas práticas em Next.js ou estruturar componentes React com mais consistência. Embora quem execute o skill seja o agente de IA, pensar em Project Skills faz sentido no fluxo de desenvolvimento porque a definição dessas capacidades faz parte da preparação do projeto.

O ponto central não é apenas adicionar comportamento ao agente, mas evitar que todo o conhecimento especializado fique carregado o tempo inteiro. Quando instruções muito específicas são colocadas diretamente no contexto inicial, elas competem com o espaço necessário para programar. Skills resolvem esse problema ao separar conhecimento especializado do contexto base e ativá-lo apenas quando ele realmente é necessário.

O comportamento padrão de um skill é ser carregado on-demand, isto é, somente quando existe uma necessidade concreta relacionada àquela capacidade. O agente não precisa manter no contexto ativo todas as instruções de code review, React, Python ou padrões internos ao mesmo tempo. Esse carregamento sob demanda reduz desperdício de contexto e torna o uso de tokens mais eficiente.

A janela de contexto é o espaço finito em que o agente mantém instruções, histórico e artefatos necessários para continuar trabalhando. Esse espaço já começa parcialmente ocupado por elementos como system prompt, memory, arquivos de apoio como CLAUDE.md, descrições de servidores MCP, lista de agentes e descrições de skills. Se muito conteúdo especializado for incluído desde o início, sobra menos espaço útil para a tarefa principal de desenvolvimento.

Uma sessão pode começar com uma parcela relevante da janela de contexto já consumida antes mesmo da primeira solicitação útil. Além disso, quando o contexto se aproxima do limite, o agente precisa reservar tokens para compactar histórico e manter a conversa viável. Isso reduz ainda mais a área efetivamente disponível para produção de código e encurta a duração útil da sessão.

Retomando o cenário em que o agente alterna entre code review, React e Python, carregar tudo de uma vez faria o contexto nascer inflado. Com skills on-demand, o agente consome tokens apenas para conhecer a existência e a descrição dessas capacidades, trazendo o conteúdo detalhado somente quando a tarefa exigir. O efeito prático é mais espaço para raciocínio, mais fôlego de sessão e menor desperdício de tokens.

Um skill, no fim das contas, também é uma forma de prompt especializado. Por isso, alguns ambientes de codificação permitem não apenas o carregamento automático sob demanda, mas também a invocação explícita dessa capacidade. Essa possibilidade é útil quando o desenvolvedor quer garantir que um comportamento específico seja aplicado naquele momento.

Em ferramentas como o Cloud Code, um skill pode aparecer como slash command, permitindo sua execução manual por meio de um comando iniciado com barra. Nesse caso, o skill deixa de depender apenas da decisão automática do agente e passa a poder ser acionado diretamente pelo usuário. O modelo principal continua sendo on-demand, mas essa variação oferece controle adicional em cenários em que a ativação precisa ser explícita.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]