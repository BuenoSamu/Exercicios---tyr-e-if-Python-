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

def media_geometrica_das_notas(notas):

    # Verifica se a lista está vazia
    if notas == []:
        return None

    # Começa em 1 porque vamos multiplicar
    produto = 1

    # Contador
    i = 0

    # Percorre a lista
    while i < len(notas):

        # Multiplica pela nota atual
        produto *= notas[i][1]

        i += 1

    # Quantidade de disciplinas
    total = len(notas)

    # Média geométrica
    media = produto ** (1 / total) #tirando a raiz

    return media

apresentacao()
print(media_geometrica_das_notas(registro_de_disciplina))