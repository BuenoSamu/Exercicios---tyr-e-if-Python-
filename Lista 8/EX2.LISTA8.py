disciplinas = [
    {"nome": "Matematica", "nota": 8.5, "freq": 90},
    {"nome": "Fisica", "nota": 9.2, "freq": 80},
    {"nome": "Historia", "nota": 7.0, "freq": 95}
]

def menorFrequencia(disciplinas):

    if len(disciplinas) == 0:
        return None
    
    menor_frequencia = disciplinas[0]["freq"]
    menor_nome = disciplinas[0]["nome"]

    i = 1 

    while i < len(disciplinas):
        if disciplinas[i]["freq"] < menor_frequencia:
            menor_frequencia = disciplinas[i]["freq"]
            menor_nome = disciplinas[i]["nome"]

        i += 1
        
        return menor_frequencia, menor_nome
    
print(menorFrequencia(disciplinas))

    
