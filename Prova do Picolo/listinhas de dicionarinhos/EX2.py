produto = [
    {"cod": "P1", "nome": "Teclado"},
    {"cod": "P2", "nome": "Mouse"},
    {"cod": "P3", "nome": "Monitor"},
    {"cod": "P4", "nome": "Notebook"}
]

loja = [
    {"id": 1, "nome": "Loja Centro"},
    {"id": 2, "nome": "Loja Shopping"}
]

venda = [
    {"idLoja": 1, "produtos": ["P1", "P2"]},
    {"idLoja": 2, "produtos": ["P3"]}
]

def produtosquenuncaforamvendidosemnenhumaloja(produto, venda): 

    i = 0 
    produtosencontrados = []
    resultado = []

    while i < len(venda): 
        
        j = 0
        while j < len(venda[i]["produtos"]): 
            cod = venda[j]["produtos"][i]

            if cod not in produtosencontrados: 
                produtosencontrados.append(cod)
            j += 1
        i += 1

    k = 0
    while k < len(produto): 
        if produto[k]["cod"] not in produtosencontrados: 
            nomedoprodutonuncavendidoemloja = produto[k]["nome"]
            resultado.append({"Nome do produto nunca vendido em loja: ": nomedoprodutonuncavendidoemloja})
        k += 1
    return resultado

print(produtosquenuncaforamvendidosemnenhumaloja(produto, venda))

