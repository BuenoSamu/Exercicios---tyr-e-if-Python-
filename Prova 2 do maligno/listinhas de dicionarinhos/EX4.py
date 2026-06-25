cliente = [
{"id":1, "nome":"Diego"},
{"id":2, "nome":"Larissa"},
{"id":3, "nome":"Mateus"},
{"id":4, "nome":"Sofia"}
]

filme = [
{"cod":"F1", "nome":"Missão Final", "genero":"Ação"},
{"cod":"F2", "nome":"Amor Eterno", "genero":"Romance"},
{"cod":"F3", "nome":"Velocidade Máxima", "genero":"Ação"},
{"cod":"F4", "nome":"Mistério Sombrio", "genero":"Suspense"}
]

ingresso = [
{"id":1, "filmes":["F1","F3"]},
{"id":2, "filmes":["F2"]},
{"id":3, "filmes":["F1","F2"]},
{"id":4, "filmes":["F4"]}
]

def nomesclientessomentegenero (cliente, filme, ingresso, genero): 

    i = 0 
    resultado = [] 

    while i < len(cliente): 
        idcliente = cliente[i]["id"]
        nomecliente = cliente[i]["nome"]

        j = 0
        listafilmes = []
        while j < len(ingresso): 
            if ingresso[j]["id"] == idcliente:
                listafilmes = ingresso[j]["filmes"]
            j += 1

        k = 0
        filmesgenero = []
        while k < len(filme): 
            if filme[k]["genero"] == genero: 
                filmesgenero.append(filme[k]["cod"])
            k += 1

        l = 0
        while l < len(listafilmes):
            if listafilmes[l] in filmesgenero:
                resultado.append({"Nome do cliente: ": nomecliente, "Nome do filme: ": filme[l]["nome"]})
            l += 1
        
        i += 1
    return resultado
print(nomesclientessomentegenero(cliente, filme, ingresso, "Ação"))

            

            

            
            
