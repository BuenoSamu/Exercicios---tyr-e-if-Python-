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
    # 2024001 -> reprovou em 1 matéria
    {"ra": "2024001", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 8.7, "freq": 92},
    {"ra": "2024001", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 3.9, "freq": 88},  
    {"ra": "2024001", "cod": "HIS103", "sem": 1, "ano": 2026, "nota": 7.5, "freq": 90},
    {"ra": "2024001", "cod": "QUI104", "sem": 1, "ano": 2026, "nota": 6.8, "freq": 85},

    # 2024002 -> aprovado em tudo
    {"ra": "2024002", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 9.1, "freq": 95},
    {"ra": "2024002", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 8.0, "freq": 84},
    {"ra": "2024002", "cod": "HIS103", "sem": 1, "ano": 2026, "nota": 7.2, "freq": 88},
    {"ra": "2024002", "cod": "QUI104", "sem": 1, "ano": 2026, "nota": 6.0, "freq": 80},

    # 2024003 -> reprovou em quase tudo (só 1 aprovação)
    {"ra": "2024003", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 4.0, "freq": 60},
    {"ra": "2024003", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 3.5, "freq": 70},
    {"ra": "2024003", "cod": "HIS103", "sem": 1, "ano": 2026, "nota": 7.2, "freq": 80},  
    {"ra": "2024003", "cod": "QUI104", "sem": 2, "ano": 2026, "nota": 3.0, "freq": 65},

    # 2024004 -> reprovou em tudo
    {"ra": "2024004", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 2.5, "freq": 50},
    {"ra": "2024004", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 4.2, "freq": 60},
    {"ra": "2024004", "cod": "HIS103", "sem": 1, "ano": 2026, "nota": 3.9, "freq": 40},
    {"ra": "2024004", "cod": "QUI104", "sem": 2, "ano": 2026, "nota": 1.8, "freq": 55}
]

def alunosquereprovarampelomenosumavez(alunos, disciplinas, resultados):
    if len(alunos) == 0 or len(disciplinas) == 0 or len(resultados) == 0:
        return None

    nomes = []
    i = 0

    while i < len(alunos):
        ra_aluno = alunos[i]["ra"]
        total_reprovado = 0

        j = 0
        while j < len(resultados):
            if resultados[j]["ra"] == ra_aluno:
                if resultados[j]["nota"] < 5 or resultados[j]["freq"] < 75:
                    total_reprovado += 1
            j += 1

        if total_reprovado >= 1:
            nomes.append(alunos[i]["nome"])

        i += 1

    if len(nomes) == 0:
        return None

    return nomes

print(alunosquereprovarampelomenosumavez(alunos, disciplinas, resultados))


