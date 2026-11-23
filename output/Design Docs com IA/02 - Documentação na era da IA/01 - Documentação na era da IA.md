Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=16964)

## Resumo da aula

Documentação deixou de ser apenas um artefato preparatório ou burocrático. Na era da IA, ela participa diretamente do desenvolvimento porque pode ser lida por modelos para orientar implementação, manutenção e planejamento. Isso a aproxima do papel dos testes automatizados: ambos preservam conhecimento útil ao longo do tempo e reduzem erro em mudanças futuras.

Modelos de IA usam documentação como contexto operacional. Quando esse contexto está claro, a geração de código tende a ser mais assertiva porque a IA não depende apenas de inferência a partir do código-fonte ou de prompts curtos. O valor da documentação, portanto, não está só em registrar decisões humanas, mas em alimentar um agente que executa trabalho técnico com base nelas.

Cada novo chat iniciado para trabalhar em um projeto se comporta como um funcionário recém-chegado: ele não conhece domínio, restrições, objetivos nem convenções locais. O código ajuda, mas não substitui a visão explícita do sistema, das intenções e dos limites do produto. A documentação reduz esse tempo de ambientação e aumenta a confiança de que a IA entendeu o projeto antes de propor mudanças.

Uma documentação bem escrita continua útil muito depois de sua criação, desde que permaneça alinhada ao sistema. O paralelo com testes automatizados é importante: assim como um teste antigo ainda protege contra regressão, um documento antigo ainda fornece contexto valioso para novas interações com IA. Isso transforma documentação em ativo acumulativo, não em custo descartável.

IA não serve apenas para gerar código; ela também acelera a produção de documentação. Isso permite criar documentos com mais rapidez, consistência e cobertura, desde que o time saiba quais tipos de documento quer produzir e como orientar essa geração. O ganho real aparece quando a IA passa a apoiar os dois lados do ciclo: implementar e documentar.

A ideia de documentação como documento vivo sempre foi desejável, mas raramente sustentada manualmente. Com um workflow bem definido, a atualização documental pode ser incorporada ao fluxo de entrega: sempre que uma feature é desenvolvida ou o software é alterado, a IA recebe a tarefa de revisar e atualizar os documentos afetados. O documento deixa de depender apenas de disciplina manual e passa a ser mantido como parte do processo.

Quando a IA gera código e depois atualiza a documentação com base nesse mesmo código, cria-se um ciclo de sincronização contínua. Esse ciclo reduz defasagem entre sistema e documentação, que é o principal motivo pelo qual documentos perdem valor ao longo do tempo. A condição para isso funcionar é ter um workflow explícito que trate atualização documental como etapa obrigatória da mudança.

Documentação entra no workflow como entrada e como saída. Primeiro, ela fornece contexto para desenvolvimento mais assertivo; depois, é regenerada ou ajustada para refletir o que foi implementado. Esse fluxo torna a documentação operacional: ela não apenas descreve o sistema, mas participa ativamente da sua evolução.

## Transcrição

00:01

Bom, pessoal, finalmente chegamos aí na era da IA, né? E agora eu quero falar com vocês sobre documentação nesse contexto que a gente está nessa área, nessa era da inteligência artificial, tá? Então, o que acontece? Hoje, quando a gente está falando sobre documentação,

00:20

a documentação acaba sendo um ativo extremamente relevante para o processo de desenvolvimento, como os testes automatizados são também. Então, não é que a documentação é importante. A documentação, hoje em dia, faz parte do processo de desenvolvimento do software. Não é que ela é um pré-requisito apenas para desenvolver o software. A documentação

00:51

é parte do desenvolvimento. E o porquê que eu estou dizendo isso? Porque a inteligência artificial consegue ler essa documentação e transformar essa documentação em tempo de execução, em código.

01:04

E isso é um ativo extremamente forte, porque, da mesma forma que um teste automatizado que a gente cria no dia 1 do projeto, quando esse projeto tiver 2 anos, o que vai acontecer? Esse teste ainda vai estar valendo, ou ele pode ter sido atualizado, mas problemas de regressão naqueles casos de uso, raramente você vai ter, porque eu tenho um teste muito claro evitando que eu tenha esses tipos de problema.

01:34

E, hoje em dia, com o IA, é a mesma coisa. A inteligência artificial, lendo a documentação do seu projeto, ela consegue ser muito mais assertiva para fazer o processo de desenvolvimento do software. Ou seja, não é que você criou uma documentação hoje e que ela não vai mais servir. Na realidade, ela vai servir

01:53

por muito tempo, porque cada vez, pense sempre isso, eu costumo sempre falar, cada vez que você começa um novo chat para desenvolver um software ali com a sua inteligência artificial, pense que esse chat é um funcionário novo que acabou de chegar. E esse funcionário novo, ele precisa entender do projeto.

02:11

E tem uma forma de fazer com que ele entenda bem o projeto também, além de olhar para o código, é olhar para a documentação. Então, no dia 1, sempre quando você criar um novo chat, você vai estar com paz de espírito, porque você sabe que a inteligência artificial vai entender o que está acontecendo ali no projeto, tá?

02:28

Outra coisa aí é, então, a documentação se tornou uma das formas mais eficientes para que o modelo de IA possa utilizar como contexto de desenvolvimento, manutenção, planejamento, a gente vai falar disso também. Outra coisa também é, a gente tem uma possibilidade de geração agora de documentações muito mais rápida, eficiente e assertiva. E eu não estou falando de geração de código, mas sim geração de documentação.

02:54

Então, a IA lê a nossa documentação e consegue melhorar o desenvolvimento do software, ser mais assertivo, mas também, para a gente criar a documentação, a gente também vai utilizar a IA. E essa disciplina aqui é exatamente para isso, para que a gente entenda os tipos de documentos que a gente quer e também como que a gente consegue gerar esses documentos trabalhando com inteligência artificial. Beleza?

03:19

Basicamente, é um ponto que não dá para negar. E uma coisa que eu quero já deixar claro aqui para você é que, nessa era da IA, a documentação, ela sim, ela pode se tornar, finalmente, um documento vivo. Porque sempre foi lindo falar, documentação, documento vivo, software muda, a gente atualiza a documentação para a gente garantir que tudo está alinhadinho. E a gente sabe que na prática não acontece isso. Mas,

03:49

Hoje em dia, se você tiver um workflow muito bem feito, trabalhando com inteligência artificial, sem dúvidas a documentação vai ser um documento vivo. Você pode colocar no seu workflow claramente que toda vez que uma feature for desenvolvida ou alguma coisa alterou no software, automaticamente peça para a IA fazer a atualização.

04:12

dos documentos que ali existem para corroborar tudo aquilo que está sendo desenvolvido. Ou seja, acabar entrando no nosso workflow. Ou seja, a IA, além dela gerar o código, ela gera a documentação e ela também atualiza a documentação baseada no código que ela mesma acabou de gerar. Então, dá muito bem para a gente fazer isso e aos poucos a gente vai evoluindo nessa disciplina para ver como é que a gente faz. Fechou? Então, vamos nessa aí, galera!

## Resumo IA

**Abreviações**  
- IA — Inteligência Artificial  
- workflow — fluxo de trabalho  

**Resumo**  
A aula apresenta a documentação como parte integrante do processo de desenvolvimento de software na era da IA, deixando de ser vista apenas como um artefato burocrático ou preparatório. O instrutor explica que a documentação passou a ter valor operacional porque pode ser lida por modelos de IA e usada como contexto para orientar implementação, manutenção e planejamento, de forma semelhante ao papel dos testes automatizados na preservação de conhecimento e na prevenção de regressões.  

Foi destacado que, a cada novo chat ou interação com a IA, o modelo se comporta como um novo integrante da equipe, sem conhecimento prévio do domínio, das restrições e das convenções do projeto. Nesse cenário, a documentação ajuda a reduzir o tempo de ambientação e aumenta a assertividade das respostas e sugestões geradas. O instrutor reforça que uma documentação bem escrita continua útil por muito tempo, desde que permaneça alinhada ao sistema, transformando-se em um ativo acumulativo do projeto.  

Além de apoiar o desenvolvimento, a IA também acelera a produção de documentação, permitindo criar documentos de maneira mais rápida, consistente e abrangente. A aula enfatiza que o ganho real ocorre quando a IA apoia os dois lados do ciclo: geração de código e geração/atualização da documentação. Para isso, é necessário definir quais documentos devem existir e como a IA deve ser orientada a produzi-los.  

Por fim, o instrutor defende que a documentação pode se tornar um documento vivo quando integrada a um workflow bem definido. Nesse fluxo, sempre que uma feature é criada ou o software é alterado, a IA é acionada para revisar e atualizar os documentos afetados. Assim, a documentação passa a participar ativamente da evolução do sistema, funcionando como entrada e saída do processo: primeiro fornece contexto para o desenvolvimento e depois é regenerada para refletir o que foi implementado.  

**Pontos de atenção**  
- A documentação não deve ser tratada como algo separado do desenvolvimento; ela faz parte do processo.  
- O valor da documentação depende de estar alinhada ao sistema real; documentos desatualizados perdem utilidade.  
- Cada novo chat com IA precisa de contexto suficiente, pois o modelo não conhece previamente o projeto.  
- O código sozinho não substitui a visão explícita de domínio, intenções e restrições presentes na documentação.  
- A documentação funciona melhor quando usada como contexto operacional para a IA, não apenas como registro estático.  
- A geração de documentação por IA exige clareza sobre quais tipos de documentos o time deseja produzir.  
- Para a documentação realmente se tornar um “documento vivo”, é necessário um workflow explícito e disciplinado.  
- A atualização documental deve ser tratada como etapa obrigatória após mudanças no software.  
- A IA pode e deve atuar nos dois sentidos do ciclo: gerar código e atualizar a documentação correspondente.  
- O principal risco é manter documentação fora do fluxo de entrega, o que gera defasagem entre sistema e conteúdo documentado.