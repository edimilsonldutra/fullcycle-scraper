Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17076)

## Resumo da aula

O Feature Design Doc funciona como insumo controlado para a geração dos diagramas. Em vez de pedir ao modelo que “imagine” a arquitetura, o processo parte de objetivos técnicos, escopo, exclusões, fluxos, interface pública, semântica, exemplos de uso, configurações e opções já documentados. Retomando o Rate Limiter já definido antes, a novidade aqui é transformar esse documento em base operacional para produzir artefatos versionáveis. Isso reduz invenção, porque o agente passa a extrair estrutura do que está escrito, não do que seria plausível.

PlantUML já foi referenciado antes como formato textual útil para diagramas C4; aqui ele vira o alvo explícito da automação. O agente gera arquivos .puml como c1.puml, c2.puml, c3.puml e, quando houver base suficiente, níveis mais detalhados. Esse formato importa porque pode ser salvo no repositório, revisado em pull request e convertido em imagem depois. A automação fica mais confiável quando a saída principal é texto, não uma imagem opaca difícil de auditar.

O idioma do diagrama deve acompanhar o idioma do documento-fonte. Se o FDD estiver em inglês, o diagrama sai em inglês; se estiver em português, o diagrama sai em português, preservando nomes de tecnologias em inglês para manter precisão técnica. Essa regra precisa ser explícita no prompt porque modelos tendem a misturar idiomas, termos traduzidos indevidamente e acentuação inconsistente. Exigir UTF-8 evita corrupção de caracteres e garante que textos em português sejam renderizados corretamente nos artefatos gerados.

A automação não deve forçar completude artificial. O agente precisa decidir até qual nível do C4 consegue ir com base na densidade real do FDD: se o documento sustenta C1, C2 e C3, ele para ali; se não houver detalhe de código, não gera C4-Code. Essa regra é central para evitar diagramas detalhados demais, porém inventados. O critério correto não é “gerar todos os níveis”, mas “gerar apenas o que o documento consegue justificar”.

Um prompt confiável deixa de ser uma instrução curta e vira um workflow operacional. Ele define leitura do FDD, decisão de nível, geração dos arquivos, tratamento de erros, exportação opcional de imagem, relatório e revalidação final. Isso exige iteração, exemplos corretos e incorretos e regras detalhadas, porque boa parte dos erros recorrentes aparece justamente nas ambiguidades do comando. Quanto mais explícito o fluxo, menor a chance de o agente improvisar etapas ou ignorar restrições.

Além dos arquivos .puml, o processo gera um arquivo .md explicando o que foi produzido e por quê. Esse relatório registra justificativas, decisões de escopo e evidências de que cada nível foi escolhido com base no documento-fonte. O valor desse artefato está na auditabilidade: o time consegue revisar não só o diagrama final, mas também a lógica usada para chegar nele. Em geração assistida por IA, saída sem justificativa é difícil de confiar e mais difícil ainda de manter.

Gerar não encerra o processo; o agente precisa reler o documento e revalidar o que acabou de produzir. Essa segunda checagem serve para detectar inconsistências, elementos não sustentados pelo FDD e problemas de exportação ou formatação. A validação também deve cobrir erros operacionais, como parâmetros inválidos ou falhas no uso do PlantUML. Sem essa etapa, a automação acelera a produção de artefatos, mas também acelera a propagação de erro.

Um subagente executa a tarefa em uma janela de contexto separada da conversa principal. Esse isolamento evita que o histórico corrente contamine a geração do diagrama e também impede que o prompt longo do gerador consuma o contexto do agente principal. Em workflows mais complexos, separar contexto melhora foco e previsibilidade. O ganho prático é transformar uma tarefa extensa e especializada em uma unidade isolada de execução.

Neste cenário, “agente” não depende de uma ferramenta específica; ele é, essencialmente, um prompt estruturado com regras e workflow. Por isso, o mesmo desenho pode ser adaptado para Claude, GPT, Gemini, Composer ou outros ambientes capazes de executar instruções longas e manipular arquivos. A portabilidade importa porque evita aprisionar o processo a um vendor ou IDE. O ativo principal deixa de ser a interface e passa a ser a especificação operacional do trabalho.

A execução do gerador depende de parâmetros explícitos. FilePath aponta para o FDD que será lido, OutputFolder define onde os artefatos serão gravados e flags como -noimage alteram o comportamento da execução, por exemplo desabilitando a geração de PNG. Essa parametrização transforma o prompt em comando reutilizável, ajustável a diferentes projetos e ambientes. Sem parâmetros claros, o processo fica acoplado a caminhos fixos e perde reprodutibilidade.

O pipeline completo segue uma ordem clara: ler o FDD, detectar idioma e regras de escrita, decidir o nível máximo sustentado, gerar os arquivos .puml, exportar imagem se necessário, produzir relatório em Markdown e revalidar tudo ao final. Retomando o exemplo do Rate Limiter, o sistema deixa de ser apenas um caso arquitetural explicado manualmente e passa a ser insumo para uma rotina repetível de documentação. Esse encadeamento é o que torna a geração útil em times reais: ela pode ser repetida, auditada e ajustada sem recomeçar do zero.

A chamada do agente pode ser simples, desde que os parâmetros estejam corretos. Informe o caminho do FDD em FilePath, escolha a pasta de saída em OutputFolder e adicione -noimage se quiser apenas os arquivos textuais. O comando também pode exigir artefatos esperados, como geração dos C4 e do relatório final. O ponto decisivo não é a sintaxe exata de uma ferramenta, mas a disciplina de tornar entradas, saídas e opções explícitas.

Depois da execução, a revisão deve verificar quatro pontos. Primeiro, se o idioma do diagrama acompanha o idioma do FDD sem traduzir nomes de tecnologia; segundo, se os níveis gerados param exatamente onde a documentação sustenta; terceiro, se os arquivos .puml e o relatório .md foram criados no local correto; quarto, se a justificativa textual realmente aponta para o documento-fonte. Se qualquer um desses itens falhar, o problema não está apenas na saída: está no prompt, nos parâmetros ou na validação insuficiente.

## Transcrição

00:01

Bom pessoal, seguinte, tô aqui na minha IDE, e pode ser qualquer IDE de forma geral. E nessa IDE minha, que eu tô utilizando o Cursor, mas poderia ser qualquer outro, no final das contas, o que eu fiz? Eu abri esse nosso Rate Limiter FDD. Então, basicamente,

00:21

foi esse cara, que a gente já falou nas aulas passadas e etc, que fala os objetivos técnicos, escopos, exclusões, fluxos detalhados, interface pública. Opa, eu acho que você está começando a entender de onde estão vindo aqueles diagramas. Semântica, exemplos de uso, configurações e opções. Está conseguindo entender de onde a IA tirou para gerar aquele tipo de diagrama C4?

00:48

Então, é basicamente daqui que as coisas estão vindo, tá? Então, nós temos aqui as diversas seções de como estão definidos o nosso Rate Limiter. O grande ponto aqui que a gente tem que se ligar é o seguinte, quando nós estamos falando especificamente de diagrama C4, existem diversas ferramentas que você utiliza para gerar esses diagramas C4. Existem diversas ferramentas.

01:15

Porém, uma coisa interessante de Diagrama C4 é que você pode utilizar algo chamado de Plain to ML. Ou seja, é uma linguagem, principalmente de marcação, que vai te ajudar a conseguir importar diversos tipos de componentes, e esses tipos de componentes são capazes de gerar os Diagrama C4 naquele padrão que eu te coloquei.

01:41

que eu mostrei pra você, tá? E aquele padrão que eu coloquei, ele é muito comum mesmo você ver em diagrama C4, aquela corzinha azul, aquele cara usa, aqueles limites e tudo mais, tá? O Plato ML, ele consegue gerar muito mais coisas além de diagrama C4.

01:59

Mas diagramas C4 funcionam muito bem com o Plane2ML porque existem diversas componentes prontas. Então, o que acontece aqui? Eu criei, nesse caso aqui, utilizando o Cloud, mas eu vou mostrar algo bem interessante aqui pra você também.

02:16

Utilizando o Cloud, e aqui no Cloud, eu tenho dois agentes. Um agente que eu quero falar especificamente agora é o do Diagrama C4. Esse agente do Diagrama C4, se você perceber aqui, basicamente o que ele faz, deixa eu trazer aqui pra gente ver melhor,

02:38

Ele... De forma geral, o que ele vai nos ajudar? Ele... Eu coloquei algumas regras interessantes, tá? Que é do tipo, se o meu documento de feature for em inglês, eu quero que o meu diagrama seja em inglês. Agora, se o meu documento de feature é em português, eu quero que meu diagrama seja em português desde que...

02:56

o que é nome de tecnologia se manter em inglês, tá? Então... E também pedir pra colocar português com acento. E tudo isso aí acaba virando detalhes, porque tem que estar em UTF-8 pra você não dar problema nos acentos. O que eu tô querendo dizer, galera, é que não é tão... Ah...

03:12

Simples fazer um prompt às vezes, dá trabalho, tem muitas iterações, mas aqui eu trouxe inclusive exemplos corretos de português, exemplos incorretos de português, mas o que eu quero que você consiga entender é que eu pedi aqui para fazer essa geração

03:29

utilizando o seguinte princípio, tá? Primeira coisa, ele vai ler o nosso Feature Design Doc, que vai determinar quais são os níveis que a gente vai utilizar. Por quê? Eu pedi pra IA olhar o seguinte, né? Se eu não tenho tantas informações, eu quero que ele gere o diagrama pra mim somente do que é possível. Então, se a gente não tiver detalhe de código, não gere o C4, gere até o C3, e assim vai.

03:55

E o ponto interessante aqui é que ele vai gerar um arquivo de plant.uml e a ideia é que ele gere dessa forma aqui. Então tem o c1, c2, c3, c4 e o p.uml é do plant.uml e depois eu quero que ele gere um arquivo md, analisando e mostrando como as justificativas e como que esse cara foi gerado, basicamente.

04:18

E aqui são detalhes realmente de como vai ler. Recomendo que depois você olhe bem esse prompt. Tem o workflow dele, o passo a passo do que ele vai ter que fazer. Depois disso, tem alguns pontos importantes aqui, que é o seguinte, ele pode gerar o arquivo Plain2ML pra gente.

04:37

Mas eu também posso pedir para ele já gerar o PNG, a imagem, tá? Então, isso depende muito da forma de como que você vai trabalhar e, inclusive, dependências no seu computador, por exemplo. Da forma como tá, ele vai utilizar o Plane2ML, ou seja, ele vai instalar na sua máquina, ou se você já tem instalado, ele vai trabalhar aqui dessa forma.

04:56

Então, dentro desse prompt, ele traz, basicamente, os pontos principais aqui para a gente. Então, ele está mostrando parâmetros corretos e incorretos, porque durante toda essa história, de todos os testes que eu fiz, esse prompt conseguiu cobrir bastante coisa para evitar problemas comuns, e eu fui sempre colocando aqui essas informações. Então, é um prompt grande, e esse prompt, no final das contas, quando a gente está falando no cloud,

05:24

Eles são importantes. E depois que ele gerar tudo, eu pedi para ele revalidar tudo e fazer uma outra verificação, ler novamente o documento, ou seja, tem bastante coisa que ele vai fazer, pedi para ele olhar aqui o Plain2ML para ele conseguir exportar o diagrama, ou seja, dei a maior parte das informações aqui que ele precisava. Coloquei como trabalhar com erro, a execução do workflow, ou seja, é um prompt bem grande. Mas, no caso do Cloud aqui, ele trabalha como um subagente. O que isso significa?

05:54

que quando o Claudio executar esse camarada, no final das contas, o que vai acontecer é que esse agente vai rodar numa janela de contexto diferente para não atrapalhar a janela de contexto do agente atual. Agora, um ponto importante que eu quero trazer aqui para você é o seguinte,

06:14

você não precisa ter o Cloud Code para conseguir utilizar esse agente aqui. E por que eu estou dizendo isso? Porque agente é simplesmente prompt, de forma geral, nesse nosso caso. Então, eu posso pedir para o GPT, eu posso pedir para o Gemini, eu posso pedir para o Composer,

06:33

que é um modelo que a própria empresa que faz o Cursor lançou também. E você vai perceber que esses caras vão ser capazes também de gerar esses diagramas aqui para vocês. Um outro ponto aqui importante que eu queria trazer é a parte de comandos. Então, se você olhar aqui no Cloud, eu tenho um prompt de comando. O que significa um prompt de comando? É como que eu vou pedir

07:01

para que aquele agente, aquele prompt, seja executado. Então, você precisa chamar esse gerador agente, ele vai extrair o FDD, onde eu passei uns parâmetros, ele tem o path do FDD, ou seja, do Feature Design Doc, com a pasta que você quer que ele coloque, e se ele não quer que gere imagens, coloca "-noimage", na hora ali no prompt.

07:27

E aqui tem, no final das contas, o que é pedido para fazer. Gério C4, Reminders, Report, ou seja, quando você terminar, você tem que trazer essas informações, troque o FilePath para o ponto que o cara está utilizando, use o Output Folder porque ele pode ser alterado,

07:48

Então, perceba, é um comando bem simples de forma geral que é totalmente capaz de fazer com que você gere esses diagramas. Agora, um ponto importante que eu queria trazer aqui no caso para vocês é que eu vou fazer algumas experiências aqui com você.

08:07

para que você consiga perceber as diferenças e as nuances de quando você trabalha com diferentes agentes ou quando você tenta gerar várias vezes a mesma coisa com o mesmo agente, com o mesmo modelo e coisas desse tipo, tá? Então, o que acontece é o seguinte,

08:25

O cursor, tá? Eu vou dar um pra vocês verem. Eu não vou nem usar o cloud nesse momento, depois eu vou cortar esse vídeo. Na realidade, eu vou cortar esse vídeo aqui e daí a gente vai direto pros agentes, vai ficar melhor. Beleza? Vamos nessa!

## Resumo IA

**Abreviações**  
- **FDD** — *Feature Design Doc* (Documento de Design da Feature)  
- **C4** — Modelo de diagramas arquiteturais em níveis: Contexto, कंटêineres, Componentes e Código  
- **PNG** — *Portable Network Graphics*  
- **UTF-8** — *Unicode Transformation Format 8-bit*  
- **IDE** — *Integrated Development Environment* (Ambiente de Desenvolvimento Integrado)  
- **Prompt** — Instrução textual dada ao modelo/agente para executar uma tarefa  
- **PlantUML / .puml** — Linguagem textual e extensão de arquivo usada para descrever diagramas  
- **Markdown / .md** — Formato de texto marcado para documentação  

**Resumo**  
A aula mostrou como usar um *Feature Design Doc* como fonte controlada para gerar diagramas de arquitetura C4 com ajuda de IA, evitando que o modelo “invente” elementos com base em suposições. O instrutor retomou o exemplo do Rate Limiter e explicou que o processo parte de informações já documentadas, como objetivos técnicos, escopo, exclusões, fluxos, interface pública, semântica, exemplos de uso, configurações e opções. A partir disso, o agente lê o documento-fonte e extrai o que realmente pode ser representado em cada nível do C4.

Foi destacada a escolha do PlantUML como formato textual de saída para os diagramas, especialmente por permitir versionamento, revisão em pull request e geração posterior de imagem. O fluxo proposto gera arquivos como c1.puml, c2.puml e c3.puml, podendo incluir níveis mais detalhados apenas quando houver base suficiente no documento. O instrutor reforçou que a automação deve ser guiada pelo conteúdo real do FDD, e não pela expectativa de completar todos os níveis do C4.

Outro ponto central foi a definição explícita de idioma e codificação. Se o FDD estiver em inglês, o diagrama deve sair em inglês; se estiver em português, o diagrama deve acompanhar esse idioma, preservando nomes de tecnologias em inglês. Para evitar problemas com acentuação e caracteres especiais, foi enfatizada a necessidade de UTF-8. O prompt também precisa conter exemplos corretos e incorretos para reduzir ambiguidades e erros de geração.

A aula descreveu o prompt como um workflow operacional, e não apenas uma instrução curta. Esse workflow inclui: leitura do FDD, decisão do nível máximo sustentado, geração dos arquivos .puml, eventual exportação de PNG, criação de um relatório em Markdown e revalidação final. O agente também deve reler o documento depois de gerar os artefatos para verificar inconsistências, elementos não sustentados e falhas operacionais. Foi explicado que esse tipo de agente pode ser executado como subagente, em uma janela de contexto separada, evitando contaminação do histórico principal.

Por fim, o instrutor comentou a parametrização da execução com campos como FilePath, OutputFolder e flags como -noimage para desabilitar imagens. A ideia é tornar o processo reutilizável, portável entre diferentes ferramentas e ambientes, e auditável por meio do relatório que justifica as decisões tomadas. O pipeline final resumido na aula é: ler o FDD, detectar idioma e regras de escrita, decidir o nível máximo, gerar os diagramas em PlantUML, exportar imagem se necessário, produzir relatório em Markdown e revalidar tudo ao final.

**Pontos de atenção**  
- Não pedir para a IA “imaginar” a arquitetura; a geração deve se basear estritamente no FDD.  
- Gerar somente até o nível do C4 que o documento realmente sustenta; não forçar C4-Code sem detalhe suficiente.  
- Manter o idioma do diagrama alinhado ao idioma do FDD, preservando nomes de tecnologias em inglês.  
- Usar UTF-8 para evitar corrupção de acentos e caracteres em português.  
- Preferir saída textual em PlantUML (.puml) para facilitar revisão, versionamento e auditoria.  
- Incluir no prompt um workflow claro: leitura, decisão de nível, geração, exportação, relatório e revalidação.  
- Exigir relatório em Markdown com justificativas e evidências da escolha de cada nível gerado.  
- Revalidar a saída após a geração para detectar inconsistências, invenções e erros de formatação/exportação.  
- Tratar falhas operacionais, como parâmetros inválidos ou problemas com PlantUML, no próprio fluxo do agente.  
- Usar parâmetros explícitos como FilePath, OutputFolder e flags como -noimage para garantir reprodutibilidade.  
- Isolar a execução em subagente quando possível, para não consumir nem contaminar o contexto principal.  
- Revisar se os arquivos .puml e .md foram gravados no local correto e se a justificativa realmente cita o documento-fonte.