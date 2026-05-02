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

    # Verifica se a lista está vazia
    if notas == []:
        return None
    
    soma = 0
    i = 0 

    while i < len(notas):

        soma += notas[i][1]

        i += 1 

    return soma


def media_aritmetica_das_notas(notas):

    # Pega a soma das notas
    soma = soma_das_notas_disciplinas(notas)

    # Verifica se veio None
    if soma == None:
        return None

    # Conta quantas matérias existem
    total_materias = len(notas)

    # Calcula a média
    media = soma / total_materias

    return media

apresentacao()
print(media_aritmetica_das_notas(registro_de_disciplina))