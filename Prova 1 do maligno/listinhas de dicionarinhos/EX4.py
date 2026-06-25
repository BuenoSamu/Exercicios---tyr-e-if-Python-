paciente = [
    {"cod": 1, "nome": "Lucas", "nasc": "10/10/1990"},
    {"cod": 2, "nome": "Marina", "nasc": "11/11/1991"},
    {"cod": 3, "nome": "João", "nasc": "12/12/1992"}
]

diagnostico = [
    {"ent": "01/01/2024", "sai": "05/01/2024", "cod": 1, "razao": ["R51"]},
    {"ent": "06/01/2024", "sai": "10/01/2024", "cod": 2, "razao": ["X99"]},
    {"ent": "11/01/2024", "sai": "15/01/2024", "cod": 1, "razao": ["R51", "F32.0"]}
]

internacao = [
    {"cod": 1, "dias": 10},
    {"cod": 2, "dias": 5},
    {"cod": 1, "dias": 7}
]

doenca = [
    {"cid": "R51", "desc": "Cefaleia"},
    {"cid": "F32.0", "desc": "Depressão"}
]

def mediainternacoescomdoencavalida(paciente, diagnostico, internacao, doenca):

    i = 0
    qtd = 0
    soma = 0
    resultado = []

    while i < len(paciente):

        idpaciente = paciente[i]["cod"]
        nomepaciente = paciente[i]["nome"]

        # Lista de CIDs válidos
        j = 0
        listadoencasexistentes = []

        while j < len(doenca):
            listadoencasexistentes.append(doenca[j]["cid"])
            j += 1

        possuidoencavalida = False

        # Verifica se o paciente tem algum diagnóstico com CID válida
        k = 0
        while k < len(diagnostico):

            if diagnostico[k]["cod"] == idpaciente:

                x = 0
                while x < len(diagnostico[k]["razao"]):

                    if diagnostico[k]["razao"][x] in listadoencasexistentes:
                        possuidoencavalida = True

                    x += 1

            k += 1

        # Soma os dias de internação do paciente
        if possuidoencavalida:

            qtd += 1

            l = 0
            cont = 0

            while l < len(internacao):

                if internacao[l]["cod"] == idpaciente:
                    cont += internacao[l]["dias"]

                l += 1

            soma += cont
            media = soma / qtd

            resultado.append({
                "Nome": nomepaciente,
                "Dias Internados": cont,
                "Media": media
            })

        i += 1

    return resultado

print(mediainternacoescomdoencavalida(paciente, diagnostico, internacao, doenca))
    
                
