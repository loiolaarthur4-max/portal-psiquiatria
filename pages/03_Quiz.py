import streamlit as st
import json

st.title("📚 Portal de Psiquiatria")

# Tenta carregar o JSON
try:
    with open("banco_questoes.json", "r", encoding="utf-8") as f:
        questoes = json.load(f)
except Exception as e:
    st.error(f"Erro ao carregar o arquivo JSON: {e}")
    st.stop()

# Garante que o índice nunca seja maior que o número de questões
if 'idx' not in st.session_state or st.session_state.idx >= len(questoes):
    st.session_state.idx = 0

idx = st.session_state.idx
q = questoes[idx]

st.write(f"### Questão {idx + 1} de {len(questoes)}")
st.write(q["pergunta"])

# Exibe as opções formatadas
opcoes_lista = [f"{letra}: {texto}" for letra, texto in q["opcoes"].items()]
escolha = st.radio("Escolha uma alternativa:", opcoes_lista, key=f"radio_{idx}")

if st.button("Verificar"):
    letra_selecionada = escolha.split(":")[0]
    if letra_selecionada == q["correta"]:
        st.success("✅ Correto!")
    else:
        st.error(f"❌ Errado. A correta era {q['correta']}")

# Botões de navegação com proteção
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Anterior"):
        if st.session_state.idx > 0:
            st.session_state.idx -= 1
            st.rerun()

with col2:
    if st.button("Próxima ➡️"):
        if st.session_state.idx < len(questoes) - 1:
            st.session_state.idx += 1
            st.rerun()
