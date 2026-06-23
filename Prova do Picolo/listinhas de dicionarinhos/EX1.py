medicos = [
    {"id": 1, "nome": "Dr. Roberto"},
    {"id": 2, "nome": "Dra. Fernanda"},
    {"id": 3, "nome": "Dr. Paulo"},
    {"id": 4, "nome": "Dra. Juliana"}
]

paciente = [
    {"id": 101, "nome": "Lucas"},
    {"id": 102, "nome": "Marina"},
    {"id": 103, "nome": "João"}
]

consulta = [
    {"idMedico": 1, "idPaciente": 101},
    {"idMedico": 2, "idPaciente": 102},
    {"idMedico": 1, "idPaciente": 103}
]

def medicosquenuncaatenderamnenhumpaciente(medicos,consulta): 

   
    resultado = [] 
    medicosencontrados  = [] 
    i = 0 

    while i < len(consulta):
         
        idmedico = consulta[i]["idMedico"]
        if idmedico not in medicosencontrados: 
            medicosencontrados.append(consulta[i]["idMedico"])
        i += 1

    j = 0 
    while j < len(medicos): 
        if medicos[j]["id"] not in medicosencontrados:
            nomemedicos = medicos[j]["nome"]
            resultado.append({
                "Nome do medico que nao tem paciente: ": nomemedicos
            })
        j += 1
        
    return resultado
print(medicosquenuncaatenderamnenhumpaciente(medicos, consulta))

            