# 🤖 Agente ATA - Condomínio Inteligente com IA Generativa

## 📋 Contexto

Muitas vezes, no corre-corre do dia a dia, ao mudarmos de residência, somos apresentados a novos vizinhos e novas regras. Um problema comum é que muitos moradores não se atentam à **ATA** ou ao regimento interno do condomínio por serem documentos extensos e de difícil leitura.

Este projeto visa transformar essa base de dados estática em um **agente inteligente e proativo**. O objetivo é prototipar um assistente que utiliza IA Generativa para:

- **Interpretar as regras**: Em vez de apenas buscar palavras-chave, entender o contexto das normas.
- **Relatórios de Acesso**: Permitir que o morador consulte rapidamente quem acessou sua unidade.
- **Confiabilidade (Anti-alucinação)**: Garantir que o agente responda apenas com base nos documentos fornecidos.

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## 🚀 O Que Você Deve Entregar

### 1. Documentação do Agente

Defina o escopo e o funcionamento do seu assistente:

- **Caso de Uso:** Suporte em segurança, normas e praticidade.
- **Persona e Tom de Voz:** Como o agente se comunica (ex: prestativo, formal, direto).
- **Arquitetura:** Fluxo de dados (RAG) e integração com a base.
- **Segurança:** Estratégias para evitar respostas inventadas.

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados fictícios** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo                      | Formato | Descrição                                     |
| :--------------------------- | :------ | :-------------------------------------------- |
| `ata_condominio.csv`         | CSV     | Decisões de assembleias e legislação interna. |
| `morador.json`               | JSON    | Cadastro de moradores e dependentes.          |
| `regras.json`                | JSON    | Regimento interno e normas de convivência.    |
| `ocorrencias_condominio.csv` | CSV     | Registro de manutenções e avisos.             |
| `visitantes.json`            | JSON    | Registro histórico de entradas e saídas.      |
| `empresas.json`              | JSON    | Lista de prestadores de serviços homologados. |

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente a engenharia de prompts utilizada:

- **System Prompt:** Regras de comportamento e restrições de segurança.
- **Exemplos (Few-shot):** Exemplos de perguntas e respostas ideais.
- **Edge Cases:** Como o agente deve agir quando não encontrar uma resposta.

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva o **protótipo**:

- Interface de Chat (Streamlit, Gradio ou similar).
- Integração com LLM (OpenAI, Google Gemini, Anthropic ou Local via Ollama).
- Mecanismo de busca nos arquivos (RAG).

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Como medir o sucesso do agente?

- **Precisão:** A resposta condiz com o PDF/CSV?
- **Privacidade:** O morador X conseguiu ver dados do morador Y? (Teste de falha).
- **Tempo de Resposta:** O quão rápido o agente processa a dúvida.

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um vídeo ou escreva um roteiro de **3 minutos** focando em:

- Problema vs. Solução.
- Demonstração rápida.
- Diferencial tecnológico.

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## 📂 Estrutura do Repositório

```text
📁 lab-agente-condominio/
│
├── 📄 README.md
│
├── 📁 data/                          # Base de dados (CSV/JSON)
│   ├── ata_condominio.csv
│   ├── empresas.json
│   ├── morador.json
│   ├── ocorrencias_condominio.csv
│   ├── regras.json
│   └── visitantes.json
│
├── 📁 docs/                          # Documentação detalhada
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── 📁 src/                           # Código-fonte da aplicação
│   └── app.py
│
└── 📁 examples/                      # Materiais de apoio
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** Não vazar informações de outros condôminos
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
