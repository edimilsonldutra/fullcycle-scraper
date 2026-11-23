Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16973)

## Resumo da aula

Um prompt de entrevista para PRD transforma a criação do documento em um fluxo guiado, no qual a IA conduz perguntas em vez de apenas receber um comando genérico para “escrever um PRD”. Isso reduz lacunas de contexto e força a coleta progressiva das informações que já foram definidas anteriormente como necessárias em um PRD de feature. A diferença prática está no controle do processo: a IA não parte direto para a redação final, mas primeiro extrai contexto, confirma entendimento e só depois consolida a saída. Esse formato é mais confiável porque trata documentação como coleta estruturada, não como improviso textual.

O prompt pode ser colado diretamente em qualquer IA conversacional ou encapsulado em um assistente configurado, como um MyGPT. A vantagem de configurá-lo como assistente é preservar comportamento estável entre usos: papel da IA, regras de entrevista, formato de saída e restrições ficam persistidos, sem precisar repetir instruções a cada sessão. Operacionalmente, o fluxo é simples: colar o prompt, iniciar com um comando como “comece a entrevista comigo” e responder etapa por etapa. Se houver documentação prévia do projeto, ela deve ser anexada logo no início para reduzir o número de perguntas.

A IA entrevistadora precisa operar com regras explícitas para não degradar a qualidade da coleta. Entre as regras centrais estão: não fazer perguntas duplas, não inventar detalhes técnicos, resumir o que entendeu, pedir confirmação antes de avançar e sugerir formulações quando o usuário ainda não tiver clareza total. Essas regras existem porque, sem elas, a conversa tende a produzir respostas vagas, inconsistentes ou excessivamente abertas. O entrevistador de IA funciona melhor como facilitador estruturado do raciocínio do que como autor autônomo do conteúdo.

A entrevista percorre uma sequência fixa de coleta: contexto e visão, problema ou oportunidade, objetivos, métricas de sucesso, escopo, requisitos, arquitetura ou abordagem, decisões, trade-offs, dependências e riscos. Retomando a estrutura de PRD de feature já estabelecida, a novidade aqui é que cada seção vira uma etapa operacional com perguntas específicas e confirmação intermediária. Isso evita que a IA misture seções ou antecipe conclusões sem base suficiente. O ganho principal é rastreabilidade: cada bloco do PRD final nasce de uma etapa explícita da conversa.

Durante a entrevista, a IA mantém um JSON interno com os campos já preenchidos, mesmo que o usuário não veja essa estrutura. Esse armazenamento intermediário organiza a coleta por chave, facilita validações posteriores e evita que respostas dadas no início da conversa se percam no texto livre da sessão. A regra de ocultar o JSON durante a coleta é importante porque o foco do usuário deve permanecer na resposta semântica, não na edição estrutural do documento. No fim, essa estrutura interna pode ser convertida em Markdown e, opcionalmente, exposta como JSON final.

Antes de gerar o PRD final, a IA precisa revisar se as respostas são coerentes entre si, se há campos críticos ausentes e se alguma formulação está ambígua demais para virar especificação útil. Essa checagem impede, por exemplo, que objetivos contradigam o escopo ou que critérios de aceitação apareçam sem relação clara com os requisitos coletados. Em vez de produzir um documento “completo” apenas na aparência, o processo interrompe a geração para pedir esclarecimentos quando necessário. A qualidade do PRD depende menos da fluência da escrita e mais dessa validação semântica prévia.

Defaults inteligentes são valores sugeridos pela IA quando o usuário não sabe preencher um campo, como uma meta inicial de latência P95 menor que 150 ms. Eles existem para evitar bloqueio na entrevista e para oferecer um ponto de partida plausível que depois pode ser revisado. O uso correto desses defaults exige duas condições: o valor deve ser claramente apresentado como sugestão e o usuário deve poder alterá-lo antes da saída final. Sem essa distinção, a IA corre o risco de transformar hipótese provisória em requisito assumido como definitivo.

O template final define a forma do PRD em Markdown e funciona como skeleton of thought para orientar a geração. Isso significa que a IA não apenas escreve “sobre a feature”, mas preenche uma estrutura previamente desenhada, com seções, ordem e estilo já delimitados. O benefício é previsibilidade: documentos diferentes passam a ter a mesma organização, o que facilita revisão humana, comparação entre features e uso posterior por agentes de IA. O template também reduz variação desnecessária de formato entre execuções do mesmo prompt.

A saída principal é um PRD em português, renderizado em Markdown conforme o template definido. Depois disso, a IA pergunta se o usuário também quer a exportação em JSON, mantendo chaves em inglês e omitindo campos vazios, como já foi estabelecido no uso estrutural de JSON em PRDs. Essa separação atende dois consumidores diferentes: pessoas revisam melhor em Markdown, enquanto automações e agentes operam melhor sobre JSON. Tornar o JSON opcional evita atrito quando o objetivo imediato é apenas leitura e revisão humana.

Retomando o PRD já estruturado nas etapas anteriores, o ganho novo aqui está em usar documentação existente como insumo da entrevista. Em vez de responder tudo do zero, o usuário pode fornecer documentos prévios do projeto e instruir a IA a preencher o template com base neles, perguntando apenas o que faltar. Isso reduz esforço, encurta a entrevista e melhora consistência com artefatos já aprovados. A IA passa a atuar como consolidadora e identificadora de lacunas, não apenas como perguntadora serial.

O prompt não deve ser tratado como peça fixa; ele é um artefato operacional que pode ser ajustado conforme o tipo de produto, o nível de detalhe desejado e o padrão documental do time. A revisão da saída deve observar três pontos: se a entrevista perguntou o suficiente, se os defaults usados fazem sentido e se o template final está adequado ao contexto real do projeto. Quando alguma seção gera ruído recorrente, o ajuste correto é alterar a regra ou a pergunta correspondente no prompt, não apenas editar manualmente o documento final. Esse ciclo de adaptação transforma o prompt em infraestrutura de documentação assistida por IA.

## Transcrição

00:01

Bom, pessoal, esse aqui é um prompt que eu criei e que você vai ter acesso agora em seguida para você conseguir gerar um PRD onde a própria IA vai te entrevistar. Então, o que você pode fazer simplesmente? Você pode pegar esse prompt, você pode criar um MyGPT como assistente, você pode entrar em qualquer IA, colar esse prompt e falar

00:25

Comece a fazer a entrevista comigo baseado nesse prompt e a IA vai seguir a partir daí, tá? Obviamente que eu não vou ler todo esse prompt aqui com você porque ele é gigante, tá? Deu um trabalhão pra criar e dá pra perceber que não é simples criar isso porque

00:44

PRDs têm sessões muito grandes, tem diversas perguntas que são feitas e validar, mas eu queria, pelo menos, passar aqui para vocês uma ideia de como que isso funciona e como que eu criei isso, e é uma estrutura de prompt step-by-step que, normalmente, na parte de Prompt Engineer, provavelmente você viu. Então é o seguinte, olha só...

01:05

Basicamente, é um prompt de entrevista para gerar PRD para desenvolvimento de feature. O objetivo é fazer uma entrevista para gerar um Product Required Document. O PRD final deve explicar o porquê essa feature existe, o que ela precisa fazer, como vamos saber quando está pronta e qual sistema vai rodar. O final deve ser renderizado em um formato definido, em um esqueleto.

01:26

E depois, gerar um PRD em português, você deve perguntar ao usuário se ele também quer o PRD exportado em JSON. Esse JSON deve seguir uma estrutura de chaves em inglês definida na estrutura de JSON. Aqui tem o papel da IA, os princípios básicos de como ele vai fazer a entrevista. Eu estou colocando sempre para a IA sugerir, para que a gente não tenha que ficar digitando tudo do zero, então ela ajuda a gente a resumir, a criar.

01:53

pontos importantes, não faça perguntas duplas, não faça aqueles travessões chatos, não invente detalhes técnicos, regras de coleta de informação. Então, aqui tem diversas regras que eu coloquei, depois você pode olhar com calma. Como que vai ser o processo da entrevista? Aqui é o step by step, né? Contece visão, problema, oportunidade, objetivos, métricas de sucesso, escopo, requisitos, funcionais, não funcionais, arquitetura, decisões, trade-offs, dependência, risco, medicação.

02:20

Basicamente, são todos aqueles itens que a gente acabou falando, tá? E aqui, em cada etapa, faça perguntas específicas, resuma o que entendeu, peça confirmação antes de seguir. E aqui, em seguida, eu trago a estrutura em JSON. Durante a entrevista, você deve amazenar essas informações no JSON interno, que segue a estrutura abaixo. O usuário não deve ver esse JSON durante a coleta.

02:42

Ao final, eu gero o PRD em português em Markdown, exatamente descrito no esqueleto, que eu vou mostrar para vocês. Pergunte se o usuário também quer o PRD em JSON. Nesse caso, o JSON deve ser como? E aqui eu trouxe exatamente o formato do JSON, de como esse cara funciona aqui.

02:58

Então, está aqui o desenho do Jason. E eu coloquei regras, né? A chave são sempre em inglês, os valores do conteúdo textual, não inclua campos vazios e coisas desse tipo. E aqui tem as perguntas que vão ajudar a Iá a te entrevistar. Ou seja, quais são as perguntas de contexto e visão? O problema ou oportunidade? As métricas? O escopo? Requisito funcional ou não funcional? Arquitetura ou abordagem? São pontos e guias de pergunta para ele ir perguntando e estressando você

03:27

para que você consiga, e ele consiga gerar um documento mais completo possível ali, tá? E aí, checagem de consistência. Antes de gerar final, verifique se tudo que foi colocado está batendo, né? Se tudo que...

03:43

basicamente foi falado, não tem ambiguidade. Então, esse aí é um ponto importante. Basicamente, ele olha tudo que foi respondido e verifica se não tem alguma coisa faltando ou alguma coisa muito ambígua que pode gerar um resultado que não tenha sentido, tá? E aqui eu trouxe alguns pontos padrão inteligente. Então, toda vez que o cara não souber, por exemplo, a latência, usa um P95 menor que 150 milissegundos.

04:13

Ou seja, ele traz como padrão, como sugestão, e depois você pode alterar. Basicamente isso. Disponibilidade, observabilidade, segurança, atualizações críticas. Aí eu coloquei o estilo, em português, simples e direto. E aqui, finalmente, o esqueleto do PRD, que é o modelo de saída. E dá pra perceber, se você olhar,

04:31

Cara, dá um trabalho danado pedir para ele gerar e chegar nesse modelo para ficar bacana realmente o resultado final. Então, aqui tem basicamente todo o template, um skeleton of thought para ele gerar dessa forma. E aqui tem o início da entrevista, a mensagem inicial para o usuário. Eu sou um assistente de criação de PRDs de features, vou te fazer algumas perguntas e etc. Então, aqui está o prompt, galera. Então, o que eu te desafio a fazer agora é

05:01

pegue esse prompt, brinque com ele, veja o que você quer colocar, veja o que você quer tirar, veja, baseado nesse prompt e baseado numa documentação que você tem, você pode até pedir pra IA, é, baseado nesse prompt e nesse documento que eu já tenho sobre o meu projeto,

05:19

Tente fazer com que eu tenha esse documento baseado nesse template, e o que faltar de informação, me pergunte. Então, é um bom desafio para você conseguir pegar projetos ou pedaços de documentação que você tem,

05:35

e trazer isso pra esse PRD pedindo pra IA fazer isso pra você. Então, isso aí é uma baita forma de você simplificar e deixar essa entrevista mais, como se diz, mais leve e com não tantas perguntas, porque é bastante pergunta, porque realmente são pontos essenciais pro desenvolvimento dos nossos projetos. Beleza?

05:59

Galera, eu sei que é bastante conteúdo, sei também que é bastante teoria, mas eu queria muito realmente ter passado essa parte de PRD. Apesar de não ser um design doc, é um documento importante e se você não quiser trabalhar dessa forma,

06:16

Você pode simplificar, mas saiba que se a IA tiver acesso a essas informações, você pode ter certeza que ela não vai sair criando código e fazendo coisas aleatórias que não deveriam ser feitas, uma vez que ela sabe o que tem no escopo e o que não tem no escopo. Isso vai ajudar bastante aí para você. Beleza? Então, galera, acabamos de falar sobre PRDs e...

06:41

Em seguida, a gente vai iniciar, finalmente, o mundo dos design docs e eu quero gerar uma clareza bem grande para você quando, como e o que você deve gerar para determinados tipos de projetos. Vamos nessa!

## Resumo IA

**Abreviações**

- **IA** — Inteligência Artificial
- **PRD** — Product Requirements Document
- **P95** — 95º percentil

**Resumo**

A aula apresentou um prompt de entrevista para geração de PRD de features com apoio de IA, mudando o fluxo tradicional de “pedir para escrever” para um processo guiado de perguntas e validação. Em vez de produzir o documento diretamente, a IA entrevista o usuário, coleta contexto de forma progressiva, confirma entendimento e só então consolida a saída final. O objetivo é reduzir lacunas de informação, evitar respostas vagas e aumentar a confiabilidade da documentação.

O instrutor explicou que o prompt pode ser usado em qualquer IA conversacional ou encapsulado em um assistente, como um MyGPT, para manter papel, regras, formato e restrições persistentes entre sessões. O fluxo operacional consiste em colar o prompt, iniciar a entrevista com um comando do tipo “comece a fazer a entrevista comigo” e responder etapa por etapa. Quando houver documentação prévia do projeto, ela deve ser anexada no início para diminuir o número de perguntas e permitir que a IA preencha apenas as lacunas.

Foi detalhado que a IA precisa seguir regras explícitas de coleta: não fazer perguntas duplas, não inventar detalhes técnicos, resumir o que entendeu, pedir confirmação antes de avançar e sugerir formulações quando o usuário ainda não tiver clareza. A entrevista segue uma sequência fixa de blocos: contexto e visão, problema ou oportunidade, objetivos, métricas de sucesso, escopo, requisitos funcionais e não funcionais, arquitetura ou abordagem, decisões, trade-offs, dependências, riscos e mitigação. Cada etapa alimenta uma estrutura de PRD já definida, funcionando como um esqueleto de pensamento que garante ordem e previsibilidade no documento final.

Durante a coleta, a IA armazena internamente as respostas em um JSON, sem exibir essa estrutura ao usuário. Isso organiza os dados por chave, evita perda de contexto ao longo da conversa e facilita a geração posterior do documento. Antes de finalizar, a IA deve revisar consistência, checar campos ausentes e identificar ambiguidades, interrompendo a geração se algo estiver contraditório ou insuficiente. O resultado principal é um PRD em português renderizado em Markdown, e depois disso a IA pergunta se o usuário também deseja a exportação em JSON, com chaves em inglês e sem campos vazios.

O instrutor também destacou o uso de defaults inteligentes, isto é, sugestões dadas pela IA quando o usuário não souber responder um campo específico, como uma meta inicial de latência P95 menor que 150 ms. Esses defaults ajudam a destravar a entrevista, mas precisam ser apresentados como sugestões revisáveis, para não virarem requisitos assumidos sem validação. Por fim, foi reforçado que o prompt é um artefato ajustável: ele deve ser refinado conforme o tipo de produto, o nível de detalhe desejado e a documentação disponível, inclusive reutilizando materiais já existentes para acelerar a criação do PRD.

**Pontos de atenção**

- Não tratar o prompt como “gerador automático” de texto; ele deve conduzir uma entrevista estruturada.
- Evitar perguntas duplas, porque elas prejudicam clareza e qualidade da resposta.
- Não inventar detalhes técnicos quando o usuário não souber informar.
- Sempre resumir o entendimento da IA antes de avançar para a próxima etapa.
- Pedir confirmação do usuário em cada bloco importante da entrevista.
- Usar sugestões/defaults apenas como ponto de partida, deixando claro que são revisáveis.
- Não deixar o JSON aparecer durante a coleta; ele deve ser apenas estrutura interna.
- Antes de gerar o PRD final, checar inconsistências, lacunas e ambiguidades.
- Garantir que objetivos, escopo, requisitos e métricas estejam coerentes entre si.
- Manter o template em Markdown estável para favorecer revisão humana e comparação entre features.
- Exportar JSON apenas quando fizer sentido, já que Markdown é melhor para leitura e revisão.
- Aproveitar documentação prévia do projeto para reduzir perguntas e acelerar a entrevista.
- Ajustar regras e perguntas do prompt quando alguma seção gerar ruído recorrente, em vez de corrigir apenas o documento final.