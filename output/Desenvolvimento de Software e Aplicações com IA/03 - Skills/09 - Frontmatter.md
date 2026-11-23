Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17528)

## Resumo da aula

Front matter é o cabeçalho da skill, do agente ou de comandos, escrito como metadata em YAML. Retomando o carregamento on-demand já discutido, ele não é apenas organização de arquivo: é a parte que permite ao agente identificar quando uma skill deve ser usada sem precisar ler seu conteúdo completo. Por isso, uma skill útil pode continuar invisível se o front matter não comunicar claramente sua finalidade. O valor prático do front matter está em transformar a intenção da skill em sinais legíveis para o mecanismo de seleção.

A descrição da skill funciona como a “venda” da skill para o agente. Como o agente decide o carregamento a partir do que lê no cabeçalho, a qualidade dessa descrição influencia diretamente se a skill será acionada ou ignorada. Isso muda a prioridade de implementação: não basta a skill funcionar internamente; ela precisa ser descrita com precisão suficiente para ser encontrada no momento certo. Investir tempo na descrição é parte do desenvolvimento, não um acabamento opcional.

Skill Trigger é a condição textual que faz o agente reconhecer que uma skill se aplica à tarefa atual. No front matter, isso aparece em padrões como use when e trigger when user..., que explicitam situações, intenções e termos associados ao uso da skill. O agente compara o pedido do usuário com esses sinais e decide se vale carregar aquela habilidade. Se a skill não dispara quando deveria, o problema muitas vezes não está na lógica da skill, mas na formulação do trigger.

Uma descrição eficaz costuma combinar três elementos: o que a skill faz, quando deve ser usada e como ela ajuda. No exemplo de documentação colaborativa, o cabeçalho não apenas informa que a skill apoia escrita de documentação, propostas e technical specs, mas também explicita ganhos como eficiência, transferência de contexto, refinamento e qualidade do conteúdo. Essa combinação reduz ambiguidade e aumenta a chance de correspondência com pedidos reais. Descrições genéricas demais enfraquecem o trigger porque não oferecem pistas suficientes ao agente.

Uma forma prática de escrever bons front matters é partir de referências de skills conhecidas e adaptar sua estrutura ao novo caso. Isso não significa copiar conteúdo, mas reaproveitar padrões de formulação que já funcionam para descoberta e acionamento. O objetivo é treinar a descrição para conter palavras-chave, intenções e contextos de uso compatíveis com a tarefa da skill. Esse processo é especialmente útil quando a skill está correta tecnicamente, mas continua sem ser carregada.

A qualidade do front matter é validada em uso real: o agente carrega ou não carrega a skill quando a tarefa aparece. Se a skill falha justamente nos cenários em que deveria entrar, isso indica que a descrição não está alinhada com a linguagem usada nas solicitações. O ajuste, então, deve ocorrer no cabeçalho, refinando termos, exemplos de uso e gatilhos textuais. Esse teste empírico é mais confiável do que assumir que a descrição está boa apenas porque parece bem escrita.

Quando o agente não carrega a skill automaticamente, há duas saídas: pedir explicitamente que ele carregue a skill ou escrever a solicitação usando as palavras-chave previstas no front matter. A segunda abordagem tende a ser mais fluida, porque integra o trigger ao próprio fluxo de trabalho. Em vez de dar um comando artificial, o pedido já nasce com termos como “criar uma proposta”, “escrever documentação” ou “draft de spec”, que funcionam como sinais de ativação. Isso aproxima a linguagem do usuário da linguagem de descoberta da skill.

O mesmo princípio vale para agentes personalizados. Se o prompt ou a configuração do agente não usa termos compatíveis com o front matter das skills disponíveis, o agente pode deixar de acioná-las mesmo quando elas seriam adequadas. Em outras palavras, o front matter não conversa apenas com o usuário final; ele também precisa conversar com a forma como o agente foi instruído a operar. Criar agentes e escrever front matters de forma isolada reduz a taxa de ativação correta das skills.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]