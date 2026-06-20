disciplinas = [
    {"nome": "Matematica", "nota": 8.5, "freq": 90},
    {"nome": "Fisica", "nota": 9.2, "freq": 80},
    {"nome": "Historia", "nota": 7.0, "freq": 95},
    {"nome": "Quimica", "nota": 6.8, "freq": 85}
]

def notacrescenteounao(disciplinas):

    if len(disciplinas) == 0: 
        return None
    
    i = 0 
    ordemdasnotas = 0 

    while i < len(disciplinas) - 1:

        if disciplinas[i]["nota"] > disciplinas[i + 1]["nota"]:
            return False
        i += 1
    return True

print(notacrescenteounao(disciplinas))