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

pesos = [1, 2, 3, 4, 5]

def NotasVezesPesos(notas):

    if notas == []:
        return None
    
    resultados = []

    i = 0

    while i < len(notas):

        resultado = notas[i][1] * pesos[i]

        resultados.append(resultado)

        i += 1

    return resultados


def SomaDosResultados(resultado):

    soma = 0 
    i = 0

    while i < len(resultado):

        soma += resultado[i]

        i += 1

    return soma


def SomaDosPesos(pesos):

    if pesos == []:
        return None

    soma = 0 
    i = 0 

    while i < len(pesos):

        soma += pesos[i]

        i += 1

    return soma


def DivisaoPorPesos():

    resultados = NotasVezesPesos(registro_de_disciplina)

    soma_resultados = SomaDosResultados(resultados)

    soma_pesos = SomaDosPesos(pesos)

    if soma_resultados == None or soma_pesos == None:
        return None

    divisao = soma_resultados / soma_pesos

    return divisao


apresentacao()
print(DivisaoPorPesos())