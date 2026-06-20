disciplinas = [
    {"nome": "Matematica", "nota": 8.5, "freq": 90},
    {"nome": "Fisica", "nota": 9.2, "freq": 80},
    {"nome": "Historia", "nota": 7.0, "freq": 95},
    {"nome": "Quimica", "nota": 6.8, "freq": 85}
]

pesos = [1.5, 2.0, 1.0, 1.2]

def mediaaritmeticaponderada(disciplinas, pesos):
    if len(disciplinas) == 0 or len(pesos) == 0:
        return None
    
    if len(disciplinas) != len(pesos):
        return None
    
    somaponderada = 0
    somapesos = 0
    i = 0

    while i < len(disciplinas):
        nota = disciplinas[i]["nota"]
        peso = pesos[i]

        somaponderada += nota * peso
        somapesos += peso
        i += 1

    if somapesos == 0:
        return None

    resultado = somaponderada / somapesos
    return resultado

print(mediaaritmeticaponderada(disciplinas, pesos))