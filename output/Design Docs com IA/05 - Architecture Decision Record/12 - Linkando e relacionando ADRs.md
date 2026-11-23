Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17129)

## Resumo da aula

ADR Linker é a etapa que transforma ADRs isoladas em um acervo conectado. Em vez de apenas listar documentos, ele analisa o conjunto de ADRs, o mapeamento anterior e os artefatos já gerados para inferir vínculos entre decisões. O resultado não é só documental: ele cria uma estrutura navegável que mostra como uma decisão depende de outra, complementa outra ou substitui uma decisão anterior. Isso reduz o risco de tratar cada ADR como um registro solto e sem contexto histórico.

O fluxo parte do que já foi produzido nas etapas anteriores: mapeamento, Potential ADRs e ADRs formais. O agente percorre esse acervo e tenta identificar relações como dependsOn, relatesTo, supersedes, substituição parcial e estado atual da decisão, usando os sinais já levantados no processo. A qualidade da linkagem depende diretamente da qualidade das evidências acumuladas antes; por isso, ela não substitui as etapas anteriores, ela as consolida. Quando a base está boa, o agente consegue reconstruir conexões que não aparecem de forma explícita em um único documento.

Um acervo linkado deixa de ser uma pasta de arquivos e passa a funcionar como um grafo histórico de decisões. Cada ADR vira um nó conectado a decisões anteriores e posteriores, permitindo navegar pela evolução arquitetural sem depender de memória oral do time. Retomando o cenário de autenticação já formalizado, a decisão de 2014 pode aparecer como base para escolhas posteriores, como a adição de JWT para API em 2021 ou integrações com Google e GitHub. Essa leitura encadeada mostra não apenas o que foi decidido, mas como uma escolha abriu caminho para outras.

Quando a IA encontra ADRs conectadas por tempo e relação, ela deixa de enxergar apenas documentos estáticos e passa a interpretar uma sequência de decisões. Isso melhora a recuperação de contexto porque o modelo consegue associar motivação, consequência e continuidade arquitetural ao longo dos anos. Em um sistema legado, essa timeline reduz a perda de racional que normalmente acontece quando o código permanece, mas o motivo original desaparece. O ganho não é só histórico: ele influencia a qualidade das próximas sugestões e análises automatizadas.

A linkagem não nasce do nada; ela depende dos indícios capturados antes, especialmente nas Potential ADRs e no histórico do repositório. Se a etapa anterior já trouxe datas, evidências, perguntas em aberto e sinais de evolução, o agente consegue conectar melhor uma decisão a outra. Por isso o caso de autenticação funciona: a decisão inicial, os pontos de Needs Input e a introdução posterior de JWT formam uma trilha coerente para o linker explorar. Sem esse preparo, a automação tende a gerar relações fracas ou arbitrárias.

Um acervo de ADRs sem links escala mal, porque a quantidade de documentos cresce mais rápido do que a capacidade humana de lembrar conexões. A linkagem resolve esse problema ao permitir que alguém entre em uma ADR e navegue para antecedentes, dependências e desdobramentos sem precisar reconstruir tudo manualmente. Para a IA, isso aumenta a precisão porque o contexto deixa de estar espalhado em arquivos independentes e passa a existir como rede semântica de decisões. O efeito prático é menos reinvenção documental e mais capacidade de entender por que o sistema chegou ao estado atual.

Mesmo em um projeto pequeno e sem Git completo, a linkagem ainda pode produzir valor se houver ADRs suficientes para inferir relações. Quando uma DR01 aparece como dependente de outra decisão e relacionada a uma terceira, já surge um caminho de navegação que organiza estratégias e middleware em sequência lógica. Esse encadeamento ajuda a entender opções disponíveis sem ler todos os documentos do zero. A ausência de data reduz a precisão histórica, mas não elimina o benefício estrutural da rede de relações.

A linkagem automatizada é um ponto de partida forte, não uma verdade final. Como qualquer processo baseado em código, histórico e inferência, ela precisa de revisão para confirmar se as relações fazem sentido arquitetural e não apenas textual. O ganho real está em evitar começar do zero e em revelar decisões, trade-offs e consequências que já existiam, mas estavam dispersos. Revisar um grafo inicial é muito mais barato do que reconstruir manualmente dez anos de arquitetura.

## Transcrição

00:01

Bom pessoal, no vídeo anterior eu mostrei pra vocês algumas ADRs, rodei num sistema que a gente tem aqui na Full Cycle. Gente, a gente tem bastante sistema, mais do que eu gostaria de ter, tá? A gente tem sistema na parte educacional, sistema na área de B2B, coisas de IA, a gente tem diversos repositórios aqui e tudo mais. Mas eu peguei um deles, que é o sistema mais antigo, exatamente porque

00:25

é um sistema de mais de 10 anos atrás, e rodando esse sistema a gente conseguiu ver muita coisa interessante de decisões que foram mudando ao longo do tempo, e eu acho que isso que vai tornando esse processo muito mais legal, tanto pra IA e quanto outros desenvolvedores que chegam aqui na empresa, tá? Agora, o ponto aqui é que você gerar ADR é uma coisa, mas o interessante de tudo, né, e que eu mostrei pra vocês aqui,

00:54

é que essas ADRs estão linkadas com outras ADRs, se você perceber. Elas realmente linkaram com outras ADRs. Tem ADRs aqui que foram substituídas. Deixa eu ver se eu acho aqui related to, deixa eu ver se eu acho aqui algum exemplo de superseded.

01:16

não tô achando, mas existem, tá? ADRs que substituíram outras ADRs aqui. É que nos exemplos que eu tô, não tô achando aqui, mas tem ADRs que elas foram realmente alteradas conforme a gente foi mudando algumas estratégias aqui na empresa. Mas esses links não são fáceis de gerar também, porque existe toda uma coisa muito louca, né? Então, o que a gente fez? Criei aqui um comando chamado ADR link.

01:46

E quando eu dou um Enter, o que esse cara vai fazer? Ele vai soltar um agente, e esse agente vai analisar todas as ADRs, vai olhar todo o mapeamento, vai olhar tudo que foi feito, e aí ele vai tentar encontrar a relação

02:01

entre uma ADR e outra ADR. Para falar se uma depende da outra, se uma substituiu a outra, se ela foi substituída por outra, se ela foi substituída parcialmente, se ela está depreciada ou se ela está ativa até o momento. Então, isso aí que eu acho que acaba sendo bem interessante para a gente ter essas partes de links. Porque se você não tem links, você, no final das contas, começa a ficar perdido pela grande quantidade de ADRs que a sua empresa pode ter.

02:30

Aqui, olha, tem a parte do chat com a IA, tem o multi-provider de autenticação, porque tem o checkout, tem uma relação com a parte de autenticação. Então, se eu entro aqui, olha só, em 2014, foi tomada uma decisão para o formato de autenticação.

02:53

E daí, baseado nisso, tem Needs Input novamente aqui pra gente. Ah, como que isso aqui era serializado em relação à autenticação? Ah, eu tenho autenticação agora, que a gente fez naquela época, também adicionamos, sei lá, token JWT pra acesso API em 2021.

03:13

E aí a coisa vai andando. Ele mostra o que foi feito. Por que ele consegue mostrar isso, galera? Porque naquela potencial ADR, naquela pesquisa que foi feita, trouxe esses pontos. Com esses pontos, mais a busca no processo de gerar ADR, ele conseguiu identificar esses pontos. E ele começa a relacionar com outras partes aqui. O bando onde que trabalha desse cara aqui.

03:38

Opa, fiz autenticação com Google, GitHub e etc. Então, você começa a perceber que você vai navegando pelos documentos, você vai conseguindo trabalhar. Olha, essa aqui foi de 2013 também, tá? Então, esse tipo de informação, pessoal, vale ouro. Vale ouro tanto para o seu time, mas vale ouro para a IA. Porque a IA, de uma forma temporal agora, ela começa a entender as decisões que você tomou e o porquê você tomou.

04:05

Ela vai ter o documento de contexto dela também. Ela vai ter um plano de ação com workflow que você vai aprender a fazer. Então, cada vez você vai conseguir fazer com que a IA tenha mais decisões, como que eu posso dizer, assertivas. Uma vez que ela entende, ela vira um funcionário da empresa que consegue entender o histórico do que aconteceu naquele sistema de 2013 até 2030.

04:35

E com isso, as coisas acabam fazendo uma bela diferença no meio de toda essa história. Galera, isso é perfeito? Não!

04:45

Isso é código, e se é código, precisa de revisão, tá? Então, mas é um baita ponto de partida pra você conseguir olhar e falar, não preciso mais criar isso do zero. Tem decisões que foram tomadas aqui que eu nem sabia que elas tinham sido tomadas, e agora eu sei que elas foram tomadas. E o mais interessante, eu sei o porquê que elas foram tomadas e, né,

05:09

o trade-off que ela tem, quais são as consequências que ela acaba gerando em relação a tudo isso. Aqui, esse agente, basicamente, o que ele faz é, ele vai buscar todas as ADRs, entender, ver a relação de cada uma delas, e ela começa a fazer os links de uma ADR para outra, para que a gente consiga navegar. Então, são esses passos, o passo de mapear,

05:34

o passo de gerar as ADRs potenciais, o passo de gerar as ADRs e o passo de linkar as ADRs. Somente você fazer isso, por mais que você vai ter que revisar, mexer,

05:46

Meu, eu vou dizer que já vai facilitar bastante a sua vida e são documentos extremamente importantes. Então, de forma geral, galera, eu espero que vocês tenham curtido aqui. Deixa eu ver se nesse projeto pequeno, que não tem Git, nada ou qualquer coisa desse tipo, ele conseguiu fazer a linkagem de uma coisa com a outra. Eu tenho aqui Midor. Vou pegar esse cara aqui. Olha aqui que interessante, galera. Ele já conseguiu... Deixa eu colocar aqui e fechar esse cara aqui.

06:17

Olha aqui, ele já conseguiu fazer os links. Olha, foi aceitado, ele não tem a data porque não tinha Git e etc. A DR01 depende dessa outra DR e está relacionada a essa outra DR. Se eu clico nessa DR, vai falar que ela foi aceita do dia 16 por algum motivo. Esse cara já estava comitado antes, é por conta disso.

06:41

foi usado por esses caras aqui e tem relação com essas caras. Então, se eu clico aqui, eu vou ver esse cara que depende desse, mas está relacionado com esse também, que vai com esse cara, que depende dessa aqui, que vai para essa estratégia aqui, que vai para o middleware. Então, quando você começa a olhar, você fala, cara, está muito melhor de eu entender as opções que eu tenho agora para conseguir trabalhar.

07:06

Então, era isso que eu queria mostrar em relação a esses agentes, esses tipos de coisa, para conseguir, de forma geral, dar opções para a gente conseguir trabalhar com o IA e ter documentos relevantes.

## Resumo IA

**Abreviações**
- **ADR** — *Architecture Decision Record* (Registro de Decisão de Arquitetura)
- **DR** — *Decision Record* (Registro de Decisão)
- **JWT** — *JSON Web Token*
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)
- **IA** — Inteligência Artificial
- **Git** — sistema de controle de versão distribuído

**Resumo**
A aula apresentou a etapa de **ADR Linker**, responsável por transformar ADRs isoladas em um acervo conectado e navegável. O instrutor explicou que, além de gerar ADRs e ADRs potenciais, é preciso criar vínculos entre decisões para que o histórico arquitetural faça sentido ao longo do tempo. O processo parte do que já foi produzido nas etapas anteriores — mapeamento, Potential ADRs e ADRs formais — e um agente analisa todo esse material para inferir relações como dependência, relação, substituição total ou parcial, desativação e estado atual da decisão.

Foi mostrado que a linkagem não surge do nada: ela depende da qualidade das evidências coletadas antes, como datas, perguntas em aberto, sinais de evolução e contexto extraído do repositório. Com essa base, o agente consegue conectar decisões que, em um documento isolado, não parecem relacionadas, reconstruindo uma timeline arquitetural. O instrutor usou o exemplo de um sistema antigo de autenticação para mostrar como uma decisão inicial pode ser a base para escolhas posteriores, como a adoção de JWT para acesso à API e integrações com Google e GitHub.

A proposta central é transformar um conjunto de arquivos em um **grafo histórico de decisões**, no qual cada ADR vira um nó conectado a antecedentes e desdobramentos. Isso facilita a navegação, reduz a dependência de memória oral do time e melhora a compreensão do porquê de cada escolha. O agente de linkagem é acionado por um comando específico e percorre todas as ADRs para gerar essas conexões automaticamente. Ao final, o instrutor reforça que o resultado não é definitivo: como se trata de um processo baseado em inferência, o grafo precisa de revisão humana, mas já representa um grande avanço por evitar começar tudo do zero e revelar trade-offs e consequências já existentes.

**Pontos de atenção**
- A linkagem depende fortemente da qualidade do mapeamento e das ADRs potenciais geradas antes.
- Sem evidências sólidas, o agente pode criar relações fracas, arbitrárias ou pouco confiáveis.
- ADRs sem links escalam mal, porque a quantidade de documentos cresce mais rápido do que a memória do time.
- A ausência de Git ou de datas reduz a precisão histórica, embora não elimine o valor estrutural da rede.
- Relações como **dependsOn**, **relatesTo**, **supersedes** e substituição parcial precisam ser interpretadas com cuidado.
- O resultado da automação deve ser revisado manualmente; não deve ser tratado como verdade final.
- O objetivo da linkagem é facilitar navegação e contexto, não substituir a análise arquitetural humana.
- Quanto mais completos forem o histórico do repositório e os artefatos anteriores, melhor será a reconstrução das conexões entre decisões.
- A principal boa prática é consolidar primeiro mapeamento, potencial ADR e ADR formal, para só então linkar.
- Revisar um grafo inicial é mais eficiente do que reconstruir manualmente anos de decisões arquiteturais.