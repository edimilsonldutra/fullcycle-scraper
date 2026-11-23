Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17118)

## Resumo da aula

Architecture Decision Record é um documento usado para registrar decisões arquiteturais relevantes e, principalmente, o motivo de elas terem sido tomadas. Código-fonte mostra o que foi implementado, mas raramente preserva com clareza as restrições, trade-offs e pressões que levaram àquela escolha. O ADR existe para transformar esse raciocínio em memória técnica explícita, acessível mesmo anos depois. Isso reduz a perda de contexto e evita que decisões importantes virem apenas tradição oral dentro do time.

Sistemas costumam evoluir por muitos anos, enquanto pessoas entram e saem do projeto continuamente. Quando o contexto das mudanças arquiteturais depende da lembrança de indivíduos específicos, o time fica vulnerável a interpretações incompletas, retrabalho e reversões mal informadas. Registrar decisões cria continuidade do raciocínio arquitetural ao longo do tempo, porque preserva não só a escolha final, mas também o porquê daquela escolha ter feito sentido naquele momento. O valor disso cresce conforme a vida útil do sistema aumenta.

O histórico de decisões funciona como uma timeline arquitetural do sistema. Em vez de enxergar a arquitetura como uma fotografia estática, o time passa a enxergá-la como uma sequência de escolhas feitas em resposta a necessidades concretas. Esse histórico ajuda a entender por que certas partes do sistema mudaram, quais direções foram priorizadas e quais consequências já eram conhecidas quando a decisão foi tomada. Documentar esse percurso torna a manutenção e a evolução mais seguras.

ADR é mais valioso quando a decisão tem impacto estrutural, afeta múltiplas partes do sistema ou tende a gerar dúvidas no futuro. Isso inclui mudanças arquiteturais relevantes, escolhas que envolvem trade-offs importantes e decisões cujo motivo não ficará evidente apenas olhando o código. Nem toda decisão operacional precisa virar ADR; o foco está naquilo que influencia a arquitetura e cuja justificativa precisa sobreviver ao tempo. O critério central é simples: se esquecer o porquê prejudica a evolução do sistema, vale registrar.

A utilidade do ADR aumenta em ambientes com inteligência artificial porque modelos conseguem operar melhor quando encontram contexto explícito, e não apenas artefatos dispersos. Um sistema de IA pode usar ADRs para recuperar intenção arquitetural, relacionar mudanças ao longo do tempo e apoiar análise, geração e revisão de documentação. Sem esse registro, a IA tende a inferir motivos a partir do código e de sinais indiretos, o que é mais frágil. Com memória técnica bem documentada, a IA deixa de adivinhar e passa a trabalhar sobre contexto declarado.

## Transcrição

00:01

Bom, pessoal, agora a gente tá entrando num outro momento, num assunto extremamente importante e que tem tudo a ver com essa parte de design docs, tá? Inclusive, na minha opinião, esse é um dos documentos, entre aspas, mais importantes que você pode ter no seu projeto, porque, no final das contas, ele vai documentar o seu projeto

00:24

durante o ciclo de vida dele, ou seja, ele vai trazer para vocês, de uma forma cada vez mais clara, o porquê determinadas decisões arquiteturais foram tomadas ao longo do tempo. E isso, na realidade, pessoal, é ouro, porque sistemas demoram muito, mais muitos anos para serem feitos, desenvolvedores entram, desenvolvedores saem, e se você tivesse registrado

00:53

o porquê grandes partes das mudanças arquiteturais foram tomadas durante o tempo, sem dúvidas ficaria muito mais fácil para o time, para o desenvolvedor, e também agora para a inteligência artificial. Então, a gente vai falar sobre um documento chamado ADR, que é Architecture Decision Record.

01:13

E durante esse capítulo, eu quero trazer para vocês e tentar deixar mais claro o quando, como, aonde você deve utilizar e não deve utilizar esse tipo de documento. Vou tentar trazer diversos esquemas para que fique mais fácil você...

01:32

entre aspas, memorizar ou ressignificar muita coisa que você foi aprendendo ao longo dos anos em relação à documentação. E, obviamente, a gente vai ver como a inteligência artificial consegue fazer, entre aspas, uma mágica para nos ajudar nessas tarefas. Então, vamos nessa, porque tem bastante coisa para a gente ver agora sobre Architecture Decision Record.

## Resumo IA

**Abreviações**  
- **ADR** — *Architecture Decision Record*.

**Resumo**  
A aula apresenta o Architecture Decision Record como um documento essencial para registrar decisões arquiteturais relevantes ao longo do ciclo de vida de um sistema, principalmente o motivo de cada escolha ter sido feita. O instrutor destaca que o código-fonte mostra o que foi implementado, mas raramente preserva com clareza o contexto, as restrições e os trade-offs que levaram àquela decisão. Por isso, o ADR funciona como uma memória técnica explícita, ajudando a evitar a perda de conhecimento quando desenvolvedores entram e saem do projeto ao longo dos anos. A ideia central é transformar a arquitetura em uma linha do tempo de decisões, permitindo entender não só o resultado final, mas também o raciocínio por trás das mudanças. A aula também enfatiza que esse tipo de documentação se torna ainda mais útil em sistemas de longa duração, em decisões com impacto estrutural e em contextos com inteligência artificial, já que a IA consegue atuar melhor quando encontra contexto declarado em vez de precisar inferir intenções a partir de sinais dispersos no código.

**Pontos de atenção**  
- Registrar o **porquê** da decisão, e não apenas a decisão final.  
- Usar ADRs principalmente para escolhas com **impacto arquitetural** ou que afetam várias partes do sistema.  
- Evitar transformar toda decisão operacional em ADR; o foco deve ser no que precisa **sobreviver ao tempo**.  
- Considerar que sistemas de longa vida útil sofrem com **troca constante de pessoas**, então depender da memória individual é arriscado.  
- Tratar o histórico de ADRs como uma **timeline arquitetural**, útil para entender evolução, mudanças e consequências já conhecidas.  
- Reconhecer que a IA trabalha melhor com **contexto explícito**; sem ADR, ela tende a inferir motivos de forma frágil a partir do código.  
- Manter a documentação clara para reduzir **retrabalho, interpretações incompletas e reversões mal informadas**.