Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17890)

## Resumo da aula

Avaliação é o mecanismo que mede se a saída do agente atende ao padrão esperado de qualidade. Em ambientes com alto throughput de código, gerar software deixa de ser o principal problema; o gargalo passa a ser verificar se o que foi gerado está correto, seguro e alinhado à arquitetura. Por isso, Harness Engineering não termina na execução: ele precisa definir como cada entrega será julgada.

Agentes tendem a superestimar a própria qualidade, o que torna a autoavaliação pouco confiável como critério principal de aceite. Esse comportamento aparece quando o mesmo sistema que gera a solução também tenta julgá-la e acaba validando resultados ruins com excesso de confiança. A consequência prática é simples: geração e avaliação devem ser separadas.

Retomando a ideia de contratos e unidades verificáveis, a revisão mais confiável acontece quando um segundo agente, em outra sessão, avalia o trabalho produzido pelo primeiro. Esse isolamento reduz o viés da autojustificação e força a checagem contra critérios explícitos, em vez de depender da percepção do próprio executor. O harness precisa definir esse contrato de avaliação com clareza suficiente para produzir um resultado verificável.

Quando a produção de código cresce para múltiplos PRs por engenheiro por dia, a capacidade humana de revisar e testar não acompanha o mesmo ritmo. O efeito não é apenas fila acumulada: aumenta também o risco de aprovar mudanças extensas sem inspeção adequada. Nesse cenário, insistir em revisão humana detalhada para toda mudança simples deixa de escalar.

A tendência operacional é reservar revisão humana para mudanças com maior impacto estrutural ou risco sistêmico. Entram nessa categoria decisões arquiteturais novas, criação de camadas e abstrações, alterações de fluxo, dependências, segurança, autenticação, permissões e mudanças de produto. Já tarefas triviais e features sem peso arquitetural tendem a ser validadas por agentes revisores, não por inspeção humana direta.

Em sistemas baseados em IA, avaliação não é um passo informal; ela exige datasets, critérios, processos e rotinas de verificação. Isso transforma avaliação em uma disciplina operacional com custo real de manutenção. Sem esse aparato, o time até consegue gerar saídas rapidamente, mas não consegue afirmar com confiança que elas são boas.

À medida que menos PRs simples passam por revisão humana, o desenvolvedor assume uma função mais próxima de arquitetura e governança. O foco deixa de ser inspecionar manualmente cada detalhe trivial e passa a ser definir direções, estabelecer limites e decidir onde a intervenção humana é obrigatória. Em Harness Engineering, isso significa organizar o ambiente de execução e os mecanismos de avaliação para que a IA produza com velocidade sem comprometer o projeto.

Confiar em agentes para gerar, corrigir e até preparar mudanças para produção deixa de ser hipótese distante e passa a ser uma trajetória operacional plausível. Essa dependência só é sustentável quando o time sabe exatamente em quais pontos sensíveis o humano deve intervir. O problema central não é escolher entre IA ou revisão humana, mas desenhar um sistema em que cada uma atua onde produz mais segurança e mais escala.

## Transcrição

00:01

Bom, pessoal, agora a gente entra num ponto extremamente importante que é avaliação,

00:05

que é a forma de como a gente pode medir a qualidade daquilo que está sendo feito.

00:10

Então, a primeira coisa que a gente tem que se

00:12

ligar é que os agentes não se avaliam bem.

00:16

Muitas vezes também o time não dá vazão

00:20

para conseguir avaliar tão rapidamente aquilo que foi feito.

00:24

Então, vamos falar um pouquinho sobre isso. Olha só o que a Anthropic falou.

00:29

Os agentes são otimistas patológicos. O agente generator,

00:34

que é um agente que eles criaram para fazer o desenvolvimento do software,

00:38

quando ele se avaliou, ele fez até elogio para ele mesmo,

00:42

mesmo quando a qualidade do trabalho era ruim. O pessoal da OpenAI falou,

00:48

conforme o throughput de código aumentou,

00:51

a capacidade humana de testes, vamos dizer assim, virou o gargalo.

00:57

Eles estavam ali com 3,5 PRs por engenheiro por dia numa equipe de 7 pessoas. Ou seja,

01:04

imagina você tendo o código em cima do código sendo gerado e você vai tendo

01:08

um monte de PR para revisar com milhares de linhas de código para pouca gente.

01:13

Então, o que acontece?

01:16

A avaliação ou verificação daquilo que foi feito é tão importante,

01:23

tanto no lado...

01:25

onde você utiliza o próprio LLM como um juiz

01:30

para verificar se aquilo que foi feito está correto,

01:32

mas também ele entra no lado humano quando nós temos que fazer a revisão.

01:38

Então, avaliação é um processo que é uma grande dor,

01:45

e não só na hora que a gente está codificando,

01:47

na hora que você está desenvolvendo agentes em plataformas,

01:50

sistemas que usam IA. Você vai ter que ter datasets,

01:53

você vai ter que ter os seus processos de avaliação e etc.

01:56

E isso aí dá um trabalho danado.

01:59

Então, é importante que você tenha o quê?

02:03

Um processo de avaliação do trabalho.

02:09

Ou seja, você pode ter agentes revisando agentes,

02:14

com humanos entrando apenas em decisões críticas,

02:18

como... Novas decisões arquiteturais com novas camadas, abstrações, fluxo,

02:23

dependência. A gente pode ter ali critérios e mudanças referentes à segurança,

02:28

autenticação, permissão, coisas sensíveis ou até mesmo mudança de produto.

02:32

Então, como que as coisas estão tendendo hoje em dia?

02:36

As tarefas mais triviais e as coisas de features que estão sendo desenvolvidas,

02:41

mas que elas não têm aquele peso arquitetural que não vai mudar o rumo do projeto.

02:47

Normalmente, isso já está sendo feito como? Agente revisando agente. Ou seja,

02:52

é um outro processo e não é o próprio agente que se avalia.

02:56

É um outro agente, numa outra sessão,

02:59

que através de um contrato acaba avaliando o outro agente.

03:02

Agora, os humanos vão entrar na onde?

03:05

Decisão mais crítica. Cada dia você vai ver menos PR sendo validada por humano.

03:12

Mas, obviamente, a gente vai validar e continuar validando muita coisa.

03:16

Mas normalmente a gente vai caindo para camadas mais sensíveis e

03:22

não ficar validando necessariamente uma PR de um CRUD extremamente simples.

03:29

Isso é um ponto polêmico, porque a gente vai depender completamente da IA,

03:35

sair fazendo o código, corrigindo, colocando em produção.

03:38

Na realidade, isso, na minha opinião,

03:40

Pelo menos na hora que eu estou gravando esse vídeo,

03:42

é só uma questão de tempo. A gente já está vendo isso acontecer agora,

03:48

mas cada vez vai ficar mais comum.

03:51

Cada vez mais, todo desenvolvedor hoje tem que ser um arquiteto de software,

03:57

pelo menos para que ele consiga o quê?

04:00

Julgar bem um trabalho, fazer bem uma PR e conseguir...

04:05

organizar toda essa arquitetura,

04:07

organizar toda essa parte de harness para que a IA faça o

04:10

trabalho dela bem feito e que na maioria das vezes,

04:13

se a gente conseguir domar bem ela,

04:16

conseguir trazer as direções, as decisões arquiteturais,

04:19

ela provavelmente vai codificar muito,

04:21

mas muito melhor e muito mais rápido que a gente. Então,

04:24

esse é o grande ponto.

04:26

Nós temos que conseguir criar mecanismos para fazer com que o agente consiga

04:32

avaliar muito bem o agente e nós consigamos também ter uma certeza clara

04:37

de onde a gente tem que entrar e quais são os pontos mais

04:41

sensíveis na hora que a gente vai ter que desenvolver o nosso software.

## Resumo IA

**Abreviações**
*   **PR**: Pull Request - Um pedido formal para incorporar alterações de código de um desenvolvedor para um repositório principal do projeto.
*   **IA**: Inteligência Artificial - Campo da ciência da computação focado em criar máquinas que podem simular a inteligência humana.
*   **LLM**: Large Language Model - Modelo de linguagem grande, um tipo de IA treinado em vastas quantidades de texto para gerar e entender linguagem humana.
*   **CRUD**: Create, Read, Update, Delete - As quatro operações básicas de persistência de dados.

**Resumo**
A aula abordou a avaliação como um mecanismo crucial para medir a qualidade da saída de agentes, especialmente em ambientes com alto volume de código gerado. O objetivo central é reconhecer que, nesses cenários, o gargalo se desloca da geração de software para a verificação de sua correção, segurança e alinhamento arquitetural. Para isso, o Harness Engineering deve ir além da execução, definindo claramente como cada entrega será julgada.

Um conceito fundamental é a separação entre geração e avaliação. Agentes, como o "generator", são "otimistas patológicos" e tendem a superestimar a própria qualidade, tornando a autoavaliação pouco confiável. A revisão mais confiável acontece quando um segundo agente, operando em uma sessão isolada, avalia o trabalho produzido pelo primeiro, seguindo um contrato de avaliação explícito.

Com o aumento exponencial de Pull Requests (PRs) por engenheiro, a capacidade humana de revisar e testar não consegue acompanhar, gerando filas e riscos de aprovação inadequada. A tendência operacional é reservar a revisão humana para mudanças de alto impacto estrutural ou risco sistêmico, como decisões arquiteturais, criação de novas camadas, abstrações, alterações de fluxo, dependências, segurança, autenticação, permissões e mudanças de produto. Tarefas triviais e features sem peso arquitetural são validadas por agentes revisores.

Em sistemas baseados em IA, a avaliação não é um processo informal; exige datasets, critérios, processos e rotinas de verificação, configurando-se como uma disciplina operacional com custo real de manutenção. À medida que menos PRs simples passam por revisão humana, o desenvolvedor assume um papel mais próximo de arquitetura e governança, focando em definir direções, estabelecer limites e decidir onde a intervenção humana é obrigatória, organizando o ambiente de execução e os mecanismos de avaliação para que a IA produza com velocidade sem comprometer o projeto. A dependência crescente da IA para gerar, corrigir e preparar código para produção é sustentável apenas quando o time sabe exatamente em quais pontos sensíveis o humano deve intervir, buscando um sistema onde IA e humanos atuem onde produzem mais segurança e escala.

**Pontos de atenção**
*   **Otimismo patológico dos agentes:** Agentes tendem a superestimar a própria qualidade, validando resultados ruins com excesso de confiança.
*   **Viés da autoavaliação:** A mesma entidade que gera a solução não deve ser a principal responsável por julgá-la. Geração e avaliação devem ser separadas para reduzir o viés da autojustificação.
*   **Gargalo humano na revisão:** Com múltiplos PRs por engenheiro por dia, a capacidade humana de revisar detalhadamente não escala, resultando em filas acumuladas e maior risco de aprovação de mudanças sem inspeção adequada.
*   **Custo da avaliação em sistemas de IA:** A avaliação em ambientes com IA não é um processo trivial; exige investimento em datasets, critérios, processos e rotinas de verificação, representando um custo operacional real.
*   **Contrato de avaliação claro:** O harness precisa definir um contrato de avaliação com clareza suficiente para produzir resultados verificáveis e evitar ambiguidades sobre os critérios de aceitação.
*   **Intervenção humana estratégica:** É fundamental reservar a revisão humana para decisões de alto impacto (arquitetura, segurança, produto) e permitir que agentes revisem tarefas triviais, otimizando o uso dos recursos humanos.
*   **Novo papel do desenvolvedor:** Com a automação da revisão de tarefas simples, o desenvolvedor deve evoluir para uma função mais arquitetural e de governança, focando em definir direções, limites e pontos de intervenção humana, em vez de inspecionar detalhes triviais.
*   **Não é IA *versus* humano:** O desafio não é escolher entre inteligência artificial ou revisão humana, mas projetar um sistema onde cada um atue onde é mais eficaz para garantir segurança e escala.