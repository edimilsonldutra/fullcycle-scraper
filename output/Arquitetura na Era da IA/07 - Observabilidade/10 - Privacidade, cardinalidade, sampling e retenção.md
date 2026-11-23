Módulo: Arquitetura na Era da IA\
Aula: [Privacidade, cardinalidade, sampling e retenção](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/291/conteudos?capitulo=291&conteudo=18757)

## Resumo da aula



## Transcrição

00:01

Olá pessoal, tudo bem?

00:03

No vídeo anterior a gente viu como enviar traces

00:05

para ferramentas diferentes usando o OpenTelemetry como base.

00:09

O ponto principal foi separar a instrumentação do destino.

00:13

A aplicação gera a telemetria com o padrão aberto e

00:17

depois essa telemetria pode ir para um LangFuse,

00:20

um Jaeger ou qualquer outro backend compatível.

00:23

Agora a gente precisa falar sobre um cuidado

00:26

que é tão importante quanto instrumentar.

00:30

que é decidir o que não deve ser enviado.

00:34

Esse é um ponto ali fundamental em aplicações com IA,

00:38

porque a telemetria pode carregar muito mais informação do que parece.

00:43

Em uma aplicação tradicional, um log mal feito já pode vazar dados sensíveis.

00:48

Numa aplicação com IA, esse risco aumenta,

00:52

porque o prompt pode conter dados do usuário.

00:55

Um contexto de reg pode conter documentos internos. O retorno de uma ferramenta,

01:01

por exemplo, pode trazer informações mega privadas.

01:04

E a resposta do modelo pode conter dados

01:08

que não deveriam ficar disponíveis numa ferramenta de observabilidade.

01:13

Então, a primeira regra é simples.

01:16

Observabilidade não significa capturar tudo.

01:19

A gente quer conseguir investigar o sistema,

01:22

mas sem transformar a ferramenta de observabilidade

01:25

numa cópia paralela dos dados sensíveis da aplicação.

01:30

No nosso projeto, por exemplo,

01:31

a instrumentação registra informações como request ID, feature, tenant, produto,

01:38

tempos, contagens, filtros, uso de tokens e modelo.

01:43

Isso é útil para investigar o comportamento do pipeline.

01:46

Mas a gente evita enviar... Pergunta completa, prompt completo,

01:52

chunks completos, documentos completos e a resposta completa,

01:57

incluindo o API Key ou a URL do banco.

01:59

Essa separação é intencional.

02:02

O que a gente quer mandar para a observabilidade são sinais seguros.

02:09

Contagens, flags, nomes de etapas, tempo de execução,

02:12

modelo usado, quantidade de tokens, quantidade de chunks,

02:16

e se a gente realmente teve resposta, ou se a gente teve um recurso na resposta,

02:24

ou se a gente teve um erro, por exemplo.

02:26

O que a gente não quer mandar sem uma decisão explícita é conteúdo bruto.

02:32

Então, isso nos leva a outro conceito importante, que é a cardinalidade.

02:37

Cardinalidade, nesse contexto,

02:39

é a quantidade de valores diferentes que um atributo pode ter. Por exemplo,

02:45

feature é igual a regchat. Ela tem baixa cardinalidade,

02:50

porque provavelmente existem poucas features.

02:54

Model, por exemplo, GPT-4.1 mini,

02:57

também tende a ter baixa cardinalidade. Agora,

03:02

se você coloca a pergunta inteira do usuário como um atributo de span,

03:06

cada pergunta pode ser um valor diferente no final das contas.

03:11

Então isso explode essa cardinalidade.

03:14

A alta cardinalidade dificulta consultas, aumenta o custo,

03:20

polui bastante os dashboards e pode prejudicar.

03:23

O back-end de fazer realmente a observabilidade.

03:27

Além disso, no caso de A,

03:29

atributos de alta cardinalidade frequentemente carregam dados sensíveis.

03:35

Uma pergunta do usuário, e-mail, nome,

03:38

o prompt completo, resposta completa, conteúdo do chunk,

03:42

e tudo isso pode gerar ali problema. Então,

03:45

uma boa prática é usar atributos estáveis e controlados.

03:50

Em vez de registrar a pergunta inteira, registre o tamanho da pergunta ou um hash,

03:55

se fizer sentido, por exemplo. Em vez de registrar o chunk inteiro,

03:59

registre o chunk ID.

04:01

O arquivo de origem... E, por exemplo,

04:05

a quantidade de chunks, você também, nesses casos,

04:07

você pode registrar. Em vez de registrar um prompt completo, você pode fazer o quê?

04:13

Registre a versão do prompt. Então, em vez de registrar uma resposta inteira,

04:17

registre se teve resposta ou se ela foi recusada e quantos tokens foram gerados. E agora,

04:24

a gente entra num outro ponto, que é o de sampling. Eu tinha comentado isso. Então,

04:29

sampling é decidir... Quais execuções serão armazenadas ou exportadas?

04:36

Em desenvolvimento, talvez faça sentido capturar quase tudo.

04:40

Em produção, já talvez não.

04:42

Você pode capturar uma porcentagem dessas requisições normais,

04:46

mas guardar 100% dos erros pode guardar todas as respostas sem fonte,

04:51

todas as chamadas caras,

04:53

todos os timeouts ou todas as execuções que passaram de um limite de latência.

04:58

Então, isso é uma decisão.

05:00

Arquitetural, você não precisa tratar todas as requisições da mesma forma.

05:06

Uma execução bem-sucedida,

05:07

barata e rápida,

05:09

talvez não precise ser guardada com o mesmo nível de detalhe que uma execução lenta,

05:14

cara ou com erro. E por último, a gente tem a retenção.

05:19

Retenção é por quanto tempo esses dados vão ficar armazenados. Traces,

05:24

logs e eventos não deveriam ficar guardados para sempre, ali sem nenhum critério.

05:29

Quanto mais sensível o sistema, mais importante é definir o período de retenção,

05:34

controle de acesso e a política de limpeza.

05:38

Ambientes diferentes também podem ter políticas completamente diferentes.

05:43

Em desenvolvimento,

05:45

talvez o time aceite mais detalhes para fazer um debug ali.

05:49

Em staging, a gente já começa a se aproximar de produção.

05:53

Em produção, a política precisa ser muito mais restrita. Menos conteúdo bruto,

05:58

menos exposição, mais controle de acesso e mais cuidado com a retenção.

06:03

Então, a ideia principal dessa aula é uma boa arquitetura

06:07

de observabilidade não define apenas o que a gente vai capturar.

06:12

Ela define o que não capturar, quando capturar...

06:17

por quanto tempo a gente tem que guardar e quem vai poder acessar.

06:21

Então já no próximo vídeo a gente já vai levar um pouquinho isso mais pra prática. Vamos nessa!

## Resumo IA

[RESUMO_IA]