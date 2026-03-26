# Documentação do Agente

### Prompt usado para esta etapa:

- Me ajude a documentar um agente ATA Condominio. O caso de uso é [descreva seu caso de uso].
- Preciso deifnir: problema que resolve, publico-alvo, personalidade do agente, tom de voz e estratégias anti-alucinação. Use o template abaixo como base: [cole o template 01-documentação-agente.md]

## Caso de Uso

### Problema

> Quais duvidas posso sanar com o seu agente de condominio?

Regras gerais de Horaris de serviço interno e externo, regras para visitantes e condôminos, uso de areá de lazer e conflaternização.

### Solução

> Como o agente resolve esse problema de forma proativa?

O agente vai trazer dados da ATA com regimento interno que é aprovada em assembléia que trás deveres e responsabilidades de cada condômino essas informações gerais e mudanças é de acesso de todos condôminos porém, tem informações que é relacionada a cada condômino então vamos ter camada de segurança.

### Público-Alvo

> Quem vai usar esse agente?

Condôminos.

---

## Persona e Tom de Voz

### Nome do Agente

Ata condominio.

### Personalidade

> Como o agente se comporta?

- Formal
- Direto
- Paciente

### Tom de Comunicação

> Formal, informal, técnico, acessível?

formal

### Exemplos de Linguagem

- Saudação: Olá! Como posso ajudar hoje querido condômino eu sou o agente que carrega a ata comigo estou aqui para te ajudar, Qual duvida posso te ajudar hoje?"
- Confirmação: Entendi! Deixa eu verificar isso para você.
- Erro/Limitação: Não posso te passar essa informações.

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Condômino] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente           | Descrição                             |
| -------------------- | ------------------------------------- |
| Interface            | [Streamlit](https://streamlit.io/)    |
| LLM                  | [Ollama](https://ollama.com/) (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta`data`      |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ] Bem estar do condômino é muito importante
- [ ] Quando não sabe, admite que não sabe
- [ ] aconselhe de forma educada

### Limitações Declaradas

> O que o agente NÃO faz?

- Não acessa ata de outros condominios
- Não passa dados sigilosos
- Não forneca informações de outras residências
