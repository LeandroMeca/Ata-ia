# 🤖 Agente ATA Condominio Inteligente com IA Generativa

## Contexto

Passamos o dia oculpados com diversas tarefas cotidianas e muita das vezes nos deparamos com seguinte situação mudei de residencia isso significa vizinhos novos regras novas, quantas pessoas ao chegar na residencia nova acaba não se atentando a ATA, sim isso mesmo acontece com muita frequencia muitos não conseguem ler o regimento interno de um condominio, esse é um ponto chave para transformar essa base de dados de um papel em um agente **agentes inteligentes e proativos**. Neste desafio, você vai idealizar e prototipar um agente de condominio que utiliza IA Generativa para:

- **Entender todas regras** ao invés de apenas responder perguntas
- **acesasr relatorio** saber quando alguém acessou seu apartamento
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Qual suporte ele oderece? (ex: Segurança e Praticidade)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo                      | Formato | Utilização no Agente                        |
| ---------------------------- | ------- | ------------------------------------------- |
| `ata_condominio.csv`         | CSV     | Regras seguidas da legislação de assembléia |
| `morador.json`               | JSON    | Dados do morador e seus dados               |
| `regras.json`                | JSON    | Regras gerais                               |
| `ocorrencias_condominio.csv` | CSV     | ocorrências diarias                         |
| `visitantes.json`            | JSON    | dados visitante                             |
| `empresas.json`              | JSON    | tipos de serviços                           |

Você pode adaptar ou expandir esses dados conforme seu caso de uso.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**

- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Conexão do visitante e o morador visitado

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria           | Ferramentas                                                                                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LLMs**            | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/)                                                        |
| **Orquestração**    | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/)                                                                |
| **Diagramas**       | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/)                                                                  |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── ata_condominio.csv            # ata do condomino (CSV)
│   ├── empresas.json                 # Perfil do cliente (JSON)
│   ├── morador.json                  # Produtos disponíveis (JSON)
│   ├── ocorrencias_condominio.csv    # Histórico de serviços, reservas (CSV)
│   ├── regras.json                   # Para evitar transtorno e manter a armonia entre visinhos (JSON)
|   └── visitantes.json               # Tenha o controle de todas as suas visitas da sua residencia (JSON)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** Não vazar informações de outros condôminos
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
