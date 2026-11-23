Módulo: Design Docs com IA\
Aula: [Alinhando expectativas](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/276/conteudos?capitulo=276&conteudo=17231)

## Resumo da aula

Estávamos na fase de pesquisa, que é um ponto importante. Tive essa fase inicial para chegar ao relatório final. Tenho a fase 1, onde faço toda a pesquisa, e tenho esta outra parte aqui, que será extremamente importante. No final das contas, ela consiste em fazer uma análise e um planejamento de como escolher o que entra e o que não entra na aplicação.

Por que estou dizendo isso? Porque algumas linguagens, dependendo da situação, trabalham muito com concorrência, então isso precisa estar presente. Outras linguagens envolvem muito o trabalho com containers. Se fizer sentido, incluo Docker. Trago diversas seções e algumas delas são opcionais. Baseado nessas seções, ele precisa elencar e verificar: será que preciso ter Docker? Será que a parte de tipagem faz sentido? Coloquei todas essas partes para avaliar se realmente faz sentido ter em determinada linguagem. Dependendo da linguagem, pode não fazer sentido ter a parte de benchmarks.

No final, ele calcula quantas seções ficaram e cria um mapeamento de numeração para identificar quais são as seções. Depois, documenta as decisões, explicando por que está fazendo aquilo, e finaliza o Project Stack, os parâmetros e tudo mais. Nesse ponto, ele já tem quase tudo para começar: as seções, a pesquisa, os detalhes, as versões, a linguagem.

E aqui está a grande pegadinha que mencionei anteriormente. Por isso, na fase 3, temos a Geração de Conteúdo em Múltiplas Fases. Por quê? Porque preciso gerar esse documento de forma parcial, caso contrário, corremos o risco de estourar a memória ou gerar arquivos grandes demais de uma vez. Então, defini que a documentação deve ser gerada separando em pelo menos quatro subfases, mantendo cada parte abaixo de 32 mil tokens. Trinta e dois mil tokens é um limite razoável. Vocês podem testar com seus modelos; nos meus testes, funcionou bem dessa forma.

Coloquei também que cada seção tem entre 30 e 50 linhas. Foram muitos detalhes, e preciso que entendam: deu muito trabalho fazer isso funcionar. Obviamente, não é o comando perfeito, mas ele faz com que vocês não partam do zero, e é isso que quero transmitir e dar clareza.

As regras gerais incluem: numerar, verificar qualidade, consistência, autenticidade específica da linguagem (convenções, boas práticas), completude, e assim por diante. Ele vai separando fase a fase, seção por seção, até chegar ao documento de checklist.

Essa checklist não é a de pré-commit, é uma validação final de tudo o que foi gerado. Ele passa revalidando e, no final, verifica se o documento está entre 1.000 e 1.500 linhas. Por quê? Porque, na maioria das vezes que testei, mesmo pedindo para gerar um documento com menos de 1.500 linhas, ao dar os apêndices, o documento acabava indo para 2.000, 2.500, 3.000 linhas. Quando chega na checklist final, ele vê que deveria ter até 1.500 e tem 2.000. Então, ele identifica onde há muita verbosidade e simplifica para caber nesse limite.

É um comando extenso, com muitos detalhes, exemplos e um template final. São muitas linhas também, mas é aquele tipo de documento que você gera uma vez e não fica alterando o tempo todo.

Então, aqui está o comando. Para entender como ele funciona, vou dar um exemplo rodando agora. Obviamente, não preciso esperar, mas quero que vocês tenham a ideia de como podem utilizá-lo. Provavelmente, vocês vão pegar esse comando e rodar em qualquer tipo de agente, e ele vai funcionar da mesma forma.

## Transcrição

00:00

Bom, pessoal. Então, a gente estava nessa fase de pesquisa, né? Então, esse é um ponto importante. Então, eu tive essa minha fase inicial, né? Para eu ter o meu report final. Eu tenho a minha fase 1, onde eu tenho que fazer toda a minha pesquisa. E eu tenho essa minha outra parte aqui, tá? Que ela vai ser extremamente importante. Que vai ser o quê no final das contas?

00:28

eu consegui fazer uma análise e um planejamento de como que...

00:36

eu vou escolher o que entra e o que não entra ali na minha aplicação, tá? Por que que eu tô dizendo? Porque tem linguagens que, dependendo da situação, trabalham muito com concorrência. Então vai ter que ter... Ah, tem linguagens que eu vou trabalhar ou falo muito sobre containers. Então, se faz sentido, tá? No parque de container vai ter Docker. Então, eu trago aqui diversas seções, tá? E eu falo que

01:02

Algumas dessas seções são opcionais. Então, baseado nessas seções, ele vai ter que elencar e ver. Será que eu preciso ter docker? Será que a parte de tipagem faz sentido? Então, eu coloquei todas essas partes aqui para ver se realmente...

01:20

Faz sentido ter isso em determinada linguagem. Dependendo de uma linguagem, não faz sentido ter a parte de benchmarks. E aí, no final, ele vai calcular quantas sessões ficaram, e aí ele vai criar um mapeamento de numeração para saber quais são as sessões. Depois, ele vai documentar as decisões, por que ele está

01:37

fazendo isso, e aí ele vai finalizar ali o Project Stack, os parâmetros e tudo mais, e agora ele tem todas as sessões, ele tem a pesquisa, ele já tem os detalhes, as versões, a linguagem, então basicamente a partir daqui ele já tem quase tudo para ele começar.

01:59

E aqui que é a grande pegadinha que eu tinha falado pra você, né? Por isso que tá aqui, ó, fase 3, Multiphase Content Generation. Por quê? Porque...

02:08

Eu preciso gerar esse documento de forma parcial, porque senão vai dar ruim na hora de estourar a memória, na hora de gerar arquivos tão grandes dessa forma. Então, eu coloquei que um output para gerar a documentação, separar ele pelo menos em quatro subfases para fazer a geração, e que ele fique embaixo de 32 mil tokens. Nossa Wesley, 32 mil tokens é... Você pode testar, depois você vê com o seu modelo, com todos que eu testei, funcionou bem dessa forma.

02:37

E aí eu coloquei, olha, pra todas as fases, cada sessão tem 30, 50 lins, então foi detalhes e galera, você tem que entender assim, deu muito trabalho pra fazer isso funcionar, obviamente não é o comando perfeito, mas faz com que você não parta do zero e é isso que eu quero trazer e dar clareza pra você em relação a isso, tá?

02:56

as regras gerais. Então, eu numero, depois eu verifico a qualidade, depois eu verifico a consistência, depois eu verifico a parte de Language Specific Authenticity. Na realidade, ele verifica as convenções, as boas práticas e tudo mais, a parte de completeness, e aí vai todas aquelas partes gigantes dos nossos documentos. Então,

03:26

aí ele vai separando fase a fase, sessões por sessões, em relação a tudo isso, até chegar no documento do checklist. E esse documento do checklist é uma validação final. Então, o que é essa validação? Não é aquela checklist de pré-commit, não, tá? É o quê? É uma validação final de tudo que ele gerou, ele vai passar revalidando.

03:48

E o mais interessante é que nessa checklist, no final, ele vai verificar a história entre 1.000 e 1.500 linhas. O porquê? Porque, na maioria das vezes que eu testei, mesmo lá em cima eu tendo pedido para ele gerar um documento com menos de 1.500 linhas, na hora que ele vai dando o append, às vezes o documento vai para 2.000, 2.500 linhas, 3.000 linhas ou coisas desse tipo. Aí, quando eu falo que o documento, nessa final checklist, que ele tem que ter entre 1.000 e 1.500,

04:15

ele vai olhar aquilo e ele vai falar, opa, era pra ter até 1.500 e eu tenho 2.000. Então, deixa eu ver onde tem muita verbosidade e deixa eu simplificar pra fazer caber nessa quantidade de linhas, tá? E aí, ele vai fazer aqui e ele vai, então, resumir o que a gente tem que fazer, tá? Então...

04:35

É um comando, é bastante coisa, depois você pode olhar, aí tem exemplos, aí tem o template final, ou seja, é algo bem grande, tem bastante linhas também esse documento, mas é aquele tipo de documento que você gera uma vez e você não fica mudando o tempo todo, tá? Então, tá aqui esse comando pra gente...

04:55

entender como é que esse cara funciona eu vou dar um exemplo rodando ele agora obviamente eu não preciso esperar mas eu queria só que você tivesse a ideia de como que você pode utilizar e novamente provavelmente você pegar esse comando e rodar em qualquer tipo de agente já esse cara vai funcionar ali da mesma forma

## Resumo IA

**Resumo**  
A aula descreve a fase de pesquisa e planejamento de uma documentação técnica voltada à definição de um Project Stack. O instrutor explica que, após a pesquisa inicial, é necessário analisar quais tópicos entram ou não na aplicação, conforme o contexto da linguagem e da solução. Alguns itens são opcionais e dependem da tecnologia escolhida, como concorrência, containers, Docker, tipagem e benchmarks. Com base nisso, o processo faz um levantamento das seções necessárias, conta quantas permanecem, cria um mapeamento de numeração, documenta as decisões tomadas e consolida parâmetros como versão, linguagem e demais detalhes do projeto.  

Em seguida, ele apresenta a fase de geração de conteúdo em múltiplas etapas, destacando que a documentação não deve ser produzida de uma só vez para evitar estouro de memória e arquivos grandes demais. Para isso, a geração é dividida em pelo menos quatro subfases, com limite de cerca de 32 mil tokens por parte, e cada seção deve ter entre 30 e 50 linhas. O fluxo inclui regras gerais de numeração, verificação de qualidade, consistência, autenticidade específica da linguagem, boas práticas e completude, avançando fase a fase até chegar ao documento final de checklist. Essa checklist final não é de pré-commit, mas uma validação completa de tudo o que foi gerado. Ao final, o sistema confere se o documento ficou entre 1.000 e 1.500 linhas e, se houver excesso de verbosidade, simplifica o conteúdo para caber no limite. O instrutor ressalta que se trata de um comando extenso, com muitos detalhes, exemplos e template final, pensado para ser gerado uma vez e reutilizado em agentes sem mudanças constantes.

**Pontos de atenção**  
- A fase de pesquisa é essencial para orientar todo o relatório final e evitar decisões sem base.  
- Nem todas as seções fazem sentido para toda linguagem; é preciso avaliar caso a caso.  
- Concorrência, containers, Docker, tipagem e benchmarks devem ser incluídos apenas quando forem pertinentes ao contexto.  
- A documentação deve registrar claramente por que cada decisão foi tomada.  
- A geração do conteúdo precisa ser quebrada em múltiplas subfases para evitar estouro de memória e arquivos grandes demais.  
- O limite de aproximadamente 32 mil tokens por subfase foi adotado como medida prática de segurança.  
- Cada seção deve manter tamanho controlado, entre 30 e 50 linhas.  
- As verificações finais devem cobrir numeração, qualidade, consistência, completude e autenticidade específica da linguagem.  
- A checklist final serve para revalidar todo o conteúdo gerado, e não substitui uma etapa de pré-commit.  
- É importante controlar a verbosidade: mesmo com limite definido, o documento pode crescer além do esperado ao adicionar apêndices.  
- Se o documento ultrapassar 1.500 linhas, o processo deve identificar excesso de texto e simplificar o conteúdo.  
- O comando é extenso e complexo, mas foi estruturado para evitar começar do zero e para funcionar de forma reutilizável em diferentes agentes.