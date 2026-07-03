import streamlit as st
import json

st.title("⚡ Quiz: Os Rumos da Psiquiatria")

# Carrega o banco de questões
with open("banco_questoes.json", "r", encoding="utf-8") as f:
    questoes = json.load(f)

if 'idx' not in st.session_state: 
    st.session_state.idx = 0

idx = st.session_state.idx
q = questoes[idx]

st.subheader(f"Questão {idx + 1}")
st.write(q["pergunta"])

# Cria um seletor com as opções A, B, C, D, E
escolha = st.radio("Escolha uma opção:", list(q["opcoes"].values()))

if st.button("Confirmar Resposta"):
    # Verifica qual foi a letra escolhida
    resposta_usuario = [k for k, v in q["opcoes"].items() if v == escolha][0]
    
    if resposta_usuario == q["correta"]:
        st.success("✅ Correto!")
    else:
        st.error(f"❌ Incorreto. A correta seria: {q['correta']}")

if st.button("Próxima Questão ➡️"):
    if idx < len(questoes) - 1:
        st.session_state.idx += 1
        st.rerun()
