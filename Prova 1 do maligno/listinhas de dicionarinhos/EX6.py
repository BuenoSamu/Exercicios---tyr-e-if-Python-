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

def converterDias(data):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    return (ano * 360) + (mes * 30) + dia

def mediaDiasInternacaoPacientesComDoenca(paciente, diagnostico, doenca):

    i = 0
    resultado = []

    while i < len(paciente):

        idpaciente = paciente[i]["cod"]
        nomepaciente = paciente[i]["nome"]

        k = 0
        listadoencas = []
        while k < len(doenca):
            listadoencas.append(doenca[k]["cid"])
            k += 1

        j = 0
        soma = 0
        qtd = 0

        while j < len(diagnostico):
            if diagnostico[j]["cod"] == idpaciente:
                tem_doenca = False
                r = 0
                while r < len(diagnostico[j]["razao"]):
                    if diagnostico[j]["razao"][r] in listadoencas:
                        tem_doenca = True
                    r += 1
                if tem_doenca:
                    entrada = converterDias(diagnostico[j]["ent"])
                    saida = converterDias(diagnostico[j]["sai"])

                    dias = saida - entrada
                    soma += dias
                    qtd += 1
            j += 1
            
        if qtd > 0:
            media = soma / qtd
            resultado.append({
                "nome": nomepaciente,
                "media": media
            })

        i += 1

    return resultado
print(mediaDiasInternacaoPacientesComDoenca(paciente,diagnostico, doenca))
    

        


