leitores = [
    {"id": 1, "nome": "Lucas", "email": "lucas@mail.com"},
    {"id": 2, "nome": "Marina", "email": "marina@mail.com"},
    {"id": 3, "nome": "Paulo", "email": "paulo@mail.com"},
    {"id": 4, "nome": "Rita", "email": "rita@mail.com"}
]

livros = [
    {"cod": "L1", "titulo": "Python Básico", "categoria": "Tecnologia"},
    {"cod": "L2", "titulo": "História do Brasil", "categoria": "História"},
    {"cod": "L3", "titulo": "Matemática Essencial", "categoria": "Educação"},
    {"cod": "L4", "titulo": "Romance na Praia", "categoria": "Ficção"}
]

emprestimos = [
    {"idLeitor": 1, "codLivro": "L1", "dias": 10, "devolvido": True},
    {"idLeitor": 1, "codLivro": "L2", "dias": 18, "devolvido": False},
    {"idLeitor": 2, "codLivro": "L3", "dias": 7, "devolvido": True},
    {"idLeitor": 3, "codLivro": "L4", "dias": 25, "devolvido": False},
    {"idLeitor": 4, "codLivro": "L1", "dias": 5, "devolvido": True}
]

def livrocomumemprestimoatrasado(leitores, livros, emprestimos):

    if len(leitores) == 0 or len(livros) == 0 or len(emprestimos) == 0:
        return None

    i = 0

    nomeleitores = []
    livrosatrasados = []

    while i < len(emprestimos):

        if emprestimos[i]["devolvido"] == False:
            
            idLeitor = emprestimos[i]["idLeitor"]
            codlivro = emprestimos[i]["codLivro"]
            

            j = 0
            while j < len(leitores):

                if leitores[j]["id"] == idLeitor:
                    nomeleitores.append(leitores[j]["nome"])
                j += 1

            k = 0 
            while k < len(livros):
                if livros[k]["cod"] == codlivro:
                    livrosatrasados.append(livros[k]["titulo"])
                k += 1
        i += 1

    return nomeleitores, livrosatrasados

print(livrocomumemprestimoatrasado(leitores, livros, emprestimos))


