medicos = [
    {"id": 1, "nome": "Dr. Paulo"},
    {"id": 2, "nome": "Dra. Carla"},
    {"id": 3, "nome": "Dr. Felipe"},
    {"id": 4, "nome": "Dra. Ana"}
]

especialidades = [
    {"cod": "C01", "nome": "Cardiologia"},
    {"cod": "O01", "nome": "Ortopedia"},
    {"cod": "P01", "nome": "Pediatria"},
    {"cod": "D01", "nome": "Dermatologia"}
]

consultas = [
    {"idMedico": 1, "especialidades": ["C01"]},
    {"idMedico": 2, "especialidades": ["P01", "D01"]},
    {"idMedico": 3, "especialidades": ["O01"]},
    {"idMedico": 4, "especialidades": ["P01"]}
]

def medicosatendempediatria (medicos, especialidades, consultas):

    if len(medicos) == 0 or len(especialidades) == 0 or len(consultas) == 0:
        return None 

    i = 0
    pediatras = []

    while i < len(consultas):
        idmedico = consultas[i]["idMedico"]
        listaespecialidades = consultas[i]["especialidades"]

        if "P01" in listaespecialidades:

            j = 0 
            nomemedico = None
            while j < len(medicos):
                if medicos[j]["id"] == idmedico:
                    nomemedico = medicos[j]["nome"]
                j +=1

                k = 0 
                nomeespecialidade = None 
                while k < len(especialidades): 
                    if especialidades[k]["cod"] == "P01":
                        nomeespecialidade = especialidades[k]["nome"]
                    k += 1
            
            if nomeespecialidade is not None and nomemedico is not None: 
                pediatras.append({
                    "Medico": nomemedico,
                    "Especialidade": nomeespecialidade
                })
    i += 1
    return pediatras

print(medicosatendempediatria(medicos, especialidades, consultas))

    

            