Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17542)

## Resumo da aula

Progressive Disclosure é a estratégia de fazer o agente ler apenas o que precisa no momento em vez de carregar toda a documentação de uma vez. Em Skills, isso reduz consumo de tokens, evita ruído de contexto e melhora a precisão da leitura. A ideia central já aparecia no uso de skill.md com referências sob demanda; aqui o foco está em como estruturar esse comportamento como padrão explícito de organização.

Um High-Level Guide concentra no skill.md uma visão geral curta e aponta para arquivos especializados quando o agente precisa se aprofundar. Retomando o cenário do design system já usado antes, o arquivo principal não tenta conter toda a especificação de layout, states ou models; ele funciona como índice operacional. Essa divisão preserva o contexto principal enxuto e transfere detalhes para referências carregadas apenas quando a tarefa exige.

A Skill opera em camadas: primeiro entra o front matter com descrição resumida, depois o conteúdo principal, e só então os arquivos complementares relevantes. Esse fluxo é importante porque transforma a documentação em uma estrutura navegável, não em um bloco monolítico de texto. O agente começa com sinais suficientes para decidir se a Skill se aplica e aprofunda a leitura apenas após a ativação.

Nem toda Skill representa apenas uma área técnica específica, como um design system. Em contextos corporativos, uma única Skill pode servir como ponto de entrada para vários domínios, como billing, CRM, certificados e vendas. Nesse formato, o arquivo principal funciona quase como um catálogo de regras de negócio e regras técnicas, encaminhando o agente para o documento correto conforme o domínio envolvido na solicitação.

Quando a Skill lista seções como billing, CRM, Student Certificates e Sales, ela está implementando roteamento de contexto. O agente não precisa inspecionar toda a base documental para descobrir onde estão as regras aplicáveis; a própria Skill informa onde procurar. Isso torna a navegação mais determinística e reduz chamadas exploratórias desnecessárias a arquivos e ferramentas.

Além de linguagem natural, a Skill pode incluir pseudocódigo ou comandos concretos para acelerar a busca por arquivos relevantes. Um exemplo é instruir o agente a executar grep -i billing para localizar rapidamente documentos relacionados a billing dentro da plataforma. Esse recurso é útil quando a estrutura do repositório é grande ou quando a descoberta por tentativa e erro geraria muitas operações intermediárias.

Comandos e pseudocódigo ajudam, mas não devem transformar a Skill em um fluxo rígido de if-else escrito em texto. A Skill continua sendo um artefato de orientação para modelos, então precisa equilibrar clareza semântica com instruções acionáveis. O ponto de equilíbrio é usar comandos onde eles reduzem ambiguidade ou custo operacional, mantendo a maior parte da intenção descrita em linguagem natural.

Domínio, nesse contexto, não significa apenas domínio de negócio. Também pode representar áreas distintas de um sistema, módulos independentes ou partes de um monorepo com pouca sobreposição entre si. Nesses casos, Progressive Disclosure permite que a Skill carregue contexto apenas da fatia arquitetural relevante para a tarefa atual, em vez de contaminar a janela de contexto com documentação de áreas não relacionadas.

Uma Skill bem estruturada pode orientar o agente a gerar filtros antes de começar a ler arquivos individualmente. Em vez de encadear ls, cat, grep e read de forma exploratória, o agente executa um comando mais direcionado e já obtém a lista de documentos relevantes. Isso reduz tool calls, economiza tokens e encurta o caminho entre a intenção da tarefa e o contexto realmente necessário.

Criar uma Skill não é apenas escrever um skill.md; é decidir como o conhecimento será particionado, descoberto e carregado. A qualidade dessa estrutura afeta diretamente custo, reutilização e assertividade do agente. Quando a Skill separa visão geral, referências especializadas e mecanismos de busca contextual, ela deixa de ser documentação passiva e passa a funcionar como interface de navegação para o conhecimento do projeto.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]