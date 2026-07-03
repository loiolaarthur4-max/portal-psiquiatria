import streamlit as st
import json
import os

st.title("⚡ Quiz: Os Rumos da Psiquiatria")

# Define o caminho absoluto para o arquivo na raiz
# O __file__ é o local atual deste script (pages/03_Quiz.py)
caminho_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_arquivo = os.path.join(caminho_raiz, 'banco_questoes.json')

# Debug: Se der erro, você verá no site exatamente onde ele está procurando
if not os.path.exists(caminho_arquivo):
    st.error(f"Erro: O arquivo não foi encontrado em: {caminho_arquivo}")
    st.write("Verifique se o arquivo 'banco_questoes.json' está na pasta raiz do seu projeto.")
    st.stop()

with open(caminho_arquivo, "r", encoding="utf-8") as f:
    questoes = json.load(f)

# ... resto do seu código
