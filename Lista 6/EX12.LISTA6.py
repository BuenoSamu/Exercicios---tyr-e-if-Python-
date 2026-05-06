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



# FUNÇÃO BUBBLE SORT
#
# Objetivo:
#
# Ordenar as disciplinas
# da menor nota para a maior nota
#
# Bubble Sort funciona:
#
# comparando vizinhos
#
# e trocando eles de lugar
# quando estão fora de ordem

def BubbleSort(registro):
    # VERIFICA SE A LISTA ESTÁ VAZIA
    #
    # [] = lista vazia
    if registro == []:
        # None significa:
        #
        # "não existe resultado válido"

        return None
    # CONTADOR EXTERNO
    #
    # Esse contador controla
    # quantas vezes o algoritmo
    # percorre a lista inteira
    #
    # Bubble Sort precisa passar
    # várias vezes pela lista
    #
    # porque uma única passada
    # não garante que tudo fique ordenado
    i = 0 
    # LOOP EXTERNO
    #
    # Vai repetir várias passadas
    # pela lista
    while i < len(registro):
        # CONTADOR INTERNO
        #
        # Esse contador compara:
        #
        # elemento atual
        #
        # com:
        #
        # próximo elemento
        j = 0 
        # LOOP INTERNO
        #
        # len(registro) - 1
        #
        # usamos -1 porque:
        #
        # vamos acessar:
        #
        # j + 1
        #
        # e o último índice
        # não possui próximo elemento
        while j < len(registro) - 1:
            # COMPARAÇÃO PRINCIPAL
            #
            # registro[j][1]
            #
            # pega a nota atual
            #
            # registro[j + 1][1]
            #
            # pega a próxima nota
            #
            # Pergunta:
            #
            # "a nota atual é maior
            # que a próxima nota?"
            #
            # Se for:
            #
            # elas estão fora de ordem
            if registro[j][1] > registro[j + 1][1]:
                # TROCA DE POSIÇÃO
                #
                # Isso troca as duas disciplinas
                #
                # EXEMPLO:
                #
                # antes:
                #
                # [9.2, 5.0]
                #
                # depois:
                #
                # [5.0, 9.2]

                registro[j], registro[j + 1] = registro[j + 1], registro[j]
            # PASSA PARA O PRÓXIMO PAR
            #
            # Sem isso:
            #
            # o loop ficaria infinito
            j += 1
        # TERMINOU UMA PASSADA COMPLETA
        #
        # Agora aumenta o contador externo
        i += 1
    # RETORNA A LISTA ORDENADA
    return registro
# EXECUTA O BUBBLE SORT
apresentacao()
BubbleSort(registro_de_disciplina)
# MOSTRA O RESULTADO FINAL
print(registro_de_disciplina)