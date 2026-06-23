funcionario = [
    {"id": 100, "nome": "Carlos", "idDept": 1},
    {"id": 101, "nome": "Patrícia", "idDept": 2},
    {"id": 102, "nome": "Rafael", "idDept": 1},
    {"id": 103, "nome": "Bianca", "idDept": 3}
]

departamento = [
    {"id": 1, "nome": "TI"},
    {"id": 2, "nome": "RH"},
    {"id": 3, "nome": "Financeiro"}
]

projeto = [
    {"idProjeto": 1, "funcionarios": [100, 102]},
    {"idProjeto": 2, "funcionarios": [101]}
]

def departamentosemfuncionarioscomprojetos(funcionario, departamento, projeto):

    funcionarios_em_projeto = []
    resultado = []

    i = 0
    while i < len(projeto):

        j = 0
        while j < len(projeto[i]["funcionarios"]):

            idfunc = projeto[i]["funcionarios"][j]

            if idfunc not in funcionarios_em_projeto:
                funcionarios_em_projeto.append(idfunc)
            j += 1
        i += 1

    k = 0
    while k < len(funcionario):

        if funcionario[k]["id"] not in funcionarios_em_projeto:

            iddep = funcionario[k]["idDept"]
            d = 0
            nomedep = None
            while d < len(departamento):

                if departamento[d]["id"] == iddep:
                    nomedep = departamento[d]["nome"]
                    break
                d += 1

            resultado.append({
                "Nome do funcionario sem projeto": funcionario[k]["nome"],
                "Departamento": nomedep
            })
        k += 1

    return resultado
print(departamentosemfuncionarioscomprojetos(funcionario, departamento, projeto))

        

    