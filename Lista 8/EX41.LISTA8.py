usuarios = [
    {"id": 10, "nome": "Ana"},
    {"id": 11, "nome": "Bruno"},
    {"id": 12, "nome": "Carla"}
]

filmes = [
    {"cod": "F1", "nome": "Matrix"},
    {"cod": "F2", "nome": "Inception"},
    {"cod": "F3", "nome": "Interstellar"}
]

assistidos = [
    {"idUser": 10, "codFilme": ["F1"]},
    {"idUser": 11, "codFilme": ["F1", "F2"]},
    {"idUser": 12, "codFilme": ["F3"]}
]

def usuariosquevirammaisdeumfilme(usuarios, filmes, assistidos): 

    i = 0 
    resultado = []

    while i < len(assistidos): 

        idusuario = assistidos[i]["idUser"]
        listafilmes = assistidos[i]["codFilme"]

        if len(listafilmes) > 1: 
            nomedousuario = None
            nomedoFilme = None 

            j = 0 
            while j < len(usuarios): 
                if usuarios[j]["id"] == idusuario:
                    nomedousuario = usuarios[j]["nome"]
                    break
                j += 1 
            
            k = 0 
            while k < len(filmes): 
                if listafilmes[0] == filmes[k]["cod"]: 
                    nomedoFilme = filmes[k]["nome"]
                    break
                k += 1 
            
            if nomedoFilme and nomedousuario: 
                resultado.append({
                    "Nome do usuario: ": nomedousuario,
                    "Nome do filme: ": nomedoFilme
                })
        i += 1 
    return resultado
print(usuariosquevirammaisdeumfilme(usuarios, filmes, assistidos))
    