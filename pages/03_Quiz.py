import streamlit as st
import json
import os

st.title("📚 Portal de Psiquiatria - 500 Questões")

# Localiza o arquivo na raiz
caminho_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_arquivo = os.path.join(caminho_raiz, 'banco_questoes.json')

@st.cache_data
def carregar_dados():
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

questoes = carregar_dados()

if 'idx' not in st.session_state: st.session_state.idx = 0
idx = st.session_state.idx

q = questoes[idx]
st.subheader(f"Questão {idx + 1} de {len(questoes)}")
st.write(q["pergunta"])

opcoes_formatadas = [f"{k} - {v}" for k, v in q["opcoes"].items()]
escolha = st.radio("Selecione:", opcoes_formatadas, key=f"q_{idx}")

if st.button("Responder"):
    if escolha.startswith(q["correta"]):
        st.success("Correto!")
    else:
        st.error(f"Errado! A correta era {q['correta']}")

col1, col2 = st.columns(2)
with col1:
    if st.button("Anterior") and idx > 0:
        st.session_state.idx -= 1
        st.rerun()
with col2:
    if st.button("Próxima") and idx < len(questoes) - 1:
        st.session_state.idx += 1
        st.rerun()
