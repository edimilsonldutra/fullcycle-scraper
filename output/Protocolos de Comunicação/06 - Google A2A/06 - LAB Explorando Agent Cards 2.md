Módulo: Protocolos de Comunicação\
Aula: [LAB: Explorando Agent Cards 2](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/296/conteudos?capitulo=296&conteudo=18618)

## Resumo da aula

A descoberta automática fica visível quando a interface encontra os agentes sem configuração manual adicional e passa a exibir suas capacidades publicadas. Retomando o laboratório anterior, o Agent Card e as skills já definem o contrato; a novidade aqui é confirmar visualmente que o aplicativo realmente consumiu esse contrato. Se o agente logístico aparece na interface com a skill rastrear-pedido, a cadeia de descoberta está funcionando de ponta a ponta: publicação correta, leitura pelo cliente e renderização para o usuário.

Exibir a skill na interface não é um detalhe cosmético, porque isso prova que a capacidade publicada pelo agente está acessível ao consumidor real. Quando rastrear-pedido aparece no Streamlit, o cliente deixa de depender de suposições sobre o servidor e passa a operar sobre o contrato descoberto. Se a skill não aparecer, o problema tende a estar na publicação do card, na rota esperada pelo cliente ou na leitura feita pela aplicação.

O cenário combina dois domínios especialistas: logística para consultar o status de um pedido e estoque para consultar a disponibilidade de um SKU. Essa separação importa porque mostra a composição horizontal entre agentes distintos, cada um responsável pelo próprio escopo. Em vez de concentrar tudo em um único serviço genérico, a interface prepara uma consulta que pode ser decomposta conforme as skills descobertas.

A pergunta sobre o pedido 123 e o SKU 9988 funciona como um teste de integração orientado por uso real. Ela força a aplicação a sair da etapa de descoberta e avançar para uma intenção que envolve mais de um agente no mesmo fluxo. O valor principal não está na resposta final ainda, mas em verificar que a interface já reconhece os especialistas corretos antes da execução da consulta composta.

O comportamento esperado é simples: a interface lista os agentes descobertos, mostra as skills correspondentes e aceita uma consulta que mistura logística e estoque. Quando isso acontece, a camada visual confirma que a descoberta automática está operacional e pronta para a próxima etapa de orquestração. Se algum agente não aparecer, a primeira verificação deve recair sobre a disponibilidade do serviço, a publicação correta do Agent Card e a presença da skill esperada no contrato.

## Transcrição

00:00

Pessoal, voltando aqui, vamos aqui no servidor, tá? No Streamlit.

00:05

Então, vamos lá. Então, vão pedir pro laboratório, tá?

00:11

Pro aplicativo achar os agentes, tá?

00:17

E que skills que eles têm, tá? Vamos lá.

00:21

Então, o sistema descobriu sozinho, ó. Então,

00:24

descobriu aqui o agente logístico online,

00:27

tá? Que tem lá o skill que a gente criou lá, ó.

00:31

Opa, opa, cadê o skill?

00:34

Aqui, skill, olha lá. Aqui é o rastrear pedido, tá?

00:39

E agora, pessoal, vamos lá.

00:43

Então, vamos fazer o seguinte. Vamos pedir aqui, ó.

00:47

Qual o status do pedido 1, 2, 3 e do estoque SKU 9988?

00:52

Vamos aqui, ó. Qual o status do pedido 1,

00:56

2, 3 e o estoque do SKU 9988?

## Resumo IA

[RESUMO_IA]