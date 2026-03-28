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


# --- CONFIGURAÇÃO DO AGENTE ---
atas_texto = ata.to_dict(orient='records')
ocorrencias_texto = ocorrecias.to_dict(orient='records')

contexto = f"""
    DADOS DO MORADOR ATUAL: {morador}
    REGRAS DO CONDOMÍNIO: {regras}
    EMPRESAS PRESTADORAS: {empresa}
    VISITANTES DO MORADOR: {visitantes}
    HISTÓRICO DE ATAS: {atas_texto}
    REGISTRO DE OCORRÊNCIAS: {ocorrencias_texto}
"""

SYSTEM_PROMPT = """Você é o Assistente Virtual do Condomínio.
Sua missão: Responder perguntas dos moradores usando APENAS as REGRAS fornecidas.

REGRAS CRÍTICAS:
1. RESPONDA APENAS EM PORTUGUÊS.
2. Seja educado e direto.
3. NÃO mostre códigos, chaves JSON, colchetes ou termos técnicos como 'False' ou 'True'.
4. Se perguntarem quem é você, diga: 'Sou seu assistente virtual do condomínio, pronto para tirar dúvidas sobre regras e avisos'."""

def perguntar(msg):
    prompt = f"{SYSTEM_PROMPT}\n\nCONTEXTO:\n{contexto}\n\nPergunta: {msg}"
    
    # Corrigido: 'false' em Python é 'False' (com F maiúsculo)
    payload = {"model": MODELO, "prompt": prompt, "stream": False}
    
    try:
        r = requests.post(OLLAMA_URL, json=payload)
        return r.json()['response']
    except Exception as e:
        return f"Erro ao conectar ao Ollama: {e}"

# --- INTERFACE STREAMLIT ---
st.title("🤖 Seu Agente do Condomínio")

# Corrigido: st.chat_message (com underline, não +)
if pergunta := st.chat_input("Sua dúvida sobre o condomínio"):
    st.chat_message("user").write(pergunta)
    
    with st.spinner("Consultando base de dados..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
