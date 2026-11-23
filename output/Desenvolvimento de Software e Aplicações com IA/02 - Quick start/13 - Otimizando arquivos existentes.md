Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17403)

## Resumo da aula

Um arquivo legado de inicialização não deve ser podado diretamente; primeiro ele precisa ser validado contra si mesmo. Contradições, regras duplicadas e instruções incompatíveis distorcem o comportamento do agente com mais força do que a ausência de contexto. Por isso, o primeiro uso do prompt é pedir que a IA localize conflitos explícitos e implícitos, apontando onde uma orientação invalida outra. Essa etapa transforma a refatoração em diagnóstico, não em simples redução de texto.

Depois da limpeza inicial, o arquivo principal deve reter somente fatos e aspectos que participam do core das decisões da aplicação. O critério prático é manter o que altera comportamento recorrente do agente e mover o que é complementar, especializado ou situacional. Retomando a distinção já estabelecida entre contexto sempre carregado e conhecimento sob demanda, o arquivo principal fica com o que precisa influenciar quase toda interação. O ganho não é apenas concisão: é foco operacional.

Quando um bloco continua útil, mas não precisa permanecer no carregamento permanente, ele deve ser movido para arquivos auxiliares ou para Skills. Essa externalização preserva o conhecimento sem transformar o arquivo principal em inventário inchado. A ligação entre os artefatos precisa ser explícita, para que o agente saiba onde buscar o detalhe quando a tarefa exigir. Separar não significa esconder; significa reposicionar o conteúdo no nível correto de carregamento.

Gatilhos são condições que indicam quando um arquivo auxiliar ou Skill deve ser consultado. Eles existem para evitar tanto o excesso de contexto inicial quanto a dependência de descoberta aleatória pelo agente. Um gatilho útil descreve a situação de uso, como um tipo de tarefa, erro recorrente ou decisão específica que exige aquele conhecimento. Sem esse mecanismo, a externalização pode reduzir o tamanho do arquivo principal, mas também reduzir a chance de o conteúdo certo ser carregado na hora certa.

Frases genéricas como “use boas práticas” não orientam ação verificável e, por isso, não ajudam na execução. O trabalho de refatoração consiste em converter abstrações vagas em regras observáveis, com condição de uso e efeito esperado. Uma forma eficaz de fazer isso é pedir que o próprio agente explicite quando a orientação se aplica, por que ela importa e que decisão concreta ela altera. Quando a instrução responde a essas perguntas, ela deixa de ser slogan e vira política operacional.

O prompt não serve apenas para reescrever texto; ele organiza o processo de análise do arquivo legado. A sequência útil é: detectar conflitos, separar fatos centrais, identificar o que deve ser externalizado, propor gatilhos de carregamento e reescrever regras vagas em termos concretos. Esse fluxo produz um arquivo mais curto sem perder informação decisiva. Como o prompt é instrumento de trabalho, ele pode e deve ser ajustado até gerar um resultado compatível com o projeto.

Depois que a IA atualiza o .md principal e cria os novos arquivos, a refatoração ainda não terminou. Esses artefatos passam a influenciar diretamente o comportamento futuro do agente, então precisam de revisão crítica, como já ocorre no code review desse tipo de arquivo. O ponto de verificação aqui não é só qualidade textual, mas também coerência entre arquivo principal, links e conteúdo externalizado. Um conjunto bem escrito, porém mal distribuído, continua produzindo ambiguidade.

Concisão não é sinônimo de esvaziamento. Um arquivo principal pequeno demais pode perder informações que ajudam o agente o tempo todo, o que força inferência desnecessária e reabre erros já conhecidos. O equilíbrio correto mantém o núcleo operacional sempre carregado e desloca apenas o que realmente pode ser consultado sob demanda. A meta é sustentabilidade do arquivo, não austeridade textual.

A mesma informação pode mudar de lugar ao longo do tempo. Retomando o exemplo em que certos trechos de código ainda permanecem no arquivo principal, isso faz sentido quando não existe Skill correspondente e aquele detalhe continua decisivo no estágio atual do projeto. Conforme o conhecimento é estabilizado e externalizado, essas responsabilidades podem migrar para outros arquivos ou Skills. A organização ideal, portanto, depende do momento do projeto e dos erros reais que o agente ainda comete.

Se uma informação gera erro recorrente e o agente ainda não consegue captá-la sozinho, mantê-la temporariamente no arquivo principal é uma decisão válida. Esse critério vale especialmente enquanto o modelo, as Skills ou os artefatos auxiliares ainda não cobrem bem aquele ponto. A refatoração de um arquivo legado não busca pureza estrutural; busca reduzir erro operacional sem perder previsibilidade. O arquivo continua vivo e deve ser redistribuído conforme o sistema amadurece.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]