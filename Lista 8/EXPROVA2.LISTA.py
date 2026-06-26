paciente = [
    {"id": 123, "nome": "João da Silva", "dataNasc": "19/12/1992"},
    {"id": 234, "nome": "Ana Souza", "dataNasc": "29/11/2000"},
    {"id": 345, "nome": "Carlos Mendes", "dataNasc": "15/03/1985"},
    {"id": 456, "nome": "Mariana Costa", "dataNasc": "07/08/1995"}
]

doenca = [
    {"cod": "F32.0", "nome": "Episódio depressivo leve"},
    {"cod": "R51", "nome": "Cefaleia"},
    {"cod": "J06.9", "nome": "Infecção respiratória aguda não especificada"},
    {"cod": "E11.9", "nome": "Diabetes mellitus tipo 2"}
]

internacao = [
    {"dataEnt": "01/10/2020", "dataSai": "07/10/2020", "idPaciente": 123, "codDoenca": ["F32.0"]},
    {"dataEnt": "12/02/2023", "dataSai": "15/02/2023", "idPaciente": 234, "codDoenca": ["R51"]},
    {"dataEnt": "22/06/2024", "dataSai": "29/06/2024", "idPaciente": 123, "codDoenca": ["J06.9"]},
    {"dataEnt": "05/11/2023", "dataSai": "12/11/2023", "idPaciente": 345, "codDoenca": ["E11.9", "R51"]},
    {"dataEnt": "18/03/2024", "dataSai": "25/03/2024", "idPaciente": 456, "codDoenca": ["F32.0", "J06.9"]}
]

def mediadedoencasdepacientescombasenodiaquenasceu(paciente, internacao, data):

    if len(paciente) == 0 or len(internacao) == 0: 
        return None
    
    qtd = 0 
    soma = 0 
    resultado = []
    i = 0 

    while i < len(paciente):
        idpaciente = paciente[i]["id"]
        if paciente[i]["dataNasc"] == data:
            qtd += 1
            cont = 0 
            nomepaciente = paciente[i]["nome"]

            j = 0 
            while j < len(internacao): 
                if internacao[j]["idPaciente"] == idpaciente:
                    if len(internacao[j]["codDoenca"]) == 1: 
                        cont += 1
                j += 1
            
            soma += cont
        i +=1 

        if qtd == 0: 
            return None

        media = soma / qtd 

        if nomepaciente is not None and media is not None:
            resultado.append({
                "Nome do paciente: ": nomepaciente,
                "Media: ": media
            })

    return resultado

print(mediadedoencasdepacientescombasenodiaquenasceu(paciente, internacao, "19/12/1992"))
