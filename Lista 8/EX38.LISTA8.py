clientes = [
    {"id": 1, "nome": "João", "estado": "SP"},
    {"id": 2, "nome": "Maria", "estado": "RJ"},
    {"id": 3, "nome": "Lucas", "estado": "SP"}
]

produtos = [
    {"cod": "P1", "nome": "Mouse"},
    {"cod": "P2", "nome": "Teclado"},
    {"cod": "P3", "nome": "Monitor"}
]

pedidos = [
    {"cliente": 1, "itens": ["P1"]},
    {"cliente": 1, "itens": ["P2", "P3"]},
    {"cliente": 3, "itens": ["P1"]},
    {"cliente": 3, "itens": ["P2"]}
]

def mediaPedidosUmItem(clientes, pedidos, estado):

    qtd = 0 
    soma = 0 

    i = 0 

    while i < len(clientes):

        idcliente = clientes[i]["id"]

        if clientes[i]["estado"] == estado:

            qtd += 1 
            cont = 0 

            j = 0 
            while j < len(pedidos):
                if pedidos[j]["cliente"] == idcliente:
                    if len(pedidos[i]["itens"]) == 1:
                        cont += 1 
                j += 1

            soma += cont 
            media = soma / qtd

        i += 1
    return media

print(mediaPedidosUmItem(clientes, pedidos, "SP"))