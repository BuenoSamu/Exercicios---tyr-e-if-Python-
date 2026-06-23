usuarios = [
    {"id": 1, "nome": "Pedro", "plano": "Premium"},
    {"id": 2, "nome": "Ana", "plano": "Básico"},
    {"id": 3, "nome": "Lucas", "plano": "Premium"}
]

filmes = [
    {"cod": "F1", "nome": "Avatar"},
    {"cod": "F2", "nome": "Titanic"},
    {"cod": "F3", "nome": "Vingadores"}
]

listas = [
    {"idUsuario": 1, "favoritos": ["F1"]},
    {"idUsuario": 1, "favoritos": ["F2", "F3"]},
    {"idUsuario": 3, "favoritos": ["F3"]}
]

def medialistasumfilme(usuarios, listas, plano):

    if len(usuarios) == 0 or len(listas) == 0:
        return None
    
    qtd = 0 
    soma = 0 

    i = 0 

    while i < len(usuarios):
        idusuario = usuarios[i]["id"]

        if usuarios[i]["plano"] == plano: 
            qtd += 1 
            cont = 0

            j = 0 
            while j < len(listas):
                if listas[j]["idUsuario"] == idusuario:
                    if len(listas[j]["favoritos"]) == 1: 
                        cont += 1
                j += 1
            
            soma += cont 
            media = soma / qtd

        i += 1
    return media

print(medialistasumfilme(usuarios, listas, "Premium"))