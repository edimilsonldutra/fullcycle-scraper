Módulo: Fundamentos de IA Generativa\
Aula: [N/A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/263/conteudos?capitulo=263&conteudo=16389)

## Resumo da aula

Reduzir alucinação começa por restringir o espaço de resposta do modelo. Em vez de pedir apenas uma resposta final, peça fontes confiáveis, autores, estudos e delimite onde a busca deve ocorrer, como jornais específicos ou publicações acadêmicas. Isso força o modelo a ancorar a resposta em referências verificáveis e facilita a auditoria humana. Quando há enriquecimento com dados externos e o domínio de busca é bem nichado, a chance de invenção tende a cair.

LLMs tendem a completar lacunas de forma plausível, especialmente quando o prompt induz uma postura excessivamente prestativa. Por isso, instruções como “se não tiver certeza, diga que não sabe” e “não invente informações ausentes” funcionam como restrições comportamentais objetivas. Esse tipo de comando reduz a pressão implícita por sempre responder e diminui inferências criativas indevidas. O efeito prático é trocar respostas confiantes e erradas por respostas mais conservadoras.

Uma forma de detectar saltos indevidos é pedir que o modelo apresente o passo a passo antes da conclusão, aqui referido como Chain of Truth Proofing. O valor dessa técnica não está em assumir que toda cadeia intermediária é verdadeira, mas em expor a estrutura lógica usada para chegar ao resultado. Se a conclusão aparece sem apoio em fontes ou sem transições justificadas, fica mais fácil identificar onde houve extrapolação. No exemplo da Amazônia, uma afirmação extrema sem base explícita já sinaliza alucinação.

Outra estratégia útil é declarar previamente o papel e os limites operacionais do modelo. Em ferramentas como ChatGPT, Copilot, Gemini, Llama ou Manus, isso pode aparecer como contexto de conversa, pasta, instruções persistentes ou configuração semelhante a um agente. Definir que o assistente só usa dados até certo ano, não prevê o futuro e deve agir dentro de um escopo específico reduz respostas fora de domínio. A vantagem adicional é não precisar repetir as mesmas restrições em toda interação.

Few-shot Prompting reduz ambiguidade ao mostrar exemplos do que deve ser considerado correto e incorreto. Em vez de depender apenas de instruções abstratas, o modelo passa a inferir padrões de aceitação a partir de casos concretos fornecidos pelo usuário. Isso ajuda a calibrar o nível de inferência tolerado e os limites esperados da resposta. O custo é operacional: preparar bons exemplos dá trabalho, por isso a técnica nem sempre é a mais conveniente no uso cotidiano.

O uso contínuo da mesma ferramenta pode produzir uma sensação de maior alinhamento ao estilo e às expectativas do usuário. Na prática, isso significa que um assistente usado por mais tempo tende a parecer mais “afinado” do que outro recém-adotado, especialmente quando há histórico, contexto persistente ou personalizações acumuladas. Essa observação não substitui validação factual, mas sugere que alternar constantemente entre plataformas pode reduzir consistência operacional. Para tarefas recorrentes, estabilidade de ambiente pode ser mais útil do que testar tudo o tempo todo.

Em contexto jurídico, uma alucinação não é apenas um erro de redação: ela pode introduzir fatos, precedentes ou citações inexistentes em documentos formais. Os casos citados mostram consequências concretas como retratação formal, multas, dano reputacional e até impacto financeiro milionário quando o erro afeta processos sensíveis. O problema central não é só incoerência argumentativa, mas a fabricação de referências que parecem legítimas. Em domínios regulados, plausibilidade textual não tem valor sem verificabilidade documental.

A postura correta diante de uma LLM é tratá-la como apoio produtivo, não como autoridade final. A analogia com um estagiário é útil: ela acelera trabalho, sugere caminhos e produz rascunhos, mas exige revisão antes de qualquer uso crítico. Isso vale ainda mais em áreas como direito e medicina, nas quais uma resposta errada pode gerar dano material, institucional ou humano. Ganho de produtividade sem verificação vira risco operacional.

## Transcrição

00:02

Bom galera, então sabendo que as LLMs tem esse problema de alucinação, o que a gente pode fazer para diminuir isso? Eu vou contar aqui algumas técnicas que podem te ajudar para diminuir esse tipo de alucinação quando você estiver promptando, beleza? Então agora eu já estou falando sobre o uso das LLMs, só pra gente já deixar isso um pouco mais organizado para quando vocês forem usar no dia a dia, tá bom?

00:24

Então, vamos lá. Se tem uma LLM que está alucinando que ela pode trazer, por exemplo, alguns fatos que não são realidade. O que a gente pode fazer? Na hora de fazer o prompt, por exemplo, é importante você pedir evidência. Então, por exemplo, imagina que você vai fazer um prompt

00:41

E dentro desse prompt, você pode colocar coisas do tipo assim... Liste as fontes confiáveis que sustentam a sua resposta. Ou busque apenas nas fontes blá, blá, blá... E daí você vai falar... Olha, eu só quero saber de artigos de jornal, eu só quero saber de revistas acadêmicas e blá, blá... E depois você coloca... Liste suas fontes confiáveis que sustentam a sua resposta. Cite os autores e os estudos que foram usados nesta fonte. E depois você vai lá e busca esses autores para ver se eles

01:11

se eles fazem sentido mesmo, e assim por diante. Isso vai forçar o modelo a buscar consistência no conhecimento que ele tem. Então, pra fazer, olha só que interessante, pra conseguir fazer a geração quando ele estiver buscando em dados externos, ele possivelmente vai precisar

01:29

é passar pelo modelo de enriquecimento onde ele vai buscar informação em um dado lugar e daí com isso é menos chance dele alucinar, entendeu? Então, quando você nicha o local onde ele vai buscar informação, quando a informação é mais nova, normalmente ele vai melhor. E quando você coloca quais são as fontes,

01:48

normalmente ele vai ter que listar essas fontes e nessa listagem de fontes ele vai trazer pra você a organização se aquilo tá certo ou não e você consegue fazer a verificação beleza outra coisa que você pode fazer também você pode incluir instrução de cautela

02:03

Então, por exemplo, você pode colocar coisas do tipo, se você não tiver certeza, diga que não sabe. Isso é importante de fazer, porque lembra aquele negócio que eu falei para você? Se você trata muito como uma pessoa, o chatGPT, ele acaba dando uma alucinada, porque na visão dele, na visão das LLMs, no final das contas, ela precisa te agradar.

02:25

de certa forma. Então, quando você coloca instruções diretas do tipo, se você não tiver certeza, diga que não sabe. Evite inventar informações se os dados não forem conhecidos. Quando você coloca alguma coisa nesse sentido, dificilmente ela vai alucinar, porque daí ela vai entender que ela não precisa te agradar também. Você vai reduzir a tendência então, dele tentar completar qualquer coisa com a criatividade dele, tá bom? Então, é um outro jeito que eu descobri de você diminuir esse tipo de problema, tá bom?

02:55

Outro jeito, tem mais um jeito aqui. Dá para você fazer sabe o que? Você pode pedir para o modelo usar um Chain of Truth Proofing, por exemplo, que chama. O que isso faz? Você vai pedir para o modelo explicar um passo a passo

03:12

antes de responder. Então, por exemplo, você vai falar exemplifique seu raciocínio antes de chegar à conclusão. Ou, por exemplo, no Manus, você consegue ver o que ele está processando. Se você tiver paciência de ficar olhando o processamento, você vai saber mais ou menos por onde ele passou e o que ele pensou. Mas você tem um outro jeito melhorado, é que você explique o seu raciocínio antes de chegar à conclusão que você está me dando. Ele vai te dar uma

03:37

no passo a passo do que ele fez, e dentro desse passo a passo você vê se ele não deu nenhuma viajada. Então, com isso, você vai conseguir fazer primeiro. Ele vai ter mais consistência lógica, porque ele vai ter que te explicar, e depois você consegue ver se ele não deu nenhum salto maluco, que é coisa de inferência, tá bom? Então, se ele fizer, por exemplo... Ah, eu tô escrevendo um artigo sobre... Sei lá...

04:01

sobre a Amazônia. Ele começa falando sobre a Amazônia com base em livros, depois ele fala que a Amazônia vai acabar ano que vem. E ele não mostra que ele buscou isso em nenhuma fonte, por exemplo. Eu já sei que ele viajou. Então, esse tipo de situação você consegue pegar. Lógico que eu inventei agora essa ideia da Amazônia, mas é um caso que você poderia pegar e você ia ver que na linha de raciocínio ele não foi em lugar nenhum para buscar essa informação, ou seja, ele inventou.

04:28

é outra coisa também que você pode fazer esse eu uso muito muito muito você cria uma persona ou um escopo pra ele então você já deixa declarado isso é legal de você fazer todo acho que hoje em dia todas as LLMs permitem isso tá então quando você pega a chatGPT quando você pega o Llama ou Manos qual mais que dá pra fazer no Gemini dá também você consegue colocar criar uma pastinha

04:58

E daí lá em cima, cada um é de um jeito, mas quando você está criando um contexto, você pode criar uma pastinha de conversa e daí você escreve qual é o tipo de ação que você espera dele. No Copilot, por exemplo, você cria isso como se fosse um agente, apesar de nem sempre ser um agente, mas você cria como se fosse um. E daí, por exemplo, no Copilot você abre uma janelinha lá e ele vai te falar

05:22

O que você quer declarar desse agente? Você fala que esse agente vai ser um assistente treinado apenas com dados até 2023, que não tenta prever o futuro. Por exemplo. Aí você já vai mostrar para ele o que ele é. Você vai falar que ele é LLM. É isso que você tem de informação até 2023. Daqui para frente, você não vai inventar mais.

05:41

É, não é pra você tentar prever. É... Dá pra fazer a mesma coisa nos demais. Só que, por exemplo, no Copilot tinha uma janelinha. No ChatGPT você abre uma pasta e lá você coloca em cima. No Manus, se eu não me engano, também é igual ao do ChatGPT. É isso.

05:57

Então cada um vai ter um jeito de você fazer isso. Só que no final das contas você consegue nichar. Você consegue fazer isso e você consegue também fazer alguma coisa sem falar que é até 2023. Você pode falar qual é o jeito que você quer que ele atue. E daí você já pode colocar inclusive todas aquelas coisas que eu falei anteriormente pra você não ter que ficar colocando isso todas as vezes que você for usar. Já deixa ele organizado pra isso. Então tem esses quatro jeitos que eu costumo usar pra diminuir qualquer tipo de coisa.

06:23

Tem mais uma também, que é o Few-shot Prompting, que ele diminui também, mas eu não gosto muito porque dá muito trabalho, sendo bem honesto. Você dá alguns exemplos de o que você entende como correto e o que você entende como incorreto.

06:39

já para o seu modelo. Então quando você tiver lá, eu criei minha conta no Gemini, eu pego e começo a jogar para ele, isso aqui eu entendo como certo e como errado. Aí depois de um tempo ele começa a entender quais são os limites dele esperado para o quanto que ele pode

06:54

responder inferindo, quanto que não, você já vai meio que afinando ele pra você. Só que eu não gosto muito não. O que eu acho que acontece é, por exemplo, depois que você já tem alguns anos usando, por base ele começa a falhar menos. Então, por exemplo, eu vejo que a minha conta do...

07:11

chatGPT, ela é muito mais afinada do que a minha do Gemini, que é muito mais afinada do que a Manus, que eu uso a menos tempo, que é menos afinada talvez do que o Llama, que eu usei pouquíssimo. Então cada um deles ele fica mais organizado ao longo do tempo. Então é uma outra dica que eu dou também, se você não ficar piquicando de um pro outro, normalmente você vai ter um assistente ali que te responde melhor, tá? Então é uma dica, tá? Você não precisa fazer isso que eu tô falando, também se você quiser ficar testando todos, fica à vontade.

07:40

É bom, é interessante para você ver, mas eu não sei se você vai conseguir ter um agente ou uma LLM que ela te entende tão bem no final das contas, porque eu vejo que ela começa a responder melhor ao longo do tempo.

07:58

Deixa eu falar algumas coisas que são importantes aqui. Tudo isso que eu falei, tem casos reais que aconteceram. Então eu vou falar pra vocês alguns casos, inclusive eu tinha até pensado em deixar aqui os links, mas como é vídeo não vai ter como clicar. Então se vocês quiserem pesquisar pra ver que eu não tô mentindo, que eu não alucinei, pesquisem. Tem um caso que eu até separei

08:21

3 casos que são de advogados que tiveram um problema, casos jurídicos que tiveram um problema com a alucinação de AI, porque usaram pra cenários muito precisos, foi aquilo que eu falei, faz a defesa de alguém, pode ser que essa pessoa seja presa ou seja absolvida, vai ter juízo olhando aquilo no detalhe, tem que tomar cuidado, porque a AI pode sim alucinar.

08:43

Pode ter bastante chance de alucinar. Ou para algum caso médico. Tem alguns casos médicos que eu não coloquei porque as fontes já saíram, sumiram. Então tinha alguns jornais que tinham postado, eu me lembro disso, mas agora quando eu entro nos links eles estão como 404 ou tão fora.

09:00

Pode ser porque teve algum processo judicial e etc. Eu achei melhor não colocar pra também não expor um caso que às vezes depois foi dado como inconsistente. Mas eu sei que saiu na mídia alguns de medicina também. Às vezes também tiraram do ar porque podia citar os pacientes e tal. Bom, o que seja, não tem. Mas eu tenho esses três casos aqui que eu trouxe pra vocês. Tem mais casos de jurídico, mas pra não ficar amassante eu trouxe três pra gente conversar e vocês entenderam o tamanho da encrenca.

09:26

Então tem o caso do Royer vs Nelson de Utah em 2025. O que aconteceu? O advogado, o nome dele é Richard Bednar, ele usou uma citação que era inexistente. Então pensa o seguinte, ele pegou lá o caso e pediu pra IA gerar um processo judicial pra levar e quando ele levou a citação

09:54

o tribunal não achou nenhum registro do caso que ele citou, ou seja, ele deve ter citado algum caso parecido, similar, algum tipo de coisa nesse sentido, e o tribunal não encontrou. A consequência é que ele teve que se retratar formalmente, porque afinal não existia aquilo,

10:10

o tribunal ele estabeleceu ali algumas diretrizes um pouco mais chatinhas no uso de I.A. e daí se eu não me engano nos Estados Unidos é por estado então cada estado acabou sofrendo diferente pra I.A. mas nesse estado em Utah foi isso que aconteceu tá bom então

10:31

O que fica aqui é que mesmo um erro factual, não é um erro de uma informação errada no final das contas, só pra vocês entenderem. Não é que ele criou algo que era incoerente constitucionalmente, eu nem sei dizer se era. Mas ele criou um fato, ele inventou um fato, que até poderia ser coerente constitucionalmente, mas é inventado. Então esse é o ponto, o fato nasceu, ele brotou. E daí faz perder a credibilidade, possivelmente deve ter tido um impacto super negativo.

11:00

pro advogado ali, pro Richard, então é complicado, tem que tomar cuidado. Você quer saber mais sobre isso? No The Guardian tem, tá? Então se você for lá no The Guardian e procurar caso Royer vs Nelson, você vai conseguir achar, tá? E esse caso, então, é um dos casos que aconteceu. Tem mais um caso que é do escritório que é o K.A.L.

11:26

também nos Estados Unidos em 2025, lá os caras estão usando mais, então os advogados ali, eles foram multados em mil dólares, mil e cem dólares, não, trinta e um mil dólares, perdão.

11:39

31 mil dólares porque eles apresentaram uma peça jurídica lá com seis citações inexistentes e todas elas depois eles falaram que foram geradas por I.A. então o juiz ele achou que era negligente e daí com isso tanta reputação do escritório porque aqui é um escritório grande tá

11:59

É um escritório grande dos Estados Unidos. Tanto o escritório quanto os advogados acabaram tendo um prejuízo legal na sua reputação sem contar os 31 mil dólares. Eu acho que 31 mil dólares para uma empresa de...

12:15

de advocacia não vai ser nada muito grande, mas em compensação você sai como... imagina sua empresa falando que você usou I.A. e usou errado. Eu se eu fosse procurá-los pra me defender eu ia ficar um pouco pé atrás. Esse caso tem no The Verge, se vocês procurarem no jornal The Verge vocês vão achar também.

12:36

Tem mais um caso do Alabama, do escritório Butler Snow. O que aconteceu? Foi o estado do Alabama que contratou o escritório pra defender o sistema prisional em um processo de violação de direitos humanos. Só que o escritório usou I.A. pra gerar argumento. E daí o que ele fez? Colocou citações falsas.

12:59

e daí por isso o estado teve que pagar, ai que o buraco foi mais embaixo, foram milhões de dólares e teve ali imagem comprometida também pro estado e daí aqui ficou muito complicado porque daí ainda

13:13

resvalou no uso de dinheiro público para defesa usando I.A. Aí olha outra discussão que abriu outro parêntese de discussão sobre o uso de I.A. Então aqui, o que eu queria deixar claro, a empolgação do uso de I.A. precisa acontecer, a gente precisa querer usar, mas precisa ter cautela, ela ainda não é

13:31

o gênio da lâmpada que vai chegar e vai resolver toda a nossa vida. A gente tem que olhar, a gente tem que... É como se fosse... Eu costumo brincar que é como se fosse... Desculpa estagiários, eu já fui estagiário também, mas é como se fosse o seu estagiário, você precisa validar, você não pode chegar aquilo e jogar para frente como se fosse verdade absoluta. É alguém que está aprendendo, então você precisa estar ali para fazer um feito conferido, tá bom? Então, é super importante. Esse caso também está no The Guardian, se eu não me engano. Então, vocês podem procurar lá...

14:00

do Butler Snow, a empresa de advocacia que tomou esse problema. Então eu trouxe esses casos só pra vocês verem que eu não tô alucinando e nem inventando. Tem mais casos, se vocês procurarem na internet vocês vão achar mais alguns casos, é só procurar no Google que seja.

14:17

os casos que tiveram de alucinação de IA, você consegue achar lá e daí você consegue ler ou traduzir a página, falar quem sabe inglês, mas é só você traduzir a página se você não sabe, né? Mas você sabe inglês também, você consegue ler lá, porque a maior parte dos casos que você encontra são dos Estados Unidos. No Brasil, eu nunca vi nenhum caso disso acontecendo. Eu não sei se tem alguma coisa que os escritórios não estão usando ou se eles ficaram mais receosos dados os problemas que aconteceram. Bom, é isso. Já já a gente volta, então, pra próxima aula.

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (Modelo de Linguagem de Grande Porte)  
- **AI / IA** — *Artificial Intelligence* / Inteligência Artificial  
- **ChatGPT** — modelo de conversação da OpenAI  
- **Gemini** — família de modelos de IA do Google  
- **Copilot** — assistente de IA da Microsoft  
- **Llama** — família de modelos de linguagem da Meta  
- **Manus** — ferramenta/agente de IA mencionada em aula  

**Resumo**  
A aula apresentou técnicas práticas para reduzir alucinações em LLMs durante o uso no dia a dia. O instrutor explicou que uma das formas mais eficazes de diminuir respostas inventadas é restringir o espaço de resposta do modelo, pedindo fontes confiáveis, autores, estudos e delimitando onde a busca deve ocorrer, como jornais específicos ou publicações acadêmicas. Essa abordagem força a resposta a se apoiar em evidências verificáveis, especialmente quando há enriquecimento com dados externos e quando o domínio consultado é bem nichado.

Outra estratégia destacada foi o uso de instruções de cautela, como orientar o modelo a responder “não sei” quando não houver certeza e a evitar inventar informações ausentes. Segundo o instrutor, isso reduz a tendência do modelo de completar lacunas de forma excessivamente criativa, trocando respostas confiantes porém erradas por respostas mais conservadoras. Em seguida, foi apresentada a ideia de pedir um passo a passo do raciocínio antes da conclusão, chamada na aula de Chain of Truth Proofing, para expor a estrutura lógica da resposta e facilitar a identificação de saltos indevidos ou extrapolações sem base.

Também foi enfatizada a importância de declarar previamente o papel e os limites operacionais do assistente, seja por contexto persistente, pastas de conversa ou configuração de agente, como em ChatGPT, Copilot, Gemini, Llama e Manus. O exemplo dado incluiu restringir o modelo a dados até determinado ano e impedir previsões do futuro. Além disso, o instrutor citou o Few-shot Prompting como técnica para reduzir ambiguidade por meio de exemplos concretos de respostas corretas e incorretas, embora tenha observado que essa abordagem exige mais trabalho. Por fim, ele comentou que o uso contínuo de uma mesma ferramenta tende a deixá-la mais alinhada ao estilo do usuário ao longo do tempo.

Na parte final, a aula mostrou casos reais de alucinação em contexto jurídico para reforçar os riscos práticos do problema. Foram citados exemplos em que advogados usaram citações inexistentes geradas por IA, resultando em retratação formal, multas, dano reputacional e prejuízos financeiros elevados. O instrutor concluiu que LLMs devem ser tratadas como apoio produtivo, comparáveis a um estagiário que acelera o trabalho mas exige revisão, sobretudo em áreas sensíveis como direito e medicina, onde erros podem causar danos materiais, institucionais ou humanos.

**Pontos de atenção**  
- Restringir o local de busca e exigir fontes verificáveis ajuda a reduzir alucinações.  
- Pedir autores, estudos e referências explícitas facilita auditoria humana.  
- Instruções como “se não tiver certeza, diga que não sabe” e “não invente informações” devem ser usadas para conter extrapolações.  
- Pedir o raciocínio passo a passo ajuda a detectar saltos lógicos e conclusões sem base.  
- Declarar papel, escopo e limites do modelo com antecedência melhora a consistência das respostas.  
- Fixar contexto persistente ou usar configuração de agente evita repetir regras em toda interação.  
- Few-shot Prompting pode calibrar melhor o comportamento, mas exige tempo para preparar bons exemplos.  
- Alternar constantemente entre ferramentas pode diminuir o alinhamento operacional; estabilidade tende a ajudar.  
- Em domínios jurídicos e médicos, plausibilidade textual não basta: é obrigatória a verificabilidade documental.  
- Alucinação em documentos formais pode gerar retratação, multa, perda de credibilidade e prejuízo financeiro.  
- IA deve ser tratada como apoio, nunca como autoridade final; toda saída crítica precisa de revisão humana.