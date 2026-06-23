usuarios = [
    {"id": 1, "nome": "Lucas"},
    {"id": 2, "nome": "Marina"},
    {"id": 3, "nome": "Pedro"}
]

livros = [
    {"cod": "L1", "titulo": "Python Básico"},
    {"cod": "L2", "titulo": "Algoritmos"},
    {"cod": "L3", "titulo": "Estruturas de Dados"}
]

emprestimos = [
    {"idUser": 1, "codLivro": ["L1"]},
    {"idUser": 2, "codLivro": ["L1", "L2"]},
    {"idUser": 3, "codLivro": ["L3"]}
]

def emprestimosdeapenasumlivro(usuarios, livros, emprestimos):

    i = 0 
    resultado = [] 

    while i < len(emprestimos):

        idusario = emprestimos[i]["idUser"]
        listalivros = emprestimos[i]["codLivro"]

        if len(listalivros) == 1:

            j = 0 
            nomeusuario = None
            while j < len(usuarios):
                if usuarios[j]["id"] == idusario: 
                    nomeusuario = usuarios[j]["nome"]
                j += 1 
            
            k = 0 
            nomelivro = None
            while k < len(livros):
                if listalivros[0] == livros[k]["cod"]:
                    nomelivro = livros[k]["titulo"]
                k +=1 

            if nomeusuario and nomelivro:
                resultado.append({
                    "Nome do leitor: ": nomeusuario,
                    "Nome do livro: ": nomelivro
                })
        i += 1 

    return resultado
print(emprestimosdeapenasumlivro(usuarios, livros, emprestimos))
           
