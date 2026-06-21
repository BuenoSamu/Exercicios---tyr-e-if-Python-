clientes = [
    {"id": 1, "nome": "Lucas"},
    {"id": 2, "nome": "Marina"},
    {"id": 3, "nome": "Pedro"},
    {"id": 4, "nome": "Juliana"},
    {"id": 5, "nome": "Carlos"}
]

contas = [
    {"idCliente": 1, "saldo": 150},
    {"idCliente": 2, "saldo": -50},
    {"idCliente": 3, "saldo": 0},
    {"idCliente": 4, "saldo": -120},
    {"idCliente": 5, "saldo": 80}
]

bancos = [
    {"idCliente": 1, "banco": "Banco A"},
    {"idCliente": 2, "banco": "Banco B"},
    {"idCliente": 3, "banco": "Banco C"},
    {"idCliente": 4, "banco": "Banco D"},
    {"idCliente": 5, "banco": "Banco E"}
]

def clientescomacontanegativada(clientes, contas, bancos):

    if len(clientes) == 0 or len(contas) == 0 or len(bancos) == 0: 
        return None
    
    i = 0 
    resultado = []

    while i < len(contas): 
        idcliente = contas[i]["idCliente"]
        saldocliente = contas[i]["saldo"]

        if saldocliente < 0: 
            j = 0 
            while j < len(clientes):
                if clientes[j]["id"] == idcliente:
                    nomecliente = clientes[j]["nome"]
                    break
                j +=1
            
            k = 0 
            while k < len(bancos): 
                if bancos[k]["idCliente"] == idcliente:
                    nomedobanco = bancos[k]["banco"]
                k += 1 

            if saldocliente is not None and nomecliente is not None and nomedobanco is not None: 
                    resultado.append({
                        "Cliente negativado": nomecliente,
                        "Saldo devedor": saldocliente,
                        "Banco": nomedobanco
                    })
        i += 1
    return resultado

print(clientescomacontanegativada(clientes, contas, bancos))