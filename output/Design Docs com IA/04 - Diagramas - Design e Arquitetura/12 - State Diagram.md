Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17081)

## Resumo da aula

State diagram em Mermaid representa os estados possíveis de um sistema e as transições entre eles. Ele é a escolha correta quando o comportamento não depende apenas de uma sequência de passos, mas do status atual em que a entidade se encontra. Isso é típico de workflows, automações e máquinas de estado, nas quais a mesma entrada pode produzir respostas diferentes conforme o estado armazenado.

Retomando os diagramas já vistos, flowchart continua útil para decisões e caminhos alternativos, e sequence para interações ao longo do tempo. O state diagram responde outra pergunta: em que estado o sistema está agora e para quais estados ele pode ir depois. Essa perspectiva é mais adequada quando a regra central é “se estiver neste status, reaja desta forma”.

O exemplo usa uma cadeia simples de estados para raciocinar sobre limitação de requisições: parado, ativo, limitado, cooling down e bloqueado. Cada nó representa uma condição persistente ou temporária do sistema, e cada seta representa o evento ou condição que autoriza a mudança. O valor do diagrama está em tornar explícito que o sistema não reage apenas ao evento atual, mas também ao histórico condensado no estado atual.

Quando uma requisição chega, o sistema sai do estado inicial e entra em ativo, o que indica operação dentro do limite esperado. Ao atingir um limite definido, ele transita para limitado, sinalizando que a política de controle passou a restringir o comportamento. Depois, entra em cooling down, estado temporário em que a janela é reiniciada antes de permitir retorno ao estado ativo.

O estado bloqueado modela uma regra mais severa do que a limitação temporária. Se durante o cooling down o sistema detectar abuso, a transição deixa de apontar para recuperação e passa a apontar para bloqueio permanente. Esse tipo de modelagem é útil porque separa claramente penalidades temporárias de penalidades definitivas, evitando que a regra fique implícita em texto solto ou espalhada no código.

Muitas regras de negócio dependem de status, flags e condições temporárias registradas no sistema. Nesses casos, o state diagram ajuda a visualizar por que determinada ação foi permitida, negada, adiada ou redirecionada para outro processamento. Se um item está em certo estado, isso implica que ele percorreu transições específicas; essa rastreabilidade melhora revisão de regra, alinhamento entre times e manutenção futura.

Em Mermaid, o state diagram permite descrever a máquina de estados como texto versionável, assim como os outros diagramas já trabalhados. O passo prático é listar os estados relevantes, nomear as transições com os eventos de negócio e verificar se cada mudança de comportamento do sistema está ancorada em um estado explícito. Se uma regra depende de “status atual + evento recebido”, esse formato tende a comunicar melhor do que um fluxo puramente procedural.

## Transcrição

00:01

Bom, pessoal, então, no vídeo anterior eu estava dando uma passada rápida aqui com vocês sobre a parte dos diagramas Mermaid. Recomendo, sim, que você se aprofunde. Ele tem diversos tipos, inclusive C4, se você olhar aqui. Novamente, pelo menos até o momento, eu prefiro ver o C4 através do Plane2ML. Eu acho que tem muitos detalhes que a gente consegue trabalhar daquela forma e etc. Por outro lado,

00:30

Tem que ser plain to ML, a gente meio que tem que compilar e etc e tudo mais, e no caso do Mermaid a gente não precisa disso e de forma geral ele é bem fácil. Recomendo que você teste, que você brinque e chegue aí até a sua própria conclusão, tá? Tem mais um tipo de...

00:49

de diagrama que eu quero mostrar aqui pra vocês, que são os diagramas de estado, tá? Então, quer ver, ó? Diagrama de estado, né? State diagram aqui, ó. Ele mostra os estados possíveis dentro de um sistema e suas transações, ele é indicado pra workflow, entender automação, máquina de estado, ou seja, qualquer coisa que armazena um estado

01:08

que vai ser utilizado para ser tomada alguma outra decisão, tá? Ou seja, a gente consegue entender como que o sistema reage. Esse exemplo aqui, tá, galera, não é necessariamente a ver com o Rate Limiter, tá? Mas, basicamente, tem o sistema aqui parado, ou seja, não tem estado nenhum, bateu a requisição, ele fica ativo.

01:27

Se atingiu um determinado limite, o que vai acontecer? Ele está limitado nesse momento, ou seja, cada carinha desse é um estado que ele fica. Aí, depois disso, eu tenho janela reiniciando, ou seja, cooling down. Ou seja, ele fica esperando naquele estado até que eu possa reiniciar a janela e voltar com o sistema ativo aqui para mim.

01:49

Aqui eu tenho um outro caso, que quando ele vai ser ativo, ou seja, significa que as minhas requisições estão dentro do meu limite. Agora, nesse caso aqui, quando ele está culling down, eu posso identificar um determinado abuso, e se esse abuso for detectado, esse cara está bloqueado permanentemente e acabou. Então, é basicamente isso que acontece, ou seja, cada ponto desse é o estado que existe no sistema naquele momento.

02:14

E isso aí realmente é bem interessante para que a gente consiga entender como que as coisas funcionam em determinadas situações. E eu vou dar um exemplo que talvez possa te ajudar e te provocar para você utilizar esse tipo de diagrama. Sabe quando a gente tem regras de negócio?

02:35

e essas regras de negócio, baseado em um determinado status, faz com que o sistema se comporte de um jeito e que ele grave dados em algum outro lugar por conta daquela forma. Ou seja, sabe quando um determinado status ou determinadas flags ou situações temporárias que aconteçam no sistema,

03:00

aconteçam, estejam ali no nosso sistema, esse tipo de diagrama é interessante, porque você consegue ver como está o estado das coisas, ou seja, se algo está nesse estado é porque ele passou por esse fluxo aqui. Então, é algo interessante. Verifique se faz sentido, inclusive, para você utilizar no seu dia a dia. Fechou? Próximo vídeo, vamos ali finalmente IDE novamente ver esses caras sendo gerados. Vamos nessa, galera.

## Resumo IA

**Abreviações**  
- **C4**: modelo de diagramação de arquitetura com níveis de contexto, contêiner, componente e código.  
- **Mermaid**: linguagem de marcação para gerar diagramas a partir de texto.  
- **Rate Limiter**: mecanismo de limitação de requisições.  
- **workflow**: fluxo de trabalho.  
- **state diagram**: diagrama de estados.  
- **machine of state / máquina de estado**: modelo em que o sistema transita entre estados conforme eventos e regras.  

**Resumo**  
A aula apresentou o diagrama de estados em Mermaid como uma forma de representar os estados possíveis de um sistema e as transições entre eles, destacando que esse tipo de diagrama é mais adequado quando o comportamento depende do estado atual da entidade, e não apenas de uma sequência linear de passos. O instrutor retomou rapidamente outros diagramas já vistos, como flowchart, útil para decisões e caminhos alternativos, e sequence, útil para interações ao longo do tempo, para reforçar que o state diagram responde a outra pergunta: em que estado o sistema está agora e para quais estados ele pode ir depois.  

O exemplo prático foi construído com estados relacionados a limitação de requisições, como parado, ativo, limitado, cooling down e bloqueado. A ideia foi mostrar que cada estado representa uma condição persistente ou temporária do sistema, e que cada transição depende de um evento ou condição específica. Quando uma requisição chega, o sistema sai do estado inicial e passa para ativo; ao atingir um limite, entra em limitado; depois segue para cooling down, período em que a janela é reiniciada antes de permitir o retorno ao estado ativo. Se durante o cooling down for detectado abuso, a transição deixa de apontar para recuperação e passa para bloqueio permanente, evidenciando a diferença entre penalidade temporária e definitiva.  

O instrutor também conectou o uso do diagrama a regras de negócio que dependem de status, flags e condições temporárias. Nesses casos, o state diagram ajuda a visualizar por que uma ação foi permitida, negada, adiada ou redirecionada, além de melhorar a rastreabilidade do comportamento do sistema e o alinhamento entre equipes. Por fim, foi reforçado que em Mermaid o diagrama pode ser descrito como texto versionável, e que o passo prático é listar os estados relevantes, nomear as transições com eventos de negócio e validar se toda mudança de comportamento está ancorada em um estado explícito.  

**Pontos de atenção**  
- Use diagrama de estados quando o comportamento depender de **status atual + evento recebido**, e não apenas de um fluxo procedural.  
- Diferencie bem **estado temporário** de **penalidade permanente** para evitar regras ambíguas.  
- Nomeie as transições com **eventos de negócio claros**, não com descrições genéricas.  
- Garanta que cada mudança importante do sistema esteja associada a um **estado explícito**.  
- Considere o histórico condensado no estado atual, pois a mesma entrada pode gerar respostas diferentes conforme o estado armazenado.  
- Regras de negócio com **flags, status e condições temporárias** costumam se beneficiar bastante desse tipo de modelagem.  
- Em Mermaid, aproveite a vantagem de ser um formato **texto versionável** e fácil de manter.  
- Compare com outros diagramas: use **flowchart** para decisões e caminhos, **sequence** para interações no tempo, e **state diagram** para máquinas de estado e workflows.