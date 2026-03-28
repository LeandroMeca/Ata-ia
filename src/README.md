# Execução da aplicação

## Ollama Setup
```bash
 # 1. Instalar o Ollama
 # 2. Baixar modelo leve ou usar Cloud
 # 3. ollama pull MODELO

 # 4. testar se funciona
ollama run MODELO "Ola!"
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run .\src\app.py
```
