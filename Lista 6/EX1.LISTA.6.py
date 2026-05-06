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

##LISTONA COM LISTINHAS

registro_de_disciplina = [
    ["Matemática", 8.5, 0.90], #POSIÇÃO 0
    ["Português", 7.0, 0.85],   #POSIÇÃO 1
    ["História", 9.2, 0.95],    #POSIÇÃO 2
    ["Física", 6.5, 0.80],  #POSIÇÃO 3
    ["Química", 5.0, 0.75]  #POSIÇÃO 4
]

#CADA LISTINHA POSSUI: 
# [0] -> NOME [1] -> NOTA [2] -> FREQUENCIA

#CHAMADA DE FUNCAO

def diciplina_com_maior_nota(disciplina):

    # Verifica se a lista está vazia
    if disciplina == []:
        return None

    # Assume a primeira disciplina como maior
    maior = disciplina[0]

    # Começa no segundo elemento
    i = 1

    # Percorre a lista
    while i < len(disciplina):

        # Compara a nota atual com a maior nota
        if disciplina[i][1] > maior[1]:

            # Atualiza a maior disciplina
            maior = disciplina[i]

        # Vai para o próximo item
        i += 1

    # Retorna apenas o nome da disciplina
    return maior[0]

apresentacao()
print(diciplina_com_maior_nota(registro_de_disciplina))


 