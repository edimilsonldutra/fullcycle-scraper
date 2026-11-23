Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16960)

## Resumo da aula

A documentação sempre acompanhou o desenvolvimento de software porque engenharia de software não se resume a programar: ela organiza como o sistema é pensado, construído, entregue e mantido. Retomando a ideia já estabelecida de documentação como ativo de engenharia, aqui o ponto novo é histórico: por muito tempo, documentar era uma condição estrutural do processo, não apenas um apoio à comunicação. Isso moldou a forma como times tomavam decisões e também a reputação da documentação dentro das empresas.

Processos sequenciais organizam o trabalho em etapas rígidas, executadas em ordem fixa, com pouca ou nenhuma sobreposição. Esse modelo existe para reduzir incerteza por meio de planejamento antecipado: antes de implementar, tenta-se definir o máximo possível sobre requisitos, arquitetura e comportamento do sistema. O custo dessa previsibilidade é a baixa capacidade de adaptação quando o contexto muda no meio do projeto.

O waterfall é a forma clássica de processo sequencial: cada fase precisa terminar completamente antes da próxima começar. A lógica é linear e pressupõe que o problema pode ser entendido com antecedência suficiente para orientar todo o restante do trabalho. Isso funciona melhor quando requisitos são estáveis; em ambientes de negócio mutáveis, o modelo tende a acumular atraso de feedback e retrabalho.

O fluxo típico do waterfall começa com levantamento de requisitos, passa por análise e projeto, segue para implementação, depois testes, deploy e manutenção. No início, todos os requisitos do sistema são definidos e documentados em alto nível de detalhe, e esse conjunto orienta arquitetura, interfaces e componentes. A implementação só começa depois que o projeto foi formalizado, e a validação mais forte do sistema acontece tardiamente, perto da entrega.

Nesse contexto, a documentação deixava de ser apenas registro e passava a funcionar como contrato entre as partes envolvidas. As decisões de software eram formalizadas antes da implementação, e o documento servia como referência para cobrar aderência ao que foi combinado. Isso aumentava controle e rastreabilidade, mas também tornava a mudança mais cara, porque alterar o sistema significava revisar acordos já consolidados em artefatos.

A forte dependência de documentação produziu uma cultura de artefatos: requisitos, especificações de sistema, diagramas e modelos como UML. Esses documentos existiam para detalhar o comportamento esperado do software antes da codificação, reduzindo ambiguidades e distribuindo entendimento entre áreas diferentes. O efeito colateral aparecia quando o volume documental virava pré-condição para avançar, desacelerando o fluxo de desenvolvimento.

Em processos sequenciais, o cliente normalmente só enxerga o software quando ele já está perto da entrega ou concluído. Isso atrasa a descoberta de erros de entendimento, porque problemas nos requisitos ou no design não aparecem cedo por meio de uso real. Quando a validação acontece apenas no fim, corrigir desvios exige voltar várias etapas, o que eleva muito o retrabalho.

Projetos longos sofrem com a diferença entre o momento em que os requisitos foram coletados e o momento em que o sistema fica pronto. Retomando o cenário de registrar decisões do projeto, no modelo sequencial quase tudo precisava ser definido antes da implementação; se o negócio mudasse seis meses depois, o software continuava refletindo o contexto antigo. O resultado era um produto tecnicamente coerente com a documentação inicial, mas desalinhado com a necessidade atual da empresa.

Quando a documentação é tratada como pré-condição para começar a construir, ela passa a controlar o ritmo do projeto. Isso cria mais previsibilidade formal, mas também adiciona fricção para colocar software em produção, porque qualquer erro de entendimento se propaga por várias fases antes de ser percebido. A relação entre documentação e tomada de decisão fica explícita: decidir cedo demais congela premissas que talvez não sobrevivam ao tempo do projeto.

O RUP surge nesse contexto como uma tentativa de organizar o desenvolvimento com forte disciplina de processo e uso intensivo de artefatos, sem abandonar a preocupação com controle. Ele não rompe com a centralidade da documentação; em vez disso, refina e estrutura melhor como decisões, requisitos e modelos são registrados ao longo do projeto. Essa posição intermediária prepara a transição entre a rigidez do waterfall e abordagens posteriores mais adaptáveis.

## Transcrição

00:01

Bom, pessoal, seguinte, a nossa disciplina está focada muito em design docs, tá? Mas eu queria te dar um contexto sobre documentações de forma geral. Principalmente, uma fundamentação somente para a gente entender como que a gente chegou até aqui.

00:18

Beleza? E também eu quero mostrar, principalmente agora, nesse início de curso, as principais diferenças de documentações entre aspas comum ou documentações muito utilizadas nas empresas e que muitas vezes são confundidas com design docs. E a nossa ideia aqui é que você tenha esse tipo de clareza para que você, conforme a gente for passando para os tipos de design docs que você vai ver e a gente vai discutir e tudo mais,

00:48

você tenha realmente ali uma certeza que você está usando a documentação, o tipo de documentação certa para o momento certo. Maravilha? Então vamos lá pessoal, qual que é o contexto que a gente tem quando a gente está falando sobre documentações? O negócio é o seguinte, o processo de documentar

01:09

ele acompanha a engenharia de software. Então, a gente tem que sempre lembrar que engenharia de software é uma disciplina. Engenharia de software não é algo extremamente específico, é um conjunto de capacidades que a gente precisa ter, ou seja, acaba gerando um começo, meio e fim para que a gente consiga, desde

01:30

criar o software, projetar o software, até esse software estar no ar, ele ter resiliência e tudo mais, tá? E a parte de documentação, ela por muito tempo, inclusive até hoje, ela sempre acompanhou o processo de desenvolvimento de um software.

01:46

Por outro lado, tem uns pontos que realmente são importantes e por isso que eu queria dar uma contextualizada. Talvez você já saiba disso, talvez não, mas vale a pena a gente dar uma lembrada nisso. Quando a gente estava muito focado nos anos 70 e 80,

02:02

normalmente a gente trabalhava com processos sequenciais, tá? Como o famoso waterfall, né? Uma cascata, um modelo cascata. E algumas metodologias, por exemplo, que é o RUP, por exemplo, né? Que é o Rational Unified Process. A RUP, ela foi comprada, a Rational, né? Ela foi comprada pela IBM, existe até hoje, inclusive. Mas o nosso ponto principal é que

02:27

Tudo o que a gente fazia naquela época, a gente não, eu não desenvolvia software em 1980, mas o que acontecia era que a documentação era um dos pontos principais para estartar um projeto. Então, enquanto toda a documentação, todos os fluxos, não estivessem

02:47

corretos e certos, é como se o software não pudesse ainda ser desenvolvido, tá? Então, durante todo esse processo, principalmente os processos sequenciais e metodologias como RUP, por exemplo, fez com que a gente tivesse algo que normalmente a gente chama de artefatos, tá? Ou seja, são diversos documentos que são gerados de requisitos, especificações de sistemas, trabalhar com o ML, que é algo extremamente útil, inclusive, tá?

03:15

E quando a gente está falando, por exemplo, no método, a gente vai falar um pouquinho mais sobre a Waterfall, a documentação era vista como um contrato, tá? E as decisões realmente de software eram claramente registradas antes da implementação.

03:32

Então, a ideia principal é, quando a gente está falando em waterfall, ou modelo cascata, vamos dizer assim, o que significa? Que a gente tem uma ordem linear e bem rígida, onde cada fase precisa ser concluída completamente antes de a próxima fase começar. Então, basicamente, a gente tinha fluxos como esses aqui que eu quero te passar agora.

03:58

que é levantamento de requisitos, ou seja, todos, absolutamente todos os requisitos do sistema, eles são definidos e documentados de forma extremamente detalhada logo no início do projeto. Isso pode parecer algo realmente bem importante, né? Já pensou se a gente tivesse realmente documentado todas as regras de negócio, tudo que a gente precisasse logo de cara na hora de desenvolver? Seria ótimo.

04:22

mas a gente vai chegar em consequências que acabaram levando, não vou dizer ao fracasso, mas gerando uma inércia muito grande no processo de desenvolvimento de um software. Bom, uma vez que a gente levantou o requisito, a gente precisa fazer a análise e o projeto, ou seja, o design do projeto. Então, com base nesses requisitos, a gente vai fazer um projeto de arquitetura, a gente vai entender as interfaces, a gente vai entender os componentes,

04:49

Depois disso, a gente entra para a fase de implementação, que é onde a gente realmente codifica de acordo com o que o projeto foi definido. Depois, a gente tem todo o processo de teste, o sistema testado para verificar se atende aos requisitos. E aí, a gente tem

05:05

os mais diversos tipos de testes, inclusive, principalmente naquela época, muitos testes manuais, com playbooks claros de como fazer testes e etc. E daí, nós temos deploy, ou seja, o produto era entregue, entre aspas, ao cliente.

05:21

E a manutenção, ele sempre servia para correções e fazer melhorias que são feitas após a entrega. Então, quando a gente fala, inclusive, produto era entregue ao cliente, é que, no final das contas, o software, até hoje, ele é um produto. Ou seja, é algo que está sendo vendido, que está sendo desenvolvido para gerar algum valor, para ele ser consumido de alguma forma, tá?

05:43

Agora, o ponto principal de quando a gente trabalha com fluxo desse tipo é que o cliente só vê o resultado final

05:54

E se algo estiver errado nos requisitos, o retrabalho é alto. Então, isso aí sempre foi um problema e gerou, vamos dizer assim, uma fricção muito grande a gente conseguir colocar software no ar. E a gente tem um ponto também que é extremamente importante a gente lembrar, que é o seguinte.

06:16

Às vezes, desenvolver um software grande pode demorar meses e mais meses, pode chegar a anos para você fazer isso, né? Agora, a empresa, ela é algo vivo, né? Existe mercado, existem produtos, existe time to market, a gente tem um monte de coisas desse tipo. O que acontecia muito no passado é que, apesar de todos os requisitos tenham sido colhidos no processo de desenvolvimento do software,

06:43

Quando o software estava para ser entregue, o momento que a empresa estava vivendo era diferente. O processo que a empresa trabalha agora é diferente. O produto que a empresa tem é diferente. Ou seja, o software não consegue acompanhar as mudanças que as empresas tinham. Então, uma empresa, no momento de pegar o requisito, ela era uma empresa. Seis meses depois, as coisas mudam.

07:09

E esse tipo de processo, ele gerava ali um bom trabalho, um bom retrabalho, muitas brigas, discussões, e simplesmente acabava gerando, além de estresse, obviamente,

07:25

acaba ficando muito caro, principalmente para as empresas, mas era o método ali, vamos dizer assim, global de um consenso de mercado de como era desenvolvido o software, beleza? Para a gente não deixar esse vídeo aqui muito grande, eu vou cortar aqui para a gente iniciar, para a gente poder falar sobre RUP, beleza? Então, vamos nessa.

## Resumo IA

**Abreviações**  
- **RUP** — *Rational Unified Process*  
- **UML** — *Unified Modeling Language*  
- **ML** — *Model Language* (como mencionado na aula, em referência a modelos/diagramas; no contexto de engenharia de software, normalmente se refere a UML e seus modelos)

**Resumo**  
A aula contextualiza o papel da documentação na engenharia de software, destacando que documentar não é apenas apoiar a comunicação, mas também organizar como o sistema é pensado, construído, entregue e mantido. O instrutor explica que, historicamente, principalmente nas décadas de 1970 e 1980, os processos sequenciais dominavam o desenvolvimento, com forte dependência de artefatos formais como requisitos, especificações, diagramas e modelos. Nesse cenário, a documentação funcionava quase como um contrato: as decisões eram formalizadas antes da implementação, e o avanço do projeto dependia de tudo estar corretamente definido.

Em seguida, a aula apresenta o waterfall como o modelo clássico de processo sequencial. Nesse fluxo, as fases acontecem em ordem rígida: levantamento de requisitos, análise e projeto, implementação, testes, deploy e manutenção. O objetivo desse modelo era reduzir incertezas por meio de planejamento antecipado, tentando definir o máximo possível no início. Porém, o instrutor ressalta que essa previsibilidade tem um custo alto: pouca capacidade de adaptação, feedback tardio, retrabalho elevado e dificuldade de acompanhar mudanças no negócio ao longo de projetos longos.

A aula também compara a expectativa de estabilidade do waterfall com a realidade dinâmica das empresas. Mesmo quando os requisitos eram bem documentados no início, o contexto organizacional podia mudar antes da entrega, fazendo com que o software chegasse ao final coerente com a documentação original, mas desalinhado com a necessidade atual. Por fim, o instrutor introduz o RUP como uma abordagem que preserva a disciplina de processo e o uso intensivo de documentação, mas busca estruturar melhor a forma de registrar decisões, requisitos e modelos ao longo do projeto, servindo como ponte entre a rigidez do waterfall e abordagens mais adaptáveis.

**Pontos de atenção**  
- Documentação não é apenas registro: em processos tradicionais, ela também atua como base de decisão e contrato entre as partes.  
- No waterfall, cada fase depende da conclusão total da anterior; essa rigidez aumenta previsibilidade, mas reduz adaptabilidade.  
- Levantar “todos” os requisitos no início pode parecer vantajoso, mas tende a gerar inércia e dificuldade de mudança.  
- A validação tardia faz com que erros de entendimento apareçam só perto da entrega, elevando muito o retrabalho.  
- Em projetos longos, o contexto do negócio muda antes do software ficar pronto; o produto pode ficar tecnicamente correto e ainda assim desalinhado da realidade.  
- Quanto mais a documentação vira pré-condição para avançar, maior a fricção para colocar software em produção.  
- Processos sequenciais tendem a atrasar o feedback do cliente, que só vê o resultado final ou quase final.  
- A centralidade de artefatos pode melhorar rastreabilidade e controle, mas também desacelerar o desenvolvimento se houver excesso documental.  
- Mudanças após a formalização das decisões tornam-se caras, pois exigem revisão de etapas e documentos já consolidados.  
- O RUP mantém forte disciplina documental; a aula o apresenta como transição importante, não como ruptura completa com o modelo sequencial.