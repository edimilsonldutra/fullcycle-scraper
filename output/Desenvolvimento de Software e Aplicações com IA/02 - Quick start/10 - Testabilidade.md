Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17398)

## Resumo da aula

Marcadores de teste são rótulos explícitos que classificam subconjuntos da suíte, como unit, integration ou slow. Eles existem para transformar pedidos vagos como “rode os testes de unidade” em comandos determinísticos, sem exigir exploração do repositório. Quando o projeto também registra dependências operacionais desses marcadores, como “integração precisa de banco”, o agente deixa de inferir contexto e passa a executar o fluxo correto na primeira tentativa.

Fixtures, usuários de teste, estados de autenticação e helpers do conftest formam o inventário operacional que o agente pode reutilizar ao escrever ou ajustar testes. Isso reduz duplicação, evita criação de dados inconsistentes e acelera a produção de casos úteis, porque o agente sabe de antemão quais blocos de apoio já existem. Em vez de improvisar factories ou payloads, ele parte de recursos reais como createTestUserData e createLoginData.

Retomando a regra operacional já definida para o projeto, os testes devem rodar dentro do container quando essa for a forma oficial de execução. Mesmo que a stack seja facilmente inferível por pytest ou jest, o comando exato ainda precisa estar explícito para impedir desvios para a máquina hospedeira. A forma mais robusta é listar comandos diretos para cenários frequentes: suíte completa, teste por nome, apenas unitários e apenas integração.

Testes acionados por IA não devem entrar em modo interativo, porque isso bloqueia automação e interrompe o fluxo de execução. Em front-end com Jest, a flag --watchAll=false elimina esse comportamento e torna a execução compatível com um agente não interativo. O mesmo princípio vale para qualquer ferramenta que abra prompts, watchers ou sessões persistentes sem necessidade.

Ferramentas de teste podem gerar diretórios e relatórios que são úteis para humanos em depuração manual, mas atrapalham o fluxo automatizado quando aparecem por padrão. No caso de Playwright, definir o comando com --reporter=list evita a criação de reports desnecessários e mantém a execução mais limpa. Esse tipo de detalhe merece entrar no arquivo de inicialização porque altera diretamente o comportamento operacional do agente.

A regra de escopo da execução precisa separar mudanças locais de validações amplas. Durante a interação, o padrão eficiente é rodar apenas os testes relacionados aos arquivos modificados; antes de PR ou após mudanças maiores, a suíte completa passa a ser obrigatória. Como a noção de “mudança grande” ainda depende de inferência, o comportamento deve ser observado e refinado com exemplos se o agente exagerar ou validar de menos.

Nem todo código merece teste dedicado, especialmente quando a cobertura já virá de integração ou quando o comportamento pertence à biblioteca ou ao framework. Entram nessa zona de exclusão validação de schema feita por biblioteca consolidada, CRUD simples já coberto em outro nível, renderização trivial de componentes e utilidades muito básicas como formatação. Essa restrição existe para evitar microtestes caros, redundantes e pouco informativos.

Os testes mais valiosos cobrem fluxos críticos do usuário e regras de negócio com risco real de regressão. Autenticação, upload, core CRUD, permissões, quotas, tratamento de erro, gerenciamento de estado e edge cases produzem mais segurança do que dezenas de testes triviais. A prioridade correta desloca o esforço do agente para comportamentos que realmente quebram o sistema quando falham.

Quando o agente começa a produzir testes demais, a resposta não é pedir “mais bom senso”, e sim registrar limites operacionais verificáveis. Regras como máximo de testes por arquivo, máximo de mocks por teste e comparação entre tamanho do teste e tamanho da implementação ajudam a detectar excesso estrutural. Essas guidelines não são universais; elas surgem do comportamento observado no projeto e devem ser ajustadas por feedback contínuo.

A camada de testabilidade do arquivo de inicialização evolui por observação de falhas reais. Se o agente hesita para rodar um comando, usa a flag errada, testa biblioteca externa ou cria artefatos inúteis, a correção deve virar instrução explícita. O objetivo não é documentar tudo, mas capturar os pontos que eliminam repetição de erro e tornam a validação rápida e previsível.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]