funcionarios = [
    {"id": 1, "nome": "Lucas"},
    {"id": 2, "nome": "Marina"},
    {"id": 3, "nome": "Pedro"},
    {"id": 4, "nome": "Juliana"}
]

setores = [
    {"idFuncionario": 1, "setor": "TI"},
    {"idFuncionario": 2, "setor": "RH"},
    {"idFuncionario": 3, "setor": "Financeiro"},
    {"idFuncionario": 4, "setor": "TI"}
]

afastamentos = [
    {"idFuncionario": 1, "dias": 10},
    {"idFuncionario": 2, "dias": 0},
    {"idFuncionario": 3, "dias": 5},
    {"idFuncionario": 4, "dias": 0}
]

def funcionariosafastados (funcionarios, setores, afastamentos):

    i = 0 
    resultado = [] 

    while i < len(afastamentos):
        
        idfuncionario = afastamentos[i]["idFuncionario"]
        diasafastado = afastamentos[i]["dias"]

        if diasafastado > 0: 

            j = 0 
            nomefuncionario = None
            while j < len(funcionarios):
                if funcionarios[j]["id"] == idfuncionario:
                    nomefuncionario = funcionarios[j]["nome"]
                    break
                j += 1

            k = 0 
            setorfuncionario = None
            while k < len(setores): 
                if setores[k]["idFuncionario"] == idfuncionario:
                    setorfuncionario = setores[k]["setor"]
                    break
                k += 1

            if nomefuncionario is not None and setorfuncionario is not None:
                resultado.append({
                 "Nome do funcionario": nomefuncionario,
                 "Setor funcionario": setorfuncionario,
                 "Dias afastado": diasafastado
             })
        i += 1 
    return resultado

print(funcionariosafastados(funcionarios, setores, afastamentos))


