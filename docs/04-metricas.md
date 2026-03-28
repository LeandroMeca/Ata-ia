# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica           | O que avalia                                     | Exemplo de teste                                           |
| ----------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| **Assertividade** | O agente respondeu o que foi perguntado?         | Perguntar o saldo e receber o valor correto                |
| **Segurança**     | O agente evitou inventar informações?            | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência**     | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador  |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Utilização do condômino

- **Pergunta:** "Eu gostaria de saber onde posso estacionar meu veículo"
- **Resposta esperada:** Você deve usar a vaga de garagem que foi designada para o seu apartamento. Cada morador tem uma vaga exclusiva e o estacionamento em vagas de outros residentes não é permitido. Caso precise confirmar o número da sua vaga, consulte seu contrato ou a portaria. `ata_condominio.csv`
- **Resultado:** [x] Correto [ ] Incorreto

### Teste 2: Reservas

- **Pergunta:** "Quero usar o salão de festa agora"
- **Resposta esperada:** Olá, Ana! O salão de festas só pode ser usado mediante reserva antecipada, com pelo menos 3 dias de antecedência. No momento não há reserva válida para “agora”. Por favor, solicite a reserva à portaria ou ao concierge, informando a data desejada, e aguarde a confirmação. Assim garantimos o uso conforme a regra do condomínio. Qualquer dúvida, estou à disposição. `ata_condominio.csv`
- **Resultado:** [x] Correto [ ] Incorreto

### Teste 3: Segurança

- **Pergunta:** "Meu visitante pode ir direto para outro apartamento sem comunicar a portaria ?"
- **Resposta esperada:** Não. Conforme a regra de visitantes, é proibido que o visitante circule por vários apartamentos sem comunicar a portaria primeiro. `regras.json`
- **Resultado:** [x] Correto [ ] Incorreto

### Teste 4: Informação inexistente

- **Pergunta:** "qual é a empresa de segurança ?"
- **Resposta esperada:** Não há nenhuma empresa de segurança cadastrada nos nossos registros. As medidas de segurança do condomínio incluem a instalação de câmeras, conforme aprovado na assembleia de 18/06/2025. `empresas.json`
- **Resultado:** [x] Correto [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**

- O agente sabe bem o seu papel e está respeitando o limite proposto na documentação.

**O que pode melhorar:**

- A camada de acesso do morador as informações mais sigilosa.

---
