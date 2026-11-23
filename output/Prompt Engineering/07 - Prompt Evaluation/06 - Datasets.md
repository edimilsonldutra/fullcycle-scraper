Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16861)

## Resumo da aula

Avaliação de prompt depende de um conjunto de casos estruturados antes de qualquer execução. Sem esse insumo, não existe base comum para medir comportamento, comparar versões nem validar pressupostos com consistência. O ponto que costuma travar equipes não é a ideia de avaliar, mas a preparação dos dados brutos em um formato reutilizável. Por isso, o dataset deixa de ser detalhe operacional e vira parte central do experimento.

Um dataset pode nascer de execuções reais de produção ou de geração sintética com IA. No primeiro caminho, a equipe coleta casos reais, normaliza os dados e os transforma em uma estrutura comparável; isso tende a refletir melhor o uso do sistema, mas exige limpeza e organização. No segundo, um prompt bem construído pede à IA múltiplos exemplos cobrindo variações específicas; isso acelera a montagem inicial, especialmente quando ainda não há volume real suficiente. As duas estratégias são válidas, desde que o resultado final seja estruturado e útil para testar hipóteses.

LangSmith funciona aqui como a ferramenta usada para cadastrar, armazenar e executar os exemplos do dataset. A conta de desenvolvedor permite começar com baixo atrito: criar conta, gerar API key e rodar experimentos pequenos sem necessidade de infraestrutura própria. Em cenários não produtivos e com poucos exemplos, isso é suficiente para preparar a base de testes do capítulo. O detalhe importante não é a ferramenta específica, mas o fato de ela impor uma organização explícita dos casos.

Retomando o cenário de revisão de código, cada exemplo do dataset é representado como um JSON com pelo menos input e output. O input descreve a tarefa que a IA deve executar, incluindo linguagem, instrução e o trecho de código a ser analisado. O output registra a resposta esperada para aquele caso, servindo como referência para a avaliação posterior. Essa estrutura transforma um teste informal em um caso reproduzível.

Além de input e output, o dataset inclui metadados como tópico e categoria. No exemplo, o tópico identifica o domínio técnico do caso, como HTTP Client, enquanto a categoria classifica uma dimensão relevante, como robustez. Esses campos não são ornamentais: eles permitem filtrar, agrupar e interpretar resultados por tipo de problema. Quando uma versão do prompt falha mais em uma categoria específica, os metadados ajudam a localizar a regressão.

O caso prático usa código Go como entrada e pede que o sistema analise o trecho e retorne um JSON com findings e um summary curto. Os findings descrevem problemas encontrados, como ausência de timeout, linha afetada, descrição e severidade; o summary consolida as principais correções sugeridas. Com cerca de 18 exemplos desse tipo, o dataset já fornece uma base inicial para testar se o prompt identifica problemas de forma consistente. O valor do exemplo não está apenas no código Go, mas no fato de cada caso já nascer com entrada, saída esperada e contexto classificatório.

O dataset não substitui o prompt; ele prepara o terreno para medir o efeito do prompt sobre os mesmos casos. Retomando a referência já estabelecida de ground truth, o output esperado de cada exemplo passa a ser a base contra a qual a saída gerada será comparada. A partir daí, o processo de evaluation deixa de ser improvisado e passa a operar sobre entradas repetíveis. Em outras palavras, o prompt só pode ser avaliado de forma técnica quando existe um conjunto de exemplos pronto para alimentá-lo.

## Transcrição

00:01

Bom, pessoal, agora que eu dei uma visão bem geral, dá pra perceber que tem bastante coisa que a gente vai ter que cobrir, é importante agora a gente colocar o pé na areia e a gente começar a brincar com tudo isso. Então, somente pra você saber, eu criei um dataset. Esse dataset, o que é no final das contas? É um conjunto de dados estruturados,

00:26

que eu vou criar em uma ferramenta. Ou seja, eu vou utilizar a Langsmith para dar esses exemplos, tá, galera? Mas existem diversas ferramentas que fazem isso e existe a forma manual também de você fazer isso, tá? Mas, obviamente, eu vou utilizar a Langsmith para fazer isso, estou utilizando a conta de desenvolvedor, ou seja, basicamente é entrar, criar uma conta gratuita, pelo menos no momento dessa gravação,

00:55

criar uma API key e fazer suas execuções. Se você passar muitas execuções, ele vai te dar um rate limit no final das contas ou vai querer te cobrar, mas como ali não são muitos exemplos ou a gente não está fazendo nada em produção, é super ok a gente trabalhar ali com o langsmith, tá? Mas isso aí, no momento, é detalhe. O importante a gente entender é que, para a gente avaliar algo, eu tenho que ter o dado antes para eu avaliar.

01:22

E esses dados têm que estar estruturados. Então, uma das coisas que eu percebo, e que acabam sendo mais chatas no meio desse processo, é realmente você conseguir ter um dataset expressivo que consiga testar e validar os seus pressupostos no meio de todo esse processo. Como que você, no final das contas, consegue ter um bom dataset? Você tem

01:48

dois pontos que você pode fazer como dataset. Um ponto é realmente pegar as execuções reais que você teve em produção, pegar esses dados simplesmente e normalizar esses dados e tornar ele numa estrutura que a gente vai utilizar, por exemplo.

02:07

Uma outra forma de você também conseguir fazer o seu dataset é usar, inclusive, IA para fazer isso. Então, você pode criar um Bond Prompt e pedir para IA gerar um dataset com não sei quantas opções diferentes, cobrindo determinados detalhes, e ali você vai ter o seu dataset que você vai poder trabalhar.

02:27

Beleza? Mas, de forma geral, o dataset é algo que, no início, é algo que, vamos dizer, trava a maioria das pessoas. Porque eu quero medir, mas eu não tenho os dados brutos, e daí eu tenho preguiça, ou eu não sei fazer esses dados brutos, eu não sei formato, ou coisa desse tipo. E aí, acaba travando todo esse processo ali pra gente iniciar qualquer tipo de avaliação, tá?

02:52

No nosso caso, o exemplo que eu vou mostrar aqui para vocês, eu tenho um dataset que está pronto. E eu vou dar um exemplo aqui para vocês. Deixa eu só achar aqui o meu querido exemplo. Achei aqui, galera. Então, é o seguinte.

03:12

E você olhar o que eu tenho. Eu tenho um JSON estruturado. E o que eu tenho nesse JSON? Eu tenho o campo de input e output. Basicamente, é isso que eu tenho. O meu dataset, no final das contas, é um dataset simples que eu criei. E a ideia é que o nosso prompt tenha que analisar...

03:37

um código que a gente vai trazer e mostrar o que ele encontrou de problemas ou qualquer coisa desse tipo. Então, eu tenho um dataset com acho que são 18 exemplos que eu criei. Aqui está um exemplo somente para você entender a estrutura do nosso JSON. Então, eu tenho input, a linguagem é Go, a tarefa é analise e retorne o JSON com os problemas encontrados em findings e

04:02

um sumário curto, ou seja, um resumo curto. Então, aqui eu tenho o código que ele vai ter que olhar, e eu tenho aqui metadados, que o tópico é um HTTP Client, e a categoria é o quanto essa parada é robusta. E como output, o que ele tem que trazer para mim no final das contas, que eu pedi?

04:21

Findings e Summary. Então, eu tenho o meu Findings. Então, aqui ele trouxe o Missing, Timeout, a linha 8, Description, o tanto de severidade e etc, etc, que são os Findings que eu tenho. E aqui eu tenho o Summary. Adicionar Timeout via Contexto, checar erros de HTTP e o Redock. Então, ele trouxe

04:43

Esse exemplo. Então, eu tenho um dataset com diversos casos desse aqui, tá? Ou seja, esses vão ser os meus dados brutos que a gente vai acabar passando para a IA. A IA vai fazer essa nossa tarefa, vai fazer essa análise e vai desenvolver. O grande ponto aí no meio de toda essa história é que para ele fazer essa análise, etc., o que vai acontecer no final das contas? Nós vamos ter que ter um prompt no meio da história.

05:09

E é a partir daí que a gente começa, então, o nosso processo de evaluation. Então, no nosso próximo vídeo, agora que a gente falou de dataset, eu vou mostrar para vocês a código e a gente vai partindo daí.

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **API key** — Chave de acesso à API  
- **JSON** — JavaScript Object Notation  
- **HTTP** — Hypertext Transfer Protocol  
- **Contexto** — Context (no trecho, uso de contexto para controlar execução/timeout)

**Resumo**  
A aula explicou que a avaliação de prompts só faz sentido quando existe um dataset estruturado previamente, pois é esse conjunto de casos que serve como base comum para medir comportamento, comparar versões e validar hipóteses de forma consistente. O instrutor destacou que o principal desafio não é “avaliar”, mas organizar os dados brutos em um formato reutilizável.

Foram apresentadas duas formas de construir o dataset: a partir de execuções reais de produção, que precisam ser coletadas, normalizadas e estruturadas; ou por meio de geração sintética com IA, usando um bom prompt para criar exemplos cobrindo variações e cenários desejados. Em ambos os casos, o objetivo é obter casos úteis para teste e comparação.

Como ferramenta de apoio, foi usada a LangSmith para cadastrar, armazenar e executar os exemplos do dataset, com conta de desenvolvedor, criação de API key e experimentos pequenos. O instrutor ressaltou que a ferramenta é menos importante do que a disciplina de estruturar os casos.

No exemplo prático, cada item do dataset foi representado por um JSON com campos de input e output. O input continha a tarefa, a linguagem, a instrução e o trecho de código a ser analisado; o output trazia a resposta esperada, funcionando como ground truth para a avaliação. Além disso, foram adicionados metadados como tópico e categoria, úteis para agrupar, filtrar e interpretar resultados por tipo de problema.

O caso mostrado usava código Go e pedia análise de um trecho com retorno em JSON contendo findings e um summary curto. Os findings listavam problemas específicos, como falta de timeout, com linha, descrição e severidade, enquanto o summary sintetizava as correções principais. O exemplo reforçou que o dataset prepara o terreno para o evaluation, permitindo comparar a saída do prompt com a resposta esperada em casos repetíveis.

**Pontos de atenção**  
- Sem dataset estruturado, não há base confiável para avaliar prompt.  
- O maior gargalo costuma ser preparar os dados brutos, não a avaliação em si.  
- Dados de produção precisam ser normalizados antes de virarem dataset.  
- Geração sintética com IA é válida, mas deve produzir exemplos realmente úteis e variados.  
- O formato do dataset precisa ser consistente e reproduzível, não apenas “informal”.  
- Input e output são o núcleo do caso; sem isso, o teste perde comparabilidade.  
- Metadados como tópico e categoria não são decorativos: ajudam a identificar regressões por tipo de problema.  
- O output esperado funciona como ground truth e deve ser a referência da comparação.  
- LangSmith facilita o processo, mas a ferramenta não substitui a organização dos casos.  
- Em contas de desenvolvedor, podem existir limites de execução e eventual cobrança conforme uso.  
- O prompt não é avaliado isoladamente; ele precisa ser testado sobre um conjunto fixo de exemplos.  
- Casos práticos bem definidos, mesmo em quantidade moderada, já permitem uma base inicial de avaliação.