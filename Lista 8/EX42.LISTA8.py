alunos = [
    {"id": 1, "nome": "João"},
    {"id": 2, "nome": "Maria"},
    {"id": 3, "nome": "José"}
]

materias = [
    {"cod": "M1", "nome": "Matemática"},
    {"cod": "M2", "nome": "Física"}
]

notas = [
    {"idAluno": 1, "materia": "M1", "nota": 8},
    {"idAluno": 1, "materia": "M2", "nota": 7},
    {"idAluno": 2, "materia": "M1", "nota": 9}
]

def alunoscommediamaiorouigualaoito(alunos, materias, notas):

    i = 0 
    soma = 0 
    quantidade = 0 
    resultado = []

    while i < len(alunos): 
        iddoaluno = alunos[i]["id"]
        nomedoaluno = alunos[i]["nome"]

        j = 0 
        while j < len(notas):
            if notas[j]["idAluno"] == iddoaluno:
                soma += notas[j]["nota"]
                quantidade += 1
                idmateria = notas[j]["materia"]
            j += 1

        k = 0 
        while k < len(materias): 
            if materias[k]["cod"] == idmateria: 
                nomemateria = materias[k]["nome"]
            k += 1

        if quantidade > 0: 

            media = soma / quantidade 

            if media >= 8: 
                resultado.append({
                    "Nome do aluno: ": nomedoaluno,
                    "Nome da materia: ": nomemateria,
                    "Media 8 ou mais: ": media
            })
        i += 1
    return resultado
print(alunoscommediamaiorouigualaoito(alunos, materias, notas))