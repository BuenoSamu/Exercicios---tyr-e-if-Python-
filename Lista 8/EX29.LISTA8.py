usuarios = [
    {"id": 1, "nome": "Lucas"},
    {"id": 2, "nome": "Marina"},
    {"id": 3, "nome": "Pedro"},
    {"id": 4, "nome": "Juliana"}
]

livros = [
    {"cod": "L01", "titulo": "Python Básico"},
    {"cod": "L02", "titulo": "Banco de Dados"},
    {"cod": "L03", "titulo": "Estruturas de Dados"},
    {"cod": "L04", "titulo": "Redes de Computadores"}
]

emprestimos = [
    {"idUsuario": 1, "livros": ["L01", "L03"]},
    {"idUsuario": 2, "livros": ["L02"]},
    {"idUsuario": 3, "livros": ["L04"]},
    {"idUsuario": 4, "livros": ["L01", "L02"]}
]

def livrosquecadaumemprestou(usuarios, livros, emprestimos):

    if len(livros) == 0 or len(usuarios) == 0 or len(emprestimos) == 0:
        return None

    resultado = []

    i = 0
    while i < len(emprestimos):

        id_usuario = emprestimos[i]["idUsuario"]
        lista_livros = emprestimos[i]["livros"]

        # acha nome do usuário
        nome_usuario = None
        j = 0
        while j < len(usuarios):
            if usuarios[j]["id"] == id_usuario:
                nome_usuario = usuarios[j]["nome"]
                break
            j += 1

        # percorre livros do empréstimo
        k = 0
        while k < len(lista_livros):
            cod_livro = lista_livros[k]

            nome_livro = None
            l = 0
            while l < len(livros):
                if livros[l]["cod"] == cod_livro:
                    nome_livro = livros[l]["titulo"]
                    break
                l += 1

            if nome_usuario is not None and nome_livro is not None:
                resultado.append({
                    "usuario": nome_usuario,
                    "livro": nome_livro
                })

            k += 1

        i += 1

    return resultado


print(livrosquecadaumemprestou(usuarios, livros, emprestimos))
