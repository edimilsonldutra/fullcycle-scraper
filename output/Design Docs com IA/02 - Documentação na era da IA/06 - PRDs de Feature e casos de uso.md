Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16969)

## Resumo da aula

Feature não merece PRD só porque existe no backlog; ela merece PRD quando deixa de ser um requisito funcional commodity e passa a concentrar decisões de produto. O critério prático é observar se há valor percebido próprio, objetivos mensuráveis, impacto na experiência, regras específicas e trade-offs que precisem ser explicitados antes do design técnico. Se a implementação pode seguir um padrão já conhecido, com decisões essencialmente técnicas, o item tende a caber apenas como requisito funcional dentro de um PRD maior. Quando a feature vira uma unidade real de decisão, ela passa a justificar contexto documental próprio.

Requisito funcional descreve uma capacidade necessária para o sistema operar, mas nem sempre carrega identidade de produto suficiente para virar um documento separado. A diferença aparece quando a funcionalidade deixa de ser apenas “o sistema precisa fazer X” e passa a exigir definição de objetivos, políticas, métricas, integrações e restrições de negócio. Nesse ponto, tratá-la como simples linha de requisito empobrece o contexto disponível para o time e para a IA. O PRD de feature existe justamente para registrar esse contexto adicional sem misturá-lo com implementação.

Retomando o cenário de login, um sistema de autenticação básico pode ser apenas um pré-requisito técnico para acessar a plataforma. Se ele segue o fluxo padrão já oferecido por frameworks, não altera a proposta do produto, não introduz inovação relevante e não exige decisões de produto, então seu enquadramento natural é como requisito funcional de um sistema maior. Nesse caso, escrever um PRD específico tende a gerar mais formalidade do que clareza. O que importa é registrar que o sistema precisa de autenticação, não abrir um subproduto documental para algo padronizado.

O login commodity não gera valor específico para o negócio por si só; ele apenas viabiliza o acesso. Como a experiência é previsível e o modelo de implementação já é conhecido, as decisões recaem sobre tecnologia, framework e configuração, não sobre posicionamento de produto. Isso reduz a necessidade de objetivos próprios, métricas dedicadas ou escopo autônomo. Nessa situação, o PRD mais útil continua sendo o macro, com o login aparecendo como requisito funcional entre outros.

O mesmo tema muda de categoria quando o login passa a fazer parte de uma plataforma multi-tenant com foco em segurança corporativa. Aqui entram capacidades como single sign-on, autenticação de dois fatores, logout centralizado e políticas de acesso, todas com impacto direto na experiência, na adoção e nas integrações entre sistemas. O login deixa de ser um detalhe técnico e passa a organizar uma parte relevante do valor entregue. Isso já caracteriza uma feature com identidade própria e decisões suficientes para merecer PRD específico.

Compliance e multi-tenant são sinais fortes de que a funcionalidade não é mais commodity. Quando a autenticação precisa atender exigências corporativas, suportar múltiplos clientes, controlar regras distintas de acesso e servir como base compartilhada para vários sistemas, surgem restrições e decisões que não cabem em uma linha de requisito. O documento precisa explicitar quem usa, quais políticas se aplicam, quais integrações são necessárias e quais riscos existem. Sem isso, o time técnico e a IA tendem a subestimar a complexidade real da feature.

Uma feature merece PRD quando seu sucesso pode ser avaliado por objetivos como reduzir fricção no login, aumentar adoção, diminuir acessos indevidos ou viabilizar integrações corporativas. Esses objetivos mostram que a funcionalidade não existe apenas para “funcionar”, mas para produzir resultado observável no negócio e na operação. Quando esse tipo de meta aparece, a feature já não é apenas implementação; ela passa a ser produto em escala menor. O PRD organiza esse raciocínio antes que o design técnico transforme tudo em componentes e fluxos.

Mesmo fora de um papel formal de produto, desenvolvedores ganham clareza ao escrever ou consumir um PRD de feature. O documento reduz inferências implícitas, explicita por que aquela funcionalidade existe e melhora a contextualização usada pela IA na geração de design docs, código e decisões auxiliares. Em features estratégicas, isso evita tratar como detalhe técnico algo que afeta segurança, onboarding, integração e operação corporativa. O ganho não é burocracia; é precisão de contexto.

Nos dois casos existe “login”, mas o nome da funcionalidade não determina sua granularidade documental. No primeiro, login é apenas capacidade necessária e padronizada; no segundo, ele se torna uma plataforma de autenticação com impacto estratégico, regras próprias e valor de produto. A decisão correta não depende da tecnologia usada, e sim da densidade de decisões de produto concentradas naquela entrega. Quando essa densidade existe, o PRD de feature prepara o terreno para as seções específicas que detalham escopo, objetivos, regras e restrições.

## Transcrição

00:01

Seguinte, no vídeo anterior eu falei pra você sobre PRD de alto nível, ou seja, ele vai dar uma visão e responder diversas daquelas perguntas que eu trouxe pra você.

00:13

Por outro lado, o que eu queria trazer aqui para você é o seguinte, além de a gente ter um PRD de alto nível, nós podemos ter um PRD mais baixo nível, e que, às vezes, pode ser necessário para você desenvolver um módulo do seu sistema ou até mesmo uma feature. Ou seja, normalmente, quando a gente fala módulo no contexto é algo mais técnico, quando a gente fala de API normalmente é um contexto mais de produto,

00:42

Mas, de forma geral, ambos representam o mesmo nível de granularidade e um agrupamento de funcionalidades relacionadas. Então, somente para tentar deixar mais claro, porque quando eu falo de um PRD de alto nível, ele engloba muita coisa estratégica da empresa, de forma geral, e que está tudo ok.

01:03

Porém, às vezes, eu preciso e quero ter um PRD do módulo que estou desenvolvendo, da feature que estou desenvolvendo, mesmo que eu não seja diretamente ligado a sendo uma pessoa de produto, mas eu posso ter certeza que, se o meu projeto tiver um PRD mais redondo, aí ela vai conseguir trabalhar melhor. Então, eventualmente, eu vou te recomendar para você criar um PRD, pelo menos básico, que vai gerar uma contextualização para a inteligência

01:32

artificial entender o que você está fazendo de forma geral, tá? Então, eu quero trazer dois casos importantes aqui para você entender quando vale e quando não vale a pena ter ali um PRD de uma feature de um módulo. Então, vamos lá. Eu tenho um caso 1 aqui, um sistema de autenticação, um sistema de login. Então, vamos lá. Para que a plataforma de estudo da FullCycle funcione, ela obrigatoriamente precisa ter um sistema de login.

01:59

Olhando dessa forma, isso é apenas mais um pré-requisito técnico para acessar o sistema. Ou seja, não há nada de novo, nenhuma inovação, nenhuma decisão de produto envolvida. Ou seja, se você pensar bem, sistema de login é algo que já vem pronto em tudo quanto é framework, se você perceber. Ou seja, ele é um commodity, ele não gera valor específico para o negócio. Ele é apenas mais um requisito ali do meu sistema, que eu preciso me autenticar para conseguir acessar.

02:27

Ou seja, já existe o modelo padrão de implementação, não muda necessariamente a experiência do usuário, nem a forma de como o produto vai trabalhar. As decisões são puramente técnicas, ou seja, não é uma decisão de produto. E, provavelmente, esse primeiro caso de sistema de autenticação de login faria parte dos requisitos funcionais de um sistema maior,

02:51

que pode possuir uma PRD. Você vai ver que, dentro das PRDs, a gente tem requisitos funcionais e não funcionais. E o que acontece? Provavelmente o sistema de login ia ser mais uma linha. O sistema precisa de autenticação, o sistema de login ali como requisito. Beleza? Então, esse é o caso número 1. Um login normal que a gente acaba vendo ali dentro do sistema que a gente usa no dia a dia. Vem aí com o seu framework, você colou meia dúzia de linha e já está funcionando ali.

03:19

Agora, eu tenho um caso número 2 aqui, tá? E esse número 2 é um pouco diferente.

03:27

O login é uma feature com valor e decisões de produto. Então, perceba que eu ainda estou falando de sistema de login. Mas, olha só, você está criando uma plataforma multi-tenant para desenvolvedores com foco em segurança corporativa. O time precisa implementar um novo sistema de login que trabalhe com single sign-on, autorização de dois fatores, trabalhe com out, tem que ter política de acesso.

03:53

o que mais que tem de acesso corporativo. Nesse caso, se você perceber, essa plataforma que eu tenho vai mudar a experiência do usuário. Eu vou ter diversas formas de fazer login. Eu vou poder utilizar essa mesma plataforma de login para diversos sistemas, para diversos clientes, e com segurança, com pontos específicos de compliance que grandes empresas precisam utilizar.

04:23

ou seja, impacta compliance, impacta onboarding, impacta integrações, tem objetivos bem mensuráveis, ou seja, eu quero facilitar a minha fricção de login, eu quero aumentar a adoção, eu quero reduzir acessos indevidos, eu quero envolver mais decisões específicas sobre integrações e segurança. Então, se você perceber,

04:47

Os dois casos, no final do dia, tem um login que o cara vai usar e vai acessar uma determinada plataforma. Mas uma coisa é você ter um requisito que o usuário vai lá e faz o login. Outra coisa é você ter um sistema próprio de autenticação que vai poder ser utilizado na empresa inteira.

05:10

que vai acompanhar diversos tipos de regra. Provavelmente, vai ter um time dedicado somente para desenvolver esse sistema, essa feature de login, para que os outros sistemas todos possam integrar nele. Você consegue perceber que essa feature é um produto.

05:31

ela acaba afetando, inclusive, a forma estratégica de como a empresa funciona. Por quê? Porque, dependendo da situação, e eu tenho política corporativa, eu posso colocar pessoas ou...

05:47

ou colaboradores de outras empresas terceirizados, eu consigo gerenciar toda essa parte. Então, se você olhar, é um nível muito diferente de você ter apenas o sistema de login e senha, e outra coisa é você ter uma plataforma multitenant para segurança, onde vai ter a parte de sistema de login. Então, se você perceber, um, provavelmente a gente não ia precisar de ter um PRD para isso.

06:10

Agora, para esse cara aqui, provavelmente eu preciso, porque muda muita coisa para a gente conseguir trabalhar e para desenvolver isso. Acredito que fez sentido isso para vocês. No próximo vídeo, eu quero trazer um pouco mais claro para você quais normalmente são as seções que você vai encontrar no PRD de feature, e não aquele PRDzão que eu passei para você de altíssimo nível, que foca muito em negócio e em produto.

06:40

Beleza? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **PRD** — *Product Requirements Document* (Documento de Requisitos do Produto)  
- **API** — *Application Programming Interface* (Interface de Programação de Aplicações)  
- **SSO** — *Single Sign-On* (Autenticação Única)  
- **Multi-tenant** — arquitetura em que uma mesma plataforma atende múltiplos clientes/tenants com isolamento lógico  
- **2FA** — *Two-Factor Authentication* (Autenticação de Dois Fatores)

**Resumo**  
A aula diferencia quando uma feature ou módulo merece um PRD específico e quando deve ser tratado apenas como um requisito funcional dentro de um PRD maior. O instrutor explica que um PRD de alto nível cobre o contexto estratégico do produto, enquanto um PRD de feature serve para registrar decisões, regras, objetivos e restrições de uma funcionalidade mais granular, ajudando o time e a IA a trabalharem com mais contexto.

O critério central apresentado é observar se a funcionalidade é apenas commodity técnica ou se concentra decisões de produto. No caso de um login básico, padrão de frameworks, a implementação é previsível, não altera a experiência nem cria valor próprio para o negócio; por isso, ele deve aparecer apenas como requisito funcional de um sistema maior. Já em um cenário de plataforma multi-tenant com foco em segurança corporativa, o login passa a envolver SSO, autenticação em dois fatores, políticas de acesso, compliance, integrações e objetivos mensuráveis, como reduzir fricção, aumentar adoção e evitar acessos indevidos.

A aula reforça que a nomenclatura “login” não define a granularidade documental; o que define é a densidade de decisões de produto presentes na entrega. Quando a feature deixa de ser só uma capacidade técnica e passa a representar uma unidade de valor, com impacto na experiência, na operação e na estratégia da empresa, ela passa a justificar um PRD próprio. Esse documento ajuda a evitar ambiguidades e prepara o terreno para o design técnico e para as próximas seções do PRD de feature.

**Pontos de atenção**  
- Não criar PRD de feature só porque o item existe no backlog; avalie se ele realmente concentra decisões de produto.  
- Se a implementação é padrão, repetitiva e resolvida por framework, normalmente basta tratá-la como requisito funcional.  
- Evite burocratizar funcionalidades commodity, pois isso tende a gerar mais formalidade do que clareza.  
- Considere PRD de feature quando houver objetivos mensuráveis, regras específicas, restrições de negócio e impactos claros na experiência.  
- Features ligadas a segurança, compliance, multi-tenant, onboarding e integrações costumam exigir contexto documental mais rico.  
- Não confunda granularidade técnica com granularidade de produto: um módulo pode ser técnico, mas a decisão de ter PRD depende do valor e das decisões embutidas.  
- Um bom PRD reduz inferências implícitas e melhora a contextualização para o time e para ferramentas de IA.  
- O mesmo nome de funcionalidade pode representar coisas bem diferentes em contextos distintos; a avaliação deve considerar o papel estratégico da entrega.  
- Quando o sucesso da feature depende de métricas e políticas próprias, ela provavelmente já deixou de ser apenas um detalhe técnico.