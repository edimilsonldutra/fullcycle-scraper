Módulo: Protocolos de Comunicação\
Aula: [LAB: Deploy e Gateway parte 3](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18611)

## Resumo da aula

Falha de deploy nem sempre vem de lógica de negócio; às vezes o problema é operacional e banal. Editar o código dentro do diretório de gabarito, em vez do src, faz a aplicação subir sem incorporar a mudança esperada, o que produz um diagnóstico enganoso: parece que o código “não funciona”, quando na verdade o artefato executado nunca foi alterado. A correção consiste em aplicar a mudança no diretório que realmente participa do build e subir novamente os serviços. Esse tipo de erro importa porque, em produção, troubleshooting começa confirmando se o binário ou container executado corresponde ao código que se pretendia testar.

Retomando o cenário do reembolso, a validação começa forçando uma execução real da operação, aqui com um pedido 2 no valor de 50 reais. A resposta ao cliente informa apenas que houve erro ao calcular o bônus e que parece existir um problema técnico. Essa resposta é um erro controlado: ela confirma a falha funcional sem expor linha de código, exceção interna ou detalhes de implementação. O objetivo é preservar a experiência e a segurança do cliente enquanto a investigação acontece na camada de observabilidade.

O ponto de entrada para diagnóstico é o menu Explore do Grafana, usando o Tempo como fonte de dados de tracing. Se o Tempo não estiver selecionado por padrão, ele precisa ser escolhido manualmente antes da busca; sem isso, a consulta vai para a fonte errada e o trace não aparece. Na aba Search, a busca é refinada pelo identificador do serviço e pelo status Error, o que reduz o volume de spans e leva direto às execuções com falha. Esse filtro é valioso porque transforma tracing em ferramenta operacional de triagem, não apenas em telemetria passiva.

Depois de localizar o horário compatível com a tentativa de reembolso, o próximo passo é abrir o span correspondente e inspecionar seus atributos. O trace mostra que a falha ocorreu dentro de emitir_reembolso_bonificado e registra uma exception do tipo boom. O valor prático está no exception stack trace, que aponta a linha exata e o ponto do fluxo onde a exceção foi lançada. Diagnóstico operacional é isso: sair de um sintoma genérico no cliente e chegar, em segundos, à causa técnica acionável pela engenharia.

A arquitetura separa deliberadamente duas visões do mesmo incidente. O cliente recebe uma mensagem limpa e limitada, suficiente para saber que a operação falhou, mas insuficiente para revelar código sensível, nomes internos ou estrutura do backend. Já a engenharia acessa o trace completo no Grafana, com exception e stack trace detalhados. Essa divisão reduz vazamento de informação na borda sem sacrificar velocidade de correção no ambiente operacional.

Retomando o mesmo ambiente, pedir “listar usuários do sistema” valida outra propriedade: a IA não enxerga tudo o que o backend poderia teoricamente oferecer. A resposta informa que não há ferramenta disponível para essa ação e restringe as capacidades visíveis ao reembolso bonificado, coerente com a allowlist já definida anteriormente no gateway. Esse comportamento demonstra isolamento de borda: a limitação é aplicada antes que a solicitação vire acesso efetivo a uma capacidade interna. Em produção, isso contém exposição acidental e reduz o espaço de ação do agente mesmo quando ele tenta uma operação fora do catálogo publicado.

A combinação final é simples e forte: erro controlado para fora, rastreabilidade profunda para dentro e superfície de tools limitada na borda. Quando uma falha ocorre, o cliente não recebe detalhes internos; quando a engenharia investiga, encontra a causa exata no tracing; quando a IA tenta sair do escopo, o gateway bloqueia pela exposição declarada. Essa composição é uma evidência prática de operação segura em produção, porque protege o consumidor, acelera correção e mantém o backend menos exposto.

## Transcrição

00:01

Opa, pessoal. O que aconteceu?

00:05

Foi simples quanto o seguinte. Você sabe, obviamente, você sabe,

00:09

né? Eu tenho dentro do meu... Nas pastinhas,

00:14

eu tenho o gabarito, né? Que é a resposta final.

00:17

E olha onde é que eu estava colocando o código. Opa.

00:27

Onde é que eu estava colocando o código?

00:29

Dentro do gabarito, tá? Óbvio, nunca ia funcionar. Beleza? Então,

00:34

o que eu fiz? obviamente fui para o lugar certo,

00:39

mudei dentro do source que é onde que sobe onde

00:43

que o nosso código sobe de fato tá e subir

00:48

de novo o doc e o stringlit tá e com

00:51

isso vamos lá eu vou pedir agora ó emita um reembolso

00:58

reembolso para para

01:03

opa o pedido 2 no valor 50 reais.

01:21

Ao tentar emitir o reembolso, o valor do bônus do sistema retornou um erro.

01:26

Parece um problema técnico. Então, de novo, olha só. Agora,

01:33

o que a gente vai fazer? Beleza, a gente viu que deu problema.

01:36

Agora, vamos abrir o Grafana, pessoal? Cara, o Grafana é muito legal.

01:42

Grafana é muito legal. Vamos abrir o Grafana.

01:47

E vamos lá, pessoal. Eu vou navegar aqui junto com vocês, tá?

01:54

No menu lateral esquerdo, a gente vai clicar em Explore,

01:57

tá? Então, vamos aqui, cara. Vamos aqui.

02:00

Vamos clicar em Explore.

02:03

Deixa eu mostrar o menu, né? Ficar mostrando o menu. Vamos clicar em Explore.

02:07

E aqui nós vamos escolher... Aqui não vai estar o tempo por default,

02:12

tá? Vocês vão colocar o tempo aqui por default.

02:14

E a gente vai pedir para atualizar. Então, beleza.

02:19

E na aba Search, pessoal, a gente vai colocar MCP 7. Vamos aqui no Search.

02:26

Opa, na aba Search, nós vamos colocar o 7, é o MCP 7.

02:31

E o status, a gente vai pôr de Error.

02:34

Beleza? E vamos atualizar. Olha só. Então, vamos lá.

02:41

Vamos ver o horário. 15h27,

02:44

15h26. Esse cara aqui.

02:46

Então, se a gente ver aqui, pessoal,

02:48

a gente vai ver que existe um... Vamos clicar aqui nele.

02:52

E vamos ver o que ele está falando aqui.

02:56

Olha só que legal. Aqui está falando o seguinte.

02:59

Que deu o erro ao emitir reembolso.

03:03

O evento é uma exception.

03:05

Do tipo boom.

03:08

Beleza? Então, olha que legal, pessoal.

03:10

Isso aqui é observabilidade. Isso aqui é um tracing.

03:17

Então, de novo, pessoal, olha só.

03:19

Aqui está indicando que o erro ocorreu exatamente

03:21

dentro do processo emitir reembolso bonificado,

03:25

tá? E melhor, como vocês podem ver, pessoal,

03:28

aqui, o exception stack trace, tá?

03:35

Aqui do lado, ele vai mostrar tudo bonitinho, pessoal. Olha aqui, ó.

03:39

Ele vai falar exatamente onde que foi, qual foi a linha e tudo mais, tá?

03:43

Ou seja, a raiz do bug catastrófico foi descoberta em segundos,

03:47

Não em horas. Ou seja, no Streamlit,

03:50

Agora vamos fazer um outro teste. Vamos colocar lá, pessoal,

03:57

Liste o nome dos usuários. Vamos ver aqui.

04:03

Listar usuários do sistema.

04:08

Vamos ver o que vai responder.

04:11

Olha só que legal, pessoal. Olha só.

04:15

Ele vai falar que a ferramenta disponível que tem é esse cara aqui.

04:20

Ou seja, ele falou o seguinte. Olha, pessoal, desculpa,

04:27

Mas eu não tenho acesso a uma ferramenta para listar os usuários do sistema.

04:30

Então, as ferramentas disponíveis no DocMCP que têm

04:34

Acesso são limitadas a emitir reembolso.

04:36

E permite emitir o reembolso com bônus financeiro. Agora, vamos lá.

04:43

Está grande lição de arquitetura esse laboratório. Na nossa borda de ar,

04:47

Nós protegemos o cliente, que é a LLM,

04:49

De ver os detalhes internos quando um erro acontece.

04:52

O Streamlit recebe apenas a falha limpa,

04:55

Sem vazar código sensível. Mas, simultaneamente,

04:58

Nós usamos observabilidade no Grafana para registrar o nível

05:01

De detalhes cirúrgicos com os TechTrace completos.

05:04

A gente garante que a equipe de engenharia conserte o problema rápido.

05:08

Ou seja, isolamento de borda e visibilidade total por trás dela,

05:11

Pessoal. Isso aqui é engenharia de produção, tá? Até mais.

## Resumo IA

[RESUMO_IA]