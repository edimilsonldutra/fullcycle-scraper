Módulo: Protocolos de Comunicação\
Aula: [SSE e Webhooks no A2A](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18622)

## Resumo da aula

Retomando o fluxo de Task já estabelecido, a novidade aqui é a observação simultânea de dois mecanismos de acompanhamento na mesma execução. O servidor envia push notifications por Webhook enquanto também produz stream chunks, sem conflito entre os dois canais. Isso permite acompanhar progresso operacional pelos logs e, ao mesmo tempo, receber texto incremental durante a geração da resposta. Em termos práticos, coexistência aqui significa que a Task continua única, mas sua visibilidade é distribuída por mais de um meio.

A leitura correta dos logs começa pelo payload com estado submitted, que confirma que a Task foi aceita e registrada pelo servidor. Em seguida aparece o estado working, sinalizando que a execução saiu da submissão e entrou em processamento. O ponto importante não é redefinir esses estados, mas reconhecer sua ordem no tráfego real para validar conformidade e diagnosticar onde uma execução parou. Quando essa sequência aparece nos logs, o acompanhamento assíncrono está funcionando de ponta a ponta.

O payload com artifacts marca a transição entre progresso operacional e entrega do resultado formal da Task. Nos logs, esse momento deve ser lido como evidência de que o servidor não apenas processou a solicitação, mas publicou a saída reutilizável no formato esperado pelo protocolo. Se o estado avançou, mas o artifact não apareceu, o problema não está mais na aceitação da Task e sim na etapa final de publicação do resultado. Essa distinção encurta bastante o troubleshooting.

A finalização aparece no log como task finished, acompanhada do conteúdo final já consolidado. Esse ponto encerra a leitura operacional da execução: houve submissão, trabalho em andamento, publicação de artifacts e término observável. Em uma inspeção E2E, esse fechamento é o que diferencia uma Task apenas ativa de uma Task realmente concluída. Sem esse evento terminal, o fluxo permanece incompleto mesmo que tenha havido atividade intermediária.

O envio de vários chunks não indica duplicação de Task, mas o uso de streaming para montar o texto incrementalmente, como já visto anteriormente com sendStreamingMessage. O que muda aqui é a interpretação conjunta: enquanto os chunks mostram a resposta sendo construída, os Webhooks registram mudanças de estado e publicação de resultado. Essa combinação melhora observabilidade porque separa claramente geração progressiva de texto e sinais formais do lifecycle. Quando ambos aparecem em paralelo, o comportamento esperado é exatamente esse volume maior de eventos no log.

## Transcrição

00:02

Pessoal, problemas resolvidos.

00:03

A vantagem é que quando vocês receberem o código dessa aula,

00:06

né? Vocês não passarão por eles.

00:09

Bem, então onde eu estava, né?

00:12

Vamos colocar aqui e ver o E2E com o WebHooks em ação, tá? Vamos ver aqui.

00:23

Vocês podem ver, ó. Primeiro mudou para o status de work,

00:26

agora recebeu. Então vamos ver o fluxo, ó.

00:29

Que legal. Muita

00:36

coisa, né? Mas olha só esse limite.

00:39

Nós checamos passivamente o nosso círculo de WebHooks, ó. Tem o payload.

00:43

Fala importância, aí

00:46

ele fica mandando os retornos, stream chunks, então

00:54

beleza, então olha só.

00:57

Agora recebemos a push notification do servidor ETA perfeitamente, vejam os logs,

01:03

o payload veio com o estado de task submitted,

01:05

depois task state work e por fim os artefatos, tá? Beleza?

01:13

Deixa eu ver

01:18

o artefato no final, artefato...

01:24

task finish e o conteúdo final está aqui, ó. Tá

01:31

vendo só que ele foi, ó, ele foi, tá vendo?

01:34

Ele também usou stream também, tá? Por isso que fica

01:37

enviando vários, tá vendo, para fazer o texto, tá? Beleza

01:42

Isso aí, pessoal.

## Resumo IA

[RESUMO_IA]