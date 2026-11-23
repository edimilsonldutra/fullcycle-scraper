Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16603)

## Resumo da aula

Prompt caching é o reaproveitamento de partes repetidas do prompt para evitar que o provider reprocese os mesmos tokens em toda chamada. Isso importa porque custo e latência já crescem com o contexto, então repetir blocos fixos sem reaproveitamento desperdiça processamento. A consequência prática é direta: quando um prefixo, instrução fixa ou documento recorrente aparece muitas vezes, vale desenhar o prompt para maximizar repetição útil.

O cache discutido aqui não é o cache da aplicação, como Redis, usado para guardar respostas, objetos ou estados do sistema. No prompt caching, quem reaproveita o conteúdo é o provider ou o mecanismo associado ao modelo, reduzindo o trabalho de inferência sobre tokens repetidos. Essa distinção muda a arquitetura da solução: um cache de aplicação evita recomputar no seu backend; o cache do provider evita reprocessar contexto no lado do modelo.

Na OpenAI, o caching ocorre de forma automática e transparente: o provider decide o que entra em cache e por quanto tempo permanece disponível. Isso não elimina a necessidade de engenharia; apenas desloca o esforço para o desenho do prompt, que deve manter o máximo possível de texto fixo no início das interações. Se cada chamada muda demais, o reaproveitamento cai e o desconto desaparece, mesmo sem nenhuma mudança na lógica da aplicação.

Retomando o cenário da aplicação, a camada nova agora é a reutilização: partes fixas do prompt deixam de ser apenas contexto e passam a ser candidatas a reaproveitamento. Em um provider com cache automático, a estratégia é estabilizar instruções, estrutura e prefixos para que os mesmos tokens reapareçam entre chamadas. Prompt Engineering, nesse caso, não busca só qualidade de resposta; busca também previsibilidade de repetição para capturar economia operacional.

No Gemini, o cache pode ser criado explicitamente por API, o que dá mais controle sobre o que será reaproveitado. Em vez de depender apenas da detecção automática de repetição, a aplicação informa que determinado conteúdo deve ser cacheado e depois o referencia em chamadas futuras. Esse modelo muda o desenho do prompt porque parte do contexto deixa de ser reenviada como texto bruto e passa a ser reutilizada por referência.

Quando um conteúdo é cacheado explicitamente, ele recebe um identificador que funciona como referência reutilizável. A chamada futura não precisa reenviar o documento inteiro; basta enviar a nova pergunta junto com o ID do conteúdo já armazenado. Isso é especialmente útil quando o mesmo artefato, como um PDF, será consultado repetidamente em várias perguntas independentes.

Se um PDF será consultado muitas vezes, reenviá-lo inteiro em cada pergunta faz o provider reprocessar o mesmo conteúdo repetidamente. A alternativa é fazer o upload uma vez, criar o cache desse documento e guardar o ID retornado. Depois, perguntas como “qual é o assunto principal deste PDF?” passam a usar o ID do cache, reduzindo custo e evitando reprocessamento desnecessário do arquivo completo.

TTL, ou Time To Live, define por quanto tempo o conteúdo cacheado permanece disponível para reutilização. Esse parâmetro importa porque cache não é gratuito: além do eventual custo de criação, o provider pode cobrar pelo armazenamento e pelo tempo de retenção. O valor do cache aparece quando o conteúdo será reutilizado o suficiente para compensar esse custo inicial e o período configurado.

Cache explícito não deve ser criado para conteúdo descartável ou de uso único, porque há um custo para materializar e manter esse estado. Ele faz sentido quando o mesmo documento, bloco fixo ou contexto recorrente será consultado várias vezes ao longo do fluxo da aplicação. A decisão correta depende da frequência de reutilização, do tamanho do conteúdo e do mecanismo oferecido pelo provider.

Prompt Engineering também é escrever de forma intencional para reaproveitamento, não apenas escolher técnicas como one-shot, few-shot ou chain of thought. O desenho do prompt muda conforme o provider: na OpenAI, a meta é maximizar repetição útil; no Gemini, além disso, é possível separar conteúdos recorrentes e referenciá-los por ID. Essa visão conecta prompt, custo, latência e escolha de provider como decisões de engenharia, não apenas de redação.

## Transcrição

00:01

Bom, pessoal, e agora, novamente, é um assunto extremamente complexo, é um assunto que tem uma intersecção com a parte de Prompt Engineer, mas, ao mesmo tempo, ele tem uma intersecção muito forte com a área de arquitetura. Eu não vou aprofundar, obviamente, nesse assunto, porque eu vou falar o suficiente para a gente pensar na parte de Prompt Engineer.

00:28

Beleza? Então o negócio é o seguinte, prompt caching. Para que serve isso? O que é um cache de prompt? Basicamente, quando você trabalha com cache de prompt, você está evitando o retrabalho do modelo, tá?

00:44

para processar partes do prompt que vão se repetir. Então, basicamente, cada provider pode trabalhar com o caching de forma diferente. O que eu estou querendo dizer com isso? Vamos imaginar que toda hora, na hora que eu vou fazer um prompt, eu estou mandando a mesma mensagem.

01:02

O que isso pode fazer? Se eu não cacheio nada, o que isso vai acontecer? Vai fazer que cada vez o modelo vai ficar reprocessando token a token, O de N². Agora, se eu consigo fazer o caching disso,

01:20

significa que eu vou evitar pra caramba fazer com que o modelo fique reprocessando mensagens antigas. O grande ponto é que esse tipo de cache que eu estou falando aqui não é o cache, nesse caso, que eu crio na minha aplicação onde eu vou salvar o dado no Redis. A gente tem esse tipo de cache também.

01:41

Mas o Prompt Caching que eu estou falando aqui é diretamente com o modelo. Então, eu vou dar um exemplo aqui para vocês de dois providers diferentes. OpenAI. Como é que eles trabalham com cache? Ele trabalha de quê? Com cache de forma automática e transparente. Pelo menos até o momento dessa gravação desse vídeo. O que isso significa?

02:03

Se eu enviar vários prompts começando com o mesmo texto fixo, você vai pagar o valor cheio apenas na primeira vez. Nas próximas vezes, você vai poder ter um desconto de em torno de 50%.

02:21

A OpenAI é quem decide o que entra em cache e por quanto tempo ele fica disponível. Então, por exemplo, se você está usando a OpenAI de forma geral, você não vai se preocupar tecnicamente com como você vai pedir para ela fazer o cache, mas

02:42

Pensando em Prompt Engineering, você vai criar estratégias para que, na hora que você cria um determinado prompt, esse prompt se repita ao máximo na hora de fazer as interações, para que a gente faça com que a OpenAI cacheie aquele seu prompt para evitar o reprocessamento e eu ter desconto. Então, não é porque ela faz isso automaticamente,

03:10

que eu não vou criar estratégias na hora de eu criar o meu prompt para que ela, de forma geral, faça o trabalho dela de cachear. Porque se cada vez eu faço um prompt completamente diferente, ou trabalho de forma completamente diferente,

03:26

Esse cash não vai acontecer e eu vou pagar 100%. E isso que uma pessoa de Prompt Engineering, ela brilha, porque ela consegue fazer com que a empresa economize muito dinheiro somente com algumas técnicas de prompt e que, às vezes, não são técnicas complexas, mas geram uma economia danada. A gente tem outros casos aqui, por exemplo, como o Gemini, o Google Gemini. O Google Gemini, por exemplo, trabalha de uma forma diferente.

03:57

Olha que interessante. Na OpenAI, ela faz isso de uma forma automática. Agora, com Gemini, olha só que interessante. Eu tenho uma API, eu posso fazer uma chamada de API, onde eu quero falar que aquele conteúdo deve ser cacheado, tá?

04:17

e eu posso depois, então, fazer referência a esse conteúdo no futuro. Por exemplo, vamos imaginar que eu vou fazer o upload de um PDF, e eu sei que esse PDF eu vou ficar extraindo informação dele o tempo todo. Então, se toda vez que eu for fazer uma pergunta baseada num PDF que eu anexei, que eu subi,

04:38

ele tiver que processar novamente todo aquele PDF, eu vou pagar uma fortuna. Então, o que eu posso fazer? Eu faço o upload de um PDF e eu falo para o Google, para o Gemini, fazer o cache daquele PDF.

04:53

E daí eu vou ter um ID falando, olha, o PDF1, por exemplo, é meu ID ali no cache. Aí o que acontece? Quando eu for fazer uma pergunta baseada, olha, qual é o assunto principal desse PDF?

05:10

E, na hora que eu vou fazer essa pergunta, o que eu faço? Eu faço o seguinte, olha só, qual é o assunto principal desse PDF, e daí eu passo qual é o ID do cache daquele PDF. Então, o que vai acontecer? Ele vai usar aquele cache

05:30

para fazer o processamento da minha pergunta. E aí, nesse caso, eu acabo tendo um super desconto. Agora, uma coisa que é interessante, somente por curiosidade, eu não quero ir a fundo nisso, novamente, porque isso acaba entrando muito em arquitetura e não em Prompt Engineer, eu posso definir um TTL, um Time To Live, ou seja, por quanto tempo esse cache fica ativo,

05:54

O Google normalmente vai te cobrar pelo tamanho do armazenamento e pelo tempo também que você quer deixar aquilo disponível. E você tem muito mais controle do que você quer cachear ou não. Os descontos aí chegam em torno de 75% de desconto para conteúdos que você cacheou. Obviamente que você vai pagar também para criar um novo cache. Então, você não vai criar cache à toa. Você só vai criar caches que você for utilizar ali de forma

06:23

Mas é importante que você saiba todas essas técnicas de caching. E o porquê que eu estou dizendo isso? Se você vai utilizar OpenAI, o seu modelo, na hora de você criar seu prompt, você pode criar de uma forma. Na hora que você vai trabalhar com Gemini, por exemplo,

06:41

Já que eu sei que posso cachear explicitamente um conteúdo, eu posso criar o prompt de uma forma diferente para que eu consiga fazer uma referência dele, algo que eu não consigo fazer diretamente na OpenAI. A Anthropic tem um outro esquema de cache também dela, de como ela trabalha. Então, lembre-se, pessoal, quando a gente está falando de prompt engineering, não está apenas em saber escrever e pedir para IA.

07:08

e tendo todas aquelas técnicas de one shot, few shot, chain of thoughts, tree of thoughts, etc. Isso tem muito a ver também de como que você escreve de uma forma estratégica para que você consiga economizar, ter mais resultado, menos latência, usando modelos menores para aquilo que você precisa...

07:33

para evitar matar uma formiga com a bazuca. Beleza? Então, somente para lembrar, Prompt Engineering tem tudo a ver também com Caching, porque se você for trabalhar com Cache, o seu Prompt tem que ser feito de forma... Como que eu posso dizer? De uma forma intencional. Você não pode simplesmente escrever o Prompt de qualquer forma. Você tem que saber extrair resultados a partir de Cache também.

## Resumo IA

**Abreviações**
- **API** — *Application Programming Interface*.
- **PDF** — *Portable Document Format*.
- **TTL** — *Time To Live*.

**Resumo**
A aula apresentou o conceito de prompt caching como uma forma de reaproveitar partes repetidas do prompt para evitar que o modelo reprocese os mesmos tokens em todas as chamadas, reduzindo custo e latência. O instrutor destacou que isso não é o mesmo que cache de aplicação, como Redis, pois no prompt caching o reaproveitamento acontece no lado do provider/modelo, e não no backend da aplicação. Foi explicado que, quando há um prefixo, instrução fixa ou documento recorrente, vale estruturar o prompt para maximizar a repetição útil e, assim, aproveitar o cache.

Em seguida, foram comparados diferentes providers. Na OpenAI, o caching é automático e transparente: o provider decide o que entra em cache e por quanto tempo, e o desenvolvedor não configura explicitamente esse mecanismo. Mesmo assim, a engenharia do prompt continua importante, porque é preciso estabilizar partes fixas do texto para aumentar a chance de reaproveitamento e obter desconto nas chamadas repetidas. Já no Gemini, o cache pode ser criado explicitamente por API, permitindo que a aplicação marque um conteúdo para ser armazenado e depois o referencie por ID em chamadas futuras, em vez de reenviar o texto bruto.

O exemplo prático dado foi o de um PDF consultado repetidamente. Em vez de reenviar o arquivo inteiro a cada pergunta, o fluxo ideal é fazer o upload uma vez, criar o cache do documento, guardar o ID retornado e usar esse ID nas consultas seguintes. Também foi comentado o uso de TTL para controlar por quanto tempo o conteúdo fica disponível no cache, além de observações sobre custo de criação e armazenamento. Por fim, a aula reforçou que prompt engineering não trata apenas de qualidade de resposta, mas também de estratégia para reaproveitamento, economia e latência, com desenho de prompt variando conforme o provider e seu modelo de caching.

**Pontos de atenção**
- Prompt caching **não é** o mesmo que cache de aplicação; não confundir com Redis ou cache de objetos/respostas no backend.
- Em providers com cache automático, como a OpenAI, é importante **manter partes fixas do prompt estáveis** para aumentar o reaproveitamento.
- Se o prompt muda demais a cada chamada, o cache **deixa de ser aproveitado** e o custo volta ao valor cheio.
- No Gemini, o cache é **explícito por API**; é preciso planejar o fluxo para criar o cache e referenciá-lo depois por ID.
- Faz mais sentido cachear conteúdos grandes e recorrentes, como PDFs ou blocos fixos, do que conteúdo descartável ou de uso único.
- Há **custo para criar e manter** cache; não vale cachear “à toa”.
- O **TTL** deve ser definido com cuidado, considerando o tempo real de reutilização do conteúdo.
- O ganho do cache depende da **frequência de reutilização** e do tamanho do conteúdo cacheado.
- Prompt engineering deve considerar **custo, latência e mecanismo do provider**, não apenas técnicas de formulação como one-shot, few-shot ou chain of thought.
- O desenho do prompt deve ser intencional para **explorar repetição útil** e evitar reprocessamento desnecessário.