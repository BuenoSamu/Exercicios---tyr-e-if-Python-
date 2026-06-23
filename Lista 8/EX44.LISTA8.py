medicos = [
    {"id": 1, "nome": "Dr. Paulo"},
    {"id": 2, "nome": "Dra. Julia"}
]

pacientes = [
    {"id": 10, "nome": "Rafael"},
    {"id": 11, "nome": "Bianca"}
]

consultas = [
    {"idMedico": 1, "idPaciente": 10, "doenca": "cancer"},
    {"idMedico": 2, "idPaciente": 11, "doenca": "tosse"},
    {"idMedico": 1, "idPaciente": 11, "doenca": "broxa"}
]

def medicocommaisdeumpaciente(medicos, pacientes, consultas): 

    i = 0
    resultado = []
    while i < len(medicos):
        qtd = 0
        idmedico = medicos[i]["id"]
        nomedomedico = medicos[i]["nome"]

        j = 0 
        listapacientes = []
        while j < len(consultas):
            if consultas[j]["idMedico"] == idmedico:
                qtd += 1
                listapacientes.append(consultas[j]["idPaciente"])
            j += 1
        
        k = 0
        nomespacientes = []
        while k < len(pacientes): 
            if pacientes[k]["id"] in listapacientes:
                nomespacientes.append(pacientes[k]["nome"])
            k +=1 
        
        if qtd > 1: 
            resultado.append({
                "Nome do medico: ": nomedomedico,
                "Nome do paciente: ": nomespacientes,
                "Quantidade de pacientes": qtd
            })
        i += 1
    return resultado
print(medicocommaisdeumpaciente(medicos, pacientes, consultas))


