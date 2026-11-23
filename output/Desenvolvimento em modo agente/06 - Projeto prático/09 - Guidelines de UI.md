Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17972)

## Resumo da aula

Gates determinísticos, já definidos anteriormente, validam compilação, lint e regras arquiteturais, mas não garantem coerência visual. Uma interface pode estar tecnicamente correta e, ainda assim, destoar do restante do produto. Esse tipo de falha aparece em espaçamento, cores, aparência de componentes, imagens e organização visual. No front-end com agentes, esse risco aumenta porque o modelo tende a completar lacunas por inferência.

Sem referência visual suficiente, o agente produz telas com estilos divergentes entre si. Uma página pode sair mais moderna, outra mais simples, outra mais carregada, mesmo pertencendo ao mesmo produto. O problema não é funcionalidade, e sim falta de alinhamento com a identidade visual. Por isso, consistência de UI precisa ser tratada como insumo explícito, não como algo que o modelo descobrirá sozinho.

Harness, retomando a definição já estabelecida, inclui qualquer mecanismo que reduza inferência e aumente aderência ao projeto. Nesse contexto, uma pasta com artefatos de UI também faz parte do harness, porque orienta a geração do front-end. Esses artefatos funcionam como base concreta para o agente construir interfaces sem começar do zero. O controle aqui não vem de um gate técnico, mas de contexto operacional fornecido ao modelo.

A referência visual pode incluir design system, tokens, imagens, logos e screenshots de telas. Esses elementos delimitam a linguagem visual que o agente deve seguir ao criar componentes e páginas. Tokens ajudam a preservar decisões de cor, espaçamento e estilo; screenshots e telas mostram composição e padrão de uso. O objetivo não é impor uma ferramenta específica, e sim disponibilizar insumos que expressem a identidade do produto.

A instrução correta para o agente é simples: não comece a interface do zero quando já existe identidade visual definida. Use as referências disponíveis, considere os tokens, observe os screenshots e respeite o padrão visual existente. Essa orientação reduz a chance de o front-end virar uma coleção de telas desconectadas. Em vez de improvisar, o agente passa a operar com restrições visuais claras.

Em equipes tradicionais, designers, tech leads e desenvolvedores front-end experientes reconhecem rapidamente quando um botão, uma cor ou um espaçamento destoam do padrão. Esse julgamento costuma existir de forma implícita na experiência da equipe. Com agentes, esse conhecimento precisa ser externalizado em artefatos e instruções, porque o modelo não compartilha o repertório tácito do time. A consistência visual depende, portanto, de transformar percepção humana em contexto explícito.

Quando as guidelines de UI se somam aos gates do back-end e às demais restrições do projeto, a consistência deixa de ser apenas estrutural e passa a incluir também a interface. O resultado é um processo mais estável ao longo de todo o desenvolvimento. A arquitetura continua protegida pelos gates, enquanto a camada visual é estabilizada por referências de UI. Cada mecanismo cobre um tipo diferente de desvio.

A origem dos artefatos pode variar conforme a equipe use Figma ou qualquer outra ferramenta. O ponto central não é a plataforma, mas a capacidade de transmitir à IA os conceitos visuais corretos. Se as telas de referência, logos, screenshots e padrões estiverem acessíveis, o agente já tem base suficiente para produzir interfaces mais coerentes. A implementação concreta pode mudar, mas a necessidade de contexto visual permanece.

## Transcrição

00:01

Bom, pessoal, seguinte.

00:02

Nesse vídeo, a gente vai falar sobre uma parte menor,

00:06

mas ela é muito importante em relação à parte do nosso harness,

00:11

que são as guidelines para UI. Até agora,

00:15

a gente falou sobre gates determinísticos, ou seja,

00:18

os mecanismos que ajudam o projeto a validar se o código continua compilando,

00:23

se as regras foram respeitadas, se a arquitetura não foi quebrada e etc.

00:27

Mas... Quando a gente olha para o front-end, por exemplo,

00:30

existe um outro tipo de problema.

00:32

Nem tudo que importa na interface aparece como um erro.

00:37

de compilação. Ou seja, uma tela pode compilar, pode passar no lint,

00:42

pode até funcionar,

00:43

mas ainda assim parecer totalmente desconectada do restante do produto.

00:48

Pode ser que a gente usou espaçamento diferente,

00:50

cor errada, componente com aparência inconsistente,

00:53

imagem fora do padrão,

00:54

ou uma estrutura visual que não está conversando com as outras telas.

00:58

E quando a gente usa agente de IA para desenvolver front-end,

01:01

isso fica ainda mais sensível.

01:03

Se o agente não tiver uma referência visual suficiente,

01:06

ele vai tentar inferir, e quando ele infere demais,

01:09

cada tela pode sair com uma cara completamente diferente.

01:13

Uma página pode parecer mais moderna, outra mais simples,

01:16

outra mais carregada, outra com componente que não seja na mesma linha visual.

01:20

Então por isso, por exemplo, no nosso caso aí do Videomax,

01:23

a gente também vai preparar uma área com artefatos de UI.

01:28

A ideia é a gente ter uma pasta contendo os materiais que

01:31

o agente pode usar como base para desenvolver o front-end.

01:34

Isso vai incluir principalmente o design system com os tokens, com imagem, logo,

01:40

de tela, para que ele utilize isso como referência para criar os componentes.

01:45

Perceba que isso também é harness. Por quê?

01:48

Porque você está dando uma forma de ele...

01:52

conseguir seguir algo. Harness é qualquer coisa que ajuda,

01:55

dá guidance ali pra nossa IA, tá? Só que esse controle,

02:00

ele não tá vendo, ele não tá vindo,

02:02

vamos dizer assim, pra um meio, pra um gate tão técnico.

02:05

Ele tá vindo muito mais pro contexto.

02:07

Então a gente tá dizendo pro agente, quando você for construir uma interface,

02:11

não comece do zero. Use essas referências. Considere esses tokens.

02:15

Observe esses screenshots. Respeite essa identidade visual.

02:19

Isso vai reduzir bastante a chance do front-end

02:22

virar uma coleção de telas totalmente desconectadas.

02:25

E esse é o ponto importante, porque no desenvolvimento tradicional,

02:28

muitas vezes um designer, um tech lead, ou um desenvolvedor front-end experiente,

02:33

carrega esse padrão visual na cabeça. Ele sabe quando uma tela está estranha,

02:37

ele percebe quando um botão não está combinando,

02:39

quando o espaçamento está inconsistente, ou que a cor saiu do padrão.

02:43

Já com os agentes, a gente precisa fazer com que isso...

02:47

como que eu posso dizer,

02:48

isso se torne um contexto de uma forma mais explícita. Então,

02:51

Não basta esperar que o modelo adivinhe a identidade visual do produto.

02:55

A gente tem que fornecer isso aí para ela. Então, no caso do VideoMax,

02:58

a gente vai ter ali as guidelines de UI e

03:02

isso aí vai funcionar como referência para que o agente,

03:06

ele utilize, tá? De forma geral, como que ele vai trabalhar, tá?

03:11

Outros pontos importantes são, então, isso aí, tendo essa parte visual,

03:16

conectada com o backend onde a gente tem esses gates também,

03:19

a gente já começa a avançar para algo que

03:23

vai gerar mais consistência ao longo de todo o processo.

03:28

Então, a gente tem que lembrar que as guidelines de UI vão

03:31

ajudar principalmente a reduzir os desvios visuais e de consistência de interface.

03:38

Então, basicamente, a gente vai preparar...

03:41

o agente para ter acesso a esses aspectos, tá?

03:44

E a gente vai poder ter logo,

03:46

a gente pode ter screenshot, a gente pode ter referência,

03:48

vai depender de como cada equipe, como cada empresa trabalha,

03:51

qual ferramenta utiliza, se utiliza Figma, se utiliza ferramenta XYZ,

03:57

eu não tô preocupado com isso, eu tô preocupado com o quê?

04:00

que você consiga passar esses tipos de conceitos ali para IA.

04:06

E eu vou mostrar agora no próximo vídeo como é que eu fiz aqui, apenas por exemplo,

04:09

mas não significa necessariamente que você precisa fazer dessa forma.

04:13

O que eu precisava era ter as telas que eu vou utilizar ali como base. Fechou?

## Resumo IA

**Abreviações**
*   **UI:** User Interface
*   **IA:** Inteligência Artificial

**Resumo**
A aula aborda a crítica necessidade de garantir a consistência visual em interfaces de usuário (UI), um desafio que se intensifica com o uso de agentes de Inteligência Artificial (IA) no desenvolvimento de front-end. Diferente dos gates determinísticos que validam a compilação, o lint e as regras arquiteturais, esses mecanismos não garantem a coerência estética e visual de um produto. Uma interface pode estar tecnicamente correta, mas visualmente desalinhada em termos de espaçamento, cores, aparência de componentes, imagens ou organização geral, especialmente porque agentes de IA tendem a completar lacunas por inferência sem referências visuais explícitas, resultando em telas com estilos divergentes.

Para solucionar isso, a consistência de UI deve ser tratada como um insumo explícito para os agentes. O conceito de "harness" é expandido para incluir uma pasta com artefatos de UI, que servem como base concreta e orientam a geração do front-end. Esses artefatos podem incluir design systems, tokens de design, imagens, logos e screenshots de telas. Tokens ajudam a preservar decisões de estilo, enquanto screenshots mostram composição e padrões de uso. O instrutor enfatiza que o controle não vem de um gate técnico, mas do contexto operacional fornecido ao modelo, e a ferramenta de design (como Figma) utilizada para criar os artefatos é secundária à capacidade de transmitir os conceitos visuais corretos à IA.

A instrução crucial para o agente é clara: não começar a interface do zero, mas sim usar as referências disponíveis, considerar os tokens, observar os screenshots e respeitar a identidade visual existente. Essa abordagem reduz significativamente a chance de o front-end se tornar uma coleção de telas desconectadas. Em contraste com o desenvolvimento tradicional, onde designers e desenvolvedores experientes carregam esse padrão visual implicitamente, com agentes de IA, esse conhecimento tácito precisa ser externalizado em artefatos e instruções explícitas. A integração das guidelines de UI com os gates de backend e outras restrições do projeto resulta em um processo de desenvolvimento mais estável e um produto final mais coeso.

**Pontos de atenção**
*   **Limitação dos Gates Determinísticos:** Gates de compilação, lint e regras arquiteturais asseguram a correção técnica e arquitetural, mas são insuficientes para garantir a consistência e coerência visual da interface do usuário.
*   **Risco da Inferência Excessiva em Agentes de IA:** Agentes de IA, na ausência de referências visuais explícitas e suficientes, tendem a inferir estilos e completar lacunas, o que leva à geração de telas com aparências inconsistentes e desalinhadas com a identidade visual do produto.
*   **UI como Insumo Explícito:** A consistência visual não é algo que o modelo de IA deve "adivinhar" ou inferir. Ela deve ser fornecida de forma explícita e clara como parte dos insumos do projeto.
*   **Externalização do Conhecimento Tácito:** O conhecimento sobre consistência visual que designers e desenvolvedores front-end experientes possuem de forma implícita deve ser externalizado em artefatos e instruções claras para que os agentes de IA possam compreendê-lo e aplicá-lo.
*   **Amplitude das Inconsistências Visuais:** Falhas na consistência visual se manifestam em detalhes como espaçamento, paleta de cores, aparência de componentes, padrões de imagem e organização visual, e não são detectáveis por validações de código convencionais.
*   **Boas Práticas para o Harness de UI:**
    *   Incluir no "harness" uma coleção de artefatos de UI, como design systems, tokens, logos, imagens e screenshots de telas de referência.
    *   Utilizar tokens para preservar decisões de estilo (cor, espaçamento, tipografia) e screenshots para demonstrar a composição e o uso de padrões visuais.
    *   Instruir o agente de IA a não criar interfaces do zero, mas a utilizar as referências fornecidas, considerando os tokens e observando os screenshots para respeitar a identidade visual existente.
    *   Priorizar a capacidade de transmitir os conceitos visuais corretos à IA, em vez da ferramenta específica utilizada para criar os artefatos (e.g., Figma).
*   **Benefício da Abordagem Holística:** A combinação das guidelines de UI com os gates de backend e outras restrições do projeto garante uma consistência abrangente, estabilizando tanto a estrutura do software quanto a camada visual ao longo de todo o processo de desenvolvimento.