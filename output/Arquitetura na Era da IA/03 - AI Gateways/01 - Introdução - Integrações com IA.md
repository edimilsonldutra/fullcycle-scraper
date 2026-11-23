Módulo: Arquitetura na Era da IA\
Aula: [Introdução - Integrações com IA](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18285)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem? Quando a gente começa a colocar IA dentro de uma aplicação,

00:06

normalmente o primeiro caminho é bem simples.

00:09

A gente pega o SDK de um provedor, chama a OpenAI,

00:12

o Gemini, o Cloud ou qualquer outro provedor e modelos,

00:15

a gente manda um prompt e recebe uma resposta

00:18

seguindo ali o fluxo da nossa aplicação.

00:20

E para começar, isso faz todo sentido.

00:22

Se você está validando uma feature, criando um MVP,

00:25

testando uma automação interna ou colocando a IA dentro

00:28

de um ponto bem específico do sistema,

00:30

chamar um modelo direto pode ser realmente o caminho mais produtivo.

00:33

O problema começa quando esse uso cresce. No começo,

00:38

existe uma chamada, depois uma segunda feature que também precisa de AI,

00:43

depois um time cria uma outra integração,

00:45

depois alguém escolhe outro provedor,

00:47

depois uma outra parte do sistema precisa de um modelo mais barato,

00:51

outro precisa de um modelo mais rápido, outro precisa de um modelo mais forte.

00:55

E aí, quando a gente precisa às vezes utilizar,

00:58

a gente tem um erro e outra pessoa eventualmente vai precisar,

01:02

por exemplo, ter uma regra de fallback. Ou seja...

01:05

a gente precisa também, em algum momento, registrar o custo,

01:10

a latência, o consumo. E quando a gente percebe a IA,

01:14

ela deixou de ser apenas uma feature isolada e ela

01:17

passou a estar espalhada pela arquitetura do nosso sistema.

01:21

Só que ela não se espalha só como uma funcionalidade,

01:24

ela se espalha como uma decisão técnica.

01:26

Cada ponto do sistema começa a conhecer detalhes que talvez não deveriam estar ali.

01:32

Ele conhece o SDK, o provedor, o modelo, o formato de request,

01:36

o formato de response, os parâmetros específicos,

01:39

tratamentos de erro, timeout, retry, custo,

01:42

limite e até o comportamento esperado de cada modelo. E aí,

01:45

aos poucos, aquilo que parecia simples começa a ficar difícil de manter.

01:50

Trocar um provedor acaba virando uma mudança muito grande.

01:55

Trocar um modelo exige mexer em vários lugares.

01:58

Aplicar uma regra padrão fica complicado. Saber quando cada fluxo está funcionando,

02:04

quanto está gastando, cada vez fica mais confuso. Então...

02:08

Simplesmente, entender por que algo falhou quando a gente vai fazer uma chamada, a gente,

02:13

por exemplo, precisa de logs, e às vezes esses logs,

02:16

inclusive, estão ali espalhados.

02:17

Então, o ponto aqui não é dizer que chamar IA... Diretamente é errado.

02:23

O ponto é entender que chamar direto funciona muito bem no início,

02:27

mas começa a ficar frágil quando a IA vira

02:30

uma capacidade usada por várias partes do sistema.

02:33

E quando isso acontece, normalmente a arquitetura precisa de uma camada no meio.

02:38

Uma camada entre a aplicação e os modelos, entre os casos de uso e os provedores,

02:44

entre a regra de negócio e a complexidade de executar as chamadas de IA em produção.

02:50

Essa camada é o que a gente chama de AI Gateway.

02:53

E no próximo vídeo eu vou falar um pouquinho mais sobre AI Gateway e a gente vai,

02:58

então, se aprofundando um pouquinho mais. Fechou? Então, até o nosso próximo vídeo.

## Resumo IA

[RESUMO_IA]