paciente = [
    {"cod": 1, "nome": "Lucas", "nasc": "01/01/1980"},
    {"cod": 2, "nome": "Marina", "nasc": "01/01/2000"},
    {"cod": 3, "nome": "João", "nasc": "01/01/1985"}
]

diagnostico = [
    {"ent": "01/01/2024", "sai": "02/01/2024", "cod": 1, "razao": ["F32.0"]},
    {"ent": "03/01/2024", "sai": "04/01/2024", "cod": 2, "razao": ["R51"]},
    {"ent": "05/01/2024", "sai": "06/01/2024", "cod": 1, "razao": ["R51"]}
]

doenca = [
    {"cid": "R51", "desc": "Cefaleia"},
    {"cid": "F32.0", "desc": "Depressao 2"}
]

def mediadiagnosticosantesdadataX (paciente, diagnostico,data): 

    i = 0
    qtd = 0
    soma = 0
    resultado = []

    while i < len(paciente): 
        idpaciente = paciente[i]["cod"]
        nomepaciente = paciente[i]["nome"]
        if paciente[i]["nasc"] < data:
            
                qtd += 1

                j = 0
                cont = 0
                listadiagnosticos = []
                while j < len(diagnostico): 
                 if diagnostico[j]["cod"] == idpaciente:
                   if len(diagnostico[j]["razao"]) == 1: 
                       listadiagnosticos.append(idpaciente)
                 j += 1

                cont += len(listadiagnosticos)
                soma += cont 
                media = soma / qtd

                resultado.append({"Nome: ": nomepaciente,
                                  "Media: ": media})
        else: 
            print("Nasceu depois da data informada")
        i += 1
       
    return resultado
print(mediadiagnosticosantesdadataX(paciente, diagnostico, "01/01/1990"))




