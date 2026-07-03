import streamlit as st
import json

st.title("📚 Portal de Psiquiatria")

with open("banco_questoes.json", "r", encoding="utf-8") as f:
    questoes = json.load(f)

if 'idx' not in st.session_state: st.session_state.idx = 0
idx = st.session_state.idx
q = questoes[idx]

st.write(f"### Questão {idx + 1}")
st.write(q["pergunta"])

# AQUI ESTÁ O SEGREDO: Vamos listar as opções com texto
opcoes_lista = []
for letra, texto in q["opcoes"].items():
    opcoes_lista.append(f"{letra}: {texto}")

escolha = st.radio("Escolha uma alternativa:", opcoes_lista)

if st.button("Verificar"):
    letra_selecionada = escolha.split(":")[0] # Pega apenas a letra (A, B...)
    if letra_selecionada == q["correta"]:
        st.success("✅ Correto!")
    else:
        st.error(f"❌ Errado. A correta era {q['correta']}")

if st.button("Próxima"):
    st.session_state.idx += 1
    st.rerun()
