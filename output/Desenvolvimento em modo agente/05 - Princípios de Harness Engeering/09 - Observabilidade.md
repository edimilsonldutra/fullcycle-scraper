Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17893)

## Resumo da aula

Observabilidade fornece evidências operacionais sobre o comportamento real do sistema: logs, métricas e tracing. Em Harness Engineering, isso amplia a avaliação além do resultado funcional e permite verificar requisitos não funcionais, como latência, comportamento sob carga e passagem correta por fluxos instrumentados. Sem esse tipo de dado, o agente só enxerga se “funcionou” localmente, não se o sistema atende às restrições reais de operação.

Retomando a separação entre execução e avaliação já estabelecida, o agente avaliador precisa receber acesso às fontes de observabilidade para validar o que foi executado. Isso inclui consultar logs gerados por testes de carga, ler métricas expostas pela aplicação e inspecionar traces de transações específicas. O harness passa a incorporar não apenas scripts de teste, mas também os canais pelos quais o agente confirma se o comportamento observado está dentro dos parâmetros esperados.

Uma aplicação crítica não pode ser considerada adequada apenas porque funciona na máquina do desenvolvedor. Quando o sistema é submetido a teste de carga, os dados coletados mostram se a latência permanece aceitável, se o comportamento degrada e se os limites operacionais continuam respeitados. O agente usa esses sinais para decidir se a entrega atende aos critérios de qualidade definidos para cenários de uso real.

Lembra dos requisitos de qualidade além da aprovação binária? Aqui eles se estendem ao caminho percorrido por uma transação dentro do sistema. Com OpenTelemetry ou ferramenta equivalente, o agente pode verificar se uma transação passou pelos spans esperados e se a instrumentação do código está produzindo rastros coerentes. Isso permite detectar falhas de integração, trechos não instrumentados e desvios no fluxo interno que não aparecem apenas com testes funcionais.

A stack de observabilidade pode ser disponibilizada junto do ambiente de execução, por exemplo com Elastic Stack rodando em Docker ou com integrações diretas de OpenTelemetry. O ponto central não é a ferramenta específica, mas garantir que logs, métricas e traces estejam acessíveis durante a avaliação automatizada. Quando essa infraestrutura faz parte do harness, requisitos não funcionais deixam de ser verificados só no fim e passam a influenciar a validação desde o desenvolvimento.

Código que passa localmente pode falhar completamente quando exposto a alta concorrência, como um cenário com 100 mil acessos simultâneos. Observabilidade reduz essa falsa confiança porque revela gargalos, aumento de latência e comportamentos anômalos que não aparecem em execuções isoladas. Em sistemas orientados por agentes, ignorar isso produz entregas aparentemente corretas, mas inadequadas para o contexto real de operação.

## Transcrição

00:01

Pessoal, ainda em relação à avaliação, a gente tem parte de observabilidade.

00:07

O que acontece é o seguinte,

00:09

a observabilidade é um dos pilares muito grandes

00:15

quando você está desenvolvendo principalmente sistema de grande porte.

00:18

Você tem que saber logs, métricas, tracing,

00:22

você tem que saber se a sua aplicação está passando em requisitos de carga de teste,

00:28

você tem que garantir... Se o comportamento,

00:31

a latência das coisas que estão acontecendo, das chamadas,

00:35

elas estão dentro dos parâmetros. Você tem que conseguir ter essas informações.

00:39

Então, quando você está pensando em Harness Engineering,

00:41

você também deve, principalmente, sempre depende do contexto,

00:46

ter as stacks de observabilidade plugadas na sua aplicação e fazendo

00:51

com que o agente consiga acessar esses dados para ele verificar.

00:57

Se realmente as coisas estão funcionando. Então, se eu tenho uma aplicação crítica,

01:01

que eu preciso rodar um teste de carga, o que eu posso fazer?

01:05

Eu posso rodar o teste de carga,

01:07

esses logs vão ficar disponíveis para o agente e o agente vai conseguir verificar.

01:11

Ah, eu preciso verificar se eu, por exemplo,

01:14

estou usando o OpenTelemetry e, de repente,

01:16

na hora que ele vai passar por uma determinada transação dentro do sistema...

01:22

para ver se essas transações estão passando por cada parte da stack de tracing,

01:28

ou pelas partes, pelos spans que a gente acaba colocando ali,

01:33

embutido no nosso código. Então, o ponto importante aqui é,

01:37

se você depende de ferramentas de observabilidade,

01:41

se você tem requisitos não funcionais, que eles precisam ser tratados,

01:46

Essas informações precisam estar disponíveis para os agentes. Então, novamente,

01:52

é mais uma coisa que você pode ou eventualmente deve plugar.

01:55

Sei lá, você pode pegar uma Elastic Stack da vida,

01:58

deixar disponível, subir com o Docker. E nesse momento,

02:01

você deixa esses caras rodando. Seu agente tem acesso às métricas,

02:05

os logs, eles conseguem acessar os tracings.

02:07

Ou você faz integrações com OpenTelemetry. Não interessa.

02:10

O ponto é que observabilidade é algo que muitas vezes já está sendo esquecida.

02:16

Na hora de desenvolver com agentes,

02:18

porque não adianta o agente desenvolver seu código e no final,

02:22

quando você for colocar o código no ar,

02:24

ele não atende aos requisitos de qualidade e às

02:28

restrições que você tem por conta de latência,

02:31

por conta de um monte de coisa,

02:33

simplesmente porque a sua máquina funciona,

02:36

mas quando tem 100 mil pessoas acessando aquilo simultaneamente,

02:40

as coisas não vão funcionar.

02:41

Então, a gente não pode pensar e ser ingênuo que essas coisas deixaram de existir.

02:46

Muito pelo contrário,

02:47

elas têm que ser embutidas dentro do seu processo de desenvolvimento

02:51

e, obviamente, nesse caso, dentro do Harness que você está customizando.

## Resumo IA

**Resumo**
A aula destaca a observabilidade como um pilar fundamental para a avaliação de sistemas de software, especialmente em contextos de Harness Engineering e no desenvolvimento de sistemas de grande porte. O principal objetivo é expandir a avaliação de software para além dos resultados funcionais, englobando a verificação de requisitos não funcionais (NFRs), como latência, comportamento sob carga e a correta passagem por fluxos instrumentados.

O instrutor explicou que a observabilidade oferece evidências operacionais sobre o comportamento real do sistema por meio de logs, métricas e tracing. Em Harness Engineering, onde existe uma separação clara entre execução e avaliação, é crucial que o agente avaliador tenha acesso a essas fontes de dados. Isso permite que o harness incorpore não apenas scripts de teste, mas também canais pelos quais o agente pode confirmar se o comportamento observado está dentro dos parâmetros esperados, mesmo sob condições reais de operação ou alta concorrência.

Ferramentas como o OpenTelemetry são exemplificadas para o tracing, possibilitando ao agente verificar se as transações percorrem os "spans" esperados, detectando falhas de integração ou desvios no fluxo interno do sistema. Para cenários de teste de carga, o agente pode consultar logs e métricas geradas para analisar a latência e a degradação do sistema. A stack de observabilidade, que pode ser composta por soluções como Elastic Stack (disponibilizada via Docker, por exemplo) ou integrações diretas com OpenTelemetry, deve ser provida junto ao ambiente de execução. O fluxo da aula enfatiza a necessidade de integrar a observabilidade desde as etapas de desenvolvimento para que os requisitos não funcionais influenciem a validação desde o início, prevenindo problemas em ambientes de produção.

**Pontos de atenção**
*   **Falsa Confiança no Funcionamento Local**: É uma armadilha acreditar que um código adequado porque funciona na máquina do desenvolvedor será robusto em produção. Código que passa localmente pode falhar completamente sob alta concorrência (ex: 100 mil acessos simultâneos).
*   **Subestimar Requisitos Não Funcionais (NFRs)**: Ignorar requisitos como latência, comportamento sob carga e o fluxo interno das transações pode levar a entregas que, embora funcionalmente corretas, são inadequadas para o contexto real de operação.
*   **Esquecimento da Observabilidade**: A observabilidade é frequentemente esquecida no processo de desenvolvimento com agentes, um erro crítico que impede a compreensão do comportamento real do sistema.
*   **Integração Proativa no Harness**: A infraestrutura de observabilidade (logs, métricas, tracing) deve ser parte integrante do harness de avaliação, acessível aos agentes avaliadores desde o desenvolvimento, e não ser uma verificação postergada para as fases finais.
*   **Verificação Aprofundada de Fluxos**: Testes funcionais não são suficientes. É crucial usar tracing (com ferramentas como OpenTelemetry e seus "spans") para verificar o caminho percorrido por uma transação, identificando falhas de integração, trechos não instrumentados ou desvios no fluxo interno do sistema.
*   **Disponibilidade da Stack de Observabilidade**: Garantir que as ferramentas e a infraestrutura de observabilidade (ex: Elastic Stack rodando em Docker) estejam sempre disponíveis e plugadas à aplicação para que os agentes possam acessar os dados necessários para uma avaliação completa e automatizada.