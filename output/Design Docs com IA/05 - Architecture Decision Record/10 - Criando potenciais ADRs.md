Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17127)

## Resumo da aula

Potential ADR é o dossiê técnico que fica entre a detecção de uma decisão e a escrita da ADR formal. Ele existe para reduzir o salto entre código bruto e documentação final, reunindo contexto suficiente para decidir se a formalização faz sentido e como ela deve ser escrita. Diferentemente da ADR final, esse artefato pode ser mais rico em evidências, perguntas abertas e histórico, porque sua função é preparar o julgamento humano e a geração posterior.

Depois do mapeamento do codebase e da leitura do mapping.md, a identificação pode ser executada por módulo ou componente. Em ferramentas que suportam paralelismo, cada módulo recebe um agente dedicado, o que acelera a análise e evita misturar decisões de áreas diferentes do sistema. Esse recorte melhora a precisão porque cada agente trabalha com contexto local, caminhos de código e responsabilidades específicas daquele módulo.

Um Potential ADR normalmente começa com título da decisão candidata, módulo identificado, categoria arquitetural, classificação de prioridade e data de identificação. Em seguida, descreve o que foi detectado no sistema, qual estratégia está em uso e em que ponto ela aparece no código. Essa estrutura transforma um candidato abstrato em um objeto inspecionável, com escopo claro e pronto para revisão.

A força de um Potential ADR vem das evidências: arquivos, trechos de implementação, configurações, tabelas e referências cruzadas no codebase. Em vez de afirmar apenas que existe uma decisão, o documento mostra onde ela está materializada e como afeta o comportamento do sistema. Isso reduz alucinação documental e facilita validar se a interpretação feita pela IA realmente corresponde à arquitetura implementada.

Quando o histórico do Git está disponível, o Potential ADR pode apontar quando a decisão surgiu, em qual commit e com que mensagem ela foi introduzida. Essa timeline ajuda a reconstruir o contexto perdido, especialmente em sistemas legados onde a motivação original já não está explícita em documentos vigentes. O resultado é uma memória arquitetural mais confiável, porque a decisão passa a ser lida como evolução histórica, não apenas como estado atual do código.

A classificação entre must document e consider, já definida anteriormente, ganha utilidade prática no documento potencial. Must document sinaliza que a evidência encontrada já sustenta formalização prioritária; consider indica que ainda existe zona cinzenta e que o julgamento humano deve confirmar relevância, estabilidade ou impacto. Essa separação evita tanto a omissão de decisões estruturais quanto a inflação do acervo com casos marginais.

O Potential ADR não serve apenas para localizar código; ele organiza o raciocínio arquitetural em torno de impacto, trade-offs, complexidade, conhecimento exigido do time e consequências futuras. No caso de uma estratégia de cache orientada por ambiente, por exemplo, simplificar o desenvolvimento local pode reduzir a paridade com produção. Esse tipo de tensão precisa aparecer antes da ADR formal, porque é ele que justifica a decisão e orienta sua revisão.

Um bom documento potencial explicita o que ainda não está resolvido. Perguntas como “essa estratégia substitui uma decisão anterior?”, “o comportamento é obrigatório em todos os ambientes?” ou “há risco operacional se o fallback divergir de produção?” ajudam a preparar a ADR final sem fingir certeza onde ainda há dúvida. Essas perguntas funcionam como checklist de validação antes da formalização.

Retomando o cenário do Rate Limiter já mapeado anteriormente, a camada nova agora é a pré-documentação da decisão. Quando o sistema usa In-Memory Map-Based Storage Backend, o Potential ADR registra que a implementação é thread-safe, usa mutex, oferece TTL e troca simplicidade por risco de consumo de memória; quando aparece Client Key Extraction Strategy, o documento mostra que a forma de identificar o cliente não é detalhe local, porque altera diretamente a semântica do rate limiting. O valor está em transformar recorrências do código em decisões argumentadas, com evidência, impacto e perguntas pendentes.

A saída da identificação costuma ser uma pasta de potential-adrs, separada por prioridade e por módulo. Esse arranjo permite inspecionar rapidamente o que merece ADR imediata e o que ainda depende de análise adicional ou ajuste de prompt e fórmula de priorização. Só depois dessa leitura faz sentido gerar a ADR formal, porque a decisão já chega com contexto reconstruído e menos espaço para ambiguidade.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior eu mostrei um pouco pra vocês em relação a essa parte do mapping, deixa eu até apagar aqui. Eu queria que vocês tivessem uma ideia quando o projetinho é um pouco maior. Uma outra ideia que eu posso dar pra vocês, se vocês quiserem testar esses tipos de coisa, entre em um projeto open source muito grande. Faça o download, faça o clone desse projeto no Git. Rode esses prompts em cima desses projetos. Você vai começar a achar bem interessante as informações que acabam pegando.

00:27

Mas lembra que eu falei aqui pra vocês que a primeira fase era mapear? A minha segunda fase, agora, aqui no final das contas, é identificar quem é o cara. E aí, nesse ponto, eu posso escolher quais são os módulos que eu quero identificar. E aqui, ele passou aqui pra mim cinco caras. Esse projeto é extremamente pequeno. Então, eu vou colocar assim, ó, barra, ADR,

00:53

a Identify, e eu vou passar aqui todas as passas, porque é um projeto muito pequeno, tá? Enquanto ele vai fazer esse cara aqui, ó, e você vai começar a perceber que, no caso do Cloud, mas você poderia estar usando a... sei lá, o VST Código, o GitHub Copilot, você vai perceber agora que aqui ele já vai gerar agentes em paralelo. Aí vai depender muito da ferramenta que você tem. De A, no caso do Cloud, ele faz isso. Então, para cada um,

01:23

desses módulos que ele encontrou, ele soltou um agente específico para cada cara, e agora ele vai a fundo nesse agente, porque ele leu aquele mapping.md, onde dá um detalhe a mais sobre aquele agente, aquele módulo, o caminho, o que ele fez, ou seja, ele trouxe contexto

01:47

para que, baseado nisso, ele possa identificar possíveis ADRs que estão ali nesse projeto. Honestamente, eu nunca rodei isso contra esse codebase tão pequeno das ADRs. Eu, inclusive, estou curioso aqui para saber, tá? Mas, enquanto ele faz isso, eu quero dar um exemplo aqui para vocês de potenciais ADRs que eu tenho

02:16

em um projeto aqui pra que você consiga entender aqui, tá? Eu vou pegar aqui algumas possíveis ADRs aqui pra mim. Só um segundinho enquanto ele vai rodando aqui, galera. Ok. Eu vou colar aqui embaixo somente pra gente dar uma olhada.

02:37

Eu criei aqui infrareds, tá? Então, isso aqui é uma possível ADR. E perceba, isso não é uma ADR, tá? No que eu vou clicar agora aqui. Então, o que esse cara faz aqui? Olha só que interessante.

02:50

Ele é uma Potential ADR, para Environment Driven Cache Driver Selection Strategy. Ele está falando que o módulo é Infrared, porque ele identificou o módulo no sistema, a categoria é Arquitetura e Configuração, é um Must Document, ou seja, esse documento provavelmente tem que ter, e a data de identificação que esse cara foi. E daí ele vai trazer, o que foi identificado? Que a plataforma implementa um...

03:19

Environment-Driven Cache Driver Selection Strategy, condicionado ao Sync Redis Bundle, para trabalhar com Redis in Production, ou trabalhar de forma fake para desenvolvimento, aí tem Cache Driver, etc. Falando, isso aqui foi introduzido em março de 2024, no comite Update Cache Driver to Redis if Cache Driver Environment Variable is Set to Redis. Ou seja, ele pegou até o nome do comite,

03:48

onde isso aí foi introduzido em algum momento. E daí ele fala, essa arquitetura vai substituir

03:58

a arquitetura always-on-reds required ali pra gente. Ou seja, a arquitetura antes dessa era que, obrigatoriamente, você sempre tinha que usar o reds. O que foi mudado é que agora você nem sempre precisa mais usar o reds. Aqui ele coloca dados mais técnicos, estratégia, vai um pouco além de simples off e não, mostra as configurações. Por que isso precisa ser uma DR?

04:22

Daí ele mostra impacto, afeta o workflow de desenvolvimento de 100% dos desenvolvedores locais e o setup. A parte de CI também muda, a parte de production também muda. Quais são os trade-offs? Isso aqui ajuda a simplificar o desenvolvimento local, ou seja, porque eu não preciso do Redis, mas ele acaba perdendo um pouco a paridade do que está em produção e do que está local.

04:46

complexidade, conhecimento do time, implicações futuras e evidências que foram encontradas no codebase em relação a tudo isso aqui. E aqui eles começam a colocar

05:01

evidências de código mostrando que isso aconteceu, e aí ele gera tabelas, questões que podem ser perguntadas caso crie uma ADR em relação a essa, aqui ADRs potenciais que podem estar ligadas com esse cara aqui, algumas notas adicionais,

05:22

Então, perceba galera, esse documento aqui de potenciais ADRs, perceba que ele é um documento muito mais completo, ao ponto de quando eu for criar uma ADR, onde a minha ADR não deve ser um documento grande,

05:37

fique mais fácil para ele criar essa ADR de uma forma mais assertiva. Perceba que ele consegue pegar para a gente a linha do tempo quando essa decisão foi tomada. E isso aí que eu acho que é uma das coisas mais...

05:53

interessantes aí pra gente ver. Então, tem muito esquema aqui. Multidriver Session Storage Strategy. Porque antes eu poderia trabalhar com File, com Database e com Redis. Então, olha só, Session Driver, quando que esse cara impacta, complexidade, evidências de código,

06:13

Meu, e assim vai, entendeu? Então, a gente tem diversos exemplos, eu copiei uma das pastas só onde falava só de Redis, mas são diversos e diversos documentos que a gente pode encontrar ao longo do tempo aqui. Conforme esse agente vai trabalhando, o que ele faz?

06:32

dentro dessa pasta ADRs, ele gera aqui, ó, Potentials ADR. E aqui eu tenho Must Document, onde, dentro desse Must Document, eu tenho um módulo, na realidade, ou componente, da forma como você queira chamar, que provavelmente vai ter uma ADR. Então, por exemplo, Storage. Então, aqui, provavelmente tem uma In-Memory Map Storage Backend.

07:00

E aqui ele está colocando o seguinte, olha só. O módulo é Storage, a ADR principal é In-Memory Mapped Based Storage Backend. O que foi identificado? Que o Rate Limiter trabalha com Thread Safe, com um mapa baseado em memória, trabalhando com Mutex. A implementação provê uma key value com TTL, com suporte de TTL.

07:24

o impacto da decisão é que afeta o... Por que tem que ter, né? Porque afeta o sistema inteiro, o trade-off é que fica mais simples, mas, ao mesmo tempo, eu posso sofrer com capacidade muito grande de memória,

07:39

a parte de complexidade, a parte do conhecimento do time, implicações futuras, evidências dentro do código que acabam mostrando isso que está sendo falado, análise de impacto, o Git não estava disponível, afetou oito arquivos, a performance, o Redis foi mencionado, mas não está aqui trabalhando nesse caso, qual o problema que estava sendo respondido, etc, etc, etc.

08:08

Ou seja, perceba que o que ele está gerando aqui para a gente são potenciais ADRs. Por exemplo, olha só, a Client Key Extraction Strategy. Olha só, ele está trazendo agora aqui quais são as estratégias que eu vou usar para conseguir extrair os dados para eu conseguir

08:29

identificar quem está acessando o meu Rate Limiter. E aí ele mostra que existem diversas formas que estão sendo utilizadas. E o impacto é que vai determinar como o cliente vai ser identificado. Então, apesar de parecer uma

08:46

uma decisão de baixo nível, é uma decisão extremamente estratégica, porque o papel do Rate Limiter é exatamente identificar esses caras. Então, ele está falando qual que é o impacto, qual que é o trade-off, qual que é o nível de complexidade, o que o time tem que saber, quais são as futuras implicações, evidência de código e etc., perguntas que têm que ser feitas, caso a ADS seja criada e notas adicionais aqui sobre isso. Então, agora, se você olhar aqui no Cloud, ele gerou, aqui para mim,

09:15

todas as possíveis ADRs que eu tenho. Agora, se você perceber, eu tenho must document, ou seja, são documentos que ele fala, cara, isso aqui você tem. Baseado nas regras que você me passou, esses caras têm que existir. Mas tem documentos a serem considerados. Por exemplo, limiter.

09:35

em memory, por instância, com rate limiting. Então, ele fala, cara, isso aqui pode ser considerado, mas eu não acho que é obrigatório, baseado nas contas que eu fiz. Basicamente, isso que ele acaba fazendo, a gente criou uma fórmula e baseado nessa fórmula, a gente olha qual é a prioridade e depois, se você quiser, você muda o prompt, muda e cria a sua própria fórmula e etc. Mas o que eu quero explicar aqui nesse momento é que isso aqui

10:00

é uma potencial ADR. A gente não está gerando a ADR ainda, beleza? Próximo vídeo, vamos ver como a gente gera uma ADR para que vocês consigam ver.

## Resumo IA

**Abreviações**

- **ADR** — *Architecture Decision Record* (Registro de Decisão Arquitetural)
- **CI** — *Continuous Integration* (Integração Contínua)
- **Git** — sistema de controle de versão distribuído
- **TTL** — *Time To Live* (tempo de vida)
- **VST** — provavelmente referência ao **Visual Studio Code** no contexto da fala, usado como editor/IDE
- **Redis** — banco de dados em memória frequentemente usado como cache e armazenamento de estruturas de dados

**Resumo**

A aula apresentou a fase de identificação de decisões arquiteturais em um codebase, após a etapa anterior de mapeamento. O instrutor explicou que, depois de ler o `mapping.md`, a análise pode ser feita por módulo ou componente, e que ferramentas com suporte a paralelismo conseguem criar agentes dedicados para cada módulo, acelerando a investigação e evitando misturar contextos de áreas diferentes do sistema.

O foco principal foi o conceito de **Potential ADR**, um dossiê técnico intermediário entre a detecção de uma decisão e a escrita da ADR formal. Esse documento não é a ADR final, mas reúne contexto suficiente para avaliar se a decisão merece formalização, com escopo claro, evidências concretas e perguntas em aberto. A estrutura típica inclui título da decisão candidata, módulo identificado, categoria arquitetural, prioridade, data de identificação, descrição do que foi detectado, estratégia em uso e local onde isso aparece no código.

O instrutor destacou que a força desse artefato está nas evidências: arquivos, trechos de implementação, configurações, tabelas e referências cruzadas no sistema. Quando disponível, o histórico do Git também entra como parte da documentação, permitindo reconstruir quando a decisão surgiu, em qual commit e com qual mensagem. Isso ajuda especialmente em sistemas legados, onde a motivação original já não está clara. O objetivo é reduzir alucinação documental e aumentar a confiança de que a interpretação da IA reflete a arquitetura real.

Foi explicado também o uso prático da classificação **must document** e **consider**. A primeira indica que a evidência já sustenta uma ADR prioritária; a segunda mostra que ainda há uma zona cinzenta e que o julgamento humano precisa confirmar relevância, impacto e estabilidade. Na prática, isso ajuda a evitar tanto a omissão de decisões importantes quanto o excesso de documentação de casos marginais.

Por fim, o instrutor mostrou exemplos reais de Potential ADRs, como uma estratégia de seleção de cache baseada no ambiente, uma estratégia de storage em memória para rate limiter e uma estratégia de extração de chave do cliente. Em cada caso, o documento registra impacto, trade-offs, complexidade, conhecimento exigido do time, implicações futuras e evidências de código. A saída organizada em pasta, separada por prioridade e módulo, serve como base para a geração posterior da ADR formal, que só deve acontecer depois que o contexto já estiver reconstruído e a decisão estiver suficientemente argumentada.

**Pontos de atenção**

- O **Potential ADR não é a ADR final**; ele serve como pré-documentação e preparação para a formalização.
- A análise deve ser feita **por módulo/componente**, de preferência com agentes paralelos quando a ferramenta suportar.
- O arquivo `mapping.md` é importante para fornecer **contexto local** e melhorar a precisão da identificação.
- Uma boa Potential ADR precisa de **evidências concretas** no codebase; não basta inferir a decisão sem suporte.
- Quando houver histórico no Git, ele deve ser usado para reconstruir a **linha do tempo da decisão**.
- A distinção entre **must document** e **consider** evita excesso de documentação e também evita deixar decisões críticas sem registro.
- O documento potencial deve explicitar **trade-offs, impacto, complexidade e implicações futuras**, não apenas descrever a implementação.
- Perguntas em aberto devem ser registradas antes da ADR formal, como forma de **checklist de validação**.
- Decisões aparentemente de baixo nível, como extração da chave do cliente, podem ter **alto impacto arquitetural**.
- A pasta de saída deve ser organizada por **prioridade e módulo** para facilitar revisão e geração da ADR.
- A ADR formal deve ser escrita **somente depois** da etapa de potencial ADR, para reduzir ambiguidade e aumentar a assertividade.