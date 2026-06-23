alunos = [
    {"id": 1, "nome": "Lucas"},
    {"id": 2, "nome": "Marina"},
    {"id": 3, "nome": "Samuel"}
]

treinos = [
    {"cod": "T1", "nome": "Perna"},
    {"cod": "T2", "nome": "Peito"}
]

frequencia = [
    {"idAluno": 1, "treinos": ["T1", "T2"]},
    {"idAluno": 2, "treinos": ["T2"]},
    {"idAluno": 3, "treinos": ["T1", "T2"]}
]

def alunosquefizeramtodosostreinos(alunos, treinos, frequencia):

    i = 0 
    resultado = [] 

    while i < len(frequencia): 
        totaltreinos = len(treinos)
        idaluno = frequencia[i]["idAluno"]
        idtreinos = frequencia[i]["treinos"]



        j = 0
        nomealuno = None
        while j < len(alunos):
            totaltreinado = len(frequencia[i]["treinos"])
            if  alunos[j]["id"] == idaluno:
                if totaltreinado == totaltreinos: 
                    nomealuno = alunos[j]["nome"]
            j += 1

        k = 0 
        listatreinos = []
        while k < len(treinos): 
            if treinos[k]["cod"] in idtreinos:
                listatreinos.append(
                    treinos[k]["nome"]
                )
            k += 1

        if totaltreinado != len(treinos):
            print("Aluno nao treinou tudo")
        else:
            resultado.append({
                "Nome do aluno: ": nomealuno,
                "Treinos do aluno ": listatreinos
            })
        i += 1
    return resultado
print(alunosquefizeramtodosostreinos(alunos, treinos, frequencia))



