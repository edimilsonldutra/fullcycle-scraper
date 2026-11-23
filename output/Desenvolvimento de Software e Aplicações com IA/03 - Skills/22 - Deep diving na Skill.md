Módulo: Desenvolvimento de Software e Aplicações com IA\
Aula: [Introdução e conceitos iniciais](https://plataforma.fullcycle.com.br/courses/a091b0fe-a5c6-4287-a3d3-1ec61defcfd3/430/224/283/conteudos?capitulo=283&conteudo=17550)

## Resumo da aula

Uma skill de setup para Next.js concentra, no skill.md, as regras operacionais necessárias para criar e preparar um projeto em ambientes variados. Retomando o uso de front matter, keywords e Progressive Disclosure já estabelecido, o ponto novo aqui é a skill atuar como um guia executável de setup, não apenas como documentação. Ela define quando agir, o que perguntar antes de agir e quais referências consultar para completar a configuração. Isso reduz improviso do agente e torna o bootstrap do projeto repetível.

Nem toda automação deve ser disparada imediatamente. A skill pode impor a regra de não executar nada sem antes perguntar ao usuário o que ele quer fazer e inferir o escopo do projeto a partir dessas respostas iniciais. Essa etapa evita criar estrutura, instalar dependências ou assumir autenticação, banco e testes sem confirmação. O resultado é uma automação guiada por intenção, não por suposição.

O arquivo assets/env.example funciona como um template base que substitui o padrão genérico gerado pelo framework quando o projeto exige convenções próprias. Em vez de depender apenas do que o Next.js cria por padrão, a skill injeta variáveis mínimas como SERVER_PORT e PORT_RANGE, além de campos adicionais quando há autenticação ou banco de dados. Isso padroniza o ambiente desde o início e evita divergência entre projetos. A regra complementar é manter .env e .env.local fora do versionamento e nunca comitar env.local.

Alguns trechos do setup só fazem sentido quando certos recursos foram escolhidos. Se o projeto usar autenticação, a skill passa a prover variáveis como NEXTAUTH_SECRET e URL; se houver banco com Prisma, entram verificações específicas desse cenário. Esse modelo de decisão condicional reaproveita a organização por contexto já discutida anteriormente, mas aqui aplicada ao bootstrap do projeto. O ganho é não poluir o setup com instruções irrelevantes para projetos menores.

Os scripts init, down e check, já referenciados em aulas anteriores, aparecem aqui como artefatos concretos distribuídos pela própria skill via pasta assets. O ponto central não é redefinir esses scripts, mas formalizar que todo projeto deve recebê-los no diretório correto e obedecer ao comportamento esperado. init precisa ser idempotente, ou seja, rodá-lo duas vezes não deve duplicar efeitos nem quebrar o ambiente; down deve encerrar processos; check participa da validação do setup. Assim, a skill deixa de só instruir e passa a entregar os componentes operacionais.

Uma skill de setup confiável não termina na cópia de arquivos. Ela também explicita um checklist para confirmar que o ambiente realmente foi preparado e distingue o que é obrigatório do que é opcional, como testes, autenticação ou Prisma. Essa separação impede falsos positivos: um projeto sem autenticação não deve falhar por ausência de variáveis desse módulo. A validação passa a refletir o escopo real escolhido no início.

Retomando a diferença entre cloud.md e skills, a skill aqui assume a responsabilidade de manter o cloud.md alinhado ao estado atual do projeto. Sempre que scripts são adicionados, pacotes são instalados ou novas convenções entram em uso, o cloud.md precisa ser atualizado para refletir essas diretivas. Os padrões de referência incluem overview do projeto, ambiente, stack, estrutura, testes, banco, worktrees e regras. Isso transforma o cloud.md em documentação operacional sincronizada com a automação.

Além do skill.md, a skill pode apontar para arquivos de referência com estruturas mínimas de projetos Next.js, organização de componentes e uso de rotas dinâmicas. Essas referências não executam ações por si só; elas servem como base para o agente escolher uma organização coerente com o que o usuário pediu. O valor está em reduzir ambiguidade arquitetural no momento da criação. Em vez de inventar uma estrutura, o agente deriva a decisão de padrões previamente aprovados.

A pasta scripts/verify-scripts adiciona uma camada objetiva de conferência após a execução do setup. Esse shell script verifica se arquivos como .init, .down, .check e cloud.md foram realmente criados ou copiados, confirmando que a skill cumpriu seu contrato. Se algo estiver faltando, o erro volta para a IA, que pode tentar corrigir o problema. A skill, portanto, não apenas orienta e executa: ela também audita o próprio resultado.

O valor real dessa abordagem aparece quando o projeto precisa rodar em ambientes com restrições severas, como sandboxes sem Docker ou sem acesso a Postgres. Nesses casos, decisões que funcionam localmente podem precisar ser substituídas por alternativas como PGLite. A skill encapsula essas adaptações para que o agente não trate todos os ambientes como equivalentes. Customizar o projeto para a realidade operacional do agente aumenta a chance de execução bem-sucedida e reduz retrabalho.

## Transcrição

[TRANSCRIÇÃO]

## Resumo IA

[RESUMO_IA]