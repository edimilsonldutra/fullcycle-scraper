Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17078)

## Resumo da aula

Mermaid é uma linguagem de marcação que converte texto em diagramas, permitindo descrever visualmente fluxos, integrações e estruturas sem sair do documento técnico. O valor principal está em tratar o diagrama como artefato textual, o que o aproxima do fluxo normal de engenharia: editar, versionar, revisar em diff e automatizar. Isso o torna especialmente adequado para documentação viva, em que o diagrama precisa evoluir junto com o conteúdo escrito.

A diferença prática em relação ao PlantUML está na verbosidade. Embora PlantUML continue útil, sua sintaxe tende a crescer rapidamente quando o diagrama incorpora mais elementos visuais, como classes, ícones e convenções adicionais. Mermaid reduz esse atrito ao oferecer uma escrita mais enxuta, o que diminui o custo de criação e manutenção e favorece uso frequente em documentação cotidiana.

Como o diagrama é texto, ele pode ser gerado, revisado e atualizado por agentes de IA com muito menos fricção do que arquivos puramente visuais. Isso combina com o workflow já visto de geração a partir de um FDD, mas amplia o uso para cenários menores e mais locais. O resultado é uma documentação mais fácil de manter consistente, porque o diagrama deixa de depender de edição manual em ferramenta gráfica ou de exportações repetidas.

Uma vantagem operacional importante é a renderização direta em Markdown, inclusive em plataformas como GitHub. Quando o bloco Mermaid é inserido no README ou em outro documento compatível, o diagrama pode aparecer no próprio contexto da documentação, sem exigir um ciclo separado de gerar imagem, fazer upload e referenciar arquivo externo. Isso reduz atrito de publicação e incentiva o time a documentar mais.

Retomando o Rate Limiter já detalhado em níveis anteriores, Mermaid é útil quando o objetivo não é reabrir toda a arquitetura, mas registrar um fluxo específico ou uma regra de negócio pontual. Em vez de insistir em uma visão estrutural completa, faz mais sentido representar, por exemplo, uma decisão de limitação, uma sequência de validações ou um fluxo de integração descrito no documento. Esse uso é mais leve, mais rápido de revisar e mais compatível com documentação embutida no texto.

C4 continua sendo mais forte quando a pergunta é arquitetural e exige convenção clara de níveis, fronteiras e relações entre partes do sistema. Mermaid atende melhor quando a necessidade é comunicar rapidamente um fluxo, uma regra ou uma estrutura simples dentro do próprio documento. A escolha correta não é “qual é melhor em absoluto”, mas qual linguagem responde melhor ao tipo de explicação que precisa ser mantida.

É possível tentar reproduzir visualmente níveis do C4 com Mermaid, mas isso não preserva automaticamente a convenção do modelo. O diagrama pode até parecer semelhante, porém tende a fugir do padrão esperado de representação arquitetural, o que reduz consistência entre leitores e artefatos. Por isso, Mermaid não substitui perfeitamente C4: ele é uma alternativa textual leve para outros tipos de comunicação, não uma cópia fiel de todas as suas regras.

Quando o custo de detalhar, renderizar e manter um diagrama arquitetural formal é maior do que o benefício, Mermaid costuma ser a opção mais eficiente. Ele favorece velocidade, embutimento no documento e baixo atrito de edição, enquanto C4 favorece estrutura arquitetural explícita. No contexto do Rate Limiter, isso significa usar C4 para vistas arquiteturais e Mermaid para fluxos e regras específicas que precisam viver junto do Markdown.

## Transcrição

00:01

Bom pessoal, dito isso, demos uma passada agora sobre diagrama C4, lembre-se que você tem acesso a todos esses prompts etc, recomendo que você teste e tudo mais, mas agora a gente também tem outros tipos de diagrama que não são C4 e que hoje em dia estão, vamos dizer, bastante na moda pela

00:21

Simplicidade que esses caras têm, tá? E eu espero que você já tenha ouvido falar, se nunca ouviu, não tem problema. Novamente, não é um curso de Mermaid, mas também dá pra você ter uma boa visão do que isso se trata, tá? Hoje em dia, a gente tem algo que a gente chama de Diagramas Mermaid, tá? Então, Mermaid é uma linguagem de marcação que transforma texto em diagramas.

00:45

Ela permite a gente representar fluxos, integrações e estruturas de sistemas de forma simples e legível dentro de documentos técnicos. Por gerar gráficos diretamente do código, facilita a manutenção, revisão e automação por agentes de IA, tornando a documentação sempre atualizada e consistente. Galera, o grande ponto aqui desses diagramas Mermaid é que eles realmente são muito fáceis de você gerar.

01:11

E o mais interessante é que ele não é Plain2ML. E o que eu estou querendo dizer com ele não ser Plain2ML? Quando você olha um código Plain2ML, deixa eu pegar esse cara aqui,

01:27

Ainda mais que esse cara aqui, a gente tá falando de classes, né? E... Cara, assim... É... Apesar de não ser difícil, é bastante verboso e isso porque o composer gerou de uma forma bem simplificada ali, quando entra ícones, quando entra um monte de coisa, as coisas acabam mudando. Mas eu acho que a grande sacada aí dos diagramas Mermaid

01:48

é que ele é muito fácil de você trabalhar com ele, e não ele é só fácil de você trabalhar. Você não precisa basicamente ir em nada, porque uma vez que você colocou ali dentro de um markdown o código desse diagrama, automaticamente, quando você estiver num GitHub da vida e você olhar sua documentação, esse diagrama já vai aparecer.

02:10

Então, você pode usar esse diagrama não apenas para gerar através de um feature design doc, mas, às vezes, você tem uma regra de negócio, você pode pedir para IA gerar um mermaid dessa regra.

02:22

Então, esses tipos de coisa facilitam muito a vida. E, nesse aspecto, eu prefiro, dependendo do contexto, trabalhar com o Mermaid do que com o C4. Como assim? Eu acho que o C4 nos dá uma visão muito clara de como que as coisas funcionam, principalmente mais em alto nível.

02:43

Em baixo nível, você precisa de muitos detalhes e acaba sendo bastante complexo você trabalhar com o C4. Também tem o aspecto de que toda vez que você quer ter um C4, você tem que gerar imagens, daí você tem que fazer upload, etc.

02:59

O mermaid, você está ali de forma geral dentro do seu readme e que você pode colocar o seu próprio diagrama, tá? Mas, novamente, eu acho que o propósito das coisas também às vezes acabam se tornando um pouco diferentes. Tanto que você pode até tentar fazer um mermaid,

03:17

a representar da mesma forma como um C4 representa cada um daqueles C's, mas você vai perceber que não é a mesma coisa. Eu já testei bastante utilizar Mermaid para gerar diagrama C4, e quando você olha,

03:34

pode até parecer e etc, mas ele foge do padrão da convenção, tá? Isso não significa que você não pode fazer e tudo mais, mas eu acho que a grande sacada aqui do Mermaid é pela facilidade, porque ele é menos verboso, é muito fácil de utilizar, ele renderiza em qualquer lugar, é somente dentro do seu próprio arquivo, do seu readme, dentro do seu markdown que você já pode utilizar esse cara, tá? No nosso próximo vídeo,

03:59

Eu vou mostrar pra vocês os principais tipos de diagrama que o Mermaid gera, e daí a gente vai fazer o mesmo esquema que a gente fez com o C4, fazendo com que o sistema gere os Mermaids pra gente. Beleza? Então, vamos nessa!

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **FDD** — Feature Design Doc
- **C4** — Context, Containers, Components, Code

**Resumo**
A aula apresentou o Mermaid como uma linguagem de marcação que transforma texto em diagramas, permitindo documentar fluxos, integrações e estruturas diretamente em arquivos técnicos. O instrutor destacou que a principal vantagem do Mermaid é tratar o diagrama como texto, o que facilita edição, revisão em diff, versionamento e automação, tornando a documentação mais viva e fácil de manter atualizada. Em comparação com o PlantUML, foi ressaltado que o Mermaid tende a ser menos verboso, reduzindo o esforço de criação e manutenção, especialmente quando o diagrama cresce em complexidade.

Também foi explicado que, por ser textual, o Mermaid se integra muito bem a fluxos com IA, já que pode ser gerado e ajustado com pouca fricção, inclusive a partir de documentos como FDDs ou de regras de negócio pontuais. Outro ponto importante foi a renderização direta em Markdown, como em README no GitHub, onde o diagrama aparece no próprio contexto da documentação sem necessidade de gerar imagem, fazer upload ou referenciar arquivos externos. O instrutor contrastou Mermaid com C4, afirmando que C4 é mais adequado para perguntas arquiteturais e representações com níveis bem definidos, fronteiras e convenções claras, enquanto Mermaid é mais eficiente para comunicar rapidamente fluxos, regras e estruturas simples dentro do próprio texto. Ele observou ainda que tentar reproduzir C4 em Mermaid pode até gerar algo visualmente parecido, mas sem preservar fielmente a convenção arquitetural, o que pode comprometer a consistência.

**Pontos de atenção**
- Mermaid é mais indicado para **fluxos, regras e estruturas simples**; não substitui perfeitamente o C4 em cenários arquiteturais formais.
- Ao tentar usar Mermaid para representar um diagrama no estilo C4, o resultado pode **parecer semelhante**, mas **foge da convenção** esperada.
- O grande diferencial do Mermaid está na **simplicidade e baixo atrito**, então ele é mais eficiente quando o custo de manter um diagrama formal seria alto.
- A renderização direta em Markdown depende de o ambiente suportar Mermaid; em contextos compatíveis, isso evita o ciclo de gerar imagem e fazer upload.
- Como o diagrama vira texto, ele deve ser tratado como **artefato versionável e revisável**, aproveitando diff e automação para manter consistência com a documentação.
- O uso com IA é vantajoso, mas requer cuidado para garantir que o diagrama gerado esteja alinhado com a intenção do documento e com a regra de negócio descrita.