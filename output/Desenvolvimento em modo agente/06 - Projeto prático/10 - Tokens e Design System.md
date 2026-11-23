Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17973)

## Resumo da aula

Interfaces geradas por agentes ficam mais consistentes quando o projeto fornece artefatos visuais explícitos em vez de depender apenas de descrições textuais. Retomando o uso de guidelines de UI já estabelecido, a aplicação prática aqui é reunir telas-chave — como landing page, login, registro, biblioteca, upload, listagem, detalhes do vídeo e notificações — para servir como referência concreta de layout e estilo. Essas telas não existem para ensinar design do zero, mas para reduzir ambiguidade na execução do front-end. Quanto mais claro for o alvo visual, menor a margem para a IA inventar padrões próprios.

Tokens traduzem a identidade visual em dados reutilizáveis: cores, tons, tipografia, estados, espaçamentos, posições, botões, ícones e outros detalhes de interface. Em vez de pedir que a IA “faça algo parecido”, o projeto entrega um vocabulário visual estruturado que pode ser aplicado de forma repetível em diferentes telas. Isso aumenta a assertividade porque decisões de UI deixam de ser implícitas e passam a ser parametrizadas. O Design System vira, na prática, uma fonte operacional de verdade para implementação.

Colocar essas referências e tokens dentro da pasta de design system da documentação transforma o material visual em contexto acessível durante o desenvolvimento. A IA consegue consultar esse conjunto como parte do ambiente do projeto, do mesmo modo que consulta regras arquiteturais e convenções já definidas em outros arquivos. O ganho principal não é estético; é operacional, porque a implementação passa a seguir um padrão verificável e menos sujeito a deriva visual. Essa externalização também facilita manutenção e evolução da interface ao longo do tempo.

Screenshots ajudam a IA a comparar o que foi implementado com uma imagem de referência e iterar até chegar mais perto de um resultado pixel perfect. Essa abordagem funciona bem como mecanismo de comparação visual, mas é menos estruturada do que fornecer tokens e especificações explícitas. Quando os tokens já estão definidos, a IA não precisa inferir cor, fonte, estado ou espaçamento a partir de imagem; ela apenas aplica o sistema visual documentado. Por isso, screenshots são úteis, mas tokens tendem a escalar melhor como instrução recorrente.

As instruções de front-end ficam mais eficazes quando o AGENTS.md aponta explicitamente para os tokens e para as referências das páginas existentes. Em vez de deixar a IA decidir livremente como compor uma nova tela, o arquivo instrui que toda implementação visual use o Design System já documentado. Isso conecta guidance contextual com artefatos concretos do projeto, reforçando a consistência entre diferentes tarefas. O resultado é um fluxo em que a IA recebe não só a tarefa, mas também o repertório visual autorizado para executá-la.

A estratégia não depende de uma ferramenta específica de design. Cloud AI Design, Figma ou qualquer outra solução servem desde que permitam extrair telas de referência e tokens de forma organizada. Em ambientes corporativos, esse insumo normalmente vem do designer; em contextos menores, pode ser produzido pelo próprio desenvolvedor. O ponto central é formalizar a identidade visual para que a IA implemente interfaces com menos inferência e mais consistência.

## Transcrição

00:00

Bom, pessoal, seguinte, tá?

00:03

Aqui tá a interface que eu criei, entre aspas,

00:08

tá? Eu tô utilizando o Cloud Design, tá?

00:11

Que é uma ferramenta da própria Anthropic pra você fazer o design da sua aplicação. Basicamente,

00:17

o que eu fiz foi, eu peguei a aplicação antiga que a gente fez,

00:20

importei no Cloud Design e pedi pra ele gerar algumas opções de design pra mim. Ou seja,

00:26

eu fiz isso de uma forma extremamente simples. Rápida,

00:28

porque o nosso objetivo aqui não é ensinar front-end pra você,

00:32

como você cria um design,

00:34

mas basicamente o que eu queria é ter componentes visuais

00:39

simples e fáceis pra que a IA conseguisse ler e seguir,

00:43

tá? Então, eu pedi pra ela criar o componente nas principais páginas,

00:48

então, basicamente, landing page, ela criou dessa forma.

00:52

A tela de login dessa forma aqui. A parte de registro,

00:57

né? Register dessa forma. A parte de biblioteca assim.

01:01

A parte de upload dessa forma aqui.

01:05

A parte de biblioteca com listagem dessa forma.

01:09

Os detalhes do vídeo, assim como é que eles acabaram ficando.

01:13

E aqui quando aparecem as notificações ali do lado, tá? Então, basicamente,

01:18

essas aqui são as páginas que eu pedi para ela criar,

01:22

para a nossa IA utilizar ali como referência visual. Então,

01:28

isso aí é um ponto importante quando a gente está trabalhando com front-end.

01:32

Eu não quero gastar, vamos dizer aqui, o nosso tempo inteiro falando sobre isso,

01:36

mas somente para você saber que eu tenho um arquivo desse e

01:39

eu vou colocar dentro da nossa pasta ali de design system,

01:43

dentro das nossas documentações, para ela conseguir andar com isso.

01:49

Outra coisa que eu fiz aqui também...

01:51

foi pedir para ela gerar os tokens do projeto. Ou seja,

01:56

com todas as cores, os tons, as fontes e etc.

02:03

Então, basicamente, ele colocou os tokens, as cores,

02:07

os status, como é que funcionam as posições, os botões. Então, se você perceber,

02:14

ele trouxe todos esses componentes aqui separados para mim.

02:18

De como que isso vai funcionar,

02:19

tudo bonitinho, pra que eu consiga utilizar isso da melhor forma possível,

02:25

em relação à parte dos ícones, os detalhes. Então, tudo isso aqui, tá?

02:31

Ele trouxe aqui pra me ajudar ali no dia a dia, tá? Então,

02:35

isso aí é um aspecto importante também que eu vou colocar ali como token,

02:39

essa parte no Design System, pra ajudar pra ele ser muito assertivo.

02:43

O que funciona muito com o IA também é você pegar os screenshots,

02:46

ele consegue, ele é muito bom em pegar o screenshot,

02:49

olhar como é que está aquela imagem e comparar aquilo que ele

02:52

fez e ele ficar tentando arrumar até tentar deixar mais pixel perfect,

02:57

tá? Mas eu prefiro muito mais ele conseguir trabalhar dessa forma aqui.

03:01

Você já dá todos os tokens,

03:03

você já deixa tudo bonitinho e daí ele consegue ler

03:06

todos esses tipos de coisa e é obviamente...

03:09

a gente vai colocar isso também no nosso agents.md, falando, olha,

03:13

toda vez que você for mexer com front-end, for criar alguma tela e etc.,

03:16

utilize esses tokens e aqui estão os detalhes das outras páginas das implementações.

03:21

Então isso aí é um ponto super importante e

03:23

Você pode usar isso em qualquer plataforma.

03:27

Eu fiz aqui usando o Cloud AI Design,

03:30

mas você pode utilizar o Figma, a ferramenta que você quiser.

03:35

Dentro da sua empresa, provavelmente você tem um designer lá muito bom,

03:38

Esse cara vai te ajudar, ou se você é o designer,

03:40

O importante é você conseguir extrair,

03:42

Gerar todos os tokens, toda a identidade visual,

03:45

Pra ficar muito mais consistente tudo que a IA vai desenvolver dali pra frente.

## Resumo IA

**Abreviações**
*   **IA**: Inteligência Artificial
*   **UI**: User Interface

**Resumo**
O objetivo da aula é demonstrar como garantir interfaces de usuário (UI) mais consistentes e reduzir a ambiguidade na execução de front-end, especialmente quando se trabalha com agentes de Inteligência Artificial (IA). O instrutor enfatiza a importância de fornecer artefatos visuais explícitos em vez de depender apenas de descrições textuais.

Os conceitos abordados incluem:
1.  **Telas-chave como referência**: A criação ou compilação de telas essenciais da aplicação (como landing page, login, registro, biblioteca, upload, listagem, detalhes do vídeo e notificações) que servem como exemplos concretos de layout e estilo. Essas telas são utilizadas para guiar a IA, minimizando a margem para a criação de padrões próprios.
2.  **Tokens de design**: A tradução da identidade visual do projeto em dados reutilizáveis, como cores, tons, tipografia, estados, espaçamentos, posições, botões e ícones. Esses tokens formam um vocabulário visual estruturado que pode ser aplicado de forma repetível, tornando as decisões de UI parametrizadas e assertivas, transformando o Design System em uma fonte operacional de verdade.
3.  **Documentação**: A prática de incluir essas referências visuais e tokens dentro de uma pasta de `design system` na documentação do projeto, tornando-os acessíveis para a IA consultar durante o desenvolvimento, assim como outras regras arquiteturais.
4.  **Screenshots**: Embora úteis para a IA comparar o que foi implementado com uma imagem de referência e iterar em busca de um resultado "pixel perfect", são menos estruturados do que tokens. Tokens são preferidos por serem mais escaláveis e permitirem que a IA aplique o sistema visual documentado diretamente, sem necessidade de inferência.

O fluxo explicado pelo instrutor envolveu a criação dessas referências utilizando o Cloud AI Design (mencionando Figma como alternativa), onde ele gerou as telas principais e os tokens do projeto. Em seguida, ele destacou que esses artefatos devem ser colocados na pasta de `design system` da documentação. Por fim, o arquivo `AGENTS.md` deve ser instruído explicitamente para que a IA, ao lidar com tarefas de front-end ou criação de novas telas, utilize sempre os tokens e as referências visuais já documentadas, conectando a orientação contextual com os artefatos concretos do projeto. A estratégia é independente da ferramenta de design utilizada, focando na formalização da identidade visual para maior consistência.

**Pontos de atenção**
*   **Forneça artefatos visuais explícitos**: Evite depender apenas de descrições textuais para a IA, pois isso leva à inconsistência e à criação de padrões próprios pela IA.
*   **Utilize telas-chave como referência concreta**: Reúna telas essenciais para servir como um alvo visual claro para a implementação do front-end.
*   **Formalize a identidade visual com tokens**: Traduza cores, tipografia, espaçamentos, estados e outros detalhes em tokens reutilizáveis. Isso aumenta a assertividade e torna as decisões de UI parametrizadas.
*   **Design System como fonte de verdade**: Os tokens e referências visuais devem ser organizados em um Design System documentado, que serve como guia operacional para a implementação.
*   **Externalize referências na documentação**: Coloque os artefatos visuais (telas de referência, tokens) na pasta de `design system` da documentação para que a IA possa consultá-los como parte do ambiente do projeto.
*   **Foco operacional, não apenas estético**: O principal ganho dessa abordagem é operacional, resultando em uma implementação que segue um padrão verificável e é menos suscetível a desvios visuais.
*   **Tokens são mais escaláveis que screenshots**: Enquanto screenshots são úteis para comparação "pixel perfect", os tokens fornecem instruções mais estruturadas e escaláveis para a IA, evitando que ela precise inferir estilos a partir de imagens.
*   **Instruções claras no `AGENTS.md`**: O arquivo de instruções para agentes deve apontar explicitamente para os tokens e as referências das páginas existentes, garantindo que toda nova implementação visual siga o Design System documentado.
*   **Ferramenta é secundária, formalização é primordial**: A estratégia não depende de uma ferramenta de design específica (Cloud AI Design, Figma, etc.). O ponto central é a capacidade de extrair telas e tokens de forma organizada e formalizar a identidade visual.
*   **Responsabilidade pela criação**: Em ambientes corporativos, designers geralmente fornecem esses insumos; em contextos menores, o próprio desenvolvedor pode produzi-los, desde que a identidade visual seja formalizada.