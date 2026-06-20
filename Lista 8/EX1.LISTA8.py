disciplinas = [
    {"nome": "Matematica", "nota": 8.5, "freq": 90},
    {"nome": "Fisica", "nota": 9.2, "freq": 80},
    {"nome": "Historia", "nota": 7.0, "freq": 95}
]

def maior_nota(disciplinas):

    #se a lista estiver vazia, retorna None
    if len(disciplinas) == 0:
        return None
    
    #pega o primeiro dado como base inicial
    maior_nota = disciplinas[0]["nota"]
    maior_nome = disciplinas[0]["nome"]

    i = 0 #comeca do segundo elemento pois quero as notas

    #percorre a lista
    while i < len(disciplinas):
        #pega a atual e compara com a maior
        if disciplinas[i]["nota"] > maior_nota:

            maior_nota = disciplinas[i]["nota"]
            maior_nome = disciplinas[i]["nome"]

        i += 1

    return maior_nome , maior_nota

print(maior_nota(disciplinas))
