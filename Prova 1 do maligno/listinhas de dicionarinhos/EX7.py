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
    {"ent":"20/05/2024", "sai":"30/05/2024", "cod":103, "razao":["J06.9"]},
    {"ent":"01/06/2024", "sai":"08/06/2024", "cod":103, "razao":["R51"]},
    {"ent":"10/06/2024", "sai":"15/06/2024", "cod":104, "razao":["I10"]},
]


def mediaQuantidadeDoencasPorDiagnosticoDosPacientesNascEmMes(paciente, diagnostico, doenca, data):

    i = 0
    resultado = [] 

    while i < len(paciente):
        idpaciente = paciente[i]["cod"]
        nomepaciente = paciente[i]["nome"]

        if paciente[i]["nasc"] == data: 

            j = 0
            listadoencas = []
            while j < len(doenca): 
                listadoencas.append(doenca[j]["cid"])
                nomedoenca = doenca[j]["desc"]
                j += 1

            k = 0
            qtd = 0 
            soma = 0 

            while k < len(diagnostico): 
                if diagnostico[k]["cod"] == idpaciente: 
                    qtd += 1 
                    cont = 0
                    l = 0 
                    while l < len(diagnostico[k]["razao"]): 
                        if diagnostico[k]["razao"][l] in listadoencas: 
                            cont += 1
                        l += 1
                k += 1
        i += 1

        soma += cont 
        media = soma / qtd 

        if nomepaciente is not None and media is not None: 
            resultado.append({"Nome do paciente: ": nomepaciente,"Nome da doenca: ": nomedoenca, "Media de doencas: ":media})

    return resultado
print(mediaQuantidadeDoencasPorDiagnosticoDosPacientesNascEmMes(paciente, diagnostico, doenca, "10/03/1990"))

                


            