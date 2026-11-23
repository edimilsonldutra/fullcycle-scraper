Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16567)

## Resumo da aula

Prompt Engineering é a prática de projetar instruções para modelos de IA de forma deliberada, em vez de tratar prompt como texto improvisado. Isso importa porque, em aplicações reais, a forma de pedir altera diretamente a qualidade da resposta, a consistência do comportamento e a utilidade do sistema. Quando o prompt passa a ser pensado como artefato de engenharia, ele entra no mesmo espaço de decisão do código e da arquitetura. A consequência é clara: escrever bem deixa de ser suficiente; é preciso estruturar, justificar e manter.

Em software com IA, o prompt influencia a saída tanto quanto regras implementadas em código influenciam um fluxo tradicional. Por isso, a aplicação não depende apenas do modelo escolhido, mas também da forma como contexto, instruções e restrições são organizados. Retomando o cenário de aplicações corporativas com IA, o prompt deixa de ser entrada casual e passa a compor o comportamento observável do sistema. Isso afeta manutenção, previsibilidade e evolução do produto.

Tipos e técnicas de prompts são estruturas recorrentes usadas para induzir respostas mais adequadas ao objetivo do sistema. Muitas já aparecem no uso cotidiano de forma intuitiva, mas resultados confiáveis exigem entender por que cada técnica existe e em que condição ela funciona melhor. Sem essa intenção, o time tende a obter respostas inconsistentes ou difíceis de reproduzir. Esse repertório será a base para escolhas mais conscientes nas próximas explorações práticas.

Escrever prompt profissional não significa apenas escolher boas palavras, mas explicitar contexto, tarefa, formato esperado e critérios de qualidade. O valor está menos em “digitar melhor” e mais em compreender o mecanismo por trás da instrução e sua relação com o resultado produzido. Em desenvolvimento de software, isso permite transformar um exemplo isolado em padrão reutilizável. A escrita passa a servir à operação do sistema, não apenas à interação momentânea.

Prompts bem estruturados viabilizam a criação de agentes e assistentes capazes de apoiar fluxos de trabalho de engenharia e produtos internos. Um agente integrado a uma aplicação empresarial depende de instruções estáveis para agir de forma útil, enquanto um assistente de codificação precisa de prompts que orientem estilo, escopo e limites da resposta. A diferença entre um experimento interessante e um componente confiável costuma estar nessa estrutura. Por isso, projetar prompts é parte da construção desses sistemas, não um detalhe periférico.

Prompt precisa ser armazenado e versionado porque mudanças pequenas podem alterar significativamente o comportamento da aplicação. Em um sistema com IA, tratar prompt como ativo solto dificulta auditoria, rollback e comparação entre versões. A gestão adequada permite saber qual instrução estava em produção, por que ela foi alterada e qual efeito gerou. Isso aproxima prompts das práticas já consolidadas para código-fonte e configuração.

Ferramentas como LangSmith e PromptLayer ampliam a observabilidade do uso de prompts ao registrar execuções, respostas, custos e outros sinais operacionais. Esse tipo de visibilidade é essencial quando o sistema precisa ser acompanhado em produção e não apenas testado localmente. Em vez de depender de percepção subjetiva, a equipe passa a inspecionar como os prompts estão sendo usados e quais resultados estão produzindo. Observabilidade, nesse contexto, é o que torna possível operar IA com disciplina técnica.

Prompt também precisa ser testável. Avaliar vários prompts para a mesma tarefa, ou o mesmo prompt em modelos diferentes, permite comparar qualidade, aderência ao esperado e estabilidade do resultado. Isso é especialmente importante quando a aplicação precisa entregar respostas úteis de forma repetível, e não apenas impressionar em uma execução isolada. Testabilidade transforma escolha de prompt em processo comparável, e não em opinião.

A geração de documentação com IA ganha valor quando o time entende que existem múltiplos tipos de documentos, cada um adequado a um contexto de software. Design docs, diagramas e outras formas de documentação exigem prompts que orientem objetivo, profundidade e formato da saída. Sem essa clareza, a IA tende a produzir texto genérico; com instruções bem definidas, ela acelera a produção de artefatos úteis para comunicação e planejamento. O ganho real está em estruturar a demanda documental, não apenas em automatizar texto.

Manter exemplos de código e prompts em um repositório permite reproduzir experimentos, validar resultados e compartilhar referência comum entre pessoas do time. Essa prática reduz ambiguidade porque o comportamento discutido deixa de depender de memória ou de capturas soltas de tela. Quando exemplos ficam versionados no GitHub, torna-se mais fácil testar, adaptar e evoluir o que já funcionou. Reprodutibilidade é um requisito prático para aprender, comparar e operar prompts com consistência.

Prompt Engineering afeta diretamente custo, latência e previsibilidade da aplicação. Instruções mal desenhadas podem gerar respostas longas demais, execuções mais lentas ou saídas inconsistentes, elevando gasto operacional e reduzindo confiança no sistema. Retomando a ideia de que prompt compõe o comportamento do software, otimizar esse artefato é também otimizar operação. Qualidade de resposta, tempo de execução e produtividade do time passam a depender dessa engenharia.

## Transcrição

00:00

Bom, pessoal, então vamos lá. Seja muito bem-vindo à nossa disciplina de Prompt Engineer. E eu acho que uma das coisas mais importantes quando a gente está falando sobre inteligência artificial generativa é a parte de prompt. E o grande ponto é que, normalmente, quando a gente está falando sobre prompts, muita gente já sabe que o importante é saber o que pedir para ir lá.

00:26

Mas o grande ponto é como pedir, quais são as técnicas que a gente tem que utilizar para fazer isso, e também conseguir trabalhar com isso de forma estruturada, organizada, para que você consiga, inclusive, trabalhar com prompts em alta escala, em aplicações que vão utilizar esses prompts, o jogo muda pra caramba. Então, o nosso objetivo aqui é a gente ter um prisma totalmente focado na parte de prompt.

00:56

Obviamente que a gente vai mostrar código, eventualmente a gente vai falar de alguns termos mais técnicos que podem convergir um pouquinho mais para o lado de arquitetura, mas a ideia principal é sempre tentar olhar pelo lado do prompt em si. Então, normalmente, o que eu costumo dizer é que se você vai falar sobre programação ou desenvolvimento, invariavelmente você vai falar sobre código,

01:22

mas, invariavelmente, você vai estar falando também um pouco sobre arquitetura. Então, existe sempre uma zona cinzenta nessas diferenciações. Então, o ponto que eu quero alinhar aqui com vocês é que tudo que a gente for falar, inclusive de forma um pouco mais técnica, eu quero deixar sempre bem alinhado na visão da criação, das técnicas, da utilização, da gestão dos prompts e tudo mais. Então, somente para a gente entender e você conseguir

01:51

ter uma visão mais geral do que a gente vai ver na disciplina como um todo, eu queria trazer aqui para vocês alguns bullet points que a gente vai seguir ao longo dessas próximas aulas. Então, a primeira coisa que a gente vai ver, e eu quero trazer isso com uma clareza bem forte, é o entendimento do que realmente é Prompt Engineering. Então, a gente vai entender isso de verdade,

02:17

e o porquê que isso é importante. Eu quero elevar o seu nível de consciência em relação a isso. Também a gente vai entender as técnicas e tipos de prompts. Existem ali um monte de tipos e técnicas de prompts que são utilizadas diariamente. Muitas delas provavelmente você já usou e talvez de forma inconsciente.

02:36

Mas existem realmente técnicas que se você não entender a estrutura, não entender o motivo, você não entender o porquê você está utilizando, simplesmente você não vai conseguir tirar resultados decentes e resultados que realmente vão ajudar a empresa ou até mesmo você em relação à produtividade e tudo mais, certo?

02:58

Também, uma coisa que eu quero deixar claro é que, apesar de essa ser uma disciplina que a gente visa muito na escrita e entender prompt, eu quero trazer ao máximo exemplos práticos, vendo os prompts, trazendo as suas respostas, mostrar o código sendo utilizado junto com o prompt. Então, eu não quero aqui também ficar apenas digitando com você, porém, a gente tem que ter a clareza

03:27

de que é uma disciplina que vai focar em escrever. Mas o grande ponto não é a gente ficar digitando palavra por palavra, é entender o que está por trás daquele prompt e como aquele exemplo pode se encaixar no nosso dia a dia.

03:43

Beleza? Outra coisa também é que com esses tipos de prompts e com as técnicas que você vai aprender, você também vai conseguir ter a capacidade de criar prompts e estruturar prompts realmente profissionais para você poder criar os seus agentes de IA para integrar nas aplicações das empresas.

04:01

Você também vai ser capaz de criar os seus próprios agentes para te ajudarem em relação à parte de codificação. Você vai também poder ser capaz de criar assistentes, como aqueles meus GPTs, que podem te ajudar no dia a dia também. Nós vamos falar também sobre estratégias de como você armazena e versiona prompts. Lembrando que uma das coisas mais importantes para o saída dos resultados das aplicações que a gente desenvolve daqui para frente utilizando o IA,

04:28

são os prompts, então eu digo normalmente 50% é código, é programação e 50% é prompt então se você não tiver uma gestão decente disso, realmente você pode trazer danos ali irreparáveis para os softwares que vão estar rodando com esses prompts, tá?

04:44

Uma outra coisa também é que a gente vai falar um pouco mais sobre a gestão desses prompts com plataformas de terceiros. Existem plataformas como a Langsmith, a gente tem PromptLayer, e a gente tem ferramentas que vão também nos ajudar a fazer a gestão desses prompts, ver, inclusive, como é que eles estão sendo utilizados, trazer estimativa de custo e diversos detalhes, inclusive essa parte de testabilidade e avaliação dos prompts, né?

05:13

como que eu consigo pegar diversos prompts e ver qual que funcionou melhor, ou pegar o mesmo prompt, testar o mesmo prompt com diversos modelos diferentes e ver se o resultado era o esperado. E uma das coisas bem fortes aqui é que, de uma forma ou de outra, a gente vai ter uma, vamos dizer assim, emendar com a parte de design docs, que é uma das coisas mais importantes nos dias de hoje,

05:41

quando a gente vai falar sobre produtividade e desenvolvimento de projetos de software, porque design docs são diversos tipos de documento de como você cria uma estratégia para organizar e trabalhar com diversos documentos em diversos contextos dos seus projetos de software.

06:00

Então, para cada tipo de necessidade, para cada tipo de contexto, você pode ter documentações diferentes, diagramas diferentes, etc. E uma das coisas que mais, agora com a inteligência artificial nos ajudando, é a geração dessa documentação.

06:18

O grande ponto é que eu percebo que muitos desenvolvedores não têm uma clareza da quantidade e das variações de documentações que a gente pode ter. Então, trabalhar com o Prompt daqui pra frente vai facilitar muito a...

06:34

a geração e a criação desses tipos de documentação quando a gente for especificamente em disciplinas ali como Design Docs, tá? E um outro ponto importante é que tudo que eu for utilizar dos exemplos, dos prompts e etc. que eu tô trazendo e que eu vou mostrar, eu vou deixar ali disponível pra você num repositório do GitHub, né? Pra que você consiga ver os exemplos de código, os prompts, pra você conseguir testar.

07:01

e tudo mais, fechou? Então, era essa visão, queria alinhar essas expectativas aqui com você. A gente não vai fazer nenhuma mágica, mas eu espero que você fique surpreso com a quantidade de coisas que você consegue fazer estruturando prompts e a quantidade de coisas que estão em volta

07:20

de Prompt Engineering, que vão afetar diretamente no custo, na qualidade, na latência da sua aplicação e o resultado final que a empresa e você, inclusive, em relação à produtividade, está esperando. Beleza? Então, vamos nessa, porque a gente tem bastante coisa para a gente ver.

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **GPTs** — Generative Pre-trained Transformers  

**Resumo**  
A aula apresenta Prompt Engineering como a prática de projetar instruções para modelos de IA de forma deliberada, tratando o prompt como um artefato de engenharia e não como texto improvisado. O instrutor destaca que, em aplicações reais, a forma de pedir influencia diretamente a qualidade, a consistência e a utilidade das respostas, impactando o comportamento observável do sistema tanto quanto regras implementadas em código. A disciplina é posicionada como um estudo focado em prompt, mas sempre com conexão prática com desenvolvimento, arquitetura e uso em software.

Ao longo da aula, são definidos os eixos que guiarão o conteúdo: entender o que é Prompt Engineering e por que ele é importante; conhecer tipos e técnicas de prompts; aplicar exemplos práticos com código e respostas; criar prompts profissionais para agentes de IA, assistentes de codificação e apoio ao dia a dia; e aprender estratégias de armazenamento, versionamento, gestão e avaliação de prompts. O instrutor também menciona ferramentas de observabilidade e gerenciamento, como LangSmith e PromptLayer, que ajudam a acompanhar execuções, custos e comportamento dos prompts em produção. Além disso, a disciplina se conecta à geração de documentação, especialmente design docs, diagramas e outros artefatos usados em projetos de software, mostrando como prompts bem estruturados podem acelerar a produção de documentação útil e contextualizada.

A aula também reforça a importância de repositórios, como o GitHub, para guardar exemplos de código e prompts, permitindo reprodução de experimentos, testes e comparação entre abordagens. O fluxo explicado é de sair da visão intuitiva de “saber o que pedir” para uma visão técnica de “saber como pedir”, estruturar, versionar, testar e monitorar prompts, com atenção a custo, latência, previsibilidade e produtividade.  

**Pontos de atenção**  
- Prompt deve ser tratado como parte da engenharia do sistema, não como texto casual ou improvisado.  
- Pequenas mudanças em um prompt podem alterar significativamente o comportamento da aplicação.  
- Não basta escrever “bem”; é preciso explicitar contexto, tarefa, formato esperado e critérios de qualidade.  
- Entender a estrutura e o motivo de cada técnica de prompt é essencial para obter resultados consistentes.  
- Prompts precisam ser armazenados e versionados para permitir auditoria, rollback e comparação entre versões.  
- Prompts sem gestão adequada podem causar danos relevantes ao software e ao comportamento em produção.  
- Ferramentas como LangSmith e PromptLayer ajudam na observabilidade, no controle de execução e na estimativa de custos.  
- Prompts devem ser testáveis: comparar versões, tarefas e modelos diferentes é parte do processo técnico.  
- Geração de documentação com IA exige instruções específicas; sem isso, o resultado tende a ser genérico.  
- Manter prompts e exemplos em repositório, como GitHub, favorece reprodutibilidade e colaboração.  
- Prompt Engineering impacta diretamente custo, latência, qualidade da resposta e produtividade do time.  
- O objetivo não é decorar fórmulas, mas entender como estruturar prompts para uso real em aplicações e agentes de IA.
