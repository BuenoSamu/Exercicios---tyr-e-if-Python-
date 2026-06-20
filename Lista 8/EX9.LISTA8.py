disciplinas = [
    {"nome": "Matematica", "nota": 10, "freq": 90},
    {"nome": "Fisica", "nota": 9, "freq": 80},
    {"nome": "Historia", "nota": 7, "freq": 95},
    {"nome": "Quimica", "nota": 6, "freq": 85}
]

def emordemdecrescenteounao(disciplinas):

    if len(disciplinas) == 0:
        return None
    
    i = 0 

    while i < len(disciplinas) - 1 :
        if disciplinas[i]["nota"] < disciplinas[i + 1]["nota"]:
            return False
        i += 1
    return True

print (emordemdecrescenteounao(disciplinas))
