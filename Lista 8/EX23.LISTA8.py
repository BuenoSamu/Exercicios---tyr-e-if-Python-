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
    {"ra": "2024001", "cod": "FIS102", "sem": 1, "ano": 2026, "nota": 3.9, "freq": 88},
    {"ra": "2024002", "cod": "MAT101", "sem": 1, "ano": 2026, "nota": 9.1, "freq": 95},
    {"ra": "2024003", "cod": "HIS103", "sem": 1, "ano": 2026, "nota": 3.8, "freq": 1},
    {"ra": "2024003", "cod": "QUI104", "sem": 2, "ano": 2026, "nota": 3.0, "freq": 85}
]

def materiaquenuncareprovouninguem(alunos, disciplinas, resultados):
    # Se alguma lista estiver vazia, não dá para analisar
    if len(alunos) == 0 or len(disciplinas) == 0 or len(resultados) == 0:
        return None

    # Lista que vai guardar os nomes das matérias sem reprovação
    materias_ok = []
    i = 0

    # Percorre todas as disciplinas
    while i < len(disciplinas):
        cod = disciplinas[i]["cod"]    # código da disciplina atual
        nome = disciplinas[i]["nome"]  # nome da disciplina atual

        j = 0
        teve_reprovado = False          # controla se alguém reprovou nessa disciplina
        apareceu_em_resultados = False  # controla se essa disciplina apareceu em resultados

        # Percorre todos os resultados para verificar essa disciplina
        while j < len(resultados):
            # Se o resultado é da disciplina atual
            if resultados[j]["cod"] == cod:
                apareceu_em_resultados = True

                # Regra de reprovação: nota < 5 OU frequência < 75
                if resultados[j]["nota"] < 5.0 or resultados[j]["freq"] < 75:
                    teve_reprovado = True
                    break  # já achou reprovação, pode parar de olhar essa disciplina
            j += 1

        # Só adiciona a matéria se:
        # 1) apareceu em resultados
        # 2) não teve nenhum reprovado
        if apareceu_em_resultados and not teve_reprovado:
            materias_ok.append(nome)

        i += 1

    # Se nenhuma matéria passou no critério, retorna None
    if len(materias_ok) == 0:
        return None

    # Retorna lista com nomes das matérias que nunca reprovaram ninguém
    return materias_ok

print(materiaquenuncareprovouninguem(alunos, disciplinas, resultados))