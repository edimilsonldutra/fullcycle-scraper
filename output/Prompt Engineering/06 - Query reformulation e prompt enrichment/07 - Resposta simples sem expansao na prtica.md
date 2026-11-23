Módulo: Prompt Engineering\
Aula: [Fazendo pull e controle de versão](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/267/conteudos?capitulo=267&conteudo=16751)

## Resumo da aula

Agora quero mostrar algumas coisas na prática para você entender a ideia principal. Tenho três arquivos, mas na realidade são dois exemplos que quero trazer. Um é sobre o loop iterativo para obter uma resposta mais completa. O segundo exemplo é sobre como enriquecer uma pergunta ampla ou mal formulada, transformando-a em uma pergunta mais completa.

O Iter-RetGen tem como objetivo trazer uma resposta mais completa. O Query Enrichment tem como objetivo trazer uma pergunta mais completa. São dois objetivos completamente diferentes: um gera respostas completas a partir de perguntas vagas; o outro melhora as próprias perguntas.

Vou explicar o que fiz. Tenho um exemplo chamado "No Expansion". Basicamente, peguei um modelo GPT-4.0 (apesar de já existirem versões mais recentes) e configurei uma temperatura um pouco mais alta para ele ser mais criativo. Utilizei um prompt genérico: "Você é um assistente na área de tecnologia. Responda à seguinte questão." Criei uma chain que envia o prompt para o LLM e obtém a resposta final.

A pergunta utilizada foi: "Explain about LangChain and LangGraph". Vou executar este exemplo com "python no_expansion.py". Aguardamos um pouco, pois não estou usando streaming.

O GPT-4.0 traz informações interessantes: LangChain e LangGraph são ferramentas para facilitar o desenvolvimento, com LangChain tendo certos aspectos e LangGraph outros. Ele fornece um resumo.

Porém, dependendo da situação, poderíamos querer mais detalhes. Às vezes, estamos buscando um documento com nuances maiores para realizar uma busca mais aprofundada. O que recebemos aqui é basicamente o conteúdo de uma resposta, que poderia ser cruzado com nosso banco de dados ou servir como resposta final para o usuário, que foi o caso.

No próximo vídeo, mostrarei a utilização desses fluxos interativos para enriquecer esse tipo de resposta, e começaremos a ver as diferenças de como isso funciona.

## Transcrição

00:01

Bom, pessoal, agora eu quero mostrar algumas coisas aqui na prática para você conseguir entender a ideia principal. Eu tenho três arquivos, mas, na realidade, são dois exemplos que eu quero trazer aqui para você. Um é sobre esse loop interativo para que eu consiga ter uma resposta mais completa, vamos dizer assim.

00:20

E o segundo exemplo é como que eu consigo enriquecer uma pergunta onde eu tenha uma pergunta ampla, uma pergunta, vamos dizer, mal feita, e eu consiga terminar com uma pergunta mais completa. Então, o Iter aqui, o Ratjen, a ideia dele é trazer uma resposta mais completa.

00:45

O Query Enrichment, o objetivo dele é trazer uma pergunta mais completa. Então, são duas coisas completamente diferentes em relação a objetivos aqui. Primeiro, é trazer uma resposta completa.

01:01

com uma pergunta vaga. O outro é trazer uma pergunta completa com uma pergunta vaga. Então, um tem a ver em gerar perguntas, quer dizer, gerar respostas, e o outro tem a ver com melhorar as perguntas. E a gente vai fazer o seguinte, somente para você entender o que eu fiz.

01:22

Eu tenho aqui um exemplo zero que eu chamei de No Expansion. O que isso significa? Basicamente, eu peguei aqui um modelo GPT-4.0, apesar de a gente já ter GPT-5 e tudo mais,

01:37

Coloquei uma temperatura até um pouco mais alta para ele ser um pouquinho mais criativo. Mas perceba que eu coloquei um prompt genérico aqui com a gente, tá? Basicamente, o que eu tenho? Você é um assistente na área de tecnologia. Responda à seguinte questão.

01:56

E depois, baseado nisso, eu criei um chain pegando o prompt, mandando para o LLM e pegando a resposta final. E aqui está a minha pergunta. Explain sobre lang chain e lang graph. Então, essa é a minha pergunta, onde eu tenho aqui a minha resposta quando eu executar. Então, vamos rodar esse cara aqui. Vou colocar Python.

02:22

Tá? Zero aqui no Expansion. Vou dar um Enter. E agora eu vou receber uma resposta.

02:30

E vamos aguardar essa resposta agora aqui, ele demora um pouquinho, eu não estou pegando informação v-streaming. Mas, se você perceber agora aqui, eu tenho um modelo muito bom, que é o GPT-4.0, e ele está trazendo informações interessantes. O LangChain e o LangRef são ferramentas para facilitar o desenvolvimento. O LangChain tem esses aspectos aqui, o LangRef tem esses aspectos, e trouxe aqui para mim um resumo e maravilha.

02:57

Mas, dependendo da situação, eu poderia querer mais detalhes. Às vezes, eu não estou nem buscando por um documento maior. Mas, às vezes, eu estou buscando um documento com nuances maiores para eu fazer a minha busca. Perceba que...

03:15

Isso aqui que a gente está recebendo, basicamente, é o conteúdo de uma pergunta. E o conteúdo dessa pergunta poderia ser cruzado agora com o nosso banco de dados, por exemplo. Ou ele poderia ser realmente uma resposta para o usuário final, que é o que aconteceu. A gente recebeu uma resposta aqui para o usuário final.

03:39

No próximo vídeo, eu vou trazer aqui para você a utilização desses fluxos iterativos para conseguir enriquecer esse tipo de resposta, e a gente vai começar a ver um pouco a diferença de como isso funciona. Beleza? Então, vamos nessa!

## Resumo IA

**Abreviações**  
- **LLM** — *Large Language Model* (modelo de linguagem de grande porte)  
- **GPT-4.0** — *Generative Pre-trained Transformer 4.0*  
- **GPT-5** — *Generative Pre-trained Transformer 5*  
- **Iter-RetGen** — *Iterative Retrieval-Generation*  
- **Query Enrichment** — enriquecimento de consulta/pergunta  
- **LangChain** — framework para construção de aplicações com LLMs  
- **LangGraph** — framework para criação de fluxos e agentes com grafos  
- **chain** — encadeamento/fluxo de etapas de processamento  
- **prompt** — instrução/pergunta enviada ao modelo  
- **streaming** — geração de resposta em fluxo contínuo  

**Resumo**  
A aula apresentou, na prática, dois conceitos diferentes: o Iter-RetGen, cujo objetivo é obter uma resposta mais completa por meio de iteração, e o Query Enrichment, cujo objetivo é transformar uma pergunta ampla ou mal formulada em uma pergunta mais completa e precisa. O instrutor destacou desde o início que essas abordagens têm finalidades distintas: uma melhora a qualidade da resposta gerada e a outra melhora a qualidade da própria pergunta.

Para exemplificar um cenário base, foi mostrado o caso “No Expansion”, em que se utiliza um modelo GPT-4.0 com temperatura um pouco mais alta para aumentar a criatividade. Nesse fluxo, foi usado um prompt genérico — “Você é um assistente na área de tecnologia. Responda à seguinte questão.” — e construída uma chain simples que envia o prompt ao LLM e retorna a resposta final. A pergunta de teste foi “Explain about LangChain and LangGraph”, executada via script Python sem streaming, o que faz a resposta demorar um pouco mais para aparecer.

O resultado obtido foi uma resposta resumida, porém útil, explicando que LangChain e LangGraph são ferramentas que facilitam o desenvolvimento, cada uma com seus próprios aspectos e finalidades. O instrutor observou que esse tipo de saída pode ser suficiente como resposta ao usuário final, mas em alguns contextos seria desejável obter mais detalhes e nuances. Também comentou que esse conteúdo poderia servir como base para cruzamento com banco de dados em um processo de busca mais aprofundada. A aula encerra preparando o terreno para o próximo passo: mostrar fluxos iterativos aplicados ao enriquecimento desse tipo de resposta.

**Pontos de atenção**  
- **Iter-RetGen e Query Enrichment não são a mesma coisa**: um busca melhorar a resposta, o outro busca melhorar a pergunta.  
- **Prompt genérico gera respostas mais gerais**: se a intenção for maior precisão ou profundidade, o prompt precisa ser mais elaborado.  
- **Temperatura mais alta aumenta criatividade, mas pode reduzir determinismo**: use com cuidado conforme o objetivo.  
- **Sem streaming, a percepção de demora aumenta**: a execução pode parecer lenta até a resposta completa ser gerada.  
- **Uma resposta útil nem sempre é uma resposta suficientemente rica**: em alguns cenários, é necessário mais detalhe para análise, busca ou cruzamento com dados.  
- **Saída do modelo pode ser reutilizada em outros fluxos**: a resposta gerada pode servir como insumo para recuperação de માહિતી/dados ou para a etapa seguinte do pipeline.