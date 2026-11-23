Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17395)

## Resumo da aula

O arquivo de inicialização precisa começar com uma linha que diga imediatamente o que o projeto é, qual tecnologia principal usa e qual problema resolve. Essa linha funciona como orientação inicial para o agente decidir com que tipo de ambiente, convenções e comandos ele está lidando. Um exemplo adequado seria algo como “API REST em FastAPI para autenticação de usuários”. O objetivo não é documentar o sistema inteiro, mas reduzir a ambiguidade logo na primeira leitura.

Esse arquivo deve ser curto porque ele compete por espaço no contexto carregado pelo agente. Quanto maior o texto, maior o custo de tokens e maior o risco de partes relevantes serem ignoradas ou perderem prioridade operacional. Concisão, porém, não significa remover informação crítica: o arquivo precisa ser pequeno sem ficar vago. O critério correto é manter apenas o que altera a execução prática do agente.

Comandos recorrentes devem aparecer com sintaxe completa para evitar que o agente invente flags, opções ou variações inexistentes. Isso inclui build, testes e outros comandos usados com frequência, sempre com os parâmetros exatos aceitos pelo projeto. A utilidade desse bloco é operacional: ele substitui adivinhação por execução reproduzível. Quando o comando já está pronto no arquivo, o agente parte para a ação em vez de explorar alternativas.

Regras de estilo genéricas, como “formate corretamente”, são fracas porque deixam espaço demais para interpretação. O arquivo fica mais útil quando explicita convenções concretas, como TypeScript strict mode, indentação de dois espaços ou proibição de type any. Esse tipo de instrução orienta a geração de código de forma compatível com o padrão real do projeto. O resultado é menos retrabalho em revisão e menos divergência entre o que a IA produz e o que o time aceita.

Listar diretórios importantes ajuda o agente a navegar com menos exploração, especialmente em monorepos ou repositórios grandes. Em vez de depender apenas da árvore completa do projeto, o arquivo destaca os pontos de entrada que realmente importam para a execução e modificação do código. Isso reduz custo de busca e acelera a localização de componentes relevantes. O ganho é maior quando a estrutura do repositório permite múltiplos caminhos plausíveis.

Retomando o arquivo de inicialização já estabelecido, ele não deve conter o processo completo de desenvolvimento, mas os microcomportamentos esperados enquanto o agente está trabalhando. Entram aqui instruções como abertura de PR, padrão de branches, critérios de code review, limites de escopo e momentos em que uma verificação manual é obrigatória. Essas orientações existem para alinhar a execução da IA ao modo real de trabalho da equipe. O agente pode saber abrir uma PR, mas ainda precisa saber como abrir a PR correta naquele projeto.

Algumas instruções não são apenas preferências de workflow, mas restrições explícitas, como nunca fazer push na main, revisar a descrição do commit antes de enviar ou evitar testes redundantes. Essas regras delimitam o espaço de ação do agente em pontos críticos que não podem depender de inferência. Elas são especialmente importantes em contextos enterprise, nos quais erro operacional pode violar política interna ou gerar retrabalho desnecessário. O arquivo deve registrar essas proibições de forma direta e inequívoca.

Problemas frequentes do ambiente também merecem espaço quando afetam a execução prática, como porta ocupada ou exigência condicional de variáveis de ambiente. Esse bloco não substitui README nem scripts; ele apenas antecipa gotchas que costumam interromper o fluxo normal. A vantagem é evitar que o agente trate falhas recorrentes como incidentes inéditos. Quando o problema comum já está descrito, a recuperação fica mais rápida e previsível.

Nem todo conhecimento operacional deve ficar concentrado no arquivo principal. Quando um assunto é importante, mas detalhado demais para o contexto inicial, o melhor caminho é apontar para arquivos menores e específicos, como um guia de coding style ou uma regra local mais extensa. Essa divisão preserva a utilidade do arquivo principal sem inflá-lo. A lógica é simples: o índice inicial orienta, e os arquivos de referência aprofundam apenas quando necessário.

Criar esse arquivo já exige clareza sobre o que entra e o que fica de fora; mantê-lo exige disciplina para acompanhar a evolução do projeto. Sempre que comandos, regras, diretórios ou políticas mudam, o arquivo precisa continuar refletindo o fluxo oficial, ou ele passa a induzir erro com aparência de verdade. A qualidade do artefato depende menos de volume e mais de atualização. Um arquivo curto, preciso e mantido vale mais do que um documento extenso desatualizado.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]