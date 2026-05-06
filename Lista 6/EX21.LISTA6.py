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

alunos = [
    [1010, "Ana Silva", "19999990001", "ana@email.com"],
    [2021, "Bruno Costa", "19999990002", "bruno@email.com"],
    [3032, "Carla Souza", "19999990003", "carla@email.com"],
    [4043, "Daniel Lima", "19999990004", "daniel@email.com"],
    [5054, "Eduarda Rocha", "19999990005", "eduarda@email.com"]
]

disciplinas = [
    ["MAT01", "Matematica", 4],
    ["POR01", "Portugues", 3],
    ["HIS01", "Historia", 2],
    ["FIS01", "Fisica", 4],
    ["BIO01", "Biologia", 3]
]

resultados = [
    [1010, "MAT01", 1, 2025, 8.5, 90],
    [1010, "POR01", 1, 2025, 7.0, 85],
    [1010, "HIS01", 1, 2025, 5.0, 60],

    [2021, "MAT01", 1, 2025, 9.8, 95],  
    [2021, "FIS01", 1, 2025, 8.0, 88],
    [2021, "BIO01", 1, 2025, 7.5, 92],

    [3032, "POR01", 1, 2025, 4.5, 55],  
    [3032, "HIS01", 1, 2025, 6.0, 70],
    [3032, "BIO01", 1, 2025, 5.5, 65],

    [4043, "MAT01", 1, 2025, 3.0, 40], 
    [4043, "FIS01", 1, 2025, 4.0, 50],

    [5054, "POR01", 1, 2025, 10.0, 98],
    [5054, "BIO01", 1, 2025, 9.0, 97],
    [5054, "HIS01", 1, 2025, 8.0, 96]
]

def maiorNota(Nota):

    if Nota == []:
        return None
    
    i = 0

    # pega a primeira nota como referência
    maiorNota = Nota[0][4]

    while i < len(Nota):
        if Nota[i][4] > maiorNota:
            maiorNota = Nota[i][4]
        i += 1
    return maiorNota

def EncontraRaMaiorNota(resultados):

    if resultados == []:
        return None

    i = 0
    
    notaMaior = maiorNota(resultados)

    while i < len(resultados):
        if resultados[i][4] == notaMaior:
            
            return resultados[i][0]
        
        i += 1

def EncontraNomeDaMaiorNota(Ra):
     
     if Ra == []:
      return None
     
     i = 0
     raMaior = EncontraRaMaiorNota(resultados)

     while i < len(alunos):
         if alunos[1][0] == raMaior:
             alunos[i][0]
         return alunos[i][1]


apresentacao()
print(EncontraNomeDaMaiorNota(alunos))