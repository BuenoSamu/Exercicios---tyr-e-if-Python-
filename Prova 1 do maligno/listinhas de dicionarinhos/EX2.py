paciente = [
    {"cod": 10, "nome": "Ana", "nasc": "01/02/1990"},
    {"cod": 11, "nome": "Carlos", "nasc": "03/03/1992"},
    {"cod": 12, "nome": "Beatriz", "nasc": "04/04/1993"}
]

diagnostico = [
    {"ent": "01/01/2024", "sai": "05/01/2024", "cod": 10, "razao": ["R51", "F32.0"]},
    {"ent": "06/01/2024", "sai": "10/01/2024", "cod": 11, "razao": ["R51"]},
    {"ent": "11/01/2024", "sai": "15/01/2024", "cod": 10, "razao": ["J06.9", "R51"]},
]

internacao = [
    {"cod": 10, "dias": 5},
    {"cod": 11, "dias": 4},
    {"cod": 10, "dias": 3}
]

def mediadediasdeinternacaocommaisdeumadoenca(paciente, diagnostico, internacao): 

    i = 0
    qtd = 0
    soma = 0
    resultado = []

    while i < len(paciente): 
        idpaciente = paciente[i]["cod"]
        nomepaciente = paciente[i]["nome"]

        listainternacoes = []

        j = 0
        while j < len(diagnostico): 
            if diagnostico[j]["cod"] == idpaciente:

                if len(diagnostico[j]["razao"]) > 1:
                    if idpaciente not in listainternacoes:
                        listainternacoes.append(idpaciente)

            j += 1
        
        cont = 0
        l = 0 
        while l < len(internacao): 
            if internacao[l]["cod"] in listainternacoes:
                cont += internacao[l]["dias"] 
            l += 1

        if cont > 0:
            qtd += 1
            soma += cont
            media = soma / qtd

            resultado.append({
                "Nome do paciente": nomepaciente,
                "Dias de internação": cont,
                "Média atual": media
            })

        i += 1

    return resultado

print(mediadediasdeinternacaocommaisdeumadoenca(paciente, diagnostico, internacao))
                
