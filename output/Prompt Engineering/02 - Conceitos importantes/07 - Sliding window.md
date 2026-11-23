Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16602)

## Resumo da aula

Sliding window é o padrão de tratar o histórico como uma janela móvel que avança ao longo do tempo. Retomando a restrição de janela de contexto já conhecida, a aplicação mantém dentro dela apenas a parte mais recente da conversa e deixa o conteúdo antigo para fora. A ideia central não nasceu em LLMs: ela já aparece em vários problemas de computação, como algoritmos clássicos e rate limiting. O valor desse padrão está em organizar crescimento contínuo sem tentar manter todo o passado ativo ao mesmo tempo.

Quando novas mensagens entram, a janela se desloca e empurra mensagens antigas para fora da área ativa. Isso cria um comportamento temporal explícito: o sistema privilegia o presente da interação, não o histórico completo. Retomando o cenário da conversa longa, o que o modelo consegue considerar é apenas o que ainda está dentro dessa faixa móvel. Sliding window, portanto, não é só um corte; é uma política contínua de atualização do contexto recente.

Quando uma mensagem sai da janela, a aplicação precisa decidir se ela será descartada ou arquivada. Descartar é aceitável quando o histórico antigo perdeu valor operacional para a próxima resposta. Arquivar faz sentido quando aquele conteúdo ainda pode ser útil depois, seja para sumarização futura, seja para auditoria, retomada de sessão ou revisão de decisões anteriores. Essa escolha define se o sistema apenas limita contexto ou também preserva memória externa.

Arquivar histórico fora da janela permite manter o prompt enxuto sem perder definitivamente o passado da interação. Esse armazenamento pode ser de curto prazo, quando o objetivo é resumir depois, ou de longo prazo, quando a conversa é salva integralmente para possível reutilização futura. O ponto importante não é o provedor de storage, mas a separação entre contexto ativo e histórico persistido. A janela continua pequena, enquanto o histórico completo fica disponível fora dela a baixo custo.

Sliding window convive com truncamento e sumarização, mas não é a mesma coisa. O truncamento define o corte do que sai; a sumarização pode reaproveitar parte do que saiu em forma comprimida; sliding window descreve o movimento contínuo da faixa de contexto ao longo da conversa. Em uma aplicação real, os três mecanismos podem aparecer juntos: a janela anda, o excedente sai, e parte dele pode ser arquivada ou resumida. Essa combinação transforma o gerenciamento de histórico em uma decisão arquitetural, não apenas em um ajuste de prompt.

A forma mais simples de visualizar o padrão é imaginar uma moldura fixa deslizando sobre uma sequência crescente de mensagens. Só o que está visível dentro da moldura entra na chamada atual do modelo; o restante fica fora do processamento imediato. A referência a problemas de LeetCode ajuda porque a lógica é a mesma de uma janela que anda sobre dados, preservando apenas um intervalo relevante por vez. Em sistemas conversacionais, esse intervalo relevante costuma ser o histórico mais recente.

## Transcrição

00:01

E agora, pessoal, que a gente falou em sumarização, eu queria falar rapidamente, isso é bem rápido mesmo, porque é algo que acaba sendo até óbvio, mas eu não posso deixar de citar, tá? Toda vez que você ouvir falar em sliding window, tá?

00:17

janela deslizante, o windowing, tá? Isso significa o quê? É tratar o histórico de mensagem que a gente tem como uma janela móvel que ela vai se deslizando, né? Deixa eu até dar um enter aqui pra ficar melhor pra você ler o texto completo.

00:35

ela vai deslizar sobre o conteúdo conforme ele vai crescendo. Esse conceito de slide on window, na realidade, ele não foi criado por conta de Al Prompt em Engineer ou qualquer coisa desse tipo. Esse conceito é muito antigo e serve para diversas áreas da computação o tempo todo. Ele é um padrão. Desde um rate limiter tem slide on window, como outros tipos de aplicabilidade.

01:01

Então, na prática, a gente vai ter sempre a versão mais recente do texto dentro do limite. A gente pode descartar ou arquivar o conteúdo que ficou para trás. E aqui que é uma outra coisa que muita gente acaba esquecendo durante uma conversa. Por isso que é importante a gente falar.

01:18

Descartar ou arquivar. Por que isso é importante? Porque eu já vi muita gente, conforme está falando, tendo aquelas conversas com a IA, as conversas mais antigas vão ficando fora de contexto, mas ela se perde. Não é gravado num banco de dados, não é sumarizado, não é feito nada.

01:39

ou seja, você perde o histórico completamente. Então, dependendo do contexto que eu estou, pode ser sim que, dane-se, eu posso descartar o que está de conversa antiga e não tem problema, mas eu também posso querer arquivar essas informações para que em algum momento eu possa sumarizar, ou possa revisitar, ou possa fazer qualquer tipo de coisa. Mas, basicamente, a ideia da Sliding Window é isso aqui.

02:06

Eu comecei aqui, vamos dizer, esse é o tamanho da minha janela, essa parte rosa aqui que você vê, e conforme eu vou escrevendo, tendo mais interação, o que ele vai fazendo? Ele vai jogando conteúdo antigo para trás, ou seja, fica fora da janela, e começa a entrar conteúdo novo aqui para dentro da janela. Então, isso basicamente é Sliding Window. Se você já

02:32

fez leach code alguma vez na sua vida, em alguns processos seletivos, tem vários casos de uso de leach code que você vai ter que criar um algoritmo de janela deslizante. Então, é basicamente isso. O que entra na janela de contexto aqui da minha A é o que está dentro dessa janela.

02:51

o que não estiver nessa janela está sendo descartado ou arquivado. E eu gosto muito de lembrar para você, sim, eu posso arquivar conversas. E, eventualmente, eu posso arquivar conversas a curto prazo, porque eu posso vir a sumarizar algo, ou eu posso até mesmo arquivar uma conversa a longo prazo, onde eu pego aquela conversa e até mesmo, em vez de sumarizar, eu salvo isso em um arquivo e jogo isso em um S3, por exemplo,

03:20

ou no Google Cloud Storage, por exemplo, também, e esses dados ficam armazenados de uma forma bem barata, não ficam ocupando espaço gigante, porque cada dia a mais a gente vai ter mais informação. Então, rotinas desse tipo cada vez vão ficando mais comuns de você ver aí no dia a dia. Beleza? Então, somente para constar, falamos aqui rapidamente de Sliding Window. Vamos nessa!

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **AI** — *Artificial Intelligence* (Inteligência Artificial)  
- **Prompt Engineer** — Engenharia de Prompt  
- **LeetCode** — plataforma de अभ्यास/treino de algoritmos e desafios de programação  
- **S3** — *Amazon Simple Storage Service*  
- **Google Cloud Storage** — serviço de armazenamento em nuvem do Google Cloud  

**Resumo**  
A aula apresentou o padrão **sliding window** como uma forma de tratar o histórico de mensagens de maneira dinâmica, mantendo apenas a parte mais recente dentro de uma janela de contexto móvel. O instrutor explicou que essa ideia não é exclusiva de LLMs ou de aplicações de IA conversacional, mas um padrão clássico da computação, presente em problemas algorítmicos e também em casos como *rate limiting*. O objetivo é controlar o crescimento contínuo de dados sem tentar manter todo o passado ativo ao mesmo tempo.

Foi mostrado que, à medida que novas mensagens chegam, a janela desliza: o conteúdo antigo sai da área de contexto ativo e o conteúdo novo entra. Assim, o sistema privilegia o presente da interação, e tudo o que ficou fora da janela deixa de participar da resposta atual. O instrutor destacou que isso não é apenas um corte pontual, mas uma política contínua de atualização do contexto recente.

A aula também diferenciou o que pode acontecer com o conteúdo que sai da janela: ele pode ser **descartado** ou **arquivado**. O descarte faz sentido quando o histórico antigo não tem mais valor operacional imediato; já o arquivamento é útil quando ainda existe a possibilidade de reaproveitamento, como em sumarização futura, auditoria, retomada de sessão ou revisão de decisões. Nesse ponto, foi enfatizada a separação entre **contexto ativo** e **histórico persistido**.

O instrutor explicou que arquivar permite manter o prompt enxuto sem perder o passado da interação, podendo usar armazenamento de curto prazo ou de longo prazo. Esse histórico pode ser salvo em soluções como **S3** ou **Google Cloud Storage**, de forma barata e escalável, sem sobrecarregar a janela de contexto. Por fim, a aula reforçou que **sliding window**, **truncamento** e **sumarização** são mecanismos diferentes, mas que podem coexistir em uma mesma arquitetura: a janela anda, o excedente sai, e parte do conteúdo pode ser resumida ou persistida para uso posterior.

**Pontos de atenção**  
- **Não confundir sliding window com sumarização ou truncamento**:  
  - sliding window = movimento contínuo da janela de contexto;  
  - truncamento = corte do que sai;  
  - sumarização = compressão/reaproveitamento do conteúdo removido.

- **Definir o destino do histórico que sai da janela**:  
  - se for apenas descartado, o sistema perde memória operacional;  
  - se for arquivado, pode ser usado depois em resumos, auditoria ou retomada.

- **Não assumir que todo histórico precisa ficar no contexto ativo**:  
  manter tudo na janela aumenta custo e pode estourar limites de contexto.

- **Separar contexto recente de histórico persistido**:  
  a janela deve permanecer pequena, enquanto o restante deve ir para armazenamento externo.

- **Arquivamento pode ser curto ou longo prazo**:  
  escolher conforme o objetivo — sumarizar depois, revisar depois ou guardar integralmente.

- **Sliding window é um padrão arquitetural recorrente**:  
  aparece em vários problemas de computação, não apenas em aplicações com IA.

- **A janela privilegia o presente da conversa**:  
  informações antigas saem naturalmente da área ativa; se forem importantes, precisam ser preservadas fora dela.

- **Usar armazenamento barato e escalável para histórico**:  
  soluções como S3 ou Google Cloud Storage foram citadas como exemplos adequados para persistência externa.