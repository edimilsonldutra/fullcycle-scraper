Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16621)

## Resumo da aula

Validar a saída de um prompt operacional significa comparar o que foi pedido com o que apareceu no relatório. A verificação não depende de a resposta parecer “boa”, mas de ela cobrir os blocos esperados com utilidade técnica para decisão. Retomando o agente auditor de dependências, o relatório confirma a eficácia do prompt quando entrega seções acionáveis como sumário, achados principais, issues críticas, análise de risco e plano de ação. Se a saída vier genérica, sem evidência de leitura dos arquivos do projeto, o prompt não cumpriu bem seu objetivo.

O idioma do prompt e o idioma da resposta não precisam ser os mesmos. Em muitos casos, prompts em inglês produzem respostas mais consistentes porque o modelo costuma ter mais dados de treinamento nesse idioma, mas isso não elimina o uso de português no trabalho diário. Uma estratégia prática é escrever o prompt no idioma em que você formula melhor a instrução e, se necessário, traduzir depois com revisão humana para evitar perda de nuance. Outra opção é manter o prompt em um idioma e explicitar no final que o relatório deve ser gerado em outro.

O sumário é a primeira prova de que o agente entendeu o contexto do projeto, porque ele sintetiza stack, objetivo do sistema, quantidade de dependências e condição geral da base. Já Key Findings concentra os achados mais relevantes, funcionando como uma triagem executiva do relatório. Quando essas seções mencionam elementos concretos como Python, Google ADK, requirements.txt, ausência de lockfile e vulnerabilidades específicas, a saída deixa de ser abstrata e passa a refletir a codebase analisada. Isso reduz o esforço de leitura e acelera a decisão sobre prioridade técnica.

Lockfiles registram a resolução exata das versões instaladas, não apenas a intenção declarada no manifesto. Sem esse arquivo, o mesmo projeto pode instalar versões diferentes em momentos distintos, o que aumenta risco de inconsistência entre desenvolvimento, CI e produção. No caso de requirements.txt, a ausência de lockfile indica menor reprodutibilidade do ambiente e dificulta auditoria confiável do que realmente foi instalado. Por isso, a menção explícita a no lockfiles present é um achado operacional importante, não um detalhe cosmético.

Uma dependência pinada fixa uma versão exata, como 1.0.2, impedindo upgrades implícitos durante nova instalação. Isso aumenta previsibilidade e ajuda a evitar que uma atualização externa quebre o software sem mudança no código do projeto. Já dependências não pinadas deixam margem para resolver versões mais novas no futuro, o que pode introduzir incompatibilidades, regressões ou mudanças de comportamento. Quando o relatório aponta mistura entre dependências pinadas e não pinadas, ele está sinalizando risco de estabilidade e dificuldade de reprodução.

Critical Issues é a seção em que o relatório transforma achados dispersos em problemas que exigem atenção imediata. Vulnerabilidades em pacotes centrais como LiteLLM, Pydantic ou Pandas ganham prioridade porque afetam partes relevantes do sistema e podem comprometer segurança, compatibilidade ou manutenção. A presença de dependências depreciadas e possíveis typos também entra aqui quando o impacto operacional é alto. Essa seção só é útil quando aponta o problema de forma específica, sem inflar severidade com afirmações vagas.

Análise de risco não é apenas repetir que existe uma vulnerabilidade; é explicar a consequência provável para o projeto. O relatório agrega valor quando relaciona dependências problemáticas a cenários como quebra em produção, exposição de credenciais, falhas de autenticação ou ingestão de conteúdo malicioso. Esse vínculo entre pacote e impacto permite priorizar correções pelo dano potencial, e não apenas pela existência do problema. Em auditoria técnica, risco bem descrito é o que transforma inventário em decisão.

Arquivos críticos são os pontos da codebase mais sensíveis aos problemas encontrados nas dependências. Quando o relatório destaca agent.py e .env, ele não está apenas listando arquivos: está indicando onde o impacto operacional tende a se concentrar, seja no core do workflow, seja em configuração e credenciais. Essa leitura é especialmente útil em agentes que interagem com GitHub, Discord ou logs externos, porque combina dependências vulneráveis com superfícies reais de execução. O resultado esperado é uma investigação mais direcionada, em vez de uma revisão difusa da base inteira.

Integration Notes resume como os pacotes se conectam ao sistema e quais integrações merecem atenção adicional. Essa seção ajuda a entender por que determinada dependência importa além do número da versão, mostrando seu papel no fluxo do agente e nas integrações externas. Em vez de tratar bibliotecas como itens isolados, o relatório passa a enxergá-las como parte de um circuito de execução. Isso melhora a leitura arquitetural do risco.

A leitura prática do relatório segue uma ordem simples: confirmar o contexto no sumário, verificar os achados prioritários em Key Findings, inspecionar Critical Issues, interpretar a análise de risco e localizar os arquivos críticos afetados. Retomando o prompt estruturado já definido antes, cada uma dessas seções corresponde a um bloco que foi explicitamente solicitado, então a validação consiste em checar se o agente realmente materializou esse contrato. O plano de ação entra no final como consequência da leitura, não como ponto de partida. Se ele recomenda corrigir typo, atualizar LiteLLM, Pydantic e Pandas, adicionar lockfile, forçar versões e revisar .env, então a saída está conectando achado, impacto e próxima ação de forma coerente.

## Transcrição

00:01

Bom, pessoal, no vídeo anterior a gente ficou explicando e falando sobre o prompt e aquela estrutura que a gente seguiu. Agora, o negócio aqui é o seguinte. Aqui é um exemplo de um resultado de...

00:16

quando eu rodei esse prompt dentro de um CodeBase que eu tinha aqui comigo. Somente a gente vai olhar isso aqui, somente para você ter uma ideia de como ele gerou. Mas depois, em seguida, o que eu vou fazer? Eu vou mostrar para você um prompt bem pequeno de um comando do Cloud Code. E lembrando pessoal, talvez na hora que você esteja vendo esse vídeo, o Cloud Code tenha mudado o formato de trabalho,

00:42

ou talvez ele esteja de uma forma diferente, ou qualquer coisa desse tipo, mas a ideia principal aqui não é focar na ferramenta Cloud Code, ou no Gemini, ou nas ferramentas do Codex da OpenAI, ou qualquer coisa desse tipo, mas sim pensar em como o Prompt pode afetar, beleza? Então, aqui é um resultado daquele report. Você deve também estar se perguntando, Wesley, por que você fez aquele report inteiramente em inglês? Normalmente,

01:11

A IA tende a trazer resultado um pouco melhor, ou às vezes, dependendo da situação, bem melhor em inglês, porque ela tem mais treinamento em inglês. Por outro lado, eu vou deixar isso bem claro para você.

01:28

No meu dia a dia, por muitas e muitas vezes, quando eu vou criar um prompt, normalmente eu faço esse prompt em português, e na maioria das vezes isso funciona, eu escrevo muito mais rápido, meu português é muito melhor para eu escrever do que o meu inglês e tudo mais, tá?

01:44

O que eu também faço, dependendo de como eu vou distribuir, ou caso eu queira emprestar, ou dar esse prompt para alguém, ou na empresa que essa pessoa trabalhe, eles trabalhem só com inglês, eu simplesmente vou e traduzo usando o próprio IA, o meu prompt de português para inglês, e, obviamente, aí você tem que passar um pente fino para evitar qualquer mal-entendido, até mesmo nesses tipos de tradução. Então, por isso que você está vendo todos esses resultados que a gente colocou.

02:14

em inglês. Uma outra coisa que a gente pode fazer é, no final do prompt, falar para ele gerar o relatório completamente em português. Talvez seja uma outra solução aqui também para a gente. A gente pode até testar isso depois. Então, basicamente, eu vou mostrar aqui o report que ele gerou nesse codebase.

02:36

Então, ele trouxe aqui, ó, Dependency Audit Report, aqui o sumário, ou seja, o resumo, eu poderia colocar para ele colocar a data que eu gerei aqui também, logo lá nas instruções, e aqui ele está falando que eu tenho um projeto de agentes baseado em Python,

02:52

criado em cima do Google ADK, que implementa a verificação de bugs e criar issues no GitHub no formato de uma pipeline. Esse projeto tem 11 dependências diretas espalhadas no requirements.txt com no-lock files present, ou seja, eu não tenho um arquivo ali locado

03:17

do requirements.txt. Enquanto as dependências geralmente são bem mantidas, a gente tem algumas vulnerabilidades de segurança e versões que foram identificadas. Então, aqui ele trouxe para mim Key Findings, ou seja, aqueles encontros, aqueles achados que ele acabou de fazer.

03:37

Então, ele colocou aqui uma vulnerabilidade crítica de segurança e ele trouxe aqui baseado no LightLLM. LightLLM é um pacote que você usa para você utilizar qualquer modelo de inteligência artificial, independente se você está rodando com ADK, por exemplo. Ele achou seis...

03:55

dependências críticas de vulnerabilidade, uma dependência que pode estar escrito, um problema de type, ou seja, ela foi escrita de forma errada ou ela não está sendo utilizada no projeto, não encontrou nenhum lockfile que pode gerar problemas na hora que eu for colocar em produção, porque os lockfiles são aqueles caras que realmente garantem qual é a versão exata que está sendo utilizada e tudo mais, tipo um

04:21

um package, .loc, quando a gente está trabalhando, e versões misturadas de especificações de padrões, algumas pinadas ou não pinadas.

04:37

Ah, e só para ficar mais claro, o que é pinado e não pinado? Quando tenho uma dependência pin, significa que essa dependência tem a versão exata de qual ela está sendo utilizada. Ou seja, se houver alguma nova versão dessas dependências, não é feito o upgrade porque você tem exatamente a versão, tipo 1.0.2.

05:01

Mas aqui também eu tenho dependências que eu não tenho isso, então só está o nome da dependência. Significa que se em algum momento houver uma atualização, isso vai ser feito e talvez possa quebrar o meu software. Então isso é importante. E aqui ele trouxe os critical issues do que está acontecendo e principalmente no

05:22

no LightLLM, que ele tinha falado bastante, achou no Pydent, que também, no Pandas, ele trouxe dependências depreciadas aqui, onde ele achou, e ele falou aqui, pode ter um problema de typo ou você tem que verificar o nome do pacote para ver se realmente está certo. Daí, ele trouxe aqui a lista de dependências que eu tenho, e quais são as dependências que estão

05:46

desatualizadas e coisas desse tipo. Aí ele trouxe pra mim uma análise de risco, falando o que pode acontecer com essas dependências aqui pra mim. Dependências sem ser verificadas, ele repetiu aqui, por conta daquela que pode estar algum erro.

06:02

E aqui ele começou a trazer para mim os arquivos que têm mais criticidade em relação às dependências. Então, ele trouxe aqui o agent.py, ou seja, basicamente ele pegou todos os arquivos principais de agentes que estão utilizando pontos do Google ADK, o python.env, ou seja, ele pegou os arquivos mais críticos que são afetados por essas dependências aqui. E ele fala o porquê, né?

06:28

porque eles usam isso como o core do workflow do meu agente, ele usa informação sensitiva, sensível, porque ele cria uma issue no GitHub e tem acesso ao Discord, ele tem vulnerabilidades de autenticação e configuração, ele também acessa logs externos que possam conter conteúdos maliciosos.

06:52

E aí ele traz aqui o integration notes, falando o que eu estou utilizando e os principais pacotes aqui para mim, né? E o meu plano de ação aqui, imediato, que eu devo ter para tentar resolver esse meu problema. Ou seja, resolver o nome daquele pacote, fazer o update do Lite LLM, atualizar o Pydentic, atualizar o Pandas, colocar um lockfile, forçar as versões, verificar as minhas variáveis de ambiente, o .env, para evitar,

07:19

E aqui ele trouxe um monte de coisa para eu fazer. Então, no final das contas, pessoal, esse foi o resultado do relatório que eu consegui, baseado naquele prompt que a gente acabou colocando e trabalhando. Próximo vídeo eu vou mostrar isso aqui na prática para vocês.

07:40

Vou mostrar também como que eu fiz para invocar esse relatório, ou seja, esse tipo de dependência aqui pra gente. Beleza? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **AI / IA** — Inteligência Artificial  
- **ADK** — Agent Development Kit  
- **CI** — Integração Contínua  
- **CI/CD** — Integração Contínua / Entrega Contínua  
- **Codebase** — Base de código  
- **Discord** — Plataforma de comunicação usada aqui como integração externa  
- **GitHub** — Plataforma de hospedagem e colaboração de código  
- **IA** — Inteligência Artificial  
- **LLM** — Large Language Model (Modelo de Linguagem de Grande Porte)  
- **Pandas** — Biblioteca Python para manipulação e análise de dados  
- **Pydantic** — Biblioteca Python para validação e serialização de dados  
- **Python** — Linguagem de programação Python  
- **requirements.txt** — Arquivo de dependências do Python  

**Resumo**  
A aula mostrou como validar a saída de um prompt operacional comparando o que foi solicitado com o que de fato apareceu no relatório gerado por um agente de auditoria de dependências. O instrutor reforçou que a avaliação não deve se basear em “parecer bom”, mas em cobrir corretamente blocos acionáveis como sumário, achados principais, issues críticas, análise de risco, arquivos críticos, notas de integração e plano de ação. O exemplo apresentado foi um relatório de auditoria aplicado a uma codebase em Python, construída com Google ADK, onde o agente identificou a quantidade de dependências, problemas de reprodutibilidade por ausência de lockfile, mistura entre dependências pinadas e não pinadas e vulnerabilidades relevantes em pacotes como LiteLLM, Pydantic e Pandas.

Também foi explicado que o idioma do prompt e o idioma da resposta podem ser diferentes. O instrutor observou que, em muitos casos, prompts em inglês tendem a gerar respostas mais consistentes por causa do volume de treinamento do modelo, mas que no dia a dia ele costuma escrever prompts em português por rapidez e clareza. Quando necessário, ele traduz o prompt com apoio de IA e faz revisão humana para evitar perda de nuance. Outra alternativa citada foi instruir diretamente o agente para gerar o relatório em português.

Na análise do relatório, o sumário confirmou o contexto técnico do projeto e os Key Findings concentraram os achados mais importantes, como vulnerabilidades críticas, ausência de lockfile e possíveis typos ou dependências mal declaradas. O instrutor explicou a diferença entre dependências pinadas, que fixam versões exatas, e não pinadas, que permitem upgrades implícitos e podem causar quebra de compatibilidade. Em seguida, ele mostrou que a seção de Critical Issues transforma achados em problemas prioritários, enquanto a análise de risco traduz vulnerabilidades em impactos prováveis, como falhas em produção, problemas de autenticação, exposição de credenciais ou ingestão de conteúdo malicioso. Por fim, o relatório destacou arquivos mais sensíveis, como agent.py e .env, apontou notas de integração para contextualizar o papel dos pacotes no fluxo do sistema e fechou com um plano de ação imediato, incluindo correção de nome de pacote, atualização de dependências, criação de lockfile, fixação de versões e revisão das variáveis de ambiente.

**Pontos de atenção**  
- Validar o prompt pela cobertura dos blocos esperados, não pela “qualidade estética” do texto.  
- Verificar se o relatório contém evidências concretas da codebase analisada, e não apenas generalidades.  
- Não depender exclusivamente do idioma: prompt em português pode funcionar bem, mas inglês pode gerar mais consistência em alguns casos.  
- Ao traduzir prompts, revisar manualmente para evitar perda de sentido técnico.  
- Considerar a ausência de lockfile como problema sério de reprodutibilidade e auditoria.  
- Entender a diferença entre dependências pinadas e não pinadas, pois isso afeta estabilidade e previsibilidade.  
- Tratar vulnerabilidades em bibliotecas centrais como prioridade maior, especialmente quando afetam o core do fluxo.  
- Evitar severidade inflada sem justificativa; issues críticas precisam ser específicas e objetivas.  
- A análise de risco deve explicar consequência prática, não apenas repetir a existência da vulnerabilidade.  
- Priorizar arquivos críticos que concentram impacto operacional, como os que lidam com workflow, credenciais e integrações externas.  
- Revisar dependências depreciadas, typos de pacote e nomes incorretos, pois podem indicar erro de configuração ou uso indevido.  
- Usar o plano de ação como consequência da análise, conectando achado, impacto e correção.