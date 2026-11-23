Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16727)

## Resumo da aula

LangSmith não deve ser visto apenas como um repositório de prompts. Dentro do ecossistema da LangChain, ele ocupa a camada operacional de acompanhamento da aplicação, enquanto LangChain e LangGraph ficam mais ligados à construção do fluxo e da lógica de execução. Essa distinção importa porque desenvolver uma aplicação com IA não termina quando o prompt ou o agente funciona localmente; depois disso, ainda é preciso inspecionar execução, custo, falhas e qualidade. O Prompt Hub, já visto antes, é apenas uma das capacidades que aparecem dentro dessa plataforma mais ampla.

LangChain e LangGraph atuam como frameworks para construir aplicações com IA, incluindo agentes e fluxos mais estruturados. Quando o sistema cresce, surge a necessidade de enxergar o que está acontecendo durante a execução real, e é aí que LangSmith entra como suporte de observabilidade e análise operacional. Se o agente foi modelado em grafos com LangGraph, essa necessidade fica ainda mais forte, porque o fluxo passa a ter múltiplos passos, estados e decisões. O valor do LangSmith está em tornar esse comportamento visível e inspecionável.

Observabilidade é a capacidade de entender o comportamento interno de uma aplicação a partir dos sinais que ela produz em execução. Em sistemas com LLMs, isso inclui acompanhar chamadas, entradas, saídas, custo, falhas, tempo de resposta e outros dados que ajudam a explicar por que o sistema se comportou de determinada forma. Sem essa camada, o time enxerga apenas o resultado final e perde contexto para diagnosticar erro, regressão ou desperdício. Em aplicações com IA, observar bem não é um extra: é parte da operação.

Tracing registra o caminho percorrido por uma execução, permitindo inspecionar chamadas e etapas do fluxo em vez de olhar apenas para a resposta final. Isso ajuda a debugar cadeias, agentes e integrações porque mostra onde uma decisão foi tomada, onde houve erro e quanto cada etapa consumiu. Monitoramento complementa esse rastreamento com visão contínua de comportamento, como volume de uso e gasto operacional. Juntos, tracing e monitoramento transformam a execução da aplicação em algo auditável.

Além de observabilidade, LangSmith reúne capacidades como debugging, testes, acompanhamento em equipe e evaluation, que já foi discutida anteriormente. O ponto novo aqui é entender que gestão de prompts aparece como uma função dentro de uma plataforma maior, e não como o produto inteiro. Retomando o cenário dos prompts de aplicação já integrados ao código, agora eles passam a viver em um ambiente que também mede execução, custo e qualidade. Isso muda a forma de operar o prompt: ele deixa de ser apenas um artefato versionado e passa a ser um componente monitorado.

LangSmith é uma ferramenta usada no mercado e tende a aparecer com frequência em ambientes que trabalham com LangGraph ou com aplicações de IA mais estruturadas. A existência de plano gratuito reduz a barreira de entrada para exploração inicial, mas o ponto principal não é comercial: é reconhecer que esse tipo de plataforma atende necessidades reais de desenvolvimento e produção. Quando uma equipe precisa debugar, monitorar e governar comportamento de agentes em operação, soluções desse tipo deixam de ser conveniência e passam a ser infraestrutura.

## Transcrição

00:01

Bom pessoal, então o que eu quero falar rapidamente aqui pra você, porque daí a gente vai ver mais código de como que isso funciona, a gente vai falar rapidamente da Langsmith. Eu já tinha mostrado pra vocês o Hub, mas somente pra você entender como é que isso funciona, tá? Então, basicamente, se você for na LangChain, os caras têm diversos produtos, tá? Então, pelo menos até o momento dessa gravação, pode ser que tenha outros produtos, outras coisas que mudam, mas eles têm dois frameworks que são extremamente importantes, o LangChain e também o LangRef.

00:31

Juntos, esses caras de forma complementares, permite com que você faça desenvolvimento de aplicações com IA, desenvolvimento de agentes e um monte de coisa. Mas, ao mesmo tempo, eles têm a LengSmith e a LengGraph Platform. LengGraph Platform é uma forma de você conseguir ter observabilidade e conseguir entender como você está construindo o seu agente de IA baseado em grafos, que é a forma de como o LengGraph funciona. Mas você vai perceber também que ele tem o LengSmith.

01:00

E esse Langsmith é um cara muito interessante, porque ele permite com que você faça a observabilidade e a evaluação, você conseguir fazer a avaliação, vamos dizer assim, da sua aplicação. Onde eu consigo fazer isso, consigo fazer testes, consigo fazer isso no meu time, consigo debugar, consigo monitorar, consigo ver o quanto eu estou gastando, eu consigo ver muita coisa. Então, ele é realmente uma ótima

01:30

ferramenta pra observabilidade. Você tem tracing das suas chamadas, você consegue gerenciar os seus prompts, você consegue fazer muita coisa. É uma ferramenta realmente bem completa e, obviamente, também nesse mundo, tudo tem seu preço. E eu não tô aqui pra vender Langsmith, mas tem plano gratuito, então...

01:51

faça os seus testes, brinquem. É uma ferramenta de mercado em muitos locais onde você pode chegar a trabalhar. Provavelmente, eles podem também estar utilizando o Langsmith. Inclusive, para desenvolvimento ou em produção, mesmo para desenvolvimento, você vai precisar utilizar, vai ser recomendado você utilizar caso você trabalhe lá em Graph, que é um dos frameworks mais completos e, vamos dizer assim,

02:17

fundamentados, mais estabelecidos nesse mundo de desenvolvimento com o IA, fechou? Então, essa que é a grande sacada aqui do Langsmith, e agora a gente vai entrar na plataforma, você vai ver que ele traz aqui bastante informação do que tem, do que não tem e tudo mais.

02:36

Aqui é mais, vamos dizer, uma página de venda do que qualquer coisa, mas agora, já no nosso próximo vídeo, a gente já vai entrar na interface dela ali. E para você fazer, você vai dar um sign up para fazer o login. Você vai criar uma conta normal, como qualquer um, e depois você já vai entrar na interface que eu vou te mostrar a seguir.

## Resumo IA

**Abreviações**
- **IA** — Inteligência Artificial
- **LLM** — Large Language Model (Modelo de Linguagem de Grande Porte)
- **LangChain** — framework para desenvolvimento de aplicações com IA
- **LangGraph** — framework para construção de agentes e fluxos de execução em grafo
- **LangSmith** — plataforma de observabilidade, avaliação e gerenciamento de aplicações com IA
- **Hub** — repositório/painel de prompts e recursos da plataforma LangChain
- **Tracing** — rastreamento de execuções e chamadas de uma aplicação
- **Evaluation / evaluação** — avaliação de qualidade, comportamento e resultados de uma aplicação

**Resumo**
A aula apresentou o LangSmith como uma plataforma essencial dentro do ecossistema LangChain, destacando que ele não deve ser entendido apenas como um repositório de prompts, mas como a camada operacional responsável por observabilidade, avaliação e acompanhamento de aplicações com IA. O instrutor diferenciou os papéis de LangChain e LangGraph, usados para construir a lógica e os fluxos da aplicação, do LangSmith, que serve para inspecionar o que acontece em tempo de execução. Também foi mencionado o Prompt Hub, mostrado anteriormente, como apenas uma das funcionalidades disponíveis dentro da plataforma mais ampla.

O foco principal da explicação foi mostrar que, ao desenvolver sistemas com LLMs e agentes, não basta fazer o fluxo funcionar localmente: é necessário acompanhar execução, custo, falhas, tempo de resposta, qualidade e comportamento real em produção ou desenvolvimento. Nesse contexto, observabilidade foi definida como a capacidade de entender internamente a aplicação a partir dos sinais gerados durante a execução. O tracing foi apresentado como o mecanismo que registra o caminho percorrido por uma execução, permitindo ver chamadas, etapas e decisões do fluxo, enquanto o monitoramento complementa isso com uma visão contínua de uso e gasto operacional.

O instrutor reforçou que o LangSmith reúne capacidades como debugging, testes, trabalho em equipe, monitoramento e avaliação, tornando a aplicação com IA mais auditável e controlável. A mensagem central foi que prompts deixam de ser apenas artefatos versionados e passam a ser componentes monitorados dentro de um ambiente que mede comportamento e qualidade. Por fim, foi comentado que o LangSmith é uma ferramenta de mercado, frequentemente associada a ambientes que usam LangGraph, e que existe um plano gratuito para experimentação. A aula terminou com a indicação de que, no próximo vídeo, seria mostrada a interface da plataforma após o cadastro e login.

**Pontos de atenção**
- Não tratar o LangSmith como simples “repositório de prompts”; ele cobre observabilidade e operação da aplicação.
- Entender a separação entre:
  - **LangChain/LangGraph**: construção do fluxo e da lógica;
  - **LangSmith**: inspeção, análise e acompanhamento da execução.
- Em aplicações com IA, observar execução, custo, falhas e tempo de resposta é parte da operação, não um extra.
- Usar tracing para depurar o caminho real da execução, e não apenas olhar a resposta final.
- Monitoramento e tracing se complementam: um mostra o percurso da execução, o outro dá visão contínua do comportamento.
- Quando o agente é estruturado em grafos com LangGraph, a necessidade de observabilidade aumenta por causa de múltiplos passos, estados e decisões.
- Prompts devem ser tratados como componentes monitorados dentro do sistema, não apenas como texto versionado.
- Ao avaliar a ferramenta, considerar o plano gratuito para testes, mas lembrar que ela se aplica a cenários reais de desenvolvimento e produção.
- Em equipes, a capacidade de compartilhar testes, debugging e avaliação é importante para governança e qualidade do sistema.