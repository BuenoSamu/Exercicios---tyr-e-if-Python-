usuarios = [
    {"id": 1, "nome": "Lucas", "cidade": "Campinas"},
    {"id": 2, "nome": "Ana", "cidade": "Limeira"},
    {"id": 3, "nome": "Pedro", "cidade": "Campinas"}
]

livros = [
    {"cod": "L1", "titulo": "Python"},
    {"cod": "L2", "titulo": "Banco de Dados"},
    {"cod": "L3", "titulo": "Redes"},
    {"cod": "L4", "titulo": "Kotlin"}
]

emprestimos = [
    {"idUsuario": 1, "livros": ["L1"]},
    {"idUsuario": 1, "livros": ["L2", "L3"]},
    {"idUsuario": 3, "livros": ["L1"]},
    {"idUsuario": 3, "livros": ["L2", "L4"]}
]

def mediaEmprestimosComUmLivro(usuarios, emprestimos, cidade):

    if len(usuarios) == 0 or len(emprestimos) == 0: 
        return None
    
    qtd = 0 
    soma = 0 
    
    i = 0 

    while i < len(usuarios):

        idusuario = usuarios[i]["id"]
        if usuarios[i]["cidade"] == cidade:
            qtd += 1
            cont  = 0

            j = 0 
            while j < len(emprestimos):
                if emprestimos[j]["idUsuario"] == idusuario:
                    if len(emprestimos[j]["livros"]) == 1: 
                        cont += 1
                j += 1
            
            if qtd == 0:
             return None
        
            soma += cont 
            media = soma / qtd
        i += 1
    return media

print(mediaEmprestimosComUmLivro(usuarios, emprestimos, "Campinas"))