Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17529)

## Resumo da aula

O arquivo skill.md deve permanecer curto porque ele funciona como a camada de orientação de alto nível que o agente consulta primeiro. A recomendação prática é mantê-lo abaixo de 500 linhas, idealmente perto de 300, para reduzir carga de contexto e evitar que instruções detalhadas ocupem espaço desnecessário. O conteúdo principal resume fluxo, critérios e decisões essenciais; os detalhes extensos ficam fora dele. Essa separação permite que a IA resolva casos simples apenas com o arquivo principal e só aprofunde quando o problema exigir.

A pasta reference concentra documentos especializados que expandem pontos resumidos no skill.md. No exemplo do MCP Builder, a skill principal orienta a implementação e delega detalhes para guias específicos de Python ou TypeScript, além de documentos sobre convenções, estrutura de projeto e implementação de ferramentas. Como o agente lê apenas o que faz sentido para a tarefa atual, um projeto em TypeScript não precisa carregar o guia de Python. O ganho direto é economia de tokens e maior precisão, porque cada etapa consulta apenas a documentação relevante.

O skill.md pode repetir partes das referências, mas de forma condensada. Essa redundância é intencional: ela garante que o agente tenha uma visão operacional mínima sem precisar abrir arquivos longos a todo momento. Quando a tarefa exige mais profundidade, como detalhes de npm run build, convenções de nome ou estrutura exata de uma tool, os arquivos de referência entram como camada de baixo nível. A skill, portanto, organiza o conhecimento em níveis de granularidade diferentes.

Retomando a estrutura de skills já discutida, o avanço aqui está em usar fases explícitas para coordenar pesquisa, implementação, revisão e validação. No caso do MCP Builder, a fase inicial cobre planejamento, nomes de tools, discoverability, contexto, erros e estudo de protocolo; a fase seguinte direciona o setup e a implementação; depois vêm review, code quality, build e testes. Essa decomposição ajuda a IA a não misturar decisões arquiteturais com detalhes de execução. Cada fase define o tipo de informação que deve ser consultado e o critério de saída antes de avançar.

Evaluation não é apenas “testar se funcionou”; é uma etapa formal com regras próprias para validar o servidor MCP de forma consistente. O guia de avaliação define a criação de dez questões em linguagem natural, compreensíveis para humanos, read-only, independentes, não destrutivas e estáveis. Também especifica formato de saída, nível de complexidade, critérios de verificação e como as tool calls devem ser usadas durante os testes. Isso transforma validação em procedimento reproduzível, em vez de depender de inspeção manual ad hoc.

Em servidores MCP, o cliente precisa descobrir ferramentas disponíveis, escolher combinações de chamadas e processar respostas em formatos aceitáveis. Por isso, a avaliação precisa verificar não só se uma tool responde, mas se o fluxo completo de uso do protocolo permanece estável e interpretável. Um conjunto de perguntas mal definido pode gerar testes frágeis, destrutivos ou impossíveis de repetir. O Evaluation Guide existe para padronizar esse processo e tornar a validação confiável.

A skill não se limita a texto: ela pode incluir scripts executáveis que automatizam etapas do fluxo. No exemplo, há scripts para conectar ao servidor MCP, rodar a avaliação e consumir um arquivo gerado com as dez perguntas no formato esperado, além de dependências como requirements.txt. Isso permite que a IA não apenas leia instruções, mas execute procedimentos concretos para validar o resultado. A skill passa a combinar prompt, documentação e automação operacional.

Uma skill pode ser instalada no projeto, no ambiente do usuário ou diretamente na ferramenta/agente, sem necessariamente fazer parte do repositório da aplicação. Essa separação é importante porque a skill representa capacidade operacional reutilizável, não lógica de negócio do sistema em desenvolvimento. O mesmo conjunto de instruções, referências e scripts pode ser acionado por comando ou carregado em tempo de execução quando o agente detecta a necessidade. O efeito prático é transformar conhecimento especializado em um componente portátil.

Quando alguém pede “crie um MCP para integrar com a API dos Correios”, a skill pode ser chamada explicitamente e conduzir o processo inteiro. Ela orienta pesquisa inicial, escolhe o guia da linguagem correta, aplica convenções de implementação, executa build e testes e depois usa o fluxo de evaluation para validar o servidor. O valor não está apenas em descrever como criar MCPs, mas em estruturar a execução de ponta a ponta. A skill funciona como um roteiro acionável com profundidade progressiva.

O mesmo padrão aparece em uma skill para PDF: o skill.md concentra quick start e operações básicas como leitura, extração, split, merge e rotação de páginas, enquanto as referências cobrem processos avançados. Quando surge um caso específico, como preenchimento de formulários, entram scripts especializados como checkFillableFields. Assim, a IA deixa de improvisar repetidamente sobre o domínio e passa a operar com ferramentas e instruções já consolidadas. O resultado é mais consistência em tarefas recorrentes e menos esforço para resolver problemas conhecidos.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]