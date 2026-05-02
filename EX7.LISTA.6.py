registro_de_disciplina = [
    ["Matemática", 8.5, 0.90], 
    ["Português", 7.0, 0.85],   
    ["História", 9.2, 0.95],   
    ["Física", 6.5, 0.80], 
    ["Química", 5.0, 0.75] 
]

pesos = [1, 2, 3, 4, 5]

def ElevaNotaPeloPeso(notas):

    if notas == []:
        return None
    resultados = []

    i = 0

    while i < len(notas):
        resultado = notas[i][1] ** pesos[i]
        resultados.append(resultado)

        i += 1
    
    return resultados

def MultiplicaTodosOsResultados(resultados):

    multiplica = 1
    i = 0 

    while i <len(resultados):

        multiplica *= resultados[i]
        i += 1
    return multiplica

def SomaDosPesos(pesos):

    if pesos == []:
        return None
    
    soma = 0 
    i = 0

    while i< len(pesos):
        soma += pesos[i]
        i += 1

    return soma

def TirarRaiz(produto, soma_pesos):

    if soma_pesos == 0:
        return None
    
    raiz = produto ** (1 / soma_pesos)

    return raiz
    
resultados = ElevaNotaPeloPeso(registro_de_disciplina)
ResultadoDaMultiplicacao = MultiplicaTodosOsResultados(resultados)
SomaDosPesos = SomaDosPesos(pesos)
media = TirarRaiz(ResultadoDaMultiplicacao, SomaDosPesos)
print(media)
