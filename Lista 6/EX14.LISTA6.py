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
    ["História", 9.2, 0.95],
    ["Química", 5.0, 0.75],
    ["Matemática", 8.5, 0.90],
    ["Física", 6.5, 0.80]
]

def ordenar_por_nota(registros):
    i = 1

    while i < len(registros):
        atual = registros[i]
        j = i - 1

        # Move os elementos maiores que a nota atual
        while j >= 0 and registros[j][1] > atual[1]:
            registros[j + 1] = registros[j]
            j = j - 1

        registros[j + 1] = atual
        i = i + 1

ordenar_por_nota(registro_de_disciplina)
print(registro_de_disciplina)

       

