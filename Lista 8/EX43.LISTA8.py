clientes = [
    {"id": 1, "nome": "Carlos"},
    {"id": 2, "nome": "Fernanda"}
]

produtos = [
    {"cod": "P1", "nome": "Mouse"},
    {"cod": "P2", "nome": "Teclado"}
]

compras = [
    {"idCliente": 1, "produtos": ["P1", "P2"]},
    {"idCliente": 2, "produtos": ["P2"]}
]

def clientequecompraramapenasumproduto(clientes, produtos, compras): 

    resultado = [] 
    i = 0 
    

    while i < len(compras): 
        iddocliente = compras[i]["idCliente"]
        listaprodutos = compras[i]["produtos"]

        nomedocliente = None 
        nomedoproduto = None 
        if len(listaprodutos) == 1: 

            j = 0 
            while j < len(clientes): 
                if clientes[j]["id"] == iddocliente: 
                    nomedocliente = clientes[j]["nome"]
                j += 1 
            
            k = 0 
            while k < len(produtos): 
                if listaprodutos[0] == produtos[k]["cod"]: 
                    nomedoproduto = produtos[k]["nome"]
                k += 1
            
            if nomedocliente and nomedoproduto: 
                resultado.append({
                    "Nome do cliente: ": nomedocliente,
                    "Nome do produto: ": nomedoproduto,
                })
        i += 1
    return resultado
print(clientequecompraramapenasumproduto(clientes, produtos, compras))