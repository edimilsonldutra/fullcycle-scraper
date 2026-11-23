Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16392)

## Resumo da aula

LLMs não atualizam seu conhecimento automaticamente depois do pré-treinamento e dos ajustes posteriores. Quando o treinamento termina, o modelo fica congelado em relação aos fatos do mundo, mesmo que continue útil para geração, síntese e raciocínio sobre o que já aprendeu. Isso cria uma limitação direta para perguntas sobre eventos recentes, preços atuais, decisões judiciais novas ou dados operacionais que mudam com frequência. Nesses casos, a resposta pode ficar desatualizada ou até derivar para alucinação, tema já discutido anteriormente.

Conversar com um modelo não significa alterar seus pesos internos. Cada interação de usuário é processada para inferência, não para treinamento contínuo, porque atualizar pesos a cada conversa exigiria custo computacional e latência incompatíveis com uso em produção. Por isso, o fato de muitas pessoas usarem o mesmo produto não implica que o modelo esteja aprendendo em tempo real com todas elas. Mesmo que logs possam ser armazenados para uso futuro, isso só teria efeito após um novo ciclo explícito de treinamento.

Retomando a ideia de infraestrutura, o modelo acessado por um usuário não é necessariamente a mesma instância de inferência usada por outro. Em ambientes com GPUs, múltiplas instâncias podem estar distribuídas por servidores diferentes e não compartilham estado de conversa nem aprendizado online entre si. Isso desmonta o mito de uma “mente coletiva” se atualizando a cada prompt. O sistema pode parecer unificado como produto, mas a inferência ocorre de forma segmentada.

Lembra da janela de contexto já discutida? Aqui ela aparece como explicação para o comportamento de “lembrar” algo dentro de uma conversa. O modelo consegue responder como se soubesse seu nome ou preferências porque essas informações ainda estão no contexto ativo, não porque ele reescreveu seu conhecimento interno. Quando a conversa ultrapassa o limite de contexto, parte dessa continuidade se perde e uma nova janela deixa de carregar automaticamente esse histórico.

Alguns produtos adicionam uma camada de memória persistente para guardar preferências e fatos recorrentes do usuário, como nome, estilo de resposta ou temas de interesse. Essa memória acompanha a interação e melhora personalização, mas continua sendo um mecanismo externo ao modelo, semelhante a um bloco de notas consultado durante a geração. O ponto central é que pesos, vieses e representações internas do modelo não são recalculados por causa disso. Há retenção de informação útil para experiência do usuário, mas não há retreinamento.

Áreas como medicina, jurídico, catálogo de produtos e dados corporativos mudam rápido demais para depender apenas do conhecimento congelado do modelo. Uma recomendação clínica, uma decisão judicial recente, um preço atualizado ou um número financeiro do dia podem simplesmente não existir na memória do modelo base. Nesses cenários, confiar apenas no que foi aprendido no treinamento é operacionalmente arriscado. O sistema precisa receber dados externos atualizados no momento da consulta.

Se um modelo foi treinado com dados até certo período, ele continuará refletindo esse recorte temporal até passar por novo treinamento ou fine-tuning apropriado. Esse processo é caro, demorado e inadequado para acompanhar mudanças diárias ou horárias. Por isso, retreinamento não é a solução padrão para conhecimento em tempo real. A arquitetura precisa separar capacidade linguística do modelo e atualização factual dos dados consultados.

Uma forma simples de contornar a desatualização é instruir o sistema a consultar fontes específicas antes de responder. Em vez de perguntar genericamente sobre tecnologia atual, é mais eficaz restringir a busca a bases como publicações do MIT ou de Stanford e usar esse conteúdo como referência imediata. Isso reduz a dependência do conhecimento congelado e melhora a confiabilidade da resposta. A estratégia continua baseada em prompt, mas passa a operar com contexto externo recente.

RAG aplica de forma estruturada a ideia de buscar informação externa e inseri-la no contexto do modelo antes da geração. Retomando o conceito já visto, a novidade aqui é seu papel como mecanismo de atualização factual: a pergunta aciona uma busca em documentos recentes, os trechos relevantes são recuperados e incorporados ao prompt, e só então o modelo responde. O modelo não aprende o conteúdo novo; ele apenas o lê no momento da inferência. A vantagem é combinar linguagem natural fluente com evidência atual sem alterar os pesos do LLM.

O comportamento se parece mais com uma pessoa que sabe ler e consulta um livro antes de responder do que com alguém que internalizou permanentemente o conteúdo. Depois da leitura, a pessoa consegue formular a resposta, mas isso não significa que dominava o assunto antes nem que reconfigurou sua mente de forma duradoura. Com LLMs ocorre algo semelhante quando documentos externos são anexados ao prompt. A resposta melhora porque a informação certa foi fornecida no momento certo.

## Transcrição

00:00

Pessoal, vamos falar então do último ponto de atenção que a gente precisa ter nessa relação da LLM e suas dificuldades, que eu deixei por último e tem muita gente que deve estar me xingando já. Quem conhece de um pouco mais já deve estar falando, poxa, falou esse monte de coisa e não falou o mais importante, pois chegou a hora de falar.

00:20

mais difícil, mais importante, mais relevante para a LLM é sobre conhecimento. Então, no final das contas, a gente usa uma generativa como uma base de conhecimento, troca de informação, resolução de problemas, assim por diante, certo? Então, a gente usa pra ajudar a gente no dia a dia, principalmente pra buscar informação e responder coisas. Então, essa é talvez a maior função utilizada, né? Fora gerar meme pra internet, brincadeiras.

00:47

mas tem bastante essa utilização. E qual que é o problema que a gente tem? Como eu falei pra vocês, a gente tem lá toda a base de treinamento, beleza? Então eu fui lá, montei toda a estratégia, organizei a LLM, consegui criar a estrutura de Transformers, treinei ela, fiz o pré-treinamento, fine-tuning, etc. Pá, acabei!

01:06

A partir dali ela tá congelada. Você não tem uma evolução pós treinamento desse conhecimento. E isso é um problema. Então, por exemplo, se você perguntar pra ela se o Palmeiras ganhou ontem, ela não vai saber te responder. Eu também não, porque eu não manjo muito de futebol. Mas ela não vai saber te responder. Eu não sei nem se ele jogou ontem. Agora, pensa no seguinte.

01:26

Nesse sentido, a informação que você tem mais nova, dificilmente ela vai conseguir buscar, a não ser que ela faça algumas coisas que a gente vai falar aqui na sequência. Então, ela não tem essa memória ativa e ela nem atualiza sua base de treinamento automaticamente, ela não tem essa estratégia, tá bom?

01:42

Então, a notícia que está rolando agora, se você for buscar, não é o melhor lugar pra você buscar. Se você consegue fazer algumas coisas pra fazer isso, a gente já vai falar, mas ela não foi treinada e criada, talvez, pra isso por enquanto, e essa é uma limitação dela de saber as coisas mais novas. Então, basicamente, esse é um ponto de atenção bastante importante pra gente, tá bom? Então, se eu perguntar, é capaz dela inventar ou alucinar ou criar alguma coisa só pra responder pra mim, tá?

02:08

Então, quando a gente olha, por exemplo, o GPT-4, ele não vai aprender ali com as interações que a gente tem individuais. É outra coisa que é mito, tá? As pessoas falam assim, ah, então quer dizer que o Natan tá aqui usando o GPT, o Manezinho tá usando o GPT, você aí tá usando o GPT, ele tá aprendendo com todo mundo e criando uma rede de estrutura, de comunicação e de conhecimento. Não. Já começa que tem um outro problema que acontece que

02:36

O GPT que você usa possivelmente não é o GPT que eu uso. Então, o processamento desses GPTs vai ser feito em algumas GPUs. Então, no servidor lá na ponta onde ele está sendo processado, dificilmente eu vou estar usando o mesmo servidor do que você. Porque os servidores de GPU não tem a mesma capacidade que a gente tem, por exemplo, na cloud.

02:57

de processar multithread, de pegar e processar várias coisas ali dentro do mesmo processador. Então, possivelmente você vai ter menos versões do GPT ou instâncias, se a gente puder chamar assim, do GPT rolando na mesma máquina e elas não vão se comunicar, ou seja, o que está rolando para mim possivelmente não está rolando para você, você não vai saber, você não vai ter como ter essa informação. Ah, mas os caras podem guardar? Pode,

03:23

Tá bom, pode ter alguma coisa aí em teoria da conspiração, os caras tão guardando no banco de dados pra usar depois. Pode. Mas eles vão ter que treinar depois. Porque agora mesmo o GPT não está aprendendo com isso, tá bom? Então essas interações individuais ele não aprende. Ele não atualiza o modelo interno quando a gente tá trocando com ele, por exemplo. Também não ajusta peso, porque pensa, atualizar o modelo é fazer toda aquela visão de cálculo e de estatística, querendo ou não.

03:52

para você chegar numa resolução de vetores ali. Então ele não vai fazer isso com base nas conversas toda hora porque vai ficar extremamente caro, não vai dar tempo, eu ia travar essa bagaça, acho que nem funcionaria. Então eu não ensino esse modelo, ele não continua aprendendo, tá bom? Então uma coisa que eu te falei aqui, poxa

04:12

Ao contrário do ser humano, esse cara não aprende com a gente. Você deve estar pensando, pô, aprende. Aprende porque quando a gente conversa, o meu GPT, por exemplo, você pode até estar falando assim, o que você fala com o seu, o meu não pega. Mas o que eu falo com o meu aqui, ele pega. O meu Gemini, a hora que eu troco ideia com ele aqui, ele sabe que meu nome é Natan. O meu de Perplexity, quando eu vou lá conversar com ele, ele sabe que eu gosto mais de verde do que de azul.

04:36

Uma coisa nesse sentido. Sim, isso pode acontecer. Por quê? Porque ele tem contexto de conversa. Então pensa o seguinte, a partir do momento que você abre uma janela, ele guarda o contexto daquela conversa. Então ele busca ali, porque... Pensa o seguinte, se você tá vendo tudo aquilo ali, ele também tá vendo, ele tá guardando aquilo, aquilo ele tá guardando porque ele tem que retroalimentar pra você. Então ele tem um pedaço, não sei se vocês já chegaram a estourar limitações de conversa, mas quando você vai perguntando muito dentro de uma mesma janela, chega uma hora que estoura e ele pede pra você abrir outra.

05:06

Mas o que ele tem ali dentro, ele vai conseguindo guardar. Quando chega um determinado tamanho, você tem que mudar de conversa. Quando você muda de conversa, ele perdeu o contexto. Ah, perdeu o contexto, Nathan? Será que perde mesmo? Porque quando eu mudo de conversa, tem vezes que eu entro numa outra conversa e ele ainda sabe meu nome.

05:27

Sim! GPT-4, por exemplo, na conta paga, ele tem um carinha que chama memória ativada. Essa memória ativada, o que ela vai fazer? Ela guarda algumas informações que são super importantes, por exemplo, nome, ou ele vai perguntar, por exemplo, as coisas que você mais trocou com ele. Ele tenta guardar ali pra facilitar e ser mais... ser melhorado, né? Na experiência com o usuário.

05:50

Então, por exemplo, ele vai conseguir guardar se você gosta de conteúdo mais profundo, ou de exemplo mais prático, ou de coisas mais aleatórias, ou você gosta mais de futebol, e assim por diante. Ele consegue guardar a principal montante de conversas que vocês vão tendo, ele entende o que é a sua atenção ali, o que faz sentido ele guardar, e guarda algumas coisas. Mas ele não consegue voltar de novo, ele não vai pegar essa informação,

06:14

e reprogramar toda a visão dele de pesos e vieses pra saber aquele monte de coisa que a gente falou de vetor e blá blá blá. Não, não vai fazer isso. Ele vai guardar numa memória pra saber mais ou menos quem é você, o que você tá fazendo e etc. Aí com base nisso ele usa pra dar a melhor mensagem pra ele. É mais ou menos uma coisa que acompanha a LLM e não um retreinamento de LLM, entendeu?

06:38

Então ele não aprendeu, ele guardou aquilo ali como se tivesse guardado num caderninho pra voltar e buscar quando precisar. Então tem isso sim, quando eu falo pra vocês não tô mentindo que ele não aprende, ele não aprende infelizmente, mas ele consegue guardar certa informação pra ter essa troca, tá bom? E o que isso gera aqui de problema?

06:59

Quando você precisa, por exemplo, de um atendimento médico que toda hora tá mudando, tem coisas novas chegando, jurídico, que cada hora tem um julgamento novo que traz informação nova, busca de produto, preço e etc. Fica mais difícil pra ele fazer ou coisas nesse sentido. Ou o dado de uma empresa que fica mudando toda hora. Você tá lá mexendo nas coisas, tá mudando toda hora o seu financeiro. Ele não vai saber. A não ser que você crie um KB e atualize ele, que é caro, aquilo que a gente falou já na hora que a gente tava falando de treinamento.

07:26

Então, o ponto que você tem que ter na cabeça é, se um modelo foi treinado em 2026, ele tá com a memória de 2025. Em 2027, ele tá com a memória de 2025. A não ser que você vá lá e retreine este cara, que é caro e demorado. A gente já falou sobre isso.

07:42

O que a gente tem aqui que a gente já falou inclusive, que pode ajudar a gente é o RAG, vamos retomar ele. Então você tem uma arquitetura aqui que você faz um complemento, tá? Então você faz por exemplo, eu costumo fazer isso quando eu preciso dele atualizado, eu faço por Prompt, não por RAG.

08:00

Eu faço o seguinte, imagina que eu quero informação do que tá rolando de tecnologia neste momento. Ele não vai saber, então eu falo pra ele buscar, por exemplo, nas revistas digitais do MIT, Stanford, blá blá blá, e jogo pra ele toda a base onde eu quero que ele busque. E daí ele vai buscar na internet, porque a internet é uma base de dados importante, e daí com base nisso,

08:22

ele traz pra gente essa resposta, tá bom? E como é que funciona o HAG? Isso é o jeito que eu faço, tá? Mas o RAG, no final das contas, ele faz isso de uma certa forma, mas numa arquitetura já organizada. Então, quando você faz uma pergunta, ele vai buscar documento e coisas atualizadas já, volta pra você com esses documentos que ele buscou e enfia no meio do seu prompt. Então, é basicamente aquilo que eu falei que eu fiz,

08:48

certo que eu escrevo a busca lá ele vai fazer isso bom jogar no seu prompt pegar essa memória atualizada e com base nisso ele vai fazer o que já está acostumado de treinamento aí como pronto está ali para guiá-lo ele vai conseguir chegar na resolução de aonde você vai chegar com aquele texto hoje o generativo dele não vai mudar peso e viés nem vetores mas ele tem informação direcionando para onde você quer e vai ser mais fácil dele conseguir é chegar a um resultado entendeu então com isso ele consegue melhorar como se fosse basicamente

09:18

a gente, que é ótimo de ler, a gente sabe ler, sabe português, etc. Aí você me pergunta alguma coisa que eu não sei. Eu vou lá, pego um livro, peguei um livro, ó que véio, né? Pego um livro e falo, ah, tá aqui a resposta. Aí eu falo pro senhor, ó, tá aqui a resposta. E te passo a resposta do que eu acabei de ler. Eu não sabia. Se bobei ainda, eu não sei. Eu só li.

09:37

falei do livro para não ficar confuso de eu buscar no Google por exemplo, mas para facilitar a vida seria mais ou menos essa analogia que eu tenho para trazer para vocês, beleza? Esse é um problema muito conhecido e quem sabe um dia a gente resolve, mas por enquanto a gente ainda não conseguiu resolver, então pense nisso também quando você estiver usando a sua IA. Você precisa pensar em como você trabalha com dados mais atualizados normalmente com o Prompt ou com estratégias como o Hack, beleza?

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem Grande)  
- **GPT** — *Generative Pre-trained Transformer* (Transformador Generativo Pré-treinado)  
- **GPU** — *Graphics Processing Unit* (Unidade de Processamento Gráfico)  
- **KB** — *Knowledge Base* (Base de Conhecimento)  
- **RAG** — *Retrieval-Augmented Generation* (Geração Aumentada por Recuperação)  

**Resumo**  
A aula abordou a principal limitação das LLMs relacionada ao conhecimento: após o pré-treinamento e eventuais ajustes como fine-tuning, o modelo fica “congelado” em relação aos fatos do mundo e não atualiza automaticamente sua base de conhecimento. Isso significa que perguntas sobre eventos recentes, preços atuais, decisões judiciais novas, dados médicos ou informações corporativas em constante mudança podem gerar respostas desatualizadas, incompletas ou até alucinações. O instrutor reforçou que conversar com um modelo não equivale a treiná-lo: cada interação é usada para inferência, não para atualização dos pesos internos, porque isso seria caro e inviável em produção.  

Também foi explicado que o sistema que cada usuário acessa pode estar rodando em instâncias diferentes, distribuídas em GPUs distintas, sem compartilhamento de estado entre elas, o que desfaz a ideia de uma “mente coletiva” aprendendo em tempo real com todos os prompts. O que pode existir é o armazenamento de logs para uso posterior em um novo ciclo explícito de treinamento, mas isso não representa aprendizado instantâneo. A aula retomou a janela de contexto para explicar por que o modelo parece “lembrar” informações dentro de uma mesma conversa: ele apenas mantém o histórico ativo enquanto a janela não estoura. Em alguns produtos, há ainda memória persistente externa para guardar preferências do usuário, como nome ou estilo de resposta, melhorando a personalização sem alterar os pesos do modelo.  

Por fim, a aula apresentou formas de contornar a desatualização factual. Uma abordagem é orientar o modelo a consultar fontes específicas antes de responder, restrigindo a busca a bases confiáveis e recentes. Outra, mais estruturada, é o RAG, que recupera documentos atualizados, insere esse conteúdo no prompt e só então gera a resposta. O ponto central é separar a capacidade linguística do modelo da atualização factual, usando dados externos no momento da inferência para melhorar a confiabilidade e manter a fluidez da geração sem retreinamento do LLM.  

**Pontos de atenção**  
- LLMs não atualizam conhecimento sozinhas após o treinamento; o recorte temporal do treino continua valendo até novo treinamento ou fine-tuning.  
- Não confiar em respostas do modelo para informações muito recentes sem validação externa.  
- Há risco de alucinação quando o modelo tenta responder sem ter base factual suficiente.  
- Conversas com o modelo não treinam os pesos em tempo real; inferência não é treinamento contínuo.  
- Instâncias diferentes do mesmo produto podem não compartilhar contexto nem aprendizado entre usuários.  
- A janela de contexto tem limite; ao ultrapassá-lo, parte do histórico se perde.  
- Memória persistente de alguns produtos é externa ao modelo e não significa retreinamento.  
- Áreas dinâmicas como medicina, jurídico, preços e dados corporativos exigem fontes atualizadas.  
- Retreinar frequentemente é caro e lento; não é a solução padrão para atualização diária ou horária.  
- Para informações atuais, usar prompts com fontes específicas ou estratégias como RAG.  
- RAG melhora a resposta ao inserir documentos recentes no contexto, mas não altera pesos, vieses ou vetores internos do modelo.  
- Sempre diferenciar “o modelo sabe” de “o sistema forneceu o contexto certo na hora certa”.