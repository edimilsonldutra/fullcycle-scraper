Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17400)

## Resumo da aula

/init é um mecanismo de bootstrap que explora o codebase e gera um primeiro arquivo de contexto operacional para o agente. Ele existe para evitar que o projeto comece do zero, principalmente quando ainda não há um cloud.md, agents.md ou equivalente. O resultado costuma capturar stack, estrutura de pastas e um resumo do sistema, mas raramente traz com precisão os detalhes que mais afetam a execução diária. Por isso, /init serve como esqueleto inicial, não como versão final do arquivo.

Um arquivo esqueleto contém diretrizes genéricas extraídas do repositório; um arquivo intencional registra apenas o contexto que muda decisões operacionais do agente. A diferença prática é que o esqueleto descreve o projeto, enquanto o arquivo intencional orienta como trabalhar nele com previsibilidade. Se o agente sabe a arquitetura, mas não sabe como subir o ambiente, validar estado ou continuar uma tarefa sem se perder, o ganho operacional continua baixo. A evolução do arquivo consiste em transformar resumo estrutural em instrução acionável.

O primeiro refinamento do esqueleto deve se apoiar em quatro pilares: inicialização, state, testabilidade e feedback. Esses pilares já foram definidos anteriormente; aqui, eles funcionam como critério de priorização para o que entra primeiro no arquivo. Se o agente consegue iniciar o ambiente, verificar estado, testar corretamente e registrar ou retomar o trabalho sem ambiguidade, a maior parte dos erros operacionais desaparece. Esse conjunto resolve o básico que sustenta o restante do desenvolvimento assistido por IA.

Quando a ferramenta oferece /init, o fluxo inicial é simples: gerar o arquivo, inspecionar o resultado e começar a corrigir o que afeta a operação real do projeto. Se a ferramenta não oferece esse comando, o substituto é pedir à IA que leia a árvore de arquivos e produza um arquivo equivalente como rascunho inicial. Em ambos os casos, o objetivo não é confiar cegamente no texto gerado, mas acelerar a criação do primeiro artefato útil. O ganho está em começar com um mapa imperfeito e refiná-lo com intenção.

O arquivo gerado por /init pode acertar bem a arquitetura e ainda errar o que mais importa para o uso diário. No exemplo retomado do projeto de upload e transcrição de vídeos, o resumo identificou fluxo de dados, testes e componentes principais, mas falhou no modo correto de subir o ambiente ao sugerir algo incompatível com o uso de Docker. Esse tipo de erro mostra por que o arquivo inicial não pode ser aceito como verdade operacional. O critério de revisão é simples: manter o que reduz ambiguidade real e corrigir imediatamente o que induz execução errada.

O arquivo de inicialização precisa entrar no mesmo regime de qualidade aplicado a código que afeta todo o time. Code review, nesse caso, não é só leitura superficial: a equipe precisa verificar se a alteração mudou o comportamento do agente para melhor ou para pior. Como esse artefato influencia geração de código, execução de comandos e continuidade de tarefas, uma instrução ruim pode degradar a produtividade coletiva. Revisar esse arquivo com seriedade significa tratá-lo como infraestrutura operacional do desenvolvimento.

A revisão do arquivo não termina quando o texto parece correto; ela precisa incluir teste do comportamento induzido no agente. Uma mudança aparentemente pequena pode fazer o agente parar de usar o fluxo certo, esquecer comandos válidos ou voltar a inferir coisas que antes estavam explícitas. Por isso, o time deve validar cenários reais após alterações relevantes, especialmente nos pontos críticos já conhecidos. O arquivo melhora quando a revisão observa efeito prático, não apenas redação.

Quando o arquivo principal cresce demais, a solução não é empilhar texto, e sim separar conteúdo em arquivos auxiliares com títulos claros e pontos críticos bem destacados. A referência a importação de arquivos já foi estabelecida antes; aqui, ela entra como mecanismo de sustentabilidade do artefato ao longo do tempo. O arquivo principal deve continuar curto o bastante para ser sempre carregado e forte o bastante para orientar o agente nos casos recorrentes. Separar por seções preserva legibilidade sem perder profundidade onde ela realmente importa.

Skills são blocos de conhecimento que o agente carrega sob demanda, apenas quando a tarefa exige aquele contexto específico. Isso muda a estratégia de manutenção do arquivo principal, porque parte do conteúdo pode sair do carregamento permanente e migrar para um mecanismo mais especializado. A vantagem é reduzir duplicação e custo de contexto, mantendo no arquivo principal apenas o que precisa influenciar o agente em praticamente toda interação. Quanto mais madura a base de skills, mais importante fica decidir conscientemente o que permanece sempre carregado.

A regra prática é manter no arquivo principal apenas o conhecimento que o agente precisa saber sempre para operar corretamente no projeto. Se uma instrução é esporádica, muito específica ou só se aplica a certos fluxos raros, ela tende a caber melhor em uma skill. Esse critério evita a tentação de colocar “tudo” no contexto inicial, porque contexto excessivo dilui prioridade e reduz utilidade. O arquivo principal deve conter o mínimo indispensável para que o processo de desenvolvimento continue fluido.

Sempre que uma nova skill é criada, a equipe deve revisar se alguma instrução equivalente ainda está duplicada no arquivo principal. O problema da duplicação não é apenas estético: quando um lado muda e o outro não, a ambiguidade volta ao sistema e o agente passa a receber orientações concorrentes. Sincronizar significa decidir uma fonte de verdade para cada conhecimento operacional. O que é permanente fica no arquivo principal; o que é condicional ou especializado migra para skill.

README continua útil como documentação para humanos, mas não substitui um arquivo de inicialização voltado ao agente. Documentos humanos costumam ser longos, narrativos e cheios de detalhes que não alteram a ação imediata da IA. Já o arquivo principal precisa ser curto, operacional e escrito para reduzir inferência desde o primeiro carregamento. Precisão no desenvolvimento assistido por IA depende desse artefato específico, não da existência genérica de documentação no repositório.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]