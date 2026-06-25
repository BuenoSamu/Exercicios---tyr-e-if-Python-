aluno = [
{"ra":101, "nome":"Bruno"},
{"ra":102, "nome":"Julia"},
{"ra":103, "nome":"Renato"},
{"ra":104, "nome":"Paula"}
]

disciplina = [
{"cod":"D1", "nome":"Algoritmos"},
{"cod":"D2", "nome":"Banco de Dados"},
{"cod":"D3", "nome":"Redes"},
{"cod":"D4", "nome":"Web"}
]

matricula = [
{"ra":101, "disciplinas":["D1","D2"]},
{"ra":102, "disciplinas":["D3"]},
{"ra":103, "disciplinas":["D2","D4"]},
{"ra":104, "disciplinas":["D1"]}
]

def nomesAlunosComApenasUmaDisciplina(aluno, matricula, disciplina):

    i = 0
    resultado = []

    while i < len(aluno):
        ra = aluno[i]["ra"]
        nome = aluno[i]["nome"]

        j = 0
        while j < len(matricula):
            if matricula[j]["ra"] == ra:

                if len(matricula[j]["disciplinas"]) == 1:
                    cod = matricula[j]["disciplinas"][0]

                    k = 0
                    nome_disc = ""

                    while k < len(disciplina):
                        if disciplina[k]["cod"] == cod:
                            nome_disc = disciplina[k]["nome"]
                        k += 1

                    resultado.append({
                        "Nome": nome,
                        "Disciplina": nome_disc
                    })

            j += 1

        i += 1

    return resultado

print(nomesAlunosComApenasUmaDisciplina(aluno, matricula, disciplina))