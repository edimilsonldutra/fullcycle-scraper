Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17130)

## Resumo da aula

ADR continua valendo porque preserva o racional das decisões e torna a timeline arquitetural legível ao longo do tempo. O ganho estratégico aparece quando o documento deixa de ser um registro isolado e passa a sustentar entendimento compartilhado sobre por que o sistema evoluiu de determinada forma. Isso reduz perda de contexto entre pessoas, times e ciclos de mudança. Em ambientes com alta rotatividade ou múltiplos stakeholders, essa memória explícita vira ativo de engenharia.

A adoção mais útil não é gerar ADRs manualmente de forma esporádica, mas integrar sua criação ao workflow normal de desenvolvimento. Quando uma nova feature introduz uma decisão estrutural relevante, o pipeline pode disparar análise, rascunho documental e revisão, em vez de depender apenas da disciplina individual do time. Retomando a timeline arquitetural já estabelecida, o valor novo aqui é a continuidade: a documentação passa a nascer junto com a evolução do sistema. Isso transforma ADR em prática recorrente, não em esforço de recuperação tardia.

No contexto de automação documental com IA, prompt deixa de ser instrução informal e passa a funcionar como mecanismo de controle do comportamento do sistema. Ele define escopo, formato, critérios de evidência, estilo de saída e limites de inferência, influenciando diretamente a qualidade do resultado. Chamar prompt de “nova linguagem de programação” faz sentido aqui porque parte da lógica operacional migra da implementação tradicional para a especificação intencional do que o agente deve fazer. O trabalho não desaparece; ele muda de forma e exige precisão editorial e técnica.

Automatizar ADR com IA não significa obter documentação perfeita em qualquer projeto. O processo continua trabalhoso, depende de contexto suficiente e sofre com diferenças de maturidade entre codebases, times e acervos documentais. Como os limites da automação já foram estabelecidos anteriormente, o ponto central agora é postura operacional: usar a IA como ponto de partida confiável o bastante para acelerar o trabalho, sem delegar a ela a validação final do racional arquitetural. A revisão humana continua sendo a etapa que transforma draft em memória técnica confiável.

A adoção prática começa quando o time traz esse contexto para dentro da empresa, em vez de esperar uma solução universal pronta. Isso pode significar alimentar a IA com documentos internos, conectar o processo ao fluxo de feature, envolver liderança técnica e ajustar o nível de formalização ao tipo de sistema. O objetivo não é copiar um modelo fechado, mas adaptar o workflow ao ambiente real de consultoria, produto ou plataforma. A utilidade cresce quando o processo conversa com a cultura e com as restrições da organização.

Documentação continua sendo uma dor porque exige esforço contínuo, mas seu valor aumenta quando ela melhora comunicação, qualidade e velocidade de desenvolvimento. Informações arquiteturais bem registradas evitam reinterpretação constante de decisões antigas e reduzem o custo de entender o sistema em momentos de mudança. Para desenvolvedores, tech leads e diretores, isso significa menos dependência de memória informal e mais previsibilidade na evolução técnica. Quando essas informações ficam acessíveis também para IA, o ganho se estende à recuperação de contexto e ao suporte à decisão.

Nenhum workflow de ADR com IA nasce pronto; ele precisa ser tratado como processo iterativo. O time começa com um ponto de partida imperfeito, observa onde a geração falha, ajusta prompts, melhora fontes de contexto e refina critérios de uso. Esse ciclo de revisão é o que torna a prática sustentável no longo prazo. A maturidade não vem de acertar tudo no início, mas de melhorar continuamente a qualidade documental sem abandonar a governança.

## Transcrição

00:01

Bom, pessoal, eu acho que deu pra falar bastante de ADR. Eu sei que, às vezes, muita gente pode gostar ou não gostar, mas é um dos documentos que ajudam muito, realmente, a gente ver a timeline do nosso projeto e entender porque as coisas aconteceram, tá? E uma vez que nós, hoje em dia, temos a IA como aliada,

00:26

fazer esses tipos de coisa que eu acabei mostrando para vocês, cada dia começa a fazer mais sentido. Porque você vai poder usar, a IA vai poder usar, você pode colocar esses documentos dentro de um workflow, onde essas ADRs podem ser geradas automaticamente conforme você cria novas features no sistema. Então, o céu é o limite, pessoal. Como eu disse para vocês, pode parecer só prompt,

00:55

Mas esse só prompt é a nova linguagem de programação.

01:02

Eu não consigo imaginar alguns anos atrás que a gente seria capaz de gerar coisas dessa forma. Assim, dá trabalho? Dá. É complexo? É. Tem como melhorar muito? Tem. Provavelmente vai funcionar perfeito em todos os projetos? Não. Mas é um ponto de partida. E o que eu queria aqui nesse momento é conseguir te provocar pra você tentar fazer coisas dessas parecidas na sua empresa.

01:28

Começar a trazer isso como contexto para o seu I.A. Trazer isso para o seu time. Eu não tenho dúvidas como o nível de comunicação, qualidade, desenvolvimento, produtividade vai aumentar, tá? Porque essas informações valem ouro. Essas informações. Você pode estar trabalhando numa consultoria, você pode ser desenvolvedor, você pode ser tech lead, você pode ser diretor.

01:54

Documentação sempre foi uma dor, e ela continua sendo uma dor, mas agora a gente consegue gerenciar isso melhor. E eu realmente, de coração, espero que você tenha gostado desse capítulo. É algo denso, é bastante falação, a gente não fica programando, muitas vezes a gente quer programar, mas eu espero que...

02:16

você tem entendido o nível de relevância e a importância que a gente tem que ter para trabalhar com esses tipos de documento e o mais interessante entender o projeto que você trabalha de uma forma como você nunca imaginou que você ia entender. Maravilha? Espero que você tenha curtido, grande abraço aí para vocês e até a próxima!

## Resumo IA

**Abreviações**
- **ADR** — *Architecture Decision Record* (Registro de Decisão Arquitetural)
- **IA** — Inteligência Artificial
- **workflow** — fluxo de trabalho

**Resumo**
A aula reforça a importância dos ADRs como documentos que preservam o racional das decisões arquiteturais e mantêm a timeline do projeto compreensível ao longo do tempo. O instrutor destaca que esse tipo de registro evita a perda de contexto entre pessoas, times e ciclos de mudança, funcionando como memória explícita da evolução do sistema. Em vez de tratar ADR como um artefato isolado ou produzido apenas manualmente em momentos pontuais, a proposta é integrá-lo ao workflow normal de desenvolvimento, especialmente quando novas features geram decisões estruturais relevantes.

Na sequência, a aula mostra como a IA pode ser usada para automatizar parte desse processo documental. O prompt é apresentado como um mecanismo de controle do comportamento do sistema, definindo escopo, formato, critérios de evidência, estilo de saída e limites de inferência — quase como uma nova linguagem de programação para especificar o que o agente deve fazer. Ainda assim, o instrutor deixa claro que a automação não elimina o esforço: ela depende de contexto suficiente, varia conforme a maturidade do projeto e não substitui a revisão humana. O fluxo sugerido é usar a IA como ponto de partida para gerar drafts, inserir isso no processo de desenvolvimento da empresa, alimentar o sistema com documentos internos e ajustar a abordagem à realidade de cada time, produto ou consultoria. Por fim, a aula enfatiza que esse workflow deve ser iterativo, melhorando continuamente prompts, fontes de contexto e critérios de uso até se tornar sustentável.

**Pontos de atenção**
- ADR não deve ser tratado como documento decorativo; ele precisa preservar o porquê das decisões.
- A documentação perde valor quando fica desconectada do fluxo real de desenvolvimento.
- Automatizar ADR com IA não garante qualidade perfeita; o resultado depende de contexto e maturidade do projeto.
- O prompt precisa ser escrito com precisão técnica e editorial, pois ele controla diretamente a saída do agente.
- A IA deve atuar como apoio inicial, não como responsável pela validação final do racional arquitetural.
- A revisão humana continua obrigatória para transformar o rascunho em memória técnica confiável.
- Não existe solução universal pronta: o workflow precisa ser adaptado à cultura, às restrições e ao tipo de sistema da organização.
- É importante envolver o time e a liderança técnica para incorporar o processo de forma efetiva.
- Documentação é uma dor contínua; o ganho vem de melhor comunicação, qualidade, velocidade e previsibilidade.
- O processo deve ser iterativo: começar imperfeito, identificar falhas, ajustar prompts, melhorar contexto e refinar critérios.
- A governança não pode ser abandonada em nome da automação.
- Quanto melhor a base documental, maior o benefício tanto para pessoas quanto para ferramentas de IA no suporte à decisão.