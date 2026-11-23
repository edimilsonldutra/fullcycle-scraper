# Engenharia de Software na Era da IA
### Guia Prático do Fundamento à Produção

> **Baseado no conteúdo integral do MBA em Engenharia de Software com IA (FullCycle — 10 módulos técnicos, 767 aulas).**
> Escrito para engenheiros de software, tech leads e arquitetos que querem dominar o ciclo completo — sem enrolação, sem hype e com foco em decisões técnicas que sustentam produção.

---

## Prefácio — Como Ler Este Livro

A mudança real trazida pela Inteligência Artificial à engenharia de software não é "digitar código mais rápido". É o deslocamento do gargalo: **gerar código ficou barato; especificar, arquitetar, validar, observar e operar com segurança virou o diferencial.**

Quem trata IA como um chat para gerar trechos soltos acumula dívida técnica em velocidade recorde. Quem trata IA como **componente arquitetural e motor de um workflow determinístico** multiplica qualidade, confiabilidade e throughput.

Este livro destila toda a trilha técnica do MBA em 10 capítulos progressivos, desenhados para funcionar tanto como **leitura sequencial** quanto como **manual de consulta rápida no dia a dia**.

### Mapa da Obra — Como os 10 Capítulos se Conectam

```mermaid
flowchart TD
    subgraph P1["Parte I — Fundamentos e Contexto"]
        C1["Cap. 1: Fundamentos de IA Generativa"]
        C2["Cap. 2: Engenharia de Prompts"]
        C3["Cap. 3: Design Docs e Documentação Viva"]
        C1 --> C2 --> C3
    end

    subgraph P2["Parte II — Fluxo de Desenvolvimento com Agentes"]
        C4["Cap. 4: Modo Agente (SDD e Harness)"]
        C5["Cap. 5: Dev de Software com IA (RPI, Rules, Testes)"]
        C6["Cap. 6: Agent Skills e Extensibilidade"]
        C4 --> C5 --> C6
    end

    subgraph P3["Parte III — Arquitetura, Sistemas Agênticos e Operação"]
        C7["Cap. 7: Arquitetura na Era da IA"]
        C8["Cap. 8: Desenvolvimento de Agentes (ADK)"]
        C9["Cap. 9: Protocolos (MCP e A2A)"]
        C10["Cap. 10: DevOps e SRE com IA"]
        C7 --> C8 --> C9 --> C10
    end

    C3 --> C4
    C6 --> C7
```

### Três trilhas rápidas conforme seu objetivo imediato

| Seu foco agora | Leia primeiro | Depois avance para |
| --- | --- | --- |
| **Aumentar produtividade e qualidade no código hoje** | Cap. 2 → Cap. 3 → Cap. 4 → Cap. 5 → Cap. 6 | Cap. 7 (Testes e Eval) |
| **Colocar aplicações com LLM/RAG em produção com segurança** | Cap. 1 → Cap. 2 → Cap. 7 | Cap. 10 (Observabilidade e SRE) |
| **Construir sistemas agênticos e multi-agente integrados** | Cap. 7 → Cap. 8 → Cap. 9 | Cap. 6 e Cap. 10 |

Cada capítulo segue a mesma estrutura didática: **modelo mental → mecânica técnica → padrões e exemplos concretos → trade-offs e armadilhas → checklist acionável**.

