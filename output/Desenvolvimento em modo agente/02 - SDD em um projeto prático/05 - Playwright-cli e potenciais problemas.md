Módulo: Desenvolvimento em modo agente\
Aula: [Introdução a SDD](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/288/conteudos?capitulo=288&conteudo=17783)

## Resumo da aula

Playwright CLI é uma forma de operar o ecossistema Playwright com foco em agentes de IA que trabalham por linha de comando e skills, em vez de depender principalmente de MCP. Retomando o uso de Playwright para validação automatizada, a diferença nova aqui está no modo de integração com o agente: o CLI tende a oferecer um fluxo mais direto e, na prática, mais veloz para certos cenários. Isso não torna o MCP irrelevante; apenas muda o canal de controle do navegador e a ergonomia do trabalho automatizado.

O Playwright CLI pode rodar em Headless Mode, o que elimina a necessidade de manter o navegador visível na tela durante a automação. Esse modo é útil quando o objetivo é velocidade, menor interferência no ambiente local e execução mais próxima de pipelines automatizados. Quando necessário, o navegador também pode ser aberto de forma visível para inspeção do que o agente está fazendo, o que ajuda a depurar navegação, interações e falhas de teste.

No ambiente Cloud Desktop, o preview da aplicação em desenvolvimento funciona como apoio visual para acompanhar o resultado do trabalho do agente. A ideia central não é substituir o Playwright, mas complementar a observação do estado atual da interface enquanto a automação acontece. O mesmo padrão geral se aplica ao Codex quando a skill correspondente já está instalada, porque o agente passa a ter acesso ao mesmo tipo de capacidade operacional.

A instalação do Playwright CLI exige atenção porque modelos frequentemente confundem o pacote com o Playwright padrão. Pedir “instale o Playwright CLI” nem sempre basta: o agente pode executar a instalação do pacote errado se a instrução não estiver precisa. O ponto crítico é explicitar o sufixo do pacote CLI na instalação, em vez de usar apenas a referência genérica ao Playwright tradicional.

Depois da instalação do Playwright CLI, o comando playwright-cli install --skills adiciona ao ambiente a skill que permite ao agente usar esse canal de automação. Essa skill funciona como a camada de capacidades operacionais que expõe navegação, interação e recursos de teste ao agente. Sem ela, o CLI pode estar presente no sistema, mas o fluxo orientado por skill fica incompleto.

A skill do Playwright CLI reúne referências e operações como geração de testes, storage state, tracing, video recording, navegação, uso de teclado e mouse, manipulação de abas, acesso a network, dev tools e snapshots. Isso amplia o escopo do agente além de simplesmente abrir páginas, porque ele passa a inspecionar comportamento, registrar execução e produzir artefatos úteis para diagnóstico. Em cenários de desenvolvimento assistido por agente, essa superfície de comandos torna a validação mais rica e mais automatizável.

Quando o agente devolve um sumário com etapas executadas, testes rodados e instruções para subir o ambiente local, ele está condensando o que acredita ter feito e como validar o resultado. Um exemplo típico inclui subir dependências com docker compose, copiar variáveis de ambiente, rodar migrações, iniciar a aplicação e executar testes. Esse tipo de saída é útil, mas também é um ponto de atenção: se o guidance estiver fraco, o agente pode produzir passos plausíveis e ainda assim desalinhados com o fluxo correto do projeto.

Guidance insuficiente gera um comportamento recorrente em agentes: eles completam lacunas com suposições razoáveis, mas potencialmente erradas. No contexto do Playwright CLI, isso aparece tanto na instalação incorreta do pacote quanto na geração de instruções de execução local que parecem corretas à primeira vista. A consequência prática é que velocidade sem precisão aumenta o risco de automação enganosa, exigindo prompts mais específicos e validação cuidadosa do que foi realmente configurado e executado.

## Transcrição

00:00

Bom, pessoal, enquanto o Claudio está desenvolvendo as coisas aqui para a gente,

00:05

o que acontece?

00:06

Eu quero falar rapidamente do Playwright CLI.

00:11

O que acontece é o seguinte, nós temos o projeto Playwright.

00:15

O Playwright possibilita que um navegador seja aberto e fazer com que,

00:21

através de MCPs, que é a forma mais utilizada,

00:25

você consiga navegar na página e tudo mais. Porém,

00:29

existe... Um projeto chamado Playwright-CLI. Esse projeto,

00:35

o Playwright-CLI, ele foi feito focado mais para quê?

00:40

Para trabalhar com agentes de A,

00:44

usando CLI e

00:49

com skills ao invés de usar o MCP.

00:53

Usar MCP é super relevante,

00:57

é importante, tem diversas formas que...

01:00

O agente consegue interagir. Mas, pra velocidade,

01:04

entendeu? E a forma de como trabalhar com o Playwright,

01:08

usar o Playwright CLI, pelo menos pra mim, tá sendo algo, assim, muito,

01:13

mas muito mais bacana, tá? Então, de forma geral,

01:16

eu hoje estou usando muito mais o Playwright CLI do que o Playwright MCP.

01:22

Tanto o Playwright normal, né? com o Playwright CLI,

01:26

você pode rodar ele em Headless Mode, ou seja,

01:28

ele não precisa ficar abrindo o navegador na tela do seu computador,

01:32

ele abre como um processo,

01:33

mas se você quiser, você pode pedir para ele abrir o navegador,

01:36

daí você vê o que ele está trabalhando.

01:38

Eu também, depois eu vou mostrar para vocês, no caso do Cloud, tá?

01:44

Ele tem a aplicação do Cloud Desktop,

01:47

onde você pode trabalhar por lá, e lá ele tem um preview.

01:53

do que ele está sendo desenvolvido, onde ele gera um arquivo pontuante, tá?

01:57

Tem o Codex também, que o comportamento dele, nesse caso,

02:01

vai ser basicamente o mesmo, uma vez que você tem skill instalada, tá?

02:05

Como é que funciona essa skill aqui?

02:08

Uma coisa que você tem que tomar cuidado é que gera muita

02:11

confusão na hora que você pede para instalar o Playwright CLI,

02:14

porque normalmente quando a gente vai instalar o Playwright,

02:17

a gente coloca npm install -g Playwright,

02:22

barra latest ou alguma coisa desse tipo,

02:24

mas nesse caso tem que ter o barra CLI arroba latest.

02:28

Por que que eu tô dando e falando esse detalhe aqui pra você,

02:31

galera? Eu tô falando isso porque grande parte dos modelos,

02:35

quando você pede pra instalar,

02:37

mesmo que você fale instale o Playwright CLI,

02:40

ele vai lá e instala o Playwright normal. Aconteceu comigo um monte de vezes,

02:45

então só tô dando esse detalhe aqui. E junto...

02:48

com o Playwright CLI, quando você pede para ele instalar,

02:52

você pode dar um, depois que você instalou,

02:54

você pode dar um Playwright CLI install --skills.

02:58

Quando você faz isso, ele vai instalar a skill no seu computador,

03:02

de forma que você pode utilizar. E uma vez que você tem essa skill,

03:07

essa skill faz com que o agente consiga utilizar o Playwright CLI para testar.

03:14

A sua aplicação,

03:16

Tá? Então, é basicamente isso que acaba acontecendo, tá?

03:21

Então, a skill dele tá aqui, ó.

03:24

Cadê? Eu estava na skill agora há pouco.

03:26

As skills, Playwright, CLI. Então, aqui tem as referências,

03:30

O código, geração de teste, storage state, tracing,

03:34

video recording, ele tem bastante opções, né?

03:38

E tem a skill principal que fala do que é capaz de fazer,

03:42

Quais são os principais comandos, navegação, keyboard, mouse,

03:45

Save, tabs, storage, né? Como que ele vê network, dev tools,

03:49

Então, ele consegue pegar todas as opções do browser,

03:51

Snapshots, então, ele tem bastante coisa e gera as referências ali pra gente,

03:56

Tá? Então, essa é uma skill super útil,

03:58

Eu tenho, e vocês viram essa skill.

04:02

Sendo utilizada ali, por baixo dos panos, obviamente,

04:06

Mas eu acredito que deva ter ficado agora um pouquinho mais claro.

04:12

Eu não quero ficar focando nesse detalhe,

04:15

Especificamente do Playwright,

04:16

Porque a gente vai ter bastante para falar na parte de Harness Engineer. Legal?

04:20

Vamos ver aqui o nosso Cloud,

04:23

Que às vezes com o zoom ele dá essas paradas.

04:28

Então, ele fez aqui.

04:31

Sumário, ele rodou a fundação, fez o estágio 2, primitivos,

04:35

Actions, routes, estágios, testes, ele rodou os testes,

04:40

Fez os testes de integração e etc. E blá blá blá, para rodar localmente,

04:44

Você tem que usar o Docker Compose app -depostgres,

04:48

Copiar o .env para .env.local, rodar a migração,

04:53

Rodar o npm run dev e rodar o npm test. Aqui eu já começo a ficar...

05:00

Preocupado e por isso que às vezes falta de guidance acaba gerando um problema.

05:05

Eu vou falar com vocês sobre isso.

05:09

Logo em seguida, eu vou parar esse vídeo pra ele não

05:11

Ficar grande e daí eu vou mostrar um comportamento que é muito,

05:18

Mas muito comum da IA quando a gente tá trabalhando dessa forma, tá? Vamos nessa.

## Resumo IA

**Abreviações**
*   **CLI**: Command Line Interface
*   **IA**: Inteligência Artificial

**Resumo**
A aula aborda o Playwright CLI como uma alternativa para operar o ecossistema Playwright, focada em agentes de Inteligência Artificial (IA) que trabalham por linha de comando e "skills", diferenciando-se da dependência principal de MCPs. O objetivo é proporcionar um fluxo mais direto e veloz para a validação automatizada, sem, contudo, tornar o MCP irrelevante.

O Playwright CLI pode ser executado em Headless Mode, ideal para velocidade, menor interferência local e integração em pipelines automatizados, pois elimina a exibição do navegador. No entanto, o navegador pode ser exibido para inspeção e depuração das ações do agente. No ambiente Cloud Desktop, a aplicação em desenvolvimento oferece um preview visual que complementa a observação do trabalho do agente, um padrão que se aplica também ao Codex quando a skill correspondente está instalada.

O fluxo de uso envolve:
1.  **Instalação**: Requer atenção para instalar o pacote `Playwright-CLI` (ex: `npm install -g Playwright-CLI@latest`), pois agentes de IA frequentemente confundem com o Playwright padrão se a instrução não for precisa.
2.  **Instalação da Skill**: Após o CLI estar instalado, o comando `playwright-cli install --skills` é necessário para adicionar ao ambiente a capacidade operacional que permite ao agente utilizar o canal de automação.
3.  **Capacidades da Skill**: A skill do Playwright CLI abrange funcionalidades como geração de testes, storage state, tracing, gravação de vídeo, navegação, uso de teclado e mouse, manipulação de abas, acesso a network e dev tools, além de snapshots. Isso permite que o agente não apenas abra páginas, mas inspecione comportamentos, registre execuções e produza artefatos para diagnóstico.
4.  **Sumário do Agente**: O agente entrega um sumário das etapas executadas, testes rodados e instruções para subir o ambiente local (ex: Docker Compose, cópia de `.env`, migrações, `npm run dev`, `npm test`).

**Pontos de atenção**
*   **Instalação Precisa**: Modelos de IA frequentemente confundem o pacote Playwright CLI com o Playwright padrão. É crucial explicitar o sufixo do pacote (`Playwright-CLI`) durante a instalação para evitar o erro.
*   **Skill do Playwright CLI é Essencial**: A instalação do Playwright CLI por si só não basta. A skill deve ser adicionada explicitamente com `playwright-cli install --skills` para que o agente tenha acesso às capacidades operacionais completas.
*   **Impacto de Guidance Insuficiente**: A falta de orientação clara (guidance) faz com que agentes de IA preencham lacunas com suposições razoáveis, mas potencialmente incorretas. Isso se manifesta tanto na instalação do pacote errado quanto na geração de instruções de execução local que, embora plausíveis, podem estar desalinhadas com o fluxo correto do projeto.
*   **Validação Cuidadosa do Output do Agente**: A velocidade proporcionada pela automação pode ser enganosa se não houver precisão. É fundamental validar cuidadosamente o sumário e as instruções fornecidas pelo agente (ex: passos para subir o ambiente local) para garantir que o que foi configurado e executado está correto.
*   **Escolha do Modo de Execução**: Use o Headless Mode para velocidade e integração em pipelines automatizados. Mantenha o navegador visível para depuração e inspeção do trabalho do agente quando necessário.