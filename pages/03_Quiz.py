import streamlit as st
import json
import os

st.title("⚡ Diagnóstico do Quiz")

try:
    # Tenta abrir o arquivo
    with open("banco_questoes.json", "r", encoding="utf-8") as f:
        questoes = json.load(f)
    
    st.write(f"Arquivo lido com sucesso! Total de questões: {len(questoes)}")
    
    # Exibe a primeira questão para testar
    if len(questoes) > 0:
        st.write("Primeira questão:", questoes[0]["pergunta"])
    else:
        st.write("O arquivo JSON está vazio (sem questões dentro dos colchetes []).")

except Exception as e:
    st.error("Ocorreu um erro ao carregar o arquivo JSON:")
    st.code(str(e))
    st.write("Dica: Verifique se o arquivo JSON está com vírgulas entre as questões e se começa com [ e termina com ].")
