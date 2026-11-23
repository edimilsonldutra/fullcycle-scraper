Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17531)

## Resumo da aula

Uma skill personalizada de design system encapsula as regras visuais de um produto para que a IA consiga gerar interfaces consistentes com a identidade da empresa. Retomando a separação entre skill.md e referências, o valor aqui não está em repetir instruções genéricas de front-end, mas em concentrar o conhecimento específico da plataforma: branding, tokens, componentes, layouts e variações reais de tela. Isso reduz ambiguidade na geração de UI e evita que a IA produza soluções visualmente corretas apenas em termos técnicos, mas desalinhadas com o produto.

O front matter continua sendo a camada que “vende” a skill para a IA, mas aqui ele é aplicado a um caso interno de design system. A descrição informa que a skill cobre tokens, cores, tipografia, espaçamento, bordas, componentes, padrões e layouts, além de deixar explícito quando ela deve ser usada: criação de interfaces, revisão visual e implementação de páginas da área do aluno. As keywords ampliam a chance de ativação em pedidos relacionados a layout, componentes, tema escuro e student area, o que torna a skill mais fácil de ser acionada no momento certo.

O arquivo principal funciona como um mapa de navegação da identidade visual da plataforma. Em vez de carregar todos os detalhes de uma vez, ele resume os elementos centrais: tema dark-first, posicionamento da marca, tom visual e acesso a ativos como o logo em SVG. Esse resumo dá contexto suficiente para a IA começar a trabalhar e, quando necessário, aprofundar a consulta nas referências especializadas.

Os design tokens registram decisões reutilizáveis de interface, como cores, fundos, tipografia, espaçamento, bordas e estados visuais. Aqui eles aparecem acompanhados de tabelas e anotações de uso, o que é crucial porque um valor isolado de cor ou fonte não explica onde aquele token deve ser aplicado. Quando a IA recebe não só o token, mas também a intenção de uso — por exemplo, inputs, cards ou áreas específicas da interface — ela consegue produzir telas mais consistentes e com menos retrabalho.

As 16 regras gerais cumprem o papel de checklist resumido para decisões frequentes de implementação. Isso é útil porque nem toda tarefa exige abrir documentação extensa; muitas vezes a IA só precisa de um conjunto curto de critérios para escolher corretamente um padrão visual. Quando o problema exige mais precisão, essas regras apontam para as referências detalhadas, preservando a estratégia de carregamento sob demanda já estabelecida anteriormente.

As referências visuais complementam o texto com screenshots, SVGs e outros artefatos que representam a interface real. Em design system aplicado a IA, isso importa porque muitos padrões visuais são mais fáceis de reconhecer por comparação do que por descrição textual. O uso de imagens como referência transforma a skill em um pacote multimodal de orientação, especialmente útil para páginas com forte dependência de composição visual.

Os IDs e nodes do Figma conectam a skill a uma fonte viva de verdade visual. Quando existe um servidor MCP do Figma, a IA pode consultar diretamente os elementos do design, recuperar detalhes e alinhar a implementação ao arquivo original, aproximando o resultado de um front-end pixel perfect. A skill, nesse caso, não substitui o Figma; ela organiza quando e como esse acesso deve ser usado dentro do fluxo de geração.

A estrutura de referências separa o conhecimento em duas dimensões: páginas e componentes. Nas páginas, entram base layout, login, cursos, módulos, trilhas, lições, home e progresso, cada uma com sua origem no Figma e uma visão próxima de mockup; nos componentes, entram botões, bordas, cards e suas variações. Essa divisão ajuda a IA a decidir se o problema atual é de composição de tela inteira ou de implementação detalhada de um elemento isolado.

Nem toda interface segue o layout base, e a skill precisa capturar essas exceções explicitamente. Páginas de documento, modals, login e visualização de vídeo em tela cheia exigem regras próprias, porque reutilizar cegamente o padrão dominante gera interfaces incorretas. Registrar variações evita que a IA trate exceções como inconsistências e melhora a aderência em cenários reais de produto.

A organização final combina um núcleo curto no skill.md com documentação aprofundada em arquivos de referência, imagens e ponteiros para o Figma. Essa estrutura mantém a skill acionável sem inflar contexto desnecessariamente, ao mesmo tempo em que preserva acesso a detalhes quando a tarefa exige precisão maior. Em um ambiente corporativo, isso transforma o design system em uma skill reutilizável para criação, revisão e evolução de interfaces da plataforma.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]