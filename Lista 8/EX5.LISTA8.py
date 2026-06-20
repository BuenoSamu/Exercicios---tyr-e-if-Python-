disciplinas = [
    {"nome": "Matematica", "nota": 8.5, "freq": 90},
    {"nome": "Fisica", "nota": 9.2, "freq": 80},
    {"nome": "Historia", "nota": 7.0, "freq": 95}
]

def mediageometrica (disciplinas):

    if len(disciplinas) == 0:
        return None
    
    i = 0 
    produto = 1
    quantidade = 0

    while i < len(disciplinas):
        produto *= disciplinas[i]["nota"] 
        quantidade = len(disciplinas)
        mediageometrica = produto ** (1 / quantidade)
        i += 1
    return mediageometrica

print(mediageometrica(disciplinas))