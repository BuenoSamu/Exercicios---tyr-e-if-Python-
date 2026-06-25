leitor = [
    {"cod":1, "nome":"Lucas" },
    {"cod":2, "nome":"Marina" },
    {"cod":3, "nome":"Felipe" },
    {"cod":4, "nome":"Camila" }
]

livro = [
    {"isbn":"L1", "titulo":"O Código", "autor":"Machado"},
    {"isbn":"L2", "titulo":"Aventura", "autor":"Paulo"},
    {"isbn":"L3", "titulo":"Mistério", "autor":"Machado"},
    {"isbn":"L4", "titulo":"Ciência", "autor":"Ana"}
]

emprestimo = [
    {"cod":1, "livros":["L1","L2"]},
    {"cod":2, "livros":["L4"]},
    {"cod":3, "livros":["L2"]},
    {"cod":4, "livros":["L1","L3"]}
]

def nomeLeitoresQueNuncaPegaramAutor(leitor, livro, emprestimo, autor): 

    i = 0 
    resultado = []

    while i < len(leitor): 
        iddoleitor = leitor[i]["cod"]

        j = 0
        listaisbn = []
        while j < len(livro): 
            if livro[j]["autor"] == autor:
                listaisbn.append(livro[j]["isbn"])
            j += 1
        
        pegouoautor = False
        k = 0 
        while k < len(emprestimo): 
            if emprestimo[k]["cod"] == iddoleitor: 
                    l= 0 
                    while l < len(emprestimo[k]["livros"]):
                        if emprestimo[k]["livros"][l] in listaisbn: 
                            leitorquenaoemprestouesseautor = emprestimo[k]["cod"]
                            pegouoautor = True
                        l += 1
            k += 1
        
        if not pegouoautor:
            nomedoleitor = leitor[i]["nome"]
            resultado.append({"Nome do cara que nunca emprestou esse autor: ": nomedoleitor})
        i += 1
    return resultado
print(nomeLeitoresQueNuncaPegaramAutor(leitor, livro, emprestimo, "Machado"))

