disciplinas = [
    {"nome": "Matematica", "nota": 10, "freq": 90},
    {"nome": "Fisica", "nota": 9, "freq": 80},
    {"nome": "Geografia", "nota": 8, "freq": 80},
    {"nome": "Historia", "nota": 7, "freq": 95},
    {"nome": "Quimica", "nota": 6, "freq": 85}
]

novadisciplina = {"nome": "Artes", "nota": 5, "freq": 70}

def adiconanovadisciplinaemordemdecrescente(disciplinas, novadisciplina):
    if len(disciplinas) == 0:
        return None

    i = 0
    while i < len(disciplinas) and disciplinas[i]["nota"] > novadisciplina["nota"]:
        i += 1

    disciplinas.insert(i, novadisciplina)
    return disciplinas

print(adiconanovadisciplinaemordemdecrescente(disciplinas, novadisciplina))