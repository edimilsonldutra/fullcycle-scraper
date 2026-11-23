Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16582)

## Resumo da aula

Retomando o ReAct já estabelecido, a novidade aqui é usar o mesmo ciclo para comparar alternativas em um problema de decisão, não para depurar código. O prompt transforma uma escolha ambígua em uma sequência auditável de verificações: custo, duração, conveniência e impacto no descanso da família. Isso importa porque a melhor opção não é simplesmente a mais barata; ela precisa satisfazer restrições simultâneas de orçamento, horário e fadiga.

O prompt funciona melhor quando separa claramente papel, contexto, opções e critério de saída. Neste caso, o papel é “planejador de viagens”, o contexto inclui composição da família, limite de mil dólares e necessidade de chegada até a noite do dia 10, e as opções já trazem custos e condições. A instrução para alternar pensamento, action e observation força o modelo a inspecionar cada alternativa antes de recomendar uma, em vez de responder por intuição.

A presença de duas crianças pequenas muda o peso de conveniência e cansaço na análise. O fim das aulas no dia 9 ao meio-dia e o casamento na manhã do dia 11 criam uma janela curta, na qual chegar no horário não basta; é preciso chegar com energia suficiente. Em cenários assim, restrições humanas e logísticas entram no prompt como critérios explícitos, porque o modelo tende a ignorá-las se elas aparecerem apenas como detalhe narrativo.

O voo atende ao limite financeiro por pouco: 220 dólares por pessoa para quatro pessoas somam 880, e a bagagem adicional leva o total a 960 dólares. Mesmo não sendo a alternativa mais barata, ele reduz drasticamente o tempo de deslocamento, ficando em cerca de 5 a 6 horas quando se considera aeroporto e procedimentos. Essa combinação de custo aceitável com menor fadiga faz o voo dominar o trade-off quando o evento principal ocorre na manhã seguinte.

O trem é financeiramente viável tanto sem quanto com camas, chegando a 600 ou 800 dólares no total. O problema não está no orçamento, mas na duração de 20 horas, que compromete descanso e conveniência para uma família com crianças. Esse é um bom exemplo de trade-off em que uma opção “cabe no budget” e ainda assim perde, porque falha no critério operacional mais sensível do cenário.

O aluguel de carro parece muito competitivo em custo, já que 60 dólares por dia mais gasolina e pedágio mantêm o total abaixo do teto. Ainda assim, dois dias dirigindo aumentam o desgaste dos pais e a chance de cansaço das crianças, o que piora a condição de chegada para o compromisso do dia 11. Em decisões com agenda apertada, custo baixo não compensa quando o deslocamento consome energia demais da família.

A recomendação final escolhe o voo porque ele oferece o melhor equilíbrio entre custo e conveniência, não porque seja o menor preço absoluto. O valor total permanece dentro do orçamento e a duração curta preserva descanso antes do casamento. Essa é a camada nova do uso de ReAct: comparar opções por trade-off explícito e justificar a decisão com base nas restrições do problema.

Esse formato produz respostas mais longas e consome mais tokens porque cada alternativa precisa ser inspecionada separadamente. Em troca, a decisão fica auditável: é possível verificar se o modelo calculou corretamente, se respeitou as restrições e se a recomendação final realmente decorre das observações. Para agentes e sistemas de apoio à decisão, essa transparência costuma valer o overhead quando o erro custa mais do que os tokens extras.

## Transcrição

00:00

Bom, pessoal, no vídeo anterior a gente fez esse exemplo na nossa bolha de desenvolvimento, né? Conseguir identificar bugs e coisas desse tipo. Mas agora tem um outro exemplo que é um exemplo que pode rodar num agente, pode rodar num sistema da empresa ou qualquer coisa desse tipo, que é o seguinte, tá? Você é um planejador de viagens e você ajuda famílias da melhor forma para sair de Orlando para Nova York no próximo mês.

00:29

Use o estilo do React entre alternar, entre pensamento, action, e o step do action é verificando.

00:40

tempo de voo, custos ou conveniência. Depois de cada ação, faça uma observação que você encontrou e, no final, conclua a resposta final como recomendação. Então, aqui tem o contexto. É uma família com dois adultos e duas crianças de cinco e oito anos. O budget, ou seja, o orçamento que eu tenho, no máximo, mil dólares para transporte, sem incluir o hotel. As datas devem chegar no dia 10 de julho.

01:09

Evening, né? E options aqui pra gente. Quais são as opções que eu tenho agora, que eu quero que ele faça? Primeira opção é avião, voo. 220 dólares por pessoa, na round trip, ou seja, em volta, com tempo de voo de 3 horas, mais 80 dólares de bagagens adicionais. Trem.

01:32

150 dólares por pessoa, 20 horas de jornada, né? E com Wi-Fi e camas disponíveis por 50 dólares por pessoa. Ou aluguel de carro, 60 dólares por dia, dois dias de dirigindo, mais gasolina, mais pedágio, que vai dar mais 250 dólares no total e as crianças vão ficar cansadas em viagens longas.

01:55

Outros detalhes, as crianças, a escola das crianças termina no dia 9, meio-dia, tá? Os pais preferem não viajar muito cansados desde que a família, o casamento que vai acontecer no dia 11, seja de manhã. Comece o pensamento. Então perceba, cara,

02:17

O nível de coisa, olha, a criança fica cansada, as aulas acabam no dia 9, mas a ideia é para a viagem no dia 10, mas tem um caso que eles vão viajar, que eles têm que chegar na noite do dia 10, então que horas que eles têm que chegar? Entende o nível de raciocínio que essas coisas acabam acontecendo aqui? Então, esse tipo de coisa é muito louco porque você consegue ver essa linha de pensamento

02:40

para gerar esses tipos de decisão. Perceba que com o prompt, você consegue fazer ela resolver esses problemas. Agora, se você não é intencional, por exemplo, num prompt de React, raramente você conseguiria uma resposta bem bacana perguntando de uma forma bem simples num GPT ou num agente com um modelo fraco que você esteja trabalhando. Então, eu coloquei, comece a fazer o seu reasoning aqui.

03:06

E agora eu vou pegar, comentar minha mensagem 1, descomentar 2, pegar a resposta da 2, eu não tenho 3, então vou até apagar 3 aqui para a gente não ficar. Maravilha! E vamos executar para ver como é que fica agora esse cara e se ele vai delirar ou se ele não vai delirar e etc. Mas é interessante pelo menos a gente ver a linha de raciocínio e o que ele vai achar melhor a gente tomar de decisão.

03:33

Então vamos lá, por isso que é bastante verboso. Pensamento, a família quer viajar no dia 10, no evening, na tardezinha, sem exceder um orçamento de mil dólares para transporte. Eles também consideram conforto e descanso durante a viagem para que a família

03:55

Chegue de manhã, num casamento, dia 11 de julho, ali. Então, vamos analisar cada opção de viagem com seus fatores. Ação. Verificar o custo e o tempo de viagem de voos para quatro pessoas, considerando o orçamento dele e a necessidade de chegada.

04:20

Daí ele tem a observação, o voo custa 220 dólares por pessoa, totalizando 880 dólares, adicionando 80 dólares de bagagem, traz no total de 960 dólares, e o voo entre si demora 3 horas, mais o tempo adicional do aeroporto e procedimentos, totalizando aproximadamente 5 a 6 horas, essa opção cabe no bolso do cliente e a família chega mais descansada.

04:48

Pensamento. Próximo, vamos considerar a opção de trem agora, para ver se isso realmente, em relação a custo, cabe nessa situação, especialmente em relação a um tempo muito longo de viagem. Então, primeiro ponto, calcular o custo total de tempo para isso.

05:07

e a parte opcional de camas para conforto. Observação, o trem custa 150 dólares por pessoa, totalizando 600 dólares, adicionando as camas das 50 dólares por pessoa, incluindo o total para 800. A jornada demora 20 horas, dando Wi-Fi e entretenimento, mas resulta em cansaço por conta da viagem e essa opção também não dá no budget aqui para eles e etc.

05:30

Aqui, na realidade, a arrival time, essa opção, ela cabe no budget, ou seja, ela cabe no orçamento, mas ela não alinha com a parte do cansaço. Pensamento final, vamos revisar a verificação em relação ao aluguel de carro.

05:51

Então, eu preciso determinar o total e o custo para a duração usando o car rental, aluguel de carro. Alugar um carro por 4 dias custa 240 dólares, mais 250 dólares de gasolina, totalizando 490 dólares, porém, a viagem requer 2 dias.

06:09

Dividindo o que dá mais que o travel time dá mais tempo com risco das crianças ficarem cansadas e risco significante de fadiga. Essa opção cabe no orçamento, mas não é o ideal para montar energia levels before wedding, né? Aqui.

06:26

A resposta final é, opção de voar é a melhor escolha. Custa 960 dólares, cabendo no orçamento, oferece três horas de voo, garantindo que a família chegue na data com um mínimo de fadiga antes do casamento chegar no dia 11.

06:44

Galera, eu sei que eu tive que ler pra caramba aqui, mas a questão que eu quero trazer é... Cara, olha como é que é incrível essa linha de pensamento que ela toma. Simplesmente pelo fato de você falar, pra ela pensar, agir e observar.

07:00

Então, isso que é o React na prática, tá? E você tem agentes que trabalham já nesse formato, você tem os modelos de IA, dependendo de como que você trabalha, naturalmente eles já fazem assim, ou você pode pegar o modelo e fazer exatamente o prompt como eu coloquei para você ter esses tipos de resposta. O grande ponto é que é token pra caramba, mas você consegue entender muito melhor ainda a linha de raciocínio que ele utilizou para você ver se ele tomou realmente uma decisão certa aí nesse caso.

07:29

Fechou? Então, espero que você tenha curtido essa parte aqui de React.

## Resumo IA

**Abreviações**
- **ReAct**: *Reasoning and Acting* — padrão de interação em que o modelo alterna entre raciocínio, ação e observação.
- **prompt**: instrução/texto de entrada dado ao modelo para orientar a resposta.
- **budget**: orçamento.

**Resumo**
A aula apresentou um uso prático do padrão ReAct para tomada de decisão, em vez de depuração de código. O instrutor mostrou como estruturar um prompt para atuar como um “planejador de viagens” e comparar alternativas de transporte para uma família de dois adultos e duas crianças, saindo de Orlando para Nova York. O objetivo era recomendar a melhor opção considerando simultaneamente custo, tempo de deslocamento, conveniência e nível de cansaço da família, com restrição de orçamento máximo de mil dólares e chegada na noite do dia 10, antes de um casamento na manhã do dia 11.

O fluxo explicado consistiu em alternar explicitamente entre pensamento, action e observation para avaliar cada alternativa separadamente. Primeiro, o voo foi analisado: 220 dólares por pessoa, mais bagagem, totalizando 960 dólares, com tempo efetivo curto de viagem e menor fadiga. Depois, o trem foi verificado: apesar de caber no orçamento, a duração de 20 horas o tornava pouco conveniente para uma família com crianças e com agenda apertada. Em seguida, o aluguel de carro foi avaliado: embora barato, o desgaste de dois dias dirigindo, somado ao cansaço das crianças, prejudicava a chegada descansada para o evento. Ao final, o modelo recomendou o voo como melhor equilíbrio entre custo e conforto, demonstrando como o ReAct ajuda a tornar a decisão auditável e baseada em critérios explícitos.

**Pontos de atenção**
- Separar claramente **papel, contexto, opções e critério de saída** no prompt melhora muito a qualidade da resposta.
- Restrições humanas e logísticas, como **cansaço, presença de crianças e janela de chegada**, precisam ser explicitadas; se ficarem só como narrativa, o modelo tende a ignorá-las.
- A melhor opção **não é necessariamente a mais barata**; é a que melhor satisfaz o conjunto de restrições.
- Avaliar cada alternativa individualmente evita respostas por intuição e reduz o risco de decisão superficial.
- O voo, mesmo não sendo o menor custo absoluto, foi favorecido por **equilibrar orçamento e conveniência**.
- O trem mostrou que uma opção pode **caber no orçamento e ainda assim ser inadequada** por tempo excessivo e fadiga.
- O aluguel de carro evidenciou que **baixo custo não compensa desgaste e perda de energia** em cenários com compromisso logo após a viagem.
- O uso de ReAct gera **respostas mais longas e maior consumo de tokens**, o que é um trade-off esperado.
- Em compensação, a decisão fica **auditável e verificável**, útil em agentes e sistemas de apoio à decisão.
- A abordagem depende de o prompt ser intencionalmente estruturado; em modelos mais fracos ou prompts simples, a qualidade tende a cair.