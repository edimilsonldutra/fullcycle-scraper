Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16725)

## Resumo da aula

Prompts de aplicação deixam de ser texto solto quando passam a existir em um registry. Esse registry funciona como o índice central da aplicação: ele lista quais prompts existem, quais versões estão disponíveis, qual está em produção e quais metadados acompanham cada item. O armazenamento pode ficar em arquivos ou banco de dados; o ponto essencial é ter uma fonte explícita de consulta e governança. Essa camada será a base para registrar, localizar e carregar prompts de forma previsível nas implementações seguintes.

Retomando a ideia de que prompts de aplicação compõem o comportamento do sistema, a organização deles precisa seguir a arquitetura do próprio software. A categorização pode ser por agentes, por use cases como payment, por componentes, por subdomínios em Domain Driven Design ou por feature. Não existe taxonomia universal; existe uma exigência de coerência estrutural. A categoria importa porque ela define como o software encontra e referencia cada prompt durante a execução.

Semantic versioning em prompts usa a mesma lógica de major.minor.patch, mas agora aplicada a mudanças comportamentais do sistema orientado por IA. Uma alteração patch tende a corrigir detalhe sem mudar a intenção central; uma minor adiciona ou ajusta comportamento de forma compatível; uma major sinaliza ruptura relevante no contrato esperado. Essa distinção melhora rastreabilidade operacional e reduz ambiguidade ao promover versões entre ambientes. Nas próximas implementações, esse versionamento será associado ao registro e ao carregamento dos prompts.

prompt.md favorece leitura humana e edição livre, o que funciona bem quando a estrutura não precisa ser rigidamente interpretada por ferramentas. O problema é que Markdown não impõe um esquema consistente, então campos importantes podem aparecer de formas diferentes entre prompts. prompt.yml introduz estrutura explícita, o que facilita validação, automação e integração com convenções usadas em ecossistemas como LangChain e LangSmith. A escolha não é entre legível e ilegível, mas entre flexibilidade textual e padronização operacional.

Metadados transformam o prompt em um artefato inspecionável pela aplicação e pela equipe. Campos como entradas esperadas, saída pretendida, versão, modelo utilizado e descrição permitem entender como o prompt deve ser executado e em que contexto ele faz sentido. Isso reduz uso incorreto e melhora manutenção, porque o comportamento esperado deixa de depender apenas da leitura do texto principal. Em formatos estruturados, esses dados também podem ser consumidos por testes, loaders e ferramentas de observabilidade.

Teste de compilação verifica se o prompt está estruturalmente válido para execução, não se sua resposta é boa. O foco é garantir, por exemplo, que todas as inputs declaradas realmente aparecem no template e que não existem placeholders ausentes, extras ou inconsistentes. Se o prompt declara name como entrada e o template não usa name, há falha estrutural antes mesmo de qualquer julgamento de qualidade. Esse tipo de teste será usado depois como parte da automação básica de segurança para prompts versionados.

Evaluation mede qualidade, adequação ou desempenho do comportamento gerado; teste estrutural apenas verifica se o prompt compila corretamente dentro do contrato definido. Confundir os dois leva a lacunas perigosas: um prompt pode ter boa avaliação qualitativa e ainda assim quebrar em produção por erro de variável, e um prompt estruturalmente válido pode continuar ruim do ponto de vista funcional. Por isso, compilação e evaluation são camadas complementares, não substitutas. A primeira protege integridade operacional; a segunda analisa resultado.

README e changelog já fazem parte da governança de prompts, mas aqui ganham peso operacional maior porque o artefato afeta diretamente produção. O README deve registrar onde o prompt é usado e qual contexto ele atende, enquanto o changelog ajuda a rastrear mudanças relevantes sem depender apenas do diff bruto. Essa documentação encurta diagnóstico quando uma regressão aparece após troca de versão. Em prompts críticos, contexto e histórico deixam de ser conveniência e passam a ser mecanismo de manutenção.

## Transcrição

00:01

Bom, pessoal, e agora eu quero trazer aqui para você a outra perspectiva que é muito importante, que é quando a gente está utilizando prompts para desenvolvimento de aplicações e agentes. O que eu estou querendo dizer com isso agora não é prompt para me deixar mais produtivo e para fazer codificação. São prompts que as aplicações que você vai desenvolver, os seus agentes que você vai desenvolver,

00:31

vão possuir, tá? E esses prompts, eles são ultra críticos, tá? E por que eles são ultra críticos? Porque esses prompts, eles mudam o comportamento do sistema que vai para a produção. É um pouco diferente de um workflow de desenvolvimento de um prompt que você está desenvolvendo, que se der algum erro na hora que você está programando, você pode dar um stop, pode entender e tudo mais. Agora, na hora que você está utilizando prompts,

00:59

que vão para o ar, para um sistema, para uma I.A. consumir e rodar ali em produção, aí o buraco é mais embaixo. E, nesse momento, eu quero que você entenda o racional, e eu prometo agora que eu não vou ficar só falando, a gente vai ver também código com exemplos e etc. de como você consegue se organizar. Mas, basicamente, é o seguinte, a gente precisa de um

01:27

registro, um registry, ou seja, ele contém todos os prompts e as suas versões que vão ser utilizadas. Então, basicamente, o que vai acontecer aqui, eu vou ter esse registry, esse registro aqui para mim, e nesse camarada registry, basicamente, o que esse cara faz? Ele é um índice. É um índice.

01:57

E esse índice aqui vai conter, de forma geral, todos os prompts da sua aplicação. E lembrando, isso é uma abordagem que eu quero trazer aqui para vocês, que é uma abordagem que eu vejo que faz muito sentido e que está sendo muito utilizado nos dias de hoje. Somente para você entender, nesse caso também, os arquivos de prompt.

02:24

que você vai utilizar, eles podem estar na realidade, inclusive, dentro do seu próprio controle de versão, dentro do seu próprio projeto. O ponto é que existe uma flexibilização que você pode ter na hora de utilizar prompts por outras áreas que vão gerenciar sua aplicação. Eu vou falar com vocês sobre isso daqui a pouco, tá? Então,

02:50

Uma vez que você tem esse registro, tá? Esse índice de prompts dentro da sua aplicação, e aí você pode gerenciar da forma como você quiser, você pode gerenciar por um banco de dados, por arquivos, etc. Mas o importante é que você tenha esse índice aqui. Esse índice, ele vai trazer o prompt, a versão, se ele está em produção, você pode ter metadados, você pode colocar qual o modelo que esse cara vai utilizar, tá? Outro ponto, que é um dos pontos mais importantes aí nesse caso, é

03:19

Como que eu vou organizar esses prompts dentro do meu projeto? Eu também preciso categorizar esses prompts. E na hora que eu vou categorizar esses prompts, a coisa não é tão simples, porque isso vai depender muito do projeto que você está. Então, deixa eu dar um exemplo aqui. Eu posso ter, por exemplo, uma parte só de agentes. Então, eu tenho um agente que tem um prompt, ou que tem mais de um prompt. Então, eu posso criar uma pasta do meu agente barra

03:49

o nome do prompt que eu quero trabalhar e etc. Mas, às vezes, eu não quero trabalhar com agentes. Às vezes, a minha aplicação nem tem agentes. Então, vamos imaginar que eu tenho um use case. Então, vamos dizer que eu tenho um payment. Então, eu tenho use case para realizar um pagamento. Então, esse cara aqui vai ter o prompt especializado somente

04:11

para que a IA injete esse prompt dentro da sua aplicação. Ah, não! Eu não vou trabalhar com casos de uso. Eu tenho diversos componentes na minha aplicação e cada componente, nesse caso, tem um prompt específico. Ou pode ser utilizado para trabalhar com subdomínios. Você está trabalhando com Domain Driven Design. Então, não interessa como você quer utilizar. Você pode trabalhar com Domain Driven Design, você pode trabalhar ali por feature,

04:42

Você pode categorizar da forma que você quiser, mas o importante é que essa categorização tenha uma lógica, porque é a partir dela que você vai fazer todas essas chamadas dentro do seu software. Então, isso tem que ficar muito claro ali para você.

05:02

Outra coisa extremamente importante é você utilizar semantical versioning. Ou seja, esses prompts precisam estar muito bem versionados. Então, basicamente, v1.1.0. Então, aqui eu tenho meus patches, as minhas minors e majors. Então, vamos lembrar sempre aqui de semantical versioning. Se você não conhece semantical versioning, recomendo que você estude

05:32

porque é extremamente importante e você pode trabalhar com isso dentro do seu próprio prompt. Então, esses prompts que você vai precisar, ele vai ter um versionamento SIM. Outra coisa que você vai precisar é ter o seu arquivo do seu prompt. E aí, as coisas começam a mudar um pouco de figura, porque o arquivo do meu prompt pode ser o meu prompt.md,

05:58

que é muito comum de você ver sendo utilizado nos dias de hoje, e é uma das coisas que a gente mais faz. Por outro lado, muitas vezes que a gente olha esse arquivo Markdown, esses arquivos MD, eles são arquivos que facilitam a nossa leitura, que ajudam a gente pra caramba, mas que não necessariamente possuem um padrão.

06:19

E uma coisa extremamente importante quando a gente está desenvolvendo uma aplicação, o que é? É padronização. Então, nem sempre você deve ou que você não deveria trabalhar com o AMD, mas o que eu estou querendo dizer é que existem formas que são mais estruturadas que podem te ajudar. E aí, nesse caso, a gente tem prompt.yml. Ou seja, você pode trabalhar com o ymlfiles

06:46

pra facilitar, inclusive, a gestão desse prompt. E eu vou mostrar isso pra você na prática daqui a pouco, tá? E uma das coisas interessantes é que trabalhar com o YAML ajuda bastante você a seguir algumas convenções que, por exemplo, o próprio pessoal da LangChain, do LangSmith, pra parte de observabilidade, faz na hora de fazer o gerenciamento dos prompts, tá? Então,

07:13

Lembrando, se você precisa de algo mais estruturado, recomendo que você, sim, trabalhe com YAML. Ah, eu não tenho tanta essa necessidade de estruturação e etc. Trabalhe com Markdown e vai dar bom também ali para você, tá? Mas o importante é que você saiba que vai ter que ter o seu arquivo de prompt.

07:30

Uma outra coisa interessante nesse caso é que você vai precisar de metadados. E esses metadados são muito importantes. Por que eu estou dizendo isso? Porque esses metadados normalmente vão definir para você coisas como o que eu vou ter de entrada, o que eu pretendo ter de saída, como eu posso testar esse prompt, qual é a versão desse prompt,

08:00

Qual é o modelo que ele utilizou? Qual é uma descrição desse prompt? Ou seja, eu posso ter muitas informações que vão me ajudar a organizar esses meus prompts. E por isso que, às vezes, trabalhar com o YAML ajuda bastante, mas, de forma geral, se você trabalhar também com o Markdown,

08:25

vai te ajudar, mas essas informações não vão ficar necessariamente legais, às vezes, dentro do Markdown. Pode gerar um pouco uma confusão em relação a esses metadados, tá? Mas, de forma geral, aí vai muito de você, de como você quer estruturar o seu software, tá?

08:47

Há um outro ponto aqui que é extremamente importante, tá? E aqui eu acho que é o ponto mais importante, inclusive. São casos de teste para validar a compilação do prompt, tá? E quando eu estou falando aqui para você em casos de teste para validar a compilação do prompt, eu não estou falando em evaluation. Eu não estou falando para medir a qualidade do meu prompt, ou seja, para dizer se o meu prompt é bom ou se ele é ruim. Eu estou realmente querendo garantir que

09:17

esse meu prompt, ele realmente consiga passar na compilação. E o que pode ser passar na compilação? Para garantir que todas as inputs que eu estou passando, elas estão sendo utilizadas dentro do meu prompt. Então, vamos imaginar que eu estou falando que eu preciso de uma input como um name, e daí quando eu vou dentro do meu prompt, não existe o campo name.

09:44

Então, ou eu coloquei um campo que não precisava, ou eu esqueci de colocar algo. Lembrando, prompt é software, e eles precisam de testes automatizados. E dá pra fazer, e eu vou mostrar isso na prática, inclusive, aí pra você. E outra coisa que eu vou sempre recomendar, mais do que nunca, inclusive, é um readme.md.

10:07

trazendo o contexto do prompt, aonde ele é utilizado e um changelog também para te ajudar, caso você queira manter o rastro de tudo isso aí. Mas, novamente, galera, o nível de responsabilidade que a gente tem com esses tipos de prompts que eu estou te falando é muito maior que o nível de responsabilidade dos prompts que a gente usa no dia a dia,

10:28

para a produtividade, porque aqui o negócio pode realmente dar ruim, tá? Então, no próximo vídeo, eu sei que esse vídeo ficou grande, a gente vai navegar um pouco sobre esse mundo aqui em relação a trabalhar com esses prompts, tá? Então, vamos nessa!

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **YAML / YML** — *YAML Ain’t Markup Language* (formato de serialização de dados legível por humanos)
- **README** — arquivo de documentação introdutória do projeto
- **ChangeLog** — registro histórico de alterações
- **DD / DDD** — *Domain Driven Design* (Projeto Guiado pelo Domínio)

**Resumo**
A aula apresenta uma abordagem para tratar prompts usados por aplicações e agentes como artefatos críticos de software, e não como texto solto. O instrutor explica que, quando esses prompts passam a influenciar o comportamento do sistema em produção, é necessário organizar tudo em um registry central, que funciona como um índice de consulta contendo os prompts disponíveis, suas versões, o status de produção e metadados relevantes. Esse registro pode ser mantido em arquivos ou banco de dados, desde que exista uma fonte explícita de governança e carregamento previsível.

Em seguida, é discutida a forma de categorizar os prompts de acordo com a arquitetura do sistema. A organização pode seguir agentes, casos de uso, componentes, subdomínios em DDD ou features, desde que a taxonomia seja coerente com a estrutura do software e com a forma como os prompts serão referenciados em execução. O instrutor também aborda versionamento semântico para prompts, usando a lógica de major, minor e patch para indicar mudanças compatíveis, incrementais ou rupturas de contrato comportamental.

A aula compara arquivos em Markdown e YAML para armazenar prompts. O Markdown é valorizado pela legibilidade e flexibilidade, mas não impõe estrutura rígida; já o YAML é destacado por permitir padronização, validação e automação, além de se alinhar melhor a ecossistemas como LangChain e LangSmith. Também são apresentados os metadados como parte essencial do artefato, incluindo entradas esperadas, saída pretendida, versão, modelo e descrição, tornando o prompt inspecionável e mais fácil de manter.

Por fim, o instrutor diferencia teste de compilação de evaluation. O teste de compilação verifica se o prompt está estruturalmente válido — por exemplo, se todas as variáveis declaradas existem no template e se não há placeholders inconsistentes — enquanto evaluation mede a qualidade do comportamento gerado. A aula fecha reforçando a importância de README e changelog para documentação e rastreabilidade, especialmente porque prompts de aplicação e agentes têm impacto direto em produção.

**Pontos de atenção**
- Prompts de aplicação e agentes são artefatos críticos: erros neles podem afetar diretamente a produção.
- É essencial manter um **registry** central para consulta, governança e carregamento previsível dos prompts.
- O armazenamento pode ser em arquivos ou banco de dados, mas a existência de uma fonte explícita e organizada é o ponto-chave.
- A categorização dos prompts deve seguir uma lógica coerente com a arquitetura do software; não existe taxonomia universal.
- O versionamento semântico deve ser aplicado aos prompts para facilitar rastreabilidade e controle de mudanças.
- **Markdown** é legível, mas pouco rígido; pode gerar inconsistência de estrutura entre prompts.
- **YAML** favorece padronização, validação e automação, sendo mais indicado quando há necessidade de estrutura formal.
- Metadados são fundamentais para reduzir uso incorreto, facilitar manutenção e apoiar testes, loaders e observabilidade.
- Teste de compilação não é o mesmo que evaluation: um prompt pode compilar e ainda ser ruim, ou pode ter boa qualidade e falhar estruturalmente.
- Verificar se todas as entradas declaradas realmente são usadas no template evita erros de variável e falhas em produção.
- README deve registrar contexto e local de uso do prompt; changelog ajuda a rastrear mudanças e investigar regressões.
- Em prompts críticos, documentação e histórico deixam de ser conveniência e passam a ser parte da manutenção operacional.