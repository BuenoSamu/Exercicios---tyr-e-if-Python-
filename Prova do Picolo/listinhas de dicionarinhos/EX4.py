livro = [
    {"cod": "L1", "titulo": "Dom Casmurro", "idAutor": 1},
    {"cod": "L2", "titulo": "1984", "idAutor": 2},
    {"cod": "L3", "titulo": "O Hobbit", "idAutor": 3},
    {"cod": "L4", "titulo": "Clean Code", "idAutor": 4}
]

autor = [
    {"id": 1, "nome": "Machado de Assis"},
    {"id": 2, "nome": "George Orwell"},
    {"id": 3, "nome": "J.R.R. Tolkien"},
    {"id": 4, "nome": "Robert C. Martin"}
]

emprestimo = [
    {"id": 1, "livros": ["L1", "L2"]},
    {"id": 2, "livros": ["L3"]},
]

def autorescomlivrosnuncaemprestados(autor, livro, emprestimo):

    livros_emprestados = []
    autores_com_livros = []
    resultado = []

    i = 0
    while i < len(emprestimo):

        j = 0
        while j < len(emprestimo[i]["livros"]):

            cod = emprestimo[i]["livros"][j]

            if cod not in livros_emprestados:
                livros_emprestados.append(cod)

            j += 1

        i += 1

    k = 0
    while k < len(livro):

        if livro[k]["cod"] in livros_emprestados:
            if livro[k]["idAutor"] not in autores_com_livros:
                autores_com_livros.append(livro[k]["idAutor"])

        k += 1

    z = 0
    while z < len(autor):

        if autor[z]["id"] not in autores_com_livros:
            resultado.append({
                "Autor que nao teve livros emprestados": autor[z]["nome"]
            })
        z += 1

    return resultado


print(autorescomlivrosnuncaemprestados(autor, livro, emprestimo))

