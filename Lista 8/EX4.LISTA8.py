disciplinas = [
    {"nome": "Matematica", "nota": 8.5, "freq": 90},
    {"nome": "Fisica", "nota": 9.2, "freq": 80},
    {"nome": "Historia", "nota": 7.0, "freq": 95}
]


def mediaaritmeticadasotas (disciplinas):

    if len(disciplinas) == 0:
        return None
    
    i = 0 
    soma = 0

    while i < len(disciplinas):

        soma += disciplinas[i]["nota"]
        media = soma / len(disciplinas)

        i += 1

    return media

    


print(mediaaritmeticadasotas(disciplinas))