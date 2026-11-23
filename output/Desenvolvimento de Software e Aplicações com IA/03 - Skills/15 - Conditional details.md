Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17543)

## Resumo da aula

Conditional Details é um pattern de organização em que a skill explicita condições para decidir qual arquivo ler, qual referência consultar ou qual caminho seguir. Diferente de uma skill puramente descritiva, aqui o conteúdo funciona como uma árvore de decisão embutida no próprio texto. Isso reduz ambiguidade porque o agente não precisa inferir sozinho qual documentação é relevante. A utilidade aparece quando uma mesma skill cobre cenários distintos e precisa direcionar a leitura conforme o estado real do projeto.

Retomando a organização progressiva já estabelecida, a novidade aqui é usar sinais da codebase para classificar o sistema em categorias como Greenfield, Emerging, Established e Mature. Essa classificação pode ser derivada de artefatos como um arquivo de CodeBase Exploration ou uma análise arquitetural, observando contagem de componentes, acoplamento médio e integração entre partes. A categoria resultante não serve apenas para rotular o projeto: ela define qual referência especializada deve ser carregada em seguida. Assim, a skill deixa de ser um texto linear e passa a operar como um mecanismo de seleção contextual.

A decisão precisa aparecer em regras claras, por exemplo: sem código ou com zero componentes, o projeto cai em Greenfield; em outros intervalos, passa para Emerging, Established ou Mature. O ponto central não é a nomenclatura das categorias, mas a explicitação do critério que leva a cada uma delas. Quando a condição está declarada, o agente consegue justificar a escolha e seguir um fluxo previsível. Isso melhora consistência entre execuções e reduz leituras irrelevantes.

Depois de produzir o output da classificação, a skill pode apontar diretamente para arquivos como greenfield.md, emerging.md, established.md e mature.md. Esse encadeamento transforma a decisão em navegação objetiva: primeiro identifica-se o contexto, depois abre-se apenas a documentação correspondente. Em relação ao uso de referências já visto anteriormente, a diferença aqui é que a leitura sob demanda passa a ser governada por condições explícitas. O ganho é economia de contexto com maior precisão operacional.

Uma skill pode ser altamente especializada em um único assunto, caso em que o skill.md atua como ponto de entrada para referências daquele domínio. Quando a skill cobre vários assuntos, o skill.md muda de papel e passa a funcionar como roteador, decidindo para onde o agente deve seguir. Conditional Details é especialmente útil nesse segundo caso, porque evita que um arquivo central grande vire um bloco indiferenciado de instruções. O design correto depende de quantos contextos distintos a skill precisa acomodar.

Quando uma skill cresce para centenas de linhas, uma Table of Contents deixa de ser apenas organização visual e passa a ser uma pista de navegação para o agente. Um índice com seções como Greenfield Projects e seus subtópicos oferece uma visão geral do conteúdo antes da leitura detalhada. Se o agente já sabe o que procura, ele pode saltar para a seção relevante em vez de percorrer o arquivo inteiro. Isso reduz consumo de tokens e diminui o risco de dispersão em partes não relacionadas ao problema atual.

Conteúdo grande deve ser particionado por domínio de decisão, como referência de API, autenticação e regras de negócio. Essa categorização não serve apenas para humanos encontrarem informação mais rápido; ela também melhora a capacidade da IA de mapear o espaço da skill e selecionar o trecho necessário. Quanto mais nítida for a estrutura global, menor a chance de o agente carregar contexto excessivo ou misturar instruções de áreas diferentes. A organização, nesse caso, é parte do comportamento da skill.

Mesmo que o custo de token tenda a cair, a limitação prática de janela de contexto continua relevante no desenho de skills. Começar uma sessão com uma fração significativa da janela já ocupada reduz espaço para raciocínio, código, logs e iterações posteriores. Além disso, uma skill excessivamente densa pode levar o agente a ignorar partes importantes, ler tudo sem necessidade ou se confundir com instruções concorrentes. Estruturar Conditional Details e índices bem definidos é uma forma de otimizar contexto antes mesmo da execução.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]