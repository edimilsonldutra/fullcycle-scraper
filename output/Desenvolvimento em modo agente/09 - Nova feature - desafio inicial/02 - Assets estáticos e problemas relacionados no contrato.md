Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17990)

## Resumo da aula



## Transcrição

00:00

Bom, pessoal, aqui está uma das partes aqui muito importantes,

00:06

que é o seguinte, que é o nosso contract.md.

00:09

Esse cara, ele vai ser usado, né,

00:11

tanto para escrever a feature, para desenvolvimento,

00:14

quanto para avaliação. Mas por que eu estou dizendo que esse cara aqui,

00:18

nesse momento, ele é crítico?

00:19

Porque a gente está fazendo um teste de uma plataforma de upload de vídeo.

00:24

Para ele fazer o upload de vídeo, ele vai ter que fazer o quê?

00:28

Ter vídeos para fazer uploads e testar o upload, né?

00:31

E todo o contrato, ele exige uma infraestrutura ali inicial,

00:37

né? Então, ele existe,

00:40

ele traz aqui para a gente um persistent state aqui para a gente,

00:44

que é o user Alice, com o token de sessão,

00:48

um usuário de Bob, um usuário de um vídeo existente,

00:53

né? Ele traz aqui diversas situações que ele vai precisar e beleza.

00:57

Mas olha só que interessante, tá?

01:01

Tudo isso aqui eu não estou preocupado porque são dados registros no banco de dados.

01:05

Por outro lado, olha só,

01:07

Static Inputs. Ele vai precisar de um vídeo de exemplo, ou seja, um MP4 válido,

01:13

que vai ter aproximadamente, nesse caso aqui, 256 KB, que o FFM,

01:19

o PROB vai verificar se a duração dele está ok,

01:22

e vai ser usado para upload todos esses pontos aqui dessas features.

01:27

Ele vai precisar de uma fixture aqui de unsupported

01:30

e ele vai precisar também aqui de um oversize

01:35

vídeo MP4, um arquivo que vai estar no disco

01:40

materializado em um test setup que vai ser reportado com

01:46

um tamanho maior que 2 gigas, que vai ser usado nesse ponto aqui, e um outro cara aqui

01:53

é um vídeo com codec ruim pra fazer essa parte

01:58

aqui de caso o vídeo provavelmente inválido, etc.

02:02

Aqui tem as configurações, o max upload bytes e etc.

02:06

Dependências externas, ffmpeg e ffprobe,

02:11

eu tenho na minha máquina aqui para mim e eu não quero me preocupar com ela.

02:15

Agora, nesse tipo de situação, como que a gente trabalha?

02:22

Eu vou prover esse arquivo para a IA.

02:24

Ela vai criar esse arquivo e por isso que não existe uma mágica por trás das coisas, tá?

02:32

Se eu rodar o agente agora aqui, a gente pode fazer essa experiência,

02:36

a gente pode ver o que ele vai tentar fazer.

02:40

Provavelmente a IA vai conseguir e provavelmente ela vai gerar um arquivo,

02:47

né? Ela vai fazer um vídeo.

02:49

Eu não duvido nada de ela fazer um vídeo somente

02:52

para ela conseguir trabalhar e ter esse input estático.

02:55

Por outro lado,

02:56

eu tenho esse teste aqui onde o vídeo tem que ter mais de 2 GB.

03:01

E, obviamente, eu não vou commitar isso também no meu repositório. Então,

03:06

como é que essas coisas aí ficam nesses momentos? Então,

03:10

é esse tipo de coisa que a gente tem que levar em consideração.

03:14

E tem várias decisões que eu posso tomar. Por exemplo,

03:19

eu posso pegar um vídeo estático meu e colocar ali,

03:23

ou esses vídeos pequenos ela mesma pode gerar, e esse vídeo oversized,

03:28

por exemplo, eu posso ter um script que gera esse vídeo.

03:33

Que vai rodar, e esse script fica, por exemplo,

03:38

No meu .gitignore, quer dizer, o script não,

03:42

O vídeo fica no meu .gitignore,

03:45

Para garantir que isso não vá para o meu repositório.

03:48

Então... Perceba, galera, que não tem almoço grátis dependendo da situação.

03:54

Você tem que tomar algumas decisões dependendo da situação,

04:00

Do seu tipo de software.

04:02

Existem softwares, por exemplo, que eu vou trabalhar muito com software de IA,

04:05

Que eu preciso de datasets.

04:07

Eu não posso sair pedindo para IA sair criando aleatoriamente datasets.

04:11

Eu tenho que ter esses tipos de direcionamento.

04:14

O fato é que, para eu conseguir testar, para eu desenvolver uma feature de upload,

04:18

Eu preciso ter exemplos de vídeo de upload. É um fato.

04:22

E se eu quiser testar... Se realmente os meus limites de upload, né?

04:26

O máximo de limites estão certos,

04:28

Eu preciso ter os arquivos com esses limites aqui para mim,

04:32

Tá? Então, como que a gente pode trabalhar em cima disso?

04:37

Eu posso utilizar a própria IA para ela me ajudar a trabalhar aqui nesses aspectos,

04:44

Tá? Então, a gente vai ver isso no nosso próximo vídeo.

## Resumo IA

**Abreviações**
*   **contract.md**: Arquivo de especificação de contrato.
*   **MP4**: MPEG-4 Part 14, um formato de contêiner multimídia digital.
*   **KB**: Kilobytes.
*   **GB**: Gigabytes.
*   **FFMPEG**: Fast Forward MPEG, um conjunto de bibliotecas e programas para manipulação de arquivos multimídia.
*   **FFPROBE**: Uma ferramenta de análise de streams multimídia, parte do projeto FFmpeg.
*   **IA**: Inteligência Artificial.
*   **.gitignore**: Um arquivo usado em sistemas de controle de versão Git para especificar arquivos e diretórios que devem ser ignorados.

**Resumo**
A aula aborda a importância crítica do arquivo `contract.md` no desenvolvimento e avaliação de uma plataforma de upload de vídeo. O objetivo principal é demonstrar como o `contract.md` define não apenas o estado persistente inicial (como usuários e tokens de sessão), mas também os "Static Inputs" essenciais para testar a funcionalidade de upload. São apresentados diversos tipos de vídeos necessários para teste: um MP4 válido de tamanho pequeno (aproximadamente 256 KB) para uploads básicos, verificado pelo FFPROBE; uma fixture de vídeo não suportado; um vídeo MP4 "oversize" (maior que 2 GB) para testar limites de upload; e um vídeo com codec ruim para validar cenários de arquivo inválido.

O instrutor destaca o desafio de gerenciar esses arquivos de entrada estáticos, especialmente os de grande porte, sem que sejam commitados no repositório. Ele explora possíveis soluções, como a utilização da IA para gerar vídeos menores, a criação de scripts que gerem vídeos "oversize" sob demanda, e o uso do `.gitignore` para excluir esses arquivos gerados do controle de versão. O instrutor enfatiza que, embora a IA possa auxiliar, não existe uma "mágica" para a geração de dados de teste, e decisões estratégicas precisam ser tomadas para cada tipo de software e cenário, especialmente ao lidar com datasets em softwares de IA. O próximo vídeo abordará como a IA pode ser empregada para auxiliar nesses aspectos.

**Pontos de atenção**
*   **`contract.md` como elemento crítico**: Fundamental tanto para a escrita de features quanto para a avaliação, definindo a infraestrutura inicial (`persistent state`) e os `static inputs` necessários.
*   **Necessidade de inputs estáticos diversos**: Para testar a funcionalidade de upload de vídeo de forma abrangente, é crucial ter uma variedade de arquivos de vídeo, incluindo válidos (pequenos), não suportados, "oversize" (grandes) e com codecs ruins.
*   **Gerenciamento de dependências externas**: Ferramentas como `ffmpeg` e `ffprobe` são essenciais para processamento e verificação de vídeo e devem ser consideradas.
*   **Evitar o commit de arquivos grandes**: Vídeos de teste volumosos (ex: >2 GB) não devem ser commitados no repositório. Deve-se usar estratégias como scripts de geração e `.gitignore` para mantê-los fora do controle de versão.
*   **Decisões estratégicas sobre dados de teste**: Não há "almoço grátis". É preciso tomar decisões conscientes sobre como gerar e gerenciar dados de teste, especialmente em softwares que dependem de datasets específicos (como os de IA), onde a geração aleatória pela IA pode não ser adequada.
*   **Uso consciente da IA**: Embora a IA possa auxiliar na geração de alguns dados de teste (ex: vídeos pequenos), ela não substitui a necessidade de direcionamento e estratégias bem definidas para inputs estáticos, especialmente para cenários complexos ou arquivos muito grandes.