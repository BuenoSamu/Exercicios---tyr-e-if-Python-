alunos = [
    {"id": 1, "nome": "Amanda"},
    {"id": 2, "nome": "Bruno"},
    {"id": 3, "nome": "Camila"},
    {"id": 4, "nome": "Diego"}
]

disciplinas = [
    {"idAluno": 1, "media": 8},
    {"idAluno": 2, "media": 4},
    {"idAluno": 3, "media": 6},
    {"idAluno": 4, "media": 3}
]

turmas = [
    {"idAluno": 1, "turma": "A"},
    {"idAluno": 2, "turma": "B"},
    {"idAluno": 3, "turma": "A"},
    {"idAluno": 4, "turma": "B"}
]

def alunoscommediabaixa (alunos, disciplinas, turmas):

    resultado = []
    i = 0 

    while i < len(disciplinas):
        
        media = disciplinas[i]["media"]
        idaluno = disciplinas[i]["idAluno"]

        if media < 5: 

            j = 0 
            nomealuno = None
            while j < len(alunos):
                if alunos[j]["id"] == idaluno:
                    nomealuno = alunos[j]["nome"]
                    break
                j += 1

                k = 0
                turmaaluno = None
                while k < len(turmas):
                    if turmas[k]["idAluno"] == idaluno:
                        turmaaluno = turmas[k]["turma"]
                        break
                    k += 1 


            if nomealuno is not None and media is not None and turmaaluno is not None: 
                resultado.append({
                    "Nome do aluno: ": nomealuno,
                    "Media do aluno: ": media,
                    "Turma do aluno: ": turmaaluno
            })

        i += 1

    return resultado

print(alunoscommediabaixa(alunos, disciplinas, turmas))
        
        