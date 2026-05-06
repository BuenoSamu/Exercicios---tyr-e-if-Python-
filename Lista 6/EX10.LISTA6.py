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
    ["Química", 5.0, 0.75],
    ["Física", 6.5, 0.80],
    ["Português", 7.0, 0.85],
    ["Matemática", 8.5, 0.90],
    ["História", 9.2, 0.95]
]

nova_materia = ["Biologia", 7.5, 0.88]


def NovoRegistroParaManterOrdemCrescente(registro):

    if registro == []:
        return None
    
    i = 0

    while i < len(registro):

        # Compara a nova nota
        # com a nota atual
        if nova_materia[1] < registro[i][1]:

            # Insere antes
            registro.insert(i, nova_materia)

            break
        
        i += 1

    return registro

apresentacao()
NovoRegistroParaManterOrdemCrescente(registro_de_disciplina)
print(registro_de_disciplina)