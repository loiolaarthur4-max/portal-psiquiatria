# No início do seu arquivo pages/03_Quiz.py
import json

# Abra o arquivo diretamente, sem caminhos complicados
with open("banco_questoes.json", "r", encoding="utf-8") as f:
    questoes = json.load(f)

# Isso deve forçar a leitura do único arquivo que existe na pasta
