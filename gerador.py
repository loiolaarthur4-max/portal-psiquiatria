import json

banco = []
temas = ["RDoC", "Psicofarmacologia", "Psiquiatria de Precisão", "Neurociência", "Psiquiatria Social"]

for i in range(1, 501):
    questao = {
        "id": i,
        "pergunta": f"Questão {i}: Sobre {temas[i % 5]}, qual a conduta baseada em evidências?",
        "opcoes": {
            "A": "Abordagem baseada em biomarcadores e circuitos",
            "B": "Tratamento empírico sem avaliação clínica",
            "C": "Ignorar os determinantes sociais",
            "D": "Uso exclusivo de métodos arcaicos",
            "E": "Focar apenas em efeitos colaterais"
        },
        "correta": "A"
    }
    banco.append(questao)

with open('banco_questoes.json', 'w', encoding='utf-8') as f:
    json.dump(banco, f, ensure_ascii=False, indent=4)

print("Arquivo 'banco_questoes.json' criado com 500 questões!")
