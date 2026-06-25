paciente = [
    {"cod": 1, "nome": "Lucas", "nasc": "10/01/1990"},
    {"cod": 2, "nome": "Marina", "nasc": "10/01/1990"},
    {"cod": 3, "nome": "João", "nasc": "05/05/1985"}
]

diagnostico = [
    {"ent": "01/01/2024", "sai": "02/01/2024", "cod": 1, "razao": ["R51"]},
    {"ent": "03/01/2024", "sai": "04/01/2024", "cod": 2, "razao": ["F32.0"]},
    {"ent": "05/01/2024", "sai": "06/01/2024", "cod": 1, "razao": ["J06.9", "R51"]},
    {"ent": "07/01/2024", "sai": "08/01/2024", "cod": 3, "razao": ["R51"]}
]

doenca = [
    {"cid": "R51", "desc": "Cefaleia"},
    {"cid": "F32.0", "desc": "Depressão leve"},
    {"cid": "J06.9", "desc": "Infecção respiratória"}
]

def mediadiagnosticoscomdata(paciente, diagnostico, data): 

    qtd = 0 
    soma = 0 
    i = 0
    resultado = []
    listadoencas = []

    while i < len(paciente): 
        idpaciente = paciente[i]["cod"]
        if paciente[i]["nasc"] == data: 
            qtd += 1
            cont = 0 
            nomepaciente = paciente[i]["nome"]

            j = 0
            while j < len(diagnostico): 
                if diagnostico[j]["cod"] == idpaciente: 
                    k = 0 
                    while k < len(diagnostico[j]["razao"]):
                        coddoenca = diagnostico[j]["razao"][k]
                        if len(diagnostico[j]["razao"]) == 1:
                            listadoencas.append(coddoenca)
                            cont += 1
                        k += 1
                j += 1
            
            l = 0 
            while l < len(doenca): 
                if doenca[l]["cid"] in listadoencas: 
                    nomedoenca = doenca[l]["desc"]
                l += 1

            if qtd == 0: 
                return None
            
            soma += cont
            media = soma / qtd

            if media is not None and nomepaciente is not None: 
                resultado.append({"Nome do paciente: ": nomepaciente,
                                  "Media de diagnosticos: ": media,
                                  "Descrição da doenca: ": nomedoenca})
        i += 1
    return resultado
print(mediadiagnosticoscomdata(paciente, diagnostico, "10/01/1990"))




        




