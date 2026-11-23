Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16569)

## Resumo da aula

Prompt Engineering aparece em dois contextos técnicos diferentes. O primeiro é usar IA para ajudar no desenvolvimento de software, onde prompts longos e muito contexto podem ser aceitáveis para melhorar produtividade. O segundo é desenvolver software cujo comportamento depende diretamente de prompts, como agentes, assistentes e aplicações multiagente. Nesse segundo caso, o prompt deixa de ser apenas apoio ao desenvolvedor e passa a governar parte do comportamento do produto.

Quando o prompt está dentro da aplicação, tamanho e complexidade passam a ter impacto operacional direto. Prompts maiores tendem a aumentar consumo de tokens, custo por requisição e latência percebida pelo usuário. Por isso, a estratégia que funciona para apoiar programação nem sempre funciona para um sistema em produção. O projeto do prompt precisa equilibrar qualidade da resposta com eficiência de execução.

O prompt delimita até onde o sistema pode ir e que tipo de ação ele está autorizado a tomar. Isso importa especialmente em fluxos críticos, como decisões que afetam cálculo, recomendação ou execução de transações sensíveis. Em vez de apenas pedir “resolva o problema”, o sistema precisa explicitar limites, critérios e contexto de atuação. Sem esse contorno, o modelo pode extrapolar comportamento de forma inadequada ao domínio.

Proatividade é o grau de iniciativa que o agente recebe para agir além da solicitação literal do usuário. Um agente pouco proativo responde apenas ao que foi pedido; um agente mais proativo infere intenção, toma próximos passos e pode até executar ações adicionais. Esse ajuste é feito no prompt, que define se a IA deve só esclarecer, sugerir, planejar ou agir. Controlar proatividade evita tanto respostas passivas demais quanto comportamento excessivo, como sair implementando quando o usuário só queria uma explicação.

O prompt também orienta o nível de especialização da resposta e como dados externos entram no raciocínio do sistema. Quando a aplicação consulta bancos, documentos ou serviços externos, o prompt precisa deixar claro o que pode ser usado, com que finalidade e sob quais restrições. Isso vale tanto para agentes internos quanto para experiências de usuário final com conectores. O resultado depende menos de “ter acesso aos dados” e mais de como esse acesso é enquadrado pela instrução.

Em aplicações com IA, o prompt pode se tornar superfície de ataque. Instruções mal desenhadas ou permissivas demais podem induzir vazamento de dados privados, acesso indevido a informações sensíveis ou execução de ações fora do escopo esperado. Segurança aqui não é só filtrar entrada; é projetar prompts com limites explícitos, contexto mínimo necessário e restrições compatíveis com o risco do domínio. Privacidade e controle de acesso passam a depender também da engenharia da instrução.

Modelos menores ou agentes altamente especializados costumam ser mais sensíveis a pequenas mudanças no prompt. Uma palavra alterada pode degradar a execução, mudar interpretação da tarefa ou até quebrar o comportamento esperado. Isso acontece porque há menos margem para compensar ambiguidades da instrução. Nesses cenários, prompt precisa ser tratado com o mesmo rigor de uma interface crítica: claro, estável e testável.

Retomando a ideia de prompt como artefato de engenharia, aqui ele assume papel ainda mais forte: passa a definir comportamento operacional do sistema. Em vez de codificar toda decisão com fluxos determinísticos de if e else, parte da lógica é delegada a um modelo probabilístico que interpreta instruções e contexto. Chamar prompt de “nova linguagem de programação” significa reconhecer que ele expressa regras, limites e intenções que afetam execução real. O código continua essencial, mas o comportamento final emerge da combinação entre software tradicional e instrução probabilística.

O domínio de prompt também muda radicalmente o uso de plataformas como ChatGPT, Gemini e Claude. Quando o usuário final aciona modo agente, deep research, conectores ou tools, a qualidade da instrução passa a influenciar consultas em CRM, agenda, busca web, documentos, planilhas e apresentações. Um conector do HubSpot, por exemplo, não gera valor sozinho; ele precisa de um pedido bem formulado para consultar vendas, resumir resultados ou produzir análise útil. A mesma infraestrutura pode entregar respostas superficiais ou operações complexas, dependendo da estrutura do prompt.

Não existe um único prompt ideal para toda situação. O formato da instrução deve variar conforme o objetivo: tirar dúvida, gerar documento, analisar codebase, consultar dados externos ou operar um agente com autonomia controlada. Escolher o tipo de prompt adequado melhora previsibilidade, reduz desperdício e aumenta a utilidade da resposta. Essa escolha criteriosa é o que separa uso casual de uso intencional em cenários reais.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior eu estava falando aqui para vocês em relação ao processo de desenvolvimento de software que está totalmente atrelado à parte de Prompt Engineer. Por outro lado, o que acontece?

00:16

você vai perceber que quando você também fala de Prompt Engineering, a gente tem a aplicabilidade do Prompt Engineering, da parte de Prompts, nos softwares que utilizam inteligência artificial. Porque uma coisa é a gente programar, e a gente ter produtividade, e a gente trabalhar com desenvolvimento, e a gente vai precisar de Prompts, no final das contas. Mas, quando você for desenvolver

00:42

suas aplicações de inteligência artificial, ou seja, você pegar a aplicação que tem na sua empresa e você vai integrar com inteligência artificial, você vai desenvolver um agente de inteligência artificial, você vai criar uma aplicação multiagêntica, tá?

00:58

Isso aí vai ser extremamente importante, porque o jogo muda muito quando a gente está falando em processo de desenvolvimento de software, onde a gente pode ter prompts gigantes para a gente conseguir instruir a IA, ou uma gama de documentos gigantes para colocar num contexto para a IA nos ajudar a programar.

01:16

Por outro lado, quando a gente vai desenvolver software que usa prompt, que a gente vai precisar dos prompts, no final das contas, a gente pode ir para o lado oposto, porque quanto menor o prompt, melhor, entre aspas, em relação a custos da empresa, latência... Então, a gente tem todo um peso diferente, por isso que a gente sai meio que do 8 a 80 na hora que a gente está falando em prompt engineering, tá? A gente não pode...

01:40

simplesmente generalizar. Mas nesse caso, a gente tem diversas aplicabilidades. Por exemplo, como que eu vou definir o comportamento e o escopo de um agente? Ou um escopo do meu sistema na hora que eu vou pedir pra ele desenvolver ou fazer alguma transação que seja...

01:59

realmente crítica, por exemplo, fazer o cálculo de uma taxa de juros de um empréstimo que um cliente está pedindo baseado nas compras anteriores que ele fez antes e o quão bom pagador ele é, entende? Então, esses tipos de coisa afetam diretamente o sistema. Então, ele define como que o comportamento do sistema vai ser, qual que é o escopo, ou seja, até onde o sistema pode ir, né?

02:22

Qual o nível de proatividade que você pode dar? Ou seja, eu peço pra ele entender a necessidade de um cliente. Pronto. O quanto que ele vai entender essa necessidade, né? O quão proativo ele vai ser? Eu não sei se você já passou por situações até em desenvolvimento que, às vezes, você fazia uma pergunta e a IA já saía programando.

02:42

E você só queria tirar dúvida. Então, isso é nível de proatividade que, com o Prompt, você consegue reduzir ou aumentar. Ou trazer respostas extremamente especializadas. Muitas vezes você consegue acessar dados externos.

02:57

bancos de dados externos, mas tudo isso vai ter que compor o Prompt no final do dia, né? A gente também tem que pensar em como a parte de Prompt Engineer nos ajuda em relação à parte de segurança, privacidade de dados e tudo mais, né? Porque o Prompt pode ser a nova forma de você fazer um exploit dentro de uma aplicação em relação à parte de segurança, né? Ou vazar dados privados, né?

03:23

Imagina a gente pegar uma comissão de tabelas, faturamentos de empresas, através de prompt de engenheiro de dados que você não poderia ter acesso, né? Ou também a execução de tarefas extremamente específicas. Às vezes a gente quer trabalhar com um modelo pequeno, que ele faça exatamente uma tarefa, mas ele tem tão poucos parâmetros que, às vezes, uma palavra ou alguma coisa que você muda no prompt

03:48

simplesmente pode quebrar aquele agente que você está fazendo, tá? Então, o que eu normalmente gosto de dizer é que o Prompt Engineer é a nova linguagem de programação. O código, os softwares, eles com certeza são importantes, mas a gente tem que entender que quando a gente está falando de IA,

04:06

eu diria que o novo código também, que vai definir o comportamento, os nossos ifs e elses, que nós estamos tão acostumados, eles vão ser feitos e tendo decisões através da IA, e que muitas vezes funciona somente de forma probabilística, ou seja, por probabilidade e não de forma determinística com onde você tem. Se isso acontece, faz isso. Se isso acontece, faz isso. Então, quando...

04:32

você precisa domar, vamos dizer, o seu agente, a IA, o que vai fazer isso, o que vai colar, botar coleira ali no seu agente, no final das contas, é trabalhar com o Prompt. Então, a gente pode dizer que, de forma geral, Prompt Engineer é a nossa

04:50

a nossa nova linguagem de programação. Então, antigamente eu programava em Go, agora eu programo em português, que vai gerar código em Go, provavelmente. Então, é mais ou menos assim. Eu acredito que você já deva estar sentindo ou até cansado de...

05:07

Vê isso no dia a dia se você já está trabalhando com IA e acredito que sim, tá? Agora, existem outros pontos de aplicabilidade em relação à parte de Prompt Engineering que ele não tem necessariamente tanto a ver com como a gente vai desenvolver ou como a gente vai integrar sistemas, mas ele muda completamente a nossa...

05:29

utilidade e utilização de IA no nosso dia a dia, né? Por quê? Porque nós somos usuários finais também de plataformas de inteligência artificial. Por exemplo, a gente tem o ChatGPT, que a gente entra na plataforma do ChatGPT. A gente tem o Gemini, a gente tem o Claude, a gente tem diversas empresas que

05:50

usam a inteligência artificial para o usuário final, eu entrando no GPT e tirando uma dúvida. E a forma de como eu interajo com a inteligência artificial muda completamente eu sabendo trabalhar com prompt ou não. Então, eu tenho...

06:07

como que eu interajo com a IA, o tipo e a qualidade do resultado nas perguntas muda completamente, como que ela pode executar uma tarefa, trabalhar com análise de dados, fazer geração de documentos. Hoje em dia, a gente já tem recursos extremamente avançados de modo agente, a gente tem recursos de deep research, a gente tem conectores, ou seja, eu consigo perguntar qual é o faturamento da minha empresa e deixo o conector do HubSpot, por exemplo,

06:35

ligado no chatGPT e ele consegue entrar no meu CRM, ver a minha área de vendas e ver quanto que eu vendi. Ele consegue agendar coisas no meu calendário, ele consegue fazer buscas na internet, ele consegue acessar um drive do Google Docs, ler o meu Excel, gerar um PowerPoint. Todas essas coisas, hoje em dia, já são possíveis e elas vão funcionar cada vez melhor se você dominar prompt.

06:59

você realmente entender como que você pode perguntar. Cada dia os modelos, eles estão ficando, vamos dizer assim, mais inteligentes, entendendo os nuances da intenção que a gente está escrevendo, mesmo se você não tiver um bom prompt.

07:14

Mas você vai perceber que o jogo muda completamente conforme você sabe como estruturar, como perguntar. E o interessante é usar cada tipo de prompt para cada situação, para cada escopo. Então, no final das contas, hoje em dia, a gente tem infinitas possibilidades para extrair informação.

07:33

A IA agora acessa dados externos, tem tools que vão trabalhar, fazem chamadas, MCPs, tem diversos protocolos hoje em dia que fazem com que a gente, como usuário final, possamos ter tarefas extremamente complexas que poderiam durar dias e semanas sendo feitas. E, muitas vezes, o resultado de um relatório que você pediu, ou uma documentação que foi gerada, ou uma análise de um code base que você pediu,

08:03

muda completamente de acordo da forma como você pediu, da técnica que você utilizou. Então, o nosso objetivo aqui é realmente fazer com que você domine essas técnicas, que você seja muito mais intencional na hora de você trabalhar no dia a dia, independente como usuário final de um chat GPT, de um Gemini da vida, ou desenvolvendo as suas aplicações, ou sendo mais produtivo no dia a dia, trabalhando aí com IA.

08:28

Beleza? Então, essa era a visão geral que eu queria dar aqui pra você do nível de importância que a gente tem em relação ao Prompt Engineering. Eu sei que tô falando bastante, eu sei que tem muito do Show Me the Code, mas eu acredito que cada momento vai ficar mais claro de acordo com os nossos próximos passos, principalmente quando a gente for trabalhar nos nossos tipos de Prompts. Beleza? Então, é isso aí.

## Resumo IA

**Abreviações**
- IA — Inteligência Artificial
- GPT — Generative Pre-trained Transformer
- CRM — Customer Relationship Management
- Go — linguagem de programação Go
- MCP — Model Context Protocol

**Resumo**
A aula apresentou o Prompt Engineering como uma prática que assume papéis diferentes conforme o contexto. No desenvolvimento de software, ele é usado para aumentar produtividade, apoiar programação e organizar contexto para a IA; nesse cenário, prompts longos e detalhados podem ser aceitáveis. Já em aplicações que usam IA como parte central do produto — como agentes, assistentes e sistemas multiagente — o prompt passa a governar comportamento operacional, escopo, proatividade, segurança e integração com dados externos, exigindo maior rigor de projeto.

O instrutor destacou que, quando o prompt está dentro da aplicação, seu tamanho e complexidade afetam diretamente custo, latência e eficiência. Por isso, o objetivo não é simplesmente “dar mais contexto”, mas equilibrar qualidade da resposta com viabilidade operacional. O prompt deve delimitar até onde o sistema pode ir, definir ações permitidas e deixar claros critérios de atuação, especialmente em fluxos críticos como cálculos, recomendações e transações sensíveis.

Outro ponto central foi o grau de proatividade do agente. O prompt pode fazer a IA apenas responder, esclarecer, sugerir, planejar ou executar ações adicionais. Esse controle é importante para evitar tanto passividade excessiva quanto comportamento invasivo, como a IA começar a executar tarefas quando o usuário só queria uma explicação. Também foi abordado que a instrução precisa orientar como dados externos serão usados, incluindo bancos de dados, documentos, conectores e ferramentas, sempre com restrições explícitas.

A aula também enfatizou que prompts podem se tornar superfície de ataque, impactando privacidade e segurança. Instruções mal desenhadas podem permitir vazamento de informações, acesso indevido a dados sensíveis ou execução fora do escopo esperado. Em modelos menores ou agentes altamente especializados, pequenas mudanças no prompt podem quebrar o comportamento, então o prompt deve ser tratado como uma interface crítica: claro, estável e testável.

Por fim, o instrutor reforçou a ideia de que o prompt funciona como uma espécie de “nova linguagem de programação”, pois expressa regras, limites e intenções que influenciam o comportamento real do sistema. Isso vale tanto para aplicações internas quanto para uso cotidiano em plataformas como ChatGPT, Gemini e Claude, principalmente quando se usam modos agente, deep research, conectores e tools para consultar CRM, agenda, internet, documentos e planilhas. A escolha do tipo de prompt deve variar conforme o objetivo, e não existe um prompt ideal para todas as situações.

**Pontos de atenção**
- Não generalizar o uso de prompt engineering: o que funciona para apoiar desenvolvimento pode não funcionar em produção.
- Em aplicações com IA, prompts grandes aumentam consumo de tokens, custo e latência.
- Prompts devem definir claramente escopo, limites e ações permitidas, sobretudo em tarefas críticas.
- Controlar a proatividade do agente é essencial para evitar respostas passivas demais ou ações indevidas.
- Ao usar dados externos, o prompt precisa explicitar finalidade, restrições e contexto de uso.
- Segurança e privacidade dependem também da engenharia do prompt; ele pode ser vetor de vazamento ou abuso.
- Em modelos pequenos ou agentes especializados, pequenas alterações no prompt podem quebrar o comportamento esperado.
- Prompts devem ser claros, estáveis e testáveis, como uma interface crítica de software.
- Conectores, tools, agentes e protocolos só geram valor quando bem instruídos; acesso a dados sozinho não garante qualidade.
- Escolher o tipo de prompt adequado para cada tarefa melhora previsibilidade, utilidade e eficiência.