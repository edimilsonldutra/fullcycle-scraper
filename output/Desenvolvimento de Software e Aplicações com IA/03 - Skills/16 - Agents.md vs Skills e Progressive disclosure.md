Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17544)

## Resumo da aula

Retomando Progressive Disclosure, a diferença central está no grau de controle e observabilidade do carregamento de contexto. Arquivos como agents.md, cloud.md e gemini.md entram no contexto logo no início da sessão e, por isso, já consomem tokens no momento zero. Eles podem apontar para documentação complementar, mas essa leitura adicional depende da decisão do agente quando a referência não é importada diretamente. Isso torna o mecanismo útil, porém sem garantia de execução.

Em arquivos de inicialização, uma referência com @caminho/do/arquivo funciona como um import imediato. Na prática, o conteúdo referenciado é anexado ao contexto já no carregamento inicial, como se o arquivo principal incorporasse aquele texto. Isso melhora a organização física dos arquivos, mas não reduz custo de contexto: se os arquivos referenciados forem grandes, todos os tokens entram de uma vez. Por isso, usar @ exige intenção explícita de carregar tudo desde o começo.

Quando a referência é feita sem @, o comportamento volta para a lógica de leitura sob demanda já discutida anteriormente. O agente pode ler o arquivo se entender que ele é relevante para a tarefa, mas essa decisão não é garantida mesmo quando o texto tenta induzir a leitura com instruções como “read them first”. Esse padrão serve para manter o arquivo inicial curto e sugerir documentação complementar, especialmente para detalhes muito específicos do projeto. Ainda assim, ele continua sendo apenas uma sugestão operacional, não um mecanismo confiável de carregamento.

Arquivos de inicialização funcionam bem para contexto-base e para referências internas muito ligadas ao projeto. Eles são adequados para registrar gotchas locais, convenções específicas e pontos em que a IA costuma falhar naquele repositório, mesmo que isso não justifique empacotar uma skill. O ponto crítico é não assumir que toda referência será lida nem que toda instrução referenciada será seguida. Em outras palavras, referência em arquivo de memória não equivale a execução previsível.

Lembra da leitura em camadas já vista antes: nas skills, esse comportamento deixa de ser apenas uma possibilidade e passa a fazer parte do desenho da solução. Uma skill acionada começa com pouco contexto, decide o que precisa consultar, lê apenas os arquivos relevantes e interrompe a leitura quando já tem informação suficiente. Esse fluxo torna o uso de contexto mais disciplinado e mais transparente, porque o carregamento acontece dentro de um processo reconhecível. A principal diferença não é só ler sob demanda, mas fazer isso dentro de uma unidade operacional explícita.

Tanto referências em arquivos de inicialização quanto skills dependem de ativação em algum nível: o agente pode não ler uma referência e também pode não acionar uma skill. A diferença aparece depois do trigger. Quando a skill é acionada, o carregamento e o fluxo ficam mais claros, o que dá mais previsibilidade sobre o que está sendo usado. Em cloud.md ou agents.md, essa clareza é menor, porque a leitura complementar pode ou não acontecer sem um sinal tão evidente.

Skills não servem apenas para documentar contexto; elas também podem executar ações como comandos em ferramentas compatíveis. Isso amplia o papel da skill de “guia de leitura” para “pacote operacional” com fluxo consistente e acionável. Como já foi mostrado em exemplos anteriores, esse formato favorece distribuição, compartilhamento e reaproveitamento entre projetos. Já os arquivos de inicialização tendem a permanecer presos ao contexto interno de um único repositório.

A escolha depende da natureza do conhecimento. Se a informação é local, altamente específica do projeto e pouco reutilizável, uma referência no cloud.md pode ser suficiente, desde que você aceite a falta de garantia de leitura. Se o conteúdo precisa ser compartilhável, reutilizável, acionável e organizado como fluxo de execução, a skill é a estrutura mais adequada. A dúvida “por que criar uma skill se posso referenciar arquivos no inicializador?” se resolve justamente nessa diferença entre sugestão contextual e mecanismo operacional reutilizável.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]