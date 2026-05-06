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

    # Nota: 9.2
    ["História", 9.2, 0.95],

    # Nota: 5.0
    ["Química", 5.0, 0.75],

    # Nota: 8.5
    ["Matemática", 8.5, 0.90],

    # Nota: 6.5
    ["Física", 6.5, 0.80]
]

def BubbleSortDecrescente(registro):

    if registro == []:
        return None
    
    i = 0 

    while i < len(registro):

        j = 0

        while j < len(registro) - 1:
            # Se a nota atual for MENOR
            # que a próxima
            if registro[j][1] < registro[j + 1][1]:

                # Troca de posição
                registro[j], registro[j + 1] = registro[j + 1], registro[j]

            j += 1

        i += 1

    return registro
apresentacao()
BubbleSortDecrescente(registro_de_disciplina)
print(registro_de_disciplina)