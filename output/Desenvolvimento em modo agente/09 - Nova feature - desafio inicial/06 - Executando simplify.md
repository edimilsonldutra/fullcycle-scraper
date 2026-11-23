Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17994)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, no vídeo anterior, a gente basicamente fez todo esse processo,

00:07

gerou uma pull request, fez o merge, a gente navegou,

00:10

viu que ele fez o upload do arquivo e tudo mais.

00:13

Alguns passos que eu sempre recomendo você fazer, eu não vou fazer isso até o fim,

00:17

mas basicamente rodar um simplify antes de você fazer

00:21

as pull requests ou gerar algum commit final.

00:24

Muitas vezes, o que esse cara aí vai fazer?

00:26

Ele vai te ajudar a tentar... a simplificar arquivos, agrupar, extrair,

00:33

esse tipo de coisa. Isso faz parte do processo de desenvolvimento.

00:37

Inclusive, você pode colocar isso, inclusive, no seu próprio agente.

00:42

Então, no meu agente que fazia o desenvolvimento,

00:46

eu podia pedir para ele dar um simplify no final ou alguma coisa desse tipo.

00:51

Não teria problema nenhum,

00:52

mas eu não quis deixar isso atribuído a um plugin específico,

00:57

tá? Mas se você olhar agora aqui...

00:59

Ele está fazendo um review aqui em três aspectos de eficiência. Aqui,

01:05

a revisão de altitude e reuso de código. Aqui, provavelmente, ele vai ter mais um agente.

01:11

São quatro agentes que ele deve estar rodando aqui.

01:13

Eficiência, reuso e simplificação.

01:15

Ele vai pegar tudo que ele encontrou em relação, dando um diff ali da implementação,

01:21

e ele vai ver o que ele consegue melhorar

01:23

para que esse código seja mais simplificado.

01:27

Isso aí é um ponto importante que vale sempre a pena você fazer,

01:32

tá? Isso já virou meio que padrão pra mim.

01:34

Eu sempre rodo o simplify antes de fazer outros commits ou... Na realidade,

01:41

você deixa ele fazer os commits e depois você pode rodar um simplify.

01:45

E por isso que é importante você ter os testes, todos os gates organizados,

01:49

porque às vezes o simplificador pode querer mudar um pouco a sua arquitetura.

01:54

E aqui, do jeito que eu estou trabalhando,

01:56

toda vez que ele tenta bater em qualquer coisa que vai

02:00

sair do padrão do que eu estou imaginando de código,

02:03

o que vai acontecer no final das contas é que o gate vai barrar.

02:06

e aí ele é obrigado a seguir e se adaptar

02:09

em relação à parte de como que acaba ficando,

02:12

tá? O interessante é que, conforme o software vai amadurecendo,

02:15

os padrões dentro de convenções já vão ficando mais claros,

02:19

né? Então, raramente o agente vai querer se desviar,

02:22

mas caso ele comece fazendo aqueles desvios pequenos e que

02:26

sejam gritantes em algum momento para ferir o gate,

02:29

o gate ele é, como que a gente pode dizer, determinístico,

02:33

então a gente vai evitar esse tipo de problema.

02:36

Então, esse aqui é o nosso primeiro aspecto que a gente tem que lembrar.

02:39

Ele, eu acho que terminou de todos os agentes rodarem para fazer

02:43

a verificação e agora provavelmente ele vai fazer o processo de simplificação.

02:48

Outra coisa, se eu poderia, e eu recomendo,

02:51

é que você crie uma nova sessão para fazer a simplificação.

02:54

Perceba que eu não criei uma nova aqui, fiquei falando.

02:57

Apesar de que, do subagente, ele usar uma nova janela de

03:01

contexto, ele usou a janela anterior que eu tinha,

03:04

eu poderia ter limpado a sessão.

03:06

Acho que seria mais interessante aqui, tá?

03:09

Então agora provavelmente ele encontrou aqui, ó.

03:14

Inclusive encontrou um dead update method no video repository.

03:18

Onde ele consegue fazer simplificação,

03:20

Reuso e tudo mais. Galera, vou esperar ele terminar de trabalhar.

03:27

E depois eu quero fazer algumas experiências aqui com

03:30

Ele em relação ao que ele aprendeu,

03:34

Aonde ele pode ter tido mais dificuldade ou coisas desse tipo que a gente

03:39

Pode utilizar talvez ali no Cloud.md para acabar melhorando toda a experiência.

03:47

Então vamos aguardar esse cara aí.

03:51

Pronto, e aqui ele acabou rodando o simplificador e etc.

03:56

E ele trouxe aqui o que ele acabou arrumando. Então,

03:59

Ele reutilizou, deduplicou e fez essas duplicações aqui,

04:04

E outros pontos que ele tinha achado,

04:06

Ele achou que provavelmente não valeria a pena fazer isso,

04:09

E ele trouxe o porquê que ele acabou não fazendo.

04:12

Então, a gente fez mais esse processo,

04:17

E eu poderia ter feito esse processo antes, mas novamente,

04:21

Quando acontece isso aqui, commands commit push pr,

04:26

Para que você possa subir esse tipo de pull request e etc.

04:33

Agora, o lance é o seguinte,

04:36

No próximo vídeo a gente vai voltar e nós vamos falar sobre o Cloud.md, o Agents.md,

04:42

Para a gente reavaliar esse cara e ver como é que ele pode ter,

04:47

No final das contas,

04:49

Ficado desatualizado ou se tem coisa que a gente poderia melhorar e etc.

04:54

Tem um plugin legal do Cloud para fazer esse tipo de verificação,

04:59

Mas também você pode criar um prompt ou mesmo escrever,

05:03

Perguntar para o Cloud o que você aprendeu nessa nova

05:06

Sessão que pode evitar que eu tenha esse problema.

05:11

A gente vai falar sobre isso ali no futuro.

05:14

Só vou fazer o merge desse

05:18

Ajuste aqui para mim e

05:25

Vou já deletar o branch lá em cima.

05:28

E a gente se vê aí no próximo vídeo.

## Resumo IA

**Abreviações**
*   **PR**: Pull Request - Um processo de colaboração de código onde um desenvolvedor pede que as alterações que fez em uma branch sejam revisadas e incorporadas em outra branch (geralmente a principal) de um repositório.

**Resumo**
Esta aula dá continuidade a um processo de desenvolvimento de software, focando na etapa de melhoria e padronização do código antes de um commit final ou pull request. O objetivo principal é introduzir e demonstrar o uso da ferramenta "simplify" e agentes de inteligência artificial para otimizar o código. O instrutor explica que o processo de "simplify" é um passo padrão que ele recomenda executar para simplificar arquivos, agrupar, extrair, reutilizar e deduplicar código.

O fluxo explicado envolve a execução do "simplify" após a implementação e, idealmente, antes da submissão de um pull request. Durante o processo de simplificação, múltiplos agentes (quatro, neste caso) são acionados para revisar o código em busca de eficiência, reuso e simplificação, gerando um "diff" das melhorias propostas. A aula destaca a importância de ter testes e "gates" bem organizados, que funcionam como barreiras para garantir que o processo de simplificação não desvie a arquitetura do projeto. O instrutor também sugere a integração do "simplify" no agente de desenvolvimento principal e a criação de uma nova sessão de contexto para o processo de simplificação, garantindo um ambiente limpo para o trabalho dos agentes. Ao final, é mencionado que os arquivos `Cloud.md` e `Agents.md` serão abordados no próximo vídeo para reavaliar e melhorar a experiência de desenvolvimento com base nos aprendizados da sessão.

**Pontos de atenção**
*   **Rodar `simplify` regularmente**: Recomenda-se rodar o processo de `simplify` (para simplificar, agrupar, extrair, reutilizar e deduplicar código) antes de fazer `pull requests` ou gerar `commits` finais.
*   **Integração com agentes**: O processo de `simplify` pode ser integrado ao agente de desenvolvimento, pedindo para ele executar a simplificação ao final do desenvolvimento.
*   **Importância dos testes e `gates`**: É crucial ter testes e `gates` bem organizados, pois o simplificador pode tentar alterar a arquitetura do código. Os `gates` atuam de forma determinística, barrando qualquer desvio do padrão de código esperado e forçando o agente a se adaptar.
*   **Criação de nova sessão para simplificação**: É uma boa prática e recomendação criar uma nova sessão de trabalho ao iniciar o processo de simplificação, ou limpar a sessão anterior, para garantir um contexto limpo e evitar o uso de uma janela de contexto anterior pelo subagente.
*   **Revisão e aprendizado contínuo**: Sugere-se reavaliar o que os agentes aprenderam em cada sessão (mencionado o uso de `Cloud.md` e `Agents.md` no futuro) para identificar dificuldades e melhorar a experiência de desenvolvimento e evitar problemas recorrentes.