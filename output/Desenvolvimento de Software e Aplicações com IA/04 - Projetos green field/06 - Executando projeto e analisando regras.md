Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17572)

## Resumo da aula

CLAUDE.md continua sendo o contrato operacional principal já estabelecido; o ponto novo aqui é evitar duplicação e divergência entre arquivos equivalentes. Como algumas ferramentas leem CLAUDE.md por padrão e outras podem usar AGENT.md, criar um link simbólico com ln -s faz um arquivo apontar para o outro e mantém uma única fonte de verdade. Isso reduz manutenção manual e impede que a IA opere com instruções diferentes dependendo do nome do arquivo encontrado.

Um projeto pronto para uso da IA não é apenas um repositório criado: ele precisa inicializar sem descoberta artesanal. O init.sh concentra setup de .env, instalação de dependências, prisma generate, atualização do banco, carga de seeds, subida do servidor e health check em uma rotina única. Esse encadeamento importa porque transforma várias pré-condições implícitas em uma operação verificável, diminuindo o custo operacional logo no primeiro comando.

Encerrar a aplicação não significa apenas parar o processo principal, porque agentes costumam deixar rastros como Playwright, Jest ou subprocessos órfãos. O down derruba o servidor; o down --force amplia a limpeza e mata processos derivados da inicialização; o down --clean vai além e remove artefatos de ambiente e build, como variáveis locais, node_modules e .next, para recolocar o projeto em estado zerado. Essa gradação é útil porque separa desligamento simples, recuperação agressiva e reset completo do ambiente.

Retomando a ideia de segunda fundação, a IA precisa assumir que o projeto pode ser reiniciado do zero a qualquer momento. Isso muda o critério de qualidade do setup: não basta funcionar uma vez na máquina do desenvolvedor, ele precisa ser reproduzível após limpeza total. Quando a inicialização é tranquila mesmo depois de um --clean, o projeto deixa de depender de estado acumulado e passa a oferecer previsibilidade real para agentes.

check.sh valida se o servidor está rodando e saudável, mas o ganho operacional aparece quando o script também sabe reagir a falhas. A opção --fix mata processos órfãos, tenta reiniciar o serviço e sobe novamente o servidor, convertendo diagnóstico em ação corretiva. Em vez de a IA improvisar comandos de recuperação a cada erro, ela recebe um procedimento padrão de reparo com comportamento conhecido.

Logs e processos precisam ser acessíveis por comandos simples, porque a IA depende de evidência de execução para depurar. O watch.sh acompanha a saída do servidor como um tail operacional, enquanto watch.sh --ps expõe quais processos estão ativos naquele contexto. Essa separação melhora observabilidade porque distingue sintomas da aplicação em execução do estado do ambiente que a sustenta.

Quando vários agentes ou processos sobem aplicações em paralelo, conflito de porta deixa de ser exceção e vira condição normal de operação. Definir no .env.local uma porta escolhida dentro de um range controlado permite verificar ocupação, selecionar uma porta livre e persistir essa decisão no arquivo de ambiente. O efeito prático é evitar que testes, navegação automatizada e servidores diferentes se misturem por apontarem para instâncias erradas.

Testes já tinham sido apresentados como parte da base operacional; o avanço aqui é torná-los explícitos no contrato do projeto desde o início. Regras de qualidade, comandos de execução, localização dos arquivos e padrões de teste orientam a IA sobre como validar mudanças sem precisar inferir convenções a cada tarefa. Isso reduz atrito porque o agente não apenas sabe que deve testar, mas também sabe onde, como e com quais critérios.

Um projeto pronto para uso da IA é aquele em que contrato, scripts, limpeza, recuperação, logs, portas e testes já estão organizados como componentes verificáveis. A diferença em relação a um scaffold comum não está só na existência dos arquivos, mas no fato de cada artefato responder a um problema operacional recorrente: iniciar, parar, reparar, observar, isolar e validar. Quando essas peças existem no dia zero, a IA deixa de gastar energia descobrindo o ambiente e passa a investir esforço em desenvolver o software.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]