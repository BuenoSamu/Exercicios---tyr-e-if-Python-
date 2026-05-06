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

registro_de_disciplina =[
    ['Química', 5.0, 0.75],
    ['Física', 6.5, 0.80],
    ['Português', 7.0, 0.85],
    ['Matemática', 8.5, 0.90],
    ['História', 9.2, 0.95]
]

def EstaEmOrdemCrescenteOuNao(notas):

    if notas == []:
        return None
    
    i = 0
    # Vai até o penúltimo elemento
    while i < len(notas) - 1:
        # Compara a nota atual com a próxima
        if notas[i][1] > notas[i + 1][1]:
            return False
        i += 1
    return True

apresentacao()
notas = EstaEmOrdemCrescenteOuNao(registro_de_disciplina)
print(notas)