Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16620)

## Resumo da aula

Um agente auditor de dependências é um prompt operacional especializado em inspecionar manifests e lockfiles de um projeto sem alterar a codebase. Retomando a estrutura já definida anteriormente, a novidade aqui é transformar persona, escopo e objetivo em um artefato executável com limites explícitos: analisar, reportar e nunca modificar. Isso reduz a chance de o agente extrapolar para upgrades, edições ou recomendações fora do escopo técnico pedido.

O objetivo deixa de ser uma frase genérica e vira uma lista operacional de verificações: dependências desatualizadas, depreciadas, legacy, sem manutenção recente, com risco de licença, com vulnerabilidades conhecidas e com impacto de manutenção. Esse detalhamento importa porque o modelo responde melhor quando cada critério de sucesso já está explicitado. A dificuldade de escrever um bom prompt costuma estar menos na sintaxe e mais na clareza do que realmente se quer auditar.

Os inputs principais são os arquivos que representam o estado declarativo das dependências, como package.json, package-lock.json, pnpm-lock.yaml, yarn.lock, requirements.txt e equivalentes de outros ecossistemas. O agente também pode inferir linguagem, framework e tooling do repositório, além de aceitar instruções opcionais do usuário, como priorizar segurança ou licenciamento. Se nenhum arquivo relevante for encontrado, o comportamento correto não é improvisar: é declarar a limitação e pedir confirmação para continuar com contexto incompleto.

O output em Markdown funciona como contrato de entrega: define seções fixas, ordem de apresentação e granularidade do relatório. Em vez de pedir “um relatório de auditoria”, o prompt especifica blocos como summary, critical issues, tabela de dependências, análise de risco, dependências não verificadas, arquivos críticos, notas de integração e plano de ação. Essa estrutura melhora legibilidade, facilita salvar o resultado em arquivo e torna a resposta mais comparável entre execuções.

Skeleton of thoughts é a especificação explícita do esqueleto da resposta antes da geração do conteúdo detalhado. Em vez de deixar o modelo decidir sozinho como organizar o raciocínio, o prompt impõe uma sequência de seções e exemplos de colunas, como versão atual, última versão e status outdated. O efeito prático é reduzir ambiguidade estrutural sem exigir que o modelo exponha cadeia de pensamento interna.

Quando o prompt mostra exemplos concretos de linhas de tabela, como Express, Lodash ou LangChain com versão atual e status, ele não está ensinando o domínio ao agente; está calibrando o formato esperado. Isso evita respostas vagas do tipo “algumas dependências estão desatualizadas” e força uma saída verificável. O mesmo vale para seções condicionais, como a lista de dependências não verificadas, que só deve aparecer quando houver casos reais.

Dependências diretas são as declaradas explicitamente pelo projeto; dependências transitivas são trazidas indiretamente por outras bibliotecas. Separar essas duas categorias é essencial porque uma auditoria completa da árvore pode explodir em volume e desviar o foco do relatório principal. Neste caso, o critério operacional é auditar apenas as diretas, deixando claro que a exclusão das transitivas é uma decisão de escopo, não uma negação de relevância.

Os critérios controlam como o agente deve executar a análise: identificar package managers, comparar versões com a última estável, sinalizar pacotes depreciados, verificar manutenção, licenças, vulnerabilidades, breaking changes e single points of failure. Retomando os critérios já vistos anteriormente, a camada nova aqui é o nível de operacionalização: cada regra orienta a produção do relatório e a classificação de risco em critical, high, medium e low. Sem esse bloco, o formato pode até sair correto, mas o conteúdo tende a ser inconsistente.

MCP servers entram como fontes auxiliares para validação externa de versões, manutenção e vulnerabilidades. Ferramentas como Context7 e Firecrawl ampliam a capacidade do agente de consultar documentação e páginas relevantes, mas o prompt não deve acoplar a execução a um único servidor específico se outros equivalentes puderem cumprir a mesma função. A instrução correta é condicional: usar MCP quando disponível e, quando não estiver acessível, declarar a limitação e continuar com base apenas nos arquivos locais.

CVE, sigla para Common Vulnerabilities and Exposures, é um identificador único para vulnerabilidades publicamente conhecidas. Em uma auditoria de dependências, citar o ID do CVE transforma uma alegação genérica de risco em uma referência rastreável por ferramentas e equipes de segurança. Isso também explica por que o prompt proíbe inventar CVEs: um identificador falso compromete a confiabilidade inteira do relatório.

Assumptions são regras de decisão antecipadas para cenários ambíguos, como múltiplos ecossistemas no mesmo diretório, ausência de versão, falta de lockfile ou execução em monorepo. Em vez de deixar o agente escolher arbitrariamente, o prompt define como ele deve separar auditorias, registrar nível de confiança e decidir entre pasta específica ou projeto inteiro. Esse bloco não elimina incerteza; ele a torna explícita e controlada.

As instruções negativas já conhecidas ganham aqui um papel de contenção operacional: não editar a codebase, não executar upgrades, não assumir vulnerabilidades, não usar linguagem vaga, não inserir emojis e não estimar tempo de correção. Cada proibição remove um comportamento comum de modelos generalistas que seria inadequado em um relatório técnico. O resultado é um agente mais previsível e menos propenso a preencher lacunas com opinião ou decoração textual.

Tratamento de erro em prompt operacional significa definir como o agente falha, não apenas como ele acerta. Se faltarem manifests, permissões de leitura ou acesso a fontes externas, a resposta deve vir em formato estruturado com status, reason e próximos passos objetivos, como informar caminho de arquivos ou liberar acesso ao workspace. Isso transforma falha em estado observável do workflow, em vez de produzir uma resposta confusa ou parcialmente inventada.

Um workflow resumido no final do prompt funciona como checklist de execução: detectar projeto e stack, inventariar dependências, comparar versões, sinalizar riscos, verificar licenças, identificar arquivos críticos e consolidar o relatório. Mesmo que essas etapas já estejam implícitas nos blocos anteriores, escrevê-las em sequência ajuda o agente a seguir uma ordem estável. O prompt deixa de ser apenas uma descrição de requisitos e passa a operar como especificação de processo.

Quando o agente roda em ambientes como CLI, o relatório pode aparecer apenas na saída do terminal, o que dificulta leitura e compartilhamento. Por isso, o prompt pode incluir um passo final: se o usuário não informar caminho de saída, o agente deve perguntar onde salvar o arquivo Markdown. Essa pequena regra conecta a análise técnica ao uso real do artefato gerado.

## Transcrição

00:01

Bom pessoal, como eu falei pra vocês no vídeo anterior, agora vamos colocar um pouco mais a mão na massa e entender esse tipo de estrutura em um prompt mais vida real, que você pode sair inclusive utilizando. Então eu vou fazer isso aqui, deixar eu aqui no meu Notion, onde eu tenho esse meu prompt.

00:20

e você vai conseguir, inclusive, ter acesso a isso aqui que eu criei. Então, seguinte, a nossa ideia aqui é nós termos um agente que faz auditoria de dependências em um projeto. Esse prompt aqui está escrito em inglês, mas, de forma geral, você vai perceber que nós temos exatamente a estrutura que eu passei para vocês.

00:48

Então, o que a gente está colocando aqui para que a gente consiga entender em relação a essa estrutura? Primeiro passo, persona e escopo, ou seja, a especialidade que o agente tem, quem é esse agente, e, no final das contas, o escopo, ou seja, até onde ele vai. Então, qual é a ideia principal? Então, nesse nosso caso aqui, eu estou falando que ele é um senior software engineer,

01:13

e também esse expert em gerenciamento de dependências, com uma expertise gigante em analisar projetos de software e dependências entre múltiplas linguagens de programação. Agora, o ponto importante que eu estou colocando aqui é, o seu papel é estritamente analisar e fazer um report, você nunca deve modificar nenhum

01:36

projeto, ou fazer inclusive upgrades, ou propostas de upgrades, ou alterar o meu code base em nenhuma etapa. Então, aqui a gente já passa pelaquela nossa primeira estrutura que a gente acabou falando. Segundo ponto aqui,

01:53

muito claro. E perceba, pessoal, eu sempre tento ser o mais pontual possível pra evitar qualquer tipo de alucinação ou evitar com que a Iá ela tente fazer mais ou menos do que eu pedir. Isso é garantido? Não é garantido.

02:09

mas você vai perceber que conforme você testa esses tipos de prompt, você vai perceber que você minimiza bastante esses riscos. Então, qual é o objetivo dele aqui? Bem claro. Performar, fazer uma auditoria completa de dependências que identifique

02:32

dependências depreciadas, desatualizadas, bibliotecas que estão em formato de legacy, ou seja, que vão ser descontinuadas, verificar, inclusive, vulnerabilidade no banco de dados de vulnerabilidade desconhecido, fazer uma flag de bibliotecas que não estão mais sendo mantidas por mais de um ano, eu coloquei aqui,

02:55

a fazer a verificação das compatibilidades de licenças e riscos legais que eu possa ter, e também aqui fazer um highlight de pontos de falha para manutenção que pode causar um grande problema no projeto, e também prover uma forma estruturada de recomendações sem ter que fazer nenhuma modificação no código. Então, se você perceber aqui, eu estou trazendo qual é o objetivo muito claro aqui do agente, tá?

03:24

Então, somente de ler isso, até pra mim fica mais claro o que eu tô querendo. E uma dica que eu já dou aqui pra você é o seguinte, fazer esses bullet points que eu acabei de colocar aqui pra você não é fácil. Por que eu tô dizendo isso? Porque, normalmente, a gente quer pedir as coisas pra IA, mas a gente mesmo não tem uma clareza tão grande. Então, o grande problema, muitas vezes,

03:49

A dificuldade que a gente tem em construir um prompt, um bom prompt, é ter essa clareza. Então, por isso, criar prompts que realmente funcionem também dá trabalho por conta disso. Agora, vamos falar sobre inputs. Lembra que a gente tem entrada e saída e tudo mais? Então, a input aqui é o seguinte.

04:08

a gente vai passar para ele, no final das contas. Arquivos de dependências e arquivos lock, onde tem aquela lista realmente das dependências, como package.json, package.lock, pnp, yarn, requirements.txt,

04:25

estou passando coisas do Rust aqui, do Go e etc. Então, se você perceber aqui, as inputs podem ser os arquivos de dependência, porque para mim são importantes, porque normalmente o projeto tem a lista de dependência nesses arquivos. Outra coisa como input é

04:43

a detectar, nesse caso aqui, a linguagem framework e as ferramentas do repositório. O que mais que ele tem de input? Instruções opcionais do usuário, como focar em segurança, licenciamento, especificação e ecossistema. E se nenhum arquivo de dependência for detectado,

05:06

falar explicitamente e pedir explicitamente qual é o caminho para confirmar se ele deve proceder ou não com informações limitadas. Então, se você perceber aqui nesse meu input, a minha input, no final das contas, são os arquivos do meu projeto.

05:25

Mas eu quis detalhar um pouco mais pra quê? Pra que ele tenha um foco maior nos arquivos que fazem, que tem normalmente o manifesto das nossas dependências ali de forma geral. Muitas vezes o usuário na input vai querer passar esse prompt, mas às vezes pedir algo adicional. Então, por isso que...

05:48

eu tenho uma parte que é opcional ali em relação, baseado as instruções do usuário, e também se eu não passar informação suficiente, ele pode ter a liberdade de perguntar para mim e ver se é o suficiente para ele conseguir fazer essa auditoria, tá? Agora, o ponto aqui está nessa parte de output format, tá? Então, aqui é uma outra coisa que é muito

06:12

complexo, novamente, se você não tem clareza do que você quer. Então, nesse caso aqui, eu estou dando aqui para ele como output o seguinte, retorne um markdown, um report de markdown, nomeado como dependence audit report com as seguintes seções. E agora que a coisa

06:33

traz para a gente uma clareza, por exemplo, de um tree of thoughts, que, no final das contas, eu estou especificando exatamente um esqueleto, um skeleton of thoughts, um esqueleto claro do que eu quero e como eu quero. Então, summary, ou sumário, ou seja, dá uma visão de high level do projeto, as dependências e os principais achados, vamos dizer assim.

07:02

Trazer também, em segundo ponto, critical issues, ou seja, vulnerabilidade de segurança, bibliotecas depreciadas, legacy e dependências core do sistema. Trazer a lista de uma tabela de dependências para a gente com as versões atuais e os status, por exemplo, o express na versão tal, a última versão é tal, então falar que ele está outdated.

07:26

A LOWDASH, a mesma coisa, a LANGCHAIN e etc. Então, se você perceber, aqui o que eu estou querendo trazer para ele é, nesse caso, um exemplo. Porque se eu falo, trago uma tabela de dependências e mostrar o que está depreciado ou não,

07:42

fica muito mais difícil e muito mais ambíguo para que a Yala consiga entender. Então, nesse nosso caso aqui, o que a gente está fazendo? Eu estou trazendo especificamente como eu quero. Mesma coisa, análise de risco. Traga os riscos presentes nessa estrutura. Então, eu estou colocando aqui o nível de criticidade, a dependência que eu estou dizendo, a isho que pode...

08:10

que está registrado no banco de dados, e os detalhes do que se trata esse tipo de problema. Ou um outro tipo de nível de risco é nível alto, por exemplo, manguzes depreciados. Então, aqui estou trazendo exemplos para a gente.

08:27

Uma outra coisa que pode acontecer é que, caso ele não consiga verificar problemas de dependências, a gente pode colocar uma sessão aqui para a gente saber o que ele não conseguiu identificar, porque daí eu posso buscar uma forma minha de tentar identificar esses casos.

08:46

Então, eu estou colocando aqui uma tabela de dependências que não foi possível verificar completamente, como versão, status ou vulnerabilidade. E aí que está o ponto. Eu coloquei aqui, importante, somente inclua essa sessão se

09:02

existirem dependências sem ser verificadas. Por que eu estou dizendo isso? Porque se eu não coloco uma observação dessa, provavelmente ele vai trazer essa sessão escrevendo, nenhuma dependência não foi conseguida fazer a verificação. Ou seja, então eu estou falando, só coloque isso aí caso ele encontre uma dependência. Beleza?

09:28

Outro ponto agora aqui, e aí vai mais algumas coisas interessantes. Critical file analysis. Então, estou colocando assim para ele. Identifique e analise os 10 arquivos mais críticos do projeto que tenham riscos de dependências. Ou ele pode ser depreciado, com vulnerabilidade, ou muito antigo, ou qualquer coisa desse tipo.

09:52

E eu coloquei, explique o porquê esse arquivo é crítico, qual que é o impacto no negócio, na integração do sistema, na dependência, na concentração dessa dependência. E eu coloquei aqui também para ele, porque às vezes você pode ter um comportamento ambíguo. Isso tinha acontecido quando eu fui testar esse prompt. Eu coloquei agora.

10:13

Always use the relative path to identify the files. Porque, às vezes, ele pegava o caminho completo do meu computador e eu não quero que isso fale. Aconteça. Então, eu falei para ele usar o meu caminho relativo. Perceba que quanto mais detalhe, melhor. Passo número 7. Notas de integração. Fazer um resumo de como cada dependência é usada no projeto. Um plano de ação. Criar recomendações para os próximos passos

10:40

Ah, sem mostrar, né, os esforços ou o tempo estimado. Por que que eu tô colocando dessa forma?

10:48

Grande parte das inteligências artificiais, quando eu peço pra ele fazer um report, uma lista de tarefa ou qualquer coisa desse tipo, eles têm uma mania de colocar o seguinte, olha, pra resolver esse problema é um dia, ou pra resolver esse problema, quatro horas de trabalho. Meu, eu não quero nada disso, não tem sentido nenhum, ainda mais se eu for resolver esse problema com o IA. Então, eu não sei de onde que ele tira.

11:12

esse tempo. E se eu realmente quisesse colocar esse tempo, eu teria que colocar no meu prompt como ele pode fazer o cálculo desse tempo. Nesse caso, eu estou explicitando para que ele não coloque esse tipo de coisa. E depois, o final step é

11:29

depois de você produzir o report completo, o relatório completo, se o usuário não colocou qual é o arquivo e o caminho desse arquivo, eu quero que ele explicitamente pergunte, você quer salvar esse report em algum lugar?

11:49

Se você quiser, traga aqui para mim o nome, o caminho e o nome do arquivo. Por quê? Porque muitas vezes, dependendo da inteligência artificial que você vai usar, ele vai gerar esse report na tela. Por exemplo, se você estiver com o Cloud Code, o Gemini ou alguma coisa desse tipo no CLI, ele vai trazer mais ou menos esse report no seu CLI e, às vezes, é muito ruim de ver. E, normalmente, esse report eu vou querer salvar comigo para eu mostrar para alguém ou para eu tomar alguma decisão.

12:19

Então, se eu, no momento que eu chamei esse agente ou utilizei esse prompt, eu não informar qual o arquivo que é para ele gerar esse report, eu quero que ele me pergunte. E agora, a gente tem os pontos aqui de critérios, somente para você lembrar aonde que a gente está. A gente está no output. Se você olhar aqui no nosso

12:41

documento inicial, a gente tem output, critérios, ambiguidade, instruções negativas, tratamentos de erro. Então, perceba que o nosso prompt, apesar de eu estar falando já faz um tempo aqui, a gente ainda está na parte de output, tá? Então, uma vez que acabou essa parte de output, a gente vai para critérios. E esses critérios aqui, eles são importantes pra caramba pra conseguir

13:10

fazer com que esse relatório seja gerado de acordo com o que eu estou esperando. Então, quais são os critérios que ele tem que pensar aqui? Identificar todos os package managers e os arquivos de dependência, porque se ele não fizer isso, no final das contas, fica mais difícil. Catalogar as dependências diretas somente, ou seja, nesse momento, ignorar as dependências transitivas. O que isso significa?

13:37

quando você tem uma dependência que depende de outra dependência que depende de outra dependência. Então, quando isso acontecer, eu estou pedindo para ele ignorar, porque senão a gente vai entrar numa árvore gigante de dependências, não que isso não seja importante, é, mas nesse report eu só quero saber minhas dependências diretas. E daí eu coloquei aqui ó, compare cada dependência contra a última versão estável dessa dependência apenas para...

14:05

reportar por que normalmente estou reforçando dessa forma, para garantir que ele não vai nem tentar fazer um upgrade. Faça um flag de dependências que estão depreciadas, considere pacotes que não estão sendo mantidos por mais de um ano,

14:21

verifique as vulnerabilidades que estão no banco de dados de vulnerabilidades, verifique a licença, categorize os riscos por critical, high, medium e low. Eu imagino que você deva ter visto naquela tabela e talvez tenha pensado, opa, mas ele não especificou quais são os tipos de criticidade. Então, aqui eu estou colocando os critérios para, na hora que ele gerar a tabela, eu escolher como que ele está querendo trabalhar.

14:48

Outra coisa, identifique os pontos de falha, os single points of failure, ou seja, dependências que geram impacto em múltiplas features do meu software. Coloquei aqui, faça um highlight e breaking changes que foram introduzidas nessas novas versões.

15:05

verifique a manutenção e o esforço de manutenção para manter essas dependências atualizadas. Quando estiver disponível, utilize MCP servers como um Context 7 ou um Firecrawl para validar as versões, as manutenções e as vulnerabilidades. Por quê? Porque esses MCPs têm acesso a documentações,

15:31

como o Context 7, e o Firecrawl, no final das contas, ele consegue fazer ali uma varredura, uma leitura das páginas de uma forma muito mais completa do que alguns outros caras que fazem web scrape, no final das contas. Mas você não é obrigado a usar o Firecrawl.

15:52

e somente se, por exemplo, o seu MCP estiver ativo. Mas perceba, eu estou falando para ele usar MCP Servers, e eu dei exemplos de MCP Servers, mas eu não estou falando necessariamente quais ele tem que usar, porque eu posso ter algum outro MCP Server que possa fazer a mesma coisa que um Content-7 da vida ou um Firecrawl aqui para a gente, tá? Outra coisa,

16:19

sempre traga para mim o número das versões, as identificações aqui de banco de dados, e também uma versão aqui completa dos próximos passos, focando sempre em sites mais claros do que você dá conselhos mais genéricos.

16:38

E se você não conseguir acessar pacotes externos, registros, MCP servers, bancos de dados de vulnerabilidades, mostre claramente essa limitação e trabalhe apenas com a informação que você tem nos arquivos de projeto. Então, eu quero que...

16:59

isso fique muito claro, mas que ele mostre pra gente que ele tem essa limitação. Então, aqui a gente está na parte de critérios, tá? Então, são critérios que eu quero que ele use pra ele conseguir gerar o report naquele formato que é o output que a gente passou, tá? E aqui a gente tem ambiguidades e pressupostos, né? Assumptions. Então, eu vou dar um exemplo aqui pra que ele parta do princípio

17:27

para evitar confusões. Então, por exemplo, se eu encontrar múltiplos ecossistemas que estão presentes, passa o audit deles separado

17:39

E fale isso explicitamente no resumo. Como assim? Imagina que eu estou em um projeto que está trabalhando com Python, em um outro projeto que está trabalhando com Go, e eles estão na mesma pasta onde eu estou rodando o agente. Então, ele tem que perceber que ele está em projetos diferentes. Ou, eventualmente, um projeto back-end ou um projeto front-end. Outra coisa, se tiver registros externos, bancos de dados onde você pode

18:07

Por exemplo, encontrar vulnerabilidades... Ah, e toda hora eu estou falando de banco de dados de vulnerabilidade, estou falando de CVE, somente para você saber e deixar claro, para evitar que... dar mais clareza para vocês. CVE significa Common Vulnerability Exposures.

18:27

Então, basicamente, são exposições de vulnerabilidades que são conhecidas e cada uma dessas vulnerabilidades vem com um tipo de código, onde vai falando qual é a vulnerabilidade e o código permite que a empresa e as ferramentas de segurança fiquem sabendo e utilizem um ID único para cada vulnerabilidade. Somente para deixar claro aqui para vocês.

18:54

Outra coisa, se alguma versão estiver faltando aqui, documente e coloque ali o seu nível de confiança em relação a isso. Se estiver faltando lockfiles, ou seja, aquele arquivo que trava a versão que você está trabalhando no projeto,

19:16

fale que você não tem, que o seu risco é maior para você reproduzir isso quando for para a produção. Aqui, se o usuário não especificar a pasta que ele quer auditar, faça o audit no projeto inteiro.

19:34

senão faça somente na pasta que ele pediu, tá? E o porquê que eu estou dizendo isso? Porque às vezes eu tenho várias pastas no meu projeto e eu quero validar somente um projeto, só um... Às vezes eu estou num monorepo, às vezes eu quero fazer uma... Auditar uma feature ou alguma coisa desse tipo. E agora a gente entra naquela outra parte, que é instruções negativas, né? Então, aqui ó, não modifique ou sugira edição no CodeBase. Não rode nenhum comando de upgrade, né? Não crie...

20:04

nenhum CVE ou assuma vulnerabilidades. Vai que a IA alucina e inventa um código como se isso fosse uma vulnerabilidade comum. Não use frases vagas como provavelmente seguro ou isso aqui deve estar ok. Não use emojis ou caracteres estilizados.

20:29

Galera, se tem algo que me irrita particularmente é a utilização de emojis em relatórios e coisas desse tipo. Então, eu sempre tento forçar para que ela não utilize. E eu vou ser honesto com você que, às vezes, mesmo assim, a IA acaba colocando, mas eu tento minimizar pra caramba isso.

20:46

Outra coisa, novamente, instruções negativas, e vale sempre apenas reforçar, não dê estimativa de tempo para resolver, como dias, horas, duração, ou em tantas horas, para fazer a resolução de fix e upgrade, para correção e fazer upgrade. Agora aqui a gente tem a parte de erro, e a parte de erro aqui eu estou colocando,

21:13

se ele não conseguir fazer auditoria, como não encontrou arquivos de dependência ou não conseguiu acessar os arquivos ou qualquer coisa desse tipo, responda no seguinte formato, status erro, razão, nenhum arquivo de dependência encontrado, D, uma instrução clara,

21:32

aonde e porquê isso aqui não foi performado. Isso gira também em próximos passos, por exemplo, dê o caminho onde estão as dependências, os arquivos de manifesto, dê permissão ao Workspace para ele poder ter leitura desses arquivos, confirme qual o ecossistema você está utilizando ou está querendo auditar. Então, aqui são formas que ele pode trazer de erro caso ele não consiga realmente fazer a tarefa.

21:57

a não ser que, provavelmente, esses tipos de erro podem acontecer se você tiver alguma falha de, como se diz, permissão que aí ela vai ter para ler os seus arquivos ou alguma coisa desse tipo, tá? E aqui, por último, pessoal,

22:14

eu gosto, às vezes, de reforçar quando eu quero ter um passo a passo do que a IA vai fazer. Apesar de eu ter passado passo a passo do que eu coloquei lá em cima, aqui eu estou fazendo um resumo, ou seja, o workflow que ele vai trabalhar.

22:31

Então, novamente, detectar o projeto, a tech stack, os package manager, fazer um inventário das dependências, comparar e declarar as versões, fazer o flag, detectar vulnerabilidades, verificar compatibilidade de licença, categorizar, identificar os arquivos, performar e etc. Então, basicamente, aqui é o workflow que eu estou dando passo a passo aqui para ele. Quando eu escrevo o workflow, para ele fica muito mais simples entender esse meu passo a passo,

23:00

de uma forma resumida. Então, normalmente, eu costumo fazer assim, e até mesmo para eu ler fica um pouco mais claro, tá? Então, se você perceber...

23:11

Esse é um prompt, não estou dizendo que é o melhor prompt possível e também não quero dizer que esse prompt vai funcionar 100% da melhor forma possível, porque provavelmente os resultados que esse prompt vai trazer usando uma I.A. num determinado tipo de code base ou uma I.A. com outro modelo ou coisas desse tipo, novamente a gente está falando sobre probabilidade.

23:36

mas um prompt desse, com certeza, ele já consegue trazer algo um pouco mais estruturado. Eu sei que esse vídeo ficou grande, mas no próximo vídeo eu vou trazer para você como que é o resultado desse prompt que ele trouxe aqui para mim. Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **MCP** — *Model Context Protocol*  
- **CVE** — *Common Vulnerabilities and Exposures*  
- **CLI** — *Command-Line Interface*  
- **IAs / IA** — Inteligências Artificiais  
- **Codebase** — Base de código  
- **Markdown** — Formato de texto leve para documentação  
- **Tree of Thoughts** — Estrutura de raciocínio em árvore  
- **Skeleton of Thoughts** — Esqueleto/estrutura da resposta antes da geração do conteúdo  

**Resumo**  
A aula apresentou, de forma prática, como estruturar um prompt operacional para criar um agente auditor de dependências em projetos de software. A ideia central foi transformar uma descrição genérica em um artefato executável, com persona, escopo, objetivo, inputs, formato de saída, critérios, pressupostos, instruções negativas, tratamento de erro e workflow bem definidos. O instrutor enfatizou que o agente deve atuar como um especialista em análise de dependências, mas com uma restrição explícita: somente inspecionar e reportar, sem modificar a codebase, sem executar upgrades e sem sugerir ações fora do escopo.

No bloco de objetivo, o prompt foi refinado para uma lista operacional de verificações, incluindo dependências desatualizadas, depreciadas, legacy, sem manutenção recente, com risco de licença, vulnerabilidades conhecidas e pontos de falha de manutenção. Em seguida, foram definidos os inputs do agente: manifests e lockfiles como package.json, package-lock, pnpm-lock.yaml, yarn.lock e requirements.txt, além da possibilidade de inferir linguagem, framework e tooling do repositório. O instrutor destacou que, se não houver arquivos relevantes, o comportamento correto é declarar a limitação e pedir confirmação ou mais contexto, em vez de improvisar.

A aula também detalhou o output esperado em Markdown, funcionando como contrato de entrega. Em vez de um relatório genérico, o prompt especifica seções fixas como summary, critical issues, tabela de dependências, análise de risco, dependências não verificadas, critical file analysis, notas de integração e plano de ação. Essa estrutura foi apresentada como um “skeleton of thoughts”, isto é, um esqueleto explícito da resposta, reduzindo ambiguidades e aumentando a consistência do relatório. O instrutor reforçou que exemplos concretos de linhas de tabela, como versões atuais, última versão estável e status de outdated, ajudam a calibrar o formato esperado sem deixar o modelo decidir a organização sozinho.

Outro ponto importante foi a separação entre dependências diretas e transitivas. O agente deve auditar apenas as diretas, para evitar a expansão da análise para uma árvore muito grande e manter o foco no relatório principal. Nos critérios, o prompt orienta identificar package managers, comparar versões com a última versão estável, sinalizar pacotes depreciados ou sem manutenção há mais de um ano, verificar vulnerabilidades em bancos de dados de vulnerabilidade, checar compatibilidade de licenças, classificar risco em critical, high, medium e low, identificar single points of failure e destacar breaking changes. Também foi explicada a possibilidade de usar MCP servers, como Context7 e Firecrawl, como fontes auxiliares para validar versões, documentação, manutenção e vulnerabilidades, sem prender o prompt a um único servidor específico.

Na parte de pressupostos e ambiguidades, o instrutor definiu regras para cenários incertos: separar auditorias quando houver múltiplos ecossistemas no mesmo diretório, registrar nível de confiança quando faltar versão ou lockfile e decidir entre auditar a pasta específica ou o projeto inteiro conforme a instrução do usuário. O termo CVE foi explicado como identificador único de vulnerabilidades conhecidas, importante para transformar risco genérico em referência rastreável. Já nas instruções negativas, o prompt proíbe editar a codebase, rodar upgrades, inventar CVEs, usar linguagem vaga, inserir emojis e estimar tempo de correção. Por fim, o tratamento de erro foi definido como parte essencial do workflow: quando faltar acesso, arquivos ou permissões, a resposta deve informar status, razão e próximos passos claros, como fornecer o caminho dos manifests ou liberar acesso ao workspace. O workflow final organiza a execução em etapas sequenciais, do reconhecimento do projeto até a consolidação do relatório, para tornar o processo mais previsível e fácil de seguir.

**Pontos de atenção**  
- Deixar explícito que o agente só analisa e reporta; não deve modificar a codebase nem propor upgrades.  
- Especificar os critérios de auditoria com bastante detalhe, para evitar respostas genéricas ou ambíguas.  
- Limitar o escopo às dependências diretas quando esse for o objetivo; transitive dependencies podem explodir o volume da análise.  
- Sempre definir os inputs esperados: manifests, lockfiles, linguagem, framework e instruções opcionais do usuário.  
- Se não houver arquivos relevantes, o agente deve declarar a limitação e pedir confirmação, em vez de inventar contexto.  
- Estruturar o output em Markdown com seções fixas melhora consistência, legibilidade e reaproveitamento do relatório.  
- Exemplos concretos de tabela ajudam o modelo a entender o formato esperado e reduzem saídas vagas.  
- Não deixar o agente inventar vulnerabilidades, CVEs ou recomendações sem base verificável.  
- Usar instruções condicionais para seções que só devem aparecer quando houver casos reais, como dependências não verificadas.  
- Definir regras para múltiplos ecossistemas, ausência de versão, falta de lockfile e execução em monorepo.  
- Sempre declarar o nível de confiança quando a informação estiver incompleta.  
- Proibir linguagem vaga, emojis e estimativas de tempo de correção para manter o relatório técnico e objetivo.  
- Quando possível, usar MCP servers para validação externa, mas sem depender obrigatoriamente de um servidor específico.  
- Em caso de erro, responder em formato estruturado com status, razão e próximos passos acionáveis.  
- Se o usuário não informar caminho de saída, perguntar onde salvar o relatório, especialmente em uso via CLI.  
- Reforçar no workflow a ordem de execução: detectar stack, inventariar dependências, comparar versões, classificar riscos e consolidar o relatório.