Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17546)

## Resumo da aula

Uma skill empacotada pode ser distribuída como arquivo .skill e depois extraída para a pasta .cloud/skills do projeto onde será usada. Retomando a estrutura já vista para skills, o arquivo central continua sendo o skill.md, que concentra descrição, gatilhos e workflow. Isso permite criar uma skill uma vez e reaproveitá-la em outros repositórios apenas copiando a pasta correspondente. O empacotamento existe para facilitar transporte e compartilhamento, não para alterar o funcionamento da skill.

A skill Critical Review foi configurada para revisar documentos, código e especificações em busca de contradições, ambiguidades, inconsistências e lacunas lógicas. O front matter define quando ela deve ser usada, inclusive em cenários como revisão de PRDs, RFCs, documentação técnica e mudanças não commitadas. O workflow orienta a coleta do material primeiro e a análise depois, o que evita conclusões sem base documental suficiente. As keywords e a descrição ajudam o ambiente a acionar a skill quando o pedido do usuário se aproxima desse tipo de revisão.

A revisão começa pela leitura do escopo correto: arquivos explicitamente citados pelo usuário, diferenças locais com git diff ou conjuntos de código e documentação que precisam ser cruzados. Esse passo é decisivo porque a qualidade da análise depende de comparar fontes reais, não de inferir intenções. Quando há código e especificação ao mesmo tempo, a skill deve ler ambos para verificar alinhamento entre implementação e documento. Em mudanças ainda não commitadas, usar staged, unstaged ou git diff HEAD expande a revisão para o estado atual do trabalho, não apenas para o repositório versionado.

A análise é organizada em quatro dimensões complementares. Contradições aparecem quando duas fontes afirmam coisas incompatíveis; ambiguidades surgem quando termos, critérios ou comportamentos ficam vagos; inconsistências revelam nomes, convenções ou definições divergentes para o mesmo conceito; lacunas lógicas indicam saltos no raciocínio, quando um passo depende de outro que nunca foi especificado. Separar os achados dessa forma melhora a triagem, porque cada tipo de problema exige uma correção diferente.

Classificar achados em severidade alta, média e baixa ajuda a priorizar correções antes que inconsistências menores consumam atenção indevida. A saída útil combina um resumo consolidado com a lista detalhada dos achados, agrupados por tipo e acompanhados de recomendações. A diretriz central é reportar apenas o que pode ser sustentado por evidência, marcando como “possível” aquilo que ainda depende de confirmação. Referenciar arquivo e linha aumenta a auditabilidade do relatório, embora esse nível de detalhe possa ser ajustado conforme a preferência de quem usa a skill.

Retomando os gatilhos já discutidos, a skill pode ser acionada por um pedido em linguagem natural que contenha a intenção de revisão crítica. Um comando como buscar contradições e ambiguidades em documentos dentro de uma pasta específica já foi suficiente para disparar a Critical Review, mesmo com o pedido escrito em português. Isso mostra que o trigger não depende apenas de uma frase exata, mas da proximidade semântica entre o pedido e a descrição da skill. Na prática, vale testar variações do prompt para validar se o front matter está bem calibrado.

Uma skill não precisa se limitar a uma sequência linear de leitura e resposta. Nesse caso, o ambiente disparou múltiplos agentes em paralelo para inspecionar o conjunto documental, acelerando a revisão de um volume grande de arquivos. Esse comportamento também pode ser incorporado intencionalmente à skill, definindo agentes especializados para tarefas distintas, como leitura rápida do codebase, cruzamento documental ou validação adicional. Paralelismo é especialmente útil quando o custo principal está na exploração de muitos artefatos independentes.

O valor da skill aparece no relatório consolidado, que transforma um conjunto grande de documentos em uma lista priorizada de conflitos reais. Entre os achados, surgiram incompatibilidades arquiteturais como JWT versus sessão em banco, divergências de tokens de design, conflitos de prazo de sessão, limites de caracteres contraditórios e dependências entre issues não documentadas. Cada exemplo representa um tipo diferente de desalinhamento entre PRD, spec, plano e organização das features. A skill não substitui decisão técnica, mas reduz drasticamente o trabalho manual de encontrar esses pontos de atrito.

Uma skill gerada automaticamente é ponto de partida, não versão final. Depois do primeiro uso, faz sentido ajustar idioma, formato do relatório, nível de detalhamento e até a estratégia de execução com agentes especializados. O refinamento pode incluir cruzamentos mais profundos, validação adicional dos achados e geração de plano de correção. O ganho prático está em transformar uma necessidade recorrente — validar consistência entre documentos e implementação — em um procedimento reutilizável e cada vez mais preciso.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]