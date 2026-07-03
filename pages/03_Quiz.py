import streamlit as st
import json
import os

st.title("⚡ Quiz: Os Rumos da Psiquiatria")

caminho_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
caminho_arquivo = os.path.join(caminho_raiz, 'banco_questoes.json')

with open(caminho_arquivo, "r", encoding="utf-8") as f:
    questoes = json.load(f)

# Verifica se o banco não está vazio
if not questoes:
    st.warning("O banco de questões está vazio.")
    st.stop()

# Inicializa o estado
if 'idx' not in st.session_state: st.session_state.idx = 0

idx = st.session_state.idx
q = questoes[idx]

st.subheader(f"Questão {idx + 1}")
st.write(q["pergunta"])

# Exibe as opções
escolha = st.radio("Escolha uma opção:", list(q["opcoes"].values()), key="opcao_selecionada")

if st.button("Confirmar Resposta"):
    # Encontra a chave (A, B, C...) da opção escolhida
    resposta_usuario = [k for k, v in q["opcoes"].items() if v == escolha][0]
    
    if resposta_usuario == q["correta"]:
        st.success("✅ Correto!")
    else:
        st.error(f"❌ Incorreto. A correta seria: {q['correta']}")

if st.button("Próxima Questão ➡️"):
    if idx < len(questoes) - 1:
        st.session_state.idx += 1
        st.rerun()
