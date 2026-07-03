import streamlit as st
import json
import os

st.title("📝 Meus Blocos de Notas")

# Carrega notas
if not os.path.exists("notas.json"):
    with open("notas.json", "w") as f: json.dump({}, f)

with open("notas.json", "r") as f:
    notas = json.load(f)

titulo = st.text_input("Nome do bloco:")
if st.button("Criar") and titulo:
    notas[titulo] = ""
    with open("notas.json", "w") as f: json.dump(notas, f)
    st.rerun()

if notas:
    bloco = st.selectbox("Escolha seu bloco:", list(notas.keys()))
    conteudo = st.text_area("Anote aqui:", value=notas[bloco], height=300)
    if st.button("Salvar"):
        notas[bloco] = conteudo
        with open("notas.json", "w") as f: json.dump(notas, f)
        st.success("Nota salva!")
