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

def mediadiagnosticoscomdata(paciente, diagnostico, doenca, data): 

    i = 0 
    qtd = 0
    soma = 0 
    resultado = [] 
    


