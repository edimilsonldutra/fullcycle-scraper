Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17892)

## Resumo da aula

Verificação funcional em nível de browser complementa os testes em código porque valida o comportamento real da aplicação durante a navegação. Um teste unitário ou mesmo parte dos testes automatizados tradicionais pode passar enquanto a interface apresenta regressões, especialmente em front-end. Ferramentas como Playwright e Puppeteer executam esse papel ao interagir com a aplicação como um usuário faria. Isso adiciona uma camada de segurança importante quando o sistema cresce e as mudanças começam a afetar partes aparentemente desconectadas.

À medida que a aplicação evolui, alterações locais podem quebrar fluxos em outras áreas sem que isso apareça nos testes de baixo nível. Esse risco é particularmente relevante em front-end, onde nem todo problema é capturado ao testar componentes isoladamente em código. Verificar features e pontos principais do sistema por navegação expõe falhas de integração, renderização e fluxo de uso. O objetivo não é substituir testes anteriores, mas cobrir o que só aparece na execução funcional completa.

Retomando a ideia de artefatos e estado já estabelecida, a verificação funcional precisa cumprir um contrato explícito entre execução e avaliação. Não basta instruir um agente a “navegar e ver se está tudo funcionando”, porque isso produz uma checagem vaga, difícil de reproduzir e de auditar. O contrato define tudo o que deve ser testado para considerar uma feature pronta. Com isso, desenvolvimento e validação passam a operar sobre a mesma definição de pronto.

O contrato só funciona quando quem implementa sabe que está construindo para aqueles critérios e quem valida sabe que deve testar exatamente os mesmos pontos. Esse alinhamento evita lacunas em que uma feature parece concluída para um lado, mas ainda não satisfaz as expectativas do outro. Em Harness Engineering, isso transforma teste funcional em parte do processo, não em uma inspeção improvisada no final. A consequência prática é previsibilidade maior na aprovação e menos ambiguidade sobre o que significa “está pronto”.

Uma vez definido o contrato, o agente pode usar Playwright, Puppeteer ou ferramenta equivalente para executar a checklist prescrita. O valor da automação não está apenas em navegar, mas em navegar segundo um mapa de ações e verificações previamente definido. Se os itens do contrato passam, a feature atende ao critério funcional esperado. Sem esse mapa, a navegação automatizada vira exploração solta e perde força como mecanismo confiável de avaliação.

Retomando o foco em processo já discutido nas aulas irmãs, testes de engenharia não devem olhar apenas para uma feature isolada, mas para a consistência do sistema como um todo. Por isso, a pergunta central não é se já existe automação de browser, e sim se existe clareza estruturada sobre o que precisa ser validado. Mesmo em ambientes menos maduros, organizar verificações funcionais em contratos e mapas de teste já melhora a confiabilidade da entrega. A diferença está entre uma IA que sai navegando sem direção e uma avaliação funcional orientada por critérios explícitos.

## Transcrição

00:01

No vídeo anterior eu falei sobre critério de qualidade,

00:03

onde uma IA, por exemplo, pode dar uma nota.

00:07

Mas uma outra coisa que simplesmente nós temos

00:12

que fazer é verificação funcional em nível do browser,

00:17

não apenas em código. O que acontece muito,

00:20

muitos desenvolvedores acabam vendo simplesmente se o teste está passando,

00:26

se o código está funcionando e tudo mais,

00:28

mas na prática acaba não testando isso no browser.

00:32

E o grande ponto aí no meio da história é,

00:36

já existem diversas ferramentas, sei lá,

00:39

um Playwright da vida que consegue navegar na sua

00:42

aplicação e ver se as coisas estão funcionando. E sim,

00:46

você precisa ter esses tipos de testes funcionais. Ou seja,

00:51

conforme você vai desenvolvendo a aplicação,

00:54

a aplicação vai podendo ter regressões.

00:59

E aí a gente começa a entrar em aspectos importantes. Por que eu estou dizendo isso?

01:04

Porque imagina que você tem um sistema e esse sistema está ficando cada vez maior.

01:09

E a gente sabe que quando a gente está mexendo,

01:12

estou dando um exemplo agora de front-end, que conforme você mexe em uma coisa,

01:16

pode dar problema em outra.

01:17

E às vezes isso no front-end não vai ser pego em testes automatizados,

01:22

porque você não vai testar todo o componente do front-end em código.

01:26

Então, o que acontece? Quando você pede para a gente navegar,

01:29

verificar as features,

01:31

verificar se os pontos principais do sistema estão funcionando,

01:35

isso vai gerar um outro nível de teste e de

01:39

segurança na hora que você está desenvolvendo o trabalho. Agora,

01:42

o grande problema aí no meio da história, e é o que eu coloco,

01:45

é que muita gente já faz isso. Agora,

01:49

o problema não é esse. O ponto é que o... a gente,

01:54

vamos dizer, o processo de avaliação, ele tem que conseguir cumprir o contrato.

02:01

Não é simplesmente chegar e desenvolver uma feature e

02:04

falar navegue e veja se está tudo funcionando. Não.

02:07

Eu tenho, por exemplo,

02:09

um contrato onde do que eu espero que todo o meu software faça,

02:14

eu tenho um contrato de tudo que vai ter que

02:17

ser testado para garantir que aquela feature está pronta.

02:21

Uma vez que eu tenho esse contrato feito de

02:24

quem desenvolveu e daquele que está testando,

02:27

aí sim o meu agente vai,

02:29

pegar um Playwright ou qualquer outra ferramenta, um Puppeteer, não interessa,

02:32

e ele vai fazer aquela checklist exatamente da forma como está no contrato.

02:39

Se aquelas coisas passarem, está ok, entendeu? Então,

02:43

se hoje você já está testando com Playwrights,

02:46

se você está fazendo bastante coisas desse tipo, ótimo, tá? Agora,

02:50

o que você tem que pensar é que na hora que você está pensando em testes de engenharia,

02:53

você não está pensando em testar só uma feature ou só um pedacinho.

02:57

Você está pensando no processo como um todo.

02:59

E como um processo,

03:00

você sempre tem que lembrar e tem que ter muita clareza do que tem que ser testado.

03:05

Mas não apenas do que tem que ser testado.

03:08

Você tem que ter um combinado entre aquele cara que desenvolveu,

03:12

ele tem que saber que ele desenvolveu para aquele contrato.

03:16

E aquele cara que está testando,

03:19

ele tem que saber que ele vai ter que testar em cima daquele mesmo contrato.

03:23

E por isso que esses tipos de contrato são importantes.

03:26

E por isso que entender o que você está desenvolvendo, como as features se encaixam,

03:32

que esse é o grande problema na hora que você está desenvolvendo em paralelo e etc.,

03:37

é uma dificuldade grande. Então, pensem sempre num contrato.

03:43

E, independente hoje, se você já tem um ambiente...

03:47

extremamente maduro para desenvolver ou não,

03:49

repense em como você está fazendo as verificações funcionais.

03:53

Se simplesmente a IA está saindo navegando ou se

03:57

você tem uma forma muito mais organizada

03:59

de gerar um mapa onde ela tem que fazer

04:01

determinadas ações para garantir que tudo está funcionando. Fechou?

## Resumo IA

**Resumo**
A aula aborda a importância da verificação funcional em nível de browser como um complemento essencial aos testes em código. O objetivo principal é validar o comportamento real da aplicação durante a navegação, especialmente para identificar regressões e falhas de integração ou renderização que testes de baixo nível (como testes unitários ou de componentes isolados) podem não capturar, particularmente em ambientes de front-end. Ferramentas como Playwright e Puppeteer são mencionadas como agentes capazes de interagir com a aplicação como um usuário faria, adicionando uma camada de segurança vital à medida que o sistema cresce e as interdependências aumentam.

O fluxo explicado pelo instrutor enfatiza que, para que esses testes sejam eficazes, não basta instruir um agente a "navegar e ver se está tudo funcionando". É crucial definir um "contrato" explícito que especifique tudo o que deve ser testado para que uma feature seja considerada pronta. Esse contrato alinha o desenvolvimento e a validação, garantindo que o desenvolvedor construa para critérios específicos e que o validador teste exatamente os mesmos pontos. Uma vez definido o contrato, o agente de automação (Playwright, Puppeteer, etc.) executa uma checklist prescrita, e a passagem desses itens do contrato confirma que a feature atende aos critérios funcionais esperados. A automação, assim, se torna um mecanismo confiável de avaliação, focado na consistência do sistema como um todo e não apenas em features isoladas.

**Pontos de atenção**
*   **Armadilha**: Confiar exclusivamente em testes de código pode mascarar regressões e falhas de interface ou integração que só se manifestam na navegação real da aplicação, especialmente em front-end.
*   **Ponto Crítico**: Uma avaliação funcional vaga, sem critérios explícitos (ex: "navegar e ver se está tudo funcionando"), resulta em verificações difíceis de reproduzir e auditar.
*   **Boa Prática**: Implementar um "contrato" explícito que defina claramente o que deve ser testado para considerar uma feature pronta. Isso garante alinhamento entre quem desenvolve e quem valida.
*   **Ponto Crítico**: A falta de alinhamento no contrato pode levar a lacunas onde uma feature parece pronta para um lado, mas não satisfaz as expectativas do outro.
*   **Boa Prática**: Utilizar ferramentas de automação de browser (como Playwright ou Puppeteer) para executar a checklist definida no contrato, transformando a navegação automatizada em uma avaliação orientada por critérios.
*   **Armadilha**: A navegação automatizada sem um "mapa" de ações e verificações previamente definido torna-se uma "exploração solta" e perde sua força como mecanismo confiável de avaliação.
*   **Boa Prática**: Em testes de engenharia, focar na consistência do sistema como um todo, e não apenas em features isoladas, mantendo clareza estruturada sobre o que precisa ser validado.
*   **Boa Prática**: Mesmo em ambientes menos maduros, organizar as verificações funcionais em contratos e mapas de teste melhora significativamente a confiabilidade da entrega.