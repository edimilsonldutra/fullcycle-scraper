Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17993)

## Resumo da aula



## Transcrição

00:01

Bom pessoal, ele criou ali a nossa feature, né?

00:04

E eu não vi como é que a coisa ficou,

00:06

então tô vendo aqui agora junto com vocês, ele criou inclusive a PR,

00:09

tá? E eu vou colocar aqui, me passe a URL do ambiente.

00:19

E vamos ver em qual porta ele colocou, somente pra eu lembrar e tudo mais.

00:24

Vamos ver agora aqui, ele tá falando que tá rodando na porta 40.

00:30

38 e etc, meu ambiente já foi encerrado, na realidade ele já foi encerrado, vamos

00:39

aguardar, e pronto, ele trouxe aqui para mim, então a web está acessando aqui,

00:45

o login está aqui, e o login após, após o login vai cair no barra app,

00:50

e o back-end está trabalhando aqui nessa porta,

00:53

então eu vou já mandar ele cair aqui para mim no login,

00:58

vamos lá, vou colocar ali admin, arroba, arroba,

01:03

admin.com, admin.

01:06

Ele fez o login e está aqui a parte

01:09

para eu fazer os meus uploads ali de forma geral. Então,

01:16

eu quero fazer, na realidade,

01:17

um teste aqui para a gente

01:20

brincar com os nossos uploads e etc.

01:26

Então, nesse momento, o que eu vou fazer? Eu vou arrastar um arquivo aqui dentro.

01:32

que é um dos arquivos que eu estou usando, inclusive, aqui no sistema.

01:35

E aqui, ele deu aqui, validando,

01:37

organizando aqui documentações e etc. aqui para mim.

01:41

E aparentemente, ele fez o upload aqui do arquivo para mim.

01:47

Deixa eu atualizar agora aqui.

01:51

Ele está aqui nesse processo aqui, validando,

01:54

aqui nesse caso para mim. E antes ele tinha,

01:58

inclusive, aparecido o thumbnail,

01:59

e aqui ele não está aparecendo mais o thumbnail para mim.

02:04

E agora, o que acontece é o seguinte.

02:08

Agora, provavelmente ele vai ficar nesse validando,

02:12

porque aqui era apenas o upload do vídeo, a infraestrutura para o upload.

02:16

O restante das coisas, provavelmente a parte de transcrição e todas essas coisas,

02:22

vão entrar em outras features aqui. Vamos olhar aqui, inclusive,

02:26

a nossa documentação. Vou colocar validando aqui.

02:30

Ele espera que realmente o status fique como validando. O tempo inteiro ele fala,

02:36

porque provavelmente essa feature vai se grudar com outras features aqui.

02:40

Então, em tese, a gente está ok com isso aqui.

02:45

Uma outra coisa que a gente não pode também esquecer é em relação a

02:51

o que ele pode ter aprendido durante um processo e outro e coisas desse tipo.

02:58

E eu mudei para cá e ele criou aqui essa pasta 'uploads' e se eu olhar aqui,

03:04

dentro de 'uploads' deve ter um thumbnail aqui de teste dele,

03:09

provavelmente que ele criou na hora do evaluator, né?

03:13

Não tem um arquivo aqui dentro, obviamente,

03:15

porque o arquivo ele tá esquipado e é aquele arquivo de vídeo,

03:20

então ele trouxe aqui esse thumbnail, mas aqui que é o ponto importante,

03:23

né? Onde eu tenho o thumbnail do vídeo que eu subi. Ah,

03:29

e tá aqui, ó. Aqui o thumbnail do vídeo que eu subi,

03:32

e aqui tá o vídeo... que eu subi, .mkv, que foi com essa extensão. Então,

03:37

aparentemente, galera, eu estou confiando que tudo isso está ok ali para mim,

03:43

mas eu já tenho a minha pull request pronta.

03:50

Então, ele gerou aqui para mim,

03:52

se eu quiser acessar a pull request, aqui no

03:58

GitHub, onde ele mostrou quais foram os critérios de aceitação.

04:04

Qual foi o processo de implementação. Quais foram os artefatos utilizados.

04:10

E aqui foram todos os commits que foram realizados aqui para mim.

04:14

E eu posso ali, no caso, fazer o merge do meu pull request.

04:19

Eu vou fazer o merge do meu pull request.

04:23

E vou dar um delete branch.

04:26

A gente vai entrar em outros aspectos daqui a pouquinho, já inclusive.

04:30

Mas a gente fala disso no próximo vídeo. Beleza? Então, vamos nessa.

## Resumo IA

**Abreviações**
*   **PR**: Pull Request - Solicitação de extração de código, usada no controle de versão para revisar e integrar alterações de código.
*   **URL**: Uniform Resource Locator - Endereço padronizado que identifica um recurso na internet e especifica a forma de localizá-lo.
*   **GitHub**: Plataforma de hospedagem de código para controle de versão e colaboração.

**Resumo**
A aula demonstra a validação e o fluxo de trabalho de uma nova funcionalidade (feature) de upload de arquivos. O instrutor inicia verificando a feature recém-criada e sua respectiva Pull Request (PR). Ele acessa o ambiente de desenvolvimento, identificando as portas da aplicação web e do backend, e realiza o login com credenciais de administrador. Na interface de upload, ele simula o processo arrastando e soltando um arquivo de vídeo. Durante o teste, o status do upload permanece como "validando", o que é explicado como comportamento esperado, uma vez que a feature atual cobre apenas a infraestrutura de upload, e etapas subsequentes como transcrição ou processamento de vídeo serão abordadas em futuras features. O instrutor então verifica o diretório de 'uploads' para confirmar a presença do arquivo de vídeo original (.mkv) e do thumbnail gerado. Finalmente, ele revisa a Pull Request no GitHub, analisando os critérios de aceitação, o processo de implementação, os artefatos utilizados e os commits realizados, antes de aprovar e realizar o merge da PR e deletar a branch da feature.

**Pontos de atenção**
*   **Escopo da Feature**: É fundamental entender que o status "validando" para uploads de vídeo indica que a feature implementada foca na infraestrutura de upload. Processamentos adicionais como transcrição e organização de documentação são esperados em features futuras, reforçando a importância da modularidade no desenvolvimento.
*   **Verificação de Ambiente**: Estar ciente das URLs e portas de acesso do ambiente (web e backend) é crucial para a validação das funcionalidades. A aula demonstrou a necessidade de aguardar o ambiente ser estabelecido caso tenha sido encerrado.
*   **Verificação de Artefatos Gerados**: Após um upload, é uma boa prática inspecionar o sistema de arquivos (como a pasta 'uploads') para confirmar que o arquivo original e quaisquer artefatos relacionados, como thumbnails, foram criados corretamente.
*   **Revisão Completa da Pull Request**: Antes de fazer o merge, revisar minuciosamente os critérios de aceitação, o processo de implementação, os artefatos gerados e todos os commits associados à PR é essencial para garantir a qualidade e conformidade do código.
*   **Gerenciamento de Branches**: A prática de deletar a branch da feature após o merge da Pull Request ajuda a manter o repositório limpo e organizado.