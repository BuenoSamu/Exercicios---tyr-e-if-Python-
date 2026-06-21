clientes = [
    {"id": 10, "nome": "Bianca", "cidade": "SP"},
    {"id": 11, "nome": "Caio", "cidade": "RJ"},
    {"id": 12, "nome": "Duda", "cidade": "BH"},
    {"id": 13, "nome": "Enzo", "cidade": "SP"}
]

produtos = [
    {"cod": "P1", "nome": "Mouse", "preco": 80},
    {"cod": "P2", "nome": "Teclado", "preco": 120},
    {"cod": "P3", "nome": "Monitor", "preco": 900},
    {"cod": "P4", "nome": "Headset", "preco": 250}
]

pedidos = [
    {"idCliente": 10, "codProduto": "P1", "qtd": 1, "pago": True},
    {"idCliente": 10, "codProduto": "P3", "qtd": 1, "pago": False},
    {"idCliente": 11, "codProduto": "P2", "qtd": 2, "pago": True},
    {"idCliente": 12, "codProduto": "P4", "qtd": 1, "pago": False},
    {"idCliente": 13, "codProduto": "P1", "qtd": 3, "pago": True}
]

def clientescomumpedidonaopago (clientes, produtos, pedidos):

    if len(clientes) == 0 or len(produtos) == 0 or len(pedidos) == 0: 
        return None
    
    i = 0
    idclientedevendo = []
    idprodutoquetadevendo = []
    nomeprodutoquetadevendo = []
    nomeclientedevendo = []

    while i < len(pedidos):
        if pedidos[i]["pago"] == False:
            idclientedevendo.append(pedidos[i]["idCliente"])
            idprodutoquetadevendo.append(pedidos[i]["codProduto"])
        i += 1

    j = 0 
    while j < len(produtos):
        if produtos[j]["cod"] in idprodutoquetadevendo:
            nomeprodutoquetadevendo.append(produtos[j]["nome"])
        j += 1
        
    k = 0
    while k < len(clientes):
        if clientes[k]["id"] in idclientedevendo:
            nomeclientedevendo.append(clientes[k]["nome"])
        k += 1
   
    return nomeclientedevendo, nomeprodutoquetadevendo

print(clientescomumpedidonaopago(clientes, produtos, pedidos))