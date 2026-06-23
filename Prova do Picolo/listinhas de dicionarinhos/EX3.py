aluno = [
    {"id": 10, "nome": "Lucas"},
    {"id": 11, "nome": "Marina"},
    {"id": 12, "nome": "João"}
]

turma = [
    {"id": 1, "nome": "3A"},
    {"id": 2, "nome": "3B"}
]

falta = [
    {"idAluno": 10, "idTurma": 1},
    {"idAluno": 11, "idTurma": 2},
    {"idAluno": 10, "idTurma": 2}
]

def alunoscomnenhumafalta(aluno, falta): 

    i = 0 
    resultado = [] 
    alunosencontrados = [] 

    while i < len(falta): 

        idaluno = falta[i]["idAluno"]
        if idaluno not in alunosencontrados: 
            alunosencontrados.append(idaluno)
        i += 1

    j = 0
    while j < len(aluno): 
        if aluno[j]["id"] not in alunosencontrados: 
            nomedoaluno = aluno[j]["nome"]
            resultado.append({"Nome do aluno que nunca tomou falta: ": nomedoaluno})
        j += 1 
    return resultado
print(alunoscomnenhumafalta(aluno, falta))

        
