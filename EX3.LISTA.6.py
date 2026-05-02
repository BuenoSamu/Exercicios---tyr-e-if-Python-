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
    ["Matemática", 8.5, 0.90], 
    ["Português", 7.0, 0.85],   
    ["História", 9.2, 0.95],   
    ["Física", 6.5, 0.80], 
    ["Química", 5.0, 0.75] 
]

def soma_das_notas_disciplinas(notas):
    
    if notas == []:
        return None

    soma = 0 
    i = 0

    while i < len(registro_de_disciplina):

        soma += registro_de_disciplina[i][1]

        i += 1

    apresentacao()
    print(soma)
soma_das_notas_disciplinas(registro_de_disciplina)