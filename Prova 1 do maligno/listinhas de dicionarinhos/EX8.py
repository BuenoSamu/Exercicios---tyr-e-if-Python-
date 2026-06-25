paciente = [
    {"cod":101, "nome":"Carlos Lima", "nasc":"10/03/1990"},
    {"cod":102, "nome":"Maria Souza", "nasc":"22/08/1985"},
    {"cod":103, "nome":"Pedro Alves", "nasc":"15/01/1990"},
    {"cod":104, "nome":"Juliana Costa", "nasc":"30/07/2000"}
]

doenca = [
    {"cid":"F32.0", "desc":"Episódio depressivo leve"},
    {"cid":"R51", "desc":"Cefaleia"},
    {"cid":"J06.9", "desc":"Infecção respiratória aguda"},
    {"cid":"I10", "desc":"Hipertensão essencial"}
]

diagnostico = [
    {"ent":"01/02/2024", "sai":"05/02/2024", "cod":101, "razao":["R51"]},
    {"ent":"10/03/2024", "sai":"20/03/2024", "cod":101, "razao":["I10","R51"]},
    {"ent":"15/04/2024", "sai":"18/04/2024", "cod":102, "razao":["F32.0"]},
    {"ent":"10/06/2024", "sai":"15/06/2024", "cod":102, "razao":["F32.0"]},
    {"ent":"10/06/2024", "sai":"15/06/2024", "cod":102, "razao":["F32.0"]},
    {"ent":"20/05/2024", "sai":"30/05/2024", "cod":103, "razao":["J06.9"]}
]

def mediaInternacoesPacientesComDoencaExclusiva(paciente, diagnostico, doenca):

    resultado = []

    i = 0
    while i < len(paciente):

        iddopaciente = paciente[i]["cod"]
        nomedopaciente = paciente[i]["nome"]

        qtdInternacoes = 0
        possuiDoencaExclusiva = False

        j = 0
        while j < len(diagnostico):

            if diagnostico[j]["cod"] == iddopaciente:

                qtdInternacoes += 1

                l = 0
                while l < len(diagnostico[j]["razao"]):

                    cid = diagnostico[j]["razao"][l]

                    pacientesComCid = []

                    k = 0
                    while k < len(diagnostico):

                        if cid in diagnostico[k]["razao"]:

                            cod = diagnostico[k]["cod"]

                            if cod not in pacientesComCid:
                                pacientesComCid.append(cod)

                        k += 1

                    if len(pacientesComCid) == 1:
                        possuiDoencaExclusiva = True

                    l += 1

            j += 1

        if possuiDoencaExclusiva:

            resultado.append({
                "Paciente": nomedopaciente,
                "Quantidade de internacoes": qtdInternacoes
            })

        i += 1

    return resultado


print(mediaInternacoesPacientesComDoencaExclusiva(paciente, diagnostico, doenca))
        

