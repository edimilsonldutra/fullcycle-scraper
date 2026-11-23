Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16378)

## Resumo da aula

LLMs foram otimizados para linguagem natural, onde a estrutura sequencial, a coesão textual e a previsão do próximo token são centrais. Em imagem, esse raciocínio não se aplica da mesma forma, porque a organização visual não depende de uma leitura linear da esquerda para a direita como no texto. Isso exige arquiteturas voltadas para coerência espacial e aparência visual, não apenas para continuidade linguística. Por isso, a geração de imagem seguiu caminhos diferentes dos modelos usados em texto.

GANs surgiram para enfrentar a baixa qualidade das imagens geradas, especialmente no contexto em que resultados visuais ainda eram muito artificiais e pouco utilizáveis. O ganho principal foi produzir saídas mais realistas, aproximando a geração sintética da aparência esperada em imagens do mundo real. Esse avanço abriu espaço para aplicações em arte, moda, jogos e design, onde qualidade visual é requisito básico. O valor do GAN está justamente em empurrar a geração para um nível de realismo que antes era difícil de alcançar.

A arquitetura de um GAN se apoia em dois componentes com papéis opostos: o gerador cria amostras sintéticas e o discriminador tenta distinguir essas amostras dos dados reais. Essa dinâmica competitiva força o gerador a melhorar continuamente, porque ele só “vence” quando produz algo suficientemente convincente para enganar o discriminador. O discriminador, por sua vez, também evolui ao aprender a separar melhor o falso do real. O treinamento acontece nesse ciclo de refinamento mútuo.

Imagine um sistema tentando gerar imagens de notas de 10 reais. O gerador produz versões sintéticas, enquanto o discriminador recebe tanto exemplos reais quanto gerados e decide quais parecem autênticos. Cada erro do discriminador ou do gerador vira sinal de ajuste para a próxima iteração, fazendo a saída sintética se aproximar gradualmente do padrão real. A lógica do exemplo não depende de dinheiro em si; ele apenas ilustra como o GAN aprende por confronto entre criação e validação.

GANs são especialmente fortes quando o objetivo é produzir imagens visualmente convincentes, como rostos humanos, peças de moda, arte digital e ativos para jogos. Nesses cenários, o critério dominante é a aparência final da saída, e não necessariamente o controle fino de cada atributo gerado. O modelo tende a ser valioso quando o realismo perceptual importa mais do que a interpretabilidade interna do processo. Essa característica explica por que GANs ganharam relevância em domínios criativos.

Além do realismo, existe outro problema importante: controlar o que será gerado. VAEs atacam esse ponto ao permitir manipular variáveis latentes para direcionar a saída, em vez de apenas produzir uma amostra plausível. Isso é útil quando a especificação precisa incluir atributos mais detalhados, como “um homem sorrindo, de cabelo curto e bigode”. O foco deixa de ser apenas gerar algo realista e passa a incluir geração orientada por características.

Um VAE é descrito aqui como um modelo probabilístico que aprende por meio de um encoder e de um decoder. O encoder comprime os dados em uma representação latente, e o decoder reconstrói a saída a partir dessa representação. Essa estrutura permite navegar por atributos internos da amostra gerada com mais controle do que no caso dos GANs. O resultado é uma geração mais organizada quando se quer especificidade.

Em comparação com GANs, VAEs aparecem como modelos matematicamente mais estáveis e mais controlados. Essa estabilidade os torna úteis em situações em que detalhes específicos da saída importam mais do que maximizar apenas o realismo visual bruto. A mesma lógica se estende além de imagem e alcança som e voz, onde a modelagem mais controlada ajuda a produzir resultados mais realistas. O ponto central é a troca entre realismo competitivo e controle probabilístico da geração.

## Transcrição

00:00

Fala galera, deixa eu falar de um capítulo super curtinho aqui só pra contar pra vocês sobre um outro aspecto da IA generativa, tá? A gente falou bastante sobre IA generativa olhando muito pra LLM, beleza? Por que que a gente fez isso? Porque no nosso dia a dia a maior parte do tempo a gente vai tá falando de geração de texto, né? No dia a dia

00:20

principalmente de quem trabalha com tecnologia ou quem está trabalhando com geração de codificação e coisas desse tipo, a geração de texto acaba sendo muito mais latente. Então você usa muito mais, tanto que a gente está tendo uma alta escala no que a gente fala de geração de texto, mas tem outras tantas matérias que vão precisar de outras coisas como geração de imagem. Então para quem é de marketing, publicidade, etc, que estiver assistindo esse vídeo, você também tem toda uma parte de geração de imagem que pode te ajudar.

00:44

Quando a gente está falando dessa geração de imagem, a gente tem algumas outras estratégias por trás que fazem isso funcionar. Normalmente, essas estratégias são diferentes do que a gente tem do LLM. O LLM, como a gente falou desde o começo, foi pensado para resolver alguns problemas muito ligados à linguagem, à nossa linguagem de fala, que é a linguagem natural.

01:09

Então essa linguagem natural, ela precisa ter algumas coisas resolvidas que a gente veio falando ao longo do tempo do curso aqui. E que pra uma imagem não é necessariamente uma realidade. Então quando a gente tá falando da linguagem natural, você precisa resolver aquela coesão textual, você precisa resolver como é que as palavras se formam, você precisa resolver como é que você gera

01:28

um texto pensando na próxima palavra que vai aparecer, tudo aquilo que a gente falou do bigrama até chegar no que a gente tá falando agora mais moderno das LLMs cheias de coisas por dentro que foram sendo resolvidas ao longo dos anos. Pra imagem é diferente, pra imagem a coesão fica um pouco diferente, é uma coesão de imagem não uma coesão textual, então nem sempre

01:50

vai correlacionar, por exemplo, você não pode dizer que uma imagem vai ter sempre uma relação direta da esquerda para a direita como você faz com texto, então você precisa ter outras estratégias. Nessas estratégias nasceu um negocinho que chama GANS

02:05

os GANs eles vieram para resolver um pouco dessa necessidade de geração visual ali por volta de 2014 as gerações de imagem eram muito rudimentares, muito difíceis, baixa qualidade a gente tinha uma aparência muito artificial você não conseguia gerar uma imagem mais ultra realista mais parecida com a realidade mesmo era muito difícil de você conseguir colocar algo ali

02:29

que fosse utilizado em ampla escala pela comunidade, porque não chegava nem perto do que, por exemplo, os editores de imagem conseguiam fazer. Os GANs vieram para resolver um pouco disso. Eles começam a trabalhar de uma forma um pouquinho diferente, eu já vou falar dessa forma para vocês, mas ele veio para trabalhar de uma forma um pouquinho diferente essa estrutura aqui. Então ele veio conseguindo criar imagens mais realistas e mais próximas do que a gente imagina que deveria ser uma imagem com uma alta qualidade,

02:58

e ele abriu caminho ali pra gente conseguir usar então também a Gen AI pra arte, moda, pra jogos, design, esse tipo de coisa. Então consegue ajudar muito a gente pra ir pra outras matérias também. E como que funciona isso aqui? Ele trabalha basicamente com dois carinhas. Um deles vai ser o gerador e o outro o discriminador, tá bom? O gerador, você pode imaginar ele como se fosse um falsificador. E o discriminador como um policial. Mais ou menos, não é tão assim, mas é mais ou menos isso, tá?

03:28

Então pense assim, o gerador vai ficar tentando gerar coisas falsas e o discriminador vai ficar falando que é falso. Então vamos fazer o seguinte, imagina que o gerador está gerando imagens de notas falsificadas, beleza? Na verdade ele está tentando gerar imagens de notas.

03:47

esquece falsificado está tentando gerar imagens de 10 reais a nota de 10 reais e o discriminador tem que dizer se aquilo é falso se não é falso então ele vai gerar uma falsa uma real uma falsa uma real duas falsas uma real ele vai ficar gerando o discriminador vai ficar falando isso aqui é falso é real isso aqui é falso aqui é real isso aqui é falso aqui é real

04:06

Quando ele vai gerando isso, ele vai alimentando para o girador cada vez ficar mais próximo de gerar só coisas reais. Então você vai preparando esse girador para ele entender o que é real e o que é falso. Ao longo do tempo ele vai ficando cada vez mais afinado e vai começando a entender o que é falso e o que é real. Então com o tempo os dois vão melhorando e vão conseguindo gerar cada vez notas mais realistas na saída desse negócio.

04:29

ele é muito bom para gerar, por exemplo, rosto humano, para gerar coisas de moda, artes, jogos, como eu falei para vocês. Então a gente conseguiu dar esse salto usando os GANs. Tem um outro carinha que eu queria falar com vocês também, que ele traz uma outra ideia também, mas também complementar, são os VAEs. O VAEs ele veio com uma ideia de, além de gerar as imagens realistas, você conseguir controlar

04:52

direto o que que você tá gerando, tá bom? Então pensa o seguinte, imagina que eu quero gerar uma imagem realista de um homem sorrindo de cabelo curto e bigode. O VAE e eu pra conseguir dar esta camada de tipo, olha, eu quero direcionar o que eu quero numa saída, não quero só um homem, eu quero conseguir aumentar o leque aqui e dizer que não é só um humano que eu quero, eu quero detalhes, eu quero trazer pra ele uma manipulação das variáveis mais latentes pra gente conseguir chegar num resultado um pouco melhor.

05:21

Então, com isso a gente consegue evoluir a visão de geração de imagem. Então, aqui você tem esses dois contextos que vão fazer isso. O VAE, no final das contas, é um modelo probabilístico que ele vai aprender com um negócio chamado encoder, que ele comprime

05:37

toda a estratégia e depois um decoder que vai reconstruir os dados para a geração do que você precisa, tá bom? Então ao contrário do que você tem nos GANs, esses caras eles são mais estáveis numa visão matemática, eles são mais controlados, eles não abrem tanto

05:53

mas em compensação eles trazem uma visão com mais qualidade quando você fala de algo muito específico, tá bom? Então aqui você consegue evoluir em algumas outras matérias onde você precisa de mais detalhes do que está sendo gerado, fechou? Acho que aqui basicamente esse cara também ajudou a gente não só na imagem mas por exemplo no som, ele conseguiu evoluir a camada de voz que antes era um pouquinho mais complicada

06:15

conseguiu deixar isso mais realista também, tá bom gente? Bom, é basicamente isso, já já a gente volta então pra aprofundar ainda mais em LLMs, tá bom? A gente vai voltar a falar de LLMs e começar a aprofundar um pouco mais nessa matéria.

## Resumo IA

**Abreviações**  
- **IA** — Inteligência Artificial  
- **LLM** — *Large Language Model*  
- **GAN** — *Generative Adversarial Network*  
- **VAE** — *Variational Autoencoder*  
- **AI/Gen AI** — Inteligência Artificial Generativa  

**Resumo**  
A aula apresentou uma visão introdutória sobre geração de imagens na IA generativa, mostrando por que as técnicas usadas em LLMs não se aplicam diretamente ao domínio visual. O instrutor explicou que modelos de linguagem são otimizados para estrutura sequencial, coesão textual e previsão do próximo token, enquanto imagens exigem coerência espacial e aparência visual, sem depender de uma leitura linear como no texto. A partir dessa diferença, foram introduzidas arquiteturas específicas para imagem, com destaque para GANs e VAEs.

Os GANs foram apresentados como uma resposta à baixa qualidade das primeiras imagens geradas por IA, que eram artificiais e pouco realistas. A lógica do GAN foi descrita como uma competição entre dois componentes: o gerador, que cria amostras sintéticas, e o discriminador, que tenta identificar se as amostras são reais ou falsas. O instrutor usou o exemplo de notas de 10 reais para ilustrar como o sistema aprende por confronto contínuo, em um ciclo de refinamento em que erros de um lado alimentam melhorias no outro. Esse mecanismo permitiu elevar o realismo das saídas e abriu espaço para aplicações em arte, moda, design e jogos, onde a aparência final é o principal critério.

Em seguida, a aula abordou os VAEs como uma alternativa complementar, voltada não só ao realismo, mas também ao controle do que é gerado. Foi explicado que o VAE permite manipular variáveis latentes para direcionar atributos específicos da saída, como gerar “um homem sorrindo, de cabelo curto e bigode”. Na visão do instrutor, o VAE é um modelo probabilístico baseado em encoder e decoder: o encoder comprime os dados em uma representação latente, e o decoder reconstrói a saída a partir dela. Em comparação com GANs, os VAEs foram descritos como matematicamente mais estáveis e mais controláveis, sendo úteis quando a especificidade e a previsibilidade da geração importam mais do que o realismo competitivo puro. A aula encerra conectando esses conceitos também a outras mídias, como som e voz, destacando que essas abordagens ajudam a tornar a geração mais realista e gerenciável.

**Pontos de atenção**  
- Em geração de imagens, não vale assumir a mesma lógica sequencial do texto: a coerência é espacial, não linear.  
- GANs dependem de uma dinâmica competitiva entre gerador e discriminador; o avanço vem do refinamento mútuo contínuo.  
- O objetivo principal dos GANs é realismo visual; eles são mais indicados quando a aparência final importa mais do que o controle fino dos atributos.  
- VAEs são mais adequados quando é necessário controlar características específicas da saída, não apenas gerar algo plausível.  
- VAEs tendem a ser mais estáveis matematicamente que GANs, mas a comparação envolve troca entre controle, estabilidade e nível de realismo.  
- O exemplo das notas de 10 reais é apenas ilustrativo: não trata de falsificação real, mas do processo de aprendizagem por contraste.  
- A escolha da arquitetura deve considerar o domínio de uso: imagem, arte, moda, jogos, som e voz podem exigir abordagens diferentes.  
- O uso de variáveis latentes é central nos VAEs para direcionar atributos da geração, evitando saídas genéricas demais.