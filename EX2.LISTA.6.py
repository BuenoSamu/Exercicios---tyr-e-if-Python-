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

def disciplina_com_menor_nota(disciplina):

    if disciplina == []:
        return None
    
    menor = disciplina[0]
    i = 1

    while i < len(disciplina):
        if disciplina[i][1] < menor[1]:
         menor = disciplina[i]
        
        i += 1
    return menor[0]

apresentacao()
print(disciplina_com_menor_nota(registro_de_disciplina))