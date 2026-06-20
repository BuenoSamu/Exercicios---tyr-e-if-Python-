alunos = [
    {"ra": "2024001", "nome": "Ana Souza", "cel": "(11) 91234-5678", "email": "ana.souza@exemplo.com"},
    {"ra": "2024002", "nome": "Bruno Lima", "cel": "(11) 92345-6789", "email": "bruno.lima@exemplo.com"},
    {"ra": "2024003", "nome": "Carla Mendes", "cel": "(11) 93456-7890", "email": "carla.mendes@exemplo.com"}
]

disciplinas = [
    {"cod": "MAT101", "nome": "Matematica", "qaSem": 4},
    {"cod": "FIS102", "nome": "Fisica", "qaSem": 3},
    {"cod": "HIS103", "nome": "Historia", "qaSem": 2},
    {"cod": "QUI104", "nome": "Quimica", "qaSem": 3}
]

resultados = [
    {"ra": "2024001", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 8.7, "freq": 92},
    {"ra": "2024001", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 7.9, "freq": 88},
    {"ra": "2024002", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 9.1, "freq": 95},
    {"ra": "2024003", "cod": "HIS103", "sem": 1, "ano": 2026, "nota": 6.8, "freq": 1},
    {"ra": "2024003", "cod": "QUI104", "sem": 2, "ano": 2026, "nota": 8.0, "freq": 85}
]

def alunocommenorfrequencia (alunos,disciplinas,resultados):

    if len(alunos) == 0 or len(disciplinas) == 0 or len(resultados) == 0:
        return None
    
    i = 0
    menorfrequencia = resultados[0]["freq"]
    menorra = resultados[0]["ra"]

    while i < len(resultados):
        if resultados[i]["freq"] < menorfrequencia:
            menorfrequencia = resultados[i]["freq"]
            menorra = resultados[i]["ra"]
        i += 1
    
    j = 0 
    nomealuno = None

    while j < len(alunos):
        if alunos[j]["ra"] == menorra:
            nomealuno = alunos[j]["nome"]
        j+=1
    return nomealuno, menorfrequencia

print(alunocommenorfrequencia(alunos, disciplinas, resultados))