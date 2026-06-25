cliente = [
{"id":1, "nome":"João"},
{"id":2, "nome":"Amanda"},
{"id":3, "nome":"Ricardo"},
{"id":4, "nome":"Bianca"}
]

produto = [
{"cod":"P1", "nome":"Notebook", "categoria":"Eletrônicos"},
{"cod":"P2", "nome":"Camiseta", "categoria":"Roupas"},
{"cod":"P3", "nome":"Celular", "categoria":"Eletrônicos"},
{"cod":"P4", "nome":"Tênis", "categoria":"Calçados"}
]

pedidos = [
{"id":1, "produtos":["P1","P2"]},
{"id":2, "produtos":["P2","P4"]},
{"id":3, "produtos":["P3"]},
{"id":4, "produtos":["P4"]}
]

def nomesClientesQueNuncaCompraramCategoria(cliente, produto, pedido, categoria):

    i = 0
    resultado = []

    while i < len(cliente):
        idcliente = cliente[i]["id"]
        nomecliente = cliente[i]["nome"]

        produtos_cliente = []

        j = 0
        while j < len(pedido):
            if pedido[j]["id"] == idcliente:
                produtos_cliente = pedido[j]["produtos"]
            j += 1

        categorias_cliente = []
        k = 0
        while k < len(produtos_cliente):
            cod_prod = produtos_cliente[k]
            l = 0
            while l < len(produto):
                if produto[l]["cod"] == cod_prod:
                    categorias_cliente.append(produto[l]["categoria"])
                l += 1

            k += 1

        if categoria not in categorias_cliente:
            resultado.append({
                "Cliente": nomecliente,
                "Status": "Nunca comprou essa categoria"
            })

        i += 1
    return resultado
print(nomesClientesQueNuncaCompraramCategoria(cliente, produto, pedidos, "Eletrônicos"))
           
                
                
