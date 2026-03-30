import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:120b-cloud"

# --- FUNÇÃO AUXILIAR PARA CARREGAR JSON CORRETAMENTE ---
def carregar_json(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

# --- CARREGAMENTO DE DADOS ---
# Corrigindo o erro AttributeError: 'str' object has no attribute 'read'
ata = pd.read_csv('C:/Users/novo/Desktop/IA Agente/agente python/data/ata_condominio.csv')
ocorrecias = pd.read_csv('C:/Users/novo/Desktop/IA Agente/agente python/data/ocorrencias_condominio.csv')

empresa = carregar_json('C:/Users/novo/Desktop/IA Agente/agente python/data/empresas.json')
morador = carregar_json('C:/Users/novo/Desktop/IA Agente/agente python/data/morador.json')
regras = carregar_json('C:/Users/novo/Desktop/IA Agente/agente python/data/regras.json')
visitantes = carregar_json('C:/Users/novo/Desktop/IA Agente/agente python/data/visitantes.json')
encomendas = carregar_json('C:/Users/novo/Desktop/IA Agente/agente python/data/encomendas.json')

# --- CONFIGURAÇÃO DO AGENTE ---
atas_texto = ata.to_dict(orient='records')
ocorrencias_texto = ocorrecias.to_dict(orient='records')

contexto = f"""
    DADOS DO MORADOR ATUAL: {morador}
    REGRAS DO CONDOMÍNIO: {regras}
    EMPRESAS PRESTADORAS: {empresa}
    ENCOMENDAS DO MORADOR: {encomendas}
    VISITANTES DO MORADOR: {visitantes}
    HISTÓRICO DE ATAS: {atas_texto}
    REGISTRO DE OCORRÊNCIAS: {ocorrencias_texto}
"""

SYSTEM_PROMPT = """Você é o Assistente Virtual do Condomínio.
Sua missão: Responder perguntas dos moradores cruzando TODOS OS DADOS fornecidos no contexto (Regras, Ocorrências, Atas, Moradores, etc.).

REGRAS CRÍTICAS DE COMPORTAMENTO:
1. RESPONDA APENAS EM PORTUGUÊS.
2. Seja educado e direto.
3. NÃO mostre códigos, chaves JSON, colchetes ou termos técnicos como 'False' ou 'True'.
4. Se perguntarem quem é você, diga: 'Sou seu assistente virtual do condomínio, pronto para tirar dúvidas sobre regras e avisos'.
5. PRIVACIDADE: Nunca forneça dados pessoais, telefone ou número de apartamento exato de outros moradores.

REGRAS CRÍTICAS DE BUSCA (ATENÇÃO AOS DADOS DE OCORRÊNCIAS):
6. PRIORIDADE DE OCORRÊNCIAS: Se o morador relatar um acontecimento específico (barulho, vazamento, obra) com DATA e HORA, você DEVE procurar PRIMEIRO no "REGISTRO DE OCORRENCIAS" antes de citar regras gerais.
7. BUSCA POR APROXIMAÇÃO E CONTEXTO: 
- Busque no arquivo de ocorrências por QUALQUER registro que tenha acontecido em um intervalo de até 15 minutos de diferença do horário relatado pelo morador (Ex: 08:00 na pergunta = 08:01 no registro).
- Ignore a palavra literal do usuário. Se ele falar "obra", mas no registro estiver "manutencao" (como janela emperrada), assuma que é o mesmo evento.
8. PADRÃO DE RESPOSTA OBRIGATÓRIO: Ao encontrar uma ocorrência de "manutencao" em blocos vizinhos na data/hora informada, IGNORE as regras de horário e responda EXATAMENTE: "Verifiquei os registros e tem um morador com um problema de manutenção a ser resolvido próximo ao seu bloco. Entendeu a resposta?"

--- EXEMPLOS OBRIGATÓRIOS (SIGA ESTE PADRÃO) ---
Usuário: Ouvi um barulho estranho de obra no dia 25/05/2025 por volta das 08:00 perto do meu bloco B, o que aconteceu?
Assistente: Verifiquei os registros e tem um morador com um problema de manutenção a ser resolvido próximo ao seu bloco. Entendeu a resposta?
"""
# --- FUNÇÃO DE PERGUNTA COM HISTÓRICO ---
def perguntar(historico_conversa):
    # Monta o prompt juntando o Sistema, o Contexto (bancos de dados) e o Histórico recente
    prompt = f"{SYSTEM_PROMPT}\n\nCONTEXTO:\n{contexto}\n\nHISTÓRICO RECENTE DA CONVERSA:\n{historico_conversa}\n\nAssistente:"
    
    payload = {"model": MODELO, "prompt": prompt, "stream": False}
    
    try:
        r = requests.post(OLLAMA_URL, json=payload)
        return r.json()['response']
    except Exception as e:
        return f"Erro ao conectar ao Ollama: {e}"

# --- INTERFACE STREAMLIT COM MEMÓRIA ---
st.title("🤖 Seu Agente do Condomínio")

# 1. Inicializa a memória da conversa no Streamlit
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# 2. Mostra as mensagens antigas na tela
for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

# 3. Recebe a nova pergunta do usuário
if pergunta := st.chat_input("Sua dúvida sobre o condomínio"):
    # Salva a pergunta do usuário na memória e mostra na tela
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    st.chat_message("user").write(pergunta)
    
    # 4. Monta o texto do histórico para a IA ler (pegamos as últimas 6 interações para não ficar gigante)
    historico_texto = ""
    for m in st.session_state.mensagens[-6:]:
        ator = "Morador" if m["role"] == "user" else "Assistente"
        historico_texto += f"{ator}: {m['content']}\n"
    
    with st.spinner("Consultando base de dados..."):
        # Envia o histórico completo para a função
        resposta = perguntar(historico_texto)
        
        # Salva a resposta do Agente na memória e mostra na tela
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
        st.chat_message("assistant").write(resposta)
