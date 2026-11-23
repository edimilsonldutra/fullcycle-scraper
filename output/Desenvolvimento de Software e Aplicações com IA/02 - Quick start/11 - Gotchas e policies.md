Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17399)

## Resumo da aula

Uma Git policy para agentes transforma regras de segurança em instruções explícitas de operação. O ponto central não é ensinar Git do zero, mas impedir que a IA aplique hábitos genéricos perigosos, como force push, hard reset ou alterações de configuração sem pedido explícito. Esse bloco também define o formato esperado de commit, como conventional commits, para reduzir ambiguidade na hora de registrar mudanças. Quando a política é clara, o agente deixa de improvisar em operações com alto impacto no histórico.

Comandos destrutivos precisam de proibição nominal, não de bom senso presumido. Regras como nunca usar force push na main ou master, nunca pular hooks com --no-verify e só usar amend quando for realmente seguro reduzem risco operacional imediato. A justificativa é simples: o custo de um erro em Git costuma ser maior do que o custo de uma instrução extra no arquivo. Em projetos assistidos por IA, esse tipo de restrição funciona como contenção de dano.

Nem toda proteção precisa ficar no arquivo de inicialização; parte dela pode ser automatizada com hooks. Hooks permitem interceptar ações antes ou durante a execução de comandos, bloqueando comportamentos indesejados sem depender apenas de instrução textual. Isso é especialmente útil para linting, validações e políticas que devem ser aplicadas sempre, mesmo quando o agente não consulta o contexto com atenção suficiente. A combinação correta é: o arquivo registra a regra crítica, e a automação reforça o cumprimento quando possível.

Gotchas são armadilhas específicas do projeto que a IA tende a repetir porque não são óbvias a partir da estrutura do repositório. Em vez de documentar teoria ampla, o arquivo deve registrar erros observados na prática e convertê-los em exemplos acionáveis de certo e errado. Esse padrão melhora o comportamento do agente porque ataca falhas reais, não hipóteses abstratas. Retomando a lógica das regras restritivas já estabelecidas, aqui a diferença é que o foco sai da proibição geral e entra na pegadinha concreta do código.

Em interfaces React, alguns erros aparecem de forma recorrente e merecem virar instrução explícita. Casos como propagação de clique em links, uso incorreto de elementos interativos dentro de Next.js Link, override indevido de refs do react-hook-form e wrappers HTML que não preservam onChange são exemplos de falhas que quebram comportamento sem parecerem graves à primeira vista. Quando esses pontos entram no arquivo com exemplos curtos, o agente passa a reconhecer padrões locais em vez de aplicar soluções genéricas. O valor está em registrar exatamente o que já deu errado naquele projeto.

Além de policies e gotchas, o arquivo pode carregar observações curtas que alteram a execução técnica do trabalho. Exemplos típicos são compatibilidade de tipos de banco, necessidade de rodar alembic upgrade head após atualizar mudanças com migrations e a possibilidade de desenvolver o front-end isoladamente com MSW mocks. Essas notas só merecem entrar quando são estáveis e realmente mudam a ação do agente. Se a informação muda o tempo todo, ela deve sair do contexto inicial e ir para outro lugar.

O limite útil do arquivo não é um número fixo, mas a capacidade de permanecer denso, estável e acionável. Um arquivo com cerca de 287 linhas pode ser adequado se cada bloco reduzir erro ou ambiguidade real; crescer sem critério só aumenta custo de manutenção e ruído. A pergunta correta não é “o que mais cabe aqui?”, mas “o que é útil para o projeto e não muda toda hora?”. Esse critério separa contexto operacional de inventário frágil.

Retomando o arquivo de inicialização já definido anteriormente, a evolução relevante aqui é tratá-lo como mecanismo de governança contínua. Sempre que a IA repete um erro perigoso no Git, quebra um padrão de formulário ou ignora uma particularidade operacional, a correção deve virar policy, gotcha ou automação complementar. Esse ciclo transforma falhas recorrentes em regras concretas e reduz a necessidade de intervenção manual futura. Um documento vivo não cresce por acumulação aleatória; ele melhora por refinamento guiado por erro observado.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]