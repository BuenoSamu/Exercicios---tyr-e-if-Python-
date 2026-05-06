def apresentacao():
    print("+----------------------------+")
    print("|                            |")
    print("| PROGRAMA PARA LISTINHAS E  |")
    print("|          LISTONAS          |")
    print("|                            |")
    print("|                            |")
    print("|Versão 2.0 de 02/05/2026    |")
    print("|                            |")
    print("+----------------------------+")

registro_de_disciplina = [
    ['História', 9.2, 0.95],
    ['Matemática', 8.5, 0.90],
    ['Português', 7.0, 0.85],
    ['Física', 6.5, 0.80],
    ['Química', 5.0, 0.75]
]

nova_materia = ["Biologia", 7.5, 0.88]

def AdiconaNovaMateriaEmOrdemDecrescente(registro):

    if registro == []:
        return None
    
    i = 0 

    while i < len(registro):
        if nova_materia[1] > registro[i][1]:
            registro.insert(i, nova_materia)
            break
        i += 1
    return registro

apresentacao()
AdiconaNovaMateriaEmOrdemDecrescente(registro_de_disciplina)
print(registro_de_disciplina)
