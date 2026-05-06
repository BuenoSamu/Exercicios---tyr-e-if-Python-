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

def EstaEmOrdemDecrescenteOuNao(notas):

    i = 0 
    while i < len(notas) - 1:
        if notas[i][1] < notas[i + 1][1]:
            return False
        i += 1
    return True

notas = EstaEmOrdemDecrescenteOuNao(registro_de_disciplina)
print(notas)
