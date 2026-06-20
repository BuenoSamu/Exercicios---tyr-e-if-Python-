alunos = [
    {"ra": "2024001", "nome": "Ana Souza", "cel": "(11) 91234-5678", "email": "ana.souza@exemplo.com"},
    {"ra": "2024002", "nome": "Bruno Lima", "cel": "(11) 92345-6789", "email": "bruno.lima@exemplo.com"},
    {"ra": "2024003", "nome": "Carla Mendes", "cel": "(11) 93456-7890", "email": "carla.mendes@exemplo.com"},
    {"ra": "2024004", "nome": "Diego Rocha", "cel": "(11) 94567-8901", "email": "diego.rocha@exemplo.com"}
]

disciplinas = [
    {"cod": "MAT101", "nome": "Matematica", "qaSem": 4},
    {"cod": "FIS102", "nome": "Fisica", "qaSem": 3},
    {"cod": "HIS103", "nome": "Historia", "qaSem": 2},
    {"cod": "QUI104", "nome": "Quimica", "qaSem": 3}
]

resultados = [
    {"ra": "2024001", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 8.7, "freq": 92},
    {"ra": "2024001", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 3.9, "freq": 88},
    {"ra": "2024002", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 9.1, "freq": 95},
    # aluno 2024003: reprovado em quase tudo, aprovado em 1 matéria (HIS103)
    {"ra": "2024003", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 4.0, "freq": 60},
    {"ra": "2024003", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 3.5, "freq": 70},
    {"ra": "2024003", "cod": "HIS103", "sem": 1, "ano": 2026, "nota": 7.2, "freq": 80},
    {"ra": "2024003", "cod": "QUI104", "sem": 2, "ano": 2026, "nota": 3.0, "freq": 65},
    # aluno 2024004: reprovado em TODAS
    {"ra": "2024004", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 2.5, "freq": 50},
    {"ra": "2024004", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 4.2, "freq": 60},
    {"ra": "2024004", "cod": "HIS103", "sem": 1, "ano": 2026, "nota": 3.9, "freq": 40},
    {"ra": "2024004", "cod": "QUI104", "sem": 2, "ano": 2026, "nota": 1.8, "freq": 55}
]

def alunoreprovadoemtudo(alunos, disciplinas, resultados):
    if len(disciplinas) == 0 or len(resultados) == 0 or len(alunos) == 0:
        return None

    i = 0
    while i < len(resultados):
        raaluno = resultados[i]["ra"]

        totalcursado = 0
        totalreprovado = 0

        j = 0
        while j < len(resultados):
            if resultados[j]["ra"] == raaluno:
                totalcursado += 1
                if resultados[j]["nota"] < 5 or resultados[j]["freq"] < 75:
                    totalreprovado += 1
            j += 1

        if totalcursado > 0 and totalcursado == totalreprovado:
            k = 0
            while k < len(alunos):
                if alunos[k]["ra"] == raaluno:
                    return alunos[k]["nome"], alunos[k]["email"]
                k += 1

        i += 1

    return []

print(alunoreprovadoemtudo(alunos, disciplinas, resultados))